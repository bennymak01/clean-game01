#!/usr/bin/env python3
"""Pull search volume / keyword difficulty / related keywords from DataForSEO
Labs for every topic in the shared cluster CSV, and write results back into
new columns on the same CSV (single source of truth - no parallel file).

Runs inside .github/workflows/seo-keyword-research.yml on a GitHub-hosted
runner, since this can't be called from a network-restricted sandbox.
"""
import base64
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.request

LOGIN = os.environ["DATAFORSEO_LOGIN"]
PASSWORD = os.environ["DATAFORSEO_PASSWORD"]
AUTH = base64.b64encode(f"{LOGIN}:{PASSWORD}".encode()).decode()
BASE = "https://api.dataforseo.com"

# Hong Kong / Traditional Chinese
LOCATION_CODE = 2344
LANGUAGE_CODE = "zh-TW"  # "zh-Hant" is rejected by DataForSEO (40501 Invalid Field)

CSV_PATH = "seo/clean-com-hk-topical-cluster-plan.csv"

NEW_COLUMNS = [
    "dfs_recommended_keyword",
    "dfs_search_volume",
    "dfs_keyword_difficulty",
    "dfs_intent",
    "dfs_related_keywords",
]


def post(path, payload):
    req = urllib.request.Request(
        BASE + path,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Basic {AUTH}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def seed_keyword(topic_zh):
    # Strip parenthetical English asides and take the primary Chinese term
    # before any "/" (topics like "除霉/除霉菌" -> "除霉")
    return topic_zh.split("(")[0].split("/")[0].strip()


def main():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames)

    for col in NEW_COLUMNS:
        if col not in fieldnames:
            fieldnames.append(col)

    seeds = [seed_keyword(row["topic_zh"]) for row in rows]

    for row, seed in zip(rows, seeds):
        payload = [{
            "keywords": [seed],
            "location_code": LOCATION_CODE,
            "language_code": LANGUAGE_CODE,
            "limit": 10,
        }]
        try:
            # keyword_suggestions returns keywords that contain the seed
            # phrase (phrase-match) - keyword_ideas returns broader semantic
            # "ideas" that can drift wildly off-topic (e.g. the seed
            # "上門機洗地氈" carpet cleaning returned "洗衣機" washing
            # machine as its top-volume idea in an earlier run). Picking by
            # volume only makes sense once relevance is guaranteed.
            data = post("/v3/dataforseo_labs/google/keyword_suggestions/live", payload)
            top_status = f"{data.get('status_code')} {data.get('status_message')}"
            task = data["tasks"][0]
            task_status = f"{task.get('status_code')} {task.get('status_message')}"
            result = task.get("result") or [{}]
            items = result[0].get("items", []) if result[0] else []
            items = sorted(
                items,
                key=lambda x: (x.get("keyword_info") or {}).get("search_volume") or 0,
                reverse=True,
            )
            if items:
                best = items[0]
                row["dfs_recommended_keyword"] = best.get("keyword", "")
                row["dfs_search_volume"] = str((best.get("keyword_info") or {}).get("search_volume") or "")
                row["dfs_intent"] = (best.get("search_intent_info") or {}).get("main_intent") or ""
                row["dfs_related_keywords"] = "; ".join(i.get("keyword", "") for i in items[1:6])
            else:
                print(
                    f"No keyword_suggestions results for seed: {seed} "
                    f"| top status: {top_status} | task status: {task_status} "
                    f"| raw task (first 500 chars): {json.dumps(task)[:500]}",
                    file=sys.stderr,
                )
        except (urllib.error.HTTPError, urllib.error.URLError, KeyError, IndexError) as e:
            body = ""
            if isinstance(e, urllib.error.HTTPError):
                try:
                    body = e.read().decode("utf-8", errors="replace")[:500]
                except Exception:
                    pass
            print(f"keyword_suggestions failed for '{seed}': {e} | body: {body}", file=sys.stderr)
        time.sleep(1)  # be polite to the API / avoid rate limits

    try:
        kd_payload = [{
            "keywords": seeds,
            "location_code": LOCATION_CODE,
            "language_code": LANGUAGE_CODE,
        }]
        kd_data = post("/v3/dataforseo_labs/google/bulk_keyword_difficulty/live", kd_payload)
        kd_task = kd_data["tasks"][0]
        kd_result = kd_task.get("result") or [{}]
        kd_items = kd_result[0].get("items", []) if kd_result[0] else []
        if not kd_items:
            print(
                f"No bulk_keyword_difficulty items | "
                f"top status: {kd_data.get('status_code')} {kd_data.get('status_message')} | "
                f"task status: {kd_task.get('status_code')} {kd_task.get('status_message')} | "
                f"raw task (first 500 chars): {json.dumps(kd_task)[:500]}",
                file=sys.stderr,
            )
        kd_map = {i.get("keyword"): i.get("keyword_difficulty") for i in kd_items}
        for row, seed in zip(rows, seeds):
            row["dfs_keyword_difficulty"] = str(kd_map.get(seed, ""))
    except (urllib.error.HTTPError, urllib.error.URLError, KeyError, IndexError) as e:
        body = ""
        if isinstance(e, urllib.error.HTTPError):
            try:
                body = e.read().decode("utf-8", errors="replace")[:500]
            except Exception:
                pass
        print(f"bulk_keyword_difficulty failed: {e} | body: {body}", file=sys.stderr)

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Updated {len(rows)} rows with DataForSEO data.")


if __name__ == "__main__":
    main()

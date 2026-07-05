#!/usr/bin/env python3
"""Generate a blog hero image via Replicate (google/nano-banana-pro), save it
into images/blog/, and record the result back into the shared cluster CSV
(single source of truth - new columns, no parallel tracking file).

Runs inside .github/workflows/seo-generate-hero-image.yml on a GitHub-hosted
runner, since this can't be called from a network-restricted sandbox.

Required env vars:
  REPLICATE_API_TOKEN
  CLUSTER_ID   - row in seo/clean-com-hk-topical-cluster-plan.csv to update
  SLUG         - output filename stem -> images/blog/{SLUG}-hero.jpg
  PROMPT       - full image prompt (should already include any title text
                 to render, in Traditional Chinese, per Nano Banana Pro's
                 native text-rendering support)
Optional env vars:
  ASPECT_RATIO (default 16:9)
  RESOLUTION   (default 2K)
"""
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.request

API_TOKEN = os.environ["REPLICATE_API_TOKEN"]
CLUSTER_ID = os.environ["CLUSTER_ID"]
SLUG = os.environ["SLUG"]
PROMPT = os.environ["PROMPT"]
ASPECT_RATIO = os.environ.get("ASPECT_RATIO", "16:9")
RESOLUTION = os.environ.get("RESOLUTION", "2K")

CSV_PATH = "seo/clean-com-hk-topical-cluster-plan.csv"
OUT_DIR = "images/blog"
RAW_PATH = f"{OUT_DIR}/{SLUG}-hero-raw.png"
FINAL_PATH = f"{OUT_DIR}/{SLUG}-hero.jpg"

NEW_COLUMNS = [
    "hero_image_path",
    "hero_image_prompt",
    "hero_image_provider",
    "hero_image_generated_date",
    "hero_image_status",
]


def api_request(method, url, body=None, extra_headers=None):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }
    if extra_headers:
        headers.update(extra_headers)
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def create_prediction():
    return api_request(
        "POST",
        "https://api.replicate.com/v1/models/google/nano-banana-pro/predictions",
        body={
            "input": {
                "prompt": PROMPT,
                "aspect_ratio": ASPECT_RATIO,
                "resolution": RESOLUTION,
                "output_format": "png",
                "safety_filter_level": "block_only_high",
            }
        },
        extra_headers={"Prefer": "wait=60"},
    )


def poll_until_done(prediction):
    get_url = prediction["urls"]["get"]
    status = prediction["status"]
    attempts = 0
    while status not in ("succeeded", "failed", "canceled") and attempts < 30:
        time.sleep(5)
        prediction = api_request("GET", get_url)
        status = prediction["status"]
        attempts += 1
    return prediction


def download(url, path):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {API_TOKEN}"})
    with urllib.request.urlopen(req, timeout=120) as resp, open(path, "wb") as f:
        f.write(resp.read())


def update_csv(status):
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames)

    for col in NEW_COLUMNS:
        if col not in fieldnames:
            fieldnames.append(col)

    # A cluster can have multiple posts (a pillar + several supporting
    # pages), each with its own hero image - accumulate "slug:value"
    # entries per column instead of overwriting, so generating a second
    # image for an already-illustrated cluster doesn't erase the record
    # of the first one.
    def append_entry(existing, value):
        entry = f"{SLUG}:{value}"
        if not existing:
            return entry
        # Replace a prior entry for the same slug (re-roll case), else append
        parts = [p for p in existing.split("; ") if not p.startswith(f"{SLUG}:")]
        parts.append(entry)
        return "; ".join(parts)

    for row in rows:
        if row["cluster_id"] == CLUSTER_ID:
            row["hero_image_path"] = append_entry(row.get("hero_image_path", ""), FINAL_PATH if status == "succeeded" else status)
            row["hero_image_prompt"] = append_entry(row.get("hero_image_prompt", ""), PROMPT)
            row["hero_image_provider"] = append_entry(row.get("hero_image_provider", ""), "replicate/google/nano-banana-pro")
            row["hero_image_generated_date"] = append_entry(row.get("hero_image_generated_date", ""), time.strftime("%Y-%m-%d"))
            row["hero_image_status"] = append_entry(row.get("hero_image_status", ""), status)

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    try:
        prediction = create_prediction()
        prediction = poll_until_done(prediction)
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        body = ""
        if isinstance(e, urllib.error.HTTPError):
            try:
                body = e.read().decode("utf-8", errors="replace")[:500]
            except Exception:
                pass
        print(f"Replicate request failed: {e} | body: {body}", file=sys.stderr)
        update_csv("failed")
        sys.exit(1)

    if prediction["status"] != "succeeded":
        print(f"Prediction did not succeed: {json.dumps(prediction)[:800]}", file=sys.stderr)
        update_csv(prediction["status"])
        sys.exit(1)

    output = prediction["output"]
    image_url = output[0] if isinstance(output, list) else output
    download(image_url, RAW_PATH)
    print(f"Downloaded raw image to {RAW_PATH}")

    update_csv("succeeded")
    print(f"Updated CSV row for cluster_id={CLUSTER_ID}")
    # RAW_PATH is converted to FINAL_PATH (resize + jpeg) by the workflow's
    # ImageMagick step, not here, to keep this script dependency-free.


if __name__ == "__main__":
    main()

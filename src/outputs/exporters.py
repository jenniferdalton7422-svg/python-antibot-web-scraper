thonpython
import json
import os
import logging

OUTPUT_FILE = "data/sample.json"

def export_item(response):
 item = {
 "url": response.url,
 "title": response.xpath("//title/text()").get() or "",
 "metadata": {},
 "content": response.text[:1000],
 "additional_fields": {},
 }

 os.makedirs("data", exist_ok=True)

 try:
 with open(OUTPUT_FILE, "a") as f:
 f.write(json.dumps(item) + "\n")
 except Exception as e:
 logging.error(f"Failed to export item: {e}")

 return item
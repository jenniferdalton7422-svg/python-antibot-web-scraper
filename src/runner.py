thonpython
import json
import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.generic_spider import GenericSpider

logging.basicConfig(level=logging.INFO)

def load_inputs(path: str):
 try:
 with open(path, "r") as f:
 return [line.strip() for line in f.readlines() if line.strip()]
 except Exception as e:
 logging.error(f"Failed to load input file: {e}")
 return []

def main():
 settings = get_project_settings()

 process = CrawlerProcess(settings)

 urls = load_inputs("data/inputs.sample.txt")
 if not urls:
 logging.warning("No input URLs found. Exiting.")
 return

 process.crawl(GenericSpider, start_urls=urls)
 process.start()

if __name__ == "__main__":
 main()
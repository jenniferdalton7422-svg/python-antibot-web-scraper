thonpython
import scrapy
from outputs.exporters import export_item

class GenericSpider(scrapy.Spider):
 name = "generic_spider"

 def __init__(self, start_urls=None, **kwargs):
 super().__init__(**kwargs)
 self.start_urls = start_urls or []

 def parse(self, response):
 yield export_item(response)
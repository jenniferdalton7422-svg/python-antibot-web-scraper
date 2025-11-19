thonpython
import random
import logging
from scrapy import signals

class AntiBotMiddleware:
 def __init__(self, header_faker, session_manager):
 self.header_faker = header_faker
 self.session_manager = session_manager

 @classmethod
 def from_crawler(cls, crawler):
 hf = crawler.settings.get("HEADER_FAKER")
 sm = crawler.settings.get("SESSION_MANAGER")
 return cls(hf, sm)

 def process_request(self, request, spider):
 fake_headers = self.header_faker.generate()
 for k, v in fake_headers.items():
 request.headers[k] = v

 session = self.session_manager.get_session()
 request.headers["Cookie"] = session

 logging.debug("Applied antibot headers and session.")

 def process_response(self, request, response, spider):
 if response.status in (403, 429):
 logging.warning(f"Soft block detected at {response.url}, retrying.")
 new_request = request.copy()
 new_request.dont_filter = True
 return new_request
 return response
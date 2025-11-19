thonpython
import random
import logging

class ProxyRotator:
 def __init__(self, proxies=None):
 self.proxies = proxies or []

 def get_proxy(self):
 if not self.proxies:
 return None
 proxy = random.choice(self.proxies)
 logging.debug(f"Using proxy: {proxy}")
 return proxy
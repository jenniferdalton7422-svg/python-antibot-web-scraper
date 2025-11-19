thonpython
import random

class HeaderFaker:
 USER_AGENTS = [
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
 "Mozilla/5.0 (X11; Linux x86_64)",
 ]

 def generate(self):
 return {
 "User-Agent": random.choice(self.USER_AGENTS),
 "Accept-Language": "en-US,en;q=0.9",
 "Accept": "text/html,application/xhtml+xml",
 }
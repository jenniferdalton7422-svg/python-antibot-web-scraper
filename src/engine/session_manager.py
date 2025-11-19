thonpython
import random
import string

class SessionManager:
 def __init__(self):
 self.current_session = None

 def get_session(self):
 if not self.current_session:
 self.current_session = self._generate()
 return self.current_session

 def _generate(self):
 return "sessionid=" + "".join(random.choices(string.ascii_letters, k=24))
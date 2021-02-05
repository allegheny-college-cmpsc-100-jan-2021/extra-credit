import random

class Lock:

    def __init__(self):
        """Clas constructor"""
        self.key = random.randint(1,1000)
        self.core = hex(self.key)

    def pick(self, key):
        """Returns the result of a lockpick attempt
        
        Keyword arguments:
        key -- Key object
        """
        return self.core == key.core

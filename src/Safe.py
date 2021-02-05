from Lock import Lock

import random

class Safe:

    def __init__(self):
        """Class constructor"""
        self.lock = Lock()
        self.riches = random.randint(100, 1000)
        self.is_cracked = False

    def __str__(self):
        """Prints the outcome of current safe's status"""
        if #TODO Test is_cracked property of this copy of Safe:
            return "$" * self.riches
        return "Nice try."

    def crack(self, key):
        """Attempts to break into the safe!
        
        Keyword arguments:
        key -- key object to try against the lock
        """
        # TODO: Check if the incoming key picks safe's lock
        #       using the pick method of the lock object
        # TODO: If true, set the is_cracked property of this copy
        #       of Safe to True
        # TODO: Return the value of this copy's is_cracked variable

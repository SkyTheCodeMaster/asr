# Provides various intent searching functions.

from nltk.tokenize import sent_tokenize,word_tokenize

class Intent:
  def __init__(self,text:str,intents:list):
    self.text = text
    self.intents = intents

  def keyword(self):
    """Finds the intent of the provided text via keyword search.
It loops over the list, and does a simple `if keyword in text return keyword` check.
It returns a list of all found keywords."""
    return [keyword for keyword in self.intents if keyword in self.text]
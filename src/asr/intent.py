# Provides various intent searching functions.

from nltk.tokenize import sent_tokenize,word_tokenize
from . import nlp

natlang = nlp.NLP()

class Intent:
  def __init__(self,text:str,intents:list):
    self.text = text
    self.intents = intents

  def keyword(self):
    """Finds the intent of the provided text via keyword search.
It loops over the list, and does a simple `if keyword in text return keyword` check.
It returns a list of all found keywords."""
    return [keyword for keyword in self.intents if keyword in self.text]

  def extendedKeyword(self):
    """Similar to normal keyword, it searches the provided text via keyword. This also returns a dictionary with extra data (persons, locations, etc) found in the text."""
    keywords = [keyword for keyword in self.intents if keyword in self.text]
    nes = natlang.extractNeTyped(self.text)
    types = {}
    for tag in nes:
      if not tag["type"] in types:
        types[tag["type"]] = [tag["name"]]
      else:
        types[tag["type"]].append(tag["name"])
    return {"keywords":keywords,"nes":types}

def findIntent(text,intents,*,method="extendedKeyword"):
  """Find the intents of a provided text
text:str The text you want to find the intent of
intents:list The valid intents to search for.

method:str The method of finding intents. Must be: `keyword`, `extendedKeyword`"""
  finder = Intent(text,intents)
  return getattr(finder,method,"extendedKeyword")()
import nltk
from nltk.tokenize import word_tokenize

import anltk

class NLP:
  def extractNe(self,text):
    words = word_tokenize(text)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags,binary=True)
    return set(
      " ".join(i[0] for i in t)
      for t in tree
      if hasattr(t,"label") and t.label() == "NE"
    )

  def extractNeTyped(self,text):
    words = word_tokenize(text)
    tags = nltk.pos_tag(words)
    bTree = nltk.ne_chunk(tags,binary=True)
    tree = nltk.ne_chunk(tags)
    ntags = []
    for i,v in enumerate(bTree):
      if hasattr(v,"label") and v.label() == "NE":
        t = tree[i]
        ntags.append({"type":t.label(),"name":t[0]})
    return ntags

  async def fullLemmatize(self,text):
    words = word_tokenize(text)
    return [await anltk.lemmatize(word) for word in words]
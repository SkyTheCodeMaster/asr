# Provides async versions of heavy nltk functions

import asyncio
import concurrent.futures

import nltk
from nltk.stem import WordNetLemmatizer

_lemmatizer = WordNetLemmatizer()

async def run(callable,*,executor:concurrent.futures.ProcessPoolExecutor=concurrent.futures.ProcessPoolExecutor):
  loop = asyncio.get_running_loop()
  with executor() as pool:
    return loop.run_in_executor(pool,callable)

async def lemmatize(word:str,**kwargs):
  return await run(lambda:_lemmatizer(word),**kwargs)

async def download(package:str,**kwargs):
  return await run(lambda:nltk.download(package),**kwargs)
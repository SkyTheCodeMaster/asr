# Async Speech Recognition via the PocketSphinx offline reader thing
import asyncio
import concurrent.futures
from typing import Union

import speech_recognition as sr

class Speech:
  def __init__(self,*,mic=Union[str,int,None]):
    self.mic = sr.Microphone()
    self.recognizer = sr.Recognizer()
    if type(mic) is str:
      for i,name in enumerate(sr.Microphone.list_microphone_names()):
        if name == mic:
          self.mic = sr.Microphone(device_index=i)
    elif type(mic) is int:
      self.mic = sr.Microphone(device_index=mic)

  def _getMicInput(self):
    with self.mic as source:
      return self.recognizer.listen(source)

  def _getText(self,audio):
    try:
      return self.recognizer.recognize_sphinx(audio)
    except sr.UnknownValueError:
      return None

  def _full(self):
    return self._getText(self._getMicInput())

  async def _getAsyncMicInput(self,*,executor:concurrent.futures.ProcessPoolExecutor=concurrent.futures.ProcessPoolExecutor):
    loop = asyncio.get_running_loop()
    with executor() as pool:
      return loop.run_in_executor(pool,self._getMicInput)

  async def _getAsyncText(self,audio,*,executor:concurrent.futures.ProcessPoolExecutor=concurrent.futures.ProcessPoolExecutor):
    loop = asyncio.get_running_loop()
    with executor() as pool:
      return loop.run_in_executor(pool,lambda a: self._getText(a))

  async def _asyncFull(self,*,executor:concurrent.futures.ProcessPoolExecutor=concurrent.futures.ProcessPoolExecutor):
    return await self._getAsyncText(await self._getAsyncMicInput())
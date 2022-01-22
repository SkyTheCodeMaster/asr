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
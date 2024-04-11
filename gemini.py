import pathlib
import textwrap
import time

import google.generativeai as genai


from IPython import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

try:
    # Or use `os.getenv('API_KEY')` to fetch an environment variable.
    GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
except ImportError:
    import os
    GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

genai.configure(api_key="AIzaSyAKmuc5YClNDyJ5lU-hv9h8TgHpaBeeuGQ")
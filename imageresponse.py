import re, urllib
import pandas as pd
from bs4 import BeautifulSoup
import json
import requests
import jsonreader



query = "dogs"
r = requests.get('https://api.duckduckgo.com/?q=dogecoin&format=json&pretty=1&no_html=1&skip_disambig=1')
data = r.json()


paster=jsonreader.extract_element_from_json(data, (["RelatedTopics"]))
paster2=jsonreader.extract_element_from_json(paster, (["Link"]))
print(paster2)
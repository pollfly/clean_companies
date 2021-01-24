# NOT DONE YET - MAY DELETE
import requests
import urllib.request
import sqlite3
import time
from bs4 import BeautifulSoup

url = "https://www.business-humanrights.org/en/companies/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

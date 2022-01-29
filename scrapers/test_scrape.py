import requests
from bs4 import BeautifulSoup

url_to_parse = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url_to_parse)
print(response)
response_text = response.text
soup = BeautifulSoup(response_text, 'lxml')
print(soup.prettify())
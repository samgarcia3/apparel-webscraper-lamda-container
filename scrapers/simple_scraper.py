import requests
from bs4 import BeautifulSoup


res = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
bs = BeautifulSoup(res.text, 'lxml')
print(bs.find("p", class_=None).text)

#test
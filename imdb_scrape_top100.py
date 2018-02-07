from bs4 import BeautifulSoup
import requests
import re
from time import sleep
from datetime import datetime

def getGoldPrice():
    url = "http://www.imdb.com/search/name?gender=male,female&ref_=nv_cel_m_3"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    js_text = soup.find_all('script', type="text/javascript")[10]
    js_text = js_text.string
    regex = re.compile('"ask":{"css":"minus","price":"(.*)","performance":-1}},"G')
    price = re.findall(regex, js_text)
    return price

with open("person.out","w") as f:
    for x in range(0,10):
        sNow = datetime.now().strftime("%I:%M:%S%p")
        f.write("{0}, {1} \n ".format(sNow, getGoldPrice()))
        sleep(59)
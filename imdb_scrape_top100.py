from bs4 import BeautifulSoup
import requests

r = requests.get('http://www.imdb.com/search/name?gender=male,female&ref_=nv_cel_m_3')
soup = BeautifulSoup(r.text, 'lxml')

actress = soup.find_all("div", class_="lister-item-content")
# print(actress[0])

# Used to test the actual text being derived for a field
print(actress[0].find("p", "text-muted").get_text(strip = True))
print(actress[0].find("p", "text-muted").string())


top100 = {}
for element in actress:
    top100[element.find("a").get_text(strip = True)] = {}

for element in actress:
    name = element.find("a").get_text(strip = True)
    top100[element.find("a").get_text(strip = True)]["Name"] = name

for element in actress:
    spot = element.find("span", "lister-item-index").get_text(strip = True)
    top100[element.find("a").get_text(strip = True)]["Ranking"] = spot

for element in actress:
    movie = element.find("p", "text-muted").find("a").get_text(strip = True)
    top100[element.find("a").get_text(strip = True)]["Movie"] = movie

for element in actress:
    movie = element.find("p", "text-muted").find("a").get_text(strip = True)
    top100[element.find("a").get_text(strip = True)]["Movie"] = movie

'''
for item in top100.keys():
    print("Ranking:\t" + top100[item]["Ranking"] + "\nName:\t" + top100[item]["Name"] + "\nMovie:\t\t" + top100[item]["Movie"] + "\n")
    '''
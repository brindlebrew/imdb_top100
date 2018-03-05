from bs4 import BeautifulSoup
import requests
import json
import csv

pages = ['http://www.imdb.com/search/name?gender=male,female&ref_=nv_cel_m_3', 'http://www.imdb.com/search/name?gender=male,female&start=51&ref_=rlm']

top100 = {}

for item in pages:

    r = requests.get(item)
    soup = BeautifulSoup(r.text, 'lxml')

    actress = soup.find_all("div", class_="lister-item-content")
    # print(actress[0])

    # Used to test the actual text being derived for a field
    #print(actress[0].find("p", "text-muted").get_text(strip = True).split(sep, 1)[0])

    # Sets up the seperator for the actor / actress step.
    sep = "|"


    for element in actress:
        top100[element.find("a").get_text(strip = True)] = {}

    for element in actress:
        name = element.find("a").get_text(strip = True)
        top100[element.find("a").get_text(strip = True)]["Name"] = name

    for element in actress:
        spot = element.find("span", "lister-item-index").get_text(strip = True)
        top100[element.find("a").get_text(strip = True)]["Ranking"] = spot

    for element in actress:
        gender = element.find("p", "text-muted").get_text(strip = True).split(sep, 1)[0]
        top100[element.find("a").get_text(strip = True)]["Gender"] = gender

    for element in actress:
        movie = element.find("p", "text-muted").find("a").get_text(strip = True)
        top100[element.find("a").get_text(strip = True)]["Movie"] = movie

'''
# Used for writting the output to screen for testing
for item in top100.keys():
    print("Ranking:\t" + top100[item]["Ranking"] + "\nName:\t\t" + top100[item]["Name"] + "\nGender:\t\t" + top100[item]["Gender"] + "\nMovie:\t\t" + top100[item]["Movie"] + "\n")
'''


with open("imdb_status.csv", "w") as toWrite:
    writer = csv.writer(toWrite, delimiter=",")
    writer.writerow(["drop", "name", "ranking", "gender", "movie"])
    for a in top100.keys():
        writer.writerow([a.encode("utf-8"), top100[a]["Name"], top100[a]["Ranking"], top100[a]["Gender"], top100[a]["Movie"]])

with open("imdb_status.json", "w") as writeJSON:
    json.dump(top100, writeJSON)
import requests
from bs4 import BeautifulSoup

url = "https://aviation-safety.net/"


headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
title = ["Date", "Airplane", "Fligth", "Airline", "Fatalities", "Airport"]
#
# def get_html(url):
#     response = urllib.request.urlopen(url)
#     return response.read()
#
#
# def parse(html):
#     soup = BeautifulSoup(html, features="html.parser")
table = soup.find_all('table')
rows = table[2].find_all('tr')
result = []
for i in rows:
    temp = []
    for j in i.find_all('td'):
        temp.append(str(j.text).strip())
    result.append(temp)
# print(result)

def to_string(arr):
    res = ""
    for i in arr:
        for j in i[:-2]:
            res += str(j) + " "
        res += "\n"
    return res

print(to_string(result))
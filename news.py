import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser

url = "https://aviation-safety.net/"

headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
titles = ["Date", "Airplane", "Fligth", "Airline", "Fatalities", "Airport"]
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
    """Transforms data to string"""
    res = ""
    for i in arr:
        for j in i[:-2]:
            res += str(j) + " "
        res += "\n"
    return res


def news_f():
    """Shows news with interface"""
    root2 = Tk()
    root2.title('News')
    root2.iconbitmap('airplane.ico')
    main2 = Frame(root2, bg="aliceblue")
    main2.pack(fill=X)
    title = Label(main2, width=50, text="Latest Safety Occurrences", font=('Marcellus SC', 12), bg='aliceblue',
                  borderwidth=2,
                  highlightbackground="deepskyblue",
                  highlightcolor="deepskyblue",
                  highlightthickness=1)
    title.grid(row=0, column=0)
    link_so = 'https://aviation-safety.net/'
    link_nn = 'http://www.airport-world.com/'

    def go_so():
        """Opens browser first link"""
        webbrowser.open(link_so)

    def go_nn():
        """Opens browser first link"""
        webbrowser.open(link_nn)

    but_so = Button(main2, bg='skyblue', text="Aviation safety news", command=go_so)
    but_nn = Button(main2, bg='skyblue', text="Airport world news", command=go_nn)
    but_so.grid(row=0, column=1)
    but_nn.grid(row=0, column=2)
    but_so.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
    but_so.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))
    but_nn.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
    but_nn.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))
    table2 = Frame(root2, bg='aliceblue', borderwidth=2, highlightbackground="deepskyblue",
                   highlightcolor="deepskyblue",
                   highlightthickness=3)
    table2.pack()
    for i in range(6):
        Label(table2, bg='aliceblue', text=titles[i]).grid(row=1, column=i)
    for i in range(4):
        for j in range(6):
            Label(table2, bg='aliceblue', text=result[i][j]).grid(row=i + 2, column=j)
    root2.mainloop()

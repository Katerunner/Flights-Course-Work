from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen


# ============== Loading screen ===============

def internet_on():
    try:
        urlopen('https://www.google.com/', timeout=10)
        return True
    except:
        return False


load_root = Tk()
load_root.title('Flight Status')
load_root.iconbitmap('airplane.ico')
load_root.geometry("900x500")
load_root.state('zoomed')
load_image = PhotoImage(file="load.gif")
load_label = Label(load_root, image=load_image)
load_label.place(x=0, y=0, relwidth=1, relheight=1)
width = load_root.winfo_screenwidth()
height = load_root.winfo_screenheight()
load_root.geometry("{0}x{1}+0+0".format(width, height))
# load_root.overrideredirect(True)
load_root.update()
if not internet_on():
    load_label.destroy()
    del load_label
    load_image = PhotoImage(file="no_inter.gif")
    load_label = Label(load_root, image=load_image)
    load_label.place(x=0, y=0, relwidth=1, relheight=1)
    load_root.update()
    message_l = Label(load_root, font=('Marcellus SC', 12), bg = 'yellow', text = "No internet connection. Try again when the internet is available")
    exit_but = Button(load_root, font=('Marcellus SC', 12), bg = 'red', text = "Exit", command = quit)
    exit_but.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
    exit_but.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))
    message_l.place(x=width/2.8, y=height/2 + 200)
    exit_but.place(x=width/2, y=height/2 + 250)
    load_root.mainloop()

# ============== Imports ==============

try:
    import airports
    import aircrafts
    import delay
    import weather
    from functools import partial
    import map
    import datetime
    import time
    import news
    from coordinates import Corray
    import webbrowser
    import os
    import urllib.request
    import io
    import parsik
    import copy
    import searchik

except Exception as b:
    print("Please check all files or install missing")
    raise b

# TODO: No internet connection

# ============== Starting window creation ==============

codes = [0, 0]
airport_names = []
airs = ['Nothing', 'Nothing']
country = ''
cur_code = ''
air = ''
date = ''

try:
    load_root.destroy()
except TclError:
    quit()
root = Tk()
# root.tk.call('encoding', 'system', 'utf-8')
airnet = airports.AirportsNet()
aicnet = aircrafts.AircraftsNet()
root.title('Flight Status')
root.iconbitmap('airplane.ico')
root.geometry("900x500")
root.state('zoomed')
background_image = PhotoImage(file="bg0.gif")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("{0}x{1}+0+0".format(width, height))
main = Frame(root, bg='aliceblue', borderwidth=2, highlightbackground="deepskyblue", highlightcolor="deepskyblue",
             highlightthickness=3)
table = Frame(main, bg='aliceblue')
main.pack()


def git_f():
    """Opens github link in browser"""
    webbrowser.open("https://github.com/Katerunner/Flights-Course-Work")


def weath_f():
    """Opens weather link in the browser"""
    webbrowser.open("https://weather.com")


weath_b = Button(root, height=2, width=12, text="Weather", font=('Marcellus SC', 12), bg='skyblue',
                 command=weath_f)
weath_b.place(x=3, y=600)
weath_b.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
weath_b.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))

news_b = Button(root, height=2, width=12, text="Airport News", font=('Marcellus SC', 12), bg='skyblue',
                command=news.news_f)
news_b.place(x=3, y=670)
news_b.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
news_b.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))
git_b = Button(root, height=2, width=12, text="GitHub Repo.", font=('Marcellus SC', 12), bg='skyblue', command=git_f)
git_b.place(x=3, y=740)
git_b.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
git_b.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))

top_menu = 0
menubar = 0


def info_wait_start():
    """Displays info screen while loading flights"""
    global info_tab, info_f
    info_f = Frame(root, borderwidth=2, highlightbackground="yellow", highlightcolor="yellow",
                   highlightthickness=3)
    info_f.place(x=1600, y=100)
    info_tab = Label(info_f,
                     text="Please wait\n\nTry not to click\nLoading can take much time\n\nThis message will disappear\nafter calculation finishes\n\n{}",
                     bg="lemonchiffon", width=25, height=10)
    info_tab['text'] = info_tab['text'].format("|")
    info_tab.pack()

    def loading():
        """Changes the loading symbol"""
        global info_tab
        if info_tab['text'][-1] == "|":
            text = "\\"
        elif info_tab['text'][-1] == "\\":
            text = u"\u2014"
        elif info_tab['text'][-1] == u"\u2014":
            text = "/"
        elif info_tab['text'][-1] == "/":
            text = "|"
        info_tab.config(text=info_tab['text'][:-1] + text)
        info_tab.after(200, loading)

    try:
        loading()
    except Exception as a:
        print(a)


def info_wait_destroy():
    """Destroys info screen"""
    info_f.destroy()


def donothing():
    """Updates map and opens the html map in browser"""
    try:
        map.update_map(codes[0], codes[1])
        webbrowser.open('file://' + os.path.realpath('map.html'))
    except:
        global info_map_tab, info_map, info_map_time
        info_map_time = time.time()
        info_map = Frame(root, borderwidth=2, highlightbackground="yellow", highlightcolor="yellow",
                         highlightthickness=3)
        info_map.place(x=100, y=100)
        info_map_tab = Label(info_map,
                             text="To see the map\nyou need to\nchoose the route first",
                             bg="lemonchiffon", width=25, height=5)
        info_map_tab.pack()

        def loading_map():
            global info_map_tab, info_map_time, info_map
            if time.time() > info_map_time + 3.5:
                info_map.destroy()
            info_map_tab.after(200, loading_map)

        try:
            loading_map()
        except Exception as a:
            print(a)


def overd_t():
    """Makes program fullscreen"""
    root.overrideredirect(True)


def overd_f():
    """Makes program windowed"""
    root.overrideredirect(False)


def but_menu():
    """Displays big button top menu"""
    global main, top_menu, menubar, time_date, time1, datik, but_list

    try:
        menubar.destroy()
        top_menu.destroy()
    except:
        pass

    root.config(menu=None)

    top_menu = Frame(root, bg='aliceblue', width=width, borderwidth=2, highlightbackground="deepskyblue",
                     highlightcolor="deepskyblue",
                     highlightthickness=1)
    main.pack_forget()
    top_menu.pack(fill=X)
    Frame(root, height=4).pack(fill=Y)
    main.pack()

    # Marcellus Sk
    im_showflight = Image.open("map_show_b.jpg")
    image_showflight = ImageTk.PhotoImage(im_showflight)
    showflight = Button(top_menu, bg='skyblue', width=328, height=33, text="Show flight on map", cursor="hand2",
                        image=image_showflight,
                        command=donothing)
    showflight.image = image_showflight
    showflight.grid(column=0, row=0)

    im_fulls = Image.open("fulls_b.jpg")
    image_fulls = ImageTk.PhotoImage(im_fulls)
    fulls = Button(top_menu, bg='skyblue', width=328, height=33, text="Fullscreen view ", cursor="hand2",
                   image=image_fulls,
                   command=overd_t)
    fulls.image = image_fulls
    fulls.grid(column=1, row=0)

    im_wind = Image.open("wind_b.jpg")
    image_wind = ImageTk.PhotoImage(im_wind)
    wind = Button(top_menu, bg='skyblue', width=328, height=33, text="Windowed view", cursor="hand2", image=image_wind,
                  command=overd_f)
    wind.image = image_wind
    wind.grid(column=2, row=0)

    im_menu = Image.open("menu_b.jpg")
    image_menu = ImageTk.PhotoImage(im_menu)
    menu_b = Button(top_menu, bg='skyblue', width=328, height=33, text="Change to menubar", cursor="hand2",
                    image=image_menu, command=menu)
    menu_b.image = image_menu
    menu_b.grid(column=3, row=0)

    time1 = ''
    datik = ''

    Label(top_menu, width=7, bg='aliceblue', text="Today:", font=('Marcellus SC', 12)).grid(column=4, row=0)
    Label(top_menu, width=7, bg='aliceblue', text="Time:", font=('Marcellus SC', 12)).grid(column=6, row=0)

    date_w = Label(top_menu, bg='aliceblue', font=('Marcellus SC', 12), width=9)
    date_w.grid(column=5, row=0)

    time_w = Label(top_menu, bg='aliceblue', font=('Marcellus SC', 12), width=8)
    time_w.grid(column=7, row=0)

    def tick():
        """Updates time each second"""
        global time1
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            time_w.config(text=time1)
        time_w.after(200, tick)

    def bam():
        """Updates date"""
        global datik
        date2 = datetime.date.today()
        if date2 != datik:
            datik = date2
            date_w.config(text=datik)
        date_w.after(5000, bam)

    try:
        tick()
        bam()
    except Exception as a:
        print(a)

    Label(top_menu, bg='aliceblue', width=11).grid(column=8, row=0)
    im_exit = Image.open("exit_b.jpg")
    image_exit = ImageTk.PhotoImage(im_exit)
    exit_b = Button(top_menu, bg='red', image=image_exit, width=43, height=33, text="Exit", cursor="hand2",
                    command=root.quit)
    exit_b.image = image_exit
    exit_b.grid(column=9, row=0)

    but_list = [showflight, fulls, wind, menu_b, exit_b]

    try:
        but_manage()
    except:
        pass


def menu():
    """Displays dtandart program menu"""
    global top_menu, menubar

    try:
        top_menu.destroy()
    except:
        pass

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Show flight on map", command=donothing)
    filemenu.add_command(label="Fullscreen view", command=overd_t)
    filemenu.add_command(label="Windowed mode", command=overd_f)
    filemenu.add_command(label="Change to big menu", command=but_menu)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo")

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)


menu()
but_menu()
print(air)


def link_to_flight(flight):
    """Opens webpage with more information for certain flight"""
    link = 'https://flightaware.com/live/flight/{}'.format(aircrafts.format_flight(flight))
    webbrowser.open(link)


def pre_final_cur(inputed_date):
    """Main function that displays all flights for given route and the delay rates for each of them"""
    global date, table, pref, canvas

    def gf_f(c1, c2, indate):
        """Activates and opens Google Flights page for certain route"""
        if not indate:
            today = datetime.datetime.today()
            tomorrow = today + datetime.timedelta(1)
            indate = datetime.datetime.strftime(tomorrow, '%Y-%m-%d')
        webbrowser.open("https://www.google.com/flights?flt={}.{}.{}".format(c1, c2, indate))

    gf_b = Button(root, height=2, width=12, text="Google Flights", font=('Marcellus SC', 12), bg='skyblue',
                  command=lambda: gf_f(codes[0], codes[1], inputed_date))
    gf_b.place(x=3, y=810)
    gf_b.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
    gf_b.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))

    info_wait_start()
    root.update()
    now = datetime.datetime.now()
    try:
        canvas.destroy()
        table.destroy()
    except:
        pass
    canvas = Canvas(main, bg="white")
    table = Frame(canvas, bg="white")
    canvas.grid(row=11, columnspan=2)
    table.pack(side="left", fill="y")
    date = str(now.day) + "." + str(now.month) + "." + str(now.year)
    pref = Label(main, text="Flights from " + str(codes[0]) + " to " + str(codes[1]) + " on " + date + ":", width=112,
                 height=2, bg="lightblue")
    pref.grid(row=10, columnspan=2)
    te_1 = parsik.flight(codes[0], codes[1], date)
    # No internet
    print(te_1)
    if te_1 != ['Nothing found']:
        scrollbar = Scrollbar(table)
        print(airnet.find_by_airname(airs[1]).code_3)
        print(airnet.find_by_airname(airs[1]).lat)
        print(airnet.find_by_airname(airs[1]).lon)

        weath = weather.Weather()
        temp = airnet.find_by_airname(airs[1])
        weathik = Corray(temp.lat, temp.lon)
        weath.weather_coord_forecast(weathik, inputed_date)
        delik = delay.Delay(temp.code_3).alter_del()
        delik += weath.danger()

        for_info = []
        for_info.clear()
        for i in range(len(te_1)):
            airline = te_1[i][1]
            try:
                airline = airline[:airline.index(' on ')]
            except:
                pass
            for_info.append(te_1[i][0])
            print("\n______________TE1_____________")
            print(te_1)
            try:
                agp = aircrafts.get_plane(te_1[i][0])
                print(agp)
                deli = aicnet.delay_extender(delik, agp[0])
            except Exception as a:
                raise a

            if deli == 0:
                color = "white"
            elif deli < 0.05:
                color = "green"
            elif 0.04 < deli < 0.07:
                color = "#B2C248"
            elif 0.06 < deli < 0.12:
                color = "yellow"
            elif 0.11 < deli < 0.16:
                color = "#E56717"
            elif deli > 0.15:
                color = "red"
            else:
                color = "white"
            Label(table, text=te_1[i][0], width=9, bg="aliceblue", relief=GROOVE, borderwidth=2,
                  highlightbackground="deepskyblue", highlightcolor="deepskyblue", ).grid(row=i, column=1)

            # im_info = Image.open("info_b.jpg")
            # image_info = ImageTk.PhotoImage(im_info)
            url = agp[1]
            raw_data = urllib.request.urlopen(url).read()
            im_airline = Image.open(io.BytesIO(raw_data))
            im_airline = im_airline.resize((22, 22), Image.ANTIALIAS)
            image_airline = ImageTk.PhotoImage(im_airline)
            airline_l = Label(table, text="I", image=image_airline, width=20, height=22, bg="aliceblue", relief=GROOVE,
                              borderwidth=2,
                              highlightbackground="deepskyblue", highlightcolor="deepskyblue", )
            airline_l.image = image_airline
            airline_l.grid(row=i, column=2)

            Label(table, text=airline, width=46, bg="aliceblue", justify=LEFT, relief=GROOVE, borderwidth=2,
                  highlightbackground="deepskyblue", highlightcolor="deepskyblue", ).grid(row=i, column=3)
            Label(table, text=airnet.find_by_airname(airs[0]).city + " " + te_1[i][2], width=17, bg="aliceblue",
                  relief=GROOVE, borderwidth=2,
                  highlightbackground="deepskyblue", highlightcolor="deepskyblue", ).grid(row=i, column=4)
            Label(table, text=airnet.find_by_airname(airs[1]).city + " " + te_1[i][3], width=17, bg="aliceblue",
                  relief=GROOVE, borderwidth=2,
                  highlightbackground="deepskyblue", highlightcolor="deepskyblue", ).grid(row=i, column=5)
            Label(table, text=round(float(deli * 5), 3), width=6, bg=color,
                  relief=GROOVE, borderwidth=2,
                  highlightbackground="deepskyblue", highlightcolor="deepskyblue", ).grid(row=i, column=6)

            action_with_arg = partial(link_to_flight, for_info[i])
            im_info = Image.open("info_b.jpg")
            image_info = ImageTk.PhotoImage(im_info)
            info_b = Button(table, text=i, width=83, height=20, image=image_info, bg="aliceblue", justify=LEFT,
                            relief=GROOVE, borderwidth=2,
                            highlightbackground="deepskyblue", highlightcolor="deepskyblue", command=action_with_arg)
            info_b.image = image_info
            info_b.grid(row=i, column=0)
            info_b.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
            info_b.bind("<Leave>", lambda e: e.widget.config(relief=GROOVE))
            root.update()
    else:
        print("i'm here")
        Label(table, text="Nothing found", width=112, bg='yellow').grid(row=0, column=0)
    info_wait_destroy()


def set_depar():
    """Sets departure airport"""
    global cur_code
    codes[0] = cur_code
    airs[0] = air
    L2 = Label(main, text='From: ' + air + " (" + str(codes[0]) + ")", width=55, bg='aliceblue')
    L2.grid(row=6)
    date_ch()
    print(codes)


def set_arriv():
    """Sets arrival airport"""
    global cur_code
    codes[1] = cur_code
    airs[1] = air
    L3 = Label(main, text='To: ' + air + " (" + str(codes[1]) + ")", width=55, bg='aliceblue')
    L3.grid(row=6, column=1)
    date_ch()
    print(codes)


def upd_con():
    """Dispalys airports for chosen country"""
    global B2, Lb2, airport_names, country, cities, cit_copy, En2, text2
    try:
        L1.grid(row=4)
        temp = Lb1.curselection()[0]
        temp_l.destroy()
        Lb2.destroy()
        En2.destroy()
        text2.set("Type airport to search")
        En2 = Entry(main, width=55, textvariable=text2, fg="gray")
        En2.bind("<Button-1>", lambda e: text2.set(""))
        En2.grid(row=1, column=1)
    except:
        pass
    print(Lb1.curselection()[0])
    cursl = sorted([(i.city, i.name) for i in airnet.airdat if i.country == countries[::-1][Lb1.curselection()[0]]])
    country = cursl
    # print(cursl)
    Lb2 = Listbox(main, width=55, cursor="sb_right_arrow")
    B2.destroy()
    B2 = Button(main, text='Choose airport', cursor="hand2", width=55, command=upd_air, bg='skyblue')
    airport_names = []
    cities = []
    for i in cursl:
        cities.append(i[1])

    for i in cities:
        Lb2.insert(END, airnet.find_by_airname(i).city + ", " + str(i))

    cit_copy = copy.copy(cities)

    def lb2_update():
        """Updates cities and airports"""
        global cities, cit_copy
        if cit_copy != cities:
            # print("Copy:", cit_copy)
            # print("Actual:", cities)
            Lb2.delete(0, END)
            for i in cities[::-1]:
                Lb2.insert(END, airnet.find_by_airname(i).city + ", " + str(i))
            cit_copy = copy.copy(cities)
        Lb2.after(200, lb2_update)

    try:
        lb2_update()
    except Exception as a:
        print("Error or Exception:", a)

    def en2_update():
        """Updates search entry"""
        global cities, cit_copy
        if text2.get() == "" or text2.get() == "Type airport to search":
            cities = []
            for i in cursl[::-1]:
                cities.append(i[1])
        elif text2.get() != "Type airport to search" and text2.get() != "":
            cities = searchik.searchik(cities, text2.get())
        En2.after(200, en2_update)

    try:
        en2_update()
    except Exception as a:
        print(a)

    Lb2.grid(row=2, column=1)
    B2.grid(row=3, column=1)
    B2.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
    B2.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))


def upd_air():
    """Selects airport for future actions"""
    global air, L1, cur_code, Lb3, Lb4, cities
    for i in airnet.airdat:
        if i.name == cities[::-1][Lb2.curselection()[0]]:
            cur_code = i.code_3
    air = cities[::-1][Lb2.curselection()[0]]
    L1.destroy()
    L1 = Label(main, text="Selected airport:  '" + air + "'", cursor="hand2", width=112, bg='aliceblue')
    L1.grid(row=4, columnspan=2)
    B3.grid(row=5, column=0)
    B4.grid(row=5, column=1)
    print(country)


countries = []
for i in sorted(list(set([i.country for i in airnet.airdat]))):
    countries.append(i)

con_copy = copy.copy(countries)

title = Label(main, text='Choose the country and airport for departure and for arrival', width=112, bg='aliceblue')

Lb1 = Listbox(main, width=55, cursor="sb_left_arrow")

for i in countries:
    Lb1.insert(END, i)


def lb1_update():
    """Updates counties list"""
    global countries, con_copy
    if con_copy != countries:
        Lb1.delete(0, END)
        for i in countries[::-1]:
            Lb1.insert(END, i)
        con_copy = copy.copy(countries)
    Lb1.after(200, lb1_update)


try:
    lb1_update()
except Exception as a:
    print(a)

text1 = StringVar()
text1.set("Type country to search")
text2 = StringVar()
text2.set("Type airport to search")
En1 = Entry(main, width=55, textvariable=text1, fg="gray")
En1.bind("<Button-1>", lambda e: text1.set(""))
En2 = Entry(main, width=55, textvariable=text2, fg="gray")
En2.bind("<Button-1>", lambda e: text2.set(""))


def en1_update():
    """Updates countries search entry"""
    global countries, con_copy
    if text1.get() == "" or text1.get() == "Type country to search":
        countries = []
        for i in sorted(list(set([i.country for i in airnet.airdat])))[::-1]:
            countries.append(i)
    elif text1.get() != "Type country to search" and text1.get() != "":
        countries = searchik.searchik(countries, text1.get())
    En1.after(200, en1_update)


try:
    en1_update()
except Exception as a:
    print(a)

temp_l = Label(main, text='Choose country and you will be able to select airport', width=55, height=10,
               bg='deepskyblue')

B1 = Button(main, text='Choose country', cursor="hand2", width=55, command=upd_con, bg='skyblue')
B2 = Button(main, width=55, bg='skyblue')
L1 = Label(main, text="Selected Airport", width=112, bg='aliceblue')
B3 = Button(main, text="Departure", cursor="hand2", width=55, command=set_depar, bg='skyblue')
B4 = Button(main, text="Arrival", cursor="hand2", width=55, command=set_arriv, bg='skyblue')

title.grid(row=0, columnspan=2)
Lb1.grid(row=2, column=0)
B1.grid(row=3, column=0)
temp_l.grid(row=2, column=1)
En1.grid(row=1, column=0)
En2.grid(row=1, column=1)
B2.grid(row=3, column=1)
L1.grid(row=4, columnspan=2)
L4 = Label(main, text="(!) Departure and arrival airports can not be the same (!)")
L5 = Label(main, text="Enter date in format: 01.01.2020, or choose today's", width=55, bg='aliceblue')


def date_ch():
    """Checks if the route is correct and displays entries and buttons for choosing date"""
    global L4, L5, B5, B6, E1
    L4.destroy()
    L5.destroy()
    if codes[0] != 0 and codes[1] != 0 and codes[0] == codes[1]:
        try:
            B5.destroy()
            B6.destroy()
        except:
            pass
        L4 = Label(main, text="(!) Departure and arrival airports can not be the same (!)", width=112, bg='lightcoral')
        L4.grid(row=7, columnspan=2)
    elif codes[0] != 0 and codes[1] != 0:
        L4 = Label(main, text="Enter or choose approximate date (10 days forward maximum available)", width=112,
                   bg='aliceblue')
        L4.grid(row=7, columnspan=2)
        L5 = Label(main, text="Enter date in format: 2019-14-05, or choose today's", width=55, bg='aliceblue')
        L5.grid(row=8, column=0)
        textik = StringVar()
        E1 = Entry(main, width=55, justify=CENTER, textvariable=textik)
        E1.grid(row=8, column=1)
        B5 = Button(main, text="Current date", cursor="hand2", width=55, bg='skyblue',
                    command=lambda: pre_final_cur(None))
        B6 = Button(main, text="Choose date", cursor="hand2", width=55, bg='skyblue',
                    command=lambda: pre_final_cur(E1.get()))
        B5.grid(row=9, column=0)
        B6.grid(row=9, column=1)
        but_list2 = [B5, B6]
        for i in but_list2:
            i.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
            i.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))

        print(airs)


def but_manage():
    """Manages the buttons to a nice looking animations"""
    global but_list
    but_list += [B1, B2, B3, B4]
    but_list = list(set(but_list))
    for i in but_list:
        i.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
        i.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))


but_manage()
root.mainloop()

import datetime
import airports
import aircrafts
import delay
import weather
from tkinter import *
from functools import partial
import map
import datetime
import time
from coordinates import Corray
import webbrowser
import os
import urllib.request
from PIL import Image, ImageTk
import io
import parsik

# TODO: No internet connection
# TODO: Google Flights reference
# TODO: Data changing and time
# TODO: Info widget

codes = [0, 0]
airport_names = []
airs = ['Nothing', 'Nothing']
country = ''
cur_code = ''
air = ''
date = ''

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
top_menu = 0
menubar = 0


def info_wait_start():
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
    info_f.destroy()



def donothing():
    map.update_map(codes[0], codes[1])
    webbrowser.open('file://' + os.path.realpath('map.html'))


def overd_t():
    root.overrideredirect(True)


def overd_f():
    root.overrideredirect(False)


def but_menu():
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
    # clock = Label(root, font=('times', 20, 'bold'), bg='green')
    # clock.pack(fill=BOTH, expand=1)
    Label(top_menu, width=8, bg='aliceblue', text="Today:", font=('Marcellus SC', 12)).grid(column=4, row=0)
    Label(top_menu, width=8, bg='aliceblue', text="Time:", font=('Marcellus SC', 12)).grid(column=6, row=0)

    date_w = Label(top_menu, bg='aliceblue', font=('Marcellus SC', 12), width=8)
    date_w.grid(column=5, row=0)

    time_w = Label(top_menu, bg='aliceblue', font=('Marcellus SC', 12), width=7)
    time_w.grid(column=7, row=0)

    def tick():
        global time1
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            time_w.config(text=time1)
        time_w.after(200, tick)

    def bam():
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
# codes = [0, 0]
# airport_names = []
# airs = ['Nothing', 'Nothing']
# country = ''
# cur_code = ''
# air = ''
# date = ''
print(air)


def link_to_flight(flight):
    link = 'https://flightaware.com/live/flight/{}'.format(aircrafts.format_flight(flight))
    webbrowser.open(link)


def pre_final_cur():
    global date, table, pref
    info_wait_start()
    root.update()
    now = datetime.datetime.now()
    table.destroy()
    table = Frame(main, bg="lightblue")
    table.grid(row=11, columnspan=2)
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

        # deli = delay.Delay(airnet.find_by_airname(airs[1]).code_3).alter_del()
        weath = weather.Weather()
        temp = airnet.find_by_airname(airs[1])
        weathik = Corray(temp.lat, temp.lon)
        weath.weather_coord(weathik)
        delik = delay.Delay(temp.code_3).alter_del()
        delik += weath.danger()

        # url = "https://e1.flightcdn.com/images/airline_logos/90p/CLH.png"
        # raw_data = urllib.request.urlopen(url).read()
        # im = Image.open(io.BytesIO(raw_data))
        # image = ImageTk.PhotoImage(im)
        #
        # for i in range(5):
        #     Label(table, image=image).grid(column=0, row=i)
        for_info = []
        for_info.clear()
        for i in range(len(te_1)):
            airline = te_1[i][1]
            for_info.append(te_1[i][0])
            print("\n______________TE1_____________")
            print(te_1)
            try:
                # print(delik)
                agp = aircrafts.get_plane(te_1[i][0])
                print(agp)
                # raw_data = urllib.request.urlopen(agp[1]).read()
                # im = Image.open(io.BytesIO(raw_data))
                # im = im.resize((25, 25), Image.ANTIALIAS)
                # image = ImageTk.PhotoImage(im)
                deli = aicnet.delay_extender(delik, agp[0])
                # print(te_1[i][0])
                # print(agp)
                # print(deli)
            except Exception as a:
                print(a)
                deli = delik

            if deli == 0:
                color = "white"
            elif deli < 0.05:
                color = "green"
            elif 0.04 < deli < 0.1:
                color = "yellow"
            elif deli > 0.09:
                color = "red"
            else:
                color = "white"
            Label(table, text=te_1[i][0], width=10, bg="aliceblue", relief=GROOVE, borderwidth=2,
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

            Label(table, text=airline, width=41, bg="aliceblue", justify=LEFT, relief=GROOVE, borderwidth=2,
                  highlightbackground="deepskyblue", highlightcolor="deepskyblue", ).grid(row=i, column=3)
            Label(table, text=airnet.find_by_airname(airs[0]).city + " " + te_1[i][2], width=17, bg="aliceblue",
                  relief=GROOVE, borderwidth=2,
                  highlightbackground="deepskyblue", highlightcolor="deepskyblue", ).grid(row=i, column=4)
            Label(table, text=airnet.find_by_airname(airs[1]).city + " " + te_1[i][3], width=17, bg="aliceblue",
                  relief=GROOVE, borderwidth=2,
                  highlightbackground="deepskyblue", highlightcolor="deepskyblue", ).grid(row=i, column=5)
            Label(table, text=round(float(deli), 4), width=10, bg=color,
                  relief=GROOVE, borderwidth=2,
                  highlightbackground="deepskyblue", highlightcolor="deepskyblue", ).grid(row=i, column=6)
            # try:
            # a = Label(table)
            # a.image = image
            # a.configure(image = image, width=14)
            # a.grid(row=i, column=0)
            # except:

            # im_exit = Image.open("exit_b.jpg")
            # image_exit = ImageTk.PhotoImage(im_exit)
            # exit_b = Button(top_menu, bg='red', image=image_exit, width=43, height=33, text="Exit", cursor="hand2",
            #                 command=root.quit)
            # exit_b.image = image_exit
            # exit_b.grid(column=9, row=0)

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
            # a.bind("<Button-1>", action_with_arg)
            root.update()
            # st = Label(table, text = parsik.flight(codes[0],codes[1]), width = 112, bg = "aliceblue")
            # st.pack()
    else:
        print("i'm here")
        Label(table, text="Nothing found", width=112, bg='yellow').grid(row=0, column=0)
    info_wait_destroy()

def set_depar():
    global cur_code
    codes[0] = cur_code
    airs[0] = air
    L2 = Label(main, text='From: ' + air + " (" + str(codes[0]) + ")", width=55, bg='aliceblue')
    L2.grid(row=6)
    date_ch()
    print(codes)


def set_arriv():
    global cur_code
    codes[1] = cur_code
    airs[1] = air
    L3 = Label(main, text='To: ' + air + " (" + str(codes[1]) + ")", width=55, bg='aliceblue')
    L3.grid(row=6, column=1)
    date_ch()
    print(codes)


def upd_con():
    global B2, Lb2, airport_names, country, cities
    try:
        L1.grid(row=4)
        temp = Lb1.curselection()[0]
        temp_l.destroy()
    except:
        pass
    print(Lb1.curselection()[0])
    cursl = sorted([(i.city, i.name) for i in airnet.airdat if i.country == countries[Lb1.curselection()[0]]])
    country = cursl
    # print(cursl)
    Lb2 = Listbox(main, width=55, cursor="sb_right_arrow")
    B2.destroy()
    B2 = Button(main, text='Choose airport', cursor="hand2", width=55, command=upd_air, bg='skyblue')
    airport_names = []
    cities = []
    for i in cursl:
        cities.append(i[1])
        Lb2.insert(END, str(i[0]) + ", " + str(i[1]))
    # for i in findflight.airports[cursl]:
    #     Lb2.insert(END, findflight.name_city_loc[list(i.keys())[0]][0] + ", " + list(i.keys())[0])
    #     airport_names.append(list(i.keys())[0])
    Lb2.grid(row=2, column=1)
    B2.grid(row=3, column=1)
    B2.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
    B2.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))


def upd_air():
    global air, L1, cur_code, Lb3, Lb4, cities
    # cursl = airport_names[Lb2.curselection()[0]]
    for i in airnet.airdat:
        if i.name == cities[Lb2.curselection()[0]]:
            cur_code = i.code_3
    # # print(Lb2.curselection())
    air = cities[Lb2.curselection()[0]]
    # cur_code = findflight.find_code(cursl, country)
    L1.destroy()
    L1 = Label(main, text="Selected airport:  '" + air + "'", cursor="hand2", width=112, bg='aliceblue')
    L1.grid(row=4, columnspan=2)
    B3.grid(row=5, column=0)
    B4.grid(row=5, column=1)
    print(country)
    # Lb2 = Listbox(root, width = 35)
    # airport_names = []
    # for i in findflight.airports[cursl]:
    #     Lb2.insert(END, list(i.keys())[0])
    #     airport_names.append(list(i.keys())[0])
    # Lb2.grid(row=1, column=1)
    # print(airport_names)


title = Label(main, text='Choose the country and airport for departure and for arrival', width=112, bg='aliceblue')
Lb1 = Listbox(main, width=55, cursor="sb_left_arrow")
temp_l = Label(main, text='Choose country and you will be able to select airport', width=55, height=10,
               bg='deepskyblue')
# Lb2 = Listbox(root, width = 35)
B1 = Button(main, text='Choose country', cursor="hand2", width=55, command=upd_con, bg='skyblue')
B2 = Button(main, width=55, bg='skyblue')
L1 = Label(main, text="Selected Airport", width=112, bg='aliceblue')
B3 = Button(main, text="Departure", cursor="hand2", width=55, command=set_depar, bg='skyblue')
B4 = Button(main, text="Arrival", cursor="hand2", width=55, command=set_arriv, bg='skyblue')
# L2 = Label(root, text = depart_ar, width = 55)
# L2 = Label(root, text = arriv_ar, width = 55)
countries = []
for i in sorted(list(set([i.country for i in airnet.airdat]))):
    countries.append(i)
    Lb1.insert(END, i)
title.grid(row=0, columnspan=2)
Lb1.grid(row=2, column=0)
B1.grid(row=3, column=0)
temp_l.grid(row=2, column=1)
B2.grid(row=3, column=1)
L1.grid(row=4, columnspan=2)
L4 = Label(main, text="(!) Departure and arrival airports can not be the same (!)")
L5 = Label(main, text="Enter date in format: 01.01.2020, or choose today's", width=55, bg='aliceblue')
E1 = Entry(main, width=55, justify=CENTER)


def date_ch():
    global L4, L5, E1, B5, B6
    L4.destroy()
    L5.destroy()
    E1.destroy()
    if codes[0] != 0 and codes[1] != 0 and codes[0] == codes[1]:
        try:
            B5.destroy()
            B6.destroy()
        except:
            pass
        L4 = Label(main, text="(!) Departure and arrival airports can not be the same (!)", width=112, bg='lightcoral')
        L4.grid(row=7, columnspan=2)
    elif codes[0] != 0 and codes[1] != 0:
        L4 = Label(main, text="Enter or choose approximate date", width=112, bg='aliceblue')
        L4.grid(row=7, columnspan=2)
        L5 = Label(main, text="Enter date in format: 11.1.2020, or choose today's", width=55, bg='aliceblue')
        L5.grid(row=8, column=0)
        E1 = Entry(main, width=55, justify=CENTER)
        E1.grid(row=8, column=1)
        B5 = Button(main, text="Current data", cursor="hand2", width=55, bg='skyblue', command=pre_final_cur)
        B6 = Button(main, text="Choose data", cursor="hand2", width=55, bg='skyblue')
        B5.grid(row=9, column=0)
        B6.grid(row=9, column=1)
        but_list2 = [B5, B6]
        for i in but_list2:
            i.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
            i.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))

        print(airs)


def but_manage():
    global but_list
    but_list += [B1, B2, B3, B4]
    but_list = list(set(but_list))
    for i in but_list:
        i.bind("<Enter>", lambda e: e.widget.config(relief=RIDGE))
        i.bind("<Leave>", lambda e: e.widget.config(relief=RAISED))


but_manage()
root.mainloop()

from tkinter import *
from tkinter import ttk
# from Image import ImageTk,Image
import findflight
import datetime
import parsik


root = Tk()
root.title('Flight Status')
root.geometry("900x500")
background_image = PhotoImage(file = "bg0.gif")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

main = Frame(root, bg = 'aliceblue', borderwidth = 2, highlightbackground="deepskyblue", highlightcolor="deepskyblue", highlightthickness=3)
table = Frame(main, bg='aliceblue')
main.pack()
def donothing():
    # filewin = Toplevel(root)
    import webbrowser, os
    webbrowser.open('file://' + os.path.realpath('map.html'))
    # button = Button(filewin, text="Do nothing button")
    # button.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open map", command=donothing)
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")

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
codes = [0, 0]
airport_names = []
country = ''
cur_code = ''
air = ''
date = ''
def pre_final_cur():
    global date, table
    now = datetime.datetime.now()
    table.destroy()
    table = Frame(main, bg = 'aliceblue')
    table.grid(row=10, columnspan=2)
    date = str(now.day) + "." + str(now.month) + "." + str(now.year)
    pref = Label(main, text = "Fights from " + str(codes[0]) + " to " + str(codes[1]) + " on " + date + ":", width = 112, height = 2, bg = "lightblue")
    pref.grid(row = 9, columnspan = 2)
    te_1 = parsik.flight(codes[0],codes[1], date)
    for i in range(len(te_1)):
        Label(table, text=te_1[i], width=112, bg="aliceblue", relief =GROOVE, borderwidth = 2, highlightbackground="deepskyblue", highlightcolor="deepskyblue",).pack()
    # st = Label(table, text = parsik.flight(codes[0],codes[1]), width = 112, bg = "aliceblue")
    # st.pack()

def set_depar():
    global cur_code
    codes[0] = cur_code
    L2 = Label(main, text='From: ' + air + " (" + codes[0]+ ")", width=55, bg ='aliceblue')
    L2.grid(row = 5)
    date_ch()
    print(codes)

def set_arriv():
    global cur_code
    codes[1] = cur_code
    L3 = Label(main, text='To: ' + air + " (" + codes[1]+ ")", width=55, bg ='aliceblue')
    L3.grid(row = 5, column = 1)
    date_ch()
    print(codes)

def upd_con():
    global B2, Lb2, airport_names, country
    try:
        L1.grid(row=3)
        temp = Lb1.curselection()[0]
        temp_l.destroy()
    except:
        pass
    cursl = sorted(list(findflight.airports.keys()))[Lb1.curselection()[0]]
    country = cursl
    print(cursl)
    Lb2 = Listbox(main, width = 55)
    B2.destroy()
    B2 = Button(main, text='Choose airport', width = 55, command=upd_air, bg = 'skyblue')
    airport_names = []
    for i in findflight.airports[cursl]:
        Lb2.insert(END, findflight.name_city_loc[list(i.keys())[0]][0] + ", " + list(i.keys())[0])
        airport_names.append(list(i.keys())[0])
    Lb2.grid(row=1, column=1)
    B2.grid(row=2, column=1)
    print(airport_names)

def upd_air():
    global air, L1, cur_code, Lb3, Lb4
    cursl = airport_names[Lb2.curselection()[0]]
    # print(Lb2.curselection())
    air = cursl
    cur_code = findflight.find_code(cursl, country)
    L1.destroy()
    L1 = Label(main, text = "Selected airport:  '" + air + "'", width = 112, bg ='aliceblue')
    L1.grid(row=3, columnspan=2)
    B3.grid(row=4, column=0)
    B4.grid(row=4, column=1)
    print(cursl)
    print(country)
    # Lb2 = Listbox(root, width = 35)
    # airport_names = []
    # for i in findflight.airports[cursl]:
    #     Lb2.insert(END, list(i.keys())[0])
    #     airport_names.append(list(i.keys())[0])
    # Lb2.grid(row=1, column=1)
    # print(airport_names)

title = Label(main, text= 'Choose the country and airport for departure and for arrival', width = 112, bg ='aliceblue')
Lb1 = Listbox(main, width = 55)
temp_l = Label(main, text = 'Choose country and you will be able to select airport', width = 55, height = 10, bg = 'deepskyblue')
# Lb2 = Listbox(root, width = 35)
B1 = Button(main, text = 'Choose country', width = 55, command = upd_con, bg = 'skyblue')
B2 = Button(main, width = 55, bg = 'skyblue')
L1 = Label(main, text = "Selected Airport", width = 112, bg ='aliceblue')
B3 = Button(main, text = "Departure", width = 55, command = set_depar, bg = 'skyblue')
B4 = Button(main, text = "Arrival", width = 55, command = set_arriv, bg = 'skyblue')
# L2 = Label(root, text = depart_ar, width = 55)
# L2 = Label(root, text = arriv_ar, width = 55)
for i in sorted(list(findflight.airports.keys())):
    Lb1.insert(END, i)
title.grid(row = 0, columnspan = 2)
Lb1.grid(row=1, column = 0)
B1.grid(row=2, column = 0)
temp_l.grid(row=1, column = 1)
B2.grid(row=2, column = 1)
L1.grid(row = 3, columnspan = 2)
L4 = Label(main, text= "(!) Departure and arrival airports can not be the same (!)")
L5 = Label(main, text = "Enter date in format: 01.01.2020, or choose today's", width = 55, bg ='aliceblue')
E1 = Entry(main, width=55, justify=CENTER)

def date_ch():
    global L4, L5, E1
    L4.destroy()
    L5.destroy()
    E1.destroy()
    if codes[0] != 0 and codes[1] != 0 and codes[0] == codes[1]:
        L4 = Label(main, text= "(!) Departure and arrival airports can not be the same (!)", width = 112, bg ='lightcoral')
        L4.grid(row = 6, columnspan = 2)
    elif codes[0] != 0 and codes[1] != 0:
        L4 = Label(main, text="Enter or choose approximate date", width = 112, bg ='aliceblue')
        L4.grid(row=6, columnspan=2)
        L5 = Label(main, text = "Enter date in format: 11.1.2020, or choose today's", width = 55, bg ='aliceblue')
        L5.grid(row = 7, column = 0)
        E1 = Entry(main, width = 55, justify=CENTER)
        E1.grid(row=7, column=1)
        B5 = Button(main, text = "Current data", width = 55, bg = 'skyblue', command = pre_final_cur)
        B6 = Button(main, text="Choose data", width = 55, bg = 'skyblue')
        B5.grid(row=8, column=0)
        B6.grid(row=8, column=1)
root.mainloop()

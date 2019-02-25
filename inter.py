from tkinter import *
from tkinter import ttk
import findflight

root = Tk()
root.geometry("500x500")
# root.overrideredirect(True)
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


# def donothing():
#     filewin = Toplevel(root)
#     button = Button(filewin, text="Do nothing button")
#     button.pack()
#
# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="New", command=donothing)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_command(label="Save as...", command=donothing)
# filemenu.add_command(label="Close", command=donothing)
#
# filemenu.add_separator()
#
# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)
# editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Undo", command=donothing)
#
# editmenu.add_separator()
#
# editmenu.add_command(label="Cut", command=donothing)
# editmenu.add_command(label="Copy", command=donothing)
# editmenu.add_command(label="Paste", command=donothing)
# editmenu.add_command(label="Delete", command=donothing)
# editmenu.add_command(label="Select All", command=donothing)
#
# menubar.add_cascade(label="Edit", menu=editmenu)
# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label="Help Index", command=donothing)
# helpmenu.add_command(label="About...", command=donothing)
# menubar.add_cascade(label="Help", menu=helpmenu)
#
# root.config(menu=menubar)
def upd_air():
    cursl = list(findflight.airports.keys())[Lb1.curselection()[0]]
    print(cursl)
    Lb2 = Listbox(root, width = 35)
    for i in findflight.airports[cursl]:
        Lb2.insert(END, list(i.keys())[0])
    Lb2.grid(row=1, column=1)

title = Label(root, text= 'Choose the country and airport for departure and for arrival')
Lb1 = Listbox(root, width = 35)
Lb2 = Listbox(root, width = 35)
B1 = Button(root, text = 'Choose country', command = upd_air)
B2 = Button(root, text = 'Choose airport')
for i in sorted(list(findflight.airports.keys())):
    Lb1.insert(END, i)
title.grid(row = 0, columnspan = 2)
Lb1.grid(row=1, column = 0)
B1.grid(row=2, column = 0)
Lb2.grid(row=1, column = 1)
B2.grid(row=2, column = 1)
root.mainloop()

from tkinter import *
import urllib.request
from PIL import Image, ImageTk
import io

url = "https://e1.flightcdn.com/images/airline_logos/90p/CLH.png"
root = Tk()
raw_data = urllib.request.urlopen(url).read()
im = Image.open(io.BytesIO(raw_data))
im.save('cropped_image.jpg')
im = Image.open('cropped_image.jpg')
im = im.resize((123, 3434), Image.ANTIALIAS)
image = ImageTk.PhotoImage(im)
table = Frame(root)
table.pack()
for i in range(5):
    Label(table, text = "heykkkkkkkkkkkkkkkkkkk", image=image).grid(column = 0, row = i)
root.mainloop()
from tkinter import *

root = Tk()
min_height = 500
min_width = 500
root.geometry(str(min_width)+"x"+str(min_height))
root.minsize(min_width, min_height)

template_names = ["stelum", "head", "details", "details2"]
labels = ["Red", "Green", "Blue"]

frame1 = LabelFrame(root, text="stelum")
for i in range(3):
    Label(frame1, text=labels[i % 3]).grid(row=i, column=0)
    w2 = Scale(frame1, from_=0, to=255, tickinterval=255, orient=HORIZONTAL, length=400)
    w2.set(127)
    w2.grid(row=i, column=1)
frame1.grid(row=0, column=0)

frame2 = LabelFrame(root, text="head")
for i in range(3):
    Label(frame2, text=labels[i % 3]).grid(row=i, column=0)
    w2 = Scale(frame2, from_=0, to=255, tickinterval=255, orient=HORIZONTAL, length=400)
    w2.set(127)
    w2.grid(row=i, column=1)
frame2.grid(row=1, column=0)

frame3 = LabelFrame(root, text="details")
for i in range(3):
    Label(frame3, text=labels[i % 3]).grid(row=i, column=0)
    w2 = Scale(frame3, from_=0, to=255, tickinterval=255, orient=HORIZONTAL, length=400)
    w2.set(127)
    w2.grid(row=i, column=1)
frame3.grid(row=2, column=0)

mainloop()

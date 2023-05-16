from tkinter import *
from tkinter import Canvas
from PIL import Image, ImageTk
from PIL.Image import Resampling

def load_png(png_file: str):
    png = Image.open(png_file)
    square_size = 320
    resized_image = png.resize((square_size, square_size), Resampling.NEAREST)
    return ImageTk.PhotoImage(resized_image)


min_height = 600
min_width = 900
root = Tk()
root.title("MycologyMC Fungi builder")
root.geometry(str(min_width)+"x"+str(min_height))
root.minsize(min_width, min_height)

template_names = ["stelum", "head", "details", "details2"]
labels = ["Red", "Green", "Blue"]
scales_frame = LabelFrame(root)
for name in template_names:
    frame = LabelFrame(scales_frame, text=name)
    for i in range(3):
        Label(frame, text=labels[i % 3]).grid(row=i, column=0)
        w2 = Scale(frame, from_=0, to=255, orient=HORIZONTAL, length=380)
        w2.set(127)
        w2.grid(row=i, column=1)
    frame.grid(row=template_names.index(name), column=0)

scales_frame.grid(row=0, column=0)

image_frame = LabelFrame(root)

#Label(image_frame, image=load_png("test.png")).pack()
w = Canvas(image_frame, width=600, height=600)

w.create_image(10, 10, anchor=NW, image=load_png("test.png"))
w.pack(side="right")

image_frame.grid(row=0, column=1)


mainloop()

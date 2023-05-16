from tkinter import *
from PIL import ImageTk, Image
from PIL.Image import Resampling


def load_png(png_file: str):
    png = (Image.open(png_file))
    square_size = 600
    resized_image = png.resize((square_size, square_size), Resampling.NEAREST)
    return ImageTk.PhotoImage(resized_image)

def print_value(val):
    #print(val)
    return

def entry_command(val1, val2):
    print(val2)
    return

###  initialise window
min_height = 710
min_width = 1040
root = Tk()
root.title("MycologyMC Fungi builder")
root.geometry(str(min_width)+"x"+str(min_height))
root.minsize(min_width, min_height)
#root.maxsize(min_width, min_height)

### build color scales
template_names = ["Stelum", "Head", "Details", "Details2"]
labels = ["Red", "Green", "Blue"]
scales_frame = LabelFrame(root)
for name in template_names:
    frame = LabelFrame(scales_frame, text=name)
    for i in range(3):
        Label(frame, text=labels[i % 3]).grid(row=i, column=0)
        w2 = Scale(frame, from_=0, to=255, orient=HORIZONTAL, length=360, command=print_value)
        w2.set(127)
        w2.grid(row=i, column=1)
    frame.grid(row=template_names.index(name), column=0)

scales_frame.grid(row=0, column=0)

color_output_frame = LabelFrame(root)
for name in template_names:
    frame = Frame(color_output_frame)
    Label(frame, text=name).grid(row=0, column=0)
    entry1 = Entry(frame)
    entry1.grid(row=0,column=1)
    entry1.insert(0, "FFFFFF")
    frame.pack()
color_output_frame.grid(row=1, column=0)


### build resulting image frame
image_frame = LabelFrame(root)

img = load_png("test.png")
Label(image_frame, image = img).pack()

image_frame.grid(row=0, column=1)

root.mainloop()

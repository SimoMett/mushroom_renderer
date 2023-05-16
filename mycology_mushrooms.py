from tkinter import *
from PIL import ImageTk, Image
from PIL.Image import Resampling

from src.colorpickerbutton import ColorPickerButton


def load_png(png_file: str):
    png = (Image.open(png_file))
    square_size = 600
    resized_image = png.resize((square_size, square_size), Resampling.NEAREST)
    return ImageTk.PhotoImage(resized_image)


def stelum_value(val):
    print("stelum" + val)
    return


def head_value(val):
    # print(val)
    return


def details_value(val):
    # print(val)
    return


def details2_value(val):
    # print(val)
    return


command_functions = [stelum_value, head_value, details_value, details2_value]

###  initialise window
min_height = 730
min_width = 1030
root = Tk()
root.title("MycologyMC Fungi builder")
root.geometry(str(min_width) + "x" + str(min_height))
root.minsize(min_width, min_height)
# root.maxsize(min_width, min_height)

### build color scales
template_names = ["Stelum", "Head", "Details", "Details2"]
labels = ["Red", "Green", "Blue"]
scales_frame = LabelFrame(root)
for name in template_names:
    frame = LabelFrame(scales_frame, text=name)
    for i in range(3):
        Label(frame, text=labels[i % 3]).grid(row=i, column=0)
        w2 = Scale(frame, from_=0, to=255, orient=HORIZONTAL, length=360,
                   command=command_functions[template_names.index(name)])
        w2.set(127)
        w2.grid(row=i, column=1)
    frame.grid(row=template_names.index(name), column=0)

scales_frame.grid(row=0, column=0)

color_output_frame = LabelFrame(root)
for name in template_names:
    frame = Frame(color_output_frame)

    Label(frame, text=name).grid(row=0, column=0)

    entry1 = Label(frame)
    entry1.grid(row=0, column=1)
    entry1.configure(text="FFFFFF")

    color_picker_button = ColorPickerButton(frame)
    color_picker_button.button.grid(row=0, column=2)

    frame.grid(row=round(template_names.index(name) / 2), column=template_names.index(name) % 2)
color_output_frame.grid(row=1, column=0)

### build resulting image frame
image_frame = LabelFrame(root)

img = load_png("test.png")
Label(image_frame, image=img).pack()

image_frame.grid(row=0, column=1)

root.mainloop()

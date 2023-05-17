from tkinter import *
from PIL import ImageTk, Image
from PIL.Image import Resampling

from src.colorpickerbutton import ColorPickerButton
from src.draw_fungus import draw_fungus, CRIMSON_FUNGUS_TYPE, WARPED_FUNGUS_TYPE


def load_fungus(colors, fungus_type=WARPED_FUNGUS_TYPE):
    png = (Image.fromarray(draw_fungus(colors, fungus_type)))
    square_size = 600
    resized_image = png.resize((square_size, square_size), Resampling.NEAREST)
    return ImageTk.PhotoImage(resized_image)


def scale_notify(val):
    notify()
    return


def notify():
    fungus_colors = []
    for j in range(4):
        fungus_colors.append(color_pickers[j].current_color)
        color_labels[j].configure(text=str(color_pickers[j].current_color))
    new_img = load_fungus(fungus_colors)
    fungus_label.configure(image=new_img)
    fungus_label.photo = new_img
    return


###  initialise window
min_height = 670
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
        w2 = Scale(frame, name=str(name).lower() + "_scale" + str(i), from_=0, to=255, orient=HORIZONTAL, length=360,
                   command=scale_notify)
        w2.set(127)
        w2.grid(row=i, column=1)
    frame.grid(row=template_names.index(name), column=0)

scales_frame.grid(row=0, column=0)

### build color pickers
color_pickers = []
color_labels = []
color_output_frame = LabelFrame(root)

i = 0
for name in template_names:
    frame = Frame(color_output_frame)

    Label(frame, text=name).grid(row=0, column=0)

    label = Label(frame, text="0")
    label.grid(row=0, column=1)
    color_labels.append(label)

    color_picker_button = ColorPickerButton(frame, notify)
    color_picker_button.button.grid(row=0, column=2)
    color_pickers.append(color_picker_button)

    frame.grid(row=i >> 1, column=i % 2)
    i += 1
color_output_frame.grid(row=1, column=0)

### build resulting image frame
image_frame = LabelFrame(root)

img = load_fungus([-1, -1, -1, -1])
fungus_label = Label(image_frame, image=img)
fungus_label.pack()

image_frame.grid(row=0, column=1)

root.mainloop()

import random
from tkinter import *
from PIL import ImageTk, Image
from PIL.Image import Resampling

from src.colorpickerbutton import ColorPickerButton
from src.draw_fungus import draw_fungus, CRIMSON_FUNGUS_TYPE, WARPED_FUNGUS_TYPE

current_fungus_type = CRIMSON_FUNGUS_TYPE

def load_fungus(colors, fungus_type):
    png = (Image.fromarray(draw_fungus(colors, fungus_type)))
    square_size = 600
    resized_image = png.resize((square_size, square_size), Resampling.NEAREST)
    return ImageTk.PhotoImage(resized_image)


def scale_notify(val):
    update_gui()
    return


def update_gui():
    fungus_colors = []
    for j in range(4):
        fungus_colors.append(color_pickers[j].current_color)
        color_labels[j].configure(text=str(color_pickers[j].current_color))
    new_img = load_fungus(fungus_colors, current_fungus_type)
    fungus_label.configure(image=new_img)
    fungus_label.photo = new_img

    is_r_g_or_b = 0
    for scale in color_scales:
        # scale.set(0)
        is_r_g_or_b = (is_r_g_or_b + 1) % 3

    return


def switch_to_crimson():
    global current_fungus_type
    current_fungus_type = CRIMSON_FUNGUS_TYPE
    update_gui()
    return

def switch_to_warped():
    global current_fungus_type
    current_fungus_type = WARPED_FUNGUS_TYPE
    update_gui()
    return

def copy_colors_to_clipboard():
    print("test")
    return

def hide_all_menus(arg):
    switch_template_menu.unpost()
    copy_colors_menu.unpost()


if __name__ == "__main__":
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
    color_scales = []
    scales_frame = LabelFrame(root)
    for name in template_names:
        frame = LabelFrame(scales_frame, text=name)
        for i in range(3):
            Label(frame, text=labels[i % 3]).grid(row=i, column=0)
            w2 = Scale(frame, name=str(name).lower() + "_scale" + str(i), from_=0, to=255, orient=HORIZONTAL, length=360,
                       command=scale_notify)
            w2.set(127)
            w2.grid(row=i, column=1)
            color_scales.append(w2)
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

        color_picker_button = ColorPickerButton(frame, update_gui)
        color_picker_button.button.grid(row=0, column=2)
        color_pickers.append(color_picker_button)

        frame.grid(row=i >> 1, column=i % 2)
        i += 1
    color_output_frame.grid(row=1, column=0)

    ### build resulting image frame
    #TODO wrap this fungus label in a class. It should be responsible to store the colors and draw the image
    image_frame = LabelFrame(root)

    img = load_fungus([random.randint(0,0xffffff) for i in range(4)], current_fungus_type)
    fungus_label = Label(image_frame, image=img)
    fungus_label.pack()

    image_frame.grid(row=0, column=1)

    ### right click to switch fungus
    switch_template_menu = Menu(root, tearoff=0)
    switch_template_menu.add_command(label="Switch to Crimson fungus template", command=switch_to_crimson)
    switch_template_menu.add_command(label="Switch to Warped fungus template", command=switch_to_warped)
    fungus_label.bind("<Button-3>", lambda event: switch_template_menu.post(event.x_root, event.y_root))

    ### right click to copy colors to clipboard
    copy_colors_menu = Menu(root, tearoff=0)
    copy_colors_menu.add_command(label="Copy to clipboard", command=copy_colors_to_clipboard)
    color_output_frame.bind("<Button-3>", lambda evt: copy_colors_menu.post(evt.x_root, evt.y_root))

    root.bind("<Button-1>", hide_all_menus)

    root.mainloop()

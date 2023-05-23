import random
from tkinter import *
from tkinter import filedialog

import cv2
import pyperclip
from PIL import ImageTk, Image

from src.colors_data_model import ColorsDataModel
from src.draw_fungus import draw_fungus
from src.fungus_image_frame import FungusImageFrame
from src.hsv_color_scale import HsvColorScale
from src.labeled_colorpicker_button import LabeledColorPickerButton
import colorsys


def scale_notify(scale_name, value):
    print(scale_name, value, color_scales[scale_name].get())
    return


def copy_colors_to_clipboard(as_hex=True):
    if as_hex:
        clipboard_string = str([hex(color_pickers[j].color_picker_button.current_color) for j in range(4)]) \
            .removeprefix("[") \
            .removesuffix("]") \
            .replace("'", "")
    else:
        clipboard_string = str([color_pickers[j].color_picker_button.current_color for j in range(4)]).removeprefix(
            "[").removesuffix("]")
    pyperclip.copy(clipboard_string)


def hide_all_menus(arg):
    copy_colors_menu.unpost()


def pick_random_colors():
    random_colors = [random.randint(0, 0xffffff) for i in range(4)]
    colors_data_model.change_colors(random_colors)


def save_as_png():
    selected_folder = filedialog.askdirectory(title="Select destination folder")
    colors = [image_frame.stelum_color, image_frame.head_color, image_frame.details_color, image_frame.details2_color]
    file_name = str(colors)
    result = draw_fungus(colors, image_frame.current_fungus_type)
    result = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)  # BGR to RGB, RGB to BGR, WTFFF
    cv2.imwrite(selected_folder + "/" + file_name + ".png", result)
    return


if __name__ == "__main__":
    ###  initialise window
    min_height = 660
    min_width = 1000
    root = Tk()
    root.iconphoto(True, ImageTk.PhotoImage(Image.open("res/icon.png").resize((32, 32), Image.NEAREST)))
    root.title("MycologyMC Fungi builder")
    root.geometry(str(min_width) + "x" + str(min_height))
    root.minsize(min_width, min_height)
    # root.maxsize(min_width, min_height)

    ### core data model
    colors_data_model = ColorsDataModel(0xffffff, 0xffffff, 0xffffff, 0xffffff)

    ### build color scales
    # FIXME broken + HSV is better suited
    # TODO update mechanism on color changes
    template_names = ["Stelum", "Head", "Details", "Details2"]
    labels = ["Hue", "Saturation", "Brightness"]
    color_scales = dict()
    scales_frame = Frame(root)
    for name in template_names:
        frame = LabelFrame(scales_frame, text=name)
        for i in range(3):
            Label(frame, text=labels[i % 3]).grid(row=i, column=0)
            w2 = Scale(frame, from_=0, to=255, orient=HORIZONTAL, length=360,
                       command=lambda val: scale_notify(name + "_" + labels[i % 3], val))
            w2.set(127)
            w2.grid(row=i, column=1)
            color_scales.update({name + "_" + labels[i % 3]: w2})

        frame.grid(row=template_names.index(name), column=0)

    scales_frame.grid(row=0, column=0)

    ### build color pickers
    color_pickers = []
    color_output_frame = LabelFrame(root)

    i = 0
    for name in template_names:
        color_picker = LabeledColorPickerButton(color_output_frame, name, i >> 1, i % 2)
        color_pickers.append(color_picker)
        color_picker.attach_colors_data_model(colors_data_model)
        i += 1
    color_output_frame.grid(row=1, column=0)

    ### build resulting image frame
    image_frame = FungusImageFrame(root)
    image_frame.grid(row=0, column=1)
    image_frame.attach_colors_data_model(colors_data_model)

    ### build random colors and save buttons
    buttons_frame = Frame(root)
    random_cols_button = Button(buttons_frame, text="Random colors", command=pick_random_colors)
    random_cols_button.grid(row=0)
    #random_cols_button.attach_colors_data_model(colors_data_model)
    Button(buttons_frame, text="Save as png", command=save_as_png).grid(row=1)
    buttons_frame.grid(row=1, column=1)

    ### right click to copy colors to clipboard
    copy_colors_menu = Menu(root, tearoff=0)
    copy_colors_menu.add_command(label="Copy to clipboard as HEX", command=lambda: copy_colors_to_clipboard(True))
    copy_colors_menu.add_command(label="Copy to clipboard as INT", command=lambda: copy_colors_to_clipboard(False))
    color_output_frame.bind("<Button-3>", lambda evt: copy_colors_menu.post(evt.x_root, evt.y_root))
    for picker in color_pickers:
        picker.color_picker_button.button.bind("<Button-3>", lambda evt: copy_colors_menu.post(evt.x_root, evt.y_root))
        picker.color_label.bind("<Button-3>", lambda evt: copy_colors_menu.post(evt.x_root, evt.y_root))
        picker.template_label.bind("<Button-3>", lambda evt: copy_colors_menu.post(evt.x_root, evt.y_root))

    root.bind("<Button-1>", lambda arg: image_frame.switch_template_menu.unpost())

    root.mainloop()

import random
from tkinter import *
from tkinter import filedialog

import cv2
import pyperclip
from PIL import ImageTk, Image
import svg

from src.colors_data_model import ColorsDataModel
from src.draw_fungus import draw_fungus
from src.fungus_image_frame import FungusImageFrame
from src.hsv_color_scale import HsvColorScale
from src.labeled_colorpicker_button import LabeledColorPickerButton


def copy_colors_to_clipboard(as_hex=True):
    if as_hex:
        clipboard_string = str([hex(color_pickers[j].color_picker_button.current_color) for j in range(4)]) \
            .removeprefix("[") \
            .removesuffix("]") \
            .replace("'", "")
    else:
        clipboard_string = str([color_pickers[j].color_picker_button.current_color for j in range(4)]) \
            .removeprefix("[") \
            .removesuffix("]")
    pyperclip.copy(clipboard_string)


def hide_all_menus(arg):
    copy_colors_menu.unpost()
    image_frame.switch_template_menu.unpost()


def pick_random_colors():
    random_colors = [random.randint(0, 0xffffff) for i in range(4)]
    colors_data_model.change_colors(random_colors)


def save_as_png():
    selected_folder = filedialog.askdirectory(title="Select destination folder", initialdir="~/")
    if len(selected_folder) != 0:
        colors = colors_data_model.get_colors_as_int()
        file_name = str(colors)
        result = draw_fungus(colors, image_frame.current_fungus_type)
        result = cv2.cvtColor(result, cv2.COLOR_RGB2BGRA)  # BGR to RGB, RGB to BGR, WTFFF
        cv2.imwrite(selected_folder + "/" + file_name + ".png", result)

        # svg
        result = cv2.cvtColor(result, cv2.COLOR_BGRA2RGBA)
        _elements = []
        for i in range(16):
            for j in range(16):
                if result[j][i][3] == 0:
                    continue
                color = hex((result[j][i][0] << 16) + (result[j][i][1] << 8) + result[j][i][2])
                box = svg.Rect(x=i, y=j, width=1, height=1,
                               fill=str(color).replace("0x", "#"))
                _elements.append(box)

        canvas = svg.SVG(
            width=16,
            height=16,
            elements=_elements
        )
        f = open(selected_folder + "/" + file_name + ".svg", "w")
        f.write(canvas.__str__())
        f.close()

    return


if __name__ == "__main__":
    ###  initialise window
    min_height = 660
    min_width = 1000
    root = Tk()
    raw_image = ImageTk.PhotoImage(Image.open("res/icon.png").resize((32, 32), Image.NEAREST))
    root.iconphoto(True, raw_image)
    root.title("MycologyMC Fungi builder")
    root.geometry(str(min_width) + "x" + str(min_height))
    root.minsize(min_width, min_height)
    # root.maxsize(min_width, min_height)

    ### core data model
    colors_data_model = ColorsDataModel(0xffffff, 0xffffff, 0xffffff, 0xffffff)

    ### build color scales
    template_names = ["Stelum", "Head", "Details", "Details2"]
    labels = ["Hue", "Saturation", "Brightness"]
    color_scales = dict()
    scales_frame = Frame(root)
    for name in template_names:
        frame = LabelFrame(scales_frame, text=name)
        hsv_scale = HsvColorScale(frame, name)
        hsv_scale.attach_colors_data_model(colors_data_model)

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

    root.bind("<Button-1>", hide_all_menus)

    root.mainloop()

import random
from tkinter import *
import pyperclip
from PIL import ImageTk, Image
from src.fungus_image_frame import FungusImageFrame
from src.labeled_colorpicker_button import LabeledColorPickerButton
import colorsys


def scale_notify(val):

    return


def copy_colors_to_clipboard(as_hex=True):
    if as_hex:
        clipboard_string = str([hex(color_pickers[j].color_picker_button.current_color) for j in range(4)]) \
            .removeprefix("[") \
            .removesuffix("]") \
            .replace("'", "")
    else:
        clipboard_string = str([color_pickers[j].color_picker_button.current_color for j in range(4)]).removeprefix("[").removesuffix("]")
    pyperclip.copy(clipboard_string)


def hide_all_menus(arg):
    copy_colors_menu.unpost()

def pick_random_colors():
    random_colors = [random.randint(0, 0xffffff) for i in range(4)]
    for j in range(4):
        color_pickers[j].color_picker_button.update_color(random_colors[j])
        color_pickers[j].update()

    hsv_random_colors = []
    for i in range(4):
        colr = str(random_colors[i])
        rgb_color = tuple(int(colr[i:i+2], 16) for i in (0, 2, 4))
        rgb_color = [val/255.0 for val in rgb_color]
        (h,s,v) = colorsys.rgb_to_hsv(rgb_color[2], rgb_color[1], rgb_color[0])
        (h,s,v)= (int(h * 179), int(s * 255), int(v * 255))
        hsv_random_colors.append(h)
        hsv_random_colors.append(s)
        hsv_random_colors.append(v)
    print(hsv_random_colors)

    j=0
    for scale in color_scales:
        scale.set(hsv_random_colors[color_scales.index(scale)])

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

    ### build color scales
    # FIXME broken + HSV is better suited
    # TODO update mechanism on color changes
    template_names = ["Stelum", "Head", "Details", "Details2"]
    labels = ["Hue", "Saturation", "Brightness"]
    color_scales = []
    scales_frame = Frame(root)
    for name in template_names:
        frame = LabelFrame(scales_frame, text=name)
        for i in range(3):
            Label(frame, text=labels[i % 3]).grid(row=i, column=0)
            w2 = Scale(frame, name=str(name).lower() + "_scale" + str(i), from_=0, to=255, orient=HORIZONTAL,
                       length=360)
            w2.set(127)
            w2.grid(row=i, column=1)
            color_scales.append(w2)
        frame.grid(row=template_names.index(name), column=0)

    scales_frame.grid(row=0, column=0)

    ### build color pickers
    color_pickers = []
    color_output_frame = LabelFrame(root)

    i = 0
    for name in template_names:
        color_picker = LabeledColorPickerButton(color_output_frame, name, i >> 1, i % 2)
        color_pickers.append(color_picker)
        i += 1
    color_output_frame.grid(row=1, column=0)

    ### build resulting image frame
    image_frame = FungusImageFrame(root)
    image_frame.grid(row=0, column=1)
    for color_picker in color_pickers:
        color_picker.attach_fungus_image_frame(image_frame)

    ### build random colors button
    Button(root, text="Random colors", command=pick_random_colors).grid(row=1, column=1)

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

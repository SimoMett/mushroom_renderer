from tkinter import *
import pyperclip
from PIL import ImageTk, Image
from src.draw_fungus import CRIMSON_FUNGUS_TYPE, WARPED_FUNGUS_TYPE
from src.fungus_image_frame import FungusImageFrame
from src.labeled_colorpicker_button import LabeledColorPickerButton

current_fungus_type = CRIMSON_FUNGUS_TYPE


def scale_notify(val):
    update_gui()
    return


def update_gui():
    fungus_colors = []
    for j in range(4):
        fungus_colors.append(color_pickers[j].current_color)
        text = str(hex(color_pickers[j].current_color)).removeprefix("0x")
        color_labels[j].configure(text=text)
    new_img = load_fungus(fungus_colors, current_fungus_type)
    #fungus_label.configure(image=new_img)
    #fungus_label.photo = new_img

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


def copy_colors_to_clipboard(as_hex=True):
    if as_hex:
        clipboard_string = str([hex(color_pickers[j].current_color) for j in range(4)]) \
            .removeprefix("[") \
            .removesuffix("]") \
            .replace("'", "")
    else:
        clipboard_string = str([color_pickers[j].current_color for j in range(4)]).removeprefix("[").removesuffix("]")
    pyperclip.copy(clipboard_string)


def hide_all_menus(arg):
    switch_template_menu.unpost()
    copy_colors_menu.unpost()


if __name__ == "__main__":
    ###  initialise window
    min_height = 670
    min_width = 1030
    root = Tk()
    root.iconphoto(True, ImageTk.PhotoImage(Image.open("res/icon.png").resize((32, 32), Image.NEAREST)))
    root.title("MycologyMC Fungi builder")
    root.geometry(str(min_width) + "x" + str(min_height))
    root.minsize(min_width, min_height)
    # root.maxsize(min_width, min_height)

    ### build color scales
    template_names = ["Stelum", "Head", "Details", "Details2"]
    labels = ["Red", "Green", "Blue"]
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
    color_labels = []
    color_output_frame = LabelFrame(root)

    i = 0
    for name in template_names:
        LabeledColorPickerButton(color_output_frame, name, i >> 1, i % 2)
        i += 1
    color_output_frame.grid(row=1, column=0)

    ### build resulting image frame
    image_frame = FungusImageFrame(root)
    image_frame.grid(row=0, column=1)

    ### right click to switch fungus
    switch_template_menu = Menu(root, tearoff=0)
    switch_template_menu.add_command(label="Switch to Crimson fungus template", command=switch_to_crimson)
    switch_template_menu.add_command(label="Switch to Warped fungus template", command=switch_to_warped)
    #fungus_label.bind("<Button-3>", lambda event: switch_template_menu.post(event.x_root, event.y_root))

    ### right click to copy colors to clipboard
    copy_colors_menu = Menu(root, tearoff=0)
    copy_colors_menu.add_command(label="Copy to clipboard as HEX", command=lambda: copy_colors_to_clipboard(True))
    copy_colors_menu.add_command(label="Copy to clipboard as INT", command=lambda: copy_colors_to_clipboard(False))
    color_output_frame.bind("<Button-3>", lambda evt: copy_colors_menu.post(evt.x_root, evt.y_root))
    for button in color_pickers:
        button.button.bind("<Button-3>", lambda evt: copy_colors_menu.post(evt.x_root, evt.y_root))
    for label in color_labels:
        label.bind("<Button-3>", lambda evt: copy_colors_menu.post(evt.x_root, evt.y_root))

    root.bind("<Button-1>", hide_all_menus)

    root.mainloop()

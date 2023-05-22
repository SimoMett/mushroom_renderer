import tkinter as ttk
from PIL import ImageTk, Image
from tkcolorpicker import askcolor


def tuple_to_color(color):
    return (color[0] << 16) + (color[1] << 8) + color[2]


def color_to_tuple(color):
    return color >> 16, (color >> 8) & 0xff, color & 0xff


def get_rotated_idiot(color):
    return (color & 0xFF00) + ((color & 0xFF) << 16) + (color >> 16)


class ColorPickerButton:

    def __init__(self, master, command=None):
        self.master = master
        self.current_color = 0xffffff
        self.command = command
        self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), self.current_color))
        self.button = ttk.Button(self.master, image=self.img, command=self.open_color_chooser)
        return

    def open_color_chooser(self):
        rgb = color_to_tuple(self.current_color)
        color = askcolor(rgb, self.master)  # FIXME sometimes askcolor doesn't return the exact color (WHY?)
        if color is not None and color[0] is not None:
            self.update_color(tuple_to_color(color[0]))
        if self.command is not None:
            self.command()
        return

    def update_color(self, color):
        self.current_color = color
        self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), color=get_rotated_idiot(color)))  # WHYYYY??
        self.button.configure(image=self.img)
        self.button.photo = self.img

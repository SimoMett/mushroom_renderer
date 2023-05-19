import tkinter as ttk
from PIL import ImageTk, Image
from tkcolorpicker import askcolor


def color_to_tuple(current_color):
    return current_color & 0xff, (current_color & 0xff00) >> 8, (current_color & 0xff0000) >> 16


class ColorPickerButton:

    def __init__(self, master, command=None):
        self.master = master
        self.current_color = 0xffffff
        self.command = command
        self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), self.current_color))
        self.button = ttk.Button(self.master, image=self.img, command=self.open_color_chooser)
        return

    def open_color_chooser(self):
        color = askcolor(color_to_tuple(self.current_color), self.master)
        if color is not None and color[0] is not None:
            self.update_color((color[0][2] << 16) + (color[0][1] << 8) + color[0][0])
        if self.command is not None:
            self.command()
        return

    def update_color(self, color):
        self.current_color = color
        self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), color=self.current_color))
        self.button.configure(image=self.img)
        self.button.photo = self.img

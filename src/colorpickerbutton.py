import tkinter as ttk
from PIL import ImageTk, Image
from tkcolorpicker import askcolor


def tuple_to_color(color):
    return (color[0] << 16) + (color[1] << 8) + color[2]


class ColorPickerButton:

    def __init__(self, master, command=None):
        self.master = master
        self.current_color = 0xffffff
        self.command = command
        self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), self.current_color))
        self.button = ttk.Button(self.master, image=self.img, command=self.open_color_chooser)
        return

    def open_color_chooser(self):
        hexa = "#"+str(hex(self.current_color)).removeprefix("0x")
        color = askcolor(hexa, self.master)
        if color is not None and color[0] is not None:
            self.update_color(tuple_to_color(color[0]))
        if self.command is not None:
            self.command()
        return

    def update_color(self, color):
        self.current_color = color
        self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), color=self.current_color))
        self.button.configure(image=self.img)
        self.button.photo = self.img

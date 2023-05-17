import tkinter as ttk
from PIL import ImageTk, Image
from tkcolorpicker import askcolor


class ColorPickerButton:

    def __init__(self, master, command=None):
        self.master = master
        self.current_color = -1
        self.command = command
        self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), self.current_color))
        self.button = ttk.Button(self.master, image=self.img, command=self.open_color_chooser)
        return

    def open_color_chooser(self):
        color = askcolor((255, 255, 0), self.master)
        if color is not None and color[0] is not None:
            self.current_color = (color[0][2] << 16) + (color[0][1] << 8) + color[0][0]
            self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), color=self.current_color))
            self.button.configure(image=self.img)
            self.button.photo = self.img
        if self.command is not None:
            self.command()
        return

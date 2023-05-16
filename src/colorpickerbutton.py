import tkinter as ttk
from PIL import ImageTk, Image
from tkcolorpicker import askcolor


class ColorPickerButton:

    def __init__(self, master):
        self.master = master
        self.current_color = 0

        self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), self.current_color))
        self.button = ttk.Button(self.master, image=self.img, command=self.open_color_chooser)
        return

    def open_color_chooser(self):
        color = askcolor((255, 255, 0), self.master)
        if color is not None:
            self.current_color = color[0]
            self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), color=self.current_color))
            self.button.configure(image=self.img)
            self.button.photo = self.img
        return

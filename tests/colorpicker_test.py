import tkinter as tk
import tkinter.ttk as ttk

import PIL.Image
from PIL import ImageTk, Image
from tkcolorpicker import askcolor


class ColorPickerButton:

    def __init__(self, master):
        self.current_color = 0

        self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), self.current_color))
        self.button = ttk.Button(image_frame, image=self.img, command=self.open_color_chooser)
        return

    def pack(self):
        self.button.pack()

    def open_color_chooser(self):
        color = askcolor((255, 255, 0), root)
        if color is not None:
            self.current_color = color[0]
            self.img = ImageTk.PhotoImage(Image.new('RGB', (24, 24), color=self.current_color))
            self.button.configure(image=self.img)
            self.button.photo = self.img
        return


root = tk.Tk()
root.geometry("100x100")
root.minsize(100, 100)

image_frame = ttk.Frame(root)

test_button = ColorPickerButton(image_frame)
test_button.pack()

image_frame.pack()

root.mainloop()

import tkinter as tk
import tkinter.ttk as ttk

import PIL.Image
from PIL import ImageTk, Image
from tkcolorpicker import askcolor


def open_color_chooser():
    color = askcolor((255, 255, 0), root)
    new_img = ImageTk.PhotoImage(Image.new('RGB', (16, 16), color=color[0]))
    test_button.configure(image=new_img)
    test_button.photo = new_img


root = tk.Tk()
root.geometry("100x100")
root.minsize(100, 100)

image_frame = ttk.Frame(root)

img = ImageTk.PhotoImage(Image.new('RGB', (16, 16), color='red'))
test_button = ttk.Button(image_frame, text="test", image=img, command=open_color_chooser)
test_button.pack()

image_frame.pack()

root.mainloop()

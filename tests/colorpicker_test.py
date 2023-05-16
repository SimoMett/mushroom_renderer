import tkinter as tk
import tkinter.ttk as ttk

import PIL.Image
import numpy
from PIL import ImageTk, Image
from tkcolorpicker import askcolor

root = tk.Tk()

image_frame = ttk.Frame(root)

#img = Image.fromarray(numpy.array([[0 for i in range(16)] for j in range(16)]))
img = ImageTk.PhotoImage(PIL.Image.open("../test.png"))

ttk.Label(image_frame, image = img).pack()

image_frame.grid(row=0, column=1)

print(askcolor((255, 255, 0), root))
root.mainloop()
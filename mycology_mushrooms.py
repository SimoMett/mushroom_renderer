from tkinter import *
from tkinter import ttk
from tkinter import Canvas
from PIL import Image, ImageTk
from PIL.Image import Resampling

root = Tk()
color_selection_frame = ttk.Frame(root, padding=5, width=200)
image_preview_frame = ttk.Frame(root, padding=5, width=20)
color_selection_frame.pack(anchor="nw", side="left")
image_preview_frame.pack(side="right")

# Create a canvas
w = Canvas(root, width=600, height=400)
w.pack()

# Load an image in the script
img = (Image.open("test.png"))

# Resize the Image using resize method
resized_image = img.resize((300, 205), Resampling.NEAREST)
new_image = ImageTk.PhotoImage(resized_image)

# Add image to the Canvas Items
w.create_image(10, 10, anchor=NW, image=new_image)

ttk.Entry().pack()
ttk.Scale(color_selection_frame).pack()
ttk.Scale(color_selection_frame).pack()
ttk.Scale(color_selection_frame).pack()

ttk.Scale(color_selection_frame).pack()
ttk.Scale(color_selection_frame).pack()
ttk.Scale(color_selection_frame).pack()

ttk.Scale(color_selection_frame).pack()
ttk.Scale(color_selection_frame).pack()
ttk.Scale(color_selection_frame).pack()

ttk.Scale(color_selection_frame).pack()
ttk.Scale(color_selection_frame).pack()
ttk.Scale(color_selection_frame).pack()

root.mainloop()

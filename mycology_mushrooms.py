import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import Canvas

root = Tk()
color_selection_frame = ttk.Frame(root, padding=10, width=200)
image_preview_frame = ttk.Frame(root, padding=10, width=20)
color_selection_frame.pack(anchor="nw", side="left")
image_preview_frame.pack(side="right")

canvas_width = 800
canvas_height = 400
w = Canvas(image_preview_frame,
           width=canvas_width,
           height=canvas_height)
w.pack()


y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")
w.scan_mark(20, 20)

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

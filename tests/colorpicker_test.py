import tkinter as tk
import tkinter.ttk as ttk

from src.colorpickerbutton import ColorPickerButton

root = tk.Tk()
root.geometry("100x100")
root.minsize(100, 100)

image_frame = ttk.Frame(root)

test_button = ColorPickerButton(image_frame)
test_button.button.pack()

image_frame.pack()

root.mainloop()

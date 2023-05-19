from tkinter import LabelFrame, Label

from PIL import Image, ImageTk

from src.draw_fungus import CRIMSON_FUNGUS_TYPE, WARPED_FUNGUS_TYPE, draw_fungus


class FungusImageFrame:

    def __init__(self, master):
        self.current_fungus_type = CRIMSON_FUNGUS_TYPE
        self.frame_square_size = 550
        self.master = master
        self.frame = LabelFrame(self.master)

        img = self.load_fungus([0xffffff for i in range(4)], self.current_fungus_type)
        self.fungus_label = Label(self.frame, image=img)
        self.fungus_label.pack()

    def grid(self, row, column):
        self.frame.grid(row=row, column=column)

    def load_fungus(self, colors, fungus_type):
        png = (Image.fromarray(draw_fungus(colors, fungus_type)))
        self.frame_square_size = 550
        resized_image = png.resize((self.frame_square_size, self.frame_square_size), Image.NEAREST)
        return ImageTk.PhotoImage(resized_image)

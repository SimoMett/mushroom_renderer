from tkinter import LabelFrame, Label

from PIL import Image, ImageTk

from src.draw_fungus import CRIMSON_FUNGUS_TYPE, draw_fungus


class FungusImageFrame:

    def __init__(self, master):
        self.stelum_color = 0xffffff
        self.head_color = 0xffffff
        self.details_color = 0xffffff
        self.details2_color = 0xffffff
        colors_array = [self.stelum_color, self.head_color, self.details_color, self.details2_color]
        self.current_fungus_type = CRIMSON_FUNGUS_TYPE

        self.frame_square_size = 550
        self.master = master
        self.frame = LabelFrame(self.master)

        self.img = self.load_fungus(colors_array, self.current_fungus_type)
        self.fungus_label = Label(self.frame, image=self.img)
        self.fungus_label.pack()

    def grid(self, row, column):
        self.frame.grid(row=row, column=column)

    def load_fungus(self, colors, fungus_type):
        png = Image.fromarray(draw_fungus(colors, fungus_type))
        resized_image = png.resize((self.frame_square_size, self.frame_square_size), Image.NEAREST)
        return ImageTk.PhotoImage(resized_image)

    def update_colors(self):
        self.img = self.load_fungus([self.stelum_color, self.head_color, self.details_color, self.details2_color],
                                    self.current_fungus_type)
        self.fungus_label.configure(image=self.img)

    def update_stelum_color(self, new_color):
        self.stelum_color = new_color
        self.update_colors()

    def update_head_color(self, new_color):
        self.head_color = new_color
        self.update_colors()

    def update_details_color(self, new_color):
        self.details_color = new_color
        self.update_colors()

    def update_details2_color(self, new_color):
        self.details2_color = new_color
        self.update_colors()

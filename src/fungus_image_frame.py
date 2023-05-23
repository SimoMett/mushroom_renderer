from tkinter import LabelFrame, Label, Menu

from PIL import Image, ImageTk

from src.colors_data_model import ColorsDataModel
from src.draw_fungus import CRIMSON_FUNGUS_TYPE, WARPED_FUNGUS_TYPE, draw_fungus


class FungusImageFrame:

    def __init__(self, master, colors_data_model=None):
        self.colors_data_model = colors_data_model
        colors_array = [0xffffff, 0xffffff, 0xffffff, 0xffffff]
        self.current_fungus_type = CRIMSON_FUNGUS_TYPE

        self.frame_square_size = 550
        self.master = master
        self.frame = LabelFrame(self.master)

        self.img = self.load_fungus(colors_array, self.current_fungus_type)
        self.fungus_label = Label(self.frame, image=self.img)
        self.fungus_label.pack()

        ### right click to switch fungus
        self.switch_template_menu = Menu(master, tearoff=0)
        self.switch_template_menu.add_command(label="Switch to Crimson fungus template", command=self.switch_to_crimson)
        self.switch_template_menu.add_command(label="Switch to Warped fungus template", command=self.switch_to_warped)
        self.fungus_label.bind("<Button-3>", lambda event: self.switch_template_menu.post(event.x_root, event.y_root))

    def grid(self, row, column):
        self.frame.grid(row=row, column=column)

    def attach_colors_data_model(self, colors_data_model: ColorsDataModel):
        self.colors_data_model = colors_data_model
        self.colors_data_model.subscribe(self)

    def load_fungus(self, colors, fungus_type):
        png = Image.fromarray(draw_fungus(colors, fungus_type))
        resized_image = png.resize((self.frame_square_size, self.frame_square_size), Resampling.NEAREST)
        return ImageTk.PhotoImage(resized_image)

    def on_color_update(self):
        self.img = self.load_fungus(self.colors_data_model.get_colors_as_int(), self.current_fungus_type)
        self.fungus_label.configure(image=self.img)

    # TODO reimplement all the methods below

    def update_template(self):
        self.on_color_update()

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

    def switch_to_crimson(self):
        self.current_fungus_type = CRIMSON_FUNGUS_TYPE
        self.update_template()
        return

    def switch_to_warped(self):
        self.current_fungus_type = WARPED_FUNGUS_TYPE
        self.update_template()
        return

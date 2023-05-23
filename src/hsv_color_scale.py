import colorsys
from tkinter import Label, Scale, HORIZONTAL

from src.color_functions import color_to_tuple


def rgb_to_hsv(rgb: tuple):
    (r, g, b) = (rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)
    (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    return int(h * 179), int(s * 255), int(v * 255)


template_names = ["Stelum", "Head", "Details", "Details2"]
hsv_channels = ["Hue", "Saturation", "Brightness"]


class HsvColorScale:

    def __init__(self, master, template_name):
        self.colors_data_model = None
        self.template_name = template_name
        self.hsv_scales = [None, None, None]

        Label(master, text="Hue").grid(row=0, column=0)
        self.hsv_scales[0] = Scale(master, from_=0, to=255, orient=HORIZONTAL, length=360, command=self.hue_change)
        self.hsv_scales[0].grid(row=0, column=1)

        Label(master, text="Saturation").grid(row=1, column=0)
        self.hsv_scales[1] = Scale(master, from_=0, to=255, orient=HORIZONTAL, length=360, command=self.sat_change)
        self.hsv_scales[1].grid(row=1, column=1)

        Label(master, text="Value").grid(row=2, column=0)
        self.hsv_scales[2] = Scale(master, from_=0, to=179, orient=HORIZONTAL, length=360, command=self.val_change)
        self.hsv_scales[2].grid(row=2, column=1)

        self.hsv_scales[0].set(0)
        self.hsv_scales[1].set(0)
        self.hsv_scales[2].set(255)

    def attach_colors_data_model(self, colors_data_model):
        self.colors_data_model = colors_data_model
        self.colors_data_model.subscribe(self)  # FIXME update of scales

    def on_color_update(self):
        template_id = template_names.index(self.template_name)
        hsv = rgb_to_hsv(color_to_tuple(self.colors_data_model.get_color_as_int(template_id)))
        self.hsv_scales[0].configure(command=None)
        self.hsv_scales[1].configure(command=None)
        self.hsv_scales[2].configure(command=None)
        for i in range(3):
            self.hsv_scales[i].set(hsv[i])
        self.hsv_scales[0].configure(command=self.hue_change)
        self.hsv_scales[1].configure(command=self.sat_change)
        self.hsv_scales[2].configure(command=self.val_change)

    def update_scales(self):
        pass

    def hue_change(self, val):
        print("test")
        template_id = template_names.index(self.template_name)
        hsv = (int(val), self.hsv_scales[1].get(), self.hsv_scales[2].get())
        self.colors_data_model.change_color_hsv(template_id, hsv)

    def sat_change(self, val):
        template_id = template_names.index(self.template_name)
        hsv = (self.hsv_scales[0].get(), int(val), self.hsv_scales[2].get())
        self.colors_data_model.change_color_hsv(template_id, hsv)

    def val_change(self, val):
        template_id = template_names.index(self.template_name)
        hsv = (self.hsv_scales[0].get(), self.hsv_scales[1].get(), int(val))
        self.colors_data_model.change_color_hsv(template_id, hsv)

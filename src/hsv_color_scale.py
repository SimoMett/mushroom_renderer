import colorsys
from tkinter import Label, Scale, HORIZONTAL


def rgb_to_hsv(rgb: tuple):
    (r, g, b) = (rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)
    (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    return int(h * 179), int(s * 255), int(v * 255)


hsv_labels = ["Hue", "Saturation", "Brightness"]


class HsvColorScale:

    def __init__(self, master, template_name):
        self.colors_data_model = None
        self.template_name = template_name
        self.hsv_scales = [None, None, None]
        for i in range(3):
            Label(master, text=hsv_labels[i]).grid(row=i, column=0)
            self.hsv_scales[i] = Scale(master, from_=0, to=255, orient=HORIZONTAL, length=360,
                                       command=lambda val: self.scale_notify(hsv_labels[i], val))

            self.hsv_scales[i].set(127)
            self.hsv_scales[i].grid(row=i, column=1)
            # color_scales.update({template_name + "_" + labels[i % 3]: w2})

    def attach_colors_data_model(self, colors_data_model):
        self.colors_data_model = colors_data_model
        self.colors_data_model.subscribe(self)

    def on_color_update(self):
        print("TODO")

    def change_color(self, color):
        pass

    def update_scales(self):
        pass

    def scale_notify(self, channel, val):
        print(self.template_name + "_" + channel, val)
        # TODO calculate rgb from hsv
        # TODO update colors in buttons and figure


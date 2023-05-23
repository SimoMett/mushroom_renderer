import colorsys

from src.color_functions import tuple_to_color, hsv_tuple_to_color, color_to_tuple
from src.hsv_color_scale import HsvColorScale

STELUM_COLOR = 0
HEAD_COLOR = 1
DETAILS_COLOR = 2
DETAILS2_COLOR = 3


class ColorsDataModel:
    def __init__(self, stelum_col, head_col, details_col, details2_col):
        self.colors = [0xffffff, 0xffffff, 0xffffff, 0xffffff]
        self.colors[STELUM_COLOR] = stelum_col
        self.colors[HEAD_COLOR] = head_col
        self.colors[DETAILS_COLOR] = details_col
        self.colors[DETAILS2_COLOR] = details2_col

        self.observers = []

    def change_color(self, color_id, new_color):
        if type(new_color) is int:
            self.colors[color_id] = new_color
        elif type(new_color) is tuple:
            self.colors[color_id] = tuple_to_color(new_color)
        else:
            raise Exception("Unexpected type")

        self.update_observers()

    def change_colors(self, colors):
        self.colors = colors
        self.update_observers()

    def change_color_hsv(self, color_id, hsv_colors):
        self.colors[color_id] = hsv_tuple_to_color(hsv_colors)
        self.update_except_scales_observers()

    def get_colors_as_int(self):
        return self.colors

    def get_color_as_int(self, color_id):
        return self.colors[color_id]

    def get_color_as_rgb(self, color_id):
        return color_to_tuple(self.colors[color_id])

    def get_color_as_hsv(self, color_id):
        (r, g, b) = self.get_color_as_rgb(color_id)
        (r, g, b) = (r / 255, g / 255, b / 255)
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
        return int(h * 179), int(s * 255), int(v * 255)

    def update_observers(self):
        for observer in self.observers:
            observer.on_color_update()

    def update_except_scales_observers(self):
        for observer in self.observers:
            if type(observer) is not HsvColorScale:
                observer.on_color_update()

    def subscribe(self, observer):
        self.observers.append(observer)

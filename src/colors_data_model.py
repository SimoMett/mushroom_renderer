import colorsys

STELUM_COLOR = 0
HEAD_COLOR = 1
DETAILS_COLOR = 2
DETAILS2_COLOR = 3


def tuple_to_color(color):
    return (color[0] << 16) + (color[1] << 8) + color[2]


def color_to_tuple(color):
    return color >> 16, (color >> 8) & 0xff, color & 0xff


class ColorsDataModel:
    def __init__(self, stelum_col, head_col, details_col, details2_col):
        self.colors = [0, 0, 0, 0]
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

        self.notify_all_observers()

    def get_color_as_int(self, color_id):
        return self.colors[color_id]

    def get_color_as_rgb(self, color_id):
        return color_to_tuple(self.colors[color_id])

    def get_color_as_hsv(self, color_id):
        (r, g, b) = self.get_color_as_rgb(color_id)
        (r, g, b) = (r / 255, g / 255, b / 255)
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
        return int(h * 179), int(s * 255), int(v * 255)

    def notify_all_observers(self):
        for observer in self.observers:
            observer.on_color_update()
        pass

    def subscribe(self, observer):
        self.observers.append(observer)




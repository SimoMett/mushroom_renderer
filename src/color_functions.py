import colorsys


def tuple_to_color(color):
    return (color[0] << 16) + (color[1] << 8) + color[2]


def color_to_tuple(color):
    return color >> 16, (color >> 8) & 0xff, color & 0xff


def hsv_tuple_to_color(hsv_color):
    (r, g, b) = colorsys.hsv_to_rgb(hsv_color[0]/255, hsv_color[1]/255, hsv_color[2]/179)
    rgb_color = (int(r*255), int(g*255), int(b*255))
    return tuple_to_color(rgb_color)


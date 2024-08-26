import urllib

import cv2
import numpy as np
import requests
from urllib3.exceptions import NewConnectionError

fungus_types = [
    "crimson",
    "warped"
]

CRIMSON_FUNGUS_TYPE = fungus_types.index("crimson")
WARPED_FUNGUS_TYPE = fungus_types.index("warped")

texture_templates = [
    "_fungus_stelum",
    "_fungus_head",
    "_fungus_details",
    "_fungus_details2"
]

templates_cache = dict()


def get_texture(fungus_type, texture):
    full_text_name = fungus_types[fungus_type] + texture
    if full_text_name in templates_cache.keys():
        return templates_cache[full_text_name]

    try:
        url = "https://raw.githubusercontent.com/SimoMett/MycologyMC/master/src/main/resources/assets/mycologymod/textures/item/" + \
              full_text_name + ".png"
        req = urllib.request.urlopen(url)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        in_img = cv2.imdecode(arr, cv2.IMREAD_UNCHANGED)
        templates_cache[full_text_name] = in_img
    except NewConnectionError as e:
        print("ERROR OCCURRED. Using local assets")

        path = "res/templates/" + full_text_name + ".png"
        in_img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    return in_img


def draw_fungus(fungus_colors, fungus_type=CRIMSON_FUNGUS_TYPE):
    out_images = []
    for texture_name in texture_templates:
        color_index = texture_templates.index(texture_name)

        in_img = get_texture(fungus_type, texture_name)

        b, g, r, a = cv2.split(in_img)

        # extracting channels from fungus_colors
        b_val = (fungus_colors[color_index] >> 16) & 0xFF
        g_val = (fungus_colors[color_index] >> 8) & 0xFF
        r_val = (fungus_colors[color_index] & 0xFF)

        # giving color
        out_blue_array = np.full((16, 16), b_val, dtype="uint8")
        np.multiply(b / 255, out_blue_array, out=out_blue_array, casting="unsafe")

        out_green_array = np.full((16, 16), g_val, dtype="uint8")
        np.multiply(g / 255, out_green_array, out=out_green_array, casting="unsafe")

        out_red_array = np.full((16, 16), r_val, dtype="uint8")
        np.multiply(r / 255, out_red_array, out=out_red_array, casting="unsafe")

        out_img = cv2.merge([out_blue_array, out_green_array, out_red_array, a])
        out_images.append(out_img)

    result = np.full((16, 16, 4), 0, dtype="uint8")
    for x in out_images:
        result += x
    return result

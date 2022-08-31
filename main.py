import cv2
import numpy as np
import random

fungus_types = [
    "crimson",
    "warped"
]

texture_templates = [
    "_fungus_stelum",
    "_fungus_head",
    "_fungus_details",
    "_fungus_details2"
]

#               stelum,    head,     details,  details2
fungus_colors = [random.randint(0, 0xFFFFFF), random.randint(0, 0xFFFFFF), random.randint(0, 0xFFFFFF), random.randint(0, 0xFFFFFF)]

out_images = []

for texture in texture_templates:

    color_index = texture_templates.index(texture)
    path = "templates/"+fungus_types[0]+texture+".png"
    in_img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    b, g, r, a = cv2.split(in_img)

    # extracting channels from fungus_colors
    r_val = (fungus_colors[color_index] & 0xFF0000) >> 16
    g_val = (fungus_colors[color_index] & 0xFF00) >> 8
    b_val = (fungus_colors[color_index] & 0xFF)

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
cv2.imwrite("test.png", result)

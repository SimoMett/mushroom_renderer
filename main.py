import cv2
import numpy as np
import random

crimson_txd_templates = [
    "templates/crimson_fungus_stelum.png",
    "templates/crimson_fungus_head.png",
    "templates/crimson_fungus_details.png",
    "templates/crimson_fungus_details2.png"
]

warped_txd_templates = [
    "templates/warped_fungus_stelum.png",
    "templates/warped_fungus_head.png",
    "templates/warped_fungus_details.png",
    "templates/warped_fungus_details2.png"
]

#               stelum,    head,     details,  details2
stelum_color = 0xffffff
head_color = 0xffffff
details_color = 0xffffff
details2_color = 0xffffff
#fungus_colors = [random.randint(0, stelum_color), random.randint(0, head_color), random.randint(0, details_color), random.randint(0, details2_color)]
fungus_colors = [stelum_color, head_color, details_color, details2_color]

out_images = []

for texture in warped_txd_templates:

    color_index = warped_txd_templates.index(texture)
    in_img = cv2.imread(texture, cv2.IMREAD_UNCHANGED)
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

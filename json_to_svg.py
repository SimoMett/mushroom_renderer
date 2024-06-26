import json

import cv2
import svg
import sys

from src.draw_fungus import draw_fungus, fungus_types


def export_svg(file_name):
    f = open(file_name, "r")
    data = json.load(f)
    colors = data["colors"]
    fungus_type = str(data["type"])
    f.close()
    fungus_type = fungus_type.removesuffix("_fungus")
    fungus_type = fungus_type.removeprefix("colored_")
    file_name = file_name.removesuffix(".json")
    result = draw_fungus(colors, fungus_types.index(fungus_type))
    result = cv2.cvtColor(result, cv2.COLOR_RGB2RGBA)
    _elements = []
    for i in range(16):
        for j in range(16):
            if result[j][i][3] == 0:
                continue
            color = "#{:06x}".format(
                (result[j][i][0] << 16) + (result[j][i][1] << 8) + result[j][i][2]
            )
            box = svg.Rect(x=i, y=j, width=1, height=1,
                           fill=color)
            _elements.append(box)
    canvas = svg.SVG(
        width=16,
        height=16,
        elements=_elements
    )
    f = open(file_name + ".svg", "w")
    f.write(canvas.__str__())
    f.close()


if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        export_svg(sys.argv[i])

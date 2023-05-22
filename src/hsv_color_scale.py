from tkinter import Label, Scale, HORIZONTAL


class HsvColorScale:

    def __init__(self, master, template_name):
        labels = ["Hue", "Saturation", "Brightness"]
        for i in range(3):
            Label(master, text=labels[i % 3]).grid(row=i, column=0)
            w2 = Scale(master, from_=0, to=255, orient=HORIZONTAL, length=360)
            # w2 = Scale(frame, from_=0, to=255, orient=HORIZONTAL, length=360,
            #           command=lambda val: scale_notify(name + "_" + labels[i % 3], val))

            w2.set(127)
            w2.grid(row=i, column=1)
            # color_scales.update({template_name + "_" + labels[i % 3]: w2})

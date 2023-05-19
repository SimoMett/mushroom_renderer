from tkinter import Frame, Label

from src.colorpickerbutton import ColorPickerButton


class LabeledColorPickerButton:

    def __init__(self, master_frame, name, grid_placement_row, grid_placement_column):
        # self.current_color = 0xffffff # useless?
        self.template_name = name
        self.fungus_image_frame = None
        self.frame = Frame(master_frame)

        # template name label
        self.template_label = Label(self.frame, text=self.template_name)
        self.template_label.grid(row=0, column=0)
        # TODO right click menu
        # label.bind("<Button-3>", lambda evt: copy_colors_menu.post(evt.x_root, evt.y_root))

        # color label
        self.color_label = Label(self.frame, text="0xffffff")
        self.color_label.grid(row=0, column=1)

        # color picker button
        self.color_picker_button = ColorPickerButton(self.frame, self.update)
        self.color_picker_button.button.grid(row=0, column=2)

        self.frame.grid(row=grid_placement_row, column=grid_placement_column)
        return

    def attach_fungus_image_frame(self, fungus_image_frame):
        self.fungus_image_frame = fungus_image_frame

    def update(self):
        color = self.color_picker_button.current_color
        text = str(hex(color))
        self.color_label.configure(text=text)
        # update image
        if self.fungus_image_frame is not None:
            if self.template_name == "Stelum":
                self.fungus_image_frame.update_stelum_color(color)
            elif self.template_name == "Head":
                self.fungus_image_frame.update_head_color(color)
            elif self.template_name == "Details":
                self.fungus_image_frame.update_details_color(color)
            elif self.template_name == "Details2":
                self.fungus_image_frame.update_details2_color(color)
            else:  # just in case
                raise RuntimeError("this self.template_name is not allowed:", self.template_name)
        return

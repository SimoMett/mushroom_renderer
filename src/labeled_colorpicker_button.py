from tkinter import Frame, Label

from src.colorpickerbutton import ColorPickerButton


class LabeledColorPickerButton:

    def __init__(self, master_frame, name, grid_placement_row, grid_placement_column):
        self.current_color = 0xffffff
        self.frame = Frame(master_frame)

        # template name label
        self.template_label = Label(self.frame, text=name)
        self.template_label.grid(row=0, column=0)
        # TODO right click menu
        # label.bind("<Button-3>", lambda evt: copy_colors_menu.post(evt.x_root, evt.y_root))

        # color label
        self.color_label = Label(self.frame, text="0")
        self.color_label.grid(row=0, column=1)

        # color picker button
        color_picker_button = ColorPickerButton(self.frame, self.update)
        color_picker_button.button.grid(row=0, column=2)

        self.frame.grid(row=grid_placement_row, column=grid_placement_column)
        return

    def update(self):
        # TODO
        return

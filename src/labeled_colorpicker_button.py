from tkinter import Frame, Label

from src.colorpickerbutton import ColorPickerButton

template_names = ["Stelum", "Head", "Details", "Details2"]


class LabeledColorPickerButton:

    def __init__(self, master_frame, name, grid_placement_row, grid_placement_column):
        self.colors_data_model = None
        self.template_name = name
        self.frame = Frame(master_frame)

        # template name label
        self.template_label = Label(self.frame, text=self.template_name)
        self.template_label.grid(row=0, column=0)

        # color label
        self.color_label = Label(self.frame, text="0xffffff")
        self.color_label.grid(row=0, column=1)

        # color picker button
        self.color_picker_button = ColorPickerButton(self.frame, template_names.index(self.template_name), self.update)
        self.color_picker_button.button.grid(row=0, column=2)

        self.frame.grid(row=grid_placement_row, column=grid_placement_column)
        return

    def attach_colors_data_model(self, colors_data_model):
        self.colors_data_model = colors_data_model
        self.colors_data_model.subscribe(self)
        self.color_picker_button.attach_colors_data_model(self.colors_data_model)

    def on_color_update(self):
        color = self.colors_data_model.get_color_as_int(template_names.index(self.template_name))
        text = str(hex(color))
        self.color_label.configure(text=text)

    def update(self):
        color = self.color_picker_button.current_color
        text = str(hex(color))
        self.color_label.configure(text=text)

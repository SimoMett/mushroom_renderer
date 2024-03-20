import random

import numpy as np
from kivy.app import App
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

from src.draw_fungus import draw_fungus, WARPED_FUNGUS_TYPE, CRIMSON_FUNGUS_TYPE


class FungusModel:
    def __init__(self):
        self.__colors = [0xffffff for i in range(4)]
        self.__editing_id = 0
        self.type = CRIMSON_FUNGUS_TYPE
        self.observers = []

    def colors(self):
        return self.__colors

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self):
        for obs in self.observers:
            obs.update_texture()
        return

    def switch_type(self):
        if self.type == CRIMSON_FUNGUS_TYPE:
            self.type = WARPED_FUNGUS_TYPE
        else:
            self.type = CRIMSON_FUNGUS_TYPE
        self.notify()

    def change_stelum_random(self):
        self.change_color(0, random.randint(0, 0xffffff))

    def change_head_random(self):
        self.change_color(1, random.randint(0, 0xffffff))

    def change_details1_random(self):
        self.change_color(2, random.randint(0, 0xffffff))

    def change_details2_random(self):
        self.change_color(3, random.randint(0, 0xffffff))

    def change_color_random(self):
        self.change_colors([random.randint(0, 0xffffff) for i in range(4)])

    def change_color(self, _id, color):
        self.__colors[_id] = color
        self.notify()

    def change_colors(self, colors):
        self.__colors = colors
        self.notify()

    def editing(self, _id):
        self.__editing_id = _id

    def get_editing_id(self):
        return self.__editing_id


fungus_model = FungusModel()


class FungusImage(Image):
    def __init__(self, **kwargs):
        super(FungusImage, self).__init__(**kwargs)
        fungus_model.subscribe(self)
        texture = Texture.create(size=(16, 16), colorfmt="rgba")
        source = draw_fungus(fungus_model.colors(), fungus_model.type)
        texture.blit_buffer(np.flipud(source).tobytes(order="A"), bufferfmt="ubyte", colorfmt="rgba")
        self.texture = texture
        # size and display
        # img.size_hint_x = None
        # img.size_hint_y = None
        # img.width = 550
        # img.height = 550
        self.allow_stretch = True
        self.texture.mag_filter = 'nearest'

    def update_texture(self):
        texture = Texture.create(size=(16, 16), colorfmt="rgba")
        source = draw_fungus(fungus_model.colors(), fungus_model.type)
        texture.blit_buffer(np.flipud(source).tobytes(order="A"), bufferfmt="ubyte", colorfmt="rgba")
        self.texture = texture
        self.allow_stretch = True
        self.texture.mag_filter = 'nearest'


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        self.fungus_image = FungusImage()
        layout.add_widget(self.fungus_image)

        grid_layout = GridLayout(cols=2)

        type_button, save_button = Button(text="Type"), Button(text="Save")
        stelum_button, random_stelum_button = Button(text='Stelum'), Button(text='Random stelum')
        head_button, random_head_button = Button(text='Head'), Button(text='Random head')
        details1_button, random_details1_button = Button(text='Details1'), Button(text='Random details1')
        details2_button, random_details2_button = Button(text='Details2'), Button(text='Random details2')

        type_button.bind(on_release=self.switch_fungus_type)
        stelum_button.bind(on_release=self.open_colorpicker)
        head_button.bind(on_release=self.open_colorpicker)
        details1_button.bind(on_release=self.open_colorpicker)
        details2_button.bind(on_release=self.open_colorpicker)
        random_stelum_button.bind(on_release=self.change_stelum_random)
        random_head_button.bind(on_release=self.change_head_random)
        random_details1_button.bind(on_release=self.change_details1_random)
        random_details2_button.bind(on_release=self.change_details2_random)

        grid_layout.add_widget(type_button)
        grid_layout.add_widget(save_button)
        grid_layout.add_widget(stelum_button)
        grid_layout.add_widget(random_stelum_button)
        grid_layout.add_widget(head_button)
        grid_layout.add_widget(random_head_button)
        grid_layout.add_widget(details1_button)
        grid_layout.add_widget(random_details1_button)
        grid_layout.add_widget(details2_button)
        grid_layout.add_widget(random_details2_button)

        layout.add_widget(grid_layout)
        random_all_button = Button(text='Random all')
        random_all_button.bind(on_release=self.change_color_random)
        layout.add_widget(random_all_button)
        self.add_widget(layout)

    def open_colorpicker(self, instance):
        names_list = ["Stelum", "Head", "Details1", "Details2"]
        _id = names_list.index(instance.text)
        assert 0 <= _id < 4
        global fungus_model
        fungus_model.editing(_id)
        self.manager.current = 'screen2'

    def switch_fungus_type(self, *args):
        global fungus_model
        fungus_model.switch_type()

    def change_stelum_random(self, *args):
        global fungus_model
        fungus_model.change_stelum_random()

    def change_head_random(self, *args):
        global fungus_model
        fungus_model.change_head_random()

    def change_details1_random(self, *args):
        global fungus_model
        fungus_model.change_details1_random()

    def change_details2_random(self, *args):
        global fungus_model
        fungus_model.change_details2_random()

    def change_color_random(self, *args):
        global fungus_model
        fungus_model.change_color_random()


class ColorPickerScreen(Screen):

    def __init__(self, **kwargs):
        super(ColorPickerScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        self.fungus_image = FungusImage()
        layout.add_widget(self.fungus_image)

        self.previous_colors = fungus_model.colors()
        self.colorpicker = ColorPicker()
        self.colorpicker.bind(color=self.on_color)
        layout.add_widget(self.colorpicker)

        grid_layout = GridLayout(cols=2)
        ok_button = Button(text="Ok")
        ok_button.bind(on_release=self.confirm)
        cancel_button = Button(text="Cancel")
        cancel_button.bind(on_release=self.rollback)
        grid_layout.add_widget(ok_button)
        grid_layout.add_widget(cancel_button)

        layout.add_widget(grid_layout)

        self.add_widget(layout)

    def confirm(self, *args):
        self.manager.current = 'screen1'

    def rollback(self, *args):
        # rollback to previous colors
        global fungus_model
        fungus_model.change_colors(self.previous_colors)
        self.manager.current = 'screen1'

    def on_enter(self, *args):
        global fungus_model
        self.previous_colors = fungus_model.colors().copy()

        # update color picker
        curr_col = self.previous_colors[fungus_model.get_editing_id()]

        r = (curr_col >> 16) / 255.0
        g = ((curr_col >> 8) & 0xff) / 255.0
        b = (curr_col & 0xff) / 255.0
        self.colorpicker.set_color([r, g, b, 1.0])

    def on_color(self, instance, value):
        # update image
        color = (int(value[0] * 255) << 16) + (int(value[1] * 255) << 8) + int(value[2] * 255)
        global fungus_model
        fungus_model.change_color(fungus_model.get_editing_id(), color)


class MycologyApp(App):

    def build(self):
        screen_manager = ScreenManager(transition=NoTransition())
        screen1 = MainScreen(name='screen1')
        screen2 = ColorPickerScreen(name='screen2')
        screen_manager.add_widget(screen1)
        screen_manager.add_widget(screen2)
        return screen_manager


if __name__ == '__main__':
    MycologyApp().run()

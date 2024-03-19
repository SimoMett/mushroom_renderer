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
        self.colors = [0xffffff for i in range(4)]
        self.preview_colors = self.colors
        self.type = CRIMSON_FUNGUS_TYPE
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self):
        for obs in self.observers:
            obs.update_texture()
        return

    def apply_preview_colors(self):
        self.colors = self.preview_colors

    def switch_type(self):
        if self.type == CRIMSON_FUNGUS_TYPE:
            self.type = WARPED_FUNGUS_TYPE
        else:
            self.type = CRIMSON_FUNGUS_TYPE
        self.notify()

    def change_stelum_random(self):
        self.colors[0] = random.randint(0, 0xffffff)
        self.notify()

    def change_head_random(self):
        self.colors[1] = random.randint(0, 0xffffff)
        self.notify()

    def change_details1_random(self):
        self.colors[2] = random.randint(0, 0xffffff)
        self.notify()

    def change_details2_random(self):
        self.colors[3] = random.randint(0, 0xffffff)
        self.notify()

    def change_color_random(self):
        self.colors = [random.randint(0, 0xffffff) for i in range(4)]
        self.notify()


fungus_model = FungusModel()


class FungusImage(Image):
    def __init__(self, **kwargs):
        super(FungusImage, self).__init__(**kwargs)
        fungus_model.subscribe(self)
        texture = Texture.create(size=(16, 16), colorfmt="rgba")
        source = draw_fungus(fungus_model.colors, fungus_model.type)
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
        source = draw_fungus(fungus_model.colors, fungus_model.type)
        texture.blit_buffer(np.flipud(source).tobytes(order="A"), bufferfmt="ubyte", colorfmt="rgba")
        self.texture = texture
        self.allow_stretch = True
        self.texture.mag_filter = 'nearest'


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        self.fungus_image = FungusImage()
        fungus_model.subscribe(self.fungus_image)
        layout.add_widget(self.fungus_image)

        grid_layout = GridLayout(cols=2)

        type_button = Button(text="Type")
        type_button.bind(on_release=self.switch_fungus_type)
        save_button = Button(text="Save")
        stelum_button = Button(text='Stelum')
        random_stelum_button = Button(text='Random stelum')
        random_head_button = Button(text='Random head')
        random_details1_button = Button(text='Random details1')
        random_details2_button = Button(text='Random details2')

        stelum_button.bind(on_release=self.changer)
        random_stelum_button.bind(on_release=self.change_stelum_random)
        random_head_button.bind(on_release=self.change_head_random)
        random_details1_button.bind(on_release=self.change_details1_random)
        random_details2_button.bind(on_release=self.change_details2_random)

        grid_layout.add_widget(type_button)
        grid_layout.add_widget(save_button)
        grid_layout.add_widget(stelum_button)
        grid_layout.add_widget(random_stelum_button)
        grid_layout.add_widget(Button(text='Head'))
        grid_layout.add_widget(random_head_button)
        grid_layout.add_widget(Button(text='Details1'))
        grid_layout.add_widget(random_details1_button)
        grid_layout.add_widget(Button(text='Details2'))
        grid_layout.add_widget(random_details2_button)

        layout.add_widget(grid_layout)
        random_all_button = Button(text='Random all')
        random_all_button.bind(on_release=self.change_color_random)
        layout.add_widget(random_all_button)
        self.add_widget(layout)

    def changer(self, *args):
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


class SecondScreen(Screen):

    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        self.fungus_image = FungusImage()
        fungus_model.subscribe(self.fungus_image)
        layout.add_widget(self.fungus_image)

        colorpicker = ColorPicker()
        layout.add_widget(colorpicker)

        grid_layout = GridLayout(cols=2)
        ok_button = Button(text="ok")
        ok_button.bind(on_release=self.changer)
        cancel_button = Button(text="cancel")
        cancel_button.bind(on_release=self.changer)
        grid_layout.add_widget(ok_button)
        grid_layout.add_widget(cancel_button)

        layout.add_widget(grid_layout)

        self.add_widget(layout)

    def changer(self, *args):
        self.manager.current = 'screen1'


class MycologyApp(App):

    def build(self):
        screen_manager = ScreenManager(transition=NoTransition())
        screen1 = MainScreen(name='screen1')
        screen2 = SecondScreen(name='screen2')
        screen_manager.add_widget(screen1)
        screen_manager.add_widget(screen2)
        return screen_manager


if __name__ == '__main__':
    MycologyApp().run()

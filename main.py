import numpy as np
from kivy.app import App
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition

from src.draw_fungus import draw_fungus, WARPED_FUNGUS_TYPE


class FungusImage(Image):
    def __init__(self, **kwargs):
        super(FungusImage, self).__init__(**kwargs)
        texture = Texture.create(size=(16, 16), colorfmt="rgba")
        source = draw_fungus([0xFFF7E7, 0xFFF7E7, 0xC7C1B4, 0xA8A398], WARPED_FUNGUS_TYPE)
        texture.blit_buffer(np.flipud(source).tobytes(order="A"), bufferfmt="ubyte", colorfmt="rgba")
        self.texture = texture
        # size and display
        # img.size_hint_x = None
        # img.size_hint_y = None
        # img.width = 550
        # img.height = 550
        self.allow_stretch = True
        self.texture.mag_filter = 'nearest'


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        layout.add_widget(FungusImage())

        grid_layout = GridLayout(cols=2)
        testButton = Button(text='Stelum')
        testButton.bind(on_release=self.changer)
        grid_layout.add_widget(testButton)
        grid_layout.add_widget(Button(text='Random stelum'))
        grid_layout.add_widget(Button(text='Head'))
        grid_layout.add_widget(Button(text='Random head'))
        grid_layout.add_widget(Button(text='Details1'))
        grid_layout.add_widget(Button(text='Random details1'))
        grid_layout.add_widget(Button(text='Details2'))
        grid_layout.add_widget(Button(text='Random details2'))

        layout.add_widget(grid_layout)
        layout.add_widget(Button(text='Random all'))
        self.add_widget(layout)

    def changer(self, *args):
        self.manager.current = 'screen2'


class SecondScreen(Screen):

    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(FungusImage())
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

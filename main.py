import numpy as np
from kivy.app import App
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

from src.draw_fungus import draw_fungus, WARPED_FUNGUS_TYPE


def get_fungus_image_widget():
    image = Image()
    texture = Texture.create(size=(16, 16), colorfmt="rgba")
    source = draw_fungus([0xFFF7E7, 0xFFF7E7, 0xC7C1B4, 0xA8A398], WARPED_FUNGUS_TYPE)
    texture.blit_buffer(np.flipud(source).tobytes(order="A"), bufferfmt="ubyte", colorfmt="rgba")
    image.texture = texture
    # size and display
    # img.size_hint_x = None
    # img.size_hint_y = None
    # img.width = 550
    # img.height = 550
    image.allow_stretch = True
    image.texture.mag_filter = 'nearest'
    return image





def get_main_screen():
    layout = BoxLayout(orientation='vertical')

    layout.add_widget(get_fungus_image_widget())

    gridLayout = GridLayout(cols=2)
    testButton = Button(text='Stelum')
    testButton.bind(on_release=MycologyApp.button_press)
    gridLayout.add_widget(testButton)
    gridLayout.add_widget(Button(text='Random stelum'))
    gridLayout.add_widget(Button(text='Head'))
    gridLayout.add_widget(Button(text='Random head'))
    gridLayout.add_widget(Button(text='Details1'))
    gridLayout.add_widget(Button(text='Random details1'))
    gridLayout.add_widget(Button(text='Details2'))
    gridLayout.add_widget(Button(text='Random details2'))

    layout.add_widget(gridLayout)
    layout.add_widget(Button(text='Random all'))
    screen = Screen(name="prima")
    screen.add_widget(layout)
    return screen


def get_second_screen():
    layout = BoxLayout(orientation='vertical')

    layout.add_widget(get_fungus_image_widget())

    colorpicker = ColorPicker()
    layout.add_widget(colorpicker)

    screen = Screen(name="seconda")
    screen.add_widget(layout)
    return screen


class MycologyApp(App):


    def build(self):
        self.sm = ScreenManager()
        self.main_screen = get_main_screen()
        self.sm.add_widget(self.main_screen)
        self.second_screen = get_second_screen()
        self.sm.add_widget(self.second_screen)

        return get_main_screen()

    def button_press(self):
        self.sm.switch_to(self.second_screen)
        print("test")


if __name__ == '__main__':
    MycologyApp().run()

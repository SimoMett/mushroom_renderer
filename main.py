import numpy as np
from kivy.app import App
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

from src.draw_fungus import draw_fungus, WARPED_FUNGUS_TYPE


class MycologyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        image = Image()
        texture = Texture.create(size=(16, 16), colorfmt="rgba")
        source = draw_fungus([0xFFF7E7, 0xFFF7E7, 0xC7C1B4, 0xA8A398], WARPED_FUNGUS_TYPE)
        texture.blit_buffer(np.flipud(source).tobytes(order="A"), bufferfmt="ubyte", colorfmt="rgba")
        image.texture = texture
        # size and display
        #img.size_hint_x = None
        #img.size_hint_y = None
        #img.width = 550
        #img.height = 550
        image.allow_stretch = True
        image.texture.mag_filter = 'nearest'
        ##
        layout.add_widget(image)

        gridLayout = GridLayout(cols=2)
        gridLayout.add_widget(Button(text='Stelum'))
        gridLayout.add_widget(Button(text='Random stelum'))
        gridLayout.add_widget(Button(text='Head'))
        gridLayout.add_widget(Button(text='Random head'))
        gridLayout.add_widget(Button(text='Details1'))
        gridLayout.add_widget(Button(text='Random details1'))
        gridLayout.add_widget(Button(text='Details2'))
        gridLayout.add_widget(Button(text='Random details2'))

        layout.add_widget(gridLayout)
        layout.add_widget(Button(text='Random all'))
        return layout


if __name__ == '__main__':
    MycologyApp().run()

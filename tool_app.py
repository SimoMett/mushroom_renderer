from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


class MycologyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        img = Image(source='res/icon.png')
        # size and display
        img.size_hint_x = None
        img.size_hint_y = None
        img.width = 500
        img.height = 500
        img.allow_stretch = True
        img.texture.mag_filter = 'nearest'
        ##
        layout.add_widget(img)
        layout.add_widget(Button(text='Hello 1'))
        layout.add_widget(Button(text='World 1'))
        return layout


if __name__ == '__main__':
    MycologyApp().run()
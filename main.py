from kivy.app import App
from Widgets.classWidgets import *
from kivy.lang import Builder
from os import listdir

Builder.load_file('styles.kv')

kv_path = "./Widgets/kvWidgets/"
for kv in listdir(kv_path):
    Builder.load_file(kv_path + kv)


class Magicolor(App):
    def build(self):
        return MainLayout()


Window.fullscreen = True
Window.clearcolor = (48 / 255.0, 51 / 255.0, 52 / 255.0, 255 / 255.0)
Magicolor().run()

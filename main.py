from kivy.app import App
from Widgets.classWidgets import *
from kivy.lang import Builder
from os import listdir


kv_path = "./Widgets/kvWidgets/"
for kv in listdir(kv_path):
    Builder.load_file(kv_path + kv)


class Magicolor(App):
    def build(self):
        return MainLayout()

Window.size = 740,440
Window.clearcolor = (48 / 255.0, 51 / 255.0, 52 / 255.0, 255 / 255.0)
Magicolor().run()

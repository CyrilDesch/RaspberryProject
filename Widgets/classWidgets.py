from kivy.graphics import CanvasBase, RoundedRectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from data import *
from kivy.core.window import Window


class Selector(BoxLayout):
    def __init__(self, nb, color, index, **kwargs):
        super(Selector, self).__init__(**kwargs)
        self.add_widget(Label(text="[font=montserrat.ttf]" + str(nb) + "  =[/font]", markup=True))
        button = Button(background_color=(0,0,0,0))
        canvas = CanvasBase()
        canvas.add(Color(1,1,1))
        canvas.add(RoundedRectangle(pos=[58.5, Window.size[1]-54.5-index*62.5], size=[43,43], radius=[11, ]))
        canvas.add(Color(rgba=color))
        canvas.add(RoundedRectangle(pos=[60, Window.size[1]-53-index*62.5], size=[40,40], radius=[10, ]))
        button.canvas = canvas
        self.add_widget(button)


class List(StackLayout):
    def __init__(self, **kwargs):
        super(List, self).__init__(**kwargs)
        self.size_hint = [0.9, 0.96]
        self.orientation = "tb-lr"
        self.spacing = 12
        index = 0
        for group in listData[0]:
            self.add_widget(Selector(group.get("number"), group.get("color"), index))
            index += 1


class MainLayout(BoxLayout):
    pass

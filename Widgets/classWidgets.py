import numpy as np
from kivy.graphics import CanvasBase, RoundedRectangle, Color
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from data import *
from kivy.core.window import Window


# LEFT LAYOUT

class Selector(BoxLayout):
    def __init__(self, nb, color, index, selectedNumberColor, showSelectedColor, **kwargs):
        super(Selector, self).__init__(**kwargs)
        self.selectedNumberColor = selectedNumberColor
        self.showSelectedColor = showSelectedColor
        self.nb = nb
        self.add_widget(Label(text="[font=montserrat.ttf]" + str(nb) + "  =[/font]", markup=True))
        button = Button(background_color=(0, 0, 0, 0))
        canvas = CanvasBase()
        canvas.add(Color(1, 1, 1))
        canvas.add(RoundedRectangle(pos=[58.5, Window.size[1] - 54.5 - index * 62.5], size=[43, 43], radius=[11, ]))
        canvas.add(Color(rgba=color))
        canvas.add(RoundedRectangle(pos=[60, Window.size[1] - 53 - index * 62.5], size=[40, 40], radius=[10, ]))
        button.canvas = canvas
        button.bind(on_touch_down=self.selectButton)
        self.add_widget(button)

    def selectButton(self, any, touche):
        if self.collide_point(*touche.pos):
            self.selectedNumberColor[0] = self.nb
            if self.showSelectedColor[0] is not None:
                canvas = CanvasBase()
                canvas.add(Color(1, 1, 1))
                canvas.add(RoundedRectangle(pos=[58.5, Window.size[1] - 54.5 - 4 * 62.5], size=[43, 43], radius=[11, ]))
                canvas.add(Color(rgba=listData[0].get("colors")[self.nb - 1].get("color")))
                canvas.add(RoundedRectangle(pos=[60, Window.size[1] - 53 - 4 * 62.5], size=[40, 40], radius=[10, ]))
                self.showSelectedColor[0].canvas.clear()
                self.showSelectedColor[0].canvas.add(canvas)
        pass


class ShowSelectedColor(Button):
    def __init__(self, **kwargs):
        super(ShowSelectedColor, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        canvas = CanvasBase()
        canvas.add(Color(1, 1, 1))
        canvas.add(RoundedRectangle(pos=[58.5, Window.size[1] - 54.5 - 4 * 62.5], size=[43, 43], radius=[11, ]))
        canvas.add(Color(rgba=listData[0].get("colors")[0].get("color")))
        canvas.add(RoundedRectangle(pos=[60, Window.size[1] - 53 - 4 * 62.5], size=[40, 40], radius=[10, ]))
        self.canvas = canvas


class List(StackLayout):
    def __init__(self, selectedNumberColor, **kwargs):
        super(List, self).__init__(**kwargs)
        self.size_hint = [0.9, 0.96]
        self.orientation = "tb-lr"
        self.spacing = 12
        self.showSelectedColor = []
        self.showSelectedColor.append(ShowSelectedColor())
        index = 0
        for group in listData[0].get("colors"):
            self.add_widget(Selector(group.get("number"), group.get("color"), index, selectedNumberColor, self.showSelectedColor))
            index += 1
        self.add_widget(self.showSelectedColor[0])


class LeftLayout(AnchorLayout):
    def __init__(self, selectedNumberColor, **kwargs):
        super(LeftLayout, self).__init__(**kwargs)
        self.add_widget(List(selectedNumberColor))


# RIGHT LAYOUT

class MagicImage(FloatLayout):
    def __init__(self, selectedNumberColor, **kwargs):
        super(MagicImage, self).__init__(**kwargs)
        image = Image()
        image.pos_hint = {'center_y': 0.5, 'center_x': 0.5}
        image.source = './Images/0.png'
        image.size_hint = 0.9, 0.9
        image.allow_stretch = True
        self.image = image
        self.add_widget(image)
        for dataCalcul in listData[0].get("calculLayout"):
            self.add_widget(calcul(dataCalcul, selectedNumberColor, image))


class RightLayout(AnchorLayout):
    def __init__(self, selectedNumberColor, **kwargs):
        super(RightLayout, self).__init__(**kwargs)
        self.add_widget(MagicImage(selectedNumberColor))


# MAIN LAYOUT

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.selectedNumberColor = np.empty(2)
        self.selectedNumberColor[0] = 1
        self.selectedNumberColor[1] = 0
        self.add_widget(LeftLayout(self.selectedNumberColor), 2)
        self.add_widget(RightLayout(self.selectedNumberColor))

    pass


#### CREATE MANY TEXT WITH ON CLICK ETC
class calcul(Button):
    def __init__(self, data, selectedNumberColor, image, **kwargs):
        super(calcul, self).__init__(**kwargs)
        self.image = image
        self.selectedNumberColor = selectedNumberColor
        self.data = data
        self.color = [1, 0, 0, 1]
        self.size = (50, 20)
        self.font_size = 11
        self.background_color = [0, 0, 0, 0]
        self.size_hint = None, None
        self.markup = True
        self.text = "[font=montserratbold.ttf]" + data.get("calcul") + "[/font]"
        self.pos = data.get("pos")

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.selectedNumberColor[0] == self.data.get("result"):
                for color in listData[0].get("colors"):
                    if color.get("number") == self.data.get("result"):
                        if self.color != color.get("color"):
                            self.color = color.get("color")
                            self.selectedNumberColor[1] = self.selectedNumberColor[1] + 1
            if self.selectedNumberColor[1] == len(listData[0].get("calculLayout")):
                self.image.source = './Images/0_colored.png'
        pass

    pass

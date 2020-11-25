from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
import pyqrcode


username_input = """
MDTextField:
    hint_text: "Enter Text or Link"
    helper_text: "Enter Text or Link"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""

class QrApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        self.username = Builder.load_string(username_input)
        button = MDRectangleFlatButton(text='Generate Qr code',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.create)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def create(self,obj):
        url=pyqrcode.create(self.username.text)
        url.png('qrcode.png',scale=8)

QrApp().run()

import os
import sys
import webbrowser
import requests
import threading
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton

os.chdir(os.path.dirname(os.path.abspath(__file__)))

LongTexsts = {
    "Text 1": ("-Because our application has many systems that operate on 3 level of devices")
}

AppLinks = {
    # texss youtube
    "Texss Youtube": ("https://m.youtube.com/@Texss-1"),
    # -------------------------------------------------
    # texss itch.io
    "Texss Itch.io": ("https://texss.itch.io/"),
}

AppManager = """
MDScreen:
    md_bg_color: 0.05, 0.05, 0.07, 1

    FloatLayout:
        id: main_container
"""

MainScene = """
FloatLayout:
    MDLabel:
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        theme_text_color: "Custom"
        text: "Hi & Welcome to Texss Systems Store"
        text_color: 1, 1, 1, 1
        
    MDRaisedButton:
        text: "Devices Level"
        font_size: "18sp"
        size_hint: (0.6, 0.08)
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        md_bg_color: 0, 0.5, 1, 1
        text_color: 1, 1, 1, 1
        on_release: app.switch_scene(__import__('__main__').DevicesLevelScene)
"""

DevicesLevelScene = """
FloatLayout:
    MDLabel:
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        font_size: "14sp"
        size_hint: (0.6, 0.08)
        theme_text_color: "Custom"
        text: "Choose Your Device Level"
        text_color: 0.4, 0.85, 0.3, 1
        
    MDLabel:
        halign: 'center'
        pos_hint: {'center_x': 0.3, 'center_y': 0.2}
        font_size: "12sp"
        size_hint: (0.6,0.08)
        theme_text_color: "Custom"
        text: "Why We Ask You What's Your Device Level ?"
        text_color: 1, 0.8, 0.1, 1
        
    MDLabel:
        halign: 'center'
        pos_hint: {'center_x': 0.3, 'center_y': 0.14}
        font_size: "13sp"
        size_hint: (0.6,0.08)
        theme_text_color: "Custom"
        text: __import__ ("__main__").LongTexsts["Text 1"]
        text_color: 0.9, 0.2, 0.2, 1
        
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {'top': 0.9, 'x': 0.02}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        on_release: app.go_back()
    
    MDRaisedButton:
        text: "Weak Device"
        font_size: "13sp"
        size_hint: (0.3, 0.05)
        pos_hint: {"center_x": 0.18, "center_y": 0.6}
        md_bg_color: 0.9, 0.2, 0.2, 1
        text_color: 1, 1, 1, 1
        on_release: app.switch_scene(__import__('__main__').WeakDevice)
         
    MDRaisedButton:
        text: "Mediume Device"
        font_size: "13sp"
        size_hint: (0.3, 0.05)
        pos_hint: {"center_x": 0.51, "center_y": 0.6}
        md_bg_color: 1, 0.7, 0.1, 1
        text_color: 1, 1, 1, 1
        on_release: app.switch_scene(__import__('__main__').MediumeDevice)
        
    MDRaisedButton:
        text: "Strong Device"
        font_size: "13sp"
        size_hint: (0.3, 0.05)
        pos_hint: {"center_x": 0.84, "center_y": 0.6}
        md_bg_color: 0.1, 0.5, 0.9, 1
        text_color: 1, 1, 1, 1
        on_release: app.switch_scene(__import__('__main__').StrongDevice)
"""

WeakDevice = """
FloatLayout:
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {'top': 0.98, 'x': 0.02}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        on_release: app.go_back()

    ScrollView:
        size_hint: (0.9, 0.8)
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}

        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: "60dp"

            MDLabel:
                text: "Choose the distro you want for your device"
                adaptive_height: True
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0.9, 0.2, 0.2, 1
                font_size: "16sp"
          
            Button:
                background_normal: "Images/Q4OS Trinty/Q4OS Trinty Icon.jpg"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "216dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Q4OS Trinty System")
            
            Button:
                background_normal: "Images/Debian/Debian Icon.png"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "222dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Debian")
                
            Button:
                background_normal: "Images/Puppy Linux/Puppy Linux Icon.jpg"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "222dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Puppy Linux")
                
            Button:
                background_normal: "Images/Linux Ubuntu/Linux Ubuntu Icon.jpg"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "195dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Linux Ubuntu")
                
            Button:
                background_normal: "Images/Linux Lite/Linux Lite Icon.jpg"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "216dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Linux Lite")
                
            Button:
                background_normal: "Images/Arch Linux/Arch Linux Icon.jpg"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "216dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Arch Linux")
                
            Button:
                background_normal: "Images/Linux Gentoo/Linux Gentoo Icon.jpg"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "220dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Linux Gentoo")
"""

MediumeDevice = '''
FloatLayout:
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {'top': 0.98, 'x': 0.02}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        on_release: app.go_back()
        
    ScrollView:
        size_hint: (0.9, 0.8)
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}

        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: "60dp"
            
            MDLabel:
                text: "Choose the distro you want for your device"
                adaptive_height: True
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 1, 0.8, 0.1, 1
                font_size: "16sp"
            
            Button:
                background_normal: "Images/Q4OS/Q4OS Icon.png"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "222dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Q4OS Completed Systrm")
            
            Button:
                background_normal: "Images/Kali Linux/Kali Linux Icon.jpg"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "220dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Kali Linux")
            
            Button:
                background_normal: "Images/Windows 10 LTSC/Windows 10 LTSC Icon.png"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "230dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Win 10 LTSC")
                
            Button:
                background_normal: "Images/Windows 10 Pro/Windows 10 Pro Icon.png"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "230dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Win 10 Pro")
                
            Button:
                background_normal: "Images/Zorin OS/Zorin OS Icon.jpg"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "230dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Zorin OS Core")
                
            Button:
                background_normal: "Images/Linux Mint/Linux Mint Icon.jpg"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "230dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Linux Mint")
'''

StrongDevice = '''
FloatLayout:
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {'top': 0.98, 'x': 0.02}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        on_release: app.go_back()
        
    ScrollView:
        size_hint: (0.9, 0.8)
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}

        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: "60dp"
            
            MDLabel:
                text: "Choose the distro you want for your device"
                adaptive_height: True
                halign: 'center'
                theme_text_color: "Custom"
                text_color: 0.2, 0.7, 1, 1
                font_size: "16sp"
            
            Button:
                background_normal: "Images/Windows 11/Windows 11.png"
                background_color: 1, 1, 1, 1
                size_hint: (None, None)
                size: ("234dp", "220dp")
                pos_hint: {'center_x': 0.5, 'center_y': 0.05}
                on_release: app.open_system_link("Windows 11")
'''


class TexssSystemsStore(MDApp):

    history = []
    current_scene = None
    dialog = None
    SystemWebs = {}
    widgets_cache = {}

    FIREBASE_URL = "https://texss-systems-store-36fa6-default-rtdb.firebaseio.com/SystemWebs.json"

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "700"
        root = Builder.load_string(AppManager)
        self.current_scene = MainScene
        
        first_widget = self.get_widget_for_scene(MainScene)
        root.ids.main_container.add_widget(first_widget)
        return root

    def on_start(self):
        threading.Thread(target=self.fetch_links_from_firebase, daemon=True).start()
        Window.bind(on_keyboard=self.on_back_button)

    def get_widget_for_scene(self, scene_kv):
        if scene_kv not in self.widgets_cache:
            self.widgets_cache[scene_kv] = Builder.load_string(scene_kv)
        return self.widgets_cache[scene_kv]

    def on_back_button(self, window, key, *args):
        if key == 27:
            if self.current_scene == MainScene or not self.history:
                self.show_exit_dialog()
            else:
                self.go_back()
            return True
        return False

    def show_exit_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Exit Continue",
                text="Did You Want To Exit ??",
                buttons=[
                    MDFlatButton(
                        text="Cancle",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                    MDRaisedButton(
                        text="Exit",
                        md_bg_color=(0.9, 0.2, 0.2, 1),
                        on_release=lambda x: self.stop()
                    ),
                ],
            )
        self.dialog.open()

    def show_error_bar(self, msg):
        Snackbar(
            text=msg,
            bg_color=(0.9, 0.1, 0.1, 1),
            duration=5
        ).open()

    def fetch_links_from_firebase(self):
        try:
            response = requests.get(self.FIREBASE_URL, timeout=5)
            if response.status_code == 200 and response.json():
                self.SystemWebs = response.json()
            else:
                Clock.schedule_once(lambda dt: self.show_error_bar("Error reading data from server"))
        except Exception:
            Clock.schedule_once(lambda dt: self.show_error_bar("Connection failed. Check your internet connection"))

    def open_system_link(self, system_name):
        link = self.SystemWebs.get(system_name)
        if link:
            try:
                webbrowser.open(link)
            except Exception:
                self.show_error_bar("Unable to launch browser right now")
        else:
            self.show_error_bar(f"Sorry, link for '{system_name}' is unavailable")


    def switch_scene(self, scene_kv, add_to_history=True, is_back=False):
        if add_to_history and self.current_scene:
            self.history.append(self.current_scene)

        self.current_scene = scene_kv
        container = self.root.ids.main_container
        new_widget = self.get_widget_for_scene(scene_kv)

        Animation.cancel_all(new_widget)

        if not is_back:
            if container.children:
                old_widget = container.children[0]
                Animation.cancel_all(old_widget)
                anim_old = Animation(
                    size_hint=(0.9, 0.9),
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    opacity=0.2,
                    duration=0.22,
                    t='out_quad'
                )
                anim_old.start(old_widget)

            new_widget.size_hint = (0.9, 0.9)
            new_widget.pos_hint = {'center_x': 0.5, 'center_y': -0.4}
            new_widget.opacity = 0
            
            if new_widget.parent:
                new_widget.parent.remove_widget(new_widget)
            container.add_widget(new_widget)

            anim_new = Animation(
                size_hint=(1, 1),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                opacity=1,
                duration=0.25,
                t='out_cubic'
            )

            def on_forward_complete(anim, widget):
                for child in list(container.children):
                    if child != new_widget:
                        container.remove_widget(child)

            anim_new.bind(on_complete=on_forward_complete)
            anim_new.start(new_widget)

        else:
            top_widget = container.children[0]
            Animation.cancel_all(top_widget)
            
            bg_widget = self.get_widget_for_scene(scene_kv)
            Animation.cancel_all(bg_widget)
            bg_widget.size_hint = (0.9, 0.9)
            bg_widget.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            bg_widget.opacity = 0.2
            
            if bg_widget.parent:
                bg_widget.parent.remove_widget(bg_widget)
            container.add_widget(bg_widget, index=len(container.children))

            anim_top = Animation(
                size_hint=(0.85, 0.85),
                pos_hint={'center_x': 0.5, 'center_y': -0.4},
                opacity=0,
                duration=0.22,
                t='in_quad'
            )
            def on_back_complete(anim, widget):
                if widget.parent:
                    container.remove_widget(widget)

            anim_top.bind(on_complete=on_back_complete)
            anim_top.start(top_widget)

            anim_bg = Animation(
                size_hint=(1, 1),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                opacity=1,
                duration=0.4,
                t='out_cubic'
            )
            anim_bg.start(bg_widget)

    def go_back(self):
        if self.history:
            prev_scene = self.history.pop()
            self.switch_scene(prev_scene, add_to_history=False, is_back=True)


if __name__ == "__main__":
    TexssSystemsStore().run()
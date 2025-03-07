from typing import Optional
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivymd.app import MDApp
from mido import MidiFile
import os
import lib.midi_management

global tracks
tracks = []

global filepath
filepath = ''

class HomeScreen(MDScreen):
    pass


class FileChooserScreen(MDScreen):
    loadfile = ObjectProperty(None)
    def load(self, path, filename):
        global filepath
        try:
            self.path = os.path.join(path, filename[0])
            try:
                mid = MidiFile(self.path, clip=True)
                filepath = self.path
                global tracks
                tracks = []
                for i, track in enumerate(mid.tracks):
                    tracks.append('{} (Track {})'.format(track.name, i))
                if len(tracks) > 1:
                    tracks.pop(0)
                    screen_manager.current = "Track"
                    screen_manager.transition.direction = "up"
                else:
                    lib.midi_management.MidiManagement().analyse_track(str(self.path), tracks.pop(0))
                    screen_manager.get_screen("Home").ids.infobox.text = "The command has been copied to the clipboard"
                    screen_manager.current = "Home"
                    screen_manager.transition.direction = "right"
            except Exception as e:
                print(e)
                self.popup_fe = Popup(title="FileError", content=Label(text="Please select a MIDI-File!"),
                            size_hint=(0.4, 0.4), auto_dismiss=True)
                self.popup_fe.open()

        except:
            self.popup_foldererror = Popup(title="FileError", content=Label(text="Only MIDI-Files allowed, not folder"),
                                  size_hint=(0.4, 0.4), auto_dismiss=True)
            self.popup_foldererror.open()


class TrackChooseScreen(MDScreen):
    def show_dropdown(self, button):
        global tracks
        menu_items = []
        for track in tracks:
            menu_items.append(
                {
                    "viewclass": "OneLineListItem",
                    "text": track,
                    "on_release": lambda t=track, menu=None : self.extract(t, menu)
                }
            )

        menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=8,
        )

        # Pass the menu to each item in the lambda callback to dismiss the menu
        for item in menu_items:
            item["on_release"] = lambda track=item["text"], menu=menu: self.extract(track, menu)

        menu.open()

    def extract(self, item: str, menu: Optional[MDDropdownMenu] = None):
        global filepath
        if menu != None:
            menu.dismiss()
        if item == "Select a track":
            popup_ns = Popup(title="NoSelectionError", content=Label(text="Please select a Track!"),
                                  size_hint=(0.4, 0.4), auto_dismiss=True)
            popup_ns.open()
        else:
            lib.midi_management.MidiManagement().analyse_track(str(filepath), item)
            screen_manager.get_screen("Home").ids.infobox.text = "The command has been copied to the clipboard"
            screen_manager.current = "Home"
            screen_manager.transition.direction = "right"



class MidiConverter(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    def build(self):
        self.title = "Midi-Microbit-Converter"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "BlueGray"
        screen_manager.add_widget(Builder.load_file("./gui/gui.kv"))
        screen_manager.add_widget(Builder.load_file("./gui/filechooser.kv"))
        screen_manager.add_widget(Builder.load_file("./gui/loading_screen.kv"))

        return screen_manager

MidiConverter().run()

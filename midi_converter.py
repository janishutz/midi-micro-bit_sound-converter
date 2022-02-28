from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivymd.app import MDApp
from mido import MidiFile
import os
import backend.midi_management
import backend.csv_parsers
import time


class HomeScreen(MDScreen):
    pass


class FileChooserScreen(MDScreen):
    loadfile = ObjectProperty(None)
    def load(self, path, filename):
        try:
            self.path = os.path.join(path, filename[0])
            try:
                self.mid = MidiFile(self.path, clip=True)
                backend.csv_parsers.CsvWrite().write_str("./backend/temp.csv", [self.path])
                self.tracks = []
                for self.track in self.mid.tracks:
                    self.tracks.append(str(self.track))
                self.tracks.pop(0)
                if len(self.tracks) > 1:
                    screen_manager.get_screen("Track").ids.track_spinner.values = self.tracks
                    screen_manager.current = "Track"
                    screen_manager.transition.direction = "up"
                else:
                    screen_manager.current = "Home"
                    screen_manager.transition.direction = "right"
            except:
                self.popup_fe = Popup(title="FileError", content=Label(text="Please select a MIDI-File!"),
                            size_hint=(0.4, 0.4), auto_dismiss=True)
                self.popup_fe.open()

        except:
            self.popup_foldererror = Popup(title="FileError", content=Label(text="Only MIDI-Files allowed, not folder"),
                                  size_hint=(0.4, 0.4), auto_dismiss=True)
            self.popup_foldererror.open()


class TrackChooseScreen(MDScreen):
    def extract(self):
        self.chosen_track = self.ids.track_spinner.text
        if self.chosen_track == "Select a track":
            self.popup_ns = Popup(title="NoSelectionError", content=Label(text="Please select a Track!"),
                                  size_hint=(0.4, 0.4), auto_dismiss=True)
            self.popup_ns.open()
        else:
            self.path = backend.csv_parsers.CsvRead().importing("./backend/temp.csv").pop(0)
            self.path_transmit = self.path.pop(0)
            backend.midi_management.MidiManagement().analyse_track(str(self.path_transmit), self.chosen_track)
            print("go")
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
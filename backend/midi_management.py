from mido import MidiFile
import pyperclip as pc


class MidiManagement:
    def __init__(self):
        pass

    def addToClipboard(self, text):
        pc.copy(text)

    def analyse_track(self, path, trackname):
        self.midi_imp = MidiFile(path, clip=True)
        self.tracks = []
        for self.track in self.midi_imp.tracks:
            self.tracks.append(str(self.track))
        self.tracks.pop(0)
        self.track_ext = self.tracks.pop(0)
        self.trackn = 0
        while self.track_ext != trackname:
            self.track_ext = self.tracks.pop(0)
            self.trackn += 1
        self.extracted_track = self.track_ext
        self.__output_list = []
        for self.msg in self.midi_imp.tracks[self.trackn]:
            self.ext = str(self.msg)
            self.note = self.ext[23:25]
            try:
                self.note_height = int(self.note)
                self.note_decod_oct = self.note_height // 12
                self.note_decode_tone = self.note_height % 12
                if self.note_decode_tone == 1:
                    self.note_ext = "C"
                elif self.note_decode_tone == 2:
                    self.note_ext = "C#"
                elif self.note_decode_tone == 3:
                    self.note_ext = "D"
                elif self.note_decode_tone == 4:
                    self.note_ext = "D#"
                elif self.note_decode_tone == 5:
                    self.note_ext = "E"
                elif self.note_decode_tone == 6:
                    self.note_ext = "F"
                elif self.note_decode_tone == 7:
                    self.note_ext = "F#"
                elif self.note_decode_tone == 8:
                    self.note_ext = "G"
                elif self.note_decode_tone == 9:
                    self.note_ext = "G#"
                elif self.note_decode_tone == 10:
                    self.note_ext = "A"
                elif self.note_decode_tone == 11:
                    self.note_ext = "A#"
                elif self.note_decode_tone == 12:
                    self.note_ext = "H"

                self.ext_shortened = self.ext[40:]
                self.pos = 0
                for buchstabe in self.ext_shortened:
                    if buchstabe == "=":
                        self.pos += 1
                        break
                    else:
                        self.pos += 1

                self.timing_exp = self.ext_shortened[self.pos:]
                self.__output = self.note_ext
                self.__output += f":{self.timing_exp}"
                self.__output_list.append(str(self.__output))

            except:
                pass

        self.addToClipboard(str(self.__output_list))




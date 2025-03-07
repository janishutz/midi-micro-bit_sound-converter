from mido import MidiFile
import pyperclip as pc


class MidiManagement:
    def __init__(self):
        pass

    def addToClipboard(self, text):
        pc.copy(text)

    def analyse_track(self, path, trackname):
        mid = MidiFile(path, clip=True)
        tracks = []
        for i, track in enumerate(mid.tracks):
            tracks.append('{} (Track {})'.format(track.name, i))
        if len(tracks) > 1:
            tracks.pop(0)
        else:
            pass
        extracted_track = tracks.pop(0)
        tracknumber = 0
        while extracted_track != trackname:
            extracted_track = tracks.pop(0)
            tracknumber += 1
        output_list = []

        # Track messages
        for msg in mid.tracks[tracknumber]:
            midi_msg = str(msg)
            if midi_msg[0:8] == "note_on ":
                try:
                    msg_loc = midi_msg.index('note=')
                    note = midi_msg[msg_loc + 5:msg_loc + 7]
                    note_height = int(note)
                    note_decod_oct = note_height // 12
                    note_decode_tone = note_height % 12
                    note_ext = ""
                    if note_decode_tone == 1:
                        note_ext = "C"
                    elif note_decode_tone == 2:
                        note_ext = "C#"
                    elif note_decode_tone == 3:
                        note_ext = "D"
                    elif note_decode_tone == 4:
                        note_ext = "D#"
                    elif note_decode_tone == 5:
                        note_ext = "E"
                    elif note_decode_tone == 6:
                        note_ext = "F"
                    elif note_decode_tone == 7:
                        note_ext = "F#"
                    elif note_decode_tone == 8:
                        note_ext = "G"
                    elif note_decode_tone == 9:
                        note_ext = "G#"
                    elif note_decode_tone == 10:
                        note_ext = "A"
                    elif note_decode_tone == 11:
                        note_ext = "A#"
                    elif note_decode_tone == 12:
                        note_ext = "H"

                    ext_shortened = midi_msg[40:]
                    pos = 0
                    for buchstabe in ext_shortened:
                        if buchstabe == "=":
                            pos += 1
                            break
                        else:
                            pos += 1

                    timing_exp = ext_shortened[pos:]
                    output = note_ext
                    output += str(note_decod_oct)
                    output += f":{timing_exp}"
                    output_list.append(str(output))

                except:
                    pass
            elif midi_msg[0:8] == "note_off":
                ext_shortened = midi_msg[40:]
                pos = 0
                for buchstabe in ext_shortened:
                    if buchstabe == "=":
                        pos += 1
                        break
                    else:
                        pos += 1
                output = "R"
                output += f":{pos}"

                timing_exp = ext_shortened[pos:]
                output_list.append(output)
            else:
                pass

        self.addToClipboard(str(output_list))


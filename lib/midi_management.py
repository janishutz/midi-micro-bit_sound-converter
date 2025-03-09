from mido import MidiFile, tempo2bpm
import math
import pyperclip as pc


class MidiManagement:
    def __init__(self):
        self.note_reference = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

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

        tracked_notes = []
        bpm = 0
        timing = 20000

        # Track messages
        for msg in mid.tracks[tracknumber]:
            if msg.type == "note_on":
                try:
                    tracked_notes.append(self.get_note_as_micro_bit_string(msg))

                except:
                    pass
            elif msg.type == "note_off":
                # End tracked note at time offset for midi msg (that is relative to start)
                note = ''
                try:
                    note = self.get_note_as_micro_bit_string(msg)
                except:
                    pass

                # Find note in tracked notes, ignore if not in there
                index = -1
                for n in range(len(tracked_notes)):
                    if tracked_notes[n] == note:
                        index = n
                        break;

                # Get duration
                if index >= 0:
                    tracked_notes.remove(note)
                    t = math.floor(msg.time / timing)

                    output_list.append(note + ':' + str(t))
            else:
                try:
                    midi_msg = str(msg)
                    i = midi_msg.index('tempo=') + 6
                    units = int(midi_msg[i:i + midi_msg[i:].index(',')])
                    bpm = int(tempo2bpm(units))
                    timing = int(units / bpm / 16)
                    # timing = units per 1/16 beat
                except:
                    pass

        self.addToClipboard(str(output_list))

    def get_note_as_micro_bit_string(self, midi_msg):
        note_value = midi_msg.note
        octave = note_value // 12
        tone = note_value % 12

        return self.note_reference[tone] + str(octave)


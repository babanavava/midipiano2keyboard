import os
import sys
import threading
import tkinter as tk
from configparser import ConfigParser

import keyboard
import pygame
import pygame.midi


class Midi2KeyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MIDI Piano to Keyboard")
        icon_image = tk.PhotoImage(file=self.resource_path('p2k.png'))
        root.iconphoto(True, icon_image)
        self.running = False
        self.thread = None

        self.toggle_button = tk.Button(root, text="Start", command=self.toggle)
        self.toggle_button.pack(pady=10)

        self.label = tk.Label(root, text="", height=2, width=50, anchor="w", justify="left")
        self.label.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))
        self.config_path = os.path.join(application_path, 'config.ini')

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def toggle(self):
        self.label.config(text="")
        if self.running:
            self.stop()
        else:
            self.start()

    def start(self):
        if not self.running:
            self.running = True
            self.toggle_button.config(text="Stop")
            self.thread = threading.Thread(target=self.run_midi2key)
            self.thread.start()

    def stop(self):
        if self.running:
            self.running = False
            self.toggle_button.config(text="Start")
            if self.thread is not None:
                self.thread.join()

    def on_closing(self):
        self.stop()
        self.root.destroy()
    
    def create_config_file(self):
        if not os.path.exists(self.config_path):
            config = ConfigParser()
            config['misc'] = {
                'midi_input_device_id': 1,
                'octave_shift': 0,
                'transpose': 0,
                'velocity_threshold': 0,
                'all_space': 0
            }

            config['midi2key'] = {
                'Eb3': 'SHIFT',
                'E3': 'CTRL',
                'F3': 'ALT',
                'Gb3': 'z',
                'G3': 'q',
                'Ab3': 'c',
                'A3': 'e',
                'Bb3': 'TAB',
                'B3': 'a',
                'C4': 's',
                'Db4': 'ESCAPE',
                'D4': 'd',
                'Eb4': 'f',
                'E4': 'w',
                'F4': 'g',
                'Gb4': 'y',
                'G4': 'h',
                'Ab4': 'u',
                'A4': 'j',
                'Bb4': 'i',
                'B4': 'k',
                'C5': 'l',
                'Db5': 'o',
                'D5': 'r',
                'Eb5': 't',
                'E5': 'b',
                'F5': 'ENTER',
                'Gb5': 'BACKSPACE',
                'G5': 'SPACE'
            }

            with open(self.config_path, 'w') as configfile:
                config.write(configfile)
            print("config.ini created successfully.")

    def note_to_midi(self, note):
        
        note_dict = {
            "c": 0, "c#": 1, "db": 1, "d": 2, "d#": 3, "eb": 3,
            "e": 4, "f": 5, "f#": 6, "gb": 6, "g": 7, "g#": 8,
            "ab": 8, "a": 9, "a#": 10, "bb": 10, "b": 11
        }

        note_name = note[:-1]
        octave = int(note[-1])
        midi_note = note_dict[note_name] + (octave + 1) * 12

        return midi_note
    
    def midi_to_note_name(self, midi_number):
        note_names = [
            "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"
        ]
        octave = (midi_number // 12) - 1
        note_name = note_names[midi_number % 12]
        full_note_name = f"{note_name}{octave}"
        return full_note_name

    def load_midi2key_from_config(self, config):
        midi2key = {}
        if 'midi2key' in config:
            for key, value in config['midi2key'].items():
                key = self.note_to_midi(key)
                midi2key[int(key)] = value
        return midi2key
    
    def operatia(self, key, release=False):
        if not key == '':
            if release:
                keyboard.release(key)
            else:
                keyboard.press(key)


    def run_midi2key(self):
        if not os.path.exists(self.config_path):
            self.create_config_file()
        pygame.init()
        pygame.midi.init()

        config = ConfigParser()
        config.read(self.config_path)
        try:
            input_device_id = int(config['misc']['midi_input_device_id'])
            midi_input = pygame.midi.Input(input_device_id)

            midi2key = self.load_midi2key_from_config(config)
            threshold = int(config['misc']['velocity_threshold'])
            octave_shift = int(config['misc']['octave_shift'])
            transpose = int(config['misc']['transpose'])
            all_space = config.getboolean('misc', 'all_space')
            
            while self.running:
                if midi_input.poll():
                    midi_events = midi_input.read(10)
                    for midi_event in midi_events:
                        status, note, velocity, _ = midi_event[0]
                        noto = note + octave_shift * -12 - transpose
                        if status & 0xF0 == 0x90 and velocity > threshold:
                            if all_space:
                                keyboard.press('SPACE')
                                self.label.config(text=f"{self.midi_to_note_name(note)}")
                            elif noto in midi2key:
                                key = midi2key[noto]
                                self.operatia(key)
                                self.label.config(text=f"{self.midi_to_note_name(note)}: {key}")

                        elif status & 0xF0 == 0x80 or (status & 0xF0 == 0x90 and velocity <= threshold):
                            if all_space:
                                keyboard.release('SPACE')
                            elif noto in midi2key:
                                key = midi2key[noto]
                                self.operatia(key, release=True)

                if not pygame.get_init():
                    break

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.stop()
                        return

        except Exception as e:
            self.stop()
            self.label.config(text="An error occurred!")

        finally:
            if pygame.midi.get_init():
                pygame.midi.quit()
            if pygame.get_init():
                pygame.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = Midi2KeyApp(root)
    root.mainloop()

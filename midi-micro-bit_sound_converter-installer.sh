#! /bin/bash

sudo apt-get install git

mkdir test_clone && cd ./midi-micro_bit-converter

git clone https://github.com/simplePCBuilding/midi-micro-bit_sound-converter

pip install kivy[base]
pip install kivymd
pip install pyperclip
pip install mido

sudo apt-get install xclip
sudo apt-get install xsel
sudo apt-get install wl-clipboard

cd ./midi-micro-bit_sound-converter
python3 midi_converter.py

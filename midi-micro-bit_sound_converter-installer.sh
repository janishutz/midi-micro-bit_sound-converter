#! /bin/bash

sudo apt-get install git

mkdir ./midi-micro_bit-converter && cd ./midi-micro_bit-converter

git clone https://github.com/simplePCBuilding/midi-micro-bit_sound-converter

pip install kivy[base] kivymd pyperclip mido

sudo apt-get install xclip xsel

cd ./midi-micro-bit_sound-converter
python3 midi_converter.py

<div id="title" align="center">
    <h1>Midi to Micro:bit Sound converter</h1>
</div>

<div id="badges" align="center">
    <img src="https://img.shields.io/github/license/janishutz/midi-micro-bit_sound-converter.svg">
    <img src="https://img.shields.io/github/repo-size/janishutz/midi-micro-bit_sound-converter.svg">
    <img src="https://img.shields.io/github/languages/top/janishutz/midi-micro-bit_sound-converter">
    <img src="https://img.shields.io/github/directory-file-count/janishutz/midi-micro-bit_sound-converter.svg">
    <br>
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/janishutz/midi-micro-bit_sound-converter">
    <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/janishutz/midi-micro-bit_sound-converter">
    <img src="https://img.shields.io/github/issues-pr-raw/janishutz/midi-micro-bit_sound-converter">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/janishutz/midi-micro-bit_sound-converter">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/janishutz/midi-micro-bit_sound-converter">
    <br>
    <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/janishutz/midi-micro-bit_sound-converter/total?label=Downloads (total)">
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/downloads/janishutz/midi-micro-bit_sound-converter/latest/total?label=Downloads (latest)">
    <img src="https://img.shields.io/github/release/janishutz/midi-micro-bit_sound-converter.svg">
    <img src="https://img.shields.io/github/package-json/v/janishutz/midi-micro-bit_sound-converter.svg?label=Development Version">
</div>

This app allows you to convert a midi file to the code needed for micro:bit programming

Creating Music with the micro:bit is a hassle. This little app will allow you to take any midi-file and convert it into the list needed for micro:bit. 

# Installation
Download the files by clicking on code, then on zip or clone the repo locally using 
```
git clone https://github.com/janishutz/midi-micro-bit_sound-converter
```

Then, run 
```
pip install -r requirements.txt
```
in the repo's folder (i.e. the folder you just cloned or downloaded and extracted)

Alternatively, create a venv using
```
python -m venv midi-converter
```

and activate it using
```
source ./midi-converter/bin/active
```

The dependencies of this project are `mido`, `pyperclip`, `kivymd` and `kivy[base]`


# Running
Open a terminal in the file location where you saved / cloned this repo to. Type 
```
python midi_converter.py
```

to run the app


## Notes for Linux users:
On some Linux distros, `xclip` and `xsel` don't come pre-installed. Install these dependencies.


# Development
Be warned, the code base is still very ugly. I only spent about two hours cleaning up the old code, so it still looks ugly. I will probably not clean up the code much more. Some variable names will simply stay weird

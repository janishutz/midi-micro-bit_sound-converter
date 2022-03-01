# midi-micro-bit_sound-converter
This app allows you to convert a midi file to the code needed for micro:bit programming

Creating Music with the micro:bit is a hassle. This little app will allow you to take any midi-file and convert it into the list needed for micro:bit. 

## INSTALLATION:
Download the files by clicking on code, then on zip.
You will need to install some dependencies, as well as python 3.8. If you haven't already go ahead and download python 3.8 and make sure to also include pip,
as this will be used right after. Now, you will need to type the following commands in the terminal / command prompt: 
pip install kivy[base]
pip install kivymd
pip install pyperclip
pip install mido

You can run the app by heading into the folder you downloaded the zip file into, unzipping it and then by running the midi-converter.py file in the terminal / command prompt. (python3 midi-converter.py)
You may do this as follows:
### Linux and MacOS:
Use cd./Path/To/File

### Windows:
Click on the navigation bar (the one where the path is displayed) and type: cmd


### SPECIAL notes for Linux users:
You'll need to install some other dependencies first. Use your distro's package manager (apt-get for Debian based distros, dnf for Fedora based and pacman for arch-based distros). I'll show an example with debian based distros here: (you may also run the script under releases if you run a debian based distro.
sudo apt-get install xclip
sudo apt-get install xsel
sudo apt-get install wl-clipboard

### OTHER OPTION:
You may also run it in a venv (Virtual Environment), e.g. in Thonny. You still must install kivy[base], kivymd, pyperclip and mido in that venv (by using the manager of the IDE you are running)

#AlbusPA 0.2 for Albus2
#Dylan Hamer 2017

from pygame import mixer

#Plugin Definitions (Required by AlbusPM)
version = 0.2 #Version
name = "AlbusPA" #Name of plugin
description = "Audio Player for Albus2" #Description of plugin
author = "Dylan Hamer" #Plugin author
depends = ["pyaudio"] #Plugin dependencies
keyword = "play"

def main(file):
	mixer.init()
	mixer.music.load(file)
	mixer.music.play()
	while mixer.get_busy():
		time.sleep(1)

#AlbusTTS V2.1 for Albus2
#Dylan Hamer 2017

from gtts import gTTS #Now uses gTTS as of 25/3/17 due to a glitch in the ESpeak and PyTTSx modules.
import AlbusPA, time

#Plugin Definitions (Required by AlbusPM)
version = 2.1 #Version
name = "AlbusTTS" #Name of plugin
description = "Provides a speech synthesis service for Albus2" #Description of plugin
author = "Dylan Hamer" #Plugin author
depends = ["espeak*"] #Plugin dependencies
keyword = "speak"

#Main function - called by AlbusPM to provide main function
def main(speech, lng):
	print "Albus: "+speech
	tts = gTTS(text=speech, lang=lng)
	tts.save("Files/speech.mp3")
	AlbusPA.main("Files/speech.mp3")
	time.sleep(1)

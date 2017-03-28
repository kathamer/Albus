#AlbusSR V2.1 for Albus2
#Dylan Hamer 2017

import speech_recognition as sr #Requires SpeechRecognition lib

#Plugin Definitions (Required by AlbusPM)
version = 2.1 #Version
name = "AlbusSR" #Name of plugin
description = "Provides a speech recognition service for Albus2" #Description of plugin
author = "Dylan Hamer" #Plugin author
depends = ["speechrecognition3.5"] #Plugin dependencies
keyword = "listen"

#Main function - called by AlbusPM to provide main function
def main():
	r = sr.Recognizer() #Init recognizer
	print("Say Something!")
	with sr.Microphone() as source: #Use microphone as source
		audio = r.listen(source) #Listen using microphone
	
	try:
		return r.recognize_google(audio)
	except sr.UnknownValueError:
		print "Sorry, didn\'t catch that."
		return ""
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
		return ""


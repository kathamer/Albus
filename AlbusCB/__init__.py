#AlbusTTS V2.1 for Albus2
#Dylan Hamer 2017

import aiml

#Plugin Definitions (Required by AlbusPM)
version = 2.1 #Version
name = "AlbusCB" #Name of plugin
description = "AIML interpreter for Albus" #Description of plugin
author = "Dylan Hamer" #Plugin author
depends = ["AIML"] #Plugin dependencies
keyword = "chat" #Activation keyword

kernel = aiml.Kernel()
kernel.learn("AIML/std-startup.xml")
kernel.respond("load aiml")

#Main function - called by AlbusPM to provide main function
def main(inp):
	return kernel.respond(inp)

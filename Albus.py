#Albus 2.1
#By Dylan Hamer

import PluginManager, InputProvider, OutputProvider, PrimaryProcessProvider, time

InputProvider.textmode = 1
OutputProvider.textmode = 1

activationKeywords = PluginManager.keywords
pluginObjects = PluginManager.plugins

def waitForWake(wakeword):
	"Listening for wakeword."
	while not wakeword in InputProvider.inp().split(" "):
		OutputProvider.output("Activation required")
	OutputProvider.output("Yes, sir?")
	while True:
		getInput()
	
def continuousProcess():
	while 1:
		process(InputProvider.inp())

def process(humanInput):
	OutputProvider.output(PrimaryProcessProvider.process(humanInput))
	for i in range(len(activationKeywords)):
		if activationKeywords[i] in humanInput:
			return PackageManager.runPlugin(pluginObjects[i], humanInput[1:])
	
		
def getInput():
	process(InputProvider.inp())

while 1:
	waitForWake("hey")

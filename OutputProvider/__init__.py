outputProvider = "AlbusTTS" #Modify this line to change provider

textmode = False

try:
	outputProvider = __import__(outputProvider)
	outputProvider.init()
	textMode = False
except:
	print "Error loading output provider. Using textmode"
	textMode = True

def output(output):
	if output == "":
		print "Albus: {NO RESPONSE}"
	else:
		if textmode:
			print output
		else:
			output = outputProvider.main(output, "en-us")	
		return 1	

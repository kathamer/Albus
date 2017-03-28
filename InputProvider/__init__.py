inputProvider = "AlbusSR" #Modify this line to change provider

textmode = False

try:
	inputProvider = __import__(inputProvider)
except:
	print "Error loading input provider. Using textmode"
	textMode = True

def inp():
	if textmode:
		inp = raw_input("User: ")
	else:
		inp = inputProvider.main()	
	return inp

primaryProcessProvider = "AlbusCB" #Modify this line to change provider

try:
	primaryProcessProvider = __import__(primaryProcessProvider)
except:
	print "Error loading primary process provider."

def process(inp):
	print inp
	return primaryProcessProvider.main(inp)


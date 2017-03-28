#AlbusPM V2.1 for Albus2
#Dylan Hamer 2017

from os import walk, getcwd #Required to find all plugins

def findPlugins():
	pluginList = [] #List of plugins found
	ignoreList = [] #List of plugins ignored
	errorList = [] #List of plugins that were not imported due to errors	
	dirList = [] #List of directories found
	loadedPlugins = [] #Loaded plugins
	
	for (dirpath, dirnames, filenames) in walk(getcwd()): #Get all directories
		dirList.extend(dirnames)
		break

	for directory in dirList:
		if directory == "AlbusPM":
			ignoreList.append("AlbusPM")

		elif directory[1] == ".":			
			ignoreList.append(directory)			

		else:
			pluginList.append(directory)
	
	newList = []

	for item in pluginList:
		if item in newList:
			pass
		else:
			newList.append(item)
	pluginList = newList
 
	print "Found: "+str(len(pluginList))+" plugin(s):"
	for plugin in pluginList:
		try:
			newPlugin = __import__(plugin)
			pluginVersion = newPlugin.query("ver")
			pluginName = newPlugin.query("nme")
			pluginAuthor = newPlugin.query("ath")
			pluginDescription = newPlugin.query("dsc")
			pluginKeyword = newPlugin.query("key")
			loadedPlugins.append([plugin, newPlugin, pluginKeyword])
	
		except:
			errorList.append(plugin)
		print "    "+pluginName+" V"+str(pluginVersion)+" - "+pluginDescription
	print

	newList = []

	for item in errorList:
		if item in newList:
			pass
		else:
			newList.append(item)
	errorList = newList
 
	print "Errors were encountered while processing: "+str(len(errorList))+" plugin(s):"
	for plugin in errorList:
		print "    "+plugin
	print

	print "Ignored: "+str(len(ignoreList))+" plugin(s):"	
	for plugin in ignoreList:
		print "    "+plugin
	print
		
	return loadedPlugins	
				
def runPlugin(plugin, *args):
	print "Running plugin: "+pluginName
	try:
		output = plugin.main(args)
		return output
	except:
		print "Failed to run .main() function for plugin"

plugins = findPlugins()

keywords = []
for plugin in plugins:
	try:
		keywords.append(plugin[2])
	except:
		keywords.append(None)

names = []
for plugin in plugins:
	try:
		names.append(plugin[0])
	except:
		names.append(None)

objects = []
for plugin in plugins:
	try:
		objects.append(plugin[1])
	except:
		objects.append(None)




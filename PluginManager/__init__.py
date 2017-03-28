#PluginManager2 for Albus2

from os import walk, getcwd

dirList = [] #List of dirs in current directory

for cdir, dirs, files in walk('.'): #Get current directory, directories in current directory and files 
	for directory in dirs: #We need directories
		dirList.append(directory)

ignoreList = ["PluginManager", #Can't import self
              "InputProvider", #InputProvider is imported by Albus
              "OutputProvider", #OutputProvider is imported by Albus
              "PrimaryProcessProvider", #PrimaryProcessProvider is imported by Albus
              "Files", #Files directory is not a plugin
              "AIML"] #AIML directory is not a plugin

pluginList = [] #List of importable plugins
errorList = [] #List of plugins that cannot be imported
successfullyImported = [] #List of successfully imported plugins

for directory in dirList: 
	if directory in ignoreList: #Remove directories in ignore list
		pass
	elif directory[0] == "_": #Remove directories starting with '_'
		pass
	else:
		pluginList.append(directory) #Use directories not set to ignore

for plugin in pluginList:
	try:
		newPlugin = __import__(plugin) #Try to import the plugin
		pluginName = newPlugin.name #Get plugin name
		pluginAuthor = newPlugin.author #Get plugin author
		pluginDescription = newPlugin.description #Get plugin description
		pluginVersion = newPlugin.version #Get plugin version
		pluginKeyword = newPlugin.keyword #Get plugin activation keyword
		successfullyImported.append([pluginName, 
                                     pluginAuthor, 
                                     pluginDescription,
                                     pluginVersion,
                                     pluginKeyword,
                                     newPlugin])
	except:
		errorList.append(str(plugin)) #Add plugin to error list if importing fails

print str(len(ignoreList))+" plugin(s) were ignored:"
for each in ignoreList:
	print "		*"+each
print

print str(len(errorList))+" plugin(s) failed to import:"
for each in errorList:
	print "		*"+each
print

print str(len(successfullyImported))+" plugin(s) were successfully imported:"
for each in successfullyImported:
	print "		*"+str(each[0])+" "+str(each[3])+" - "+str(each[2])

keywords = [] #List of activation keywords
names = [] #List of names
plugins = [] #List of plugin objects

for each in successfullyImported: #Organize data for easy access
	names.append(each[0])	
	keywords.append(each[4])
	plugins.append([5])
	 


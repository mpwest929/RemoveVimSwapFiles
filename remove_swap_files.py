#!/usr/bin/python

import os;

# Retrieve current directory files
currentDirectoryFiles = os.listdir(".")

hiddenFiles = []
visibleFiles = []
for fileName in currentDirectoryFiles:
	if fileName[0:1] == '.' and (fileName != "." and fileName != ".."):
		hiddenFiles.append(fileName)
	else:
		 visibleFiles.append(fileName)

for hiddenFileName in hiddenFiles:
	stripOffBeginDot = hiddenFileName[1:]
	lastDotIndex = stripOffBeginDot.rfind('.')
	baseFileName = stripOffBeginDot[0:lastDotIndex]

	if baseFileName in visibleFiles:
		os.system("rm "+hiddenFileName);		




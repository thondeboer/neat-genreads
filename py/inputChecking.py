import os
import sys

def requiredField(s,errString):
	if s == None:
		print '\n'+errString+'\n'
		exit(1)

def checkFileOpen(fn,errString,required=False):
	if required:
		if fn == None:
			print '\n'+errString+'\n'
			exit(1)
		else:
			try:
				open(fn,'r')
			except:
				print '\n'+errString+'\n'
				exit(1)

def checkDir(dir,errString):
	if not os.path.isdir(dir):
		print '\n'+errString+'\n'
		exit(1)
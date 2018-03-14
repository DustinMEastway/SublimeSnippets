import sublime, sublime_plugin

import os
import re

def exportPath(path):
	return re.sub(
		r'^\s*(.+?)(?:\.ts)?\s*$',
		r"export * from './\1';",
		path)

def isBarrellable(path):
	# return True for typescript files and for directories with barrel files in them
	return ((os.path.isfile(path) and path.endswith('.ts'))
		or (os.path.isdir(path) and os.path.isfile(path + '/index.ts')))

def splitPath(path):
	# if path is already a dir, then return it
	if (os.path.isdir(path)): return path, None
	# split the path by the last '/' or '\' character found
	return re.split(r'[\\/](?!.*[\\/])', path)

# TODO EastwayD: make sure that this function works for Windows paths as well ('\' instead of '/')
class BarrelCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		filePath, fileName = splitPath(self.view.file_name())
		if (len(filePath) > 0):
			barrelFiles = [exportPath(file) for file in os.listdir(filePath) if file != fileName and isBarrellable(filePath + '/' + file)]
			self.view.insert(edit, 0, '\n'.join(barrelFiles) + '\n')

	def is_enabled(self):
		return (self.view.file_name() and len(self.view.file_name()) > 0)

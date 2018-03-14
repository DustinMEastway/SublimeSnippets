"""
Command features:
	sublime.set_clipboard('Hello World')
"""
import sublime, sublime_plugin

import os
import re

def castPath(path):
	return re.sub(
		r'\\s*(.*?)(?:\\.ts)\\s*',
		r'export * from \'./\1\';',
		path)

def isBarrellable(path):
	# TODO EastwayD: make this function work for Windows paths as well ('\' instead of '/')
	# can not barrel the base index.ts file
	if (re.search(r'\/index\.ts$', path)): return False
	# return True for typescript files and for directories with barrel files in them
	return ((os.path.isfile(path) and path.endswith('.ts'))
		or (os.path.isdir(path) and os.path.isfile(path + '/index.ts')))

def getDir(path):
	# if path is already a dir, then return it
	if (os.path.isdir(path)): return path
	return re.sub(
		r'^(.+)[\\/].*$',
		r'\1',
		path)

class HelloWorldCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if len(self.view.file_name()) > 0:
			# get the base directory to create a barrel from
			basePath = getDir(self.view.file_name())
			# get the export paths
			pathsToRexport = [castPath(path) for path in os.listdir(basePath) if isBarrellable(basePath + '/' + path)]
			# add the export statements to the top of the current file
			self.view.insert(edit, 0, '\n'.join(pathsToRexport))

	def is_enabled(self):
		return self.view.file_name() and len(self.view.file_name()) > 0

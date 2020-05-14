import os
from sys import argv as pars
del pars[0]


path = os.getcwd()

if len(pars) > 0:
	path = pars[0]


gap = 2


if not os.path.isdir(path):
	print(f"Couldn't find the specified path: '{path}'")

def buildString(times, char=" "):
	result = ""

	for x in range(times):
		result += char

	return result

def branch(lvl, path):
	nodes = os.listdir(path)

	for node in nodes:
		

		if os.path.isdir(os.path.join(path, node)):
			branch(lvl+1, os.path.join(path, node))

		else:
			print(buildString(lvl*gap) + node)
try:
	branch(0, path)
except PermissionError:
	print("Permission denied.")
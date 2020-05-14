import os, colorama, termcolor
from sys import argv as pars
del pars[0]
colorama.init()



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

	if len(nodes) == 0:
		print(buildString(lvl*gap)+"└"+termcolor.colored("Empty", "red"))

	for index, node in enumerate(nodes):
		

		if os.path.isdir(os.path.join(path, node)):
			print(f"{buildString(lvl*gap)}└{termcolor.colored(node, on_color='on_green')}")
			branch(lvl+1, os.path.join(path, node))

		else:
			if index+1 == len(nodes):
				print(buildString(lvl*gap)+"└"+node)
				continue

			print(buildString(lvl*gap)+ "├" + node)
try:
	branch(1, path)
except PermissionError:
	print("Permission denied.")
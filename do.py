import os
from sys import argv as pars
from json import loads, dumps, JSONDecodeError



def main():
	if not os.path.isfile("do.json"):
		raise FileNotFoundError("There is no 'do' file in the current working directory.")

	else:
		# Read the do file 
		try:
			content = loads(open("do.json", "r").read())

		except JSONDecodeError:
			raise JSONDecodeError("The do file seems to be corrupted.")

		# In case that the user didn't specify anything, the script will display all the available orders in the file.
		if len(pars) == 0:
			print("DISPLAYING ALL AVAILABLE ORDERS FROM THE DO FILE...")
			for index, order in enumerate(content):
				print(f"\t[{index}]: {order}")

			exit()

		else:
			order = pars[0]

			if not order in content:
				raise ValueError(f"There is no order such as '{order}' in the do file.")

			else:
				commands = content[order]

				if type(commands) == str:
					os.system(commands)
					exit()

				if type(commands) == list:
					for command in commands:
						os.system(command)

					exit()

				else:
					raise ValueError("There is a problem with how the commands related with the order are stored (they only can be stored in array or string).")




# Help message for the user
if "--help" in pars:
	print("""
This plugin executes orders referred to names from a do.json file in the current directory.
	--help
		Shows this help message

	\%nameoforder\%
		Executes the commands referred to that order inside the do.json file, in case it doesn't exist it will raise an error

	--check
		This parameter makes the plugin search for the do.json file in the folder, and tells the user if it exist or not.

""")
	exit()

if "--check" in pars:
	if os.path.isfile("do.json"):
		print("A do file have been found in the current working directory.")

	else:
		print("There is no do file in the current working directory.")

	exit()

if __file__ in pars:
	del pars[pars.index(__file__)]


main()


		




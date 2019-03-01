"""
Author: Henry Keena
Date: 8/6/2018
Release: 0.1
License: MIT
"""

#Imports subprocess
import subprocess as sub

#Imports sys
import sys

#Import yaml
import yaml

"""
Class: usable_manager(object)
Class To Create The Parameters For The Configured Manager 
"""
class wrapped_manager(object):
	"""
	Function: __init__(self, pac_man)
	Init Function For usable_manager Object
	"""
	def __init__(self, pac_man):
		self.pac_man = pac_man
	
	"""
	Function: pac_rem(self, package)
	Function To Remove A Package Using A Specified Package Manager
	"""
	def pac_rem(self, package):
		if self.pac_man == "apt":
			sub.call('sudo apt remove '+package,shell=True)
		elif self.pac_man == "apt-get":
			sub.call('sudo apt-get remove '+package,shell=True)
		elif self.pac_man == "pacman":
			sub.call('sudo pacman -R '+package,shell=True)
		elif self.pac_man == "yum":
			sub.call('sudo yum remove '+package,shell=True)
		elif self.pac_man == "dpkg":
			sub.call('sudo dpkg --remove '+package,shell=True)
		elif self.pac_man == "rpm":
			sub.call('sudo rpm -e '+package,shell=True)

	"""
	Function: pac_inst(self, package)
	Function To Install A Package Using A Specified Package Manager
	"""
	def pac_inst(self, package):
		if self.pac_man == "apt":
			sub.call('sudo apt install '+package,shell=True)
		elif self.pac_man == "apt-get":
			sub.call('sudo apt-get install '+package,shell=True)
		elif self.pac_man == "pacman":
			sub.call('sudo pacman -S '+package,shell=True)
		elif self.pac_man == "yum":
			sub.call('sudo yum install '+package,shell=True)
		elif self.pac_man == "dpkg":
			sub.call('sudo dpkg --install '+package,shell=True)
		elif self.pac_man == "rpm":
			sub.call('sudo rpm -ivh '+package,shell=True)

	"""
	Function: sys_upd(self)
	Function To Update System Packages
	"""
	def sys_upd(self):
		if self.pac_man == "apt":
			sub.call('sudo apt update && sudo apt upgrade && sudo apt autoremove',shell=True)
		elif self.pac_man == "apt-get":
			sub.call('sudo apt-get update && sudo apt-get upgrade && sudo apt-get autoremove',shell=True)
		elif self.pac_man == "pacman":
			sub.call('sudo pacman -Syu',shell=True)
		elif self.pac_man == "yum":
			sub.call('sudo yum update',shell=True)
		elif self.pac_man == "dpkg":
			print("Total System Update Unsupported By Package Manager")
		elif self.pac_man == "rpm":
			print("Total System Update Unsupported By Package Manager")

"""
Function: read_config(config_file)
Function To Read And Use YAML Config File
"""
def read_config(config_file):
	with open(config_file, 'r') as ymlfile:
    		cfg = yaml.load(ymlfile)
	pack = cfg['selected_package_manager']
	return pack

"""
Function: change_config(config_file, pac_man)
Function To Alter Config File To Use Prefered Packager Manager
"""
def change_config(config_file, pac_man):
	with open(config_file) as ymlfile:
		confil = yaml.load(ymlfile)
		if confil['selected_package_manager'] == pac_man:
			pass
		else:
			confil['selected_package_manager'] = pac_man
	with open(config_file, 'w') as ymlfile:
		yaml.dump(confil, ymlfile, default_flow_style=False)

"""
Function: read_me()
Function That Prints README For User
"""
def read_me():
	sub.call('clear',shell=True)
	sub.call('cat README.md',shell=True)
	try:
    		input("\n\n\nPRESS ENTER TO CONTINUE")
	except SyntaxError:
    		pass
	sub.call('clear',shell=True)

"""
Function: read_lic()
Function That Prints License Information
"""
def read_lic():
	sub.call('clear',shell=True)
	sub.call('cat LICENSE',shell=True)
	try:
    		input("\n\n\nPRESS ENTER TO CONTINUE")
	except SyntaxError:
    		pass
	sub.call('clear',shell=True)

"""
Function: display_help()
Function To Display All Phypac Options
"""
def display_help():
	print("Tuxi 0.1")
	print("Usage: tuxi [options]\n")
	print("Options:")
	print("\t-i <target>: Install a package with configured package manager")
	print("\t-r <target>: Remove a package with configured package manager")
	print("\t-su: Complete system package update with configured package manager")
	print("\t-c <target>: Rewrites config file to use a specified package manager")
	print("\t-rl: Displays LICENSE")
	print("\t-rm: Displays README")
	print("\t-h: Displays this help message")
	print("")

"""
Function: main()
Main Function 
"""
def main():
	try:
		current_pac = read_config("config.yaml")
		wrap = wrapped_manager(current_pac)
		args = sys.argv
		if args[1] == "-h":
			display_help()
		elif args[1] == "-i":
			if current_pac == "apt":
				wrap.pac_inst(args[2])
			elif current_pac == "rpm":
				wrap.pac_inst(args[2])
			elif current_pac == "apt-get":
				wrap.pac_inst(args[2])
			elif current_pac == "pacman":
				wrap.pac_inst(args[2])
			elif current_pac == "yum":
				wrap.pac_inst(args[2])
			elif current_pac == "dpkg":
				wrap.pac_inst(args[2])
			else:
				print("Invalid Package Manager")

		elif args[1] == "-r":
			if current_pac == "apt":
				wrap.pac_rem(args[2])
			elif current_pac == "rpm":
				wrap.pac_rem(args[2])
			elif current_pac == "apt-get":
				wrap.pac_rem(args[2])
			elif current_pac == "pacman":
				wrap.pac_rem(args[2])
			elif current_pac == "yum":
				wrap.pac_rem(args[2])
			elif current_pac == "dpkg":
				wrap.pac_rem(args[2])
			else:
				print("Invalid Package Manager")
		elif args[1] == "-c":
			if args[2] == "apt":
				change_config("config.yaml", args[2])
			elif args[2] == "rpm":
				change_config("config.yaml", args[2])
			elif args[2] == "apt-get":
				change_config("config.yaml", args[2])
			elif args[2] == "pacman":
				change_config("config.yaml", args[2])
			elif args[2] == "yum":
				change_config("config.yaml", args[2])
			elif args[2] == "dpkg":
				change_config("config.yaml", args[2])
			else:
				print("Invalid Package Manager")
		elif args[1] == "-su":
			if current_pac == "apt":
				wrap.sys_upd()
			elif current_pac == "rpm":
				wrap.sys_upd()
			elif current_pac == "apt-get":
				wrap.sys_upd()
			elif current_pac == "pacman":
				wrap.sys_upd()
			elif current_pac == "yum":
				wrap.sys_upd()
			elif current_pac == "dpkg":
				wrap.sys_upd()
		elif args[1] == "-rl":
			read_lic()
		elif args[1] == "-rm":
			read_me()
		else:
			display_help()
	except IndexError:
		display_help()

#Calls Main
if __name__ == "__main__":
	main()

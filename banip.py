#!/usr/bin/env python3
# _____  ___  ______ _____  __   _______ _   _ 
#/  ___|/ _ \ |  ___|  ___| \ \ / /  _  | | | |
#\ `--./ /_\ \| |_  | |__    \ V /| | | | | | |
# `--. \  _  ||  _| |  __|    \ / | | | | | | |
#/\__/ / | | || |   | |___    | | \ \_/ / |_| |
#\____/\_| |_/\_|   \____/    \_/  \___/ \___/  
#
#			Prevention attack DDoS

import sys
import getopt
import subprocess

_name    = "SafeYOU BANIP"
_version = "1.0"

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "ha:d:lv", ["help", "add=", "delete=", "list", "version"])
		
		if len(opts) == 0:
			if len(args) > 0:
				opts = []
				for arg in args:
					opts.append(("-a", arg))
			else:
				opts = [("-h","")]
		
		for opt, arg in opts:
			if opt in ("-h", "--help"):
				aide()
			elif opt in ("-a", "--add"):
				subprocess.call(["iptables", "-A", "INPUT", "-s", arg, "-j", "DROP"])
			elif opt in ("-d", "--delete"):
				subprocess.call(["iptables", "-D", "INPUT", "-s", arg, "-j", "DROP"])
			elif opt in ("-l", "--list"):
				subprocess.call(["iptables", "-L", "-n"])
	except getopt.GetoptError as err:
		print("IPban error: " + str(err))
		sys.exit(2)
	except:
		print("IPban error (unknown).")
		sys.exit(2)

def version():
	global _name, _version
	return _name + " " + _version

def aide():
	print(version())
	print("Utilisation : ipban [ips|-h|-a ip|-d ip|-l]\n")
	print("-h       Affiche ce message.")
	print("-a       Ajoute une adresse IP à la liste de blocage. Exemple: 1.2.3.4")
	print("-d       Supprime une adresse IP de la liste de blocage. Exemple: 1.2.3.4")
	print("-l       Les règles iptables appliquées.")

if __name__ == "__main__":
	main(sys.argv[1:])

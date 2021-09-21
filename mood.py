# #!/usr/bin/env python

import os
import argparse

# Enter your moods and commands
browser = "firefox "


google = browser + "www.google.com/"

# Moods
def hello(args):
	print('Use -h for help, {0}!'.format(args.name))

def mood(args):
	if args.mood == 'google':
		os.system(google)
	else:
		os.system(browser + args.mood)

def add(args):
	os.system("nano mood.py")

def delete(args):
	os.system("nano mood.py")

def usage():
	print("ggs")

# Initalize parser
parser = argparse.ArgumentParser()
subparsers= parser.add_subparsers()

mood_parser = subparsers.add_parser('mood')
mood_parser.add_argument('mood')
mood_parser.set_defaults(func=mood)


if __name__ == '__main__':
	args = parser.parse_args()
	try:
		args.func(args)
	except AttributeError:
		usage()
		parser.exit()

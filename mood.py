""" Mood

Usage:
  mood.py -m <mood>
  mood.py -a <add mood>
  mood.py -d <remove mood>
"""
import os
import argparse

# Enter your moods and commands
#firefox = "firefox"
#codeforces = 
#spotify = 
#idea =
google = "firefox www.google.com"

# Methods
def hello(args):
	print('Use -h for help, {0}!'.format(args.name))

def mood(args):
#	if {1}  == 'google':
		print(google)
		os.system(google)

def add(args):
	os.system("nano mood.py")

def delete(args):
	os.system("nano mood.py")

# Initalize parser
parser = argparse.ArgumentParser()
subparsers= parser.add_subparsers()

hello_parser = subparsers.add_parser('hello')
hello_parser.add_argument('name')
hello_parser.set_defaults(func=hello)

mood_parser = subparsers.add_parser('mood')
mood_parser.add_argument('mood')
mood_parser.set_defaults(func=mood)


if __name__ == '__main__':
	args = parser.parse_args()
	args.func(args)

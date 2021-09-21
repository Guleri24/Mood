import os
import argparse

# Browser (make sure to add space after browser command)
browser = "firefox "

# Websites
eclipse_foundation = browser + "https://blogs.eclipse.org/"
easter_egg = browser + "https://youtu.be/DGa6MAibjzA"
instagram = browser + "https://www.instagram.com/"
java_magazine = browser + "https://blogs.oracle.com/javamagazine/"
linkedin = browser + "https://www.linkedin.com/feed/"
phoronix = browser + "https://www.phoronix.com/scan.php?page=home"

# Applications
spotify = ""
intellij_idea = ""
eclipse = ""
signal = ""
discord = ""

def add(args):
	os.system("nano mood.py")

def delete(args):
	os.system("nano mood.py")

# Make sure to add new moods
def updates():
	print("Available moods:")
	print("updates, social, coding \n")
	print("Example: python mood.py enable updates")

def about():
	print("""

                        _
  /\/\   ___   ___   __| |
 /    \ / _ \ / _ \ / _` |
/ /\/\ \ (_) | (_) | (_| |
\/    \/\___/ \___/ \__,_|

Minimalistic user mood generator and executor
    """)

# Add you moods here
def mood(args):
    if args.mood == 'updates':
        os.system(java_magazine)
        os.system(phoronix)
        os.system(eclipse_foundation)

    elif args.mood == 'social':
	    os.system(instagram)
	    os.system(linkedin)

    elif args.mood == 'coding':
	    print("coding..")

    else:
	    os.system(easter_egg)




# Initialize parser
parser = argparse.ArgumentParser()
subparsers= parser.add_subparsers()

mood_parser = subparsers.add_parser('enable', help="enter desired mood")
mood_parser.add_argument('mood')
mood_parser.set_defaults(func=mood)

add_mood = subparsers.add_parser('add', help="add new mood")
add_mood.set_defaults(func=add)

delete_mood = subparsers.add_parser('delete', help="delete mood")
delete_mood.set_defaults(func=delete)

if __name__ == '__main__':
	args = parser.parse_args()
	try:
		args.func(args)
	except AttributeError:
		about()
		updates()
		print("no argument passed, use -h for help")
		parser.exit()

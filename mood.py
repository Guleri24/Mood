import os
import argparse

# make sure to add space after browser and webistes command)

# Browser
browser = "firefox "

# Websites
eclipse_foundation = "https://blogs.eclipse.org/ "
easter_egg = "https://youtu.be/DGa6MAibjzA "
instagram = "https://www.instagram.com/ "
java_magazine = "https://blogs.oracle.com/javamagazine/ "
linkedin = "https://www.linkedin.com/feed/ "
phoronix = "https://www.phoronix.com/scan.php?page=home "

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
        updates = browser + java_magazine + phoronix + eclipse_foundation
        os.system(updates)

    elif args.mood == 'social':
        social = browser + instagram + linkedin
        os.system(social)

    elif args.mood == 'coding':
        print("coding..")

    else:
        os.system(easter_egg)


# Initialize parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

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

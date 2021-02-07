import sys

def debug(message):
    if sys.stdout.isatty():
        print("[debug]: " + message)

def updater(message):
    if sys.stdout.isatty():
        print(u"\u001b[35m [updater]: \u001b[35;1m" + message + "\u001b[0m")
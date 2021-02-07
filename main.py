import random,os,argparse,sys,math,json,requests
import logger,urllib.request, configparser
from saveutils import *
from time import sleep

cfgParser = configparser.ConfigParser()
cfgParser.read("settings.ini")
check_for_updates = cfgParser.getboolean("settings","check_for_updates",)

reqText = requests.get("https://github.com/C-ffeeStain/Kali-Sim/raw/main/version.json").text
webJson = json.loads(reqText)
with open("version.json") as f:
    vJson = json.load(f)

webVersion = webJson["version"]
webFeatures = webJson["features"]
version = vJson["version"]
features = vJson["features"]

if webVersion == version:
    logger.updater("You have the latest updates.")
    logger.updater("To disable these messages, change 'check_for_updates' to false in settings.ini.")
else:
    logger.updater("You have an outdated version. Please download the latest release.").lower()
    logger.updater("To disable these messages, change 'check_for_updates' to false in settings.ini.")
debug = False
parser = argparse.ArgumentParser(description="Simple command line game to sacrifice to Spelunky 2's Kali.")
parser.add_argument("--debug",help="Use this to tell this program to use debug mode.",action="store_true")
args = parser.parse_args()

debug = args.debug
check_save(debug)
save_number = get_save_num()

items = ("Climbing Gloves", "Pitcher's Mitt", "Spring Shoes", "Spike Shoes", "Spectacles", "Compass", "Cape", "Paste")
favor = open_save(save_number)

got_present = False
got_kapala = False
while True:
    dead = False
    sacrifice = ""
    
    print("For the dead version of the item, add 'd' after it.\n"
    + "So a dead damsel would be '1d'.\n\n"
    + "1: Damsel \n"
    + "2: Spelunker, Hired Hand, Shopkeeper, Other NPCs\n"
    + "3: Witch Doctor, Crocman, Sorceress, Necromancer\n"
    + "4: Caveman, Cave Mole, Tiki Man, Octopy, \n"
    + "\tYeti, Olmite, Cave Turkey, Rock Dog, \n"
    + "\tAxolotl, Qilin\n"
    + "5: (can't be dead) Horned Lizard, Mantrap, Vampire, Vlad, \n"
    + "\tScorpion\n"
    + "6: Present\n"
    + "7: Rock\n"
    + "8: Golden Idol\n"
    + "9: Ushabti\n"
    + "10: Quit Sim\n\n")
    print("Your favor with Kali: " + str(favor))
    sacrifice = input("What would you like to sacrifice? ")
    print(" ")
    if sacrifice[-1].lower() == "d" and sacrifice != 5:
        sacrifice = sacrifice.removesuffix("d")
        dead = True
    elif sacrifice == 5 and sacrifice[-1].lower() == "d":
        sacrifice = sacrifice.removeprefix("d")
    if sacrifice == "10":
        save_game = input("Would you like to save before you go? (Y/n) ")
        if save_game.lower() == 'y':
            save(favor, save_number, True)
        print("\nQuitting sim...")
        sys.exit(0)
    elif sacrifice == "1":
        if not dead:
            favor += 8
        else:
            favor += 4
    elif sacrifice == "2":
        if not dead:
            favor += 6
        else:
            favor += 3
    elif sacrifice == "3":
        if not dead:
            favor += 4
        else:
            favor += 2
    elif sacrifice == "4":
        if not dead:
            favor += 2
        else:
            favor += 1
    elif sacrifice == "5":
        if not dead:
            favor += 2
        else:
            print("---------------------------------------------------------")
            print("None of those can be dead. They don't have corpses.")
            print("---------------------------------------------------------\n")
    elif sacrifice == "6":
        print("---------------------------------------------------------")
        print("Kali enjoys a good mystery!")
        print("You get an eggplant.")
        print("---------------------------------------------------------\n")
    elif sacrifice == "7":
        if favor >= 16:
            print("---------------------------------------------------------")
            print("Kali admires your warrior spirit. She fashions a weapon for you!\n"
            + "Your rock turns into an arrow.")
            print("---------------------------------------------------------\n")
        else:
            print("---------------------------------------------------------")
            print("Nothing happens. Maybe you need more favor.")
            print("---------------------------------------------------------\n")
    elif sacrifice == "8":
        print("---------------------------------------------------------")
        print("A golden monkey hops off the altar.")
        print("---------------------------------------------------------\n")
    elif sacrifice == "9":
        print("---------------------------------------------------------")
        print("So you desire a companion? Here you go!")
        print("---------------------------------------------------------\n")
        if favor <= 7 and favor >= 0:
            print("---------------------------------------------------------")
            print("A caveman spawns on the altar.")
            print("---------------------------------------------------------\n")
        elif favor <= 15 and favor >= 8:
            print("---------------------------------------------------------")
            print("A cave turkey spawns on the altar.")
            print("---------------------------------------------------------\n")
        elif favor <= 31 and favor >= 16:
            print("---------------------------------------------------------")
            print("A hired hand spawns on the altar.")
            print("---------------------------------------------------------\n")
        elif favor >= 32:
            print("---------------------------------------------------------")
            print("A hired hand with a shotgun in his hands spawns on the altar.")
            print("---------------------------------------------------------\n")
        favor = math.ceil(favor / 2)
    if int(sacrifice) <= 5:
        if sacrifice == 5 and dead:
            sacrifice = 0
        if favor >= 1 and favor <= 7:
            print("---------------------------------------------------------")
            print("Kali accepts your sacrifice. She seems pleased with you.\n")
            print("---------------------------------------------------------\n")
        elif favor > 8 and favor <= 15 and got_present:
            print("---------------------------------------------------------")
            print("Kali accepts your sacrifice. She seems happy with you.")
            print("---------------------------------------------------------\n")
        elif favor > 16 and got_kapala:
            print("Kali accepts your sacrifice. She seems ecstatic with you.\n")
            print("You pick up the royal jelly.")
        elif favor >= 8 and not got_present:
            print("---------------------------------------------------------")
            print("Kali accepts your sacrifice. She bestows a gift upon you!")
            print("You pick up the " + items[random.randint(0, 8)] + ".")
            print("---------------------------------------------------------\n")
            got_present = True
        elif favor >= 16 and not got_kapala:
            print("---------------------------------------------------------")
            print("Kali accepts your sacrifice. She bestows a gift upon you!")
            print("You pick up the Kapala.\n")
            print("---------------------------------------------------------\n")
            got_kapala = True
    sleep(1.75)
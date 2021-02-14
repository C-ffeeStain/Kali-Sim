import os
from logger import debug as dbg
import configparser

def get_save_num() -> int:
    save_num = int(input("Which save number would you like to use? "))
    return save_num

def save(favor : int, save_number : int, show_msg : bool):
    cfg = configparser.ConfigParser()
    cfg.read("saves.ini")
    if show_msg:
        print("Saving!")
    cfg["save-" + save_number]["favor"] = favor
    
    with open("saves.ini", "w") as f:
        cfg.write(f)

def open_save(save_number):
    cfg = configparser.ConfigParser()
    cfg.read("saves.ini")
    return int(cfg["save-" + save_number]["favor"])

def check_save(debug):
    cfg = configparser.ConfigParser()

    if os.path.exists("saves.ini"):
        if debug:
            dbg("Saves file exists!")
    else:
        if debug:
            dbg("Saves file does not exist, creating...")
        with open("saves.ini", "w") as f:
            f.write("# This is Kali Sim's save file!\n# Make sure if you add a save, change 'num_saves' in the [general] section\n")
    
    cfg.read("saves.ini")

    if "general" in cfg:
        if debug:
            dbg("General section exists.")
    else:
        if debug:
            dbg("No general section, creating!")
        cfg["general"] = {}
        cfg["general"]["num_saves"] = len(cfg.sections()) - 1

    if int(cfg["general"]["num_saves"]) > len(cfg.sections()) - 1 or int(cfg["general"]["num_saves"]) < 0:
        if debug:
            dbg("Number of saves error, fixing.")
        cfg["general"]["num_saves"] = len(cfg.sections()) - 1
    else:
        if debug:
            dbg("No save number error.")
    
    if "save-1" in cfg.sections():
        if debug:
            dbg("A save section exists!")
    else:
        if debug:
            dbg("A save section does not exist, creating!")
        save(0, 1, False)
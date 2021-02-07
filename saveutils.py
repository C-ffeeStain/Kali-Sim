import os
from logger import debug as dbg

def get_save_num() -> int:
    save_num = int(input("Which save number would you like to use? "))
    return save_num

def save(favor : int, save_number : int, show_msg : bool):
    """Saves the game by writing to the currently used save.
    favor: An integer to represent the kali favor to save.
    save_number: The save number to save to. Can be from 1 to 3.
    show_msg: Whether to show the message "Saving!" or not."""
    if show_msg:
        print("Saving!")
    with open("saves/save" + str(save_number) + ".txt", "w") as f:
        f.write(str(favor))

def open_save(save_number : int):
    with open("saves/save" + str(save_number) + ".txt", "r") as f:
        return int(f.readline())

def check_save(debug):
    if os.path.exists("saves"):
        if debug:
            dbg("Saves directory exists!")
    else:
        if debug:
            dbg("Saves directory does not exist, creating...")
        os.mkdir("saves")

    if os.path.exists("saves/save1.txt"):
        if debug:
            dbg("Save one exists!")
    else:
        if debug:
            dbg("Save one does not exist, creating...")
        save(0, 1, False)

    if os.path.exists("saves/save2.txt"):
        if debug:
            dbg("Save two exists!")
    else:
        if debug:
            dbg("Save two does not exist, creating...")
        save(0, 2, False)

    if os.path.exists("saves/save3.txt"):
        if debug:
            dbg("Save three exists!\n")
    else:
        if debug:
            dbg("Save three does not exist, creating...\n")
        save(0, 3, False)
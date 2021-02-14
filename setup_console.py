import os
import urllib
import logger
import urllib.request

install_dir = f"{os.getenv('APPDATA')}\\Kali Sim - CE\\"
base_url = "https://github.com/C-ffeeStain/Kali-Sim/raw/main/"
logger.updater("Installing...")

if not os.path.exists(install_dir):
    os.mkdir(install_dir)

urllib.request.urlretrieve(base_url + "dist/main.exe", install_dir + "KaliSim_ConsoleEdition.exe")

# Create and write to the config file
with open(install_dir + "settings.ini", "w") as cfg:
    cfg.writelines(["[settings]\n", "check_for_updates = true"])

logger.updater(f"Finished installing to \"{install_dir}!\"")
logger.updater("You can now delete this file!")

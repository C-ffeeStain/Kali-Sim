import os
import logger
import shutil

install_dir = f"{os.getenv('APPDATA')}\\Kali Sim - CE\\"
base_url = "https://github.com/C-ffeeStain/Kali-Sim/raw/main/"
requirements = ["pyinstaller", "requests"]
logger.updater("Installing...")
for requirement in requirements:
    os.system(f"py -m pip install --upgrade {requirement}")

import requests

if not os.path.exists(install_dir):
    os.mkdir(install_dir)
if not os.path.exists(".install"):
    os.mkdir(".install")
    os.system("attrib +H .install")

os.chdir(".install\\")

request = requests.get(base_url + "main.py")
if request.status_code == requests.codes.ok:
    with open("main.py", "w") as f:
        f.write(request.text)

request = requests.get(base_url + "icon.ico", stream = True)
if request.status_code == requests.codes.ok:
    request.raw.decode_content = True
    with open("icon.ico", "wb") as icon:
        shutil.copyfileobj(request.raw, icon)

os.system(f"pyinstaller main.py --onefile --icon icon.ico")

exe_data = []
with open("dist\\main.exe", "rb") as f:
    exe_data = f.readlines()


with open(install_dir + "KaliSim_ConsoleEditon.exe", "wb") as f:
    f.writelines(exe_data)


try:
    os.chdir("..\\")
    shutil.rmtree(".install")
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))

# Create and write to the config file
cfg = open(install_dir + "settings.ini", "w")
cfg.writelines(["[settings]\n", "check_for_updates = true"])
cfg.close()

logger.updater(f"Finished installing to \"{install_dir}!\"")
logger.updater("You can now delete this file!")

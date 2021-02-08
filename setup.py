import os
import logger
import requests
import shutil

install_dir = f"{os.getenv('APPDATA')}\\Kali Sim - CE\\"
url = "https://github.com/C-ffeeStain/Kali-Sim/raw/main/main.py"

logger.updater("Installing...")
os.system("pip install -r requirements.txt")
request = requests.get(url)
if request.status_code == requests.codes.ok:
    with open("main.py", "w") as f:
        f.write(request.text)
os.system("pyinstaller main.py")

exe_data = []
with open("dist\\main.exe", "rb") as f:
    exe_data = f.readlines()
if not os.path.exists(install_dir):
    os.mkdir(install_dir)

new_pos = open(install_dir + "KaliSim_ConsoleEditon.exe", "wb")
new_pos.writelines(exe_data)
new_pos.close()

try:
    shutil.rmtree("build")
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

try:
    shutil.rmtree("dist")
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

# Create and write to the config file 
cfg = open(install_dir + "settings.ini", "w")
cfg.writelines(["[settings]", "check_for_updates = true"])
cfg.close()

logger.updater(f"Finished installing to \"{install_dir}!\"")

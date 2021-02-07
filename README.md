# Kali Sim
 A command-line form of Kali from Spelunky 2.

# Installation
Go to the [releases page](https://github.com/C-ffeeStain/Kali-Sim/releases/latest) and just click *kali-console.zip* to download it.


# Building
Get Git, Python 3.8 (or later), and run the following code to build this project:

```bash
git clone https://github.com/C-ffeeStain/Kali-Sim/
cd Kali-Sim
python -m venv venv
"venv/scripts/activate.bat"
python -m pip install requests
python -m pip install pyinstaller
pyinstaller --onefile main.py
pyinstaller --onefile setup.py
```
The two exe's will be in the 'dist' folder in the Kali-Sim folder.

# Kali Sim
 A command-line form of Kali from Spelunky 2.

# Installation
Install Python 3.9, go to the [releases page](https://github.com/C-ffeeStain/Kali-Sim/releases/latest), and just click *setup.exe* to download it.


# Building
Get Git, Python 3.9, and run the following commands to build this project:

```bash
git clone https://github.com/C-ffeeStain/Kali-Sim/
cd Kali-Sim
python -m venv venv
"venv/scripts/activate.bat"
pip install -r requirements.txt
pyinstaller --onefile main.py
pyinstaller --onefile setup.py
```
The two exe's will be in the 'dist' folder in the Kali-Sim folder.

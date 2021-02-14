import os
import logger
import sys
import urllib.request

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

def msg_box(win, title, text, icon) -> QMessageBox:
    msg_box = QMessageBox(win)
    msg_box.setWindowTitle(title)
    msg_box.setText(text)
    msg_box.adjustSize()
    msg_box.setIcon(icon)
    return msg_box


app = QApplication(sys.argv)


class App(QMainWindow):
    install_dir = f"{os.getenv('APPDATA')}\\Kali Sim - CE\\"
    base_url = "https://github.com/C-ffeeStain/Kali-Sim/raw/main/"

    @pyqtSlot()
    def get_folder(self):
        selected_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', self.install_dir)
        if selected_folder:
            self.install_dir = selected_folder
            self.install_dir_lineedit.setText(self.install_dir)

    def __init__(self) -> None:
        super().__init__()

        self.init_ui()

    @pyqtSlot()
    def cancel_clicked(self):
        sys.exit(0)

    @pyqtSlot()
    def install_clicked(self):
        self.installing = msg_box(
            self,
            "Starting",
            "Installing 'Kali Sim - Console Edition'!",
            QMessageBox.Information
        )
        self.installing.exec_()

        if not self.install_dir_input.text().isspace():
           self.install_dir = self.install_dir_input.text()

        urllib.request.urlretrieve(
            self.base_url + "dist/main.exe", self.install_dir + "KaliSim_ConsoleEdition.exe")
        if self.check_for_updates.isChecked():
            # Update checking
            with open(os.path.join(self.install_dir, "settings.ini"), "w") as cfg:
                cfg.writelines(["[settings]\n", "check_for_updates = true"])
        else:
            # No update checking
            with open(os.path.join(self.install_dir, "settings.ini"), "w") as cfg:
                cfg.writelines(["[settings]\n", "check_for_updates = false"])

        if self.shortcut.isChecked():
            with open("shortcut.ps1", "w") as f:
                f.write(f"""$linkPath = Join-Path ([Environment]::GetFolderPath("Desktop")) "Kali Sim - Console Edition.lnk"
$targetPath = Join-Path ([Environment]::GetFolderPath("ApplicationData")) "{self.install_dir}\\KaliSim_ConsoleEdition.exe"
$link = (New-Object -ComObject WScript.Shell).CreateShortcut( $linkpath )
$link.TargetPath = $targetPath
$link.Save()""")
            os.system("Powershell.exe -executionpolicy remotesigned -File  shortcut.ps1")
            os.remove("shortcut.ps1")
        self.installed = msg_box(
            self, "Success!", "Successfully installed! You can now delete this file.", QMessageBox.Information)
        self.installed.exec_()
    def init_ui(self):
        if not os.path.exists(self.install_dir):
            os.mkdir(self.install_dir)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(400, 400, 350, 175)
        self.setFixedSize(350, 175)
        self.setWindowTitle("Setup for Kali Sim - CE")
        self.setFont(QFont("Consolas", 10))

        self.title = QtWidgets.QLabel(self)
        self.title.setText("Setup for Kali Sim - CE")
        self.title.setFont(QFont("Consolas", 12))
        self.title.adjustSize()
        self.title.move(45, 10)

        self.shortcut = QtWidgets.QCheckBox(self)
        self.shortcut.move(20, 30)
        self.shortcut.setChecked(True)
        self.shortcut_text = QtWidgets.QLabel(self)
        self.shortcut_text.setText("Create desktop shortcut")
        self.shortcut_text.adjustSize()
        self.shortcut_text.move(40, 36)

        self.check_for_updates = QtWidgets.QCheckBox(self)
        self.check_for_updates.move(20, 50)
        self.check_for_updates.setChecked(True)

        self.check_for_updates_text = QtWidgets.QLabel(self)
        self.check_for_updates_text.setText("Check for updates on app start")
        self.check_for_updates_text.adjustSize()
        self.check_for_updates_text.move(40, 56)

        self.install = QtWidgets.QPushButton(self)
        self.install.setText("Install")
        self.install.adjustSize()
        self.install.setFixedSize(self.install.size())
        self.install.move(70, 140)
        self.install.clicked.connect(self.install_clicked)
        
        self.install_dir_text = QtWidgets.QLabel(self)
        self.install_dir_text.setText("Install Folder:")
        self.install_dir_text.adjustSize()
        self.install_dir_text.move(20, 76)

        self.install_dir_lineedit = QLineEdit(self)
        self.install_dir_lineedit.setReadOnly(True)
        self.install_dir_lineedit.setText(self.install_dir)
        self.install_dir_lineedit.setToolTip(self.install_dir)
        self.install_dir_lineedit.adjustSize()
        self.install_dir_lineedit.setFixedWidth(200)
        self.install_dir_lineedit.move(130, 75)

        self.choose_folder = QtWidgets.QPushButton(self)
        self.choose_folder.setText("Choose")
        self.choose_folder.adjustSize()
        self.choose_folder.move(195, 105)
        self.choose_folder.clicked.connect(self.get_folder)

        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setText("Cancel")
        self.cancel.adjustSize()
        self.cancel.setFixedSize(self.cancel.size())
        self.cancel.move(150, 140)
        self.cancel.clicked.connect(self.cancel_clicked)

        self.show()


win = App()
sys.exit(app.exec_())

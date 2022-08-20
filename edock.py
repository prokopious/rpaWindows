from pywinauto.application import Application
import datetime
import os
import time
import sys




def automate_notepad():
    app = Application().start("notepad.exe")
    list = app.windows()
    print(list)

   


if __name__ == "__main__":
    automate_notepad()
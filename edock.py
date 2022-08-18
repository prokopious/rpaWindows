from RPA.Windows import Windows
import datetime
import os
import sys

windows = Windows()


def automate_notepad():
    windows.windows_run("C:/Users/Public/Desktop/edock.exe")
   


if __name__ == "__main__":
    automate_notepad()
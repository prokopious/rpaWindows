import os
import sys
import time
import subprocess
import ctypes
import uiautomation as auto
# Open Notepad
subprocess.Popen('notepad')
# Identify Notepad Class
window = auto.WindowControl(searchDepth = 1, ClassName = 'Notepad', RegexName = '.* - Notepad')
#Find the format menuitem
window.MenuItemControl(Name = 'File').DoubleClick()
time.sleep(2)
#Click the Font within format menuitem




edit = auto.EditControl(searchFromControl = window)  #or edit = window.EditControl()
edit.Click(waitTime = 0)
#Typing rich text on notepad
edit.SendKeys('Hello from UI Automation!!')
edit.SendKeys('{Ctrl}{A}', 0.2, 0)
window.MenuItemControl(Name = 'Format').Click()
window.MenuItemControl(Name = 'Font...').Click()
windowFont = window.WindowControl(Name = 'Font')
windowFont.ComboBoxControl(AutomationId = '1136').Select('Segoe UI Symbol')
windowFont.ComboBoxControl(AutomationId = '1138').Select('18')
windowFont.ButtonControl(Name = 'OK').Click()
edit.SendKeys('{Ctrl}{End}{Enter}Lets test with keyboard{! 4}{ENTER}', 0.2, 0)
edit.SendKeys('{Enter 2}0123456789{Enter}', waitTime = 0)
edit.SendKeys('{Enter}ABCDEFGHIJKLMNOPQRSTUVWXYZ{Enter}', waitTime = 0)
edit.SendKeys('{Enter}abcdefghijklmnopqrstuvwxyz{Enter}', waitTime = 0)
edit.SendKeys('{Enter}`~!@#$%^&*()-_=+{Enter}', waitTime = 0)
edit.SendKeys('{Enter}[]{{}{}}\\|;:\'\",<.>/?{Enter}{Ctrl}a')
# Click close button before exit
window.ButtonControl(searchDepth=2, Name='Close').Click()
# Name the notepad
window.ButtonControl(Name="Save").Click()
auto.SendKeys('UIA')
#Exit
window.ButtonControl(Name="Save").Click()
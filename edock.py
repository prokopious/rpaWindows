from pywinauto.application import Application
import datetime
import os
import time
import sys




app = Application().start("C:/Users/huyetto/Desktop/eDockFiles/eDock.exe")
dlg = app.top_window()
dlg['Continue'].click_input()
app['frmLogin'].child_window(title="Log In", auto_id="btnLogIn", control_type="System.Windows.Forms.Button").click_input()

dialogs = app.windows()
print(dialogs)

   


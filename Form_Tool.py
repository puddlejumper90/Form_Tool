'''
The purpose of this application is to allow the user to create their own forms that can be used to easily store data in csv files.
'''

#Import the needed libraries
import tkinter
import numpy as np
import pandas as pd
import pandasql as psql
from tkinter import *

#Defined functions 1
def OBL(): #Prints one blank line
    print("")
    
#Main menu
m_screen = Tk()
m_screen.title("Form Tool Main Menu")
ms_description = Label(m_screen, text="The purpose of this application is to allow the user to create their own forms that can be used to easily store data in csv files.")
ms_description.pack()

#Main menu buttons
button1 = Button(m_screen, text="Create New")
button1.pack()

button2 = Button(m_screen, text="Add Data To Existing Form")
button2.pack()

button3 = Button(m_screen, text="Cancel")
button3.pack()
m_screen.mainloop()

'''
The purpose of this application is to allow the user to create their own forms that can be used to easily store data in csv files.

The main menu is the center of the overall application. Each of the buttons on the main menu need to be defined as functions so that they can be called when each button on the main menu is clicked on.

I am going to go ahead and integrate sqlite into the application code.

update 8/5/2020 I need to be able to work with one UI window at a time. i.e., when a selection is made, that menu is closed and another is opened. This is my first project working with a GUI in Python. I typically work on data science projects.
'''

#Import the needed libraries
#Import the needed libraries
import tkinter
import os
import numpy as np
import pandas as pd
import pandasql as psql
import sqlite3 #Should be able to use this to store the data... Will need to create a new database if the database does not currently exist though.
import time
from tkinter import * #"*" Means all
from tkinter.ttk import *
#Defined Functions

class basic():
    
    def OBL(): #Prints one blank line
        print("")

    def delay2(): #Application sleeps for two seconds
        time.sleep(2)
  
class gui(): #Functions to establish the GUI of the application

    def main_event_loop():
        root = Tk()
        root.title("Form_Creator")
        label = Label(root, text = "Welcome to the Form Creator tool!").pack()
        exit_button = Button(root, text = 'Exit', command = root.quit()).pack
        root.mainloop()

#Opening Process
gui.main_event_loop()

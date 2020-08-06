'''
The purpose of this application is to allow the user to create their own forms that can be used to easily store data in csv files.

The main menu is the center of the overall application. Each of the buttons on the main menu need to be defined as functions so that they can be called when each button on the main menu is clicked on.

I am going to go ahead and integrate sqlite into the application code.

update 8/5/2020 I need to be able to work with one UI window at a time. i.e., when a selection is made, that menu is closed and another is opened. This is my first project working with a GUI in Python. I typically work on data science projects.
'''

#Import the needed libraries
import tkinter
import os
import numpy as np
import pandas as pd
import pandasql as psql
import sqlite3 #Should be able to use this to store the data... Will need to react a new database if the database does not currently exist though.
from tkinter import *

#Defined functions

def OBL(): #Prints one blank line
    print("")

#def search_4_db(): #ADD IF THEN FUNCTION THAT SEARCH FOR FILE AND CREATES IF IT DOES NOT EXIST

def db_connection():
	conn = sqlite3.connect('Form_DB.db')


def b1(): #This will allow the user to create a new form when button 1 is pressed.
	create_new_form = Tk()
	create_new_form.title("Create a New Form")
	cnf_desc = Label(create_new_form, text="The application will now walk you through the process of creating a new form")
	cnf_desc.pack()

def b2(): #Adds data to an existing form
	add_data = Tk()
	add_data.title('Add data to existing form')
	ad_desc = Label(add_data, text="This function is under development")

def b3(): #Allows the user to exit the application
	quit()

#Opening Process
open_screen = Tk()
open_screen.title("Opening Processes")
if os.path.isfile('Form_DB.db') == TRUE:
	Label(open_screen, text="Database has already been established")
else:
	db_connection()
	Label(open_screen, text="Your database has been connected")


#Main menu
m_screen = Tk()
m_screen.title("Form Tool Main Menu")
ms_description = Label(m_screen, text="The purpose of this application is to allow the user to create their own forms that can be used to easily store data in csv files or via SQL databases.")
ms_description.pack()

#Main menu buttons
button1 = Button(m_screen, text="Create New", command = b1)
button1.pack()

button2 = Button(m_screen, text="Add Data To Existing Form", command = b2)
button2.pack()

button3 = Button(m_screen, text="Cancel", command = b3)
button3.pack()
m_screen.mainloop()

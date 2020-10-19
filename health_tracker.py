#Import the needed libraries
import numpy as np
import pandas as pd
import pandasql as psql
import time
import tkinter
from tkinter import *

#Application improvement functions
class app_imp():

	def obl(): #Adds one blank line on terminal output
		print("")

	def delay1(): #Sleep application for 1 second
		time.delay(1)

	def help(): #Displays basic application information
		print("PRINTED TEXT HERE")

#Defined values
database = "form_data.sqlite3"
log_file = "form_dat.csv"
help = app_imp.help()

window = Tk()
window.title("Health Tracker Form")

#Form Labels
a = Label(window, text="Current weight (lbs): ").grid(row=0, column=0)
b = Label(window, text="Current height (in): ").grid(row=1, column=0)
c = Label(window, text="Current heart rate (BPM): ").grid(row=2, column=0)
d = Label(window, text="How do you feel today? ").grid(row=3, column=0)
e = Label(window, text="Rate your day on a scale of 1 - 5: ").grid(row=4, column=0)
f = Label(window, text="Was/will today (be) stressful? ").grid(row=5, column=0)

#Form Entries
weight = tkinter.Entry().grid(row=0, column=1)
height = tkinter.Entry().grid(row=1, column=1)
h_rate = tkinter.Entry().grid(row=2, column=1)
feeling = tkinter.Entry().grid(row=3, column=1)
rate_day = tkinter.Entry().grid(row=4, column=1)
stress = tkinter.Entry().grid(row=5, column=1)
exit = Button(window, text="Exit", command=window.destroy).grid(row=6, column=0)
submit = Button(window, text='Submit').grid(row=6, column=1)
window.mainloop()


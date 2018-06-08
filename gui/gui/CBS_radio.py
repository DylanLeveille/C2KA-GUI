"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.

def rows_CBS(radioRowsCBS, radioBoxCBS, concreteScrollingArea, frameCBS, textBoxCBS):
  textBoxCBS.pack_forget()
  concreteScrollingArea.pack(expand=1, fill = BOTH) 
  frameCBS.pack(anchor = W)
  radioRowsCBS.config(state = 'disabled')
  radioBoxCBS.config(state = 'normal')  
  
def box_CBS(radioRowsCBS, radioBoxCBS, concreteScrollingArea, frameCBS, textBoxCBS):
  concreteScrollingArea.pack_forget()
  frameCBS.pack_forget()
  textBoxCBS.pack()
  radioRowsCBS.config(state = 'normal')
  radioBoxCBS.config(state = 'disabled')
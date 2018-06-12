"""Imported modules."""
from tkinter import * ##Import the tkinter module to allow construction of the GUI interface.

"""Function to change CBS page based on radio button."""
def change_CBS(radioRowsCBS, radioBoxCBS, concreteScrollingArea, frameCBS, 
               textBoxCBSFrame, whichRadio):
  """ (tkinter.Radiobutton, tkinter.Radiobutton, vertSuperscroll.Scrolling_Area, 
       tkinter.Frame, tkinter.Text, StringVar) -> (none)
    
    Switches the display of the main window based on which radio button is 
    clicked. If user clicked on rowsCBS, then the concrete behaviours 
    will be displayed as rows. If the user clicked on boxCBS, then the
    concrete behaviours will be displayed as a text box.
  
  """   
  if (whichRadio.get() == 'Rows'): ##User clicked on rowsCBS Button.
    textBoxCBSFrame.pack_forget()
    concreteScrollingArea.pack(expand=1, fill = BOTH) 
    frameCBS.pack(anchor = W)
    radioRowsCBS.config(state = 'disabled')
    radioBoxCBS.config(state = 'normal')  
    
  else: ##User clicked on boxCBS Button.
    concreteScrollingArea.pack_forget()
    frameCBS.pack_forget()
    textBoxCBSFrame.pack()
    radioRowsCBS.config(state = 'normal')
    radioBoxCBS.config(state = 'disabled')
# Python 2.7
from tkinter import *
import tkinter.scolledtext

class App(object):

    def __init__(self):
        self.root = Tk()

    # create a Text widget with a Scrollbar attached
        self.txt = scrolledtext(self.root, undo=True)
        self.txt['font'] = ('consolas', '12')
        self.txt.pack(expand=True, fill='both')

app = App()
app.root.mainloop()
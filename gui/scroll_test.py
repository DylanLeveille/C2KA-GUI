from tkinter import *


class NotebookDemo(Frame):

    def __init__(self):      
        Frame.__init__(self)       
        self.pack(expand=1, fill=BOTH)
        self.master.title('Sample')
        self.master.geometry("650x550+100+50")
        


    def _createPanel(self):

        # create frame inside top level frame
        panel = Frame(self)    
        panel.pack(side=TOP, fill=BOTH, expand=1)

        # create the notebook
        nb = Notebook(panel)
        nb.pack(fill=BOTH, expand=1, padx=2, pady=3)        
        


    def _FirstTab(self, nb):

        # frame to hold content
        frame = Frame(nb)

        #textbox
        txtOutput = Text(frame, wrap = NONE, height = 17, width = 70)
        txtOutput.place(x=10, y=75)

        #button
        btnStart = Button(frame, text = 'Start', underline=0)
        btnStart.place(x=220, y=380)

        #scrollbar
        vscroll = Scrollbar(frame, orient=VERTICAL, command=txtOutput.yview)
        #txtOutput['yscroll'] = vscroll.set
        #vscroll.pack(side=RIGHT, fill=Y)
        #txtOutput.pack(fill=BOTH, expand=Y)

        #add to notebook (underline = index for short-cut character)
        nb.add(frame, text='TAB 1', underline=0, padding=2)

if __name__ == '__main__':
    app = NotebookDemo()
    app.mainloop()
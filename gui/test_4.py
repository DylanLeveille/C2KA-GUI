from tkinter import*

class DpWin(object):
    def run(self):
        root=Tk()
        root.geometry('768x612')
        title='dp'
        root.title(title)

        f = Frame(root)
        f.pack()

        xscrollbar = Scrollbar(f, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=N+S+E+W)

        yscrollbar = Scrollbar(f)
        yscrollbar.grid(row=0, column=1, sticky=N+S+E+W)

        text = Text(f, wrap=NONE,
                    xscrollcommand=xscrollbar.set,
                    yscrollcommand=yscrollbar.set)
        text.grid(row=0, column=0)

        xscrollbar.config(command=text.xview)
        yscrollbar.config(command=text.yview)
        text.insert(END, 'a'*999)
        mainloop()

    def start(self):
        self.b_start.config(state=DISABLED)
        self.b_stop.config(state=ACTIVE)

    def stop(self):
        self.b_stop.config(state=DISABLED)
        self.b_start.config(state=ACTIVE)

if __name__=='__main__':
    win=DpWin()
    win.run()
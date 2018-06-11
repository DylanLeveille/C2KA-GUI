from tkinter import *


def killme():
    root.quit()
    root.destroy()

root=Tk()

root.geometry('1000x1000')

lb=Text(root, width=300, height=5)

lb.pack(side=LEFT, fill=BOTH, expand = YES)

yscrollbar=Scrollbar(root, orient=VERTICAL, command=lb.yview)
yscrollbar.pack(side=RIGHT, fill=Y)
lb["yscrollcommand"]=yscrollbar.set

root.mainloop()
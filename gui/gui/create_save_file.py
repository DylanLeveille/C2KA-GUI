from tkinter import filedialog

def create_save_file():
    pathName =  filedialog.asksaveasfilename(initialdir = "/", title = "Save text file", filetypes = ((".txt","*.txt"), ("all files","*.*")), initialfile = 'agentspec.txt')
 
    if pathName!= '':
        
        dst = open(pathName, "w+")
        src = open("agentspec.txt", "r")
        dst.write(src.read())
        
        dst.close()
        src.close()
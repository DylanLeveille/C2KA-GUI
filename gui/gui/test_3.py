import tkinter as tk

root = tk.Tk()
for text in (
        "Hello", "short", "All the buttons are not the same size",
        "Options", "Test2", "ABC", "This button is so much larger"):
    button = tk.Button(root, text=text)
    button.pack(side="right", fill="x")

root.mainloop()
import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets title of GUI window
        self.master.title("File Transfer")


if __name__ == "__main__":
    root = tk.tk()
    App = ParentWindow(root)
    root.mainloop()

#Creates button to select files from source directory
self.sourceDir_btn = Button(text="Select Source", width=20)
#Positions source button in GUI using tkinteer grid()
self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30,0))

#Creates entry for source directory selection
self.source_dir = Entry(width=75)
#Positions entry in GUI using tkinter grid() padx and pady are the same as
#the button to ensure they will line up
self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

#Creates button to select destiantion of files from destnation directory
self.destDir_btn = Button(text="Select Destination", width=20)
#Positions entry in GUI using tkinter grid() padx and pady are the same as
#the button to ensure they will line up
self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

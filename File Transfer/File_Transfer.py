import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import time
import datetime
import shutil
from datetime import date
from datetime import datetime, timedelta

class ParentWindow(Frame):
    def __init__(self, master):
            
        Frame.__init__(self)
        #Sets title of GUI window
        self.master = master
        self.master.title("File Transfer")

        #Creates button to select files from source directory
        self.sourceDir_btn = Button(
            text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinteer grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30,0))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Creates button to select destiantion of files from destnation directory
        self.destDir_btn = Button(
            text="Select Destination", width=20, command=self.destDir)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Creates entry for source directory selection
        self.destination_dir = Entry(width=75)
        #Postions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #Creates button to transfer files
        self.transfer_btn = Button(
            text="Transfer Files", width=20, command=self.transferFiles)
        #Postions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

    #Creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in thhe entry widget,
        #this allows the path to be inserted into the entry widget properly.
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir entry
        self.source_dir.insert(0, selectSourceDir)
        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)

    #Creates function to select desitnation directory.
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in thhe entry widget,
        #this allows the path to be inserted into the entry widget properly.
        self.destination_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir entry
        self.destination_dir.insert(0, selectDestDir)
        #Creates button to select files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)

    #Creates function to transfer files from one directory to another
    def transferFiles(self):
        #Module os.path.join
        #modeul os.path.getmtime
        #modeul os.getmtime
        #modeul os.daytime.fromtimestimestamp
        #modeul os.timedelta geeks for geeks and tutorial point 
        #Gets source directory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        #Gets a list of files in the source directory
        source_files = os.listdir(source)
        #Runs through each file in the source directory
        #Gets today's date
        One_day_ago = datetime.now()-timedelta(hours=24)
        print(One_day_ago)
        for i in source_files:
            #builds the file path
            path = os.path.join(source, i)
            #gets modification time which comes back as a
            modification_time = os.path.getmtime(path)
            #converts the modification time to a date format we can work with
            fileDateTime = datetime.fromtimestamp(modification_time);
            if (fileDateTime > One_day_ago):
                #moves each file from the source to the destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transfered.')
            

    #Creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()
                                
                                
                        
                

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

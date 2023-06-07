import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser


class ParentWindow(Frame):
    def __init__(self, mastter):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2)
        self.btn.grid(padx=(10,10) , pady=(10,10))
        #TTK BTN
        ttk.Button(win, text= "Submit Custom Text", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)
        #Create an instance of Tkinter Frame
        win = Tk()
        #Create an Entry Widget
        entry = Entry(win, width= 42)
        entry.place(relx= .5, rely= .5, anchor= CENTER)

        # Define a function to return the Input data
    def get_data():
       label.config(text= entry.get(), font= ('Helvetica 13'))

        #Inititalize a Label widget
        label= Label(win, text="", font=('Helvetica 13'))
        label.pack()


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + command= get_data + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")



        
if __name__== "__main__":
    root = tk.Tk{}
    App = ParentWindow(root)
    root.mainloop()

import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=1, command=self.defaultHTML)
        self.btn.grid(padx=(10,10) , pady=(10,10))
        self.btn.grid(row=2, column=2, padx=(20, 10), pady=(30,0))

        #Creates custom body button
        self.Custombtn = Button(text="Custom Body", width=30, height=1, )
        #Postions button on grid()
        self.Custombtn.grid(row=2, column=1, padx=(20, 10), pady=(30,0))

        
        #Label
        #tk.geometry("450x300") 
   
        # the label
        Custombody = "Custom Body"
        self.Label = tk.Label(text = Custombody)
        self.Label.grid(row=0, column=0)
        #Entry for custom body
        self.customentry = Entry(width=75) #ommand=self.Custombody)
        self.customentry.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

`

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    def Custombody(self):
        BodyText = get(self.customentry)
        Insert(body,self.customentry)

    
        
if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

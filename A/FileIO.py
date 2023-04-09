import os

fName = "Hello.txt"

fPath = "C:\\Users\\Domin\\Documents\\GitHub\\Python\\A"

abPath = os.path.join(fPath, fName)
print(abPath)

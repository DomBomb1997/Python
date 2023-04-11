import sqlite3
#Imports sqllite
conn = sqlite3.connect('Files.db')
#connects to the database
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
          col_Files TEXT)")
    conn.commit()
conn.close()
#creates the database if there isn't one
conn = sqlite3.connect('test.db')
#connects to the database again

Filelist = ('Information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt','data.pdf','myPhoto.jpg')
#tuple list
for x in Filelist:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            # The value for each row will be one name out of the tuple therefore (x,)
            # will denote a one element tuple for each name ending in txt
            cur.execute('INSERT INTO tbl_Files (cole_Files) VALUES (?)', (x,))
            print(x)

conn.close

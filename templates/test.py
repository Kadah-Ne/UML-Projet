import sqlite3

conn = sqlite3.connect('ma_base.db')

title = request.form['searchTitle']
author = request.form['searchAuthor']
topic = request.form['searchTopic']
format = request.form['format']
lib = librairie                     #a changer

if title != "":
    if format !="None":
        cursor.execute("""SELECT barcode,tag FROM BookItem where title=? and format=? and library=?""", (title,format,lib,))
    else:
        cursor.execute("""SELECT barcode,tag FROM BookItem where title=? and library=?""", (title,lib,))

elif author != "":
    if format !="None":
        cursor.execute("""SELECT barcode,tag FROM BookItem where author=? and format=? and library=?""", (author,format,lib,))
    else:
        cursor.execute("""SELECT barcode,tag FROM BookItem where title=? and library=?""", (title,lib,))

elif topic != "":
    if format !="None":
        cursor.execute("""SELECT barcode,tag FROM BookItem where title=? and format=? and library=?""", (topic,format,lib,))
    else:
        cursor.execute("""SELECT barcode,tag FROM BookItem where title=? and library=?""", (title,lib,))

elif format != "None":
    cursor.execute("""SELECT barcode,tag FROM BookItem where format=? and library=?""", (format,lib,))

rows = cursor.fetchall()

for row in rows:
    print('{0} , {1}'.format(row[0], row[1]))
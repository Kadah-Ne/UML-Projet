import DBmanager

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

with DBmanager.open('cache', 'c') as db:

    # Record some values
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'

    # Note that the keys are considered bytes now.
    assert db[b'www.python.org'] == b'Python Website'
    # Notice how the value is now in bytes.
    assert db['www.cnn.com'] == b'Cable News Network'

    # Often-used methods of the dict interface work too.
    print(db.get('python.org', b'not present'))

    # Storing a non-string key or value will raise an exception (most
    # likely a TypeError).
    db['www.yahoo.com'] = 4

for row in rows:
    print('{0} , {1}'.format(row[0], row[1]))
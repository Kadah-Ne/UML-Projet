import sqlite3

def search(title, author, topic, format, library):
    
    if title == "":
        title = "%"
    if author == "":
        author = "%"
    if topic == "":
        topic = "%"
    if format == "":
        format = "%"
    
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()

    #cursor.execute("""SELECT Book.ISBN, name, overview, publisher, publicationDate, Book.lang, authors FROM (BookItem INNER JOIN Book on BookItem.ISBN = Book.ISBN) INNER JOIN Catalog on BookItem.Barcode = Catalog.BookItemBarcode and BookItem.Tag = Catalog.BookItemTag where title like ? and authors like ? and Book.subject like ? and format like ? and Catalog.LibraryId = ? """, (title,author,topic,format,library,))
    cursor.execute("""Select * from Book""")
    results = tuple(cursor.fetchall())
    print(results)
    cursor.close()
    connection.close()
    return results
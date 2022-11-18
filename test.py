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

    cursor.execute("""SELECT Book.ISBN, name, overview, publisher, publicationDate, Book.lang, authors FROM (BookItem INNER JOIN Book on BookItem.ISBN = Book.ISBN) where title like '?' and authors like '?' and topic like '?' and format like '?' and libraryId = '?' """, (title,author,topic,format,library,))

    results = tuple(cursor.fetchall())
    cursor.close()
    connection.close()
    return results
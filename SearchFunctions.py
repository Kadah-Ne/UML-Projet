import sqlite3

def search(title ="", author="", topic="", format="", library = 0):
    
    if title == "":
        title = "%"
    else :
        title = "%"+title+"%"
    if author == "":
        author = "%"
    else :
        author = "%"+author+"%"
    if topic == "":
        topic = "%"
    else :
        topic = "%"+topic+"%"
    if format == "":
        format = "%"
    else :
        fomat = "%"+format+"%"
    
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()

    cursor.execute("""SELECT Book.ISBN, name,Book.subject, overview, publisher, publicationDate, Book.lang, authors FROM (BookItem INNER JOIN Book on BookItem.ISBN = Book.ISBN) INNER JOIN Catalog on BookItem.Barcode = Catalog.BookItemBarcode and BookItem.Tag = Catalog.BookItemTag where title like ? and authors like ? and Book.subject like ? and format like ? and Catalog.LibraryId = ? """, (title,author,topic,format,library,))   
    #cursor.execute("""Select * from Book""")
    #cursor.execute("""SELECT * from Book WHERE name like ? and authors like ?""",(title,author))
    if cursor.arraysize < 1 :
        results = tuple(cursor.fetchall())
    else :
        results = cursor.fetchall()
    
    #print(results)
    cursor.close()
    connection.close()
    return results

def LogIn(Username = "", Passwrd = ""):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    
    cursor.execute("""SELECT Id, Passwrd, Account.LibraryId, Account.type, Account.state FROM LogIn INNER JOIN Account on LogIn.Id = Account.number WHERE LogIn.Username like ?""",(Username,))
    result = cursor.fetchall()
    if result[0][1] == Passwrd:
        UserId = result[0][0]
        LibId = result[0][2]
        UserType = result[0][3]
        AccountState = result[0][4]
        return [UserId,LibId,UserType,AccountState]
    else :
        return -1

def searchHistorique(UserId : int):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute(f"""SELECT Book.ISBN, name, authors, Item.borrowed,Item.dueDate,isOverdue FROM Book INNER JOIN Bookitem as Item on Item.ISBN = Book.ISBN INNER JOIN IsBorrowed on IsBorrowed.BookId = Item.ISBN INNER JOIN Account on Account.number = IsBorrowed.PatronId WHERE Account.number like {UserId}""")
    resultB = cursor.fetchall()
    cursor.execute(f"""SELECT Book.ISBN, name, authors, Item.borrowed,Item.dueDate,isOverdue FROM Book INNER JOIN Bookitem as Item on Item.ISBN = Book.ISBN INNER JOIN IsReserved on IsReserved.BookId = Item.ISBN INNER JOIN Account on Account.number = IsReserved.PatronId WHERE Account.number like {UserId}""")
    resultR = cursor.fetchall()
    result = []
    for i in resultB:
        result.append(i)
    for i in resultR:
        result.append(i)
    return result
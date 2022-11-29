import sqlite3

import StarterDB


def characterlist():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor() #obligatoire
    Firsttable = """CREATE TABLE IF NOT EXISTS 
      Book(ISBN int(14),
      name TEXT,
      subject TEXT,
      overview TEXT,
      publisher TEXT,
      publicationDate TEXT,
      lang TEXT,
      authors TEXT,
      PRIMARY KEY (ISBN)
    )"""

    Authortable = """CREATE TABLE IF NOT EXISTS Author (
        name TEXT PRIMARY KEY,
        biography TEXT,
        birthdate TEXT,
        books TEXT
      )"""

    Accounttable = """ CREATE TABLE IF NOT EXISTS Account (
      `number` int(11) NOT NULL,
      `opened` date NOT NULL,
      `state` varchar(255) NOT NULL,
      `type` varchar(255) NOT NULL,
      `LibraryId` int(11) NOT NULL,
      `FullName` varchar(255) NOT NULL,
      PRIMARY KEY (number),
      FOREIGN KEY (LibraryId) REFERENCES Library(LibraryId)
      FOREIGN KEY (FullName) REFERENCES Patron(FullName)
    )"""

    UserTable = """CREATE TABLE IF NOT EXISTS `Patron` (
      `FullName` varchar(255),
      `Address` varchar(255),
      PRIMARY KEY(FullName)
    )"""

    Bookitemtable= """CREATE TABLE IF NOT EXISTS `Bookitem`  (
      `barcode` varchar(255) NOT NULL,
      `tag` float NOT NULL,
      `ISBN` int(14) NOT NULL,
      `subject` varchar(255) NOT NULL,
      `title` text NOT NULL,
      `isReferenceOnly` tinyint(1) NOT NULL,
      `lang` varchar(255) NOT NULL,
      `numberOfPages` int(11) NOT NULL,
      `format` varchar(255) NOT NULL,
      `borrowed` date NOT NULL,
      `loanPeriod` int(11) NOT NULL,
      `dueDate` date NOT NULL,
      `isOverdue` tinyint(1) NOT NULL,
      PRIMARY KEY (barcode, tag),
      FOREIGN KEY (ISBN) REFERENCES Book(ISBN),
      FOREIGN KEY (subject) REFERENCES Book(subject)
    )"""

    BookStateTable = """CREATE TABLE IF NOT EXISTS `BookState` (
      """
    
    Catalogtable= """CREATE TABLE IF NOT EXISTS `Catalog` (
      `LibraryId` int(11) NOT NULL,
      `BookItemBarcode` varchar(255) NOT NULL,
      `BookItemTag` varchar(255) NOT NULL,
      PRIMARY KEY (BookItembarcode,BookItemTag,LibraryId),
      FOREIGN KEY (BookItembarcode) REFERENCES Bookitem(barcode),
      FOREIGN KEY (LibraryId) REFERENCES Library(LibraryId)
    )"""

    Librarytable = """CREATE TABLE IF NOT EXISTS `Library` (
      `LibraryId` int(11) NOT NULL PRIMARY KEY,
      `Name` varchar(255) NOT NULL,
      `Address` varchar(255) NOT NULL,
      `BookItemTag` varchar(255) NOT NULL
    )"""

    LogInTable = """CREATE TABLE IF NOT EXISTS `LogIn` (
      `Id` int(11) NOT NULL,
      `Username` varchar(255) NOT NULL,
      `Passwrd` varchar(255) NOT NULL,
      PRIMARY KEY (Id,Username)
      FOREIGN KEY (Id) REFERENCES Account(number)
    )"""

    cursor.execute(Firsttable)
    cursor.execute(Authortable)
    cursor.execute(Accounttable)
    cursor.execute(Bookitemtable)
    cursor.execute(Catalogtable)
    cursor.execute(Librarytable)
    cursor.execute(UserTable)
    cursor.execute(LogInTable)
    cursor.close()

    connection.close()
    StarterDB.fillDB()

    connection = sqlite3.connect('library.db')
    cursor = connection.cursor() #obligatoire

    cursor.execute("SELECT * FROM Book")
    results = cursor.fetchall()
    cursor.execute("SELECT * FROM Author")
    #authorresult = cursor.fetchall()
    cursor.execute("SELECT * FROM Account")
    #accountresult = cursor.fetchall()



    

    return results #,authorresult,accountresult

print(characterlist())
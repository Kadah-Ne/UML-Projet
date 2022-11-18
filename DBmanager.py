import sqlite3

def characterlist():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor() #obligatoire
    Firsttable = """CREATE TABLE IF NOT EXISTS 
    Book(ISBN INTEGER,
    name TEXT,subject TEXT,
    overview TEXT,
    publisher TEXT,
    publicationDate TEXT,
    lang TEXT,
    authors TEXT,
    PRIMARY KEY (ISBN)
    )"""
    Authortable = """CREATE TABLE IF NOT EXISTS 
        Author(name TEXT PRIMARY KEY,
        biography TEXT,
        birthdate TEXT,
        books TEXT)"""
    Accounttable = """ CREATE TABLE IF NOT EXISTS Account (
  `number` int(11) NOT NULL,
  `opened` date NOT NULL,
  `state` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `LibraryId` int(11) NOT NULL,
  PRIMARY KEY (number),
  FOREIGN KEY (LibraryId) REFERENCES Library(LibraryId)
)"""
    Bookitemtable= """CREATE TABLE IF NOT EXISTS `Bookitem`  (
  `barcode` varchar(255) NOT NULL,
  `tag` float NOT NULL,
  `ISBN` varchar(255) NOT NULL,
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
      `Address` varchar(255) NOT NULL,
      `BookItemTag` varchar(255) NOT NULL
    )"""

    cursor.execute(Firsttable)
    cursor.execute(Authortable)
    cursor.execute(Accounttable)
    cursor.execute(Bookitemtable)
    cursor.execute(Catalogtable)
    cursor.execute(Librarytable)

    cursor.execute("INSERT INTO Book VALUES (12345,'sacreu bleu','histoire','histoire','histoire','histoire','histoire','Monsieur R')")
    cursor.execute(
        "INSERT INTO account VALUES (1235,'11/02/2020','histoire','histoire','1')")
    cursor.execute("INSERT INTO Author VALUES ('maximus','maximum','1755','Peter Pan')")

    # cursor.execute("INSERT INTO Book VALUES (153548,32,86)")

    cursor.execute("SELECT * FROM Book")
    results = cursor.fetchall()
    cursor.execute("SELECT * FROM Author")
    #authorresult = cursor.fetchall()
    cursor.execute("SELECT * FROM Account")
    #accountresult = cursor.fetchall()



    cursor.close()
    connection.close()


    return results #,authorresult,accountresult

#print(characterlist())
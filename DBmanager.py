import sqlite3

def characterlist():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor() #obligatoire
    Firsttable = """CREATE TABLE IF NOT EXISTS 
    Joueur(ISBN INTEGER PRIMARY KEY,name TEXT,subject TEXT,overview TEXT,publisher TEXT,publicationDate TEXT,lang TEXT)"""

    cursor.execute(Firsttable)
    cursor.execute("INSERT INTO Joueur VALUES (12345,'sacreu bleu','histoire')")
    cursor.execute("INSERT INTO Joueur VALUES (153548,32,86)")
    cursor.execute("SELECT * FROM Joueur")

    results = tuple(cursor.fetchall())
    cursor.close()
    connection.close()


    return results

#print(characterlist())
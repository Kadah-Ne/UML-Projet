import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()

cursor.execute("""DROP TABLE Book""")
cursor.execute("""DROP TABLE Author""")
cursor.execute("""DROP TABLE Account""")
cursor.execute("""DROP TABLE Bookitem""")
cursor.execute("""DROP TABLE Catalog""")
cursor.execute("""DROP TABLE Library""")
connection.commit()
cursor.close()
connection.close()
#DBmanager.characterlist()
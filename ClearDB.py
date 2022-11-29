import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS Book""")
cursor.execute("""DROP TABLE IF EXISTS Author""")
cursor.execute("""DROP TABLE IF EXISTS Account""")
cursor.execute("""DROP TABLE IF EXISTS Bookitem""")
cursor.execute("""DROP TABLE IF EXISTS Catalog""")
cursor.execute("""DROP TABLE IF EXISTS Library""")
cursor.execute("""DROP TABLE IF EXISTS Patron""")
cursor.execute("""DROP TABLE IF EXISTS LogIn""")
connection.commit()
cursor.close()
connection.close()
#DBmanager.characterlist()
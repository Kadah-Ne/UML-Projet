import sqlite3

def fillDB():
    try:
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()  # obligatoire
        cursor.execute(
            "INSERT INTO Book VALUES (158,'sacreu bleu','histoire','histoire','histoire','histoire','histoire','Monsieur R')")
        cursor.execute(
            "INSERT INTO account VALUES (123,'11/02/2020','histoire','histoire','1')")
        cursor.execute("INSERT INTO Author VALUES ('maximus','maximum','1755','Peter Pan')")

        connection.commit()
        print("inserted example books on startup")
    except:
        print("Initial examples already exist")


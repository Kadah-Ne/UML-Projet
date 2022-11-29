import sqlite3


def fillDB():
    try:
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()  # obligatoire

        cursor.execute(
            "INSERT INTO Book VALUES (978-0062662569,'The Poppy War','Grimdark, High fantasy','The war','Harper Voyager','May 1, 2018','EN','R.F. Kuang')")

        cursor.execute(
            "INSERT INTO Author VALUES ('R.F. Kuang','something','1996','The Poppy War')")

        cursor.execute(
            "INSERT INTO Bookitem VALUES ('MartinIsTheBest','123','978-0062662569','Grimdark, High fantasy','The Poppy War','0','EN','544','Hardcover','0','0','0','0')"
        )

        cursor.execute(
            "INSERT INTO Library VALUES ('1','30 rue joseph rey','12345')"
        )

        cursor.execute(
            "INSERT INTO Catalog VALUES ('1','MartinIsTheBest','12345')"
        )

        # cursor.execute(
        #     "INSERT INTO Account VALUES ('1','01/05/1999','Open','Type ?','1'")

        connection.commit()
        print("inserted example books on startup")
    except:
        print("Initial examples already exist")

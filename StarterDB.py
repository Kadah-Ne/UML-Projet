import sqlite3


def fillDB():
    try:
        connection = sqlite3.connect('library.db')
        cursor = connection.cursor()  # obligatoire

        cursor.execute(
            "INSERT INTO Book VALUES (9780062662569,'The Poppy War','Grimdark, High fantasy','The war','Harper Voyager','May 1, 2018','EN','R.F. Kuang')")

        cursor.execute(
            "INSERT INTO Book VALUES (9780316075558,'The Black Prism','Grimdark, High fantasy','Lightbringer serie','Orbit','August 25, 2010','EN','Brent Weeks')")

        cursor.execute(
            "INSERT INTO Book VALUES (9780316362535,'Bloody Rose','Grimdark, High fantasy','The 2nd book in the band series','Orbit','August 28, 2018','EN','Nicholas Eames')")

        cursor.execute(
            "INSERT INTO Author VALUES ('R.F. Kuang','something','1996','The Poppy War')")

        cursor.execute(
            "INSERT INTO Author VALUES ('Nicholas Eames','something','unknown','Bloody Rose')")

        cursor.execute(
            "INSERT INTO Author VALUES ('Brent Weeks','something','1977','The Black Prism')")

        cursor.execute(
            "INSERT INTO Bookitem VALUES ('MartinIsTheBest','123',9780316075558,'Grimdark, High fantasy','The Black Prism','0','EN','600','Hardcover','0','0','0','0')"
        )

        cursor.execute(
            "INSERT INTO Bookitem VALUES ('MartinIsTheBest','1234',9780062662569,'Grimdark, High fantasy','The Poppy War','0','EN','544','Hardcover','22/11/2022','30','22/12/2022','0')"
        )

        cursor.execute(
            "INSERT INTO Bookitem VALUES ('MartinIsTheBest','12345',9780316362535,'Grimdark, High fantasy','Bloody Rose','0','EN','560','PaperBack','0','0','0','0')"
        )

        cursor.execute(
            "INSERT INTO Library VALUES ('1','Librairie du petit jean','30 rue joseph rey','12345')"
        )

        cursor.execute(
            "INSERT INTO Catalog VALUES ('1','MartinIsTheBest','12345')"
        )
        cursor.execute(
            "INSERT INTO Catalog VALUES ('1','MartinIsTheBest','1234')"
        )
        cursor.execute(
            "INSERT INTO Catalog VALUES ('1','MartinIsTheBest','123')"
        )

        

        cursor.execute(
            "INSERT INTO Patron VALUES ('Laure','11 rue casimir brenier')"
        )

        cursor.execute(
            "INSERT INTO Account VALUES ('2','20/01/2013','Active','Patron','1','Laure')"
        )

        cursor.execute(
            "INSERT INTO LogIn VALUES ('2','Lore','123')"
        )

        cursor.execute(
            "INSERT INTO Patron VALUES ('Martin Gouviaux','18bis chemin de la viotte')"
        )

        cursor.execute(
            "INSERT INTO Account VALUES ('1','01/05/1999','Active','Lib','1','Martin Gouviaux')"
        )

        cursor.execute(
            "INSERT INTO LogIn VALUES ('1','Martin','1')"
        )
        
        cursor.execute(
            "INSERT INTO IsBorrowed VALUES ('9780062662569','1','1')"
        )

        cursor.execute(
            "INSERT INTO IsReserved VALUES ('9780062662569','2','1')"
        )

        cursor.execute(
            "INSERT INTO IsReserved VALUES ('9780316075558',NULL,'0')"
        )

        cursor.execute(
            "INSERT INTO IsReserved VALUES ('9780316362535',NULL,'0')"
        )
        

        connection.commit()
        print("inserted example books on startup")
    except:
        print("Initial examples already exist")

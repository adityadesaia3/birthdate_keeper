import mysql.connector

def add_birthdate_to_db():
    pass

def create_db():
    connection = None
    try:
        connection = mysql.connector.connect(host='localhost', user='root', password='')
        if connection.is_connected():
            cursor = connection.cursor()

            # creating database "birthdate_keeper_db"
            try:
                cursor.execute("create database birthdate_keeper_db")

                # Connecting to newly created database
                connection = mysql.connector.connect(host='localhost', user='root', password='', database="birthdate_keeper_db")
                
                # Getting new cursor
                cursor = connection.cursor()
                
                # Adding table to newly created database
                cursor.execute("CREATE TABLE birthdate_keeper_tb (id INT NOT NULL AUTO_INCREMENT , name TEXT NOT NULL , birthdate DATE NOT NULL , image BLOB , PRIMARY KEY (id))")
            except mysql.connector.Error as error:
                print(error)
            finally:
                cursor.close()
    except mysql.connector.Error as error:
        print(error)
    finally:
        if connection:
            connection.commit()
            connection.close()
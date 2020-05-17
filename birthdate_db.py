import mysql.connector

def get_max_id():
    connection = None
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="birthdate_keeper_db")
        if connection.is_connected():
            cursor = connection.cursor()

            try:
                # insert data
                select_query = f"select max(id) from birthdate_keeper_tb"
                cursor.execute(select_query)
                max_id = cursor.fetchone()[0]
                
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
    if max_id:
        return max_id
    else:
        return 0

def fetch_birthdates_today():
    birthdate_data = None
    connection = None
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="birthdate_keeper_db")
        if connection.is_connected():
            cursor = connection.cursor()

            try:
                # select data
                select_query = f"SELECT * FROM birthdate_keeper_tb where EXTRACT(MONTH FROM birthdate) = EXTRACT(MONTH FROM CURRENT_DATE) and EXTRACT(day FROM birthdate) = EXTRACT(DAY FROM CURRENT_DATE)"
                cursor.execute(select_query)
                birthdate_data = cursor.fetchall()
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
    return birthdate_data

def fetch_birthdates_from_db():
    birthdate_data = None
    connection = None
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="birthdate_keeper_db")
        if connection.is_connected():
            cursor = connection.cursor()

            try:
                # select data
                select_query = f"SELECT * FROM birthdate_keeper_tb order by EXTRACT(MONTH FROM birthdate), EXTRACT(DAY FROM birthdate)"
                cursor.execute(select_query)
                birthdate_data = cursor.fetchall()
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
    return birthdate_data


def fetch_single_birthdate_from_db(b_id):
    birthdate_data = None
    connection = None
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="birthdate_keeper_db")
        if connection.is_connected():
            cursor = connection.cursor()

            try:
                # insert data
                select_query = f"select * from birthdate_keeper_tb where id = {b_id}"
                cursor.execute(select_query)
                birthdate_data = cursor.fetchall()[0]
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
    return birthdate_data


def add_birthdate_to_db(name, birthdate, photo_name):
    connection = None
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="birthdate_keeper_db")
        if connection.is_connected():
            cursor = connection.cursor()

            try:
                # insert data
                insert_query = f"insert into birthdate_keeper_tb(name, birthdate, photo_name) values ('{name}', '{birthdate}', '{photo_name}')"
                cursor.execute(insert_query)
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


def update_birthdate_from_db(b_id, name, birthdate, photo_name):
    connection = None
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="birthdate_keeper_db")
        if connection.is_connected():
            cursor = connection.cursor()

            try:
                # update data
                update_query = f"update birthdate_keeper_tb set name = '{name}', birthdate = '{birthdate}', photo_name = '{photo_name}' where id = {b_id}"
                cursor.execute(update_query)
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


def delete_birthdate_from_db(b_id):
    connection = None
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="birthdate_keeper_db")
        if connection.is_connected():
            cursor = connection.cursor()

            try:
                # delete data
                delete_query = f"delete from birthdate_keeper_tb where id = {b_id}"
                cursor.execute(delete_query)
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


def create_db():
    connection = None
    try:
        connection = mysql.connector.connect(host='localhost', user='root', password='')
        if connection.is_connected():
            cursor = connection.cursor()

            # creating database "birthdate_keeper_db"
            try:
                cursor.execute("create database birthdate_keeper_db")

                # Connecting(XAMPP) to newly created database
                connection = mysql.connector.connect(host='localhost', user='root', password='', database="birthdate_keeper_db")
                
                # Getting new cursor
                cursor = connection.cursor()
                
                # Adding table to newly created database
                cursor.execute("CREATE TABLE birthdate_keeper_tb (id INT NOT NULL AUTO_INCREMENT , name TEXT NOT NULL , birthdate TINYTEXT NOT NULL, photo_name TEXT , PRIMARY KEY (id))")
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
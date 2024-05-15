import mysql.connector


class DatabaseCode:
    def __init__(self):
        pass

    def connect_to_db(self):
        hireme_development_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Sumanark123",
            database='hireme_development',
            auth_plugin='mysql_native_password'
        )
        return hireme_development_db

from base.my_connector import DatabaseCode


class UsersDB(DatabaseCode):
    def count_of_users(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"select count(*) from users;")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def find_user_by_id(self, user_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"select * from users where id={user_id};")
        result = db_cursor.fetchone()
        db.close()
        return result

    def find_user_id_by_email(self, email):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT id FROM users WHERE  email='{email}';")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def get_value_from_db(self, user_id, column):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f" select `{column}` from users where id={user_id};")
        result = db_cursor.fetchone()[0]
        db.close()
        return result


# udb = UsersDB()
# x= udb.find_user_id_by_email('newadmin@hireme.com')
# print(x)
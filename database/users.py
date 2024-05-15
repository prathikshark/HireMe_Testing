from base.my_connector import DatabaseCode


class UsersDB(DatabaseCode):
    def count_of_users(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"select count(*) from users;")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

#
# udb = UsersDB()
# print (udb.count_of_users())

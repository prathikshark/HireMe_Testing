from base.my_connector import DatabaseCode


class WorkersDB(DatabaseCode):
    def get_value_from_worker(self, worker_id, column):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f" select `{column}` from workers where id={worker_id};")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def find_worker_id_by_user_id(self, user_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT id FROM workers WHERE  user_id='{user_id}';")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def get_from_and_to_date(self, worker_id, column):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT `{column}` FROM workers WHERE id = {worker_id};")
        result = db_cursor.fetchone()
        result = result[0].strftime('%d-%m-%Y')
        db.close()
        return result

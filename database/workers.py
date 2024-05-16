from base.my_connector import DatabaseCode


class WorkersDB(DatabaseCode):
    def get_value_from_worker(self, worker_id, column):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f" select `{column}` from workers where user_id={worker_id};")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

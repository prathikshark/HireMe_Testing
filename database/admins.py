from base.my_connector import DatabaseCode


class AdminsDB(DatabaseCode):
    def count_of_booked_services(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT count(*) FROM booked_services")
        result = db_cursor.fetchone()[0]
        db.close()
        return result
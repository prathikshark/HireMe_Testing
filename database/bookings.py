from base.my_connector import DatabaseCode


class BookingsDB(DatabaseCode):
    def count_of_bookings_for_customer(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("SELECT count(*) FROM bookings")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def check_if_booking_is_active(self, booking_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"select booked from bookings where id={booking_id}")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

#
# udb = BookingsDB()
# print(udb.check_if_booking_is_active(25))

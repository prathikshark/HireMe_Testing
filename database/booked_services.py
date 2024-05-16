from base.my_connector import DatabaseCode


class BookedServicesDB(DatabaseCode):
    def count_of_booked_services(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT count(*) FROM booked_services")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def check_if_booking_is_active(self, booking_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"select booked from bookings where id={booking_id}")
        result = db_cursor.fetchone()[0]
        db.close()
        return bool(result)

    def check_if_rating_added(self, serviceId):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT rating FROM booked_services where id={serviceId}")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

# udb = BookedServicesDB()
# c=udb.count_of_booked_services()
# print (c)
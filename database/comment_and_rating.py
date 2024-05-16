from base.my_connector import DatabaseCode


class CommentAndRatingDB(DatabaseCode):
    def check_if_rating_added(self, serviceId):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT rating FROM booked_services where id={serviceId}")
        result = db_cursor.fetchone()[0]
        db.close()
        return result


# udb = CommentAndRatingDB()
# x = udb.check_if_rating_added(27)
# print(x)

from base.my_connector import DatabaseCode


class SkillsDB(DatabaseCode):

    def get_count_of_skills(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f" select count(*) from skills;")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

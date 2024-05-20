from base.my_connector import DatabaseCode


class WorkerSkillsDB(DatabaseCode):
    def count_of_worker_skills(self, worker_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"select count(*) from worker_skills where worker_id = {worker_id};")
        result = db_cursor.fetchone()[0]
        db.close()
        return result


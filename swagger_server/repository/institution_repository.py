sql_select = "select * from institution where status = 'A'"
sql_delete = "delete from institution where id = :institution_id"

class InstitutionRepository:

    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_institution(self):
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows

    def delete_institution(self, institution_id: int):
        with self.session_factory() as session:
            result = session.execute(sql_delete, {"institution_id": institution_id})

            session.commit()
            return result.rowcount if result is not None else 0
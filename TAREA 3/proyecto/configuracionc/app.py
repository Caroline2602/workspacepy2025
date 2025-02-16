from configuracionc.database import Database
from configuracionc.mail import Mail

class App:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = Database(db_path)
        self.mail = Mail(
            smtp_server='sandbox.smtp.mailtrap.io',
            port=2525,
            user='9a3c8223168f67',
            password='367b96da6a548b'
        )
        self.init_db()

    def init_db(self):
        self.db.initConnection()

    def getConnection(self):
        return self.db.getConnection()

    def getDatabase(self):
        return self.db



from lib.users import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:

            item = User(row["name"], row["email"], row["phone_number"], row["password"], row["id"])

            users.append(item)
        return users
    
    
    
    def create(self, user):
        self._connection.execute(
            "INSERT INTO books (name, email, phone_number, password) "
            "VALUES (%s, %s, %s, %s)", [user.name, user.email, user.phone_number, user.password]
        )
        return None
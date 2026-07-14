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
        # check whether user email, etc. already exists

        rows = self._connection.execute("SELECT email FROM users;")

        emails = [row["email"] for row in rows]

        if user.email in emails:
            raise ValueError("Email already exists. Please log-in.")
        
        self._connection.execute(
            "INSERT INTO users (name, email, phone_number, password) "
            "VALUES (%s, %s, %s, %s)", [user.name, user.email, user.phone_number, user.password]
        )
        return None
    
    def find_by_email(self, email_address):
        result = self._connection.execute('SELECT * FROM users WHERE email = %s', [email_address])[0]



        return User(result["name"], result["email"], result["phone_number"], result["password"], result["id"])
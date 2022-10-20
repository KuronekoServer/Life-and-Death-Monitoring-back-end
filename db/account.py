from aiomysql import Cursor


class Account:
    "Account database"
    def __init__(self, cursor: Cursor):
        self.cursor = cursor

    async def prepare_table(self):
        "Creates the accounts table if it doesn't exist."
        await self.cursor.execute("""CREATE TABLE IF NOT EXISTS Accounts (
            id INT PRIMARY KEY, username TEXT, token VARCHAR(255)
        );""")

    async def create_account(self, userid: int, username: str, token: str):
        "Creates an account."
        await self.cursor.execute(
            "INSERT INTO Accounts (id, username, token) VALUES (%s, %s, %s);",
            (userid, username, token)
        )
    
    async def get_user(self, userid: int):
        "Gets an account."
        await self.cursor.execute(
            "SELECT * FROM Accounts WHERE id = %s;", (userid,)
        )
        return await self.cursor.fetchone()
    
    async def get_account(self, token: str):
        "Gets an account."
        await self.cursor.execute(
            "SELECT * FROM Accounts WHERE token = %s;", (token,)
        )
        return await self.cursor.fetchone()
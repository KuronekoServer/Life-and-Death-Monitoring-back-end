from aiomysql import Cursor


class Account:
    "Account database"
    def __init__(self, cursor: Cursor):
        self.cursor = cursor

    async def prepare_table(self):
        "Creates the accounts table if it doesn't exist."
        await self.cursor.execute("""CREATE TABLE IF NOT EXISTS accounts (
            id INT PRIMARY KEY, username TEXT, token VARCHAR(255)
        );""")

    async def create_account(self, userid: int, username: str, token: str):
        "Creates an account."
        await self.cursor.execute(
            "INSERT INTO accounts (id, username, token) VALUES (%s, %s, %s);",
            (userid, username, token)
        )
    
    async def get_user(self, userid: int):
        "Gets an account."
        await self.cursor.execute(
            "SELECT * FROM accounts WHERE id = %s;", (userid,)
        )
        return await self.cursor.fetchone()
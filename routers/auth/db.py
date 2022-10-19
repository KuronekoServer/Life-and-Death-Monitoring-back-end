from aiomysql import Pool


class Account:
    "Account database"
    def __init__(self, pool: Pool):
        self.pool = pool

    async def prepare_table(self):
        "Creates the accounts table if it doesn't exist."
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("CREATE TABLE IF NOT EXISTS accounts (id INT PRIMARY KEY, username TEXT, token VARCHAR(255))")

    async def create_account(self, userid: int, username: str, token: str):
        "Creates an account."
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("INSERT INTO accounts (id, username, token) VALUES (%s, %s, %s)", (userid, username, token))
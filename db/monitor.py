from aiomysql import Cursor


class Monitor:
    def __init__(self, cursor: Cursor):
        self.cursor = cursor

    async def get_all(self):
        await self.cursor.execute('SELECT * FROM Monitor')
        return await self.cursor.fetchall()

    async def prepare_table(self):
        await self.cursor.execute("""CREATE TABLE IF NOT EXISTS Monitor (
            type INT, name TEXT, value TEXT, author_id INT,
            id INT PRIMARY KEY AUTO_INCREMENT
        );""")
        await self.cursor.execute("""CREATE TABLE IF NOT EXISTS MonitorHttpLog (
            monitor_id INT, status_code INT, timestamp TIMESTAMP
        );""")
    
    async def get(self, id):
        await self.cursor.execute('SELECT * FROM Monitor WHERE id=%s', (id,))
        return await self.cursor.fetchone()

    async def http_log(self, monitor_id, status_code):
        await self.cursor.execute(
            'INSERT INTO MonitorHttpLog VALUES (%s, %s, NOW())',
            (monitor_id, status_code)
        )
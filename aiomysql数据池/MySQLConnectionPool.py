import asyncio
import aiomysql


class MySqlConnectionPool:
    def __init__(self, max_connections, loop, host: str, port: int, user: str, password: str, db: str):
        self.max_connections = max_connections
        self.connection = asyncio.Queue(max_connections)
        self.loop = loop
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    async def _create_connection(self):
        # 创建新的数据库连接
        return await aiomysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            loop=self.loop,

        )
    
    async def acquire(self):
        # 获取连接
        if self.connection.qsize() < self.max_connections:
            connection = await self._create_connection()
            await self.connection.put(connection)
        return await self.connection.get()
    
    async def release(self, connection):
        # 释放连接
        await self.connection.put(connection)




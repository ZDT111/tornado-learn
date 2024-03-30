import asyncio
import aiomysql

class AsyncConnectionPool:
    def __init__(self, max_connections, loop, **kwargs):
        self.max_connections = max_connections
        self.connections = asyncio.Queue(max_connections)
        self.loop = loop
        self.kwargs = kwargs

    async def _create_connection(self):
        # 创建新的数据库连接
        return await aiomysql.connect(loop=self.loop, **self.kwargs)

    async def acquire(self):
        # 获取连接
        if self.connections.qsize() < self.max_connections:
            connection = await self._create_connection()
            await self.connections.put(connection)
        return await self.connections.get()

    async def release(self, connection):
        # 释放连接
        await self.connections.put(connection)

# 示例用法
async def example_usage():
    loop = asyncio.get_event_loop()

    async_pool = AsyncConnectionPool(
        max_connections=10,
        loop=loop,
        user='root',
        password='',
        host='localhost',
        port=3306,
        db='ai_exercise'
    )
    
    # 连接数据库
    conn = await async_pool.acquire()
    try:
        cursor = await conn.cursor()
        await cursor.execute("select * from Class;")
        data = await cursor.fetchall()
        print(data)
    finally:
        await async_pool.release(conn)

loop = asyncio.get_event_loop()
loop.run_until_complete(example_usage())
# 示例用法
import asyncio

from State import CURSOR


async def example_usage(sql):
    # 连接数据库
    conn = await CURSOR.acquire()
    try:
        cursor = await conn.cursor()
        await cursor.execute(sql)
        data = await cursor.fetchall()
        print(data)
    finally:
        await CURSOR.release(conn)


loop = asyncio.get_event_loop()
sql = "select * from Class;"
loop.run_until_complete(example_usage(sql))



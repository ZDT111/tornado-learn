import asyncio
from MySQLConnectionPool import MySqlConnectionPool
from contextlib import asynccontextmanager

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DATABASE = 'ai_exercise'

# 获取当前的 Tornado 事件循环
loop = asyncio.get_event_loop()

CURSOR = MySqlConnectionPool(
    5, loop, MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
)
'''mysql 连接'''




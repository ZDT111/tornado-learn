import sqlite3
from queue import Queue
from threading import Lock
from contextlib import contextmanager

class ConnectionPool:
    # 初始化一些参数
    
    def __init__(self, max_connections, min_idle_connections, connection_timeout, max_idle_time):
        '''
        - max_connections      最大连接数
        - min_idle_connections 最小空闲连接数
        - connection_timeout   连接超时时间
        - max_idle_time        最大连接空闲时间
        '''
        self.max_connections = max_connections
        self.connections = Queue(max_connections)
        self.lock = Lock()

    # 与数据库创建连接
    def _create_connection(self):
        return sqlite3.connect('ai_exercise')
    
    # 使用数据库
    def get_connection(self):
        with self.lock:
            if self.connections.qsize() < self.max_connections:
                connection = self._create_connection()
                self.connections.put(connection)
            return self.connections.get()
        
    def release_connection(self, connection):
        self.connections.put(connection)




pool = ConnectionPool(max_connections=10, min_idle_connections=5, connection_timeout=10, max_idle_time=3600)

@contextmanager
def get_connection():
    connection = pool.get_connection()
    try:
        yield connection
    finally:
        pool.release_connection(connection)
    
def execute_query(query):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    return result
    
    



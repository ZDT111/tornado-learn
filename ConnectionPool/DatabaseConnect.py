class ConnectionPool:
    def get_connection(self):
        with self.lock:
            if self.connections.qsize() < self.max_connections:
                connection = self._create_connection()
                self.connections.put((connection, time.time()))
            return self.connections.get()

    def release_connection(self, connection):
        self.connections.put((connection, time.time()))

    def _cleanup_connections(self):
        while not self.connections.empty():
            connection, last_used_time = self.connections.get()
            if time.time() - last_used_time > self.max_idle_time:
                connection.close()
            else:
                self.connections.put((connection, last_used_time))






   
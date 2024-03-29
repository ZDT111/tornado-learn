from tornado import web, ioloop


class IndexHandler(web.RequestHandler):
    async def get(self):
        self.write("hello")


class IndexHandler2(web.RequestHandler):
    async def get(self):
        self.write("Hello")


class UserHandler(web.RequestHandler):
    async def get(self, id):
        self.write(f"Hello:{id}")


class UserNameHandler(web.RequestHandler):
    async def get(self, name):
        self.write(f"hello {name}")


if __name__ == '__main__':
    app = web.Application([
        ("/", IndexHandler),
        # 自动填充‘/’
        ("/index/?", IndexHandler2),
        # 匹配传递字符串
        ("/user/(\w+)/?", UserNameHandler),
        # 匹配传递数字字符
        ("/user/(\d+)/?", UserHandler),
    ], debug=True)
    app.listen(9999)
    ioloop.IOLoop.current().start()

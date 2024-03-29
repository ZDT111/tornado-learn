from tornado import web, ioloop
from tornado.options import define, options, parse_command_line, parse_config_file

# 定义key来接受传递进来的参数

parse_config_file('server.conf')


class IndexHandler(web.RequestHandler):
    async def get(self):
        self.write("hello")


if __name__ == '__main__':
    app = web.Application([
        ("/", IndexHandler),
    ], debug=True)
    app.listen(options.port)
    ioloop.IOLoop.current().start()

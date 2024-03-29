from tornado import web
from tornado import ioloop
from time import sleep


class IndexHandler(web.RequestHandler):
    def get(self):
        self.write("hello11111")


if __name__ == '__main__':
    app = web.Application([
        ("/", IndexHandler),
    ], debug=True)
    app.listen(9999)
    ioloop.IOLoop.current().start()

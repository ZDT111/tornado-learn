from tornado import web
from tornado import ioloop


class IndexHandler(web.RequestHandler):
    def get(self):
        


if __name__ == '__main__':
    app = web.Application([
        ("/", IndexHandler),

    ], debug=True)
    app.listen(9999)
    # 开启事件循环
    ioloop.IOLoop.current().start()


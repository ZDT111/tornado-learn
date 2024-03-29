from tornado import web
from tornado import ioloop


class IndexHandler(web.RequestHandler):
    # 初始化参数（不要添加异步）
    def initialize(self, db=None):
        # 初始化handler参数
        self.db = db

    # 请求来后立即运行
    # 访问前运行
    def prepare(self):
        # 打开一些文件，打印日志
        pass

    # 访问结束后运行
    def on_finish(self):
        # 清理内存
        pass

    async def get(self):
        name = self.get_argument("q")
        names = self.get_arguments("q")

        # 获取单个参数的值
        name = self.get_query_argument('q')
        # 获取多个参数的值
        names = self.get_query_arguments('q')
        print(name)
        print(names)
        pass

    async def post(self):

        name = self.get_argument("q")
        names = self.get_arguments("q")

        name = self.get_body_argument("q")
        names = self.get_body_arguments("q")

        name = self.request.body.decode('utf-8')

        print(name)
        print(names)
        pass



if __name__ == '__main__':
    app = web.Application([
        ("/", IndexHandler),

    ], debug=True)
    app.listen(9999)
    # 开启事件循环
    ioloop.IOLoop.current().start()

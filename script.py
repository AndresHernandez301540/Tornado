import time
import tornado.web
from tornado.ioloop import IOLoop
from tornado import gen


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        self.write("Yendo a dormir...")

        yield gen.Task(IOLoop.instance().add_timeout, time.time() + 1)
        self.write("Estoy despierto!")
        self.finish()


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

# Andres Ivan Hernandez Zamora
# Aaron Jafed Martinez Sarmiento
# Raul Issack Ramirez Gonzalez

# http_0.py
from tornado.ioloop import IOLoop
from tornado import gen, web
import queue

class ExampleHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('template/test.html', subject='Test')
    #@gen.coroutine
    # def get(self):
    #     delay = self.get_argument('delay', 5)
    #     yield gen.sleep(int(delay))
    #     self.write({"status": 1, "msg": "success"})
    #     self.finish()
    @gen.coroutine
    def post( self ):
        pass
class OtherHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        delay = self.get_argument('delay', 5)
        yield gen.sleep(int(delay))
        self.write({"status": 1, "msg": "success"})
        self.finish()
    @gen.coroutine
    def post( self ):
        pass

application = web.Application([(r"/example", ExampleHandler),( r"/other", OtherHandler ),], autoreload = True )
application.listen(8765)
IOLoop.current().start()

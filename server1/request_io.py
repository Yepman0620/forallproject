#coding=utf-8


from tornado.web import RequestHandler
from tornado import gen
from tornado.web import stream_request_body
import time
import random


@stream_request_body
class A(RequestHandler):
    def initialize(self):
        self.fp = open('xxxx.tmp','wb')
        self.size = 0
        self.id = random.randint(0,100)

    @gen.coroutine
    def post(self):
        self.set_header('Content-Type', 'application/json;charset=utf-8')
        self.finish('{"msg":"ok"}')
        yield gen.sleep(0)
        self.fp.close()

    @gen.coroutine
    def data_received(self, chunk):
        self.size += len(chunk)
        print(time.time(), self.id, self.size)
        self.fp.write(chunk)
        yield gen.sleep(0)
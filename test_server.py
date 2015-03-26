#!/usr/bin/env python
# coding: utf-8

import tprofile

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.log import app_log
from tornado.options import define, options


define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="debug", type=bool)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        import pdb; pdb.set_trace()
        self.write("Hello, world")


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], debug=options.debug)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    app_log.info("Listen on %d", options.port)
    app_log.info("Debug %s", options.debug)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

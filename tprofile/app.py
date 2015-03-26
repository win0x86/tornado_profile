# coding: utf-8

import sys
import tornado.web


def profile(func):
    def wrap(application, request):
        print "profile start", application, request
        ret = func(application, request)
        print "profile end."
        return ret

    return wrap


class ProfileApp(tornado.web.Application):
    @profile
    def __call__(self, http_request):
        return super(ProfileApp, self).__call__(http_request)


tornado.web.Application = ProfileApp

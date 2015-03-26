# coding: utf-8


from app import profile



class A(object):
    @profile
    def hello(self, name):
        print "hello func", name
        return name


def test_a():
    A().hello("http_request")



if __name__ == "__main__":
    test_a()

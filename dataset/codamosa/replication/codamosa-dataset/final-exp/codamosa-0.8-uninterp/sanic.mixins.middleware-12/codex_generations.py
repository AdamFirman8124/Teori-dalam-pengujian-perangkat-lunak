

# Generated at 2022-06-14 07:40:16.901946
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json
    from sanic.exceptions import SanicException
    from sanic.models.exceptions import add_status_code
    from sanic.models.http import Request, HTTPResponse
    from sanic.models.websocket import WebsocketConnection, WebSocketProtocol

    class SanicException2(SanicException):
        pass

    class SanicException3(SanicException):
        pass

    sanic_app = Sanic('test_sanic_server')
    add_status_code(SanicException2, 503)
    add_status_code(SanicException3, 504)

    def middleware1(request: Request):
        return True

    def middleware2(request: Request):
        return True


# Generated at 2022-06-14 07:40:25.241636
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._middleware_applied = False

        def _apply_middleware(self, middleware: FutureMiddleware):
            self._middleware_applied = True

    test_app = TestMiddlewareMixin()
    test_app.middleware(lambda request: None)
    assert test_app._future_middleware[0].middleware.__name__ == "<lambda>"
    assert test_app._future_middleware[0].attach_to == "request"
    assert test_app._middleware_applied

# Generated at 2022-06-14 07:40:38.272054
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.exceptions import SanicException

    app = Sanic()

    # Middleware which does not return a response
    @app.middleware
    def simple_middleware(request: Request):
        pass

    # Middleware which modifies the request
    @app.middleware
    def changed_request_middleware(request: Request):
        request.args["changed"] = "changed"

    # Middleware which returns a response
    @app.middleware
    def changed_response_middleware(request: Request):
        return request.url

    # Middleware which raises an exception
    @app.middleware
    def exception_middleware(request: Request):
        raise SanicException("Error", status_code=500)

    # Test the simple middleware


# Generated at 2022-06-14 07:40:52.578994
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.response import json

    # Testing decorator
    app = Sanic(__name__)
    @app.on_response
    async def do_stuff(request, response):
        response.body = "OK"

    request, response = app.test_client.get("/")

    assert response.status == 200
    assert response.body == b"OK"

    app = Sanic(__name__)

    # Testing partial
    partial_stuff = app.on_response()
    @partial_stuff
    async def do_stuff(request, response):
        response.body = "OK"

    request, response = app.test_client.get("/")

    assert response.status == 200
    assert response.body == b"OK"


# Generated at 2022-06-14 07:40:54.161723
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    pass


# Generated at 2022-06-14 07:40:56.561404
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    request = {}
    response = {}
    MiddlewareMixin._apply_middleware(request, response)


# Generated at 2022-06-14 07:41:00.048134
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    @MiddlewareMixin.on_response()
    def test_middleware_response(request):
        pass
    assert test_middleware_response.__name__=="test_middleware_response"

# Generated at 2022-06-14 07:41:08.022517
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class SanicExample1(MiddlewareMixin):
        async def _apply_middleware(self, middleware):
            print("The middleware is ", middleware)

    sanic_example1 = SanicExample1()

    def middleware_func(request):
        print("Apply middleware!")

    sanic_example1.middleware(middleware_func, attach_to="request")

if __name__ == "__main__":
    test_MiddlewareMixin_middleware()

# Generated at 2022-06-14 07:41:22.502018
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import pytest
    from sanic.exceptions import SanicException
    from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware
    
    # Test when calling the middleware method
    class Test:
        def __init__(self, *args, **kwargs):
            self._future_middleware = []
        def _apply_middleware(self, middleware):
            raise Exception("apply method is not overridden.")
    
    middleware = MiddlewareMixin()
    middleware._future_middleware = []
    middleware._apply_middleware = Test._apply_middleware
    assert callable(middleware.middleware)

    # Test when calling the decorator
    @middleware.middleware
    async def hello(request):
        return request
    
    print(hello)


# Generated at 2022-06-14 07:41:33.937851
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """Unit test for method middleware of class MiddlewareMixin."""

    # Arrange
    class MockMiddlewareMixin(MiddlewareMixin):

        def _apply_middleware(self, _: FutureMiddleware):
            pass

    middleware_mixin = MockMiddlewareMixin()

    # Act
    @middleware_mixin.middleware
    def mock_middleware(request):
        pass

    # Assert
    assert len(middleware_mixin._future_middleware) == 1
    assert isinstance(middleware_mixin._future_middleware[0], FutureMiddleware)
    assert middleware_mixin._future_middleware[0].middleware == mock_middleware



# Generated at 2022-06-14 07:41:45.184213
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic, response
    from sanic.request import Request
    from sanic.response import HTTPResponse

    def request_middleware(request: Request):
        return

    def request_middleware_invalid(request: Request, a, b):
        return

    def response_middleware_invalid(request: Request, a, x):
        return

    # TODO - test for this method.
    app = Sanic("test_MiddlewareMixin_on_request")

    # Test with invalid parameters
    try:
        app.on_request(request_middleware_invalid)
        assert False
    except:
        assert True

    try:
        app.on_request(response_middleware_invalid)
        assert False
    except:
        assert True

    # Test with valid parameters
   

# Generated at 2022-06-14 07:41:59.009373
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class test(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    t = test()
    m = t.middleware
    # test the return value of @app.middleware
    assert m is not None
    # test the return value of @app.middleware('request')
    assert m('request') is not None
    # test the return value of @app.middleware('response')
    assert m('response') is not None
    # test the future_middleware list
    assert t._future_middleware == []
    # test the add @app.middleware
    from sanic import Sanic
    from sanic.exceptions import ServerError
    app = Sanic("test_MiddlewareMixin_middleware")

# Generated at 2022-06-14 07:42:04.477074
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic
    app = Sanic('test')
    request, response = app.asgi()

    @app.middleware('request')
    def middleware1(request):
        _id = request.headers.get('id', None)
        return _id

    assert middleware1(request) is not None

# Generated at 2022-06-14 07:42:05.523905
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    assert 1==1


# Generated at 2022-06-14 07:42:15.236414
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.models.interface import Interface
    from sanic.models.delegates import Delegate
    from sanic.request import Request
    from sanic.response import HTTPResponse,stream,text
    from sanic.exceptions import InvalidUsage
    import asyncio
    class Middleware(Interface):

        def apply(self, *args, **kwargs):
            pass
    class Delegate(Delegate):

        def __init__(self, *args, **kwargs):
            pass
        
        def create_mock(self):
            pass
    class Request(Request):

        def __init__(self, app, *args, **kwargs):
            pass


# Generated at 2022-06-14 07:42:25.992729
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    import inspect
    from sanic.models.middleware import MiddlewareMixin
    from sanic.models.futures import FutureMiddleware
    my_MiddlewareMixin = MiddlewareMixin()
    @my_MiddlewareMixin.on_request
    def foo():
        pass
    assert isinstance(my_MiddlewareMixin._future_middleware[0], FutureMiddleware)
    assert inspect.getargspec(my_MiddlewareMixin._future_middleware[0].middleware).args == ['request']
    assert my_MiddlewareMixin._future_middleware[0].attach_to == 'request'


# Generated at 2022-06-14 07:42:27.716509
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    assert MiddlewareMixin.on_request is not None


# Generated at 2022-06-14 07:42:30.861097
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic
    app = Sanic()
    assert app.on_request(None) is not None
    assert app.on_request(callable) is not None

# Generated at 2022-06-14 07:42:43.936671
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    '''
    on_request的作用是将middleware的attach_to字段设置成request
    其实就是把middleware注册到request流程中
    '''
    import uuid
    from sanic import Sanic
    request_middleware_id = uuid.uuid1()
    response_middleware_id = uuid.uuid1()

    app = Sanic('test_MiddlewareMixin_on_request')

    @app.on_request
    async def request_middleware1(request):
        assert(request.middleware_test_value == request_middleware_id)


# Generated at 2022-06-14 07:42:47.553069
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    mixin = MiddlewareMixin()
    assert callable(mixin.on_request())
    assert callable(mixin.on_request(middleware=lambda x: x))

# Generated at 2022-06-14 07:43:02.784489
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic.handlers import ErrorHandler, RequestParameters

    class ParamMiddleware:
        def __init__(self, request):
            pass

        def __call__(self, request):
            return request

    class ErrorMiddleware:
        def __init__(self, request, exception):
            pass

        def __call__(self, request, exception):
            pass

    # Test on_request method
    app = Sanic(__name__)
    app.middleware(ParamMiddleware, attach_to="request")
    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert isinstance(app._future_middleware[0].middleware, ParamMiddleware)


# Generated at 2022-06-14 07:43:04.151585
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    MiddlewareMixin(1)

# Generated at 2022-06-14 07:43:18.170548
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestClass(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super.__init__(*args, **kwargs)

        def _apply_middleware(self, middleware):
            pass

    # test arguments are correct
    middleware = lambda: True
    t = TestClass()
    t.middleware(middleware, "request")
    # test for apply
    t.middleware(middleware, "request", apply=False)
    # test for return
    t1 = t.middleware(middleware, "request", apply=False)
    assert middleware == t1

    # #test for partial
    t2 = TestClass()
    t2.middleware(middleware, "request")
    t2.middleware(middleware, "response")
    t2.middleware

# Generated at 2022-06-14 07:43:25.915886
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    class Midd(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    midd = Midd()
    midd.middleware(middleware_or_request=1, attach_to="request", apply=True)


# Generated at 2022-06-14 07:43:39.153596
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Set up class
    class MiddlewareTest(MiddlewareMixin):
        def __init__(self):
            super().__init__()
    
    # Test instance
    middlewareTest = MiddlewareTest()

    # Test middleware method
    test_function = lambda r: 1

    middlewareTest.middleware(test_function)
    assert middlewareTest._future_middleware[0] == FutureMiddleware(
        test_function, "request"
    )
    middlewareTest._future_middleware = []
    
    middlewareTest.middleware(test_function, "response")
    assert middlewareTest._future_middleware[0] == FutureMiddleware(
        test_function, "response"
    )
    middlewareTest._future_middleware = []
    

# Generated at 2022-06-14 07:43:49.100022
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    from sanic.response import json as sanic_json
    from sanic.sanic import Sanic
    from sanic.request import Request
    app = Sanic()

    @app.middleware('response')
    async def handler(request, response):
        response.headers["X-Served-By"] = "Sanic"

    @app.route('/')
    async def handler(request):
        return sanic_json({"served": True})

    request, response = app.test_client.get('/')
    assert request.path == '/'
    assert response.status == 200
    assert response.headers["X-Served-By"] == "Sanic"



# Generated at 2022-06-14 07:43:59.769932
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestApp(MiddlewareMixin):
        def __init__(self):
            MiddlewareMixin.__init__(self)

        def _apply_middleware(self, middleware: FutureMiddleware):
            return True

    app = TestApp()
    assert app._future_middleware == []

    # Test the decorator form
    @app.middleware
    def test_on_response_decorator_form(middleware_request):
        return middleware_request

    assert app._future_middleware[0].future_middleware == test_on_response_decorator_form
    assert app._future_middleware[0].attach_to == "request"

    # Test partial form
    @app.middleware('response')
    def test_on_response_partial_form(middleware_response):
        return middle

# Generated at 2022-06-14 07:44:07.547496
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic(__name__)
    f = app.middleware
    assert f.__name__ == "middleware"
    f = app.middleware("request")
    assert f.__name__ == "middleware"
    f = app.middleware(attach_to="request")
    assert f.__name__ == "middleware"



# Generated at 2022-06-14 07:44:09.910632
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    app = MiddlewareMixin()
    app.middleware('abc')
    len(app._future_middleware) == 1

# Generated at 2022-06-14 07:44:11.755999
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    a = MiddlewareMixin()
    # TODO
    assert True==True

# Generated at 2022-06-14 07:44:26.876189
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    from sanic import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.exceptions import RequestTimeout
    from sanic.router import Router
    from sanic.websocket import WebSocketProtocol
    from sanic.blueprints import Blueprint
    from sanic.config import Config
    from sanic.server import HttpProtocol, HttpProtocol
    from sanic.constants import HTTP_METHODS

    class TestMiddlewareMixin(MiddlewareMixin):

        def __init__(self):
            self.list_request = []
            self.list_response = []
            self.is_request = True
            self.is_response = True


# Generated at 2022-06-14 07:44:36.582515
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.exceptions import SanicException

    class Middleware:
        def __call__(self, _, __, ___):
            pass

    # Create a Sanic application
    app = Sanic()

    # Check that middleware is registered on app
    @app.middleware
    def middleware(_):
        pass

    # Check that middleware is registered on app
    @app.middleware('request')
    def middleware(_):
        pass

    # Check that middleware is registered on app
    @app.middleware(attach_to='request')
    def middleware(_):
        pass

    # Check that middleware is registered on app
    app.middleware(Middleware())

   

# Generated at 2022-06-14 07:44:49.318049
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json
    from sanic.request import Request
    from unittest.mock import MagicMock
    import mock
    import pytest
    app = Sanic()
    a = MiddlewareMixin()
    a._apply_middleware = MagicMock()
    a.middleware(app)
    a._apply_middleware.assert_called_once()
    a.middleware(app, attach_to="request")
    assert len(a._future_middleware) == 2
    assert a._future_middleware[1].attach_to == "request"
    a.middleware(app, attach_to="response")
    assert len(a._future_middleware) == 3
    assert a._future_middleware[2].attach_to == "response"
    a

# Generated at 2022-06-14 07:44:57.072131
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    sanic_app = Sanic(__name__)
    # sanic_app.middleware(middleware_or_request, attach_to="request", apply=True)
    assert sanic_app.middleware(middleware_or_request="request") == partial(sanic_app.middleware, attach_to="request")

# Generated at 2022-06-14 07:45:02.935574
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareTest(MiddlewareMixin):
        def __init__(self):
            super(MiddlewareTest, self).__init__()
        
        def _apply_middleware(self, middleware: FutureMiddleware):
            self._future_middleware.append(middleware)
    
    test = MiddlewareTest()
    @test.on_request
    def x(request):
        pass
    
    assert test._future_middleware[0] == FutureMiddleware(x, "request"),   \
        "Received: " + str(test._future_middleware[0])
    assert len(test._future_middleware) == 1,  \
        "len(_future_middleware) == " + str(len(test._future_middleware))

# Generated at 2022-06-14 07:45:07.587268
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_1(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    m1 = MiddlewareMixin_1()

    # test method middleware
    m1.middleware()



# Generated at 2022-06-14 07:45:20.574500
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixinTest(MiddlewareMixin):
        def __init__(self):
            super().__init__()
            self._result = []
        def _apply_middleware(self, middleware: FutureMiddleware):
            self._result.append(middleware)

    class TestMiddleware1:
        pass
    
    class TestMiddleware2:
        pass

    m = MiddlewareMixinTest()

    test_middleware1 = TestMiddleware1()
    test_middleware2 = TestMiddleware2()

    m.middleware(test_middleware1)
    m.middleware(test_middleware2)
    assert len(m._future_middleware) == 2
    assert m._future_middleware[0].middleware == test_middleware1
    assert m._future_middleware[0].attach

# Generated at 2022-06-14 07:45:23.285418
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert (
        "not yet implemented"
    ) == "not yet implemented"



# Generated at 2022-06-14 07:45:35.218374
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import text

    # app = Sanic('test_MiddlewareMixin_middleware')
    MiddlewareMixin.__abstractmethods__ = frozenset()
    app = MiddlewareMixin()

    @app.middleware('request')
    def before_request(request):
        return text('I am a request middleware, registering with a string')

    @app.middleware
    def before_request2(request):
        return text('I am a request middleware, registering without a string')

    @app.on_response('response')
    def after_response(request, response):
        return text('I am a response middleware, registering with a string')


# Generated at 2022-06-14 07:45:48.468884
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.futures import FutureMiddleware
    from sanic.models.core import Sanic

    class FakeRequest:
        pass

    class FakeSanic(MiddlewareMixin, Sanic):

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    fake_sanic = FakeSanic()

    @fake_sanic.middleware("request")
    def fake_middleware(request):
        """fake_middleware"""
        return request

    @fake_sanic.middleware("response")
    def fake_middleware_response(request, response):
        """fake_middleware"""
        return response

    assert len(fake_sanic._future_middleware) == 2
    future_middleware = fake_sanic._future_middleware[0]
    fake_request = Fake

# Generated at 2022-06-14 07:46:07.004440
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Foo(MiddlewareMixin):
        pass

    _foo = Foo()
    a = 0

    def test1(req):
        nonlocal a
        a += 5
        return a

    def test2(req):
        nonlocal a
        a += 10
        return a

    def test3(req):
        nonlocal a
        a += 20
        return a

    _foo.middleware(test1)
    _foo.middleware(test2, attach_to="request")
    _foo.middleware(test3, attach_to="response")
    assert _foo._future_middleware == [(test1, "request"), (test2, "request"), (test3, "response")]

    _foo.on_request(test1)
    _foo.on_request(test2)
    _foo.on_

# Generated at 2022-06-14 07:46:08.337543
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    MiddlewareMixin()


# Generated at 2022-06-14 07:46:14.277467
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app=Sanic()
    print(dir(app))
    print(dir(app.middleware))
    print(dir(MiddlewareMixin))

if __name__ == "__main__":
    test_MiddlewareMixin_middleware()

# Generated at 2022-06-14 07:46:26.653527
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Sanic:
        def __init__(self, *args, **kwargs):
            self.middlewares = {}
            self.request_middleware = []

        def register_middleware(self, middleware, attach_to):
            self.middlewares[middleware] = attach_to
            if attach_to == "request":
                self.request_middleware.append(middleware)
            self.middleware(middleware, attach_to=attach_to)

        def middleware(self, middleware_or_request, attach_to="response"):
            if callable(middleware_or_request):
                return self.register_middleware(middleware_or_request, attach_to)
            else:
                return partial(self.register_middleware, attach_to=middleware_or_request)

   

# Generated at 2022-06-14 07:46:34.258938
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddleware(MiddlewareMixin):
        pass

    @TestMiddleware.middleware
    def test_middleware():
        pass
    
    assert len(TestMiddleware._future_middleware) == 1
    assert TestMiddleware._future_middleware[0].middleware == test_middleware
    assert TestMiddleware._future_middleware[0].attach_to == "request"


# Generated at 2022-06-14 07:46:45.237834
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    @TestMiddlewareMixin.middleware
    async def my_middleware1(request):
        pass

    @TestMiddlewareMixin.middleware
    async def my_middleware2(request):
        pass

    test_middleware_mixin = TestMiddlewareMixin()

    assert len(test_middleware_mixin._future_middleware) == 2
    assert test_middleware_mixin._future_middleware[0].middleware_func == \
           my

# Generated at 2022-06-14 07:46:56.499960
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.response import json
    from sanic.testing import HttpTestClient
    from sanic import Sanic

    app = Sanic(__name__)

    @app.middleware('request')
    async def process_request(request):
        request['process_request'] = True

    @app.route('/')
    async def handler(request):
        return json(request)

    request, response = HttpTestClient(app, app.handle_request)
    _, response = request('GET', '/')
    assert response.status == 200
    assert response.raw_body.decode('utf-8') == '{"process_request": true}'

# Generated at 2022-06-14 07:46:57.857565
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:47:02.711034
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.exceptions import ServerError

    app = Sanic("test_MiddlewareMixin_middleware")

    @app.middleware
    def middleware_test(req, res):
        try:
            print("request")
        except Exception as e:
            raise ServerError("Error", status_code=500)

    assert app.middleware([]) == app._future_middleware

# Generated at 2022-06-14 07:47:11.672253
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A:
        def __init__(self):
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    a = A()
    a.middleware(middleware=None, attach_to='request', apply=True)
    a.middleware(middleware=middleware, attach_to='request', apply=True)
    a.middleware(middleware=middleware, apply=True)
    a.middleware(middleware=None, apply=True)
    a.middleware(apply=True)


# Generated at 2022-06-14 07:47:29.384286
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    test_func = lambda x, y: x + y
    app = Sanic()
    assert [i.attach_to for i in app._future_middleware] == ["request"]

    app.middleware(test_func, attach_to="response")
    assert [i.attach_to for i in app._future_middleware] == ["request", "response"]
    assert app._future_middleware[1].middleware == test_func


# Generated at 2022-06-14 07:47:30.178632
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:47:38.008057
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestListener:
        async def __call__(self, request):
            pass

    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, future_middleware):
            pass

    middleware_test_mixin = TestMiddlewareMixin()
    middleware_test_mixin.middleware(TestListener())
    middleware_test_mixin.middleware(TestListener(), 'request')
    middleware_test_mixin.middleware(TestListener(), 'response')
    middleware_test_mixin.middleware(TestListener(), apply=False)



# Generated at 2022-06-14 07:47:49.340204
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.futures import FutureMiddleware
    from sanic.models.futures import MiddlewareSchema
    from sanic.router import Param
    from sanic.router import RouteSchema
    from sanic.router import Router
    from sanic import Sanic
    from sanic.request import Request

    app = Sanic('sanic-server')
    class C(MiddlewareMixin):
        router = Router()

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    middleware_mixin = C()
    async def handle_request(request):
        assert request is not None

    @middleware_mixin.middleware
    async def example_middleware(request):
        return await handle_request(request)


# Generated at 2022-06-14 07:47:57.023935
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class fake_app:
        def __init__(self):
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    @fake_app.middleware
    async def fake_middleware(request):
        pass
    assert fake_app._future_middleware[0] == FutureMiddleware(fake_middleware, 'request')

# Generated at 2022-06-14 07:48:05.210758
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Arrange
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            pass

    middleware_mixin = TestMiddlewareMixin()

    # Act
    middleware_mixin.middleware(None)(lambda x: x)

    # Assert
    assert middleware_mixin._future_middleware[0].middleware_func is not None


# Generated at 2022-06-14 07:48:18.560859
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.exceptions import InvalidUsage
    from sanic.request import Request
    from sanic.blueprints import Blueprint
    from sanic.response import text

    class MySanic(MiddlewareMixin, Sanic):
        pass

    app = MySanic("middleware-test")

    @app.route("/")
    async def handler(request: Request) -> str:
        return text("OK")

    # decorated but not registered
    @app.on_response
    async def on_response_empty(request: Request, response: str) -> None:
        pass

    assert len(app._future_middleware) == 0

    @app.middleware
    async def on_request_empty(request: Request) -> None:
        pass


# Generated at 2022-06-14 07:48:25.014185
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super(TestMiddlewareMixin, self).__init__()
            self._future_middleware = []

    def middleware1(req):
        print('run middleware1')

    def middleware2(req):
        print('run middleware2')

    test_object = TestMiddlewareMixin()
    assert len(test_object._future_middleware) == 0

    test_object.middleware(middleware1)
    test_object.middleware(middleware2)
    assert len(test_object._future_middleware) == 2

    assert test_object._future_middleware[0].middleware == middleware1
    assert test_object._future_middleware[1].middleware == middleware2

# Unit test

# Generated at 2022-06-14 07:48:34.272750
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic, response

    app = Sanic('test_MiddlewareMixin_middleware')

    request_id = 0

    @app.middleware('request')
    async def request_middleware(request):
        nonlocal request_id
        request_id += 1

    @app.route('/')
    async def handler(request):
        return response.text('OK')

    request, response = app.test_client.get('/')

    assert request_id == 1

# Generated at 2022-06-14 07:48:39.024979
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Arrange
    @MiddlewareMixin.middleware
    async def middleware(r):
        pass

    # Act
    # Assert
    assert callable(middleware)



# Generated at 2022-06-14 07:49:07.770747
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TEST(MiddlewareMixin):

        def __init__(self):
            MiddlewareMixin.__init__(self)

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    mid_1 = lambda x: x
    mid_2 = lambda x: x
    test = TEST()

    test.middleware(mid_1)
    test.middleware(mid_2, attach_to='response')
    assert len(test._future_middleware) == 2

# Generated at 2022-06-14 07:49:16.216589
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class CustomHandler:
        pass

    custom_handler = CustomHandler()
    middleware_mixin = MiddlewareMixin()

    # MiddlewareMixin.middleware(middleware_or_request, attach_to="request", apply=True)

    # Case 1: middleware_or_request is instance object of CustomHandler
    result = middleware_mixin.middleware(custom_handler, attach_to="request", apply=True)
    assert result is custom_handler

    # Case 2: middleware_or_request is string "request"
    result = middleware_mixin.middleware("request", attach_to="request", apply=True)
    assert callable(result)
    assert result() is None


# Generated at 2022-06-14 07:49:23.626852
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.services.simply import Simply
    assert Simply._future_middleware == []
    @Simply.middleware
    def test_middel(request):
        pass
    assert Simply._future_middleware != []
    assert Simply._future_middleware[0].middleware == test_middel
    assert Simply._future_middleware[0].attach_to == "request"


# Generated at 2022-06-14 07:49:24.353541
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert 0 == 0

# Generated at 2022-06-14 07:49:32.764254
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    test_middleware = MiddlewareMixin()
    # test when no callable is passed into middleware
    assert test_middleware.middleware()

    # test when a callable is passed into middleware
    def test_callable():
        return "Test callable"

    assert test_middleware.middleware(test_callable)

    @test_middleware.middleware
    def test_callable_2():
        return "Test callable 2"

    assert test_middleware._future_middleware[0]
    assert test_middleware._future_middleware[0].middleware == test_callable

# Generated at 2022-06-14 07:49:45.825307
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class _TestMiddlewareMixin(MiddlewareMixin):
        pass

    obj = _TestMiddlewareMixin()

    # The MiddlewareMixin.middleware() returns a function
    # The following code will test if the returned is a function,
    # and it has the right properties
    func = obj.middleware()
    assert callable(func)
    assert not hasattr(func, '__self__')
    assert hasattr(func, '__call__')
    assert hasattr(func, '__get__')
    assert not hasattr(func, '__set__')
    assert hasattr(func, '__delete__')

    # Finally, do a test to make sure the function is working as expected
    # and the function has a correct properties
    func = obj.middleware('request')
    assert callable(func)
   

# Generated at 2022-06-14 07:49:50.221844
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')
    assert app.middleware == MiddlewareMixin.middleware
    assert app.on_request == MiddlewareMixin.on_request
    assert app.on_response == MiddlewareMixin.on_response
    @app.on_request()
    async def on_request(request):
        pass

# Generated at 2022-06-14 07:49:56.638347
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware
    async def middleware(request):
        pass
    assert app._future_middleware == [FutureMiddleware(middleware, "request")]

    @app.middleware('response')
    async def middleware2(request):
        pass
    assert app._future_middleware == [FutureMiddleware(middleware, "request"), FutureMiddleware(middleware2, "response")]


# Generated at 2022-06-14 07:50:06.662983
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    middleware1 = FutureMiddleware(middleware=None, attach_to="request")
    middleware2 = FutureMiddleware(middleware=None, attach_to="request")
    test = MiddlewareMixin()
    test.middleware(middleware1, attach_to="request")
    test.middleware(middleware2, attach_to="request")
    assert test._future_middleware == [middleware1, middleware2]
    test.middleware(middleware2, attach_to="request")
    assert test._future_middleware == [middleware1, middleware2, middleware2]


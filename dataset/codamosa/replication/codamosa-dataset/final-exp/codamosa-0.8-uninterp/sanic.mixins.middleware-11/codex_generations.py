

# Generated at 2022-06-14 07:40:17.926883
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class Test_MiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._future_middleware: List[FutureMiddleware] = []
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    test = Test_MiddlewareMixin()
    @test.on_request
    def on_request(request):
        pass
    assert test._future_middleware.pop().attach_to == 'request'


# Generated at 2022-06-14 07:40:26.369469
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.server import HttpProtocol
    m = MiddlewareMixin()
    assert m._future_middleware == []
    m.middleware(None, None)

    async def _my_middleware(request):
        """middleware
        """
        pass
    
    m.middleware(_my_middleware, None)
    assert m._future_middleware == [FutureMiddleware(_my_middleware, "request")]

    def _my_middleware1(request, response):
        """middleware
        """
        pass
    m.middleware(_my_middleware1, "response")
    assert m._future_middleware == [
        FutureMiddleware(_my_middleware, "request"),
        FutureMiddleware(_my_middleware1, "response")
    ]

# Generated at 2022-06-14 07:40:28.984657
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    pass


# Generated at 2022-06-14 07:40:41.124072
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestClass(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    test_object = TestClass()
    assert test_object._future_middleware == []

    @test_object.middleware('request')
    def handler1(request):
        return

    @test_object.middleware
    def handler2():
        return

    assert len(test_object._future_middleware) == 2
    assert test_object._future_middleware[0].middleware == handler1
    assert test_object._future_middleware[0].attach_to == "request"
    assert test_object._future_middleware[1].middleware == handler2
    assert test_object._future_middleware[0].attach_to == "request"


# Generated at 2022-06-14 07:40:49.863181
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from unittest.mock import Mock
    from sanic.app import Sanic
    class D:
        def __init__(self):
            self._future_middleware: List[FutureMiddleware] = []

    c = D()
    future_middleware = FutureMiddleware(Mock(), "request")
    c._apply_middleware = Mock()
    c.middleware(Mock())
    c.middleware(Mock(), "request")
    c.on_request(Mock())
    c.on_response(Mock())

# Generated at 2022-06-14 07:40:54.041168
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Arrange
    import sanic
    app = sanic.Sanic()
    # Act
    app.on_response(response="response")
    # Assert

# Generated at 2022-06-14 07:40:59.244035
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    mix = MiddlewareMixin()
    @mix.middleware('request')
    def handler(request):
        return request

    mix._apply_middleware = Mock()
    handler = mix.middleware(handler, 'request', False)
    handler()
    assert len(mix._future_middleware) == 1

# Generated at 2022-06-14 07:41:10.969581
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """
    Case 1:
    """
    # mock
    @MiddlewareMixin
    class _MockView(object):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            assert middleware._middleware == "middleware"
            assert middleware._attach_to == "request"

    obj = _MockView()
    @obj.middleware
    def middleware():
        pass

    """
    Case 2:
    """
    obj = _MockView()
    @obj.middleware('request')
    def middleware():
        pass


# Generated at 2022-06-14 07:41:12.306794
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
  
  # pass
  return



# Generated at 2022-06-14 07:41:14.794260
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    m = MiddlewareMixin()
    m.on_response()
    assert m


# Generated at 2022-06-14 07:41:21.466919
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    obj = MiddlewareMixin()
    assert isinstance(obj.on_response(middleware=None), partial)
    # noqa
    assert isinstance(obj.on_response(middleware=str), partial)
    assert not callable(obj.on_response())



# Generated at 2022-06-14 07:41:28.469675
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json
    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('request')
    async def add_host(request):
        request.host = '127.0.0.1:8000'

    @app.middleware('response')
    async def add_header(request, response):
        response.headers['Content-Type'] = 'text/html'

    @app.route('/')
    async def handler(request):
        return json({'test': True})

    request, response = app.test_client.get('/')

    # Verify 'request' middleware
    assert request.host == '127.0.0.1:8000'

    # Verify 'response' middleware

# Generated at 2022-06-14 07:41:38.059986
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.app import Sanic

    app = Sanic("test_MiddlewareMixin_on_request")
    setattr(app, "_future_middleware", [])

    def register_middleware(middleware, attach_to="request"):
        future_middleware = FutureMiddleware(middleware, attach_to)
        setattr(app, "_future_middleware", [future_middleware])

    app.on_request(register_middleware)
    assert app._future_middleware != []


# Generated at 2022-06-14 07:41:48.068148
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super(TestMiddlewareMixin, self).__init__(*args, **kwargs)
            self.responses = []

        def _apply_middleware(self, middleware):
            async def response_middleware(request, response, self=self):
                self.responses.append(response)

            return response_middleware

    test_app = TestMiddlewareMixin()
    response_middleware = test_app.on_response()
    assert test_app.responses == []
    response_middleware(None, 4)
    assert test_app.responses == [4]

# Generated at 2022-06-14 07:42:00.661410
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Sanic:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []
            
        # Test method middleware
        def middleware(
            self, middleware_or_request, attach_to="request", apply=True
        ):
            """
            Decorate and register middleware to be called before a request.
            Can either be called as *@app.middleware* or
            *@app.middleware('request')*

            `See user guide re: middleware
            <https://sanicframework.org/guide/basics/middleware.html>`__

            :param: middleware_or_request: Optional parameter to use for
                identifying which type of middleware is being registered.
            """


# Generated at 2022-06-14 07:42:09.177926
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.app import Sanic

    def before_request():
        pass

    @Sanic.middleware("request")
    def before_request1():
        pass

    def after_request():
        pass

    @Sanic.middleware("request")
    def after_request1():
        pass

    Sanic.on_request(before_request)
    Sanic.on_request(after_request1)
    Sanic.on_response(before_request1)
    Sanic.on_response(after_request)

    assert Sanic._future_middleware == []


# Generated at 2022-06-14 07:42:19.385134
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app_middleware_mixin = MiddlewareMixin()
    app_middleware_mixin.middleware(middleware_or_request=None, attach_to="request", apply=True)
    # app_middleware_mixin.middleware(middleware_or_request=None)
    # app_middleware_mixin.middleware(middleware_or_request=None)
    # app_middleware_mixin.middleware(middleware_or_request=None)
    # app_middleware_mixin.middleware(middleware_or_request=None)
    # app_middleware_mixin.middleware(middleware_or_request=None)

# def test():
#     from sanic.app import Sanic
#     app = Sanic()
#    

# Generated at 2022-06-14 07:42:22.892270
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    @MiddlewareMixin.on_response
    async def on_response(request, response):
        pass
    assert on_response.__name__ == "on_response"



# Generated at 2022-06-14 07:42:33.601316
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.server import HttpProtocol

    app = Sanic('test_MiddlewareMixin_middleware')
    # HttpProtocol is a subclass of MiddlewareMixin
    assert issubclass(HttpProtocol, MiddlewareMixin)
    # HttpProtocol is a subclass of MiddlewareMixin
    assert isinstance(app.create_protocol(None), HttpProtocol)

    @app.middleware('response')
    async def handle_response(request, response):
        print('handle_response middleware')
        return response

    request = None # type: ignore
    response = None # type: ignore
    app.create_protocol(None)._apply_middleware(app._future_middleware[0])
    assert app.create_protocol(None)._apply_

# Generated at 2022-06-14 07:42:38.049875
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class A(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
             pass

    def m(request, response):
        return "foo"

    A().on_response(m)

# Generated at 2022-06-14 07:42:46.078738
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    s = Sanic()
    assert len(s._future_middleware) == 0

    @s.middleware
    async def m(request):
        return True

    assert len(s._future_middleware) == 1

    assert s._future_middleware[0]._middleware == m
    assert s._future_middleware[0]._attach_to == "request"

# Generated at 2022-06-14 07:42:49.367597
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic

    server = Sanic('test')
    assert hasattr(server, 'on_response'), 'test has no attribute on_response'

# Generated at 2022-06-14 07:42:52.805307
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    @MiddlewareMixin.on_request()
    def some_middleware(request):
        print("I can run code before each request")
        print(request)



# Generated at 2022-06-14 07:42:53.537510
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert True

# Generated at 2022-06-14 07:42:56.466565
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert MiddlewareMixin.on_response()('middleware') == partial(MiddlewareMixin.middleware, attach_to="response")

# Generated at 2022-06-14 07:42:59.369455
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class obj(MiddlewareMixin):
        pass

    o = obj()
    o.middleware(middleware=None, attach_to="request")

# Generated at 2022-06-14 07:43:10.650562
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():

    class TestOnResponse:

        def __init__(self):
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

        def on_response(self, middleware=None):
            if callable(middleware):
                return self.middleware(middleware, "response")
            else:
                return partial(self.middleware, attach_to="response")

        def middleware(self, middleware_or_request, attach_to="request",
                       apply=True):

            def register_middleware(middleware, attach_to="request"):
                nonlocal apply

                future_middleware = FutureMiddleware(
                    middleware, attach_to)
                self._future_middleware.append(future_middleware)
                if apply:
                    self._apply

# Generated at 2022-06-14 07:43:21.861305
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    @Sanic.middleware
    async def mw(request):
        return request
    @Sanic.middleware('request')
    async def mw_request(request):
        return request
    @Sanic.middleware('response')
    async def mw_response(request, response):
        return request
    assert hasattr(mw, "_sanic_middleware") and mw._sanic_middleware == "response"
    assert hasattr(mw_request, "_sanic_middleware") and mw_request._sanic_middleware == "request"
    assert hasattr(mw_response, "_sanic_middleware") and mw_response._sanic_middleware == "response"
    app = Sanic("test_middleware")
    assert app._future_middle

# Generated at 2022-06-14 07:43:27.352495
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic

    app = Sanic("test_MiddlewareMixin_on_request")
    @app.on_request
    def before_request_on_request():
        pass

    assert len(app._before_request_funcs) == 1


# Generated at 2022-06-14 07:43:39.629096
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic.exceptions import NotFound
    from sanic.blueprints import Blueprint
    from sanic.request import RequestParameters
    from sanic.testing import HOST, PORT
    import asyncio

    app = Sanic("test_MiddlewareMixin_on_response")

    @app.exception(NotFound)
    async def ignore_404s(request, exception):
        return json({"msg": "Got a 404"})

    @app.middleware("response")
    async def print_on_response(request, response):
        print("I am a response middleware")
        return response

    @app.route("/middleware")
    async def handler(request):
        print("I am a request handler")

# Generated at 2022-06-14 07:43:44.512073
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class Zz:
        def __init__(self):
            self._future_middleware = []

    x = MiddlewareMixin()
    y = Zz()
    z = y.on_response()
    z(x)

# Generated at 2022-06-14 07:43:45.763102
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert 0

# Generated at 2022-06-14 07:43:57.997916
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware

    app = Sanic('test_MiddlewareMixin_on_response')

    @app.middleware('response')
    async def simple_middleware(request):
        pass

    @app.middleware
    async def simple_middleware2(request):
        pass

    @app.middleware('response')
    def simple_middleware3(request):
        pass

    @app.middleware
    def simple_middleware4(request):
        pass

    @app.on_response('response')
    async def simple_middleware5(request):
        pass

    @app.on_response
    async def simple_middleware6(request):
        pass


# Generated at 2022-06-14 07:44:03.614537
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    middlewareMixin = MiddlewareMixin()
    def testable_middleware(request, response):
        return response
    middleware = middlewareMixin.on_response(testable_middleware)
    assert(testable_middleware in middlewareMixin._future_middleware)
    assert(testable_middleware == middleware)

# Generated at 2022-06-14 07:44:16.120309
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MyHandler(MiddlewareMixin):
        def __init__(self):
            super(MyHandler, self).__init__()
            self._future_middleware = []
            self.futures: List[FutureMiddleware] = []
            
        def _apply_middleware(self, middleware: FutureMiddleware):
            self.futures.append(middleware)
    
    def on_request(middleware):
        def decorator(f):
            return f
        return decorator

    def on_response(middleware):
        def decorator(f):
            return f
        return decorator

    my_handler = MyHandler()
    @my_handler.middleware
    async def mw_1(request):
        return await request

# Generated at 2022-06-14 07:44:27.457163
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert callable(MiddlewareMixin.on_response(MiddlewareMixin))
    assert callable(MiddlewareMixin.on_response(MiddlewareMixin,))
    assert callable(MiddlewareMixin.on_response(MiddlewareMixin, callable))
    assert not callable(MiddlewareMixin.on_response(MiddlewareMixin, callable, callable))
    assert callable(MiddlewareMixin.on_response(MiddlewareMixin, "test string"))
    assert callable(MiddlewareMixin.on_response(MiddlewareMixin, "test string", callable))
    assert not callable(MiddlewareMixin.on_response(MiddlewareMixin, "test string", callable, callable))


# Generated at 2022-06-14 07:44:38.407486
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.futures import FutureMiddleware
    
    class MiddlewareMixinMock(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    @MiddlewareMixinMock.middleware
    def middleware_func(request):
        pass
    
    m = MiddlewareMixinMock()
    assert middleware_func.__name__ == "middleware_func"
    assert middleware_func.__doc__ == None
    
    # Check if the middleware method is a instance of FutureMiddleware
    assert isinstance(m._future_middleware[0], FutureMiddleware)
    assert m._

# Generated at 2022-06-14 07:44:47.308553
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    from sanic.response import text
    from sanic.request import Request
    # Test code

    def middleware(request: Request):
        return text("OK")

    app = Sanic(__name__)

    app.on_response(middleware)
    # Sanity check
    assert len(app._future_middleware) == 1

    future_middleware = app._future_middleware[0]
    assert future_middleware.middleware == middleware
    assert future_middleware.attach_to == "response"

# Generated at 2022-06-14 07:44:56.536889
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class MyMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            ...

    my_middleware_mixin = MyMiddlewareMixin()

    @my_middleware_mixin.on_response
    def b(request, response):
        ...

    assert my_middleware_mixin._future_middleware
    assert my_middleware_mixin._future_middleware[0].middleware == b
    assert my_middleware_mixin._future_middleware[0].attach_to is "response"


# Generated at 2022-06-14 07:45:03.062602
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.response import text
    from sanic.constants import HTTP_METHODS
    from sanic.server import HttpProtocol
    from sanic.exceptions import (
        SanicException,
        NotFound,
        InvalidUsage,
        MethodNotSupported,
        PayloadTooLarge,
        RequestTimeout,
        InvalidUsage,
        FileNotFound,
        Forbidden,
        ServerError,
        URLBuildError,
    )
    from sanic.views import HTTPMethodView

    # Sanic(debug=True)
    app = Sanic("sanic-test", debug=True)
    app.config.REQUEST_MAX_SIZE = 10_485_760
    app.config.REQUEST_TIMEOUT = 60

# Generated at 2022-06-14 07:45:16.541655
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._future_middleware = None

    t = TestMiddlewareMixin()

    assert t.middleware is MiddlewareMixin.middleware
    assert t.on_request is MiddlewareMixin.on_request
    assert t.on_response is MiddlewareMixin.on_response

# Generated at 2022-06-14 07:45:25.017242
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text

    app = Sanic()

    @app.middleware
    async def test_middleware(request):
        return text('Middleware was applied')

    request, response = app.test_client.get('/')
    assert response.status == 200
    assert response.text == 'Middleware was applied'


# Unit test on_request method of class MiddlewareMixin

# Generated at 2022-06-14 07:45:33.615523
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Test case 1
    from sanic import Sanic
    @Sanic.middleware
    async def add_logs(request):
        pass
    # Test case 2
    @Sanic.on_response
    def add_logs(request):
        pass

    # Test case 3
    @Sanic.middleware('request')
    def add_logs(request):
        pass

    # Test case 4
    @Sanic.middleware('response')
    def add_logs(request):
        pass

# Generated at 2022-06-14 07:45:37.362811
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin1(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    MiddlewareMixin1()

# Generated at 2022-06-14 07:45:50.889158
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    class CustomSanic(Sanic, MiddlewareMixin):
        pass

    app = CustomSanic(__name__)
    assert isinstance(app, CustomSanic)
    assert isinstance(app, Sanic)

    assert len(app._future_middleware) == 0
    @app.middleware("request")
    async def a_middleware(request):
        pass
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].attach_to == "request"
    assert app._future_middleware[0].middleware is a_middleware
    @app.middleware("response")
    async def b_middleware(request, response):
        pass
    assert len(app._future_middleware) == 2
    assert app._future_

# Generated at 2022-06-14 07:46:04.340958
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    def say_hi(request):
        return text("Hi")

    @MiddlewareMixin.middleware
    async def say_hello_middleware(request):
        return text("Hello")

    @MiddlewareMixin.middleware("response")
    async def say_goodbye_middleware(request, response):
        return text("Goodbye")

    @MiddlewareMixin.on_request
    async def say_hi_middleware(request):
        return text("Hi")

    @MiddlewareMixin.on_response
    async def say_bye_middleware(request, response):
        return text("Bye")

    assert isinstance(say_hello_middleware, partial)
    assert say_hello_middleware.func == MiddlewareMixin.middleware

# Generated at 2022-06-14 07:46:15.061859
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.exceptions import RequestTimeout
    from sanic.request import Request
    from sanic.response import HTTPResponse
    import asyncio
    app = Sanic()

    # A middleware that raises a RequestTimeout exception.
    # This exception is then caught by the Sanic server.
    # If the middleware function is not defined correctly
    # Sanic server will raise a TypeError instead of the
    # expected exception.
    @app.middleware('request')
    async def raise_RequestTimeout(request):
        raise RequestTimeout("Manually raised Request Timeout")

    @app.route('/')
    async def test_request_pad_result(request):
        return HTTPResponse("Hello World")

    request, response = app.test_client.get('/')


# Generated at 2022-06-14 07:46:29.061521
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse

    @sanic.middleware('response')
    async def before_request(request):
        pass

    # 应用在response中的middleware
    # Ensure that the middleware is registered as a response middleware
    assert before_request in sanic._middleware['response']


    # 应用在request中的middleware
    # Ensure that the middleware is registered as a request middleware
    async def before_request(request):
        pass

    @sanic.middleware('request')
    async def before_request(request):
        pass

    assert before_request in sanic._middleware['request']


    # 没有显式声明middleware

# Generated at 2022-06-14 07:46:42.430469
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from unittest.mock import Mock

    class FakeMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super().__init__()
            self._apply_middleware = Mock()

    fake_mid = FakeMiddlewareMixin()
    fake_dis = lambda: None

    fake_mid.middleware(fake_dis, "request", True)
    fake_mid.on_request(fake_dis)
    fake_mid.on_response(fake_dis)

    assert len(fake_mid._future_middleware) == 3
    assert fake_mid._future_middleware[0].middleware == fake_dis
    assert fake_mid._future_middleware[0].attach_to == "request"
    assert fake_mid._future_middleware[1].middleware == fake_dis

# Generated at 2022-06-14 07:46:50.366494
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.middleware import FutureMiddleware
    from sanic.models.middleware import Middleware

    app = Sanic("test_app")
    future_middleware = Middleware(lambda x: x)
    future_middleware.attach_to = "response"

    # Test register middleware to class
    app.middleware(future_middleware, attach_to="request")

    # Test register middleware to class with apply parameter
    app.middleware(future_middleware, apply=False)

    # Test register middleware by decorator
    @app.middleware("request")
    def future_middleware_one(request):
        return request

    # Test register middleware by decorator with no args

# Generated at 2022-06-14 07:47:06.875524
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MixinClass(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(MixinClass, self).__init__()
            # Set some default value
            self.middleware_register_order = 0
            self.middleware_func_order = 0

        def _apply_middleware(self, middleware: FutureMiddleware):
            self.middleware_register_order += 1
            middleware.registered_func(self.middleware_register_order)

    mixin_test = MixinClass()
    _middleware_func = mixin_test.middleware(
        lambda request: ("test_MiddlewareMixin_middleware", request))
    assert isinstance(_middleware_func, partial)

    assert len(mixin_test._future_middleware) == 1


# Generated at 2022-06-14 07:47:12.974830
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic()
    assert len(app._future_middleware) == 0
    app.middleware(lambda x: x, attach_to='request')
    assert len(app._future_middleware) == 1
    app.middleware(lambda x: x, attach_to='response')
    assert len(app._future_middleware) == 2


# Generated at 2022-06-14 07:47:18.614693
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')

    async def m1(request, *args, **kwargs):
        return await  m2(request, *args, **kwargs)

    async def m2(request, *args, **kwargs):
        return 'test_MiddlewareMixin_middleware'

    @app.middleware(apply=True)
    async def m3(request):
        return await m1(request)

    @app.middleware
    async def m4(request):
        return await m3(request)

    request, response = app.test_client.get('/')

    assert response.text == 'test_MiddlewareMixin_middleware'

# Generated at 2022-06-14 07:47:26.314108
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models.futures import FutureMiddleware

    app = Sanic()
    # mock the _apply_middleware method
    def _apply_middleware(self, middleware: FutureMiddleware):
        assert middleware.middleware == middleware
        assert middleware.attach_to == "request"

    app._apply_middleware = _apply_middleware
    func = lambda request: None
    app.middleware(func)

# Generated at 2022-06-14 07:47:34.873608
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MyClass(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            print(middleware)
            return None

    mc = MyClass()
    mc.middleware(lambda: 'a')
    mc.middleware(lambda: 'b', 'request')
    mc.middleware(lambda: 'c', 'response')
    assert mc._future_middleware == [
        FutureMiddleware(lambda: 'a', 'request'),
        FutureMiddleware(lambda: 'b', 'request'),
        FutureMiddleware(lambda: 'c', 'response'),
    ]

# Generated at 2022-06-14 07:47:38.166899
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Initialize
    args = ()
    kwargs = {}
    obj = MiddlewareMixin(*args, **kwargs)

    # Check
    assert obj

# Generated at 2022-06-14 07:47:47.445289
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    from sanic.models.middleware import middleware

    app = Sanic()

    assert not hasattr(app, "_future_middleware")

    @app.middleware
    def a_middleware(request):
        pass

    assert isinstance(app._future_middleware[0].middleware, a_middleware)

    @app.middleware
    def another_middleware(request):
        pass

    assert (
        isinstance(app._future_middleware[1].middleware, another_middleware)
    )


# Generated at 2022-06-14 07:47:55.149822
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class _Sanic(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.middleware_type = None

        def _apply_middleware(self, middleware):
            self.middleware_type = middleware.type

    app = _Sanic()
    middleware_type = 'request'

    @app.middleware
    async def test_middleware(request):
        return

    @app.middleware(middleware_type)
    async def test_middleware2(request):
        return

    assert app.args == ()
    assert app.kwargs == {}
    assert app.middleware_type == middleware_type
    assert hasattr(app, '_future_middleware')


# Unit test

# Generated at 2022-06-14 07:48:06.678803
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_test:
        def __init__(self):
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa

    test_obj = MiddlewareMixin_test()
    test_obj_mix = MiddlewareMixin()

    @test_obj.middleware
    def middleware_test(request):
        pass
    assert isinstance(middleware_test, FutureMiddleware)
    assert isinstance(middleware_test.middleware, partial)

    @test_obj.middleware(attach_to="response")
    def middleware_test(request):
        pass
    assert isinstance(middleware_test, FutureMiddleware)

# Generated at 2022-06-14 07:48:15.193335
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware(): 
    from sanic import Sanic
    app = Sanic(__name__)
    app.config.KEEP_ALIVE = False


    @app.middleware('request')
    async def request_middleware(request):
        pass


    assert len(app._future_middleware) == 1
    assert callable(app._future_middleware[0].middleware)
    assert app._future_middleware[0].attach_to == 'request'


# Generated at 2022-06-14 07:48:39.323982
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
  from sanic import Sanic
  from sanic.response import json

  # 1. test no parameter
  @app.middleware
  def sample_middleware(request):
      return request

  @app.route('/')
  def _(request):
      return json({'msg': 'success'})

  # 2. test 1 parameter
  @app.middleware('request')
  def sample_middleware(request):
      return request

  @app.route('/')
  def _(request):
      return json({'msg': 'success'})

  # 3. test 2 parameters
  @app.middleware(attach_to='request')
  def sample_middleware(request):
      return request

  @app.route('/')
  def _(request):
      return json({'msg': 'success'})




# Generated at 2022-06-14 07:48:53.349355
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    tmm = TestMiddlewareMixin("test")
    assert len(tmm._future_middleware) == 0
    tmm_middleware = tmm.middleware
    tmm_middleware(lambda x: x)
    assert len(tmm._future_middleware) == 1
    assert len(tmm._future_middleware[0].middleware_handlers) == 1

# Generated at 2022-06-14 07:49:00.159465
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestC(MiddlewareMixin):
        def __init__(self):
            self._future_middleware = []
            self._apply_middleware = None

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    
    middleware = TestC()
    @middleware.middleware
    def test_middleware(request):
        pass
    assert len(middleware._future_middleware) != 0


# Generated at 2022-06-14 07:49:12.404064
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Test no middleware
    a = MiddlewareMixin()
    assert len(a._future_middleware) == 0

    # Test add one middleware
    fm1 = FutureMiddleware(lambda x: x, "request")
    a.middleware(fm1, apply=False)
    assert len(a._future_middleware) == 1 and a._future_middleware[0] == fm1

    # Test add two middlewares
    fm2 = FutureMiddleware(lambda x: x, "response")
    a.middleware(fm2, apply=False)
    assert len(a._future_middleware) == 2 \
           and a._future_middleware[0] == fm1 \
           and a._future_middleware[1] == fm2

    # Test if middleware is duplicated
    a

# Generated at 2022-06-14 07:49:15.080285
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixinObject(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    obj = MiddlewareMixinObject()

    obj.middleware()

# Generated at 2022-06-14 07:49:25.893617
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class testMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa

    testObj = testMiddlewareMixin()

    @testObj.middleware
    async def testMiddleware(request):
        pass

    # Expected result: The length of list _future_middleware is 1
    assert len(testObj._future_middleware) == 1
    assert testObj._future_middleware[0].middleware == testMiddleware
    assert testObj._future_middleware[0].attach_to == "request"


# Generated at 2022-06-14 07:49:35.081333
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Application(MiddlewareMixin):
        def __init__(self):
            super().__init__()
            self._middleware = []
        
        def _apply_middleware(self, middleware):
            self._middleware.append(middleware)
    
    def on_response(request, handler):
        return handler
    
    app = Application()
    
    app.middleware(on_response)
    assert len(app._middleware) == 1
    assert type(app._middleware[0]) == FutureMiddleware
    assert app._middleware[0].middleware == on_response
    assert app._middleware[0].attach_to == "request"

    app.middleware(on_response, "response")
    assert len(app._middleware) == 2
    assert app._middleware[1].attach_

# Generated at 2022-06-14 07:49:39.481479
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixinTest:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

    assert MiddlewareMixinTest

# Generated at 2022-06-14 07:49:49.939486
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.futures.middleware import FutureMiddleware
    from sanic.models.futures.middleware import FutureMiddlewareList

    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(TestMiddlewareMixin, self).__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware) -> None:
            return None

    test_middleware_mixin = TestMiddlewareMixin()

    def test_func():
        return

    def test_func2():
        return

    @test_middleware_mixin.on_response()
    def test_func_on_response():
        return


# Generated at 2022-06-14 07:49:56.513176
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Given
    class Server(MiddlewareMixin):
        pass

    s = Server()

    @s.middleware
    async def handler(request):
        return 'request'

    # When
    s._apply_middleware = lambda x: x
    handler = s.middleware(handler)

    # Then
    assert len(s._future_middleware) == 1
    assert s._future_middleware[0].future == handler
    assert s._future_middleware[0].attach_to == 'request'


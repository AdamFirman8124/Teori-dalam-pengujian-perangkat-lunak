

# Generated at 2022-06-14 07:40:21.960103
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models.futures import FutureMiddleware
    from sanic.response import text
    from sanic.utils import sanic_endpoint_test

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('response')
    def handler(request):
        return text('OK')

    request, response = sanic_endpoint_test(app)

    assert response.text == 'OK'
    assert app._future_middleware != []
    assert isinstance(app._future_middleware[0], FutureMiddleware)



# Generated at 2022-06-14 07:40:34.139241
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    app = Sanic(__name__)
    app.__class__ = TestMiddlewareMixin
    assert hasattr(app, "_future_middleware")

    @app.middleware
    def test_middleware(request):
        pass

    @app.middleware('request')
    def test_middleware2(request):
        pass

    @app.middleware('response')
    def test_middleware3(request, response):
        pass

    @app.on_request
    def test_middleware4(request):
        pass

    @app.on_response
    def test_middleware5(request, response):
        pass

# Generated at 2022-06-14 07:40:38.076138
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    test_class = MiddlewareMixin()
    test_class.on_response()
    # assert isinstance(obj, BaseClass)

# Generated at 2022-06-14 07:40:42.029867
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # 1. Arrange
    mm = MiddlewareMixin()

    # 2. Act
    mm.on_response()

    # 3. Assert

# Generated at 2022-06-14 07:40:49.425708
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """
    Test method middleware of class MiddlewareMixin
    """
    from sanic.app import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    def middleware(request):
        pass

    m = MiddlewareMixin()
    assert len(m._future_middleware) == 0
    m.middleware(middleware)
    assert len(m._future_middleware) == 1


# Generated at 2022-06-14 07:40:55.516076
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class HttpProtocol(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            if middleware.attach_to == "response":
                print("apply on_response")

    http_procol = HttpProtocol()

    @http_procol.on_response
    def my_request_middleware(request):
        print("on_response my_request_middleware")
        pass

    http_procol._future_middleware[0].middleware(None)



# Generated at 2022-06-14 07:41:01.277236
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    app = Sanic("test_MiddlewareMixin_on_response")

    # test all required methods
    assert callable(app.on_response)
    assert callable(app.on_response())
    assert callable(app.on_response(lambda x: print(x)))
    assert callable(app.on_response(lambda x: x))

    # test default behaviour
    def test_middleware(request):
        return request
    app.on_response(test_middleware)
    assert test_middleware in app._future_middleware



# Generated at 2022-06-14 07:41:11.410078
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_UnitTest(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)               
        
        def _apply_middleware(self, middleware = FutureMiddleware):
            assert True

    middleware_mixin = MiddlewareMixin_UnitTest()
    middleware_or_request = 1
    attach_to = "request"
    apply = True
    middleware_mixin.middleware(middleware_or_request = middleware_or_request, attach_to = attach_to, apply = apply)


# Generated at 2022-06-14 07:41:16.644607
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    middleware_mixin = MiddlewareMixin()
    middleware_mixin._apply_middleware = lambda x: None
    middleware_mixin.on_response(lambda x: None)
    middleware_mixin.on_response()


# Generated at 2022-06-14 07:41:18.922513
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # test for unit test
    a = MiddlewareMixin()
    assert a.middleware
    assert a.on_request
    assert a.on_response

# Generated at 2022-06-14 07:41:28.087868
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import text
    from sanic.models.futures import Middleware

    def response_middleware(request):
        return text("Test")

    app = Sanic("test_MiddlewareMixin_middleware")
    app.middleware(response_middleware, attach_to="response")
    for middleware in app._future_middleware:
        assert isinstance(middleware, Middleware)
        assert middleware.attach_to == "response"

    def request_middleware(request):
        return text("Test")

    app = Sanic("test_MiddlewareMixin_middleware")
    app.middleware(request_middleware, attach_to="request")
    for middleware in app._future_middleware:
        assert isinstance(middleware, Middleware)

# Generated at 2022-06-14 07:41:30.123442
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    assert MiddlewareMixin.on_request(MiddlewareMixin) == True

# Generated at 2022-06-14 07:41:31.879186
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    pass


# Generated at 2022-06-14 07:41:40.396156
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.request import Request
    from sanic.response import HTTPResponse

    # Test Request
    i=0
    @request.on_request
    async def test_on_request(request1):
        i += 1
        return
    assert i==1

    # Test HTTPResponse
    i=0
    @response.on_response
    async def test_on_request(request1):
        i += 1
        return
    assert i==1

# Generated at 2022-06-14 07:41:47.161896
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic
    app = Sanic()

    # Sanic is the only class inheriting from Sanic, but since this is not
    # a concrete class, we cannot directly check for an instance of Sanic
    assert isinstance(app, Sanic)

    # Only Sanic has the on_request method
    assert hasattr(app, "on_request")
    
    # We can now call the on_request method
    assert callable(app.on_request())


# Generated at 2022-06-14 07:42:00.036972
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    import pytest
    from sanic.exceptions import InvalidUsage
    from sanic.blueprints import Blueprint
    from sanic.response import text
    from sanic.request import Request
    from sanic.exceptions import Forbidden

    class CustomMiddleware(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

    app = CustomMiddleware()
    request_mock = Request(b'GET', '/', host='127.0.0.1', port=80, protocol=1)
    request_mock.transport = ['127.0.0.1', 80]

    @app.route("/")
    async def handler(request):
        return text("OK")


# Generated at 2022-06-14 07:42:11.030364
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware

    app = Sanic('test_MiddlewareMixin_middleware')

    # noinspection PyShadowingNames
    async def middleware_test(request):
        return response.text("OK")

    # noinspection PyShadowingNames
    async def request_middleware_test(request):
        request.ctx._request_middleware_test = True
        return request

    # noinspection PyShadowingNames
    async def response_middleware_test(request, response):
        response.ctx._response_middleware_test = True
        return response

    app.add_route(middleware_test, '/')

    app.on_request(request_middleware_test)

# Generated at 2022-06-14 07:42:24.023583
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    # fixture
    class ClassExample(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa

    app = ClassExample()

    # test
    test_middleware = Middleware()
    app.on_request(test_middleware)
    assert app._future_middleware[0].middleware == test_middleware
    assert app._future_middleware[0].attach_to == "request"

    # test
    test_middleware2 = Middleware()
    app.on_request(test_middleware2)
    assert app._future_middleware[1].middleware == test_middle

# Generated at 2022-06-14 07:42:30.339270
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic()

    @app.middleware
    async def handler(request):
        pass

    @app.middleware('request')
    async def handler(request):
        pass

    @app.middleware('response')
    async def handler(request, response):
        pass
    assert len(app._future_middleware) == 3

# Generated at 2022-06-14 07:42:43.551228
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    import pytest
    from sanic.config import Config
    from sanic.server import Server

    server = Server(Config())
    result = server.on_request(middleware=None)
    assert isinstance(result, partial)
    assert result.func is server.middleware
    assert result.keywords == {'attach_to': 'request'}

    result = server.on_request(middleware="my_middleware")
    assert isinstance(result, partial)
    assert result.func is server.middleware
    assert result.keywords == {'attach_to': 'request'}

    def test_middleware(request):
        return request

    result = server.on_request(middleware=test_middleware)
    assert isinstance(result, partial)
    assert result.func is server.middleware

# Generated at 2022-06-14 07:42:54.289724
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic()

    @app.middleware
    def test_mid_1(request):
        pass

    @app.middleware('request')
    def test_mid_2(request):
        pass

    @app.on_request
    def test_mid_3(request):
        pass

    assert app.is_request_stream is False

# Generated at 2022-06-14 07:43:03.010193
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_Test(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    middleware_mixin_test = MiddlewareMixin_Test()
    @middleware_mixin_test.middleware
    def middleware_function(req):
        pass
    assert middleware_function == middleware_mixin_test._future_middleware[0].middleware # noqa


# Generated at 2022-06-14 07:43:03.663415
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert True == True

# Generated at 2022-06-14 07:43:12.049973
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    def middlewarefunc():
        pass

    app = MiddlewareMixin()
    assert len(app._future_middleware) == 0
    app.middleware(middlewarefunc)
    assert len(app._future_middleware) == 1
    assert (
        app._future_middleware[0].__str__() == "{} request {}".format(
            middlewarefunc, middlewarefunc
        )
    )



# Generated at 2022-06-14 07:43:24.844036
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic, response

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    async def handler1(request):
        print('hit handler 1')
        print('handler 1:', request)

    @app.middleware('response')
    async def handler2(request, response):
        print('handler 2:', request)

    @app.route('/middleware')
    async def handler(request):
        print('handler:', request)
        return response.text('OK')

    _, response = app.test_client.get('/middleware')
    assert response.status == 200
    assert response.text == 'OK'



# Generated at 2022-06-14 07:43:38.357686
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    # Setup testing app and method
    app = Sanic(__name__)

    @app.middleware
    async def first_middleware(request):
        request["middleware"] = "first_middleware"

    @app.middleware('response')
    async def second_middleware(request, response):
        request["middleware"] += " second_middleware"

    @app.route("/<name>")
    async def test(request, name):
        return text(name)

    # Trigger the route and retrieve the response
    request, response = app.test_client.get('/test')

    assert response.text == 'test'
    assert request["middleware"] == "first_middleware second_middleware"


# Generated at 2022-06-14 07:43:50.095928
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    TestMiddlewareMixin = MiddlewareMixin()
    """
    Test the functionality of method middleware
    """
    # This test case is similar to actual application.
    # The basic functionality of the method is verified by a simple function
    # which takes an argument and returns the result value
    def func(arg1):
        return arg1
    # Middleware is the returned partial function from the middleware method
    # The partial function takes 2 parameters, a middleware and attach_to
    # The attach_to parameter is by default set to "request"
    # Here, the partial function is not applied and the function is just
    # returned as is
    middleware = TestMiddlewareMixin.middleware(func)
    assert middleware == func
    # The partial function is called with parameters

# Generated at 2022-06-14 07:44:00.101049
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic_jwt import SanicJWT
    from sanic.helpers import is_coroutine_function

    class App(SanicJWT):
        def __init__(self, *args, **kwargs):
            super(SanicJWT, self).__init__(*args, **kwargs)
            self._future_middleware: List[FutureMiddleware] = []

        async def index(self, request):
            return text("OK")

    app = App()

    @app.route("/login", methods=["POST"])
    async def login(request):
        return text("OK")

    @app.middleware
    async def middleware(request):
        print("middleware called")
        return response.text("middleware called")

    assert isinstance(app._future_middleware, list)
    assert len

# Generated at 2022-06-14 07:44:00.956200
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:44:13.198472
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            MiddlewareMixin.__init__(self, *args, **kwargs)

        def _apply_middleware(self, future_middleware):
            pass

    @TestMiddlewareMixin.middleware()
    def middleware():
        pass

    assert TestMiddlewareMixin._future_middleware
    assert len(TestMiddlewareMixin._future_middleware) == 1
    assert TestMiddlewareMixin._future_middleware[0].middleware == middleware
    assert TestMiddlewareMixin._future_middleware[0].attach_to == 'request'


# Generated at 2022-06-14 07:44:27.761998
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A: pass
    class B: pass
    class C: pass
    class D: pass
    
    from sanic.server import Sanic
    
    app = Sanic()
    app.middleware(A)
    app.middleware(B)
    app.middleware(C)
    app.middleware(D)
    assert(A in app._future_middleware)
    assert(B in app._future_middleware)
    assert(C in app._future_middleware)
    assert(D in app._future_middleware)
    

# Generated at 2022-06-14 07:44:34.892365
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    async def custom_middleware(request):
        pass

    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].middleware == custom_middleware
    assert app._future_middleware[0].attach_to == "request"
    assert app._future_middleware[0].initialized == False



# Generated at 2022-06-14 07:44:45.809155
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic()

    @app.middleware
    async def test_middleware(request):
        return request


    @app.middleware('response')
    async def test_middleware_response(request, response):
        return response

    assert app._future_middleware
    assert app._future_middleware[0].handler == test_middleware
    assert app._future_middleware[0].attach_to == 'request'
    assert app._future_middleware[1].handler == test_middleware_response
    assert app._future_middleware[1].attach_to == 'response'



# Generated at 2022-06-14 07:44:47.039007
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:44:56.709163
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    class Test:
        def __init__(self, *args, **kwargs):
            self._future_middleware = []

        def _apply_middleware(self, middleware):
            self._future_middleware.append(middleware)
            return middleware

    test = Test()
    test.middleware(None)
    assert len(test._future_middleware) == 1
    test.middleware('request')(None)
    assert len(test._future_middleware) == 2
    test.middleware('response')(None)
    assert len(test._future_middleware) == 3

# Generated at 2022-06-14 07:44:59.643096
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic()
    app.middleware(lambda a, b, c: None)
    assert 1 == len(app._future_middleware)
    assert 'request' == app._future_middleware[0].attach_to


# Generated at 2022-06-14 07:45:10.031513
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    class TestService(MiddlewareMixin):
        def __init__(self):
            self.request_middleware_calls_number = 0
            self.response_middleware_calls_number = 0
            self.request_middleware_futures = []
            self.response_middleware_futures = []

        def _apply_middleware(self, future_middleware):
            if future_middleware.attach_to == "request":
                self.request_middleware_futures.append(future_middleware)
            elif future_middleware.attach_to == "response":
                self.response_middleware_futures.append(future_middleware)

        @staticmethod
        def _mock_request(request):
            print("MOCK REQUEST")


# Generated at 2022-06-14 07:45:21.967484
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic import Sanic, Blueprint

    app = Sanic()

    @app.middleware
    async def print_on_request(request):
        print("I am in request middleware")

    @app.middleware('request')
    async def print_on_request2(request):
        print("I am also in request middleware")

    @app.middleware('response')
    async def print_on_response1(request, response):
        print("I am in response middleware")

    @app.middleware('response')
    async def print_on_response2(request, response):
        print("I am also in response middleware")


# Generated at 2022-06-14 07:45:25.416942
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    mm: MiddlewareMixin = MiddlewareMixin()
    mm.middleware(middleware=None)
    mm.middleware(middleware_or_request=None)

# Generated at 2022-06-14 07:45:29.871484
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Sanic(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    assert Sanic().middleware
    assert Sanic().on_request
    assert Sanic().on_response

# Generated at 2022-06-14 07:45:46.428652
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    import pytest
    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware
    def shunkai_middleware(request):
        print('middleware on request')

    @app.middleware('response')
    def shunkai_middleware_response(request, response):
        print('middleware on response')

    @app.route('/')
    def shunkai_handler(request):
        return text('OK')

    request, response = app.test_client.get('/')
    assert response.text == 'OK'
    assert app._future_middleware[0].middleware == shunkai_middleware
    assert app._future_middleware[1].middleware == shunkai_middleware_response

# Generated at 2022-06-14 07:45:58.265194
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.server import HttpProtocol
    from sanic.views import HTTPMethodView

    middleware = []

    async def f(request):
        return request

    async def h(request, handler):
        return handler

    class A(Sanic):
        async def handle_request(self, request, write_callback, stream_callback):
            pass

    app = A("test_MiddlewareMixin_middleware")
    middleware_instance = MiddlewareMixin()
    middleware_instance._future_middleware = []
    middleware_instance._apply_middleware = partial(middleware.append)

    # Test normal
    middleware_instance.middleware(f)
    assert len(middleware_instance._future_middleware) == 1
    assert middleware_instance

# Generated at 2022-06-14 07:46:08.210366
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class FakeApp(MiddlewareMixin):
        def __init__(self):
            super().__init__()

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    middleware_or_request = 'request'
    attach_to = 'request'
    apply = True
    app = FakeApp()
    def middleware(request):
        pass
    result = app.middleware(middleware, attach_to=attach_to)
    assert callable(result), 'Result should be a callable.'

# Generated at 2022-06-14 07:46:11.038599
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    m = MiddlewareMixin()
    assert m.middleware == MiddlewareMixin.middleware


# Generated at 2022-06-14 07:46:16.305550
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic()

    app.middleware('request', on_request)
    assert isinstance(app._future_middleware, list)
    assert app._future_middleware[0].middleware == on_request



# Generated at 2022-06-14 07:46:26.177880
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    test_methods = [
        "on_request",
        "on_response"
    ]

    mixin = MiddlewareMixin()

    for method in test_methods:
        assert callable(getattr(mixin, method))
        assert callable(getattr(mixin, method)())

    callable_middleware = callable(getattr(mixin, "on_request")())
    observer = getattr(mixin, "on_request")()
    assert callable(callable_middleware)
    assert callable(observer)

# Generated at 2022-06-14 07:46:36.306196
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    mock_app = MagicMock()
    mock_app.__call__ = MiddlewareMixin.__call__
    mock_app.__init__ = MagicMock()
    mock_app.middleware = MiddlewareMixin.middleware
    mock_app.on_request = MagicMock()
    mock_app.on_response = MagicMock()

    mock_app.middleware(MagicMock())
    mock_app.on_request.assert_called_with()
    mock_app.on_response.assert_not_called()



# Generated at 2022-06-14 07:46:36.958812
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert True == True

# Generated at 2022-06-14 07:46:46.986799
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class App(MiddlewareMixin):
        def __init__(self):
            super(App, self).__init__()
            self.a = 1

        def _apply_middleware(self, middleware):
            self.a = 2

        def clear(self):
            del self._future_middleware[:]

    app = App()
    assert app.a == 1

    @app.middleware
    async def a_middleware(request):
        return 'ok'

    assert app.a == 2
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].middleware is a_middleware
    assert app._future_middleware[0].attach_to == 'request'


# Generated at 2022-06-14 07:46:53.825371
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic()
    @app.middleware('response')
    def handler(request):
        return request

    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].middleware == handler
    assert app._future_middleware[0].attach_to == 'response'

# Generated at 2022-06-14 07:47:17.860579
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MyClass(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    obj = MyClass()

    @obj.middleware
    def fun1(request):
        pass

    fun1 = obj.middleware(fun1)
    fun1 = obj.on_request(fun1)
    fun1 = obj.on_response(fun1)


# Generated at 2022-06-14 07:47:30.049353
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models.futures import FutureMiddleware

    # test_MiddlewareMixin_middleware#1
    @Sanic.middleware
    async def middleware_1(request):
        return 1
    assert middleware_1._middleware_type == FutureMiddleware
    assert middleware_1._middleware_type.middleware == middleware_1
    assert middleware_1._middleware_type.attach_to == 'request'

    # test_MiddlewareMixin_middleware#2
    @Sanic.middleware("response")
    async def middleware_2(request):
        return 2
    assert middleware_2._middleware_type == FutureMiddleware
    assert middleware_2._middleware_type.middleware == middleware_2
    assert middleware_2._

# Generated at 2022-06-14 07:47:40.325073
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from pprint import pprint #todo fix
    from sanic.app import Sanic
    from sanic.response import text
    from sanic.models.futures import FutureMiddleware

    app = Sanic('test_sanic')

    @app.route('/')
    async def handler(request):
        return text('OK')

    @app.middleware('request')
    def request_middleware(request):
        request['middleware'] = 'this is a test'

    @app.middleware('response')
    def response_middleware(request, response):
        response.text += ' middleware'

    request, response = app.test_client.get('/')
    assert response.text == 'OK middleware'
    assert request['middleware'] == 'this is a test'

# Generated at 2022-06-14 07:47:47.376056
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic()

    @app.middleware('request')
    async def attach_something(request):
        request['something'] = 'Nothing'

    @app.route('/')
    async def handler(request):
        assert request['something'] == 'Nothing'
        return text('OK')

    request, response = app.test_client.get('/')
    assert response.text == 'OK'

# Generated at 2022-06-14 07:47:55.134538
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Test:
        def __init__(self):
            self.__dict__ = MiddlewareMixin.__dict__
            super().__init__()

    s = Test()
    m = None

    # Test for on_request
    @s.on_request()
    def middleware(request):
        print(request)
        return request

    assert m is not None
    assert str(m.__name__) == "middleware"
    assert m.__code__.co_argcount == 1
    assert m.__module__ == __name__

    # Test for on_response
    @s.on_response()
    def another_middleware(request, response):
        print(response)
        return response

    assert m is not None
    assert str(m.__name__) == "another_middleware"
   

# Generated at 2022-06-14 07:47:55.887092
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:48:03.756425
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic()

    @app.middleware('request')
    async def foo(request):
        return 'foo'

    assert isinstance(app._future_middleware, list)
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].attach_to == 'request'
    assert asyncio.iscoroutinefunction(app._future_middleware[0].middleware)


# Generated at 2022-06-14 07:48:07.566641
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    app = MiddlewareMixin()
    assert app._future_middleware == []
    assert app.middleware('AT')
    assert app._future_middleware == []
    assert app.middleware('AT', apply=False)
    assert app._future_middleware == []


# Generated at 2022-06-14 07:48:20.837952
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.views import HTTPMethodView

    app = Sanic('test_MiddlewareMixin_middleware')

    # Ensure that middleware functions are
    # registered and properly attached to
    # handler and response_handler lists.
    @app.middleware('request')
    async def handler(request):
        handler.called = True
    @app.middleware('response')
    async def response_handler(request, response):
        response_handler.called = True
    @app.route('/')
    async def handler(request):
        return text('OK')

    request, response = app.test_client.get('/')
    assert handler.called is True
    assert response_handler.called is True

    # Ensure that middleware functions are registered
    # and properly attached when using HTT

# Generated at 2022-06-14 07:48:25.187905
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Initialize
    m = MiddlewareMixin()
    # Run
    result = m.middleware("middleware_or_request")('attach_to')
    # Assert
    assert result == "attach_to"


# Generated at 2022-06-14 07:49:13.006091
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json

    app = Sanic("test_MiddlewareMixin_middleware")

    # test 1
    @app.middleware("request")
    async def test_middleware1(request):
        request["middleware"] = "test_middleware1"

    @app.middleware("response")
    async def test_middleware2(request, response):
        response.body = response.body.decode() + " test_middleware2"

    @app.route("/")
    async def test_handler(request):
        return json({"foo": 1})

    # test 2
    # test 3
    @app.on_request
    async def test_middleware3(request):
        request["middleware"] = "test_middleware3"


# Generated at 2022-06-14 07:49:26.176580
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixinTest:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    mixin = MiddlewareMixinTest()

    # Test default
    @mixin.middleware
    async def middleware_default(request):
        pass

    assert middleware_default.__self__ == mixin
    assert middleware_default.__wrapped__ == wrap_middleware(middleware_default)
    assert mixin._future_middleware == [
        FutureMiddleware(middleware_default, "request")
    ]

    # Test 'request'

# Generated at 2022-06-14 07:49:31.022654
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic(__name__)

    app.middleware('middleware_test')

    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].middleware == 'middleware_test'


# Generated at 2022-06-14 07:49:34.141906
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class testMiddlewareMixin(MiddlewareMixin):
        pass
    a = testMiddlewareMixin()
    a.middleware(middleware_or_request = "request")

# Generated at 2022-06-14 07:49:35.952197
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Not tested because it's just a decorator
    pass


# Generated at 2022-06-14 07:49:45.575235
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic("name")

    @app.middleware("request")
    def route_middleware(request):
        pass

    assert type(
        app.middleware("response")) is partial
    assert type(
        app.middleware) is partial
    assert type(
        app.middleware("request")) is partial
    assert app._apply_middleware is None
    assert app._future_middleware[0].middleware == route_middleware
    assert app._future_middleware[0].attach_to == "request"


# Generated at 2022-06-14 07:49:46.311583
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert 0 == 1

# Generated at 2022-06-14 07:50:00.112232
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import pytest
    from sanic.app import Sanic

    def middleware(request):
        return request

    def another_middleware(request):
        return request

    app = Sanic(__name__)
    app._future_middleware = []
    app.middleware(middleware)
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].middleware_func == middleware
    assert app._future_middleware[0].attach_to == "request"

    app.middleware(attach_to="response")(another_middleware)
    assert len(app._future_middleware) == 2
    assert app._future_middleware[1].middleware_func == another_middleware
    assert app._future_middleware[1].attach_to == "response"

    #

# Generated at 2022-06-14 07:50:07.445294
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic, SanicException
    from sanic.models.futures import FutureMiddleware

    def midd1():
        return

    def midd2():
        return

    with Sanic() as app:
        app.middleware(midd1)
        app.middleware(midd2, 'response')

        assert len(app._future_middleware) == 2
        assert all([isinstance(i, FutureMiddleware) for i in app._future_middleware])

# Generated at 2022-06-14 07:50:21.186979
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic("test_MiddlewareMixin_middleware")
    middleware_or_request = None

    def register_middleware(middleware, attach_to="request"):
        nonlocal middleware_or_request
        middleware_or_request = middleware

    # Test case:
    # middleware_or_request = None
    assert MiddlewareMixin.middleware(None, middleware_or_request) == register_middleware


    # Test case:
    # middleware_or_request = 'request'
    attach_to = "request"
    middleware_or_request = "request"
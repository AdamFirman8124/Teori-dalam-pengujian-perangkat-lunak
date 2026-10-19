

# Generated at 2022-06-14 07:40:16.901968
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class MM(MiddlewareMixin):
        pass
    args = None
    kwargs = {}
    mm = MM(*args, **kwargs)
    mm.middleware("greet", "request")
    mm.on_request("greet")

# Generated at 2022-06-14 07:40:26.826437
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.app import Sanic
    from sanic.models.middleware import MiddlewareMixin
    from sanic.models.futures import FutureMiddleware
    app = Sanic('test')
    app.on_request(print)
    assert app._future_middleware[0].__class__ == FutureMiddleware, app._future_middleware[0].__class__
    assert app._future_middleware[0].middleware == print

    app.on_response(print)
    assert app._future_middleware[1].__class__ == FutureMiddleware, app._future_middleware[1].__class__
    assert app._future_middleware[1].middleware == print
    return

if __name__ == '__main__':
    test_MiddlewareMixin_on_request()

# Generated at 2022-06-14 07:40:40.234598
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.server import HttpProtocol
    from sanic.websocket import WebSocketProtocol

    @MiddlewareMixin.on_request
    def handler_function(request):
        pass

    MiddlewareMixin.on_request(handler_function)

    middleware_mixin = MiddlewareMixin()

    request = Request(b"GET", b"/", [], b"", version=b"1.1")

    class TestMiddleware:
        def __init__(self, request):
            self.request = request

        async def do_request(self):
            pass

        async def do_response(self, response):
            pass

    def middleware_factory(request):
        return TestMiddleware(request)



# Generated at 2022-06-14 07:40:50.320788
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class Test(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa

    def middleware(request):
        pass

    register_middleware = Test().on_request(middleware)
    assert callable(register_middleware)

    register_middleware = Test().on_request()
    register_middleware(middleware)
    assert register_middleware('request') is None


# Generated at 2022-06-14 07:41:00.394448
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json
    from sanic.testing import HOST, PORT

    app = Sanic('test_MiddlewareMixin_middleware')
    x = 0
    @app.middleware
    async def middleware(request):
        nonlocal x
        x = x + 1

    @app.route('/test_1')
    async def test(request):
        return json(x)

    request, response = app.test_client.get('/test_1')
    assert response.json == 1



# Generated at 2022-06-14 07:41:08.255140
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    # Given
    class TestClass(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

    test_class = TestClass()

    @test_class.on_request()
    async def test_middleware(request):
        print('middleware')

    # When
    # Then
    assert len(test_class._future_middleware) is 1


# Generated at 2022-06-14 07:41:18.911452
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    # arrange
    class TestClass(MiddlewareMixin):
        def __init__(self):
            super(TestClass, self).__init__()

        def _apply_middleware(self, middleware):
            pass

    # act
    test_obj = TestClass()

    @test_obj.on_request
    def test_on_request():
        print("teste")

    @test_obj.on_request
    def test_on_request_2():
        print("teste2")

    # assert



# Generated at 2022-06-14 07:41:25.001342
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareClass(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            future_middleware = FutureMiddleware(middleware, 'request')
            self._future_middleware.append(future_middleware)
            return future_middleware

    @MiddlewareClass
    def one_plus(request):
        return request + 1

    assert one_plus(2) != 3
    assert one_plus(2) == 3

# Generated at 2022-06-14 07:41:28.898913
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    m = MiddlewareMixin()
    @m.on_request()
    def ex(request):
        return request
    l = m._future_middleware
    assert(len(l) == 1)


# Generated at 2022-06-14 07:41:40.139299
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.models.middlewares import MiddlewareMixin
    from sanic.models.futures import FutureMiddleware
    from typing import List

    c = MiddlewareMixin()
    _future_middleware: List[FutureMiddleware] = []

    _future_middleware.append(FutureMiddleware(middleware="middleware", attach_to="request"))
    c._future_middleware.append(FutureMiddleware(middleware="middleware", attach_to="request"))

    assert object.__eq__(c._future_middleware, _future_middleware)

    return True


# Generated at 2022-06-14 07:41:56.206811
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class DummyMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super().__init__()
            self.callable = None
            self.middleware_or_request = None
            self.attach_to = None
            self.apply = None

        def _apply_middleware(self, middleware):
            self.callable = None
            self.middleware_or_request = None
            self.attach_to = None
            self.apply = None

    dummy_middleware_mixin = DummyMiddlewareMixin()

    # test for fake callable
    callable_foo = lambda: None
    dummy_middleware_mixin.middleware(callable_foo)

    assert dummy_middleware_mixin.callable == None
    assert dummy_middleware_mixin.middleware_

# Generated at 2022-06-14 07:42:03.682822
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json
    @app.middleware
    async def handler(request):
        pass
    @app.middleware('request')
    async def handler(request):
        pass
    @app.middleware('response')
    async def handler(response):
        pass
    @app.on_request
    async def handler(request):
        pass
    @app.on_response
    async def handler(response):
        pass


# Generated at 2022-06-14 07:42:04.313750
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # TODO: add unit test for method middleware of class MiddlewareMixin
    pass

# Generated at 2022-06-14 07:42:04.911307
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:42:09.151877
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.middleware import Middleware

    m = Middleware()
    assert m.middleware
    assert m.middleware(partial(1, 'test'))
    assert m.on_request(partial(2, 2))
    assert m.on_response(partial(3, 3))

# Generated at 2022-06-14 07:42:11.022481
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass



# Generated at 2022-06-14 07:42:18.332971
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestHandler:
        def method(self, req):
            pass

    app = TestHandler()
    app.middleware = MiddlewareMixin.middleware
    app.on_request = MiddlewareMixin.on_request
    app.on_response = MiddlewareMixin.on_response
    app.on_request(lambda _: None)()(app.method)(app, {}, {})
    app.on_response(lambda _: None)()(app.method)(app, {}, {})
    app.middleware(lambda _: None)()(app.method)(app, {}, {})

# Generated at 2022-06-14 07:42:31.676002
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware
    from sanic.models.futures import FutureType

    app = Sanic()

    @app.middleware
    async def test_middleware(request):
        pass

    assert app._future_middleware == [FutureMiddleware(test_middleware, attach_to="request")]

    app = Sanic()

    @app.middleware("request")
    async def test_middleware(request):
        pass

    assert app._future_middleware == [FutureMiddleware(test_middleware, attach_to="request")]

    app = Sanic()

    @app.middleware("response")
    async def test_middleware(request, response):
        pass


# Generated at 2022-06-14 07:42:41.851989
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('request')
    def request(request):
        return request

    @app.middleware
    def response(request, response):
        return response

    assert len(app._future_middleware) == 2
    assert app._future_middleware[0].middleware == request
    assert app._future_middleware[0].attach_to == "request"
    assert app._future_middleware[1].middleware == response
    assert app._future_middleware[1].attach_to == "response"

# Generated at 2022-06-14 07:42:52.251264
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic("test_MiddlewareMixin_middleware")

    async def middleware1(request):
        request["middleware1"] = True
        return request

    @app.middleware
    def middleware2(request):
        request["middleware2"] = True
        return request

    request = app.request("/", method="GET")
    assert request.get("middleware1") is None
    assert request.get("middleware2") is None

    app.add_task(app._run_request_middleware, request)

    request = sanic.server.loop.run_until_complete(request)  # type: ignore

    assert request["middleware1"] is True
    assert request["middleware2"] is True

    request = app.request("/", method="GET")
   

# Generated at 2022-06-14 07:43:06.803786
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """
    Unit test for method middleware of class MiddlewareMixin
    """
    # Create a dummy class Inherit from MiddlewareMixin class
    class DummyMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(DummyMiddlewareMixin, self).__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    # Test
    dummy_obj = DummyMiddlewareMixin()
    assert dummy_obj.middleware() is not None
    assert dummy_obj.middleware("request") is not None

if __name__ == "__main__":
    test_MiddlewareMixin_middleware()

# Generated at 2022-06-14 07:43:08.998303
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    MiddlewareMixin.middleware(object, 'request')


# Generated at 2022-06-14 07:43:21.239201
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Unit test for method middleware of class MiddlewareMixin
    # _future_middleware: List[FutureMiddleware] = []
    from sanic.app import Sanic
    app = Sanic(__name__)
    @app.middleware  # noqa
    def aa(request):
        pass
    @app.middleware('request')
    def bb(request):
        pass
    @app.middleware('response')  # noqa
    def cc(request, response):
        pass
    @app.on_request  # noqa
    def dd(request):
        pass
    @app.on_response  # noqa
    def ee(request, response):
        pass

# Generated at 2022-06-14 07:43:30.949955
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    print('Unit test for method middleware of class MiddlewareMixin')
    def middleware_1(request):
        return request

    def middleware_2(request):
        return request

    app = Sanic('test_MiddlewareMixin_middleware')
    app.middleware(middleware_1)
    app.middleware(middleware_2)
    assert len(app._future_middleware) == 2
    print('Unit test completed')
    print('----------------------------------------------------------------------')


# Generated at 2022-06-14 07:43:40.829794
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import asynctest

    from sanic import Sanic
    from sanic.models.futures import FutureMiddleware

    app = Sanic("middleware_test")

    assert len(app._future_middleware) == 0

    @app.middleware
    async def test_middleware(request):
        pass

    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert app._future_middleware[0].middleware == test_middleware
    assert app._future_middleware[0].attach_to == "request"

    @app.middleware("response")
    async def test_middleware_2(request):
        pass

    assert len(app._future_middleware) == 2

# Generated at 2022-06-14 07:43:45.565231
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    test_MiddlewareMixin = MiddlewareMixin()
    def test_func1(self, request):
        pass
    def test_func2(self, request):
        pass
    test_MiddlewareMixin.middleware(test_func1, "request")
    test_MiddlewareMixin.middleware(test_func2, "response")


# Generated at 2022-06-14 07:43:54.792617
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    async def middleware_1(request):
        pass

    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].middleware is middleware_1
    assert app._future_middleware[0].attach_to == 'request'

    @app.middleware('response')
    async def middleware_2(request):
        pass

    assert len(app._future_middleware) == 2
    assert app._future_middleware[1].middleware is middleware_2
    assert app._future_middleware[1].attach_to == 'response'


# Generated at 2022-06-14 07:44:08.476840
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    my_app = Sanic()
    assert my_app._future_middleware == []
    assert my_app._middleware == []

    @my_app.middleware
    def mid_war(request):
        return request

    @mid_war
    def test_function():
        pass

    assert my_app._future_middleware == [
        FutureMiddleware(mid_war, "request")
    ]
    assert my_app._middleware == [mid_war]

    @my_app.middleware('response')
    def mid_war_response(request, response):
        return response

    @mid_war_response
    def test_function_response():
        pass


# Generated at 2022-06-14 07:44:13.200127
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    mm = MiddlewareMixin()

    @mm.middleware
    def middleware_func(request,response):
        pass

    fm = FutureMiddleware(middleware_func, "request")
    assert fm in mm._future_middleware


# Generated at 2022-06-14 07:44:26.072333
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Test: call on a class that inherits this class
    from sanic import Sanic
    app = Sanic()
    assert isinstance(app, MiddlewareMixin)

    # Test: register a middleware without specifying attach_to, which will call
    # self._apply_middleware, which is an abstract method that must be
    # implemented by the subclasses
    @app.middleware
    async def test_middleware(request):
        return await request.app.Test(request)

    # Test: register a middleware with specifying attach_to
    @app.middleware('response')
    async def test_middleware_response(request, response):
        return await request.app.Test(request)

    # Test: register a middleware with specifying attach_to, then call
    # self._apply_middleware to apply it

# Generated at 2022-06-14 07:44:35.243046
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class SomeClass(MiddlewareMixin):
        def __init__(self):
            super().__init__()

        def test_function(self):
            return "test"

    my_test = SomeClass()

    def test_middleware(request):
        assert request == "test"

    on_request = my_test.middleware(test_middleware)
    on_request(my_test.test_function())

# Generated at 2022-06-14 07:44:48.536151
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    a = 1
    def b(a):
        pass
    test = TestMiddlewareMixin()

    assert test.middleware(b, 'request', True) == b
    assert test.middleware(b, 'response', True) == b
    assert test.middleware(b) == b

    test.middleware(b, 'request', False)
    assert test._future_middleware[0].middleware == b and test._future_middleware[0].attach_to == 'request'

    test.middleware(b, 'response', False)
    assert test._future_middleware[1].middleware == b and test._future_middleware[1].attach_to == 'response'

# Generated at 2022-06-14 07:44:58.749944
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    s = MiddlewareMixin()
    s2 = MiddlewareMixin()
    # 1
    @s.middleware
    def test_middleware(request):
        pass
    assert isinstance(test_middleware, partial)
    # 2
    @s2.middleware('request')
    def test_middleware(request):
        pass
    assert isinstance(test_middleware, partial)
    # 3
    @s.on_request
    def test_middleware(request):
        pass
    assert isinstance(test_middleware, partial)
    # 4
    @s.on_response
    def test_middleware(request):
        pass
    assert isinstance(test_middleware, partial)

# Generated at 2022-06-14 07:45:12.140194
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_test(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    mm = MiddlewareMixin_test

    @mm.middleware
    async def mw1(request):
        print("mw1")

    assert len(mm._future_middleware) == 1
    assert mm._future_middleware[0].middleware == mw1

    @mm.middleware("request")
    async def mw2(request):
        print("mw2")

    assert len(mm._future_middleware) == 2

# Generated at 2022-06-14 07:45:23.657646
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.handlers import ErrorHandler
    from sanic.response import BaseHTTPResponse
    from sanic.router import Router
    from sanic.server import HttpProtocol
    from sanic.websocket import WebSocketProtocol
    from sanic.utilities import REGEX_TYPE

    app = Sanic("test")

    @app.middleware
    async def middleware_callable(request):
        return request
    
    # Check instance variables
    assert app._future_middleware[0]._middleware_fun == middleware_callable
    assert app._future_middleware[0]._attach_to == "request"
    assert app._middleware[0]._middleware_fun == middleware_callable
    assert app._middleware[0]._attach

# Generated at 2022-06-14 07:45:35.397189
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic.testing import HOST, PORT, SanicTestClient
    from sanic.websocket import WebSocketProtocol

    app = Sanic(__name__)
    client = SanicTestClient(app, protocol=WebSocketProtocol)

    # Middleware
    async def my_middleware(request, response):
        response.headers["request-middleware-loaded"] = "yes"

    async def my_response_middleware(request, response):
        response.headers["response-middleware-loaded"] = "yes"

    app.middleware(my_middleware, attach_to="request")
    app.middleware(my_response_middleware, attach_to="response")


# Generated at 2022-06-14 07:45:36.105405
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:45:37.207510
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:45:48.578868
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic()

    assert not app._future_middleware

    @app.middleware
    async def example_middleware(request):
        pass

    assert app._future_middleware[0].middleware == example_middleware
    assert app._future_middleware[0].attach_to == "request"

    app._future_middleware = []

    @app.middleware('response')
    async def another_example_middleware(request):
        pass

    assert app._future_middleware[0].middleware == another_example_middleware
    assert app._future_middleware[0].attach_to == "response"



# Generated at 2022-06-14 07:45:57.016133
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models import SanicMiddleware
    from sanic.models.futures import FutureMiddleware
    from sanic.models.futures import MiddlewareType

    app=Sanic("test")
    app.middleware(SanicMiddleware)
    assert len(app._future_middleware) == 1
    middleware=app._future_middleware[0]
    assert middleware.middleware == SanicMiddleware
    assert middleware.attach_to == MiddlewareType.REQUEST

# Generated at 2022-06-14 07:46:14.894505
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.server import BaseHTTPServer
    from sanic.app import Sanic

    class MockHttpServer(BaseHTTPServer):
        def prepare_middleware(self, *args, **kwargs):
            from sanic.app import Sanic
            # Sanic.__new__()::return: <sanic.app.Sanic object>
            sanic_test_app = Sanic.__new__(Sanic, *args, **kwargs)
            # Sanic.__init__()
            sanic_test_app.__init__(*args, **kwargs)
            # Sanic._apply_middleware()
            sanic_test_app._apply_middleware = mock.MagicMock(
                side_effect=sanic_test_app._apply_middleware
            )
            return sanic_test_app



# Generated at 2022-06-14 07:46:15.961010
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert True

# Generated at 2022-06-14 07:46:25.876773
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super().__init__()

    tmm = TestMiddlewareMixin()
    middleware_content = [lambda *args, **kwargs: args, lambda *args, **kwargs: kwargs]
    for middleware in middleware_content:
        tmm.middleware(middleware, "response")
    print("test_MiddlewareMixin_middleware passed")
test_MiddlewareMixin_middleware()


# Generated at 2022-06-14 07:46:26.497368
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:46:40.362620
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMWMixin(MiddlewareMixin):
        def __init__(self) -> None:
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    m = TestMWMixin()
    assert m._future_middleware == []

    # The first form of @app.middleware in docstring
    @m.middleware
    async def foo_request(request):
        return request
    @m.middleware
    async def foo_response(request, response):
        return response

    # The second form of @app.middleware in docstring
    @m.middleware('request')
    async def bar_request(request):
        return request
    @m.middleware('response')
    async def bar_response(request, response):
        return response

# Generated at 2022-06-14 07:46:49.334915
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # mock class MiddlewareMixin
    class MockClassMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._future_middleware = []

    # mock method _apply_middleware
    def mock_apply_middleware(middleware: FutureMiddleware):
        return middleware

    # mock method callable
    def callable_mock(middleware_or_request):
        assert middleware_or_request == "request"
        return True

    # mock method callable
    def callable_mock_2(middleware_or_request, attach_to):
        assert middleware_or_request == "request"
        assert attach_to == "request"
        return True

    class_middleware_mix

# Generated at 2022-06-14 07:46:56.834794
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MSubject(MiddlewareMixin):
        def __init__(self):
            super().__init__()
            self._future_middleware:List[FutureMiddleware]=[]

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    mSubject=MSubject()
    mSubject.middleware('request',apply=True)
    assert mSubject._future_middleware != None

# Generated at 2022-06-14 07:47:07.625291
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import unittest
    from sanic.app import Sanic
    from sanic import response
    class MyTestCase(unittest.TestCase):
        def test_middleware_mixin_register(self):
            app = Sanic(__name__)
            @app.middleware
            def example_middleware(request):
                print('Before request')
            
            @app.middleware('request')
            def example_middleware2(request):
                print('Before request')
            
            @app.middleware('response')
            def example_middleware3(request, response):
                print('Before request')

            @app.route('/')
            async def handler(request):
                return response.text('OK')

            self.assertEqual(len(app._future_middleware), 3)
            self.assertE

# Generated at 2022-06-14 07:47:14.444339
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class DummyClass(MiddlewareMixin):
        pass

    def dummy_middleware(request):
        ...

    dummy_instance = DummyClass()

    assert not dummy_instance._future_middleware

    dummy_instance.middleware(dummy_middleware)

    assert len(dummy_instance._future_middleware) == 1
    assert dummy_instance._future_middleware[-1].middleware is dummy_middleware
    assert dummy_instance._future_middleware[-1].attach_to == "request"


# Generated at 2022-06-14 07:47:18.320278
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.log import logger
    from sanic.app import Sanic

    app = Sanic(__name__)

    @app.middleware('request')
    async def before_all_bar_request(request):
        logger.debug("Before all bar request")

    @app.middleware('response')
    async def before_all_bar_response(request, response):
        logger.debug("Before all bar response")

    @app.route('/')
    async def handler(request):
        return response.json({"foo": "bar"})


# Generated at 2022-06-14 07:47:32.693872
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:47:38.383327
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            assert middleware

    test_middleware = TestMiddlewareMixin()

    @test_middleware.middleware
    async def test(request):
        pass

# Generated at 2022-06-14 07:47:49.502158
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models import FutureMiddleware

    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, future_middleware: FutureMiddleware):
            pass

    s = Sanic(__name__)

    # __init__
    future_middleware: List[FutureMiddleware] = []
    assert s._future_middleware == future_middleware

    # test _apply_middleware
    with pytest.raises(NotImplementedError):
        s._apply_middleware(future_middleware)

    # test middleware
    # 1. Test register_middleware of app.middleware
    def middleware(request):
        pass
    assert s.middleware(middleware) == middleware

# Generated at 2022-06-14 07:48:03.085887
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import BaseHTTPResponse, text

    class MyMiddleware:
        def __init__(self, app, attach_to):
            self.app = app
            self.attach_to = attach_to

    app = Sanic(__name__)
    app.middleware(MyMiddleware, attach_to='request')
    app.middleware(MyMiddleware, attach_to='response')

    assert len(app._middleware) == 0
    assert len(app._future_middleware) == 2
    assert isinstance(
        app._future_middleware[0], FutureMiddleware
    )
    assert app._future_middleware[0].middleware == MyMiddleware
    assert app._future_middleware[0].attach_to == 'request'


# Generated at 2022-06-14 07:48:10.065651
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        _apply_middleware = MagicMock()
        pass

    test_MiddlewareMixin = TestMiddlewareMixin()
    middleware = MagicMock()

    test_MiddlewareMixin.middleware(middleware)
    assert test_MiddlewareMixin._apply_middleware.call_args_list == [
        call(middleware, "request")
    ]

    test_MiddlewareMixin.middleware("response")(middleware)

    assert test_MiddlewareMixin._apply_middleware.call_args_list == [
        call(middleware, "request"),
        call(middleware, "response"),
    ]

# Generated at 2022-06-14 07:48:20.762742
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic import Sanic
    from sanic.models.futures import FutureMiddleware

    def middleware_func(request):
        return request

    app = Sanic()
    assert len(app._future_middleware) == 0
    app.middleware(middleware_func)
    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert app._future_middleware[0].middleware_func == middleware_func
    assert app._future_middleware[0].attach_to == "request"


# Generated at 2022-06-14 07:48:32.923013
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Server:
        pass

    server = Server()
    server_address = ("127.0.0.1", 8000)

    server.config = {
        "KEEP_ALIVE": False,
        "REQUEST_MAX_SIZE": 100000000,
        "REQUEST_BUFFER_QUEUE_SIZE": 100,
        "RESPONSE_TIMEOUT": 60,
        "WEBSOCKET_MAX_SIZE": 2 ** 20,
        "REQUEST_TIMEOUT": 60,
        "RESPONSE_MAX_SIZE": 100000000,
    }

    server.debug = False
    server.is_running = False
    server.before_start = []
    server.after_start = []
    server.before_server_stop = []
    server.after_server_stop = []
    server.before_task

# Generated at 2022-06-14 07:48:41.923453
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic('test_MiddlewareMixin')

    @app.middleware  # noqa
    def middleware_test(request):
        assert True

    @app.middleware('request')  # noqa
    def middleware_test_request(request):
        assert True

    @app.middleware('response')  # noqa
    def middleware_test_response(request, response):
        assert True

    @app.listener('before_server_start')
    async def after_server_start_test(app, loop):
        assert True

    @app.listener('before_server_stop')
    async def before_server_stop_test(app, loop):
        assert True


# Generated at 2022-06-14 07:48:45.634599
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic("sanic-server")

    def middleware(request):
        pass

    app.middleware(middleware)

    assert middleware in app._middleware



# Generated at 2022-06-14 07:48:53.623663
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """
    Test if method "middleware" returns expected object when decorate a function as a middleware
    """
    # Given
    app = MiddlewareMixin()
    @app.middleware
    async def middleware(request):
        print ("Executing $$$$ Middleware$$$")
    # Then
    assert "(FutureMiddleware: 'middleware' @ 'request'" in str(app._future_middleware[0])


# Generated at 2022-06-14 07:49:32.801080
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Test_MiddlewareMixin(unittest.TestCase):
        def setUp(self):
            self.app = sanic.Sanic('test_MiddlewareMixin_middleware')

        def test_middleware(self):

            result = self.app.middleware
            #print(result)

            @self.app.middleware
            def handler(request):
                return request

            @self.app.middleware('request')
            def handler2(request):
                return request

            @self.app.on_request
            def handler3(request):
                return request

            @self.app.middleware
            async def handler4(request):
                return request

            @self.app.on_response
            def handler5(request, response):
                return response


# Generated at 2022-06-14 07:49:33.814756
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:49:34.912228
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert True
    

# Generated at 2022-06-14 07:49:47.637188
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import sanic
    from sanic.models import FutureMiddleware

    app = sanic.Sanic()
    assert app._future_middleware == []

    @app.middleware()
    def test(request):
        pass
    assert app._future_middleware == [FutureMiddleware(test, "request")]
    assert app.middleware == MiddlewareMixin.middleware

    @app.on_request()
    def test2(request):
        pass
    assert app._future_middleware == [
        FutureMiddleware(test, "request"),
        FutureMiddleware(test2, "request"),
    ]
    assert app.on_request == MiddlewareMixin.on_request

    @app.on_response()
    def test3(request, response):
        pass

# Generated at 2022-06-14 07:50:01.212502
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            self._future_middleware.append(middleware)

    # test middleware
    tmm = TestMiddlewareMixin()
    @tmm.middleware
    async def test_middleware(request):
        return request

    assert len(tmm._future_middleware) == 1
    assert tmm._future_middleware[0].middleware == test_middleware
    assert tmm._future_middleware[0].attach_to == "request"

    # test on_request
    tmm = TestMiddlewareMixin()
    @tmm.on_request
    async def test_middleware(request):
        return request

    assert len(tmm._future_middleware) == 1
   

# Generated at 2022-06-14 07:50:02.613774
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert 1 == 1

# Generated at 2022-06-14 07:50:04.492469
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    M = MiddlewareMixin()
    assert M.middleware is not None


# Generated at 2022-06-14 07:50:18.562720
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import pytest
    
    from sanic import Sanic
    
    from sanic.models.futures import FutureMiddleware

    class TestMiddlewareMixin(MiddlewareMixin):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    sanic = Sanic(__name__)
    assert isinstance(sanic, MiddlewareMixin)

    @sanic.middleware
    async def call_middleware(request):
        pass

    assert len(sanic._future_middleware) == 1
    future_middleware = sanic._future_middleware[0]
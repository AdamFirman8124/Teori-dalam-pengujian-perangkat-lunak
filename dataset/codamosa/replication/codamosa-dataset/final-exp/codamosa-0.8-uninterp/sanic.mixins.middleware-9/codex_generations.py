

# Generated at 2022-06-14 07:40:08.510890
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_test(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            print("middleware = {}".format(middleware))
    @MiddlewareMixin_test.middleware("request")
    async def middleware_test(request, handler):
        pass
    
    assert MiddlewareMixin_test._future_middleware != [] and MiddlewareMixin_test._future_middleware[0].attach_to == "request"

# Generated at 2022-06-14 07:40:21.820219
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.futures import FutureMiddleware

    class B:
        pass

    obj = MiddlewareMixin()
    assert not obj._future_middleware

    # Sanity check
    try:
        obj._apply_middleware(FutureMiddleware(B))
        assert False
    except NotImplementedError:
        assert True

    def foo():
        pass

    # @app.middleware(attach_to='request')
    func = obj.middleware('request')
    func(foo)
    assert obj._future_middleware
    assert isinstance(obj._future_middleware[0], FutureMiddleware)
    assert obj._future_middleware[0].middleware is foo
    assert obj._future_middleware[0].attach_to == 'request'

    # @app.middleware(attach_to='

# Generated at 2022-06-14 07:40:27.351005
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class T(MiddlewareMixin):
        pass
    t = T()
    @t.on_request
    def m(x):
        return x
    assert t._future_middleware[0].attach_to == "request"
    assert t._future_middleware[0].middleware == m


# Generated at 2022-06-14 07:40:38.433605
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    # In this test, we use MiddlewareMixin as a base class for another class,
    # and call the on_request method, which should return a function with
    # attach_to='request'
    class Test:
        def __init__(self):
            self.attach_to = None

        def register_middleware(self, middleware, attach_to):
            self.attach_to = attach_to

        def _apply_middleware(self, middleware):
            pass

    test = Test()
    mixin = MiddlewareMixin()

    test.middleware = mixin.middleware
    test.on_request = mixin.on_request
    test.on_response = mixin.on_response

    test_middleware = lambda: 0
    test_middleware_with_param = lambda param: None
    real_

# Generated at 2022-06-14 07:40:42.030165
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    obj = MiddlewareMixin()
    assert isinstance(obj.on_response(), partial)

# Generated at 2022-06-14 07:40:42.881666
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    assert Sanic.on_response



# Generated at 2022-06-14 07:40:54.682213
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """
    Unit test for method middleware of class MiddlewareMixin
    """
    class DummySanic(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            pass

    class DummyMiddleware:
        def __init__(self):
            self.info = None

        def __call__(self, request):
            self.info = request

    dummy_middleware = DummyMiddleware()

    # Test @app.middleware
    dummy = DummySanic()
    dummy.middleware(dummy_middleware)

    assert dummy._future_middleware[0].middleware == dummy_middleware
    assert dummy._future_middleware[0].attach_to == "request"

    # Test @app.middleware('response')
    dummy = DummySanic()
    dummy.middleware

# Generated at 2022-06-14 07:40:55.591941
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:41:00.832724
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.model import MiddlewareMixin
    class TestMiddleware(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []
    
    a = TestMiddleware()

    @a.on_request
    def some_func(request):
        pass

    assert a._future_middleware[0].middleware == some_func
    assert a._future_middleware[0].attach_to == 'request'

# Generated at 2022-06-14 07:41:13.126736
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import unittest

    class _MiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super(_MiddlewareMixin, self).__init__()

        def _apply_middleware(self, middleware: FutureMiddleware):
            return middleware

    # TODO should remove this test
    class _MiddlewareMixinTestCase(unittest.TestCase):
        def setUp(self):
            self._app = _MiddlewareMixin()

        def test_call_middleware_two_ways(self):
            def _middleware_callable():
                pass

            def _middleware_callback(request, response):
                pass

            self.assertIs(_middleware_callable, self._app.middleware(_middleware_callable, attach_to='request'))

# Generated at 2022-06-14 07:41:22.496014
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    from sanic.response import text

    app = Sanic("test_MiddlewareMixin_on_response")

    @app.route("/")
    async def handler(request):
        return text("OK")

    @app.middleware("response")
    async def add_header_middleware(request, response):
        response.headers["Awesome"] = "OK"

    request, response = app.test_client.get("/")

    assert response.status == 200
    assert response.headers.get("Awesome") == "OK"

# Generated at 2022-06-14 07:41:30.232581
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    import asyncio
    app = Sanic()

    async def add_2(request):
        return request + 2

    @app.middleware(attach_to="response")
    async def add_1(request):
        return request + 1

    @app.middleware(attach_to="response")
    async def add_3(request):
        return request + 3

    @app.route("/")
    async def handler(request):
        return request

    request, response = app.test_client.get("/")
    assert response.text == '0'

    request, response = app.test_client.get("/add_2")
    assert response.text == '2'

    request, response = app.test_client.get("/add_1")

# Generated at 2022-06-14 07:41:38.597343
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic

    app = Sanic()
    @app.on_request
    def my_middleware(request):
        print("do something on request", request)
        return

    assert len(app._future_middleware) == 1
    middleware = app._future_middleware[0]
    assert middleware.middleware == my_middleware
    assert middleware.attach_to == "request"


# Generated at 2022-06-14 07:41:41.959261
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    # Define middleware
    @Sanic.middleware
    def dd(request):
        pass
    # check data
    assert callable(dd)

# Generated at 2022-06-14 07:41:55.050815
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    from sanic.testing import SanicTestClient


    class MiddlewareMixinTest(MiddlewareMixin):
        ...

    s = Sanic("test_MiddlewareMixin_middleware")

    @s.middleware("request")
    async def request_test(request):
        print("Test request")

    @s.middleware("response")
    async def response_test(request, response):
        print("Test response")

    client = SanicTestClient(s)
    client.get("/")

    assert len(s._future_middleware) == 2
    assert s._future_middleware[0].middleware is request_test
    assert s._future_middleware[0].attach_to == "request"
    assert s._future_middleware[1].middleware is response_test
    assert s._future_middleware

# Generated at 2022-06-14 07:42:06.762861
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class FakeApp(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            return None

    def middleware(middleware=None):
        if callable(middleware):
            return self.middleware(middleware, "request")
        else:
            return partial(self.middleware, attach_to="request")
            
    app = FakeApp()

    middleware = app.on_request(middleware)
    assert middleware
    assert middleware.keywords["attach_to"] == "request"

    middleware = app.on_request()
    assert middleware

# Generated at 2022-06-14 07:42:12.907613
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    import sanic
    app = sanic.Sanic(__name__)

    @app.on_request
    def on_request(request):
        from sanic.response import text
        return text('on_request')

    request, response = app.test_client.get('/')
    assert response.text == 'on_request'


# Generated at 2022-06-14 07:42:16.301450
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert MiddlewareMixin.middleware
    assert MiddlewareMixin.on_request
    assert MiddlewareMixin.on_response



# Generated at 2022-06-14 07:42:25.087731
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Server:
        def __init__(self, *args, **kwargs):
            self._future_middleware = []

    server = Server()

    assert server._future_middleware == []

    @MiddlewareMixin.middleware(server, 'test')
    def handler(request):
        pass
    assert server._future_middleware[0].attach_to == 'test'

    assert server._future_middleware[0].future_middleware == handler



# Generated at 2022-06-14 07:42:34.256374
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    import unittest
    class UnitTestMiddlewareMixin(MiddlewareMixin):
        #def __init__(self, *args, **kwargs):
        #    pass
        def _apply_middleware(self, middleware):
            pass
    class MiddlewareMixinTestCase(unittest.TestCase):
        def test_on_response_with_middleware_callable(self):
            uut = UnitTestMiddlewareMixin()
            result = uut.on_response(middleware=lambda response: response)
            self.assertEqual(type(result), partial)

        def test_on_response_with_no_middleware(self):
            uut = UnitTestMiddlewareMixin()
            result = uut.on_response()
            self.assertEqual(type(result), partial)


# Generated at 2022-06-14 07:42:45.092571
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class FakeMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            print(middleware)
    def mw(request, response):
        pass
    fmw = FakeMiddlewareMixin()
    fmw.on_response(mw)()


# Generated at 2022-06-14 07:42:56.798903
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class DummyClass():
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa

    obj = DummyClass()
    MiddlewareMixin.__init__(obj)
    res = obj.on_response()
    assert type(res).__name__ == "partial"
    assert res.func == obj.middleware
    assert res.keywords == {"attach_to": "response"}
    assert res.args == ()

    # execute callable
    res = obj.on_response(middleware=str)
    assert res == str

# Generated at 2022-06-14 07:43:02.297601
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Given
    instance_MiddlewareMixin = MiddlewareMixin()
    middleware = lambda *args, **kwargs: print(args, kwargs)

    # When
    result = instance_MiddlewareMixin.on_response(middleware)

    # Then
    assert result == None

# Generated at 2022-06-14 07:43:06.679001
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.models.middlewares import MiddlewareMixin
    @MiddlewareMixin.on_response()
    def mw1(request):
        return request
    assert mw1.__name__ == "mw1"

# Generated at 2022-06-14 07:43:08.754651
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert MiddlewareMixin.mixin_test is not None


# Generated at 2022-06-14 07:43:12.579751
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class fake_app(MiddlewareMixin):
        pass
    # call a fake middleware
    app = fake_app()
    app.on_response(middleware = lambda x: print(x))

# Generated at 2022-06-14 07:43:18.824865
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    obj = TestMiddlewareMixin()
    assert isinstance(obj.on_response(lambda: None), types.FunctionType)



# Generated at 2022-06-14 07:43:28.147054
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from http import HTTPStatus
    from sanic.response import json
    from sanic.models.futures import FutureMiddleware
    from typing import List

    def check_middleware(middleware: FutureMiddleware):
        nonlocal app
        assert middleware.attach_to == "response"
        assert middleware.middleware in app.response_middleware

    async def _on_response_middleware(request, response):
        return json({"on_response middleware": True})

    app = Sanic("sanic-middleware")
    app.response_middleware = []
    app._apply_middleware = check_middleware


# Generated at 2022-06-14 07:43:34.047083
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Arrange
    import sanic
    app = sanic.Sanic("test_sanic_on_response")
    
    def func(*args, **kwargs):
        return True
    
    # Act & Assert
    response = app.on_response(func)
    assert response()

# Generated at 2022-06-14 07:43:36.852001
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    middleware_mock_class = MiddlewareMixin()
    middleware_mock_class.on_response()
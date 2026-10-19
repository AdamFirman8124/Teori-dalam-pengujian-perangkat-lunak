

# Generated at 2022-06-14 07:40:27.161762
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    import json
    
    class MockMiddlewareMixin:
        def __init__(self):
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    
    with pytest.raises(ValueError):
        MockMiddlewareMixin.middleware(
            attach_to="aaaaa"
        )
    
    mm = MiddlewareMixin()

    def test1(self):
        pass
    
    def test2(self):
        pass

    def test3(self):
        pass
    
    mm.on_response(test1)
    mm.on_response(test2)
    mm.on_response(test3)

# Generated at 2022-06-14 07:40:36.133071
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    middleware = MiddlewareMixin()
    assert hasattr(middleware, '_future_middleware')
    assert hasattr(middleware, '_apply_middleware')

    assert hasattr(middleware, 'on_request')
    assert hasattr(middleware, 'on_response')
    assert hasattr(middleware, 'middleware')

    assert callable(middleware.on_response)
    assert callable(middleware.on_response(middleware))
    assert callable(middleware.on_response(middleware))



# Generated at 2022-06-14 07:40:38.536318
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    response = MiddlewareMixin()
    response.on_response(middleware=None)


# Generated at 2022-06-14 07:40:52.579781
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic_base_router import Router
    from sanic_base_server import Server
    from sanic_base_app import SanicBase
    from sanic_base_client import Client

    app = SanicBase("test_on_response")

    @app.middleware("response")
    async def response_middleware(request):
        foo = request.headers.get("foo")
        assert foo == "bar"

    @app.route("/")
    async def handler(request):
        return text("OK")

    client = app.test_client

    server = Server(app)
    server.create_server(loop=app.loop)
    server.server.close()

    assert len(app._middleware["response"]) == 1
    assert len(app._future_middleware) == 1


# Generated at 2022-06-14 07:41:03.175436
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Check whether the on_response method behaves as expected
    from sanic.app import Sanic
    from sanic.views import HTTPMethodView

    class Dummy_view(HTTPMethodView):
        pass

    app = Sanic(__name__)
    route = app.route("/test/", methods=["GET", "POST"])(
        Dummy_view.as_view("dummy_view")
    )
    app.on_response(lambda request, response: 1)
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].attach_to == "response"

# Generated at 2022-06-14 07:41:14.436158
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import sys
    import io
    import pytest
    from unittest.mock import MagicMock

    from sanic.app import Sanic
    from sanic.response import HTTPResponse

    @MiddlewareMixin.middleware(attach_to='request')
    async def request_middleware(request):
        request.used_middleware = True

    @MiddlewareMixin.middleware(attach_to='response')
    async def response_middleware(request, response):
        response.used_middleware = True

    saved_print = print

# Generated at 2022-06-14 07:41:24.448319
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    def request_middleware(request):
        pass

    def response_middleware(request, response):
        pass

    class DummyMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(DummyMiddlewareMixin, self).__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    dummy_middleware_mixin = DummyMiddlewareMixin()

    dummy_middleware_mixin.middleware(request_middleware)
    dummy_middleware_mixin.on_request(request_middleware)
    dummy_middleware_mixin.on_response(response_middleware)


# Generated at 2022-06-14 07:41:37.958822
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Create a new class inheriting MiddlewareMixin
    class TestClass(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.counter = 0

        # Create method test_on_response
        def test_on_response(self):
            # Increment the counter
            self.counter = self.counter + 1
            # Use on_response to increment the counter
            self.on_response(self.on_response1)
            # Call on_response that should increment the counter
            self.on_response()
            # Assert the counter should be 2
            assert self.counter == 2
        
        def on_response1(self):
            self.counter = self.counter + 1

    # Create a new object of class Test

# Generated at 2022-06-14 07:41:49.192256
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            pass

    # test case 1:
    # value of parameter middleware is type 'function'
    # expected: return the value from method middleware of class MiddlewareMixin
    # with parameters is type 'function' and 'response'
    method_under_test = TestMiddlewareMixin()
    desired_output = "function"
    assert method_under_test.on_response(desired_output) == method_under_test.middleware("function", "response")

    # test case 2:
    # value of parameter middleware is type 'str'
    # expected: return partial object from method middleware of class MiddlewareMixin
    # with parameters is value 'response'
    method_under_test = TestMiddlewareMixin

# Generated at 2022-06-14 07:42:01.522087
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from types import ModuleType
    from sanic import Sanic
    from random import randint
    from datetime import datetime
    from time import time
    from os import getcwd, remove, path
    
    
    # Importing module
    module_path = path.abspath(path.join(getcwd(), 'middleware_mixin_tests.py'))
    module_spec = ModuleSpec(name='middleware_mixin_tests', loader=SourceFileLoader(name='middleware_mixin_tests', file_path=module_path))
    module = module_spec.loader.load_module()
    
    
    # Initializing class
    
    
    # Executing method
    app = Sanic()
    app.on_response(module.on_response_tests)
    response = app.get('/')


# Generated at 2022-06-14 07:42:09.489277
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Create an instance of MiddlewareMixin
    middleware_mixin = MiddlewareMixin()

    # Create a mock for the middleware
    mock_middleware = MagicMock(return_value = 'Middleware')

    # Call method middleware of MiddlewareMixin
    result = middleware_mixin.middleware(mock_middleware)

    # Assert if method middleware is not None
    assert result is not None

# Generated at 2022-06-14 07:42:19.529336
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Application(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.middleware_parameter = []
            self.middleware_request = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            f = middleware.middleware
            if middleware.attach_to == "request":
                self.middleware_request.append(f)
            else:
                self.middleware_parameter.append(f)

    @Application.middleware('parameter')
    async def to_uppercase(request, parameter):
        parameter = parameter.upper()
        return request, parameter

    @Application.middleware('request')
    async def to_lowercase(request):
        request = request

# Generated at 2022-06-14 07:42:31.197529
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')

    # test case:
    #  1. enable middleware
    #  2. iterate over middleware to check if middleware enabled
    #  3. disable middleware
    #  4. iterate over middleware to check if middleware make enabled
    test_middleware: List[str] = []

    @app.middleware
    def test_middleware_decorator(request):
        test_middleware.append('test_middleware_decorator')

    @app.middleware('response')
    def test_middleware_decorator2(request, response):
        test_middleware.append('test_middleware_decorator2')


# Generated at 2022-06-14 07:42:32.090111
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:42:44.816399
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic.exceptions import NotFound

    class A(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            pass

    def middleware1(request):
        return request

    def middleware2(request):
        if request.path == '/test':
            raise NotFound("test")
        return request

    a = A()
    a.middleware(middleware1, attach_to="request")
    a.middleware(middleware2, attach_to="request")
    assert a._future_middleware[0].middleware == middleware1
    assert a._future_middleware[0].attach_to == "request"
    assert a._future_middleware[1].middleware == middleware2
    assert a

# Generated at 2022-06-14 07:42:50.359177
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Application(MiddlewareMixin):
            def __init__(self):
                MiddlewareMixin.__init__(self)

            def _apply_middleware(self, middleware: FutureMiddleware):
                pass

    @Application.middleware
    async def before_request(request):
        pass

    assert before_request in Application()._future_middleware


# Generated at 2022-06-14 07:42:51.740172
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:43:02.945848
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class M:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa

    m = M()
    m2 = M()
    m3 = MiddlewareMixin()
    # assert m._apply_middleware(None) == m2._apply_middleware(None)
    assert m._future_middleware == m2._future_middleware
    assert m._future_middleware == m3._future_middleware

# Generated at 2022-06-14 07:43:04.598356
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # TODO: Add unit test for method middleware of class MiddlewareMixin
    pass


# Generated at 2022-06-14 07:43:11.747415
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    testApp = MiddlewareMixin()
    @testApp.middleware
    def testMiddleware(request):
        return request

    assert(len(testApp._future_middleware) == 1)
    assert(testApp._future_middleware[0].attach_to == "request")
    assert(testApp._future_middleware[0].middleware == testMiddleware)


# Generated at 2022-06-14 07:43:22.451047
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            assert middleware.attach_to == "request"

    t = TestMiddlewareMixin()
    t.middleware(middleware_or_request="request")
    t.middleware(middleware_or_request="response")
    t.middleware(middleware_or_request=lambda: None)



# Generated at 2022-06-14 07:43:23.862268
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass



# Generated at 2022-06-14 07:43:24.583870
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:43:38.497884
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    '''
    测试使用过程:
    1. 用 MiddlewareMixin 类构造一个类
    2. 执行这个应该被测试的方法
    3. 用 assert 来验证结果是否是正确的
    '''
    class Test(MiddlewareMixin):
        pass

    @Test.middleware
    def test_middleware():
        pass

    test_middleware.assert_called_with(test_middleware, 'request')

    @Test.on_response
    def test_on_response():
        pass


# Generated at 2022-06-14 07:43:46.510590
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class FakeMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    class FakeMiddleware():
        def __init__(self, middleware_or_request, attach_to):
            pass

    fmm = FakeMiddlewareMixin()

    fmm.middleware(FakeMiddleware)
    fmm.middleware(FakeMiddleware, attach_to="request")
    assert len(fmm._future_middleware) == 2


# Generated at 2022-06-14 07:43:58.488536
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Test:
        def __init__(self, *args, **kwargs):
            self._future_middleware: List[FutureMiddleware] = []
            self.middleware_or_request = None
            self.attach_to = None
            self.apply = None
            self.check = False
            self.result = None

        def _apply_middleware(self, middleware: FutureMiddleware):
            if self.apply:
                self.check = True

        def _register_middleware(self):
            nonlocal self
            future_middleware = FutureMiddleware(
                self.middleware_or_request, self.attach_to)
            self._future_middleware.append(future_middleware)
            if self.apply:
                self._apply_middleware(future_middleware)

            self.result = future

# Generated at 2022-06-14 07:44:03.023464
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.response import text

    middleware = MiddlewareMixin()

    @middleware.middleware
    async def mw(request):
        return text('works')

    mw = partial(mw, apply=False)

    mw()

# Generated at 2022-06-14 07:44:15.871543
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.futures import FutureMiddleware
    from sanic.testing import HOST, PORT
    from sanic.server import HttpProtocol
    from sanic import Sanic

    class MiddlewareMixinTester(Sanic, MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            self.middleware_called = False
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            self.middleware_called = True

    app = MiddlewareMixinTester(__name__)

    @app.middleware
    async def middleware(request, handler):
        pass

    # MiddlewareMixin.middleware must return middleware
    # thus we can use it this way:

# Generated at 2022-06-14 07:44:20.735902
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')
    app.middleware('request')(lambda request: request)
    app.middleware(lambda request: request)
    assert len(app._future_middleware) == 2

# Generated at 2022-06-14 07:44:33.257704
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.views import HTTPMethodView
    from sanic.response import text
    from sanic.request import Request

    class LoginView(HTTPMethodView):
        async def get(self, request):
            return text('Login Here')

        async def post(self, request):
            return text('Process Login')

    app = Sanic()
    app.add_route(LoginView.as_view(), '/login')

    # check middleware
    @app.middleware
    async def first_middleware(request):
        return request

    @app.middleware('response')
    async def second_middleware(request, response):
        return response

    assert isinstance(app._future_middleware[0].middleware, type(first_middleware))

# Generated at 2022-06-14 07:44:43.231853
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic()
    assert app.__dict__.get('_future_middleware', None) is None

    @app.middleware('request')
    async def before_request(request):
        pass

    assert app.__dict__.get('_future_middleware', None) is not None

# Generated at 2022-06-14 07:44:51.941787
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from unittest.mock import patch
    from sanic.app import Sanic
    from sanic.models import FutureMiddleware

    with patch.object(Sanic, "_apply_middleware", return_value=None) as mocked_method:
        app = Sanic()
        assert isinstance(app._future_middleware, list)
        app.middleware(attach_to="request")
        app.middleware(attach_to="response")
        app.middleware()
        app.middleware(lambda : None)
        app.middleware(apply=False)
        assert all(isinstance(item, FutureMiddleware) for item in app._future_middleware)
        assert mocked_method.call_count == 4


# Generated at 2022-06-14 07:45:05.740120
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text
    from sanic.models.futures import FutureMiddleware
    app = Sanic("test_MiddlewareMixin_middleware")

    fake_middleware = text("fake_middleware")

    # Middleware functions are usually in the format:
    # async def middleware(request):
    app.middleware(fake_middleware, attach_to = 'request')

    # get future_middleware
    future_middleware = app._future_middleware

    assert isinstance(future_middleware[0], FutureMiddleware)
    assert future_middleware[0].middleware == fake_middleware
    assert future_middleware[0].attach_to == 'request'
    assert not future_middleware[0].applied

    # fake_middleware has not applied in

# Generated at 2022-06-14 07:45:06.919692
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # FIXME
    pass

# Generated at 2022-06-14 07:45:18.043320
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    import sanic.request
    import sanic.response

    def _middleware(request, response):
        return response

    # The _middleware should be added to _future_middleware
    app = Sanic("sanic-server")
    app.middleware(_middleware)
    assert app._future_middleware == [FutureMiddleware(_middleware, "request")]

    app = Sanic("sanic-server")
    app.middleware(_middleware, attach_to="response")
    assert app._future_middleware == [FutureMiddleware(_middleware, "response")]


# Generated at 2022-06-14 07:45:23.285705
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    obj = MiddlewareMixin()
    obj.__init__()

    assert callable(obj.middleware) is True
    assert callable(obj.on_request) is True
    assert callable(obj.on_response) is True

# Generated at 2022-06-14 07:45:30.973870
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Server1(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(args, kwargs)

        def _apply_middleware(self, future_middleware: FutureMiddleware):
            return
    ms = Server1()
    @ms.middleware
    async def mw1(request):
        pass
    assert len(ms._future_middleware) == 1

# Generated at 2022-06-14 07:45:36.046037
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic(__name__)
    app.middleware(lambda x: x, attach_to="request")
    assert app._future_middleware == [FutureMiddleware(lambda x: x, 'request')]



# Generated at 2022-06-14 07:45:49.172053
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.utils import sanic_endpoint_test
    from sanic.app import Sanic
    from sanic.response import json

    def request_middleware(request):
        request.parsed_json = {"key": "value"}

    def response_middleware(request, response):
        response.headers["custom-header"] = "Custom header value"

    app = Sanic()

    @app.route("/")
    async def handler(request):
        return json({"received": True, "message": request.parsed_json})

    @app.middleware("request")
    def attach_value_middleware(request):
        request.processed_by_middleware = True

    app.request_middleware(request_middleware)
    app.response_middleware(response_middleware)

    request,

# Generated at 2022-06-14 07:45:53.956014
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    middleware_mixin = MiddlewareMixin()

    def middleware(*args, **kwargs):
        pass
    middleware_mixin.middleware(middleware)
    assert len(middleware_mixin._future_middleware) == 1


# Generated at 2022-06-14 07:46:13.864507
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from typing import Any
    from functools import partial
    from sanic.response import json

    class MiddlewareMixin_test(MiddlewareMixin):
        def __init__(self):
            self._future_middleware = []
            self.on_request(self.on_request_param)
            self.on_response(self.on_response_param)

        def _apply_middleware(self, middleware):
            pass

        async def on_request_param(  # noqa
            self, request: Any, attach_to: str = None  # noqa
        ):
            pass

        async def on_response_param(  # noqa
            self, request: Any, response: Any  # noqa
        ):
            pass

    m = MiddlewareMixin_test()

# Generated at 2022-06-14 07:46:26.444019
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic()

    from sanic.models.futures import FutureMiddleware

    @app.middleware
    def middleware1(request):
        pass

    @app.middleware('request')
    def middleware2(request):
        pass

    @app.middleware('response')
    def middleware3(request, response):
        pass

    # test add @app.middleware
    @app.middleware
    def middleware4(request):
        pass

    # test add @app.middleware('request')
    @app.middleware('request')
    def middleware5(request):
        pass

    # test add @app.middleware('response')
    @app.middleware('response')
    def middleware6(request, response):
        pass

   

# Generated at 2022-06-14 07:46:35.590062
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic("Test_MiddlewareMixin_middleware")
    def request(request):
        async def response(request, response):
            pass
        return response

    app.middleware(request)
    assert app._future_middleware[0] == FutureMiddleware(request, "request")

    app.middleware(request, attach_to="response")
    assert app._future_middleware[1] == FutureMiddleware(
            request, "response"
        )

# Generated at 2022-06-14 07:46:45.093897
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import sanic
    # create an app
    app = sanic.Sanic("test_MiddlewareMixin_middleware")
    # test `middleware` method
    @app.middleware('response')
    def method_response(request):
        return request

    assert isinstance(app.middleware, MiddlewareMixin)
    assert hasattr(app.middleware, '_future_middleware')
    assert len(app.middleware._future_middleware) == 1
    assert app.middleware._future_middleware[0].attach_to == "response"
    assert app.middleware._future_middleware[0].middleware.__name__ == method_response.__name__


# Generated at 2022-06-14 07:46:53.850509
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestClass(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    callable_test = lambda request, *args, **kwargs: request
    test = TestClass()
    test.middleware(callable_test, attach_to="request")
    assert test._future_middleware
    test.middleware(attach_to="request")(callable_test)
    assert test._future_middleware

# Generated at 2022-06-14 07:47:01.758630
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class App(MiddlewareMixin):
        pass

    app = App()
    middleware = lambda request: request
    app.middleware(middleware)
    app.middleware(middleware, 'response')
    app.middleware(middleware, 'request')
    assert app._future_middleware == [
        FutureMiddleware(middleware, 'request'),
        FutureMiddleware(middleware, 'response'),
        FutureMiddleware(middleware, 'request')
    ]

# Generated at 2022-06-14 07:47:08.118033
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """test function of method middleware of class MiddlewareMixin"""

    # instance
    from sanic.app import Sanic
    app = Sanic("test_MiddlewareMixin_middleware")

    # function
    @app.middleware("request")
    async def middleware_prepare_bundle(request):

        pass
    middleware_prepare_bundle(None)



# Generated at 2022-06-14 07:47:12.189581
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            return

    TestMiddlewareMixin().middleware(1, 2)

# Generated at 2022-06-14 07:47:17.393253
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app_test = Sanic("TestMiddlewareMixin")
    def test_middle_ware(request):
        print("test_middle_ware: request")

    app_test.middleware(test_middle_ware)
    assert len(app_test._future_middleware) == 1



# Generated at 2022-06-14 07:47:26.201482
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import HTTPResponse
    from sanic.models.futures import FutureMiddleware

    app = Sanic()

    @app.middleware
    def middleware(request):
        return HTTPResponse('This is a middleware.', status=200)

    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert app._future_middleware[0].middleware == middleware


# Generated at 2022-06-14 07:47:42.563694
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert 1==1


# Generated at 2022-06-14 07:47:47.429635
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert MiddlewareMixin.middleware("request")

    class TestMiddleware(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            pass

    t = TestMiddleware()
    assert t.middleware("request")

# Test for method on_request of class MiddlewareMixin

# Generated at 2022-06-14 07:47:49.460054
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass



# Generated at 2022-06-14 07:47:52.330512
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic("test_functional")
    assert app._future_middleware == []

# Generated at 2022-06-14 07:48:02.392207
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    sanic = Sanic(__name__)

    @sanic.middleware
    async def middleware_a(session):
        pass

    assert isinstance(middleware_a, partial)

    @sanic.middleware('response')
    async def middleware_b(session):
        pass

    assert isinstance(middleware_a, partial)

    @sanic.middleware()
    async def middleware_c(session):
        pass

    assert isinstance(middleware_a, partial)

    assert len(sanic._future_middleware) == 3



# Generated at 2022-06-14 07:48:09.365006
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic, BaseModel
    from sanic.models.base import ModelMeta

    app = Sanic()

    assert issubclass(Sanic, MiddlewareMixin)

    class TestModel(ModelMeta):
        @classmethod
        def middleware(cls, middleware_or_request, attach_to="request", apply=True):
            # This Class is callable, but not callable in
            # MiddlewareMixin.middleware
            assert False

    class MyModel(BaseModel):
        __middleware_builtin__ = TestModel

        @classmethod
        def middleware(cls, middleware_or_request, attach_to="request", apply=True):
            # This Class is callable, but not callable in
            # MiddlewareMixin.middleware
            assert False


# Generated at 2022-06-14 07:48:22.560426
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Test:
        def __init__(self):
            self._future_middleware = []

        def _apply_middleware(self, middleware):
            pass
    test = Test()
    test.middleware = MiddlewareMixin.middleware.__get__(test)
    test.on_request = MiddlewareMixin.on_request.__get__(test)
    test.on_response = MiddlewareMixin.on_response.__get__(test)
    assert len(test._future_middleware) == 0
    @test.on_request
    async def test1(request, *args, **kwargs):
        return request
    assert len(test._future_middleware) == 1
    assert test._future_middleware[0].middleware == test1
    assert test._future_middleware[0].attach

# Generated at 2022-06-14 07:48:28.423795
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')

    app.middleware('request')(print)

    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].attach_to == 'request'


# Generated at 2022-06-14 07:48:39.947534
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_test:
        def __init__(self, *args, **kwargs):
            self._future_middleware = []

    class FutureMiddleware:
        def __init__(self, middleware, attach_to):
            self.middleware = middleware
            self.attach_to = attach_to

    middleware_mixin = MiddlewareMixin()
    record = {}

    @middleware_mixin.middleware
    def mw_test(request):
        record["called"] = True

    request = {}
    @middleware_mixin.middleware('response')
    def mw_test2(request, response):
        record["called-response"] = True
        return response

    middleware_mixin._future_middleware = []

# Generated at 2022-06-14 07:48:54.041495
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.websocket import WebSocketProtocol, ConnectionClosed
    from sanic.server import HttpProtocol

    class TestGlobalMiddle(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            print('applied')

    async def async_middleware_handler(request):
        return HTTPResponse(b'OK')

    handler_func = async_middleware_handler

    middleware = TestGlobalMiddle()
    assert len(middleware._future_middleware) == 0

    # test: @middleware
    middleware.middleware(handler_func)
    assert len(middleware._future_middleware) == 1

    # test: @middleware('request')
    middle

# Generated at 2022-06-14 07:49:31.147774
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Test:
        def test_fn(self):
            pass

    res = Test()
    res.test_fn = MiddlewareMixin.middleware(res.test_fn)

    assert callable(res.test_fn)
    assert res.test_fn.__name__ == 'test_fn'
    assert res.test_fn.__qualname__ == 'Test.test_fn'


# Generated at 2022-06-14 07:49:38.291800
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic.exceptions import ServerError

    def middleware(request):
        #do something through request
        return json({"ok": True})

    app = Sanic(__name__)
    app.middleware(middleware)
    request, response = app.test_client.get('/')
    assert response.json == {"ok": True}



# Generated at 2022-06-14 07:49:48.509154
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic('middleware_mixin_test')
    assert len(app._future_middleware) == 0

    @app.middleware
    async def foo(request):
        pass

    @app.middleware('request')
    async def foo1(request):
        pass

    @app.middleware('response')
    async def foo2(request, response):
        pass

    assert len(app._future_middleware) == 3
    assert app._future_middleware[0].attach_to == "request"
    assert app._future_middleware[1].attach_to == "request"
    assert app._future_middleware[2].attach_to == "response"


# Generated at 2022-06-14 07:49:49.037986
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:49:57.917042
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.middleware import ErrorMiddleware, NormalizeMiddleware

    """
    This function was created for testing the method middleware of class MiddlewareMixin
    """
    app = Sanic("MiddlewareMixin_test")
    app_test = MiddlewareMixin("MiddlewareMixin_test")
    test_middleware = lambda request: request
    assert app_test.middleware(test_middleware, "request") == test_middleware
    assert app_test._future_middleware != []
    assert app_test._future_middleware[0].middleware == test_middleware
    app_test.middleware(ErrorMiddleware)
    assert app_test._future_middleware[1].middleware == ErrorMiddleware
    app_test.middleware(NormalizeMiddleware)
    assert app

# Generated at 2022-06-14 07:50:00.760853
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        pass

    tmm = TestMiddlewareMixin()
    print(tmm._future_middleware)

# Generated at 2022-06-14 07:50:07.918574
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text
    sanic_app = Sanic(__name__)
    def before_request(request):
        return text('response')

    @sanic_app.middleware(before_request)
    def test():
        return None

    assert len(sanic_app._future_middleware) == 1
    assert sanic_app._future_middleware[0].middleware == before_request


# Generated at 2022-06-14 07:50:08.751185
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass
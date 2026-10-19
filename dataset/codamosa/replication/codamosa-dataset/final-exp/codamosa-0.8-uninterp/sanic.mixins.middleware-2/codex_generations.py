

# Generated at 2022-06-14 07:40:13.360890
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic()

    @app.middleware()
    def process_response(request, response):
        pass

    assert app._future_middleware[0].middleware == process_response
    assert app._future_middleware[0].attach_to == 'request'

    @app.middleware(attach_to='response')
    def process_response(request, response):
        pass

    assert app._future_middleware[1].middleware == process_response
    assert app._future_middleware[1].attach_to == 'response'

# Generated at 2022-06-14 07:40:14.234664
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:40:21.662548
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic(__name__)

    @app.middleware
    async def test_middleware(request):
        """Middleware docstring"""
        return "test"

    assert app._future_middleware[0].middleware == test_middleware
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].attach_to == "request"



# Generated at 2022-06-14 07:40:34.139190
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic("test_MiddlewareMixin_middleware")

    @app.middleware("request")
    async def handler_request_1(request):
        pass

    @app.middleware("request")
    async def handler_request_2(request):
        pass

    @app.middleware("response")
    async def handler_response_1(request, response):
        pass

    @app.middleware("response")
    async def handler_response_2(request, response):
        pass

    assert app._future_middleware[0].middleware == handler_request_1
    assert app._future_middleware[1].middleware == handler_request_2
    assert app._future_middleware[2].middleware == handler_response_1
    assert app._future_middleware

# Generated at 2022-06-14 07:40:47.792374
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse

    app = Sanic(__name__)


    # without function 'middleware'
    def test_on_request(request: Request):
        return HTTPResponse(text="This is a test", status=200)

    app.add_route(test_on_request, "/", methods=["GET"])

    request, response = app.test_client.get("/")

    assert response.text == "This is a test"
    assert response.status == 200


    # with function 'middleware'
    def on_request(request: Request):
        request["processed_by"] = "on_request"


# Generated at 2022-06-14 07:40:57.566182
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text
    from sanic.models.middleware import Middleware
    from sanic.models.futures import MiddlewareFuture
    from sanic.models.futures import FutureMiddleware
    from sanic.models.futures import FutureConditional
    from sanic.models.futures import ConditionalType

    app = Sanic('test_MiddlewareMixin')

    @app.middleware
    def method_middleware(request):
        return text('Pass')

    assert hasattr(app, '_future_middleware')
    assert isinstance(app._future_middleware, list)
    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)


# Generated at 2022-06-14 07:41:10.731808
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')

    from functools import partial, update_wrapper
    from typing import Callable, List

    from sanic.models.futures import Future, FutureMiddleware

    app.reusable = True

    # app.middleware(middleware_or_request, *args, **kwargs)
    # app.on_request(middleware=None)
    # app.on_response(middleware=None)

    from sanic.exceptions import (
        PayloadTooLarge,
        ServerError,
        URLBuildError,
        InvalidUsage,
    )

    # 装饰器用法

# Generated at 2022-06-14 07:41:24.045205
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware):
            raise NotImplementedError

    middleware_mixin = MiddlewareMixin_()
    # test for @middleware
    @middleware_mixin.middleware
    def middleware_fun(request, response):
        pass

    assert middleware_mixin._future_middleware[0].middleware == middleware_fun
    assert middleware_mixin._future_middleware[0].attach_to == 'request'
    # test for @middleware('request')

# Generated at 2022-06-14 07:41:37.415325
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic(__name__)

    @app.middleware
    async def middleware(request, handler):
        return await handler(request)

    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0].middleware, types.FunctionType)
    assert app._future_middleware[0].attach_to == "request"

    app2 = Sanic(__name__)

    @app2.middleware("request")
    async def middleware(request, handler):
        return await handler(request)

    assert len(app2._future_middleware) == 1
    assert isinstance(app2._future_middleware[0].middleware, types.FunctionType)

# Generated at 2022-06-14 07:41:44.801760
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test')
    print('\n')
    print('Unit test for method middleware of class MiddlewareMixin')
    assert isinstance(app, MiddlewareMixin)
    app.middleware(middleware_or_request = 'request')
    print('*** Method middleware of Class MiddlewareMixin works well ***')


# Generated at 2022-06-14 07:41:58.513617
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    n = MiddlewareMixin()
    n.middleware(middleware_or_request=partial(lambda x, y: x+y), attach_to='request')
    n.middleware(middleware_or_request=partial(lambda x, y: x*y), attach_to='response')
    assert len(n._future_middleware) == 2
    assert str(n._future_middleware[0]) == '<Middleware [<function <lambda> at 0x000001809E8A8AE8>] @request>'
    assert str(n._future_middleware[1]) == '<Middleware [<function <lambda> at 0x000001809E8A8AE8>] @response>'


# Generated at 2022-06-14 07:42:05.942421
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.response import json
    from sanic import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware
    async def with_middleware(request):
        return json({"middleware": "working"})
    request, response = app.test_client.get('/')
    assert response.json == {'middleware': 'working'}


# Generated at 2022-06-14 07:42:15.260065
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A(MiddlewareMixin):
        def __init__(self):
            super().__init__()
    
    a = A()
    a.middleware('a')
    assert a._future_middleware[0].middleware == 'a'

    a.middleware('b', 'a')
    assert a._future_middleware[1].middleware == 'b'
    assert a._future_middleware[1].attach_to == 'a'

    def b(middle='b'):
        return middle
    a.middleware(b, 'b')
    assert a._future_middleware[2].middleware('') == 'b'
    assert a._future_middleware[2].attach_to == 'b'


test_MiddlewareMixin_middleware()

# Generated at 2022-06-14 07:42:28.659410
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.models.futures import FutureMiddleware
    from sanic.websocket import WebSocketProtocol

    from random import randint
    from string import ascii_letters

    def _fake_middleware(request: Request):
        return HTTPResponse(b'fake_middleware')

    def _fake_middleware_with_num(request: Request, num: int):
        return HTTPResponse(b'fake_middleware_with_num')

    def _fake_middleware_with_str(request: Request, str: str):
        return HTTPResponse(b'fake_middleware_with_str')


# Generated at 2022-06-14 07:42:29.502710
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:42:42.976973
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    
    from sanic.app import Sanic

    app = Sanic()

    # Create mock object of middleware
    class FutureMiddlewareMock(object):
        pass
    class MiddlewareMock(object):
        pass

    middleware_mock = MiddlewareMock()
    future_middleware_mock = FutureMiddlewareMock()

    # Mock method _apply_middleware
    def _apply_middleware_mock(self, middleware):
        #print("Mock middleware")
        pass
    app._apply_middleware = _apply_middleware_mock

    # Mock method _future_middleware
    app._future_middleware = []

    app.middleware(middleware_mock, apply=True)
    
    #print("Future middleware length: " + str(len(app._future_

# Generated at 2022-06-14 07:42:49.349227
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MyMiddleware:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.name = "MiddlewareMixin's middleware"
    instance = MiddlewareMixin()
    result = instance.middleware(MyMiddleware)
    assert isinstance(result, MyMiddleware)


# Generated at 2022-06-14 07:42:50.165593
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:43:00.943088
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    mm=MiddlewareMixin()
    with pytest.raises(NotImplementedError):
        mm._apply_middleware(FutureMiddleware(None,None))
    @mm.middleware
    def middleware1(request): pass

    @mm.middleware()
    def middleware2(request): pass

    @mm.middleware
    def middleware3(request): pass

    assert mm._future_middleware[0].handler==middleware3
    assert mm._future_middleware[1].handler==middleware2
    assert mm._future_middleware[2].handler==middleware1

# Generated at 2022-06-14 07:43:11.284767
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    try:
        class TestMiddlewareMixin(MiddlewareMixin):
            def _apply_middleware(self, middleware: FutureMiddleware):
                pass
    except NotImplementedError:
        assert False, "_apply_middleware must be implemented"

    app = TestMiddlewareMixin()
    assert len(app._future_middleware) == 0

    @app.middleware('request')
    def middleware(request):
        return request

    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].middleware == middleware
    assert app._future_middleware[0].attach_to == "request"

    @app.on_response
    def on_response(request, response):
        return response

    assert len(app._future_middleware) == 2
    assert app._

# Generated at 2022-06-14 07:43:21.310137
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Temp(MiddlewareMixin):
        def __init__(self):
            super().__init__()
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    instance = Temp()
    instance.middleware(middleware_or_request="some_request", apply=True)


# Generated at 2022-06-14 07:43:32.708930
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic(__name__)
    assert hasattr(app, 'middleware')

    def middleware1(request, response):
        return response
    app.middleware(middleware1)
    assert len(app._future_middleware) == 1

    app2 = Sanic(__name__)
    @app2.middleware('request')
    def middleware2(request):
        return request

    @app2.middleware
    def middleware3(request, response):
        return response
    assert len(app2._future_middleware) == 2


# Generated at 2022-06-14 07:43:41.292625
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    app = MiddlewareMixin()
    # call method middleware
    n = app.middleware(middleware_or_request=1)
    assert n == partial(app.middleware, attach_to=1)
    # call method middleware directly
    n = app._future_middleware
    assert n == []
    app._apply_middleware(1)
    # call method middleware
    @app.middleware(middleware_or_request=1)
    def test_callable():
        return 1
    n = app._future_middleware
    assert len(n) == 1
    n = n[0].decorator
    assert n == test_callable
    # call method middleware
    @app.middleware(attach_to="request")
    def test_callable():
        return 1
    n = app

# Generated at 2022-06-14 07:43:51.451443
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic()
    assert(app._future_middleware == [])
    f = lambda: True
    app.middleware()(f)
    assert(len(app._future_middleware) == 1)
    assert(app._future_middleware[0].middleware is f)
    assert(app._future_middleware[0].attach_to == "request")
    assert(app._future_middleware[0].execute_before_request)
    g = lambda: True
    app.middleware("response")(g)
    assert(len(app._future_middleware) == 2)
    assert(app._future_middleware[1].middleware is g)
    assert(app._future_middleware[1].attach_to == "response")

# Generated at 2022-06-14 07:43:52.223512
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert True

# Generated at 2022-06-14 07:43:57.049441
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware('request')
    async def test_middleware(request):
        return request
    assert 'test_middleware' in app.middlewares['request']


# Generated at 2022-06-14 07:44:10.153250
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            self._future_middleware = []
            super().__init__(*args, **kwargs)
        
        def _apply_middleware(self, middleware):
            return middleware.middleware
    
    test_middleware_mixin = TestMiddlewareMixin()
    expect_future_middleware_list_len = len(test_middleware_mixin._future_middleware)+1
    def test_middleware1(request):
        return "test_middleware1 is called"
    @test_middleware_mixin.middleware('request')
    def test_middleware2(request):
        return "test_middleware2 is called"


# Generated at 2022-06-14 07:44:15.485061
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        pass

    temp = TestMiddlewareMixin()
    assert len(temp._future_middleware) == 0

    middleware_func = lambda x, request, func: func
    middleware_request_func = lambda x, request, func: func
    middleware_response_func = lambda x, request, func: func

    temp.middleware(middleware_func, attach_to="request")
    temp.middleware(middleware_response_func, attach_to="response")
    temp.middleware(middleware_request_func, attach_to="request")

    assert len(temp._future_middleware) == 3

    # temp.middleware(middleware_func, attach_to="request")

    middleware_func.__name__ = "middleware_func"
   

# Generated at 2022-06-14 07:44:22.999232
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    test_middleware_mixin_object = TestMiddlewareMixin()
    @test_middleware_mixin_object.middleware
    def middleware_example(request):
        print("Hello")
    assert len(test_middleware_mixin_object._future_middleware)==1


# Generated at 2022-06-14 07:44:34.554639
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import unittest
    from unittest import mock
    from  sanic.models.base import MiddlewareMixin

    class MM(MiddlewareMixin):
        pass

    mm = MM()

    mock_callable = mock.Mock()

    mm.middleware(mock_callable)
    assert mm._future_middleware[0].middleware is mock_callable
    assert mm._future_middleware[0].attach_to == "request"

    mm.middleware(mock_callable, attach_to="response")
    assert mm._future_middleware[1].middleware is mock_callable
    assert mm._future_middleware[1].attach_to == "response"

    mm.middleware(attach_to="request")(mock_callable)

# Generated at 2022-06-14 07:44:50.895567
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Test_MiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            self._future_middleware = []
            self._apply_middleware = None

        def _apply_middleware(self, future_middleware):
            return future_middleware

        def test_register_middleware(self, middleware, attach_to="request"):
            nonlocal apply
            future_middleware = FutureMiddleware(middleware, attach_to)
            self._future_middleware.append(future_middleware)
            if apply:
                self._apply_middleware(future_middleware)
            return middleware
    instance = Test_MiddlewareMixin()
    def some_middleware():
        pass
    assert instance.middleware(some_middleware, attach_to='request') == some_middleware



# Generated at 2022-06-14 07:44:56.357383
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        @MiddlewareMixin.middleware
        def _apply_middleware(*args, **kwargs):
            pass

    a = A()
    assert a._apply_middleware is not None

# Generated at 2022-06-14 07:45:08.944980
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.exceptions import SanicException

    app=Sanic()
    assert app._future_middleware==[]

    def middleware(request):
        pass

    app.middleware(middleware,attach_to='request',apply=True)
    # print('app._future_middleware',app._future_middleware)
    assert len(app._future_middleware)==1

    middleware2=FutureMiddleware(middleware,attach_to='request')
    app._future_middleware.append(middleware2)
    # print('app._future_middleware',app._future_middleware)
    assert len(app._future_middleware)==2

    app.middleware(middleware,attach_to='response',apply=True)
    # print('app._future_

# Generated at 2022-06-14 07:45:21.618823
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text
    from sanic.server import HttpProtocol
    app = Sanic(__name__)
    @app.middleware
    async def on_request(request):
        pass
    @app.middleware('request')
    async def on_request_2(request):
        pass
    @app.middleware
    def on_response(request, response):
        pass
    @app.middleware('response')
    def on_response_2(request, response):
        pass
    request, response = app.request_middleware[0]('request', 'response')
    request, response = app.response_middleware[0]('request', 'response')
    request, response = app.request_middleware[1]('request', 'response')
    request, response

# Generated at 2022-06-14 07:45:23.475700
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert False
    # TODO: implement


# Generated at 2022-06-14 07:45:35.308060
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import text
    import asyncio

    app = Sanic("app_sanic")
    request_calls = []
    response_calls = []

    @app.middleware("request")
    async def before_request_middleware(request):
        request_calls.append(1)

    @app.middleware("response")
    async def after_request_middleware(request, response):
        response_calls.append(1)

    @app.route("/")
    async def handler(request):
        return text("OK")

    client = app.test_client

    # first call
    request, response = client.get("/")
    assert len(request_calls) == 1
    assert len(response_calls) == 1

    request,

# Generated at 2022-06-14 07:45:48.524525
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # creating an app and assinging it to a variable app
    app = Sanic('test_sanic_router')
    # creating an instance of MiddlewareMixin
    m_instance = MiddlewareMixin(app)
    # creating a middleware with a decorator
    @app.middleware
    def mware1(request):
        pass
    # creating a middleware with a decorator
    @app.middleware('request')
    def mware2(request):
        pass
    # creating a middleware with a decorator
    @app.middleware('response')
    def mware3(request, response):
        pass
    # testing if the list _future_middleware is not empty
    assert m_instance._future_middleware
    # testing the length of the list _future_middleware

# Generated at 2022-06-14 07:45:59.282995
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class DummyFeature(MiddlewareMixin):
        pass

    dummy_feature = DummyFeature()
    assert dummy_feature._future_middleware == []
    # Test case 1: attach_to == 'request'.
    dummy_feature.middleware(lambda request, *args, **kwargs: None)
    assert dummy_feature._future_middleware == [
        FutureMiddleware(
            lambda request, *args, **kwargs: None, attach_to="request"
        )
    ]
    # Test case 2: attach_to == 'response'.
    dummy_feature.middleware(lambda request, response, *args, **kwargs: None)

# Generated at 2022-06-14 07:46:05.148229
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    sanic_app = Sanic('test')

    def middleware(request):
        pass

    sanic_app.middleware(middleware)

    assert sanic_app.__dict__['_future_middleware'] == [FutureMiddleware(middleware, "request")]


# Generated at 2022-06-14 07:46:12.117363
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A():
        def __init__(self):
            pass
        async def middleware_1(self):
            pass
        async def middleware_2(self):
            pass
    a = A()
    a.middleware(a.middleware_1, "request")
    a.middleware(a.middleware_1, "response")
    a.middleware(a.middleware_2, "request")
    a.middleware("request", a.middleware_1)
    a.middleware("response", a.middleware_1)
    a.middleware("request", a.middleware_2)
    a.middleware(a.middleware_1)
    a.middleware(a.middleware_2)



# Generated at 2022-06-14 07:46:32.950588
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class App(MiddlewareMixin):
        def __init__(self):
            super().__init__()
            pass

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    app = App()

    def middleware(request):
        pass

    @app.middleware
    def middleware_without_params():
        pass

    @app.middleware('request')
    def middleware_request(request):
        pass

    @app.middleware('response')
    def middleware_response(request, response):
        pass

    app.middleware(middleware, apply=False)

    assert(len(app._future_middleware) == 4)
    assert(app._future_middleware[0].middleware == middleware_without_params)

# Generated at 2022-06-14 07:46:44.650683
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    print("test_MiddlewareMixin_middleware")

    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            pass

    tmm = TestMiddlewareMixin()

    # Test: call with one parameter
    def middleware(request):
        return request

    tmm.middleware(middleware, "request")

    # Test: call with two parameters
    tmm.middleware(middleware)

    # Test: call with two parameters, one at a time
    tmm.middleware(middleware, "request")

    # Test: call with one parameter, attach_to
    def middleware_attach(response):
        return response

    tmm.middleware(middleware_attach, "response")

    return


# Generated at 2022-06-14 07:46:45.957183
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:46:59.078345
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixinTester(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(MiddlewareMixinTester, self).__init__(*args, **kwargs)
            self.cnt_middleware_request = 0
            self.cnt_middleware_response = 0

        def _apply_middleware(self, middleware: FutureMiddleware):
            if middleware.attach_to == "request":
                self.cnt_middleware_request += 1
            if middleware.attach_to == "response":
                self.cnt_middleware_response += 1

    m = MiddlewareMixinTester()
    m.on_request()(lambda x: x)
    m.on_response()(lambda x: x)
    m.on_request()

# Generated at 2022-06-14 07:47:01.667813
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    test = MiddlewareMixin()
    assert len(test._future_middleware) == 0
    test.middleware(middleware_or_request=None)
    assert len(test._future_middleware) == 1

# Generated at 2022-06-14 07:47:11.058278
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Arrange
    class TestMiddleware():
        pass

    dummy_mw = TestMiddleware()

    class DummyApp():
        pass
    
    dummy_app = DummyApp()
    dummy_app.middleware = MiddlewareMixin.middleware.__get__(dummy_app)
    # Act
    dummy_app.middleware(dummy_mw, attach_to="request")
    # Assert
    assert len(dummy_app._future_middleware) == 1
    assert dummy_app._future_middleware[0].middleware is dummy_mw


# Generated at 2022-06-14 07:47:18.608915
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    # testing if the parameter attach_to is properly assigned
    app = Sanic(__name__)

    @app.middleware(attach_to = "request")
    def request_middleware(request):
        pass

    @app.middleware
    def normal_middleware(request):
        pass

    assert len(app._future_middleware) == 2
    assert app._future_middleware[0].attachment_type == "request"
    assert app._future_middleware[1].attachment_type == "request"


# Generated at 2022-06-14 07:47:31.865038
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class DummyRequest:
        def __init__(self):
            self.headers = {}

        def update_headers(self, headers: dict):
            self.headers.update(headers)

    class DummyResponse:
        def __init__(self, response_text: str):
            self.response_text = response_text

    class DummySanic:
        def __init__(self):
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            self._future_middleware.append(middleware)

    dummy_request = DummyRequest()
    dummy_response = DummyResponse("response")

    def dummy_request_middleware(request: DummyRequest):
        request.update_headers({'key1': 'value1'})
        return request


# Generated at 2022-06-14 07:47:45.645154
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # create a class and mock it
    class MiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            MiddlewareMixin.__init__(self, *args, **kwargs)
        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa

    # create a class and mock it
    class FutureMiddleware:
        def __init__(self, middleware, attach_to):
            pass
        def append(self, future_middleware):
            pass

    # create a class and mock it
    class Partial:
        def __init__(self, partial, attach_to):
            pass

    # create a class and mock it

# Generated at 2022-06-14 07:47:49.504475
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    import sanic

    app = sanic.Sanic()

    def midd_func(request):
        return 

    app.middleware(midd_func)


# Generated at 2022-06-14 07:48:13.913752
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert MiddlewareMixin.middleware is not None



# Generated at 2022-06-14 07:48:24.324073
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.log import log
    from sanic.request import Request, RequestParameters

    request = Request(
        "POST",
        "/test",
        parameters=RequestParameters(),
        headers={},
        version=(1, 1),
        app=Sanic("test"),
    )

    class TestMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            log.info(middleware)

    test_mixin = TestMixin()

    def test_function(request):
        pass

    @test_mixin.middleware
    def test_function(request):
        pass

    test_mixin.middleware(test_function)
    assert test_mixin._future_middleware[0].middleware == test_function
    assert test

# Generated at 2022-06-14 07:48:31.512422
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic()
    assert isinstance(app, MiddlewareMixin)

    @app.middleware
    def auth(request):
        return None

    assert len(app._future_middleware) > 0
    assert isinstance(app._future_middleware[0], FutureMiddleware)


# Generated at 2022-06-14 07:48:41.328677
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """
    Unit test MiddlewareMixin.middleware
    """
    # Initialize test variables
    class T(MiddlewareMixin):
        def __init__(self):
            self.middleware = MiddlewareMixin.middleware

    # Create an instance of T
    t = T()

    # Using t.middleware, define "@middleware"
    @t.middleware
    def middleware_decorator(request):
        return request

    # The middleware_decorator must be of type FutureMiddleware
    # Otherwise, it will fail the test
    assert isinstance(middleware_decorator, FutureMiddleware)
    # The attr of middleware_decorator must be 'request'
    # Otherwise, it will fail the test
    assert middleware_decorator.attach_to == 'request'
    #

# Generated at 2022-06-14 07:48:44.219911
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_Sanic_middleware')
    a = app.middleware(None, 'request')
    print(a)

# Generated at 2022-06-14 07:48:58.275341
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    class TestApp:
        def __init__(self):
            self.middleware_mixin = TestMiddlewareMixin()

    @TestApp.middleware()
    def test_request_middleware(request):
        pass

    @TestApp.middleware(attach_to='response')
    def test_response_middleware(request, response):
        pass

    assert len(TestApp.middleware_mixin._future_middleware) == 2
    for mdw in TestApp.middleware_mixin._future_middleware:
        if mdw._name == 'test_request_middleware':
            assert mdw._attach_to == 'request'

# Generated at 2022-06-14 07:49:10.712598
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import text
    from sanic.utils import sanic_endpoint_test
    from sanic.views import CompositionView
    
    app = Sanic('test_MiddlewareMixin_middleware')
    class MyMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            print('***************_apply_middleware()***************')

    class MySanic(MyMiddlewareMixin, Sanic):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


# Generated at 2022-06-14 07:49:15.345497
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    f_v = 0
    def f():
        nonlocal f_v
        f_v += 1
    s = Sanic('test')
    s.middleware(f)
    assert f_v == 1
    m = s.middleware()
    assert callable(m)
    m(f)
    assert f_v == 2


# Generated at 2022-06-14 07:49:28.368921
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic(__name__)

    @app.middleware
    def test1(request):
        pass

    @app.middleware()
    def test2(request):
        pass

    @app.middleware('request')
    def test3(request):
        pass

    @app.middleware('response')
    def test4(request):
        pass

    assert len(app._future_middleware) == 4
    assert app._future_middleware[0].middleware == test1
    assert app._future_middleware[0].attach_to == 'request'
    assert app._future_middleware[1].middleware == test2
    assert app._future_middleware[1].attach_to == 'request'
    assert app._future_middleware[2].middleware

# Generated at 2022-06-14 07:49:32.241886
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    object = MiddlewareMixin()
    object.middleware(middleware=None)
    object.on_request(middleware=None)
    object.on_response(middleware=None)
    #object._apply_middleware(FutureMiddleware(middleware=None, attach_to="request"))
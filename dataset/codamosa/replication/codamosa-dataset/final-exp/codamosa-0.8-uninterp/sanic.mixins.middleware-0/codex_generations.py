

# Generated at 2022-06-14 07:40:16.901950
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic("MiddlewareMixin")

    @app.middleware("request")
    async def handler(request):
        return request

    assert handler == app._future_middleware[0].middleware
    assert app._future_middleware[0].attach_to == "request"
    assert app._apply_middleware.__name__ == "_apply_middleware"



# Generated at 2022-06-14 07:40:20.316534
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('request')
    async def request_middleware(request):
        pass

    @app.middleware('response')
    async def response_middleware(request, response):
        pass

    assert len(app._future_middleware) == 2



# Generated at 2022-06-14 07:40:34.139129
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    class TestingMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa

    app = TestingMiddlewareMixin()
    m = app.middleware(middleware_or_request='request', attach_to="request", apply=True)
    with mock.patch('sanic.models.futures.FutureMiddleware', return_value = FutureMiddleware):
        assert m == FutureMiddleware(m, "request")
    m = app.middleware(middleware_or_request=lambda: None, attach_to="request", apply=True)


# Generated at 2022-06-14 07:40:45.210607
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Given
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(
            self, middleware: FutureMiddleware
        ):
            pass

    TestMiddlewareMixin()
    TestMiddlewareMixin._apply_middleware = MagicMock()
    TestMiddlewareMixin._future_middleware = MagicMock()
    # When
    TestMiddlewareMixin.middleware(MagicMock())
    # Then
    assert TestMiddlewareMixin._apply_middleware.call_count == 1
    assert TestMiddlewareMixin._future_middleware.append.call_count == 1


# Generated at 2022-06-14 07:40:53.920467
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')
    # Second param is attach_to
    # when attach_to isn't 'request' or 'response'.
    # will raise TypeError
    try:
        @app.middleware('test')
        def m1(request):
            pass
        assert False
    except TypeError as e:
        assert "Test is not a valid attachment target" in str(e)


# Generated at 2022-06-14 07:41:06.377137
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            pass

    a = A()
    def m0():
        pass
    def m1():
        pass

    # middleware can accept 2 params
    a.middleware(m0, attach_to="request", apply=True)
    a.middleware(m1, apply=True)
    # middleware can accept 1 param
    a.middleware(m0)
    a.middleware(m1)
    # middleware can accept 0 param
    # middleware will be decorated by default
    a.middleware()(m0)
    a.middleware()(m1)
    # middleware can accept 0 param
    # middleware will be decorated by default (attach_to="request")

# Generated at 2022-06-14 07:41:15.982908
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super().__init__()

        def _apply_middleware(self, middleware):
            pass

    test_results = []

    # Test case: normal register
    def test_logger1(request):
        return request

    def test_logger2(request):
        return request

    @TestMiddlewareMixin().middleware
    def test_logger3(request):
        return request

    test_results.append(
        TestMiddlewareMixin()._future_middleware[0].middleware == test_logger1
    )

    @TestMiddlewareMixin().middleware("request")
    def test_logger4(request):
        return request


# Generated at 2022-06-14 07:41:20.342843
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class UnitTest(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            assert isinstance(middleware, FutureMiddleware)

    app = UnitTest()
    @app.middleware
    def test_function(request):
        pass


# Generated at 2022-06-14 07:41:23.141756
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    obj = MiddlewareMixin()

    # Testing: test if the method MiddlewareMixin.middleware can be called
    @obj.middleware('request')
    def test_middleware():
        pass



# Generated at 2022-06-14 07:41:28.523263
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    m = MiddlewareMixin()
    # test case with one argument
    response = m.middleware(lambda request, handler: 'success')
    assert response == 'success'
    # test case with two arguments
    response = m.middleware('request', apply=False)(lambda request, handler: 'success')
    assert response == 'success'
    # test case with two arguments in another order
    response = m.middleware('response', lambda request, handler: 'failed', False)
    assert response == 'failed'


# Generated at 2022-06-14 07:41:33.252921
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    @MiddlewareMixin.middleware({"123"}, True)
    def func():
        pass

    assert func() == "123"


# Generated at 2022-06-14 07:41:45.101666
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware
    async def middleware(request):
        return request

    @app.route('/')
    async def handler(request):
        return text('OK')

    request, response = app.test_client.get('/')

    assert response.text == 'OK'


if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils import *

    test_MiddlewareMixin_middleware()

# Generated at 2022-06-14 07:41:51.063577
# Unit test for method middleware of class MiddlewareMixin

# Generated at 2022-06-14 07:42:02.878745
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import sys
    import pytest
    from sanic.exceptions import SanicException
    from sanic.log import logger
    from sanic import Sanic
    from sanic.models.futures import FutureMiddleware

    sys.modules["sanic"].exceptions.SanicException = SanicException
    sys.modules["sanic"].log.logger = logger
    del sys.modules["sanic"].log.logger

    app = Sanic()

    sut = MiddlewareMixin(app)

    @sut.on_request(middleware=None)
    def test_middleware():
        pass

    assert isinstance(sut._future_middleware[0], FutureMiddleware)

# Generated at 2022-06-14 07:42:04.179756
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:42:06.267060
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import json
    pass


# Generated at 2022-06-14 07:42:17.064132
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from utils import SanicTestClient

    app = SanicTestClient()

    # Test for middleware
    assert len(app._future_middleware) == 0
    app.middleware(lambda request: None, attach_to="request", apply=False)
    assert len(app._future_middleware) == 1

    # Test for on_request
    assert len(app._future_middleware) == 1
    app.on_request(lambda request: None)
    assert len(app._future_middleware) == 2

    # Test for on_response
    assert len(app._future_middleware) == 2
    app.on_response(lambda request: None)
    assert len(app._future_middleware) == 3

# Generated at 2022-06-14 07:42:18.367077
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert MiddlewareMixin()

# Generated at 2022-06-14 07:42:28.248928
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        pass

    test_middleware_mixin = TestMiddlewareMixin()
    test_middleware_mixin.middleware(lambda x: x)
    test_middleware_mixin.middleware(lambda x: x, "request")
    test_middleware_mixin.middleware(lambda x: x, "response")

    test_middleware_mixin.on_request(lambda x: x)
    test_middleware_mixin.on_response(lambda x: x)


# Generated at 2022-06-14 07:42:41.790450
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import copy

    from tempfile import NamedTemporaryFile
    from unittest import mock

    from sanic.models.futures import FutureMiddleware

    from sanic.server import HttpProtocol
    from sanic.router import Router
    from sanic.response import HTTPResponse

    sanic_app = mock.Mock()

    sanic_app.configure_logging = mock.Mock()
    sanic_app.handle_request = mock.Mock()
    sanic_app.router = Router()
    sanic_app.error_handler = mock.Mock()
    sanic_app.listeners = mock.Mock()
    sanic_app.blueprints = mock.Mock()
    sanic_app.before_start = mock.Mock()
    sanic_app.after

# Generated at 2022-06-14 07:42:49.244139
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models.futures import FutureMiddleware
    app = Sanic()
    assert len(app._future_middleware) == 0
    def m():
        pass
    app.middleware(m, 'request')
    assert app._future_middleware[0] == FutureMiddleware(m, 'request')

# Generated at 2022-06-14 07:42:58.840438
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse

    def request_middleware(request: Request):
        return request

    app = Sanic(__name__)
    app.middleware(request_middleware)
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].middleware == request_middleware
    assert app._future_middleware[0].attach_to == "request"



# Generated at 2022-06-14 07:43:01.515114
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test')
    app.middleware()



# Generated at 2022-06-14 07:43:08.210481
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Testing scenario when the middleware parameter is function
    # Given an object of MiddlewareMixin class
    mid_m = MiddlewareMixin()

    # When the middleware parameter is a function
    @mid_m.middleware
    def test_function(request):
        return request

    # Then the _future_middleware variable should be equal to middleware variable
    assert mid_m._future_middleware == [test_function]

# Generated at 2022-06-14 07:43:09.570191
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:43:12.876260
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
  x = MiddlewareMixin()
  y = x.middleware(middleware_or_request=None, attach_to="response", apply=False)
  assert isinstance(y, partial)

# Generated at 2022-06-14 07:43:24.562205
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models import REQUEST, RESPONSE

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware(REQUEST)
    def request_middleware(request, handler):
        return handler()

    @app.middleware(RESPONSE)
    def response_middleware(request, response, handler):
        pass

    assert (
        len(app._future_middleware) == 2 and
        app._future_middleware[0].function == request_middleware and
        app._future_middleware[1].function == response_middleware
    )

# Generated at 2022-06-14 07:43:28.977519
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # TODO: implement test

    print("Method middleware of class MiddlewareMixin is tested")
    print("Verify that the method is executed by checking the coverage report")
    return True


# Generated at 2022-06-14 07:43:35.550712
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    instance = MiddlewareMixin()

    def _middleware_func():
        pass

    assert instance.middleware(_middleware_func) is None
    assert instance.middleware(_middleware_func, attach_to="response") is None
    assert instance.middleware(_middleware_func, attach_to="request") is None



# Generated at 2022-06-14 07:43:37.258816
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert callable(MiddlewareMixin.middleware)

# Generated at 2022-06-14 07:43:56.125013
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import HTTPResponse
    from sanic.request import Request
    from sanic.exceptions import InvalidUsage

    from sanic import Sanic
    from sanic.response import HTTPResponse
    from sanic.request import Request
    from sanic.exceptions import InvalidUsage

    class CustomMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            middleware.run(self, Request({'type': 'fake'}))

    def simple_post_handler(request):
        return HTTPResponse()

    def simple_post_middleware(request):
        request['post_middleware'] = True


# Generated at 2022-06-14 07:43:57.752362
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:44:07.818568
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    import logging
    import sys
    import asyncio
    import time

    app = Sanic(__name__)

    @app.route("/")
    def handler(request):
        return response.text("OK")
    
    def loggingMiddleware(request):
        print("@loggingMiddleware before {0}({1})".format(request.method, request.path))
        resp = yield
        print("@loggingMiddleware after {0}({1})".format(request.method, request.path))

    app.middleware(loggingMiddleware)


# Generated at 2022-06-14 07:44:17.867873
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    middleware_mixin = MiddlewareMixin()
    assert len(middleware_mixin._future_middleware) == 0

    @middleware_mixin.middleware()
    async def hello_middleware(request):
        # do something
        pass

    assert len(middleware_mixin._future_middleware) == 1

    middleware_mixin = MiddlewareMixin()
    @middleware_mixin.on_request()
    async def hello_middleware(request):
        # do something
        pass

    assert len(middleware_mixin._future_middleware) == 1
    middleware_mixin = MiddlewareMixin()
    @middleware_mixin.on_response()
    async def hello_middleware(request):
        # do something
        pass


# Generated at 2022-06-14 07:44:31.391707
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A(MiddlewareMixin):
        def __init__(self):
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            self._future_middleware.append(middleware)

    def foo_middleware(request):
        pass

    def bar_middleware(request):
        pass

    @A.middleware
    def baz_middleware(request, response):
        pass

    @A.middleware('response')
    def qux_middleware(request, response):
        pass

    @A.on_request
    def quux_middleware(request):
        pass

    @A.on_response
    def quuux_middleware(request):
        pass


# Generated at 2022-06-14 07:44:32.671744
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:44:46.182631
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):

        def __init__(self, app):
            super(TestMiddlewareMixin, self).__init__()
            self.app = app

        def _apply_middleware(self, middleware: FutureMiddleware):
            print(middleware.attach_to, type(middleware.future))

    class App:
        pass

    app = App()
    m = TestMiddlewareMixin(app)

    @m.on_request
    def middle_before(request):
        print("request")

    @m.on_response
    def middle_after(request, response):
        print("response")

    assert m._future_middleware[0].attach_to == "request"
    assert m._future_middleware[1].attach_to == "response"
    assert len

# Generated at 2022-06-14 07:44:54.083515
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json

    app = Sanic()

    @app.middleware('request')
    def request(request):
        raise Exception

    @app.middleware('response')
    def response(request, response):
        raise Exception

    @app.route('/')
    async def handler(request):
        return json([])

    request, response = app.test_client.get('/')



# Generated at 2022-06-14 07:45:06.803616
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic(name='test')
    test_method = app.middleware
    class MiddlewareMixinTest(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            assert isinstance(middleware, FutureMiddleware)
    assert isinstance(MiddlewareMixinTest(), MiddlewareMixin)

    # Case 1
    @test_method
    async def middleware_test(request):
        return request

    # Case 2
    @test_method('request')
    async def middleware_test(request):
        return request

    # Case 3
    @test_method('response')
    async def middleware_test(request):
        return request


# Generated at 2022-06-14 07:45:19.597650
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # The case check function to be tested, please enter your code
    # Write the test code here, the test case of the program.
    def real_case_check_func(self, middleware_or_request, attach_to="request", apply=True):
        future_middleware = FutureMiddleware(middleware_or_request, attach_to)
        self._future_middleware.append(future_middleware)
        if apply:
            self._apply_middleware(future_middleware)
        return middleware_or_request
    # The case check function to be tested, please enter your code
    # Write the test code here, the test case of the program.
    def parameter_case_check_func(self):
        middleware_or_request = 'AT'
        attach_to = "request"
        apply = True
        future

# Generated at 2022-06-14 07:45:32.293856
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    m = MiddlewareMixin()
    assert m.middleware == m._apply_middleware

# Generated at 2022-06-14 07:45:42.290428
# Unit test for method middleware of class MiddlewareMixin

# Generated at 2022-06-14 07:45:53.957018
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.futures import FutureMiddleware

    class Test(MiddlewareMixin):
        def __init__(self):
            self._future_middleware = []
            super().__init__()

        def _apply_middleware(self, middleware: FutureMiddleware):
            self._future_middleware.append(middleware)

    test = Test()
    @test.middleware
    def middleware(request):
        pass

    assert len(test._future_middleware) == 1
    assert test._future_middleware[0].handler == middleware
    assert test._future_middleware[0].attach_to == "request"



# Generated at 2022-06-14 07:46:01.238849
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('name')

    @app.middleware('response')
    async def hello_world(request):
        print('Hello World!')

    assert app._future_middleware[0].name == 'Hello World!'
    assert app._future_middleware[0].attach_to == 'response'



# Generated at 2022-06-14 07:46:11.002314
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    obj = MiddlewareMixin()
    if len(obj._future_middleware) != 0:
        raise Exception('_future_middleware is not empty')

    def test_middleware(request):
        return True

    obj.middleware(test_middleware)
    if len(obj._future_middleware) != 1:
        raise Exception('_future_middleware is not empty')
    if obj._future_middleware[0].middleware != test_middleware:
        raise Exception('Middleware is not successfully added')


# Generated at 2022-06-14 07:46:16.721009
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.base import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware
    def test_middleware(request, response):
        pass
    assert app._future_middleware[0].middleware == test_middleware


# Generated at 2022-06-14 07:46:28.938357
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestClass(MiddlewareMixin):

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            self._future_middleware.append(middleware)

    def test_method(*args, **kwargs):
        pass

    instance = TestClass()
    instance.middleware(test_method, attach_to="request")
    assert len(instance._future_middleware) == 1
    assert instance._future_middleware[0].middleware == test_method
    assert instance._future_middleware[0].attach_to == "request"


# Generated at 2022-06-14 07:46:41.878603
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('request')
    def test_middleware(request):
        return json({'middleware': 'request'})

    @app.middleware('response')
    def test_middleware(request, response):
        return json({'middleware': 'response'})

    request, response = app.test_client.get('/')
    assert response.status == 200
    assert response.json == {"middleware": "request"}

    request, response = app.test_client.get('/', allow_redirects=True)
    assert response.status == 200
    assert response.json == {"middleware": "response"}



# Generated at 2022-06-14 07:46:50.099414
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import HTTPResponse


    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super(TestMiddlewareMixin, self).__init__()

        def _apply_middleware(self, middleware):
            print("_apply_middleware")

        async def test(self, request):
            return HTTPResponse("hello")

    # test 1
    # test @middleware
    async def test_middleware(request):
        print("test_middleware")
        return HTTPResponse("test_middleware")

    app = Sanic("test_MiddlewareMixin_middleware_1")
    app.add_route(app.test, "/", methods=['GET', 'POST'])

# Generated at 2022-06-14 07:46:58.187997
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddleware(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.middleware = "middleware"

        def _apply_middleware(self, middleware: FutureMiddleware):
            """"""

    test_object = TestMiddleware()
    assert test_object.middleware == "middleware"



# Generated at 2022-06-14 07:47:22.963625
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic(name="test_MiddlewareMixin_middleware")
    assert True



# Generated at 2022-06-14 07:47:34.616095
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic, Blueprint
    app = Sanic(__name__)
    bp = Blueprint("test_bp", url_prefix="/test")

    @bp.middleware("request")
    async def request_middleware(request):
        assert request["test"] == 1
        request["test"] = 2

    @bp.middleware("response")
    async def response_middleware(request, response):
        assert request["test"] == 2
        response.body = b"OK"

    @app.route("/")
    async def handler(request):
        return text("")

    app.blueprint(bp)

    _, response = app.test_client.get("/test/")
    assert response.text == "OK"

    _, response = app.test_client.get("/")
    assert response.text

# Generated at 2022-06-14 07:47:43.390050
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.server import HttpProtocol
    from sanic.testing import SanicTestClient

    app = Sanic("test_MiddlewareMixin_middleware")

    def test_middleware(request):
        return

    @app.middleware
    def middleware(request):
        return

    application = app.create_server(HttpProtocol)
    client = SanicTestClient(app)

    assert len(app._future_middleware) == 2



# Generated at 2022-06-14 07:47:53.470499
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.middleware import Middleware
    app = Sanic(__name__)
    def middleware(request):
        return 1

    assert len(app._middleware) == 0
    # check function middleware is empty and without parameter or with parameter
    app.middleware(middleware)
    assert len(app._middleware) == 1
    app.middleware(middleware)
    assert len(app._middleware) == 2
    assert isinstance(app._middleware[0], Middleware)
    assert app._middleware[0].function == middleware
    assert len(app._middleware[0].args) == 0
    assert len(app._middleware[0].kwargs) == 0

    # check function middleware is empty and with parameter

# Generated at 2022-06-14 07:48:01.458816
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Create instance of the class to be tested
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            self._called_middleware = middleware

    instance = TestMiddlewareMixin()
    # Call the method to be tested
    middleware = instance.middleware(lambda x : x, attach_to='request')
    assert middleware(1) == 1
    assert middleware(2) == 2


# Generated at 2022-06-14 07:48:08.949260
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    import asyncio

    app = Sanic('test_MiddlewareMixin_middleware')

    async def _middleware(request):
        pass
    app.middleware(_middleware)

    for middleware in app._future_middleware:
        assert middleware.middleware == _middleware

    async def _request(request):
        return

    app.add_route(_request, '/test')

    _, response = app.test_client.get('/test')
    assert response.status == 404


# Generated at 2022-06-14 07:48:17.171687
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    app = sanic.Sanic("test_MiddlewareMixin_middleware")
    assert app._future_middleware == []
    assert callable(app.middleware)

    @app.middleware('request')
    def request(request):
        return True

    assert app._future_middleware[0].middleware is request
    assert app._future_middleware[0].attach_to == "request"



# Generated at 2022-06-14 07:48:25.046381
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic import response

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('request')
    async def print_on_request(request):
        print('Inside request middleware')
        return response.text('I am a teapot', status=418)

    @app.middleware('response')
    async def print_on_response(request, response):
        print('Inside response middleware')

    @app.route('/')
    async def handler(request):
        return response.json({'test': 'OK'})

    request, response = app.test_client.get('/')
    assert response.status == 200

# Generated at 2022-06-14 07:48:36.747326
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """
    Test middleware with and without request parameter
    """

    class App(MiddlewareMixin):
        def __init__(self):
            super().__init__()
            self.middleware(self)
            self.middleware('request', apply=False)

        def _apply_middleware(self, middleware):
            pass

    assert len(App()._future_middleware) == 2

    assert App()._future_middleware[0].attach_to == 'response'
    assert App()._future_middleware[1].attach_to == 'request'
    assert App()._future_middleware[1].apply == False



# Generated at 2022-06-14 07:48:39.110803
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    app = MiddlewareMixin()
    assert app.middleware == MiddlewareMixin.middleware

# Generated at 2022-06-14 07:49:35.283901
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware
    from sanic.util import sanic_endpoint_test
    from sanic.views import HTTPMethodView
    from sanic.websocket import WebSocketProtocol

    class MiddlewareView(HTTPMethodView):
        def get(self, request):
            return text("Get")

        def post(self, request):
            return text("Post")

    class MiddlewareTestApp(MiddlewareMixin):
        pass

    app = MiddlewareTestApp()

    @app.middleware
    async def process_request(request):
        request.ctx.processed_by_pre_request_middleware = True

    @app.middleware("request")
    async def process_request2(request):
        pass

# Generated at 2022-06-14 07:49:47.786011
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.request import Request
    from sanic.response import text
    from sanic.testing import HOST, PORT

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    async def middleware_one(request: Request):
        return text('pass')

    @app.middleware('request')
    async def middleware_two(request: Request):
        return text('pass')

    @app.middleware('response')
    async def middleware_three(request: Request, response: text):
        return response

    @app.route('/')
    async def handler(request: Request):
        return text('OK')


# Generated at 2022-06-14 07:49:56.113370
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    @middleware('AT')
    def middleware_func():
        return 'middleware func'

    app = MiddlewareMixin()
    assert app._future_middleware == []
    app.middleware(middleware_func)
    assert app._future_middleware == [middleware_func]
    app.middleware('AT', apply=False)(middleware_func)
    assert app._future_middleware == [middleware_func, middleware_func]


# Generated at 2022-06-14 07:50:08.813224
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import json
    import asynctest
    from asynctest.mock import ANY, call, CoroutineMock, Mock, patch
    from sanic.models.middlewares import Middleware

    # the mocks
    middleware_patch = Mock()
    future_middleware_patch = Mock()
    future_middleware_patch.attach_to = "request"
    future_middleware_patch.middleware = middleware_patch

    # creating the test object
    app = Sanic("test_MiddlewareMixin_middleware")

    # the code to be tested
    app.middleware(future_middleware_patch, "request", True)

    # assertions
    assert app._future_middleware == [future_middleware_patch]



# Unit test
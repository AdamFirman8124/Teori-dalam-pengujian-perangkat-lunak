

# Generated at 2022-06-14 07:40:00.883371
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic

    app = Sanic('test')
    app.on_request
    app.on_response
    assert app.on_request(lambda r: None)
    assert app.on_response(lambda r: None)

# Generated at 2022-06-14 07:40:02.019451
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    assert True


# Generated at 2022-06-14 07:40:06.219816
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    import sanic
    app = sanic.Sanic()
    app.on_request(lambda x : print("Run on request"))
    assert(app._future_middleware[0]._middleware == (lambda x : print("Run on request")))

# Generated at 2022-06-14 07:40:18.454569
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import pytest
    from sanic.models.futures import FutureMiddleware

    class T(MiddlewareMixin):
        @property
        def future_middleware(self):
            return self._future_middleware

        def _apply_middleware(self, middleware: FutureMiddleware):
            return True

    t = T()
    assert t.future_middleware == [], "future_middleware is not empty"

    @t.middleware("request")
    async def m1(request):
        return True

    @t.middleware("response")
    async def m2(request):
        return True

    assert len(t.future_middleware) == 2
    assert t.future_middleware[0].middleware == m1
    assert t.future_middleware[0].attach_to == "request"
   

# Generated at 2022-06-14 07:40:24.483705
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.app import Sanic
    app = Sanic('test')
    @app.middleware
    async def on_request(request):
        middleware = True
    @app.middleware('response')
    async def on_response(request, response):
        middleware = True
    app.on_request(middleware=True)
    app.on_response(middleware=True)
    pass


# Generated at 2022-06-14 07:40:37.098789
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.exceptions import RequestTimeout

    utils.init_logging(logging.DEBUG)

    # Define middleware of class 'MiddlewareMixin'
    # (optional) apply=False
    @app.middleware
    async def middleware1(request):
        pass

    # Define middleware of class 'MiddlewareMixin'
    # (optional) attach_to='response'
    @app.middleware('response')
    async def middleware2(request, response):
        pass

    # Test if middleware1 have been registered
    assert len(app._future_middleware) == 2

    # Test if middleware2 have been registered
    assert app._future_middleware[1].middleware == middleware2

# Generated at 2022-06-14 07:40:45.511099
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import pytest
    from sanic.app import Sanic
    app = Sanic("test_Sanic_middleware")
    assert app.__class__.__name__ == "Sanic"

    def middleware1(request):
        pass

    app.middleware(middleware1)
    assert len(app._future_middleware) == 1

    def middleware2(request):
        pass

    app.middleware(middleware2, attach_to='request')
    assert len(app._future_middleware) == 2

    with pytest.raises(NotImplementedError):
        app._apply_middleware(app._future_middleware[0])


# Generated at 2022-06-14 07:40:57.955971
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class App(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._future_middleware.append(FutureMiddleware(self, "request"))

        def _apply_middleware(self, middleware: FutureMiddleware):
            self.middleware = middleware

        def __call__(self, *args, **kwargs):
            pass

    app = App()
    assert app._future_middleware == [FutureMiddleware(app, attach_to='request')]
    app.middleware(app, attach_to='request')
    assert app._future_middleware == [FutureMiddleware(app, attach_to='request'),
                                      FutureMiddleware(app, attach_to='request')]



# Generated at 2022-06-14 07:41:04.474804
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    m = TestMiddlewareMixin()
    @m.middleware()
    def func():
        pass

    middle = m._future_middleware[0]
    assert middle.middleware is func
    assert middle.attach_to == "request"

# Generated at 2022-06-14 07:41:15.111798
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic
    from sanic.exceptions import InvalidUsage
    import types

    app = Sanic(__name__)

    # dummy middleware
    def example_middleware(request):
        return
    @app.middleware
    def example_middleware2(request):
        return

    example_middleware_bak = example_middleware
    example_middleware2_bak = example_middleware2
    # on_request function should return an function
    example_middleware = app.on_request(example_middleware)
    assert callable(example_middleware)
    assert isinstance(example_middleware, types.FunctionType)
    # on_request middleware should be added to the middleware list
    assert example_middleware == example_middleware_bak
    assert example_middleware in app

# Generated at 2022-06-14 07:41:22.819702
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    app = Sanic("test_MiddlewareMixin_middleware")

    assert app._future_middleware == []

    @app.middleware
    def register_test_middleware(request):
        pass

    assert len(app._future_middleware) == 1

    @app.middleware('response')
    def register_test_middleware2(request):
        pass

    assert len(app._future_middleware) == 2



# Generated at 2022-06-14 07:41:30.383464
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class ClassForTesting(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    mid = ClassForTesting()
    assert middleware_register_1 == mid.on_request(middleware_register_1)
    assert middleware_register_2 == mid.middleware(middleware_register_2)
    assert middleware_register_3 == mid.on_response(middleware_register_3)
    
async def middleware_register_1(request):
    pass

async def middleware_register_2(request):
    pass

async def middleware_register_3(request, response):
    pass

# test MiddlewareMixin
if __name__ == "__main__":
    test_MiddlewareMixin_middleware()

# Generated at 2022-06-14 07:41:41.350211
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # assemble
    target = MiddlewareMixin()
    middleware = lambda r:r
    # act
    target.middleware(middleware)
    # assert
    assert callable(target.middleware)
    assert target._future_middleware is not None
    assert len(target._future_middleware) == 1
    assert target._apply_middleware is None
    assert callable(target.middleware)
    assert target.on_request is not None
    assert callable(target.on_request)
    assert target.on_response is not None
    assert callable(target.on_response)



# Generated at 2022-06-14 07:41:50.004768
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """
    This test is to make sure that method middleware of class MiddlewareMixin works well
    @app.middleware
    async def example(request):
        return request.app.name

    :return: None
    """
    v = MiddlewareMixin()
    def middleware():
        return "googleglass"
    result = v.middleware('request')(middleware)
    assert result.__name__ == 'middleware', "unit test is wrong"

# Generated at 2022-06-14 07:42:01.705233
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    middleware_mixin = MiddlewareMixin()
    with pytest.raises(NotImplementedError):
        middleware_mixin._apply_middleware(middleware_mixin)

    middleware = middleware_mixin.middleware(middleware_mixin)
    assert middleware == middleware_mixin

    def middleware_mock(request):
        return request

    middleware_mock_response = middleware_mixin.middleware(middleware_mock, "response")
    assert middleware_mock_response == middleware_mock
    assert middleware_mixin._future_middleware[0].middleware == middleware_mock
    assert middleware_mixin._future_middleware[0].attach_to == "response"


# Generated at 2022-06-14 07:42:09.366985
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Test:
        def __init__(self):
            self._future_middleware = []

        def _apply_middleware(self, middleware):
            pass

    test = Test()
    test.middleware(middleware=False, attach_to="request")
    test.middleware(middleware=True, attach_to="request", apply=True)
    test.on_request(middleware=False)
    test.on_request(middleware=True)
    test.on_response(middleware=False)
    test.on_response(middleware=True)

# Generated at 2022-06-14 07:42:16.161224
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic("test_MiddlewareMixin")
    assert app._future_middleware == []

    @app.middleware
    def middleware(request):
        pass

    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].middleware == middleware
    assert app._future_middleware[0].attach_to == "request"



# Generated at 2022-06-14 07:42:29.420958
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models import FutureMiddleware

    app = Sanic("test_sanic")
    assert (app._future_middleware == [])

    @app.middleware("request")
    async def test_middleware1(request):
        pass

    @app.middleware("request")
    async def test_middleware2(request):
        pass

    @app.middleware("response")
    async def test_middleware3(request, response):
        pass

    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert isinstance(app._future_middleware[1], FutureMiddleware)
    assert isinstance(app._future_middleware[2], FutureMiddleware)
    assert (len(app._future_middleware) == 3)

# Generated at 2022-06-14 07:42:42.977170
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.response import text

    app = Sanic(__name__)

    @app.middleware("request")
    async def before_request(request):
        request["test_before_request"] = True
        return request

    @app.middleware("response")
    async def after_request(request, response):
        response._test_after_request = True
        return response

    @app.route("/middleware")
    async def handler(request):
        return text("OK")

    request, response = app.test_client.get("/middleware")

    assert response._test_after_request
    assert request["test_before_request"]
    assert response.status == 200
    assert response

# Generated at 2022-06-14 07:42:52.514440
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import unittest

    from sanic.exceptions import SanicException

    from .server import Sanic
    from .server import SanicException

    class MiddlewareTest(unittest.TestCase):

        def setUp(self):
            self.app = Sanic('test_MiddlewareMixin_middleware')

        def test_middleware_call(self):
            @self.app.middleware
            def simple_middleware(request):
                pass

            @self.app.middleware('request')
            def simple_middleware_request(request):
                pass

            @self.app.middleware('response')
            def simple_middleware_response(request, response):
                pass

            middleware_count = len(self.app._future_middleware)
            self.app.middleware(simple_middleware)
           

# Generated at 2022-06-14 07:43:05.255526
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    '''
    - Method Name: test_MiddlewareMixin_middleware
    - Description: This method tests the functionality of middleware method in MiddlewareMixin class.
    - Param: None.
    - Return: AssertionError if test case not passed, else None.
    '''
    try:
        class TestClass(MiddlewareMixin):
            pass
        @TestClass.middleware('request')
        def test_middleware(request):
            pass
    except AssertionError:
        print('test_MiddlewareMixin_middleware Failed.')
        raise
    else:
        pass


# Generated at 2022-06-14 07:43:10.857475
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    testMiddlewareMixin = TestMiddlewareMixin()
    testMiddlewareMixin.middleware(middleware='response')
# End of test code

# Generated at 2022-06-14 07:43:17.457037
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    async def print_on_request(request):
        print('I run before every request')

    request, response = app.test_client.get('/')
    assert response.text == 'Hello world!'
    assert response.status == 200



# Generated at 2022-06-14 07:43:24.271694
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.request import Request
    app = MiddlewareMixin()
    @app.middleware
    def example_middleware(request):
        pass

    # verify if the middleware is properly registered
    assert app._future_middleware == [FutureMiddleware(example_middleware, 'request')]


# Generated at 2022-06-14 07:43:35.551921
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    def request_middleware(request):
        request['middleware'] = True

    def response_middleware(request, response):
        response['context']['middleware'] = True

    app = Sanic('test_MiddlewareMixin_middleware')
    app.middleware(request_middleware)
    app.middleware(response_middleware, attach_to="response")
    request, response = app.test_client.get("/")

    assert request.get('middleware') is True
    assert response.get('middleware') is True



# Generated at 2022-06-14 07:43:47.191616
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.blueprints import Blueprint
    from sanic.constants import HTTP_METHODS
    from sanic.exceptions import SanicException
    from typing import Callable, Awaitable

    async def async_test():
        pass

    def normal_test():
        pass

    class MiddlewareTest(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    app = MiddlewareTest()

    # Test normal function
    @app.middleware
    def test_middleware(req):
        pass

    assert len(app._future_middleware) == 1

    # Test Async function
    @app.middleware
    async def test_async_middleware(req):
        pass

    assert len(app._future_middleware) == 2

    # Test on_request

# Generated at 2022-06-14 07:43:57.106209
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    middleware_mixin_obj = MiddlewareMixin()
    # middleware_mixin_obj._future_middleware = []
    middleware_mixin_obj.middleware(middleware_mixin_obj, attach_to="request")
    assert (
            middleware_mixin_obj
            ._future_middleware[0]
            ._middleware == middleware_mixin_obj
    )
    assert (
            middleware_mixin_obj
            ._future_middleware[0]
            ._attach_to == "request"
    )
    assert middleware_mixin_obj._future_middleware[0]._future is None

# Generated at 2022-06-14 07:44:00.065696
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')
    app.middleware('request')(lambda r: r)
    app.middleware('response')(lambda r: r)
    assert len(app._future_middleware) == 2


# Generated at 2022-06-14 07:44:13.823385
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    # test for function middleware
    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    async def handler(request):
        pass

    assert app._future_middleware.__len__() == 1
    assert app._future_middleware[0]._middleware == handler
    assert app._future_middleware[0]._attach_to == 'request'

    app._future_middleware.clear()

    # test for partial function middleware
    app = Sanic('test_MiddlewareMixin_middleware')
    handler_partial = partial(handler, 123)

    @app.middleware
    async def handler(x):
        pass

    app.middleware(handler_partial)

    assert app._future_middleware.__len__() == 2

# Generated at 2022-06-14 07:44:26.646883
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import unittest

    class MiddlewareMixin_(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware) -> None:
            pass

    class Test(unittest.TestCase):
        def setUp(self) -> None:
            self.MiddlewareMixin = MiddlewareMixin_(None)

        def tearDown(self) -> None:
            self.MiddlewareMixin.__init__(None)

        def test_middleware_request(self):
            self.MiddlewareMixin.middleware(lambda r: None)
            self.assertEqual(len(self.MiddlewareMixin._future_middleware), 1)


# Generated at 2022-06-14 07:44:36.765437
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class SomeClass(MiddlewareMixin):
        pass
    instance = SomeClass()
    @instance.middleware
    def some_middleware(request):
        return request
    instance._apply_middleware(instance._future_middleware[0])
    assert len(instance._future_middleware) == 1


# Generated at 2022-06-14 07:44:39.941533
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')

    def test_middleware(request, response):
        return True

    app.middleware(test_middleware)

    assert app.request_middleware[0][0] == test_middleware
    assert app.request_middleware[0][1] == "request"

    assert app.response_middleware[0][0] == test_middleware
    assert app.response_middleware[0][1] == "response"



# Generated at 2022-06-14 07:44:49.351477
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    testMiddlewareMixin = TestMiddlewareMixin()
    @testMiddlewareMixin.middleware
    async def testMiddleware(request):
        return 'testMiddleware'

    futureMiddleware = testMiddlewareMixin._future_middleware[0]
    assert inspect.iscoroutinefunction(futureMiddleware.func) == True
    assert futureMiddleware.attach_to == 'request'
    assert futureMiddleware.name == 'testMiddleware'


# Generated at 2022-06-14 07:45:00.044802
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MyApp(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super(MyApp, self).__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            print("Apply {}".format(middleware))

    app = MyApp()
    print("--- (1) @app.middleware ---")
    @app.middleware
    def midware(req, res):
        pass

    app._future_middleware[0].middleware(1, 2)


# Generated at 2022-06-14 07:45:07.062942
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixinClass(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    MiddlewareMixinClass().middleware(middleware_or_request=None)

# Generated at 2022-06-14 07:45:20.278864
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.futures import Future
    
    from sanic.models.futures import FutureMiddleware
    from sanic.models.futures import FutureMiddlewareFunction

    class CustomFuture(Future):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self._middleware_functions: List[
                FutureMiddlewareFunction] = []
            self._middleware_functions_installed: bool = False

        def _install_middleware(self):
            raise NotImplementedError  # noqa

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa


# Generated at 2022-06-14 07:45:33.851270
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic import request
    from sanic.response import html
    from sanic.views import HTTPMethodView
    from sanic_restful import Api
    from sanic_restful.response import json_dumps

    app = Sanic(__name__)

    class R(object):
        method = 'GET'
        body = None
        uri = '/'
        app = app

    import json

    @app.middleware('request')
    async def add_data_to_request(request):
        request['data'] = {'hello': 'world'}

    @app.middleware('response')
    async def add_data_to_response(request, response):
        response.set('Hello', 'world')


# Generated at 2022-06-14 07:45:47.918652
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test')

    def _on_request(req, res):
        pass

    app.middleware(_on_request)
    assert app._future_middleware[0].request_handler == _on_request
    app._future_middleware.pop()

    app.middleware(_on_request, 'request')
    assert app._future_middleware[0].request_handler == _on_request
    app._future_middleware.pop()

    app.middleware(_on_request, 'response')
    assert app._future_middleware[0].response_handler == _on_request
    app._future_middleware.pop()

    def _on_response(req, res):
        pass
    app.middleware(_on_response, 'response')
    assert app._

# Generated at 2022-06-14 07:45:58.939818
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import unittest
    from types import FunctionType
    from sanic.models.futures import FutureMiddleware
    from sanic.models import MiddlewareMixin
    from werkzeug.wsgi import DispatcherMiddleware
    from werkzeug.serving import run_simple

    # create test classes
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware):
            pass

    # create test data
    attach_to = 'request'
    middleware = lambda request: 'test_middleware_function'
    middleware_function = lambda request: 'test_middleware_function'

# Generated at 2022-06-14 07:46:09.809878
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    # Create a new instance of class Sanic
    app = Sanic(__name__)

    # Test method middleware
    @app.middleware
    async def simple_middleware(request):
        pass

    @app.middleware('response')
    async def simple_response_middleware(request, response):
        pass

    # Test method on_request
    @app.on_request
    async def simple_on_request(request):
        pass

    # Test method on_response
    @app.on_response
    async def simple_on_response(request, response):
        pass

    # Assert the correct result of middleware
    assert app._future_middleware == []
    assert len(app._future_middleware) == 0


# Generated at 2022-06-14 07:46:18.233659
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:46:30.932450
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    # Instance app
    app = Sanic('test_MiddlewareMixin_middleware')

    # _future_middleware of app is a list
    assert isinstance(app._future_middleware, list)

    # The length of the list is 0
    assert len(app._future_middleware) == 0

    # Middleware is a function
    async def middleware_test(request):
        return request

    # Register middleware
    @app.middleware
    async def middleware_test2(request):
        return request

    # The length of the list is 2
    assert len(app._future_middleware) == 2

    # The second element in list is a partial function
    # for function middleware_test2
    assert isinstance(app._future_middleware[1], partial)

# Generated at 2022-06-14 07:46:43.517922
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import pytest
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.response import text
    from sanic.exceptions import SanicException
    
    def wrapper_middleware(request: Request):
        text_list = []
        if request.app.get('middleware') == None:
            request.app['middleware'] = True
            return wrapper_middleware(request)

        #test the values of request and response
        if not isinstance(request, Request):
            raise SanicException('Request is not Request')
        if not isinstance(request.app, dict):
            raise SanicException('Request.app is not dict')
        if not isinstance(request.args, dict):
            raise SanicException('Request.args is not dict')

# Generated at 2022-06-14 07:46:55.844400
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json
    app = Sanic("test_MiddlewareMixin_middleware")

    @app.middleware("request")
    async def request_middleware(request):
        request["middleware"] = True

    @app.middleware("response")
    async def response_middleware(request, response):
        response.body = b"Request processed"

    @app.route("/")
    async def handler(request):
        return json({"hello": "world"})

    request, response = app.test_client.get("/")
    assert response.text == "Request processed"
    assert response.status == 200
    assert request["middleware"]

# Generated at 2022-06-14 07:47:01.873771
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.review.model import MiddlewareMixin
    from sanic.models.futures import FutureMiddleware

    class A(MiddlewareMixin):
        async def _apply_middleware(self, middleware):
            pass

    def middleware():
        pass

    a = A()
    a.middleware(middleware)
    # a._apply_middleware(FutureMiddleware(middleware, "request"))



# Generated at 2022-06-14 07:47:11.217692
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic(__name__)
    assert app.middleware(None) == partial(app.middleware, attach_to=None)
    assert app.middleware(None, apply=False) == partial(
        app.middleware, attach_to=None
    )
    assert app.middleware('None') == partial(app.middleware, attach_to='None')
    assert app.on_request() == partial(app.middleware, attach_to='request')
    assert app.on_response() == partial(app.middleware, attach_to='response')

# Generated at 2022-06-14 07:47:15.572190
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic import Sanic
    app = Sanic()
    a = MiddlewareMixin(app)
    assert a._future_middleware == []
    a.middleware(middleware_or_request = 'request')


# Generated at 2022-06-14 07:47:21.201398
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_Test(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    MiddlewareMixin_Test().middleware(1, attach_to="R")
    test = MiddlewareMixin_Test().middleware(lambda req, resp: None)
    test()
    assert MiddlewareMixin_Test()._future_middleware[0].middleware is not None
    assert MiddlewareMixin_Test()._future_middleware[0].attach_to == "request"
    assert MiddlewareMixin_Test().middleware(lambda: None, attach_to="R").__name__ == "<lambda>"


# Generated at 2022-06-14 07:47:22.968838
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # TODO: implement test
    raise NotImplementedError

# Generated at 2022-06-14 07:47:34.616483
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app_mock = Sanic(__name__)

    @app_mock.middleware
    async def middleware_func(request):
        pass
    assert isinstance(middleware_func, partial)

    @app_mock.middleware('request')
    async def middleware_func(request):
        pass
    assert isinstance(middleware_func, partial)

    @app_mock.middleware('response')
    async def middleware_func(request):
        pass
    assert isinstance(middleware_func, partial)

    # Get method object from class
    middleware = MiddlewareMixin.middleware
    assert isinstance(middleware, classmethod)

    # Register method as attribute of class
    MiddlewareMixin.middleware = middleware_func
    middleware
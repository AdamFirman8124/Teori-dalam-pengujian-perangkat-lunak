

# Generated at 2022-06-14 07:40:11.584874
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert False

# Generated at 2022-06-14 07:40:15.687626
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Set up the test environment and create the MiddlewareMixin object
    import unittest
    import sys
    import os
    import inspect
    currentdir = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)  # Add the package to the directory path
    from sanic import Sanic
    sanic_obj = Sanic('sanic_test')

    # Test for 'middleware' with Argument Server object
    response = sanic_obj.on_response('response')
    assert response == partial(sanic_obj.middleware, attach_to='response')



# Generated at 2022-06-14 07:40:23.797675
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    try:
        from sanic import Sanic
        from sanic.models import MiddlewareMixin

        class MySanic(Sanic, MiddlewareMixin):
            pass
        asynic = MySanic()
        @asynic.on_response
        def custom_middleware(request, response):
            if response.status == 200:
                response.text = "Hello, world!"
        
        assert len(asynic._future_middleware) == 1
    except:
        assert False

# Generated at 2022-06-14 07:40:34.738140
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    app = Sanic(__name__)

    @app.on_response
    def on_response(request, response):
        """
        当返回的response的body非空，对body进行解密处理
        """
        import json
        import logging
        import datetime
        from sanic.helpers import json as json_dumps

        logging.info("请求：{}".format(request))

        # 返回响应之前检查是否需要解密

# Generated at 2022-06-14 07:40:43.826454
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text
    
    app = Sanic()
    
    @app.middleware('request')
    async def request_middleware(request):
        request['parsed_data'] = 'middleware'
    
    @app.route('/')
    async def handler(request):
        return text(request['parsed_data'])
    
    request, response = app.test_client.get('/')
    assert response.text == 'middleware'
    

# Generated at 2022-06-14 07:40:51.797159
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class DummyClass(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

    dummy = DummyClass()
    assert dummy.on_response(1) == partial(dummy.middleware, attach_to="response")
    assert dummy.on_response() == partial(dummy.middleware, attach_to="response")
    assert dummy.on_response(middleware = 1) == partial(dummy.middleware, attach_to="response")

# Generated at 2022-06-14 07:40:53.922320
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert MiddlewareMixin.on_response(MiddlewareMixin) is not None
    assert MiddlewareMixin.on_response(MiddlewareMixin, 1) is not None

# Generated at 2022-06-14 07:40:58.206702
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    app = Sanic(__name__)
    @app.on_response
    async def response(request, response):
        pass
    assert len(app._future_middleware) != 0


# Generated at 2022-06-14 07:41:02.214326
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    # create app
    app = Sanic()
    # assign on_response
    on_response = app.on_response

    assert isinstance(on_response, types.MethodType)


# Generated at 2022-06-14 07:41:12.604366
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    def test_middleware(request):
        pass
    assert app._future_middleware

    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware('request')
    def test_request_middleware(request):
        pass
    assert app._future_middleware

    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware('response')
    def test_request_middleware(request, response):
        pass
    assert app._future_middleware


# Generated at 2022-06-14 07:41:18.137911
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic("middleware")
    def test_middleware():
        pass
    app.middleware(test_middleware)
    app.middleware("response")(test_middleware)

# Generated at 2022-06-14 07:41:27.126991
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    from sanic.handlers import ErrorHandler
    from sanic.response import text

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    async def middleware_1_name(request):
        pass

    @app.middleware('request')
    async def middleware_2_name(request):
        pass

    @app.middleware('response')
    async def middleware_3_name(request):
        pass

    assert len(app._future_middleware) == 3
    assert app._future_middleware[0].name == 'middleware_1_name'
    assert app._future_middleware[1].name == 'middleware_2_name'

# Generated at 2022-06-14 07:41:33.466909
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic()
    def assert_middleware_mixin():
        assert isinstance(app, MiddlewareMixin)
        assert app.on_response == app.middleware

    assert_middleware_mixin()

# Generated at 2022-06-14 07:41:34.764254
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:41:36.524738
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert isinstance(MiddlewareMixin, MiddlewareMixin)

# Generated at 2022-06-14 07:41:39.969470
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixinObj(MiddlewareMixin):
        pass
    obj = MiddlewareMixinObj()
    # Testing middleware method
    obj._apply_middleware(0)
    obj.on_request(0)
    obj.on_response(0)

# Generated at 2022-06-14 07:41:50.260442
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin1:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError

        def middleware(
            self, middleware_or_request, attach_to="request", apply=True
        ):
            def register_middleware(middleware, attach_to="request"):
                nonlocal apply

                future_middleware = FutureMiddleware(middleware, attach_to)
                self._future_middleware.append(future_middleware)
                if apply:
                    self._apply_middleware(future_middleware)
                return middleware

            if callable(middleware_or_request):
                return register_middle

# Generated at 2022-06-14 07:42:02.507353
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareObject(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super(MiddlewareObject,self).__init__(*args, **kwargs)
    
    # Create a MiddlewareMixin Object
    middleware_object = MiddlewareObject()
    # Check whether the middleware list is empty
    assert middleware_object._future_middleware == []

    # Check whether the method middleware is working properly.
    @middleware_object.middleware
    def test_middleware_method(request):
        pass

    assert len(middleware_object._future_middleware) == 1
    assert type(middleware_object._future_middleware[0]) is FutureMiddleware
    # Check whether the attach_to field is 'request'

# Generated at 2022-06-14 07:42:08.407121
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic()
    test_str = "test"
    @app.middleware
    def middleware_func(*args):
        return test_str
    assert middleware_func() == test_str
    assert app._future_middleware[0].middleware == middleware_func
    assert app._future_middleware[0].attach_to == "request"


# Generated at 2022-06-14 07:42:18.940992
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    app = Sanic(__name__)

    @app.middleware
    def logger_middleware(request):
        print('logging')

    @app.middleware()
    def logger_middleware2(request):
        print('logging2')

    @app.middleware('request')
    def logger_request(request):
        print('logging_request')

    @app.middleware('response')
    def logger_response(request, response):
        print('logging_response')

    # Unit test for method middleware of class MiddlewareMixin
    def test_MiddlewareMixin_on_request():
        app = Sanic(__name__)

        @app.on_request
        def logger_request(request):
            print('logging_request')

    # Unit test for method middleware of class MiddlewareMix

# Generated at 2022-06-14 07:42:32.376423
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('request')
    async def request_middleware(request):
        print('in request middleware')

    @app.middleware('response')
    async def response_middleware(request, response):
        print('in response middleware')

    @app.route('/')
    def handler(request):
        pass

    client = app.test_client
    request, response = client.get('/')
    assert response.status == 200
    assert 'in request middleware' in str(response.content)
    assert 'in response middleware' in str(response.content)


# Generated at 2022-06-14 07:42:34.746533
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    Test = MiddlewareMixin()

    Test.middleware(middleware_or_request=False, attach_to="request")

# Generated at 2022-06-14 07:42:48.818663
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')
    assert hasattr(app, 'middleware'), 'app not contains middleware() method'
    assert callable(app.middleware), 'app.middleware() is not callable'
    assert callable(app.on_request), 'app.on_request() is not callable'
    assert callable(app.on_response), 'app.on_response() is not callable'
    @app.middleware
    async def test_MiddlewareMixin_middleware_request(request):
        return request
    @app.on_request
    async def test_MiddlewareMixin_middleware_request_1(request):
        return request

# Generated at 2022-06-14 07:42:54.697615
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # arrange
    from sanic import Sanic
    app = Sanic("test_MiddlewareMixin_middleware")
    middleware_func: Callable = lambda request: None
    # act
    middle_result = app.middleware(middleware_func)
    # assert
    assert middle_result == middleware_func


# Generated at 2022-06-14 07:43:08.130978
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.futures import FutureMiddleware
    from sanic.models.futures import register_future_middleware
    from sanic.server import HttpProtocol
    from sanic.server_options import ServerOptions
    from sanic.server import Server
    import sentry_sdk
    import asynctest
    from unittest.mock import MagicMock
    from unittest.mock import patch

    class Middleware_test(MiddlewareMixin):
        def __init__(self):
            super().__init__()
            self.middleware_list = []

        def _apply_middleware(self, middleware):
            if middleware not in self.middleware_list:
                self.middleware_list.append(middleware)

    M_obj = Middleware_test()

   

# Generated at 2022-06-14 07:43:20.896774
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_middlewareClass(MiddlewareMixin):
        def __init__(self):
            super().__init__()
        def _apply_middleware(self, middleware: FutureMiddleware):
            return middleware

    # First way
    @MiddlewareMixin_middlewareClass.middleware
    async def _middleware(request):
        return True

    assert len(MiddlewareMixin_middlewareClass._future_middleware) == 1
    assert MiddlewareMixin_middlewareClass._future_middleware[0].attach_to == 'request'
    assert MiddlewareMixin_middlewareClass._future_middleware[0].middleware == _middleware

    # Second way

# Generated at 2022-06-14 07:43:21.467172
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:43:30.199474
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa

    a = MiddlewareMixin()
    A.middleware = a.middleware
    A.on_request = a.on_request
    A.on_response = a.on_response

# Generated at 2022-06-14 07:43:32.546229
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    '''
    Test middleware method
    '''
    pass


# Generated at 2022-06-14 07:43:41.256276
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super(TestMiddlewareMixin, self).__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    test_middleware = lambda request, response: response
    test_middleware_obj = TestMiddlewareMixin()
    test_middleware_obj.middleware(test_middleware)
    test_middleware_obj.middleware(test_middleware, attach_to='request')
    test_middleware_obj.middleware(test_middleware, attach_to='response')
    test_middleware_obj.on_request(test_middleware)
    test_middleware_obj.on_response(test_middleware)

# Generated at 2022-06-14 07:43:58.734025
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            pass

    test_middleware_mixin = TestMiddlewareMixin()
    test_middleware_mixin.middleware(middleware_or_request="request", apply=True)
    assert test_middleware_mixin._future_middleware[0]._attach_to == "request"
    test_middleware_mixin.middleware(middleware_or_request="response", apply=True)
    assert test_middleware_mixin._future_middleware[1]._attach_to == "response"
    def test_middleware(request):
        return request
    test_middleware_mixin.middleware(middleware_or_request=test_middleware, apply=True)
    assert test_middleware_mixin._

# Generated at 2022-06-14 07:44:10.883237
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.views import CompositionView
    from sanic.response import json
    app = Sanic(__name__)

    @app.middleware('request')
    async def before_request(request):
        return json({"before_request": "success"})

    @app.middleware('response')
    async def before_response(request, response):
        return json({"before_response": "success"})

    @app.route('/')
    async def handler(request):
        return json({"route": "success"})

    request, response = app.test_client.get('/')
    assert response.status == 200
    assert response.json == {"before_request": "success"}


# Generated at 2022-06-14 07:44:11.551572
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:44:25.262692
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import inspect
    import types
    import sys
    import asyncio
    import functools

    from sanic.app import Sanic
    from sanic.server import serve

    app = Sanic('test_MiddlewareMixin_middleware')

    @sanic.middleware
    async def print_on_request(request):
        print ("I print when a request is processed")
        # Anything returned gets passed to next middleware in chain, or to
        # views and routes if no more middleware
        #return request


    @sanic.middleware('response')
    async def print_on_response(request, response):
        print ("I print when a response is returned")


    async def handler(request):
        return sanic.response.text('OK')


    app.add_route(handler, '/')




# Generated at 2022-06-14 07:44:32.586535
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_test(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    test_middleware1 = lambda request: request
    test_middleware2 = lambda request: request
    mm = MiddlewareMixin_test()

    mm.middleware(test_middleware1)(test_middleware2)

    assert mm._future_middleware == [FutureMiddleware(test_middleware2)]



# Generated at 2022-06-14 07:44:34.237328
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert True == True


# Generated at 2022-06-14 07:44:47.616346
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    import os
    import sys
    import string
    import random

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('request')
    async def request_middleware1(request):
        pass

    @app.middleware('response')
    async def response_middleware2(request, response):
        pass

    @app.middleware('request')
    def request_middleware3(request):
        pass

    @app.middleware('response')
    def response_middleware4(request, response):
        pass

    @app.middleware
    def response_middleware5(request, response):
        pass

    middlewares = app._future_middleware

    assert len(middlewares) == 5


# Generated at 2022-06-14 07:44:59.089001
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.helpers import to_coroutine
    from sanic.response import json, text


    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('request')
    async def test_on_request(request):
        request['modified'] = True

    @app.middleware('response')
    async def test_on_response(request, response):
        response['modified_response'] = True

    @app.route('/')
    def handler(request):
        return text('OK')

    request, response = app.test_client.get('/')

    assert response.status == 200
    assert response.body == b'OK'
    assert response.headers.get('modified_response') == 'true'
    assert request['modified'] == True

# Generated at 2022-06-14 07:45:12.809658
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.middleware import Middleware
    from sanic.models.functional import FunctionalMiddleware

    class MockMiddleware(Middleware):
        pass


    class MockFunctionalMiddleware(FunctionalMiddleware):
        pass


    app = Sanic(__name__)
    app.middleware(MockMiddleware)

    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert isinstance(app._future_middleware[0].middleware, MockMiddleware)

    app.middleware(MockFunctionalMiddleware())

    assert isinstance(app._future_middleware[1], FutureMiddleware)
    assert isinstance(
        app._future_middleware[1].middleware, MockFunctionalMiddleware
    )


# Generated at 2022-06-14 07:45:21.039065
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from unittest import TestCase


    class TestPrint(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass


    @TestPrint.middleware('xx')
    async def test(x, y):
        print(x, y)
        print(x, y)


    TestPrint.middleware(test)
    test(1, 2)

# Generated at 2022-06-14 07:45:42.219381
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.futures import FutureMiddleware

    class FakeMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    fake_middleware_mixin = FakeMiddlewareMixin()
    # test middleware
    assert fake_middleware_mixin._future_middleware == []

    fake_middleware_mixin.middleware(attach_to='request')()
    assert len(fake_middleware_mixin._future_middleware) == 1
    assert isinstance(fake_middleware_mixin._future_middleware[0], FutureMiddleware)

    # test on_request, on_response
    fake_middleware_mixin.on_request()
    fake_middleware_mixin.on_response()

# Generated at 2022-06-14 07:45:51.726580
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import text

    app = Sanic(__name__)

    @app.middleware('request')
    async def handle_request(request):
        pass

    @app.middleware('response')
    async def custom_banner(request, response):
        response.text += ' - <3 Sanic'
        return response

    @app.route('/test')
    def handler(request):
        return text('AWESOME!')

    _, response = app.test_client.get(app.url_for('handler'))
    assert response.text == 'AWESOME! - <3 Sanic'

# Generated at 2022-06-14 07:45:56.335359
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Test:
        _future_middleware: List[FutureMiddleware] = []

    t = Test()
    t.middleware(middleware_or_request='request')
    print(t._future_middleware)

# Generated at 2022-06-14 07:46:05.653161
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    class Application(Sanic):
        @Application.middleware('request')
        def test_middleware(request):
            pass
    
    class Application_1(Sanic):
        @Application_1.middleware('request')
        def test_middleware(request):
            pass
        @Application_1.middleware('response')
        def test_middleware_1(request):
            pass
    
    assert Application._future_middleware[0]
    assert not Application_1._future_middleware[1]


# Generated at 2022-06-14 07:46:15.392973
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic(__name__)

    @app.middleware
    def my_middleware(*args, **kwargs):
        print("my_middleware...")

    # Verify that my_middleware is only added once:
    assert app._future_middleware.count(FutureMiddleware("my_middleware")) == 1

    @app.middleware("request")
    def request_middleware(*args, **kwargs):
        print("request_middleware...")

    @app.middleware("response")
    def response_middleware(*args, **kwargs):
        print("response_middleware...")

    @app.on_request()
    def on_request(*args, **kwargs):
        print("on_request...")


# Generated at 2022-06-14 07:46:29.236132
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    @TestMiddlewareMixin.middleware
    def middleware_func(*args, **kwargs):
        pass

    assert isinstance(middleware_func, FunctionType)

    @TestMiddlewareMixin.middleware('request')
    def middleware_func_1(*args, **kwargs):
        pass

    assert isinstance(middleware_func_1, FunctionType)

    assert hasattr(TestMiddlewareMixin, '_future_middleware')

# Generated at 2022-06-14 07:46:42.572047
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.exceptions import InvalidUsage
    from sanic.request import RequestParameters
    from sanic.response import HTTPResponse

    def test_middleware(request):
        return request

    app = Sanic()

    assert len(app._future_middleware) == 0

    @app.middleware
    def middleware_1(request):
        return request

    assert len(app._future_middleware) == 1

    @app.middleware('request')
    def middleware_2(request):
        return request

    assert len(app._future_middleware) == 2

    @app.middleware('response')
    def middleware_3(request, response):
        return response

    assert len(app._future_middleware) == 3


# Generated at 2022-06-14 07:46:43.252808
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:46:57.352167
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    def pass_middleware():
        pass

    # Testing on_request middleware
    app = MiddlewareMixin()
    app.middleware(pass_middleware, "request")
    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert app._future_middleware[0].attach_to == "request"
    assert app._future_middleware[0].middleware == pass_middleware

    # Testing on_response middleware
    app = MiddlewareMixin()
    app.middleware(pass_middleware, "response")
    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert app._future_middleware[0].attach_to == "response"

# Generated at 2022-06-14 07:47:07.084637
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestClass(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []
            self.middlewares = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            self.middlewares.append(middleware)
    from sanic.models.futures import FutureMiddleware
    middleware_orig = FutureMiddleware(lambda r,f,m: r, 'response')

    t = TestClass()
    t.middleware(middleware_orig)
    assert(len(t.middlewares) == 1)
    assert(t.middlewares[0] == middleware_orig)



# Generated at 2022-06-14 07:47:37.688841
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic()
    assert issubclass(MiddlewareMixin, Sanic)

    def request_middleware(request):
        pass

    def response_middleware(request, response):
        pass

    # decorator no arguments
    middleware = app.middleware(request_middleware)
    assert middleware(lambda: None) == request_middleware
    assert middleware._kwargs["attach_to"] == "request"

    # decorator with arguments
    middleware = app.middleware(request_middleware, attach_to="request")
    assert middleware(lambda: None) == request_middleware
    assert middleware._kwargs["attach_to"] == "request"

    # partial decorator
    middleware = app.middleware("request")

# Generated at 2022-06-14 07:47:46.550767
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware('request')
    def test_request_middleware(request):
        return True

    @app.middleware('response')
    def test_response_middleware(request, response):
        return True

    @app.route('/')
    async def handler(request):
        return text('OK')

    client = app.test_client

    response = client.get('/')
    assert response.status == 200

# Generated at 2022-06-14 07:47:54.493696
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    m = MiddlewareMixin()
    x = m.middleware(lambda :None)
    assert x() is None
    assert len(m._future_middleware) == 1
    assert m._future_middleware[0].middleware() is None
    m1 = Sanic('test_middleware')
    m1.on_request(lambda :None)
    assert len(m1._future_middleware) == 1
    assert m1._future_middleware[0].middleware() is None
    m1.on_response(lambda :None)
    assert len(m1._future_middleware) == 2
    assert m1._future_middleware[1].middleware() is None


# Generated at 2022-06-14 07:48:06.360579
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import unittest
    import time
    from sanic.response import text
    from sanic.server import HttpProtocol
    from sanic.app import Sanic

    class TestMiddlewareMixin(unittest.TestCase):
        def test_middleware(self):
            app = Sanic("test_middleware")

            # Try the @app.middleware decorator first
            @app.middleware
            async def test_middleware(request):
                request["middleware"] = True

            @app.middleware("response")
            async def response_middleware(request, response):
                response["middleware"] = True

            @app.get("/")
            async def handler(request):
                return text("PASS")

            _, response = app.test_client.get("/")


# Generated at 2022-06-14 07:48:19.748778
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class App(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    app = App()

    @app.middleware
    def app_middleware_01(request):
        request.ctx['middleware'].append('app_middleware_01')

    @app.middleware('response')
    def app_middleware_02(request, response):
        request.ctx['middleware'].append('app_middleware_02')

    @app.on_request
    def app_middleware_03(request):
        request.ctx['middleware'].append('app_middleware_03')

    @app.on_response
    def app_middleware_04(request, response):
        request.ctx['middleware'].append('app_middleware_04')

   

# Generated at 2022-06-14 07:48:31.948647
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def test_middleware(self):
            self._apply_middleware(self._future_middleware[0])

    instance1 = TestMiddlewareMixin()

    @instance1.middleware
    async def middleware1(request):
        pass

    @instance1.on_request
    async def middleware2(request):
        pass

    @instance1.on_response
    async def middleware3(request, response):
        pass

    instance1.test_middleware()

    assert(len(instance1._future_middleware) == 3)
    assert(instance1._future_middleware[0].middleware == middleware1)
    assert(instance1._future_middleware[1].middleware == middleware2)

# Generated at 2022-06-14 07:48:36.692911
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Sanic:
        def __init__(self):
            self._future_middleware: List[FutureMiddleware] = []

    sanic = Sanic()
    sanic.middleware(response)
    assert sanic._future_middleware[0].name == 'response'

# Generated at 2022-06-14 07:48:43.036897
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic()

    # Unit test for method middleware of class MiddlewareMixin with
    # parameter middleware_or_request is not callable
    assert app.middleware(None) != None

    # Unit test for method middleware of class MiddlewareMixin with
    # parameter middleware_or_request is callable
    assert app.middleware(None, None) != None



# Generated at 2022-06-14 07:48:47.240248
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models.futures import FutureMiddleware

    mixin = MiddlewareMixin()
    mixin.middleware(FutureMiddleware('test', 'request'))

# Generated at 2022-06-14 07:48:57.695035
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
  from main.start import app
  class TestMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      pass

    def _apply_middleware(self, future_middleware):
      pass
  test = TestMiddleware()
  @test.middleware
  def middleware_test():
    pass
  test.middleware(middleware_test)
  test.on_request(middleware_test)
  test.on_response(middleware_test)


# Generated at 2022-06-14 07:49:50.166759
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from .app import Sanic
    from .request import Request

    class FakeMiddleware():
        def __init__(self, request):
            self.request = request

        def on_request(self):
            return self.request

    class FakeMiddlewareResponse():
        def __init__(self, request):
            self.request = request

        def on_response(self):
            return self.request

    class FakeMiddlewareMixed():
        def __init__(self, request):
            self.request = request

        def on_request(self):
            return self.request

        def on_response(self):
            return self.request

    app = Sanic("test_MiddlewareMixin_middleware")
    request = Request.empty
    middleware = FakeMiddleware(request)

# Generated at 2022-06-14 07:49:58.466829
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('request')
    async def middleware1(request):
        return request

    @app.middleware('response')
    async def middleware2(request, response):
        return response

    assert 1 == len(app._future_middleware)

    app = Sanic('test_MiddlewareMixin_middleware2')

    @app.middleware
    async def middleware1(request):
        return request

    @app.middleware
    async def middleware2(request, response):
        return response

    assert 1 == len(app._future_middleware)

    app = Sanic('test_MiddlewareMixin_middleware3')


# Generated at 2022-06-14 07:50:07.200284
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestingMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._apply_middleware = self.apply_middleware
        def apply_middleware(self, middleware: MiddlewareMixin.FutureMiddleware):
            pass
        @MiddlewareMixin.middleware('request')
        def test_middleware(self, request, response):
            pass
    test = TestingMiddlewareMixin()
    assert len(test._future_middleware) == 1

# Generated at 2022-06-14 07:50:10.311917
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    self = MiddlewareMixin()
    self._future_middleware = []
    # TODO: add middleware tests




# Generated at 2022-06-14 07:40:17.227242
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Create a mock class
    class MockClass:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware) -> None:
            pass

    # Create a class with our mixin
    class MyClass(MiddlewareMixin, MockClass):
        pass

    # Perform the test
    my_class = MyClass()

    # Test case: A callable is specified as the middleware
    my_function = lambda x: x
    result = my_class.on_response(my_function)
    assert callable(result)

    # Test case: A callable is not specified as the middleware
    result = my_class.on_response()
    assert callable(result)

# Generated at 2022-06-14 07:40:19.433407
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert MiddlewareMixin.middleware
    assert MiddlewareMixin.on_response
    assert MiddlewareMixin.on_request

# Generated at 2022-06-14 07:40:24.215872
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:40:30.928377
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    from types import FunctionType
    from sanic.exceptions import SanicException
    from sanic.response import text
    app = Sanic(__name__)

    @app.on_response
    def test_middleware(response):
        return response
    assert app._future_middleware
    assert app._future_middleware[0]._future_middleware == test_middleware
    assert len(app._future_middleware) == 1


# Generated at 2022-06-14 07:40:36.343483
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class app(MiddlewareMixin):
        pass
    @app.on_response()
    def hello(request, response):
        return response
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].attach_to == "response"
    assert app._future_middleware[0].middleware == hello


# Generated at 2022-06-14 07:40:42.977424
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json

    app = Sanic()

    @app.middleware('response')
    async def print_on_response(request, response):
        print('I am a middleware, and I am attached to response')

    @app.route('/')
    async def handler(request):
        return json({'hello': 'world'})



# Generated at 2022-06-14 07:40:51.607101
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():

    class Test(MiddlewareMixin):
        def __init__(self):
            super().__init__()

        def _apply_middleware(self, middleware):
            self._future_middleware.append(middleware)

    def test():
        return 'ok'

    obj = Test()
    obj.on_request(test)

    assert obj._future_middleware[0].middleware == test
    assert obj._future_middleware[0].attach_to == "request"

    obj.on_response(test)
    assert obj._future_middleware[1].middleware == test
    assert obj._future_middleware[1].attach_to == "response"




# Generated at 2022-06-14 07:41:01.138482
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class object_test(MiddlewareMixin):
        pass
    object_test_1 = object_test()
    #  Return type of object_test_1.middleware - 'function'
    assert callable(object_test_1.middleware)
    #  Return type of object_test_1.on_request - 'function'
    assert callable(object_test_1.on_request)
    #  Return type of object_test_1.on_response - 'function'
    assert callable(object_test_1.on_response)

# Generated at 2022-06-14 07:41:12.604513
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.response import text
    app = Sanic(__name__)
    no_body = []

    # set test user middleware and test response
    @app.middleware('response')
    def request_middleware(request):
        no_body.append(True)

    @app.route('/')
    async def test(request):
        return text('hello world')

    # clean test user middleware and test response
    app.remove_middleware('request', request_middleware)
    del test

    # call test user middleware
    response = app.test_client.get('/')
    assert response.status == 200
    assert no_body == []


# Generated at 2022-06-14 07:41:14.060792
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert MiddlewareMixin().on_response()

# Generated at 2022-06-14 07:41:22.496687
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    tmm = TestMiddlewareMixin()
    def function_middleware(request, response):
        return response
    tmm.on_response(function_middleware)
    assert len(tmm._future_middleware) == 1

# Generated at 2022-06-14 07:41:25.781458
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    class FakeMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(FakeMiddlewareMixin, self).__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            print('Test _apply_middleware')


# Generated at 2022-06-14 07:41:27.366583
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert callable(MiddlewareMixin().on_response())

# Generated at 2022-06-14 07:41:40.186205
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Given:
    class call_mock:
        def __init__(self):
            self.invokes=0
        def __call__(self,*args):
            self.invokes+=1

    # When:
    #  Executing method on_response of class MiddlewareMixin
    class cMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super().__init__()
            self.mock = call_mock()
            self.attached = "response"

        def _apply_middleware(self, m):
            self.mock()
            self.attached = m.attach_to

    middlewareMixin = cMiddlewareMixin() 
    middlewareMixin.on_response()

    # Then:
    #  variable invokes of object call_mock must

# Generated at 2022-06-14 07:41:50.407685
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from unittest.mock import Mock
    from unittest.mock import patch
    tmp_dir = tempfile.mkdtemp()
    sys.path.append(tmp_dir)

    # Mock the module 'sanic.models.futures'
    MiddlewareMixin_expected = [
        "FutureMiddleware",
        "_apply_middleware",
        "_future_middleware",
        "middleware",
        "on_request",
        "on_response"
    ]
    unused_module_name = "sanic.models.futures"

    # Create a mock object for module 'sanic.models.futures'

# Generated at 2022-06-14 07:42:02.251836
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text, json

    app = Sanic()

    @app.middleware
    def middleware(request):
        key = request.args.get('key', None)

        if key is None:
            return json({'error': 'Missing key'}, status=500)

        if key != 'test':
            return text('Forbidden', status=403)

    @app.route('/')
    def index(request):
        return text('OK')

    request, response = app.test_client.get('/')
    assert response.status == 500
    assert b'"error": "Missing key"' in response.body

    request, response = app.test_client.get('/?key=test')
    assert response.status == 200
    assert response.text == 'OK'

   

# Generated at 2022-06-14 07:42:07.538300
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic, response

    app = Sanic("test_MiddlewareMixin_on_response")

    @app.middleware("response")
    async def method_response(request, response):
        pass

    assert app._future_middleware
    assert app._future_middleware
 

# Generated at 2022-06-14 07:42:15.709158
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert MiddlewareMixin.middleware.__doc__ == \
"""
        Decorate and register middleware to be called before a request.
        Can either be called as *@app.middleware* or
        *@app.middleware('request')*

        `See user guide re: middleware
        <https://sanicframework.org/guide/basics/middleware.html>`__

        :param: middleware_or_request: Optional parameter to use for
            identifying which type of middleware is being registered.
        """

# Generated at 2022-06-14 07:42:28.600483
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # 1. Arrange
    class TestClass(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            self._future_middleware.append(middleware)
    test_obj = TestClass()

    def test_func(request, response):
        pass
    # 2. Act
    result = test_obj.middleware(test_func, 'request')
    # 3. Assert
    assert test_obj._future_middleware[0].middleware == test_func
    assert callable(result)
    assert result == test_func



# Generated at 2022-06-14 07:42:42.341535
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Create a mock object
    class MockMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            self._future_middleware = list()

    # Create an instance of the mock object
    mm = MockMiddlewareMixin()
    
    # Set the expected value for the method to test
    expected_value = partial(mm.middleware, attach_to='response')
    
    # Call the method and check the results
    assert mm.on_response() == expected_value

    # Set the expected value for the method to test
    expected_value_middleware = partial(mm.middleware, attach_to='response')
    
    # Define the mock object's methods
    def mock_middleware(middleware, attach_to = "response"):
        return middleware


# Generated at 2022-06-14 07:42:53.237687
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import sanic
    app = sanic.Sanic()
    assert app._future_middleware == []

    @app.middleware
    def middleware1(request):
        pass

    assert len(app._future_middleware) == 1

    @app.middleware('request')
    def middleware2(request):
        pass

    assert len(app._future_middleware) == 2



# Generated at 2022-06-14 07:42:54.463661
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert MiddlewareMixin.middleware

# Generated at 2022-06-14 07:43:08.012403
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware
    from sanic.models.middleware import Request, Response

    app = Sanic()

    @app.middleware
    async def middleware1(request):
        """Docstring for middleware1."""
        return 'middleware1'

    @app.middleware('response')
    async def middleware2(response):
        """Docstring for middleware2."""
        return 'middleware2'

    @app.middleware
    def middleware3(request):
        """Docstring for middleware3."""
        return 'middleware3'

    @app.middleware('response')
    def middleware4(response):
        """Docstring for middleware4."""
        return 'middleware4'


# Generated at 2022-06-14 07:43:18.722188
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic("sanic-server")

    # Case: add middleware on app
    @app.middleware
    async def middleware(request):
        return request

    # Case: add middleware on app 
    @app.on_request
    async def on_request(request):
        return request

    # Case: add middleware on app
    @app.on_response
    async def on_response(request, response):
        return response

    # Case: add middleware on app with wrong param
    @app.middleware("response")
    async def middleware2(request):
        return request

# Generated at 2022-06-14 07:43:28.136234
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Application(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            MiddlewareMixin.__init__(self, *args, **kwargs)
            ## create a list to store received middleware
            self.middleware_list = []

        def _apply_middleware(self, middleware):
            self.middleware_list.append(middleware)

    # Test all 3 cases
    app = Application()
    app.middleware(lambda x: x)
    app.middleware(lambda x: x, attach_to="request")
    app.middleware("request", apply=False)(lambda x: x)

    # Test that all 3 middleware were stored
    assert len(app.middleware_list) == 3


if __name__ == "__main__":
    test_MiddlewareMix

# Generated at 2022-06-14 07:43:32.220208
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class App:
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    app = App()
    app.middleware(middleware_or_request='request')



# Generated at 2022-06-14 07:43:37.561292
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Son(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    s = Son()
    @s.middleware
    def fun():
        pass
    s.middleware == fun


# Generated at 2022-06-14 07:43:48.215234
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
	# Arrange
	class TestMiddlewareMixin(MiddlewareMixin):
		def __init__(self, *args, **kwargs) -> None:
			super().__init__(*args, **kwargs)
			self.middleware_called = False
			self.middleware_with_args_called = False
			self.middleware_with_args_called_with = None

		def _apply_middleware(self, middleware: FutureMiddleware):
			self.middleware_called = True
			self.middleware_args = args
			self.middleware_kwargs = kwargs

		async def _middleware_with_args(self, request, *args):
			self.middleware_with_args_called = True
			

# Generated at 2022-06-14 07:43:54.457821
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic()
    app.middleware(lambda x: x)

# Generated at 2022-06-14 07:44:06.915061
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import text
    app = Sanic("test_MiddlewareMixin_middleware")

    @app.middleware('request')
    async def middleware_request(request):
        request['processed_by'] = 'middleware_request'

    @app.middleware('response')
    async def middleware_response(request, response):
        response.text += '-middleware_response'
    
    @app.route('/')
    async def handler(request):
        pass

    request, response = app.test_client.get('/')

    assert request['processed_by'] == 'middleware_request'
    assert response.text == '-middleware_response'



# Generated at 2022-06-14 07:44:25.800681
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text
    from sanic.request import Request
    from sanic.exceptions import ServerError
    from sanic.response import json
    from sanic.models.futures import FutureMiddleware

    def print_request(request: Request):
        print(request)

    def increase_request_number(request: Request):
        key = "num"
        if key not in request.ctx:
            request.ctx[key] = 0
        request.ctx[key] = request.ctx[key] + 1

    def request_num_assert(request: Request):
        assert request.ctx["num"] == 2

    @middleware
    def middleware_test(request: Request):
        print_request(request)
        increase_request_number(request)


# Generated at 2022-06-14 07:44:36.142237
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Empty middleware
    middleware_mixin = MiddlewareMixin()
    assert middleware_mixin._future_middleware == []
    assert middleware_mixin.middleware.__name__ == "register_middleware"

    # Decorated middleware
    with pytest.raises(NotImplementedError):
        middleware_mixin._apply_middleware(None)

    # TODO: Add unit test for middleware(middleware_or_request, attach_to="request", apply=True)
    # TODO: Add unit test for middleware(middleware_or_request)(middleware, attach_to="request")
    # TODO: Add unit test for middleware(middleware_or_request, attach_to="response")
    # TODO: Add unit test for middleware(middleware_or_request)(middle

# Generated at 2022-06-14 07:44:37.222241
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # TODO
    pass


# Generated at 2022-06-14 07:44:43.871448
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic()
    req = "request"
    res = "response"

    @app.middleware(middleware_or_request=req)
    def request_middleware(request):
        pass

    @app.middleware(middleware_or_request=res)
    def response_middleware(request, response):
        pass

    assert len(app._future_middleware) == 2

    assert app._future_middleware[0].middleware == request_middleware
    assert app._future_middleware[0].attach_to == req

    assert app._future_middleware[1].middleware == response_middleware
    assert app._future_middleware[1].attach_to == res


# Generated at 2022-06-14 07:44:52.690711
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    import pytest

    class TestMiddlewareMixin:
        def __init__(self, *args, **kwargs):
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    app = Sanic("test_App_middleware")
    assert app._future_middleware == []

    @app.middleware
    def test_middleware1(request):
        pass

    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert app._future_middleware[0].middleware == test_middleware1

    test_middleware2 = lambda request: None


# Generated at 2022-06-14 07:45:06.413754
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    myobj = MiddlewareMixin()
    myobj.middleware(middleware_or_request = 'asd',attach_to = 'request')
    myobj.middleware(middleware_or_request = 'asd')
    myobj.middleware(middleware_or_request = lambda a,b,c : a+b+c,attach_to = 'asd')
    myobj.middleware(lambda a,b,c : a+b+c)

# Generated at 2022-06-14 07:45:19.372343
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic()

    @app.middleware('request')
    async def request_middleware(request):
        pass

    @app.middleware('response')
    async def response_middleware(request, response):
        pass

    my_middleware = lambda request: request.text
    @app.middleware(my_middleware)
    def my_middleware_2(request):
        pass

    @app.middleware('request', apply=False)
    async def request_middleware_2(request):
        pass

    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert isinstance(app._future_middleware[1], FutureMiddleware)
    assert isinstance(app._future_middleware[2], FutureMiddleware)
    assert isinstance

# Generated at 2022-06-14 07:45:22.078408
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    m = MiddlewareMixin()
    assert m.middleware  # can't test its behavior without lower layers

# Generated at 2022-06-14 07:45:34.652283
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text, HTTPResponse
    from sanic.exceptions import NotFound

    app = Sanic()

    @app.middleware
    async def handler1(request):
        return text("OK1")

    @app.middleware('response')
    async def handler2(request, response):
        return HTTPResponse("OK2")

    @app.route('/')
    async def handler3(request):
        return text("OK3")

    request, response = app.test_client.get('/')

    assert response.text == 'OK1'
    assert response.status == 200

    request, response = app.test_client.get('/1')

    assert response.text == 'Not Found'
    assert response.status == 404

    request, response

# Generated at 2022-06-14 07:45:36.227346
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    MiddlewareMixin()


# Generated at 2022-06-14 07:45:58.976119
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super().__init__()

        def _apply_middleware(self, middleware: FutureMiddleware):
            self._future_middleware.append(middleware)
            self.middleware_called_count += 1

    # pylint: disable=invalid-name
    test_app = TestMiddlewareMixin()
    test_app.middleware_called_count = 0

    @test_app.on_request
    def mock_middleware(req):
        pass

    assert len(test_app._future_middleware) == 1
    assert test_app._future_middleware[0].middleware == mock_middleware
    assert test_app._future_middleware[0].attach_to == 'request'

    assert test_

# Generated at 2022-06-14 07:46:12.696163
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.middleware import request_middleware, response_middleware, middleware
    from sanic.models.futures import FutureMiddleware
    from sanic.request import Request
    from sanic.response import HTTPResponse

    app = Sanic(__name__)
    assert app._future_middleware == []

    middleware1 = lambda x: 1
    Future_Middleware1 = FutureMiddleware(middleware1, 'request')

    middleware2 = lambda x: 2
    Future_Middleware2 = FutureMiddleware(middleware2, 'response')

    app.middleware(Future_Middleware1)
    app.middleware(Future_Middleware2)

    assert isinstance(app._future_middleware[0], FutureMiddleware) and \
           app._future

# Generated at 2022-06-14 07:46:26.118768
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class test_mixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    tmp_mixin = test_mixin(*[], **{})
    assert tmp_mixin.middleware(callable)
    tmp_mixin = test_mixin(*[], **{})
    assert tmp_mixin.middleware('request')
    tmp_mixin = test_mixin(*[], **{})
    assert tmp_mixin.middleware(callable,'request')
    tmp_mixin = test_mixin(*[], **{})
    assert tmp_mixin.middleware(callable,'response')
    tmp_mixin = test_

# Generated at 2022-06-14 07:46:39.968880
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._expect_apply_middleware = False

        def _apply_middleware(self, middleware: FutureMiddleware):
            assert self._expect_apply_middleware
            self._future_middleware.append(middleware)

    test_app = TestMiddlewareMixin()
    middleware_func = lambda req, res, _: res

    @test_app.middleware(middleware_func)
    def test_func(request):
        return request

    test_func(request=None)
    assert test_app._future_middleware
    assert test_app._future_middleware[-1].middleware == middleware_func



# Generated at 2022-06-14 07:46:49.136720
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import unittest
    import sys
    import os
    import re
    # noinspection PyProtectedMember
    from sanic import Sanic
    from sanic.plugins.sanic_pipeline.sanic_pipeline import PipelineMiddleware
    # noinspection PyProtectedMember
    from sanic.router import Router as SanicRouter

    class TestSanic(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.request_middleware = []
            self.response_middleware = []
            self.router = SanicRouter()


# Generated at 2022-06-14 07:47:01.669934
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import sanic
    from helper_class_mixin import HelperClassMixin
    app = Sanic('test_MiddlewareMixin_middleware')
    app.helper = HelperClassMixin()
    @app.middleware
    async def test_first(request):
        return request

    @app.middleware('request')
    async def test_second(request):
        return request

    @app.middleware('response')
    async def test_third(request, response):
        return response

    assert app.middleware(test_first)
    assert app.middleware(test_first, attach_to='request')
    assert app.middleware(test_first, attach_to='response')
    assert app.middleware('request')(test_second)
    assert app.middleware('response')(test_third)



# Generated at 2022-06-14 07:47:13.172392
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('request')
    async def _middleware(request):
        pass

    assert len(app._future_middleware) == 1

    @app.middleware('request')
    async def _middleware_2(request):
        pass

    assert len(app._future_middleware) == 2

    @app.middleware('response')
    async def _middleware_3(request, response):
        pass

    assert len(app._future_middleware) == 3

    @app.middleware('response')
    async def _middleware_4(request, response):
        pass

    assert len(app._future_middleware) == 4



# Generated at 2022-06-14 07:47:16.447856
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    def test_middleware(request, *args, **kwargs):
        pass
    app = Sanic()
    app.middleware(test_middleware, "request")
    assert app._future_middleware == [FutureMiddleware(test_middleware, "request")]


# Generated at 2022-06-14 07:47:28.792678
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class SanicMock:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            return

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


# Generated at 2022-06-14 07:47:31.916996
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    mw = MiddlewareMixin()
    assert(mw._future_middleware == [])
    assert(mw._apply_middleware(middleware=None) is None)

test_MiddlewareMixin_middleware()

# Generated at 2022-06-14 07:47:57.982781
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    MM = MiddlewareMixin()

    assert MM._future_middleware == []



# Generated at 2022-06-14 07:48:07.814701
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.base import Sanic
    from sanic.exceptions import RequestTimeout
    from sanic.models.futures import FutureMiddleware
    from sanic.models.middleware import Middleware

    from inspect import signature
    from sanic.response import HTTPResponse

    import sys
    import pytest

    class TestMiddlewareMixin(MiddlewareMixin, Sanic):
        def _apply_middleware(self, middleware: FutureMiddleware):
            self._middleware = middleware

    app = TestMiddlewareMixin()

    async def async_middleware_function(request):
        return None

    async def async_middleware_function_no_request(response):
        return response

    @app.middleware
    def middleware_function(request):
        return None


# Generated at 2022-06-14 07:48:09.595026
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:48:22.286926
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.base import SanicModel

    class TestApp(SanicModel, MiddlewareMixin):
        pass

    app = TestApp()

    # test middleware, attach_to = 'request'
    @app.middleware()
    def middleware1(request):
        return request
    # test middleware, attach_to = 'response'
    @app.middleware()
    def middleware2(request, response):
        return response

    assert app._future_middleware[0].middleware == middleware1
    assert app._future_middleware[0].attach_to == 'request'
    assert app._future_middleware[1].middleware == middleware2
    assert app._future_middleware[1].attach_to == 'response'

# Generated at 2022-06-14 07:48:23.492305
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    MiddlewareMixin().middleware()

# Generated at 2022-06-14 07:48:33.500569
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
	# middleware_or_request is a function
	def middleware1():
		assert True

	middleware_test = MiddlewareMixin()
	middleware_test.middleware(middleware1)

	# middleware_or_request is a string
	def middleware2():
		assert True

	middleware_test = MiddlewareMixin()
	middleware_test.middleware('request')(middleware2)

	# middleware_or_request is not a string and a function
	def middleware3():
		assert True

	middleware_test = MiddlewareMixin()
	middleware_test.middleware(0)(middleware3)


# Generated at 2022-06-14 07:48:42.070071
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    def middleware(request):
        pass

    def on_request(request):
        pass

    def on_response(request, response):
        pass

    mixin = MiddlewareMixin()
    mixin._apply_middleware = lambda x: x

    assert len(mixin._future_middleware) == 0

    mixin.middleware(middleware)
    assert len(mixin._future_middleware) == 1
    assert mixin._future_middleware[0].middleware == middleware
    assert mixin._future_middleware[0].attach_to == "request"

    mixin.middleware(middleware, 'response')
    assert len(mixin._future_middleware) == 2
    assert mixin._future_middleware[1].middleware == middleware

# Generated at 2022-06-14 07:48:50.928509
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models.futures import FutureMiddleware
    app = Sanic('test_MiddlewareMixin_middleware')
    app.logger.disabled = True

    @app.middleware('response')
    async def test_on_response(request):
        return request

    @app.middleware
    async def test_on_request(request):
        return request

    assert len(app._future_middleware) == 2
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert isinstance(app._future_middleware[1], FutureMiddleware)
    assert app._future_middleware[0].middleware == test_on_request
    assert app._future_middleware[1].middleware == test_on_response
    assert app._future_middleware

# Generated at 2022-06-14 07:49:00.044435
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    from sanic import Sanic
    from sanic.models.middlewares import Middleware

    app = Sanic("sanic-middleware")

    @app.middleware("request")
    async def test_middleware_01(request):
        return

    @app.middleware("request")
    async def test_middleware_02(request):
        return

    @app.middleware("response")
    async def test_middleware_03(request, response):
        return

    assert len(app._future_middleware) == 3
    assert type(app._future_middleware[0]) == Middleware



# Generated at 2022-06-14 07:49:07.099683
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Session:
        def __init__(self, host, port, debug):
            self._future_middleware = []
            self._future_middleware.append(FutureMiddleware("123", "request"))

        def _apply_middleware(self, middleware: FutureMiddleware):
            return

    session = Session("host", "port", "debug")
    session.middleware("request")
    session.on_request("request")
    session.on_response("response")

# Generated at 2022-06-14 07:50:04.621042
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Example_MiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            return

    example_middleware = Example_MiddlewareMixin()
    def test_middleware(request):
        pass

    @example_middleware.middleware
    def test_middleware_1(request):
        pass

    assert len(example_middleware._future_middleware) == 1
    assert example_middleware._future_middleware[0].middleware == test_middleware_1
    assert example_middleware._future_middleware[0].attach_to == "request"

    @example_middleware.middleware("request")
    def test_middleware_2(request):
        pass

    assert len(example_middleware._future_middleware) == 2
    assert example
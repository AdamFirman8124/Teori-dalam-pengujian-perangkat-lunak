

# Generated at 2022-06-14 07:39:59.916562
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    app = Sanic("test_sanic")
    app.on_response(middleware=None)


# Generated at 2022-06-14 07:40:06.990192
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    app = MiddlewareMixin()
    def request_handler(req):
        return

    def response_handler(req, resp):
        return

    # Register request and response middleware using method middleware
    @app.middleware('request')
    def request_handler(req):
        return
    
    @app.middleware('response')
    def response_handler(req, resp):
        return
    
    # Register request and response middleware using shortcut method
    @app.on_request
    def request_handler2(req):
        return
    
    @app.on_response
    def response_handler2(req, resp):
        return
    
    assert len(app._future_middleware) == 4
    assert callable(app._future_middleware[0]._middleware_func)

# Generated at 2022-06-14 07:40:09.216059
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from mysancy.server import app as mysancy_app
    assert mysancy_app.on_response()

# Generated at 2022-06-14 07:40:11.469355
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class App(MiddlewareMixin):
        pass

    app = App()

    app.on_response(middleware=None)

# Generated at 2022-06-14 07:40:24.456662
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Test without passing attach_to, attaching to request
    import sanic
    app = sanic.Sanic("test_MiddlewareMixin_middleware")

    @app.middleware
    def simple_middleware(request):
        pass

    assert len(app._future_middleware) == 1
    with pytest.raises(TypeError) as excinfo:
        app.middleware("not callable")
    assert 'is not callable' in str(excinfo.value)
    with pytest.raises(TypeError) as excinfo:
        app._apply_middleware("not a future_middleware")
    assert 'is not a FutureMiddleware' in str(excinfo.value)

    # Test with passing attach_to, attaching to response

# Generated at 2022-06-14 07:40:37.050833
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # The test target
    class Obj:
        def _apply_middleware(self,middleware):
            return middleware
    obj = Obj()

    # assertion of method middleware of class MiddlewareMixin
    # @app.middleware
    test1_expected = "test1"
    test1_actual = obj.middleware(test1_expected)()
    assert test1_actual == test1_expected

    # @app.middleware('request')
    test2_actual = obj.middleware(test1_expected,'request')()
    assert test2_actual == test1_expected

    # @app.middleware('response')
    test3_actual = obj.middleware(test1_expected,'response')()
    assert test3_actual == test1_expected


# Generated at 2022-06-14 07:40:49.428036
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestClass:
        def __init__(self):
            self.midd = MiddlewareMixin()
            self.mid = None

        def _apply_middleware(self, middleware):
            self.mid = middleware

        def func1(self):
            pass

        def func2(self):
            pass

        def func3(self):
            pass

    obj = TestClass()

    obj.midd.middleware(obj.func1)
    obj.midd.middleware(obj.func2, 'response')
    obj.midd.middleware(obj.func3, 'request')

    assert obj.mid.middleware == obj.func1
    assert obj.mid.attach_to == 'request'
    assert obj.mid.apply == True

    assert obj.mid.middleware == obj.func2


# Generated at 2022-06-14 07:40:55.828734
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    mm: MiddlewareMixin = MiddlewareMixin()

    # get partial object
    result = mm.on_response()
    assert callable(result)
    assert result.args == ()
    assert result.keywords == {'attach_to': 'response'}

    # get decorator
    @result
    def somefunc(a, b):
        pass
    assert somefunc.__name__ == 'somefunc'
    assert mm._future_middleware[0].middleware == somefunc
    assert mm._future_middleware[0].attach_to == 'response'

# Generated at 2022-06-14 07:41:01.885859
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Using mock objects to simulate a HTTP response object
    request_obj = 'request_obj'
    response_obj = 'response_obj'
    mock_request = MagicMock()
    mock_request.response = mock_request.response_class(response_obj)
    # Create an instance of the class
    middleware_mixin = MiddlewareMixin()
    # Call the method using a mock object to simulate a method
    middleware_mixin.on_response(lambda request, response: (request, response))(
        mock_request, mock_request.response
    )
    # Check if the method to be called was called
    mock_request.assert_called_once_with(mock_request, mock_request.response)


# Generated at 2022-06-14 07:41:08.669882
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    '''
    test_MiddlewareMixin_middleware: unit tests method middleware of class MiddlewareMixin
    '''
    # Create a test instance of MiddlewareMixin
    a = MiddlewareMixin()

    # Create a FutureMiddleware object
    fm = FutureMiddleware(None, None)

    # Call the method _apply_middleware
    a._apply_middleware(fm)

# Generated at 2022-06-14 07:41:20.272526
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class App(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    app = App()
    @app.middleware('response')
    def middleware1(request):
        return True
    @app.middleware('response')
    def middleware1(request):
        return True
    @app.on_request()
    def middleware2(request):
        return True
    assert len(app._future_middleware) == 3

test_MiddlewareMixin_middleware()

# Generated at 2022-06-14 07:41:29.167617
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic
    from sanic.views import HTTPMethodView

    app = Sanic('test_MiddlewareMixin_on_request')

    @app.middleware('request')
    async def print_on_request(request):
        print("I am request1")

    @app.middleware('request')
    async def print_on_request(request):
        print("I am request2")

    @app.middleware('response')
    async def print_on_response(request, response):
        print("I am response1")

    @app.middleware('response')
    async def print_on_response(request, response):
        print("I am response2")

    @app.get('/')
    async def handler(request):
        return text('OK')


# Generated at 2022-06-14 07:41:42.263478
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    import random

    app = Sanic('test')
    @app.middleware
    def request_middleware(request):
        request['request_middleware'] = random.random()
    @app.middleware('request')
    def request_middleware_2(request):
        request['request_middleware_2'] = random.random()

    @app.route('/')
    async def handler(request):
        return HTTPResponse()

    request, response = app.test_client.get('/')
    assert request.get('request_middleware') == request.get('request_middleware_2')

# Generated at 2022-06-14 07:41:55.111838
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import json

    app = Sanic()

    async def simple_middleware(request, handler):
        return json({"Hello": "World"})

    @app.middleware
    async def simple_middleware_2(request, handler):
        return json({"Hello": "World"})

    @app.middleware("response")
    async def simple_middleware_3(request, handler):
        return json({"Hello": "World"})

    app.add_route(
        simple_middleware,
        "/middleware",
        methods=["GET", "POST"],
    )

    app.add_route(
        simple_middleware_2,
        "/middleware_2",
        methods=["GET", "POST"],
    )

    app.add_

# Generated at 2022-06-14 07:42:06.815946
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    async def mw1(request):
        req_middleware_called.append(1)

    @app.middleware('request')
    async def mw2(request):
        req_middleware_called.append(2)

    @app.middleware('response')
    async def mw3(request, response):
        res_middleware_called.append(3)

    @app.route('/1')
    async def handler1(request):
        return text('OK')

    request, response = app.test_client.get('/1')
    assert response.status == 200
    assert b'OK' in response.body

    assert req_middle

# Generated at 2022-06-14 07:42:16.281582
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    import json
    import sanic.app

# Generated at 2022-06-14 07:42:20.193567
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class Demo(MiddlewareMixin):
        pass
    demo = Demo()
    assert demo.on_request
    assert demo.on_request(lambda x,y: x * y)


# Generated at 2022-06-14 07:42:26.805506
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.app import Sanic
    from sanic.request import Request
    app = Sanic("test_on_request")
    app.on_response(print)
    assert app._future_middleware[0].attach_to == "response"

    @app.route("/test")
    async def handler(request):
        return TextResponse("test")


# Generated at 2022-06-14 07:42:30.350193
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    app = MiddlewareMixin()
    request_middleware = app.on_request()
    assert callable(request_middleware)
    assert request_middleware.__name__ == 'register_middleware'


# Generated at 2022-06-14 07:42:39.179134
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MyMiddleWareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
        def _apply_middleware(self, middleware: FutureMiddleware):
            print(middleware)

    my_app = MyMiddleWareMixin()
    return my_app.middleware, my_app.on_request, my_app.on_response

# Test the MiddlewareMixin

# Generated at 2022-06-14 07:42:43.880601
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    result = MiddlewareMixin().on_request(middleware=None)
    assert result == partial(MiddlewareMixin().middleware, attach_to="request")


# Generated at 2022-06-14 07:42:51.885807
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')
    # right
    @app.middleware
    async def middleware(request):
        pass
    # right
    @app.middleware('request')
    async def middleware(request):
        pass
    # right
    @app.on_request
    async def middleware(request):
        pass
    # right
    @app.on_response
    async def middleware(request):
        pass

    # wrong: will throw error
    @app.middleware('wrong')
    async def middleware_wrong(request):
        pass

# Generated at 2022-06-14 07:42:55.741067
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic

    app = Sanic()

    @app.on_request
    def request_middleware(request):
        return request

    assert app._future_middleware is not None


# Generated at 2022-06-14 07:43:07.248260
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class TestMiddleware:
        def __init__(self, app, request, attach_to='request'):
            pass
        
        async def __call__(self, request):
            print('processing request')

    class TestClass(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            print('Middleware applied')

    test_class = TestClass()
    test_class.on_request(TestMiddleware)
    assert(len(test_class._future_middleware) == 1)



# Generated at 2022-06-14 07:43:15.560432
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class TestMiddlewareMixin(MiddlewareMixin): pass

    mixin = TestMiddlewareMixin()

    @mixin.on_request()
    def middleware(request): pass

    assert mixin._future_middleware[0].attach_to == "request"

    @mixin.on_request
    def middleware(request): pass

    assert mixin._future_middleware[1].attach_to == "request"


# Generated at 2022-06-14 07:43:26.156499
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class SubMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
        async def add(self, i, j):
            return i + j

    @SubMiddlewareMixin.on_request()
    def test_middleware(req, res):
        pass

    assert issubclass(SubMiddlewareMixin, MiddlewareMixin)
    assert issubclass(SubMiddlewareMixin, MiddlewareMixin)
    assert SubMiddlewareMixin.on_request.__name__ == "on_request"
    assert SubMiddlewareMixin.on_request() == test_middleware


# Generated at 2022-06-14 07:43:32.286639
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    try:
        instance = MiddlewareMixin()
        on_request = instance.on_request()
        assert callable(on_request)
        assert hasattr(on_request, '__call__')
    except Exception as e:
        print(f"Test 1 failed with {e}")


# Generated at 2022-06-14 07:43:37.143857
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    test_mixin=MiddlewareMixin()
    assert callable(test_mixin.on_request())
    assert callable(test_mixin.on_request(middleware=test_MiddlewareMixin_on_request))


# Generated at 2022-06-14 07:43:43.640590
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.app import Sanic
    from sanic.response import text
    app = Sanic()
    
    @app.middleware
    async def is_website_up(request):
        return text('Hola!')
    
    @app.route('/')
    async def test(request):
        return text('Hello World!')
    
    request, response = app.test_client.get('/')
    assert response.text == 'Hola!'


# Generated at 2022-06-14 07:43:45.949132
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    pass


# Generated at 2022-06-14 07:44:00.484325
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Test MiddlewareMixin.middleware without apply
    mm = MiddlewareMixin()
    try:  # Test for middleware with wrong type
        mm.middleware(1)
    except NotImplementedError:
        pass
    except Exception:
        assert False
    try:  # Test for middleware with wrong type attach to
        mm.middleware(test_MiddlewareMixin_middleware, 1)
    except TypeError:
        pass
    except Exception:
        assert False
    try:  # Test for middleware with wrong tag
        mm.middleware(test_MiddlewareMixin_middleware, 'UNKNOWN')
    except TypeError:
        pass
    except Exception:
        assert False
    mm.middleware(test_MiddlewareMixin_middleware)  # Test for middleware with default type
    mm.middle

# Generated at 2022-06-14 07:44:03.897836
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    # Case 1: middleware == None
    # Case 2: middleware == callable
    # None
    pass

# Generated at 2022-06-14 07:44:09.600490
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            assert middleware.attach_to == "request"
            assert callable(middleware.middleware)

    TestMiddlewareMixin().on_request(lambda x: x)


# Generated at 2022-06-14 07:44:16.626782
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    # arrange
    from sanic.app import Sanic

    app = Sanic("test_MiddlewareMixin_on_request")

    # act
    @app.on_request
    async def middleware(request):
        pass

    # assert
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].type == "request"
    assert app._future_middleware[0].middleware == middleware
    assert not app._future_middleware[0].is_app_route

# Generated at 2022-06-14 07:44:19.921612
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    # Arrange

    # Act
    result = MiddlewareMixin().on_request()

    # Assert
    assert isinstance(result, partial)


# Generated at 2022-06-14 07:44:23.223420
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class FakeApp(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            print(middleware)
    FakeApp()

# Generated at 2022-06-14 07:44:32.930817
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.app import Sanic
    
    app = Sanic()
    
    # Test with middleware
    def on_request(request):
        pass
    result = app.on_request(on_request)
    assert result == None
    
    # Test without middleware
    result = app.on_request()
    
    assert result() == None
    assert result(1) == None
    assert result(None) == None
    assert result(1.1) == None
    assert result("a") == None
    assert result(False) == None
    assert result([]) == None
    assert result({}) == None


# Generated at 2022-06-14 07:44:44.272251
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    print('===test_MiddlewareMixin_on_request===')
    class MiddlewareMixinTest(MiddlewareMixin):
        pass
    @MiddlewareMixinTest.on_request()
    def middleware_test():
        return None
    @MiddlewareMixinTest.on_request()
    def middleware_test2():
        return None
    @MiddlewareMixinTest.on_request(middleware_test)
    def middleware_test3():
        return None
    print(MiddlewareMixinTest._future_middleware)
    MiddlewareMixinTest._future_middleware = []
    print(MiddlewareMixinTest._future_middleware)


# Generated at 2022-06-14 07:44:52.788900
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super().__init__()

    test1 = TestMiddlewareMixin()
    test2 = TestMiddlewareMixin()


    def register_middleware(middleware, attach_to="request"):
        if attach_to == "request":
            assert middleware == "test"
            assert attach_to == "request"
            return "test request"
        elif attach_to == "response":
            assert middleware == "test"
            assert attach_to == "response"
            return "test response"
        else:
            return None

    test1.middleware = register_middleware
    assert test1.on_request("test") == "test request"
    test2.middleware = register_middleware

# Generated at 2022-06-14 07:45:02.919436
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json

    app = Sanic('test_Middleware')
    print(app.__dict__)

    @app.middleware('response')
    async def cors_headers(request, response):
        response.headers['X-Custom-Header'] = 'blue'

    @app.route('/')
    async def handler(request):
        return json({'result': 'OK'})

    request, response = app.test_client.get('/')
    assert response.headers.get('X-Custom-Header') == 'blue'

# Generated at 2022-06-14 07:45:18.352514
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            print(middleware)

    a = A()
    @a.middleware
    async def b():
        pass
    @a.middleware('c')
    async def d():
        pass

    assert b == a._future_middleware[0].middleware
    assert 'c' == a._future_middleware[1].attach_to


# Generated at 2022-06-14 07:45:25.208582
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

    test_middleware_mixin = TestMiddlewareMixin()

    @test_middleware_mixin.middleware
    def test_middleware_decorator(request):
        print("test_middleware_decorator")
        return request

    assert isinstance(test_middleware_mixin._future_middleware, list)
    assert len(test_middleware_mixin._future_middleware) == 1


# Generated at 2022-06-14 07:45:30.693772
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware

    class Middleware:
        pass

    app = Sanic()
    app.middleware(Middleware())
    assert isinstance(app._future_middleware[0], FutureMiddleware)



# Generated at 2022-06-14 07:45:41.676423
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # create a new instance of MiddlewareMixin
    middlewareMixin = MiddlewareMixin()
    # create a new instance of FutureMiddleware and add it to _future_middleware list
    middlewareMixin._future_middleware.append(FutureMiddleware(None, None))
    # set the length of _future_middleware list to length
    length = len(middlewareMixin._future_middleware)
    # assert length is equal to 1
    assert length == 1, "The length is not equal to 1"
    # create a new instance of FutureMiddleware and add it to _future_middleware list
    middlewareMixin._future_middleware.append(FutureMiddleware(None, None))
    # set the length of _future_middleware list to length2
    length2 = len(middlewareMixin._future_middleware)


# Generated at 2022-06-14 07:45:46.423331
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic(__name__)

    async def middleware_test(request):
        pass

    app.middleware(middleware_test)

    assert len(app._future_middleware) == 1

# Generated at 2022-06-14 07:45:47.152376
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert 1 == 1

# Generated at 2022-06-14 07:45:52.475207
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class __MiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            pass

        async def _apply_middleware(self, middleware):
            pass
    m = __MiddlewareMixin()
    result = m.middleware(request=None, attach_to="request", apply=True)
    assert result.keywords['attach_to'] == 'request'


# Generated at 2022-06-14 07:46:01.057793
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.request import Request
    
    async def foo(request: Request):
        assert True
    
    app = Sanic("test_MiddlewareMixin_middleware")
    app.middleware("request")(foo)
    app.middleware("response")(foo)
    
    # Request cant be mocked
    # request = Request("GET", "/")
    # app.handle_request(request)


# Generated at 2022-06-14 07:46:13.642371
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    app = MiddlewareMixin()
    assert app._future_middleware == []
    @app.middleware
    def example_middleware(request):
        return "example_middleware"
    assert app._future_middleware[0] == FutureMiddleware(example_middleware, "request")
    assert app._future_middleware[0].middleware == example_middleware
    assert app._future_middleware[0].attach_to == "request"
    @app.middleware('response')
    def example_middleware1(request):
        return "example_middleware1"
    assert app._future_middleware[1] == FutureMiddleware(example_middleware1, "response")
    assert app._future_middleware[1].middleware == example_middleware1
    assert app._future_middleware[1].attach_

# Generated at 2022-06-14 07:46:26.339936
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text
    from sanic.views import HTTPMethodView
    from sanic.models.constants import HTTP_METHODS
    for method in HTTP_METHODS:
        if method in ('HEAD', 'OPTIONS'):
            continue
        app = Sanic(__name__)

        # Use a class-based handler
        class Handler(HTTPMethodView):
            def post(self, request):
                return text("I'm post response")

        app.add_route(Handler.as_view(), '/')

        @app.middleware('request')
        async def before(request):
            return text("I'm before request")

        @app.middleware('request')
        async def before2(request):
            return text("I'm before request2")

       

# Generated at 2022-06-14 07:46:42.649822
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Bot:
        def __init__(self):
            self.request = None

    bot = Bot()
    bot.middleware(lambda request: bot.request)
    assert bot.request == None


# Generated at 2022-06-14 07:46:54.522795
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import unittest
    import sanic
    class A(MiddlewareMixin):
        pass
    a = A()
    def f():
        pass
    a.middleware(f)
    @a.on_request
    def f():
        pass
    @a.on_response
    def f():
        pass
    class B(sanic.Sanic):
        pass
    b = B()
    b.middleware(f)
    @b.on_request
    def f():
        pass
    @b.on_response
    def f():
        pass
    unittest.main(argv=[''])

# Generated at 2022-06-14 07:47:02.904188
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json
    import pytest
    app = Sanic(__name__)
    @app.middleware()
    async def new_middleware(request):
        print("new middleware")
        return await request.app.middleware.get('request')(request)
    @app.route("/")
    async def test(request):
        assert isinstance(request.app.middleware.get('request'), list)
        return json({"test": True})

    request, response = app.test_client.get('/')
    assert response.status == 200



# Generated at 2022-06-14 07:47:12.292604
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import text
    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    def example_middleware_1(request):
        pass

    @app.middleware('request')
    def example_middleware_2(request):
        pass

    @app.middleware('response')
    def example_middleware_3(request, response):
        pass

    @app.route('/')
    def handler(request):
        return text('OK')

    request, response = app.test_client.get('/')

    assert response.text == 'OK'

# Generated at 2022-06-14 07:47:20.733279
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Arrange
    from sanic.app import Sanic

    app = Sanic(__name__)

    # Act
    @app.middleware('request')
    def my_middleware(request):
        print(request)

    @app.middleware
    def my_middleware2(request):
        print(request)

    @app.on_request
    def my_middleware3(request):
        print(request)
    
    @app.on_response
    def my_middleware4(request, response):
        print(request)
        print(response)

    # Assert
    assert isinstance(app._future_middleware, list)
    assert len(app._future_middleware) == 4
    assert app._future_middleware[0].attach_to == "request"
    assert app._future_

# Generated at 2022-06-14 07:47:27.603620
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import sanic
    app = sanic.Sanic('test_MiddlewareMixin_middleware')
    app.middleware('middleware')
    app.middleware('middleware2')
    assert len(app._future_middleware) == 2
    assert app._future_middleware[0].middleware_func == 'middleware'
    assert app._future_middleware[1].middleware_func == 'middleware2'


# Generated at 2022-06-14 07:47:37.236627
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.server import HttpProtocol

    app = Sanic('test_MiddlewareMixin_middleware')


    @app.middleware('request')
    async def before_request(request):
        return True

    app.http_protocol = HttpProtocol(app, None)

    app._apply_middleware(app._future_middleware[-1])
    assert app.request_middleware[0](None) is True


    @app.middleware('response')
    async def after_request(request, response):
        return False

    app._apply_middleware(app._future_middleware[-1])
    assert app.response_middleware[0](None, None) is False



# Generated at 2022-06-14 07:47:48.997653
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class ClassMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super().__init__()

    def m1(request):
        print("m1")
        return request

    def m2(request):
        print("m2")
        return request

    def m3(request):
        print("m3")
        return request

    # Test callable object passed as a parameter
    cmm = ClassMiddlewareMixin()
    assert cmm._future_middleware == []
    cmm.middleware(m1, 'request')
    assert cmm._future_middleware == [FutureMiddleware(m1, 'request')]
    cmm.middleware(m2, 'response')

# Generated at 2022-06-14 07:48:02.631330
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware('request')
    async def request_1(request):
        pass
    assert request_1.__name__ == 'request_1'
    assert request_1.__module__ == 'test_MiddlewareMixin_middleware'
    @app.middleware()
    async def request_2(request):
        pass
    assert request_2.__name__ == 'request_2'
    assert request_2.__module__ == 'test_MiddlewareMixin_middleware'
    @app.middleware('response')
    async def request_3(request):
        pass
    assert request_3.__name__ == 'request_3'
    assert request_3.__module__ == 'test_MiddlewareMixin_middleware'



# Generated at 2022-06-14 07:48:09.132902
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic(__name__)


    def middleware1(res):
        print("middleware1")
        return res

    def middleware2(req):
        print("middleware2")
        return req

    @app.middleware(middleware2)
    async def handler(request):
        print("handler is called!")

    # test the response middleware
    res = middleware1(None)
    assert res is None

    # test the request middleware
    # find that the request middleware is not working
    h = handler
    assert h is handler


if __name__=="__main__":
    test_MiddlewareMixin_middleware()



# Generated at 2022-06-14 07:48:43.354297
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    instance = Sanic()
    def middleware(request):
        nonlocal request_called
        request_called = True
        return request
    instance.middleware(middleware, attach_to="request")
    assert len(instance._future_middleware) == 1
    request_called = False
    request = 'foo'
    result = instance._apply_middleware(instance._future_middleware[0])(request)
    assert request_called == True
    assert result == request

# Generated at 2022-06-14 07:48:49.025988
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Create a new class that inherits class MiddlewareMixin
    class MiddlewareMixin_Test(MiddlewareMixin):
        def __init__(self):
            self._future_middleware = []

    # Create a new object of class MiddlewareMixin_Test
    middlewareMixin_Test = MiddlewareMixin_Test()

    # test case 1
    @middlewareMixin_Test.middleware
    def test_middleware1(request):
        print('In test_middleware1')
        pass

    assert(len(middlewareMixin_Test._future_middleware) == 1)
    assert(middlewareMixin_Test._future_middleware[0].middleware == test_middleware1)
    assert(middlewareMixin_Test._future_middleware[0].attach_to == 'request')

    # test

# Generated at 2022-06-14 07:48:56.773026
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    
    class FutureMiddlewareMock:
        def __init__(self, middleware, attach_to="request"):
            self._middleware = middleware
            self._attach_to = attach_to
    
    app = Sanic("name_mock")
    app._apply_middleware = lambda x: None

    @app.middleware('request')
    def request_middleware(request):
        pass

    @app.middleware("response")
    def response_middleware(request, response):
        pass

    assert len(app._future_middleware) == 2
    assert isinstance(app._future_middleware[0], FutureMiddlewareMock)
    assert isinstance(app._future_middleware[1], FutureMiddlewareMock)
    assert app._future_middleware

# Generated at 2022-06-14 07:49:06.674262
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    import pytest
    from sanic.models.futures import FutureMiddleware


    class MiddlewareMixinTest(MiddlewareMixin):

        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError


    @MiddlewareMixinTest.middleware
    def foo(request):
        pass

    @MiddlewareMixinTest.on_request
    def bar(request):
        pass


# Generated at 2022-06-14 07:49:16.791938
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.response import HTTPResponse

    class Temp:
        def __init__(self, *args, **kwargs):
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            return middleware

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
                return

# Generated at 2022-06-14 07:49:27.404962
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    '''
    Unit test for testing method "middleware" in class "MiddlewareMixin"
    '''
    from sanic.app import Sanic

    def test_middleware(request,response):
        return actual
    
    app = Sanic(__name__)
    actual = app.middleware(test_middleware, attach_to="response")
    assert actual.__name__ == 'test_middleware'
    assert actual.__closure__[0].cell_contents == 'response'
    assert actual.__closure__[1].cell_contents == test_middleware



# Generated at 2022-06-14 07:49:35.799014
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import text
    from sanic.request import Request
    from sanic import Blueprint

    
    def middleware_func(request):
        return text("ok")
    
    
    def middleware_func_response(request, response):
        return response
    
    app = Sanic('test')
    app.blueprint(Blueprint(__name__))
    bp = Blueprint('test_bp')

    app.blueprint(bp)
    
    @bp.middleware('request')
    def middleware_func_bp(request):
        return text("ok")
    
    
    @bp.middleware('response')
    def middleware_func_bp_response(request, response):
        return response
    

# Generated at 2022-06-14 07:49:43.644489
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    class MyMiddlewareClass:
        def hanlder(self, request):
            print(request)

    app = Sanic()
    app.middleware(MyMiddlewareClass().hanlder, attach_to="request")

    assert app._future_middleware[0].add_to == "request"
    assert app._future_middleware[0].handler == MyMiddlewareClass().hanlder



# Generated at 2022-06-14 07:49:51.892359
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class _Middleware(object):
        def __init__(self, *args, **kwargs):
            super(_Middleware, self).__init__(*args, **kwargs)
            self._future_middleware = []

    _Middleware.middleware = MiddlewareMixin.middleware.__get__
    _Middleware.on_request = MiddlewareMixin.on_request.__get__
    _Middleware.on_response = MiddlewareMixin.on_response.__get__

    x = _Middleware()
    assert type(x.middleware) is type(MiddlewareMixin.middleware)
    assert type(x.on_request) is type(MiddlewareMixin.on_request)
    assert type(x.on_response) is type(MiddlewareMixin.on_response)

# Generated at 2022-06-14 07:50:03.461418
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic('test')
    m1 = app.middleware('request')
    def middleware_fun():
        pass
    m2 = app.middleware(middleware_fun, 'request')
    m3 = app.middleware(middleware_fun, attach_to='request')
    m4 = app.middleware(attach_to='request')(middleware_fun)
    assert m1.__name__ == 'register_middleware'
    assert m2.__name__ == 'middleware_fun'
    assert m3.__name__ == 'middleware_fun'
    assert m4.__name__ == 'middleware_fun'

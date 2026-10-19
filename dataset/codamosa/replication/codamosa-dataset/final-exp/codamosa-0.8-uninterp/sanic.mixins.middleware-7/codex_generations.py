

# Generated at 2022-06-14 07:40:23.548968
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json
    from sanic.views import HTTPMethodView

    app = Sanic("test_MiddlewareMixin_middleware")

    @app.middleware("response")
    async def process_response(request, response):
        return json({"processed": True})

    @app.route("/")
    async def handler(request):
        return json({"test": True})

    request, response = app.test_client.get("/")

    assert response.json.get("processed")

    class ExampleView(HTTPMethodView):
        @app.middleware("response")
        async def process_response(self, request, response):
            return json({"processed": True})

    ExampleView.get = app.route("/test2/")

# Generated at 2022-06-14 07:40:26.630423
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    foo = MiddlewareMixin()
    @foo.on_request()
    def on_request():
        pass
    assert isinstance(foo._future_middleware[0], FutureMiddleware)


# Generated at 2022-06-14 07:40:29.766959
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert MiddlewareMixin.on_response("middleware")("response") == "response"

# Generated at 2022-06-14 07:40:41.443010
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class App(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            self._future_middleware.append(middleware)
    app = App()

    # test method @middleware
    @app.middleware
    def m1(request):
        return request
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].attach_to == "request"
    assert app._future_middleware[0].middleware == m1

    # test default attach_to: request
    @app.middleware('response')
    def m2(request):
        return request
    assert len(app._future_middleware) == 2
    assert app._future_middleware[1].attach_to == "response"
    assert app._future_middleware[1].middleware

# Generated at 2022-06-14 07:40:43.879056
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    MiddlewareMix_obj = MiddlewareMixin()
    MiddlewareMix_obj.on_response(middleware="response")

# Generated at 2022-06-14 07:40:56.601399
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """Unit test for method middleware of class MiddlewareMixin"""
    # Test with a simple decorator
    @MiddlewareMixin.middleware
    def test_middleware(request):
        print("middleware")
        return request

    class TestMiddlewareClass:
        """Test class for unit test of method middleware of class
        MiddlewareMixin"""

        @MiddlewareMixin.middleware
        def __call__(self, request):
            print("middleware")
            return request

    # Test with a class
    test_middleware_class = TestMiddlewareClass()
    # Test with the class instance
    test_middleware_class.middleware()



# Generated at 2022-06-14 07:41:05.684894
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.blueprints import Blueprint

    bp = Blueprint('bp', url_prefix='/dummy')
    bp.middleware = MiddlewareMixin.middleware
    bp.on_response = MiddlewareMixin.on_response

    @bp.on_response
    def testfunc(request, response):
        pass
    
    assert len(bp._future_middleware) == 1
    assert bp._future_middleware[0].middleware == testfunc

# Generated at 2022-06-14 07:41:07.953592
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    def middleware():
        pass

    mixin = MiddlewareMixin()
    on_response = mixin.on_response
    assert on_response(middleware) == middleware



# Generated at 2022-06-14 07:41:10.359115
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    assert MiddlewareMixin().on_request(middleware=None)

# Generated at 2022-06-14 07:41:23.999386
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MyMiddlewareMixin(MiddlewareMixin):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            self._middleware.append(middleware)

    def my_middleware():
        pass

    my_middleware_mixin = MyMiddlewareMixin()
    my_middleware_mixin.middleware(my_middleware)

    assert len(my_middleware_mixin._future_middleware) == 1
    assert my_middleware_mixin._future_middleware[0].middleware == my_middleware

    assert len(my_middleware_mixin._middleware) == 1
    assert my_middleware_mixin

# Generated at 2022-06-14 07:41:39.307357
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware
    from sanic.middleware import CORSHeadersMiddleware, ErrorsMiddleware
    from sanic.response import text

    async def handler(request, *args, **kwargs):
        return text("Hi")

    app = Sanic("MiddlewareMixin")

    @app.route("/")
    def handler(request, *args, **kwargs):
        return text('hi~')

    application = app.asgi()

    app.middleware(CORSHeadersMiddleware())
    app.middleware(ErrorsMiddleware())

    assert len(app._future_middleware) == 2
    assert any(isinstance(middleware, FutureMiddleware) for middleware in app._future_middleware)

    futures = app._future

# Generated at 2022-06-14 07:41:40.587516
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass



# Generated at 2022-06-14 07:41:47.142029
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    app = MiddlewareMixin()
    def middleware(request):
        pass
    app.on_request(middleware)
    assert app._future_middleware[0].middleware == middleware
    assert app._future_middleware[0].attach_to == "request"


# Generated at 2022-06-14 07:41:53.287349
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware('request')
    def attach_stuff(request):
        request["stuff"] = {'from': 'test_MiddlewareMixin_middleware'}

    @app.middleware('response')
    def detach_stuff(request, response):
        response['stuff'] = {'from': 'test_MiddlewareMixin_middleware'}

    @app.route('/')
    async def handler(request):
        return text("OK")

    request, response = app.test_client.get('/')
    assert response.status == 200
    assert response.text == 'OK'

    assert request.args.get("from_request") == 'test_MiddlewareMixin_middleware'
    assert response

# Generated at 2022-06-14 07:42:02.533766
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    def foo(request):
        pass
    def bar(request):
        pass
    a = A()
    a.on_request(foo)
    a.on_response(bar)
    assert len(a._future_middleware) == 2
    assert a._future_middleware[0].middleware == foo
    assert a._future_middleware[1].middleware == bar

# Generated at 2022-06-14 07:42:11.241388
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MyMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        # Unit test for method _apply_middleware of class MiddlewareMixin
        def _apply_middleware(self, middleware: FutureMiddleware):
            return True

    app = MyMiddlewareMixin()

    # Unit test for case when @middleware('request')
    @app.on_request
    async def request_handler(request):
        return True

    assert app._future_middleware[-1].middleware == request_handler
    assert app._future_middleware[-1].attach_to == "request"
    assert app._future_middleware[-1].middleware(app, 1) == True
    del app._future

# Generated at 2022-06-14 07:42:19.422207
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixinTest(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._test = 0

        def _apply_middleware(self, middleware: FutureMiddleware):
            if middleware.attach_to == "request":
                self._test = 1

    # test
    middlewareMixin = MiddlewareMixinTest()
    @middlewareMixin.middleware(attach_to="request")
    def middleware_request(request):
        pass
    assert middlewareMixin._test == 0
    middleware_request()
    assert middlewareMixin._test == 1



# Generated at 2022-06-14 07:42:29.862183
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.response import HTTPResponse

    async def foo_middleware(request):
        return HTTPResponse("Hi there!")

    app = Sanic("test_MiddlewareMixin_on_response")
    app.config.KEEP_ALIVE_TIMEOUT = 0
    app.on_response(foo_middleware)

    @app.route("/")
    async def handler(request):
        return HTTPResponse("Hi there!")

    request, response = app.test_client.get("/")
    # assert response.text == "Hi there!"



# Generated at 2022-06-14 07:42:31.126943
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert callable(MiddlewareMixin.on_response)

# Generated at 2022-06-14 07:42:32.701063
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:42:40.495805
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class App(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    
    def some_middleware():
        pass

    app = App()
    app.middleware(some_middleware)
    assert len(app._future_middleware) == 1

# Generated at 2022-06-14 07:42:47.209699
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic
    from sanic import response

    app = Sanic('test_MiddlewareMixin_on_request')

    @app.middleware('request')
    async def print_on_request(request):
        print("I am in request middleware")

    @app.route('/')
    async def index(request):
        return response.text('OK')

    request, response = app.test_client.get('/')
    assert response.status == 200
    assert response.text == 'OK'


# Generated at 2022-06-14 07:42:52.182519
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    """Unit test for method on_request of class MiddlewareMixin"""

    def test_middleware(request):
        return False

    test_class = MiddlewareMixin()
    assert(test_class.on_request(test_middleware) is test_middleware)

# Generated at 2022-06-14 07:43:06.070827
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    app = Sanic(__name__)

    # Test for @app.middleware
    # When call middleware as decorator, we should set the
    # attach_to to "request" and apply to True
    @app.middleware
    def test_middleware(request):
        return "Middleware"

    assert app._future_middleware[-1].middleware == test_middleware
    assert app._future_middleware[-1].attach_to == "request"
    assert app._future_middleware[-1].apply == True

    # Test for @app.middleware('response')
    # When call middleware as decorator and pass 'response' as
    # a parameter, we should set the attach_to to "response" and
    # apply to True

# Generated at 2022-06-14 07:43:09.827705
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class SomeClass(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            return 'apply_middleware'
    some_class = SomeClass()
    assert some_class.on_request()(lambda _: _).__name__ == 'inner'


# Generated at 2022-06-14 07:43:11.117047
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    # Arrange
    pass



# Generated at 2022-06-14 07:43:25.214010
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.websocket import WebSocketProtocol
    from sanic.exceptions import HTTPException
    import pytest
    from functools import partial

    # create an instance of Sanic
    app = Sanic("sanic-server")

    # a simple middleware
    def process_request(request: Request) -> Request:
        request.consumer_cache["key"] = "value"
        return request

    # a simple middleware that returns a response
    def process_request_with_response(request: Request) -> HTTPResponse:
        response = HTTPResponse("Sanic-plugin-middleware-test")
        return response

    # a simple middleware that throws an exception
   

# Generated at 2022-06-14 07:43:37.388169
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    # create a mock object of MiddlewareMixin class
    mock = MagicMock(MiddlewareMixin)
    # call on_request of MiddlewareMixin class with an instance of MiddlewareMixin
    on_request = mock.on_request(mock())
    # assert that on_request is returning a partial object
    assert isinstance(on_request, partial)
    # assert that the argument of partial object which is a partial function must not be None
    assert on_request.keywords['attach_to'] is not None
    # assert that the argument of partial object which is a partial function has to be "request"
    assert on_request.keywords['attach_to'] == 'request'



# Generated at 2022-06-14 07:43:48.841844
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class test_Class(MiddlewareMixin):
        def __init__(self):
            self.init_times = 0
            super(MiddlewareMixin, self).__init__()

        def _apply_middleware(self, middleware: FutureMiddleware):
            self.init_times += 1

    def middleware_func(request):
        return None

    test_obj = test_Class()
    test_obj.middleware(middleware_func)
    assert test_obj.init_times == 0

    test_obj.middleware(middleware_func, apply=False)
    assert test_obj.init_times == 0

    test_obj.middleware(middleware_func)
    assert test_obj.init_times == 1

    test_obj.middleware(middleware_func, apply=False)
    assert test

# Generated at 2022-06-14 07:43:51.096292
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    assert MiddlewareMixin.on_request(MiddlewareMixin) == 'request'


# Generated at 2022-06-14 07:44:00.713176
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    # create decorator
    @MiddlewareMixin.middleware('request')
    def method(request):
        print("response(): request={}".format(request))

    try:
        method('test request')
    except NotImplementedError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 07:44:14.293665
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    from sanic.response import json
    from sanic.views import CompositionView
    from sanic.blueprints import Blueprint
    from sanic.router import RouteExists
    from sanic.exceptions import InvalidUsage
    from sanic.views import HTTPMethodView

    class SimpleView(HTTPMethodView):
        def get(self, request):
            return response.text("Welcome to Sanic!")

        def post(self, request):
            return response.text("POST request - Welcome to Sanic!")

        def put(self, request):
            return response.text("PUT request - Welcome to Sanic!")

        def patch(self, request):
            return response.text("PATCH request - Welcome to Sanic!")


# Generated at 2022-06-14 07:44:19.794802
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    app = Sanic("test_app")

    async def one(request):
        return response

    # returns True if the test passes and False if the test fails
    return True if app.on_response(one) == app.middleware(one, "response") else False



# Generated at 2022-06-14 07:44:32.777796
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import json

    app = Sanic()

    @app.middleware
    async def print_on_request(request):
        print("I am a request middleware")

    @app.on_event("before_server_start")
    async def print_before_server(app, loop):
        print("I print before the server starts")

    @app.middleware("response")
    async def print_on_response(request, response):
        print("I am a response middleware")

    @app.route("/", methods=["GET"])
    async def index(request):
        return json({"message": "hello world"})

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8000)



# Generated at 2022-06-14 07:44:39.478979
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text

    app = Sanic('test_MiddlewareMixin_middleware')

    @app.middleware
    def test(request):
        return text('pass')

    request, response = app.test_client.get('/')

    assert response.status == 200
    assert response.text == 'pass'


# Generated at 2022-06-14 07:44:50.711046
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic

    app = Sanic()

    @app.middleware("request")
    async def _request_resp():
        assert request is not None

    @app.middleware("response")
    async def _request_resp():
        assert request is not None

    @app.middleware("request")
    async def _request_resp():
        assert request is not None
    assert len(app.request_middleware) == 2
    assert len(app.response_middleware) == 1

    assert app.on_request(lambda: None) is not None
    assert len(app.request_middleware) == 3
    assert len(app.response_middleware) == 1

    assert app.on_response(lambda: None) is not None
    assert len(app.request_middleware) == 3

# Generated at 2022-06-14 07:44:53.773627
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    m=MiddlewareMixin()
    m.on_response(middleware=None)


# Generated at 2022-06-14 07:44:55.691728
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    app = MiddlewareMixin()
    assert callable(app.on_response())

# Generated at 2022-06-14 07:45:07.422542
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    from sanic.response import json

    app = Sanic()

    @app.middleware('response')
    async def response_middleware(request, response):
        return json({'status': 'success'})

    app.__middlewares__ = []
    on_response_middleware_result = app.on_response(partial(response_middleware, request=None))
    assert on_response_middleware_result == response_middleware

    # Coverage
    on_response_middleware_result = app.on_response()
    assert on_response_middleware_result(partial(response_middleware, request=None)) == response_middleware


# Generated at 2022-06-14 07:45:11.310266
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class TestClass(MiddlewareMixin):
        assert False
    obj = TestClass()
    on_response = obj.on_response
    on_response(lambda x: x)

# Generated at 2022-06-14 07:45:18.921847
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    app = Sanic('test')
    app.on_response(middleware=lambda request, response: response)

# Generated at 2022-06-14 07:45:26.476131
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    ordinary_object = unittest.mock.MagicMock()
    MiddlewareMixin_object = MiddlewareMixin()
    MiddlewareMixin_object.middleware = unittest.mock.MagicMock()
    ordinary_object.on_response().return_value = MiddlewareMixin_object.middleware

    assert ordinary_object.on_response() == MiddlewareMixin_object.middleware



# Generated at 2022-06-14 07:45:34.451408
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.response import text

    app = Sanic("test_on_response")

    @app.on_response
    def on_response_middleware(request, response):
        response.text = response.text + "_test"

    @app.route("/")
    async def handler(request):
        return text("test")

    _, response = app.test_client.get("/")
    assert response.text == "test_test"


# Generated at 2022-06-14 07:45:36.669266
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert callable(MiddlewareMixin().on_response())



# Generated at 2022-06-14 07:45:40.225883
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    object_MiddlewareMixin = MiddlewareMixin()
    assert type(object_MiddlewareMixin.on_response()) == partial


# Generated at 2022-06-14 07:45:51.874357
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    from sanic.response import json
    from sanic.request import Request
    from sanic.exceptions import ServerError
    from sanic.types import Receive
    from sanic.models.futures import FutureMiddleware

    app = Sanic("test")

    async def handler(request: Request):
        return json({"test": True})

    async def middleware1(request: Request, receive: Receive):
        return json({"test": True})

    async def middleware2(request: Request, receive: Receive):
        return json({"test": True})

    app.add_route(handler, "/middleware")
    app.on_response(middleware1)
    app.on_response(middleware2)

    fake_request, fake_response = app.test_client.get

# Generated at 2022-06-14 07:46:01.915675
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    @app.on_response
    def example_response_middleware(request, response):
        response.body = response.body.upper()

    assert isinstance(app._future_middleware, list)
    assert len(app._future_middleware) == 1
    assert isinstance(app._future_middleware[0], FutureMiddleware)
    assert app._future_middleware[0].middleware == example_response_middleware
    assert app._future_middleware[0].attach_to == "response"
    assert app._future_middleware[0].executed == False


# Generated at 2022-06-14 07:46:03.209801
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:46:14.599554
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Arrange
    class App:
        
        def __init__(self):
            self._future_middleware=[]
            self.middleware=MiddlewareMixin.middleware
            self.on_request=MiddlewareMixin.on_request
            self.on_response=MiddlewareMixin.on_response
            # self._apply_middleware=MiddlewareMixin._apply_middleware

        def _apply_middleware(self, middleware):
            # self._middleware[middleware.attach_to]=middleware.middleware
            pass
    test_app=App()

    @test_app.middleware
    async def test_middleware(request):
        print("This is a test middleware")


# Generated at 2022-06-14 07:46:19.259245
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(self, *args, **kwargs)

    with pytest.raises(NotImplementedError):
        TestMiddlewareMixin()

# Generated at 2022-06-14 07:46:45.694147
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import text, json

    app = Sanic()

    @app.middleware('request')  # type: ignore
    async def request_middleware(request):
        request['msg'] = 'I am a request middleware'

    @app.middleware('response')  # type: ignore
    async def response_middleware(request, response):
        response = text('I am a response middleware')

    @app.route('/')
    async def bp(request):
        return json({"hello": "world"})

    client = app.test_client
    response = client.get('/')
    assert response.status == 200
    assert response.json == {"hello": "world"}

# Generated at 2022-06-14 07:46:59.603429
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class FakeSanic:
        def __init__(self):
            self._future_middleware: List[FutureMiddleware] = []
        def _apply_middleware(self, middleware: FutureMiddleware):
            return None 
    fake_sanic = FakeSanic()
    MiddlewareMixin.__init__(fake_sanic, *(), **())
    assert len(fake_sanic._future_middleware) == 0
    def fake_middleware():
        return None
    fake_sanic.middleware(fake_middleware, "request", True)
    # check future_middleware
    assert len(fake_sanic._future_middleware) == 1
    assert isinstance(fake_sanic._future_middleware[0].middleware, type(fake_middleware))
    assert fake_sanic._future_middle

# Generated at 2022-06-14 07:47:00.672879
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
	assert True

# Generated at 2022-06-14 07:47:12.603634
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import sanic
    from sanic.models.futures import FutureMiddleware
    from sanic.models.futures import MiddlewareMixin as mw

    class App(mw):

        def __init__(self, *args, **kwargs) -> None:
            super(App, self).__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    app = App()
    app.middleware(None)(lambda x,y : 1)
    assert app._future_middleware == [FutureMiddleware(lambda x,y : 1, 'request')]
    app.middleware(None, 'response')(lambda x,y : 2)

# Generated at 2022-06-14 07:47:19.419911
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin_middleware(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            pass
    test_middleware_mixin_middleware = TestMiddlewareMixin_middleware()
    # case 1:
    # function middleware should be executed
    @test_middleware_mixin_middleware.middleware('request')
    def new_function_middleware(request):
        return request

    # case 2:
    # function new_function_middleware_2 and new_function_middleware's return 
    # are both None. 
    @test_middleware_mixin_middleware.middleware('request')
    def new_function_middleware_2(request):
        return

    # case 3:
    # function new_function_middleware_3's return is not

# Generated at 2022-06-14 07:47:31.211319
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware
    from sanic.models.factory import ServiceFactory
    from sanic.exceptions import InvalidUsage
    from sanic.response import HTTPResponse
    from sanic.server import  HttpProtocol
    from sanic.websocket import WebSocketProtocol
    from sanic.server import serve
    from sanic.app import exceptions
    from sanic.exceptions import ServerError


    @exceptions.handler.register
    def default(request, error):
        return HTTPResponse(
            "We could not find your friend: %s" % error.args[0], status=404
        )

    app = Sanic('test')
    assert app._future_middleware == []
    assert app._apply_middle

# Generated at 2022-06-14 07:47:35.475838
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic()
    app.middleware('request', lambda x: x)
    app.middleware(lambda x: x)
    assert callable(app.middleware)
    assert callable(app.on_request)
    assert callable(app.on_response)


# Generated at 2022-06-14 07:47:48.189010
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    class A:
        def __init__(self, *args, **kwargs):
            pass

    assert hasattr(A, 'middleware')

    assert hasattr(A(), 'middleware')

    # Not implemented:
    # @A().middleware()
    # @A().middleware('request')

    class B(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super(MiddlewareMixin, self).__init__(*args, **kwargs)

    # @B().middleware()
    # @B().middleware('request')
    assert hasattr(B().middleware, '__call__')

    class C(Sanic):
        def __init__(self, *args, **kwargs):
            super(Sanic, self).__init

# Generated at 2022-06-14 07:48:01.166166
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    m = MiddlewareMixin()
    from sanic.models.futures import FutureMiddleware

    assert isinstance(m._future_middleware, list)
    assert len(m._future_middleware) == 0

    m.middleware(None)

    assert isinstance(m._future_middleware[0], FutureMiddleware)
    assert m._future_middleware[0]._middleware is None
    assert m._future_middleware[0]._attach_to == "request"

    m.middleware(None, 'response')

    assert isinstance(m._future_middleware[1], FutureMiddleware)
    assert m._future_middleware[1]._middleware is None
    assert m._future_middleware[1]._attach_to == 'response'


# Generated at 2022-06-14 07:48:06.228836
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    tmm = TestMiddlewareMixin()
    tmm.middleware()

# Generated at 2022-06-14 07:48:29.303914
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    #instance = MiddlewareMixin()
    #instance.middleware(middleware_or_request, attach_to)
    assert True

# Generated at 2022-06-14 07:48:39.356433
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.server import HttpProtocol, WebSocketProtocol

    m = MiddlewareMixin()
    assert type(m._future_middleware) == list
    assert m._future_middleware == []
    m._apply_middleware(None)
    m.middleware(None)
    m.middleware(None, 'request')
    m.middleware(None, apply=True)
    m.middleware(None, attach_to="request", apply=True)
    m.on_request(None)
    m.on_request(middleware=None)
    m.on_response(None)
    m.on_response(middleware=None)

# Generated at 2022-06-14 07:48:42.291381
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    @MiddlewareMixin.middleware
    async def my_middle_ware(request):
        print(request)


# Generated at 2022-06-14 07:48:49.214155
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MyClass(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            self._future_middleware.append(middleware)

        def test_apply_middleware(self):
            @self.middleware
            def mw1(request):
                pass

            self.assertEqual(self._future_middleware[-1].middleware, mw1)

        @staticmethod
        def middleware(self, middleware):
            pass

    myObj = MyClass()
    myObj.test_apply_middleware()


# Generated at 2022-06-14 07:48:57.013051
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A(MiddlewareMixin):
        pass
        
    a = A()
    m = lambda x: x+1
    # x will be attach_to and m will be middleware
    a.middleware(m)
    assert len(a._future_middleware) == 1
    assert a._future_middleware[0].middleware == m
    assert a._future_middleware[0].attach_to == 'request'
    m = lambda x: x+1
    attach = 'response'
    # x will be middleware and attach will be attach_to
    a.middleware(m, attach)
    assert len(a._future_middleware) == 2
    assert a._future_middleware[1].middleware == m
    assert a._future_middleware[1].attach_to == attach
    
# Unit test

# Generated at 2022-06-14 07:49:04.730366
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import text

    app = Sanic()
    #
    @app.middleware
    async def f1(request):
        return text("f1")

    @app.on_request
    async def f2(request):
        return text("f2")

    @app.on_response
    async def f3(request, response):
        return text("f3")
    
    #
    assert True==True

# Generated at 2022-06-14 07:49:15.934278
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.futures import FutureMiddleware

    class Dummy:
        pass

    dummy = Dummy()
    dummy.results = []
    dummy.middleware = MiddlewareMixin()

    @dummy.middleware
    def mw1(request):
        dummy.results.append(1)
        return request

    @dummy.middleware
    def mw2(request):
        dummy.results.append(2)
        return request

    @dummy.middleware
    def mw3(request):
        dummy.results.append(3)
        return request

    @dummy.middleware('on-request')
    def mw4(request):
        dummy.results.append(4)
        return request


# Generated at 2022-06-14 07:49:28.772711
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic()

    @app.middleware
    def middleware_function(request):
        pass
    assert len(app._future_middleware) == 1
    assert middleware_function in app._future_middleware[0].middleware
    assert app._future_middleware[0].attach_to == "request"

    @app.middleware('request')
    def middleware_request(request):
        pass
    assert len(app._future_middleware) == 2
    assert middleware_request in app._future_middleware[1].middleware
    assert app._future_middleware[1].attach_to == "request"

    @app.middleware('response')
    def middleware_response(request, response):
        pass

# Generated at 2022-06-14 07:49:32.801147
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # test case 1
    a = MiddlewareMixin
    assert a._MiddlewareMixin__init__() == NoReturn()
    # test case 2
    assert a._MiddlewareMixin__init__() == Exception()
    # test case 3
    assert a._MiddlewareMixin__init__() == Exception()


# Generated at 2022-06-14 07:49:46.123932
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Applicator(BaseApplicator):
        def apply_middleware(self, middleware: list):
            pass
    middleware_mixin = MiddlewareMixin()

    # Type check
    assert isinstance(middleware_mixin.middleware, partial)
    assert isinstance(middleware_mixin.on_request, partial)
    assert isinstance(middleware_mixin.on_response, partial)

    # Function check
    def test_middleware():
        pass
    def test_on_request():
        pass
    def test_on_response():
        pass

    assert 0 == len(middleware_mixin._future_middleware)
    middleware_mixin.middleware(test_middleware, apply=False)
    assert 1 == len(middleware_mixin._future_middleware)
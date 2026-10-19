

# Generated at 2022-06-14 07:40:09.797877
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic()

    @app.middleware
    async def m1(request):
        return request

    @app.middleware
    async def m2(request):
        return request

    @app.middleware('response')
    async def m3(request, response):
        return response

    @app.middleware('response')
    async def m4(request, response):
        return response

    assert app._future_middleware[0].middleware == m1
    assert app._future_middleware[1].middleware == m2
    assert app._future_middleware[2].middleware == m3
    assert app._future_middleware[3].middleware == m4

    assert len(app._future_middleware) == 4



# Generated at 2022-06-14 07:40:21.506005
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic
    app = Sanic()
    @app.on_request
    def process_request(request):
        print("Request process")
        return
    assert hasattr(app, '_future_middleware') == True
    assert app._future_middleware == []
    # The second parameter of function 'middleware' is 'attach_to'
    assert app.middleware(process_request, attach_to = 'request') == process_request
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].middleware == process_request
    assert app._future_middleware[0].attach_to == 'request'

# Generated at 2022-06-14 07:40:22.338178
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    pass

# Generated at 2022-06-14 07:40:25.423638
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Given
    @MiddlewareMixin.middleware(attach_to="request")
    async def middlewareTest(request):
        pass
    # Then
    assert MiddlewareMixin.middleware(attach_to="request")

# Generated at 2022-06-14 07:40:34.847810
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('sanic')

    @app.middleware('response')
    def process_response(request, response):
        pass

    assert app._future_middleware[0].middleware_func == process_response
    assert app._future_middleware[0].attach_to == 'response'
    assert app._future_middleware[0].middleware is None


# Generated at 2022-06-14 07:40:36.760812
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    mixin = MiddlewareMixin()
    mixin.on_response()



# Generated at 2022-06-14 07:40:49.158184
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.testing import SanicTestClient

    app = Sanic("test_MiddlewareMixin_middleware")

    @app.middleware
    async def test_middleware_1(request):
        return HTTPResponse("OK")

    @app.middleware("request")
    def test_middleware_2(request):
        pass

    @app.middleware("response")
    def test_middleware_3(request, response):
        pass
    
    @app.route("/")
    async def handler(request):
        return HTTPResponse("OK")

    request, response = app.test_client.get("/")

    assert response.status == 200
   

# Generated at 2022-06-14 07:40:52.149369
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    m = MiddlewareMixin()
    def mw_on_request(request):
        pass
    
    o = m.on_request()
    assert o.func == m.middleware

# Generated at 2022-06-14 07:40:54.401457
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    obj = MiddlewareMixin()
    obj.on_response()

# Generated at 2022-06-14 07:41:00.508598
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    @MiddlewareMixin.on_request()
    def middleware(request_, *args, **kwargs):
        pass

    assert middleware.__name__ == "middleware"

    @MiddlewareMixin.on_request
    def middleware2(request_, *args, **kwargs):
        pass

    assert middleware2.__name__ == "middleware2"

# Generated at 2022-06-14 07:41:03.874557
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:41:14.531448
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.app import Sanic
    from sanic.response import text

    app = Sanic("MiddlewareMixin")

    @app.on_request
    async def handler(request):
        request.app.request_handler_called_once = True
        request.app.request_handler_called_twice = True

    @app.on_request
    async def handler_second(request):
        request.app.request_handler_called_twice = False

    @app.route("/")
    async def handler_third(request):
        return text("OK")

    _, response = app.test_client.get("/")
    assert response.status == 200
    assert app.request_handler_called_once is True
    assert app.request_handler_called_twice is False

# Generated at 2022-06-14 07:41:20.245182
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    # create a class that has a method on_request
    class MyMiddlewareMixin(MiddlewareMixin):
        def on_request(self, middleware=None):
            if callable(middleware):
                self.middleware(middleware, "request")
            else:
                self.middleware(attach_to="request")

    MyMiddlewareMixin.on_request()


# Generated at 2022-06-14 07:41:26.423309
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    logger.info("Start testing for method on_request of class MiddlewareMixin")
    from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware
    app = Sanic()
    @app.on_request
    def first_function(request):
        assert isinstance(request, FutureMiddleware)
        return True
    assert app.on_request == first_function
    logger.info("Finish testing for method on_request of class MiddlewareMixin")


# Generated at 2022-06-14 07:41:39.630674
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.app import Sanic
    from sanic.exceptions import SanicException
    from sanic.request import Request

    app = Sanic('test_MiddlewareMixin_on_request')

    @app.middleware('request')
    async def testMiddleware(request):
        pass

    @app.on_response
    async def testMiddleware2(request, response):
        pass

    assert app.on_request(testMiddleware) == testMiddleware

    assert app._middleware == [{'middleware': testMiddleware,
                                'attach_to': 'request'}]

    assert app.on_response(testMiddleware2) == testMiddleware2


# Generated at 2022-06-14 07:41:41.411111
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    assert MiddlewareMixin().on_request()("test") == "test"

# Generated at 2022-06-14 07:41:43.929966
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
	# Test for method middleware of class MiddlewareMixin
	pass

# Generated at 2022-06-14 07:41:56.789832
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    from sanic.exceptions import NotFound, ServerError
    from sanic.log import logger, access_logger

    app = Sanic(__name__)
    bp = Blueprint('test_bp')

    @app.middleware
    def custom_middleware():
        pass

    @app.middleware('request')
    def custom_middleware_request():
        pass

    @app.middleware('response')
    def custom_middleware_response():
        pass

    @bp.middleware
    def custom_bp_middleware():
        pass

    @bp.middleware('request')
    def custom_bp_middleware_request():
        pass


# Generated at 2022-06-14 07:42:00.547150
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic import Sanic
    app = Sanic(__name__)

    @app.on_request
    async def on_request(request):
        return request

    # TODO: 
    # assert call on_request returns request

# Generated at 2022-06-14 07:42:04.085809
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class ClassA(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            print(middleware.middleware)



# Generated at 2022-06-14 07:42:11.431234
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app = Sanic(__name__)

    @app.middleware
    async def example_middleware(request):
        pass

# Generated at 2022-06-14 07:42:12.412383
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass


# Generated at 2022-06-14 07:42:26.241527
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class App(MiddlewareMixin):
        def __init__(self):
            super(App, self).__init__()
            self.middleware_type = None
            self.middleware_records = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            self.middleware_type = middleware.attach_to

        def _handle_middleware_request(self, wrapper):
            if wrapper.attach_to == "response":
                self.middleware_records.append(wrapper.middleware_index)

    app = App()

    assert app.middleware_type is None
    assert app.middleware_records == []

    first_middleware_index = app.middleware(lambda req: req)('response')

# Generated at 2022-06-14 07:42:29.119916
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    @MiddlewareMixin.on_request
    def test():
        return "test"
    assert test() == "test"


# Generated at 2022-06-14 07:42:30.205166
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    obj = MiddlewareMixin()
    assert obj.on_response()

# Generated at 2022-06-14 07:42:41.064818
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestObject:
        def __init__(self):
            self.middleware_runned = False

        def __call__(self):
            self.middleware_runned = True

    test_middleware = TestObject()

    middleware_mixin_object = MiddlewareMixin()
    middleware_mixin_object.middleware(test_middleware)

    assert not test_middleware.middleware_runned
    middleware_mixin_object._apply_middleware(
        middleware_mixin_object._future_middleware[0]
    )
    assert test_middleware.middleware_runned


# Generated at 2022-06-14 07:42:48.580601
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.testing import create_test_server

    # Prepare the function for test, which
    # include the function on_response and
    # the method start_server together
    app = Sanic(
        __name__,
        middleware=[MiddlewareMixin]
    )
    @app.on_response()
    async def on_response(request, response):
        response.headers["Server"] = "Sanic"
        return response
    
    # Perform the test
    test_client = create_test_server(app, app.config)
    request, response = test_client.get("/")
    assert response.status == 200
    assert response.headers["Server"] == "Sanic"

# Generated at 2022-06-14 07:42:51.029047
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    test = MiddlewareMixin()
    assert test.on_request is test.middleware



# Generated at 2022-06-14 07:42:54.698067
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class MockMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            pass

    obj = MockMiddlewareMixin()
    obj.on_request("mock")

# Generated at 2022-06-14 07:42:57.141790
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    obj1 = MiddlewareMixin() # noqa
    obj2 = MiddlewareMixin() # noqa



# Generated at 2022-06-14 07:43:20.076939
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.response import json

    # sanic, version 18.12.0
    app = Sanic()
    # app, version 18.12.0

    @app.on_response
    async def a_middle_ware(request, response):
        # request, version 18.12.0
        # response, version 18.12.0
        # print(request, response)
        return response

    @app.route("/")
    async def get_hello(request):
        # request, version 18.12.0
        return json({"hello": "world"})

    request, response = app.test_client.get('/')



# Generated at 2022-06-14 07:43:26.449271
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class MyMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    m_mixin = MyMiddlewareMixin()
    @m_mixin.on_response
    def my_middleware(request):
        pass


# Generated at 2022-06-14 07:43:37.335097
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class FakeClass:
        def __init__(self):
            self._future_middleware = []
            self._apply_middleware = lambda middleware: None

    class FakeMiddleware:
        def __init__(self):
            self.attach_to = 'response'


    mixin = MiddlewareMixin()
    fake_class = FakeClass()
    fake_middleware = FakeMiddleware()
    fake_class.on_response(fake_middleware)
    assert len(fake_class._future_middleware) == 1
    assert fake_class._future_middleware[0].attach_to == 'response'

# Generated at 2022-06-14 07:43:48.054257
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.response import json
    from sanic.testing import HOST, PORT
    from sanic.request import Request
    from sanic.exceptions import SanicException
    from sanic import Sanic
    from sanic.websocket import ConnectionClosed
    import asyncio
    import traceback

    app = Sanic('sanic-middleware')

    @app.middleware
    async def handler1(request):
        request['message'] = 'Middleware1 executed'

    @app.middleware
    async def handler2(request):
        request['message'] = 'Middleware2 executed'

    @app.route('/1')
    async def handler(request):
        return json(request.get('message'))


# Generated at 2022-06-14 07:43:59.091619
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    app = Sanic(__name__)
    
#     @app.on_response
#     def on_response(request, response):
#         print("on_response")
    @app.middleware("response")
    def on_response(request, response):
        print("on_response")

    # @app.on_request
    @app.middleware("request")
    def on_request(request):
        print("on_request")
        
    @app.route("/")
    async def test(request):
        return text("test")

    request, response = app.test_client.get("/")
    
if __name__ == '__main__':
    test_MiddlewareMixin_on_response()

# Generated at 2022-06-14 07:44:08.255216
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.response import json
    from sanic import Sanic

    app = Sanic()

    @app.on_response
    async def before_response(request, response):
        return await json({"test": "async"})

    @app.route("/")
    async def handler(request):
        return json({"test": "async"})

    request, response = app.test_client.get("/")

    assert response.json == {"test": "async"}


# Generated at 2022-06-14 07:44:18.020603
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class A:
        def __init__(self):
            self.__dict__["middleware_or_request"] = "response"
            self.__dict__["attach_to"] = "response"

        def __getattribute__(self, attr):
            if attr == "middleware":
                def middleware(middleware_or_request, attach_to):
                    self.__dict__["middleware_or_request"] = middleware_or_request
                    self.__dict__["attach_to"] = attach_to
                    return middleware_or_request
                return middleware
            else:
                return object.__getattribute__(self, attr)
    a = A()
    a.on_response()(A())
    return a.__dict__["attach_to"] == "response" and a.__dict__

# Generated at 2022-06-14 07:44:26.401664
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestClass(MiddlewareMixin):
        def __init__(self):
            super().__init__()
        def _apply_middleware(self, middleware: FutureMiddleware):
            assert middleware.attach_to == 'request'
            assert hasattr(middleware.middleware, '__call__')
    test_class = TestClass ()
    test_class.middleware(lambda a: a)
    test_class.middleware(3)


# Generated at 2022-06-14 07:44:32.968201
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    app = Sanic("test-on_response")
    @app.on_response
    async def test(request, response):pass

    assert len(app.middleware_request) == 0, \
        "MiddlewareMixin.on_response(middleware) does not work"
    assert len(app.middleware_response) == 1, \
        "MiddlewareMixin.on_response(middleware) does not work"

# Generated at 2022-06-14 07:44:46.417042
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    arg1 = "arg1"

    class Test(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware):
            raise NotImplementedError  # noqa

    test = Test()

    # 1.
    result = test.middleware(arg1, attach_to="request")
    assert isinstance(result, partial)
    assert result.args == (arg1,)
    assert result.keywords == {"attach_to": "request"}
    assert result.func == test.middleware

    # 2.
    result = test.middleware(arg1, attach_to="request", apply=True)
    assert result == arg1

# Generated at 2022-06-14 07:45:05.071781
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    class TestClass(MiddlewareMixin):
        def __init__(self):
            pass

        def on_request(self, request):
            pass

    @TestClass.on_response()
    async def middleware_func(request, response):
        response.body = "test"

    test_class = TestClass()

    assert middleware_func == test_class._future_middleware[0].middleware

# Generated at 2022-06-14 07:45:10.518399
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():

    class App(MiddlewareMixin): # noqa
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    app = App()

    # callable
    @app.on_response
    def middleware(request, response):
        pass

    # not callable
    app.on_response()

# Generated at 2022-06-14 07:45:15.804989
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class A:
        def __init__(self):
            self.middleware = MiddlewareMixin()
            self.handler = lambda *args: ""
    a = A()
    # test for no middleware
    assert a.middleware.on_response() == a.middleware.on_response



# Generated at 2022-06-14 07:45:20.468169
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    t: MiddlewareMixin = MiddlewareMixin("aa","bb")
    def mw():
        return 1
    t.on_response(mw)
    assert t._future_middleware[0]._attach_to == "response"

# Generated at 2022-06-14 07:45:30.058817
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    from sanic.response import text
    app = Sanic('test_MiddlewareMixin_on_response')

    @app.on_response
    def test_on_response(response, request):
        response.text += '\n request_id:{}'.format(request.id)

    @app.route("/")
    def handler(request):
        return text("OK")

    request, response = app.test_client.get("/")
    assert 'request_id' in response.text


# Generated at 2022-06-14 07:45:41.476494
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    """
    Ensure, that the method on_response can be called as
    @app.on_response or @app.on_response().
    """
    class App:
        def __init__(self):
            self.count = 0
            self.on_response_call_count = 0

        def on_response(self, middleware=None):
            self.on_response_call_count += 1
            if callable(middleware):
                self.count += 1
            else:
                self.count -= 1
            return

    app = App()
    @app.on_response
    async def response_handler(request, response):
        pass

    assert app.count == 1
    assert app.on_response_call_count == 1


# Generated at 2022-06-14 07:45:44.782407
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    m = MiddlewareMixin()
    assert m.on_response() == m.middleware('response')
    assert m.on_response(1) == m.middleware(1)

# Generated at 2022-06-14 07:45:57.759754
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    from sanic.app import Sanic
    app = Sanic(__name__)
    msg1 = "MiddlewareMixin_test_msg"
    msg2 = "MiddlewareMixin_test_msg2"
    msg3 = "MiddlewareMixin_test_msg3"

    @app.middleware
    async def test_middleware(request):
        print(f"msg:{msg1}")
        response = await request
        return response

    @app.middleware('response')
    async def test_middleware2(request, response):
        print(f"msg:{msg2}")
        return response

    @app.middleware
    async def test_middleware3(request):
        print(f"msg:{msg3}")
        response = await request
        return response


# Generated at 2022-06-14 07:46:09.452200
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    from sanic_cors import CORS

    app = Sanic(name="test_MiddlewareMixin_on_response")

    @app.route("/")
    async def test():
        return text("Hello, world!")

    # The default attach_to of CORS is 'response'
    # So it should also work without setting it
    # If you still want to set it, you should do it like this:
    # cors = CORS(app, automatic_options=True, attach_to='response')
    cors = CORS(app, automatic_options=True)

    request, response = app.test_client.get("/")

    assert response.status == 200
    assert response.headers.get("access-control-allow-origin") == "*"
    assert response.headers.get

# Generated at 2022-06-14 07:46:19.832565
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Description:
    #   This method decorator is just syntactic sugar for: @app.middleware('response')
    # Arguments:
    #   middleware (callable): Wrapped function for attaching to the different events.
    # Return:
    print("test_MiddlewareMixin_on_response")
    middleware1 = lambda x: x
    middleware2 = lambda x: x
    app = MiddlewareMixin()
    app.middleware(middleware1)
    app.on_request(middleware2)
    assert len(app._future_middleware) == 2

# Generated at 2022-06-14 07:46:36.305418
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    op_m = MiddlewareMixin()
    op_f = op_m.on_response() # op_f is still a function
    op_x = op_f("x")
    print(op_x) # Prints 'x'
test_MiddlewareMixin_on_response()

# Generated at 2022-06-14 07:46:46.535775
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.exceptions import SanicException
    from sanic.models import SanicRequest

    class MyException(SanicException):
        pass

    app = Sanic("test_sanic_exception")

    caught_exception = None

    @app.exception(MyException)
    def handle_my_exception(request, exception):
        nonlocal caught_exception
        assert isinstance(request, SanicRequest)
        assert isinstance(exception, MyException)
        caught_exception = exception

    @app.on_response
    def on_response(request, response):
        raise MyException("this is my exception")

    request, response = app.test_client.get("/")

    assert response.status == 500

# Generated at 2022-06-14 07:46:48.724243
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert issubclass(MiddlewareMixin, object)

#Unit test for method middleware of class MiddlewareMixin

# Generated at 2022-06-14 07:47:01.454553
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic.exceptions import NotFound
    from sanic.handlers import ErrorHandler
    from sanic import response

    @test_MiddlewareMixin_on_response.app.route("/")
    def handler(request):
        return response.text("OK")

    @test_MiddlewareMixin_on_response.app.route("/error")
    def handler_error(request):
        raise ValueError("OK")

    async def handler_not_found(request, exception):
        return json({"message": exception.args[0]}, status=404)

    test_MiddlewareMixin_on_response.app.error_handler = ErrorHandler(
        {NotFound: handler_not_found}
    )


# Generated at 2022-06-14 07:47:10.036785
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    import asynctest

    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(TestMiddlewareMixin, self).__init__(*args, **kwargs)

    test_middleware_mixin = TestMiddlewareMixin()
    test_result = test_middleware_mixin.on_response(asynctest)

    assert test_result == test_middleware_mixin.middleware(
        asynctest, "response"
    )

# Generated at 2022-06-14 07:47:15.869220
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic

    app = Sanic()

    @app.on_response
    def on_response(request, response):
        print("On response")

    @app.on_response
    def on_response2(request, response):
        print("On response2")

    @app.on_response("request")
    def on_response(request, response):
        print("On response")

    @app.on_response("request")
    def on_response2(request, response):
        print("On response2")


# Generated at 2022-06-14 07:47:17.784012
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    assert MiddlewareMixin().on_response(lambda x:x) == None

# Generated at 2022-06-14 07:47:29.998566
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # Create a fake class to test this method
    class FakeClass(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    # Instantiate the fake class
    fake_class_instance = FakeClass()

    # Create a mock method
    fake_middleware = (lambda request, response: True)

    # Call the on_response method with a mock method
    method_result = fake_class_instance.on_response(fake_middleware)

    # Check that the method returns a funtion
    assert(callable(method_result))

    # Check that the returned function is the same as the function passed in
    # the call

# Generated at 2022-06-14 07:47:38.379024
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    class MiddlewareMixin_test:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

    #test_on_response_1():
    MiddlewareMixin_test._apply_middleware = lambda _, __: print("_apply_middleware is called")
    test_MiddlewareMixin = MiddlewareMixin_test()
    test_MiddlewareMixin.on_response()("middleware")

    #test_on_response_2():
    MiddlewareMixin_test._apply_middleware = lambda _, __: print("_apply_middleware is called")
    test_MiddlewareMixin = MiddlewareMixin_test()
    test_MiddlewareMixin.on_response(middleware="middleware")


# Generated at 2022-06-14 07:47:49.813864
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic(__name__)

    def middleware(request):
        return "ok"

    assert app.request_middleware == []
    assert app.response_middleware == []

    app.middleware(middleware, attach_to="request")
    assert len(app._future_middleware) == 1
    assert app.request_middleware == [middleware]
    assert app.response_middleware == []

    app.middleware(middleware, attach_to="response")
    assert len(app._future_middleware) == 2
    assert app.request_middleware == [middleware]
    assert app.response_middleware == [middleware]

# Generated at 2022-06-14 07:48:09.487389
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class CallableMixin:
        def __init__(self):
            self.has_been_called = False

        def __call__(self):
            self.has_been_called = True

    class MiddlewareMixinTest(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            assert self.has_been_called is False
            assert middleware.attach_to == "request"
            middleware.middleware()
            assert self.has_been_called is True

    m = MiddlewareMixinTest()
    m.middleware(CallableMixin())

    m = MiddlewareMixinTest()
    m.middleware(CallableMixin())

# Generated at 2022-06-14 07:48:22.560830
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super(A, self).__init__()
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    def fun():
        pass
    a = A()
    a.middleware(fun)
    assert len(a._future_middleware) == 1
    assert a._future_middleware[0].middleware == fun
    assert a._future_middleware[0].attach_to == "request"
    a.middleware(fun, attach_to="response")
    assert len(a._future_middleware) == 2
    assert a._future_middleware[1].middleware == fun
    assert a._future_middleware[1].attach_

# Generated at 2022-06-14 07:48:27.823684
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Test Data
    middelwareTest = 'Middleware Mixin'


    class Test(MiddlewareMixin):
        def __init__(self):
            self.var = 'sanic'

    t = Test()
    middleware_condition = t.middleware(middleware)
    assert middleware_condition == None

# Generated at 2022-06-14 07:48:39.775139
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    try:
        # Test pass
        mix = MiddlewareMixin()
        mix.middleware(lambda: None, 'request', True)
    except Exception as e:
        print(f'{e}(test_MiddlewareMixin_middleware)')
        assert True == False, 'Test fail'
    
    try:
        # Test fail
        mix = MiddlewareMixin()
        mix.middleware(lambda: True, 'request', True)
    except Exception as e:
        print(f'{e}(test_MiddlewareMixin_middleware)')
        assert True == False, 'Test fail'
        

# Generated at 2022-06-14 07:48:48.865921
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    warnings.simplefilter("always")
    from sanic.views import CompositionView

    # Setup
    m = MiddlewareMixin(db=None)
    m.blueprints = {}
    m.middleware(None, apply=False)

    # Test class
    assert isinstance(MiddlewareMixin, object) is True

    # Test middleware
    m.middleware(None, apply=False)
    assert len(m._future_middleware) is 1

    # Test on_request
    m.on_request(None)(None)
    assert len(m._future_middleware) is 2

    # Test on_response
    m.on_response(None)(None)
    assert len(m._future_middleware) is 3

    CompositionView()

# Generated at 2022-06-14 07:48:56.632943
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class DerivedMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa

    derived_middleware_mixin = DerivedMiddlewareMixin()
    assert len(derived_middleware_mixin._future_middleware) == 0

    # unit test for MiddlewareMixin.middleware()
    @derived_middleware_mixin.middleware
    async def on_request(request):
        pass

    assert len(derived_middleware_mixin._future_middleware) == 1
    assert derived_middleware_mixin._future_middleware[0].attach_to == "request"

# Generated at 2022-06-14 07:49:03.016780
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware
    async def test_middleware(request):
        pass

    assert len(app._future_middleware) == 1
    assert app._future_middleware[0] == FutureMiddleware(test_middleware, "request")


# Generated at 2022-06-14 07:49:04.576308
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # TODO: How to test this?
    assert True

# Generated at 2022-06-14 07:49:10.111875
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    def my_middleware(request):
        return request

    from sanic.app import Sanic

    app = Sanic()
    app.middleware(my_middleware)
    assert app._future_middleware[0].attach_to == "request"
    assert app._future_middleware[0].middleware == my_middleware



# Generated at 2022-06-14 07:49:17.992326
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from types import FunctionType
    from sanic.app import Sanic
    app = Sanic(__name__)

    def middleware_no_param():
        print('middleware_no_param executed')

    def middleware_with_param(request):
        print('middleware_with_param executed')

    @app.middleware()
    def middleware_decorator_no_param():
        print('middleware_decorator_no_param executed')

    @app.middleware('response')
    def middleware_decorator_with_param(request):
        print('middleware_decorator_with_param executed')

    # Test with middleware no param
    app.middleware(middleware_no_param)
    assert isinstance(app._future_middleware[0].middleware_object, FunctionType)

# Generated at 2022-06-14 07:49:42.003791
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_MiddlewareMixin')
    app.middleware(lambda r: r)
    assert app._future_middleware[0].middleware(None) is None

# Generated at 2022-06-14 07:49:51.234807
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Client:
        def __init__(self):
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    @Client.on_request
    def m1(request: Request):
        pass

    @Client.on_response
    def m2(request: Response):
        pass

    client = Client()

    # test return value
    assert isinstance(m1, partial)
    assert isinstance(m2, partial)

    # test pass to object
    assert len(client._future_middleware) == 0
    assert client.middleware(m1, 'request', False) == m1
    assert len(client._future_middleware) == 1
    assert client._future_middleware[0].middleware == m1
    assert client._future_middle

# Generated at 2022-06-14 07:49:58.545071
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic_jwt_extended import initialize

    app = Sanic()
    initialize(app)
    @app.middleware('response')
    async def test1(request, response):
        response.text = "test1"

    @app.middleware('response')
    async def test2(request, response):
        response.text = "test2"

    # create a mock request and response object
    request = dict()
    response = dict()
    response['text'] = None

    # run the middleware
    for future_middleware in app._future_middleware:
        future_middleware.middleware(request, response)

    assert response['text'] == "test2"

# Generated at 2022-06-14 07:50:07.283826
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            assert isinstance(middleware, FutureMiddleware)
            assert callable(middleware.middleware)
            assert middleware.attach_to == "response"

    TestMiddlewareMixin().middleware(lambda request, response, middleware_method: None, attach_to="response")

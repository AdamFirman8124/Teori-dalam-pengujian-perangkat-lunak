

# Generated at 2022-06-14 07:40:07.237875
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []
            self._apply_middleware = self._real_apply_middleware

        def _real_apply_middleware(self, middleware: FutureMiddleware):
            self._future_middleware.append(middleware)

    test = TestMiddlewareMixin()
    test.middleware(lambda req, resp: None)
    assert len(test._future_middleware) == 1

# Generated at 2022-06-14 07:40:16.597938
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from sanic.exceptions import MethodNotSupported

    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super().__init__()

    test_middleware = TestMiddlewareMixin()

    def test_function():
        pass

    # success
    test_middleware.on_request(test_function)

    # test_function is not callable
    with pytest.raises(MethodNotSupported):
        test_middleware.on_request(None)

# Generated at 2022-06-14 07:40:26.825961
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic("middleware_mixin")

    class MiddlewareMixin:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

    def _apply_middleware(self, middleware: FutureMiddleware):
        raise NotImplementedError  # noqa


# Generated at 2022-06-14 07:40:30.216273
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic()

    async def my_middleware(request):
        print('> In my Middleware')

    app.on_request(my_middleware)

# Generated at 2022-06-14 07:40:41.017620
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic.websocket import ConnectionClosed

    app = Sanic("test_MiddlewareMixin_middleware")

    @app.middleware("request")
    async def request_middleware(request):
        request["data"] = "1"

    @app.middleware("response")
    async def response_middleware(request, response):
        response.headers["Custom-Middleware"] = "Works"

    @app.websocket("/middleware")
    async def middleware(request, ws):
        data = request["data"]
        assert data == "1"
        await ws.send("hello")
        with pytest.raises(ConnectionClosed):
            await ws.recv()


# Generated at 2022-06-14 07:40:45.613481
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    def test_func_1():
        pass
    test_obj = MiddlewareMixin()
    try:
        test_obj.on_request(middleware = test_func_1)
    except:
        assert False



# Generated at 2022-06-14 07:40:52.017945
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    app=Sanic(__name__)

    @app.middleware('request')
    def request(request):
        return True

    assert len(app._middleware['request']) == 1
    assert request == app._middleware['request'][0]

# Generated at 2022-06-14 07:41:03.858353
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    # assert callable(MiddlewareMixin().on_response)
    m = MiddlewareMixin()
    assert callable(m.on_response)

    try:
        m.on_response()()
    except TypeError:
        pass

    assert callable(m.on_response(lambda a, b: (a, b))())
    assert m.on_response(lambda a, b: (a, b))(1, 2) == (1, 2)

    assert callable(MiddlewareMixin().on_response(lambda a, b: (a, b))())
    assert MiddlewareMixin().on_response(lambda a, b: (a, b))(1, 2) == (1, 2)

# Generated at 2022-06-14 07:41:14.825181
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    import time
    import random
    from zk_monitor.server.core.asgi.handler import MonitorHandler

    @MiddlewareMixin.on_response()
    async def response_middleware(request, response):
        """
        this middleware just will run after the response is sent
        """
        print(response.status)
        print(request.status)

    @MiddlewareMixin.on_response()
    async def response_middleware_2(request, response):
        """
        this middleware just will run after the response is sent
        """
        print(response.status)
        print(request.status)

    @MiddlewareMixin.on_response()
    async def response_middleware_3(request, response):
        """
        this middleware just will run after the response is sent
        """

# Generated at 2022-06-14 07:41:20.074745
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class TestClass(MiddlewareMixin):
        pass
    test_class = TestClass()
    assert test_class.on_request(middleware=test_MiddlewareMixin_on_request) == test_MiddlewareMixin_on_request
    assert test_class.on_request(middleware=test_MiddlewareMixin_on_request) != None


# Generated at 2022-06-14 07:41:27.825415
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, args, kwargs):
            super().__init__(args, kwargs)
        def _apply_middleware(self, middleware: FutureMiddleware):
            assert middleware.middleware == mw
            assert middleware.attach_to == "request"
    TestMiddlewareMixin(1, 2)
    mw = lambda x: x
    TestMiddlewareMixin(1, 2).on_request(mw)


# Generated at 2022-06-14 07:41:33.060572
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Sanic:
        pass
    class SanicMock(MiddlewareMixin, Sanic):
        pass
    mock = SanicMock()
    mock.middleware(middleware_or_request = "request")



# Generated at 2022-06-14 07:41:35.813530
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    MiddlewareMixin = MiddlewareMixin()
    MiddlewareMixin.on_request(middleware = test_MiddlewareMixin_on_request)

# Generated at 2022-06-14 07:41:43.709663
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super(TestMiddlewareMixin, self).__init__(*args, **kwargs)

        def _apply_middleware(self, middleware):
            raise NotImplementedError  # noqa

    tmm = TestMiddlewareMixin()
    check_point = {'result': False}

    @tmm.on_request
    def on_request(request):
        check_point['result'] = True

    # call tmm.on_request
    on_request('request')

    assert check_point['result'] == True


# Generated at 2022-06-14 07:41:47.236653
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    from unittest.mock import MagicMock
    from sanic.app import Sanic

    def test():
        print('test')

    app = Sanic()
    app.on_response(test)
    assert app._future_middleware[0].handler == test


# Generated at 2022-06-14 07:41:48.706152
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    pass


# Generated at 2022-06-14 07:41:54.300656
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class ClassTest(MiddlewareMixin):
        def foo(*args, **kwargs):
            pass

    class_test = ClassTest()
    class_test.on_request()("foo")
    class_test.foo("foo")
    assert class_test.foo("foo") == "foo"


# Generated at 2022-06-14 07:41:55.578445
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    pass


# Generated at 2022-06-14 07:42:03.437824
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # arrange
    from sanic.app import Sanic

    @Sanic.middleware(attach_to="request")
    def middleware(request):
        pass

    @Sanic.middleware
    def error_handler(request, exception):
        pass

    @Sanic.middleware("response")
    def response_middleware(request, response):
        pass

    # assert
    assert middleware in Sanic()._future_middleware
    assert error_handler in Sanic()._future_middleware
    assert response_middleware in Sanic()._future_middleware



# Generated at 2022-06-14 07:42:11.784856
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    start = time.time()
    app = Sanic('test_MiddlewareMixin_on_request')
    @app.route('/')
    def handler(request):
        return text('OK')
    @app.on_request()
    def handler2(request):
        print('on_request test')
        request['start'] = start
    request, response = app.test_client.get('/')
    end = time.time()
    diff = end - start
    assert type(request['start']) == float
    assert type(diff) == float
    assert diff <= 1.0
    assert response.text == 'OK'


# Generated at 2022-06-14 07:42:20.632188
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    m = MiddlewareMixin()

    @m.on_request()
    async def middleware():
        pass

    assert m._future_middleware[0].middleware == middleware

# Generated at 2022-06-14 07:42:28.831433
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    class TestClass(MiddlewareMixin):

        def __init__(self, *args, **kwargs):
            MiddlewareMixin.__init__(self)
            self.test_run = False
        
        def _apply_middleware(self, middleware):
            self.test_run = True

    tc = TestClass()
    
    @tc.on_request
    def test_middleware(request):
        pass

    assert tc.test_run == True


# Generated at 2022-06-14 07:42:35.506383
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.response import json
    from sanic import Sanic
    app = Sanic(__name__)

    @app.middleware
    def middleware_a(request):
        print("middleware_a_before")
        response = request.app.get_response(request)
        print("middleware_a_after")
        return response

    @app.middleware('request')
    def middleware_b(request):
        print("middleware_b_before")
        response = request.app.get_response(request)
        print("middleware_b_after")
        return response

    @app.middleware('response')
    def middleware_c(request, response):
        print("middleware_c")
        return response

    @app.route('/')
    async def index(request):
        return

# Generated at 2022-06-14 07:42:38.470884
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    a = MiddlewareMixin()
    assert callable(a.on_request)


# Generated at 2022-06-14 07:42:40.194977
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    MiddlewareMixin.on_request()


# Generated at 2022-06-14 07:42:48.321668
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    app = MiddlewareMixin()
    # not callable middleware
    with pytest.raises(TypeError):
        app.on_request(middleware='')
    # not callable middleware
    with pytest.raises(TypeError):
        app.on_request(middleware=None)
    # decorator middleware
    @app.on_request(middleware="request")
    def test_middleware():
        pass
    assert app._future_middleware[0]._attach_to == "request"
    # callable middleware
    @app.on_request()
    def test_callable_middleware():
        pass
    assert app._future_middleware[1]._attach_to == "request"


# Generated at 2022-06-14 07:42:53.704836
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    middleware_mixin = MiddlewareMixin()
    middleware = middleware_mixin.on_request(lambda r: True)
    assert callable(middleware)
    assert middleware_mixin.__class__._future_middleware[0]._attach_to == 'request'


# Generated at 2022-06-14 07:42:59.843499
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
  from sanic.app import Sanic
  from sanic.response import text

  app = Sanic(__name__)

  @app.middleware
  def some_middle_ware(request):
    return text('OK')

  request, response = app.test_client.get('/')
  assert response.status == 200


# Generated at 2022-06-14 07:43:06.253117
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    print("START: test_MiddlewareMixin_on_request")
    mm = MiddlewareMixin()
    assert callable(mm.on_request)
    assert mm.on_request() == partial(mm.middleware, attach_to="request")
    print("STOP: test_MiddlewareMixin_on_request")


# Generated at 2022-06-14 07:43:08.438165
# Unit test for method on_request of class MiddlewareMixin
def test_MiddlewareMixin_on_request():
    app_instance = MiddlewareMixin()
    assert isinstance(app_instance.on_request(middleware=None), partial)


# Generated at 2022-06-14 07:43:25.172932
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []
        def _apply_middleware(self, middleware: FutureMiddleware):
            self._future_middleware.append(middleware)
    
    temp_middleware_mixin = TestMiddlewareMixin()
    def middleware_func(request, response, middleware_type, *args, **kwargs):
        return "middleware_func"

    # middleware(middleware)
    temp_middleware_mixin.middleware(middleware_func)
    assert(len(temp_middleware_mixin._future_middleware) == 1)
    future_middleware = temp_middleware_mixin._future_middle

# Generated at 2022-06-14 07:43:31.883990
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    # Correct way to call this method
    test_middleware_mixin = TestMiddlewareMixin()
    assert isinstance(test_middleware_mixin.middleware(None), partial)

# Generated at 2022-06-14 07:43:43.991569
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    global m
    m = MiddlewareMixin(None)

    def test_function1(request, response):
        pass

    def test_function2(request, response):
        pass

    @m.middleware
    def test_function3(request, response):
        pass

    @m.on_request
    def test_function4(request, response):
        pass

    @m.on_response
    def test_function5(request, response):
        pass

    @m.middleware('request')
    def test_function6(request, response):
        pass

    @m.middleware('response')
    def test_function7(request, response):
        pass

    assert m.middleware(test_function1) is test_function1
    assert m.middleware(test_function2) is test_function2


# Generated at 2022-06-14 07:43:47.232899
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    mixin = MiddlewareMixin()
    mixin.middleware("request")("request")
    mixin.middleware("response")("response")


# Generated at 2022-06-14 07:43:58.931115
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    class MyMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    my_app = Sanic("test_sanic_app")
    MyMiddlewareMixin(my_app)

    @my_app.middleware("request")
    async def my_middleware(request):
        pass

    # register_middleware(middleware_or_request, attach_to="request")
    # middleware_or_request: callable
    # attach_to: "request"
    # attach_to: "response"
    # middleware_or_request: not callable

    assert len(my_app._future_middleware) == 1

# Generated at 2022-06-14 07:44:12.713476
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    """
    Test MiddlewareMixin middleware methode
    """
    class TestMiddlewareMixin(MiddlewareMixin):

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    test_middleware_mixin = TestMiddlewareMixin()

    @test_middleware_mixin.middleware
    def no_arguments_middleware(request):
        pass

    assert len(test_middleware_mixin._future_middleware) == 1
    assert test_middleware_mixin._future_middleware[0].middleware == no_arguments_middleware

    @test_middleware_mixin.middleware('request')
    def request_middleware(request):
        pass

    assert len(test_middleware_mixin._future_middleware) == 2
    assert test_middle

# Generated at 2022-06-14 07:44:18.262727
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    print('\n')
    '''test caset for MiddlewareMixin_middleware method'''
    print(test_MiddlewareMixin_middleware.__doc__)
    mm = MiddlewareMixin()
    mm.middleware(middleware_or_request='request', attach_to="request", apply=True)

# Generated at 2022-06-14 07:44:26.599832
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from unittest import mock

    # create app
    app = Sanic(__name__)

    # create middleware
    middleware = mock.MagicMock()

    # call middleware method
    app.middleware(middleware)

    # check if middleware was registered
    assert len(app._future_middleware) == 1
    assert app._future_middleware[-1].middleware is middleware



# Generated at 2022-06-14 07:44:36.481712
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.models.middleware import MiddlewareMixin
    from sanic.models.futures import FutureMiddleware
    from sanic.exceptions.exceptions import SanicException
    import pytest

    class MiddlewareMixinTest(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    class SanicExceptionTest(MiddlewareMixinTest):
        pass

    function_test_1 = lambda x: x
    function_test_2 = lambda x: x
    function_test_3 = lambda x: x
    function_test_4 = lambda x: x
    function_test_5 = lambda x: x
    function_test_6 = lambda x: x

    # Test 1
    middleware_mixin = MiddlewareMixinTest()

    # Test 1.1

# Generated at 2022-06-14 07:44:49.248832
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class req:
        pass
    class rep:
        pass
    class mixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa
    a = mixin()
    b = a.middleware(req)
    c = a.middleware(rep)
    d = a.middleware(rep, "rep")
    e = a.middleware(rep, "request")
    f = a.middleware(rep, "response")
    assert callable(b)
    assert callable(c)
    assert callable(d)
    assert callable(e)
    assert callable(f)
    assert b is c
    assert c is d
    assert d is not e
    assert e is not f

# Generated at 2022-06-14 07:45:00.363828
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic('test')
    a_list = []
    @app.middleware('request')
    async def test_middleware (request):
        a_list.append(1)
        a_list.append(2)

    print(app._future_middleware[0])
    app._apply_middleware(app._future_middleware[0])

    print(app._request_middleware)

    # assert app._request_middleware[0] == test_middleware
    # assert a_list == [1,2]



# Generated at 2022-06-14 07:45:04.211061
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic()

    async def middleware(request):
        pass

    assert app.middleware(middleware) == middleware



# Generated at 2022-06-14 07:45:16.975671
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.request import Request
    
    app = Sanic(__name__)
    
    def request_middleware(request):
        return "request_middleware"
   
    def response_middleware(request, response):
        return "response_middleware"
    
    f_req_middleware = app.on_request(request_middleware)
    f_res_middleware = app.on_response(response_middleware)
    
    assert f_req_middleware == request_middleware
    assert f_res_middleware == response_middleware
    
    assert type(app._future_middleware) is list
    assert len(app._future_middleware) is 2
    
    assert app._future_middleware[0].attach_to == "request"


# Generated at 2022-06-14 07:45:24.397421
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super(TestMiddlewareMixin,self).__init__()
    testMiddlewareMixin = TestMiddlewareMixin()
    def middleware_test(request):
        return request
    assert testMiddlewareMixin.middleware(middleware_test) == middleware_test


# Generated at 2022-06-14 07:45:35.702328
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    class TestMiddlewareMixin(MiddlewareMixin):
        pass

    tmm = TestMiddlewareMixin()
    assert tmm._future_middleware == []

    # @tmm.middleware, attach_to="request"
    @tmm.middleware
    def a(request, response):
        pass
    assert len(tmm._future_middleware) == 1
    b = tmm._future_middleware[0]
    assert b._middleware == a
    assert b._attach_to == "request"
    assert b._args == ()
    assert b._kwargs == {}

    # @tmm.middleware, attach_to="response"
    @tmm.middleware("response")
    def c(request, response):
        pass
    assert len(tmm._future_middleware) == 2
    d

# Generated at 2022-06-14 07:45:48.856541
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    import asyncio

    wsgi_app = Sanic('test_MiddlewareMixin_middleware')
    server = Sanic('test_MiddlewareMixin_middleware')

    bp = Blueprint('test_bp', url_prefix='test')

    @bp.middleware('response')
    async def handler_middleware(request):
        pass

    wsgi_app.blueprint(bp)
    server.blueprint(bp)

    assert wsgi_app.middleware('request')(lambda x: x)
    assert wsgi_app.on_response(lambda x: x)
    assert wsgi_app.on_request(lambda x: x)
    assert server.middleware('request')(lambda x: x)
   

# Generated at 2022-06-14 07:45:54.498650
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Future:
        def __init__(self, request, response=None):
            self.request = request
            self.response = response
        def set_result(self, response):
            self.response = response
        def done(self):
            return True
    class FutureMixin:
        def __init__(self):
            self.futures = []
        def future_request(self, request):
            self.futures.append(Future(request))
            return self.futures[-1]
    mm = MiddlewareMixin()
    fm = FutureMixin()
    mm._apply_middleware = fm.future_request
    @mm.middleware
    def middleware(request, response):
        response["test"] = "test"
    for future in mm._future_middleware:
        future

# Generated at 2022-06-14 07:46:03.886812
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test')
    assert isinstance(app, MiddlewareMixin)
    app.middleware(middleware_or_request='request')
    app.middleware(middleware_or_request='response')
    assert app._future_middleware[0].attach_to == 'request'
    assert app._future_middleware[1].attach_to == 'response'
    assert callable(app.on_request)
    assert callable(app.on_response)


# Generated at 2022-06-14 07:46:14.934864
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    a = A()
    assert a._future_middleware == []

    @a.middleware
    def mw(request):
        pass

    assert a._future_middleware == [FutureMiddleware(mw, "request")]

    @a.middleware('response')
    def mw2(request, response):
        pass

    assert a._future_middleware == [
        FutureMiddleware(mw, "request"),
        FutureMiddleware(mw2, "response")
    ]

    @a.on_request
    def mw3(request, response):
        pass


# Generated at 2022-06-14 07:46:28.082969
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MockMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._middleware_calls = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            self._middleware_calls.append(middleware)

    @MockMiddlewareMixin.on_request()
    def middleware(request):
        pass

    test_case = MiddlewareMixin()
    test_case.middleware(middleware)

    assert len(test_case._future_middleware) == 0
    assert len(test_case._middleware_calls) == 1



# Generated at 2022-06-14 07:46:45.215296
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    middleware_mixin = MiddlewareMixin()

    assert middleware_mixin._future_middleware == []

    @middleware_mixin.middleware
    async def middleware_func(request):
        return request

    assert len(middleware_mixin._future_middleware) == 1
    assert middleware_mixin._future_middleware[0].attach_to == "request"
    assert middleware_mixin._future_middleware[0].middleware == middleware_func



# Generated at 2022-06-14 07:46:48.488197
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    m = MiddlewareMixin('nvt_event')
    assert m.middleware(m, attach_to="request") == None
    assert m.middleware(m) == None
    assert m.on_request(m) == None
    assert m.on_response(m) == None
    assert isinstance(m._future_middleware, list)

# Generated at 2022-06-14 07:46:59.710121
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Test(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            return middleware
    test = Test()
    @test.middleware('request')
    def middleware(request):
        pass
    assert type(test._future_middleware[0]) == FutureMiddleware
    assert callable(test._future_middleware[0].middleware)

    @test.middleware('request', apply=False)
    def middleware2(request):
        pass
    assert type(test._future_middleware[1]) == FutureMiddleware
    assert callable(test._future_middleware[1].middleware)

# Generated at 2022-06-14 07:47:06.926083
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin:
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []
            
        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError
            
    assert TestMiddlewareMixin()._future_middleware == []
    assert TestMiddlewareMixin().middleware
    assert TestMiddlewareMixin().on_request
    assert TestMiddlewareMixin().on_response
    
test_MiddlewareMixin_middleware()

# Generated at 2022-06-14 07:47:10.416030
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    @middleware('request')
    def f(request):
        return request

    class A(MiddlewareMixin):
        pass

    a = A()
    assert a.middleware('request') is middleware

# Generated at 2022-06-14 07:47:18.485125
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # middleware(self, middleware_or_request, attach_to="request", apply=True)
    # register_middleware(middleware, attach_to="request")
    # m = MiddlewareMixin()
    # assert isinstance(m.middleware(on_request), types.FunctionType)
    # assert isinstance(m.middlewar(on_response), types.FunctionType)
    # assert isinstance(m.middleware(on_request()), types.FunctionType)
    # assert isinstance(m.middlewar(on_response()), types.FunctionType)
    # TODO
    pass



# Generated at 2022-06-14 07:47:30.465910
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models import FutureMiddleware

    def test_middleware(request):
        return request

    test_app = Sanic("test_MiddlewareMixin_middleware")

    # Middleware is successfully registered
    test_app.middleware(test_middleware)
    assert test_app._future_middleware[0].middleware == test_middleware

    # Partial is successfully created for given attach_to
    test_app._future_middleware.clear()
    test_app.middleware(attach_to="request")(test_middleware)
    assert test_app._future_middleware[0].middleware == test_middleware

    # Partial is successfully created by on_request
    test_app._future_middleware.clear()

# Generated at 2022-06-14 07:47:39.475852
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models.futures import FutureMiddleware
    app = Sanic("middleware_mixin")
    class DummyMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            return middleware

    dummy_middleware_mixin = DummyMiddlewareMixin()
    dummy_middleware_mixin.middleware(None)
    assert dummy_middleware_mixin._future_middleware == [FutureMiddleware(None, "request")]
    dummy_middleware_mixin.middleware(None, attach_to="response")
    assert dummy_middleware_mixin._future_middleware == [FutureMiddleware(None, "request"), FutureMiddleware(None, "response")]

# Generated at 2022-06-14 07:47:51.508525
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware

    app = Sanic()

    @app.middleware  # type: ignore
    async def a(request):
        pass

    @app.middleware('request')  # type: ignore
    async def b(request):
        pass

    assert app._future_middleware[0] == FutureMiddleware(a, "request")
    assert app._future_middleware[1] == FutureMiddleware(b, "request")

    @app.middleware('response')  # type: ignore
    async def c(request, response):
        pass

    assert app._future_middleware[2] == FutureMiddleware(c, "response")


# Generated at 2022-06-14 07:47:56.452416
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    mm = MiddlewareMixin()
    def test_md(a):
        print('test_md', a)
    mm.middleware(test_md, 'request')

    print(mm._future_middleware)


# Generated at 2022-06-14 07:48:24.638707
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.router_handler import RouterHandler
    from sanic.request import Request
    from sanic.response import HTTPResponse
    import asyncio

    def testing_middleware1(request, handler):
        return HTTPResponse(status=200, body=b'testing middleware1')

    def testing_middleware2(request, handler):
        return HTTPResponse(status=200, body=b'testing middleware2')

    class TestingMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    testing_middleware_mixin = TestingMiddlewareMixin()
    testing_middleware_mixin.middleware(testing_middleware1)
    testing_middleware_mixin.middle

# Generated at 2022-06-14 07:48:38.691318
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.application import Sanic
    from sanic.response import json
    from sanic_base.sanic_base import SanicBase
    # type
    app = SanicBase(__name__)
    app.config.KEEP_ALIVE_TIMEOUT = 5

    @app.middleware('request')
    async def handle_request(request):
        request['parsed_data'] = 'I am a request'

    @app.middleware('response')
    async def handle_response(request, response):
        response.body = b'I am a response'

    @app.route('/')
    async def handler(request):
        return json({'foo': 'bar'})


# Generated at 2022-06-14 07:48:40.449783
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    m = MiddlewareMixin()
    m.middleware()



# Generated at 2022-06-14 07:48:52.405679
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')
    # 1. test @middleware
    @app.middleware
    def process_response(request):
        pass

    assert process_response in app._future_middleware
    # 2. test @middleware.request
    @app.middleware('request')
    def process_request(request):
        pass

    assert process_request in app._future_middleware
    # 3. test @middleware.response
    @app.middleware('response')
    def process_response(request):
        pass

    assert process_response in app._future_middleware


# Generated at 2022-06-14 07:48:52.826265
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert True

# Generated at 2022-06-14 07:49:04.407575
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    print("\n---start test_MiddlewareMixin_middleware---\n\n")

    def test_middleware(request):
        return

    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            self._future_middleware: List[FutureMiddleware] = []
            # self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError

    testMiddlewareMixin = TestMiddlewareMixin()
    testMiddlewareMixin.middleware(test_middleware)
    print("testMiddlewareMixin.middleware(test_middleware):")
    print(">>for middleware in testMiddlewareMixin._future_middleware:")

# Generated at 2022-06-14 07:49:10.960942
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Sanic(MiddlewareMixin):
        def _apply_middleware(self, middleware):
            pass
    app = Sanic(__name__)
    @app.middleware
    def middleware(request):
        pass
    assert app._future_middleware[0].middleware == middleware
    assert app._future_middleware[0].attach_to == "request"



# Generated at 2022-06-14 07:49:18.190917
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    ''' 
    test the functionality of method middleware of class MiddlewareMixin
    '''
    print('Test for method middleware of class MiddlewareMixin')
    # create a MiddlewareMixin object
    middleware_mixin_obj = MiddlewareMixin()
    # update the _future_middleware instance variable with a partial object
    middleware_mixin_obj._future_middleware = [partial(print, 'hello')]
    assert middleware_mixin_obj._future_middleware == [partial(print, 'hello')]
    # check if it returns a partial object in the case that first argument is not a callable
    assert type(middleware_mixin_obj.middleware('request')) == partial
    # create a callable object

# Generated at 2022-06-14 07:49:31.363247
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    def showMiddleWare():
        print("it's showMiddleWare")

    def showMiddleWare2():
        print("it's showMiddleWare2")

    class middleWare:
        def __init__(self,request):
            pass

    class middleWare2:
        def __init__(self,request):
            pass

    class A(MiddlewareMixin):
        def __init__(self):
            super().__init__()
        def test1(self):
            print('middleware test 1')
            super().middleware(showMiddleWare)
        def test2(self):
            print('middleware test 2')
            super().middleware(middleWare)

        def test3(self):
            print('middleware test 3')
            super().middleware(showMiddleWare2)

    a = A()
    a.test1

# Generated at 2022-06-14 07:49:33.919854
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic()
    print(app.middleware(None, apply=True))
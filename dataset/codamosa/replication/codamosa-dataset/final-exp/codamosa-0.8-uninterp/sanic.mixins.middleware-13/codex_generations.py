

# Generated at 2022-06-14 07:40:17.433159
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    from sanic.response import json as json_res

    app = Sanic(__name__)

    @app.middleware
    async def test_middleware(request):
        assert request.app is not None
        assert request.args is not None
        assert request.json is None
        assert request.files is not None
        assert request.form is not None
        assert request.method is not None
        assert request.ip is not None
        assert request.port is not None
        assert request.scheme is not None
        assert request.host is not None
        assert request.headers is not None
        assert request.body is not None
        assert request.cookies is not None
        assert request.match_info is not None
        assert request.match_dict is not None
        assert request.path is not None


# Generated at 2022-06-14 07:40:25.130914
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic import Sanic
    app = Sanic("test_sanic_app")
    def response_middleware(request, response):
        pass

    # check with assign middleware to app.response_middleware
    app.response_middleware(response_middleware)
    assert app._future_middleware[0].middleware == response_middleware
    assert app._future_middleware[0].attach_to == "response"

    # check with return partial function
    m = app.on_response()
    assert m.__defaults__[0] == 'response'


# Generated at 2022-06-14 07:40:33.532808
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    def test_on_response(request):
        pass
    obj = MiddlewareMixin()
    obj.on_response(test_on_response)
    assert obj._future_middleware[0].middleware == test_on_response
    assert obj._future_middleware[0].attach_to == "response"


# Generated at 2022-06-14 07:40:39.502657
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from unittest.mock import MagicMock

    mm = MiddlewareMixin()
    mm.on_response("response")("middleware")
    mm.middleware.assert_called_once_with("middleware", attach_to="response")

# Generated at 2022-06-14 07:40:43.638663
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    m = MiddlewareMixin()
    assert isinstance(m.on_response, partial)
    assert m.on_response.keywords == {"attach_to": "response"}

# Generated at 2022-06-14 07:40:49.576261
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')

    async def middleware_2(request):
        return 1

    @app.middleware('request')
    async def middleware_1(request):
        return 2
    
    assert middleware_1.__name__ == 'middleware_1'
    assert middleware_2.__name__ == 'middleware_2'



# Generated at 2022-06-14 07:41:02.145684
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.app import Sanic
    from sanic.models import FutureMiddleware
    app = Sanic()
    middleware_mixin = MiddlewareMixin()

    @middleware_mixin.on_response
    def test_middleware(request):
        return request

    assert len(middleware_mixin._future_middleware) == 1
    assert isinstance(middleware_mixin._future_middleware[0], FutureMiddleware)

    @middleware_mixin.on_response('request')
    def test_middleware(request):
        return request

    assert len(middleware_mixin._future_middleware) == 2
    assert isinstance(middleware_mixin._future_middleware[1], FutureMiddleware)



# Generated at 2022-06-14 07:41:04.955526
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    from sanic.models.sanic import Sanic
    app = Sanic()
    @app.on_response
    def handle(request):
        pass

# Generated at 2022-06-14 07:41:06.114877
# Unit test for method on_response of class MiddlewareMixin
def test_MiddlewareMixin_on_response():
    obj = MiddlewareMixin()
    middleware = obj.on_response()
    assert callable(middleware)

# Generated at 2022-06-14 07:41:15.877752
# Unit test for method on_response of class MiddlewareMixin

# Generated at 2022-06-14 07:41:21.512159
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Given
    test_class = MiddlewareMixin()

    # When
    result = test_class.middleware(123)

    # Then
    assert result == NotImplemented


# Generated at 2022-06-14 07:41:28.088182
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    import os

    app = Sanic("test_MiddlewareMixin_middleware")

    # Unit test for method middleware of class MiddlewareMixin
    def test_mw():
        pass

    # Unit test for method middleware of class MiddlewareMixin
    def test_mw_1():
        pass

    app.middleware(test_mw)
    app.middleware(test_mw_1)
    assert test_mw in app.__dict__["_future_middleware"][0].middleware
    assert test_mw_1 in app.__dict__["_future_middleware"][1].middleware


# Generated at 2022-06-14 07:41:29.612013
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():

    pass



# Generated at 2022-06-14 07:41:36.460424
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    print("test_MiddlewareMixin_middleware")
    from sanic.models.middleware_mixin import MiddlewareMixin

    class App(MiddlewareMixin):
        pass

    app = App()

    @app.middleware("request")
    async def middleware_test(request):
        pass

    assert len(app._future_middleware) == 1



# Generated at 2022-06-14 07:41:48.529409
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    '''
    Test method middleware of class MiddlewareMixin
    '''

    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super(TestMiddlewareMixin, self).__init__()

    fixture = TestMiddlewareMixin()

    # Case 1
    m_1 = lambda request: True
    m_2 = lambda request: True

    fixture.middleware(m_1)()(m_2)
    assert fixture._future_middleware[0].future() is m_1
    assert fixture._future_middleware[1].future() is m_2

    # Case 2
    fixture = TestMiddlewareMixin()  # Create new instance
    fixture.middleware(m_1, "request")
    assert fixture._future_middleware[0].attach_to == "request"

# Generated at 2022-06-14 07:41:59.285023
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test_MiddlewareMixin_middleware')
    # need to add routes in order to be able to run the test
    @app.route('/test')
    def handler(request):
        return text('OK')
    @app.middleware
    def add_server_header(request):
        request['server'] = 'sanic'
    @app.middleware('request')
    def add_request_header(request):
        request['request_header'] = 'sanic'

# Generated at 2022-06-14 07:42:09.535195
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic(__name__)

    @app.middleware('request')
    async def test_middleware1(request):
        return True

    @app.middleware('request')
    async def test_middleware2(request):
        return True

    @app.middleware('request')
    def test_middleware3(request):
        return True

    @app.middleware('response')
    async def test_middleware1(request, response):
        return True

    @app.middleware('response')
    async def test_middleware2(request, response):
        return True

    @app.middleware('response')
    def test_middleware3(request, response):
        return True


# Generated at 2022-06-14 07:42:12.022477
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    m = MiddlewareMixin()
    m.middleware(middleware_or_request="request")

# Generated at 2022-06-14 07:42:18.886010
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Given
    class Test(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    test = Test()
    # When
    test.middleware(None)
    # Then
    assert False

# Generated at 2022-06-14 07:42:30.916740
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    class MockMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._apply_middleware_called = 0

        def _apply_middleware(self, middleware):
            self._apply_middleware_called += 1

    sanic = Sanic(__name__)
    sanic.config.MIDDLEWARE = []
    mixin = MockMiddlewareMixin()
    assert len(mixin._future_middleware) == 0

    def ok(request):
        pass

    assert mixin.middleware(ok) == ok
    assert len(mixin._future_middleware) == 1
    assert mixin._apply_middleware_called == 1



# Generated at 2022-06-14 07:42:45.141143
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json
    from sanic.models.futures import FutureMiddleware

    app = Sanic('SanicMiddlewareMixin')

    async def before_request(request):
        request['error_1'] = "ErrorValue1"

    @app.middleware('response')
    async def after_response(request, response):
        response.body = str(response.body)

    @app.get('/')
    async def index(request):
        return json({'result': True})

    # assert 'on_start' in app.config.keys()

    # assert 'on_shutdown' in app.config.keys()

    assert 'error_1' in app.request_middleware
    assert 'after_response' in app.response_middleware

    app._apply_

# Generated at 2022-06-14 07:42:45.920677
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert None


# Generated at 2022-06-14 07:42:57.926878
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import json
    from sanic_minimal.middleware.unit_test_future_middleware import future_middleware

    app = Sanic(__name__)

    # Sanic-Minimal 没有默认的 Middleware
    assert app._future_middleware == []

    @app.route("/")
    def handler(request):
        return json({"foo": "bar"})

    app.middleware(future_middleware)
    assert app._future_middleware[0]._middleware == future_middleware
    assert app._future_middleware[0]._attach_to == "request"



# Generated at 2022-06-14 07:42:58.710827
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert True

# Generated at 2022-06-14 07:43:09.472320
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class A():
        def __init__(self):
            self._future_middleware = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    a = A()

    def middleware():
        pass
    a.middleware(middleware)
    assert a._future_middleware
    assert a._future_middleware[0].middleware == middleware
    assert a._future_middleware[0].attach_to == "request"

    a.middleware(middleware, attach_to="response")
    assert a._future_middleware[1].middleware == middleware
    assert a._future_middleware[1].attach_to == "response"


# Generated at 2022-06-14 07:43:21.432901
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic('test')
    assert 'middleware' in dir(app)
    assert callable(app.middleware)

    # using middleware
    @app.middleware
    async def test_middleware(request):
        return
    assert hasattr(app, '_future_middleware')
    assert len(app._future_middleware) == 1

    # using on_request
    @app.on_request
    async def test_on_request(request):
        return
    assert hasattr(app, '_future_middleware')
    assert len(app._future_middleware) == 2

    # using on_response
    @app.on_response
    async def test_on_response(request, response):
        return

# Generated at 2022-06-14 07:43:35.789852
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.exceptions import ServerError
    from sanic.testing import mock

    class TestMiddlewareMixin(MiddlewareMixin):
        def __init__(self):
            super(TestMiddlewareMixin, self).__init__()

        def _apply_middleware(self, middleware):
            assert middleware == self._future_middleware[-1]

    app = TestMiddlewareMixin()
    middleware_callable = mock.Mock()
    middleware = mock.Mock()

    # test that calling middleware without attach_to calls middleware with
    # "request"
    # and that the middleware is added to the list of future middleware
    app.middleware(middleware_callable)

# Generated at 2022-06-14 07:43:47.318618
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class ObjectForTest(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            print('test')

    object_for_test = ObjectForTest()
    assert len(object_for_test._future_middleware) == 0
    object_for_test.middleware = lambda x: print('test')
    object_for_test.middleware('request')
    assert len(object_for_test._future_middleware) == 1
    object_for_test.middleware('response')
    assert len(object_for_test._future_middleware) == 2
    object_for_test.middleware('request')
    assert len(object_for_test._future_middleware) == 3
    object_for_test.middleware('response')

# Generated at 2022-06-14 07:43:57.210489
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MockMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    mm = MockMiddlewareMixin()
    assert mm._future_middleware == []
    mm.middleware(lambda x: x)
    assert len(mm._future_middleware) == 1
    assert mm._future_middleware[0].attach_to == "request"
    mm.middleware(lambda x: x, attach_to="response")
    assert len(mm._future_middleware) == 2
    assert mm._future_middleware[1].attach_to == "response"

# Generated at 2022-06-14 07:44:10.221770
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    assert hasattr(MiddlewareMixin, "middleware")
    assert callable(MiddlewareMixin.middleware)

    class MiddlewareMixinSubClass(MiddlewareMixin):
        def __init__(self, app: Sanic = None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.app = app

        def _apply_middleware(self, middleware: FutureMiddleware):
            assert isinstance(middleware, FutureMiddleware)
            assert not middleware.has_been_applied
            middleware.has_been_applied = True

    instance = MiddlewareMixinSubClass()

    @instance.middleware(attach_to="request")
    def test_middleware(request):
        request["unittest"] = True

# Generated at 2022-06-14 07:44:21.328243
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    def mw_func():
        pass

    app = Sanic('test_MiddlewareMixin_middleware')
    app.middleware = MiddlewareMixin
    app.middleware(mw_func)
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].attach_to == "request"
    assert app._future_middleware[0].middleware == mw_func

# Generated at 2022-06-14 07:44:27.825982
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    inst = MiddlewareMixin()
    assert isinstance(inst, MiddlewareMixin)
    assert len(inst._future_middleware) == 0
    inst.middleware(1)
    assert len(inst._future_middleware) == 1
    inst.middleware(2)
    assert len(inst._future_middleware) == 2

# Generated at 2022-06-14 07:44:29.755240
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Write code here
    print('Test MiddlewareMixin_middleware()')


# Generated at 2022-06-14 07:44:36.360230
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.models.futures import FutureMiddleware

    def middleware(request):
        print("EXECUTED MIDDLEWARE")

    app = Sanic()
    assert app._future_middleware == []
    app.middleware(middleware)
    middleware: FutureMiddleware = app._future_middleware[0]
    assert middleware.middleware == middleware
    assert middleware.attach_to == "request"

# Generated at 2022-06-14 07:44:49.175837
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_Test(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    app = MiddlewareMixin_Test()
    assert len(app._future_middleware) == 0

    @app.on_request
    def mw_func(request):
        return 0

    assert mw_func() == 0
    assert len(app._future_middleware) == 1

    @app.middleware
    def mw_func2(request):
        return 1

    assert mw_func2() == 1
    assert len(app._future_middleware) == 2

    # Test test middleware with attach_

# Generated at 2022-06-14 07:44:56.946483
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from middleware_core import Middleware
    app = Sanic("test_MiddlewareMixin_middleware")
    app.middleware(Middleware)
    assert hasattr(app, "middleware")
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].attach_to == "request"

# Generated at 2022-06-14 07:45:07.264455
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    assert issubclass(Sanic, MiddlewareMixin)

    # TODO: return the first middleware
    sanic_app = Sanic(__name__)
    middleware_closure = lambda request, w_response: w_response
    middleware_decorator = sanic_app.middleware(middleware_closure)
    assert middleware_decorator is middleware_closure
    assert sanic_app._future_middleware
    assert sanic_app._future_middleware[-1] == FutureMiddleware(
        middleware_closure, 'request')

# Generated at 2022-06-14 07:45:14.123087
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixinTest(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            raise NotImplementedError  # noqa

    middleware_mixin_test = MiddlewareMixinTest()
    middleware_mixin_test.middleware(middleware_or_request=lambda: print("hey"))



# Generated at 2022-06-14 07:45:14.931940
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    MiddlewareMixin()

# Generated at 2022-06-14 07:45:16.664044
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Tests for method middleware of class MiddlewareMixin
    pass


# Generated at 2022-06-14 07:45:34.906493
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Given
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    from unittest.mock import Mock

    middleware_or_request = Mock()
    attach_to = "request"
    apply = True
    test_MiddlewareMixin_inst = TestMiddlewareMixin()
    
    # When
    test_MiddlewareMixin_inst.middleware(middleware_or_request, attach_to, apply)
    
    # Then
    assert len(test_MiddlewareMixin_inst._future_middleware) == 1
    assert test_MiddlewareMixin_inst._future_middleware[0].middleware == middleware_or_request
    assert test_MiddlewareMixin_inst._future_middleware[0].attach

# Generated at 2022-06-14 07:45:41.687306
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Server(MiddlewareMixin):
        def __init__(self):
            self.name = "My Server"
    server = Server()
    assert len(server._future_middleware) == 0
    server.middleware(lambda request, response: response)
    assert len(server._future_middleware) == 1


# Generated at 2022-06-14 07:45:55.091021
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # check whether the method middleware of MiddlewareMixin class can associate proper decorator with a method 
    class myMiddlewareMixin(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []

        def _apply_middleware(self, middleware: FutureMiddleware):
            assert middleware is not None

        def middleware(
            self, middleware_or_request, attach_to="request", apply=True
        ):
            def register_middleware(middleware, attach_to="request"):
                nonlocal apply

                future_middleware = FutureMiddleware(middleware, attach_to)
                self._future_middleware.append(future_middleware)

# Generated at 2022-06-14 07:46:06.834526
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    def m1(request):
        return request
    def m2(request):
        return request

    class Request:
        pass

    @MiddlewareMixin.middleware(attach_to="request")
    def m3(request):
        return request

    mm = MiddlewareMixin()

    mm.middleware(m1, attach_to="request")
    mm.middleware(m2, attach_to="response")
    mm.middleware(m3, attach_to="request")

    r1 = mm.middleware(Request())
    r2 = mm.middleware(Request(), attach_to="request")

    assert r1 == r2


# Test for method on_request of class MiddlewareMixin

# Generated at 2022-06-14 07:46:13.851946
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text
    app = Sanic()

    # 使用装饰器
    @app.middleware
    async def some_middleware(request):
        request['middleware'] = 'ok'

    @app.route('/')
    async def handler(request):
        return text('')

    request, response = app.test_client.get('/')

    assert (b"ok" in response.content)

# Generated at 2022-06-14 07:46:14.648592
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert True

# Generated at 2022-06-14 07:46:15.837926
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:46:17.683585
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    assert callable(MiddlewareMixin.middleware)


# Generated at 2022-06-14 07:46:30.664353
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class MiddlewareMixin_temp(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            MiddlewareMixin.__init__(self, *args, **kwargs)

        def _apply_middleware(self, middleware: FutureMiddleware):
            return None

    # Create an instance of MiddlewareMixin and assert that
    # _future_middleware is an empty list
    m = MiddlewareMixin_temp()
    assert m._future_middleware == []

    # Create a middleware function and call m.middleware(middleware_func)
    # then assert that _future_middleware is a list with one element
    # and that the first element is an instance of class FutureMiddleware.
    def middleware_func():
        return None

# Generated at 2022-06-14 07:46:38.138447
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class TestMiddlewareMixin(MiddlewareMixin):
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    a = TestMiddlewareMixin()
    a.on_request(1)
    a.on_response(1)
    assert len(a._future_middleware) == 2

if __name__ == "__main__":
    test_MiddlewareMixin_middleware()

# Generated at 2022-06-14 07:47:03.433071
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    app = Sanic("sanic-middleware-mixin")

    @app.listener("before_server_start")
    def before_server_start(app, loop):
        # Before Start
        pass

    @app.listener("before_server_stop")
    def before_server_stop(app, loop):
        # Before Stop
        pass

    @app.listener("after_server_start")
    def after_server_start(app, loop):
        # After Start
        pass

    @app.listener("after_server_stop")
    def after_server_stop(app, loop):
        # After Stop
        pass

    @app.middleware("request")
    @asyncio.coroutine
    def error_middleware(request):
        pass


# Generated at 2022-06-14 07:47:06.237122
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    with pytest.raises(NotImplementedError):
        MiddlewareMixin().middleware(lambda x: x)



# Generated at 2022-06-14 07:47:17.651408
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    # Arrange
    from sanic_odoo.app import SanicOdoo
    app = SanicOdoo()

    def request_handler(request): return True

    @app.middleware('request')
    def handler_1(request): return True

    @app.middleware('response')
    def handler_2(request): return True

    @app.middleware
    def handler_3(request): return True

    @app.on_request()
    def handler_4(request): return True

    @app.on_response()
    def handler_5(request): return True

    # Act
    app.request_middleware.append(request_handler)

    middleware_1 = app._future_middleware[0]
    middleware_2 = app._future_middleware[1]

# Generated at 2022-06-14 07:47:22.164508
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    
    m = MiddlewareMixin()

    result1 = m.middleware('request')
    result2 = m.middleware('response')

    assert isinstance(result1, partial)
    assert isinstance(result2, partial)



# Generated at 2022-06-14 07:47:30.048033
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    asd = {}
    @MiddlewareMixin.middleware
    def asdasds(request):
        pass
    @MiddlewareMixin.on_request
    def asdasdas(request):
        pass
    @MiddlewareMixin.on_response
    def asdasdasda(request):
        pass
    assert asdasds(asd) == None
    assert asdasdas(asd) == None
    assert asdasdasda(asd) == None

# Generated at 2022-06-14 07:47:38.949608
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Sanic(MiddlewareMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass
    app = Sanic()
    @app.middleware
    def test_middleware(request):
        pass
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].middleware == test_middleware
    assert app._future_middleware[0].attach_to == 'request'

    @app.middleware('response')
    def test_middleware(request):
        pass
    assert len(app._future_middleware) == 2
    assert app._future_middleware[1].middleware == test_middleware

# Generated at 2022-06-14 07:47:49.942056
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class Server(MiddlewareMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_middleware: List[FutureMiddleware] = []
        def _apply_middleware(self, middleware: FutureMiddleware):
            pass

    app = Server()
    def mid_func():
        pass
    def mid_func2():
        pass

    app.middleware(mid_func)
    app.middleware(mid_func2, attach_to='response')
    app.middleware(mid_func, attach_to='request', apply=False)

    assert len(app._future_middleware) == 3



# Generated at 2022-06-14 07:47:58.238013
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    app = MiddlewareMixin()
    assert app._future_middleware == []
    @app.middleware()
    def mymiddleware_func():
        pass
    @app.middleware("request")
    def mymiddleware_func2():
        pass
    assert app._future_middleware == [FutureMiddleware(mymiddleware_func, None),
                                      FutureMiddleware(mymiddleware_func2, "request")]


# Generated at 2022-06-14 07:48:01.921081
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    app = Sanic()
    @app.middleware
    def test_mw(request):
        pass
    assert app._future_middleware[0].handle is test_mw

# Generated at 2022-06-14 07:48:06.988593
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic

    def test_middleware(request):
        return request

    app = Sanic('test_MiddlewareMixin_middleware')

    app.middleware(test_middleware, attach_to="request")

    assert app._future_middleware[0].middleware == test_middleware
    assert app._future_middleware[0].attach_to == "request"



# Generated at 2022-06-14 07:48:31.736871
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic.exceptions import NotFound

    app = Sanic('middleware_test')

    @app.middleware('request')
    async def request_middleware(request):
        request['middleware_request'] = True
        return

    @app.middleware('response')
    async def response_middleware(request, response):
        response.body = None
        response.content_type = 'application/json'
        response.text = 'response_middleware was here'
        return

    @app.route('/')
    async def handler(request):
        return json({'test': True})

    request, response = app.test_client.get('/')

    assert response.status == 200

# Generated at 2022-06-14 07:48:32.437241
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass

# Generated at 2022-06-14 07:48:36.702571
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    class M:
        pass
    assert M.middleware is MiddlewareMixin.middleware

    class T(MiddlewareMixin):
        pass
    assert T.middleware is MiddlewareMixin.middleware
    
    

# Generated at 2022-06-14 07:48:44.093324
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.sanic import Sanic
    app = Sanic(__name__)
    @app.middleware
    def test_middleware(request):
        print('This is a test')
        return request

    @app.middleware('response')
    def test_middleware2(request, response):
        print('This is a test')
        return response

    assert app.listeners["request"] == [app.middleware]
    assert app.listeners["response"] == [app.middleware]

# Generated at 2022-06-14 07:48:57.228801
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic()

    @app.middleware
    async def test_middleware(request):
        request["test"] = True

    server = app.create_server(
        host="127.0.0.1", port=8800, return_asyncio_server=True
    )
    task = asyncio.ensure_future(server)
    time.sleep(1)

    try:
        r = requests.get("http://127.0.0.1:8800/")
        assert r.status_code == 200
        assert r.json() == {"test": True}
    finally:
        task.cancel()



# Generated at 2022-06-14 07:49:09.983151
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic
    from sanic.models.futures import FutureMiddleware
    from sanic.request import Request
    from sanic.router import RouteResult
    from sanic.response import HTTPResponse

    # Create a mock class, which inherits MiddlewareMixin
    class Test(MiddlewareMixin):
        pass

    # Create object test of class Test
    test = Test()

    # Create a mock class, which inherits Request
    class Request(Request):
        pass

    # Create a mock class, which inherits RouteResult
    class RouteResult(RouteResult):
        pass

    # Create a mock function, which can be called
    def on_request_middleware(request: Request, app: Sanic):
        return request

    # Create a mock function, which can be called

# Generated at 2022-06-14 07:49:17.848241
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    import sys
    import os
    import pytest
    import asyncio
    import contextlib
    import json
    import subprocess
    import time
    import types
    from inspect import signature
    from datetime import timedelta

    from sanic import Sanic
    from sanic.exceptions import NotFound, ServerError, RequestTimeout
    from sanic.response import text, json as json_response
    from sanic.request import Request
    from sanic.server import HttpProtocol
    from sanic.views import HTTPMethodView
    from sanic.websocket import WebSocketProtocol
    from sanic.config import Config

    from sanic.config import LOGGING_CONFIG_DEFAULTS
    from sanic.log import logger
    from sanic.server import serve
    from sanic.exceptions import SanicException

# Generated at 2022-06-14 07:49:25.210578
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.app import Sanic

    app = Sanic('test_MiddlewareMixin_middleware')
    @app.middleware('request')
    async def print_on_request(request):
        print('request')

    @app.middleware('response')
    async def print_on_response(request, response):
        print('response')

    assert len(app._future_middleware) == 2



# Generated at 2022-06-14 07:49:26.463766
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    pass



# Generated at 2022-06-14 07:49:34.653070
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic import Sanic
    from sanic.response import text


    async def mw(request):
        return text("Hello, world!")


    app = Sanic()
    app.middleware(mw)
    assert len(app._future_middleware) == 1
    assert app._future_middleware[0].attach_to == "request"
    app.middleware(attach_to="response")(mw)
    assert len(app._future_middleware) == 2
    assert app._future_middleware[1].attach_to == "response"
    app.middleware_refused_callable(mw)
    assert len(app._future_middleware) == 2


# Generated at 2022-06-14 07:50:07.917764
# Unit test for method middleware of class MiddlewareMixin
def test_MiddlewareMixin_middleware():
    from sanic.server import Sanic
    from sanic.app import Sanic
    from sanic.response import text
    app = Sanic('test_app')
    @app.middleware  # noqa
    async def my_middleware(request):
        print('before request')
        # Do something before request
        response = await handler(request)
        print('after request')
        # Do something after request
        return response
    @app.route('/')
    async def handler(request):
        return text('I have a middleware attached')
    request, response = app.test_client.get('/')
    assert response.status == 200
    assert response.text == 'I have a middleware attached'
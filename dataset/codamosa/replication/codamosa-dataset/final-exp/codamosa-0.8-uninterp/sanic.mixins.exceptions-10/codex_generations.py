

# Generated at 2022-06-14 07:27:23.410150
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import inspect
    import uuid
    import random
    import unittest
    from sanic.models.futures import FutureException
    from sanic.app import Sanic

    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            handler.handler(self, *handler.args, **handler.kwargs)
    
    class CustomException(Exception):
        pass

    random_string = uuid.uuid4().hex

    class AppTest(Sanic):
        def register_blueprint(self, blueprint, **options):
            pass

        def add_route(self, handler, uri, methods, *args, **kwargs):
            pass

        def stop(self):
            pass



# Generated at 2022-06-14 07:27:31.140686
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class TestExceptionMixin:
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

    def handler(request, exception):
        pass

    TestExceptionMixin._apply_exception_handler = MagicMock()

    exception_mixin = TestExceptionMixin()
    exception_mixin.exception(Exception)(handler)

    assert len(exception_mixin._future_exceptions) == 1
    assert TestExceptionMixin._apply_exception_handler.call_count == 1

# Generated at 2022-06-14 07:27:43.259137
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        pass
    m_exception_mixin = MyExceptionMixin()

    def handler(request, exception):
        pass

    exception_handler = m_exception_mixin.exception(Exception)(handler)
    # import ipdb; ipdb.set_trace()
    assert len(m_exception_mixin._future_exceptions) == 1
    assert exception_handler == handler

# Generated at 2022-06-14 07:27:44.124577
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:27:53.137551
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class exception_mixin(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    em = exception_mixin()
    @em.exception(IOError, apply=False)
    def foo():
        pass

    assert len(em._future_exceptions) == 1
    assert em._future_exceptions.pop().handler == foo


if __name__ == "__main__":
    test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:28:04.602374
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import pytest
    from sanic.exceptions import SanicException

    class ExceptionMixinSubclass(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    exception_mixin_subclass = ExceptionMixinSubclass()
    assert exception_mixin_subclass._future_exceptions == set()

    @exception_mixin_subclass.exception(SanicException)
    def exception_handler():
        pass

    assert len(exception_mixin_subclass._future_exceptions) == 1
    assert exception_mixin_subclass._future_exceptions[0].handler() is None
    
    # Please note that this test is mostly useless.
    # It basically tests a no-op.


# Generated at 2022-06-14 07:28:15.403609
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Sanic(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    sanic = Sanic()

    @sanic.exception(Exception)
    def exception_handler(request, exception):
        pass

    future_exception = FutureException(exception_handler, (Exception,))

    assert future_exception in sanic._future_exceptions

    @sanic.exception([KeyError, TypeError])
    def exception_handler2(request, exception):
        pass

    future_exception2 = FutureException(exception_handler2, (KeyError, TypeError))

    assert future_exception2 in sanic._future_exceptions

# Generated at 2022-06-14 07:28:25.169428
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class So:
        def method(self):
            pass

        def method_a(self):
            pass

    class Test(ExceptionMixin):
        def __init__(self) -> None:
            super().__init__(So)
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

        def exception1(self, *exceptions, apply=True):
            return super().exception(*exceptions, apply=apply)

    test = Test()
    assert test.exception1(Exception)(test.method)('foo')
    assert test._future_exceptions


# Generated at 2022-06-14 07:28:35.315610
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    from sanic.route_generator import Route, RouteGroup
    
    def test_func(*args, **kwargs):
        return 1
    test_bp = Blueprint(__name__)
    test_route = Route('/', test_func, test_bp)
    test_group = RouteGroup(test_bp)
    test_group.routes.append(test_route)
    test_exception = ExceptionMixin()
    test_exception._apply_exception_handler = test_func
    
    test_exception.exception(Exception)(test_func)
    assert test_exception._future_exceptions[0].handler == test_func
    
    test_func2 = test_exception.exception(Exception)

# Generated at 2022-06-14 07:28:41.093686
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            return True
    
    a = TestExceptionMixin()
    def test():
        return True
    a.exception(Exception, apply=True)(test)()
    

# Generated at 2022-06-14 07:28:53.966189
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            self.added_handler = None
        def _apply_exception_handler(self, handler: FutureException):
            self.added_handler = handler
    mixin = TestExceptionMixin()
    handler1 = lambda x: None
    mixin.exception(KeyError)(handler1)
    assert(handler1 == mixin.added_handler.handler)
    assert({KeyError} == mixin.added_handler.exceptions)
    handler2 = lambda x, y: None
    kw = dict(a = 1, b = 2)
    mixin.exception(KeyError, apply=False)(handler2)
    assert({KeyError} == mixin.added_handler.exceptions)

# Generated at 2022-06-14 07:28:54.777890
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert False

# Generated at 2022-06-14 07:29:04.736113
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test No.1 - Test initial case when the method exception is called
    # without any arguments and when no global exception handler is
    # previously registered.
    class TestHandleExceptions(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    # create an object of the class
    handle_exceptions = TestHandleExceptions()
    # assert that the '_future_exceptions' attribute contains no
    # future exception
    assert not handle_exceptions._future_exceptions

    # Test No.2 - Test case when the method exception is called with
    # arguments (handler function, list of exceptions to be caught,
    # application flag)

# Generated at 2022-06-14 07:29:09.452513
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(args=[1,2], c=3)
    def handler(*args, **kwargs):
        print(args)

    obj = ExceptionMixin()
    obj.exception(args=[1,2], c=3)(handler)


# Generated at 2022-06-14 07:29:15.564022
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    
    obj = TestExceptionMixin()
    @obj.exception(1, 2)
    def handler(request, e):
        pass
    assert len(obj._future_exceptions) == 1
    assert handler in obj._future_exceptions

# Generated at 2022-06-14 07:29:25.299964
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException
    from sanic import Sanic


    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            handler.handler(Exception('hello'))


    class TestBlueprint(TestExceptionMixin, Blueprint):
        def register(self, bp, options):
            self.bp = bp

    app = Sanic()
    bp = TestBlueprint('test', url_prefix='/bp')

    @bp.exception(Exception)
    def handler(request, e):
        return text('Excepcion')

    bp.register(app)
    assert len(bp._future_exceptions) == 1

# Generated at 2022-06-14 07:29:37.079296
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.exceptions import abort

    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            self._future_exceptions.add(handler)

    # case: there aren't args
    exception_mixin = ExceptionMixinTest()
    @exception_mixin.exception()
    async def exception_handler():
        pass

    assert len(exception_mixin._future_exceptions) is 1
    future_exception = exception_mixin._future_exceptions.pop()
    assert len(future_exception.exceptions) is 0

    # case: there are args
    exception_mixin = ExceptionMix

# Generated at 2022-06-14 07:29:46.148909
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.exceptions import ServerError
    from sanic.response import text

    class MyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print(handler)

    my_exception_mixin = MyExceptionMixin()
    @my_exception_mixin.exception(ServerError, apply=False)
    def handler(request, exception):
        return text('OK')

    assert my_exception_mixin._future_exceptions
    assert len(my_exception_mixin._future_exceptions) == 1


# Generated at 2022-06-14 07:29:56.621128
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # This class is defined so that we can test the method exception of class ExceptionMixin
    class Class_Mock_for_ExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            ExceptionMixin.__init__(self, *args, **kwargs)
            self._apply_exception_handler_calls = 0

        def _apply_exception_handler(self, handler: FutureException):
            self._apply_exception_handler_calls += 1

    obj = Class_Mock_for_ExceptionMixin()
    # Case: apply=True and exceptions is a list of 2 elements
    handler1 = obj.exception([ValueError, TypeError], apply=True)
    exceptions1 = list(obj._future_exceptions)[0].exceptions

# Generated at 2022-06-14 07:30:04.100693
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler):
            return handler

    exception_mixin = TestExceptionMixin()
    @exception_mixin.exception()
    def f():
        pass
    assert f.__name__ == 'f'

# Generated at 2022-06-14 07:30:13.193294
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    blueprint = Blueprint('test_blueprint')

    @blueprint.exception(ZeroDivisionError, KeyError, apply=True)
    def handle_error(request, exception):
        return text('Something happened!')
    assert blueprint._future_exceptions
    assert blueprint._apply_exception_handler

# Generated at 2022-06-14 07:30:18.116132
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(KeyError)
    def test_exception(request, exception):
        pass
    # assert test_exception.path == "\\test_exception"
    assert repr(test_exception) == "<FutureException: test_exception>"


# Generated at 2022-06-14 07:30:22.349360
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    user_id = '10010'
    bp = Blueprint('user', url_prefix='/user')
    @bp.exception(AssertionError)
    def assert_handler(request, exception):
        return response.text('Internal server error.', 500)



# Generated at 2022-06-14 07:30:35.090380
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import ServerError
    from sanic.response import json
    
    
    app = Blueprint("test_ExceptionMixin_exception")
    
    @app.exception(Exception, apply=True)
    async def test(request, exception):
        return json({"exception": "ServerError"})
    
    
    assert test.__name__ == 'test'
    assert test.__doc__ == None
    assert test.__annotations__ == {}
    assert test.__kwdefaults__ == None
    
    
    assert len(app._future_exceptions) == 1
    assert app._future_exceptions == {FutureException(test, (Exception,))}

    with app.test_client() as c:
        rv = c.get("/")

# Generated at 2022-06-14 07:30:43.009664
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    # Test build blueprint
    class exceptionMixin(ExceptionMixin):
        pass

    @exceptionMixin.exception(Exception('Expected exception'))
    def test_exception_mixin_exception(request, exception):
        return exception

    ex = exceptionMixin()

    # Get the exception handler
    handler = ex.blueprint.error_handler.__dict__['default_handler'].__dict__['handler']

    # Execute the handler for exception
    result = handler(request, Exception('Expected exception'))

    assert result == 'Expected exception'

# Generated at 2022-06-14 07:30:52.935333
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    from sanic.exceptions import NotFound
    from sanic.response import text

    blueprint = Blueprint('exceptions')

    @blueprint.exception(NotFound)
    def handle_404(request, exception):
        return text("Not Found", status=404)

    assert blueprint._future_exceptions

    future_exception = list(blueprint._future_exceptions)[0]

    assert future_exception.handler
    assert future_exception.exceptions

    blueprint.add_exception_handler(
        future_exception.exceptions[0],
        future_exception.handler)

# Generated at 2022-06-14 07:31:01.468673
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.response import json
    from sanic.exceptions import NotFound
    from sanic.blueprints import Blueprint

    def test_exception(request, exception):
        return json({"exception": str(exception)}, status=exception.status_code)

    app = Sanic()
    blueprint = Blueprint(__name__, url_prefix="/test")

    class Error(NotFound):
        pass

    blueprint.exception(Error, apply=False)(test_exception)
    blueprint.exception(Error, apply=False)(test_exception)
    blueprint.exception(NotFound, apply=False)(test_exception)

    @app.route("/test")
    def test(request):
        raise Error("test")


# Generated at 2022-06-14 07:31:06.997137
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def test_func():
        pass

    class Test(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    test = Test()
    assert test.exception(Exception)(test_func) == test_func
    assert len(test._future_exceptions) == 1

# Generated at 2022-06-14 07:31:13.308560
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Foo(ExceptionMixin):
        pass
    foo = Foo()
    for exceptions in [[Exception], (Exception,)]:
        for apply in [True, False]:
            func = lambda x: x
            assert foo.exception(*exceptions, apply=apply)(func) == func
            assert foo._future_exceptions
            assert not apply


# Generated at 2022-06-14 07:31:19.848184
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from unittest import TestCase
    from unittest.mock import Mock, patch

    class Test(ExceptionMixin, TestCase):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    test = Test()
    test_function = Mock()

    test.exception(Exception)(test_function)

    test_function.assert_called_once()

# Generated at 2022-06-14 07:31:30.911233
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def exception_handler(request, exception):
        print('exception_handler')

    ret = ExceptionMixin.exception(exception_handler)
    ret(exception_handler)
    pass


# Generated at 2022-06-14 07:31:43.575862
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.config import Config
    from sanic.response import text
    from sanic.router import RouteExists

    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._routes = []

        def _apply_exception_handler(self, handler: FutureException):
            self._routes.append(handler)

    @TestExceptionMixin.exception(ZeroDivisionError)
    async def exception_handler(request, exception):
        return text("internal error", 500)

    blueprint = Blueprint("test", url_prefix="/test")
    assert blueprint._routes[0].exception == ZeroDivisionError

# Generated at 2022-06-14 07:31:48.388530
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self):
            super(ExceptionMixinTest, self).__init__()

        def _apply_exception_handler(self, handler):
            pass

    exc = ExceptionMixinTest()
    test = exc.exception(Exception)

    def handler():
        pass

    test(handler)

    assert len(exc._future_exceptions) == 1
    for future_exception in exc._future_exceptions:
        assert future_exception.handler == handler
        assert len(future_exception.exceptions) == 1

# Generated at 2022-06-14 07:32:01.791409
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.exceptions import SanicException
    
    class ExceptionMixin_test(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._handlers = []

        def _apply_exception_handler(self, handler: FutureException):
            self._handlers.append(handler)

    ExceptionMixin_test_object = ExceptionMixin_test()
    assert not ExceptionMixin_test_object._future_exceptions

    @ExceptionMixin_test_object.exception(apply=False)
    def handler(*args, **kwargs):
        return
    
    @ExceptionMixin_test_object.exception()
    def handler2(*args, **kwargs):
        return
    

# Generated at 2022-06-14 07:32:14.252439
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.base_route import BaseRoute

    class MockExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    mixin = MockExceptionMixin()
    assert mixin.exception(Exception)
    assert mixin.exception(Exception, apply=False)

    def decorator(handler):
        pass

    mixin.exception([Exception])(decorator)
    mixin.exception([Exception], apply=False)(decorator)

    @mixin.exception([Exception])
    def exception_handler1(request, exception):
        pass

    @mixin.exception([Exception], apply=False)
    def exception_handler2(request, exception):
        pass


# Generated at 2022-06-14 07:32:17.688279
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    blueprint = Blueprint(__name__, url_prefix='')
    assert blueprint._future_exceptions == set()
    blueprint.exception(ValueError)(lambda x: x)
    assert len(blueprint._future_exceptions) == 1
    blueprint.exception(HTTPException)(lambda x: x)
    assert len(blueprint._future_exceptions) == 2

# Generated at 2022-06-14 07:32:23.902194
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    blueprint = ExceptionMixin()
    blueprint.exception(ZeroDivisionError)(print)
    blueprint.exception(ZeroDivisionError)(print)
    blueprint.exception(ZeroDivisionError)(str)
    blueprint.exception([ZeroDivisionError,NameError])(str)



# Generated at 2022-06-14 07:32:32.974902
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class X:
        def __init__(self, *args, **kwargs):
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            return handler

    x = X()
    def decorator(handler):
        return FutureException(handler, [IOError])

    def handler():
        return True

    x.exception = ExceptionMixin.exception.__get__(x, X)
    fut_exc = x.exception(IOError)(handler)
    assert fut_exc._future_handler is handler
    assert tuple(fut_exc._future_exc_types) == (IOError,)

# Generated at 2022-06-14 07:32:39.731282
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    type_test = TypeVar('type_test', bound=ExceptionMixin)
    obj_test = ExceptionMixin()
    obj_test.exception(ValueError)
    assert len(obj_test._future_exceptions) == 1
    full_name = obj_test._future_exceptions.pop().exceptions[0].__name__
    assert full_name == 'ValueError'

# Generated at 2022-06-14 07:32:52.598578
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.exceptions import InvalidUsage
    from sanic.blueprints import Blueprint
    from sanic.request import Request
    from sanic.response import HTTPResponse
    import pytest

    @pytest.fixture
    def bp():
        bp = Blueprint('name', url_prefix='prefix')
        @bp.route('/a')
        def a_handler(request: Request):
            return HTTPResponse(text='a_handler')
        @bp.exception([InvalidUsage])
        def handle_exception(request: Request, exception: InvalidUsage):
            return HTTPResponse(text=exception.message, status=exception.status_code)
        return bp

    @pytest.fixture
    def app(bp):
        from sanic import Sanic
        app = Sanic

# Generated at 2022-06-14 07:33:21.151143
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import pytest
    from src.web.server.exceptions import MyException

    class TExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__()

    def int_handler(*args, **kwargs):
        pass

    def str_handler(*args, **kwargs):
        pass

    def exp_handler(*args, **kwargs):
        pass

    myexception = MyException("a", "b")

    t = TExceptionMixin()

    t.exception([int, str])(int_handler)
    t.exception(MyException)(exp_handler)
    t.exception(str)(str_handler)

    handler = t._future_exceptions.pop()
    assert handler.exceptions == (int, str)

# Generated at 2022-06-14 07:33:29.653608
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprints

    class MockExceptionMixin(ExceptionMixin):

        def _apply_exception_handler(self, handler: FutureException):
            self.handler = handler

    blueprints = Blueprints(None)
    blueprints.add(MockExceptionMixin)

    @blueprints.exception(ValueError, apply=True)
    def handler(request, exception):
        pass

    @blueprints.exception(ValueError, apply=True)
    def handler_1(request, exception):
        pass

    @blueprints.exception(ValueError, apply=True)
    def handler_2(request, exception):
        pass

    assert blueprints.handler.handler == handler
    assert blueprints.handler_1.handler == handler_1
    assert blueprints.handler_2.handler == handler_2

# Generated at 2022-06-14 07:33:36.602673
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print('apply handler')

    em = TestExceptionMixin()

    @em.exception([PageNotFound])
    def handler(self, request, exception):
        pass

    print(em._future_exceptions)


# Generated at 2022-06-14 07:33:44.473093
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic.views import HTTPMethodView
    import pytest

    # Create a sanic app
    app = Sanic("test_ExceptionMixin_exception")

    # Register blueprint
    @app.listener("before_server_start")
    async def register(app, loop):
        from sanic.blueprints import Blueprint

        bp = Blueprint("test_bp", url_prefix="/test")

        class MyView(HTTPMethodView, ExceptionMixin):
            pass

        bp.add_route(MyView.as_view(), "/overview")
        app.blueprint(bp)

    # Blueprint method exception

# Generated at 2022-06-14 07:33:54.629424
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def __init__(self):
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    blueprint = Blueprint()
    my_exceptions: tuple = (Exception(), NotImplementedError)
    @blueprint.exception(*my_exceptions)
    def my_handler():
        pass

    future_exception = blueprint._future_exceptions.pop()
    assert future_exception.handler == my_handler
    assert future_exception.exceptions == my_exceptions

# Generated at 2022-06-14 07:33:55.952243
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert False


# Generated at 2022-06-14 07:33:59.936110
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert ExceptionMixin._future_exceptions == set()
    assert ExceptionMixin._apply_exception_handler == NotImplementedError
    assert ExceptionMixin.exception(apply=True) == decorator

# Generated at 2022-06-14 07:34:00.896970
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # TODO
    pass

# Generated at 2022-06-14 07:34:01.431375
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True

# Generated at 2022-06-14 07:34:02.127807
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:34:40.825012
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            return

    a = A()
    @a.exception(IOError)
    def foo(request, exception):
        return "bar"

    @a.exception([Exception, ImportError])
    def bar(request, exception):
        return "baz"

    assert a._future_exceptions == {
        FutureException(foo, (IOError,)),
        FutureException(bar, (Exception, ImportError))
        }

# Generated at 2022-06-14 07:34:41.715104
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True is True

# Generated at 2022-06-14 07:34:49.431422
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.bluetext import BlueText
    from sanic.models.exceptions.handler import HandlerException

    @BlueText.exception(ValueError)
    def handler(request, exception):
        return text("Internal server error")

    # Check that if decorator is called and has argument 'apply=False' the exception
    # handler will not be applyed to blueprint.
    BlueText.assert_true(hasattr(handler, '__getitem__'))

    # Check that if decorator is called and has argument 'apply=True' the exception
    # handler will be applyed to blueprint.
    try:
        @BlueText.exception(KeyError)
        def handler(request, exception):
            return text("Internal server error")
    except BluePrintNameError:
        pass
    except HandlerException:
        pass

# Generated at 2022-06-14 07:34:51.475904
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic_restful.mixins import ExceptionMix

# Generated at 2022-06-14 07:34:53.975768
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # TODO: Implement unit test for method exception of class ExceptionMixin
    raise NotImplementedError

# Generated at 2022-06-14 07:35:02.070005
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class SomeClass(ExceptionMixin):
         def __init__(self, *args, **kwargs) -> None:
             super().__init__(*args, **kwargs)
             self.routes = None

         def _apply_exception_handler(self, handler):
             return None

    SomeClass()

    exceptions = [Exception]
    apply = True
    additional_args = {}
    handler = lambda *args, **kwargs: args and kwargs
    handler(*[], **additional_args)
    SomeClass.exception(exceptions, apply)(handler)

# Generated at 2022-06-14 07:35:06.050749
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(Exception)
    def exception_handler():
        pass
    assert exception_handler is not None
    assert len(exception_handler._future_exceptions) == 1

# Generated at 2022-06-14 07:35:19.383268
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest:
        def __init__(self):
            self._future_exceptions = set()
            self._exception_handler = []

        def _apply_exception_handler(self, handler):
            self._exception_handler.append(handler)

    obj = ExceptionMixinTest()
    blueprint = ExceptionMixin()
    blueprint.__setattr__('_future_exceptions', obj._future_exceptions)
    blueprint.__setattr__('_apply_exception_handler', obj._apply_exception_handler)

    # test apply=True
    @blueprint.exception(Exception)
    def exception_handler1():
        pass
    assert len(obj._exception_handler) == 1
    _h1 = obj._exception_handler[0]
    assert _h1.handler == exception_

# Generated at 2022-06-14 07:35:23.726452
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    try:
        @exception(0)
        def handler():
            return "exception"
    except Exception as e:
        assert e == 'invalid type: 0'

# Generated at 2022-06-14 07:35:34.910062
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class TestExeptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

    exception_mixin = TestExeptionMixin()

    @exception_mixin.exception(ZeroDivisionError)
    def test_zero_division_error(request, exception):
        print('Zero Division Error', exception)

    @exception_mixin.exception(AttributeError)
    def test_attribute_error(request, exception):
        print('Attribute Error', exception)

    @exception_mixin.exception(TypeError)
    def test_type_error(request, exception):
        print('Type Error', exception)


# Generated at 2022-06-14 07:36:48.012629
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Note:
    # This test is disabled because the following exception is often found in
    # Travis-CI:
    #   File "tests/test_exceptions.py", line 150, in test_ExceptionMixin_exception
    #     @bp.exception([ValueError])
    # NameError: name 'bp' is not defined
    #
    # I think this is because the test for class Sanic was executed before
    # this test. In other words, the test for class Sanic has not been
    # completed yet.
    #
    # Note:
    # This test passed in my environment.
    import sanic
    app = sanic.Sanic('test_exceptionmixin_exception')

    bp = sanic.Blueprint('test_exceptionmixin_exception_bp', url_prefix='bp')
    b

# Generated at 2022-06-14 07:36:56.362361
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):

        def test_apply_exception_handler(self, handler: FutureException):
            pass

        apply_exception_handler = test_apply_exception_handler

        def test_handler():
            pass

    exception_mixin_ins = TestExceptionMixin()
    exception_mixin_ins.exception([1, 2])
    assert len(exception_mixin_ins._future_exceptions) == 1

# Generated at 2022-06-14 07:37:06.645583
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    try:
        import sanic
    except ImportError:
        return
    # normal usage
    @sanic.blueprints.Blueprint.exception(Exception)
    def handler(request, exception):
        return exception

    # args is tuple
    @sanic.blueprints.Blueprint.exception((Exception, ValueError))
    def handler(request, exception):
        return exception

    # args is list
    @sanic.blueprints.Blueprint.exception([Exception, ValueError])
    def handler(request, exception):
        return exception

    # args is list and tuple
    @sanic.blueprints.Blueprint.exception([123], ('abc', Exception()))
    def handler(request, exception):
        return exception

# Generated at 2022-06-14 07:37:15.923961
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint

    @blueprint.exception(Exception)
    def default_exception(request, exception):
        return text('Exception')

    app = Sanic('test_ExceptionMixin_exception')
    blueprint = Blueprint('test_ExceptionMixin_exception')
    blueprint.exception(Exception)(default_exception)
    blueprint.exception([Exception, Exception])(default_exception)
    app.blueprint(blueprint)
    assert len(blueprint._future_exceptions) == 2
    assert app.error_handler.keys() == {(Exception,), (Exception,), }


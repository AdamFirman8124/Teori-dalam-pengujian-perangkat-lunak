

# Generated at 2022-06-14 07:27:27.580075
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.response import json
    from sanic.exceptions import InvalidUsage

    blueprint = Blueprint('test_ExceptionMixin_exception')

    @blueprint.exception(InvalidUsage)
    def Exception_handler(request, exception):
        return json({'Error': "That's an invalid usage."})

    @blueprint.exception(InvalidUsage, apply=False)
    def Exception_handler2(request, exception):
        return json({'Error': "That's an invalid usage."})

    @blueprint.exception([ValueError, ZeroDivisionError])
    def Exception_handler3(request, exception):
        return json({'Error': "That's an invalid usage."})


# Generated at 2022-06-14 07:27:30.811959
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    bp = Blueprint("test_bp")
    @bp.exception()
    def exception_handler():
        pass
    assert len(bp._future_exceptions) == 1


# Generated at 2022-06-14 07:27:40.816383
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test when apply is True by default
    @ExceptionMixin.exception(IndexError)
    def index_error_handler1(request, exception):
        pass
    # Test when apply is True
    @ExceptionMixin.exception(IndexError, apply=True)
    def index_error_handler2(request, exception):
        pass
    # Test when apply is False
    @ExceptionMixin.exception(IndexError, apply=False)
    def index_error_handler3(request, exception):
        pass

# Generated at 2022-06-14 07:27:48.244520
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic_blueprint import Blueprint
    from sanic import Sanic
    app = Sanic("sanic-blueprint-exception-test")
    bp = Blueprint("exception", url_prefix="/exception")

    @bp.exception(Exception)
    def exception_handler(request, exception):
        return text("Exception has been handled")

    app.blueprint(bp)
    client = app.test_client
    response = client.get("/exception/test/Exception")
    assert response.status == 200
    assert response.text == "Exception has been handled"

# Generated at 2022-06-14 07:27:59.796578
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.exceptions import SanicExceptionHandler
    from sanic.models.futures import FutureException
    from unittest.mock import Mock
    from sanic.views.exceptions import ExceptionHandlerMixin
    from sanic.models.endpoints import EndpointModel

    class SanicExceptionHandler(ExceptionHandlerMixin):
        def __init__(self, *args, **kwargs):
            self.app = Mock()
            self.app.error_handler = Mock()

    handler = SanicExceptionHandler()
    handler_mock = Mock()
    handler.exception(ValueError)(handler_mock)

    assert len(handler._future_exceptions) == 1
    assert isinstance(handler._future_exceptions.pop(), FutureException)

    endpoint_mock = Mock()
    endpoint_mock.name

# Generated at 2022-06-14 07:28:07.645417
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTester(ExceptionMixin):
        def __init__(self):
            super().__init__()
            
        def _apply_exception_handler(self, handler: FutureException):
            pass

    ExceptionMixinTester = ExceptionMixinTester()
    @ExceptionMixinTester.exception(Exception)
    def handler_func(*args):
        pass

    assert len(ExceptionMixinTester._future_exceptions) == 1
    assert Exception in ExceptionMixinTester._future_exceptions.pop().exceptions

# Generated at 2022-06-14 07:28:18.421298
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from unittest import mock
    from sanic.blueprints import Blueprint

    blueprint = Blueprint("test_bp")
    assert blueprint is not None

    with mock.patch.object(blueprint, '_apply_exception_handler') as mock_method:
        @blueprint.exception(ZeroDivisionError)
        def error_handler(request, exception):
            pass
        assert mock_method.called
        assert mock_method.call_count == 1
        mock_method.assert_called_with(mock.ANY)

    with mock.patch.object(blueprint, '_apply_exception_handler') as mock_method:
        @blueprint.exception([ZeroDivisionError])
        def error_handler(request, exception):
            pass
        assert mock_method.called
        assert mock_method.call_count == 1

# Generated at 2022-06-14 07:28:31.729082
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    from sanic.handlers import ErrorHandler
    from sanic.response import text
    from sanic.testing import SOCKET_TIMEOUT

    app = Sanic()
    bp = Blueprint('test_ExceptionMixin_exception', url_prefix='test')

    @bp.listener('before_server_start')
    async def setup(app, loop):
        pass

    @bp.exception(SOCKET_TIMEOUT)
    async def timeout_handler(request, exception):
        return text('Request timed out', 408)


    @bp.route('test')
    async def test(request):
        raise SOCKET_TIMEOUT()

    app.blueprint(bp)


# Generated at 2022-06-14 07:28:36.230202
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    @sanic.response.json
    @blueprint.exception(AttributeError)
    async def handler_exception(request, exception):
        return {"exception": "AttributeError"}

    assert isinstance(handler_exception, types.FunctionType)



# Generated at 2022-06-14 07:28:50.212816
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from sanic.blueprints import Blueprint
    from sanic.constants import HTTP_METHODS

    blueprint = Blueprint(None, strict_slashes=True)
    # test function
    async def my_handler(request, *args, **kwargs):
        pass

    assert len(blueprint._future_exceptions) == 0

    @blueprint.exception(Exception)
    async def my_handler2(request, exception):
        pass
    assert len(blueprint._future_exceptions) == 1

    @blueprint.exception([Exception, IndexError])
    async def my_handler3(request, exception):
        pass
    assert len(blueprint._future_exceptions) == 2


# Generated at 2022-06-14 07:28:55.222134
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    bp = Blueprint()
    @bp.exception(Exception)
    def exception_handler(request, exception):
        pass



# Generated at 2022-06-14 07:29:01.261791
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Bp(ExceptionMixin):
        pass
    bp = Bp()

    @bp.exception()
    def handler():
        pass
    assert len(bp._future_exceptions) == 1

    @bp.exception([Exception])
    def handler():
        pass
    assert len(bp._future_exceptions) == 2


# Generated at 2022-06-14 07:29:14.885725
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # setup
    class DummyExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__()
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    dummy_exception_mixin = DummyExceptionMixin()
    # check
    handler_deco = dummy_exception_mixin.exception(
        exceptions=Exception, apply=True
    )

    @handler_deco
    def handler_for_exception(req, exc):
        return "handler_for_exception"

    result = handler_for_exception(
        req="req", exc="exc"
    )

# Generated at 2022-06-14 07:29:19.902463
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._exception_handler = None

        def _apply_exception_handler(self, handler: FutureException):
            self._exception_handler = handler

    a = A()
    @a.exception(Exception)
    def handler():
        pass
    assert a._future_exceptions
    assert a._exception_handler

# Generated at 2022-06-14 07:29:28.113801
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from unittest import mock
    from sanic.blueprint import Blueprint

    blueprint = Blueprint('test_blueprint', url_prefix='/test_blueprint')
    blueprint._apply_exception_handler = mock.MagicMock()
    blueprint.exception(Exception)(mock.MagicMock())
    assert len(blueprint._future_exceptions) == 1
    blueprint._apply_exception_handler.assert_called_once()

# Generated at 2022-06-14 07:29:33.591917
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Given
    class ExceptionMixin_(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass

    blueprint = ExceptionMixin_()

    @blueprint.exception(test_ExceptionMixin_exception)
    def exception_handler(request, exception):
        pass

    # Then
    assert len(blueprint._future_exceptions) == 1
    future_exception = blueprint._future_exceptions.pop()
    assert future_exception.handler is exception_handler
    assert test_ExceptionMixin_exception in future_exception.exceptions

# Generated at 2022-06-14 07:29:40.229044
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class DemoExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    class DemoBlueprint(DemoExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(args, kwargs)

    demo_blueprint = DemoBlueprint()
    demo_blueprint.exception(ValueError, apply=True)(lambda request: None)
    demo_blueprint.exception([ValueError, TypeError], apply=True)(lambda request: None)

# Generated at 2022-06-14 07:29:47.742625
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.response import text

    class MyBlueprint(ExceptionMixin):
        pass

    my_bp = MyBlueprint()

    @my_bp.exception(RuntimeError)
    def exception_handler(request, exception):
        return text(str(exception), status=500)

    assert len(my_bp._future_exceptions) == 1
    assert my_bp._future_exceptions[0].handler == exception_handler
    assert my_bp._future_exceptions[0].exceptions[0] == RuntimeError



# Generated at 2022-06-14 07:29:54.200515
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.server import Sanic
    class A(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)
            self.server = Sanic('test')
            self.blueprints = []

    def handle(request, exception):
        return "Exception"

    ex = A()
    assert ex.exception(Exception)(handle) == handle



# Generated at 2022-06-14 07:30:02.258027
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    blueprint = Blueprint('', '')

    @blueprint.exception(ValueError)
    def value_error_handler(request, exception):
        return text('Internal server error', 500)

    @blueprint.exception([ValueError, TypeError])
    def value_error_handler(request, exception):
        return text('Internal server error', 500)

    @blueprint.exception(ValueError, apply=False)
    def value_error_handler(request, exception):
        return text('Internal server error', 500)



# Generated at 2022-06-14 07:30:11.518771
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exception_mixin = ExceptionMixin()
    @exception_mixin.exception(Exception, apply=False)
    def some_exception_handler():
        return 1
    assert len(exception_mixin._future_exceptions) == 1

# Generated at 2022-06-14 07:30:19.197867
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from sanic.models.exceptions import ServerError
    from sanic.blueprints import Blueprint

    def test_function():
        pass

    blueprint = Blueprint("test_blueprint", url_prefix="test")
    blueprint.exception(test_function)

    assert isinstance(blueprint._future_exceptions.pop(), FutureException)
    assert blueprint.error_handler(ServerError) is test_function

# Generated at 2022-06-14 07:30:24.234695
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import sanic

    @sanic.blueprint.exception(IndexError)
    async def index_error(request, exception):
        pass

    assert len(sanic.blueprint._future_exceptions) == 1
    assert isinstance(sanic.blueprint._future_exceptions.pop(),
                      FutureException)

# Generated at 2022-06-14 07:30:30.583874
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    blueprint = Blueprint("test")
    blueprint.exception(ZeroDivisionError, apply=False)(ZeroDivisionError)
    blueprint.exception(ZeroDivisionError, apply=True)(ZeroDivisionError)
    blueprint.exception(ZeroDivisionError, apply=True)(ZeroDivisionError)

    assert blueprint._future_exceptions

# Generated at 2022-06-14 07:30:36.909703
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class blueprint:
        def register(self):
            raise NotImplementedError  # noqa
    class request:
        pass
    class response:
        pass

    em = ExceptionMixin(blueprint)
    @em.exception(ValueError)
    def exception_handler(request, exception):
        pass
    em._apply_exception_handler(em._future_exceptions.pop())
    em.exception_handler(request, ValueError)

# Generated at 2022-06-14 07:30:43.817126
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin1(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

    class ExceptionMixin2(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

    a=ExceptionMixin1()
    b=ExceptionMixin2()
    print("a1: ", a._future_exceptions)
    print("b1: ", b._future_exceptions)
    @a.exception(ExceptionMixin, ExceptionMixin2, apply=False)
    def handler1(request, exception):
        return request


# Generated at 2022-06-14 07:30:50.593915
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    blueprint = Blueprint()
    blueprint.exception(Exception)
    assert isinstance(blueprint._future_exceptions, set)
    assert len(blueprint._future_exceptions) == 1
    assert isinstance(blueprint._future_exceptions.pop(), FutureException)

# Generated at 2022-06-14 07:30:57.157167
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprint import Blueprint

    bp = Blueprint('test', url_prefix='test')
    t = ExceptionMixin()
    assert callable(ExceptionMixin.exception)

    class testexception(Exception):
        pass

    @t.exception(testexception)
    def myhandler(request, exception):
        pass

    assert myhandler in t._future_exceptions

# Generated at 2022-06-14 07:30:58.868715
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:31:08.323227
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Create a blueprint object
    blueprint = Blueprint("test_blueprint")


    @blueprint.exception(ValueError)
    def value_error(request, exception):
        pass


    @blueprint.exception(Exception)
    def exception(request, exception):
        pass


    # Check _future_exceptions set of the blueprint object
    future_exceptions = set()
    future_exceptions.add(FutureException(value_error, (ValueError,)))
    future_exceptions.add(FutureException(exception, (Exception,)))
    assert blueprint._future_exceptions == future_exceptions

# Generated at 2022-06-14 07:31:17.757368
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
  x = ExceptionMixin(1,2)
  with raises(NotImplementedError):
    x.exception()

# Generated at 2022-06-14 07:31:23.460895
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    @Blueprint.exception(Exception)  # noqa
    def handler(request, exception):
        request.ctx.foo = 'bar'
        return 'error'

    assert isinstance(handler, Exception) is not True
    assert handler.__name__ == 'handler'

# Generated at 2022-06-14 07:31:31.014198
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin:
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            return handler

    handler = ExceptionMixin()
    assert handler.exception([1], apply=True)
    assert handler.exception(apply=True)

# Generated at 2022-06-14 07:31:43.628337
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    args = ("test",)
    kwargs = {}
    future_exception = FutureException(None, args)
    assert future_exception._exceptions == ("test", ) and \
        future_exception._handler == None

    from sanic.blueprints import Blueprint
    b = Blueprint()
    assert b._future_exceptions == set()

    def func1():
        return "Hi"
    def func2():
        return "Hi"
    b.exception(exceptions="test")(func1)
    b.exception(exceptions="test1")(func1)
    b.exception(exceptions="test2")(func1)
    b.exception(exceptions="test")(func2)
    b.exception(exceptions="test1")(func2)
    # Test multiple future_exceptions

# Generated at 2022-06-14 07:31:49.792950
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    import asyncio
    from sanic.exceptions import NotFound
    from sanic.response import text, json
    from sanic.blueprints.exceptions import ExceptionMixin

    class Blueprint(ExceptionMixin):
        def __init__(self, name: str, url_prefix: str = None, version: str = None):
            super(Blueprint, self).__init__(name, url_prefix, version)

        def _apply_exception_handler(self, handler: FutureException):
            pass


    class TestBlueprint(unittest.TestCase):
        def test_exception(self):
            bp = Blueprint('bp')

            @bp.exception(NotFound)
            def test(request, exception):
                return json({'status': False, 'message': 'not found'})

           

# Generated at 2022-06-14 07:31:54.683040
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Should raise a TypeError
    try:
        exception_mixin_instance = ExceptionMixin()
        exception_mixin_instance.exception(1,2,3)(1)
    except TypeError:
        print("exception method in ExceptionMixin works as expected")

# Generated at 2022-06-14 07:32:01.407048
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Arrange
    class SanicTestExceptionMixin(ExceptionMixin):
        pass

    testExceptionMixin = SanicTestExceptionMixin()
    # Act

    @testExceptionMixin.exception(Exception)
    def test_exception_handler():
        return 1

    # Assert
    assert isinstance(test_exception_handler, types.FunctionType)

# Generated at 2022-06-14 07:32:04.935550
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    h = ExceptionMixin()
    assert h.exception is ExceptionMixin.exception  # noqa

# Generated at 2022-06-14 07:32:05.587608
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:32:16.175021
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # arrange
    import asyncio
    from sanic.blueprints import Blueprint
    from sanic.response import json
    from sanic.router import Router
    from sanic.request import Request
    from sanic.server import HttpProtocol
    from sanic.utils import generate_uri

    app = Blueprint(name='test', url_prefix='test')

    @app.route("/test")
    async def test(request):
        raise RuntimeError("test error")

    app.add_route(test, "/test")

    @app.exception(RuntimeError)
    def runtime_error_handler(request, exception):
        return json("Internal server error", 500)

    router = Router()
    router.add(app)

    server_settings = {'debug': True}

# Generated at 2022-06-14 07:32:38.480610
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            return handler

    test_mixin = TestExceptionMixin()
    assert test_mixin._future_exceptions == set()

    @test_mixin.exception(KeyError, TypeError)
    def test_handler(request, exception):
        return exception

    assert len(test_mixin._future_exceptions) == 1
    assert test_mixin._future_exceptions.pop() == FutureException(test_handler, (KeyError, TypeError))

# Generated at 2022-06-14 07:32:41.712998
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint("test_bp")
    assert isinstance(bp.exception(), Blueprint)


# Generated at 2022-06-14 07:32:46.351582
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    test = TestExceptionMixin()
    assert isinstance(test.exception(Exception), types.FunctionType)

# Generated at 2022-06-14 07:32:55.340740
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import sys
    import pytest
    from types import MappingProxyType
    from unittest.mock import Mock

    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException

    bp = Blueprint("bp", url_prefix="bp")
    registry = MappingProxyType({})

    handler = Mock()
    exceptions = (KeyError, ValueError)
    exception = FutureException(handler, exceptions)

    # Test case method is not present
    with pytest.raises(NotImplementedError):
        bp._apply_exception_handler(exception)

    # Test case assert method exception signature
    assert hasattr(bp.exception, "__name__") == True
    assert hasattr(bp.exception, "__defaults__") == True

    # Test case assert method decorator

# Generated at 2022-06-14 07:33:07.831674
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    import pytest

    app = Sanic('sanic-test')
    blueprint = Sanic.blueprint(app, url_prefix='/v1', strict_slashes=True)

    @blueprint.exception(ValueError, apply=True)
    async def handle_value_error(request, exception):
        return response.text('Internal server error', 500)

    @blueprint.exception(TypeError)
    async def handle_type_error(request, exception):
        return response.text('Internal server error', 500)

    @blueprint.route('/', methods=['GET'])
    async def tst(request):
        global a
        a = a[1]
        return response.text('OK')


# Generated at 2022-06-14 07:33:21.335200
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test for methods that are not implemented:
    # _apply_exception_handler
    assert ExceptionMixin.__init__
    assert ExceptionMixin._apply_exception_handler
    assert ExceptionMixin.exception
    assert ExceptionMixin._future_exceptions

    # Test the case: _future_exceptions is a set
    obj = ExceptionMixin()
    assert isinstance(obj._future_exceptions, set)

    # Test the case: exceptions is a tuple
    # @obj.exception((_exceptions))
    exceptions = (Exception,)
    obj._apply_exception_handler = mock.Mock()
    obj.exception(*exceptions)()
    obj._future_exceptions.add = mock.Mock()

# Generated at 2022-06-14 07:33:28.733224
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    Test method exception of class ExceptionMixin
    """

    exception_mixin = ExceptionMixin()
    @exception_mixin.exception(Exception)
    def exception_handler(request, exception):
        return exception

    assert len(exception_mixin._future_exceptions) == 1
    
    future_exception = exception_mixin._future_exceptions.pop()
    assert future_exception.handler == exception_handler
    assert len(future_exception.exceptions) == 1
    assert isinstance(future_exception.exceptions[0], type)
    assert future_exception.exceptions[0] == Exception


# Generated at 2022-06-14 07:33:33.435070
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import gc
    from exceptions import NotImplementedError

    def handler():
        pass

    class Test:
        def __init__(self):
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError

    test = Test()
    test.exception(NotImplementedError, apply=True)(handler)
    assert len(test._future_exceptions) == 1
    del test
    gc.collect()

# Generated at 2022-06-14 07:33:43.142392
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.response import html

    class TestClass(ExceptionMixin):
        def __init__(self):
            super(TestClass, self).__init__()

        def _apply_exception_handler(self, handler: FutureException):
            handler._handler(Exception("test"), None)

    exception_mixin = TestClass()

    @exception_mixin.exception(Exception)
    def handler(request, exception):
        return html("test")

    assert len(exception_mixin._future_exceptions) == 1

    future_exception: FutureException = list(exception_mixin._future_exceptions)[0]

    assert future_exception._exceptions == (Exception,)
    assert isinstance(future_exception._handler(Exception("test"), None), html)

# Generated at 2022-06-14 07:33:56.236314
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    blueprint = BlueprintMixin()
    blueprint.name = "Test"
    blueprint.url_prefix = "/test"

    @blueprint.exception(ZeroDivisionError)
    def ZeroDivisionError_handler(request, exception):
        pass

    @blueprint.exception([TypeError, ZeroDivisionError])
    def TypeError_ZeroDivisionError_handler(request, exception):
        pass

    assert len(blueprint._future_exceptions) == 2

    try:
        1/0
    except ZeroDivisionError:
        for exception_handler in blueprint._future_exceptions:
            if exception_handler.exceptions == (ZeroDivisionError,):
                exception_handler.handler(request, ZeroDivisionError)


# Generated at 2022-06-14 07:34:35.041534
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_exception_Test(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

        def index(self, request):
            assert request.method == 'GET'
            return await self.request.app.redis.incr('counter')

        def post(self, request):
            assert request.method == 'POST'
            # return 'I am post'

    @ExceptionMixin_exception_Test.exception(TypeError, ValueError)
    async def exception_handler(request, exception):
        return text('Internal server error', 500)

    ExceptionMixin_exception_Test.route('/', 'GET', index)
    # ExceptionMixin_exception_Test.route('/', 'POST', post)


# Generated at 2022-06-14 07:34:45.336730
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    The unit test for the ExceptionMixin exception method
    """
    class ExecptionMixinTest(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler):
            handler.handler(FileNotFoundError)

    exception_mixin = ExecptionMixinTest()

    @exception_mixin.exception(IndexError)
    async def test(request, exception):
        """
        :return: Handler of exception method
        """
        return request, exception

    assert len(exception_mixin._future_exceptions) == 1
    assert isinstance(exception_mixin._future_exceptions.pop(), FutureException)

# Generated at 2022-06-14 07:34:51.411462
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def handler():
        pass

    set_future_exceptions = set()
    exception_mixin = ExceptionMixin()
    exception_mixin._future_exceptions = set_future_exceptions
    exception_mixin.exception(Exception)(handler)
    future_exception = FutureException(handler, (Exception,))
    assert future_exception in set_future_exceptions

# Generated at 2022-06-14 07:35:01.625503
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass
    test_exception_mixin = TestExceptionMixin()
    @test_exception_mixin.exception(Exception, apply=True)
    def test_exception_handler(request, exception):
        pass
    assert len(test_exception_mixin._future_exceptions) == 1
    assert test_exception_mixin._future_exceptions.pop().exceptions == (Exception,)

# Generated at 2022-06-14 07:35:15.568803
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Define a mockup class FutureException
    class MockupFutureException:
        def __init__(self, handler, exceptions):
            self.handler = handler
            self.exceptions = exceptions
            self.__str__ = self.handler
            self.__repr__ = self.handler
        
        def __hash__(self):
            return hash(self.handler)

    # Define a mockup class Handler
    class Handler:
        def __init__(self):
            self.handled_exceptions = None

        def __call__(self, request, exception):
            self.handled_exceptions = exception

    # Define a mockup class ExceptionMixin

# Generated at 2022-06-14 07:35:21.913943
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            return handler

    test_mixin = TestExceptionMixin()
    @test_mixin.exception(Exception, apply=True)
    def test_handler(request, exception: Exception):
        return 'caught'

    assert len(test_mixin._future_exceptions) == 1


test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:35:31.991327
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.exception_handling import FutureException
    from sanic.models.blueprints import Blueprint
    from unittest import mock

    blueprint = Blueprint("Prefix")
    blueprint._apply_exception_handler = mock.Mock()
    decorator = blueprint.exception(Exception)
    handler = mock.Mock()
    decorator(handler)
    assert blueprint._future_exceptions == {
        FutureException(handler, (Exception,))
    }
    blueprint._apply_exception_handler.assert_called_once_with(
        blueprint._future_exceptions.pop()
    )



# Generated at 2022-06-14 07:35:36.928973
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    bp = Blueprint("test")

    @bp.exception(Exception)
    async def handle_exception(request, exception):
        return text("ok")

    assert bp.exception_handlers



# Generated at 2022-06-14 07:35:43.463295
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class SanicMock(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print(handler)

    sanic_mock = SanicMock()

    @sanic_mock.exception([ValueError])
    def handler(request, exception):
        print(request)
        print(exception)


# Generated at 2022-06-14 07:35:45.129853
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert ExceptionMixin.exception.__doc__ is not None

# Generated at 2022-06-14 07:36:54.609099
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(Exception)
    def handler(*args, **kwargs):
        raise Exception("Exception")
    
    cls = ExceptionMixin.__new__(ExceptionMixin)

    assert cls.exception is handler
    assert cls._future_exceptions == set()

# Generated at 2022-06-14 07:37:02.260508
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyBlueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            # "Debug" method, the test should check this method was called with
            # the correct parameter
            print(handler)
            from unittest.mock import sentinel

            # Handler must be a sentinel
            return sentinel

    blueprint = MyBlueprint()
    print(blueprint)
    # Call to exception method
    blueprint.exception(Exception)


# Generated at 2022-06-14 07:37:12.752010
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            self.exit = 1
            if str(handler.handler) == 'f1':
                self.exit = 0

    e = TestExceptionMixin()

    @e.exception(ValueError)
    def f1(request, exception, kwargs):
        return 'a'

    assert e.exit == 0
    assert f1('request', 'exception', 'kwargs') == 'a'

    @e.exception([ValueError])
    def f2(request, exception, kwargs):
        return 'a'

    assert f2('request', 'exception', 'kwargs') == 'a'

# Generated at 2022-06-14 07:37:20.914905
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import types
    ExceptionMixinObj = ExceptionMixin()
    result = ExceptionMixinObj.exception(ValueError, IndexError)
    assert result is not None
    assert result is types.FunctionType
    assert isinstance(result, types.FunctionType)
    @ExceptionMixinObj.exception(ValueError, IndexError)
    def test(request):
        pass
    assert isinstance(test, types.FunctionType)
    assert test.__name__ == 'test'
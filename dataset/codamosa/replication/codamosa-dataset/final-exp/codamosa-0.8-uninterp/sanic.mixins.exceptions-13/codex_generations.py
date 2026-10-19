

# Generated at 2022-06-14 07:27:21.819976
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException
    from sanic.response import HTTPResponse

    test_exception = Exception("This is a test exception")

    bp = Blueprint("TestBlueprint")

    @bp.exception(apply=False)
    async def test_handler(request, exception):
        """This function is used as a global error handler for
        all routes registered under this blueprint
        """
        assert isinstance(exception, Exception)
        assert exception == test_exception

        return HTTPResponse("This is a test handler")

    future_exception = FutureException(test_handler, (Exception, ))
    future_exceptions = set()
    future_exceptions.add(future_exception)

    assert bp._future_exceptions == future_

# Generated at 2022-06-14 07:27:24.395810
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Mock object
    class _A: pass

    # Instance
    a = ExceptionMixin()

    # result
    result = a.exception(Exception)(_A())

    # Assert
    assert result

# Generated at 2022-06-14 07:27:34.552014
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from unit_tests.utilities.test_blueprint import blueprint
    blueprint.exception(ZeroDivisionError, apply=False)(lambda x: x)

    assert blueprint._future_exceptions
    assert blueprint._future_exceptions[0]
    assert blueprint._future_exceptions[0].handler(lambda x: x)
    assert blueprint._future_exceptions[0].exceptions == (ZeroDivisionError,)
    assert blueprint._future_exceptions[0].kwargs == {}

# Generated at 2022-06-14 07:27:47.599104
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class SanicExceptionsTest(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    a = SanicExceptionsTest()
    @a.exception(IOError)
    def handler_io_error(request, exception):
        return 'foo'

    @a.exception(OSError)
    def handler_os_error(request, exception):
        return 'bar'

    class MyExcep(Exception):
        pass

    @a.exception(MyExcep)
    def handler_my_excep(request, exception):
        return 'foobar'

    assert len(a._future_exceptions) == 3

    as_list = list(a._future_exceptions)

    assert as_list[0].handler == handler_io_error

# Generated at 2022-06-14 07:27:56.264934
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    print("Testing method exception of class ExceptionMixin")
    class A(ExceptionMixin):
        pass
    a = A()
    print("Initially, _future_exceptions is {}".format(a._future_exceptions))
    print("Starting with test")
    exception_handler = Exception("This is a test")
    ex = a.exception(exception_handler)
    print("_future_exceptions is now {}".format(a._future_exceptions))
    assert ex == exception_handler
    assert len(a._future_exceptions) == 1

# Generated at 2022-06-14 07:27:58.257770
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    with pytest.raises(NotImplementedError):
        ExceptionMixin().exception(RuntimeError)

# Generated at 2022-06-14 07:28:02.247896
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint

    bp = Blueprint('test_ExceptionMixin_exception')
    @bp.route('/')
    async def hello(request):
        """
        dummy function
        """
        return text('Hello world!')

    @bp.exception(Exception)
    def _exception_handler(request, exception):
        """
        dummy function
        """
        print('inside second exception handler!')
        return text('Internal server error')

# Generated at 2022-06-14 07:28:07.206785
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def handler():
        try:
            raise IndexError
        except Exception as e:
            print(e)
            return "Exception Handler"
    
    blueprint = Blueprint()
    blueprint.exception(IndexError)(handler)
    assert "Exception handler" == blueprint._future_exceptions.pop().handler()

# Generated at 2022-06-14 07:28:14.015915
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint

    class CustomException(Exception):
        pass

    async def handler(request, exception):
        pass

    bp = Blueprint("bp")
    app = Sanic("test_exception_handler")
    bp.exception(CustomException)(handler)
    bp.bind(app)

    assert bp._exception_handler_order[CustomException] == handler

# Generated at 2022-06-14 07:28:25.169356
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    import inspect

    app = Sanic('test_app_exception')
    app.blueprint(ExceptionMixin)

    @app.route('/exception')
    @app.exception(IndexError)
    def handler_function_exception(request, exception):
        return text('OK')

    assert hasattr(app.exception, '__call__')
    assert inspect.ismethod(app.exception) is True
    assert app.exception.__name__ == 'exception'

    assert app.exception.__code__.co_argcount == 1
    assert app.exception.__code__.co_varnames == ('handler',)

    assert hasattr(app,'_future_exceptions') is True

# Generated at 2022-06-14 07:28:34.209127
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest.mock as mock

    def handler(request, exception):
        return 0

    exceptions_list = [ZeroDivisionError]
    bp = ExceptionMixin(None)
    bp._apply_exception_handler = mock.Mock()

    @bp.exception(*exceptions_list)
    def handler(request, exception):
        return None

    bp._apply_exception_handler.assert_called_once_with(
        FutureException(handler, exceptions_list),
    )

# Generated at 2022-06-14 07:28:46.450377
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
    p = TestExceptionMixin()
    @p.exception()
    def test(req):
        return 'get from test'
    assert p._future_exceptions == {FutureException(test, ())}
    p = TestExceptionMixin()
    @p.exception([Exception, BaseException])
    def test(req):
        return 'get from test'
    assert p._future_exceptions == {FutureException(test, (Exception, BaseException))}


if __name__ == '__main__':
    test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:28:51.685689
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    e = ExceptionMixin()
    @e.exception(BaseException)
    def abc():
        return "Exception handler"
    assert e._future_exceptions[0].handler == abc
    assert e._future_exceptions[0].exceptions[0] == BaseException

# Generated at 2022-06-14 07:29:00.677945
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprints import Blueprint

    blueprint = Blueprint.new()

    @blueprint.exception(Exception, 500, foo='bar')
    def exception_handler(self, request, exception):
        pass

    assert len(blueprint._future_exceptions) == 1
    future_exception = blueprint._future_exceptions.pop()
    assert future_exception.handler == exception_handler
    assert future_exception.exceptions == (Exception,)
    assert future_exception.kwargs == {'foo':'bar'}

# Generated at 2022-06-14 07:29:09.575340
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    args = []
    kwargs = {}
    exception_mixin = MyExceptionMixin(1, 2, 3, 4)
    @exception_mixin.exception()
    def handler_for_exception(*args, **kwargs):
        pass
    args = []
    kwargs = {}
    handler_for_exception(*args, **kwargs)

# Generated at 2022-06-14 07:29:21.593823
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # create sanic app
    app = Sanic('test_ExceptionMixin')

    @app.blueprint(name='test_ExceptionMixin', url_prefix='/test_ExceptionMixin')
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    # check obj TestExceptionMixin is not empty
    obj_TestExceptionMixin = TestExceptionMixin()
    assert obj_TestExceptionMixin is not None

    # check obj TestExceptionMixin.exception is not empty
    assert obj_TestExceptionMixin.exception is not None

# Generated at 2022-06-14 07:29:22.162675
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:29:27.628972
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    bp = Blueprint(__name__)
    assert bp._future_exceptions == set()
    assert isinstance(bp._future_exceptions, set)

    @bp.exception(Exception, apply=True)
    def handler(request, exception):
        # handler that will handle exceptions
        assert request is not None
        assert exception is not None
        assert exception.status



# Generated at 2022-06-14 07:29:36.401955
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # 1. Arrange
    from sanic.blueprints import Blueprint
    class ExceptionMixin_exception_Test(Blueprint, ExceptionMixin):
        pass

    exceptionMixin_exception_Test = ExceptionMixin_exception_Test("test_ExceptionMixin_exception")

    # 2. Act
    @exceptionMixin_exception_Test.exception(Exception, apply=False)
    def test(request, exception):
        pass


    # 3. Assert
    assert len(exceptionMixin_exception_Test._future_exceptions) == 1

# Generated at 2022-06-14 07:29:45.131965
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTestClass(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            return True

    test_class = ExceptionMixinTestClass()

    class ErrorException(Exception):
        pass

    @test_class.exception(ErrorException)
    def test_exception_handler():
        return True

    assert len(test_class._future_exceptions) == 1

# Generated at 2022-06-14 07:29:53.925621
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint():
        def add_exception_handler(self, exception: FutureException):
            raise NotImplementedError  # noqa

    blueprint = Blueprint()

    blueprint = ExceptionMixin()
    blueprint.__init__()

    blueprint.exception(ValueError)(lambda request, exception: 10)

    blueprint._future_exceptions = set()

    blueprint.exception(ValueError)(lambda request, exception: 10)

# Generated at 2022-06-14 07:30:05.133264
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from project.blueprint.blueprint import Blueprint
    from project.blueprint.blueprint import route
    from project.blueprint.blueprint import response
    from project.blueprint.exception import SanicException
    from project.blueprint.exception import SanicExceptionClass
    from sanic.exceptions import ServerError
    from project.util.type import function

    @route('/exception', methods=['GET'])
    def view_function():
        raise SanicException(ServerError, "Server Error", "Something went wrong")

    class SanicBlueprint(ExceptionMixin, Blueprint):
        pass

    sanic_blueprint = SanicBlueprint(__name__)
    sanic_blueprint.exception(ServerError)(function)
    # sanic_blueprint.response(SanicException)(function_response)
    sanic

# Generated at 2022-06-14 07:30:12.311473
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            print(handler)

    a = MyExceptionMixin()
    a.exception(Exception, apply=True)(lambda x, y: x + y)

# Generated at 2022-06-14 07:30:24.665094
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Create new ExceptionMixin class instance
    from sanic.blueprints import Blueprint
    test_instance = Blueprint('test_exception_mixin', url_prefix="/testing")

    # Test if applying exception handler
    @test_instance.exception(apply=True)
    async def error_handler(request, exception):
        pass

    # Test if not applying exception handler
    @test_instance.exception(IndexError, apply=False)
    async def error_handler_2(request, exception):
        pass

    # Test if adding exceptions to handler
    @test_instance.exception(apply=True)
    async def error_handler_3(request, exception) -> int:
        pass

    # Test if not adding exceptions if index error

# Generated at 2022-06-14 07:30:34.848785
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(ExceptionMixin, self).__init__(*args, **kwargs)
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            return None

    class SimpleException(Exception):
        def __init__(self, message):
            self.message = message

    @TestExceptionMixin.exception(SimpleException)
    def test_handler(request, exception):
        return "testing"

    assert len(TestExceptionMixin._future_exceptions) == 1

# Generated at 2022-06-14 07:30:39.945206
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import os
    import sys
    utility_path = os.path.join(os.path.dirname(__file__), '..', '..', 'utility')
    sys.path.append(utility_path)
    from util import test_blueprint_class
    test_blueprint_class(ExceptionMixin)

# Generated at 2022-06-14 07:30:44.275256
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    future_exception = FutureException(object, object)
    future_exceptions: Set[FutureException] = set()
    future_exceptions.add(future_exception)
    assert future_exception == object

# Generated at 2022-06-14 07:30:51.501999
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    blueprint = Blueprint("test")
    blueprint_decorator = blueprint.exception(Exception, apply=False)

    @blueprint_decorator
    def handler(request, exception):
        assert request == "request"
        assert exception == "exception"

    blueprint._apply_exception_handler(blueprint._future_exceptions.pop())
    blueprint._exception_handler(request="request", exception="exception")

# Generated at 2022-06-14 07:30:58.627325
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_Unit(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)
            self.value = 0

        def _apply_exception_handler(self, handler: FutureException):
            self.value =  1

    mixin = ExceptionMixin_Unit()

    def handler():
        return None

    assert(not decorated(handler=handler, exceptions=(), apply=False))
    assert(decorated(handler=handler, exceptions=(), apply=True))

# Generated at 2022-06-14 07:31:04.456492
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    exception_mixin = TestExceptionMixin()

    @exception_mixin.exception(Exception)
    def handler():
        pass

    assert len(exception_mixin._future_exceptions) == 1

# Generated at 2022-06-14 07:31:09.168270
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert False


# Generated at 2022-06-14 07:31:16.137670
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Bysan:
        pass

    class ExMixin(ExceptionMixin):
        pass

    class Sanic(Bysan, ExMixin):
        pass

    assert "exception" in Sanic.__dict__
    assert Sanic.exception.__name__ == "decorator"
    assert isinstance(Sanic.exception(*[Exception]), Sanic.exception)
    assert isinstance(Sanic.exception.__call__(*[Exception]), Sanic.exception)

# Generated at 2022-06-14 07:31:25.024503
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    from sanic import Sanic

    blueprint = Blueprint(__name__)

    @blueprint.exception(Exception)
    def handler(request, exception):
        pass

    assert blueprint._future_exceptions
    assert isinstance(blueprint._future_exceptions, set)
    assert len(blueprint._future_exceptions) == 1

    sanic = Sanic(__name__)
    sanic.blueprint(blueprint)

    assert sanic.error_handler is handler

# Generated at 2022-06-14 07:31:33.564107
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # create instance of ExceptionMixin
    instance = ExceptionMixin()

    # create a mock function for the handler, which should be returned by
    # the decorator
    def handler(x, y):
        pass

    # mock of the apply method, to make sure it gets called if and only if
    # apply is True
    def apply(x):
        pass

    # create a mock of the FutureException class
    class FG:
        def __init__(self, handler, exceptions):
            self.handler = handler
            self.exceptions = exceptions
    future_exception = FG(handler, (ValueError,))

    # mock the add method
    instance._future_exceptions.add = lambda x: None
    # mock the call of the apply method
    instance._apply_exception_handler = lambda x: apply(x)

    # Test

# Generated at 2022-06-14 07:31:45.478483
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from unittest.mock import patch
    class DummyException(Exception):
        pass

    class DummyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    class DummyApp(DummyExceptionMixin, Sanic):
        pass
    app = DummyApp()
    mock_handler = patch.object(app, '_apply_exception_handler')

    # AssertionError when decorator implements no handler
    with pytest.raises(AssertionError):
        decorator = app.exception(DummyException)
        decorator(None)
    mock_handler.assert_not_called()

    # AssertionError when decorator implements no exception

# Generated at 2022-06-14 07:31:52.433097
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from unittest.mock import MagicMock

    def handler():
        pass

    exception_mixin = ExceptionMixin()
    exception_mixin.exception(Exception, apply=True)(handler)
    exception_mixin._apply_exception_handler = MagicMock()
    assert exception_mixin.exception(Exception, apply=False) == handler
    with pytest.raises(TypeError):
        exception_mixin.exception([Exception])

# Generated at 2022-06-14 07:31:56.305676
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    class ExceptionMixinTest(Blueprint, ExceptionMixin):
        pass

    blueprint = ExceptionMixinTest('test_ExceptionMixin')
    blueprint.exception(ValueError)

# Generated at 2022-06-14 07:31:57.074980
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:32:07.690508
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    class A(Exception):
        pass

    class B(Exception):
        pass

    exception_mixin = ExceptionMixin()

    def test_exception_handler(request, exception):
        pass

    try:
        exception_mixin.exception(A, B)(test_exception_handler)
    except NotImplementedError:
        assert True
    else:
        assert False

    blueprint = Blueprint('test', url_prefix='test')
    blueprint.exception([A, B])(test_exception_handler)
    assert len(blueprint._future_exceptions) == 1
    exception = blueprint._future_exceptions.pop()
    assert test_exception_handler == exception.handler
    assert isinstance(exception.exceptions, tuple)
    assert A in exception.ex

# Generated at 2022-06-14 07:32:17.213702
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """Unit tests for method exception of class ExceptionMixin"""

    @sanic.blueprint.blueprint('test_ExceptionMixin_exception', url_prefix='/prefix')
    class ExceptionMixinMock(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _set_name(self, name):
            self.name = name

        def _apply_exception_handler(self, handler):
            self.exception_handler = handler

    class HandlerMock:
        def __init__(self, *args, **kwargs):
            pass

        def __call__(self, *args, **kwargs):
            pass

    mock = ExceptionMixinMock()

# Generated at 2022-06-14 07:32:32.214543
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            return

        def fake_handler(self):
            return

    a = A()
    a.exception(Exception)(a.fake_handler)

    assert len(a._future_exceptions) == 1

# Generated at 2022-06-14 07:32:40.417669
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.exception_mixin import ExceptionMixin
    from sanic.models.futures import FutureException

    result_tuple = ExceptionMixin.exception()

    assert callable(result_tuple)

    result_tuple(Exception)

    result_tuple = FutureException(Exception, Exception)

    assert isinstance(result_tuple, FutureException)

# Generated at 2022-06-14 07:32:43.683711
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    @Blueprint.exception(Exception)
    def handler():
        raise ValueError()

    assert isinstance(handler, types.FunctionType)

# Generated at 2022-06-14 07:32:54.378302
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    from sanic.exceptions import NotFound
    from sanic.request import Request
    from sanic.response import json

    blueprint_abc = Blueprint('abc', url_prefix='abc',version='abc')
    blueprint_abc.exception(NotFound)(lambda request: json({'error': 'Not found'}))
    blueprint_abc.exception(NotFound, apply=False)(lambda request: json({'error': 'Not found'}))

    blueprint_bcd = Blueprint('bcd', url_prefix='bcd',version='bcd')
    blueprint_bcd.exception(NotFound, apply=False)(lambda request: json({'error': 'Not found'}))



# Generated at 2022-06-14 07:33:05.095561
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestClass(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

        def test_case(self):
            global decorated_handler
            @self.exception(Exception, ValueError, apply=True)
            def decorated_handler(request, exception, *args, **kwargs):
                raise NotImplementedError  # noqa

            @self.exception([Exception, ValueError], apply=True)
            def decorated_handler_with_list(request, exception, *args, **kwargs):
                raise NotImplementedError  # noqa

    test_class = TestClass()
    test_class.test_

# Generated at 2022-06-14 07:33:08.589294
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        pass

    exception_mixin = TestExceptionMixin()
    exception_mixin.exception(RuntimeError)

# Generated at 2022-06-14 07:33:18.719722
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class U:
        def __init__(self):
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    from sanic.blueprints import Blueprint

    bp = Blueprint('name', url_prefix='')
    assert bp._future_exceptions == set()

    @bp.exception(ValueError, apply=True)
    def handler(request, exception):
        return exception

    assert bp._future_exceptions != set()

    return True

# Generated at 2022-06-14 07:33:24.713368
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
  # Create a instance of ExceptionMixin
  # exception_mixin = ExceptionMixin()

  # TODO: Needs to find a way to mock the decorator "decorator"
  # @exception_mixin.exception(KeyError)
  # def handle_exception(request, exception):
  #     pass
  pass

# Generated at 2022-06-14 07:33:30.101468
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exception_mixin = ExceptionMixin()

    @exception_mixin.exception(ValueError)
    def handler():
        pass

    assert len(exception_mixin._future_exceptions) == 1
    assert isinstance(exception_mixin._future_exceptions, set)



# Generated at 2022-06-14 07:33:33.245567
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception
    def my_exception():
        print("my_exception")

    my_exception()

# Generated at 2022-06-14 07:33:59.634270
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    '''
    Test case for exception method of ExceptionMixin class
    '''
    import pytest
    from sanic.models.futures import FutureException
    from typing import Any
    from typing import Set

    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            super(TestExceptionMixin, self).__init__()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    bp = TestExceptionMixin()

    # Test default value of variable apply in exception method
    assert bp.exception(TypeError)(None) == None
    future_exception = FutureException(None, (TypeError,))
    assert future_exception in bp._future_exceptions

    # Test custom value of variable apply in exception method
    apply = False
    assert bp

# Generated at 2022-06-14 07:34:02.303659
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    test_instance = ExceptionMixin()
    result = test_instance.exception(Exception)
    assert result == decorator


# Generated at 2022-06-14 07:34:08.008251
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import SanicException

    blueprint = Blueprint('test', url_prefix='test')

    @blueprint.exception(SanicException)
    def handler(request, exception):
        pass

    assert blueprint._future_exceptions

test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:34:11.671393
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.router import ExceptionMixin
    em = ExceptionMixin()
    em_exception = em.exception(Exception)
    def em_decorator(handler):
        return handler

# Generated at 2022-06-14 07:34:16.846171
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic import response

    bp = Blueprint(__name__)

    @bp.exception(Exception)
    def handle_exception(request, exception):
        return response.json({"exception": str(exception)})

    @bp.route("/")
    def handler(request):
        raise Exception("This is an exception!")

    app = bp.as_app()
    client = app.test_client()
    request, response = client.get("/")

    assert response.json["exception"] == "This is an exception!"

# Generated at 2022-06-14 07:34:29.821581
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.data = {}
        def _apply_exception_handler(self, handler: FutureException):
            self.data.update({'exception': handler})

    a = A()
    exceptions = [Exception, KeyError]
    @a.exception(*exceptions, apply=True)
    def handler(*args, **kwargs):
        pass
    assert a.data['exception'].handler is handler
    assert a.data['exception'].args == exceptions

    exceptions = [[Exception, KeyError]]
    @a.exception(*exceptions, apply=True)
    def handler2(*args, **kwargs):
        pass
    assert a.data

# Generated at 2022-06-14 07:34:34.918709
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionTest(ExceptionMixin):
        def __init__(self):
            pass
    obj = ExceptionTest()
    with pytest.raises(NotImplementedError):
        obj._apply_exception_handler(None)

# Generated at 2022-06-14 07:34:44.769491
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            ExceptionMixin.__init__(self)

        def _apply_exception_handler(self, handler):
            pass

    test_exception_mixin = TestExceptionMixin()

    def exception_handler(*args, **kwargs):
        pass

    @test_exception_mixin.exception(ValueError)
    def assert_exception(handler):
        assert isinstance(handler, FutureException)
        assert handler.exceptions == (ValueError,)
        assert handler.handler == exception_handler

    assert_exception(exception_handler)

# Generated at 2022-06-14 07:34:57.750534
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from operator import add
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.server import HttpProtocol

    from sanic.blueprints import Blueprint

    blueprint = Blueprint("test_blueprint", url_prefix="/test")

    @blueprint.exception(ZeroDivisionError)
    async def zero_division(request: Request, exception: ZeroDivisionError):
        return HTTPResponse(body=str(exception), status=500)

    @blueprint.route("/zero_division")
    async def test_zero_division(request: Request):
        return add(1, 1) / 0

    request, response = HttpProtocol.create_request_and_response(blueprint)
    protocol = HttpProtocol(request, response)

    test_zero_division

# Generated at 2022-06-14 07:35:01.920619
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic

    app = Sanic('test_app')
    test_exception = ExceptionMixin(app)

    @test_exception.exception([TypeError, Exception])
    def handler(request, exception):
        return 'Handle an exception'

    assert test_exception._future_exceptions

# Generated at 2022-06-14 07:35:40.330255
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    app = Sanic('test_ExceptionMixin')
    class test_ExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass
    my_test_ExceptionMixin = test_ExceptionMixin()
    response = app.exception(NotImplementedError)(my_test_ExceptionMixin.exception(NotImplementedError))(app)
    assert not isinstance(response, FutureException)
    assert isinstance(response, Sanic)

# Generated at 2022-06-14 07:35:50.678670
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixinEx(ExceptionMixin):

        def __init__(self, *args, **kwargs) -> None:
            self.args = args
            self.kwargs = kwargs
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler):
            self.handler = handler

    testmixin = TestExceptionMixinEx('testexception', 'testexception2')
    def test_exception_handler(request, exception):
        return "Here we are"
    testmixin.exception('testexception')(test_exception_handler)
    assert testmixin.handler.handler == test_exception_handler
    assert testmixin.handler.exceptions == ('testexception',)

# Generated at 2022-06-14 07:35:54.389804
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def decorator(handler): return handler

    em = ExceptionMixin()
    em.exception(decorator)

    #Unit test for parameter apply of method exception
    #assert em._future_exceptions.pop()._apply == False

# Generated at 2022-06-14 07:36:01.790538
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.testing import SanicTestClient

    from .main import app

    async def handler(request, exception):
        return sanic.response.json({"exception": exception}, status=500)

    app.exception(handler)

    client = SanicTestClient(app)
    response = client.get("/")
    assert response.json["exception"] == "NotFound"
    assert response.status == 500
    response = client.get("/headers")
    assert response.json["exception"] == "NotAcceptable"
    assert response.status == 500



# Generated at 2022-06-14 07:36:09.386650
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    
    @blueprint.route("/exception")
    @blueprint.exception(IndexError, apply=True)
    def handler1(request, exception):
        return response.text("Failed with {}".format(exception.__class__.__name__))

    @blueprint.route("/multiple_exception")
    @blueprint.exception([IndexError, ValueError], apply=True)
    def handler2(request, exception):
        return response.text("Failed with {}".format(exception.__class__.__name__))

# Generated at 2022-06-14 07:36:11.199889
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert ExceptionMixin.exception.__doc__ is not None

# Generated at 2022-06-14 07:36:22.240837
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import sanic

    class MyBlueprint(ExceptionMixin, sanic.Blueprint):
        def __init__(self, *args, **kwargs):
            super(MyBlueprint, self).__init__(*args, **kwargs)

    test_my_blueprint = MyBlueprint("test_my_blueprint", url_prefix="/test")

    @test_my_blueprint.exception
    def my_exception_handler(request, exception):
        return request.json

    assert(type(test_my_blueprint.exception) ==
           type(test_my_blueprint._apply_exception_handler))
    assert(test_my_blueprint._future_exceptions.__len__() == 1)

# Generated at 2022-06-14 07:36:30.287681
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print('MyExceptionMixin::_apply_exception_handler()')
    ex = MyExceptionMixin()
    @ex.exception(ValueError)
    def add(a, b):
        return a + b
    print(add(1,2))

test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:36:40.378171
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # GIVEN a blueprint and its function
    url_prefix = "/api"
    blueprint = Blueprint("test_blueprint", url_prefix=url_prefix)

    def decorated_handler():
        pass

    # WHEN exception decorator is added to function
    error_message = "exception called"
    blueprint.exception(TypeError, apply=True, error_message=error_message)(decorated_handler)

    # THEN the decorated_handler is added to future_exceptions
    assert(len(blueprint._future_exceptions) == 1)
    assert(blueprint._future_exceptions.pop() == FutureException(decorated_handler, TypeError, error_message))


# Generated at 2022-06-14 07:36:53.235179
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.response import text
    from sanic.exceptions import NotFound
    from sanic.models.futures import FutureException

    bp = Blueprint('bp', url_prefix='/bp')
    bp.exception(NotFound)(lambda request, exception: text('not found1'))
    bp.exception(NotFound, apply=False)(lambda request, exception: text('not found2'))
    bp.exception([NotFound])(lambda request, exception: text('not found3'))
    bp.exception([NotFound, NotFound])(lambda request, exception: text('not found4'))

    assert len(bp._future_exceptions) == 4
    assert isinstance(bp._future_exceptions.pop(), FutureException)
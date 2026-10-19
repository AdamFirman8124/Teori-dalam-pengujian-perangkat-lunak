

# Generated at 2022-06-14 07:27:13.979948
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(Exception)
    def my_exception(request, exception):
        return "Handler exception"

    assert issubclass(Exception, tuple(my_exception._future_exceptions)[0].exceptions)
    assert "Handler exception" == my_exception(None, Exception())

# Generated at 2022-06-14 07:27:26.128771
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.exceptions import ServerError

    class MyExceptionMixin(ExceptionMixin):
        def __init__(self):
            super(MyExceptionMixin, self).__init__()

        def _apply_exception_handler(self, handler):
            print("Applied handler")
            assert True

    exception_mixin = MyExceptionMixin()

    # Check valid method def
    @exception_mixin.exception(ServerError)
    def handler():
        assert True

    # Check invalid method def
    @exception_mixin.exception(ServerError)
    def handler_2(a):
        assert False

    # Check valid method def, with no apply
    @exception_mixin.exception(ServerError, apply=False)
    def handler_3():
        assert True

    # Check invalid method def

# Generated at 2022-06-14 07:27:36.548619
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    my_exceptions = ('BaseException', 'ValueError', 'Exception')
    my_handler = lambda x: x

    # Create an object of ExceptionMixin
    ex = ExceptionMixin()

    # Assert the size of the future_exceptions set before calling
    # method exception of class ExceptionMixin
    assert len(ex._future_exceptions) == 0

    # Call method exception of class ExceptionMixin
    ex.exception(apply=True)(my_exceptions)(my_handler)

    # Assert the size of the future_exceptions set after calling
    # method exception of class ExceptionMixin
    assert len(ex._future_exceptions) == 1

# Generated at 2022-06-14 07:27:48.079056
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import pytest
    from sanic.models.future_exceptions import FutureException
    from sanic.router import Router
    from sanic.blueprints import Blueprint

    class MyBlueprint(Router, Blueprint, ExceptionMixin):
        def __init__(self, url_prefix=None, name=None):
            self._future_exceptions: Set[FutureException] = set()
            Router.__init__(self, url_prefix, name)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    @MyBlueprint.exception(IndexError)
    def error_handler(request, exception):
        pass

    @MyBlueprint.exception(IndexError, ValueError)
    def error_handler_2(request, exception):
        pass


# Generated at 2022-06-14 07:27:54.455761
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.exceptions = ((Exception, ), {}, lambda _: print('hi'))

        def _apply_exception_handler(self, handler):
            assert self.exceptions == handler.exceptions

    a = A()
    a.exception()(lambda _: print('hi'))

# Generated at 2022-06-14 07:28:02.653377
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.response import text
    from sanic.models.futures import FutureException
    from sanic.blueprints import Blueprint

    app = Sanic('test_ExceptionMixin_exception')

    test_bp = Blueprint('test_ExceptionMixin_exception')

    @app.listener('before_server_start')
    async def before_server_start(app, loop):
        test_bp.exception()(text)(ValueError)
        app.blueprint(test_bp)

    @test_bp.route('/')
    def handler(request):
        raise ValueError('This is a ValueError!')

    request, response = app.test_client.get('/')

    assert response.status == 500
    assert request.app.exception_handler.exceptions


# Generated at 2022-06-14 07:28:14.758392
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.exceptions import add_status_code
    import sys

    class CustomException(Exception):
        def __init__(self, message):
            self.message = message

    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    test_obj = TestExceptionMixin()
    test_func = test_obj.exception(CustomException)

    def decorator(handler):
        future_exception = FutureException(handler, CustomException)
        test_obj._future_exceptions.add(future_exception)
       

# Generated at 2022-06-14 07:28:23.780152
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestClass(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler: FutureException) -> None:
            pass

    test = TestClass()
    @test.exception('a')
    def handler():
        pass

    _handler = handler
    _future_exceptions = test._future_exceptions

    assert len(_future_exceptions) == 1
    assert handler in [exc.handler for exc in _future_exceptions]
    assert (Exception, 'a') in [exc.exceptions for exc in _future_exceptions]

# Generated at 2022-06-14 07:28:34.978887
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class blueprint:
        def add_route(self, path, handler, method):
            return path

    dummy_bp = blueprint()
    class DummyExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.bp = dummy_bp

        def _apply_exception_handler(self, handler):
            handler.apply(self.bp)

    dummy_exception_mixin = DummyExceptionMixin()
    exception = dummy_exception_mixin.exception(Exception)
    def dummy_handler():
        return "exception handler"

    handler = exception(dummy_handler)
    assert len(dummy_exception_mixin._future_exceptions) == 1

# Generated at 2022-06-14 07:28:38.008616
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(IndexError)
    def exc_hand():
        raise IndexError()

    print("Unit test for method exception of class ExceptionMixin")
    exc_hand()

# Generated at 2022-06-14 07:28:49.125527
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Mixin(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass

    mixin = Mixin()
    assert not mixin._future_exceptions

    def exception_handler():
        pass

    mixin.exception(KeyError)(exception_handler)
    assert mixin._future_exceptions
    assert mixin._future_exceptions == {FutureException(
        exception_handler, (KeyError,))}
    assert mixin._future_exceptions.pop().handler == exception_handler

# Generated at 2022-06-14 07:28:50.468858
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:29:02.160456
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.route import Route
    from sanic.models.endpoint import Endpoint
    from sanic.models.futures import FutureException
    from sanic.blueprints.blueprint import Blueprint
    from sanic.response import json

    bp = Blueprint(__name__)
    endpoint = Endpoint('some')
    route = Route(endpoint, bp)
    bp.add_route(route, '/')

    future_exception = FutureException(lambda x: json({}), None)
    bp._future_exceptions.add(future_exception)

    def test_function():
        pass

    try:
        bp._apply_exception_handler(future_exception)
    except TypeError:
        pass
    else:
        assert False

# Generated at 2022-06-14 07:29:07.741552
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        pass
    test = A()
    @test.exception(IOError)
    def handle_exception(req, exc):
        pass
    assert (handle_exception, (IOError,)) in test._future_exceptions

# Generated at 2022-06-14 07:29:14.884904
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.blueprints import BluePrint
    from sanic.exceptions import _Exception

    class TestClass(ExceptionMixin, BluePrint):
        def _apply_exception_handler(self, handler : FutureException):
            pass

        def _prepare(self, app : Sanic, options: dict):
            super()._prepare(app, options)

    test_class = TestClass("test_class")

# Generated at 2022-06-14 07:29:24.916971
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Arrange
    error_msg = "A test exception"

    class TestException(Exception):
        """A test exception"""
        def __init__(self):
            super().__init__(error_msg)

    class TestExceptionMixin:
        def __init__(self, *args, **kwargs):
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler):
            nonlocal exception_handler_called
            exception_handler_called = True

    from unittest.mock import Mock
    from unittest.mock import patch

    with patch('sanic.blueprints.base.FutureException') as mock_future_exception:
        exception_mixin = TestExceptionMixin()

        # Act
        handler = Mock()
        exception_handler_called = False
        exception

# Generated at 2022-06-14 07:29:36.942554
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    def test_exception_handler(*args, **kwargs):
        pass
    # Create a ExceptionMixin object
    test_mixin = ExceptionMixin()
    # Create a Blueprint object which inherit from ExceptionMixin
    test_blueprint = Blueprint('test_bp', url_prefix='/test')
    # Test decorator
    method = test_mixin.exception(test_exception_handler)
    # Test decorator with parameter: apply
    method = test_mixin.exception(test_exception_handler, apply=False)
    # Test decorator with parameter: exceptions
    method = test_mixin.exception(
        test_exception_handler,
        AttributeError,
        IndexError,
        apply=False)
    # Test decorator with parameter: exceptions and handler

# Generated at 2022-06-14 07:29:48.734818
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
        :param args:
        :param kwargs:
        :return:
    """
    class A(ExceptionMixin):
        def __init__(self):
            self.called=False
            self.exc_type: Type[Exception] = None

        def _apply_exception_handler(self, handler: Exception) -> None:
            self.called = True
            self.exc_type = handler.exceptions[0]

    e = A()
    # unit test for function decorator of ExceptionMixin.exception()
    def handler(request, exception):
        pass
    # unit test for ExceptionMixin.exception(**kwargs)
    e.exception(ValueError)(handler)
    e.exception(ValueError, apply=True)(handler)
    assert e.called is True
    # unit test for

# Generated at 2022-06-14 07:29:57.422912
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class test_exception:
        def __init__(self, type_exception):
            self.type_exception = type_exception

    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    exception_mixin = TestExceptionMixin()

    # Test exception(tuple)
    @exception_mixin.exception(ValueError)
    def handle_value_error(request, exception):
        pass

    assert len(exception_mixin._future_exceptions) == 1
    assert type(exception_mixin._future_exceptions.pop()) == test_exception
    assert exception_mixin._future_exceptions == set()
    #

# Generated at 2022-06-14 07:30:09.822545
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinBaseClass:
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

    class TestExceptionMixinException(ExceptionMixinBaseClass):
        def _apply_exception_handler(self, handler: FutureException):
            return

    test_exception_mixin_class = TestExceptionMixinException()
    exceptions_list = [Exception, FutureWarning, PermissionError]
    exceptions_tuple = tuple(exceptions_list)

    def test_handler_1(request, exception):
        return request, exception,

    def test_handler_2(request, exception):
        return request, exception,


# Generated at 2022-06-14 07:30:25.796012
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.exceptions import future_exceptions
    from sanic.exceptions import InvalidUsage, NotFound

    future_exceptions.clear()

    class MyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            future_exceptions.add(handler)

    exception_mixin = MyExceptionMixin()

    @exception_mixin.exception([InvalidUsage, NotFound])
    def handler(*args, **kwargs):
        return {'code': args[0].status_code,
                'message': args[0].status_code}

    @exception_mixin.exception([IndexError])
    def handler2(*args, **kwargs):
        return {'code': args[0].status_code,
                'message': args[0].status_code}

# Generated at 2022-06-14 07:30:26.900234
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass


# Generated at 2022-06-14 07:30:30.437498
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    c = ExceptionMixin()
    assert c._future_exceptions == set()
    c.exception('Exception')(lambda: None)
    assert len(c._future_exceptions) == 1

# Generated at 2022-06-14 07:30:42.658144
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.handlers import ErrorHandler
    from sanic.blueprints import Blueprint
    from sanic.request import Request
    from sanic.response import HTTPResponse
    import asyncio
    
    blueprint = Blueprint('test_blueprint')
    blueprint.exception(IndexError)(lambda request, exception: 'index')
    blueprint.exception(Exception, apply = False)(lambda request, exception: 'normal')
    
    @blueprint.exception(ValueError)
    def value_error(request, exception):
        return 'value'
    @blueprint.exception(TypeError)
    def type_error(request, exception):
        return 'type'
    
    @blueprint.route('/test')
    def test(request):
        raise TypeError
    
    loop = asyncio.new_event_loop()

# Generated at 2022-06-14 07:30:47.968643
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Class(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

    @Class.exception(ValueError)
    def handler():
        pass

    assert len(Class._future_exceptions) == 1

# Generated at 2022-06-14 07:30:53.658020
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        pass
    myExcepMixin = MyExceptionMixin()
    exception = myExcepMixin.exception([Exception])
    def handler(request, exception):
        pass
    handler = exception(handler)
    assert handler in myExcepMixin._future_exceptions

# Generated at 2022-06-14 07:31:00.882066
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MockSanic:
        def exception(self, *args, **kwargs):
            return "exception"
    mock_sanic = MockSanic()
    class MockSanicBlueprint(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            pass

        @staticmethod
        def _apply_exception_handler(handler):
            return True
    mock_sanicbp = MockSanicBlueprint(mock_sanic, "test_blueprint")
    class MockException():
        pass
    mock_exception = MockException()
    assert mock_sanicbp.exception(mock_exception) == "exception"


# Generated at 2022-06-14 07:31:04.517738
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(ZeroDivisionError)
    def my_handler(request, exception):
        print("Received exception! %s" % exception)

    assert callable(my_handler) is True

# Generated at 2022-06-14 07:31:10.779075
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    blueprint = Blueprint()
    @blueprint.exception(Exception)
    def global_exception_handler():
        pass
    assert len(blueprint._future_exceptions) == 1

# Generated at 2022-06-14 07:31:21.280588
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinMock(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)
            self.exception_called = False

        def _apply_exception_handler(self, handler: FutureException):
            self.exception_called = True
            self._future_exceptions.add(handler)

    def handler(exception):
        return exception

    mixinMock = ExceptionMixinMock()
    mixinMock.exception(Exception)(handler)

    assert(mixinMock.exception_called)
    assert(handler in mixinMock._future_exceptions)

# Generated at 2022-06-14 07:31:42.228845
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprint import Blueprint
    import types

    bp = Blueprint('')
    assert isinstance(bp, ExceptionMixin)
    assert len(bp._future_exceptions) == 0

    def expected_handler(*args, **kwargs):
        pass

    decorator_handler = bp.exception(Exception)(expected_handler)
    assert expected_handler == decorator_handler
    assert len(bp._future_exceptions) == 1
    first_future_exception = list(bp._future_exceptions)[0]
    assert first_future_exception.handler == expected_handler
    assert first_future_exception.exceptions == (Exception,)
    assert isinstance(first_future_exception.exceptions, tuple)
    assert isinstance(first_future_exception.handler, types.FunctionType)

# Generated at 2022-06-14 07:31:48.022178
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    a = A()
    print(a.exception(IOError)(handler=1))
    print(a.exception([IOError])(handler=1))

test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:31:57.137396
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import pytest
    from sanic.exceptions import ServerError

    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()
        
        def _apply_exception_handler(self, handler: FutureException):
            pass

    obj = TestExceptionMixin()
    @obj.exception(ServerError)
    def handler(request, exception):
        pass

    assert len(obj._future_exceptions) == 1
    assert obj._future_exceptions.pop().handler == handler

# Generated at 2022-06-14 07:32:07.678237
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyClass(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
            super.__init__()
    # create a obj without param
    obj = MyClass()
    # create an exception handler for the obj
    def handler(*args, **kwargs):
        print("Hello World")
    # make the exception handler a global exception handler for obj
    obj.exception(NameError)(handler)
    # assert
    assert len(obj._future_exceptions) == 1
    assert obj._future_exceptions == {FutureException(handler, (NameError,))}
    # create another exception handler for the obj
    def han(*args, **kwargs):
        print("Goodbye World")

# Generated at 2022-06-14 07:32:17.748073
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Class(ExceptionMixin):
        # The dummy method _apply_exception_handler is required to prevent the
        # test to throw an exception due to the method being abstract.
        def _apply_exception_handler(self, handler: FutureException):
            return NotImplementedError

    errors_list = [TypeError]
    handler = lambda x: None
    futures_exception = FutureException(handler, errors_list)
    c = Class()

    @c.exception(*errors_list)
    def test_handler(*args, **kwargs):
        return None

    assert c._future_exceptions.pop() == futures_exception

# Generated at 2022-06-14 07:32:30.482176
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.response import json
    from unittest.mock import patch

    # For testing the method
    class Sanic(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            ExceptionMixin.__init__(self, *args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    # Mock out the logging functionality
    with patch('logging.Logger.exception') as mock_logger:
        sanic = Sanic()

        @sanic.exception(Exception)
        def handler_001(request, exception):
            return json({}, 500)

        @sanic.exception(Exception)
        def handler_002(request, exception):
            return json({}, 500)


# Generated at 2022-06-14 07:32:31.085244
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:32:32.803485
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    a = ExceptionMixin()
    assert a


# Generated at 2022-06-14 07:32:36.105675
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Given
    ExceptionMixin_class = ExceptionMixin()
    # Then
    assert ExceptionMixin_class is not None

# Generated at 2022-06-14 07:32:38.179577
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    result = ExceptionMixin().exception(10)
    assert callable(result)



# Generated at 2022-06-14 07:33:06.909006
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from unittest.mock import MagicMock

    class Blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    blueprint_mock = Blueprint()
    def handler_mock():
        return None

    @blueprint_mock.exception()
    def exception_mock():
        return None

    mock = MagicMock()
    blueprint_mock._apply_exception_handler = mock
    blueprint_mock.exception(ValueError, apply=False)()
    assert len(blueprint_mock._future_exceptions) == 1
    blueprint_mock.exception(ValueError, apply=False)()
    assert len(blueprint_mock._future_exceptions) == 1
    blueprint_mock.exception(ValueError, apply=True)

# Generated at 2022-06-14 07:33:08.173036
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # TODO
    pass

# Generated at 2022-06-14 07:33:15.897466
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    blueprint = Blueprint('test')
    
    @blueprint.exception(Exception)
    def handler(request, exception):
        pass
    
    def handler2(request, exception):
        pass
    blueprint.exception(Exception, apply=False)(handler2)
    
    assert len(blueprint._future_exceptions) == 2
    
    

# Generated at 2022-06-14 07:33:24.987073
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic import Blueprint
    app = Blueprint.group(app=Sanic('test_exception_mixin'))
    @app.exception(Exception, apply=True)
    def exception(request: Request, exception: Exception):
        return json({"exception": "Found"})
    @app.exception([Exception], apply=True)
    def exception(request: Request, exception: Exception):
        return json({"exception": "Found"})
    @app.exception(KeyError)
    def key_error(request: Request, exception: KeyError):
        return json({"exception": "Found"})

# Generated at 2022-06-14 07:33:34.040831
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Bp(ExceptionMixin):
        def __init__(self):
            self._future_exceptions = set()
            self.exception_handler = None

        def _apply_exception_handler(self, handler: FutureException):
            self.exception_handler = handler

    bp = Bp()

    @bp.exception(Exception)
    def exception_handler(request, exception):
        pass

    assert bp.exception_handler == FutureException(exception_handler, (Exception,))

# Generated at 2022-06-14 07:33:41.237728
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def some_function():
        print('execution of some_function()')

    class MockExceptionMixin(ExceptionMixin):
        def __init__(self):
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            handler.handler()

    exception_mixin = MockExceptionMixin()
    exception_mixin.exception(Exception)(some_function)()



# Generated at 2022-06-14 07:33:49.496504
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        pass

    exception_mixin_test = ExceptionMixinTest()
    @exception_mixin_test.exception()
    def _apply_exception_handler(self):
        raise NotImplementedError  # noqa

    @exception_mixin_test.exception()
    def _apply_exception_handler2(self):
        return 1, 2, 3

    assert len(exception_mixin_test._future_exceptions) == 2

# Generated at 2022-06-14 07:34:00.156268
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

        def __init__(self):
            super().__init__()
            self.a = 0

    def exception1(request, exception):
        return request

    def exception2(request, exception):
        return request

    @ExceptionMixinTest.exception(Exception)
    def exception3(request, exception):
        pass

    @ExceptionMixinTest.exception(KeyError)
    def exception4(request, exception):
        pass

    @ExceptionMixinTest.exception(ValueError)
    def exception5(request, exception):
        pass


    @ExceptionMixinTest.exception(IndexError)
    def exception6(request, exception):
        pass

    exp1 = ExceptionMix

# Generated at 2022-06-14 07:34:11.324014
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    from unittest.mock import Mock, patch
    from sanic.models.blueprints import Blueprint

    blueprint = Blueprint(__name__, url_prefix='/test')

    @blueprint.exception(ValueError)
    def error_handler(request, exception):
        return request, exception

    assert isinstance(blueprint._future_exceptions, set)

    assert blueprint._future_exceptions == {
        FutureException(error_handler, (ValueError,))
    }

    blueprint._apply_exception_handler = Mock()
    blueprint.exception(ValueError)(Mock())

    blueprint._apply_exception_handler.assert_not_called()

    blueprint.exception(ValueError, apply=False)(Mock())
    blueprint._apply_exception_handler.assert_not_called()

   

# Generated at 2022-06-14 07:34:15.123053
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    ExceptionExpected = Exception
    @ExceptionMixin.exception(ExceptionExpected)
    def handle_exception(request, exception):
        return text('Exception handler')

    assert isinstance(handle_exception, types.FunctionType)
    assert handle_exception.__name__ == 'handle_exception'
    assert handle_exception.__qualname__ == 'handle_exception'

# Generated at 2022-06-14 07:34:47.410154
# Unit test for method exception of class ExceptionMixin

# Generated at 2022-06-14 07:34:56.380268
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

    test = TestExceptionMixin()
    @test.exception(None)
    def test_handler():
        pass

    future_exception = FutureException(test_handler, (None,))

    assert len(test._future_exceptions) == 1
    assert tuple(test._future_exceptions)[0] == future_exception



# Generated at 2022-06-14 07:34:59.726970
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint('')
    assert isinstance(bp.exception(Exception)(lambda x: x), types.FunctionType)

# Generated at 2022-06-14 07:35:02.746014
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class test(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_exception = test()
    @test_exception.exception()
    def test():
        pass
    assert test_exception._future_exceptions

# Generated at 2022-06-14 07:35:06.050878
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A:
        pass

    a = A()
    a.exception(Exception)(1)

    assert a._future_exceptions == {FutureException(1, (Exception,))}

# Generated at 2022-06-14 07:35:10.633612
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print("FutureException handler applied")

    a = A()
    a.exception(ValueError, ValueError)(ValueError)

# Generated at 2022-06-14 07:35:19.843482
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Foo(ExceptionMixin):
        pass
    
    # test case
    foo = Foo()
    def bar():
        print('bar')
    foo.exception(ValueError)(bar)
    assert len(foo._future_exceptions) == 1
    assert type(list(foo._future_exceptions)[0]) == FutureException
    assert list(foo._future_exceptions)[0].handler == bar
    assert list(foo._future_exceptions)[0].exceptions == (ValueError,)
    assert list(foo._future_exceptions)[0].args == ()

# Generated at 2022-06-14 07:35:27.286625
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            print(handler)

        def test(self, *args):
            print(*args)
            pass

    test = TestExceptionMixin()
    test.exception([Exception])(test.test)('a', 'b')

test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:35:31.748640
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass

    app = Blueprint()

    @app.exception(Exception)
    def handler(request, exception):
        pass

    assert len(app._future_exceptions) == 1

# Generated at 2022-06-14 07:35:39.984039
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A:
        def __init__(self):
            self._future_exceptions = None
        def _apply_exception_handler(self, handler):
            pass
    a = A()
    @a.exception(Exception)
    def err(request, exception):
        print("Exception: {}".format(exception))
    from sanic.exceptions import ServerError
    try:
        raise ServerError("Bad Request")
    except Exception as e:
        err(None, e)

# Generated at 2022-06-14 07:36:50.617203
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.exceptions import SanicException
    import pytest

    class BlueprintMock(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    blueprint = BlueprintMock()

    @blueprint.exception([TypeError, ValueError])
    async def exception_handler(request, exception):
        return None

    assert len(blueprint._future_exceptions) == 1

    handler_to_test = blueprint._future_exceptions.pop()
    assert handler_to_test.handler == exception_handler
    assert handler_to_test.exceptions == (TypeError, ValueError)

    @blueprint.exception(SanicException)
    async def exception_handler2(request, exception):
        return None

    assert len(blueprint._future_exceptions) == 1

# Generated at 2022-06-14 07:36:58.609633
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Foo:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError
    
    obj = Foo()
    assert not hasattr(obj, '_future_exceptions')
    obj.exception('RuntimeError')(lambda x: x)
    assert obj._future_exceptions
    assert len(obj._future_exceptions) == 1
    assert (callable(obj._future_exceptions.pop().handler),)
    assert not obj._future_exceptions

# Generated at 2022-06-14 07:37:04.067437
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models import Blueprint

    blueprint = Blueprint('my_blueprint', url_prefix='/v1')
    @blueprint.exception(Exception)
    def ex_handler(request, exception):
        pass
    assert len(blueprint._future_exceptions) == 1
    assert not blueprint._apply_exception_handler(Exception)

# Generated at 2022-06-14 07:37:10.966143
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Foo(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    foo = Foo()
    assert len(foo._future_exceptions) == 0

    @foo.exception(IndexError)
    def index_error_handler(request, exception):
        pass

    assert len(foo._future_exceptions) == 1
    assert len(foo._future_exceptions.pop().exceptions) == 1


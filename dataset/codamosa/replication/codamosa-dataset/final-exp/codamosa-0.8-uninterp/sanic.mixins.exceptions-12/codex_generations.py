

# Generated at 2022-06-14 07:27:21.784007
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprint import Blueprint
    bp = Blueprint('test_bp')
    bp.add_to_app(app)
    @bp.exception(ValueError)
    def exception_handler_1(request, exception):
        return exception
    @bp.exception([ValueError, ZeroDivisionError])
    def exception_handler_2(request, exception):
        return exception
    @bp.exception(ValueError, apply=False)
    def exception_handler_3(request, exception):
        return exception
    assert exception_handler_1(None, ValueError) == ValueError
    assert exception_handler_2(None, ValueError) == ValueError
    assert exception_handler_2(None, ZeroDivisionError) == ZeroDivisionError



# Generated at 2022-06-14 07:27:30.873189
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from unittest.mock import patch
    from sanic.models.blueprint import Blueprint
    blueprint = Blueprint(__name__)

    @blueprint.exception(Exception)
    def handler():
        pass

    assert len(blueprint._future_exceptions) == 1
    assert isinstance(blueprint._future_exceptions.pop(), FutureException)

    # Test apply parameter
    with patch.object(blueprint, '_apply_exception_handler') as handler:
        blueprint.exception(Exception, apply=False)
        assert not handler.called

    # Test passing a list of exceptions
    with patch.object(blueprint, '_apply_exception_handler'):
        @blueprint.exception([Exception])
        def handler():
            pass

# Generated at 2022-06-14 07:27:47.478442
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Pre-conditions
    from sanic.blueprints import Blueprint
    class ExTest(Exception):
        pass

    def custom_handler(request, exception):
        return request.json

    bp = Blueprint("test", url_prefix="/test")

    # Testing
    # Normal case
    @bp.exception(TypeError)
    def handler1(request, exception):
        return request.json

    assert isinstance(handler1, FutureException) == True
    # Abnormal case
    @bp.exception([ExTest, TypeError])
    def handler2(request, exception):
        return request.json

    assert isinstance(handler2, FutureException) == True
    #

# Generated at 2022-06-14 07:27:49.976529
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    routes = Blueprint.routes + ['exception']
    assert 'exception' in routes

# Generated at 2022-06-14 07:27:54.048775
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    m = Blueprint("m", url_prefix="/m")
    m1 = ExceptionMixin("m1")
    m1.exception("error")
    print(m1._future_exceptions)

# Generated at 2022-06-14 07:28:02.230339
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ClassTestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            class TestClass:
                def test_exception(self, handler: FutureException):
                    assert handler == handler

            class_test = TestClass()
            class_test.test_exception(handler)

    class_test_exception_mixin = ClassTestExceptionMixin()

    class_test_exception_mixin.exception(ValueError)(lambda r, e: None)

# Generated at 2022-06-14 07:28:09.871304
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class B(ExceptionMixin):
        def __init__(self):
            self.a = 1
        def _apply_exception_handler(self, handler):
            pass
    m = B()
    assert m.a == 1
    def test_exception_handler():
        return 1
    m.exception(Exception)(test_exception_handler)
    assert len(m._future_exceptions) == 1


if __name__ == '__main__':
    test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:28:16.799985
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    app = Blueprint(__name__, url_prefix="/")

    class MyException(Exception):
        pass

    @app.exception(Exception, MyException, apply=False)
    def handler(request, exception):
        return "no route exception handler"

    assert(issubclass(handler.exceptions[0], Exception))
    assert(issubclass(handler.exceptions[1], MyException))
    assert(handler.function == handler)
    assert(handler.apply is False)

# Generated at 2022-06-14 07:28:26.964445
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    exception_mixin = TestExceptionMixin()
    @exception_mixin.exception(ValueError)
    def test_handler(request, exception):
        pass

    assert len(exception_mixin._future_exceptions) == 1
    future_exception = exception_mixin._future_exceptions.pop()
    assert future_exception.handler == test_handler
    assert future_exception.exception_types[0] == ValueError

# Generated at 2022-06-14 07:28:36.790045
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    future_exceptions = set()
    exception_mixin = ExceptionMixin()
    exception_mixin._future_exceptions = future_exceptions
    exception_mixin._apply_exception_handler = MagicMock(return_value=True)

    @exception_mixin.exception(Exception)
    def test_exception_handler(request, exception):
        pass

    assert len(future_exceptions) == 1
    assert len(exception_mixin._future_exceptions) == 1
    assert exception_mixin._apply_exception_handler.called
    assert exception_mixin._apply_exception_handler.call_count == 1

# Generated at 2022-06-14 07:28:43.969355
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint("test_bp")
    bp.exception(ZeroDivisionError)(lambda req, err: "Computer says no")
    assert bp._future_exceptions


# Generated at 2022-06-14 07:28:49.020573
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyClass(ExceptionMixin):
        @_exception
        def handler():
            pass

    o = MyClass()
    o._future_exceptions = {
        FutureException(handler, (KeyError,))
    }
    assert o._future_exceptions == FutureException.get(KeyError)

# Generated at 2022-06-14 07:29:00.636273
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            return handler
    
    actual = blueprint()

    @actual.exception(Exception, apply=False)
    def handler(request, exception):
        return True

    @actual.exception(Exception, apply=True)
    def handler(request, exception):
        return True
    
    assert len(actual._future_exceptions) == 2
    assert all(isinstance(i, FutureException) for i in actual._future_exceptions)
    for fe in actual._future_exceptions:
        assert fe.handler(None, None) == True

test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:29:10.961688
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Test(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    test = Test()
    @test.exception(Exception)
    def handler1():
        pass
    @test.exception([Exception])
    def handler2():
        pass
    @test.exception(Exception, apply = False)
    def handler3():
        pass
    assert len(test._future_exceptions) == 3
    assert handler1 in test._future_exceptions
    assert handler2 in test._future_exceptions
    assert handler3 in test._future_exceptions

# Generated at 2022-06-14 07:29:13.784075
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from sanic.models.handlers import RouteHandler



# Generated at 2022-06-14 07:29:24.227479
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.exceptions import RequestTimeout, ServerError

    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    def handler(*args, **kwargs):
        pass

    app = Sanic(__name__)
    app.blueprint(TestExceptionMixin())

    @app.exception(RequestTimeout)
    def handle_request_timeout(request, exception):
        pass

    assert len(app.error_handler.keys()) == 0

    app.blueprint(TestExceptionMixin())
    app.blueprint(TestExceptionMixin()).exception(
        RequestTimeout, ServerError, apply=True
    )(handler)

    assert len(app.error_handler.keys()) == 2
    assert Request

# Generated at 2022-06-14 07:29:32.205966
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # setup

    # parametrize
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_exception_mixin = TestExceptionMixin()

    # return
    exception_handler = test_exception_mixin.exception
    assert callable(exception_handler)
    assert len(test_exception_mixin._future_exceptions) == 0

    # execute
    decorated_handler = exception_handler(Exception)(lambda x: x)

    # assert
    assert callable(decorated_handler)
    assert len(test_exception_mixin._future_exceptions) == 1

    # teardown

# Generated at 2022-06-14 07:29:35.161812
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        pass

    TestExceptionMixin()
    TestExceptionMixin().exception(Exception)

# Generated at 2022-06-14 07:29:44.924944
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.__exception_applied = False

        def _apply_exception_handler(self, handler):
            self.__exception_applied = True

        @property
        def exception_applied(self):
            return self.__exception_applied

    test_instance = ExceptionMixinTest()

    @test_instance.exception(apply=False)
    def exception_handler(request, exception):
        pass

    assert not test_instance.exception_applied

# Generated at 2022-06-14 07:29:48.434024
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(Exception, apply=True)
    def exception_handler(request, exception):
        return "test_exception_handler"
    print(exception_handler)

# Generated at 2022-06-14 07:29:57.404360
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(ZeroDivisionError, apply=True)
    def gen_exception_handler(request, e):
        pass

    assert gen_exception_handler is not None
    assert gen_exception_handler.handler is not None
    assert gen_exception_handler.kwargs is not None

# Generated at 2022-06-14 07:30:04.777090
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import pytest  # type: ignore
    from sanic.blueprints import Blueprint
    from sanic.exceptions import InvalidUsage

    bp = Blueprint('exception_mixin', url_prefix='exception_mixin')
    assert bp._future_exceptions == set()
    assert bp.exception(InvalidUsage)
    assert len(bp._future_exceptions) == 1
    assert isinstance(bp._future_exceptions, set)

# Generated at 2022-06-14 07:30:11.785340
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    # Create a blueprint object
    blueprint = Blueprint('Blueprint', url_prefix='/test')

    # Create a handler function that can be decorated by blueprint
    def decorated_func():
        pass

    # Decorate the handler function
    decorated_func = blueprint.exception(Exception)(decorated_func)

    # Check if the handler function is decorated
    assert hasattr(
        decorated_func, 'exceptions') and decorated_func.exceptions


# Generated at 2022-06-14 07:30:24.233401
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.views import HTTPMethodView

    from sanic.middleware.exception_handler import add_exception_handler

    @add_exception_handler(ValueError)
    def handler(request, exception):
        status_code = 500
        return response.text(str(exception), status_code,
                             headers={'X-Theme': 'Mint'})

    class MyView(HTTPMethodView):
        def get(self, request):
            raise ValueError('Something is wrong.')

    blueprint = Blueprint('exceptions')
    blueprint.add_route(MyView.as_view(), '/')

    app = Sanic(__name__)
    app.blueprint(blueprint)

    request, response = app.test_client.get('/')

# Generated at 2022-06-14 07:30:36.251830
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.views import HTTPMethodView

    class HTTPMethodViewSubClass(HTTPMethodView):
        def __init__(self):
            pass

    view_cls = HTTPMethodViewSubClass()
    exception_mixin = ExceptionMixin()

    @exception_mixin.exception(Exception)
    def handler():
        pass
    handler()

    assert len(exception_mixin._future_exceptions) == 1
    assert not exception_mixin._future_exceptions[0].view_func
    assert exception_mixin._future_exceptions[0].handler == handler

    @exception_mixin.exception(Exception, apply=False)
    def handler_not_apply():
        pass
    handler_not_apply()


# Generated at 2022-06-14 07:30:40.291931
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    def exception_decorator(handler):
        return handler

    my_exception_mixin = MyExceptionMixin()
    assert my_exception_mixin.exception() == exception_decorator

# Generated at 2022-06-14 07:30:40.905044
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True == True

# Generated at 2022-06-14 07:30:54.399774
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from unittest import mock
    from unittest.mock import MagicMock
    from sanic.blueprints import Blueprint
    blueprint = Blueprint('test_ExceptionMixin_exception', url_prefix='test_ExceptionMixin_exception')

    def mock_apply_exception_handler(handler):
        pass

    blueprint._apply_exception_handler = mock_apply_exception_handler
    blueprint.add_route = mock.MagicMock()

    # this is a method
    @blueprint.exception(Exception, apply=True)
    def http_exception_handler(request, exception):
        raise Exception

    assert len(blueprint._future_exceptions) == 1


# Generated at 2022-06-14 07:31:02.696997
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            super(TestExceptionMixin, self).__init__()
            self.applied = False

        def _apply_exception_handler(self, handler: FutureException):
            self.applied = True
            assert handler

        def test1(self):
            assert self.applied

    t = TestExceptionMixin()
    @t.exception(TypeError)
    def handler(request, exception): pass

    @t.exception(Exception)
    def handler(request, exception): pass

    t.test1()

    # Now test without applying
    t.applied = False
    @t.exception(TypeError, ValueError, apply=False)
    def handler(request, exception): pass
    assert not t.applied

# Generated at 2022-06-14 07:31:06.400853
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.models.exception_handling import ExceptionHandler

    exception_mixin = ExceptionMixin()

    @exception_mixin.exception()
    def exception_handler(request, exception):
        pass

    assert len(exception_mixin._future_exceptions) == 1
    exception_mixin._apply_exception_handler(
        exception_mixin._future_exceptions.pop()
    )
    exception_handler()

# Generated at 2022-06-14 07:31:21.093706
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    class MyBP(ExceptionMixin, Blueprint):
        pass
    bp = MyBP('test', url_prefix='test')
    @bp.exception(Exception)
    def myexcepthandler(request, exception):
        return exception
    assert myexcepthandler(None, Exception('test error')) == Exception('test error')


# Generated at 2022-06-14 07:31:24.823317
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert exception(AssertionError,apply=True)(my_handler)
    assert not exception(AssertionError,Apply=True)(my_handler)


# Generated at 2022-06-14 07:31:32.057660
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinImpl(ExceptionMixin):
        def  _apply_exception_handler(self, handler: FutureException):
            return '_apply_exception_handler'

    exc_mixin = ExceptionMixinImpl()

    def expected_result():
        return 'Exception handler'

    decorator = exc_mixin.exception(Exception)
    handler = decorator(expected_result)
    assert expected_result == handler
    assert exc_mixin._future_exceptions == {FutureException(expected_result, (Exception,))}



# Generated at 2022-06-14 07:31:44.104250
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class User(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(User, self).__init__(*args, **kwargs)

        @staticmethod
        def _apply_exception_handler(handler: FutureException) -> None:
            pass

    user = User()

    # testing method exception
    @user.exception(RuntimeError, apply=False)
    def handle_user_exception(request, exception):
        pass

    assert (type(handle_user_exception) == function)
    assert (type(user._future_exceptions) == set)
    assert (type(user._future_exceptions.pop()) == FutureException)

# Generated at 2022-06-14 07:31:47.347290
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(self,*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError
    a = A()
    assert a._future_exceptions is not None

# Generated at 2022-06-14 07:31:55.460315
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestClass(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            return handler

    @TestClass.exception(Exception)
    def callback(request, exception):
        pass

    model = TestClass()
    assert len(model._future_exceptions) == 1



# Generated at 2022-06-14 07:32:06.996027
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class bp(ExceptionMixin):
        def __init__(self):
            super().__init__()
    # func exception(self, *exceptions, apply=True):
    #     """
    #     This method enables the process of creating a global exception
    #     handler for the current blueprint under question.
    #
    #     :param args: List of Python exceptions to be caught by the handler
    #     :param kwargs: Additional optional arguments to be passed to the
    #         exception handler
    #
    #     :return a decorated method to handle global exceptions for any
    #         route registered under this blueprint.
    #     """
    @bp.exception(ValueError, NameError)
    def handler(request, exception):
        return

    assert len(bp._future_exceptions) == 1

# Generated at 2022-06-14 07:32:13.002847
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    bp = Blueprint('a', 'b', '/c')
    def handler():
        return 1

    bp.exception(handler)
    assert len(bp._future_exceptions) == 1
    f = bp._future_exceptions.pop()
    assert isinstance(f, FutureException) and len(f._exceptions) == 1
    assert f._exceptions[0] is Exception



# Generated at 2022-06-14 07:32:21.633531
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    @Blueprint.exception()
    def handler(*args, **kwargs):
        pass

    assert Blueprint.exception is ExceptionMixin.exception, \
        "Fail to overwrite the method exception!"

    # unit test for ExceptionMixin.exception with apply=True
    blueprint = Blueprint(__name__)
    blueprint.exception(apply=True)(handler)
    assert blueprint._future_exceptions is not None, \
    	"Fail to build the set _future_exceptions!"
    assert len(blueprint._future_exceptions) == 1, \
    	"Fail to build the set _future_exceptions with proper length!"
    assert list(blueprint._future_exceptions)[0].handler is handler, \
    	"Fail to build the set _future_exceptions with proper element!"

# Generated at 2022-06-14 07:32:22.348431
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:32:48.070541
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Tests the decorator exception method of class ExceptionMixin
    class MyClass(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    my_object = MyClass()

    # Test the correct behavior of the decorator
    @my_object.exception(ValueError)
    def my_handler(request, exception):
        pass

    assert len(my_object._future_exceptions) == 1
    assert my_object._future_exceptions == {FutureException(my_handler, (ValueError,))}  # noqa

    # Test the return value of the decorator

# Generated at 2022-06-14 07:32:56.118815
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            return

    @Blueprint.exception(list(range(5)))
    def test_handler():
        pass

    assert len(Blueprint._future_exceptions) == 1

# Generated at 2022-06-14 07:33:08.335894
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprint import Blueprint
    from sanic.constants import HTTP_METHODS
    from sanic.models.futures import FutureException

    # Test inheritance of mixin class
    bp = Blueprint(__name__, url_prefix='tests')
    assert isinstance(bp, ExceptionMixin)

    # Test exception attribute
    assert isinstance(bp._future_exceptions, set)

    @bp.exception(ValueError)
    def handler(request, exception):
        return text('Oops!', 500)

    assert len(bp._future_exceptions) == 1
    future_exception = list(bp._future_exceptions)[0]
    assert isinstance(future_exception, FutureException)
    assert future_exception.handler is handler
    assert future_exception.exceptions == (ValueError,)



# Generated at 2022-06-14 07:33:21.776190
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest:
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
    class FutureExceptionTest(Exception):
        pass
    class FutureExceptionTest1(Exception):
        pass
    class FutureExceptionTest2(Exception):
        pass
    class FutureExceptionTest3(Exception):
        pass
    args={}
    handler=lambda *args, **kwargs: str(args)
    my_new_class=ExceptionMixinTest()
    my_new_class.exception(FutureExceptionTest)(handler)('hello', 'world')
    my_new_class.exception(FutureExceptionTest1, FutureExceptionTest2)(handler)('hello', 'world')

# Generated at 2022-06-14 07:33:28.987920
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MockExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(MockExceptionMixin, self).__init__(*args, **kwargs)
            self.future_exceptions_called = False

        def _apply_exception_handler(self, handler: FutureException):
            self.future_exceptions_called = True

    mixin = MockExceptionMixin()

    @mixin.exception(AssertionError, Exception)
    def handler(request, exception):
        pass

    assert isinstance(handler, types.FunctionType)
    assert isinstance(mixin.future_exceptions_called, bool)

# Generated at 2022-06-14 07:33:31.069371
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, future_exception):
            pass
    mixin = MyExceptionMixin()
    mixin.exception(Exception, apply=True)(handle_exception)
    assert len(mixin._future_exceptions) == 1
    assert isinstance(mixin._future_exceptions.pop(), FutureException)


# Generated at 2022-06-14 07:33:42.185733
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    class ExceptionMixinBlueprint(Blueprint, ExceptionMixin):
        def __init__(self, name):
            Blueprint.__init__(self, name, url_prefix='test')
            ExceptionMixin.__init__(self)
            self._apply_exception_handler = self._mock_apply_exception_handler

        def _mock_apply_exception_handler(self, handler: FutureException):
            pass

    blueprint = ExceptionMixinBlueprint('test')
    @blueprint.exception(Exception)
    def error_handler(request, exception):
        print("Exception raised: " + str(exception))

    assert len(blueprint._future_exceptions) == 1

# Generated at 2022-06-14 07:33:48.340911
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    try:
        bp = TestExceptionMixin()
        @bp.exception(IndexError, apply=False)
        def exception(request, exception):
            return 'exception'
    except:
        return False
    return True


# Generated at 2022-06-14 07:33:59.634957
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import pytest
    from sanic import Sanic
    from sanic.exceptions import ServerError
    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException

    app = Sanic(__name__)
    bp = Blueprint('test_bp', url_prefix='test_bp')

    @bp.exception(ServerError)
    def handler(request, exception):
        pass

    @bp.listener('before_server_start')
    def attach(app, loop):
        bp.register_exception_handler(app)
        assert len(bp._future_exceptions) == 1
        future_exception = next(iter(bp._future_exceptions))
        assert future_exception.handler == handler
        assert future_exception.exceptions == (ServerError,)
        
       

# Generated at 2022-06-14 07:34:05.867686
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint("test_bp", url_prefix="/test_bp")
    @bp.exception(ValueError, TypeError)
    @bp.exception(ZeroDivisionError)
    def handle_exception(request, exception):
        return "Exception handler executed. Exception: {}".format(exception)
    
    assert bp._future_exceptions != None
    assert len(bp._future_exceptions) == 2



# Generated at 2022-06-14 07:34:46.241371
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    app = Sanic(__name__)

    @app.exception(Exception)
    def handle_my_exception(request, exception):
        return text('Here is your exception', status=418)

    @app.blueprint.exception(Exception)
    def handle_my_exception(request, exception):
        return text('Here is your exception', status=418)

    @app.route('/exception/')
    def endpoint(request):
        raise Exception

if __name__ == '__main__':
    test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:34:50.782719
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Object(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            ExceptionMixin.__init__(self, *args, **kwargs)
    
    obj = Object()

    assert len(obj._future_exceptions) == 0

# Generated at 2022-06-14 07:34:56.222833
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            self._future_exceptions = set()
        def _apply_exception_handler(self, handler):
            print("apply_exception_handler")

    ts = TestExceptionMixin()
    ts.exception(Exception)



# Generated at 2022-06-14 07:35:08.319297
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Object_BluprintException(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    @Object_BluprintException.exception(apply=True)
    def test1(request, exception):
        return exception

    @Object_BluprintException.exception()
    def test2(request, exception):
        return exception

    @Object_BluprintException.exception(apply=False)
    def test3(request, exception):
        return exception

    @Object_BluprintException.exception(ZeroDivisionError)
    def test4(request, exception):
        return

# Generated at 2022-06-14 07:35:19.214062
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    def dummy_func_1(exc):
        return exc
    def dummy_func_2(exc):
        return exc
    test_inst = ExceptionMixin()
    dummy_func_1(ExceptionMixin().exception(apply=True, exc=IOError))
    assert test_inst._future_exceptions == {ExceptionMixin().exception(apply=True, exc=IOError)}
    dummy_func_2(ExceptionMixin().exception(apply=True, exc=[ValueError, KeyError]))

# Generated at 2022-06-14 07:35:28.547262
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.blueprints import Blueprint
    from sanic.response import HTTPResponse

    blueprint = Blueprint("test", url_prefix="/v1")
    app = Sanic("test_sanic_blueprint")

    @blueprint.exception(Exception)
    @blueprint.exception(Exception, apply=False)
    def default(exception):
        return HTTPResponse(body=exception.message, status=500)
    
    app.blueprint(blueprint)

# Generated at 2022-06-14 07:35:36.755152
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    @TestExceptionMixin.exception(KeyError)
    def generic_handler(request, exception):
        return "Found exception"

    assert generic_handler(KeyError, 1) == "Found exception"

# Generated at 2022-06-14 07:35:47.602950
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import asyncio
    from sanic import Sanic
    from sanic.response import text
    from sanic.models.futures import FutureException

    app = Sanic('ExceptionMixin')

    @app.exception(Exception)
    def exception_handler(request, exception):
        return text('An exception occurred: %s' % exception)
    
    @app.route('/1')
    async def test1(request):
        raise Exception('An exception occurred')

    @app.route('/2')
    async def test2(request):
        raise Exception('An exception occurred')

    request, response = app.test_client.get('/1')
    assert response.text == 'An exception occurred: An exception occurred'

    request, response = app.test_client.get('/2')

# Generated at 2022-06-14 07:35:53.153316
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @Blueprint.exception(IndexError)
    def handler(request, exception):
        return ""
    
    assert repr(handler) == repr(handler.__wrapped__)
    assert handler.__name__ == "handler"
    assert handler.__module__ == __name__

# Generated at 2022-06-14 07:36:06.230672
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
	class Blueprint(ExceptionMixin):
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.handler = None
			self.exceptions = None
			self.apply = None

		def _apply_exception_handler(self, handler: FutureException):
			if self.apply:
				self.handler = handler.handler
				self.exceptions = handler.exceptions

	blueprint = Blueprint()
	blueprint.exception(10)(handler=10)
	assert blueprint.handler == 10
	assert blueprint.exceptions == (10,)
	assert blueprint._future_exceptions == {FutureException(10, (10,))}
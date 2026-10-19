

# Generated at 2022-06-14 07:27:09.379926
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    global_exception_method=ExceptionMixin()
    global_exception_method._apply_exception_handler=Mock()
    global_exception_method._future_exceptions=set()
    @global_exception_method.exception([ZeroDivisionError])
    def the_handler():
        print('o')

# Generated at 2022-06-14 07:27:22.217875
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints.blueprint import Blueprint
    from sanic.models.futures import FutureException

    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    test_exceptions = [Exception]
    test_kwargs = {}
    test_apply = True
    test_handler = lambda _: None

    test_blueprint = TestExceptionMixin()

    test_blueprint.exception(test_exceptions, apply=test_apply)(test_handler)

# Generated at 2022-06-14 07:27:27.366336
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    blueprint = Blueprint('test_ExceptionMixin_exception')
    blueprint.exception(ZeroDivisionError)(lambda req, ex: 'ZeroDivisionError')

    future_exceptions = blueprint._future_exceptions

    assert future_exceptions
    assert len(future_exceptions) == 1
    assert future_exceptions.pop().handler(None, None) == 'ZeroDivisionError'

# Generated at 2022-06-14 07:27:35.096032
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self):
            super().__init__()
        def _apply_exception_handler(self, handler):
            print('exception handler is applied')
    test_obj = ExceptionMixinTest()

    # test1: call __init__
    assert test_obj._future_exceptions == set()

    # test2: call exception, with apply = True
    @test_obj.exception(Exception)
    def test_handler(request, exception):
        print('exception handler is called')
    assert test_obj._future_exceptions == {FutureException(test_handler, (Exception,))}

    # test3: call exception, with apply = False

# Generated at 2022-06-14 07:27:41.494721
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    blueprint = Blueprint("Test", url_prefix="/test")
    blueprint.exception(Exception)(lambda request, exception: "test")
    future_exception = FutureException(lambda request, exception: "test", (Exception,))
    assert future_exception in blueprint._future_exceptions

# Generated at 2022-06-14 07:27:52.871978
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint

    blueprint1 = Blueprint("test", url_prefix="/test", version=1)
    blueprint2 = Blueprint("test", url_prefix="/test", version=1)

    """
    def _apply_exception_handler(self, handler: FutureException):
        raise NotImplementedError  # noqa
        """

    @blueprint1.exception(IndexError)
    def handler(request, exception):
        pass

    @blueprint2.exception(IndexError, apply=False)
    def handler(request, exception):
        pass

    assert blueprint1._future_exceptions
    assert not blueprint2._future_exceptions



# Generated at 2022-06-14 07:27:57.942799
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException

    b = Blueprint(__name__)
    b.exception(Exception, apply=False)
    assert len(b._future_exceptions) == 1
    assert FutureException(Exception, Exception) in b._future_exceptions

# Generated at 2022-06-14 07:28:04.644468
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MockClass(ExceptionMixin):
        pass

    mockclass = MockClass()
    exception_type = "ValueError"
    @mockclass.exception(exception_type)
    def mock_exception_handler():
        pass
    assert isinstance(mock_exception_handler, types.FunctionType)
    future_exception = FutureException(mock_exception_handler, (exception_type,))
    assert future_exception in mockclass._future_exceptions

# Generated at 2022-06-14 07:28:10.847253
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    @TestExceptionMixin.exception(Exception)
    def handler(request, exception):
        pass

    expected = FutureException(handler, [Exception])
    assert TestExceptionMixin()._future_exceptions == {expected}

# Generated at 2022-06-14 07:28:14.015503
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test case 1: ExceptionMixin is implemented in all classes that
    # use this decorator, but it is not the case for the class Route
    r = Route()
    assert r.exception() is None

# Generated at 2022-06-14 07:28:20.190779
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.abstract import Blueprint
    from sanic.app import Sanic

    bp = Blueprint(__name__)
    app = Sanic()
    bp.exception(ValueError)(lambda x: 1)
    bp.exception(KeyError, apply=False)(lambda x: 1)
    assert len(bp._future_exceptions) == 2
    bp.register(app)
    assert len(bp._future_exceptions) == 0
    assert len(app._exception_handlers) == 1

# Generated at 2022-06-14 07:28:23.075252
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    blueprint = Blueprint('test')
    blueprint.exception(Exception)
    blueprint_decorator = blueprint.exception(Exception)
    blueprint_decorator(Exception)

# Generated at 2022-06-14 07:28:24.776539
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    #TODO: Implement this
    pass

# Generated at 2022-06-14 07:28:33.093157
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinSubClass(ExceptionMixin):
        """
        This is a subclass of ExceptionMixin
        """
        def _apply_exception_handler(self, handler: FutureException):
            pass

    ex_mixin_obj = ExceptionMixinSubClass()
    @ex_mixin_obj.exception(ValueError, TypeError)
    def exception_handler():
        pass
    for future_exception in ex_mixin_obj._future_exceptions:
        assert(future_exception._handler == exception_handler)

# Generated at 2022-06-14 07:28:38.460209
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # create an object of class ExceptionMixin
    exception_mixin = ExceptionMixin()

    # test case 1:
    # check if exceptions are inside the future_exceptions
    @exception_mixin.exception(Exception)
    def exception_handler(request, exception):
        pass

    assert exception_handler in exception_mixin._future_exceptions


# Generated at 2022-06-14 07:28:41.416663
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(IndexError, ValueError)
    def A(request, e):
        pass

# Generated at 2022-06-14 07:28:53.009464
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic, blueprint
    from sanic.exceptions import Forbidden

    app = Sanic(__name__)

    bp = blueprint(__name__)

    @bp.exception(Forbidden)
    async def forbidden_error_handler(request, exception):
        return "Forbidden"

    @bp.route('/')
    async def handler(request):
        return "Hello world"

    app.blueprint(bp)

    request, response = app.test_client.get('/')
    assert response.status == 200
    assert response.text == "Hello world"

    @bp.route('/forbidden')
    async def handler(request):
        raise Forbidden()

    request, response = app.test_client.get('/forbidden')
    assert response.status == 403
    assert response.text

# Generated at 2022-06-14 07:28:59.083469
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class UnitExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            ExceptionMixin.__init__(self, *args, **kwargs)

        def _apply_exception_handler(self, handler):
            print("_apply_exception_handler")

    UnitExceptionMixin()

# Generated at 2022-06-14 07:29:06.203508
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.request import Request
    from sanic.response import json, HTTPResponse

    class Bp(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super(Bp, self).__init__(*args, **kwargs)

    bp = Bp()
    assert bp._future_exceptions == set()
    assert bp.exception(ValueError, apply=True)(lambda: None)

# Generated at 2022-06-14 07:29:16.655006
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinClass(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    #Testing ExceptionMixinClass.exception
    #Test 1: normal
    try:
        bp = Blueprint('test_blueprint_1', url_prefix='/test')
        @bp.exception(ValueError, KeyError)
        def exception_handler(request, exception):
            pass
    except TypeError:
        raise TypeError('test_ExceptionMixin_exception')

    #Test 2: normal

# Generated at 2022-06-14 07:29:32.202006
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    from sanic import response
    from sanic.exceptions import NotFound

    bp = Blueprint('bp')

    def handler_404(request, exception):
        return response.text('Not Found', status=exception.status_code)
    @bp.exception(NotFound)
    def catch_404s(request, exception):
        return response.text('Not Found', status=exception.status_code)

    assert len(bp._future_exceptions) == 2

    # will only return first route
    future_exception = next(iter(bp._future_exceptions))
    assert future_exception.handler == handler_404
    assert future_exception.exceptions == (NotFound,)

    future_exception = next(iter(bp._future_exceptions))

# Generated at 2022-06-14 07:29:34.344592
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    a = ExceptionMixin()
    assert a.exception(Exception)

# Generated at 2022-06-14 07:29:42.255062
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException
    
    bp = Blueprint(name='test')
    assert len(bp._future_exceptions) == 0

    @bp.exception(Exception)
    def handler(r, err):
        return 'error', 500

    assert len(bp._future_exceptions) == 1

    # Since ex1 is a list of exceptions, it should be converted to tuple
    ex1 = [Exception, ValueError]
    expected = FutureException(handler, ex1)
    result = bp._future_exceptions.pop()
    assert result == expected
    bp._future_exceptions.add(result)

    ex2 = (Exception, ValueError)
    expected = FutureException(handler, ex2)
    result = bp._future_exceptions

# Generated at 2022-06-14 07:29:53.048683
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class TestExceptionMixin(ExceptionMixin):

        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    @TestExceptionMixin.exception("test")
    def test_exception():
        pass

    @TestExceptionMixin.exception("test")
    def test_exception_list():
        pass

    assert isinstance("test_exception", types.FunctionType)
    assert isinstance("test_exception_list", types.FunctionType)
    assert len(TestExceptionMixin()._future_exceptions) == 2

# Generated at 2022-06-14 07:30:02.159133
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blues import SanicBlue

    app = SanicBlue()

    class TestClass(ExceptionMixin):
        pass

    test_class = TestClass()

    @app.exception(Exception)
    def exception_handler(request, exception):
        return text("exception")

    @test_class.exception
    def test_exception_handler(request, exception):
        return text("exception")

    test_class._apply_exception_handler = lambda x: None

    assert(
        test_class._future_exceptions ==
        {FutureException(test_exception_handler, (Exception,))})

# Generated at 2022-06-14 07:30:06.217116
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            return

    MyExceptionMixin().exception(Exception)
    MyExceptionMixin().exception([Exception])

# Generated at 2022-06-14 07:30:19.246545
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class SanicMock(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.applied_exceptions = []

        def _apply_exception_handler(self, handler: FutureException):
            self.applied_exceptions.append(handler)

    # Will create a new blueprint
    app = SanicMock(__name__)

    # Assigning a handler for AssertionError
    @app.exception(AssertionError)
    def handler_for_AssertionError(self, request, exception):
        pass

    # Assigning a handler for ArithmeticError
    @app.exception(ArithmeticError)
    def handler_for_ArithmeticError(self, request, exception):
        pass

    # Assigning

# Generated at 2022-06-14 07:30:25.148384
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    class App(ExceptionMixin):
        def __new__(cls, *args, **kwargs):
            return App

        def _apply_exception_handler(self):
            raise NotImplementedError

    app = App()
    assert app.exception is not None

    @app.exception
    def exception_handler(request, exception):
        pass

# Generated at 2022-06-14 07:30:34.746442
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class MockExceptionMixin(ExceptionMixin):
        def __init__(self) -> None:
            super(MockExceptionMixin, self).__init__()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    exception_mixin = MockExceptionMixin()

    @exception_mixin.exception(ValueError)
    def sum_function(a, b):
        return a + b

    @exception_mixin.exception(TypeError)
    def sum_function(a, b):
        return a + b

    assert len(exception_mixin._future_exceptions) == 2

# Generated at 2022-06-14 07:30:38.850491
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_exception_mixin = ExceptionMixinTest()
    test_exception_mixin.exception(Exception)

# Generated at 2022-06-14 07:30:55.336486
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.exceptions import AppException
    from sanic.models.route import Route
    from sanic.router import Router
    from sanic.app import Sanic
    from sanic.blueprint import Blueprint

    # Create Simple Sanic App
    app = Sanic('TestApp')

    # Create Simple Sanic Blueprint
    blueprint = Blueprint('TestBlueprint')

    # Register blueprint on Sanic App
    app.blueprint(blueprint)

    # Register a sample route
    @blueprint.route('/')
    async def handler(request):
        return text('OK')

    # Register a sample exception handler
    @blueprint.exception([AppException])
    async def handler_exception(request, exception):
        return text('OK')

    # Build Router

# Generated at 2022-06-14 07:31:03.480170
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from unittest.mock import Mock
    from unittest.mock import call
    from sanic.models.futures import FutureException

    exception_mixin = ExceptionMixin()
    handler = Mock()

    result = exception_mixin.exception()(handler)
    assert handler == result

    assert call(FutureException(handler, ())) in exception_mixin._apply_exception_handler.mock_calls

# Generated at 2022-06-14 07:31:09.961075
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint:
        def __init__(self):
            self._future_exceptions: Set[FutureException] = set()
    
    Blueprint.exception = ExceptionMixin.exception
    blueprint = Blueprint()
    assert blueprint._future_exceptions == set()

    @blueprint.exception(NameError)
    def handler(request, exception):
        return True

    assert blueprint._future_exceptions != set()



# Generated at 2022-06-14 07:31:12.609186
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.views import HTTPMethodView

    class TestExceptionMixin(HTTPMethodView, ExceptionMixin):
        pass

    exception_mixin = TestExceptionMixin()

    @exception_mixin.exception
    def func():
        pass

    assert len(exception_mixin._future_exceptions) == 1

# Generated at 2022-06-14 07:31:18.670769
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    bp = Blueprint()

    @bp.exception(ValueError)
    def handler():
        pass

    assert len(bp._future_exceptions) == 1
    assert bp._future_exceptions.pop().handler == handler

# Generated at 2022-06-14 07:31:26.072451
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.response import json
    
    blueprint = Blueprint('bp')
    
    @blueprint.exception(RuntimeError)
    def handle_exception(request, exception):
        return json({"message": "Internal Server Error"}, status=500)
    
    # test if the method exception will generate a set.
    assert type(blueprint._future_exceptions) is not None

# Generated at 2022-06-14 07:31:28.847966
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    '''Test cases for ExceptionsMixin.exception'''
    # TODO
    fire = False
    assert fire == False

# Generated at 2022-06-14 07:31:42.235206
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.result = None
            self.params = None

        def _apply_exception_handler(self, handler: FutureException):
            self.params = (handler.handler, handler.exceptions)
            self.result = "success"

    a = A()
    a.exception(BaseException)(lambda: None)

# Generated at 2022-06-14 07:31:52.502091
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super(A, self).__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    obj = A()

    @obj.exception(apply=True, exceptions=(ValueError,))
    def handler(request, exception):
        return 'exception handler'

    assert len(obj._future_exceptions) == 1
    assert isinstance(obj._future_exceptions.pop(), FutureException)
    assert isinstance(obj._future_exceptions.pop(), FutureException)

    assert handler('value') == 'exception handler'

# Generated at 2022-06-14 07:31:54.293579
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    decorator = ExceptionMixin().exception()
    assert callable(decorator)

# Generated at 2022-06-14 07:32:09.851291
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    blueprint = Blueprint(name="Test", url_prefix='/handle')

    exceptions = ["Exception1", "Exception2"]
    try:
        raise Exception(*exceptions)
    except Exception as e:
        def handle_function(request, exception):
            current_app.logger.debug(exception)
            return json({'code': 400, 'message': 'Exception handled'})

        blueprint.exception(["Exception1", "Exception2"])(handle_function)

# Generated at 2022-06-14 07:32:15.985386
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Base_test(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            self.handler=handler
    test_instance=Base_test()
    @test_instance.exception
    def test_function():
        pass
    assert test_instance.handler.handler==test_function

# Generated at 2022-06-14 07:32:16.672427
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:32:29.225362
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic import Blueprint
    from sanic.models.exception import ExceptionMixin

    blueprint = Blueprint("test_bp")
    blueprint.add_exception_handler(Exception, {})
    blueprint.add_exception_handler(Exception, {})
    app = Sanic(load_env=True)
    @blueprint.exception(Exception)
    def exception_handler(request, exception):
        pass
    @blueprint.exception([Exception, ZeroDivisionError])
    def exception_handler(request, exception):
        pass
    @blueprint.exception([ZeroDivisionError])
    def exception_handler(request, exception):
        pass
    app.register_blueprint(blueprint)
    assert len(app._exception_handlers) == 5

# Generated at 2022-06-14 07:32:35.186155
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Arrange
    class SanicTest(ExceptionMixin):

        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    # Act
    sanic_test = SanicTest()
    handler = sanic_test.exception(exceptions=[HTTPException])
    handler(Exception)

    # Assert
    assert len(sanic_test._future_exceptions) == 1


# Generated at 2022-06-14 07:32:46.573511
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    import unittest.mock
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

        def dummy(self):
            return "dummy"
    test = TestExceptionMixin()
    @test.exception(ZeroDivisionError)
    def foo():
        return 1
    @test.exception(ZeroDivisionError, apply=True)
    def zoo():
        return 1
    class Test(unittest.TestCase):
        def test_exception(self):
            self.assertTrue(foo()==zoo())

# Generated at 2022-06-14 07:32:52.657106
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    '''
    Test ExceptionMixin's method exception:
    method:          exception
    test case:       no parameter
    expected result: raise NotImplementedError
    '''
    @ExceptionMixin.exception()
    def exception_handler():
        return

    try:
        exception_handler()
        assert False
    except TypeError:
        assert True


# Generated at 2022-06-14 07:32:53.516930
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:33:01.078972
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            return None

    TestExceptionMixin = TestExceptionMixin()
    @TestExceptionMixin.exception(IndexError, NameError)
    def test(request, exception):
        return None

    assert isinstance(test, types.FunctionType)

# Generated at 2022-06-14 07:33:10.988511
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class parentclass:
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
    class childclass(ExceptionMixin, parentclass):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
            
    a = childclass()

    def myhandler(request, exception):
        print("something")
        return "something"

    def mydecorator(handler):
        a._future_exceptions.add(FutureException(handler,("exception","exception2")))
        return handler

    result = mydecorator(myhandler)
    assert result

    result = a.exception("exception", "exception2")(myhandler)
   

# Generated at 2022-06-14 07:33:30.124675
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            return handler
    
    em = TestExceptionMixin()
    assert em._future_exceptions == set()
    em.exception(Exception, apply=False)
    assert em._future_exceptions == set()
    em.exception(Exception, apply=True)
    assert em._future_exceptions == set()

# Generated at 2022-06-14 07:33:35.682893
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import ServerError

    blueprint = Blueprint(__name__)
    assert len(blueprint._future_exceptions) == 0

    @blueprint.exception(ServerError)
    def server_error_handler(request, exception):
        return response.text('Internal server error')

    assert len(blueprint._future_exceptions) == 1
    future_exception = list(blueprint._future_exceptions)[0]
    assert future_exception.handler == server_error_handler
    assert len(future_exception.exceptions) == 1
    assert future_exception.exceptions[0] == ServerError

# Generated at 2022-06-14 07:33:39.045636
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class _ExceptionMixin(ExceptionMixin):

        def _apply_exception_handler(self, handler: FutureException):
            pass
    _ExceptionMixin()

# Generated at 2022-06-14 07:33:47.876537
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Test(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError   

    test = Test()
    @test.exception(Exception)
    def handler(request, exception):
        print(exception)

    try:
        raise Exception
    except Exception as e:
        for exception in test._future_exceptions:
            exception.handler({"request": "request"}, e)

# Generated at 2022-06-14 07:33:57.103006
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class TestException(Exception):
        pass

    test_exception_set = [TestException()]
    test_kwargs = {'apply': False}

    test_object = ExceptionMixin()
    test_decorator = test_object.exception(*test_exception_set, **test_kwargs)
    
    def test_handler(request, exception):
        pass

    test_decorator(test_handler)

    assert test_object._future_exceptions == set([
        FutureException(test_handler, test_exception_set)
    ])

# Generated at 2022-06-14 07:33:57.636313
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True

# Generated at 2022-06-14 07:34:02.692690
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixinException(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            return 
    test_ExceptionMixin_exception_obj=TestExceptionMixinException()
    @test_ExceptionMixin_exception_obj.exception(Exception)
    def function1(request, *args, **kwargs):
        return
    assert len(test_ExceptionMixin_exception_obj._future_exceptions) == 1

# Generated at 2022-06-14 07:34:09.840622
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    def apply_exception_handler(handler):
        return handler

    class MixinTest(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)
            self._apply_exception_handler = apply_exception_handler

    mixin = MixinTest()
    mixin.exception(IndexError, apply=False)(print)
    assert len(mixin._future_exceptions) == 1

# Generated at 2022-06-14 07:34:16.402183
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    import sanic
    class Example(ExceptionMixin):
        @ExceptionMixin.exception(Exception)
        def exception_handler(self, request, exception):
            pass
    assert isinstance(Example().exception_handler, type(ExceptionMixin.exception))
    @Example.exception(Exception)
    def exception_handler(self, request, exception):
        pass
    assert isinstance(Example().exception_handler, type(ExceptionMixin.exception))


# Generated at 2022-06-14 07:34:29.287681
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.exceptions import NotFound
    from sanic.blueprints import Blueprint, _BlueprintSetupState
    from sanic.router import RouteExists
    from sanic.request import Request

    blueprint = Blueprint('test_bp', url_prefix='/test_bp')
    app = Sanic(__name__)

    async def handler(request):
        return text('OK')

    @blueprint.exception(NotFound)
    async def test_exception(request):
        return text('')

    # Assert if Blueprint can handle NotFound exception
    app.register_blueprint(blueprint)
    assert app.has_blueprint(blueprint.name)
    assert app.is_request_stream is False
    assert app.is_websocket_enabled is False
   

# Generated at 2022-06-14 07:35:06.298589
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from unittest import mock

    class ExceptionMixinTest(ExceptionMixin):
        pass

    emt = ExceptionMixinTest()

    with mock.patch.object(ExceptionMixinTest, '_apply_exception_handler') as mock_aeh:
        emt.exception(IndexError)
        emt.exception(IndexError)
        mock_aeh.assert_called_once()

        mock_aeh.reset_mock()
        emt.exception(IndexError, True)
        emt.exception(IndexError)
        mock_aeh.assert_called_once()

        mock_aeh.reset_mock()
        emt.exception([IndexError, IndexError])
        mock_aeh.assert_called_once()



# Generated at 2022-06-14 07:35:19.548653
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Setup
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

    exception_mixin_test = ExceptionMixinTest()
    decorator1 = exception_mixin_test.exception(Exception)
    decorator2 = exception_mixin_test.exception(Exception)

    @decorator1
    def decorator1_method():
        pass

    @decorator2
    def decorator2_method():
        pass

    # Assertion
    assert len(exception_mixin_test._future_exceptions) == 2
    for exception in exception_mixin_test._future_exceptions:
        assert exception.handler == decorator1_method or exception.handler == decorator2

# Generated at 2022-06-14 07:35:32.138747
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinfor_test(ExceptionMixin):
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa
            
    def custom_handler(*args, **kwargs):
        return "custom_handler"
    
    blueprint = Blueprint(__name__)
    blueprint.exception([Exception], apply=True)(custom_handler)
    for i in blueprint._future_exceptions:
        assert callable(i._handler)
        assert i._handler() == "custom_handler"
        assert i._exceptions == (Exception,)


# Generated at 2022-06-14 07:35:45.065817
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.response import json
    from datetime import datetime

    class MyBluePrint(Blueprint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.exception([ZeroDivisionError])(self._div_by_zero_handler)
            # Add another handler for the same exception
            self.exception([ZeroDivisionError])(self._div_by_zero_handler)
            self.exception([KeyError])(self._key_error_handler)

        def _div_by_zero_handler(self, request, exception):
            return json({
                'status': 'exception',
                'exception': exception.__class__.__name__
            })


# Generated at 2022-06-14 07:35:52.148671
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from sanic.handlers import ErrorHandlers
    from sanic.response import json

    class Blueprint(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__()
            self.error_handler = ErrorHandlers()

        def _apply_exception_handler(self, handler: FutureException):
            self.error_handler.add(handler.exceptions, handler.handler)

    blueprint = Blueprint()
    blueprint.exception(Exception)(lambda request, exception: json({"TestExcHandler": str(exception)}))
    assert blueprint.error_handler[Exception](None, Exception("Test Exception")).body == \
           b'{"TestExcHandler": "Test Exception"}'



# Generated at 2022-06-14 07:35:58.961116
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint('test_bp')

    @bp.exception(ValueError)
    async def exception_handler(request, exception):
        return text("You raised a ValueError")

    assert len(bp._future_exceptions) == 1
    future_exception = bp._future_exceptions.pop()
    assert future_exception.handler == exception_handler
    assert tuple(future_exception.exceptions) == (ValueError,)

# Generated at 2022-06-14 07:36:08.458391
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            return None

    test_object = TestExceptionMixin()
    future_exception_set = (ValueError, )
    assert len(test_object._future_exceptions) == 0

    def error_handler(self):
        return None

    test_object.exception(future_exception_set)(error_handler)
    test_object.exception(future_exception_set)(error_handler)
    assert len(test_object._future_exceptions) == 2

    # test with apply=False
    test_object.exception(future_exception_set, apply=False)(error_handler)
    assert len(test_object._future_exceptions) == 3

    # test with set object


# Generated at 2022-06-14 07:36:16.899472
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from unittest.mock import Mock
    from sanic.response import json

    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            try:
                handler(Mock(), Mock())
            except ValueError as e:
                assert str(e) == 'Test exception'

    TestExceptionMixin().exception([ValueError])(
        lambda *args, **kwargs: json(str(args[1]['exception'])))()


# Generated at 2022-06-14 07:36:30.018337
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from sanic.response import json as json_response
    from sanic.response import text as text_response
    from sanic.testing import SanicTestClient
    from sanic import Sanic

    # We define a class which inherit from ExceptionMixin
    class MyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            # We mock the _apply_exception_handler function defined in the
            # ExceptionMixin class because we don't have a blueprint or a
            # router to apply the exception handler.
            pass

        # We define a route to trigger an exception
        async def trigger_exception(self, request):
            """Raise an exception"""
            raise Exception("Test exception")

    app = Sanic()
    MyException

# Generated at 2022-06-14 07:36:34.027992
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestClass(ExceptionMixin):
        def __init__(self):
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    TestClass()


# Generated at 2022-06-14 07:27:27.511726
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
        def _apply_exception_handler(self, handler: FutureException):
            self._future_exceptions.add(handler)

    @TestExceptionMixin.exception(Exception, apply=False)
    def handler1(self, request, exception):
        pass

    @TestExceptionMixin.exception(Exception, apply=True)
    def handler2(self, request, exception):
        pass

    # Test handler2
    t = TestExceptionMixin()
    assert len(t._future_exceptions) == 0

    handler2(t, Exception, Exception)
    assert len(t._future_exceptions) == 1

# Generated at 2022-06-14 07:27:34.819469
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic_openapi import doc
    
    class TestExceptionMixin(ExceptionMixin):
        @doc.produces({"code": doc.Integer("error code"), "message": doc.String("message")})
        def test_mixin_function(*args, **kwargs):
            """
            Fake method for testing ExceptionMixin
            """
            return {"code": 200, "message": "OK"}
    
    @TestExceptionMixin.exception(ZeroDivisionError)
    def test_exception_handler(request: Request, exception: ZeroDivisionError):
        """
        Fake test exception handler for testing ExceptionMixin
        """
        return text(str(exception), 500)

    assert len(TestExceptionMixin._future_exceptions) == 1

# Generated at 2022-06-14 07:27:45.520093
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.response import text
    from sanic.blueprints import Blueprint

    class BlueprintImplementation(ExceptionMixin, Blueprint):
        pass

    my_blueprint = BlueprintImplementation(__name__, url_prefix='bp')

    @my_blueprint.exception(ZeroDivisionError)
    def handler(request, exception, *args):
        return text('Internal Server Error')

    assert my_blueprint._apply_exception_handler.__func__.__name__ == '_apply_exception_handler_'
    assert my_blueprint._future_exceptions is not None

# Generated at 2022-06-14 07:27:52.591550
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass

    test_mixin = TestExceptionMixin()
    assert test_mixin._future_exceptions == set()
    func = test_mixin.exception(Exception)(lambda x:x)
    assert not test_mixin._future_exceptions == set()

# Generated at 2022-06-14 07:27:55.491234
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    blueprint = Blueprint('test',url_prefix='test')
    exception = blueprint.exception(Exception)
    assert isinstance(exception, exceptions)
    @exception
    def test():
        return 'test'
    assert test() == 'test'

# Generated at 2022-06-14 07:28:06.182047
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    Test the method exception of class ExceptionMixin
    :return:
    """

# Generated at 2022-06-14 07:28:09.119063
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    blueprint = ExceptionMixin()
    blueprint.exception(AssertionError)
    blueprint._future_exceptions



# Generated at 2022-06-14 07:28:19.087977
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FakeBlueprint(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    fake_blueprint = FakeBlueprint()

    @fake_blueprint.exception(Exception)
    def fake_handler():
        pass

    assert len(fake_blueprint._future_exceptions) == 1

    fake_future_exception = next(iter(fake_blueprint._future_exceptions))
    assert fake_future_exception.handler == fake_handler
    assert fake_future_exception.exceptions == (Exception,)
    assert fake_future_exception.kwargs == {}

# Generated at 2022-06-14 07:28:25.510239
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    app = Blueprint('test', url_prefix='/test')

    @app.exception(apply=True)
    def handle_exception(request, exception):
        return "I am the exception handler!"

    assert len(app._future_exceptions) == 1
    assert app._future_exceptions.pop().exceptions == tuple()

# Generated at 2022-06-14 07:28:32.886012
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            pass


    a = A()
    assert len(a._future_exceptions) == 0

    @a.exception(IndexError)
    def f(request):
        pass
    assert len(a._future_exceptions) == 1
    # assert len(a._future_exceptions) == 0

# Generated at 2022-06-14 07:28:43.496005
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    from sanic.exceptions import SanicException

    @Blueprint.exception(SanicException, apply=True)
    def exception_handler(request, exception):
        pass

    app = Sanic(__name__)
    blueprint = Blueprint('test')
    blueprint._apply_exception_handler = lambda x: x
    assert len(blueprint._future_exceptions) == 1

# Generated at 2022-06-14 07:28:44.060635
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:28:54.840074
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
  from sanic.blueprints import Blueprint
  from sanic.exceptions import ServerError
  def teste_func(request):
    return {'message': 'hello'}
  @ExceptionMixin.exception()
  def handler(request, exception):
    return {'message': 'we are so sorry :('}
  teste_app = Blueprint('exception_mixin', url_prefix='/exception_mixin')
  teste_app.add_route(teste_func, '/test')
  func = teste_app.routes[0][2]
  assert len(func._future_exceptions) == 0


# Generated at 2022-06-14 07:29:04.188425
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import sys
    from sanic.models.route import Route
    from sanic.models.blueprint import Blueprint

    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    def test_handler(request, exception):
        return 'Exception'

    bp = Blueprint('test_bp')
    bp.route('/test', methods=['GET'])(lambda r: 'OK')

    bp.exception(test_handler)

    assert isinstance(bp.exception_handler, FutureException)
    assert bp.exception_handler.handler == test_handler
    assert bp.exception_handler.exceptions == (Exception,)

# Generated at 2022-06-14 07:29:08.528460
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    blue = Blueprint("test_ExceptionMixin_exception")

    @blue.exception(Exception)
    async def not_found(request, exception):
        return text("Exception" + exception)



# Generated at 2022-06-14 07:29:16.156398
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A:
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    @A.exception(Exception)
    def handler(req):
        return "hello"

    assert len(A._future_exceptions) == 1
    assert A._future_exceptions.pop().handler is handler

# Generated at 2022-06-14 07:29:23.886856
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint

    app = Sanic('test_ExceptionMixin_exception')
    bp = Blueprint('bp')

    @bp.exception(Exception)
    def erorr_handler(request, exception):
        return response.text('Internal Server Error: {}'.format(exception.args[0]))

    assert len(bp._future_exceptions) == 1

    app.blueprint(bp)

    request, response = app.test_client.get('/')
    assert response.status == 500
    assert response.text == 'Internal Server Error: '

# Generated at 2022-06-14 07:29:30.052385
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    mixin = ExceptionMixin()
    assert len(mixin._future_exceptions) is 0
    assert isinstance(mixin.exception(Exception), types.FunctionType) is True
    assert len(mixin._future_exceptions) is 1
    mixin._future_exceptions.clear()
    assert len(mixin._future_exceptions) is 0
    assert isinstance(mixin.exception([Exception]), types.FunctionType) is True
    assert len(mixin._future_exceptions) is 1



# Generated at 2022-06-14 07:29:30.373306
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:29:39.657303
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyException(Exception):
        pass

    class HttpException(Exception):
        pass

    @ExceptionMixin.exception(MyException)
    def custom_exception_handler(request, exception):
        return exception.args[-1]

    @ExceptionMixin.exception([HttpException, ValueError])
    def multiple_exception_handler(request, exception):
        return exception.args[-1]

    @ExceptionMixin.exception(RuntimeError, apply=False)
    def runtime_error_handler(request, exception):
        return str(exception)


# Generated at 2022-06-14 07:29:54.577020
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    "Check that the method exception of ExceptionMixin is working properly"
    import pytest
    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException
    from sanic.exceptions import SanicException

    @Blueprint.exception(SanicException)
    def catch_exception(request, exception):
        return "internal server error"

    assert isinstance(Blueprint.exception, ExceptionMixin.exception)
    assert isinstance(catch_exception, Blueprint.exception)
    assert Blueprint._future_exceptions
    assert isinstance(Blueprint._future_exceptions, set)
    for future_exception in Blueprint._future_exceptions:
        assert isinstance(future_exception, FutureException)
    # assert FutureException(catch_exception, SanicException) in Blueprint._future_

# Generated at 2022-06-14 07:30:00.930911
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    app = Sanic("test_ExceptionMixin_exception")
    @app.exception(ZeroDivisionError)
    def handle_zero_division_error(request, exception):
        return text("I caught a zero division error", 500)
    response = app.test_client.get("/zero/div/",allow_redirects=True)
    assert response.status == 500



# Generated at 2022-06-14 07:30:10.208605
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.router import Router

    class BluePrint(ExceptionMixin):
        def __init__(self, router: Router):
            self.router = router
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            self.router.add_exception_handler(handler)


    router = Router()
    blue = BluePrint(router)
    @blue.exception(Exception, base=True)
    def exception_handler(request, e):
        pass

    assert len(router.exception_handlers) >= 1

# Generated at 2022-06-14 07:30:23.202644
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    #Test Blueprint class
    from sanic.blueprints import Blueprint
    from sanic.models.exceptions import SanicException, RequestTimeout, Unauthorized, Forbidden
    from sanic.models.futures import FutureException
    from sanic.models.request import Request
    from sanic.models.response import HTTPResponse
    from sanic.models.route import Route
    from sanic.models.static import File
    from sanic.models.template import Template
    from sanic.models.types import T_CORO_A
    from sanic.models.websocket import WebSocket


# Generated at 2022-06-14 07:30:36.215628
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import pytest
    from sanic import Sanic

    bp = Sanic("test_ExceptionMixin_exception")

    @bp.exception(ZeroDivisionError)
    def zero_division(request, exception):
        pass

    assert isinstance(bp.exception, ExceptionMixin.exception)

    @bp.exception([ZeroDivisionError])
    def zero_division_list(request, exception):
        pass

    assert isinstance(bp.exception, ExceptionMixin.exception)

    @bp.exception(ZeroDivisionError, False)
    def zero_division_false(request, exception):
        pass

    assert isinstance(bp.exception, ExceptionMixin.exception)


# Generated at 2022-06-14 07:30:42.931895
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    blueprint = Blueprint('bp', url_prefix='/v1')
    blueprint.exception(Exception)(lambda r: r)

    @blueprint.route('/a')
    def test_a(request):
        return 'a'

    @blueprint.route('/b')
    def test_b(request):
        return 'b'

    @blueprint.exception(RuntimeError)
    def custom_exception(request, exception):
        return response.text(str(exception), 500)

    assert len(blueprint.error_handlers) == 2
    assert len(blueprint._future_exceptions) == 2

# Generated at 2022-06-14 07:30:47.314205
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exceptions = None
    apply = True
    def handler(request, exception):
        return exception

    mixin = ExceptionMixin()
    mixin.exception(exceptions, apply)(handler)

    assert len(mixin._future_exceptions) == 1

# Generated at 2022-06-14 07:30:49.020851
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Implementing the test for method exception for class ExceptionMixin
    pass

# Generated at 2022-06-14 07:30:52.795867
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    app = Sanic('test_ExceptionMixin_exception')
    exception = ExceptionMixin()
    @exception.exception(Exception)
    async def handler(request, exception):
        return text('Ola')

# Generated at 2022-06-14 07:31:01.413258
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    Case 1: ExceptionMixin.exception() when there is no exception
    Case 2: ExceptionMixin.exception() when there is one exception
    Case 3: ExceptionMixin.exception() when there are multiple exceptions
    """

    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass
    exception_mixin = TestExceptionMixin()

    @exception_mixin.exception()
    def test_handler():
        pass

    exception_mixin._future_exceptions.clear()

    @exception_mixin.exception(Exception)
    def test_handler():
        pass

    exception_mixin._future_exceptions.clear()


# Generated at 2022-06-14 07:31:15.184077
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass
    em = TestExceptionMixin()
    exceptions = (Exception,)

    # No arguments
    @em.exception()
    def handler():
        pass

    # Single argument
    @em.exception(Exception)
    def handler():
        pass

    # Multiple arguments
    @em.exception(exceptions)
    def handler():
        pass

    assert len(em._future_exceptions) == 3



# Generated at 2022-06-14 07:31:28.798095
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            self.exceptions = []

        def _apply_exception_handler(self, handler: FutureException):
            self.exceptions.append(handler)

    def exception_handler(req, exception):
        pass

    exception_mixin = TestExceptionMixin()
    exception_mixin.exception(Exception, apply=False)(exception_handler)

    exception_mixin.exception(AttributeError, apply=False)(exception_handler)

    assert len(exception_mixin.exceptions) == 0

    exception_mixin.exception(Exception)(exception_handler)

    assert len(exception_mixin.exceptions) == 1
    assert exception_mixin.exceptions[-1].handler == exception_handler
    assert exception_

# Generated at 2022-06-14 07:31:36.236525
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import sanic.models.exception as exception
    import sanic.models.futures as futures

    obj = exception.ExceptionMixin()

    assert obj._future_exceptions is set()

    @obj.exception(Exception)
    def f(request, exception):
        assert isinstance(exception, Exception)

    assert len(obj._future_exceptions) == 1

    assert isinstance(obj._future_exceptions.pop(), futures.FutureException)

# Generated at 2022-06-14 07:31:39.236878
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Test(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            assert handler == FutureException(handler, [])

    Test().exception()

# Generated at 2022-06-14 07:31:42.055594
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    Test the exception method is defined properly
    """
    assert isinstance(ExceptionMixin.exception, FunctionType)


# Generated at 2022-06-14 07:31:50.006994
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.blueprints import ExceptionMixin
    from sanic.models.futures import FutureException

    blueprint = Blueprint(__name__)
    assert isinstance(blueprint, ExceptionMixin)

    def handler(request, exception):
        return True

    blueprint.exception(Exception)(handler)

    assert len(blueprint._future_exceptions) == 1
    assert isinstance(list(blueprint._future_exceptions)[0], FutureException)

# Generated at 2022-06-14 07:31:55.239352
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    
    # create a blueprint
    bp = Blueprint('MyTestBlueprint', url_prefix='test')
    
    # test that there is no exception handler set yet
    assert len(bp._future_exceptions) == 0
    
    # set an exception handler for the blueprint
    @bp.exception()
    def test_handler():
        pass
    
    # test that the exception handler has been set
    assert len(bp._future_exceptions) == 1

# Generated at 2022-06-14 07:32:04.805094
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprint import Blueprint
    class TestExceptionMixin(Blueprint):
        pass
    mixin = ExceptionMixin()
    # Pass in an integer.
    try:
        assert mixin.exception(1)
    except TypeError as e:
        assert str(e) == "handler must be a function"
    # Pass in a set.
    try:
        assert mixin.exception({1})
    except TypeError as e:
        assert str(e) == "handler must be a function"
    # Pass in a function.
    assert mixin.exception(test_ExceptionMixin_exception)

# Generated at 2022-06-14 07:32:16.721627
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.router import RouteExists
    from sanic.router import RouteNotFound
    from sanic.router import Router

    bp = Blueprint('test_bp', url_prefix='test')

    # Create a mock sanic app without adding any routes to it
    class MockRouter(Router):
        def add(self, uri, handler, methods, host=None):
            # Do not add any route
            pass

    app = Mock()
    app.router = MockRouter(app)
    bp.app = app

    # Call blueprint.exception(myException) and return a handler
    # that does nothing

# Generated at 2022-06-14 07:32:26.963411
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self._future_exception = set()

        def _apply_exception_handler(self, handler):
            self._future_exception.add(handler)

    a = TestExceptionMixin()
    handler = a.exception(KeyError)
    a.exception([KeyError])
    assert len(a._future_exceptions) == 2

    assert handler is not None
    assert a._future_exception is not None

# Generated at 2022-06-14 07:32:45.356432
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ServRequest:
        pass
    
    class Blueprint:
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
    
    def ex_handler(request, exception):
        print(exception)
    
    test_blueprint = Blueprint()
    test_blueprint.exception(Exception)(ex_handler)
    request = ServRequest()
    try:
        raise Exception("Testing!")
    except Exception as ex:
        for exception in test_blueprint._future_exceptions:
            if issubclass(ex.__class__, exception.exceptions):
                exception.handler(request, ex)

# Generated at 2022-06-14 07:32:49.524135
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exc_mixin = ExceptionMixin()
    def handler():
        pass
    assert isinstance(ExceptionMixin.exception(exc_mixin)(handler)(1,2,3),
        type(handler))

# Generated at 2022-06-14 07:33:02.428580
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.utils import create_future
    from sanic.exceptions import ServerError
    from sanic.blueprints import Blueprints
    from sanic.config import Config
    from sanic.router import Router
    from sanic.response import BaseHTTPResponse
    from sanic.server import HttpProtocol
    from sanic.app import Sanic
    from sanic.views import CompositionView

    class TestBlueprint(ExceptionMixin, Blueprints):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

# Generated at 2022-06-14 07:33:07.680464
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    GIVEN  an ExceptionMixin
    WHEN   call method exception
    THEN   return FutureException object
    """
    # Arrange
    exception_mixin = ExceptionMixin()

    # Act
    new_exception = exception_mixin.exception()

    # Assert
    assert isinstance(new_exception, FutureException)

# Generated at 2022-06-14 07:33:08.444973
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:33:16.575292
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print('calling _apply_exception_handler')

    a = A()

    @a.exception(Exception)
    def test(e: Exception):
        print("exception")
        return e

    print(a)
    # assert a._future_exceptions.__next__()._handler == test



# Generated at 2022-06-14 07:33:23.762121
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class foo:
        def __init__(self):
            pass

        def __call__(self, handler):
            return handler

    bp = Blueprint('foo', url_prefix='/foo')

    def example_handler(request, exception):
        pass

    bp.exception(BADRequestException)(example_handler)

    assert example_handler in bp.exception_handlers[BADRequestException]
    assert len(bp.exception_handlers) == 1
    assert example_handler not in bp.exception_handlers[InternalServerError]



# Generated at 2022-06-14 07:33:37.468031
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Request:
        pass

    class Response:
        pass

    app = Sanic('test')
    blueprint = Blueprint('test_blueprint', url_prefix='/test')
    exception = blueprint.exception(Exception)

    @exception
    def handler(request):
        return Response()

    @blueprint.route('/get')
    def handler2(request):
        return Response()

    @blueprint.route('/index/<name:string>/')
    async def handler3(request, name):
        return Response()

    app.blueprint(blueprint)

    @app.exception(Exception)
    def handler_global(request, exception):
        return Response()

    @app.route('/get')
    def handler_global2(request):
        return Response()


# Generated at 2022-06-14 07:33:44.751994
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)

        def _apply_exception_handler(self, handler: FutureException):
            assert handler.handler == 'handler'
            assert handler.exceptions == ('IndexError', 'NaN', 'KeyError')

    mixin = MyExceptionMixin()
    assert mixin._future_exceptions == set()

    def decorator(handler):
        nonlocal apply
        nonlocal exceptions

        if isinstance(exceptions[0], list):
            exceptions = tuple(*exceptions)

        future_exception = FutureException(handler, exceptions)
        mixin._future_exceptions.add(future_exception)
        if apply:
            mixin._apply_exception_handler(future_exception)
        return

# Generated at 2022-06-14 07:33:52.279390
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.future_exceptions_test = self._future_exceptions
        
        def _apply_exception_handler(self, handler):
            pass

    @TestExceptionMixin().exception(Exception)
    def test(request, exception):
        pass
    
    assert test in TestExceptionMixin().future_exceptions_test

# Generated at 2022-06-14 07:34:10.214757
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert ExceptionMixin.exception()

# Generated at 2022-06-14 07:34:13.634021
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    bp = Blueprint()

    @bp.exception(Exception)
    def test(request, exception):
        return text('test')

    fut = bp._future_exceptions.pop()
    assert fut.handler is test
    assert fut.exceptions == (Exception,)

# Generated at 2022-06-14 07:34:21.784701
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprint import Blueprint
    bp = Blueprint('test')

    # test
    assert len(bp._future_exceptions) == 0

    @bp.exception
    def test():
        pass

    assert len(bp._future_exceptions) == 1

    @bp.exception(Exception)
    def test():
        pass

    assert len(bp._future_exceptions) == 2

# Generated at 2022-06-14 07:34:25.095613
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    blueprint = Blueprint('test_bp_exception_mixin', url_prefix='/blueprint')
    # Unit test for assert type(blueprint._future_exceptions) is set
    assert type(blueprint._future_exceptions) is set
    # Unit test for assert len(blueprint._future_exceptions) == 0
    assert len(blueprint._future_exceptions) == 0

    @blueprint.exception(ValueError, apply=False)
    def custom_handler(*args, **kwargs):
        return 'Custom Handler'.encode()

    # Unit test for assert len(blueprint._future_exceptions) == 1
    assert len(blueprint._future_exceptions) == 1

    blueprint._apply_exception_handler(blueprint._future_exceptions.pop())

# Generated at 2022-06-14 07:34:26.196495
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # can't be tested
    pass

# Generated at 2022-06-14 07:34:30.460378
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    @blu.exception(IndexError)
    async def handler(request, exception):
        pass

    assert len(blu._future_exceptions) == 1
    exception = blu._future_exceptions.pop()
    assert isinstance(exception, FutureException)
    assert issubclass(exception.exceptions[0], IndexError)
    assert exception.handler == handler

# Generated at 2022-06-14 07:34:41.336419
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    ExceptionMixin._apply_exception_handler = lambda self, x: None
    # normal case
    exception_mixin = ExceptionMixin()
    @exception_mixin.exception
    def test_exception():
        try:
            1/0
        except Exception as e:
            print(e)
    test_exception()
    # wrong input for function test_exception
    exception_mixin2 = ExceptionMixin()
    @exception_mixin2.exception
    def test_exception2():
        try:
            1/1
        except Exception as e:
            print(e)
    test_exception2()

# Generated at 2022-06-14 07:34:48.924316
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint('bp')
    # Test with proper parameter
    @bp.exception(exception_handler = Exception)
    def handler(request, error):return True
    assert len(bp._future_exceptions) == 1
    assert bp._future_exceptions.pop().handler is handler
    # Test with wrong parameter
    try:
        @bp.exception(wrong_parameter)
        def handler(request, error):return True
    except:
        pass
    else:
        assert False
    # Test without parameter
    try:
        @bp.exception()
        def handler(request, error):return True
    except:
        pass
    else:
        assert False

# Generated at 2022-06-14 07:34:54.326187
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import server_error

    blueprint = Blueprint('test_bp')
    @blueprint.exception(server_error)
    def my_handler(request, exception):
        return 'error happened'

    assert len(blueprint._future_exceptions) == 1

# Generated at 2022-06-14 07:34:59.668105
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            assert handler.type() == (ValueError, TypeError)

    emm = MyExceptionMixin()
    emm.exception(ValueError, TypeError, apply=True)

# Generated at 2022-06-14 07:35:45.330020
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.response import text

    app = Sanic('test_ExceptionMixin_exception')

    @app.exception(ZeroDivisionError)
    async def zero_division(request, exception):
        return text("cannot divide by zero")

    @app.route('/1')
    async def handler_1(request):
        return 1 / 0

    @app.route('/2')
    async def handler_2(request):
        return 2 / 1

    request, response = app.test_client.get('/1')
    assert response.text == 'cannot divide by zero'

    request, response = app.test_client.get('/2')
    assert response.text == '2'

# Generated at 2022-06-14 07:35:46.223628
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True

# Generated at 2022-06-14 07:35:54.121344
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    Test case for method exception of class ExceptionMixin
    """

    from sanic.blueprints import Blueprint

    blueprint = Blueprint(name='test_blueprint_exception')

    @blueprint.exception(Exception, Exception)
    def catch_all_exception(request, exception):
        raise RuntimeError('cannot catch all exceptions')

    with pytest.raises(RuntimeError):
        catch_all_exception({}, {})



# Generated at 2022-06-14 07:36:02.924437
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.views import HTTPMethodView
    from sanic_openapi import doc
    from sanic.response import json

    app = Sanic('test_ExceptionMixin_exception')


# Generated at 2022-06-14 07:36:07.837953
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    obj = ExceptionMixin()
    def my_handler(request, exception):
        return f"Exception has been caught: {exception}"
    n = obj.exception(my_handler)
    assert n(my_handler) is not None
    assert n(my_handler) is my_handler


# Generated at 2022-06-14 07:36:18.121695
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    
    class BlueprintStub:
        def __init__(self):
            self.exceptions: Set[FutureException] = set()

        def apply_exception_handler(self, exception):
            self.exceptions.add(exception)


    def handler(*args):
        return args

    blueprint = BlueprintStub()
    exception_mixin = ExceptionMixin()
    exception_mixin.blueprint = blueprint

    exception_mixin.exception(ZeroDivisionError, KeyError)(handler)

    expected = { 
        FutureException(handler, (ZeroDivisionError, KeyError)) 
    }

    assert expected == blueprint.exceptions

# Generated at 2022-06-14 07:36:28.749219
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import ServerError

    # Arange
    # Create a blueprint
    bp_test = Blueprint('test_bp', url_prefix='test')

    # Act
    @bp_test.exception([ServerError])
    def exception_handler(request, exception):
        return text('I am the exception_handler for ServerError')

    # Assert
    assert len(bp_test._future_exceptions) == 1
    future_exception = bp_test._future_exceptions.pop()
    assert future_exception.exceptions == [ServerError]
    assert future_exception.handler == exception_handler


# Generated at 2022-06-14 07:36:40.574843
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.models import Blueprint

    app = Sanic('test_ExceptionMixin_exception')
    bp = Blueprint('test_ExceptionMixin_exception_blueprint')

    class TestException(Exception):
        pass

    class TestException1(Exception):
        pass

    @bp.exception(TestException)
    def handler_TestException(request, exception):
        return (
            'TestException.msg: {}, TestException.args: {}, TestException.__cause__: {}'.format(exception.msg, exception.args, exception.__cause__))
    assert (bp._future_exceptions[0].handler(None, TestException('TestException'))
            == 'TestException.msg: TestException, TestException.args: (), TestException.__cause__: None')

   

# Generated at 2022-06-14 07:36:53.432793
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class BB(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(BB, self).__init__()
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    assert isinstance(BB, ExceptionMixin)

    try:
        @BB.exception(ValueError)
        def handler(request, exc):
            pass
    except:
        assert False
    else:
        assert True

    try:
        @BB.exception([ValueError])
        def handler(request, exc):
            pass
    except:
        assert False
    else:
        assert True

    BB().exception(ValueError)

# Unit test

# Generated at 2022-06-14 07:37:00.033528
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    blueprint = ExceptionMixin()

    @blueprint.exception([Exception])
    def exception_handler(request, exception):
        pass

    assert len(blueprint._future_exceptions) == 1

    exception = list(blueprint._future_exceptions)[0]

    assert exception.handler == exception_handler
    assert exception.exceptions == tuple([Exception])


# Complete test for method exception of class ExceptionMixin
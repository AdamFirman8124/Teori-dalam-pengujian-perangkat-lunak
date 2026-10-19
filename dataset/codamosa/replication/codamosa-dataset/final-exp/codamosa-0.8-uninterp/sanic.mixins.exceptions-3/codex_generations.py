

# Generated at 2022-06-14 07:27:21.784003
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint as SanicBlueprint
    from sanic import Blueprint
    from sanic.models.futures import FutureException

    class MySanicBlueprint(SanicBlueprint, ExceptionMixin):

        def _apply_exception_handler(self, handler: FutureException):
            pass

    sanic_bp = MySanicBlueprint('sanic_bp', url_prefix='/sanic_bp')
    bp = Blueprint('bp', url_prefix='/bp')

    # Verify that they have different exception handlers
    assert sanic_bp._future_exceptions != bp._future_exceptions

    # Verify that they have no exception handlers
    assert len(sanic_bp._future_exceptions) == 0
    assert len(bp._future_exceptions) == 0

# Generated at 2022-06-14 07:27:31.837949
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.exceptions import NotFound
    from sanic.models.futures import FutureException
    from sanic.utils import sanic_endpoint_test

    class MyExceptionMixin(ExceptionMixin):
        def apply_exception_handler(self, handler):
            super().apply_exception_handler(handler)

    bp = Blueprint('test', url_prefix='/test', host='test')
    bp.add_exception_handler = MyExceptionMixin.apply_exception_handler.__get__(bp)
    bp.add_exception_handler = MyExceptionMixin.apply_exception_handler.__get__(bp)


# Generated at 2022-06-14 07:27:43.260201
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.exceptions import Exceptions
    from sanic.models.blueprint import Blueprint

    blueprint = Blueprint("test", url_prefix="/test")
    blueprint["exceptions"] = Exceptions(blueprint)

    @blueprint.exception(Exception)
    def handler(request: Request, exception: Exception):
        pass

    assert blueprint["exceptions"]._future_exceptions.pop() == FutureException(
        handler, Exception
    )

# Generated at 2022-06-14 07:27:55.284507
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    Test: the function 'exception' of class 'ExceptionMixin'
    """

    class TempClass(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    temp_class = TempClass()
    @temp_class.exception(ValueError)
    def exception_handler(request, exception):
        return "exception handler"

    if len(temp_class._future_exceptions) == 1:
        assert True
    else:
        assert False
    assert exception_handler(1, ValueError) == "exception handler"

test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:28:02.504889
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import SanicException

    class test_ExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print("_apply_exception_handler")

    blueprint = Blueprint(name='test_exception_mixin')
    blueprint.add_route(blueprint.exception(SanicException)(lambda request, exception: None), 'test')
    blueprint.add_route(blueprint.exception(list(SanicException), list(SanicException))(lambda request, exception: None), 'test')
    print(blueprint.routes_all)


test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:28:12.601062
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.http import HTTPResponse
    from sanic.models.futures import FutureException

    bp = Blueprint("mock_bp", url_prefix="/mock_bp")

    @bp.exception(Exception, apply=False)
    def error_handler(request, exception):
        return HTTPResponse("Unhandled error!\n{}".format(exception))

    assert bp._future_exceptions
    assert len(bp._future_exceptions) == 1
    assert type(bp._future_exceptions) is set
    assert bp._future_exceptions.pop() == FutureException(
        error_handler, (Exception,)
    )

# Generated at 2022-06-14 07:28:20.499886
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    from sanic.response import text
    b = Blueprint("name_bp")
    func = "func"
    # TODO Как достать исключение из декоратора
    # @b.exception(TypeError)
    # def example(request):
    #     return text('Example')
    assert isinstance(b.exception, Blueprint.exception.__class__)
    assert b.exception is Blueprint.exception

# Generated at 2022-06-14 07:28:27.573450
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Router(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print(handler)

    router = Router()
    @router.exception(Exception)
    def handler(request, exception):
        print(exception)

    assert len(router._future_exceptions) == 1
    future_exception = router._future_exceptions.pop()
    assert future_exception.handler == handler
    assert len(future_exception.exceptions) == 1
    assert future_exception.exceptions[0] == Exception

# Generated at 2022-06-14 07:28:36.540417
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    bp = Blueprint(__name__)

    @bp.exception([Exception])
    def exception_handler(request, exception):
        return text('<p>Exception: {}</p>'.format(exception),
                    status=500)

    assert len(bp._future_exceptions) == 1
    future_exception = bp._future_exceptions.pop()
    assert future_exception._handler.__name__ == 'exception_handler'
    assert 'Exception' in future_exception._exceptions_to_catch

# Generated at 2022-06-14 07:28:50.425484
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.request import Request
    from sanic.exceptions import NotFound

    class TestExceptionMixin(ExceptionMixin):

        def _apply_exception_handler(self, handler: FutureException):
            # Assert that handler is actually a FutureException
            assert isinstance(handler, FutureException)
            # Assert that handler is in the set of FutureExceptions
            assert handler in self._future_exceptions
            # Assert that the handler has been called with the right arguments
            assert handler(None, NotFound(), Request(b'testdata', 'testurl')) == 'test'

    TestBlueprint = Blueprint('testbp')
    TestBlueprint.exception([NotFound], apply=True)(lambda _, exc, req: 'test')

# Generated at 2022-06-14 07:28:58.751390
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import sanic.blueprints
    import sanic.app

    assert hasattr(sanic.blueprints.BluePrint, 'exception'), 'Should be defined'
    assert hasattr(sanic.app.Sanic, 'exception'), 'Should be defined'

# Generated at 2022-06-14 07:29:05.329827
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    # arrange
    args = [None, None]
    kwargs = {}
    exceptions = [None, None]
    apply = True

    def decorator(handler):
        nonlocal apply
        nonlocal exceptions

        if isinstance(exceptions[0], list):
            exceptions = tuple(*exceptions)

        future_exception = FutureException(handler, exceptions)
        self._future_exceptions.add(future_exception)
        if apply:
            self._apply_exception_handler(future_exception)
        return handler

    # act
    returned = decorator(exceptions)

    # assert
    assert returned == None

# Generated at 2022-06-14 07:29:06.542363
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert ExceptionMixin.exception("test")

# Generated at 2022-06-14 07:29:19.060464
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin(object):
        def __init__(self):
            self._future_exceptions = set()
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler):
            raise NotImplementedError  # noqa

        def exception(self, *exceptions, apply=True):
            if len(exceptions) == 1 and isinstance(exceptions[0], list):
                exceptions = tuple(*exceptions)

            future_exception = FutureException(None, exceptions)
            self._future_exceptions.add(future_exception)
            if apply:
                self._apply_exception_handler(future_exception)

    ex = ExceptionMixin()
    assert ex.__class__.__name__ == 'ExceptionMixin'
    assert ex.exception.__name__

# Generated at 2022-06-14 07:29:29.631892
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            self.handler = handler
            return handler

    blueprint = Blueprint()
    assert not blueprint._future_exceptions

    @blueprint.exception(Exception)
    def handler(request, exception):
        return 'Error'

    assert len(blueprint._future_exceptions) == 1
    assert blueprint.handler.handler() == handler()
    assert blueprint.handler.exceptions == (Exception, )
    assert blueprint.handler.handler_kwargs == {}

# Generated at 2022-06-14 07:29:34.794263
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    exception_mixin_test = ExceptionMixinTest()
    exception_mixin_test.exception(Exception)

# Generated at 2022-06-14 07:29:35.439664
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    ExceptionMixin()

# Generated at 2022-06-14 07:29:46.398362
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Create a mock instance of future exception
    future_exception = Mock()
    future_exception.handler = 'sample'
    future_exception.exceptions = 'sample'

    # Create mock instance of request handler
    request_handler = Mock()
    request_handler.__name__ = 'sample'

    # Mocking the static method register of class ExceptionMixin
    with patch.object(ExceptionMixin, '_apply_exception_handler'):
        # Create a mock instance of ExceptionMixin
        exception_mixin = ExceptionMixin()

        # Assert that the mocked request handler is in future exception
        assert request_handler in exception_mixin.exception(None, apply=False)

# Generated at 2022-06-14 07:29:50.266697
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        pass
    blueprint = Blueprint()
    @blueprint.exception(ValueError)
    def handler(request):
        pass

# Generated at 2022-06-14 07:29:57.579923
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint

    bp = Blueprint('test', url_prefix='test')
    @bp.exception(ValueError)
    def error_handler(request, exception):
        return response.text('Internal server error')

    assert len(bp._future_exceptions) == 1
    first = next(iter(bp._future_exceptions))
    assert first.handler == error_handler
    assert first.as_list() == [ValueError]

# Generated at 2022-06-14 07:30:07.982010
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint, response
    from sanic.exceptions import NotFound
    # Initialization
    blueprint = Blueprint(__name__)
    # Test
    @blueprint.exception(NotFound)
    def exception_handler(request, exception):
        return response.json(
            {"exception": "{}".format(exception)},
            status=exception.status_code
        )

# Generated at 2022-06-14 07:30:13.193701
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            assert len(self._future_exceptions) == 1
            assert handler.handler == handler
            assert handler.exceptions[0] == RuntimeError

    blueprint = Blueprint()
    blueprint.exception(RuntimeError)(lambda x: x)

# Generated at 2022-06-14 07:30:19.525251
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    _args = ('a','b','c')
    
    class ExceptionMixin_(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

    instance = ExceptionMixin_(*_args)
    assert isinstance(instance.exception(*_args), types.FunctionType)

# Generated at 2022-06-14 07:30:22.832121
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(exceptions=(ValueError,))
    def handle_exception(request, exc):
        pass

    assert isinstance(handle_exception,types.FunctionType)

# Generated at 2022-06-14 07:30:31.361305
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FooException(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    foo = FooException()

    def foo_handler(*args, **kwargs):
        pass

    foo.exception(foo_handler)
    
    assert foo._future_exceptions == {FutureException(foo_handler, ())}

# Generated at 2022-06-14 07:30:42.950819
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test case 1: no exception handler
    blueprint_exception = ExceptionMixin()
    blueprint_exception._apply_exception_handler = Mock()
    blueprint_exception.exception()()
    assert not blueprint_exception._apply_exception_handler.called

    # Test case 2: has exception handler
    blueprint_exception = ExceptionMixin()
    blueprint_exception._apply_exception_handler = Mock()

    @blueprint_exception.exception()
    def just_test():
        pass

    assert blueprint_exception._apply_exception_handler.called
    assert len(blueprint_exception._future_exceptions) == 1
    assert type(blueprint_exception._future_exceptions.pop()) is FutureException
    assert just_test is not None

# Generated at 2022-06-14 07:30:43.774660
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert 1 == 1

# Generated at 2022-06-14 07:30:55.509896
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @sanic.blueprint(url_prefix='test')
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
        async def _apply_exception_handler(handler, *exceptions, **kwargs) -> None:
            pass

    # Create an instance of class TestExceptionMixin
    test_exception_mixin = TestExceptionMixin()
    # Use test_exception_mixin's method exception
    @test_exception_mixin.exception(ValueError)
    async def test(_):
        return 'ok'
    # If there is no exception, the result will be 'ok'
    assert test('') == 'ok'



# Generated at 2022-06-14 07:31:08.685765
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    import pytest
    from functools import partial

    blueprint = Blueprint(name='test', url_prefix='/test', version=1)

    @blueprint.exception(IndexError)
    async def handler(request, exception):
        return "OK"

    @blueprint.route('/ping')
    async def ping(request):
        raise IndexError
    
    app = blueprint.create_app()

    test_params = [
        (IndexError, 200, 'OK'),
    ]


    @pytest.mark.parametrize('exc, status, result', test_params)
    def test_eception(exc, status, result):
        request, response = app.test_client.get('/test/1/')

        assert response.status == status

# Generated at 2022-06-14 07:31:17.212874
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint("test_ExceptionMixin_exception", url_prefix='/test')

    @bp.exception(ValueError)
    def handler(request, exception):
        return text("OK", status=200)

    #  bp.exception(ValueError)(handler)
    bp._apply_exception_handler(bp._future_exceptions.pop())
    bp_exception_handler = bp.error_handler.handlers[(ValueError,)]

    print(bp_exception_handler)
    assert bp_exception_handler == handler

# Generated at 2022-06-14 07:31:30.487895
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import BluePrint

    my_bp = BluePrint('my_bp')

    @my_bp.exception(FileNotFoundError)
    def file_not_found_error_handler(request, exception):
        return 'File not found.'

    assert my_bp._future_exceptions

    @my_bp.exception(FileExistsError, apply=False)
    def file_exists_error_handler(request, exception):
        return 'File already exists.'

    assert my_bp._future_exceptions

# Generated at 2022-06-14 07:31:39.579447
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    from sanic import response

    bp = Blueprint('bp')

    @bp.exception(Exception)
    def unhandled_exception(request, exception):
        return response.text('Internal Server Error', 500)

    assert isinstance(bp.exception, ExceptionMixin.exception)

    assert bp.exception_handler_order == 500
    assert bp.exception_handler.__name__ == "unhandled_exception"


# Generated at 2022-06-14 07:31:46.987621
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException

    bp = Blueprint("bp", url_prefix="/bp")
    # test not raise exception when applying
    # the exception handler for blueprint
    bp.exception(IndexError)(lambda request, exception: None)
    # test raise exception when applying
    # the exception handler for blueprint
    bp.exception(IndexError, IndexError)(lambda request, exception: None)

# Generated at 2022-06-14 07:31:55.526419
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    test1 = A()
    test2 = A()

    @test1.exception(IndexError)
    def handler1(request, exception):
        return 'found exception'
    @test2.exception(IndexError, KeyError)
    def handler2(request, exception):
        return 'found exception'

    assert A._future_exceptions == {handler1, handler2}

# Generated at 2022-06-14 07:32:02.413994
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyException(Exception):
        pass

    class MyBluePrint(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            i = 0
            while i < 10:
                print('test exception')
                i += 1
    blueprint = MyBluePrint()
    blueprint.exception(MyException)(handle)

#Unit test for method _apply_exception_handler of class ExceptionMixin

# Generated at 2022-06-14 07:32:06.524295
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    em = ExceptionMixin()
    em._apply_exception_handler = lambda x: x
    em.exception(Exception)

# Generated at 2022-06-14 07:32:16.649760
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.blueprints import Blueprint

    # Create a app
    bp = Blueprint("test", url_prefix="/test")
    app = Sanic(__name__)

    # Create a function as a global exception handler
    @bp.exception(Exception)
    def test_exception(request, exception):
        return text("Oops! Something went wrong")

    sanic_bp = bp.as_blueprint()
    app.register_blueprint(sanic_bp)

    #Check the class attribute of exception object which is created by method exception
    assert isinstance(sanic_bp._future_exceptions, set)
    assert next(iter(sanic_bp._future_exceptions)).handler == test_exception
    assert next(iter(sanic_bp._future_exceptions)).exceptions

# Generated at 2022-06-14 07:32:29.225242
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.blueprints import Blueprint

    class TestMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    class TestBlueprint(TestMixin, Blueprint):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

    app = Sanic("test_ExceptionMixin_exception")
    test_blueprint = TestBlueprint('test_blueprint')

    @test_blueprint.exception(Exception)
    def exception_handler(request, exception):
        pass


# Generated at 2022-06-14 07:32:37.876552
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    This function executes a unit test for the method __init__ of class
    ExceptionMixin.
    """
    # Define an ExceptionMixin object and apply one function called 'handler'
    # with the exceptions: NotImplementedError and AttributeError
    test_instance = ExceptionMixin()
    assert test_instance._future_exceptions == set()
    test_instance.exception(NotImplementedError, AttributeError)(handler)
    assert test_instance._future_exceptions == set({
        FutureException(handler, (NotImplementedError, AttributeError))
    })



# Generated at 2022-06-14 07:32:42.606805
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.views import HTTPMethodView

    class HandlerMethodView(HTTPMethodView):
        async def get(self):
            pass

    exception_view = HandlerMethodView.exception
    assert hasattr(exception_view, "exception")
    assert exception_view.exception == HandlerMethodView.exception

# Generated at 2022-06-14 07:32:52.007043
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:33:03.732226
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint

    # Create application
    app = Sanic('test_ExceptionMixin_exception')

    # Create bluerint
    bp = Blueprint('name', url_prefix='/prefix')

    # Test decorator
    @bp.exception(Exception)
    async def test(request, exception):
        return request, exception

    assert len(bp._future_exceptions) == 1
    assert bp._future_exceptions.pop().exceptions == (Exception,)
    assert bp._future_exceptions == set()
    assert test.__name__ == 'test'

    # Add blueprint to application
    app.blueprint(bp)

    # Get exceptions of application
    exception_handlers = app.error_handler.handlers

# Generated at 2022-06-14 07:33:11.848772
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from sanic.blueprints import Blueprint
    from sanic.models.routes import Route

    blueprint = Blueprint('test', url_prefix='/test')
    blueprint.exception(IndexError)(lambda x: x)
    blueprint.exception(ValueError)(lambda x: x)
    blueprint.exception(Exception)(lambda x: x)

    assert len(blueprint._future_exceptions) == 3

    _future_exception = FutureException(lambda x: x, Exception)
    blueprint._future_exceptions.add(_future_exception)
    assert len(blueprint._future_exceptions) == 3


# Generated at 2022-06-14 07:33:23.633221
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.response import json
    from sanic.blueprints import Blueprint

    bp = Blueprint("test_bp")
    app = Sanic("test_app")


    async def handler_exceptions(request, exception):
        return json({"exception": f"{exception}"})

    @bp.exception(ZeroDivisionError)
    def handler_exceptions():
        return json({"exception": "ZeroDivisionError"})

    bp.add_route(handler_exceptions, "/div/<var1>", methods=["GET"])

    @bp.get("/div/<var1>")
    async def handler(request, var1):
        return json({"result": 1000 / int(var1)})

    app.blueprint(bp)

   

# Generated at 2022-06-14 07:33:30.360528
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class UnitTestExceptionMixin(ExceptionMixin):

        def __init__(self):
            super(ExceptionMixin, self).__init__()

        def _apply_exception_handler(self, handler):
            pass

    # Define a blueprint to be tested
    blueprint = UnitTestExceptionMixin()

    @blueprint.exception(Exception)
    def test(request, exception):
        pass

    # Assert that exception method add a new object of class FutureException
    # to set _future_exceptions
    assert type(blueprint._future_exceptions) == set
    assert len(blueprint._future_exceptions) == 1
    assert type(blueprint._future_exceptions.pop()) == FutureException

# Generated at 2022-06-14 07:33:34.439188
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def __init__(self):
            super(Blueprint, self).__init__()

    blueprint = Blueprint()
    @blueprint.exception(ZeroDivisionError)
    def div_by_zero(request, exception):
        print('Handling {} exception'.format(exception.__class__.__name__))

    assert blueprint
    assert blueprint._future_exceptions
    assert blueprint._apply_exception_handler

# Generated at 2022-06-14 07:33:40.876931
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.handlers import ErrorHandler
    blueprint = Blueprint('')
    blueprint.exception(ValueError)(lambda x: '')

    assert blueprint._future_exceptions is not None
    assert blueprint._future_exceptions
    assert len(blueprint._future_exceptions) == 1
    assert blueprint._future_exceptions.pop().handler is not None

# Generated at 2022-06-14 07:33:54.103231
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MockBlueprint:
        def __init__(self):
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    bp = MockBlueprint()

    @bp.exception(Exception)
    def exception_handler(request, exception):
        pass

    assert exception_handler in bp._future_exceptions
    assert exception_handler.args == (Exception,)

    # Test exceptions list
    @bp.exception([Exception])
    def exception_handler2(request, exception):
        pass

    assert exception_handler2 in bp._future_exceptions
    assert exception_handler2.args == (Exception,)

    # Test apply

# Generated at 2022-06-14 07:34:01.957868
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test mixed in class should also have method exception, together
    # with attribute _future_exceptions.
    class TestExceptionMixin(ExceptionMixin):
        pass

    assert hasattr(TestExceptionMixin, '_future_exceptions')
    assert hasattr(TestExceptionMixin, 'exception')

    # Test _future_exceptions should be initialized to empty set.
    obj = TestExceptionMixin()
    assert obj._future_exceptions == set()

    # Test if decorator `exception` is working properly.
    @obj.exception(ValueError, IndexError)
    def handler():
        pass

    future_exception = FutureException(handler, (ValueError, IndexError))
    assert obj._future_exceptions == {future_exception}

# Generated at 2022-06-14 07:34:05.934102
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Arrange
    class Test(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)
    # Act
    test = Test()
    test_exception = test.exception
    # Assert
    assert(test_exception)

# Generated at 2022-06-14 07:34:24.534251
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    test = ExceptionMixin()
    exceptions = (Exception,)
    result = test.exception(exceptions)
    assert result


# Generated at 2022-06-14 07:34:30.360291
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.exceptions import ServerError

    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_exception_mixin = TestExceptionMixin()

    @test_exception_mixin.exception(ServerError)
    def test_exception_handler(request, exception):
        print(request, exception)

    assert test_exception_mixin._future_exceptions is not None

# Generated at 2022-06-14 07:34:36.468298
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    #import warnings
    #with warnings.catch_warnings(record=True) as w:
    #    warnings.simplefilter("always")

    # TODO: Create a mock version of ExceptionMixin, and set up with
    #       a mock version of FutureException.
    # TODO: Test 'apply' argument
    assert True

# Generated at 2022-06-14 07:34:37.340028
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:34:49.137962
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinSub(ExceptionMixin):
        def __init__(self):
            super(ExceptionMixinSub, self).__init__()
        
        def _apply_exception_handler(self, handler: FutureException):
            self._future_exceptions.add(handler)
    
    sub = ExceptionMixinSub()
    test_handler_1 = lambda x: x
    test_handler_2 = lambda x: x * 2
    sub.exception(AssertionError)(test_handler_1)
    sub.exception(ZeroDivisionError)(test_handler_2)
    assert sub._future_exceptions == {
        FutureException(handler=test_handler_1, exceptions=(AssertionError,)),
        FutureException(handler=test_handler_2, exceptions=(ZeroDivisionError,)),
    }

# Generated at 2022-06-14 07:34:56.663809
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    ex_mixin = TestExceptionMixin()

    @ex_mixin.exception(ValueError, apply=True)
    def ex_func(ex_error):
        raise ex_error
    assert isinstance(ex_mixin._future_exceptions.pop(), FutureException)


# Generated at 2022-06-14 07:34:59.374839
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    e = ExceptionMixin()
    with pytest.raises(NotImplementedError):
        e.exception(Exception)()

# Generated at 2022-06-14 07:35:10.405471
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint2(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    blueprint = Blueprint2()

    @blueprint.exception(Exceptions)
    def handler():
        pass

    future_exception = FutureException(handler, (Exceptions,))
    assert future_exception in blueprint._future_exceptions

    blueprint = Blueprint2()
    exceptions = (Exceptions, another_exception)

    @blueprint.exception(*exceptions)
    def handler():
        pass

    future_exception = FutureException(handler, (Exceptions, another_exception))
    assert future_exception in blueprint._future_exceptions

# Generated at 2022-06-14 07:35:21.525243
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException

    mixin = ExceptionMixin()
 
    # case 1
    args = (IndexError,)
    kwargs = {"status_code":404}
    def handler(request, exception):
        print("exception IndexError:",exception,"status_code:",kwargs["status_code"])
        
    exception = FutureException(handler,args)
    mixin._future_exceptions.add(exception)
    mixin._apply_exception_handler(exception)
    assert mixin._future_exceptions == {handler:(IndexError,)}
    assert mixin.exception(*args,**kwargs)(handler) == handler  

    # case 2
    args = (IndexError,)
    kwargs = {"status_code":404}

# Generated at 2022-06-14 07:35:34.274425
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.response import json
    from sanic import Sanic

    # create a blueprint
    my_bp1 = Blueprint("my_bp1")

    @my_bp1.exception(ValueError)
    def my_bp1_handler(request, exception):
        return json({"exception": str(exception)})

    # create a app decorated with the blueprint
    app = Sanic(__name__)
    
    # check the app dict
    assert app.__dict__['exception_handlers'] == {}
    assert app.__dict__['blueprints'] == {}

    # register the blueprint on the app
    app.blueprint(my_bp1)

    # check the app dict
    assert app.__dict__['exception_handlers'] == {}
    assert app

# Generated at 2022-06-14 07:36:19.800021
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    from sanic.models.futures import FutureException

    class FakeBlueprint:
        def __init__(self):
            self.exception_handler_called = False
            self.future_exceptions = []

        def _apply_exception_handler(self, handler: FutureException):
            self.exception_handler_called = True
            self.future_exceptions.append(handler)

    fake_blueprint = FakeBlueprint()

    class Mixin:
        def __init__(self):
            self._future_exceptions: Set[FutureException] = set()

    mixin = Mixin()

    # Define the decorator function

# Generated at 2022-06-14 07:36:31.328452
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint

    blp1 = Blueprint('blp1')

    @blp1.exception(KeyError)
    def handler(request, exception):
        print(type(exception))
        return 'hello'

    assert type(blp1.exception) == Blueprint.exception.__class__
    assert len(blp1._future_exceptions) == 1
    assert len(blp1.blueprint_functions) == 0
    assert len(blp1.blueprint_route_middleware) == 0

    import uuid
    blp2 = Blueprint('blp2')


# Generated at 2022-06-14 07:36:33.448134
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # TODO: implement unit test for method exception of class ExceptionMixin
    assert True == True


# Generated at 2022-06-14 07:36:39.778944
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class DummyClass(ExceptionMixin):
        pass

    exception_mixin = DummyClass()
    exception = ['ConnectionError', 'TimeoutError']
    handler = lambda exception, request: print(exception, request)
    exception_mixin.exception(exception)(handler)
    assert len(exception_mixin._future_exceptions) == 1


# Generated at 2022-06-14 07:36:49.847884
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.response import json
    from sanic.exceptions import NotFound

    app = Sanic(name=__name__)

    @app.exception(Exception)
    def all_exception_handler(request, exception):
        return json({'global': 'exception handler'}, status=500)

    @app.route('/404')
    def handler(request):
        raise NotFound('Not found', status_code=404)

    request, response = app.test_client.get('/404')
    assert response.status == 404

# Generated at 2022-06-14 07:36:58.279372
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.exception_mixin import ExceptionMixin
    from sanic.models.futures import FutureException
    from sanic.models.blueprint import Blueprint
    class Test(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

    test = Test()
    test.exception(KeyError, apply=True)
    assert len(test._future_exceptions) == 1


# Generated at 2022-06-14 07:37:10.822417
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import asyncio
    from sanic.app import Sanic
    from sanic.exceptions import Forbidden, NotFound
    from sanic.models import BlueprintMixin, ExceptionMixin
    from sanic.response import text
    from sanic.testing import HOST, PORT

    app = Sanic()

    class MockBlueprint(BlueprintMixin, ExceptionMixin):
        pass

    bp = MockBlueprint()

    @bp.exception(NotFound)
    def ignore_exception(request, exception):
        return text("You should not see this.")

    @bp.route("/")
    def handler(request):
        raise NotFound

    app.blueprint(bp)

    request, response = app.test_client.get("/")
    assert response.status == 404



# Generated at 2022-06-14 07:37:23.540105
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.exceptions import InvalidUsage

    class Base:
        def __init__(self, *args, **kwargs):
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    class Test(ExceptionMixin, Base):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler: FutureException):
            #nothing to do
            return
    
    # Test get goods result
    class TestException:
        def __init__(self, test_object):
            self._
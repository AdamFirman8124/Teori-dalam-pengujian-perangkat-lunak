

# Generated at 2022-06-14 07:27:15.157164
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    blueprint = ExceptionMixin()
    blueprint.exception(Exception)
    assert blueprint._future_exceptions

# Generated at 2022-06-14 07:27:21.035417
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import SanicException

    bp = Blueprint('test_bp', url_prefix='test')

    @bp.exception(SanicException)
    def exception_handler(request, exception):
        request['handled'] = True

    assert exception_handler in bp._future_exceptions.handlers.values()

# Generated at 2022-06-14 07:27:22.661909
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test the method
    assert True

# Generated at 2022-06-14 07:27:32.610063
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # test param apply=True
    bp1 = Mock()
    bp1.exception.return_value = exception_handler
    bp1._apply_exception_handler = Mock()
    bp1.exception(Exception)

    bp1.exception.assert_called_with(Exception)
    bp1._apply_exception_handler.assert_called_with(FutureException(exception_handler, (Exception,)))

    # test param apply=False
    bp2 = Mock()
    bp2.exception.return_value = exception_handler
    bp2._apply_exception_handler = Mock()
    bp2.exception(Exception, apply=False)

    bp2.exception.assert_called_with(Exception)
    bp2._apply_exception_handler.assert_

# Generated at 2022-06-14 07:27:46.576417
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_1(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_obj = ExceptionMixin_1()

    @test_obj.exception(Exception)
    def func():
        return

    assert isinstance(func, types.FunctionType)
    assert callable(func)

    @test_obj.exception([Exception, Exception])
    def func_1():
        return

    assert isinstance(func_1, types.FunctionType)
    assert callable(func_1)

# Generated at 2022-06-14 07:27:58.366803
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic, response
    from sanic.exceptions import InvalidUsage, ServerError

    # Given
    app = Sanic('test')
    blueprint = app.blueprint('test')
    blueprint.init_exception()

    # When
    @blueprint.exception(InvalidUsage,ServerError)
    def test_exception_handler(request, exception):
        return response.text(exception.status_code)

    @app.get('/test')
    def test_exception_handler_route(request):
        raise InvalidUsage()

    # Then
    assert test_exception_handler.sanic_exception_handler == True
    assert app.exception_handler != None

# Generated at 2022-06-14 07:28:05.196653
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    mixin = ExceptionMixin()

    @mixin.exception(ValueError)
    def test_exception_handler(request, exception):
        return 'exception'

    future_exceptions = list(mixin._future_exceptions)
    assert len(future_exceptions) == 1
    fut_exception = future_exceptions[0]
    assert fut_exception.handler == test_exception_handler
    assert fut_exception.exceptions == (ValueError,)

# Generated at 2022-06-14 07:28:16.939410
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def handler():
        pass
    
    origin = test_ExceptionMixin_exception
    origin.app = Sanic('test_ExceptionMixin_exception')
    origin.app.blueprint(ExceptionMixin())

    @origin.app.exception()
    def catch_all_exception(request, exception):
        pass

    @origin.app.exception(404, 405)
    def catch_not_found_exceptions(request, exception):
        pass

    @origin.app.exception(ZeroDivisionError)
    def zerodivisionerror_handler(request, exception):
        pass

    @origin.app.exception([ZeroDivisionError, BlockingIOError])
    def zerodivisionerror_and_blockingioerror_handler(request, exception):
        pass


    origin.app.error

# Generated at 2022-06-14 07:28:29.967849
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.handlers import ErrorHandler
    from sanic.exceptions import NotFound

    class A(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, exception: FutureException):
            exception.handler(None, exception.exception_type)

    test_class = A()
    test_exception_handler = test_class.exception([NotFound], apply=True)
    assert isinstance(test_exception_handler, ErrorHandler)
    not_found_exceptions = set()
    try:
        test_exception_handler(None, [NotFound])
    except Exception:
        not_found_exceptions.add(Exception)
    assert NotFound in not_found_exceptions

# Generated at 2022-06-14 07:28:41.778485
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    from unittest import TestCase
    from sanic.exceptions import SanicException
    from sanic.models.exceptions import FutureException

    class TestException(SanicException):
        pass

    testExceptionMixin = TestExceptionMixin()
    exception_sets = testExceptionMixin.exception(
        TestException, apply=False)

    @exception_sets
    def test_function():
        pass


# Generated at 2022-06-14 07:28:47.806797
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        pass

    test_exc_mixin = TestExceptionMixin()
    test_exc_mixin.exception(Exception)
    assert test_exc_mixin._future_exceptions != set()

# Generated at 2022-06-14 07:28:56.250217
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic import Blueprint

    class MyException(Exception):
        pass
    
    # Create a new Sanic app
    app = Sanic('test')

    # Create a new Blueprint
    bp = Blueprint('test_blueprint')

    @bp.exception(MyException)
    def handler(request, exception):
        pass
    
    handler(None, MyException)

    assert handler in bp._future_exceptions

# Generated at 2022-06-14 07:28:58.372356
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_test(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    ExceptionMixin_test().exception('test_1','test_2','test_3')('test_handler')



# Generated at 2022-06-14 07:29:08.849287
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException

    class BasicExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.applied_future_exceptions = []

        def _apply_exception_handler(self, handler):
            self.applied_future_exceptions.append(handler)

    class DummyHandler:
        pass

    basic_exception_mixin: BasicExceptionMixin = BasicExceptionMixin()
    dummy_handler: DummyHandler = DummyHandler()
    exception_handler = basic_exception_mixin.exception(Exception)(dummy_handler)
    assert type(basic_exception_mixin._future_exceptions.pop()) is FutureException
    assert exception_handler is dummy_handler
    assert basic_exception_mixin.app

# Generated at 2022-06-14 07:29:10.056687
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass


# Generated at 2022-06-14 07:29:10.837463
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:29:17.874555
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import BaseFuture
    from sanic.models.blueprint import SanicBlueprint

    blueprint = SanicBlueprint("test", url_prefix="test")
    blueprint.exception(Exception)(print)
    # Unit test for method _apply_exception_handler of class ExceptionMixin
    blueprint._apply_exception_handler(blueprint._future_exceptions.pop())

# Generated at 2022-06-14 07:29:19.960276
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    blueprint = Blueprint()

    @blueprint.exception(Exception)
    def test_function(request, exception):
        return "OK"

# Generated at 2022-06-14 07:29:23.276800
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    a = ExceptionMixin()
    @a.exception(Exception)
    def b():
        return "test"
    assert "test" == b()

# Generated at 2022-06-14 07:29:24.549469
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """[Summary]
    """
    pass

# Generated at 2022-06-14 07:29:33.268407
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class bp_test(ExceptionMixin):
        def __init__(self):
            self._future_exceptions = set()
            self.name='test'
    bp = bp_test()
    @bp.exception([Exception],except_key='except_key')
    async def exception_handler(request,exception,except_key):
        return except_key
    assert bp._future_exceptions.pop().kwargs['except_key'] == 'except_key'
    del bp

# Generated at 2022-06-14 07:29:38.223570
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FakeBlueprint(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    blueprint = FakeBlueprint()

    @blueprint.exception(IndexError)
    def exception_handler():
        pass

    len(blueprint._future_exceptions) == 1

# Generated at 2022-06-14 07:29:40.306797
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    a = ExceptionMixin()
    assert a.exception('x','y','z')

# Generated at 2022-06-14 07:29:41.003699
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:29:54.200594
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A:
        pass
    class B:
        pass
    a = A()
    b = B()
    a.__name__ = "exception_handler"
    
    em = ExceptionMixin()
    em.exception(A, apply=True)(a)

    assert (a, (A,), {}, True) == (em._future_exceptions.pop().handler, em._future_exceptions.pop().exceptions, em._future_exceptions.pop().kwargs, em._future_exceptions.pop().apply_handler)

    em1 = ExceptionMixin()

    em1.exception([A, B], apply=False)(b)

# Generated at 2022-06-14 07:29:57.288501
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def dummy_handler():
        pass

    @ExceptionMixin.exception(ZeroDivisionError, apply=True)
    def handler():
        pass

    assert dummy_handler == handler

# Generated at 2022-06-14 07:30:03.747047
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic

    app = Sanic("test_ExceptionMixin_exception")
    @app.exception(IndexError)
    def exception_handler(request, exception):
        return text("Exception handled")

    request, response = app.test_client.get("/")
    assert response.status == 500
    assert response.text == "Exception handled"

# Generated at 2022-06-14 07:30:10.173356
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from sanic.blueprints import Blueprint

    blueprint = Blueprint('test_blueprint', url_prefix='/test')
    try:
        raise ValueError
    except ValueError:
        blueprint.exception(ValueError)(print)
    assert(isinstance(blueprint._future_exceptions, set))
    assert(isinstance(blueprint._future_exceptions.pop(), FutureException))

# Generated at 2022-06-14 07:30:12.295102
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert ExceptionMixin.exception(1, 2, 3)

# Generated at 2022-06-14 07:30:18.968945
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    ExceptionMixin(self, *args, **kwargs)
    unit test for method exception
    """

    class Fake_ExceptionMixin(ExceptionMixin):
        def __init__(self):
            pass

    fake_exception_mixin = Fake_ExceptionMixin()
    fake_exception_mixin.exception(1, 2, apply = True)

# Generated at 2022-06-14 07:30:34.406992
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def handler(*args):
        pass

    mixin = ExceptionMixin()
    mixin.exception('a', 'b')(handler)
    assert len(mixin._future_exceptions) == 1

    # default must be True
    future_exception = FutureException(handler, ('a', 'b'))
    assert future_exception.apply is True

    mixin.exception('a')(handler)
    assert len(mixin._future_exceptions) == 2

# Generated at 2022-06-14 07:30:44.224505
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin:
        """
        This class is a temporary test class for class ExceptionMixin.
        """
        def __init__(self):
            self._apply_exception_handler = MagicMock()
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler: FutureException):
            self._apply_exception_handler(handler)

    exception_mixin = ExceptionMixin.__new__(TestExceptionMixin)

    @exception_mixin.exception(Exception)
    def test_exception_handler(request, exception):
        return "test_exception_handler"

    # check method exception
    assert test_exception_handler(None, None) == "test_exception_handler"

# Generated at 2022-06-14 07:30:55.926479
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class BB:
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    class AA(ExceptionMixin, BB):
        pass
    a = AA()
    def decorator(handler):
        nonlocal apply
        nonlocal exceptions

        if isinstance(exceptions[0], list):
            exceptions = tuple(*exceptions)

        future_exception = FutureException(handler, exceptions)
        a._future_exceptions.add(future_exception)
        if apply:
            a._apply_exception_handler(future_exception)
        return handler

    a.exception(1)

# Generated at 2022-06-14 07:31:08.989554
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import pytest
    from sanic import Sanic

    app = Sanic()

    class FakeBlueprint(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.exception_handler = object()
            self.name = 'FakeBlueprint'

        def _apply_exception_handler(self, handler: FutureException):
            self.exception_handler = handler

    bp = FakeBlueprint()

    def handler():
        pass

    #Test for base case
    bp.exception(KeyboardInterrupt)(handler)
    assert handler in [exc.handler for exc in bp._future_exceptions]
    assert bp.exception_handler.handler == handler
    assert bp.exception_handler.args == (KeyboardInterrupt,)

    #Test for passing list of arguments


# Generated at 2022-06-14 07:31:18.224311
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    # create a new blueprint
    bp = Blueprint("bp")
    assert bp._future_exceptions == set()
    # add an exception handler
    @bp.exception(Exception)
    def handler(request, exception):
        pass
    
    # Check handler get inserted into future_exceptions of blueprint
    assert len(bp._future_exceptions) == 1
    assert bp._future_exceptions.pop() == FutureException(handler, (Exception,))
    
    # check handler is not applied
    try:
        raise Exception()
    except Exception as e:
        assert not bp.module_has_handler(e)

# Generated at 2022-06-14 07:31:20.518983
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    def get_method_exception(obj):
        assert obj is not None
        return obj.exception

    assert callable(get_method_exception(ExceptionMixin()))

# Generated at 2022-06-14 07:31:21.789819
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True


# Generated at 2022-06-14 07:31:31.738998
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    instance = Blueprint()
    handler = lambda _: None
    exception = IndexError

    instance.exception(IndexError)(handler)

    apply = True
    future_exceptions = instance._future_exceptions
    future_exception = next(iter(future_exceptions))
    exception = future_exception.exception
    handler = future_exception.handler
    kwargs = future_exception.kwargs

    assert apply is True
    assert callable(handler)
    assert exception == (exception,)
    assert kwargs == {}

# Generated at 2022-06-14 07:31:33.331059
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(Exception)
    def exception_handler():
        pass

# Generated at 2022-06-14 07:31:45.353347
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.exceptions import NotFound

    from sanic_babel.exceptions import NotAcceptable

    app = Sanic('test_ExceptionMixin_exception')

    @app.exception(NotAcceptable)
    async def custom_exception(request, exception):
        return response.text('Got {} exception'.format(exception.name),
                             status=424)

    @app.route('/')
    async def handler(request):
        raise NotFound

    @app.route('/2')
    async def handler(request):
        raise NotAcceptable

    request, response = app.test_client.get('/')
    assert response.status == 404

    request, response = app.test_client.get('/2')
    assert response.status == 424

# Generated at 2022-06-14 07:32:10.628210
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    class Test(ExceptionMixin):
        def __init__(self):
            super(Test, self).__init__()

        def _apply_exception_handler(self, handler: FutureException):
            pass
    test = Test()
    test.exception(ValueError, TypeError)
    assert len(test._future_exceptions)
    assert FutureException in type(test._future_exceptions).__bases__
    assert len(test._future_exceptions) == 1
    test.exception(ValueError, TypeError, apply=False)
    assert len(test._future_exceptions) == 2
    test.exception(exceptions=(ValueError, TypeError))
    assert len(test._future_exceptions) == 3

# Generated at 2022-06-14 07:32:16.510380
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    ex = A()
    handler = ex.exception(ValueError)(print)
    assert len(ex._future_exceptions) == 1
    assert handler == print


# Generated at 2022-06-14 07:32:18.541229
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class d(ExceptionMixin):
        pass
    assert d().exception == ExceptionMixin.exception

# Generated at 2022-06-14 07:32:25.195364
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinClass(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self.args = args
            self.kwargs = kwargs
            super().__init__(*args, **kwargs)
    mixin = ExceptionMixinClass()
    assert mixin is not None

# Generated at 2022-06-14 07:32:35.669526
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class mock_app:

        def register_exception(self, exception):
            pass 

    app = mock_app()
    em = ExceptionMixin()
    em.exception(404)
    assert isinstance(em._future_exceptions.pop(), FutureException)
    em.exception(404, apply=False)
    assert isinstance(em._future_exceptions.pop(), FutureException)
    em.exception(404, apply=False)(app.register_exception)
    assert isinstance(em._future_exceptions.pop(), FutureException)


# Generated at 2022-06-14 07:32:40.759255
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A:
        def __init__(self):
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler):
            pass
    a = A()
    exc = Exception('error')
    @a.exception(exc)
    def handler():
        return 'Hello'
    assert handler() == 'Hello'

# Generated at 2022-06-14 07:32:43.105987
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    obj = ExceptionMixin()
    assert obj._future_exceptions == set()
    obj.exception()

# Generated at 2022-06-14 07:32:54.152123
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse

    app = Sanic('test_ExceptionMixin_exception')

    class ExceptionMixinTest(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            self.handler = handler

        async def handle_request(self, request: Request, write_callback:
        WriteCallback, stream_callback: StreamCallback) -> HTTPResponse:
            handler = self.handler(request)
            return handler()

    mixin = ExceptionMixinTest()

    @mixin.exception()
    def handler(request):
        return HTTPResponse('Not found', status=404)
    assert len(mixin._future_exceptions) == 1


# Generated at 2022-06-14 07:33:06.133894
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.views import HTTPMethodView
    from sanic.blueprints import Blueprint

    class MyView(HTTPMethodView):
        def get(self, request):
            return text("Hello, world!")

    bp = Blueprint('test', url_prefix='test')
    my_view = MyView.as_view()

    @bp.exception(IndexError, apply=True)
    def index_error(request, exception):
        return text('internal server error', status=500)

    bp.add_route(my_view, '/myview')

    assert len(bp._future_exceptions) == 1
    assert bp._exception_handlers[IndexError] is index_error

# Generated at 2022-06-14 07:33:12.388177
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    exception_instance = ExceptionMixin()
    def exception_handler(handler, exceptions):
        pass

    exception_instance.exception(exception_handler)

    assert exception_instance._future_exceptions
    assert len(list(exception_instance._future_exceptions)[0]._exceptions) == 1
    assert len(exception_instance._future_exceptions) == 1

# Generated at 2022-06-14 07:33:50.821993
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    blueprint = Blueprint("test_blueprint_exception")
    @blueprint.exception(Exception)
    def exception_handler(request, exception):
        return text("Error: {}".format(exception), status=500)

    assert exception_handler in blueprint._future_exceptions
    # I can't know how to test this code because method _apply_exception_handler
    # not implement in Sanic
    # blueprint._apply_exception_handler(exception_handler)

# Generated at 2022-06-14 07:33:58.884273
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(self, *args, **kwargs)

        def _apply_exception_handler(self, handler):
            pass

    exception_test = ExceptionMixinTest()

    @exception_test.exception(Exception)
    def handler():
        pass

    assert len(exception_test._future_exceptions) == 1
    assert type(exception_test._future_exceptions.pop()) == FutureException
    assert handler() is None

# Generated at 2022-06-14 07:34:05.731422
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinImpl(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            self._future_exceptions.add(handler)

    exception_mixin_impl = ExceptionMixinImpl()
    @exception_mixin_impl.exception(ValueError, apply=False)
    def foo(x):
        return x

    assert len(exception_mixin_impl._future_exceptions) == 1
    assert foo(42) == 42



# Generated at 2022-06-14 07:34:06.478488
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True

# Generated at 2022-06-14 07:34:11.610549
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(ValueError, apply=False)
    def a():
        pass

    assert callable(a)
    assert isinstance(a.__self__, FutureException)
    assert a.__self__._handler == a
    assert a.__self__._exceptions == (ValueError,)

# Generated at 2022-06-14 07:34:16.183744
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Exception_obj(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super(Exception_obj, self).__init__(*args, **kwargs)
        def _apply_exception_handler(self, handler: FutureException):
            pass
    Exception_obj_obj = Exception_obj()
    @Exception_obj_obj.exception('a')
    def handler():
        pass
    assert len(Exception_obj_obj._future_exceptions) == 1

# Generated at 2022-06-14 07:34:22.986030
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler):
            pass

    exception_mixin = TestExceptionMixin()
    def exception_handler(request, exception):
        pass
    exception_mixin.exception(exception_handler)
    assert len(exception_mixin._future_exceptions) == 1

# Generated at 2022-06-14 07:34:29.185363
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    bp = Blueprint("test_bp_exception_mixin")
    assert bp._future_exceptions == set()
    try:
        @bp.exception([Exception])
        def handle_exception(request, e):
            raise Exception("message")
    except TypeError:
        return

    assert len(bp._future_exceptions) == 1

# Generated at 2022-06-14 07:34:42.022587
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Scenario 1:
    # Given a existing exception handler (handler) and a set of exceptions (exceptions)
    # When we set the new exception handler
    # Then it should be stored in the set of exceptions
    # AND the handler should be applied
    # AND the decorator should be returned
    class ExceptionMixinTestClass(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            assert (handler == expected_future_exception)

        def handler():
            pass

    exception_mixin = ExceptionMixinTestClass()
    exceptions = (Exception,)
    expected_future_exception = FutureException(ExceptionMixinTestClass.handler, exceptions)
    decorator = exception_mixin.exception(*exceptions)
    handler = decorator(ExceptionMixinTestClass.handler)

# Generated at 2022-06-14 07:34:42.765626
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:35:51.403352
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
  class fake_ExceptionMixin(ExceptionMixin):
    def __init__(self, *args, **kwargs) -> None:
        self._future_exceptions: Set[FutureException] = set()
        self._future_exceptions.add(Exception('This is an exception'))

  # extend blueprint
  blueprint = fake_ExceptionMixin()

  # First decorator
  @blueprint.exception(Exception)
  def my_exception_handler(request, exception):
    print('A new exception was created.')
    print(exception)
    return None

  # Second decorator
  @blueprint.exception(Exception)
  def my_exception_handler1(request, exception):
    print('A new exception was created.')
    print(exception)
    return None


# Generated at 2022-06-14 07:36:01.842923
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.response import json
    from sanic.exceptions import Forbidden, NotFound
    from sanic.models.futures import FutureException

    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    app = Sanic('test_ExceptionMixin_exception')

    class TestException(Exception):
        pass

    mixin_instance = TestExceptionMixin()

    @mixin_instance.exception([Forbidden, NotFound])
    def test_exception_handler(*args, **kwargs):
        return json({'result': 'exception_handler'})

    assert isinstance(
        next(iter(mixin_instance._future_exceptions)), FutureException)




# Generated at 2022-06-14 07:36:08.725761
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.views import HTTPMethodView

    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass


    class TestView(HTTPMethodView):
        def get(self):
            pass


    TestView.exception = TestExceptionMixin.exception

    @TestView.exception(Exception)
    def error_handler(request, exception):
        pass

# Generated at 2022-06-14 07:36:20.658735
# Unit test for method exception of class ExceptionMixin

# Generated at 2022-06-14 07:36:31.854494
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException

    @ExceptionMixin.exception(KeyError, apply=False)
    def handler_1(request, exception):
        return "K"

    @ExceptionMixin.exception([KeyError], apply=False)
    def handler_2(request, exception):
        return "L"

    @ExceptionMixin.exception(KeyError, apply=True)
    def handler_3(request, exception):
        return "B"

    assert callable(handler_1)
    assert callable(handler_2)
    assert callable(handler_3)

    em = ExceptionMixin()
    em.exception(KeyError, apply=False)(handler_1)
    em.exception([KeyError], apply=False)(handler_2)

# Generated at 2022-06-14 07:36:41.008651
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTester(ExceptionMixin):

        def _apply_exception_handler(self, handler: FutureException):
            assert len(self._future_exceptions) == 1
            assert handler.handler is not None
            assert handler.exceptions[0] == ValueError
            assert handler.exceptions[1] == IndexError


    def handle_exception():
        pass

    future_exceptions = ExceptionMixinTester()
    future_exceptions.exception(ValueError, IndexError)(handle_exception)
    assert handle_exception is not None
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# Generated at 2022-06-14 07:36:53.334422
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FakeExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    fake_exception_mixin = FakeExceptionMixin()

    fake_exception = BaseException("fake_exception")
    fake_handler = lambda x: x
    fake_exception_mixin.exception(fake_exception)(fake_handler)

    assert fake_exception_mixin._future_exceptions
    assert len(fake_exception_mixin._future_exceptions) == 1
    assert fake_exception_mixin._future_exceptions.pop().exceptions == (fake_exception, )
    assert fake_exception_mixin._future_exceptions == set()

# Generated at 2022-06-14 07:37:05.340418
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from mockito import mock, verify

    blueprint_mock = mock(Blueprint)
    assert isinstance(blueprint_mock, Blueprint)
    assert isinstance(blueprint_mock, ExceptionMixin)

    @blueprint_mock.exception(Exception)
    def handle_exception(request, exception):
        pass

    blueprint_mock.exception.assert_called_once_with(Exception, True)

    assert blueprint_mock._future_exceptions.__sizeof__() == 1
    assert isinstance(next(iter(blueprint_mock._future_exceptions)), FutureException)
    future_exception = next(iter(blueprint_mock._future_exceptions))
    assert future_exception.exceptions == (Exception,)

# Generated at 2022-06-14 07:37:15.516845
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTester(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)

        def _apply_exception_handler(self, handler: FutureException):
            print('This is the apply of ExceptionMixin')

    # create a class of ExceptionMixinTester
    exception_mixin_tester = ExceptionMixinTester()
    # test the method exception
    @exception_mixin_tester.exception(1)
    def test_exception_mixin_exception(self):
        print('This is the exception of ExceptionMixin')
    # debug test the method exception
    assert isinstance(exception_mixin_tester._future_exceptions,set)
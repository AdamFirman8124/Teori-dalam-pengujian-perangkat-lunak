

# Generated at 2022-06-14 07:27:21.784022
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    blueprint = Blueprint('test_bp', url_prefix='/test_bp')
    blueprint.exception(ZeroDivisionError)(lambda x, y: x/y)

    assert isinstance(blueprint, ExceptionMixin)
    assert isinstance(blueprint, Blueprint)

# Generated at 2022-06-14 07:27:30.223075
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.exceptions import SanicException, NotFound

    class ExceptionClass(SanicException):
        pass

    app = Sanic(__name__)

    @app.exception(ExceptionClass)
    async def all_exceptions_handler(request, exception):
        pass

    @app.exception(ExceptionClass, NotFound)
    async def custom_exceptions_handler(request, exception):
        pass

    @app.exception(NotFound)
    async def not_found_exception_handler(request, exception):
        pass

    assert len(app.exception_handlers) == 3

# Generated at 2022-06-14 07:27:47.508010
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.applied = None

        def _apply_exception_handler(self, handler: FutureException):
            # pylint: disable=attribute-defined-outside-init
            self.applied = handler

    test_exception_mixin = TestExceptionMixin()

    def decorator(handler):
        return handler

    @test_exception_mixin.exception(ValueError, apply=False)
    def exception_handler():
        pass

    assert(len(test_exception_mixin._future_exceptions) == 1)
    assert(isinstance(exception_handler, decorator))

# Generated at 2022-06-14 07:27:55.157765
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_instance(ExceptionMixin):
        def __init__(self):
            super().__init__()
        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError
    exceptionmixin_instance = ExceptionMixin_instance()
    def handler():
        return "handler"
    # Call method decorator of decorator exception
    result = exceptionmixin_instance.exception(ZeroDivisionError, apply=True)(handler)
    assert result == 'handler'
    assert isinstance(exceptionmixin_instance._future_exceptions, set)
    assert len(exceptionmixin_instance._future_exceptions) == 1
    future_exception = next(iter(exceptionmixin_instance._future_exceptions))
    assert future_exception.handler == handler

# Generated at 2022-06-14 07:27:59.698111
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    bp = ExceptionMixin()
    @bp.exception(RuntimeError, apply=False)
    def handler():
        pass
    future_exception = bp._future_exceptions.pop()
    assert future_exception.handler == handler
    assert future_exception.exception_types == (RuntimeError,)

# Generated at 2022-06-14 07:28:11.474449
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import exceptions

    from sanic.exceptions import add_exception_handler
    from sanic.blueprints import Blueprint
    import asyncio
    from sanic import request
    from sanic.response import text as resp

    blueprint = Blueprint('test_ExceptionMixin_exception')
    blueprint.exception(exceptions.NotFound, apply=True)(lambda a, b: print(a, b))  # noqa
    blueprint.exception(exceptions.NotFound, apply=True)(lambda a, b: print(a, b))  # noqa

    bp = Blueprint('test_ExceptionMixin_exception')
    bp.exception(exceptions.NotFound, apply=True)(lambda a, b: print(a, b))  # noqa

# Generated at 2022-06-14 07:28:21.665750
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class SomeClass(ExceptionMixin):
        pass

    some_class = SomeClass()
    handler = lambda x: "Some handler"

    assert not some_class._future_exceptions
    some_class.exception(ValueError)
    assert not some_class._future_exceptions

    # def _apply_exception_handler(self, handler: FutureException):
    # raise NotImplementedError  # noqa
    #     with pytest.raises(NotImplementedError) as e_info:
    #         some_class.exception(handler=handler)
    #     assert "not all arguments converted during string formatting" in str(e_info.value)
    #     assert "not all arguments converted during string formatting" in str(e_info.value)
    # def _apply_exception_handler(self, handler:

# Generated at 2022-06-14 07:28:28.692820
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            super(TestExceptionMixin, self).__init__()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_obj = TestExceptionMixin()
    assert(not test_obj._future_exceptions)

    # decorator
    @test_obj.exception()
    def test_decorator():
        pass

    assert(not test_obj._future_exceptions)
    test_obj.exception()(test_decorator)
    assert(test_obj._future_exceptions)

# Generated at 2022-06-14 07:28:38.560503
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    '''Test for method exception of class ExceptionMixin'''
    from sanic.blueprints import Blueprint

    bp = Blueprint('test',url_prefix='test')

    @bp.exception(Exception)
    async def test(request, exception):
        return response.text('Ive got an Exception!')

    assert(bp._future_exceptions.__len__()==1)
    assert(bp._future_exceptions.pop().handler.__name__ == "test")

    bp.exception(Exception)('add another exception')
    assert(bp._future_exceptions.__len__()==1)
    assert(bp._future_exceptions.pop().handler=='add another exception')

# Generated at 2022-06-14 07:28:45.755264
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    blueprint = ExceptionMixin()
    blueprint.__init__()
    blueprint._apply_exception_handler = lambda handler: None

    @blueprint.exception(Exception, apply=False)
    def handler():
        print('An exception has occurred')

    assert isinstance(handler, types.FunctionType)
    assert isinstance(blueprint._future_exceptions.pop(), FutureException)

# Generated at 2022-06-14 07:28:56.235178
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.views import HTTPMethodView
    from sanic import Sanic
    from sanic.exceptions import ServerError

    class TestView(HTTPMethodView):
        def get(self, request):
            raise ServerError("Some exception happened.", status_code=500)

    test_app = Sanic("test_ExceptionMixin_exception")

    @test_app.exception(ServerError)
    def handler(request, exception):
        return text("Oops! Something went wrong!")

    test_view = TestView.as_view()
    test_bp = Blueprint("test_bp")
    test_bp.validate_on_headers = True
    test_bp.add_route(test_view, "/")


# Generated at 2022-06-14 07:28:56.943597
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:28:59.816208
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    #TODO: This test has not been written yet, check out the test coverage
    # document in docs/tests/testing-coverage.md
    pass

# Generated at 2022-06-14 07:29:03.459879
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTester(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    tester = ExceptionMixinTester()
    try:
        @tester.exception(Exception)
        def handler(request, exception):
            raise Exception()
    except Exception:
        pass

# Generated at 2022-06-14 07:29:16.157763
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ClasseExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            print(handler)

    # Cas nominal
    objet = ClasseExceptionMixin()
    objects = {"objet": objet}

    def valid_exception_handler():
        print("Handler")

    def valid_exception_handler_2():
        print("Handler 2")

    objet.exception(ValueError, KeyError)(valid_exception_handler)
    objet.exception(ValueError, KeyError)(valid_exception_handler_2)
    assert len(objet._future_exceptions) == 2
    # Cas d'erreur: ExceptionHandlerException()

# Generated at 2022-06-14 07:29:25.586268
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.response import json
    from sanic.blueprints import Blueprint

    # Case 1: Global exception handling
    app = Sanic(__name__)
    blueprint = Blueprint("b1_1")

    @blueprint.exception(ZeroDivisionError, apply=True)
    def handler(request, exception):
        return json("Exception happened", status=500)

    blueprint.add_exception(ZeroDivisionError, handler, apply=True)

    @blueprint.route("/")
    def handler(request):
        return json("Test")

    app.blueprint(blueprint)

    # Case 2: Exception handling by route
    app = Sanic(__name__)
    blueprint = Blueprint("b1_2")


# Generated at 2022-06-14 07:29:26.182923
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:29:30.545713
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class Foo(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    foo = Foo()
    foo.exception(IndexError)(lambda x: x)
    assert(len(foo._future_exceptions) == 1)
    assert(IndexError in foo._future_exceptions.pop().exceptions)

# Generated at 2022-06-14 07:29:37.779485
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_exception(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    ex = ExceptionMixin_exception()
    assert len(ex._future_exceptions) == 0
    assert len(ex.exception(None)(test_ExceptionMixin_exception)._future_exceptions) == 1

# Generated at 2022-06-14 07:29:44.250047
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # initialize a blueprint
    blueprint = Blueprint('test bp')
    try:
        # create a exception handler
        @blueprint.exception(apply = True)
        def exception_handler(request, exception):
            pass
        assert len(blueprint._future_exceptions) == 1
        print('ExceptionMixin exception test passed')
    except:
        print('ExceptionMixin exception test failed')



# Generated at 2022-06-14 07:29:51.765260
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    bp = Blueprint('my_blueprint', url_prefix='/test_url_prefix')

    assert len(bp._future_exceptions) == 0

    @bp.exception(ValueError)
    def handle_exception(request, exception):
        print('Hello')

    assert len(bp._future_exceptions) == 1



# Generated at 2022-06-14 07:30:03.274915
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class BlueprintStub(ExceptionMixin):
        def __init__(self):
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler):
            pass
    blueprint = BlueprintStub()

    @blueprint.exception(ValueError)
    def handler():
        pass

    assert len(blueprint._future_exceptions) == 1
    future_exception = list(blueprint._future_exceptions)[0]
    assert future_exception
    assert future_exception.handler is handler
    assert (ValueError,) == future_exception.exceptions

    @blueprint.exception([ValueError, FileNotFoundError])
    def handler():
        pass

    assert len(blueprint._future_exceptions) == 2

# Generated at 2022-06-14 07:30:09.746879
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FakeMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            self._handler = handler

    class FakeException(Exception):
        def __init__(self):
            super().__init__()

    mixin = FakeMixin()
    mixin.exception(Exception)
    assert len(mixin._future_exceptions) == 1
    assert mixin._future_exceptions.pop().handler is None

    test_func = lambda a: a
    mixin = FakeMixin()
    mixin.exception(FakeException)(test_func)
    assert len(mixin._future_exceptions) == 1
    assert mixin._future_exceptions.pop().handler == test_func



# Generated at 2022-06-14 07:30:20.306489
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def apply_exception_handler(handler):
        handler(Exception)

    class Fake(ExceptionMixin):
        def __init__(self):
            super(Fake, self).__init__()

        def _apply_exception_handler(self, handler):
            apply_exception_handler(handler)

    fake = Fake()
    assert len(fake._future_exceptions) == 0

    @fake.exception(Exception)
    def exception_handler(request, exception): pass

    assert len(fake._future_exceptions) == 1
    exception_handler = fake._future_exceptions.pop()

    with pytest.raises(Exception):
        exception_handler(Exception)

    exception_handler.handler(Exception)

# Generated at 2022-06-14 07:30:21.661261
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:30:29.493076
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    from sanic.models.exception import exception
    from sanic.models.futures import FutureException
    from sanic.router import RouteExists

    @exception(Exception, ValueError)
    async def error_handler(error, request):
        pass

    blueprint = Blueprint("blueprint_test_exception", url_prefix="/test")
    assert blueprint._exception_handlers == {}
    blueprint.exception(Exception, ValueError)(error_handler)
    assert blueprint._exception_handlers == {(Exception, ValueError): error_handler}
    assert blueprint._exception_handlers == {(Exception, ValueError): error_handler}
    assert blueprint._apply_exception_handler(FutureException(error_handler, (Exception, ValueError))) == RouteExists
    assert blueprint._exception_

# Generated at 2022-06-14 07:30:42.151594
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic

    app = Sanic('test_ExceptionMixin_exception')

    class MyExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler):
            pass

    class ExceptionSanic(MyExceptionMixin, Sanic):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    app = ExceptionSanic('test_ExceptionMixin_exception')

    @app.exception(Exception)
    def test_exception(request, exception):
        return text('OK')

    request, response = app.test_client.get('/test')

# Generated at 2022-06-14 07:30:46.882798
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            print(handler)

    mixin = MyExceptionMixin()
    @mixin.exception()
    def handler():
        pass

# Generated at 2022-06-14 07:30:58.586754
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint

    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    bp = Blueprint("test", url_prefix="/test")
    t = TestExceptionMixin()

    @t.exception(ValueError)
    def exception_handler(request, exception):
        raise NotImplementedError  # noqa

    @bp.route("/")
    def handler(request):
        return "ok"

    assert len(t._future_exceptions) > 0

# Generated at 2022-06-14 07:31:10.521932
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprints import Blueprint

    @Blueprint.exception(KeyError)
    def handler_KeyError(request, exception):
        raise NotImplementedError

    @Blueprint.exception([KeyError, ValueError])
    def handler_KeyOrValueError(request, exception):
        raise NotImplementedError

    assert Blueprint.exception(KeyError)(handler_KeyError) == handler_KeyError

    for future_exception in Blueprint._future_exceptions:
        assert isinstance(future_exception, FutureException)
        assert future_exception.exceptions == (KeyError,)
        assert future_exception.handler == handler_KeyError

    assert Blueprint.exception([KeyError, ValueError])(handler_KeyOrValueError) == handler_KeyOrValueError


# Generated at 2022-06-14 07:31:21.155698
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def handler(a):
        return a
    class TestExceptionMixin(ExceptionMixin):
        pass
    assert TestExceptionMixin.exception(1) == decorator

# Generated at 2022-06-14 07:31:31.305129
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprints import Blueprint
    from sanic.exceptions import SanicException, NotFound

    assert issubclass(SanicException, Exception)
    assert issubclass(NotFound, SanicException)

    blueprint = Blueprint('test', url_prefix='/test')
    blueprint.exception(SanicException)(print)
    blueprint.exception(NotFound)(print)

    assert blueprint._future_exceptions

    blueprint._apply_exception_handler(blueprint._future_exceptions.pop())
    blueprint._apply_exception_handler(blueprint._future_exceptions.pop())

    assert not blueprint._future_exceptions

# Generated at 2022-06-14 07:31:43.468290
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test case of just one Exception
    test_ExceptionMixin = ExceptionMixin
    def test_handler():
        raise Exception("Handler Exception")
    test_ExceptionMixin.exception(Exception)(test_handler)
    assert isinstance(Exception, test_handler)
    # Test case of few Exceptions
    def test_handler1():
        raise Exception("Handler Exception")
    test_ExceptionMixin.exception(Exception, Exception)(test_handler1)
    assert isinstance(Exception, test_handler1)
    # Test case of few Exceptions in List
    def test_handler2():
        raise Exception("Handler Exception")
    test_ExceptionMixin.exception(Exception, [Exception, Exception])(test_handler2)
    assert isinstance(Exception, test_handler2)

# Generated at 2022-06-14 07:31:52.778443
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            ExceptionMixin.__init__(self, *args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    a = A()
    assert len(a._future_exceptions) == 0

    @a.exception(Exception)
    def handler(request, exception):
        return exception

    assert len(a._future_exceptions) == 1
    assert a._future_exceptions.pop().exceptions == (Exception,)
    assert handler(None, Exception) == Exception

# Generated at 2022-06-14 07:31:53.519924
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True

# Generated at 2022-06-14 07:32:00.645247
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def decorated_function():
        pass
    args = (Exception, )
    kwargs = {'test': 'test'}
    
    exception_mixin = ExceptionMixin()
    exception_result = exception_mixin.exception(*args, **kwargs)(decorated_function)
    
    assert isinstance(exception_result, types.FunctionType), "The result of the exception method is not a function"

# Generated at 2022-06-14 07:32:07.590946
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest:
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa
    testInstance = ExceptionMixinTest()
    assert(testInstance != None)
    try:
        testInstance.exception([Exception])()
        assert(False)
    except NotImplementedError:
        assert(True)

# Generated at 2022-06-14 07:32:16.146166
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def __init__(self):
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

        def get_exception_handler(self):
            return self._future_exceptions

    @Blueprint.exception(Exception)
    def future_exception_handler(request, exception):
        pass

    r = Blueprint()
    r._apply_exception_handler(r.get_exception_handler())

    assert len(r.get_exception_handler()) == 1

# Generated at 2022-06-14 07:32:20.019328
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    my_exception_mixin = MyExceptionMixin()

    @my_exception_mixin.exception(BaseException)
    def handler():
        pass

    assert handler == my_exception_mixin._future_exceptions.pop().handler

# Generated at 2022-06-14 07:32:28.416139
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprints import SanicBlueprint
    from sanic.response import text
    from sanic.views import HTTPMethodView
    from sanic.exceptions import SanicException

    class HttpMethodView(HTTPMethodView):
        pass

    blueprint = SanicBlueprint(__name__, url_prefix='/blueprint')
    blueprint.exception(SanicException)(text)

    @blueprint.route('/test')
    def test():
        raise SanicException('test')


# Generated at 2022-06-14 07:32:43.684861
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:32:49.925810
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.response import json

    # set exception handler for blueprint
    app = Sanic(__name__)

    @app.exception(Exception, apply=False)
    def error_handler(request, exception):
        """Handle all the exceptions!"""
        return json({"status": 404, "message": "exception"})

    @app.get("/error")
    async def error(request):
        raise Exception("error")

    # test exception handler
    request, response = app.test_client.get("/error")
    assert response.status == 404
    assert response.json == {"status": 404, "message": "exception"}

# Generated at 2022-06-14 07:33:01.874213
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.blueprints import Blueprint
    import traceback

    def handler(request, exception):
        if request == 'test':
            if exception == 1:
                return 'test1'
        return 'test2'
    
    app = Sanic('test_ExceptionMixin')
    bp = Blueprint('test_ExceptionMixin', url_prefix='test')
    bp.exception(handler)('Exception')

    try:
        assert bp._future_exceptions[0].exception == 'Exception'
        assert bp._future_exceptions[0].handler == handler
    except Exception as e:
        print(traceback.format_exc())

test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:33:11.224773
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.isApply = False
            self.exceptions = None

        def _apply_exception_handler(self, handler: FutureException):
            self.exceptions = handler.exceptions
            self.isApply = True

    def handler(arg):
        pass

    def handler2(arg):
        pass

    a = A()
    a.exception(ValueError, apply=True)(handler)
    assert a.isApply == True
    assert a.exceptions == (ValueError,)
    assert handler in a._future_exceptions

    a.exception([ValueError, AttributeError, SystemError], )(handler2)
    assert handler2 in a._future_exceptions
    assert a.isApply == False

# Generated at 2022-06-14 07:33:19.342735
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    mixin = ExceptionMixin()
    assert not hasattr(mixin, '_exception')
    # Test decorator
    @mixin.exception()
    def handler():
        pass
    assert hasattr(mixin, '_exception')
    mixin._apply_exception_handler = MagicMock()
    mixin._exception()
    assert mixin._apply_exception_handler.called

# Generated at 2022-06-14 07:33:24.154576
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    Unit test for the method exception of class ExceptionMixin
    """
    class Test(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            return handler

    test = Test()
    assert test.exception


# Generated at 2022-06-14 07:33:28.975988
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Arrange
    # Act
    instance = ExceptionMixin()
    handler = instance.exception(handler)

    # Assert
    # TODO: verify add_exception_handler
    # instance.add_exception_handler.assert_called_once_with(handler, None)

# Generated at 2022-06-14 07:33:33.120025
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyBlueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    MyBlueprint.exception(Exception)(lambda x: print(x))

# Generated at 2022-06-14 07:33:41.163419
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def exception_handler(request, exception):
        print("Exception catched!")
    
    class DummyModel(ExceptionMixin):
        pass
    
    dummy = DummyModel()

    dummy.exception(IndexError)(exception_handler)

    future_exceptions_list = list(dummy._future_exceptions)
    future_exception = future_exceptions_list[0]

    assert exception_handler == future_exception.handler
    assert (IndexError,) == future_exception.exceptions

# Generated at 2022-06-14 07:33:53.130668
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    blueprint = Blueprint()
    blueprint_name = 'test_ExceptionMixin_exception'

    def exception_handler_1(request, exception):
        pass

    def exception_handler_2(request, exception):
        pass

    blueprint.exception(ValueError)(exception_handler_1)

    blueprint.exception(IndexError)(exception_handler_2)

    assert len(blueprint._future_exceptions) == 2
    assert (exception_handler_2, (IndexError,)) in blueprint._future_exceptions
    assert (exception_handler_1, (ValueError,)) in blueprint._future_exceptions

# Generated at 2022-06-14 07:34:26.786799
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    import inspect

    blueprint = Blueprint("test")
    assert blueprint._future_exceptions == set()
    assert blueprint.exception is ExceptionMixin.exception
    assert inspect.ismethod(blueprint.exception)

# Generated at 2022-06-14 07:34:35.427527
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler):
            self._handler = handler
    # Test whether exception returns a decorator
    test_exception_mixin = TestExceptionMixin()
    @test_exception_mixin.exception(AssertionError)
    def handler():
        return "Test"
    assert handler() == "Test"
    # Test whether self._future_exceptions is set
    assert len(test_exception_mixin._future_exceptions) == 1
    # Test whether _apply_exception_handler is called
    assert test_exception_mixin._handler.handler() == "Test"
    # Test whether exceptions can be passed in tuple
    test_exception_mix

# Generated at 2022-06-14 07:34:38.404251
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_test(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            return handler
    obj = ExceptionMixin_test()
    assert obj.exception(ValueError)

# Generated at 2022-06-14 07:34:50.172069
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    import cProfile
    import time
    from sanic.models.exceptions import SanicException
    from sanic.models.futures import FutureException
    from sanic.models.blueprint import Blueprint

    class testExceptionMixin(unittest.TestCase):
        def setUp(self):
            # Runs before each test
            self.blueprint = Blueprint("test", url_prefix="/test")

        def tearDown(self):
            # Runs after each test
            del self.blueprint

        def test_exception(self):
            # Testing exception(apply = True) with exception SanicException
            def exception_handler(request, exception):
                return request, exception


# Generated at 2022-06-14 07:34:54.616781
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.future import Future

    future_exception = FutureException
    fm = ExceptionMixin()
    assert fm._future_exceptions == set()
    assert isinstance(fm.exception(None), Future)

# Generated at 2022-06-14 07:34:58.425066
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint("test", url_prefix="/test")
    bp.exception(Exception)
    assert len(bp._future_exceptions) == 1

# Generated at 2022-06-14 07:35:01.736418
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestClass(ExceptionMixin):
        pass

    test = TestClass()
    assert test._future_exceptions
    assert type(test._future_exceptions) == set
    
    test.exception
    assert not test._future_exceptions

# Generated at 2022-06-14 07:35:07.955231
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class fake_param(ExceptionMixin):
        def __init__(self, *args):
            self.args = args
    param = fake_param()
    @param.exception(Exception)
    def fake_func():
        return True
    assert fake_func() == True
    assert param.args == ()

# Generated at 2022-06-14 07:35:20.232512
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    from sanic.handlers import ErrorHandler

    mock_app = Sanic("ExceptionMixin Test")
    blueprint = Blueprint("ExceptionMixin Test", url_prefix="/")

    @blueprint.exception(ValueError, apply=False)
    def exception_handler():
        return "exception handled!"

    assert len(blueprint._future_exceptions) == 1

    # Test adding exception handler with ErrorHandler
    @blueprint.listener("after_server_start")
    async def add_exception_handlers(app: Sanic, loop):
        assert len(app.error_handler.handlers) == 0
        assert len(blueprint._future_exceptions) == 1
        assert isinstance(app.error_handler, ErrorHandler)

        #

# Generated at 2022-06-14 07:35:27.287806
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint(__name__,url_prefix='test')
    @bp.exception(Exception)
    def handler(request, exception):
        return request, exception
    assert len(bp._future_exceptions) == 1
    assert bp._future_exceptions.pop().handler == handler

# Generated at 2022-06-14 07:36:37.286346
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic import Sanic
    from sanic.response import json

    app = Sanic("test_ExceptionMixin_exception")
    bp = Blueprint("test_ExceptionMixin_exception_bp")

    @bp.route("/")
    def handler(request):
        return json({"test": True})

    @bp.exception(Exception)
    def error_handler(request, exception):
        return json({"error": True}, status=500)

    app.blueprint(bp)

    _, response = app.test_client.get("/")
    assert response.status == 500



# Generated at 2022-06-14 07:36:38.071886
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:36:41.326892
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    blueprint: Blueprint = Blueprint(name="bp_exceptionmixin", url_prefix="/bp_exceptionmixin")
    blueprint.exception([RuntimeError])("exception")

# Generated at 2022-06-14 07:36:44.135234
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    '''Test method exception of class ExceptionMixin'''



# Generated at 2022-06-14 07:36:44.862405
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:36:50.983958
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def _test_ExceptionMixin_exception(exec_type: str, expected_result: int):
        class TestExceptionMixin(ExceptionMixin):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(*args, **kwargs)
                self._exception_count = 0

            def _apply_exception_handler(self, handler: FutureException):
                self._exception_count += 1

        def f1():
            raise Exception

        ex = TestExceptionMixin()
        if exec_type == 'all':
            @ex.exception(Exception)
            def error_handler(request, exception):
                pass
        elif exec_type == 'many':
            @ex.exception([Exception, RuntimeError])
            def error_handler(request, exception):
                pass


# Generated at 2022-06-14 07:36:54.552715
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(TypeError)
    def handler(request, response):
        pass

    
    assert issubclass(handler.exceptions[0], TypeError)

# Generated at 2022-06-14 07:37:04.330864
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test with apply=True
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            return handler

    test_mixin_object = TestExceptionMixin()
    test_mixin_object.exception(TypeError)(func)

    # Test with apply=False
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            return handler

    test_mixin_object = TestExceptionMixin()
    test_mixin_object.exception(TypeError, apply=False)(func)



# Generated at 2022-06-14 07:37:13.038353
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)

        def _apply_exception_handler(self, handler: FutureException):
            self._handler = handler

    test = TestExceptionMixin()
    assert not test._future_exceptions

    @test.exception(Exception)
    def test():
        pass

    assert test.__class__.test is test._handler.handler
    assert issue9403 in test._future_exceptions

root = pathlib.Path(__file__).parent.parent.parent

sys.path.append(str(root))

# Generated at 2022-06-14 07:37:18.582857
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic

    app = Sanic('test_ExceptionMixin_exception')

    @ExceptionMixin.exception(Exception)
    def handler(request, exception):
        return text('OK')

    assert handler.__name__ == 'handler'
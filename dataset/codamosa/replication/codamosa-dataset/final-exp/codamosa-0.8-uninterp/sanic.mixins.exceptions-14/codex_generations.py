

# Generated at 2022-06-14 07:27:05.492554
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True == True
    # TODO: Unit test exception method
    pass

# Generated at 2022-06-14 07:27:10.866164
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Test(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    @Test.exception(TypeError, KeyError)
    def handler(request, exception):
        pass
    assert len(Test._future_exceptions) == 1
    assert isinstance(Test._future_exceptions.pop(), FutureException)

# Generated at 2022-06-14 07:27:22.990755
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Users(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

    class Root(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

    @Root.exception(Exception)
    def test_exception(request, exception):
        pass

    assert len(Root._future_exceptions) == 1

    @Users.exception(Exception)
    def test_exception(request, exception):
        pass

    assert len(Root._future_exceptions) == 1
    assert len(Users._future_exceptions) == 1

# Generated at 2022-06-14 07:27:25.947227
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_impl(ExceptionMixin):
        def __init__(self):
            super().__init__()
            
    ExceptionMixin_impl().exception(Exception)(lambda exc: None)

# Generated at 2022-06-14 07:27:34.958622
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.models.futures import FutureException

    app = Sanic()
    setattr(app, '_future_exceptions', set())

    def _apply_exception_handler(handler: FutureException):
        pass

    setattr(app, '_apply_exception_handler', _apply_exception_handler)

    app.exception(IndexError)
    assert app._future_exceptions != set()
    assert app._future_exceptions != None

# Generated at 2022-06-14 07:27:47.627503
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.response import text
    from sanic.models.futures import FutureException

    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self._future_exceptions = set()
            self._exception_handlers = {}

        def _apply_exception_handler(self, handler: FutureException):
            self._exception_handlers[handler.exceptions[0]] = handler

    app = Sanic('test_ExceptionMixin_exception')
    app.blueprint(TestExceptionMixin())

    @app.exception(Exception, apply=False)
    def handle_exception(request, exception):
        return text('internal server error', status=500)


# Generated at 2022-06-14 07:27:55.844342
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # arrange
    class SanicMock:
        def add_exception(self, exception):
            pass

    class ExceptionMixinMock():
        _future_exceptions = set()
        _sanic = SanicMock()
        def __init__(self):
            pass

        def _apply_exception_handler(self, handler: FutureException):
            self._sanic.add_exception(handler)

    # act
    instance = ExceptionMixinMock()

    @instance.exception(apply=True)
    def handler():
        pass

# Generated at 2022-06-14 07:28:00.676596
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MockException(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    mock_exception = MockException()

    @mock_exception.exception(Exception) # noqa
    def hello(request):
        return "No problem here"

    assert len(mock_exception._future_exceptions) == 1

# Generated at 2022-06-14 07:28:12.807688
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class ExceptionMixin_test(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.apply = False

        def _apply_exception_handler(self, handler: FutureException):
            self.apply = True

    # 测试decorator_test
    exception_mixin_test = ExceptionMixin_test()
    decorator_test = exception_mixin_test.exception(Exception)
    handler = lambda request, exception: None
    assert decorator_test == handler

    # 测试两个请求的object id值是否相等
    decorator_test = exception_mixin_test.exception(Exception, apply=False)
   

# Generated at 2022-06-14 07:28:18.546423
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinClass(ExceptionMixin):

        async def _apply_exception_handler(self, handler: FutureException):
            pass

    exceptions = ExceptionMixinClass()
    handler = objects.function()
    args = [Exception]
    kwargs = {'apply': True}
    result = exceptions.exception(*args, **kwargs)(handler)
    assert result is handler
    assert len(exceptions._future_exceptions) == 1

# Generated at 2022-06-14 07:28:25.801761
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    The method exception of class ExceptionMixin returns the decorated method to handle global exceptions for any route registered under this blueprint.
    """
    test_class = ExceptionMixin()
    def custom_method():
        return 'test_value'
    
    assert test_class.exception(custom_method)() == 'test_value'

# Generated at 2022-06-14 07:28:26.520496
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:28:32.885991
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Sanic(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    global a
    a = 0
    s = Sanic()
    @s.exception(Exception)
    def global_exception_handler(request, exception):
        global a
        a += 1
    global_exception_handler(None, None)
    assert a == 1

# Generated at 2022-06-14 07:28:39.907132
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exception_mixin = ExceptionMixin()
    assert exception_mixin._future_exceptions == set()

    def handler_method(request, exception):
        pass

    exception_mixin.exception(handler_method)

    assert len(exception_mixin._future_exceptions) == 1

    def handler_method(request, exceptions):
        pass

    exception_mixin.exception(handler_method, [BaseException])

    assert len(exception_mixin._future_exceptions) == 1

# Generated at 2022-06-14 07:28:47.603753
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super(ExceptionMixinTest, self).__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler):
            pass

    test = ExceptionMixinTest()
    assert test._future_exceptions == set()
    assert test.exception(RuntimeError)

# Generated at 2022-06-14 07:28:56.234887
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import InvalidUsage
    from sanic.models.futures import FutureException

    expected_exception = FutureException(
        "dummy_method", (InvalidUsage,).__class__)

    class Dummy(ExceptionMixin):
        def __init__(self):
            super(Dummy, self).__init__()
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler):
            assert handler == expected_exception

    dummy_obj = Dummy()
    dummy_bp = Blueprint("dummy_bp", url_prefix="/dummy_prefix")

    @exception(InvalidUsage)
    async def dummy_method():
        return "dummy_method"

    # This will raise an error because apply=False
   

# Generated at 2022-06-14 07:29:02.197198
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MockBlueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    bp = MockBlueprint()

    @bp.exception(Exception)
    def exception_handler(request, exception):
        pass

    assert len(bp._future_exceptions) == 1
    assert isinstance(bp._future_exceptions.pop(), FutureException)

# Generated at 2022-06-14 07:29:11.141001
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super(TestExceptionMixin, self).__init__(*args, **kwargs)

    def dummy_handler():
        pass
    test_exceptionMixin = TestExceptionMixin()
    
    test_exceptionMixin.exception(RuntimeError)(dummy_handler)
    assert test_exceptionMixin._future_exceptions == {FutureException(dummy_handler, (RuntimeError,))}

# Generated at 2022-06-14 07:29:15.336312
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A:
        @exception
        def test(self):
            return "Excepcion"
    a = A()
    a.test()
    assert a.test() == "Excepcion"
# ----------------------------------------------------------------------------------------------------------------------

# Generated at 2022-06-14 07:29:25.200090
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    Unit test for method exception of class ExceptionMixin
    """

    import unittest
    from sanic.models.futures import FutureException
    from sanic.app import Sanic
    from sanic import Blueprint

    class ExceptionMixinTests(unittest.TestCase):
        def test_exception(self):
            """
            Test if method exception of class ExceptionMixin works properly.
            """

            bp = Blueprint('test_bp')
            bp.exception(ZeroDivisionError)(lambda _: None)
            self.assertEqual(len(bp._future_exceptions), 1)
            self.assertIsInstance(list(bp._future_exceptions)[0], FutureException)

    suite = unittest.TestLoader().loadTestsFromModule(ExceptionMixinTests())

# Generated at 2022-06-14 07:29:35.321775
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    Unit test for exception method of ExceptionMixin.

    When the exception method is called, it returns a decorator.

    When the decorator is called, no matter what parameters are passed in,
    a FutureException is added to the blueprint.

    The blueprint we use here is made specially for this unit test, it
    inherits from the ExceptionMixin.
    """
    from sanic.models.future import FutureException

    class TestBluePrint(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass

    test = TestBluePrint()

    @test.exception(NotImplementedError)
    def handler(request, exception):
        pass

    @test.exception(KeyError, apply=False)
    def handler2(request, exception):
        pass


# Generated at 2022-06-14 07:29:36.668979
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert ExceptionMixin.exception('ExceptionMixin')

# Generated at 2022-06-14 07:29:46.398085
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.models.base import BaseContainer
    from sanic.models.futures import FutureException

    class ExceptionMixinTest(ExceptionMixin,BaseContainer):
        pass

    app = Sanic('test_ExceptionMixin_exception')
    my_blueprint = ExceptionMixinTest(app=app)

    def test_handler():
        pass

    my_blueprint.exception(test_handler)
    assert isinstance(my_blueprint._future_exceptions.pop(), FutureException)
    assert isinstance(
        my_blueprint._future_exceptions.pop(), FutureException) == False

# Generated at 2022-06-14 07:29:56.695743
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FakeBlueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    fb = FakeBlueprint()
    def fake_handler(self, req, exc):
        pass

    # list as exceptions
    fb.exception([ValueError, KeyError])(fake_handler)
    assert len(fb._future_exceptions) == 1
    assert ValueError in fb._future_exceptions.pop().exceptions
    assert KeyError in fb._future_exceptions.pop().exceptions

    # multiple exception as arguments
    fb.exception(ValueError, KeyError)(fake_handler)
    assert len(fb._future_exceptions) == 1
    assert ValueError in fb._future_exceptions.pop().exceptions
    assert KeyError in fb._future_

# Generated at 2022-06-14 07:30:02.802023
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest

    class TestBlueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass


    blueprint = TestBlueprint()

    @blueprint.exception(attr="attr", apply=True)
    def exception_handler():
        pass


    assert blueprint._future_exceptions



# Generated at 2022-06-14 07:30:12.798555
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ClassWithException(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
            self._register_apply_exception_handler_method(self._apply_exception_handler)
    
    # test with args
    @ClassWithException.exception(IndexError)
    def test_function1(request, exception, *args, **kwargs):
        raise Exception(exception)
    # test with args and apply=True
    @ClassWithException.exception(IndexError, apply=True)
    def test_function2(request, exception, *args, **kwargs):
        raise Exception(exception)
    # test with args and apply=False

# Generated at 2022-06-14 07:30:16.042307
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    instance = ExceptionMixin()
    assert isinstance(instance.exception, object)
    assert callable(instance.exception)

# Generated at 2022-06-14 07:30:25.455575
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprint import Blueprint
    from sanic.models.futures import FutureException

    # Define a dummy blueprint:
    blueprint = Blueprint('exception_mixin_blueprint', url_prefix='/')

    # Create a dummy exception class:
    class CustomFakeException(Exception):
        pass

    # Define a dummy handler method:
    def dummy_handler(request, exception):
        return response.text('Exception handled!')

    exception_handler = blueprint.exception([CustomFakeException])(dummy_handler)

    assert dummy_handler == exception_handler

    # Check that the dummy handler method has been added to the list
    # of future exception handlers:
    assert len(blueprint._future_exceptions) == 1

    future_exception = list(blueprint._future_exceptions)[0]


# Generated at 2022-06-14 07:30:36.763964
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            return handler.handler(handler.exceptions[0])

    exception_mixin_t = ExceptionMixinTest()
    exception_mixin_t.exception(Exception)(print)
    assert exception_mixin_t._future_exceptions
    assert type(exception_mixin_t._future_exceptions) is set
    assert len(exception_mixin_t._future_exceptions) == 1
    for e in exception_mixin_t._future_exceptions:
        assert isinstance(e, FutureException)
        assert isinstance(e.exceptions, tuple)
        assert e.exceptions[0] is Exception
        assert e.handler is print

# Generated at 2022-06-14 07:30:43.787150
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.server import HttpProtocol
    from sanic.testing import SanicTestClient
    from sanic import Sanic

    sanic = Sanic(__name__)

    class ExceptionException(Exception):
        pass

    @sanic.exception(ExceptionException)
    def handler1(request, exception):
        return text('exception')

    test_bp = Blueprint('exception_mixin', url_prefix='/bp')

    @test_bp.exception(ExceptionException)
    def handler2(request, exception):
        return text('exception')

    @test_bp.route('/', methods=['GET'])
    async def handler(request):
        return text('OK')


# Generated at 2022-06-14 07:30:58.086487
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from sanic.blueprints import Blueprint
    blueprint = Blueprint("test", url_prefix="/test")

    @blueprint.exception(Exception)
    def handler(request, exception):
        return request, exception

    assert blueprint._future_exceptions
    assert isinstance(blueprint._future_exceptions.pop(), FutureException)
    assert blueprint.exception_handlers[Exception] == handler

# Generated at 2022-06-14 07:31:02.633758
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    future_exception = FutureException("handler", "exception")
    _future_exceptions = set()
    _future_exceptions.add(future_exception)
    assert _future_exceptions == {future_exception}

# Generated at 2022-06-14 07:31:11.487143
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class TestExceptionMixin(ExceptionMixin):

        def _apply_exception_handler(self, handler: FutureException):
            pass

    class TestException(Exception):
        pass

    exceptionMixin = TestExceptionMixin()

    @exceptionMixin.exception(TestException)
    def hander(request, exception):
        assert exception.__cause__

    future_exceptions = exceptionMixin._future_exceptions

    assert len(future_exceptions) == 1
    future_exception = next(iter(future_exceptions))
    assert future_exception.handler == hander
    exception = TestException('Test exception')
    future_exception.handler(None, exception)

# Generated at 2022-06-14 07:31:19.577973
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MySanic(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

    def handler(A, B, C=None):
        print('Exception Occured:', A, B, C)

    my_sanic = MySanic()
    augmented_handler = my_sanic.exception(KeyError)(handler)
    augmented_handler(5, 6, 7)

# Generated at 2022-06-14 07:31:26.699069
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestException(Exception):
        def __init__(self, msg):
            self.msg = msg

    class ExceptionMixinSubclass(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    exceptionMixinInstance = ExceptionMixinSubclass()
    exceptionHandler = lambda request, exception: request.text(exception)

    exceptionMixinInstance.exception(TestException)

# Generated at 2022-06-14 07:31:33.725918
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass
    def handler(request):
        pass
    test = TestExceptionMixin()
    assert len(test._future_exceptions) == 0
    test.exception(ValueError)(handler)
    assert len(test._future_exceptions) == 1
    test.exception(RuntimeError)(handler)
    assert len(test._future_exceptions) == 2
    # not applicable
    test.exception(ValueError)(handler)
    assert len(test._future_exceptions) == 2

# Generated at 2022-06-14 07:31:34.934364
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert False # TODO: implement your test here

# Generated at 2022-06-14 07:31:38.636076
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    promise = ExceptionMixin()
    @promise.exception(Exception, apply = True)
    def handler():
        return "handler"
    assert handler() == 'handler'
    assert promise._apply_exception_handler

# Generated at 2022-06-14 07:31:39.301075
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass  # TODO

# Generated at 2022-06-14 07:31:47.530456
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def apply_exception_handler(handler):
        assert handler == handler_1

    blueprint = type('blueprint', (ExceptionMixin,), {'_apply_exception_handler': apply_exception_handler})
    blueprint = blueprint()

    @blueprint.exception(Exception, apply=True)
    async def handler_1(request, exception):
        pass
    
    @blueprint.exception(Exception, apply=False)
    async def handler_2(request, exception):
        pass

# Generated at 2022-06-14 07:32:09.645798
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
  from sanic.blueprints import Blueprint
  from sanic.models.futures import FutureException
  bp = Blueprint("test_ExceptionMixin_exception")
  bp.exception(TypeError)(lambda req, ex: None)
  assert len(bp._future_exceptions) == 1
  assert isinstance(bp._future_exceptions.pop(), FutureException)

# Generated at 2022-06-14 07:32:16.805555
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.response import json
    from sanic import Blueprint

    # request handler
    def handle_request(request):
        return json({'text': 'I am a JSON response'})

    blueprint = Blueprint('my_api', __name__)

    blueprint.add_route(handle_request, '/')

    # exception handler
    @blueprint.exception(KeyError, apply=False)
    def handle_exception(request, exception):
        return json({"error": "KeyError"}, status=500)

    assert ('KeyError', handle_exception) in blueprint.exception_handlers

# Generated at 2022-06-14 07:32:29.324798
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprint import Blueprint
    from sanic.models.route import Route
    from sanic.models.exceptions import SanicException
    from sanic.models.exceptions import SanicExceptionWithContext

    blueprint = Blueprint('test')
    blueprint.exception(SanicException)
    blueprint.exception_handler(
        routes=[
            Route(
                blueprint,
                'GET',
                '/v1/users/{name}',
                'id'
            )
        ],
        exceptions=[SanicException]
    )

    blueprint.exception(SanicExceptionWithContext)(lambda: None)
    blueprint.exception(
        SanicExceptionWithContext,
        apply=False
    )(lambda: None)
    blueprint.exception(SanicException)(lambda: None)

# Generated at 2022-06-14 07:32:39.414211
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Handlers:
        def exception_handler(request, exception):
            pass

    class BpTester(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            handler.handler(None, ZeroDivisionError())

    bp = BpTester(Handlers)

    @bp.exception(ZeroDivisionError)
    def exception_handler():
        pass

    @bp.exception([ZeroDivisionError])
    def exception_handler_with_a_list():
        pass

    @bp.exception([ZeroDivisionError], apply=False)
    def exception_handler_without_apply():
        pass

    assert len(bp._future_exceptions) == 2

    bp.exception_handler()
    bp.exception_handler_with_a_list()

    assert len

# Generated at 2022-06-14 07:32:44.780605
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinObject(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass
    import pytest
    foo = ExceptionMixinObject()
    foo.exception(['test1', 'test2'], apply=False)
    with pytest.raises(TypeError):
        foo.exception([], apply=False)

# Generated at 2022-06-14 07:32:54.780799
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from .blueprint import Blueprint
    from .router import Router
    from sanic import Sanic
    from sanic.views import CompositionView
    from sanic.request import Request
    from sanic.response import text

    class ExceptionView(CompositionView):
        blueprint = Blueprint('exceptions', url_prefix='exceptions')

        @blueprint.route('/')
        async def index(request):
            1 / 0

        @blueprint.exception(ZeroDivisionError)
        def handle_div(request, exception):
            return text('Zero division')

        @blueprint.route('/foo')
        async def not_handling(request):
            1 / 0

        def register(self, app: Sanic):
            blueprint = self.blueprint
            app.blueprint(blueprint)


# Generated at 2022-06-14 07:33:01.663023
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestException(Exception):
        pass

    class DummyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print(handler)

    @DummyExceptionMixin().exception(TestException)
    def handler():
        pass

    assert len(DummyExceptionMixin()._future_exceptions) == 1



# ---------------------------
# Sanic global exception class
# ---------------------------



# Generated at 2022-06-14 07:33:06.854566
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.test_flag = 0

        def _apply_exception_handler(self, handler: FutureException):
            self.test_flag = 1
            return handler

    def handler():
        pass

    emt = ExceptionMixinTest()
    emt.exception(Exception)(handler)
    assert emt.test_flag == 1

# Generated at 2022-06-14 07:33:20.441708
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # This method tests that the exception decorator on the ExceptionMixin class
    # is working properly.

    from sanic.models.exceptions import SanicBlueprint

    from pytest import raises

    # First we define a mock class (just a class that has the exception method
    # from ExceptionMixin and the _apply_exception_handler method from the
    # SanicBlueprint class)
    class MockExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    # Next we define the mock class to be used within our test
    blueprint = MockExceptionMixin()

    # Then we test that the exception method is working properly

# Generated at 2022-06-14 07:33:23.314721
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            return True

    testExceptionMixin = TestExceptionMixin()
    testExceptionMixin.exception(IndexError)

# Generated at 2022-06-14 07:33:58.808472
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass


    a = ExceptionMixinTest()
    @a.exception(Exception)
    def test(a):
        pass

    assert len(a._future_exceptions) == 1
    assert len(a._future_exceptions.pop().exception_handlers) == 1



# Generated at 2022-06-14 07:34:11.550643
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A:
        def __init__(self, *args, **kwargs):
            self.exceptions = set()
            self.handler = None
            self.kwargs = None
            self.apply = None

        def _apply_exception_handler(self, handler):
            self.handler = handler
            self.apply = True

        def exception(self, *exceptions, apply=True):
            def decorator(handler):
                nonlocal apply
                nonlocal exceptions
                nonlocal self

                if isinstance(exceptions[0], list):
                    exceptions = tuple(*exceptions)

                future_exception = FutureException(handler, exceptions)
                self.exceptions.add(future_exception)
                if apply:
                    self._apply_exception_handler(future_exception)
                return handler

            return decorator



# Generated at 2022-06-14 07:34:17.849925
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    import unittest.mock
    from sanic import Sanic
    from sanic.blueprints import Blueprint

    class ExceptionMixinTest(unittest.TestCase):
        def setUp(self) -> None:
            self.app = Sanic('test_ExceptionMixin_exception')
            self.bp = Blueprint('test_ExceptionMixin_exception')

        @unittest.mock.patch.object(Blueprint, 'exception')
        def test_exception_decorator(self, blueprint_exception_mock):

            @self.bp.exception()
            def my_handler(self, request, exception):
                pass

            self.bp._apply_exception_handler(
                FutureException(handler=my_handler, exceptions=()))


# Generated at 2022-06-14 07:34:30.309003
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import SanicException

    class Error(SanicException):
        pass

    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            if handler.exception is None:
                handler.exception = Exception
            else:
                assert handler.exception == Exception
            if handler.handler_function is None:
                handler.handler_function = test_exception
            else:
                assert handler.handler_function == test_exception

    TestExceptionMixin = Blueprint.__new__(
        TestExceptionMixin, "TestExceptionMixin"
    )
    TestExceptionMixin.init_step_1_prepare()
    TestExceptionMixin.register_blueprint(TestExceptionMixin)


# Generated at 2022-06-14 07:34:43.209440
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
            self._been_applied = False

        def _apply_exception_handler(self, handler: FutureException):
            self._been_applied = True

    from sanic.exceptions import Forbidden
    from sanic.exceptions import NotFound
    from sanic.response import json

    # create a blueprint for unit test
    blueprint = TestExceptionMixin()

    # unit test for method exception of class ExceptionMixin
    @blueprint.exception([Forbidden, NotFound])
    def exception_handler_1(request, exception):
        return json({"exception": getattr(exception, "name", None)})

    future_

# Generated at 2022-06-14 07:34:46.765392
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    test_ExceptionMixin = ExceptionMixin()

    @test_ExceptionMixin.exception('*')
    def test_exception_handler(*args):
        print(args)

    assert test_exception_handler.__name__ == 'test_exception_handler'


# Generated at 2022-06-14 07:34:47.634885
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pytest.skip('Tests not implemented.')

# Generated at 2022-06-14 07:35:00.459327
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.router import RouteExists

    blueprint = Blueprint('exception_test_bp')

    @blueprint.exception(Exception)
    def blueprint_exception_handler(request: Request, exception: Exception):
        return 'blueprint_exception_handler'

    async def view_function(request):
        raise Exception

    blueprint.add_route(view_function, '/')

    sanic_app = blueprint.create_app('/prefix')

    @sanic_app.exception(RouteExists)
    def sanic_exception_handler(request: Request, exception: Exception):
        return 'sanic_exception_handler'

    result = sanic_app.test_client

# Generated at 2022-06-14 07:35:06.209865
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyException(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass

    def handler():
        pass

    # Expected result:
    # FutureException(handler, (ValueError,)
    exception = MyException().exception(ValueError)(handler)

# Generated at 2022-06-14 07:35:13.077802
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    app = Sanic('test_ExceptionMixin_exception')
    exception = ExceptionMixin(app)
    exception.blueprint = Blueprint('test', url_prefix='/test')
    route = exception.blueprint.route('/test')
    try:
        @route('/test', methods=['POST'])
        def handler(request):
            pass
    except Exception:
        pass

# Generated at 2022-06-14 07:36:19.213197
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.response import text

    app = Sanic()

    @app.exception(Exception)
    async def exception_handler(request, exception):
        raise RuntimeError

    @app.route('/')
    async def handler(request):
        return text('OK')

    request, response = app.test_client.get('/')
    assert response.status == 500

# Generated at 2022-06-14 07:36:25.059015
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestClass(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            assert handler.handler == testHandler
            assert handler.exceptions == ('testExceptionOne', 'testExceptionTwo')

    testClass = TestClass()
    @testClass.exception('testExceptionOne', 'testExceptionTwo')
    def testHandler():
        pass


# Generated at 2022-06-14 07:36:36.020046
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self) -> None:
            super(TestExceptionMixin, self).__init__()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    bp = TestExceptionMixin()
    assert len(bp._future_exceptions) == 0

    @bp.exception(TypeError)
    def test_handle_exc():
        pass

    assert len(bp._future_exceptions) == 1

    @bp.exception(AttributeError, apply=False)
    def test_handle_exc1():
        pass

    assert len(bp._future_exceptions) == 2

# Generated at 2022-06-14 07:36:39.953242
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError

# Generated at 2022-06-14 07:36:48.969389
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Model(ExceptionMixin):

        def _apply_exception_handler(self, handler: FutureException):
            pass
    # case 1
    model = Model()
    # case 2
    model.exception()
    # case 3
    model.exception(AttributeError)
    # case 4
    model.exception(AttributeError, KeyError)
    # case 5
    model.exception([AttributeError, KeyError])
    # case 6
    model.exception([AttributeError, KeyError], apply=False)

# Generated at 2022-06-14 07:36:53.361660
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    my_mixin = ExceptionMixin()
    exception_handler =1
    exceptions = [Exception]
    assert my_mixin.exception(exceptions)(exception_handler) == 1

# Generated at 2022-06-14 07:36:58.384723
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class DummyBlueprint(ExceptionMixin):
        pass

    blueprint = DummyBlueprint()
    blueprint.exception(BaseException)(BaseException)
    blueprint.exception(BaseException)(BaseException)
    blueprint.exception([BaseException, Exception])(TypeError)

    assert len(blueprint._future_exceptions) == 2

# Generated at 2022-06-14 07:37:10.558091
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MockExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            return handler

    mock = MockExceptionMixin()
    mock_handler = mock.exception(Exception)(lambda x: x)
    assert type(mock_handler) == types.LambdaType
    mock_handler = mock.exception([Exception])(lambda x: x)
    assert type(mock_handler) == types.LambdaType
    mock_handler = mock.exception(Exception, apply=False)(lambda x: x)
    assert type(mock_handler) == types.LambdaType
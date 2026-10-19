

# Generated at 2022-06-14 07:27:13.901708
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class SimpleExceptionMixin(ExceptionMixin):
        pass

    sem = SimpleExceptionMixin()

    @sem.exception(Exception)
    def handler(request, exception):
        return 'handler'

    # Using set built-in type to store instances of class FutureException
    result = set(sem._future_exceptions)
    expected = {
        FutureException(handler, (Exception,))
    }

    assert result == expected

test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:27:17.084853
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test object initialization
    em = ExceptionMixin()
    assert em._future_exceptions == set()
    # Test exception method
    @em.exception(Exception)
    def future(request, exception):
        return exception
    assert future(request=None, exception=Exception()) == Exception()

# Generated at 2022-06-14 07:27:26.928219
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)
            self._future_exceptions = []
            self.build_route = []

        def _apply_exception_handler(self, handler: FutureException):
            for futur_ex in self._future_exceptions:
                if handler == futur_ex:
                    self.build_route.append(handler)

    mixin = TestExceptionMixin()

    def handler():
        pass

    mixin.exception(handler)
    assert len(mixin._future_exceptions) == 1
    assert len(mixin.build_route) == 1

    def handler2():
        pass

    mixin.exception(handler2)
    assert len(mixin._future_exceptions) == 2


# Generated at 2022-06-14 07:27:27.803424
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:27:32.249598
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic

    app = Sanic('test_ExceptionMixin_exception')
    assert hasattr(app, '_future_exceptions')

    @app.exception(Exception)
    def handler(request, exception):
        return 'Exception happened'
    
    ExceptionMixin.exception(None, Exception)

# Generated at 2022-06-14 07:27:42.641892
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.response import HTTPResponse
    from sanic import Sanic
    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException

    class FakeException(Exception):
        pass

    app = Sanic('test_exception')
    bluprint = Blueprint('test_exception_bp')

    # Create mock handler to test global exception handler 
    @bluprint.exception(Exception)
    def handle_exception(request, exception):
        return HTTPResponse('Exception %s' % str(exception), status=500)

    # Test exception handler 
    @bluprint.route('/test')
    def handler(request):
        raise FakeException('fake exception')

    app.blueprint(bluprint)

    request, _response = app.test_client

# Generated at 2022-06-14 07:27:44.530207
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert ExceptionMixin.exception == 'exception'


# Generated at 2022-06-14 07:27:48.296497
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # TODO, implement unit test for method exception of class ExceptionMixin
    pass

# Generated at 2022-06-14 07:27:59.847251
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyException1(Exception):
        pass
    class MyException2(Exception):
        pass
    class MyException3(Exception):
        pass
    class MyException4(Exception):
        pass

    class MyException7(Exception):
        pass

    class MyClass(ExceptionMixin):
        exceptions = set()
        def _apply_exception_handler(self, handler):
            self.exceptions.add(handler)

    my_class = MyClass()

    handler1 = my_class.exception(MyException1, apply=False)
    handler2 = my_class.exception(MyException1, MyException2, apply=False)
    handler3 = my_class.exception(MyException1, apply=True)
    handler4 = my_class.exception([MyException3, MyException4], apply=True)


# Generated at 2022-06-14 07:28:12.291689
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint

    blueprint = Blueprint("test", url_prefix="/test")
    @blueprint.exception(apply=False)
    async def exception_handler(*args, **kwargs):
        pass

    assert len(blueprint._future_exceptions) == 1
    future_exception = blueprint._future_exceptions.pop()
    assert future_exception.handler == exception_handler
    assert future_exception.exceptions == ()

    app = Sanic("test_exception_handler")
    app.blueprint(blueprint)
    assert len(app.exception_handlers) == 1
    app_future_exception = app.exception_handlers.pop()
    assert app_future_exception.handler == exception_handler
    assert app_future_

# Generated at 2022-06-14 07:28:25.432505
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Foo(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    foo = Foo()

    # Check that the right type is returned
    @foo.exception(Exception)
    def handle_table_does_not_exist(request, exception):
        pass
    assert isinstance(handle_table_does_not_exist, types.FunctionType)

    # Check that the `FutureException` object was created successfully
    assert len(foo._future_exceptions) == 1
    assert all(map(lambda e: e.handler is handle_table_does_not_exist,
                   foo._future_exceptions))
    assert isinstance(list(foo._future_exceptions)[0].exceptions, tuple)
    assert Exception in list(foo._future_exceptions)[0].exceptions



# Generated at 2022-06-14 07:28:27.147929
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True
# s = ExceptionMixin()
# print(s)

# Generated at 2022-06-14 07:28:34.887477
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            print("_apply_exception_handler:")
            print("handler: ", handler)

    def handle_exception(exception):
        print("handle_exception")
        print("exception: ", exception)

    test_exception_mixin = TestExceptionMixin()
    test_exception_mixin.exception(handle_exception)

# Generated at 2022-06-14 07:28:47.170698
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from exceptions import Exception

    def handler(request, exception):
        pass

    # Create a class inherited from ExceptionMixin
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super(TestExceptionMixin, self).__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            assert handler.exceptions == (Exception,)

    # Initialize TestExceptionMixin instance
    exception_mixin = TestExceptionMixin()

    # Call method exception in TestExceptionMixin instance
    decorated_handler = exception_mixin.exception(Exception)(handler)

    # Verify result
    assert decorated_handler == handler

# Generated at 2022-06-14 07:28:49.043262
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert ExceptionMixin().exception(Exception)


# Generated at 2022-06-14 07:28:56.569370
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_test(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    mixin = ExceptionMixin_test()
    exception_test = mixin.exception(ValueError)(None)
    assert isinstance(exception_test, FutureException)
    assert exception_test.exception_type == ValueError
    assert exception_test.handler == None

# Generated at 2022-06-14 07:29:07.077893
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    explicit_bp = Blueprint('test', strict_slashes=True)
    class_bp = type('Test', (Blueprint, ExceptionMixin), {'name': 'test', 'strict_slashes' : True})()
    def not_none(bp):
        return bp is not None
    # Test explicit Blueprint
    assert not_none(explicit_bp.exception(ValueError)(lambda r: r))
    assert not_none(explicit_bp.exception(ValueError, apply=False)(lambda r: r))
    assert not_none(explicit_bp.exception([ValueError, RuntimeError])(lambda r: r))
    assert not_none(explicit_bp.exception([ValueError, RuntimeError], apply=False)(lambda r: r))
    # Test class-based

# Generated at 2022-06-14 07:29:19.104585
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FakeExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            return

    fake_exception_mixin = FakeExceptionMixin()
    decorator = fake_exception_mixin.exception(TypeError)
    @decorator
    def fake_handler():
        return

    assert isinstance(fake_exception_mixin._future_exceptions, set)
    assert fake_exception_mixin._future_exceptions != set()
    for future_exception in fake_exception_mixin._future_exceptions:
        assert isinstance(future_exception, FutureException)
        assert future_exception.handler == fake_handler
        assert future_exception.exceptions == (TypeError,)

# Generated at 2022-06-14 07:29:32.763280
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test scenario 1: apply=True
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            # Nothing to do
            pass

    test_args: tuple = (Exception, Exception, Exception)
    decorator = TestExceptionMixin().exception(*test_args)
    def test_handler():
        pass

    # Test exception
    decorator(test_handler)
    assert len(TestExceptionMixin()._future_exceptions) == 1
    # Test exception handler
    assert TestExceptionMixin()._future_exceptions.pop().handler == test_handler
    # Test exceptions
    assert TestExceptionMixin()._future_exceptions.pop

# Generated at 2022-06-14 07:29:38.179360
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exceptions = ["t1", "t2"]
    apply = True
    class A:
        def __init__(self):
            self._future_exceptions = set()
    a = A()
    obj = ExceptionMixin()
    handler = obj.exception(*exceptions, apply=apply)
    handler(a)
    assert len(a._future_exceptions) == 1

# Generated at 2022-06-14 07:29:51.883076
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class DummyExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    dummy_blueprint = DummyExceptionMixin()
    @dummy_blueprint.exception([ValueError, RuntimeError])
    def dummy_exception_handler(request, exception):
        pass

    new_exception = dummy_blueprint._future_exceptions.pop()
    assert [ValueError, RuntimeError] == new_exception.exception_types
    assert dummy_exception_handler == new_exception.handler

# Generated at 2022-06-14 07:29:55.137786
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    blueprint = Blueprint("test-bp")
    blueprint.exception(Exception)
    assert len(blueprint._future_exceptions) > 0



# Generated at 2022-06-14 07:29:57.226948
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # TODO: Write unit test for method exception of class ExceptionMixin
    # assert False
    pass

# Generated at 2022-06-14 07:30:07.982883
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        # unit test for method exception of class ExceptionMixin
        def __init__(self, *args, **kwargs):
            ExceptionMixin.__init__(self, *args, **kwargs)
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    # unit test for method exception of class ExceptionMixin
    # test case no 1
    def decorator(handler):
        return handler

    a = A()
    func = a.exception(1, 2, apply=True)
    assert func(a)

# Generated at 2022-06-14 07:30:14.007734
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_instance(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def handler(self):
            print('Hello World!')

    ExceptionMixin_instance().exception(Exception)(ExceptionMixin_instance().handler)
    print('Done!')

# Unit test
if __name__ == '__main__':
    test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:30:23.369636
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class SanicMock(ExceptionMixin):
        def __init__(self):
            pass

        def _apply_exception_handler(self, handler):
            pass

    sanic_mock = SanicMock()

    global exception_handler_called
    exception_handler_called = False

    @sanic_mock.exception(Exception)
    def exception_handler(request, exception):
        global exception_handler_called
        exception_handler_called = True

    with pytest.raises(Exception):
        raise Exception('test')

    assert exception_handler_called


# Generated at 2022-06-14 07:30:28.054340
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.exceptions import NotFound
    @ExceptionMixin.exception(NotFound)
    def k(request, exception):
        return 'Hello'

    exc_obj = ExceptionMixin()

# Generated at 2022-06-14 07:30:37.068057
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    test_ExceptionMixin = TestExceptionMixin()
    # ExceptionMixin.exception()
    @test_ExceptionMixin.exception(IndexError)
    def test_exception_handler(request, exception):
        pass
    assert len(test_ExceptionMixin._future_exceptions) == 1
    assert isinstance(test_ExceptionMixin._future_exceptions.pop(), FutureException)


# Generated at 2022-06-14 07:30:43.457697
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    blueprint = Blueprint(__name__)

    @blueprint.exception([NameError])
    def handler1(request, exception):
        pass

    @blueprint.exception(KeyError)
    def handler2(request, exception):
        pass

    @blueprint.exception(KeyError, apply=False)
    def handler3(request, exception):
        pass

    assert len(blueprint._future_exceptions) == 3
    assert False


# Generated at 2022-06-14 07:30:54.774224
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import InvalidUsage
    # Declare a Blueprint
    bp = Blueprint('test_bp', url_prefix='test')

    # An exception handler
    @bp.exception(InvalidUsage)
    def catch_invalid_usage(request, exception):
        pass

    # Assert the exception handler is in the set of future exception
    # handlers of the Blueprint
    assert len(bp._future_exceptions) == 1
    future_exception = tuple(bp._future_exceptions)[0]
    assert future_exception.handler == catch_invalid_usage
    assert isinstance(future_exception.exceptions[0], InvalidUsage)

# Generated at 2022-06-14 07:31:07.052851
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinClass(ExceptionMixin):
        ...
    class Handler:
        async def handler(*args, **kwargs):
            return 0
    emc = ExceptionMixinClass()
    emc.exception(TypeError)(Handler().handler)
    assert emc._future_exceptions != set()

# Generated at 2022-06-14 07:31:13.740304
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Object(ExceptionMixin):
        def __init__(self):
            self._apply_exception_handler = lambda x: x  # noqa

    a = Object()
    assert not len(a._future_exceptions)
    assert a.exception
    assert len(a._future_exceptions) == 1
    assert isinstance(a._future_exceptions, set)

# Generated at 2022-06-14 07:31:27.518015
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprint import Blueprint

    bp = Blueprint("api", url_prefix='/api')

    @bp.exception(IndexError)
    def index_error(request, exception):
        print("index error")

    @bp.exception(KeyError)
    def key_error(request, exception):
        print("key error")

    @bp.exception(Exception)
    def total_error(request, exception):
        print("total error")

    @bp.exception(ZeroDivisionError)
    def zero_error(exception):
        print("zero error")

    @bp.exception(ZeroDivisionError)
    def zero_error2(exception, **kwargs):
        print("zero error")

    assert len(bp._future_exceptions) == 5
    
    
# Unit

# Generated at 2022-06-14 07:31:32.622095
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Arrange
    class Blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print('Handler is applied')

    bp = Blueprint()

    # Act
    @bp.exception(NameError)
    def exception_handler(request, exception):
        pass

    # Assert
    assert exception_handler is not None
    print(bp._future_exceptions)
    assert len(bp._future_exceptions) == 1

# Generated at 2022-06-14 07:31:39.008663
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exception_mixin = ExceptionMixin()
    def handler():
        handler_fact = 1
        return handler_fact
    excepts = (Exception,)
    exception_mixin.exception(*excepts)(handler)
    expected = True
    actual = (handler == exception_mixin._future_exceptions.pop().handler)
    assert expected == actual

# Generated at 2022-06-14 07:31:40.120391
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert ExceptionMixin._future_exceptions == None

# Generated at 2022-06-14 07:31:51.179879
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    from sanic.response import json, text
    @ExceptionMixin.exception(ValueError)
    async def handle_exception(request, exception):
        return json({'message': "Error"}, status=404)
    bp = Blueprint.group(handle_exception, url_prefix='/test1')
    assert len(bp._future_exceptions) == 1

    @ExceptionMixin.exception([ValueError, ValueError])
    async def handle_exception(request, exception):
        return text('Error')
    bp = Blueprint.group(handle_exception.route, url_prefix='/test2')
    assert len(bp._future_exceptions) == 1

# Generated at 2022-06-14 07:32:02.142324
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.response import json
    from sanic.exceptions import SanicException
    from sanic import Sanic
    from sanic.blueprints import Blueprint
    from sanic.request import Request
    from sanic.models.futures import FutureException

    app = Sanic("test_ExceptionMixin_exception")
    bp = Blueprint("test_ExceptionMixin_exception")

    @bp.exception
    def handler(request: Request, exception: SanicException):
        return json({"exception": exception.__class__.__name__})

    app.blueprint(bp)

    request, response = app.asgi_wrapper.test_client.get("/")
    assert response.json == {"exception": "NotFound"}


# Generated at 2022-06-14 07:32:14.673324
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic import response

    from sanic.testing import SanicTestClient

    app = Sanic(__name__)
    bp = Blueprint('test_bp', url_prefix='test')

    @bp.listener('before_server_start')
    def register_bp(app, loop):
        app.blueprint(bp)


    @bp.exception(IndexError)
    def exception_handler(request, exception):
        """Test the usage of exception"""
        print(exception)
        return response.json({'exception': str(exception)}, status=500)

    @bp.get('/')
    def handler(request):
        """Test the usage of exception"""
        raise IndexError('Testing exception')


# Generated at 2022-06-14 07:32:16.094035
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    test_ExceptionMixin = ExceptionMixin()
    assert test_ExceptionMixin.exception

# Generated at 2022-06-14 07:32:37.736928
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    a = TestExceptionMixin()
    @a.exception()
    def handler():
        raise AttributeError
    assert len(a._future_exceptions) == 1

# Generated at 2022-06-14 07:32:41.352890
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    try:
        mixin = ExceptionMixin()
    except Exception as e:
        assert type(e) is NotImplementedError

# Generated at 2022-06-14 07:32:52.441295
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    mixin = TestExceptionMixin()

    exception_list = [Exception, ValueError, IndexError]
    exception_kwargs = {'status_code': 404}

    @mixin.exception(exception_list, **exception_kwargs)
    def handler(*args, **kwargs):
        pass

    assert len(mixin._future_exceptions) == 1

    handler_ = mixin._future_exceptions.pop()
    assert handler.handler == handler_
    assert handler.exceptions == exception_list
    assert handler_._kwargs == exception_kwargs

# Generated at 2022-06-14 07:32:53.277425
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:33:04.567627
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.middleware import MiddlewareModel
    from sanic.models.plugins import PluginModel
    from sanic.models.handler import HandlerModel
    from sanic.exceptions import ServerError, SanicException

    def handler():
        pass
    # test for class BluePrint
    from sanic.models.blueprint import BluePrint

    bp = BluePrint('bp1')
    bp.exception(RuntimeError)(handler)
    for future_exception in bp._future_exceptions:
        assert future_exception.handler == handler
        assert future_exception.exceptions == (RuntimeError,)
    # test for class Server
    from sanic.models.server import Server

    server = Server()
    server.exception(ServerError, SanicException)(handler)

# Generated at 2022-06-14 07:33:12.388336
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin1(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    a = ExceptionMixin1()
    try:
        a.exception(Exception)(lambda x:x)(1)
    except Exception as e:
        print('test_ExceptionMixin_exception Exception:', e)
        return

    assert True

test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:33:23.862306
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import types
    import unittest
    from sanic.blueprints import Blueprint
    
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            self.handler_passed = handler

    exceptions = [Exception,]
    apply = False
    bp = Blueprint("ExceptionMixin")
    def handler(): pass

    for apply in [True, False]:
        for exceptions in [Exception, [Exception,]]:
            bp.exception(exceptions, apply)(handler)
            future_exception = bp._future_exceptions.pop()
            assert isinstance(future_exception, FutureException)
            assert future_exception.handler == handler
            assert future_exception.exceptions == tuple(
                exceptions if isinstance(exceptions, list) else [exceptions,])

# Generated at 2022-06-14 07:33:27.253238
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    value = ExceptionMixin(1,2)
    value.exception('hello', 'world', apply=True)(print)
# test: Done


# Generated at 2022-06-14 07:33:40.589893
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    import inspect
    import types

    class ExceptionMixin_obj(ExceptionMixin):
        def __init__(self, app):
            self._app = app

        def _apply_exception_handler(self, handler: FutureException):
            self._app.exception(*handler.exceptions)(handler.handler)

    app = Sanic(__name__)
    
    ExceptionMixin_test = ExceptionMixin_obj(app)

    @ExceptionMixin_test.exception([Exception])
    def test_1():
        return
    
    @ExceptionMixin_test.exception([Exception])
    def test_2():
        return

    @ExceptionMixin_test.exception([Exception])
    def test_3():
        return


# Generated at 2022-06-14 07:33:50.035470
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    print('Unit test for method exception of class ExceptionMixin')
    global test_Blueprint_exception_flag
    test_Blueprint_exception_flag = 0
    @ExceptionMixin.exception(ApplyError)
    def test_func(request, exception):
        nonlocal test_Blueprint_exception_flag
        test_Blueprint_exception_flag = 1
    assert not test_Blueprint_exception_flag
    # if things go well, this excute should raise ApplyError
    raise ApplyError
    assert test_Blueprint_exception_flag
    print('Pass\n')

# Generated at 2022-06-14 07:34:30.850245
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic

    """
    Check whether method exception works well in class ExceptionMixin.
    """
    app = Sanic('sanic-test')

    # Check whether the decorated method can be returned
    @app.exception(Exception)
    def test_function():
        print('test_function')

    assert app.exception(Exception)(test_function) is test_function

    # Check whether a FutureException is added to the list of
    # future_exceptions
    @app.exception(Exception)
    def second_test_function():
        print('second_test_function')

    assert app.exception(Exception)(second_test_function) is second_test_function
    assert len(app._future_exceptions) == 2

    # Check whether the list of future_exceptions has removed the FutureException


# Generated at 2022-06-14 07:34:42.560908
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.blueprints import Blueprint
    from sanic.exceptions import NotFound
    from sanic.response import text
    from sanic.server import HttpProtocol

    @Blueprint.exception(NotFound)
    def ignore_404s(request, exception):
        return text("Yep, I totally found the page: {}".format(request.url))

    app = Sanic(__name__)
    app.blueprint(Blueprint)
    app.exception(Exception)(HttpProtocol.handle_request_exception)

    request, response = app.test_client.get("/")
    assert response.text == "Yep, I totally found the page: http://localhost/"



# Generated at 2022-06-14 07:34:45.844129
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exceptions = [Exception]
    kwargs = {}
    handler = lambda x: True
    exp = handler
    exception_mixin = ExceptionMixin()
    assert exception_mixin.exception(exceptions)(handler) == exp

# Generated at 2022-06-14 07:34:54.153739
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_mixin = TestExceptionMixin()

    @test_mixin.exception([ValueError, KeyError])
    def handle_exception(request, exception):
        pass

    assert test_mixin._future_exceptions[0].handler == handle_exception
    assert test_mixin._future_exceptions[0].exceptions == tuple(
        [ValueError, KeyError])

# Generated at 2022-06-14 07:34:59.493594
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    #Arrange
    blueprint_name = 'blueprint'
    blueprint = Blueprint(blueprint_name)
    exception_mixin = ExceptionMixin()
    
    #Action
    exception_mixin.exception()
    
    #Assert
    assert exception_mixin
    #assertExceptionMixin

# Generated at 2022-06-14 07:35:09.402206
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from sanic.views.exceptions import exception_handler

    class Test(ExceptionMixin):
        def __init__(self):
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler: FutureException):
            exception_handler.add_future_exception(handler)

    test = Test()

    @test.exception(Exception, apply=False)
    def test_handler(request, e):
        pass

    assert len(test._future_exceptions) == 1

    @test.exception(Exception)
    def test_handler_2(request, e):
        pass

    assert len(test._future_exceptions) == 2

# Generated at 2022-06-14 07:35:19.623183
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # test when apply is True
    server = Sanic("test_ExceptionMixin_exception")
    @server.get("/test")
    @server.exception(ValueError, apply=True)
    def test(request):
        pass
    assert len(server._future_exceptions) == 1
    assert server._future_exceptions == set([FutureException(test, ValueError)])

    # test when apply is False
    server = Sanic("test_ExceptionMixin_exception")
    @server.get("/test")
    @server.exception(ValueError, apply=False)
    def test(request):
        pass

# Generated at 2022-06-14 07:35:32.980517
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Mocker():
        def __init__(self, *args, **kwargs):
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler):
            self._future_exceptions.add(handler)

    instance = Mocker()
    assert 0 == len(instance._future_exceptions)
    @instance.exception(ZeroDivisionError)
    def zero_div(request, exception):
        pass
    assert 1 == len(instance._future_exceptions)
    assert next(iter(instance._future_exceptions)).handler == zero_div
    assert [ZeroDivisionError] == list(next(iter(instance._future_exceptions)).exceptions)
    assert True == next(iter(instance._future_exceptions)).apply

# Generated at 2022-06-14 07:35:42.347862
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint('test', url_prefix='/test')

    @bp.exception(ZeroDivisionError)
    def error_handler(request, exception):
        return text(str(exception), status=500)

    @bp.route('/')
    def handler(request):
        return 1 / 0

    app = bp.create_app()

    request, response = app.test_client.get('/')
    assert response.text == 'division by zero'
    assert response.status == 500

# Generated at 2022-06-14 07:35:49.484179
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FakeExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.done = False

        def _apply_exception_handler(self, handler: FutureException):
            self.done = True

    blue = FakeExceptionMixin()
    @blue.exception(Exception, apply=True)
    def func():
        pass

    func()
    assert blue.done is True
    assert isinstance(blue._future_exceptions.pop(), FutureException)


# Generated at 2022-06-14 07:37:02.245881
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class blueprint:
        pass
    bp = blueprint()
    ex_mixin = ExceptionMixin()
    def handler():
        pass
    def test(ex, apply):
        nonlocal bp
        nonlocal ex_mixin
        nonlocal handler
        bp.exception = ex_mixin.exception
        bp.exception(handler, *ex, apply=apply)
    test(ValueError, True)
    assert len(ex_mixin._future_exceptions) == 1
    test(ZeroDivisionError,False)
    assert len(ex_mixin._future_exceptions) == 2
    test([],True)
    assert len(ex_mixin._future_exceptions) == 3
    test(None, True)
    assert len(ex_mixin._future_exceptions) == 4
    test

# Generated at 2022-06-14 07:37:12.016456
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            assert len(self._future_exceptions) == 1
            exception = next(iter(self._future_exceptions))
            assert exception == handler
            assert exception.exceptions == (ZeroDivisionError,)
            assert exception.args == (1, 2)


    test = TestExceptionMixin()
    @test.exception(ZeroDivisionError, 1, 2)
    def handler(err):
        assert err is ZeroDivisionError  # noqa


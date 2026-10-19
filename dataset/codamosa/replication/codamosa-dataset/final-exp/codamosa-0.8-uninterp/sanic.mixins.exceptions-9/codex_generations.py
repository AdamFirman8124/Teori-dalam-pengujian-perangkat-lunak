

# Generated at 2022-06-14 07:27:19.298268
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test case 1: Handle exception
    @ExceptionMixin.exception(ZeroDivisionError, apply=True)
    def test_handler(request, exception):
        assert True
    # Test case 2: Handle exception with multiple exceptions
    @ExceptionMixin.exception(ZeroDivisionError, AssertionError, apply=False)
    def test_handler(request, exception):
        assert True

# Generated at 2022-06-14 07:27:26.501281
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprints import Blueprint
    
    class DummyBlueprint(Blueprint, ExceptionMixin):
        pass

    blueprint = DummyBlueprint("test_blueprint", url_prefix="/test")

    @blueprint.exception(ZeroDivisionError)
    def handler(request, exception):
        request.app.test_exception_handler = handler

    assert blueprint._future_exceptions
    assert blueprint._future_exceptions.pop().handler == handler


# Generated at 2022-06-14 07:27:34.334152
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    
    from sanic.models.futures import FutureException
    from sanic.models.blueprints import Blueprint

    bp = Blueprint(name="test", url_prefix='test')
    # This will not be apply in method ExceptionMixin.exception
    assert bp._future_exceptions == set()
    assert bp.exception(Exception)
    assert bp._future_exceptions == set(FutureException)

    # This will be apply in method ExceptionMixin.exception
    assert bp._future_exceptions == set()
    assert bp.exception(Exception, apply=True)
    assert bp._future_exceptions == set(FutureException)

# Generated at 2022-06-14 07:27:41.039687
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_ExceptionMixin = TestExceptionMixin()
    assert len(test_ExceptionMixin._future_exceptions) == 0
    # If a handler doesn't be created, it will throw error
    assert test_ExceptionMixin.exception()

# Generated at 2022-06-14 07:27:54.109198
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.views import HTTPMethodView

    class View(HTTPMethodView, ExceptionMixin):

        def _apply_exception_handler(self, handler: FutureException):
            app.error_handler.add(handler)

        @HTTPMethodView.get("/test_exception_method")
        def test_exception_method(self):
            return HTTPResponse("response")

        @HTTPMethodView.post("/test_exception_method")
        def test_exception_method(self):
            return HTTPResponse("response")


# Generated at 2022-06-14 07:28:02.528930
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.exceptions import SanicException
    from sanic.blueprints import Blueprint
    from sanic.helpers import is_coroutine_function
    from sanic.response import text

    class CustomException(SanicException):
        pass

    app = Sanic('test_exception_of_blueprint')
    blueprint = Blueprint('test_exception_of_blueprint')

    @blueprint.exception(CustomException)
    def custom_exception_handler1(request, exception):
        return text('Error', 500)

    @blueprint.exception()
    def custom_exception_handler2(request, exception):
        return text('Error', 500)

    @blueprint.exception([CustomException])
    def custom_exception_handler3(request, exception):
        return text('Error', 500)


# Generated at 2022-06-14 07:28:03.143352
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True

# Generated at 2022-06-14 07:28:15.404009
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    import unittest.mock
    from sanic.blueprints import Blueprint

    class Handler:
        pass

    blueprint = Blueprint("name")
    handler = Handler()
    blueprint.exception(Exception)(handler)

    future_exception = blueprint._future_exceptions.pop()

    assert future_exception.handler is handler
    assert future_exception.exceptions == ((Exception,),)
    assert future_exception.kwargs == {}

    blueprint.exception((Exception,  FileNotFoundError))(handler)

    future_exception = blueprint._future_exceptions.pop()

    assert future_exception.handler is handler
    assert future_exception.exceptions == ((Exception,  FileNotFoundError),)
    assert future_exception.kwargs == {}


# Generated at 2022-06-14 07:28:17.333614
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Sanic(ExceptionMixin):
        pass

    with pytest.raises(NotImplementedError):
        Sanic().exception(ValueError)

# Generated at 2022-06-14 07:28:22.709732
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinInstant(ExceptionMixin):
        def __init__(self):
            super(ExceptionMixinInstant, self).__init__()

    e = ExceptionMixinInstant()
    @e.exception(ValueError)
    def test_exception_handler(request, exception):
        pass


# Generated at 2022-06-14 07:28:35.114311
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.models.route import Route
    from sanic.response import HTTPResponse

    #Create instance of ExceptionMixin
    class Route_(Route, ExceptionMixin):
        def __init__(self):
            self.name = None
            self.host = None
            self.uri = None
            self.methods = None
            self.handler = None
            self.register = False
            self.uri_template = None
            self.strict_slashes = None

        def _apply_exception_handler(self, handler: FutureException):
            pass

    route = Route_()

    #Test method exception of object route

# Generated at 2022-06-14 07:28:43.646200
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint("blueprint_1")
    @bp.exception(ZeroDivisionError)
    def divide_by_zero_handler(request, exception):
        raise ZeroDivisionError("division by zero")
    assert len(bp._future_exceptions) == 1
    assert bp._future_exceptions == set({FutureException(divide_by_zero_handler, (ZeroDivisionError,))})


# Generated at 2022-06-14 07:28:50.713483
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # GIVEN
    class FakeExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    exc_mixin = FakeExceptionMixin()
    # WHEN
    @exc_mixin.exception()
    def my_handler():
        pass
    # THEN
    assert len(exc_mixin._future_exceptions) == 1

# Generated at 2022-06-14 07:29:02.541304
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models import Blueprint
    from sanic.server import Sanic
    from sanic.request import Request

    app = Sanic()
    bp = Blueprint('Name', url_prefix='/prefix')

    @bp.exception(ValueError)
    def handle_exception(request: Request, exception: Exception):
        return 'error_value'

    @bp.exception()
    def handle_default_exception(request: Request, exception: Exception):
        return 'error_default'

    assert len(bp._future_exceptions) == 2

    @bp.route('/')
    def handler(request):
        raise ValueError

    @app.exception(bp)
    def handle_exception(request: Request, exception: Exception):
        return 'error_global'

    app.blueprint(bp)
   

# Generated at 2022-06-14 07:29:11.203341
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    ex_mixin = ExceptionMixin()
    arguments = [1, 2, 3]
    with pytest.raises(NotImplementedError):
        ex_mixin._apply_exception_handler(arguments)
    def decorator(handler):
        return handler
    decorator = ex_mixin.exception(arguments)
    assert decorator is not None
    def func():
        return 1
    assert decorator(func) is func
    assert decorator(func) is not None

# Generated at 2022-06-14 07:29:22.679008
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import sys
    from sanic.models.futures import FutureException

    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self):
            super(ExceptionMixinTest, self).__init__()

        def _apply_exception_handler(self, handler):
            return handler

    class X(Exception):
        pass

    class Y(Exception):
        pass

    class Z(Exception):
        pass

    emt = ExceptionMixinTest()

    @emt.exception(X, Y, Z)
    def handle_exception(request, exception):
        return 'x', exception

    assert len(emt._future_exceptions) == 1
    fe = next(iter(emt._future_exceptions))
    assert fe.handler == handle_exception

# Generated at 2022-06-14 07:29:31.457549
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Test1(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

    class Test2(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            return "Exception handler applied"

    test1 = Test1()
    assert test1.exception(AssertionError)
    assert test1.exception(AssertionError, Exception, apply=False)

    test2 = Test2()
    assert test2._apply_exception_handler(...).startswith("Exception handler applied")

# Generated at 2022-06-14 07:29:37.504549
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler):
            pass
    exception_mixin_test_obj = ExceptionMixinTest()
    exception_mixin_test_obj.exception(Exception)(print)

# Generated at 2022-06-14 07:29:42.813207
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def handler(request, exception):
        return 'exception'

    obj = ExceptionMixin()
    setattr(obj, '_apply_exception_handler', lambda x: None)

    obj.exception(ValueError)(handler)

    assert len(obj._future_exceptions) == 1



# Generated at 2022-06-14 07:29:55.078057
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTester(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            return
    # exception((Exception, ))
    # return value is a function
    assert callable(ExceptionMixinTester().exception((Exception, ))) 

    # exception((Exception, Exception), apply=False)
    # return value is a function
    assert callable(ExceptionMixinTester().exception((Exception, Exception), apply=False)) 

    # exception([Exception, Exception])
    # return value is a function
    assert callable(ExceptionMixinTester().exception([Exception, Exception])) 

    # exception([Exception, Exception], apply=False)
    # return value is a function

# Generated at 2022-06-14 07:30:08.689212
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class DummyExceptionMixin(ExceptionMixin):

        def _apply_exception_handler(self, handler):
            pass

    dummy_exception_mixin = DummyExceptionMixin()
    def handler():
        pass

    dummy_exception_mixin.exception(IndexError)(handler)
    future_exceptions = dummy_exception_mixin._future_exceptions

    future_exception = next(iter(future_exceptions))
    assert (
        future_exception.handler == handler and
        len(future_exception.exceptions) == 1 and
        IndexError in future_exception.exceptions
    )

# Generated at 2022-06-14 07:30:12.533709
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    futex = FutureException("test", "test2")
    mixin = ExceptionMixin()
    mixin._future_exceptions.add(futex)

    assert futex in mixin._future_exceptions
    

# Generated at 2022-06-14 07:30:13.947267
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    isinstance(ExceptionMixin, object)

# Generated at 2022-06-14 07:30:25.831445
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.models import FutureException, FutureRoute
    from sanic.views.route import View
    from sanic.blueprints import Blueprint

    app = Sanic('test_exception')
    bp = Blueprint(
        'test_bp',
        url_prefix='/prefix',
        host='example.com',
        strict_slashes=True,
        version=1,
    )
    bp.exception(Exception, apply=False)('test_handler')

    assert any([True for f in bp._future_exceptions if f.exception == Exception])

    bp._apply_exception_handler(FutureException('test_handler', Exception))

    routes = bp.routes_namespace
    assert routes['test_handler']


# Generated at 2022-06-14 07:30:36.128395
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint, Sanic
    from sanic.exceptions import abort

    app = Sanic("test")
    blueprint = Blueprint("test_blueprint", url_prefix="/blueprint")

    @blueprint.exception(ValueError)
    def value_error_handler(request, exception):
        return response.text("value error")

    @blueprint.route("/")
    def handler(request):
        raise ValueError("something went wrong")

    app.blueprint(blueprint)

    request, response = app.test_client.get("/blueprint/")
    assert response.text == "value error"


# Generated at 2022-06-14 07:30:40.686141
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMix(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(args, kwargs)

    mix = ExceptionMix()
    assert mix.exception is ExceptionMixin.exception

# Generated at 2022-06-14 07:30:41.305338
# Unit test for method exception of class ExceptionMixin

# Generated at 2022-06-14 07:30:54.813765
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint, Sanic
    from sanic.response import text
    from sanic_restplus.api import Api
    import pytest

    @pytest.fixture()
    def setup_api():
        app = Sanic()
        api = Api(app)
        return app, api

    @pytest.fixture()
    def setup_bp():
        bp = Blueprint("test_exception")
        return bp

    @pytest.mark.asyncio
    async def test_return_function_decorator(setup_api, setup_bp):
        app, api = setup_api


# Generated at 2022-06-14 07:30:55.818694
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass # TODO: implement test

# Generated at 2022-06-14 07:30:56.883189
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # raise NotImplementedError()
    pass

# Generated at 2022-06-14 07:31:12.731209
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler):
            print(handler.handle)

    a = A()
    a.exception(Exception)(lambda a: print(a))
    assert len(a._future_exceptions) == 1

# Generated at 2022-06-14 07:31:26.498260
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Given a blueprint
    class TestClass(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            ExceptionMixin.__init__(self, *args, **kwargs)

        def _apply_exception_handler(self, handler):
            assert handler.handler is not None

    # and a blueprint
    blueprint = TestClass()
    assert blueprint._future_exceptions is not None
    assert blueprint._future_exceptions == set()

    # when we add an exception handler
    @blueprint.exception()
    def handler():
        assert True

    # then we should have a decorated handler
    assert blueprint._future_exceptions is not None
    assert len(blueprint._future_exceptions) == 1
    assert blueprint._future_exceptions.pop().handler is not handler

# Generated at 2022-06-14 07:31:32.635251
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest.mock
    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException

    blueprint = Blueprint('test_blueprint')

    @blueprint.exception(Blueprint)
    def handler(request, exception):
        return (request, exception)

    handler = blueprint._future_exceptions.pop()

    assert isinstance(handler, FutureException)
    assert handler.exceptions[0] is Blueprint
    assert handler.handler(0, 1) == (0, 1)



# Generated at 2022-06-14 07:31:46.239928
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    bp = Blueprint()
    assert len(bp._future_exceptions) == 0
    @bp.exception(IndexError)
    def handler(request, exception):
        pass
    assert len(bp._future_exceptions) == 1
    future_exception = next(iter(bp._future_exceptions))
    assert future_exception.handler is handler
    assert future_exception.exceptions == (IndexError,)

    @bp.exception(IndexError, ValueError, apply=False)
    def handler2(request, exception):
        pass
    assert len(bp._future_exceptions) == 2
    future_exception = next(iter(bp._future_exceptions))
    assert future_

# Generated at 2022-06-14 07:31:57.712462
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestClass(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.exception1 = None

    test_class = TestClass()
    exception1 = Exception
    exception2 = Exception('Exception 2')

    def test_handler1(request, exception2):
        test_class.exception1 = exception2

    test_class.exception(exception1, exception2, apply=False)(test_handler1)

    assert test_class.exception1 is exception2
    assert test_handler1 in [
        e.handler for e in test_class._future_exceptions
    ]
    assert len(test_class._future_exceptions) == 1



# Generated at 2022-06-14 07:32:07.737883
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FakeClass:
        def __init__(self):
            self._future_exceptions = set()
            
        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    fake_class = FakeClass()
    FakeClass.exception = ExceptionMixin.exception.__get__(fake_class) 

    import inspect
    assert inspect.ismethod(FakeClass.exception)

    def fake_handler_exception(fake_request, fake_exception):
        pass

    fake_class.exception(TypeError)(fake_handler_exception)

    future_exception = FutureException(fake_handler_exception, (TypeError,))
    assert future_exception in fake_class._future_exceptions

# Generated at 2022-06-14 07:32:13.764582
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
        GIVEN ExceptionMixin class
        WHEN exception method is called
        THEN assert isinstance of list exceptions
    """
    exp = ExceptionMixin()
    exceptions = [Exception, ZeroDivisionError, FileNotFoundError]
    res = exp.exception(*exceptions)
    assert isinstance(res, list)
    assert isinstance(exceptions, list)
    assert res == exceptions
    assert exceptions == exp._future_exceptions

# Generated at 2022-06-14 07:32:21.736194
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        def _apply_exception_handler(self, handler: FutureException):
            pass
    test_object = TestExceptionMixin()
    handler = lambda *args,**kwargs:None
    mixin_future_exceptions = test_object._future_exceptions

    @test_object.exception(ValueError, ZeroDivisionError)
    def test_exception_handler():
        pass

    expected_future_exceptions = {FutureException(handler, (ValueError, ZeroDivisionError))}
    assert (mixin_future_exceptions ==
            expected_future_exceptions) is True

# Generated at 2022-06-14 07:32:30.482577
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Declare the exception mixin class
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError("_apply_exception_handler is not implemented")

    # Test Case
    case: TestExceptionMixin = TestExceptionMixin()
    assert case._future_exceptions == set()
    case.exception(RuntimeError, apply=True)
    assert case._future_exceptions != set()

# Generated at 2022-06-14 07:32:37.165409
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

    bp = Blueprint()

    def handler(*args, **kwargs):
        return

    bp.exception(ValueError, apply=True)(handler)
    assert len(bp._future_exceptions) == 1
    assert bp._future_exceptions.pop().handler == handler

# Generated at 2022-06-14 07:32:56.175397
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprint import Blueprint

    blueprint = Blueprint('test')
    assert blueprint.exception(Exception)(None) == None
    assert blueprint._future_exceptions != set()
    assert blueprint._future_exceptions.pop()

# Generated at 2022-06-14 07:33:07.219549
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FutureException:
        def __init__(self, exception, handler):
            assert exception == exceptions[0]
            assert handler == handler1
            
    class Blueprint:
        def __init__(self):
            self._future_exceptions: Set[FutureException] = set()
            self._apply_exception_handler = ExceptionHandler
        
    def ExceptionHandler(handler: FutureException):
        assert handler.handler == handler1
        
    exceptions = [Exception]
    bp = Blueprint()
    @bp.exception(exceptions[0])
    def handler1(*args, **kwargs):
        pass
    assert isinstance(bp._future_exceptions.pop(), FutureException)



# Generated at 2022-06-14 07:33:20.807196
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # get 
    def get(request):
        return text('{"status_code": 200,"msg": "get"}')

    # post
    def post(request):
        return text('{"status_code": 200,"msg": "post"}')

    # put
    def put(request):
        return text('{"status_code": 200,"msg": "put"}')

    # delete
    def delete(request):
        return text('{"status_code": 200,"msg": "delete"}')
    
    # patch
    def patch(request):
        return text('{"status_code": 200,"msg": "patch"}')

    class ExceptionMixin_class():
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()


# Generated at 2022-06-14 07:33:29.497819
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            handler.apply()

    em = TestExceptionMixin()
    em.exception(ValueError)(print)
    em.exception(KeyError, 404)(print)
    em.exception(KeyError, 404, apply=False)(print)

    assert len(em._future_exceptions) == 3
    assert type(em._future_exceptions) == set
    assert list(em._future_exceptions)[0].handler == print
    assert list(em._future_exceptions)[0].exceptions == (ValueError,)
    assert list(em._future_exceptions)[1].handler == print
    assert list(em._future_exceptions)[1].exceptions == (KeyError, 404)

# Generated at 2022-06-14 07:33:41.872401
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.blueprints import Blueprint
    from sanic.exceptions import SanicException
    from sanic.handlers import ErrorHandler
    from sanic.response import text
    from sanic.views import HTTPMethodView

    app = Sanic("test_ExceptionMixin_exception")

    blueprint = Blueprint("test_ExceptionMixin_exception", url_prefix="test")

    class SimpleView(HTTPMethodView):
        def get(self, request):
            raise SanicException("You made a bad request!")

    blueprint.add_route(SimpleView.as_view(), "/route")

    @blueprint.exception(SanicException)
    def handler_404(request, exception):
        return text("Exception!")

    app.blueprint(blueprint)
    client

# Generated at 2022-06-14 07:33:54.990436
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic

    class ExceptionMixinTestCase(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.exception_future_exceptions = set()

        def _apply_exception_handler(self, handler: FutureException):
            self.exception_future_exceptions.add(handler)

    # ExceptionMixinTestCase.__init__
    exception_mixin_test_case = ExceptionMixinTestCase()
    # ExceptionMixinTestCase.exception
    @exception_mixin_test_case.exception(Exception)
    def test_function():
        raise Exception

    test_function()
    assert isinstance(exception_mixin_test_case._future_exceptions.pop(), FutureException)

# Generated at 2022-06-14 07:34:01.860782
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test Object
    class Sanic(ExceptionMixin):
        def catch_all_exception_handler(self, request, exception):
            return "{}".format(exception)

        @staticmethod
        def _apply_exception_handler(handler: FutureException) -> None:
            pass

    # Test Case:
    # Passes without exception
    Sanic().exception(Exception)

    # Test Case:
    # Passes without exception
    Sanic().exception([ValueError, RuntimeError])


# Generated at 2022-06-14 07:34:11.487132
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(RuntimeError)
    async def handler(request, exception):
        raise RuntimeError()

# Assignment of parameter `apply` to the method
# def test_ExceptionMixin_exception_apply(apply = True):
#     @ExceptionMixin.exception(RuntimeError, apply = apply)
#     async def handler(request, exception):
#         raise RuntimeError()
#
# # Assignment of parameter `apply` to the method with another value
# def test_ExceptionMixin_exception_apply(apply = False):
#     @ExceptionMixin.exception(RuntimeError, apply = apply)
#     async def handler(request, exception):
#         raise RuntimeError()

# Generated at 2022-06-14 07:34:16.920002
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.mediator import Mediator
    
    blueprint = Blueprint(__name__, url_prefix='/test')
    mediator = Mediator()
    mediator.add_blueprint(blueprint)
    

# Generated at 2022-06-14 07:34:29.856410
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.response import json
    from sanic.request import Request
    from sanic.exceptions import ServerError

    bp = Blueprint("test_ExceptionMixin_exception")

    @bp.exception()
    async def handler1(request: Request, exception: ServerError):
        return json("testing handler1")

    @bp.exception()
    async def handler2(request: Request, exception: ServerError):
        return json("testing handler2")

    @bp.route("/test_ExceptionMixin_exception")
    async def test_ExceptionMixin_exception_handler(request: Request):
        raise ServerError("Internal Server Error", status_code=500)


# Generated at 2022-06-14 07:35:10.293188
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.models.blueprint import Blueprint

    app = Sanic("TestApp")
    bp = Blueprint("TestExceptionMixin", url_prefix="test")
    exception_mixin_bp = Blueprint("TestExceptionMixin", url_prefix="test")

    @bp.exception(KeyError)
    def exception_handler(request, exception):
        return text("There was a problem!")

    @exception_mixin_bp.exception([KeyError, OverflowError])
    def exception_mixin_bp_handler(request, exception):
        return text("There was a problem!")

    assert isinstance(bp.exception, types.MethodType)
    assert isinstance(exception_mixin_bp.exception, types.MethodType)


# Generated at 2022-06-14 07:35:20.981857
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.views import HTTPMethodView

    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    blueprint = Blueprint(__name__)

    decorator = blueprint.exception(Exception)

    @decorator
    def exception_handler1(request, exception):
        pass

    @blueprint.route('/')
    class TestClassA(HTTPMethodView):
        @blueprint.exception(Exception)
        def exception_handler2(request, exception):
            pass

    assert exception_handler1 in blueprint._future_exceptions
    assert exception_handler2 in blueprint._future_exceptions


# Generated at 2022-06-14 07:35:24.785603
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    raise NotImplementedError
    """
    # assert ExceptionMixin.exception(*args, **kwargs) == "expected"

# Generated at 2022-06-14 07:35:31.754322
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import logging

    class TestExceptionMixin(ExceptionMixin):

        def _apply_exception_handler(self, handler: FutureException):
            pass

    testex = TestExceptionMixin()

    @testex.exception(Exception, logging.ERROR)
    def handleexception(request, exception):
        return "Exception"
    logging.ERROR.value
    # value == 40

    fu = set()

    fu.add(None)
    fu.add(123)
    fu.add(None)
    # fu == {None}
    fu.add(None)
    fu.add(123)
    fu.add(None)
    # fu == {None}

    assert set([FutureException(handleexception, (Exception,))]) == testex._future_exceptions

# Generated at 2022-06-14 07:35:39.984742
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyException(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    @MyException.exception(ValueError, ZeroDivisionError)
    def handler(self, request, exception):
        pass

    assert isinstance(MyException._future_exceptions.pop(), FutureException)

# Generated at 2022-06-14 07:35:40.890277
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:35:41.637864
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True

# Generated at 2022-06-14 07:35:45.073205
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    bp = Blueprint('test_bp')

    @bp.exception([Exception])
    async def exception_handler(request, exception):
        print('request',request)
        print('exception',exception)

# Generated at 2022-06-14 07:35:50.283725
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.exceptions import SanicException

    class FakeExceptionMixin(ExceptionMixin):
        pass

    fake_exception_mixin = FakeExceptionMixin()

    @fake_exception_mixin.exception(SanicException)
    async def fake_handler_func(request, exception):
        return None

    assert len(fake_exception_mixin._future_exceptions) == 1


# Generated at 2022-06-14 07:35:56.292184
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    bp = Blueprint(name="test_bp")
    assert(len(bp._future_exceptions) == 0)
    bp.exception(IndexError)(lambda x: x)
    assert(len(bp._future_exceptions) == 0)
    bp.exception(IndexError, apply=False)(lambda x: x)
    assert(len(bp._future_exceptions) == 1)



# Generated at 2022-06-14 07:36:57.721268
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exception_mixin = ExceptionMixin()
    exception_mixin.exception(ValueError)

# Generated at 2022-06-14 07:37:10.507530
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import sanic
    app = sanic.Sanic()

    @app.exception(IndexError)
    def index_error(request, exception):
        print("Index error")

    @app.exception(KeyError)
    async def key_error(request, exception):
        print("Key error")

    @app.exception([ZeroDivisionError, ValueError])
    def zero_division_or_value_error(request, exception):
        print("Zero division or value error")

    @app.exception()
    def all_exceptions(request, exception):
        print("All exceptions")

    @app.route("/index_error")
    def index_error_route(request):
        raise IndexError

    @app.route("/key_error")
    async def key_error_route(request):
        raise Key

# Generated at 2022-06-14 07:37:19.523318
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class mock_ExceptionMixin(ExceptionMixin):
        def __init__(self,*args):
            ExceptionMixin.__init__(self,*args)
            self.future_exceptions= set()
        def _apply_exception_handler(self,handler):
            self.future_exceptions.add(handler)

    mock_instance=mock_ExceptionMixin()
    @mock_instance.exception(Exception,ValueError,str)
    def handle_exception(request,exception):
        pass
    future_exception= FutureException(handle_exception,(Exception,ValueError,str))
    assert mock_instance.future_exceptions=={future_exception}
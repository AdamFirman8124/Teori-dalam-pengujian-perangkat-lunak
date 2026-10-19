

# Generated at 2022-06-14 07:27:21.783969
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint(name='test', version=1, url_prefix='')
    bp.exception(Exception)
    bp.exception(Exception, apply=True)


# Generated at 2022-06-14 07:27:23.231427
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert ExceptionMixin().exception(FutureException)

# Generated at 2022-06-14 07:27:27.613468
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class obj(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    @obj.exception(None)
    def handler(request, exception):
        return "Hello world!"

    assert handler(None, None) == "Hello world!"

# Generated at 2022-06-14 07:27:35.192883
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from sanic.app import Sanic

    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_exception_mixin = TestExceptionMixin()
    app = Sanic('test_ExceptionMixin_exception')

    @test_exception_mixin.exception
    def default_handler(request, exception):
        pass

    assert isinstance(test_exception_mixin.exception(default_handler), type(default_handler))
    assert len(test_exception_mixin._future_exceptions) == 1



# Generated at 2022-06-14 07:27:44.615388
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class B:
        exceptions = set()
        def _apply_exception_handler(self, handler: FutureException):
            self.exceptions.add(handler)

    b = B()
    e = ExceptionMixin()
    e.__init__(b)
    assert isinstance(e, ExceptionMixin)
    assert e._future_exceptions == set()
    assert b.exceptions == set()
    def f1():
        print("ok")
    e.exception(Exception)(f1)

# Generated at 2022-06-14 07:27:51.679716
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyExceptionMixin(ExceptionMixin):  # noqa
        pass
    exc_m = MyExceptionMixin()

    @exc_m.exception(Exception)
    def exception_handler(request, exception):
        pass

    assert len(exc_m._future_exceptions) == 1

# Generated at 2022-06-14 07:27:59.816792
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_exception_test(ExceptionMixin):
        def __init__(self):
            super(ExceptionMixin_exception_test,self).__init__()
            self.some_exception_handler = None
            self.some_exceptions = None
            self.apply_flag = None

        def _apply_exception_handler(self,handler:FutureException):
            self.some_exception_handler = handler
            self.some_exceptions = handler.exceptions
            self.apply_flag = True

    def test_function(request,some_exception):
        pass

    my_ExceptionMixin = ExceptionMixin_exception_test()
    my_ExceptionMixin.exception([ValueError],apply=False)(test_function)
    assert my_ExceptionMixin.some_exception_handler == None

# Generated at 2022-06-14 07:28:10.580948
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # setup
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from sanic.application import Sanic
    from sanic.blueprints import Blueprint

    bp = Blueprint('test_bp')

    # call the method exception of class ExceptionMixin
    bp.exception(ValueError)(handler_function)

    # check the results 
    assert bp._future_exceptions[0].handler == handler_function
    assert bp._future_exceptions[0].exceptions == ValueError
    assert bp._future_exceptions[0].kwargs == dict()


# Generated at 2022-06-14 07:28:14.173018
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exception_mixin = ExceptionMixin()
    assert len(exception_mixin._future_exceptions) == 0
    assert exception_mixin.exception()

if __name__ == '__main__':
    test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:28:24.840355
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    args_1 = (1,2,3)
    kwargs_1 = {'a' : 'b'}
    flag = False
    def decorator(handler_1):
        nonlocal flag
        nonlocal args_1
        nonlocal kwargs_1
        flag = True
        return 'decorator'
    class A(ExceptionMixin):
        def _apply_exception_handler(self, handler_1):
            pass
    a = A()
    assert hasattr(a, '_future_exceptions')
    assert len(a._future_exceptions) == 0
    a.exception(args_1, apply = True, **kwargs_1)(decorator)
    assert flag == True
    assert len(a._future_exceptions) == 1

# Generated at 2022-06-14 07:28:35.958725
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.response import text
    from sanic.exceptions import ServerError

    # Create a blueprint for testing exception
    blueprint = Blueprint('test_blueprint_exception', url_prefix='blueprint_exception')

    @blueprint.exception(IndexError)
    def handle_request_exception(request, exception):
        return text('Invalid exception', status=500)

    @blueprint.route('/exception')
    def exception(request):
        raise IndexError("Index Error 1")

    @blueprint.route('/exception2')
    def exception2(request):
        raise ServerError("server Error 2")

    app = Sanic('test_ExceptionMixin_exception')
    app.blueprint(blueprint)

    request, response = app.test_client.get

# Generated at 2022-06-14 07:28:48.981141
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test for checking exception and add exception_handler of that to self._future_exceptions
    def exception_handler(request, exception):
        return text('I am the exception_handler')
    mix_in = ExceptionMixin()
    mix_in.exception(Exception)(exception_handler)
    assert(mix_in._future_exceptions != None)

    # Test for the behavior that when apply is not True
    # then function exception_handler does not appear in self._apply_exception_handler
    mix_in = ExceptionMixin()
    mix_in.exception(Exception, apply=False)(exception_handler)
    assert(mix_in._future_exceptions != None)
    assert(mix_in._apply_exception_handler == None)

# Generated at 2022-06-14 07:28:56.495102
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    
    blueprint = Blueprint("test")
    
    @blueprint.exception(ValueError)
    def handler(request, exception):
        return request, exception
        
    # Assert that, when there is an exception, the request and exception will be returned
    request = None
    exception = ValueError("test")
    assert handler(request, exception) == (request, exception)

# Generated at 2022-06-14 07:29:01.700080
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler):
            pass

    bp = Blueprint()
    assert bp.exception is not None



# Generated at 2022-06-14 07:29:15.278489
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from .blueprint import Blueprint
    from .constants import HTTP_METHODS
    from sanic.exceptions import NotFound

    @Blueprint.exception(NotFound)
    def page_not_found(request, exception):
        return "Page not found", 404

    assert page_not_found in Blueprint._future_exceptions

    for method, view in Blueprint._routes.copy().items():
        if isinstance(view, list):
            for rule, _view in view:
                assert _view.__name__ == "page_not_found"
        elif isinstance(view, dict):
            for _, rule, _view in view[method]:
                assert _view.__name__ == "page_not_found"
        else:
            for rule, _view in view.items():
                assert _view.__name__

# Generated at 2022-06-14 07:29:22.292139
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.request import Request
    from sanic.exceptions import NotFound
    from sanic.response import text
    from sanic.blueprints import Blueprint

    blue_print = Blueprint('test_blueprint', url_prefix='test/')

    @blue_print.exception(NotFound)
    async def error_handler(request: Request, exception: NotFound):
        return text('Gotcha')

    @blue_print.route('error')
    async def error(request: Request):
        raise NotFound('aww')

    # Execute the blueprint
    request, response = blue_print.as_handler(
        request_factory=lambda:Request.init('/test/error', method='POST'))

    assert response._status_code == 404

# Generated at 2022-06-14 07:29:26.730330
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint as bp
    from werkzeug.exceptions import Unauthorized as UNAUTHORIZED
    from sanic.response import text

    @bp.exception(UNAUTHORIZED)
    def unauthorized(request, exception):
        return text("You are not authorized for this!")

    assert "exception" in dir(bp)

# Generated at 2022-06-14 07:29:34.338940
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A:
        def __init__(self):
            self._future_exceptions = set()
            self.exception_called = False
            self.apply_called = False
            
        def _apply_exception_handler(self, handler: FutureException):
            self.apply_called = True
            
    obj = A()
    exceptionMixin = ExceptionMixin.__new__(ExceptionMixin)
    exceptionMixin.__init__()

    exceptionMixin._apply_exception_handler = obj._apply_exception_handler
    exceptionMixin._future_exceptions = obj._future_exceptions

    @exceptionMixin.exception(Exception)
    def test(s):
        obj.exception_called = True
        
    test(1)

    assert obj.exception_called == True
    assert obj

# Generated at 2022-06-14 07:29:41.393989
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """Unit test for method exception of class ExceptionMixin"""
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.passed_future_exception = None

        def _apply_exception_handler(self, handler: FutureException):
            self.passed_future_exception = handler

    exception_mixin = ExceptionMixinTest()
    def handler():
        pass
    exception_mixin.exception(Exception)(handler)
    
    assert len(exception_mixin._future_exceptions) == 1
    assert exception_mixin.passed_future_exception in exception_mixin._future_exceptions



# Generated at 2022-06-14 07:29:52.445874
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic

    app = Sanic("ExceptionMixin")

    # when the apply = False
    @app.exception(Exception)
    async def error_handler(request, exception):
        return await response.json({"error": str(exception)}, status=500)

    assert len(app._future_exceptions) == 1

    # when the apply = True
    @app.exception(Exception, apply=True)
    async def error_handler(request, exception):
        return await response.json({"error": str(exception)}, status=500)

    assert len(app._future_exceptions) == 1

# Generated at 2022-06-14 07:30:04.452731
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self) -> None:
            super().__init__()
            self._future_exceptions = set()


    test_instance = TestExceptionMixin()
    def test_func(a, b):
        pass
    test_instance.exception(Exception)(test_func)
    test_instance.exception(Exception, a=1, b=2)(test_func)


if __name__ == "__main__":
    test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:30:13.415165
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # create an object of class ExceptionMixin
    class test(ExceptionMixin):
        def __init__(self):
            pass

    # create a ExceptionMixin instance
    obj = test()
    # create a handler
    def handler(request, exception):
        print(exception.args[0])
        return "exception"
    # to test the method exception
    obj.exception(TypeError)(handler)
    
    # test the funcitonality of exception.
    try:
        dict(name="john", age=None)
    except TypeError as e:
        assert handler("request", e) == "exception"
    # test the TypeError
    try:
        raise TypeError("test")
    except TypeError as e:
        assert handler("request", e) == "exception"

# Generated at 2022-06-14 07:30:18.407261
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Test_ExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa
    
    obj1 = Test_ExceptionMixin()
    obj1.exception()

# Generated at 2022-06-14 07:30:28.135096
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.exceptions import InvalidUsage
    from sanic.blueprints import Blueprint

    app = Sanic('test_ExceptionMixin_exception')
    blueprint = Blueprint('test_ExceptionMixin_exception', url_prefix='test')

    @blueprint.exception(Exception)
    def handler_Exception_false(request, exception):
        return request, exception

    @blueprint.exception(Exception, apply=False)
    def handler_Exception_true(request, exception):
        return request, exception

    @blueprint.route('/E_False')
    def handler_Exception_False(request):
        raise Exception

    @blueprint.route('/E_True')
    def handler_Exception_True(request):
        raise Exception


# Generated at 2022-06-14 07:30:37.137927
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.models.futures import FutureException
    from sanic.blueprints import Blueprint

    app = Sanic(__name__)

    bp = Blueprint(__name__)

    @bp.exception(ZeroDivisionError)
    def handler(request, exception):
        raise ZeroDivisionError
    bp.exception(ZeroDivisionError)(handler)
    assert len(bp._future_exceptions) == 1
    assert isinstance(list(bp._future_exceptions)[0], FutureException)

# Generated at 2022-06-14 07:30:41.089394
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    from sanic.response import text

    app = Blueprint(name='test_ExceptionMixin_exception')

    @app.exception(Exception, apply=False)
    async def handle_exception(request, exception):
        return text('Exception: %s' % exception)

    need_exc = ExceptionMixin()
    need_exc.exception(Exception, apply=True)

# Generated at 2022-06-14 07:30:41.696719
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass # TODO

# Generated at 2022-06-14 07:30:55.128590
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from types import FunctionType
    from typing import Callable
    from sanic.models.futures import FutureException
    from unittest.mock import MagicMock

    blueprint = Blueprint('test_ExceptionMixin_exception')
    blueprint._future_exceptions = set()

    def mock_apply_exception_handler(handler: FutureException):
        pass

    blueprint.exception.append_exception = True
    blueprint._apply_exception_handler = mock_apply_exception_handler

    def mock_handler(bp: Blueprint, err: Exception):
        pass

    deferred_mock_handler: Callable[[Exception], FunctionType] = blueprint.exception(MagicMock, apply=True)(mock_handler)

# Generated at 2022-06-14 07:31:08.271552
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic

    app = Sanic('test_ExceptionMixin_exception')
    @app.exception(ZeroDivisionError)
    def zero_division(request, exception):
        pass

    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self) -> None:
            super().__init__()

        def _apply_exception_handler(self, future_exception: FutureException):
            app.error_handler.add(future_exception.exceptions, future_exception.handler)

    obj = ExceptionMixinTest()
    obj.exception(ZeroDivisionError)(zero_division)

    assert len(app.error_handler.handlers) == 1


if __name__ == '__main__':
    import pytest

# Generated at 2022-06-14 07:31:14.868276
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Bp:
        pass
    
    Bp.__bases__ = (ExceptionMixin,)
    import sanic.exceptions
    @Bp.exception(sanic.exceptions.BaseSanicException)
    def handler(request, exception):
        return None

    future_exception = FutureException(handler, (sanic.exceptions.BaseSanicException,))
    assert future_exception in Bp._future_exceptions

# Generated at 2022-06-14 07:31:20.644407
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exception_mixin = ExceptionMixin()
    assert isinstance(exception_mixin.exception(), partial)

# Generated at 2022-06-14 07:31:26.463935
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.response import json

    class SanicTest(sanic.Sanic):
        @sanic.exception(Exception)
        def exception_handler(self, request, exception):
            return json(
                {"exception": "%s" % (exception.__class__.__name__,)},
                status=500,
            )

    app = SanicTest()

    @app.exception(Exception)
    def test(request, exception):
        return json(
            {"exception": "%s" % (exception.__class__.__name__,)},
            status=500,
        )

    @app.route("/test")
    def test_exception(request):
        raise Exception("Foo!")

    request, response = app.test_client.get("/test")


# Generated at 2022-06-14 07:31:30.839769
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exception_mixin = ExceptionMixin()
    assert len(exception_mixin._future_exceptions) == 0
    exception_mixin.exception(IndexError, FileNotFoundError)(print)
    assert len(exception_mixin._future_exceptions) == 1

# Generated at 2022-06-14 07:31:43.575545
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    '''This unit test does not yet cover all function branches'''
    from sanic.sanic import Sanic
    from sanic import Blueprint
    import random

    app = Sanic(__name__)
    blueprint_name = "{}_bp".format(random.random())
    exception_bp = Blueprint(blueprint_name)

    @exception_bp.exception(Exception)
    def handle_exception(request, exception):
        return request, exception

    app.blueprint(exception_bp)
    exception_bp.is_setup = True

    assert exception_bp._future_exceptions is not None
    assert len(exception_bp._future_exceptions) == 1
    exception = exception_bp._future_exceptions.pop()
    assert exception
    assert exception.handler == handle_exception
    assert exception.ex

# Generated at 2022-06-14 07:31:49.770593
# Unit test for method exception of class ExceptionMixin

# Generated at 2022-06-14 07:31:56.176215
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic, Blueprint

    app = Sanic('test_ExceptionMixin_exception')
    bp = Blueprint('test_ExceptionMixin_exception')
    bp.exception(IndexError, apply=False)
    assert len(bp._future_exceptions) == 1
    assert isinstance(bp._future_exceptions.pop(), FutureException)



# Generated at 2022-06-14 07:32:07.456956
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class _Sanic(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.exception_hander = None
        def _apply_exception_handler(self, handler: FutureException):
            self.exception_hander = handler
    sanic_instance = _Sanic("sanic")
    assert sanic_instance.exception_hander is None
    def testExceptionHandler(request, exception):
        return request, exception

    sanic_instance.exception(ValueError, apply=True)(testExceptionHandler)
    future_exception = FutureException(testExceptionHandler, (ValueError,))
    assert sanic_instance.exception_hander is future_exception 

# Generated at 2022-06-14 07:32:16.285647
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic

    app = Sanic('test_ExceptionMixin_exception')

    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler):
            pass

    testExceptionMixin = TestExceptionMixin(app=app)

    try:
        @testExceptionMixin.exception(Exception, 404)
        def testing(request, exception):
            assert True

        testing(None, None)
    except AssertionError:
        assert False
    else:
        assert True

# Generated at 2022-06-14 07:32:23.248558
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import types

    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    TestExceptionMixin()

    exc_mixin = TestExceptionMixin()
    @exc_mixin.exception()
    def func_exc():
        pass
    assert isinstance(func_exc, types.FunctionType)

# Generated at 2022-06-14 07:32:28.986979
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    testExceptionMixin = TestExceptionMixin()
    assert testExceptionMixin._future_exceptions == set()
    assert testExceptionMixin.exception(ValueError)


# Generated at 2022-06-14 07:32:45.692849
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    obj = ExceptionMixin()
    global g_handler
    global g_exceptions
    g_handler = None
    g_exceptions = None
    class Handler:
        def __init__(self):
            pass
        def __call__(self, a):
            pass
    g_handler = Handler()

    decorator = obj.exception(g_handler, g_exceptions)
    assert decorator(g_handler) == g_handler

# Generated at 2022-06-14 07:32:52.092163
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin_test(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print(self)

    import random
    import string
    ExceptionMixin_test().exception(random.choice(string.ascii_lowercase), apply=True)(
        random.choice(string.ascii_lowercase))

# Generated at 2022-06-14 07:33:01.819662
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixin1(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    exceptionMixin1 = ExceptionMixin1()

    @exceptionMixin1.exception('asdf')
    def test():
        pass

    assert len(exceptionMixin1._future_exceptions) > 0
    assert str(exceptionMixin1._future_exceptions.pop()) == \
        "<FutureException handler=test, exceptions=('asdf',)>"

# Generated at 2022-06-14 07:33:08.033839
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            handler.handler()

    a = A()
    assert a._future_exceptions == set()
    @a.exception(ZeroDivisionError)
    def zero_handler(error):
        assert isinstance(error, ZeroDivisionError)
    a.apply_exception_handlers()

# Generated at 2022-06-14 07:33:15.283323
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    runner = Sanic('test_ExceptionMixin_exception')
    bp = Blueprint("test_ExceptionMixin_exception")

    async def handler(request, exception):
        pass

    bp.exception(handler)
    runner.register_blueprint(bp)
    assert runner.error_handler.exception_handler == handler

# Generated at 2022-06-14 07:33:24.733244
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            self.app = 'app'
            super().__init__()

        def add_route(self, *args, **kwargs):
            pass

        def _apply_exception_handler(self, handler: FutureException):
            from sanic.response import text
            return lambda req, exc: text('Something bad happened', 500)

    test = TestExceptionMixin()
    assert isinstance(test._future_exceptions, set)

    @test.exception(Exception)
    def handler():
        return 'handler'
    assert test._future_exceptions == {
        FutureException(handler, (Exception,))
    }

    @test.exception(Exception, apply=False)
    def handler2():
        return 'handler2'

# Generated at 2022-06-14 07:33:36.298499
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Create instance of class ExceptionMixin
    ex_mixin = ExceptionMixin()

    # Create method to be used as exception handler
    def handle_error(request, exception):
        pass

    # Call method exception
    exception_handler = ex_mixin.exception(handle_error)

    # Check if returned value is handle_error
    assert exception_handler is handle_error

    # Get list of all future exceptions
    future_exceptions = ex_mixin._future_exceptions

    # Check if list contains one element
    assert len(future_exceptions) == 1

    # Check if the element is of class FutureException
    assert isinstance(future_exceptions.pop(), FutureException)

# Generated at 2022-06-14 07:33:43.623424
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.exception_handler = None

        def _apply_exception_handler(self, handler: FutureException):
            self.exception_handler = handler

    exception_mixin_test = ExceptionMixinTest()

    @exception_mixin_test.exception(apply=True)
    async def handler():
        pass

    assert_equal(handler, exception_mixin_test.exception_handler.handler)


if __name__ == '__main__':
    response = nose.runmodule()

# Generated at 2022-06-14 07:33:49.740235
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    blueprint = Blueprint(url_prefix='/prefix')

    @blueprint.exception(TypeError)
    async def handle_exception(request, exception):
        return text('Exception')

    assert blueprint._future_exceptions is not None
    assert len(blueprint._future_exceptions) == 1

# Generated at 2022-06-14 07:33:56.195557
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    blueprint = blueprint()
    assert blueprint._future_exceptions == set()

    @blueprint.exception([Exception])
    def exception_handler(request):
        return 'exception_handler'

    assert len(blueprint._future_exceptions) == 1

# Generated at 2022-06-14 07:34:17.431281
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest

    from sanic.blueprints import Blueprint
    from sanic.exceptions import ServerError

    bp = Blueprint('test_ExceptionMixin_exception')

    @bp.exception(ServerError)
    def custom_exception_handler(request, exception):
        print('Exception Mixin Blueprint')
        return 'A ServerError caused this exception handler to fire'

    try:
        raise ServerError('Test exception')
    except ServerError as e:
        value = bp.handle_request_exception(e, 'ExceptionMixin')

    assert value == 'A ServerError caused this exception handler to fire'


# Generated at 2022-06-14 07:34:30.058475
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestException(Exception):
        pass
    class Test:
        def __init__(self):
            self._future_exceptions = set()
        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    test = Test()
    test.__class__.__bases__ = (ExceptionMixin,)
    @test.exception(Exception)
    def handle_exception1(request, exception):
        pass
    @test.exception(zerodivisionerror)
    def handle_exception2(request, exception):
        pass
    @test.exception(TestException)
    def handle_exception3(request, exception):
        pass
    assert handle_exception1 in test._future_exceptions
    assert handle_exception2 in test._future

# Generated at 2022-06-14 07:34:41.032877
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.clients import Client
    from sanic.exceptions import ServerError

    client = Client()

    class A(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    a = A()

    @a.exception(apply=False)
    def handler(request, e):
        assert isinstance(e, ServerError)
        return 'OK'

    assert isinstance(handler, FutureException)
    h = handler.handler
    e = ServerError(status_code=500, message='Server Error', payload=None)
    assert h(None, e) == 'OK'

# Generated at 2022-06-14 07:34:49.207425
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic import Blueprint
    from sanic.exceptions import SanicException
    from sanic.response import text


    class MyException(SanicException):
        status_code = 403


    app = Sanic('test_ExceptionMixin_exception')
    bp = Blueprint('test_ExceptionMixin_exception', url_prefix='test')

    @bp.exception(MyException)
    def handle_exception(request, exception):
        return text('internal error', 500)

    @bp.route('/')
    def handler(request):
        raise MyException('omg!')

    app.blueprint(bp)

    request, response = app.test_client.get('/test/')
    assert response.status == 500
    assert response.text == 'internal error'

# Generated at 2022-06-14 07:34:56.664387
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Futures(ExceptionMixin):

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    bp = Futures()
    bp.exception(test)
    assert bp._future_exceptions.__len__() == 1



# Generated at 2022-06-14 07:35:02.971093
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            assert (handler in self._future_exceptions)
            raise NotImplementedError

    blue = Blueprint()

    @blue.exception(ZeroDivisionError)
    def handle_division_error(request, exception):
        pass


# Generated at 2022-06-14 07:35:09.741739
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    bp = Blueprint("test_bp", url_prefix='/test')

    def test_exception_handler(request, exception):
        pass

    bp.exception(Exception)(test_exception_handler)

    assert len(bp._future_exceptions) == 1
    assert Exception in bp._future_exceptions.pop().exceptions

# Generated at 2022-06-14 07:35:20.180906
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_exception_mixin = TestExceptionMixin()
    exceptions = [Exception]
    def test():
        return 'test'

    decorator = test_exception_mixin.exception(*exceptions)
    handler = decorator(test)
    assert len(test_exception_mixin._future_exceptions) == 1
    assert test_exception_mixin._future_exceptions.pop() == FutureException(handler, exceptions)

# Generated at 2022-06-14 07:35:31.889383
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic

    app = Sanic()

    @app.exception(IndexError)
    async def handler_error_instance(request, exception):
        """
        This method will provide the base frame to handle global exceptions
        """
        pass

    assert hasattr(app, "exception")
    assert hasattr(app, "_future_exceptions")
    
    @app.exception(ValueError, apply=False)
    async def handler_error_instance(request, exception):
        """
        This method will provide the base frame to handle global exceptions
        """
        pass
    
    assert hasattr(app, "_apply_exception_handler")

# Generated at 2022-06-14 07:35:43.572189
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def exception_func_1():
        pass

    def exception_func_2():
        pass

    instance = ExceptionMixin()
    assert len(instance._future_exceptions) == 0

    with pytest.raises(TypeError):
        instance.exception(exception_func_1())
    assert len(instance._future_exceptions) == 0

    instance.exception(Exception)(exception_func_1)
    assert len(instance._future_exceptions) == 1

    instance.exception(IOError)(exception_func_2)
    assert len(instance._future_exceptions) == 2

    with pytest.raises(NotImplementedError):
        instance._apply_exception_handler(None)

# Generated at 2022-06-14 07:36:30.732695
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic import Blueprint

    app = Sanic('test_exception_mixin_exception')
    bp = Blueprint('test_exception_mixin_exception')

    @bp.exception(ValueError)
    def handler_for_value_error(request, exception):
        return text('Exception: %s' % exception)

    # bp's exception method is triggered, bp.exception is an instance of Set
    assert bp.exception(ValueError)
    assert type(bp._future_exceptions) is set
    # bp.exception is an instance of FutureException
    assert bp._future_exceptions.pop()

    app.blueprint(bp)

    request, response = app.test_client.get('/')
    assert response.status == 500



# Generated at 2022-06-14 07:36:39.570257
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class Server(ExceptionMixin):

        @exception
        def exception(self, *args):
            return None

        @exception
        def apply_exception_handler(self, handler: FutureException):
            return None

    s = Server()
    assert (s.exception is not None)

    @s.exception(IndexError)
    def exception_handler(request, exception):
        return None

    assert (exception_handler is not None)


if __name__ == '__main__':
    test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:36:40.418555
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:36:53.285546
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinClass(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass

        def exception(self):
            pass

    exception_mixin = ExceptionMixinClass()

    @exception_mixin.exception(NameError)
    def ee():
        return 32 * 2
    first = exception_mixin._future_exceptions.pop()
    assert None == first.kwargs
    assert ee == first.handler
    assert (NameError,) == first.exceptions

    @exception_mixin.exception([ZeroDivisionError, ValueError])
    def e():
        return 32 * 2
    first = exception_mixin._future_exceptions.pop()
    assert None == first.kwargs
    assert e == first.handler

# Generated at 2022-06-14 07:36:54.440082
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass


# Generated at 2022-06-14 07:37:03.924777
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    from sanic.response  import text
    from sanic.exceptions import InvalidUsage

    bp = Blueprint('test')

    @bp.exception(InvalidUsage)
    def exception_handler(request, exception):
        return text('exception: {}'.format(exception), 500)

    assert len(bp._future_exceptions) == 1
    assert isinstance(bp._future_exceptions.pop(), FutureException)

    # Make sure that the class is included in the sanic.Blueprint
    assert bp.__class__.__bases__[0] == ExceptionMixin

# Generated at 2022-06-14 07:37:11.650498
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprint import Blueprint

    bp = Blueprint('name', url_prefix='url_prefix')
    bp.exception([ZeroDivisionError, IndexError])(lambda: 0)
    assert len(bp._future_exceptions) == 1
    assert bp._future_exceptions.pop().handler() == 0
    bp.exception([ZeroDivisionError, IndexError])(lambda: 0)
    assert len(bp._future_exceptions) == 1
    assert len(bp._future_exceptions.pop().exceptions) == 2

# Generated at 2022-06-14 07:37:24.398933
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.exceptions import ServerError
    from sanic.server import HttpProtocol
    from sanic.blueprints import Blueprint
    from sanic.views import CompositionView
    from sanic.response import text

    class TestHttpProtocol(HttpProtocol):
        pass

    route = Blueprint('test', url_prefix='test')

    @route.exception(ServerError)
    def handler(request, exception):
        # here it is handler
        return text('OK')

    @route.route('/test', methods=['POST'])
    def handler(request):
        # here it is handler, but not decorated
        return text('OK')

    app = Sanic('test')
    app.blueprints = [route]
    app.error_handler = TestHttpProtocol.error_handler
    app.request_middleware
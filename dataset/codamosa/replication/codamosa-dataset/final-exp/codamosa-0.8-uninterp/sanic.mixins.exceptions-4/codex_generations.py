

# Generated at 2022-06-14 07:27:17.561476
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinClass:
        def __init__(self, *args, **kwargs):
            # create an empty set
            self.exceptions = set()

        def apply_exception_handler(self, handler):
            self.exceptions.add(handler)

    c = ExceptionMixinClass()
    exception_mixin = ExceptionMixin(c)
    exception_mixin(ExceptionMixinClass)
    assert excepti

# Generated at 2022-06-14 07:27:20.649859
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    test exception method of class ExceptionMixin
    """
    from sanic import Sanic

    app = Sanic('test')
    app.blueprint(ExceptionMixin)

# Generated at 2022-06-14 07:27:31.838317
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.views import HTTPMethodView
    import inspect

    class ViewA(HTTPMethodView):
        def get(self, request):
            return "view a"

        def post(self, request):
            return "view b"

    blueprint = Blueprint('test_ExceptionMixin_exception', url_prefix='/test')
    view = ViewA.as_view()

    blueprint.add_route(view, '/view')
    bp_exceptions_len = len(blueprint._future_exceptions)

    # test exception decorator
    @blueprint.exception(ValueError)
    def exc_handler(request, exception):
        return "test_ExceptionMixin_exception"

    assert len(blueprint._future_exceptions) == bp_ex

# Generated at 2022-06-14 07:27:47.478271
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FakeSanicExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()
            self._applied_exceptions: Set[FutureException] = set()
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler):
            self._applied_exceptions.add(handler)

    class FakeView:
        pass

    fe1 = FakeView()
    fe2 = FakeView()
    fem = FakeSanicExceptionMixin()

    @fem.exception(ValueError)
    def fe1(request, exception):
        pass


# Generated at 2022-06-14 07:27:59.177206
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest

    from sanic.blueprints import Blueprint

    from sanic.exceptions import SanicException

    class TestBlueprintException(Blueprint):
        pass

    blueprint = TestBlueprintException()
    blueprint_exception = unittest.TestCase(blueprint)

    @blueprint_exception.exception(SanicException)
    def sanic_exception(request, exception):
        pass

    @blueprint_exception.exception([FileNotFoundError])
    def file_not_found_error(request, exception):
        pass

    assert len(blueprint._future_exceptions) == 2

    assert SanicException in blueprint._future_exceptions[0].exception_types
    assert FileNotFoundError in blueprint._future_exceptions[1].exception_types


# Generated at 2022-06-14 07:28:03.268777
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import ServerError

    blueprint = Blueprint('test_blueprint', url_prefix='/test_blueprint')
    blueprint.exception(ServerError)(lambda request, exception : 'Error')

# Generated at 2022-06-14 07:28:15.465883
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Foo(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler: FutureException):
            self._future_exceptions.add(handler)

    foo = Foo()

    # noinspection PyUnusedLocal
    @foo.exception(BaseException)
    def error_handler(req, exc):
        pass

    @foo.exception(Exception, apply=False)
    def another_error_handler(req, exc):
        pass

    assert len(foo._future_exceptions) == 1
    for future_exception in foo._future_exceptions:
        assert len(future_exception.exceptions) == 1
        assert future_exception.exceptions == (BaseException,)
       

# Generated at 2022-06-14 07:28:18.503440
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Sanic_Blueprint_Test(ExceptionMixin):
        pass
    exceptions = {'Exception': Sanic_Blueprint_Test().exception(Exception)}
    try:
        raise Exception()
    except Exception:
        assert True

# Generated at 2022-06-14 07:28:28.502776
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from .conftest import Sanic, Blueprint
    from sanic import SanicException
    app = Sanic('sanic')
    bp = Blueprint('sanic')

    @app.route('/')
    def handler(request):
        raise SanicException('msg')

    @bp.exception(SanicException)
    def handler(request, exception):
        return text('global')

    app.blueprint(bp)

    request, response = app.test_client.get('/')
    assert response.text == 'global'
    assert response.status == 500



# Generated at 2022-06-14 07:28:37.755657
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.exceptions import ServerError
    from sanic.models.futures import FutureException
    from sanic import Sanic

    app = Sanic('test_exception_mixin_exception')

    @app.exception([ServerError])
    def test(request, exception):
        assert exception.status_code == 500
        return text('Internal Server Error')

    request, response = app.test_client.get('/')
    assert response.status == 500
    assert response.text == 'Internal Server Error'
    assert isinstance(app.exception_handlers[0], FutureException)

# Generated at 2022-06-14 07:28:49.235779
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from unittest.mock import Mock, patch

    class Blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            assert handler is future_exception

    blueprint = Blueprint()
    @blueprint.exception(Exception)
    def handler():
        pass

    future_exception = FutureException(handler, (Exception,))
    assert blueprint._future_exceptions == {
        future_exception
    }

# Generated at 2022-06-14 07:29:02.085909
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    from sanic.exceptions import SanicException
    from sanic.response import json
    from sanic.server import HttpProtocol
    from sanic.testing import SanicTestClient
    from sanic.views import HTTPMethodView
    from werkzeug.test import Client

    class TestBlueprint(Blueprint):
        def _exception_handler(self, request, exception):
            return json({"exception": str(exception)}, status=exception.status_code)

        def _register_on_app(self, app: Sanic):
            super()._register_on_app(app)
            app.error_handler.add(SanicException, self._exception_handler)


# Generated at 2022-06-14 07:29:10.660067
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyClass(ExceptionMixin):
        def __init__(self):
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler):
            assert handler == futur_exp

        def _add_route(self, handler, uri, methods):
            def hdl():
                print("handler")

            return hdl

    def my_handler():
        print('my_handler')

    futur_exp = FutureExceptio

# Generated at 2022-06-14 07:29:16.765242
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class testExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            return

    test = testExceptionMixin()
    class testException(Exception):
        def __init__(self):
            super().__init__()

    @test.exception(testException)
    def exception_handler(self, exception: Exception):
        return

    assert exception_handler in test._future_exceptions

# Generated at 2022-06-14 07:29:24.153716
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MixinTest(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass
    m = MixinTest()
    assert len(m._future_exceptions) == 0

    @m.exception(IndexError)
    def decorator(request, e):
        pass
    assert len(m._future_exceptions) == 1

    # No effect
    def decorator_without_add(request, e):
        pass
    m.exception(IndexError)(decorator_without_add)
    assert len(m._future_exceptions) == 1

# Generated at 2022-06-14 07:29:26.226510
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    exception_mixin = ExceptionMixin()
    exception = AssertionError()
    assert exception_mixin.exception(exception) is not None

# Generated at 2022-06-14 07:29:31.746503
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    bp = Blueprint("test_bp", url_prefix="test")
    assert bp._future_exceptions == set()

    @bp.exception(Exception)
    def catcher(request, exception):
        return text("Exception catched!")

    assert len(bp._future_exceptions) == 1

    fe = bp._future_exceptions.pop()
    assert fe.handler is catcher
    assert fe.exceptions == (Exception,)

# Generated at 2022-06-14 07:29:35.900256
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import types

    class Sample:
        pass

    sample = Sample()

    sample.exception = types.MethodType(ExceptionMixin.exception, sample)

    assert callable(sample.exception)

# Generated at 2022-06-14 07:29:45.748730
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import NotFound
    from sanic.models.futures import FutureException
    from sanic.response import text

    assert not hasattr(Blueprint, 'exception')

    bp = Blueprint('test', url_prefix='test')
    assert not bp._future_exceptions

    @bp.exception(NotFound)
    def handler():
        return text('error')

    assert len(bp._future_exceptions) == 1
    assert bp._future_exceptions == {FutureException(handler, (NotFound,))}

# Generated at 2022-06-14 07:29:54.351821
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint

    blueprint = Blueprint("test_ExceptionMixin_exception", url_prefix="test")

    @blueprint.exception(GiveMyException)
    def give_my_exception(request, exception):
        pass

    assert blueprint.has_future_exception(GiveMyException) is True

    @blueprint.exception([GiveMyException])
    def give_my_exception2(request, exception):
        pass

    assert blueprint.has_future_exception(GiveMyException) is True


# Generated at 2022-06-14 07:30:10.173440
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from unittest import mock

    class My_BP(Blueprint, ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            pass

    bp = My_BP(name="test")

    bp.exception(ZeroDivisionError)(lambda request: 1)
    request = Request("GET", "/", stream=mock.Mock())
    bp.handle_request(request, Exception())
    bp.handle_request(request, ZeroDivisionError())


# Generated at 2022-06-14 07:30:21.864437
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    def test_handler():
        pass
    
    from sanic.blueprints import Blueprint
    @Blueprint.exception(ZeroDivisionError)
    def exceptionHandler():
        pass
    blueprint = Blueprint('test_blueprint', url_prefix='test')
    blueprint._apply_exception_handler = test_handler
    
    blueprint.exception(ZeroDivisionError)
    assert blueprint._future_exceptions == set(exceptionHandler)

    # blueprint.exception(ZeroDivisionError)
    # blueprint._future_exceptions == blueprint._future_exceptions #empty set
    # blueprint.exception(ZeroDivisionError, ValueError)
    # blueprint._future_exceptions == blueprint._future_exceptions #empty set

# Generated at 2022-06-14 07:30:29.581149
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class A(ExceptionMixin):
        pass

    a = A()
    
    # Test exception with function
    @a.exception(TypeError, ZeroDivisionError)
    def handler():
        pass
    assert len(a._future_exceptions) == 1
    future_exception = a._future_exceptions.pop()
    assert future_exception.handler == handler
    assert future_exception.exceptions == (TypeError, ZeroDivisionError)
    assert future_exception.args == {}

    @a.exception([TypeError, ZeroDivisionError])
    def handler():
        pass
    assert len(a._future_exceptions) == 1
    future_exception = a._future_exceptions.pop()
    assert future_exception.handler == handler

# Generated at 2022-06-14 07:30:38.713474
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.blueprints import Blueprint
    app = Sanic("sanic-blueprint")

    blueprint = Blueprint("blueprint", url_prefix="/blueprint")

    @blueprint.exception(Exception, apply=False)
    def handler(request, exception):
        return response.text("I caught an exception: {}".format(exception))

    # Here we are sure that exceptions are added to _future_exceptions
    assert isinstance(blueprint._future_exceptions, set)

    # Here we are sure that handler is created and returned
    assert callable(handler)

# Generated at 2022-06-14 07:30:51.556659
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.exceptions import Forbidden
    from sanic.models.futures import FutureException
    from sanic.response import text
    from sanic.views import HTTPMethodView

    class ExceptionMixinView(HTTPMethodView, ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler: FutureException):
            self._future_exceptions.add(handler)

        async def get(self, request):
            pass

        async def post(self, request):
            pass

    app = Sanic('test_sanic')
    exception_view = ExceptionMixinView.as_view()


# Generated at 2022-06-14 07:30:57.961745
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprint import Blueprint
    from sanic.models.exception_handler import ExceptionHandler
    blueprint = Blueprint("Test_ExceptionMixin", url_prefix="/test")

    @blueprint.exception(IndexError)
    async def index_error_handler(request, exception):
        assert True

    @blueprint.exception(IndexError, NameError)
    async def mixed_error_handler(request, exception):
        assert True

    @blueprint.exception([IndexError, NameError])
    async def mixed_error_handler2(request, exception):
        assert True


# Generated at 2022-06-14 07:31:05.065405
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Unit test for method exception of class ExceptionMixin

    from sanic.blueprints import Blueprint

    blueprint = Blueprint("test", url_prefix="/test")

    def blueprint_exception(request, exception):
        return request.url

    blueprint.exception(Exception)(blueprint_exception)
    assert blueprint._future_exceptions

## Unit test for method _apply_exception_handler of class ExceptionMixin

# Generated at 2022-06-14 07:31:06.287154
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # TODO
    assert True

# Generated at 2022-06-14 07:31:11.599251
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    exception_mixin_ins = ExceptionMixin()
    blueprint_ins = Blueprint(None, None)
    blueprint_ins._future_exceptions = set()

    @blueprint_ins.exception(Exception)
    def exception_handler(request, exception):
        return None

    assert exception_mixin_ins.exception(KeyError)(None)
    assert type(blueprint_ins._future_exceptions) == set

# Generated at 2022-06-14 07:31:19.190557
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.exceptions import SanicException

    class MySanicApp(Sanic, ExceptionMixin):
        pass

    async def exception_handler(request, exception):
        return text("Handled Exception")

    app = MySanicApp()
    app.exception(SanicException, apply=True)(exception_handler)

    assert app.error_handler.get(SanicException) == exception_handler

# Generated at 2022-06-14 07:31:33.706014
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super(Blueprint, self).__init__(*args, **kwargs)
            self.exception_handler = []
            self.exceptions = []

        def _apply_exception_handler(self, ex):
            self.exception_handler.append(ex)

    blueprint = Blueprint('test_Blueprint_exception')
    blueprint.exception(ValueError, Exception)
    assert len(blueprint._future_exceptions) == 1
    assert len(blueprint.exception_handler) == 1
    assert isinstance(blueprint.exception_handler[0], FutureException)



# Generated at 2022-06-14 07:31:42.770589
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    bp = Blueprint(name="", register=False)
    @bp.exception(apply=False)
    def exception_handler(request, exception):
        pass
    @bp.exception(ValueError, apply=False)
    def exception_handler_2(request, exception):
        pass
    @bp.exception([ValueError, IndexError], apply=False)
    def exception_handler_3(request, exception):
        pass
    assert len(bp._future_exceptions) == 3

# Generated at 2022-06-14 07:31:53.475806
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    test_ExceptionMixin = TestExceptionMixin()
    
    def decorator(decorator_handler):
        def decorator_inner(inner_handler):
            return decorator_handler
        return decorator_inner

    applied = test_ExceptionMixin.exception(
        decorator, apply = True,
        exceptions = [*(Exception,), *(ZeroDivisionError,)]
    )

    assert callable(applied)

# Generated at 2022-06-14 07:31:59.980191
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic

    app = Sanic()
    blueprint = Blueprint(app)

    @blueprint.exception((ZeroDivisionError, RuntimeError), pass_error_type=True)
    def handler(request, exception):
        return f"Got a {exception}"

    assert len(blueprint._future_exceptions) == 1



# Generated at 2022-06-14 07:32:03.654950
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @Object.exception
    def exception_handler(request, exception):
        pass
    future_exception = FutureException(exception_handler, (Exception,))
    assert future_exception in Object._future_exceptions


# Generated at 2022-06-14 07:32:10.308237
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    import asyncio
    from sanic.exceptions import InvalidUsage
    from sanic.response import text
    from sanic.server import HttpProtocol
    
    # will use later
    app = None
    cli = None

    class ExceptionMixinTest(ExceptionMixin, HttpProtocol):
        pass

    class TestExceptionMixin(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            global cli
            global app
            app = Sanic('app1')

            @app.middleware('request')
            async def handler(request):
                request['a'] = 'dsaf'

            @app.middleware('response')
            async def handler(request, response):
                response.text = 'dsaf'
                response.headers['Content-Type']

# Generated at 2022-06-14 07:32:20.941889
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    #test_ExceptionMixin_exception
    #unit case
    @app.exception(ZeroDivisionError)
    def zero_divison(request,exception):
        return text('Oops! Zero division error.')
    test_case={"args":[],"apply":True,"decorator":decorator,"exceptions":[ZeroDivisionError]}
    assert zero_divison.__name__=="zero_divison"
    assert zero_divison.__code__.co_argcount==2
    test_instance=ExceptionMixin()
    test_instance._apply_exception=apply_exception
    test_instance.exception(*test_case["exceptions"],apply=test_case["apply"])(zero_divison)(*test_case["args"])
    assert len(test_instance._future_exceptions)==1

# Generated at 2022-06-14 07:32:32.424479
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    Test that the method exception of class ExceptionMixin actually
    can catch an exception and print the proper
    message if that exception is thrown.
    """
    
    class Route:
        def __init__(self, *args, **kwargs):
            pass

        async def get(self, request, *args, **kwargs):
            raise Exception('Raise an exception')

    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            ExceptionMixin.__init__(self, *args, **kwargs)
            self.route = Route()

        def _apply_exception_handler(self, handler: FutureException):
            function = handler.handler
            exceptions = handler.exceptions

# Generated at 2022-06-14 07:32:42.076716
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class DummyClass(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            pass

    dummy_class = DummyClass()
    dummy_exception = Exception
    dummy_handler = lambda: None
    assert len(dummy_class._future_exceptions) == 0

    dummy_class.exception(dummy_exception)(dummy_handler)

    assert len(dummy_class._future_exceptions) == 1
    assert (
        dummy_handler in [
            future_exception.handler
            for future_exception in dummy_class._future_exceptions
        ]
    )

# Generated at 2022-06-14 07:32:47.370485
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    exception_mixin = TestExceptionMixin()
    exception_mixin.exception(None)
    assert(ExceptionMixin)

# Generated at 2022-06-14 07:33:08.407056
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class CustomClass(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super(CustomClass, self).__init__(*args, **kwargs)

    cc = CustomClass()
    assert cc.__dict__ == {'_future_exceptions': set()}
    assert callable(cc.exception(Exception))

# Generated at 2022-06-14 07:33:19.521896
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Base class ExceptionMixin
    class ExceptionMixinTest:
        def __init__(self, *args, **kwargs):
            pass
        def _apply_exception_handler(self, handler):
            pass
    test = ExceptionMixin(ExceptionMixinTest)
    apply = True
    exceptions = (1,2)
    func = lambda x: x

    # call the decorator that calls exception
    decorator = test.exception(exceptions)
    # call the decorator
    result = decorator(func)
    assert result == func
    # check if set works
    assert len(test._future_exceptions) == 1

# Generated at 2022-06-14 07:33:26.766702
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.exceptions import RequestTimeout

    try:
        class TestException(ExceptionMixin):
            def _apply_exception_handler(self, handler: FutureException):
                pass

            def exception_handler(self, request, exception):
                return 'ok'

    except TypeError:
        assert False

    test = TestException()

    @test.exception(RequestTimeout)
    def handler(request, exception):
        return 'ok'

    assert len(test._future_exceptions) == 1
    assert handler is test.exception_handler

# Generated at 2022-06-14 07:33:32.051118
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import sanic

    class Blueprint(ExceptionMixin, sanic.Blueprint):
        pass

    blueprint = Blueprint("test", url_prefix="test")

    @blueprint.exception(Exception)
    async def handler(request, exception):
        return request, exception

    assert len(blueprint._future_exceptions) > 0

# Generated at 2022-06-14 07:33:37.998704
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    inst = ExceptionMixin()

    def handler(request, exception,**kwargs):
        pass

    inst.exception(1)(handler)

    current_exc_set = inst._future_exceptions

    assert len(current_exc_set) == 1
    assert current_exc_set.pop().exceptions == (1,)

# Generated at 2022-06-14 07:33:44.932794
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin:
        apply = False

        def __init__(self, *args, **kwargs):
            self._future_exceptions = set()

        def _apply_exception_handler(self, handler):
            if self.apply:
                self._future_exceptions.add(handler)

    class TestExceptionHandler:
        def __init__(self):
            self.handler_args = []

    class TestException:
        pass

    test_except_handler = TestExceptionHandler()
    test_except_mixin = TestExceptionMixin()
    test_except_mixin.exception([TestException], apply=True)(test_except_handler)
    assert isinstance(
        test_except_mixin._future_exceptions.pop(), TestExceptionHandler
    )

    # Test that the exception mixin returns the handler

# Generated at 2022-06-14 07:33:57.538488
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """unit test method ExceptionMixin.exception"""
    # test:
    #    def exception(self, *exceptions, apply=True)
    #        :param args: List of Python exceptions to be caught by the handler
    #        :param kwargs: Additional optional arguments to be passed to the
    #            exception handler

    #        :return a decorated method to handle global exceptions for any
    #            route registered under this blueprint.
    from sanic import Blueprint
    bp = Blueprint('bp')
    exception_mixin = ExceptionMixin()

    @bp.exception(AttributeError, apply=True)
    def handler(request, exception):
        print("Exception: {}".format(exception))
        return "handler"
    bp.name = "bp"
    bp._apply_exception_handler('')
    # assert

# Generated at 2022-06-14 07:34:06.415399
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Test_ExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError  # noqa

    test_exception_mixin = Test_ExceptionMixin()
    test_exception_mixin.exception(1)
    assert isinstance(test_exception_mixin, Test_ExceptionMixin)

# Generated at 2022-06-14 07:34:17.418403
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.testing import HOST, PORT

    class MockBlueprint(ExceptionMixin, Blueprint):
        called = False

        def _apply_exception_handler(self, handler: FutureException):
            self.called = True

    blueprint = MockBlueprint('MockBlueprint')

    @blueprint.exception(ZeroDivisionError)
    def exception_handler(request, exception):
        return response.text('error')

    assert blueprint.called

    app = Sanic('test_ErrorHandling_handle_error')
    blueprint = app.register_blueprint(blueprint)

    @app.route('/post', methods=['POST'])
    async def handler(request):
        1 / 0

    request, response = app.test_client.post('/post')
    assert request

# Generated at 2022-06-14 07:34:25.626795
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TempException(ExceptionMixin):
        def __init__(self):
            super().__init__()

        def _apply_exception_handler(self, handler):
            assert handler.handler == _handler
            assert handler.exceptions == (ValueError, )

    temp = TempException()
    _handler = lambda *args, **kwargs: None
    temp.exception(ValueError)(_handler)

# Generated at 2022-06-14 07:35:01.957619
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            raise NotImplementedError # noqa

    assert TestExceptionMixin().exception is not None
    assert TestExceptionMixin().exception(Exception) is not None

# Generated at 2022-06-14 07:35:15.621650
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionDummy(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    dummy = ExceptionDummy()
    assert not dummy._future_exceptions

    def handler_exception_1(req, res):
        return 'exception_1'

    @dummy.exception(ValueError, apply=False)
    def func_1():
        raise ValueError()

    @dummy.exception(
        [ValueError, ZeroDivisionError], apply=False)
    def func_2():
        raise ZeroDivisionError()

    assert dummy._future_exceptions
    for future_exception in dummy._future_exceptions:
        assert future_exception.handler == func_1 or func_2

# Generated at 2022-06-14 07:35:21.729750
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint
    assert callable(ExceptionMixin.exception)

    blueprint = Blueprint(__name__)
    _exception = blueprint.exception

    # Check with default arguments and default return value
    handler = object()
    future_exception = _exception(handler)
    assert future_exception is handler

    # Check with exceptional and default return value
    handler = object()
    future_exception = _exception(ZeroDivisionError, handler)
    assert future_exception is handler

# Generated at 2022-06-14 07:35:34.274789
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Handler:
        def __init__(self):
            self.description = None
            self.is_before = None
            self.is_after = None

        def __call__(self, req, resp):
            pass

    class SanicApp:
        def __init__(self):
            pass

        def error_handler(self, desc: Exception) -> Handler:
            handler = Handler()
            handler.description = desc
            return handler

        def register_middleware(self, middleware: Handler, attach_to: str = None):
            middleware.is_before = True

        def register_middleware_after(self, middleware: Handler, attach_to: str = None):
            middleware.is_after = True


# Generated at 2022-06-14 07:35:46.509716
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest.mock as mock
    from sanic.views import View

    blueprint_mock = mock.MagicMock()
    blueprint_mock.name = "test_blueprint_name"
    blueprint_mock.url_prefix = "/test/blueprint/"

    exception_mixin_mocked = ExceptionMixin()

    @exception_mixin_mocked.exception(Exception)
    def my_first_exception_handler(request, exception):
        return None

    assert len(exception_mixin_mocked._future_exceptions) == 1
    assert exception_mixin_mocked._future_exceptions.pop()
    assert isinstance(exception_mixin_mocked._future_exceptions.pop(), FutureException)


# Generated at 2022-06-14 07:35:53.153506
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FakeBlueprint(ExceptionMixin):
        def _apply_exception_handler(self,handler: FutureException):
            print("apply exception handler")
    
    bp = FakeBlueprint()
    @bp.exception(Exception)
    def handler(request,exception):
        print("handle exception")

    assert(len(bp._future_exceptions) == 1)

# Generated at 2022-06-14 07:35:54.675096
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    result = True
    assert result == ExceptionMixin.exception()

# Generated at 2022-06-14 07:36:02.108978
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    obj_test = ExceptionMixin()
    handler = lambda *args : None
    assert (obj_test.exception(TypeError, apply=True)(handler)) == handler
    assert obj_test._future_exceptions == set([FutureException(handler, (TypeError,))])

    class FutureException1:
        def __init__(self, handler, exceptions):
            self.handler = handler
            self.exceptions = exceptions

    future_exception1 = FutureException1(handler, (TypeError,))
    assert obj_test._apply_exception_handler(future_exception1) == NotImplementedError

# Generated at 2022-06-14 07:36:13.721227
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTestClass(ExceptionMixin):
        def __init__(self):
            super().__init__()
        
        def _apply_exception_handler(self, handler):
            return
    
    test_class = ExceptionMixinTestClass()
    assert len(test_class._future_exceptions) == 0
    
    @test_class.exception()
    def test_func_1():
        return

    assert len(test_class._future_exceptions) == 1
    
    @test_class.exception([])
    def test_func_2():
        return

    assert len(test_class._future_exceptions) == 2
    
    @test_class.exception([1, 2, 3])
    def test_func_3():
        return


# Generated at 2022-06-14 07:36:20.089030
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    bp = Blueprint(__name__, url_prefix='/test_ExceptionMixin_exception')
    bp.exception(ValueError)(lambda r, e: None)
    bp.exception(FileNotFoundError)(lambda r, e: None)
    bp.exception(ZeroDivisionError)(lambda r, e: None)
    assert len(bp._future_exceptions) == 3
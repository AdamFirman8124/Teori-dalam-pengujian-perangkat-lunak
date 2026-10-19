

# Generated at 2022-06-14 07:27:14.159740
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
  assert True

# Generated at 2022-06-14 07:27:26.242786
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Test of default behaviour
    """
    Test case to verify the exception method without any parameter.
    """

    @exception()
    def a(request,e):
        pass

    assert a.__name__ == 'a'
    assert a.__doc__  == None

    # Test of exception method with one parameter
    """
    Test case to verify the exception method with one parameter.
    """

    @exception(Exception)
    def a(request,e):
        pass

    assert a.__name__ == 'a'
    assert a.__doc__  == None

    # Test of exception method with multiple parameter
    """
    Test case to verify the exception method with multiple parameter.
    """

    @exception(Exception,[1,2,3])
    def a(request,e):
        pass

    assert a.__

# Generated at 2022-06-14 07:27:31.838146
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Test(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            print(handler)
    t = Test()
    @t.exception(ValueError)
    def process(req, res):
        print(req, res)
        
    def process(req, res):
        print(req, res)
        
test_ExceptionMixin_exception()


# Generated at 2022-06-14 07:27:47.478859
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # given:
    class TestExceptionMixin(ExceptionMixin):
        _future_exceptions = set()
        _future_exceptions_tmp = set()
        def _apply_exception_handler(self, handler: FutureException):
            self._future_exceptions_tmp.add(handler)
    TestExceptionMixin_instance = TestExceptionMixin()
    # when:
    x = TestExceptionMixin_instance.exception(FileNotFoundError, apply=True)(lambda a: a)
    # then:
    assert TestExceptionMixin_instance._future_exceptions_tmp.__len__() == 1

# Generated at 2022-06-14 07:27:55.120936
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class App:
        def add_exception(self, *args):
            return args

    class BluePrint(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.app = App()

        def _apply_exception_handler(self, handler: FutureException):
            return self.app.add_exception(handler.handler, handler.exceptions)

    bp = BluePrint()
    @bp.exception("exception")
    def exception_handler1(request, exception):
        return ''

    assert ('exception_handler1', ('exception',)) == bp._apply_exception_handler(next(iter(bp._future_exceptions)))


# Generated at 2022-06-14 07:28:01.613918
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs) -> None:
            self._future_exceptions: Set[FutureException] = set()

        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_exception_mixin = TestExceptionMixin()
    @test_exception_mixin.exception(Exception, apply=False)
    def handler(self, request, exception):
        pass
    assert(len(test_exception_mixin._future_exceptions) == 1)

# Generated at 2022-06-14 07:28:07.603892
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @sanic.blueprint('test_bp')
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    test_bp = TestExceptionMixin()

    @test_bp.exception(ZeroDivisionError)
    def handler(request, exception):
        return text('internal server error!')

# Generated at 2022-06-14 07:28:10.357508
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    response = ExceptionMixin()
    response.exception(ValueError)
    assert len(response._future_exceptions) == 1



# Generated at 2022-06-14 07:28:16.492824
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self):
            pass

        def _apply_exception_handler(self, handler):
            pass
    exception_mixin = TestExceptionMixin()
    @exception_mixin.exception(apply=True)
    def handler():
        pass
    assert hasattr(handler, '__exception_handler')
    assert isinstance(handler.__exception_handler, FutureException)

# Generated at 2022-06-14 07:28:30.324521
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    try:
        1 / 0
    except Exception as err:
        ExceptionMixin_exception_err = err
    def test_decorator(handler):
        test_func = handler
        return test_func
    def test_handler(request,exception):
        print("in test_handler")
    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler):
            return test_decorator(handler)

    test_ExceptionMixin = TestExceptionMixin()
    test_ExceptionMixin.exception([Exception])

    #test trigger the exception
    try:
        test_ExceptionMixin.test_decorator(test_handler)(request = None,exception = ExceptionMixin_exception_err)
        print("wrong answer")
    except:
        print("correct answer")

# Generated at 2022-06-14 07:28:40.095405
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint

    bp = Blueprint('Test')

    # Code path where apply is true
    list_of_exceptions : List[Exception] = list()
    dict_of_exceptions : Dict[str, Exception] = dict()
    @bp.exception(list_of_exceptions, dict_of_exceptions)
    def exception_handler(request, exception):
        return None

    # Code path where apply is false
    # @bp.exception
    # def exception_handler(request,exception):
    #     return None

# Generated at 2022-06-14 07:28:52.494820
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            assert self._future_exceptions == {handler}, 'The value of _future_exceptions is not initialized as a empty set.'

    import pytest
    from sanic.exceptions import NotFound

    # Case 1: the first argument of decorator function is not a list
    blueprint = Blueprint()

    @blueprint.exception(NotFound)
    def not_found(request, exception):
        pass

    assert blueprint._future_exceptions == {
        FutureException(not_found, (NotFound,))
    }, "The exception handler can't add to the set of _future_exceptions"

    #

# Generated at 2022-06-14 07:28:56.435900
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.blueprints import Blueprint

    @Blueprint.exception(IndexError, IndexError, apply=True)
    async def handler(request, exception):
        print('foo')

    handler(None, None)

# Generated at 2022-06-14 07:29:01.383469
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    blueprint = Blueprint('test', url_prefix='/test')
    @blueprint.exception(Exception, apply=True)
    def handler(request, exception):
        pass
    assert(isinstance(blueprint._future_exceptions[0], FutureException))

# Generated at 2022-06-14 07:29:10.116610
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Blueprint, Sanic


    app = Sanic()
    bp = Blueprint('test_bp')

    @bp.exception(ValueError)
    def handle_value_error(request, exception):
        return text('Internal server error', 500)

    @bp.exception([ValueError, RuntimeError])
    def handle_any_error(request, exception):
        return text('Internal server error', 500)

    app.blueprint(bp)



# Generated at 2022-06-14 07:29:17.322826
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class TestExceptionMixin(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            assert handler in self._future_exceptions
            return handler

    @TestExceptionMixin.exception([Exception])
    def test_handler(*args, **kwargs):
        return args, kwargs

    assert test_handler in TestExceptionMixin._future_exceptions
    TestExceptionMixin._apply_exception_handler(test_handler)


# Generated at 2022-06-14 07:29:24.929939
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint

    app = Sanic()
    blp = Blueprint('test', url_prefix='')

    @blp.exception(ZeroDivisionError)
    def handle_zero_div(request, exception):
        return text('zero division')

    assert len(blp._future_exceptions) == 1

    app.blueprint(blp)

    # Test that the exception handler is registered in the app
    assert len(app.error_handler.keys()) == 1
    assert app.error_handler[ZeroDivisionError] == handle_zero_div

    # Test that the exception handler is passed to any blueprint used
    blp2 = Blueprint('test2', url_prefix='')
    blp3 = Blueprint('test3', url_prefix='')
   

# Generated at 2022-06-14 07:29:28.312915
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    blueprint = Blueprint('main', url_prefix='test', version=2)
    @blueprint.exception([Exception])
    def handler():
        pass
    assert blueprint._future_exceptions

# Generated at 2022-06-14 07:29:33.267395
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Test(ExceptionMixin):
        def _apply_exception_handler(self, _):
            pass
        # _apply_exception_handler = Mock(wraps=_apply_exception_handler)
    t = Test()

    @t.exception(ZeroDivisionError)
    def handler(request, exception):
        pass

    # t._apply_exception_handler.assert_called()
    assert t._future_exceptions
    assert t._future_exceptions.pop()



# Generated at 2022-06-14 07:29:41.646003
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    error_list = []
    class TestExceptionMixin(ExceptionMixin):
        pass

    @TestExceptionMixin.exception(IndexError)
    def raiseIndexError(*args, **kwargs):
        raise IndexError  # noqa

    @TestExceptionMixin.exception(AssertionError)
    def raiseAssertionError(*args, **kwargs):
        raise AssertionError  # noqa

    def request_handler(request):
        raiseIndexError()

    try:
        request_handler(None)
    except:
        error_list.append("IndexError")

    try:
        raiseAssertionError()
    except:
        error_list.append("AssertionError")

    assert len(error_list) == 2
    assert error_list[0] == 'IndexError'
    assert error

# Generated at 2022-06-14 07:29:47.101320
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True

# Generated at 2022-06-14 07:29:55.600832
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from pytest_sanic.utils import TestClient

    class BP_EXCEPTION(ExceptionMixin):
        def __init__(self, app):
            ExceptionMixin.__init__(self)
            self.app = app

    class APP:
        pass

    app = APP()
    blueprint = BP_EXCEPTION(app)
    blueprint.exception(Exception)
    client = TestClient(app, blueprint)

    @blueprint.route('/')
    def handler(request):
        raise Exception('Oh no!')

    with client:
        resp = client.get('/')
        assert resp.status == 500

# Generated at 2022-06-14 07:30:07.440898
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    mixin_object = ExceptionMixin()

    @mixin_object.exception(ValueError)
    def exception_handler(request, exception):
        return exception

    assert len(mixin_object._future_exceptions) == 0

    assert isinstance(exception_handler(None, ValueError()), ValueError)

    assert len(mixin_object._future_exceptions) == 1

    future_exception = list(mixin_object._future_exceptions)[0]
    assert future_exception.handler == exception_handler

    assert len(future_exception.exception_types) == 1
    exception_type = list(future_exception.exception_types)[0]
    assert exception_type == ValueError

# Generated at 2022-06-14 07:30:19.510705
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import exception_handler
    from sanic.models.exceptions import SanicException

    class BlueprintForTestException(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            super(BlueprintForTestException, self).__init__(*args, **kwargs)

        def _apply_exception_handler(self, handler: FutureException):
            exception_handler(handler)

    blueprint = BlueprintForTestException()

    @blueprint.exception([SanicException])
    def handle_all_exception(request, e):
        return text('Internal Server Error', 500)

    blueprint_exception_handler_list = blueprint._future_exceptions
    assert blueprint_exception_handler_list == {
        FutureException(handle_all_exception, (SanicException,))
    }

# Generated at 2022-06-14 07:30:22.168437
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
   pass
# result = ExceptionMixin(FutureException,*args, **kwargs)
# assert result ==

# Generated at 2022-06-14 07:30:34.946882
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.models.futures import FutureException
    from sanic.models.futures import FutureExceptionHandler

    class Error:
        def __init__(self):
            self.raised = False

    e = Error()
    def test_exception_handler(*args, **kwargs):
        e.raised = True

    class TestExceptionMixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            if handler.handler is not test_exception_handler:
                raise
            assert len(handler.exceptions) == 1
            assert handler.exceptions[0] == Exception
            assert handler.kwargs is None
            assert isinstance(handler, FutureException)
            assert handler.handler is test_exception_handler
            handler.handler(1)

    a = TestExceptionMixin

# Generated at 2022-06-14 07:30:39.093473
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class class1(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)

    @class1.exception(Exception)
    def Test(self):
        pass

    Test(class1)

# Generated at 2022-06-14 07:30:44.149554
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    example = ExceptionMixin()

    @example.exception(ValueError)
    def handler(request, exception):
        return exception

    assert len(example._future_exceptions) == 1
    assert example._future_exceptions.pop() == FutureException(handler, (ValueError, ))

# Generated at 2022-06-14 07:30:44.908707
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:30:49.134311
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    test = ExceptionMixin()
    test.exception(ValueError, ValueError)(print)
    test_state = test._future_exceptions
    test_state = len(test_state) is 1
    assert test_state


# Generated at 2022-06-14 07:31:02.509711
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    bp = ExceptionMixin()
    assert bp._future_exceptions == set()
    bp.exception(ValueError, NameError, apply=True)(lambda req: None)
    assert len(bp._future_exceptions) == 1

# Generated at 2022-06-14 07:31:06.169149
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    blueprint = Blueprint("name", url_prefix="prefix")
    blueprint.exception(Exception)(lambda x: x)
    assert blueprint._future_exceptions is not None

# Generated at 2022-06-14 07:31:11.543985
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Test(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            ExceptionMixin.__init__(self, *args, **kwargs)
        def _apply_exception_handler(self, handler: FutureException):
            handler.handler = 'Test'
    test = Test()
    @test.exception
    def handler():
        return 1
    assert test._future_exceptions.pop().handler == 'Test'

# Generated at 2022-06-14 07:31:13.839450
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    ExceptionMixin().exception(ValueError)
    ExceptionMixin().exception(ValueError, KeyError)

# Generated at 2022-06-14 07:31:27.656160
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic, Blueprint
    from sanic.response import json

    app = Blueprint(__name__)

    @app.exception([ZeroDivisionError])
    def zero_division_handler(request, exception):
        return json('Invalid Response', 500)

    @app.route('/')
    def regular_route(request):
        return json({'hello': 'world'})

    @app.route('/divide/<number_one>/<number_two>')
    def divide_route(request, number_one, number_two):
        return json(number_one/number_two)

    @app.route('/type/<number>')
    def type_route(request, number):
        return json(int(number))

    app_full = Sanic(__name__)

    app_full

# Generated at 2022-06-14 07:31:30.875539
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    args = [5, 5]
    apply = True
    exceptions = [5, 5]
    decorator = ExceptionMixin.exception(apply, exceptions)
    result = decorator(None)
    assert result is not None

# Generated at 2022-06-14 07:31:33.896318
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    try:
        normal_value = test_ExceptionMixin_exception
        if normal_value is not None:
            assert True
    except:
        assert False

# Generated at 2022-06-14 07:31:43.778933
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    class ExceptionMixinTestCase(unittest.TestCase):
        def test_ExceptionMixin_exception(self):
            class MyException(Exception):
                pass
            @ExceptionMixin.exception(MyException)
            def exception_handler(request, exception):
                return 'exception_handler() executed'
            self.assertEqual('exception_handler() executed', exception_handler(None, MyException()))

    suite = unittest.TestLoader().loadTestsFromTestCase(ExceptionMixinTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-14 07:31:44.514779
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:31:44.969446
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:32:11.095267
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Blueprint(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            return

    blueprint = Blueprint()

    # Test for the decorator
    @blueprint.exception([Exception])
    def exception_handler(*args, **kwargs):
        return

    assert len(blueprint._future_exceptions) == 1
    future_exception = blueprint._future_exceptions.pop()
    assert future_exception.handler == exception_handler
    assert future_exception.exceptions == (Exception,)

    # Test for the decorator with arguments
    @blueprint.exception([Exception])
    def exception_handler(*args, **kwargs):
        return

    assert len(blueprint._future_exceptions) == 1
    future_exception = blueprint._future_exceptions.pop()

# Generated at 2022-06-14 07:32:21.239207
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.models.futures import FutureException

    blueprint_object = Blueprint('Test', url_prefix='/test/')

    @blueprint_object.exception(ValueError, KeyError)
    def exception_handler(request, exception):
        return request, exception

    try:
        assert(blueprint_object)
    except Exception as e:
        print("Error is: ", e)
    try:
        assert(isinstance(blueprint_object._future_exceptions, set))
    except Exception as e:
        print("Error is: ", e)
    try:
        assert(isinstance(blueprint_object._future_exceptions.pop(), FutureException))
    except Exception as e:
        print("Error is: ", e)

# Generated at 2022-06-14 07:32:30.033223
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    exception_mixin = ExceptionMixin()

    # Test with apply
    @exception_mixin.exception(TypeError)
    # Function to test exception
    def test_with_apply():
        raise TypeError

    # Test with apply = False
    @exception_mixin.exception(TypeError, apply = False)
    # Function to test exception
    def test_without_apply():
        raise TypeError

    # Test with parameter as a list
    @exception_mixin.exception([TypeError])
    # Function to test exception
    def test_list_exception():
        raise TypeError

# Generated at 2022-06-14 07:32:39.519727
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    import unittest
    from unittest.mock import MagicMock, patch

    from sanic.blueprints import Blueprint
    from sanic.views import HTTPMethodView

    class Example(HTTPMethodView, ExceptionMixin):
        def __init__(self, *args, **kwargs):
            ExceptionMixin.__init__(self, *args, **kwargs)
            HTTPMethodView.__init__(self, *args, **kwargs)

        def get(self, request, *args, **kwargs):
            return 'Hello World'

        def post(self, request, *args, **kwargs):
            return self.get(request, *args, **kwargs)


# Generated at 2022-06-14 07:32:40.149413
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    assert True

# Generated at 2022-06-14 07:32:46.280873
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Fake:
        pass

    fake = Fake()
    fake.sanic = Sanic(__name__)
    fake.exception(Exception)(print)
    assert fake._future_exceptions.pop()
    assert fake._future_exceptions == set()


if __name__ == "__main__":
    print(test_ExceptionMixin_exception())

# Generated at 2022-06-14 07:32:52.764526
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Mock_Mixin(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    mixin = Mock_Mixin()

    @mixin.exception(Exception)
    def handler(request, exception):
        return 'test'

    assert handler(None, None) == 'test'
    assert len(mixin._future_exceptions) == 1

# Generated at 2022-06-14 07:33:00.417261
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    """
    ExceptionMixin.exception(apply=True)
    """
    from sanic.blueprints import Blueprint
    from sanic.exceptions import SanicException

    def test_exception_handler(request, exception):
        pass

    blue = Blueprint(__name__)

    @blue.exception(SanicException, apply=True)
    def exception_handler(request, exception):
        return "test"


# Generated at 2022-06-14 07:33:08.670362
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class FuturesTest(ExceptionMixin):
        def _apply_exception_handler(self, handler: FutureException):
            pass

    myFuturesTest = FuturesTest()

    def test_exception(request, arg2):
        return arg2

    myFuturesTest.exception(IndexError)(test_exception)
    assert len(myFuturesTest._future_exceptions) == 1
    assert myFuturesTest._future_exceptions.pop() == FutureException(test_exception, (IndexError))

test_ExceptionMixin_exception()

# Generated at 2022-06-14 07:33:15.832368
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    @ExceptionMixin.exception(KeyError)
    def handler(exception):
        return '{type(exception)}: {exception}'

    try:
        raise KeyError('Value error')
    except KeyError as e:
        assert handler(e) == f'{KeyError}: {e}'


# Integration test for method exception of class ExceptionMixin

# Generated at 2022-06-14 07:33:59.030695
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self):
            ExceptionMixin.__init__(self)
            self._apply_exception_handler = Mock()

        @property
        def future_exceptions(self):
            return self._future_exceptions

    exception_mixin_test = ExceptionMixinTest()
    # test for exception method
    assert len(exception_mixin_test.future_exceptions) == 0
    @exception_mixin_test.exception(NotImplementedError)
    def exception_handler():
        return 'exception handler'
    assert len(exception_mixin_test.future_exceptions) == 1
    exception_mixin_test._apply_exception_handler.assert_called_once()
    assert exception_mixin_test._apply_ex

# Generated at 2022-06-14 07:34:03.057496
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    m = ExceptionMixin()
    test_exception = Exception("Test Exception")
    @m.exception(test_exception)
    def e():
        return "OK"
    assert e() == "OK"
    assert len(m._future_exceptions) == 1



# Generated at 2022-06-14 07:34:13.503610
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class MyException(Exception):
        pass

    class ChildExceptionMixin(ExceptionMixin):
        def __init__(self):
            super().__init__()
            self.test_handler = None

        def _apply_exception_handler(self, handler):
            self.test_handler = handler
    
    # create a ErrorMixin instance
    error_Mixin = ChildExceptionMixin()
    @error_Mixin.exception(MyException)
    def test_handler():
        pass
    
    # check if test_handler added to the future_exceptions 
    assert error_Mixin._future_exceptions
    assert len(error_Mixin._future_exceptions) == 1
    assert error_Mixin.test_handler

# Generated at 2022-06-14 07:34:22.519728
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint

    bp = Blueprint('test', url_prefix='/test')

    # test if exceptions are stored
    assert bp._future_exceptions == set()

    @bp.exception([Exception])
    def h(*args, **kwargs):
        print(args, kwargs)

    # test if exceptions are stored
    assert len(bp._future_exceptions) == 1
    assert isinstance(bp._future_exceptions.pop(), FutureException)

# Generated at 2022-06-14 07:34:29.220418
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    future_exception = FutureException(handler=None, exceptions=None)
    future_exceptions = set()
    future_exceptions.add(future_exception)
    args = ["test"]
    kwargs = {'test': 'test'}
    exception_mixin = ExceptionMixin()
    exception_mixin._future_exceptions = future_exceptions
    assert exception_mixin.exception(args, **kwargs)

# Generated at 2022-06-14 07:34:42.069990
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    # Build a dummy class called DummyExceptionMixin.
    # DummyExceptionMixin is a subclass of ExceptionMixin
    # with an overrideable method _apply_exception_handler.
    class DummyExceptionMixin(ExceptionMixin):  # noqa
        def __init__(self, *args, **kwargs):
            super(DummyExceptionMixin, self).__init__(*args, **kwargs)
            self.applied_exception_handlers = []

        def _apply_exception_handler(self, handler: FutureException):
            # This method will be used to mock the behaviour of
            # _apply_exception_handler
            self.applied_exception_handlers.append(handler)

    # Build a dummy exception handler
    def dummy_exception_handler(): pass

    # Build a dummy class to test

# Generated at 2022-06-14 07:34:49.537200
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Lazy:
        def __init__(self, **attrs):
            self.__dict__.update(attrs)

    # set the keyword argument of decorator.
    # decorator_app = create_app()
    # decorator_app.exception(*exceptions)
    # decorator_app.exception(apply=True)

    # set the keyword arguments of the Lazy class.
    class Lazy:
        def __init__(self, **attrs):
            self.__dict__.update(attrs)


# Generated at 2022-06-14 07:35:01.626010
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    import pytest

    app = Sanic("test_ExceptionMixin_exception")

    @app.exception(Exception)
    async def handle_exception(request: Request, exception):
        return HTTPResponse("Exception:\n" + str(exception),
                            status=500)
    @app.route("/")
    async def handler(request: Request):
        # noinspection PyUnresolvedReferences
        raise Exception("Test Exception")

    request, response = app.test_client.get("/")

    assert response.status == 500
    assert response.text == "Exception:\nTest Exception"


# Generated at 2022-06-14 07:35:15.567798
# Unit test for method exception of class ExceptionMixin

# Generated at 2022-06-14 07:35:21.701184
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():

    class ExceptionMixinTest(ExceptionMixin):
        def __init__(self) -> None:
            super().__init__()

        def _apply_exception_handler(self, handler: FutureException):
            return NotImplemented

    emt = ExceptionMixinTest()
    emt.exception(Exception)(lambda x: x)
    emt.exception([Exception])
    emt.exception(Exception, apply=False)
    emt.exception([Exception], apply=False)

# Generated at 2022-06-14 07:36:39.204407
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class ExceptionMixinMock(ExceptionMixin):
        def __init__(self):
            super(ExceptionMixinMock, self).__init__()

    exception_mixin_mock = ExceptionMixinMock()
    exception_mixin_mock.exception(NotImplementedError)
    exception_mixin_mock.exception([NotImplementedError])
    exception_mixin_mock.exception((NotImplementedError))
    exception_mixin_mock.exception(ZeroDivisionError)
    assert exception_mixin_mock._future_exceptions is not None
    assert len(exception_mixin_mock._future_exceptions) is 2
    exception_mixin_mock.exception(NotImplementedError)

# Generated at 2022-06-14 07:36:52.272211
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.blueprints import Blueprint
    from sanic.response import json

    def test_handler(request, exception):
        handler_request = request
        handler_exception = exception
        return json({'test': True}, status=500)

    exception_name = 'test_exception'

    bp = Blueprint('test_bp', url_prefix='test')
    bp.exception(test_handler)
    bp.exception(
        [exception_name],
        test_handler,
        apply=False,
        param_test_1='test_value_1',
        param_test_2='test_value_2')
    bp.exception([exception_name])

    assert bp.exception_handlers
    assert bp.exception_handlers[None].handler == test_handler


# Generated at 2022-06-14 07:37:04.170625
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    class Bp(ExceptionMixin):
        def __init__(self, *args, **kwargs):
            self._future_exceptions = set()
            super(Bp, self).__init__(*args, **kwargs)

        async def get_exceptions(self):
            exceptions = set()
            for future_exception in self._future_exceptions:
                exceptions.add(future_exception)

            return exceptions

    @Bp.exception(ValueError, apply=False)
    def my_exception_handler(request, err):
        pass

    test_bp = Bp()
    exceptions = test_bp.get_exceptions()
    assert(exceptions.__len__() == 1)
    assert(exceptions.pop().__class__.__name__ == 'FutureException')

# Generated at 2022-06-14 07:37:04.932625
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    pass

# Generated at 2022-06-14 07:37:15.569375
# Unit test for method exception of class ExceptionMixin
def test_ExceptionMixin_exception():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    from sanic.exceptions import SanicException

    blueprint = Blueprint(__name__, url_prefix='test_bp')

    @blueprint.exception(SanicException, apply=False)
    def bp_exception_handler(request, exception):
        return text('Hello!')

    @blueprint.route('test_bp/test_route')
    def bp_test_route(request):
        raise SanicException('Test exception')

    app = Sanic()
    app.blueprint(blueprint)

    request, response = app.test_client.get('/test_bp/test_route')

    assert response.status == 500
    assert response.text == 'Internal Server Error'


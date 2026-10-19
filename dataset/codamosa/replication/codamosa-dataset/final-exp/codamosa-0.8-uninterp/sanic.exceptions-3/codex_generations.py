

# Generated at 2022-06-14 07:11:07.886112
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(999)
    class Bla(SanicException):
        pass
    assert _sanic_exceptions[999] == Bla

# Generated at 2022-06-14 07:11:09.527508
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(404)


# Generated at 2022-06-14 07:11:18.402124
# Unit test for function add_status_code
def test_add_status_code():
    def is_except_code(except_, code):
        return isinstance(except_, SanicException) and except_.status_code == code

    # Test the decorator
    @add_status_code(code=422)
    class TestSanicException(SanicException):
        pass

    assert TestSanicException.status_code == 422
    assert TestSanicException.quiet is False

    # Test the decorator with quiet=True
    @add_status_code(code=422, quiet=True)
    class TestSanicException(SanicException):
        pass

    assert TestSanicException.status_code == 422
    assert TestSanicException.quiet is True

    # Test the decorator with quiet=None

# Generated at 2022-06-14 07:11:24.063115
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(502, quiet=True)
    class InvalidGateway(SanicException):
        pass

    assert InvalidGateway.status_code == 502
    assert InvalidGateway.quiet is True
    assert _sanic_exceptions[502] is InvalidGateway

# Generated at 2022-06-14 07:11:31.265554
# Unit test for function add_status_code
def test_add_status_code():
    # Verify that add_status_code returns a class_decorator
    assert callable(add_status_code)
    # Verify that the class_decorator function returns a function
    assert callable(add_status_code(500))
    assert callable(add_status_code(500, True))
    # Create a new exception class marked up with the status code
    @add_status_code(417)
    class ExpClass1(SanicException):
        pass
    # Verify that the decorated function has the correct status code
    assert ExpClass1.status_code == 417
    # Create a new exception class marked up with the status code and quiet
    @add_status_code(417, True)
    class ExpClass2(SanicException):
        pass
    # Verify that the decorated function has the correct status code and quiet
    assert Exp

# Generated at 2022-06-14 07:11:44.600218
# Unit test for function add_status_code
def test_add_status_code():
    # pylint: disable=missing-docstring
    @add_status_code(200)
    class SanicException200(SanicException):
        pass

    @add_status_code(200, True)
    class SanicException200Quiet(SanicException):
        pass

    @add_status_code(500)
    class SanicException500(SanicException):
        pass

    @add_status_code(500, True)
    class SanicException500Quiet(SanicException):
        pass

    try:
        raise SanicException200()
    except SanicException200 as err:
        assert err.status_code == 200
        assert err.quiet is False
    except Exception as err:
        assert False, err


# Generated at 2022-06-14 07:11:55.794483
# Unit test for function add_status_code
def test_add_status_code():
    class MyException1(SanicException):
        pass

    class MyException2(SanicException):
        pass

    class MyException3(SanicException):
        pass

    class MyException4(SanicException):
        pass

    # check if add_status_code works
    # if it does, the status_code of MyException1, MyException2, MyException3 should
    # be equal to the value they were decorated with.
    add_status_code(401)(MyException1)
    add_status_code(402)(MyException2)
    add_status_code(403, True)(MyException3)
    add_status_code(404, False)(MyException4)
    assert MyException1.status_code == 401
    assert MyException2.status_code == 402
    assert MyException3.status_code == 403

# Generated at 2022-06-14 07:12:09.195987
# Unit test for function add_status_code
def test_add_status_code():
    def assert_add_status_code(code, ctx):
        add_status_code(code)(ctx)
        assert _sanic_exceptions.get(code) == ctx

    class Context:
        pass

    ctx = Context()
    yield assert_add_status_code, 1, ctx
    assert ctx.status_code == 1
    assert ctx.quiet is None

    ctx = Context()
    yield assert_add_status_code, 500, ctx
    assert ctx.status_code == 500
    assert ctx.quiet is None

    ctx = Context()
    add_status_code(404, False)(ctx)
    assert ctx.status_code == 404
    assert ctx.quiet is False

    ctx = Context()
    add_status_code(400, True)(ctx)


# Generated at 2022-06-14 07:12:20.145943
# Unit test for function add_status_code
def test_add_status_code():

    def check_exc_type(code: int, exc: SanicException):
        assert _sanic_exceptions[code] is exc
        assert issubclass(exc, SanicException)

    @add_status_code(405)
    class MethodNotSupported2(SanicException):
        pass

    @add_status_code(503)
    class ServiceUnavailable2(SanicException):
        pass

    check_exc_type(503, ServiceUnavailable2)
    check_exc_type(405, MethodNotSupported2)
    with pytest.raises(ValueError):
        add_status_code(123, "bd")


# Generated at 2022-06-14 07:12:29.246983
# Unit test for function add_status_code
def test_add_status_code():
    """
    This unit test is for the function add_status_code
    """
    class_decorator = add_status_code(200)
    @class_decorator
    class Test:
        """Test class for units test."""
        def __init__(self):
            """ Test initialization"""
            self.foo = "bar"
        @staticmethod
        def get_foo():
            """ Test get_foo method"""
            return "foo"
    test_obj = Test()
    assert test_obj.foo == "bar"
    assert test_obj.status_code == 200
    assert Test.get_foo() == "foo"

# Generated at 2022-06-14 07:12:33.716452
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    add_status_code(404)(TestException)
    assert _sanic_exceptions[404] == TestException

# Generated at 2022-06-14 07:12:39.014803
# Unit test for function add_status_code
def test_add_status_code():
    class ErrorTest(SanicException):
        pass
    expected_status_code = 404
    ErrorTest = add_status_code(expected_status_code)(ErrorTest)
    assert ErrorTest.status_code == expected_status_code

# Generated at 2022-06-14 07:12:42.336390
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class OK(SanicException):
        pass

    assert OK.status_code == 200
    assert OK.quiet is True

    @add_status_code(500, quiet=False)
    class ServerError(SanicException):
        pass

    assert ServerError.status_code == 500
    assert ServerError.quiet is False

# Generated at 2022-06-14 07:12:44.941550
# Unit test for function add_status_code
def test_add_status_code():
    return True


# Generated at 2022-06-14 07:12:46.777086
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class Test(SanicException):
        pass

    return (Test.status_code, Test().status_code, Test.quiet, Test().quiet)

# Generated at 2022-06-14 07:13:00.825242
# Unit test for function add_status_code

# Generated at 2022-06-14 07:13:07.662341
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    # add_status_code(code, quiet=None)
    with pytest.raises(AssertionError):
        add_status_code("code", None)
    assert TestException.status_code == 400

    # add_status_code(code, quiet=None)
    with pytest.raises(AssertionError):
        add_status_code(1, None)
    assert TestException.status_code == 400

# Generated at 2022-06-14 07:13:13.568926
# Unit test for function add_status_code
def test_add_status_code():
    import types

    @add_status_code(123)
    class CustomException(Exception):
        pass

    custom_exception = CustomException("message")
    assert custom_exception.status_code == 123
    assert custom_exception.args[0] == "message"

# Generated at 2022-06-14 07:13:18.252882
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(999)
    class NewException(SanicException):
        pass

    assert 999 in _sanic_exceptions
    assert _sanic_exceptions[999] == NewException



# Generated at 2022-06-14 07:13:24.276955
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(Exception):
        pass

    test_exception = add_status_code(201)(TestException)

    assert test_exception.status_code == 201
    assert test_exception.quiet == False
    assert _sanic_exceptions[201] == TestException

# Generated at 2022-06-14 07:13:39.645241
# Unit test for function add_status_code
def test_add_status_code():
    """
    Unittest for function add_status_code
    """
    from unittest import mock
    from types import AsyncGeneratorType
    from threading import Thread
    from asynctest import TestCase
    import json
    import asyncio
    from sanic import Sanic, response
    from sanic.exceptions import (
        Unauthorized,
        NotFound,
        InvalidUsage,
        ServerError,
    )

    class AddStatusCodeTest(TestCase):
        def setUp(self):
            self.app = Sanic("test_add_status_code")

            @self.app.exception(Unauthorized)
            async def exception_handler_auth(request, exception):
                return response.json(
                    {"exception": type(exception).__name__}, 403, exception
                )

           

# Generated at 2022-06-14 07:13:49.678665
# Unit test for function add_status_code
def test_add_status_code():
    """

    """
    # test add status code
    @add_status_code(1000)
    class TestException(SanicException):
        """

        """
        pass
    ex = TestException("TestException")
    assert ex.status_code == 1000

    # test add status code
    @add_status_code(999)
    class TestException1(SanicException):
        """

        """
        pass
    ex = TestException1("TestException1")
    assert ex.status_code == 999

    # test add status code
    @add_status_code(999, quiet=False)
    class TestException2(SanicException):
        """

        """
        pass
    ex = TestException2("TestException2")
    assert ex.status_code == 999
    assert ex.quiet == False

    # test add

# Generated at 2022-06-14 07:14:03.944730
# Unit test for function add_status_code
def test_add_status_code():
    '''
    Test for adding new code to the SanicException class.
    '''
    import sys
    import unittest
    from types import ModuleType
    from unittest.mock import patch

    _exc_cls = sys.exc_info()[0]
    class MyException(SanicException):
        pass

    with patch.object(SanicException, '__init__') as mock:
        mock.return_value = None
        with patch.object(MyException, '__init__') as mock:
            mock.return_value = None
            this_module = sys.modules[__name__]
            add_status_code(code=400)(MyException)
            add_status_code(code=500)(MyException)
            add_status_code(code=503)(MyException)
            add_status_

# Generated at 2022-06-14 07:14:11.086070
# Unit test for function add_status_code
def test_add_status_code():
    class MockException(SanicException):
        pass

    assert not hasattr(MockException, 'status_code')
    def decorator(cls):
        cls.status_code = 919
        return cls

    decorator = add_status_code(919)
    decorated_MockException = decorator(MockException)
    assert decorated_MockException.status_code == 919
    assert decorated_MockException.status_code == 919

# Generated at 2022-06-14 07:14:24.923303
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class Category(SanicException):
        """ The Coffee Pot Error """
    assert Category.status_code == 418

    try:
        raise Category
    except Category as ex:
        assert ex.status_code == 418

    # with status code
    status_code = 403
    try:
        raise Category(status_code=status_code)
    except Category as ex:
        assert ex.status_code == status_code

    # with message and status code
    message = "the message"
    status_code = 403
    try:
        raise Category(message=message, status_code=status_code)
    except Category as ex:
        assert ex.status_code == status_code
        assert ex.args[0] == message


# Unit tests for function abort

# Generated at 2022-06-14 07:14:36.743707
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass
    class TestException2(SanicException):
        pass
    class TestException3(SanicException):
        pass
    TestException = add_status_code(1)(TestException)
    TestException2 = add_status_code(2, True)(TestException2)
    TestException3 = add_status_code(3, False)(TestException3)
    assert TestException.status_code == 1
    assert TestException.quiet == False
    assert TestException2.status_code == 2
    assert TestException2.quiet == True
    assert TestException3.status_code == 3
    assert TestException3.quiet == False

# Generated at 2022-06-14 07:14:39.611980
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class A(SanicException):
        pass
    assert _sanic_exceptions[200] is A

# Generated at 2022-06-14 07:14:46.495151
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    assert hasattr(MyException, "status_code")

    add_status_code(302)(MyException)

    assert MyException.status_code == 302
    add_status_code(413, True)(MyException)

    assert MyException.status_code == 413

    add_status_code(418)(MyException)

    assert MyException.status_code == 418

    abort(302)
    abort(302, "This is a custom message for redirect exception")

    abort(413)

    try:
        abort(418)
    except SanicException as e:
        assert e.status_code == 418
    except:
        assert False

# Generated at 2022-06-14 07:14:57.499344
# Unit test for function add_status_code
def test_add_status_code():
    # Test by adding 500 status code: Internal Server Error
    add_status_code(500)
    assert _sanic_exceptions[500] == ServerError, "500 is not added to _sanic_exception"

    # Test by adding 404 status code: Not Found
    add_status_code(404)
    assert _sanic_exceptions[404] == NotFound, "404 is not added to _sanic_exception"

    # Test by adding an existing status code
    add_status_code(404)
    assert _sanic_exceptions[404] == NotFound, "404 is added to _sanic_exception again"


# Generated at 2022-06-14 07:15:10.781381
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class MyException(SanicException):
        pass

    assert MyException.status_code == 500
    assert not MyException.quiet

    # if code = 500, quiet = None
    @add_status_code(500, quiet=None)
    class MyException2(SanicException):
        pass
    assert not MyException2.quiet

    # if code = 404, quiet = False
    @add_status_code(404, quiet=False)
    class MyException3(SanicException):
        pass
    assert MyException3.quiet

    # if code = 404, quiet = True
    @add_status_code(404, quiet=True)
    class MyException4(SanicException):
        pass
    assert MyException4.quiet

# Generated at 2022-06-14 07:15:31.237110
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class MyException100(Exception):
        def __init__(self, message):
            self.message = message

    @add_status_code(200)
    class MyException200(Exception):
        def __init__(self, message):
            self.message = message

    @add_status_code(300, quiet=True)
    class MyException300(Exception):
        def __init__(self, message):
            self.message = message

    @add_status_code(400, quiet=False)
    class MyException400(Exception):
        def __init__(self, message):
            self.message = message

    @add_status_code(500, quiet=None)
    class MyException500(Exception):
        def __init__(self, message):
            self.message

# Generated at 2022-06-14 07:15:34.729656
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class MyException(SanicException):
        pass
    my_exception = MyException("message")
    assert my_exception.status_code == 200
    assert _sanic_exceptions[200] == MyException



# Generated at 2022-06-14 07:15:49.160770
# Unit test for function add_status_code
def test_add_status_code():
    foo_exception = add_status_code(418)(SanicException)
    assert foo_exception.status_code == 418
    assert _sanic_exceptions[418] == foo_exception

    foo_exception = add_status_code(418, True)(SanicException)
    assert foo_exception.status_code == 418
    assert foo_exception.quiet is True
    assert _sanic_exceptions[418] == foo_exception

    # quiet=None/False/True with None meaning choose by status
    foo_exception = add_status_code(418, None)(SanicException)
    assert foo_exception.status_code == 418
    assert foo_exception.quiet is True
    assert _sanic_exceptions[418] == foo_exception

# Generated at 2022-06-14 07:15:52.840549
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(202)
    class Foobar(SanicException):
        pass

    assert Foobar.status_code == 202
    assert Foobar.quiet == True

    exception = Foobar("foobar")
    assert exception.status_code == 202
    assert exception.quiet == True


# Generated at 2022-06-14 07:16:07.072269
# Unit test for function add_status_code
def test_add_status_code():

    # Case 1: Invalid status code
    try:
        add_status_code()
    except TypeError as e:
        assert "add_status_code() missing 1 required positional argument: 'code'" in str(e)
    # Case 2: Non-integer status code
    try:
        add_status_code(500.5)
    except TypeError as e:
        assert "add_status_code() argument 'code' should be integer" in str(e)
    # Case 3: Valid status code
    class_decorator = add_status_code(500)
    assert class_decorator(SanicException) == SanicException
    assert _sanic_exceptions[500] == SanicException
    # Case 4: Status code already exists
    add_status_code = add_status_code(500)

# Generated at 2022-06-14 07:16:17.774965
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class DefinedStatus(SanicException):
        """
        **Status**: 403 Forbidden
        """

        pass

    @add_status_code(405)
    class DefinedStatus1(SanicException):
        """
        **Status**: 405 Method Not Allowed
        """

        pass

    assert len(_sanic_exceptions) == 2

    assert _sanic_exceptions[403] == DefinedStatus
    assert _sanic_exceptions[405] == DefinedStatus1

    try:
        # Test the exception is raised correctly.
        raise DefinedStatus("test")
    except DefinedStatus as ex:
        assert ex.status_code == 403
        assert ex.args[0] == "test"


# Generated at 2022-06-14 07:16:22.126345
# Unit test for function add_status_code
def test_add_status_code():
    class mock_Exception(Exception):
        pass

    @add_status_code(405)
    class mock_Exception(Exception):
        pass
    assert issubclass(mock_Exception, SanicException)

# Generated at 2022-06-14 07:16:33.089539
# Unit test for function add_status_code
def test_add_status_code():
    """Unit test for add_status_code"""
    @add_status_code(408, quiet=True)
    class TestClass(SanicException):
        pass
    assert _sanic_exceptions[408] == TestClass
    assert hasattr(TestClass, "status_code")
    assert hasattr(TestClass, "quiet")
    assert TestClass.status_code == 408
    assert TestClass.quiet is True
    assert TestClass.__name__ == "TestClass"
    try:
        raise TestClass()
    except Exception as e:
        assert isinstance(e, SanicException)
        assert isinstance(e, TestClass)
    try:
        raise TestClass(message="test msg")
    except Exception as e:
        assert isinstance(e, SanicException)
        assert isinstance(e, TestClass)

# Generated at 2022-06-14 07:16:42.532184
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class NewException(SanicException):
        pass
    try:
        raise NewException('404 error')
    except NewException as e:
        assert e.status_code == 404
    try:
        raise NewException('404 error', status_code=500)
    except NewException as e:
        assert e.status_code == 500


if __name__ == '__main__':
    test_add_status_code()

# Generated at 2022-06-14 07:16:48.124969
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test function add_status_code.
    """
    code = 200
    quiet = True
    is_success = True

    def class_decorator(cls):
        if cls.status_code != code:
            is_success = False

        if cls.quiet:
            is_success = False

        _sanic_exceptions[code] = cls
        return cls

    class_decorator(class_decorator)
    assert(is_success)

# Generated at 2022-06-14 07:17:10.297558
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(199)
    class Abc(SanicException):
        pass

    assert _sanic_exceptions[199] == Abc
    assert Abc().status_code == 199
    assert Abc.status_code == 199

    @add_status_code(299, quiet=True)
    class Bcd(SanicException):
        pass

    assert Bcd().quiet
    assert Bcd.quiet

# Generated at 2022-06-14 07:17:15.714696
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200, quiet=True)
    class NewException(SanicException):
        pass
    assert issubclass(_sanic_exceptions[200], NewException)
    assert STATUS_CODES[200] == NewException("").args[0]
    assert _sanic_exceptions[200].quiet



# Generated at 2022-06-14 07:17:27.386288
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class BLA(SanicException):
        status_code = 999999
        quiet = None

    assert BLA.status_code == 400
    assert BLA.quiet is False
    assert len(_sanic_exceptions) == 11

    @add_status_code(400, quiet=False)
    class BLA2(SanicException):
        status_code = 999999
        quiet = None

    assert BLA2.status_code == 400
    assert BLA2.quiet is False
    assert len(_sanic_exceptions) == 12

    @add_status_code(400, quiet=True)
    class BLA3(SanicException):
        status_code = 999999
        quiet = None

    assert BLA3.status_code == 400
    assert BLA3.quiet

# Generated at 2022-06-14 07:17:32.056010
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(300)
    class MyException(SanicException):
        pass

    assert MyException.status_code == 300
    assert MyException('err').status_code == 300
    assert MyException().status_code == 300


# Unit tests for the exception classes themselves

# Generated at 2022-06-14 07:17:35.443123
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(400)
    assert 400 in _sanic_exceptions
    assert _sanic_exceptions[400] is SanicException



# Generated at 2022-06-14 07:17:45.998096
# Unit test for function add_status_code
def test_add_status_code():
    class Test(SanicException):
        pass

    add_status_code(418)(Test)
    assert Test.status_code == 418
    assert _sanic_exceptions[418] == Test
    t = Test('hello')
    assert t.status_code == 418
    add_status_code(500)(Test)
    assert Test.status_code == 500
    assert _sanic_exceptions[500] == Test
    t = Test('hello')
    assert t.status_code == 500
    add_status_code(500, quiet=True)(Test)
    assert Test.status_code == 500
    assert _sanic_exceptions[500] == Test
    assert Test.quiet
    t = Test('hello')
    assert t.status_code == 500

# Generated at 2022-06-14 07:17:49.046048
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(302)
    class TestClass(SanicException):
        pass
    assert TestClass.status_code == 302
    assert TestClass.quiet == True

# Generated at 2022-06-14 07:18:00.447543
# Unit test for function add_status_code
def test_add_status_code():
    global NotFound
    assert(NotFound.status_code == 404)
    assert(NotFound.quiet == True)
    new_exception = add_status_code(1001)(SanicException)
    assert(new_exception.status_code == 1001)
    assert(new_exception.quiet == False)
    new_exception = add_status_code(1002, quiet=True)(SanicException)
    assert(new_exception.status_code == 1002)
    assert(new_exception.quiet == True)

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:18:05.235254
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass
    add_status_code(400, MyException)
    _sanic_exceptions[400] = MyException
    assert 400 in _sanic_exceptions
    assert isinstance(abort(400), MyException)


# Generated at 2022-06-14 07:18:11.436567
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test the base add_status_code function
    """
    # Test for adding a status code
    @add_status_code(404)
    class SanicExceptionTest(SanicException):
        pass
    assert _sanic_exceptions[404] == SanicExceptionTest
    assert SanicExceptionTest.status_code == 404

    # Test that the last usage of the decorator overrides the old usage
    @add_status_code(404)
    class SanicExceptionTest2(SanicException):
        pass
    assert _sanic_exceptions[404] == SanicExceptionTest2

    # Test that the quiet argument works
    assert SanicExceptionTest2.quiet is False
    @add_status_code(500, quiet=True)
    class SanicExceptionTest3(SanicException):
        pass
    assert San

# Generated at 2022-06-14 07:18:46.112567
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 400
    # Add the class using the decorator
    @add_status_code(status_code)
    class TestException(SanicException):
        pass

    assert TestException.status_code == status_code
    assert _sanic_exceptions[status_code] == TestException
    raise _sanic_exceptions[status_code]("Invalid Usage")

# Generated at 2022-06-14 07:18:56.505198
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(501)
    class NotImplemented(SanicException):
        pass

    assert isinstance(_sanic_exceptions[501](), NotImplemented)

    @add_status_code(502, quiet=True)
    class NotImplemented(SanicException):
        pass

    assert isinstance(_sanic_exceptions[502](), NotImplemented)

    @add_status_code(503, quiet=False)
    class NotImplemented(SanicException):
        pass

    assert isinstance(_sanic_exceptions[503](), NotImplemented)

# Generated at 2022-06-14 07:19:02.525184
# Unit test for function add_status_code
def test_add_status_code():
    class NewSanicException(SanicException):
        pass

    @add_status_code(404)
    class NewNotFound(NewSanicException):
        """
        **Status**: 404 Not Found
        """

        pass


    try:
        raise NewNotFound('Test')
        assert False
    except Exception as e:
        assert e.status_code == 404

# Generated at 2022-06-14 07:19:09.583047
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        """
        **Status**: 400 Bad Request
        """

    assert 'TestException' in _sanic_exceptions[400].__name__
    assert _sanic_exceptions[400].status_code == 400
    assert _sanic_exceptions[400].quiet == True

    @add_status_code(500)
    class TestException2(SanicException):
        """
        **Status**: 500 Server Error
        """

    assert 'TestException2' in _sanic_exceptions[500].__name__
    assert _sanic_exceptions[500].status_code == 500
    assert _sanic_exceptions[500].quiet == False


# Generated at 2022-06-14 07:19:18.078110
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class InvalidKey(SanicException):
        pass

    @add_status_code(404)
    class KeyNotFound(SanicException):
        pass

    assert _sanic_exceptions[400] == InvalidKey
    assert _sanic_exceptions[404] == KeyNotFound
    assert _sanic_exceptions[405] == MethodNotSupported


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:19:23.105338
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(Exception):
        pass
    # add a new status code to SanicException
    add_status_code(999)(MyException)

    # if MyException is not in SanicException, the get code will return None
    assert _sanic_exceptions.get(999) is MyException

# Generated at 2022-06-14 07:19:27.366195
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(808)
    assert _sanic_exceptions[808].status_code == 808
    add_status_code(809, quiet=True)
    assert _sanic_exceptions[809].quiet == True

# Generated at 2022-06-14 07:19:33.227109
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test add_status_code decorator.
    """

    @add_status_code(200)
    class CustomClass(SanicException):
        pass

    assert _sanic_exceptions[200].__name__ == "CustomClass"

    @add_status_code(201)
    class CustomClass2(SanicException):
        pass

    assert _sanic_exceptions[201].__name__ == "CustomClass2"

# Generated at 2022-06-14 07:19:35.471293
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(234, True)
    class MyException(SanicException):
        pass
    assert MyException.status_code == 234
    assert MyException.quiet is True
    assert _sanic_exceptions[234] is MyException

# Generated at 2022-06-14 07:19:37.367540
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    add_status_code(code=400)(TestException)

    assert _sanic_exceptions[400] == TestException

# Generated at 2022-06-14 07:20:44.765502
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(code=200)
    class Test(SanicException):
        pass

    assert(Test.status_code == 200)
    assert(Test.quiet == True)
    assert(Test(message="test_message").__str__() == "test_message")

    @add_status_code(code=500)
    class Test(SanicException):
        pass

    assert(Test.status_code == 500)
    assert(Test.quiet == False)
    assert(Test(message="test_message").__str__() == "test_message")

# Generated at 2022-06-14 07:20:56.337858
# Unit test for function add_status_code
def test_add_status_code():
    code = 100000
    quiet = True
    assert code not in _sanic_exceptions

    # Unit test for decorator
    @add_status_code(code, quiet)
    class Sanic100000(SanicException):
        pass

    assert code in _sanic_exceptions
    assert str(Sanic100000(message="my_message", status_code=code, quiet=True)) == 'my_message'
    assert Sanic100000(message="my_message", status_code=code, quiet=True).status_code == code
    assert Sanic100000(message="my_message", status_code=code, quiet=True).quiet == True



# Generated at 2022-06-14 07:21:05.625191
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class TestException123(SanicException):
        pass

    @add_status_code(456, quiet=True)
    class TestException456(SanicException):
        pass

    assert issubclass(_sanic_exceptions[123], SanicException)
    assert issubclass(_sanic_exceptions[456], SanicException)

    assert _sanic_exceptions[123].status_code == 123
    assert _sanic_exceptions[456].status_code == 456

    assert _sanic_exceptions[123].quiet
    assert _sanic_exceptions[456].quiet


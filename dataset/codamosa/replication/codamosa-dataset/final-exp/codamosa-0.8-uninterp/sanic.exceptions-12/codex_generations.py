

# Generated at 2022-06-14 07:11:21.720469
# Unit test for function add_status_code
def test_add_status_code():
    class A(SanicException):
        pass

    @add_status_code(423)
    class B(SanicException):
        pass
    assert A.status_code is None
    assert A.quiet is None
    assert B.status_code == 423
    assert B.quiet is True

# Generated at 2022-06-14 07:11:24.776636
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(101)
    class ExtendedProtocol(SanicException):
        pass

    assert ExtendedProtocol.status_code == 101
    assert ExtendedProtocol.quiet == False

# Generated at 2022-06-14 07:11:30.675074
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass
    global _sanic_exceptions
    _sanic_exceptions = {}
    add_status_code(1)(MyException)
    assert _sanic_exceptions[1].__name__ == 'MyException'
    assert _sanic_exceptions[1]().status_code == 1


# Generated at 2022-06-14 07:11:36.581850
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class BadRequest(SanicException):
        pass

    assert _sanic_exceptions[400] == BadRequest
    assert _sanic_exceptions[400] is not SanicException
    assert BadRequest.status_code == 400



# Generated at 2022-06-14 07:11:50.835847
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(status_code=200)
    class Success(SanicException):
        pass
    assert Success.status_code == 200
    assert Success.quiet == False
    @add_status_code(status_code=400, quiet=True)
    class BadRequest(SanicException):
        pass
    assert BadRequest.status_code == 400
    assert BadRequest.quiet == True
    @add_status_code(400, quiet=False)
    class BadRequest1(SanicException):
        pass
    assert BadRequest1.status_code == 400
    assert BadRequest1.quiet == False
    @add_status_code(500, quiet=False)
    class ServerError1(SanicException):
        pass
    assert ServerError1.status_code == 500
    assert ServerError1.quiet == False


# Generated at 2022-06-14 07:11:55.757608
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(566)
    class TestClass:
        pass

    assert TestClass.status_code == 566
    assert TestClass.quiet == True

    @add_status_code(567)
    class TestClass2:
        pass

    assert TestClass2.status_code == 567
    assert TestClass.quiet == True
    assert TestClass2.quiet == None


# Generated at 2022-06-14 07:12:00.752728
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyException(Exception):
        pass

    assert MyException.status_code == 400
    assert issubclass(MyException, SanicException)


# Generated at 2022-06-14 07:12:11.516505
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class CustomException(SanicException):
        pass

    # Since 500 is added to status codes, so this exception should be found
    assert _sanic_exceptions[500] == CustomException

    @add_status_code(501)
    class CustomException2(SanicException):
        pass

    # Since 501 is added to status codes, so this exception should be found
    assert _sanic_exceptions[501] == CustomException2

    # Test the quiet=None feature.
    # If you pass quiet=None, it will use quiet=True if the status_code isn't 500
    # or you don't pass a status_code.
    assert CustomException2(quiet=None).quiet == False
    assert CustomException(quiet=None).quiet == True

# Generated at 2022-06-14 07:12:15.677662
# Unit test for function add_status_code
def test_add_status_code():
    assert(add_status_code(401)(SanicException).status_code == 401)
    assert(_sanic_exceptions[401].__name__ == "SanicException")


# Generated at 2022-06-14 07:12:21.968052
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class MyException(SanicException):
        pass

    assert 123 in _sanic_exceptions
    assert _sanic_exceptions[123].__name__ == "MyException"
    assert _sanic_exceptions[123].status_code == 123

# Generated at 2022-06-14 07:12:28.209384
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(status_code=999, quiet=True)
    class TestException(SanicException):
        pass

    assert(TestException.status_code == 999)
    assert(TestException.quiet == True)

# Generated at 2022-06-14 07:12:31.496832
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class Test(SanicException):
        pass

    assert _sanic_exceptions[123] is Test


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:12:36.816887
# Unit test for function add_status_code
def test_add_status_code():
    # This should work
    @add_status_code(200)
    class A(SanicException):
        pass

    # This should work, too
    @add_status_code(304)
    class B(SanicException):
        pass



# Generated at 2022-06-14 07:12:44.852415
# Unit test for function add_status_code
def test_add_status_code():
    # Assert that the function 'add_status_code' makes a successful addition
    # to the '_sanic_exceptions' dict.
    @add_status_code(444)
    class MyException(SanicException):
        """ 
        **Status**: 444 Connection Closed Without Response 
        """
        pass

    MyException.status_code == 444
    _sanic_exceptions[444] == MyException


# Unit tests for SanicException

# Generated at 2022-06-14 07:12:50.634789
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(999)
    class TestClass(SanicException):
        pass
    test_instance = TestClass
    assert test_instance.status_code == 999
    assert test_instance is _sanic_exceptions[999]
    assert test_instance.quiet == True
    
    
if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:12:56.526224
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test add_status_code function
    """

    class NewException(SanicException):
        pass
    add_status_code(505)(NewException)
    assert 505 in _sanic_exceptions
    assert _sanic_exceptions[505] == NewException



# Generated at 2022-06-14 07:13:02.611874
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(300)
    class _300(SanicException):
        """
        **Status**: 300 Multiple Choices
        """
        pass

    assert 300 == _300.status_code
    assert _300() is not None


if __name__ == "__main__":
    # Unit test for function add_status_code

    pass

# Generated at 2022-06-14 07:13:09.420204
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(404)
    assert add_status_code(400)
    assert add_status_code(405)
    assert add_status_code(500)
    assert add_status_code(503)
    assert add_status_code(408)
    assert add_status_code(413)
    assert add_status_code(416)
    assert add_status_code(417)
    assert add_status_code(403)
    assert add_status_code(401)

# Generated at 2022-06-14 07:13:14.379943
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(4545)
    class SanicTestException(SanicException):
        pass

    assert SanicTestException.status_code == 4545
    assert 4545 in _sanic_exceptions and _sanic_exceptions[4545] == SanicTestException
    assert SanicTestException.__name__ == 'SanicTestException'


# Generated at 2022-06-14 07:13:16.081801
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(418)(SanicException).status_code == 418



# Generated at 2022-06-14 07:13:25.221112
# Unit test for function add_status_code
def test_add_status_code():
    """
    Makes sure that the add_status_code decorator sets the status code as
    expected.
    """

    @add_status_code(400)
    class testException(SanicException):
        pass

    assert testException.status_code == 400
    assert _sanic_exceptions[400].status_code == 400

# Generated at 2022-06-14 07:13:30.941977
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200, quiet=True)
    class MyException(SanicException):
        pass
    assert MyException.status_code == 200
    assert MyException.quiet
    assert _sanic_exceptions.get(200) == MyException


# Generated at 2022-06-14 07:13:36.767317
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class CustomException(SanicException):
        pass

    instance = CustomException("msg")
    assert instance.status_code == 500
    assert instance.message == "msg"
    assert _sanic_exceptions[500] == CustomException

# Generated at 2022-06-14 07:13:49.928371
# Unit test for function add_status_code
def test_add_status_code():
    """
    test_add_status_code
    """
    # Test default status_code
    @add_status_code(404)
    class SanicExceptionTest1(SanicException):
        """
        SanicExceptionTest1
        """
        pass

    result = SanicExceptionTest1("test")
    assert result.status_code == 404

    # Test quiet=True
    @add_status_code(404, quiet=True)
    class SanicExceptionTest2(SanicException):
        """
        SanicExceptionTest2
        """
        pass

    result = SanicExceptionTest2("test")
    assert result.status_code == 404 and result.quiet == True
    # Test quiet=None

# Generated at 2022-06-14 07:13:52.936769
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class MyException(SanicException):
        pass
    assert _sanic_exceptions[201] == MyException

# Generated at 2022-06-14 07:14:00.112255
# Unit test for function add_status_code
def test_add_status_code():
    assert _sanic_exceptions[404] == NotFound
    assert _sanic_exceptions[400] == InvalidUsage
    assert _sanic_exceptions[405] == MethodNotSupported
    assert _sanic_exceptions[500] == ServerError
    assert _sanic_exceptions[503] == ServiceUnavailable
    assert _sanic_exceptions[403] == Forbidden

# Generated at 2022-06-14 07:14:12.105200
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(300)
    class _SanicException300(SanicException):
        pass
    assert _SanicException300.__name__ == '_SanicException300'

    @add_status_code(200)
    class _SanicException200(SanicException):
        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message, status_code=status_code, quiet=quiet)

    assert _SanicException200.__name__ == '_SanicException200'

    assert _SanicException300.status_code == 300
    assert _SanicException300.quiet == True
    assert _SanicException200.status_code == 200
    assert _SanicException200.quiet == None

# Generated at 2022-06-14 07:14:16.062793
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyException(SanicException):
        pass
    assert MyException.status_code == 400
    assert _sanic_exceptions[400].status_code == 400

# Generated at 2022-06-14 07:14:20.582823
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    assert TestException not in _sanic_exceptions.values()
    test_exception = add_status_code(200)(TestException)
    assert test_exception == TestException

# Generated at 2022-06-14 07:14:21.655220
# Unit test for function add_status_code
def test_add_status_code():
    assert abort(200) == "OK"
    assert abort(400) == "Bad Request"
    assert abort(404) == "Not Found"

# Generated at 2022-06-14 07:14:34.571298
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[400] is TestException

    @add_status_code(500, True)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[500] is TestException
    assert _sanic_exceptions[500]().quiet

    @add_status_code(500, False)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[500] is TestException
    assert _sanic_exceptions[500]().quiet is False

    @add_status_code(500)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[500] is TestException

# Generated at 2022-06-14 07:14:45.205081
# Unit test for function add_status_code
def test_add_status_code():
    # Case 1: Decorating an exception
    # Case 1.1: When args are passed
    # Case 1.1.1: When args does not contain status_code
    @add_status_code(500)
    class TestException1(SanicException):
        def __init__(self, a, status_code=None, quiet=None):
            super().__init__(a, status_code, quiet)

    assert TestException1._status_code == 500

    # Case 1.1.1: When args contains status_code but not quiet
    @add_status_code(500)
    class TestException2(SanicException):
        def __init__(self, a, status_code=None, quiet=None):
            super().__init__(a, status_code, quiet)

    assert TestException2._status_code

# Generated at 2022-06-14 07:14:58.630211
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class MyTestException(SanicException):
        pass
    assert MyTestException(message='test').status_code == 201

    # Test for re-add status code with different quiet value
    @add_status_code(201, quiet=True)
    class MyTestException(SanicException):
        pass
    assert MyTestException(message='test').status_code == 201
    assert MyTestException(message='test', quiet=False).quiet == False

    # Test when adding status code without parameters
    @add_status_code(201)
    class MyTestException(SanicException):
        pass
    assert MyTestException(message='test').status_code == 201
    assert MyTestException(message='test').quiet == None

    # Test when adding status code with param quiet = false

# Generated at 2022-06-14 07:15:01.768860
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Hello(SanicException):
        pass

    assert Hello.status_code == 200


# Generated at 2022-06-14 07:15:07.982899
# Unit test for function add_status_code
def test_add_status_code():
    class NoStatusException(SanicException):
        pass

    class HasStatusException(SanicException):
        status_code = 1000

    add_status_code(404)(NoStatusException)
    add_status_code(500)(HasStatusException)
    assert NoStatusException().status_code == 404
    assert HasStatusException().status_code == 500



# Generated at 2022-06-14 07:15:10.390241
# Unit test for function add_status_code
def test_add_status_code():
    new_exception = add_status_code(100)
    assert new_exception(Exception).status_code == 100

# Generated at 2022-06-14 07:15:20.342057
# Unit test for function add_status_code
def test_add_status_code():
    """Unit test for function add_status_code"""
    @add_status_code(403)
    class TestException1(SanicException):
        """TestException1 class to test add_status_code"""
        pass

    @add_status_code(404, quiet=True)
    class TestException2(SanicException):
        """TestException2 class to test add_status_code"""
        pass

    @add_status_code(500, quiet=True)
    class TestException3(SanicException):
        """TestException3 class to test add_status_code"""
        pass

    assert TestException1.status_code == 403
    assert TestException1.quiet is False
    assert TestException2.status_code == 404
    assert TestException2.quiet is True
    assert TestException3.status_code == 500

# Generated at 2022-06-14 07:15:23.919993
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(4)
    class TestException(Exception):
        pass

    assert _sanic_exceptions[4] == TestException


# Generated at 2022-06-14 07:15:35.834664
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        pass

    @add_status_code(500)
    class TestException2(SanicException):
        pass

    class TestException3(SanicException):
        pass

    assert TestException.status_code == 400
    assert TestException2.status_code == 500
    assert TestException3.status_code == 500
    assert TestException3.quiet is True

    assert not hasattr(TestException, "quiet")
    assert hasattr(TestException2, "quiet")
    assert TestException2.quiet is False

    try:
        raise TestException()
    except TestException as te:
        assert te.status_code == 400

    try:
        raise TestException2()
    except TestException2 as te:
        assert te.status_code

# Generated at 2022-06-14 07:15:47.874539
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(402)
    class PaymentRequired(SanicException):
        """
        **Status**: 402 Payment Required
        """

        pass
    assert _sanic_exceptions[402].__name__ == "PaymentRequired"
    assert _sanic_exceptions[402].quiet == False

    @add_status_code(501)
    class NotImplemented(SanicException):
        """
        **Status**: 501 Not Implemented
        """

        pass
    assert _sanic_exceptions[501].__name__ == "NotImplemented"
    assert _sanic_exceptions[501].quiet == True

# Generated at 2022-06-14 07:16:08.924385
# Unit test for function add_status_code
def test_add_status_code():
    def cls(self):
        pass
    cls.status_code = 200
    cls.quiet = True

    test_class = add_status_code(200)(cls)
    assert isinstance(test_class, cls)
    assert test_class.status_code == 200
    assert test_class.quiet is True
    assert _sanic_exceptions[200] is test_class

# Generated at 2022-06-14 07:16:18.484346
# Unit test for function add_status_code
def test_add_status_code():
    class MockException1(SanicException):
        pass

    class MockException2(SanicException):
        pass

    class MockException3(SanicException):
        pass

    add_status_code(404)(MockException1)
    add_status_code(400)(MockException2)
    add_status_code(500)(MockException3)

    assert _sanic_exceptions[404] is MockException1
    assert _sanic_exceptions[400] is MockException2
    assert _sanic_exceptions[500] is MockException3

# Generated at 2022-06-14 07:16:22.370581
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(999)
    class SanicException999(SanicException):
        pass
    assert SanicException999.status_code == 999


# Generated at 2022-06-14 07:16:33.181407
# Unit test for function add_status_code
def test_add_status_code():
    # test with quiet as None and code != 500
    @add_status_code(600, quiet=None)
    class test_exception(SanicException):
        pass
    
    assert test_exception.status_code == 600
    assert test_exception.quiet is True
    assert _sanic_exceptions[600].__name__ == "test_exception"

    # test with quiet as True
    @add_status_code(601, quiet=True)
    class test_exception_2(SanicException):
        pass

    assert test_exception_2.status_code == 601
    assert test_exception_2.quiet is True
    assert _sanic_exceptions[601].__name__ == "test_exception_2"

    # test with quiet as False

# Generated at 2022-06-14 07:16:47.226692
# Unit test for function add_status_code
def test_add_status_code():
    # pylint: disable=
    @add_status_code(404)
    class Hello(SanicException):
        pass

    # pylint: enable=no-member
    assert getattr(Hello, "status_code", None) == 404
    assert getattr(Hello, "quiet", False) is True

    assert _sanic_exceptions[404] == Hello

    # pylint: disable=unused-variable
    @add_status_code(status_code=200, quiet=False)
    class Hi(SanicException):
        pass

    # pylint: enable=unused-variable
    assert getattr(Hi, "status_code", None) == 200
    assert getattr(Hi, "quiet", True) is False

    assert _sanic_exceptions[200] == Hi

# Generated at 2022-06-14 07:16:50.466219
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class Test(SanicException):
        pass

    assert Test.status_code == 400
    assert Test.quiet is None


# Generated at 2022-06-14 07:16:55.200736
# Unit test for function add_status_code
def test_add_status_code():
    AbortException = add_status_code(418)(SanicException)
    assert 418 in _sanic_exceptions
    assert AbortException is _sanic_exceptions[418]

# Generated at 2022-06-14 07:17:01.268494
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(217)
    class SomeException(SanicException):
        pass

    # test by status code
    assert isinstance(SomeException(message="msg"), SanicException)
    assert _sanic_exceptions[217] is SomeException

    # test by class
    assert SomeException(message="msg").status_code == 217



# Generated at 2022-06-14 07:17:05.748518
# Unit test for function add_status_code
def test_add_status_code():  # pylint: disable=unused-variable
    code_list = [200, 400, 404, 500, 503, 408, 413, 416, 417, 403, 401]
    for code in code_list:
        assert _sanic_exceptions[code].status_code == code

# Generated at 2022-06-14 07:17:12.893562
# Unit test for function add_status_code
def test_add_status_code():
    class IntentionalException(Exception):
        status_code = -1
        def __init__(self):
            super().__init__()

    @add_status_code(410)
    class GoneException(Exception):
        def __init__(self):
            super().__init__()

    assert IntentionalException.status_code == -1

    assert GoneException.status_code == 410
    assert GoneException.quiet is True

    assert _sanic_exceptions[410] == GoneException



# Generated at 2022-06-14 07:17:42.591860
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class Nonsense(SanicException):
        """
        **Status**: 418 I'm a Teapot
        """
        pass
    assert Nonsense.status_code == 418
    assert _sanic_exceptions[418] == Nonsense

# Generated at 2022-06-14 07:17:46.726028
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class NotFound(SanicException):
        pass
    _sanic_exceptions[500] = NotFound
    assert _sanic_exceptions[500].status_code is 500

    _sanic_exceptions[500] = ServerError
    assert _sanic_exceptions[500].status_code is 500


# Generated at 2022-06-14 07:18:00.533518
# Unit test for function add_status_code
def test_add_status_code():
    assert _sanic_exceptions.get(404) == NotFound
    assert _sanic_exceptions.get(400) == InvalidUsage
    assert _sanic_exceptions.get(405) == MethodNotSupported
    assert _sanic_exceptions.get(500) == ServerError
    assert _sanic_exceptions.get(503) == ServiceUnavailable
    assert _sanic_exceptions.get(408) == RequestTimeout
    assert _sanic_exceptions.get(413) == PayloadTooLarge
    assert _sanic_exceptions.get(416) == ContentRangeError
    assert _sanic_exceptions.get(417) == HeaderExpectationFailed
    assert _sanic_exceptions.get(403) == Forbidden
    assert _sanic_exceptions.get(401) == Unauthorized

# Unit test

# Generated at 2022-06-14 07:18:08.154252
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class AccessDenied(SanicException):
        pass
    err = AccessDenied(message="Access denied")
    assert err.status_code == 403
    assert err.quiet is True

    @add_status_code(403, quiet=False)
    class AccessDenied(SanicException):
        pass
    err = AccessDenied(message="Access denied")
    assert err.status_code == 403
    assert err.quiet is False

# Generated at 2022-06-14 07:18:12.562377
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(status_code=400, quiet=True)
    class TestException(SanicException):
        pass

    assert TestException(message="Test", status_code=400).quiet == True

# Generated at 2022-06-14 07:18:15.385963
# Unit test for function add_status_code
def test_add_status_code():
    """
    add_status_codeのテスト
    """

    @add_status_code(123)
    class TestSanicException(SanicException):
        pass

    assert _sanic_exceptions[123] == TestSanicException
    assert TestSanicException.status_code == 123
    assert TestSanicException.quiet is True

# Generated at 2022-06-14 07:18:20.913226
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class IAmATeapot(SanicException):
        """
        **Status**: 418 I Am A Teapot
        """

        pass

    assert _sanic_exceptions.get(418) == IAmATeapot

# Generated at 2022-06-14 07:18:26.504938
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        """ Class to test"""
    assert TestException.status_code is None
    add_status_code(406)(TestException) # pylint: disable=no-value-for-parameter
    assert TestException.status_code == 406
    assert TestException.quiet is True

# Generated at 2022-06-14 07:18:31.633348
# Unit test for function add_status_code
def test_add_status_code():
    # the function add_status_code return an add_status_code function
    decorator = add_status_code(100)
    @decorator
    class TestException(SanicException):
        pass
    assert TestException.status_code == 100


# Generated at 2022-06-14 07:18:42.597126
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test add_status_code function
    """
    def test_exception(code):
        class TestException(SanicException):
            pass

        return add_status_code(code)(TestException)

    _test_exc = test_exception(503)
    assert _sanic_exceptions[503] is _test_exc
    assert hasattr(_test_exc, "status_code")
    assert _test_exc.status_code == 503
    assert not hasattr(_test_exc, "quiet")
    assert not hasattr(_test_exc, "headers")

    _test_exc = test_exception(500)
    assert _sanic_exceptions[500] is _test_exc
    assert hasattr(_test_exc, "status_code")
    assert _test_exc.status_code == 500
   

# Generated at 2022-06-14 07:19:48.098949
# Unit test for function add_status_code
def test_add_status_code():
    # When status_code is 500
    @add_status_code(500)
    class My500Exception(SanicException):
        pass

    exception = My500Exception()
    assert exception.status_code == 500
    assert hasattr(exception, 'quiet') == False
    # When status_code is 404
    @add_status_code(404)
    class My404Exception(SanicException):
        pass

    exception = My404Exception()
    assert exception.status_code == 404
    assert exception.quiet == True
    # When status_code is 405
    @add_status_code(405)
    class My405Exception(SanicException):
        pass

    exception = My405Exception()
    assert exception.status_code == 405
    assert exception.quiet == False
    # When status_code is 400

# Generated at 2022-06-14 07:19:54.875021
# Unit test for function add_status_code
def test_add_status_code():
    http_status_code = 418

    @add_status_code(http_status_code)
    class Test(SanicException):
        pass

    assert Test.__name__ == "Test"
    assert Test.status_code == http_status_code
    assert _sanic_exceptions[http_status_code] == Test

# Generated at 2022-06-14 07:19:59.689946
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(666)
    class TestException(SanicException):
        pass
        # status_code = 666

    assert _sanic_exceptions[666] == TestException
    assert TestException().status_code == 666
    assert TestException().quiet == False

    @add_status_code(666, quiet=True)
    class TestException(SanicException):
        pass
        # status_code = 666
        # quiet = True

    assert TestException().quiet == True



# Generated at 2022-06-14 07:20:03.726334
# Unit test for function add_status_code
def test_add_status_code():
    assert not hasattr(NotFound, 'quiet')
    assert not hasattr(ServerError, 'quiet')
    assert hasattr(NotFound, 'status_code')
    assert hasattr(ServerError, 'status_code')
    assert hasattr(NotFound, 'status_code')
    assert ServerError.status_code == 500
    assert NotFound.status_code == 404

# Generated at 2022-06-14 07:20:07.409305
# Unit test for function add_status_code
def test_add_status_code():
    """Calling add_status_code as function should create class decorator"""
    @add_status_code(200)
    class TestSanicException(SanicException):
        pass
    assert issubclass(TestSanicException, SanicException)
    assert TestSanicException().status_code == 200



# Generated at 2022-06-14 07:20:18.879253
# Unit test for function add_status_code
def test_add_status_code():

    if not _sanic_exceptions:
        assert SanicException(message='Custom SanicException',
                              status_code=418)
        assert NotFound(message='NotFound')
        assert InvalidUsage(message='InvalidUsage')
        assert ServerError(message='ServerError')
        assert ServiceUnavailable(message='ServiceUnavailable')
        assert FileNotFound(message='FileNotFound', path='file',
                            relative_url='url')
        assert URLBuildError(message='URLBuildError')
        assert RequestTimeout(message='RequestTimeout')
        assert PayloadTooLarge(message='PayloadTooLarge')
        assert HeaderNotFound(message='HeaderNotFound')
        assert ContentRangeError(message='ContentRangeError',
                                 content_range='contentRange')

# Generated at 2022-06-14 07:20:28.399377
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(301, True)
    class TestException(SanicException):
        pass

    exc = TestException('Test')
    assert exc.status_code == 301
    assert exc.quiet is True

    @add_status_code(304)
    class TestException(SanicException):
        pass

    exc = TestException('Test')
    assert exc.status_code == 304
    assert exc.quiet is False

    @add_status_code(500)
    class TestException(SanicException):
        pass

    exc = TestException('Test')
    assert exc.status_code == 500
    assert exc.quiet is False

# Generated at 2022-06-14 07:20:31.300491
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Test(SanicException):
        pass
    
    assert Test.status_code == 200
    assert Test().status_code == 200
    assert id(Test) == id(_sanic_exceptions[200])

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:20:33.081631
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestingAddStatusCode:
        pass
    assert TestingAddStatusCode.status_code == 200
    assert _sanic_exceptions[200] == TestingAddStatusCode


# Generated at 2022-06-14 07:20:37.084464
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class CustomException(SanicException):
        """
        **Status**: 400 Bad Request
        """

        pass

    assert CustomException.status_code == 400


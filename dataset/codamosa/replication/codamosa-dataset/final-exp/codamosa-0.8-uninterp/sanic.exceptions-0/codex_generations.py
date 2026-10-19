

# Generated at 2022-06-14 07:11:07.735816
# Unit test for function add_status_code
def test_add_status_code():
    try:
        add_status_code(404)(Exception)
    except TypeError:
        assert True
    else:
        assert False



# Generated at 2022-06-14 07:11:17.530889
# Unit test for function add_status_code
def test_add_status_code():
    assert(add_status_code(200, quiet=True).__name__ == add_status_code(200).__name__)
    assert(add_status_code(200, quiet=False).__name__ == add_status_code(200).__name__)
    assert(add_status_code(200, quiet=None).__name__ == add_status_code(200).__name__)
    assert(add_status_code(500, quiet=True).__name__ != add_status_code(500).__name__)
    assert(add_status_code(500, quiet=False).__name__ != add_status_code(500).__name__)
    assert(add_status_code(500, quiet=None).__name__ != add_status_code(500).__name__)

# Generated at 2022-06-14 07:11:26.706641
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class Test(SanicException):
        pass
    assert Test.status_code == 400
    assert isinstance(_sanic_exceptions[400], type(Test))

    @add_status_code(410)
    class Test2(SanicException):
        pass
    assert Test2.status_code == 410
    assert isinstance(_sanic_exceptions[410], type(Test2))



# Generated at 2022-06-14 07:11:30.236639
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestClass(SanicException):
        pass

    assert TestClass.status_code == 400
    assert TestClass.quiet == True

# Generated at 2022-06-14 07:11:44.102659
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestException(SanicException):
        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message)
            self.status_code = status_code
            self.quiet = quiet

    assert issubclass(_sanic_exceptions[404], TestException)
    # Make sure the status_code is correct
    assert _sanic_exceptions[404](message="Test").status_code == 404
    # Make sure the is_x_exception and is_informational functions work
    assert _sanic_exceptions[404](message="Test").is_client_error() and _sanic_exceptions[404](message="Test").is_error()
    assert not _sanic_exceptions[404](message="Test").is_server

# Generated at 2022-06-14 07:11:49.096372
# Unit test for function add_status_code
def test_add_status_code():
    # Test for status code not found
    assert add_status_code(999)
    # Test for status code already existing
    assert add_status_code(404)
    # Test for status code 500
    assert add_status_code(500)

# Generated at 2022-06-14 07:11:52.964275
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400,'quiet')
    class TestClass():
        pass
    
    assert _sanic_exceptions[400] == TestClass
    assert TestClass.status_code == 400
    assert TestClass.quiet == True

# Generated at 2022-06-14 07:11:55.873776
# Unit test for function add_status_code
def test_add_status_code():
    assert '404' in _sanic_exceptions
    assert '400' in _sanic_exceptions

# Generated at 2022-06-14 07:12:00.215321
# Unit test for function add_status_code
def test_add_status_code():
    class CustomException(SanicException):
        pass

    add_status_code(501)(CustomException)
    assert _sanic_exceptions[501] == CustomException

# Generated at 2022-06-14 07:12:08.695866
# Unit test for function add_status_code
def test_add_status_code():
    """
    Check if the correct status_code has been added to the SanicException
    """
    @add_status_code(402)
    class PaymentRequired(SanicException):
        pass

    assert PaymentRequired.status_code == 402


if __name__ == "__main__":
    for status_code, sanic_exception in _sanic_exceptions.items():
        try:
            raise sanic_exception("{} exception".format(status_code))
        except Exception as exception:
            print(exception)

# Generated at 2022-06-14 07:12:17.184929
# Unit test for function add_status_code
def test_add_status_code():
    class HTTPBadRequest(SanicException):
        pass

    add_status_code(400)(HTTPBadRequest)
    assert _sanic_exceptions[400] is HTTPBadRequest

    add_status_code(500, quiet=False)(SanicException)
    assert _sanic_exceptions[500] is SanicException



# Generated at 2022-06-14 07:12:24.836764
# Unit test for function add_status_code
def test_add_status_code():
    # Create a class to show that we can add exception with different status codes
    @add_status_code(200)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 200
    assert TestException.quiet is False

    # Create a class to show that we can add exception with different status codes
    @add_status_code(400, quiet=True)
    class TestException2(SanicException):
        pass

    assert TestException2.status_code == 400
    assert TestException2.quiet is True



# Generated at 2022-06-14 07:12:37.537448
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class A(SanicException):
        pass

    @add_status_code(500, quiet=False)
    class B(SanicException):
        pass

    @add_status_code(500, True)
    class C(SanicException):
        pass

    @add_status_code(500, False)
    class D(SanicException):
        pass

    @add_status_code(500, quiet=False)
    class E(SanicException):
        pass

    assert A.status_code == 500
    assert A.quiet is True
    assert B.status_code == 500
    assert B.quiet is False
    assert C.status_code == 500
    assert C.quiet is True
    assert D.status_code == 500
    assert D.quiet is False


# Generated at 2022-06-14 07:12:42.579807
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class NewResourceCreated(SanicException):
        pass

    assert NewResourceCreated.status_code == 201
    assert NewResourceCreated.quiet == True
    assert _sanic_exceptions[201] == NewResourceCreated


# Generated at 2022-06-14 07:12:55.551335
# Unit test for function add_status_code
def test_add_status_code():
    class A:
        pass

    class B:
        pass

    assert len(_sanic_exceptions) == 8

    add_status_code(555)(A)
    add_status_code(555)(B)

    assert len(_sanic_exceptions) == 9
    assert _sanic_exceptions[555] is B

    add_status_code(556, True)(A)
    add_status_code(556, False)(B)

    assert len(_sanic_exceptions) == 10
    assert _sanic_exceptions[556] is A
    assert _sanic_exceptions[556].quiet is False

    add_status_code(557, True)(A)
    add_status_code(557, False)(B)

    assert len(_sanic_exceptions) == 11
    assert _sanic_exceptions

# Generated at 2022-06-14 07:13:01.988857
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(501)
    class NotImplementedException(Exception):
        pass
    assert NotImplementedException.status_code == 501
    assert NotImplementedException.quiet == True
    assert _sanic_exceptions[501] == NotImplementedException


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:13:08.592121
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(503)
    class ServiceUnavailable(SanicException):
        """
        **Status**: 503 Service Unavailable

        The server is currently unavailable (because it is overloaded or
        down for maintenance). Generally, this is a temporary state.
        """

        pass

    assert len(_sanic_exceptions.keys()) == 7
    assert _sanic_exceptions.get(503) == ServiceUnavailable


# Generated at 2022-06-14 07:13:21.474523
# Unit test for function add_status_code
def test_add_status_code():
    # Create a class with a few attributes
    @add_status_code(321)
    class Foo(SanicException):
        somestr = "foo"
        someint = 4
    # Check that all attributes are transferred
    assert Foo.status_code == 321
    assert Foo.somestr == "foo"
    assert Foo.someint == 4
    # Check in the global sanic exception dictionary
    assert _sanic_exceptions[321] == Foo
    # Test with the quiet parameter
    @add_status_code(123, quiet=True)
    class Bar(SanicException):
        pass
    assert Bar.status_code == 123
    assert Bar.quiet == True
    # Test quiet parameter on an exception with status >=500

# Generated at 2022-06-14 07:13:24.277063
# Unit test for function add_status_code
def test_add_status_code():

    @add_status_code(420)
    class TooHigh(SanicException):
        pass

    assert TooHigh.status_code == 420

# Generated at 2022-06-14 07:13:27.369311
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(300)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 300

# Generated at 2022-06-14 07:13:35.391418
# Unit test for function add_status_code
def test_add_status_code():
    # This function is tested by the return value of function `_sanic_exception_view`
    # which invokes add_status_code
    pass


# Generated at 2022-06-14 07:13:41.191888
# Unit test for function add_status_code
def test_add_status_code():
    # class_decorator not call
    assert _sanic_exceptions.get(200) is None
    # class_decorator called
    @add_status_code(200)
    class Foo(SanicException):
        pass
    assert _sanic_exceptions.get(200) is Foo


# Generated at 2022-06-14 07:13:43.991452
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(400)(SanicException)
    assert _sanic_exceptions[400] == SanicException

# Generated at 2022-06-14 07:13:55.896145
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 500
    assert TestException.quiet is False
    assert _sanic_exceptions[500] == TestException

    @add_status_code(404)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 404
    assert TestException.quiet is True
    assert _sanic_exceptions[404] == TestException

    @add_status_code(400)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 400
    assert TestException.quiet is True
    assert _sanic_exceptions[400] == TestException

# Generated at 2022-06-14 07:14:03.128203
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(203)
    class DummyException(SanicException):
        pass

    assert DummyException.status_code == 203
    assert _sanic_exceptions[203] == DummyException
    assert _sanic_exceptions[404] == NotFound
    assert _sanic_exceptions[500] == ServerError
    assert _sanic_exceptions[503] == ServiceUnavailable

# Generated at 2022-06-14 07:14:15.558681
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class TestException(Exception):
        pass

    assert _sanic_exceptions[100] == TestException
    assert _sanic_exceptions[100]().status_code == 100

    @add_status_code(200)
    class TestException2(Exception):
        pass

    assert _sanic_exceptions[200] == TestException2
    assert _sanic_exceptions[200]().status_code == 200

    @add_status_code(100, quiet=True)
    class TestException3(Exception):
        pass

    assert _sanic_exceptions[100] == TestException3
    assert _sanic_exceptions[100]().status_code == 100
    assert _sanic_exceptions[100]().quiet


# Generated at 2022-06-14 07:14:24.741765
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyException(SanicException):
        def __init__(self):
            super().__init__("Custom Exception message", status_code=400, quiet=True)
    assert isinstance(_sanic_exceptions[400], MyException)
    assert _sanic_exceptions[400].__doc__ == "Custom Exception message"
    assert _sanic_exceptions[400].status_code == 400
    assert _sanic_exceptions[400].quiet



# Generated at 2022-06-14 07:14:39.113750
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(409)
    class MyException(SanicException):
        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message, status_code, quiet)
    assert _sanic_exceptions[409] == MyException
    assert _sanic_exceptions[409].status_code == 409
    assert _sanic_exceptions[409](message="test").status_code == 409
    assert _sanic_exceptions[409].quiet == False

    @add_status_code(409, quiet=True)
    class MyException2(SanicException):
        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message, status_code, quiet)

# Generated at 2022-06-14 07:14:43.932338
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        pass

    try:
        raise TestException()
    except TestException as e:
        assert (e.status_code == 400)
    except Exception as e:
        assert (False)

if __name__ == '__main__':
    test_add_status_code()

# Generated at 2022-06-14 07:14:56.071558
# Unit test for function add_status_code
def test_add_status_code():
    # Add a SanicException subclass and then check if it's in the dict _sanic_exceptions
    @add_status_code(500)
    class MyException(SanicException):
        """Check if add_status_code works."""

    assert issubclass(MyException, SanicException)
    assert MyException.__doc__ == "Check if add_status_code works."
    assert 500 in _sanic_exceptions
    assert _sanic_exceptions[500] == MyException, "The status code should point to MyException"

    # Make a new instance, create a response and compare it to the desired output
    sanic_exception = MyException("Bla")
    response = sanic_exception.create_response(None)
    assert response.status == 500
    assert response.body == b'Bla'

# Generated at 2022-06-14 07:15:14.114083
# Unit test for function add_status_code
def test_add_status_code():
    def test_decorator(status_code):
        @add_status_code(status_code)
        class TestException(SanicException):
            pass
        return TestException
    TestException1 = test_decorator(400)
    TestException2 = test_decorator(500)
    TestException3 = test_decorator(600)
    TestException4 = test_decorator(400, False)
    TestException5 = test_decorator(500, True)
    assert TestException1.status_code == 400
    assert TestException2.status_code == 500
    assert TestException3.status_code == 600
    assert TestException4.status_code == 400
    assert TestException4.quiet is False
    assert TestException5.status_code == 500
    assert TestException5.quiet is True




# Generated at 2022-06-14 07:15:17.828291
# Unit test for function add_status_code
def test_add_status_code():
    class Test(SanicException):
        pass
    assert Test.status_code == 500
    assert Test.quiet is None
    add_status_code(400)(Test)
    assert Test.status_code == 400
    assert Test.quiet is True
    add_status_code(402, quiet=False)(Test)
    assert Test.status_code == 402
    assert Test.quiet is False
    add_status_code(500, quiet=True)(Test)
    assert Test.status_code == 500
    assert Test.quiet is True

# Generated at 2022-06-14 07:15:26.459592
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestNotFound(SanicException):
        """
        **Status**: 404 Not Found
        """
    assert issubclass(_sanic_exceptions[404], SanicException)
    assert _sanic_exceptions[404].status_code == 404
    assert _sanic_exceptions[404].quiet == True

    @add_status_code(500)
    class TestServerError(SanicException):
        """
        **Status**: 500 Internal Server Error
        """
    assert issubclass(_sanic_exceptions[500], SanicException)
    assert _sanic_exceptions[500].status_code == 500
    assert _sanic_exceptions[500].quiet == False

# Generated at 2022-06-14 07:15:30.908782
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class Created(SanicException):
        pass

    assert Created.status_code == 201
    assert _sanic_exceptions[201] == Created
    assert Created("").status_code == 201



# Generated at 2022-06-14 07:15:36.544184
# Unit test for function add_status_code
def test_add_status_code():
    try:
        raise SanicException()
    except SanicException as e:
        assert e.status_code == 500
        assert e.quiet is False
    try:
        raise NotFound()
    except NotFound as e:
        assert e.status_code == 404
        assert e.quiet is True
    try:
        raise MethodNotSupported()
    except MethodNotSupported as e:
        assert e.status_code == 405
        assert e.quiet is True


# Generated at 2022-06-14 07:15:41.210950
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(code=404)
    class Error(SanicException):
        pass

    assert Error.status_code == 404
    assert Error.quiet == True

    @add_status_code(code=500)
    class Error(SanicException):
        pass

    assert Error.status_code == 500
    assert Error.quiet == False

    try:
        @add_status_code(code=777)
        class Error(SanicException):
            pass
    except Exception as e:
        assert isinstance(e, KeyError)

# Generated at 2022-06-14 07:15:45.430487
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(code=200)
    class AddStatusCodeTest:
        pass

    assert _sanic_exceptions.get(200) == AddStatusCodeTest


# Generated at 2022-06-14 07:15:51.666480
# Unit test for function add_status_code
def test_add_status_code():
    code = 500
    quiet = True
    class MySanicException(SanicException):
        pass
    add_status_code(code,quiet)(MySanicException)
    assert MySanicException.status_code == code
    assert MySanicException.quiet == quiet
    assert isinstance(MySanicException(_sanic_exceptions[code].__doc__), MySanicException)

# Generated at 2022-06-14 07:15:54.430237
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class FakeException(SanicException):
        pass

    assert FakeException.status_code == 100

# Generated at 2022-06-14 07:16:07.124796
# Unit test for function add_status_code
def test_add_status_code():
    """
    Ensure functions add_status_code is working as expected.
    """

    @add_status_code(404, quiet=True)
    class MySanicError(SanicException):
        pass

    assert MySanicError.status_code == 404
    assert MySanicError.quiet is True
    assert _sanic_exceptions[404] == MySanicError

    @add_status_code(400)
    class MyOtherSanicError(SanicException):
        pass

    assert MyOtherSanicError.status_code == 400
    assert MyOtherSanicError.quiet is True
    assert _sanic_exceptions[400] == MyOtherSanicError


# Unit tests for class SanicException

# Generated at 2022-06-14 07:16:34.122415
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(199)
    class _199(SanicException):
        pass

    assert _199.status_code == 199
    assert _199.quiet is False

    @add_status_code(299, quiet=False)
    class _299(SanicException):
        pass

    assert _299.status_code == 299
    assert _299.quiet is False

    @add_status_code(399)
    class _399(SanicException):
        pass

    assert _399.status_code == 399
    assert _399.quiet is True



# Generated at 2022-06-14 07:16:44.352739
# Unit test for function add_status_code
def test_add_status_code():
  add_status_code(400)(SanicException)
  assert _sanic_exceptions[400] == SanicException
  assert _sanic_exceptions[400](status_code=400).status_code == 400
  assert _sanic_exceptions[400](status_code=400).quiet
  assert _sanic_exceptions[400](status_code=500).quiet is None
  assert _sanic_exceptions[400](status_code=500, quiet=True).quiet

  assert _sanic_exceptions[401] == Unauthorized

# Generated at 2022-06-14 07:16:51.513771
# Unit test for function add_status_code
def test_add_status_code():
    class Http400(SanicException):
        pass
    add_status_code(400)(Http400)
    assert _sanic_exceptions[400] == Http400
    class Http400(SanicException):
        pass
    add_status_code(400, quiet=True)(Http400)
    assert _sanic_exceptions[400] == Http400
    assert _sanic_exceptions[400].quiet == True

# Generated at 2022-06-14 07:17:02.216288
# Unit test for function add_status_code
def test_add_status_code():
    assert _sanic_exceptions[404] == NotFound
    assert _sanic_exceptions[400] == InvalidUsage
    assert _sanic_exceptions[405] == MethodNotSupported
    assert _sanic_exceptions[500] == ServerError
    assert _sanic_exceptions[408] == RequestTimeout
    assert _sanic_exceptions[413] == PayloadTooLarge
    assert _sanic_exceptions[416] == ContentRangeError
    assert _sanic_exceptions[417] == HeaderExpectationFailed
    assert _sanic_exceptions[503] == ServiceUnavailable

# Generated at 2022-06-14 07:17:07.630242
# Unit test for function add_status_code
def test_add_status_code():

    @add_status_code(200)
    class Example(SanicException):
        pass

    assert Example.status_code == 200
    assert _sanic_exceptions.get(200) == Example


# Generated at 2022-06-14 07:17:08.378655
# Unit test for function add_status_code
def test_add_status_code():
    pass

# Generated at 2022-06-14 07:17:18.756141
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class NotFoundTest(SanicException):
        pass

    @add_status_code(400)
    class InvalidUsageTest(SanicException):
        pass

    @add_status_code(405)
    class MethodNotSupportedTest(SanicException):
        pass

    @add_status_code(500)
    class ServerErrorTest(SanicException):
        pass

    @add_status_code(503)
    class ServiceUnavailableTest(SanicException):
        pass

    @add_status_code(408)
    class RequestTimeoutTest(SanicException):
        pass

    @add_status_code(413)
    class PayloadTooLargeTest(SanicException):
        pass


# Generated at 2022-06-14 07:17:23.949597
# Unit test for function add_status_code
def test_add_status_code():
    # The extra level of nesting is needed for python3.8
    @add_status_code(400, quiet=True)
    class Demo(SanicException):
        pass

    assert Demo.status_code == 400
    assert Demo.quiet is True
    assert _sanic_exceptions[400] == Demo



# Generated at 2022-06-14 07:17:27.642811
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(450)
    class BlockedByWindowsParentalControls(SanicException):
        pass

    assert _sanic_exceptions[450] == BlockedByWindowsParentalControls

# Generated at 2022-06-14 07:17:31.357679
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class TeaPot(SanicException):
        pass
    assert _sanic_exceptions[418].__name__ == "TeaPot"



# Generated at 2022-06-14 07:18:11.568707
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class Test100(SanicException):
        pass

    @add_status_code(100, quiet=True)
    class Test100Quiet(SanicException):
        pass

    @add_status_code(100, quiet=False)
    class Test100Noisy(SanicException):
        pass

    assert Test100.status_code == 100
    assert Test100.quiet is False

    assert Test100Quiet.status_code == 100
    assert Test100Quiet.quiet is True

    assert Test100Noisy.status_code == 100
    assert Test100Noisy.quiet is False

# Generated at 2022-06-14 07:18:14.498034
# Unit test for function add_status_code
def test_add_status_code():
    class TmpSanicException(SanicException):
        pass

    add_status_code(404, quiet=True)(TmpSanicException)

# Generated at 2022-06-14 07:18:25.314610
# Unit test for function add_status_code
def test_add_status_code():
    
    default_status_message = STATUS_CODES[200]
    
    class CustomException(SanicException):
        pass
    
    # Decorate CustomException with status code 200
    add_status_code(200)(CustomException)
    
    # Status code is set
    assert CustomException.status_code == 200
    
    # Default message is returned
    assert CustomException().args[0] == default_status_message
    
    # Custom message can be returned
    message = "Custom Message"
    assert CustomException(message).args[0] == message

# Generated at 2022-06-14 07:18:32.290844
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(308)
    class TestAddStatusCode(SanicException):
        pass
    assert 308 in STATUS_CODES
    assert len(STATUS_CODES) == len(list(STATUS_CODES.keys()))
    assert TestAddStatusCode.status_code == 308
    assert 308 in _sanic_exceptions
    assert TestAddStatusCode is _sanic_exceptions[308]

# Generated at 2022-06-14 07:18:42.057691
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(503, True)
    class ServiceUnavailable(SanicException):
        """
        **Status**: 503 Service Unavailable

        The server is currently unavailable (because it is overloaded or
        down for maintenance). Generally, this is a temporary state.
        """

        pass

    assert _sanic_exceptions[503] == ServiceUnavailable
    assert _sanic_exceptions[503]().status_code == 503
    assert _sanic_exceptions[503]().quiet == True

# Generated at 2022-06-14 07:18:49.094252
# Unit test for function add_status_code
def test_add_status_code():
    def _add_status_code(code, quiet=None):
        def class_decorator(cls):
            cls.status_code = code
            if quiet or quiet is None and code != 500:
                cls.quiet = True
            _sanic_exceptions[code] = cls
            return cls

        return class_decorator

    assert add_status_code is _add_status_code

# Generated at 2022-06-14 07:18:55.059861
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class TestException(SanicException):
        pass
    assert TestException(message="test").status_code == 500

    @add_status_code(504)
    class Test2Exception(SanicException):
        pass
    assert Test2Exception(message="test").status_code == 504



# Generated at 2022-06-14 07:19:06.793145
# Unit test for function add_status_code
def test_add_status_code():

    class TestException(SanicException):
        pass

    @add_status_code(500)
    class Test500Exception(SanicException):
        pass

    assert getattr(Test500Exception, "status_code", None) == 500
    assert Test500Exception.quiet == False

    @add_status_code(503)
    class Test503Exception(SanicException):
        pass

    assert getattr(Test503Exception, "status_code", None) == 503
    assert Test503Exception.quiet == True

    @add_status_code(503, True)
    class Test503ExceptionQuiet(SanicException):
        pass

    assert getattr(Test503ExceptionQuiet, "status_code", None) == 503
    assert Test503ExceptionQuiet.quiet == True


# Generated at 2022-06-14 07:19:20.672036
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class MyException(SanicException):
        pass

    assert MyException.status_code == 200

    @add_status_code(500)
    class MyException2(SanicException):
        pass

    assert MyException2.status_code == 500
    assert MyException2.quiet == False

    @add_status_code(200, quiet=True)
    class MyException3(SanicException):
        pass

    assert MyException3.status_code == 200
    assert MyException3.quiet == True

    @add_status_code(500, quiet=True)
    class MyException4(SanicException):
        pass

    assert MyException4.status_code == 500
    assert MyException4.quiet == False

# Generated at 2022-06-14 07:19:29.672599
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class CustomException(Exception):
        pass
    assert CustomException.status_code == 500
    assert CustomException.quiet is False
    assert _sanic_exceptions[500] == CustomException
    assert issubclass(CustomException, SanicException)

    @add_status_code(502, quiet=True)
    class CustomException2(Exception):
        pass
    assert _sanic_exceptions[502] == CustomException2
    assert _sanic_exceptions[502]().quiet is True


# Generated at 2022-06-14 07:20:48.953008
# Unit test for function add_status_code
def test_add_status_code():
    stop = add_status_code(418)
    assert issubclass(stop, SanicException)


# Generated at 2022-06-14 07:20:54.118314
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418, True)
    class IAmATeapot(SanicException):
        pass
    assert IAmATeapot(message='Dont Panic!').status_code == 418
    assert IAmATeapot(message='Dont Panic!').quiet == True

# Generated at 2022-06-14 07:21:06.156236
# Unit test for function add_status_code
def test_add_status_code():
    class NewException(SanicException):
        pass

    @add_status_code(444)
    class NewException(SanicException):
        pass

    assert NewException.status_code == 444
    assert NewException(message="hello").status_code == 444

    @add_status_code(555, quiet=False)
    class NewException1(SanicException):
        pass

    assert NewException1.status_code == 555
    assert NewException1.quiet is False

    @add_status_code(666)
    class NewException2(SanicException):
        pass

    assert NewException2.status_code == 666
    assert NewException2.quiet is True

    @add_status_code(777, quiet=True)
    class NewException3(SanicException):
        pass

    assert NewException3.status_code
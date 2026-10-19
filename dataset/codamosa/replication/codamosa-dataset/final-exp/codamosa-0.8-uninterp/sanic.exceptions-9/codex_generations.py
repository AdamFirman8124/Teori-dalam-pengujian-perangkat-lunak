

# Generated at 2022-06-14 07:11:20.003994
# Unit test for function add_status_code
def test_add_status_code():
    '''
    It should add a new exception to the _sanic_exceptions dictionary
    '''
    add_status_code(448)(SanicException)
    assert _sanic_exceptions.get(448) == SanicException



# Generated at 2022-06-14 07:11:26.151003
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(999)
    class CustomException(SanicException):
        pass

    custom = CustomException('Custom message')

    assert custom.status_code == 999
    assert custom.quiet == False
    assert custom.message == 'Custom message'
    assert _sanic_exceptions[999] == CustomException

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:11:39.123970
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(1042, quiet=None)
    class TestSanicException(SanicException):
        pass

    assert TestSanicException.status_code == 1042
    assert TestSanicException().status_code == 1042
    assert len(_sanic_exceptions) == 1
    assert _sanic_exceptions[1042] == TestSanicException

    @add_status_code(999, quiet=True)
    class TestSanicException(SanicException):
        pass

    assert TestSanicException.status_code == 999
    assert TestSanicException().status_code == 999
    assert len(_sanic_exceptions) == 2
    assert _sanic_exceptions[999] == TestSanicException



# Generated at 2022-06-14 07:11:45.984816
# Unit test for function add_status_code
def test_add_status_code():
    try:
        class Exception(SanicException):
            """
            **Status**: 401 Unauthorized
            """

            pass

        Exception = add_status_code(401)(Exception)

        assert issubclass(Exception, SanicException)
        assert Exception.status_code == 401
        assert Exception.quiet is True
    except Exception:
        assert False, "Fail to add status code to the class"

# Generated at 2022-06-14 07:11:53.622031
# Unit test for function add_status_code
def test_add_status_code():
    # get the function
    func = add_status_code(418)
    # test if decorator
    assert inspect.isfunction(func)

    # the new class to add
    @func
    class NewClass(SanicException):
        pass

    # check if added to _sanic_exception dict
    assert NewClass.status_code in _sanic_exceptions.keys()


# Generated at 2022-06-14 07:12:07.557632
# Unit test for function add_status_code
def test_add_status_code():
    msg = '404 Unknown Error'
    status_code = 404
    quiet = None

    @add_status_code(status_code)
    class MyException(SanicException):
        pass

    # In the case of 404, quiet should be set as True
    assert _sanic_exceptions[status_code].quiet == True
    exception = _sanic_exceptions[status_code](message=msg)
    assert exception.quiet == True
    assert type(exception) == _sanic_exceptions[status_code]
    assert str(exception) == msg
    assert exception.status_code == status_code

    # In the case of 500, quiet should be set as False
    status_code = 500
    msg = '500 Unknown Error'
    quiet = None


# Generated at 2022-06-14 07:12:09.160963
# Unit test for function add_status_code
def test_add_status_code():
  pass

# Generated at 2022-06-14 07:12:12.031600
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyTest(SanicException):
        pass

    assert _sanic_exceptions[400] is MyTest

# Generated at 2022-06-14 07:12:21.237485
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    assert MyException.status_code is None

    add_status_code(498)(MyException)
    assert MyException.status_code == 498

    add_status_code(499)(MyException)
    assert MyException.status_code == 498

    add_status_code(500)(MyException)
    assert MyException.status_code == 498

    add_status_code(501)(MyException)
    assert MyException.status_code == 501


# Generated at 2022-06-14 07:12:26.241057
# Unit test for function add_status_code
def test_add_status_code():
    new_code = 999
    @add_status_code(new_code)
    class NewStatusCode(SanicException):
        pass

    assert NewStatusCode.status_code == new_code
    assert _sanic_exceptions[new_code] == NewStatusCode

# Generated at 2022-06-14 07:12:34.526610
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(status_code=123)
    class TestException(SanicException):
        pass
    assert STATUS_CODES[123] == "Unknown"
    assert TestException.status_code == 123
    assert TestException(message="Message").status_code == 123

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:12:39.464324
# Unit test for function add_status_code
def test_add_status_code():
    """Check if the status code is added to the _sanic_exceptions dictionary
    when the function is called"""
    add_status_code(2004, quiet=True)
    assert _sanic_exceptions[2004]


# Generated at 2022-06-14 07:12:44.809981
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class test_add_status_code_class(SanicException):
        pass
    assert STATUS_CODES[test_add_status_code_class.status_code]\
        == STATUS_CODES[404]



# Generated at 2022-06-14 07:12:51.132578
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 200

    # Default quiet is None
    @add_status_code(status_code)
    class FakeSanicTest(SanicException):
        pass
    assert FakeSanicTest.status_code == status_code
    assert FakeSanicTest.quiet is None

    # Default quiet is True
    @add_status_code(status_code, quiet=True)
    class FakeSanicTest(SanicException):
        pass
    assert FakeSanicTest.status_code == status_code
    assert FakeSanicTest.quiet is True

    # Default quiet is False
    @add_status_code(status_code, quiet=False)
    class FakeSanicTest(SanicException):
        pass
    assert FakeSanicTest.status_code == status_code
    assert FakeSanicTest.quiet is False




# Generated at 2022-06-14 07:13:04.085104
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(410)
    class Gone(SanicException):
        pass

    assert getattr(Gone, "status_code", None) is 410
    assert _sanic_exceptions[410] is Gone

    @add_status_code(418, quiet=True)
    class Teapot(SanicException):
        pass

    assert getattr(Teapot, "status_code", None) is 418
    assert _sanic_exceptions[418] is Teapot
    assert getattr(Teapot, "quiet", None) is True

    @add_status_code(420)
    class EnhanceYourCalm(SanicException):
        pass

    assert getattr(EnhanceYourCalm, "status_code", None) is 420
    assert _sanic_exceptions[420] is EnhanceYourCalm

# Generated at 2022-06-14 07:13:14.827844
# Unit test for function add_status_code
def test_add_status_code():

    class TestClass(SanicException):
        pass

    assert TestClass.status_code == 500
    assert TestClass.quiet == False
    assert TestClass.status_code not in _sanic_exceptions

    add_status_code(code=404, quiet=True)(TestClass)

    assert TestClass.status_code == 404
    assert TestClass.quiet == True
    assert TestClass.status_code in _sanic_exceptions

    add_status_code(code=500)(TestClass)

    assert TestClass.status_code == 500
    assert TestClass.quiet == False
    assert TestClass.status_code in _sanic_exceptions

# Generated at 2022-06-14 07:13:26.867898
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test add_status_code
    """
    code = 300
    message = "test_add_status_code"
    @add_status_code(code)
    class Test_add_status_code(SanicException):
        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message)

            if status_code is not None:
                self.status_code = status_code

            # quiet=None/False/True with None meaning choose by status
            if quiet or quiet is None and status_code not in (None, 500):
                self.quiet = True

    test = Test_add_status_code(message)
    assert test.status_code == code
    assert test.quiet == False
    assert test.message == message

    code = 300
    message

# Generated at 2022-06-14 07:13:33.950424
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(502)
    class BadGateway(SanicException):
        pass

    assert hasattr(BadGateway, "quiet")
    assert BadGateway.quiet is True
    assert BadGateway.status_code == 502
    assert _sanic_exceptions[502] is BadGateway

    @add_status_code(503)
    class ServiceUnavailable(SanicException):
        pass

    assert not hasattr(ServiceUnavailable, "quiet")
    assert ServiceUnavailable.status_code == 503
    assert _sanic_exceptions[503] is ServiceUnavailable

# Generated at 2022-06-14 07:13:44.640351
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    add_status_code(404, quiet=True)(TestException)
    assert TestException.status_code == 404
    assert TestException.quiet == True
    assert _sanic_exceptions[404] == TestException

    del TestException.status_code
    del TestException.quiet
    assert TestException.status_code is None
    assert TestException.quiet is None

    add_status_code(200)(TestException)
    assert TestException.status_code == 200
    assert TestException.quiet is None
    assert _sanic_exceptions[200] == TestException

# Generated at 2022-06-14 07:13:57.032464
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class Created(SanicException):
        pass
    assert Created.status_code == 201
    assert _sanic_exceptions[201] == Created
    assert Created().status_code == 201
    assert Created(message='Created').status_code == 201

    @add_status_code(202, quiet=True)
    class Accepted(SanicException):
        pass
    assert Accepted.status_code == 202
    assert Accepted.quiet == True
    assert _sanic_exceptions[202] == Accepted
    assert Accepted().status_code == 202
    assert Accepted(message='Accepted').status_code == 202

    @add_status_code(205)
    class ResetContent(SanicException):
        pass
    assert ResetContent.status_code == 205
    assert Reset

# Generated at 2022-06-14 07:14:09.928812
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class IAmATeapot(SanicException):
        """
        **Status**: 418 I Am A Teapot
        """
    assert _sanic_exceptions[418] == IAmATeapot
    assert IAmATeapot().status_code == 418
    assert IAmATeapot("I'm not the droid you're looking for.").status_code == 418
    assert IAmATeapot.__doc__ == "**Status**: 418 I Am A Teapot"



# Generated at 2022-06-14 07:14:11.492731
# Unit test for function add_status_code
def test_add_status_code():
    # test whether we can add new status code to the sanic_exceptions
    # dict
    @add_status_code(411)
    class LengthRequired(SanicException):
        pass
    assert _sanic_exceptions[411].__name__ == "LengthRequired"

# Generated at 2022-06-14 07:14:16.597919
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    add_status_code(418, True)(MyException)

    assert MyException.status_code == 418
    assert isinstance(MyException.quiet, bool)
    assert isinstance(_sanic_exceptions[418], MyException)

# Generated at 2022-06-14 07:14:20.519810
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418, quiet=True)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 418
    assert TestException.quiet == True



# Generated at 2022-06-14 07:14:26.066891
# Unit test for function add_status_code
def test_add_status_code():
    # Code 406 is not a standard HTTP code
    @add_status_code(406)
    class NotAcceptable(SanicException):
        """
        **Status**: 406 Not Acceptable
        """
        pass
    error = NotAcceptable('Error')
    assert error.status_code == 406

# Generated at 2022-06-14 07:14:32.404448
# Unit test for function add_status_code
def test_add_status_code():
    class MySanicException(SanicException):
        pass

    add_status_code(200)(MySanicException)
    assert MySanicException.status_code == 200

    with pytest.raises(Exception):
        class ExceptionOne(SanicException):
            pass

        add_status_code(999)(ExceptionOne)

# Generated at 2022-06-14 07:14:41.432884
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(402)
    class PaymentRequired(SanicException):
        pass
    assert PaymentRequired.status_code == 402
    assert _sanic_exceptions[402].status_code == 402
    assert not PaymentRequired.quiet

    @add_status_code(405, quiet=True)
    class MethodNotSupported(SanicException):
        pass
    assert MethodNotSupported.status_code == 405
    assert MethodNotSupported.quiet
    assert _sanic_exceptions[405].status_code == 405
    assert _sanic_exceptions[405].quiet

# Generated at 2022-06-14 07:14:49.056184
# Unit test for function add_status_code
def test_add_status_code():
    # test with default value quiet=None
    @add_status_code(423)
    class Locked(SanicException):
        pass
    assert Locked().status_code == 423
    assert Locked().quiet == True

    # test with quiet=False
    @add_status_code(423, quiet=False)
    class Locked(SanicException):
        pass
    assert Locked().status_code == 423
    assert Locked().quiet == False


# Generated at 2022-06-14 07:14:56.143162
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(406)
    class NotAcceptable(Exception):
        pass

    assert NotAcceptable.status_code == 406
    assert _sanic_exceptions[406] == NotAcceptable

    @add_status_code(446, quiet=True)
    class Blah(Exception):
        pass

    assert Blah.status_code == 446
    assert Blah.quiet is True
    assert _sanic_exceptions[446] == Blah

# Generated at 2022-06-14 07:15:09.744265
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class InvalidTest(SanicException):
        """
        **Status**: 400 Bad Request
        """
        pass

    @add_status_code(400, quiet=True)
    class InvalidQuietTest(SanicException):
        """
        **Status**: 400 Bad Request
        """
        pass

    @add_status_code(400, quiet=False)
    class InvalidNoisyTest(SanicException):
        """
        **Status**: 400 Bad Request
        """
        pass

    assert issubclass(InvalidTest, InvalidUsage)
    assert issubclass(InvalidQuietTest, InvalidUsage)
    assert issubclass(InvalidNoisyTest, InvalidUsage)

    assert InvalidTest(message="test").status_code == 400
    assert InvalidTest(message="test").quiet == False

# Generated at 2022-06-14 07:15:21.853141
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(401)
    class Unauthorized(SanicException):
        """
        **Status**: 401 Unauthorized
        """

        pass


# Generated at 2022-06-14 07:15:34.745501
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class BadRequest(SanicException):
        """
        **Status**: 400 Bad Request
        """

        pass

    @add_status_code(400, False)
    class BadRequest2(SanicException):
        """
        **Status**: 400 Bad Request
        """

        pass

    @add_status_code(400, True)
    class BadRequest3(SanicException):
        """
        **Status**: 400 Bad Request
        """

        pass

    assert "BadRequest" in dir()
    assert _sanic_exceptions[400] == BadRequest
    assert BadRequest.status_code == 400
    assert BadRequest.quiet == None

    assert "BadRequest2" in dir()
    assert _sanic_exceptions[400] == BadRequest2
    assert BadRequest

# Generated at 2022-06-14 07:15:41.055477
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(105)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 105
    assert TestException.quiet is True
    assert TestException.__name__ == 'TestException'
    assert _sanic_exceptions[105] == TestException

# Generated at 2022-06-14 07:15:46.966913
# Unit test for function add_status_code
def test_add_status_code():
    """
    It has to add a class decorator
    in order to add status code to SanicException
    """
    add_status_code(201)
    assert 201 in _sanic_exceptions
    assert _sanic_exceptions[201].status_code == 201

test_add_status_code()

# Generated at 2022-06-14 07:15:51.593588
# Unit test for function add_status_code
def test_add_status_code():
    """
    >>> add_status_code(999)
    <function add_status_code.<locals>.class_decorator at 0x7f44a1d04ea0>
    """
    pass

if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 07:15:55.352175
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(499)
    class MyException(SanicException):
        pass

    assert MyException.status_code == 499


# Generated at 2022-06-14 07:16:07.396597
# Unit test for function add_status_code
def test_add_status_code():
    # Test usage without existing SanicException
    @add_status_code(403)
    class MyException(SanicException):
        pass
    exc = MyException("test")
    assert exc.status_code == 403
    assert exc.quiet is None

    # Test usage with existing SanicException
    @add_status_code(403)
    class Forbidden(SanicException):
        pass
    exc = Forbidden("test")
    assert exc.status_code == 403
    assert exc.quiet

    @add_status_code(500)
    class InternalServerError(SanicException):
        pass
    exc = InternalServerError("test")
    assert exc.status_code == 500
    assert exc.quiet is False

# Generated at 2022-06-14 07:16:19.280014
# Unit test for function add_status_code
def test_add_status_code():
    """
    Assert status_code and quiet set correctly from decorator.
    """
    @add_status_code(400)
    class SanicException1(SanicException):
        pass
    assert SanicException1.status_code == 400
    assert not SanicException1.quiet

    @add_status_code(400, quiet=True)
    class SanicException2(SanicException):
        pass
    assert SanicException2.status_code == 400
    assert SanicException2.quiet

    @add_status_code(500, quiet=True)
    class SanicException3(SanicException):
        pass
    assert SanicException3.status_code == 500
    assert not SanicException3.quiet



# Generated at 2022-06-14 07:16:31.933385
# Unit test for function add_status_code
def test_add_status_code():
    # Case: Code exists in STATUS_CODES
    code = 403
    class_decorator = add_status_code(code)
    class SanicException403(SanicException):
        pass
    
    cls = class_decorator(SanicException403)
    # _sanic_exceptions should have 1 item with code 403
    assert _sanic_exceptions[code].status_code == 403 
    assert _sanic_exceptions[code].quiet == None

    # Case: Code does not exist in STATUS_CODES
    code = 999
    class_decorator = add_status_code(code)
    class SanicException999(SanicException):
        pass
    
    cls = class_decorator(SanicException999)
    # _sanic_exceptions should have 1 item

# Generated at 2022-06-14 07:16:36.281746
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(Exception):
        pass

    add_status_code(400)(MyException)

    assert _sanic_exceptions[400] == MyException
    assert MyException.status_code == 400


# Generated at 2022-06-14 07:17:04.950567
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test add_status_code function
    :return None:
    """
    assert _sanic_exceptions[404] == NotFound
    assert _sanic_exceptions[400] == InvalidUsage
    assert _sanic_exceptions[405] == MethodNotSupported
    assert _sanic_exceptions[500] == ServerError
    assert _sanic_exceptions[503] == ServiceUnavailable
    assert _sanic_exceptions[408] == RequestTimeout
    assert _sanic_exceptions[413] == PayloadTooLarge
    assert _sanic_exceptions[416] == ContentRangeError
    assert _sanic_exceptions[417] == HeaderExpectationFailed
    assert _sanic_exceptions[403] == Forbidden
    assert _sanic_exceptions[401] == Unauthorized

# Generated at 2022-06-14 07:17:08.176611
# Unit test for function add_status_code
def test_add_status_code():
    try:
        @add_status_code(300)
        class DummyException(Exception):
            pass
    except Exception:
        return False
    return True


# Generated at 2022-06-14 07:17:11.977830
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(701)
    class MyException(SanicException):
        pass
    error = MyException('Something happened')
    expected = '701 Something happened'
    assert str(error) == expected


# Generated at 2022-06-14 07:17:21.718570
# Unit test for function add_status_code
def test_add_status_code():
    # Define function
    def add_status_code(code, quiet=None):
        def class_decorator(cls):
            cls.status_code = code
            if quiet or quiet is None and code != 500:
                cls.quiet = True
            _sanic_exceptions[code] = cls
            return cls
        return class_decorator
    # Test
    assert _sanic_exceptions[404] == add_status_code(404)


# Generated at 2022-06-14 07:17:24.931827
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(999)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 999
    assert _sanic_exceptions[999] == TestException

# Generated at 2022-06-14 07:17:29.018425
# Unit test for function add_status_code
def test_add_status_code():
    code = 500
    cls = "class_decorator"
    ans = add_status_code(code, quiet=None)
    assert ans(cls).status_code == 500
    assert _sanic_exceptions[code] == cls

# Generated at 2022-06-14 07:17:35.425947
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(666)
    class CustomException(SanicException):
        pass

    instance = CustomException("CustomException")
    assert instance.status_code == 666
    assert instance.quiet is True

    instance2 = CustomException("CustomException", quiet=True)
    assert instance2.quiet is True

    instance3 = CustomException("CustomException", quiet=False)
    assert instance3.quiet is False

# Generated at 2022-06-14 07:17:40.261764
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(999)
    assert add_status_code(999, True)
    assert add_status_code(999, False)
    assert add_status_code(999, None)


# Generated at 2022-06-14 07:17:47.419493
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestException(SanicException):
        pass
    correct_status_code = 404
    assert TestException.status_code == correct_status_code
    assert TestException.quiet is None
    assert TestException() in _sanic_exceptions
    assert _sanic_exceptions[404].name == TestException.__name__


# Generated at 2022-06-14 07:18:00.536110
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(401)
    class MyException(SanicException):
        pass
    assert MyException()

    @add_status_code(402)
    class MyException(SanicException):
        pass
    assert MyException()

    @add_status_code(403)
    class MyException(SanicException):
        pass
    assert MyException()

    # Test with quiet=True
    @add_status_code(401, quiet=True)
    class MyException(SanicException):
        pass
    assert MyException()

    @add_status_code(402, quiet=True)
    class MyException(SanicException):
        pass
    assert MyException()

    @add_status_code(403, quiet=True)
    class MyException(SanicException):
        pass
    assert MyException()

# Generated at 2022-06-14 07:18:32.908601
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code == add_status_code


# Generated at 2022-06-14 07:18:46.112741
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class Test100(SanicException):
        pass

    @add_status_code(102)
    class Test102(SanicException):
        pass
        
    @add_status_code(200)
    class Test200(SanicException):
        pass

    @add_status_code(201)
    class Test201(SanicException):
        pass
    
    assert _sanic_exceptions.get(100) == Test100
    assert _sanic_exceptions.get(102) == Test102
    assert _sanic_exceptions.get(200) == Test200
    assert _sanic_exceptions.get(201) == Test201

# Generated at 2022-06-14 07:18:51.104929
# Unit test for function add_status_code
def test_add_status_code():
    '''add_status_code should add the given code to SanicException'''
    @add_status_code(400)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 400



# Generated at 2022-06-14 07:18:55.324162
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class TestStatus123(SanicException):
        pass

    assert TestStatus123.status_code == 123


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:18:58.259291
# Unit test for function add_status_code
def test_add_status_code():
    # If a new SanicException is added to this file, please modify this
    # method
    assert (len(_sanic_exceptions.keys()) == 10)

# Generated at 2022-06-14 07:19:06.300561
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test add_status_code function.
    """
    @add_status_code(400, quiet=True)
    class NewException(SanicException):
        pass
    assert NewException.quiet == True
    assert NewException.status_code == 400
    assert _sanic_exceptions[400] == NewException

    @add_status_code(403)
    class NewException(SanicException):
        pass
    assert NewException.status_code == 403
    assert _sanic_exceptions[403] == NewException

# Generated at 2022-06-14 07:19:12.661603
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(code=429)
    class RateLimitExceeded(SanicException): pass

    assert RateLimitExceeded.status_code == 429
    assert 429 in _sanic_exceptions
    assert _sanic_exceptions[429] == RateLimitExceeded

# Generated at 2022-06-14 07:19:18.142117
# Unit test for function add_status_code
def test_add_status_code():
    class TestClass(SanicException):
        pass
    test_class = add_status_code(404)(TestClass)
    assert test_class.status_code == 404
    assert _sanic_exceptions[404] is test_class
    assert test_class.quiet == True


# Generated at 2022-06-14 07:19:20.031326
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(200)


# Generated at 2022-06-14 07:19:32.295625
# Unit test for function add_status_code
def test_add_status_code():
    def add_status_code_error(code, quiet=None):
        return code

    try:
        @add_status_code(200, quiet=1)
        class TestStatusCode(SanicException):
            pass

        @add_status_code(400)
        class TestQuiet(SanicException):
            pass

        assert TestStatusCode(message="", status_code=200).status_code == 200
        assert TestStatusCode(message="").quiet

        assert TestQuiet(message="", status_code=400).status_code == 400
        assert not TestQuiet(message="").quiet
    except TypeError:
        add_status_code = add_status_code_error


# Generated at 2022-06-14 07:20:49.470076
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[403] == TestException
    assert issubclass(TestException, SanicException)

    @add_status_code(301, quiet=False)
    class TestException2(SanicException):
        pass
    assert not getattr(TestException2, "quiet")

    @add_status_code(501, quiet=True)
    class TrueException(SanicException):
        pass
    assert getattr(TrueException, "quiet")

    @add_status_code(501, quiet=False)
    class FalseException(SanicException):
        pass
    assert not getattr(FalseException, "quiet")


# Generated at 2022-06-14 07:20:54.062123
# Unit test for function add_status_code
def test_add_status_code():
    from sanic.exceptions import add_status_code

    @add_status_code(200)
    class TestException(Exception):
        pass

    assert TestException.status_code == 200
    assert "TestException" in _sanic_exceptions[200]

# Generated at 2022-06-14 07:20:59.030160
# Unit test for function add_status_code
def test_add_status_code():
    assert NotFound.status_code == 404
    assert NotFound().status_code == 404
    assert NotFound(quiet=True).quiet
    assert NotFound(quiet=False).quiet == False
    assert NotFound().quiet == True


# Generated at 2022-06-14 07:21:06.980382
# Unit test for function add_status_code
def test_add_status_code():
    # Test if code is added to _sanic_exceptions
    def test_code(code, quiet_resp):
        global _sanic_exceptions
        _sanic_exceptions = {}
        @add_status_code(code, quiet=None)
        class TestClass(SanicException):
            pass
        assert _sanic_exceptions[code] == TestClass
        assert TestClass.status_code == code
        assert TestClass.quiet == quiet_resp

    # Test for both quiet=False and quiet=None
    test_code(200, False)
    test_code(404, True)
    test_code(500, False)

# Generated at 2022-06-14 07:21:07.843869
# Unit test for function add_status_code
def test_add_status_code():
    pass

# Generated at 2022-06-14 07:21:18.214217
# Unit test for function add_status_code
def test_add_status_code():
    # Test 1
    @add_status_code(404)
    class NotFound(SanicException):
        pass

    assert NotFound.__dict__["status_code"] == 404
    assert NotFound.__dict__["quiet"] == True

    # Test 2
    @add_status_code(500)
    class InternalServerError(SanicException):
        pass

    assert InternalServerError.__dict__["status_code"] == 500
    assert InternalServerError.__dict__["quiet"] == False

    # Test 3
    @add_status_code(500, True)
    class InternalServerError(SanicException):
        pass

    assert InternalServerError.__dict__["status_code"] == 500
    assert InternalServerError.__dict__["quiet"] == True

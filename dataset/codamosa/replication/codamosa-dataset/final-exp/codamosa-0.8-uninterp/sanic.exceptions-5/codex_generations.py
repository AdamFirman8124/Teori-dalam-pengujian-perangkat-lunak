

# Generated at 2022-06-14 07:11:17.283746
# Unit test for function add_status_code
def test_add_status_code():
    def _assert_status_and_quiet(e, status_code, quiet):
        assert e.status_code == status_code
        assert e.quiet == quiet

    @add_status_code(1)
    class CE1(SanicException):
        pass

    _assert_status_and_quiet(CE1(), 1, True)

    @add_status_code(2, quiet=False)
    class CE2(SanicException):
        pass

    _assert_status_and_quiet(CE2(), 2, False)

    @add_status_code(3, quiet=None)
    class CE3(SanicException):
        pass

    _assert_status_and_quiet(CE3(), 3, False)


# Generated at 2022-06-14 07:11:22.741668
# Unit test for function add_status_code
def test_add_status_code():
    class_not_found = 404
    class_bad_request = 400
    class_internal_server_error = 500
    assert NotFound.status_code == class_not_found
    assert InvalidUsage.status_code == class_bad_request
    assert ServerError.status_code == class_internal_server_error

# Generated at 2022-06-14 07:11:25.045207
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class SanicException400(SanicException):
        pass
    assert _sanic_exceptions[200] == SanicException400

# Generated at 2022-06-14 07:11:27.742089
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    def new_exception(message):
        pass
    assert new_exception.status_code == 200


# Generated at 2022-06-14 07:11:41.552904
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyCustomException(SanicException):
        pass

    try:
        raise NotFound
    except SanicException as e:
        assert e.status_code == 404
        assert e.quiet == True

    try:
        raise MyCustomException("Customized Exception")
    except SanicException as e:
        assert e.status_code == 400
        assert e.quiet == True

    # status_code can be overwritten
    try:
        raise MyCustomException("Customized Exception", status_code=401)
    except SanicException as e:
        assert e.status_code == 401
        assert e.quiet == None


# Generated at 2022-06-14 07:11:46.691262
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class ExampleException(SanicException):
        pass
    
    expected_result = ExampleException(message="Test Message")

    assert(expected_result.status_code == 400)


# Generated at 2022-06-14 07:11:49.693720
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(401)
    class NewException(SanicException):
        pass
    
    assert _sanic_exceptions[401].status_code == 401

# Generated at 2022-06-14 07:11:55.508598
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", scheme="Bearer", realm="Restricted Area")
    except Unauthorized as exc:
        assert exc.status_code == 401
        assert exc.headers == {'WWW-Authenticate': 'Bearer realm="Restricted Area"'}

# Unit tests for class SanicException

# Generated at 2022-06-14 07:11:58.628287
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestException(SanicException):
        pass

    assert(TestException.status_code == 200)



# Generated at 2022-06-14 07:12:01.476834
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(500)(SanicException) == SanicException

# Generated at 2022-06-14 07:12:08.484688
# Unit test for function add_status_code
def test_add_status_code():
    try:
        add_status_code(500)(Exception)
    except Exception as e:
        assert type(e) != Exception
        assert type(e) == TypeError

    assert add_status_code(500, quiet=True)(Exception).status_code == 500
    assert add_status_code(500, quiet=True)(Exception).quiet == True

# Generated at 2022-06-14 07:12:13.339303
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(402)
    class PaymentRequired(SanicException):
        """
        **Status**: 402 Payment Required
        """
        pass

    assert '402' in _sanic_exceptions



# Generated at 2022-06-14 07:12:15.703283
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class FakeException(SanicException):
        pass
    assert _sanic_exceptions[400] == FakeException
    assert _sanic_exceptions[404] == NotFound

# Generated at 2022-06-14 07:12:19.636024
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(507)
    class InsufficientStorage(SanicException):
        pass

    assert _sanic_exceptions[507] == InsufficientStorage


# Generated at 2022-06-14 07:12:24.425373
# Unit test for function add_status_code
def test_add_status_code():
    with pytest.raises(Exception):
        add_status_code(401)

    @add_status_code(401)
    class SomeException(Exception):
        pass

    with pytest.raises(SomeException):
        raise SomeException("some message")



# Generated at 2022-06-14 07:12:37.174245
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class Status100Class(SanicException):
        pass
    assert _sanic_exceptions[100] == Status100Class
    assert _sanic_exceptions[100]().status_code == 100
    assert _sanic_exceptions[100]().quiet == False

    @add_status_code(200)
    class Status200Class(SanicException):
        pass
    assert _sanic_exceptions[200] == Status200Class
    assert _sanic_exceptions[200]().status_code == 200
    assert _sanic_exceptions[200]().quiet == True

    @add_status_code(300)
    class Status300Class(SanicException):
        pass
    assert _sanic_exceptions[300] == Status300Class
    assert _sanic_exceptions

# Generated at 2022-06-14 07:12:47.756072
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    class MyException2(SanicException):
        status_code = 505

    class MyException3(SanicException):
        status_code = 601
        quiet = False

    _sanic_exceptions.clear()

    assert MyException.status_code is None
    assert MyException2.status_code == 505
    assert MyException3.status_code == 601

    add_status_code(501)(MyException)
    add_status_code(506)(MyException2)
    add_status_code(602)(MyException3)

    assert MyException.status_code == 501
    assert MyException2.status_code == 506
    assert MyException3.status_code == 602

# Generated at 2022-06-14 07:12:53.234199
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(999)
    class A(SanicException):
        pass
    assert A.status_code == 999
    assert A.quiet is False
    assert A().status_code == 999
    assert 999 in _sanic_exceptions


# Generated at 2022-06-14 07:13:02.353718
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class NewExc(SanicException):
        pass

    assert NewExc.status_code == 400
    assert NewExc.quiet == True
    assert isinstance(NewExc(''), SanicException)
    assert isinstance(NewExc(''), NewExc)
    assert isinstance(_sanic_exceptions[400], type)
    assert issubclass(_sanic_exceptions[400], SanicException)
    assert issubclass(_sanic_exceptions[400], NewExc)


# Generated at 2022-06-14 07:13:09.054807
# Unit test for function add_status_code
def test_add_status_code():
    """
    check that we get normal status code, 500 is not quiet
    """
    assert 404 == _sanic_exceptions.get(404).status_code
    assert _sanic_exceptions.get(404).quiet == True
    assert _sanic_exceptions.get(500).quiet == False
    assert 500 == _sanic_exceptions.get(500).status_code
    assert _sanic_exceptions.get(500).quiet == False


# Generated at 2022-06-14 07:13:25.765676
# Unit test for function add_status_code
def test_add_status_code():
    class TestException1(SanicException):
        pass

    class TestException2(SanicException):
        pass

    assert _sanic_exceptions[404] == NotFound
    assert _sanic_exceptions[500] == ServerError
    assert _sanic_exceptions[503] == ServiceUnavailable
    assert _sanic_exceptions[404].status_code == 404
    assert _sanic_exceptions[400].status_code == 400
    assert _sanic_exceptions[405].status_code == 405
    assert _sanic_exceptions[500].status_code == 500
    assert _sanic_exceptions[503].status_code == 503
    assert _sanic_exceptions[408].status_code == 408
    assert _sanic_exceptions[413].status_code == 413
    assert _sanic_

# Generated at 2022-06-14 07:13:31.419485
# Unit test for function add_status_code
def test_add_status_code(): 
    # Testing inifinite loop
    result=add_status_code(200)(NotFound)
    assert result == 200
    assert result != 300
    # Testing normal case
    result=add_status_code(400)(NotFound)
    assert result == 400
    assert result != 500

# Generated at 2022-06-14 07:13:36.955664
# Unit test for function add_status_code
def test_add_status_code():
    """Test the function add_status_code."""
    @add_status_code(408)
    class Timeout(SanicException):
        """
        **Status**: 408 Request Timeout
        """

        pass

    assert _sanic_exceptions.get(408) == Timeout

# Generated at 2022-06-14 07:13:42.454254
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class foo(SanicException):
        pass
    assert foo.status_code == 400
    assert foo.name == "foo"
    assert foo() is not None


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:13:44.876703
# Unit test for function add_status_code
def test_add_status_code():
    # Test code, if code has been registered, then raise error
    with pytest.raises(ValueError) as e:
        @add_status_code(404)
        class Err404(SanicException):
            pass
    # Test class has a status

# Generated at 2022-06-14 07:13:49.538877
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    add_status_code(500, quiet=True)(MyException)
    assert _sanic_exceptions[500].status_code == 500
    assert issubclass(_sanic_exceptions[500], SanicException)

# Generated at 2022-06-14 07:14:00.224884
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class TestClass(SanicException):
        pass
    assert TestClass().status_code == 201
    assert TestClass.status_code == 201
    assert _sanic_exceptions[201] is TestClass

    @add_status_code(202)
    class TestClassQuiet(SanicException):
        pass
    assert TestClassQuiet().status_code == 202
    assert TestClassQuiet().quiet == True

    @add_status_code(203, quiet=True)
    class TestClassQuietParam(SanicException):
        pass
    assert TestClassQuietParam().status_code == 203
    assert TestClassQuietParam().quiet == True

    @add_status_code(204, quiet=False)
    class TestClassNotQuietParam(SanicException):
        pass

# Generated at 2022-06-14 07:14:06.948819
# Unit test for function add_status_code
def test_add_status_code():
    class test1(SanicException):
        def __init__(self, message, status_code, quiet):
            super().__init__(message, status_code, quiet)

    class test2(test1):
        def __init__(self, message, status_code, quiet):
            super().__init__(message, status_code, quiet)

    test1 = add_status_code(503, quiet=None)(test1)
    assert test1._sanic_exceptions[503] is test1
    test2 = add_status_code(503, quiet=True)(test2)
    assert test2._sanic_exceptions[503] is test2

# Generated at 2022-06-14 07:14:18.413472
# Unit test for function add_status_code
def test_add_status_code():
    # Test for status code 500
    test_exception = add_status_code(500)(SanicException)
    assert test_exception.status_code == 500
    assert test_exception.quiet == False

    # Test for status code 200
    test_exception = add_status_code(200)(SanicException)
    assert test_exception.status_code == 200
    assert test_exception.quiet == True

    # Test for status code 400 with quiet = False
    test_exception = add_status_code(400, quiet = False)(SanicException)
    assert test_exception.status_code == 400
    assert test_exception.quiet == False


# Generated at 2022-06-14 07:14:21.795768
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class Created(SanicException):
        pass

    assert Created.status_code == 201
    assert Created.quiet == True


# Generated at 2022-06-14 07:14:31.283757
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class Forbidden_test(SanicException):
        pass
    assert Forbidden_test.status_code == 403

# Generated at 2022-06-14 07:14:43.620461
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[400] == TestException
    assert _sanic_exceptions[400]().status_code == 400

    # raise error if status_code is an int
    with pytest.raises(AttributeError):
        @add_status_code(400)
        class ErrorTestException:
            pass

    # raise error if status_code is an int
    with pytest.raises(AttributeError):
        @add_status_code(400, quiet=False)
        class ErrorTestException(SanicException):
            pass

    # raise error if status_code is not in STATUS_CODES

# Generated at 2022-06-14 07:14:48.106089
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(500)
    assert _sanic_exceptions[500].__name__ == 'ServerError'
    add_status_code(503)
    assert _sanic_exceptions[503].__name__ == 'ServiceUnavailable'

# Generated at 2022-06-14 07:14:48.796955
# Unit test for function add_status_code
def test_add_status_code():
    pass

# Generated at 2022-06-14 07:15:01.008317
# Unit test for function add_status_code
def test_add_status_code():

    @add_status_code(code=200)
    class Exception1(SanicException):
        pass

    assert Exception1.status_code == 200
    assert Exception1.quiet is False

    @add_status_code(code=200, quiet=True)
    class Exception2(SanicException):
        pass

    assert Exception2.status_code == 200
    assert Exception2.quiet is True

    @add_status_code(code=200, quiet=False)
    class Exception3(SanicException):
        pass

    assert Exception3.status_code == 200
    assert Exception3.quiet is False

    @add_status_code(code=500, quiet=None)
    class Exception4(SanicException):
        pass

    assert Exception4.status_code == 500
    assert Exception4.quiet is False


# Generated at 2022-06-14 07:15:05.491502
# Unit test for function add_status_code
def test_add_status_code():
    class Code401(SanicException):
        pass
    add_status_code(401)(Code401)
    assert Code401.status_code == 401
    assert _sanic_exceptions.get(401) == Code401
    assert Code401.quiet

# Generated at 2022-06-14 07:15:09.552210
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(250)
    class A(Exception):
        pass

    @add_status_code(250)
    class B(Exception):
        pass

    class C(Exception):
        pass
    add_status_code(250)(C)

    assert A.status_code == 250
    assert B.status_code == 250
    assert C.status_code == 250


# Generated at 2022-06-14 07:15:19.956441
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test add_status_code
    This is a quick ``sanic`` test for ``add_status_code``.
    """
    # Create a set of tests
    test_set = [
        # Check ``add_status_code`
        ("add_status_code", lambda: add_status_code(201) == add_status_code(200)),
        # Check ``add_status_code`
        ("Check add_status_code", lambda: add_status_code(404) == add_status_code(200)),
    ]
    # Run the tests
    results = (test[1]() for test in test_set)
    passed = sum(1 for res in results if res)
    total = len(test_set)
    print(f"{passed}/{total} passed")
################################################################################
#

# Generated at 2022-06-14 07:15:23.478937
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418, quiet=True)
    class Test(SanicException):
        pass

    assert Test(message="Test").message == "Test"



# Generated at 2022-06-14 07:15:33.432022
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(502)
    class A(Exception):
        pass
    assert issubclass(A, SanicException)
    assert A.status_code == 502
    assert A().status_code == 502

    @add_status_code(403, quiet=True)
    class B(SanicException):
        pass
    assert B.status_code == 403
    assert B().status_code == 403
    assert B().quiet == True

    @add_status_code(200)
    class C(SanicException):
        pass
    assert C().quiet == False

# Generated at 2022-06-14 07:15:56.587381
# Unit test for function add_status_code
def test_add_status_code():
    status_code=42
    class NewException(SanicException):
        pass

    @add_status_code(status_code)
    class NewException2(SanicException):
        pass

    @add_status_code(status_code, quiet=True)
    class NewException3(SanicException):
        pass

    assert status_code in _sanic_exceptions
    exception = _sanic_exceptions[status_code]
    assert exception == NewException2
    assert exception().status_code == status_code
    assert not exception().quiet
    exception = _sanic_exceptions[status_code]
    assert exception == NewException3
    assert exception().status_code == status_code
    assert exception().quiet

# Generated at 2022-06-14 07:15:59.686474
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(605)
    class CustomException(SanicException):
        pass
    assert _sanic_exceptions[605] == CustomException

# Generated at 2022-06-14 07:16:13.394065
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class NewException(Exception):
        pass

    # Raises ServerError exception
    try:
        abort(500, "test")
    except ServerError as ex:
        assert ex.status_code == 500
        assert str(ex) == "test"

    # Raises NewException exception
    try:
        abort(500, "test 2")
    except NewException as ex:
        assert ex.status_code == 500
        assert ex.message == "test 2"

    # Raises SanicException exception
    try:
        abort(503, "test 3")
    except SanicException as ex:
        assert ex.status_code == 503
        assert ex.message == "test 3"

    # Raises SanicException exception

# Generated at 2022-06-14 07:16:25.085599
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 402
    message = "402 Test Test"
    quiet = True
    test_exception = add_status_code(status_code, quiet)(SanicException)
    try:
        raise test_exception("402 Test Test")
    except Exception as e:
        assert e.status_code == status_code
        assert str(e) == message
        assert e.quiet == quiet
    # make sure it doesn't add the same code twice
    add_status_code(status_code)(SanicException)
    try:
        raise test_exception("402 Test Test")
    except Exception as e:
        assert e.status_code == status_code
        assert str(e) == message
        assert e.quiet == quiet

# Generated at 2022-06-14 07:16:27.318874
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(500)(SanicException)

# Generated at 2022-06-14 07:16:35.944106
# Unit test for function add_status_code
def test_add_status_code():
    assert isinstance(NotFound(), SanicException)
    assert isinstance(InvalidUsage(), SanicException)
    assert isinstance(ServerError(), SanicException)
    assert isinstance(ServiceUnavailable(), SanicException)
    assert isinstance(PayloadTooLarge(), SanicException)
    assert isinstance(ContentRangeError(), SanicException)
    assert isinstance(HeaderExpectationFailed(), SanicException)
    assert isinstance(Forbidden(), SanicException)
    assert isinstance(InvalidRangeType(), ContentRangeError)
    assert isinstance(Unauthorized(), SanicException)

# Generated at 2022-06-14 07:16:49.052426
# Unit test for function add_status_code
def test_add_status_code():
    original_exception = _sanic_exceptions.copy()

    @add_status_code(510, False)
    class NotExtended(SanicException):
        pass

    assert _sanic_exceptions[510] is NotExtended
    assert _sanic_exceptions[510].__name__ == 'NotExtended'
    assert _sanic_exceptions[510].quiet is False

    @add_status_code(511, True)
    class NetworkAuthenticationRequired(SanicException):
        pass

    assert _sanic_exceptions[511] is NetworkAuthenticationRequired
    assert _sanic_exceptions[511].__name__ == 'NetworkAuthenticationRequired'
    assert _sanic_exceptions[511].quiet is True

    # Should not have changed
    assert _sanic_exceptions[500] is ServerError



# Generated at 2022-06-14 07:16:58.740930
# Unit test for function add_status_code
def test_add_status_code():
    def check_status_code(cls):
        assert cls.status_code is not None
        assert _sanic_exceptions[cls.status_code] == cls

    @add_status_code(999)
    class TempException(SanicException):
        pass

    check_status_code(TempException)
    del _sanic_exceptions[999]

    @add_status_code(993)
    class TempException(SanicException):
        pass
    check_status_code(TempException)

    del _sanic_exceptions[993]

    @add_status_code(993, quiet=True)
    class TempException(SanicException):
        pass
    check_status_code(TempException)
    assert TempException.quiet is True

    del _sanic_exceptions[993]

   

# Generated at 2022-06-14 07:17:09.306685
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class FooBar(SanicException):
        pass

    assert _sanic_exceptions[200] == FooBar
    exception = FooBar("Something went wrong")
    assert exception.status_code == 200

    @add_status_code(201, quiet=True)
    class BarBaz(SanicException):
        pass

    assert _sanic_exceptions[201] == BarBaz
    exception = BarBaz("Something went wrong")
    assert exception.status_code == 201
    assert exception.quiet == True


# Generated at 2022-06-14 07:17:12.052767
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(408)
    class RequestTimeOut(SanicException):
        pass

    assert RequestTimeOut(message="timeout").status_code == 408

# Generated at 2022-06-14 07:17:41.690725
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(409)
    class Conflict(SanicException):
        pass
    try:
        raise Conflict()
    except Conflict as e:
        assert e.status_code == 409
        assert '409' in str(e)


# Generated at 2022-06-14 07:17:48.499805
# Unit test for function add_status_code
def test_add_status_code():
    class SanicException(Exception):
        pass

    new_status_code = 201

    add_status_code(new_status_code)(SanicException)
    assert _sanic_exceptions.get(new_status_code) == SanicException
    assert _sanic_exceptions[new_status_code].status_code == new_status_code

# Generated at 2022-06-14 07:17:53.401826
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class TestException(SanicException):
        pass
    assert _sanic_exceptions[201] == TestException
    assert TestException.status_code == 201
    assert TestException.quiet

# Generated at 2022-06-14 07:17:58.122800
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class TestException(Exception):
        pass

    exception = TestException("Test exception")
    assert exception.status_code == 123
    assert _sanic_exceptions[123] == TestException



# Generated at 2022-06-14 07:18:08.383763
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class OkCreated(SanicException):
        pass

    assert 201 in _sanic_exceptions
    assert _sanic_exceptions[201].__name__ == 'OkCreated'

    @add_status_code(202)
    class OkAccepted(SanicException):
        pass

    assert 202 in _sanic_exceptions
    assert _sanic_exceptions[202].__name__ == 'OkAccepted'

    @add_status_code(204)
    class OkNoContent(SanicException):
        pass

    assert 204 in _sanic_exceptions
    assert _sanic_exceptions[204].__name__ == 'OkNoContent'

    @add_status_code(400)
    class BadRequest(SanicException):
        pass

    assert 400 in _san

# Generated at 2022-06-14 07:18:12.562877
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(401)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 401
    assert TestException.quiet is None


# Generated at 2022-06-14 07:18:17.494106
# Unit test for function add_status_code
def test_add_status_code():
    # Existing Status Code
    assert _sanic_exceptions.get(404) == NotFound
    # Non-Existing Status Code
    assert _sanic_exceptions.get(505) is None
    # Valid Status Code
    assert _sanic_exceptions.get(400) == InvalidUsage


# Generated at 2022-06-14 07:18:25.527768
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400, quiet=True)
    class _Error(SanicException):
        pass
    assert _Error.status_code == 400
    assert _Error.quiet == True
    assert _Error('Test').status_code == 400
    assert _Error('Test').quiet == True
    assert str(_Error('Test')) == 'Test'
    assert _sanic_exceptions[400] == _Error



# Generated at 2022-06-14 07:18:35.391054
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200, quiet=True)
    class TestEx(SanicException):
        pass

    assert 200 in _sanic_exceptions
    assert _sanic_exceptions[200] == TestEx
    assert TestEx.status_code == 200
    assert TestEx.quiet

    @add_status_code(201, quiet=False)
    class TestEx(SanicException):
        pass

    assert 201 in _sanic_exceptions
    assert _sanic_exceptions[201] == TestEx
    assert TestEx.status_code == 201
    assert not TestEx.quiet

    @add_status_code(202)
    class TestEx(SanicException):
        pass

    assert 202 in _sanic_exceptions
    assert _sanic_exceptions[202] == TestEx
    assert TestEx

# Generated at 2022-06-14 07:18:39.084764
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(410)
    class BagelException(SanicException):
        pass
    _sanic_exceptions[410] = BagelException

# Generated at 2022-06-14 07:19:39.448907
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message, status_code, quiet)
        pass

    add_status_code(404)(MyException)
    assert(MyException.status_code == 404)

    try:
        raise MyException("Test")
    except MyException as e:
        assert(e.status_code == 404)


# Generated at 2022-06-14 07:19:41.985798
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Ok(SanicException):
        pass



# Generated at 2022-06-14 07:19:46.682402
# Unit test for function add_status_code
def test_add_status_code():
    """ Checks whether the add_status_code decorator
    properly sets the status_code of the class
    """
    @add_status_code(404)
    class MyTestException(SanicException):
        pass

    assert MyTestException.status_code == 404


# Generated at 2022-06-14 07:19:49.937140
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(444)
    class CustomException(SanicException):
        pass

    assert _sanic_exceptions[444] == CustomException

# Generated at 2022-06-14 07:20:00.807436
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(284)
    class Example(SanicException):
        pass
    
    assert 284 in _sanic_exceptions
    assert _sanic_exceptions[284] == Example
    assert Example().status_code == 284

    @add_status_code(500)
    class Example2(SanicException):
        pass

    assert 500 in _sanic_exceptions
    assert _sanic_exceptions[500] == Example2
    assert Example2().quiet == False
    assert Example2().status_code == 500

    @add_status_code(500, True)
    class Example3(SanicException):
        pass

    assert 500 in _sanic_exceptions
    assert _sanic_exceptions[500] == Example3
    assert Example3().quiet == True
    assert Example3().status_code

# Generated at 2022-06-14 07:20:09.019106
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(599)
    class Test(SanicException):
        pass

    @add_status_code(599, True)
    class TestQuiet(SanicException):
        pass

    assert Test('').status_code == 599
    assert TestQuiet('').status_code == 599
    assert TestQuiet('').quiet == True

    assert _sanic_exceptions[599] == Test
    assert _sanic_exceptions[599] == TestQuiet


# Generated at 2022-06-14 07:20:21.034420
# Unit test for function add_status_code
def test_add_status_code():
    class TestClass:
        pass

    # Test code with quiet = True
    code = 100
    cls = add_status_code(code, True)(TestClass)
    assert cls.status_code == code
    assert cls.quiet

    # Test code with quiet = False
    code = 200
    cls = add_status_code(code, False)(TestClass)
    assert cls.status_code == code
    assert not cls.quiet

    # Test code = None without quiet = None
    code = 300
    cls = add_status_code(code)(TestClass)
    assert cls.status_code == code
    assert not cls.quiet

    # Test code with quiet = None
    code = 500
    cls = add_status_code(code, None)(TestClass)
    assert cls.status

# Generated at 2022-06-14 07:20:29.650779
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class CustomException(SanicException):
        pass

    assert hasattr(CustomException, 'status_code')
    assert hasattr(CustomException, 'quiet')
    assert getattr(CustomException, 'status_code') == 200
    assert getattr(CustomException, 'quiet') == True

    @add_status_code(200, quiet=False)
    class CustomException(SanicException):
        pass

    assert hasattr(CustomException, 'status_code')
    assert hasattr(CustomException, 'quiet')
    assert getattr(CustomException, 'status_code') == 200
    assert getattr(CustomException, 'quiet') == False

# Generated at 2022-06-14 07:20:34.957932
# Unit test for function add_status_code
def test_add_status_code():
    class NewException(SanicException):
        pass
    add_status_code(444, quiet=True)
    assert _sanic_exceptions[444] == NewException
    assert not hasattr(_sanic_exceptions[444], 'quiet')



# Generated at 2022-06-14 07:20:41.611576
# Unit test for function add_status_code
def test_add_status_code():
    
    # Test decorator
    @add_status_code(200)
    class Cls:
        pass

    assert Cls.status_code == 200
    assert Cls.quiet is False

    @add_status_code(200, True)
    class Cls:
        pass

    assert Cls.status_code == 200
    assert Cls.quiet is True


test_add_status_code()
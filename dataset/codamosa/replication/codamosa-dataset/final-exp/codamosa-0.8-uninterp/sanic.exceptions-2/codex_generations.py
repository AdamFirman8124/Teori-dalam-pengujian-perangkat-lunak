

# Generated at 2022-06-14 07:11:11.527139
# Unit test for function add_status_code
def test_add_status_code():
    assert 500 in _sanic_exceptions
    assert 408 in _sanic_exceptions
    assert 400 in _sanic_exceptions
    assert 403 in _sanic_exceptions
    assert 405 in _sanic_exceptions
    assert 413 in _sanic_exceptions
    assert 416 in _sanic_exceptions
    assert 417 in _sanic_exceptions
    assert 503 in _sanic_exceptions



# Generated at 2022-06-14 07:11:24.859257
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as e:
        assert(isinstance(e, Unauthorized))
        assert(e.status_code == 401)
        assert(e.headers["WWW-Authenticate"] == "Basic realm=\"Restricted Area\"")
    try:
        raise Unauthorized("Auth required.", scheme="Digest", realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    except Unauthorized as e:
        assert(isinstance(e, Unauthorized))
        assert(e.status_code == 401)

# Generated at 2022-06-14 07:11:27.461990
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class B(SanicException):
        pass

    assert _sanic_exceptions[201] == B

# Generated at 2022-06-14 07:11:41.422438
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized('Unauthorized')
    except Unauthorized as e:
        assert e.message == 'Unauthorized'
        assert e.status_code == 401
        assert e.scheme == 'Basic'
        assert e.headers == {
            'WWW-Authenticate': 'Basic realm="Restricted Area"'
        }
    try:
        raise Unauthorized('Unauthorized', scheme='Digest', realm='Restricted Area')
    except Unauthorized as e:
        assert e.message == 'Unauthorized'
        assert e.status_code == 401
        assert e.scheme == 'Digest'
        assert e.headers == {
            'WWW-Authenticate': 'Digest realm="Restricted Area"'
        }

if __name__ == "__main__":
    test_U

# Generated at 2022-06-14 07:11:54.300202
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # Test with no scheme.
    try:
        raise Unauthorized("Auth required.")
    except Unauthorized as err:
        assert err.message == "Auth required."
        assert err.headers is None

    # Test with scheme equals to Basic.
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Area")
    except Unauthorized as err:
        assert err.message == "Auth required."
        assert err.headers == {"WWW-Authenticate": 'Basic realm="Area"'}

    # Test with scheme equals to Digest.

# Generated at 2022-06-14 07:12:00.989854
# Unit test for function add_status_code
def test_add_status_code():
    # For function add_status_code, if status_code is not already present
    # in _sanic_exceptions, then add it
    if 404 not in _sanic_exceptions:
        error_code = 404
        error = add_status_code(error_code)

    assert error_code in _sanic_exceptions

# Generated at 2022-06-14 07:12:09.798653
# Unit test for function add_status_code
def test_add_status_code():
    class Status(SanicException):
        pass

    assert Status.status_code is None
    assert Status.quiet is None

    add_status_code(100)(Status)
    assert Status.status_code == 100
    assert Status.quiet is True

    add_status_code(500, quiet=False)(Status)
    assert Status.status_code == 100
    assert Status.quiet is False

    add_status_code(500, quiet=True)(Status)
    assert Status.status_code == 500
    assert Status.quiet is True


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:12:17.056935
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class A(SanicException):
        pass

    assert A.status_code == 400
    assert A().status_code == 400
    assert A(message='HALP').status_code == 400
    assert A(message='HALP', status_code=418).status_code == 418
    assert A().quiet is True
    assert A(quiet=False).quiet is False

# Generated at 2022-06-14 07:12:29.054670
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    expected_header = {"WWW-Authenticate": f"{'Basic'} {''}".rstrip()}
    exception = Unauthorized("Auth required.", scheme="Basic")
    assert exception.headers == expected_header

    username = "jack"
    password = "pass"
    auth_header = f"username=\"{username}\", password=\"{password}\""
    expected_header = {"WWW-Authenticate": f"{'Basic'} {auth_header}".rstrip()}
    exception = Unauthorized("Auth required.",
                             scheme="Basic",
                             username=username,
                             password=password)
    assert exception.headers == expected_header

    exception = Unauthorized("Auth required.", status_code=401)
    assert exception.status_code == 401
    assert hasattr(exception, 'headers') == False

   

# Generated at 2022-06-14 07:12:31.887294
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class InvalidUsage1(SanicException):
        pass
    assert _sanic_exceptions[400].__name__ == "InvalidUsage1"



# Generated at 2022-06-14 07:12:37.916686
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class CustomException(Exception):
        pass
    ce = CustomException("Test")
    assert ce.status_code == 500

# Generated at 2022-06-14 07:12:48.598784
# Unit test for function add_status_code
def test_add_status_code():
    import unittest
    class TestException(SanicException):
        pass
    class TestCase(unittest.TestCase):
        def test_add_status_code(self):
            self.assertEqual(TestException.status_code, None)
            self.assertEqual(TestException.quiet, None)
            with self.assertRaises(TestException):
                raise TestException
            add_status_code(1)(TestException)
            self.assertEqual(TestException.status_code, 1)
            self.assertEqual(TestException.quiet, False)
            with self.assertRaises(TestException):
                raise TestException
            add_status_code(2, quiet=True)(TestException)
            self.assertEqual(TestException.status_code, 2)

# Generated at 2022-06-14 07:13:02.507115
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    exception = Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    assert exception.headers["WWW-Authenticate"] == 'Basic realm="Restricted Area"'
    exception = Unauthorized("Auth required.", scheme="Digest", realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    assert exception.headers["WWW-Authenticate"] == 'Digest realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu"'
    exception = Unauthorized("Auth required.", scheme="Bearer")
    assert exception.headers["WWW-Authenticate"] == 'Bearer'
    exception = Unauthorized("Auth required.", scheme="Bearer", realm="Restricted Area")
    assert exception.headers

# Generated at 2022-06-14 07:13:09.704249
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as e:
        assert e.message == "Auth required."
        assert e.status_code == 401
        assert e.headers == {'WWW-Authenticate': 'Basic realm="Restricted Area"'}

    try:
        raise Unauthorized("Auth required.", scheme="Bearer")
    except Unauthorized as e:
        assert e.message == "Auth required."
        assert e.status_code == 401
        assert e.headers == {'WWW-Authenticate': 'Bearer'}

# Generated at 2022-06-14 07:13:17.424422
# Unit test for function add_status_code
def test_add_status_code():
    from Sanic.exceptions import _sanic_exceptions
    @add_status_code(123)
    class TestException(Exception):
        pass
    assert _sanic_exceptions[123] == TestException
    assert TestException.status_code == 123
    assert TestException.quiet == True
    @add_status_code(456, False)
    class TestException2(Exception):
        pass
    assert _sanic_exceptions[456] == TestException2
    assert TestException2.status_code == 456
    assert TestException2.quiet == False
    @add_status_code(789, True)
    class TestException3(Exception):
        pass
    assert _sanic_exceptions[789] == TestException3
    assert TestException3.status_code == 789
    assert TestException3.quiet == True

# Generated at 2022-06-14 07:13:25.025720
# Unit test for function add_status_code
def test_add_status_code():
    #Test for SanicException
    try:
        add_status_code(400)(SanicException)
    except Exception as e:
        assert e.status_code == 400
    #Test for NotFound
    try:
        add_status_code(400)(NotFound)
    except Exception as e:
        assert e.status_code == 400
    #Test for InvalidUsage
    try:
        add_status_code(400)(InvalidUsage)
    except Exception as e:
        assert e.status_code == 400
    #Test for MethodNotSupported
    try:
        add_status_code(405)(MethodNotSupported)
    except Exception as e:
        assert e.status_code == 405
    #Test for ServerError

# Generated at 2022-06-14 07:13:31.239837
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class NewSanicException(SanicException):
        """
        **Status**: 404 Not Found
        """

    assert isinstance(NewSanicException(message="Test"), _sanic_exceptions[404])
    assert 404 in _sanic_exceptions


# Generated at 2022-06-14 07:13:45.335550
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404, False)
    class NotFound(SanicException):
        """
        This is an exception
        """
        pass
    assert(NotFound.status_code == 404)
    assert(NotFound.quiet == False)
    assert(str(NotFound) == "NotFound: This is an exception")

    @add_status_code(500, True)
    class ServerError(SanicException):
        """
        This is an exception
        """
        pass
    assert(ServerError.status_code == 500)
    assert(ServerError.quiet == True)
    assert(str(ServerError) == "ServerError: This is an exception")

    @add_status_code(503, None)
    class ServiceUnavailable(SanicException):
        """
        This is an exception
        """
       

# Generated at 2022-06-14 07:13:48.811919
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class TestException(Exception):
        pass
    assert _sanic_exceptions[100] == TestException

# Generated at 2022-06-14 07:13:52.964470
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    from sanic.exceptions import Unauthorized
    try:
        raise Unauthorized("Auth required.", scheme="Basic")
    except Unauthorized as e:
        assert e.headers["WWW-Authenticate"] == "Basic"

# Generated at 2022-06-14 07:13:57.625447
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class Custom404Error(Exception):
        pass

    assert _sanic_exceptions[404] == Custom404Error

# Generated at 2022-06-14 07:14:10.316860
# Unit test for function add_status_code
def test_add_status_code():
    # pylint: disable=missing-function-docstring

    # Check created exception class
    @add_status_code(418)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[418] == TestException

    # Check that args get passed to init
    class TestException2(SanicException):
        def __init__(self, message, status_code, quiet):
            assert status_code == 418
            assert quiet
            super().__init__(message, status_code)

    @add_status_code(418, True)
    class TestException2(TestException2):
        pass

    assert _sanic_exceptions[418] == TestException2

    # Check that args get passed to init

# Generated at 2022-06-14 07:14:12.505269
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(200)(SanicException)
    assert _sanic_exceptions[200] is SanicException

# Generated at 2022-06-14 07:14:15.933876
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(700)
    class TestException(SanicException):
        pass
    assert 700 == TestException.status_code



# Generated at 2022-06-14 07:14:28.277828
# Unit test for function add_status_code
def test_add_status_code():
    # Test add_status_code on random code
    code = random.randint(100, 600)
    assert add_status_code(code)(SanicException) == SanicException
    assert add_status_code(code, quiet=True)(SanicException).quiet == True
    assert add_status_code(code, quiet=False)(SanicException).quiet == False
    assert add_status_code(code, quiet=None)(SanicException).quiet == False

    # Test add_status_code on code 500
    code = 500
    assert add_status_code(code)(SanicException) == SanicException
    assert add_status_code(code, quiet=True)(SanicException).quiet == True
    assert add_status_code(code, quiet=False)(SanicException).quiet == False

# Generated at 2022-06-14 07:14:33.567609
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 400
    test_message = "test message"
    quiet = True
    test_ex = SanicException(test_message, status_code, quiet)
    assert test_ex.status_code == status_code
    assert test_ex.quiet == quiet

# Generated at 2022-06-14 07:14:34.914240
# Unit test for function add_status_code
def test_add_status_code():
    # TODO
    pass

# Generated at 2022-06-14 07:14:45.148126
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(581)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 581
    assert TestException().status_code == 581

    @add_status_code(582, quiet=True)
    class TestExceptionWithQuiet(SanicException):
        pass

    assert TestExceptionWithQuiet.status_code == 582
    assert TestExceptionWithQuiet().status_code == 582
    assert TestExceptionWithQuiet().quiet is True

    @add_status_code(583)
    class TestExceptionWithQuiet(SanicException):
        pass

    assert TestExceptionWithQuiet.status_code == 583
    assert TestExceptionWithQuiet().status_code == 583
    assert TestExceptionWithQuiet().quiet is False

# Generated at 2022-06-14 07:14:58.586882
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(status_code=400, quiet=True)
    class TestException(SanicException):
        pass
    assert _sanic_exceptions[400] == TestException
    assert _sanic_exceptions[400]().status_code == 400
    assert _sanic_exceptions[400]().message is None
    assert _sanic_exceptions[400]().quiet is True

    @add_status_code(status_code=500)
    class TestException2(SanicException):
        pass
    assert _sanic_exceptions[500] == TestException2
    assert _sanic_exceptions[500]().status_code == 500
    assert _sanic_exceptions[500]().message is None
    assert _sanic_exceptions[500]().quiet is None


# Generated at 2022-06-14 07:15:00.016799
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(408)(Exception)
    assert Exception.status_code == 408

# Generated at 2022-06-14 07:15:03.181577
# Unit test for function add_status_code

# Generated at 2022-06-14 07:15:12.513996
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class CustomizedException(SanicException):
        pass
    assert CustomizedException.status_code == 400
    assert 400 in _sanic_exceptions

    @add_status_code(500)
    class CustomizedException(SanicException):
        pass
    assert CustomizedException.quiet == True

    @add_status_code(500, quiet=True)
    class CustomizedException(SanicException):
        pass
    assert CustomizedException.quiet == True
    @add_status_code(500, quiet=False)
    class CustomizedException(SanicException):
        pass
    assert CustomizedException.quiet == False

# Generated at 2022-06-14 07:15:16.916519
# Unit test for function add_status_code
def test_add_status_code():
    assert getattr(_sanic_exceptions[503], "status_code", None) == 503
    assert getattr(_sanic_exceptions[503], "quiet", None) is True

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:15:23.417365
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(413)
    class PayloadTooLarge(SanicException):
        """
        **Status**: 413 Payload Too Large
        """

    assert PayloadTooLarge.status_code == 413
    assert PayloadTooLarge.quiet is True
    assert _sanic_exceptions[413] == PayloadTooLarge


# Generated at 2022-06-14 07:15:35.572867
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    # Test for add_status_code with True for quiet parameter
    my_exception = add_status_code(400, True)(MyException)
    assert my_exception.status_code == 400
    assert my_exception.quiet == True

    # Test for add_status_code with False for quiet parameter
    my_exception = add_status_code(400, False)(MyException)
    assert my_exception.status_code == 400
    assert my_exception.quiet == False

    # Test for add_status_code with None for quiet parameter
    my_exception = add_status_code(400)(MyException)
    assert my_exception.status_code == 400
    assert my_exception.quiet == False

    # Test for add_status_code with 500

# Generated at 2022-06-14 07:15:50.044462
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Normal(SanicException):
        pass
    assert _sanic_exceptions[200] == Normal

    @add_status_code(500)
    class OopsError(SanicException):
        pass
    assert _sanic_exceptions[500] == OopsError

    @add_status_code(400, quiet=False)
    class BadRequest(SanicException):
        pass
    assert _sanic_exceptions[400] == BadRequest
    exc = BadRequest()
    assert exc.quiet == False
    assert exc.status_code == 400

    @add_status_code(200, quiet=False)
    class OK(SanicException):
        pass
    assert _sanic_exceptions[200] == OK
    exc = OK()
    assert exc.quiet == False


# Generated at 2022-06-14 07:15:53.953283
# Unit test for function add_status_code
def test_add_status_code():

    def example_decorator(func):
        def function_wrapper(*args, **kwargs):
            f"This is a function wrapper {func}"
            func(*args, **kwargs)
        return function_wrapper

    @add_status_code(200)
    class Test():
        pass

    assert Test.status_code == 200

# Generated at 2022-06-14 07:15:57.675402
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class InvalidUsage(SanicException):
        pass

    assert _sanic_exceptions[400] == InvalidUsage

# Generated at 2022-06-14 07:15:59.083516
# Unit test for function add_status_code
def test_add_status_code():
    assert isinstance(abort, type(Exception))

# Generated at 2022-06-14 07:16:08.143783
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class ServerError1(SanicException):
        def __init__(self):
            pass

    assert ServerError1.status_code == 500
    assert _sanic_exceptions[500] is ServerError1

    @add_status_code(201)
    class ServerError2(SanicException):
        def __init__(self):
            pass

    assert ServerError2.status_code == 201
    assert _sanic_exceptions[201] is ServerError2

# Generated at 2022-06-14 07:16:17.000240
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(501)
    class NotImplementedException(SanicException):
        """
        **Status**: 501 Not Implemented
        """
        pass
    assert _sanic_exceptions.get(501) is NotImplementedException

# Generated at 2022-06-14 07:16:21.237040
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(401)
    class TestException(SanicException):
        pass

    assert (TestException.status_code == 401)
    assert (TestException.quiet == False)



# Generated at 2022-06-14 07:16:25.006910
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class PostOnlyMethod(SanicException):
        pass

    assert PostOnlyMethod.status_code == 400
    assert _sanic_exceptions[400] == PostOnlyMethod

# Generated at 2022-06-14 07:16:31.960429
# Unit test for function add_status_code
def test_add_status_code():
    def test_decorator(cls):
        assert(cls.status_code == status_code)
        assert(cls.quiet == True)
        assert(_sanic_exceptions[status_code] == cls)
        return cls
    status_code = 200
    add_status_code(status_code, quiet=True)(test_decorator)

# Generated at 2022-06-14 07:16:35.840907
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class MyCustomError(SanicException):
        pass

    assert _sanic_exceptions[100] == MyCustomError


# Generated at 2022-06-14 07:16:40.920863
# Unit test for function add_status_code
def test_add_status_code():
    '''
    Test that adding an exception works
    '''
    add_status_code(404)(NotFound)

    assert STATUS_CODES[404] == NotFound.__str__()
    # TODO Add second type of assertion

# Generated at 2022-06-14 07:16:44.797346
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class CustomException(SanicException):
        pass
    e = CustomException("test", status_code=400)
    assert e.status_code == 400

# Generated at 2022-06-14 07:16:51.442342
# Unit test for function add_status_code
def test_add_status_code():
    # Modify STATUS_CODES dict
    STATUS_CODES[200] = ""
    # Create exceptions with HTTP status codes
    @add_status_code(200)
    class Ex1(SanicException):
        pass

    @add_status_code(200)
    class Ex2(SanicException):
        pass

    # Assert that Ex1 and Ex2 are _sanic_exceptions
    assert Ex1.status_code == 200
    assert Ex2.status_code == 200
    assert Ex1.status_code in _sanic_exceptions
    assert Ex2.status_code in _sanic_exceptions
    assert type(_sanic_exceptions[200]) == type(Ex2)

test_add_status_code()

# Generated at 2022-06-14 07:16:54.777747
# Unit test for function add_status_code
def test_add_status_code():
    test = add_status_code(418)(SanicException)
    assert test.status_code == 418
    assert test.quiet == True

# Generated at 2022-06-14 07:17:00.868656
# Unit test for function add_status_code
def test_add_status_code():
    # Test error scenario
    try:
        @add_status_code(100)
        class A:
            pass
        assert False
    except KeyError:
        pass

    # Test valid scenario
    @add_status_code(200)
    class B:
        pass

    assert _sanic_exceptions[200] == B

# Generated at 2022-06-14 07:17:24.986341
# Unit test for function add_status_code
def test_add_status_code():
    # Test add_status_code function
    # Test case 1: test class of HTTPStatus code 201
    assert _sanic_exceptions[201].status_code == 201
    # Test case 2: test class of HTTPStatus code 404
    assert _sanic_exceptions[404].status_code == 404
    # Test case 3: test class of HTTPStatus code 400
    assert _sanic_exceptions[400].status_code == 400
    # Test case 4: test class of HTTPStatus code 405
    assert _sanic_exceptions[405].status_code == 405
    # Test case 5: test class of HTTPStatus code 503
    assert _sanic_exceptions[503].status_code == 503
    # Test case 6: test class of HTTPStatus code 500
    assert _sanic_exceptions[500].status_code == 500
    # Test

# Generated at 2022-06-14 07:17:29.088310
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class TestClass(SanicException):
        pass
    assert TestClass.status_code == 403
    assert TestClass.quiet == True
    assert TestClass.__doc__ is None


# Generated at 2022-06-14 07:17:31.357451
# Unit test for function add_status_code
def test_add_status_code():
    from sanic.exceptions import NotFound

    assert NotFound.status_code == 404



# Generated at 2022-06-14 07:17:43.218099
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(1001)
    class Foo(SanicException):
        pass

    assert Foo.status_code == 1001
    assert Foo().status_code == 1001

    @add_status_code(1002)
    class Bar(SanicException):
        pass

    assert Bar.status_code == 1002
    assert Bar().status_code == 1002
    
    @add_status_code(1003, "quiet")
    class Baz(SanicException):
        pass

    assert Baz.status_code == 1003
    assert Baz().status_code == 1003
    assert Baz().quiet == True

    @add_status_code(1004, quiet = False)
    class Qux(SanicException):
        pass

    assert Qux.status_code == 1004
    assert Qux().status_code

# Generated at 2022-06-14 07:17:47.966713
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(555)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 555

    @add_status_code(555, quiet=True)
    class TestException(SanicException):
        pass

    assert TestException.quiet is True

    @add_status_code(555, quiet=False)
    class TestException(SanicException):
        pass

    assert TestException.quiet is False



# Generated at 2022-06-14 07:17:53.198551
# Unit test for function add_status_code
def test_add_status_code():
    # status code not added
    assert 404 not in _sanic_exceptions
    assert isinstance(NotFound, type)

    # status code added
    assert 404 in _sanic_exceptions
    assert issubclass(_sanic_exceptions[404], SanicException)
    assert issubclass(NotFound, SanicException)

    @add_status_code(400)
    class BadRequestException(SanicException):
        pass

    # status code not added
    assert 400 in _sanic_exceptions
    assert issubclass(_sanic_exceptions[400], SanicException)
    assert issubclass(BadRequestException, SanicException)



# Generated at 2022-06-14 07:17:57.966898
# Unit test for function add_status_code
def test_add_status_code():
    status_codes = {200: "OK"}

    @add_status_code(200)
    class A(SanicException):
        status_code = 200

    assert A.status_code == 200
    assert _sanic_exceptions[200] == A

# Generated at 2022-06-14 07:18:07.761494
# Unit test for function add_status_code
def test_add_status_code():
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

# Generated at 2022-06-14 07:18:10.229327
# Unit test for function add_status_code
def test_add_status_code():
    try:
        add_status_code(500)
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-14 07:18:18.410580
# Unit test for function add_status_code
def test_add_status_code():
    try:
        abort(0)
    except Exception as e:
        assert e.status_code == 0
        assert e.args[0] == 'Unknown status code: 0'

    try:
        abort(400)
    except Exception as e:
        assert e.status_code == 400
        assert e.args[0] == 'Bad Request'

    try:
        abort(404)
    except Exception as e:
        assert e.status_code == 404
        assert e.args[0] == 'Not Found'



# Generated at 2022-06-14 07:18:44.945339
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class NewSanicException(SanicException):
        pass

    assert STATUS_CODES[400] == "Bad Request"
    assert NewSanicException.status_code == 400

# Generated at 2022-06-14 07:18:47.944519
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class CustomException(Exception):
        pass

    assert 400 in _sanic_exceptions
    assert _sanic_exceptions[400] is CustomException

# Generated at 2022-06-14 07:18:53.965327
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(501)
    class TestException(SanicException):
        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message)

    assert TestException.status_code == 501
    assert isinstance(_sanic_exceptions[501], TestException)

# Generated at 2022-06-14 07:19:06.473044
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class Teapot(SanicException):
        """
        **Status**: 418 I'm a teapot
        """

    assert Teapot.status_code == 418
    assert Teapot.quiet == False
    assert _sanic_exceptions[418] == Teapot
    Teapot.quiet = True
    assert Teapot.quiet == True

    @add_status_code(418, True)
    class Teapot(SanicException):
        """
        **Status**: 418 I'm a teapot
        """

    assert Teapot.quiet == True

    @add_status_code(418, False)
    class Teapot(SanicException):
        """
        **Status**: 418 I'm a teapot
        """

    assert Teapot

# Generated at 2022-06-14 07:19:20.731500
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class CustomException(SanicException):
        pass
    assert CustomException.status_code == 200
    # Ensure the code is actually added to _sanic_exception
    assert _sanic_exceptions[200] == CustomException

    @add_status_code(500)
    class CustomException(SanicException):
        pass
    assert CustomException.status_code == 500
    assert _sanic_exceptions[500] == CustomException

    @add_status_code(501)
    class CustomExceptionQuiet(SanicException):
        pass
    assert CustomExceptionQuiet.status_code == 501
    assert _sanic_exceptions[501] == CustomExceptionQuiet
    assert CustomExceptionQuiet.quiet == True


# Generated at 2022-06-14 07:19:24.162672
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123, quiet=True)
    class TestClass(SanicException):
        pass

    assert TestClass.status_code == 123
    assert TestClass.quiet



# Generated at 2022-06-14 07:19:33.037303
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class NotFound1(SanicException):
        pass
    assert _sanic_exceptions.get(404) == NotFound1
    assert NotFound1.quiet == True

    @add_status_code(405)
    class MethodNotSupported1(SanicException):
        pass
    assert _sanic_exceptions.get(405) == MethodNotSupported1
    assert MethodNotSupported1.quiet == False

    @add_status_code(403)
    class Forbidden1(SanicException):
        pass
    assert _sanic_exceptions.get(403) == Forbidden1
    assert Forbidden1.quiet == True

# Generated at 2022-06-14 07:19:35.558134
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class OK(SanicException):
        pass
    assert OK.status_code == 200
    assert isinstance(_sanic_exceptions[200], OK)
    assert issubclass(_sanic_exceptions[200], SanicException)

# Generated at 2022-06-14 07:19:39.475539
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200, 'OK')
    class OK(SanicException):
        pass

    assert OK.status_code == 200
    assert OK.message == 'OK'
    assert _sanic_exceptions.get(200, None) == OK


# Generated at 2022-06-14 07:19:49.708698
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test the function add_status_code, check if the created class has the
    correct status code, quiet value and message.
    """
    @add_status_code(600, quiet=False)
    class customEx1(SanicException):
        pass

    @add_status_code(700, quiet=True)
    class customEx2(SanicException):
        pass

    @add_status_code(800)
    class customEx3(SanicException):
        pass

    @add_status_code(900)
    class customEx4(SanicException):
        pass


# Generated at 2022-06-14 07:20:46.019069
# Unit test for function add_status_code
def test_add_status_code():
    class test_add_status_code1(SanicException):
        pass
    class test_add_status_code2(SanicException):
        pass
    add_status_code(200)(test_add_status_code1)
    add_status_code(201)(test_add_status_code2)
    assert test_add_status_code1.status_code == 200
    assert test_add_status_code2.status_code == 201
    assert _sanic_exceptions[200] == test_add_status_code1
    assert _sanic_exceptions[201] == test_add_status_code2

# Generated at 2022-06-14 07:20:59.627663
# Unit test for function add_status_code
def test_add_status_code():
    # SanicException
    assert isinstance(_sanic_exceptions[500], ServerError)
    assert _sanic_exceptions[500].status_code == 500
    # not quiet=true
    assert _sanic_exceptions[500].quiet == True

    # NotFound
    assert isinstance(_sanic_exceptions[404], NotFound)
    assert _sanic_exceptions[404].status_code == 404
    # quiet=true
    assert _sanic_exceptions[404].quiet == True

    # InvalidUsage
    assert isinstance(_sanic_exceptions[400], InvalidUsage)
    assert _sanic_exceptions[400].status_code == 400
    # quiet=true
    assert _sanic_exceptions[400].quiet == True

    # MethodNotSupported

# Generated at 2022-06-14 07:21:02.767219
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(555)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[555] == TestException


# Generated at 2022-06-14 07:21:07.355378
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class _Test(SanicException):
        pass

    assert _sanic_exceptions[400] is _Test
    assert _Test.status_code == 400


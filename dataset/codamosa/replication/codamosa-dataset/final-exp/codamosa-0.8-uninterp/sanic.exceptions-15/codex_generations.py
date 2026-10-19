

# Generated at 2022-06-14 07:11:26.503327
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    message = "Auth required."
    status_code = 401
    scheme = "Basic"
    realm = "Restricted Area"

    # With a Basic auth-scheme, realm MUST be present:
    with pytest.raises(Unauthorized) as exc:
        raise Unauthorized(message, status_code, scheme, realm)

    assert exc.value.message == message
    assert exc.value.status_code == status_code
    assert exc.value.headers["WWW-Authenticate"] == f'{scheme} realm="{realm}"'

    scheme = "Digest"
    qop = "auth, auth-int"
    algorithm = "MD5"
    nonce = "abcdef"
    opaque = "zyxwvu"

    # With a Digest auth-scheme, things are a bit more complicated:
   

# Generated at 2022-06-14 07:11:30.556017
# Unit test for function add_status_code
def test_add_status_code():
    # Verify that BaseException is overriden
    assert not issubclass(NotFound, BaseException)

    # Verify that add_status_code works
    assert issubclass(NotFound, SanicException)


# Generated at 2022-06-14 07:11:38.951505
# Unit test for function add_status_code
def test_add_status_code():
    def my_exception_class(SanicException):
        def __init__(self, message):
            super().__init__(message)

    my_exception_class = add_status_code(status_code=400)(my_exception_class)
    assert my_exception_class(message="Hello").status_code == 400


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-14 07:11:50.279186
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    from sanic import Sanic

    app = Sanic(__name__)

    @app.route('/')
    async def unauthorized(request):
        raise Unauthorized("Auth required.",
                           scheme="Basic",
                           realm="Restricted Area")

    request, response = app.test_client.get(
        '/', headers={'Content-type': 'application/json'})
    assert response.status == 401
    assert response.headers.get('Content-type') == 'application/json'

# Generated at 2022-06-14 07:11:54.144453
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(401)
    class Unauthorized2(SanicException):
        pass

    assert _sanic_exceptions[401] == Unauthorized2


# Check all exceptions are in the _sanic_exceptions dict and status code is set.

# Generated at 2022-06-14 07:11:57.682662
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    with pytest.raises(Unauthorized) as excinfo:
        raise Unauthorized(message="Invalid username or password",
                           status_code=401,
                           scheme="Basic")
    assert excinfo.value.message == 'Invalid username or password'
    assert excinfo.value.status_code == 401
    assert excinfo.value.headers == {'WWW-Authenticate': 'Basic'}


# Generated at 2022-06-14 07:12:04.490528
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class Created(SanicException):
        pass
    assert _sanic_exceptions[201] == Created
    assert STATUS_CODES[201] == b"Created"
    assert Created("test").status_code == 201
    assert Created("test", status_code=201).status_code == 201

# Generated at 2022-06-14 07:12:14.428250
# Unit test for function add_status_code
def test_add_status_code():
    # add a new exception
    error_code = -1
    message = 'An error'
    # The purpose of this test is to add a new exception to _sanic_exceptions
    # with status code error_code
    @add_status_code(error_code, quiet=True)
    class NewException(SanicException):
        pass

    exception = NewException(message, error_code)
    # exception should be a SanicException
    assert isinstance(exception, SanicException)
    # exception should have a status_code
    assert hasattr(exception, 'status_code')
    # exception should have quiet set to True
    assert hasattr(exception, 'quiet')
    # exception should be in _sanic_exceptions
    assert exception in _sanic_exceptions.values()

# Generated at 2022-06-14 07:12:27.751358
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as e:
        assert e.status_code == 401
        assert e.message == "Auth required."
        assert e.scheme == "Basic"
        assert e.headers == {"WWW-Authenticate": "Basic realm=\"Restricted Area\""}
    try:
        raise Unauthorized("Auth required.", scheme="Digest", realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    except Unauthorized as e:
        assert e.status_code == 401
        assert e.message == "Auth required."
        assert e.scheme == "Digest"

# Generated at 2022-06-14 07:12:35.251141
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # check that Unauthorized is a subclass of SanicException
    assert issubclass(Unauthorized, SanicException)

    # check that status code is 401 Unauthroized
    assert Unauthorized.status_code == 401

    # check that Unauthorized is not a quiet exception
    assert not getattr(Unauthorized, "quiet", False)

    # check that valid WWW-Auth header is generated (Basic auth-scheme)
    www_auth = "Basic realm=Restricted_Area"
    assert Unauthorized("Auth required.",
                        scheme="Basic",
                        realm="Restricted_Area").headers == {
                            'WWW-Authenticate': www_auth
                        }

    # check that valid WWW-Auth header is generated (Digest auth-scheme)

# Generated at 2022-06-14 07:12:45.616647
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(1000)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 1000
    assert TestException.quiet == None

    @add_status_code(1001, quiet=True)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 1001
    assert TestException.quiet == True

    @add_status_code(1003, quiet=False)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 1003
    assert TestException.quiet == False

    @add_status_code(1003, quiet=None)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 1003
    assert TestException.quiet == None

# Generated at 2022-06-14 07:12:56.931266
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(202)
    class MyException(Exception):
        pass
    assert (issubclass(_sanic_exceptions[202], MyException))
    assert (_sanic_exceptions[202].status_code == 202)
    assert _sanic_exceptions[202]().status_code == 202
    assert isinstance(_sanic_exceptions[202](), MyException)

    @add_status_code(202, False)
    class MyException2(Exception):
        pass
    assert (issubclass(_sanic_exceptions[202], (MyException, MyException2)))
    assert (_sanic_exceptions[202].status_code == 202)
    assert _sanic_exceptions[202]().status_code == 202
    assert _sanic_exceptions[202]().quiet is False

# Generated at 2022-06-14 07:13:07.613058
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class Invalid(SanicException):
        pass

    assert 400 in _sanic_exceptions
    assert _sanic_exceptions[400] == Invalid

    @add_status_code(401, True)
    class Unauthorized(SanicException):
        pass

    assert 401 in _sanic_exceptions
    assert _sanic_exceptions[401] == Unauthorized
    assert Unauthorized().quiet is True

    @add_status_code(402)
    class PaymentRequired(SanicException):
        pass

    assert 402 in _sanic_exceptions
    assert _sanic_exceptions[402] == PaymentRequired
    assert PaymentRequired().quiet is False

# Generated at 2022-06-14 07:13:19.068176
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(410)
    class Gone(SanicException):
        """
        **Status**: 410 Gone

        This response code SHOULD be used if the server knows, through some
        internally configurable mechanism, that an old resource is permanently
        unavailable and has no forwarding address.
        """
        pass

    assert (_sanic_exceptions[410] == Gone)
    assert (Gone.quiet == True)
    assert (Gone.status_code == 410)

    try:
        abort(410)
    except Gone as e:
        assert (e.status_code == 410)
        assert (e.message == "Gone")

# Generated at 2022-06-14 07:13:24.769047
# Unit test for function add_status_code
def test_add_status_code():

    test_dict = {}

    @add_status_code(400, quiet=True)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions is not test_dict
    assert _sanic_exceptions[400] is TestException
    assert TestException.quiet is True

# Generated at 2022-06-14 07:13:29.434345
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 404
    assert TestException.__name__ == 'TestException'

# Generated at 2022-06-14 07:13:35.371455
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 400

    class_decorator = add_status_code(status_code, quiet=True)

    @class_decorator
    class TestClass(SanicException):
        pass

    assert TestClass.status_code == status_code
    assert TestClass.quiet is True
    assert _sanic_exceptions[status_code] == TestClass



# Generated at 2022-06-14 07:13:40.647919
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(100)
    assert add_status_code(200)
    assert add_status_code(300)
    assert add_status_code(400)
    assert add_status_code(500)
    assert add_status_code(600)


# Generated at 2022-06-14 07:13:48.332728
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(400)(SanicException)
    assert SanicException.status_code == 400

    add_status_code(401)(SanicException)
    assert SanicException.status_code == 401

    add_status_code(402)(SanicException)
    assert SanicException.status_code == 402

    add_status_code(403)(SanicException)
    assert SanicException.status_code == 403



# Generated at 2022-06-14 07:13:53.191524
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyException(SanicException):
        pass

    class MyException(SanicException):
        pass
    add_status_code(400)(MyException)

    assert _sanic_exceptions[400] == MyException

# Generated at 2022-06-14 07:13:59.458697
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(500)(SanicException) == ServerError
    assert add_status_code(503)(SanicException) == ServiceUnavailable


# Generated at 2022-06-14 07:14:03.430627
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    decorated = add_status_code(99, quiet=True)(MyException)
    assert decorated is MyException
    assert decorated.status_code == 99
    assert decorated.quiet is True
    assert _sanic_exceptions[99] is MyException



# Generated at 2022-06-14 07:14:11.086254
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        pass
    assert _sanic_exceptions[400] == TestException
    assert TestException().status_code == 400
    @add_status_code(500)
    class TestException(SanicException):
        pass
    assert _sanic_exceptions[500] == TestException
    assert TestException().status_code == 500


#Execute unit test for function add_status_code
test_add_status_code()

# Generated at 2022-06-14 07:14:24.567771
# Unit test for function add_status_code
def test_add_status_code():
    """Tests add_status_code"""
    class TestException(SanicException):
        """Test Exception"""
    # test 400
    add_status_code(400)(TestException)
    assert TestException.status_code == 400
    assert TestException.quiet
    assert _sanic_exceptions[400] == TestException
    # test 500
    add_status_code(500)(TestException)
    assert TestException.status_code == 500
    assert not TestException.quiet
    assert _sanic_exceptions[500] == TestException
    # test 500 quiet
    add_status_code(500, quiet=True)(TestException)
    assert TestException.status_code == 500
    assert TestException.quiet
    assert _sanic_exceptions[500] == TestException

# Generated at 2022-06-14 07:14:29.862300
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class CustomException(SanicException):
        pass
    assert 404 in _sanic_exceptions
    assert _sanic_exceptions[404] == CustomException
    assert CustomException('').status_code == 404


# Generated at 2022-06-14 07:14:41.935989
# Unit test for function add_status_code
def test_add_status_code():
    global _sanic_exceptions
    # Check 404 exception
    try:
        abort(404)
    except SanicException as e:
        assert e.message == STATUS_CODES[404].decode("utf8")
        assert e.status_code == 404
        assert e.quiet
        assert e.__class__.__name__ == "NotFound"

    class MyException(SanicException):
        pass

    # Add a new 200 exception
    add_status_code(200)(MyException)
    try:
        abort(200)
    except MyException as e:
        assert e.message == STATUS_CODES[200].decode("utf8")
        assert e.status_code == 200
        assert e.__class__.__name__ == "MyException"

    # Add a new 412 exception with quiet

# Generated at 2022-06-14 07:14:44.714745
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class SanicTest(SanicException):
        pass
    assert SanicTest.status_code == 201

# Generated at 2022-06-14 07:14:58.290378
# Unit test for function add_status_code
def test_add_status_code():
    __sanic_exceptions = {}

    def __add_status_code(code, quiet=None):
        def __class_decorator(cls):
            cls.status_code = code
            if quiet or quiet is None and code != 500:
                cls.quiet = True
            __sanic_exceptions[code] = cls
            return cls

        return __class_decorator

    @__add_status_code(404)
    class __NotFound(SanicException):
        pass

    @__add_status_code(500)
    class __ServerError(SanicException):
        pass

    exception1 = __sanic_exceptions.get(404)
    exception2 = __sanic_exceptions.get(500)

    assert exception1.status_code == 404
    assert exception1.quiet

# Generated at 2022-06-14 07:15:08.994173
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(800)
    class NewException(SanicException):
        pass
    assert NewException.status_code == 800
    assert _sanic_exceptions[800] == NewException
    assert NewException().status_code == 800

    @add_status_code(999)
    class QuietException(SanicException):
        pass
    assert QuietException.status_code == 999
    assert QuietException.quiet == True
    assert _sanic_exceptions[999] == QuietException
    assert QuietException().status_code == 999
    assert QuietException().quiet == True


# Generated at 2022-06-14 07:15:10.811973
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class TestException(Exception):
        pass
    assert TestException.status_code == 418

# Generated at 2022-06-14 07:15:21.228846
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class ForbiddenTest(SanicException):
        pass
    e = ForbiddenTest('Forbidden')
    assert(e.status_code == 403)
    assert(e.quiet == True)


# Generated at 2022-06-14 07:15:25.587471
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class Test:
        pass

    assert _sanic_exceptions[123](
        "test", status_code=123, quiet=True
    ) is not None

# Generated at 2022-06-14 07:15:30.011709
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class FuncException(SanicException):
        pass

    assert _sanic_exceptions[500] == FuncException


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:15:33.764219
# Unit test for function add_status_code
def test_add_status_code():
    # Test pass
    add_status_code(418)(SanicException)
    # Test fail
    with pytest.raises(TypeError):
        add_status_code("418")(SanicException)

# Generated at 2022-06-14 07:15:48.105083
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(567)
    class A(SanicException):
        pass

    @add_status_code(567, quiet=True)
    class B(SanicException):
        pass

    @add_status_code(567, quiet=False)
    class C(SanicException):
        pass

    def _abort_with_message(status_code, expected_message):
        try:
            abort(status_code)
        except SanicException as e:
            assert e.status_code == status_code
            assert str(e) == expected_message
        else:
            raise AssertionError("abort() did not raise an exception.")


# Generated at 2022-06-14 07:15:52.275906
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass   
    
    add_status_code(400)(TestException)
    
    assert TestException.status_code == 400
    assert TestException.quiet == False
    assert _sanic_exceptions[400] == TestException

    _sanic_exceptions.clear()

# Generated at 2022-06-14 07:16:05.379147
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    assert TestException.status_code is None
    assert TestException.quiet is None

    add_status_code(500)(TestException)
    assert TestException.status_code == 500
    assert TestException.quiet is False

    add_status_code(404, quiet=True)(TestException)
    assert TestException.status_code == 404
    assert TestException.quiet is True

    add_status_code(200)(TestException)
    assert TestException.status_code == 200
    assert TestException.quiet is True

    add_status_code(500, quiet=True)(TestException)
    assert TestException.status_code == 500
    assert TestException.quiet is True

# Generated at 2022-06-14 07:16:15.816190
# Unit test for function add_status_code
def test_add_status_code():
    # Define a class decorator for adding exceptions to :class:`SanicException`
    @add_status_code(code=404)
    class NotFoundTest(SanicException):
        """
        **Status**: 404 Not Found
        """

        pass

    assert NotFoundTest.status_code == 404
    assert NotFoundTest.quiet == True

    # status_code=None
    with pytest.raises(TypeError) as excinfo:
        @add_status_code()
        class NotFoundTest(SanicException):
            pass
    assert "status_code=404" in str(excinfo.value)


# Generated at 2022-06-14 07:16:26.543149
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class MyException(SanicException):
        pass
    assert _sanic_exceptions[404] == MyException

    @add_status_code(400)
    class MyException(SanicException):
        pass
    assert _sanic_exceptions[400] == MyException

    @add_status_code(500)
    class MyException(SanicException):
        pass
    assert _sanic_exceptions[500] == MyException

    @add_status_code(500)
    class MyException(SanicException):
        pass
    assert _sanic_exceptions[500] == MyException



# Generated at 2022-06-14 07:16:31.206497
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(415)
    class UnsupportedMediaType(SanicException):
        pass
    assert UnsupportedMediaType.status_code == 415
    umt_instance = UnsupportedMediaType("Unsupported Media Type")
    assert umt_instance.status_code == 415

# Generated at 2022-06-14 07:16:50.107133
# Unit test for function add_status_code
def test_add_status_code():
    def do_raise(status_code, error, exception_class):
        try:
            abort(status_code, error)
        except exception_class as e:
            assert e.status_code == status_code
            assert e.message == error
            return

        assert False, "Expected exception"

    do_raise(401, "Authentication Required", Unauthorized)
    do_raise(401, "Authentication Required", SanicException)
    do_raise(402, "Payment Required", SanicException)
    do_raise(403, "Forbidden", Forbidden)
    do_raise(403, "Forbidden", SanicException)
    do_raise(404, "Not Found", SanicException)
    do_raise(405, "Method Not Allowed", SanicException)

# Generated at 2022-06-14 07:16:55.971064
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(444)
    class SanicExceptionWithStatus_444(SanicException):
        pass

    assert SanicExceptionWithStatus_444(message='test').status_code == 444
    assert SanicExceptionWithStatus_444(message='test').message == 'test'

# Generated at 2022-06-14 07:17:07.675429
# Unit test for function add_status_code
def test_add_status_code():
    try:
        raise abort(404)
    except NotFound:
        assert 1
    else:
        assert 0

    try:
        raise abort(400)
    except InvalidUsage:
        assert 1
    else:
        assert 0

    try:
        raise abort(405)
    except MethodNotSupported:
        assert 1
    else:
        assert 0

    try:
        raise abort(500)
    except ServerError:
        assert 1
    else:
        assert 0

    try:
        raise abort(503)
    except ServiceUnavailable:
        assert 1
    else:
        assert 0

    try:
        raise abort(408)
    except RequestTimeout:
        assert 1
    else:
        assert 0

    try:
        raise abort(413)
    except PayloadTooLarge:
        assert 1


# Generated at 2022-06-14 07:17:13.359254
# Unit test for function add_status_code
def test_add_status_code():
    #test for Quiet = True
    @add_status_code(402)
    class VException(SanicException):
        pass
    assert VException().quiet == True
    assert VException().status_code == 402

    #test for Quiet = False
    @add_status_code(402, quiet=False)
    class VException(SanicException):
        pass
    assert VException().quiet == False
    assert VException().status_code == 402

# Generated at 2022-06-14 07:17:18.117136
# Unit test for function add_status_code
def test_add_status_code():
    assert _sanic_exceptions[404] == NotFound
    assert _sanic_exceptions[500] == ServerError
    assert _sanic_exceptions[400] == InvalidUsage
    assert _sanic_exceptions[405] == MethodNotSupported
    assert _sanic_exceptions[503] == ServiceUnavailable

# Generated at 2022-06-14 07:17:21.881873
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class BadRequest(SanicException):
        pass
    assert _sanic_exceptions[400] == BadRequest
    assert _sanic_exceptions[400]().quiet

# Generated at 2022-06-14 07:17:25.910129
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class MyException(SanicException):
        pass

    assert(_sanic_exceptions[200] == MyException)

# Generated at 2022-06-14 07:17:39.221685
# Unit test for function add_status_code
def test_add_status_code():
    class Exc(SanicException):
        pass

    @add_status_code(500)
    class ServerError(SanicException):
        pass

    @add_status_code(500)
    class ServerError(SanicException):
        pass

    assert Exc.status_code == 500
    assert ServerError.status_code == 500
    assert ServerError.quiet is False

    @add_status_code(200)
    class Ok(SanicException):
        pass

    assert Ok.status_code == 200
    assert Ok.quiet is False

    @add_status_code(200, quiet=True)
    class Ok(SanicException):
        pass

    assert Ok.status_code == 200
    assert Ok.quiet is True


# Generated at 2022-06-14 07:17:41.769610
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(123, True)(SanicException)
    assert 123 in _sanic_exceptions
    assert _sanic_exceptions[123].quiet


# Generated at 2022-06-14 07:17:49.475281
# Unit test for function add_status_code
def test_add_status_code():
    # Build a dummy class inheriting from SanicException
    @add_status_code(200)
    class TestClass(SanicException):
        pass

    assert TestClass.status_code == 200
    assert isinstance(TestClass, type)

    assert TestClass(status_code=200, message="Test") == TestClass(
        status_code=200, message="Test")


# Test the add_status_code decorator

# Generated at 2022-06-14 07:18:16.978687
# Unit test for function add_status_code
def test_add_status_code():
    def class_decorator(cls):
        cls.status_code = 100
        if 1 or 1 is None and 100 != 500:
            cls.quiet = True
        _sanic_exceptions[100] = cls
        return cls
    add_status_code(code=100, quiet=1)

# Generated at 2022-06-14 07:18:22.077991
# Unit test for function add_status_code
def test_add_status_code():
    class SimpleException(SanicException):
        pass

    @add_status_code(1001)
    class ExceptionWithCode(SanicException):
        pass

    assert _sanic_exceptions[1001] == ExceptionWithCode


# Generated at 2022-06-14 07:18:27.147022
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(499)
    class CustomException(SanicException):
        """
        **Status**: 499 Custom Status
        """
        pass

    assert CustomException()
    assert CustomException().status_code == 499
    assert CustomException().quiet is True

# Generated at 2022-06-14 07:18:36.071165
# Unit test for function add_status_code
def test_add_status_code():

    global _sanic_exceptions
    _sanic_exceptions.clear()

    class Foo(SanicException):
        pass

    class Bar(SanicException):
        pass

    class NotQuiet(SanicException):
        pass

    add_status_code(400)(Foo)
    add_status_code(410, quiet=True)(Bar)
    add_status_code(500)(NotQuiet)

    assert _sanic_exceptions[400] is Foo
    assert _sanic_exceptions[410] is Bar
    assert _sanic_exceptions[500] is NotQuiet

    assert Foo.status_code == 400
    assert Bar.status_code == 410
    assert NotQuiet.status_code == 500

    assert Foo.quiet is None
    assert Bar.quiet is True

# Generated at 2022-06-14 07:18:43.364753
# Unit test for function add_status_code
def test_add_status_code():
    a=400;b=True;c='not found'
    @add_status_code(a,b)
    class NotFound(SanicException):
        """
        **Status**: 404 Not Found
        """
        pass
    assert NotFound.status_code == a;assert NotFound.quiet == b;assert _sanic_exceptions[a].__doc__ == c

# Generated at 2022-06-14 07:18:51.019051
# Unit test for function add_status_code
def test_add_status_code():
    class some:
        pass
    assert not hasattr(some, 'status_code')
    assert not hasattr(some, 'quiet')
    assert _sanic_exceptions.get(300, None) is None
    add_status_code(300)(some)
    assert hasattr(some, 'status_code')
    assert hasattr(some, 'quiet')
    assert some.status_code == 300
    assert some.quiet is True
    assert _sanic_exceptions.get(300, None) is some

# Generated at 2022-06-14 07:18:58.082321
# Unit test for function add_status_code
def test_add_status_code():
    code = 400
    @add_status_code(code)
    class DummyException:
        ''' Dummy Class for test. '''
        pass
    assert _sanic_exceptions[code] == DummyException
    assert DummyException.status_code == code
    assert DummyException.quiet == True
    del _sanic_exceptions[code]

# Generated at 2022-06-14 07:19:05.419795
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(code=200, quiet=True)
    class OnSuccess(SanicException):
        pass
    
    assert OnSuccess.status_code == 200
    assert OnSuccess.quiet == True

    @add_status_code(code=400, quiet=True)
    class OnBadRequest(SanicException):
        pass

    assert OnBadRequest.status_code == 400
    assert OnBadRequest.quiet == True

test_add_status_code()

# Generated at 2022-06-14 07:19:11.956331
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class HTTPOk(SanicException):
        pass

    assert HTTPOk.status_code == 200

    @add_status_code(200, quiet=True)
    class HTTPOk2(SanicException):
        pass

    assert HTTPOk2.quiet is True

    @add_status_code(200, quiet=False)
    class HTTPOk3(SanicException):
        pass

    assert HTTPOk3.quiet is False

# Generated at 2022-06-14 07:19:15.382754
# Unit test for function add_status_code
def test_add_status_code():
    class Foo(SanicException):
        pass
    add_status_code(500)(Foo)
    assert(isinstance(_sanic_exceptions[500], Foo))

# Generated at 2022-06-14 07:20:08.719408
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class Test(SanicException):
        pass

    assert Test.status_code == 400
    assert Test.quiet

    @add_status_code(500)
    class Test2(SanicException):
        pass

    assert Test2.status_code == 500
    assert not Test2.quiet

    @add_status_code(500, True)
    class Test3(SanicException):
        pass

    assert Test3.status_code == 500
    assert Test3.quiet

# Generated at 2022-06-14 07:20:10.854828
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class _(SanicException):
        pass
    assert _.status_code == 123
    assert _sanic_exceptions[123] == _

# Generated at 2022-06-14 07:20:14.783680
# Unit test for function add_status_code
def test_add_status_code():
    class TestException1(SanicException):
        pass

    @add_status_code(502)
    class TestException2(SanicException):
        pass

    assert TestException1().status_code == 400
    assert TestException2().status_code == 502

# Generated at 2022-06-14 07:20:17.770162
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class MyCustomException(SanicException):
        pass

    e = MyCustomException("My custom exception")
    assert e.status_code == 201

# Generated at 2022-06-14 07:20:23.774577
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestException(Exception):
        pass

    assert TestException is _sanic_exceptions[404]
    assert TestException(message="test_exception").status_code == 404

    try:
        raise TestException(message="test_exception")
    except TestException as e:
        assert e.status_code == 404



# Generated at 2022-06-14 07:20:27.105064
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 100
    @add_status_code(status_code)
    class MyClass(SanicException):
        pass
    assert status_code in _sanic_exceptions

# Generated at 2022-06-14 07:20:33.863533
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        def __init__(self, message):
            super().__init__(message)

    assert TestException.status_code == 400
    assert TestException(_sanic_exceptions[400].__doc__).status_code == 400



# Generated at 2022-06-14 07:20:36.079580
# Unit test for function add_status_code
def test_add_status_code():
    class_decorator = add_status_code(500)

    def test_cls(cls):
        _sanic_exceptions[500] = cls
        return cls

    class_decorator(SanicException) == test_cls(SanicException)

# Generated at 2022-06-14 07:20:47.103680
# Unit test for function add_status_code
def test_add_status_code():
    class T1(SanicException):
        pass

    add_status_code(404)(T1)
    add_status_code(400)(T1)
    add_status_code(405)(T1)
    add_status_code(500)(T1)
    add_status_code(503)(T1)
    add_status_code(408)(T1)
    add_status_code(413)(T1)
    add_status_code(416)(T1)
    add_status_code(417)(T1)
    add_status_code(403)(T1)
    add_status_code(401)(T1)
    add_status_code(500)(PyFileError)
    add_status_code(500)(URLBuildError)

    assert T1.status_code == 400
    assert T1

# Generated at 2022-06-14 07:20:53.326283
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestException(SanicException):
        pass

    inst = TestException('Test Message')
    assert inst.status_code == 404
    assert inst.message == 'Test Message'
    assert inst.args == ('Test Message',)
    assert inst.quiet is False

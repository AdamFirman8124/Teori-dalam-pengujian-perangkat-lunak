

# Generated at 2022-06-14 07:11:18.970962
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    assert hasattr(TestException, 'status_code') == False

    add_status_code(400)(TestException)

    assert hasattr(TestException, 'status_code') == True
    assert TestException.status_code == 400
    assert _sanic_exceptions.get(400) == TestException
    assert _sanic_exceptions.get(500) == ServerError



# Generated at 2022-06-14 07:11:25.473083
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    """
    Unauthorized should have header when scheme is set.
    """
    scheme = "Basic"
    realm = "Restricted Area"
    message = "Auth required."
    u = Unauthorized(message, scheme=scheme, realm=realm)
    assert u.headers["WWW-Authenticate"] == f"{scheme} realm=\"{realm}\""

# Generated at 2022-06-14 07:11:32.996088
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as e:
        assert e.message.find("Auth required.") != -1
        assert e.status_code == 401
        assert e.headers["WWW-Authenticate"] == "Basic realm=Restricted Area"


# Generated at 2022-06-14 07:11:49.682067
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    with pytest.raises(Unauthorized) as excinfo:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")

    assert excinfo.value.status_code == 401
    assert excinfo.value.headers["WWW-Authenticate"] == 'Basic realm="Restricted Area"'

    with pytest.raises(Unauthorized) as excinfo:
        raise Unauthorized("Auth required.", scheme="Digest",
                           realm="Restricted Area", qop="auth, auth-int",
                           algorithm="MD5", nonce="abcdef", opaque="zyxwvu")

    assert excinfo.value.status_code == 401

# Generated at 2022-06-14 07:11:54.030201
# Unit test for function abort
def test_abort():
    try:
        abort(403)
    except SanicException as e:
        assert e.status_code == 403
        assert e.message == b'Forbidden'
    else:
        raise AssertionError()

# Generated at 2022-06-14 07:12:02.195900
# Unit test for function abort
def test_abort():
    try:
        abort(200)
    except Exception as e:
        assert e.message == "OK"

    try:
        abort(500)
    except Exception as e:
        assert e.message == "Internal Server Error"
        assert e.status_code == 500

    try:
        abort(400)
    except Exception as e:
        assert e.message == "Bad Request"
        assert e.status_code == 400

# Generated at 2022-06-14 07:12:06.925645
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    with pytest.raises(Unauthorized) as exc_info:
        raise Unauthorized("Auth required.",
                           scheme="Basic",
                           realm="Restricted Area")
        assert exc_info.headers['WWW-Authenticate'] == "Auth required."

# Generated at 2022-06-14 07:12:14.853624
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")

    except Unauthorized as e:
        assert e.message == "Auth required."
        assert e.scheme == "Basic"
        assert e.realm == "Restricted Area"
        assert e.status_code == 401


if __name__ == "__main__":
    test_Unauthorized()

# Generated at 2022-06-14 07:12:20.205315
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", scheme="Digest", realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    except:
        pass

# Generated at 2022-06-14 07:12:29.295537
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as ex:
        pass
    try:
        raise Unauthorized("Auth required.", scheme="Digest", realm="Restricted Area", qop="auth", algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    except Unauthorized as ex:
        pass
    try:
        raise Unauthorized("Auth required.", scheme="Bearer")
    except Unauthorized as ex:
        pass
    try:
        raise Unauthorized("Auth required.", scheme="Bearer", realm="Restricted Area")
    except Unauthorized as ex:
        pass

# Generated at 2022-06-14 07:12:44.245155
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    """
    Tests SanicException.__init__ method using the example in the docstring
    of Unauthorized.
    """
    # When auth-scheme is specified, set "WWW-Authenticate" header
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as exc:
        assert exc.headers == {"WWW-Authenticate": 'Basic realm="Restricted Area"'}

    # With a Digest auth-scheme, things are a bit more complicated:

# Generated at 2022-06-14 07:12:50.163325
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    message = "Auth required."
    status_code = 401
    status_message = STATUS_CODES[status_code].decode("utf8")
    scheme = "Bearer"
    realm = "Restricted Area"
    params = {"realm": realm}

    try:
        raise Unauthorized(message, status_code, scheme, **params)
    except Unauthorized as e:
        assert e.message == message
        assert e.status_code == status_code
        assert str(e) == f"{status_message}: {message}"
        assert e.headers["WWW-Authenticate"] == f'{scheme} realm="{realm}"'
    else:
        assert False  # Exception was not raised. Failure!

# Generated at 2022-06-14 07:12:54.405033
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(320)
    class TestException(Exception):
        pass

    assert _sanic_exceptions[320] == TestException
    assert _sanic_exceptions[320]().status_code == 320

# Generated at 2022-06-14 07:12:55.968110
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(111)(int) is int
    assert add_status_code(111)(float) is float



# Generated at 2022-06-14 07:13:00.579266
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    """It should raise an exception with an empty WWW-Authenticate header. """
    try:
        raise Unauthorized("Auth required.", scheme="Foo")
    except Unauthorized as e:
        assert e.headers["WWW-Authenticate"] == "Foo"

# Generated at 2022-06-14 07:13:06.239354
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    with pytest.raises(Unauthorized):
        abort(401)
    with pytest.raises(Unauthorized) as excinfo:
        abort(401, message="Auth required.")
        assert excinfo.value.message == "Auth required."
        assert excinfo.value.scheme == "Basic"
        assert excinfo.value.realm == "Restricted Area"

# Generated at 2022-06-14 07:13:20.006980
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # Note: the implementation of Unauthorized is simple, so we test the
    #   non-default cases only.

    # Test 1: Unauthorized(...) with scheme = Basic and realm = "Restricted Area"
    #   and no other parameter
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as exception:
        assert exception.status_code == 401
        assert exception.headers == {"WWW-Authenticate": 'Basic realm="Restricted Area"'}
        assert str(exception) == "401: Auth required."
    else:
        pytest.fail("Test 1: Exception not raised")

    # Test 2: Unauthorized(...) with scheme = Digest and realm = "Restricted Area"
    #   and other parameters: qop="auth, auth-int", algorithm="MD5",
   

# Generated at 2022-06-14 07:13:24.218522
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    excp = Unauthorized(message="Unauthorized",
                           scheme="Basic",
                           realm="Restricted Area",
                           status_code=401)
    assert excp.status_code == 401

#Unit test for method abort

# Generated at 2022-06-14 07:13:34.595042
# Unit test for function add_status_code
def test_add_status_code():
    assert _sanic_exceptions
    assert abort(404)
    assert abort(404, b"my message")
    assert abort(404, "my message")
    assert isinstance(abort(404), NotFound)
    assert isinstance(abort(500), ServerError)
    # These are not quiet by default
    assert not isinstance(abort(500), ServerError).quiet
    assert not isinstance(abort(404), NotFound).quiet
    # But these are
    assert isinstance(abort(400), InvalidUsage).quiet
    assert isinstance(abort(405), MethodNotSupported).quiet

# Generated at 2022-06-14 07:13:42.491258
# Unit test for function add_status_code
def test_add_status_code():
    assert isinstance(NotFound, SanicException)
    assert NotFound.status_code == 404
    assert NotFound.quiet == True

    assert isinstance(InvalidUsage, SanicException)
    assert InvalidUsage.status_code == 400
    assert InvalidUsage.quiet == True

    assert isinstance(MethodNotSupported, SanicException)
    assert MethodNotSupported.status_code == 405
    assert MethodNotSupported.quiet == True

    assert isinstance(ServerError, SanicException)
    assert ServerError.status_code == 500
    assert ServerError.quiet == False

    assert isinstance(ServiceUnavailable, SanicException)
    assert ServiceUnavailable.status_code == 503
    assert ServiceUnavailable.quiet == True

# Generated at 2022-06-14 07:13:56.379555
# Unit test for function add_status_code
def test_add_status_code():

    class TestSanicException(SanicException):
        pass

    _sanic_exceptions = {}
    
    decorator = add_status_code(404, False)
    decorator(TestSanicException)

    assert issubclass(_sanic_exceptions[404], TestSanicException)
    assert _sanic_exceptions[404].status_code == 404
    assert _sanic_exceptions[404].quiet == False

    decorator = add_status_code(405)
    decorator(TestSanicException)

    assert issubclass(_sanic_exceptions[405], TestSanicException)
    assert _sanic_exceptions[405].status_code == 405
    assert _sanic_exceptions[405].quiet == True

    decorator = add_status_code(500, True)

# Generated at 2022-06-14 07:14:02.589652
# Unit test for function add_status_code
def test_add_status_code():
    assert _sanic_exceptions[404] == NotFound
    assert _sanic_exceptions[400] == InvalidUsage
    assert _sanic_exceptions[405] == MethodNotSupported
    assert _sanic_exceptions[500] == ServerError
    assert _sanic_exceptions[503] == ServiceUnavailable


# Generated at 2022-06-14 07:14:12.872461
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(402)
    class A(SanicException):
        pass
    assert A.status_code == 402
    assert A in _sanic_exceptions
    assert _sanic_exceptions[402] == A

    @add_status_code(403, True)
    class A(SanicException):
        pass
    assert A.status_code == 403
    assert A.quiet == True
    assert A in _sanic_exceptions
    assert _sanic_exceptions[403] == A

    class A(SanicException):
        pass
    a = A("a")
    assert a.status_code == 500
    assert a.quiet == False



# Generated at 2022-06-14 07:14:17.969681
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Hello(SanicException):
        pass
    hello = Hello("Hello!")
    assert hello.status_code == 200
    assert hello.quiet is True
    assert _sanic_exceptions.get(200) == Hello

# Generated at 2022-06-14 07:14:21.334207
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(413)
    class TestClass(SanicException):
        pass
    assert TestClass.status_code == 413
    assert TestClass.quiet == True

# Generated at 2022-06-14 07:14:31.375772
# Unit test for function add_status_code
def test_add_status_code():
    class SanicException(Exception):
        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message)
            self.status_code = status_code
            # quiet=None/False/True with None meaning choose by status
            if quiet or quiet is None and status_code not in (None, 500):
                self.quiet = True

    exception_dict = {}

    def add_status_code(code, quiet=None):
        def class_decorator(cls):
            cls.status_code = code
            if quiet or quiet is None and code != 500:
                cls.quiet = True
            exception_dict[code] = cls
            return cls

        return class_decorator


# Generated at 2022-06-14 07:14:37.063814
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class InvalidJsUsage(SanicException):
        """
        **Status**: 400 Bad Request
        """

        pass
    
    import pytest    
    with pytest.raises(InvalidJsUsage):
        raise InvalidJsUsage("Invalid js usage")

# Generated at 2022-06-14 07:14:43.645255
# Unit test for function add_status_code
def test_add_status_code():
    """
    Function test for add_status_code
    """

    from sanic.exceptions import add_status_code

    # Test status code not in _sanic_exceptions
    @add_status_code(418)
    class TestStatusCode(SanicException):
        pass

    assert TestStatusCode(message='Hello, world!', status_code=418).status_code == 418

    # Test status code in _sanic_exceptions
    @add_status_code(400)
    class TestStatusCode(SanicException):
        pass

    assert TestStatusCode(message='Hello, world!', status_code=400).status_code == 400



# Generated at 2022-06-14 07:14:53.517649
# Unit test for function add_status_code
def test_add_status_code():
    class CustomException(SanicException):
        pass

    # Test for custom exception
    assert add_status_code(400, False)(CustomException)

    # Test for ExceptionError
    assert add_status_code(500, True)(Exception)

    # Test for SanicException
    assert add_status_code(400, True)(SanicException)
    assert add_status_code(400)(SanicException)
    assert add_status_code(400, None)(SanicException)

    # Test to ensure an exception is raised
    try:
        add_status_code(400)(Exception)
    except TypeError:
        pass


# Generated at 2022-06-14 07:15:02.956577
# Unit test for function add_status_code
def test_add_status_code():
    # 被装饰的对象会被修改相应的属性, 也就是我们加的quiet和status_code属性
    @add_status_code(404)
    class NotFound(SanicException):
        """
        **Status**: 404 Not Found
        """
        pass
    exception = NotFound('Not Found', 404)
    assert exception.status_code == 404
    assert exception.quiet == True
    # 不传递quiet参数, 会自动设置quiet属性为True

# Generated at 2022-06-14 07:15:08.870264
# Unit test for function add_status_code
def test_add_status_code():

    @add_status_code(201)
    class Created(SanicException):
        pass
    assert _sanic_exceptions[201].__name__ == 'Created'
    assert _sanic_exceptions[201].status_code == 201
    assert _sanic_exceptions[201](message='testing').message == 'testing'
    assert _sanic_exceptions[201]().status_code == 201

if __name__ == '__main__':
    test_add_status_code()

# Generated at 2022-06-14 07:15:11.888755
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    def test_func():
        pass

    assert "test_func" in globals().keys(), "test_func existed or not"
    assert test_func.status_code == 100, "test function status code is not 100"



# Generated at 2022-06-14 07:15:20.675716
# Unit test for function add_status_code
def test_add_status_code():
    class A(SanicException):
        pass

    class B(SanicException):
        pass

    assert not A.quiet
    assert not B.quiet

    with_status = add_status_code(400)
    with_status(A)
    assert A.__name__ == A.__qualname__ == "A"
    assert A.status_code == 400
    assert A.quiet
    assert _sanic_exceptions[400] is A

    with_quiet = add_status_code(500, quiet=True)
    with_quiet(B)
    assert B.__name__ == B.__qualname__ == "B"
    assert B.status_code == 500
    assert B.quiet
    assert _sanic_exceptions[500] is B

# Generated at 2022-06-14 07:15:34.127010
# Unit test for function add_status_code
def test_add_status_code():
    """
    This function test add_status_code(code, quiet=None)
    """

    # Testing status code that needs to be added
    code = 555
    quiet = False

    @add_status_code(code, quiet)
    class SanicException(Exception):
        """
        This class test SanicException(Exception)
        """
        def __init__(self, message, status_code=None, quiet=None):
            super.__init__(message)

    assert code in _sanic_exceptions
    assert _sanic_exceptions[code].quiet == quiet

    # Testing for status code that doesn't need to be added
    code = 500
    quiet = False


# Generated at 2022-06-14 07:15:39.317154
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 418
    message = STATUS_CODES[status_code].decode("utf8")
    with pytest.raises(SanicException) as e:
        abort(status_code)
    assert e.value.message == message

# Generated at 2022-06-14 07:15:48.843167
# Unit test for function add_status_code
def test_add_status_code():
    def test_class():
        pass

    add_status_code(404)(test_class)
    assert test_class.status_code == 404
    assert test_class.quiet is True

    add_status_code(500, False)(test_class)
    assert test_class.status_code == 500
    assert test_class.quiet is False

    def test_class2():
        pass

    add_status_code()(test_class2)
    assert test_class2.status_code == 500
    assert test_class2.quiet is False

# Generated at 2022-06-14 07:15:56.009107
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(421)
    class MisdirectedRequest(Exception):
        pass

    # Check attributes of the exception
    assert issubclass(MisdirectedRequest, SanicException)
    assert MisdirectedRequest.status_code == 421
    assert MisdirectedRequest.quiet is False

    # Check that the exception can be raised
    with pytest.raises(MisdirectedRequest):
        raise MisdirectedRequest("")


# Unit tests for function abort

# Generated at 2022-06-14 07:16:08.580611
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class SomeException(Exception):
        pass

    assert SomeException.status_code == 123
    assert SomeException(123, 'bla', 'blub').status_code == 123

    try:
        raise SomeException()
    except Exception as e:
        assert e.status_code == 123

    @add_status_code(123)
    class SomeException(SanicException):
        pass

    assert SomeException.status_code == 123
    assert SomeException(123, 'bla', 'blub').status_code == 123

    try:
        raise SomeException()
    except SanicException as e:
        assert e.status_code == 123

    try:
        raise SomeException()
    except Exception as e:
        assert e.status_code == 123



# Generated at 2022-06-14 07:16:15.230002
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(401)
    class Unauthorized(SanicException):
        """
        **Status**: 401 Unauthorized
        """
        def __init__(self, message, status_code=None):
            super().__init__(message, status_code)
    assert _sanic_exceptions[401] == Unauthorized

# Generated at 2022-06-14 07:16:19.336641
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[200] == TestException
    assert _sanic_exceptions[200]().status_code == 200



# Generated at 2022-06-14 07:16:25.544316
# Unit test for function add_status_code
def test_add_status_code():
    class MockException(SanicException):
        pass

    status_code = 404
    add_status_code(status_code)(MockException)
    assert MockException.status_code == status_code
    assert status_code in _sanic_exceptions

# Generated at 2022-06-14 07:16:34.296500
# Unit test for function add_status_code
def test_add_status_code():
    # As it is not a function, I can't get the doc string from Abort
    # Test if the doc string is correctly added
    assert NotFound.__doc__ == '''
    **Status**: 404 Not Found
    '''
    assert InvalidSignal.__doc__ == None
    # Test if the constant is correctly added
    assert NotFound.status_code == 404
    assert InvalidSignal.status_code == None
    # Test if the exception is correctly added
    assert abort(404) == '404 Not Found'
    assert abort(500) == '500 Internal Server Error'
    assert abort(0) == '500 Internal Server Error'
    # 404 is a quiet exception, thus it won't raise exception
    assert abort(404) == '404 Not Found'
    assert abort(500) == '500 Internal Server Error'


# Generated at 2022-06-14 07:16:41.758785
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class SanicException200(SanicException):
        pass

    @add_status_code(201)
    class SanicException201(SanicException):
        pass

    assert(_sanic_exceptions[200] == SanicException200)
    assert(_sanic_exceptions[201] == SanicException201)

# Generated at 2022-06-14 07:16:44.813789
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        pass

    assert isinstance(TestException(), SanicException)
    assert 400 in _sanic_exceptions

# Generated at 2022-06-14 07:16:51.564287
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(Exception):
        status_code = 200

    @add_status_code(400)
    class Test400Exception(Exception):
        status_code = 400
        quiet = True

    assert TestException.status_code == 200
    assert Test400Exception.status_code == 400
    assert Test400Exception.quiet is True
    assert _sanic_exceptions[400] == Test400Exception

# Generated at 2022-06-14 07:17:04.605997
# Unit test for function add_status_code
def test_add_status_code():
    class Foo:
        pass

    class Bar:
        pass

    assert add_status_code(400)(Foo) == Foo
    assert add_status_code(500)(Bar) == Bar
    assert Foo.status_code == 400
    assert Bar.status_code == 500

    assert add_status_code(500, quiet=False)(Bar) == Bar
    assert Bar.quiet is False

    assert add_status_code(200)(Bar) == Bar
    assert Bar.status_code == 200
    assert Bar.quiet is True

    assert add_status_code(400, quiet=False)(Foo) == Foo
    assert Foo.status_code == 400
    assert Foo.quiet is False

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:17:12.824122
# Unit test for function add_status_code
def test_add_status_code():
    # Make sure add_status_code as expected
    assert add_status_code(300)(SanicException).status_code == 300
    assert add_status_code(500)(SanicException).quiet is None
    assert add_status_code(None, quiet=True)(SanicException).quiet is True
    assert add_status_code(300, True)(SanicException).quiet is True
    assert add_status_code(300)(SanicException).quiet is None
    assert _sanic_exceptions[300] == add_status_code(300)(SanicException)


# Generated at 2022-06-14 07:17:15.376407
# Unit test for function add_status_code
def test_add_status_code():
    try:
        add_status_code(501)(Exception)('Something Wrong')
    except Exception as e:
        assert e.status_code == 501

# Generated at 2022-06-14 07:17:19.781931
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class SanicException200(Exception):
        pass

    assert "200" in list(_sanic_exceptions.keys())
    assert _sanic_exceptions[200] == SanicException200

# Generated at 2022-06-14 07:17:23.253172
# Unit test for function add_status_code
def test_add_status_code():
    foo = None
    @add_status_code(100)
    class TestAddStatusCode(SanicException):
        foo = None

    assert TestAddStatusCode.status_code == 100


# Generated at 2022-06-14 07:17:30.522282
# Unit test for function add_status_code
def test_add_status_code():
    try:
        raise abort(404)
    except NotFound:
        assert True
    else:
        assert False


# Generated at 2022-06-14 07:17:36.536805
# Unit test for function add_status_code
def test_add_status_code():
    class SanicException(Exception):
        pass
    @add_status_code(404)
    class NotFound(SanicException):
        pass
    assert NotFound.status_code == 404
    assert NotFound.quiet == True
    assert _sanic_exceptions[404].__name__ == "NotFound"

# Generated at 2022-06-14 07:17:47.602508
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class MyException(SanicException):
        pass
    assert 201 in _sanic_exceptions
    try:
        raise MyException()
    except MyException as e:
        assert e.status_code == 201
        assert e.message == STATUS_CODES[201].decode('utf8')


# SanicException = exceptions.SanicException
# add_status_code = exceptions.add_status_code
# NotFound = exceptions.NotFound
# InvalidUsage = exceptions.InvalidUsage
# MethodNotSupported = exceptions.MethodNotSupported
# ServerError = exceptions.ServerError
# ServiceUnavailable = exceptions.ServiceUnavailable
# URLBuildError = exceptions.URLBuildError
# FileNotFound = exceptions.FileNotFound
# RequestTimeout = exceptions.RequestTimeout
# PayloadTooLarge = exceptions

# Generated at 2022-06-14 07:17:54.050070
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(501)
    class NotImplementedException(SanicException):
        """
        **Status**: 501 Not Implemented
        """

        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message, status_code, quiet)

    assert hasattr(NotImplementedException, "status_code")
    assert hasattr(NotImplementedException, "quiet")

    assert 501 in _sanic_exceptions
    assert _sanic_exceptions[501] == NotImplementedException

    # test exception with quiet=True
    @add_status_code(502, quiet=True)
    class BadGatewayException(SanicException):
        """
        **Status**: 502 Bad Gateway
        """


# Generated at 2022-06-14 07:17:59.018639
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[400] is TestException
    assert repr(_sanic_exceptions[400]).startswith("<class")

# Generated at 2022-06-14 07:18:08.986778
# Unit test for function add_status_code
def test_add_status_code():
    class CustomException(Exception):
        pass

    assert add_status_code(404)
    assert add_status_code(404, True)
    assert add_status_code(404, False)
    assert add_status_code(404, None)

    with pytest.raises(AttributeError, match=r".* has no attribute 'status_code'"):
        add_status_code(404)(CustomException)
    with pytest.raises(AttributeError, match=r".* has no attribute 'status_code'"):
        add_status_code(404)(CustomException)



# Generated at 2022-06-14 07:18:16.822497
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(300)
    class SanicException300(SanicException):
        """
        **Status**: 300
        """
        pass

    @add_status_code(400)
    class SanicException400(SanicException):
        """
        **Status**: 400
        """
        pass

    assert SanicException400.status_code == 400
    assert SanicException300.status_code == 300
    assert _sanic_exceptions[300] == SanicException300

# Generated at 2022-06-14 07:18:21.607032
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class Test(SanicException):
        pass

    @add_status_code(456, quiet=True)
    class Test(SanicException):
        pass

    @add_status_code(789, quiet=False)
    class Test(SanicException):
        pass

    try:
        raise Test("test")
    except Test as e:
        assert e.status_code == 123
        assert not e.quiet

    try:
        raise Test("test")
    except Test as e:
        assert e.status_code == 456
        assert e.quiet

    try:
        raise Test("test")
    except Test as e:
        assert e.status_code == 789
        assert not e.quiet
        
if __name__ == "__main__":
    test_

# Generated at 2022-06-14 07:18:33.585931
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(status_code=200)
    class TestClass(SanicException):
        pass
    
    assert issubclass(TestClass, SanicException)
    assert TestClass.status_code == 200
    assert TestClass.quiet is None
    assert isinstance(_sanic_exceptions[200], type)
    assert _sanic_exceptions[200] == TestClass
    
    @add_status_code(status_code=300, quiet=True)
    class TestClass2(SanicException):
        pass
    
    assert issubclass(TestClass2, SanicException)
    assert TestClass2.status_code == 300
    assert TestClass2.quiet is True
    assert isinstance(_sanic_exceptions[300], type)
    assert _sanic_exceptions[300] == TestClass

# Generated at 2022-06-14 07:18:42.267345
# Unit test for function add_status_code
def test_add_status_code():
    class CustomException(SanicException):
        def __init__(self, message, status_code=200, quiet=True):
            super().__init__(message)
            self.status_code = status_code
            self.quiet = quiet

    add_status_code(200)(CustomException)
    assert 200 in _sanic_exceptions.keys()
    assert _sanic_exceptions[200] == CustomException


# Generated at 2022-06-14 07:18:56.940898
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class MyException(SanicException):
        pass

    assert MyException.status_code == 123
    assert _sanic_exceptions[123] == MyException
    assert type(_sanic_exceptions[123]) == type(MyException) is \
                                         type(SanicException)


# Generated at 2022-06-14 07:19:01.599381
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class NewException(SanicException):
        pass
    assert NewException.status_code == 400
    assert _sanic_exceptions[400] == NewException
    assert NewException(message="Test message").message == "Test message"



# Generated at 2022-06-14 07:19:07.121240
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(3000)
    class Block(SanicException):
        pass
    @add_status_code(3001)
    class Block1(SanicException):
        pass

    assert _sanic_exceptions[3000] == Block
    assert _sanic_exceptions[3001] == Block1
    assert Block.status_code == 3000
    assert Block1.status_code == 3001


# Generated at 2022-06-14 07:19:15.106031
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(404)(SanicException).status_code == 404
    assert add_status_code(500)(SanicException).status_code == 500
    assert add_status_code(404)(SanicException).quiet == True
    assert add_status_code(500)(SanicException).quiet == None


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:19:19.088174
# Unit test for function add_status_code
def test_add_status_code():
    # Test for status_code = 404
    assert _sanic_exceptions[404] == NotFound

    # Test for status_code = 503
    assert _sanic_exceptions[503] == ServiceUnavailable

# Generated at 2022-06-14 07:19:23.687858
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class StatusCode200(SanicException):
        pass
    assert StatusCode200().status_code == 200
    assert _sanic_exceptions[200].__name__ == 'StatusCode200'
    assert _sanic_exceptions[200]() is not None

# Generated at 2022-06-14 07:19:29.334500
# Unit test for function add_status_code
def test_add_status_code():
    # The decorator raises an exception if an error occurs.
    @add_status_code(404)
    class testClassOne(SanicException):
        pass

    # Check if class is a subclass of SanicException, that is, if the class is
    # in the dictionary _sanic_exceptions.
    assert testClassOne.__name__ in _sanic_exceptions

# Generated at 2022-06-14 07:19:38.383937
# Unit test for function add_status_code
def test_add_status_code():
    assert STATUS_CODES[500] == b"Internal Server Error"
    assert STATUS_CODES[404] == b"Not Found"
    assert STATUS_CODES[401] == b"Unauthorized"
    assert STATUS_CODES[400] == b"Bad Request"
    assert STATUS_CODES[408] == b"Request Timeout"
    assert STATUS_CODES[413] == b"Payload Too Large"
    assert STATUS_CODES[503] == b"Service Unavailable"
    assert STATUS_CODES[416] == b"Range Not Satisfiable"
    assert STATUS_CODES[417] == b"Expectation Failed"
    assert STATUS_CODES[403] == b"Forbidden"
    assert STATUS_CODES

# Generated at 2022-06-14 07:19:49.284373
# Unit test for function add_status_code
def test_add_status_code():
    # import question code
    from sanic import SanicException
    # import auto test
    from utils import assert_raises
    app = SanicException("Not Found", status_code=404)
    assert app.status_code == 404
    assert app.message == "Not Found"
    app = SanicException("Server Error", status_code=500)
    assert app.status_code == 500
    assert app.message == "Server Error"
    app = SanicException("Server Error", status_code=503)
    assert app.status_code == 503
    assert app.message == "Server Error"
    app = SanicException("Request Timeout", status_code=408)
    assert app.status_code == 408
    assert app.message == "Request Timeout"

# Generated at 2022-06-14 07:19:56.246582
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestException(Exception):
        pass
    assert TestException.status_code == 404
    assert TestException.quiet == True
    
    @add_status_code(500)
    class TestException2(Exception):
        pass
    assert TestException2.status_code == 500
    assert TestException2.quiet == False



# Generated at 2022-06-14 07:20:27.838146
# Unit test for function add_status_code
def test_add_status_code():
    
    def class_decorator(cls):
        cls.status_code = code
        if quiet or quiet is None and code != 500:
            cls.quiet = True
        _sanic_exceptions[code] = cls
        return cls

    class SanicException(Exception):
        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message)

            if status_code is not None:
                self.status_code = status_code

            # quiet=None/False/True with None meaning choose by status
            if quiet or quiet is None and status_code not in (None, 500):
                self.quiet = True
    """
    Test for method add_status_code
    """
    code = 404
    quiet = None
    

# Generated at 2022-06-14 07:20:41.824113
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class NewException(SanicException):
        pass

    assert _sanic_exceptions[400] == NewException

    @add_status_code(400, False)
    class NewException2(SanicException):
        pass

    assert _sanic_exceptions[400] == NewException2
    assert hasattr(NewException2, 'status_code')
    assert NewException2.status_code == 400
    assert not hasattr(NewException2, 'quiet')

    @add_status_code(400, True)
    class NewException3(SanicException):
        pass

    assert _sanic_exceptions[400] == NewException3
    assert hasattr(NewException3, 'status_code')
    assert NewException3.status_code == 400

# Generated at 2022-06-14 07:20:44.713925
# Unit test for function add_status_code
def test_add_status_code():
    code = 12345
    @add_status_code(code)
    class TestException(SanicException):
        pass
    assert TestException.status_code == code


# Generated at 2022-06-14 07:20:53.028221
# Unit test for function add_status_code
def test_add_status_code():
    code = 404
    quiet = True
    # Expected result of function add_status_code

# Generated at 2022-06-14 07:21:05.519368
# Unit test for function add_status_code
def test_add_status_code():
    from sanic.exceptions import (
        InvalidUsage,
        NotFound,
        ServerError,
        MethodNotSupported,
    )

    @add_status_code(400)
    class TestStatusCode400(SanicException):
        pass

    assert TestStatusCode400.status_code == 400
    assert TestStatusCode400().status_code == 400
    assert issubclass(TestStatusCode400, InvalidUsage)

    @add_status_code(404)
    class TestStatusCode404(SanicException):
        pass

    assert TestStatusCode404.status_code == 404
    assert TestStatusCode404().status_code == 404
    assert issubclass(TestStatusCode404, NotFound)

    @add_status_code(500)
    class TestStatusCode500(SanicException):
        pass

    assert TestStatusCode

# Generated at 2022-06-14 07:21:08.940671
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class ImATeapot(SanicException):
        pass
    assert ImATeapot.status_code == 418

# Generated at 2022-06-14 07:21:18.872622
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test add_status_code(code, quiet=None)
    """
    # code is not a intger
    try:
        @add_status_code("a")
        class ATestException(Exception):
            pass
    except TypeError:
        pass
    else:
        assert False, "code should be int type"

    # add status code 200
    @add_status_code(200)
    class A200Exception(Exception):
        pass
    assert A200Exception.status_code == 200
    assert A200Exception.quiet is None
    assert _sanic_exceptions[200] == A200Exception

    #add status code 500
    @add_status_code(500)
    class A500Exception(Exception):
        pass
    assert A500Exception.status_code == 500
    assert A500Exception.quiet
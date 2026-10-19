

# Generated at 2022-06-14 07:11:17.425158
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(411)
    class LengthRequired(SanicException):
        """
        **Status**: 411 Length Required
        """

        pass

    assert LengthRequired(message="test")

# Generated at 2022-06-14 07:11:24.333252
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    exception = Unauthorized("Auth required.", scheme="Basic", realm="Realm")
    assert exception.message == "Auth required."
    assert exception.status_code == 401
    assert exception.headers == {"WWW-Authenticate": "Basic realm=\"Realm\""}
    assert str(exception) == "Auth required."

# Generated at 2022-06-14 07:11:33.240852
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(202)
    class Accepted(SanicException):
        pass

    assert Accepted.status_code == 202
    assert Accepted().status_code == 202

    assert _sanic_exceptions[202] == Accepted

    @add_status_code(203)
    class NonAuthoritativeInformation(SanicException):
        pass

    assert NonAuthoritativeInformation.status_code == 203
    assert NonAuthoritativeInformation().status_code == 203

    assert _sanic_exceptions[203] == NonAuthoritativeInformation

# Generated at 2022-06-14 07:11:49.682828
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized('Auth required.', scheme='Basic', realm='Restricted Area')
    except Unauthorized as err:
        assert(str(err) == 'Auth required.')
        assert(err.status_code == 401)
        assert(err.message == 'Auth required.')
        assert(err.scheme == 'Basic')
        assert(err.realm == 'Restricted Area')

    try:
        raise Unauthorized('Auth required.', scheme='Digest', realm='Restricted Area', qop='auth, auth-int', algorithm='MD5', nonce='abcdef', opaque='zyxwvu')
    except Unauthorized as err:
        assert(str(err) == 'Auth required.')
        assert(err.status_code == 401)
        assert(err.message == 'Auth required.')

# Generated at 2022-06-14 07:11:57.825488
# Unit test for function add_status_code
def test_add_status_code():
    """ Test the function add_status_code """
    @add_status_code(456)
    class TestClass(SanicException):
        """ Test class for add_status_code """
        pass

    assert TestClass.status_code == 456
    assert TestClass is _sanic_exceptions[456]
    assert TestClass.quiet is False
    assert 456 in _sanic_exceptions

    @add_status_code(789, False)
    class TestClass2(SanicException):
        """ Test class for add_status_code """
        pass

    assert TestClass2.status_code == 789
    assert TestClass2 is _sanic_exceptions[789]
    assert TestClass2.quiet is None


# Generated at 2022-06-14 07:12:10.247624
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # failure 1
    try:
        raise Unauthorized("Auth required.")
    except Unauthorized as e:
        assert e.headers == {}

    # failure 2
    try:
        raise Unauthorized(message="Auth required.", status_code=401)
    except Unauthorized as e:
        assert e.headers == {}

    # failure 3
    try:
        raise Unauthorized("Auth required.", scheme="Basic")
    except Unauthorized as e:
        assert e.headers == {'WWW-Authenticate': 'Basic'}

    # failure 4
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as e:
        assert e.headers == {'WWW-Authenticate': 'Basic realm="Restricted Area"'}

    # failure 5

# Generated at 2022-06-14 07:12:23.317816
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    """
    Test the constructor of class Unauthorized.
    """

    # test for basic auth
    unauthorized = Unauthorized("Auth required.", scheme="Basic",
                                realm="Restricted Area")
    assert unauthorized.headers["WWW-Authenticate"] \
        == 'Basic realm="Restricted Area"'

    # test for digest auth
    unauthorized = Unauthorized("Auth required.", scheme="Digest",
                                realm="Restricted Area", qop="auth, auth-int",
                                algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    assert unauthorized.headers["WWW-Authenticate"] \
        == 'Digest algorithm="MD5", nonce="abcdef", opaque="zyxwvu", ' \
           'qop="auth, auth-int", realm="Restricted Area"'

    # test for bearer auth
    unauthorized

# Generated at 2022-06-14 07:12:27.387584
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    with pytest.raises(Unauthorized) as exc:
        raise Unauthorized("Auth required.",
                           scheme="Basic",
                           realm="Restricted Area")

    assert exc.value.headers['WWW-Authenticate'] == 'Basic realm="Restricted Area"'

# Generated at 2022-06-14 07:12:35.000023
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # The message is given as class docstring
    assert Unauthorized.__doc__ == "Unauthorized\n    **Status**: 401 Unauthorized\n    "

    # The message is given as parameter
    try:
        raise Unauthorized('Auth required.')
    except Unauthorized as e:
        assert e.message == 'Auth required.'
        assert e.status_code == 401

    # The status code is given as parameter
    try:
        raise Unauthorized('Auth required.', 401)
    except Unauthorized as e:
        assert e.message == 'Auth required.'
        assert e.status_code == 401

    # The status code is given as class attribute
    try:
        raise Unauthorized('Auth required.', 400)
    except Unauthorized as e:
        assert e.message == 'Auth required.'
        assert e.status_

# Generated at 2022-06-14 07:12:45.960965
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    message = "Auth required."
    scheme = "Digest"
    realm = "Restricted Area"
    qop = "auth, auth-int"
    algorithm = "MD5"
    nonce = "abcdef"
    opaque = "zyxwvu"
    args = [message, scheme, realm, qop, algorithm, nonce, opaque]
    try:
        raise Unauthorized(*args)
    except Unauthorized as e:
        assert (
            e.headers
            == {"WWW-Authenticate": 'Digest realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu"'}
        )

# Generated at 2022-06-14 07:13:01.662662
# Unit test for function add_status_code
def test_add_status_code():
    # Add a new exception type
    @add_status_code(404)
    class NotFoundTest(SanicException):
        """
        **Status**: 404 Not Found
        """
        pass

    assert issubclass(NotFoundTest, SanicException)
    assert NotFoundTest.status_code == 404
    assert NotFoundTest.quiet is True
    assert _sanic_exceptions[404] == NotFoundTest

    # Overwrite the status code for an existing exception type
    @add_status_code(404)
    class NotFoundTest(SanicException):
        """
        **Status**: 404 Not Found
        """
        pass

    assert issubclass(NotFoundTest, SanicException)
    assert NotFoundTest.status_code == 404
    assert NotFoundTest.quiet is True
    # Make sure it didn't overwrite

# Generated at 2022-06-14 07:13:09.780309
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(304)
    class MyStatusCode(SanicException):
        pass

    assert hasattr(MyStatusCode, "status_code")
    assert MyStatusCode.status_code == 304
    assert _sanic_exceptions[304] == MyStatusCode

    @add_status_code(304)
    class MyStatusCode(SanicException):
        pass

    assert _sanic_exceptions[304] == MyStatusCode

    @add_status_code(300)
    class MyStatusCode(SanicException):
        pass

    assert _sanic_exceptions[304] == MyStatusCode

# Generated at 2022-06-14 07:13:17.423485
# Unit test for function add_status_code
def test_add_status_code():
    class TestAddStatusCode(SanicException):
        pass
    new_exception = add_status_code(
        404)(TestAddStatusCode)('test message')
    assert new_exception.status_code == 404
    assert new_exception.message == 'test message'
    assert new_exception.quiet is True
    new_exception = add_status_code(
        404, quiet=False)(TestAddStatusCode)('test message')
    assert new_exception.status_code == 404
    assert new_exception.message == 'test message'
    assert new_exception.quiet is False
    new_exception = add_status_code(
        500)(TestAddStatusCode)('test message')
    assert new_exception.status_code == 500
    assert new_exception.message == 'test message'

# Generated at 2022-06-14 07:13:28.611171
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # test submodule class Unauthorized
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as err:
        assert err.status_code == 401
        assert err.headers["WWW-Authenticate"] == "Basic realm=\"Restricted Area\""
    try:
        # With a Digest auth-scheme, things are a bit more complicated:
        raise Unauthorized("Auth required.",
                           scheme="Digest",
                           realm="Restricted Area",
                           qop="auth, auth-int",
                           algorithm="MD5",
                           nonce="abcdef",
                           opaque="zyxwvu")
    except Unauthorized as err:
        assert err.status_code == 401

# Generated at 2022-06-14 07:13:33.733570
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    assert TestException not in _sanic_exceptions.values()
    add_status_code(200)(TestException)
    assert TestException in _sanic_exceptions.values()
    assert _sanic_exceptions[200] is TestException

# Generated at 2022-06-14 07:13:43.421039
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class CustomException(SanicException):
        pass

    @add_status_code(201, quiet=True)
    class CustomExceptionQuiet(SanicException):
        pass

    assert CustomException._sanic_status_code == 200
    assert CustomExceptionQuiet._sanic_status_code == 201
    assert CustomExceptionQuiet.quiet is True

    assert CustomException is _sanic_exceptions[200]
    assert CustomExceptionQuiet is _sanic_exceptions[201]


# Generated at 2022-06-14 07:13:47.144105
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestCls(SanicException):
        pass


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:14:01.177641
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # With a Basic auth-scheme, realm MUST be present:
    exc = Unauthorized("Auth required.",
                       scheme="Basic",
                       realm="Restricted Area")
    assert exc.headers == {"WWW-Authenticate": 'Basic realm="Restricted Area"'}

    # With a Digest auth-scheme, things are a bit more complicated:
    exc = Unauthorized("Auth required.",
                       scheme="Digest",
                       realm="Restricted Area",
                       qop="auth, auth-int",
                       algorithm="MD5",
                       nonce="abcdef",
                       opaque="zyxwvu")

# Generated at 2022-06-14 07:14:13.575980
# Unit test for function add_status_code
def test_add_status_code():
    # add new status code 901
    @add_status_code(901)
    class TestException(SanicException):
        pass

    assert issubclass(_sanic_exceptions[901], SanicException)
    assert _sanic_exceptions[901].status_code == 901

    # add new status code 902, which is the same as 901
    @add_status_code(902)
    class TestException_2(SanicException):
        pass

    assert issubclass(_sanic_exceptions[902], SanicException)
    assert _sanic_exceptions[902].status_code == 902
    assert _sanic_exceptions[902] is not _sanic_exceptions[901]

    # add new status code 903, which is the same as 901

# Generated at 2022-06-14 07:14:17.049211
# Unit test for function add_status_code
def test_add_status_code():
    code = 404
    @add_status_code(code)
    class NotFound(SanicException):
        pass

    assert _sanic_exceptions[code] == NotFound

# Generated at 2022-06-14 07:14:23.198777
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestException(Exception):
        pass

    _sanic_exceptions[404].__name__ == 'TestException'
    isinstance(_sanic_exceptions[404](), TestException)



# Generated at 2022-06-14 07:14:27.978375
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    test_exception = add_status_code(400)(TestException)

    assert test_exception.status_code == 400
    assert test_exception.quiet is True



# Generated at 2022-06-14 07:14:33.165733
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(999)
    class MyException(SanicException):
        pass
    assert _sanic_exceptions.get(999).__name__ == "MyException"

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:14:44.578144
# Unit test for function add_status_code
def test_add_status_code():
    # Helper function for test
    def _add_status_code(code, quiet=None):
        def class_decorator(cls):
            cls.status_code = code
            if quiet or quiet is None and code != 500:
                cls.quiet = True
            _sanic_exceptions[code] = cls
            return cls
        return class_decorator

    @_add_status_code(400)
    class InvalidUsage(SanicException):
        """
        **Status**: 400 Bad Request
        """
        pass

    assert InvalidUsage.status_code == 400
    assert InvalidUsage.quiet == True
    assert _sanic_exceptions[400] == InvalidUsage


# Generated at 2022-06-14 07:14:48.515425
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 403
    assert _sanic_exceptions[403] == TestException

# Generated at 2022-06-14 07:14:56.040446
# Unit test for function add_status_code
def test_add_status_code():
    '''
    Test suite for add_status_code
    '''
    status_code = 404
    s_code = add_status_code(status_code)
    def test_decorator(cls):
        s_decorator = s_code(cls)
        return s_decorator
    test_decorator(NotFound)
    assert status_code == NotFound.status_code

# Generated at 2022-06-14 07:15:00.487971
# Unit test for function add_status_code
def test_add_status_code():
    # Arrange
    class NotFound(SanicException):
        pass

    # Act
    add_status_code(404)

    # Assert
    assert _sanic_exceptions[404] == NotFound


# Generated at 2022-06-14 07:15:06.652812
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class test_100(SanicException):
        pass

    @add_status_code(200)
    class test_200(SanicException):
        pass

    assert _sanic_exceptions[100] == test_100
    assert _sanic_exceptions[200] == test_200

# Generated at 2022-06-14 07:15:13.658086
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class A(SanicException):
        pass
    assert A.status_code == 404
    assert A.quiet == True

    class A(SanicException):
        pass

    @add_status_code(404, quiet=False)
    def foo():
        pass
    assert foo.status_code == 404
    assert foo.quiet == False

# Generated at 2022-06-14 07:15:18.168103
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(300)
    class MySanicException(SanicException):
        pass
    # All exceptions class should have a status code
    assert MySanicException.status_code == 300
    # All exceptions class should have a status code in the SanicException dict
    assert _sanic_exceptions[300] == MySanicException

# Generated at 2022-06-14 07:15:27.530044
# Unit test for function add_status_code
def test_add_status_code():
    """
    test for function add_status_code
    """
    @add_status_code(302)
    class TestException(SanicException):
        pass

    try:
        raise TestException("test")
    except TestException as exception:
        assert exception.status_code == 302
        assert exception.quiet is False

# Generated at 2022-06-14 07:15:30.971568
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class TestException(Exception):
        pass
    assert _sanic_exceptions[201] == TestException


# Generated at 2022-06-14 07:15:37.460194
# Unit test for function add_status_code
def test_add_status_code():
    """
    Testing function add_status_code()
    """
    @add_status_code(status_code=400)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 400
    assert TestException.quiet == False
    assert _sanic_exceptions[400] == TestException

    @add_status_code(status_code=404)
    class TestException2(SanicException):
        pass
    assert TestException2.status_code == 404
    assert TestException2.quiet == True
    assert _sanic_exceptions[404] == TestException2

# Generated at 2022-06-14 07:15:46.750054
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(405)
    class TestingException(SanicException):
        pass

    assert TestingException.status_code == 405
    assert _sanic_exceptions[405] == TestingException

    @add_status_code(410)
    class TestingExceptionWithQuiet(SanicException):
        pass

    assert TestingExceptionWithQuiet.status_code == 410
    assert _sanic_exceptions[410] == TestingExceptionWithQuiet
    assert TestingExceptionWithQuiet.quiet is True

# Generated at 2022-06-14 07:15:49.924553
# Unit test for function add_status_code
def test_add_status_code():
    class test404(SanicException):
        pass

    assert _sanic_exceptions[404] == test404

# Unit tests for class SanicException

# Generated at 2022-06-14 07:15:56.733758
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class A(SanicException):
        pass
    assert A().status_code == 200
    assert _sanic_exceptions[200] is A

    @add_status_code(300)
    class B(SanicException):
        pass
    assert B().status_code == 300
    assert _sanic_exceptions[300] is B

    # quiet=None/False/True with None meaning choose by status
    assert A().quiet is True
    assert B().quiet is False

    # quiet=False should override automatic choice
    @add_status_code(200, False)
    class C(SanicException):
        pass
    assert C().quiet is False

    # quiet=True should override any other values

# Generated at 2022-06-14 07:15:59.284287
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(code=440)
    assert _sanic_exceptions.get(440).status_code == 440

# Generated at 2022-06-14 07:16:06.825939
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(405)
    class _(SanicException):
        pass

    assert type(_sanic_exceptions[405]) == _
    assert _().status_code == 405
    assert _().message == "405: Method Not Allowed"


if __name__ == "__main__":
    # Unit test for function add_status_code
    test_add_status_code()

# Generated at 2022-06-14 07:16:10.197797
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(code=1001)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[1001] == TestException



# Generated at 2022-06-14 07:16:23.390908
# Unit test for function add_status_code
def test_add_status_code():
    # without quiet=True
    exc, status_code = InternServerError(), 500
    assert isinstance(exc, SanicException)
    assert exc.status_code == status_code
    assert exc.quiet == False

    # with quiet=False
    exc, status_code = InternServerError(quiet=False), 500
    assert isinstance(exc, SanicException)
    assert exc.status_code == status_code
    assert exc.quiet == False

    # with quiet=True
    exc, status_code = InternServerError(quiet=True), 500
    assert isinstance(exc, SanicException)
    assert exc.status_code == status_code
    assert exc.quiet == True

    # with quiet=None and status_code = 500
    exc, status_code = InternServerError(quiet=None), 500

# Generated at 2022-06-14 07:16:31.365597
# Unit test for function add_status_code
def test_add_status_code():
    assert _sanic_exceptions[404] is NotFound

# Generated at 2022-06-14 07:16:41.453802
# Unit test for function add_status_code
def test_add_status_code():
    # Test with standard exception, using default quiet
    add_status_code(404)
    assert _sanic_exceptions[404].quiet

    # Test with standard exception, using quiet=True
    add_status_code(500, quiet=True)
    assert _sanic_exceptions[500].quiet

    # Test with standard exception, using quiet=False
    add_status_code(500, quiet=False)
    assert not _sanic_exceptions[500].quiet

    # Test with custom exception, using default quiet
    @add_status_code(404)
    class MyException(Exception):
        pass
    assert _sanic_exceptions[404].quiet

    # Test with custom exception, using quiet=True
    @add_status_code(500, quiet=True)
    class MyException(Exception):
        pass

# Generated at 2022-06-14 07:16:46.598739
# Unit test for function add_status_code
def test_add_status_code():

    @add_status_code(400)
    class BadRequest(SanicException):
        def __init__(self, message):
            super().__init__(message, status_code=400)

    assert _sanic_exceptions[400] == BadRequest
    assert _sanic_exceptions[400](message="test").status_code == 400
    assert _sanic_exceptions[400](message="test").message == "test"



# Generated at 2022-06-14 07:16:54.341489
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(Exception):
        pass
    assert 404 not in _sanic_exceptions
    assert (add_status_code(404)(TestException) == TestException)
    assert 404 in _sanic_exceptions
    assert _sanic_exceptions[404] == TestException
    assert _sanic_exceptions[404]().status_code == 404


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:17:06.902196
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(405)
    class TestException(SanicException):
        """
        **Status**: 405 Method Not Allowed
        """

    @add_status_code(408)
    class TestException1(SanicException):
        """
        **Status**: 408 Request Timeout
        """

    @add_status_code(413, True)
    class TestException2(SanicException):
        """
        **Status**: 413 Request Entity Too Large
        """

    @add_status_code(902)
    class TestException3(SanicException):
        """
        **Status**: 902 Server Not Configured
        """

    assert _sanic_exceptions[405].status_code == 405
    assert _sanic_exceptions[408].status_code == 408
    assert _sanic_ex

# Generated at 2022-06-14 07:17:19.931530
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test if the decorator add_status_code is working. Test if status_code and
    quiet are set correctly.
    """
    @add_status_code(405)
    class Test1(SanicException):
        pass
    @add_status_code(406, True)
    class Test2(SanicException):
        pass
    @add_status_code(407, False)
    class Test3(SanicException):
        pass
    @add_status_code(408)
    class Test4(SanicException):
        pass

    assert Test1.status_code == 405
    assert Test1.quiet is None
    assert Test2.status_code == 406
    assert Test2.quiet is True
    assert Test3.status_code == 407
    assert Test3.quiet is False

# Generated at 2022-06-14 07:17:24.992684
# Unit test for function add_status_code
def test_add_status_code():
    code = 200

    def class_decorator(cls):
        cls.status_code = code
        _sanic_exceptions[code] = cls
        return cls

    class_decorator(NotFound)

    assert _sanic_exceptions[200] == NotFound

# Generated at 2022-06-14 07:17:30.528163
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Test(SanicException):
        pass
    assert Test().status_code == 200
    assert Test().quiet == True

    @add_status_code(500)
    class Test(SanicException):
        pass
    assert Test().status_code == 500
    assert Test().quiet == False

    @add_status_code(500, quiet=True)
    class Test(SanicException):
        pass
    assert Test().status_code == 500
    assert Test().quiet == True

# Generated at 2022-06-14 07:17:38.769912
# Unit test for function add_status_code
def test_add_status_code():
    class NewException(SanicException):
        pass

    @add_status_code(599)
    class NewException2(SanicException):
        pass

    assert issubclass(NewException, SanicException)
    assert issubclass(NewException2, SanicException)

    assert NewException.status_code is None
    assert NewException2.status_code == 599

    assert _sanic_exceptions[599] == NewException2

# Generated at 2022-06-14 07:17:41.164157
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(410)
    class Gone(SanicException):
        pass
    assert Gone.status_code == 410



# Generated at 2022-06-14 07:18:00.143549
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(202)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 202
    assert _sanic_exceptions[202] == TestException
    assert TestException().status_code == 202



# Generated at 2022-06-14 07:18:12.125074
# Unit test for function add_status_code
def test_add_status_code():
    def class_decorator(cls):
        cls.status_code = code
        if quiet or quiet is None and code != 500:
            cls.quiet = True
        _sanic_exceptions[code] = cls
        return cls

    code = 200
    quiet = None
    @add_status_code(code, quiet)
    class TestException(Exception): 
        def __init__(self, message, status_code=None, quiet=None): 
            super().__init__(message) 
            if status_code is not None: 
                self.status_code = status_code
            if quiet or quiet is None and status_code not in (None, 500): 
                self.quiet = True


    assert _sanic_exceptions[code] is TestException
    assert _sanic_ex

# Generated at 2022-06-14 07:18:21.355583
# Unit test for function add_status_code
def test_add_status_code():
    # Test for add_status_code decorator with default parameters
    @add_status_code(408)
    class TestClass(SanicException):
        """
        **Status**: 408 Timeout
        """
        pass
    # Test for class TestClass attributes, should be 408 and False
    assert TestClass.status_code == 408
    assert TestClass.quiet is False
    # Test for add_status_code decorator with custom parameters
    @add_status_code(418,True)
    class TestClass2(SanicException):
        """
        **Status**: 418 I'm a teapot
        """
        pass
    # Test for class TestClass2 attributes, should be 418 and True
    assert TestClass2.status_code == 418
    assert TestClass2.quiet is True

# Generated at 2022-06-14 07:18:33.444279
# Unit test for function add_status_code
def test_add_status_code():
    # STATUS CODE 404
    @add_status_code(404)
    class Test404(SanicException):
        pass
    assert Test404.status_code == 404
    # STATUS CODE 400
    @add_status_code(400)
    class Test400(SanicException):
        pass
    assert Test400.status_code == 400
    # STATUS CODE 405
    @add_status_code(405)
    class Test405(SanicException):
        pass
    assert Test405.status_code == 405
    # STATUS CODE 500
    @add_status_code(500)
    class Test500(SanicException):
        pass
    assert Test500.status_code == 500
    # STATUS CODE 503
    @add_status_code(503)
    class Test503(SanicException):
        pass


# Generated at 2022-06-14 07:18:47.630695
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyException(SanicException):
        pass

    assert _sanic_exceptions[400] == MyException
    assert MyException.status_code == 400

    @add_status_code(500)
    class MyException2(SanicException):
        pass

    assert _sanic_exceptions[500] == MyException2
    assert MyException2.status_code == 500
    assert not getattr(MyException2, 'quiet', False)

    @add_status_code(404, quiet=True)
    class MyException3(SanicException):
        pass

    assert _sanic_exceptions[404] == MyException3
    assert MyException3.status_code == 404
    assert getattr(MyException3, 'quiet', False)

# Generated at 2022-06-14 07:18:56.670596
# Unit test for function add_status_code

# Generated at 2022-06-14 07:19:04.611794
# Unit test for function add_status_code
def test_add_status_code():
    # Test SanicException functionality
    with pytest.raises(SanicException) as e:
        raise SanicException("test status 501")
    assert e.value.status_code == 501

    # Test decorator functionality of add_status_code
    @add_status_code(502)
    class TestException(SanicException):
        pass
    with pytest.raises(TestException) as e:
        raise TestException("test status 502")
    assert e.value.status_code == 502

# Generated at 2022-06-14 07:19:09.975933
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class MyException(SanicException):
        pass

    class MyException2(SanicException):
        pass

    try:
        raise MyException("message")
    except SanicException as ex:
        assert ex.status_code == 500

    try:
        raise MyException2("message")
    except SanicException as ex:
        assert ex.status_code == 500

# Generated at 2022-06-14 07:19:17.440451
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class _TestException(SanicException): # pylint: disable=unused-variable
        pass

    assert _TestException.status_code == 400

    @add_status_code(401)
    class _TestException(SanicException): # pylint: disable=unused-variable
        pass

    assert _TestException.status_code == 401



# Generated at 2022-06-14 07:19:21.341348
# Unit test for function add_status_code
def test_add_status_code():

    code = 420
    class MyClass(SanicException):
        pass

    assert code not in _sanic_exceptions

    @add_status_code(code)
    class EnhancedClass(MyClass):
        pass

    assert code in _sanic_exceptions

# Generated at 2022-06-14 07:19:53.674474
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    add_status_code(404)(MyException)
    assert issubclass(MyException, NotFound)

# Generated at 2022-06-14 07:20:02.138493
# Unit test for function add_status_code
def test_add_status_code():
    """
    Tests the add_status_code
    """

    @add_status_code(100)
    class X100(SanicException):
        pass

    assert _sanic_exceptions[100] == X100
    assert X100.status_code == 100
    assert not X100.quiet

    @add_status_code(200)
    class X200(SanicException):
        pass

    assert _sanic_exceptions[200] == X200
    assert X200.status_code == 200
    assert X200.quiet

    @add_status_code(300, quiet=False)
    class X300(SanicException):
        pass

    assert _sanic_exceptions[300] == X300
    assert X300.status_code == 300
    assert not X300.quiet


# Generated at 2022-06-14 07:20:13.354854
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

# Generated at 2022-06-14 07:20:20.856553
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    status_code_test = 200
    @add_status_code(status_code_test)
    class TestException(SanicException):
        pass

    assert TestException.status_code is status_code_test
    assert TestException.quiet is True
    assert TestException(message="Test Exception with status code {status_code}".format(status_code=TestException.status_code)).status_code is status_code_test


# Generated at 2022-06-14 07:20:30.565907
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test for function add_status_code
    """

    # Test for class_decorator with quiet=True
    @add_status_code(401, quiet=True)
    class SomeException(NotFound):
        pass
    assert SomeException.status_code == 401
    assert SomeException.quiet == True
    assert 401 in _sanic_exceptions
    assert isinstance(_sanic_exceptions[401], Exception)

    # Test for class_decorator with quiet=False
    @add_status_code(402, quiet=False)
    class SomeException(NotFound):
        pass
    assert SomeException.status_code == 402
    assert SomeException.quiet == False
    assert 402 in _sanic_exceptions
    assert isinstance(_sanic_exceptions[402], Exception)

    # Test for class_dec

# Generated at 2022-06-14 07:20:32.779495
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class IAMATEAPOT(SanicException):
        pass

    assert '418' in _sanic_exceptions
    assert isinstance(_sanic_exceptions['418'](), IAMATEAPOT)



# Generated at 2022-06-14 07:20:40.185501
# Unit test for function add_status_code
def test_add_status_code():
    # Tests that add_status_code correctly adds a class to _sanic_exceptions dictionary
    # and that it has the correct status code and quiet status
    class test_class(SanicException):
        def __init__(self, message):
            self.message = message
    add_status_code(test_class, 404)
    assert _sanic_exceptions[404].status_code == 404
    assert _sanic_exceptions[404].quiet == True
    add_status_code(test_class, 500)
    assert _sanic_exceptions[500].status_code == 500
    assert _sanic_exceptions[500].quiet == False
    add_status_code(test_class, 500, False)
    assert _sanic_exceptions[500].status_code == 500

# Generated at 2022-06-14 07:20:43.284451
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(400)
    assert add_status_code(500, quiet=True)
    assert add_status_code(500, quiet=False)

# Generated at 2022-06-14 07:20:50.255678
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class MyException(SanicException):
        pass
    assert _sanic_exceptions[100].status_code == 100
    assert _sanic_exceptions[100].__name__ == "MyException"
    assert _sanic_exceptions[100]().status_code == 100


# Generated at 2022-06-14 07:20:57.107381
# Unit test for function add_status_code
def test_add_status_code():
    message = 'Test custom exception'
    status_code = 406
    custom_exception = add_status_code(406)(SanicException)
    assert custom_exception.status_code == status_code
    assert custom_exception(message).message == message
    assert custom_exception(message).status_code == status_code
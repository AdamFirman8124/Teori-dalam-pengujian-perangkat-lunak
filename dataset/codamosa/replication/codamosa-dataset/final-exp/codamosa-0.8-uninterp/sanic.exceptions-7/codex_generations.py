

# Generated at 2022-06-14 07:11:26.655356
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as e:
        assert e.status_code == 401
        assert e.headers['WWW-Authenticate'] == "Basic realm=\"Restricted Area\""

    try:
        raise Unauthorized("Auth required.", scheme="Digest", realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    except Unauthorized as e:
        assert e.status_code == 401
        assert e.headers['WWW-Authenticate'] == "Digest realm=\"Restricted Area\", qop=\"auth, auth-int\", algorithm=MD5, nonce=\"abcdef\", opaque=\"zyxwvu\""


# Generated at 2022-06-14 07:11:31.799302
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(405)
    class Foo(SanicException):
        pass

    assert _sanic_exceptions[405] == Foo
    assert Foo.status_code == 405
    assert Foo.quiet == True
    assert Foo.__name__ == "Foo"

# Generated at 2022-06-14 07:11:37.648616
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class DemoException(SanicException):
        pass

    demo_exception = DemoException(message="Test Message.", status_code=200)
    assert demo_exception.status_code == 200
    assert demo_exception.message == "Test Message."

# Generated at 2022-06-14 07:11:40.901154
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class A(SanicException):
        pass

    assert A.status_code == 200


# Generated at 2022-06-14 07:11:45.781259
# Unit test for function add_status_code
def test_add_status_code():
    # Given
    code = 400

    @add_status_code(code, False)
    class Bar(SanicException):
        pass

    # When
    bar = Bar("message", status_code=code)

    # Then
    assert bar.status_code == code
    assert bar.quiet == False
    assert bar.message == "message"



# Generated at 2022-06-14 07:11:59.393197
# Unit test for function add_status_code

# Generated at 2022-06-14 07:12:07.505507
# Unit test for function add_status_code
def test_add_status_code():
    # add status_code=400, quiet=None
    @add_status_code(400, quiet=None)
    class NotFound(SanicException): 
        pass
    assert _sanic_exceptions[400].quiet == False

    # add status_code=404, quiet=None
    @add_status_code(404, quiet=None)
    class NotFound(SanicException): 
        pass
    assert _sanic_exceptions[404].quiet == True


# Generated at 2022-06-14 07:12:21.645952
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(300)
    class mySanicException(SanicException): pass

    assert mySanicException('').status_code == 300
    assert isinstance((_sanic_exceptions[300]), mySanicException)


if __name__ == "__main__":
    import unittest

    # Unit test for function add_status_code
    class UTtest1(unittest.TestCase):
        def test_add_status_code(self):
            @add_status_code(300)
            class mySanicException(SanicException): pass

            self.assertEqual(mySanicException('').status_code, 300)
            self.assertIsInstance((_sanic_exceptions[300]), mySanicException)


    unittest.main()

# Generated at 2022-06-14 07:12:27.838714
# Unit test for function add_status_code
def test_add_status_code():
    assert(InvalidUsage.status_code == 400)
    assert(NotFound.status_code == 404)
    assert(ServerError.status_code == 500)
    assert(ServerError.quiet == False)
    assert(ServiceUnavailable.status_code == 503)
    assert(ServiceUnavailable.quiet == True)

test_add_status_code()

# Generated at 2022-06-14 07:12:39.548971
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    def __init__(self, message, status_code=None, scheme=None, **kwargs):
        super().__init__(message, status_code)

        # if auth-scheme is specified, set "WWW-Authenticate" header
        if scheme is not None:
            values = ['{!s}="{!s}"'.format(k, v) for k, v in kwargs.items()]
            challenge = ", ".join(values)

            self.headers = {
                "WWW-Authenticate": f"{scheme} {challenge}".rstrip()
            }

    assert message == "Auth required."  
    assert status_code == 401
    assert scheme == "Basic"
    assert scheme == "Digest"
    assert scheme == "Bearer"

# Generated at 2022-06-14 07:12:51.624746
# Unit test for function add_status_code
def test_add_status_code():
    assert(add_status_code(404))
    assert(add_status_code(400))
    assert(add_status_code(405))
    assert(add_status_code(500))
    assert(add_status_code(503))
    assert(add_status_code(408))
    assert(add_status_code(413))
    assert(add_status_code(416))
    assert(add_status_code(417))
    assert(add_status_code(403))
    assert(add_status_code(401))


# Generated at 2022-06-14 07:13:04.261778
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # Normal case
    try:
        raise Unauthorized("Auth required.", scheme="Bearer")
    except Unauthorized as exc:
        assert exc.status_code == 401
        assert exc.scheme == "Bearer"
        assert "WWW-Authenticate" not in exc.headers

    try:
        raise Unauthorized("Auth required.",
                           scheme="Bearer",
                           realm="Restricted Area")
    except Unauthorized as exc:
        assert exc.status_code == 401
        assert exc.scheme == "Bearer"
        assert exc.headers["WWW-Authenticate"] == 'Bearer realm="Restricted Area"'


# Generated at 2022-06-14 07:13:11.361215
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required", scheme="Basic", realm="Restricted Area")
    except Unauthorized as err:
        assert(err.headers == {'WWW-Authenticate': 'Basic realm="Restricted Area"'})
        assert(err.scheme == "Basic")
        assert(err.kwargs == {"realm": "Restricted Area"})
    try:
        raise Unauthorized("Auth required", scheme="Digest", realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    except Unauthorized as err:
        assert(err.headers == {'WWW-Authenticate': 'Digest realm="Restricted Area", algorithm="MD5", qop="auth, auth-int", nonce="abcdef", opaque="zyxwvu"'})


# Generated at 2022-06-14 07:13:22.383022
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # Basic auth-scheme, realm MUST be present
    try:
        raise Unauthorized("Auth required.", scheme="Basic")
    except Unauthorized as e:
        assert e.scheme == "Basic"
        assert e.realm == "Restricted Area"

    # With a Basic auth-scheme, realm MUST be present
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as e:
        assert e.scheme == "Basic"
        assert e.realm == "Restricted Area"

    # With a Digest auth-scheme

# Generated at 2022-06-14 07:13:28.970176
# Unit test for function add_status_code
def test_add_status_code():
    # Test without quiet
    sanic_exception = _sanic_exceptions.get(404, SanicException)
    assert sanic_exception is NotFound
    # Test with quiet
    sanic_exception = _sanic_exceptions.get(400, SanicException)
    assert sanic_exception is InvalidUsage
    assert sanic_exception.quiet is True


# Generated at 2022-06-14 07:13:40.200987
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # with a Basic scheme, realm MUST be present
    with pytest.raises(Unauthorized):
        raise Unauthorized("Auth required.",
                           scheme="Basic")

    # with a Basic scheme, realm must be present
    raise Unauthorized("Auth required.",
                       scheme="Basic",
                       realm="Restricted Area")

    # with a Digest scheme, things are a bit more complicated
    raise Unauthorized("Auth required.",
                       scheme="Digest",
                       realm="Restricted Area",
                       qop="auth, auth-int",
                       algorithm="MD5",
                       nonce="abcdef",
                       opaque="zyxwvu")

    # with a Bearer scheme, realm is optional so you can write
    raise Unauthorized("Auth required.", scheme="Bearer")

    # or, if you want to specify the realm

# Generated at 2022-06-14 07:13:42.914182
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    """
    Test constructor of class Unauthorized.
    """
    obj = Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    assert obj.headers == {
        "WWW-Authenticate": 'Basic realm="Restricted Area"'
    }

# Generated at 2022-06-14 07:13:52.754406
# Unit test for function add_status_code
def test_add_status_code():
    def decorator(cls):
        cls.status_code=code
        print("decorator")
        print(cls.status_code)
        return cls

    def class_decorator(cls):
        cls.status_code = code
        if quiet or quiet is None and code != 500:
            cls.quiet = True
        _sanic_exceptions[code] = cls
        print("class_decorator")
        print(cls.status_code)
        return cls

    code=500
    quiet=None
    decorator(NotFound)
    class_decorator(NotFound)

# Generated at 2022-06-14 07:14:02.659361
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    """
    This is a testcase.
    """

    # Testcase 1
    try:
        message1 = "testing Auth required."
        status_code1 = 401
        scheme1 = "Basic"
        realm1 = "Restricted Area"
        raise Unauthorized(message1,
                           scheme1,
                           realm1)
    except Unauthorized as e:
        assert e.message == message1
        assert e.headers == {"WWW-Authenticate": 'Basic realm="Restricted Area"'}

    # Testcase 2
    try:
        message2 = "testing Auth required."
        status_code2 = 401
        scheme2 = "Basic"
        raise Unauthorized(message2,
                           scheme2)
    except Unauthorized as e:
        assert e.message == message2

# Generated at 2022-06-14 07:14:07.064757
# Unit test for function add_status_code
def test_add_status_code():
    import pytest
    exception_type = add_status_code(404)(SanicException)

    with pytest.raises(NotFound):
        raise NotFound('Test')
    with pytest.raises(exception_type):
        raise exception_type('Test')

# Generated at 2022-06-14 07:14:11.330141
# Unit test for function add_status_code
def test_add_status_code():
    # Test with a custom exception class
    @add_status_code(500)
    class InternalServerError(SanicException):
        pass

    exc = InternalServerError()
    assert exc.status_code == 500
    assert str(exc) == "InternalServerError"

# Generated at 2022-06-14 07:14:17.474870
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class CustomException(SanicException):
        pass

    assert isinstance(_sanic_exceptions[500], CustomException)
    assert _sanic_exceptions[500].status_code == 500

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:14:20.836347
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class NewException(SanicException):
        pass

    assert NewException.status_code == 100



# Generated at 2022-06-14 07:14:28.028234
# Unit test for function add_status_code
def test_add_status_code():
    class TestClass1(SanicException):
        pass
    class TestClass2(SanicException):
        pass
    add_status_code(404)(TestClass1)
    add_status_code(404, quiet=True)(TestClass2)
    assert _sanic_exceptions[404](message='Test') == TestClass1('Test', 404, False)
    assert _sanic_exceptions[404](message='Test') == TestClass2('Test', 404, True)

# Generated at 2022-06-14 07:14:34.463138
# Unit test for function add_status_code
def test_add_status_code():
    # Case 1
    @add_status_code(404)
    class NotFound(SanicException):
        """
        **Status**: 404 Not Found
        """
        pass

    assert NotFound.status_code == 404
    assert NotFound.quiet == True

    # Case 2
    @add_status_code(400)
    class InvalidUsage(SanicException):
        """
        **Status**: 400 Bad Request
        """
        pass
    assert InvalidUsage.status_code == 400
    assert InvalidUsage.quiet == True

    # Case 3
    @add_status_code(405)
    class MethodNotSupported(SanicException):
        """
        **Status**: 405 Method Not Allowed
        """
        def __init__(self, message, method, allowed_methods):
            super().__init__(message)

# Generated at 2022-06-14 07:14:37.486480
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class Error500(SanicException):
        pass
    assert _sanic_exceptions[500] == Error500

# Generated at 2022-06-14 07:14:38.730535
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(0)

# Generated at 2022-06-14 07:14:46.982086
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(412)
    class _412(SanicException):
        pass

    assert _sanic_exceptions[412] == _412

    assert _sanic_exceptions[404] == NotFound
    assert _sanic_exceptions[400] == InvalidUsage
    assert _sanic_exceptions[405] == MethodNotSupported
    assert _sanic_exceptions[500] == ServerError
    assert _sanic_exceptions[503] == ServiceUnavailable
    assert _sanic_exceptions[413] == PayloadTooLarge
    assert _sanic_exceptions[408] == RequestTimeout
    assert _sanic_exceptions[416] == ContentRangeError
    assert _sanic_exceptions[417] == HeaderExpectationFailed
    assert _sanic_exceptions[403] == Forbidden

# Generated at 2022-06-14 07:14:59.088287
# Unit test for function add_status_code
def test_add_status_code():
    with pytest.raises(AttributeError):
        class TempCode(SanicException):
            pass

    add_status_code(202)(TempCode)
    temp_code = TempCode("Just a test")
    assert hasattr(temp_code, "status_code")
    assert temp_code.status_code == 202

    @add_status_code(101)
    class TempCode2(SanicException):
        pass

    assert TempCode2.status_code == 101
    assert TempCode2.quiet is True

    @add_status_code(500, quiet=False)
    class TempCode3(SanicException):
        pass

    assert TempCode3.status_code == 500
    assert TempCode3.quiet is False

# Generated at 2022-06-14 07:15:11.079436
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class NotFound(SanicException):
        """
        **Status**: 404 Not Found
        """
        pass

    assert(NotFound.status_code == 404)
    assert(NotFound.quiet)

    @add_status_code(400)
    class InvalidUsage(SanicException):
        """
        **Status**: 400 Bad Request
        """
        pass

    assert(InvalidUsage.status_code == 400)
    assert(InvalidUsage.quiet)

    @add_status_code(500)
    class ServerError(SanicException):
        """
        **Status**: 500 Internal Server Error
        """
        pass

    assert(ServerError.status_code == 500)
    assert(not ServerError.quiet)


# Generated at 2022-06-14 07:15:21.915428
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class MyTestException200(SanicException):
        pass

    assert MyTestException200.status_code == 200
    assert _sanic_exceptions[200] is MyTestException200
    assert _sanic_exceptions[200]().status_code == 200
    assert MyTestException200(quiet=True).quiet is True
    assert MyTestException200(quiet=False).quiet is False
    assert MyTestException200().quiet is False

    @add_status_code(400)
    class MyTestException400(SanicException):
        pass

    assert MyTestException400.status_code == 400
    assert _sanic_exceptions[400] is MyTestException400
    assert _sanic_exceptions[400]().status_code == 400

# Generated at 2022-06-14 07:15:32.998219
# Unit test for function add_status_code
def test_add_status_code():
    new_status_code = 402
    # Add new status code for Payload Required
    @add_status_code(new_status_code, quiet=True)
    class PayloadRequired(SanicException):
        pass

    # Check after adding status code
    assert _sanic_exceptions[new_status_code].__name__ == "PayloadRequired"
    assert _sanic_exceptions[new_status_code].status_code == new_status_code

    # Check for status_code is not there
    status_code = 405
    assert _sanic_exceptions[status_code].__name__ == "MethodNotSupported"
    assert _sanic_exceptions[status_code].status_code == status_code

    # Check for status_code is there
    status_code = 404

# Generated at 2022-06-14 07:15:35.892245
# Unit test for function add_status_code
def test_add_status_code():
    try:
        add_status_code(1,'Test1')
        add_status_code(2,'Test2')
        add_status_code(3,'Test3')
    except Exception as e:
        raise e


# Generated at 2022-06-14 07:15:45.917252
# Unit test for function add_status_code
def test_add_status_code():
    class SanicException1(SanicException):
        pass

    add_status_code(404)(SanicException1)
    assert _sanic_exceptions[404] == SanicException1
    assert _sanic_exceptions[404].quiet == True

    class SanicException2(SanicException):
        pass

    add_status_code(500)(SanicException2)
    assert _sanic_exceptions[500] == SanicException2
    assert _sanic_exceptions[500].quiet == False

# Generated at 2022-06-14 07:15:52.624251
# Unit test for function add_status_code
def test_add_status_code():
    """
    Add a status code to the dictionary of exceptions.

    :return:
    """
    # Create a decorator
    decorator = add_status_code(status_code=599)

    @decorator
    class Something(SanicException):
        pass

    assert Something.status_code == 599
    assert Something.quiet is None
    assert _sanic_exceptions[599] == Something


# Generated at 2022-06-14 07:16:07.018258
# Unit test for function add_status_code
def test_add_status_code():
    class StatusCodeTest(SanicException):
        pass

    test_code = 300
    assert test_code not in _sanic_exceptions

    add_status_code(test_code)(StatusCodeTest)
    assert test_code in _sanic_exceptions

    # Assert that the SanicException is a subclass of the given status_code
    # exception
    assert issubclass(SanicException, _sanic_exceptions[test_code])

    # Test that the status_code exception is a subclass of SanicException
    exc = _sanic_exceptions[test_code]()
    assert isinstance(exc, SanicException)

    # Test that the status_code exception has the correct status_code set
    assert exc.status_code == test_code

    # Test that the SanicException has the correct status_code set


# Generated at 2022-06-14 07:16:09.372788
# Unit test for function add_status_code
def test_add_status_code():
    """
    **Status**: 100
    """
    pass

test_add_status_code()

# Generated at 2022-06-14 07:16:14.022336
# Unit test for function add_status_code
def test_add_status_code():
    def class_decorator(cls):
        cls.status_code = 200
        return cls

    add_status_code(200, quiet=None)(class_decorator)
    assert _sanic_exceptions[200] == class_decorator

# Generated at 2022-06-14 07:16:24.592106
# Unit test for function add_status_code
def test_add_status_code():
    class TestClass(SanicException):
        pass

    assert 400 not in _sanic_exceptions

    # Check that we add a status code
    add_status_code(400)(TestClass)
    assert isinstance(_sanic_exceptions[400], TestClass)

    # Check that we don't add a status code
    with pytest.raises(ValueError):
        add_status_code(400)(TestClass)

    # Check that we remove a status code and don't add it again
    _sanic_exceptions.pop(400)
    add_status_code(400)(TestClass)
    assert isinstance(_sanic_exceptions[400], TestClass)



# Generated at 2022-06-14 07:16:28.158798
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class BadRequest(SanicException):
        pass

    assert BadRequest(message='').status_code == 400

# Generated at 2022-06-14 07:16:40.544556
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(666)
    class CustomException(Exception):
        pass

    assert 666 in _sanic_exceptions
    assert _sanic_exceptions[666] is CustomException


# Generated at 2022-06-14 07:16:50.585670
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class TestCode(SanicException):
        pass

    assert _sanic_exceptions[100] == TestCode
    test_code = TestCode()
    assert test_code.status_code == 100

    @add_status_code(100, quiet=True)
    class TestCodeQuiet(SanicException):
        pass

    assert _sanic_exceptions[100] == TestCodeQuiet
    test_code_quiet = TestCodeQuiet()
    assert test_code_quiet.quiet

    @add_status_code(500, quiet=False)
    class TestCodeHighQuiet(SanicException):
        pass

    assert _sanic_exceptions[500] == TestCodeHighQuiet
    test_code_high_quiet = TestCodeHighQuiet()
    assert not test

# Generated at 2022-06-14 07:17:00.471858
# Unit test for function add_status_code
def test_add_status_code():
    class A(SanicException):
        pass
    class B(SanicException):
        pass
    class C(SanicException):
        pass
    add_status_code(200)(A)
    add_status_code(300, quiet=True)(B)
    add_status_code(400)(C)
    assert A().status_code == 200
    assert B().status_code == 300
    assert C().status_code == 400
    assert A().quiet == False
    assert B().quiet == True
    assert C().quiet == True

# Generated at 2022-06-14 07:17:09.337574
# Unit test for function add_status_code
def test_add_status_code():
    # When there is no error
    class TestException(SanicException):
        pass
    add_status_code(400)(TestException)
    assert issubclass(_sanic_exceptions[400], TestException)
    assert _sanic_exceptions[400].status_code == 400
    
    # When there is an error
    with pytest.raises(ValueError) as e_info:
        class TestException2(SanicException):
            pass
        add_status_code(400)(TestException2)
        add_status_code(400)(TestException2)
    assert e_info.value.args[0] == "A subclass of SanicException with status code 400 already exists."

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:17:17.631903
# Unit test for function add_status_code
def test_add_status_code():
    """
    test_add_status_code
    函数装饰器:添加状态码和状态信息.
    参数:
        code : 状态码
        quiet : 是否允许不安静
    """
    add_status_code(404, True)
    add_status_code(200, False)
    add_status_code(404, False)
    add_status_code(200, True)


# Generated at 2022-06-14 07:17:28.142662
# Unit test for function add_status_code
def test_add_status_code():
    with pytest.raises(Exception):
        @add_status_code
        class A(SanicException):
            pass
    with pytest.raises(Exception):
        @add_status_code(101)
        class A():
            pass
    with pytest.raises(Exception):
        @add_status_code(101)
        def f():
            pass
    # All of these are valid
    @add_status_code(101)
    class A(SanicException):
        pass
    @add_status_code(101, quiet=True)
    class A(SanicException):
        pass
    @add_status_code(101, quiet=False)
    class A(SanicException):
        pass

# Generated at 2022-06-14 07:17:33.840598
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(status_code=200)
    class _TestClass(SanicException):
        pass

    assert _TestClass.status_code == 200
    assert issubclass(_TestClass, SanicException)
    assert _TestClass().status_code == 200

# Generated at 2022-06-14 07:17:36.295585
# Unit test for function add_status_code
def test_add_status_code():
    class TestEx(SanicException):
        pass

    assert TestEx in _sanic_exceptions

# Generated at 2022-06-14 07:17:47.219441
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class test1(SanicException):
        """
        **Status**: 400 Bad Request
        """
        pass

    @add_status_code(500)
    class test2(SanicException):
        """
        **Status**: 500 Internal Server Error
        """
        pass

    @add_status_code(500, quiet=False)
    class test3(SanicException):
        """
        **Status**: 500 Internal Server Error
        """
        pass

    assert test1.status_code == 400
    assert test2.status_code == 500
    assert test1.quiet == True
    assert test2.quiet == True
    assert test3.quiet == False


# Generated at 2022-06-14 07:18:00.873405
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500, quiet=True)
    class Exception1(Exception):
        pass

    assert Exception1.quiet == True

    @add_status_code(500, quiet=False)
    class Exception2(Exception):
        pass

    assert Exception2.quiet == False

    @add_status_code(500, quiet=None)
    class Exception3(Exception):
        pass

    assert Exception3.quiet == False

    @add_status_code(200, quiet=None)
    class Exception4(Exception):
        pass

    assert Exception4.quiet == True

    @add_status_code(200, quiet=False)
    class Exception5(Exception):
        pass

    assert Exception5.quiet == False


# Generated at 2022-06-14 07:18:26.446040
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 404
    quiet =  False
    def class_decorator(cls):
        cls.status_code = status_code
        if quiet or quiet is None and status_code != 500:
            cls.quiet = True
        _sanic_exceptions[status_code] = cls
        return cls
    original_class_decorator = add_status_code(status_code, quiet)
    assert original_class_decorator.__name__ == class_decorator.__name__
    

# Generated at 2022-06-14 07:18:38.266399
# Unit test for function add_status_code
def test_add_status_code():
    global _sanic_exceptions
    _sanic_exceptions = {}
    def class_decorator(cls):
        cls.status_code = 500
        _sanic_exceptions[500] = cls
        return cls
    @add_status_code(500)
    class TestClass1(SanicException):
        pass
    class_decorator(TestClass1)
    assert _sanic_exceptions[500] == TestClass1
    assert TestClass1.status_code == 500
    @add_status_code(500, quiet=True)
    class TestClass2(SanicException):
        pass
    class_decorator(TestClass2)
    assert _sanic_exceptions[500] == TestClass2
    assert TestClass2.status_code == 500 and TestClass2.quiet

# Generated at 2022-06-14 07:18:42.697333
# Unit test for function add_status_code
def test_add_status_code():
    def f(x):
        raise NotImplementedError
    add_status_code(100, quiet=True)(f)
    assert f.quiet
    assert f.status_code == 100


# Generated at 2022-06-14 07:18:47.402699
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(300)
    class TestingException(SanicException):
        pass
    
    assert TestingException.status_code == 300

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:18:53.317807
# Unit test for function add_status_code
def test_add_status_code():
    __status_code = 555
    add_status_code(__status_code)
    assert issubclass(SanicException, _sanic_exceptions[__status_code]), "Expected %s class to be in %s." \
                                                                         % (__status_code, _sanic_exceptions)

# Generated at 2022-06-14 07:19:00.539793
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 100
    assert TestException.quiet is False

    @add_status_code(200)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 200
    assert TestException.quiet is True


# Generated at 2022-06-14 07:19:06.603167
# Unit test for function add_status_code
def test_add_status_code():

    add_status_code(123, quiet=True)

    class TestException(SanicException):
        pass

    @add_status_code(456)
    class DecoratedTestException(TestException):
        pass

    decorated_test_exception = DecoratedTestException("DecoratedTestException")
    # assert decorated_test_exception.status_code == 456
    assert decorated_test_exception.quiet is True
    assert _sanic_exceptions[456] == DecoratedTestException

# Generated at 2022-06-14 07:19:14.207880
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class TestError1(SanicException):
        pass

    assert type(TestError1) == type(_sanic_exceptions[403])

    @add_status_code(403)
    class TestError2(SanicException):
        pass

    assert type(TestError2) == type(_sanic_exceptions[403])

# Generated at 2022-06-14 07:19:22.467082
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500, quiet=True)
    class A(Exception):
        pass

    assert _sanic_exceptions[500] == A
    assert A().status_code == 500
    assert A().quiet is True

    @add_status_code(501, quiet=False)
    class B(Exception):
        pass

    assert _sanic_exceptions[501] == B
    assert B().status_code == 501
    assert B().quiet is False


# Unit tests for function abort

# Generated at 2022-06-14 07:19:31.727750
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    @add_status_code(200)
    class TestException2(SanicException):
        pass

    @add_status_code(201)
    class TestException3(SanicException):
        pass

    assert TestException().status_code == 500
    assert TestException2().status_code == 200
    assert TestException3().status_code == 201
    assert TestException2().quiet is True
    assert TestException3().quiet is True
    assert _sanic_exceptions[200] == TestException2
    assert _sanic_exceptions[201] == TestException3

# Generated at 2022-06-14 07:20:08.525683
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(599)
    class CustomException(SanicException):
        pass

    assert _sanic_exceptions.get(599) == CustomException
    assert CustomException('message', status_code=599).status_code == 599

# Generated at 2022-06-14 07:20:19.837057
# Unit test for function add_status_code
def test_add_status_code():
    class CustomException(SanicException):
        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message)

            if status_code is not None:
                self.status_code = status_code

            # quiet=None/False/True with None meaning choose by status
            if quiet or quiet is None and status_code not in (None, 500):
                self.quiet = True

    test_exception = add_status_code(418)(CustomException)
    assert test_exception.status_code == 418

    test_exception = add_status_code(418, quiet=True)(CustomException)
    assert test_exception.status_code == 418
    assert test_exception.quiet


# Generated at 2022-06-14 07:20:29.047139
# Unit test for function add_status_code
def test_add_status_code():

    class UnknownException(SanicException):
        pass

    assert None == SanicException.status_code
    assert None == SanicException.quiet

    assert 404 == NotFound.status_code
    assert True == NotFound.quiet

    assert 400 == InvalidUsage.status_code
    assert True == InvalidUsage.quiet

    assert 405 == MethodNotSupported.status_code
    assert None == MethodNotSupported.quiet

    assert 500 == ServerError.status_code
    assert None == ServerError.quiet

    assert 503 == ServiceUnavailable.status_code
    assert True == ServiceUnavailable.quiet

    assert None == UnknownException.status_code
    assert None == UnknownException.quiet

# Generated at 2022-06-14 07:20:31.172524
# Unit test for function add_status_code
def test_add_status_code():
    #DWT - not sure how to test this...
    pass

# Generated at 2022-06-14 07:20:43.213765
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test function add_status_code()
    """
    @add_status_code(400)
    class test1(SanicException):
        def __init__(self, message):
            super().__init__(message)
    assert hasattr(_sanic_exceptions[400], "quiet") and _sanic_exceptions[400].quiet is True

    @add_status_code(500)
    class test1(SanicException):
        def __init__(self, message):
            super().__init__(message)
    assert hasattr(_sanic_exceptions[500], "quiet") and _sanic_exceptions[500].quiet is False


# Generated at 2022-06-14 07:20:48.694373
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyException(SanicException):
        pass

    assert MyException.status_code == 400

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:20:54.334870
# Unit test for function add_status_code
def test_add_status_code():
    assert hasattr(_sanic_exceptions[404], 'status_code')
    assert hasattr(NotFound, 'status_code')
    assert hasattr(NotFound, 'quiet')
    assert hasattr(_sanic_exceptions[404], 'quiet')


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:20:59.773742
# Unit test for function add_status_code
def test_add_status_code():
    class TestError(SanicException):
        pass

    test = add_status_code(555, True)(TestError)
    
    assert _sanic_exceptions[555] == test
    assert test.status_code == 555
    assert test.quiet is True

# Generated at 2022-06-14 07:21:06.344634
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class BadRequest(SanicException):
        pass

    @add_status_code(500)
    class InternalServerError(SanicException):
        pass

    @add_status_code(429)
    class TooManyRequests(SanicException):
        pass

    assert _sanic_exceptions[400] == BadRequest
    assert _sanic_exceptions[500] == InternalServerError
    assert _sanic_exceptions[429] == TooManyRequests

# Generated at 2022-06-14 07:21:12.790255
# Unit test for function add_status_code
def test_add_status_code():
    """
    To add a new exception, simply create a subclass of SanicException and
    decorate it with an integer status code.
    """
    @add_status_code(200)
    class Test(SanicException):
        pass
    assert _sanic_exceptions[200] == Test
    assert Test(message="", status_code=200, quiet=True)
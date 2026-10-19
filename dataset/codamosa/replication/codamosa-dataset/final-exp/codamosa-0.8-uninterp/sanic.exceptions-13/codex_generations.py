

# Generated at 2022-06-14 07:11:15.257637
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    exception = Unauthorized("Authentication required",scheme = "Basic", realm = "Testing?")
    assert exception.status_code == 401 and exception.headers == {"WWW-Authenticate": "Basic realm=Testing?"}

# Generated at 2022-06-14 07:11:27.011598
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    error = Unauthorized('Auth required.')
    assert error.status_code == 401
    assert error.message == 'Auth required.'
    assert not hasattr(error, 'headers')

    error = Unauthorized('Auth required.', scheme='Basic')
    assert error.status_code == 401
    assert error.message == 'Auth required.'
    assert error.headers == {'WWW-Authenticate': 'Basic'}

    error = Unauthorized('Auth required.', scheme='Basic', realm='Welcome')
    assert error.status_code == 401
    assert error.message == 'Auth required.'
    assert error.headers == {'WWW-Authenticate': 'Basic realm="Welcome"'}


# Generated at 2022-06-14 07:11:32.618152
# Unit test for constructor of class ServerError
def test_ServerError():
    """
    This function is used to test the constructor of class ServerError
    """
    message = "There is a server error"
    status_code = 500
    obj = ServerError(message, status_code)
    assert obj.status_code == 500
    assert message in str(obj)


# Generated at 2022-06-14 07:11:37.233175
# Unit test for constructor of class LoadFileException
def test_LoadFileException():
    loadFileException = LoadFileException("test input")
    assert loadFileException.args[0] == "test input"

# Generated at 2022-06-14 07:11:42.491591
# Unit test for constructor of class Forbidden
def test_Forbidden():
    try:
        raise Forbidden()
        #raise Exception()
    except Forbidden as fde:
        print('exception message: ' + str(fde))
        print(fde.status_code)

if __name__ == "__main__":
    test_Forbidden()

# Generated at 2022-06-14 07:11:47.716935
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    header = Unauthorized.__init__.__code__.co_varnames
    scheme = header[0]
    realm = header[1]
    nonce = header[2]
    opaque = header[3]

# Generated at 2022-06-14 07:11:49.304435
# Unit test for constructor of class InvalidSignal
def test_InvalidSignal():
    try:
        raise InvalidSignal('test')
    except Exception as e:
        assert str(e) == 'test'

# Generated at 2022-06-14 07:11:53.085516
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", 
                           scheme="Bearer",
                           realm="Restricted Area")
    except Unauthorized as e:
        assert e.headers["WWW-Authenticate"] == "Bearer realm=\"Restricted Area\""

# Generated at 2022-06-14 07:12:07.556657
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    """
    Test case for Unauthorized class

    Basic auth test case
    """
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except Unauthorized as e:
        assert str(e) == "Auth required."
        assert e.status_code == 401
        assert e.scheme == "Basic"
        assert e.realm == "Restricted Area"
    else:
        assert False, "Unauthorized not raised"

    try:
        raise Unauthorized("Auth required.", status_code=123, scheme="Basic", realm="Restricted Area")
    except Unauthorized as e:
        assert e.status_code == 123
    else:
        assert False, "Unauthorized not raised"


# Generated at 2022-06-14 07:12:15.183415
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    except SanicException as exc:
        assert exc.headers == {
                "WWW-Authenticate": "Basic realm=\"Restricted Area\""
                }
        assert exc.status_code == 401
    else:
        assert False, "Unauthorized constructor passess test"


# Generated at 2022-06-14 07:12:19.487952
# Unit test for constructor of class InvalidSignal
def test_InvalidSignal():
    with pytest.raises(TypeError):
        InvalidSignal()


# Generated at 2022-06-14 07:12:20.369085
# Unit test for constructor of class InvalidSignal
def test_InvalidSignal():
    pass

# Generated at 2022-06-14 07:12:24.406944
# Unit test for constructor of class HeaderExpectationFailed
def test_HeaderExpectationFailed():
    """
    >>> try:
    ...    raise HeaderExpectationFailed("foo")
    ... except HeaderExpectationFailed as err:
    ...    print(err.message)
    ...    print(err.status_code)
    foo
    417
    """

# Generated at 2022-06-14 07:12:28.394127
# Unit test for constructor of class LoadFileException
def test_LoadFileException():
    msg = "Load file exception"
    try:
        raise LoadFileException(msg)
    except LoadFileException as e:
        assert e.status_code == 500
        assert e.message == msg

# Generated at 2022-06-14 07:12:29.801786
# Unit test for constructor of class InvalidSignal
def test_InvalidSignal():
    InvalidSignal(message="Test", status_code=500)

# Generated at 2022-06-14 07:12:31.494215
# Unit test for constructor of class ServerError
def test_ServerError():
    assert ServerError("error message", 500, True).message == "error message"

# Generated at 2022-06-14 07:12:40.112009
# Unit test for function add_status_code
def test_add_status_code():
    # Define a custom exception
    @add_status_code(418)
    class IAmATeaPot(SanicException):
        pass
    # Ensure the status code is being set on the exception
    assert IAmATeaPot.status_code == 418
    # Ensure that the exception is registered with Sanic
    assert _sanic_exceptions[418] == IAmATeaPot

if __name__ == '__main__':
    test_add_status_code()

# Generated at 2022-06-14 07:12:45.105347
# Unit test for constructor of class HeaderNotFound
def test_HeaderNotFound():
    header_not_found = HeaderNotFound()
    assert header_not_found.status_code == 400
    assert str(header_not_found) == '400: Bad Request'


# Generated at 2022-06-14 07:12:47.320588
# Unit test for constructor of class Forbidden
def test_Forbidden():
    exception = Forbidden("message")
    assert exception.message == "message"
    assert exception.status_code == 403

# Generated at 2022-06-14 07:13:01.279162
# Unit test for constructor of class LoadFileException
def test_LoadFileException():
    _file = "/path/SQL.py"
    _exception = LoadFileException("could not execute config file %s", _file)
    assert(_exception.args[0] == "could not execute config file %s")
    assert(_exception.args[1] == _file)

if __name__ == "__main__":
    # Unit test for the class SanicException
    _message = "HTTP status code is not implemented"
    _status_code = 600
    _quiet = True
    _exception = SanicException(_message, _status_code, _quiet)
    assert(_exception.args[0] == _message)
    assert(_exception.status_code == _status_code)
    assert(_exception.quiet == _quiet)

    # Unit test for the method add_status_code

# Generated at 2022-06-14 07:13:07.914423
# Unit test for function add_status_code
def test_add_status_code():
    """
    * Test that add_status_code() returns a decorator
    * Test that class_decorator() returns a class
    """

    @add_status_code(status_code=418)
    class SomeErrorClass(SanicException):
        pass

    assert SomeErrorClass.status_code == 418
    assert _sanic_exceptions[418] == SomeErrorClass



# Generated at 2022-06-14 07:13:13.246188
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestException(Exception):
        pass

    assert _sanic_exceptions[200] == TestException
    assert TestException('test').status_code == 200


# Unit tests for class SanicException

# Generated at 2022-06-14 07:13:18.572859
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(408)
    class TestException(SanicException):
        pass
    assert ServerError.status_code == 500
    assert TestException.status_code == 408
    assert _sanic_exceptions[408] == TestException

# Generated at 2022-06-14 07:13:29.359475
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestClass(SanicException):
        pass

    assert TestClass.status_code == 200
    assert TestClass.quiet is False
    assert TestClass.message == ""
    assert TestClass(message="test") is not None
    assert TestClass(message="test").status_code == 200

    @add_status_code(200, quiet=True)
    class TestClass(SanicException):
        pass

    assert TestClass.status_code == 200
    assert TestClass.quiet is True
    assert TestClass(message="test") is not None
    assert TestClass(message="test").status_code == 200
    assert TestClass(message="test").message == "test"

    @add_status_code(201)
    class TestClass(SanicException):
        pass

    assert Test

# Generated at 2022-06-14 07:13:37.319721
# Unit test for function add_status_code
def test_add_status_code():
    assert _sanic_exceptions[404] == NotFound
    assert _sanic_exceptions[400] == InvalidUsage
    assert _sanic_exceptions[405] == MethodNotSupported
    assert _sanic_exceptions[500] == ServerError
    assert _sanic_exceptions[503] == ServiceUnavailable
    assert _sanic_exceptions[408] == RequestTimeout
    assert _sanic_exceptions[413] == PayloadTooLarge
    assert _sanic_exceptions[401] == Unauthorized

# Generated at 2022-06-14 07:13:44.379043
# Unit test for function add_status_code
def test_add_status_code():
    def class_decorator(cls):
        cls.status_code = code
        if code != 500:
            cls.quiet = True
        _sanic_exceptions[code] = cls
        return cls
    code = 404
    assert add_status_code(code) is class_decorator
    code = 500
    assert add_status_code(code) is class_decorator

# Generated at 2022-06-14 07:13:48.112605
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class Created(SanicException):
        pass
    assert Created.status_code == 201
    assert Created.quiet == True


# Generated at 2022-06-14 07:13:59.047234
# Unit test for function add_status_code
def test_add_status_code():
    assert not hasattr(SanicException, "status_code")
    assert SanicException.status_code is None
    assert not hasattr(SanicException, "quiet")
    assert SanicException.quiet is False

    assert hasattr(ServerError, "status_code")
    assert ServerError.status_code == 500
    assert hasattr(ServerError, "quiet")
    assert ServerError.quiet is False

    assert hasattr(NotFound, "status_code")
    assert NotFound.status_code == 404
    assert hasattr(NotFound, "quiet")
    assert NotFound.quiet is True

    assert hasattr(Forbidden, "status_code")
    assert Forbidden.status_code == 403
    assert hasattr(Forbidden, "quiet")
    assert Forbidden.quiet is True


# Generated at 2022-06-14 07:14:02.172504
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(999)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[999] is TestException
    assert TestException.status_code == 999

# Generated at 2022-06-14 07:14:07.954740
# Unit test for function add_status_code
def test_add_status_code():
    # Add a new exception type to SanicException
    @add_status_code(123)
    class New_exception(SanicException):
        pass

    # Check that it has the right status code and is in the dict
    assert New_exception.status_code == 123
    assert _sanic_exceptions[123].__name__ == "New_exception"


# Generated at 2022-06-14 07:14:17.104234
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(555)
    class CustomException(SanicException):
        pass

    # check that the exception was registered
    assert 555 in _sanic_exceptions

    # check that exception's status_code was updated
    assert CustomException.status_code == 555

    # check that exception's quiet was updated to True
    assert CustomException.quiet == True

# Generated at 2022-06-14 07:14:22.726823
# Unit test for function add_status_code
def test_add_status_code():
    """
    add_status_code adds the status code to the exception class,
    and adds the exception class to a dictionary of exceptions
    """

    @add_status_code(203)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 203
    assert _sanic_exceptions[203] == TestException
    # Test without quiet
    @add_status_code(203)
    class TestException2(SanicException):
        pass
    assert TestException2.quiet == False
    # Test with quiet
    @add_status_code(203, quiet=True)
    class TestException3(SanicException):
        pass
    assert TestException3.quiet == True

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:14:31.214257
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(412)  # precondition failed
    class PreconditionFailed(SanicException):
        pass

    assert PreconditionFailed.status_code == 412
    assert not hasattr(PreconditionFailed, "quiet")

    @add_status_code(406)  # not acceptable
    class NotAcceptable(SanicException):
        pass

    assert NotAcceptable.status_code == 406
    assert hasattr(NotAcceptable, "quiet")



# Generated at 2022-06-14 07:14:37.501609
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class TestClass(SanicException):
        pass

    assert TestClass.status_code == 123
    assert TestClass.quiet is None
    assert isinstance(_sanic_exceptions[123], TestClass)
    assert _sanic_exceptions[123].status_code == 123


# Generated at 2022-06-14 07:14:44.371522
# Unit test for function add_status_code
def test_add_status_code():
    # Create a dummy class to use with

    @add_status_code(200)
    class MyException(SanicException):
        pass

    assert MyException.status_code == 200
    assert MyException.quiet is True
    assert _sanic_exceptions[200] is MyException

    @add_status_code(500)
    class OtherException(SanicException):
        pass

    assert OtherException.status_code == 500
    assert OtherException.quiet is False
    assert _sanic_exceptions[500] is OtherException

    @add_status_code(201, quiet=False)
    class AnotherException(SanicException):
        pass

    assert AnotherException.status_code == 201
    assert AnotherException.quiet is False
    assert _sanic_exceptions[201] is AnotherException



# Generated at 2022-06-14 07:14:48.671179
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(402)
    class ClassDecorator(SanicException):
        pass

    class_decorator = ClassDecorator("")
    assert class_decorator.status_code == 402




# Generated at 2022-06-14 07:14:50.815414
# Unit test for function add_status_code
def test_add_status_code():
    result = add_status_code(200)(NotFound)
    assert result.status_code == 200


# Generated at 2022-06-14 07:14:55.237143
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class BadRequest(SanicException):
        """
        **Status**: 400 Bad Request
        """

        pass

    assert BadRequest.status_code == 403
    assert _sanic_exceptions[403] == BadRequest

# Generated at 2022-06-14 07:15:03.666577
# Unit test for function add_status_code
def test_add_status_code():
    try:
        abort(418)
        assert False, "no exception raised"
    except SanicException as e:
        assert e.status_code == 418
        assert e.message == "I'm a teapot"

    @add_status_code(418)
    class Teapot(SanicException):
        pass

    try:
        abort(418)
        assert False, "no exception raised"
    except Teapot as e:
        assert e.status_code == 418
        assert e.message == "I'm a teapot"

    try:
        abort(500)
        assert False, "no exception raised"
    except ServerError as e:
        assert e.status_code == 500
        assert e.message == "Internal Server Error"


if __name__ == "__main__":
    test_add

# Generated at 2022-06-14 07:15:07.917451
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(503)
    class ServiceUnavailable(SanicException):
        pass

    assert ServiceUnavailable



# Generated at 2022-06-14 07:15:13.862755
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(900) == class_decorator
    # TODO


# Generated at 2022-06-14 07:15:17.648624
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class UnexpectedError(SanicException):
        pass

    assert 418 in _sanic_exceptions
    assert _sanic_exceptions[418] == UnexpectedError
    assert UnexpectedError.status_code == 418

# Generated at 2022-06-14 07:15:29.113761
# Unit test for function add_status_code
def test_add_status_code():
    from types import MethodType

    status_code = 206

    # GIVEN
    # - a function with a decorator
    @add_status_code(status_code)
    class Status(SanicException):
        pass

    # THEN
    # - the decorated method should have a new property "status_code"
    assert hasattr(Status, "status_code")
    # - the value of the new property should be the status_code passed in.
    assert getattr(Status, "status_code") == status_code
    # - Status should be registered with status_code in _sanic_exceptions
    assert _sanic_exceptions[status_code] == Status

# Generated at 2022-06-14 07:15:32.414115
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestAddStatusCode(SanicException):
        pass

    assert TestAddStatusCode().status_code == 400



# Generated at 2022-06-14 07:15:38.016064
# Unit test for function add_status_code
def test_add_status_code():
    class Test(SanicException):
        def __init__(self, status_code, message=None):
            super().__init__(message, status_code=status_code)

    @add_status_code(400)
    def test_decorated():
        pass

    # Check if adding an int works
    assert test_decorated().status_code == 400
    # Check if adding a class works
    assert Test(400).status_code == 400


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:15:47.335457
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    assert TestException.status_code is None

    add_status_code(200)(TestException)
    assert TestException.status_code == 200

    add_status_code(400, quiet=True)(TestException)
    assert TestException.status_code == 400
    assert TestException.quiet is True

    add_status_code(500, quiet=False)(TestException)
    assert TestException.status_code == 500
    assert TestException.quiet is False



# Generated at 2022-06-14 07:15:57.118397
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    add_status_code(400)(TestException)
    assert issubclass(_sanic_exceptions[400], TestException)
    assert issubclass(_sanic_exceptions[400], SanicException)

    add_status_code(500, quiet=False)(TestException)
    assert _sanic_exceptions[500].quiet is False
    add_status_code(500, quiet=True)(TestException)
    assert _sanic_exceptions[500].quiet is True
    add_status_code(500, quiet=None)(TestException)
    assert _sanic_exceptions[500].quiet is False

    assert _sanic_exceptions[404].quiet is True

# Generated at 2022-06-14 07:16:09.040200
# Unit test for function add_status_code
def test_add_status_code():
    '''
    # add_status_code
    ## test class_decorator(...)
    ### add a new SanicException with status code and message
    ### add a new SanicException with status code and message, and quiet to true
    ### add a new SanicException with status code, message and quiet to false
    ### add a new SanicException with status code, message, and quiet to true
    '''
    def test():
        @add_status_code(101)
        class Test101(SanicException):
            pass
        @add_status_code(102, True)
        class Test102(SanicException):
            pass
        @add_status_code(103, False)
        class Test103(SanicException):
            pass

# Generated at 2022-06-14 07:16:12.323749
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(600)
    class BadBad(SanicException):
        pass

    assert BadBad.status_code == 600

# Generated at 2022-06-14 07:16:15.952234
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class MockSanicException(SanicException):
        pass

    assert _sanic_exceptions[100] is MockSanicException

# Generated at 2022-06-14 07:16:31.094887
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400, quiet=True)
    class CustomException(SanicException):
        pass
    assert CustomException.status_code == 400
    assert CustomException.quiet == True
    assert _sanic_exceptions.get(400) == CustomException

# Generated at 2022-06-14 07:16:34.302851
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class InternalServerError(SanicException):
        """
        **Status**: 500 Internal Server Error
        """
    assert InternalServerError.status_code==500

# Generated at 2022-06-14 07:16:45.348701
# Unit test for function add_status_code
def test_add_status_code():
    test_status_code=500
    test_message="Test Message"
    test_quiet=True
    SanicException.quiet=False

    add_status_code(test_status_code, test_quiet)(SanicException)
    sanic_exception_obj=_sanic_exceptions[test_status_code](test_message)
    assert sanic_exception_obj.status_code is test_status_code
    assert sanic_exception_obj.message is test_message
    assert sanic_exception_obj.quiet is test_quiet

test_add_status_code()


# Generated at 2022-06-14 07:16:51.659819
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 400
    quiet = True
    def class_decorator(cls):
        cls.status_code = status_code
        if quiet:
            cls.quiet = True
        _sanic_exceptions[status_code] = cls
        return cls
    assert add_status_code(status_code, quiet)(class_decorator)

# Generated at 2022-06-14 07:17:05.180992
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(404)(NotFound) == NotFound
    assert add_status_code(400)(InvalidUsage) == InvalidUsage
    assert add_status_code(405)(MethodNotSupported) == MethodNotSupported
    assert add_status_code(500)(ServerError) == ServerError
    assert add_status_code(503)(ServiceUnavailable) == ServiceUnavailable
    assert add_status_code(408)(RequestTimeout) == RequestTimeout
    assert add_status_code(413)(PayloadTooLarge) == PayloadTooLarge
    assert add_status_code(416)(ContentRangeError) == ContentRangeError
    assert add_status_code(417)(HeaderExpectationFailed) == HeaderExpectationFailed
    assert add_status_code(403)(Forbidden) == Forbidden

# Generated at 2022-06-14 07:17:09.428312
# Unit test for function add_status_code
def test_add_status_code():
    assert len(_sanic_exceptions) == 0
    @add_status_code(400)
    class Bad(Exception):
        pass
    assert _sanic_exceptions[400] == Bad
    assert len(_sanic_exceptions) == 1

# Generated at 2022-06-14 07:17:12.685198
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class TestClass(SanicException):
        pass
    assert TestClass.status_code == 403
    assert TestClass.quiet is None
    assert _sanic_exceptions[403] == TestClass



# Generated at 2022-06-14 07:17:15.715001
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class A(SanicException):
        pass

    assert A.status_code == 400
    assert A.quiet == True

# Generated at 2022-06-14 07:17:21.589098
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class Foo(SanicException):
        pass

    @add_status_code(500, quiet=True)
    class Bar(SanicException):
        pass

    assert isinstance(Foo().quiet, bool)
    assert Foo().quiet is False

    assert isinstance(Bar().quiet, bool)
    assert Bar().quiet is True

# Generated at 2022-06-14 07:17:30.730545
# Unit test for function add_status_code
def test_add_status_code():
    # create a status code
    @add_status_code(418)
    class IAmATeapot(SanicException):
        pass
    assert IAmATeapot is not None
    assert IAmATeapot.status_code == 418
    assert IAmATeapot().status_code == 418
    assert IAmATeapot.quiet is True

    assert _sanic_exceptions[418] == IAmATeapot

    # test quiet does not default to true
    @add_status_code(500)
    class TestStatusCode(SanicException):
        pass
    assert TestStatusCode.quiet is None

    assert _sanic_exceptions[500] == TestStatusCode

# Generated at 2022-06-14 07:17:59.373739
# Unit test for function add_status_code
def test_add_status_code():
    class SomeException(SanicException):
        pass

    @add_status_code(200)
    class SomeException200(SanicException):
        pass

    @add_status_code(400, quiet=False)
    class SomeException400(SanicException):
        pass

    assert SomeException(message="Not Found")
    assert SomeException200(message="")
    assert SomeException400(message="Bad Request")
    assert SomeException400.quiet is False

# Generated at 2022-06-14 07:18:01.505246
# Unit test for function add_status_code
def test_add_status_code():
    class FooException(SanicException):
        pass

    add_status_code(400)(FooException)

    assert _sanic_exceptions.get(400) == FooException



# Generated at 2022-06-14 07:18:05.171387
# Unit test for function add_status_code
def test_add_status_code():
    class MockException(Exception):
        status_code = 500
        pass

    add_status_code(MockException.status_code)(MockException)

    assert MockException in _sanic_exceptions.values()

# Generated at 2022-06-14 07:18:08.010878
# Unit test for function add_status_code
def test_add_status_code():
    class A(SanicException):
        pass

    assert A.status_code is None
    assert A.quiet is None

    add_status_code(200)(A)
    assert A.status_code == 200
    assert A.quiet is True

# Generated at 2022-06-14 07:18:19.760464
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Code200(SanicException):
        pass
    assert Code200.status_code == 200
    assert Code200.quiet == False
    @add_status_code(400, quiet=True)
    class Code400(SanicException):
        pass
    assert Code400.status_code == 400
    assert Code400.quiet == True
    @add_status_code(500, quiet=False)
    class Code500(SanicException):
        pass
    assert Code500.status_code == 500
    assert Code500.quiet == False
    @add_status_code(500)
    class Code500Default(SanicException):
        pass
    assert Code500Default.status_code == 500
    assert Code500Default.quiet == False

# Generated at 2022-06-14 07:18:32.503222
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(401)
    class TestException(SanicException):
        pass

    @add_status_code(402)
    class TestException2(SanicException):
        pass

    assert 401 in _sanic_exceptions
    assert hasattr(_sanic_exceptions[401], "status_code")
    assert hasattr(_sanic_exceptions[401], "quiet")

    assert 402 in _sanic_exceptions
    assert hasattr(_sanic_exceptions[402], "status_code")
    assert hasattr(_sanic_exceptions[402], "quiet")

    assert 501 not in _sanic_exceptions

    # Test Exception for 500
    try:
        raise NotFound()
    except NotFound as e:
        assert e.status_code == 404
        assert e.quiet is True

   

# Generated at 2022-06-14 07:18:36.657028
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Foo(SanicException):
        pass

    assert Foo.status_code == 200
    assert Foo.quiet == True
    assert _sanic_exceptions[200] == Foo

# Generated at 2022-06-14 07:18:39.898483
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(501)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[501] is TestException

# Generated at 2022-06-14 07:18:47.057058
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class test(SanicException):
        pass
    # tests to make sure adding a status code causes the status code to be added to
    # the _sanic_exceptions dictionary
    assert _sanic_exceptions[403] is test
    # tests to make sure that the test class has the correct status code
    assert test.status_code is 403

# Generated at 2022-06-14 07:18:56.618348
# Unit test for function add_status_code
def test_add_status_code():
    class a(SanicException):
        pass
    assert a.status_code == 500
    assert a.__name__ == 'a'
    assert not a.quiet
    add_status_code(502)(a)
    assert a.status_code == 502
    assert a.quiet
    class b(SanicException):
        pass
    add_status_code(504)(b)
    assert b.status_code == 504
    assert not b.quiet

if __name__ == '__main__':
    test_add_status_code()

# Generated at 2022-06-14 07:19:49.393676
# Unit test for function add_status_code
def test_add_status_code():
    message = 'This is a custom message to be returned'
    status_code = 284

    # GIVEN a class decorated as a custom exception
    @add_status_code(status_code)
    class CustomException(SanicException):
        pass

    # WHEN abort() is called with the status code
    custom_exception = CustomException(message, status_code)
    # THEN the exception is raised
    assert custom_exception.status_code == status_code
    assert custom_exception.message == message

    # GIVEN a class decorated as a custom exception with its own default message
    @add_status_code(status_code, quiet=True)
    class CustomMessageException(SanicException):
        default_message = 'Default message to be returned'

    # WHEN abort() is called with the status code
    custom_message_ex

# Generated at 2022-06-14 07:19:55.955306
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 200
    message = "Success"
    exception = "Success"
    new_exception = add_status_code(status_code)(SanicException)
    new_exception = new_exception(message, status_code)
    assert new_exception.status_code == status_code
    assert str(new_exception) == exception

# Generated at 2022-06-14 07:20:09.691436
# Unit test for function add_status_code
def test_add_status_code():
    class StatusCodeException(SanicException):
        status_code = None

    def check_status_code(code, quiet=None):
        @add_status_code(code, quiet)
        class TestException(StatusCodeException):
            pass

        assert TestException.status_code == code
        assert TestException.quiet is quiet

    check_status_code(400, quiet=True)
    check_status_code(500, quiet=True)
    check_status_code(500, quiet=False)

    check_status_code(200, quiet=None)
    check_status_code(404, quiet=None)
    check_status_code(404, quiet=False)


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "-s", __file__])

# Generated at 2022-06-14 07:20:12.825986
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class TestAddStatusCode(SanicException):
        pass
    assert TestAddStatusCode.status_code == 123

# Generated at 2022-06-14 07:20:24.042430
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Hello(SanicException):
        pass

    @add_status_code(404, quiet=False)
    class Goodbye(SanicException):
        pass

    assert _sanic_exceptions.get(200) is Hello
    assert _sanic_exceptions.get(404) is Goodbye

    assert _sanic_exceptions.get(200)("hello").status_code == 200
    assert _sanic_exceptions.get(404)("goodbye").status_code == 404

    assert not _sanic_exceptions.get(200)("hello").quiet == False
    assert _sanic_exceptions.get(404)("goodbye").quiet == False

    assert _sanic_exceptions.get(500)("goodbye").quiet == False



# Generated at 2022-06-14 07:20:32.086976
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class CustomHTTPException(SanicException):
        pass

    assert 400 in _sanic_exceptions
    assert _sanic_exceptions[400] == CustomHTTPException

    @add_status_code(410)
    class CustomHTTPExceptionQuiet(SanicException):
        pass
    assert 410 in _sanic_exceptions
    assert _sanic_exceptions[410] == CustomHTTPExceptionQuiet

    @add_status_code(410, quiet=True)
    class CustomHTTPExceptionQuiet(SanicException):
        pass
    assert 410 in _sanic_exceptions
    assert _sanic_exceptions[410] == CustomHTTPExceptionQuiet

    @add_status_code(410, quiet=False)
    class CustomHTTPExceptionQuiet(SanicException):
        pass


# Generated at 2022-06-14 07:20:41.826399
# Unit test for function add_status_code
def test_add_status_code():
    def func():
        pass

    # creating a test SanicException
    class TestSanicException(SanicException):
        pass

    # adding status code to SanicException
    add_status_code(400)(TestSanicException)

    # testing SanicException status code
    assert TestSanicException(message="test").status_code == 400
    assert TestSanicException(message="test").__name__ == 'TestSanicException'

    # Testing add_status_code with a function
    add_status_code(404)(func)
    assert hasattr(func, "status_code") == True


# Generated at 2022-06-14 07:20:46.175626
# Unit test for function add_status_code
def test_add_status_code():
    # Make sure we have at least one status code
    assert _sanic_exceptions
    # Make sure code is correct
    assert _sanic_exceptions.get(404).status_code == 404


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:20:53.028004
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Test200(SanicException):
        pass
    
    @add_status_code(201)
    class Test201(SanicException):
        pass
    
    assert _sanic_exceptions[200] == Test200
    assert _sanic_exceptions[201] == Test201


# Generated at 2022-06-14 07:20:58.411493
# Unit test for function add_status_code
def test_add_status_code():
    status = 400
    message = "Testing."
    msg = STATUS_CODES[status]
    exception = _sanic_exceptions[status](message)
    assert(exception.status_code == status)
    assert(exception.message == msg)


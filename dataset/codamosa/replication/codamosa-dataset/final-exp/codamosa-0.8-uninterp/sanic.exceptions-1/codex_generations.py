

# Generated at 2022-06-14 07:11:13.448848
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    with pytest.raises(Unauthorized, match="Auth required."):
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")
    with pytest.raises(Unauthorized, match="Auth required."):
        raise Unauthorized("Auth required.", scheme="Digest", realm="Restricted Area", qop="auth, auth-int", algorithm="MD5", nonce="abcdef", opaque="zyxwvu")
    with pytest.raises(Unauthorized, match="Auth required."):
        raise Unauthorized("Auth required.", scheme="Bearer")
    with pytest.raises(Unauthorized, match="Auth required."):
        raise Unauthorized("Auth required.", scheme="Bearer", realm="Restricted Area")

# Generated at 2022-06-14 07:11:17.708694
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class TestException(SanicException):
        pass
    assert isinstance(TestException(''), TestException)
    assert TestException('').status_code == 403

if __name__ == '__main__':
    test_add_status_code()

# Generated at 2022-06-14 07:11:30.910043
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.")
    except Unauthorized as e:
        got_message = str(e)
        assert got_message == "Auth required."

    try:
        raise Unauthorized("Auth required.",
                           scheme="Basic",
                           realm="Restricted Area")
    except Unauthorized as e:
        got_message = str(e)
        got_scheme = e.headers["WWW-Authenticate"]
        assert got_message == "Auth required."
        assert got_scheme == "Basic realm='Restricted Area'"


# Generated at 2022-06-14 07:11:44.420631
# Unit test for function add_status_code
def test_add_status_code():

    class _Test(ServerError):
        pass

    add_status_code(900)(_Test)
    add_status_code(901, quiet=True)(_Test)
    add_status_code(1000)(_Test)

    assert _sanic_exceptions[900] is _Test
    assert _sanic_exceptions[901] is _Test
    assert _sanic_exceptions[1000] is _Test

    assert _sanic_exceptions[900]().status_code == 900
    assert _sanic_exceptions[901]().status_code == 901
    assert _sanic_exceptions[1000]().status_code == 1000

    assert _sanic_exceptions[900]().quiet is False
    assert _sanic_exceptions[901]().quiet is True

# Generated at 2022-06-14 07:11:51.062140
# Unit test for function add_status_code
def test_add_status_code():
    class MyInvalidUsage(SanicException):
        pass

    class MyNotFound(SanicException):
        pass

    add_status_code(400)(MyInvalidUsage)
    add_status_code(404)(MyNotFound)

    assert _sanic_exceptions[400] == MyInvalidUsage
    assert _sanic_exceptions[404] == MyNotFound


# Generated at 2022-06-14 07:11:58.455476
# Unit test for function add_status_code
def test_add_status_code():
    """
    test add_status_code function
    """
    # add 400 status code for two times.
    @add_status_code(400)
    class test_add_status_code_class1(SanicException):
        def __init__(self, message, status_code=None, quiet=None):
            SanicException.__init__(self, message, status_code, quiet)

    @add_status_code(400)
    class test_add_status_code_class2(SanicException):
        def __init__(self, message, status_code=None, quiet=None):
            SanicException.__init__(self, message, status_code, quiet)

    assert 400 in _sanic_exceptions, "status code 400 not in _sanic_exceptions"
    assert _sanic_exceptions

# Generated at 2022-06-14 07:12:10.717114
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # Test with scheme and realm
    scheme = "Basic"
    realm = "Restricted Area"
    message = "Auth required."
    ex1 = Unauthorized(message, scheme=scheme, realm=realm)
    assert ex1.message == message
    assert ex1.status_code == 401
    assert ex1.headers == {"WWW-Authenticate": f'{scheme} realm="{realm}"'}

    # Test with scheme, realm, qop, algorithm, nonce, opaque
    scheme = "Digest"
    realm = "Restricted Area"
    qop = "auth, auth-int"
    algorithm = "MD5"
    nonce = "abcdef"
    opaque = "zyxwvu"
    message = "Auth required."

# Generated at 2022-06-14 07:12:21.929064
# Unit test for function add_status_code
def test_add_status_code():
    # given status code 201 and quiet False
    @add_status_code(201, False)
    class NonQuiet(SanicException):
        pass

    assert NonQuiet.status_code == 201
    assert NonQuiet(message="test message").status_code == 201
    assert NonQuiet.quiet is False
    assert NonQuiet(message="test message").quiet is False

    # given status code 201 and quiet True
    @add_status_code(201, True)
    class Quiet(SanicException):
        pass

    assert Quiet(message="test message").status_code == 201
    assert Quiet.quiet is True
    assert Quiet(message="test message").quiet is True


# Generated at 2022-06-14 07:12:35.164976
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    @add_status_code(200)
    class TestException2(SanicException):
        pass

    @add_status_code(200, True)
    class TestException3(SanicException):
        pass

    try:
        raise TestException('test', 200)
    except SanicException as exception:
        assert not exception.quiet
        assert exception.status_code == 200
    
    try:
        raise TestException2('test', 200)
    except SanicException as exception:
        assert not exception.quiet
        assert exception.status_code == 200

    try:
        raise TestException3('test', 200)
    except SanicException as exception:
        assert exception.quiet
        assert exception.status_code == 200


# Generated at 2022-06-14 07:12:42.390159
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # Arrange
    message = "Auth required."
    scheme = "Basic"
    realm = "Restricted Area"
    exception = Unauthorized(message, scheme=scheme, realm=realm)

    # Assert
    assert exception.headers['WWW-Authenticate'] == 'Basic realm="Restricted Area"'
    assert exception.status_code == 401
    assert str(exception) == 'Auth required.'

# Generated at 2022-06-14 07:12:51.572367
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.",
                           scheme="Basic",
                           realm="Restricted Area")
    except Unauthorized as e:
        print(e.headers)
        print(e.status_code)
        print(e.args)
        print(e.kwargs)
    print('end test')


if __name__ == "__main__":
    test_Unauthorized()

# Generated at 2022-06-14 07:12:58.359302
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.", scheme="Basic", realm="test")
    except Unauthorized as e:
        assert e.headers["WWW-Authenticate"] == "Basic realm=\"test\""
        assert e.message == "Auth required."
        assert e.status_code == 401
    else:
        raise RuntimeError("Unauthorized exception is not thrown")



# Generated at 2022-06-14 07:13:01.277790
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    with pytest.raises(Unauthorized):
        raise Unauthorized("Auth required.", scheme="Basic", realm="Restricted Area")

# Generated at 2022-06-14 07:13:06.861493
# Unit test for function add_status_code
def test_add_status_code():
    """
    添加自定义异常
    """
    @add_status_code(202)
    class NewException(SanicException):
        pass

    assert _sanic_exceptions[202] == NewException





# Generated at 2022-06-14 07:13:10.504079
# Unit test for function add_status_code
def test_add_status_code():
    x = add_status_code(432)
    @x
    class MyException(Exception):
        pass
    return MyException



# Generated at 2022-06-14 07:13:14.455963
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    # add 'TestException' to status code 403
    add_status_code(403)(TestException)
    assert _sanic_exceptions[403] == TestException

# Generated at 2022-06-14 07:13:26.577682
# Unit test for function add_status_code
def test_add_status_code():
    # Set the status code
    # quiet=None/False/True with None meaning choose by status
    assert add_status_code(404)(SanicException).status_code == 404
    assert add_status_code(404)(SanicException)(message=None).status_code == 404
    assert add_status_code(404)(SanicException)(message=None).quiet == True
    assert add_status_code(500)(SanicException).status_code == 500
    assert add_status_code(500)(SanicException)(message=None).status_code == 500
    assert add_status_code(500)(SanicException)(message=None).quiet == False
    # Set the status code with quiet
    assert add_status_code(404, True)(SanicException).status_code == 404

# Generated at 2022-06-14 07:13:34.652715
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    with pytest.raises(Unauthorized) as excinfo:
        raise Unauthorized('Auth required.', scheme='Basic', realm='Restricted Area')
    assert 'Auth required.' == str(excinfo.value)
    assert 'Basic' == excinfo.value.headers['WWW-Authenticate'].split()[0]
    assert 'Restricted Area' == excinfo.value.headers['WWW-Authenticate'].split()[1][9:-1]


# Generated at 2022-06-14 07:13:43.122268
# Unit test for function add_status_code
def test_add_status_code():
    class IllegalStatusCode(SanicException):
        status_code = -1

    assert IllegalStatusCode.status_code == -1
    assert IllegalStatusCode.quiet is None
    assert 500 not in _sanic_exceptions

    class LegalStatusCode(SanicException):
        status_code = 500

    assert LegalStatusCode.status_code == 500
    assert LegalStatusCode.quiet is None
    assert 500 not in _sanic_exceptions

    @add_status_code(500)
    class LegalStatusCode2(SanicException):
        pass

    assert LegalStatusCode2.status_code == 500
    assert LegalStatusCode2.quiet is None
    assert 500 in _sanic_exceptions

    @add_status_code(500, quiet=True)
    class LegalStatusCode3(SanicException):
        pass


# Generated at 2022-06-14 07:13:48.981002
# Unit test for function add_status_code
def test_add_status_code():
    global _sanic_exceptions
    len_sanic_exceptions = len(_sanic_exceptions)

    @add_status_code(123)
    class SomeException(SanicException):
        pass

    assert len(_sanic_exceptions) == len_sanic_exceptions + 1
    assert _sanic_exceptions[123] == SomeException

# Generated at 2022-06-14 07:13:54.551718
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(999)
    class Bad(SanicException):
        pass
    assert Bad.status_code == 999
    assert _sanic_exceptions[999] == Bad

# Generated at 2022-06-14 07:14:00.241315
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    try:
        raise Unauthorized("Auth required.",
                           scheme="Basic",
                           realm="Restricted Area")
    except Unauthorized as e:
        assert e.scheme == "Basic"
        assert e.realm == "Restricted Area"



# Generated at 2022-06-14 07:14:12.753013
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class T(SanicException):
        pass

    assert T.status_code is 200
    assert _sanic_exceptions[200] is T
    assert T.quiet == False

    @add_status_code(201, True)
    class T(SanicException):
        pass

    assert T.status_code is 201
    assert _sanic_exceptions[201] is T
    assert T.quiet == True

    @add_status_code(202)
    class T(SanicException):
        pass

    assert T.status_code is 202
    assert _sanic_exceptions[202] is T
    assert T.quiet == True

    @add_status_code(203, False)
    class T(SanicException):
        pass

    assert T.status_code

# Generated at 2022-06-14 07:14:17.844412
# Unit test for function add_status_code
def test_add_status_code():
    test_code=300
    assert add_status_code(test_code)(SanicException)
    assert SanicException.status_code == test_code
    assert _sanic_exceptions.get(300) == SanicException
    assert SanicException.quiet == True

# Generated at 2022-06-14 07:14:22.787871
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class NotFound(SanicException):
        pass

    assert NotFound.status_code == 404
    assert _sanic_exceptions[404] == NotFound
    # Quiet defaults to False
    assert NotFound.quiet == False

# Generated at 2022-06-14 07:14:28.054675
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class _403Exception(SanicException):
        pass
    @add_status_code(404, quiet=False)
    class _404Exception(SanicException):
        pass

# Unit tests for class SanicException

# Generated at 2022-06-14 07:14:33.628431
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(599)
    class MyException(Exception):
        pass

    assert _sanic_exceptions[599] is MyException
    assert MyException.quiet is True

    # Test if status code added as a class decorator
    @add_status_code(400)
    class Error400(Exception):
        pass

    assert _sanic_exceptions[400] is Error400
    assert Error400.quiet is False

# Generated at 2022-06-14 07:14:43.212615
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(600)
    class My600Error(SanicException):
        pass
    assert My600Error.status_code == 600
    assert My600Error().status_code == 600
    assert My600Error.quiet is None
    assert My600Error().quiet is None

    # quiet=None/False/True with None meaning choose by status
    assert My600Error(None, status_code=599).quiet is None
    assert My600Error(None, status_code=500).quiet is True
    assert My600Error(None, status_code=599, quiet=None).quiet is True

    assert My600Error(None, status_code=600).quiet is True
    assert My600Error(None, status_code=600, quiet=True).quiet is True


# Generated at 2022-06-14 07:14:51.790740
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class NewException(SanicException):
        pass

    assert NewException.status_code == 403
    assert NewException.quiet is False
    assert type(_sanic_exceptions[403]) == type(NewException)

    @add_status_code(403, quiet=True)
    class NewException(SanicException):
        pass

    assert NewException.status_code == 403
    assert NewException.quiet is True
    assert type(_sanic_exceptions[403]) == type(NewException)

# Generated at 2022-06-14 07:15:02.222799
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    # Check if exception is raised when no parameters specified
    try:
        raise Unauthorized()
    except Unauthorized as e:
        assert str(e) == 'message'

    # Check if exception is raised when message is specified
    try:
        raise Unauthorized("this is probably not what you expect")
    except Unauthorized as e:
        assert str(e) == 'this is probably not what you expect'

    # Check if exception is raised when custom status code is specified
    try:
        raise Unauthorized("whatever you want", status_code=418)
    except Unauthorized as e:
        assert e.status_code == 418

    # Check if exception is raised when auth-scheme is specified

# Generated at 2022-06-14 07:15:14.358772
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(foo=1)(NotFound).__dict__ == add_status_code(foo=1)(SanicException).__dict__
    assert add_status_code(500, quiet=True).__dict__ == add_status_code(500, quiet=False).__dict__
    assert add_status_code(500, quiet=1).__dict__ != add_status_code(500, quiet=False).__dict__
    assert add_status_code(500,
                           quiet=True).__dict__ != add_status_code(500,
                                                                   quiet=False).__dict__
    assert add_status_code(200, quiet=True).__dict__ != add_status_code(200, quiet=False).__dict__

# Generated at 2022-06-14 07:15:17.532905
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(status_code=500, quiet=False)
    class NewException(SanicException):
        pass

    assert NewException.status_code == 500
    assert not NewException.quiet


# Generated at 2022-06-14 07:15:26.490979
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass
    add_status_code(201)(MyException)
    assert MyException.status_code == 201
    assert _sanic_exceptions[201] == MyException
    MyException()
    assert MyException.quiet == True

    assert SanicException.status_code == None
    assert SanicException.quiet == None
    SanicException()
    assert SanicException.status_code == None
    assert SanicException.quiet == None


# Generated at 2022-06-14 07:15:35.424468
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class CustomException(SanicException):
        pass

    assert CustomException.status_code == 400
    assert CustomException.quiet is True  # default
    assert STATUS_CODES[400] == b"Bad Request"  # default

    @add_status_code(500, quiet=False)
    class CustomException(SanicException):
        pass

    assert CustomException.quiet is False

    @add_status_code(200, quiet=False)
    class CustomException(SanicException):
        pass

    assert CustomException.quiet is False



# Generated at 2022-06-14 07:15:47.932347
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class IAmATeaPot(SanicException):
        pass
    assert 418 in _sanic_exceptions
    assert _sanic_exceptions[418] == IAmATeaPot
    assert _sanic_exceptions[418]().data == "IAmATeaPot"
    assert _sanic_exceptions[418]().status_code == 418
    # Test quiet
    assert _sanic_exceptions[418]().quiet == True  # quiet=True
    assert _sanic_exceptions[500]().quiet == False  # quiet=False
    assert _sanic_exceptions[400]().quiet == True  # quiet=None

# Generated at 2022-06-14 07:15:50.963242
# Unit test for function add_status_code
def test_add_status_code():
    class SanicInternalError400(SanicException):
        pass

    add_status_code(400)(SanicInternalError400)

    assert 400 in _sanic_exceptions

# Generated at 2022-06-14 07:15:54.325184
# Unit test for function add_status_code
def test_add_status_code():
    from sanic.exceptions import add_status_code

    @add_status_code(400)
    class TestException(Exception):
        pass

    assert TestException.status_code == 400


# Generated at 2022-06-14 07:16:00.423178
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class IAmATeaPot(SanicException):
        pass
    assert IAmATeaPot.status_code == 418
    assert IAmATeaPot().status_code == 418
    assert "418" in _sanic_exceptions

# Generated at 2022-06-14 07:16:11.389614
# Unit test for function add_status_code
def test_add_status_code():
    a = add_status_code(200)
    b = add_status_code(404, True)
    @a
    class InvalidUsage(SanicException):
        pass
    @b
    class NotFound(SanicException):
        pass
    assert InvalidUsage(message="InvalidUsage", status_code=200).status_code == 200
    assert InvalidUsage(message="InvalidUsage", status_code=200).quiet == False
    assert NotFound(message="NotFound", status_code=404).status_code == 404
    assert NotFound(message="NotFound", status_code=404).quiet == True


# Generated at 2022-06-14 07:16:16.382693
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(300)
    class HTTP300(SanicException):
        pass
    assert 300 in _sanic_exceptions
    assert _sanic_exceptions[300] == HTTP300
    assert HTTP300.status_code == 300
    assert HTTP300.quiet

# Generated at 2022-06-14 07:16:32.243597
# Unit test for function add_status_code
def test_add_status_code():
    # Test normal operation
    @add_status_code(123)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 123
    assert TestException.quiet == False
    assert _sanic_exceptions[123] == TestException

    # Test a code that's already present
    try:
        @add_status_code(404)
        class TestException1(SanicException):
            pass
    except KeyError:
        pass
    else:
        assert False

    # Test quiet=True
    @add_status_code(456, quiet=True)
    class TestException2(SanicException):
        pass
    assert TestException2.status_code == 456
    assert TestException2.quiet == True
    assert _sanic_exceptions[456] == TestException2

    # Test

# Generated at 2022-06-14 07:16:37.714759
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test the function add_status_code
    """
    @add_status_code(400)
    class Foo(SanicException):
        """
        **Status**: 400 Bad Request
        """
        pass

    assert Foo.status_code == 400


# Generated at 2022-06-14 07:16:49.614884
# Unit test for function add_status_code
def test_add_status_code():
    # add_status_code returns a function which decorates a class
    decorator = add_status_code(42)
    @decorator
    class Foo(SanicException):
        pass

    assert Foo.status_code == 42
    assert Foo.quiet  # Not 500
    assert _sanic_exceptions[42] is Foo

    class Bar(SanicException):
        pass
    Bar = decorator(Bar)

    assert Bar.status_code == 42
    assert Bar.quiet  # Not 500
    assert _sanic_exceptions[42] is Bar

    # If we do not get a status code when decorating the class,
    # it does not raise
    @add_status_code()
    class Foo2(SanicException):
        pass


# Generated at 2022-06-14 07:16:55.843990
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class CustomException(SanicException):
        pass

    try:
        raise CustomException()
    except CustomException as e:
        search_str = "CustomException: CustomException"
        assert search_str in str(e)
        assert 400 == e.status_code

# Generated at 2022-06-14 07:17:06.839828
# Unit test for function add_status_code
def test_add_status_code():
    class MySanicException(SanicException):
        pass

    add_status_code(404)(MySanicException)
    assert MySanicException.status_code == 404
    assert MySanicException.quiet

    add_status_code(500)(MySanicException)
    assert MySanicException.status_code == 500
    assert not MySanicException.quiet

    add_status_code(501, False)(MySanicException)
    assert MySanicException.status_code == 501
    assert not MySanicException.quiet

    add_status_code(502, True)(MySanicException)
    assert MySanicException.status_code == 502
    assert MySanicException.quiet

# Generated at 2022-06-14 07:17:19.028868
# Unit test for function add_status_code
def test_add_status_code():
    msg = "An error has occurred"
    status_code = 400

    @add_status_code(status_code)
    class Foo(SanicException):
        pass

    try:
        raise Foo(msg)
    # Test status_code
    except Foo as exc:
        assert(exc.status_code == status_code)
    # Test exception arguments
    except Exception as exc:
        assert(exc.args[0] == msg)

    try:
        abort(status_code)
    # Test status_code
    except Foo as exc:
        assert(exc.status_code == status_code)

    try:
        raise Foo(msg)
    except Foo as exc:
        assert(exc.quiet)



# Generated at 2022-06-14 07:17:25.206445
# Unit test for function add_status_code
def test_add_status_code():
    new_status_code_500 = 500
    new_sanic_exception = SanicException
    assert add_status_code(new_status_code_500, 1)(new_sanic_exception).status_code == new_status_code_500
    assert add_status_code(new_status_code_500, 1)(new_sanic_exception).quiet == 1


# Generated at 2022-06-14 07:17:27.008651
# Unit test for function add_status_code
def test_add_status_code():
    response = add_status_code(777)
    assert response.status_code == 777

# Generated at 2022-06-14 07:17:40.338208
# Unit test for function add_status_code
def test_add_status_code():
    if __name__ == "__main__":

        def test_func(*args, **kwargs):
            print("kwargs: ", kwargs)
            print("args: ", args)

        test_func(1, "3", a=1, b=2)
        # kwargs:  {'a': 1, 'b': 2}
        # args:  (1, '3')
        print("test_func's name is ", test_func.__name__)
        # test_func's name is  test_func


        # 简单装饰器
        def deco_func(func):
            def wrapper(*args, **kwargs):
                print("before call %s" % func.__name__)
                func(*args, **kwargs)

# Generated at 2022-06-14 07:17:43.139120
# Unit test for function add_status_code
def test_add_status_code():
    class NotFound(SanicException):
        """
        **Status**: 404 Not Found
        """
        pass

    assert NotFound.status_code == 404
    assert _sanic_exceptions.get(404) == NotFound

# Generated at 2022-06-14 07:17:58.340818
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class UserDoesNotExist(SanicException):
        pass

    exception_404 = UserDoesNotExist("User does not exist", status_code=404)
    
    assert _sanic_exceptions[404] == UserDoesNotExist
    assert exception_404.status_code == 404
    assert exception_404.quiet is True


# Generated at 2022-06-14 07:18:00.873942
# Unit test for function add_status_code
def test_add_status_code():
    class TestClass: pass
    exception = add_status_code(200)(TestClass)
    assert exception.status_code == 200

# Generated at 2022-06-14 07:18:09.680654
# Unit test for function add_status_code
def test_add_status_code():
    # Test to add an exception
    test_exc = add_status_code(510)(SanicException)()
    assert test_exc.status_code == 510
    assert test_exc.quiet is False
    # Test to add an exception with quiet=True
    test_exc = add_status_code(520, quiet=True)(SanicException)()
    assert test_exc.status_code == 520
    assert test_exc.quiet is True
    # Test to add an exception with 500 status code with quiet=None
    test_exc = add_status_code(500, quiet=None)(SanicException)()
    assert test_exc.status_code == 500
    assert test_exc.quiet is False
    # Test to add an exception with 500 status code with quiet=True

# Generated at 2022-06-14 07:18:12.625121
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestClass(SanicException):
        pass
    assert TestClass.status_code == 400

# Generated at 2022-06-14 07:18:17.533761
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class MyException(SanicException):
        pass

    ex = MyException("Test")
    assert ex.message == "Test"
    assert MyException.status_code == 200
    assert _sanic_exceptions[200] == MyException



# Generated at 2022-06-14 07:18:23.963271
# Unit test for function add_status_code
def test_add_status_code():
    def add_status_code(code):
        def decorator(cls):
            cls.code = code
            return cls
        return decorator

    @add_status_code(404)
    class NotFound(SanicException):
        pass

    assert hasattr(NotFound, "code")
    assert NotFound.code == 404

# Generated at 2022-06-14 07:18:25.677928
# Unit test for function add_status_code
def test_add_status_code():
    assert True

# Generated at 2022-06-14 07:18:28.856805
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class SomeException(SanicException):
        pass
    exception = SomeException('foo')
    assert exception.status_code == 123
    assert exception.quiet is False
    assert _sanic_exceptions[123] is SomeException

# Generated at 2022-06-14 07:18:33.028065
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(125)
    class ServerError125(SanicException):
        pass

    check = _sanic_exceptions[125]
    assert check == ServerError125
    assert check.status_code == 125
    # check.quiet = False

# Generated at 2022-06-14 07:18:38.021895
# Unit test for function add_status_code
def test_add_status_code():
    # Base class
    assert SanicException.status_code is None

    # test decorator
    @add_status_code(200)
    class A(SanicException):
        pass

    assert A.status_code == 200

# Generated at 2022-06-14 07:19:01.274603
# Unit test for function add_status_code
def test_add_status_code():

    code = 428
    expected = 'test_message'

    @add_status_code(code)
    class TestException(SanicException):
        """ Test Exception """
    try:
        raise TestException(expected)
    except TestException as e:
        assert e.message == expected
        assert e.status_code == code
        assert isinstance(e, SanicException)

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:19:04.475701
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestSanicException(SanicException):
        pass

    assert TestSanicException.status_code == 200
    assert TestSanicException.quiet is False

# Generated at 2022-06-14 07:19:07.358008
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class FooException:
        pass

    assert FooException.status_code == 123
    assert _sanic_exceptions[123] is FooException

# Generated at 2022-06-14 07:19:21.298910
# Unit test for function add_status_code
def test_add_status_code():
    def add_status_code_test(code, test_type):
        @add_status_code(code, quiet=test_type)
        class AddStatusCodeTest(SanicException):
            pass
        return AddStatusCodeTest
    assert add_status_code_test(404, None).status_code == 404
    assert add_status_code_test(404, None).quiet == True
    assert add_status_code_test(400, True).status_code == 400
    assert add_status_code_test(400, True).quiet == True
    assert add_status_code_test(405, False).status_code == 405
    assert add_status_code_test(405, False).quiet == False
    assert add_status_code_test(500, None).status_code == 500
    assert add_status_code_test

# Generated at 2022-06-14 07:19:25.644226
# Unit test for function add_status_code
def test_add_status_code():
    # Test for adding 200 status code
    @add_status_code(200)
    class Custom200(SanicException):
        pass

    assert 401 in _sanic_exceptions
    assert 200 in _sanic_exceptions


# Generated at 2022-06-14 07:19:35.155383
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(999)
    class NewException(SanicException):
        pass

    assert len(_sanic_exceptions) == 9
    assert _sanic_exceptions[999].status_code == 999
    assert NewException.status_code == 999
    assert NewException.__name__ == 'NewException'
    assert issubclass(NewException, SanicException)
    assert _sanic_exceptions[999] is NewException

    @add_status_code(100, True)
    class NewException(SanicException):
        pass

    assert NewException.quiet is True

    @add_status_code(100)
    class NewException(SanicException):
        pass

    assert NewException.quiet is False


# Generated at 2022-06-14 07:19:36.305698
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(123)(SanicException)
    assert 123 in _sanic_exceptions


# Generated at 2022-06-14 07:19:49.298243
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class SanicException400(SanicException):
        pass

    @add_status_code(401)
    class SanicException401(SanicException):
        pass

    @add_status_code(402)
    class SanicException402(SanicException):
        pass

    @add_status_code(403)
    class SanicException403(SanicException):
        pass

    @add_status_code(404)
    class SanicException404(SanicException):
        pass

    @add_status_code(405)
    class SanicException405(SanicException):
        pass

    @add_status_code(406)
    class SanicException406(SanicException):
        pass


# Generated at 2022-06-14 07:19:55.544331
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Test(SanicException):
        pass
    assert _sanic_exceptions[200] == Test

    @add_status_code(500)
    class Test(SanicException):
        pass
    assert _sanic_exceptions[500] is Test


# Generated at 2022-06-14 07:20:04.167542
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(502)
    class BadGateway(SanicException):
        pass

    assert _sanic_exceptions[502] is BadGateway

    # When the return value for a function is not used,
    # python warns that it might not be actually used.
    # This line is to disable that warning.
    assert add_status_code(status_code=505, quiet=True)(SanicException) is SanicException

# Generated at 2022-06-14 07:20:45.882775
# Unit test for function add_status_code
def test_add_status_code():
    sanic_exceptions = _sanic_exceptions

    @add_status_code(300)
    class MySanicException(SanicException):
        pass

    assert MySanicException.status_code == 300
    assert sanic_exceptions[300] == MySanicException
    assert MySanicException.quiet is False

    @add_status_code(301, quiet=True)
    class MySanicException2(SanicException):
        pass

    assert MySanicException2.status_code == 301
    assert sanic_exceptions[301] == MySanicException2
    assert MySanicException2.quiet is True

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:20:53.265819
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418, quiet=True)
    class IAmATeaPotException(SanicException):
        pass

    assert IAmATeaPotException.status_code == 418
    assert IAmATeaPotException.quiet is True
    assert IAmATeaPotException('').status_code == 418
    assert IAmATeaPotException('').quiet is True

# Generated at 2022-06-14 07:20:59.713181
# Unit test for function add_status_code
def test_add_status_code():
    """
    Unit test for function add_status_code.
    """
    def class_decorator(cls):
        cls.status_code = 123
        _sanic_exceptions[123] = cls
        return cls

    assert add_status_code(123)(class_decorator)(NotFound) == NotFound

# Generated at 2022-06-14 07:21:05.798773
# Unit test for function add_status_code
def test_add_status_code():
    # Fails because status_code is not defined
    try:
        add_status_code(400)
    except Exception as e:
        if "status_code" not in str(e):
            raise Exception("error message should contain 'status_code'")

    @add_status_code(400)
    class InvalidUsage(SanicException):
        pass

    InvalidUsage.status_code
    InvalidUsage().status_code


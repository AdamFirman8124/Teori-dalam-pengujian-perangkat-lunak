

# Generated at 2022-06-14 07:11:22.136577
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(601)
    class MyException(SanicException):
        pass

    MyException.status_code == 601

# Generated at 2022-06-14 07:11:25.005233
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class HelloWorld(SanicException):
        pass
    assert 201 in _sanic_exceptions.keys()


# Generated at 2022-06-14 07:11:37.304139
# Unit test for function add_status_code
def test_add_status_code():
    """
    add_status_code is used as a decorator to add status code to SanicException
    """
    @add_status_code(400)
    class BadRequest(SanicException):
        """
        **Status**: 400 Bad Request
        """
    assert BadRequest.status_code == 400
    assert BadRequest.quiet == True
    assert _sanic_exceptions[400].__name__ == 'BadRequest'

    @add_status_code(500, quiet = True)
    class ServerError(SanicException):
        """
        **Status**: 500 Internal Server Error
        """
    assert ServerError.status_code == 500
    assert ServerError.quiet == True
    assert _sanic_exceptions[500].__name__ == 'ServerError'


# Generated at 2022-06-14 07:11:42.052196
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(code=401, quiet=False)
    class Exc(SanicException):
        pass

    assert Exc.status_code == 401
    assert Exc.quiet == False
    assert 401 in _sanic_exceptions

# Generated at 2022-06-14 07:11:51.589121
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(202)
    class TestException(SanicException):
        pass
    
    assert TestException.status_code == 202
    assert TestException.quiet == None
    assert _sanic_exceptions[202] == TestException
    
    @add_status_code(403, quiet=False)
    class TestException2(SanicException):
        pass
    
    assert TestException2.status_code == 403
    assert TestException2.quiet == False
    assert _sanic_exceptions[403] == TestException2

# Generated at 2022-06-14 07:11:54.261574
# Unit test for function add_status_code
def test_add_status_code():
    class OK(SanicException):
        pass

    add_status_code(200)(OK)

    assert OK.status_code == 200
    assert OK.quiet is True

# Generated at 2022-06-14 07:12:07.760732
# Unit test for function add_status_code
def test_add_status_code():
    Error1 = add_status_code(200)(SanicException)
    Error2 = add_status_code(201, quiet=True)(SanicException)
    Error3 = add_status_code(202, quiet=False)(SanicException)
    Error4 = add_status_code(203)(SanicException)

    # check if the class has our custom fields
    assert Error1.status_code == 200
    assert not hasattr(Error1, "quiet")
    assert Error2.status_code == 201
    assert Error2.quiet
    assert Error3.status_code == 202
    assert not Error3.quiet
    assert Error4.status_code == 203
    assert Error4.quiet

    # Check the registry
    assert _sanic_exceptions.get(200) == Error1
    assert _sanic_exceptions.get

# Generated at 2022-06-14 07:12:17.303977
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class ERROR(SanicException):
        pass

    assert ERROR.status_code == 500
    assert ERROR.quiet is None
    assert ServerError.status_code == 500
    assert ServerError.quiet is None
    assert ERROR in _sanic_exceptions
    # Test the new status code exception are required to be of SanicException Type
    with pytest.raises(TypeError):
        @add_status_code(400)
        class TEST(Exception):
            pass

# Generated at 2022-06-14 07:12:22.541584
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyException(SanicException):
        pass
    exception = MyException("Bad Request")
    assert exception.status_code == 400
    assert exception.quiet == True
    exception2 = MyException("Bad Request", quiet=False)
    assert exception2.quiet == False


# Generated at 2022-06-14 07:12:25.782243
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class TestException(SanicException):
        pass
    assert _sanic_exceptions[100] == TestException
    assert _sanic_exceptions[100]().message == ''

# Generated at 2022-06-14 07:12:32.721144
# Unit test for function add_status_code
def test_add_status_code():
    from sanic.exceptions import _sanic_exceptions

    assert _sanic_exceptions[404] == NotFound
    assert _sanic_exceptions[408] == RequestTimeout
    assert _sanic_exceptions[413] == PayloadTooLarge
    assert _sanic_exceptions[500] == ServerError
    assert _sanic_exceptions[503] == ServiceUnavailable



# Generated at 2022-06-14 07:12:39.982166
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestException(SanicException):
        pass

    assert type(TestException(404, "Error")) == TestException
    assert isinstance(TestException(404, "Error"), SanicException)
    assert TestException(404, "Error").status_code == 200
    assert TestException(404, "Error").message == "Error"

# Generated at 2022-06-14 07:12:49.407077
# Unit test for function add_status_code
def test_add_status_code():
    def foo(cls):
        cls.status_code = 3000
        cls.quiet = False
        _sanic_exceptions[3000] = cls
        return cls

    @foo
    class Bar(SanicException):
        pass

    @add_status_code(3001, quiet=True)
    class Bar2(SanicException):
        pass

    @add_status_code(3002)
    class Bar3(SanicException):
        pass

    assert (Bar().status_code == 3000)
    assert (_sanic_exceptions.get(3000, None) == Bar)
    assert (Bar().quiet == False)

    assert (Bar2().status_code == 3001)
    assert (_sanic_exceptions.get(3001, None) == Bar2)

# Generated at 2022-06-14 07:12:52.721783
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestClass(SanicException):
        pass
    assert TestClass.status_code == 400

# Generated at 2022-06-14 07:13:03.362633
# Unit test for function add_status_code
def test_add_status_code():
    # class Foo(Exception):
    #     pass
    # add_status_code(400)(Foo)
    # assert _sanic_exceptions[400] == Foo
    # try:
    #     raise Foo()
    # except SanicException:
    #     pass
    # else:
    #     assert False

    class Foo2(SanicException):
        pass
    add_status_code(400)(Foo2)
    assert _sanic_exceptions[400] == Foo2
    try:
        raise Foo2()
    except SanicException:
        pass
    else:
        assert False



# Generated at 2022-06-14 07:13:07.603948
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(142)
    class Foo(SanicException):
        pass
    foo_obj = Foo("message", quiet=True)
    assert foo_obj.status_code == 142
    assert foo_obj.quiet == True
    assert _sanic_exceptions[142] == Foo

# Generated at 2022-06-14 07:13:20.873028
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test add_status_code function

    AssertionError: Expected 1 to be 4
    AssertionError: Expected False to be True

    :return:
    """
    # test the decorator

    @add_status_code(404)
    class NullClass:
        pass

    assert NullClass.status_code == 4
    assert NullClass.quiet is False

    @add_status_code(404, True)
    class NullClass2:
        pass

    assert NullClass2.status_code == 4
    assert NullClass2.quiet

    @add_status_code(500, False)
    class NullClass3:
        pass

    assert NullClass3.status_code == 5
    assert NullClass3.quiet is False


# Generated at 2022-06-14 07:13:28.378077
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class InvalidUsage(SanicException):
        """
        **Status**: 400 Bad Request
        """

        pass

    assert InvalidUsage.status_code == 400
    assert InvalidUsage.__doc__ == "**Status**: 400 Bad Request"
    assert 400 in _sanic_exceptions
    assert isinstance(_sanic_exceptions[400], InvalidUsage)
    assert issubclass(SanicException, Exception)


# Generated at 2022-06-14 07:13:33.172851
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class TestException(SanicException):
        pass

    exception = TestException("test message")
    assert exception.message == "test message"
    assert exception.status_code == 201
    assert _sanic_exceptions[201] is TestException

# Generated at 2022-06-14 07:13:38.129604
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Test(SanicException):
        pass

    test = Test('Hello')
    assert test.status_code == 200
    assert test.quiet is False
    assert test.message == 'Hello'

# Generated at 2022-06-14 07:13:46.971706
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(501)
    class NotImplemented(SanicException):
        pass
    assert NotImplemented.status_code == 501
    assert _sanic_exceptions[501] == NotImplemented

# Generated at 2022-06-14 07:13:51.485869
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass
    
    add_status_code(400)(TestException)
    exception = TestException("message")
    assert exception.status_code == 400
    assert _sanic_exceptions[400] == TestException

# Generated at 2022-06-14 07:14:01.833534
# Unit test for function add_status_code
def test_add_status_code():
    # add_status_code should add an exception to _sanic_exceptions and set the
    # status_code attribute
    @add_status_code(501)
    class NotImplemented(SanicException):
        pass

    assert isinstance(_sanic_exceptions[501], NotImplemented)
    assert _sanic_exceptions[501].status_code == 501

    # reusing an existing status_code should raise an exception.
    with pytest.raises(Exception):
        @add_status_code(500)
        class InternalServerError(SanicException):
            pass

# Generated at 2022-06-14 07:14:14.244868
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(code=400)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 400
    assert TestException.quiet is True
    assert 400 in _sanic_exceptions

    # Test adding status code and setting quiet manually
    @add_status_code(code=401, quiet=True)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 401
    assert TestException.quiet is True
    assert 401 in _sanic_exceptions

    # Test adding status code and setting quiet manually
    @add_status_code(code=402, quiet=False)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 402
    assert TestException.quiet is False
    assert 402 in _sanic_ex

# Generated at 2022-06-14 07:14:26.512340
# Unit test for function add_status_code
def test_add_status_code():
    class TestBase(Exception):
        pass
        # quiet=True will set the property of SanicException
        # as quiet = True
    @add_status_code(123, quiet=True)
    class TestException(TestBase):
        pass
    assert issubclass(TestException, Exception)
    assert issubclass(TestException, TestBase)
    assert issubclass(TestException, SanicException)
    assert TestException.status_code == 123
    assert TestException.quiet == True
    assert TestException.__name__ == "TestException"
    assert TestException.__doc__ == ""
    assert TestException.__module__ == __name__ 


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:14:30.673094
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class OauthCallback(SanicException):
        pass
    assert OauthCallback.status_code == 201
    assert OauthCallback.quiet == None
    assert _sanic_exceptions[201] == OauthCallback
    assert not 201 in _sanic_exceptions



# Generated at 2022-06-14 07:14:39.727832
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    class MyException2(SanicException):
        pass

    class MyException3(SanicException):
        pass

    add_status_code(404)(MyException)
    add_status_code(404, quiet=True)(MyException2)
    add_status_code(500)(MyException3)
    assert _sanic_exceptions[404] == MyException
    assert _sanic_exceptions[404] == MyException2
    assert _sanic_exceptions[500] == MyException3

# Generated at 2022-06-14 07:14:44.037240
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class FooException(SanicException):
        pass
    assert _sanic_exceptions[123] is FooException

test_add_status_code()

# Generated at 2022-06-14 07:14:56.142233
# Unit test for function add_status_code
def test_add_status_code():
    class NewException(SanicException):
        pass

    assert NewException not in _sanic_exceptions
    assert 500 in _sanic_exceptions
    assert isinstance(_sanic_exceptions[500], ServerError)

    add_status_code(350)(NewException)

    assert 350 in _sanic_exceptions
    assert isinstance(_sanic_exceptions[350], NewException)
    assert _sanic_exceptions[350].status_code == 350
    assert _sanic_exceptions[350].quiet is False

    add_status_code(350, quiet=False)(NewException)

    assert 350 in _sanic_exceptions
    assert isinstance(_sanic_exceptions[350], NewException)
    assert _sanic_exceptions[350].status_code == 350

# Generated at 2022-06-14 07:15:01.120177
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class MyException(SanicException):
        pass

    assert MyException.status_code == 404
    assert _sanic_exceptions[404] == MyException
    assert _sanic_exceptions == {404: MyException}


# Generated at 2022-06-14 07:15:11.708471
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(401)
    class Unauthorized(SanicException): pass
    assert 401 in _sanic_exceptions
    assert _sanic_exceptions[401] is Unauthorized

# Generated at 2022-06-14 07:15:15.823291
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(203)
    class CustomException(SanicException):
        pass

    assert _sanic_exceptions[203] is CustomException
    assert CustomException().status_code == 203



# Generated at 2022-06-14 07:15:18.962070
# Unit test for function add_status_code
def test_add_status_code():
    from sanic.exceptions import SanicException

    SanicException = add_status_code(404)(SanicException)
    assert SanicException.status_code == 404
    assert SanicException.quiet == True

# Generated at 2022-06-14 07:15:23.766823
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class TestException(SanicException):
        pass

    e = TestException('message')
    assert e.status_code == 201
    assert _sanic_exceptions.get(201) == TestException


# Generated at 2022-06-14 07:15:28.345686
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyException(SanicException):
        pass

    assert _sanic_exceptions[400] == MyException
    assert issubclass(MyException, SanicException)



# Generated at 2022-06-14 07:15:37.704226
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test add_status_code
    """
    import inspect

    msg = "Test Exception"
    status_code = 999
    test_exception = add_status_code(status_code)(SanicException)
    assert issubclass(test_exception, SanicException)

    instance = test_exception(msg)
    signature = inspect.signature(SanicException.__init__)
    assert set(signature.parameters) == set(instance.__dict__.keys())
    assert instance.status_code == status_code
    assert instance.message == msg
    assert str(instance) == f"{msg}"

    with pytest.raises(test_exception) as err:
        raise test_exception(msg)
    assert err.value.status_code == status_code



# Generated at 2022-06-14 07:15:48.454711
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class Success(SanicException):
        pass

    from sanic.server import Server
    server = Server()
    server.app.error_handler.add(Success, lambda req, res, exception: res)

    req, res = server.app.test_client.get("/")
    try:
        raise Success("Created")
    except SanicException as e:
        server.app.error_handler.default(req, res, e)
    assert res.status == 201
    assert res.body == b"Created"
    assert res.headers["Content-Length"] == "7"

# Generated at 2022-06-14 07:15:57.084431
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class MyExc(SanicException):
        pass
    assert _sanic_exceptions[200] is MyExc
    try:
        raise MyExc("Test")
    except SanicException as e:
        assert e.status_code == 200
        assert str(e) == "Test"

    assert MyExc.status_code == 200
    assert MyExc.quiet is False

    @add_status_code(200, quiet=False)
    class MyExc(SanicException):
        pass
    assert MyExc.status_code == 200
    assert MyExc.quiet is False

    @add_status_code(200, quiet=True)
    class MyExc(SanicException):
        pass
    assert MyExc.status_code == 200
    assert MyExc.quiet is True


# Generated at 2022-06-14 07:15:59.088075
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class SanicException500(SanicException):
        pass

    assert ServerError == _sanic_exceptions[500]

# Generated at 2022-06-14 07:16:02.689024
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(Exception):
        pass

    add_status_code(test_1=400)(TestException)
    assert _sanic_exceptions[400] == TestException

# Generated at 2022-06-14 07:16:23.369491
# Unit test for function add_status_code
def test_add_status_code():
    d = {}
    def test_decorator(func):
        def wrapper(*args, **kwargs):
            return d
        return wrapper

    @test_decorator
    def test_function():
        pass

    assert test_function() == d

# Generated at 2022-06-14 07:16:28.067412
# Unit test for function add_status_code
def test_add_status_code():

    @add_status_code(400)
    class BadRequest(SanicException):
        """
        **Status**: 400 Bad Request
        """

        pass

    assert _sanic_exceptions.get(400).__name__ == 'BadRequest'



# Generated at 2022-06-14 07:16:38.613606
# Unit test for function add_status_code
def test_add_status_code():
    """
    Testing class add_status_code.
    """
    @add_status_code(status_code=200)
    class TestAddStatusCode(SanicException):
        pass

    assert TestAddStatusCode().status_code == 200
    assert TestAddStatusCode().quiet == True

    @add_status_code(status_code=500)
    class TestAddStatusCode(SanicException):
        pass

    assert TestAddStatusCode().status_code == 500
    assert TestAddStatusCode().quiet == False

    @add_status_code(status_code=418, quiet=False)
    class TestAddStatusCode(SanicException):
        pass

    assert TestAddStatusCode().status_code == 418
    assert TestAddStatusCode().quiet == False


# Generated at 2022-06-14 07:16:47.729430
# Unit test for function add_status_code
def test_add_status_code():
    # test for basic add status code
    @add_status_code(543)
    class TestClass(SanicException):
        pass
    assert _sanic_exceptions[543] == TestClass
    assert _sanic_exceptions[543](message="hello").status_code == 543
    assert _sanic_exceptions[543](message="hello").message == "hello"
    # test for quiet status code
    @add_status_code(543, quiet=True)
    class TestClass2(SanicException):
        pass
    assert _sanic_exceptions[543] == TestClass2
    assert _sanic_exceptions[543](message="hello").status_code == 543
    assert _sanic_exceptions[543](message="hello").message == "hello"
    assert _san

# Generated at 2022-06-14 07:16:55.655147
# Unit test for function add_status_code
def test_add_status_code():
    class Test1(SanicException):
        pass
    class Test2(SanicException):
        pass

    add_status_code(status_code=400)(Test1)
    assert Test1.status_code == 400
    assert Test1.quiet == False
    assert _sanic_exceptions[400] is Test1

    add_status_code(status_code=500)(Test2)
    assert Test2.status_code == 500
    assert Test2.quiet == True
    assert _sanic_exceptions[500] is Test2


# Generated at 2022-06-14 07:16:59.632668
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class success(SanicException):
        pass

    assert success.status_code == 200
    assert _sanic_exceptions[200] == success


# Generated at 2022-06-14 07:17:07.134753
# Unit test for function add_status_code
def test_add_status_code():
    def MyException1(SanicException):
        pass
    def MyException2(SanicException):
        pass

    assert add_status_code(100)(MyException1).status_code == 100
    assert add_status_code(200, quiet=True)(MyException2).quiet is True
    assert add_status_code(300)(MyException1).quiet is False
    assert add_status_code(400)(MyException1).quiet is True
    assert add_status_code(500)(MyException1).quiet is False

# Generated at 2022-06-14 07:17:19.987554
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test the functionality of the add_status_code decorator.
    """
    # Verify that a class is added to the _sanic_exceptions dict
    assert 200 not in _sanic_exceptions

    @add_status_code(200)
    class _TestClass(Exception):
        pass

    assert 200 in _sanic_exceptions

    # Verify that the exception class has the correct attributes
    exc = _TestClass()
    assert exc.status_code == 200
    assert exc.quiet == False

    # Verify that quiet=False is overruled by status_code=500
    @add_status_code(500, quiet=False)
    class _TestClass2(Exception):
        pass

    exc = _TestClass2()
    assert exc.status_code == 500
    assert exc.quiet == True

    # Verify that

# Generated at 2022-06-14 07:17:25.425959
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class IAmATeapot(SanicException):
        pass

    assert _sanic_exceptions[418] == IAmATeapot
    assert hasattr(IAmATeapot, "status_code")
    assert IAmATeapot.status_code == 418

# Generated at 2022-06-14 07:17:29.914068
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 200
    assert TestException.quiet is False

    @add_status_code(200, True)
    class TestException2(SanicException):
        pass

    assert TestException2.status_code == 200
    assert TestException2.quiet is True

# Generated at 2022-06-14 07:18:07.760830
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(1)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions == {1: TestException}

    @add_status_code(2)
    class TestException2(SanicException):
        pass

    assert _sanic_exceptions == {1: TestException, 2: TestException2}

    del _sanic_exceptions[1]
    del _sanic_exceptions[2]

# Generated at 2022-06-14 07:18:12.008148
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyException(SanicException):
        pass

    assert 400 in _sanic_exceptions
    assert _sanic_exceptions[400] == MyException



# Generated at 2022-06-14 07:18:21.551063
# Unit test for function add_status_code
def test_add_status_code():
    """
    Verify that the units correctly create exceptions
    with the correct status code.
    """

    # 200
    class HTTPOk(SanicException):
        pass

    # 300
    class HTTPRedirect(SanicException):
        pass

    @add_status_code(404)
    class HTTPNotFound(SanicException):
        pass

    # 400
    class HTTPBadRequest(SanicException):
        pass

    # 500
    class HTTPServerError(SanicException):
        pass

    # Testing non status code
    class HTTPUnknown(SanicException):
        pass

    assert _sanic_exceptions[200] == HTTPOk
    assert _sanic_exceptions[404] == HTTPNotFound
    assert _sanic_exceptions[500] == HTTPServerError

    assert HTTPOk.status_code is 200


# Generated at 2022-06-14 07:18:27.146738
# Unit test for function add_status_code
def test_add_status_code():

    @add_status_code(401)
    class Unauthorized(SanicException):
        pass

    assert Unauthorized.status_code == 401
    assert _sanic_exceptions[401] == Unauthorized
    assert Unauthorized("").status_code == 401
    assert Unauthorized("").message == ""



# Generated at 2022-06-14 07:18:33.035151
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(code=200)
    class Test(SanicException):
        pass
    assert 200 in _sanic_exceptions
    assert _sanic_exceptions[200] == Test

    with pytest.raises(SanicException) as e:
        raise _sanic_exceptions[200]('Test')
    assert e.value.status_code == 200
    assert e.value.message == 'Test'
    assert e.value.headers is None
    assert e.value.quiet is False is e.value.is_quiet

    with pytest.raises(SanicException) as e:
        raise _sanic_exceptions[200]('Test', headers={'Test header': 'Test header value'})
    assert e.value.status_code == 200
    assert e.value.message == 'Test'

# Generated at 2022-06-14 07:18:46.730279
# Unit test for function add_status_code
def test_add_status_code():
    class FooException(SanicException):
        pass

    assert FooException.status_code is None
    assert not hasattr(FooException, "quiet")

    add_status_code(400)(FooException)

    assert FooException.status_code == 400
    assert FooException.quiet is True

    add_status_code(500)(FooException)

    assert FooException.status_code == 500
    assert FooException.quiet is False

    add_status_code(200, quiet=True)(FooException)

    assert FooException.status_code == 200
    assert FooException.quiet is True

    add_status_code(200, quiet=False)(FooException)

    assert FooException.status_code == 200
    assert FooException.quiet is False

# Generated at 2022-06-14 07:18:59.599194
# Unit test for function add_status_code
def test_add_status_code():
    # Test for status code 404
    assert _sanic_exceptions[404].status_code == 404
    assert _sanic_exceptions[404].quiet == True
    assert _sanic_exceptions[404].__name__ == "NotFound"

    # Test for status code 400
    assert _sanic_exceptions[400].status_code == 400
    assert _sanic_exceptions[400].quiet == True
    assert _sanic_exceptions[400].__name__ == "InvalidUsage"

    # Test for status code 405
    assert _sanic_exceptions[405].status_code == 405
    assert _sanic_exceptions[405].quiet == True
    assert _sanic_exceptions[405].__name__ == "MethodNotSupported"

    # Test for status code 500

# Generated at 2022-06-14 07:19:04.821353
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123, quiet=True)
    class DerivedException(SanicException):
        pass

    assert DerivedException.status_code == 123
    assert DerivedException.quiet == True
    assert issubclass(DerivedException, SanicException)
    assert DerivedException in _sanic_exceptions.values()



# Generated at 2022-06-14 07:19:11.674574
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Testing(SanicException):
        pass

    assert Testing.status_code == 200
    assert Testing.quiet is True

    @add_status_code(500)
    class Testing(SanicException):
        pass

    assert Testing.status_code == 500
    assert Testing.quiet is False

    @add_status_code(500, quiet=True)
    class Testing(SanicException):
        pass

    assert Testing.status_code == 500
    assert Testing.quiet is True

# Generated at 2022-06-14 07:19:18.206299
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class DummyException(SanicException):
        pass
    exc = DummyException("dummy", 200)
    assert exc.status_code == 200
    assert exc.message == "dummy"
    assert exc.headers == {}
    assert exc.quiet == True
    assert _sanic_exceptions[200] == DummyException

# Generated at 2022-06-14 07:20:32.425691
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestOK(SanicException):
        pass

    @add_status_code(200, quiet=True)
    class TestOK2(SanicException):
        pass

    @add_status_code(500, quiet=True)
    class TestServerError(SanicException):
        pass

    @add_status_code(500, quiet=False)
    class TestServerError2(SanicException):
        pass

    assert issubclass(TestOK, SanicException)
    assert issubclass(TestOK2, SanicException)
    assert issubclass(TestServerError, SanicException)
    assert issubclass(TestServerError2, SanicException)

    assert isinstance(TestOK(), SanicException)
    assert isinstance(TestOK2(), SanicException)


# Generated at 2022-06-14 07:20:34.766579
# Unit test for function add_status_code
def test_add_status_code():
    class CustomException(SanicException):
        pass

    assert CustomException.status_code == 500



# Generated at 2022-06-14 07:20:38.319053
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class DummyException(SanicException):
        pass

    assert "DummyException" in str(_sanic_exceptions.get(400))

# Generated at 2022-06-14 07:20:43.439464
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(202)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[202].__name__ == 'TestException'
    assert _sanic_exceptions[202]().status_code == 202


# Generated at 2022-06-14 07:20:56.904841
# Unit test for function add_status_code
def test_add_status_code():
    # test adding new status code to sanic_exceptions
    @add_status_code(401)
    class Ex1(SanicException):
        pass

    assert 401 in _sanic_exceptions
    assert _sanic_exceptions[401] == Ex1

    # test adding new status code to sanic_exceptions which already contains status code
    @add_status_code(404)
    class Ex2(SanicException):
        pass

    assert 404 in _sanic_exceptions
    assert _sanic_exceptions[404] == NotFound

    # test adding new status code to sanic_exceptions and changing status code
    @add_status_code(301)
    class Ex3(SanicException):
        pass

    assert 301 in _sanic_exceptions
    assert _sanic_exceptions[301] == Ex

# Generated at 2022-06-14 07:21:03.945595
# Unit test for function add_status_code
def test_add_status_code():
    class CustomException(SanicException):
        pass

    add_status_code(402)(CustomException)

    assert isinstance(CustomException(), SanicException)
    assert CustomException.status_code == 402
    assert CustomException.message == "CustomException"
    assert _sanic_exceptions[402] is CustomException

    exc = CustomException(message="foo")
    assert exc.status_code == 402
    assert exc.message == "foo"

# Generated at 2022-06-14 07:21:08.479477
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(501)
    class NotImplemented(SanicException):
        pass

    assert _sanic_exceptions[501] == NotImplemented

# Generated at 2022-06-14 07:21:12.304706
# Unit test for function add_status_code
def test_add_status_code():
    exception = add_status_code(9999)
    assert callable(exception)
    exception = exception(SanicException)
    assert exception.status_code == 9999
    assert exception not in _sanic_exceptions


# Generated at 2022-06-14 07:11:25.171241
# Unit test for function add_status_code
def test_add_status_code():
    # Test the default quiet argument
    assert_raises(SanicException, SanicException, message="Foo", status_code=500)
    assert_raises(ServerError, ServerError, message="Foo", status_code=500)
    assert_raises(NotFound, NotFound, message="Foo", status_code=404)

    # Test quiet argument with values True and False
    assert_raises(SanicException, SanicException, message="Foo", status_code=403, quiet=True)
    assert_raises(SanicException, SanicException, message="Foo", status_code=403, quiet=False)
    assert_raises(Forbidden, Forbidden, message="Foo", status_code=403, quiet=True)

# Generated at 2022-06-14 07:11:32.304601
# Unit test for function add_status_code
def test_add_status_code():
    def my_class_decorator(cls):
        cls.status_code = code
        if quiet or quiet is None and code != 500:
            cls.quiet = True
        _sanic_exceptions[code] = cls
        return cls

    #testing for add_status_code
    code = 404
    quiet = None
    my_class = add_status_code(404)
    assert my_class == my_class_decorator

# Generated at 2022-06-14 07:11:38.472279
# Unit test for function add_status_code
def test_add_status_code():
    # Test that add_status_code adds the specified status code
    class TestException(SanicException):
        pass

    add_status_code(555)(TestException)
    assert TestException.status_code == 555
    assert _sanic_exceptions[555] == TestException


# Generated at 2022-06-14 07:11:51.770725
# Unit test for function add_status_code
def test_add_status_code():
    assert add_status_code(100) is class_decorator
    assert add_status_code(100, quiet=True) is class_decorator
    assert not hasattr(_sanic_exceptions, 100)

    @add_status_code(101)
    class Sanic101(SanicException):
        pass

    assert _sanic_exceptions[101] is Sanic101
    assert not hasattr(Sanic101, "quiet")
    assert _sanic_exceptions[101](message="Sanic101").quiet == True

    @add_status_code(102, quiet=True)
    class Sanic102(SanicException):
        pass

    assert _sanic_exceptions[102] is Sanic102
    assert Sanic102(message="Sanic102").quiet == True

# Generated at 2022-06-14 07:12:05.363364
# Unit test for function add_status_code
def test_add_status_code():
    class A(SanicException):
        pass

    class B(SanicException):
        pass

    class C(SanicException):
        pass

    add_status_code(400)(A)
    add_status_code(410)(B)
    add_status_code(410, quiet=True)(C)

    assert _sanic_exceptions[410] == B
    assert B.status_code == 410
    assert B().status_code == 410
    assert _sanic_exceptions[410] is C
    assert C.status_code == 410
    assert C().status_code == 410
    assert C.quiet == True

# Generated at 2022-06-14 07:12:08.105078
# Unit test for function add_status_code
def test_add_status_code():
    new_exception = add_status_code(600)(SanicException)
    code, message = new_exception()
    assert code == 600
    assert message == "None"

# Generated at 2022-06-14 07:12:16.721040
# Unit test for function add_status_code
def test_add_status_code():
    # Call add_status_code with a valid status code to add a new SanicException
    # class
    invalid_usage_status_code = 400
    add_status_code(invalid_usage_status_code)
    assert isinstance(_sanic_exceptions.get(invalid_usage_status_code), SanicException)

    # Call add_status_code with a status code to modify the existing SanicException
    not_found_status_code = 404
    add_status_code(not_found_status_code)
    assert NotFound == _sanic_exceptions.get(not_found_status_code)

    # Call add_status_code with a status code SanicException does not have
    server_error_status_code = 501
    add_status_code(server_error_status_code)

# Generated at 2022-06-14 07:12:29.006468
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Test_1(SanicException):
        pass

    @add_status_code(200, True)
    class Test_2(SanicException):
        pass

    @add_status_code(500, True)
    class Test_3(SanicException):
        pass

    @add_status_code(500, False)
    class Test_4(SanicException):
        pass

    assert Test_1.status_code == 200
    assert Test_1.quiet is False
    assert Test_2.status_code == 200
    assert Test_2.quiet is True
    assert Test_3.status_code == 500
    assert Test_3.quiet is True
    assert Test_4.status_code == 500
    assert Test_4.quiet is False


# Generated at 2022-06-14 07:12:31.843506
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(600)
    class TestClass(SanicException):
        pass
    assert TestClass.status_code == 600
    assert TestClass.__init__.__annotations__ == {}



# Generated at 2022-06-14 07:12:43.524750
# Unit test for constructor of class Unauthorized
def test_Unauthorized():
    message = "Authentication required"
    scheme = "Bearer"
    realm = "Restricted Area"
    exception = Unauthorized(message, scheme, realm)
    assert exception.headers["WWW-Authenticate"] == "Bearer realm=Restricted Area"

    # OpenID Connect (OIDC)
    # 'scope' is an OIDC extension to the HTTP authentication framework.
    # http://openid.net/specs/openid-connect-core-1_0.html#AuthError
    exception = Unauthorized(message, scheme, realm, scope="openid profile")
    assert exception.headers["WWW-Authenticate"] == "Bearer realm=Restricted Area scope=openid profile"

# Generated at 2022-06-14 07:12:49.331347
# Unit test for function add_status_code
def test_add_status_code():
    # Make sure SanicException is returned when code is not found
    assert isinstance(abort(100), SanicException)
    # Make sure we can match server errors with a given code
    assert isinstance(abort(404), NotFound)

# Generated at 2022-06-14 07:12:53.665943
# Unit test for function add_status_code
def test_add_status_code():
    class ExceptionClass(SanicException):
        pass

    ExceptionClass = add_status_code(123, quiet=True)(ExceptionClass)
    assert ExceptionClass.status_code == 123
    assert ExceptionClass.quiet is True

# Generated at 2022-06-14 07:13:05.030290
# Unit test for function add_status_code
def test_add_status_code():
    # Set up Status code 1, 100, 200, 400, 500, 501
    # Set up SanicException class, ServerException subclass

    # test Status code 1, 100, 200, 400, 500, 501 add to _sanic_exceptions
    assert _sanic_exceptions[1].status_code == 1
    assert _sanic_exceptions[100].status_code == 100
    assert _sanic_exceptions[200].status_code == 200
    assert _sanic_exceptions[400].status_code == 400
    assert _sanic_exceptions[500].status_code == 500
    assert _sanic_exceptions[501].status_code == 501

    # Raise exception

# Generated at 2022-06-14 07:13:08.127584
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    add_status_code(400)(MyException)
    assert _sanic_exceptions[400] == MyException

# Generated at 2022-06-14 07:13:16.511608
# Unit test for function add_status_code
def test_add_status_code():
    # type: () -> None
    @add_status_code(status_code=200)
    class OK(SanicException):
        pass
    assert 200 in _sanic_exceptions
    assert "OK" == _sanic_exceptions[200].__name__
    assert True is _sanic_exceptions[200].quiet
    assert not hasattr(_sanic_exceptions[200].headers, "Allow")



# Generated at 2022-06-14 07:13:24.694864
# Unit test for function add_status_code
def test_add_status_code():
    assert _sanic_exceptions == {}

    @add_status_code(500)
    class TestClass(SanicException):
        pass

    class SanicExceptionSubclass(SanicException):
        pass

    with pytest.raises(TypeError):
        add_status_code(500)(SanicExceptionSubclass)

    assert TestClass.status_code == 500
    assert 500 in _sanic_exceptions
    assert isinstance(_sanic_exceptions[500], type)

    # Assert that the add_status_code decorator works on
    # Inherited classes
    @add_status_code(503)
    class TestClassSubclass(TestClass):
        pass
    assert TestClassSubclass.status_code == 503
    assert 503 in _sanic_exceptions

# Generated at 2022-06-14 07:13:37.479824
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class MyServerError1(Exception):
        pass
    assert 500 in _sanic_exceptions
    assert _sanic_exceptions[500] == MyServerError1

    @add_status_code(501)
    class MyServerError2(Exception):
        pass
    assert 501 in _sanic_exceptions
    assert _sanic_exceptions[501] == MyServerError2

    @add_status_code(500, quiet=True)
    class MyServerError3(Exception):
        pass
    assert _sanic_exceptions[500].quiet

    @add_status_code(501, quiet=True)
    class MyServerError4(Exception):
        pass
    assert _sanic_exceptions[501].quiet


# Generated at 2022-06-14 07:13:40.462446
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class MyException(SanicException):
        pass

    MyException() == SanicException()

# Generated at 2022-06-14 07:13:44.777126
# Unit test for function add_status_code
def test_add_status_code():
    with pytest.raises(Exception) as excinfo:
        @add_status_code(111)
        class Abcd(SanicException):
            pass
    assert excinfo._excinfo[0].__name__ == "AssertionError"

# Generated at 2022-06-14 07:13:50.056511
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass
    test_status = 400
    TestException = add_status_code(test_status)(TestException)
    exception = TestException("test message")
    assert exception.status_code == test_status
    assert exception.quiet is True
    assert exception.message == "test message"

# Generated at 2022-06-14 07:13:59.046505
# Unit test for function add_status_code
def test_add_status_code():
    class CustomException(SanicException):
        pass

    @add_status_code(409)
    class MissingResource(CustomException):
        pass

    @add_status_code(500)
    class InternalError(CustomException):
        pass

    assert _sanic_exceptions[409] is MissingResource
    assert _sanic_exceptions[500] is InternalError
    assert not hasattr(MissingResource, "quiet")
    assert InternalError.quiet is True

# Generated at 2022-06-14 07:14:07.301189
# Unit test for function add_status_code
def test_add_status_code():
    # Test whether argument quiet is passed to the class decorator
    # as argument quiet.
    quiet_test = add_status_code(808, quiet=True)
    assert isinstance(quiet_test(SanicException), SanicException)
    assert quiet_test(SanicException).status_code == 808
    assert quiet_test(SanicException, quiet=True).quiet == True

    # Test whether the default value for quiet is None for a 500-class HTTP
    # error.
    quiet_test2 = add_status_code(500)
    assert isinstance(quiet_test2(SanicException), SanicException)
    assert quiet_test2(SanicException, quiet=False).quiet == False

    # Test whether the default value for quiet is True for a non-500-class
    # HTTP error.
    quiet_test3 = add

# Generated at 2022-06-14 07:14:11.424084
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class NotFound(SanicException):
        pass

    assert NotFound.status_code == 400
    assert _sanic_exceptions[400] == NotFound

# Generated at 2022-06-14 07:14:25.228888
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418, quiet=True)
    class TestException(SanicException):
        pass
    assert issubclass(_sanic_exceptions[418], TestException)
    assert _sanic_exceptions[418].status_code == 418
    assert _sanic_exceptions[418].quiet is True
    # Test quiet=None
    @add_status_code(403, quiet=None)
    class TestException2(SanicException):
        pass
    assert issubclass(_sanic_exceptions[403], TestException2)
    assert _sanic_exceptions[403].quiet is False
    # Test default quiet=None
    @add_status_code(500, quiet=None)
    class TestException3(SanicException):
        pass

# Generated at 2022-06-14 07:14:30.468206
# Unit test for function add_status_code
def test_add_status_code():
    class Foo(SanicException):
        pass

    assert Foo.status_code is None
    assert Foo.quiet is None

    add_status_code(202, quiet=True)(Foo)
    assert Foo.status_code == 202
    assert Foo.quiet is True

# Generated at 2022-06-14 07:14:36.214537
# Unit test for function add_status_code
def test_add_status_code():
    """
    Ensure the add_status_code decorator does what we expect it to.
    """

    @add_status_code(666)
    class Foo(SanicException):
        pass

    assert _sanic_exceptions[666] is Foo
    assert Foo.status_code == 666



# Generated at 2022-06-14 07:14:42.458746
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestException(SanicException):
        pass
    assert _sanic_exceptions[200] == TestException
    assert _sanic_exceptions[200]().status_code == 200

    @add_status_code(514)
    class TestException2(SanicException):
        pass
    assert _sanic_exceptions[514] == TestException2
    assert _sanic_exceptions[514]().status_code == 514



# Generated at 2022-06-14 07:14:47.917269
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyException(Exception):
        pass

    assert "MyException" in _sanic_exceptions
    assert _sanic_exceptions[400] == MyException


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:14:50.978933
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class test_SanicException(SanicException):
        pass
    assert test_SanicException.status_code == 100


# Generated at 2022-06-14 07:14:57.133071
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(503)
    class TestException(SanicException):
        """
        **Status**: 503 Test Exception
        """

        pass

    assert _sanic_exceptions[TestException.status_code] == TestException
    assert TestException.quiet is True
    exc_obj = TestException("Test exception")
    assert exc_obj.status_code == 503
    assert exc_obj.quiet is True
    assert "Test exception" in str(exc_obj)

# Generated at 2022-06-14 07:15:11.412136
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test for add_status_code.
    """
    _sanic_exceptions = {}

    # Test decorator without status code
    @add_status_code(200)
    def test_1():
        pass

    assert "200" in _sanic_exceptions.keys()

    # Test decorator with status code
    @add_status_code(400)
    def test_2():
        pass

    assert "400" in _sanic_exceptions.keys()

# Generated at 2022-06-14 07:15:19.986967
# Unit test for function add_status_code
def test_add_status_code():
    # Test non-quiet default
    @add_status_code(402)
    class NewClass(SanicException):
        pass

    assert(NewClass.quiet == False)
    assert(NewClass.status_code == 402)

    # Test quiet
    @add_status_code(403, quiet=True)
    class NewClass(SanicException):
        pass

    assert(NewClass.quiet == True)
    assert(NewClass.status_code == 403)

    # Test default 500 is non-quiet
    @add_status_code(500)
    class NewClass(SanicException):
        pass

    assert(NewClass.quiet == False)
    assert(NewClass.status_code == 500)



# Generated at 2022-06-14 07:15:28.992040
# Unit test for function add_status_code
def test_add_status_code():
    # add_status_code(code, quiet)
    # return a class_decorator
    @add_status_code(400)
    class MyClass(SanicException):
        pass

    assert MyClass.status_code == 400
    assert MyClass.quiet == True

    # _sanic_exceptions should contain 400
    assert 400 in _sanic_exceptions

    # _sanic_exceptions[400] == MyClass
    assert _sanic_exceptions[400] == MyClass


# Generated at 2022-06-14 07:15:34.126875
# Unit test for function add_status_code
def test_add_status_code():
    assert 400 == InvalidUsage().status_code
    assert 404 == NotFound().status_code
    assert 500 == ServerError().status_code
    assert 503 == ServiceUnavailable().status_code
    assert "3.3.3" == SanicException("3.3.3").message


# Generated at 2022-06-14 07:15:48.553764
# Unit test for function add_status_code
def test_add_status_code():
    import unittest

    class TestException(SanicException):
        pass

    class TestExceptionClassDecorator(unittest.TestCase):

        def test_add_status_code(self):
            class DecoratorTestException(SanicException):
                pass

            add_status_code(100)(DecoratorTestException)

            self.assertIn(
                100,
                _sanic_exceptions.keys(),
                'add_status_code only adds new class to _sanic_exceptions'
            )

            self.assertEqual(
                _sanic_exceptions[100],
                DecoratorTestException,
                'add_status_code class decorator does not set status_code'
            )


# Generated at 2022-06-14 07:15:51.993872
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(42)
    class CustomException(SanicException):
        pass

    assert CustomException.status_code == 42
    assert _sanic_exceptions[42] == CustomException


# Generated at 2022-06-14 07:16:06.443026
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(100)(SanicException)
    status_code = SanicException.status_code
    assert status_code == 100

    add_status_code(200)(SanicException)
    status_code = SanicException.status_code
    assert status_code == 100

    class A(SanicException):
        pass
    add_status_code(300)(A)
    status_code = A.status_code
    assert status_code == 300

    add_status_code(400)(SanicException)
    status_code = SanicException.status_code
    assert status_code == 100

    add_status_code(500, quiet=True)(SanicException)
    status_code = SanicException.status_code
    assert status_code == 100



# Generated at 2022-06-14 07:16:12.316188
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    status_code = 200

    MyException = add_status_code(status_code)(MyException)

    assert MyException.status_code == status_code
    assert MyException().status_code == status_code
    assert _sanic_exceptions.get(status_code) == MyException

# Generated at 2022-06-14 07:16:25.085748
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 404
    class test_class(Exception):
        pass

    t1 = add_status_code(status_code)(test_class)
    assert type(t1) is type
    assert t1.status_code == status_code
    assert t1.quiet == True

    status_code = 500
    t2 = add_status_code(status_code)(test_class)
    assert type(t1) is type
    assert t2.status_code == status_code
    assert t2.quiet == False

    status_code = 400
    t3 = add_status_code(status_code)(test_class)
    assert type(t1) is type
    assert t3.status_code == status_code
    assert t3.quiet == True

    status_code = 200
    t4 = add_

# Generated at 2022-06-14 07:16:31.150339
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(401)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[401] == TestException
    assert issubclass(_sanic_exceptions[401], TestException)
    assert issubclass(_sanic_exceptions[401], SanicException)

# Generated at 2022-06-14 07:16:50.965606
# Unit test for function add_status_code
def test_add_status_code():

    def _test(cls):
        assert cls.status_code == 512
        assert cls.quiet is True
        assert cls.__name__ == "TestClass"

    @add_status_code(512, True)
    class TestClass(SanicException):
        pass

    _test(TestClass)



# Generated at 2022-06-14 07:17:00.669409
# Unit test for function add_status_code
def test_add_status_code():
    # a case with status_code = 500.
    @add_status_code(500)
    class MyException(SanicException):
        pass

    assert MyException(message = "Test") is not None
    assert MyException(message = "Test").status_code == 500
    # a case with status_code = 403.
    @add_status_code(403)
    class Forbidden(SanicException):
        pass

    assert Forbidden(message = "Test") is not None
    assert Forbidden(message = "Test").status_code == 403

# Generated at 2022-06-14 07:17:05.692497
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(status_code = 403, quiet = True)
    class ClassA(SanicException):
        pass

    classA = ClassA("ClassA message")

    assert classA.message == "ClassA message"
    assert classA.status_code == 403
    assert classA.quiet == True

# Generated at 2022-06-14 07:17:08.944850
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class IAmATeapot(SanicException):
        pass

    assert IAmATeapot.status_code == 418

# Generated at 2022-06-14 07:17:17.079059
# Unit test for function add_status_code
def test_add_status_code():
    class NewSanicException(SanicException):
        """Test class for the add_status_code method."""
    
    status_code = 999
    assert not NewSanicException.status_code
    assert 999 not in _sanic_exceptions
    add_status_code(status_code)(NewSanicException)
    assert NewSanicException.status_code == status_code
    assert status_code in _sanic_exceptions
    assert _sanic_exceptions[status_code] == NewSanicException
test_add_status_code()

# Generated at 2022-06-14 07:17:29.482714
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class Teapot(SanicException):
        pass

    assert Teapot.status_code == 418
    assert issubclass(_sanic_exceptions[418], Teapot)
    assert isinstance(Teapot(), Teapot)

    exc = Teapot()
    assert isinstance(exc, SanicException)
    assert exc.status_code == 418
    assert exc.args[0] == ""
    assert exc.args[1] == 418

    exc = Teapot("The Thing is not a teapot!")
    assert exc.args[0] == "The Thing is not a teapot!"
    assert exc.args[1] == 418

    exc = Teapot(status_code=200)
    assert exc.status_code == 200

    exc = Te

# Generated at 2022-06-14 07:17:41.122996
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

# Generated at 2022-06-14 07:17:54.516305
# Unit test for function add_status_code
def test_add_status_code():
    sanic_exception_base_class = SanicException

    @add_status_code(401)
    class MyCustomError(sanic_exception_base_class):
        pass

    assert MyCustomError.status_code == 401
    assert MyCustomError.quiet == False
    assert _sanic_exceptions[401] == MyCustomError

    @add_status_code(404, quiet=True)
    class MyCustomError(sanic_exception_base_class):
        pass

    assert MyCustomError.status_code == 404
    assert MyCustomError.quiet == True
    assert _sanic_exceptions[404] == MyCustomError

    @add_status_code(500, quiet=False)
    class MyCustomError(sanic_exception_base_class):
        pass

    assert MyCustomError.status

# Generated at 2022-06-14 07:17:58.862537
# Unit test for function add_status_code
def test_add_status_code():
    """
    unit test for function add_status_code
    """
    assert add_status_code(123)


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:18:03.070012
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class MyNewException(SanicException):
        pass
    assert 100 in _sanic_exceptions
    assert _sanic_exceptions[100] is MyNewException

# Generated at 2022-06-14 07:18:33.182326
# Unit test for function add_status_code
def test_add_status_code():
    def status_function():
        pass

    add_status_code(201)(status_function)
    assert status_function.status_code == 201



# Generated at 2022-06-14 07:18:37.148529
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class C(SanicException):
        pass
    assert C().status_code == 404
    assert C().quiet == True

# Generated at 2022-06-14 07:18:46.668329
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    class MyException2(SanicException):
        pass

    add_status_code(404)(MyException)
    assert _sanic_exceptions[404] == MyException
    add_status_code(405)(MyException2)
    assert _sanic_exceptions[405] == MyException2
    add_status_code(503)(MyException2)
    assert _sanic_exceptions[503] == MyException2



# Generated at 2022-06-14 07:18:51.749545
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(422)
    class UnprocessableEntity(SanicException):
        pass
    assert UnprocessableEntity.status_code == 422  # check class attribute
    assert UnprocessableEntity().status_code == 422  # check instance attribute

# Generated at 2022-06-14 07:18:56.343313
# Unit test for function add_status_code
def test_add_status_code():
    class Test401(SanicException):
        pass

    add_status_code(401)(Test401)
    assert _sanic_exceptions[401].__name__ == 'Test401'
    with pytest.raises(Test401):
        abort(401)

# Generated at 2022-06-14 07:19:05.996295
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(444)
    class TestException(SanicException):
        def __init__(self, message, quiet=None):
            super().__init__(message, 444)
            if quiet or quiet is None:
                self.quiet = True

    assert issubclass(TestException, SanicException)
    assert 444 in _sanic_exceptions
    assert _sanic_exceptions[444] is TestException

    try:
        raise TestException("Test exception for coverage.")
    except TestException as te:
        assert te.status_code == 444


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:19:16.389761
# Unit test for function add_status_code
def test_add_status_code():
    # Test the basic execution of add_status_code
    @add_status_code(123)
    class A(SanicException):
        pass
    assert A.status_code == 123
    assert A.quiet == False

    @add_status_code(456)
    class A(SanicException):
        pass
    assert A.status_code == 123
    assert A.quiet == False
    assert _sanic_exceptions[123] == A

    @add_status_code(123, quiet=True)
    class A(SanicException):
        pass
    assert A.status_code == 123
    assert A.quiet == True
    assert _sanic_exceptions[123] == A

    @add_status_code(123, quiet=False)
    class A(SanicException):
        pass

# Generated at 2022-06-14 07:19:23.688146
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(300)
    class _TestException(SanicException): pass

    assert _TestException.status_code == 300
    assert _TestException.quiet is None

    @add_status_code(300, quiet=False)
    class _TestException(SanicException): pass

    assert _TestException.status_code == 300
    assert _TestException.quiet is False

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:19:34.614454
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(123)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 123
    assert TestException.quiet is None
    assert _sanic_exceptions[123] == TestException

    @add_status_code(123, quiet=True)
    class TestException2(SanicException):
        pass

    assert TestException2.status_code == 123
    assert TestException2.quiet is True
    assert _sanic_exceptions[123] == TestException2

    @add_status_code(123, quiet=False)
    class TestException3(SanicException):
        pass

    assert TestException3.status_code == 123
    assert TestException3.quiet is False
    assert _sanic_exceptions[123] == TestException3


# Generated at 2022-06-14 07:19:35.811933
# Unit test for function add_status_code
def test_add_status_code():
    assert STATUS_CODES[404] == b'Not Found'


# Generated at 2022-06-14 07:20:37.052756
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestAddStatusCodeException(SanicException):
        pass



# Generated at 2022-06-14 07:20:41.014575
# Unit test for function add_status_code
def test_add_status_code():
    # Returned class should be added to dict
    assert _sanic_exceptions[404] == NotFound


if __name__ == "__main__":
    # Run unit tests
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 07:20:44.361139
# Unit test for function add_status_code
def test_add_status_code():
    """ Test decorator add_status_code"""

    @add_status_code(code=555)
    class TestClass(SanicException):
        pass

    assert TestClass.status_code == 555

# Generated at 2022-06-14 07:20:50.762804
# Unit test for function add_status_code
def test_add_status_code():
    # Return a SanicException instance
    @add_status_code(500)
    class CustomException(SanicException):
        pass

    assert issubclass(CustomException, SanicException)
    assert isinstance(CustomException(), SanicException)
    assert CustomException.status_code == 500


# Generated at 2022-06-14 07:21:00.254117
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(502)
    class BadGateway(SanicException):
        pass

    test_instance = BadGateway('message')
    assert test_instance.status_code == 502

    @add_status_code(405)
    class BadMethod(SanicException):
        pass

    test_instance = BadMethod('message')
    assert test_instance.status_code == 405

    assert _sanic_exceptions[502] == BadGateway
    assert _sanic_exceptions[405] == BadMethod

# Generated at 2022-06-14 07:21:03.996011
# Unit test for function add_status_code
def test_add_status_code():
    assert len(_sanic_exceptions) == 9
    assert _sanic_exceptions.get(404) is NotFound
    assert _sanic_exceptions.get(500) is ServerError


# Generated at 2022-06-14 07:21:08.478505
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class Testing(SanicException):
        pass
    assert _sanic_exceptions.get(400).__name__ == 'Testing'
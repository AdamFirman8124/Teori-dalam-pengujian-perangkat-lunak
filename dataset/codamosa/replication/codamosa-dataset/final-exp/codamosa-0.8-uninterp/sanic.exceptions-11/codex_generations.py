

# Generated at 2022-06-14 07:11:21.720485
# Unit test for function add_status_code
def test_add_status_code():
    # Need to create instance of SanicException first
    class Foo(SanicException):
        pass

    add_status_code(502, quiet=False)(Foo)

    assert hasattr(Foo, 'status_code')
    assert hasattr(Foo, 'quiet')
    assert Foo.status_code == 502
    assert Foo.quiet == False
    assert Foo(status_code=502)

# Generated at 2022-06-14 07:11:29.208255
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class TestException(SanicException):
        pass

    exception = TestException(message="Testing")
    assert exception.status_code == 500

    @add_status_code(200)
    class TestException(SanicException):
        pass

    exception = TestException(message="Testing")
    assert exception.status_code == 200

    @add_status_code(200, quiet=False)
    class TestException(SanicException):
        pass

    exception = TestException(message="Testing")
    assert exception.status_code == 200
    assert exception.quiet == False

    @add_status_code(200, quiet=True)
    class TestException(SanicException):
        pass

    exception = TestException(message="Testing")
    assert exception.status_code == 200
    assert exception

# Generated at 2022-06-14 07:11:35.780771
# Unit test for function add_status_code
def test_add_status_code():
    class Test(SanicException):
        pass

    test_cls = add_status_code(123)(Test)
    assert test_cls.status_code == 123
    assert test_cls.quiet is False
    assert test_cls() is not None


# Test for the exception creation

# Generated at 2022-06-14 07:11:42.113806
# Unit test for function add_status_code
def test_add_status_code():
    class NewException(SanicException):
        pass
    assert NewException.status_code is None
    NewException = add_status_code(500)(NewException)
    assert NewException.status_code == 500
    NewException = add_status_code(500, quiet=True)(NewException)
    assert NewException.quiet is True



# Generated at 2022-06-14 07:11:46.759418
# Unit test for function add_status_code
def test_add_status_code():
    # test to check status code is set as property
    class TestStatusCode(SanicException):
        pass

    add_status_code(401)(TestStatusCode)
    assert TestStatusCode.status_code == 401

# Generated at 2022-06-14 07:11:50.650013
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(402)
    class PaymentRequired(SanicException):
        pass

    assert PaymentRequired.status_code == 402
    assert PaymentRequired.quiet == True

    class PaymentRequired2(SanicException):
        pass

    assert PaymentRequired2.status_code == 500
    add_status_code(402, True)(PaymentRequired2)
    assert PaymentRequired2.quiet == True

# Generated at 2022-06-14 07:12:00.527262
# Unit test for function add_status_code
def test_add_status_code():
    class TestClass(SanicException):
        pass
    add_status_code(404)(TestClass)
    assert TestClass.status_code == 404
    assert TestClass.quiet == True
    assert _sanic_exceptions[404] == TestClass

    #
    class TestClass2(SanicException):
        pass
    add_status_code(500)(TestClass2)
    assert TestClass2.status_code == 500
    assert TestClass2.quiet == False
    assert _sanic_exceptions[500] == TestClass2


if __name__ == '__main__':
    test_add_status_code()

# Generated at 2022-06-14 07:12:11.377611
# Unit test for function add_status_code
def test_add_status_code():
    class MockException(SanicException):
        pass

    mock_args = [404, 500, 200]
    for code in mock_args:
        assert code not in _sanic_exceptions

    for code in mock_args:
        add_status_code(code)(MockException)
        assert code in _sanic_exceptions
        assert _sanic_exceptions[code] == MockException

        MockException.__module__ = 'tests'

    assert _sanic_exceptions[404] == MockException
    assert _sanic_exceptions[404].__module__ == "tests"

    mock_kwargs = {
        404: True,
        500: None,
        200: False
    }


# Generated at 2022-06-14 07:12:14.986612
# Unit test for function add_status_code
def test_add_status_code():
    exception = add_status_code(100)
    @exception
    class Exception100(SanicException):
        pass
    assert Exception100.status_code is 100

# Generated at 2022-06-14 07:12:19.213976
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403, quiet=True)
    class Test(SanicException):
        pass
    
    assert Test.status_code == 403
    assert Test.quiet is True

# Generated at 2022-06-14 07:12:33.681560
# Unit test for function add_status_code
def test_add_status_code():
    class FooException(SanicException):
        pass
    
    @add_status_code(400)
    class BarException(SanicException):
        pass

    @add_status_code(500)
    class SpamException(SanicException):
        pass

    # Ensure FooException is not added to _sanic_exceptions
    assert FooException.status_code is None
    assert len(_sanic_exceptions) == 3

    with pytest.raises(BarException):
        raise BarException("BarException")

    with pytest.raises(SpamException):
        raise SpamException("SpamException")

    with pytest.raises(SanicException) as err:
        raise FooException("FooException")

    assert err.value.status_code is None
    assert len(_sanic_exceptions) == 3

# Generated at 2022-06-14 07:12:39.014777
# Unit test for function add_status_code
def test_add_status_code():

    @add_status_code(500)
    class CustomException(SanicException):
        """
        **Status**: 500 Internal Server Error
        """
        pass

    assert _sanic_exceptions.get(500) == CustomException

# Generated at 2022-06-14 07:12:49.022309
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class test(SanicException):
        pass

    @add_status_code(200, quiet=True)
    class test2(SanicException):
        pass

    @add_status_code(400, quiet=False)
    class test3(SanicException):
        pass

    @add_status_code(500)
    class test4(SanicException):
        pass

    exception = test("testing")
    assert exception.status_code == 100
    assert exception.quiet == False

    exception = test2("testing")
    assert exception.status_code == 200
    assert exception.quiet == True

    exception = test3("testing")
    assert exception.status_code == 400
    assert exception.quiet == False

    exception = test4("testing")
    assert exception.status_code

# Generated at 2022-06-14 07:13:02.661238
# Unit test for function add_status_code
def test_add_status_code():
    from inspect import isclass, getmembers
    status = 500
    @add_status_code(status)
    class TestSanicException(SanicException):
        pass
    assert status in _sanic_exceptions.keys()
    assert TestSanicException.status_code == 500
    @add_status_code(status)
    class TestSanicException(SanicException):
        pass
    assert TestSanicException.status_code == 500
    @add_status_code(status)
    class TestSanicException(Exception):
        pass
    assert TestSanicException.status_code == 500
    @add_status_code(status)
    class TestSanicException():
        pass
    assert TestSanicException.status_code == 500
    for code, cls in _sanic_exceptions.items():
        assert iss

# Generated at 2022-06-14 07:13:06.723027
# Unit test for function add_status_code
def test_add_status_code():
    # Reference: https://github.com/sanic-dev/sanic/pull/1347
    @add_status_code(422, quiet=True)
    class UnprocessableEntity(SanicException):
        pass

    assert UnprocessableEntity.status_code == 422
    assert UnprocessableEntity.quiet == True
    assert _sanic_exceptions[422] == UnprocessableEntity
    assert _sanic_exceptions[422](message='fail').status_code == 422
    assert _sanic_exceptions[422].__name__ == 'UnprocessableEntity'

# Generated at 2022-06-14 07:13:18.036800
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class MyTestException(SanicException):
        pass

    assert MyTestException.status_code == 400
    assert _sanic_exceptions[400] == MyTestException

    @add_status_code(404)
    class MyTestException(SanicException):
        pass
    assert MyTestException.status_code == 404
    assert _sanic_exceptions[404] == MyTestException

    @add_status_code(500)
    class MyTestException(SanicException):
        pass
    assert MyTestException.status_code == 500
    assert _sanic_exceptions[500] == MyTestException

# Generated at 2022-06-14 07:13:22.880944
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418, quiet=True)
    class IAmATeapot(SanicException):
        pass

    assert IAmATeapot.status_code == 418
    assert IAmATeapot.quiet == True
    assert _sanic_exceptions[418] == IAmATeapot

# Generated at 2022-06-14 07:13:25.991012
# Unit test for function add_status_code
def test_add_status_code():
    class NotFound(SanicException):
        pass
    assert NotFound._sanic_exceptions[404] == NotFound
    assert NotFound.status_code == 404

# Generated at 2022-06-14 07:13:30.571447
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(201)
    class Test(SanicException):
        pass
    assert _sanic_exceptions.get(201) is Test
    assert _sanic_exceptions.get(200) is None

# Generated at 2022-06-14 07:13:36.764379
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class IAmATeaPot(SanicException):
        pass
    assert IAmATeaPot.status_code == 418
    assert IAmATeaPot().status_code == 418
    assert isinstance(IAmATeaPot(), SanicException)


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:13:45.623634
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        pass
    
    test_exception = TestException('test', status_code=400)
    assert test_exception.status_code == 400 and test_exception.message == 'test'

# Generated at 2022-06-14 07:13:57.540283
# Unit test for function add_status_code
def test_add_status_code():
    # test for add_status_code(code, quiet=None)
    @add_status_code(code=200, quiet=None)
    class Status_200(Exception):  # this could be any class
        pass

    # test for add_status_code(code, quiet=None)
    @add_status_code(code=202, quiet=True)
    class Status_202(Exception):  # this could be any class
        pass

    try:
        raise Status_200()
    except Status_200:
        assert Status_200.status_code == 200
        assert Status_200.quiet == True

    try:
        raise Status_202()
    except Status_202:
        assert Status_202.status_code == 202
        assert Status_202.quiet == True


# Generated at 2022-06-14 07:14:03.221218
# Unit test for function add_status_code
def test_add_status_code():
    class FooBaseException(SanicException):
        pass

    code = 400
    @add_status_code(code)
    class FooException(FooBaseException):
        pass
    assert _sanic_exceptions[code] == FooException
    assert _sanic_exceptions[code](message="test", status_code=code).status_code == code
    assert _sanic_exceptions[code](message="test", status_code=code).message == "test"

# Generated at 2022-06-14 07:14:15.621352
# Unit test for function add_status_code
def test_add_status_code():
    class Test_1(SanicException):
        pass
    class Test_2(SanicException):
        pass
    class Test_3(SanicException):
        pass
    class Test_4(SanicException):
        pass
    class Test_5(SanicException):
        pass
    class Test_6(SanicException):
        pass
    class Test_7(SanicException):
        pass
    class Test_8(SanicException):
        pass
    class Test_9(SanicException):
        pass
    Test_1 = add_status_code(405)(Test_1)
    Test_1 = add_status_code(500, True)(Test_1)
    Test_2 = add_status_code(500, False)(Test_2)

# Generated at 2022-06-14 07:14:25.147769
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(Exception):
        pass

    test_exception = TestException

    assert test_exception.__name__ != "Forbidden"
    assert test_exception.__name__ != "403"
    assert test_exception.__name__ == "TestException"
    assert hasattr(test_exception, "status_code") is False

    add_status_code(403)(test_exception)

    assert hasattr(test_exception, "status_code") is True
    assert test_exception.status_code == 403

# Generated at 2022-06-14 07:14:30.943265
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(400)(SanicException)
    assert SanicException.status_code == 400
    add_status_code(400, True)(SanicException)
    assert SanicException.quiet == True
    assert SanicException.status_code == 400

test_add_status_code()

# Generated at 2022-06-14 07:14:33.948187
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class MockException(Exception):
        pass
    assert _sanic_exceptions[100] == MockException

# Generated at 2022-06-14 07:14:35.236890
# Unit test for function add_status_code
def test_add_status_code():
    assert 400 == InvalidUsage.status_code

# Generated at 2022-06-14 07:14:45.516593
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class Http400Exception(SanicException):
        pass

    assert 400 not in STATUS_CODES
    assert 400 in _sanic_exceptions
    assert _sanic_exceptions[400] == Http400Exception
    assert Http400Exception.status_code == 400

# Unit tests for function abort
# STATUS_CODES from sanic.helpers

# Generated at 2022-06-14 07:14:48.811707
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class Dummy(SanicException):
        pass
    assert Dummy.status_code == 100



# Generated at 2022-06-14 07:15:10.017922
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class Foo(SanicException):
        pass

    assert Foo.status_code == 100
    assert Foo().status_code == 100

    @add_status_code(200, quiet=True)
    class Bar(SanicException):
        pass

    assert Bar.status_code == 200
    assert Bar().status_code == 200
    assert Bar().quiet is True

    @add_status_code(300, quiet=False)
    class Baz(SanicException):
        pass

    assert Baz.status_code == 300
    assert Baz().status_code == 300
    assert Baz().quiet is False

    @add_status_code(400)
    class Quxx(SanicException):
        pass

    assert Quxx.status_code == 400
    assert Quxx().status_code == 400


# Generated at 2022-06-14 07:15:13.710938
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class Expected(SanicException):
        pass
    assert _sanic_exceptions[200] == Expected


# Generated at 2022-06-14 07:15:16.776582
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400, True)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 400
    assert TestException.quiet == True

# Generated at 2022-06-14 07:15:19.407529
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(201)
    assert 201 in _sanic_exceptions


# Generated at 2022-06-14 07:15:33.265644
# Unit test for function add_status_code
def test_add_status_code():
    # Test the default code and Quiet
    @add_status_code(404)
    class test404(SanicException):
        pass
    assert getattr(test404, 'status_code') == 404
    assert getattr(test404, 'quiet') == True

    # Test add new code without specified Quiet or Quiet = False
    @add_status_code(432)
    class test432_1(SanicException):
        pass

    assert getattr(test432_1, 'status_code') == 432
    assert getattr(test432_1, 'quiet') == False

    # Test add new code with specified Quiet
    @add_status_code(432, quiet=True)
    class test432_2(SanicException):
        pass

    assert getattr(test432_2, 'status_code') == 432
    assert getattr

# Generated at 2022-06-14 07:15:38.648950
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 500
    assert TestException.quiet is True
    assert hash(TestException) == hash(TestException.status_code)

    @add_status_code(500, quiet=False)
    class TestException2(SanicException):
        pass

    assert TestException2.status_code == 500
    assert TestException2.quiet is False
    assert hash(TestException2) == hash(TestException2.status_code)

# Generated at 2022-06-14 07:15:43.581307
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 404
    assert TestException.quiet is True
    assert issubclass(TestException, SanicException)



# Generated at 2022-06-14 07:15:46.056036
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(501)(SanicException)

    assert 501 in _sanic_exceptions


# Generated at 2022-06-14 07:15:49.193782
# Unit test for function add_status_code
def test_add_status_code():
    with pytest.raises(TypeError):
        @add_status_code()
        class Kodama(SanicException):
            pass

# Generated at 2022-06-14 07:15:54.193006
# Unit test for function add_status_code
def test_add_status_code():
    status_code = 400

    class TestSanicException(SanicException):
        def __init__(self, message, status_code=None, quiet=None):
            super().__init__(message)
            self.status_code = status_code
            if quiet or quiet is None and status_code != 500:
                self.quiet = True
    
    add_status_code(status_code)(TestSanicException)
    assert _sanic_exceptions[status_code] is TestSanicException


# Generated at 2022-06-14 07:16:20.965236
# Unit test for function add_status_code
def test_add_status_code():

    @add_status_code(876)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 876
    assert TestException.quiet is None

    @add_status_code(876, quiet=True)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 876
    assert TestException.quiet is True
    _sanic_exceptions.pop(876)

    @add_status_code(876)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 876
    assert TestException.quiet is True
    _sanic_exceptions.pop(876)

# Generated at 2022-06-14 07:16:27.303418
# Unit test for function add_status_code
def test_add_status_code():
    # give the test function a numeric code
    @add_status_code(code=402)
    class TestException(SanicException):
        pass

    # create an instance of the test exception
    my_exception = TestException('message')

    # verify that the code is set to the value specified in @add_status_code
    assert my_exception.status_code == 402

# Generated at 2022-06-14 07:16:35.943812
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(status_code=200)
    class Test(SanicException):
        pass
    assert Test.status_code == 200
    assert Test.quiet == False
    @add_status_code(status_code=201)
    class Test1(SanicException):
        pass
    assert Test1.status_code == 201
    assert Test1.quiet == True
    @add_status_code(status_code=201, quiet=False)
    class Test2(SanicException):
        pass
    assert Test2.status_code == 201
    assert Test2.quiet == False

# Generated at 2022-06-14 07:16:45.532705
# Unit test for function add_status_code
def test_add_status_code():
    def test_initialization_of_a_status_code_exception(code, message):
        _sanic_exceptions[code] = 0
        add_status_code(code)(SanicException)
        assert _sanic_exceptions[code].status_code == code
        assert isinstance(_sanic_exceptions[code](message), SanicException)

    test_initialization_of_a_status_code_exception(400, "test")
    test_initialization_of_a_status_code_exception(401, "test")
    test_initialization_of_a_status_code_exception(402, "test")
    test_initialization_of_a_status_code_exception(403, "test")

# Generated at 2022-06-14 07:16:46.693752
# Unit test for function add_status_code
def test_add_status_code():
    assert abort.__name__ == 'abort'

# Generated at 2022-06-14 07:16:57.822404
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(404)(NotFound)
    add_status_code(400)(InvalidUsage)
    add_status_code(405)(MethodNotSupported)
    add_status_code(500)(ServerError)
    add_status_code(503)(ServiceUnavailable)
    add_status_code(408)(RequestTimeout)
    add_status_code(413)(PayloadTooLarge)
    add_status_code(416)(ContentRangeError)
    add_status_code(417)(HeaderExpectationFailed)
    add_status_code(403)(Forbidden)
    add_status_code(401)(Unauthorized)
    assert _sanic_exceptions[404] == NotFound
    assert _sanic_exceptions[400] == InvalidUsage
    assert _sanic_exceptions[405] == MethodNotSupported

# Generated at 2022-06-14 07:17:06.831733
# Unit test for function add_status_code
def test_add_status_code():
    # default quiet = False
    MyException = add_status_code(444)(SanicException)
    assert MyException.status_code == 444
    assert MyException.quiet == False
    # quiet = True
    MyException1 = add_status_code(445, True)(SanicException)
    assert MyException1.status_code == 445
    assert MyException1.quiet == True


if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:17:13.351191
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class NewException(SanicException):
        pass

    # SanicException should have status_code 400
    assert NewException.status_code == 400

    # Check if the new exception is available in the _sanic_exceptions dict
    assert _sanic_exceptions[400] == NewException


# Generated at 2022-06-14 07:17:16.807310
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    add_status_code(500)(MyException)
    assert _sanic_exceptions[500] == MyException

# Generated at 2022-06-14 07:17:20.902734
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(code=201, quiet=False)
    class Error_201(SanicException):
        pass

    assert Error_201.status_code == 201
    assert Error_201.quiet == False


test_add_status_code()

# Generated at 2022-06-14 07:17:59.928802
# Unit test for function add_status_code
def test_add_status_code():
    class TestAddStatusCode(SanicException):
        pass

    add_status_code(5000)(TestAddStatusCode)

    assert TestAddStatusCode.status_code == 5000
    assert TestAddStatusCode.quiet == False

    add_status_code(5001, quiet=True)(TestAddStatusCode)
    assert TestAddStatusCode.status_code == 5001
    assert TestAddStatusCode.quiet == True


# Generated at 2022-06-14 07:18:11.967114
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(402)
    class PaymentRequired(SanicException):
        pass

    assert PaymentRequired.status_code == 402
    assert PaymentRequired.message == STATUS_CODES[402].decode("utf8")

    # Test quiet parameter
    @add_status_code(402)
    class PaymentRequired2(SanicException):
        pass

    assert PaymentRequired2.status_code == 402
    assert not PaymentRequired2.quiet

    @add_status_code(402, quiet=True)
    class PaymentRequired3(SanicException):
        pass

    assert PaymentRequired3.status_code == 402
    assert PaymentRequired3.quiet

    with pytest.raises(Exception) as error:
        @add_status_code(500)
        class ServerError2(SanicException):
            pass

   

# Generated at 2022-06-14 07:18:14.831787
# Unit test for function add_status_code
def test_add_status_code():

    @add_status_code(400)
    class CustomException(SanicException):
        pass

    assert CustomException.status_code == 400

# Generated at 2022-06-14 07:18:23.231941
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(401)
    class Unauthorized1(SanicException):
        pass

    assert _sanic_exceptions[401] == Unauthorized1

    @add_status_code(403)
    class Forbidden1(SanicException):
        pass

    assert _sanic_exceptions[403] == Forbidden1

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:18:34.332735
# Unit test for function add_status_code
def test_add_status_code():

    # Test for class SanicException
    try:
        raise SanicException
    except SanicException as test:
        assert str(test) == 'None'
        assert test.status_code == None
        assert test.quiet == None
    try:
        raise SanicException(status_code=1)
    except SanicException as test:
        assert str(test) == 'None'
        assert test.status_code == 1
        assert test.quiet == False
    try:
        raise SanicException(status_code=1, quiet=True)
    except SanicException as test:
        assert str(test) == 'None'
        assert test.status_code == 1
        assert test.quiet == True

    # Test for function add_status_code and class NotFound

# Generated at 2022-06-14 07:18:45.543597
# Unit test for function add_status_code
def test_add_status_code():
    assert 500 in _sanic_exceptions

    # Patching _sanic_exceptions
    backup = _sanic_exceptions.copy()
    try:
        _sanic_exceptions.clear()
        assert not _sanic_exceptions

        # Add new status code
        add_status_code(418)(SanicException)
        assert len(_sanic_exceptions) == 1
        assert 418 in _sanic_exceptions
    finally:
        _sanic_exceptions.clear()
        _sanic_exceptions.update(backup)

# Generated at 2022-06-14 07:18:58.388109
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class BadRequest(SanicException):
        pass
    assert BadRequest.status_code == 400


if __name__ == "__main__":
    import unittest

    class TestExceptions(unittest.TestCase):
        def test_addStatusCode(self):
            @add_status_code(400)
            class BadRequest(SanicException):
                pass

            assert BadRequest.status_code == 400

        def test_baseException(self):
            """
            Test SanicException response
            """
            exception = SanicException("Base exception", status_code=500)
            assert exception.response.status_code == 500
            assert exception.response.body == b'"Base exception"'


# Generated at 2022-06-14 07:19:04.360073
# Unit test for function add_status_code
def test_add_status_code():
    code = 404
    class MyException(SanicException):
        pass
    name = MyException.__name__
    new_exception = add_status_code(code)(MyException)
    assert hasattr(new_exception, 'status_code')
    assert new_exception.status_code == code
    assert name in _sanic_exceptions


# Generated at 2022-06-14 07:19:07.304440
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestException(Exception):
        pass
    assert TestException is _sanic_exceptions[200]


# Generated at 2022-06-14 07:19:11.935796
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class TestException(Exception):
        pass

    assert type(TestException()).__name__ == "TestException"
    assert TestException().status_code == 500

# Generated at 2022-06-14 07:20:19.609508
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(code=200)
    class TestException(Violation):
        """
        **Status**: 200 OK
        """

        pass

    assert TestException(message="A problem occurred.").status_code == 200
    assert TestException(message="A problem occurred.").message == "A problem occurred."
    assert TestException(message="A problem occurred.").quiet == None  # True

# Generated at 2022-06-14 07:20:30.037115
# Unit test for function add_status_code
def test_add_status_code():
    # unit test for function add_status_code
    global _sanic_exceptions
    _sanic_exceptions = {}
    @add_status_code(101)
    class Testing(SanicException): # noqa
        pass

    assert Testing.status_code == 101
    assert Testing.quiet is None
    assert isinstance(Testing(), SanicException)

    @add_status_code(102, quiet=True)
    class Testing(SanicException): # noqa
        pass
    assert Testing.status_code == 102
    assert Testing.quiet is True

    @add_status_code(103)
    class Testing(SanicException): # noqa
        pass
    assert Testing.status_code == 103
    assert Testing.quiet is None
    assert isinstance(Testing(), SanicException)

# Generated at 2022-06-14 07:20:36.560089
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class SomeException(SanicException):
        pass

    assert SomeException.status_code == 200
    assert SomeException.__name__ == "SomeException"
    assert SomeException.quiet

    with pytest.raises(SanicException):
        raise SomeException("test")


# Generated at 2022-06-14 07:20:39.285947
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class InvalidUsage(SanicException):
        pass
    assert _sanic_exceptions[400] == InvalidUsage

# Generated at 2022-06-14 07:20:42.641357
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(1001)
    class MyException(SanicException):
        pass
    assert MyException.quiet == True
    assert MyException.status_code == 1001



# Generated at 2022-06-14 07:20:45.798231
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class IAmATeapot(SanicException):
        pass

    assert _sanic_exceptions[418] == IAmATeapot



# Generated at 2022-06-14 07:20:50.700064
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400, quiet=True)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[400] is TestException
    assert TestException().quiet

# Generated at 2022-06-14 07:20:55.962955
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class MyFlaskException(Exception):
        pass
    my_exception = MyFlaskException("Hello world")
    assert my_exception.status_code == 200
    assert my_exception.quiet == True

# Generated at 2022-06-14 07:20:59.836156
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 404
    assert TestException().status_code == 404


# Generated at 2022-06-14 07:21:08.311064
# Unit test for function add_status_code
def test_add_status_code():
    new_status = 900
    @add_status_code(new_status)
    class NewStatus(SanicException):
        pass
    assert NewStatus.status_code == new_status
    assert _sanic_exceptions[new_status] is NewStatus
    assert not hasattr(NewStatus, 'quiet')
    @add_status_code(new_status)
    class NewStatusQuiet(SanicException):
        pass
    assert NewStatusQuiet.status_code == new_status
    assert _sanic_exceptions[new_status] is NewStatusQuiet
    assert NewStatusQuiet.quiet
    @add_status_code(new_status, quiet=True)
    class NewStatusQuiet2(SanicException):
        pass
    assert NewStatusQuiet2.status_code == new_status
    assert _
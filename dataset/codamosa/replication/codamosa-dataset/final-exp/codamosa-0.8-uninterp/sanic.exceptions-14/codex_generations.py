

# Generated at 2022-06-14 07:11:25.130978
# Unit test for function add_status_code
def test_add_status_code():

    # Test function decorator
    @add_status_code(302)
    class Hello(SanicException):
        pass
    assert Hello.status_code == 302
    assert Hello().status_code == 302
    assert _sanic_exceptions[302] == Hello

    # Test default behavior
    @add_status_code(200)
    class Hello2(SanicException):
        pass
    assert Hello2.status_code == 200
    assert Hello2().status_code == 200
    assert not hasattr(Hello2(), "quiet")
    assert _sanic_exceptions[200] == Hello2

    # Test quiet parameter
    @add_status_code(201)
    class Hello3(SanicException):
        pass
    assert Hello3.status_code == 201
    assert Hello3().status_code == 201
    assert Hello

# Generated at 2022-06-14 07:11:27.879994
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200, quiet=False)
    class Successful(SanicException):
        pass
    assert _sanic_exceptions[200].status_code == 200
    assert not _sanic_exceptions[200].quiet


# Generated at 2022-06-14 07:11:43.768319
# Unit test for function add_status_code
def test_add_status_code():
    # Given a status_code and a class
    # When this mock class is registered
    # Then is should be a part of the _sanic_exceptions dict
    @add_status_code(400)
    class TestBadRequest(SanicException):
        pass

    assert _sanic_exceptions[400].__name__ == 'TestBadRequest'

    # Given a custom message
    # When it is sent
    # The status code should still be present
    # And it should be a 400
    with pytest.raises(InvalidUsage) as e:
        abort(400, message="custom message")
    assert e.value.status_code == 400

    # Given a status code with no message
    # When it is sent
    # And if it is a not found
    # Then it should raise a NotFound exception

# Generated at 2022-06-14 07:11:50.237340
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(202)
    class MyException(Exception):
        pass

    assert isinstance(MyException(None), MyException)
    assert isinstance(MyException(None), SanicException)
    assert MyException.status_code == 202
    assert _sanic_exceptions[202] == MyException



# Generated at 2022-06-14 07:11:58.092513
# Unit test for function add_status_code
def test_add_status_code():
    # Test using the decorator to add a new exception
    @add_status_code(409)
    class Conflict(SanicException):
        """
        **Status**: 409 Conflict
        """

        pass

    assert Conflict.status_code == 409
    assert _sanic_exceptions[409] == Conflict

    # Test using the decorator to add a new exception without specifying quiet
    @add_status_code(410)
    class Gone(SanicException):
        """
        **Status**: 410 Gone
        """

        pass

    assert Gone.status_code == 410
    assert _sanic_exceptions[410] == Gone
    assert Gone.quiet == True

    # Test using the decorator with quiet = False

# Generated at 2022-06-14 07:12:07.661740
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test if function add_status_code is working properly
    """

    @add_status_code(444)
    class TestClass(SanicException):
        pass

    assert TestClass.status_code == 444
    assert TestClass.quiet

    TestClass2 = add_status_code(500)(TestClass)
    assert TestClass2.status_code == 500
    assert not TestClass2.quiet

    assert _sanic_exceptions[444] == TestClass
    assert _sanic_exceptions[500] == TestClass2



# Generated at 2022-06-14 07:12:21.819739
# Unit test for function add_status_code
def test_add_status_code():
    class MyException(SanicException):
        pass

    class MyException2(SanicException):
        pass

    assert isinstance(add_status_code(418, quiet=False)(MyException), MyException)
    assert hasattr(MyException, 'status_code')
    assert MyException.status_code == 418
    assert hasattr(MyException, 'quiet')
    assert not MyException.quiet

    assert isinstance(add_status_code(404, quiet=True)(MyException2), MyException2)
    assert hasattr(MyException2, 'status_code')
    assert MyException2.status_code == 404
    assert hasattr(MyException2, 'quiet')
    assert MyException2.quiet

    assert isinstance(add_status_code(500, quiet=None)(MyException), MyException)

# Generated at 2022-06-14 07:12:28.946563
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class OK(SanicException):
        ''' it is class doc
        '''
        pass
    assert 'it is class doc' == OK.__doc__.strip()
    assert 200 == OK.status_code
    assert False == OK.quiet
    assert OK is _sanic_exceptions[200]
    assert isinstance(OK(), OK)


# Generated at 2022-06-14 07:12:35.217717
# Unit test for function add_status_code
def test_add_status_code():
    def test_decorator(cls):
        cls.status_code = code
        cls.quiet = True
        _sanic_exceptions[code] = cls
        return cls

    code = 500
    add_status_code(code, quiet=True)(SanicException)
    assert test_decorator(SanicException)


# Generated at 2022-06-14 07:12:43.922776
# Unit test for function add_status_code
def test_add_status_code():
    from typing import Type, Dict

    class TestCode(SanicException):
        pass

    def func():
        add_status_code(404)(TestCode)

    # Check if TestCode can be added to _sanic_exceptions
    assert TestCode not in _sanic_exceptions.values()
    func()
    assert TestCode in _sanic_exceptions.values()

    # Check if duplicated status_code raises error
    with pytest.raises(Exception):
        func()



# Generated at 2022-06-14 07:12:56.881207
# Unit test for function add_status_code
def test_add_status_code():
    # Test add_status_code with quiet = False
    add_status_code(400)(SanicException)
    assert _sanic_exceptions[400] == SanicException
    # Test add_status_code with quiet = True and status_code = 500
    add_status_code(500, True)(SanicException)
    assert _sanic_exceptions[500] == SanicException
    # Test add_status_code with quiet = None and status_code = 200
    add_status_code(200)(SanicException)
    assert _sanic_exceptions[200] == SanicException
    # Test add_status_code with quiet = None and status_code = 500
    add_status_code(500, None)(SanicException)
    assert _sanic_exceptions[500] == SanicException

# Generated at 2022-06-14 07:13:00.163725
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class B(SanicException):
        pass

    assert B.status_code == 403

# Generated at 2022-06-14 07:13:03.708029
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestNotFound(SanicException):
        pass

    assert TestNotFound.message == "Not Found"
    assert TestNotFound.status_code == 404

# Generated at 2022-06-14 07:13:10.682832
# Unit test for function add_status_code
def test_add_status_code():
    assert _sanic_exceptions[404] is NotFound
    assert _sanic_exceptions[400] is InvalidUsage
    assert _sanic_exceptions[500] is ServerError
    assert _sanic_exceptions[503] is ServiceUnavailable

    assert NotFound.status_code == 404
    assert InvalidUsage.status_code == 400
    assert ServerError.status_code == 500
    assert ServiceUnavailable.status_code == 503

    assert NotFound.quiet is True
    assert InvalidUsage.quiet is True
    assert ServiceUnavailable.quiet is True

    # exception instances are quiet if the class is quiet
    assert NotFound().quiet is True

    # except for 500, which is never quiet
    assert ServerError().quiet is False

# Generated at 2022-06-14 07:13:16.571350
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200, quiet=True)
    class SanicOkay(SanicException):
        pass
    assert SanicOkay.status_code == 200
    assert SanicOkay.quiet == True
    assert _sanic_exceptions[SanicOkay.status_code] == SanicOkay


# Generated at 2022-06-14 07:13:24.108811
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(500)
    class TestException(SanicException):
        pass

    assert len(_sanic_exceptions) == 5
    assert TestException.status_code == 500
    assert TestException.quiet is False

    @add_status_code(400)
    class TestException(SanicException):
        pass

    assert len(_sanic_exceptions) == 6
    assert TestException.status_code == 400
    assert TestException.quiet is True

    @add_status_code(500, quiet=True)
    class TestException(SanicException):
        pass

    assert len(_sanic_exceptions) == 7
    assert TestException.status_code == 500
    assert TestException.quiet is True

# Generated at 2022-06-14 07:13:30.757123
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class MockClass(SanicException):
        pass
    assert MockClass.status_code == 200
    assert MockClass.quiet is False
    assert MockClass('') is not None
    assert _sanic_exceptions[200] == MockClass
    assert _sanic_exceptions[200] is not None

# Generated at 2022-06-14 07:13:41.886317
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 404
    assert isinstance(_sanic_exceptions.get(404), TestException)
    assert _sanic_exceptions.get(404).status_code == 404

    @add_status_code(400)
    class TestException(SanicException):
        pass
    assert TestException.status_code == 400
    assert isinstance(_sanic_exceptions.get(400), TestException)
    assert _sanic_exceptions.get(400).status_code == 400

# Generated at 2022-06-14 07:13:45.898673
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(100)
    class TestAddStatusCode(SanicException):
        pass
    assert _sanic_exceptions[100].__name__ == "TestAddStatusCode"

# Generated at 2022-06-14 07:13:52.254734
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class MyException(SanicException):
        pass

    my_exception = MyException("Test")
    assert my_exception.status_code == 404
    assert _sanic_exceptions.get(404) == MyException
    assert _sanic_exceptions.get(400) != MyException



# Generated at 2022-06-14 07:14:00.794436
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(505)
    class TestExcept(SanicException):
        pass

    assert StatusCode.get(505) == StatusCode.HTTP_505_HTTP_VERSION_NOT_SUPPORTED
    assert TestExcept.status_code == 505
    assert TestExcept.quiet is None

# Generated at 2022-06-14 07:14:04.994291
# Unit test for function add_status_code
def test_add_status_code():
    new_status_code = 451

    @add_status_code(new_status_code)
    class TestStatusCode(SanicException):
        pass

    assert _sanic_exceptions[new_status_code] == TestStatusCode

# Generated at 2022-06-14 07:14:15.374461
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(409)
    class Conflict(SanicException):
        """
        **Status**: 409 Conflict
        """

        pass

    assert 409 in _sanic_exceptions
    assert issubclass(_sanic_exceptions[409], Conflict)

    @add_status_code(100)
    class Continue(SanicException):
        """
        **Status**: 100 Continue
        """

        pass

    assert 100 in _sanic_exceptions
    assert issubclass(_sanic_exceptions[100], Continue)

# Generated at 2022-06-14 07:14:19.884356
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        pass
    exc = TestException(message="test")
    assert exc.status_code == 400
    assert _sanic_exceptions[400] is TestException

# Generated at 2022-06-14 07:14:27.728529
# Unit test for function add_status_code
def test_add_status_code():
    assert 404 in _sanic_exceptions
    assert 400 in _sanic_exceptions
    assert 405 in _sanic_exceptions
    assert 500 in _sanic_exceptions
    assert 503 in _sanic_exceptions
    assert 408 in _sanic_exceptions
    assert 413 in _sanic_exceptions
    assert 416 in _sanic_exceptions
    assert 417 in _sanic_exceptions
    assert 403 in _sanic_exceptions
    assert 401 in _sanic_exceptions



# Generated at 2022-06-14 07:14:35.153354
# Unit test for function add_status_code
def test_add_status_code():
    class Hello(SanicException):
        pass

    @add_status_code(200)
    class Hey(SanicException):
        pass

    assert isinstance(Hey(), SanicException)
    assert Hey().status_code == 200

    @add_status_code(201, quiet=True)
    class Hi(SanicException):
        pass

    assert Hi().quiet == True
    assert Hi().status_code == 201

# Generated at 2022-06-14 07:14:38.179373
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class ErrorWithException(SanicException):
        pass

    assert ErrorWithException.status_code == 400

# Generated at 2022-06-14 07:14:44.578338
# Unit test for function add_status_code
def test_add_status_code():
    class Test(SanicException): pass
    assert 200 not in _sanic_exceptions
    add_status_code(200)(Test)
    assert 200 in _sanic_exceptions
    assert issubclass(_sanic_exceptions[200], SanicException)
    assert issubclass(Test, _sanic_exceptions[200])
    assert issubclass(Test, SanicException)

if __name__ == "__main__":
    test_add_status_code()

# Generated at 2022-06-14 07:14:57.312236
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(status_code=418)
    class TeaPotException(SanicException):
        pass

    test_exception = TeaPotException()
    assert test_exception.status_code == 418

    @add_status_code(status_code=1000)
    class CustomException(SanicException):
        pass

    test_exception = CustomException()
    assert test_exception.status_code == 1000
    assert test_exception.quiet is None

    @add_status_code(status_code=200, quiet=True)
    class CustomException2(SanicException):
        pass

    test_exception = CustomException2()
    assert test_exception.quiet is True
    assert test_exception.status_code == 200

# Generated at 2022-06-14 07:15:00.814042
# Unit test for function add_status_code
def test_add_status_code():
    # create a simple class
    @add_status_code(500)
    class ServerError(SanicException):
        pass

    assert ServerError.status_code == 500



# Generated at 2022-06-14 07:15:15.252540
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 400
    assert TestException.quiet == True

    try:
        raise TestException("Test Message")
    except TestException as e:
        assert e.status_code == 400

    @add_status_code(500, True)
    class TestException2(SanicException):
        pass

    assert TestException2.status_code == 500
    assert TestException2.quiet == True

    try:
        raise TestException2("Test Message")
    except TestException2 as e:
        assert e.status_code == 500

    @add_status_code(500, False)
    class TestException3(SanicException):
        pass

    assert TestException3.status_code == 500
    assert Test

# Generated at 2022-06-14 07:15:25.631686
# Unit test for function add_status_code
def test_add_status_code():
    # test status_code without quiet
    class MyException(Exception):
        pass

    add_status_code(333)(MyException)
    assert MyException.status_code == 333
    assert MyException.quiet is False

    # test status_code with quiet=True
    add_status_code(444, quiet=True)(MyException)
    assert MyException.status_code == 444
    assert MyException.quiet is True

    # test status_code with quiet=False
    add_status_code(444, quiet=False)(MyException)
    assert MyException.status_code == 444
    assert MyException.quiet is False

    # test status_code with quiet=None
    add_status_code(555, quiet=None)(MyException)
    assert MyException.status_code == 555
    assert MyException.quiet is True

# Generated at 2022-06-14 07:15:34.814213
# Unit test for function add_status_code
def test_add_status_code():
    """
    Register an exception to SanicException
    """
    @add_status_code(201)
    class CreateError(SanicException):
        """"""

    assert CreateError.status_code == 201
    assert _sanic_exceptions[201] == CreateError

    @add_status_code(403)
    class FailedError(SanicException):
        """"""

    assert FailedError.status_code == 403
    assert _sanic_exceptions[403] == FailedError

    @add_status_code(503)
    class MaintenanceError(SanicException):
        """"""

    assert MaintenanceError.status_code == 503
    assert _sanic_exceptions[503] == MaintenanceError

# Generated at 2022-06-14 07:15:49.214289
# Unit test for function add_status_code
def test_add_status_code():
    def test_func():
        class Test(SanicException):
            pass

        @add_status_code(4)
        class Test2(Test):
            pass

        @add_status_code(5, quiet=True)
        class Test3(Test):
            pass

        @add_status_code(6, quiet=False)
        class Test4(Test):
            pass

        @add_status_code(7, quiet=None)
        class Test5(Test):
            pass

        assert Test.status_code is None

        assert Test2.status_code == 4
        assert Test2.quiet is False

        assert Test3.status_code == 5
        assert Test3.quiet is True

        assert Test4.status_code == 6
        assert Test4.quiet is False

        assert Test5.status_code == 7

# Generated at 2022-06-14 07:15:56.472082
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404, True)
    class A(SanicException):
        pass

    @add_status_code(500)
    class B(SanicException):
        pass

    try:
        raise A("message")
    except SanicException as e:
        assert e.message == "message"
        assert e.status_code == 404
        assert e.quiet == True

    try:
        raise B("message")
    except SanicException as e:
        assert e.message == "message"
        assert e.status_code == 500
        assert e.quiet == False

    try:
        raise NotFound("message")
    except SanicException as e:
        assert e.message == "message"
        assert e.status_code == 404
        assert e.quiet == True


# Generated at 2022-06-14 07:16:03.451175
# Unit test for function add_status_code
def test_add_status_code():
    
    class NotFound(SanicException):
        pass

    # Test to see if the status code is being set
    assert NotFound.status_code == None
    add_status_code(404)(NotFound)
    assert NotFound.status_code == 404

    # Test to see if the exception is added to the dictionary
    assert _sanic_exceptions[404] == NotFound

# Generated at 2022-06-14 07:16:11.204298
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestException(SanicException):
        pass

    assert 200 in _sanic_exceptions
    assert isinstance(_sanic_exceptions[200], TestException)
    assert _sanic_exceptions[200].status_code == 200
    assert _sanic_exceptions[200].quiet is True


# Unit tests for class SanicException

# Generated at 2022-06-14 07:16:24.036137
# Unit test for function add_status_code
def test_add_status_code():
    # Test if add_status_code make a SanicException into a SanicException
    # with the correct status code and message
    @add_status_code(400)
    class TestException(SanicException):
        pass

    try:
        raise TestException('test')
    except TestException as e:
        assert e.status_code == 400
        assert e.args[0] == 'test'
    # Test nonquiet is processed as expected
    @add_status_code(500, quiet=True)
    class TestException2(SanicException):
        pass

    try:
        raise TestException2('test')
    except TestException2 as e:
        assert e.quiet is True
    # Test 500 mapping to nonquiet
    @add_status_code(500)
    class TestException3(SanicException):
        pass

# Generated at 2022-06-14 07:16:29.992360
# Unit test for function add_status_code
def test_add_status_code():
    sclass = add_status_code(200)(SanicException)
    assert sclass.status_code == 200

    sclass = add_status_code(201, quiet=True)(SanicException)
    assert sclass.status_code == 201
    assert sclass.quiet

    sclass = add_status_code(202)(SanicException)
    assert sclass.status_code == 202
    assert sclass.quiet

    sclass = add_status_code(203, quiet=False)(SanicException)
    assert sclass.status_code == 203
    assert not sclass.quiet

    sclass = add_status_code(500)(SanicException)
    assert sclass.status_code == 500
    assert not sclass.quiet

# Generated at 2022-06-14 07:16:34.844527
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(200)
    class TestException(Exception):
        pass

    assert _sanic_exceptions[200] == TestException
    assert TestException.status_code == 200

    # Quiet is default when status code is not 500
    assert TestException.quiet

    assert "quiet" not in _sanic_exceptions[500].__dict__

# Generated at 2022-06-14 07:16:51.906237
# Unit test for function add_status_code
def test_add_status_code():
    """
    Decorator used for adding exceptions to :class:`SanicException`.
    """
    @add_status_code(404)
    class TestExample(SanicException):
        pass

    assert TestExample


# Generated at 2022-06-14 07:16:56.348620
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code("status", quiet=False)
    class Foo(Exception):
        pass
    assert Foo.status_code == "status"
    assert Foo.quiet == False



# Generated at 2022-06-14 07:17:07.858091
# Unit test for function add_status_code
def test_add_status_code():
    # test for add_status_code
    # create new class
    @add_status_code(444)
    class TestAddStatusCode(SanicException):
        pass
    # test for new class
    assert TestAddStatusCode.status_code == 444
    # test for new class in _sanic_exceptions
    assert TestAddStatusCode in _sanic_exceptions.values()
    # create new class with quiet
    @add_status_code(444, True)
    class TestAddStatusCodeQuiet(SanicException):
        pass
    # test for new class with quiet
    assert TestAddStatusCodeQuiet.quiet == True
    # create new class without quiet
    @add_status_code(444, False)
    class TestAddStatusCodeNotQuiet(SanicException):
        pass
    # test for new class without

# Generated at 2022-06-14 07:17:13.209974
# Unit test for function add_status_code
def test_add_status_code():

    # unit test for function add_status_code
    # test whether AddStatusCode decorator is useful
    @add_status_code(111, quiet=True)
    class A(SanicException):
        pass

    assert A.status_code == 111
    assert A.quiet is True
    assert 111 in _sanic_exceptions
    assert isinstance(_sanic_exceptions[111](), A)



# Generated at 2022-06-14 07:17:21.005652
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class Test(SanicException):
        pass
    assert Test.status_code == 403
    assert _sanic_exceptions[403] == Test
    
    @add_status_code(403, quiet=True)
    class Test(SanicException):
        pass
    assert Test.quiet == True
    
    @add_status_code(403, quiet=False)
    class Test(SanicException):
        pass
    assert Test.quiet == False

# Generated at 2022-06-14 07:17:30.930225
# Unit test for function add_status_code
def test_add_status_code():
    """
    Test to verify that function add_status_code adds a custom SanicException to _sanic_exceptions
    """

    new_code = 420
    new_message = "Custom exception"
    new_exception_name = "CustomException"

    @add_status_code(new_code)
    class CustomException(SanicException):
        pass

    assert (
        _sanic_exceptions[new_code].__name__ == new_exception_name
    ), "SanicException was not added to _sanic_exceptions"
    assert (
        _sanic_exceptions[new_code](new_message).message == new_message
    ), "SanicException did not inherit SanicException"

# Generated at 2022-06-14 07:17:43.491430
# Unit test for function add_status_code
def test_add_status_code():
    class SanicException2(Exception):
        pass

    @add_status_code(600)
    class SanicException3(SanicException2):
        pass

    assert 600 in _sanic_exceptions
    assert _sanic_exceptions[600] == SanicException3
    assert SanicException3.status_code == 600
    assert SanicException3.quiet is False

    @add_status_code(500)
    class SanicException4(SanicException2):
        pass

    assert 500 in _sanic_exceptions
    assert _sanic_exceptions[500] == SanicException4
    assert SanicException4.status_code == 500
    assert SanicException4.quiet is False


# Generated at 2022-06-14 07:17:54.135593
# Unit test for function add_status_code
def test_add_status_code():
    """Unit test add_status_code function by creating two new exceptions using
    decorator add_status_code.

    :return: No return.
    """
    # Create new exception 1
    @add_status_code(403)
    class Forbidden_1(SanicException):
        """
        **Status**: 403 Forbidden
        """

    # Create new exception 2
    @add_status_code(503)
    class ServiceUnavailable_1(SanicException):
        """
        **Status**: 503 Service Unavailable
        """

    assert _sanic_exceptions[403] is Forbidden_1
    assert _sanic_exceptions[503] is ServiceUnavailable_1

# Generated at 2022-06-14 07:17:57.854968
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass

    add_status_code(400)(TestException)
    assert _sanic_exceptions[400] == TestException



# Generated at 2022-06-14 07:18:07.417767
# Unit test for function add_status_code
def test_add_status_code():
    class TestException(SanicException):
        pass
    
    def function_with_add_status_code(code, quiet=None):
        def class_decorator(cls):
            cls.status_code = code
            if quiet or quiet is None and code != 500:
                cls.quiet = True
            _sanic_exceptions[code] = cls
            return cls
        return class_decorator

    @function_with_add_status_code(202)
    class TestException2(TestException):
        pass

    assert TestException2.status_code == 202
    assert TestException2.quiet == True
    assert _sanic_exceptions[202] == TestException2

# Generated at 2022-06-14 07:18:40.024156
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(404)
    class X(SanicException):
        pass

    assert isinstance(X(), SanicException)
    assert X.status_code == 404
    assert _sanic_exceptions[404] == X

# Generated at 2022-06-14 07:18:44.001707
# Unit test for function add_status_code
def test_add_status_code():
    class xxx(SanicException):
        pass
    add_status_code(444)(xxx)
    assert _sanic_exceptions[444] == xxx

# Generated at 2022-06-14 07:18:52.339548
# Unit test for function add_status_code
def test_add_status_code():
    with pytest.raises(TypeError):
        class TestException(SanicException):
            pass
    assert isinstance(_sanic_exceptions[404], SanicException)
    assert issubclass(_sanic_exceptions[404], SanicException)
    assert not issubclass(_sanic_exceptions[404], BaseException)
    assert issubclass(_sanic_exceptions[404], NotFound)
    assert isinstance(_sanic_exceptions[404](), NotFound)
    assert isinstance(_sanic_exceptions[404](), SanicException)
    assert _sanic_exceptions[404](message="internal error").status_code == 404

# Generated at 2022-06-14 07:18:55.738345
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(400)
    class TestSanicException(SanicException):
        pass

    assert TestSanicException.status_code == 400

# Generated at 2022-06-14 07:18:59.921048
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(418)
    class FooException(SanicException):
        pass

    assert _sanic_exceptions[418] == FooException
    assert issubclass(FooException, SanicException)



# Generated at 2022-06-14 07:19:08.679518
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(403)
    class TestException(SanicException):
        pass
    assert issubclass(TestException, SanicException)
    assert 403 in _sanic_exceptions, "TestException not added to _sanic_exceptions"
    @add_status_code(319, quiet=True)
    class Test2(SanicException):
        pass
    assert Test2.quiet == True, "Test2.quiet is not True"
    @add_status_code(320, quiet=False)
    class Test3(SanicException):
        pass
    assert Test3.quiet == True, "Test3.quiet is not True"
    @add_status_code(321)
    class Test4(SanicException):
        pass
    assert Test4.quiet == True, "Test4.quiet is not True"

# Generated at 2022-06-14 07:19:13.483418
# Unit test for function add_status_code
def test_add_status_code():
    # Check the decorator works
    @add_status_code(400)
    class TestException(SanicException):
        pass

    assert TestException.status_code == 400
    assert TestException().status_code == 400



# Generated at 2022-06-14 07:19:16.842591
# Unit test for function add_status_code
def test_add_status_code():
    @add_status_code(422)
    class TestException(SanicException):
        pass

    assert _sanic_exceptions[422] == TestException
    assert TestException.quiet

# Generated at 2022-06-14 07:19:27.830681
# Unit test for function add_status_code
def test_add_status_code():
    from sanic.exceptions import add_status_code, ServerError

    @add_status_code(500)
    class ServerError500(Exception):
        pass

    # 400 is already added in add_status_code(400)
    assert ServerError500.status_code == 500
    assert ServerError500.quiet is True
    assert ServerError500.quiet is True
    assert ServerError500.quiet == ServerError.quiet
    assert ServerError500.status_code == 500
    # not set below, so default of False
    assert not ServerError.quiet

    # Both are ServerError, but we only added the decorator for ServerError500
    assert issubclass(ServerError, SanicException)
    assert issubclass(ServerError500, SanicException)

# Generated at 2022-06-14 07:19:32.539261
# Unit test for function add_status_code
def test_add_status_code():
    
    # Add new code to dictionary _sanic_exceptions
    add_status_code(200)

    # Check if 200 is a key
    if 200 in _sanic_exceptions:
        print("Unit test for function add_status_code passed")
    else:
        print("Unit test for function add_status_code failed")


# Generated at 2022-06-14 07:20:43.043135
# Unit test for function add_status_code
def test_add_status_code():
    __status_code__ = 404
    @add_status_code(__status_code__)
    class cls(SanicException):
        pass

    assert cls.status_code == __status_code__
    assert _sanic_exceptions.get(__status_code__) == cls

    __status_code__ = 404
    @add_status_code(__status_code__, True)
    class cls(SanicException):
        pass

    assert cls.status_code == __status_code__
    assert _sanic_exceptions.get(__status_code__) == cls
    assert cls.quiet == True

    __status_code__ = 400
    @add_status_code(__status_code__)
    class cls(SanicException):
        pass

# Generated at 2022-06-14 07:20:56.702800
# Unit test for function add_status_code
def test_add_status_code():
    """
    This function is designed for unit test.
    """
    # Test function add_status_code without quiet and status_code.
    @add_status_code(200)
    class Test_SanicException(Exception):
        pass

    # Test function add_status_code with True quiet and status_code.
    @add_status_code(300, quiet=True)
    class Test_SanicException2(Exception):
        pass

    # Test function add_status_code with False quiet and status_code.
    @add_status_code(300, quiet=False)
    class Test_SanicException3(Exception):
        pass

    # Test function add_status_code with None quiet and status_code.

# Generated at 2022-06-14 07:21:00.927502
# Unit test for function add_status_code
def test_add_status_code():
    add_status_code(200)
    assert _sanic_exceptions[200].status_code == 200
    add_status_code(500)
    assert _sanic_exceptions[500].status_code == 500

# Generated at 2022-06-14 07:21:14.594833
# Unit test for function add_status_code
def test_add_status_code():
    # pylint: disable=unused-variable,unused-argument

    @add_status_code(501, quiet=True)
    class NotImplemented(SanicException):
        """
        **Status**: 501 Not Implemented
        """

    assert _sanic_exceptions[501] == NotImplemented
    assert NotImplemented.quiet == True

    @add_status_code(502)
    class BadGateway(SanicException):
        """
        **Status**: 502 Bad Gateway
        """

    assert _sanic_exceptions[502] == BadGateway
    # pylint: disable=no-member
    assert BadGateway.quiet == True

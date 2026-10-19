

# Generated at 2022-06-14 04:23:35.071111
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test message")
    except ProgrammingError as e:
        assert str(e) == "This is a test message"


# Generated at 2022-06-14 04:23:39.483105
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Boom")
    except Exception as e:
        assert isinstance(e, ProgrammingError)
        assert e.__class__.__name__ == "ProgrammingError"
        assert str(e) == "Boom"


# Generated at 2022-06-14 04:23:42.041340
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as err:
        assert str(err) == "Test"


# Generated at 2022-06-14 04:23:45.494612
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A new error message")
    except ProgrammingError as e:
        assert "A new error message" in e.args[0]

# Generated at 2022-06-14 04:23:50.013953
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."
    else:
        assert False


# Generated at 2022-06-14 04:23:54.934212
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message="This is not expected")
        assert False, "ProgrammingError.passert didn't raise an exception when it should."
    except ProgrammingError as exc:
        assert str(exc) == "This is not expected", "The message is not the expected."

test_ProgrammingError()

# Generated at 2022-06-14 04:24:01.550448
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from unittest import TestCase

    # WHEN a ProgrammingError is instantiated WITHOUT a message THEN it is properly initialized
    exc = ProgrammingError()
    assert exc.args[0] == "Broken coherence. Check your code against domain logic to fix it."

    # WHEN a ProgrammingError is instantiated WITH a message THEN it is properly initialized
    exc = ProgrammingError("Error instantiated with message")
    assert exc.args[0] == "Error instantiated with message"


# Generated at 2022-06-14 04:24:04.902375
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Error occurred")
        assert(False)
    except ProgrammingError as e:
        assert(str(e) == "Error occurred")

# Generated at 2022-06-14 04:24:05.615071
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError()

# Generated at 2022-06-14 04:24:07.423218
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, "test"):
        pass

# Generated at 2022-06-14 04:24:14.179095
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test the exception :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert isinstance(e, Exception)
        assert str(e) == "Test"
    ProgrammingError.passert(True, "")
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert isinstance(e, Exception)
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:24:20.738662
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    def instanciate_ProgrammingError():
        from pypara.common.errors import ProgrammingError
        return ProgrammingError()

    def instanciate_ProgrammingError_with_msg():
        from pypara.common.errors import ProgrammingError
        return ProgrammingError("test")

    # Assert that the constructor of class ProgrammingError does not throw
    assert instanciate_ProgrammingError is not None
    assert instanciate_ProgrammingError_with_msg is not None


# Generated at 2022-06-14 04:24:25.282539
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of class ProgrammingError
    """
    try:
        ProgrammingError.passert(False, "This is a test")
    except ProgrammingError as e:
        print(e)

# Generated at 2022-06-14 04:24:29.199123
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Hello")
    except ProgrammingError as e:
        assert e.__str__() == "Hello"
    else:
        raise AssertionError("Nope")


# Generated at 2022-06-14 04:24:32.348179
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "test")
    except ProgrammingError as e:
        assert "test" in str(e)
    assert True

# Generated at 2022-06-14 04:24:35.033694
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("error")
    except ProgrammingError as ex:
        assert str(ex) == "error"


# Generated at 2022-06-14 04:24:43.117789
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test assert
    ProgrammingError.passert(True, None)
    assert True
    # Test assert with message
    ProgrammingError.passert(True, "MESSAGE")
    assert True
    # Test assert with wrong condition
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError:
        assert True
    else:
        assert False
    # Test assert with wrong condition and message
    try:
        ProgrammingError.passert(False, "MESSAGE")
    except ProgrammingError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:24:52.145040
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests if :py:class:`ProgrammingError` constructor raises always an exception with the given message.
    """
    from .testcase import PyParaTestCase

    class _testProgrammingError(PyParaTestCase):
        """
        Unit test for constructor of class :py:class:`ProgrammingError`.
        """

        def test_ProgrammingError(self):
            """
            Tests if :py:class:`ProgrammingError` constructor raises always an exception with the given message.
            """
            self.assertRaises(ProgrammingError, ProgrammingError, "Test")

    return _testProgrammingError


# Generated at 2022-06-14 04:24:55.078341
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Something bad happened")
    except ProgrammingError as err:
        assert type(err) is ProgrammingError
        assert str(err) == "Something bad happened"


# Generated at 2022-06-14 04:24:58.469707
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    msg = "test"
    try:
        raise ProgrammingError(msg)
    except ProgrammingError as err:
        assert msg == err.args[0]

# Generated at 2022-06-14 04:25:04.532537
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    passert = ProgrammingError.passert
    try:
        passert(False, "Test")
        assert 0, "Expected a ProgrammingError exception"
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:25:06.214920
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(False, "This is a test.")

# Generated at 2022-06-14 04:25:11.127029
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "")
        raise Exception("Error test failed.")
    except ProgrammingError:
        pass
    try:
        ProgrammingError.passert(False, "Error")
        raise Exception("Error test failed.")
    except ProgrammingError as error:
        assert str(error) == "Error"
    try:
        ProgrammingError.passert(False, None)
        raise Exception("Error test failed.")
    except ProgrammingError as error:
        assert str(error) == "Broken coherence. Check your code against domain logic to fix it."


# Regression test for issue #1

# Generated at 2022-06-14 04:25:21.753835
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test constructor (1)
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",), "Unexpected exception: %s" % e
    except Exception as e:
        assert False, "Unexpected exception: %s" % e

    # Test constructor (2)
    try:
        raise ProgrammingError("Custom message")
    except ProgrammingError as e:
        assert e.args == ("Custom message",), "Unexpected exception: %s" % e
    except Exception as e:
        assert False, "Unexpected exception: %s" % e


# Generated at 2022-06-14 04:25:28.282624
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Raise an error without message
    try:
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError:
        pass
    assert True
    # Raise an error with a message
    try:
        ProgrammingError.passert(False, "Some message")
        assert False
    except ProgrammingError:
        pass
    assert True
    # Ensure the the error is not raised with the condition is True
    ProgrammingError.passert(True, None)
    assert True

# Generated at 2022-06-14 04:25:32.960570
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Constructor of class :py:class:`ProgrammingError` should work as expected.
    """
    try:
        raise ProgrammingError("Hello")
    except ProgrammingError as ex:
        assert ex.args[0] == "Hello"


# Generated at 2022-06-14 04:25:34.842391
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    err = ProgrammingError("Testing ProgrammingError.")
    assert err.args[0] == "Testing ProgrammingError."

# Generated at 2022-06-14 04:25:41.937235
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        # Try with wrong condition, hence it should raise the exception
        ProgrammingError.passert(False, "This is an error message.")
        assert False, "This line should not be reachable."
    except ProgrammingError as ex:
        assert ex.args[0] == "This is an error message."

    # Try with good condition, hence it should not raise the exception
    ProgrammingError.passert(True, "This is an error message.")

# Generated at 2022-06-14 04:25:45.671620
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Dummy message")
    except ProgrammingError as e:
        assert str(e) == "Dummy message"


# Generated at 2022-06-14 04:25:48.901147
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Some explanation")
    except ProgrammingError as e:
        assert str(e) == "Some explanation"


# Generated at 2022-06-14 04:25:55.652998
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    assert ProgrammingError("Problem") is not None


# Generated at 2022-06-14 04:25:56.547674
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    pass

# Generated at 2022-06-14 04:26:04.040755
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of :py:class:`ProgrammingError`.

    :return: ``None`` in case of success.
    :raises AssertionError: In case that the test is failing.
    """
    try:
        ProgrammingError()
        ProgrammingError("Anything")
        # No exception should be triggered
        assert True
    except ProgrammingError:
        # This case should not happen
        assert False
    except:
        # This case should not happen
        assert False



# Generated at 2022-06-14 04:26:12.869042
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test case for :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as ex:
        assert ex.args[0] == "Test"
    try:
        raise ProgrammingError()
    except ProgrammingError as ex:
        assert ex.args[0] == "Broken coherence. Check your code against domain logic to fix it."


if __name__ == '__main__':
    import unittest
    unittest.main()

# Generated at 2022-06-14 04:26:17.817304
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Arrange
    err_message = "This is the expected error message."

    # Act

    # Assert
    try:
        raise ProgrammingError(err_message)
    except ProgrammingError as err:
        assert err.args == (err_message,)
        assert err.__str__() == err_message

# Generated at 2022-06-14 04:26:23.341850
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, None)
        assert False, "An exception was expected"
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it.", "Unexpected error message"

# Generated at 2022-06-14 04:26:26.665932
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "condition is not met.")
    except ProgrammingError as error:
        assert error.args[0] == "condition is not met."

# Generated at 2022-06-14 04:26:30.617329
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A message")
    except ProgrammingError as err:
        assert isinstance(err, ProgrammingError)
        assert str(err) == "A message"


# Generated at 2022-06-14 04:26:32.996179
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        pass
    else:
        assert False


# Generated at 2022-06-14 04:26:38.528221
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert isinstance(e.args[0], str)
    try:
        raise ProgrammingError("Message")
    except ProgrammingError as e:
        assert e.args[0] == "Message"


# Generated at 2022-06-14 04:26:51.978929
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.args is not None and len(e.args) == 1 and isinstance(e.args[0], str)


# Generated at 2022-06-14 04:26:53.983025
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    err = ProgrammingError("test message")
    assert err.args == ("test message",)


# Generated at 2022-06-14 04:26:56.887408
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Testing")
    except ProgrammingError as e:
        assert e.args[0] == "Testing"


# Generated at 2022-06-14 04:27:00.391340
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Testing ProgrammingError constructor")
    except ProgrammingError as e:
        assert str(e) == "Testing ProgrammingError constructor"


# Generated at 2022-06-14 04:27:03.112335
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("tested") as e:
        assert (str(e) == "tested")


# Generated at 2022-06-14 04:27:04.854656
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the ProgrammingError class constructor.

    :return: None
    """
    ProgrammingError()


# Generated at 2022-06-14 04:27:07.214403
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, "Test error"):
        pass

# Generated at 2022-06-14 04:27:12.727355
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(True, "Requested value is greater than accepted value")
    try:
        ProgrammingError.passert(False, "Requested value is greater than accepted value")
    except ProgrammingError:
        pass
    else:
        raise AssertionError("No exception is raised when it is expected.")

# Generated at 2022-06-14 04:27:15.575402
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Just check if a ProgrammingError can be raised and if it does not crash
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:27:17.204990
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError(None)
    ProgrammingError("dummy")


# Generated at 2022-06-14 04:27:39.694608
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for the constructor of class :py:class:`ProgrammingError`.
    """
    error = ProgrammingError("Hello, world!")
    assert error.args == ("Hello, world!",)
    assert str(error) == "Hello, world!"


# Generated at 2022-06-14 04:27:44.969622
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Testing the constructor with a message
    try:
        raise ProgrammingError("A breach of coherence has been found")
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert e.args == ("A breach of coherence has been found",)


# Generated at 2022-06-14 04:27:48.238536
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Forced exception.")
    except ProgrammingError as e:
        assert str(e) == "Forced exception."



# Generated at 2022-06-14 04:27:51.264865
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("just a test")
    except ProgrammingError as e:
        assert e.args[0] == "just a test"


# Generated at 2022-06-14 04:27:54.754366
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:27:58.195302
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    class DummyException(ProgrammingError):
        pass

    dummy_message = "Hello world"
    dummy_exception = DummyException(dummy_message)

    assert dummy_exception.args[0] == dummy_message


# Generated at 2022-06-14 04:28:02.039618
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    from ...util.test import assert_message_in_exception

    assert_message_in_exception(pytest, ProgrammingError, "Broken coherence. Check your code against domain logic to fix it.")


# Generated at 2022-06-14 04:28:04.885430
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("test")
    except Exception as error:
        assert error.args[0] == "test"


# Generated at 2022-06-14 04:28:07.669591
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises

    with raises(ProgrammingError):
        ProgrammingError.passert(False, "Message")

# Generated at 2022-06-14 04:28:10.463257
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("exception message")
    except ProgrammingError as e:
        assert e.args[0] == "exception message"


# Generated at 2022-06-14 04:28:54.599147
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "")
        raise Exception("Failed to raise ProgrammingError")
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:28:58.059741
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("This is a programming error")

# Generated at 2022-06-14 04:28:59.759595
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("this is an error")
    assert error.args == ("this is an error",)


# Generated at 2022-06-14 04:29:02.042544
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    err = ProgrammingError("Something went wrong")
    assert str(err) == "Something went wrong"


# Generated at 2022-06-14 04:29:04.603694
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    e = ProgrammingError("This is the message.")
    assert str(e) == "This is the message."


# Generated at 2022-06-14 04:29:10.091575
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    err = ProgrammingError()
    assert (None, None) == err.args
    assert "Broken coherence. Check your code against domain logic to fix it." == err.args[0]
    assert None is err.args[1]
    assert "Exc" in str(err)


# Generated at 2022-06-14 04:29:11.191972
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError("This is a programming error")


# Generated at 2022-06-14 04:29:16.004825
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Raises exception if condition is False
    try:
        ProgrammingError.passert(True, "")
    except ProgrammingError:
        assert False, "Unexpected ProgrammingError exception"

    # Raises exception if condition is False
    try:
        ProgrammingError.passert(False, "Error message")
    except ProgrammingError:
        assert True, "Expected ProgrammingError exception"
    else:
        assert False, "Expected ProgrammingError exception"

# Generated at 2022-06-14 04:29:18.483941
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "My message")
    except ProgrammingError as e:
        assert e.message == "My message"


# Generated at 2022-06-14 04:29:20.377948
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Some helpful message")
    except ProgrammingError as e:
        assert str(e) == "Some helpful message"



# Generated at 2022-06-14 04:30:58.459977
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test.")
    except ProgrammingError as error:
        assert error.args == ("This is a test.",)


# Generated at 2022-06-14 04:30:59.974463
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError("Error message")


# Generated at 2022-06-14 04:31:07.791010
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, "Test")
    except ProgrammingError as e:
        assert False, "Shouldn't raise exception"

    try:
        ProgrammingError.passert(False, "Test")
        assert False, "Should raise exception"
    except ProgrammingError as e:
        assert e.args[0] == "Test"

    try:
        ProgrammingError.passert(False, None)
        assert False, "Should raise exception"
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:31:10.079938
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError(message="Something is wrong.")



# Generated at 2022-06-14 04:31:14.317836
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Wrong code")
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
    else:
        assert False


# Generated at 2022-06-14 04:31:17.522239
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("error message")
    except Exception as e:
        assert type(e) is ProgrammingError
        assert str(e) == "error message"



# Generated at 2022-06-14 04:31:20.178212
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        assert False, "constructor not working"


# Generated at 2022-06-14 04:31:23.445169
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception)
    assert isinstance(
        ProgrammingError('There is something wrong in the code.'),
        ProgrammingError)
    assert ProgrammingError().__str__() == 'Broken coherence. Check your code against domain logic to fix it.'


# Generated at 2022-06-14 04:31:27.441656
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert isinstance(e, Exception)


# Generated at 2022-06-14 04:31:35.153749
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    try:
        with pytest.raises(ProgrammingError) as e:
            raise ProgrammingError()
        assert(str(e.value) == "Broken coherence. Check your code against domain logic to fix it.")
        with pytest.raises(ProgrammingError) as e:
            raise ProgrammingError("Something went wrong")
        assert(str(e.value) == "Something went wrong")
    except AssertionError:
        print("ProgrammingError class test failed")

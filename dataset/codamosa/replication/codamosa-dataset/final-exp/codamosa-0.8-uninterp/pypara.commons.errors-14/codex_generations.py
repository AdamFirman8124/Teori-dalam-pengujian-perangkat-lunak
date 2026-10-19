

# Generated at 2022-06-14 04:23:36.245959
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("This is an error")
    except ProgrammingError as error:
        assert error.args[0] == "This is an error"


# Generated at 2022-06-14 04:23:39.223972
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class ProgrammingError.
    """
    try:
        ProgrammingError("None")
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:23:49.740039
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError:
        assert False, "This branch must not be reached if the condition is ``True``."

    try:
        ProgrammingError.passert(False, "This is a custom message.")
    except ProgrammingError as e:
        assert e.args[0] == "This is a custom message.",\
            f"The exception was excepted to have the message {e.args[0]}."

    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it.",\
            f"The default message was excepted to be {e.args[0]}."

# Generated at 2022-06-14 04:23:52.815773
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is the programming error message")
    except ProgrammingError as e:
        assert(e.args[0] == "This is the programming error message")

# Generated at 2022-06-14 04:23:56.874812
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test  for constructor of clas ProgrammingError"""
    try:
        ProgrammingError.passert(False, "This is a message")
    except ProgrammingError as err:
        assert err.args[0] == "This is a message"
    else:
        assert False, "Expected ProgrammingError exception has not been raised!"

# Generated at 2022-06-14 04:24:03.420851
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from unittest.mock import patch
    from py3utils.log_utils import get_logger

    stderr_patch = patch('sys.stderr')
    with stderr_patch as stderr:
        try:
            raise ProgrammingError("Test test_ProgrammingError")
        except ProgrammingError as exc:
            get_logger().debug(exc)
            assert stderr.write.assert_called()
            assert stderr.flush.assert_called()

# Generated at 2022-06-14 04:24:10.122583
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests that the constructor of :py:class:`ProgrammingError` works as expected.

    :raises AssertionError: If any of the assertions fails.
    """
    exception = ProgrammingError("some message")
    assert exception.args == ("some message",)
    assert str(exception) == "some message"
    exception = ProgrammingError("some message", "some additional message")
    assert exception.args == ("some message", "some additional message")
    assert str(exception) == "some message: some additional message"


# Generated at 2022-06-14 04:24:13.385951
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)



# Generated at 2022-06-14 04:24:16.611396
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as exception:
        assert str(exception) == "Test"


# Generated at 2022-06-14 04:24:18.989655
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Hello")
    except ProgrammingError as ex:
        assert str(ex) == "Hello"


# Generated at 2022-06-14 04:24:24.774017
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError:
        ProgrammingError.passert(True, "")
    with ProgrammingError:
        ProgrammingError.passert(False, "")
    with ProgrammingError:
        ProgrammingError.passert(False, None)

# Generated at 2022-06-14 04:24:28.680183
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test constructor of class :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as e:
        assert str(e) == "Test"

# Generated at 2022-06-14 04:24:35.000661
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.
    """
    # Constructor with a message
    try:
        raise ProgrammingError("test")
    except ProgrammingError as exp:
        assert exp.args[0] == "test"

    # Constructor without a message
    try:
        raise ProgrammingError()
    except ProgrammingError as exp:
        assert exp.args[0] == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:24:38.221668
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test the instantiation of a :py:class:`ProgrammingError` instance.
    """
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert e.args == ("test",)


# Generated at 2022-06-14 04:24:43.598002
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, "Success"):
        pass
    try:
        with ProgrammingError.passert(False, "Expected error"):
            pass
    except ProgrammingError:
        pass
    else:
        assert False, "Expected error"

# Generated at 2022-06-14 04:24:49.478157
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(True, "")
    try:
        ProgrammingError.passert(False, None)
        assert False, "Should have raised"
    except ProgrammingError as e:
        print(e)
    try:
        ProgrammingError.passert(False, "")
        assert False, "Should have raised"
    except ProgrammingError as e:
        print(e)

# Generated at 2022-06-14 04:24:52.979814
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("TEST")
    except ProgrammingError as e:
        if str(e) != "TEST":
            raise e


# Generated at 2022-06-14 04:24:53.974046
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("Error")



# Generated at 2022-06-14 04:25:07.239518
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Testing standard instantiation.
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert e.args[0] == "test"
    else:
        assert False, "Except must be raised in this statement."

    # Testing failing assertion.
    try:
        ProgrammingError.passert(False, "test")
    except ProgrammingError as e:
        assert e.args[0] == "test"
    else:
        assert False, "Except must be raised in this statement."

    # Testing passing assertion.
    ProgrammingError.passert(True, "test")

    # Testing failing assertion with empty message.

# Generated at 2022-06-14 04:25:10.334401
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "BOOM")
    except ProgrammingError as e:
        assert str(e) == "BOOM", f"Expected error message to be 'BOOM' but is '{e}'"

# Generated at 2022-06-14 04:25:21.966000
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Check we get the proper message
    message = "Test message"
    error = ProgrammingError(message)
    assert isinstance(error, ProgrammingError)
    assert str(error) == message
    # Check we get a default message
    error = ProgrammingError()
    assert isinstance(error, ProgrammingError)
    assert str(error) == "Broken coherence. Check your code against domain logic to fix it."
    # Check that condition is checked
    ProgrammingError.passert(True, "Test message")
    # Check that condition is checked with default message
    ProgrammingError.passert(True, None)

# Generated at 2022-06-14 04:25:23.577233
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("TEST") as e:
        assert e.args[0] == "TEST"

# Generated at 2022-06-14 04:25:25.310677
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError(message = "Test")

# Generated at 2022-06-14 04:25:27.670703
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert(ProgrammingError)


if __name__ == '__main__':
    test_ProgrammingError()

# Generated at 2022-06-14 04:25:30.873679
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    msg = "This is a test message"
    try:
        raise ProgrammingError(msg)
    except ProgrammingError as err:
        assert(msg == str(err))


# Generated at 2022-06-14 04:25:40.574235
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "My message")
    except ProgrammingError as err:
        assert err.args[0] == "My message"
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as err:
        assert err.args[0] == "Broken coherence. Check your code against domain logic to fix it."
    try:
        ProgrammingError.passert(False, "")
    except ProgrammingError as err:
        assert err.args[0] == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:25:44.777807
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # pylint: disable=expression-not-assigned
    expected = "foo"
    try:
        raise ProgrammingError(expected)
    except ProgrammingError as programming_error:
        assert programming_error.message == expected


# Generated at 2022-06-14 04:25:48.200030
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("This is an error!")
    except:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:25:51.016073
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """ProgrammingError: Tests for constructor of class ProgrammingError."""
    with ProgrammingError("Error message"):
        pass


# Generated at 2022-06-14 04:25:53.183235
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("My message.")
    except ProgrammingError as error:
        if str(error) != "My message.":
            raise RuntimeError("ProgrammingError failed to store its message.")


# Generated at 2022-06-14 04:26:00.435169
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Test for the constructor of class ProgrammingError."""
    try:
        ProgrammingError()
    except ProgrammingError:
        pass
    else:
        raise Exception()


# Generated at 2022-06-14 04:26:03.665001
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except Exception as ex:
        assert isinstance(ex, ProgrammingError)
        assert ex.__cause__ is None


# Generated at 2022-06-14 04:26:12.928303
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of the class :py:class:`ProgrammingError`.

    :raise AssertionError: In case that any of the tests is broken.
    :rtype: None
    """
    # Test the behaviour of the constructor if the message is not provided
    try:
        raise ProgrammingError()
    except ProgrammingError as _:
        pass

    # Test the behaviour of the constructor if the message is provided
    try:
        raise ProgrammingError("This is an error")
    except ProgrammingError as _:
        pass


# Generated at 2022-06-14 04:26:22.579364
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Some message here :)")
    except ProgrammingError as e:
        print(e)
        assert str(e) == "Some message here :)"
        assert e.args[0] == "Some message here :)"

    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        print(e)
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."

    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError as e:
        print(e)
        assert False   # Should not get here

    print("Done!")

# Generated at 2022-06-14 04:26:24.889922
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Mock message")
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:26:28.619584
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Ouch!")
    except ProgrammingError as e:
        assert e.args[0] == "Ouch!"


# Generated at 2022-06-14 04:26:29.883015
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError(message="This is a dummy message.")
    assert error.message == "This is a dummy message."

# Generated at 2022-06-14 04:26:31.999339
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError(message="Error 1")
    ProgrammingError(message="Error 2")


# Generated at 2022-06-14 04:26:38.178962
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for :py:class:`ProgrammingError`.
    """
    try:
        ProgrammingError.passert(False, "Should fail")
        assert False, "Should have raised an exception"
    except ProgrammingError as e:
        assert "Should fail" == str(e)


# Generated at 2022-06-14 04:26:40.730334
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Hello World")
    except ProgrammingError as e:
        assert str(e) == "Hello World"


# Generated at 2022-06-14 04:26:53.140937
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test.")
    except ProgrammingError as e:
        assert e.args[0] == "This is a test."


# Generated at 2022-06-14 04:27:00.694123
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Raising the exception when no message is provided
    try:
        raise ProgrammingError()
    except ProgrammingError as error:
        assert str(error) == "Broken coherence. Check your code against domain logic to fix it."
    # Raising the exception with a fixed message
    try:
        raise ProgrammingError("A fixed message")
    except ProgrammingError as error:
        assert str(error) == "A fixed message"


# Generated at 2022-06-14 04:27:04.679230
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the ``__init__`` method of :py:class:`ProgrammingError`.
    """
    message = "Programming error"
    error = ProgrammingError(message)
    assert error.args[0] == message


# Generated at 2022-06-14 04:27:08.844390
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("An error has occurred.")
    except ProgrammingError as e:
        assert str(e) == "An error has occurred."


# Generated at 2022-06-14 04:27:11.290479
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:27:13.267932
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        ...
    except:
        assert False


# Generated at 2022-06-14 04:27:16.933485
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as e:
        assert str(e) == "Test"
        assert isinstance(e, Exception)

# Generated at 2022-06-14 04:27:22.205585
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests if the :py:class:`ProgrammingError` class is working as expected.
    """

    try:
        ProgrammingError.passert(False, "Something is wrong")
    except ProgrammingError as e:
        assert str(e) == "Something is wrong"
    else:
        raise AssertionError("ProgrammingError.passert did not work as expected.")

# Generated at 2022-06-14 04:27:25.925831
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as e:
        ProgrammingError("message")
    assert e.value.args[0] is "message"


# Generated at 2022-06-14 04:27:27.345734
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError



# Generated at 2022-06-14 04:27:48.822203
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test.")
    except ProgrammingError as ex:
        assert ex.args[0] == "This is a test."


# Generated at 2022-06-14 04:27:57.706600
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # The exception must be raised if the condition is not met
    broke_contract = False
    try:
        ProgrammingError.passert(False, "Precondition not met")
    except ProgrammingError:
        broke_contract = True
    if not broke_contract:
        raise AssertionError("Assertion in ProgrammingError class must be raised if the precondition is not met")

    # The exception must not be raised if the condition meets
    broke_contract = True
    try:
        ProgrammingError.passert(True, "Precondition not met")
    except ProgrammingError:
        broke_contract = False
    if broke_contract:
        raise AssertionError("Assertion in ProgrammingError class must not be raised if the precondition is met")

# Generated at 2022-06-14 04:28:01.794406
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Test for constructor of class ProgrammingError."""
    try:
        raise ProgrammingError("Unit test.")
    except ProgrammingError as error:
        assert str(error) == "Unit test."
    else:
        assert False, "No exception was raised."


# Generated at 2022-06-14 04:28:05.892734
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Error message to be raised.")
        assert False, "ProgrammingError did not raise an exception on condition False."
    except ProgrammingError as e:
        assert str(e) == "Error message to be raised."
    else:
        assert True

# Generated at 2022-06-14 04:28:09.701406
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:28:12.971113
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Creates an instance of :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Programming error"

# Generated at 2022-06-14 04:28:15.777218
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except Exception as e:
        assert isinstance(e, ProgrammingError)


# Generated at 2022-06-14 04:28:19.753298
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(True, "")
    caught = False
    try:
        ProgrammingError.passert(False, "")
    except ProgrammingError:
        assert True
        caught = True
    assert caught

# Generated at 2022-06-14 04:28:20.733251
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("test")

# Generated at 2022-06-14 04:28:23.981948
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Test constructor of class ProgrammingError."""
    try:
        raise ProgrammingError("One")
    except ProgrammingError as error:
        assert str(error) == "One"


# Generated at 2022-06-14 04:29:07.094279
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("message")
    except ProgrammingError as pe:
        assert str(pe) == "message"


# Generated at 2022-06-14 04:29:12.548002
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    exc = ProgrammingError
    assert isinstance(exc, type)
    assert issubclass(exc, Exception)
    assert exc.__name__ == "ProgrammingError"
    assert exc.__module__ == __name__
    assert exc.__qualname__ == "ProgrammingError"
    assert exc.__bases__ == (Exception,)

# Generated at 2022-06-14 04:29:21.319692
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, None)
        assert False, "ProgrammingError.passert didn't raise anything while it should've raised a ProgrammingError"
    except ProgrammingError:
        pass
    try:
        ProgrammingError.passert(False, "Should raise")
        assert False, "ProgrammingError.passert didn't raise anything while it should've raised a ProgrammingError"
    except ProgrammingError as e:
        assert str(e) == "Should raise", \
            "ProgrammingError.passert didn't raise the proper ProgrammingError"

# Generated at 2022-06-14 04:29:27.425016
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except Exception as e:
        assert isinstance(e, ProgrammingError)
        assert str(e) == ""
    try:
        ProgrammingError("Error message defined by programmer.")
    except Exception as e:
        assert isinstance(e, ProgrammingError)
        assert str(e) == "Error message defined by programmer."



# Generated at 2022-06-14 04:29:29.287324
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, "XXX"):
        pass

# Generated at 2022-06-14 04:29:34.597325
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, "OK"):
        pass
    try:
        with ProgrammingError.passert(False, "NOK"):
            pass
    except ProgrammingError as ex:
        assert str(ex) == "NOK"
        assert type(ex) is ProgrammingError
    else:
        raise AssertionError("Expected exception not raised.")

# Generated at 2022-06-14 04:29:37.636321
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A programming error occurred")
    except ProgrammingError as err:
        assert err.args[0] == "A programming error occurred"


# Generated at 2022-06-14 04:29:42.059172
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    passassert = ProgrammingError.passert
    try:
        passassert(False, "TestMessage")
    except ProgrammingError as e:
        assert e.args[0] == "TestMessage"
    try:
        passassert(False, None)
    except ProgrammingError as e:
        assert e.args[0].startswith("Broken coherence")

# Generated at 2022-06-14 04:29:46.397498
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    try:
        # noinspection PyTypeChecker
        raise ProgrammingError(1)
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:29:48.775359
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Exception raised for testing.")


# Generated at 2022-06-14 04:31:28.916415
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Something went wrong.")
        raise AssertionError("A ProgrammingError should have been raised.")
    except ProgrammingError as e:
        assert str(e) == "Something went wrong."


# Generated at 2022-06-14 04:31:32.591900
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    prg_error = ProgrammingError("Programming error!")
    assert prg_error.__class__ is ProgrammingError
    assert prg_error.args[0] == "Programming error!"


# Generated at 2022-06-14 04:31:35.417612
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Foo")
    except ProgrammingError as exception:
        assert exception.args[0] == "Foo"


# Generated at 2022-06-14 04:31:39.982023
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the :py:meth:`ProgrammingError.__init__` method.
    """

    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        err = e
    assert err.args == ("Broken coherence. Check your code against domain logic to fix it.",)

# Generated at 2022-06-14 04:31:42.042640
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:31:45.644026
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("message")
    except Exception as ex:
        assert str(ex) == "message"

# Generated at 2022-06-14 04:31:54.715474
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Suppress the message of the exception in order not to pollute the command line
    from contextlib import suppress
    from pypara.common.errors import ProgrammingError

    # Negative test
    with suppress(ProgrammingError):
        ProgrammingError.passert(False, None)
    with suppress(ProgrammingError):
        ProgrammingError.passert(False, "")
    with suppress(ProgrammingError):
        ProgrammingError.passert(False, "Whatever")

    # Positive test
    ProgrammingError.passert(True, None)
    ProgrammingError.passert(True, "")
    ProgrammingError.passert(True, "Whatever")

# Generated at 2022-06-14 04:32:01.087888
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of the :py:class:`ProgrammingError` class.

    :return: ``None``.
    """
    try:
        ProgrammingError("My own message.")
    except ProgrammingError as ex:
        print(f"Caught exception: {ex}")
        assert (ex.args[0] == "My own message.")
    else:
        assert (False)
    print("End.")


# Generated at 2022-06-14 04:32:03.626278
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, None)

# Generated at 2022-06-14 04:32:06.161682
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises

    with raises(ProgrammingError):
        ProgrammingError()

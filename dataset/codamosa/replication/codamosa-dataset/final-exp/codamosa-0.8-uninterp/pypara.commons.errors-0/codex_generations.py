

# Generated at 2022-06-14 04:23:38.577032
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as e:
        assert str(e) == "Test"


# Unit test of function ProgrammingError.passert

# Generated at 2022-06-14 04:23:49.936855
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    class MyAppException(ProgrammingError):
        pass

    class MyAppExceptionWithMessage(ProgrammingError):
        pass

    # Make sure that no error is raised if the condition is met
    ProgrammingError.passert(True, "Nothing should happen.")

    # Make sure that the provided message is used if it is provided
    try:
        ProgrammingError.passert(False, "This should be printed.")
    except ProgrammingError as e:
        assert e.args[0] == "This should be printed."

    # Make sure that the default message is used if no message is provided
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."

    # Make sure that the default message is used if no message is

# Generated at 2022-06-14 04:23:52.229480
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Should not raise this exception")
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:23:55.125771
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test message")
    except ProgrammingError as err:
        assert err.args == ("test message",)


# Generated at 2022-06-14 04:23:59.400917
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Tests the default constructor of this class."""
    error_message = "Test exception message"
    try:
        raise ProgrammingError(error_message)
    except ProgrammingError as error:
        assert error.args[0] == error_message



# Generated at 2022-06-14 04:24:01.163315
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError(None)
    except ProgrammingError:
        assert False


# Generated at 2022-06-14 04:24:08.642791
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    msg = "Broken coherence. Check your code against domain logic to fix it."
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert msg in str(e), "Empty programmer error message"
    try:
        raise ProgrammingError(msg)
    except ProgrammingError as e:
        assert msg in str(e), "Non empty programmer error message"
    try:
        ProgrammingError.passert(False, msg)
    except ProgrammingError as e:
        assert msg in str(e), "Programmer error message with assertion"

# Generated at 2022-06-14 04:24:10.859786
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError(message="This is a message")
    except ProgrammingError as e:
        assert str(e) == "This is a message"


# Generated at 2022-06-14 04:24:13.083756
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("foo")
    except ProgrammingError as e:
        assert str(e) == "foo"

# Generated at 2022-06-14 04:24:16.507471
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises

    # When
    with raises(ProgrammingError):
        ProgrammingError.passert(False, "You need to implement this method!")

# Generated at 2022-06-14 04:24:21.429652
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests :py:class:`ProgrammingError` constructor.
    """
    # Check that the error contains the message sent
    try:
        raise ProgrammingError("This is the message")
    except ProgrammingError as ex:
        assert str(ex) == "This is the message"


# Generated at 2022-06-14 04:24:23.800376
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError("Message of the error.")


# Generated at 2022-06-14 04:24:26.473168
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ProgrammingError
    """
    # Input parameter
    message = "Testing constructor of class ProgrammingError"

    # Should not happen
    try:
        raise ProgrammingError(message)
    except ProgrammingError as ex:
        assert str(ex) == message
    else:
        raise Exception



# Generated at 2022-06-14 04:24:29.772548
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("I am an error")
    except ProgrammingError as e:
        assert e.args[0] == "I am an error"


# Generated at 2022-06-14 04:24:33.556456
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a programming error!")  # pragma: no cover
    except ProgrammingError as e:
        assert str(e) == "This is a programming error!"


# Generated at 2022-06-14 04:24:34.998736
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:24:39.775812
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit-test the constructor of class ProgrammingError
    """
    # condition is True -> no exception
    ProgrammingError.passert(True, "Should not be raised")
    # condition is False -> exception shall be raised
    try:
        ProgrammingError.passert(False, "Should be raised")
    except ProgrammingError:
        pass
    else:
        raise AssertionError("Programming error exception expected but not raised")

# Generated at 2022-06-14 04:24:42.640034
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
        assert False
    except ProgrammingError:
        assert True


# Generated at 2022-06-14 04:24:45.790694
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests that an instance can be created.
    """
    try:
        raise ProgrammingError("Check your code.")
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:24:47.358937
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Inevitable error")


# Generated at 2022-06-14 04:24:52.830001
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        raise AssertionError("ProgrammingError missing")


# Generated at 2022-06-14 04:24:59.142819
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test suite for :py:class:`ProgrammingError` constructor.

    :return: ``None``
    """
    try:
        ProgrammingError.passert(False, "Test message")
        raise Exception("Passert did not raise ProgrammingError")
    except ProgrammingError:
        pass


if __name__ == "__main__":
    test_ProgrammingError()

# Generated at 2022-06-14 04:25:01.331963
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Arrange
    passed = False
    # Act

# Generated at 2022-06-14 04:25:03.346146
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Some message")
    except ProgrammingError as e:
        assert e.args[0] == "Some message"

# Generated at 2022-06-14 04:25:06.417686
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as error:
        assert error.args == ('Broken coherence. Check your code against domain logic to fix it.',)


# Generated at 2022-06-14 04:25:08.762975
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test the constructor of class ProgrammingError.
    """
    err = ProgrammingError("Some error")
    assert str(err) == "Some error"

# Generated at 2022-06-14 04:25:12.662771
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is an error")
    except ProgrammingError as error:
        assert str(error) == "This is an error"


# Generated at 2022-06-14 04:25:16.357330
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert(str(e) == "test")
    else:
        raise


# Generated at 2022-06-14 04:25:18.029711
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    msg = "This is a message"
    assert str(ProgrammingError(msg)) == msg

# Generated at 2022-06-14 04:25:19.944838
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except Exception as e:
        assert type(e) is ProgrammingError


# Generated at 2022-06-14 04:25:23.208897
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(False, "This is wrong")

# Generated at 2022-06-14 04:25:27.505325
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test the class constructor of :py:class:`ProgrammingError`
    """
    try:
        raise ProgrammingError("This is a test")
    except ProgrammingError as err:
        assert str(err) == "This is a test"



# Generated at 2022-06-14 04:25:32.170543
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("")
    except ProgrammingError as error:
        assert str(error) == ""
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as error:
        assert str(error) == "Test"



# Generated at 2022-06-14 04:25:42.698796
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the :py:class:`ProgrammingError` class constructor and its assert method.
    """
    try:
        ProgrammingError.passert(False, "The 1st error is to be raised")
        assert False, "A programming error was expected"
    except ProgrammingError as e:
        assert "The 1st error is to be raised" in str(e)
        ProgrammingError.passert(True, None)
        ProgrammingError.passert(True, "")
        ProgrammingError.passert(True, "The 2nd error is to be ignored")
    try:
        ProgrammingError.passert(False, None)
        assert False, "A programming error was expected"
    except ProgrammingError as e:
        assert "Check your code against domain logic to fix it." in str(e)

# Generated at 2022-06-14 04:25:45.924302
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Broken logic")
    except ProgrammingError as e:
        assert str(e) == "Broken logic"

# Generated at 2022-06-14 04:25:54.821268
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "foo")
    except ProgrammingError as err:
        assert str(err) == "foo"
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as err:
        assert str(err) == "Broken coherence. Check your code against domain logic to fix it."
    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError as err:
        assert False, "Expected not to raise an exception"

# Generated at 2022-06-14 04:25:56.889909
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        raise AssertionError()

# Generated at 2022-06-14 04:25:59.348692
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # type: () -> None

    try:
        ProgrammingError("Something is wrong here")
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:26:03.367063
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test failure")
    except ProgrammingError as pe:
        assert pe.args[0] == "Test failure"
    except Exception as e:
        assert False, e


# Generated at 2022-06-14 04:26:07.071572
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Test for ProgrammingError.__init__()."""
    # Initialize
    msg = "Testing ProgrammingError"

    # Assert
    assert ProgrammingError(msg).args[0] == msg

# Generated at 2022-06-14 04:26:15.873126
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError(message="Test error.")
    except Exception as e:
        assert isinstance(e, ProgrammingError)
        assert e.message == "Test error."

# Unit test of method passert of class ProgrammingError

# Generated at 2022-06-14 04:26:18.718141
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    exc = ProgrammingError("some error message")
    assert str(exc) == "some error message"

# Generated at 2022-06-14 04:26:22.183635
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("This is just a test")
    except ProgrammingError as e:
        assert(e.args == ("This is just a test", ))


# Generated at 2022-06-14 04:26:24.127578
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass

# Unit tests for methods of class ProgrammingError

# Generated at 2022-06-14 04:26:33.103508
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("")
    except ProgrammingError as e:
        assert e.args[0] == ""
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.args[0] == ""
    try:
        raise ProgrammingError("Error message")
    except ProgrammingError as e:
        assert e.args[0] == "Error message"
    try:
        raise ProgrammingError("Error message", "Meta-message")
    except ProgrammingError as e:
        assert e.args[0] == "Error message"
        assert e.args[1] == "Meta-message"


# Generated at 2022-06-14 04:26:37.556812
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception)
    msg = "Broken coherence. Check your code against domain logic to fix it."
    assert ProgrammingError(msg).args == (msg,)
    assert ProgrammingError(msg).__str__() == msg


# Generated at 2022-06-14 04:26:41.734544
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Testing ProgrammingError")
    except ProgrammingError as e:
        assert str(e) == "Testing ProgrammingError"
    else:
        assert False, "ProgrammingError not raised despite condition was False"

# Generated at 2022-06-14 04:26:46.534156
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError` and checks the exception message.

    :return: ``None``
    """
    try:
        raise ProgrammingError()
    except ProgrammingError as exception:
        assert str(exception) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:26:48.269072
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as exc:
        assert exc.args == ("Test",)

# Generated at 2022-06-14 04:26:50.912851
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Foo")
    except Exception as e:
        assert "Foo" in str(e)

# Generated at 2022-06-14 04:27:06.361958
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pypara.test.test_basics import assert_Passert_ProgrammingError

    assert_Passert_ProgrammingError(ProgrammingError, True, "any message")
    assert_Passert_ProgrammingError(ProgrammingError, False, "any message")
    assert_Passert_ProgrammingError(ProgrammingError, True, None)
    assert_Passert_ProgrammingError(ProgrammingError, False, None)

# Generated at 2022-06-14 04:27:09.571523
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError()

# Unit tests for member function passert of class ProgrammingError

# Generated at 2022-06-14 04:27:13.002287
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("It is broken!")
    except ProgrammingError as e:
        assert e.args[0] == "It is broken!"


# Generated at 2022-06-14 04:27:18.255833
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    # Trying to create an error with a message
    try:
        ProgrammingError("test")
        assert False, "Should be impossible to create this object"
    except TypeError:
        pass

    # Trying to create an error without a message
    try:
        ProgrammingError()
        assert False, "Should be impossible to create this object"
    except TypeError:
        pass



# Generated at 2022-06-14 04:27:22.637508
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Lorem ipsum")
    except ProgrammingError as ex:
        if str(ex) != "Lorem ipsum":
            raise AssertionError("Unexpected error message")
    else:
        raise AssertionError("ProgrammingError has not been raised")



# Generated at 2022-06-14 04:27:24.596105
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Failure")
    except ProgrammingError as e:
        assert str(e)=="Failure"

# Generated at 2022-06-14 04:27:29.161285
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("Test message")
    assert isinstance(error, ProgrammingError)
    assert isinstance(error, Exception)
    assert str(error) == "Test message"


# Generated at 2022-06-14 04:27:32.241655
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert "Broken coherence. Check your code against domain logic to fix it." in str(e)


# Generated at 2022-06-14 04:27:38.244799
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ProgrammingError."""
    try:
        ProgrammingError.passert(True, "This callback should not be called.")
        raise RuntimeError("Test has failed as the exception was not raised as expected")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
        ProgrammingError.passert(False, "This callback should be called.")
        pass

# Generated at 2022-06-14 04:27:41.733203
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert str(e).startswith("test")


# Generated at 2022-06-14 04:28:03.809231
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("bazinga")
    except ProgrammingError as pe:
        assert "bazinga" == str(pe)


# Generated at 2022-06-14 04:28:07.079117
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is an error message to be raised")
    except ProgrammingError as error:
        assert error.args[0] == "This is an error message to be raised"

# Generated at 2022-06-14 04:28:11.395085
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as e_info:
        ProgrammingError.passert(False, "The parameter was not allowed to be None.")
    assert e_info.match("Broken coherence. Check your code against domain logic to fix it.")


# Generated at 2022-06-14 04:28:15.188399
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test case for the constructor of :py:class:`ProgrammingError`.
    """
    error = ProgrammingError("Test.")
    assert error.args == ("Test.",)

# Generated at 2022-06-14 04:28:17.396958
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("a message")


# Generated at 2022-06-14 04:28:22.643135
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ProgrammingError"""
    passert = ProgrammingError.passert
    # Expected to execute without exceptions
    passert(True, None)
    # Expected to raise ProgrammingError
    passert(False, None)
    passert(False, "Test message")

# Generated at 2022-06-14 04:28:27.534724
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test message")
    except ProgrammingError as e:
        assert str(e) == "Test message"
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)

# Generated at 2022-06-14 04:28:28.682390
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError(message="This is a test error...")

# Generated at 2022-06-14 04:28:31.068976
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test error")
    except ProgrammingError as e:
        assert str(e) == "Test error"



# Generated at 2022-06-14 04:28:34.095056
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Testing the constructor of class ProgrammingError.")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:29:18.918305
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # The constructor of ProgrammingError is not supposed to be directly used. 
    # It will be raised only when calling the class method passert.
    error = ProgrammingError("An expected error for unit testing")
    assert str(error) == "An expected error for unit testing"


# Generated at 2022-06-14 04:29:25.698977
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    # Check that it fails if the condition is False
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError:
        pass
    else:
        assert False

    # Check that it works well if the condition is True
    ProgrammingError.passert(True, None)

    # Check that it fails with a non-empty message
    try:
        ProgrammingError.passert(False, "Message")
    except ProgrammingError as err:
        assert err.args[0] == "Message"
    else:
        assert False

# Generated at 2022-06-14 04:29:28.074473
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    err = ProgrammingError("An error happened.")
    assert str(err) == "An error happened."


# Generated at 2022-06-14 04:29:30.804253
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("foo")
    except ProgrammingError as e:
        assert str(e) == "foo"


# Generated at 2022-06-14 04:29:34.926400
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError):
        ProgrammingError()
    with raises(ProgrammingError):
        ProgrammingError(None)
    with raises(ProgrammingError):
        ProgrammingError("Broken coherence. Check your code against domain logic to fix it.")


# Generated at 2022-06-14 04:29:35.775490
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError


# Generated at 2022-06-14 04:29:38.066182
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Boom!")
    except ProgrammingError as e:
        assert e.args == ("Boom!",)



# Generated at 2022-06-14 04:29:39.262677
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("Test ProgrammingError")

# Generated at 2022-06-14 04:29:44.879115
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def _test_ProgrammingError_succeed():
        ProgrammingError.passert(condition=True, message="")

    def _test_ProgrammingError_failed():
        try:
            ProgrammingError.passert(condition=False, message="")
        except Exception as e:
            assert isinstance(e, ProgrammingError)
            assert e.args == ("",)

    _test_ProgrammingError_succeed()
    _test_ProgrammingError_failed()

# Generated at 2022-06-14 04:29:49.430638
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
        raise AssertionError("Exception was not raised.")
    except Exception as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:31:28.012184
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError(message = "A message")


# Generated at 2022-06-14 04:31:33.554942
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Checks that :py:class:`ProgrammingError` is raised when you expect it.

    It is expected that it can be raised whenever the constructor is called.
    """

    try:
        raise ProgrammingError("This is a programming error.")
    except ProgrammingError as error:
        assert error.args == ("This is a programming error.",)


# Generated at 2022-06-14 04:31:35.045487
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError(message="The error message"):
        pass


# Generated at 2022-06-14 04:31:38.122168
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        message = "Expected this error to be triggered."
        ProgrammingError.passert(False, message)
    except ProgrammingError as exception:
        assert exception.args == (message,)

# Generated at 2022-06-14 04:31:41.678741
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is a test!")
    except ProgrammingError as e:
        assert "This is a test!" == e.args[0]
        return
    assert False

# Generated at 2022-06-14 04:31:47.218698
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Unimplemented method. Check your code against domain logic to fix it.")
    except ProgrammingError as error:
        assert error.args[0] == "Unimplemented method. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:31:48.404830
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(True, "will be ignored")

# Generated at 2022-06-14 04:31:51.386805
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test messaging.")
    except ProgrammingError as ex:
        print(ex)
    assert True

# Generated at 2022-06-14 04:31:53.172330
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError.__doc__
    exc = ProgrammingError("message")
    assert exc.args == ("message", )


# Generated at 2022-06-14 04:31:55.703980
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert str(ProgrammingError("Just a test")) == "Just a test"


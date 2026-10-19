

# Generated at 2022-06-14 04:23:34.955669
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError()

# Generated at 2022-06-14 04:23:38.055139
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Expected to pass")
    except ProgrammingError as e:
        assert e.args[0] == "Expected to pass"


# Generated at 2022-06-14 04:23:40.829236
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError(message="coherent")
    except ProgrammingError as err:
        assert str(err) == "coherent"


# Generated at 2022-06-14 04:23:44.984647
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Broken coherence. Check your code against domain logic to fix it.")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:23:47.388975
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError()
    assert str(error) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:23:50.415928
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Here I am!")
    except ProgrammingError as e:
        assert str(e) == "Here I am!"


# Generated at 2022-06-14 04:23:53.162402
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, message="test message")
    except ProgrammingError as e:
        assert str(e) == "test message"


# Generated at 2022-06-14 04:23:55.413139
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError, match="test"):
        ProgrammingError.passert(False, message="test")

# Generated at 2022-06-14 04:23:57.961974
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        raise Exception("Error assertion.")


# Generated at 2022-06-14 04:23:59.855826
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # This is a not unit test but a functional test.
    ProgrammingError()


# Generated at 2022-06-14 04:24:05.088620
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, message="KOKO")
    except ProgrammingError as e:
        pass
    else:
        raise AssertionError("The condition should be False.")

# Generated at 2022-06-14 04:24:07.362281
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pypara.error import ProgrammingError as P
    P(message = "Whatever")


# Generated at 2022-06-14 04:24:19.984245
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # expect no error thrown
    ProgrammingError.passert(True, None)
    ProgrammingError.passert(True, "")
    ProgrammingError.passert(True, "Foo!")

    # expect a ProgrammingError raised
    try:
        # noinspection PyTypeChecker
        ProgrammingError.passert(False, None)
        raise Exception("expected a ProgrammingError")
    except ProgrammingError as e:
        assert str(e) == 'Broken coherence. Check your code against domain logic to fix it.'

    try:
        # noinspection PyTypeChecker
        ProgrammingError.passert(False, "")
        raise Exception("expected a ProgrammingError")
    except ProgrammingError as e:
        assert str(e) == 'Broken coherence. Check your code against domain logic to fix it.'


# Generated at 2022-06-14 04:24:31.584119
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test that passing True as condition does not raise anything
    ProgrammingError.passert(True, "message")

    # Test that passing None as condition raises ProgrammingError
    try:
        ProgrammingError.passert(False, "message")
    except ProgrammingError:
        pass
    else:
        raise AssertionError("ProgrammingError not raised")

    # Test that passing None as condition raises ProgrammingError
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError:
        pass
    else:
        raise AssertionError("ProgrammingError not raised")


if __name__ == "__main__":

    from pytest import main

    main([__file__])

# Generated at 2022-06-14 04:24:35.580060
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "a message")
    except ProgrammingError as e:
        assert e.args == ("a message",)
        return
    raise AssertionError("ProgrammingError.passert() failed to raise ProgrammingError")

# Generated at 2022-06-14 04:24:40.493215
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests :py:meth:`ProgrammingError` constructor.
    """
    try:
        raise ProgrammingError("Testing ProgrammingError")
    except ProgrammingError as e:
        assert str(e) == "Testing ProgrammingError"


# Generated at 2022-06-14 04:24:44.641489
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("")
    except ProgrammingError as error:
        assert str(error) == "Broken coherence. Check your code against domain logic to fix it."



# Generated at 2022-06-14 04:24:47.694430
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as pe:
        assert str(pe) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:24:51.572674
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit testing of :py:class:`ProgrammingError`.
    """
    try:
        ProgrammingError("Error message")
    except:
        raise AssertionError("Error in exception.")


# Generated at 2022-06-14 04:24:55.275203
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests that the constructor of the :py:class:`ProgrammingError` does not raise any exception.
    """
    error = ProgrammingError("Testing a programming error.")
    assert isinstance(error, ProgrammingError)
    assert isinstance(error, Exception)


# Generated at 2022-06-14 04:24:59.906359
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test case for constructor of class ProgrammingError.
    """
    try:
        ProgrammingError("This is a message")
        assert False
    except ProgrammingError as error:
        assert error.args[0] == "This is a message"


# Generated at 2022-06-14 04:25:03.542326
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Everything is just right!")
    except ProgrammingError as error:
        assert error.args[0] == "Everything is just right!"

# Generated at 2022-06-14 04:25:06.622205
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Auditing is necessary")
    except ProgrammingError as ex:
        assert str(ex) == "Auditing is necessary"


# Generated at 2022-06-14 04:25:08.433076
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("error")
    except ProgrammingError as e:
        assert str(e) == "error"

# Generated at 2022-06-14 04:25:14.935198
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # type: () -> None
    from pytest import raises
    from .util import assert_error_message

    error = ProgrammingError("Custom message")
    assert_error_message(error, "Custom message")

    with raises(ProgrammingError):
        ProgrammingError.passert(False, "Custom message")


# Generated at 2022-06-14 04:25:17.551164
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Some error.")
    except ProgrammingError as pe:
        assert str(pe) == "Some error."


# Generated at 2022-06-14 04:25:18.720571
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    raise ProgrammingError("Test")

# Generated at 2022-06-14 04:25:25.600075
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is a test.")
        assert False
    except ProgrammingError as e:
        assert str(e) == "This is a test."
    try:
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    ProgrammingError.passert(True, "This is a test.")

# Main program for unit testing
if __name__ == "__main__":
    test_ProgrammingError()

# Generated at 2022-06-14 04:25:28.401773
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("a message")
    except ProgrammingError as e:
        assert str(e) == "a message"



# Generated at 2022-06-14 04:25:32.170743
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is an error!")
    except ProgrammingError as e:
        assert str(e) == "This is an error!"


# Generated at 2022-06-14 04:25:35.298445
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("An error has occurred.")
    assert error.args == "An error has occurred."


# Generated at 2022-06-14 04:25:38.160623
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as err:
        assert str(err) == "Test"



# Generated at 2022-06-14 04:25:40.890565
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Message")
    except ProgrammingError as e:
        assert e.args == ("Message",)


# Generated at 2022-06-14 04:25:43.734225
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("")
    except Exception as e:
        assert isinstance(e, ProgrammingError)


# Generated at 2022-06-14 04:25:57.210203
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Raising the error
    try:
        raise ProgrammingError("Programming error")
    except ProgrammingError as ex:
        assert str(ex) == "Programming error"
    # Assertion
    try:
        ProgrammingError.passert(True, "Something is wrong")
    except ProgrammingError as ex:
        assert False
    try:
        ProgrammingError.passert(False, "Something is wrong")
        assert False
    except ProgrammingError as ex:
        assert str(ex) == "Something is wrong"
    try:
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError as ex:
        assert str(ex) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:25:59.628441
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as ex:
        ProgrammingError("error message")
    assert str(ex.value) == "error message"

# Generated at 2022-06-14 04:26:01.858489
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("foo")
    except ProgrammingError as exception:
        assert exception.args == ("foo",)

# Generated at 2022-06-14 04:26:09.527242
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=True, message="It should not raise the exception")
    except ProgrammingError as e:
        assert False, "Should not raise the exception"
    try:
        ProgrammingError.passert(condition=False, message="It should raise the exception")
    except ProgrammingError as e:
        assert True, "Should raise the exception"
        assert e.args[0] == "It should raise the exception"

# Generated at 2022-06-14 04:26:12.733077
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test message")

    except ProgrammingError as e:
        assert e.args[0] == "Test message"


# Generated at 2022-06-14 04:26:16.495460
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for the constructor of the :py:class:`ProgrammingError` exception.
    """
    try:
        raise ProgrammingError("Some message")
    except ProgrammingError as ex:
        assert ex.args[0] == "Some message"

# Generated at 2022-06-14 04:26:20.284882
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    err = ProgrammingError("This is a test")
    assert str(err) == "This is a test"



# Generated at 2022-06-14 04:26:24.184126
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test error")
    except Exception as ex:
        assert ex.__class__ == ProgrammingError
        assert str(ex) == "Test error"


# Generated at 2022-06-14 04:26:28.556106
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Foo")
    except ProgrammingError as e:
        assert(str(e) == "Foo")

    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert(str(e) == "Broken coherence. Check your code against domain logic to fix it.")

# Generated at 2022-06-14 04:26:32.416313
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:26:35.193767
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("example")
    except ProgrammingError as e:
        assert e.args[0] == "example"


# Generated at 2022-06-14 04:26:40.223823
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        with pytest.raises(ProgrammingError):
            ProgrammingError.passert(False, "This is a test")
    except Exception as e:
        pytest.fail(f"Raised exception was not as expected: {e}")

# Generated at 2022-06-14 04:26:43.310886
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Verify constructor")
    except ProgrammingError as e:
        assert str(e) == "Verify constructor"


# Generated at 2022-06-14 04:26:50.676852
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, "")
    except ProgrammingError as e:
        assert False, "Unexpected ProgrammingError: {}".format(e)
    try:
        ProgrammingError.passert(False, "123")
        assert False, "Expected ProgrammingError!"
    except ProgrammingError as e:
        assert e.args[0] == "123", \
            "Expected error message: [123], found: [{}]".format(e.args[0])

# Generated at 2022-06-14 04:26:55.022152
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message="")
        assert False, "This line should not be reached"
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:27:02.435242
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception)
    assert ProgrammingError.__doc__.startswith("Provides a programming error exception.")
    with pytest.raises(ProgrammingError) as exc_info:
        ProgrammingError.passert(False, "Test")
    assert str(exc_info.value) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:27:05.875418
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Message")
    except ProgrammingError as err:
        assert err.args[0] == "Message"

# Generated at 2022-06-14 04:27:08.148231
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("The 'condition' is not fulfilled"):
        pass

# Generated at 2022-06-14 04:27:16.000727
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of the exception.

    :raise AssertionError: In case that the test fails.
    """
    import pytest
    try:
        raise ProgrammingError("Everything is fine")
    except ProgrammingError as e:
        assert str(e) == "Everything is fine"
    with pytest.raises(ProgrammingError, match="Broken coherence"):
        ProgrammingError.passert(False, "Broken coherence")

# Test the constructor of class ProgrammingError
test_ProgrammingError()

# Generated at 2022-06-14 04:27:17.835455
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "")

# Generated at 2022-06-14 04:27:19.922602
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("The message")
    assert error.__class__.__name__ == "ProgrammingError"

# Generated at 2022-06-14 04:27:24.402549
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests for the :py:class:`ProgrammingError` class.
    """

    # Expected exception when the condition is not fulfilled
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(condition=False, message="This is an error!")
    # No exception when the condition is fulfilled
    ProgrammingError.passert(condition=True, message="This is an error!")

# EOF

# Generated at 2022-06-14 04:27:28.093571
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        assert False


# Generated at 2022-06-14 04:27:31.153138
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    message = "error message"
    try:
        ProgrammingError(message)
    except ProgrammingError as e:
        assert str(e) == message


# Generated at 2022-06-14 04:27:35.408746
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError.passert(False, "This is an error message")

    assert "This is an error message" in str(excinfo.value)



# Generated at 2022-06-14 04:27:38.044252
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Some message")
    except ProgrammingError as e:
        assert str(e) == "Some message"


# Generated at 2022-06-14 04:27:43.664803
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Given
    message = "It failed."

    # When
    try:
        raise ProgrammingError(message)
    except ProgrammingError as error:
        # Then
        assert str(error) == message


# Generated at 2022-06-14 04:27:55.703134
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Unit test for constructor of class ProgrammingError
    def test_ctor():
        try:
            raise ProgrammingError()        # pylint: disable=E0710
        except ProgrammingError as e:
            assert not e.args               # pylint: disable=E1133
            assert not e.with_traceback()   # pylint: disable=E1101,W0212
            assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
            # Adding a message
            try:
                raise ProgrammingError("Rats!")
            except ProgrammingError as e:
                assert e.args              # pylint: disable=E1133
                assert e.args[0] == "Rats!"
                assert str(e) == "Rats!"
    # Unit test for method passert of class ProgrammingError


# Generated at 2022-06-14 04:27:58.842379
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "test")
    except ProgrammingError:
        pass
    else:
        assert True

# Generated at 2022-06-14 04:28:01.317890
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Fatal error")
    except ProgrammingError as e:
        assert e.args[0] == "Fatal error"

# Generated at 2022-06-14 04:28:08.506856
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error_message = "This is a test."
    correctness = True
    try:
        # Act
        ProgrammingError.passert(False, error_message)
    except ProgrammingError as e:
        # Assert
        assert isinstance(e, ProgrammingError)
        assert e.args and len(e.args) == 1
        assert e.args[0] == error_message
        # Correct execution
        correctness = True
    finally:
        assert correctness
        

# Generated at 2022-06-14 04:28:10.368950
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test failed.")
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:28:13.163284
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Foo")



# Generated at 2022-06-14 04:28:15.474471
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    e = ProgrammingError("Test error")
    assert isinstance(e, ProgrammingError)



# Generated at 2022-06-14 04:28:21.241479
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ProgrammingError."""
    try:
        ProgrammingError.passert(False, message="Just testing")
        raise Exception("ProgrammingError was not raised. Can not continue with the unit test.")
    except ProgrammingError as e:
        assert str(e) == "Just testing"

# Generated at 2022-06-14 04:28:27.194096
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception), "ProgrammingError is not a subclass of Exception"
    assert issubclass(ProgrammingError, RuntimeError), "ProgrammingError is not a subclass of RuntimeError"
    assert ProgrammingError.__bases__ == (Exception,), "ProgrammingError must have only one superclass, Exception"
    assert ProgrammingError.__doc__, "ProgrammingError must have a docstring"


# Generated at 2022-06-14 04:28:32.555760
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as ex:
        assert str(ex) == "Test"


# Generated at 2022-06-14 04:28:34.701617
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError):
        ProgrammingError(message="Error raised after assertion")



# Generated at 2022-06-14 04:28:41.599087
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests :py:class:`ProgrammingError`.
    """
    try:
        ProgrammingError.passert(False, "Should not pass this check.")
    except ProgrammingError as exception:
        assert str(exception) == "Should not pass this check."

    try:
        ProgrammingError.passert(True, "Should pass this check.")
    except Exception:
        assert False

# Generated at 2022-06-14 04:28:45.358538
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError as e:
        assert False, "Programming Error should not have been raised"
    try:
        ProgrammingError.passert(False, None)
        assert False, "Programming Error should have been raised"
    except ProgrammingError as e:
        assert True, "Programming Error should have been raised"

# Generated at 2022-06-14 04:28:52.744989
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    # Test the default constructor
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    # Test a constructor with error message
    try:
        raise ProgrammingError("A message")
    except ProgrammingError:
        pass
    # Test condition
    with raises(ProgrammingError):
        ProgrammingError.passert(False, "We raise an exception")

# Generated at 2022-06-14 04:28:56.388084
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test.")
    except ProgrammingError as e:
        assert "This is a test." in str(e)

# Unit tests for method passert of class ProgrammingError

# Generated at 2022-06-14 04:28:59.631145
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."



# Generated at 2022-06-14 04:29:07.094223
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "Broken coherence")
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, None)
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "")
    ProgrammingError.passert(True, "")
    ProgrammingError.passert(True, None)

# Generated at 2022-06-14 04:29:13.409116
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the :py:class:`ProgrammingError` constructor.
    """
    ProgrammingError.passert(True, "Message")
    try:
        ProgrammingError.passert(False, "Message")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    except Exception:
        assert False, "ProgrammingError was not raised."

# Generated at 2022-06-14 04:29:16.822207
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError

    except ProgrammingError:
        pass

    except Exception:
        assert False, "Unexpected exception raised."

    assert True, "Exception not raised."


# Generated at 2022-06-14 04:29:25.623976
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "test")
        assert False
    except ProgrammingError as e:
        assert str(e) == "test"



# Generated at 2022-06-14 04:29:29.101454
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:29:33.060725
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False,
                                 "This is a test for the constructor of the class ProgrammingError")
        assert False
    except ProgrammingError as e:
        assert str(e) == "This is a test for the constructor of the class ProgrammingError"

# Generated at 2022-06-14 04:29:39.438386
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, "")
        ProgrammingError.passert(False, "")

        # If we reach this line then it means that the assertion has failed
        raise AssertionError("This line is not supposed to be reached")

    except ProgrammingError:
        return

    # If we reach this line then it means that the assertion has failed
    raise AssertionError("This line is not supposed to be reached")



# Generated at 2022-06-14 04:29:41.857669
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test")
    except ProgrammingError as error:
        assert error.args[0] == "This is a test"


# Generated at 2022-06-14 04:29:44.879605
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of class ProgrammingError.

    Since the class does not provide any functionality, the unit test checks that it does not raise any exceptions.
    """

    error = ProgrammingError("Test")
    assert str(error) == "Test"

# Generated at 2022-06-14 04:29:48.903121
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, message="Failed")
        assert False, "Should not reach this point"
    except ProgrammingError as exception:
        assert exception.__str__() == "Failed"

# Generated at 2022-06-14 04:29:55.549985
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "custom message")
    except ProgrammingError as e:
        assert str(e) == "custom message"
    try:
        ProgrammingError.passert(False, "")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:30:00.326064
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Custom message")
    except Exception as e:
        assert e.args == ("Custom message",)

    try:
        ProgrammingError.passert(False, None)
    except Exception as e:
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)

# Generated at 2022-06-14 04:30:03.076519
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("This is an error.")
        assert False, "The constructor of class ProgrammingError should raise an exception."
    except ProgrammingError as e:
        assert str(e) == "This is an error.", "The exception message has not been properly defined."


# Generated at 2022-06-14 04:30:21.835483
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as err:
        ProgrammingError.passert(condition=False, message="")
    assert "Broken coherence. Check your code against domain logic to fix it." in str(err.value)
    ProgrammingError.passert(condition=True, message="")

# Generated at 2022-06-14 04:30:24.520842
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "This error is expected.")

# Generated at 2022-06-14 04:30:26.895937
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError("Test ProgrammingError passert")



# Generated at 2022-06-14 04:30:30.971465
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Wrong usage of parameters")
    except ProgrammingError as err:
        assert(err.args[0] == "Wrong usage of parameters")


# Generated at 2022-06-14 04:30:35.168206
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests constructor of class ProgrammingError.
    """
    try:
        ProgrammingError()
    except:  # noqa: E722
        pass
    else:
        assert False, "Expected exception not thrown"

# Generated at 2022-06-14 04:30:38.513417
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    new_error = ProgrammingError()
    assert new_error.args == tuple()
    new_error = ProgrammingError("Some error message.")
    assert new_error.args == ("Some error message.",)

# Generated at 2022-06-14 04:30:40.641664
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:30:43.977760
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    from pypara.util.exception import ProgrammingError
    with raises(ProgrammingError):
        raise ProgrammingError()


# Generated at 2022-06-14 04:30:45.815140
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("This is a message"):
        raise ProgrammingError

# Generated at 2022-06-14 04:30:49.544843
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a message")
    except ProgrammingError as e:
        assert e.args[0] == "This is a message"


# Generated at 2022-06-14 04:31:24.630847
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    try:
        ProgrammingError.passert(False, "message")
    except ProgrammingError as e:
        assert "message" == e.args[0]
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert "Broken coherence. Check your code against domain logic to fix it." == e.args[0]
    with pytest.raises(ProgrammingError) as e:
        ProgrammingError.passert(False, "")
    assert "Broken coherence. Check your code against domain logic to fix it." == e.value.args[0]
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, None)
    ProgrammingError.passert(True, "message")

# Generated at 2022-06-14 04:31:27.730769
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:31:30.982221
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a message")
    except ProgrammingError as error:
        assert str(error) == "This is a message"


# Generated at 2022-06-14 04:31:33.955327
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:31:38.874357
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(True, "")
    ProgrammingError.passert(True, "Pass")
    try:
        ProgrammingError.passert(False, "")
    except ProgrammingError:
        pass
    try:
        ProgrammingError.passert(False, "Fail")
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:31:42.422464
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests if the constructor of :py:class:`ProgrammingError` can be invoked and raises an exception with a given message.
    """
    try:
        raise ProgrammingError("Just a dummy error message.")
    except ProgrammingError as e:
        pass



# Generated at 2022-06-14 04:31:46.167427
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("An error occurred")
    except ProgrammingError as err:
        assert err.args == ("An error occurred", )


# Generated at 2022-06-14 04:31:53.547486
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    class TestClass:
        pass
    assert issubclass(ProgrammingError, RuntimeError)
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    assert not issubclass(ProgrammingError, TestClass)
    try:
        raise ProgrammingError
    except ProgrammingError:
        pass
    exception = ProgrammingError()
    assert issubclass(type(exception), RuntimeError)
    assert str(exception) == ''



# Generated at 2022-06-14 04:31:55.610950
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("Test exception"):
        raise ProgrammingError("Test exception")

# Generated at 2022-06-14 04:31:57.308752
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except Exception as e:
        assert(str(e) == "test")

# Generated at 2022-06-14 04:33:03.566012
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError(message="Some message"):
        pass

# Generated at 2022-06-14 04:33:08.547002
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    exception = ProgrammingError
    exception.passert(True, None)
    try:
        exception.passert(False, None)
    except exception as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
        return
    assert False

# Generated at 2022-06-14 04:33:10.781812
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises

    with raises(ProgrammingError):
        raise ProgrammingError("Programming error")

# Generated at 2022-06-14 04:33:11.590473
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(True, "some message")

# Generated at 2022-06-14 04:33:14.104940
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Foo")
    except ProgrammingError as e:
        assert str(e) == "Foo"


# Generated at 2022-06-14 04:33:17.659160
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    e = ProgrammingError()
    assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)
    e = ProgrammingError("Test logical error message")
    assert e.args == ("Test logical error message",)
    try:
        raise e
    except ProgrammingError as caught:
        assert e is caught
        assert e.args == caught.args


# Generated at 2022-06-14 04:33:19.464445
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Coherence has been broken")
    except ProgrammingError as e:
        assert str(e) == "Coherence has been broken"

# Generated at 2022-06-14 04:33:28.124114
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "I do not like red apples")
        assert False, "Exception has not been thrown"
    except ProgrammingError as exc:
        assert isinstance(exc, ProgrammingError)
        assert "I do not like red apples" == str(exc)
    try:
        ProgrammingError.passert(False, None)
        assert False, "Exception has not been thrown"
    except ProgrammingError as exc:
        assert isinstance(exc, ProgrammingError)

# Generated at 2022-06-14 04:33:34.214935
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        assert True
        ProgrammingError.passert(True, "message")
    except ProgrammingError:
        assert False  # The test should not raise exceptions if condition and message are provided.

    try:
        ProgrammingError.passert(False, "message")
        assert False  # The test should raise exceptions if condition is not met.
    except ProgrammingError:
        assert True
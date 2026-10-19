

# Generated at 2022-06-14 04:23:31.972775
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Fake error")
    except Exception as err:
        assert isinstance(err, ProgrammingError)
        assert str(err) == "Fake error"


# Generated at 2022-06-14 04:23:36.302328
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "test message")
    except ProgrammingError as e:
        assert str(e) == "test message"


# Generated at 2022-06-14 04:23:38.843030
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests that the constructor defaults to an empty string when no message is provided.
    """
    assert ProgrammingError().args == ("",)



# Generated at 2022-06-14 04:23:41.808685
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, 'Must error')
    except ProgrammingError as e:
        assert str(e) == 'Must error'


# Generated at 2022-06-14 04:23:45.293320
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    try:
        ProgrammingError.passert(False, "This is a test")
    except ProgrammingError as e:
        assert str(e) == "This is a test"
    else:
        assert False

# Generated at 2022-06-14 04:23:46.815327
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception)


# Generated at 2022-06-14 04:23:50.507174
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        raise Exception(
            "ProgrammingError constructor should have thrown an exception."
        )


# Generated at 2022-06-14 04:24:00.676700
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # pylint: disable=unused-variable
    with ProgrammingError.passert(condition=True,   message="positive assertion"):
        pass
    with ProgrammingError.passert(condition=False,  message="negative assertion"):
        pass
    with ProgrammingError.passert(condition=True,   message=None):
        pass
    with ProgrammingError.passert(condition=False,  message=None):
        pass
    # pylint: enable=unused-variable
    try:
        ProgrammingError.passert(condition=True, message="positive assertion")
    except ProgrammingError:
        raise AssertionError("Expected no exception")
    with ProgrammingError.passert(condition=False,  message="negative assertion"):
        raise AssertionError("Expected no exception")

# Generated at 2022-06-14 04:24:05.036254
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert len(e.args) == 1
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:24:07.516590
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("error message")
    assert repr(error) == "error message"
    assert str(error) == "error message"

# Generated at 2022-06-14 04:24:13.874064
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit testing for constructor.
    """
    assertion_error = ProgrammingError("AssertionError")
    assert assertion_error.args == ("AssertionError",)

# Generated at 2022-06-14 04:24:16.702726
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError(message="foo")
    except ProgrammingError as e:
        assert str(e) == "foo"

# Generated at 2022-06-14 04:24:24.258821
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError as e:
        assert False, "passert must not raise any exception if condition is True"

    try:
        ProgrammingError.passert(False, "Test message")
        assert False, "passert must raise an exception if condition is False"
    except ProgrammingError as e:
        assert str(e) == "Test message"

    try:
        ProgrammingError.passert(False, None)
        assert False, "passert must raise an exception if condition is False"
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:24:25.559206
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("Test")



# Generated at 2022-06-14 04:24:27.399065
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("Oops!")
    assert str(error) == "Oops!"

# Generated at 2022-06-14 04:24:32.174112
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of class ProgrammingError.
    """
    case_1 = lambda: ProgrammingError.passert(True, None)
    assert case_1() is None

    case_2 = lambda: ProgrammingError.passert(False, None)
    assert case_2() is None

# Generated at 2022-06-14 04:24:35.882684
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test constructor of class ProgrammingError
    """
    e = ProgrammingError("Test")
    assert isinstance(e, Exception)
    assert str(e) == "Test"
    assert e.args[0] == "Test"


# Generated at 2022-06-14 04:24:37.040667
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    pass


# Generated at 2022-06-14 04:24:42.001082
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as e:
        raise ProgrammingError("This is a test of ProgrammingError")

    assert e.type is ProgrammingError
    assert "This is a test of ProgrammingError" == str(e.value)



# Generated at 2022-06-14 04:24:50.226301
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    This unit test case ensures that the constructor of the class :py:class:`ProgrammingError` raises an exception
    properly, but if the condition is met, then the error is not instantiated at all.
    """
    ProgrammingError.passert(True, "A message")
    raises_error = False
    try:
        ProgrammingError.passert(False, "Another message")
    except ProgrammingError:
        raises_error = True
    assert raises_error, "ProgrammingError should be raised"

# Generated at 2022-06-14 04:24:55.342112
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception)
    assert ProgrammingError.__doc__
    assert isinstance(ProgrammingError("message"), ProgrammingError)


# Generated at 2022-06-14 04:25:02.700274
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Tests that the generic constructor is working
    try:
        raise ProgrammingError("This is a test exception.")
    except ProgrammingError as e:
        print(e)

    # Tests that the passert function works as expected
    ProgrammingError.passert(False, "This is a test exception.")

if __name__ == "__main__":
    test_ProgrammingError()

# Generated at 2022-06-14 04:25:08.199927
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    
    # The constructor must raise an error
    try:
        raise ProgrammingError
        assert False
    except ProgrammingError:
        pass
    
    # The constructor must raise an error with the specified message
    try:
        raise ProgrammingError("Error message")
        assert False
    except ProgrammingError as e:
        assert e.args[0] == "Error message"



# Generated at 2022-06-14 04:25:11.786918
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("case 1")
    except ProgrammingError as e:
        assert str(e) == "case 1"


# Generated at 2022-06-14 04:25:15.478785
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "CAUTION: Code violates domain logic")
    except Exception as e:
        assert str(e) == "CAUTION: Code violates domain logic"

# Generated at 2022-06-14 04:25:19.005478
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test message")
    except ProgrammingError as e:
        assert issubclass(e.__class__, Exception)
        assert str(e) == "Test message"


# Generated at 2022-06-14 04:25:23.714386
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "A simple programming error test")
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert str(e) == "A simple programming error test"



# Generated at 2022-06-14 04:25:26.927336
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as cm:
        ProgrammingError.passert(False, "msg")
    assert "msg" == cm.value.args[0]



# Generated at 2022-06-14 04:25:29.860503
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit tests for constructor of class ProgrammingError."""
    msg = "Test error message."
    try:
        raise ProgrammingError(msg)
    except ProgrammingError as e:
        assert str(e) == msg


# Generated at 2022-06-14 04:25:36.457189
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.
    """
    assert ProgrammingError("Pypara programming error.")
    assert ProgrammingError("Pypara programming error.",
                            {"key": "value"})
    assert ProgrammingError()
    assert ProgrammingError("Pypara programming error.",
                            {"key": "value"},
                            ["a", "b", "c"])


# Generated at 2022-06-14 04:25:44.955813
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class ProgrammingError.
    """

    # We don't expect any exception
    ProgrammingError("test")

    # We don't expect any exception
    ProgrammingError()

# Generated at 2022-06-14 04:25:48.263533
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Arrange
    # Act
    # Assert
    assert issubclass(ProgrammingError, Exception)


# Generated at 2022-06-14 04:25:50.570884
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError(message="Test")
    except Exception:
        assert False
    else:
        assert True

# Generated at 2022-06-14 04:25:53.840618
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test message")
    except ProgrammingError as e:
        assert e.__str__() == "test message"


# Generated at 2022-06-14 04:25:57.478580
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as error:
        ProgrammingError.passert(False, "Expected error")
    assert str(error) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:25:59.046916
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    e = ProgrammingError("test")
    assert e.args[0] == "test"

# Generated at 2022-06-14 04:26:04.002401
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # noinspection PyStatementEffect
    ProgrammingError(message="Testing programming error.")
    try:
        # noinspection PyStatementEffect
        ProgrammingError()
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:26:08.192687
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError(message="Test error")
    except ProgrammingError as e:
        assert e.args[0] == "Test error"
    else:
        assert False


# Generated at 2022-06-14 04:26:12.539193
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Here is an error!")
        assert False, "This should not be reached!"
    except ProgrammingError as e:
        assert e.args[0] == "Here is an error!"

# Generated at 2022-06-14 04:26:22.651476
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the coherence of the constructor for :py:class:`ProgrammingError`.
    """

    # When no arguments are provided it works
    try:
        raise ProgrammingError()
    # Then the exception is raised
    except Exception as e:
        # And the exception is ProgrammingError
        assert type(e) is ProgrammingError

    # When the message argument is provided it works
    try:
        raise ProgrammingError(message="Test message.")
    # Then the exception is raised
    except Exception as e:
        # And the exception is ProgrammingError
        assert type(e) is ProgrammingError
        # And the message is proper
        assert e.args[0] == "Test message."

    # When the message argument is empty it works

# Generated at 2022-06-14 04:26:38.178424
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Check your code")
        assert False, "This code should not be reached."
    except ProgrammingError as ex:
        assert isinstance(ex, ProgrammingError)
        assert ex.args == ("Check your code",)

# Generated at 2022-06-14 04:26:40.400475
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("TEST")
    assert str(error) == "TEST"



# Generated at 2022-06-14 04:26:42.593597
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(False, "Something went wrong")
    ProgrammingError.passert(True, "Programming error")

# Generated at 2022-06-14 04:26:46.257016
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError):
        ProgrammingError.passert(False, "message")


# Generated at 2022-06-14 04:26:48.779400
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test message.")
    except ProgrammingError as e:
        assert e.__str__() == "Test message."


# Generated at 2022-06-14 04:26:50.518686
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError):
        ProgrammingError()


# Generated at 2022-06-14 04:26:57.192727
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        # Test if ProgrammingError passes
        ProgrammingError.passert(True, "blah")

        # Test if ProgrammingError fails
        ProgrammingError.passert(False, "blah")
        assert False, "condition must be false for this test to succeed"

    except ProgrammingError:
        # Success
        pass

    except Exception:
        assert False, "ProgrammingError is not related to unexpected exception"

# Generated at 2022-06-14 04:27:00.214623
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Some message.")
    except ProgrammingError:
        pass
    else:
        raise AssertionErr

# Generated at 2022-06-14 04:27:03.871531
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of the :py:class:`ProgrammingError` class.
    """
    assert issubclass(ProgrammingError, Exception)

# A unit test for testing the assert method of class ProgrammingError

# Generated at 2022-06-14 04:27:06.989610
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    succeeded = False
    try:
        raise ProgrammingError
    except ProgrammingError:
        succeeded = True
    assert succeeded
    
    succeeded = False
    try:
        raise ProgrammingError
    except Exception:
        succeeded = True
    assert succeeded


# Generated at 2022-06-14 04:27:29.241117
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def _test():
        raise ProgrammingError("Something is wrong here.")

    return _test



# Generated at 2022-06-14 04:27:37.162742
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    # Test constructor with empty error message
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        raise Exception("Test failed.")

    # Test constructor with custom error message
    try:
        raise ProgrammingError("This is a custom message")
    except ProgrammingError as e:
        assert str(e) == "This is a custom message"
    else:
        raise Exception("Test failed.")



# Generated at 2022-06-14 04:27:43.276749
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("Unit tests are mandatory"):
        pass

    try:
        with ProgrammingError("Unit tests are mandatory"):
            raise Exception("I am not a unit test!")
    except Exception as ex:
        assert str(ex) == "Unit tests are mandatory"


# Generated at 2022-06-14 04:27:46.727948
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Something is wrong.")
        assert False
    except ProgrammingError as e:
        assert str(e) == "Something is wrong."

# Generated at 2022-06-14 04:27:50.205356
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        assert True
    try:
        raise ProgrammingError("Chocolate!")
    except ProgrammingError as e:
        assert str(e) == "Chocolate!"

# Generated at 2022-06-14 04:27:55.283427
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Custom message")
        assert False, "It should have thrown an exception before"
    except ProgrammingError as ex:
        assert ex.args[0] == "Custom message"
    except Exception as ex:
        assert False, f"Unexpected exception: {ex}"

# Generated at 2022-06-14 04:27:58.842409
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:28:03.160677
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Not expected message")
    except Exception as e:
        assert str(e) == "Not expected message"
    try:
        ProgrammingError()
    except Exception as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:28:05.762823
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
        assert False, "An exception should have been thrown"
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:28:10.234488
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Foo bar baz")
        assert False, "Should not happen"
    except ProgrammingError as e:
        assert e.args == ('Foo bar baz',)

# Generated at 2022-06-14 04:28:58.810263
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests if the constructor of :py:class:`ProgrammingError` works as expected.
    """
    try:
        raise ProgrammingError("This is a test.")
    except ProgrammingError as err:
        assert str(err) == "This is a test."

# Generated at 2022-06-14 04:29:01.930596
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as e:
        ProgrammingError("Unexpected error")
    assert e.value.args == ("Unexpected error",)


# Generated at 2022-06-14 04:29:07.807597
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test")
    except ProgrammingError as e:
        assert e.args[0] == "This is a test"
        assert isinstance(e, ProgrammingError)
    else:
        assert False, "ProgrammingError constructor not working"


# Generated at 2022-06-14 04:29:10.448779
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)



# Generated at 2022-06-14 04:29:13.409276
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "a")
        assert False
    except ProgrammingError as other:
        assert str(other) == "a"


# Generated at 2022-06-14 04:29:16.344532
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "Broken coherence.")
    ProgrammingError.passert(True, "Broken coherence.")

# Generated at 2022-06-14 04:29:17.997422
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:29:21.541188
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:29:24.198653
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("This is an error message.")
    except Exception as e:
        assert isinstance(e, ProgrammingError)


# Generated at 2022-06-14 04:29:26.967034
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Oops!")
    except ProgrammingError as e:
        assert str(e) == "Oops!"

# Generated at 2022-06-14 04:31:11.971876
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    with ProgrammingError.passert(False, "Condition is not met"):
        pass

    with ProgrammingError.passert(True, "Condition is not met"):
        raise Exception("This code must not be reached")

# Generated at 2022-06-14 04:31:17.768450
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # If a message is passed to constructor, it should be stored as error message
    msg = "Test message"
    exception = ProgrammingError(msg)
    assert exception.message == msg
    # If no message is passed to constructor, it should store 'Broken coherence' as error message
    exception = ProgrammingError()
    assert exception.message == "Broken coherence"

# Generated at 2022-06-14 04:31:26.548239
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Set testing flag to True
    import pypara.utils
    pypara.utils.is_testing = True
    try:
        # Invoke constructor
        exc = ProgrammingError("message")
        # Check member variables
        assert exc.args[0] == "message"
        assert len(exc.args) == 1

        # Invoke constructor
        exc = ProgrammingError()
        # Check member variables
        assert exc.args[0] == "Broken coherence. Check your code against domain logic to fix it."
        assert len(exc.args) == 1
    finally:
        # Reset testing flag to False
        pypara.utils.is_testing = False


# Generated at 2022-06-14 04:31:29.560643
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Intentional raise")
    except ProgrammingError as e:
        assert e.args == ("Intentional raise", )


# Generated at 2022-06-14 04:31:40.564515
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # GIVEN: Condition is True and message is None
    condition, message = True, None

    # WHEN: Asserting the condition
    try:
        ProgrammingError.passert(condition, message)
    except ProgrammingError:
        # THEN: An error is raised
        assert False

    # WHEN: Asserting the condition
    try:
        # GIVEN: Condition is False and message is not None
        condition, message = False, "should-raise-error"

        ProgrammingError.passert(condition, message)
        # THEN: An error is raised
        assert False
    except ProgrammingError as e:
        # THEN: An error is raised
        assert e.args[0] == message

    # WHEN: Asserting the condition

# Generated at 2022-06-14 04:31:43.418167
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:31:47.041632
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Creates a new exception with a message using the constructor.
    """
    exception = ProgrammingError("Something bad happened here.")
    assert exception.args[0] == "Something bad happened here."


# Generated at 2022-06-14 04:31:50.514145
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Oh, shoot!")
    except ProgrammingError as e:
        assert e.args == ("Oh, shoot!",)

# Generated at 2022-06-14 04:31:55.654226
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises

    with raises(ProgrammingError):
        ProgrammingError("This is a programming error")

    # Unit test for method passert
    with raises(ProgrammingError):
        ProgrammingError.passert(False, "This is a programming error")
    # pylint: disable=unexpected-keyword-arg
    ProgrammingError.passert(True, message="Testing")

# Generated at 2022-06-14 04:31:58.407701
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test")
    except ProgrammingError as exc:
        assert str(exc) == "This is a test"

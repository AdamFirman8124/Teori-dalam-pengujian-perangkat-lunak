

# Generated at 2022-06-14 04:23:42.092839
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error_message = "No, it is not allowed to re-define the program's logic"
    # Use the constructor directly
    try:
        raise ProgrammingError(error_message)
    except ProgrammingError as exception:
        assert exception.args[0] is error_message
    # Instantiate it by the class method
    try:
        ProgrammingError.passert(False, error_message)
    except ProgrammingError as exception:
        assert exception.args[0] is error_message

# Generated at 2022-06-14 04:23:44.244782
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except NotImplementedError:
        pass


# Generated at 2022-06-14 04:23:46.815527
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "")
        assert False, "No exception raised"
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:23:49.001767
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A message.")
    except ProgrammingError as pe:
        pass


# Generated at 2022-06-14 04:23:52.475316
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Testing error.")
    except ProgrammingError as err:
        assert str(err) == "Testing error."
        assert err.args == ("Testing error.",)


# Generated at 2022-06-14 04:23:55.507240
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    output = None
    try:
        ProgrammingError.passert(False, 'test')
    except ProgrammingError as e:
        output = str(e)
    assert output == 'test'

# Generated at 2022-06-14 04:23:57.580801
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:24:02.823102
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # TODO: This test fails. It raises no exception when it should have.
    #       Check this at some moment.
    #
    # pylint: disable=protected-access
    # assert not ProgrammingError._condition, "Condition passed to error constructor 'ProgrammingError' is False."
    ProgrammingError.passert(False, "This is a test.")

test_ProgrammingError()

# Generated at 2022-06-14 04:24:05.025442
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    erro = ProgrammingError("Test")
    assert str(erro) == "Test"

# Generated at 2022-06-14 04:24:07.783211
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert str(e) == "test"



# Generated at 2022-06-14 04:24:11.910196
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test assertion")
        assert False
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:24:16.793016
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Test if the ProgrammingError is raised when it is expected to."""
    try:
        ProgrammingError.passert(False, "ABC")
    except ProgrammingError:
        return
    raise AssertionError("The exception is not raised.")


# Generated at 2022-06-14 04:24:20.170074
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the default constructor of :py:class:`ProgrammingError` and the exception is raised as expected.
    """
    error = ProgrammingError("test message")
    assert error.args[0] == "test message"


# Generated at 2022-06-14 04:24:23.999097
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Something went wrong!")
    except ProgrammingError as e:
        assert str(e) == "Something went wrong!"


# Generated at 2022-06-14 04:24:27.399122
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Error Message for Test")
    except ProgrammingError as e:
        assert e.args[0] == "Error Message for Test"


# Generated at 2022-06-14 04:24:32.171155
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "We should not reach here")
    except ProgrammingError as e:
        assert(e.args[0] == "We should not reach here")
    else:
        raise RuntimeError("test_ProgrammingError: failed")

# Generated at 2022-06-14 04:24:35.884418
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Cannot raise this exception.")
    except ProgrammingError as e:
        assert(str(e) == "Cannot raise this exception.")
    assert(ProgrammingError.passert(False, "Cannot raise") is None)

# Generated at 2022-06-14 04:24:43.083192
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "error")
    except ProgrammingError as e:
        assert "Broken coherence. Check your code against domain logic to fix it." in str(e)
    try:
        ProgrammingError.passert(True, "error")
    except ProgrammingError as e:
        assert False, "Not expected exception: {}".format(e)

# Generated at 2022-06-14 04:24:46.222300
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a programming error.")
    except ProgrammingError as e:
        assert str(e) == "This is a programming error."


# Generated at 2022-06-14 04:24:50.548151
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Given
    condition = True
    message = "A message"
    # When
    # Then
    try:
        ProgrammingError.passert(condition, "A message")
    except ProgrammingError as e:
        assert e.args[0] == message


# Generated at 2022-06-14 04:24:54.429922
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is the programming error.")
    except ProgrammingError as e:
        assert e.args[0] == "This is the programming error."


# Generated at 2022-06-14 04:24:59.204634
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Message")
        assert False, "The exception was not raised!"
    except ProgrammingError as e:
        assert str(e) == "Message", "The message was not properly formatted!"

# Generated at 2022-06-14 04:25:02.378639
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def test_ProgrammingError_constructor():
        ProgrammingError("This is a test message")
    test_ProgrammingError_constructor()


# Generated at 2022-06-14 04:25:04.589507
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    err = ProgrammingError("Just a test.")
    assert err.args == ('Just a test.',)


# Generated at 2022-06-14 04:25:10.084904
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test case for :py:class:`ProgrammingError`.
    """

    try:
        ProgrammingError()
    except ProgrammingError:
        pass
    else:
        assert False, "ProgrammingError() does not raise a ProgrammingError"

    try:
        ProgrammingError("boo")
    except ProgrammingError as e:
        assert str(e) == "boo", "ProgrammingError() does not provide the correct error message"
    else:
        assert False, "ProgrammingError() does not raise a ProgrammingError"


# Generated at 2022-06-14 04:25:11.395678
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("Hello World")


# Generated at 2022-06-14 04:25:14.567708
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except Exception as e:
        assert type(e) is ProgrammingError
        assert e.args == ()


# Generated at 2022-06-14 04:25:18.600895
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Programming error")
    except ProgrammingError as e:
        assert str(e) == "Programming error"
    else:
        assert False, "ProgrammingError not raised"


# Generated at 2022-06-14 04:25:21.585626
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("")
    ProgrammingError.passert(True, "")
    try:
        ProgrammingError.passert(False, "")
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:25:23.495584
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    o = ProgrammingError("this is an error")
    assert str(o) == "this is an error"

# Generated at 2022-06-14 04:25:29.451483
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except Exception as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:25:39.136917
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Testing with a negative condition.
    try:
        ProgrammingError.passert(False, "MESSAGE")
        assert False, "There should be an exception"  # pragma: no cover
    except ProgrammingError as e:
        assert str(e) == "MESSAGE", "The exception message should be the intended one"
    # Testing with a positive condition.
    try:
        ProgrammingError.passert(True, "MESSAGE")
    except:  # noqa
        assert False, "There should be no exception"  # pragma: no cover

# Generated at 2022-06-14 04:25:43.184335
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError):
        ProgrammingError()
    with raises(ProgrammingError) as exception_info:
        ProgrammingError("Broken coherence")
    assert exception_info.value.args == ("Broken coherence",)
    with raises(ProgrammingError) as exception_info:
        ProgrammingError(message="Broken coherence")
    assert exception_info.value.args == ("Broken coherence",)


# Generated at 2022-06-14 04:25:46.238364
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test message")
    except ProgrammingError as e:
        assert "Test message" in str(e)


# Generated at 2022-06-14 04:25:51.014962
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of the class :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("Testing...")
    except ProgrammingError as e:
        print(e)
        assert str(e) == "Testing..."

# Generated at 2022-06-14 04:25:58.352470
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "error message")
    except ProgrammingError as e:
        assert e.__str__() == "error message"

    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert e.__str__() == "Broken coherence. Check your code against domain logic to fix it."

    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError as e:
        assert False

# Generated at 2022-06-14 04:25:59.362192
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError()


# Generated at 2022-06-14 04:26:02.147925
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Broken coherence")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence"

# Generated at 2022-06-14 04:26:06.225166
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, None)
        ProgrammingError.passert(False, "")
        ProgrammingError.passert(False, "Oops! Broken coherence")

# Generated at 2022-06-14 04:26:11.013220
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("I have raised a programming error")
    except ProgrammingError as e:
        assert(str(e) == "I have raised a programming error")
        assert(type(e) == ProgrammingError)


# Generated at 2022-06-14 04:26:22.340291
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # 1. Test passing an error message
    try:
        raise ProgrammingError("This is a test")
    except ProgrammingError as e:
        assert str(e) == "This is a test"
    # 2. Test passing an invalid error message (None)
    try:
        raise ProgrammingError(None)
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    # 3. Test passing no error message (defaulting to the fixed message)
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:26:27.504287
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the default constructor of :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Programming error. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:26:30.837467
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        with ProgrammingError.passert(False, "some message"):
            pass
        assert False, "This code should not be reached"
    except ProgrammingError as e:
        assert str(e) == "some message"

    with ProgrammingError.passert(True, "some message"):
        pass

# Generated at 2022-06-14 04:26:35.306101
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ProgrammingError"""
    try:
        raise ProgrammingError("error message")
    except ProgrammingError as error:
        assert error.args == ("error message",)
        assert str(error) == "error message"


# Generated at 2022-06-14 04:26:41.391002
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("foo")
    except ProgrammingError as ex:
        assert str(ex) == "foo"
    try:
        raise ProgrammingError()
    except ProgrammingError as ex:
        assert str(ex) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:26:44.280781
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("MESSAGE")
    except ProgrammingError as err:
        assert err.args[0] == "MESSAGE"


# Generated at 2022-06-14 04:26:46.839963
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "Test")

# Generated at 2022-06-14 04:26:48.546968
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests :py:class:`ProgrammingError` constructor.
    """

    ProgrammingError("Hello world!")

# Generated at 2022-06-14 04:26:52.302851
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, "test"):
        pass  # test case
    with ProgrammingError.passert(False, "test"):
        pass  # shouldn't be executed



# Generated at 2022-06-14 04:26:55.578611
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A programming error has occurred")
    except ProgrammingError as error:
        assert error.args == ("A programming error has occurred",), "unexpected args"


# Generated at 2022-06-14 04:27:05.909581
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # All methods in class ProgrammingError should be tested
    ProgrammingError.passert(True, None)
    try:
        ProgrammingError.passert(False, "Error message")
    except ProgrammingError as err:
        assert err.__str__() == "Error message"
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as err:
        assert err.__str__() == "Broken coherence. Check your code against domain logic to fix it."

# Unit tests for module exceptions_test

# Generated at 2022-06-14 04:27:11.290762
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of class ProgrammingError.
    """
    try:
        raise ProgrammingError(None)
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."



# Generated at 2022-06-14 04:27:12.951345
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(1 == 2, "This is a wrong assumption")

# Generated at 2022-06-14 04:27:15.791174
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("No reason given.")
    except ProgrammingError as e:
        assert e.args == ("No reason given.",)


# Generated at 2022-06-14 04:27:18.067827
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Some message.")
    except ProgrammingError as e:
        assert str(e) == "Some message."


# Generated at 2022-06-14 04:27:22.483318
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    try:
        raise ProgrammingError("Testing")
    except ProgrammingError as e:
        assert str(e) == "Testing"


# Generated at 2022-06-14 04:27:24.503142
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(condition=True, message=None)
    ProgrammingError.passert(condition=True, message="")

# Generated at 2022-06-14 04:27:31.498116
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # An empty error message
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)

    # With some message
    try:
        raise ProgrammingError("This is not possible")
    except ProgrammingError as e:
        assert e.args == ("This is not possible",)



# Generated at 2022-06-14 04:27:37.005083
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Arrange
    message = "Expectation not met."

    # Act
    def exec_test():
        raise ProgrammingError(message)

    # Assert
    try:
        exec_test()
        assert False, "error was not raised"
    except ProgrammingError as e:
        assert message == str(e)



# Generated at 2022-06-14 04:27:39.663448
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Foo")

# Generated at 2022-06-14 04:27:50.859168
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # This statement is intended to raise an ProgrammingError exception
    try:
        ProgrammingError.passert(condition=False, message="Test exception")
    except ProgrammingError as e:
        # Make sure that the message is as expected
        assert str(e) == "Test exception"
        # Make sure that the exception was raised
        pass
    else:
        raise Exception("Expected ProgrammingError to be raised")

# Generated at 2022-06-14 04:27:52.397976
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(1 == 2, "This will be raised!")
    except ProgrammingError as err:
        assert str(err) == "This will be raised!"

# Generated at 2022-06-14 04:27:56.408073
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except Exception as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Unit tests for method passert of class ProgrammingError

# Generated at 2022-06-14 04:28:01.703452
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests basic initializations of class ProgrammingError.
    """
    err = ProgrammingError()
    assert str(err) == "Broken coherence. Check your code against domain logic to fix it."
    err = ProgrammingError("This is my error message!")
    assert str(err) == "This is my error message!"

# Generated at 2022-06-14 04:28:02.795929
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert isinstance(ProgrammingError(), ProgrammingError)

# Generated at 2022-06-14 04:28:06.492233
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("My error message."):
        pass
    try:
        with ProgrammingError("My error message."):
            pass
    except ProgrammingError as e:
        assert str(e) == "My error message."


# Generated at 2022-06-14 04:28:09.837940
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        raise Exception("test failed")


# Generated at 2022-06-14 04:28:14.326995
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unique test for constructor of class ProgrammingError."""
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass

    try:
        raise ProgrammingError(message="Hello")
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:28:18.269044
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Check your code against domain logic to fix it.")
    except ProgrammingError as e:
        assert str(e) == "Check your code against domain logic to fix it."



# Generated at 2022-06-14 04:28:20.481550
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception)


# Generated at 2022-06-14 04:28:37.993119
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    class Dummy:
        pass

    # Ensure that no error is raised if condition is met
    ProgrammingError.passert(1 == 1, "Error message")

    # Check that the message is set
    try:
        ProgrammingError.passert(1 == 2, "Error message")
        assert False
    except ProgrammingError as e:
        assert e.args[0] == "Error message"

    # Check that the exception has no parameters in case no message is given
    try:
        ProgrammingError.passert(1 == 2, None)
        assert False
    except ProgrammingError as e:
        assert len(e.args) == 0

    # Check that the exception has no parameters in case no message is given
    try:
        ProgrammingError.passert(1 == 2, "")
        assert False
    except ProgrammingError as e:
        assert len

# Generated at 2022-06-14 04:28:42.010042
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # given
    message = "Failure"

    # when
    error = ProgrammingError(message)

    # then
    assert error.args == (message,)



# Generated at 2022-06-14 04:28:43.926010
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as e:
        assert "Test" == str(e)


# Generated at 2022-06-14 04:28:48.536975
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of class ProgrammingError.

    :return: None.
    """
    try:
        raise ProgrammingError("any message")
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)


# Generated at 2022-06-14 04:28:50.322016
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError):
        ProgrammingError()


# Generated at 2022-06-14 04:28:52.054401
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert isinstance(ProgrammingError(), ProgrammingError)


# Generated at 2022-06-14 04:28:54.336986
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except NotImplementedError:
        pass



# Generated at 2022-06-14 04:28:58.481484
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert "test" == str(e)

# Unit tests for ProgrammingError.passert

# Generated at 2022-06-14 04:29:01.530145
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """ Unit test for constructor of class ProgrammingError """
    try:
        ProgrammingError()
        assert False
    except ProgrammingError:
        assert True


# Generated at 2022-06-14 04:29:04.541235
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
# Unit testing for classmethod passert of class ProgrammingError

# Generated at 2022-06-14 04:29:26.823356
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Some message")
    except ProgrammingError as ex:
        assert ex.args[0] == "Some message"


# Generated at 2022-06-14 04:29:28.520225
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, "Test message"):
        pass

# Generated at 2022-06-14 04:29:32.658851
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.
    """
    try:
        ProgrammingError("ABC")
    except ProgrammingError as error:
        assert error.args[0] == "ABC"
    else:
        assert False


# Generated at 2022-06-14 04:29:43.083215
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of the :py:class:`ProgrammingError` class.
    """
    try:
        # Try to raise the programming error with an empty message
        raise ProgrammingError()
    except ProgrammingError as e:
        # The error is expected to be raised
        assert True
        # The default message is expected to be raised
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    except:
        # Not expected to raise another kind of exception
        assert False
    try:
        # Try to raise the programming error with a custom message
        raise ProgrammingError("My custom message.")
    except ProgrammingError as e:
        # The error is expected to be raised
        assert True
        # The custom message is expected to be raised
        assert str(e) == "My custom message."

# Generated at 2022-06-14 04:29:46.994018
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class ProgrammingError.

    :return: ``None``
    """
    # Check constructor
    exception = ProgrammingError()
    assert exception.args == ("Broken coherence. Check your code against domain logic to fix it.",)

    # Check constructor with message
    message = "Test exception"
    exception = ProgrammingError(message)
    assert exception.args == (message,)

# Generated at 2022-06-14 04:29:49.937794
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is an error.")
    except ProgrammingError as error:
        assert error.args[0] == "This is an error."

# Generated at 2022-06-14 04:29:51.880731
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        pass



# Generated at 2022-06-14 04:29:56.712636
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for class ProgrammingError"""
    try:
        raise ProgrammingError("This is a new programming error")
    except ProgrammingError as p:
        print(p)
        assert p.args == ("This is a new programming error", )


# Generated at 2022-06-14 04:30:01.343217
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Error message")
    except ProgrammingError as e:
        assert e.args[0] == "Error message"
    else:
        assert False, "Expected an exception"


# Generated at 2022-06-14 04:30:05.748275
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    condition = True
    message = "This is a test message."

    ProgrammingError.passert(condition=True, message=message)
    ProgrammingError.passert(condition=condition, message=message)
    ProgrammingError.passert(condition=condition, message=message)
    ProgrammingError.passert(condition=condition, message=message)

    try:
        ProgrammingError.passert(condition=False, message=message)
        assert False, "ProgrammingError not raised."
    except ProgrammingError as e:
        assert e.args[0] == message, "Wrong error message."

# Generated at 2022-06-14 04:31:02.058716
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        raise AssertionError("ProgrammingError not raised")


# Generated at 2022-06-14 04:31:06.770791
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception)
    ProgrammingError()
    ProgrammingError.passert(True, "")
    try:
        ProgrammingError.passert(False, "")
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:31:19.915910
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class ProgrammingError.
    """

    # Asserts that an error is raised if the condition is False
    try:
        ProgrammingError.passert(False, "Test message")
        assert False, "Must raise an exception"
    except ProgrammingError as error:
        assert isinstance(error, ProgrammingError)
        assert "Test message" in str(error)
    try:
        ProgrammingError.passert(False, None)
        assert False, "Must raise an exception"
    except ProgrammingError as error:
        assert isinstance(error, ProgrammingError)
        assert "Broken coherence. Check your code against domain logic to fix it." in str(error)

    # Asserts that no error is raised if the condition is True
    ProgrammingError.passert(True, "Test message")

# Generated at 2022-06-14 04:31:22.887891
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Broken coherence. Check your code against domain logic to fix it.")
    except ProgrammingError as pe:
        assert str(pe) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:31:30.199615
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Check constructor
    try:
        ProgrammingError()
    except Exception as error:
        assert isinstance(error, ProgrammingError)
        assert len(error.args) == 1
        assert error.args[0] == "Broken coherence. Check your code against domain logic to fix it."
    else:
        raise AssertionError("Assertion error: Expected exception.")


# Generated at 2022-06-14 04:31:34.678256
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    class Test(ProgrammingError):
        pass
    try:
        Test.passert(False, "")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:31:37.029143
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("This is a message")
    except ProgrammingError as exc:
        assert str(exc) == "This is a message"


# Generated at 2022-06-14 04:31:39.673537
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test")
    except ProgrammingError as e:
        assert e.args[0] == "This is a test"

# Generated at 2022-06-14 04:31:49.516194
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a programming error!")
    except ProgrammingError as e:
        assert e.args[0] == "This is a programming error!"
    try:
        ProgrammingError.passert(False, "This condition is not met!")
    except ProgrammingError as e:
        assert e.args[0] == "This condition is not met!"
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:31:57.342049
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Test function for the :py:class:`ProgrammingError` class."""

    try:
        ProgrammingError.passert(False, None)
    except Exception as ex:
        assert ex.__class__ is ProgrammingError
        assert str(ex) == "Broken coherence. Check your code against domain logic to fix it."

    try:
        ProgrammingError.passert(False, "Message")
    except Exception as ex:
        assert ex.__class__ is ProgrammingError
        assert str(ex) == "Message"

    ProgrammingError.passert(True, "Message")
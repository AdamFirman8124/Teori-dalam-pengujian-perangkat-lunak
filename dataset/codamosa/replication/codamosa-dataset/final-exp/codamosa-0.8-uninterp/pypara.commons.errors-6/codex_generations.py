

# Generated at 2022-06-14 04:23:29.481231
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, "Test error"):
        pass

test_ProgrammingError()

# Generated at 2022-06-14 04:23:31.224339
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test message")
    except ProgrammingError as e:
        assert str(e) == "Test message"


# Generated at 2022-06-14 04:23:40.360415
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Verifies the class :py:class:`ProgrammingError` and its constructor.
    """
    try:
        ProgrammingError.passert(False, "this is a message")
        assert False
    except ProgrammingError as error:
        assert error.args[0] == "this is a message"

    try:
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError as error:
        assert error.args[0] == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:23:44.140890
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("expected")
    except ProgrammingError as e:
        assert e.__class__.__name__ == "ProgrammingError"
        assert str(e) == "expected"

# Generated at 2022-06-14 04:23:47.508303
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError as pe:
        assert pe.args[0] == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:23:51.582845
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError:
        ProgrammingError.passert(True, "")
        ProgrammingError.passert(False, "")
    with ProgrammingError:
        ProgrammingError.passert(False, None)
    with ProgrammingError:
        ProgrammingError.passert(False, "msg")

# Generated at 2022-06-14 04:23:59.855687
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for :py:class:`ProgrammingError` class.
    """
    try:
        # The following statements should raise an instance of ProgrammingError.
        ProgrammingError.passert(True, "message 1")
        ProgrammingError.passert(False, "message 2")

        # The following statement should not be executed, but we raise this assertion in case that it is true.
        assert False, "No ProgrammingError raised."

    # The following statement should catch an instance of ProgrammingError.
    except ProgrammingError:
        assert True

# Generated at 2022-06-14 04:24:03.670263
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # noinspection PyTypeChecker
    with ProgrammingError("The error message.") as err:
        assert "The error message." == err.args[0]

# Generated at 2022-06-14 04:24:18.388702
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    passert = ProgrammingError.passert

    # Clearly False condition without any additional message
    try:
        passert(False, None)
    except ProgrammingError:
        pass
    except Exception:
        assert False, "The exception raised should be a ProgrammingError"

    # Clearly False condition with an additional message
    try:
        passert(False, "Custom message")
    except ProgrammingError as error:
        assert str(error) == "Custom message", "The message has not be passed by the exception"
    except Exception:
        assert False, "The exception raised should be a ProgrammingError"

    # Clearly True condition without any additional message
    try:
        passert(True, None)
    except ProgrammingError:
        assert False, "The condition is True so the exception should have not been raised"

    # Clearly True condition with an additional message

# Generated at 2022-06-14 04:24:20.317424
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
        assert False
    except ProgrammingError:
        pass
    except Exception:
        assert False


# Generated at 2022-06-14 04:24:25.121329
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "A programming error")
    except ProgrammingError as e:
        assert e.args == ("A programming error",)

# Generated at 2022-06-14 04:24:28.486435
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError`.
    """
    err = ProgrammingError('Test error message')
    assert err is not None

# Generated at 2022-06-14 04:24:29.283054
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:24:29.741303
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError



# Generated at 2022-06-14 04:24:30.595828
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    class DummyProgrammingError(ProgrammingError):
        pass

    DummyProgrammingError(message="Message")


# Generated at 2022-06-14 04:24:33.901597
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError(message="A programming error has been raised")
    except ProgrammingError as e:
        assert e.message == "A programming error has been raised"


# Generated at 2022-06-14 04:24:36.370981
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Someting bad happened")
    except ProgrammingError as ex:
        assert ex.args[0] == "Someting bad happened"


# Generated at 2022-06-14 04:24:39.476635
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:24:41.512782
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError): ProgrammingError()


# Generated at 2022-06-14 04:24:49.316850
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test of method ProgrammingError.passert() passing a valid condition
    try:
        ProgrammingError.passert(True, "")
    except:
        assert False
    # Test of method ProgrammingError.passert() passing an invalid condition
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert e.__class__ is ProgrammingError
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:24:55.862287
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError()
    excinfo.match("Broken coherence. Check your code against domain logic to fix it.")
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError("Some message")
    excinfo.match("Some message")

# Generated at 2022-06-14 04:25:01.394200
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    with pytest.raises(ProgrammingError):
        # The condition is not fulfilled, so a ProgrammingError is raised.
        ProgrammingError.passert(False, "Broken coherence.")

    # In this case the condition is fulfilled, so no exception is raised.
    ProgrammingError.passert(True, "Broken coherence.")

# Generated at 2022-06-14 04:25:03.173153
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test error")
    except ProgrammingError as e:
        assert "Test error" == str(e)



# Generated at 2022-06-14 04:25:08.200627
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of class ProgrammingError.

    The test simply checks that an exception is raised if the condition is ``False``.
    """

    raised = False
    try:
        ProgrammingError.passert(False, "Test")
    except ProgrammingError:
        raised = True

    assert raised, "Constructor of class ProgrammingError did not raise an exception"

# Generated at 2022-06-14 04:25:12.326036
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Expectation not met")
    except ProgrammingError as error:
        assert error.args[0] == "Expectation not met"

# Generated at 2022-06-14 04:25:16.012519
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("an error")
    except ProgrammingError as e:
        assert str(e) == "an error", "unexpected message: " + str(e)

# Generated at 2022-06-14 04:25:19.528905
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:25:22.854148
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Error!!!")
    except ProgrammingError as e:
        assert str(e) == "Error!!!"
    ProgrammingError.passert(True, "Error!!!")

# Generated at 2022-06-14 04:25:25.760864
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Some message")
    except ProgrammingError as e:
        assert e.args == ("Some message",)


# Generated at 2022-06-14 04:25:28.569228
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Testing")
    except ProgrammingError as e:
        assert e.args[0] == "Testing"

# Generated at 2022-06-14 04:25:39.814605
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(True, "Dummy assertion")  # Should pass
    try:
        ProgrammingError.passert(False, "Dummy assertion")  # Should raise an exception
        assert False
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert str(e) == "Dummy assertion"

# Generated at 2022-06-14 04:25:42.077768
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A message")
    except ProgrammingError as e:
        assert str(e) == "A message"


# Generated at 2022-06-14 04:25:48.264548
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as e:
        assert str(e) == "Test"


# Generated at 2022-06-14 04:25:49.579634
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except NotImplementedError:
        pass


# Generated at 2022-06-14 04:25:51.832383
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "Error")


# Generated at 2022-06-14 04:25:54.694432
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Exception message")
    except ProgrammingError as e:
        assert str(e) == "Exception message"


# Generated at 2022-06-14 04:25:56.835570
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    with raises(ProgrammingError):
        ProgrammingError(message="My message")


# Generated at 2022-06-14 04:26:02.194372
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("An error message")
    except ProgrammingError as e:
        assert str(e) == "An error message"
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:26:04.124825
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert e.args == ("test",)

# Generated at 2022-06-14 04:26:08.894594
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is a dummy test")
        raise Exception("An exception was expected but not raised")
    except ProgrammingError as e:
        assert "This is a dummy test" == e.args[0]

# Generated at 2022-06-14 04:26:20.641273
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("foo")
    assert error.args == ("foo",)

# Generated at 2022-06-14 04:26:25.577651
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    expected_message = 'Expected message'
    try:
        raise ProgrammingError(expected_message)
    except ProgrammingError as e:
        assert str(e) == expected_message
    else:
        raise Exception('should have raised an exception')


# Generated at 2022-06-14 04:26:28.338615
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, "This is a test"):
        pass



# Generated at 2022-06-14 04:26:30.938750
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Run
    try:
        ProgrammingError.passert(False, "Test.")
    except ProgrammingError as e:
        assert str(e) == "Test."
    else:
        assert False, "ProgrammingError should have been raised"


# Generated at 2022-06-14 04:26:35.022404
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    a = ProgrammingError("Test message")

    try:
        ProgrammingError.passert(False, "Test error")
        assert False
    except ProgrammingError as e:
        assert str(e) == "Test error"

# Generated at 2022-06-14 04:26:38.058974
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        return
    assert False


# Generated at 2022-06-14 04:26:40.859561
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, 'ok'):
        pass
    with ProgrammingError.passert(False, 'ko'):
        pass

# Generated at 2022-06-14 04:26:42.090336
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test error")
    except ProgrammingError as e:
        assert (str(e) == "Test error")

# Generated at 2022-06-14 04:26:43.882106
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Isn't it a cool new exception?")
    except ProgrammingError as e:
        assert str(e) == "Isn't it a cool new exception?"


# Generated at 2022-06-14 04:26:47.035401
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Some message")
    except ProgrammingError:
        pass
    else:
        raise Exception()

# Generated at 2022-06-14 04:27:13.100999
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pypara.testing.utils import assert_exception

    # Case of normal
    assert_exception(ProgrammingError, lambda: ProgrammingError())

    # Case of message
    assert_exception(ProgrammingError, lambda: ProgrammingError("message"))

    # Case of cause
    assert_exception(ProgrammingError, lambda: ProgrammingError(ProgrammingError()))

    # Case of cause and message
    assert_exception(ProgrammingError, lambda: ProgrammingError("message", ProgrammingError()))


# Generated at 2022-06-14 04:27:16.768054
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert(str(e) == "Broken coherence. Check your code against domain logic to fix it.")
    else:
        assert(False)


# Generated at 2022-06-14 04:27:19.270167
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError('This is a test.')
    except ProgrammingError as e:
        assert str(e) == 'This is a test.'


# Generated at 2022-06-14 04:27:21.073673
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    error = ProgrammingError("a message")
    assert error.args == ("a message",)

# Generated at 2022-06-14 04:27:23.985403
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Programming error.")
    except Exception:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:27:27.674188
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as e:
        assert "Test" == e.args[0]

# Generated at 2022-06-14 04:27:36.129592
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Testing message")
        raise AssertionError("This line should never be executed.")
    except ProgrammingError as e:
        assert e.args and e.args[0] == "Testing message"
    try:
        ProgrammingError.passert(False, None)
        raise AssertionError("This line should never be executed.")
    except ProgrammingError as e:
        assert e.args and e.args[0] == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:27:37.477484
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    raise ProgrammingError("This is a test")



# Generated at 2022-06-14 04:27:40.714256
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, "Nothing to do"):
        ProgrammingError()


# Generated at 2022-06-14 04:27:47.399543
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class :py:class:`ProgrammingError`."""
    try:
        raise ProgrammingError("A programming error has occurred")
    except ProgrammingError as error:
        assert str(error) == "A programming error has occurred"
        assert str(error) == error.__str__()
        assert str(error) == error.__repr__()


# Generated at 2022-06-14 04:28:32.117693
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError`.
    """

    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:28:38.294936
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for class :py:class:`ProgrammingError`.

    Test cases:

    * Tests that is raises a :py:class:`ProgrammingError` with a message.
    * Tests that is raises a :py:class:`ProgrammingError` with a default message.
    * Tests that does not raise a :py:class:`ProgrammingError` if the condition is ``True``.
    """
    try:
        ProgrammingError.passert(False, "This is a test message.")
        assert False, "This statement is expected to raise an exception."
    except ProgrammingError as exception:
        assert str(exception) == "This is a test message.", "The exception message is incorrect."

# Generated at 2022-06-14 04:28:40.196688
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Arrange, Act and Assert
    assert issubclass(ProgrammingError, Exception)

# Generated at 2022-06-14 04:28:44.413003
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message="test message")
    except ProgrammingError as e:
        assert e.args[0] == "test message"
    else:
        raise Exception("Constructor of ProgrammingError does not raise the expected exception")


# Generated at 2022-06-14 04:28:48.657794
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert(e.args == ('Broken coherence. Check your code against domain logic to fix it.',))


# Generated at 2022-06-14 04:28:57.678664
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(Exception):
        ProgrammingError()

    # Unit test for method passert of class ProgrammingError
    def test_ProgrammingError_passert():
        with pytest.raises(ProgrammingError):
            ProgrammingError.passert(False, "Whoops!")

        with pytest.raises(ProgrammingError):
            ProgrammingError.passert(False, None)

        # No exception expected for true conditions
        ProgrammingError.passert(True, "Whoops!")
        ProgrammingError.passert(True, None)
        assert True

# Generated at 2022-06-14 04:29:01.120400
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of class ProgrammingError.
    """
    try:
        ProgrammingError()
    except Exception as exception:
        assert isinstance(exception, ProgrammingError), "Should be equal"
    else:
        raise Exception("Should not be equal")


# Generated at 2022-06-14 04:29:01.819698
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError()

# Generated at 2022-06-14 04:29:05.772863
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Expected error, not a bug.")
    except ProgrammingError as e:
        assert e.args[0] == "Expected error, not a bug."

# Generated at 2022-06-14 04:29:07.927821
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(condition=False, message="Nonexisting name"):
        pass

# Generated at 2022-06-14 04:30:45.951752
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ex = ProgrammingError("Expected message")
    assert isinstance(ex, Exception)
    assert ex.args == ("Expected message",)

# Generated at 2022-06-14 04:30:49.546025
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert e.args
        assert "".join(e.args)

# Generated at 2022-06-14 04:30:53.317464
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("Broken coherence. Check your code against domain logic to fix it.")
    assert error.message == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:30:57.466914
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for the constructor of class :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("Testing")
    except ProgrammingError as err:
        assert err.args[0] == "Testing"

# Generated at 2022-06-14 04:31:04.022293
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "A test message")
        assert False, "ProgrammingError must be raised"
    except ProgrammingError as e:
        assert "A test message" == e.args[0]
    else:
        assert False, "ProgrammingError must be raised"


if __name__ == "__main__":
    import pytest
    import sys
    pytest.main([sys.argv[0]])

# Generated at 2022-06-14 04:31:11.282844
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Use of :py:class:`ProgrammingError` constructor to create error objects."""

    # Tests passing a valid message
    test_error = ProgrammingError("This is a valid message")
    assert test_error.args[0] == "This is a valid message"

    # Tests passing a null message
    test_error = ProgrammingError(None)
    assert test_error.args[0] == "Broken coherence. Check your code against domain logic to fix it."

    # Tests not passing a message at all
    test_error = ProgrammingError()
    assert test_error.args[0] == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:31:20.021754
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(condition=True, message="OK!"):
        print("OK!")
    try:
        with ProgrammingError.passert(condition=False, message="KO!"):
            print("KO!")
    except ProgrammingError as e:
        print(f"KO! {e}")
    try:
        with ProgrammingError.passert(condition=False, message=None):
            print("KO! (None)")
    except ProgrammingError as e:
        print(f"KO! (None) {e}")

# Generated at 2022-06-14 04:31:22.203629
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    pass
    # This method is not tested because it merely contains code to determine the name of the caller.
    # The test is in the function test_ProgrammingError_passert()


# Generated at 2022-06-14 04:31:24.984819
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test")
        assert False, "The passert() should raise an exception"
    except ProgrammingError as e:
        assert str(e) == "Test"


# Generated at 2022-06-14 04:31:26.919337
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        pass

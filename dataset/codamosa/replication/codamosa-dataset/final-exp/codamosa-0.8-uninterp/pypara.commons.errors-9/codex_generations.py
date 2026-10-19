

# Generated at 2022-06-14 04:23:32.699860
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    success = False
    try:
        raise ProgrammingError()
    except ProgrammingError:
        success = True

    assert success



# Generated at 2022-06-14 04:23:41.222829
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of the :py:class:`ProgrammingError`.
    """

    try:
        raise ProgrammingError
    except ProgrammingError:
        pass
    except Exception:
        raise AssertionError("Failed to raise a ProgrammingError.")

    try:
        raise ProgrammingError("A message")
    except ProgrammingError:
        pass
    except Exception:
        raise AssertionError("Failed to raise a ProgrammingError with a message.")


# Generated at 2022-06-14 04:23:43.514803
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except Exception as e:
        assert "Test" == str(e)

# Generated at 2022-06-14 04:23:46.069251
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)



# Generated at 2022-06-14 04:23:50.164457
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    ProgrammingError.passert(False, "Failing condition")
    try:
        ProgrammingError.passert(False, "Failing condition")
    except ProgrammingError as err:
        assert(str(err) == "Failing condition")

# Generated at 2022-06-14 04:23:53.015893
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # noinspection PyBroadException
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    except:
        assert False, "Unexpected exception raised"

# Generated at 2022-06-14 04:23:55.740746
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A programming error message")
    except ProgrammingError as e:
        assert e.args == ("A programming error message",)


# Generated at 2022-06-14 04:24:01.321286
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    m = "hello world!"
    try:
        ProgrammingError.passert(False, m)
    except ProgrammingError as e:
        assert m ==  str(e)
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert "Broken coherence. Check your code against domain logic to fix it." ==  str(e)

    try:
        ProgrammingError.passert(True, None)
        assert True
    except ProgrammingError as e:
        assert False

# Generated at 2022-06-14 04:24:05.323993
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assertTrue(str(e), "Broken coherence. Check your code against domain logic to fix it.")


# Generated at 2022-06-14 04:24:07.608383
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Tests the constructor of class ProgrammingError."""
    ProgrammingError(message="This is an error")


# Generated at 2022-06-14 04:24:15.274663
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit-tests the constructor of class `ProgrammingError`.
    """
    # noinspection PyUnusedLocal
    def dummy():
        ProgrammingError.passert(True, "Message")
        ProgrammingError.passert(False, "Message")

    import pytest

    pytest.raises(ProgrammingError, dummy)

# Generated at 2022-06-14 04:24:21.029790
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert not ProgrammingError.passert(True, None)
    try:
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    try:
        ProgrammingError.passert(False, "Not expected")
        assert False
    except ProgrammingError as e:
        assert str(e) == "Not expected"

# Generated at 2022-06-14 04:24:24.880444
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a programming error")
    except ProgrammingError as e:
        assert str(e) == "This is a programming error"


# Generated at 2022-06-14 04:24:26.805405
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is a test")
    except Exception as e:
        assert isinstance(e, ProgrammingError)
        assert e.__str__() == "This is a test"


# Generated at 2022-06-14 04:24:28.205064
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:24:30.898324
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert isinstance(e.args[0], str)


# Generated at 2022-06-14 04:24:34.640950
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError.passert(False, "Test")
    assert 'Test' in str(excinfo.value)



# Generated at 2022-06-14 04:24:37.880916
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class :py:class:`ProgrammingError`."""
    with ProgrammingError.passert(True, "message"):
        pass
    with ProgrammingError.passert(False, "message"):
        pass

# Generated at 2022-06-14 04:24:45.277672
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # pylint: disable=W0612
    try:
        ProgrammingError.passert(False, "Some message")
    except ProgrammingError as ex:
        assert ex.args[0] == "Some message"
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as ex:
        assert ex.args[0] == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:24:46.946707
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("test")

# Generated at 2022-06-14 04:24:54.516953
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with assert_raises(ProgrammingError,
                       msg="ProgrammingError does not raise expected exception.") as cm:
        raise ProgrammingError("SOME MESSAGE GOES HERE.")
    assert cm.exception is not None
    assert str(cm.exception) == "SOME MESSAGE GOES HERE."

# Generated at 2022-06-14 04:24:58.351565
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Testing ProgrammingError")
    except ProgrammingError as e:
        assert e.args[0] == "Testing ProgrammingError"


# Generated at 2022-06-14 04:25:01.990628
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("test")
    except ProgrammingError:
        pass
    else:
        assert False, "ProgrammingError should be raised"


# Generated at 2022-06-14 04:25:04.132109
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("1")
    assert error.args[0] == "1"


# Generated at 2022-06-14 04:25:07.684277
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("You have passed something which is not expected.")
    except ProgrammingError as e:
        assert str(e) == "You have passed something which is not expected."


# Generated at 2022-06-14 04:25:10.042242
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."



# Generated at 2022-06-14 04:25:14.743843
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "message")
    except ProgrammingError as e:
        assert isinstance(e, Exception)
        assert str(e) == "message"
    else:
        assert False


# Generated at 2022-06-14 04:25:18.315693
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as exc_info:
        ProgrammingError.passert(False, "You are doing it wrong!")
    assert exc_info.value.args == ("You are doing it wrong!", )

# Generated at 2022-06-14 04:25:20.860351
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest

    with pytest.raises(ProgrammingError):
        raise ProgrammingError("This should be raised.")


# Generated at 2022-06-14 04:25:24.026279
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Checks the constructor of the class :py:class:`ProgrammingError`.
    """
    error = ProgrammingError("Test error message.")
    assert str(error) == "Test error message."

# Generated at 2022-06-14 04:25:30.547501
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests for :py:class:`ProgrammingError`.
    """
    with ProgrammingError.passert:
        pass

    with ProgrammingError.passert(0 == 0):
        pass


# Generated at 2022-06-14 04:25:39.846217
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def test_passert_nothing():
        ProgrammingError.passert(True, None)

        # This must not fail
        ProgrammingError.passert(True, "")

    def test_passert_fail():
        def fail():
            ProgrammingError.passert(False, "Some error")

        ProgrammingError.passert(False, "")
        ProgrammingError.passert(False, None)
        ProgrammingError.passert(False, "Some error")
        ProgrammingError.passert(False, None)
        assert_raises(ProgrammingError, fail)

# Generated at 2022-06-14 04:25:42.079675
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        raise AssertionError()


# Generated at 2022-06-14 04:25:45.341450
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Hello World!")
    except ProgrammingError as e:
        assert str(e) == "Hello World!"


# Generated at 2022-06-14 04:25:49.093583
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message="...")
    except ProgrammingError as e:
        assert str(e) == "..."

# Generated at 2022-06-14 04:25:55.042808
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError):
        raise ProgrammingError()
    with raises(ProgrammingError):
        raise ProgrammingError("Some error message")
    with raises(ProgrammingError):
        ProgrammingError.passert(False, "Some error message")
    # Do not raise anything
    ProgrammingError.passert(True, None)


# Generated at 2022-06-14 04:25:57.944248
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():  # pragma: no cover
    try:
        raise ProgrammingError("Message")
    except ProgrammingError as e:
        assert e.args[0] == "Message"

# Generated at 2022-06-14 04:26:00.620081
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:26:03.887604
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError()
    with pytest.raises(ProgrammingError):
        ProgrammingError("test")


# Generated at 2022-06-14 04:26:13.685607
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test error reporting with simple message
    try:
        raise ProgrammingError("msg")
    except Exception as ex:
        assert str(ex) == "msg"
    # Test error reporting with no message
    try:
        raise ProgrammingError()
    except Exception as ex:
        assert str(ex) == "Broken coherence. Check your code against domain logic to fix it."
    # Test error reporting with custom message
    try:
        ProgrammingError.passert(False, "msg")
    except Exception as ex:
        assert str(ex) == "msg"


# Generated at 2022-06-14 04:26:20.695575
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)
    else:
        assert False


# Generated at 2022-06-14 04:26:23.080233
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This error is raising by design.")
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:26:26.931381
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message="Message")
        assert False
    except ProgrammingError as e:
        assert str(e) == "Message"
    else:
        assert False

# Generated at 2022-06-14 04:26:29.981346
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError(message="A simple message")
    assert error.args[0] == "A simple message"


# Generated at 2022-06-14 04:26:32.078686
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, "It must not be possible to construct this"):
        pass


# Generated at 2022-06-14 04:26:37.823410
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    message = "This is an error message"
    try:
        ProgrammingError.passert(condition=False, message=message)
    except ProgrammingError as pe:
        assert (str(pe) == message)
    except Exception:
        assert False



# Generated at 2022-06-14 04:26:43.800650
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test that the constructor is not doing anything else
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == ""
    # Test that the constructor is able to set a message
    try:
        raise ProgrammingError("A message")
    except ProgrammingError as e:
        assert str(e) == "A message"


# Generated at 2022-06-14 04:26:55.161575
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from linesman.misprediction import MisPredict
    from linesman.linesman import MisPredictError

    # Reset the MisPrediction error counter
    MisPredict.error_counter = 0

    try:
        # Check that we properly handle the error counter
        raise MisPredictError("Using just the default constructor")
        raise MisPredictError("Shouldn't reach this line of code")
    except MisPredictError as ex:
        if ex.error_info != "Error #1. Using just the default constructor":
            raise ProgrammingError.passert(False, "Check the error counter in the error message")
    else:
        raise ProgrammingError.passert(False, "Check that we raise the exception")


# Generated at 2022-06-14 04:26:59.344122
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class ProgrammingError.
    """
    try:
        raise ProgrammingError("ProgrammingError.")
    except ProgrammingError as e:
        assert(e.__str__() == "ProgrammingError.")

# Generated at 2022-06-14 04:27:02.377305
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test message")
    except ProgrammingError as e:
        assert str(e) == "Test message"


# Generated at 2022-06-14 04:27:16.306520
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit-test for the constructor of :py:class:`ProgrammingError`.
    """
    try:
        ProgrammingError.passert(False, "Broken coherence. Check your code against domain logic to fix it.")
    except ProgrammingError as error:
        assert error.args[0] == "Broken coherence. Check your code against domain logic to fix it."
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as error:
        assert error.args[0] == "Broken coherence. Check your code against domain logic to fix it."
    ProgrammingError.passert(True, "Broken coherence. Check your code against domain logic to fix it.")

# Generated at 2022-06-14 04:27:17.301227
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(True, "")

# Generated at 2022-06-14 04:27:22.174847
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as error:
        assert error.args == ("Broken coherence. Check your code against domain logic to fix it.",)
    try:
        raise ProgrammingError("Some error")
    except ProgrammingError as error:
        assert error.args == ("Some error",)


# Generated at 2022-06-14 04:27:27.008635
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    passed = False
    try:
        ProgrammingError("This is the error message")
        passed = True
    except Exception:
        pass
    assert passed, "The constructor of class ProgrammingError must allow passing an error message."


# Generated at 2022-06-14 04:27:30.151824
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:27:34.412481
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Exercise the unit test for having coverage
    try:
        raise ProgrammingError
    except ProgrammingError as ex:
        assert str(ex) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:27:37.966246
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        assert False, "Expected a ProgrammingError."

# Generated at 2022-06-14 04:27:43.664232
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as exception_info:
        ProgrammingError.passert(False, "Some error")
    assert isinstance(exception_info.value, ProgrammingError)
    assert "Some error" in str(exception_info.value)


# Generated at 2022-06-14 04:27:46.975560
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """ Unit test for class ProgrammingError. """
    try:
        raise ProgrammingError("some message").with_traceback(None)
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:27:49.113269
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    expected = "I am a message"
    exc = ProgrammingError(expected)
    assert exc.args[0] == expected

# Generated at 2022-06-14 04:27:56.110378
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except:
        pass



# Generated at 2022-06-14 04:27:59.315206
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class ProgrammingError.
    """
    assert str(ProgrammingError("test")) == "test"


# Generated at 2022-06-14 04:28:02.205840
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test message")
    except ProgrammingError as e:
        assert e.args[0] == "Test message"


# Generated at 2022-06-14 04:28:05.024385
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Hi")
    except ProgrammingError as e:
        assert e.args == ("Hi",), "Constructor of ProgrammingError is broken"


# Generated at 2022-06-14 04:28:10.085755
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for the constructor of :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("Mock message")
    except ProgrammingError as ex:
        assert str(ex) == "Mock message", "Message is not correct. Result: {0}".format(str(ex))

# Generated at 2022-06-14 04:28:13.265438
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    e = ProgrammingError()
    assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)

# Generated at 2022-06-14 04:28:17.658339
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def my_function():
        raise ProgrammingError("It is not working")
    try:
        my_function()
    except ProgrammingError as error:
        assert error.args[0] == "It is not working"


# Generated at 2022-06-14 04:28:22.340465
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Testing constructor for ProgrammingError."""
    try:
        raise ProgrammingError("Just a test of exception")
    except ProgrammingError as ce:
        assert str(ce).endswith("Just a test of exception")


# Generated at 2022-06-14 04:28:28.042432
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    This test exercises the constructor of the :py:class:`ProgrammingError` class.
    """
    try:
        raise ProgrammingError("test.test_test")
    except ProgrammingError as exception:
        assert isinstance(exception, ProgrammingError)
        assert exception.args == ("test.test_test",)
    else:
        raise Exception("ProgrammingError should have been raised")


# Generated at 2022-06-14 04:28:31.725084
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class ProgrammingError.
    """
    message = "A programming error"
    try:
        raise ProgrammingError(message)
    except ProgrammingError as error:
        assert error.args[0] == message

# Generated at 2022-06-14 04:28:46.949221
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests constructor.
    """
    try:
        raise ProgrammingError("Error message")
    except ProgrammingError as e:
        assert e.args[0] == "Error message"


# Generated at 2022-06-14 04:28:49.028360
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(False, "This error is expected.")

# Generated at 2022-06-14 04:28:52.806063
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        with ProgrammingError.passert(False, "Simulating a broken coherence."):
            pass
    except ProgrammingError:
        pass
    else:
        assert False, "It was expected to get a ProgrammingError"

# Generated at 2022-06-14 04:28:58.107156
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    This function unit tests the class :py:class:`ProgrammingError`.
    """
    with ProgrammingError.passert(True, "Expecting True"):
        pass

    try:
        with ProgrammingError.passert(False, "Expecting False"):
            pass
    except ProgrammingError as e:
        assert str(e) == "Expecting False"
    else:
        raise Exception("Unit test failed")

# Generated at 2022-06-14 04:28:59.904406
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("test_message")
    assert str(error) == "test_message"


# Generated at 2022-06-14 04:29:03.559294
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test!")
    except ProgrammingError as e:
        assert e.args[0] == "This is a test!"

# Generated at 2022-06-14 04:29:06.678221
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, "Correct evaluation"):
        ...

    with ProgrammingError.passert(False, "Incorrect evaluation"):
        ...

# Generated at 2022-06-14 04:29:09.316417
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass

# Unit tests for class method passert of class ProgrammingError

# Generated at 2022-06-14 04:29:11.453288
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError("Foo bar")


# Generated at 2022-06-14 04:29:18.179808
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests if :py:class:`ProgrammingError` object can be created and the functionality of method :py:meth:`passert`.
    """
    try:
        # Should not raise exception.
        ProgrammingError.passert(True, "should not raise exception")
    except Exception as e:
        raise AssertionError(f"Should not raise exception: {e}")
    try:
        # Should raise exception.
        ProgrammingError.passert(False, "should raise exception")
    except ProgrammingError as e:
        pass
    except Exception as e:
        raise AssertionError(f"Should raise ProgrammingError, not exception: {e}")
    try:
        # Should raise exception.
        ProgrammingError.passert(False, None)
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:29:44.068297
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as ex:
        assert isinstance(ex, ProgrammingError)
        assert isinstance(ex, Exception)
        assert isinstance(ex, BaseException)
        assert str(ex) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:29:51.621544
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Verifies that the constructor of class ProgrammingError works properly.

    :return: ``True`` if the test succeed and ``False`` if it fails.
    :rtype: ``bool``
    """
    try:
        raise ProgrammingError("The input is not a string")
    except ProgrammingError as exception:
        return "" == exception.args[0]
    else:
        return False


# Generated at 2022-06-14 04:29:55.550543
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert "Broken coherence. Check your code against domain logic to fix it." == str(e)

# Generated at 2022-06-14 04:29:58.197152
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    try:
        raise ProgrammingError("Programming went wrong")
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:30:00.904416
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except Exception as e:
        assert isinstance(e, ProgrammingError)


# Generated at 2022-06-14 04:30:02.749468
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    exception = ProgrammingError("Broken coherence. Check your code against domain logic to fix it.") # type: ProgrammingError
    assert isinstance(exception, ProgrammingError)


# Generated at 2022-06-14 04:30:08.294360
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        # We do nothing. The constructor works as expected.
        pass
    else:
        raise AssertionError("Expected exception, none received.")


# Generated at 2022-06-14 04:30:15.354419
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test message from init
    message = "TEST_ERROR_MESSAGE"
    error = ProgrammingError(message)
    assert message in str(error)
    # Test message from class method passert
    ProgrammingError.passert(condition=False, message=message)
    # Test message from class method passert with empty message
    ProgrammingError.passert(condition=False, message=None)
    # Test the positive case
    ProgrammingError.passert(condition=True, message=message)

# Generated at 2022-06-14 04:30:18.258225
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("test message")
    except ProgrammingError as error:
        assert error.args == ("test message",)
    else:
        assert False, "Instance of ProgrammingError not raises"

# Generated at 2022-06-14 04:30:19.766448
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Test error.")



# Generated at 2022-06-14 04:31:18.953120
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except Exception as e:
        assert type(e) == TypeError
        assert str(e) == "Missing 1 required positional argument: 'message'"

    try:
        ProgrammingError('my very own message')
    except Exception as e:
        assert type(e) == ProgrammingError
        assert str(e) == 'my very own message'

# Generated at 2022-06-14 04:31:21.428581
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test error")
    except ProgrammingError as pe:
        assert str(pe) == "Test error"


# Generated at 2022-06-14 04:31:23.681539
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pypara.contract import Contract

    error = ProgrammingError("Some error")
    Contract.assert_that(error.args[0], "Some error")


# Generated at 2022-06-14 04:31:28.916783
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest

    with pytest.raises(ProgrammingError) as exc_info:
        raise ProgrammingError("Some random error.")

    assert "Some random error." == exc_info.value.args[0]


# Generated at 2022-06-14 04:31:31.261437
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        assert False


# Generated at 2022-06-14 04:31:33.767358
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception)
    assert not issubclass(ProgrammingError, AssertionError)

# Generated at 2022-06-14 04:31:35.260346
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError("test")

# Generated at 2022-06-14 04:31:40.141787
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError`.
    """

    try:
        raise ProgrammingError("Something is broken")
    except ProgrammingError as exp:
        assert str(exp) == "Something is broken"
        assert repr(exp) == "ProgrammingError('Something is broken',)"



# Generated at 2022-06-14 04:31:44.124184
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        assert True
    else:
        assert False, "ProgrammingError failed to raise"


# Generated at 2022-06-14 04:31:53.799599
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Programmer error
    try:
        raise ProgrammingError("This is a programmer error")
    except ProgrammingError as e:
        print(e)
    # Programmer error with default constructor
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        print(e)
    try:
        ProgrammingError.passert(False, "This is a programmer error")
    except ProgrammingError as e:
        print(e)
    ProgrammingError.passert(True, "This is a programmer error")
    print("Unit test for ProgrammingError was successful")

if __name__ == "__main__":
    test_ProgrammingError()
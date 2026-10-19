

# Generated at 2022-06-14 04:23:41.809991
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "does not matter")
    except ProgrammingError:
        pass  # ok
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError:
        pass  # ok
    with pytest.raises(ProgrammingError) as exception:
        ProgrammingError.passert(True, "does not matter")
    assert exception.value.args[0] == ""

# Generated at 2022-06-14 04:23:43.188919
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError()


# Generated at 2022-06-14 04:23:46.574861
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as error:
        assert error.args == ("Broken coherence. Check your code against domain logic to fix it.",)


# Generated at 2022-06-14 04:23:47.526081
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    Programmi

# Generated at 2022-06-14 04:23:49.837695
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the basic functionality of :py:class:`ProgrammingError`.
    """
    raise ProgrammingError("This is a test.")


# Generated at 2022-06-14 04:24:00.523490
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    # Check that an assertion pass
    ProgrammingError.passert(True, None)

    # Check that an assertion fail
    try:
        ProgrammingError.passert(False, "Assertion test")
        raise RuntimeError("ProgrammingError constructor failed (1).")
    except ProgrammingError as ex:
        if str(ex) == "Broken coherence. Check your code against domain logic to fix it.":
            raise RuntimeError("ProgrammingError constructor failed (2).")

    # Check that an assertion fail with a message
    try:
        ProgrammingError.passert(False, "Assertion test")
        raise RuntimeError("ProgrammingError constructor failed (2).")
    except ProgrammingError as ex:
        if str(ex) != "Assertion test":
            raise RuntimeError("ProgrammingError constructor failed (3).")

# Generated at 2022-06-14 04:24:02.655970
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("his is a test")


# Generated at 2022-06-14 04:24:04.041329
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    print("* Testing constructor ...")
    ProgrammingError()


# Generated at 2022-06-14 04:24:06.814157
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError()

    with pytest.raises(ProgrammingError, match="Something is wrong."):
        raise ProgrammingError("Something is wrong.")


# Generated at 2022-06-14 04:24:09.696787
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        assert True
    else:
        assert False



# Generated at 2022-06-14 04:24:11.716669
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    pass

# Generated at 2022-06-14 04:24:15.456681
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as exc_info:
        ProgrammingError.passert(False, "Some error message.")

    assert str(exc_info.value) == "Some error message."


# Generated at 2022-06-14 04:24:22.703120
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError(): # pylint: disable=unused-variable
    """
    Tests the constructor of :py:class:`ProgrammingError`.
    """
    # Executing the constructor raises the exception with the given message
    try:
        raise ProgrammingError("sample message")
    except ProgrammingError as err:
        assert "sample message" == str(err)

    # Executing the constructor raises the exception without message
    try:
        raise ProgrammingError()
    except ProgrammingError as err:
        assert "Broken coherence. Check your code against domain logic to fix it." == str(err)


# Generated at 2022-06-14 04:24:26.716458
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is an error!")
        assert False
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)


# Generated at 2022-06-14 04:24:28.432895
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def test_passert():
        ProgrammingError.passert(True, None)
        try:
            ProgrammingError.passert(False, None)
        except ProgrammingError:
            pass
        else:
            raise AssertionError("Failed to catch ProgrammingError.")
    test_passert()

# Generated at 2022-06-14 04:24:30.660252
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:24:37.101986
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the :py:class:`ProgrammingError` class.
    """

    try:
        ProgrammingError()
        assert False
    except Exception as err:
        assert isinstance(err, ProgrammingError)
        assert str(err) == "Broken coherence. Check your code against domain logic to fix it."

    err = ProgrammingError("A programming error has happened.")
    assert isinstance(err, ProgrammingError)
    assert str(err) == "A programming error has happened."



# Generated at 2022-06-14 04:24:40.559435
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Arrange
    message = "Programming error!"

    # Act and assert
    with ProgrammingError.passert(False, message):
        pass

# Generated at 2022-06-14 04:24:46.564647
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError:
        assert False

    try:
        ProgrammingError.passert(False, "message")
    except ProgrammingError as e:
        assert type(e) is ProgrammingError
        assert e.args == ("message",)
    else:
        assert False

# Generated at 2022-06-14 04:24:48.837240
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for class ProgrammingError."""
    try:
        ProgrammingError("")
    except Exception as e:
        assert isinstance(e, ProgrammingError), "Failed to raise a ProgrammingError"


# Generated at 2022-06-14 04:24:54.058108
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a ProgrammingError")
    except ProgrammingError as e:
        assert "This is a ProgrammingError" == str(e)


# Generated at 2022-06-14 04:24:57.786806
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Error.")
        assert False
    except ProgrammingError as e:
        assert str(e) == "Error."

# Generated at 2022-06-14 04:24:59.827427
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError('test')
    except ProgrammingError as e:
        assert e.args[0] == 'test'


# Generated at 2022-06-14 04:25:02.501583
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Simulated error")


# Generated at 2022-06-14 04:25:06.159137
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Hello, I am a programming error")
    except ProgrammingError as e:
        assert str(e) == "Hello, I am a programming error"


# Generated at 2022-06-14 04:25:10.494883
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Ensures that the :py:class:`ProgrammingError` is properly handled when raised.
    """
    try:
        raise ProgrammingError("This is a programming error")
    except ProgrammingError:
        return
    assert False, "ProgrammingError is not properly handled"


# Generated at 2022-06-14 04:25:12.269608
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("")      # Shall not raise an exception


# Generated at 2022-06-14 04:25:15.478224
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError(message="This is a test")
    except ProgrammingError as e:
        assert str(e) == "This is a test"

# Generated at 2022-06-14 04:25:23.623486
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test the constructor with None as error message
    try:
        raise ProgrammingError(None)
    except ProgrammingError as exc:
        assert type(exc.args) is tuple
        assert len(exc.args) == 1
        assert exc.args[0] is None
        assert str(exc) == "None"

    # Test the constructor with a string as error message
    try:
        raise ProgrammingError("This is a test string.")
    except ProgrammingError as exc:
        assert type(exc.args) is tuple
        assert len(exc.args) == 1
        assert exc.args[0] == "This is a test string."
        assert str(exc) == "This is a test string."


# Generated at 2022-06-14 04:25:26.846519
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is the message")
    except ProgrammingError as error:
        assert error.args[0] == "This is the message"

# Generated at 2022-06-14 04:25:34.988835
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError, match=r"^Broken coherence"):
        ProgrammingError.passert(False, None)



# Generated at 2022-06-14 04:25:40.166158
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError, match="Broken coherence. Check your code against domain logic to fix it."):
        raise ProgrammingError("Broken coherence. Check your code against domain logic to fix it.")


# Generated at 2022-06-14 04:25:41.819458
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("error message") as e:
        assert e.args[0] == "error message"

# Generated at 2022-06-14 04:25:42.994783
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("something is wrong")


# Generated at 2022-06-14 04:25:49.734959
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pypara.testing.abstract_test_case import AbstractTestCase

    class TestCase(AbstractTestCase):
        def test_ProgrammingError(self):
            try:
                raise ProgrammingError()
            except ProgrammingError as e:
                self.assertIsInstance(e, ProgrammingError, "Programming errors should be caught as such.")


# Generated at 2022-06-14 04:25:50.507898
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError()

# Generated at 2022-06-14 04:25:52.770681
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:25:56.120263
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    msg = "Something went wrong"
    try:
        raise ProgrammingError(msg)
    except ProgrammingError as err:
        assert str(err) == msg


# Generated at 2022-06-14 04:26:00.855763
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Test case for :py:class:`ProgrammingError` constructor."""
    # GIVEN:
    condition = False
    message = "A message."
    # WHEN:
    try:
        ProgrammingError.passert(condition, message)
    except ProgrammingError as e:
        # THEN:
        assert str(e) == message

# Generated at 2022-06-14 04:26:02.988832
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest

    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Test")


# Generated at 2022-06-14 04:26:16.008247
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    message = "Unit test"
    try:
        raise ProgrammingError(message)
    except ProgrammingError as e:
        assert message in str(e)
    assert message in str(ProgrammingError(message))


# Generated at 2022-06-14 04:26:18.285274
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:26:21.225716
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests :py:class:`ProgrammingError`.
    """
    ProgrammingError("Message")
    ProgrammingError()


# Generated at 2022-06-14 04:26:32.981491
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.

    :return: ``None``.
    """
    # Constructor with generic message
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        assert False, "Expected a ProgrammingError to be raised."
    # Constructor with a specific message
    try:
        raise ProgrammingError("Something wrong happened.")
    except ProgrammingError:
        pass
    else:
        assert False, "Expected a ProgrammingError to be raised."
    # No error should be raised when the condition is met
    ProgrammingError.passert(True, None)
    # The assertion should raise an error when the condition is not met
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:26:37.519183
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "message")
        assert False  # pragma: no cover
    except ProgrammingError as error:
        assert error.args[0] == "message"



# Generated at 2022-06-14 04:26:46.722652
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from unittest import TestCase
    from . _pyunit_helpers import assert_raises_with_message

    # We setup the test class
    class TestProgrammingError(TestCase):
        """Unit test for class ProgrammingError."""
        def test_ProgrammingError(self):
            """Unit test for constructor of class ProgrammingError."""
            with assert_raises_with_message(ProgrammingError,
                                            "Broken coherence. Check your code against domain logic to fix it."):
                ProgrammingError.passert(False, None)

    # We execute the unit test
    TestProgrammingError().test_ProgrammingError()

# Generated at 2022-06-14 04:26:48.717626
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Test with a message")


# Generated at 2022-06-14 04:26:52.034513
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Aspect not ready.")
    except ProgrammingError as pe:
        assert pe.args[0] == "Aspect not ready."



# Generated at 2022-06-14 04:26:54.032912
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:26:56.315931
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("")


# Generated at 2022-06-14 04:27:19.884613
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    exception1 = ProgrammingError("Dummy error")
    assert exception1.args == ("Dummy error",)
    exception2 = ProgrammingError()
    assert exception2.args == ("Broken coherence. Check your code against domain logic to fix it.",)


# Generated at 2022-06-14 04:27:23.314064
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    "Test case for :py:class:`ProgrammingError`."
    try:
        try:
            raise ProgrammingError()
        except ProgrammingError as err:
            assert not err.args
            raise err
    except ProgrammingError as err:
        assert not err.args


# Generated at 2022-06-14 04:27:30.742664
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.
    """
    test_message = "This error is raised in order to test the constructor of class ProgrammingError."
    try:
        raise ProgrammingError(test_message)
    except ProgrammingError as e:
        assert e.args[0] == test_message
    else:
        raise AssertionError("Expected ProgrammingError exception")


# Generated at 2022-06-14 04:27:34.921565
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Test")
    except TypeError:
        raise AssertionError("ProgrammingError must be constructed with a string argument.")
    except ProgrammingError:
        pass
    else:
        raise AssertionError("ProgrammingError must be raised.")


# Generated at 2022-06-14 04:27:37.466158
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test message")
        assert False
    except ProgrammingError as pe:
        assert pe.args[0] == "Test message"

# Generated at 2022-06-14 04:27:44.137203
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises

    with raises(ProgrammingError, match="Broken coherence. Check your code against domain logic to fix it."):
        ProgrammingError.passert(False, None)

    with raises(ProgrammingError, match="My error!"):
        ProgrammingError.passert(False, "My error!")

# Generated at 2022-06-14 04:27:48.836751
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    with raises(ProgrammingError) as exception_info:
        ProgrammingError() # pylint: disable=E1120, E1123
    assert str(exception_info.value) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:27:52.534996
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        pass
    else:
        raise AssertionError("Does not raise ProgrammingError")

# Unit tests for the passert class method of class ProgrammingError

# Generated at 2022-06-14 04:27:56.159439
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as ex:
        assert str(ex) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:27:58.842768
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        pass
    assert True


# Generated at 2022-06-14 04:28:43.014905
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:28:43.922321
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert callable(ProgrammingError)


# Generated at 2022-06-14 04:28:46.188479
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError()
    assert error.args == ("Broken coherence. Check your code against domain logic to fix it.",)

# Generated at 2022-06-14 04:28:49.298874
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("P")
    except ProgrammingError as e:
        assert "P" == str(e)


# Generated at 2022-06-14 04:28:54.090625
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is a message for a failed assertion")
    except ProgrammingError as e:
        assert e.args[0] == "This is a message for a failed assertion"
    ProgrammingError.passert(True, "This assertion holds")

# Generated at 2022-06-14 04:28:56.721244
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    from pypara import ProgrammingError
    with raises(ProgrammingError):
        ProgrammingError.passert(False, "It fails")

# Generated at 2022-06-14 04:28:59.672995
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "ARGH")
    except ProgrammingError as e:
        assert(e.args[0] == "ARGH")

# Generated at 2022-06-14 04:29:08.106826
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError):
        ProgrammingError.passert(False, None)

    with raises(ProgrammingError):
        ProgrammingError.passert(False, "")

    with raises(ProgrammingError):
        ProgrammingError.passert(False, "Test exception")

    assert ProgrammingError.passert(True, None) is None
    assert ProgrammingError.passert(True, "") is None
    assert ProgrammingError.passert(True, "Test exception") is None

# Generated at 2022-06-14 04:29:10.741051
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError as error:
        assert isinstance(error, ProgrammingError)


# Generated at 2022-06-14 04:29:13.257661
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This should fail")
        assert False
    except ProgrammingError:
        assert True

# Generated at 2022-06-14 04:30:53.147282
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def funAssert(condition, message = None):
        with pytest.raises(ProgrammingError, match=message or "Broken coherence"):
            ProgrammingError.passert(condition, message)
    funAssert(True, 'should not raise')
    funAssert(False, 'should raise')
    funAssert(False, 'should raise and match')

# Generated at 2022-06-14 04:30:57.314274
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test message")
        raise AssertionError("Expected ProgrammingError")
    except ProgrammingError as e:
        assert e.args[0] == "Test message"



# Generated at 2022-06-14 04:31:04.766750
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is the message")
    except ProgrammingError as e:
        assert e.args[0] == "This is the message"
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."
    try:
        ProgrammingError.passert(True, "This is the message")
    except ProgrammingError:
        raise Exception("should not have been raised " \
                        "since the condition was True")

# Generated at 2022-06-14 04:31:08.234013
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Creates an instance of the :py:class:`ProgrammingError` class.
    """
    err = ProgrammingError("Simulated error")
    assert(str(err) == "Simulated error")


# Generated at 2022-06-14 04:31:09.038622
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("This is an error!")
    assert error

# Generated at 2022-06-14 04:31:11.971449
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ProgrammingError."""
    try:
        ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:31:14.822133
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "there was a problem")

# Generated at 2022-06-14 04:31:18.485190
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:31:20.887879
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError(message="hello exception!")

# Generated at 2022-06-14 04:31:26.147067
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Just a test")
        assert False
    except ProgrammingError:
        pass
    try:
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError:
        pass
    ProgrammingError.passert(True, "Just a test")
    ProgrammingError.passert(True, None)
    try:
        raise ProgrammingError("Just a test")
    except ProgrammingError:
        pass
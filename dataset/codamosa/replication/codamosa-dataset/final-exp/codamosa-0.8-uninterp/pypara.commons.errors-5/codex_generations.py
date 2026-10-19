

# Generated at 2022-06-14 04:23:46.007345
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the :py:class:`ProgrammingError` constructor.

    :return: ``None``
    """
    try:
        raise ProgrammingError("Testing")
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert e.args[0] == "Testing"
    try:
        raise ProgrammingError
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."
    try:
        raise ProgrammingError(None)
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:23:51.457314
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    # We expect to have no error if the condition is true.
    ProgrammingError.passert(condition=True, message="")

    # We expect to raise an error if the condition is false.
    try:
        ProgrammingError.passert(condition=False, message="")
    except ProgrammingError:
        pass
    else:
        raise AssertionError("ProgrammingError was not raised.")

# Generated at 2022-06-14 04:23:59.030407
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests :py:class:`ProgrammingError`.
    """
    try:
        ProgrammingError.passert(False, "Error")
        raise AssertionError("Code should have failed.")
    except ProgrammingError as exc:
        assert exc.args[0] == "Error", "Wrong message."

    try:
        ProgrammingError.passert(True, "Error")
    except:
        raise AssertionError("Code should have succeeded.")

# Generated at 2022-06-14 04:24:02.106826
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "MESSAGE")
    except ProgrammingError as e:
        assert e.args[0] == "MESSAGE"


# Generated at 2022-06-14 04:24:03.201224
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("This is a programming error.")

# Generated at 2022-06-14 04:24:09.632900
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class ``ProgrammingError``.
    """
    try:
        raise ProgrammingError("Unit test message")
    except ProgrammingError as error:
        assert error.message == "Unit test message"
    try:
        raise ProgrammingError("")
    except ProgrammingError as error:
        assert error.message == ""


# Generated at 2022-06-14 04:24:20.916799
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import unittest
    from pypara.testing import Patch

    class Setup(unittest.TestCase):

        def setUp(self) -> None:
            self.msg = "dummy error message"

    class TestPassert(Setup):

        def test_passert_condition_is_true(self):
            ProgrammingError.passert(True, self.msg)

        def test_passert_condition_is_false_raises_exception(self):
            with self.assertRaises(ProgrammingError):
                ProgrammingError.passert(False, self.msg)

    class TestConstructor(Setup):

        def test_constructor_returns_proper_instance(self):
            exc = ProgrammingError(self.msg)
            self.assertIsInstance(exc, ProgrammingError)


# Generated at 2022-06-14 04:24:34.530713
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Tests the constructor of class ProgrammingError"""

    # Wrong usage
    try:
        import inspect

        raise ProgrammingError("An error message.")
    except Exception as e:
        assert(isinstance(e, ProgrammingError))
        assert(str(e) == "An error message.")
        assert(inspect.getsource(e.__init__).strip().endswith("Exception.__init__(self, message)"))

    # Correct usage
    ProgrammingError.passert(True, "Should not be called.")
    try:
        ProgrammingError.passert(False, "Should be called.")
    except Exception as e:
        assert(isinstance(e, ProgrammingError))
        assert(str(e) == "Should be called.")


# Generated at 2022-06-14 04:24:38.136416
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test for :py:exc:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("Boom!")
    except ProgrammingError as e:
        e2 = e
    assert "Boom!" in str(e2)


# Generated at 2022-06-14 04:24:46.397892
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)

    try:
        raise ProgrammingError("message")
    except ProgrammingError as e:
        assert str(e) == "message"
        assert e.args == ("message",)


# Generated at 2022-06-14 04:24:51.559475
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("msg")
    except ProgrammingError as e:
        assert str(e) == "msg"
    else:
        assert False, "This line should not have been reached."


# Generated at 2022-06-14 04:25:00.374958
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """ Test the constructor of clas ProgrammingError """
    try:
        ProgrammingError.passert(False, "Test error")
        assert False, "The condition returns a false value"
    except ProgrammingError as err:
        assert True
        assert str(err) == "Test error"

    try:
        ProgrammingError.passert(True, "Test error")
        assert True
    except ProgrammingError as err:
        assert False, "The condition returns a true value and it must be accepted"

    try:
        ProgrammingError.passert(False, None)
        assert False, "The condition returns a false value and it must return an error with a message"
    except ProgrammingError as err:
        assert True
        assert str(err) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:25:05.995475
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the functionality of the constructor of the :py:class:`ProgrammingError`.

    :return: ``None``
    """
    from pytest import raises

    with raises(ProgrammingError):
        raise ProgrammingError

    with raises(ProgrammingError):
        raise ProgrammingError("Test")


# Generated at 2022-06-14 04:25:07.970417
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception)


# Generated at 2022-06-14 04:25:16.898691
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises

    try:
        raise ProgrammingError("Message")
    except ProgrammingError as e:
        assert str(e) == "Message"

    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

    with raises(ProgrammingError):
        ProgrammingError.passert(False, "Message")
        ProgrammingError.passert(True, "Message")

# Generated at 2022-06-14 04:25:18.547202
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, "Foo"):
        assert True


# Generated at 2022-06-14 04:25:26.856461
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # GIVEN
    condition, message = True, "Hello"
    # WHEN-THEN
    try:
        ProgrammingError.passert(condition, message)
    except ProgrammingError as ex1:
        assert False, "ProgrammingError.passert should not raise an error when condition is True"

    # WHEN-THEN
    condition = False
    try:
        ProgrammingError.passert(condition, message)
        assert False, "ProgrammingError.passert should raise an error when condition is False"
    except ProgrammingError as ex2:
        assert ex2.args[0] == message, "ProgrammingError.passert should raise a ProgrammingError with the given " \
                                       "message when condition is False"

    # WHEN-THEN
    condition, message = True, None

# Generated at 2022-06-14 04:25:29.244438
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:25:32.684756
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the :py:class:`ProgrammingError` class.
    """
    try:
        raise ProgrammingError("Error message")
    except ProgrammingError as error:
        assert str(error) == "Error message"

# Generated at 2022-06-14 04:25:34.696992
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        assert False, "The ProgrammingError cannot be instantiated"

# Generated at 2022-06-14 04:25:41.011662
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest

    with pytest.raises(ProgrammingError):
        ProgrammingError()

    with pytest.raises(ProgrammingError) as ex:
        ProgrammingError("Failure")
    assert str(ex.value) == "Failure"


# Generated at 2022-06-14 04:25:45.751293
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "A test message")
        raise AssertionError("Programming error must be raised")
    except ProgrammingError as ex:
        assert ex.args[0] == "A test message"


# Generated at 2022-06-14 04:25:49.993979
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Some message")
        assert False, "The assertion must fail!"
    except ProgrammingError as e:
        assert e.args[0] == "Some message"

# Generated at 2022-06-14 04:25:52.769998
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as ex:
        assert ex.args == ("Test",)


# Generated at 2022-06-14 04:25:56.999759
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():                                                                                          # noqa: E501
    try:
        ProgrammingError.passert(False, message="Foobar")
        assert False
    except ProgrammingError as ex:
        assert str(ex) == "Foobar"

# Generated at 2022-06-14 04:25:59.385545
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    with ProgrammingError(message="Test failed!"):
        raise ProgrammingError("Message not used")

    with ProgrammingError():
        raise ProgrammingError()


# Generated at 2022-06-14 04:26:02.551294
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Programming error message.")
    except ProgrammingError as e:
        assert str(e) == "Programming error message."


# Generated at 2022-06-14 04:26:05.826443
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Checks that :py:class:`ProgrammingError` raises the exception properly.

    :raises AssertionError: In case that :py:class:`ProgrammingError` is not properly checked.
    """

# Generated at 2022-06-14 04:26:09.142527
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as e:
        assert str(e) == "Test"


# Generated at 2022-06-14 04:26:11.384047
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:26:16.223973
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Hello World")
    except ProgrammingError as err:
        assert str(err) == "Hello World"


# Generated at 2022-06-14 04:26:21.101365
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
        assert 0, "Did not raise ProgrammingError"
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:26:25.514967
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert(isinstance(e.args, tuple) and isinstance(e.args[0], str) and e.args[0] == "test")


# Generated at 2022-06-14 04:26:28.733244
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except Exception as e:
        assert type(e) is ProgrammingError


# Generated at 2022-06-14 04:26:32.001517
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Testing error constructor")
    except ProgrammingError as error:
        assert isinstance(error, ProgrammingError)
        assert(str(error) == "Testing error constructor")


# Generated at 2022-06-14 04:26:41.219923
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError`.
    """
    # Call the constructor with a message
    try:
        ProgrammingError("error")
    except ProgrammingError as e:
        assert e.args[0] == "error"

    # Call the constructor without a message
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."



# Generated at 2022-06-14 04:26:43.997250
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests constructor of class :py:class:`ProgrammingError`.

    :return: ``None``
    """
    # Constructor does not require anything
    e = ProgrammingError()
    assert e.args == ()

    # But we can use it with messages
    e = ProgrammingError("Foobar")
    assert e.args == ("Foobar",)


# Generated at 2022-06-14 04:26:48.944590
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError:
        print("Error should not have been raised")
        raise AssertionError

    try:
        ProgrammingError.passert(False, "Error")
    except ProgrammingError:
        return
    raise AssertionError

# Generated at 2022-06-14 04:26:50.123699
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError()
    assert True


# Generated at 2022-06-14 04:26:53.676177
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Asserts the correct initialization of the exception"""
    try:
        raise ProgrammingError("this is a test")
    except ProgrammingError as e:
        assert str(e) == "this is a test"


# Generated at 2022-06-14 04:27:03.928624
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    from pypara.errors import ProgrammingError
    from pypara.errors import ProgrammingError

    with raises(ProgrammingError):
        ProgrammingError()

    with raises(ProgrammingError):
        ProgrammingError.passert(False, "Incorrect condition")

    assert True


# Generated at 2022-06-14 04:27:06.169888
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test.")
    except ProgrammingError as e:
        assert str(e) == "This is a test."

# Generated at 2022-06-14 04:27:08.910707
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ex = ProgrammingError("Expected message")
    assert str(ex) == "Expected message"


# Generated at 2022-06-14 04:27:11.350896
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with assert_raises(ProgrammingError):
        ProgrammingError.passert(False, "This is a test message")

# Generated at 2022-06-14 04:27:12.084273
# Unit test for constructor of class ProgrammingError

# Generated at 2022-06-14 04:27:14.536852
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Hello")
    except ProgrammingError as e:
        assert e.args[0] == "Hello"


# Generated at 2022-06-14 04:27:16.880146
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from contextlib import suppress
    with suppress(ProgrammingError):
        ProgrammingError.passert(condition=False, message="")

# Generated at 2022-06-14 04:27:25.643306
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the :py:class:`ProgrammingError` class.
    """
    try:
        ProgrammingError.passert(condition=True, message="test message")
    except Exception as e:
        assert False, "ProgrammingError.passert() did raise an exception with message \"{0}\".".format(e)

    try:
        ProgrammingError.passert(condition=False, message="test message")
        assert False, "ProgrammingError.passert() did not raise an exception."
    except ProgrammingError as e:
        assert "test message" == e.args[0], "Unexpected message \"{0}\".".format(e.args[0])
    except Exception as e:
        assert False, "ProgrammingError.passert() did raise an unexpected exception with message \"{0}\".".format(e)



# Generated at 2022-06-14 04:27:26.507071
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception)



# Generated at 2022-06-14 04:27:29.684734
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(True, "Test")
    try:
        ProgrammingError.passert(False, "Test")
        assert False
    except ProgrammingError:
        assert True

# Generated at 2022-06-14 04:27:42.046268
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:27:45.892039
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.
    """
    assert ProgrammingError(message="Hello World!").args[0] == "Hello World!"


# Generated at 2022-06-14 04:27:48.985371
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError`

    :return: ``None``
    """
    assert ProgrammingError("message")
    assert ProgrammingError("message"), "Exception not raised"

# Generated at 2022-06-14 04:27:52.716560
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    "Unit test for constructor of class ProgrammingError"
    try:
        raise ProgrammingError("unit test passed")
    except ProgrammingError as e:
        assert str(e) == "unit test passed"


# Generated at 2022-06-14 04:27:56.156415
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A programming error")
    except ProgrammingError as ex:
        assert str(ex) == "A programming error"


# Generated at 2022-06-14 04:28:01.539581
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Tests :py:class:`ProgrammingError` constructor."""
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        assert False, "raise the error"


# Generated at 2022-06-14 04:28:11.488692
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError` for the following cases:

    * The exception behave as a normal one.
    * The condition is met.
    """

    # Given: a generic exception
    m = "Some error"

    # When: the constructor is invoked
    e = ProgrammingError(m)

    # Then: the exception is raised
    assert str(e) == m

    # And: the exception behaves as a normal one
    try:
        raise ProgrammingError(m)
    except ProgrammingError as e:
        assert e.args[0] == m
    else:
        pytest.fail("Failed to raise a ProgrammingError.")

    # And: the condition is fulfilled

# Generated at 2022-06-14 04:28:18.269365
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    msg = "This is an error message."
    try:
        raise ProgrammingError(msg)
    except ProgrammingError as e:
        assert e.__str__() == msg
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:28:22.463837
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, "nothing to see here")
        ProgrammingError.passert(False, "too bad")
    except ProgrammingError as e:
        assert str(e) == "too bad"

# Generated at 2022-06-14 04:28:25.529520
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Don't use this class directly. Use the classmethod passert() instead.")
    except ProgrammingError as err:
        print(err)


# Generated at 2022-06-14 04:28:51.689683
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for the constructor of class :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("This is an error.")
    except ProgrammingError as e:
        assert e.args[0] == "This is an error."


# Generated at 2022-06-14 04:28:57.251444
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for :py:class:`ProgrammingError`.
    """

    from pypara.unit_test import assert_raises_with_matching_message

    assert_raises_with_matching_message(ProgrammingError, "Broken coherence. Check your code against domain logic to fix it.", lambda: ProgrammingError())


# Generated at 2022-06-14 04:29:01.406841
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This should fail")
        assert False
    except ProgrammingError as e:
        assert str(e) == "This should fail"
    try:
        ProgrammingError.passert(True, "This should not fail")
        assert True
    except ProgrammingError as e:
        assert False

# Generated at 2022-06-14 04:29:03.930849
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("Incorrect statement")
    ProgrammingError.passert(True, "Description")

# Generated at 2022-06-14 04:29:07.987700
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Something went wrong!")
        assert False, "No exception has been raised!"
    except ProgrammingError as e:
        assert str(e) == "Something went wrong!"

# Generated at 2022-06-14 04:29:10.623942
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert str(e) == "test"


# Generated at 2022-06-14 04:29:14.538736
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, "All right"):
        assert True
    try:
        with ProgrammingError.passert(False, "Broken!"):
            assert False
    except ProgrammingError as e:
        assert "Broken!" == e.args[0]

# Generated at 2022-06-14 04:29:24.716840
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    try:
        ProgrammingError.passert(False, "Expect True")
    except ProgrammingError as e:
        assert "Expect True" == str(e)
    else:
        raise Exception("Expected ProgrammingError [1]")

    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert "Broken coherence. Check your code against domain logic to fix it." == str(e)
    else:
        raise Exception("Expected ProgrammingError [2]")

    try:
        ProgrammingError.passert(True, "Expect False")
    except ProgrammingError:
        raise Exception("Did not expect ProgrammingError")

# Generated at 2022-06-14 04:29:26.747623
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:29:34.597334
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.
    """
    # pylint:disable=unused-variable
    _ = ProgrammingError("test")
    _ = ProgrammingError("test1").args
    assert ProgrammingError("test1") == ProgrammingError("test1")
    assert not ProgrammingError("test1") == ProgrammingError("test2")
    assert str(ProgrammingError("test1")) == "test1"
    assert repr(ProgrammingError("test1")) == "ProgrammingError('test1',)"

# Generated at 2022-06-14 04:30:28.059036
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Asserts that class :py:class:`ProgrammingError` behaves properly.
    """
    assert issubclass(ProgrammingError, Exception)
    try:
        raise ProgrammingError("Error")
    except ProgrammingError as e:
        assert e.args[0] == "Error"


# Generated at 2022-06-14 04:30:32.143494
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Test")

if __name__ == '__main__':
    test_ProgrammingError()

# Generated at 2022-06-14 04:30:38.800994
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests :py:class:`ProgrammingError` constructor.
    """
    try:
        raise ProgrammingError
    except ProgrammingError:
        pass
    else:
        raise AssertionError("ProgrammingError not raised when no parameters given")
    try:
        raise ProgrammingError("Message")
    except ProgrammingError:
        pass
    else:
        raise AssertionError("ProgrammingError not raised when no parameters given")


# Generated at 2022-06-14 04:30:41.194497
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest

    with pytest.raises(ProgrammingError):
        raise ProgrammingError("FAIL")


# Generated at 2022-06-14 04:30:54.235054
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    # It should raise a ProgrammingError when the code is bugged
    try:
        ProgrammingError.passert(False, None)
        # Check if we reach this point
        assert False
    except ProgrammingError:
        pass

    # It should raise a ProgrammingError when the code is bugged
    try:
        ProgrammingError.passert(False, "Message")
        # Check if we reach this point
        assert False
    except ProgrammingError:
        pass

    # It should not raise a ProgrammingError when the code is not bugged
    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError:
        assert False

    # It should not raise a ProgrammingError when the code is not bugged
    try:
        ProgrammingError.passert(True, "Message")
    except ProgrammingError:
        assert False

# Generated at 2022-06-14 04:30:58.564667
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # ARRANGE
    error = ProgrammingError

    # ACT AND ASSERT
    error.passert(True, "Dummy message")

    # ACT AND ASSERT
    try:
        error.passert(False, "Dummy message")
        assert False
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:31:07.600888
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, message="Internal error.")
    except ProgrammingError:
        import pytest
        pytest.fail("ProgrammingError raised in spite of a proper message.")
    except Exception:
        pass
    else:
        import pytest
        pytest.fail("A ProgrammingError was expected to be raised, but it did not.")
    try:
        ProgrammingError.passert(False, message=None)
    except ProgrammingError:
        pass
    except Exception:
        import pytest
        pytest.fail("A ProgrammingError was expected to be raised, but it did not.")
    else:
        import pytest
        pytest.fail("A ProgrammingError was expected to be raised, but it did not.")

# Generated at 2022-06-14 04:31:15.886947
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Testing of ProgrammingError.
    """
    exception_1 = "This is an error message"
    exception_2 = "This is a different error message"
    try:
        ProgrammingError.passert(False, exception_1)
    except ProgrammingError as err:
        assert str(err) == exception_1

    try:
        ProgrammingError.passert(False, exception_2)
    except ProgrammingError as err:
        assert str(err) == exception_2

# Generated at 2022-06-14 04:31:25.075834
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Try to raise an error without a message and ensure that this exception is raised
    try:
        ProgrammingError()
    except ProgrammingError as e:
        # Check to ensure that the message is assigned to the exception and it is not empty
        assert e.args[0] is not None

    # Try to raise an error with a message and ensure that this exception is raised
    try:
        ProgrammingError("Test message")
    except ProgrammingError as e:
        # Check to ensure that the message is assigned to the exception and it is not empty
        assert e.args[0] == "Test message"

    # Try to raise an error with a message and ensure that this exception is raised
    try:
        ProgrammingError(message="Test message")
    except ProgrammingError as e:
        # Check to ensure that the message is assigned to the exception and it is not empty
        assert e

# Generated at 2022-06-14 04:31:28.455414
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Foo happened.")
    except ProgrammingError as e:
        assert e.args[0] == "Foo happened."


# Generated at 2022-06-14 04:33:14.584373
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        assert False
    except AssertionError:
        with pytest.raises(ProgrammingError, match="Broken coherence"):
            ProgrammingError.passert(False, "Broken coherence")
    ProgrammingError.passert(True, "Should not raise exception")

# Generated at 2022-06-14 04:33:19.430582
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("My message")
    except ProgrammingError as e:
        assert e.args == ("My message",)
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)


# Generated at 2022-06-14 04:33:23.543273
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test")
        raise AssertionError("ProgrammingError has not been raised as expected.")
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:33:26.842094
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError as ex:
        assert str(ex) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:33:30.778015
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Check your code against domain logic.")
    except Exception as err:
        assert(str(err) == "Check your code against domain logic.")
    else:
        assert(False)


# Generated at 2022-06-14 04:33:33.318307
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error: Exception = ProgrammingError()
    assert error.args == ("Broken coherence. Check your code against domain logic to fix it.",)
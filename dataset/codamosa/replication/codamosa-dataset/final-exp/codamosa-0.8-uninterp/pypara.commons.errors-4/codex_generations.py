

# Generated at 2022-06-14 04:23:33.276219
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ProgrammingError"""
    from pypara.constants import COMPLETE_MODULE_NAME
    try:
        raise ProgrammingError("Test of ProgrammingError")
    except ProgrammingError as error:
        assert str(error) == "Test of ProgrammingError"
        assert error.__class__.__module__ == COMPLETE_MODULE_NAME
        assert error.__class__.__qualname__ == "ProgrammingError"


# Generated at 2022-06-14 04:23:46.057552
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the :py:meth:`ProgrammingError.passert`.
    """
    try:
        ProgrammingError.passert(condition=True, message=None)
    except ProgrammingError:
        raise AssertionError("ProgrammingError.passert did not accept a fulfilled condition.")

    try:
        ProgrammingError.passert(condition=False, message="A message")
    except ProgrammingError as e:
        if str(e) != "A message":
            raise AssertionError("ProgrammingError.passert did not use the error message to construct the exception.")
    else:
        raise AssertionError("ProgrammingError.passert did not raise with a not fulfilled condition.")


# Generated at 2022-06-14 04:23:50.164587
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test message.")
        raise AssertionError("Expected exception has not been raised.")
    except ProgrammingError as e:
        assert e.args[0] == "Test message."

# Generated at 2022-06-14 04:23:54.546343
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError):
        ProgrammingError.passert(condition=False, message="")

    with raises(ProgrammingError):
        ProgrammingError.passert(condition=False, message=None)

    with raises(ProgrammingError):
        ProgrammingError.passert(condition=False, message="Something went wrong")

# Generated at 2022-06-14 04:23:58.714810
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """ Unit test for :py:class:`ProgrammingError` """
    try:
        ProgrammingError("Programming error")
    except Exception as exception:
        if not isinstance(exception, ProgrammingError):
            raise Exception("Test of constructor of class ProgrammingError has failed.")


# Generated at 2022-06-14 04:24:04.343439
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from nose.tools import assert_raises, assert_equal
    with assert_raises(ProgrammingError):
        ProgrammingError.passert(False, "This is the message")
    with assert_raises(ProgrammingError):
        ProgrammingError.passert(False, None)
    assert_equal(1, ProgrammingError.passert(True, None))

# Generated at 2022-06-14 04:24:06.355320
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for the constructor of class :py:class:`ProgrammingError`.
    """
    ProgrammingError("Error message")

# Generated at 2022-06-14 04:24:09.822415
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ProgrammingError"""
    try:
        ProgrammingError()
    except ProgrammingError:
        pass
    else:
        assert False


# Generated at 2022-06-14 04:24:16.533674
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    A unit test for the constructor of :py:class:`ProgrammingError`.
    """
    try:
        ProgrammingError.passert(False, "This is a test")
        assert False, "An exception was expected"  # pragma: no cover
    except ProgrammingError as e:
        assert "This is a test" == str(e)


# Generated at 2022-06-14 04:24:17.617633
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("Some programming error")


# Generated at 2022-06-14 04:24:21.878645
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        pass
    else:
        assert False


# Generated at 2022-06-14 04:24:24.820938
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class ProgrammingError.
    """

    with ProgrammingError("Error description."):
        pass



# Generated at 2022-06-14 04:24:28.228356
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test error")
    except ProgrammingError as e:
        assert "Test error" == e.args[0]


# Generated at 2022-06-14 04:24:30.009958
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("Oh oh!"):
        pass


# Generated at 2022-06-14 04:24:38.707423
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import unittest
    import sys

    def test_passert(self):
        with self.assertRaises(ProgrammingError):
            ProgrammingError.passert(False, "Testing")
            with self.assertRaises(TypeError):
                ProgrammingError.passert(None, "Testing")

    class TestProgrammingError(unittest.TestCase):
        def test_init(self):
            try:
                raise ProgrammingError("Testing")
            except ProgrammingError as e:
                self.assertEqual(e.args[0], "Testing")

        def test_passert(self):
            test_passert(self)


# Generated at 2022-06-14 04:24:41.693429
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message="hello")
    except ProgrammingError as err:
        assert err.args == ('hello',)

# Generated at 2022-06-14 04:24:52.919575
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # pylint: disable=unused-argument
    """
    Tests for :py:class:`ProgrammingError`.
    """
    def test_passert_condition():
        """
        Tests for :py:func:`ProgrammingError.passert` (condition is true).
        """
        ProgrammingError.passert(True, None)

    def test_passert_message():
        """
        Tests for :py:func:`ProgrammingError.passert` (condition is false, message is provided).
        """
        try:
            ProgrammingError.passert(False, "FooBarized")
        except ProgrammingError as exception:
            assert str(exception) == "FooBarized"


# Generated at 2022-06-14 04:24:55.555932
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Something went wrong.")
    except ProgrammingError as error:
        assert(str(error) == "Something went wrong.")


# Generated at 2022-06-14 04:24:57.966772
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():  # pylint: disable=missing-docstring
    ProgrammingError()


# Generated at 2022-06-14 04:25:00.161585
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest

    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "Test")

# Generated at 2022-06-14 04:25:03.233358
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as ex:
        assert str(ex) == "Test"


# Generated at 2022-06-14 04:25:04.931794
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("Oops, I did it again!")


# Generated at 2022-06-14 04:25:06.982801
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert issubclass(ProgrammingError, Exception)
    assert isinstance(ProgrammingError, type)


# Generated at 2022-06-14 04:25:12.568632
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Test for constructor of class ProgrammingError"""
    assert ProgrammingError.passert(True, "")

    try:
        ProgrammingError.passert(False, "")
        assert False
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

    try:
        ProgrammingError.passert(False, "foo")
        assert False
    except ProgrammingError as e:
        assert str(e) == "foo"

# Generated at 2022-06-14 04:25:16.724942
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:25:21.244360
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a programming error")
    except ProgrammingError as e:
        assert e.__str__() == "This is a programming error"
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.__str__() == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:25:26.131454
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("You broke the coherence of your domain logic.") as e:
        # noinspection PyUnresolvedReferences
        assert e.args[0] == "You broke the coherence of your domain logic."


if __name__ == "__main__":
    test_ProgrammingError()

# Generated at 2022-06-14 04:25:30.109266
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError(message="Compilation error in the code")
    except ProgrammingError as e:
        assert str(e) == "Compilation error in the code"
    else:
        assert False


# Generated at 2022-06-14 04:25:32.696295
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as exc:
        assert exc is not None and isinstance(exc, Exception)


# Generated at 2022-06-14 04:25:34.695902
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    t = ProgrammingError("No message")
    assert(t.args[0] == "No message")

# Generated at 2022-06-14 04:25:40.296629
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError(message="test")
    except Exception as ex:
        assert isinstance(ex, ProgrammingError)


# Generated at 2022-06-14 04:25:44.781182
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message="Some message")
        assert False
    except ProgrammingError as e:
        assert str(e) == "Some message"

    # Expect no error
    ProgrammingError.passert(condition=True, message="Some message")

# Generated at 2022-06-14 04:25:50.760544
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("TEST")
    except ProgrammingError as e:
        assert "TEST" in str(e)
    try:
        raise ProgrammingError
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:25:56.998912
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.
    """
    from . import unittest
    with unittest.TestCase("__init__", "ProgrammingError") as suite:
        # Setup
        suite.addTest("""
        Test that the constructor works as expected.
        """, lambda t: ProgrammingError("my-message"))


# Generated at 2022-06-14 04:25:58.483209
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    exception = ProgrammingError("foo")
    assert "foo" == exception.args[0]

# Generated at 2022-06-14 04:25:59.937950
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError):
        ProgrammingError()

# Generated at 2022-06-14 04:26:03.601832
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError("test error")
    assert excinfo.type is ProgrammingError
    assert str(excinfo.value) == "test error"


# Generated at 2022-06-14 04:26:13.368853
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    from .testing import assert_error_message

    assert_error_message(ProgrammingError, "Programming error: Broken coherence. "
                                           "Check your code against domain logic to fix it.",
                         "Broken coherence. Check your code against domain logic to fix it.")
    assert_error_message(ProgrammingError, ("Programming error: "), None)

    with raises(ProgrammingError):
        ProgrammingError.passert(False, None)

    with raises(ProgrammingError):
        ProgrammingError.passert(False, "Test failed")

# Generated at 2022-06-14 04:26:19.434991
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import unittest.mock

    with unittest.mock.patch("click.secho") as mocked:
        raised = False
        try:
            ProgrammingError.passert(False, "something is broken")
        except ProgrammingError:
            raised = True
        assert raised, "ProgrammingError.passert() did not raise exception argument"
        assert mocked.assert_called, "ProgrammingError.passert() did not notify the user"

# Generated at 2022-06-14 04:26:23.806136
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    with pytest.raises(ProgrammingError):
        raise ProgrammingError("You should not see me!")

    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "You should not see me!")

# Generated at 2022-06-14 04:26:31.795311
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Arrange
    message = "Heisenbug detected"
    # Act & Assert
    try:
        raise ProgrammingError(message)
    except ProgrammingError as e:
        assert e.args == (message,)

# Generated at 2022-06-14 04:26:33.100278
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError.__doc__



# Generated at 2022-06-14 04:26:36.561207
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("My message")
    except ProgrammingError as e:
        assert str(e) == "My message"
        return

    assert False


# Generated at 2022-06-14 04:26:45.971372
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("First test")
    except ProgrammingError as e:
        assert e.args == ("First test",)

    try:
        raise ProgrammingError("Second test")
    except ProgrammingError as e:
        assert e.args == ("Second test",)

    try:
        raise ProgrammingError(None)
    except ProgrammingError as e:
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)

    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)



# Generated at 2022-06-14 04:26:48.883856
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Cannot recover from messed up state")
    except ProgrammingError as exc:
        assert str(exc) == "Cannot recover from messed up state"



# Generated at 2022-06-14 04:26:50.518246
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    e = ProgrammingError("foo")
    assert e.args[0] == "foo"

# Generated at 2022-06-14 04:26:52.715530
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert not e


# Generated at 2022-06-14 04:26:57.427428
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is a test")
        assert False, "This line must not be executed"
    except ProgrammingError as exception:
        assert str(exception) == "This is a test", "Improper error message associated to the exception"


# Generated at 2022-06-14 04:27:01.538267
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(condition=False, message="Error message.")
    ProgrammingError.passert(condition=True, message="Error message.")

# Generated at 2022-06-14 04:27:05.230981
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Given
    error = None
    # When
    try:
        ProgrammingError.passert(False, "");
    except ProgrammingError as e:
        error = e
    # Then
    assert isinstance(error, ProgrammingError)


# Generated at 2022-06-14 04:27:21.413555
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit tests for :class:`ProgrammingError`."""
    try:
        raise ProgrammingError()
    except ProgrammingError as error:
        assert error.args and "Broken coherence" in str(error)
    try:
        raise ProgrammingError("This should not be raised, we are testing the constructor")
    except ProgrammingError as error:
        assert error.args and "This should not be raised" in str(error)

# Generated at 2022-06-14 04:27:24.631040
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Arrange
    # Act
    error = ProgrammingError()

    # Assert
    assert type(error) == ProgrammingError
    assert str(error) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:27:28.757188
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Foo")
    except ProgrammingError as e:
        assert e.args[0] == "Foo"


# Generated at 2022-06-14 04:27:33.241203
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Wrong code")
        assert False
    except ProgrammingError:
        assert True
    try:
        ProgrammingError.passert(True, "Wrong code")
        assert True
    except ProgrammingError:
        assert False

# Generated at 2022-06-14 04:27:35.577829
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except:
        raise AssertionError("Failed to construct instance of ProgrammingError")

# Generated at 2022-06-14 04:27:38.402182
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert "Programming error has happened" in str(e)

assert test_ProgrammingError() is None

# Generated at 2022-06-14 04:27:45.829739
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is a test")
    except ProgrammingError:
        pass
    else:
        raise AssertionError("Expected ProgrammingError to be raised for this condition")

    try:
        ProgrammingError.passert(True, "This is a test")
    except ProgrammingError:
        raise AssertionError("Expected no ProgrammingError to be raised for this condition")

# Generated at 2022-06-14 04:27:49.528416
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ProgrammingError"""
    try:
        ProgrammingError.passert(False, "Test")
        assert False
    except ProgrammingError:
        pass
    ProgrammingError.passert(True, None)

# Generated at 2022-06-14 04:27:51.813469
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, None)

# Generated at 2022-06-14 04:27:56.069560
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        # noinspection PyUnusedLocal
        def test():
            raise ProgrammingError("Error message to test")

        test()
        assert False, "An assertion error should have been raised"
    except ProgrammingError as e:
        assert "Error message to test" == e.args[0]


# Generated at 2022-06-14 04:28:20.430534
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:28:23.612189
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("")
    except ProgrammingError as e:
        # Check exception message
        assert e.args[0] == ""


# Generated at 2022-06-14 04:28:27.116244
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError(message="something")
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:28:38.300374
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # We call the constructor and expect a ProgrammingError exception
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    # We call the constructor and expect a ProgrammingError exception
    try:
        raise ProgrammingError("Wrong programming")
    except ProgrammingError:
        pass
    # We test that the assertion does nothing
    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError:
        assert False, "OK"
    # We test that the assertion does nothing
    try:
        ProgrammingError.passert(True, "Some error message")
    except ProgrammingError:
        assert False, "OK"
    # We test that the assertion raises a ProgrammingError
    try:
        ProgrammingError.passert(False, None)
        assert False, "Not OK"
    except ProgrammingError:
        pass
    #

# Generated at 2022-06-14 04:28:40.626974
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, "TEST sentinel message"):
        pass


# Generated at 2022-06-14 04:28:44.122326
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of class ProgrammingError
    """
    try:
        ProgrammingError("Test")
    except ProgrammingError:
        pass
    else:
        assert False


# Generated at 2022-06-14 04:28:51.325088
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test that given a false condition and a message, then the exception is raised, and the message is as expected
    try:
        ProgrammingError.passert(False, "Message")
        assert False
    except ProgrammingError as ex:
        assert "Message" == str(ex)
    # Test that given a true condition and a message, then the exception is not raised
    ProgrammingError.passert(True, "Message")

# Generated at 2022-06-14 04:28:56.058125
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
        raise Exception()
    except ProgrammingError as e:
        pass
    try:
        ProgrammingError("Error message")
        raise Exception()
    except ProgrammingError as e:
        assert "Error message" in str(e)


# Generated at 2022-06-14 04:28:59.631280
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test for :py:class:`ProgrammingError`.
    """
    ProgrammingError("test... test... 1... 2... 3...")



# Generated at 2022-06-14 04:29:01.473048
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError()


# Generated at 2022-06-14 04:29:45.375512
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        return
    assert False, "ProgrammingError() did not raise a ProgrammingError exception"


# Generated at 2022-06-14 04:29:55.239091
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError:
        assert False
    try:
        ProgrammingError.passert(False, "Fail!")
    except ProgrammingError as pe:
        assert pe.args[0] == "Fail!"
    try:
        from unittest.mock import MagicMock
        ProgrammingError.passert(False, MagicMock())
        assert False
    except ProgrammingError as pe:
        assert pe.args[0] == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:30:03.988454
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
        assert False, "ProgrammingError() should not raise an exception."
    except Exception:
        pass

    assert ProgrammingError.passert(True, "It is OK.") is None, "ProgrammingError.passert(True, ...) should return None."

    try:
        ProgrammingError.passert(False, "Message in exception.")
        assert False, "ProgrammingError.passert(False, ...) should raise an exception."
    except ProgrammingError as e:
        assert "Message in exception." == e.args[0], "ProgrammingError.passert(False, ...) should contain the message."


# Generated at 2022-06-14 04:30:07.161032
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Some description")
    except ProgrammingError as ex:
        assert(isinstance(ex, ProgrammingError))


# Generated at 2022-06-14 04:30:16.167809
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.
    """

    # Valid arguments
    try:
        ProgrammingError("Test error message.")
    except ProgrammingError as e:
        assert str(e) == "Test error message."
    else:
        assert False, "Expected exception not raised."

    # Default argument
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        assert False, "Expected exception not raised."


# Generated at 2022-06-14 04:30:19.007394
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Message of my programming error")
    except ProgrammingError as e:
        assert str(e) == "Message of my programming error"


# Generated at 2022-06-14 04:30:22.464398
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:30:25.181900
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)


# Generated at 2022-06-14 04:30:26.559289
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError


# Generated at 2022-06-14 04:30:29.159837
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    with raises(ProgrammingError):
        ProgrammingError.passert(False, "Not met.")

# Generated at 2022-06-14 04:32:05.345168
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("I am always wrong.")
    except ProgrammingError as e:
        assert e.args == ("I am always wrong.", )


# Generated at 2022-06-14 04:32:10.843334
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    # Test 1
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

    # Test 2
    try:
        raise ProgrammingError("custom message")
    except ProgrammingError as e:
        assert str(e) == "custom message"



# Generated at 2022-06-14 04:32:12.503158
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "message")


# Generated at 2022-06-14 04:32:14.822825
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:32:17.886878
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from tests import test_ProgrammingError
    test_ProgrammingError.run(ProgrammingError)



# Generated at 2022-06-14 04:32:21.034711
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError
    with pytest.raises(error) as excinfo:
        error()
        assert excinfo == "Passed message"


# Generated at 2022-06-14 04:32:23.088794
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Error")
    except ProgrammingError as e:
        assert str(e) == "Error"

# Generated at 2022-06-14 04:32:26.481080
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        pass
    assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:32:29.319738
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert str(e) == "test"


# Generated at 2022-06-14 04:32:31.923486
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except:
        pass
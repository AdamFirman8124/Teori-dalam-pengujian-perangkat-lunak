

# Generated at 2022-06-14 04:23:34.579414
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(1 == 1, "Test")

# Generated at 2022-06-14 04:23:38.577353
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("message")
    except ProgrammingError:
        pass
    else:
        raise AssertionError("Impossible to instantiate exception")
    assert ProgrammingError("message").args == ("message",)


# Generated at 2022-06-14 04:23:44.451628
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError` with a message.
    """
    try:
        raise ProgrammingError("This is a programming error")
    except ProgrammingError as e:
        assert e.args[0] == "This is a programming error"
    else:
        assert False, "ProgrammingError was not raised"


# Generated at 2022-06-14 04:23:52.772477
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    asserterror = lambda condition, msg: ProgrammingError.passert(condition, msg)
    asserterror(False, "The coherence is broken!")
    try:
        asserterror(True, "Some message")
    except ProgrammingError as e:
        raise AssertionError("Should not raise an exception when the assumption holds")
    try:
        asserterror(False, "Some message")
    except ProgrammingError as e:
        pass
    try:
        asserterror(False, "")
    except ProgrammingError as e:
        pass
    try:
        asserterror(False, None)
    except ProgrammingError as e:
        pass

# Generated at 2022-06-14 04:23:56.499330
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("")
    except ProgrammingError as e:
        assert str(e) == ""
    try:
        raise ProgrammingError("Some error")
    except ProgrammingError as e:
        assert str(e) == "Some error"


# Generated at 2022-06-14 04:23:59.294500
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as ex:
        assert str(ex) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:24:03.690016
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("")
    except ProgrammingError as e:
        assert str(e) == ""

    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:24:11.200790
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for the constructor of class :py:class:`ProgrammingError`.
    """

    error = ProgrammingError("Some error message")

    assert isinstance(error, ProgrammingError)
    assert isinstance(error, Exception)
    assert error.args == ("Some error message",)
    assert error.__str__() == "Some error message"


# Generated at 2022-06-14 04:24:18.843270
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is a message")
    except ProgrammingError as err:
        assert str(err) == "Broken coherence. Check your code against domain logic to fix it."
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as err:
        assert str(err) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:24:22.244491
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        pass
    else:
        assert False, "ProgrammingError not raised"


# Generated at 2022-06-14 04:24:27.522112
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit testing for the constructor of class ProgrammingError."""
    try:
        raise ProgrammingError("a programming error")
    except ProgrammingError as e:
        assert str(e) == "a programming error"


# Generated at 2022-06-14 04:24:32.880886
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises

    with raises(ProgrammingError):
        ProgrammingError.passert(False, "foo bar")

    # Without message
    with raises(ProgrammingError):
        ProgrammingError.passert(False, None)

    # With fulfilled condition
    ProgrammingError.passert(True, "foo bar")

# Generated at 2022-06-14 04:24:36.798854
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def test(message: str) -> None:
        try:
            raise ProgrammingError(message)
        except ProgrammingError as pe:
            assert pe.args == (message,)

    test("This is a test")


# Generated at 2022-06-14 04:24:45.104720
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test message")
    except ProgrammingError as e:
        assert e.args[0] == "Test message"
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."
    ProgrammingError.passert(True, "Any message")

# Generated at 2022-06-14 04:24:47.196756
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        pass
    else:
        raise AssertionError("Should have raised ProgrammingError")

# Generated at 2022-06-14 04:24:48.767354
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # pylint: disable=missing-docstring
    assert ProgrammingError



# Generated at 2022-06-14 04:24:52.436836
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as error:
        assert error.args[0] == "test"


# Generated at 2022-06-14 04:24:57.181340
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test message")
        assert False, "ProgrammingError.passert does not fail"
    except ProgrammingError as e:
        if str(e) != "Test message":
            raise ValueError("ProgrammingError constructor has failed")

# Generated at 2022-06-14 04:24:59.388530
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:25:04.013758
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert "Check your code against domain logic to fix it." == str(e)
    except Exception:
        assert False


# Generated at 2022-06-14 04:25:07.540138
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError:
        pass


# Generated at 2022-06-14 04:25:11.646531
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    try:
        raise ProgrammingError("Someting failed!")
    except ProgrammingError as exc:
        assert str(exc) == "Someting failed!"
    except:
        assert False, "ProgammingError raised an unexpected exception!"


# Generated at 2022-06-14 04:25:16.784699
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test message")
    except ProgrammingError as error:
        assert error.__str__() == "Test message"
        return
    raise AssertionError("ProgrammingError.passert() failed to raise exception.")


# Generated at 2022-06-14 04:25:24.135596
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    class AProgrammingError(ProgrammingError):
        pass

    class BProgrammingError(ProgrammingError):
        pass

    ae_msg = "A domain logic error has been detected."
    ae = AProgrammingError(ae_msg)
    assert ae.msg == ae_msg

    be_msg = "Another domain logic error has been detected."
    be = BProgrammingError(be_msg)
    assert be.msg == be_msg

    assert ae != be


# Generated at 2022-06-14 04:25:32.629643
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests that the exception is raised if ``ProgrammingError.passert`` is called with ``False``.
    """
    try:
        ProgrammingError.passert(False, "Expected message")
    except ProgrammingError as ex:
        if not isinstance(ex, ProgrammingError):
            raise Exception("Unexpected class '%s' in exception." % type(ex))
        if ex.args[0] != "Expected message":
            raise Exception("Unexpected exception message '%s'." % ex.args[0])

# Generated at 2022-06-14 04:25:38.511796
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        # No error expected
        ProgrammingError.passert(True, "")
        # Expecting an error
        ProgrammingError.passert(False, "")
    except ProgrammingError:
        pass
    except Exception:
        assert False, "Expected a ProgrammingError exception"
    else:
        assert False, "Expected a ProgrammingError exception"

# Generated at 2022-06-14 04:25:41.781034
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Something went wrong!")
    except ProgrammingError as e:
        assert str(e) == "Something went wrong!"


# Generated at 2022-06-14 04:25:43.657842
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:25:46.110537
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    # Passes if the error is raised
    ProgrammingError.passert(False, "This is the test")

# Generated at 2022-06-14 04:25:50.886741
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, "Test")
    except ProgrammingError:
        raise Exception("ProgrammingError::passert() failed")
    try:
        ProgrammingError.passert(False, "Test")
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:26:00.666283
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # noinspection PyUnusedLocal
    """Tests the constructor of class ProgrammingError."""
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass

    message = "This is a message."
    try:
        raise ProgrammingError(message)
    except ProgrammingError as exception:
        assert str(exception) == message



# Generated at 2022-06-14 04:26:03.887883
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "error")
        assert False
    except ProgrammingError as e:
        assert str(e) == "error"

# Generated at 2022-06-14 04:26:07.072221
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # noinspection PyTypeChecker
    err = ProgrammingError("m", "n")
    assert str(err) == "m"


# Generated at 2022-06-14 04:26:09.466772
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass # Expected!


# Generated at 2022-06-14 04:26:11.706638
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:26:13.969089
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError()



# Generated at 2022-06-14 04:26:16.621235
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test.")
    except ProgrammingError as e:
        assert "This is a test." in str(e)


# Generated at 2022-06-14 04:26:22.054113
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("An error occurred.")
    except ProgrammingError as error:
        assert error.__class__ is ProgrammingError
        assert error.args == ("An error occurred.",)
    else:
        raise Exception("ProgrammingError has not been raised!")


# Generated at 2022-06-14 04:26:23.868721
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("This is a test"):
        pass


# Generated at 2022-06-14 04:26:26.665218
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ProgrammingError"""

    error = ProgrammingError("Test error.")
    assert str(error) == "Test error."

# Generated at 2022-06-14 04:26:37.217304
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError()

# Generated at 2022-06-14 04:26:41.447886
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "")
        assert False
    except ProgrammingError:
        pass
    try:
        ProgrammingError.passert(True, "")
        pass
    except ProgrammingError:
        assert False

# Generated at 2022-06-14 04:26:43.011530
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("this is a message")
    except ProgrammingError as ex:
        assert str(ex) == "this is a message"


# Generated at 2022-06-14 04:26:47.787069
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ProgrammingError"""
    with ProgrammingError.passert(True, "Condition is met"):
        pass
    with ProgrammingError.passert(False, "Condition is not met"):
        pass


# Generated at 2022-06-14 04:26:57.688298
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    from tdda.constraints.pd.constraints import DfConstraints
    from tdda.referencetest.referencetest import ReferenceTest, MissingDataError
    from tdda.referencetest.comparisons import (NO_COMPARISONS, DEFAULT_COMPARISONS,
                                               COMPARISONS_WITH_EXTRA_PAIRS)
    from pathlib import Path
    from filecmp import cmp

    with raises(ProgrammingError, match=r"^Broken coherence"):
        DfConstraints.constraints(None, "", "", "")

    ReferenceTest.__init__(None, "", "")
    ReferenceTest.__init__(None, "", "", "")

# Generated at 2022-06-14 04:27:01.986821
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("ProgrammingError should happen!")
    except ProgrammingError as e:
        assert str(e) == "ProgrammingError should happen!"


# Generated at 2022-06-14 04:27:03.884800
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
        assert False
    except:
        assert True


# Generated at 2022-06-14 04:27:06.731124
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Something went wrong")
    except ProgrammingError as e:
        assert e.__class__.__name__ == "ProgrammingError"
        assert str(e) == "Something went wrong"


# Generated at 2022-06-14 04:27:09.456108
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as excinfo:
       raise ProgrammingError("test")


# Generated at 2022-06-14 04:27:12.895972
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("Test message."):
        raise ProgrammingError("Test message.")
    with ProgrammingError("Error."):
        ProgrammingError.passert(False, "Error.")


# Generated at 2022-06-14 04:27:37.183154
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    with ProgrammingError.passert(True, ""):
        pass

    msg = "This is an error"
    try:
        with ProgrammingError.passert(False, msg):
            pass
    except ProgrammingError as e:
        m = str(e)
        assert isinstance(m, str)
        assert m == msg

# Generated at 2022-06-14 04:27:41.281404
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as e:
        assert e.args[0] == "Test"


# Generated at 2022-06-14 04:27:44.665163
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Something went wrong!")
    except ProgrammingError as error:
        assert str(error) == "Something went wrong!"


# Generated at 2022-06-14 04:27:49.816096
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert e.args == ("test",)
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)

# Generated at 2022-06-14 04:27:51.299556
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
        assert False, "Should not be reached!"
    except:
        assert True


# Generated at 2022-06-14 04:27:59.487547
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test for :py:class:`ProgrammingError` constructor.
    """
    # Empty constructor
    error_str = str(ProgrammingError())
    assert error_str == "Broken coherence. Check your code against domain logic to fix it.", "Unexpected error message."
    # With message
    error_str = str(ProgrammingError("Message."))
    assert error_str == "Message.", "Unexpected error message."
    # passert
    try:
        ProgrammingError.passert(True, "Error message.")
    except ProgrammingError:
        assert False, "Assertion should not raise an exception."
    try:
        ProgrammingError.passert(False, "Error message.")
        assert False, "Assertion should raise an exception."
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:28:01.925433
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except BaseException as ex:
        assert isinstance(ex, ProgrammingError)


# Generated at 2022-06-14 04:28:05.622810
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test_ProgrammingError")
    except ProgrammingError as e:
        assert(e.args == ("test_ProgrammingError",))
    else:
        assert(False) # assertUnreachable()


# Generated at 2022-06-14 04:28:07.804389
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("Message of the error")


# Generated at 2022-06-14 04:28:09.793887
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("foo")
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:28:57.251003
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is my message")
    except ProgrammingError as e:
        assert e.args == ("This is my message", )
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.", )

# Generated at 2022-06-14 04:29:01.079034
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    error = ProgrammingError("Hey, programmer! Check your code against domain logic to fix it.")
    assert error.args == ("Hey, programmer! Check your code against domain logic to fix it.",)
    assert str(error) == "Hey, programmer! Check your code against domain logic to fix it."



# Generated at 2022-06-14 04:29:02.861552
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:29:10.091212
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    :raises ProgramError: In case that the test is broken.
    """
    try:
        ProgrammingError.passert(False, "This error was raised on purpose.")
    except ProgrammingError:
        pass
    else:
        raise ProgrammingError("The above error should have been raised.")

    # No error should be raised
    ProgrammingError.passert(True, "This error was raised on purpose.")

# Generated at 2022-06-14 04:29:13.512043
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("test")
        assert False
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert str(e) == "test"


# Generated at 2022-06-14 04:29:16.881979
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    from pypara.errors import ProgrammingError
    with raises(ProgrammingError):
        ProgrammingError.passert(False, "No greeting at all")



# Generated at 2022-06-14 04:29:23.331804
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as pe:
        assert pe.args[0] == "test"
        assert isinstance(pe.args, tuple)
        assert len(pe.args) == 1
        assert isinstance(pe.args[0], str)
    else: # pragma: no cover
        assert False


# Generated at 2022-06-14 04:29:26.533844
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    deviation = "This is a test of exception"
    exc = ProgrammingError(deviation)
    assert isinstance(exc, Exception)
    assert exc.description == deviation


# Generated at 2022-06-14 04:29:34.805404
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def _check_ProgrammingError_error(message: Optional[str]):
        try:
            ProgrammingError.passert(False, message)
        except ProgrammingError as ex:
            assert ex.args == (message or "Broken coherence. Check your code against domain logic to fix it.",)
        else:
            assert False, "Call to ProgrammingError.passert(...) should have raised an exception"

    _check_ProgrammingError_error(None)
    _check_ProgrammingError_error("ProgrammingError")
    _check_ProgrammingError_error("Programming error")


# Generated at 2022-06-14 04:29:37.251029
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:31:18.892204
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test message")
    except ProgrammingError as e:
        assert str(e) == "This is a test message"


# Generated at 2022-06-14 04:31:21.754014
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a programming error.")
    except ProgrammingError as e:
        assert str(e) == "This is a programming error."


# Generated at 2022-06-14 04:31:23.994070
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError('Test')
    except Exception as e:
        assert e.args[0] == 'Test'

# Testing of classmethod passert.

# Generated at 2022-06-14 04:31:27.206892
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "test")

# Generated at 2022-06-14 04:31:31.395962
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    with ProgrammingError.passert(True, "Programming error"):
        pass

    try:
        with ProgrammingError.passert(False, "Programming error"):
            pass

        assert False
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:31:40.673371
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest

    with pytest.raises(ProgrammingError, match="some_message"):
        ProgrammingError(message="some_message")

    with pytest.raises(ProgrammingError, match="some_message"):
        ProgrammingError.passert(condition=False, message="some_message")

    ProgrammingError.passert(condition=True, message="some_message")

    with pytest.raises(ProgrammingError, match="Broken coherence"):
        ProgrammingError.passert(condition=False)

    ProgrammingError.passert(condition=True)


if __name__ == '__main__':
    import pytest

    pytest.main(["-s", __file__])

# Generated at 2022-06-14 04:31:53.647181
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # pylint: disable=unused-argument
    # pylint: disable=missing-function-docstring
    # pylint: disable=expression-not-assigned
    # pylint: disable=singleton-comparison

    # Test the exception
    assert isinstance(ProgrammingError("A message"), ProgrammingError)

    # Test the assert
    try:
        ProgrammingError.passert(False, "A message")
    except ProgrammingError as ex:
        assert str(ex) == "A message"
    else:
        raise AssertionError("ProgrammingError.passert didn't raise the exception")

    # Test the assert with no message

# Generated at 2022-06-14 04:31:56.946420
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError`.
    """
    message = "This is an error message"
    assert ProgrammingError(message).message == message

# Generated at 2022-06-14 04:32:00.285126
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "message")
    except ProgrammingError as e:
        assert e.__str__() == "message"



# Generated at 2022-06-14 04:32:05.579458
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Should pass
    ProgrammingError.passert(True, "")

    # Should raise
    try:
        ProgrammingError.passert(False, "")
        assert False, "ProgrammingError.passert(False, '') did not raise"
    except ProgrammingError:
        pass
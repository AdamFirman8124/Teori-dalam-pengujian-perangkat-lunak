

# Generated at 2022-06-14 04:23:39.114279
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A programming error is thrown")
    except ProgrammingError as error:
        assert error.args[0] == "A programming error is thrown", "Programming error has not been thrown properly"
    except:
        raise AssertionError("The wrong exception has been thrown")


# Generated at 2022-06-14 04:23:43.245098
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as exc:
        assert str(exc) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        assert True == False


# Generated at 2022-06-14 04:23:45.662287
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(ProgrammingError):
        raise ProgrammingError()

# Generated at 2022-06-14 04:23:49.340098
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.
    """
    assert "Broken coherence. Check your code against domain logic to fix it." == str(ProgrammingError(""))


# Generated at 2022-06-14 04:23:51.150253
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    err = ProgrammingError()
    assert isinstance(err, ProgrammingError)


# Generated at 2022-06-14 04:23:53.751614
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is the message.")
    except ProgrammingError as err:
        assert err.args[0] == "This is the message."


# Generated at 2022-06-14 04:23:56.116158
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert isinstance(ProgrammingError("test"), Exception)
    assert isinstance(ProgrammingError("test"), ProgrammingError)


# Generated at 2022-06-14 04:23:58.924352
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    from pypara.common.error import ProgrammingError

    with raises(ProgrammingError):
        ProgrammingError("Exception statement")

# Generated at 2022-06-14 04:24:07.371940
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """ Tests the class constructor of :py:class:`ProgrammingError` """
    err = ProgrammingError()
    assert type(err) is ProgrammingError
    assert str(err) == "Broken coherence. Check your code against domain logic to fix it."
    assert repr(err) == "ProgrammingError('Broken coherence. Check your code against domain logic to fix it.')"
    assert isinstance(err, Exception)
    assert issubclass(ProgrammingError, Exception)
    assert err.__class__ is ProgrammingError


# Generated at 2022-06-14 04:24:11.262536
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a programming error")
    except ProgrammingError as e:
        assert str(e) == "This is a programming error"


# Generated at 2022-06-14 04:24:16.715029
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError as exc:
        assert exc.args == ()
    else:
        raise ValueError("ProgrammingError is not raised.")


# Generated at 2022-06-14 04:24:21.693308
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message=None)
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)
    with pytest.raises(ProgrammingError) as e:
        ProgrammingError.passert(condition=False, message="Some message")
    assert isinstance(e.value, ProgrammingError)
    assert e.value.args == ("Some message",)

# Generated at 2022-06-14 04:24:24.859880
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        # Problem: The variable 'a' is not defined.
        a = b
    except NameError as e:
        ProgrammingError("%s: %s" % (type(e).__name__, e))
    except Exception as e:
        raise e


# Generated at 2022-06-14 04:24:26.781672
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for the class :py:class:`ProgrammingError`."""
    my_error = ProgrammingError()
    assert isinstance(my_error, ProgrammingError)
    assert isinstance(my_error, Exception)


# Generated at 2022-06-14 04:24:28.942549
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test for class :py:class:`ProgrammingError`.
    """

    from pytest import raises

    with raises(ProgrammingError):
        ProgrammingError.passert(True, None)

    with raises(ProgrammingError):
        ProgrammingError.passert(False, None)

    with raises(ProgrammingError):
        ProgrammingError.passert(False, "Message")

# Generated at 2022-06-14 04:24:30.811113
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as error:
        assert str(error) == "Broken coherence. Check your code against domain logic to fix it."



# Generated at 2022-06-14 04:24:34.073171
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test")
    except ProgrammingError as e:
        assert e.args[0] == "This is a test"
    else:
        assert False

# Generated at 2022-06-14 04:24:36.561964
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError(message="something")
    except ProgrammingError:
        pass
    else:
        assert 0, "should have raised"


# Generated at 2022-06-14 04:24:39.206347
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("test")
    assert error.args == ("test",)


# Generated at 2022-06-14 04:24:43.602846
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("something has happened")
    except ProgrammingError:
        return "Exception raised."
    return "No exception raised."

assert test_ProgrammingError() == "Exception raised."



# Generated at 2022-06-14 04:24:46.506381
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("test"):
        pass


# Generated at 2022-06-14 04:24:49.956776
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pypara.exceptions import ProgrammingError

    try:
        ProgrammingError.passert(False, "Test message")
    except ProgrammingError as err:
        assert err.args[0] == "Test message"

# Generated at 2022-06-14 04:24:52.233701
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass



# Generated at 2022-06-14 04:24:54.730282
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is a test")
    except ProgrammingError as pe:
        assert pe.__str__() == "This is a test"


# Generated at 2022-06-14 04:24:58.042488
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    "Unit test for constructor of class ProgrammingError"
    error = ProgrammingError('error')
    assert error.__str__() == 'error'

# Generated at 2022-06-14 04:25:02.197357
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    # Test that the message is correctly set
    assert str(ProgrammingError("Message")) == "Message"
    assert str(ProgrammingError()) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:25:05.350228
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.args == ("Broken coherence. Check your code against domain logic to fix it.",)


# Generated at 2022-06-14 04:25:11.805752
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(condition=False, message=None):
        pass
    with ProgrammingError.passert(condition=False, message="Something went wrong"):
        pass
    try:
        with ProgrammingError.passert(condition=True, message=None):
            pass
    except ProgrammingError as e:
        assert False
    try:
        with ProgrammingError.passert(condition=True, message="Something went wrong"):
            pass
    except ProgrammingError as e:
        assert False

# Generated at 2022-06-14 04:25:16.898758
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test message")
    except ProgrammingError as prg_error:
        assert prg_error.args == ("Test message",)
    except Exception:
        assert False, "ProgrammingError's constructor works as expected"


# Generated at 2022-06-14 04:25:18.543339
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Checks that the constructor of the class :py:class:`ProgrammingError` works as expected.
    """
    assert issubclass(ProgrammingError, Exception)


# Generated at 2022-06-14 04:25:23.082939
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message="Test message")
    except ProgrammingError as e:
        assert str(e) == "Test message"

# Generated at 2022-06-14 04:25:25.213425
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:25:28.013226
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test.")
    except Exception as e:
        assert str(e) == "This is a test."

# Generated at 2022-06-14 04:25:31.251266
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        raise Exception("Expected ProgrammingError to be caught")



# Generated at 2022-06-14 04:25:33.337218
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with assert_raises(ProgrammingError):
        ProgrammingError.passert(False, 'ProgrammingError message')

# Generated at 2022-06-14 04:25:36.119367
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Very True")
    except ProgrammingError as err:
        assert str(err) == "Very True"
        return
    raise Exception("Expected error assertion")

# Generated at 2022-06-14 04:25:39.858295
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError('test error')


# Generated at 2022-06-14 04:25:42.562721
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, "test_ProgrammingError"):
        pass
    with ProgrammingError.passert(False, "test_ProgrammingError"):
        pass

# Generated at 2022-06-14 04:25:43.537505
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    pass

# Generated at 2022-06-14 04:25:45.540563
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, "error"):
        pass

# Generated at 2022-06-14 04:25:52.391191
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("a", "b")
    except TypeError:
        pass
    else:
        assert False
    try:
        raise ProgrammingError("description")
    except ProgrammingError as e:
        assert e.args[0]=="description"
    else:
        assert False

# Generated at 2022-06-14 04:25:55.768150
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a programming error instance.")
    except ProgrammingError as e:
        assert str(e) == "This is a programming error instance."


# Generated at 2022-06-14 04:25:56.996427
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(False, message="Error message")

# Generated at 2022-06-14 04:26:00.525794
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("message"):
        pass
    with ProgrammingError.passert(condition=True, message="should pass"):
        pass
    with ProgrammingError.passert(condition=False, message="should fail"):
        pass

# Generated at 2022-06-14 04:26:03.256320
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Error")
    except ProgrammingError as e:
        assert str(e) == "Error"


# Generated at 2022-06-14 04:26:04.453372
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("Random message"):
        assert False

# Generated at 2022-06-14 04:26:07.198809
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(1 < 0, "Error message")

# Generated at 2022-06-14 04:26:10.580792
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test message")
    except ProgrammingError as e:
        assert e.args[0] == "Test message"


# Generated at 2022-06-14 04:26:13.305926
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:26:15.871554
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("error")
    except ProgrammingError as e:
        assert str(e) == "error"



# Generated at 2022-06-14 04:26:23.201760
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    exception = ProgrammingError("test")
    assert exception.args[0] == "test"



# Generated at 2022-06-14 04:26:24.455041
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("Dummy programming error")

# Generated at 2022-06-14 04:26:26.211928
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(False, "Foo")


# Generated at 2022-06-14 04:26:29.251725
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("There is an issue with the logic of your program.")
    except ProgrammingError as e:
        assert str(e) == "There is an issue with the logic of your program."


# Generated at 2022-06-14 04:26:33.278347
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError:
        raise AssertionError("ProgrammingError.passert succeeded, while it shouldn't")
    try:
        ProgrammingError.passert(False, "Intended message")
    except ProgrammingError as e:
        if str(e) != "Intended message":
            raise AssertionError("ProgrammingError.passert diagnosis error")
    else:
        raise AssertionError("ProgrammingError.passert succeeded, while it shouldn't")

# Generated at 2022-06-14 04:26:39.268055
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError as e:
        assert True
    try:
        ProgrammingError.passert(False, "Boudou")
        assert False
    except ProgrammingError as e:
        assert str(e) == "Boudou"

# Generated at 2022-06-14 04:26:42.428891
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test_ProgrammingError")
    except ProgrammingError as ex:
        assert ex.args[0] == "test_ProgrammingError"



# Generated at 2022-06-14 04:26:45.192229
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "foo")
    except ProgrammingError as ex:
        assert str(ex) == "foo"


# Generated at 2022-06-14 04:26:48.871946
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pypara.common.exception import ProgrammingError

    try:
        raise ProgrammingError("foo")
    except ProgrammingError as e:
        assert str(e) == "foo"

# Unit tests for function passert

# Generated at 2022-06-14 04:26:58.569966
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from nose_parameterized import parameterized
    from pypara.utils import raise_exception
    from pypara.utils import get_exception_message

    @parameterized.expand([
        ["", ""],
        ["This is an error message.", "This is an error message."]
    ])
    def _test(message: str, expected: str):
        try:
            raise_exception(ProgrammingError(message))
        except ProgrammingError as e:
            assert get_exception_message(e) == expected, "The message of the exception is not correct"


# Generated at 2022-06-14 04:27:11.679563
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a programming error")
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)

# Generated at 2022-06-14 04:27:16.714039
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as error:
        assert str(error) == "Broken coherence. Check your code against domain logic to fix it."

    try:
        raise ProgrammingError("Message for ProgrammingError")
    except ProgrammingError as error:
        assert str(error) == "Message for ProgrammingError"


# Generated at 2022-06-14 04:27:20.828907
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "Sample message")
    ProgrammingError.passert(True, "Sample message")
    ProgrammingError.passert(True, "Sample message")
    ProgrammingError.passert(True, None)

# Generated at 2022-06-14 04:27:26.950507
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Test for constructor of :py:class:`ProgrammingError`"""
    try:
        raise ProgrammingError("This should be handled!")
    except ProgrammingError as e:
        assert "This should be handled!" in repr(e)
        assert "This should be handled!" in str(e)


# Generated at 2022-06-14 04:27:31.536595
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests for the constructor of class :py:class:`ProgrammingError`.
    """
    try:
        ProgrammingError('test error message')
    except ProgrammingError as pe:
        assert str(pe) == 'test error message'
        return

    assert False, 'Error not raised'


# Generated at 2022-06-14 04:27:35.799597
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the :py:class:`ProgrammingError` constructor.
    """
    try:
        raise ProgrammingError("Custom error message.")
    except ProgrammingError as err:
        assert isinstance(err, ProgrammingError)



# Generated at 2022-06-14 04:27:40.082881
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # should not throw an exception
    ProgrammingError.passert(True, None)
    ProgrammingError.passert(True, "")

    # should throw an exception
    try:
        ProgrammingError.passert(False, None)
        assert False, "Expected to raise ProgrammingError"
    except ProgrammingError:
        pass

    try:
        ProgrammingError.passert(False, "")
        assert False, "Expected to raise ProgrammingError"
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:27:45.400105
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is an error.")
    except ProgrammingError as e:
        assert e.args[0] == "This is an error.", \
            "ProgrammingError should assign the exception message as the first element of the args tuple."


# Generated at 2022-06-14 04:27:49.583093
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Broken coherence.")
        assert False, "Unreachable code has been reached."
    except ProgrammingError as e:
        assert str(e) == "Broken coherence."


# Generated at 2022-06-14 04:27:50.314399
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, None):
        pass

# Generated at 2022-06-14 04:28:14.495381
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "message")
    except ProgrammingError as ex:
        assert ex.args[0] == "message"
    ProgrammingError.passert(True, "message")

# Generated at 2022-06-14 04:28:16.922141
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("a message")
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:28:21.177614
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a dummy message")
    except ProgrammingError as e:
        err_msg = e.args[0]
        assert err_msg == "This is a dummy message"


# Generated at 2022-06-14 04:28:24.385103
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Testing exception class")
    except ProgrammingError as e:
        assert(e.args[0] == "Testing exception class")


# Generated at 2022-06-14 04:28:28.137575
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(condition=True, message=None):
        pass
    with ProgrammingError.passert(condition=False, message=None):
        pass

# Generated at 2022-06-14 04:28:29.746509
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("This is a message",)


# Generated at 2022-06-14 04:28:32.069961
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        return
    assert False, "Did not raise exception"


# Generated at 2022-06-14 04:28:36.876507
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    try:
        raise ProgrammingError("Some message here.")
    except ProgrammingError as e:
        assert str(e) == "Some message here."

# Generated at 2022-06-14 04:28:38.450169
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("Test")
    assert str(error).__eq__("Test")


# Generated at 2022-06-14 04:28:42.065707
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a dummy message.")
    except ProgrammingError as e:
        assert e.message == "This is a dummy message."

# Generated at 2022-06-14 04:29:30.859738
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:

        # When: raise a ProgrammingError
        ProgrammingError.passert(False, "My message")

        # Then: Exception should be raised
        assert False, "Should have raised an exception"

    except ProgrammingError as pe:
        # Then: Message should be equal to message introduced as a parameter
        assert pe.args[0] == "My message"

    except Exception as e:
        # Then: Exception should be of type ProgrammingError
        assert False, "Should have raised a ProgrammingError. Raised {}".format(type(e))

# Generated at 2022-06-14 04:29:32.860635
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError("This is an error")


# Generated at 2022-06-14 04:29:35.774827
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as error:
        assert error.args[0] == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:29:44.673369
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    class Oops(Exception):
        pass

    try:
        ProgrammingError.passert(True, None)
    except Exception as e:
        raise Oops("ProgrammingError.passert does not seem to ignore fulfilled condition.") from e

    try:
        ProgrammingError.passert(False, "Klokkenluider, klokkenluider, torenbouwer, torenbouwer...")
    except ProgrammingError as e:
        assert str(e) == "Klokkenluider, klokkenluider, torenbouwer, torenbouwer..."
    else:
        raise Oops("ProgrammingError.passert did not raise error on failed condition.")


# Generated at 2022-06-14 04:29:47.491694
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert str(e) == "test"


# Generated at 2022-06-14 04:29:51.131488
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is a test")
    except ProgrammingError as e:
        assert "This is a test" == str(e)

# Generated at 2022-06-14 04:29:56.538552
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of class ProgrammingError.
    """
    try:
        raise ProgrammingError("Testing")
    except ProgrammingError as e:
        assert e.args == ("Testing",)
    else:
        raise Exception("ProgrammingError Exception has not been raised")


# Generated at 2022-06-14 04:29:58.766047
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Test")


# Generated at 2022-06-14 04:30:02.180858
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Testing...")
    except ProgrammingError as e:
        expected = "Testing..."
        actual = str(e)
        assert expected == actual
        assert isinstance(e, ProgrammingError)


# Generated at 2022-06-14 04:30:06.977104
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Given
    message = "I am the error message"

    # When
    error = ProgrammingError(message)

    # Then
    assert error.args == (message,)


# Generated at 2022-06-14 04:31:47.099481
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError()

    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Broken coherence. Check your code against domain logic to fix it.")


# Generated at 2022-06-14 04:31:50.371122
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError.passert(True, "") is None

    # Unit test for passert of class ProgrammingError
    try:
        ProgrammingError.passert(False, "")
        assert False
    except ProgrammingError:
        assert True

# Generated at 2022-06-14 04:31:56.177324
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of :py:class:`ProgrammingError`.
    """

    # No error raised
    msg = "This is a test"
    try:
        ProgrammingError.passert(True, msg)
    except ProgrammingError:
        assert False

    # Error raised
    try:
        ProgrammingError.passert(False, msg)
        assert False
    except ProgrammingError as e:
        assert e.args[0] == msg

# Generated at 2022-06-14 04:31:58.210229
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as e:
        assert e.args[0] == "Test"


# Generated at 2022-06-14 04:32:02.435662
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for constructor of class ProgrammingError.
    """
    try:
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:32:09.873704
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :class:`ProgrammingError`.
    """
    try:
        ProgrammingError("Expected message")
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError), "Expected class ProgrammingError."
        assert hasattr(e, "message"), "Expected e.message."
        assert e.message == "Expected message", "Expected message 'Expected message', got '{}'".format(e.message)


# Generated at 2022-06-14 04:32:13.043406
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Some message")
    except ProgrammingError as e:
        assert e.args[0] == "Some message"
    else:
        assert False, "Expected to raise ProgrammingError due to False condition."

# Generated at 2022-06-14 04:32:17.396457
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is just a test")
    except ProgrammingError as e:
        assert "This is just a test" in str(e)


# Generated at 2022-06-14 04:32:20.354337
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Negative test trying to construct a ProgrammingError using the constructor
    assert False, "Negative test succeeded: We have to use the class method for construction."


# Generated at 2022-06-14 04:32:23.962682
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises

    with raises(ProgrammingError):
        ProgrammingError.passert(False, "This is a test")
        ProgrammingError.passert(True, "This is a test")


# Generated at 2022-06-14 04:23:36.740413
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the :py:class:`ProgrammingError` constructor.
    """
    try:
        raise ProgrammingError("Test")
    except ProgrammingError as e:
        assert(e.args[0] == "Test")


# Generated at 2022-06-14 04:23:37.996712
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError()


# Generated at 2022-06-14 04:23:43.461330
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of the class ProgrammingError.
    """
    try:
        raise ProgrammingError("Testing")
    except Exception as exception:
        if str(exception) != "Testing":
            raise Exception("test_ProgrammingError: testing failed")
    else:
        raise Exception("test_ProgrammingError: testing failed")


# Generated at 2022-06-14 04:23:52.740752
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Some description")
        assert False, "Should have raised ProgrammingError."
    except ProgrammingError as e:
        assert e.args[0] == "Some description"

    try:
        ProgrammingError.passert(False, None)
        assert False, "Should have raised ProgrammingError."
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."

    try:
        ProgrammingError.passert(True, "Some description")
        assert True, "Should not have raised ProgrammingError."
    except ProgrammingError as e:
        assert False, "Should not have raised ProgrammingError."


# Generated at 2022-06-14 04:23:57.892101
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Testing ProgrammingError")
    except ProgrammingError as e:
        assert(isinstance(e, ProgrammingError) and e.args[0] == "Testing ProgrammingError")
        print("ProgrammingError test succeeded.")
    else:
        assert(False and "It should have raised a ProgrammingError!")

# Generated at 2022-06-14 04:24:02.270220
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("fake message")
    except ProgrammingError as e:
        assert str(e) == "fake message"
    else:
        raise Exception("Expected exception")


# Generated at 2022-06-14 04:24:09.565086
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(True, "Test")
    try:
        ProgrammingError.passert(False, "Test")
    except ProgrammingError as e:
        assert str(e) == "Test"
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:24:15.823047
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("Accidental error in domain logic"):
        raise ProgrammingError("Expected error in domain logic")
    try:
        raise ProgrammingError("Expected error in domain logic")
    except ProgrammingError as e:
        message = e.args[0]
    assert message == "Expected error in domain logic"


# Generated at 2022-06-14 04:24:18.785375
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("test")
    assert error.args == ("test",)
    assert str(error) == error.args[0] == "test"


# Generated at 2022-06-14 04:24:23.301639
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Check that the constructor runs ok
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    try:
        raise ProgrammingError("x")
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:24:27.460586
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Not working")
    except ProgrammingError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:24:30.716953
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "New Error")
    except ProgrammingError as err:
        assert str(err) == "New Error"


# Generated at 2022-06-14 04:24:34.473413
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Any message")
    except ProgrammingError as ex:
        assert isinstance(ex, Exception)
        assert ex.args == ("Any message",)


# Generated at 2022-06-14 04:24:36.188786
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("Test message")
    assert error.args[0] == "Test message"


# Generated at 2022-06-14 04:24:44.929119
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class ProgrammingError.

    :return: None
    """
    try:
        ProgrammingError.passert(False, "My condition is bogus")
        assert False
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert e.args[0] == "My condition is bogus"
    except Exception:
        assert False
    try:
        ProgrammingError.passert(True, "My condition is bogus")
    except Exception:
        assert False

# Generated at 2022-06-14 04:24:47.522665
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("message")
    except ProgrammingError as e:
        assert e.args[0] == "message"


# Generated at 2022-06-14 04:24:50.441461
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a programming error.")
    except ProgrammingError as e:
        assert e.args[0] == "This is a programming error."


# Generated at 2022-06-14 04:24:53.764442
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # GIVEN

    # WHEN
    exception = ProgrammingError("Assertion has failed")

    # THEN
    assert "Assertion has failed" == exception.args[0]



# Generated at 2022-06-14 04:24:59.390207
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, "This should not be run"):
        print("Foo")
    try:
        with ProgrammingError.passert(False, "GAG"):
            print("Bar")
    except ProgrammingError as err:
        assert err.args[0] == "GAG"

# Generated at 2022-06-14 04:25:04.536870
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():

    # Define a message for the exception
    message = "The specified code is breaking coherence with the domain logic."

    # Create the exception passing the message
    exception = ProgrammingError(message)

    # Check the message
    assert exception.args[0] == message



# Generated at 2022-06-14 04:25:09.401577
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "The condition is not met")
    except ProgrammingError as error:
        assert error.args[0] == "The condition is not met"
    else:
        assert False

# Generated at 2022-06-14 04:25:12.380424
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    else:
        raise Exception("ProgrammingError() should be raised")

# Generated at 2022-06-14 04:25:17.023505
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # pylint: disable=E0110

    with ProgrammingError.passert(False, None):
        pass # pragma: no cover

    with ProgrammingError.passert(False, "My message"):
        pass # pragma: no cover

# Generated at 2022-06-14 04:25:18.623204
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "This is a test")
    except ProgrammingError as e:
        assert str(e) == "This is a test"


# Generated at 2022-06-14 04:25:22.447108
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test function for constructor of class ProgrammingError.
    """
    with pytest.raises(ProgrammingError) as info:
        ProgrammingError("Test message")
    assert info.value.args[0] == "Test message"

# Generated at 2022-06-14 04:25:27.158072
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "We have a problem.")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        raise AssertionError("The above statement must rise an exception.")

# Generated at 2022-06-14 04:25:40.326005
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("Test case"):
        pass

    try:
        with ProgrammingError("Test case"):
            raise AssertionError("Test case")
    except AssertionError as ae:
        assert str(ae) == "Test case"
    else:
        raise AssertionError("Test case")

    with ProgrammingError("Test case"):
        raise ProgrammingError("Test case")

    with ProgrammingError("Test case"):
        raise AssertionError("Test case")

    try:
        with ProgrammingError("Test case"):
            raise AssertionError("Test case")
    except AssertionError as ae:
        assert str(ae) == "Test case"
    else:
        raise AssertionError("Test case")

    with ProgrammingError("Test case"):
        raise ProgrammingError("Test case")




# Generated at 2022-06-14 04:25:42.086277
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, "A message."):
        pass



# Generated at 2022-06-14 04:25:49.801583
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test for :py:class:`ProgrammingError`.
    """
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as exc:
        assert isinstance(exc, ProgrammingError)
        assert str(exc) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        raise RuntimeError("Broken coherence. ProgrammingError not raised when expected.")

# Generated at 2022-06-14 04:25:51.551507
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    pass

# Generated at 2022-06-14 04:25:56.736145
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "My assertion failed")
        raise AssertionError("Expected exception not raised")
    except ProgrammingError as e:
        assert e.args == ("My assertion failed",)

# Generated at 2022-06-14 04:25:59.532561
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("No problem here")
    except ProgrammingError as e:
        assert "No problem here" == str(e)


# Generated at 2022-06-14 04:26:03.603024
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("'ProgrammingError' test is done!")
    except ProgrammingError as e:
        assert str(e) == "'ProgrammingError' test is done!"

# Unit tests for passert method of class ProgrammingError

# Generated at 2022-06-14 04:26:09.405062
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("Example message")
    except ProgrammingError as exception:
        assert str(exception) == "Example message"
    else:
        assert False, "ProgrammingError was not raised"


# Generated at 2022-06-14 04:26:13.118406
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        assert False

# Generated at 2022-06-14 04:26:22.911864
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # pylint: disable=missing-function-docstring, no-self-use
    # noinspection PyMethodMayBeStatic
    class TestProgrammingError(ProgrammingError):

        def __init__(self, message: str, new_param: bool):
            super().__init__(message)
            # We want to test that you can use `super` to initialize parent exception classes.
            self._new_param = new_param

        @property
        def new_param(self) -> bool:
            return self._new_param

    # noinspection PyUnusedLocal
    raised: TestProgrammingError = None


# Generated at 2022-06-14 04:26:25.204727
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    err = ProgrammingError(message="some message")
    assert str(err) == "some message"

# Generated at 2022-06-14 04:26:28.001741
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises

    with raises(ProgrammingError):
        ProgrammingError("Programming error")


# Generated at 2022-06-14 04:26:30.038513
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError()


# Generated at 2022-06-14 04:26:34.358414
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except Exception as e:
        assert isinstance(e, ProgrammingError)
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:26:42.154424
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Check if bad condition raises exception
    try:
        ProgrammingError.passert(False, "")
    except ProgrammingError as error:
        assert error
    else:
        assert False, "Undesired exception"

    # Check if good condition does not raise an exception
    ProgrammingError.passert(True, "")

# Generated at 2022-06-14 04:26:44.118821
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(1 == 1, "We should not get here")
    try:
        ProgrammingError.passert(1 != 1, "Bad assertion")
    except ProgrammingError:
        return
    raise Exception("ProgrammingError test failed")

# Generated at 2022-06-14 04:26:49.429672
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Testing the constructor")
    except ProgrammingError as pe:
        assert pe.args[0] == "Testing the constructor"
        assert pe.args[1] is None
    except Exception as e:
        pytest.fail(f"Expected a ProgrammingError but was {e}")


# Generated at 2022-06-14 04:26:50.645331
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert 1 == 1


# Generated at 2022-06-14 04:26:54.970435
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Hello World")
    except ProgrammingError as e:
        error = e
    else:
        error = None
        raise AssertionError("Error not raised")

    assert error.args == ("Hello World",)

# Generated at 2022-06-14 04:27:00.816169
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test for the constructor of the :py:class:`ProgrammingError`.
    """
    message = "Hi! I'm a message for a programming error exception."
    try:
        raise ProgrammingError(message)
    except ProgrammingError as exception:
        assert exception.args[0] == message, exception


# Generated at 2022-06-14 04:27:03.623153
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("testing class")
    except ProgrammingError as e:
        assert e.args[0] == "testing class"

# Generated at 2022-06-14 04:27:06.217701
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # GIVEN
    msg = 'foo'
    # WHEN
    try:
        ProgrammingError(msg)
    except ProgrammingError as pe:
        # THEN
        assert pe.args[0] == msg

# Generated at 2022-06-14 04:27:09.837595
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        pass
    else:
        assert False, "ProgrammingError constructor must always raise the exception"



# Generated at 2022-06-14 04:27:13.167515
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Foo")
    except ProgrammingError as e:
        assert e.args[0] == "Foo"


# Generated at 2022-06-14 04:27:19.024461
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError

# Generated at 2022-06-14 04:27:22.325239
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."



# Generated at 2022-06-14 04:27:24.313577
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("Test message")
    assert error.message == "Test message"


# Generated at 2022-06-14 04:27:28.031463
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("undefined")
    except Exception as e:
        assert isinstance(e, ProgrammingError)



# Generated at 2022-06-14 04:27:31.093993
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Custom message")
    except ProgrammingError as e:
        assert "Custom message" == e.args[0]

# Generated at 2022-06-14 04:27:34.912741
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Something went wrong with the program's logic: ...")
    except ProgrammingError as e:
        assert "Something went wrong with the program's logic: ..." == str(e)



# Generated at 2022-06-14 04:27:36.881044
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    message = "Foo bar"
    error = ProgrammingError(message)
    assert error.message == message

# Generated at 2022-06-14 04:27:39.358041
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Calling constructor.
    try:
        raise ProgrammingError("Broken coherence. Check your code against domain logic to fix it.")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:27:44.665190
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        # noinspection PyUnresolvedReferences
        __ = ProgrammingError("Error message")
    except Exception as programming_error:
        assert isinstance(programming_error, ProgrammingError)
        assert programming_error.args[0] == "Error message"


# Generated at 2022-06-14 04:27:46.667140
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("msg"):
        pass



# Generated at 2022-06-14 04:28:00.486670
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test_ProgrammingError")
    except ProgrammingError as e:
        assert str(e) == "test_ProgrammingError"


# Generated at 2022-06-14 04:28:02.034753
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:28:08.797948
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("I got an error ")
    except ProgrammingError as e:
        if "I got an error" not in str(e):
            assert False
    ProgrammingError.passert(False, "I got an error")
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        if "Check your code against domain logic" not in str(e):
            assert False

# Generated at 2022-06-14 04:28:14.081758
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message="")
        assert False
    except ProgrammingError:
        pass
    try:
        ProgrammingError.passert(condition=False, message="my message")
        assert False
    except ProgrammingError as ex:
        assert str(ex) == "my message"
    assert ProgrammingError.passert(condition=True, message="") is None

# Generated at 2022-06-14 04:28:25.744012
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, None)
    except ProgrammingError:
        assert False, "The condition is met, the exception should not be raised."
    try:
        ProgrammingError.passert(False, None)
        assert False, "The condition is not met, the exception should be raised."
    except ProgrammingError:
        assert True, "The condition is not met, the exception has to be raised."
    try:
        ProgrammingError.passert(False, "CUSTOM ERROR")
        assert False, "The condition is not met, the exception should be raised."
    except ProgrammingError as e:
        assert str(e) == "CUSTOM ERROR", "An error message has been provided, it has to be used."

# Generated at 2022-06-14 04:28:33.473732
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of the class :py:class:`ProgrammingError`.
    """

    def raise_programming_error(message: Optional[str]) -> None:
        """
        Raises a :py:class:`ProgrammingError`.
        :param message: Message of the exception.
        :raises ProgrammingError:
        """
        raise ProgrammingError(message)

    try:
        raise_programming_error("This is an expected error")
    except ProgrammingError as ex:
        assert "This is an expected error" == ex.args[0]


# Generated at 2022-06-14 04:28:38.678841
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    success = False
    try:
        raise ProgrammingError("Test")
        assert False, "Exception not raised."
    except ProgrammingError as e:
        assert str(e) == "Test", "Unexpected message in exception."
        success = True
    assert success, "Error not thrown."


# Generated at 2022-06-14 04:28:46.610872
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    class TestError(ProgrammingError):
        pass

    try:
        raise TestError("Some long description of a programming error")
    except TestError as e:
        assert str(e) == "Some long description of a programming error", f"Wrong message. {str(e)}"
        assert type(e) is TestError

    try:
        raise AssertionError("Some long description of an assertion error")
    except AssertionError as e:
        assert str(e) == "Some long description of an assertion error", f"Wrong message. {str(e)}"
        assert type(e) is AssertionError


# Generated at 2022-06-14 04:28:51.259501
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as exception:
        assert str(exception) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        assert False, "Error not raised."


# Generated at 2022-06-14 04:28:54.531797
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A programming error was introduced.")
    except ProgrammingError as e:
        assert "A programming error was introduced." in str(e)


# Generated at 2022-06-14 04:29:16.940569
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError("Testing ProgrammingError constructor")


# Generated at 2022-06-14 04:29:18.582171
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:29:23.254112
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError(): # pylint: disable=missing-function-docstring
    from nose import tools
    from pypara.errors import ProgrammingError

    tools.assert_raises(ProgrammingError, lambda: ProgrammingError(None))
    tools.assert_raises(ProgrammingError, lambda: ProgrammingError(""))
    tools.assert_raises(ProgrammingError, lambda: ProgrammingError("a message"))



# Generated at 2022-06-14 04:29:30.714859
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Type hinting
    from pytest import raises

    # Test nominal behaviour
    try:
        raise ProgrammingError()
    except ProgrammingError as ex:
        assert not ex.args

    # Test error message
    try:
        raise ProgrammingError("This is an error")
    except ProgrammingError as ex:
        assert ex.args[0] == "This is an error"

    # Test type hinting
    with raises(ProgrammingError):
        raise ProgrammingError()


# Generated at 2022-06-14 04:29:32.204963
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with assertRaises(ProgrammingError):
        ProgrammingError()


# Generated at 2022-06-14 04:29:33.606727
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def test():
        raise ProgrammingError()
    assert test.__name__ == "test"


# Generated at 2022-06-14 04:29:36.694670
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    e = ProgrammingError("testing")
    assert str(e) == "testing"
    with raises(ProgrammingError):
        ProgrammingError.passert(False, "unit testing")

# Generated at 2022-06-14 04:29:42.848068
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test")
    except ProgrammingError as e:
        assert e.args[0] == "Test"
    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."
    try:
        ProgrammingError.passert(True, "Test")
    except ProgrammingError as e:
        assert False

# Generated at 2022-06-14 04:29:44.506408
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as ex:
        pass


# Generated at 2022-06-14 04:29:57.290276
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # This code should never be executed. But we test it here to ensure that the constructor of ProgrammingError
    # raises a ProgrammingError. Otherwise the meta-programming above makes no sense.
    from pypara.syntax.content import IndentationContent
    from pypara.domain.content import Content

    ic = IndentationContent(0, Content.empty)
    assert ic.indentation is not None
    assert ic.content is not None
    # On the next line, the indentation is ``None``, which should be impossible. We try it here to check that this
    # case is handled accordingly.
    try:
        ic = IndentationContent(None, Content.empty)
        assert False
    except ProgrammingError:
        assert True


# Generated at 2022-06-14 04:30:56.805178
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test: Test constructor of class ProgrammingError.
    """
    try:
        raise ProgrammingError()
    except Exception as err:
        assert isinstance(err, ProgrammingError)


# Generated at 2022-06-14 04:30:58.700913
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "test")
        raise Exception
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:31:01.770445
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test the constructor of ProgrammingError
    try:
        raise ProgrammingError("Something went wrong")
    except ProgrammingError as e:
        assert e.args == ("Something went wrong",)


# Generated at 2022-06-14 04:31:04.805824
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for the :py:class:`ProgrammingError` class."""
    # pylint: disable=W0612
    with ProgrammingError("Programming error"):
        assert (True)


# Generated at 2022-06-14 04:31:09.446868
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Broken")
    except ProgrammingError as e:
        assert e.args[0] == "Broken"
    try:
        ProgrammingError.passert(False, "")
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:31:11.785501
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    condition = False
    message = "Please check your code."
    try:
        ProgrammingError.passert(condition, message)
        assert False
    except ProgrammingError as e:
        assert str(e) == message


# Generated at 2022-06-14 04:31:20.896988
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("")
    except ProgrammingError as e:
        assert str(e) == ""
    try:
        raise ProgrammingError("", "")
    except ProgrammingError as e:
        assert str(e) == ": "
    try:
        raise ProgrammingError("", "Message")
    except ProgrammingError as e:
        assert str(e) == ": Message"
    try:
        raise ProgrammingError("Caption", "Message")
    except ProgrammingError as e:
        assert str(e) == "Caption: Message"

# Generated at 2022-06-14 04:31:24.761840
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    message = "This is a test message."
    try:
        ProgrammingError(message)
        assert True, "ProgrammingError should not raise errors when the message is provided."
    except Exception as e:
        assert False, "ProgrammingError raised an exception when the message is provided."

# Generated at 2022-06-14 04:31:36.872724
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pyaf.exceptions import ProgrammingError
    try:
        ProgrammingError()
    except:
        assert False
    try:
        ProgrammingError("")
    except:
        assert False
    try:
        ProgrammingError("toto")
    except:
        assert False
    try:
        ProgrammingError.passert(True, "")
    except:
        assert False
    try:
        ProgrammingError.passert(True, "")
    except:
        assert False
    try:
        ProgrammingError.passert(True, "toto")
    except:
        assert False
    try:
        ProgrammingError.passert(False, "")
        assert False
    except:
        pass
    try:
        ProgrammingError.passert(False, "")
        assert False
    except:
        pass

# Generated at 2022-06-14 04:31:39.848633
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Some message.")
    except ProgrammingError as e:
        assert "Some message." == e.args[0]

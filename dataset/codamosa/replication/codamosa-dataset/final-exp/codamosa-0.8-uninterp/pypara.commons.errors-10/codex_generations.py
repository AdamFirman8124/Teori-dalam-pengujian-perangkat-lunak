

# Generated at 2022-06-14 04:23:36.575253
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "check coherence")
        raise AssertionError("assertion error expected")
    except ProgrammingError as e:
        assert e.args == ("check coherence",)

# Generated at 2022-06-14 04:23:39.944052
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(True, "")
    except ProgrammingError:
        assert False
    try:
        ProgrammingError.passert(False, "")
        assert False
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:23:43.724707
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # When we pass a message to the constructor
    # Then the message is returned
    error = ProgrammingError("message")
    assert error.args[0] == "message"


# Generated at 2022-06-14 04:23:45.764848
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    exception: ProgrammingError = ProgrammingError("message")
    assert str(exception) == "message"

# Generated at 2022-06-14 04:23:48.992813
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Mocked error message")
    except ProgrammingError as ex:
        assert ex.args and ex.args[0] == "Mocked error message"

# Generated at 2022-06-14 04:23:51.200002
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:23:52.228761
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(False, "message")

# Generated at 2022-06-14 04:23:54.312111
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, None):
        pass

# Generated at 2022-06-14 04:23:58.496153
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test that an exception can be raised without message
    try:
        ProgrammingError()
    except ProgrammingError:
        pass

    # Test that an exception can be raised with message
    try:
        ProgrammingError("Testing message")
    except ProgrammingError:
        pass



# Generated at 2022-06-14 04:23:59.938177
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError.passert(False, "error message")

###############################################################################

# Generated at 2022-06-14 04:24:01.885415
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    pass

# Generated at 2022-06-14 04:24:04.974998
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)


# Generated at 2022-06-14 04:24:11.909004
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    t = ProgrammingError
    try:
        t()
        assert False
    except Exception as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    try:
        t("My message.")
        assert False
    except Exception as e:
        assert str(e) == "My message."



# Generated at 2022-06-14 04:24:16.410099
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def f():
        ProgrammingError.passert(False, "")
    try:
        f()
    except Exception as e:
        assert isinstance(e, ProgrammingError)



# Generated at 2022-06-14 04:24:18.822653
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises

    with raises(ProgrammingError):
        ProgrammingError.passert(False, "This is an error message.")

# Generated at 2022-06-14 04:24:22.836571
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError.passert(False, "Error message")
    assert "Error message" in str(excinfo.value)

# Generated at 2022-06-14 04:24:25.215715
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except Exception as ex:
        raise AssertionError(ex)


# Generated at 2022-06-14 04:24:28.614090
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Testing")
        raise Exception("ProgrammingError did not raise")
    except ProgrammingError as e:
        assert True

# Generated at 2022-06-14 04:24:31.825922
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Error message")
    except ProgrammingError as e:
        assert "Error message" == e.args[0]


# Generated at 2022-06-14 04:24:34.130948
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("This is the error message."): pass
    with ProgrammingError(): pass


# Generated at 2022-06-14 04:24:39.341851
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:24:42.767859
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert str(e) == "test"



# Generated at 2022-06-14 04:24:46.391731
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Self-test")
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
        assert str(e) == "Self-test"
        pass


# Generated at 2022-06-14 04:24:49.612002
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError as e:
        assert e.args[0] == 'Broken coherence. Check your code against domain logic to fix it.'


# Generated at 2022-06-14 04:24:54.155229
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    message = "message"

    try:
        raise ProgrammingError
    except ProgrammingError as e:
        assert str(e) == ""

    try:
        raise ProgrammingError(message)
    except ProgrammingError as e:
        assert str(e) == message


# Generated at 2022-06-14 04:24:56.019241
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:24:59.506687
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pytest import raises
    with raises(ProgrammingError):
        ProgrammingError()
    with raises(ProgrammingError):
        ProgrammingError("foo")


# Generated at 2022-06-14 04:25:04.131773
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`
    """
    try:
        raise ProgrammingError("Test message")
    except ProgrammingError as e:
        assert str(e) == "Test message"

# Generated at 2022-06-14 04:25:05.399442
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError()


# Generated at 2022-06-14 04:25:09.494334
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Message")
        assert False, "ProgrammingError exception must be raised"
    except ProgrammingError as error:
        assert error.args[0] == "Message"


# Generated at 2022-06-14 04:25:19.007734
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests if instance of class ProgrammingError can be created.
    """
    try:
        raise ProgrammingError("Just a test")
    except ProgrammingError as e:
        assert isinstance(e, ProgrammingError)
    else:
        assert False # pragma: no cover


# Generated at 2022-06-14 04:25:21.965715
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        # We expect an exception here
        ProgrammingError.passert(False, "message")
    except ProgrammingError as e:
        assert str(e) == "message"

# Generated at 2022-06-14 04:25:25.041428
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error_msg = "This is an error"
    exception = ProgrammingError(error_msg)
    assert exception.args[0] == error_msg, exception.args



# Generated at 2022-06-14 04:25:31.311481
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Checks the constructor of class ProgrammingError.

    :return: ``None``.
    """
    # pylint: disable=unused-variable
    try:
        with ProgrammingError.passert(False, "Test message"):
            # Empty statement
            pass
    except ProgrammingError:
        pass
    else:
        assert False, "Should have raised exception"

# Generated at 2022-06-14 04:25:35.994734
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except Exception as e:
        assert isinstance(e, ProgrammingError)
        assert len(e.args) == 0
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:25:39.846119
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError(message="Error creating ProgrammingError")
    except ProgrammingError as e:
        assert(str(e) == "Error creating ProgrammingError")


# Generated at 2022-06-14 04:25:42.519226
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Expected condition has failed.")
    except ProgrammingError as e:
        assert(e.args[0] == "Expected condition has failed.")


# Generated at 2022-06-14 04:25:45.212503
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError().args == ("Broken coherence. Check your code against domain logic to fix it.",)

# Generated at 2022-06-14 04:25:45.988552
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    pass

# Generated at 2022-06-14 04:25:50.252597
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "I expected True.")
        assert False, "It should have failed."
    except ProgrammingError as e:
        assert str(e) == "I expected True."

# Generated at 2022-06-14 04:26:06.947262
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Test message")
        raise AssertionError("ProgrammingError raised an exception. This test case expects that this does not happen")
    except ProgrammingError as e:
        if str(e) != "Test message":
            raise AssertionError("Unexpected message from ProgrammingError constructor: {0}".format(str(e)))



# Generated at 2022-06-14 04:26:12.803904
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A programming error.")
    except ProgrammingError as e:
        assert e.__str__() == "A programming error."
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.__str__() == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:26:20.570251
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition = False, message = "Foo")
    except ProgrammingError as e:
        assert e.args[0] == "Foo"
    try:
        ProgrammingError.passert(condition = False, message = None)
    except ProgrammingError as e:
        assert e.args[0] == "Broken coherence. Check your code against domain logic to fix it."
    try:
        ProgrammingError.passert(condition = True, message = "Foo")
    except ProgrammingError as e:
        assert False, "ProgrammingError.passert should have not raised in this unit test's case."

# Generated at 2022-06-14 04:26:23.997848
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("a/b")
    except ProgrammingError:
        return
    assert False, "ProgrammingError should not be caught"


# Generated at 2022-06-14 04:26:32.846477
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, "Test message"):
        pass

    try:
        with ProgrammingError.passert(False, "Test message"):
            pass
    except ProgrammingError as err:
        assert "Test message" in str(err)
    else:
        raise AssertionError("ProgrammingError expected")

    try:
        with ProgrammingError.passert(False, None):
            pass
    except ProgrammingError as err:
        assert "Broken coherence" in str(err)
    else:
        raise AssertionError("ProgrammingError expected")


# Generated at 2022-06-14 04:26:36.908064
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        error = ProgrammingError("A test")
        assert error.args[0] == "A test"


# Generated at 2022-06-14 04:26:39.129712
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        raise ProgrammingError("Something went wrong.")


# Generated at 2022-06-14 04:26:42.772633
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Dummy Error")
    except ProgrammingError as e:
        assert str(e) == "Dummy Error"
    else:
        assert False


# Generated at 2022-06-14 04:26:44.695798
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, "Test message")

# Generated at 2022-06-14 04:26:49.149868
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, ""):
        pass
    try:
        with ProgrammingError.passert(False, "ERROR"):
            pass
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:27:12.891866
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    exc = ProgrammingError()
    assert exc
    assert str(exc) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:27:15.737947
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "exp")
    except ProgrammingError as pe:
        assert pe.args == ("exp",)


# Generated at 2022-06-14 04:27:17.204757
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert isinstance(ProgrammingError(), ProgrammingError)


# Generated at 2022-06-14 04:27:19.319094
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pypara.test import catch_error
    catch_error(ProgrammingError, lambda: ProgrammingError.passert(False, None))

# Generated at 2022-06-14 04:27:22.865520
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for :py:class:`ProgrammingError`."""
    with pytest.raises(ProgrammingError):
        ProgrammingError(message="Broken coherence. Check your code against domain logic to fix it.")


# Generated at 2022-06-14 04:27:26.774270
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("The message")
    except ProgrammingError as exception:
        assert exception.args[0] == "The message"


# Generated at 2022-06-14 04:27:29.909607
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Act and assert
    with pytest.raises(ProgrammingError) as info:
        raise ProgrammingError("Programming error message")

    assert str(info.value) == "Programming error message"



# Generated at 2022-06-14 04:27:32.537037
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Check your code")
    except ProgrammingError as e:
        assert str(e) == "Check your code"

# Generated at 2022-06-14 04:27:34.911135
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass



# Generated at 2022-06-14 04:27:38.753655
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a test message.")
    except ProgrammingError as e:
        assert str(e) == "This is a test message."
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:28:21.851237
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as exception:
        assert exception.args == tuple()


# Generated at 2022-06-14 04:28:27.675086
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Error")
    except ProgrammingError as e:
        assert e.__cause__ is None
        assert e.args[0] == "Error"
        assert e.__class__.__name__ == "ProgrammingError"
        assert e.__class__.__qualname__ == "ProgrammingError"
    else:
        raise Exception("Missing exception")


# Generated at 2022-06-14 04:28:36.438091
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # No message
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e == ProgrammingError()
        assert e.args == ProgrammingError().args
        assert e.args == ('Broken coherence. Check your code against domain logic to fix it.',)
        assert str(e) == e.args[0]
        assert repr(e) == ''.join([type(e).__name__, '("', ProgrammingError().args[0], '")'])
    # With message
    try:
        raise ProgrammingError("something strange has happened")
    except ProgrammingError as e:
        assert e == ProgrammingError("something strange has happened")
        assert e.args == ProgrammingError("something strange has happened").args
        assert e.args == ("something strange has happened",)
        assert str(e) == e.args[0]


# Generated at 2022-06-14 04:28:43.739231
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError, match="Broken coherence. Check your code against domain logic to fix it."):
        ProgrammingError.passert(False, None)
    with pytest.raises(ProgrammingError, match="My message"):
        ProgrammingError.passert(False, "My message")
    ProgrammingError.passert(True, None)
    ProgrammingError.passert(True, "My message")

# Generated at 2022-06-14 04:28:56.778415
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # GIVEN a condition which is valid for the programmer's expectation and an error message
    condition_true = True
    message = "Something failed in my code"
    # WHEN creating a ProgrammingError
    # THEN no exception should be raised
    ProgrammingError.passert(condition_true, message)

    # GIVEN a condition which is not valid for the programmer's expectation and an error message
    condition_false = False
    message = "Something failed in my code"
    # WHEN creating a ProgrammingError
    # THEN no exception should be raised
    try:
        ProgrammingError.passert(condition_false, message)
        raise Exception("Should not reach here")
    except ProgrammingError:
        # It is OK to reach here
        pass

    # GIVEN a condition which is not valid for the programmer's expectation and no error message
    condition_false = False


# Generated at 2022-06-14 04:28:59.323764
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError(message="Test")
    except ProgrammingError as e:
        assert str(e) == "Test"

# Generated at 2022-06-14 04:29:01.648740
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError("Message")
    assert error.args == ("Message",)



# Generated at 2022-06-14 04:29:14.238811
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from unittest import TestCase, main
    from unittest.mock import patch, call

    class ProgrammingErrorTestCase(TestCase):
        def test_raises_with_no_message(self):
            with self.assertRaises(ProgrammingError):
                ProgrammingError.passert(False, None)

        def test_raises_with_message(self):
            with self.assertRaises(ProgrammingError) as cm:
                ProgrammingError.passert(False, "TestMessage")
            exception: ProgrammingError = cm.exception
            self.assertEqual(exception.args, ("TestMessage",))

        def test_does_nothing(self):
            m = patch("ProgrammingError.assert", side_effect=ProgrammingError.passert)

# Generated at 2022-06-14 04:29:18.232305
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Test constructor.
    try:
        raise ProgrammingError(mesg="My error")
    except Exception as e:
        assert(isinstance(e, ProgrammingError))
        assert(str(e) == "My error")


# Generated at 2022-06-14 04:29:25.565747
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # When leaving the message to its default value, it should not raise any exception.
    ProgrammingError.passert(True, None)
    # When passing a message as false state, it should raise the corresponding exception.
    try:
        ProgrammingError.passert(False, "This is an error")
        # We should not reach this line
        assert False
    except ProgrammingError as pe:
        assert str(pe) == "This is an error"

# Generated at 2022-06-14 04:31:09.358354
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # GIVEN
    msg = "Test case failed!"

    # WHEN
    try:
        # Error message not provided
        ProgrammingError.passert(False, None)
        raise RuntimeError("Test case did not raise any exception.")
    except ProgrammingError:
        pass

    # WHEN
    try:
        # Error message provided
        ProgrammingError.passert(False, msg)
        raise RuntimeError("Test case did not raise any exception.")
    except ProgrammingError as e:
        assert str(e) == msg
        pass

# Generated at 2022-06-14 04:31:13.047425
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # GIVEN
    testcase = {True: "Expected error message", False: None}
    for condition, message in testcase.items():
        # WHEN
        try:
            ProgrammingError.passert(condition, message)
        except ProgrammingError as error:
            # THEN
            assert str(error) == message or "Broken coherence. Check your code against domain logic to fix it."
        else:
            assert condition == True


# Generated at 2022-06-14 04:31:19.753122
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # GIVEN
    error: ProgrammingError
    message: str

    # WHEN
    error = ProgrammingError("This is a programming error message")

    # THEN
    assert error is not None
    assert error.args[0] == "This is a programming error message"

    # WHEN
    error = ProgrammingError()

    # THEN
    assert error is not None
    assert error.args[0] == "No message"

# Generated at 2022-06-14 04:31:21.670374
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of class :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:31:29.904244
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():   # pylint: disable=missing-docstring
    from unittest import TestCase
    class TestProgrammingError(TestCase):
        """
        Unit test case to verify the proper creation of the exception.
        """
        def test_message(self):
            # When no message is provided, the default message is returned
            exc = ProgrammingError()
            self.assertEqual(exc.args[0], "Broken coherence. Check your code against domain logic to fix it.")
            # When a message is provided, the provided message is returned
            exc = ProgrammingError("My custom message")
            self.assertEqual(exc.args[0], "My custom message")
    TestProgrammingError('test_message').test_message()


# Generated at 2022-06-14 04:31:37.477652
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    except Exception as e:
        assert False, "Unexpected exception: %s" % str(e)
    try:
        raise ProgrammingError("A programming error")
    except ProgrammingError as e:
        assert str(e) == "A programming error", "Unexpected exception message: %s" % str(e)
    except Exception as e:
        assert False, "Unexpected exception: %s" % str(e)


# Generated at 2022-06-14 04:31:40.461777
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError(message="Error")
    except ProgrammingError as error:
        assert str(error) == "Error"


# Generated at 2022-06-14 04:31:44.353405
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(True, "Should not be raised"):
        pass

    with ProgrammingError.passert(False, "SHOULD BE RAISED"):
        pass

# Generated at 2022-06-14 04:31:47.394246
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError:
        assert True
    except Exception:
        assert False


# Generated at 2022-06-14 04:31:48.456570
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError("Just a message") is not None

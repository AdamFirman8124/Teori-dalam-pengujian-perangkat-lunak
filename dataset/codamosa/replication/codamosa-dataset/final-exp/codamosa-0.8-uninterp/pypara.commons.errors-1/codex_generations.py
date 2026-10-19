

# Generated at 2022-06-14 04:23:31.522953
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    pass

# Generated at 2022-06-14 04:23:36.687990
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Some message")
    except ProgrammingError as e:
        assert e.args[0] == "Some message"
    else:
        assert False, "Expected exception not raised"


# Generated at 2022-06-14 04:23:40.880559
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor of the class :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("This is a test exception.")
    except ProgrammingError as e:
        assert str(e) == "This is a test exception."


# Generated at 2022-06-14 04:23:45.859376
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test: :py:meth:`file_utils.ProgrammingError.__init__`.
    """
    error = ProgrammingError()
    assert isinstance(error, ProgrammingError)
    assert isinstance(error, Exception)
    assert isinstance(error, BaseException)


# Generated at 2022-06-14 04:23:49.961599
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Tests the constructor of class :py:class:`ProgrammingError`."""
    try:
        raise ProgrammingError("My message")
    except ProgrammingError as e:
        assert str(e) == "My message"


# Generated at 2022-06-14 04:23:53.016656
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is a message")
    except ProgrammingError as e:
        assert str(e) == "This is a message"


# Generated at 2022-06-14 04:23:58.021020
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest

    with pytest.raises(ProgrammingError, match="Broken coherence. Check your code against domain logic to fix it."):
        ProgrammingError.passert(False, None)

    with pytest.raises(ProgrammingError, match="Something is badly wrong"):
        ProgrammingError.passert(False, "Something is badly wrong")

# Generated at 2022-06-14 04:23:59.897409
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except Exception:
        assert False
    else:
        assert True

# Generated at 2022-06-14 04:24:06.629839
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Unit test for the constructor of :py:class:`ProgrammingError`.
    """

    def _check_raise(message):
        try:
            raise ProgrammingError(message)
        except ProgrammingError as e:
            assert message == str(e)

    _check_raise("Test message 1")
    _check_raise("")
    _check_raise(None)


# Generated at 2022-06-14 04:24:09.031189
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:24:13.995783
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Given
    def foo() -> None:
        # When
        raise ProgrammingError("This is a programming error!")
    # Then
    assert foo is not None


# Generated at 2022-06-14 04:24:15.617781
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError):
        raise ProgrammingError()


# Generated at 2022-06-14 04:24:18.388151
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    import pytest
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(condition=False, message="This is a test")

# Generated at 2022-06-14 04:24:21.463498
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests :py:class:`ProgrammingError`.
    """
    try:
        ProgrammingError.passert(False, "Always fails")
    except ProgrammingError:
        pass
    else:
        raise AssertionError("ProgrammingError instance not raised")

# Generated at 2022-06-14 04:24:24.525046
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for class ProgrammingError."""
    try:
        raise ProgrammingError
    except ProgrammingError:
        assert True


# Generated at 2022-06-14 04:24:28.936332
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Given
    msg = "This is an error message"

    # When
    try:
        raise ProgrammingError(msg)
    except ProgrammingError as e:
        # Then
        assert e.args == (msg,)


# Generated at 2022-06-14 04:24:35.749125
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message="A programmed error has occurred")
        assert False
    except ProgrammingError as e:
        assert str(e) == "A programmed error has occurred"
    try:
        ProgrammingError.passert(condition=False, message=None)
        assert False
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:24:39.871590
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Arrange
    message = "A ProgrammingError message"

    # Act and assert
    try:
        raise ProgrammingError(message)
    except ProgrammingError as err:
        assert str(err) == message


# Generated at 2022-06-14 04:24:43.269254
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test exception")
    except Exception as err:
        assert str(err) == "Test exception"

# Generated at 2022-06-14 04:24:47.350625
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError:
        pass
    except Exception as ex:
        assert False, "Constructor of ProgrammingError has failed"

#  Unit test for passert of class ProgrammingError

# Generated at 2022-06-14 04:24:53.024405
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    try:
        raise ProgrammingError("test")
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:24:56.019022
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("This is an error.")
    except ProgrammingError as ex:
        assert ex.args[0] == "This is an error."


# Generated at 2022-06-14 04:24:59.507020
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:25:03.185635
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError
    exception = ProgrammingError("foo")
    assert isinstance(exception, ProgrammingError)
    assert str(exception) == "foo"


# Generated at 2022-06-14 04:25:08.886000
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def exception_helper(exception_class: type, *args, **kwargs):
        try:
            raise exception_class(*args, **kwargs)
        except Exception as e:
            assert e.args == args or e.args == kwargs['message']

    exception_helper(ProgrammingError)
    exception_helper(ProgrammingError, 'message')
    exception_helper(ProgrammingError, message='message')


# Generated at 2022-06-14 04:25:11.340887
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    error = ProgrammingError() # Should not fail
    del error

# Generated at 2022-06-14 04:25:23.634941
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    def raisesProgrammingError():
        try:
            raise ProgrammingError("Test exception")
        except ProgrammingError as e:
            assert(str(e) == "Test exception")

    def raisesNothing():
        ProgrammingError.passert(True, "Test exception")

    def raisesProgrammingError2():
        try:
            ProgrammingError.passert(False, "Test exception")
        except ProgrammingError as e:
            assert(str(e) == "Test exception")
        else:
            raise AssertionError("An exception was expected")

    def raisesProgrammingError3():
        try:
            ProgrammingError.passert(False, None)
        except ProgrammingError as e:
            assert(str(e) == "Broken coherence. Check your code against domain logic to fix it.")

# Generated at 2022-06-14 04:25:27.246754
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from nose.tools import assert_raises

    exc_msg = "This is a test error message."
    assert_raises(ProgrammingError, ProgrammingError, exc_msg)


# Generated at 2022-06-14 04:25:30.491966
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        pass
    except Exception:
        raise AssertionError("ProgrammingError() raised something which is not ProgrammingError")

# Generated at 2022-06-14 04:25:33.502092
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Intended error message")
    except ProgrammingError as error:
        assert str(error) == "Intended error message"


# Generated at 2022-06-14 04:25:45.122836
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("A programming error")
    except ProgrammingError:
        pass
    ProgrammingError.passert(True, "A programming error")
    try:
        ProgrammingError.passert(False, "Cannot check this")
        assert False
    except ProgrammingError:
        pass
    ProgrammingError.passert(True, None)
    try:
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:25:50.378559
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """Unit test for constructor of class ``ProgrammingError``."""
    # Arrange
    expected_message = "The message."
    # Act
    error = ProgrammingError(message=expected_message)
    # Assert
    assert str(error) == expected_message


# Generated at 2022-06-14 04:25:54.248931
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError("Check your code against domain logic to fix it.")
    except Exception as e:
        assert str(e) == "Check your code against domain logic to fix it."


# Generated at 2022-06-14 04:26:05.861496
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # test 1
    try:
        raise ProgrammingError("Simulated programming error")
    except ProgrammingError as e:
        assert str(e) == "Simulated programming error"
    # test 2
    assert ProgrammingError.passert(True, "Simulated programming error") is None
    try:
        ProgrammingError.passert(False, "Simulated programming error")
        raise AssertionError("The previous statement should have raised a ProgrammingError")
    except ProgrammingError as e:
        assert str(e) == "Simulated programming error"
    # test 3
    try:
        ProgrammingError.passert(False, None)
        raise AssertionError("The previous statement should have raised a ProgrammingError")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:26:10.210117
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError(message="foo")
        assert False, "Programming error should have been raised"
    except ProgrammingError as e:
        assert "foo" in str(e)


# Generated at 2022-06-14 04:26:13.431760
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, 'Test')
        assert False
    except ProgrammingError as e:
        assert str(e) == 'Test'


# Generated at 2022-06-14 04:26:19.775458
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Constructor has no arguments
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass
    except Exception as e:
        assert False, "Unexpected error caught: [{}]".format(e)

    # Constructor accepts a message
    try:
        raise ProgrammingError("Custom error")
    except ProgrammingError:
        pass
    except Exception as e:
        assert False, "Unexpected error caught: [{}]".format(e)


# Generated at 2022-06-14 04:26:22.651225
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("test")
    except ProgrammingError as e:
        assert(str(e) == "test")


# Generated at 2022-06-14 04:26:24.454773
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:26:32.591378
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pypara.utilities.exc import ProgrammingError

    try:
        ProgrammingError.passert(True, "")
        assert True
    except ProgrammingError as err:
        assert False, "ProgrammingError exception unexpectedly thrown. Raised exception message was: {}".format(err)

    try:
        ProgrammingError.passert(False, "")
        assert False, "ProgrammingError exception not raised"
    except ProgrammingError as err:
        assert True
        assert "Broken coherence. Check your code against domain logic to fix it." in str(err)

# Generated at 2022-06-14 04:26:46.073233
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # Arrange
    message = "This is a message"
    # Act / Assert
    try:
        raise ProgrammingError(message)
    except ProgrammingError as e:
        # Assert
        assert e.args[0] == message


# Generated at 2022-06-14 04:26:54.595217
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Condition is False")
        assert False, "ProgrammingError.passert(False, 'Condition is False') should raise an exception"
    except ProgrammingError as err:
        assert str(err) == "Condition is False", "ProgrammingError.passert(False, 'Condition is False') raised " \
                           + "an exception with the wrong message"
    except:
        assert False, "ProgrammingError.passert(False, 'Condition is False') raised an exception of wrong type"
    else:
        assert True, "ProgrammingError.passert(True, 'Condition is False') should not raise any exception"

# Generated at 2022-06-14 04:26:59.617337
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    catch = False

    try:
        ProgrammingError.passert(False, "test message")
    except ProgrammingError as e:
        assert str(e) == "test message"
        catch = True

    assert catch

    ProgrammingError.passert(True, "test message")

# Generated at 2022-06-14 04:27:06.509575
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Tests the constructor for class :py:class:`ProgrammingError`.
    """
    try:
        raise ProgrammingError("test message")
    except ProgrammingError as err:
        assert err.args[0] == "test message"

    try:
        raise ProgrammingError("")
    except ProgrammingError as err:
        assert err.args[0] == "Broken coherence. Check your code against domain logic to fix it."



# Generated at 2022-06-14 04:27:12.025998
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Verifies that :py:class:`ProgrammingError` correctly creates exceptions.
    """
    pe = ProgrammingError("Exception message")
    assert isinstance(pe, Exception)
    assert pe.args[0] == "Exception message"



# Generated at 2022-06-14 04:27:15.790910
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        raise AssertionError()


# Generated at 2022-06-14 04:27:20.015115
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert "Broken coherence. Check your code against domain logic to fix it." == e.args[0]
    except Exception as e:
        assert False, "Unexpected exception: {0}".format(e)

# Generated at 2022-06-14 04:27:23.089997
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError(ProgrammingError.__doc__)
    except ProgrammingError:
        ProgrammingError.passert(True, ProgrammingError.__doc__)
    else:
        assert False, "Programming error not raised"


# Generated at 2022-06-14 04:27:26.526925
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("error")
    except ProgrammingError as e:
        assert(str(e) == "error")

# Generated at 2022-06-14 04:27:29.744542
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Oops")
    except ProgrammingError as p:
        assert p.args[0] == "Oops"


# Generated at 2022-06-14 04:27:51.173526
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError(message="Test")


# Generated at 2022-06-14 04:27:54.718485
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError as e:
        assert e.message == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:28:01.363447
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # pylint: disable=unused-argument

    # Constructor is tested through :py:meth:`ProgrammingError.passert()`
    def _unused(parameter):
        pass

    # No exception is expected
    ProgrammingError.passert(True, "No exception expected")

    # An exception *is* expected
    try:
        ProgrammingError.passert(False, "Exception expected")
        raise AssertionError("Exception expected")
    except ProgrammingError:
        pass

# Generated at 2022-06-14 04:28:05.562685
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Error!!")
    except ProgrammingError as e:
        assert "Error!!" == str(e), "Message of the exception is not correct"
    else:
        raise AssertionError("Exception was not raised!")

# Generated at 2022-06-14 04:28:08.648475
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        pass


# Generated at 2022-06-14 04:28:10.932567
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pypara.error import ProgrammingError
    ProgrammingError()
    ProgrammingError("")
    ProgrammingError("a")


# Generated at 2022-06-14 04:28:12.898274
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    assert ProgrammingError("ERROR")


# Generated at 2022-06-14 04:28:17.729584
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        error = ProgrammingError("test_message")
    except Exception as error:
        pass

    assert isinstance(error, ProgrammingError)
    assert isinstance(error, Exception)
    assert error.args[0] == "test_message"


# Generated at 2022-06-14 04:28:20.904350
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Exception message.")
    except Exception as e:
        assert str(e) == "Exception message."


# Generated at 2022-06-14 04:28:24.611818
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    condition = False
    message = "This is a test"
    try:
        ProgrammingError.passert(condition, message)
    except ProgrammingError as err:
        assert err.args[0] == message


# Generated at 2022-06-14 04:29:08.938400
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError.passert(False, ""):
        pass

# Generated at 2022-06-14 04:29:12.934198
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
        ProgrammingError.passert(False, "Test!")
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        assert False

# Generated at 2022-06-14 04:29:25.229625
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError()
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."
    else:
        raise AssertionError("ProgrammingError() did not raise a ProgrammingError exception")

    try:
        ProgrammingError("Para programming error.")
    except ProgrammingError as e:
        assert str(e) == "Para programming error."
    else:
        raise AssertionError("ProgrammingError('Para programming error.') did not raise a ProgrammingError exception")

    try:
        ProgrammingError.passert(False, None)
    except ProgrammingError as e:
        assert str(e) == "Broken coherence. Check your code against domain logic to fix it."

# Generated at 2022-06-14 04:29:27.986969
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Test message")
    except ProgrammingError as exc:
        assert str(exc) == "Test message"


# Generated at 2022-06-14 04:29:30.364196
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError()
    except ProgrammingError:
        return True
    return False


# Generated at 2022-06-14 04:29:33.251137
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with raises(ProgrammingError, match="Broken coherence"):
        ProgrammingError.passert(False, "Broken coherence. Check your code against domain logic to fix it.")

# Generated at 2022-06-14 04:29:34.468180
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    ProgrammingError('')


# Generated at 2022-06-14 04:29:36.771938
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    p = ProgrammingError("This is the error message.")
    assert p.message == "This is the error message."


# Generated at 2022-06-14 04:29:40.906461
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    """
    Test constructor of class ProgrammingError
    """
    # Intialization Test
    try:
        ProgrammingError("Test")
    except ProgrammingError as instance:
        assert isinstance(instance, ProgrammingError)
    else:
        assert False, "Did not raise an exception like expected"


# Generated at 2022-06-14 04:29:43.302651
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "Test message")
    except ProgrammingError as e:
        assert str(e) == "Test message"


# Generated at 2022-06-14 04:31:27.029884
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("programming error occurred")
    except ProgrammingError as e:
        assert e.args[0] == "programming error occurred"

# Generated at 2022-06-14 04:31:34.367567
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    from pyassert import assert_that

    # ARRANGE
    condition = False
    message = "message"

    # ACT
    actual_exception = None
    try:
        ProgrammingError.passert(condition, message)
    except ProgrammingError as e:
        actual_exception = e
    except Exception as e:
        actual_exception = e

    # ASSERT
    assert_that(actual_exception).is_not_none()


# Generated at 2022-06-14 04:31:38.754338
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    context = {}
    try:
        ProgrammingError.passert(False, "Test")
    except ProgrammingError as e:
        context["error"] = e
    assert "error" in context
    assert context["error"].args == ("Test",)


# Generated at 2022-06-14 04:31:41.493975
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    msg = "Testing ProgrammingError"
    try:
        raise ProgrammingError(msg)
    except ProgrammingError as err:
        assert str(err) == msg



# Generated at 2022-06-14 04:31:45.699897
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        raise ProgrammingError("Error message")
    except ProgrammingError as e:
        assert isinstance(e, Exception) and isinstance(e, ProgrammingError)



# Generated at 2022-06-14 04:31:49.221965
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(False, "")
        ProgrammingError.passert(False, None)
        assert False
    except ProgrammingError:
        assert True
    assert False


# Generated at 2022-06-14 04:31:52.552394
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with pytest.raises(ProgrammingError):
        ProgrammingError.passert(False, 'Broken coherence. Check your code against domain logic to fix it.')

# Generated at 2022-06-14 04:31:54.466858
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    with ProgrammingError("It's broken."):
        raise ProgrammingError("It's broken.")


# Generated at 2022-06-14 04:31:58.201698
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    try:
        ProgrammingError.passert(condition=False, message="Something goes wrong.")
    except ProgrammingError:
        import traceback
        print(traceback.format_exc())
        assert True
    else:
        assert False


# Generated at 2022-06-14 04:32:01.042277
# Unit test for constructor of class ProgrammingError
def test_ProgrammingError():
    # We are testing the construction of the exception
    # This is just a placeholder to show that we are testing something
    ProgrammingError("Just testing...")
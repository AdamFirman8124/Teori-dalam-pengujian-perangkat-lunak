

# Generated at 2022-06-13 04:31:05.639184
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('uh oh')
    except ValueError:
        e = get_exception()
    assert e.args[0] == 'uh oh'


# Generated at 2022-06-13 04:31:07.895151
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('oops')
    except ValueError:
        e = get_exception()
        assert str(e) == 'oops'

# Generated at 2022-06-13 04:31:10.835496
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("Test Exception")
    except ValueError:
        e = get_exception()
        assert "Test Exception" == str(e)

# Generated at 2022-06-13 04:31:13.421592
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("I'm an error")
    except:
        e = get_exception()
        assert isinstance(e, RuntimeError)
        assert str(e) == "I'm an error"

# Generated at 2022-06-13 04:31:15.196319
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('TEST')
    except Exception:
        assert 'TEST' in str(get_exception())


# Generated at 2022-06-13 04:31:20.415731
# Unit test for function get_exception
def test_get_exception():
    # Normal case
    try:
        raise ValueError("Invalid value for name")
    except Exception:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert 'name' in text_type(e)

    # No exception raised
    try:
        pass
    except Exception:
        e = get_exception()
        assert e is None

    # Nested exceptions
    try:
        try:
            raise ValueError("Invalid value for name")
        except Exception:
            raise IndexError("Index into the list failed")
    except Exception:
        e = get_exception()
        assert isinstance(e, IndexError)
        assert 'list' in text_type(e)

# Generated at 2022-06-13 04:31:25.211180
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test_get_exception')
    except:
        e = get_exception()
        assert e.args == ('test_get_exception',), 'get_exception returned wrong exception'



# Generated at 2022-06-13 04:31:28.896495
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('generic error')
    except RuntimeError:
        exc = get_exception()
    assert isinstance(exc, RuntimeError)
    assert str(exc) == 'generic error'
    assert getattr(exc, 'returncode', None) is None

# Generated at 2022-06-13 04:31:34.060433
# Unit test for function get_exception
def test_get_exception():
    e = Exception("This is an exception")
    try:
        raise e
    except Exception:
        got_exception = get_exception()

    assert e == got_exception, "get_exception didn't give us the exception we just raised!"

# Generated at 2022-06-13 04:31:38.721381
# Unit test for function get_exception
def test_get_exception():
    class FakeException(Exception):
        pass
    try:
        raise FakeException
    except Exception:
        ex = get_exception()
    assert type(ex) == FakeException, ('Expected %s, not %s' % (FakeException, type(ex)))

# Generated at 2022-06-13 04:31:58.630652
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        e = get_exception()
    assert isinstance(e, Exception)
    assert isinstance(e, e.__class__)



# Generated at 2022-06-13 04:32:03.434372
# Unit test for function get_exception
def test_get_exception():
    class TestException(Exception):
        pass
    try:
        raise TestException('Somthing bad happened')
    except TestException:
        exc = get_exception()
    exception_string = str(exc)
    assert exception_string.startswith("Somthing bad happened")

# Generated at 2022-06-13 04:32:04.362640
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except Exception:
        assert get_exception()

# Generated at 2022-06-13 04:32:06.043912
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('message')
    except Exception:
        exc = get_exception()
        assert exc.message == 'message'

# Generated at 2022-06-13 04:32:11.578050
# Unit test for function get_exception
def test_get_exception():
    try:
        __not_exists__
    except NameError:
        e = get_exception()
        if type(e) != NameError:
            raise AssertionError('Unable to get the exception object')
        if not isinstance(e, NameError):
            raise AssertionError('Unable to get the exception object')
    else:
        raise AssertionError('get_exception failed')

# Generated at 2022-06-13 04:32:15.977474
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('This is a test')
    except ValueError:
        e = get_exception()
    else:
        assert False, "This should never be reached"

    assert e.args[0] == 'This is a test'

# Generated at 2022-06-13 04:32:19.468041
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("This is an exception")
    except ValueError:
        e = get_exception()

    assert str(e) == 'This is an exception'


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 04:32:28.534071
# Unit test for function get_exception
def test_get_exception():
    """
    Test get_exception() works
    """
    def raise_and_get_exception():
        try:
            raise Exception('Test exception')
        except Exception:
            return get_exception()

    def raise_and_get_exception_from_exec():
        try:
            raise Exception('Test exception')
        except Exception:
            return sys.exc_info()[1]

    e = raise_and_get_exception()
    assert e.args[0] == 'Test exception'

    e = raise_and_get_exception_from_exec()
    assert e.args[0] == 'Test exception'

# Generated at 2022-06-13 04:32:32.005489
# Unit test for function get_exception
def test_get_exception():
    '''
    Ensure our method works properly.
    '''
    try:
        raise ValueError
    except:
        found = get_exception()

    assert isinstance(found, ValueError)

# Generated at 2022-06-13 04:32:34.845487
# Unit test for function get_exception

# Generated at 2022-06-13 04:32:55.717014
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass
    try:
        raise MyException
    except:
        e = get_exception()
        assert isinstance(e, MyException)
        assert str(e)  # Make sure exception is not empty.


# Generated at 2022-06-13 04:32:58.938625
# Unit test for function get_exception
def test_get_exception():
    import pytest
    try:
        literal_eval('a')
    except NameError:
        e = get_exception()
    assert isinstance(e, NameError)


# Generated at 2022-06-13 04:33:02.668324
# Unit test for function get_exception

# Generated at 2022-06-13 04:33:05.002957
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('testing')
    except:
        exception = get_exception()
    assert str(exception) == 'testing'


# Generated at 2022-06-13 04:33:07.791444
# Unit test for function get_exception
def test_get_exception():
    """Test for the get_exception function"""
    try:
        raise RuntimeError('my exception')
    except RuntimeError:
        exc = get_exception()
        assert str(exc) == 'my exception'

# Generated at 2022-06-13 04:33:09.981027
# Unit test for function get_exception
def test_get_exception():
    class TestException(Exception):
        pass
    try:
        raise TestException("foo")
    except TestException as e:
        assert id(e) == id(get_exception())

# Generated at 2022-06-13 04:33:12.554036
# Unit test for function get_exception
def test_get_exception():
    """Test that get_exception() works like except Exception, e:"""
    # pylint: disable=bare-except, unused-variable
    try:
        raise RuntimeError("testing")
    except:
        e = get_exception()
    assert isinstance(e, RuntimeError)
    assert "testing" in str(e)



# Generated at 2022-06-13 04:33:13.798665
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()

    assert e.args[0] == 'foo'

# Generated at 2022-06-13 04:33:18.152882
# Unit test for function get_exception
def test_get_exception():
    """A simple unit test for get_exception that just verifies that it
    can get the exception and that no exception occurs in doing so.

    If a real exception occurs while running this test then it's likely that
    get_exception is broken.  The unit test is mainly to verify that the
    test suites will run properly.

    .. todo::
        We need to find a way to test that get_exception gets the correct
        exception.

    .. note::
        This is an "internal" function.  We need to make sure that it
        doesn't get excluded when the tests are run.
    """
    try:
        # Python 3.x (namespace)
        raise RuntimeError('Unit test for get_exception')
    except RuntimeError as e:
        exception = get_exception()
    assert exception is e


# Generated at 2022-06-13 04:33:22.219278
# Unit test for function get_exception
def test_get_exception():
    """
    >>> test_get_exception()
    100
    """
    try:
        raise RuntimeError(100)
    except Exception:
        e = get_exception()
        return e.args[0]

# Generated at 2022-06-13 04:34:00.398459
# Unit test for function get_exception
def test_get_exception():
    import pytest  # pylint:disable=import-error
    # Generate a TestException so we don't have any unittest or pytest
    # internal stuff in the exception.
    class TestException(Exception):
        pass

    try:
        raise TestException('Human readable error message')  # pylint: disable=undefined-variable
    except (TestException, Exception):
        e = get_exception()
    assert e.__class__ == TestException
    assert 'Human readable error message' in str(e)



# Generated at 2022-06-13 04:34:04.213403
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Test get_exception')
    except Exception:
        e = get_exception()
        assert isinstance(e, ValueError) and str(e) == 'Test get_exception'


# Generated at 2022-06-13 04:34:06.991299
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        raise RuntimeError("Test Exception")
    try:
        raise_exception()
    except:  # noqa
        assert get_exception()


# Generated at 2022-06-13 04:34:09.130544
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Some error')
    except Exception:
        e = get_exception()
    assert(str(e) == 'Some error')

# Generated at 2022-06-13 04:34:12.296760
# Unit test for function get_exception
def test_get_exception():
    """Test the get_exception function.

    Simplest test is to make sure that a bare except doesn't fail

    >>> try:
    ...     a = 1/0
    ... except:
    ...     e = get_exception()

    TODO: Write code that actually verifies this worked
    """
    pass


# Generated at 2022-06-13 04:34:15.978501
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("This is a test exception")
    except:
        exc = get_exception()
        assert exc.__class__ == RuntimeError
        assert str(exc) == "This is a test exception"

# Generated at 2022-06-13 04:34:21.373291
# Unit test for function get_exception
def test_get_exception():  # pragma: no cover
    def func1():
        try:
            raise ValueError('whatever')
        except Exception:
            e = get_exception()
            print('The exception from get_exception: %s' % e)
            print('The class of the exception from get_exception: %s' % e.__class__)
    func1()


# Generated at 2022-06-13 04:34:23.736713
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except:
        e = get_exception()
        assert type(e) == type(Exception())

# Generated at 2022-06-13 04:34:27.376773
# Unit test for function get_exception
def test_get_exception():
    def exception_raiser():
        raise Exception("An exception")

    try:
        exception_raiser()
    except Exception:
        assert get_exception() is not None
        assert isinstance(get_exception(), Exception)
        assert get_exception().args[0] == "An exception"

# Generated at 2022-06-13 04:34:30.722261
# Unit test for function get_exception
def test_get_exception():
    """Ensure that get_exception() works"""
    try:
        raise RuntimeError('test')
    except Exception as e:
        assert get_exception() is e # noqa: F821

# Generated at 2022-06-13 04:35:36.145032
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except Exception:
        assert get_exception() is not None


# Generated at 2022-06-13 04:35:38.673192
# Unit test for function get_exception
def test_get_exception():
    try:
        x = 1/0
    except Exception:
        e = get_exception()
        assert type(e) is ZeroDivisionError
        assert str(e) == "integer division or modulo by zero"
    else:
        assert False, "Did not raise exception"

# Generated at 2022-06-13 04:35:41.950118
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except ValueError:
        e = get_exception()
    assert str(e) == 'foo'

    try:
        raise TypeError('bar')
    except Exception:
        e = get_exception()
    assert str(e) == 'bar'

# Generated at 2022-06-13 04:35:44.257923
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("Test exception")
    except Exception:
        exc = get_exception()
    assert exc.args[0] == "Test exception"
    assert isinstance(exc, ValueError)

# Generated at 2022-06-13 04:35:46.311724
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except ValueError as e:
        assert(e is get_exception())

# Generated at 2022-06-13 04:35:47.967497
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        e = get_exception()
    assert isinstance(e, Exception)


# Generated at 2022-06-13 04:35:51.671704
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('This is a test exception!')
    except:
        exception = get_exception()
    assert exception.args == ('This is a test exception!',)

# Generated at 2022-06-13 04:35:54.294648
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except ValueError:
        e = get_exception()
    assert isinstance(e, ValueError)


# Generated at 2022-06-13 04:35:57.305763
# Unit test for function get_exception
def test_get_exception():
    try:
        raise NameError('foo')
    except NameError:
        exc = get_exception()

    assert exc.__class__.__name__ == 'NameError'
    assert exc.args[0] == 'foo'

# Generated at 2022-06-13 04:35:59.816166
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception as e:
        assert e is get_exception()
    else:
        raise AssertionError('Error: Exception not raised')


# Generated at 2022-06-13 04:38:30.288259
# Unit test for function get_exception
def test_get_exception():
    def raises_exception():
        try:
            raise RuntimeError()
        except Exception:
            return get_exception()
    e = raises_exception()
    assert isinstance(e, Exception)

# Generated at 2022-06-13 04:38:32.978486
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Inner exception')
    except:
        try:
            raise Exception('Outer exception')
        except:
            exc = get_exception()
    assert str(exc) == 'Outer exception'



# Generated at 2022-06-13 04:38:34.929066
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("test")
    except Exception:
        ex = get_exception()

    assert type(ex) == ValueError
    assert str(ex) == "test"


# Generated at 2022-06-13 04:38:36.822972
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except Exception:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert e.args == ('foo',)

# Generated at 2022-06-13 04:38:38.800388
# Unit test for function get_exception
def test_get_exception():
    import exceptions
    try:
        raise ValueError('unit test raise')
    except exceptions.Exception:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert str(e) == 'unit test raise'



# Generated at 2022-06-13 04:38:46.501031
# Unit test for function get_exception
def test_get_exception():
    '''
    This function should return the current exception.  It is usually
    called by an except block::

        try:
            raise Exception("Test exception")
        except Exception:
            e = get_exception()
            assert isinstance(e, Exception)
            assert str(e) == "Test exception"
    '''
    try:
        raise Exception("Test exception")
    except:
        e = get_exception()
        assert isinstance(e, Exception)
        assert str(e) == "Test exception"

# Generated at 2022-06-13 04:38:50.199711
# Unit test for function get_exception
def test_get_exception():

    class TestException(Exception):
        pass

    try:
        raise TestException('Test exception message')
    except TestException:
        e = get_exception()

    assert isinstance(e, TestException)
    assert str(e) == 'Test exception message'

# vim: set expandtab shiftwidth=4 tabstop=4:

# Generated at 2022-06-13 04:38:54.886691
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        e = get_exception()
    except:  # pylint: disable=bare-except # noqa F841
        assert False, 'Failed to get the exception'
    if not e:
        assert False, 'Failed to get the exception'

# Generated at 2022-06-13 04:39:04.340635
# Unit test for function get_exception
def test_get_exception():
    import random
    import string
    import time

    start_time = time.time()
    while time.time() - start_time < 10:
        try:
            raise RuntimeError(''.join(random.choice(string.letters) for i in xrange(random.randint(0, 100))))
        except Exception:
            # pylint: disable=broad-except
            e = get_exception()
            if not isinstance(e, RuntimeError):
                raise AssertionError('Expected a RuntimeError to be raised')
            try:
                raise AssertionError('Expected a RuntimeError to be raised')
            except Exception:
                # pylint: disable=broad-except
                if get_exception() is not e:
                    raise AssertionError('Expected get_exception() to return the exception that was raised')

# Generated at 2022-06-13 04:39:07.803224
# Unit test for function get_exception
def test_get_exception():
    def f():
        raise Exception("bogus error")
    try:
        f()
    except Exception:
        exc = get_exception()
        assert str(exc) == "bogus error"
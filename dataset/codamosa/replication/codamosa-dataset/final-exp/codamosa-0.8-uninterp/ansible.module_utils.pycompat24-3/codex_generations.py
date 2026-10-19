

# Generated at 2022-06-13 04:31:06.258044
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("Hello")
    except Exception:
        e = get_exception()

    assert isinstance(e, ValueError)

# Generated at 2022-06-13 04:31:15.813280
# Unit test for function get_exception
def test_get_exception():
    def f1():
        try:
            raise Exception('f1')
        except Exception:
            return get_exception()
    def f2():
        try:
            raise Exception('f2')
        except Exception:
            return get_exception()
    def f3():
        try:
            raise TypeError('f1')
        except Exception:
            return get_exception()
    def f4():
        try:
            raise NameError('f1')
        except Exception:
            return get_exception()

    # Make sure basic exceptions return
    assert type(f1()) == Exception
    assert type(f2()) == Exception
    assert type(f3()) == TypeError
    assert type(f4()) == NameError

    # Make sure we are getting the correct exception

# Generated at 2022-06-13 04:31:18.914267
# Unit test for function get_exception
def test_get_exception():
    """Verify that get_exception returns the current exception"""
    try:
        x = 1/0
    except ZeroDivisionError as e:
        assert e is get_exception()
    try:
        x = 1/0
    except ZeroDivisionError:
        e = get_exception()
    assert type(e) == ZeroDivisionError


# Generated at 2022-06-13 04:31:25.511323
# Unit test for function get_exception
def test_get_exception():
    def this_raises(x):
        raise x

    try:
        this_raises(Exception('test message'))
    except Exception:
        e = get_exception()
        print(e)
        assert str(e) == 'test message'
    else:
        assert False, "Did not raise"


# Generated at 2022-06-13 04:31:28.230333
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError('test')
    except TypeError as e:
        assert e is get_exception()
    try:
        try:
            raise TypeError('test')
        except TypeError:
            e = get_exception()
        raise NameError('test')
    except NameError as e:
        assert str(e) == 'test'
        assert isinstance(e, NameError)



# Generated at 2022-06-13 04:31:32.208710
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test exception')
    except Exception:
        e = get_exception()
        assert str(e) == 'Test exception', 'The exception we get back is not the one we just raised'

# Generated at 2022-06-13 04:31:40.323364
# Unit test for function get_exception
def test_get_exception():
    def test_function(foo, bar=10):
        try:
            return foo / bar
        except Exception:
            e = get_exception()
            return e
    assert get_exception() is None
    assert test_function(1.0, 2.0) == 0.5
    assert get_exception() is None
    assert isinstance(test_function(1, 0), ZeroDivisionError)
    assert isinstance(test_function(1), ZeroDivisionError)
    assert test_function(1) == get_exception()

# Generated at 2022-06-13 04:31:43.513190
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except ValueError:
        e = get_exception()

    assert isinstance(e, ValueError)



# Generated at 2022-06-13 04:31:47.479144
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert str(e) == 'foo'


# Generated at 2022-06-13 04:31:53.891435
# Unit test for function get_exception
def test_get_exception():

    # Test that it returns the right exception
    try:
        raise RuntimeError('foo')
    except:
        err = get_exception()
    assert RuntimeError is type(err)
    assert 'foo' == str(err)

    # Test that it does not mask the exception
    try:
        raise RuntimeError('foo')
    except:
        err = get_exception()
    assert sys.exc_info()[0] is RuntimeError
    assert 'foo' == str(sys.exc_info()[1])

# Generated at 2022-06-13 04:32:14.741349
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert str(e) == 'foo'

# Generated at 2022-06-13 04:32:17.554694
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('An error')
    except Exception:
        e = get_exception()

    assert isinstance(e, RuntimeError)
    assert e.args == ('An error',)



# Generated at 2022-06-13 04:32:22.637870
# Unit test for function get_exception
def test_get_exception():  # pragma: no cover
    def foo():
        try:
            raise Exception('foo')
        except Exception:
            e = get_exception()
            return e
    exc = foo()
    assert str(exc) == 'foo'

# Unit tests for function literal_eval

# Generated at 2022-06-13 04:32:28.105562
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('1')
    except RuntimeError as e1:
        assert e1 == get_exception()

# Generated at 2022-06-13 04:32:31.196076
# Unit test for function get_exception
def test_get_exception():
    """Ensure that the get_exception function works."""
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert e.args == ('foo',)

# Generated at 2022-06-13 04:32:42.178708
# Unit test for function get_exception
def test_get_exception():
    # import here so we don't have a spurious test dependency on pytest
    import pytest
    # The code below does several things:
    # 1) Raises an exception
    # 2) Catches the exception and verifies that the output is as expected
    # 3) Verifies that the exception is actually raised by the test framework
    try:
        raise Exception('Message')
     # pylint: disable=bare-except
     # Bare except cannot be made to work here because the pytest assertion
     # breaks the python2.4 compatibility that we have elsewhere.  The unit
     # test *should* fail if this except block catches the wrong type
    except:  # noqa: E722
        assert get_exception().args[0] == 'Message'
    with pytest.raises(Exception, match='Message'):
        raise Exception('Message')

# Generated at 2022-06-13 04:32:46.704088
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('This is the exception')
    except Exception:
        e = get_exception()
    try:
        raise e  # pylint: disable=raising-bad-type
    except Exception as e2:
        assert str(e) == str(e2), 'Original and re-raised exception must be identical'

# Generated at 2022-06-13 04:32:51.434782
# Unit test for function get_exception
def test_get_exception():
    try:
        this_should_fail
    except NameError:
        e = get_exception()

    assert isinstance(e, NameError)
    assert str(e) == 'name \'this_should_fail\' is not defined'
    assert repr(e) == 'NameError("name \'this_should_fail\' is not defined",)'



# Generated at 2022-06-13 04:32:56.957674
# Unit test for function get_exception
def test_get_exception():
    """Test function get_exception

    Create an exception, then call get_exception() in the except block to get the
    exception and verify it's the same exception.
    """
    assert get_exception() is None

    try:
        raise ValueError('test exception')
    except ValueError:
        exc = get_exception()

    assert isinstance(exc, ValueError)
    assert str(exc) == 'test exception'


# Generated at 2022-06-13 04:33:01.378029
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass

    try:
        raise MyException('foo')
    except:
        result = get_exception()
        assert type(result) is MyException
        assert result.args == ('foo',)

# Generated at 2022-06-13 04:33:40.080845
# Unit test for function get_exception
def test_get_exception():
    def a():
        raise RuntimeError('foo')

    try:
        a()
    except:
        e = get_exception()
    else:
        raise Exception('should not get here')
    assert type(e) is RuntimeError
    assert str(e) == 'foo'
    assert repr(e) == "RuntimeError('foo',)"

# Generated at 2022-06-13 04:33:43.349214
# Unit test for function get_exception
def test_get_exception():
        try:
            raise RuntimeError("Test exception")
        except Exception:
            e = get_exception()

        assert str(e) == "Test exception"



# Generated at 2022-06-13 04:33:52.605203
# Unit test for function get_exception
def test_get_exception():
    """Tests for the get_exception function"""
    # Reset the sys.exc_info for the test, so that we know that the
    # value we get back is from the call to get_exception
    sys.exc_clear()
    try:
        raise ValueError('Test exception')
    except ValueError as e:
        # Check that get_exception returns the current exception
        _exception = get_exception()
        assert e is _exception
        # Check that the exception is reraised
        try:
            raise
        except ValueError:
            assert e is sys.exc_info()[1]

# Unit tests for function literal_eval

# Generated at 2022-06-13 04:34:00.520305
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('This is a unit test of the get_exception helper function')
    except Exception:
        exc = get_exception()
        assert exc.args == ('This is a unit test of the get_exception helper function',), \
            'Failed to get the correct exception with get_exception helper function'
    try:
        raise Exception('This is a unit test of the get_exception helper function', 'two', 3)
    except Exception:
        exc = get_exception()
    assert exc.args == ('This is a unit test of the get_exception helper function', 'two', 3),\
        'Failed to get the correct exception with get_exception helper function'

# Generated at 2022-06-13 04:34:03.662574
# Unit test for function get_exception
def test_get_exception():
    try:
        foo
        assert False
    except NameError:
        e = get_exception()
        assert "name 'foo' is not defined" in str(e)

# Generated at 2022-06-13 04:34:06.427338
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Raised to test get_exception')
    except ValueError:
        assert get_exception().args[0] == 'Raised to test get_exception'



# Generated at 2022-06-13 04:34:08.612865
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('fubar')
    except ValueError as e:
        return_value = get_exception()
    assert e == return_value



# Generated at 2022-06-13 04:34:11.832731
# Unit test for function get_exception
def test_get_exception():
    """Test function to ensure proper functionality"""

    try:
        raise ValueError('test')
    except:
        e = get_exception()
        assert 'test' in str(e)
    try:
        raise ValueError()
    except:
        e = get_exception()
        assert 'test' not in str(e)


# Generated at 2022-06-13 04:34:16.532762
# Unit test for function get_exception
def test_get_exception():
    def expected_exception():
        try:
            raise ValueError('test_get_exception')
        except ValueError:
            e = get_exception()
            if e.args[0] != 'test_get_exception':
                raise Exception('Unexpected exception contents')

    expected_exception()

# Generated at 2022-06-13 04:34:23.336450
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('somevalue')
    except ValueError:
        exception = get_exception()

    if not isinstance(exception, ValueError):
        raise AssertionError('get_exception failed to return the current exception')
    if exception.message != 'somevalue':
        raise AssertionError('get_exception didn\'t return the right exception')

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:35:37.766037
# Unit test for function get_exception
def test_get_exception():
    "Unit test for function get_exception."

    def func():
        "This is the function we will call get_exception from"
        try:
            raise RuntimeError('testing')
        except Exception:
            return get_exception()

    def test():
        "This is the unit test function."
        try:
            raise RuntimeError('testing')
        except Exception:
            e = get_exception()
        assert str(e) == 'testing'

    test()
    assert func().args == ('testing',)

# Generated at 2022-06-13 04:35:40.116941
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except ZeroDivisionError as e:
        assert get_exception() is e



# Generated at 2022-06-13 04:35:41.808196
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Hello there!")
    except:
        assert("Hello there!" == get_exception().args[0])

# Generated at 2022-06-13 04:35:43.457718
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("some error")
    except Exception:
        e = get_exception()
        assert str(e) == 'some error'

# Generated at 2022-06-13 04:35:45.808774
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Hello')
    except Exception:
        e = get_exception()
        assert str(e) == 'Hello'
        assert repr(e) == 'Exception(\'Hello\',)'
        assert isinstance(e, Exception)

# Generated at 2022-06-13 04:35:47.306817
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        ex = get_exception()
    assert ex.__class__ == ZeroDivisionError

# Generated at 2022-06-13 04:35:50.828211
# Unit test for function get_exception
def test_get_exception():
    # Work around pyflakes stupidity
    get_exception

    try:
        raise ValueError('test')
    except ValueError as e:
        assert get_exception() is e



# Generated at 2022-06-13 04:35:54.868421
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=unused-variable,unused-argument
    def inner():
        try:
            raise TypeError('This is a test')
        except Exception:
            e = get_exception()

    try:
        inner()
    except TypeError as e:
        assert str(e) == 'This is a test'
        return

    assert False, 'Exception should have been reraised'



# Generated at 2022-06-13 04:35:57.860511
# Unit test for function get_exception
def test_get_exception():
    """
    Ensure that get_exception functions correctly.
    """
    try:
         raise RuntimeError("test_get_exception")
    except RuntimeError as e:
        assert get_exception() == e


# Generated at 2022-06-13 04:36:05.206280
# Unit test for function get_exception
def test_get_exception():
    import io
    import sys
    import cStringIO
    try:
        str(io.StringIO())
    except Exception:
        if sys.version_info[0] >= 3:
            # Python 3.x
            assert get_exception().__class__.__name__ == 'TypeError'
        else:
            # Python 2.6 (2.6 <= x <= 2.7)
            assert get_exception().__class__.__name__ == 'AttributeError'
        # Python 2.5
        assert str(get_exception()) == "StringIO instance has no attribute '__unicode__'"

# Generated at 2022-06-13 04:37:22.973246
# Unit test for function get_exception
def test_get_exception():

    def inner():
        raise ValueError('We get signal')

    try:
        inner()
    except ValueError:
        e = get_exception()
        exc_message = str(e)
    assert exc_message == 'We get signal'

# Generated at 2022-06-13 04:37:28.709957
# Unit test for function get_exception
def test_get_exception():
    """
    >>> try:
    ...     raise AssertionError('This is a test')
    ... except AssertionError:
    ...     e = get_exception()
    ...
    >>> e.args[0]
    'This is a test'
    """

# Generated at 2022-06-13 04:37:32.473257
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('This is a test.')
    except ValueError:
        exception = get_exception()
    assert exception.message == 'This is a test.'

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:37:36.258997
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Unit test")
    except RuntimeError:
        e = get_exception()
    assert isinstance(e, RuntimeError)
    assert e.args == ("Unit test",)

# unit test for function literal_eval.

# Generated at 2022-06-13 04:37:39.752653
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('testing')
    except Exception:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert e.args[0] == 'testing'


# Generated at 2022-06-13 04:37:44.577381
# Unit test for function get_exception
def test_get_exception():
    # Can't test this very well since the exception is based on system
    # state.  We'll just try to ensure that the exception is set and
    # that the types match what we expect:
    try:
        raise RuntimeError('This is the error text')
    except RuntimeError:
        exc = get_exception()
    assert isinstance(exc, RuntimeError)
    assert str(exc) == 'This is the error text'



# Generated at 2022-06-13 04:37:48.423293
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('abc')
    except RuntimeError as e:
        e2 = get_exception()
    assert e == e2



# Generated at 2022-06-13 04:37:50.452562
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError()
    except RuntimeError as e:
        assert get_exception() is e


# Generated at 2022-06-13 04:37:54.960474
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test Exception')
    except Exception:
        e = get_exception()
        assert e.args[0] == 'Test Exception'

# Generated at 2022-06-13 04:37:58.081417
# Unit test for function get_exception
def test_get_exception():
    try:
        try:
            raise Exception("message")
        except:
            e = get_exception()
            assert e.message == "message"
    except:  # pylint: disable=bare-except
        assert False, "Unittest for get_exception() failed"

# Generated at 2022-06-13 04:39:31.976346
# Unit test for function get_exception
def test_get_exception():
    import unittest

    class TestException(Exception):
        pass

    class GetExceptionTester(unittest.TestCase):
        def test_get_exception(self):
            try:
                raise TestException('Test.')
            except Exception:
                exc = get_exception()
            self.assertTrue(isinstance(exc, TestException))
            self.assertEqual(exc.args, ('Test.',))

    import sys
    # Python2.6 doesn't have argv[0] set properly, so populate it
    if len(sys.argv) < 1:
        sys.argv.append('ansible.module_utils.basic')
    unittest.main()

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:39:34.268856
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Foo")
    except Exception:
        e = get_exception()
        assert str(e) == "Foo"

# Generated at 2022-06-13 04:39:40.499129
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=unused-argument
    def raise_exception():
        raise ValueError
    try:
        raise_exception()
    # Need to catch the exception, but we want to check that it got
    # passed to us correctly.  So, store it away in a list so we can
    # compare it to what our function returns without it getting
    # garbage collected by err in the try/except scope.
    except:
        exc_info = sys.exc_info()
    assert exc_info[1] == get_exception()



# Generated at 2022-06-13 04:39:41.819028
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Foo')
    except Exception:
        e = get_exception()
        assert str(e) == 'Foo'



# Generated at 2022-06-13 04:39:44.368832
# Unit test for function get_exception
def test_get_exception():
    def testfunc():
        try:
            raise ValueError('test exception')
        except:
            return get_exception()

    e = testfunc()
    assert isinstance(e, ValueError)
    assert e.args == ('test exception',)


# Unit tests for function literal_eval

# Generated at 2022-06-13 04:39:47.246777
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('I\'m awesome')
    except Exception:
        e = get_exception()
        assert e.args[0] == 'I\'m awesome'

# Generated at 2022-06-13 04:39:52.219870
# Unit test for function get_exception
def test_get_exception():
    '''Validate that get_exception can retrieve the last exception's value.'''
    # pylint: disable=unreachable

# Generated at 2022-06-13 04:39:55.424852
# Unit test for function get_exception
def test_get_exception():
    def inner_test_get_exception():  # pylint: disable=unused-variable
        try:
            1 / 0
        except Exception:
            e = get_exception()
            return e
    assert isinstance(inner_test_get_exception(), ZeroDivisionError)

# Generated at 2022-06-13 04:39:58.861082
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('message')
    except RuntimeError:
        e = get_exception()
        assert e.args[0] == 'message'
        return
    assert False, 'Should not be reached'



# Generated at 2022-06-13 04:40:06.140371
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("test exception")
    except Exception as e:
        assert get_exception() is e
        assert get_exception() == e

# We use the literal_eval function in the module_utils/six.py module as well, but that
# module can import this one.  So we only do the unit tests for this module when it
# is run by itself.
if __name__ == '__main__':
    def test_literal_eval():
        def fail_type(x):
            try:
                literal_eval(x)
                raise AssertionError('%r should have failed' % x)
            except ValueError:
                pass
        fail_type('[foo]')
        fail_type('{foo: None}')
        fail_type('foo')
        fail_type(1)
       
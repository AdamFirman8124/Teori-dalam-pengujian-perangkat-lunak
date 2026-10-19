

# Generated at 2022-06-13 04:31:09.859494
# Unit test for function get_exception
def test_get_exception():
    success = False
    try:
        raise Exception()
    except Exception:
        exc_info = get_exception()
        success = True
    assert success, "Failed to get exception"
    assert exc_info is not None
    assert exc_info is not False  # This is a common failure mode

# Generated at 2022-06-13 04:31:11.649819
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except ZeroDivisionError:
        exc = get_exception()
    else:
        raise AssertionError

    try:
        raise exc
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError

# Generated at 2022-06-13 04:31:14.083076
# Unit test for function get_exception
def test_get_exception():
    def raise_exception(text):
        raise Exception(text)

    try:
        raise_exception("exception message")
    except Exception:
        exc = get_exception()
        assert exc.args[0] == "exception message"
        try:
            raise exc
        except Exception:
            pass
        try:
            raise exc from None
        except Exception:
            pass



# Generated at 2022-06-13 04:31:15.849537
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except ValueError:
        exc = get_exception()
    assert exc.__class__ == ValueError

# Generated at 2022-06-13 04:31:17.726325
# Unit test for function get_exception
def test_get_exception():
    # Test that we can use this code
    try:
        raise ValueError('An exception')
    except ValueError:
        e = get_exception()
    assert e.args == ('An exception',)


# Generated at 2022-06-13 04:31:20.061304
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Testing get_exception')
    except Exception:
        e = get_exception()
        assert e.args[0] == 'Testing get_exception'

# Tests for literal_eval()

# Generated at 2022-06-13 04:31:24.760833
# Unit test for function get_exception
def test_get_exception():
    '''Test function get exception'''
    try:
        raise ValueError('A really cool error')
    except ValueError as e:
        error = e
    assert error == get_exception()



# Generated at 2022-06-13 04:31:27.476322
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('xyz')
    except Exception:
        err = get_exception()

    assert str(err).endswith('xyz')



# Generated at 2022-06-13 04:31:32.820370
# Unit test for function get_exception
def test_get_exception():
    test_exc_msg = "Test message string"
    try:
        raise Exception(test_exc_msg)
    except Exception:
        exc = get_exception()
        assert str(exc) == test_exc_msg, "Test exception message"
        assert exc.__class__.__name__ == "Exception", "Test exception class"

# Generated at 2022-06-13 04:31:43.017385
# Unit test for function get_exception
def test_get_exception():
    """Unit test for get_exception.

    This test consists of simple thinko checks and is intended to test the edge cases
    (like Python 2.5) that are hard to test with a normal test suite.
    """
    # pylint: disable=unused-variable, missing-docstring

    # Test the basic idea
    try:
        raise Exception
    except Exception:
        e = get_exception()
    assert isinstance(e, Exception)

    # Make sure this works with bare excepts
    try:
        raise Exception
    except:
        e = get_exception()
    assert isinstance(e, Exception)

    # Make sure this works when there is a different exception class in scope.
    # Note: This will not work on Python 2.4
    class Exception2(Exception):
        pass


# Generated at 2022-06-13 04:32:02.677646
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)

# Generated at 2022-06-13 04:32:05.102297
# Unit test for function get_exception
def test_get_exception():
    try:
        raise NameError('I have a pet banana')
    except NameError as e:
        e2 = get_exception()
        assert e2 is e



# Generated at 2022-06-13 04:32:08.354493
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass

    def my_test_func():
        raise MyException('My Message')

    try:
        my_test_func()
    except:
        e = get_exception()
        assert isinstance(e, MyException)
        assert str(e) == 'My Message'

# Generated at 2022-06-13 04:32:10.848549
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("This is a test")
    except RuntimeError as exc:
        exc2 = get_exception()
        assert exc is exc2


# Generated at 2022-06-13 04:32:20.971135
# Unit test for function get_exception
def test_get_exception():

    def test_exception(exc):
        try:
            raise exc
        except:
            my_exception = get_exception()
        assert type(my_exception) is type(exc)
        assert str(my_exception) == str(exc)

    test_exception(Exception('foo'))
    test_exception(Exception(1, 'foo'))
    test_exception(Exception(Exception(1, 'foo'), 'bar'))

    # make sure we only catch the exception once
    class MyException(Exception):
        def __init__(self, *args, **kwargs):
            Exception.__init__(self, *args, **kwargs)
            self.raised = False

        def __str__(self):
            if not self.raised:
                self.raised = True

# Generated at 2022-06-13 04:32:24.563471
# Unit test for function get_exception
def test_get_exception():
    try:
        int('a')
    except:
        exc = get_exception()
        assert str(exc) == "invalid literal for int() with base 10: 'a'"

# Generated at 2022-06-13 04:32:27.287184
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except ValueError:
        e = get_exception()
    assert isinstance(e, ValueError)


# Generated at 2022-06-13 04:32:30.478679
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except Exception:
        e = get_exception()
        assert isinstance(e, RuntimeError)
        assert str(e) == 'foo'


# Generated at 2022-06-13 04:32:36.874850
# Unit test for function get_exception
def test_get_exception():
    # The function does not need to be covered by pytest as it is not used
    # within the unit tests
    try:
        raise TypeError('test exception')
    except TypeError:
        e = get_exception()
        if not isinstance(e, TypeError):
            raise AssertionError
        if str(e) != 'test exception':
            raise AssertionError

# Generated at 2022-06-13 04:32:42.258028
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert str(e) == 'foo'
        assert repr(e) == 'Exception(\'foo\',)'
    try:
        raise Exception('bar')
    except Exception:
        e = get_exception()
        assert str(e) == 'bar'
        assert repr(e) == 'Exception(\'bar\',)'



# Generated at 2022-06-13 04:33:20.068372
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Exception raised")
    except Exception:
        e = get_exception()
    assert e.args[0] == "Exception raised"



# Generated at 2022-06-13 04:33:26.792291
# Unit test for function get_exception
def test_get_exception():
    try:
        raise AssertionError('test')
    except AssertionError as e:
        assert e == get_exception()
    try:
        raise AssertionError('test')
    except AssertionError:
        e = get_exception()
        assert isinstance(e, AssertionError)
        assert e.message == 'test'


# Test the literal_eval function on python versions that have it

# Generated at 2022-06-13 04:33:29.746985
# Unit test for function get_exception
def test_get_exception():
    try:
        try:
            raise Exception("Bacon")
        except:
            e = get_exception()
            assert str(e) == "Bacon"
    except:
        assert False, "Unable to return the current exception"



# Generated at 2022-06-13 04:33:34.026429
# Unit test for function get_exception
def test_get_exception():
    """print out the current exception"""
    def raise1():
        raise Exception()

    def raise2():
        def inner():
            raise1()
        inner()

    try:
        raise2()
    except Exception:
        print(get_exception())



# Generated at 2022-06-13 04:33:45.628142
# Unit test for function get_exception
def test_get_exception():  # pragma: no cover
    import pytest
    from ansible.module_utils._text import to_text

    from ansible.module_utils import basic

    try:
        raise ValueError('abc')
    except ValueError as e:
        assert basic.get_exception() is e

    try:
        raise ValueError('def')
    except:  # pylint: disable=bare-except
        e = basic.get_exception()
        assert isinstance(e, ValueError)
        assert to_text(e) == 'def'

    try:
        raise ValueError('ghi')
    except:  # pylint: disable=bare-except
        e = basic.get_exception()
        assert isinstance(e, ValueError)
        assert to_text(e) == 'ghi'

# Generated at 2022-06-13 04:33:50.788762
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        exc = get_exception()

# Generated at 2022-06-13 04:33:53.547865
# Unit test for function get_exception
def test_get_exception():
    test_string = 'this is a test'
    try:
        raise Exception(test_string)
    except Exception:
        e = get_exception()
        assert test_string in str(e), str(e)



# Generated at 2022-06-13 04:33:55.690596
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
    assert unicode(e) == 'foo'

# Generated at 2022-06-13 04:33:58.138137
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except Exception:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)


# Generated at 2022-06-13 04:34:00.860502
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("Exception thrown")
    except:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert "Exception thrown" == e.args[0]



# Generated at 2022-06-13 04:34:38.866279
# Unit test for function get_exception
def test_get_exception():
    class TestException(Exception):
        pass

    try:
        raise TestException('test exception')
    except TestException:
        e = get_exception()
        assert isinstance(e, TestException)
        assert e.args[0] == 'test exception'

# Generated at 2022-06-13 04:34:43.019323
# Unit test for function get_exception
def test_get_exception():
    import doctest
    import ansible.module_utils.basic

    failed, _ = doctest.testmod(ansible.module_utils.basic, raise_on_error=True)
    if failed == 0:
        print('SUCCESS: %s' % __file__)

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:34:45.555894
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('hello')
    except Exception:
        e = get_exception()
    assert str(e) == 'hello'

# Generated at 2022-06-13 04:34:52.177734
# Unit test for function get_exception
def test_get_exception():
    def foo(x):
        raise Exception(x)

    def bar(x):
        try:
            foo(x)
        except Exception:
            return get_exception()

    random_value = 'bogus'
    e = bar(random_value)
    assert e.args[0] == random_value
    assert str(e) == random_value


# Generated at 2022-06-13 04:34:54.682740
# Unit test for function get_exception
def test_get_exception():
    try:
        int("spam")
    except:
        exc = get_exception()
    assert str(exc) == "'spam' is not a valid integer"

# Generated at 2022-06-13 04:34:59.883616
# Unit test for function get_exception

# Generated at 2022-06-13 04:35:02.811580
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('An exception')
    except:
        e = get_exception()
        x = str(e)
    assert(x == 'An exception')

# Generated at 2022-06-13 04:35:05.265777
# Unit test for function get_exception
def test_get_exception():
    class testException(Exception):
        pass
    try:
        raise testException
    except Exception:
        e = get_exception()
    assert isinstance(e, testException)

# Generated at 2022-06-13 04:35:06.666512
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Test exception')
    except ValueError:
        e = get_exception()
    assert e.args[0] == 'Test exception'


# Generated at 2022-06-13 04:35:08.920946
# Unit test for function get_exception
def test_get_exception():

    def _():
        raise ValueError('foo')


# Generated at 2022-06-13 04:35:43.463351
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('bar')
    except RuntimeError:
        e = get_exception()
    assert e.args == ('bar',)



# Generated at 2022-06-13 04:35:45.064059
# Unit test for function get_exception

# Generated at 2022-06-13 04:35:48.324242
# Unit test for function get_exception
def test_get_exception():
    def div(dividend, divisor):
        try:
            raise ValueError('Test exception')
        except ValueError:
            e = get_exception()
            assert e.args == ('Test exception',)
            assert str(e) == 'Test exception'
            assert repr(e) == "ValueError('Test exception',)"

    div(1, 0)

# Generated at 2022-06-13 04:35:51.037812
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('silly stray value error')
    except:
        e = get_exception()
        assert isinstance(e, ValueError), '%s is not a ValueError' % e.__class__.__name__
        assert str(e) == 'silly stray value error', '%s is not the expected ValueError' % str(e)

# Generated at 2022-06-13 04:35:57.700513
# Unit test for function get_exception
def test_get_exception():
    import sys
    import unittest

    class GetExceptionTest(unittest.TestCase):
        def test_get_exception(self):
            try:
                raise Exception("Testing get_exception")
            except Exception:
                self.assertEqual(b"Testing get_exception", get_exception().args)

    suite = unittest.TestLoader().loadTestsFromTestCase(GetExceptionTest)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)

# Generated at 2022-06-13 04:35:59.579521
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except:
        assert str(get_exception()) == 'foo'


# Generated at 2022-06-13 04:36:02.221726
# Unit test for function get_exception
def test_get_exception():
    def f():  # pylint: disable=unused-variable
        raise ValueError('test')

    try:
        f()
    except:
        e = get_exception()
        assert(isinstance(e, ValueError))

# Generated at 2022-06-13 04:36:03.296628
# Unit test for function get_exception
def test_get_exception():
    import unittest
    import sys

    # On py3 this module

# Generated at 2022-06-13 04:36:11.341509
# Unit test for function get_exception

# Generated at 2022-06-13 04:36:16.094352
# Unit test for function get_exception
def test_get_exception():
    """Ensure that get_exception() returns the correct values.

    When an exception occurs, get_exception() should return the exception
    after it is assigned to a variable.

    When no exception occurs, get_exception() should return None.
    """

    # No Exception
    if get_exception():
        raise Exception("get_exception returned %s instead of None" % get_exception())
    # Exception
    try:
        raise TypeError('foo')
    except Exception:
        e = get_exception()

    # On python3, the exception message is a unicode string and the type
    # is a subclass (i.e. TypeError is subclass of builtin_function_or_method)
    # of the base Exception type.

# Generated at 2022-06-13 04:37:32.120221
# Unit test for function get_exception
def test_get_exception():
    """
    >>> from ansible.module_utils._text import to_text
    >>> try:
    ...     raise ValueError("This is a test exception")
    ... except ValueError:
    ...     exc = get_exception()
    ...     try:
    ...         raise exc
    ...     except ValueError as exc:
    ...         assert to_text(str(exc)) == 'This is a test exception'

    """



# Generated at 2022-06-13 04:37:34.753476
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        raise ValueError('expected_error')

    try:
        raise_exception()
    except Exception as e:
        assert get_exception().args == e.args

# Generated at 2022-06-13 04:37:42.733287
# Unit test for function get_exception
def test_get_exception():
    class ReallyReallyBadError(Exception):
        pass

    try:
        raise ReallyReallyBadError
    except Exception:
        e = get_exception()
        if isinstance(e, ReallyReallyBadError):
            pass
        else:
            raise AssertionError("Try/Except didn't catch the right exception")

    try:
        raise ReallyReallyBadError
    except Exception:
        e = get_exception()
        if isinstance(e, IOError):
            raise AssertionError('Try/Except caught the wrong exception')
    else:
        raise AssertionError('Try/Except didnt catch any exception')

# Generated at 2022-06-13 04:37:47.970554
# Unit test for function get_exception
def test_get_exception():
    import random
    import traceback
    try:
        lst = []
        random.shuffle(lst)
    except TypeError:
        exc = get_exception()
        filtered_traceback = traceback.extract_tb(sys.exc_info()[2])
        full_traceback = traceback.extract_tb(sys.exc_info()[2],
                                              limit=None)
        assert exc == get_exception()
        assert filtered_traceback == traceback.extract_tb(sys.exc_info()[2])
        assert full_traceback != filtered_traceback
        assert sys.exc_info()[2]


# Generated at 2022-06-13 04:37:49.171541
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except:
        e = get_exception()
        assert e.args == ('foo',)



# Generated at 2022-06-13 04:37:50.067840
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        exc = get_exception()
    assert isinstance(exc, ZeroDivisionError)

# Generated at 2022-06-13 04:37:55.422859
# Unit test for function get_exception
def test_get_exception():  # pylint: disable=missing-docstring
    try:
        raise Exception('Outer exception')
    except Exception:
        outer_exception = get_exception()
        assert outer_exception.args == ('Outer exception',)
        try:
            raise Exception('Inner exception')
        except Exception:
            inner_exception = get_exception()
            assert inner_exception.args == ('Inner exception',)
    assert outer_exception is not inner_exception


# Generated at 2022-06-13 04:37:57.733728
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('hey there')
    except ValueError as e:
        actual_e = get_exception()
    assert e is actual_e


# Generated at 2022-06-13 04:38:00.612326
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass
    try:
        raise MyException('Test')
    except:
        # pylint: disable=bare-except
        e = get_exception()
        assert isinstance(e, MyException)
        assert str(e) == 'Test'


# Generated at 2022-06-13 04:38:02.350580
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('test error')
    except Exception as e:
        assert e == get_exception()

# Generated at 2022-06-13 04:40:53.014847
# Unit test for function get_exception
def test_get_exception():
    # Test_exceptions is an exception that we use for testing purposes.
    class Test_exceptions(Exception):
        def __init__(self, value=None):
            self.value = value

        def __str__(self):
            return repr(self.value)

    try:
        raise Test_exceptions("Catch me")
    except Exception:
        e = get_exception()
        assert(type(e) == type(Test_exceptions("Catch me")))
        assert(str(e) == "Catch me")
    else:
        raise AssertionError("'except Exception' didn't catch anything")

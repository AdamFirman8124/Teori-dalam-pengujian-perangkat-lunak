

# Generated at 2022-06-13 04:31:08.128074
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=simplifiable-if-expression,unused-variable
    # python2
    try:
        raise Exception()
    except Exception:
        e = get_exception()
        assert e
    # python3
    try:
        raise Exception()
    except Exception:
        e = get_exception()
        assert e

# Generated at 2022-06-13 04:31:12.298660
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except ZeroDivisionError:
        e = get_exception()
        assert isinstance(e, ZeroDivisionError)
        assert e.__class__.__name__ == 'ZeroDivisionError'
    else:
        raise Exception('1 / 0 did not raise exception')

# Generated at 2022-06-13 04:31:13.368622
# Unit test for function get_exception
def test_get_exception():
    e = None
    try:
        raise ValueError
    except:
        e = get_exception()
    assert isinstance(e, ValueError)

# Generated at 2022-06-13 04:31:17.767907
# Unit test for function get_exception
def test_get_exception():  # pragma: no cover
    try:
        raise RuntimeError('foobar')
    except RuntimeError:
        exc = get_exception()
    assert exc.args[0] == 'foobar'



# Generated at 2022-06-13 04:31:19.598370
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test exception')
    except Exception:
        exc = get_exception()
    assert str(exc) == 'Test exception'


# Generated at 2022-06-13 04:31:26.807850
# Unit test for function get_exception
def test_get_exception():
    global raises_error  # pylint: disable=global-statement

    def raises_error():
        return 1 + "foo"  # pylint: disable=unsupported-binary-operation

    try:
        raises_error()
    except:
        exc_info = sys.exc_info()
        assert get_exception() is exc_info[1]



# Generated at 2022-06-13 04:31:28.677553
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('a test')
    except:
        e = get_exception()
        assert str(e) == 'a test'

# Generated at 2022-06-13 04:31:32.335911
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except ValueError:
        e = get_exception()

    if e.args[0] != 'foo':
        raise AssertionError("get_exception() didn't return the exception we just raised")


# Generated at 2022-06-13 04:31:37.306390
# Unit test for function get_exception
def test_get_exception():
    def test_function():
        try:
            raise Exception('exception message')
        except Exception:
            return get_exception()
    res = test_function()
    assert isinstance(res, Exception)
    assert str(res) == 'exception message'

# Generated at 2022-06-13 04:31:41.315774
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('123')
    except RuntimeError:
        e = get_exception()
        assert e.args == ('123',)
        assert str(e) == "123"
        assert repr(e) == 'RuntimeError(\'123\',)'

# Generated at 2022-06-13 04:32:05.469784
# Unit test for function get_exception
def test_get_exception():
    '''
    >>> def f():
    ...     try:
    ...         raise Exception('test')
    ...     except Exception:
    ...         e = get_exception()
    ...         return e
    >>> e = f()
    >>> isinstance(e, Exception)
    True
    >>> str(e)
    'test'
    '''

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 04:32:07.239718
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        e = get_exception()
    assert e


# Unit testing for function literal_eval

# Generated at 2022-06-13 04:32:16.131575
# Unit test for function get_exception
def test_get_exception():
    """Function 'get_exception' should return the same exception object as is
    currently being handled.
    """
    try:
        raise ValueError("This is a test exception")
    except ValueError as exc:
        assert exc is get_exception(),\
            "The exception object does not match the current exception"
    try:
        raise ValueError("This is a test exception")
    except ValueError:
        exc = get_exception()
        assert isinstance(exc, ValueError)
        assert str(exc) == "This is a test exception",\
            "The exception object does not match the current exception"

# Generated at 2022-06-13 04:32:28.106454
# Unit test for function get_exception
def test_get_exception():
    # Catch an exception that we expect
    try:
        raise KeyError()
    except KeyError:
        e = get_exception()
    assert isinstance(e, KeyError)

    # Catch a catch-all exception
    try:
        raise KeyError()
    except:
        e = get_exception()
    assert isinstance(e, KeyError)

    # Make sure the exception is only caught once
    def test_except(n):
        try:
            raise KeyError()
        except:
            if n:
                return test_except(n-1)
            else:
                return get_exception()
    e = test_except(10)
    assert isinstance(e, KeyError)



# Generated at 2022-06-13 04:32:30.697202
# Unit test for function get_exception
def test_get_exception():
    import pytest

    try:
        int('bad')
    except:
        exc = get_exception()

    with pytest.raises(ValueError):
        int('bad')

# Generated at 2022-06-13 04:32:41.721815
# Unit test for function get_exception
def test_get_exception():
    def test1():
        try:
            1 / 0
        except:
            return get_exception()

    class TestException(Exception):
        pass

    def test2():
        try:
            raise TestException('Yet another dummy exception')
        except:
            return get_exception()

    # Python 2.4 does not have ZeroDivisionError.  (We're not testing
    # python 2.4, just checking to see if ZeroDivisionError doesn't exist)
    if getattr(ZeroDivisionError, "__module__", None) is None:
        # Python 2.4, ZeroDivisionError doesn't exist
        assert issubclass(test1().__class__, Exception)
        assert issubclass(test2().__class__, Exception)
        assert test2().__class__.__name__ == 'TestException'


# Generated at 2022-06-13 04:32:44.951529
# Unit test for function get_exception
def test_get_exception():
    """Test the get_exception function"""
    try:
        raise RuntimeError('Test Exception')
    except RuntimeError as e:
        exc = get_exception()
        assert e == exc



# Generated at 2022-06-13 04:32:53.547960
# Unit test for function get_exception
def test_get_exception():  # pylint: disable=too-many-branches
    import imp, os
    import types

    # Test for bug in get_exception that would cause it to fail on python 2.4
    if sys.version_info[:2] < (2, 6):
        class TestException(Exception):
            pass

        def test_call():
            raise TestException

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'get_exception_test.py'), 'w') as f:
            f.write('def test_call():\n')
            f.write('    raise TestException\n')
            f.write('\n')
            f.write('class TestException(Exception):\n')

# Generated at 2022-06-13 04:32:56.460114
# Unit test for function get_exception
def test_get_exception():
    '''Test that get_exception() returns the current exception.'''
    try:
        raise Exception('boo')
    except:
        assert get_exception().message == 'boo'



# Generated at 2022-06-13 04:33:02.149103
# Unit test for function get_exception
def test_get_exception():
    '''
    >>> try:
    ...     raise Exception("foo")
    ... except:
    ...     exc = get_exception()
    ...
    >>> print("%s" % exc)
    foo
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 04:33:21.432234
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)



# Generated at 2022-06-13 04:33:27.513616
# Unit test for function get_exception
def test_get_exception():
    try:
        int('a')
    except ValueError:
        e = get_exception()
        if str(e) != "invalid literal for int() with base 10: 'a'":
            raise AssertionError('Exception has the wrong value. Actual: {}'.format(str(e)))
    else:
        raise AssertionError('get_exception() should have been called inside the exception block')

# Generated at 2022-06-13 04:33:39.303506
# Unit test for function get_exception
def test_get_exception():  # pylint: disable=unused-variable
    # pylint: disable=no-self-use,invalid-name,unused-argument,too-few-public-methods
    def method_that_raises():
        raise Exception()

    class Struct:
        def __init__(self, **entries):
            self.__dict__.update(entries)

        def __eq__(self, other):
            if not isinstance(other, Struct):
                return False

            return self.__dict__ == other.__dict__

    class TestGetException:
        def test_exception(self):
            try:
                method_that_raises()
            except Exception:
                e = get_exception()
            assert Struct(name='Exception', args=[]) == e


# Generated at 2022-06-13 04:33:43.859000
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception:
        e = get_exception()
        assert e.__class__.__name__ == 'ZeroDivisionError'

# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

# Generated at 2022-06-13 04:33:49.848238
# Unit test for function get_exception
def test_get_exception():
    # Test a string exception
    try:
        raise 'foo'
    except:
        assert get_exception() == 'foo'

    # Test an object exception, then catch with a string exception
    try:
        raise object()
    except 'foo':
        pass
    except:
        assert get_exception() is not 'foo'



# Generated at 2022-06-13 04:33:53.259087
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("foo")
    except:
        e = get_exception()
    assert str(e) == "foo"

# Generated at 2022-06-13 04:33:57.631209
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except ValueError as e:
        e_test = get_exception()
        if e is not e_test:
            raise AssertionError("%s is not %s" % (e, e_test))

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:34:00.396028
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except ZeroDivisionError:
        exc = get_exception()
        assert type(exc) == ZeroDivisionError
        assert str(exc) == 'integer division or modulo by zero'



# Generated at 2022-06-13 04:34:04.206837
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Ansible RuntimeError")
    except RuntimeError:
        exc = get_exception()
        assert isinstance(exc, RuntimeError)
        assert exc.args == ("Ansible RuntimeError",)



# Generated at 2022-06-13 04:34:06.950088
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test')
    except:
        e = get_exception()
    assert str(e) == 'Test'
# vim: set expandtab:ts=4:sw=4

# Generated at 2022-06-13 04:34:43.512641
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Fake Exception")
    except:  # noqa  -- catch it all
        e = get_exception()
    assert str(e) == "Fake Exception"



# Generated at 2022-06-13 04:34:47.816373
# Unit test for function get_exception
def test_get_exception():
    try:
        raise(ValueError('This is a test'))
    except:
        e = get_exception()
        assert isinstance(e, ValueError)

# Generated at 2022-06-13 04:34:52.528231
# Unit test for function get_exception
def test_get_exception():
    e = get_exception()
    if e is not None:
        raise ValueError('No exception should currently be present')
    try:
        raise ValueError()
    except:
        e = get_exception()
    if not isinstance(e, ValueError):
        raise ValueError('Exception is not a ValueError')

# Generated at 2022-06-13 04:34:57.504280
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass
    try:
        raise MyException('test')
    except:
        e = get_exception()
    assert e.args[0] == 'test', e.args[0]
    assert type(e) == MyException, type(e)



# Generated at 2022-06-13 04:35:00.671526
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert e.args[0] == 'foo'

# Generated at 2022-06-13 04:35:05.959290
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("An exception")
    except Exception:
        try:
            raise TypeError("an inner exception")
        except Exception:
            pass
        e = get_exception()
        assert e is not None
        assert e.__class__ == ValueError
        assert str(e) == "An exception"
        assert e.args == ("An exception",)


# Generated at 2022-06-13 04:35:07.891864
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError()
    except ValueError:
        exc = get_exception()
    assert isinstance(exc, ValueError)
    try:
        1 / 0
    except Exception:
        exc = get_exception()
    assert isinstance(exc, ZeroDivisionError)

# Generated at 2022-06-13 04:35:10.774341
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except ZeroDivisionError as e:
        assert get_exception() is e
    else:
        assert False, 'Division by zero did not raise ZeroDivisionError'


# Generated at 2022-06-13 04:35:15.264467
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Testing get_exception")
    except:
        e = get_exception()
    assert str(e) == "Testing get_exception"
    assert repr(e) == "Exception('Testing get_exception',)"


# Generated at 2022-06-13 04:35:21.106333
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')  # pylint: disable=redefined-outer-name
    except Exception:
        e = get_exception()
        assert str(e) == 'foo'
    try:
        raise ValueError(42, 'life')  # pylint: disable=redefined-outer-name
    except Exception:
        e = get_exception()
        assert str(e) == '(42, \'life\')'

# Generated at 2022-06-13 04:36:38.897905
# Unit test for function get_exception

# Generated at 2022-06-13 04:36:40.885414
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception as e:
        exception = get_exception()
    assert exception == e

# Generated at 2022-06-13 04:36:44.550453
# Unit test for function get_exception
def test_get_exception():
    class TheException(Exception):
        pass

    try:
        raise TheException()
    except Exception:
        e = get_exception()
        assert type(e) == TheException
        try:
            raise
        except Exception:
            e2 = get_exception()
            assert e2 is e

# Generated at 2022-06-13 04:36:50.183235
# Unit test for function get_exception
def test_get_exception():
    def f1(a, b):
        raise ValueError('f1')

    try:
        f1('x', None)
    except ValueError:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert str(e) == 'f1'
    else:
        assert False, 'f1() did not raise'

# Generated at 2022-06-13 04:36:53.150070
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError
    except TypeError:
        e = get_exception()
    assert e.__class__.__name__ == 'TypeError'



# Generated at 2022-06-13 04:36:55.015905
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Bad thing happened')
    except:
        _e = get_exception()

    assert str(_e) == 'Bad thing happened'

# Generated at 2022-06-13 04:36:57.253654
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Foobar Exception")
    except:
        e = get_exception()
        assert str(e) == "Foobar Exception"

# Generated at 2022-06-13 04:36:59.300768
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
    assert e.args[0] == 'foo'



# Generated at 2022-06-13 04:37:02.791232
# Unit test for function get_exception
def test_get_exception():
    """Test that get_exception works."""

    def buggy_function():
        """A function that raises exceptions."""
        raise ValueError("Away")

    test_cases = [
        ValueError("Incoming"),
        buggy_function(),
    ]
    for test_case in test_cases:
        try:
            raise test_case
        except Exception:
            assert get_exception() == test_case

# Generated at 2022-06-13 04:37:05.934590
# Unit test for function get_exception
def test_get_exception():
    """Unit tests for get_exception"""
    try:
        raise ValueError('Testing')
    except ValueError as e:
        assert e == get_exception()

# Generated at 2022-06-13 04:39:41.387328
# Unit test for function get_exception
def test_get_exception():
    t = None
    try:
        raise Exception('test')
    except:
        t = get_exception()
    assert isinstance(t, Exception)
    assert 'test' in str(t)

# Generated at 2022-06-13 04:39:43.128029
# Unit test for function get_exception
def test_get_exception():
    import pytest
    try:
        raise RuntimeError('foo')
    except RuntimeError as e:
        got_exception = get_exception()
        assert got_exception is e

# Generated at 2022-06-13 04:39:45.159292
# Unit test for function get_exception
def test_get_exception():
    try:
        raise 'test'
    except:
        e = get_exception()
    assert 'test' == e

# Generated at 2022-06-13 04:39:50.341196
# Unit test for function get_exception
def test_get_exception():
    """Run the unittest for get_exception"""
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
    assert 'foo' == str(e)

# Test literal eval - tests the 2.4 version, the 2.6 version should be covered
# by python's own unit tests

# Generated at 2022-06-13 04:39:52.549159
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except RuntimeError:
        e = get_exception()
    assert e.args[0] == 'foo'


# Generated at 2022-06-13 04:39:54.811689
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        exc = get_exception()
    assert str(exc) == 'integer division or modulo by zero'


# Generated at 2022-06-13 04:39:58.240227
# Unit test for function get_exception
def test_get_exception():
    def foo(bar, baz):
        raise ValueError
    try:
        foo(1, 2)
    except:
        ex = get_exception()
        assert isinstance(ex, ValueError)



# Generated at 2022-06-13 04:39:59.660638
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("hello world")
    except ValueError as e:
        assert e is get_exception()

# Generated at 2022-06-13 04:40:00.986881
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test')
    except Exception:
        assert get_exception().args[0] == 'test'

# Generated at 2022-06-13 04:40:04.714250
# Unit test for function get_exception
def test_get_exception():
    try:
        raise AssertionError('test')
    except AssertionError:
        assert get_exception().args == ('test', )
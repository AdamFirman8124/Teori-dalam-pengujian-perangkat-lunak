

# Generated at 2022-06-13 04:31:04.422238
# Unit test for function get_exception
def test_get_exception():
    try:
        # Don't use ``raise IOError`` here, it doesn't work on Python 2.4
        raise IOError()
    except IOError:
        exc = get_exception()
    assert exc is not None



# Generated at 2022-06-13 04:31:07.984992
# Unit test for function get_exception
def test_get_exception():
    """Unit test for function get_exception"""
    try:
        raise Exception('Test exception')
    except Exception:
        e = get_exception()
        assert str(e) == 'Test exception'

if __name__ == "__main__":
    test_get_exception()

# Generated at 2022-06-13 04:31:10.197615
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        assert get_exception().message == 'foo'

# Generated at 2022-06-13 04:31:16.000244
# Unit test for function get_exception
def test_get_exception():
    """
    Function: get_exception
    Input: Nothing
    Output: Return code and exception information
    Test case 1: Test get_exception
               1: Run the get_exception function
               2: Check the returned exception
    Expected result: Expected exception information should be retuned
    """

# Generated at 2022-06-13 04:31:19.195317
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Test")
    except RuntimeError:
        e = get_exception()
        assert e.args[0] == "Test"


# Generated at 2022-06-13 04:31:26.088836
# Unit test for function get_exception
def test_get_exception():
    "Test the get_exception function"

    def f1():
        raise Exception('message f1')

    def f2():
        try:
            f1()
        except Exception:
            return get_exception()

    result = f2()
    assert type(result) == Exception
    assert str(result) == 'message f1'

# Generated at 2022-06-13 04:31:28.117414
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception as e:
        assert get_exception() is e


# Generated at 2022-06-13 04:31:30.333188
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Test')
    except RuntimeError:
        e = get_exception()
    assert str(e) == 'Test'

# Generated at 2022-06-13 04:31:37.047771
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except ZeroDivisionError:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)

    # Python 2.4 compatibility test
    try:
        1 / 0
    except ZeroDivisionError:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)

# Generated at 2022-06-13 04:31:41.934583
# Unit test for function get_exception
def test_get_exception():
    """
    Sanity test for function get_exception.
    """
    class MyException(Exception):
        pass
    try:
        raise MyException('test')
    except Exception:
        e = get_exception()
    # Make sure we get an exception out
    assert isinstance(e, MyException)
    # Make sure it's the exception we threw
    assert str(e) == 'test'



# Generated at 2022-06-13 04:31:59.458121
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=import-error,no-member
    import pytest
    import ansible.module_utils.six as six
    try:
        raise Exception('foo')
    except Exception:
        e = ansible.module_utils.six.get_exception()
        assert isinstance(e, Exception)
        assert str(e) == 'foo'
    try:
        raise AssertionError('bar')
    except AssertionError:
        e = ansible.module_utils.six.get_exception()
        assert isinstance(e, AssertionError)
        assert str(e) == 'bar'


# Generated at 2022-06-13 04:32:02.363027
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Foobar")
    except:
        pass
    assert isinstance(get_exception(), RuntimeError)

# Generated at 2022-06-13 04:32:04.497633
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('boring error')
    except ValueError as e:
        assert get_exception() is e

# Generated at 2022-06-13 04:32:06.802217
# Unit test for function get_exception
def test_get_exception():
    try:
        raise IOError('Reason')
    except IOError:
        e = get_exception()
        assert e.args[0] == 'Reason'
    else:
        assert False

# Generated at 2022-06-13 04:32:14.317651
# Unit test for function get_exception
def test_get_exception():
    """Unit test for function get_exception()."""
    assert get_exception() is None
    try:
        raise ValueError
    except ValueError:
        exc = get_exception()
        assert isinstance(exc, ValueError)
    assert get_exception() is None
    try:
        1/0
    except ZeroDivisionError:
        exc = get_exception()
        assert isinstance(exc, ZeroDivisionError)
    assert get_exception() is None



# Generated at 2022-06-13 04:32:17.556110
# Unit test for function get_exception
def test_get_exception():
    def throw_exception():
        try:
            raise Exception('foo')
        except Exception:
            e = get_exception()
        return e

    e = throw_exception()
    assert e.args == ('foo',)

# Generated at 2022-06-13 04:32:21.829436
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("Unit test for get_exception")
    except:
        assert get_exception().args[0] == "Unit test for get_exception"


# Generated at 2022-06-13 04:32:26.813638
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=unused-variable,missing-docstring
    try:
        raise ValueError('foo')
    except Exception:
        e = get_exception()
    assert isinstance(e, ValueError)
    assert e.args == ('foo',)



# Generated at 2022-06-13 04:32:29.962086
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Foo")
    except Exception:
        assert get_exception() is sys.exc_info()[1]


# Generated at 2022-06-13 04:32:33.347671
# Unit test for function get_exception

# Generated at 2022-06-13 04:32:52.393063
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except ValueError as e:
        assert get_exception() is e



# Generated at 2022-06-13 04:32:55.762474
# Unit test for function get_exception
def test_get_exception():
    ''' Test the get_exception function '''

# Generated at 2022-06-13 04:32:58.146008
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test')
    except:
        e = get_exception()
        assert e.__class__ is Exception

# Generated at 2022-06-13 04:33:02.421514
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass

    try:
        raise MyException()
    except Exception:
        e = get_exception()

    assert isinstance(e, MyException)
    assert str(e) == "()"


# Generated at 2022-06-13 04:33:04.771289
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test')
    except:
        e = get_exception()
    assert str(e) == 'test'


# Generated at 2022-06-13 04:33:05.755168
# Unit test for function get_exception
def test_get_exception():
    import unittest


# Generated at 2022-06-13 04:33:08.423457
# Unit test for function get_exception
def test_get_exception():
    """Test get_exception function"""
    try:
        raise RuntimeError('This is a test')
    except RuntimeError as e:
        e2 = get_exception()
    assert e == e2



# Generated at 2022-06-13 04:33:12.276704
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('This is a test')
    except ValueError as e:
        exc = get_exception()
    assert e == exc
    class TestException(Exception):
        def __init__(self):
            pass
    try:
        raise TestException()
    except TestException as e:
        exc = get_exception()
    assert e == exc

# Generated at 2022-06-13 04:33:14.364673
# Unit test for function get_exception

# Generated at 2022-06-13 04:33:15.949476
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0  # pylint: disable=pointless-statement
    except Exception:
        e = get_exception()
        assert e.args == ('integer division or modulo by zero',)

# Generated at 2022-06-13 04:33:34.492096
# Unit test for function get_exception
def test_get_exception():
    try:
        int('foo')
    except Exception:
        e = get_exception()
    assert isinstance(e, ValueError)



# Generated at 2022-06-13 04:33:37.806674
# Unit test for function get_exception

# Generated at 2022-06-13 04:33:50.097174
# Unit test for function get_exception
def test_get_exception():
    class A(Exception):
        pass
    class B(Exception):
        pass
    class C(Exception):
        pass
    def test(a, b, c):
        try:
            a()
        except A:
            e = get_exception()
            if not isinstance(e, A):
                return False
            b()
        except B:
            e = get_exception()
            if not isinstance(e, B):
                return False
            c()
        except C:
            e = get_exception()
            if not isinstance(e, C):
                return False
        return True
    def a():
        raise A()
    def b():
        raise B()
    def c():
        raise C()
    assert test(a, b, c)


# Generated at 2022-06-13 04:33:54.374248
# Unit test for function get_exception
def test_get_exception():
    """Unit test for get_exception"""
    # Make sure that it returns the exception instance
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert e.args == ('foo', )
        assert e.message == 'foo'

    # Make sure that it works even if no exception is being handled
    e = get_exception()
    assert e is None

# Generated at 2022-06-13 04:33:58.138292
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test')
    except Exception:
        exc = get_exception()
        if exc.args[0] != 'test':
            raise AssertionError("Expected 'test' as exception message, got %s" % (exc.args[0],))

# Generated at 2022-06-13 04:34:01.086767
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('yay')
    except:
        e = get_exception()
        assert e.__class__.__name__ == 'ValueError'
        assert str(e) == 'yay'

# Generated at 2022-06-13 04:34:04.288862
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except ZeroDivisionError:
        exception = get_exception()
    assert isinstance(exception, ZeroDivisionError)


# Generated at 2022-06-13 04:34:07.387003
# Unit test for function get_exception
def test_get_exception():
    def test_func():
        try:
            raise ValueError("This is a test")
        except:
            return get_exception()
    assert(test_func().args[0] == "This is a test")



# Generated at 2022-06-13 04:34:10.587849
# Unit test for function get_exception
def test_get_exception():
    class SpecialException(Exception):
        pass

    try:
        raise SpecialException
    except:
        e = get_exception()
        if not isinstance(e, SpecialException):
            raise Exception("get_exception() did not find the special exception")
    else:
        raise Exception("The raised exception did not get detected")

# Generated at 2022-06-13 04:34:12.436881
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError), \
            "The exception we received isn't the one we wanted: %s" % e

# Generated at 2022-06-13 04:34:49.250277
# Unit test for function get_exception
def test_get_exception():
    class Bogus(Exception):
        pass

    try:
        raise Bogus()
    except:
        exc_info = get_exception()
        assert isinstance(exc_info, Bogus)

# Generated at 2022-06-13 04:34:54.153430
# Unit test for function get_exception
def test_get_exception():
    """Unit test for function get_exception

    This unit test is not considered a part of the python versions compatibility
    code.  It'll be removed as soon as we can upgrade.
    """
    try:
        raise ValueError('Test error')
    except Exception:
        e = get_exception()
        assert e.args[0] == 'Test error'

# Generated at 2022-06-13 04:35:00.923528
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        exc = get_exception()
        assert exc.args == ('foo',)

        try:
            raise Exception('bar')
        except Exception:
            exc2 = get_exception()
            assert exc2.args == ('bar',)
            assert exc.args == ('foo',)
            assert exc is not exc2

# Generated at 2022-06-13 04:35:06.457648
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Exception 1")
    except:
        # Python 2.4 - 2.6
        e = get_exception()
        assert(str(e) == "Exception 1")
        assert(e.__class__.__name__ == "Exception")
    # Python 2.7+ doesn't execute the inner block
    # https://docs.python.org/2/reference/compound_stmts.html#the-try-statement

# Generated at 2022-06-13 04:35:08.918784
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('bar')
    except ValueError:
        exc = get_exception()

    assert type(exc) == ValueError
    assert exc.args == ('bar',)

# Generated at 2022-06-13 04:35:11.510820
# Unit test for function get_exception
def test_get_exception():
    def f1():
        try:
            foo()
        except Exception:
            e = get_exception()
            assert e.__class__.__name__ == 'NameError'
    f1()

# Generated at 2022-06-13 04:35:19.200695
# Unit test for function get_exception
def test_get_exception():
    def testfunc():
        try:
            x = 1
            y = 2
            z = x / y
        except ZeroDivisionError:
            import ansible.module_utils.basic
            e = ansible.module_utils.basic.get_exception()
            raise e

    try:
        testfunc()
    except Exception:
        e = get_exception()
        assert 'division by zero' in str(e)
    else:
        raise AssertionError('get_exception(): exception not raised')

# Generated at 2022-06-13 04:35:22.779580
# Unit test for function get_exception
def test_get_exception():
    t = type('test_get_exception_Type', (object,), {})
    try:
        raise t('test get exception')
    except:
        e = get_exception()
    assert isinstance(e, t)
    assert str(e) == 'test get exception'



# Generated at 2022-06-13 04:35:24.428823
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('bar')
    except Exception:
        e = get_exception()
        assert str(e) == 'bar'

# Generated at 2022-06-13 04:35:26.130173
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('oops')
    except:
        e = get_exception()
        assert e.args == ('oops',)

# Generated at 2022-06-13 04:36:41.258284
# Unit test for function get_exception
def test_get_exception():
    # Try to raise an exception and catch it
    try:
        raise Exception('Test exception')
    except Exception:
        e = get_exception()
        if str(e) != 'Test exception':
            raise AssertionError('Incorrect error message')

# Generated at 2022-06-13 04:36:42.870221
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        assert get_exception()


# Generated at 2022-06-13 04:36:44.745424
# Unit test for function get_exception
def test_get_exception():
    """Make sure that get_exception returns something
    """
    try:
        raise ValueError
    except:
        assert get_exception()


# Generated at 2022-06-13 04:36:53.987311
# Unit test for function get_exception
def test_get_exception():
    # The default exception raising behavior is to print the exception text
    # to stderr. Since we're testing if get_exception returns the correct value,
    # in this function we overwrite stderr so we can capture it.
    oldstderr = sys.stderr
    oldexc_info = sys.exc_info()

# Generated at 2022-06-13 04:36:55.441091
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception as e:
        result = get_exception()
    assert('foo' in str(result))

# Generated at 2022-06-13 04:37:02.850312
# Unit test for function get_exception
def test_get_exception():
    import logging
    import os

    logger = logging.getLogger('test_get_exception')

    try:
        raise Exception('Exception raised')
    except Exception:
        e = get_exception()
        logger.info('%s', type(e))
        logger.info('%s', e)

    # A variable that does not exist
    try:
        os.path.gettattr('fail_if_this_exists')
    except Exception:
        e = get_exception()
        logger.info('%s', type(e))
        logger.info('%s', e)

if __name__ == '__main__':
    import logging
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Test get_exception')

# Generated at 2022-06-13 04:37:06.617175
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=unused-variable
    try:
        raise Exception('foo')
    except:  # noqa: F811
        exc = get_exception()
    assert "foo" in str(exc)

# Generated at 2022-06-13 04:37:11.205467
# Unit test for function get_exception
def test_get_exception():
    import ansible.module_utils.pycompat24

    try:
        raise RuntimeError("get_exception() works")
    except Exception:
        e = ansible.module_utils.pycompat24.get_exception()
    assert "get_exception() works" in str(e)



# Generated at 2022-06-13 04:37:15.259855
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError()
    except ValueError:
        e = get_exception()
        assert type(e) == ValueError


# Generated at 2022-06-13 04:37:18.516534
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test')
    except:
        exception = get_exception()

    assert exception.args[0] == 'test', 'get_exception() did not capture the exception correctly'


# Generated at 2022-06-13 04:39:52.024108
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('An exception')
    except:
        assert get_exception().args[0] == 'An exception'



# Generated at 2022-06-13 04:39:55.228812
# Unit test for function get_exception
def test_get_exception():
    class MyBaseClass(Exception):
        pass
    class MyClass(MyBaseClass):
        pass


# Generated at 2022-06-13 04:40:00.168135
# Unit test for function get_exception
def test_get_exception():
    def func_with_exception():
        try:
            1 / 0
        except ZeroDivisionError:
            return get_exception()
    exc = func_with_exception()
    assert isinstance(exc, ZeroDivisionError)
    try:
        1 / 0
    except ZeroDivisionError:
        exc = get_exception()
    assert isinstance(exc, ZeroDivisionError)

# Generated at 2022-06-13 04:40:02.537609
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert e.__class__ == Exception
        assert str(e) == 'foo'


# Generated at 2022-06-13 04:40:04.555836
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test')
    except Exception: # pylint: disable=broad-except
        e = get_exception()

    assert type(e) == Exception
    assert str(e) == 'test'

# Generated at 2022-06-13 04:40:06.645603
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Get outta here!')
    except ValueError as e:
        assert get_exception() is e

# Unit tests for function literal_eval

# Generated at 2022-06-13 04:40:11.858239
# Unit test for function get_exception
def test_get_exception():
    try:
        raise NameError('Bob')
    except NameError:
        e = __import__('ansible.module_utils.common.exceptions', {}, {}, ['ansible', 'module_utils', 'common', 'exceptions'])
        e = e.get_exception()
    assert str(e) == 'Bob'
    assert repr(e) == "NameError('Bob',)"


# Generated at 2022-06-13 04:40:14.562017
# Unit test for function get_exception
def test_get_exception():
    import pytest
    try:
        raise ValueError('Test exception')
    except:
        exc = get_exception()
    assert isinstance(exc, ValueError)
    assert str(exc) == 'Test exception'

# Generated at 2022-06-13 04:40:18.025506
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass

    try:
        raise MyException('test')
    except MyException:
        exc = get_exception()
        assert exc.args == ('test', )

# Generated at 2022-06-13 04:40:23.288372
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('This is expected')
    except:
        expected = get_exception()
        assert expected

        try:
            raise RuntimeError('This is not expected')
        except:
            assert expected == get_exception()

            try:
                raise ValueError('This is not expected')
            except:
                assert expected == get_exception()


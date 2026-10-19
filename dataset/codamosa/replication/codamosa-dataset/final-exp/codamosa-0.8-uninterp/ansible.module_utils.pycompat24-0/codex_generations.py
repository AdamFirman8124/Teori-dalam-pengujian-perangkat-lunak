

# Generated at 2022-06-13 04:31:11.617884
# Unit test for function get_exception
def test_get_exception():
    e = get_exception()
    if e is not None:
        raise AssertionError("get_exception() should return None, "
                             "returned: %r" % (e,))

    try:
        raise RuntimeError("Error")
    except RuntimeError:
        e = get_exception()
    if not isinstance(e, RuntimeError):
        raise AssertionError("get_exception() should return a RuntimeError, "
                             "returned: %r" % (e,))


# Generated at 2022-06-13 04:31:14.036668
# Unit test for function get_exception
def test_get_exception():
    test_variable = 4
    try:
        # Create an exception
        test_variable.we_know_there_is_no_such_attribute
    except:
        exctype, excvalue = sys.exc_info()[:2]
        exc = get_exception()
        # Make sure the two ways of getting the exception are the same
        assert exctype == type(exc)
        assert excvalue == exc

# Generated at 2022-06-13 04:31:16.082952
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass

    try:
        raise MyException("Some Message")
    except MyException:
        e = get_exception()


# This unit test is based off of ast.literal_eval's unit test.

# Generated at 2022-06-13 04:31:21.037880
# Unit test for function get_exception
def test_get_exception():
    def fn():
        return 0/0
    try:
        fn()
    except:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)

# Unit tests for literal_eval

# Generated at 2022-06-13 04:31:24.439349
# Unit test for function get_exception
def test_get_exception():
    """Tests whether get_exception returns the exception object"""
    try:
        raise ValueError('test')
    except:
        assert get_exception() == ValueError('test')

# Generated at 2022-06-13 04:31:32.099720
# Unit test for function get_exception
def test_get_exception():
    import unittest
    import ansible.module_utils.pycompat as pycompat

    class FakeException(Exception):
        pass

    class TestGetException(unittest.TestCase):
        def test_exception(self):
            try:
                raise FakeException('Faux Exception')
            except Exception:
                e = pycompat.get_exception()
                self.assertTrue(isinstance(e, FakeException), repr(e))
                self.assertEqual(str(e), 'Faux Exception')
    return unittest.TestLoader().loadTestsFromTestCase(TestGetException)

# Generated at 2022-06-13 04:31:34.191412
# Unit test for function get_exception
def test_get_exception():
    class MyError(Exception):
        pass
    try:
        raise MyError('The message')
    except MyError:
        e = get_exception()
    assert str(e) == 'The message'
    assert isinstance(e, MyError)


# Generated at 2022-06-13 04:31:38.467156
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('some message')
    except:
        e = get_exception()
        if e.message != 'some message':
            raise Exception("get_exception doesn't return the last exception raised")


# Generated at 2022-06-13 04:31:41.748565
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except ValueError as e:
        assert get_exception() is e
    try:
        raise ValueError('foo')
    except ValueError:
        assert get_exception().args[0] == 'foo'



# Generated at 2022-06-13 04:31:50.083050
# Unit test for function get_exception
def test_get_exception():
    '''Test the get_exception function'''
    # Get the exception we expect
    try:
        raise ValueError('Test get_exception')
    except:
        ex = get_exception()
        pass
    # We don't care what the message is, just that the message
    # is the same as the exception we caught and the return value
    # is a ValueError
    assert isinstance(ex, ValueError)
    try:
        raise ex
    except:
        test_ex = get_exception()
        pass
    assert ex is test_ex

# Generated at 2022-06-13 04:32:08.671427
# Unit test for function get_exception
def test_get_exception():
    try:
        raise IOError()
    except IOError:
        assert get_exception()


# Generated at 2022-06-13 04:32:14.587237
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError('foo')
    except TypeError:
        tb = get_exception()

    assert repr(tb) == repr(TypeError('foo')), repr(tb)
    assert str(tb) == str(TypeError('foo')), str(tb)


# Generated at 2022-06-13 04:32:15.779670
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Test exception')
    except ValueError as e:
        assert e == get_exception()

# Generated at 2022-06-13 04:32:20.562904
# Unit test for function get_exception
def test_get_exception():  # pylint: disable=missing-docstring, no-self-use
    raise ValueError('message')

if __name__ == '__main__':
    import unittest

    class TestException(unittest.TestCase):
        def test_exception(self):
            try:
                test_get_exception()
            except ValueError:
                e = get_exception()
                assert e.args[0] == 'message'
            else:
                assert False

# Generated at 2022-06-13 04:32:24.521892
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except Exception:
        e = get_exception()
        if not isinstance(e, ValueError):
            raise Exception('Unexpected exception: %s' % e)



# Generated at 2022-06-13 04:32:27.607026
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except:
        e = get_exception()
    assert isinstance(e, ValueError)
    assert e.args == ('foo',)



# Generated at 2022-06-13 04:32:29.625122
# Unit test for function get_exception
def test_get_exception():
    try:
        raise
    except Exception:
        e = get_exception()
    assert e.__class__ == Exception

# Generated at 2022-06-13 04:32:32.004415
# Unit test for function get_exception
def test_get_exception():
    try:
        int('a')
    except:
        assert isinstance(get_exception(), ValueError)

# Generated at 2022-06-13 04:32:35.664320
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('This is a test')
    except ValueError:
        exception = get_exception()
        assert exception.args[0] == 'This is a test'


# Generated at 2022-06-13 04:32:37.768927
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except Exception:
        e = get_exception()
        assert isinstance(e, ValueError), e

# Generated at 2022-06-13 04:33:11.506739
# Unit test for function get_exception
def test_get_exception():
    try:
         raise RuntimeError()
    except Exception:
         e = get_exception()
    assert e.__class__ is RuntimeError

# Generated at 2022-06-13 04:33:16.574703
# Unit test for function get_exception
def test_get_exception():

    def function_raising_exception():
        raise Exception

    try:
        function_raising_exception()
    except Exception:
        assert Exception == get_exception().__class__

    class MyException(Exception): pass

    try:
        raise MyException
    except Exception:
        assert MyException == get_exception().__class__

# Generated at 2022-06-13 04:33:21.971347
# Unit test for function get_exception
def test_get_exception():
    def a_function_that_raises():
        raise Exception('just an error message')

    try:
        a_function_that_raises()
    except:
        e = get_exception()
        assert str(e) == 'just an error message'
        assert isinstance(e, Exception)

# Generated at 2022-06-13 04:33:22.962464
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except Exception:
        ex = get_exception()
    assert ex.args == ('foo',)

# Generated at 2022-06-13 04:33:27.226775
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=unused-argument,unnecessary-pass
    def run_test(thunk):
        def inner_run_test(thunk):
            try:
                thunk()
            except:
                return get_exception()
        return inner_run_test(thunk)


# Generated at 2022-06-13 04:33:30.317122
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('This is my exception')
    except:
        e = get_exception()
        assert e.args[0] == 'This is my exception'

# Generated at 2022-06-13 04:33:33.850766
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Emergency')
    except RuntimeError:
        e = get_exception()
        assert isinstance(e, RuntimeError)
        assert str(e) == 'Emergency'

# Generated at 2022-06-13 04:33:38.236846
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test exception')
    except ValueError as e:
        assert get_exception() == e
    try:
        raise ValueError('test exception')
    except ValueError:
        assert get_exception() == sys.exc_info()[1]

# Generated at 2022-06-13 04:33:46.740868
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Foo')
    except ValueError:
        e = get_exception()
        assert isinstance(e, ValueError)

        # Make sure that we aren't returning the current exception off the stack
        try:
            raise IndexError('Bar')
        except IndexError:
            e2 = get_exception()
            assert e is not e2

    try:
        raise ValueError('Foo')
    except ValueError:
        # another way to get an exception
        e = sys.exc_info()[1]
        assert isinstance(e, ValueError)



# Generated at 2022-06-13 04:33:51.057096
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Test Exception')
    except:
        e = get_exception()

    assert isinstance(e, ValueError)
    assert e.args == ('Test Exception',)



# Generated at 2022-06-13 04:34:27.719555
# Unit test for function get_exception
def test_get_exception():
    """
    >>> try:
    ...     raise ValueError(1)
    ... except Exception:
    ...     e = get_exception()
    ...     print(e)
    ...     print(type(e))
    ...     print(repr(e))
    ...
    1
    <class 'ValueError'>
    ValueError(1,)
    """
    pass

# Generated at 2022-06-13 04:34:30.129542
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError('foo')
    except TypeError as e:
        assert e == get_exception()



# Generated at 2022-06-13 04:34:36.586097
# Unit test for function get_exception
def test_get_exception():

    # Test that get_exception gets the exception raised
    try:
        raise Exception()
    except Exception as e:
        assert get_exception() is e

    # Test that get_exception gets the exception raised even if the exception
    # is swallowed by another except clause.
    try:
        try:
            raise Exception()
        except:
            raise AssertionError()
    except Exception as e:
        assert get_exception() is e

# Generated at 2022-06-13 04:34:39.455474
# Unit test for function get_exception
def test_get_exception():
    try:
        'foo' + 1
    except Exception:
        exc = get_exception()
    assert str(exc) == "'str' object cannot be interpreted as an index"



# Generated at 2022-06-13 04:34:41.108854
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Testing get_exception')
    except:
        ex = get_exception()

    assert 'Testing get_exception' in ex.args[0]

# Generated at 2022-06-13 04:34:43.554727
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        raise Exception('boom')

    try:
        raise_exception()
    except Exception:
        e = get_exception()
    assert str(e) == 'boom'

# Generated at 2022-06-13 04:34:47.510827
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        assert get_exception().args[0] == 'foo'


# Generated at 2022-06-13 04:34:50.246742
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError
    except TypeError:
        e = get_exception()
        assert isinstance(e, TypeError)


# Generated at 2022-06-13 04:34:52.874840
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=unreachable
    try:
        raise ValueError('foo')
    except ValueError:
        e = get_exception()
        assert str(e) == 'foo'
        return
    assert False, 'Should never reach this point'


# Generated at 2022-06-13 04:34:56.657445
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('testing get_exception')
    except Exception:
        e = get_exception()
    assert isinstance(e, Exception)
    assert e.args == ('testing get_exception',)



# Generated at 2022-06-13 04:36:02.540509
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except ZeroDivisionError:
        e = get_exception()

        assert e is not None
        assert e.__class__ is ZeroDivisionError


# Generated at 2022-06-13 04:36:04.120099
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        exc = get_exception()

    assert str(exc) == 'foo'
    assert repr(exc) == 'Exception("foo",)'
    assert type(exc) == Exception


# Generated at 2022-06-13 04:36:09.466135
# Unit test for function get_exception
def test_get_exception():
    import traceback

    try:
        int("foo")
    except ValueError:
        e = get_exception()
        t, v, b = sys.exc_info()
        assert e is v

    try:
        int("foo")
    except ValueError:
        e = get_exception()
        t, v, b = sys.exc_info()
        assert e is v
        assert str(e) == str(v)

    try:
        int("foo")
    except ValueError:
        e = get_exception()
        t, v, b = sys.exc_info()
        assert e is v
        assert repr(e) == repr(v)
        assert e.args == v.args


# Generated at 2022-06-13 04:36:10.566643
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("Testing")
    except:
        deet = get_exception()
    assert str(deet) == "Testing"

# Generated at 2022-06-13 04:36:11.858968
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        assert type(get_exception()) == ZeroDivisionError
    else:
        assert False, 'ZeroDivisionError not raised'

# Generated at 2022-06-13 04:36:16.333853
# Unit test for function get_exception
def test_get_exception():
    # A function that throws an exception
    def thrower():
        raise Exception("Test Exception")

    try:
        thrower()
    except Exception:
        # Get the current exception
        e = get_exception()

        # Make sure we can get the type and value of the exception
        assert(type(e) == Exception)
        assert(e.args[0] == "Test Exception")

# Generated at 2022-06-13 04:36:17.797489
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError()
    except ValueError as e:
        assert e is get_exception()

# Generated at 2022-06-13 04:36:21.674492
# Unit test for function get_exception
def test_get_exception():
    import io
    import sys
    import unittest

    class TestGetException(unittest.TestCase):
        def test_get_current_exception(self):
            try:
                raise ValueError
            except:
                self.assertEqual(get_exception(), sys.exc_info()[1])


# Generated at 2022-06-13 04:36:25.034513
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo bar')
    except ValueError:
        e = get_exception()
        assert str(e) == 'foo bar'



# Generated at 2022-06-13 04:36:32.617132
# Unit test for function get_exception
def test_get_exception():

    import copy

    class ExceptionClass(Exception):
        pass

    def fail():
        raise ExceptionClass('This is a failure')

    try:
        fail()
    except:
        try:
            fail()
        except:
            exc1 = get_exception()
        exc2 = sys.exc_info()[1]
        exc3 = copy.copy(exc2)
        exc4 = copy.deepcopy(exc2)

    for exc in (exc1, exc2, exc3, exc4):
        assert type(exc) == ExceptionClass
        assert str(exc) == 'This is a failure'


# Generated at 2022-06-13 04:39:01.549237
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("An exception")
    except Exception:
        e = get_exception()
    assert isinstance(e, Exception)
    assert str(e) == "An exception"



# Generated at 2022-06-13 04:39:03.869807
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test')
    except Exception:
        assert get_exception().args[0] == 'Test'


# Generated at 2022-06-13 04:39:13.365701
# Unit test for function get_exception
def test_get_exception():
    def f():
        def g():
            1/0
        g()

    try:
        f()
    except:
        exc = get_exception()

        # The traceback module prints the repr() of the string, so to test
        # that we're getting the right thing, we have to do the same thing
        assert str(exc) == repr(str(exc))
        assert type(str(exc)) is str
        assert len(str(exc))
        assert type(exc) is ZeroDivisionError

        # PyPy raises a different exception than CPython does.
        # The Actual exception can be either depending on the PyPy
        # compiled with.  Since PyPy raises a subclass of
        # ZeroDivisionError, we can just check for ZeroDivisionError's
        # existence in the hierarchy instead of checking for the
        # particular subclass that

# Generated at 2022-06-13 04:39:15.373633
# Unit test for function get_exception
def test_get_exception():
    try:
        x = 1 / 0
    except Exception:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)

# Generated at 2022-06-13 04:39:16.428918
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except:
        assert get_exception() is sys.exc_info()[1]

# Generated at 2022-06-13 04:39:21.339672
# Unit test for function get_exception
def test_get_exception():
    # Make sure we have a reference to an actual exception
    try:
        raise ValueError('foo')
    except ValueError:
        pass
    else:
        assert False, 'No exception raised'
    assert get_exception().args[0] == 'foo'

# Generated at 2022-06-13 04:39:28.661594
# Unit test for function get_exception
def test_get_exception():

    # Make sure calling get_exception() when there is no exception
    # doesn't do anything bad
    get_exception()

    # Make sure we can call get_exception() when there is an exception
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert str(e) == 'foo'



# Generated at 2022-06-13 04:39:30.351220
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Test exception text.")
    except RuntimeError as e:
        assert get_exception() == e



# Generated at 2022-06-13 04:39:32.803909
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        assert get_exception() == e


# Generated at 2022-06-13 04:39:39.505988
# Unit test for function get_exception
def test_get_exception():
    try:
        # Test the get_exception handles a caught exception
        raise Exception('hello world')
    except:
        e = get_exception()
        assert str(e) == 'hello world'

    # Test the get_exception handles an uncaught exception
    try:
        raise Exception('hello world')
    except:
        pass

    # This can't be caught by the except: above because test_get_exception
    # wasn't called within an except block.  So this will be caught by the base
    # class's except:
    try:
        test_get_exception()
    except BaseException as e:
        assert str(e) == "'NoneType' object is not callable"
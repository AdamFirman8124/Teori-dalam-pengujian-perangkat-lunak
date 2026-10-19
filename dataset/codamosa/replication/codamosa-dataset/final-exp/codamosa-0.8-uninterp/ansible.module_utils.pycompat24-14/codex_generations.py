

# Generated at 2022-06-13 04:31:07.796528
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('test')
    except RuntimeError:
        assert get_exception() == RuntimeError('test')


# Generated at 2022-06-13 04:31:10.698825
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("This is the exception")
    except Exception:
        exc = get_exception()
    assert exc.args == ("This is the exception",)



# Generated at 2022-06-13 04:31:16.638311
# Unit test for function get_exception
def test_get_exception():
    try:
        get_exception()
    except Exception as e:
        assert 'No exception currently active' == str(e)
    try:
        raise ValueError('Foo')
    except Exception as e:
        assert 'Foo' == str(get_exception())
        assert e is get_exception()
    try:
        raise ValueError('Foo')
    except Exception:
        e = get_exception()
        assert 'Foo' == str(e)
    assert 'No exception currently active' == str(get_exception())


# Generated at 2022-06-13 04:31:18.563534
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Test exception')
    except RuntimeError:
        assert get_exception() is sys.exc_info()[1]


# Generated at 2022-06-13 04:31:22.703631
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('hello world')
    except Exception:
        e = get_exception()
        assert str(e) == 'hello world'

# Generated at 2022-06-13 04:31:24.667007
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception as e:
        assert e == get_exception()

# Generated at 2022-06-13 04:31:27.782492
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except Exception:
        exc = get_exception()
        assert isinstance(exc, RuntimeError)
        assert exc.message == 'foo'



# Generated at 2022-06-13 04:31:31.407679
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("foo")
    except ValueError:
        exc = get_exception()

    assert isinstance(exc, ValueError)
    assert str(exc) == "foo"


# Generated at 2022-06-13 04:31:36.071196
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        raise ValueError(u'an exception just for testing')

    try:
        raise_exception()
    except:
        e = get_exception()

    assert e.args[0] == u'an exception just for testing'

# Generated at 2022-06-13 04:31:39.600803
# Unit test for function get_exception
def test_get_exception():
    def get_traceback():
        try:
            raise RuntimeError('xyz')
        except RuntimeError:
            return get_exception()

    assert 'xyz' in str(get_traceback())

# Generated at 2022-06-13 04:32:00.657772
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except ZeroDivisionError:
        exc = get_exception()
        assert exc.__class__ is ZeroDivisionError
        assert str(exc) == 'integer division or modulo by zero'

# Generated at 2022-06-13 04:32:02.533362
# Unit test for function get_exception
def test_get_exception():
    try:
        raise AssertionError('foo')
    except AssertionError:
        e = get_exception()
    assert isinstance(e, AssertionError)
    assert str(e) == 'foo'


# Generated at 2022-06-13 04:32:05.313598
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Test exception')
    except:
        e = get_exception()

    assert isinstance(e, ValueError)
    assert 'Test exception' in str(e)


# Generated at 2022-06-13 04:32:07.380990
# Unit test for function get_exception
def test_get_exception():
    def test():
        try:
            raise Exception(True)
        except Exception:
            e = get_exception()
        assert bool(e)
    test()



# Generated at 2022-06-13 04:32:09.934914
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Expected')
    except:
        exc = get_exception()
        assert isinstance(exc, Exception)
        assert str(exc) == 'Expected'

# Generated at 2022-06-13 04:32:14.183203
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        exc = get_exception()
    assert exc.__class__.__name__ == 'ZeroDivisionError'


# Generated at 2022-06-13 04:32:18.430718
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass
    try:
        raise MyException("testing")
    except MyException as exc:
        result = sys.exc_info()
        assert result == get_exception()
    finally:
        del exc
        #result = sys.exc_info()
        #assert result != get_exception()


# Generated at 2022-06-13 04:32:22.326889
# Unit test for function get_exception
def test_get_exception():
    e = None
    try:
        raise TypeError('foo')
    except Exception:
        e = get_exception()
    assert isinstance(e, TypeError)
    assert 'foo' in str(e)



# Generated at 2022-06-13 04:32:25.221661
# Unit test for function get_exception

# Generated at 2022-06-13 04:32:28.326543
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        exc = get_exception()
        assert type(exc) is Exception
        assert str(exc) == 'foo'
        assert repr(exc) == 'Exception(\'foo\',)'

# Generated at 2022-06-13 04:32:48.640435
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Exception!')
    except:
        exc = get_exception()
    assert exc.args[0] == 'Exception!'
    assert exc.__class__.__name__ == 'RuntimeError'

# Generated at 2022-06-13 04:32:52.367162
# Unit test for function get_exception
def test_get_exception():
    try:
        raise AttributeError('foo')
    except AttributeError as e:
        assert e is get_exception()

    try:
        raise ValueError('bar')
    except AttributeError:
        assert False, 'Previous exception should not be overwritten'
    except ValueError as e:
        assert e is get_exception()



# Generated at 2022-06-13 04:32:55.717839
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception:
        e = get_exception()
        assert e.__class__.__name__ == 'ZeroDivisionError'
        assert str(e) == 'integer division or modulo by zero'

# Generated at 2022-06-13 04:32:59.343401
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0  # pylint: disable=pointless-statement
    except ZeroDivisionError:
        e = get_exception()
        assert str(e) == 'division by zero'


# Generated at 2022-06-13 04:33:06.667161
# Unit test for function get_exception
def test_get_exception():
    # Python 3.x's io.StringIO will raise a TypeError if given bytes
    if sys.version_info < (3,):  # noqa
        try:
            raise TypeError('Hello')
        except TypeError as e:
            assert get_exception() is e
        else:
            assert False, "No exception raised?"
    else:
        try:
            raise TypeError('Hello')
        except TypeError:
            assert 'Hello' in str(get_exception())
        else:
            assert False, "No exception raised?"

# Generated at 2022-06-13 04:33:11.157760
# Unit test for function get_exception
def test_get_exception():
    def use_get_exception():
        try:
            int('wut', base=0)
        except Exception:
            e = get_exception()
            assert e.args == ("invalid literal for int() with base 0: 'wut'",)
            return e

    e = use_get_exception()
    assert e.args == ("invalid literal for int() with base 0: 'wut'",)

# Generated at 2022-06-13 04:33:13.132338
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception
    except Exception:
        e = get_exception()
        assert isinstance(e, Exception)

# Generated at 2022-06-13 04:33:15.268331
# Unit test for function get_exception

# Generated at 2022-06-13 04:33:19.837715
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception as e:
        #print(e)
        pass
    e = get_exception()
    assert e == ZeroDivisionError('integer division or modulo by zero',)

# Generated at 2022-06-13 04:33:23.081136
# Unit test for function get_exception
def test_get_exception():
    class TestException(Exception):
        pass

    try:
        raise TestException('hello')
    except TestException:
        e = get_exception()
        assert e.args[0] == 'hello'



# Generated at 2022-06-13 04:33:57.843015
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except Exception:
        e = get_exception()
        assert str(e) == 'foo'

# Generated at 2022-06-13 04:33:59.657315
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Test exception')
    except ValueError as e:
        assert e == get_exception()


# Generated at 2022-06-13 04:34:05.643765
# Unit test for function get_exception
def test_get_exception():
    class TestException(Exception):
        pass

    try:
        raise TestException('first')
    except TestException:
        e = get_exception()
        assert e.__class__ == TestException, "Wrong exception returned, got %s" % e
        assert str(e) == 'first', "Wrong exception message, got %s" % e
    #else:
    #    raise AssertionError('Should have thrown an exception')

# Generated at 2022-06-13 04:34:09.950957
# Unit test for function get_exception
def test_get_exception():
    """Test get_exception"""
    class MyException(Exception):
        pass

    try:
        raise MyException('Test')
    except:
        assert get_exception() is sys.exc_info()[1]
        e = get_exception()
    try:
        raise e
    except MyException:
        return
    assert False, 'get_exception failed to recreate the exception'


# Generated at 2022-06-13 04:34:12.500508
# Unit test for function get_exception
def test_get_exception():
    # First, check the case where we don't have an exception
    if not get_exception():
        try:
            raise Exception('This is a demonstration')
        except Exception:
            pass

    # Now we should have an exception
    assert get_exception()


# Generated at 2022-06-13 04:34:15.890119
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except ValueError:
        e = get_exception()
    assert e.__class__ is ValueError


# Generated at 2022-06-13 04:34:18.986164
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test')
    except Exception:
        e = get_exception()
        assert str(e) == 'test'


# Generated at 2022-06-13 04:34:21.575191
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test exception')
    except:
        res = get_exception()

    assert isinstance(res, Exception)
    assert 'test exception' == str(res)

# Generated at 2022-06-13 04:34:24.742580
# Unit test for function get_exception
def test_get_exception():
    import pytest
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert e.args[0] == 'foo'



# Generated at 2022-06-13 04:34:27.409658
# Unit test for function get_exception
def test_get_exception():
    import os

    # Create a file that doesn't exist
    nonexistent_file = 'nonexistent_file'
    if os.path.exists(nonexistent_file):
        os.remove(nonexistent_file)
    try:
        # Try to open it as a file
        f = open(nonexistent_file)
    except:
        # Get the exception that occured
        e = get_exception()
    # Make sure the exception is the one we expect
    assert isinstance(e, IOError)



# Generated at 2022-06-13 04:35:36.388258
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('test message')
    except RuntimeError:
        e = get_exception()
        assert isinstance(e, RuntimeError)



# Generated at 2022-06-13 04:35:38.190555
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('b')
    except:
        exception = get_exception()
    assert exception.args[0] == 'b'



# Generated at 2022-06-13 04:35:40.463267
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Test exception')
    except Exception:
        e = get_exception()
    assert isinstance(e, RuntimeError)
    assert e.args == ('Test exception',)



# Generated at 2022-06-13 04:35:46.741552
# Unit test for function get_exception
def test_get_exception():  # pylint: disable=too-many-branches
    """Test that get_exception can get all the possible exceptions."""
    class MyException(Exception):
        """Sample Exception"""
        pass

    class MyException2(Exception):
        """Sample Exception"""
        pass

    class MyException3(Exception):
        """Sample Exception"""
        pass

    excs = (Exception, MyException, MyException2, MyException3)

    try:
        raise Exception('testing')
    except Exception:
        assert get_exception() == sys.exc_info()[1]
    try:
        raise Exception('testing')
    except:  # pylint: disable=bare-except
        assert get_exception() == sys.exc_info()[1]

# Generated at 2022-06-13 04:35:50.213918
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        e = get_exception()
        assert isinstance(e, ZeroDivisionError)
        assert e.args == ('integer division or modulo by zero',)

# Generated at 2022-06-13 04:35:55.599585
# Unit test for function get_exception
def test_get_exception():
    # Test that we can catch an exception and get the same exception back
    try:
        raise ValueError('foo')
    except ValueError:
        e = get_exception()
    assert isinstance(e, ValueError)
    assert e.args == ('foo',)

    # Test that we can catch an exception and get the same exception back
    # even if we raise it again
    try:
        raise ValueError('foo')
    except ValueError:
        e = get_exception()
        raise
    assert isinstance(e, ValueError)
    assert e.args == ('foo',)

# Generated at 2022-06-13 04:35:58.259633
# Unit test for function get_exception
def test_get_exception():
    """Unit test for function get_exception"""

    try:
        1/0
    except Exception:
        e = get_exception()

    assert e.__class__ is ZeroDivisionError

# Generated at 2022-06-13 04:36:00.434381
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Test exception')
    except RuntimeError:
        exc = get_exception()
        assert exc.message == 'Test exception'



# Generated at 2022-06-13 04:36:01.495528
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Something bad happened')
    except ValueError:
        e = get_exception()

    assert e.args == ('Something bad happened',)

# Generated at 2022-06-13 04:36:04.028919
# Unit test for function get_exception
def test_get_exception():
    def raise_f():
        try:
            1 / 0
        except ZeroDivisionError:
            return get_exception()

    e = raise_f()
    assert e.__class__ is ZeroDivisionError
    assert str(e)

# Generated at 2022-06-13 04:38:50.487848
# Unit test for function get_exception
def test_get_exception():
    try:
        raise SyntaxError('foo')
    except:
        e = get_exception()
    assert isinstance(e, SyntaxError)
    assert str(e) == 'foo'
    try:
        raise SyntaxError('bar')
    except:
        e = get_exception()
    assert isinstance(e, SyntaxError)
    assert str(e) == 'bar'
    try:
        raise SyntaxError('baz')
    except:
        e = get_exception()
    assert isinstance(e, SyntaxError)
    assert str(e) == 'baz'

# Generated at 2022-06-13 04:38:53.046913
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')

    except RuntimeError as e:
        e2 = get_exception()
        assert e == e2


# Generated at 2022-06-13 04:38:58.632413
# Unit test for function get_exception
def test_get_exception():
    class TestException(Exception):
        pass

    try:
        raise TestException('test')
    except TestException:
        e = get_exception()
    if isinstance(e, TestException) and str(e) == 'test':
        print('OK')
    else:
        print('NG')

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:39:02.053933
# Unit test for function get_exception
def test_get_exception():
    # You can't call test_get_exception from a test because tests are run
    # inside a try/except.  Run this from an interactive session to test
    # the test :)
    try:
        raise Exception('This is a test')
    except Exception:
        e = get_exception()
        assert isinstance(e, Exception)
        assert type(e) == Exception
        assert str(e) == 'This is a test'


# Generated at 2022-06-13 04:39:11.694684
# Unit test for function get_exception
def test_get_exception():
    (f1, f2, f3) = (None, None, None)

    try:
        f1 = get_exception()
    except:
        f1 = get_exception()

    try:
        raise ValueError("test_get_exception")
    except:
        f2 = get_exception()

    try:
        raise RuntimeError("test_get_exception")
    except:
        f3 = get_exception()

    assert f1 is None, "get_exception should return None if no exception occurred"
    assert f2.args[0] == 'test_get_exception', "get_exception should return the exception object"
    assert f3.args[0] == 'test_get_exception', "get_exception should return the exception object"



# Generated at 2022-06-13 04:39:17.575267
# Unit test for function get_exception
def test_get_exception():
    """
    Simple unit test for function get_exception
    """
    import unittest
    try:
        raise ValueError('bad')
    except:
        e = get_exception()

    class GetExceptionTest(unittest.TestCase):
        def test_get_exception(self):
            self.assertTrue(isinstance(e, ValueError))
            self.assertEqual(e.message, 'bad')
    t = GetExceptionTest()
    t.test_get_exception()

# Generated at 2022-06-13 04:39:20.366981
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        assert get_exception()



# Generated at 2022-06-13 04:39:23.952073
# Unit test for function get_exception

# Generated at 2022-06-13 04:39:28.736225
# Unit test for function get_exception
def test_get_exception():
    try:
        try:
            raise RuntimeError('oops!')
        except RuntimeError:
            e = get_exception()
        assert e.message == 'oops!'

    except AssertionError:
        raise AssertionError('assertion failed in test_get_exception()')


# Generated at 2022-06-13 04:39:36.407056
# Unit test for function get_exception
def test_get_exception():
    # Test that we can catch and retrieve exceptions
    # Use a global function on purpose so we can catch the exception without
    # overriding it on the function
    try:
        raise RuntimeError('Test Exception')
    except Exception:
        e = get_exception()
    assert e.args[0] == 'Test Exception'

    # Test that we can retrieve exceptions that were thrown out of a
    # function
    def raise_exception():
        raise RuntimeError('Test Exception')

    try:
        raise_exception()
    except Exception:
        e = get_exception()
    assert e.args[0] == 'Test Exception'

    # Test that we can re-raise the exception
    try:
        raise RuntimeError('Test Exception')
    except Exception:
        e = get_exception()
        raise e



# Generated at 2022-06-13 04:31:09.516411
# Unit test for function get_exception
def test_get_exception():
    try:
        try:
            # On Python 2.4-2.5, raise in a nested try/except block doesn't
            # propagate to the outer try/except block.
            raise Exception('foo')
        except Exception:
            e = get_exception()
            assert e.args[0] == 'foo'
        raise Exception('bar')
    except Exception:
        e = get_exception()
        assert e.args[0] == 'bar'

# Generated at 2022-06-13 04:31:16.407621
# Unit test for function get_exception
def test_get_exception():
    def foo(a=None, b=None):
        if a > b:
            raise Exception("a > b")

    def foo1():
        try:
            foo(3,2)
        except:
            return get_exception()

    e = foo1()
    assert(e.args[0] == 'a > b')

    def foo2():
        try:
            foo(2,3)
        except:
            return get_exception()

    e = foo2()
    assert(e.args[0] == None)

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:31:18.350401
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("test")
    except RuntimeError:
        e = get_exception()
        assert e.args[0] == "test"

# Generated at 2022-06-13 04:31:25.463606
# Unit test for function get_exception
def test_get_exception():
    try:
        sys.exc_info()
        assert False
    except Exception:
        got_exc = get_exception()
        assert type(got_exc) is Exception

if __name__ == '__main__':
    import pytest
    pytest.main(shlex.split(sys.argv[1]) + [os.path.basename(__file__)])

# Generated at 2022-06-13 04:31:33.557945
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        raise Exception('test')
    try:
        # pylint: disable=too-few-public-methods, missing-docstring
        class ExceptionSubclass(Exception):
            pass
        # pylint: enable=too-few-public-methods, missing-docstring
        raise ExceptionSubclass('test')
    except Exception as e:
        assert isinstance(get_exception(), ExceptionSubclass)
        assert get_exception() is e
        assert get_exception() == e
    try:
        raise_exception()
    except Exception as e:
        assert isinstance(get_exception(), Exception)
        assert get_exception() is e
        assert get_exception() == e


# Generated at 2022-06-13 04:31:38.670025
# Unit test for function get_exception
def test_get_exception():
    import types

    try:
        raise Exception('foo')
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        exc = get_exception()
        assert exc is not None
        assert exc is exc_value
        assert not isinstance(exc, types.StringType)

# Generated at 2022-06-13 04:31:43.729232
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except ZeroDivisionError as e:
        e2 = get_exception()
    assert e2 is e

if __name__ == '__main__':
    import unittest

    class TestGetException(unittest.TestCase):
        def test_get_exception(self):
            try:
                1 / 0
            except ZeroDivisionError as e:
                e2 = get_exception()
            self.assertEqual(e2, e)

    unittest.main()

# Generated at 2022-06-13 04:31:47.716764
# Unit test for function get_exception
def test_get_exception():
    class FooException(Exception):
        pass

    try:
        raise FooException('Testing')
    except FooException:
        assert 'Testing' in get_exception().args


# Generated at 2022-06-13 04:31:49.629839
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        e = get_exception()
        assert type(e) is Exception

# Generated at 2022-06-13 04:31:52.673820
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('boo')
    except RuntimeError:
        exc = get_exception()
        assert isinstance(exc, RuntimeError)
        assert exc.args == ('boo',)



# Generated at 2022-06-13 04:32:05.313213
# Unit test for function get_exception
def test_get_exception():
    # This is a placeholder that can be used later to add unit tests for the
    # get_exception function.
    try:
        raise Exception('dummy')
    except:
        try:
            foo()
        except:
            # py2.6 print('Got exception %s' % exc)
            print('Got exception %s' % get_exception())

# Generated at 2022-06-13 04:32:11.934267
# Unit test for function get_exception
def test_get_exception():
    try:
        x = 1 / 0
    except Exception:
        exc = get_exception()
        if exc.__class__.__name__ != 'ZeroDivisionError':
            raise AssertionError("Expected ZeroDivisionError, got %s" % exc)
        if exc.args != ():
            raise AssertionError("Expected (), got %r" % (exc.args,))


if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:32:15.040991
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except:
        ex = get_exception()
    assert str(ex) == 'foo'

# Generated at 2022-06-13 04:32:19.054031
# Unit test for function get_exception
def test_get_exception():
    """Test that the get_exception function works

    :raises AssertionError:  if the function doesn't work
    """
    try:
        raise Exception('Test exception')
    except:
        e = get_exception()

    assert isinstance(e, Exception)
    assert e.args[0] == 'Test exception'


# Generated at 2022-06-13 04:32:22.636340
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError()
    except Exception as e:
        assert e is e
    except:  # noqa: E722  pylint: disable=bare-except
        e = get_exception()
    assert e is not None

# Generated at 2022-06-13 04:32:26.813533
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except:
        e = get_exception()
    assert e.args[0] == 'foo', e.args[0]
test_get_exception()

# Generated at 2022-06-13 04:32:29.962907
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        ex = get_exception()
        assert ex.args[0] == 'foo'



# Generated at 2022-06-13 04:32:38.437785
# Unit test for function get_exception
def test_get_exception():
    """
    Test retrieving the exception
    """
    try:
        raise RuntimeError('Test RunTimeError')
    except RuntimeError as e:
        assert get_exception() == e, 'RuntimeError exception was not captured'
        assert get_exception() != NameError, 'NameError exception wasn\'t thrown'

    try:
        raise NameError('Test NameError')
    except NameError as e:
        assert get_exception() == e, 'NameError exception was not captured'
        assert get_exception() != RuntimeError, 'RunTimeError exception wasn\'t thrown'

# Generated at 2022-06-13 04:32:40.795982
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception:
        e = get_exception()
        assert type(e) == ZeroDivisionError


# Generated at 2022-06-13 04:32:47.163922
# Unit test for function get_exception
def test_get_exception():
    class FakeException(Exception):
        pass

    try:
        try:
            raise FakeException('foo bar')
        except Exception:
            e = get_exception()
            assert e.args[0] == 'foo bar'
            assert e.__class__.__name__ == 'FakeException'
    except:
        raise AssertionError('test_get_exception raised an exception')

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:33:07.600150
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass
    try:
        raise MyException('foo')
    except Exception:
        assert get_exception().args == ('foo',)
        try:
            raise get_exception()
        except MyException:
            pass
        else:
            assert False, 'Not able to raise new exception from previous'

# Generated at 2022-06-13 04:33:09.458564
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except Exception:
        value_error = get_exception()
    assert isinstance(value_error, ValueError)

# Generated at 2022-06-13 04:33:11.477726
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('boo')
    except:
        e = get_exception()
    assert(e.args[0] == 'boo')

# Generated at 2022-06-13 04:33:14.392930
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except ZeroDivisionError:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)
    try:
        a = []
        a[0]
    except IndexError:
        e = get_exception()
    assert isinstance(e, IndexError)


# Generated at 2022-06-13 04:33:20.263390
# Unit test for function get_exception
def test_get_exception():
    '''Dummy function to test get_exception'''
    try:
        raise Exception('This is a test of the emergency broadcast system')
    except Exception:
        e = get_exception()
    assert e.args == ('This is a test of the emergency broadcast system',)



# Generated at 2022-06-13 04:33:25.796990
# Unit test for function get_exception
def test_get_exception():
    class SomeError(Exception):
        pass
    m = 'This is an exception'
    try:
        raise SomeError(m)
    except Exception:
        e = get_exception()
        assert isinstance(e, SomeError)
        assert m == str(e)
    else:
        assert False, 'Exception not raised'



# Generated at 2022-06-13 04:33:28.426047
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception
    except Exception:
        exc = get_exception()
    assert exc.__class__ == Exception



# Generated at 2022-06-13 04:33:32.258268
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError('Unit test.')
    except TypeError:
        e = get_exception()
    assert isinstance(e, TypeError)
    assert str(e) == 'Unit test.'



# Generated at 2022-06-13 04:33:36.238956
# Unit test for function get_exception

# Generated at 2022-06-13 04:33:43.964642
# Unit test for function get_exception
def test_get_exception():  # pylint: disable=redefined-outer-name
    # pylint: disable=g-import-not-at-top
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class TestGetException(unittest.TestCase):

        def test_get_exception(self):  # pylint: disable=no-self-use
            try:
                raise ValueError('test')
            except:
                self.assertEqual(get_exception().args, ('test',))

# Generated at 2022-06-13 04:34:23.691392
# Unit test for function get_exception

# Generated at 2022-06-13 04:34:27.013719
# Unit test for function get_exception

# Generated at 2022-06-13 04:34:30.001064
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Test RuntimeError")
    except:
        assert isinstance(get_exception(), RuntimeError)

# Generated at 2022-06-13 04:34:31.971321
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError
    except RuntimeError as e:
        pass
    assert e == get_exception()

# Generated at 2022-06-13 04:34:35.355905
# Unit test for function get_exception
def test_get_exception():
    try:
        raise IndexError
    except IndexError:
        e = get_exception()
    assert e.__class__ is IndexError


# Generated at 2022-06-13 04:34:39.289577
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        raise ValueError('test exception')
    try:
        raise_exception()
    except Exception:
        e = get_exception()
    assert type(e) == ValueError
    assert e.args == ('test exception',)

# Generated at 2022-06-13 04:34:44.715546
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0     # pylint: disable=pointless-statement
    except ZeroDivisionError:
        e = get_exception()
        assert isinstance(e, ZeroDivisionError)
        assert e.args[0] == 'integer division or modulo by zero'
        assert e.args[0] in str(e)
        assert str(e) == 'integer division or modulo by zero'
    else:
        sys.stderr.write("No exception raised during test_get_exception")
        assert False


# Generated at 2022-06-13 04:34:50.853482
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Error_Test')
    except Exception:
        e = get_exception()
        assert str(e) == "Error_Test"


if __name__ == '__main__':
    import pytest
    pytest.main(sys.argv[1:])

# Generated at 2022-06-13 04:34:53.399278
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("Test exception msg")
    except ValueError:
        e = get_exception()
        assert e.args == ("Test exception msg",)



# Generated at 2022-06-13 04:34:56.517069
# Unit test for function get_exception
def test_get_exception():
    """Unit test for get_exception()."""
    try:
        raise RuntimeError('Test exception')
    except RuntimeError:
        exc = get_exception()
        assert str(exc) == 'Test exception'

# Generated at 2022-06-13 04:36:03.580859
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('This is a test')
    except Exception:
        e = get_exception()
        assert isinstance(e, Exception)
        assert str(e) == 'This is a test'


# Generated at 2022-06-13 04:36:05.045423
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Hello")
    except:
        exc = get_exception()

    assert str(exc) == "Hello"


# Generated at 2022-06-13 04:36:10.161542
# Unit test for function get_exception

# Generated at 2022-06-13 04:36:15.384879
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ZeroDivisionError
    except ZeroDivisionError as e:
        assert e is get_exception()
    try:
        raise ValueError
    except ValueError as e:
        assert e is get_exception()


if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-13 04:36:17.630310
# Unit test for function get_exception
def test_get_exception():
    try:
        raise IndexError('This is the error message')
    except Exception:
        e = get_exception()

    assert str(e) == 'This is the error message'
    assert isinstance(e, IndexError)



# Generated at 2022-06-13 04:36:20.777395
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except:
        e = get_exception()
        assert e.args[0] == 'foo'

if __name__ == '__main__':
    # Run unit test for function get_exception()
    test_get_exception()

# Generated at 2022-06-13 04:36:28.753565
# Unit test for function get_exception
def test_get_exception():
    '''
    Test that get_exception returns the current exception.
    '''
    try:
        1 / 0
    except ZeroDivisionError:
        exc = get_exception()
        # Python 2.4-2.5, the exception is an instance of class
        # exceptions.ZeroDivisionError
        # Python 3, the exception is an instance of class ZeroDivisionError
        assert exc.__class__.__name__ in ('ZeroDivisionError',
                'exceptions.ZeroDivisionError')
    return None

# Generated at 2022-06-13 04:36:30.758366
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError()
    except ValueError:
        e = get_exception()
        assert e.__class__ == ValueError

# Generated at 2022-06-13 04:36:33.280339
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert str(e) == 'foo'

# Generated at 2022-06-13 04:36:36.707750
# Unit test for function get_exception
def test_get_exception():
    class TestException(Exception):
        pass

    try:
        raise TestException('test')
    except:
        e = get_exception()
    assert e.args == ('test',)
    assert type(e) is TestException



# Generated at 2022-06-13 04:37:44.810172
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test_exception')
    except:
        e = get_exception()


# Generated at 2022-06-13 04:37:50.093960
# Unit test for function get_exception
def test_get_exception():
    """Unit test for get_exception"""
    try:
        raise Exception('test_get_exception message')
    except Exception:
        e = get_exception()
    assert e.args == ('test_get_exception message',)


# Generated at 2022-06-13 04:37:53.664467
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError('get_exception')
    except TypeError:
        e = get_exception()
        re = repr(e)
        assert re == "TypeError('get_exception',)"
        te = str(e)
        assert te == 'get_exception'

# Generated at 2022-06-13 04:37:55.776369
# Unit test for function get_exception
def test_get_exception():
    try:
        raise AssertionError()
    except AssertionError:
        e = get_exception()
    assert isinstance(e, AssertionError)

# Generated at 2022-06-13 04:37:59.884843
# Unit test for function get_exception
def test_get_exception():
    err = None
    try:
        raise ValueError('foobar')
    except ValueError:
        err = get_exception()

    # Since we're getting the exception this way, the traceback won't be set
    # in the exception object.  So, only compare the type and message.
    assert isinstance(err, ValueError)
    assert err.args == ('foobar',)



# Generated at 2022-06-13 04:38:02.429893
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('this is an exception')
    except Exception as e:
        assert e == get_exception()

    try:
        raise ValueError('this is a ValueError')
    except ValueError as e:
        assert e == get_exception()



# Generated at 2022-06-13 04:38:04.294537
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("foo")
    except Exception:
        e = get_exception()
        print("e is: %s" % str(e))
        assert(str(e) == "foo")



# Generated at 2022-06-13 04:38:06.536405
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except ZeroDivisionError:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)



# Generated at 2022-06-13 04:38:10.353698
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('not a real error')
    except Exception:
        pass
    assert get_exception().args[0] == 'not a real error'



# Generated at 2022-06-13 04:38:15.420503
# Unit test for function get_exception
def test_get_exception():
    def test_func():
        try:
            raise ValueError('Foo')
        except Exception:
            got_exception = get_exception()

        assert isinstance(got_exception, ValueError), 'Got the wrong exception!'
        assert got_exception.args == ('Foo',), 'Got the wrong exception!'

    test_func()

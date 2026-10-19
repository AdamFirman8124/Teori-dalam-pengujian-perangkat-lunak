

# Generated at 2022-06-13 04:31:04.862004
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test exception')
    except Exception:
        ex = get_exception()

    assert ex.args == ('Test exception',)

# Generated at 2022-06-13 04:31:08.894653
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('This is a test exception')
    except Exception:
        e = get_exception()
    assert type(e) == Exception
    assert e.args == ('This is a test exception', )
    assert str(e) == 'This is a test exception'

# Generated at 2022-06-13 04:31:13.520347
# Unit test for function get_exception
def test_get_exception():
    '''Unit test for function get_exception'''
    from ansible.module_utils.six import StringIO

    # First test it works correctly on Python 2.6+
    output_start = StringIO()
    try:
        raise NameError('name')
    except NameError as exc:
        e = get_exception()
        print(e, file=output_start)
    output_start_value = output_start.getvalue()

    # Now test it on Python 2.4
    output = StringIO()
    try:
        raise NameError('name')
    except NameError:
        e = get_exception()
        print(e, file=output)
    output_value = output.getvalue()

    # If we're on Python 2.6+, then get_exception should have returned the
    # exception. 

# Generated at 2022-06-13 04:31:15.886586
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Unit test exception')
    except Exception:
        e = get_exception()
    assert type(e) == Exception
    assert e.args == ('Unit test exception',)

# Generated at 2022-06-13 04:31:17.782296
# Unit test for function get_exception
def test_get_exception():
    """Make sure that get_exception always returns the current exception"""
    try:
        raise Exception('blah')
    except Exception:
        e = get_exception()
    assert e.message == 'blah'

# Generated at 2022-06-13 04:31:20.579796
# Unit test for function get_exception
def test_get_exception():
    '''Test method get_exception'''
    try:
        raise Exception('Test exception')
    except:
        # pylint: disable=bare-except
        exception = get_exception()
        assert isinstance(exception, Exception)
        assert 'Test exception' == exception.message


# Generated at 2022-06-13 04:31:24.862968
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError("Hi!")
    except TypeError:
        e = get_exception()
    assert e.args == ("Hi!",)
    assert isinstance(e, TypeError)



# Generated at 2022-06-13 04:31:27.950557
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("A test exception")
    except ValueError:
        e = get_exception()
        assert e.args[0] == "A test exception"



# Generated at 2022-06-13 04:31:31.794705
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test exception')
    except:
        exc = get_exception()
        assert exc.args[0] == 'test exception'
        assert str(exc) == 'test exception'

# Generated at 2022-06-13 04:31:35.349365
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test error')
    except Exception:
        e = get_exception()
        assert type(e) == ValueError
        assert str(e) == 'test error'

# Generated at 2022-06-13 04:31:57.089825
# Unit test for function get_exception
def test_get_exception():
    try:
        int('asdf')
    except Exception:
        exctype, excobj, tb = sys.exc_info()
        assert exctype == type(get_exception())
        assert exctype == type(get_exception())

# Generated at 2022-06-13 04:32:01.310150
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        e = get_exception()
        if e.__class__ != Exception:
            raise AssertionError("get_exception() doesn't return an exception on Python 2.4")



# Generated at 2022-06-13 04:32:03.632572
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Ansible foo module')
    except RuntimeError as e:
        assert get_exception() == e

# Generated at 2022-06-13 04:32:05.402099
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test')
    except Exception:
        e = get_exception()

    assert e.args == ('Test',)


# Generated at 2022-06-13 04:32:16.184353
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):

        def __init__(self, message):
            self.message = message

        def __str__(self):
            return self.message

    try:
        raise MyException('foo')
    except Exception:
        # Python 2.6+
        exc = sys.exc_info()[1]
        # pylint: disable=unpacking-non-sequence
        type_, value, traceback = sys.exc_info()
        assert type_ is MyException
        assert isinstance(value, MyException)
        assert value.message == 'foo'
    else:
        assert False, 'Exception not raised'

    try:
        raise MyException('foo')
    except Exception:
        exc = get_exception()
        assert isinstance(exc, MyException)
        assert exc.message == 'foo'

# Generated at 2022-06-13 04:32:19.359310
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("This is a test of the get_exception function")
    except RuntimeError:
        exc_info = get_exception()
    assert exc_info.args[0] == "This is a test of the get_exception function"

# Generated at 2022-06-13 04:32:22.941467
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=unused-argument,missing-docstring
    try:
        1 / 0
    except:
        exc = get_exception()
    assert exc.__doc__.startswith("ZeroDivisionError(")

# Generated at 2022-06-13 04:32:25.736441
# Unit test for function get_exception

# Generated at 2022-06-13 04:32:28.394104
# Unit test for function get_exception
def test_get_exception():
    """Simple test to make sure get_exception() works"""
    try:
        raise KeyError
    except KeyError:
        e = get_exception()

    assert isinstance(e, KeyError)



# Generated at 2022-06-13 04:32:35.897075
# Unit test for function get_exception
def test_get_exception():
    try:
        int('a')
    except Exception:
        e = get_exception()
        try:
            assert isinstance(e, ValueError)
            assert "invalid literal for int() with base 10" in str(e)
        except AssertionError:
            raise AssertionError("get_exception() did not return the current exception")
    else:
        raise AssertionError("get_exception() did not return the current exception")



# Generated at 2022-06-13 04:33:10.828350
# Unit test for function get_exception
def test_get_exception():
    def fail():
        raise RuntimeError("Test error")

    try:
        fail()
    except RuntimeError as e:
        assert(get_exception() == e)


# Generated at 2022-06-13 04:33:12.250118
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError()
    except RuntimeError:
        e = get_exception()
    assert isinstance(e, RuntimeError)

# Generated at 2022-06-13 04:33:17.561771
# Unit test for function get_exception
def test_get_exception():
    def inner():
        raise TypeError("this is a test")

    def outer():
        try:
            inner()
        except Exception:
            return get_exception()

    result = outer()
    assert isinstance(result, TypeError)
    assert result.args == ("this is a test",)

# Generated at 2022-06-13 04:33:25.085775
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError()
    except RuntimeError:
        e = get_exception()
        assert str(type(e)) == "<type 'exceptions.RuntimeError'>"
        assert e.args == tuple()

    try:
        raise RuntimeError("testing")
    except RuntimeError:
        e = get_exception()
        assert str(type(e)) == "<type 'exceptions.RuntimeError'>"
        assert e.args == ("testing",)

# Generated at 2022-06-13 04:33:27.427563
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError("foo")
    except TypeError as e:
        assert get_exception() is e


# Generated at 2022-06-13 04:33:30.537319
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)


# Generated at 2022-06-13 04:33:33.710729
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test exception')
    except Exception:
        e = get_exception()
    assert str(e) == 'Test exception'



# Generated at 2022-06-13 04:33:36.448475
# Unit test for function get_exception
def test_get_exception():
    try:
        raise KeyError('blah')
    except KeyError as e:
        assert e == get_exception()


# Generated at 2022-06-13 04:33:40.168349
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('test')
    except RuntimeError:
        e = get_exception()
        print(e)
    try:
        raise ValueError('test2')
    except:
        e = get_exception()
        print(e)

# Generated at 2022-06-13 04:33:43.917484
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('hi there test')
    except:
        e = get_exception()
    assert isinstance(e, Exception)
    assert 'hi there test' in e



# Generated at 2022-06-13 04:34:55.016892
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Test exception")
    except:
        e = get_exception()
    assert e.args == ("Test exception",)



# Generated at 2022-06-13 04:35:01.128370
# Unit test for function get_exception
def test_get_exception():
    """Ensure that get_exception can retrieve an exception during a
    function call.
    """
    def func():
        raise Exception('foo')

    try:
        func()
    except:
        exception = get_exception()
        if str(exception) != 'foo':
            raise Exception("Exception was not saved properly")


# Generated at 2022-06-13 04:35:03.994439
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('oops')
    except:
        e = get_exception()
        assert str(e) == 'oops'



# Generated at 2022-06-13 04:35:10.153924
# Unit test for function get_exception
def test_get_exception():
    ''' Unit test for function get_exception
    '''
    # Simple check
    try:
        raise RuntimeError("test_get_exception")
    except RuntimeError:
        et, ev, tb = sys.exc_info()
        e = get_exception()
        assert(type(e) == RuntimeError)
        assert(e.__class__ == RuntimeError)

    # Check that it works more than once
    try:
        raise RuntimeError("test_get_exception")
    except RuntimeError:
        et, ev, tb = sys.exc_info()
        e = get_exception()
        assert(type(e) == RuntimeError)
        assert(e.__class__ == RuntimeError)



# Generated at 2022-06-13 04:35:13.150424
# Unit test for function get_exception
def test_get_exception():
    try:
        a = 1 / 0
    except Exception:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)



# Generated at 2022-06-13 04:35:15.535242
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception as e:
        assert get_exception() == e


# Generated at 2022-06-13 04:35:18.001253
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test')
    except:
        e = get_exception()
        assert isinstance(e, ValueError)

# Generated at 2022-06-13 04:35:22.861502
# Unit test for function get_exception
def test_get_exception():
    def test_code():
        try:
            try:
                raise TypeError('hi')
            except Exception:
                e = get_exception()
            else:
                e = None
            return e

        except Exception:
            return get_exception()
    assert test_code().args == ('hi',)

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:35:24.222971
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except:
        return get_exception()


# Generated at 2022-06-13 04:35:25.789360
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        assert get_exception()


# Generated at 2022-06-13 04:36:42.159340
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test')
    except Exception:
        e = get_exception()
    assert e.args == ('test',)

# Generated at 2022-06-13 04:36:44.701550
# Unit test for function get_exception
def test_get_exception():
    """Get the current exception should get the current exception.
    """
    try:
        raise ValueError()
    except:
        exc = get_exception()
    assert isinstance(exc, ValueError)



# Generated at 2022-06-13 04:36:48.235657
# Unit test for function get_exception
def test_get_exception():
    def func1():
        try:
            1 / 0
        except ZeroDivisionError:
            return get_exception()

    assert isinstance(func1(), ZeroDivisionError)



# Generated at 2022-06-13 04:36:49.939697
# Unit test for function get_exception
def test_get_exception():
    def f():
        try:
            raise Exception()
        except:
            return get_exception()
    assert f()

# Generated at 2022-06-13 04:36:53.289479
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('An exception')
    except Exception:
        e = get_exception()
        assert str(e) == 'An exception', "get_exception() returned %r (type: %s), which does not contain 'An exception'" % (e, type(e))

# Generated at 2022-06-13 04:36:55.107381
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)


# Generated at 2022-06-13 04:37:02.528369
# Unit test for function get_exception
def test_get_exception():
    """Test the get_exception function"""
    # pylint: disable=import-error,too-few-public-methods
    # Import error because we're importing a class that imports a module that's not available
    # on all platforms so pylint reports an error.  Too few public methods because we only
    # have one and pylint shows an error for that as well.

    from ansible.module_utils.six import PY3

    class ClassException(Exception):
        """Dummy exception class"""

    # pylint: enable=import-error,too-few-public-methods

    # This code needs to work on Python 2.4 through 3.x, so we cannot use
    # "except Exception, e:" (SyntaxError on Python 3.x) nor
    # "except Exception as e:" (SyntaxError on Python 2

# Generated at 2022-06-13 04:37:06.179255
# Unit test for function get_exception
def test_get_exception():
    try:
        raise AssertionError('foo')
    except AssertionError:
        exc = get_exception()
        assert exc.args[0] == 'foo'


# Generated at 2022-06-13 04:37:17.989176
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Test exception")
    except Exception:
        e = get_exception()
        assert str(e) == "Test exception"

# Imitate ansible/module_utils/text.py
#FIXME: this should be in a file which resides in module_utils/text.py
# rather than duplicated in core and module_utils.
try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()
try:
    unicode
except NameError:
    # Python 3
    basestring = str
    unicode = str
    long = int
    display_warning = display.display_warning
else:
    # Python 2.x
    display_warning = display.warning

# Generated at 2022-06-13 04:37:23.561466
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Test exception')
    except RuntimeError as e:
        # Check that the excpetion object we got from get_exception() is
        # the same we got from raising the exception with 'as e':
        assert get_exception() is e
    try:
        raise RuntimeError('Test exception')
    except RuntimeError:
        # Check that the excpetion object we got from get_exception() is
        # is an instance of RuntimeError
        assert isinstance(get_exception(), RuntimeError)

# Generated at 2022-06-13 04:38:48.001688
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except RuntimeError:
        e = get_exception()
        assert 'foo' == e.args[0]

# Generated at 2022-06-13 04:38:55.400227
# Unit test for function get_exception
def test_get_exception():
    import types
    try:
        1 / 0
    except ZeroDivisionError:
        # zero division error should be the type
        assert get_exception() is get_exception()
        assert isinstance(get_exception(), ZeroDivisionError)
        assert isinstance(get_exception(), types.InstanceType)

    assert get_exception() is not get_exception()
    assert isinstance(get_exception(), ZeroDivisionError)
    assert isinstance(get_exception(), types.InstanceType)



# Generated at 2022-06-13 04:38:59.188733
# Unit test for function get_exception
def test_get_exception():
    def raise_exc():
        raise ValueError("This is the exception")
    try:
        raise_exc()
    except:
        exc = get_exception()
    assert isinstance(exc, ValueError)
    assert str(exc) == "This is the exception"



# Generated at 2022-06-13 04:39:02.813929
# Unit test for function get_exception
def test_get_exception():
    # Catch an exception and make sure it's the correct exception
    try:
        raise ValueError('This is a test')
    except ValueError:
        exc = get_exception()
        assert exc.args[0] == 'This is a test'


# Generated at 2022-06-13 04:39:04.950824
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Test exception")
    except Exception:
        e = get_exception()
        assert "Test exception" in str(e)


# Generated at 2022-06-13 04:39:12.454463
# Unit test for function get_exception
def test_get_exception():
    import unittest
    try:
        raise TypeError('test_get_exception')
    except TypeError:
        err = get_exception()
    class T(unittest.TestCase):
        def test(self):
            self.assertEquals(str(err), 'test_get_exception')
    suite = unittest.TestLoader().loadTestsFromTestCase(T)
    result = unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise Exception('test_get_exception failed')

# Generated at 2022-06-13 04:39:16.292642
# Unit test for function get_exception
def test_get_exception():
    import errno


# Generated at 2022-06-13 04:39:23.466124
# Unit test for function get_exception
def test_get_exception():
    class TestException1(Exception):
        pass

    class TestException2(Exception):
        pass

    try:
        raise TestException1('test')
    except:
        ex = get_exception()
        assert isinstance(ex, TestException1)

    try:
        raise TestException2('test')
    except:
        ex = get_exception()
        assert isinstance(ex, TestException2)


# Generated at 2022-06-13 04:39:27.312979
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except ValueError:
        e = get_exception()
    assert isinstance(e, ValueError)
    assert e.args == ('foo',)

# Generated at 2022-06-13 04:39:31.830817
# Unit test for function get_exception
def test_get_exception():
    def raises_new():
        raise RuntimeError('A new exception')

    def wraps_old():
        try:
            raises_new()
        except:
            return get_exception()

    def raises_old():
        raise wraps_old()

    try:
        raises_new()
    except RuntimeError as e_new:
        pass
    try:
        raises_old()
    except RuntimeError as e_old:
        pass
    assert e_new is e_old


# Generated at 2022-06-13 04:31:08.867717
# Unit test for function get_exception
def test_get_exception():
    '''
    Test function get_exception
    '''
    def inner_exception(raise_exception):
        try:
            raise Exception('This is the inner exception')
        except:
            if raise_exception:
                raise
            return get_exception()

    def outer_exception():
        try:
            inner_exception(True)
        except:
            return get_exception()

    raised_exc = outer_exception()
    caught_exc = inner_exception(False)

    assert raised_exc.args == caught_exc.args

# Generated at 2022-06-13 04:31:13.380443
# Unit test for function get_exception
def test_get_exception():
    try:
        try:
            raise ValueError('value')
        except:
            e = get_exception()
            if str(e) != 'value':
                raise RuntimeError("get_exception() returned a different exception than the current exception")
    except RuntimeError as e:
        raise AssertionError('test_get_exception failed: ' + str(e))

# Generated at 2022-06-13 04:31:17.205418
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        e = get_exception()
        assert e.__class__ == Exception


# Generated at 2022-06-13 04:31:22.127361
# Unit test for function get_exception

# Generated at 2022-06-13 04:31:26.763049
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except Exception:
        e = get_exception()
    assert e.__class__.__name__ == 'ZeroDivisionError'
    assert str(e) == 'integer division or modulo by zero'
    assert repr(e) == 'ZeroDivisionError()'


# Generated at 2022-06-13 04:31:30.605673
# Unit test for function get_exception
def test_get_exception():
    def _raise(exc):
        # This could be 'raise exc' but that's illegal syntax in Python 2.4.
        raise exc

    def _catch(exc):
        try:
            _raise(exc)
        except Exception:
            return get_exception()

    assert _catch(ValueError()) == _catch(ValueError())



# Generated at 2022-06-13 04:31:36.216347
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foobar')
    except Exception:
        e = get_exception()
        assert str(e) == 'foobar'
    except: # pragma: no cover
        assert False, "get_exception() raised an exception outside of the context of another exception"



# Generated at 2022-06-13 04:31:44.301143
# Unit test for function get_exception
def test_get_exception():

    # First try it with a simple exception
    def test():
        1/0
    try:
        test()
    except:
        e = get_exception()
        if e.args[0] != "integer division or modulo by zero":
            raise Exception("get_exception didn't get the exception")
        if sys.version_info[0] == 3:
            if str(type(e)) != "<class 'ZeroDivisionError'>":
                raise Exception("get_exception didn't get the right exception type (%s)" % str(type(e)))
        else:
            if str(type(e)) != "<type 'exceptions.ZeroDivisionError'>":
                raise Exception("get_exception didn't get the right exception type (%s)" % str(type(e)))

    # Now try it using a different exception type so that we

# Generated at 2022-06-13 04:31:55.788407
# Unit test for function get_exception
def test_get_exception():
    def test_exception(exception_type):
        try:
            raise exception_type()
        except:
            e = get_exception()
            if not isinstance(e, exception_type):
                raise Exception("Didn't get expected exception type")

    all_exceptions = (TypeError, ValueError, ImportError, IndexError,
            IOError, OSError, KeyError, NameError, AssertionError)
    for exception_type in all_exceptions:
        test_exception(exception_type)

    # Make sure we get the last exception if there are multiple ones

# Generated at 2022-06-13 04:31:58.765445
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Exception message")
    except Exception:
        e = get_exception()
    assert str(e) == "Exception message"


# Generated at 2022-06-13 04:32:17.428979
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        exception = get_exception()
        assert 'foo' in str(exception)

# Generated at 2022-06-13 04:32:25.322929
# Unit test for function get_exception
def test_get_exception():
    def raising():
        raise ValueError('Testing')

    try:
        raising()
    except ValueError:
        e = get_exception()
    assert e.args[0] == 'Testing'

    try:
        literal_eval()
    except TypeError:
        e = get_exception()
    assert e.args[0] == 'literal_eval() takes exactly 1 argument (0 given)'

# Generated at 2022-06-13 04:32:28.914975
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test exception')
    except Exception:
        e = get_exception()
    assert isinstance(e, Exception), ('test_get_exception', 'test exception')
    assert str(e) == 'test exception', ('test_get_exception', 'test exception')

# Generated at 2022-06-13 04:32:34.604854
# Unit test for function get_exception
def test_get_exception():
    def fn1():
        raise Exception('exception message')
    def fn2():
        try:
            fn1()
        except Exception:
            return get_exception()
    e = fn2()
    assert e.args == ('exception message',)
    assert str(e) == 'exception message'


# Generated at 2022-06-13 04:32:37.598805
# Unit test for function get_exception
def test_get_exception():
    class FooError(Exception):
        pass

    try:
        raise FooError
    except:
        e = get_exception()
    assert isinstance(e, FooError)


# Generated at 2022-06-13 04:32:39.874812
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Dummy exception')
    except ValueError:
        e = get_exception()
        assert str(e) == 'Dummy exception'


# Generated at 2022-06-13 04:32:44.835727
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        raise Exception('test_get_exception exception message')

    try:
        raise_exception()
    except:
        exception = get_exception()
    assert isinstance(exception, Exception)
    assert 'test_get_exception exception message' in str(exception), '%s' % exception


# Generated at 2022-06-13 04:32:46.704110
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except:
        e = get_exception()

    assert isinstance(e, ValueError)


# Generated at 2022-06-13 04:32:49.847569
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except ValueError:
        result = get_exception()
        assert isinstance(result, ValueError)
        assert result.args == ('foo',)



# Generated at 2022-06-13 04:32:52.788245
# Unit test for function get_exception
def test_get_exception():
    # A no-op test to make sure that the method compiles under Python 3
    try:
        raise Exception('test_get_exception')
    except:
        e = get_exception()
    assert (e.args[0] == 'test_get_exception')
    return

# Generated at 2022-06-13 04:33:26.719073
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Test")
    except:
        e = get_exception()
        assert str(e) == "Test"

# Generated at 2022-06-13 04:33:30.922421
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Testing get_exception()')
    except:
        e = get_exception()
        assert e.args == ('Testing get_exception()',)
        assert str(e)
        assert repr(e)


# Generated at 2022-06-13 04:33:33.756982
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()

    assert(e.message == 'foo')

# Generated at 2022-06-13 04:33:37.806821
# Unit test for function get_exception
def test_get_exception():
    class BogusException(Exception):
        pass

    try:
        raise BogusException('bogus')
    except BogusException:
        exc = get_exception()
    assert exc.args[0] == 'bogus'

# Generated at 2022-06-13 04:33:39.993610
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError
    except Exception:
        e = get_exception()
        assert(isinstance(e, RuntimeError))



# Generated at 2022-06-13 04:33:43.712965
# Unit test for function get_exception
def test_get_exception():
    def foo():
        raise Exception('test exception')
    try:
        foo()
    except Exception:
        returned = get_exception()
        assert returned.args[0] == 'test exception'


# Generated at 2022-06-13 04:33:46.739875
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        raise NameError('foo')

# Generated at 2022-06-13 04:33:50.690299
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except Exception:
        e = get_exception()
        assert isinstance(e, ZeroDivisionError)
    else:
        assert False

# Generated at 2022-06-13 04:33:53.437506
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('boo')
    except Exception:
        e = get_exception()
        assert str(e) == 'boo'
        assert repr(e) == 'Exception(\'boo\',)'


# Generated at 2022-06-13 04:33:56.897712
# Unit test for function get_exception
def test_get_exception():
    '''Test getting the current exception

    This function is defined in the module so that it can be unit tested.
    '''
    try:
        raise Exception('Test exception')
    except Exception:
        e = get_exception()
        assert e.args == ('Test exception',)

# Generated at 2022-06-13 04:34:37.203040
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except:
        e = get_exception()

    # Test: In python2 we have an actual exception here
    assert type(e) == ValueError
    assert str(e) == 'foo'

    # Test: In python3, this exception has been reraised, so we have a string
    e = get_exception()
    assert type(e) == str
    assert e == 'foo'


# Generated at 2022-06-13 04:34:45.327352
# Unit test for function get_exception
def test_get_exception():
    '''
    Unit test for get_exception
    '''
    # pylint: disable=unused-variable,unused-argument,expression-not-assigned,singleton-comparison,unreachable

    # Raising the exception inside a function means we can capture the
    # exception on Python 2.x without it printing to stderr
    def raise_exc():
        try:
            raise ValueError('Exception')
        except Exception:
            e = get_exception()

    try:
        raise_exc()
    except Exception:
        e = get_exception()
    try:
        raise ValueError('Exception')
    except:  # noqa: F821
        e = get_exception()
    try:
        raise_exc()
    except: # noqa: F821
        e = get

# Generated at 2022-06-13 04:34:50.756385
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("An exception")
    except Exception:
        e = get_exception()

    assert e.__class__ is Exception, "get_exception should return an Exception"
    assert e.message == "An exception", "get_exception should return the raised exception"

# Generated at 2022-06-13 04:34:53.675812
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        exc = get_exception()
        assert isinstance(exc, Exception)
        assert str(exc) == 'foo'



# Generated at 2022-06-13 04:34:58.581703
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("test exception")
    except:
        e = get_exception()
        assert e
        assert isinstance(e, ValueError)
        assert isinstance(e, Exception)
        assert str(e) == "test exception"


# Generated at 2022-06-13 04:35:05.918168
# Unit test for function get_exception
def test_get_exception():
    """Test whether get_exception() works."""
    # If this test fails, then get_exception() cannot be used.  It's an
    # almost-non-functional piece of code and will lead to failures in any
    # other code that uses it.
    try:
        raise ValueError('test')
    except:
        our_exception = get_exception()

    assert isinstance(our_exception, ValueError)
    assert our_exception.args[0] == 'test'



# Generated at 2022-06-13 04:35:07.000216
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        assert get_exception()


# Generated at 2022-06-13 04:35:09.303589
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('This is a test exception')
    except Exception:
        exception = get_exception()
    assert 'This is a test exception' in str(exception)

# Generated at 2022-06-13 04:35:20.142559
# Unit test for function get_exception
def test_get_exception():
    try:
        # pylint: disable=undefined-variable
        print(foo)
    except Exception:
        e = get_exception()
    assert isinstance(e, NameError)


# Generated at 2022-06-13 04:35:22.664711
# Unit test for function get_exception
def test_get_exception():
    def inner():
        try:
            raise Exception('e')
            raise AssertionError('Should not get here')
        except Exception:
            return get_exception()
    assert inner().args == ('e', )

# Generated at 2022-06-13 04:36:41.351672
# Unit test for function get_exception
def test_get_exception():
    def fail():
        raise ValueError('Kilroy was here!')
    try:
        fail()
    except Exception:
        exc = get_exception()
        assert type(exc) is ValueError
        assert 'Kilroy was here!' in str(exc)



# Generated at 2022-06-13 04:36:44.626532
# Unit test for function get_exception
def test_get_exception():
    '''Test that get_exception returns the correct information'''
    try:
        raise Exception('Test exception')
    except Exception as e:
        exc = get_exception()
    assert isinstance(exc, Exception)
    assert str(exc) == 'Test exception'


# Generated at 2022-06-13 04:36:49.053657
# Unit test for function get_exception
def test_get_exception():
    """Make sure that get_exception returns the current exception"""
    try:
        raise NameError('Test')
    except NameError:
        e = get_exception()
    assert e.args[0] == 'Test'



# Generated at 2022-06-13 04:36:58.555996
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foobar')
    except Exception as e:
        e2 = get_exception()
        assert e == e2
        assert e.args == e2.args

if __name__ == '__main__':
    from ansible.module_utils.six.moves import unittest
    import ansible.module_utils.ast

    class TestAST(unittest.TestCase):
        def test_literal_eval(self):
            self.assertRaises(ValueError, literal_eval, 'foo')
            self.assertEqual(literal_eval('True'), True)
            self.assertEqual(literal_eval('"foo"'), 'foo')
            self.assertEqual(literal_eval('1'), 1)

# Generated at 2022-06-13 04:37:01.221723
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foobar')
    except RuntimeError as e:
        exc = get_exception()
        if exc is not e:
            raise AssertionError(
                    'get_exception() did not return the caught exception: '
                    'it returned %r instead of %r'
                    % (exc, e))

# Generated at 2022-06-13 04:37:05.222805
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test message')
    except Exception:
        e = get_exception()
        assert e.args == ('test message',)


# Generated at 2022-06-13 04:37:07.555035
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("test")
    except Exception:
        exc = get_exception()
        assert exc.args == ('test',)


# Generated at 2022-06-13 04:37:10.410152
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test exception')
    except Exception:
        e = get_exception()
    assert e.args == ('Test exception',)

# Generated at 2022-06-13 04:37:12.378666
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
    assert e.args[0] == 'foo'

# Generated at 2022-06-13 04:37:17.541621
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("I am an exception")
    except Exception:
        assert get_exception().args[0] == "I am an exception"
        assert str(get_exception()) == "I am an exception"

# Generated at 2022-06-13 04:40:02.190363
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=bare-except,pointless-statement
    try:
        raise RuntimeError('test exception')
    except:
        e = get_exception()
    assert isinstance(e, RuntimeError)
    assert e.args == ('test exception',)

    # pylint: disable=bare-except
    try:
        1 + '1'
    except:
        e = get_exception()
    assert isinstance(e, TypeError)
    assert e.args == ("unsupported operand type(s) for +: 'int' and 'str'",)

# Generated at 2022-06-13 04:40:05.050115
# Unit test for function get_exception
def test_get_exception():
    try:
        int('not a digit')
    except:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert 'invalid literal for int()' in str(e)
    else:
        assert False, "int('not a digit') didn't raise an exception"

# Generated at 2022-06-13 04:40:07.774357
# Unit test for function get_exception
def test_get_exception():
    """
    >>> try:
    ...     raise ValueError()
    ... except ValueError:
    ...     exception = get_exception()
    >>> exception
    Traceback (most recent call last):
    ...
    ValueError
    """


# Generated at 2022-06-13 04:40:12.452826
# Unit test for function get_exception
def test_get_exception():
    '''
    Ensure that we are returning a value
    '''
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert e is not None
        assert str(e) == 'foo'


if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:40:14.482087
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        assert get_exception().args == ('foo',)



# Generated at 2022-06-13 04:40:18.274971
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except Exception:
        e = get_exception()

    assert isinstance(e, ZeroDivisionError)
    assert str(e) == 'integer division or modulo by zero'



# Generated at 2022-06-13 04:40:21.309169
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("This is a test")
    except Exception:
        e = get_exception()
        assert str(e) == "This is a test"


# Generated at 2022-06-13 04:40:24.794476
# Unit test for function get_exception
def test_get_exception():
    def get_exception_inner():
        try:
            raise Exception()
        except Exception:
            return get_exception()
    e = get_exception_inner()
    assert e is not None
    assert isinstance(e, Exception)

# Generated at 2022-06-13 04:40:26.268663
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0  # noqa
    except:
        e = get_exception()
        assert isinstance(e, ZeroDivisionError), type(e)

# Generated at 2022-06-13 04:40:28.521752
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
    assert e.args[0] == 'foo'


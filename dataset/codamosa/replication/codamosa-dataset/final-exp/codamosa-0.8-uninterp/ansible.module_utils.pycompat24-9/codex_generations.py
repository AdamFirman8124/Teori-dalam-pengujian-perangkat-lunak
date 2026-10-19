

# Generated at 2022-06-13 04:31:06.273431
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception(u'\u4500')
    except:
        ex = get_exception()
    try:
        raise ex
    except:
        ex2 = get_exception()
    assert ex == ex2

# Generated at 2022-06-13 04:31:10.563916
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Blah')
    except RuntimeError:
        exc = get_exception()
    if not isinstance(exc, RuntimeError):
        raise AssertionError("get_exception() failed to get the "
                             "exception from the stack.")


# Generated at 2022-06-13 04:31:12.508263
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert 'foo' in str(e)

# Generated at 2022-06-13 04:31:15.588840
# Unit test for function get_exception
def test_get_exception():
    # Note: this test is not exhaustive.  It is meant only to catch regressions.
    try:
        int('foo')
    except:
        exc = get_exception()
        assert type(exc).__name__ == 'ValueError'



# Generated at 2022-06-13 04:31:18.226616
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Foo')
    except Exception as e:
        assert e.__class__ is Exception
        assert get_exception().__class__ is Exception
        assert isinstance(e, Exception)
        assert isinstance(get_exception(), Exception)
    return True

# Test for literal eval

# Generated at 2022-06-13 04:31:24.667993
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('This is a unit test')
    except ValueError:
        e = get_exception()
        assert e.args[0] == 'This is a unit test'
    else:
        assert False, "Shouldn't be able to get here"


# Generated at 2022-06-13 04:31:30.079545
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('b')
    except Exception:
        e = get_exception()

    assert isinstance(e, Exception)
    assert str(e) == 'b'

# A unit test for function literal_eval.  Since literal_eval may be implemented
# by a different technique on Python 2.4, we want to make sure that it works
# the same as Python 2.6+ on all versions of Python.

# Generated at 2022-06-13 04:31:34.006953
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError()
    except ValueError:
        e = get_exception()
        assert e
        assert isinstance(e, ValueError)



# Generated at 2022-06-13 04:31:36.998408
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test message')
    except Exception:
        assert get_exception().args[0] == 'test message'


# Generated at 2022-06-13 04:31:39.987521
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except Exception:
        e = get_exception()
        assert str(e) == 'foo'
        assert isinstance(e, ValueError)

# Generated at 2022-06-13 04:32:00.880886
# Unit test for function get_exception
def test_get_exception():
    def f():
        g()

    def g():
        raise Exception('foo')

    try:
        f()
    except:
        assert 'foo' == get_exception().args[0]



# Generated at 2022-06-13 04:32:11.542856
# Unit test for function get_exception
def test_get_exception():
    from ansible.module_utils import basic

    try:
        1/0
    except:
        e = get_exception()

    assert isinstance(e, ZeroDivisionError)
    assert str(e) == 'integer division or modulo by zero'

    # Test in a function
    def f():
        try:
            1/0
        except:
            return get_exception()

    e = f()
    assert isinstance(e, ZeroDivisionError)
    assert str(e) == 'integer division or modulo by zero'

    # Test in a class
    class MyClass(object):
        def f(self):
            try:
                1/0
            except:
                return get_exception()

    o = MyClass()
    e = o.f()

# Generated at 2022-06-13 04:32:17.428513
# Unit test for function get_exception
def test_get_exception():
    def inner_function():
        raise Exception('this is my exception')
    def outer_function():
        try:
            inner_function()
        except Exception:
            return get_exception()
    exception_object = outer_function()
    assert isinstance(exception_object, Exception)
    assert exception_object.args == ('this is my exception',)


# Generated at 2022-06-13 04:32:19.507287
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError('foo')
    except TypeError:
        e = get_exception()
        assert e.args == ('foo',)

test_get_exception()

# Generated at 2022-06-13 04:32:22.688048
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test')
    except Exception:
        (exc_type, exc_value, exc_traceback) = sys.exc_info()
        assert exc_value == get_exception()

# Generated at 2022-06-13 04:32:28.697201
# Unit test for function get_exception
def test_get_exception():
    # Global scope
    try:
        raise Exception('Message')
    except Exception:
        exc = get_exception()
        assert str(exc) == 'Message'

    # Local scope
    def foo():
        try:
            raise Exception('Message')
        except Exception:
            exc = get_exception()
            assert str(exc) == 'Message'

    foo()


# Generated at 2022-06-13 04:32:32.168014
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Test')
    except ValueError:
        e = get_exception()

    assert type(e) == ValueError
    assert str(e) == 'Test'



# Generated at 2022-06-13 04:32:36.694615
# Unit test for function get_exception
def test_get_exception():
    try:
        # pylint: disable=undefined-variable
        l = [0, 1, 2, 3]
        i = l[4]
    except Exception:
        e = get_exception()
    assert isinstance(e, IndexError)



# Generated at 2022-06-13 04:32:38.604327
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("bar")
    except RuntimeError:
        e = get_exception()

    assert e.args == ("bar",)

# Generated at 2022-06-13 04:32:41.022052
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test')
    except:
        exc = get_exception()
        assert exc is not None
        assert 'test' in str(exc)

# Generated at 2022-06-13 04:33:17.005708
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except ValueError as e:
        assert e == get_exception()


# Generated at 2022-06-13 04:33:20.261800
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test')
    except Exception:
        e = get_exception()
    assert isinstance(e, Exception)
    assert 'Test' in str(e)

# Generated at 2022-06-13 04:33:24.770177
# Unit test for function get_exception
def test_get_exception():
    import traceback

    try:
        raise Exception('foobar')
    except Exception:
        stack = traceback.extract_stack()
        exc_info = sys.exc_info()
        e = get_exception()
        assert exc_info[1] == e



# Generated at 2022-06-13 04:33:28.428323
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Problem!')
    except:
        exc = get_exception()
    assert str(exc) == 'Problem!', '%s != %s' % (str(exc), 'Problem!')

# Generated at 2022-06-13 04:33:30.278364
# Unit test for function get_exception
def test_get_exception():
    class TestException(Exception):
        pass

    try:
        raise TestException()
    except Exception:
        assert get_exception().__class__ == TestException

# Generated at 2022-06-13 04:33:39.170756
# Unit test for function get_exception
def test_get_exception():

    def inner():
        try:
            try:
                raise RuntimeError('blah')
            except Exception:
                e = get_exception()
            raise e
        except Exception as e2: # pragma: no cover
            if not isinstance(e2, RuntimeError):
                raise
            if not e is e2:
                raise

    def outer():
        try:
            inner()
        except Exception as e: # pragma: no cover
            if not isinstance(e, RuntimeError):
                raise
            if e.args != ('blah',):
                raise

    outer()



# Generated at 2022-06-13 04:33:43.661130
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except Exception as e:
        ge = get_exception()
    assert ge is e
    assert str(ge) == 'foo'


if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:33:46.336671
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert str(e) == 'foo'

# Generated at 2022-06-13 04:33:51.755160
# Unit test for function get_exception
def test_get_exception():
    def f():
        raise ValueError('foo')
    try:
        f()
    except:
        assert get_exception().args[0] == 'foo'
    try:
        raise ValueError('foo')
    except:
        assert get_exception().args[0] == 'foo'

# Generated at 2022-06-13 04:33:55.212947
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('something bad happened')
    except ValueError:
        e = get_exception()
    assert e.args[0] == 'something bad happened'


# Generated at 2022-06-13 04:35:10.527204
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        raise Exception()

    try:
        raise_exception()
    except Exception:  # pylint: disable=bare-except
        exc = get_exception()
        assert isinstance(exc, Exception)
    try:
        raise Exception(u'\N{FULLWIDTH LATIN SMALL LETTER A}')
    except Exception:  # pylint: disable=bare-except
        exc = get_exception()
        assert isinstance(exc, Exception)
        assert isinstance(exc.args[0], text_type)



# Generated at 2022-06-13 04:35:13.201621
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("hello")
    except ValueError as e:
        assert e == get_exception()


# Generated at 2022-06-13 04:35:18.177417
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=bare-except
    try:
        int('nope')
    except:
        e = get_exception()
        if str(e) != "invalid literal for int() with base 10: 'nope'":
            raise AssertionError("Unexpected exception: %s" % (e,))

# Generated at 2022-06-13 04:35:18.975360
# Unit test for function get_exception
def test_get_exception():
    pass  # TODO

# Generated at 2022-06-13 04:35:22.915098
# Unit test for function get_exception
def test_get_exception():  # pragma: no cover
    try:
        raise Exception("test")
    except Exception:
        e = get_exception()
    # pylint: disable=no-member
    assert isinstance(e, Exception)
    assert e.args == ("test",)
    assert str(e) == "test"


# Generated at 2022-06-13 04:35:25.338743
# Unit test for function get_exception
def test_get_exception():
    try:
        raise KeyError('FooBar')
    except:
        e = get_exception()
        assert isinstance(e, KeyError)
        assert str(e) == 'FooBar'


# Generated at 2022-06-13 04:35:26.995866
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        exc = get_exception()
        assert isinstance(exc, Exception)


# Generated at 2022-06-13 04:35:37.933011
# Unit test for function get_exception
def test_get_exception():
    import imp
    import os
    import sys

    # Use the following to debug test failures (when running the test inside a debugger):
    # def _raise_exception_in_subprocess():
    #     raise Exception('Test Exception!')
    # _raise_exception_in_subprocess()

    # On Python 3.x, this test would fail if the code calling get_exception happens to be written in a
    # python 3.x module and executed with python 3.x, since the Python2 exec... will return a python 3.x
    # exception.  Therefore, we write the code in this test as a Python 2.x module.

    # Write an example module to the temp directory
    (fd, path) = imp.find_module('ansible_test_get_exception', ['ansible/module_utils'])

# Generated at 2022-06-13 04:35:40.279028
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Foo")
    except Exception:
        e = get_exception()
        assert e.args[0] == "Foo"

# Generated at 2022-06-13 04:35:42.281104
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except Exception:
        e = get_exception()  # noqa
    else:
        raise AssertionError("Expected exception")



# Generated at 2022-06-13 04:36:59.486773
# Unit test for function get_exception
def test_get_exception():
    try:
        i = int('spam')
    except Exception:
        e = get_exception()
    assert isinstance(e, ValueError)

# Generated at 2022-06-13 04:37:04.922477
# Unit test for function get_exception

# Generated at 2022-06-13 04:37:06.938947
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test')
    except Exception:
        e = get_exception()
        assert str(e) == 'test'

# Generated at 2022-06-13 04:37:11.588483
# Unit test for function get_exception
def test_get_exception():
    """
    Execute the get_exception function to make sure it works.
    """
    try:
        raise Exception
    except:
        # pylint: disable=bare-except
        result = get_exception()
    assert result.__class__.__name__ == 'Exception'



# Generated at 2022-06-13 04:37:16.559096
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Unit test')
    except:
        e = get_exception()
    assert 'Unit test' == e.args[0]

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:37:18.840200
# Unit test for function get_exception
def test_get_exception():
    try:
        1 // 0
    except ZeroDivisionError:
        assert get_exception() is not None



# Generated at 2022-06-13 04:37:21.344057
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('oops')
    except Exception:
        e = get_exception()
        assert e.message == 'oops'

# Generated at 2022-06-13 04:37:24.522614
# Unit test for function get_exception
def test_get_exception():
    """Unit tests for get_exception"""
    try:
        raise ValueError('This is an error')
    except ValueError:
        v = get_exception()
        assert str(v) == 'This is an error'

# Generated at 2022-06-13 04:37:30.888181
# Unit test for function get_exception
def test_get_exception():
    try:
        x = 1/0
    except ZeroDivisionError:
        e = get_exception()
        if not isinstance(e, ZeroDivisionError):
            raise AssertionError('Expected ZeroDivisionError but got %r instead' %
                    (e,))
    else:
        raise AssertionError('Expected ZeroDivisionError but no exception thrown')

# Generated at 2022-06-13 04:37:37.163715
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("test_get_exception exception")
    except Exception:
        e = get_exception()
        if not isinstance(e, Exception):
            raise AssertionError("Expected instance of %s, got %s"
                                 % (Exception, type(e)))
        if str(e) != "test_get_exception exception":
            raise AssertionError("Expected 'test_get_exception exception', got %s"
                                 % repr(str(e)))



# Generated at 2022-06-13 04:40:27.477043
# Unit test for function get_exception
def test_get_exception():
    try:
        raise NameError
    except Exception:
        e = get_exception()

    assert isinstance(e, NameError)



# Generated at 2022-06-13 04:40:29.287576
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("foo")
    except Exception:
        exc = get_exception()
        assert str(exc) == "foo"

# Generated at 2022-06-13 04:40:30.813483
# Unit test for function get_exception
def test_get_exception():
    try:
        print(foo)
    except NameError as e:
        assert get_exception() == e



# Generated at 2022-06-13 04:40:33.006367
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test')
    except Exception:
        try:
            has_exc = True
            if get_exception():
                has_exc = True
        except UnboundLocalError:
            has_exc = False

    assert has_exc



# Generated at 2022-06-13 04:40:34.819066
# Unit test for function get_exception
def test_get_exception():
    """Test the ability to get the exception"""
    try:
        raise ValueError('Test exception')
    except ValueError:
        exception = get_exception()
    assert exception.args[0] == 'Test exception'


# Generated at 2022-06-13 04:40:37.818528
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo bar')
    except ValueError as e:
        exc = get_exception()
    if exc != e:
        raise Exception('get_exception() returned wrong exception')


# Generated at 2022-06-13 04:40:42.112180
# Unit test for function get_exception
def test_get_exception():
    def raise_runtime():
        raise RuntimeError('test exception')

    try:
        raise_runtime()
    except Exception:
        e = get_exception()
        assert str(e) == 'test exception'


# Generated at 2022-06-13 04:40:44.861570
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test_get_exception')
    except ValueError:
        e = get_exception()
    assert e.args == ('test_get_exception',)

# Generated at 2022-06-13 04:40:46.298893
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except:
        assert isinstance(get_exception(), Exception)



# Generated at 2022-06-13 04:40:51.659745
# Unit test for function get_exception
def test_get_exception():
    class ExceptionToCatch(Exception):
        def __init__(self, a, b, c):
            super(ExceptionToCatch, self).__init__(a, b, c)

    try:
        raise ExceptionToCatch('abc', 123, {'foo': 'bar'})
    except Exception:
        exc = get_exception()

    assert isinstance(exc, ExceptionToCatch)
    assert exc.args == ('abc', 123, {'foo': 'bar'})




# Generated at 2022-06-13 04:31:04.097272
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception:
        assert True
        return

    assert False

# Generated at 2022-06-13 04:31:07.304620
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert str(e) == 'foo'
    else:
        raise AssertionError('get_exception did not catch an exception')



# Generated at 2022-06-13 04:31:09.733911
# Unit test for function get_exception
def test_get_exception():
    try:
        'foo' in 10
    except Exception:
        e = get_exception()
    assert isinstance(e, TypeError)

# Generated at 2022-06-13 04:31:11.547070
# Unit test for function get_exception
def test_get_exception():  # pylint: disable=missing-docstring
    error = None
    try:
        raise ValueError('Test')
    except ValueError:
        error = get_exception()
    assert isinstance(error, ValueError)
    assert str(error) == 'Test'



# Generated at 2022-06-13 04:31:15.922720
# Unit test for function get_exception
def test_get_exception():
    import unittest

    class TestGetException(unittest.TestCase):
        def test_get_exception(self):
            try:
                raise Exception('An exception')
            except:
                e = get_exception()
                assert str(e) == 'An exception'
    unittest.main(module='ansible.module_utils.basic', argv=[''])


# Generated at 2022-06-13 04:31:18.290687
# Unit test for function get_exception
def test_get_exception():
    try:
        int('Not a number')
        assert False, 'Expected exception'
    except ValueError:
        e = get_exception()
        assert str(e) == 'invalid literal for int() with base 10: \'Not a number\''


# Generated at 2022-06-13 04:31:22.474891
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError
    except:
        exc = get_exception()
        assert type(exc) == TypeError

# Generated at 2022-06-13 04:31:32.498097
# Unit test for function get_exception
def test_get_exception():

    """
    A few tests to see if the get_exception function works.

    If this test starts to fail check to see what the new syntax is for
    getting the exception off sys.exc_info().
    """

    # Check that get_exception() returns the exception that was just raised
    raised_exception = None
    try:
        raise Exception("Hey I'm an exception")
    except Exception:
        raised_exception = get_exception()
    assert isinstance(raised_exception, Exception)
    assert raised_exception.args[0] == "Hey I'm an exception"

    # Check that it works with a generic exception
    raised_exception = None
    try:
        raise Exception("Hey I'm a generic exception")
    except:
        raised_exception = get_exception()

# Generated at 2022-06-13 04:31:39.559077
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except RuntimeError as e:
        assert get_exception() is e
    try:
        raise RuntimeError('foo')
    except RuntimeError:
        e = get_exception()

# Generated at 2022-06-13 04:31:43.773394
# Unit test for function get_exception
def test_get_exception():
    try:
        foo
    except:
        e = get_exception()
        if str(e) != "'foo'":
            raise AssertionError("%s != 'foo'" % e)

# Generated at 2022-06-13 04:32:03.826848
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        try:
            raise IndexError()
        except Exception:
            return get_exception()
    e = raise_exception()
    assert isinstance(e, IndexError)

# Generated at 2022-06-13 04:32:06.310236
# Unit test for function get_exception
def test_get_exception():
    class Foo(Exception):
        pass
    def _():
        try:
            raise Foo()
        except Exception:
            return get_exception()
    foo = _()
    assert isinstance(foo, Foo)

# Generated at 2022-06-13 04:32:07.969311
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Boom!')
    except Exception:
        e = get_exception()
        assert str(e) == 'Boom!'

# Generated at 2022-06-13 04:32:10.734197
# Unit test for function get_exception
def test_get_exception():
    try:
        raise NameError('get_exception test')
    except NameError:
        e = get_exception()
        assert str(e) == 'get_exception test'


# Generated at 2022-06-13 04:32:14.586099
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception:
        assert get_exception().__class__.__name__ == 'ZeroDivisionError'

# Generated at 2022-06-13 04:32:17.082293
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("foo")
    except ValueError as e:
        foo = e
    assert get_exception() == foo


# Generated at 2022-06-13 04:32:19.208070
# Unit test for function get_exception
def test_get_exception():
    def foo():
        raise ValueError(3)

    try:
        foo()
    except:
        e = get_exception()

    assert e.args[0] == 3

# Generated at 2022-06-13 04:32:25.884103
# Unit test for function get_exception
def test_get_exception():
    def raise_exc(message):
        try:
            raise Exception(message)
        except:
            return sys.exc_info()[1]

    exc1 = raise_exc('hello')
    exc2 = raise_exc('world')

    assert exc1.args[0] == 'hello'
    assert exc2.args[0] == 'world'
    assert exc1 is not exc2


# Generated at 2022-06-13 04:32:28.217754
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Something bad happened")
    except:
        e = get_exception()
    assert e.args == ("Something bad happened",)

# Generated at 2022-06-13 04:32:33.620720
# Unit test for function get_exception
def test_get_exception():
    """
    >>> def test():
    ...     try:
    ...         raise Exception('Blah')
    ...     except Exception:
    ...         return get_exception()
    ...
    >>> e = test()
    >>> str(e)
    'Blah'
    """



# Generated at 2022-06-13 04:32:53.188179
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError()
    except ValueError:
        e = get_exception()
    assert isinstance(e, ValueError)



# Generated at 2022-06-13 04:32:55.761655
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert e.args == ('foo',)



# Generated at 2022-06-13 04:32:58.588330
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError()
    except ValueError:
        e = get_exception()
    assert isinstance(e, ValueError)


# Generated at 2022-06-13 04:33:02.055934
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("test")
    except Exception:
        the_error = get_exception()
        assert the_error.args[0] == "test"

# Generated at 2022-06-13 04:33:10.945907
# Unit test for function get_exception
def test_get_exception():
    # This is a bogus exception.  We're not going to use it in the try/except.
    # Instead we're going to use it to get the exception name to raise.
    # We're going to use it multiple times to make sure that the exception
    # handler doesn't use the same exception
    class BogusException(Exception):
        pass
    raised = None
    try:
        raise BogusException()
    except BogusException:
        raised = get_exception()
        raised2 = get_exception()
        raise
    # We shouldn't reach this next line
    assert False
    assert raised is raised2
    try:
        raise raised
    except BogusException:
        assert True
    except Exception:
        assert False
        # The raised exception was not a BogusException

# Generated at 2022-06-13 04:33:14.537868
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foobar')
    except Exception:
        e = get_exception()
        if e.args != ('foobar',):
            raise Exception('failed to get exception args')
        if e.message != 'foobar':
            raise Exception('failed to get exception message')


# Generated at 2022-06-13 04:33:23.907762
# Unit test for function get_exception
def test_get_exception():
    # Make sure get_exception works even when someone has monkey patched the normal
    # exception raising
    try:
        raise RuntimeError('bork')
    except RuntimeError:
        # We don't care that we're reusing e.  If get_exception has a problem, it'll be
        # caught on the 2nd exception
        e = get_exception()
        try:
            raise RuntimeError('bork again')
        except RuntimeError:
            e2 = get_exception()
            assert e == e2
    return True


# Generated at 2022-06-13 04:33:26.749626
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except:
        e = get_exception()
    assert e.args[0] == 'foo'



# Generated at 2022-06-13 04:33:33.940060
# Unit test for function get_exception
def test_get_exception():
    # This function is supposed to return the exception in a manner that works
    # on Python 2.4 through Python 3.x so if this fails in any of the versions
    # we're testing then the test fails

    class ExceptionWrapper():
        def __call__(self):
            try:
                raise ValueError()
            except ValueError as e:
                self.exc = e
    e = ExceptionWrapper()
    e()
    assert get_exception() is e.exc


# Generated at 2022-06-13 04:33:38.389209
# Unit test for function get_exception
def test_get_exception():
    def test():
        raise Exception('xyzzy')
    try:
        test()
    except Exception:
        caught = get_exception()
        assert len(caught.args) == 1
        assert caught.args[0] == 'xyzzy'


# Generated at 2022-06-13 04:34:13.530026
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass

    try:
        raise MyException('foo')
    except:  # noqa: E722
        e = get_exception()
        assert isinstance(e, MyException)
        assert str(e) == 'foo'

# Generated at 2022-06-13 04:34:18.785346
# Unit test for function get_exception
def test_get_exception():
    def get_exc(exc):
        def func():
            raise exc
        try:
            func()
            return None
        except Exception:
            return get_exception()
    assert get_exc(KeyError('foo')) == get_exc(KeyError('foo'))

# Generated at 2022-06-13 04:34:22.194377
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        e = get_exception()
        assert isinstance(e, ZeroDivisionError)
    else:
        assert False, 'Exception should have been raised'


# Generated at 2022-06-13 04:34:29.179468
# Unit test for function get_exception
def test_get_exception():
    import unittest

    class TestGetException(unittest.TestCase):

        def test_get_exception(self):
            try:
                raise Exception("Testing")
            except:
                self.assertEqual("Testing", get_exception().args[0])

    import ansible.module_utils.basic  # pylint: disable=unused-import
    # I hate you python and your inability to use unittest easily from code in the same file
    # that doesn't have a __main__ block.
    ansible.module_utils.basic.__unit_test_get_exception__ = True
    sys.exit(unittest.main())

# Generated at 2022-06-13 04:34:32.345701
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("test")
    except ValueError:
        e = get_exception()
    assert isinstance(e, ValueError)
    assert unicode(e) == u"test"

# Generated at 2022-06-13 04:34:38.269206
# Unit test for function get_exception
def test_get_exception():
    """Test that the get_exception function is able to get the current
    exception.
    """
    assert not get_exception(), 'No exception expected'

    def func():
        try:
            raise ValueError('hello')
        except Exception:
            e = get_exception()

            assert e, 'Exception expected'
            assert str(e) == 'hello', 'Unexpected exception text'
    func()

# Generated at 2022-06-13 04:34:43.096372
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError('Failed')
    except TypeError:
        e = get_exception()
        assert isinstance(e, TypeError), 'e is not a TypeError'
        assert isinstance(e, Exception), 'e is not an Exception'
        assert str(e) == 'Failed', 'Exception text does not match'

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:34:48.900228
# Unit test for function get_exception
def test_get_exception():
    foo = None
    try:
        foo.bar()
    except: # pylint: disable=bare-except
        e = get_exception()
        assert e.__class__.__name__ == 'AttributeError'
        assert str(e) == "'NoneType' object has no attribute 'bar'"



# Generated at 2022-06-13 04:34:55.714393
# Unit test for function get_exception
def test_get_exception():
    '''get_exception should return the current exception'''

    def foo():
        bar()

    def bar():
        try:
            baz()
        except Exception:
            curr_exception = get_exception()
        assert isinstance(curr_exception, NameError)
        raise curr_exception

    def baz():
        quux

    try:
        foo()
    except NameError:
        pass
    else:
        raise AssertionError('Expected NameError to be raised')

# Generated at 2022-06-13 04:34:59.668570
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('abc')
    except Exception:
        e = get_exception()
    assert isinstance(e, ValueError)


# Generated at 2022-06-13 04:36:10.002183
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception:
        e = get_exception()

    assert isinstance(e, ZeroDivisionError)



# Generated at 2022-06-13 04:36:14.604714
# Unit test for function get_exception
def test_get_exception():
    try:
        raise SyntaxError('test')
    except SyntaxError:
        e = get_exception()
        if 'test' not in str(e):
            raise AssertionError('get_exception failed: %r' % e)

# Generated at 2022-06-13 04:36:22.455432
# Unit test for function get_exception
def test_get_exception():

    # This is the exception we'll see on Python 2.4
    class FooException(Exception):
        pass

    # This is the exception we'll see on Python 2.6
    class BarException(FooException):
        pass

    try:
        raise BarException("Foo!")
    except FooException as e:
        # 2.6 style exception variable
        assert e.args == ('Foo!',)
        assert sys.version_info >= (2, 6)

# Generated at 2022-06-13 04:36:25.159024
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except:
        ret = get_exception()
    assert ret.args[0] == 'foo'

# Generated at 2022-06-13 04:36:28.670607
# Unit test for function get_exception
def test_get_exception():
    try:
        x = 1/0  # noqa
    except:
        e = get_exception()
        assert 'division by zero' in str(e)

# Generated at 2022-06-13 04:36:30.952567
# Unit test for function get_exception
def test_get_exception():
    class TestException(Exception):
        pass
    try:
        raise TestException
    except:
        e = get_exception()
        assert(type(e) == TestException)

# Generated at 2022-06-13 04:36:34.183343
# Unit test for function get_exception
def test_get_exception():
    def f():
        try:
            raise Exception(u'\xe7')
        except Exception:
            return get_exception()

    assert isinstance(f(), Exception)
    assert not isinstance(f(), UnicodeError)


# Generated at 2022-06-13 04:36:44.974740
# Unit test for function get_exception
def test_get_exception():
    """Verify that the function get_exception works.
    """
    class FooException(Exception):
        pass

    def get_exception_bad():
        try:
            raise FooException()
        except FooException as e:
            foo = e

    def get_exception_good():
        try:
            raise FooException()
        except FooException:
            foo = get_exception()

    if sys.version_info[0] > 2:
        get_exception_to_test = get_exception_bad
    else:
        get_exception_to_test = get_exception_good
    try:
        get_exception_to_test()
    except SyntaxError:
        pass
    else:
        raise AssertionError('Should have raised SyntaxError')

# Generated at 2022-06-13 04:36:48.383539
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Foo')
    except:
        e = get_exception()
        assert e.args[0] == 'Foo'

# Generated at 2022-06-13 04:36:54.528565
# Unit test for function get_exception
def test_get_exception():
    def _raise():
        # pylint: disable=unused-variable
        try:
            x = 1 / 0
        except Exception as e:
            e = get_exception()

    try:
        _raise()
    except ZeroDivisionError as e:
        assert e == get_exception()
    else:
        raise RuntimeError('Test failed: get_exception() did not catch ZeroDivisionError')



# Generated at 2022-06-13 04:38:06.496100
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('example')
    except Exception:
        e = get_exception()

    assert e.__class__.__name__ == 'RuntimeError'
    assert str(e) == 'example'


# Generated at 2022-06-13 04:38:12.394004
# Unit test for function get_exception
def test_get_exception():
    def test_code():
        raise Exception("A test exception")

    try:
        test_code()
        assert False, "test_code did not raise an exception"
    except:
        exc = get_exception()
        assert isinstance(exc, Exception)
        assert str(exc) == "A test exception"

# Generated at 2022-06-13 04:38:14.825656
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except ZeroDivisionError:
        ex = get_exception()
    assert ZeroDivisionError == type(ex), type(ex)
    assert 'division' in str(ex), ex

# Generated at 2022-06-13 04:38:17.388635
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('boom')
    except RuntimeError as e:
        assert e is get_exception()


# Generated at 2022-06-13 04:38:20.264605
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Something bad happened')
    except Exception:
        e = get_exception()
    assert e.args[0] == 'Something bad happened'

# Generated at 2022-06-13 04:38:22.272832
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except RuntimeError:
        e = get_exception()
        assert str(e) == 'foo'

# Generated at 2022-06-13 04:38:28.357045
# Unit test for function get_exception
def test_get_exception():
    def this_raises():
        raise RuntimeError('this should fail')

    try:
        this_raises()
    except Exception:
        e = get_exception()
        assert str(e) == 'this should fail', (str(e), 'this should fail')

    # Test to see if the original exception is preserved
    try:
        raise ValueError('this should fail')
    except Exception:
        e = get_exception()
        assert isinstance(e, ValueError)



# Generated at 2022-06-13 04:38:31.419748
# Unit test for function get_exception
def test_get_exception():

    try:
        raise ValueError("some exception")
    except Exception:
        e = get_exception()
        if str(e) != 'some exception':
            print("exception was: %s" % (e))
            raise

# Generated at 2022-06-13 04:38:33.357940
# Unit test for function get_exception
def test_get_exception():
    try: raise RuntimeError('This is the error message.')
    except RuntimeError: e = get_exception()
    assert e.args[0] == 'This is the error message.'

# Generated at 2022-06-13 04:38:35.117506
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        e = get_exception()
        assert isinstance(e, Exception)

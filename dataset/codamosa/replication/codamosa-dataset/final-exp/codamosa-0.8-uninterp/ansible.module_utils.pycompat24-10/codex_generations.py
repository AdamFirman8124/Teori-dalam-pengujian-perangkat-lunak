

# Generated at 2022-06-13 04:31:11.272469
# Unit test for function get_exception
def test_get_exception():
    def some_function():
        # Intentionally cause an exception
        return 1 / 0

    try:
        some_function()
    except Exception as e:
        # Try the python2-way to access the exception
        assert e == get_exception()
    except:  # pylint: disable=bare-except
        # Try the python3-way to access the exception
        assert get_exception()



# Generated at 2022-06-13 04:31:14.149446
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("This is a test exception")
    except:
        ex = get_exception()
    assert isinstance(ex, RuntimeError)
    assert ex.args[0] == "This is a test exception"

# Generated at 2022-06-13 04:31:15.518167
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError("hi")
    except TypeError:
        assert get_exception().args == ("hi",)

# Generated at 2022-06-13 04:31:17.199197
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('test exception')
    except Exception:
        ex = get_exception()
        assert(str(ex) == 'test exception')



# Generated at 2022-06-13 04:31:18.805120
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert e.args[0] == 'foo'

# Generated at 2022-06-13 04:31:23.300809
# Unit test for function get_exception
def test_get_exception():
    #No exception
    assert get_exception() is None

    #Test not raising an exception
    try:
        raise ValueError
    except ValueError:
        assert get_exception()

# Generated at 2022-06-13 04:31:26.993502
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test_get_exception: expected exception')
    except:
        exc_info = get_exception()
        assert exc_info.args[0] == 'test_get_exception: expected exception'



# Generated at 2022-06-13 04:31:33.402217
# Unit test for function get_exception
def test_get_exception():
    import nose

    def raiser():
        raise ValueError('')

    try:
        raiser()
    except ValueError:
        nose.tools.assert_equal(get_exception(), sys.exc_info()[1])

    nose.tools.assert_raises(ValueError, literal_eval, 'q')
    nose.tools.assert_true(literal_eval('{"a": 42}'))

# Generated at 2022-06-13 04:31:38.519265
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass

    try:
        raise MyException('Exception value')
    except MyException:
        e = get_exception()
    else:
        raise Exception("Didn't work")
    assert "Exception value" in '%s' % e


# Generated at 2022-06-13 04:31:41.482366
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test_get_exception')
    except ValueError:
        e = get_exception()
        assert e.args == ('test_get_exception',), "ValueError doesn't match: %r" % repr(e)

# Generated at 2022-06-13 04:32:01.954934
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except:
        e = get_exception()
        assert e.args[0] == 'foo'
        assert str(e) == 'foo'



# Generated at 2022-06-13 04:32:08.371542
# Unit test for function get_exception
def test_get_exception():
    # Success
    def raise_ioerror():
        raise IOError()
    try:
        raise_ioerror()
    except Exception:
        e = get_exception()
    assert isinstance(e, IOError)
    # Failure
    try:
        raise_ioerror()
    except Exception:
        pass
    else:
        raise AssertionError("Did not have exception")



# Generated at 2022-06-13 04:32:10.409222
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("test")
    except ValueError:
        exc = get_exception()
    assert isinstance(exc, ValueError)

# Generated at 2022-06-13 04:32:14.586266
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Akbar!')
    except:
        exc = get_exception()
        assert repr(exc) == "ValueError('Akbar!',)"

# Generated at 2022-06-13 04:32:16.017098
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except RuntimeError:
        assert get_exception().args[0] ==  'foo'

# Generated at 2022-06-13 04:32:17.960539
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except Exception:
        e = get_exception()
    assert e.args[0] == 'foo'

# Generated at 2022-06-13 04:32:28.823721
# Unit test for function get_exception
def test_get_exception():
    import unittest
    import ansible.module_utils.six

    class TestCase(unittest.TestCase):
        def test_get_exception(self):
            try:
                raise ValueError('Unit test')
            except Exception:
                e = get_exception()
                self.assertTrue(isinstance(e, Exception))
                self.assertTrue(repr(e).startswith(type(e).__name__))
                self.assertEqual(e.args, ('Unit test',))

    suite = unittest.TestSuite()
    suite.addTest(TestCase('test_get_exception'))
    unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0)

# Generated at 2022-06-13 04:32:31.885750
# Unit test for function get_exception
def test_get_exception():
    try:
        raise AnsibleModuleError('foo')
    except Exception:
        error = get_exception()
        assert error.report_msg == 'foo'


# Generated at 2022-06-13 04:32:35.992717
# Unit test for function get_exception
def test_get_exception():
    def foo():
        raise NotImplementedError('Not here')

    try:
        foo()
    except:
        e = get_exception()
        assert str(e) == 'Not here'
        assert type(e) == NotImplementedError

# Generated at 2022-06-13 04:32:38.397316
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except:
        e = get_exception()
    assert e.args[0] == 'foo'



# Generated at 2022-06-13 04:33:14.275966
# Unit test for function get_exception
def test_get_exception():
    def thrower():
        raise ValueError('foo')
    try:
        thrower()
    except:
        e = get_exception()
    assert str(e) == 'foo'
    import sys
    orig_exc = sys.exc_info()
    assert orig_exc == (ValueError, e, None)

# Generated at 2022-06-13 04:33:27.011029
# Unit test for function get_exception
def test_get_exception():
    '''Test get_exception.'''
    from ansible.module_utils import basic

    ignores = (
        (None, ),
        (None, None),
        (None, None, None),
        (None, None, None, None),
        (None, ),
        (None, None),
        (None, None, None),
        (None, None, None, None),
        (None, None, None, None),
        ('', None, None),
        ('', ),
        ('', None),
        ('', None, None),
        ('', None, None, None),
        ('', None, None, None),
        ('', None, None, None, None),
        ('', None, None, None, None, None),
    )


# Generated at 2022-06-13 04:33:32.154756
# Unit test for function get_exception
def test_get_exception():
    def foo():
        try:
            raise NameError("Foo")
        except NameError:
            e = get_exception()
        return e

    assert foo().args[0] == "Foo"

    def foo():
        e = get_exception()
        return e

    assert not foo()

# Generated at 2022-06-13 04:33:34.713790
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass
    try:
        raise MyException
    except Exception:
        assert isinstance(get_exception(), MyException)


# Generated at 2022-06-13 04:33:38.025628
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('nope')
    except:
        pass
    e = get_exception()
    assert str(e) == 'nope'


# Generated at 2022-06-13 04:33:40.626495
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('This is a test')
    except Exception:
        e = get_exception()
    assert str(e) == 'This is a test'


# Generated at 2022-06-13 04:33:46.434877
# Unit test for function get_exception
def test_get_exception():
    '''
    Test that we get the right exception.
    '''
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert str(e) == 'foo'
        assert isinstance(e, Exception)
        assert e.args == ('foo',)
    else:
        assert False, 'Exception was not raised'

# Generated at 2022-06-13 04:33:50.393927
# Unit test for function get_exception
def test_get_exception():
    try:
        x = 1 / 0
    except Exception:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)



# Generated at 2022-06-13 04:33:53.792124
# Unit test for function get_exception
def test_get_exception():
    def foo():
        # pylint: disable=undefined-variable
        raise Exception('This is an exception')
    try:
        foo()
    except:
        exc = get_exception()
        assert isinstance(exc, Exception)
        assert exc.args[0] == 'This is an exception'


# Generated at 2022-06-13 04:33:57.891202
# Unit test for function get_exception

# Generated at 2022-06-13 04:34:33.069146
# Unit test for function get_exception
def test_get_exception():  # pylint: disable=missing-docstring
    try:
        raise Exception('foo')
    except Exception:
        return get_exception()


# Generated at 2022-06-13 04:34:35.614888
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
    assert e.args == ('foo',)

# Generated at 2022-06-13 04:34:38.136902
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        e = get_exception()
    assert isinstance(e, Exception)

# Generated at 2022-06-13 04:34:41.016663
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('testing')
    except RuntimeError:
        exc = get_exception()
        assert isinstance(exc, RuntimeError)
        assert str(exc) == 'testing'
        assert exc.args == ('testing',)


# Generated at 2022-06-13 04:34:43.169344
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test exception')
    except:
        e = get_exception()
    assert (str(e) == 'test exception')
    return



# Generated at 2022-06-13 04:34:45.760195
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except ValueError as e:
        assert e is get_exception()



# Generated at 2022-06-13 04:34:55.491726
# Unit test for function get_exception
def test_get_exception():
    class C(object):
        def m(self):
            try:
                foo()
            except:
                assert get_exception()

        def mm(self):
            foo()

    try:
        C().m()
        raise AssertionError('get_exception() failed (1)')
    except AssertionError:
        pass
    try:
        C().mm()
        raise AssertionError('get_exception() failed (2)')
    except NameError as e:
        if not e.args[0].startswith('global name'):
            raise

# unit test for function literal_eval

# Generated at 2022-06-13 04:35:01.176541
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        raise ValueError('Hello')

    def testit():
        try:
            raise_exception()
        except:
            e = get_exception()
            return e

    e = testit()
    assert isinstance(e, ValueError)
    assert str(e) == 'Hello'

# Generated at 2022-06-13 04:35:09.290891
# Unit test for function get_exception
def test_get_exception():
    # Python 2.6 compatibility
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    import sys
    import inspect

    class ExceptionOne(object):
        pass

    class ExceptionTwo(object):
        pass

    buffer = StringIO()

    # ExceptionOne happens inside the function

# Generated at 2022-06-13 04:35:11.598924
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('This is a unit test')
    except:
        e = get_exception()
    assert e.args[0] == 'This is a unit test'

# Generated at 2022-06-13 04:36:30.043711
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except:
        assert get_exception() is sys.exc_info()[1]
    try:
        raise RuntimeError('foo')
    except:
        e = get_exception()
        assert e.args[0] == 'foo'
    try:
        raise RuntimeError('foo', 'bar', 'baz')
    except:
        e = get_exception()
        assert e.args[0] == 'foo'
        assert e.args[1] == 'bar'
        assert e.args[2] == 'baz'



# Generated at 2022-06-13 04:36:37.074787
# Unit test for function get_exception
def test_get_exception():
    # Some Exceptions have internal state and can only be raised once.
    # We need to create a new Exception and raise it so that a second except clause
    # can reraise it.
    try:
        raise Exception("Test Exception")
    except Exception:
        e = get_exception()
    try:
        raise e
    except Exception:
        assert sys.exc_info()[1] is e

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:36:40.527865
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError()
    except Exception:
        e = get_exception()
        assert isinstance(e, ValueError)
        raise


# Generated at 2022-06-13 04:36:45.628873
# Unit test for function get_exception
def test_get_exception():
    try:
        foo = bar  # pylint: disable=undefined-variable
    except NameError:
        e = get_exception()
        assert str(e) == "'bar'"

    try:
        1/0 # pylint: disable=pointless-statement
    except ZeroDivisionError:
        e = get_exception()
        assert str(e) == "integer division or modulo by zero"


# Generated at 2022-06-13 04:36:49.053885
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("some error")
    except Exception:
        e = get_exception()
    assert isinstance(e, ValueError)
    assert str(e) == "some error"


# Generated at 2022-06-13 04:36:58.556899
# Unit test for function get_exception
def test_get_exception():
    """Test get_exception()

    This test is only run when the module is invoked directly.
    """
    # pylint: disable=unused-argument,missing-docstring,unreachable

    import pytest
    from ansible.module_utils.basic import AnsibleModule

    def test_get_exception_error(fail):
        try:
            raise RuntimeError('testing exceptions')
        except RuntimeError:
            e = get_exception()

        assert e.args[0] == 'testing exceptions'

    def test_get_exception_ok():
        try:
            raise RuntimeError('testing exceptions')
        except RuntimeError:
            e = get_exception()

        assert e.args[0] == 'testing exceptions'


# Generated at 2022-06-13 04:37:00.965552
# Unit test for function get_exception
def test_get_exception():
    """
    Test that we catch the current exception when we're inside an exception
    handler
    """
    try:
        raise RuntimeError("test")
    except Exception:
        e = get_exception()
    assert str(e) == "test"

# Generated at 2022-06-13 04:37:02.358753
# Unit test for function get_exception
def test_get_exception():
    try:
        raise IndexError
    except IndexError:
        e = get_exception()
    assert type(e) is IndexError

# Generated at 2022-06-13 04:37:04.156473
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Test Exception")
    except Exception:
        exc = get_exception()
        assert exc.__class__.__name__ == "Exception"
        assert str(exc) == "Test Exception"


# Generated at 2022-06-13 04:37:05.689745
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Sample exception')
    except ValueError:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert e.args[0] == 'Sample exception'



# Generated at 2022-06-13 04:39:37.678895
# Unit test for function get_exception
def test_get_exception():
    def raising_func():
        raise ValueError('This is a test')
    try:
        raising_func()
    except ValueError as e:
        assert e == get_exception()
    finally:
        del raising_func

# Generated at 2022-06-13 04:39:39.668507
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        e = get_exception()
    assert e
    assert isinstance(e, ZeroDivisionError)


# Generated at 2022-06-13 04:39:41.861569
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('An exception')
    except ValueError:
        e = get_exception()
        assert type(e) is ValueError
        assert str(e) == 'An exception'

# Generated at 2022-06-13 04:39:43.279388
# Unit test for function get_exception
def test_get_exception():
    """Test that the get_exception function works"""

    try:
        raise NameError("This is a test")
    except NameError as e:
        assert e == get_exception()
    except:
        assert False # We should never get here

# Generated at 2022-06-13 04:39:46.188489
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Something is wrong')
    except ValueError:
        exc = get_exception()
        assert exc is not None
        assert 'Something is wrong' in str(exc)


# Generated at 2022-06-13 04:39:50.798667
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('test')
    except:
        try:
            raise get_exception()
        except:
            exc = get_exception()
            if str(exc) != 'test':
                raise AssertionError('Failed to get the right exception')

# Generated at 2022-06-13 04:39:54.080235
# Unit test for function get_exception
def test_get_exception():
    def _raise_exception():
        try:
            raise ValueError('a test')
        except Exception:
            return (sys.exc_info()[1], get_exception())
    t1, t2 = _raise_exception()
    assert t1 is t2

# Generated at 2022-06-13 04:39:56.526770
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('The quick brown fox jumps over the lazy dog')
    except RuntimeError:
        e = get_exception()

    assert e.args == ('The quick brown fox jumps over the lazy dog',)

# Generated at 2022-06-13 04:39:59.624764
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('testing')
    except ValueError:
        e = get_exception()
        assert isinstance(e, ValueError)
        assert 'testing' in str(e)


# Generated at 2022-06-13 04:40:02.018654
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Catch me!")
    except:
        exc = get_exception()
        assert exc.__class__ == RuntimeError
        assert str(exc) == "Catch me!"
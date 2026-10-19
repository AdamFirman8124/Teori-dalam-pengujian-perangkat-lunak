

# Generated at 2022-06-13 04:31:06.288952
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("testing")
    except Exception:
        assert get_exception().args == ("testing",)


# Generated at 2022-06-13 04:31:09.340227
# Unit test for function get_exception
def test_get_exception():
    class CustomException(Exception):
        pass
    try:
        raise CustomException('foo')
    except Exception:
        assert isinstance(get_exception(), CustomException)

# Generated at 2022-06-13 04:31:16.793195
# Unit test for function get_exception
def test_get_exception():
    import unittest

    def get_exception_testable(raise_exception):
        try:
            raise_exception
        except RuntimeError:
            return get_exception()

    class GetExceptionTestCase(unittest.TestCase):
        class ExceptionToRaise(RuntimeError):
            pass

        def test_get_exception(self):
            e = get_exception_testable(self.ExceptionToRaise("Error!"))
            self.assertIsInstance(e, self.ExceptionToRaise)

    suite = unittest.TestLoader().loadTestsFromTestCase(GetExceptionTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-13 04:31:18.702813
# Unit test for function get_exception
def test_get_exception():
    try:
        raise AssertionError('foo')
    except AssertionError:
        exc = get_exception()
    assert str(exc) == 'foo'


# Generated at 2022-06-13 04:31:23.685906
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
    assert isinstance(e, Exception)
    assert e.args[0] == 'foo'



# Generated at 2022-06-13 04:31:27.295789
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass

    try:
        raise MyException('test')
    except Exception:
        e = get_exception()
        assert e
        assert isinstance(e, MyException)
        assert str(e) == 'test'

# Generated at 2022-06-13 04:31:28.896579
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except:
        assert get_exception() is sys.exc_info()[1]

# Generated at 2022-06-13 04:31:41.327404
# Unit test for function get_exception
def test_get_exception():
    try:
        raise NameError
    except NameError:
        assert get_exception().__class__ == NameError
    try:
        raise NameError
    except NameError:
        assert sys.exc_info() == sys.exc_info()

# Generated at 2022-06-13 04:31:44.313155
# Unit test for function get_exception
def test_get_exception():
    import pytest
    try:
        5 / 0
    except ZeroDivisionError:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)

# Generated at 2022-06-13 04:31:48.178078
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except ValueError:
        e = get_exception()
    assert e.args[0] == 'foo'
    assert isinstance(e, ValueError)


# Generated at 2022-06-13 04:31:58.808725
# Unit test for function get_exception
def test_get_exception():
    '''
    Don't test this in the unit tests, it can't be tested.
    '''
    pass


# Generated at 2022-06-13 04:32:09.337567
# Unit test for function get_exception
def test_get_exception():
    # type(None) is not recognized as a type in python2.6 so we have to do
    # the old style of comparison
    class DummyException(object):
        pass
    try:
        raise DummyException('foo')
    except:
        e = get_exception()
        assert isinstance(e, DummyException)
        assert 3 == sys.version_info[0] or 'foo' == e.args[0]
    try:
        eval('foo', {}, {})
    except:
        e = get_exception()
        assert isinstance(e, NameError)
        assert 3 == sys.version_info[0] or 'foo' == e.args[0]

# Generated at 2022-06-13 04:32:12.467291
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('xyz')
    except RuntimeError as e:
        assert get_exception() == e

# Generated at 2022-06-13 04:32:14.924760
# Unit test for function get_exception
def test_get_exception():
    try:
        {}['foo']
    except:
        ex = get_exception()
        assert type(ex).__name__ == 'KeyError'


# unit test for function literal_eval

# Generated at 2022-06-13 04:32:17.720406
# Unit test for function get_exception
def test_get_exception(): # pylint: disable=unused-variable
    class A(Exception):
        pass
    try:
        raise A()
    except Exception:
        assert isinstance(get_exception(), A)

# Generated at 2022-06-13 04:32:21.879079
# Unit test for function get_exception
def test_get_exception():
    def func():
        try:
            raise Exception('a test exception')
        except Exception:
            e = get_exception()
            assert str(e) == 'a test exception'
    func()


# Generated at 2022-06-13 04:32:25.220594
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('caught')
    except Exception:
        assert str(get_exception()) == 'caught'

# Generated at 2022-06-13 04:32:27.412794
# Unit test for function get_exception
def test_get_exception():
    assert get_exception() is None
    try:
        1/0
    except:
        assert type(get_exception()) == ZeroDivisionError

# Generated at 2022-06-13 04:32:29.052510
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except:
        pass



# Generated at 2022-06-13 04:32:32.116289
# Unit test for function get_exception
def test_get_exception():
    def f():
        try:
            raise Exception()
        except Exception:
            return get_exception()
    e = f()
    assert e.__class__ == Exception

# Generated at 2022-06-13 04:32:51.743320
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("foo")
    except:
        e = get_exception()
    assert isinstance(e, ValueError)
    assert str(e) == "foo"

# Unit tests for function literal_eval

# Generated at 2022-06-13 04:32:57.090036
# Unit test for function get_exception
def test_get_exception():
    # Python 3.3 no longer has cStringIO.
    try:
        import cStringIO as StringIO
    except ImportError:
        import StringIO

    class Error(Exception):
        pass

    class ErrorWithTraceback(Exception):
        def __init__(self, message):
            self.message = message
            self.tb = StringIO.StringIO()

    try:
        raise Error("error message")
    except Error as e:
        catched_e = get_exception()
        if catched_e != e:
            raise AssertionError('e != catched_e')

    try:
        raise ErrorWithTraceback("error with traceback")
    except ErrorWithTraceback as e:
        catched_e = get_exception()
        if catched_e != e:
            raise

# Generated at 2022-06-13 04:33:05.136670
# Unit test for function get_exception
def test_get_exception():
    def inner():
        try:
            try:
                raise ValueError('Something is wrong')
            except:
                e = get_exception()
            raise RuntimeError('Something else is wrong')
        except:
            e = get_exception()
        return e

    e = inner()
    if isinstance(e, ValueError):
        print('got a ValueError')
    else:
        print('did not get a ValueError')
    return e

if __name__ == '__main__':  # pragma: no cover
    print(test_get_exception())

# Generated at 2022-06-13 04:33:08.590664
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('oh noes')
    except RuntimeError:
        exc = get_exception()
    assert isinstance(exc, RuntimeError)
    assert exc.args == ('oh noes',)
    assert str(exc) == 'oh noes'


# Generated at 2022-06-13 04:33:13.609419
# Unit test for function get_exception
def test_get_exception():
    import unittest

    class GetExceptionTests(unittest.TestCase):
        def test_exception_is_caught(self):
            """Catching an exception"""
            try:
                raise ValueError('Error Message')
            except Exception:
                exc = get_exception()
                self.assertTrue(isinstance(exc, ValueError))
                self.assertEqual('Error Message', str(exc))

    return unittest.TestLoader().loadTestsFromNames(['test_get_exception'], globals())


# Generated at 2022-06-13 04:33:17.334342
# Unit test for function get_exception
def test_get_exception():
    e = None
    try:
        raise ValueError("Error raised")
    except:
        e = get_exception()
    assert isinstance(e, ValueError)


# Generated at 2022-06-13 04:33:21.558855
# Unit test for function get_exception
def test_get_exception():
    '''test function get_exception
    '''
    try:
        raise ValueError('test')
    except Exception:
        e = get_exception()
    assert e.args[0] == 'test'


# Generated at 2022-06-13 04:33:24.637286
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Test')
    except ValueError as e:
        assert isinstance(get_exception(), ValueError)
        assert get_exception() is e

# Generated at 2022-06-13 04:33:26.658686
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("fooo")
    except Exception as e:
        assert e == get_exception()

# Generated at 2022-06-13 04:33:30.537645
# Unit test for function get_exception
def test_get_exception():
    class FooException(Exception):
        pass

    try:
        raise FooException('blah')
    except FooException:
        e = get_exception()
        assert isinstance(e, FooException)
        assert 'blah' in str(e)

# Generated at 2022-06-13 04:34:06.468151
# Unit test for function get_exception
def test_get_exception():
    try:
        x = 5
        y = 0
        z = x/y
    except Exception:
        ex = get_exception()
        assert ex.__class__.__name__ == 'ZeroDivisionError'


# Unit tests for function literal_eval

# Generated at 2022-06-13 04:34:08.655623
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('This is a test exception')
    except Exception:
        e = get_exception()
        assert str(e) == 'This is a test exception'

# Generated at 2022-06-13 04:34:11.375959
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("This is the exception")
    except ValueError:
        e, = get_exception()
        assert("This is the exception" == str(e))
    else:
        raise AssertionError("Didn't raise an exception")



# Generated at 2022-06-13 04:34:13.032704
# Unit test for function get_exception
def test_get_exception():
    # Test the function on an actual exception
    try:
        raise Exception('foo')
    except:
        assert get_exception() == 'foo'


# Generated at 2022-06-13 04:34:16.492217
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception as e:
        ex = get_exception()
        assert(ex == e)

# Generated at 2022-06-13 04:34:19.490894
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except Exception:
        e = get_exception()

    s = str(e)
    assert "RuntimeError" in s

# Generated at 2022-06-13 04:34:22.070752
# Unit test for function get_exception
def test_get_exception():
    assert not get_exception()
    try:
        raise RuntimeError()
    except:
        assert isinstance(get_exception(), RuntimeError)


# Generated at 2022-06-13 04:34:25.208606
# Unit test for function get_exception
def test_get_exception():
    def foo():
        raise ValueError("Test error")

    try:
        foo()
    except ValueError:
        e = get_exception()
    assert e.args[0] == "Test error"

# Generated at 2022-06-13 04:34:28.741662
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception:
        e = get_exception()
        assert(isinstance(e, ZeroDivisionError))
        assert(str(e) == "integer division or modulo by zero")
        assert(isinstance(e, BaseException))
    else:
        assert False, 'Division by zero did not raise an exception'

# Generated at 2022-06-13 04:34:32.344234
# Unit test for function get_exception
def test_get_exception():
    # Python3 doesn't support this style of code
    exec("""
try:
    raise Exception("Test")
except Exception:
    e = get_exception()
assert(str(e) == "Test")
""")



# Generated at 2022-06-13 04:35:41.758214
# Unit test for function get_exception
def test_get_exception():
    import ansible.module_utils.basic

    def do_raise():
        raise RuntimeError('some error')
    try:
        do_raise()
    except RuntimeError:
        e = get_exception()
        assert e.__class__ == RuntimeError
        assert str(e) == 'some error'


# Generated at 2022-06-13 04:35:43.993258
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("This is a test exception")
    except ValueError:
        e = get_exception()
    assert e.__str__() == "This is a test exception"

# Generated at 2022-06-13 04:35:50.131065
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError(42)
    except ValueError as e:
        # Python 2.6+: directly compare the exception instance variable
        assert e is get_exception()
    try:
        raise ValueError(42)
    except ValueError:
        # Python 2.5 and earlier: compare the string representation of the
        # exception
        assert str(e) == str(get_exception())

# Generated at 2022-06-13 04:35:54.582238
# Unit test for function get_exception
def test_get_exception():
    def f():
        try:
            raise ValueError('foobar')
        except ValueError:
            return get_exception()

    assert f().args == ('foobar', )

    def f():
        try:
            raise ValueError('foobar', 1, 2, 3)
        except ValueError:
            return get_exception()

    assert f().args == ('foobar', 1, 2, 3)



# Generated at 2022-06-13 04:35:56.438154
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Unit test")
    except:
        e = get_exception()
    assert str(e) == "Unit test"

# Generated at 2022-06-13 04:35:58.165547
# Unit test for function get_exception
def test_get_exception():
    def foo():
        try:
            raise Exception('test')
        except Exception:
            return get_exception()
    assert foo().args[0] == 'test'


# Generated at 2022-06-13 04:36:00.051784
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError("hello")
    except TypeError:
        e = get_exception()
        assert e.message == "hello"

# Generated at 2022-06-13 04:36:03.260438
# Unit test for function get_exception
def test_get_exception():
    import os
    try:
        raise Exception('testing')
    except Exception:
        e = get_exception()
        if e.args[0] != 'testing':
            raise AssertionError('Unexpected value for exception: %s' % (e,))

# Unit tests for literal_eval

# Generated at 2022-06-13 04:36:05.723772
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except:
        # We're relying on the fact that Python 2.4-2.6 don't have a 'as' keyword
        # for exceptions
        exc = get_exception()
        assert isinstance(exc, ValueError)


# Generated at 2022-06-13 04:36:07.108875
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('This is a test')
    except ValueError:
        assert get_exception().args[0] == 'This is a test'

# Generated at 2022-06-13 04:38:43.267358
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test')
    except:
        exc = get_exception()
        assert exc.args == ('Test',)

# Generated at 2022-06-13 04:38:46.082978
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test exception')
    except Exception:
        e = get_exception()

    assert e.args == ('test exception',)

# Generated at 2022-06-13 04:38:51.454727
# Unit test for function get_exception
def test_get_exception():
    try:
        raise AssertionError('Unit test')
    except AssertionError:
        e = get_exception()
        assert e
        assert isinstance(e, AssertionError)
        assert "Unit test" in e.args
        assert "Unit test" in str(e)
    else:
        raise AssertionError('Unit test')

if __name__ == '__main__':
    # We want to be able to run this directly from git checkout
    from six.moves import reload_module
    reload_module(sys)
    test_get_exception()

# Generated at 2022-06-13 04:38:55.357838
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foobar')
    except:
        e = get_exception()
        assert isinstance(e, RuntimeError)
        assert e.args == ('foobar',)
        assert str(e) == 'foobar'

# Generated at 2022-06-13 04:39:00.616862
# Unit test for function get_exception
def test_get_exception():
    def inner():
        raise ValueError('test')
    try:
        inner()
    except:
        exc = get_exception()
    if not isinstance(exc, ValueError):
        raise AssertionError('Unexpected type of exception: %s' % type(exc))
    if exc.args != ('test',):
        raise AssertionError('Unexpected exception contents: %r' % (exc.args,))
    print('OK')

# Generated at 2022-06-13 04:39:07.216107
# Unit test for function get_exception
def test_get_exception():
    # Yes, this is a weird unit test, but it's the easiest way to test
    # that get_exception can be used to get the exception object.
    import traceback
    def foo():
        try:
            raise RuntimeError('Test')
        except RuntimeError:
            exc = get_exception()
            if exc.args[0] == 'Test':
                print('Success')
            else:
                print('Failure')
            traceback.print_exc()

    foo()

# Generated at 2022-06-13 04:39:09.501598
# Unit test for function get_exception
def test_get_exception():
    __tracebackhide__ = True
    try:
        raise Exception('foo')
    except:
        e = get_exception()
        assert e.args[0] == 'foo'

# Generated at 2022-06-13 04:39:13.194161
# Unit test for function get_exception

# Generated at 2022-06-13 04:39:16.061589
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Should get this exception')
    except ValueError:
        e = get_exception()
        if str(e) != 'Should get this exception':
            raise AssertionError("'%s' != 'Should get this exception'" % str(e))

# Generated at 2022-06-13 04:39:21.301191
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except ZeroDivisionError:
        exc = get_exception()
    else:
        raise AssertionError("Should have raised a ZeroDivisionError")
    assert isinstance(exc, ZeroDivisionError)

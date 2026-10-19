

# Generated at 2022-06-13 04:31:07.799046
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Something failed')
    except RuntimeError:
        exc = get_exception()
        assert str(exc) == 'Something failed'

# Generated at 2022-06-13 04:31:11.097636
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test_get_exception')
    except ValueError:
        e = get_exception()
    assert e.args[0] == 'test_get_exception'



# Generated at 2022-06-13 04:31:13.665401
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('spline reticulation')
    except RuntimeError as e:
        e2 = get_exception()
        assert(e is e2)
        return True



# Generated at 2022-06-13 04:31:14.525263
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError()
    except ValueError:
        assert get_exception()

# Generated at 2022-06-13 04:31:16.644094
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test exception')
    except:
        e = get_exception()
        assert str(e) == 'test exception'
        assert repr(e) == "Exception('test exception',)"



# Generated at 2022-06-13 04:31:18.804987
# Unit test for function get_exception
def test_get_exception():
    try:
        try:
            raise ValueError('Foo')
        except Exception:
            e = get_exception()
            assert 'Foo' in str(e)
    finally:
        del e


# Generated at 2022-06-13 04:31:22.415347
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except ValueError:
        assert get_exception()


# Generated at 2022-06-13 04:31:26.617722
# Unit test for function get_exception
def test_get_exception():
    def do_test():
        raise Exception('Test exception message')

    try:
        do_test()
    except Exception:
        e = get_exception()
        assert e.__str__() == 'Test exception message', e.__str__()


# Generated at 2022-06-13 04:31:28.572883
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Failed to run")
    except RuntimeError as e:
        assert e == get_exception()

# Generated at 2022-06-13 04:31:32.818987
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception()
    except Exception:
        e = get_exception()
        assert e is not None
        try:
            raise e
        except Exception:
            pass



# Generated at 2022-06-13 04:31:45.197517
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        # Should work
        e = get_exception()
        unused = 1
        assert e.__class__ is ZeroDivisionError


# Generated at 2022-06-13 04:31:48.565835
# Unit test for function get_exception
def test_get_exception():
    def foo():
        try:
            raise Exception('test')
        except:
            return get_exception()

    e = foo()
    assert isinstance(e, Exception)
    assert e.args == ('test', )

# Generated at 2022-06-13 04:31:51.472014
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('This is a test exception')
    except Exception:
        exc = get_exception()
        assert repr(exc) == repr(Exception('This is a test exception'))


# Generated at 2022-06-13 04:31:53.805939
# Unit test for function get_exception
def test_get_exception():
    try:
        1 / 0
    except ZeroDivisionError:
        e = get_exception()
        assert isinstance(e, ZeroDivisionError)

# Generated at 2022-06-13 04:31:57.434585
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("This is an exception")
    except Exception:
        e = get_exception()
        assert str(e) == "This is an exception"

# Generated at 2022-06-13 04:31:59.962863
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)

# Generated at 2022-06-13 04:32:04.977806
# Unit test for function get_exception
def test_get_exception():
    try:
        int('not a number')
    except Exception:
        e = get_exception()
    assert isinstance(e, ValueError), "Wrong type of exception: %s" % type(e)
    assert str(e) == "invalid literal for int() with base 10: 'not a number'", "Wrong exception: %s" % e

# Generated at 2022-06-13 04:32:08.005246
# Unit test for function get_exception
def test_get_exception():
    try:
        x = 1/0
    except Exception:
        e = get_exception()
        assert type(e) == ZeroDivisionError
        assert e.message == 'integer division or modulo by zero'
    else:
        raise Exception('Test setup failed')

# Generated at 2022-06-13 04:32:11.808054
# Unit test for function get_exception
def test_get_exception():
    def foo():
        raise RuntimeError('This is an error message')

    try:
        foo()
    except Exception:
        exception = get_exception()
    else:
        exception = None
    assert isinstance(exception, RuntimeError)
    assert str(exception) == 'This is an error message'


# Generated at 2022-06-13 04:32:15.296796
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except:
        ret = get_exception()
    assert ret == ZeroDivisionError('integer division or modulo by zero')

# Generated at 2022-06-13 04:32:34.604621
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('testing')
    except ValueError:
        assert get_exception() is sys.exc_info()[1]

# Generated at 2022-06-13 04:32:41.624287
# Unit test for function get_exception
def test_get_exception():
    # Use a local import to prevent polluting the namespace.
    import ansible.module_utils.basic
    assert ansible.module_utils.basic.get_exception() is None

    def foo():
        raise RuntimeError()
    try:
        foo()
    except RuntimeError:
        assert isinstance(ansible.module_utils.basic.get_exception(), RuntimeError)

    try:
        1 // 0
    except ZeroDivisionError:
        assert isinstance(ansible.module_utils.basic.get_exception(), ZeroDivisionError)



# Generated at 2022-06-13 04:32:44.912381
# Unit test for function get_exception
def test_get_exception():
    def foo():
        try:
            1 / 0
        except Exception:
            e = get_exception()

        return e

    assert foo().__class__ == ZeroDivisionError


# Generated at 2022-06-13 04:32:46.787856
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foobar')
    except ValueError as e:
        e2 = get_exception()
    assert e == e2

# Generated at 2022-06-13 04:32:50.895849
# Unit test for function get_exception
def test_get_exception():
    try:
        raise NameError('This should be the exception')
    except NameError:
        exc = get_exception()

    assert isinstance(exc, NameError)
    assert exc.args == ('This should be the exception',)


if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:32:53.153437
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Testing')
    except Exception:
        e = get_exception()
        assert e.message == 'Testing'
        assert isinstance(e, Exception)

# Generated at 2022-06-13 04:32:55.717379
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('dummy')
    except ValueError:
        e = get_exception()
        assert e.args == ('dummy',)

# Generated at 2022-06-13 04:33:04.646113
# Unit test for function get_exception
def test_get_exception():
    # None is No Exception
    assert get_exception() is None

    # Make sure that get_exception really does fetch exceptions
    try:
        raise RuntimeError('Test Runtime Error')
    except RuntimeError as e:
        assert e is get_exception()

    # Make sure that get_exception will fetch the second exception in a chain
    # of exceptions
    import ansible.module_utils.six
    try:
        raise RuntimeError('Test Runtime Error')
    except RuntimeError:
        try:
            raise SyntaxError('Test Syntax Error')
        except SyntaxError as e:
            assert e is get_exception()


# Generated at 2022-06-13 04:33:07.092430
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError
    except ValueError:
        e = get_exception()
    assert isinstance(e, ValueError)



# Generated at 2022-06-13 04:33:09.335246
# Unit test for function get_exception
def test_get_exception():  # pragma: no cover
    try:
        raise IndexError('foo')
    except IndexError:
        e = get_exception()
        print(e)


# Generated at 2022-06-13 04:33:45.970938
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('testing get_exception')
    except ValueError:
        e = get_exception()
    assert isinstance(e, ValueError)
    assert 'testing get_exception' in str(e)



# Generated at 2022-06-13 04:33:51.836074
# Unit test for function get_exception
def test_get_exception():
    # If we don't have an active exception, get_exception should return None
    assert get_exception() is None

    # If we have an active exception, it should return it
    try:
        int('a')
    except Exception:
        exc_info = get_exception()
    assert isinstance(exc_info, ValueError)

# Generated at 2022-06-13 04:33:55.332836
# Unit test for function get_exception
def test_get_exception():
    try:
        1/0
    except Exception:
        e = get_exception()
    assert 'ZeroDivisionError' in str(e) and 'division by zero' in str(e)



# Generated at 2022-06-13 04:33:59.696309
# Unit test for function get_exception
def test_get_exception():
    def raises_a():
        try:
            raise ValueError('some message')
        except Exception:
            e = get_exception()

        return e

    def raises_b():
        try:
            raise ValueError('some message')
        except Exception:
            e = sys.exc_info()[1]

        return e

    assert raises_a().args == raises_b().args

# Generated at 2022-06-13 04:34:03.068035
# Unit test for function get_exception
def test_get_exception():
    def f():
        try:
            raise RuntimeError()
        except:
            return get_exception()

    assert f()
    assert f().__class__ == RuntimeError



# Generated at 2022-06-13 04:34:06.181610
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Something broke')
    except Exception:
        exc = get_exception()
        assert exc.args[0] == 'Something broke'
        assert repr(exc) == "RuntimeError('Something broke',)"

# Generated at 2022-06-13 04:34:09.565988
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('This is a unit test for get_exception')
    except Exception:
        e = get_exception()
        if e.args[0] != 'This is a unit test for get_exception':
            raise Exception('Unexpected exception message: %s' % e.args[0])

# Generated at 2022-06-13 04:34:11.441742
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test')
    except Exception:
        e = get_exception()
    assert str(e) == 'test'


# Generated at 2022-06-13 04:34:17.023105
# Unit test for function get_exception
def test_get_exception():
    def inner_function():
        # This line should not be executed.  This is to make sure that the
        # python syntax checker doesn't complain about the line above.
        if True:
            return True

        1 / 0

    outer_function = lambda: inner_function()

# Generated at 2022-06-13 04:34:20.834239
# Unit test for function get_exception
def test_get_exception():
    def test_function():
        try:
            1/0
        except Exception:
            return get_exception()
        assert False, "Should not reach here"

    assert isinstance(test_function(), ZeroDivisionError)


# Generated at 2022-06-13 04:35:30.620586
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Bang!')
    except:
        e = get_exception()
    assert e.args[0] == 'Bang!'
    # Pass


# Generated at 2022-06-13 04:35:36.589274
# Unit test for function get_exception
def test_get_exception():
    def inner():
        def inner():
            raise ValueError('oops')
        try:
            inner()
        except Exception:
            return get_exception()
    try:
        inner()
    except Exception:
        exc = get_exception()
        assert isinstance(exc, ValueError)
        assert str(exc) == 'oops'
    else:
        raise AssertionError('did not get exception')


# Generated at 2022-06-13 04:35:38.383355
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('blah')
    except Exception:
        exception = get_exception()
    assert exception.args[0] == 'blah'



# Generated at 2022-06-13 04:35:40.539713
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('This is a unit test exception')
    except Exception:
        assert get_exception().args == ('This is a unit test exception',)



# Generated at 2022-06-13 04:35:44.366699
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError('foo')
    except Exception:
        e = get_exception()
        assert isinstance(e, TypeError)
        assert str(e) == 'foo'
    try:
        raise TypeError
    except Exception:
        e = get_exception()
        assert isinstance(e, TypeError)
        assert str(e) == ''

# Generated at 2022-06-13 04:35:47.521430
# Unit test for function get_exception
def test_get_exception():
    """Test that the get_exception function returns the exception."""
    try:
        raise ValueError('Test exception')
    except:
        e = get_exception()
    assert e.args[0] == 'Test exception'

# Generated at 2022-06-13 04:35:52.983359
# Unit test for function get_exception
def test_get_exception():
    try:
        raise IndexError('list index out of range')
    except:
        e = get_exception()
    assert e.__class__ == IndexError
    assert str(e) == 'list index out of range'
    try:
        raise ValueError
    except:
        e = get_exception()
    assert e.__class__ == ValueError
    assert str(e) == ''


# Generated at 2022-06-13 04:35:56.601310
# Unit test for function get_exception
def test_get_exception():
    def raise_exception():
        try:
            raise NameError('test')
        except:
            pass

    try:
        raise_exception()
    except:
        exc = get_exception()

    assert isinstance(exc, NameError)
    assert exc.__str__() == 'test'



# Generated at 2022-06-13 04:35:58.452728
# Unit test for function get_exception
def test_get_exception():
    import pytest
    with pytest.raises (Exception):
       raise Exception
    assert get_exception()



# Generated at 2022-06-13 04:36:01.841830
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except:  # noqa
        import traceback
        e = get_exception()
        print(e, traceback.format_exc())

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 04:38:40.114133
# Unit test for function get_exception
def test_get_exception():
    try:
        raise TypeError(u'fo\xe4o')
    except Exception:
        e = get_exception()
        if e.args[0] != 'fo\xc3\xa4o':
            raise AssertionError("get_exception() returned %r, expected 'foäo'" % e.args[0])
        raise RuntimeError(u'bar')
    except Exception:
        e = get_exception()
        if e.args[0] != 'bar':
            raise AssertionError("get_exception() returned %r, expected 'bar'" % e)


# Generated at 2022-06-13 04:38:42.490166
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("This is a test exception")
    except Exception:
        exception = get_exception()
        assert exception.args[0] == "This is a test exception"

# Generated at 2022-06-13 04:38:47.824483
# Unit test for function get_exception
def test_get_exception():
    def f():
        a = 5 // 0  # pylint: disable=pointless-statement
    try:
        f()
    except Exception:
        e = get_exception()
    assert isinstance(e, ZeroDivisionError)

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:38:49.305593
# Unit test for function get_exception

# Generated at 2022-06-13 04:38:52.577672
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Hello")
    except:
        ret = get_exception()
        assert ret.__str__() == "Hello"


# Generated at 2022-06-13 04:38:55.853971
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        if str(e) != 'foo':
            raise AssertionError('get_exception failed')

# Generated at 2022-06-13 04:38:58.436893
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Foo")
    except:
        e = get_exception()

    assert 'Foo' == str(e)

# Generated at 2022-06-13 04:39:01.074812
# Unit test for function get_exception
def test_get_exception():
    class Exception(object):
        pass
    try:
        raise Exception("foo")
    except Exception:
        e = get_exception()
    assert e.args == ("foo",)  # pylint: disable=no-member



# Generated at 2022-06-13 04:39:04.833281
# Unit test for function get_exception
def test_get_exception():
    class AnsibleError(Exception): # pylint: disable=invalid-name
        pass

    try:
        raise AnsibleError("Error for Unit Test")
    except AnsibleError as e:
        e2 = get_exception()
    assert e == e2

# Generated at 2022-06-13 04:39:07.983895
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('who is this')
    except RuntimeError:
        e = get_exception()
        assert e.args == ('who is this',)

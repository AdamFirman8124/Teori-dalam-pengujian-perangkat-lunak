

# Generated at 2022-06-13 04:31:08.942243
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass

    try:
        raise MyException('e is me')
    except Exception:
        e = get_exception()

    assert type(e) == MyException
    assert str(e) == 'e is me'



# Generated at 2022-06-13 04:31:17.230693
# Unit test for function get_exception
def test_get_exception():
    def assert_exception(exception, message):
        try:
            raise exception
        except Exception:
            e = get_exception()
            assert e == exception, '%r != %r: %r' % (e, exception, message)
            assert e.args == exception.args, '%r != %r: %r' % (e.args, exception.args, message)

    assert_exception(Exception('test message'), 'Exception class')
    assert_exception(OSError(13, 'test message'), 'OSError class')
    assert_exception(OSError(13, 'test message'), 'OSError class')
    assert_exception(ValueError('test message'), 'ValueError class')


# Generated at 2022-06-13 04:31:19.634453
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("What is the airspeed of an unladen swallow?")
    except ValueError:
        e = get_exception()
        assert e.args[0] == "What is the airspeed of an unladen swallow?"

# Generated at 2022-06-13 04:31:25.011221
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=undefined-variable
    try:
        raise Exception('blah')
    except Exception:
        e = get_exception()
    assert e.__str__() == 'blah'


# Generated at 2022-06-13 04:31:26.993293
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError
    except:
        assert get_exception()



# Generated at 2022-06-13 04:31:29.244704
# Unit test for function get_exception
def test_get_exception():
    def foo():
        try:
            raise ValueError("bar")
        except Exception:
            e = get_exception()
        return e
    assert foo().args == ('bar', )



# Generated at 2022-06-13 04:31:33.288501
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert e.args[0] == 'foo'

# Generated at 2022-06-13 04:31:35.966225
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError()
    except ValueError:
        e = get_exception()
        assert type(e) is ValueError

# Generated at 2022-06-13 04:31:39.064506
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except Exception:
        e = get_exception()
        assert isinstance(e, RuntimeError)



# Generated at 2022-06-13 04:31:46.033413
# Unit test for function get_exception
def test_get_exception():
    test_passed = False
    try:
        raise ValueError()
    except:
        try:
            # Call code that raises an exception
            raise KeyError()
        except:
            e = get_exception()
            if isinstance(e, KeyError):
                test_passed = True
    assert test_passed

# Generated at 2022-06-13 04:31:58.720013
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('I am an exception')
    except Exception:
        e = get_exception()
        if str(e) != 'I am an exception':
            raise AssertionError('get_exception did not return exception')

# Generated at 2022-06-13 04:32:03.090034
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('Hello World')
    except ValueError:
        pass
    e = get_exception()
    assert e is not None
    assert isinstance(e, ValueError)
    assert str(e) == 'Hello World'

# Generated at 2022-06-13 04:32:04.711124
# Unit test for function get_exception
def test_get_exception():
    try:
        raise AssertionError('foo')
    except AssertionError:
        exception = get_exception()

    assert exception.args[0] == 'foo'

# Generated at 2022-06-13 04:32:06.461425
# Unit test for function get_exception
def test_get_exception():
    try:
        i = 1 / 0
    except Exception as e:
        exc = e
    assert exc == get_exception()

# Generated at 2022-06-13 04:32:11.075629
# Unit test for function get_exception
def test_get_exception():
    # This test method simply runs the code to make sure there are no
    # syntax errors
    try:
        raise Exception('Foo')
    except Exception as e:
        obj = e

    try:
        raise Exception('Bar')
    except Exception as e:
        obj = e
    assert obj.args[0] == 'Bar'


# Generated at 2022-06-13 04:32:16.321186
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('testing exception')
    except ValueError:
        e = get_exception()
    assert isinstance(e, ValueError)
    assert repr(e) == repr(ValueError('testing exception'))
    assert str(e) == 'testing exception'

# Generated at 2022-06-13 04:32:20.562266
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Test exception')
    except Exception:
        e = get_exception()
        assert e.args[0] == 'Test exception'
        print(e)

# Generated at 2022-06-13 04:32:27.119978
# Unit test for function get_exception
def test_get_exception():
    def inner_func():
        return get_exception()

    def middle_func():
        try:
            raise Exception('This should be the return value')
        except Exception:
            return inner_func()
    try:
        raise Exception('This should not be the return value')
    except Exception:
        ex = middle_func()

    assert str(ex) == 'This should be the return value'

# Generated at 2022-06-13 04:32:30.044411
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('foo')
    except Exception:
        e = get_exception()

    if e.args[0] != 'foo':
        raise

# Generated at 2022-06-13 04:32:35.538468
# Unit test for function get_exception
def test_get_exception():
    class TestException(Exception):
        def __init__(self):
            super(TestException, self).__init__("Test Exception")
    try:
        raise TestException
    except Exception:
        e = get_exception()
    assert type(e) == TestException, "Did not get the exception we raised back"

# Generated at 2022-06-13 04:32:56.067353
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except:
        e = get_exception()
        isinstance(e, Exception)
        e.args == ('foo',)


# Generated at 2022-06-13 04:32:59.341270
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('Testing get_exception()')
    except RuntimeError:
        exc = get_exception()
    assert exc.args == ('Testing get_exception()',)

# Generated at 2022-06-13 04:33:03.054624
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("A test exception")
    except ValueError as e:
        assert get_exception() is e
        return
    assert False, "Should not reach this point"


# Generated at 2022-06-13 04:33:06.192645
# Unit test for function get_exception
def test_get_exception():
    """Test that get exception does what it is supposed to do"""
    try:
        raise IndexError
    except IndexError:
        e = get_exception()
        print(e)
        assert isinstance(e, IndexError)

# Generated at 2022-06-13 04:33:10.138390
# Unit test for function get_exception
def test_get_exception():
    class MyException(Exception):
        pass

    try:
        raise MyException('An exception occurred')
    except Exception:
        exc = get_exception()

    assert isinstance(exc, MyException)
    assert exc.args == ('An exception occurred',)
    assert repr(exc) == "MyException('An exception occurred',)"

# Generated at 2022-06-13 04:33:12.342614
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('Ouch!')
    except:
        e = get_exception()
        assert type(e) == Exception
        assert str(e) == 'Ouch!'



# Generated at 2022-06-13 04:33:17.155917
# Unit test for function get_exception
def test_get_exception():
    """
    >>> try:
    ...     raise Exception('this is a test')
    ... except:
    ...     e = get_exception()
    ...     print(e)
    ...
    this is a test
    >>>
    """



# Generated at 2022-06-13 04:33:21.812650
# Unit test for function get_exception
def test_get_exception():
    sys.exc_clear()
    errmsg = "message"
    e = None
    try:
        raise RuntimeError(errmsg)
    except:
        e = get_exception()
    assert e is not None
    assert str(e) == errmsg



# Generated at 2022-06-13 04:33:24.934437
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('expected exception')
    except ValueError:
        assert get_exception().args[0] == 'expected exception'


# Generated at 2022-06-13 04:33:32.603812
# Unit test for function get_exception
def test_get_exception():
    """Unit test for Ansible module utils get exception"""
    def get_exception_test():
        try:
            raise ValueError('foo')
        except Exception:
            return get_exception()

    e = get_exception_test()
    assert isinstance(e, ValueError)
    assert e.args == ('foo',)

    e2 = get_exception()
    assert e2 is None

if __name__ == '__main__':
    test_get_exception()

# Generated at 2022-06-13 04:34:06.509536
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("Test exception")
    except:
        assert get_exception()


# Generated at 2022-06-13 04:34:08.693412
# Unit test for function get_exception
def test_get_exception():
    try:
        foo
    except NameError:
        e = get_exception()
    assert "global name 'foo' is not defined" in str(e)

# Generated at 2022-06-13 04:34:10.480646
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
    assert str(e) == 'foo'

# Generated at 2022-06-13 04:34:11.998732
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError()
    except RuntimeError:
        exc = get_exception()
        assert isinstance(exc, RuntimeError)

# Generated at 2022-06-13 04:34:16.451052
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError("dummy error")
    except Exception:
        e = get_exception()
    assert isinstance(e, ValueError)
    assert str(e) == "dummy error"

# Unit tests for function literal_eval

# Generated at 2022-06-13 04:34:19.040275
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('foo')
    except Exception:
        assert get_exception().args[0] == 'foo'



# Generated at 2022-06-13 04:34:21.222935
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError("Simulated Exception")
    except RuntimeError as e:
        assert get_exception() == e


# Generated at 2022-06-13 04:34:25.831511
# Unit test for function get_exception
def test_get_exception():
    def an_exception(x):
        raise Exception(x)

    e = get_exception()
    assert e is None
    try:
        an_exception(42)
    except Exception:
        e2 = get_exception()
    assert e2.args[0] == 42
    assert e2.args == (42, )



# Generated at 2022-06-13 04:34:28.258603
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError('test')
    except RuntimeError as e:
        assert get_exception() is e

# Generated at 2022-06-13 04:34:31.207442
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('err')
    except Exception:
        e = get_exception()
        assert e.args[0] == 'err'



# Generated at 2022-06-13 04:35:41.578889
# Unit test for function get_exception
def test_get_exception():
    import pytest
    try:
        raise ValueError("This is a test exception")
    except:
        got_exception = get_exception()
        assert type(got_exception) == ValueError
        assert str(got_exception) == "This is a test exception"



# Generated at 2022-06-13 04:35:45.037837
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('test_get_exception')
    except Exception:
        e = get_exception()
        assert str(e) == 'test_get_exception'



# Generated at 2022-06-13 04:35:47.058334
# Unit test for function get_exception
def test_get_exception():
    # pylint: disable=bare-except
    try:
        raise Exception('test exception')
    except:
        e = get_exception()
        assert e.args[0] == 'test exception'

# Generated at 2022-06-13 04:35:48.685488
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("foo bar")
    except Exception:
        e = get_exception()
        assert e.args[0] == "foo bar"


# Generated at 2022-06-13 04:35:52.540775
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('uhoh')
    except:
        # Get the exception
        e = get_exception()

    assert isinstance(e, ValueError)
    assert "uhoh" in str(e)


# Generated at 2022-06-13 04:35:55.414043
# Unit test for function get_exception
def test_get_exception():
    """Test the get_exception function"""
    from ansible.module_utils import basic

    try:
        raise Exception('Test')
    except Exception:
        e = get_exception()
        assert 'Test' in str(e)

# Generated at 2022-06-13 04:35:58.057969
# Unit test for function get_exception
def test_get_exception():
    def inner_function():
        try:
            raise ValueError('This is a test')
        except ValueError:
            return get_exception()

    assert str(inner_function()) == 'This is a test'

# Generated at 2022-06-13 04:36:00.865514
# Unit test for function get_exception
def test_get_exception():
    try:
        raise ValueError('test_get_exception')
    except:
        e = get_exception()
        if e.args[0] != 'test_get_exception':
            raise AssertionError()


# Generated at 2022-06-13 04:36:04.302246
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('hello world')
    except Exception:
        e = get_exception()
        assert str(e) == 'hello world'
    try:
        raise Exception(1, 2, 3)
    except Exception:
        e = get_exception()
        assert str(e) == '(1, 2, 3)'



# Generated at 2022-06-13 04:36:14.216494
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()
        assert e.message == 'foo'
        assert e.args == ('foo', )
    try:
        raise Exception(Exception('foo'))
    except Exception:
        e = get_exception()
        assert e.message == ('foo', )
        assert e.args == ('foo', )
    try:
        raise Exception('foo', Exception('bar'))
    except Exception:
        e = get_exception()
        assert e.message == 'foo'
        assert e.args == ('foo', 'bar')

# Generated at 2022-06-13 04:38:53.444037
# Unit test for function get_exception
def test_get_exception():
    class TestException(Exception):
        pass
    try:
        raise TestException('test exception')
    except:
        e = get_exception()
        assert isinstance(e, TestException)
        assert str(e) == 'test exception'


# Generated at 2022-06-13 04:39:03.310073
# Unit test for function get_exception
def test_get_exception():
    def do_test_get_exception(exception_type, exception_instance):
        '''Make sure get_exception returns the exception we expect'''
        try:
            raise exception_instance
        except exception_type:
            e = get_exception()
            assert isinstance(e, exception_type), \
                "get_exception didn't return the same exception type"
            assert e is exception_instance, \
                "get_exception didn't return the same exception instance"

    do_test_get_exception(ZeroDivisionError, ZeroDivisionError())
    try:
        do_test_get_exception(ZeroDivisionError, ZeroDivisionError())
    except SystemExit as e:
        if e.code == 0:
            # Successfully finished
            pass

# Generated at 2022-06-13 04:39:05.476546
# Unit test for function get_exception
def test_get_exception():
    try:
        ipsum
    except Exception:
        e = get_exception()
        assert str(e) == "name 'ipsum' is not defined"

# Generated at 2022-06-13 04:39:08.617549
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception('foo')
    except Exception:
        e = get_exception()

    assert e.args[0] == 'foo'



# Generated at 2022-06-13 04:39:12.219960
# Unit test for function get_exception
def test_get_exception():
    def inner1():
        return 1 / 0
    def inner2():
        try:
            return inner1()
        except:
            return get_exception()

    exc = inner2()
    assert isinstance(exc, ZeroDivisionError)
    assert '(innermost last)' in str(exc)

# Generated at 2022-06-13 04:39:13.976216
# Unit test for function get_exception
def test_get_exception():
    try:
        raise RuntimeError()
    except Exception:
        exc = get_exception()
        assert isinstance(exc, RuntimeError)

# Generated at 2022-06-13 04:39:15.921896
# Unit test for function get_exception
def test_get_exception():

    def try_raise_exception(e):
        try:
            raise e
        except:
            return get_exception()

    assert try_raise_exception(KeyError('Key error here')) == KeyError('Key error here')



# Generated at 2022-06-13 04:39:26.365234
# Unit test for function get_exception
def test_get_exception():
    '''
    >>> try:
    ...     raise Exception('test exception')
    ... except:
    ...     e = get_exception()
    ...
    >>> print(e)
    test exception

    Unit test for function literal_eval
    >>> literal_eval('1')
    1
    >>> literal_eval('[1,2]')
    [1, 2]
    >>> literal_eval('{"a":1}')
    {'a': 1}
    >>> literal_eval("{'a':1}")
    {'a': 1}
    >>> literal_eval("{u'a':1}")
    {u'a': 1}
    >>> literal_eval("{u'a':1}") == literal_eval("{'a':1}")
    True
    '''
    pass



# Generated at 2022-06-13 04:39:29.227363
# Unit test for function get_exception
def test_get_exception():
    try:
        raise Exception("Test exception")
    except:
        e = get_exception()
        assert e.args == ("Test exception",)

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 04:39:36.896756
# Unit test for function get_exception
def test_get_exception():
    import pytest
    try:
        raise ValueError
    except:
        e = get_exception()
    assert isinstance(e, ValueError)

    try:
        return
    except Exception:
        e = get_exception()
    assert isinstance(e, UnboundLocalError)

    try:
        raise NameError
    except Exception:
        try:
            return
        except:
            e = get_exception()
    assert isinstance(e, UnboundLocalError)

    try:
        raise ValueError
    except Exception:
        try:
            raise NameError
        except:
            e = get_exception()
    assert isinstance(e, NameError)

    try:
        raise ValueError
    except:
        try:
            raise NameError
        except:
            e = get_exception
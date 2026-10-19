

# Generated at 2022-06-14 05:49:08.567402
# Unit test for function ok
def test_ok():
    """Unit test for function ok."""
    with ok(TypeError):
        raise(TypeError)
    with pytest.raises(ValueError):
        raise(ValueError)


# %%

# Generated at 2022-06-14 05:49:11.257982
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with ok(ValueError):
        raise TypeError

# -----------------------------------------------------------------------------



# Generated at 2022-06-14 05:49:15.370474
# Unit test for function ok
def test_ok():
    # No exception
    with ok():
        pass

    # Exception of wrong type
    with ok(ZeroDivisionError):
        1 / 0

    # Exception of correct type
    with ok(TypeError):
        x=1
        x()

# Generated at 2022-06-14 05:49:19.724387
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('N/A')

    with ok(TypeError, ValueError):
        int('N/A')

    with ok(TypeError, ValueError):
        int('5')



# Generated at 2022-06-14 05:49:21.858993
# Unit test for function ok
def test_ok():
    with ok(IndexError):
        raise IndexError('pass')
    assert True



# Generated at 2022-06-14 05:49:24.666934
# Unit test for function ok
def test_ok():
    with ok(ValueError, TypeError):
        pass

    try:
        with ok(ValueError, TypeError):
            raise ValueError
        assert False
    except:
        assert True



# Generated at 2022-06-14 05:49:29.282504
# Unit test for function ok
def test_ok():
    with ok():
        pass

    with ok(AssertionError, KeyError):
        raise KeyError

    with pytest.raises(TypeError):
        with ok(AssertionError, KeyError):
            raise TypeError

# Generated at 2022-06-14 05:49:31.232886
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        print("Trying to divide by zero")
        1 / 0



# Generated at 2022-06-14 05:49:34.700908
# Unit test for function ok
def test_ok():
    with ok(IOError):
        try:
            f = open('file.txt', 'r')
        except FileNotFoundError as e:
            raise IOError(e)
    assert f.closed is True



# Generated at 2022-06-14 05:49:40.506411
# Unit test for function ok
def test_ok():
    with ok(TypeError, ValueError):
        1+"a"
    with ok(TypeError, ValueError):
        raise ValueError("ok")
    with ok(TypeError, KeyboardInterrupt):
        raise KeyboardInterrupt("ok")
    try:
        with ok(TypeError, ValueError):
            1+1
    except Exception as e:
        assert(isinstance(e, Exception))



# Generated at 2022-06-14 05:49:44.232097
# Unit test for function ok
def test_ok():
    assert ok
    with ok(ZeroDivisionError):
        1 / 0



# Generated at 2022-06-14 05:49:46.130617
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0



# Generated at 2022-06-14 05:49:51.826264
# Unit test for function ok
def test_ok():
    # With an exception that must be passed
    with ok(Exception):
        raise Exception('Test exception')

    # With an exception that must be passed but other raise
    with pytest.raises(Exception):
        with ok(ValueError):
            raise Exception('Test exception')

    # Without exception
    with ok():
        pass



# Generated at 2022-06-14 05:49:57.004956
# Unit test for function ok
def test_ok():
    """Test function ok."""
    with ok(ValueError, IOError):
        raise ValueError()
    with ok():
        raise ValueError()
    with ok():
        raise ValueError()
    with ok(ValueError, IOError):
        raise Exception()



# Generated at 2022-06-14 05:50:02.056420
# Unit test for function ok
def test_ok():
    with ok(ValueError, IndexError):
        v = 'a'
        int(v)  # Should raise ValueError
        lst = []
        v = lst[100]  # Should raise IndexError
    # Check if no exceptions are raised
    assert True



# Generated at 2022-06-14 05:50:06.267836
# Unit test for function ok

# Generated at 2022-06-14 05:50:10.844274
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        int('asdf')
    with ok(TypeError):
        asdf
    with ok(TypeError):
        print('asdf')


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:50:17.470197
# Unit test for function ok
def test_ok():
    """Unit test for function ok.
    :return: void
    """
    with ok(Exception):
        1 / 0
    with ok(OSError, IOError):
        1 / 0
    with ok(OSError, IOError, ValueError):
        1 / 0
    with ok(OSError, IOError, ValueError, ZeroDivisionError):
        1 / 0
    with ok(ZeroDivisionError):
        raise ValueError

# Generated at 2022-06-14 05:50:19.574469
# Unit test for function ok
def test_ok():
    """Test function ok"""
    def f():
        raise Exception()

    with ok(Exception):
        f()



# Generated at 2022-06-14 05:50:21.087794
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        print(1+"1")



# Generated at 2022-06-14 05:50:26.450001
# Unit test for function ok
def test_ok():
    try:
        with ok(ZeroDivisionError):
            a = 1 / 0
    except ZeroDivisionError as e:
        assert 0
    except Exception as e:
        assert 1

# Generated at 2022-06-14 05:50:28.815238
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        raise IndexError



# Generated at 2022-06-14 05:50:30.511411
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False



# Generated at 2022-06-14 05:50:32.958252
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        print(1)



# Generated at 2022-06-14 05:50:39.912511
# Unit test for function ok
def test_ok():
    """Unit test for function ok"""
    with ok(ValueError):
        raise ValueError
    with ok(ValueError, TypeError):
        raise ValueError
    with ok(ValueError, TypeError):
        raise TypeError
    with ok(ValueError, TypeError):
        print(5 + '2')
    with ok(TypeError):
        print(5 + '2')



# Generated at 2022-06-14 05:50:43.110648
# Unit test for function ok
def test_ok():
    @ok(AssertionError)
    def test_function():
        assert False, "This test is false"

    test_function()


_TZINFO = None



# Generated at 2022-06-14 05:50:45.631950
# Unit test for function ok
def test_ok():
    with ok(TypeError, ValueError):
        int('N/A')

    with ok(TypeError, ValueError):
        raise KeyboardInterrupt



# Generated at 2022-06-14 05:50:50.185145
# Unit test for function ok
def test_ok():
    try:
        with ok(Exception):
            raise Exception
        assert True
    except Exception:
        assert False

    try:
        with ok(IOError):
            raise Exception
        assert False
    except Exception:
        assert True


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:50:54.073787
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        raise AssertionError
    with raises(ZeroDivisionError):
        with ok(AssertionError):
            rais

# Generated at 2022-06-14 05:50:54.985987
# Unit test for function ok
def test_ok():
    assert ok() is not None



# Generated at 2022-06-14 05:51:05.830428
# Unit test for function ok
def test_ok():
    """Test function ok
    Test function should have name test_ok()
    This is a basic test which test if the function return a context manager
    """
    try:
        with ok():
            raise ValueError
    except ValueError:
        pass
    else:
        assert False, "context manager did not raise exception"

# Generated at 2022-06-14 05:51:10.076313
# Unit test for function ok
def test_ok():
    """Test function ok
    """
    with ok():
        pass
    try:
        with ok():
            raise Exception()
    except Exception:
        pass
    try:
        with ok(ValueError):
            raise ValueError()
        with ok(ValueError):
            raise KeyError()
    except Exception as e:
        assert isinstance(e, KeyError)



# Generated at 2022-06-14 05:51:12.304521
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with ok(ValueError):
        raise TypeError


# Functional programming tools

# Generated at 2022-06-14 05:51:19.076617
# Unit test for function ok
def test_ok():
    """Test Function ok.
    """
    with pytest.raises(Exception):
        with ok():
            raise Exception('Test')

    with ok(ValueError, TypeError):
        raise TypeError('Test')

    with ok(ValueError, TypeError):
        raise ValueError('Test')

    with pytest.raises(Exception):
        with ok(ValueError, TypeError):
            raise Exception('Test')

# Generated at 2022-06-14 05:51:22.152647
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with ok(TypeError):
        pass
    try:
        with ok(ValueError):
            pass
    except TypeError:
        ok(True)

# Generated at 2022-06-14 05:51:27.311916
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError, TypeError):
        1 / 0
    with ok(ZeroDivisionError, TypeError):
        1 / 'a'
    with pytest.raises(KeyError):
        with ok(ZeroDivisionError, TypeError):
            {}['a']



# Generated at 2022-06-14 05:51:30.469141
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        print(10 + "10")
    with ok(TypeError):
        print(10 / 0)


# Context manager for resource allocation-deallocation

# Generated at 2022-06-14 05:51:34.870193
# Unit test for function ok
def test_ok():
    context = None
    with ok(Exception):
        context = 'something'
    assert context == 'something'


try:
    with ok(Exception):
        raise Exception('passed')
except:
    print('error')
else:
    assert True



# Generated at 2022-06-14 05:51:40.538328
# Unit test for function ok
def test_ok():
    """Test function ok.
    """
    with ok():
        pass

    with ok(ValueError):
        4 + "a"

    with ok(TypeError):
        4 + "a"

    # In the following, the exception should be raised
    with raises(ZeroDivisionError):
        4 / 0

# Generated at 2022-06-14 05:51:50.232658
# Unit test for function ok
def test_ok():
    import sys
    import traceback

    class T1(Exception):
        pass

    class T2(Exception):
        pass

    class T3(Exception):
        pass

    from io import StringIO
    s = StringIO()
    try:
        sys.stdout = s
        with ok(T1, T2):
            1 / 0
    except ZeroDivisionError:
        pass
    else:
        assert False, "ZeroDivisionError not raised"
    assert s.getvalue() == ''

    try:
        with ok(T1, T2):
            raise T1()
    except T1:
        pass
    else:
        assert False, "T1 not raised"
    assert s.getvalue() == ''


# Generated at 2022-06-14 05:52:06.168342
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError, TypeError):
        1 / 0
        1 + '1'



# Generated at 2022-06-14 05:52:12.098314
# Unit test for function ok
def test_ok():
    """Unit test for context manager ok"""
    with ok(ValueError):
        print('OK to pass ValueError!')
        raise ValueError()

    with ok(TypeError):
        print('OK to pass TypeError!')
        raise ValueError()


# Make it a module
if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:52:17.730389
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        raise (TypeError, "TypeError raised.")
    try:
        with ok(TypeError):
            raise (ZeroDivisionError, "ZeroDivisionError raised.")
    except ZeroDivisionError:
        pass
    else:
        raise (ValueError, "Wrong Exceptions passed.")



# Generated at 2022-06-14 05:52:21.066278
# Unit test for function ok
def test_ok():
    with ok(IndexError):
        a = [1, 2, 3]
        a[3]

    with pytest.raises(TypeError):
        a = [1, 2, 3]
        a[3]


# Unit for function ok

# Generated at 2022-06-14 05:52:25.960120
# Unit test for function ok
def test_ok():
    with ok(IndexError, NameError):
        [1, 2, 3][10]

    with ok(Exception):
        [1, 2, 3][10]

    with ok(IndexError):
        [1, 2, 3][10]
        raise NameError("Aaron")



# Generated at 2022-06-14 05:52:28.127352
# Unit test for function ok
def test_ok():
    """Test function ok
    """
    with ok(ZeroDivisionError):
        1 / 0



# Generated at 2022-06-14 05:52:30.652128
# Unit test for function ok
def test_ok():
    """
    Test for ok
    """
    assert ok(ZeroDivisionError) is not None

# Generated at 2022-06-14 05:52:34.718163
# Unit test for function ok
def test_ok():
    """Unit test for context manager ok"""
    with ok(Exception):
        raise Exception
    try:
        with ok(Exception):
            raise TypeError
    except TypeError:
        pass
    else:
        raise AssertionError("TypeError not raised")


test_ok()

# Generated at 2022-06-14 05:52:39.555482
# Unit test for function ok
def test_ok():
    """Unit test for function ok

    Ensure that exception thrown by context is NOT passed
    """
    with assert_raises(RuntimeError):
        with ok(ZeroDivisionError):
            print(1 / 0)



# Generated at 2022-06-14 05:52:43.412478
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        with ok(ValueError, TypeError):
            raise ValueError('Test context manager ok.')
    return



# Generated at 2022-06-14 05:53:12.813123
# Unit test for function ok
def test_ok():
    with pytest.raises(ZeroDivisionError):
        with ok(IOError):
            1 / 0

    with ok(IOError):
        1 / 0

# Generated at 2022-06-14 05:53:23.870754
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError

    with ok(IndexError, ValueError):
        raise ValueError

    with ok(IndexError, ValueError):
        raise IndexError

    try:
        with ok(ValueError):
            raise IndexError
    except IndexError:
        pass
    else:
        assert False, "The except IndexError was not executed"

    try:
        with ok(IndexError, ValueError):
            raise NameError
    except NameError:
        pass
    else:
        assert False, "The except NameError was not executed"

    # test if exceptions are passed by reference
    def test():
        with ok(IndexError, ValueError):
            raise ValueError

    try:
        test()
    except ValueError:
        pass

# Generated at 2022-06-14 05:53:25.741386
# Unit test for function ok
def test_ok():
    with ok():
        pass



# Generated at 2022-06-14 05:53:35.221876
# Unit test for function ok
def test_ok():
    """Test ok() function."""
    # All ok
    with ok(ValueError):
        pass
    # Simple error
    with pytest.raises(TypeError):
        with ok(ValueError):
            raise TypeError
    # Check if an error of the right type is also passed
    with ok(ValueError, TypeError):
        raise TypeError
    # Check that an error of the wrong type is not passed,
    # and the right type is raised
    with pytest.raises(ValueError):
        with ok(ValueError, TypeError):
            raise ValueError


# Generated at 2022-06-14 05:53:38.980547
# Unit test for function ok
def test_ok():
    with ok(TypeError, ValueError):
        raise TypeError()
    with raises(ZeroDivisionError):
        with ok(TypeError, ValueError):
            raise ZeroDivisionError()

# Generated at 2022-06-14 05:53:41.168037
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise Exception
    with ok(Exception):
        raise IOError

# Generated at 2022-06-14 05:53:42.607497
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError()



# Generated at 2022-06-14 05:53:51.702688
# Unit test for function ok
def test_ok():
    """Unit test for function ok
    Test case:
    - Test with the exception ZeroDivisionError
    - Test with the exception IndentationError
    - Test with the exception IndexError
    - Test with the exception Exception
    """
    with ok(ZeroDivisionError):
        print(1 / 0)
    with ok(ZeroDivisionError, IndentationError):
        print(1 / 0)
    with ok(ZeroDivisionError, IndentationError):
        print(1 / 0)
    with ok(ZeroDivisionError, IndentationError):
        print(1 / 0)
        print(1 + a)


if __name__ == "__main__":
    test_ok()

# Generated at 2022-06-14 05:53:56.488832
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        print("hi")

    with ok(TypeError, ValueError):
        pass

    with ok(TypeError, ValueError):
        raise TypeError

    with ok(TypeError, ValueError):
        raise ValueError

    with raises(ZeroDivisionError):
        with ok(TypeError, ValueError):
            raise ZeroDivisionError



# Generated at 2022-06-14 05:54:01.123599
# Unit test for function ok
def test_ok():
    """ Unit test for function ok """
    with ok(TypeError, ValueError):
        int('1')
    try:
        int('a')
    except Exception as e:
        if isinstance(e, ValueError):
            assert True
        else:
            assert False



# Generated at 2022-06-14 05:54:58.470960
# Unit test for function ok
def test_ok():
    with ok(IndexError, KeyError):
        raise IndexError
    with ok(IndexError, KeyError):
        raise KeyError
    with ok(IndexError, KeyError) as cm:
        raise TypeError
    with raises(TypeError):
        cm.__exit__(None, None, None)

    with ok(Exception):
        raise ValueError
    with raises(ValueError):
        with ok(AssertionError):
            raise ValueError



# Generated at 2022-06-14 05:55:02.205297
# Unit test for function ok
def test_ok():
    with ok(Exception):
        pass

    try:
        with ok(Exception):
            raise Exception()
    except Exception:
        assert False

    try:
        with ok(Exception):
            raise ValueError()
    except ValueError:
        pass



# Generated at 2022-06-14 05:55:09.313796
# Unit test for function ok
def test_ok():
    with ok(NameError):
        print("Hi, ugly_nature!")
    with ok(NameError):
        print("Hi, ugly_nature!")
        raise NameError
        print("Do you wanna hear a joke?")
    with ok(AttributeError):
        print("Hi, ugly_nature!")
        raise NameError
        print("Do you wanna hear a joke?")



# Generated at 2022-06-14 05:55:10.993662
# Unit test for function ok
def test_ok():
    with ok():
        raise Exception('this is an error')



# Generated at 2022-06-14 05:55:20.738411
# Unit test for function ok
def test_ok():
    """Unit test for function ok"""

    # Check if simple raise exception case works
    with ok():
        assert True
    with pytest.raises(Exception):
        with ok():
            raise AttributeError

    # Check if function raises exception when it should
    with pytest.raises(Exception):
        with ok(AttributeError):
            raise Exception

    # Check function doesn't raise exception when it shouldn't
    with ok(AttributeError):
        assert True

    # Check if function correctly passes exception
    with ok(AttributeError):
        raise AttributeError
    with pytest.raises(AttributeError):
        with ok():
            raise AttributeError

# Generated at 2022-06-14 05:55:23.098801
# Unit test for function ok
def test_ok():
    """Unit test for function ok"""
    with ok(ValueError):
        pass



# Generated at 2022-06-14 05:55:27.763449
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False

    with ok(AssertionError, IndexError):
        assert False

    with ok(IndexError):
        x = []
        x[1]

    with raises(ZeroDivisionError):
        with ok(AssertionError):
            1 / 0

# Generated at 2022-06-14 05:55:29.159207
# Unit test for function ok
def test_ok():
    with ok(TypeError, ZeroDivisionError):
        pass



# Generated at 2022-06-14 05:55:32.317283
# Unit test for function ok
def test_ok():
    with ok():
        raise AssertionError("Should break inner scope, not outer scope")
    try:
        with ok(ZeroDivisionError):
            raise ValueError
    except ValueError:
        pass
    else:
        assert False, "ok context manager doesn't raise the right exception"



# Generated at 2022-06-14 05:55:43.549243
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0
    with ok(OSError, IndexError):
        raise IndexError
    with ok(OSError, IndexError):
        raise OSError
    with ok(ZeroDivisionError):
        with ok(IndexError):
            raise IndexError
    try:
        with ok(OSError):
            raise ValueError
    except ValueError:
        pass
    try:
        with ok(OSError):
            raise KeyError
    except KeyError:
        pass
    try:
        with ok(OSError, IndexError):
            raise ValueError
    except ValueError:
        pass



# Generated at 2022-06-14 05:57:39.257435
# Unit test for function ok
def test_ok():
    with ok():
        raise ValueError

    with ok(ValueError):
        raise ValueError

    with raises(TypeError):
        with ok(ValueError):
            raise TypeError



# Generated at 2022-06-14 05:57:42.994272
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with ok():
        print(1)
        raise ValueError
    with ok(ValueError):
        print(2)
        raise TypeError
    with ok(TypeError):
        print(3)
        raise ValueError

test_ok()

# Generated at 2022-06-14 05:57:47.575578
# Unit test for function ok
def test_ok():
    with ok(RuntimeError):
        raise RuntimeError
    with ok(RuntimeError):
        raise TypeError
        # ValueError is not raised
    with ok(RuntimeError):
        raise MemoryError
        # MemoryError is not raised



# Generated at 2022-06-14 05:57:54.627666
# Unit test for function ok
def test_ok():
    # Check that the context manager allows exceptions to be re-raised
    with pytest.raises(Exception):
        with ok(Exception):
            raise Exception("test")
    # Check that exceptions are not passed if the are not in the given list
    with pytest.raises(ValueError):
        with ok(IndexError):
            raise ValueError("test")
    # Check that exceptions in the given list passed
    with ok(TypeError):
        raise TypeError("test")



# Generated at 2022-06-14 05:57:59.345308
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError('message')
    with ok(ValueError):
        pass

    with pytest.raises(ValueError) as excinfo:
        with ok(TypeError):
            raise ValueError('message')

    assert excinfo.value.args[0] == 'message'

# Generated at 2022-06-14 05:58:02.651793
# Unit test for function ok
def test_ok():
    """Unit test for function ok()."""
    try:
        with ok(ZeroDivisionError):
            1 / 0
    except ZeroDivisionError:
        pytest.fail('ok() failed to pass exception.')

# Generated at 2022-06-14 05:58:06.857009
# Unit test for function ok
def test_ok():
    """Tests basic functionality of the context manager."""

    with ok(Exception):
        raise ValueError('error')

    with raises(AttributeError):
        with ok(ValueError):
            raise AttributeError('error')



# Generated at 2022-06-14 05:58:12.666257
# Unit test for function ok
def test_ok():
    """Test function ok()"""
    with ok(ValueError):
        raise ValueError()
    with pytest.raises(ZeroDivisionError):
        with ok(ValueError):
            raise ZeroDivisionError()
    with pytest.raises(IndexError):
        with ok(ValueError):
            raise IndexError()



# Generated at 2022-06-14 05:58:23.586567
# Unit test for function ok
def test_ok():
    """
    Test the ok context manager.
    """
    with ok(TypeError):
        raise TypeError

    with ok(ZeroDivisionError):
        raise ZeroDivisionError

    with ok(IndexError):
        pass

    with ok(TypeError):
        pass

    with ok(TypeError, ZeroDivisionError):
        raise ZeroDivisionError

    with ok(TypeError, ZeroDivisionError):
        raise TypeError

    with ok():
    # We can pass no exceptions
        pass

    # If a wrong exception is raised, re-raise it
    with ok(ZeroDivisionError):
        raise IndexError


# Run the unit tests
test_ok()

# Generated at 2022-06-14 05:58:27.676420
# Unit test for function ok
def test_ok():
    with ok(FileNotFoundError):
        raise FileNotFoundError()

    with ok(ValueError):
        raise ValueError()

    with ok(FileNotFoundError):
        raise PermissionError()


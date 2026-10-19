

# Generated at 2022-06-14 05:49:12.117935
# Unit test for function ok
def test_ok():
    """Test ok function
    """
    # Test with pass
    with ok(ZeroDivisionError, ImportError):
        a = 1 / 0
    assert a == ZeroDivisionError

    # Test with raise
    try:
        with ok(ZeroDivisionError):
            a = 1 / 0
    except Exception as e:
        assert isinstance(e, ZeroDivisionError)


if __name__ == "__main__":
    test_ok()
    print("Everything passed")

# Generated at 2022-06-14 05:49:17.236003
# Unit test for function ok
def test_ok():
    # Normal usage
    with ok():
        pass

    # Exception raised, no exception specified
    with ok(Exception):
        raise Exception("test")

    # Exception raised, exception specified
    with ok(ArithmeticError):
        raise ArithmeticError("test")

# Generated at 2022-06-14 05:49:22.700861
# Unit test for function ok
def test_ok():
    with ok((TypeError, ValueError), ZeroDivisionError):
        1 + '1'
    try:
        with ok(TypeError):
            5 / 0
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError('Expected exceptions not occurred')


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:49:25.391487
# Unit test for function ok
def test_ok():
    try:
        with ok():
            raise Exception()
    except Exception:
        return True
    else:
        return False


print('Test for function "ok": ', test_ok())



# Generated at 2022-06-14 05:49:37.060985
# Unit test for function ok
def test_ok():
    def mess(func, *exceptions):
        try:
            func()
        except Exception as e:
            if isinstance(e, exceptions):
                print("{0} => {1}: OK".format(
                    func.__name__, e.__class__.__name__))
            else:
                print("{0} => {1}: FAIL".format(
                    func.__name__, e.__class__.__name__))
    tests = [lambda: 1 / 0, lambda: x + 1, lambda: {}["key"]]
    [mess(test, ZeroDivisionError) for test in tests]
    [mess(test, ZeroDivisionError, NameError) for test in tests]
    [mess(test, ZeroDivisionError, NameError, KeyError) for test in tests]

# Generated at 2022-06-14 05:49:40.825563
# Unit test for function ok
def test_ok():
    """Test function ok."""
    with ok():
        a = 1
    assert a == 1
    with ok(Exception):
        b = [1, 2, 3]
        print(b[3])
    with ok(ZeroDivisionError):
        c = 1 / 0
    assert c == 1



# Generated at 2022-06-14 05:49:46.063428
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        print("ok")
    with ok(ValueError):
        print("ok")
        raise ValueError
    with pytest.raises(RuntimeError):
        with ok(ValueError):
            print("no ok")
            raise RuntimeError



# Generated at 2022-06-14 05:49:56.350213
# Unit test for function ok
def test_ok():
    def dummy():
        try:
            with ok():
                pass
        except Exception:
            return False
        else:
            return True

    assert(dummy())

    def dummy2():
        try:
            with ok(Exception):
                raise Exception()
        except Exception:
            return False
        else:
            return True

    assert(dummy2())

    def dummy3():
        try:
            with ok(Exception):
                raise ValueError()
        except Exception:
            return True
        else:
            return False

    assert(dummy3())

    def dummy4():
        try:
            with ok(Exception, ValueError):
                raise ValueError()
        except Exception:
            return False
        else:
            return True

    assert(dummy4())


# Generated at 2022-06-14 05:49:58.538001
# Unit test for function ok
def test_ok():
    """Test function ok."""
    with ok(Exception):
        raise Exception()



# Generated at 2022-06-14 05:50:02.169337
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('asdasd')

    with raises(TypeError):
        with ok(ValueError):
            int(None)



# Generated at 2022-06-14 05:50:09.645701
# Unit test for function ok
def test_ok():
    """Standalone Testcase"""
    # Test whether exception is raised
    with ok(ValueError, IndexError):
        x = ["apple", "bob"]
        y = x[2]



# Generated at 2022-06-14 05:50:13.730378
# Unit test for function ok
def test_ok():
    """Function test_ok() to test the context manager ok."""
    with ok(Exception):
        raise Exception('ok')


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:50:15.718085
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('N/A')


print(test_ok())

# Generated at 2022-06-14 05:50:19.682927
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise Exception('test')

    with raises(Exception):
        with ok(StopIteration):
            raise Exception('test')

    with raises(Exception):
        with ok(StopIteration):
            raise StopIteration('test')

# Generated at 2022-06-14 05:50:23.354110
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0

    with ok(ValueError, ZeroDivisionError):
        1 / 0

    with ok():
        1 / 0

    with ok(ValueError):
        1 / 1



# Generated at 2022-06-14 05:50:25.586672
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError()


if __name__ == "__main__":
    test_ok()

# Generated at 2022-06-14 05:50:38.055067
# Unit test for function ok
def test_ok():
    """Test for the ok() context manager.
    """

    def get_file(filename):
        """Yield a sequence of lines from a file.

        :param filename: Name of file to read. 
        """
        with open(filename, 'rb') as f:
            for line in f:
                yield line


    # Will raise StopIteration exception
    # with ok(StopIteration):
    #     get_file('sample.txt').next()

    # Will raise IOError exception 
    # with ok(StopIteration, IOError):
    #     get_file('sample.txt').next()

    # Will raise Exception exception
    with ok(StopIteration, IOError):
        get_file('wrong.txt').next()

if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:50:45.490799
# Unit test for function ok
def test_ok():
    with ok():
       pass
    with ok(ValueError):
        raise ValueError()
    with ok(IndexError, ValueError):
        raise ValueError()
    with ok(IndexError, ValueError):
        raise IndexError()
    with ok(IndexError, ValueError):
        raise TypeError()
    with raises(TypeError):
        with ok():
            raise TypeError()
    with raises(TypeError):
        with ok(IndexError):
            raise TypeError()

# Generated at 2022-06-14 05:50:57.157488
# Unit test for function ok
def test_ok():
    try:
        with ok(ValueError, TypeError):
            raise ValueError('test')
    except ValueError:
        pass

    try:
        with ok(ValueError, TypeError):
            raise TypeError('test')
    except TypeError:
        pass

    try:
        with ok(ValueError, TypeError):
            raise NameError('test')
    except NameError:
        pass

    try:
        with ok(ValueError, TypeError):
            raise NameError('test')
    except NameError:
        pass

    try:
        with ok(int):
            raise TypeError('test')
    except TypeError:
        pass

    try:
        with ok(TypeError):
            raise TypeError('test')
    except TypeError:
        pass


# Generated at 2022-06-14 05:51:10.269792
# Unit test for function ok
def test_ok():
    # Test for a specific exception
    try:
        with ok(TypeError):
            raise TypeError
        with ok(TypeError):
            raise KeyError
    except TypeError:
        pass
    except:
        raise AssertionError("Don't raise a valid exception")
    else:
        raise AssertionError("Don't raise a valid exception")

    with ok(KeyError, TypeError):
        raise TypeError

    try:
        with ok(KeyError, TypeError):
            raise KeyError
        with ok(KeyError, TypeError):
            raise AssertionError()
    except KeyError:
        pass
    except:
        raise AssertionError("Don't raise a valid exception")
    else:
        raise AssertionError("Don't raise a valid exception")



# Generated at 2022-06-14 05:51:25.458841
# Unit test for function ok
def test_ok():
    """Unit test for function ok"""

    class CustomError(Exception):
        pass

    class CustomError2(Exception):
        pass

    with ok(ValueError):
        print("in with")
        raise ValueError("Catched this ok")

    try:
        with ok(ValueError):
            print("in with")
            raise AttributeError("Uncatched this failed")
    except AttributeError:
        assert True
    else:
        assert False

    try:
        with ok(ValueError, CustomError):
            raise CustomError("Catched this ok")
    except CustomError:
        assert True
    else:
        assert False

    try:
        with ok(CustomError, ValueError):
            raise CustomError2("Uncatched this failed")
    except CustomError2:
        assert True
    else:
        assert False

# Generated at 2022-06-14 05:51:28.096739
# Unit test for function ok
def test_ok():
    class CustomError(Exception):
        ...

    with ok(CustomError):
        raise CustomError
        print('Error')



# Generated at 2022-06-14 05:51:37.751693
# Unit test for function ok
def test_ok():

    with ok():
        print("No exception:")

    with ok(TypeError, ValueError):
        print("No exception:")

    with ok(TypeError, ValueError):
        print("No exception:")
        raise Exception("Exception!")

    with ok(TypeError, ValueError):
        print("TypeError:")
        raise TypeError

    with ok(TypeError, ValueError):
        with ok(TypeError, ValueError):
            print("TypeError:")
            raise TypeError

    with ok(TypeError, ValueError):
        with ok():
            print("TypeError:")
            raise TypeError

    with ok(TypeError, ValueError):
        with ok(Exception):
            print("TypeError:")
            raise TypeError

    with ok(TypeError, ValueError):
        with ok(TypeError):
            print

# Generated at 2022-06-14 05:51:43.779280
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError()
    with ok(ValueError, TypeError):
        raise ValueError()
    with ok(ValueError, TypeError):
        raise TypeError()
    with raises(TypeError):
        with ok(ValueError):
            raise TypeError()



# Generated at 2022-06-14 05:51:47.619357
# Unit test for function ok
def test_ok():
    with pytest.raises(IndexError):
        with ok(ValueError, TypeError):
            raise IndexError

    with ok(ValueError, TypeError):
        raise TypeError

    with ok(ValueError, TypeError):
        raise ValueError



# Generated at 2022-06-14 05:51:52.822783
# Unit test for function ok
def test_ok():
    with pytest.raises(TypeError):
        with ok(TypeError):
            raise ValueError
    with ok(TypeError):
        raise TypeError


###############################################################################
# Functions and classes to estimate the metrics: Precision, Recall and F-Score #
###############################################################################


# Function to calculate precision

# Generated at 2022-06-14 05:51:55.068616
# Unit test for function ok
def test_ok():
    with ok():
        1 + 1
    # This should fail:
    1 / 0



# Generated at 2022-06-14 05:52:01.682965
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        5 / 0
    try:
        with ok(ValueError):
            5 / 0
    except ZeroDivisionError:
        pass
    else:
        raise RuntimeError("ZeroDivisionError should have been raised")



# Generated at 2022-06-14 05:52:02.324171
# Unit test for function ok
def test_ok():
    assert True

# Generated at 2022-06-14 05:52:07.699875
# Unit test for function ok
def test_ok():
    ok_tuple = (TypeError, IndexError)
    with ok(*ok_tuple):
        l = [1, 2, 3]
        int('s')
        l[100]
    with raises(AttributeError):
        with ok(*ok_tuple):
            'hello'.index()


# Generated at 2022-06-14 05:52:18.530498
# Unit test for function ok
def test_ok():
    assert_raises(ZeroDivisionError, ok(), lambda: 1 / 0)
    assert_raises(AssertionError, ok(ZeroDivisionError), lambda: 1 / 0)
    assert_raises(AssertionError, ok(AssertionError), lambda: 1)

    assert_raises(ZeroDivisionError, ok(ValueError), lambda: 1 / 0)
    assert_raises(ValueError, ok(ZeroDivisionError), lambda: 1)



# Generated at 2022-06-14 05:52:25.122960
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False

    with ok(AssertionError):
        assert True

    try:
        with ok(AssertionError):
            assert False

            # Should not be executed since the assertion raises an error
            assert True
    except Exception as e:
        print('Caught an exception which is {0}'.format(e))



# Generated at 2022-06-14 05:52:29.933457
# Unit test for function ok
def test_ok():
    with pytest.raises(TypeError):
        with ok(TypeError):
            raise TypeError()
    with ok(TypeError):
        raise ValueError()
    # with pytest.raises(ValueError):
    with ok():
        raise ValueError()
    with ok():
        pass



# Generated at 2022-06-14 05:52:34.527534
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        a = 0
        int(a)
    with ok(ValueError, TypeError):
        b = 0
        int(b)
    with ok():
        b = 0
        int(b)
    with ok(ValueError):
        a = 0
        int("a")



# Generated at 2022-06-14 05:52:38.432703
# Unit test for function ok
def test_ok():
    with ok():
        pass

    with pytest.raises(ImportError):
        with ok(ValueError):
            raise ImportError



# Generated at 2022-06-14 05:52:42.412817
# Unit test for function ok
def test_ok():
    import math

    with ok(ZeroDivisionError):
        a = 1 / 0
    with ok(ZeroDivisionError):
        a = math.sqrt(-1)


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:52:49.749905
# Unit test for function ok
def test_ok():
    try:
        with ok(TypeError):
            print('ok')
    except Exception as e:
        print(e)
    try:
        with ok(TypeError):
            raise TypeError('Test')
    except Exception as e:
        print(e)
    try:
        with ok(TypeError):
            raise ValueError('Test')
    except Exception as e:
        print(e)



# Generated at 2022-06-14 05:52:53.895632
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        print(1/0)
    print("Whoa..")


# The same as above, but using object as exception

# Generated at 2022-06-14 05:53:01.325819
# Unit test for function ok
def test_ok():
    """Unit test for function ok."""
    with ok():
        pass
    try:
        with ok():
            raise ValueError
    except ValueError:
        pass
    try:
        with ok(TypeError):
            raise ValueError
    except ValueError:
        pass
    try:
        with ok(TypeError, ValueError):
            raise TypeError
    except TypeError:
        pass



# Generated at 2022-06-14 05:53:05.142419
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise Exception

    try:
        with ok(RuntimeError):
            raise Exception
    except Exception as e:
        assert isinstance(e, Exception)



# Generated at 2022-06-14 05:53:23.485891
# Unit test for function ok
def test_ok():
    """Unit test for function ok."""
    # pylint: disable=W0201, R0913, W0212
    class TestException(Exception):
        pass

    class TestException2(Exception):
        pass

    class TestException3(TestException2):
        pass

    def test(exceptions, raises):
        with ok(*exceptions):
            raise raises

    # Test a single exception type
    assert test((TestException,), TestException()) is None
    assert test((TestException,), Exception())

    # Test multiple exception types
    assert test((TestException, TestException2), TestException()) is None
    assert test((TestException, TestException2), TestException2()) is None
    assert test((TestException, TestException2), TestException3())
    assert test((TestException, TestException2), Exception())

    # Test passing Der

# Generated at 2022-06-14 05:53:29.395123
# Unit test for function ok
def test_ok():
    """Test function ok"""
    # Testing that an exception is caught
    with ok (TypeError):
        print ("hello") + 2

    # Testing that an exception is raised
    with pytest.raises(ZeroDivisionError):
        with ok (TypeError):
            print (1/0)



# Generated at 2022-06-14 05:53:37.294654
# Unit test for function ok
def test_ok():
    """Test for function ok."""
    # This is legitimate,
    # there is no reason to fail
    assert ok()

    # Failing assertions are expected to raise an exception
    with pytest.raises(Exception):
        with ok(AssertionError):
            assert False

    # Regular exceptions are not propagated
    with ok(AssertionError):
        raise Exception

    # This is still raising an exception
    with pytest.raises(Exception):
        with ok(AssertionError):
            raise Exception



# Generated at 2022-06-14 05:53:40.157363
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError, AssertionError):
        assert 1 == 1
        assert 1 == 0



# Generated at 2022-06-14 05:53:44.592867
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        pass

    with ok(ValueError, TypeError):
        pass

    with ok(ValueError):
        raise ValueError("test")

    with ok(TypeError):
        raise TypeError("test")



# Generated at 2022-06-14 05:53:49.963947
# Unit test for function ok
def test_ok():
    """Unit test for function ok."""
    # Pass an exception
    with ok(IOError, NameError):
        raise IOError
    assert True

    # Fail an exception
    try:
        with ok(IOError, NameError):
            raise SyntaxError
    except SyntaxError:
        pass



# Generated at 2022-06-14 05:53:51.419904
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise Exception
        print('ok')



# Generated at 2022-06-14 05:53:53.335280
# Unit test for function ok
def test_ok():
    with ok(OSError):
        pass  # use here something that raises the exception



# Generated at 2022-06-14 05:53:55.474663
# Unit test for function ok
def test_ok():
    with ok():
        pass



# Generated at 2022-06-14 05:54:01.067534
# Unit test for function ok
def test_ok():
    """Unit test for function ok
    """
    with ok(TypeError, IndexError):
        [1, 2, 3][3] = "a string"

    with ok(TypeError, IndexError):
        int("a string")

    with ok(TypeError, IndexError):
        raise KeyError("some exception")



# Generated at 2022-06-14 05:54:24.580075
# Unit test for function ok
def test_ok():
    print('Unit testing function ok ... ', end='')

    class CustomException(Exception):
        pass

    # Exceptions are correct => pass
    try:
        with ok(Exception):
            raise Exception
        with ok(BaseException):
            raise Exception
        with ok(BaseException, CustomException):
            raise Exception
    except:
        assert False, 'Error: exception was caught despite function ok'

    # Exceptions are wrong => raise exception
    try:
        with ok(CustomException):
            raise Exception
    except:
        pass
    else:
        assert False, 'Error: exception was not caught'

    print('Pass')


test_ok()

# Generated at 2022-06-14 05:54:30.115347
# Unit test for function ok
def test_ok():
    """Unit test for function ok"""
    with ok(TypeError, NameError):
        raise TypeError()
    with ok(TypeError, NameError):
        raise NameError()
    try:
        with ok(TypeError, NameError):
            raise IndexError()
        raise AssertionError("function ok failed")
    except IndexError:
        pass

# Generated at 2022-06-14 05:54:41.479785
# Unit test for function ok
def test_ok():
    def square_error(x):
        if x == 0:
            raise ZeroDivisionError
        return 1 / x

    # function raises only ZeroDivisionError
    # it won't be passed
    with pytest.raises(ZeroDivisionError):
        with ok(TypeError):
            square_error(0)

    # function raises only ZeroDivisionError
    # it will be passed
    with ok(ZeroDivisionError):
        value = square_error(0)
        assert value == 0

    # function raises TypeError
    # it will be passed
    with ok(ZeroDivisionError, TypeError):
        value = square_error("ABC")
        assert value == 0

# Generated at 2022-06-14 05:54:49.564486
# Unit test for function ok
def test_ok():
    """Test correct usage of context manager ok
    """
    with ok():
        pass
    with ok():
        raise ValueError("Value error")

    # Function ok to pass exception ValueError
    with ok(ValueError):
        raise ValueError("Value error")

# Generated at 2022-06-14 05:54:53.152309
# Unit test for function ok
def test_ok():
    with pytest.raises(ValueError):
        with ok(ValueError):
            raise ValueError

    with ok(ValueError):
        raise TypeError



# Generated at 2022-06-14 05:54:57.525801
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise Exception("Error")
    with ok(Exception, TypeError):
        raise TypeError("Error")
    with ok():
        raise ValueError("Error")
    try:
        with ok():
            raise ValueError("Error")
    except ValueError:
        pass
    else:
        assert False



# Generated at 2022-06-14 05:55:01.417699
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0
    try:
        with ok(TypeError):
            1 / 0
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("Did not raise ZeroDivisionError")



# Generated at 2022-06-14 05:55:08.465502
# Unit test for function ok
def test_ok():
    """Unit test for ok function."""
    with ok(TypeError):
        raise TypeError
    with ok(TypeError, ZeroDivisionError):
        raise TypeError
        raise ZeroDivisionError
    with ok(TypeError, ZeroDivisionError):
        raise TypeError
        raise ZeroDivisionError
    with raises(ZeroDivisionError):
        with ok(TypeError, ZeroDivisionError):
            raise ZeroDivisionError

# Generated at 2022-06-14 05:55:18.876852
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0
    with ok(ZeroDivisionError):
        raise ZeroDivisionError
    with ok(ZeroDivisionError):
        raise KeyError


# /////////////////////////////////////////////////////////////////////////////
#
# Exercise 2.
# Write a context manager, which timestamps every operation.
#
# Example usage:
#
# >>> with timestamps():
# ...     print("Hello")
# ...     print("World")
# ...
# [2018-02-15 15:24:04]    Hello
# [2018-02-15 15:24:04]    World
#
# /////////////////////////////////////////////////////////////////////////////
from datetime import datetime



# Generated at 2022-06-14 05:55:20.447835
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1/0



# Generated at 2022-06-14 05:56:03.521763
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise Exception
    with ok(ValueError):
        pass
    with ok(TypeError):
        pass
    with ok(Exception, TypeError):
        pass
    with ok(TypeError, Exception):
        pass
    with ok(Exception, TypeError, ValueError):
        pass
    with ok(ValueError, TypeError, Exception):
        raise Exception
    with ok(ValueError, TypeError, Exception):
        raise TypeError
    with ok(ValueError, TypeError, Exception):
        raise ValueError
    with ok(ValueError, TypeError, Exception):
        raise ValueError
    with ok(Exception, ValueError, TypeError):
        raise ValueError
    with ok(TypeError, Exception, ValueError):
        raise ValueError
    with ok(TypeError, ValueError, Exception):
        raise ValueError

# Generated at 2022-06-14 05:56:12.837274
# Unit test for function ok
def test_ok():
    # Case 1
    with ok():
        print('No exceptions!')

    # Case 2
    with ok(TypeError):
        print('TypeError error')
        raise TypeError('This is a sample TypeError error!')

    # Case 3
    with ok(KeyError, TypeError):
        print('KeyError error')
        raise KeyError('This is a sample KeyError error!')

    # Case 4
    with ok(IndexError):
        print('KeyError error')
        raise KeyError('This is a sample KeyError error!')



# Generated at 2022-06-14 05:56:16.532813
# Unit test for function ok
def test_ok():
    with ok(ValueError, TypeError):
        int('hello')
    with ok(ValueError, TypeError):
        int('hello')
    with ok(ValueError, TypeError):
        int('123.456')



# Generated at 2022-06-14 05:56:18.747316
# Unit test for function ok
def test_ok():
    """Test that ok() context manager works correctly.
    """
    with ok():
        pass
    assert True



# Generated at 2022-06-14 05:56:20.672389
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with ok(ValueError):
        raise TypeError



# Generated at 2022-06-14 05:56:28.862081
# Unit test for function ok
def test_ok():
    with ok():
        pass
    with ok(KeyError):
        raise KeyError()
    with ok(KeyError, ValueError):
        raise ValueError()
    with ok(KeyError, ValueError):
        raise TypeError()
    with pytest.raises(TypeError):
        with ok():
            raise TypeError()
    with pytest.raises(TypeError):
        with ok(KeyError, ValueError):
            raise TypeError()


if __name__ == "__main__":
    pytest.main()

# Generated at 2022-06-14 05:56:32.032277
# Unit test for function ok
def test_ok():
    with pytest.raises(IndexError):
        with ok():
            raise IndexError
    with ok(ZeroDivisionError):
        raise IndexError



# Generated at 2022-06-14 05:56:36.379820
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False

    with raises(ZeroDivisionError):
        with ok(AssertionError):
            1 / 0


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:56:45.258302
# Unit test for function ok
def test_ok():
    with ok(OSError):
        raise OSError
    with ok(ValueError, TypeError):
        raise TypeError
    with ok(ValueError, TypeError):
        raise ValueError

    try:
        with ok(OSError):
            raise ValueError
    except Exception as e:
        assert isinstance(e, ValueError)


# Generated at 2022-06-14 05:56:47.365152
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('N/A')


# so that it can be used in the below example

# Generated at 2022-06-14 05:57:55.982239
# Unit test for function ok
def test_ok():
    with ok():
        pass

    with ok(ValueError):
        raise ValueError()

    with pytest.raises(IndexError):
        with ok(ValueError):
            raise IndexError()

    with pytest.raises(Exception):
        with ok(ValueError):
            raise Exception()



# Generated at 2022-06-14 05:58:03.377416
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0

    # Should not raise IndexError
    with ok(IndexError):
        lst = []
        lst[0]

    # Should raise IndexError
    with raises(IndexError):
        lst = []
        with ok(ZeroDivisionError):
            lst[0]


# ----------------------------------------------
# • Implement function get_even_list(l) which gets a list of integers
# and returns a list of only the even numbers in it.



# Generated at 2022-06-14 05:58:05.604700
# Unit test for function ok
def test_ok():
    """Test function ok."""
    assert ok(ValueError).__class__ is GeneratorType


# Helper functions

# Generated at 2022-06-14 05:58:08.669967
# Unit test for function ok
def test_ok():
    with ok(FileNotFoundError):
        raise FileNotFoundError()
    with raises(OSError):
        with ok(FileNotFoundError):
            raise OSError()



# Generated at 2022-06-14 05:58:10.001779
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False



# Generated at 2022-06-14 05:58:13.443359
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('N/A')
    with ok(TypeError, ValueError):
        int('N/A')
    with ok(TypeError, AttributeError):
        [] + 1

# Generated at 2022-06-14 05:58:18.021872
# Unit test for function ok
def test_ok():
    """Test for function ok."""
    x = 1
    with ok(ValueError):
        x = 'a'

    with raises(TypeError):
        with ok(ValueError):
            x = int('a')

    print(x)


# hide function, for debugging
# test_ok()

# Generated at 2022-06-14 05:58:27.012759
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False
    with ok(TypeError):
        int('foo')
    with ok(AssertionError, TypeError) as e:
        int('foo')
    assert e is None
    with ok(TypeError, AssertionError) as e:
        int('foo')
    assert e is None
    with ok(TypeError, AssertionError) as e:
        assert False
    assert e is None


# Test for failed exceptions

# Generated at 2022-06-14 05:58:28.078771
# Unit test for function ok
def test_ok():
    with ok():
        raise ValueError



# Generated at 2022-06-14 05:58:33.876634
# Unit test for function ok
def test_ok():
    # Test passing exception
    with ok(ZeroDivisionError):
        1/0
    # Test passing non existing exception
    with raises(AssertionError):
        with ok(TypeError):
            1/0
    # Test passing multiple exceptions
    with ok(ZeroDivisionError, ValueError):
        1/0


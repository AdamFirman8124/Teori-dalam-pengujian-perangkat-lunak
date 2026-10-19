

# Generated at 2022-06-14 05:49:05.409129
# Unit test for function ok
def test_ok():

    with ok(AssertionError):
        assert False

    with ok(AssertionError):
        assert True

    with raises(ZeroDivisionError):
        1 / 0



# Generated at 2022-06-14 05:49:08.009630
# Unit test for function ok
def test_ok():
    with ok(OSError):
        os.remove('/path/to/non-existent/file')

    with ok(OSError):
        raise ValueError('error')



# Generated at 2022-06-14 05:49:12.532509
# Unit test for function ok
def test_ok():
    x = None
    with ok(AttributeError, TypeError):
        x = [1, 2, 3]
        x.pop()
        x.do_stuf()

    assert isinstance(x, list)
    assert x == [1, 2]



# Generated at 2022-06-14 05:49:16.646233
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise ValueError('pass')
    try:
        with ok(ValueError):
            raise Exception('raise')
    except Exception as exc:
        assert str(exc) == 'raise'


# Decorator

# Generated at 2022-06-14 05:49:20.453754
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise Exception
    with ok(Exception):
        raise ValueError
    with ok(Exception):
        raise AssertionError
    with ok(AssertionError):
        raise AssertionError



# Generated at 2022-06-14 05:49:24.074135
# Unit test for function ok
def test_ok():
    """Unit test for function ok."""
    import random

    with pytest.raises(ZeroDivisionError):
        with ok(ValueError):
            random.choice([0, 1]) / 0



# Generated at 2022-06-14 05:49:27.156170
# Unit test for function ok
def test_ok():
    try:
        with ok(TypeError):
            print('TypeError test')
    except:
        print('Exceptions other than TypeError')

# Generated at 2022-06-14 05:49:30.183984
# Unit test for function ok
def test_ok():
    """ Unit test for function ok """
    with ok(ZeroDivisionError):
        10 / 0


if __name__ == '__main__':
    # test_ok()
    pass

# Generated at 2022-06-14 05:49:31.680926
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False



# Generated at 2022-06-14 05:49:38.883620
# Unit test for function ok
def test_ok():
    with ok(IndexError) as cm:
        [1, 2, 3][4]
    assert not cm.exception
    with ok(IndexError, ValueError) as cm:
        [1, 2, 3][1]
    assert not cm.exception
    with ok(IndexError, ValueError) as cm:
        int('hello')
    assert cm.exception
    with ok(IndexError, ValueError) as cm:
        [1, 2, 3]['foo']
    assert cm.exception


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:49:45.506378
# Unit test for function ok
def test_ok():
    # Testing contextmanager ok
    with ok(ValueError):
        x = 5 / 0  # noqa
    try:
        with ok(ValueError):
            x = 5 / 1  # noqa
    except ZeroDivisionError:
        pass



# Generated at 2022-06-14 05:49:49.737379
# Unit test for function ok
def test_ok():
    @ok(ValueError, AssertionError)
    def test():
        if random.random() < 0.5:
            raise ValueError
        else:
            raise AssertionError

    # test()


# Memoization decorator

# Generated at 2022-06-14 05:49:51.721302
# Unit test for function ok
def test_ok():
    @ok(ZeroDivisionError)
    def _test_ok():
        raise ZeroDivisionError
        print("test")

    _test_ok()



# Generated at 2022-06-14 05:49:56.998088
# Unit test for function ok
def test_ok():
    try:
        with ok():
            print('Hello world!')
    except:
        # It should not raise any exception
        assert 0

    try:
        with ok(ZeroDivisionError):
            1 / 0
    except:
        # It should not raise any exception
        assert 0

    try:
        with ok():
            1 / 0
    except Exception as e:
        # It should raise an exception
        assert isinstance(e, ZeroDivisionError)


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:50:00.201136
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('N/A')

    with ok():
        int('N/A')



# Generated at 2022-06-14 05:50:05.640109
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise Exception
    try:
        with ok(ValueError):
            raise Exception
    except Exception as e:
        assert isinstance(e, ValueError) is False
    try:
        with ok(ValueError):
            raise ValueError
    except Exception as e:
        assert isinstance(e, ValueError)



# Generated at 2022-06-14 05:50:11.238000
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        # This block will raise a TypeError and be silently
        # ignored
        {}['a'] = 'b'

    with ok(IndexError, TypeError):
        # This block will raise a KeyError and will not be
        # ignored
        [][1] = 'd'



# Generated at 2022-06-14 05:50:16.451477
# Unit test for function ok
def test_ok():
    """Test ok function."""
    with ok(ValueError):
        pass
    with ok(ValueError, RuntimeError):
        1 / 0
    with ok(ValueError, RuntimeError):
        raise TypeError
    with ok(ValueError, RuntimeError):
        raise TypeError()


if __name__ == "__main__":
    test_ok()

# Generated at 2022-06-14 05:50:17.531918
# Unit test for function ok
def test_ok():
    ok()



# Generated at 2022-06-14 05:50:19.186389
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        raise TypeError


# Practice again:

# Generated at 2022-06-14 05:50:25.825248
# Unit test for function ok
def test_ok():
    with ok(IOError):
        with open("file", "r") as fp:
            print(fp.read())
    print("ok")


if __name__ == "__main__":
    test_ok()

# Generated at 2022-06-14 05:50:34.010368
# Unit test for function ok
def test_ok():
    try:
        with ok(ZeroDivisionError):
            1 / 0
    except Exception:
        pass
    else:
        raise AssertionError("Test failed")

    try:
        with ok(ZeroDivisionError):
            raise AssertionError("Test failed")
    except AssertionError:
        pass
    else:
        raise AssertionError("Test failed")


if __name__ == "__main__":
    # Run unit tests
    test_ok()

# Generated at 2022-06-14 05:50:38.314926
# Unit test for function ok
def test_ok():
    with ok(Exception):
        pass

    with raises(AttributeError):
        with ok(Exception):
            raise AttributeError()

    with raises(Exception):
        with ok(AttributeError):
            raise Exception()



# Generated at 2022-06-14 05:50:43.255123
# Unit test for function ok
def test_ok():
    with raises(TypeError):
        with ok():
            raise TypeError

    with ok(TypeError):
        raise TypeError

    with raises(RuntimeError):
        with ok(TypeError):
            raise RuntimeError


# Generated at 2022-06-14 05:50:49.386627
# Unit test for function ok
def test_ok():
    """Test the ok() function."""
    with ok(TypeError):
        {'a': 1}['b']
    with ok(TypeError):
        raise FileNotFoundError("test")
    with pytest.raises(FileNotFoundError):
        with ok(TypeError):
            raise FileNotFoundError("test")
    with ok(TypeError, FileNotFoundError):
        raise FileNotFoundError("test")



# Generated at 2022-06-14 05:51:00.068112
# Unit test for function ok
def test_ok():
    """Test function ok."""
    with ok(FileNotFoundError):
        raise FileNotFoundError
    with ok(FileNotFoundError):
        raise Exception
    with ok():
        raise Exception
    with ok(FileNotFoundError):
        pass
    with ok(FileNotFoundError):
        raise FileNotFoundError('test')
    with ok(FileNotFoundError):
        raise FileNotFoundError('test') from None

    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        try:
            with ok(FileNotFoundError):
                raise FileNotFoundError
        except Exception:
            pass

    assert captured_output.getvalue() == ''


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:51:03.507287
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('N/A')
    with ok(IndexError, ValueError):
        int('N/A')



# Generated at 2022-06-14 05:51:06.823875
# Unit test for function ok
def test_ok():
    with pytest.raises(Exception):
        with ok():
            raise Exception('Cannot do')
    with ok(AssertionError):
        raise AssertionError('Cannot do')

# Generated at 2022-06-14 05:51:11.059121
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        pass
    with ok(ZeroDivisionError):
        raise ZeroDivisionError('error')
    with ok(ZeroDivisionError):
        raise KeyError('error')



# Generated at 2022-06-14 05:51:15.650684
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        raise AssertionError()

    with ok(ZeroDivisionError):
        raise AssertionError()

    with ok():
        raise AssertionError()

    import pytest
    with pytest.raises(Exception):
        with ok(AssertionError):
            raise Exception()



# Generated at 2022-06-14 05:51:27.578888
# Unit test for function ok
def test_ok():
    with ok():
        print("ok")
    with ok(AttributeError):
        raise AttributeError
    with ok(IOError, AttributeError):
        raise IOError
    with ok(AttributeError, IOError):
        raise ValueError
    with pytest.raises(TypeError):
        with ok():
            raise ValueError
    with pytest.raises(ValueError):
        with ok(AttributeError, IOError):
            raise ValueError

# Generated at 2022-06-14 05:51:30.369360
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0
    with raises(TypeError), ok():
        1 + None



# Generated at 2022-06-14 05:51:36.148438
# Unit test for function ok
def test_ok():
    with pytest.raises(ValueError):
        with ok(AttributeError, TypeError):
            {'a': 1}['b']

    with ok(AttributeError, TypeError):
        with ok(KeyError):
            {'a': 1}['b']

    with pytest.raises(ZeroDivisionError):
        with ok(AttributeError, TypeError):
            1 / 0

# Generated at 2022-06-14 05:51:39.247689
# Unit test for function ok
def test_ok():
    x = 1
    with ok():
        print(x / 1)

    with ok(ZeroDivisionError):
        print(x / 0)
    assert isinstance(ZeroDivisionError(), Exception)



# Generated at 2022-06-14 05:51:41.644690
# Unit test for function ok

# Generated at 2022-06-14 05:51:45.188851
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        1 + "2"

    with pytest.raises(ValueError):
        with ok(TypeError):
            raise ValueError("value error")



# Generated at 2022-06-14 05:51:47.288990
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False



# Generated at 2022-06-14 05:51:51.492689
# Unit test for function ok
def test_ok():
    """Test function ok."""
    try:
        with ok(TypeError):
            print('The function works well.')
    except Exception:
        print('The function does not work.')


# Part II. Canopy

# Generated at 2022-06-14 05:51:56.744334
# Unit test for function ok
def test_ok():
    a = 5
    b = 0
    with ok(ZeroDivisionError):
        a / b
    try:
        a / b
    except Exception as e:
        if isinstance(e, (ArithmeticError, ValueError, ZeroDivisionError)):
            pass
        else:
            raise e



# Generated at 2022-06-14 05:52:03.935566
# Unit test for function ok
def test_ok():
    with ok(Exception, ValueError):
        raise ValueError('Error')
    with ok(Exception, ValueError) as cm:
        raise Exception('Error')
    with pytest.raises(Exception) as cm:
        with ok(ValueError):
            raise Exception('Error')
    assert cm.type == Exception
    assert str(cm.value) == 'Error'



# Generated at 2022-06-14 05:52:23.525081
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    try:
        with ok(ValueError):
            raise NameError
    except NameError:
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Unit test

# Generated at 2022-06-14 05:52:35.570333
# Unit test for function ok
def test_ok():
    # Instantiate exceptions
    class Exception1(Exception):
        pass
    class Exception2(Exception):
        pass
    class Exception3(Exception):
        pass

    # Block exempt from launch of exception
    with ok(Exception2, Exception3):
        raise Exception1()

    # Verify that Exception1 is raised
    with raises(Exception1):
        raise Exception1()

    # Block exempt from launch of exception
    with ok(Exception2):
        raise Exception1()

    # Verify that Exception1 is raised
    with raises(Exception1):
        raise Exception1()

    # Block exempt from launch of exception
    with ok():
        raise Exception1()

    # Verify that Exception1 is raised
    with raises(Exception1):
        raise Exception1()

    # Block exempt from launch of exception
    with ok(Exception1):
        raise Exception1()

# Generated at 2022-06-14 05:52:39.497624
# Unit test for function ok
def test_ok():
    try:
        with ok():
            raise ValueError('We are inside a "ok" context manager')
    except ValueError as e:
        print(e)



# Generated at 2022-06-14 05:52:44.309453
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        int('a')
    with ok(TypeError, ValueError):
        int('a')
    try:
        with ok(ValueError):
            int('a')
    except TypeError:
        pass
    else:
        raise Exception('Exception not raised')



# Generated at 2022-06-14 05:52:47.858956
# Unit test for function ok
def test_ok():
    with ok():
        pass

    with ok(TypeError):
        raise TypeError()

    with ok(KeyError):
        raise ValueError()



# Generated at 2022-06-14 05:52:51.375630
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        print("Asdf")
    with ok(TypeError):
        10 + 'hello'
    with ok(ZeroDivisionError):
        rek = 0 / 1

# Generated at 2022-06-14 05:52:56.381616
# Unit test for function ok
def test_ok():
    with ok(AssertionError, IndexError):
        assert 1 == 1
    # with ok(TypeError) as ctx:
    #     x = 1 + "hi"
    # assert isinstance(ctx.exception, TypeError)



# Generated at 2022-06-14 05:53:07.189070
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        print('ok!')
    with ok(ValueError, TypeError):
        print('ok!')
    with ok(TypeError, ValueError):
        print('ok!')

    with ok(TypeError):
        print('ok!')
        raise ValueError
    with ok(TypeError, ValueError):
        print('ok!')
        raise ValueError

    with raises(ValueError):
        with ok(TypeError):
            print('ok!')
            raise ValueError
    with raises(ValueError):
        with ok(TypeError):
            print('ok!')
            raise KeyError('A')



# Generated at 2022-06-14 05:53:09.995488
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        assert True
    with ok(TypeError):
        int("test")
    with ok(TypeError):
        assert False



# Generated at 2022-06-14 05:53:14.627063
# Unit test for function ok
def test_ok():
    """Test ok function in contextlib.py"""

    # Testing with try-except block
    try:
        raise TypeError("Example")
    except Exception:
        pass
    else:
        print("Success")

    # Testing with ok context-manager
    with ok(TypeError):
        raise TypeError("Example")


test_ok()

# Generated at 2022-06-14 05:53:46.137579
# Unit test for function ok
def test_ok():
    with ok():
        pass



# Generated at 2022-06-14 05:53:50.066746
# Unit test for function ok
def test_ok():
    """Unit test for ok()."""
    with ok(ZeroDivisionError, IndexError):
        1 / 0
    with ok(ZeroDivisionError, IndexError):
        [1][2]
    with ok(ZeroDivisionError, IndexError):
        raise TypeError



# Generated at 2022-06-14 05:53:56.034961
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise ValueError('oops')

    with ok(Exception):
        raise Exception('oops')

    with ok(ValueError):
        raise ValueError('oops')
        raise Exception('oops')

    with ok(ValueError, TypeError):
        raise TypeError('oops')

    with ok(AttributeError):
        raise TypeError('oops')


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:54:00.277349
# Unit test for function ok
def test_ok():
    """
    Test function ok using pytest
    """
    value = 1
    try:
        with ok(ValueError):
            value = int("1")
    except ValueError:
        pass
    assert value == 1



# Generated at 2022-06-14 05:54:05.204979
# Unit test for function ok
def test_ok():
    with ok(Exception):
        pass

    try:
        with ok(IndexError, ZeroDivisionError, SyntaxError):
            raise Exception('exception!')
    except Exception as e:
        assert str(e) == 'exception!'



# Generated at 2022-06-14 05:54:09.763439
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError, ValueError):
        1/0
    with ok(ZeroDivisionError, ValueError):
        raise ValueError
    with ok(ZeroDivisionError, ValueError):
        raise TypeError



# Generated at 2022-06-14 05:54:16.109915
# Unit test for function ok
def test_ok():
    with ok(NameError, ValueError):
        print("test_ok: 1")
        foo = 'bar'
        raise NameError("test_ok: 2")
    try:
        with ok(NameError, ValueError):
            raise ValueError("test_ok: 3")
    except NameError:
        print("test_ok: 4")
    except ValueError:
        print("test_ok: 5")

# Generated at 2022-06-14 05:54:18.313241
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise Exception('Test ok')


# Decorator to test a function

# Generated at 2022-06-14 05:54:22.502197
# Unit test for function ok
def test_ok():
    """Tests the ok context manager.
    """
    with ok(FileNotFoundError):
        raise FileNotFoundError

    with ok(ArithmeticError):
        raise TypeError

    with ok(Exception, ArithmeticError):
        raise TypeError

# Generated at 2022-06-14 05:54:26.928726
# Unit test for function ok
def test_ok():
    with ok(Exception, ZeroDivisionError):
        raise Exception
        print('Some error')
    with ok(Exception, ZeroDivisionError):
        1/0
    with ok(Exception, ZeroDivisionError):
        raise ZeroDivisionError


# 2. Rewrite the following program into a single list comprehension:
# S = [x**2 for x in range(10)]
# V = [2**i for i in range(13)]
# M = [x for x in S if x % 2 == 0]

# Solution
S = [x ** 2 for x in [x for x in range(10)]]
print(S)


# 3. Write a Python program that accepts a string and calculate the number of digits and letters.
string_to_test = "Hi! xxx I'm a programmer. 123"


# Solution

# Generated at 2022-06-14 05:55:30.275781
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        n = 3/0


# Exercise 8. Make a decorator that receives a filename and writes to a file
# the time execution of the function it decorates.

# Generated at 2022-06-14 05:55:34.596869
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        1 / 0
    with raises(TypeError):
        with ok(ValueError):
            1 / 0



# Generated at 2022-06-14 05:55:38.278648
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        print(1+'a')
    with ok(TypeError):
        print(1+1)
    with ok():
        print(1+'a')



# Generated at 2022-06-14 05:55:42.819902
# Unit test for function ok
def test_ok():
    with ok(TypeError, ValueError):
        raise TypeError('TypeError')
    try:
        with ok():
            raise KeyError('KeyError')
    except KeyError:
        pass



# Generated at 2022-06-14 05:55:48.153700
# Unit test for function ok
def test_ok():
    """Test for the ok context manager"""
    with ok(ValueError):
        x = int('a')

    with raises(TypeError):
        with ok(ValueError):
            x = int('a')

    with ok():
        assert 1 == 0
    return

# Generated at 2022-06-14 05:55:50.384543
# Unit test for function ok
def test_ok():
    with ok(Exception) as my_context:
        logger.info("Test OK")
    assert my_context is not None



# Generated at 2022-06-14 05:55:56.232146
# Unit test for function ok
def test_ok():
    """Unit test for function ok"""
    try:
        with ok(Exception):
            raise Exception
    except:
        assert False

    try:
        with ok(ValueError):
            raise TypeError
        assert False
    except:
        pass



# Generated at 2022-06-14 05:56:01.672473
# Unit test for function ok
def test_ok():
    exceptions = (OSError, TypeError)

    with ok(*exceptions):
        raise OSError('Error 1')

    with ok(*exceptions):
        raise TypeError('Error 2')

    with pytest.raises(ValueError, match='Error 3'):
        with ok(*exceptions):
            raise ValueError('Error 3')

# Generated at 2022-06-14 05:56:05.517506
# Unit test for function ok
def test_ok():
    """Test ok function."""
    with ok(ValueError):
        # Will not raise exception
        int('a')

    try:
        with ok(TypeError):
            int('a')
    except ValueError:
        pass
    else:
        raise Exception("Did not raise ValueError")

# Generated at 2022-06-14 05:56:12.945895
# Unit test for function ok
def test_ok():
    """Test function ok()."""
    with ok(ZeroDivisionError):
        1 / 0
    with ok(ZeroDivisionError, TypeError):
        print(1+'a')
    with ok(ZeroDivisionError, TypeError):
        1+2
    try:
        with ok(ZeroDivisionError, TypeError):
            raise Exception
    except Exception:
        pass
    with ok(ZeroDivisionError, TypeError):
        1 / 0



# Generated at 2022-06-14 05:58:26.695983
# Unit test for function ok
def test_ok():
    """Test the functionality of ok()"""
    with ok(ValueError, TypeError):
        print("I'm safe!")

    with ok(LookupError):
        print("I'm not safe!")


if __name__ == "__main__":
    # Test the functionality of ok()
    test_ok()

# Generated at 2022-06-14 05:58:28.609605
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        int('a')


# Context manager to handle IO exceptions

# Generated at 2022-06-14 05:58:31.522995
# Unit test for function ok
def test_ok():
    with ok(ValueError, TypeError):
        int('N/A')


test_ok()



# Generated at 2022-06-14 05:58:35.309324
# Unit test for function ok
def test_ok():
    """Test ok context manager."""
    with ok(AttributeError):
        []()
    with raises(TypeError):
        with ok(AttributeError):
            []()
    assert True



# Generated at 2022-06-14 05:58:44.422173
# Unit test for function ok
def test_ok():
    class ProductNotFoundError(Exception):
        pass

    class ProductNotFoundError2(Exception):
        pass

    with ok(ProductNotFoundError):
        try:
            raise ProductNotFoundError()
        except ProductNotFoundError as e:
            assert True, 'ProductNotFoundError passed'

    with ok(ProductNotFoundError):
        try:
            raise ProductNotFoundError2()
        except ProductNotFoundError as e:
            assert False, 'ProductNotFoundError2 raised'



# Generated at 2022-06-14 05:58:46.219739
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        i = 'str'
        int(i)
    with ok(ValueError, TypeError):
        i = 'str'
        int(i)
        int(i, base=10)

# Generated at 2022-06-14 05:58:51.072423
# Unit test for function ok
def test_ok():

    with ok(TypeError):
        1()

    try:
        with ok():
            1()
    except TypeError:
        pass
    else:
        assert False, "An exception should have been raised."

# Generated at 2022-06-14 05:58:53.652886
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:58:58.893460
# Unit test for function ok
def test_ok():
    """Testing function ok.
    :return: None
    """

    @ok(ValueError)
    def my_function():
        raise ValueError

    my_function()
    with pytest.raises(TypeError):
        my_function()


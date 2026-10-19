

# Generated at 2022-06-14 05:49:06.066536
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('a')



# Generated at 2022-06-14 05:49:11.133962
# Unit test for function ok
def test_ok():
    with ok():
        pass

    with ok(ZeroDivisionError):
        1 / 0

    with pytest.raises(AssertionError):
        with ok(BaseException):
            pass

    with pytest.raises(ValueError):
        with ok(ZeroDivisionError, AssertionError):
            raise ValueError



# Generated at 2022-06-14 05:49:14.299181
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        print(1 / 0)
    print('cool')


# ---------------------------

# Solution 2 - Using assert

# Generated at 2022-06-14 05:49:16.947588
# Unit test for function ok
def test_ok():
    try:
        with ok(Exception):
            raise Exception('test')
    except:
        raise AssertionError



# Generated at 2022-06-14 05:49:20.502706
# Unit test for function ok
def test_ok():
    with ok(Exception):
        pass
    with ok(Exception):
        raise Exception()
    with ok(ValueError, TypeError):
        raise TypeError()
    with ok(Exception):
        raise TypeError()



# Generated at 2022-06-14 05:49:24.077764
# Unit test for function ok
def test_ok():
    try:
        with ok(ZeroDivisionError):
            1 / 0
    except IndexError:
        pass
    except ZeroDivisionError:
        pass
    except Exception as e:
        assert False



# Generated at 2022-06-14 05:49:28.105067
# Unit test for function ok
def test_ok():
    # test success
    with ok():
        pass

    # test failure
    with pytest.raises(AssertionError):
        with ok(AssertionError):
            raise AssertionError

# Generated at 2022-06-14 05:49:31.468090
# Unit test for function ok
def test_ok():
    with ok(ValueError) as cm2:
        raise ValueError
    try:
        with ok(ValueError) as cm2:
            raise KeyError
    except KeyError:
        pass



# Generated at 2022-06-14 05:49:36.257244
# Unit test for function ok
def test_ok():
    """Tests the ok function.
    """
    with ok(TypeError):
        # TypeError is not raised
        int('42')  # $ nosec
    with ok(TypeError, ValueError):
        # ValueError is raised
        int('foo')  # $ nosec


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:49:44.708612
# Unit test for function ok
def test_ok():
    """Unit test for function ok"""
    with ok(Exception):
        print(1 / 0)

    with ok(ZeroDivisionError):
        print(1 / 0)

    with ok(IndexError):
        with ok(ZeroDivisionError):
            print(1 / 0)

    with ok(AssertionError):
        assert 1 == 0

    with ok(AssertionError):
        with ok(ZeroDivisionError):
            assert 1 == 0

    with ok(ZeroDivisionError, IndexError):
        try:
            print(l)
        except NameError:
            pass

        try:
            print(1 / 0)
        except ZeroDivisionError:
            pass

    with ok(Exception):
        try:
            print(1 / 0)
        except Exception as e:
            print(e)


#

# Generated at 2022-06-14 05:49:56.032746
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        "string" + 5
    try:
        with ok(TypeError):
            4 + 5
    except Exception as e:
        assert e.args[0] == "unsupported operand type(s) for +: 'int' and 'int'"

    with ok(KeyError):
        dictionary = {}
        dictionary['key']

    try:
        with ok(KeyError):
            dictionary = {'key': 5}
            dictionary['key']
    except Exception as e:
        assert e.args[0] == "Ruh roh! A Key Error!"

# Generated at 2022-06-14 05:50:00.634954
# Unit test for function ok
def test_ok():
    """Unit test for ok() context manager."""
    try:
        with ok(ZeroDivisionError):
            v = 5 / 0
    except ZeroDivisionError:
        raise AssertionError('Unit test for ok() failed')

# Generated at 2022-06-14 05:50:06.970900
# Unit test for function ok
def test_ok():
    """Unit test for function ok"""
    with ok(Exception):
        raise Exception('ok')

    with raises(Exception):
        with ok(ValueError):
            raise Exception('not ok')


dict_lower = lambda d: {k.lower(): v for k, v in d.iteritems()}



# Generated at 2022-06-14 05:50:11.649228
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False

    with ok(ZeroDivisionError, AssertionError):
        1 / 0

    with ok(AssertionError):
        assert True

    with ok(ZeroDivisionError, AssertionError):
        1 / 2

# Generated at 2022-06-14 05:50:21.087767
# Unit test for function ok
def test_ok():
    try:
        with ok(TypeError, ValueError):
            print("Running ok()")
            raise ValueError("test ok()")
    except ValueError:
        print("Caught ValueError")
    try:
        with ok(TypeError, ValueError):
            print("Running ok()")
            raise TypeError("test ok()")
    except TypeError:
        print("Caught TypeError")
    try:
        with ok(TypeError, ValueError):
            print("Running ok()")
            raise NameError("test ok()")
    except NameError:
        print("Caught NameError")



# Generated at 2022-06-14 05:50:26.596352
# Unit test for function ok
def test_ok():
    # Test that exception is passed when ok is passed with that exception
    with ok(ZeroDivisionError):
        1 / 0

    # Test that exception is not passed when ok is passed without the exception
    with pytest.raises(ZeroDivisionError) as e:
        with ok(AssertionError):
            1 / 0
    assert e.type == ZeroDivisionError



# Generated at 2022-06-14 05:50:39.859325
# Unit test for function ok
def test_ok():
    with ok(Exception):
        raise Exception
    with ok(Exception):
        raise ValueError
    try:
        with ok(Exception):
            raise ValueError('not this')
    except ValueError:
        pass


# Global variables
version = '0.1.2'
verbose = False
force = False


# Generated at 2022-06-14 05:50:46.845536
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        int('a')

    with ok(TypeError):
        int(2)

    with ok(ZeroDivisionError):
        4 / 0

    with ok(TypeError):
        4 / '0'

    def p():
        2 + '3'

    with ok(TypeError):
        p()



# Generated at 2022-06-14 05:50:48.303890
# Unit test for function ok
def test_ok():
    with ok(AttributeError):
        {}.bla



# Generated at 2022-06-14 05:50:52.102067
# Unit test for function ok
def test_ok():
    with ok(ValueError, TypeError):
        int('N/A')
    with ok(ValueError):
        int('N/A')
    with ok(TypeError):
        int('N/A')
    with ok():
        int('N/A')

# Generated at 2022-06-14 05:50:59.687466
# Unit test for function ok
def test_ok():
    """Unit test function for function ok.
    """

    exception_list = [IndexError, ValueError]
    exception = IndexError

    try:
        with ok(*exception_list):
            pass
    except Exception as e:
        assert isinstance(e, exception)



# Generated at 2022-06-14 05:51:07.709853
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0
    with ok():
        1 / 1
    with pytest.raises(ZeroDivisionError) as e:
        with ok(ZeroDivisionError):
            1 / 0
    assert isinstance(e.value, ZeroDivisionError)
    with pytest.raises(ZeroDivisionError) as e:
        with ok(ValueError):
            1 / 0
    assert isinstance(e.value, ZeroDivisionError)

# Generated at 2022-06-14 05:51:12.400750
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        print("Do a thing that may raise type error")
        print(3 + 's')
    with ok(ValueError):
        print("Do a thing that may raise value error")
        print("This is fine")

    print("One more thing")

# Generated at 2022-06-14 05:51:14.179227
# Unit test for function ok
def test_ok():
    with raises(ValueError):
        with ok(ValueError):
            raise KeyError



# Generated at 2022-06-14 05:51:22.762420
# Unit test for function ok
def test_ok():
    with ok(ValueError, TypeError) as cm:
        raise ValueError
    assert cm.exception.__class__ is ValueError
    try:
        with ok(ValueError, TypeError):
            raise TypeError
    except TypeError:
        pass
    else:
        assert False, 'TypeError was not passed'
    try:
        with ok(ValueError, TypeError):
            raise KeyError
    except KeyError:
        assert True
    else:
        assert False, 'KeyError was passed'



# Generated at 2022-06-14 05:51:34.765670
# Unit test for function ok
def test_ok():
    """Test ok context manager."""
    with ok(AssertionError):
        assert False
    with ok(AssertionError, TypeError):
        assert False
    with ok(TypeError):
        assert False
    with ok():
        assert False

    with ok(AssertionError):
        raise TypeError()
    with ok(AssertionError, TypeError):
        raise TypeError()
    with ok(TypeError):
        raise TypeError()
    with ok():
        raise TypeError()

    try:
        with ok(AssertionError):
            assert False
        raise AssertionError
    except AssertionError:
        pass
    try:
        with ok(AssertionError, TypeError):
            assert False
        raise AssertionError
    except AssertionError:
        pass

# Generated at 2022-06-14 05:51:36.948215
# Unit test for function ok
def test_ok():
    with ok(TypeError) as result:
        a = 1 + "error"
    assert result is None



# Generated at 2022-06-14 05:51:42.053231
# Unit test for function ok
def test_ok():
    """Test for function ok."""

    def fn(n):
        with ok(ZeroDivisionError):
            1/n

    try:
        fn(1)
    except ZeroDivisionError:
        pass

    try:
        fn(0)
        assert False
    except ZeroDivisionError:
        assert True

# Generated at 2022-06-14 05:51:45.643287
# Unit test for function ok
def test_ok():
    """Test function ok."""
    with ok(IndexError) as context_manager:
        l = []
        l[2]
    assert not context_manager.exception

    with ok(TypeError) as context_manager:
        a = 'a'
        a + 2
    assert context_manager.exception is not None

# Generated at 2022-06-14 05:51:49.223492
# Unit test for function ok
def test_ok():
    """Test function ok to pass exceptions.
    :return: None
    """
    with ok(ZeroDivisionError):
        print(5 / 0)


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:52:03.539138
# Unit test for function ok
def test_ok():
    # Test that ok() context manager works.
    try:
        with ok(ValueError):
            raise ValueError("All is ok")
    except:
        assert False

    try:
        with ok(ValueError):
            raise TypeError("All is NOT ok")
    except TypeError:
        pass
    else:
        assert False



# Generated at 2022-06-14 05:52:05.901484
# Unit test for function ok
def test_ok():
    """Function to test function ok"""
    assert ok(ValueError)



# Generated at 2022-06-14 05:52:10.355854
# Unit test for function ok
def test_ok():
    """Test function ok."""
    with ok(AssertionError):
        assert False

    with ok(ValueError, AssertionError):
        assert False

    with ok(ZeroDivisionError, AssertionError):
        assert False



# Generated at 2022-06-14 05:52:11.610065
# Unit test for function ok
def test_ok():
    with ok():
        raise Exception()



# Generated at 2022-06-14 05:52:16.040516
# Unit test for function ok
def test_ok():
    with ok(TypeError, KeyError):
        print("ok")
        # raise KeyError("key")
        # raise TypeError("type")
        # raise IndexError("index")


# -- Customize and backup Exceptions

# Generated at 2022-06-14 05:52:22.191189
# Unit test for function ok
def test_ok():
    """Unit test for function ok"""
    with raises(Exception):
        with ok(ZeroDivisionError, TypeError):
            print(5 / 0)
    with ok(ZeroDivisionError, TypeError):
        print(5 / 2)
    with raises(Exception):
        with ok(ZeroDivisionError, TypeError):
            print(None + 2)


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:52:26.081558
# Unit test for function ok
def test_ok():
    try:
        with ok(TypeError):
            wrong_type = int('Hello World!')
    except ValueError:
        print('ValueError!')
    except TypeError:
        print('TypeError!')

# Generated at 2022-06-14 05:52:28.690533
# Unit test for function ok
def test_ok():
    @ok(ValueError, TypeError)
    def test_func():
        raise ValueError

    test_func()



# Generated at 2022-06-14 05:52:31.505329
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0
    with ok(TypeError):
        '1' + 1



# Generated at 2022-06-14 05:52:36.003791
# Unit test for function ok
def test_ok():
    with ok(ValueError, IndexError):
        print('hi')
        x = 10
        x.append(5)
        raise ValueError
    try:
        with ok(ValueError):
            print('show this to user')
            print(int('N/A'))
            print('never reached')
    except TypeError as e:
        print('TypeError!')

# Generated at 2022-06-14 05:53:02.033940
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False

    with ok(AssertionError):
        assert True

    with ok(ZeroDivisionError):
        1 / 0

    with ok(AssertionError, ZeroDivisionError):
        assert False

    with ok(AssertionError, ZeroDivisionError):
        assert True

    with ok(AssertionError, ZeroDivisionError):
        1 / 0

    with ok(ZeroDivisionError):
        assert False

    with ok(IndexError):
        a = [1, 2, 3]
        a[4]

    with ok(AssertionError, ZeroDivisionError, IndexError):
        assert False

    with ok(AssertionError, ZeroDivisionError, IndexError):
        assert True


# Generated at 2022-06-14 05:53:06.904685
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('test')
    with ok(Exception):
        raise Exception()
    with ok(ValueError, Exception):
        raise ValueError()
    with ok(ValueError):
        raise TypeError()



# Generated at 2022-06-14 05:53:12.196921
# Unit test for function ok
def test_ok():
    with ok(TypeError, AttributeError):
        pass

    with ok(TypeError):
        raise AttributeError

    with ok():
        raise TypeError

    with ok():
        # Just a simple example
        pass

    try:
        with ok(AttributeError):
            raise TypeError
    except TypeError:
        pass



# Generated at 2022-06-14 05:53:16.104722
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('N/A')
    with pytest.raises(TypeError):
        with ok(ValueError):
            int(None)


# Tests for ContextDecorator

# Generated at 2022-06-14 05:53:20.262551
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0
    with ok(ValueError):
        raise ValueError("error")
    with pytest.raises(IndexError):
        with ok(ValueError):
            raise IndexError("error")



# Generated at 2022-06-14 05:53:26.353565
# Unit test for function ok
def test_ok():
    """Test the context manager ok."""
    with ok(ValueError, TypeError):
        int('hello')
    with ok(ValueError, TypeError):
        int(None)
    with ok(ValueError, TypeError):
        print(1/0)


if __name__ == "__main__":
    test_ok()

# Generated at 2022-06-14 05:53:28.047701
# Unit test for function ok
def test_ok():
    with ok(TypeError, ValueError):
        bad_name = 'Bad Name'



# Generated at 2022-06-14 05:53:31.144926
# Unit test for function ok
def test_ok():
    """Unit test for function ok."""
    with ok(ValueError):
        int('N/A')
    with ok(ValueError):
        int('123')
    with ok(TypeError):
        {}[0]
    with pytest.raises(KeyError):
        {}[1]


# Example for using ok with a custom exception

# Generated at 2022-06-14 05:53:33.529500
# Unit test for function ok
def test_ok():
    with ok():
        raise TypeError()
    try:
        with ok(TypeError):
            raise ValueError()
    except ValueError:
        pass



# Generated at 2022-06-14 05:53:34.793413
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        pass
    with ok(ValueError):
        raise ValueError("Error")
    with ok(ValueError):
        raise TypeError("Error")

# Generated at 2022-06-14 05:54:07.204164
# Unit test for function ok
def test_ok():
    # You can pass exceptions in ok function
    with ok(TypeError, ValueError):
        int('N/A')
    # And it wil pass this
    # If you don't pass exception in ok function...
    with ok(TypeError):
        int('N/A')
    # It will raise TypeError exception, because
    # int('N/A') will raise ValueError exception.



# Generated at 2022-06-14 05:54:16.009009
# Unit test for function ok
def test_ok():
    """Tests for the ok() context manager."""
    # Test TypeError
    with ok(TypeError):
        int("Nope")
    # Test ValueError
    with ok(TypeError, ValueError):
        int("Nope")
    # Test IndexError
    with ok(TypeError, ValueError, IndexError):
        [][1]
    # Test generic Exception
    with ok(Exception):
        raise Exception("Catch me")
    # Test assertion
    with ok(AssertionError):
        assert False



# Generated at 2022-06-14 05:54:19.230034
# Unit test for function ok
def test_ok():
    with ok(TypeError):
    # Will raise a NameError
        len(3)
    # NameError will pass through, as it's not a TypeError



# Generated at 2022-06-14 05:54:21.490801
# Unit test for function ok
def test_ok():
    """
    Tests ok function
    """
    with ok(ValueError):
        raise ValueError

    assert True

# Generated at 2022-06-14 05:54:29.406999
# Unit test for function ok
def test_ok():
    import sys
    import pytest
    with ok(Exception):
        print('passing Exception')
    with ok(AttributeError):
        pass

    with pytest.raises(SyntaxError):
        with ok(AttributeError):
            raise SyntaxError('foo')
    with pytest.raises(SyntaxError):
        with ok(AttributeError):
            pass
        raise SyntaxError('foo')

# Generated at 2022-06-14 05:54:33.930449
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        a = {'a': 1}
        a['b']

    with assert_raises(KeyError):
        with ok(ValueError):
            a = {'a': 1}
            a['b']



# Generated at 2022-06-14 05:54:39.209215
# Unit test for function ok
def test_ok():
    class FooException(Exception):
        """Custom exception"""

    def test():
        raise FooException

    with ok(Exception):
        test()

    try:
        with ok(FooException):
            print('foo')
            raise Exception('test')
    except Exception as e:
        print(e)

# Generated at 2022-06-14 05:54:43.313667
# Unit test for function ok
def test_ok():
    """Test for function ok"""
    with ok(ValueError) as ok_:
        raise ValueError("Aaargh!")
    with ok(ValueError) as ok_:
        int("one")



# Generated at 2022-06-14 05:54:46.483821
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        print('123')
        raise ValueError


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:54:49.465136
# Unit test for function ok
def test_ok():
    with ok(OSError):
        with open('/no-such-file') as f:
            print(f.read())


# Key-value pair sort

# Generated at 2022-06-14 05:55:55.592020
# Unit test for function ok
def test_ok():
    with ok(AttributeError):
        my_bad_func(1, 2)
    with ok(ValueError, TypeError):
        int('N/A')
    with ok():
        int('N/A')



# Generated at 2022-06-14 05:55:58.429417
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('N/A')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 05:56:09.106415
# Unit test for function ok
def test_ok():
    try:
        with ok(ZeroDivisionError):
            2 / 0
    except Exception as e:
        assert type(e) == ZeroDivisionError
    else:
        assert False

    try:
        with ok(ZeroDivisionError):
            1 / 0
    except Exception as e:
        assert type(e) == ZeroDivisionError
    else:
        assert False

    try:
        with ok(ValueError, ZeroDivisionError):
            2 / 0
    except Exception as e:
        assert type(e) == ZeroDivisionError
    else:
        assert False

    try:
        with ok(ValueError, ZeroDivisionError):
            raise ValueError
    except Exception as e:
        assert type(e) == ValueError
    else:
        assert False


# Generated at 2022-06-14 05:56:12.015004
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError, unittest.TestCase):
        1 / 0

    with ok(unittest.TestCase):
        pass



# Generated at 2022-06-14 05:56:13.884702
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        print(1 / 0)



# Generated at 2022-06-14 05:56:16.638139
# Unit test for function ok
def test_ok():
    def a():
        raise ValueError
    try:
        with ok(ValueError):
            a()
    except ValueError:
        return False
    return True



# Generated at 2022-06-14 05:56:18.591694
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('a')
    assert_equal(int('a'), 'a')



# Generated at 2022-06-14 05:56:22.237430
# Unit test for function ok
def test_ok():
    """Function to test the context manager ok"""
    with ok(IndexError):
        raise IndexError
    with ok(IndexError):
        raise TypeError



# Generated at 2022-06-14 05:56:25.073795
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False
    with ok(ZeroDivisionError, OSError):
        1/0



# Generated at 2022-06-14 05:56:36.692248
# Unit test for function ok
def test_ok():
    """Test function body for ok"""

    try:
        with ok():
            pass

    except Exception:
        assert False

    try:
        with ok(ValueError):
            pass

    except Exception:
        assert False

    try:
        with ok(ValueError, AttributeError):
            pass

    except Exception:
        assert False

    try:
        with ok(ValueError, AttributeError):
            raise ValueError

    except Exception:
        assert False

    try:
        with ok(ValueError, AttributeError):
            raise AttributeError

    except Exception:
        assert False

    try:
        with ok(AttributeError):
            raise ValueError

    except ValueError:
        pass
    else:
        assert False



# Generated at 2022-06-14 05:58:45.730809
# Unit test for function ok
def test_ok():
    with ok():
        pass



# Generated at 2022-06-14 05:58:55.254736
# Unit test for function ok
def test_ok():
    # No exception raised
    with ok(FileNotFoundError, MemoryError):
        print("This is printed when there is no error")

    # FileNotFoundError doesn't pass
    with ok(MemoryError):
        raise FileNotFoundError("This error is not passed")

    # MemoryError passes
    with ok(FileNotFoundError, MemoryError):
        raise MemoryError("This error is passed")

    # AssertionError doesn't pass
    with ok(AssertionError):
        raise AssertionError("This error is not passed")


test_ok()

# Generated at 2022-06-14 05:59:00.361488
# Unit test for function ok
def test_ok():
    with ok():
        pass
    with ok(ValueError, TypeError):
        raise ValueError
    with ok(ValueError, TypeError):
        raise TypeError
    with raises(Exception):
        with ok(ValueError, TypeError):
            raise Exception



# Generated at 2022-06-14 05:59:06.080536
# Unit test for function ok
def test_ok():
    """Test function ok."""
    with ok(TypeError, ValueError):
        pass
    with ok(TypeError, ValueError):
        print('Error that should be passed')
        raise ValueError
    with ok(TypeError, ValueError):
        raise TypeError
    with pytest.raises(ZeroDivisionError):
        with ok(TypeError, ValueError):
            raise ZeroDivisionError


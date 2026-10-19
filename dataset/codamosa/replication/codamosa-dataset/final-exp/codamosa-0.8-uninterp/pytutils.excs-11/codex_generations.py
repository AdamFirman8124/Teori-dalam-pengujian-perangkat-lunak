

# Generated at 2022-06-14 05:49:12.649850
# Unit test for function ok
def test_ok():
    # Test for correct exception
    try:
        with ok(ValueError):
            raise ValueError
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not passed by context manager.")
    # Test for incorrect exception
    try:
        with ok(ValueError):
            raise TypeError
    except TypeError:
        raise AssertionError("TypeError was passed, "
                             "but was not handled by context manager.")


if __name__ == "__main__":
    test_ok()

# Generated at 2022-06-14 05:49:14.794250
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int("a")



# Generated at 2022-06-14 05:49:17.488568
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        x = 'foo'
        int(x)



# Generated at 2022-06-14 05:49:20.310770
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False

    with ok(ZeroDivisionError):
        x = 1 / 0


# Exercise 1

# Generated at 2022-06-14 05:49:27.446738
# Unit test for function ok
def test_ok():
    """Unit test for function ok."""
    @ok(TypeError, ValueError)
    def passes(x, y):
        return x + y
    assert passes(10, 5) == 15
    assert passes(10, '5') == 15
    assert passes(10, 'foo') is None
    assert passes(10, [5]) is None

    @ok(TypeError, ValueError)
    def raises_error(x, y):
        raise ValueError()
    assert raises_error(10, 5) is None



# Generated at 2022-06-14 05:49:32.943288
# Unit test for function ok
def test_ok():
    """Test that it pass exceptions in context manager."""
    with ok(ValueError):
        raise ValueError()

    with pytest.raises(TypeError):
        with ok(ValueError):
            raise TypeError()

    with ok(ValueError, TypeError):
        raise TypeError()



# Generated at 2022-06-14 05:49:36.862106
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        pass
    with ok(TypeError, IndexError):
        pass
    with ok():
        raise Exception
    with ok(ZeroDivisionError):
        raise Exception



# Generated at 2022-06-14 05:49:40.813631
# Unit test for function ok
def test_ok():
    with ok(ValueError, TypeError):
        raise ValueError
    try:
        with ok(ValueError, TypeError):
            raise ZeroDivisionError
    except Exception as e:
        assert isinstance(e, ZeroDivisionError)



# Generated at 2022-06-14 05:49:46.000756
# Unit test for function ok
def test_ok():
    try:
        with ok(ValueError):
            x = 1/0
            assert False, "Division by zero not detected"
        assert True
    except Exception as e:
        assert False, "Exception %s should not be raised" % e



# Generated at 2022-06-14 05:49:51.218935
# Unit test for function ok
def test_ok():
    """Unit test function for function ok
    """
    with ok(TypeError, ValueError, ZeroDivisionError):
        print(1 / 0)
    with ok(TypeError, ValueError, ZeroDivisionError):
        print(1 / "a")


if __name__ == "__main__":
    test_ok()

# Generated at 2022-06-14 05:49:56.602059
# Unit test for function ok
def test_ok():
    with ok(IOError, EOFError):
        raise EOFError()
    with ok(IOError, EOFError):
        raise KeyError()
    with ok(IOError, EOFError):
        raise ValueError()

# Generated at 2022-06-14 05:50:00.833185
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with ok(ValueError, TypeError):
        raise ValueError
    with ok(ValueError, TypeError):
        raise TypeError



# Generated at 2022-06-14 05:50:06.397571
# Unit test for function ok
def test_ok():
    """Test ok."""
    pi = 3.14159265
    with ok(ZeroDivisionError):
        1 / 0
    try:
        with ok(ZeroDivisionError):
            pi / 0
    except ValueError:
        pass



# Generated at 2022-06-14 05:50:11.650427
# Unit test for function ok
def test_ok():
    try:
        with ok(ValueError):
            int('a')
    except Exception as e:
        assert isinstance(e, TypeError)
    else:
        raise AssertionError('Passed the wrong exception')


# #3 @ok

# Generated at 2022-06-14 05:50:15.050771
# Unit test for function ok
def test_ok():
    """Function to test ok context manager"""
    with ok(TypeError):
        int('a')
    with ok(TypeError):
        bool('a')
    with ok(TypeError):
        int('a')

# Generated at 2022-06-14 05:50:19.519238
# Unit test for function ok
def test_ok():
    # Testing ok
    with ok(AssertionError):
        assert False

    # Testing exception raised
    with ok(AssertionError):
        assert True
        assert False

    # Testing exception not raised
    with ok(KeyError):
        assert True



# Generated at 2022-06-14 05:50:21.700056
# Unit test for function ok
def test_ok():
    with ok():
        raise NameError('No Bob')



# Generated at 2022-06-14 05:50:28.573205
# Unit test for function ok
def test_ok():
    """Unit test for function ok."""
    try:
        with ok(ZeroDivisionError):
            1 / 0
        assert False
    except Exception:
        assert True
    try:
        with ok(ZeroDivisionError):
            1 / 0
            assert False
    except Exception:
        assert True
    try:
        with ok(ZeroDivisionError):
            1 / 1
            assert True
    except Exception:
        assert False


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:50:30.267280
# Unit test for function ok
def test_ok():
    """Tests function ok"""
    with ok():
        pass



# Generated at 2022-06-14 05:50:36.847907
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with ok(ValueError, TypeError):
        raise TypeError
    with ok(ValueError, TypeError):
        raise ValueError
    with ok(ValueError, TypeError):
        raise KeyError
    with ok():
        raise ValueError
    with ok(TypeError):
        raise ValueError



# Generated at 2022-06-14 05:50:43.634028
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('N/A')

    with ok(TypeError, ValueError):
        int('N/A')

    with ok(TypeError):
        int('N/A')

# Generated at 2022-06-14 05:50:48.153269
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        raise TypeError
    with ok(TypeError, ValueError):
        raise TypeError
    with ok(TypeError, ValueError):
        raise ValueError
    with raises(AttributeError):
        with ok(TypeError, ValueError):
            raise AttributeError



# Generated at 2022-06-14 05:50:57.255501
# Unit test for function ok
def test_ok():
    with ok(AssertionError):
        assert False
    
    with ok(AssertionError):
        assert True
    
    with ok(ZeroDivisionError):
        x = 1 / 0
    
    with ok(AssertionError, ZeroDivisionError):
        x = 1 / 0
    
    with ok(AssertionError, ZeroDivisionError):
        assert True



# Generated at 2022-06-14 05:50:58.634554
# Unit test for function ok
def test_ok():
    assert ok()



# Generated at 2022-06-14 05:51:01.514496
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        print("Caught value error")
        raise ValueError
    print("Didn't catch")



# Generated at 2022-06-14 05:51:04.842992
# Unit test for function ok
def test_ok():
    with ok(AttributeError):
        raise AttributeError
    with ok(AttributeError):
        raise AttributeError


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:51:07.797801
# Unit test for function ok
def test_ok():
    assert ok
    with ok(Exception):
        raise Exception

# Generated at 2022-06-14 05:51:11.376436
# Unit test for function ok
def test_ok():
    a = 1
    b = 0

    with ok(ZeroDivisionError):
        a / b
    print(a)

# Generated at 2022-06-14 05:51:13.192817
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError, ValueError):
        1 / 0
        int('a')



# Generated at 2022-06-14 05:51:18.692250
# Unit test for function ok
def test_ok():
    with ok():
        print("Doing nothing")

    with ok(IndexError):
        "Not raising an IndexError"

    with assert_raises(TypeError):
        with ok(TypeError):
            raise IndexError



# Generated at 2022-06-14 05:51:34.526664
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        '''do sth'''
    with ok(ZeroDivisionError, TypeError):
        '''do sth'''
    try:
        with ok(ZeroDivisionError, TypeError):
            '''do sth'''
            raise IndexError()
    except IndexError:
        pass
    try:
        with ok(ZeroDivisionError, TypeError):
            '''do sth'''
            raise ZeroDivisionError()
    except ZeroDivisionError:
        pass


print(test_ok.__doc__)
test_ok()

# Generated at 2022-06-14 05:51:38.177940
# Unit test for function ok
def test_ok():
    """Test for function ok()."""
    with ok(ZeroDivisionError):
        1 / 0
    with raises(NameError):
        with ok(ZeroDivisionError):
            1 + undefined



# Generated at 2022-06-14 05:51:43.187480
# Unit test for function ok
def test_ok():
    with ok():
        print('ok')
    with ok(ValueError):
        x = int('asdf')


test_ok()


# Properties
# see: http://www.python-course.eu/python3_properties.php

# Generated at 2022-06-14 05:51:46.766230
# Unit test for function ok
def test_ok():
    """Test function ok"""
    with ok(TypeError):
        1 + "1"
    with ok():
        1 + 2


if __name__ == "__main__":
    test_ok()

# Generated at 2022-06-14 05:51:51.047942
# Unit test for function ok
def test_ok():
    with ok(Exception, ValueError):
        print('hello')
        raise ValueError
        print('world')
    with ok(Exception):
        print('hello')
        raise ValueError
        print('world')


test_ok()

# Generated at 2022-06-14 05:51:52.822826
# Unit test for function ok
def test_ok():
    """Test for function ok"""
    assert ok



# Generated at 2022-06-14 05:51:57.547668
# Unit test for function ok
def test_ok():
    # Pass an exception and expect no exception
    with ok(ValueError):
        raise ValueError

    # Pass a different exception and expect it to be raised
    with pytest.raises(TypeError):
        with ok(ValueError):
            raise TypeError



# Generated at 2022-06-14 05:52:06.672525
# Unit test for function ok
def test_ok():
    """Test ok function."""
    from contextlib import suppress

    with ok():
        pass

    with ok(ValueError):
        raise ValueError()

    with ok(ValueError, KeyError):
        raise KeyError()

    with raises(Exception):
        with ok():
            raise Exception()

    with raises(ValueError):
        with ok(KeyError):
            raise ValueError()

    with raises(KeyError):
        with ok(IndexError, KeyError):
            raise KeyError()

    assert True



# Generated at 2022-06-14 05:52:11.495073
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        int('n/a')
    with ok(ValueError, TypeError):
        x = int('n/a')
    # with ok(ValueError):
    #     x = int('n/a')
    with ok(KeyError):
        x = {}[0]
    with ok(TypeError, IndexError):
        1 + []



# Generated at 2022-06-14 05:52:17.184802
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with ok(ValueError, RuntimeError):
        raise ValueError
    with pytest.raises(ValueError):
        with ok(RuntimeError):
            raise ValueError
    with pytest.raises(ValueError):
        with ok(RuntimeError, ValueError):
            raise ValueError

# Generated at 2022-06-14 05:52:37.028560
# Unit test for function ok
def test_ok():
    """Test function ok"""
    tests = [
        [False, ValueError, TypeError],
        [ValueError],
        [ValueError, TypeError],
        []
    ]
    expected = [
        False,
        True,
        True,
        False,
    ]

    for i in range(len(tests)):
        try:
            with ok(*tests[i]):
                raise ValueError
            result = True
        except ValueError:
            result = False
        assert expected[i] == result

# Generated at 2022-06-14 05:52:38.492039
# Unit test for function ok
def test_ok():
    assert ok()



# Generated at 2022-06-14 05:52:39.311428
# Unit test for function ok
def test_ok():
    pass



# Generated at 2022-06-14 05:52:42.825516
# Unit test for function ok
def test_ok():
    with ok(Exception):
        pass


if __name__ == '__main__':
    import os
    import pytest
    pytest.main([os.path.abspath(__file__)])

# Generated at 2022-06-14 05:52:50.922796
# Unit test for function ok
def test_ok():
    with ok():
        pass
    with ok(TypeError):
        raise TypeError
    with ok(ValueError):
        raise TypeError
    with ok(TypeError, ValueError):
        raise TypeError
    with ok(TypeError, ValueError):
        raise ValueError
    with ok(TypeError, ValueError):
        raise KeyError
    with ok(TypeError, ValueError):
        raise KeyError


if __name__ == '__main__':
    test_ok()

# Generated at 2022-06-14 05:52:58.981049
# Unit test for function ok
def test_ok():
    """Test ok function."""
    try:
        with ok(KeyError):
            my_dict = {'a': 1, 'b': 2}
            my_dict['c']  # Raises KeyError
    except KeyError:
        raise AssertionError('ok failed')

    with pytest.raises(ValueError):
        with ok(KeyError):
            my_dict = {'a': 1, 'b': 2}
            my_dict['c']  # Raises KeyError

# Generated at 2022-06-14 05:53:01.969760
# Unit test for function ok
def test_ok():
    """Test for ok()."""
    with ok(TypeError):
        a = 1 + '1'
    assert a == '11'

# Generated at 2022-06-14 05:53:04.247496
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        val = int("not a number")
    assert val == 0



# Generated at 2022-06-14 05:53:06.630276
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        1 / 0


# Test ok without exceptions to pass

# Generated at 2022-06-14 05:53:15.399146
# Unit test for function ok
def test_ok():
    with ok():
        pass
    with ok(TypeError):
        raise TypeError('TypeError')
    with ok(TypeError):
        raise ValueError('ValueError')
    with ok(TypeError):
        raise AssertionError('AssertionError')
    with ok(TypeError, ValueError):
        raise AssertionError('AssertionError')
    with ok(TypeError, ValueError):
        raise TypeError('TypeError')
    with ok(TypeError, ValueError):
        raise ValueError('ValueError')
    with ok(TypeError, ValueError):
        raise Exception('Exception')



# Generated at 2022-06-14 05:53:56.971236
# Unit test for function ok
def test_ok():
    # Ensure no exception is raised if no exception occurs in the with-block.
    with ok():
        pass

    # Ensure that exceptions that are specific types are not
    # raised (i.e. the context manager is doing its job)
    with ok(IndexError):
        a = [1,2,3]

# Generated at 2022-06-14 05:53:59.827461
# Unit test for function ok
def test_ok():
    with ok(TypeError):
        int('hello')

    with raises(ValueError):
        with ok(TypeError):
            int('world')



# Generated at 2022-06-14 05:54:05.695432
# Unit test for function ok
def test_ok():
    with ok():
        raise StopIteration
    with ok(Exception):
        raise Exception
    with ok(ValueError, ArithmeticError):
        raise ArithmeticError

    with pytest.raises(StopIteration):
        with ok(ValueError, ArithmeticError):
            raise StopIteration



# Generated at 2022-06-14 05:54:12.453477
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        pass

    with ok(ZeroDivisionError):
        int(1) / 0

    with ok(ZeroDivisionError, ValueError):
        1 / 0


# Test for function ok
# use command line:
# pytest -sv --cov-report html --cov=. tutorial_coverage.py

# For more coverage or unittest tutorial
# follow this link
# https://docs.pytest.org/en/latest/contents.html

# Generated at 2022-06-14 05:54:18.438862
# Unit test for function ok
def test_ok():
    try:
        with ok():
            print("This should never get printed")
            1/0
    except Exception as e:
        print("Got exception: {0}".format(e))

    with ok(ValueError):
        raise ValueError("Value error passed")

# Generated at 2022-06-14 05:54:22.610581
# Unit test for function ok
def test_ok():
    """Unit test fot function ok."""
    with ok():
        pass
    with ok(TypeError):
        raise TypeError()
    with pytest.raises(ValueError):
        with ok(TypeError):
            raise ValueError()



# Generated at 2022-06-14 05:54:27.488752
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with ok(ValueError, TypeError):
        raise TypeError
    with raises(ZeroDivisionError):
        with ok(ValueError, TypeError):
            raise ZeroDivisionError

# Generated at 2022-06-14 05:54:30.699255
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with raises(ZeroDivisionError):
        with ok(ValueError):
            raise ZeroDivisionError



# Generated at 2022-06-14 05:54:36.735625
# Unit test for function ok
def test_ok():
    with ok(Exception):
        a = 3 + 2
    with ok(Exception):
        a = 3 + 'A'
    with ok(Exception):
        a = 3 + '2'
    with ok(Exception):
        raise ValueError("A")



# Generated at 2022-06-14 05:54:38.878786
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError("no error")
    with raises(TypeError):
        raise TypeError("error")



# Generated at 2022-06-14 05:55:51.946632
# Unit test for function ok
def test_ok():
    """Unit test for function ok.
    :return: Nothing
    """
    with ok(Exception):
        raise Exception('foobar')

    # with ok(ZeroDivisionError):
    #     raise ValueError('foobar')
    # with ok(ZeroDivisionError):
    #     raise TypeError('foobar')
    # with ok(ZeroDivisionError):
    #     raise ZeroDivisionError('foobar')
    # with ok(ZeroDivisionError):
    #     raise RuntimeError('foobar')
    # with ok(ZeroDivisionError):
    #     raise ArithmeticError('foobar')



# Generated at 2022-06-14 05:55:57.243191
# Unit test for function ok
def test_ok():
    with pytest.raises(IOError):
        with ok():
            raise IOError
    try:
        with ok(OSError):
            raise OSError
    except Exception as e:
        assert isinstance(e, OSError)



# Generated at 2022-06-14 05:55:58.835638
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError):
        x = 1 / 0



# Generated at 2022-06-14 05:56:00.483588
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        value = int('value')



# Generated at 2022-06-14 05:56:04.822419
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with ok():
        raise ValueError

    try:
        with ok(ValueError):
            raise TypeError
    except TypeError:
        pass

    try:
        with ok():
            raise TypeError
    except TypeError:
        pass



# Generated at 2022-06-14 05:56:09.746034
# Unit test for function ok
def test_ok():
    try:
        with ok(IOError):
            raise NoSuchFileException(None)
    except IOError:
        pass
    try:
        with ok(IOError):
            raise Exception()
    except NoSuchFileException:
        pass



# Generated at 2022-06-14 05:56:13.056823
# Unit test for function ok
def test_ok():
    with ok(KeyError):
        pass

    # context manager should not pass exceptions other than KeyError
    with pytest.raises(Exception):
        with ok(KeyError):
            raise Exception()



# Generated at 2022-06-14 05:56:14.593292
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError

    with ok(ValueError):
        raise FileNotFoundError()

    with raises(FileNotFoundError):
        with ok(ValueError):
            raise FileNotFoundError()



# Generated at 2022-06-14 05:56:25.187291
# Unit test for function ok
def test_ok():
    with ok() as e:
        raise RuntimeError('failed')
    assert e is None
    with ok(RuntimeError) as e:
        raise RuntimeError('failed')
    assert isinstance(e, RuntimeError)
    with ok(RuntimeError) as e:
        raise AssertionError('failed')
    assert e is None
    with ok(RuntimeError, AssertionError) as e:
        raise AssertionError('failed')
    assert isinstance(e, AssertionError)


if __name__ == '__main__':
    import sys
    import nose
    # This code will run the test in this file.'
    module_name = sys.modules[__name__].__file__


# Generated at 2022-06-14 05:56:30.031081
# Unit test for function ok
def test_ok():
    with ok(ValueError):
        raise ValueError
    with ok(ValueError, TypeError):
        raise TypeError
    with pytest.raises(IndexError):
        with ok(ValueError, TypeError):
            raise IndexError



# Generated at 2022-06-14 05:58:50.507152
# Unit test for function ok
def test_ok():
    try:
        with ok(ValueError):
            raise ValueError()
        with ok(ValueError):
            raise TypeError()
        assert False, 'Must pass 2 exceptions.'
    except TypeError:
        pass



# Generated at 2022-06-14 05:58:54.521445
# Unit test for function ok
def test_ok():
    with ok(IndexError):
        [][0]
    with ok(TypeError):
        int('s')
    with ok(TypeError, IndexError):
        [][0]


# Test the ok function with a non-raise exception

# Generated at 2022-06-14 05:58:58.761133
# Unit test for function ok
def test_ok():
    """Test function 'ok'."""
    # Check if ok is a context manager
    assert inspect.ismethod(ok) is contextmanager

    # Check if 'ok' passes exceptions
    assert ok()



# Generated at 2022-06-14 05:59:03.618302
# Unit test for function ok
def test_ok():
    with ok(ZeroDivisionError, ValueError):
        int("1")
    with ok(ZeroDivisionError, ValueError):
        a = 1 / 0
    with ok(ZeroDivisionError, ValueError):
        int("1a")


# Context manager to measure time.
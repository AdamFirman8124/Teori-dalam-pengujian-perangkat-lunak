

# Generated at 2022-06-14 06:35:42.903618
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert not (PyInfo.PY2 and PyInfo.PY3)

    if PyInfo.PY2:
        assert PyInfo.maxsize == int((1 << 63) - 1)
    else:
        assert PyInfo.maxsize == int((1 << 31) - 1)

# Generated at 2022-06-14 06:35:48.491118
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 ^ PyInfo.PY3
    assert callable(PyInfo.string_types)
    assert callable(PyInfo.integer_types)
    assert callable(PyInfo.class_types)


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-14 06:35:57.378948
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p = PyInfo()
    assert p.PY2 is True
    assert p.PY3 is False
    assert p.string_types is basestring
    assert p.text_type is unicode
    assert p.binary_type is str
    assert p.integer_types is (int, long)
    assert p.class_types is (type, types.ClassType)
    assert p.maxsize == (1 << 63) - 1


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:36:03.399674
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.PY3 == (PyInfo.PY2 is False)
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY2 == (PyInfo.PY3 is False)

    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.integer_types == (int, long)
    else:
        assert PyInfo.string_types == (str,)
        assert PyInfo.integer_types == (int,)



# Generated at 2022-06-14 06:36:09.629012
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo is not None
    assert pyinfo.PY2 is not None
    assert pyinfo.PY3 is not None
    assert pyinfo.string_types is not None
    assert pyinfo.text_type is not None
    assert pyinfo.binary_type is not None
    assert pyinfo.integer_types is not None
    assert pyinfo.class_types is not None
    assert pyinfo.maxsize is not None



# Generated at 2022-06-14 06:36:14.191732
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    assert isinstance(b'', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)

# Generated at 2022-06-14 06:36:21.217013
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (PyInfo.PY3 != True)
    assert PyInfo.PY3 != (PyInfo.PY2 != True)
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

# Generated at 2022-06-14 06:36:27.209313
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print("\n", "=" * 50, "Constructor of Class PyInfo ", "=" * 50)

    print("type(PyInfo.PY2) =", type(PyInfo.PY2))
    print("isinstance(PyInfo.PY2, bool) =", isinstance(PyInfo.PY2, bool))

    print("type(PyInfo.PY3) =", type(PyInfo.PY3))
    print("isinstance(PyInfo.PY3, bool) =", isinstance(PyInfo.PY3, bool))

    print("type(PyInfo.string_types) =", type(PyInfo.string_types))
    print("isinstance(PyInfo.string_types, tuple) =", isinstance(PyInfo.string_types, tuple))


# Generated at 2022-06-14 06:36:35.576781
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p = PyInfo

    assert p.PY2 is not p.PY3
    assert isinstance("", p.string_types)
    assert isinstance("", p.text_type)
    assert isinstance("".encode(), p.binary_type)
    assert isinstance(1, p.integer_types)
    assert isinstance(type, p.class_types)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_PyInfo()

# Generated at 2022-06-14 06:36:41.228874
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert issubclass(PyInfo.text_type, PyInfo.text_type)
    assert isinstance('abc', PyInfo.string_types)
    assert max(PyInfo.integer_types) == PyInfo.maxsize
    assert isinstance(int, PyInfo.class_types)

# Generated at 2022-06-14 06:36:55.612641
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def check_type(instance, type):
        assert isinstance(instance, type)

    check_type(PyInfo.PY2, bool)
    check_type(PyInfo.PY3, bool)
    check_type(PyInfo.string_types, tuple)
    check_type(PyInfo.text_type, type)
    check_type(PyInfo.binary_type, type)
    check_type(PyInfo.integer_types, tuple)
    check_type(PyInfo.class_types, tuple)
    check_type(PyInfo.maxsize, int)

    assert PyInfo.PY2 ^ PyInfo.PY3  # XOR, i.e. one+only one of PY2, PY3 is True



# Generated at 2022-06-14 06:37:01.030128
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert (PyInfo.PY2, PyInfo.PY3) == (2, 3)
    assert PyInfo.string_types == (str, )
    assert PyInfo.text_type == str
    assert PyInfo.maxsize == 2 ** 31 - 1



# Generated at 2022-06-14 06:37:09.694830
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert str is PyInfo.text_type
        assert str is not PyInfo.binary_type
        assert isinstance('string', PyInfo.string_types)
        assert isinstance('string', PyInfo.binary_type)
        assert not isinstance(u'string', PyInfo.string_types)
    else:
        assert str is PyInfo.string_types
        assert str is not PyInfo.text_type
        assert str is not PyInfo.binary_type
        assert not isinstance('string', PyInfo.string_types)
        assert isinstance('string', PyInfo.binary_type)
        assert isinstance(u'string', PyInfo.string_types)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:37:16.121879
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()
    assert(info.PY2 == (sys.version_info[0] == 2))
    assert(info.PY3 == (sys.version_info[0] == 3))

    if info.PY2:
        assert(isinstance('abc', PyInfo.string_types))
        assert(isinstance('abc', basestring))
        assert(not isinstance('abc', str))

        assert(isinstance(u'abc', PyInfo.string_types))
        assert(isinstance(u'abc', basestring))
        assert(not isinstance(u'abc', str))

        assert(isinstance('abc', PyInfo.text_type))
        assert(isinstance('abc', unicode))
        assert(not isinstance('abc', str))


# Generated at 2022-06-14 06:37:23.420241
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:37:29.978276
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    assert isinstance(b'', PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)
    assert isinstance(type, PyInfo.class_types)
    assert PyInfo.maxsize == sys.maxsize


test_PyInfo()
del test_PyInfo

# Generated at 2022-06-14 06:37:37.925332
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # pylint: disable=unused-variable
    assert PyInfo.PY2 or PyInfo.PY3
    assert type(PyInfo.string_types) == tuple
    assert type(PyInfo.text_type) == type
    assert type(PyInfo.binary_type) == type
    assert type(PyInfo.integer_types) == tuple
    assert type(PyInfo.class_types) == tuple
    assert type(PyInfo.maxsize) == int

# Generated at 2022-06-14 06:37:41.269338
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """ """
    assert PyInfo.PY2 == (2 == sys.version_info.major)
    assert PyInfo.PY3 == (3 == sys.version_info.major)



# Generated at 2022-06-14 06:37:48.526259
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)
    else:
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)

# Generated at 2022-06-14 06:38:01.210924
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3

    assert isinstance("", PyInfo.string_types)
    assert not isinstance('', PyInfo.string_types)

    assert str() == PyInfo.text_type()
    assert str.__name__ == PyInfo.text_type.__name__
    assert b"" == PyInfo.binary_type()
    assert bytes.__name__ == PyInfo.binary_type.__name__

    if PyInfo.PY2:
        assert isinstance(0, PyInfo.integer_types)
        assert not isinstance(0, (PyInfo.integer_types, PyInfo.float_types))
    else:
        assert isinstance(0, PyInfo.integer_types)
        assert isinstance(0, (PyInfo.integer_types, PyInfo.float_types))

# Generated at 2022-06-14 06:38:11.631371
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()

    # Test if the possibility of false positives is low
    assert not (pyinfo.PY2 and pyinfo.PY3)

    # Test if the possibility of false negatives is low
    assert pyinfo.PY2 or pyinfo.PY3


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:14.498965
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is (2 == sys.version_info.major)
    assert PyInfo.PY3 is (3 == sys.version_info.major)



# Generated at 2022-06-14 06:38:20.036721
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert getattr(PyInfo, '__name__') == 'PyInfo'
    return

# Ensure the module is callable
if __name__ == '__main__':
    if __doc__:
        print(__doc__)
    test_PyInfo()

# Generated at 2022-06-14 06:38:33.115326
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # class PyInfo(object):
    assert isinstance(PyInfo, type)
    # if PY3:
    if PyInfo.PY3:
        assert PyInfo.PY3
        assert not PyInfo.PY2
        # string_types = str,
        assert isinstance(PyInfo.string_types, tuple)
        assert str in PyInfo.string_types
        # text_type = str
        assert PyInfo.text_type == str
        # binary_type = bytes
        assert PyInfo.binary_type == bytes
        # integer_types = int,
        assert isinstance(PyInfo.integer_types, tuple)
        assert int in PyInfo.integer_types
        # class_types = type,
        assert isinstance(PyInfo.class_types, tuple)
        assert type in PyInfo.class_types

# Generated at 2022-06-14 06:38:40.518049
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()

    assert isinstance(info, PyInfo)

    assert info.PY2 == (sys.version_info[0] == 2)
    assert info.PY3 == (sys.version_info[0] == 3)

    if info.PY3:
        assert info.string_types == (str,)
        assert info.text_type == str
        assert info.binary_type == bytes
        assert info.integer_types == (int,)
        assert info.class_types == (type,)

        assert isinstance(info.maxsize, int)
    else:  # PY2
        assert info.string_types == (basestring,)
        assert info.text_type == unicode
        assert info.binary_type == str
        assert info.integer_types == (int, long)
        assert info

# Generated at 2022-06-14 06:38:53.712402
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2, "Sorry, this unit test only works with python 2."

    assert type(PyInfo.PY2) == bool, "PY2 is not a boolean object."
    assert type(PyInfo.PY3) == bool, "PY3 is not a boolean object."

    assert type(PyInfo.string_types) == tuple, "string_types is not a tuple."
    assert type(PyInfo.text_type) == type, "text_type is not a type."
    assert type(PyInfo.binary_type) == type, "binary_type is not a type."
    assert type(PyInfo.integer_types) == tuple, "integer_types is not a tuple."
    assert type(PyInfo.class_types) == tuple, "class_types is not a tuple."


# Generated at 2022-06-14 06:39:00.063433
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True
    assert PyInfo.PY3 is False
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == sys.maxsize
    assert unicode is type('')
    # assert PyInfo.string_types == (unicode, str)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:39:08.848290
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from itertools import permutations

    # Check that the following tests only work on certain version of Python
    assert not PyInfo.PY2 or sys.version_info[0] == 2
    assert not PyInfo.PY3 or sys.version_info[0] == 3

    # Check that Permutations can be invoked with PyInfo.PY3 and PyInfo.PY2
    [__ for __ in permutations(['PY3', 'PY2'], 2)]

    # Check that PyInfo.text_type is a string type
    assert isinstance("test", PyInfo.text_type)

    # Check that PyInfo.binary_type is a string type
    assert isinstance("test", PyInfo.binary_type)

    # Check that PyInfo.string_types can iterate over the string types

# Generated at 2022-06-14 06:39:12.345889
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert PyInfo.maxsize > (1 << 32) - 1
    else:
        assert PyInfo.maxsize == (1 << 63) - 1



# Generated at 2022-06-14 06:39:21.242127
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3
    assert not PyInfo.PY2

    assert PyInfo.string_types == (str,)
    assert PyInfo.text_type == str
    assert PyInfo.binary_type == bytes
    assert PyInfo.integer_types == (int,)
    assert PyInfo.class_types == (type,)

    if sys.platform == "win32":
        assert (2 ** 32) - 1 == PyInfo.maxsize
    else:
        assert (2 ** 64) - 1 == PyInfo.maxsize


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:39:32.992721
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is True


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:39:39.407156
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def subtest(expected, actual):
        if expected == actual:
            print("Pass")
        else:
            print("Fail")

    print("Test for %s" % (__file__))
    subtest(PyInfo.PY2, sys.version_info[0] == 2)
    subtest(PyInfo.PY3, sys.version_info[0] == 3)

    if PyInfo.PY2:
        subtest(PyInfo.string_types, (basestring,))
        subtest(PyInfo.text_type, unicode)
        subtest(PyInfo.binary_type, str)
        subtest(PyInfo.integer_types, (int, long))
        subtest(PyInfo.class_types, (type, types.ClassType))


# Generated at 2022-06-14 06:39:48.364070
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys
    assert sys.version_info[0] == 2 and not PyInfo.PY3
    assert sys.version_info[0] == 3 and not PyInfo.PY2
    assert isinstance("", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.class_types)
    assert isinstance(object, PyInfo.class_types)

# Generated at 2022-06-14 06:39:51.772540
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == True or PyInfo.PY2 == True
    assert PyInfo.PY3 == True and PyInfo.PY2 == False


# Generated at 2022-06-14 06:40:00.091293
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert not isinstance(1, PyInfo.string_types)
    assert not isinstance(1.1, PyInfo.string_types)
    assert not isinstance([], PyInfo.string_types)
    assert not isinstance({}, PyInfo.string_types)
    assert not isinstance(None, PyInfo.string_types)
    assert isinstance('abc', PyInfo.text_type)
    assert isinstance(u'abc', PyInfo.text_type)
    assert not isinstance(b'abc', PyInfo.text_type)
    assert isinstance('abc', PyInfo.binary_type)

# Generated at 2022-06-14 06:40:06.390593
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('a', PyInfo.string_types)
        assert isinstance(u'a', PyInfo.string_types)
    else:
        assert isinstance('a', PyInfo.string_types)
        assert isinstance('a', PyInfo.string_types)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:40:13.894645
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert not isinstance(b"", PyInfo.text_type)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:40:25.631268
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance('a', PyInfo.string_types)
    assert not isinstance(b'a', PyInfo.string_types)

    assert isinstance(u'a', PyInfo.text_type)
    assert not isinstance('a', PyInfo.text_type)

    assert isinstance(b'a', PyInfo.binary_type)
    assert not isinstance('a', PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert not isinstance(1.1, PyInfo.integer_types)

    assert isinstance(int, PyInfo.class_types)
    assert not isinstance(1, PyInfo.class_types)

# Generated at 2022-06-14 06:40:34.853652
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)
        print(PyInfo.text_type)
    else:
        assert PyInfo.string_types == (str,)
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)
        print(PyInfo.text_type)
    assert PyInfo.binary_type


# Generated at 2022-06-14 06:40:46.723138
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Python 2 or 3
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    # string_types
    assert isinstance(PyInfo.string_types, tuple)
    assert len(PyInfo.string_types) == 1
    assert isinstance(PyInfo.string_types[0], type)
    assert isinstance("", PyInfo.string_types)

    # text_type
    assert isinstance(PyInfo.text_type, type)
    assert isinstance("", PyInfo.text_type)

    # binary_type
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance("", PyInfo.binary_type)

    # integer_types
    assert isinstance(PyInfo.integer_types, tuple)

# Generated at 2022-06-14 06:41:12.834435
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.binary_type == (bytes,)
    assert PyInfo.class_types == (type,)
    assert PyInfo.integer_types == (int,)
    assert PyInfo.maxsize == 9223372036854775807
    assert PyInfo.string_types == (str,)
    assert PyInfo.text_type == str


# Class for Functions Meta

# Generated at 2022-06-14 06:41:19.435085
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert type(PyInfo.string_types) == tuple
    assert type(PyInfo.text_type) == type
    assert type(PyInfo.binary_type) == type
    assert type(PyInfo.integer_types) == tuple
    assert type(PyInfo.class_types) == tuple
    assert type(PyInfo.maxsize) == int



# Generated at 2022-06-14 06:41:31.675591
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert isinstance("str", PyInfo.string_types)
    assert not isinstance(22, PyInfo.string_types)
    assert isinstance("", PyInfo.string_types)
    assert isinstance("str", PyInfo.text_type)
    assert not isinstance(22, PyInfo.text_type)
    assert isinstance("", PyInfo.text_type)
    assert isinstance("str", PyInfo.binary_type)
    assert not isinstance(22, PyInfo.binary_type)
    assert isinstance("", PyInfo.binary_type)
    assert isinstance(22, PyInfo.integer_types)
    assert not isinstance("str", PyInfo.integer_types)

# Generated at 2022-06-14 06:41:42.275548
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import codecs
    import os
    import shutil
    import tempfile

    try:
        from io import BytesIO
    except ImportError:
        from io import StringIO as BytesIO

    from .pycompat import iteritems

    py2 = PyInfo.PY2
    py3 = PyInfo.PY3
    string_types = PyInfo.string_types
    text_type = PyInfo.text_type
    binary_type = PyInfo.binary_type
    integer_types = PyInfo.integer_types
    class_types = PyInfo.class_types
    maxsize = PyInfo.maxsize

    def check_py2_3(obj, obj_py2, obj_py3):
        if py2:
            assert obj == obj_py2
        if py3:
            assert obj == obj_

# Generated at 2022-06-14 06:41:52.789100
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance("", PyInfo.string_types)
        assert isinstance(u"", PyInfo.text_type)
        assert not isinstance("", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(1, PyInfo.class_types)

# Generated at 2022-06-14 06:41:54.055346
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo().string_types, tuple)

# Generated at 2022-06-14 06:41:58.520500
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types



# Generated at 2022-06-14 06:42:07.576331
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True
    assert PyInfo.PY3 is False
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == (1 << 31) - 1
    # Note: Don't check the value of PyInfo.maxsize since it may be changed by the host.


# Create a random string with fixed length

# Generated at 2022-06-14 06:42:12.746803
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert_equal(PyInfo.PY2, True)
    assert_equal(PyInfo.PY3, False)
    assert_equal(PyInfo.maxsize, (1 << 63) - 1)


if __name__ == "__main__":
    run()

# Generated at 2022-06-14 06:42:19.891592
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2


# Define which types are allowed in dict-like data structures
allowed_types = (str, int, datetime.datetime, datetime.timedelta, dateutil.tz.tzoffset,
                 dateutil.tz.tzlocal, dateutil.tz.tzutc, dict)

# Get type of variable (custom function)

# Generated at 2022-06-14 06:43:06.390363
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)

# Generated at 2022-06-14 06:43:08.452338
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3



# Generated at 2022-06-14 06:43:13.385183
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == True or PyInfo.PY2 == True
    assert PyInfo.PY3 != PyInfo.PY2
    if PyInfo.PY3:
        assert PyInfo.maxsize == sys.maxsize
        assert sys.maxsize == 2 ** 63 - 1

# Generated at 2022-06-14 06:43:21.930428
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def test_constant(name):
        value = getattr(PyInfo, name)
        assert isinstance(value, PyInfo.integer_types)
        assert value > 0
        setattr(PyInfo, name, value + 1)
        new_value = getattr(PyInfo, name)
        assert new_value == value
        setattr(PyInfo, name, value)
        assert getattr(PyInfo, name) == value

    test_constant("maxsize")

# Generated at 2022-06-14 06:43:24.517753
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3


# ==============================================================================
# String Functions
# ==============================================================================


# Generated at 2022-06-14 06:43:28.620879
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not None
    assert PyInfo.PY3 is not None
    assert PyInfo.string_types is not None
    assert PyInfo.text_type is not None
    assert PyInfo.binary_type is not None
    assert PyInfo.integer_types is not None
    assert PyInfo.class_types is not None

# Generated at 2022-06-14 06:43:33.102158
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 ^ PyInfo.PY3  # XOR
    assert isinstance("", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(type(1), PyInfo.class_types)



# Generated at 2022-06-14 06:43:41.893866
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert type(PyInfo.PY2) is bool
    assert type(PyInfo.PY3) is bool
    if PyInfo.PY2:
        assert PyInfo.PY2 is True
        assert PyInfo.PY3 is False
        assert PyInfo.text_type is unicode
        assert PyInfo.binary_type is str
    elif PyInfo.PY3:
        assert PyInfo.PY2 is False
        assert PyInfo.PY3 is True
        assert PyInfo.text_type is str
        assert PyInfo.binary_type is bytes
    else:
        assert False, "unhandled Python version"

# Generated at 2022-06-14 06:43:44.048346
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # test the class
    assert isinstance(PyInfo.class_types, tuple)

# Generated at 2022-06-14 06:43:46.989055
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    pyinfo = PyInfo()
    assert isinstance(pyinfo.string_types[0], type)
    assert isinstance(pyinfo.text_type, type)
    assert isinstance(pyinfo.binary_type, type)
    assert isinstance(pyinfo.integer_types[0], type)
    assert isinstance(pyinfo.class_types[0], type)
    assert isinstance(pyinfo.maxsize, type(1))


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:45:30.788870
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (sys.version_info[0] == 3), \
        "PyInfo.PY3 should be equal to the result of sys.version_info[0]"
    assert PyInfo.PY2 == (sys.version_info[0] == 2), \
        "PyInfo.PY2 should be equal to the result of sys.version_info[0]"
    if PyInfo.PY3:
        assert PyInfo.string_types == (str,), \
            "PyInfo.string_types should be equal to the result of " \
            "sys.version_info[0]"
        assert PyInfo.text_type == str, \
            "PyInfo.text_type should be equal to the result of " \
            "sys.version_info[0]"

# Generated at 2022-06-14 06:45:37.644090
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """ Unit test for class PyInfo. """
    import six

    for attr in ("PY2", "PY3", "string_types", "text_type", "binary_type", "integer_types", "class_types", "maxsize"):
        assert getattr(six, attr, None) == getattr(PyInfo, attr)




# Generated at 2022-06-14 06:35:43.102902
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3
    assert type(PyInfo.string_types) == tuple
    assert type(PyInfo.text_type) == str
    assert type(PyInfo.binary_type) == bytes
    assert type(PyInfo.integer_types) == tuple
    assert type(PyInfo.class_types) == tuple
    assert type(PyInfo.maxsize) == int

# Generated at 2022-06-14 06:35:54.006283
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)
    else:  # PY2
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)


# Exports

# Generated at 2022-06-14 06:35:56.144777
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 or pyinfo.PY3


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 06:35:56.980954
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3



# Generated at 2022-06-14 06:36:02.786159
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import unittest

    class PyInfoTestCase(unittest.TestCase):
        def test_constructor(self):
            import sys
            PyInfo()
        if sys.version_info[0] == 2:
            def test_maxsize_python2(self):
                self.assertEqual(PyInfo.maxsize, sys.maxsize)

        def test_maxsize_python3(self):
            self.assertGreaterEqual(PyInfo.maxsize, sys.maxsize)

    unittest.main()


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:36:11.778231
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()
    assert info.PY2 == (sys.version_info[0] == 2)
    assert info.PY3 == (sys.version_info[0] == 3)

    if info.PY3:
        assert info.string_types == (str, )
        assert info.text_type == str
        assert info.binary_type == bytes
        assert info.integer_types == (int, )
        assert info.class_types == (type, )
        assert info.maxsize == sys.maxsize
    else:  # PY2
        assert info.string_types == (basestring, )
        assert info.text_type == unicode
        assert info.binary_type == str
        assert info.integer_types == (int, long)

# Generated at 2022-06-14 06:36:24.094956
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from nose.tools import eq_
    from nose.tools import ok_

    assert PyInfo.PY2 != PyInfo.PY3
    if PyInfo.PY2:
        ok_(isinstance('abc', PyInfo.string_types))
    else:
        ok_(not isinstance('abc', PyInfo.string_types))

    if PyInfo.PY3:
        ok_(isinstance('abc', PyInfo.string_types))
    else:
        ok_(not isinstance('abc', PyInfo.string_types))

    if PyInfo.PY2:
        ok_(isinstance(u'abc', PyInfo.string_types))
    else:
        ok_(not isinstance(u'abc', PyInfo.string_types))


# Generated at 2022-06-14 06:36:30.934777
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3

    assert isinstance('a', PyInfo.string_types)
    assert isinstance(b'a', PyInfo.binary_type)
    assert isinstance(u'a', PyInfo.text_type)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:36:36.887286
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert(PyInfo.PY2 or PyInfo.PY3)
    assert(isinstance("", PyInfo.string_types))
    assert(isinstance(u"", PyInfo.text_type))
    assert(isinstance(b"", PyInfo.binary_type))
    assert(isinstance(0, PyInfo.integer_types))
    assert(isinstance(None, type))

# Generated at 2022-06-14 06:36:45.407853
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert isinstance(u'', PyInfo.text_type)
    assert isinstance('', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, int)
    if PyInfo.PY2:
        assert isinstance(1, (int, long))
        assert isinstance(1, long)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(object, PyInfo.class_types)

# Generated at 2022-06-14 06:36:57.187136
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type is str
        assert PyInfo.binary_type is bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)

        assert PyInfo.maxsize == sys.maxsize
    else:  # PY2
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type is unicode
        assert PyInfo.binary_type is str
        assert PyInfo.integer_types == (int, long)

# Generated at 2022-06-14 06:37:03.083121
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (2 == sys.version_info[0])
    assert PyInfo.PY3 == (3 == sys.version_info[0])
    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.integer_types == (int,)
        assert PyInfo.maxsize == sys.maxsize
    else:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.integer_types == (int, long)

# Generated at 2022-06-14 06:37:10.125740
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.string_types == (str, ) if PyInfo.PY3 else (
        basestring, )
    assert PyInfo.text_type == str if PyInfo.PY3 else unicode
    assert PyInfo.binary_type == bytes if PyInfo.PY3 else str

# Generated at 2022-06-14 06:37:20.098386
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert isinstance('', PyInfo.string_types)
        assert isinstance(b'', PyInfo.binary_type)
        assert isinstance(u'', PyInfo.text_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(object, PyInfo.class_types)

        assert PyInfo.maxsize == sys.maxsize
    else:  # PY2
        assert isinstance('', PyInfo.string_types)
        assert isinstance(b'', PyInfo.binary_type)
        assert not isinstance(u'', PyInfo.string_types)


# Generated at 2022-06-14 06:37:24.669864
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.string_types
    assert PyInfo.binary_type
    assert PyInfo.text_type
    assert PyInfo.integer_types
    assert PyInfo.class_types
    assert PyInfo.maxsize

# Generated at 2022-06-14 06:37:29.916864
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()
    assert info.PY2 == (sys.version_info[0] == 2)
    assert info.PY3 == (sys.version_info[0] == 3)
    assert info.string_types
    assert info.text_type
    assert info.binary_type
    assert info.integer_types
    assert info.class_types

# Generated at 2022-06-14 06:37:39.750430
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance(u"", PyInfo.text_type)
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:37:45.326831
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance('', PyInfo.string_types)
    assert isinstance(PyInfo.text_type(''), PyInfo.text_type)
    assert isinstance(PyInfo.binary_type(''), PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)



# Generated at 2022-06-14 06:37:53.895865
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types
    assert PyInfo.maxsize

    assert not PyInfo.PY3
    assert not PyInfo.string_types
    assert not PyInfo.text_type
    assert not PyInfo.binary_type
    assert not PyInfo.integer_types
    assert not PyInfo.class_types
    assert not PyInfo.maxsize

# Generated at 2022-06-14 06:38:03.751701
# Unit test for constructor of class PyInfo
def test_PyInfo():
    obj = PyInfo()
    assert obj.PY2 is False
    assert obj.PY3 is True
    assert obj.string_types == (str,)
    assert obj.text_type == str
    assert obj.binary_type == bytes
    assert obj.integer_types == (int,)
    assert obj.class_types == (type,)
    # sys.maxsize == 9223372036854775807
    assert obj.maxsize == sys.maxsize


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help="test the class PyInfo")
    args = parser.parse_args()

    if args.test:
        test_PyInfo()

# Generated at 2022-06-14 06:38:18.806587
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import os
    import sys
    import fcntl

    # on windows, I couldn't find a method to limit max_number - so I just
    # checked if an OverflowError is thrown
    # TODO: use the PyInfo class to check that max_number is the same
    # like sys.maxint
    try:
        max_number = sys.maxint
    except AttributeError:
        # Py3 doesn't have sys.maxint
        max_number = sys.maxsize
    if sys.platform == 'win32':
        assert_raises_regex(OverflowError, "", PyInfo, '')
    elif sys.platform == 'java':
        # Jython always uses 32 bits.
        assert PyInfo('').maxsize == int((1 << 31) - 1)

# Generated at 2022-06-14 06:38:26.659127
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """ PyInfo test """
    print(PyInfo.PY2)
    print(PyInfo.PY3)
    print(PyInfo.string_types)
    print(PyInfo.text_type)
    print(PyInfo.binary_type)
    print(PyInfo.integer_types)
    print(PyInfo.class_types)
    print(PyInfo.maxsize)


# Unit test

# Generated at 2022-06-14 06:38:31.043002
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert id(PyInfo.string_types) == id(PyInfo.string_types)
    assert isinstance(PyInfo.string_types, tuple)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:38:43.427512
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == sys.version_info[0] == 2
    assert PyInfo.PY3 == sys.version_info[0] == 3

    assert isinstance("1", PyInfo.string_types)
    assert not isinstance(b"1", PyInfo.string_types)
    assert isinstance(u"1", PyInfo.text_type)

    assert isinstance(b"1", PyInfo.binary_type)
    assert not isinstance("1", PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert not isinstance(1.0, PyInfo.integer_types)

    assert isinstance(int, PyInfo.class_types)
    assert not isinstance(dict, PyInfo.class_types)

# Generated at 2022-06-14 06:38:48.210619
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance("", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(str, PyInfo.class_types)



# Generated at 2022-06-14 06:38:57.162607
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)

# Generated at 2022-06-14 06:39:04.181597
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print(PyInfo.PY2)
    print(PyInfo.PY3)
    print(PyInfo.string_types)
    print(PyInfo.text_type)
    print(PyInfo.binary_type)
    print(PyInfo.integer_types)
    print(PyInfo.class_types)
    print(PyInfo.maxsize)


# Unit test

# Generated at 2022-06-14 06:39:11.253884
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not None
    assert PyInfo.PY3 is not None
    assert PyInfo.string_types is not None
    assert PyInfo.text_type is not None
    assert PyInfo.binary_type is not None
    assert PyInfo.integer_types is not None
    assert PyInfo.maxsize is not None

# Generated at 2022-06-14 06:39:16.326800
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance(PyInfo.maxsize, int)
        assert isinstance(PyInfo.maxsize, long)
    else:
        assert isinstance(PyInfo.maxsize, int)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:39:19.973208
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(PyInfo.maxsize, int)
    assert isinstance(PyInfo.maxsize, PyInfo.integer_types)

# Generated at 2022-06-14 06:39:42.371340
# Unit test for constructor of class PyInfo
def test_PyInfo():

    def get_attrs(inst):
        return [attr for attr in dir(inst) if not attr.startswith('__')]

    import sys
    if sys.version_info.major == 3:
        py2_attrs = get_attrs(PyInfo())
        assert py2_attrs == ['PY2', 'PY3', 'binary_type', 'class_types',
                             'integer_types', 'maxsize', 'string_types',
                             'text_type']
        assert PyInfo().maxsize == sys.maxsize
    else:
        py2_attrs = get_attrs(PyInfo())

# Generated at 2022-06-14 06:39:56.673784
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('', PyInfo.string_types), 'string types should be basestring, but is {}'.format(
            ', '.join(map(lambda s: str(s), PyInfo.string_types))
        )
        assert isinstance(u'', PyInfo.string_types), 'string types should be unicode, but is {}'.format(
            ', '.join(map(lambda s: str(s), PyInfo.string_types))
        )
    elif PyInfo.PY3:
        assert isinstance('', PyInfo.string_types), 'string types should be str, but is {}'.format(
            ', '.join(map(lambda s: str(s), PyInfo.string_types))
        )
    else:
        raise EnvironmentError('No valid python version found')




# Generated at 2022-06-14 06:40:04.207714
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.string_types == basestring
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == sys.maxsize


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:40:16.227314
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        for i in range(3):
            assert isinstance(i, PyInfo.integer_types)
        assert isinstance("", PyInfo.string_types)
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(PyInfo, PyInfo.class_types)
    else:  # PY2
        assert isinstance(0, PyInfo.integer_types)

# Generated at 2022-06-14 06:40:27.331538
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert not (PyInfo.PY2 and PyInfo.PY3)


# This is a py2/py3 compatible implementation of the following py3 code:
#
#   isinstance(obj, (basestring, bytearray, memoryview))
#
# Note that in py2, the 'memoryview' is unsupported and thus it is converted
# to 'buffer'.
#
# To write code in a py2/py3 compatible way, you can use this function as a
# substitute of 'isinstance(obj, (basestring, bytearray, memoryview))'.
#
# This function makes no difference between the py2 'str' and the py3 'bytes'.
# Both are considered 'binary_type'.
#

# Generated at 2022-06-14 06:40:33.710651
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()
    assert isinstance(info.PY2, bool)
    assert isinstance(info.PY3, bool)
    assert isinstance(info.string_types, tuple)
    assert isinstance(info.text_type, type)
    assert isinstance(info.binary_type, type)
    assert isinstance(info.integer_types, tuple)
    assert isinstance(info.class_types, tuple)



# Generated at 2022-06-14 06:40:43.947283
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.string_types[0], type)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.integer_types[0], type)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.class_types[0], type)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:40:50.950414
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    print(pyinfo.PY2)
    print(pyinfo.PY3)
    print(pyinfo.string_types)
    print(pyinfo.text_type)
    print(pyinfo.integer_types)
    print(pyinfo.class_types)
    print(pyinfo.maxsize)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:40:53.644247
# Unit test for constructor of class PyInfo
def test_PyInfo():
    i = PyInfo()
    assert i.PY2 or i.PY3
    assert i.maxsize > 0



# Generated at 2022-06-14 06:41:04.680141
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    if PyInfo.PY3:
        assert PyInfo.maxsize == sys.maxsize
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == type
    else:  # PY2
        # PY2
        if sys.platform.startswith("java"):
            # Jython always uses 32 bits.
            assert PyInfo.maxsize == int((1 << 31) - 1)

# Generated at 2022-06-14 06:41:28.566776
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 ^ PyInfo.PY3
    assert isinstance('123', PyInfo.string_types)
    assert isinstance(123, PyInfo.integer_types)
    assert isinstance(PyInfo(12), PyInfo.class_types)

# Generated at 2022-06-14 06:41:39.064383
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert str in PyInfo.string_types
        assert unicode in PyInfo.string_types
        assert str is PyInfo.binary_type
        assert int in PyInfo.integer_types
        assert long in PyInfo.integer_types
        assert type in PyInfo.class_types
        assert types.ClassType in PyInfo.class_types
    else:
        assert str in PyInfo.string_types
        assert bytes not in PyInfo.string_types
        assert str is PyInfo.text_type
        assert bytes is PyInfo.binary_type
        assert int in PyInfo.integer_types
        assert type in PyInfo.class_types

# Generated at 2022-06-14 06:41:45.562127
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    if PyInfo.PY3:
        assert isinstance('', PyInfo.text_type)
        assert isinstance(b'', PyInfo.binary_type)
    else:  # PyInfo.PY2
        assert isinstance('', PyInfo.string_types)
        assert isinstance(u'', PyInfo.string_types)

# Generated at 2022-06-14 06:41:53.774598
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert isinstance(pyinfo.PY2, bool)
    assert isinstance(pyinfo.PY3, bool)
    assert isinstance(pyinfo.string_types, tuple)
    if sys.version_info[0] == 2:
        assert pyinfo.text_type == unicode
        assert pyinfo.binary_type == str
        assert pyinfo.integer_types == (int, long)
        assert pyinfo.class_types == (type, types.ClassType)
        assert pyinfo.maxsize > 0
    else:
        assert pyinfo.text_type == str
        assert pyinfo.binary_type == bytes
        assert pyinfo.integer_types == (int,)
        assert pyinfo.class_types == (type,)
        assert pyinfo.maxsize > 0

# Generated at 2022-06-14 06:42:02.541546
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    >>> pi = PyInfo()
    >>> pi.PY2
    False
    >>> pi.PY3
    True
    >>> pi.string_types
    (<class 'str'>,)
    >>> pi.maxsize
    9223372036854775807
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS, verbose=True)

# Generated at 2022-06-14 06:42:10.191761
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:42:12.128862
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3



# Generated at 2022-06-14 06:42:25.397428
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert pyinfo.PyInfo.PY2 is True
    assert pyinfo.PyInfo.PY3 is False
    assert isinstance(pyinfo.PyInfo.string_types, tuple)
    assert basestring in pyinfo.PyInfo.string_types
    assert isinstance(pyinfo.PyInfo.text_type, unicode)
    assert isinstance(pyinfo.PyInfo.binary_type, str)
    assert isinstance(pyinfo.PyInfo.integer_types, tuple)
    assert int in pyinfo.PyInfo.integer_types
    assert long in pyinfo.PyInfo.integer_types
    assert isinstance(pyinfo.PyInfo.class_types, tuple)
    assert type in pyinfo.PyInfo.class_types
    assert types.ClassType in pyinfo.PyInfo.class_types
    assert sys.max

# Generated at 2022-06-14 06:42:39.248913
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(b"", PyInfo.string_types)

    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.text_type)
    assert isinstance(b"", PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:42:42.252667
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if not PyInfo.PY2:
        assert PyInfo.maxsize == sys.maxsize



# Generated at 2022-06-14 06:43:28.110340
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)
    if not PyInfo.PY2:
        assert isinstance(PyInfo.maxsize, int)



# Generated at 2022-06-14 06:43:36.709935
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert not (PyInfo.PY2 and PyInfo.PY3)
    assert isinstance(u"test", PyInfo.string_types)
    assert isinstance(b"test", PyInfo.binary_type)
    assert isinstance(b"test", PyInfo.string_types)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)
    if sys.version_info[:2] == (3, 2):
        # issue8696
        assert PyInfo.maxsize > (1 << 32)
    else:
        assert PyInfo.maxsize > (1 << 31)

# Generated at 2022-06-14 06:43:44.502248
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:43:52.586277
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance("", PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)
    assert isinstance(0, PyInfo.class_types)
    if PyInfo.PY3:
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(b"", PyInfo.string_types)
    else:
        assert not isinstance(b"", PyInfo.binary_type)
        assert not isinstance(b"", PyInfo.string_types)
    if PyInfo.PY3 or PyInfo.maxsize > 2147483647:
        assert PyInfo.maxsize > 2

# Generated at 2022-06-14 06:44:02.979997
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert bool(PyInfo.PY2) != bool(PyInfo.PY3)

    for t in PyInfo.string_types:
        assert isinstance('test', t)
    assert isinstance(u'test', PyInfo.text_type)
    assert isinstance('test', PyInfo.binary_type)

    for t in PyInfo.class_types:
        assert isinstance(PyInfo, t)

    for t in PyInfo.integer_types:
        assert isinstance(PyInfo.maxsize, t)
    assert isinstance(PyInfo.maxsize, PyInfo.integer_types[-1])

# Generated at 2022-06-14 06:44:11.519941
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    if PyInfo.PY2:
        assert str in PyInfo.string_types
        assert unicode in PyInfo.string_types
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert 1 in PyInfo.integer_types

# Generated at 2022-06-14 06:44:22.292644
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == isinstance(__name__, str)

# Generated at 2022-06-14 06:44:23.659974
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:44:30.258689
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py2 = PyInfo.PY2
    py3 = PyInfo.PY3
    assert py2 or py3
    assert not (py2 and py3)

    if py2:
        assert type('abc') is types.StringType
        assert PyInfo.maxsize == sys.maxint
    else:
        assert type('abc') is not types.StringType
        assert PyInfo.maxsize == sys.maxsize


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:44:41.440837
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert not PyInfo.PY3
        assert str == PyInfo.text_type
        assert str == PyInfo.binary_type
        assert isinstance('', PyInfo.text_type)
        assert isinstance('', PyInfo.binary_type)
        assert isinstance(u'', PyInfo.text_type)
        assert isinstance(u'', PyInfo.binary_type)
    else:
        assert not PyInfo.PY2
        assert str == PyInfo.text_type
        assert bytes == PyInfo.binary_type
        assert isinstance('', PyInfo.text_type)
        assert not isinstance('', PyInfo.binary_type)
        assert isinstance(u'', PyInfo.text_type)
        assert not isinstance(u'', PyInfo.binary_type)
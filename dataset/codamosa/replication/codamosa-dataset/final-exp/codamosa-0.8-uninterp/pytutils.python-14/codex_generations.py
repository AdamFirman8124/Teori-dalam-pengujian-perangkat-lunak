

# Generated at 2022-06-14 06:35:46.453876
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 ^ PyInfo.PY3
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("hi", PyInfo.string_types)
    assert isinstance(u"hi", PyInfo.string_types)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:35:55.659801
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
        assert PyInfo.maxsize == sys.maxsize
    else:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)

# Generated at 2022-06-14 06:36:05.441514
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def is_expected(arg, expected_type_name):
        assert isinstance(arg, getattr(PyInfo, expected_type_name))

    assert PyInfo.PY2 or PyInfo.PY3

    is_expected(PyInfo.string_types, 'class_types')
    is_expected(PyInfo.text_type, 'class_types')
    is_expected(PyInfo.binary_type, 'class_types')
    is_expected(PyInfo.integer_types, 'class_types')
    assert isinstance(PyInfo.integer_types, tuple)
    is_expected(PyInfo.class_types, 'class_types')
    assert isinstance(PyInfo.class_types, tuple)

    is_expected(PyInfo.maxsize, 'integer_types')



# Generated at 2022-06-14 06:36:12.059181
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance("".encode("UTF-8"), PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)

    assert isinstance(PyInfo, PyInfo.class_types)
    assert PyInfo.maxsize > 0

# Generated at 2022-06-14 06:36:24.012025
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
    assert isinstance(PyInfo.maxsize, int)
    assert isinstance(PyInfo.maxsize, int)
    assert PyInfo.maxsize >= 1 << 32


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:36:36.938705
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance(u'', PyInfo.text_type)
        assert isinstance(b'', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:36:45.711778
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('foo', PyInfo.string_types)
    assert isinstance(u'foo', PyInfo.text_type)
    assert isinstance(b'foo', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(object, PyInfo.class_types)

    # Memory size test
    if PyInfo.PY3:
        assert PyInfo.maxsize == sys.maxsize
    else:
        X = PyInfo.maxsize

        assert X == int((1 << 63) - 1)
        assert X == int((1 << 31) - 1)



# Generated at 2022-06-14 06:36:52.704032
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    assert PyInfo.PY2 is not PyInfo.PY3
    if PyInfo.PY2:
        assert not isinstance(1, PyInfo.integer_types)
        assert isinstance(1, PyInfo.integer_types + (bool,))
    else:
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:36:57.404298
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert PyInfo.maxsize > 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:37:00.336727
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3, "Unsupported Python version {}".format(
        sys.version_info[0])

# Generated at 2022-06-14 06:37:07.570287
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert type(PyInfo.PY2) == bool
    assert type(PyInfo.PY3) == bool
    assert type(PyInfo.string_types) == tuple
    assert type(PyInfo.text_type) == type
    assert type(PyInfo.binary_type) == type
    assert type(PyInfo.integer_types) == tuple
    assert type(PyInfo.class_types) == tuple
    assert type(PyInfo.maxsize) == int

# Generated at 2022-06-14 06:37:19.488466
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    isinstance("foo", PyInfo.string_types)
    isinstance(u"foo", PyInfo.string_types)
    isinstance(b"foo", PyInfo.binary_type)

    isinstance("foo", PyInfo.text_type)
    isinstance(u"foo", PyInfo.text_type)
    isinstance(b"foo", PyInfo.binary_type)

    if not PyInfo.PY3:
        isinstance("foo", PyInfo.binary_type)
        isinstance(u"foo", PyInfo.text_type)
        isinstance(b"foo", PyInfo.binary_type)

    isinstance(42, PyInfo.integer_types)

# Generated at 2022-06-14 06:37:31.384857
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True
    assert PyInfo.PY3 is False

    assert isinstance("a", PyInfo.string_types)
    assert isinstance(u"a", PyInfo.string_types)
    assert isinstance(u"a", PyInfo.text_type)
    assert isinstance("a".encode("UTF-8"), PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)

    assert isinstance(int, PyInfo.class_types)
    assert isinstance(type, PyInfo.class_types)
    assert isinstance(PyInfo, PyInfo.class_types)

    info = PyInfo()
    assert isinstance(info.PY2, bool)
    assert isinstance(info.PY3, bool)

    assert info.PY2 is PyInfo

# Generated at 2022-06-14 06:37:40.306223
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 + PyInfo.PY3 == 1
    assert PyInfo.maxsize > 1
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:37:44.379255
# Unit test for constructor of class PyInfo
def test_PyInfo():
    class_types = (type, types.ClassType) if not PyInfo.PY3 else type
    assert PyInfo.class_types == class_types


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:37:56.633505
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()

    # Verify that PyInfo has set all the right variables
    assert pyinfo.PY2 == (2 == sys.version_info[0])
    assert pyinfo.PY3 == (3 == sys.version_info[0])
    assert pyinfo.string_types == (basestring,) if pyinfo.PY2 else (str,)
    assert pyinfo.text_type == unicode if pyinfo.PY2 else str
    assert pyinfo.binary_type == str if pyinfo.PY2 else bytes
    assert pyinfo.integer_types == (int, long) if pyinfo.PY2 else (int,)
    assert pyinfo.class_types == (type, types.ClassType) if pyinfo.PY2 else (type,)

# Generated at 2022-06-14 06:38:01.576649
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py2 = (PyInfo.PY2, True)
    py3 = (PyInfo.PY3, True)
    assert py2 != py3
    assert py2 == py2
    assert py3 == py3
    assert py2 != py3
    assert py3 != py2



# Generated at 2022-06-14 06:38:05.966023
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # check result of "binary_type is bytes"
    # Check types in PY2 and PY3
    # Check maxsize in PY2 and PY3
    pass

# Generated at 2022-06-14 06:38:16.784313
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.maxsize > 0
    assert PyInfo.maxsize == sys.maxsize
    assert isinstance('', PyInfo.string_types)
    assert isinstance(b'', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert not isinstance(1, PyInfo.string_types)
    assert not isinstance([], PyInfo.string_types)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:38:22.170734
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert isinstance('', PyInfo.string_types)
        assert isinstance('', PyInfo.text_type)
        assert isinstance(b'', PyInfo.binary_type)
        assert isinstance(0, PyInfo.integer_types)
        assert isinstance(object, PyInfo.class_types)
    else:  # PY2
        assert isinstance('', PyInfo.string_types)
        assert isinstance(u'', PyInfo.text_type)
        assert isinstance('', PyInfo.binary_type)
        assert isinstance(0, PyInfo.integer_types)
        assert isinstance(object, PyInfo.class_types)

    assert isinstance(PyInfo.maxsize, int)


if __name__ == '__main__':
    import nose

    nose

# Generated at 2022-06-14 06:38:32.088430
# Unit test for constructor of class PyInfo
def test_PyInfo():
    i = PyInfo()
    assert i.PY2 == sys.version_info[0] == 2
    assert i.PY3 == sys.version_info[0] == 3
    assert i.maxsize >= 0


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:38:40.034401
# Unit test for constructor of class PyInfo
def test_PyInfo():
    is_python2 = PyInfo.PY2
    is_python3 = PyInfo.PY3
    assert is_python2 ^ is_python3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.string_types[0], type)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.maxsize, int)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.integer_types[0], type)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.class_types[0], type)
    return


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:53.097462
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    assert isinstance(PyInfo.string_types, (list, tuple))
    assert len(PyInfo.string_types) == 1 and isinstance(PyInfo.string_types[0], type)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, (list, tuple))
    assert len(PyInfo.integer_types) == 2 and isinstance(PyInfo.integer_types[0], type) and isinstance(PyInfo.integer_types[1], type)
    assert isinstance(PyInfo.class_types, (list, tuple))

# Generated at 2022-06-14 06:39:04.657732
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # string_type
    assert isinstance("hello", PyInfo.string_types)
    assert isinstance(u"hello", PyInfo.string_types)
    # text_type
    assert isinstance("hello", PyInfo.text_type)
    # binary_type
    assert isinstance(b"hello", PyInfo.binary_type)
    # maxsize
    if PyInfo.PY2:
        assert PyInfo.maxsize == (1 << 63) - 1
    else:
        assert PyInfo.maxsize == sys.maxsize
    # integer_types
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:39:07.338461
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2



# Generated at 2022-06-14 06:39:19.265686
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Test for PY2
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert not isinstance(b"", PyInfo.string_types)

    assert isinstance("", PyInfo.text_type)
    assert not isinstance(u"", PyInfo.text_type)
    assert not isinstance(b"", PyInfo.text_type)

    assert not isinstance("", PyInfo.binary_type)
    assert not isinstance(u"", PyInfo.binary_type)
    assert isinstance(b"", PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(0, PyInfo.integer_types)
    assert isinstance(2**63, PyInfo.integer_types)

   

# Generated at 2022-06-14 06:39:24.453840
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.maxsize == 2147483647
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.binary_type == str
    assert PyInfo.class_types == (type, types.ClassType)

# Generated at 2022-06-14 06:39:34.851363
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import pyinfo
    assert isinstance(pyinfo.PyInfo, type)
    assert isinstance(pyinfo.PyInfo(), pyinfo.PyInfo)

    assert isinstance(pyinfo.PyInfo.PY2, bool)
    assert isinstance(pyinfo.PyInfo.PY3, bool)

    assert isinstance(pyinfo.PyInfo.string_types, tuple)
    assert isinstance(pyinfo.PyInfo.text_type, type)
    assert isinstance(pyinfo.PyInfo.binary_type, type)
    assert isinstance(pyinfo.PyInfo.integer_types, tuple)
    assert isinstance(pyinfo.PyInfo.class_types, tuple)

    assert isinstance(pyinfo.PyInfo.maxsize, int)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:39:36.248568
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3



# Generated at 2022-06-14 06:39:43.822835
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if "unicode" in dir():
        assert PyInfo.PY2
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type is unicode
        assert PyInfo.binary_type is bytes
        assert PyInfo.class_types == (type, types.ClassType)
    else:
        assert PyInfo.PY3
        assert PyInfo.integer_types == (int,)
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type is str
        assert PyInfo.binary_type is bytes
        assert PyInfo.class_types == (type,)

    assert PyInfo.maxsize > 0

# Generated at 2022-06-14 06:39:59.636080
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert PyInfo.maxsize > 0
    assert isinstance(u"", PyInfo.text_type) is True
    assert isinstance(b"", PyInfo.binary_type) is True
    assert callable(PyInfo.string_types) is True
    assert callable(PyInfo.integer_types) is True
    assert callable(PyInfo.class_types) is True


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:40:04.644916
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('', PyInfo.text_type)
    assert isinstance(b'', PyInfo.binary_type)
    assert isinstance([], types.ListType)
    assert isinstance(0, int)



# Generated at 2022-06-14 06:40:14.125711
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance("aaa", PyInfo.string_types)
        assert not isinstance(b"aaa", PyInfo.string_types)

        assert not isinstance("aaa", PyInfo.binary_type)
        assert isinstance(b"aaa", PyInfo.binary_type)

        assert isinstance(unicode("aaa"), PyInfo.text_type)
        assert not isinstance("aaa", PyInfo.text_type)

        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:40:22.951574
# Unit test for constructor of class PyInfo
def test_PyInfo():
    i = PyInfo()
    assert type(i.PY2) is bool
    assert type(i.PY3) is bool
    assert type(i.string_types) is tuple
    assert type(i.text_type) is type
    assert type(i.binary_type) is type
    assert type(i.integer_types) is tuple
    assert type(i.class_types) is tuple
    assert type(i.maxsize) is int



# Generated at 2022-06-14 06:40:33.548797
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import os
    import sys

    assert PyInfo.PY2 or PyInfo.PY3, "Unknown Python version"

    # test some basic properties of the class
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.class_types, tuple)

    assert PyInfo.maxsize < sys.maxsize
    assert PyInfo.maxsize >= PyInfo.string_types[0](-1).bit_length()

    # test some assumptions
    assert isinstance(os.name, PyInfo.text_type)
    assert isinstance(sys.platform, PyInfo.text_type)

# Generated at 2022-06-14 06:40:35.510059
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pass


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:40:47.022089
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3

    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert not isinstance(b'', PyInfo.string_types)
    assert isinstance(u'', PyInfo.text_type)
    assert not isinstance('', PyInfo.text_type)
    assert not isinstance(b'', PyInfo.text_type)
    assert isinstance(b'', PyInfo.binary_type)
    assert not isinstance('', PyInfo.binary_type)
    assert not isinstance(u'', PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:40:54.197236
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()
    assert pi.PY2
    assert not pi.PY3
    assert pi.string_types == (basestring,)
    assert pi.text_type == unicode
    assert pi.binary_type == str
    assert pi.integer_types == (int, long)
    assert pi.maxsize == sys.maxint

# The default locale
LOCALE_DEFAULT = "C"



# Generated at 2022-06-14 06:40:59.374024
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    assert PyInfo.PY2 is False or PyInfo.PY3 is False
    assert (
        PyInfo.maxsize == (1 << 31) - 1 or PyInfo.maxsize == (1 << 63) - 1
    )  # noqa


test_PyInfo()

# Generated at 2022-06-14 06:41:05.514790
# Unit test for constructor of class PyInfo
def test_PyInfo():
    psi = PyInfo()

    assert psi.PY2 == sys.version_info[0] == 2
    assert psi.PY3 == sys.version_info[0] == 3

    assert psi.maxsize == sys.maxsize
    assert psi.binary_type == sys.maxsize

# Generated at 2022-06-14 06:41:32.144167
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert len(PyInfo.string_types) == 1
    assert len(PyInfo.integer_types) == 2
    assert len(PyInfo.class_types) == 2
    if PyInfo.PY2:
        assert type("") in PyInfo.string_types
        assert type(1) in PyInfo.integer_types
        assert type(object) in PyInfo.class_types
    else:
        assert str in PyInfo.string_types
        assert int in PyInfo.integer_types
        assert type(object) in PyInfo.class_types

# Generated at 2022-06-14 06:41:41.400669
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

# Generated at 2022-06-14 06:41:49.147978
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert type(PyInfo.string_types) == tuple
    assert PyInfo.text_type == str or PyInfo.text_type == unicode
    assert PyInfo.binary_type == str or PyInfo.binary_type == bytes
    assert type(PyInfo.integer_types) == tuple
    assert type(PyInfo.class_types) == tuple
    assert type(PyInfo.maxsize) == int
    assert PyInfo.maxsize > 0

# Generated at 2022-06-14 06:41:57.876522
# Unit test for constructor of class PyInfo
def test_PyInfo():
    try:
        assert PyInfo.PY2
        assert not PyInfo.PY3
        assert isinstance('str', PyInfo.string_types)
        assert isinstance('str', PyInfo.text_type)
        assert isinstance(b'a', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
    except NameError:
        assert not PyInfo.PY2
        assert PyInfo.PY3
        assert isinstance('str', PyInfo.string_types)
        assert isinstance('str', PyInfo.text_type)
        assert isinstance(b'a', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:42:08.486051
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert not PyInfo.PY2 or isinstance('', PyInfo.string_types)
    assert not PyInfo.PY2 or isinstance('', PyInfo.text_type)
    assert not PyInfo.PY2 or isinstance(b'', PyInfo.binary_type)
    assert not PyInfo.PY2 or isinstance(1, PyInfo.integer_types)
    assert not PyInfo.PY2 or isinstance(type, PyInfo.class_types)
    assert not PyInfo.PY2 or PyInfo.maxsize <= (2 ** 63) - 1

    assert PyInfo.PY3 or isinstance(u'', PyInfo.string_types)
    assert PyInfo.PY3 or isinstance(u'', PyInfo.text_type)

# Generated at 2022-06-14 06:42:22.605695
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 or pyinfo.PY3

    if pyinfo.PY3:
        assert isinstance("1", pyinfo.string_types)
        assert isinstance("1", pyinfo.text_type)
        assert isinstance("1".encode("utf-8"), pyinfo.binary_type)
        assert isinstance(1, pyinfo.integer_types)
        assert isinstance(pyinfo, pyinfo.class_types)
    else:  # PY2
        assert isinstance("1", pyinfo.string_types)
        assert isinstance(u"1", pyinfo.text_type)
        assert isinstance("1", pyinfo.binary_type)
        assert isinstance(1, pyinfo.integer_types)

# Generated at 2022-06-14 06:42:27.996648
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert not isinstance("", PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)
    assert isinstance(0, PyInfo.class_types)
    if PyInfo.PY2:
        import struct

        assert struct.calcsize("l") == 4
        assert struct.calcsize("L") == 8
    assert PyInfo.maxsize <= sys.maxsize


test_PyInfo()

# Generated at 2022-06-14 06:42:41.716849
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import unittest2
    from intbitset import PyInfo

    class PyInfoTestCase(unittest2.TestCase):

        def test_PY2(self):
            if sys.version_info[0] == 2:
                self.assertIs(True, PyInfo.PY2)
            else:
                self.assertIs(False, PyInfo.PY2)

        def test_PY3(self):
            if sys.version_info[0] == 3:
                self.assertIs(True, PyInfo.PY3)
            else:
                self.assertIs(False, PyInfo.PY3)

        def test_string_types(self):
            self.assertIsInstance('', PyInfo.string_types)
            self.assertIsNotInstance(1, PyInfo.string_types)



# Generated at 2022-06-14 06:42:44.903606
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 == sys.version_info[0] == 2
    assert pyinfo.maxsize > 0

# Generated at 2022-06-14 06:42:48.106201
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()
    print(info.PY2)
    print(info.PY3)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:43:32.653274
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (sys.version_info[0] == 3)


test_PyInfo()

# Generated at 2022-06-14 06:43:40.155258
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == True
    assert PyInfo.PY2 == False
    assert PyInfo.string_types != (str, unicode)
    assert PyInfo.text_type == str
    assert PyInfo.binary_type != (str, unicode)
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == (1 << 63) - 1
    print('test_PyInfo')


test_PyInfo()

# Generated at 2022-06-14 06:43:48.874561
# Unit test for constructor of class PyInfo
def test_PyInfo():
    '''
    >>> PyInfo.PY3 == (3 == sys.version_info[0])
    True
    >>> PyInfo.PY2 == (2 == sys.version_info[0])
    True
    >>> isinstance('xxx', PyInfo.string_types)
    True
    >>> isinstance(b'xxx', PyInfo.binary_type)
    True
    >>> isinstance(u'xxx', PyInfo.text_type)
    True
    >>> isinstance(1, PyInfo.integer_types)
    True
    >>> isinstance(1, PyInfo.class_types)
    False
    '''
    pass



# Generated at 2022-06-14 06:43:57.888165
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert isinstance('', PyInfo.string_types)
        assert isinstance(u'', PyInfo.string_types)
        assert isinstance(b'', PyInfo.string_types)
        assert isinstance(1, PyInfo.string_types) is False

        assert isinstance('', PyInfo.text_type)
        assert isinstance(u'', PyInfo.text_type)
        assert isinstance(b'', PyInfo.text_type) is False
        assert isinstance(1, PyInfo.text_type) is False

        assert isinstance(b'', PyInfo.binary_type)
       

# Generated at 2022-06-14 06:44:06.322339
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Unit test for constructor of class PyInfo
    inst = PyInfo()

    assert isinstance(inst.string_types, tuple)
    assert isinstance(inst.text_type, str)
    assert isinstance(inst.binary_type, str)
    assert isinstance(inst.integer_types, tuple)
    assert isinstance(inst.class_types, tuple)
    assert isinstance(inst.maxsize, int)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:44:11.421021
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2 and PyInfo.PY3:
        assert False
    if PyInfo.PY2:
        assert type(PyInfo.string_types[0]) == str
        assert type(PyInfo.text_type) == unicode
        assert type(PyInfo.binary_type) == str
    elif PyInfo.PY3:
        assert type(PyInfo.string_types[0]) == str
        assert type(PyInfo.text_type) == str
        assert type(PyInfo.binary_type) == bytes
    else:
        assert False



# Generated at 2022-06-14 06:44:19.415245
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)
    assert PyInfo.PY3 == (not PyInfo.PY2)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:44:25.876933
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.maxsize > 0  # since 2.6

    pyinf = PyInfo()
    assert pyinf

    if PyInfo.PY2:
        assert PyInfo.class_types == (type, types.ClassType)
        assert PyInfo.integer_types == (int, long)
    else:
        assert PyInfo.class_types == (type,)
        assert PyInfo.integer_types == (int,)

# Generated at 2022-06-14 06:44:33.750167
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 or PyInfo.PY2, "PyInfo.PY2 or PyInfo.PY3 should be True"
    assert not (PyInfo.PY3 and PyInfo.PY2), "PyInfo.PY3 and PyInfo.PY2 " \
                                            "can't be True at the same time"



# Generated at 2022-06-14 06:44:37.065286
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == True or PyInfo.PY3 == False
    assert PyInfo.PY2 == True or PyInfo.PY2 == False
    assert PyInfo.maxsize > 0

    if PyInfo.PY3:
        assert PyInfo.maxsize > 9223372036854775
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
    if PyInfo.PY2:
        assert PyInfo.maxsize > 2147483647
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
    pass


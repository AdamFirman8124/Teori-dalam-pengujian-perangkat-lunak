

# Generated at 2022-06-14 06:35:45.541173
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not True
    assert PyInfo.PY3 is not False
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance("", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.integer_types)
    assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:35:51.877581
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("test", PyInfo.string_types) is True
    assert isinstance("test", PyInfo.binary_type) is False
    assert isinstance("test", PyInfo.text_type) is False
    if PyInfo.PY2:
        assert isinstance("test", PyInfo.integer_types) is False
        assert isinstance(1, PyInfo.integer_types) is True

    a = []
    assert isinstance(a, PyInfo.class_types) is True

# Generated at 2022-06-14 06:35:53.735765
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance('', PyInfo.text_type)
    assert isinstance(1, PyInfo.integer_types)



# Generated at 2022-06-14 06:36:04.992208
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert not isinstance(1, PyInfo.string_types)

    assert isinstance(u"", PyInfo.text_type)
    assert not isinstance("", PyInfo.text_type)
    assert not isinstance(1, PyInfo.text_type)

    assert isinstance("", PyInfo.binary_type)
    assert not isinstance(u"", PyInfo.binary_type)
    assert not isinstance(1, PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1 << 63, PyInfo.integer_types)

# Generated at 2022-06-14 06:36:14.786862
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert len(PyInfo.string_types) == 1
    assert isinstance('', PyInfo.string_types[0])
    assert isinstance(u'', PyInfo.text_type)
    assert isinstance(b'', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert len(PyInfo.class_types) == 1
    assert isinstance(PyInfo, PyInfo.class_types[0])
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:36:25.510803
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == True or PyInfo.PY2 == True
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)


if __name__ == '__main__':
    test_PyInfo()



# Generated at 2022-06-14 06:36:34.108381
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert type(PyInfo.string_types) is tuple
    assert type(PyInfo.text_type) is type
    assert type(PyInfo.binary_type) is type
    assert type(PyInfo.integer_types) is tuple
    assert type(PyInfo.class_types) is tuple
    assert type(PyInfo.maxsize) is int


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:36:45.056410
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is True
    assert PyInfo.PY2 is False
    assert PyInfo.string_types == (str,)
    assert PyInfo.text_type is str
    assert PyInfo.binary_type is bytes
    assert PyInfo.integer_types == (int,)
    assert PyInfo.class_types == (type,)
    assert PyInfo.maxsize == 9223372036854775807


# -----------------------------------------------------------------------------
# Copyright 2015 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software

# Generated at 2022-06-14 06:36:53.869641
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    if PyInfo.PY2:
        assert isinstance(u'', PyInfo.text_type)
        assert isinstance('', PyInfo.binary_type)

    if PyInfo.PY3:
        assert isinstance(b'', PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)


test_PyInfo()

# Generated at 2022-06-14 06:37:00.360162
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()
    assert isinstance(info.string_types, tuple)
    assert isinstance(info.string_types, tuple)  # FIXME
    assert isinstance(info.text_type, type(""))
    assert isinstance(info.binary_type, type(""))
    assert isinstance(info.integer_types, tuple)
    assert isinstance(info.class_types, tuple)
    assert isinstance(info.maxsize, int)

# Generated at 2022-06-14 06:37:10.363802
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.PY2 != PyInfo.PY3

    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert not isinstance(b"", PyInfo.string_types)

    assert isinstance("", PyInfo.text_type)
    assert not isinstance(u"", PyInfo.text_type)
    assert not isinstance(b"", PyInfo.text_type)

    assert not isinstance("", PyInfo.binary_type)
    assert not isinstance(u"", PyInfo.binary_type)
    assert isinstance(b"", PyInfo.binary_type)

    assert isinstance(0, PyInfo.integer_types)

# Generated at 2022-06-14 06:37:15.233357
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    >>> PyInfo.PY2
    True

    >>> PyInfo.PY3
    False

    >>> PyInfo.integer_types = int, long
    Traceback (most recent call last):
    ...
    AttributeError: can't set attribute

    >>> pyinfo = PyInfo()
    Traceback (most recent call last):
    ...
    TypeError: 'PyInfo' object is not callable

    """
    pass


if __name__ == "__main__":
    # only for unit test
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:37:19.779041
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("str", PyInfo.string_types)
    assert isinstance(b"str", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)



# Generated at 2022-06-14 06:37:31.425973
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    assert PyInfo.PY2 is not True or PyInfo.PY3 is not True
    assert PyInfo.PY2 is False or PyInfo.PY3 is True
    assert PyInfo.PY2 is True or PyInfo.PY3 is False
    if PyInfo.PY2:
        assert PyInfo.maxsize < 2 ** 31
        assert PyInfo.text_type is unicode
        assert PyInfo.integer_types is (int, long)
        assert PyInfo.string_types is (basestring,)
    if PyInfo.PY3:
        assert PyInfo.maxsize > 2 ** 31
        assert PyInfo.string_types is (str,)
        assert PyInfo.text_type is str
        assert PyInfo.integer_

# Generated at 2022-06-14 06:37:41.957849
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()

    assert info.PY2 is True or info.PY2 is False
    assert info.PY3 is True or info.PY3 is False

    assert type(info.string_types) is tuple or type(info.string_types) is list
    assert type(info.string_types[0] is type)

    assert type(info.text_type) is type
    assert type(info.binary_type) is type
    assert type(info.integer_types) is tuple or type(info.integer_types) is list
    assert type(info.class_types) is tuple

    assert sys.maxsize == info.maxsize

# Generated at 2022-06-14 06:37:50.088280
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, str)
    assert isinstance(PyInfo.binary_type, str)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:37:56.249701
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not None
    assert PyInfo.PY3 is not None

    assert PyInfo.string_types is not None
    assert PyInfo.text_type is not None
    assert PyInfo.binary_type is not None
    assert PyInfo.integer_types is not None
    assert PyInfo.class_types is not None
    assert PyInfo.maxsize is not None

# Generated at 2022-06-14 06:38:00.487487
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py_info = PyInfo()
    assert (py_info.PY2 == sys.version_info[0] == 2) or (
        py_info.PY3 == sys.version_info[0] == 3
    )



# Generated at 2022-06-14 06:38:10.706484
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from six import assertRaisesRegex

    # Checking for PY2 constant
    assert isinstance(PyInfo.PY2, bool), "PY2 should be a boolean"
    assert PyInfo.PY2 != PyInfo.PY3, \
        "PY2 and PY3 booleans should be exclusive"

    # Checking for PY3 constant
    assert isinstance(PyInfo.PY3, bool), "PY3 should be a boolean"
    assert PyInfo.PY3 != PyInfo.PY2, \
        "PY3 and PY2 booleans should be exclusive"

    # Checking for string_types constant
    assert isinstance(PyInfo.string_types, tuple), \
        "string_types should be a tuple"

# Generated at 2022-06-14 06:38:15.027079
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        print("Python2")
    elif PyInfo.PY3:
        print("Python3")
    else:
        print("Python not detected")


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:32.797266
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # PY2 and PY3 are mutually exclusive
    assert PyInfo.PY2 ^ PyInfo.PY3
    # PY2 and PY3 are only either True or False
    assert (PyInfo.PY2 and not PyInfo.PY3) or (not PyInfo.PY2 and PyInfo.PY3)

    # Check the right types
    assert isinstance("some string", PyInfo.string_types)
    assert isinstance(b"some string as bytes", PyInfo.binary_type)
    assert isinstance(123456789, PyInfo.integer_types)
    assert isinstance(object, PyInfo.class_types)
    assert isinstance(object(), type(object))

    # the following types are only present in Python 2

# Generated at 2022-06-14 06:38:37.815197
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:38:49.978351
# Unit test for constructor of class PyInfo
def test_PyInfo():
    class Temp(object):
        pass

    assert isinstance('', PyInfo.string_types)
    assert isinstance(Temp(), PyInfo.string_types)

    assert isinstance(u'', PyInfo.text_type)
    assert not isinstance(Temp(), PyInfo.text_type)

    assert isinstance(b'', PyInfo.binary_type)
    assert not isinstance(Temp(), PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:38:56.562302
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)


# Generated at 2022-06-14 06:39:05.701586
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
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:39:14.363094
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

# Generated at 2022-06-14 06:39:21.248054
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(b"", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:39:34.030869
# Unit test for constructor of class PyInfo
def test_PyInfo():
    foo = PyInfo()
    assert foo.PY2 == (sys.version_info[0] == 2)
    assert foo.PY3 == (sys.version_info[0] == 3)
    assert foo.string_types == (str, str) if foo.PY3 else (basestring,)
    assert foo.text_type == str if foo.PY3 else unicode
    assert foo.binary_type == bytes if foo.PY3 else str
    assert foo.integer_types == (int,) if foo.PY3 else (int, long)
    assert foo.class_types == (type,) if foo.PY3 else (type, types.ClassType)
    assert foo.maxsize == sys.maxsize



# Generated at 2022-06-14 06:39:43.547889
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Test class attributes for PY2
    if PyInfo.PY2:
        assert PyInfo.binary_type == str
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)

    # Test class attributes for PY3
    if PyInfo.PY3:
        assert PyInfo.binary_type == bytes
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)

    # Test maxsize
    if PyInfo.PY3:
        assert PyInfo.maxsize == sys.max

# Generated at 2022-06-14 06:39:48.456057
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == True or PyInfo.PY2 == False
    assert PyInfo.PY3 == True or PyInfo.PY3 == False
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:40:01.730427
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.maxsize < sys.maxsize
    assert (1 << 31) - 1 == PyInfo.maxsize

# Generated at 2022-06-14 06:40:03.537518
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    asse

# Generated at 2022-06-14 06:40:13.706739
# Unit test for constructor of class PyInfo
def test_PyInfo():
    b2 = False
    b3 = False

    if sys.version_info[0] == 2:
        b2 = True
    if sys.version_info[0] == 3:
        b3 = True

    assert b2 != b3, "The interpreter is neither a python 2 nor a python 3"

    assert PyInfo.PY2 == b2, "The value returned by PyInfo.PY2 is not the same as the value of sys.version_info[0] for \
    python 2"

    assert PyInfo.PY3 == b3, "The value returned by PyInfo.PY3 is not the same as the value of sys.version_info[0] for \
    python 3"


# Generated at 2022-06-14 06:40:27.511480
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py_info = PyInfo()
    assert py_info.PY2 is True or py_info.PY3 is True
    assert type(py_info.string_types) == tuple  # this is how the idioms work
    assert type(py_info.text_type) == type  # this is how the idioms work
    assert type(py_info.binary_type) == type  # this is how the idioms work
    assert type(py_info.integer_types) == tuple  # this is how the idioms work
    assert type(py_info.class_types) == tuple  # this is how the idioms work


py_info = PyInfo()
TEXT_TYPE = py_info.text_type
BINARY_TYPE = py_info.binary_type
UNICODE_TYPE = py_info.text_type

# Generated at 2022-06-14 06:40:36.049038
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)
    else:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)


if __name__ == "__main__":
    test_PyInfo()
    print("Everything passed")

# Generated at 2022-06-14 06:40:47.178444
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert not isinstance(b'', PyInfo.string_types)
    assert isinstance(b'', PyInfo.binary_type)
    assert not isinstance('', PyInfo.binary_type)
    assert isinstance('', PyInfo.text_type)
    assert not isinstance(b'', PyInfo.text_type)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:40:49.071307
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.string_types[0] == 'abc'



# Generated at 2022-06-14 06:41:00.411429
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert type(u"abc" + PyInfo.text_type("abc")) == PyInfo.text_type
        assert type("abc" + PyInfo.binary_type("abc")) == PyInfo.binary_type
    else:  # PyInfo.PY3
        assert type(u"abc" + PyInfo.text_type("abc")) == PyInfo.text_type
        assert type("abc" + PyInfo.binary_type("abc")) == PyInfo.binary_type
        assert len(PyInfo.string_types) == 1
        assert len(PyInfo.integer_types) == 1
        assert len(PyInfo.class_types) == 1


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:41:03.871692
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyInfo = PyInfo()
    assert pyInfo.PY2
    assert not pyInfo.PY3

# Generated at 2022-06-14 06:41:15.757407
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        ok_(isinstance("", PyInfo.string_types))
        ok_(isinstance(u"", PyInfo.string_types))
        ok_(not isinstance(b"", PyInfo.string_types))

        ok_(not isinstance("", PyInfo.text_type))
        ok_(isinstance(u"", PyInfo.text_type))
        ok_(not isinstance(b"", PyInfo.text_type))

        ok_(isinstance(b"", PyInfo.binary_type))
        ok_(not isinstance("", PyInfo.binary_type))
        ok_(not isinstance(u"", PyInfo.binary_type))

        ok_(isinstance(1, PyInfo.integer_types))

# Generated at 2022-06-14 06:41:43.884206
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert isinstance(b'', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)

    if PyInfo.PY2:
        assert isinstance('', PyInfo.text_type)
        assert isinstance(u'', PyInfo.text_type)
        assert not isinstance(b'', PyInfo.text_type)
    elif PyInfo.PY3:
        assert isinstance(''.encode(), PyInfo.binary_type)

# Generated at 2022-06-14 06:41:51.964401
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


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:42:00.973944
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert type("") == PyInfo.string_types[0]
    assert type(u"") == PyInfo.text_type
    assert type("") == PyInfo.binary_type
    assert type(0) in PyInfo.integer_types

# Generated at 2022-06-14 06:42:07.781853
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance('abc', PyInfo.string_types)
    assert isinstance(u'abc', PyInfo.text_type)
    assert isinstance(b'abc', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(type, PyInfo.class_types)
    assert isinstance(PyInfo, PyInfo.class_types)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:42:21.411482
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """Test the PyInfo class."""
    pi = PyInfo()
    assert pi.PY2 or pi.PY3
    if pi.PY3:
        assert pi.maxsize == sys.maxsize
        assert len(pi.string_types) == 1
        assert len(pi.integer_types) == 1
        assert len(pi.class_types) == 1
        assert pi.text_type is str
        assert pi.binary_type is bytes
    else:
        assert pi.maxsize == pi.maxsize
        assert len(pi.string_types) == 2
        assert len(pi.integer_types) == 2
        assert len(pi.class_types) == 2
        assert pi.text_type is unicode
        assert pi.binary_type is str

# Generated at 2022-06-14 06:42:22.949283
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pass


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:42:27.339751
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert issubclass(PyInfo.text_type, PyInfo.string_types)
    assert issubclass(PyInfo.binary_type, PyInfo.string_types)
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert not isinstance("", PyInfo.binary_type)

# Generated at 2022-06-14 06:42:37.532981
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.maxsize == (1 << 63) - 1
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)


if __name__ == '__main__':
    sys.exit(pytest.main(["-x", __file__]))

# Generated at 2022-06-14 06:42:46.225578
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyi = PyInfo()
    assert pyi.PY2 == (sys.version_info[0] == 2)
    assert pyi.PY3 == (sys.version_info[0] == 3)
    assert pyi.string_types == (str, basestring) if sys.version_info[0] == 2 else (str,)
    assert pyi.text_type == str if sys.version_info[0] == 3 else unicode
    assert pyi.binary_type == bytes if sys.version_info[0] == 3 else str
    assert pyi.integer_types == (int, long) if sys.version_info[0] == 2 else (int,)
    assert pyi.class_types == (type,) if sys.version_info[0] == 3 else (type, types.ClassType)
    assert py

# Generated at 2022-06-14 06:42:49.302494
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 or pyinfo.PY3
    assert pyinfo.maxsize > 1000000



# Generated at 2022-06-14 06:43:36.058498
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py_info = PyInfo()
    assert py_info.PY2 is not py_info.PY3
    if py_info.PY2:
        assert isinstance(b'', py_info.binary_type)
        assert isinstance('', py_info.text_type)
    else:
        assert isinstance(b'', py_info.binary_type)
        assert isinstance('', py_info.text_type)

# Generated at 2022-06-14 06:43:40.109440
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types

# Generated at 2022-06-14 06:43:46.785445
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True
    assert PyInfo.PY3 is False

    assert PyInfo.maxsize == 2147483647

    assert PyInfo.string_types == (basestring,)
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str

# Generated at 2022-06-14 06:43:53.585852
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    if PyInfo.PY2:
        assert isinstance(PyInfo.maxsize, (int, long))
    else:
        assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:44:06.048364
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert not isinstance(1, PyInfo.string_types)

    assert isinstance("", PyInfo.text_type)
    assert not isinstance(u"", PyInfo.text_type)
    assert not isinstance(1, PyInfo.text_type)

    assert isinstance(b"", PyInfo.binary_type)
    assert not isinstance(u"", PyInfo.binary_type)
    assert not isinstance(1, PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:44:09.958150
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print(PyInfo.PY3)
    print(PyInfo.PY2)
    print(PyInfo.string_types)
    print(PyInfo.text_type)
    print(PyInfo.binary_type)
    print(PyInfo.integer_types)
    print(PyInfo.class_types)
    print(PyInfo.maxsize)



# Generated at 2022-06-14 06:44:20.061617
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(u"", PyInfo.text_type)
    assert isinstance("", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:44:31.306664
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print("Test PyInfo")

    if PyInfo.PY2:
        assert isinstance("test_PyInfo", PyInfo.string_types)
        assert isinstance(u"test_PyInfo", PyInfo.string_types)
        assert isinstance("test_PyInfo".decode("UTF-8"), PyInfo.string_types)
        assert not isinstance("test_PyInfo", PyInfo.binary_type)

        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:44:39.159855
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert isinstance(' ', PyInfo.string_types)
    assert not isinstance(b' ', PyInfo.string_types)
    assert isinstance(b' ', PyInfo.binary_type)
    assert not isinstance(' ', PyInfo.binary_type)
    assert isinstance(123, PyInfo.integer_types)
    assert not isinstance(123.123, PyInfo.integer_types)
    assert isinstance(type(None), PyInfo.class_types)



# Generated at 2022-06-14 06:44:51.098287
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY2:
        assert isinstance('', PyInfo.string_types)
        assert isinstance(u'', PyInfo.text_type)
        assert PyInfo.binary_type == str
        assert isinstance(1, PyInfo.integer_types)
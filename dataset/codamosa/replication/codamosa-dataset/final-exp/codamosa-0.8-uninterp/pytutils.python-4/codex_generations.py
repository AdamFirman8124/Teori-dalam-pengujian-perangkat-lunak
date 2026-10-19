

# Generated at 2022-06-14 06:35:48.119424
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not None and PyInfo.PY2 is not None
    for i in range(0, 2):
        assert PyInfo.integer_types[i] is not None and isinstance(PyInfo.integer_types[i], type)
        assert PyInfo.class_types[i] is not None and isinstance(PyInfo.class_types[i], type)
        assert PyInfo.string_types[i] is not None and isinstance(PyInfo.string_types[i], type)

    assert isinstance(PyInfo.maxsize, int)
    assert PyInfo.binary_type is not None and isinstance(PyInfo.binary_type, type)
    assert PyInfo.binary_type is not None and isinstance(PyInfo.binary_type, type)

# Generated at 2022-06-14 06:35:56.097152
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (
        sys.version_info[0] == 2
    ), "PyInfo is not equal to sys.version_info[0] == 2"
    assert PyInfo.PY3 == (
        sys.version_info[0] == 3
    ), "PyInfo is not equal to sys.version_info[0] == 2"


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:36:01.569632
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # For coverage
    assert PyInfo.PY2 == (2 == sys.version_info[0])
    assert PyInfo.PY3 == (3 == sys.version_info[0])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    test_PyInfo()

# Generated at 2022-06-14 06:36:07.069765
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance("", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:36:12.176071
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert not PyInfo.PY2
    assert PyInfo.PY3
    assert isinstance('a', PyInfo.string_types)
    assert isinstance(u'a', PyInfo.string_types)
    assert isinstance(b'a', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:36:22.122974
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys

    assert PyInfo.PY2 != PyInfo.PY3

    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)

    assert isinstance(None, PyInfo.text_type)

    assert isinstance(b'', PyInfo.binary_type)

    assert isinstance(0, PyInfo.integer_types)

# Generated at 2022-06-14 06:36:35.577374
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    assert isinstance(PyInfo.string_types, tuple)
    assert all(isinstance(t, type) for t in PyInfo.string_types)

    assert isinstance(PyInfo.text_type, type)

    assert isinstance(PyInfo.binary_type, type)

    assert isinstance(PyInfo.integer_types, tuple)
    assert all(isinstance(t, type) for t in PyInfo.integer_types)

    assert isinstance(PyInfo.class_types, tuple)
    assert all(isinstance(t, type) for t in PyInfo.class_types)

    assert isinstance(PyInfo.maxsize, int)



# Generated at 2022-06-14 06:36:45.625803
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def check_types(info):
        assert issubclass(info.string_types[0], (basestring, type(None)))
        assert issubclass(info.binary_type, str)
        assert issubclass(info.integer_types[0], (int, long))
        assert issubclass(info.class_types[0], (type, types.ClassType))

    PyInfo_copy = type("PyInfo_copy", (object,), dict(PyInfo.__dict__))
    check_types(PyInfo_copy)

    # Check that type of PyInfo_copy is the same as the type of PyInfo
    # in Python3
    if PyInfo.PY3:
        assert PyInfo_copy == type(PyInfo)
    else:
        assert PyInfo_copy == types.ClassType



# Generated at 2022-06-14 06:36:56.390873
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('a', PyInfo.string_types)
        assert isinstance(u'a', PyInfo.string_types)
        assert not isinstance(b'a', PyInfo.string_types)
        assert not isinstance(0, PyInfo.string_types)

        assert not isinstance('a', PyInfo.text_type)
        assert isinstance(u'a', PyInfo.text_type)
        assert not isinstance(b'a', PyInfo.string_types)

        assert not isinstance('a', PyInfo.binary_type)
        assert not isinstance(u'a', PyInfo.binary_type)
        assert isinstance(b'a', PyInfo.binary_type)

        assert not isinstance('a', PyInfo.integer_types)
        assert not isinstance

# Generated at 2022-06-14 06:37:06.937871
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys
    import types
    i = PyInfo()
    assert (i.PY2 and sys.version_info[0] == 2) or (i.PY3 and sys.version_info[0] == 3)
    if i.PY3:
        assert i.string_types == (str,)
        assert i.text_type == str
        assert i.binary_type == bytes
        assert i.integer_types == (int,)
        assert i.class_types == (type,)
    else:
        assert i.string_types == (basestring,)
        assert i.text_type == unicode
        assert i.binary_type == str
        assert i.integer_types == (int, long)
        assert i.class_types == (type, types.ClassType)

# Generated at 2022-06-14 06:37:14.184740
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert(PyInfo.PY2 or PyInfo.PY3)
    assert(isinstance(PyInfo.string_types, tuple))
    assert(isinstance(PyInfo.text_type, type))
    assert(isinstance(PyInfo.binary_type, type))
    assert(isinstance(PyInfo.integer_types, tuple))
    assert(isinstance(PyInfo.class_types, tuple))

# Generated at 2022-06-14 06:37:19.908052
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert (PyInfo.PY2 or PyInfo.PY3)

    s = "hello"
    assert isinstance(s, PyInfo.string_types)

    assert isinstance(u"hello", PyInfo.text_type)

    assert isinstance(b"hello", PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)

    assert isinstance(int, PyInfo.class_types)

# Generated at 2022-06-14 06:37:29.978767
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert isinstance(PyInfo.integer_types, tuple)
    assert PyInfo.integer_types == (int, long)
    assert isinstance(PyInfo.class_types, tuple)
    assert PyInfo.class_types == (type, types.ClassType)
    assert isinstance(PyInfo.maxsize, int)
    assert PyInfo.maxsize == 2147483647


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:37:41.904278
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3

    if PyInfo.PY3:
        assert isinstance("", PyInfo.string_types)
        assert isinstance("", PyInfo.text_type)
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(Exception, PyInfo.class_types)
    else:
        assert isinstance("", PyInfo.string_types)
        assert isinstance(u"", PyInfo.text_type)
        assert isinstance("", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(Exception, PyInfo.class_types)
    assert type(PyInfo.maxsize) is int

# Generated at 2022-06-14 06:37:48.731128
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.maxsize > 0
    assert type(PyInfo.maxsize) is int
    assert len(PyInfo.string_types) >= 1
    assert len(PyInfo.integer_types) >= 1
    assert type(PyInfo.text_type()) is PyInfo.text_type
    assert type(PyInfo.binary_type()) is PyInfo.binary_type



# Generated at 2022-06-14 06:37:51.909505
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    assert PyInfo.PY2 is False or PyInfo.PY3 is False

# Generated at 2022-06-14 06:37:59.859420
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:38:02.474719
# Unit test for constructor of class PyInfo
def test_PyInfo():
    try:
        p = PyInfo()
    except NameError:
        pass
    except Exception as e:
        raise e


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:12.399854
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

# Generated at 2022-06-14 06:38:15.271292
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert len(pyinfo.string_types) == 1
    assert pyinfo.maxsize
    assert pyinfo.PY3 is not None



# Generated at 2022-06-14 06:38:33.312779
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == True or PyInfo.PY2 == False
    assert PyInfo.PY3 == True or PyInfo.PY3 == False
    assert isinstance(PyInfo.string_types, (tuple, list))
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, (tuple, list))
    assert isinstance(PyInfo.class_types, (tuple, list))

    # maxsize is a long in C code. But we don't have a long type in py2, so
    # we convert it to an int manually.
    maxsize = int(PyInfo.maxsize)
    assert isinstance(maxsize, int)
    assert maxsize > 0



# Generated at 2022-06-14 06:38:36.955718
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3


print(PyInfo.text_type)
print(PyInfo.string_types)
print(PyInfo.binary_type)
print(PyInfo.integer_types)
print(PyInfo.class_types)
print(PyInfo.maxsize)

# Generated at 2022-06-14 06:38:46.328334
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)

    assert isinstance(PyInfo.maxsize, (int, long))



# Generated at 2022-06-14 06:38:52.852784
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.maxsize
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance("", PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)
    assert isinstance(type, PyInfo.class_types)



# Generated at 2022-06-14 06:39:04.488940
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if not PyInfo.PY2:
        assert isinstance(u"", PyInfo.string_types)
        assert not isinstance(b"", PyInfo.string_types)
    else:
        assert isinstance(u"", PyInfo.string_types)
        assert isinstance(b"", PyInfo.string_types)

    assert isinstance(u"", PyInfo.text_type)
    assert not isinstance(b"", PyInfo.text_type)

    assert not isinstance(u"", PyInfo.binary_type)
    assert isinstance(b"", PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:39:18.138622
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import re

    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    if PyInfo.PY3:
        assert isinstance(b"", PyInfo.string_types)

    assert isinstance(u"", PyInfo.text_type)
    assert not isinstance("", PyInfo.text_type)
    if PyInfo.PY3:
        assert not isinstance(b"", PyInfo.text_type)

    assert isinstance(b"", PyInfo.binary_type)
    assert not isinstance("", PyInfo.binary_type)

# Generated at 2022-06-14 06:39:26.780153
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3, "Python version 2 or 3 required!"


# =============================================================================


# py_compat.moved_attributes
# ==============================================================================
# Attributes that have moved between Python 2 and Python 3
# - Backported from Django
# - Slightly modified
#
# Django version:
# - https://github.com/django/django/blob/master/django/utils/py3.py
# - https://github.com/django/django/blob/master/LICENSE
#
# Copyright (c) Django Software Foundation and individual contributors.
# Copyright (c) 2016-2017 Benjamin Althues <benjamin@babab.nl>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are

# Generated at 2022-06-14 06:39:39.742337
# Unit test for constructor of class PyInfo
def test_PyInfo():
    with pytest.raises(AttributeError):
        PyInfo.PY3

    with pytest.raises(AttributeError):
        PyInfo.PY2

    with pytest.raises(AttributeError):
        PyInfo.string_types

    with pytest.raises(AttributeError):
        PyInfo.text_type

    with pytest.raises(AttributeError):
        PyInfo.binary_type

    with pytest.raises(AttributeError):
        PyInfo.integer_types

    with pytest.raises(AttributeError):
        PyInfo.class_types

    with pytest.raises(AttributeError):
        PyInfo.maxsize


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)

# Generated at 2022-06-14 06:39:51.386396
# Unit test for constructor of class PyInfo
def test_PyInfo():
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


# test_PyInfo()


# Generated at 2022-06-14 06:39:55.081038
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2
    assert not pyinfo.PY3
    assert pyinfo.string_types == (basestring,)
    assert pyinfo.text_type == unicode
    assert pyinfo.binary_type == str
    assert pyinfo.integer_types == (int, long)
    assert pyinfo.class_types == (type, types.ClassType)


# Generated at 2022-06-14 06:40:16.266211
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from pyclbr import readmodule
    from .textwrap import dedent
    from .tokenize import generate_tokens, untokenize
    from .unittest import TestCase

    class X(TestCase):
        pass

    mod = "pyclbr_test"
    key = "ClassInfo(%r, %r, %r)" % (mod, "MyClass", (1,))
    myclass = readmodule(mod)[key]
    assert isinstance(myclass, PyInfo.class_types)

    def make_py2_source(code):
        code = dedent(code)
        tokens = generate_tokens(StringIO(code).readline)
        tokens = [token for token in tokens if token[0] != tokenize.NL]
        return untokenize(tokens).strip()


# Generated at 2022-06-14 06:40:29.201138
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (not PyInfo.PY3)
    assert PyInfo.maxsize <= sys.maxsize
    assert PyInfo.maxsize >= 0x7fffffff
    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert isinstance(u'', PyInfo.text_type)
    assert isinstance('', PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)

# Generated at 2022-06-14 06:40:41.533131
# Unit test for constructor of class PyInfo
def test_PyInfo():

    def check(attr, value):
        assert getattr(PyInfo, attr) == value
        assert getattr(pyinfo, attr) == value
        if not attr.startswith("__"):
            assert hasattr(pyinfo, attr)
            assert not hasattr(pyinfo, "_" + attr)

    check("PY2", sys.version_info[0] == 2)
    check("PY3", sys.version_info[0] == 3)

    if PyInfo.PY2:
        check("string_types", (basestring,))
        check("text_type", unicode)
        check("binary_type", str)
        check("integer_types", (int, long))
        check("class_types", (type, types.ClassType))


# Generated at 2022-06-14 06:40:46.455700
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3
    assert PyInfo.string_types == (str,)
    assert PyInfo.text_type == str
    assert PyInfo.binary_type == bytes
    assert PyInfo.integer_types == (int,)
    assert PyInfo.class_types == (type,)
    assert PyInfo.maxsize == sys.maxsize



# Generated at 2022-06-14 06:40:58.537161
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.string_types[0], type)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.integer_types[0], type)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.class_types[0], type)
    assert isinstance(PyInfo.maxsize, int)  # 1 << 31
    assert PyInfo.maxsize < (1 << 32)
    assert PyInfo.PY2 != Py

# Generated at 2022-06-14 06:41:11.529287
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert isinstance("foo", PyInfo.string_types)
    if PyInfo.PY2:
        assert isinstance(u"foo", PyInfo.string_types)

    assert isinstance("foo", PyInfo.text_type)
    assert not isinstance(b"foo", PyInfo.text_type)

    assert isinstance(b"foo", PyInfo.binary_type)
    assert not isinstance("foo", PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert not isinstance(1.1, PyInfo.integer_types)

    assert issubclass(bool, PyInfo.integer_types)
    assert issubclass(float, PyInfo.integer_types)

# Generated at 2022-06-14 06:41:19.360358
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    assert isinstance(PyInfo.maxsize, int)

    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)

# Generated at 2022-06-14 06:41:23.184206
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3


# Convert binary bytes to unicode string in Py3 or return the passed in string in Py2

# Generated at 2022-06-14 06:41:31.953385
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys

    #print(sys.version_info)
    #print(PyInfo.PY2)
    #print(PyInfo.PY3)
    #print(PyInfo.string_types)
    #print(PyInfo.text_type)
    #print(PyInfo.binary_type)
    #print(PyInfo.integer_types)
    #print(PyInfo.class_types)
    #print(PyInfo.maxsize)


"""
if __name__ == '__main__':
    import doctest
    doctest.testmod()
"""

if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:41:39.955866
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    # Check type and length
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:42:02.531361
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    >>> PyInfo.maxsize
    sys.maxsize
    >>> PyInfo.string_types
    basestring
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:42:15.259396
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def test_PyInfo_check():
        assert True if PyInfo.PY2 else False

    test_PyInfo_check()

    def test_PyInfo_string_types():
        assert PyInfo.string_types == (
            str,
        ) if PyInfo.PY3 else (basestring,)

    test_PyInfo_string_types()

    def test_PyInfo_text_type():
        assert PyInfo.text_type == str if PyInfo.PY3 else unicode

    test_PyInfo_text_type()

    def test_PyInfo_binary_type():
        assert PyInfo.binary_type == bytes if PyInfo.PY3 else str

    test_PyInfo_binary_type()


# Generated at 2022-06-14 06:42:24.344034
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.maxsize, int)
    assert isinstance(PyInfo.class_types, tuple)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:42:26.153905
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.maxsize > 0


# Usage

# Generated at 2022-06-14 06:42:40.025694
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.PY2 ^ PyInfo.PY3

    assert isinstance("str", PyInfo.string_types)
    assert not isinstance("str", PyInfo.binary_type)
    assert isinstance("str", PyInfo.text_type)
    assert not isinstance("str", PyInfo.integer_types)

    assert isinstance(u"unicode", PyInfo.string_types)
    assert not isinstance(u"unicode", PyInfo.binary_type)
    assert isinstance(u"unicode", PyInfo.text_type)
    assert not isinstance(u"unicode", PyInfo.integer_types)

    assert not isinstance(b"bytes", PyInfo.string_types)

# Generated at 2022-06-14 06:42:45.625945
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('abc', PyInfo.string_types)
    assert isinstance(b'abc', PyInfo.binary_type)
    assert isinstance(99, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)

# Generated at 2022-06-14 06:42:51.184107
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    if PyInfo.PY2:
        assert PyInfo.PY3 == False
    else:
        assert PyInfo.PY3 == True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:43:02.188708
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 and not PyInfo.PY3
    assert isinstance("hello", PyInfo.string_types)
    assert isinstance(u"hello", PyInfo.string_types)
    assert not isinstance(b"hello", PyInfo.string_types)
    assert isinstance(b"hello", PyInfo.binary_type)
    assert isinstance(2, PyInfo.integer_types)

# Generated at 2022-06-14 06:43:15.702736
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print("\n### Unit test for constructor of class PyInfo")

    def test_symbols():
        print("string_types = type(''), string_types[0] = ", type(""), PyInfo.string_types[0])
        print("text_type = type(u''), text_type = ", type(u""), PyInfo.text_type)
        print("binary_type = type(b''), binary_type = ", type(b""), PyInfo.binary_type)
        print("integer_types = type(0), integer_types[0] = ", type(0), PyInfo.integer_types[0])
        print("class_types = type(Object), class_types[0] = ", type(object), PyInfo.class_types[0])

    test_symbols()
    print()


# Unit test

# Generated at 2022-06-14 06:43:25.835150
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is sys.version_info[0] == 2
    assert PyInfo.PY3 is sys.version_info[0] == 3
    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)
        assert PyInfo.maxsize == sys.maxsize
    else:  # PY2
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)

# Generated at 2022-06-14 06:44:11.613752
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()
    if pi.PY2:
        assert isinstance('abc', pi.string_types)
        assert isinstance(u'abc', pi.text_type)
        assert isinstance(b'abc', pi.binary_type)
        assert 2**32 > pi.maxsize >= 2**31 - 1

    if pi.PY3:
        assert isinstance('abc', pi.string_types)
        assert isinstance('abc', pi.text_type)
        assert isinstance(b'abc', pi.binary_type)
        assert 2**64 > pi.maxsize >= 2**63 - 1


# A global object
pyinfo = PyInfo()



# Generated at 2022-06-14 06:44:15.115383
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo is not None


# Check if both PY2 and PY3 raise NotImplementedError

# Generated at 2022-06-14 06:44:25.418762
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)

    # recheck the value of variable maxsize
    if (
        PyInfo.maxsize == sys.maxsize
        or sys.platform.startswith("java")
        and PyInfo.maxsize == 2 ** 31 - 1
    ):
        assert PyInfo.maxsize == sys.maxsize
    elif PyInfo.maxsize == 2 ** 31 - 1:
        assert sys.maxsize == 2 ** 63 - 1



# Generated at 2022-06-14 06:44:33.265647
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types
    assert PyInfo.maxsize


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:44:34.330747
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is not PyInfo.PY2



# Generated at 2022-06-14 06:44:38.649949
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True
    assert PyInfo.PY3 is False
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type is unicode
    assert PyInfo.binary_type is str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)


# if __name__ == '__main__':
#     test_PyInfo()

# Generated at 2022-06-14 06:44:46.263923
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert type(PyInfo.string_types) is tuple
    assert type(PyInfo.text_type) is type
    assert type(PyInfo.binary_type) is type
    assert type(PyInfo.integer_types) is tuple
    assert type(PyInfo.class_types) is tuple
    assert type(PyInfo.maxsize) is int



# Generated at 2022-06-14 06:44:51.300632
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3, "Should be either PY2 or PY3, but got {}".format(
        sys.version_info[0]
    )

# Generated at 2022-06-14 06:44:56.988111
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types
    assert PyInfo.maxsize

# Generated at 2022-06-14 06:45:05.558345
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
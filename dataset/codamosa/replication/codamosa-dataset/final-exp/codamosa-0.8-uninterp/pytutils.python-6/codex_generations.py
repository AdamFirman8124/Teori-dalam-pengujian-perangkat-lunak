

# Generated at 2022-06-14 06:35:49.429748
# Unit test for constructor of class PyInfo
def test_PyInfo():
    u"""TODO."""
    assert PyInfo.PY2 is True or PyInfo.PY2 is False
    assert PyInfo.PY3 is True or PyInfo.PY3 is False
    assert PyInfo.PY2 is not PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple), PyInfo.string_types
    assert isinstance(PyInfo.integer_types, tuple), PyInfo.integer_types
    assert isinstance(PyInfo.class_types, tuple), PyInfo.class_types
    assert isinstance(PyInfo.maxsize, long if PyInfo.PY2 else int), PyInfo.maxsize
    assert isinstance(PyInfo.maxsize, long) or isinstance(PyInfo.maxsize, int)



# Generated at 2022-06-14 06:35:55.776483
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3

    assert PyInfo.string_types[0] == basestring
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.maxsize == 9223372036854775807



# Generated at 2022-06-14 06:36:00.741854
# Unit test for constructor of class PyInfo
def test_PyInfo():
    for k, v in PyInfo.__dict__.items():
        if not k.startswith("_"):
            print(k, v)


__all__ = ['PyInfo']

if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:36:10.365026
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3, "Invalid Python version"
    assert not (PyInfo.PY2 and PyInfo.PY3), "Both Python 2 and Python 3"
    assert PyInfo.text_type is not str and PyInfo.text_type is not unicode
    assert isinstance(PyInfo.text_type(), str)
    assert PyInfo.binary_type is not str and PyInfo.binary_type is not bytes
    assert isinstance(PyInfo.binary_type(), bytes)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.class_types)
    assert not isinstance(1, PyInfo.string_types)

# Generated at 2022-06-14 06:36:22.893246
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert PyInfo.string_types == (str, )
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int, )
        assert PyInfo.class_types == (type, )
        assert PyInfo.maxsize == sys.maxsize
    else:  # PyInfo.PY2
        assert PyInfo.string_types == (basestring, )
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)

# Generated at 2022-06-14 06:36:29.194223
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types
    assert PyInfo.maxsize


# Send a message to stderr and exit the program.

# Generated at 2022-06-14 06:36:40.302641
# Unit test for constructor of class PyInfo
def test_PyInfo():
    global PY2
    global PY3
    global string_types
    global text_type
    global binary_type
    global integer_types
    global class_types
    global maxsize
    PY2 = sys.version_info[0] == 2
    PY3 = sys.version_info[0] == 3

    if PY3:
        string_types = str,
        text_type = str
        binary_type = bytes
        integer_types = int,
        class_types = type,

        maxsize = sys.maxsize
    else:  # PY2
        string_types = basestring,
        text_type = unicode
        binary_type = str
        integer_types = (int, long)
        class_types = (type, types.ClassType)


# Generated at 2022-06-14 06:36:44.353938
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo().PY3, bool)
    assert isinstance(PyInfo().PY2, bool)



# Generated at 2022-06-14 06:36:47.671683
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert PyInfo.maxsize > 0


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:36:57.144554
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # check that string_types is a tuple of length 1
    assert isinstance(PyInfo.string_types, tuple)
    assert len(PyInfo.string_types) == 1

    assert isinstance(PyInfo.string_types[0], type)

    # check that text_type is a string
    assert isinstance(PyInfo.text_type, type)
    assert issubclass(PyInfo.text_type, str) or issubclass(PyInfo.text_type, unicode)

    # check that binary_type is a string
    assert isinstance(PyInfo.binary_type, type)
    assert issubclass(PyInfo.binary_type, str) or issubclass(PyInfo.binary_type, bytes)

    # check that binary_type is a tuple of length 2

# Generated at 2022-06-14 06:37:12.771871
# Unit test for constructor of class PyInfo
def test_PyInfo():

    if not (PyInfo.PY2 or PyInfo.PY3):
        raise Exception("invalid python version")

    if not PyInfo.string_types == (basestring,) and PyInfo.string_types == (str,):
        raise Exception("invalid string types")

    if not PyInfo.text_type == unicode and PyInfo.text_type == str:
        raise Exception("invalid text type")

    if not PyInfo.binary_type == str and PyInfo.binary_type == bytes:
        raise Exception("invalid binary type")

    if not PyInfo.maxsize == int((1 << 31) - 1) and PyInfo.maxsize == int((1 << 63) - 1):
        raise Exception("invalid maxsize")


# Generated at 2022-06-14 06:37:20.487279
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import unittest

    class Test(unittest.TestCase):
        def test_py2(self):
            self.assertEqual(PyInfo.PY2, sys.version_info[0] == 2)

        def test_py3(self):
            self.assertEqual(PyInfo.PY3, sys.version_info[0] == 2)

    unittest.main()

if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:37:29.345835
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p = PyInfo()
    print('PY2: ', p.PY2)
    print('PY3: ', p.PY3)
    print('string_types: ', p.string_types)
    print('text_type: ', p.text_type)
    print('binary_type: ', p.binary_type)
    print('integer_types: ', p.integer_types)
    print('class_types: ', p.class_types)
    print('maxsize: ', p.maxsize)
    print('version_info: ', sys.version_info)


# Unit test

# Generated at 2022-06-14 06:37:36.874180
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import platform
    import sys

    py_info = PyInfo()

    if "java" in platform.python_implementation().lower():
        assert py_info.maxsize == 2 ** 31 - 1
    elif sys.maxsize == 2 ** 32 - 1:
        assert py_info.maxsize == 2 ** 31 - 1
    elif sys.maxsize == 2 ** 63 - 1:
        assert py_info.maxsize == 2 ** 63 - 1
    else:
        raise Exception("Failed to test constructor of class PyInfo.")

# Generated at 2022-06-14 06:37:41.957597
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import unittest
    import sys

    class TestPyInfo(unittest.TestCase):
        def test_PyInfo(self):
            self.assertTrue(PyInfo.PY2)
            self.assertFalse(PyInfo.PY3)

    unittest.main()
    sys.exit()



# Generated at 2022-06-14 06:37:54.216666
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys
    import types
    import jupyter_client.manager

    # Note: PyInfo is a singleton class; it will raise ValueError
    # if we try to instantiate it again.
    PyInfo()
    PyInfo()

    if sys.version_info[0] == 3:
        assert jupyter_client.manager.PyInfo.PY2 == False
        assert jupyter_client.manager.PyInfo.PY3 == True

        assert jupyter_client.manager.PyInfo.integer_types == (int,)
        assert jupyter_client.manager.PyInfo.string_types == (str, )
        assert jupyter_client.manager.PyInfo.class_types == (type, )

# Generated at 2022-06-14 06:38:01.276440
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("aa", PyInfo.string_types)
    assert isinstance(u"aa", PyInfo.string_types)
    assert isinstance(b"aa", PyInfo.binary_type)
    assert isinstance(10, PyInfo.integer_types)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:38:05.650948
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print('Python version  :', sys.version.split()[0])
    print('Maximum integer :', PyInfo.maxsize)
    print('Test Successful :', PyInfo.PY2)


# call the unittest
if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:38:13.989115
# Unit test for constructor of class PyInfo
def test_PyInfo():
    
    # Verify that the constructor raises an exception on invalid parameters
    try:
        PyInfo.__init__(1)
    except:
        try:
            PyInfo.__init__('1')
        except:
            try:
                PyInfo.__init__(False)
            except:
                pass
            else:
                assert False, "Unsupported type of parameter"
        else:
            assert False, "Unsupported type of parameter"
    else:
        assert False, "Unsupported type of parameter"

    # Verify that the constructor raises an exception on invalid parameters
    try:
        PyInfo.__init__(None)
    except:
        pass
    else:
        assert False, "Unsupported type of parameter"

    # Verify that the constructor does not raise any exception

# Generated at 2022-06-14 06:38:24.650756
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert type("s") == types.StringType
        assert type("s") != types.InstanceType
        assert type("s") != types.ClassType

        assert type("s") == types.StringType
        assert type("s") != types.InstanceType
        assert type("s") != types.ClassType
    else:
        # In python3, str and InstanceType are different types
        assert type("s") != types.InstanceType

        # but function code object and InstanceType are the same type
        assert type(test_PyInfo.__code__) == types.InstanceType


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:30.975924
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3



# Generated at 2022-06-14 06:38:41.834395
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from sys import maxsize

    assert PyInfo.maxsize == maxsize
    assert PyInfo.PY2 != PyInfo.PY3
    assert isinstance("Hello", PyInfo.string_types) is True
    assert isinstance(b"Hello", PyInfo.string_types) is False
    assert isinstance("Hello", PyInfo.binary_type) is False
    assert isinstance("Hello", PyInfo.text_type) is True
    assert isinstance("Hello", PyInfo.binary_type) is False
    assert isinstance(1, PyInfo.integer_types) is True
    assert isinstance(lambda: 1, PyInfo.class_types) is True



# Generated at 2022-06-14 06:38:46.577653
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p = PyInfo()

    assert (p.PY2 == p.PY3 == False)
    assert p.maxsize == (1 << 63) - 1


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:39:00.258218
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    assert PyInfo.PY2 is False or PyInfo.PY3 is False

    if PyInfo.PY3:
        assert isinstance('unicode', PyInfo.string_types)
        assert isinstance(b'bytes', PyInfo.text_type)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert isinstance(0, PyInfo.integer_types)
        assert isinstance(0, PyInfo.class_types)
        assert isinstance(int, PyInfo.class_types)
        assert isinstance(types, PyInfo.class_types)
    else:
        assert isinstance('unicode', PyInfo.string_types)

# Generated at 2022-06-14 06:39:08.847965
# Unit test for constructor of class PyInfo

# Generated at 2022-06-14 06:39:17.720340
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('123', PyInfo.string_types)
        assert isinstance(123, PyInfo.integer_types)
        assert isinstance(u'123', PyInfo.text_type)
    assert isinstance(123, PyInfo.integer_types)
    assert isinstance(u'123', PyInfo.text_type)
    assert isinstance(b'123', PyInfo.binary_type)
    assert isinstance(PyInfo, PyInfo.class_types)


if __name__ == "__main__":
    PyInfo()
    test_PyInfo()

# Generated at 2022-06-14 06:39:24.601381
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("test", PyInfo.string_types)
    assert isinstance(u"test", PyInfo.string_types)
    assert isinstance("test", PyInfo.text_type)
    assert isinstance(b"test", PyInfo.binary_type)
    assert isinstance(1.0, PyInfo.integer_types)
    assert isinstance(object, PyInfo.class_types)
    assert isinstance(PyInfo, PyInfo.class_types)


# Class for testing class PyInfo

# Generated at 2022-06-14 06:39:34.961333
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert isinstance("", PyInfo.string_types)
        assert isinstance(str(), PyInfo.string_types)  # noqa
        assert isinstance(b"", PyInfo.binary_type)

        assert isinstance(True, PyInfo.integer_types)
        assert isinstance(1, PyInfo.integer_types)

        assert isinstance(int, PyInfo.class_types)
        assert not isinstance(1, PyInfo.class_types)

        assert isinstance(sys.maxsize, PyInfo.integer_types)
        assert PyInfo.maxsize == sys.maxsize

        # noins

# Generated at 2022-06-14 06:39:43.762441
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys

    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    if PyInfo.PY2:
        assert PyInfo.PY3 is False
    else:
        assert PyInfo.PY3 is True

    assert sys.version_info[0] == PyInfo.PY2 + 2 * PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, (type, types.ClassType))
    assert isinstance(PyInfo.binary_type, (type, types.ClassType))
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)


# Generated at 2022-06-14 06:39:49.023663
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3
    assert PyInfo.string_types == str
    assert isinstance(PyInfo.text_type(), str)
    assert isinstance(PyInfo.binary_type(), bytes)
    assert PyInfo.integer_types == int
    assert isinstance(PyInfo.maxsize, int)
    assert isinstance(PyInfo.class_types(), type)

# Generated at 2022-06-14 06:40:05.242773
# Unit test for constructor of class PyInfo
def test_PyInfo():
    for name in dir(PyInfo):
        if name == '__class__':
            continue
        assert getattr(PyInfo, name) is not None
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types
    assert PyInfo.maxsize

# Generated at 2022-06-14 06:40:11.367989
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance(u'a', PyInfo.string_types)
    else:
        assert not isinstance(u'a', PyInfo.string_types)
    assert isinstance('a', PyInfo.string_types)
    assert PyInfo.maxsize == (1 << 63) - 1

# Generated at 2022-06-14 06:40:18.713761
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance('string', PyInfo.string_types)
    assert isinstance(u'string', PyInfo.string_types)
    assert not isinstance(b'string', PyInfo.string_types)

    assert isinstance(b'string', PyInfo.binary_type)
    assert not isinstance('string', PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.integer_types)

    assert isinstance(type, PyInfo.class_types)
    assert isinstance(str, PyInfo.class_types)
    assert not isinstance(1, PyInfo.class_types)

# Generated at 2022-06-14 06:40:25.470287
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types
    assert PyInfo.maxsize
    assert isinstance(1, PyInfo.integer_types)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:40:28.655437
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.maxsize == sys.maxsize
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:40:41.094986
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
    else:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)



# Generated at 2022-06-14 06:40:48.922390
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Test for method PY2
    assert isinstance(PyInfo.PY2, bool)
    # Test for method PY3
    assert isinstance(PyInfo.PY3, bool)
    # Test for method string_types
    assert isinstance(PyInfo.string_types, tuple)
    # Test for method text_type
    assert isinstance(PyInfo.text_type, type)
    # Test for method binary_type
    assert isinstance(PyInfo.binary_type, type)
    # Test for method integer_types
    assert isinstance(PyInfo.integer_types, tuple)
    # Test for method class_types
    assert isinstance(PyInfo.class_types, tuple)
    # Test for method maxsize
    assert isinstance(PyInfo.maxsize, int)



# Generated at 2022-06-14 06:41:01.131563
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

# Generated at 2022-06-14 06:41:09.676755
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
    else:
        assert isinstance(u"", PyInfo.text_type)
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:41:13.825965
# Unit test for constructor of class PyInfo
def test_PyInfo():
    res = PyInfo.PY3
    if sys.version_info[0] == 2:
        assert res is False
    else:
        assert res is True



# Generated at 2022-06-14 06:41:37.350226
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    from sys import version_info
    from sys import maxsize

    assert isinstance(version_info[0], int)
    if PyInfo.PY2:
        assert isinstance(maxsize, (int, long))
    if PyInfo.PY3:
        assert isinstance(maxsize, int)

# Generated at 2022-06-14 06:41:41.629240
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert {PyInfo.string_types}.issubset({basestring, str})


Py2Bytes = type(bytes(b''))
Py3Bytes = type(bytes())

# Generated at 2022-06-14 06:41:46.654351
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == isinstance(u"abc", str)
    assert PyInfo.PY3 == isinstance(b"abc", bytes)
    assert PyInfo.PY3 == isinstance(123456, int)
    assert PyInfo.PY3 == isinstance(dict(), type)



# Generated at 2022-06-14 06:41:57.089389
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not None
    assert PyInfo.PY3 is not None

    for string_type in PyInfo.string_types:
        assert isinstance("", string_type)
        assert isinstance(string_type(), string_type)

    assert isinstance("", PyInfo.binary_type)
    assert isinstance(PyInfo.binary_type(), PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(PyInfo.maxsize, PyInfo.integer_types)

    for class_type in PyInfo.class_types:
        assert isinstance(PyInfo, class_type)
        assert isinstance(class_type(), class_type)

# Generated at 2022-06-14 06:42:07.631892
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3

    assert str in PyInfo.string_types
    assert unicode in PyInfo.string_types
    assert not bytes in PyInfo.string_types

    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str

    assert int in PyInfo.integer_types
    assert long in PyInfo.integer_types
    assert not float in PyInfo.integer_types
    assert not complex in PyInfo.integer_types

    assert type in PyInfo.class_types
    assert types.ClassType in PyInfo.class_types
    assert not int in PyInfo.class_types
    assert not unicode in PyInfo.class_types

# Generated at 2022-06-14 06:42:08.919327
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is s

# Generated at 2022-06-14 06:42:23.064779
# Unit test for constructor of class PyInfo
def test_PyInfo():
    class TestPyInfo(object):
        def __init__(self):
            self.enable = True
            self.message = ""


# Generated at 2022-06-14 06:42:29.704309
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print('Python version: %s' % PyInfo.PY3)
    print('Python maxsize: %s' % PyInfo.maxsize)


# test_PyInfo()

if PyInfo.PY3:
    from urllib.parse import urlparse
    from urllib.parse import urljoin
    from urllib import request
    import configparser
    from queue import Queue
    from queue import Empty
    from collections import OrderedDict
    from multiprocessing import Process
    from multiprocessing import Lock
    from multiprocessing import Value
    from multiprocessing import Manager
    from multiprocessing import Pool
    from multiprocessing import cpu_count
    import http.client
    import urllib
    import queue as Queue
else:
    import urllib.request as request


# Generated at 2022-06-14 06:42:41.716797
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert len(PyInfo.string_types) == 1
    assert isinstance("test", PyInfo.string_types)
    assert not isinstance(u"test", PyInfo.string_types)
    assert isinstance("test", PyInfo.text_type)
    assert not isinstance(u"test", PyInfo.text_type)
    assert len(PyInfo.integer_types) == 2
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:42:43.243633
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3


test_PyInfo()

# Generated at 2022-06-14 06:43:35.860006
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert sys.version_info[0] == 2 or sys.version_info[0] == 3
    assert PyInfo.PY3 or PyInfo.PY2

    assert isinstance('', (PyInfo.string_types))
    assert isinstance(b'', (PyInfo.string_types))
    assert isinstance(u'', (PyInfo.string_types))

    assert isinstance('', (PyInfo.text_type))
    assert not isinstance(b'', (PyInfo.text_type))
    assert isinstance(u'', (PyInfo.text_type))

    assert not isinstance('', (PyInfo.binary_type))
    assert isinstance(b'', (PyInfo.binary_type))

# Generated at 2022-06-14 06:43:38.923590
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is sys.version_info[0] == 2
    assert PyInfo.PY3 is sys.version_info[0] == 3

# Generated at 2022-06-14 06:43:41.097009
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3


# Check if input is string

# Generated at 2022-06-14 06:43:46.144420
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types
    assert PyInfo.maxsize



# Generated at 2022-06-14 06:43:53.571523
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (2 == sys.version_info[0])
    assert PyInfo.PY3 == (3 == sys.version_info[0])

    if PyInfo.PY2:
        assert PyInfo.string_types == (types.StringType, types.UnicodeType)
        assert PyInfo.text_type == types.UnicodeType
        assert PyInfo.binary_type == types.StringType
        assert PyInfo.integer_types == (int, types.LongType)
        assert PyInfo.class_types == (types.TypeType,)
        assert PyInfo.maxsize == sys.maxint
    else:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types

# Generated at 2022-06-14 06:43:57.794783
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys

    assert PyInfo.PY2 ^ PyInfo.PY3
    if PyInfo.PY2:
        assert sys.version_info[0] == 2
    else:  # PY3
        assert sys.version_info[0] == 3

# Generated at 2022-06-14 06:44:07.094632
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert PyInfo.PY3 is False
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

    print ("All tests passed for class PyInfo")


# Provide a static class that check if a dict object is not empty

# Generated at 2022-06-14 06:44:09.085640
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:44:14.429963
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert isinstance(b"hello", bytes)
        assert isinstance(u"hello", str)
    else:
        assert isinstance(b"hello", str)
        assert isinstance(u"hello", unicode)

# Generated at 2022-06-14 06:44:25.149009
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert isinstance('string', PyInfo.string_types)
        assert isinstance('string', PyInfo.text_type)
        assert not isinstance('string', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(1, PyInfo.class_types)

    else:
        assert isinstance('string', PyInfo.string_types)
        assert isinstance(u'string', PyInfo.text_type)
        assert not isinstance(u'string', PyInfo.binary_type)
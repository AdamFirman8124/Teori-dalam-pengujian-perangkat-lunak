

# Generated at 2022-06-13 17:40:54.153608
# Unit test for function walk_packages
def test_walk_packages():
    import unittest

    run = unittest.TestCase()
    root = 'pyslvs'
    sys_path.append(dirname(__file__))
    run.assertEqual(list(walk_packages(root, '.')), [(root, 'pyslvs')])
    run.assertRaises(ValueError, list, walk_packages(root, root))
    run.assertRaises(ValueError, list, walk_packages(root, root + 'xxx'))

# Generated at 2022-06-13 17:41:01.477083
# Unit test for function walk_packages
def test_walk_packages():
    from os import sep
    from os.path import dirname, basename
    from shutil import rmtree
    from tempfile import TemporaryDirectory
    from urllib.request import urlretrieve
    from tarfile import open as tarfile_open
    from importlib.machinery import SourceFileLoader
    with TemporaryDirectory() as tmp:
        target = join(tmp, 'pathlib-stubs.tar.gz')
        urlretrieve(
            'https://github.com/python/typeshed/raw/master/stdlib/3.7/pathlib.pyi',
            target,
        )
        with tarfile_open(target) as t:
            t.extractall(tmp)
        assert True is SourceFileLoader(
            'pathlib',
            join(tmp, 'pathlib.pyi')
        ).load_

# Generated at 2022-06-13 17:41:05.212395
# Unit test for function loader
def test_loader():
    """Test function."""
    import pkgutil
    loader(
        'pyslvs',
        pkgutil.get_loader('pyslvs').archive,
        True,
        1,
        True
    )

# Generated at 2022-06-13 17:41:10.770646
# Unit test for function loader
def test_loader():
    import tempfile
    import shutil
    import sys

    docs = ['#' + ('=' * 12)]


# Generated at 2022-06-13 17:41:18.292453
# Unit test for function loader
def test_loader():
    """Unit test for loader()."""
    from .pkg_resources import import_module
    # Assume this directory
    pwd = dirname(abspath(__file__))
    assert import_module('compiler').__file__ == __file__
    assert import_module('compiler.__main__').__file__ == __file__
    assert import_module('numpy').__file__ == pwd + '/../__init__.py'
    assert import_module('numpy.__init__').__file__ == pwd + '/../__init__.py'
    assert import_module('numpy.core').__file__ == pwd + '/../core.py'
    assert import_module('numpy.core.__init__').__file__ == pwd + '/../core.py'

# Generated at 2022-06-13 17:41:26.047874
# Unit test for function loader
def test_loader():
    doc = loader('math', abspath('docs'), False, 2, False)

# Generated at 2022-06-13 17:41:31.086363
# Unit test for function loader
def test_loader():
    """Test case of function loader."""
    sys_path.append(join(dirname(__file__), "test"))
    doc = loader("test", dirname(__file__), False, 1, False)

# Generated at 2022-06-13 17:41:37.301664
# Unit test for function loader
def test_loader():
    from .test_parser import assert_equals
    from pkgutil import get_data
    from io import StringIO
    path = join(dirname(__file__), 'test_compiler')
    assert_equals(loader('module', path, False, 1, False),
                  get_data('module', 'test.txt').decode())
    io = StringIO()
    import logging
    logger.addHandler(logging.StreamHandler(io))
    logger.setLevel(logging.DEBUG)
    loader('module', path, True, 1, True)
    logger.handlers[0].close()
    logger.removeHandler(logger.handlers[0])
    assert_equals(io.getvalue(), get_data('module', 'test.log').decode())

# Generated at 2022-06-13 17:41:41.640664
# Unit test for function loader
def test_loader():
    p = Parser.new(False, 1, False)
    if not _load_module('math', join('/', 'usr', 'lib', 'python3.8', 'lib-dynload', 'math.cpython-38-x86_64-linux-gnu.so'),
                      p, True):
        raise ValueError("math can not be loaded!")
    if not _load_module('ctypes.cdll', '/usr/lib/python3.8/lib-dynload/ctypes.cpython-38-x86_64-linux-gnu.so',
                      p, True):
        raise ValueError("ctypes.cdll can not be loaded!")



# Generated at 2022-06-13 17:41:45.314730
# Unit test for function walk_packages
def test_walk_packages():
    from .robotics import kin

    def path_list(name: str) -> list[str]:
        return [path for _, path in walk_packages(name, dirname(kin.__file__))]

    assert path_list('pyslvs') == [
        kin.__file__,
        dirname(kin.__file__) + f'/structures{PEP561_SUFFIX}.pyi',
    ]
    assert path_list('pyslvs.structures') == [
        dirname(kin.__file__) + '/structures.py',
        kin.__file__,
        dirname(kin.__file__) + f'/robotics{PEP561_SUFFIX}.pyi',
    ]




# Generated at 2022-06-13 17:41:06.436798
# Unit test for function walk_packages
def test_walk_packages():
    assert tuple(walk_packages("test", "test_data")) == (
        ("test.test", "test_data/test/__init__.pyi"),
        ("test.test_data", "test_data/test_data/__init__.pyi"),
        ("test.test_data.__main__", "test_data/test_data/__main__.py"),
        ("test.test_data.test", "test_data/test_data/test.py"),
        ("test.test_data.test_data", "test_data/test_data/test_data.pyi"),
    )

# Generated at 2022-06-13 17:41:08.880979
# Unit test for function loader
def test_loader():
    """Test loader function."""
    assert loader('pyslvs', r'D:\GitHub\PySLVS\src', False, 1, False)


if __name__ == "__main__":
    test_loader()

# Generated at 2022-06-13 17:41:13.357794
# Unit test for function walk_packages
def test_walk_packages():
    from .test_data import pypi_package
    with temporarily_chdir(pypi_package):
        assert tuple(walk_packages('pkg1', 'pkg1')) == (
            ('pkg1.a', 'pkg1/a.pyi'),
            ('pkg1.b', 'pkg1/b.py'),
            ('pkg1.b.c', 'pkg1/b/c.py')
        )



# Generated at 2022-06-13 17:41:16.346344
# Unit test for function loader
def test_loader():
    from pprint import pprint
    from .test_data import root_names, pwd
    pprint(gen_api(root_names, pwd, dry=True))

# Generated at 2022-06-13 17:41:18.148952
# Unit test for function loader
def test_loader():
    """Unit test."""
    assert loader('test', '.')

# Generated at 2022-06-13 17:41:26.048839
# Unit test for function loader
def test_loader():
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from random import choice
    from string import ascii_letters

    def name_gen() -> str:
        return ''.join(choice(ascii_letters) for _ in range(6))

    def path_gen() -> str:
        return name_gen() + '.py'

    def path_gen_upper() -> str:
        return '__init__.py'

    def stmt_gen(name: str) -> str:
        return f"def {name}():\n    pass\n"

    root = name_gen()

    with TemporaryDirectory(prefix='pyslvs-') as temp:
        root_path = Path(temp) / root

        root_path.mkdir()


# Generated at 2022-06-13 17:41:31.086464
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from pkgutil import get_data
    from typing import Optional
    from os.path import dirname
    from .logger import logger

    logger.info("Test loader")

    def create_root_names(name: str) -> Optional[str]:
        return get_data(name, "root_names.txt").decode("utf-8")

    def _test_loader(name: str) -> None:
        root_names = create_root_names(name)
        if root_names is None:
            logger.info("skip")
            return
        root_names = {i.strip() for i in root_names.split("\n")}
        path = dirname(get_data(name, ""))

# Generated at 2022-06-13 17:41:37.475799
# Unit test for function walk_packages

# Generated at 2022-06-13 17:41:46.473445
# Unit test for function loader
def test_loader():
    import pytest
    root = 'mock_root'
    name1 = root + ".sub"
    name2 = root + ".sub.__init__"
    name3 = root + ".sub.subsub"
    pkg = """
    def func1(): ...
    class C: ...
    """
    subsub = """
    def func2(): ...
    class D: ...
    """
    doc = loader(root, 'tests/mock_package', False, 3, False)
    assert 'Subpackage' in doc
    assert name1 in doc
    assert 'func1' in doc
    assert 'func2' in doc
    assert 'C' in doc
    assert 'D' in doc
    assert name2 not in doc
    assert name3 not in doc
    p = Parser.new(False, 3, False)


# Generated at 2022-06-13 17:41:51.169781
# Unit test for function walk_packages
def test_walk_packages():
    from math import pi
    from sys import version
    from os.path import join, dirname, basename, splitext
    for root, path in walk_packages('math', dirname(pi.__file__)):
        package = __import__(root)
        assert path == join(dirname(package.__file__), basename(path))
    for root, path in walk_packages(version[:3], dirname(version.__file__)):
        package = __import__(root)
        assert path == join(dirname(package.__file__), splitext(basename(path))[0])

# Generated at 2022-06-13 17:42:54.952870
# Unit test for function walk_packages
def test_walk_packages():
    assert _site_path("pyslvs_ui")


# Generated at 2022-06-13 17:42:59.335250
# Unit test for function loader
def test_loader():
    from unittest import TestCase, main
    from importlib import reload
    from .cached import cache

    class CompilerTest(TestCase):

        def test_loader(self) -> None:
            reload(cache)
            text = loader("ns_truetype", "../../", True, 2, True)
            self.assertNotEqual(len(text), 0)

    main()

# Generated at 2022-06-13 17:43:09.939097
# Unit test for function walk_packages
def test_walk_packages():
    """Unit test for function walk_packages."""
    from os.path import join, dirname, exists
    from sys import path
    from importlib import reload
    from .test_packages import test_package
    from .__main__ import __version__ as VERSION

    path.append(__file__)
    test_package()
    prefix = join(dirname(__file__), test_package.__name__)
    p = Parser.new(False, 1, False)
    p.parse('pyslvs', f"# {VERSION}\n")
    for name, path in walk_packages(test_package.__name__, prefix):
        p.parse(name, _read(path + ".py"))

# Generated at 2022-06-13 17:43:22.088118
# Unit test for function walk_packages
def test_walk_packages():
    from . import common
    from .common import test
    assert test(walk_packages, [
        '', '', []
    ])

# Generated at 2022-06-13 17:43:30.258266
# Unit test for function loader
def test_loader():
    """Some unit test for the `loader()` function."""
    import sys
    import os.path
    import pathlib
    import tempfile
    import shutil

    def get_temp_dir():
        """get_temp_dir() -> (path, close)"""
        dir_name = tempfile.mkdtemp()
        def close():
            shutil.rmtree(dir_name)
        return dir_name, close

    root_name = 'test'
    wrapper_code = 'def wrapper(func):\n    return func'

    test_root, close = get_temp_dir()

# Generated at 2022-06-13 17:43:40.360021
# Unit test for function loader
def test_loader():
    from os import remove
    from os.path import exists
    from pytest import raises
    from pyslvs_ui.package_manager.path import get_path
    from pyslvs_ui.compiler import api_solver

    def test_loader(api_name, link: bool, level: int):
        p = Parser.new(link, level, False)
        for name, path in walk_packages(api_name, get_path()):
            logger.debug(f"{name} <= {path}.py")
            p.parse(name, _read(path + ".py"))
        return p

    p = test_loader(api_solver, True, 2)
    assert p.compile()
    p = test_loader(api_solver, False, 3)
    assert p.compile()

   

# Generated at 2022-06-13 17:43:48.028870
# Unit test for function loader
def test_loader():
    """Integration test for the module."""
    from pkgutil import get_importer
    from os import path
    import sys

    def app_path(name: str) -> str:
        """Get the path of an application."""
        name = sys.executable if name == "python" else name
        imp = get_importer(name)
        return path.join(path.dirname(path.dirname(imp.path)), name)

    def test_generate(name: str) -> str:
        return loader(name, app_path("python"), link=False, level=1, toc=True)

    assert test_generate("sys")
    assert test_generate("time")
    assert test_generate("os")
    assert test_generate("types")
    assert test_generate("numpy")


# Generated at 2022-06-13 17:43:55.668791
# Unit test for function loader
def test_loader():
    """Test for function loader."""
    from importlib import machinery
    from sys import path as sys_path
    from pathlib import Path
    from unittest import TestCase, mock

    def _load_mock_ext(name: str, path: str) -> bool:
        """Wrapper."""
        path = Path(path)
        if path.suffix:
            s = spec_from_file_location(name, path, loader=machinery.ExtensionFileLoader)
        else:
            s = spec_from_file_location(name, path / (path.name + '.c'))
        if s is None or not isinstance(s.loader, machinery.ExtensionFileLoader):
            return False
        m = module_from_spec(s)
        s.loader.exec_module(m)
        return True



# Generated at 2022-06-13 17:44:04.438407
# Unit test for function walk_packages
def test_walk_packages():
    from unittest import TestCase


# Generated at 2022-06-13 17:44:12.847475
# Unit test for function walk_packages
def test_walk_packages():
    from tempfile import TemporaryDirectory
    from shutil import rmtree
    from os import environ, chdir
    from os.path import dirname
    from pkg_resources import WorkingSet
    from ..vendor import pkgutil
    from types import ModuleType
    from importlib import import_module, InvalidModuleName
    with TemporaryDirectory() as tmp:
        environ['PYTHONPATH'] = tmp
        working_set = WorkingSet([tmp])
        mkdir(join(tmp, 'a'))
        mkdir(join(tmp, 'a', 'b'))
        with open(join(tmp, 'a', 'b', '__init__.py'), 'w+') as f:
            f.write("__version__ = '0.1.0'\n")

# Generated at 2022-06-13 17:45:10.486514
# Unit test for function loader
def test_loader():
    """Test loader function."""
    from .test_loader import get_test_dir
    from .logger import enable_logger
    enable_logger('INFO')
    logger.info(f"Test dir: {get_test_dir()}")
    loader(__name__, get_test_dir(), False, 1, False)

# Generated at 2022-06-13 17:45:13.232928
# Unit test for function loader
def test_loader():
    from pyslvs_ui.package import __path__
    from pyslvs_ui.compiler import loader
    for name, path in walk_packages('pyslvs_ui', __path__[0]):
        if not name.startswith('pyslvs_ui.compiler'):
            continue
        loader(name, path, False, 1, False)


if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:45:19.523033
# Unit test for function walk_packages
def test_walk_packages():
    """Tests the walker."""
    assert list(walk_packages("test", "./test/module")) == [
        ("test.__init__", "./test/module/test/__init__.py"),
        ("test.test_test", "./test/module/test/test_test.py"),
    ]
    assert list(walk_packages("test", "./test/packages")) == [
        ("test.dummy", "./test/packages/test/dummy.py"),
        ("test.dummy", "./test/packages/test/dummy-stubs.pyi"),
        ("test.__init__", "./test/packages/test/__init__.py"),
    ]

# Generated at 2022-06-13 17:45:28.268121
# Unit test for function loader
def test_loader():
    p = Parser.new(True, 1, False)
    test_data = join('Pyslvs', 'src', 'pyslvs_ui', 'plugin', 'test', 'data')
    paths = [join(test_data, 'a.so'), join(test_data, 'b.pyi')]
    for name, path in walk_packages('test', test_data):
        for path_ext in paths:
            if not str(path_ext).startswith(path):
                continue
            if path_ext.endswith('.pyi'):
                p.parse(name, _read(path_ext))
            elif path_ext.endswith('.so'):
                _load_module(name, path_ext, p)
            break
        else:
            break

# Generated at 2022-06-13 17:45:35.480652
# Unit test for function loader
def test_loader():
    root = 'pyslvs'
    pwd = dirname(dirname(abspath(__file__)))
    link = False
    level = 0
    toc = True
    doc = loader(root, pwd, link, level, toc).strip()
    print(doc)
    assert "class" in doc
    assert '##' not in doc

# Generated at 2022-06-13 17:45:43.723453
# Unit test for function walk_packages
def test_walk_packages():
    assert len(
        list(
            walk_packages(
                "math",
                join(dirname(abspath(__file__)), "..", "..", "python", "lib")
            )
        )
    ) >= 20
    assert len(
        list(
            walk_packages(
                "turtle",
                join(dirname(abspath(__file__)), "..", "..", "python", "lib")
            )
        )
    ) >= 4
    assert len(
        list(
            walk_packages(
                "tkinter",
                join(dirname(abspath(__file__)), "..", "..", "python", "lib")
            )
        )
    ) >= 5

# Generated at 2022-06-13 17:45:47.269915
# Unit test for function walk_packages
def test_walk_packages():
    assert list(walk_packages(name='pyslvs', path='test_src')) == [
        ('test_src.test', 'test_src/test.py'),
        ('test_src.test.test_test', 'test_src/test/test_test.py'),
        ('test_src.test_src', 'test_src/test_src.pyi'),
    ]
    assert list(walk_packages(name='pyslvs', path='test_src/test')) == [
        ('test_src.test.test_test', 'test_src/test/test_test.py'),
    ]

# Generated at 2022-06-13 17:45:56.859842
# Unit test for function loader
def test_loader():
    import tempfile
    import os
    import shutil
    from pkgutil import extend_path
    from importlib import import_module
    from io import StringIO
    from .parser import Parser

    # Create temporary directory
    temp_name = "temp"
    temp_path = os.path.join(tempfile.gettempdir(), temp_name)
    os.makedirs(temp_path)
    sys_path.append(tempfile.gettempdir())

    p = Parser.new(True, 1, False)

    # Create package
    package_path = os.path.join(temp_path, temp_name)
    os.makedirs(package_path)

# Generated at 2022-06-13 17:46:01.434639
# Unit test for function walk_packages
def test_walk_packages():
    from os.path import relpath, basename, normpath
    package_name = 'pyslvs_ui'
    sys_path.append('.')
    assert isdir(package_name)
    assert isdir('pyslvs-ui')
    assert isdir('pyslvs_ui-stubs')
    path = _site_path(package_name)
    assert path != '', "site-packages not found"
    res = []
    for name, p in walk_packages(package_name, path):
        assert p.startswith(path)
        assert name == relpath(p, path).replace(sep, '.')
        assert not name.startswith('.')

# Generated at 2022-06-13 17:46:06.988900
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from unittest import TestCase, main
    from os import remove
    from tempfile import TemporaryDirectory

    class TestCase(TestCase):

        def setUp(self) -> None:
            self.dir = TemporaryDirectory()
            self.path = self.dir.name

        def test_gen_api(self):
            root_names = {'Test': 'test'}
            print(gen_api(root_names, self.path, dry=True))
            remove(join(self.path, 'docs', 'test-api.md'))

    from datetime import timedelta
    from timeit import default_timer
    kwargs = dict(setup='from __main__ import test_loader; t=test_loader()', number=1)
    t = default_timer()

# Generated at 2022-06-13 17:47:53.690573
# Unit test for function loader
def test_loader():
    root = "pyslvs"
    doc = loader(root, "../", link=False, level=1, toc=False)
    print(f"Parsed document:\n\n{doc}")

# Generated at 2022-06-13 17:47:55.878903
# Unit test for function loader
def test_loader():
    """Test local module."""
    # import pathlib
    assert loader('pathlib', '.', link=True, level=1, toc=False)


if __name__ == "__main__":
    test_loader()

# Generated at 2022-06-13 17:47:58.926018
# Unit test for function loader
def test_loader():
    import sys
    logger.cri('Unit test for function "loader"')
    logger.info('=' * 12)
    doc = loader("tkinter", sys.executable, True, 2, False)
    print(doc)

# Generated at 2022-06-13 17:48:01.660586
# Unit test for function walk_packages
def test_walk_packages():
    """Test function walk_packages."""
    print(list(walk_packages('test', '.')))
    print(list(walk_packages('pyslvs', '.')))

# Generated at 2022-06-13 17:48:07.842362
# Unit test for function loader
def test_loader():
    """Test function `loader`."""
    logger.debug('=' * 12)
    logger.debug('Function loader:')
    from .pkg_loader import main
    from pkgutil import iter_modules
    from .logger import logger
    from .pyslvs import __version__
    logger.setLevel(50)
    main(bind=False, output=('-', '-'),
         modules=tuple(m.name for m in iter_modules()),
         link=False, level=1, toc=False, target=__version__)

# Generated at 2022-06-13 17:48:17.638682
# Unit test for function walk_packages
def test_walk_packages():
    """Test: walk packages."""
    # Test with relative path
    print("Test with relative path")
    for n, p in walk_packages("pyslvs", "../pyslvs"):
        print(f"{n} <= {p}")
    # Test with absolute path
    print("Test with absolute path")
    for n, p in walk_packages("pyslvs", abspath("../pyslvs")):
        print(f"{n} <= {p}")
    # Test with site-package path
    print("Test with site-package path")
    for n, p in walk_packages("pyslvs_ui", _site_path("pyslvs_ui")):
        print(f"{n} <= {p}")


if __name__ == "__main__":
    test_

# Generated at 2022-06-13 17:48:21.068064
# Unit test for function walk_packages
def test_walk_packages():
    """Test for function walk_packages."""
    path = 'tests/data/dummy'
    for name, f_path in walk_packages('dummy', path):
        print(name, f_path)
    assert name == 'dummy.test'
    assert f_path == path + sep + 'test.py'



# Generated at 2022-06-13 17:48:27.472805
# Unit test for function loader
def test_loader():
    from tempfile import TemporaryDirectory
    from unittest import TestCase

    from .parser import format_yaml

    class Test(TestCase):

        def test(self):
            # A simple test
            with TemporaryDirectory(prefix='tmp_') as tmp_path:
                pwd = f"{tmp_path}/site-packages"
                mkdir(pwd)
                _write(f"{pwd}/__init__.py", "# init")
                _write(f"{pwd}/example.py", "# test")
                _write(f"{pwd}/example.pyi", f"'''{format_yaml(**{'var': 'var'})}'''\n")
                doc = loader("example", tmp_path, False, 1, False)

# Generated at 2022-06-13 17:48:36.583975
# Unit test for function loader
def test_loader():
    """Test function loader."""
    import sys
    import io
    import unittest

    class TestLoader(unittest.TestCase):
        """Test function loader."""

        def __init__(self, *args, **kwargs) -> None:
            """Initialize the test."""
            super(TestLoader, self).__init__(*args, **kwargs)
            self.maxDiff = None

        def test_loader(self) -> None:
            """Test function loader."""
            doc = loader(
                'PyQt5',
                r'C:\Users\ycchang\AppData\Local\Programs\Python\Python39\Lib'
                r'\site-packages\PyQt5', True, 1, True)
            self.assertEqual(len(doc), 3948)


# Generated at 2022-06-13 17:48:46.257608
# Unit test for function walk_packages
def test_walk_packages():
    from os import remove
    from os.path import isfile
    from shutil import rmtree

    # Create directories
    assert not isdir('__PACKAGES_TEST__')
    assert not isdir('__PACKAGES_TEST__/server/')
    assert not isdir('__PACKAGES_TEST__/client/')
    mkdir('__PACKAGES_TEST__')
    mkdir('__PACKAGES_TEST__/server/')
    mkdir('__PACKAGES_TEST__/client/')

    # Create files
    def _write(path: str, doc: str) -> None:
        with open(path, 'w+', encoding='utf-8') as f:
            f.write(doc)

    # 1. Common files
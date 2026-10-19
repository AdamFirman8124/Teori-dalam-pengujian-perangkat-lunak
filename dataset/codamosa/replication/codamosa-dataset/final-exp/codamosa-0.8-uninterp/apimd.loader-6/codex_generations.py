

# Generated at 2022-06-13 17:41:20.751535
# Unit test for function loader
def test_loader():
    # Loading modules
    assert _load_module('foo', 'foo.so', Parser())
    # Wrong path
    assert not _load_module('foo', 'foo.so', Parser())
    loader('pyslvs_ui', './pyslvs_ui', True, 1, True)


# Unit test gen_api

# Generated at 2022-06-13 17:41:27.696024
# Unit test for function loader
def test_loader():
    root = "pyslvs"
    pwd = parent(parent(abspath(__file__)))
    logger.info(f"ZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZz")
    logger.info(f"Generate api summary for {root}")
    logger.info(f"ZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZz")
    p = Parser.new(True, 1, False)

# Generated at 2022-06-13 17:41:36.335610
# Unit test for function loader
def test_loader():
    from unittest.mock import patch

    def _spec(name):
        from importlib.machinery import SourceFileLoader
        return spec_from_file_location(name, 'test.py')

    with patch('pyslvs.compiler.find_spec', return_value=_spec('test')):
        with patch('pyslvs.compiler.SourceFileLoader.get_code', return_value="def a(): pass"):
            assert loader('test', '.', True, 1, True) == '''
# test API

## a()

No docstring.

---
'''.strip()

# Generated at 2022-06-13 17:41:41.496391
# Unit test for function walk_packages

# Generated at 2022-06-13 17:41:51.242221
# Unit test for function loader
def test_loader():
    from tempfile import mkdtemp
    from shutil import rmtree
    from importlib import import_module
    p = Parser.new(True, 0, False)
    # Create temp path to test walk
    tmp = mkdtemp()
    root = join(tmp, 'tmp')
    mkdir(root)
    # Test modules
    mkdir(join(root, 'tmp'))
    _write(join(root, '__init__.py'), '')
    _write(join(root, 'tmp', '__init__.py'), '')
    _write(join(root, 'tmp', 'tmp1.py'), 'def f1(): pass\n')
    _write(join(root, 'tmp', 'tmp1.pyi'), 'def f1(): ...\n')

# Generated at 2022-06-13 17:41:57.493536
# Unit test for function walk_packages
def test_walk_packages():
    packages = list(walk_packages("app_name", "app_path"))
    assert packages
    assert packages[0][0] == "app_name.module_name"
    assert packages[0][1].endswith("app_path/app_name/module_name.py")
    assert packages[-1][0] == "app_name.module_name.sub_module_name3"
    assert packages[-1][1].endswith("app_path/app_name/module_name/sub_module_name3.pyi")

# Generated at 2022-06-13 17:42:03.462449
# Unit test for function walk_packages
def test_walk_packages():
    from tempfile import TemporaryDirectory
    from importlib import util
    from pytest import approx
    from .test_data import test_data
    from .readme import copyright
    with TemporaryDirectory() as temp:
        for name, py in test_data.items():
            spec = util.spec_from_file_location(name, f"{temp}/{name}.py")
            assert spec.submodule_search_locations is None
            module = util.module_from_spec(spec)
            spec.loader.exec_module(module)
            assert module.copyright == copyright
            with open(f"{temp}/{name}.py", "w+") as fp:
                fp.write(py)
        print(list(walk_packages('hello', temp)))

# Generated at 2022-06-13 17:42:07.752673
# Unit test for function walk_packages
def test_walk_packages():
    from tempfile import TemporaryDirectory
    from importlib import import_module
    from tests.data import TEST_DATA

    with TemporaryDirectory() as folder:
        for k, v in TEST_DATA.items():
            p = join(folder, k.replace('.', sep))
            mkdir(dirname(p))
            if p.endswith('.py'):
                _write(p, v)
            else:
                _write(p + '.pyi', v)
        for k, v in walk_packages('test_package', folder):
            assert k == v.replace(folder, '').replace(sep, '.').removesuffix('.py')
            import_module(k)

# Generated at 2022-06-13 17:42:12.393974
# Unit test for function loader
def test_loader():
    from .testlib.path import Path
    pwd = abspath(join(__file__, "..", "..", "testlib"))
    sys_path.append(pwd)
    assert isinstance(loader(
        'testlib', pwd, False, 1, False
    ), str)
    with Path(join(pwd, 'testlib.py')):
        assert isinstance(loader(
            'testlib', pwd, False, 1, False
        ), str)

# Generated at 2022-06-13 17:42:15.737325
# Unit test for function loader
def test_loader():
    """Test for function loader."""
    sys_path.append('')
    a = loader('', '../test/test_package', True, 2, False)
    assert a.strip()
    sys_path.clear()

# Generated at 2022-06-13 17:45:31.111798
# Unit test for function loader
def test_loader():
    """Test `loader` function."""
    import unittest
    import os
    import platform

    class TestLoader(unittest.TestCase):

        """Test `loader` function."""

        def test_loader(self):
            """Test `loader` function."""
            from .parser import Parser as P
            from .parser import linkify, Header as H
            from .parser import mk_toc, parse
            root = os.path.dirname(os.path.abspath(__file__))
            pwd = os.path.join(root, 'modules')
            # Make sure there is a "__init__.py" file first
            os.chdir(pwd)
            # Load root first
            __import__("test")
            parser = P(link=True, level=1, toc=False)
           

# Generated at 2022-06-13 17:45:41.767942
# Unit test for function loader
def test_loader():
    """Test for the loader function."""
    from .parser import Parser

    p = Parser.new(False, 1, False)
    for name, path in walk_packages('pyslvs', _site_path('pyslvs')):
        # Load its source or stub
        pure_py = False
        for ext in [".py", ".pyi"]:
            path_ext = path + ext
            if not isfile(path_ext):
                continue
            p.parse(name, _read(path_ext))
            if ext == ".py":
                pure_py = True
        if pure_py:
            continue
        # Try to load module here
        for ext in EXTENSION_SUFFIXES:
            path_ext = path + ext
            if not isfile(path_ext):
                continue

# Generated at 2022-06-13 17:45:52.660729
# Unit test for function loader
def test_loader():
    """Compiler test."""
    from pathlib import Path
    with Path('test').mkdir(parents=True, exist_ok=True) as path:
        p = Parser.new(False)
        for m, f in walk_packages('numpy', path):
            p.parse(m, _read(f))
        p.parse('x', 'document_x')

# Generated at 2022-06-13 17:46:01.128201
# Unit test for function loader
def test_loader():
    from tempfile import TemporaryDirectory
    from os import chdir, symlink, scandir
    from os.path import join as join_path
    from shutil import copy
    from pprint import pprint

    def find(path: str, name: str) -> str:
        for f in scandir(path):
            if f.is_dir():
                r = find(f.path, name)
                if r:
                    return r
            elif f.name == name:
                return abspath(f.path)

    with TemporaryDirectory() as tempdir:
        print(f"TemporaryDirectory: {tempdir}")
        chdir(tempdir)
        cp = 'copyfile.py'
        mkdir('copyfile')

# Generated at 2022-06-13 17:46:06.686057
# Unit test for function loader
def test_loader():
    """Test the function loader."""
    import sys
    import os
    if sys.platform == "win32":
        os.chdir(r"M:\OneDrive\Documents\Pyslvs-UI\Docs")
    else:
        os.chdir("/home/i3thuan5/Documents/Pyslvs-UI/Docs")
    from .compiler import loader
    from .parser import Parser
    parser = Parser.new()
    loader('pyslvs', '/home/i3thuan5/Documents/Pyslvs-UI/dev/src', parser)
    loader(
        'pyslvs_ui',
        '/home/i3thuan5/Documents/Pyslvs-UI/dev/src/pyslvs_ui',
        parser
    )

# Generated at 2022-06-13 17:46:09.328028
# Unit test for function loader
def test_loader():
    from .test import test_src

    print(loader("test", test_src, True, 1, False).strip())


if __name__ == "__main__":
    test_loader()

# Generated at 2022-06-13 17:46:16.093272
# Unit test for function loader
def test_loader():
    """Test for `loader`."""
    from os import remove, chdir
    from os.path import dirname
    from time import sleep
    from shutil import rmtree
    from tempfile import mkdtemp, mkstemp
    from pkgutil import get_data
    from pyslvs_ui.package_path import package_path

    # Get example path
    example_dir = '_example'
    example_path = join(dirname(dirname(package_path)), example_dir)
    # Get test path
    temp_dir = mkdtemp()
    chdir(temp_dir)
    # Copy data to test path
    for parent_dir, _, fs in walk(example_path):
        rel_path = parent(parent_dir.removeprefix(example_path))
        for f in fs:
            src

# Generated at 2022-06-13 17:46:25.300626
# Unit test for function loader
def test_loader():
    """Test script."""
    from pyslvs import __version__
    import pytest
    with pytest.warns(ImportWarning):
        assert loader('pyslvs', './pyslvs', True, 1, False)
    # aiohttp testing
    with pytest.warns(ImportWarning):
        assert loader('aiohttp', '/home/master/.local/lib/python3.8/site-packages', True, 1, False)
    # mpi4py testing
    with pytest.warns(ImportWarning):
        assert loader('mpi4py', '/home/master/.local/lib/python3.8/site-packages', True, 1, False)
    # sympy testing

# Generated at 2022-06-13 17:46:34.826107
# Unit test for function walk_packages
def test_walk_packages():
    assert not any(walk_packages('not_found', 'site-packages'))
    assert not any(walk_packages('numpy', '.'))
    assert not any(walk_packages('numpy', 'site-packages'))

# Generated at 2022-06-13 17:46:37.926561
# Unit test for function loader
def test_loader():
    """Unit test for loader."""
    assert len(gen_api({"solvespace": "pyslvs"}, pwd="..", dry=True)) == 1
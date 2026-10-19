

# Generated at 2022-06-13 17:42:29.561234
# Unit test for function walk_packages
def test_walk_packages():
    import pathlib
    sys_path.append(str(pathlib.Path(__file__).parent))
    assert list(walk_packages('test', '.')) == [('test.test', './test/test.py')]
    sys_path.remove(str(pathlib.Path(__file__).parent))

# Generated at 2022-06-13 17:42:35.934203
# Unit test for function loader
def test_loader():
    """Unit test for loader()."""
    import sys
    import doctest
    sys.path.append(abspath('.'))
    module_names = [root.replace('_', '-') for root in root_names.keys()]
    docs = [f"{name}-api.md" for name in module_names]
    for path in walk_packages('pyslvs', '../'):
        # Skip test file and file with no document
        if any(path[0].endswith(name) for name in docs) or path[1] == '':
            continue
        # Print name of module file
        logger.debug(path[0])
        n, v = path[0].split('.', 1)
        # Skip module for pyslvs
        if n == 'pyslvs':
            continue


# Generated at 2022-06-13 17:42:40.206986
# Unit test for function walk_packages
def test_walk_packages():
    assert tuple(walk_packages('numpy', 'site-packages'))
    assert tuple(walk_packages('topycalc', './lib'))
    assert tuple(walk_packages('topycalc', '.'))

# Generated at 2022-06-13 17:42:42.167065
# Unit test for function loader
def test_loader():
    """Unit test for function `loader`."""
    assert len(gen_api({'test': 'pyslvs'}, 'example', dry=True))

# Generated at 2022-06-13 17:42:45.414805
# Unit test for function loader
def test_loader():
    from .temp import temp_dir, temp_file
    from .parser import _TableOfContents
    from .logger import logging_off

    with logging_off():
        with temp_dir() as t:
            with open(join(t, "__init__.py"), "w+") as f:
                f.write("# -*- coding: utf-8 -*-")


# Generated at 2022-06-13 17:42:51.805029
# Unit test for function walk_packages
def test_walk_packages():
    """Test walk packages."""

# Generated at 2022-06-13 17:43:00.958880
# Unit test for function loader
def test_loader():
    """Test the loader function."""
    from unittest.mock import patch
    import sys
    import doctest
    from pyslvs import __path__ as pyslvs_path
    # Mock `pkgutil` function
    modules_mock = patch('pyslvs.compiler.loader.pkgutil.walk_packages')
    import pyslvs
    # Make the unit test can pass
    pyslvs_dir = pyslvs_path[0]
    with modules_mock as modules:
        modules.side_effect = lambda *a, **k: walk_packages(*a, **k)
        from pyslvs.compiler import loader
        sys_path.append(pyslvs_dir)
        loader('pyslvs', pyslvs_dir, True, 1, True)


# Generated at 2022-06-13 17:43:02.474941
# Unit test for function loader
def test_loader():
    docs = loader('pyslvs_ui', 'D:/Python', 'link', 'toc')
    print(docs)

# Generated at 2022-06-13 17:43:07.571036
# Unit test for function loader
def test_loader():
    assert isinstance(
        loader(
            "pyslvs_ui",
            "C:\\Users\\Yuan\\Anaconda3\\envs\\pyslvs\\lib\\site-packages\\pyslvs_ui",
            True,
            2,
            False
        ),
        str
    )

# Generated at 2022-06-13 17:43:09.750961
# Unit test for function loader
def test_loader():
    """Unit test."""
    logger.setLevel("DEBUG")
    test = gen_api({
        'root': 'pyslvs_ui'
    })
    print(test)

# Generated at 2022-06-13 17:45:57.505078
# Unit test for function loader
def test_loader():
    """Unit test of function loader."""
    from os import remove
    from os.path import isfile
    from .logger import set_log_level
    from .temp_sys_path import add_path
    from .test_utils import sample_path_creator

    set_log_level(40)
    with add_path(sample_path_creator('sample', True)):
        loader('sample', '.', False, 1, False)
        assert isfile('docs/sample-api.md')
        remove('docs/sample-api.md')
    with add_path(sample_path_creator('sample', True)):
        loader('sample', '.', True, 3, False)
        assert isfile('docs/sample-api.md')
        remove('docs/sample-api.md')

# Generated at 2022-06-13 17:46:04.095317
# Unit test for function walk_packages
def test_walk_packages():
    import unittest
    from sys import path
    from os.path import dirname, join
    from tempfile import TemporaryDirectory

    class TestWalk(unittest.TestCase):

        def test_walk(self):
            with TemporaryDirectory() as pwd:
                path.append(pwd)
                mkdir(join(pwd, 'sub_package'))
                mkdir(join(pwd, 'sub_package_stubs'))
                mkdir(join(pwd, 'sub_package.__init___stubs'))
                _write(join(pwd, 'sub_package.__init__.py'), '')
                _write(join(pwd, 'sub_package.__init___stubs.pyi'), '')

# Generated at 2022-06-13 17:46:07.398129
# Unit test for function loader
def test_loader():
    import pyslvs_ui

    def test_gen_api(name: str) -> str:
        name = parent(name)
        path = pyslvs_ui.__file__.replace(".pyc", ".py")
        return loader(name, dirname(path), True, 2, False)

    print(test_gen_api("pyslvs_ui.api.core"))
    print(test_gen_api("pyslvs_ui.api.core_o"))
    print(test_gen_api("pyslvs_ui.api.core_g"))

# Generated at 2022-06-13 17:46:15.309557
# Unit test for function walk_packages
def test_walk_packages():
    from unittest.mock import Mock, patch
    from os import makedirs

    pwd = '_test_data'
    if not isdir(pwd):
        makedirs(pwd)
    # Create the file first
    p = join(pwd, 'foo', '__init__.pyi')
    with open(p, 'w+') as f:
        f.write('')
    p1 = join(pwd, 'foo', 'bar.pyi')
    with open(p1, 'w+') as f:
        f.write('')
    p2 = join(pwd, 'foo.pyi')
    with open(p2, 'w+') as f:
        f.write('')
    # The result

# Generated at 2022-06-13 17:46:19.406106
# Unit test for function loader
def test_loader():
    import sys
    import doctest
    doctest.testmod(sys.modules[__name__], verbose=True)


if __name__ == "__main__":
    test_loader()

# Generated at 2022-06-13 17:46:24.098345
# Unit test for function loader
def test_loader():
    from pprint import pprint
    from .api import API_CODING
    from .parser import Parser
    from .api import API_LINK
    p = Parser.new(API_LINK, 1, True)
    pprint(list(walk_packages("pyslvs", API_CODING)))
    loader("pyslvs", API_CODING, 1, True)

# Generated at 2022-06-13 17:46:31.031116
# Unit test for function loader
def test_loader():
    from unittest.mock import patch
    from os import makedirs

    makedirs('pkg1')
    makedirs('pkg1/subpkg1')
    makedirs('pkg2')
    makedirs('pkg2/subpkg2')

    # PEP 561 stubs

# Generated at 2022-06-13 17:46:42.199990
# Unit test for function loader
def test_loader():
    from os import remove
    from os.path import isdir, isfile
    from shutil import rmtree

    def assert_dir(name: str) -> None:
        assert isdir(name)
        rmtree(name)

    def assert_file(name: str, content: str) -> None:
        assert isfile(name)
        with open(name, 'r') as f:
            assert f.read() == content
        remove(name)

    prefix = '.gen-docs-test'
    assert not isdir(prefix)
    gen_api({'Core': 'pygeppetto'}, prefix=prefix)

# Generated at 2022-06-13 17:46:45.670394
# Unit test for function loader
def test_loader():
    """Test loader."""
    with open(__file__, 'r') as f:
        assert f.read() == loader('pyslvs_ui', dirname(__file__), False, 1, False)

# Generated at 2022-06-13 17:46:48.247472
# Unit test for function loader
def test_loader():
    """Test for loader."""

    def exists(name: str) -> bool:
        """Check if module exists."""
        try:
            __import__(name)
            return True
        except ImportError:
            return False

    assert 'Pillow' in sys_path
    assert exists('PIL')
    doc = loader('PIL', '.', True, 2, False)
    assert len(doc) > 0
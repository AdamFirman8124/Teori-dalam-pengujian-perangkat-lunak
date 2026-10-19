

# Generated at 2022-06-13 17:44:51.419743
# Unit test for function walk_packages
def test_walk_packages():
    path: str = tmpdir + "/testsite/"
    mkdir(path)

    mkdir(path + "a")
    mkdir(path + "a/b")
    mkdir(path + "a/b/e")
    mkdir(path + "a/b/e/f")
    mkdir(path + "a/b/e/g")
    mkdir(path + "a/b/e/g/h")
    mkdir(path + "a/b/c")
    mkdir(path + "a/b/d")
    mkdir(path + "a/b/d/i")
    mkdir(path + "a/b/d/i/j")
    mkdir(path + "a/b/d/k")

# Generated at 2022-06-13 17:44:54.184855
# Unit test for function walk_packages
def test_walk_packages():
    for name, path in walk_packages("core", ".."):
        assert name == "core.dim2"
        assert path == ".." + sep + "core" + sep + "dim2"
        break
    else:
        assert False

# Generated at 2022-06-13 17:44:59.464717
# Unit test for function walk_packages

# Generated at 2022-06-13 17:45:07.676877
# Unit test for function walk_packages
def test_walk_packages():
    assert list(walk_packages("dummy", "./")) == []
    assert list(walk_packages("dummy", ".")) == []
    assert list(walk_packages("tests", ".")) == [
        ("tests.logger", "./tests/logger.py"),
        ("tests.__main__", "./tests/__main__.py"),
        ("tests.__main__", "./tests/__main__.pyi"),
        ("tests.logger", "./tests/logger.pyi"),
        ("tests.__init__", "./tests/__init__.py"),
        ("tests.__init__", "./tests/__init__.pyi"),
    ]

# Generated at 2022-06-13 17:45:15.857048
# Unit test for function loader
def test_loader():
    assert loader('foobar', 'C:/', True, 1, False) != ''
    assert loader('foobar', 'C:/', True, 1, True) != ''
    assert loader('foobar', 'C:/', False, 1, False) != ''
    assert loader('foobar', 'C:/', False, 1, True) != ''
    assert loader('foobar', 'C:/', True, 2, False) != ''
    assert loader('foobar', 'C:/', True, 2, True) != ''
    assert loader('foobar', 'C:/', False, 2, False) != ''
    assert loader('foobar', 'C:/', False, 2, True) != ''
    assert loader('foobar', 'C:/', True, 3, False) != ''
    assert loader('foobar', 'C:/', True, 3, True) != ''

# Generated at 2022-06-13 17:45:26.744662
# Unit test for function walk_packages
def test_walk_packages():
    import unittest
    import inspect
    import shutil
    import pkgutil
    import importlib

    def write(name: str, content: str, path: str = '') -> None:
        with open(join(path, f"{name}.py"), 'w+', encoding='utf-8') as f:
            f.write(content)

    class TestWalkPackages(unittest.TestCase):

        def setUp(self) -> None:
            if not isdir("_dummy"):
                mkdir("_dummy")

        def test_walk(self) -> None:
            c = inspect.currentframe()
            write("__init__", "", "_dummy")
            write("__init__", '', "_dummy/dummy")

# Generated at 2022-06-13 17:45:33.038538
# Unit test for function loader
def test_loader():
    from shutil import rmtree
    from tempfile import mkdtemp
    from pkgutil import get_loader
    from ... import __path__ as pyslvs_path

    pyslvs = abspath(pyslvs_path[0])

    def mktmp() -> str:
        """Make a temp directory."""
        return mkdtemp(prefix="pyslvs-test-")

    def mkmod(name: str, code: str) -> None:
        """Make a temp module."""
        _write(join(pwd, name), code)

    pwd = mktmp()
    # Create new env
    mkmod("a.py", "import b\nc = 1")
    mkmod("b.py", "import c\nb = 2")

# Generated at 2022-06-13 17:45:34.729382
# Unit test for function loader
def test_loader():
    from doctest import testmod
    testmod()

# Generated at 2022-06-13 17:45:44.261174
# Unit test for function loader
def test_loader():
    from unittest.mock import patch
    from os import remove
    from shutil import rmtree, copy

    test_dir = 'pyslvs_test'
    if isdir(test_dir):
        rmtree(test_dir)
    mkdir(test_dir)

    test_file = """
from .a import A
from .b import B
from .c import C
    """
    name, path = 'main', test_dir + '/main.py'
    _write(path, test_file)

    test_file = """
from .a import A
from .b import B
from .c import C

if __name__ == "__main__":
    pass
    """
    name, path = 'main._main__', test_dir + '/main/__main__.py'
    _write

# Generated at 2022-06-13 17:45:47.079589
# Unit test for function loader
def test_loader():
    import pkgutil
    import sys

    def _test_loader(package: str, root: str) -> None:
        import importlib
        importlib.invalidate_caches()
        sys.modules.pop(package, None)
        assert loader(root, pkgutil.get_loader(package), True, 2, False)

    _test_loader('pyslvs', 'pyslvs')
    _test_loader('pythoncom', 'pythoncom')

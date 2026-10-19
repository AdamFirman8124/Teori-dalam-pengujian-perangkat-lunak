

# Generated at 2022-06-13 17:43:06.532759
# Unit test for function loader
def test_loader():
    assert loader("pyslvs", "..", True, 1, True)
    assert loader("pyslvs", "..", True, 2, True)

# Generated at 2022-06-13 17:43:12.828237
# Unit test for function loader
def test_loader():
    """Test function loader."""
    from os.path import isfile
    from shutil import rmtree
    from pyslvs_ui.info import __path__ as root
    name = 'pyslvs_ui'
    doc = loader(name, root[0], False, 1, False)
    assert doc.startswith("""# Pyslvs UI API

## Top-level variables

### __version__ = '2.0.0'

### __author__ = 'Yuan Chang'

### __email__ = 'pyslvs@gmail.com'

### __license__ = 'MIT'
""")
    name = 'pyslvs_ui.info'
    doc = loader(name, root[0], False, 1, False)

# Generated at 2022-06-13 17:43:24.037232
# Unit test for function loader
def test_loader():
    import tempfile
    path = tempfile.mkdtemp()

# Generated at 2022-06-13 17:43:30.959410
# Unit test for function walk_packages
def test_walk_packages():
    import tempfile
    d = tempfile.TemporaryDirectory()
    pwd = d.name

    def makedir(pkg: str) -> None:
        pth = join(pwd, *pkg.split("."))
        if isdir(pth):
            return
        mkdir(pth)

    def makefile(path: str, doc: str) -> None:
        _write(join(pwd, *path.split(".")), doc)

    # Test with some docs
    makedir("test")
    makefile("test.py", '"""hello"""')
    # Test with some subpackage
    makedir("test.sub_test")
    assert "test.sub_test" in list(walk_packages("test", pwd))

# Generated at 2022-06-13 17:43:39.844769
# Unit test for function loader
def test_loader():
    import sys
    import os
    root = os.path.join(os.path.dirname(__file__), "test")
    if not os.path.exists(root):
        os.mkdir(root)
    sys.path.append(root)
    assert loader(
        "pyslvs_ui",
        os.path.join(os.path.dirname(__file__), ".."),
        True,
        3,
        False
    )
    assert loader(
        "pyslvs",
        os.path.join(os.path.dirname(__file__), ".."),
        True,
        3,
        False
    )

# Generated at 2022-06-13 17:43:47.506561
# Unit test for function walk_packages
def test_walk_packages():
    """Test function walk_packages."""
    assert list(walk_packages("foo", "test/test_module.py")) == [("foo", "test/test_module.py/foo")]
    assert list(walk_packages("foo", "test/test_module.py/foo")) == [("foo", "test/test_module.py/foo")]
    assert list(walk_packages("foo", "test/test_module.py/foo/__init__.py")) == [("foo", "test/test_module.py/foo")]
    assert list(walk_packages("foo", "test/test_module.py/foo/module.py")) == [("foo", "test/test_module.py/foo")]

# Generated at 2022-06-13 17:43:51.400790
# Unit test for function loader
def test_loader():
    from unittest.mock import patch
    from os import devnull
    from pathlib import Path

    pwd = Path('.').absolute()
    with patch('os.devnull', new=str(pwd / devnull)):
        loader('', pwd / 'tests' / 'test_loader', False, 0, True)

# Generated at 2022-06-13 17:43:53.873714
# Unit test for function loader
def test_loader():
    from tempfile import TemporaryDirectory
    from shutil import rmtree
    with TemporaryDirectory() as td:
        test_script = join(td, "test_script.py")

# Generated at 2022-06-13 17:44:00.229629
# Unit test for function loader
def test_loader():
    logger.setLevel('DEBUG')
    assert len(gen_api({'sys': 'sys'}, dry=True))
    assert len(gen_api({'pyslvs': 'pyslvs'}, dry=True))
    assert len(gen_api({'PyQt5': 'PyQt5'}, dry=True))
    assert len(gen_api({'numpy': 'numpy'}, dry=True))
    assert len(gen_api({'yaml': 'yaml'}, dry=True))
    assert len(gen_api({'pandoc': 'pandoc'}, level=3, dry=True))
    assert len(gen_api({'numpy': 'numpy'}, level=1, link=False, dry=True))

# Generated at 2022-06-13 17:44:10.060036
# Unit test for function walk_packages
def test_walk_packages():
    from os import getcwd, chdir
    from os.path import exists
    from shutil import rmtree
    from .__init__ import __file__ as resource

    # Create a dummy package
    root = "module_test"
    if exists(root):
        rmtree(root)
    for sub in ["a", "b", "c"]:
        mkdir(join(root, sub))
    with open(join(root, "a", "__init__.py"), 'w+'):
        pass
    with open(join(root, "b", "__init__.py"), 'w+'):
        pass
    with open(join(root, "c", "__init__.py"), 'w+'):
        pass

# Generated at 2022-06-13 17:48:14.112129
# Unit test for function loader
def test_loader():
    from .pytest import check_ignore
    from .logger import setup_test_logger
    import pkg_resources

    setup_test_logger()
    name = 'PySLVS'
    path = pkg_resources.resource_filename(__name__, 'tests')
    d = loader(name, path, False, 1, False)

# Generated at 2022-06-13 17:48:21.278280
# Unit test for function loader
def test_loader():
    root = "pyslvs"
    pwd = ".."
    p = Parser.new(link=True, level=2, toc=False)
    for name, path in walk_packages(root, pwd):
        try:
            __import__(parent(name), fromlist=["__doc__"])
        except ImportError:
            continue
        p.parse(name, _read(path + ".py"))
        # Try to load module here
        for ext in EXTENSION_SUFFIXES:
            path_ext = path + ext
            if isfile(path_ext):
                if _load_module(name, path_ext, p):
                    break
    assert p.compile()



# Generated at 2022-06-13 17:48:27.641125
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from unittest import mock
    from contextlib import ExitStack
    from tempfile import mkdtemp
    from shutil import rmtree
    from os.path import dirname

    def generate_fake_packages(path: str):
        """Generate fake packages."""
        # Create fake packages
        mkdir(path + '/fake_package')
        mkdir(path + '/fake_package/__pycache__')
        mkdir(path + '/fake_package/submodule')
        mkdir(path + '/fake_package/submodule/__pycache__')

# Generated at 2022-06-13 17:48:36.614329
# Unit test for function loader
def test_loader():
    def check(name: str, path: str, p: Parser):
        for ext in [".py", ".pyi"]:
            path_ext = path + ext
            if not isfile(path_ext):
                continue
            logger.debug(f"{name} <= {path_ext}")
            p.parse(name, _read(path_ext))
        pure_py = True
        if pure_py:
            return
        logger.debug(f"loading extension module for fully documented:")
        # Try to load module here
        for ext in EXTENSION_SUFFIXES:
            path_ext = path + ext
            if not isfile(path_ext):
                continue
            logger.debug(f"{name} <= {path_ext}")

# Generated at 2022-06-13 17:48:42.708801
# Unit test for function loader
def test_loader():
    """Test for the function loader."""
    # pylint: disable=no-member
    from .pyslvs_ui import pyslvs
    assert len(gen_api({
        'pyslvs': 'pyslvs'
    }, pyslvs, dry=True))
    # pylint: enable=no-member


if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:48:49.020153
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from os import remove
    from tempfile import gettempdir
    from pkgutil import get_data

    # Create test package
    path = join(gettempdir(), "test_package")
    sys_path.append(path)
    if not isdir(path):
        mkdir(path)

# Generated at 2022-06-13 17:48:50.295013
# Unit test for function loader
def test_loader():
    """Test case."""
    assert loader("pyslvs_ui", ".", True, 1, False) is not None

# Generated at 2022-06-13 17:48:57.846873
# Unit test for function loader
def test_loader():
    """Unit test for `loader`."""
    from tempfile import TemporaryDirectory
    from importlib import import_module
    from shutil import move
    from os.path import join as pjoin
    from pkgutil import get_loader

    def _create_py(path: str, text: str):
        with open(path, "w+", encoding='utf-8') as f:
            f.write(text)

    def _create_pyi(path: str, text: str):
        with open(path, "w+", encoding='utf-8') as f:
            f.write(text)

    with TemporaryDirectory() as tmp:
        logger.info(tmp)

# Generated at 2022-06-13 17:49:07.579627
# Unit test for function loader
def test_loader():
    from .parser import Parser
    root = 'pyslvs'
    pwd = '../'
    link = False
    level = 1
    toc = False
    p = Parser.new(link, level, toc)
    for name, path in walk_packages(root, pwd):
        for ext in [".py", ".pyi"]:
            path_ext = path + ext
            if not isfile(path_ext):
                continue
            logger.debug(f"{name} <= {path_ext}")
            p.parse(name, _read(path_ext))
        pure_py = True
        for ext in EXTENSION_SUFFIXES:
            path_ext = path + ext
            if not isfile(path_ext):
                continue
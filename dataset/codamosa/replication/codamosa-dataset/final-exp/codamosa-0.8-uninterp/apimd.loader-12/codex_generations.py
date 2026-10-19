

# Generated at 2022-06-13 17:43:57.978720
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    p = Parser.new(False, 1, False)
    count = 0
    for name, path in walk_packages('test', 'tests'):
        if not isfile(path + '.py'):
            continue
        p.parse(name, _read(path + '.py'))
        logger.debug(f"{name} <= {path}")
        count += 1
    assert len(p.docs) == count
    doc = p.compile()
    assert doc
    # Print root
    for k, v in p.docs.items():
        if '.' not in k:
            logger.info(f"\nRoot: {k}\n" + v.full)

# Generated at 2022-06-13 17:44:06.032134
# Unit test for function loader
def test_loader():
    from unittest.mock import patch
    from pkgutil import iter_modules
    import site

    sys_path.insert(0, '')
    with patch("builtins.__import__", side_effect=ImportError):
        # No modules
        assert loader("pyslvs", "", False, 1, False) == ""

        # Load error
        assert loader("pyslvs", "", False, 1, False) == ""

        # No modules
        assert loader("pyslvs", "", False, 1, False) == ""

    with patch("builtins.__import__", side_effect=KeyError):
        # Load error
        assert loader("pyslvs", "", False, 1, False) == ""

    sys_path.insert(0, 'pyslvs')

# Generated at 2022-06-13 17:44:07.147911
# Unit test for function loader
def test_loader():
    assert isinstance(loader('name', '.'), str)



# Generated at 2022-06-13 17:44:15.270134
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from sys import version_info
    from .parser import Parser
    from .compiler import loader

    # Skip this unit test because we can not load compiled module.
    if version_info.major == 3 and version_info.minor < 8:
        return

    # Write test package
    name = abspath(dirname(dirname(__file__))) + "/test/test_package"
    mkdir(name)
    _write(join(name, "__init__.py"), "")
    _write(join(name, "module.py"), "def module(): pass\n")
    _write(join(name, "module.pyi"), "def module(): ...\n")
    _write(join(name, "test_package.py"), "def root(): pass\n")
    _

# Generated at 2022-06-13 17:44:25.607266
# Unit test for function loader
def test_loader():
    from .compiler import loader as _loader
    from .parser import Parser
    from .logger import logger as _logger
    import sys
    _logger.setLevel("DEBUG")
    sys.path.append("packages/pyslvs")
    _loader("pyslvs", "packages/pyslvs", True, 2, False)
    Parser.setup("packages/pyslvs", True)
    for name, path in walk_packages("pyslvs", "packages/pyslvs"):
        _logger.debug(f'{name} "{path}"')
    walk_packages("pyslvs", "packages/pyslvs")
    from .compiler import gen_api

# Generated at 2022-06-13 17:44:34.454261
# Unit test for function walk_packages
def test_walk_packages():
    from tempfile import mkdtemp
    from shutil import rmtree
    from os import (
        makedirs,
        mkdir,
    )

    def create(name: str, path: str) -> None:
        """Create a file."""
        makedirs(parent(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write("")

    # create temp dir
    path = mkdtemp()
    mkdir(join(path, "a"))
    mkdir(join(path, "a", "__init__.py"))
    mkdir(join(path, "b", "__init__.py"))
    mkdir(join(path, "c"))
    mkdir(join(path, "c", "__init__.py"))

# Generated at 2022-06-13 17:44:39.393077
# Unit test for function loader
def test_loader(): # pragma: no cover
    from os import getcwd
    from os.path import join
    from qtpy import QtWidgets, QtCore
    from .loader_ui_solver import Ui_Pyslvs
    from . import root_names

    def gen_api():
        nonlocal root, path, link, level, toc
        root, path, link, level, toc = ui.get_params()
        root_names[root] = root
        logger.info(f"Load root: {root}")
        doc = loader(root, path, link, level, toc)
        path = join(getcwd(), f"{root_names[root]}-api.md")
        logger.info(f"Write file: {path}")
        _write(path, doc)


# Generated at 2022-06-13 17:44:44.693008
# Unit test for function loader
def test_loader():
    root = "sys"
    pwd = _site_path(root)
    sys.path.append(pwd)
    doc = loader(root, pwd, True, 1, False)
    assert doc.replace('\n', ' ') == (
        "## sys module\n\n"
        "The `sys` module provides access to some "
        "variables used or maintained by the interpreter and to "
        "functions that interact strongly with the interpreter. "
        "It is always available."
    )

# Generated at 2022-06-13 17:44:47.427156
# Unit test for function loader
def test_loader():
    """Test for loader."""
    from .parser import ParserTest
    import doctest
    doc = loader('pyslvs', _site_path('pyslvs'), True, 1, True)
    print(doc)
    doctest.testmod(ParserTest)

# Generated at 2022-06-13 17:44:56.212967
# Unit test for function walk_packages
def test_walk_packages():
    from os import chdir, curdir, sep
    from os.path import isdir
    from shutil import rmtree
    from datetime import datetime
    from tempfile import mkdtemp
    chdir(curdir)
    temp_dir = mkdtemp()


# Generated at 2022-06-13 17:41:19.535889
# Unit test for function loader
def test_loader():
    from pkgutil import walk_packages
    from .parser import Parser
    loader = Parser.new(True)
    for _, name, _ in walk_packages(['pyslvs'], prefix='pyslvs'):
        loader.parse(name, _read(name.replace('.', '/') + '.py'))
    loader.compile()

# Generated at 2022-06-13 17:41:23.697565
# Unit test for function loader
def test_loader():
    """Test function loader."""
    with open('pytest.md', 'w') as f:
        f.write(loader('pytest', '.', True, 1, True))
    with open('pyslvs.md', 'w') as f:
        f.write(loader('pyslvs', '.', True, 1, True))



# Generated at 2022-06-13 17:41:25.914860
# Unit test for function loader
def test_loader():
    from io import StringIO
    from contextlib import redirect_stdout
    f = StringIO()
    with redirect_stdout(f):
        gen_api({'numpy': 'numpy'}, dry=True)
    assert f.getvalue().strip()

# Generated at 2022-06-13 17:41:31.320095
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    import pytest
    from pytest import approx
    from math import ceil
    from .parser import Parser

    class DummyParser(Parser):

        def __init__(self):
            self.doc: str = ""
            self.toc: str = ""
            self.table: str = ""

        def set_toc(self, title: str) -> None:
            self.toc = f"{title}\n{'=' * len(title)}\n"

        def link_to_title(self, name: str, title: str) -> str:
            return title

        def link_to_pkg(self, name: str) -> str:
            return f"[{name}]({name})"


# Generated at 2022-06-13 17:41:33.477024
# Unit test for function loader
def test_loader():
    assert len(loader(
        "Pyslvs",
        "../../",
        link=False,
        level=3,
        toc=True
    )) > 0

# Generated at 2022-06-13 17:41:35.596644
# Unit test for function loader
def test_loader():
    """Test for function loader."""
    assert loader("pyslvs", "..", False, 2, False)


if __name__ == '__main__':
    loader("pyslvs", "..", False, 2, False)

# Generated at 2022-06-13 17:41:40.879435
# Unit test for function loader
def test_loader():
    import tempfile
    from pyslvs_ui.io import make_package


# Generated at 2022-06-13 17:41:45.488642
# Unit test for function walk_packages
def test_walk_packages():
    """ Test walk_packages function. """
    logger.info("Test walk_packages function ... ", end='')
    path = join(dirname(__file__), 'test')
    i = 0
    for name, _ in walk_packages('test', path):
        logger.info(f"{name}")
        i += 1
    assert i == 11
    logger.info("OK")


if __name__ == "__main__":
    test_walk_packages()

# Generated at 2022-06-13 17:41:51.521464
# Unit test for function loader
def test_loader():
    root_names = {
        "main": "pyslvs",
        "UI": "pyslvs_ui",
        "UI plugin": "pyslvs_ui_manager",
        "Dynamics": "pyslvs_dynamics",
        "Kinematics": "pyslvs_kinematics",
        "Systems": "pyslvs_system",
        "Dynamics Simulator": "pyslvs_dynamics_simulator",
        "Kinematics Simulator": "pyslvs_kinematics_simulator",
        "Motion Simulator": "pyslvs_motion_simulator",
        "VCS": "pyslvs-vcs"
    }
    sys_path.insert(0, dirname(__file__))

# Generated at 2022-06-13 17:41:54.371609
# Unit test for function walk_packages
def test_walk_packages():
    for p in walk_packages("test", "."):
        print(p)
    for p in walk_packages("test", "./test"):
        print(p)

# Generated at 2022-06-13 17:43:19.913267
# Unit test for function loader
def test_loader():
    logger.info(gen_api({'Python Standard Library': 'pyslvs'}))


if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:43:24.693966
# Unit test for function loader
def test_loader():
    """Test package loader."""
    logger.info("Unit test for package loader")
    root = "PySlvs"
    pwd = _site_path(root)
    doc = loader(root, pwd, True, 2, True)
    logger.info("=" * 12)
    logger.info(doc)
    assert doc.strip()
    return doc



# Generated at 2022-06-13 17:43:31.303174
# Unit test for function loader
def test_loader():
    " Doctest."
    class Info:
        def __init__(self):
            self.name = 'pyslvs_ui'
            self.path = 'C:/Users/User/AppData/Local/Programs/Python/Python38/Lib/site-packages/pyslvs_ui'
            self.submodule_search_locations = [
                'C:/Users/User/AppData/Local/Programs/Python/Python38/Lib/site-packages/pyslvs_ui/pyslvs_ui.py'
            ]
    assert _site_path('pyslvs_ui') == 'C:/Users/User/AppData/Local/Programs/Python/Python38/Lib/site-packages'
    assert _site_path('pyslvs-ui') == ''

test_loader.__test__ = False

# Generated at 2022-06-13 17:43:41.147835
# Unit test for function loader
def test_loader():
    import pytest


# Generated at 2022-06-13 17:43:49.071162
# Unit test for function loader
def test_loader():
    from .test_parser import script
    from .test_parser import module_script
    from .test_parser import stub_script
    from .test_parser import module_stub_script

    def simulate_package(name: str, path: str, *, link: bool) -> str:
        """Mock the module and stubs.

        The path will be the parent of the module folder.
        """
        __import__(name)
        path = abspath(path)
        with open(join(path, name.split('.')[-1] + '.py'), 'w') as f:
            f.write(script)
        with open(join(path, name.split('.')[-1] + '-stubs.pyi'), 'w') as f:
            f.write(stub_script)

# Generated at 2022-06-13 17:43:51.585354
# Unit test for function loader
def test_loader():
    """Test function: loader."""
    result = loader('numpy', __file__.parent, link=False, level=1, toc=False)
    assert not result.strip(), 'loader() should return empty text'

# Generated at 2022-06-13 17:43:58.401331
# Unit test for function loader
def test_loader():
    """Test for function loader."""
    # Load a module
    module_name = 'pyslvs_ui.info'
    path = parent(__file__) + '\\info.py'
    p = Parser.new()
    logger.debug(path)
    p.parse(module_name, _read(path))
    p.parse('pyslvs_ui.info.__init__', '')
    p.parse('pyslvs', '')
    # Load a package
    package_name = 'pyslvs_ui'
    path = parent(path) + '\\__init__.py'
    logger.debug(path)
    p.parse(package_name, _read(path))
    # Load a package with submodule
    package_name = 'pyslvs'
    path = parent

# Generated at 2022-06-13 17:44:06.076177
# Unit test for function loader
def test_loader():
    from .docstring import Docstring
    from . import exceptions

    with exceptions.suppress(exceptions.FileNotFoundError):
        os.remove('./docs/pyslvs-api.md')

    t = time.perf_counter()
    p = Parser.new(False, 1, True)
    assert str(p)

    assert _site_path('pyslvs')
    assert not _site_path('pyslvs-not-exist')
    assert _load_module('pyslvs.structures',
                        './build/lib.linux-x86_64-3.8/pyslvs/structures.cpython-38-x86_64-linux-gnu.so', p)

# Generated at 2022-06-13 17:44:14.247453
# Unit test for function loader
def test_loader():
    def sys_path_inject(pwd: str) -> None:
        sys_path.append(abspath(pwd))
        logger.info(f"Directory appended to `sys.path` : {pwd}")

    def read_module(name: str) -> str:
        with open(find_spec(name).origin, 'r', encoding='utf-8') as f:
            return f.read()

    logger.info("Test data 1 (`demo_package`)")
    sys_path_inject('demo_package')
    assert loader('demo_package', dirname(__file__)) == read_module('demo_package')

    logger.info("Test data 2 (`svgstatistics`)")
    sys_path_inject('.')

# Generated at 2022-06-13 17:44:20.260790
# Unit test for function loader
def test_loader():
    from .var import PYDOC_TEST_FILE
    p = Parser.new(True, 1, False)
    p.parse("test_parser", _read(PYDOC_TEST_FILE))

# Generated at 2022-06-13 17:45:14.713316
# Unit test for function loader
def test_loader():
    import os
    import sys
    import doctest
    from io import StringIO
    from .parser import parse_link

    def runner(doc, globs):
        save_stdout = sys.stdout
        save_stderr = sys.stderr
        try:
            sys.stdout = StringIO()
            sys.stderr = StringIO()
            failures, _ = doctest.testmod(globs=globs)
            sys.stdout.seek(0)
            sys.stderr.seek(0)
            out = sys.stdout.read() + sys.stderr.read()
            if failures:
                print(doc)
                print(out)
        finally:
            sys.stdout = save_stdout
            sys.stderr = save_stderr
        assert failures == 0

# Generated at 2022-06-13 17:45:19.606802
# Unit test for function walk_packages
def test_walk_packages():
    from pathlib import Path
    from .main import lvs_root
    for name, path in walk_packages('_compiler', lvs_root):
        assert name == 'pyslvs_ui.info.compiler'
        assert str(Path(path).relative_to(lvs_root)) == 'docs/info/compiler.py'

# Generated at 2022-06-13 17:45:21.371859
# Unit test for function loader
def test_loader():
    doc = loader("pyslvs", "tests", False, 2, False)
    assert '## API' in doc

# Generated at 2022-06-13 17:45:26.281619
# Unit test for function walk_packages
def test_walk_packages():
    """Test function `walk_packages`."""
    for name, path in walk_packages('..', 'test'):
        print(f"'{name}' at '{path}'")


if __name__ == "__main__":
    import sys
    gen_api({
        "pySolveFEM": "pySolveFEM"
    }, sys.path[0], prefix='tmp', dry=True)
    test_walk_packages()

# Generated at 2022-06-13 17:45:31.123074
# Unit test for function walk_packages
def test_walk_packages():
    """Test walk_packages."""
    from sys import path as sys_path
    from os import getcwd

    def update_path(path: str):
        sys_path.append(abspath(path))

    update_path(parent(getcwd()))
    update_path(parent(parent(getcwd())))
    for name, path in walk_packages("pyslvs_ui", "pyslvs_ui/testdata/site"):
        logger.info(f"walk_packages: {name} <= {path}")



# Generated at 2022-06-13 17:45:34.991044
# Unit test for function walk_packages
def test_walk_packages():
    pwd = abspath(__file__)
    for name, path in walk_packages('pyslvs', pwd):
        logger.debug(f"name = {name}, path = {path}")



# Generated at 2022-06-13 17:45:35.898205
# Unit test for function loader
def test_loader():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 17:45:42.557284
# Unit test for function loader
def test_loader():
    """Test function loader."""
    assert """
| Name | Description |
| --- | --- |
| [`test.test_test`](https://docs.python.org/3/library/test.html#module-test.test_test) | Tests [`test.py`](https://github.com/python/cpython/blob/3.8/Lib/test/test_test.py) |
""".strip() == loader("test", "test.test_test", True, 1, False).strip()


__all__ = ['gen_api']

# Generated at 2022-06-13 17:45:48.441730
# Unit test for function walk_packages
def test_walk_packages():
    """Test for function walk_packages."""
    assert list(walk_packages('t', './t')) == [
        ('t', './t/t.py'),
        ('t.__init__', './t/__init__.py'),
        ('t.c', './t/c.py'),
        ('t.c.__init__', './t/c/__init__.py'),
        ('t.c.d', './t/c/d.py'),
        ('t.e', './t/e.py'),
    ]

# Generated at 2022-06-13 17:45:51.000316
# Unit test for function loader
def test_loader():
    """Test the loader function."""
    from pathlib import Path
    from .utils import EXE_DIR
    from .config import API_ROOT
    root = API_ROOT
    # Test package name
    name, path = list(walk_packages(root, EXE_DIR))[0]
    assert name == root
    assert str(Path(path).parent) == str(Path(EXE_DIR) / root)

# Generated at 2022-06-13 17:48:04.848903
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    p = Parser.new()
    name = 'pyslvs_ui'
    path = '/usr/local/lib/python3.8/dist-packages/pyslvs_ui/main.py'
    logger.debug(f"{name} <= {path}")
    p.parse(name, _read(path))
    logger.debug(f"loading extension module for fully documented:")
    path = '/usr/local/lib/python3.8/dist-packages/pyslvs_ui/main.cpython-38-x86_64-linux-gnu.so'
    logger.debug(f"{name} <= {path}")
    _load_module(name, path, p)
    print(p.compile())



# Generated at 2022-06-13 17:48:15.154772
# Unit test for function loader
def test_loader():
    def _test_parse(
        name: str,
        path: str,
        link: bool = False,
        level: int = 2,
        toc: bool = False
    ) -> None:
        print(name + ":" + path)
        doc = Parser.new(link, level, toc).parse(name, _read(path))
        print(doc.compile())

    # Simply unit test for module
    test_path = join(dirname(abspath(__file__)), "../..")
    _test_parse("pyslvs", join(test_path, "pyslvs/__init__.py"))

    # Simply unit test for package
    _test_parse("pyslvs.core", join(test_path, "pyslvs/core/__init__.py"))

# Generated at 2022-06-13 17:48:17.183787
# Unit test for function loader
def test_loader():
    assert loader('pyslvs', 'tests', True, 1, False)
    assert loader('pyslvs', 'tests', True, 2, False)

# Generated at 2022-06-13 17:48:24.394954
# Unit test for function walk_packages
def test_walk_packages():
    """Tests for function walk_packages."""
    import pyslvs
    assert not isfile('_test.py')

# Generated at 2022-06-13 17:48:29.834393
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from unittest import TestCase
    from .parser import Parser
    from .parser import Nested, Text, Link
    from .parser import AnchoredHead
    from .parser import Syntax, Type, Arguments, Signatures, Returns

    class T(TestCase):
        """Test class."""

        # pylint: disable=E1101,W0613

        def test_parse(self):
            """Test load parser."""
            p = Parser.new()
            p.parse('test', 'test')
            self.assertTrue('test' in p.root.nodes)
            self.assertTrue(isinstance(p.root.nodes['test'], Nested))
            self.assertTrue(isinstance(p.root.nodes['test'].doc, Text))
           

# Generated at 2022-06-13 17:48:35.540551
# Unit test for function loader
def test_loader():
    from pkgutil import get_loader
    root, pwd = 'xml', dirname(abspath(__file__))
    assert get_loader(root) is not None
    assert loader(root, pwd, False, 2, False).strip()
    assert loader(root, pwd, True, 2, False).strip()
    loader(root, pwd, False, 2, True)  # No assert

if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:48:45.180230
# Unit test for function loader
def test_loader():
    pwd = r"D:\Users\yuan\Documents\GitHub\Qt.py\Qt"
    p = Parser.new(True, 1, False)
    for name, path in walk_packages("Qt", pwd):
        logger.debug(f"{name} <= {path}")
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


# Generated at 2022-06-13 17:48:53.952671
# Unit test for function loader
def test_loader():
    from pkgutil import walk_packages
    from tempfile import TemporaryDirectory
    from shutil import copy, copytree
    from .parser import _make_link

    # Create temp dirs
    with TemporaryDirectory() as temp:
        with TemporaryDirectory() as temp2:
            # To create project's dirs
            for d in ['a', 'a.b', 'a.b.c']:
                mkdir(join(temp, *d.split('.')))
            # To create link target
            for d in ['a', 'a.b']:
                mkdir(join(temp2, *d.split('.')))
            # Make script files

# Generated at 2022-06-13 17:48:57.977718
# Unit test for function loader
def test_loader():
    import PIL # pylint: disable=import-error
    PIL_NAME = 'PIL'
    load_path = _site_path(PIL_NAME)
    assert load_path
    # No need to parse PIL source code,
    # as it may not be installed in some environments.
    doc = loader(PIL_NAME, load_path, False, 0, False)
    assert PIL_NAME in doc

# Generated at 2022-06-13 17:49:02.348499
# Unit test for function loader
def test_loader():
    pwd = dirname(dirname(abspath(__file__)))
    loader('core', pwd)
    loader('core', pwd, link=False)
    loader('core', pwd, toc=True)
    loader('core', pwd, level=2)
    gen_api({'core': 'core'}, pwd, dry=True)
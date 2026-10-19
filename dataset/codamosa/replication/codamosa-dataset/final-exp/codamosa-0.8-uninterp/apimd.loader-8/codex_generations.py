

# Generated at 2022-06-13 17:40:32.790750
# Unit test for function walk_packages
def test_walk_packages():
    """Test for function walk_packages."""
    for name, path in walk_packages("pyslvs", "pyslvs"):
        logger.info(f"{name} <= {path}")


# Generated at 2022-06-13 17:40:38.365679
# Unit test for function loader
def test_loader():
    from pprint import pformat
    from .parser import Parser
    p = Parser.new(True, 3, False)
    for name, path in walk_packages("pyslvs_ui", join(dirname(__file__), "..")):
        # Load its source or stub
        for ext in [".py", ".pyi"]:
            path_ext = path + ext
            if not isfile(path_ext):
                continue
            p.parse(name, open(path_ext, 'r').read())
            break
        else:
            logger.debug(f"loading extension module for fully documented:")
            # Try to load module here
            for ext in EXTENSION_SUFFIXES:
                path_ext = path + ext
                if not isfile(path_ext):
                    continue

# Generated at 2022-06-13 17:40:42.758055
# Unit test for function walk_packages
def test_walk_packages():
    from unittest import TestCase

    class TestCase(TestCase):
        def setUp(self):
            mkdir('test_walk_packages')
            _write('test_walk_packages/__init__.py', '')
            _write('test_walk_packages/package.py', '')
            _write('test_walk_packages/foo/__init__.py', '')
            _write('test_walk_packages/foo/bar.py', '')
            _write('test_walk_packages/foo/bar.pyi', '')
            _write('test_walk_packages/foo/baz.py', '')
            _write('test_walk_packages/foo/baz.pyi', '')


# Generated at 2022-06-13 17:40:46.856533
# Unit test for function walk_packages
def test_walk_packages():
    assert list(walk_packages('', 'tests')) == [
        ('module', 'tests/module.py')
    ]

# Generated at 2022-06-13 17:40:50.011549
# Unit test for function walk_packages
def test_walk_packages():
    from unittest import TestCase, main
    TEST_PATH = abspath(join(dirname(abspath(__file__)), 'test'))
    class TestWalker(TestCase):
        """Test file walker."""
        def test_path(self):
            """Test the path search."""
            for name, path in walk_packages('test', TEST_PATH):
                self.assertEqual(name, 'test.foo')
                self.assertTrue(path.endswith('test/foo.py'))

    main()


if __name__ == '__main__':
    test_walk_packages()

# Generated at 2022-06-13 17:40:57.485770
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from importlib import util
    import pyslvs as mod
    module_path = util.find_spec(mod.__name__).origin
    module_path = parent(module_path)
    parser = Parser.new()
    for name, path in walk_packages(mod.__name__, module_path):
        logger.info(f"{name} <= {path}")
        for ext in [".py", ".pyi"]:
            path_ext = path + ext
            if not isfile(path_ext):
                continue
            parser.parse(name, _read(path_ext))
    logger.info('=' * 12)
    logger.info(parser.compile())

# Generated at 2022-06-13 17:41:03.889493
# Unit test for function loader
def test_loader():
    test_name = "__main__"
    main_path = __file__.replace(".py", ".md")
    _write(main_path, loader(test_name, dirname(__file__), True, 3, False))
    logger.info(f"Write file: {main_path}")
    test_name = "__builtin__"
    pwd = _site_path(test_name)
    if pwd == "":
        logger.info(f"{test_name} can not be loaded")
    else:
        built_path = join(dirname(__file__), f"{test_name}.md")
        _write(built_path, loader(test_name, pwd, True, 3, False))
        logger.info(f"Write file: {built_path}")
    test_name

# Generated at 2022-06-13 17:41:08.625391
# Unit test for function walk_packages
def test_walk_packages():
    """Test function walk_packages."""
    assert list(walk_packages('root', './test/test_module')) == [
        ('root.a.b', './test/test_module/root/a/b.py'),
    ]
    assert list(walk_packages('root2', './test/test_module')) == [
        ('root2.c.d', './test/test_module/root2/c/d.py'),
    ]

# Generated at 2022-06-13 17:41:09.660995
# Unit test for function loader
def test_loader():
    print(loader("matplotlib", "..", False))


# Generated at 2022-06-13 17:41:13.126452
# Unit test for function walk_packages
def test_walk_packages():
    root = r'D:\Coding\Python\PySlvs\pyslvs_ui\widgets'
    pwd = r'D:\Coding\Python\PySlvs\pyslvs_ui'
    print(list(walk_packages(root, pwd)))


# Generated at 2022-06-13 17:42:29.626841
# Unit test for function loader
def test_loader():
    from os import path
    from pkgutil import extend_path
    from .logger import logger
    from .parser import parent, Parser
    p = Parser(True, 2, False)

    def load_ext(name: str, path: str) -> None:
        __import__(parent(name))
        s = find_spec(name, path)
        if s is not None:
            m = s.loader.load_module(name)
            p.load_docstring(name, m)

    load_ext('py2d_engine', [path.dirname(path.abspath(__file__))])
    print(p.compile())

# Generated at 2022-06-13 17:42:32.323190
# Unit test for function loader
def test_loader():
    """Dry run."""
    logger.info("Walk package: Pyslvs")
    for name, path in walk_packages("pyslvs", "../Pyslvs"):
        logger.info(f"{name} <= {path}")


# Generated at 2022-06-13 17:42:34.704518
# Unit test for function loader
def test_loader():
    # Use * instead of ** for Python 3.5 support
    assert "empty" in gen_api(dict(empty='empty_module'), '.', link=False, toc=False, dry=True)[0]


if __name__ == "__main__":
    test_loader()

# Generated at 2022-06-13 17:42:45.313263
# Unit test for function walk_packages
def test_walk_packages():
    from tempfile import TemporaryDirectory
    from shutil import rmtree
    with TemporaryDirectory() as d:
        path = f'{d}{sep}my_package{sep}'
        mkdir(path)
        with open(f'{path}__init__.py', 'w') as f:
            f.write("def test(): pass")
        with open(f'{path}sub_package{sep}__init__.py', 'w') as f:
            f.write("def test(): pass")
        with open(f'{path}sub_package{sep}module.py', 'w') as f:
            f.write("def test(): pass")

# Generated at 2022-06-13 17:42:47.500879
# Unit test for function walk_packages
def test_walk_packages():
    from .debug import Test
    with Test("_site_path"):
        assert _site_path("importlib")
    with Test("walk_packages"):
        assert tuple(walk_packages("importlib", _site_path("importlib")))

# Generated at 2022-06-13 17:42:58.612878
# Unit test for function walk_packages
def test_walk_packages():
    """Test function walk_packages."""
    # Walk one file
    assert len(list(walk_packages('numpy', r'C:\Python37\Lib\site-packages'))) == 1
    # Walk all files
    assert len(list(walk_packages('numpy', r'C:\Python37\Lib\site-packages\numpy'))) == 4
    # Walk error
    assert len(list(walk_packages('numpy', r'C:\Python37\Lib\site-packages\numpy\n'))) == 0
    # Walk one sys path
    assert len(list(walk_packages('numpy', r'C:\Python37\Lib\site-packages\numpy'))) >= 1
    # Walk all sys path
    assert len(list(walk_packages('numpy', r'C:\Python37\Lib'))) >= 1
   

# Generated at 2022-06-13 17:43:08.303253
# Unit test for function loader
def test_loader():
    import tempfile
    with tempfile.TemporaryDirectory() as pwd:
        c = (
            "import sys\n"
            "sys.path.append('..')\n\n"
            "class A:\n"
            "    '''A test document.'''\n"
            "    pass"
        )
        _write(join(pwd, 'A.py'), c)
        _write(
            join(pwd, '__init__.py'),
            "from .A import *"
        )
        print('=' * 12)
        print(loader('A', pwd, False, 1, False))

# Generated at 2022-06-13 17:43:12.699668
# Unit test for function walk_packages
def test_walk_packages():
    def assert_equal(a: tuple, b: tuple):
        assert a[0] == b[0]
        assert a[1] == b[1]

    assert_equal(next(walk_packages('pkgutil', 'pkgutil')),
                 ('pkgutil.__main__', 'pkgutil/__main__.py'))
    assert_equal(next(walk_packages('pkgutil', 'site-packages')),
                 ('pkgutil.__main__', 'pkgutil/__main__.py'))
    assert_equal(next(walk_packages('pkgutil', 'site-packages.pkgutil')),
                 ('pkgutil.__main__', 'pkgutil/__main__.py'))

# Generated at 2022-06-13 17:43:15.996042
# Unit test for function loader
def test_loader():
    from pyslvs_ui.package import __path__
    print(loader('solver', __path__[0], False, 1, False))



# Generated at 2022-06-13 17:43:26.266033
# Unit test for function loader
def test_loader():
    """Function loader unit test."""
    from mock import patch
    from sys import path
    from os.path import dirname
    from .parser import Parser
    from .colorlog import colorlog
    from .logger import logger_init, logger_deinit

    logger_init(colorlog.logging.DEBUG)
    path.insert(0, dirname(__file__))
    with patch('importlib.util.find_spec'):
        p = Parser.new(True, 1, True)
        with patch('importlib.abc.Loader'), patch('importlib.machinery.EXTENSION_SUFFIXES', ['.so']):
            assert not _load_module('test', 'test', p)
        with patch('importlib.abc.Loader') as mock_loader:
            mock_loader.return_value = None

# Generated at 2022-06-13 17:44:19.358155
# Unit test for function walk_packages
def test_walk_packages():
    from unittest import TestCase, main
    from tempfile import NamedTemporaryFile, TemporaryDirectory
    from shutil import rmtree
    from os import remove
    from os.path import dirname, basename
    from importlib.util import module_from_spec, spec_from_file_location

    class TestWalkPackages(TestCase):

        def setUp(self) -> None:
            self.temp = TemporaryDirectory()
            self.temp_file = NamedTemporaryFile('w', encoding='utf-8')

        def tearDown(self) -> None:
            self.temp_file.close()
            rmtree(self.temp.name)


# Generated at 2022-06-13 17:44:22.856517
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    logger.info("Load modules")
    loader('pybimstab', _site_path('pybimstab'), True, 1, False)


if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:44:33.915226
# Unit test for function loader
def test_loader():
    dummy_path = '/dummy'
    docs = loader('dummy', dummy_path, True, 1, True).strip()
    docs_link = loader('dummy', dummy_path, True, 1, False).strip()
    assert 'dummy.pyi' in docs
    assert '[dummy](dummy.html)' in docs
    assert 'dummy.pyi' in docs_link
    assert '[dummy](dummy.html)' in docs_link
    docs = loader('dummy', dummy_path, False, 1, True).strip()
    docs_lack = loader('dummy', dummy_path, False, 1, False).strip()
    assert 'dummy.pyi' in docs
    assert 'dummy.pyi' in docs_lack
    assert '[dummy](dummy.html)' not in docs

# Generated at 2022-06-13 17:44:43.970095
# Unit test for function loader
def test_loader():
    """Test function `loader`."""
    from importlib import reload
    from pkgutil import get_data
    from .parser import Parser
    from .template import get_theme
    import sys
    import os
    import platform
    import pytest
    logger.info(f"System: {platform.system()}")
    logger.info(f"Python: {sys.version}")
    # Remove stubs if exist
    try:
        import xml
        import xml.stubs
        logger.info(f"Uninstall stub: {xml.stubs.__spec__.name}")
        del xml.stubs
    except ImportError:
        pass
    os.chdir(os.path.dirname(__file__))
    sys.path.append('./data')
    # Test without stubs
    p = Pars

# Generated at 2022-06-13 17:44:51.143308
# Unit test for function walk_packages
def test_walk_packages():
    from tempfile import TemporaryDirectory
    from shutil import rmtree
    from os import chdir
    with TemporaryDirectory() as td:
        chdir(td)
        mkdir("a")
        mkdir("a/b")
        mkdir("a/b/c")
        mkdir("a/b/c/d")
        mkdir("a-stubs")
        mkdir("a-stubs/b")
        mkdir("a-stubs/b/c")
        mkdir("a-stubs/b/c/d")
        with open("a/b/c/d/e.py", 'w+') as f:
            f.write("def test1(): pass")

# Generated at 2022-06-13 17:44:57.101573
# Unit test for function loader
def test_loader():
    def test_py(name: str, path: str) -> None:
        logger.debug(f"{name} <= {path}")
        assert find_spec(name) is not None

    def test_ext(name: str, path: str) -> None:
        logger.debug(f"{name} <= {path}")
        assert find_spec(name) is not None

    p = Parser.new(True, 1, False)
    for name, path in walk_packages("pyslvs", r"..\.."):
        test_py(name, path + ".py")
        test_ext(name, path)

# Generated at 2022-06-13 17:45:00.583104
# Unit test for function loader
def test_loader():
    """Test for compiler."""
    logger.setLevel("DEBUG")
    result = loader("pyslvs", "./pyslvs", True, 2, False)
    print(result)



# Generated at 2022-06-13 17:45:03.398141
# Unit test for function loader
def test_loader():
    path = join(dirname(__file__), "test")
    sys_path.append(path)
    text = loader("test", path, link=False, level=1, toc=False)
    assert "## test" in text
    assert "### sub1" in text
    assert "### sub2" in text
    assert "### sub_module" in text

# Generated at 2022-06-13 17:45:08.235501
# Unit test for function loader
def test_loader():
    import sys
    import os
    import site
    site_path = [os.path.abspath(p) + os.sep for p in site.getsitepackages()]
    def search_path(path: str, sub: str) -> str:
        for p in site_path:
            if path.startswith(p):
                for root, dirs, _ in os.walk(p):
                    for d in dirs:
                        if d.startswith(sub):
                            return root
        raise RuntimeError(f"can't find path of {path}")
    def test_path(path: str) -> None:
        if not os.path.isfile(path):
            return

# Generated at 2022-06-13 17:45:12.900297
# Unit test for function loader
def test_loader():
    from .extension import __name__ as name
    doc = loader(name, dirname(__file__), False, 1, False)
    print('=' * 12 + f" {name} API " + '=' * 12)
    print(doc)


if __name__ == "__main__":
    from .extension import __name__ as name
    test_loader()

# Generated at 2022-06-13 17:47:25.058618
# Unit test for function loader
def test_loader():
    import os
    import locale
    import sys
    import pyslvs
    import pyslvs_ui
    root_names = {
        'Pyslvs': 'pyslvs',
        'Pyslvs-UI': 'pyslvs_ui',
    }
    os.chdir(os.getcwd())
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'examples'))
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    for title, name in root_names.items():
        logger.info(f"Load root: {name} ({title})")

# Generated at 2022-06-13 17:47:33.817598
# Unit test for function walk_packages
def test_walk_packages():
    import unittest
    from tempfile import TemporaryDirectory

    class WalkerTest(unittest.TestCase):

        def setUp(self):
            self.tmp_dir = TemporaryDirectory(prefix="slvs-")
            self.path = self.tmp_dir.name + sep

        def tearDown(self):
            self.tmp_dir.cleanup()

        def test_walk_packages(self):
            import shutil
            from io import BytesIO
            # Copy "site-packages/solvespace" to temp dir
            shutil.copytree(
                _site_path('solvespace'),
                self.path + 'solvespace',
            )

# Generated at 2022-06-13 17:47:39.797153
# Unit test for function walk_packages
def test_walk_packages():
    import shutil
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(join(temp_dir, '__init__.py'), 'w+') as f:
            f.write('')
        with open(join(temp_dir, 'module.py'), 'w+') as f:
            f.write('')
        with open(join(temp_dir, 'module.pyi'), 'w+') as f:
            f.write('')
        shutil.rmtree(join(temp_dir, '__pycache__'))
        for name, path in walk_packages('module', temp_dir):
            assert name == 'module'
            assert dirname(path) == temp_dir


# Generated at 2022-06-13 17:47:49.362107
# Unit test for function loader
def test_loader():
    from .test_cases import package_path
    from .logger import logger
    from importlib import reload
    from sys import path as sys_path
    # Set logger level
    logger.setLevel('DEBUG')
    # Add test path to sys.path
    sys_path.insert(0, package_path)
    # Reload this module
    reload(__import__(__name__))
    # Make loader in global scope
    global loader
    from .parser import parse
    # Test
    doc = loader('test_package', package_path)

# Generated at 2022-06-13 17:47:55.475882
# Unit test for function loader
def test_loader():
    """Test function: loader()"""
    _loader = loader('PyQt5', '..', True, 1, False)
    assert '## PyQt5.QtCore' in _loader
    assert '## PyQt5.QtWidgets' in _loader
    assert '## PyQt5.uic' in _loader
    assert '## PyQt5.QtXmlPatterns' in _loader
    assert '## PyQt5.QtDesigner' not in _loader



# Generated at 2022-06-13 17:48:01.068431
# Unit test for function loader
def test_loader():
    assert _load_module(
        "pyslvs_ui.widgets.canvas",
        "/home/appveyor/miniconda/envs/testenv/lib/python3.7/site-packages/pyslvs_ui/widgets/canvas.cpython-37m-x86_64-linux-gnu.so",
        Parser.new(False, 1, True)
    )

# Generated at 2022-06-13 17:48:09.343677
# Unit test for function walk_packages
def test_walk_packages():
    l = []
    for name, path in walk_packages('pyslvs_ui', '../pyslvs_ui'):
        l.append((name, path))
    assert l[0] == ('pyslvs_ui',
                    '../pyslvs_ui/pyslvs_ui')
    assert l[-1] == ('pyslvs_ui.core.planar_editor',
                     '../pyslvs_ui/pyslvs_ui/core/planar_editor')
    # PEP 561
    l = []
    for name, path in walk_packages('cffi', '../cffi'):
        l.append((name, path))

# Generated at 2022-06-13 17:48:18.766743
# Unit test for function loader
def test_loader():
    import sys
    sys.path.append(r"D:\python\pyslvs-ui\pyslvs-ui.egg")
    sys.path.append(r"D:\pyslvs-ui")
    p = Parser.new()
    for name, path in walk_packages("pyslvs_ui", r"D:\python\pyslvs-ui\pyslvs_ui"):
        # Load its source or stub
        for ext in [".py", ".pyi"]:
            path_ext = path + ext
            if not isfile(path_ext):
                continue
            logger.debug(f"{name} <= {path_ext}")
            p.parse(name, _read(path_ext))
    print(p.compile())


# Generated at 2022-06-13 17:48:25.672332
# Unit test for function loader
def test_loader():
    """Test package searching algorithm."""
    p = Parser.new(True, 1, False)
    # Load root first to avoid import error
    __import__('pyslvs')
    # local:
    p.parse('pyslvs', _read('pyslvs.pyi'))
    # site-packages:
    s = spec_from_file_location('pyslvs', 'C:/Program Files/Python 38/Lib/site-packages/pyslvs.pyi')
    s.loader.exec_module(module_from_spec(s))
    p.load_docstring('pyslvs', module_from_spec(s))
    # local:
    p.parse('pyslvs.ui', _read('pyslvs/ui.pyi'))
    # site-packages:


# Generated at 2022-06-13 17:48:35.967577
# Unit test for function loader
def test_loader():
    assert loader('tests.example', '.', True, 1, False).strip()
    assert loader('tests.path', '.', True, 1, False).strip()
    assert loader('tests.attr_doc', '.', True, 1, False).strip()
    assert loader('tests.doc', '.', True, 1, False).strip()
    assert loader('tests.script', '.', True, 1, False).strip()
    assert loader('tests.script2', '.', True, 1, False).strip()
    assert loader('tests.script3', '.', True, 1, False).strip()
    assert loader('tests.script4', '.', True, 1, False).strip()
    assert loader('tests.script5', '.', True, 1, False).strip()
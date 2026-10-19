

# Generated at 2022-06-13 17:41:11.481827
# Unit test for function walk_packages
def test_walk_packages():
    for name, path in walk_packages('pyslvs', '.'):
        print(name, path)
    assert next(walk_packages('pyslvs', '.')) == ('pyslvs', './pyslvs.py')

# Generated at 2022-06-13 17:41:22.248085
# Unit test for function loader
def test_loader():
    """Test the loader."""
    from os import remove
    from os.path import sep
    from shutil import rmtree
    from tempfile import TemporaryDirectory
    
    def _assert_str(a: str, b: str) -> None:
        assert a == b, f"{a!r} != {b!r}"

    with TemporaryDirectory() as d:
        # Create a fake module
        m_dir = join(d, "fake_module")

# Generated at 2022-06-13 17:41:28.656425
# Unit test for function walk_packages
def test_walk_packages():
    def __(s: str) -> str:
        return str(s)

# Generated at 2022-06-13 17:41:30.530997
# Unit test for function loader
def test_loader():
    """Test the loader function."""
    assert isinstance(loader('pkgutil', '.', False, 3, False), str)

# Generated at 2022-06-13 17:41:36.947095
# Unit test for function walk_packages
def test_walk_packages():
    root_name = 'test'
    root_path = './test'
    package_name = 'test.test1'
    package_path = './test/test1'
    file_name = 'test.test1.test2'
    file_path = './test/test1/test2.py'
    stub_name = 'test.test1.test2-stubs'
    stub_path = './test/test1/test2-stubs.py'
    names = []
    paths = []
    for n, p in walk_packages(root_name, root_path):
        names.append(n)
        paths.append(p)

# Generated at 2022-06-13 17:41:41.976993
# Unit test for function loader
def test_loader():
    """Test for `loader`."""
    from unittest import TestCase, mock
    from pkgutil import get_loader
    from os.path import basename
    import pyslvs_ui
    
    class Test(TestCase):
        def test(self):
            """Test for `pyslvs_ui`."""
            self.assertIsNotNone(get_loader(parent(basename(pyslvs_ui.__file__))))
            self.assertIsNotNone(loader('pyslvs_ui', _site_path('pyslvs_ui'), True, 2, False))


# Generated at 2022-06-13 17:41:48.693963
# Unit test for function walk_packages
def test_walk_packages():
    """The argument `pwd` must be absolute path."""
    import unittest

    class WalkPackagesTest(unittest.TestCase):

        """Test for walk_packages."""

        def test_none_exist_root(self):
            """Test for non-exist root."""
            root = 'non_exist_root'
            pwd = dirname(__file__)
            r = walk_packages(root, pwd)
            self.assertListEqual(list(r), [])

        def test_empty_root(self):
            """Test for empty root."""
            root = ''
            pwd = dirname(__file__)
            r = walk_packages(root, pwd)
            self.assertListEqual(list(r), [])


# Generated at 2022-06-13 17:41:53.732330
# Unit test for function loader
def test_loader():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from shutil import copytree

    with TemporaryDirectory() as temp:
        temp = Path(temp)
        copytree(Path(__file__).parent.parent / 'sphobjwl', temp)
        loader('sphobjwl', str(temp))


if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:42:00.906355
# Unit test for function loader
def test_loader():
    import pkgutil
    from .parser import parse_docstring
    from .highlight import wiki, pyslvs
    import pyslvs
    from .__main__ import parse_argv

    parser_args = parse_argv([
        '-v',
        '--link', 'wiki'
    ])
    p = Parser.new(
        parser_args.link,
        parser_args.level,
        parser_args.toc,
        [wiki],
        [pyslvs]
    )
    for importer, _, is_pkg in pkgutil.walk_packages(pyslvs.__path__):
        for name, path in walk_packages('', importer.path + sep):
            if name == ".":
                continue

# Generated at 2022-06-13 17:42:02.316960
# Unit test for function loader
def test_loader():
    """Test code is located in the `tests` directory."""
    print(loader("lark", "../tests", False, None, False))

# Generated at 2022-06-13 17:43:55.408601
# Unit test for function walk_packages
def test_walk_packages():
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as td:
        for _ in range(2):
            for path in ["package", "package" + PEP561_SUFFIX]:
                mkdir(join(td, path))
                for _ in range(2):
                    with open(join(td, path, 'a.py'), 'w+'):
                        with open(join(td, path, 'b.pyi'), 'w+'):
                            pass
        for _, path in walk_packages("package", td):
            if PEP561_SUFFIX in path:
                assert path.endswith(PEP561_SUFFIX)
                assert not isfile(path.replace(PEP561_SUFFIX, ""))
            else:
                assert isfile(path)

# Generated at 2022-06-13 17:44:01.392823
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    import json
    import pyslvs_ui
    loader = pyslvs_ui.__path__[0]
    doc = loader('pyslvs_ui', loader, False, 2, False)
    assert doc.startswith('## Pyslvs_ui API\n\n')
    doc = loader('pyslvs', pyslvs_ui.__path__[0], False, 2, False)
    assert doc.startswith('## Pyslvs API\n\n')
    with open(join(pyslvs_ui.__path__[0], 'api.json'), 'r', encoding='utf-8') as f:
        api = json.load(f)

# Generated at 2022-06-13 17:44:11.104430
# Unit test for function walk_packages
def test_walk_packages():
    """Test result of walk_packages()."""
    assert tuple(walk_packages('math', '.')) == (
        ('math', './math'),
        ('math.__init__', './math/__init__.py'),
        ('math.__init__', './math/__init__.pyi'),
        ('math.sqrt', './math/sqrt.py')
    )
    assert tuple(walk_packages('math', './math')) == (
        ('math.__init__', './math/__init__.py'),
        ('math.__init__', './math/__init__.pyi'),
        ('math.sqrt', './math/sqrt.py')
    )

# Generated at 2022-06-13 17:44:16.863943
# Unit test for function loader
def test_loader():
    p = Parser.new(True, 1, False)
    import numpy
    s = find_spec('numpy.core._multiarray_umath')
    assert s is not None
    m = module_from_spec(s)
    s.loader.exec_module(m)
    p.load_docstring('numpy.core._multiarray_umath', m)
    doc = p.compile()
    assert doc
    assert 'numpy.core._multiarray_umath' in doc
    assert 'numpy.multiarray' in doc
    assert 'multiarray' in doc
    assert 'add' in doc

# Generated at 2022-06-13 17:44:23.023685
# Unit test for function loader
def test_loader():
    assert not loader('', '', False, 0, False).strip()
    assert not loader('pyslvs', '../pyslvs', False, 0, False).strip()
    assert loader('os', '', True, 1, True).strip()
    assert loader('os', '', True, 2, True).strip()



# Generated at 2022-06-13 17:44:30.910166
# Unit test for function loader
def test_loader():  # pragma: no cover
    import pkgutil
    import sys
    assert pkgutil.find_loader("pyslvs") is not None
    assert pkgutil.find_loader("pyslvs.ui") is not None
    assert pkgutil.find_loader("pyslvs_ui") is None
    loader("pyslvs", dirname(sys.modules["pyslvs"].__file__), False, 2, False)

# Generated at 2022-06-13 17:44:37.410955
# Unit test for function walk_packages
def test_walk_packages():
    from unittest import TestCase, main
    from tempfile import TemporaryDirectory
    from shutil import copytree

    class TestWalk(TestCase):

        def __init__(self, *args, **kwargs):
            super(TestWalk, self).__init__(*args, **kwargs)
            self.dir = TemporaryDirectory()

        def test_walk(self):
            path = abspath(self.dir.name)
            copytree('tests/data/pack', join(path, 'pack'))
            pkgs = dict()
            for name, _ in walk_packages('pack', path):
                pkgs[name] = True
            self.assertEqual(len(pkgs), 4)
            self.assertTrue('pack' in pkgs)

# Generated at 2022-06-13 17:44:43.078284
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from sys import path
    from os.path import dirname, join
    path.append(dirname(__file__))
    docs = gen_api(
        {
            "Compiler": "pyslvs_ui.packages.compiler",
        },
        join(dirname(__file__), '..', '..'),
        dry=True
    )
    assert len(docs) == 1

if __name__ == "__main__":
    test_loader()

# Generated at 2022-06-13 17:44:50.235380
# Unit test for function walk_packages
def test_walk_packages():
    """Test function`walk_packages`."""
    # Setup package
    import sys
    import shutil
    from tempfile import mkdtemp
    _pwd = mkdtemp()
    sys_path.append(_pwd)
    mkdir(join(_pwd, 'x'))
    mkdir(join(_pwd, 'x', 'y'))
    mkdir(join(_pwd, 'x', 'y', 'z'))
    with open(join(_pwd, 'x.py'), 'w+') as f:
        f.write("x = 0")
    with open(join(_pwd, 'x.pyi'), 'w+') as f:
        f.write("x: int")
    with open(join(_pwd, 'x', 'y.py'), 'w+') as f:
        f

# Generated at 2022-06-13 17:44:53.182880
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from os.path import dirname
    from . import __file__
    name = 'pyslvs'
    path = dirname(__file__)
    assert loader(name, path, True, 2, False)
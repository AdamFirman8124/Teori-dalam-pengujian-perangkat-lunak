

# Generated at 2022-06-13 17:43:41.174295
# Unit test for function loader
def test_loader():
    from sys import path
    from os.path import dirname, realpath
    from pkgutil import get_loader
    path += [
        dirname(dirname(dirname(realpath(__file__)))),
    ]
    tests = {
        'sys.path': [dirname(dirname(dirname(realpath(__file__))))],
        'sys.builtin_module_names': ['math'],
        'math': 'math',
        'math.pi': 'math.pi',
        'math.sin': 'math.sin',
        'math.factorial': 'math.factorial',
    }

    def __test(root_name: str, name: str):
        full_name = root_name + '.' + name
        loader = get_loader(full_name)
        path = ''

# Generated at 2022-06-13 17:43:50.387272
# Unit test for function loader
def test_loader():
    assert loader('pyslvs', '/usr/local/lib/python3.7/dist-packages', False, 1, False)
    assert loader('pyslvs', '/usr/local/lib/python3.7/dist-packages', False, 1, True)
    assert loader('pyslvs', '/usr/local/lib/python3.7/dist-packages', True, 1, False)
    assert loader('pyslvs', '/usr/local/lib/python3.7/dist-packages', True, 1, True)
    assert loader('pyslvs', '/usr/local/lib/python3.7/dist-packages', False, 2, False)
    assert loader('pyslvs', '/usr/local/lib/python3.7/dist-packages', False, 2, True)

# Generated at 2022-06-13 17:43:56.595242
# Unit test for function walk_packages
def test_walk_packages():
    def _walker(name: str, path: str):
        yield name, path
        yield f".{name}", path
        yield f"{name}", parent(path)
        yield f"{name}.__init__", parent(path)


# Generated at 2022-06-13 17:44:00.545542
# Unit test for function walk_packages
def test_walk_packages():
    """Unit test for function: walk_packages"""
    names = list(walk_packages("docs", "."))
    print("root names:")
    print("\n".join(f" - {name}" for name, _ in names))
    assert names[0] == (
        ".__main__",
        abspath(".") + sep + ".__main__.py"
    )
    assert any(p.endswith("site-packages/docs/__init__.pyi") for _, p in names)

# Generated at 2022-06-13 17:44:07.336769
# Unit test for function loader
def test_loader():
    from importlib import import_module
    from .test_data import ALL_ROOT, ALL_PATH
    from .test_data import pwd, link, level, toc

    for name in ALL_ROOT:
        assert import_module(name).__version__

    for name in ALL_ROOT:
        assert _site_path(name) == ALL_PATH

    for name in ALL_ROOT:
        doc = loader(name, pwd, link, level, toc)
        assert doc.strip()



# Generated at 2022-06-13 17:44:15.393219
# Unit test for function loader
def test_loader():
    """Test the function loader."""
    # File path
    f = join(dirname(__file__), "test_code")
    # Module `point`
    p = Parser.new(True, 1, False)
    p.parse("point", _read(join(f, "point.py")))
    assert p.compile() == _read(join(f, "point.md"))
    # Module `line`
    p = Parser.new(True, 1, False)
    p.parse("line", _read(join(f, "line.py")))
    assert p.compile() == _read(join(f, "line.md"))
    # Module `circle`
    p = Parser.new(True, 1, False)

# Generated at 2022-06-13 17:44:22.143334
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    p = Parser.new(True, 2, False)
    _load_module('test', './tests/test.py', p)
    print(p.compile())
    p.clear()
    p.parse('test', _read('./tests/test.py'))
    print(p.compile())



# Generated at 2022-06-13 17:44:29.261577
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from os import remove
    from tempfile import TemporaryDirectory
    from shutil import copyfile
    from pkg_resources import require
    require('pyslvs')
    require('pyslvs_ui')
    require('solvespace')
    with TemporaryDirectory() as temp:
        test_file_list = ('pyslvs-stubs.pyi', 'pyslvs_ui.pyi', 'solvespace.pyi')
        for f in test_file_list:
            try:
                p = find_spec(f.removeprefix('-stubs'))
            except TypeError:
                remove(f)
            else:
                copyfile(p.submodule_search_locations[0], f)

# Generated at 2022-06-13 17:44:37.694307
# Unit test for function loader
def test_loader():
    r = loader(root="test", pwd="test", link=False, level=1, toc=False)

# Generated at 2022-06-13 17:44:45.680080
# Unit test for function loader
def test_loader():
    """Test function loader."""
    from os import chdir
    from os.path import isfile, dirname
    from contextlib import contextmanager
    from pyslvs import __path__ as path
    from pyslvs.logger import get_logger
    from .core.compiler import gen_api

    @contextmanager
    def _in_dir(d: str, fn):
        """Run a function in a directory and change back."""
        old_dir = dirname(__file__)
        chdir(d)
        fn()
        chdir(old_dir)

    @contextmanager
    def _log_file(_):
        """Create a logger with a log file."""
        get_logger('pyslvs-compiler-loader-test.log')
        yield


# Generated at 2022-06-13 17:47:32.775945
# Unit test for function loader
def test_loader():
    from unittest import TestCase, main

    class LoaderTest(TestCase):

        """Unit tests for functions in loader."""

        def test_walk_packages(self):
            """Test walk_packages."""
            self.assertEqual(list(walk_packages('abc', __file__)), [])
            self.assertEqual(list(walk_packages('', abspath(dirname(__file__)))), [
                ('', abspath(__file__)),
                ('loader-test', abspath(__file__)),
            ])

        def test_loader(self):
            """Test loader."""
            self.assertEqual(
                loader('abc', __file__, False, 1, False),
                ""
            )

# Generated at 2022-06-13 17:47:38.846261
# Unit test for function loader
def test_loader():
    """Test function loader."""
    doc = loader("aims", "test/libs/aims", True, 2)
    assert "## aims.geom.plane" in doc
    assert "### aims.geom.plane.intersection" in doc
    assert "### aims.geom.plane.project" in doc
    assert "## aims.geom.point" not in doc
    assert "## aims.materials.Material" in doc
    assert "### aims.materials.Material.plasma_frequency" in doc
    try:
        loader("omega", "test/libs/omega", True, 2)
    except AssertionError:
        pass
    else:
        raise AssertionError("Import error test fail")

# Generated at 2022-06-13 17:47:43.705393
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    print(loader(
        'pyslvs',
        # 'C:/Python38/Lib/site-packages/pyslvs',
        '.',
        True,
        1,
        False
    ))


if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:47:52.577687
# Unit test for function walk_packages
def test_walk_packages():
    core_path = join(abspath(dirname(__file__)), '..', '..', 'core')
    packages = []
    for name, path in walk_packages('core', core_path):
        packages.append((name, path))

# Generated at 2022-06-13 17:47:55.359689
# Unit test for function loader
def test_loader():
    """Test loader function."""
    d = {
        "abc": "abc",
        "abc.xyz": "abc.xyz",
        "__init__": "abc.__init__",
    }
    for k, v in d.items():
        assert loader(k, '.', True, 1, False).startswith(f"# {v}")



# Generated at 2022-06-13 17:48:04.149736
# Unit test for function loader
def test_loader():
    from tempfile import TemporaryDirectory
    from shutil import copy2
    from shutil import rmtree as remove
    from pathlib import Path

    def tmp_file(*paths: str) -> Path:
        return Path(tmp_dir) / Path("/".join(paths))

    tmp_dir = TemporaryDirectory().name
    root = "solve"
    pwd = str(tmp_file("other"))
    mkdir(pwd)
    copy2("../solve.py", pwd)
    copy2("../solve.pyi", tmp_file("solve.pyi"))
    docs = loader(root, pwd, False, 1, False)
    remove(tmp_dir)
    print(docs)
    assert "platform" in docs
    assert "solve.revision" in docs

# Generated at 2022-06-13 17:48:14.691768
# Unit test for function loader
def test_loader():
    test_str = '''
<?xml version="1.0" encoding="utf-8"?>
<!-- This file is automatically generated. Do not modify. To update, see https://github.com/pyslvs/pyslvs_ui/projects/6. -->
<!-- Doc-link: https://docs.python.org/3/library/xml.etree.elementtree.html -->
<!-- Code-link: https://github.com/python/cpython/blob/master/Lib/xml/etree/ElementTree.py -->
<api>
  <element name="Element">
    <meth>
    </meth>
    <prop>
    </prop>
  </element>
</api>'''

# Generated at 2022-06-13 17:48:20.782748
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from pyslvs import to_doc
    from unittest.mock import patch
    from os.path import isfile
    # Unit test for loader
    with patch('sys.argv', ['', '/dev/null', '-debug']):
        to_doc.main()
    assert isfile('docs/pyslvs-api.md')
    with patch('sys.argv', ['', '/dev/null', '-debug', '-dry']):
        to_doc.main()
    assert isfile('docs/pyslvs-api.md')

# Generated at 2022-06-13 17:48:23.743841
# Unit test for function walk_packages
def test_walk_packages():
    name = "pyslvs"
    root = find_spec(name).submodule_search_locations[0]
    c = list(walk_packages(name, dirname(root)))
    assert len(c) == 1
    assert c[0] == ('pyslvs', root)

# Generated at 2022-06-13 17:48:29.187433
# Unit test for function walk_packages
def test_walk_packages():
    root_path = 'P:/pyslvs-ui'
    good = [
        'pyslvs_ui.uie',
        'pyslvs_ui.list_widget',
        'pyslvs_ui.list_widget.__init__',
        'pyslvs_ui.ui_files.__init__',
    ]
    assert len(list(walk_packages('pyslvs_ui', root_path))) == len(good)
    for i, item in enumerate(walk_packages('pyslvs_ui', root_path)):
        assert i == 0 if item[0] == 'pyslvs_ui.uie' else i
        assert item[0] in good
        assert item[1].replace(sep, '/') in good
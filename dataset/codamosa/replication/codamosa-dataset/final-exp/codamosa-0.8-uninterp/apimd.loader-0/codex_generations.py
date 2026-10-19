

# Generated at 2022-06-13 17:44:25.807225
# Unit test for function loader
def test_loader():
    """Test the loader function."""
    logger.setLevel('DEBUG')
    # Load all the Python standard library's modules
    assert gen_api(
        {'standard library': 'std'},
        pwd=_site_path('std'),
        dry=True,
        toc=True
    )
    # Load scipy package
    assert gen_api(
        {'scipy': 'scipy'},
        pwd=_site_path('scipy'),
        dry=True,
        toc=True
    )
    # Load the package used by PySVGL
    assert gen_api(
        {'PySVGL': 'pysvgl'},
        pwd=_site_path('pysvgl'),
        dry=True,
        toc=True
    )
    #

# Generated at 2022-06-13 17:44:34.525801
# Unit test for function loader
def test_loader():
    # This link is used to make PEP561_SUFFIXes.
    link = 'https://github.com/pyslvs/pyslvs/blob/master/pyslvs/'
    p = Parser.new(link, 1, False)

    s = spec_from_file_location('test', __file__)
    assert s is not None
    assert isinstance(s.loader, Loader)
    m = module_from_spec(s)
    s.loader.exec_module(m)
    p.load_docstring('test', m)
    # __file__ == 'test.py'
    assert abspath(__file__) == abspath(__file__.removepostfix('.py'))
    assert p.parse('test', _read(__file__))
    # This module contains

# Generated at 2022-06-13 17:44:41.776348
# Unit test for function loader
def test_loader():
    """Test function loader with Sphinx docs."""
    # Sphinx is a standard Python libray
    import sphinx
    import sphinx.util
    import sphinx.domains
    import sphinx.web.extensions
    import sphinx.theming
    import sphinx.websupport.storage.redisstorage
    import sphinx.websupport.search.postgresql
    assert loader('sphinx', '', link=False, level=1, toc=False)
    assert loader('sphinx', '', link=True, level=1, toc=False)
    assert loader('sphinx', '', link=True, level=2, toc=False)
    assert loader('sphinx', '', link=True, level=1, toc=True)
    assert loader

# Generated at 2022-06-13 17:44:44.692074
# Unit test for function loader
def test_loader():
    """Unit test for generator."""
    assert loader(
        "pyslvs",
        ".",
        True,
        1,
        False
    ).split()[:3] == ['#', 'Pyslvs', 'API']

# Generated at 2022-06-13 17:44:51.804778
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    from unittest import TestCase, mock
    from importlib import machinery
    from ..data_buf import DataBuf
    from ..topo_links import TopoLink

    class TestLoader(TestCase):

        """Unit test for the loader."""

        @staticmethod
        def loader(*args, **kwargs) -> str:
            """Wrapper for the loader."""
            return loader(*args, **kwargs)

        def test_core(self) -> None:
            """Core package."""
            pkg = TestLoader.loader("core", "../")
            self.assertIn("Pyslvs", pkg)
            self.assertIn("Calculation", pkg)
            self.assertIn("Settings", pkg)
            self.assertIn("Version", pkg)

# Generated at 2022-06-13 17:44:58.759032
# Unit test for function walk_packages
def test_walk_packages():
    """Walk packages test."""

# Generated at 2022-06-13 17:45:08.366360
# Unit test for function loader
def test_loader():
    import pkgutil
    import sys
    from site import ENABLE_USER_SITE
    from .compiler import loader
    from .logger import logger
    logger.setLevel(1)
    for _, name, _ in pkgutil.iter_modules():
        if not name.startswith('pyslvs') or name.endswith('__main__'):
            continue
        print(name)
        print('-' * len(name))
        print(loader(name, _site_path(name), False, 1, False))
        print('-' * len(name))
        print(loader(name, _site_path(name), True, 1, False))
        print('-' * len(name))
        print(loader(name, _site_path(name), True, 2, True))

# Generated at 2022-06-13 17:45:16.358344
# Unit test for function loader
def test_loader():
    """Testing function loader."""
    path = dirname(dirname(abspath(__file__)))

# Generated at 2022-06-13 17:45:22.321167
# Unit test for function walk_packages
def test_walk_packages():
    import pkgutil
    name = 'Pyslvs'
    path = abspath(dirname(__file__)) + sep + '..'
    assert all(path.endswith(pwd)
               for pwd in pkgutil.walk_packages(path=[path]))
    for name, path in walk_packages(name, path):
        assert isfile(path + '.py') or isfile(path + '.pyi')

# Generated at 2022-06-13 17:45:24.151202
# Unit test for function loader
def test_loader():
    assert loader(
        'pyslvs',
        abspath(dirname(__file__)),
        True,
        1,
        False
    )

# Generated at 2022-06-13 17:48:37.978829
# Unit test for function loader
def test_loader():
    """Test for function loader."""
    from .parser import Parser
    assert loader('pyslvs', '.', True, 2, True) == Parser.new(
        True, 2, True
    ).compile()



# Generated at 2022-06-13 17:48:47.530686
# Unit test for function loader
def test_loader():
    """Test `loader` function."""
    import re
    import numpy as np
    import pyslvs as pslvs
    # Create temporary module
    logger.info("Test temporary module")
    name = 'test_api'
    text = 'def main():\n    pass'
    doc = loader(name, '', True, 1, False)
    assert not doc.strip(), "doc should be empty with temporary module"
    logger.info("Test loading from source file")
    text = "def main():\n    pass"
    doc = loader(name, '', True, 1, False)
    assert not doc.strip(), "doc should be empty without source file"
    path = join('.', f"{name}.py")
    _write(path, text)

# Generated at 2022-06-13 17:48:54.173796
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    # If not in site-packages, then "ModulNotFoundError" will be raise
    assert len(list(walk_packages('pyslvs', '.'))) != 0
    path = list(walk_packages('pyslvs', '..'))[0][1]  # pyslvs.__init__.py
    assert _load_module('pyslvs', path.replace('__init__.py', 'logger.py'), None)
    assert not _load_module('pyslvs', '..', None)
    assert not _load_module('pyslvs', '', None)

# Generated at 2022-06-13 17:48:57.346948
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    logger.info(loader('pyslvs_ui', '.', link=False, level=2, toc=False))
    logger.info(loader('pyslvs_ui', '../..', link=False, level=2, toc=False))



# Generated at 2022-06-13 17:48:58.683211
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    print(loader("pyslvs", "../..", False, 1, False))

# Generated at 2022-06-13 17:49:05.057356
# Unit test for function loader
def test_loader():
    from tempfile import mkdtemp
    from shutil import rmtree

    def mk_temp():
        path = mkdtemp()
        logger.debug(f"path: {path}")
        return path

    temp_root = mk_temp()
    path = join(temp_root, 'pyslvs_ui')
    mkdir(path)

    path_py = join(path, '__init__.py')
    path_rt = join(path, 'root.py')
    path_cd = join(path, 'child')
    path_ct = join(path_cd, '__init__.py')

    _write(path_py, "'''Root'''")
    _write(path_rt, "'''Root'''")
    _write(path_ct, "'''Child'''")

   
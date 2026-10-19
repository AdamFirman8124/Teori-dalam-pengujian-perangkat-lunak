

# Generated at 2022-06-13 17:43:20.294738
# Unit test for function walk_packages
def test_walk_packages():
    from pytest import approx
    sys_path.append('./tests')
    from .test_mof import mof, pep561
    for doc_name, file_path in walk_packages(mof.__name__, './tests'):
        assert file_path == mof.__file__
    for doc_name, file_path in walk_packages(pep561.__name__, './tests'):
        assert file_path.endswith(pep561_name.py)

# Generated at 2022-06-13 17:43:22.777406
# Unit test for function loader
def test_loader():
    root = "pyslvs"
    pwd = _site_path(root)
    print(loader(root, pwd, True, 1, False))


if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:43:26.518225
# Unit test for function loader
def test_loader():
    """Test function loader."""
    from .test import root_names
    from .test.site_packages import pwd
    docs = gen_api(root_names, pwd)
    for doc in docs:
        print(doc)

# Generated at 2022-06-13 17:43:30.419251
# Unit test for function loader
def test_loader():
    from pyslvs import api_info
    logger.info("Load VPython packages")
    gen_api({'VPython': 'visual'}, isdir('site-packages') and 'site-packages')
    logger.info("Load Pyslvs packages")
    gen_api({'Pyslvs': 'pyslvs'}, prefix='build/docs', link=False)
    logger.info("Load API information")
    gen_api(api_info, prefix='docs', link=False)

# Generated at 2022-06-13 17:43:40.447689
# Unit test for function loader
def test_loader():
    """Test for loader."""
    from tempfile import TemporaryDirectory
    import unittest.mock as mock
    with TemporaryDirectory() as tmp:
        tmp = abspath(tmp)
        __path__ = [tmp, tmp + '-stubs']
        __name__ = ''
        logger.debug = mock.Mock()
        logger.info = mock.Mock()
        logger.warning = mock.Mock()
        logger.error = mock.Mock()
        logger.critical = mock.Mock()
        p = Parser.new(False, 0, False)
        _load_module(__name__, f"{tmp}/pkg.py", p)

# Generated at 2022-06-13 17:43:42.074865
# Unit test for function loader
def test_loader():
    from . import __root__
    print(loader('tests', __root__, False, 2, True))


if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:43:50.290741
# Unit test for function loader
def test_loader():
    """Test the API generate algorithm."""
    p = Parser.new(link=True, level=1, toc=False)
    root = 'pyslvs'
    for name, path in walk_packages(root, 'test_pyslvs'):
        pure_py = False
        for ext in [".py", ".pyi"]:
            path_ext = path + ext
            if not isfile(path_ext):
                continue
            logger.debug(f"{name} <= {path_ext}")
            p.parse(name, _read(path_ext))
            if ext == ".py":
                pure_py = True
        if pure_py:
            continue
        logger.debug(f"loading extension module for fully documented:")
        # Try to load module here

# Generated at 2022-06-13 17:43:56.516437
# Unit test for function walk_packages
def test_walk_packages():
    # noinspection PyUnresolvedReferences
    import sys
    import os
    import pkgutil
    import pkg_resources
    import distutils.sysconfig
    import distutils.version
    # noinspection PyUnresolvedReferences
    import pytest

    def pkg_walk(path: str) -> Iterator[tuple[str, str]]:
        return ((x[1], x[1]) for x in pkgutil.iter_modules([path]))

    def egg_walk(path: str) -> Iterator[tuple[str, str]]:
        return ((x.project_name, x.location) for x in pkg_resources.working_set)


# Generated at 2022-06-13 17:43:59.847716
# Unit test for function loader
def test_loader():
    import os
    import sys
    import inspect
    import tempfile
    from os.path import exists, dirname, join as path_join
    from importlib import import_module

    PWD = tempfile.mkdtemp()


# Generated at 2022-06-13 17:44:01.791506
# Unit test for function walk_packages
def test_walk_packages():
    for item in walk_packages('pyslvs', 'pyslvs/tests/data'):
        print(item)
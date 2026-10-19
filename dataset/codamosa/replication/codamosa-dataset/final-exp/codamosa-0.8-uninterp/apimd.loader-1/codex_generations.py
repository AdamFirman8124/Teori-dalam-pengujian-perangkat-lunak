

# Generated at 2022-06-13 17:42:21.879462
# Unit test for function loader
def test_loader():
    def report() -> None:
        assert len(pwd) != 0
        assert len(name) != 0
        assert len(res) != 0
        assert res.startswith("# Pyslvs API\n")

    pwd = _site_path("pyslvs")
    logger.info(f"Load root: pyslvs")
    res = loader("pyslvs", pwd, False, 1, False)
    logger.info("=" * 12)
    logger.info(res)
    report()
    if pwd != _site_path("qtpy"):
        logger.info(f"Load root: qtpy")
        name = "qtpy"
        res = loader(name, _site_path(name), False, 1, False)
        logger.info("=" * 12)

# Generated at 2022-06-13 17:42:26.470496
# Unit test for function loader
def test_loader():
    """Test package loading."""
    from importlib import import_module
    import pytest

    @pytest.mark.parametrize(["level", "toc"], [
        (1, False),
        (2, True)
    ])
    def test_loader_level(level: int, toc: bool):
        """Test the loaded modules."""
        name = 'pyslvs'
        pwd = _site_path(name)
        doc = loader(name, pwd, False, level, toc)
        assert doc.count(f'#{"#" * level} ') == (1 if toc else 0)
        for line in doc.strip().splitlines():
            if line.startswith('#'):
                continue
            name = line.strip()

# Generated at 2022-06-13 17:42:28.807243
# Unit test for function loader
def test_loader():
    for name, path in walk_packages("numpy", "numpy"):
        print(name, path, sep='\t')


if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:42:30.304953
# Unit test for function loader
def test_loader():
    """Unit test."""
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:42:31.989182
# Unit test for function loader
def test_loader():
    """Unit test for function loader."""
    # Load test module in the current directory
    loader('test', '.', True, 2, True)

# Generated at 2022-06-13 17:42:37.654569
# Unit test for function walk_packages
def test_walk_packages():
    s = "test_compiler_find.find_spec.spec_from_file_location"
    b = "test_compiler_find.find_spec.spec_from_loader.module_from_spec"
    c = "test_compiler_find.find_spec.spec_from_loader.module_from_spec.parent"
    case = [(s, join("test_compiler_find", "find_spec", s + '.pyi')),
            (b, join("test_compiler_find", "find_spec", b + '.pyi')),
            (c, join("test_compiler_find", "find_spec", c + '.pyi')),
            ]
    res = list(walk_packages("test_compiler_find.find_spec",
                             "test_compiler_find"))

# Generated at 2022-06-13 17:42:47.031346
# Unit test for function loader
def test_loader():
    def walk_packages_test(name: str, path: str) -> Iterator[tuple[str, str]]:
        """Walk packages without import them."""
        path = abspath(path) + sep
        valid = (path + name, path + name + PEP561_SUFFIX)
        for root, _, fs in walk(path):
            for f in fs:
                if not f.endswith(('.py', '.pyi')):
                    continue
                f_path = parent(join(root, f))
                if not f_path.startswith(valid):
                    continue
                name = (f_path
                        .removeprefix(path)
                        .replace(PEP561_SUFFIX, "")
                        .replace(sep, '.')
                        .removesuffix('.__init__'))


# Generated at 2022-06-13 17:42:50.506810
# Unit test for function loader
def test_loader():
    """Tests for module loader."""
    # A moudle for test
    loader('pyslvs', dirname(__file__), False, 1, False)


if __name__ == '__main__':
    test_loader()

# Generated at 2022-06-13 17:42:55.330805
# Unit test for function walk_packages
def test_walk_packages():
    # pk = '/usr/local/lib/python3.8/site-packages'
    pk = '/Users/develop/Library/Python/3.8/lib/python/site-packages'



# Generated at 2022-06-13 17:43:01.966614
# Unit test for function loader
def test_loader():
    from os import chdir
    from os.path import split, dirname
    from unittest.mock import patch
    with patch('os.path.abspath', lambda p: p):
        doc = loader('PySlvs', join(dirname(__file__), '..'))
        logger.info('=' * 12)
        logger.info(doc)
        assert '# PySlvs API' in doc
    chdir(dirname(dirname(dirname(__file__))))
    doc = loader('PySlvs', dirname(split(dirname(__file__))[0]))
    logger.info('=' * 12)
    logger.info(doc)
    assert '# PySlvs API' in doc

if __name__ == '__main__':
    test_loader()
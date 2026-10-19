

# Generated at 2022-06-13 20:43:29.243855
# Unit test for function bump_version

# Generated at 2022-06-13 20:43:35.352248
# Unit test for function bump_version
def test_bump_version():
    """
    Check the bump_version function.

    This is not run with the other unit tests.
    """
    print('Testing bump_version...')

    # pylint: disable=C0301,C0330

# Generated at 2022-06-13 20:43:46.885045
# Unit test for function bump_version
def test_bump_version():
    """Test bump_version."""

# Generated at 2022-06-13 20:43:56.958528
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    """Test bump_version()."""
    from pprint import pprint as pp
    from flutils.debugging import set_trace

# Generated at 2022-06-13 20:44:08.091456
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:44:16.693407
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    # Test position = 0
    assert bump_version('1.2.2', position=0) == '2.0'
    assert bump_version('1.1.2', position=0) == '2.0'
    assert bump_version('1.0.0', position=0) == '2.0'
    assert bump_version('0.2.2', position=0) == '1.0'
    assert bump_version('0.1.2', position=0) == '1.0'
    assert bump_version('0.0.0', position=0) == '1.0'

    # Test position = 1
    assert bump_version('1.2.2', position=1) == '1.3'

# Generated at 2022-06-13 20:44:25.888037
# Unit test for function bump_version
def test_bump_version():

    assert bump_version('1.2.4') == '1.2.5'
    assert bump_version('1.2.4', position=1) == '1.3'
    assert bump_version('1.2.4', position=0) == '2'
    assert bump_version('1.2.4', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4b0', position=1) == '1.3'
    assert bump_version('1.2.4b0', position=0) == '2'
    assert bump_version('1.2.4b0', position=-1) == '1.2.4'
    assert bump_version('1.2.4a0', position=1) == '1.3'
    assert bump_version

# Generated at 2022-06-13 20:44:35.797560
# Unit test for function bump_version
def test_bump_version():
    '''
    Unit test for function :obj:`bump_version`

    '''
    from flutils.fileutils import TempFile
    from flutils.objutils import DictObject

    from click.testing import CliRunner
    from click.types import STRING

    from flutils.packageutils import bump_version

    TEST_DATA = (
        '1.2.3',
        '1.2.3a0',
        '1.2.3b0',
        '1.2.3a1',
        '1.2.3b1',
        '1.2.3a1.dev1',
    )
    runner = CliRunner()
    with runner.isolated_filesystem():
        for version in TEST_DATA:
            with TempFile('w') as fp:
                fp.write

# Generated at 2022-06-13 20:44:42.010291
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    print('Testing function bump_version...')
    import sys
    import io
    import unittest


# Generated at 2022-06-13 20:44:50.648301
# Unit test for function bump_version
def test_bump_version():
    def run_test(input_value, position, pre_release, output_expected):
        output_actual = bump_version(input_value, position, pre_release)
        print('Input: %r' % input_value)
        print('Output: %r' % output_actual)
        print('Expected: %r' % output_expected)
        assert output_actual == output_expected

    run_test('1.2.2', position=2, pre_release=None, output_expected='1.2.3')
    run_test('1.2.3', position=1, pre_release=None, output_expected='1.3')
    run_test('1.3.4', position=0, pre_release=None, output_expected='2.0')

# Generated at 2022-06-13 20:45:16.064580
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    ver_info = _build_version_info('2.2.0')
    for pos in (-3, -2, -1, 0, 1, 2):
        for prerelease in (None, 'a', 'alpha', 'b', 'beta'):
            bump_type = _build_version_bump_type(pos, prerelease)
            assert bump_type in (
                _BUMP_VERSION_MAJOR,
                _BUMP_VERSION_MINOR,
                _BUMP_VERSION_MINOR_ALPHA,
                _BUMP_VERSION_MINOR_BETA,
                _BUMP_VERSION_PATCH,
                _BUMP_VERSION_PATCH_ALPHA,
                _BUMP_VERSION_PATCH_BETA
            )

# Generated at 2022-06-13 20:45:28.988610
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    from flutils.testing import (
        assert_equal,
        assert_equal_results,
        assert_in,
    )


# Generated at 2022-06-13 20:45:42.168338
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""


# Generated at 2022-06-13 20:45:52.620060
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:05.369603
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for bump_version function.

    Run with:

        ``python -m flutils.packages.test_bump_version``

    """
    import sys
    import unittest

    # noinspection PyMissingOrEmptyDocstring

# Generated at 2022-06-13 20:46:13.644769
# Unit test for function bump_version
def test_bump_version():
    """Unit test for the ``bump_version`` function."""
    from random import randint

    for _ in range(100):
        for major in range(1, 10):
            for minor in range(0, 10):
                for patch in range(0, 10):
                    for pre_pos in (1, 2):
                        for pre_num in range(0, 10):
                            for pre_txt in ('a', 'alpha'):
                                base = '%s.%s.%s' % (major, minor, patch)
                                if pre_txt == 'a':
                                    pre_str = 'a%s'
                                else:
                                    pre_str = 'alpha%s'


# Generated at 2022-06-13 20:46:23.429174
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for function bump_version
    """

    from .testing import validate_test

    # New in version 0.3.1
    assert bump_version('2.2', position=-2, pre_release='b') == '2.2b0'


# Generated at 2022-06-13 20:46:33.627999
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function ``bump_version``.
    """

# Generated at 2022-06-13 20:46:46.903548
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:58.075457
# Unit test for function bump_version
def test_bump_version():
    """Unit test for package ``flutils``'s module ``packages``'s function
    ``bump_version``.
    """

    # noinspection PyUnresolvedReferences
    """
    Coverage: 100%
    """

    # noinspection PyPackageRequirements
    import doctest
    doctest.testmod()


# Make the unit test's functions/classes visible for testing
# noinspection PyUnresolvedReferences
del (
    _VersionPart,
    _VersionInfo,
    _each_version_part,
    _build_version_info,
    _build_version_bump_position,
    _build_version_bump_type,
    test_bump_version
)

# Generated at 2022-06-13 20:47:15.134046
# Unit test for function bump_version
def test_bump_version():
    from pprint import pprint
    from flutils.packages import bump_version
    numbers = [
        '0.0.1',
        '0.0.9',
        '1.0.0',
        '1.2.1a1',
        '1.2.1a9',
        '1.2.1b1',
        '1.2.1b9',
        '1.2.9',
        '1.9.9',
        '2.0.1',
        '2.0.9',
        '2.1.1a1',
        '2.1.1a9',
        '2.1.1b1',
        '2.1.1b9',
        '2.1.9',
        '2.9.9',
    ]

# Generated at 2022-06-13 20:47:24.258381
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version

    # Test defaults
    assert bump_version('1.2.2') == '1.2.3'
    # Test minor
    assert bump_version('1.2.2', position=1) == '1.3'
    # Test major
    assert bump_version('1.2.2', position=0) == '2.0'
    # Test alpha
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    # Test alpha bump
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    # Test beta
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:47:39.656719
# Unit test for function bump_version
def test_bump_version():
    print('Begin unit test %s' % __name__)
    print('Testing function bump_version')
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=2) == '1.3.5'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

# Generated at 2022-06-13 20:47:48.861748
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:47:59.094846
# Unit test for function bump_version
def test_bump_version():
    """Test bump_version."""
    from flutils.packages import bump_version as bv

    # Test prefix
    assert bv('1.2.3') == '1.2.4'
    assert bv('1.5.0') == '1.5.1'
    assert bv('1.5.12.34') is None

    # Test 'major' release
    assert bv('1.2.3', 0) == '2.0'
    assert bv('1.5.0', 0) == '2.0'
    assert bv('1.5.12.34', 0) is None

    # Test 'minor' release
    assert bv('1.2.3', 1) == '1.3'
    assert bv('1.5.0', 1) == '1.6'


# Generated at 2022-06-13 20:48:10.580354
# Unit test for function bump_version
def test_bump_version():

    # noinspection PyUnusedLocal
    def version(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ) -> str:
        return bump_version(version, position, pre_release)


# Generated at 2022-06-13 20:48:21.874121
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    import os
    import unittest as unitest

    class BumpVersionTests(unitest.TestCase):
        """Tests for function bump_version."""

        def setUp(self):
            self.maxDiff = None

        def _call_fut(self, version, position=2, pre_release=None):
            from flutils.packages import bump_version
            return bump_version(
                version,
                position=position,
                pre_release=pre_release
            )

        def test_good(self):
            """Basic tests."""
            self.assertEqual(
                self._call_fut('1.2.2'),
                '1.2.3'
            )

# Generated at 2022-06-13 20:48:33.839334
# Unit test for function bump_version
def test_bump_version():
    """Test the bump version function."""
    import unittest

    class TestBumpVersion(unittest.TestCase):
        """Unit tests for function bump_version."""

        def test_bump_version_case_01(self):
            """Unit test for function bump_version."""
            from flutils import packages
            self.assertEqual(packages.bump_version('1.2.2'), '1.2.3')

        def test_bump_version_case_02(self):
            """Unit test for function bump_version."""
            from flutils import packages
            self.assertEqual(packages.bump_version('1.2.3', position=1), '1.3')

        def test_bump_version_case_03(self):
            """Unit test for function bump_version."""


# Generated at 2022-06-13 20:48:46.545184
# Unit test for function bump_version
def test_bump_version():
    
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position = 1) == '1.3'
    assert bump_version('1.3.4', position = 0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:56.889726
# Unit test for function bump_version
def test_bump_version():
    # print(bump_version(version='1.2.2'))
    assert bump_version(version='1.2.2') == '1.2.3'

    # print(bump_version(version='1.2.3', position=1))
    assert bump_version(version='1.2.3', position=1) == '1.3'

    # print(bump_version(version='1.3.4', position=0))
    assert bump_version(version='1.3.4', position=0) == '2.0'

    # print(bump_version(version='1.2.3', prerelease='a'))
    assert bump_version(version='1.2.3', prerelease='a') == '1.2.4a0'

    # print(bump_version(

# Generated at 2022-06-13 20:49:13.026317
# Unit test for function bump_version
def test_bump_version():
    import unittest
    import flutils.packages

    class TestBumpVersion(unittest.TestCase):
        """Test the ``bump_version`` function."""

        def setUp(self) -> None:
            """Set up a test."""
            self.func = flutils.packages.bump_version

        def test_is_importable(self) -> None:
            """Ensure we can import ``bump_version``."""
            from flutils.packages import bump_version
            bump_version('1.2.3')

        def test_empty_version(self) -> None:
            """Ensure we raise an exception if we're given an empty version."""
            self.assertRaises(ValueError, self.func, '')


# Generated at 2022-06-13 20:49:21.137037
# Unit test for function bump_version
def test_bump_version():
    ver = bump_version('1.2.2')
    assert ver == '1.2.3'
    ver = bump_version('1.2.3', position=1)
    assert ver == '1.3'
    ver = bump_version('1.3.4', position=0)
    assert ver == '2.0'
    ver = bump_version('1.2.3', prerelease='a')
    assert ver == '1.2.4a0'
    ver = bump_version('1.2.4a0', pre_release='a')
    assert ver == '1.2.4a1'
    ver = bump_version('1.2.4a1', pre_release='b')
    assert ver == '1.2.4b0'

# Generated at 2022-06-13 20:49:30.194633
# Unit test for function bump_version
def test_bump_version():
    """Tests the function: bump_version()."""
    import sys

    if sys.version_info.major == 3 and sys.version_info.minor < 6:
        from importlib import reload
    else:
        from importlib import reload

    reload(package)
    from flutils.packages import bump_version

    def test_version(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None,
            exp_out: Optional[str] = None,
            exp_exc: Union[int, None] = None
    ) -> None:
        if exp_exc is None:
            out = bump_version(
                version=version,
                position=position,
                pre_release=pre_release
            )
            assert out == exp_out
        else:
            exp

# Generated at 2022-06-13 20:49:45.936235
# Unit test for function bump_version
def test_bump_version():
    def _test(version, bump_pos, prerelease, expected):
        res = bump_version(version, bump_pos, prerelease)
        assert(res == expected)

    _test('1.2.2', 2, None, '1.2.3')
    _test('1.2.3', 1, None, '1.3')
    _test('1.3.4', 0, None, '2.0')
    _test('1.2.3', 2, 'a', '1.2.4a0')
    _test('1.2.4a0', 2, 'a', '1.2.4a1')
    _test('1.2.4a1', 2, 'b', '1.2.4b0')

# Generated at 2022-06-13 20:49:55.706533
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version function."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:50:09.367002
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version"""
    import unittest

    class TestBumpVersion(unittest.TestCase):
        """Class for testing the function bump_version"""
        def test_bump_version(self):
            """Test the function bump_version"""
            self.assertEqual(bump_version('1.2.2'), '1.2.3')
            self.assertEqual(bump_version('1.2.3', position=1), '1.3')
            self.assertEqual(bump_version('1.3.4', position=0), '2.0')
            self.assertEqual(bump_version('1.2.3', prerelease='a'), '1.2.4a0')

# Generated at 2022-06-13 20:50:11.502791
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2')

test_bump_version()

# Generated at 2022-06-13 20:50:21.968069
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    # pylint: disable=C0103
    import pytest
    with pytest.raises(ValueError, match='non-zero pre-release tag'):
        bump_version('2.1.3a0', position=0)
    with pytest.raises(ValueError, match='must not be a major version'):
        bump_version('1.1a0', position=0)
    with pytest.raises(ValueError, match='must not be a major version'):
        bump_version('1.1a2', position=0)
    with pytest.raises(ValueError, match='must not be a major version'):
        bump_version('1.1b2')

# Generated at 2022-06-13 20:50:27.709648
# Unit test for function bump_version
def test_bump_version():

    from sys import version_info as python_version
    if python_version.major != 3 or python_version.minor < 7:
        return

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:50:33.998206
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for function bump_version
    """

    from flutils.packages import bump_version


# Generated at 2022-06-13 20:50:53.659544
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    """Unit test for function: ``bump_version()``."""

# Generated at 2022-06-13 20:51:05.801437
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:51:13.464835
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""

# Generated at 2022-06-13 20:51:19.067827
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for ``bump_version``.

    """
    bump_version(version='1.2.2', position=2, pre_release=None)
    bump_version(version='1.2.2', position=1, pre_release=None)
    bump_version(version='1.2.2', position=0, pre_release=None)
    bump_version(version='1.2.2', position=2, pre_release='a')
    bump_version(version='1.2.3', position=2, pre_release='a')
    bump_version(version='1.2.3a0', position=2, pre_release='a')
    bump_version(version='1.2.3a0', position=2, pre_release='b')

# Generated at 2022-06-13 20:51:29.108552
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version"""
    # pylint: disable=C0116,C0115

    import pytest

    from ._version import __version__
    from .packages import bump_version

    def _raise_exc(exc):
        raise exc

    def _get_exc_msg(exc):
        return '%s: %s' % (exc.__class__.__name__, str(exc))

    class Test(object):

        def __init__(self, test, result=None):
            self.test = test
            self.result = result

        def run(self):
            got = bump_version(self.test)
            assert got == self.result


# Generated at 2022-06-13 20:51:40.820404
# Unit test for function bump_version
def test_bump_version():
    from itertools import product
    from mypy_extensions import TypedDict

    class TestCase(TypedDict, total=False):
        version: str
        test_args: Tuple[Any, ...]

    class TestResult(TypedDict):
        expected: str
        reason: str

    def run_tests(tests: List[Tuple[TestCase, TestResult]]):
        import sys
        from mypy_extensions import TypedDict

        class TestResult(TypedDict, total=False):
            version: str
            result: str
            reason: str

        def build_test_result(version: str, result: str, reason: str) -> TestResult:
            return TestResult(version=version, result=result, reason=reason)


# Generated at 2022-06-13 20:51:46.030872
# Unit test for function bump_version
def test_bump_version():
    from flutils.testingutils import run_doctest

    results = run_doctest(bump_version.__doc__)
    assert results.failures == 0

# Generated at 2022-06-13 20:51:55.649007
# Unit test for function bump_version

# Generated at 2022-06-13 20:52:04.932355
# Unit test for function bump_version
def test_bump_version():
    import flutils.packages as pack
    version = '1.2.3'
    assert pack.bump_version(version) == '1.2.4'

    version = '1.2.3'
    assert pack.bump_version(version, pre_release='alpha') == '1.2.4a0'

    version = '1.2.4a0'
    assert pack.bump_version(version, pre_release='alpha') == '1.2.4a1'

    version = '1.2.4a1'
    assert pack.bump_version(version, pre_release='beta') == '1.2.4b0'

    version = '1.2.4a1'
    assert pack.bump_version(version) == '1.2.4'


# Generated at 2022-06-13 20:52:18.581532
# Unit test for function bump_version
def test_bump_version():
    """Test the function ``bump_version``."""
    # fmt: off

# Generated at 2022-06-13 20:52:46.158001
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:52:53.186159
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    from .testing import run_tests
    from .testing import message_cache

    clean_first = False

    if clean_first:
        message_cache.clear()


# Generated at 2022-06-13 20:53:02.949712
# Unit test for function bump_version
def test_bump_version():
    versions = [
        (1, 2, 0),
        (1, 2, 3),
        (1, 3, 0),
        (2, 0, 0),
        (1, 2, 0, 'a', 0),
        (1, 2, 4, 'a', 0),
        (1, 2, 4, 'a', 1),
        (1, 2, 4, 'b', 0),
        (1, 2, 4),
        (1, 2, 4, 'b', 0),
        (2, 1, 3)
    ]
    for ver in versions:
        ver_str = '.'.join(map(str, ver))
        new_ver = ver_str
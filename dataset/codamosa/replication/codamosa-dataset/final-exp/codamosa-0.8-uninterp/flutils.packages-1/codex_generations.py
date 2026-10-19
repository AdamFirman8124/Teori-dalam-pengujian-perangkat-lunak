

# Generated at 2022-06-13 20:43:41.105759
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:43:52.885406
# Unit test for function bump_version
def test_bump_version():
    """Test bump_version()."""
    ver = '1.2.3'
    bump_ver = bump_version(ver, position=2)
    assert bump_ver == '1.2.4'

    ver = '1.2.3'
    bump_ver = bump_version(ver, position=1)
    assert bump_ver == '1.3'

    ver = '1.2.3'
    bump_ver = bump_version(ver, position=0)
    assert bump_ver == '2.0'

    ver = '1.2.3'
    bump_ver = bump_version(ver, pre_release='a')
    assert bump_ver == '1.2.4a0'

    ver = '1.2.4a0'

# Generated at 2022-06-13 20:44:00.282539
# Unit test for function bump_version
def test_bump_version():
    """bump_version unit test"""

    def test(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ) -> str:
        """Test the bump_version function and raise any errors."""
        return bump_version(
            version=version,
            position=position,
            pre_release=pre_release
        )

    test_exception = ValueError

# Generated at 2022-06-13 20:44:12.593147
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:19.047287
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version"""

    # Positional argument
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.4') == '1.2.5'
    assert bump_version('1.2.4a0') == '1.2.4a1'
    assert bump_version('1.2.4a1') == '1.2.4a2'
    assert bump_version('1.2.4a2') == '1.2.4a3'
    assert bump_version('1.2.4a2') == '1.2.4a3'
    assert bump_version('1.2.4b0') == '1.2.4b1'

# Generated at 2022-06-13 20:44:31.454175
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version() function.

    This is a unit test for the :func:`bump_version` function.

    *New in version 0.3*

    """
    print('Testing the bump_version() function...')

    def do_test(testdata: List[str]) -> None:
        """Do a test.

        This is a little function used in the test function to "do" a test.

        Args:
            testdata (List[str]): The test data.

        """
        ver, position, pre_release, expected = testdata
        msg = ': {}, {}, {}'.format(ver, position, pre_release)

# Generated at 2022-06-13 20:44:43.379918
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:53.799468
# Unit test for function bump_version
def test_bump_version():
    def _test(version_in: str, version_out: str, *args, **kwargs):
        assert bump_version(version_in, *args, **kwargs) == version_out

    _test('1.2.2', '1.2.3')
    _test('1.2.3', '1.3', position=1)
    _test('1.3.4', '2.0', position=0)
    _test('1.2.3', '1.2.4a0', prerelease='a')
    _test('1.2.4a0', '1.2.4a1', pre_release='a')
    _test('1.2.4a1', '1.2.4b0', pre_release='b')

# Generated at 2022-06-13 20:45:04.638693
# Unit test for function bump_version
def test_bump_version():
    """Test :func:`flutils.packages.bump_version`"""
    from flutils.packages import bump_version as b

    def _ex(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ) -> str:
        """Run bump_version and return the increased version number."""
        return b(version, position, pre_release)

    assert _ex('1.2.2') == '1.2.3'
    assert _ex('1.2.3', position=1) == '1.3'
    assert _ex('1.3.4', position=0) == '2.0'
    assert _ex('1.2.3', prerelease='a') == '1.2.4a0'

# Generated at 2022-06-13 20:45:15.102951
# Unit test for function bump_version
def test_bump_version():
    """Unit test for the ``bump_version`` function."""
    from pprint import pprint

    # First, test invalid input and error conditions.

    def test_invalid_input(version: str, position: Any, pre_release: Any):
        try:
            bump_version(version, position, pre_release)
            assert False
        except ValueError:
            pass

    test_invalid_input('1.2.3', 4, None)
    test_invalid_input('1.2.3', -3, None)
    test_invalid_input('1.2.3', '2', None)
    test_invalid_input('1.2.3', 2, 'xxx')
    test_invalid_input('1.2.3', 0, 'a')

    # Then, test expected behavior

   

# Generated at 2022-06-13 20:45:53.755511
# Unit test for function bump_version
def test_bump_version():
    """Testing function bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:06.278928
# Unit test for function bump_version
def test_bump_version():
    import pytest
    from flutils.packages import bump_version

    with pytest.raises(ValueError):
        bump_version('1.2.3', position=4)

    with pytest.raises(ValueError):
        bump_version('1.2.3', pre_release='foo')

    with pytest.raises(ValueError):
        bump_version('1.2.3', position=0, pre_release='a')

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

# Generated at 2022-06-13 20:46:08.601426
# Unit test for function bump_version
def test_bump_version():
    # noinspection PyUnusedLocal
    return

if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:46:21.305198
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:32.996560
# Unit test for function bump_version
def test_bump_version():
    import unittest

    class TestBumpVersion(unittest.TestCase):
        """Test the function bump_version"""

        def test_bump_major(self):
            """Test bump major version."""
            version = '1.2.3'
            position = 0
            pre_release = None
            expected = '2.0.0'
            actual = bump_version(version, position)
            self.assertEqual(expected, actual)

        def test_bump_minor(self):
            """Test bump minor version."""
            version = '1.2.3'
            position = 1
            pre_release = None
            expected = '1.3.0'
            actual = bump_version(version, position)
            self.assertEqual(expected, actual)


# Generated at 2022-06-13 20:46:46.621967
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=E1101
    import pytest
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:46:52.006166
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    # pylint: disable=W0612
    from flutils.packages import bump_version


if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:47:03.216712
# Unit test for function bump_version
def test_bump_version():
    """Test the function ``bump_version``.
    """
    print(bump_version('1.2.2'))  # '1.2.3'
    print(bump_version('1.2.3', position=1))  # '1.3'
    print(bump_version('1.3.4', position=0))  # '2.0'
    print(bump_version('1.2.3', prerelease='a'))  # '1.2.4a0'
    print(bump_version('1.2.4a0', pre_release='a'))  # '1.2.4a1'
    print(bump_version('1.2.4a1', pre_release='b'))  # '1.2.4b0'

# Generated at 2022-06-13 20:47:14.291159
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    # Setup
    import sys

    # Exercise
    # pylint: disable=W0612
    import flutils
    from flutils.packages import bump_version

    # Verify
    assert sys.modules['flutils'].__version__ == flutils.__version__
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'

# Generated at 2022-06-13 20:47:24.002639
# Unit test for function bump_version
def test_bump_version():
    from .testing import run_until_complete
    from .testing import setup_test_loop
    loop = setup_test_loop()
    loop.run_until_complete(bump_version('0.2.3a0'))
    loop.run_until_complete(bump_version('0.2.3a0', 1))
    loop.run_until_complete(bump_version('0.2.3a0', 2))
    loop.run_until_complete(bump_version('0.2.3'))
    loop.run_until_complete(bump_version('0.2.3', 1))
    loop.run_until_complete(bump_version('0.2.3', 2))
    loop.run_until_complete(bump_version('0.2.3', position=0))


# Generated at 2022-06-13 20:47:48.402845
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version
    """
    from sys import stdout
    from os import EX_OK
    from xml.etree.ElementTree import Element, SubElement, tostring
    from flutils.packages import (
        bump_version,
        _BUMP_VERSION_MAJOR,
        _BUMP_VERSION_MINOR,
        _BUMP_VERSION_MINOR_ALPHA,
        _BUMP_VERSION_MINOR_BETA,
        _BUMP_VERSION_PATCH,
        _BUMP_VERSION_PATCH_ALPHA,
        _BUMP_VERSION_PATCH_BETA
    )
    from flutils.testing import (
        FileCase,
        StringCase
    )


# Generated at 2022-06-13 20:47:58.772295
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=missing-docstring
    import unittest

    class TestVersion(unittest.TestCase):
        def test_bump_version(self):
            # pylint: disable=no-self-use
            # pylint: disable=invalid-name
            from flutils.packages import bump_version

            self.assertEqual(bump_version('1.2.2'), '1.2.3')
            self.assertEqual(bump_version('1.2.3', position=1), '1.3')
            self.assertEqual(bump_version('1.3.4', position=0), '2.0')
            self.assertEqual(bump_version('1.2.3', prerelease='a'), '1.2.4a0')
            self

# Generated at 2022-06-13 20:48:10.547931
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:21.876558
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version function."""
    # noinspection SpellCheckingInspection

# Generated at 2022-06-13 20:48:33.839742
# Unit test for function bump_version
def test_bump_version():
    """Ensure bump_version is working."""
    # pylint: disable=W0612
    print('=== Testing function: bump_version ===')
    print(bump_version('1.2.2'))
    print(bump_version('1.2.3', position=1))
    print(bump_version('1.3.4', position=0))
    print(bump_version('1.2.3', prerelease='a'))
    print(bump_version('1.2.4a0', pre_release='a'))
    print(bump_version('1.2.4a1', pre_release='b'))
    print(bump_version('1.2.4a1'))
    print(bump_version('1.2.4b0'))

# Generated at 2022-06-13 20:48:46.544977
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.packages import bump_version
    # noinspection PyUnresolvedReferences
    from flutils.packages import _BUMP_VERSION_POSITION_NAMES, _BUMP_VERSION_PATCHES, _BUMP_VERSION_MINORS, _BUMP_VERSION_MAJOR, _BUMP_VERSION_MINOR, _BUMP_VERSION_PATCH, _BUMP_VERSION_MINOR_ALPHA, _BUMP_VERSION_MINOR_BETA, _BUMP_VERSION_PATCH_ALPHA, _BUMP_VERSION_PATCH_BETA, _VersionInfo, bump_version, _build_version_bump_position, _build_version_bump_type, _build_version_info, _each_version_part



# Generated at 2022-06-13 20:48:56.135019
# Unit test for function bump_version
def test_bump_version():
    """Test for the function :func:`flutils.packages.bump_version`."""

    from flutils.packages import bump_version

    # pylint: disable=C0116
    def _test_bump(version: str, position: int, pre_release: Optional[str]):
        bumped = bump_version(version, position, pre_release)
        old_v = StrictVersion(version)
        new_v = StrictVersion(bumped)
        if old_v >= new_v:
            raise AssertionError(
                "The version number, %r, was not bumped to a higher "
                "version number." % version
            )

    _test_bump('1.2.2', position=2, pre_release=None)

# Generated at 2022-06-13 20:49:03.990540
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:15.853150
# Unit test for function bump_version
def test_bump_version():
    # noinspection PyUnresolvedReferences
    """Unit-test for the :func:`bump_version` function."""
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:49:28.554326
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""


# Generated at 2022-06-13 20:50:10.329717
# Unit test for function bump_version
def test_bump_version():
    """ Test the functionality of bump_version. """

    from flutils.packages import bump_version
    from ..testing import test_module

    expected = '1.2.3'
    actual = bump_version('1.2.2')
    assert actual == expected, test_module(expected, actual)

    expected = '1.2.3'
    actual = bump_version('1.2.3')
    assert actual == expected, test_module(expected, actual)

    expected = '1.3'
    actual = bump_version('1.2.3', pre_release='b')
    assert actual == expected, test_module(expected, actual)

    expected = '1.3'
    actual = bump_version('1.3.4', position=1)
    assert actual == expected, test_module(expected, actual)

   

# Generated at 2022-06-13 20:50:18.731166
# Unit test for function bump_version
def test_bump_version():
    from flutils.testing import assert_type_equality, run_tests

    tests: List[str] = [
        '0.0.0',
        '2.3.4',
        '1.2.3a0',
        '1.2.4a4',
        '1.2.3b0',
        '1.2.4b4',
    ]
    for ver in tests:
        out = bump_version(ver)
        assert_type_equality(0, [out], [str])
        out = bump_version(ver, 1)
        assert_type_equality(0, [out], [str])
        out = bump_version(ver, 1, 'a')
        assert_type_equality(0, [out], [str])
    del ver

    # Invalid positions

# Generated at 2022-06-13 20:50:28.557647
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:50:38.483421
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0201
    """
    Unit test for function bump_version.
    """

# Generated at 2022-06-13 20:50:49.993203
# Unit test for function bump_version
def test_bump_version():
    """Test function 'bump_version' in module 'flutils.packages'"""
    from flutils.versions import Version
    from flutils.strings import random_string
    from flutils.packages import bump_version

    def test_cases():
        v: List[str] = [
            '1.2.2',
            '1.2.3', '1.2.4a0',
            '1.2.4b0', '1.2.4a1', '1.2.4b1',
            '1.2'
        ]
        for item in v:
            yield item
        yield '1.2.1'
        yield '1.2.3b0'
        yield '1.2.3a0'
        yield '1.2.3a1'

# Generated at 2022-06-13 20:51:02.455119
# Unit test for function bump_version

# Generated at 2022-06-13 20:51:12.333628
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=too-many-branches,too-many-statements
    from textwrap import dedent
    from random import randint
    from flutils.packages import bump_version

    # noinspection PyUnusedLocal
    def assert_invalid(
            version,
            position,
            pre_release,
            expected,
            should_pass,
    ):
        if should_pass is False:
            try:
                bump_version(
                    version=version,
                    position=position,
                    pre_release=pre_release
                )
            except ValueError:
                pass

# Generated at 2022-06-13 20:51:20.120900
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    def _run_test(
            version: str,
            position: int = 2,
            prerelease: Optional[str] = None,
            out: str = None
    ) -> None:
        nonlocal count
        count += 1
        out = bump_version(version, position, prerelease)
        output = 'Version (%r) with position=%r, result: %r' % (
            version, position, out
        )
        if out == out:
            print(output)
        else:
            print('FAIL:', output)

    count = 0
    print('\nTesting function "bump_version"\n')
    _run_test('1.2.2')
    _run_test('1.2.3', position=1)

# Generated at 2022-06-13 20:51:30.183868
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function ``bump_version``."""
    import rstcheck
    import textwrap

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:51:41.378110
# Unit test for function bump_version

# Generated at 2022-06-13 20:52:18.075697
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:52:31.986522
# Unit test for function bump_version
def test_bump_version():
    """Makes sure that bump_version works as expected."""

    # Test default value
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2') == '1.2.1'
    assert bump_version('1.2') == '1.2.1'
    assert bump_version('1a') == '1a1'
    assert bump_version('1a1') == '1a2'
    assert bump_version('1b') == '1b1'
    assert bump_version('1b1') == '1b2'

    # Test moving to a pre-release

# Generated at 2022-06-13 20:52:39.758357
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version()."""
    from flutils.packages import bump_version
    from hypothesis import given
    from hypothesis import strategies as st

    @given(version=st.text(min_size=1))
    def _inner(version: str):
        """Test the function bump_version()."""
        out = bump_version(version=version)
        assert isinstance(out, str)
    _inner()

# Generated at 2022-06-13 20:52:50.154188
# Unit test for function bump_version
def test_bump_version():
    # noinspection PyUnresolvedReferences
    """Unit tests for function ``bump_version``."""
    import sys
    import unittest

    from flutils.packages import bump_version
    from flutils._compat import PYTHON_VERSION

    @staticmethod
    def _get_tb(exception: Exception) -> str:
        """Get the traceback from the exception."""
        tmp_exc_name, exc_value, tmp_exc_traceback = sys.exc_info()
        if PYTHON_VERSION < (3, 5):
            # pylint: disable=W1505
            out = traceback.format_tb(tmp_exc_traceback)
            out = ''.join(out)

# Generated at 2022-06-13 20:53:01.251267
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for ``bump_version()``.
    """
    import unittest
    import sys

    class TestBumpVersion(unittest.TestCase):
        """Unit tests for ``bump_version()``.
        """
        def test_bump_version_major(self):
            """Test: bumping with ``position=0``.
            """
            cases = (
                ('1.2.3', '2'),
                ('2.0', '3'),
                ('2.0.1', '3'),
                ('1.2.3rc1', '2')
            )
            for test in cases:
                exp = test[1]
                res = bump_version(test[0], position=0)
                self.assertEqual(exp, res)


# Generated at 2022-06-13 20:53:09.070622
# Unit test for function bump_version
def test_bump_version():
    """Unit test for the function bump_version."""

    # Set up variables
    def verify_version(
            ver_in,
            ver_out,
            position,
            pre_release
    ):
        """
        """
        assert ver_in == ver_out, (
            "bump_version(%r, position=%r, pre_release=%r) "
            "returned %r, but %r was expected " % (
                ver_in,
                position,
                pre_release,
                ver_out,
                ver_in
            )
        )

    # Test a basic bump: patch
    ver_in = '1.2.3'
    ver_out = bump_version(ver_in)
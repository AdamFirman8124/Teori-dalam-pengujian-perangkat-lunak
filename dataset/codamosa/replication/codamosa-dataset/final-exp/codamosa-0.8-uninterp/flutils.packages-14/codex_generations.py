

# Generated at 2022-06-13 20:43:33.107091
# Unit test for function bump_version
def test_bump_version():
    """ Test function bump_version
    """
    # Test minor bump
    assert '1.2.3' == bump_version('1.2.2')
    assert '1.2.3' == bump_version('1.2.2', pre_release='a')

    # Test major bump
    assert '2.0' == bump_version('1.2.2', position=0)

    # Test minor alpha bump
    assert '1.2.3a0' == bump_version('1.2.3', pre_release='a')
    assert '1.2.3a1' == bump_version('1.2.3a0', pre_release='a')
    assert '1.2.3b0' == bump_version('1.2.3a1', pre_release='b')

# Generated at 2022-06-13 20:43:44.120291
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.packages import bump_version

    # Major
    assert bump_version('0.2.3', position=0) == '1.0'
    assert bump_version('1.2.3', position=0) == '2.0'

    # Minor
    assert bump_version('0.2.3', position=1) == '0.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.2.0', position=1) == '1.3'
    assert bump_version('1.2.3', position=-2) == '1.3'

    # Patch
    assert bump_version('0.2.3', position=2) == '0.2.4'
   

# Generated at 2022-06-13 20:43:55.509502
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from pprint import pprint
    from flutils.packages import bump_version

    # TODO: Fix up unit tests.
    def _do_test(ver: str, position: int, pre_release: str, result: str):
        print('Testing with: %s %s %s' % (ver, position, pre_release))
        ver_out = bump_version(ver, position, pre_release)
        print('ver_out: %s' % ver_out)
        assert ver_out == result, 'bump_version(%s, %s, %s) failed' % (
            ver,
            position,
            pre_release
        )

    # Test 1.2.3

# Generated at 2022-06-13 20:44:05.143192
# Unit test for function bump_version
def test_bump_version():
    """
    Run the unit test for bump_version.
    """
    from pytest import raises

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:44:15.176256
# Unit test for function bump_version
def test_bump_version():
    """Ensures that version numbers are correctly bumped."""

# Generated at 2022-06-13 20:44:25.170395
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version
    """
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:35.479285
# Unit test for function bump_version
def test_bump_version():
    from . import test_data

    for ver, config in test_data.test_bump_version.items():
        pos: int = config['pos']
        pre_release: Union[str, None] = config['pre']
        out: str = config['out']
        try:
            assert bump_version(ver, pos, pre_release) == out
        except Exception as err:  # pylint: disable=W0703
            msg = (
                "Failed to bump version number, %r, at position: %s, for "
                "pre-release: %r.  Error: '%s (type: %s)'" % (
                    ver,
                    pos,
                    pre_release,
                    err,
                    type(err).__name__,
                )
            )

# Generated at 2022-06-13 20:44:46.713022
# Unit test for function bump_version
def test_bump_version():
    from nose2.tools import params
    from pprint import pformat
    from decimal import Decimal

    version_args = (
        '1.4',
        '1.4.2',
        '1.4a0',
        '1.4a5',
        '1.4b0',
        '1.4b5',
        '1.4.0',
        '1.4.5',
        '1.4.0a0',
        '1.4.5a0',
        '1.4.0b0',
        '1.4.5b0',
        '1.4.0a3',
        '1.4.5a3',
        '1.4.0b3',
        '1.4.5b3',
    )

    # 1.4a1

# Generated at 2022-06-13 20:44:54.545409
# Unit test for function bump_version

# Generated at 2022-06-13 20:45:05.018996
# Unit test for function bump_version
def test_bump_version():
    def _assert(
            given_version: str,
            expected_version: str
    ) -> None:
        actual_version = bump_version(given_version)
        assert actual_version == expected_version

    _assert('1.2.3', '1.2.4')
    _assert('1.2.3', '1.2.4')
    _assert('1.2.3', '1.2.4')
    _assert('1.2.3', '1.2.4')
    _assert('1.2.1', '1.2.2')
    _assert('1.2.0', '1.2.1')
    _assert('1.2.0', '1.2.1')
    _assert('1.2.0', '1.2.1')

# Generated at 2022-06-13 20:45:42.520105
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

    import json
    import sys

    from flutils.packages import bump_version

    print('Python Version: %s' % sys.version)
    print()

    with open('tests/_version_data.json', 'r') as f:
        version_tests: Dict[str, Any] = json.load(f)
    for test in version_tests:
        version: str = version_tests[test].pop('version')
        for args, expected in version_tests[test].items():
            args = args.split(', ')
            args[0] = int(args[0])
            if args[1] == 'None':
                args[1] = None
            out: str = bump_version(version, *args)

# Generated at 2022-06-13 20:45:52.947510
# Unit test for function bump_version
def test_bump_version():
    """Execute the module's unit tests."""
    print(bump_version('0.1.3'))
    print(bump_version('0.1.3', position=0))
    print(bump_version('0.1.3', position=1))
    print(bump_version('0.1.3', position=2))
    print(bump_version('0.1.3', position=0, pre_release='a'))
    print(bump_version('0.1.3', position=1, pre_release='a'))
    print(bump_version('0.1.3', position=2, pre_release='a'))
    print(bump_version('0.1.3', position=0, pre_release='b'))

# Generated at 2022-06-13 20:46:05.652358
# Unit test for function bump_version
def test_bump_version():
    """Tests for bump_version()"""

# Generated at 2022-06-13 20:46:19.017078
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:31.905737
# Unit test for function bump_version
def test_bump_version():
    # Test bump_version with no exception
    def _check_bump_version(version, position, pre_release, expected):
        actual = bump_version(version, position, pre_release)
        assert actual == expected, 'actual: %s, expected: %s' % (
            actual,
            expected
        )

    _check_bump_version('2.0.0', -1, None, '2.0.1')
    _check_bump_version('2.0.1a0', -1, None, '2.0.1')
    _check_bump_version('2.0.1.1', -1, None, '2.0.1')


if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:46:45.941589
# Unit test for function bump_version
def test_bump_version():
    """Test the :function:`bump_version` function."""
    # pylint: disable=C0103
    # noinspection PyUnusedLocal
    def _build_test_case(version, position, pre_release):
        ver_info = _build_version_info(version)
        position = _build_version_bump_position(position)
        bump_type = _build_version_bump_type(position, pre_release)
        # noinspection PyUnusedLocal
        hold: List[Union[int, str]] = []
        if bump_type == _BUMP_VERSION_MAJOR:
            hold = [ver_info.major.num + 1, 0]

# Generated at 2022-06-13 20:46:58.514558
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:47:11.167298
# Unit test for function bump_version
def test_bump_version():
    assert bump_version(
        '1.2.2'
    ) == '1.2.3'
    assert bump_version(
        '1.2.3',
        position=1
    ) == '1.3'
    assert bump_version(
        '1.3.4',
        position=0
    ) == '2.0'
    assert bump_version(
        '1.2.3',
        pre_release='a'
    ) == '1.2.4a0'
    assert bump_version(
        '1.2.4a0',
        pre_release='a'
    ) == '1.2.4a1'

# Generated at 2022-06-13 20:47:22.355320
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for bump_version.

    Returns:
        None

    """
    from flutils.validate import is_version_number

    for ver in (
        '1.2.2',
        '1.3',
        '2.0',
        '1.2.4a0',
        '1.2.4a1',
        '1.2.4a10',
        '1.2.4b1',
        '1.2.4b10',
        '1.2.4',
        '1.2.4',
        '1.2.1',
    ):
        assert is_version_number(ver)

    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2022-06-13 20:47:34.579431
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=W0613
    """
    Unit test for function bump_version()
    """
    # noinspection PyUnresolvedReferences
    from flutils.packages import bump_version  # pylint: disable=E0611,E0401


# Generated at 2022-06-13 20:48:09.960550
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function 'bump_version'"""

    import pytest
    # noinspection PyUnresolvedReferences,PyPackageRequirements
    from flutils.packages import bump_version

    def _test_bad_inputs() -> None:
        """Test function inputs that are not good."""

# Generated at 2022-06-13 20:48:21.660050
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version.
    """

    # Bump a patch version
    assert bump_version('1.2.3') == '1.2.4'

    # Bump a minor version
    assert bump_version('1.2.3', position=1) == '1.3'

    # Bump a major version
    assert bump_version('1.2.3', position=0) == '2.0'

    # Bump a patch version to an alpha version
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'

    # Increase an alpha version
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

    # Bump an alpha version to a beta version
    assert bump

# Generated at 2022-06-13 20:48:33.735793
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""

    version = '0.0.1'
    expected = '1.0'
    actual = bump_version(version, position=0)
    assert expected == actual

    version = '1.0.0'
    expected = '2.0'
    actual = bump_version(version, position=1)
    assert expected == actual

    version = '1.0.0'
    expected = '1.1'
    actual = bump_version(version, position=-2)
    assert expected == actual

    version = '1.0.0'
    expected = '1.1'
    actual = bump_version(version, position=-2)
    assert expected == actual

    version = '0.0.1'
    expected = '1.0'

# Generated at 2022-06-13 20:48:46.475845
# Unit test for function bump_version
def test_bump_version():
    """Tests the :meth:`bump_version` method."""

# Generated at 2022-06-13 20:48:56.822883
# Unit test for function bump_version

# Generated at 2022-06-13 20:49:04.390042
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    print('Testing function bump_version() from module packages')

# Generated at 2022-06-13 20:49:14.046818
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0201
    """Unit test for function bump_version.

    *New in version 0.3*
    """
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:49:21.850587
# Unit test for function bump_version
def test_bump_version():
    from flutils import TEST_STATUS
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:49:31.092400
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'


# Generated at 2022-06-13 20:49:46.838378
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    base_version: str = '1.2.3'

# Generated at 2022-06-13 20:50:10.697085
# Unit test for function bump_version
def test_bump_version():
    r"""Unit test for function bump_version.

    This test is intended to be run from the repository root using:

    .. code-block:: bash

        $ py.test flutils/packages.py

    """

# Generated at 2022-06-13 20:50:21.468091
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=R0914
    # pylint: disable=R0915
    # pylint: disable=R1702
    # pylint: disable=C0325
    # pylint: disable=C0116
    # pylint: disable=C0103
    # pylint: disable=W0212
    # pylint: disable=W0612
    import unittest

    class TestVersionBump(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_bump_position_ok(self):
            for pos in range(-3, 3):
                bump_version('1.2.2', position=pos)

# Generated at 2022-06-13 20:50:30.341873
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.testing import assert_raises

# Generated at 2022-06-13 20:50:39.285854
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    # pylint: disable=too-many-branches,too-many-locals

    import sys
    import time
    import unittest
    import warnings
    from unittest import SkipTest
    from pprint import pprint
    from flutils.packages import bump_version

    try:
        from unittest.mock import patch, Mock
    except ImportError:
        from mock import patch, Mock

    try:
        from pathlib import Path
    except ImportError:
        from pathlib2 import Path  # backport for Python 2.7

    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    try:
        import pytest
    except ImportError:
        raise SkipTest('Could not import pytest.')

    #

# Generated at 2022-06-13 20:50:50.263838
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=R0904
    # pylint: disable=C0103
    """Test the function bump_version.
    """
    import unittest

    class TestBumpVersion(unittest.TestCase):
        """Unit test for function bump_version."""

        @classmethod
        def setUpClass(cls):
            """Perform class-level setup."""
            cls.func = bump_version

        def test_bump_version_current(self) -> None:
            """Test the current version number."""
            from flutils import __version__
            self.assertEqual(self.func(__version__), __version__)

        def test_examples(self) -> None:
            """Test the function examples."""

# Generated at 2022-06-13 20:51:02.554334
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""


# Generated at 2022-06-13 20:51:13.454411
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version.

    *New in version 0.3*

    """
    print(bump_version('1.2.2'))
    print(bump_version('1.2.3', position=1))
    print(bump_version('1.3.4', position=0))
    print(bump_version('1.2.3', position=-2))
    print(bump_version('1.2.3', prerelease='a'))
    print(bump_version('1.2.4a0', pre_release='a'))
    print(bump_version('1.2.4a1', pre_release='b'))
    print(bump_version('1.2.4a1'))

# Generated at 2022-06-13 20:51:20.626526
# Unit test for function bump_version

# Generated at 2022-06-13 20:51:30.359551
# Unit test for function bump_version
def test_bump_version():
    """
    Function test for flutils.packages.bump_version
    """
    from sys import version_info
    from tempfile import mkdtemp
    from pyfakefs.fake_filesystem_unittest import TestCase
    from pyfakefs.fake_filesystem import FakeFilesystem
    from pyfakefs.fake_filesystem import fake_filesystem
    from flutils.packages import bump_version

    if version_info < (3, 0):
        print('This unit test requires Python 3.0 or above.  No tests run.')
        return

    class Test(TestCase):
        """
        TestCase class for flutils.packages.bump_version
        """


# Generated at 2022-06-13 20:51:41.485750
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version."""
    from flutils.packages import bump_version

    def test_case(
            name: str,
            expected: str,
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None,
    ) -> None:
        actual = bump_version(version, position, pre_release)
        if expected != actual:
            msg = '%r != %r' % (expected, actual)
            raise AssertionError('{}: {}'.format(name, msg))

    test_case('basic major', '2.0', '1.2.3')
    test_case('basic minor', '1.3', '1.2.3', position=1)

# Generated at 2022-06-13 20:52:14.985774
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""

    from flutils.packages import bump_version

    # Unit test for function bump_version
    # Tests for bump_version 1.2.2
    s_ver = '1.2.2'
    s_ver_bump = bump_version(s_ver)
    assert(s_ver_bump == '1.2.3')


    # Unit test for function bump_version
    # Tests for bump_version 1.2.2
    s_ver = '1.2.2'
    pos = 1
    s_ver_bump = bump_version(s_ver, position=pos)
    assert(s_ver_bump == '1.3')


    # Unit test for function bump_version
    # Tests for bump_version 1.2.2
    s_

# Generated at 2022-06-13 20:52:21.944894
# Unit test for function bump_version
def test_bump_version():
    """ Test that bump_version() returns the expected values. """
    def bump_step(in_version, position, pre_release):
        """ Test each version step. Returns the increment version. """
        out_version = bump_version(in_version, position, pre_release)
        return out_version

    # Test major version step
    assert bump_step('1.2.2', 0, None) == '2'
    assert bump_step('1.2.3', 0, None) == '2'
    assert bump_step('1.2.4a1', 0, None) == '2'
    assert bump_step('1.2.4b0', 0, None) == '2'

    # Test minor version step.  Increase minor version, clear pre-release

# Generated at 2022-06-13 20:52:33.716221
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    bump_version('1.2.2')
    bump_version('1.2.3', position=1)
    bump_version('1.3.4', position=0)
    bump_version('1.2.3', prerelease='a')
    bump_version('1.2.4a0', pre_release='a')
    bump_version('1.2.4a1', pre_release='b')
    bump_version('1.2.4a1')
    bump_version('1.2.4b0')
    bump_version('2.1.3', position=1, pre_release='a')
    bump_version('1.2b0', position=2)

if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:52:46.294630
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    import sys
    import doctest
    import flutils.packages

    options = (doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE |
               doctest.IGNORE_EXCEPTION_DETAIL)
    results = doctest.testmod(optionflags=options,
                              module=flutils.packages)
    print('{0}: {1.attempted:2d} tests, '
          '{1.failed:2d} failures, '
          '{1.errors:2d} errors'.format(sys.argv[0], results))
    if results.failed or results.errors:
        sys.exit(1)


if __name__ == '__main__':  # pragma: no cover
    test_bump_version()

# Generated at 2022-06-13 20:52:59.256216
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:53:07.460803
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
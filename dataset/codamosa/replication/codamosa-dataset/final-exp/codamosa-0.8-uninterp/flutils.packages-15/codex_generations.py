

# Generated at 2022-06-13 20:43:32.988310
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:43:43.974677
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:43:55.329875
# Unit test for function bump_version
def test_bump_version():
    """ Test function bump_version """

# Generated at 2022-06-13 20:44:01.637147
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:13.475891
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version
    """

    def _test(
            version: str,
            should: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ) -> None:
        try:
            got = bump_version(version, position=position,
                               pre_release=pre_release)
            assert got == should
        except:
            print("\nError in unit test for function "
                  "bump_version\n")
            raise

    _test('1.2.3', '1.2.4')
    _test('1.2.3', '1.3', position=1)
    _test('1.2.3', '2.0', position=0)

# Generated at 2022-06-13 20:44:15.993453
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version, get_version

    assert get_version() == bump_version(get_version())

# Generated at 2022-06-13 20:44:25.556763
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:35.631011
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version function."""
    kwargs = {
        'position': 2,
        'pre_release': None
    }
    assert bump_version('1.2.2', **kwargs) == '1.2.3'
    kwargs['position'] = 1
    assert bump_version('1.2.3', **kwargs) == '1.3'
    kwargs['position'] = 0
    assert bump_version('1.3.4', **kwargs) == '2.0'
    kwargs['pre_release'] = 'a'
    assert bump_version('1.2.3', **kwargs) == '1.2.4a0'
    kwargs['pre_release'] = 'a'

# Generated at 2022-06-13 20:44:41.950850
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function: :func`bump_version`."""

    # pylint: disable=C0116,C0103
    from unittest.mock import patch
    from itertools import permutations
    from random import randint
    from collections import namedtuple
    from flutils.packages import bump_version
    from importlib import reload as reload_module

    reload_module(bump_version)

# Generated at 2022-06-13 20:44:50.617867
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version"""
    import sys
    import unittest

    sys.path[0] = sys.path[0] + '_test'

    class TestCase(unittest.TestCase):
        """Test class"""

        def test_normal(self):
            """Test normal"""
            import nose.tools as nose_tools


# Generated at 2022-06-13 20:45:17.937060
# Unit test for function bump_version

# Generated at 2022-06-13 20:45:29.670687
# Unit test for function bump_version
def test_bump_version():
    '''
    Run: python -m flutils.packages

    '''
    # pylint: disable=R0914,R1702
    import unittest

    class TestBumpVersion(unittest.TestCase):
        def test_valid_positions(self):
            for position in (-3, -2, -1):
                with self.subTest(position=position):
                    self.assertEqual(
                        bump_version(
                            '1.2.3',
                            position=position
                        ),
                        '1.2.4'
                    )

# Generated at 2022-06-13 20:45:42.473401
# Unit test for function bump_version
def test_bump_version():
    """Test :func:`flutils.packages.bump_version`"""
    from flutils.packages import bump_version

    # These tests should not raise an error

# Generated at 2022-06-13 20:45:52.909486
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    import unittest
    import unittest.mock


    class DummyModule(object):
        """Object that is used for unit testing."""

    _msg = "Expected: %r\n  Actual: %r"
    _expected: Dict[str, Any]
    _actual: Dict[str, Any]
    _func_name: str


    class TestBumpVersion(unittest.TestCase):
        """Unit testing class for function bump_version."""

        def setUp(self: 'TestBumpVersion') -> None:
            """Set up method to be run before each unit test."""
            self.dut: DummyModule = DummyModule()
            self.dut.bump_version = bump_version
            self.dut.StrictVersion

# Generated at 2022-06-13 20:46:05.613421
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version.

    Test to ensure that all scenarios are handled.
    """
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:46:13.644646
# Unit test for function bump_version
def test_bump_version():
    '''
    Unit test for function bump_version
    '''
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:21.994649
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:33.147456
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:46.691776
# Unit test for function bump_version
def test_bump_version():
    """Test bump_version."""
    from unittest.case import TestCase


# Generated at 2022-06-13 20:46:51.086895
# Unit test for function bump_version
def test_bump_version():
    # TODO: Add unit tests
    pass


if __name__ == '__main__':
    raise ImportError(
        'You should import this module, not run it directly.'
    )

# Generated at 2022-06-13 20:47:10.244553
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version."""
    from pprint import pprint
    from inspect import getdoc
    from docopt import docopt
    from flutils.packages import bump_version

    doc = getdoc(bump_version)
    args = docopt(doc=doc, argv=[])


# Generated at 2022-06-13 20:47:17.929253
# Unit test for function bump_version
def test_bump_version():
    """Tests for the 'bump_version' function."""

    # Make a set of versions to test

# Generated at 2022-06-13 20:47:28.457669
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=W0613
    def get_results(position: int, pre_release: Optional[str], *args: str) -> List[str]:
        return [bump_version(x, position, pre_release) for x in args]


# Generated at 2022-06-13 20:47:39.229055
# Unit test for function bump_version
def test_bump_version():
    from .test import function_test


# Generated at 2022-06-13 20:47:48.522191
# Unit test for function bump_version
def test_bump_version():
    """Test the function :func:`bump_version`."""
    def _test_string(
            value: str,
            position: int,
            pre_release: Optional[str],
            expected: str
    ) -> None:
        actual = bump_version(value, position=position,
                              pre_release=pre_release)
        assert actual == expected, '%s : %s != %s' % (
            value,
            actual,
            expected
        )

    _test_string('3.4', 2, None, '3.4.1')
    _test_string('3.4.5', 2, None, '3.4.6')
    _test_string('3.4', 1, None, '3.5')

# Generated at 2022-06-13 20:47:58.847396
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version function.

        :return: None

        """
    from random import random

    from flutils.packages import compare_versions


# Generated at 2022-06-13 20:48:10.547465
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function :func:`flutils.packages.bump_version`."""
    from flutils.packages import bump_version

# Generated at 2022-06-13 20:48:21.873532
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:34.007180
# Unit test for function bump_version
def test_bump_version():
    """Unit test of function bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:39.475342
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:03.201271
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:13.122119
# Unit test for function bump_version
def test_bump_version():
    """Test function: bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:21.193662
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for the :func:`~flutils.packages.bump_version` function.

    """
    from flutils.packages import bump_version
    from flutils.testhelpers import make_test_suite, run_test_suite


# Generated at 2022-06-13 20:49:30.235182
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for function bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:41.619253
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for function bump_version
    """
    # pylint: disable=missing-docstring,too-many-locals,unused-variable
    from unittest import TestCase
    from flutils.packages import bump_version

    class Test_bump_version(TestCase):

        def test_bump(self):
            import string
            import random

            for _ in range(100):
                major = random.randint(1, 9)
                minor = random.randint(1, 99)
                patch = random.randint(1, 99)
                alpha = random.choice((0, 1))
                beta = random.choice((0, 1))
                alpha_n = random.randint(0, 99)
                beta_n = random.randint(0, 99)
                pre_release = random

# Generated at 2022-06-13 20:49:54.031218
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version
    """

# Generated at 2022-06-13 20:50:08.250274
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    """Unit test for function flutils.packages.bump_version()."""
    import sys  # pylint: disable=import-error,redefined-outer-name
    import logging  # pylint: disable=import-error,redefined-outer-name
    import unittest  # pylint: disable=import-error,redefined-outer-name

    class TestBumpVersion(unittest.TestCase):
        """Unit test class for function flutils.packages.bump_version()."""

        out_capture_fh = None
        err_capture_fh = None

        @classmethod
        def setUpClass(cls):
            """Set up class for unit test for flutils.packages.bump_version()."""
            # turn off logging output

# Generated at 2022-06-13 20:50:19.580770
# Unit test for function bump_version

# Generated at 2022-06-13 20:50:28.556760
# Unit test for function bump_version
def test_bump_version():
    """Test bumping a version number."""
    assert bump_version('1.2') == '1.2.0'
    assert bump_version('1.2.0') == '1.2.1'
    assert bump_version('1.2.1') == '1.2.2'
    assert bump_version('1.2', position=1) == '1.3'
    assert bump_version('1.3', position=1) == '1.4'
    assert bump_version('1.2.0', position=1) == '1.3'
    assert bump_version('1.2.1', position=1) == '1.3'
    assert bump_version('1.2.1', position=0) == '2.0'

# Generated at 2022-06-13 20:50:34.532365
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.packages import (
        _build_version_info,
        _build_version_bump_position,
        _build_version_bump_type,
        bump_version,
    )
    from flutils.common import print_string


# Generated at 2022-06-13 20:51:27.842501
# Unit test for function bump_version
def test_bump_version():
    def compare(v1, v2):
        v1 = StrictVersion(v1)
        v2 = StrictVersion(v2)
        if v1 == v2:
            return 0
        if v1 < v2:
            return -1
        return 1


# Generated at 2022-06-13 20:51:40.400299
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version"""

    def _test_bump_version(version: str, position: int, pre_release: Optional[str], expected: str):
        actual = bump_version(version, position, pre_release)
        assert actual == expected, 'bump_version(%r, %r, %r) == %r, expected: %r' % (
            version, position, pre_release, actual, expected)

    _test_bump_version('1.2.2', position=2, pre_release=None, expected='1.2.3')
    _test_bump_version('1.2.3', position=1, pre_release=None, expected='1.3')

# Generated at 2022-06-13 20:51:44.550161
# Unit test for function bump_version
def test_bump_version():

    assert bump_version('1.2.2') == '1.2.3'



# Generated at 2022-06-13 20:51:55.260371
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=W0613
    from pytest import raises

    re_base = "^The given value for '{0}', {1}, {2}$"
    raise_re_base = "^The given value for '{0}', {1}, must {2}$"
    raise_re_base2 = "^Only the '{0}' or '{1}' parts of the version number " \
                     "can get a prerelease bump.$"

    # 1.0
    assert bump_version('1.0') == '1.0.1'
    # 1.0.1
    assert bump_version('1.0.1') == '1.0.2'
    # 1.0.1.1

# Generated at 2022-06-13 20:52:04.766580
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    # noinspection PyUnresolvedReferences
    import pytest

    args: Dict[str, Any] = {
        'version': '1.2.3',
        'position': 2,
        'pre_release': None
    }
    err_msg = "The unit test for 'bump_version' failed."
    assert bump_version(**args) == '1.2.4', err_msg

    args['position'] = 1
    assert bump_version(**args) == '1.3', err_msg

    args['position'] = 0
    assert bump_version(**args) == '2.0', err_msg

    args['pre_release'] = 'a'
    assert bump_version(**args) == '1.2.4a0', err_msg

   

# Generated at 2022-06-13 20:52:18.464033
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    """Unit testing for function bump_version."""
    from flutils.packages import bump_version

    print('Starting unit test for function: bump_version')
    # pylint: disable=line-too-long

# Generated at 2022-06-13 20:52:32.180582
# Unit test for function bump_version
def test_bump_version():
    """Test bump_version function by calling it and comparing the result."""
    print('--- Bump version tests')
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:52:40.138522
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    # pylint: disable=E1101
    # Test: no pre-release
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('2.1.3', position=1) == '2.2'
    # Test: a, alpha
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

# Generated at 2022-06-13 20:52:47.358704
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for function bump_version"""
    # Basic text
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump

# Generated at 2022-06-13 20:52:51.390192
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version from the module bump_version."""
    from unittest import TestCase, mock
    from sys import version_info
    from itertools import product
    from flutils.packages import bump_version

    class Test(TestCase):
        """Test the function bump_version."""

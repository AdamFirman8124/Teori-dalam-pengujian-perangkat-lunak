

# Generated at 2022-06-13 20:43:33.330021
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""

    from os import linesep as eol

    from flutils.packages import (
        bump_version
    )

    # Tests for bump_version

# Generated at 2022-06-13 20:43:38.100593
# Unit test for function bump_version
def test_bump_version():
    # This is here to force the unit test to run - Travis CI will not run
    # if there are no classes or functions in a module
    assert bump_version('1.2.3') == '1.2.3'

# Generated at 2022-06-13 20:43:46.304780
# Unit test for function bump_version
def test_bump_version():
    """Test flutils.packages.bump_version with pytest."""
    import pytest


# Generated at 2022-06-13 20:43:56.558199
# Unit test for function bump_version
def test_bump_version():
    """Test the version number increment function.

    :return:

    """
    from flutils.packages import bump_version

    #
    # Basic major, minor, and patch level testing.
    #
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

    #
    # Basic pre-release testing
    #
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

# Generated at 2022-06-13 20:44:07.061782
# Unit test for function bump_version
def test_bump_version():
    big_ver = '1.2.3'
    big_pos = 2
    big_pre = None
    big_bump_type = _BUMP_VERSION_PATCH
    _bump_version(big_ver, big_pos, big_pre, big_bump_type)

    med_ver = '1.2.3'
    med_pos = 1
    med_pre = None
    med_bump_type = _BUMP_VERSION_MINOR
    _bump_version(med_ver, med_pos, med_pre, med_bump_type)

    ver_pre_a = '1.2.3a0'
    pos_pre_a = 2
    pre_pre_a = 'a'
    bump_pre_a = _BUMP_VERSION_PATCH_ALPHA


# Generated at 2022-06-13 20:44:10.061842
# Unit test for function bump_version
def test_bump_version():
    return bump_version('1.2.3') == '1.2.4'

if __name__ == '__main__':
    print(test_bump_version())

# Generated at 2022-06-13 20:44:17.732669
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version
    from flutils.strings import force_str
    from . import test_version_info

    def _test(version: str,
              position: int = 2,
              pre_release: Optional[str] = None):
        info = test_version_info(version)
        new_version = bump_version(version, position, pre_release)
        new_info = test_version_info(new_version)
        bp = _build_version_bump_position(position)
        bt = _build_version_bump_type(bp, pre_release)
        if bt == _BUMP_VERSION_MAJOR:
            if info.major.num < 9:
                assert new_info.major.num == info.major.num + 1
            else:
                assert new

# Generated at 2022-06-13 20:44:26.236579
# Unit test for function bump_version

# Generated at 2022-06-13 20:44:36.126375
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:47.189716
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version

    # noinspection PyUnusedLocal
    def _build_tests(
            version: str,
            position: int,
            pre_release: Optional[str],
            expected: str,
    ) -> None:
        actual = bump_version(version, position, pre_release)
        assert actual == expected

    _build_tests('1.2.2', 2, None, '1.2.3')
    _build_tests('1.2.3', 1, None, '1.3')
    _build_tests('1.3.4', 0, None, '2.0')
    _build_tests('1.2.3', 1, 'a', '1.2.4a0')

# Generated at 2022-06-13 20:45:09.133996
# Unit test for function bump_version
def test_bump_version():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:45:17.010180
# Unit test for function bump_version

# Generated at 2022-06-13 20:45:29.258767
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""

    # Major
    ver = '1.0'
    new_ver = bump_version(ver, 0)
    assert new_ver == '2.0'
    new_ver = bump_version(ver, 0, 'a')
    assert new_ver == '1.0a0'
    new_ver = bump_version(ver, 0, 'alpha')
    assert new_ver == '1.0a0'
    new_ver = bump_version(ver, 0, 'b')
    assert new_ver == '1.0b0'
    new_ver = bump_version(ver, 0, 'beta')
    assert new_ver == '1.0b0'
    # Minor
    ver = '1.0'
    new_ver = bump_version(ver, 1)

# Generated at 2022-06-13 20:45:42.426127
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.packages import bump_version
    from flutils.testing import (
        UnitTester,
        get_data_path,
    )
    ut = UnitTester()
    from flutils.packages import bump_version
    from flutils.testing import get_data_path

    inp = '1.2.4a1'
    out = '1.2.4a2'
    ut.assert_str(bump_version(inp, position=2, pre_release='a'), out)

    inp = '1.2.4a1'
    out = '1.2.4a1'
    ut.assert_str(bump_version(inp, pre_release='b'), out)


# Generated at 2022-06-13 20:45:52.868956
# Unit test for function bump_version
def test_bump_version():
    """ Test function bump_version. """
    import pytest
    from flutils.packages import bump_version
    # Test with complete version number
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:46:05.613428
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:13.644423
# Unit test for function bump_version
def test_bump_version():
    min_ver = '1.2.3'
    assert bump_version('1.2.2') == min_ver
    assert bump_version('1.2.2', position=1) == min_ver
    assert bump_version('1.2.2', position=4) == min_ver
    assert bump_version('1.2.2', position=2) == min_ver
    assert bump_version('1.2.2', position=3) == min_ver
    assert bump_version('1.2.2', position=5) == min_ver
    assert bump_version('1.2.2', position=6) == min_ver
    assert bump_version('1.2.2', position=2) == min_ver
    assert bump_version('1.2.2', position=2, pre_release='a')

# Generated at 2022-06-13 20:46:21.995675
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2022-06-13 20:46:32.162697
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:46.103458
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

# Generated at 2022-06-13 20:47:13.632486
# Unit test for function bump_version
def test_bump_version():
    from unittest import TestCase
    from unittest.mock import patch
    from flutils.tests.packages import (
        CAPTURED_STDIO,
        captured_stdio,
        patch_expect,
        PatchExpect,
    )

    class TestBumpVersion(TestCase):
        def test_bump_version(self):
            self.assertEqual('1.2.3', bump_version('1.2.2'))

        def test_bump_version_2(self):
            self.assertEqual('1.3', bump_version('1.2.3', position=1))

        def test_bump_version_3(self):
            self.assertEqual('2.0', bump_version('1.3.4', position=0))


# Generated at 2022-06-13 20:47:23.581473
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:47:29.752366
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    # pylint: disable=R0914
    ver = '1.2.3'
    out = bump_version(ver)
    exp = '1.2.4'
    assert out == exp

    ver = '1.2.3'
    out = bump_version(ver, position=1)
    exp = '1.3'
    assert out == exp

    ver = '1.3.4'
    out = bump_version(ver, position=0)
    exp = '2.0'
    assert out == exp

    ver = '1.2.3'
    out = bump_version(ver, pre_release='a')
    exp = '1.2.4a0'
    assert out == exp


# Generated at 2022-06-13 20:47:40.989926
# Unit test for function bump_version
def test_bump_version():
    """Test the function :func:`bump_version`."""

# Generated at 2022-06-13 20:47:49.717157
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:47:59.524869
# Unit test for function bump_version
def test_bump_version(): # pylint: disable = W0612, W0613
    from unittest import TestCase
    from xml.etree import ElementTree


    class Test_bump_version(TestCase):

        def test_basic_upgrade(self):
            self.assertEqual(bump_version('1.0.0'), '1.0.1')
            self.assertEqual(bump_version('1.0.0', position=1), '1.1')
            self.assertEqual(bump_version('1.0.0', position=0), '2.0')

        def test_basic_downgrade(self):
            self.assertEqual(bump_version('1.0.0', position=-2), '1.0.0')

# Generated at 2022-06-13 20:48:10.610550
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=import-outside-toplevel
    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:48:21.908722
# Unit test for function bump_version
def test_bump_version():
    """Tests for the ``bump_version`` function."""
    assert bump_version('1.2.2') == '1.2.3'  # type: ignore
    assert bump_version('1.2.3', position=1) == '1.3'  # type: ignore
    assert bump_version('1.3.4', position=0) == '2.0'  # type: ignore
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'  # type: ignore
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'  # type: ignore
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'  #

# Generated at 2022-06-13 20:48:25.777082
# Unit test for function bump_version
def test_bump_version():

    from flutils.packages import bump_version
    from flutils.testing import get_module_attr_value

    version, position, pre_release = get_module_attr_value(
        __name__,
        '_test_bump_version',
        is_all=True
    )
    out = bump_version(version, position, pre_release)
    _test_bump_version_expected = get_module_attr_value(
        __name__,
        '_test_bump_version_expected'
    )
    assert out == _test_bump_version_expected, out



# Generated at 2022-06-13 20:48:35.467377
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version()."""
    try:
        bump_version('1.2.2')
    except Exception:
        assert False, 'Failed bump_version("1.2.2")'

    try:
        bump_version('1.2.3', position=1)
    except Exception:
        assert False, 'Failed bump_version("1.2.3", position=1)'

    try:
        bump_version('1.3.4', position=0)
    except Exception:
        assert False, 'Failed bump_version("1.3.4", position=0)'

    try:
        bump_version('1.2.3', prerelease='a')
    except Exception:
        assert False, 'Failed bump_version("1.2.3", prerelease="a")'


# Generated at 2022-06-13 20:48:56.168035
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version function.

    *New in version 0.3*

    Args:
        None

    Returns:
        None

    """
    # Initialize key variables
    expected_result = '0.40.0'

    # Test
    result = bump_version('0.39.0')
    assert(expected_result == result)


if __name__ == '__main__':
    # Test the function
    test_bump_version()

# Generated at 2022-06-13 20:49:01.308220
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a0', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:49:12.156937
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('0.0.0') == '0.0.1'
    assert bump_version('1.2.1', 1) == '1.3'
    assert bump_version('1.3.1', 0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'


# Generated at 2022-06-13 20:49:18.790478
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    from flutils.packages import bump_version

# Generated at 2022-06-13 20:49:29.126168
# Unit test for function bump_version
def test_bump_version():
    import copy

    from flutils.packages import bump_version

    def test_data(
            func,
            ver_pos_pre,
            should_raised,
            raise_exc):
        ver, pos, pre = ver_pos_pre
        try:
            func(ver, position=pos, pre_release=pre)
        except Exception as err:
            if should_raised is False:
                return False
            if raise_exc:
                if isinstance(err, raise_exc) is False:
                    raise
            raise
        return True


# Generated at 2022-06-13 20:49:41.133439
# Unit test for function bump_version
def test_bump_version():
    from flutils.tests import parametrize
    from flutils.tests import run_test_module_by_name

    # noinspection PyUnusedLocal
    def run_tests() -> bool:
        def test_bump_version_inputs(
                version: str,
                position: int,
                pre_release: Optional[str],
                expected: str
        ) -> None:
            result = bump_version(version, position, pre_release)
            assert result == expected


# Generated at 2022-06-13 20:49:53.671393
# Unit test for function bump_version
def test_bump_version():
    """Test ``bump_version``.

    """
    # pylint: disable=E1123
    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version

# Generated at 2022-06-13 20:50:08.486890
# Unit test for function bump_version
def test_bump_version():
    out = bump_version('1.2.2')
    assert out == '1.2.3'

    out = bump_version('1.2.3', position=1)
    assert out == '1.3'

    out = bump_version('1.3.4', position=0)
    assert out == '2.0'

    out = bump_version('1.2.3', prerelease='a')
    assert out == '1.2.4a0'

    out = bump_version('1.2.4a0', pre_release='a')
    assert out == '1.2.4a1'

    out = bump_version('1.2.4a1', pre_release='b')
    assert out == '1.2.4b0'


# Generated at 2022-06-13 20:50:19.735284
# Unit test for function bump_version
def test_bump_version():
    """
    Test the bump_version function.
    """
    import sys
    import unittest

    class TestBumpVersion(unittest.TestCase):
        """
        Test the bump_version function.
        """
        def test_major(self):
            """
            Test the major part of the version number.
            """
            self.assertEqual(bump_version('1.2.3', position=0), '2.0')
            self.assertEqual(bump_version('2.4.5', position=0), '3.0')
            self.assertEqual(bump_version('3.9.11', position=0), '4.0')

        def test_minor(self):
            """
            Test the minor part of the version number.
            """

# Generated at 2022-06-13 20:50:26.473069
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

# Generated at 2022-06-13 20:50:52.170247
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version."""
    # pylint: disable=W0105

# Generated at 2022-06-13 20:51:04.504427
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=W0612
    from sys import modules
    from unittest import TestCase, skip, TestSuite, TextTestRunner
    from unittest.mock import patch

    class _TestBumpVersion(TestCase):
        """Unit test for function bump_version."""

        def test_bump_version(self):
            """Unit test"""
            expected = '2.0.0'
            actual = bump_version('1.2.3', position=0)
            self.assertEqual(expected, actual)

        def test_bump_version_dont_bump_pre_release(self):
            """Unit test"""
            expected = '2.0.0'
            actual = bump_version('1.2.3.4.5a0', position=0)
            self.assertE

# Generated at 2022-06-13 20:51:13.014298
# Unit test for function bump_version

# Generated at 2022-06-13 20:51:20.432746
# Unit test for function bump_version
def test_bump_version():
    from copy import copy


# Generated at 2022-06-13 20:51:29.222112
# Unit test for function bump_version
def test_bump_version():
    from nose.tools import assert_equals
    test_data = [
        ('0.0.0', ''),
        ('0.0.1', ''),
        ('0.1.0', ''),
        ('0.1.1', ''),
        ('1.0.0', ''),
        ('1.0.1', ''),
        ('1.1.0', ''),
        ('1.1.1', ''),
    ]
    for version, pre_release in test_data:
        new_version = bump_version(version, pre_release=pre_release)
        expected_version = '%s.1' % (version.split('.')[0])
        assert_equals(
            expected_version, new_version
        )

# Generated at 2022-06-13 20:51:40.880149
# Unit test for function bump_version
def test_bump_version():
    """Test the function ``bump_version``."""

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version

# Generated at 2022-06-13 20:51:54.145755
# Unit test for function bump_version
def test_bump_version():
    print('bump_version started')
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:52:04.244673
# Unit test for function bump_version
def test_bump_version():

    # Test valid input and output for a bunch of different values
    versions = [
        '1.2.0', '1.1.7', '1.1.7a0', '1.1.7b1', '1.2.7a3', '1.2.7b3',
        '1.2.7', '0.0.0', '1.1.0', '1.1.0a15'
    ]

    for version in versions:
        assert(bump_version(version) == StrictVersion(version)._incr(2))

    # Test invalid input
    invalid_versions = ['a', '1.1', '1.0.0b', '1.0.1b3a1', '2.0.0a3b3']


# Generated at 2022-06-13 20:52:18.394352
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    versions: List[Tuple[str, str]] = [
        ('1.2.3', '1.2.4'),
        ('1.3.4', '1.4'),
        ('2.1.3', '3.0'),
        ('1.2.3', '1.2.4a0'),
        ('1.2.4a0', '1.2.4a1'),
        ('1.2.4a1', '1.2.4b0'),
        ('1.2.4a1', '1.2.4'),
        ('1.2.4b0', '1.2.4'),
        ('2.1.3', '2.2a0'),
        ('1.2b0', '1.2.1'),
    ]


# Generated at 2022-06-13 20:52:32.145715
# Unit test for function bump_version
def test_bump_version():
    """Tests for the function bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:53:06.653917
# Unit test for function bump_version
def test_bump_version():
    """Testing the flutils.packages.bump_version() function."""
    from flutils.packages import bump_version

    def _build_test(
            ver_in: str,
            ver_out: Optional[str],
            pos: int,
            pre: Optional[str]
    ) -> None:
        msg = "in: '{}', out: '{}', pos: '{}', pre: '{}'".format(
            ver_in, ver_out, pos, pre
        )
        ver_out = cast(str, ver_out)
        ver = bump_version(ver_in, position=pos, pre_release=pre)
        assert ver == ver_out, msg

    # Testing to ensure that bumping a given version works as expected.
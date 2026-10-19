

# Generated at 2022-06-13 20:43:29.300787
# Unit test for function bump_version
def test_bump_version():
    version = bump_version('1.2.2')
    assert version == '1.2.3'
    version = bump_version('1.2.3', position=1)
    assert version == '1.3'
    version = bump_version('1.3.4', position=0)
    assert version == '2.0'
    version = bump_version('1.2.3', prerelease='a')
    assert version == '1.2.4a0'
    version = bump_version('1.2.4a0', pre_release='a')
    assert version == '1.2.4a1'
    version = bump_version('1.2.4a1', pre_release='b')
    assert version == '1.2.4b0'

# Generated at 2022-06-13 20:43:41.328547
# Unit test for function bump_version
def test_bump_version():
    import random
    import string
    # noinspection PyUnusedLocal
    spacer = ' '
    good = []
    bad = []
    # noinspection PyUnusedLocal
    num = 0

    def fn1(
            ver_str: str,
            position: int = 0,
            pre_release: Union[str, None] = None,
            is_good: bool = True
    ) -> None:
        """Test the ``version`` and ``position`` arguments."""
        # Change random things -- good test, still must work
        if is_good is True:
            lst = list(ver_str)
            for index in range(0, 5):
                lst[random.randint(0, len(lst) - 1)] = '0'
            ver_str = ''.join(lst)
       

# Generated at 2022-06-13 20:43:53.059366
# Unit test for function bump_version
def test_bump_version():
    """
    Tests function bump_version
    """
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:00.387111
# Unit test for function bump_version

# Generated at 2022-06-13 20:44:12.635177
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0914,R0201,W0613,W0110
    """Testing the 'bump_version' function from this module.
    """

    from flutils.testing import AssertEqual
    from flutils.testing import AssertRaises

    with AssertRaises(ValueError, 'a version number.*'):
        bump_version('1')

    with AssertRaises(ValueError, 'a version number.*'):
        bump_version('1.2')

    with AssertRaises(ValueError, 'a version number.*'):
        bump_version('1.2.3.4')

    with AssertRaises(ValueError,
                      "The given value for 'position', '10', must be an"):
        bump_version('1.2.3', position=10)


# Generated at 2022-06-13 20:44:24.370267
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version

    # Test that versions work correctly
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'


# Generated at 2022-06-13 20:44:35.019294
# Unit test for function bump_version
def test_bump_version():
    """
    Test function ``bump_version``.

    *New in version 0.3*

    """
    def _test_func(version, position, pre_release, exp):
        try:
            act = bump_version(version, position, pre_release)
        except Exception as err:
            act = '%s: %s' % (type(err).__name__, err)
        return act == exp


# Generated at 2022-06-13 20:44:46.334181
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version."""
    from flutils.packages import bump_version
    from flutils.test_helpers import unit_test

    # Test the functions primary functionality.
    # noinspection PyProtectedMember

# Generated at 2022-06-13 20:44:54.499051
# Unit test for function bump_version

# Generated at 2022-06-13 20:45:04.993237
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version."""
    import pytest

    # Test basic version bumps
    assert bump_version('1.0') == '1.1'
    assert bump_version('1.0.0') == '1.0.1'
    assert bump_version('1.0', position=0) == '2.0'
    assert bump_version('1.0.0', position=0) == '2.0'

    # Test version bumps with pre-releases
    assert bump_version('1.0a0') == '1.0a1'
    assert bump_version('1.0a1') == '1.0a2'
    assert bump_version('1.0b0') == '1.0b1'
    assert bump_version('1.0b1') == '1.0b2'

# Generated at 2022-06-13 20:45:32.459192
# Unit test for function bump_version
def test_bump_version():
    """Test for bump_version function."""
    from flutils.apptools import SimpleNamespace
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:45:45.266520
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version"""
    # pylint: disable=C0103
    def _assert_equal(
            args: Tuple[str, int, Optional[str]],
            expect: str
    ) -> None:
        """Local assert function"""
        actual = bump_version(*args)
        assert actual == expect

    _assert_equal(('1.2.2',), '1.2.3')
    _assert_equal(('1.2.2', 0), '2.0')
    _assert_equal(('1.2.2', 1), '1.3')
    _assert_equal(('1.2.2', 2), '1.2.3')
    _assert_equal(('1.2.3', 0), '2.0')

# Generated at 2022-06-13 20:45:55.487268
# Unit test for function bump_version
def test_bump_version():
    import time
    import unittest

    class UnitTest(unittest.TestCase):
        def setUp(self):
            self.start_time = time.time()

        def tearDown(self):
            t = time.time() - self.start_time
            print('%s: %0.3f' % (self.id(), t))

        def test_bump_version(self):
            self.assertEqual(bump_version('1.2.2'), '1.2.3')
            self.assertEqual(bump_version('1.2.3', position=1), '1.3')
            self.assertEqual(bump_version('1.3.4', position=0), '2.0')

# Generated at 2022-06-13 20:46:07.207135
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version."""
    from pathlib import Path
    import sys
    import unittest
    from unittest.mock import Mock

    from flutils.packages import bump_version
    from flutils.systemutils import (
        is_executable_in_path,
        run_command,
    )

    try:
        import coverage
    except ImportError:
        coverage = None

    # Python 2 and 3 compatibility
    old_pyver = sys.version_info[:2]
    if old_pyver <= (3, 3):
        cmd_arg = 'command'
    else:
        # noinspection PyCompatibility
        cmd_arg = 'args'


# Generated at 2022-06-13 20:46:20.441691
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    """Test the function bump_version."""
    print(bump_version('1.2.2'))
    print(bump_version('1.2.3', position=1))
    print(bump_version('1.3.4', position=0))
    print(bump_version('1.2.3', prerelease='a'))
    print(bump_version('1.2.4a0', pre_release='a'))
    print(bump_version('1.2.4a1', pre_release='b'))
    print(bump_version('1.2.4a1'))
    print(bump_version('1.2.4b0'))

# Generated at 2022-06-13 20:46:32.663799
# Unit test for function bump_version
def test_bump_version():
    this = bump_version('1.2.2')
    assert this == '1.2.3', 'The incremented version number is wrong.'
    this = bump_version('1.2.3', position=1)
    assert this == '1.3', 'The incremented version number is wrong.'
    this = bump_version('1.3.4', position=0)
    assert this == '2.0', 'The incremented version number is wrong.'
    this = bump_version('1.2.3', prerelease='a')
    assert this == '1.2.4a0', 'The incremented version number is wrong.'
    this = bump_version('1.2.4a0', pre_release='a')
    assert this == '1.2.4a1', 'The incremented version number is wrong.'

# Generated at 2022-06-13 20:46:46.408994
# Unit test for function bump_version

# Generated at 2022-06-13 20:46:58.902090
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version.

    *New in version 0.3*
    """
    import flutils.packages


# Generated at 2022-06-13 20:47:11.482739
# Unit test for function bump_version
def test_bump_version():
    ver_str = '1.2.3'
    assert bump_version(ver_str, 0) == '2.0'
    assert bump_version(ver_str, 1) == '1.3'
    assert bump_version(ver_str, 2) == '1.2.4'
    ver_str = '1.2.4a0'
    assert bump_version(ver_str, 2) == '1.2.4a1'
    ver_str = '1.2.4a1'
    assert bump_version(ver_str, 2) == '1.2.4a2'
    assert bump_version(ver_str, 2, 'b') == '1.2.4b0'
    assert bump_version(ver_str, 2) == '1.2.5'
    assert bump_

# Generated at 2022-06-13 20:47:18.654267
# Unit test for function bump_version
def test_bump_version(): # pylint: disable=R0914
    """Test the ``bump_version`` function."""
    from flutils.packages import bump_version
    from flutils.status import Status

    _STATUS: Status = Status(header='Test: flutils.packages.bump_version')

    _OK: str = 'OK'
    _NO: str = 'NO'
    _ERROR: str = 'ERROR'

    _FUNC_INFO: str = str(bump_version)

    _RESULTS: List[Tuple[
        str,
        str,
        str,
        Union[str, Exception],
        str,
        str,
    ]] = []


# Generated at 2022-06-13 20:47:42.037123
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

    from sys import modules
    from unittest import TestCase
    from unittest.mock import MagicMock
    from unittest.mock import patch
    from unittest.mock import sentinel
    from unittest.mock import Mock

    from flutils.packages import get_pkg_version

    class BumpVersionTest(TestCase):  # pylint: disable=too-few-public-methods
        """Unit test for function bump_version."""

        def test_bump_version_exceptions(self):
            """Test exceptions in bump_version."""

            with self.assertRaises(ValueError):
                bump_version('1.2.0', pre_release='asdf')

# Generated at 2022-06-13 20:47:49.934545
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=too-many-statements
    import unittest

    class TestBumpVersion(unittest.TestCase):
        """Unit tests for the bump_version function."""

        def test_patch_no_pre_release(self) -> None:
            """Test patch bumping with no pre-release."""
            self.assertEqual(
                bump_version('1.2.2'),
                '1.2.3'
            )

        def test_patch_bump_pre_release__no_pre_release(self) -> None:
            """Test patch bumping with no pre-release."""
            self.assertEqual(
                bump_version('1.2.3', position=1),
                '1.3'
            )


# Generated at 2022-06-13 20:47:59.641197
# Unit test for function bump_version

# Generated at 2022-06-13 20:48:10.644092
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:21.942591
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:34.040547
# Unit test for function bump_version
def test_bump_version():
    """Test function 'bump_version'."""

    def _test(
            version: str,
            position: Optional[int] = None,
            pre_release: Optional[str] = None
    ) -> None:
        """Test 'bump_version' for a given version number.

        Args:
            version (str): The version number to test.
            position (int, optional): The version position to bump.
            pre_release (str, optional): The pre-release to bump.

        """
        if position is None:
            position = 2
        bmprs = bump_version(version, position=position,
                             pre_release=pre_release)
        ver_obj = StrictVersion(bmprs)

# Generated at 2022-06-13 20:48:39.496652
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for 'bump_version' function."""
    ver_str = '1.2.2'

# Generated at 2022-06-13 20:48:48.819415
# Unit test for function bump_version
def test_bump_version():
    """Simple unit test for function bump_version."""
    from unittest import TestCase
    from unittest.mock import patch

    from flutils.packages import bump_version

    class Test(TestCase):

        @patch('flutils.packages.StrictVersion')
        def test_bump_version_patch(self, mock_strictversion):
            """Test the 'patch' part of the version number."""
            mock_strictversion.return_value.version = (1, 2, 3)
            mock_strictversion.return_value.prerelease = None
            self.assertEqual(bump_version('1.2.3'), '1.2.4')


# Generated at 2022-06-13 20:48:58.068685
# Unit test for function bump_version
def test_bump_version():
    """Test for function "bump_version"."""

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version

# Generated at 2022-06-13 20:49:05.069996
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version

    *New in version 0.3*

    """
    version = '1.2.3'
    assert bump_version(version) == '1.2.4'
    assert bump_version(version, position=1) == '1.3'
    assert bump_version(version, position=0) == '2.0'
    assert bump_version(version, pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'


# Generated at 2022-06-13 20:49:19.887497
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

# Generated at 2022-06-13 20:49:28.815540
# Unit test for function bump_version
def test_bump_version():
    """Test bump_version function."""

# Generated at 2022-06-13 20:49:40.969854
# Unit test for function bump_version
def test_bump_version():
    from unittest import TestCase
    test = TestCase()
    class RestTest(TestCase):
        def assertRaisesWithString(self, exc_type, exc_string, func, *args):
            try:
                func(*args)
                self.fail()
            except exc_type as e:
                assert e == exc_string

        def assertRaisesWithValueError(self, string, func, *args):
            self.assertRaisesWithString(ValueError, string, func, *args)

        def test_bump_version_minor_to_minor_alpha(self):
            result = bump_version('1.2.3', position=1, pre_release='a')
            assert result == '1.3a0'


# Generated at 2022-06-13 20:49:53.564498
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    # noinspection SpellCheckingInspection

# Generated at 2022-06-13 20:50:08.447520
# Unit test for function bump_version
def test_bump_version():
    """Test the function :obj:`bump_version`."""
    from .data.packages import test_bump_version as test_data

    for data in test_data:
        version = data['version']
        position = data['position']
        pre_release = data.get('pre_release', None)
        out = bump_version(version, position, pre_release)
        msg = (
            "The 'bump_version' function failed with "
            "version: '%s', position: '%s', pre_release: '%s'.\n"
            "Expected: '%s', got: '%s.'"
        ) % (version, position, pre_release, data['expected'], out)
        assert out == data['expected'], msg


# if __name__ == '__main__':
#    

# Generated at 2022-06-13 20:50:19.695618
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:50:29.291461
# Unit test for function bump_version
def test_bump_version():
    print("Starting unit test for function bump_version.")
    # Create a list of tuples:
    #     version, position, pre_release, output
    # When a value of None is given for 'pre_release' it is ignored.

# Generated at 2022-06-13 20:50:38.783671
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:50:50.212949
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:51:02.554315
# Unit test for function bump_version
def test_bump_version():
    import os
    import sys

    if os.name == 'nt':
        return
    version_string = '1.2.3'

    assert bump_version(version_string) == '1.2.4'

    assert bump_version(version_string, position=1) == '1.3'

    assert bump_version(version_string, position=0) == '2.0'

    assert bump_version(version_string, pre_release='a') == '1.2.4a0'

    assert bump_version(version_string, pre_release='b') == '1.2.4b0'

    assert bump_version(
        bump_version(version_string, pre_release='a'),
        pre_release='a'
    ) == '1.2.4a1'


# Generated at 2022-06-13 20:51:18.580315
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=too-many-branches,too-many-statements
    # pylint: disable=too-many-locals,too-many-nested-blocks
    from random import randint
    from string import ascii_lowercase
    from itertools import product

    def _build_version(
            add_minor_pre_release: Optional[bool],
            add_patch_pre_release: Optional[bool],
            use_numbers_only: Optional[bool],
            use_chars_only: Optional[bool]
    ) -> List[Tuple[int, str, int]]:
        major_num = randint(1, 100)

        if use_chars_only is True:
            minor_num = ascii_lowercase[randint(0, 25)]
            patch_

# Generated at 2022-06-13 20:51:28.852075
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:51:40.696681
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    func = bump_version

# Generated at 2022-06-13 20:51:54.037415
# Unit test for function bump_version
def test_bump_version():
    from pytest import warns, raises
    from flutils.packages import bump_version
    from distutils.version import StrictVersion

    # Basic version bumping
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.4.5', position=1) == '2.0'
    assert bump_version('1.2.3', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_

# Generated at 2022-06-13 20:52:04.183792
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    import unittest
    import unittest.mock

    class _BumpVersionTester(unittest.TestCase):
        """Internal test class for function bump_version."""

# Generated at 2022-06-13 20:52:18.363564
# Unit test for function bump_version
def test_bump_version():
    """Tests for function bump_version

    :rtype: None
    """

# Generated at 2022-06-13 20:52:32.146512
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    import pytest  # pylint: disable=import-error
    from .core import _UTILS_TESTING_VERSION

    assert bump_version('1.0.0') == '1.0.1'
    assert bump_version('1.0.1') == '1.0.2'
    assert bump_version('1.0.0', position=0) == '2.0'

    try:
        bump_version(_UTILS_TESTING_VERSION)
    except ValueError:
        pytest.fail("bump_version() raised ValueError unexpectedly!")

    with pytest.raises(ValueError):
        bump_version('1.0.0a0', position=0, pre_release='a')


# Generated at 2022-06-13 20:52:40.096671
# Unit test for function bump_version
def test_bump_version():
    """ Tests function bump_version
    """
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:52:47.340021
# Unit test for function bump_version
def test_bump_version():
    print('bump_version')
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:52:59.557416
# Unit test for function bump_version
def test_bump_version():
    """ Unit test for function bump_version. """
    import math


    def _t1(
            version: str,
            position: int,
            pre_release: Optional[str],
            exp_out: str
    ) -> None:
        """ Test function bump_version.

            Args:
                version (str):
                    Version number to be passed to bump_version().
                position (int):
                    Position to be passed to bump_version().
                pre_release (str):
                    Pre-release to be passed to bump_version().
                exp_out (str):
                    The expected output from bump_version().
        """
        out = bump_version(version, position, pre_release)
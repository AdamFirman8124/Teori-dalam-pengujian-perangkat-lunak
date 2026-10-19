

# Generated at 2022-06-13 20:43:29.296410
# Unit test for function bump_version
def test_bump_version():
    """Quick test for the bump_version function."""
    import sys
    import os
    import unittest
    sys.path.append(os.path.abspath('flutils'))
    from flutils import bump_version

    class TestBumpVersion(unittest.TestCase):
        def test_bump_version_1(self):
            """Bumps a version number from '1.2.3' to '1.2.4'."""
            self.assertEqual(
                bump_version('1.2.3'),
                '1.2.4',
            )

        def test_bump_version_2(self):
            """Bumps a version number from '1.2.3' to '1.3'."""

# Generated at 2022-06-13 20:43:41.329119
# Unit test for function bump_version

# Generated at 2022-06-13 20:43:42.783364
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function ``bump_version``."""
    pass

# Generated at 2022-06-13 20:43:54.319351
# Unit test for function bump_version

# Generated at 2022-06-13 20:44:01.096474
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:13.229742
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:44:24.446868
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

# Generated at 2022-06-13 20:44:35.095973
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

# Generated at 2022-06-13 20:44:46.410888
# Unit test for function bump_version
def test_bump_version():

    def test_feature(version, position, pre_release, expected):
        result = bump_version(version, position, pre_release)
        msg_tmpl = "'{0}' - '{1}' - '{2}' - '{3}' - '{4}'"
        msg = msg_tmpl.format(version, position, pre_release, expected, result)
        assert result == expected, msg

    # noinspection PyUnusedLocal
    def test_bug(version, position, pre_release, exception, exc_msg):
        try:
            bump_version(version, position, pre_release)
        except exception as e:
            msg_tmpl = "'{0}' - '{1}' - '{2}' - '{3}' - '{4}'"
            msg = msg_tmpl

# Generated at 2022-06-13 20:44:53.498672
# Unit test for function bump_version
def test_bump_version():
    """Test function 'bump_version'."""

# Generated at 2022-06-13 20:45:18.494156
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0914,R0915,C0116
    """Unit test for function bump_version"""
    from collections import namedtuple
    from sys import version_info
    if version_info < (3, 7):
        from flutils.units import unittest
    else:
        import unittest
    from flutils.packages import bump_version

    class TestBumpVersion(unittest.TestCase):
        """Unit test for function bump_version"""

        def test_bump_version(self):
            """Test for function bump_version"""
            TestData: namedtuple = namedtuple(
                'TestData', 'version position pre_release expected_result'
            )

# Generated at 2022-06-13 20:45:30.117368
# Unit test for function bump_version
def test_bump_version():
    import sys
    import time
    from flutils.packages import show_versions
    from flutils.testing import suppress_stdout, suppress_warnings

    ver_pattern = r'^\d+\.\d+\.(\d+|\d+a\d+|\d+b\d+)$'

# Generated at 2022-06-13 20:45:42.658557
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

    def _do_test(
            version: str,
            position: int,
            pre_release: str,
            should_be: str
    ) -> None:
        actual = bump_version(version, position, pre_release)
        assert actual == should_be, "Failed to bump version %r" % version

    _do_test('1.2.2', 2, '', '1.2.3')
    _do_test('1.2.3', 1, '', '1.3')
    _do_test('1.3.4', 0, '', '2.0')
    _do_test('1.2.3', 2, 'a', '1.2.4a0')

# Generated at 2022-06-13 20:45:53.133742
# Unit test for function bump_version
def test_bump_version():
    """ Tests for the bump version function. """
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:05.726277
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0914
    # type: () -> None
    """Test function bump_version.

    *New in version 0.3*

    """
    from sys import version_info
    from pytest import raises
    from flutils.packages import bump_version
    from flutils.packages.bump_version import _build_version_info

    if version_info.major != 3 or version_info.minor < 4:
        raise AssertionError(
            'This unit test requires, at least, Python 3.4 to test "str.isidentifier()".'
        )

    # Testing: _build_version_info
    version_info = _build_version_info('1.2.3')
    assert version_info.version == '1.2.3'

# Generated at 2022-06-13 20:46:19.144888
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

# Generated at 2022-06-13 20:46:25.082936
# Unit test for function bump_version
def test_bump_version():
    from .dummy import (
        FunctionNotDefined,
        test_code_output,
    )
    FunctionNotDefined(test_code_output, 'bump_version')



# Generated at 2022-06-13 20:46:34.121427
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    # noinspection PyUnusedLocal
    ver_info: Union[str, List[str]] = []
    versions: List[str] = []
    versions.append('1.2.3')
    versions.append('1.2.4')
    versions.append('1.2.4a0')
    versions.append('1.2.4a1')
    versions.append('1.2.4b0')
    versions.append('1.2.4b1')
    versions.append('1.3.0')
    versions.append('2.0.0')

# Generated at 2022-06-13 20:46:47.108788
# Unit test for function bump_version
def test_bump_version():
    # Test bump_version(...)
    import unittest

    class TestBumpVersion(unittest.TestCase):
        def test_basic(self):
            # Test basic functionality
            self.assertEqual(bump_version('1.2.2'), '1.2.3')
            self.assertEqual(bump_version('1.2.3', position=1), '1.3')
            self.assertEqual(bump_version('1.3.4', position=0), '2.0')
            self.assertEqual(bump_version('1.2.3', prerelease='a'),
                             '1.2.4a0')

# Generated at 2022-06-13 20:46:59.438723
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    try:
        import unittest.mock as mock
    except ImportError:
        import mock

    class MockStrictVersion(NamedTuple):
        version: Tuple[int, int, int]
        prerelease: Tuple[str, int]


# Generated at 2022-06-13 20:47:22.870362
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    import unittest

    class TestBumpVersion(unittest.TestCase):
        """Unit test for function bump_version"""

        def test_bump_version(self):
            """Unit test for function bump_version"""
            self.assertEqual(bump_version('1.2.2'), '1.2.3')
            self.assertEqual(bump_version('1.2.3', position=1), '1.3')
            self.assertEqual(bump_version('1.3.4', position=0), '2.0')
            self.assertEqual(bump_version('1.2.3', prerelease='a'), '1.2.4a0')

# Generated at 2022-06-13 20:47:35.478747
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:47:47.695161
# Unit test for function bump_version
def test_bump_version():
    def test_version_part(
            version: str,
            position: int,
            text: str,
            number: int,
            pre_text: str,
            pre_number: int
    ) -> None:
        """
        Tests that the attributes of a version part match the given values.
        """
        ver_info = _build_version_info(version)
        try:
            ver_part = ver_info._asdict()[text]
        except KeyError:
            raise ValueError('Unable to find the %r part' % text)
        ver_part = cast(_VersionPart, ver_part)
        assert ver_part.pos == position
        assert ver_part.txt == text
        assert ver_part.num == number
        assert ver_part.pre_txt == pre_text

# Generated at 2022-06-13 20:47:58.425232
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    # pylint: disable=import-error
    from flutils.jsonutils import rformat


# Generated at 2022-06-13 20:48:10.334611
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

# Generated at 2022-06-13 20:48:21.735945
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

# Generated at 2022-06-13 20:48:33.780532
# Unit test for function bump_version
def test_bump_version():
    """Tests for :func:`flutils.packages.bump_version`."""
    from flutils.packages import bump_version

    #################################################
    # Test for valid version number changes
    #################################################

    # Test patch changes
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

    # Test pre-release alpha changes
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version

# Generated at 2022-06-13 20:48:46.512282
# Unit test for function bump_version
def test_bump_version():
    def _assert_raises_prerelease_major(vstring: str):
        with pytest.raises(ValueError) as ex:
            bump_version(vstring, pre_release='a')
        assert 'only the \'minor\' or \'patch\' parts' in str(ex.value)

    def _assert_raises_prerelease_alpha_to_beta(vstring: str):
        with pytest.raises(ValueError) as ex:
            bump_version(vstring, pre_release='beta')
        assert '\'pre_release\' can only be one of' in str(ex.value)

    def _assert_raises_prerelease_beta_to_alpha(vstring: str):
        with pytest.raises(ValueError) as ex:
            bump_version(vstring, pre_release='alpha')

# Generated at 2022-06-13 20:48:56.855622
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    ver_increase = {
        '1.2.3': '1.2.4',
        '1.2.3a2': '1.2.3a3',
        '1.2.3a0': '1.2.3a1',
        '1.2.3b7': '1.2.3b8',
        '1.2.3b0': '1.2.3b1',
        '1.2.3b1': '1.2.3',
        '1.2.3a1': '1.2.3',
    }

# Generated at 2022-06-13 20:49:04.421837
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    print(bump_version('1.2.2'))
    print(bump_version('1.2.3', position=1))
    print(bump_version('1.3.4', position=0))
    print(bump_version('1.2.3', prerelease='a'))
    print(bump_version('1.2.4a0', pre_release='a'))
    print(bump_version('1.2.4a1', pre_release='b'))
    print(bump_version('1.2.4a1'))
    print(bump_version('1.2.4b0'))
    print(bump_version('2.1.3', position=1, pre_release='a'))

# Generated at 2022-06-13 20:49:32.849825
# Unit test for function bump_version
def test_bump_version():
    from unittest import TestCase

    class Testing(TestCase):
        def test_bump_version(self):
            err = "flutils.packages: bump_version"
            out = bump_version('1.2.2')
            self.assertEqual(out, '1.2.3', '%s (1)' % err)

            out = bump_version('1.2.3', position=1)
            self.assertEqual(out, '1.3', '%s (2)' % err)

            out = bump_version('1.3.4', position=0)
            self.assertEqual(out, '2.0', '%s (3)' % err)

            out = bump_version('1.2.3', prerelease='a')

# Generated at 2022-06-13 20:49:42.513877
# Unit test for function bump_version
def test_bump_version():
    """Test the function "bump_version" with no options.

    The versions being tested:

    1.1.1
    1.1.2
    1.2.1
    1.2.2
    2.1.0
    2.1.1
    2.2.0
    3.0.0
    3.1.0
    3.2.0
    4.0.0
    4.1.0
    4.2.0
    5.0.0
    6.0.0

    """

# Generated at 2022-06-13 20:49:54.622820
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version
    from flutils.debugutils import dprint

    # Version bump

# Generated at 2022-06-13 20:50:08.907948
# Unit test for function bump_version
def test_bump_version():
    """Test 'bump_version' function."""
    for i in (
        '1.2.3',
        '1.3.4',
        '2.1.3',
        '1.2.4a0',
        '1.2.4a1',
        '1.2.4a0',
        '1.2.4b0',
        '1.2.4b0'
    ):
        assert bump_version(i) == bump_version(i)

# Generated at 2022-06-13 20:50:20.657840
# Unit test for function bump_version
def test_bump_version():
    """Tests for bump_version"""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:50:26.796283
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    print('Function bump_version')

    # Test simple version
    test = '1.2.3'
    out = bump_version(test)
    assert out == '1.2.4', out

    # Test minor version
    expected = '1.3'
    out = bump_version(test, position=1)
    assert out == expected, out

    # Test major version
    expected = '2.0'
    out = bump_version(test, position=0)
    assert out == expected, out

    # Test pre-release
    test = '1.2.3'
    expected = '1.2.4a0'
    out = bump_version(test, prerelease='a')
    assert out == expected, out

    # Test pre-release again

# Generated at 2022-06-13 20:50:33.403604
# Unit test for function bump_version
def test_bump_version():
    """Test ``bump_version`` function."""
    print('Testing function: bump_version()')


# Generated at 2022-06-13 20:50:34.604695
# Unit test for function bump_version
def test_bump_version():
    from doctest import testmod
    from flutils import packages
    testmod(packages, raise_on_error=True)



# Generated at 2022-06-13 20:50:48.098403
# Unit test for function bump_version
def test_bump_version():
    # As I want to do 2.1.3 I want to make patch number = 2, but that is
    # a 2 and not a 3, so for position I will use 2 - 3 or -1
    assert bump_version('2.1.3') == '2.1.4'
    assert bump_version('2.1.3', position=1) == '2.2'
    assert bump_version('2.1.3', position=0) == '3.0'
    assert bump_version('2.1.3', pre_release='a') == '2.1.4a0'
    assert bump_version('2.1.4a0', pre_release='a') == '2.1.4a1'

# Generated at 2022-06-13 20:51:01.782156
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:52:03.824406
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version
    """
    # Region - Test normal functions

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:52:18.204943
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    from flutils.packages import bump_version

# Generated at 2022-06-13 20:52:32.028278
# Unit test for function bump_version
def test_bump_version():
    print('testing bump_version()...')

    print('major')
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('2.2.3') == '2.2.4'
    assert bump_version('2.2.4') == '2.2.5'
    assert bump_version('100.2.3') == '100.2.4'

    print('minor')
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.0.3', position=1) == '1.1'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('2.2.3', position=1) == '2.3'

# Generated at 2022-06-13 20:52:45.825631
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version.
    """

# Generated at 2022-06-13 20:52:59.007824
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

# Generated at 2022-06-13 20:53:07.871266
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0914,W0212
    """Unit test for function bump_version."""
    #
    # Make sure pre-release bumps work in all positions
    #

    #
    # Major version
    #
    version = '1.0.0'
    position = 0
    pre_release = 'a'
    expected = '2.0.0'
    out = bump_version(version, position, pre_release)
    assert out == expected, (
        'Invalid major version bump.  Expected (%r) got (%r).' % (
            expected,
            out
        )
    )

    #
    # Minor version
    #
    version = '1.0.0'
    position = 1
    pre_release = 'b'
    expected = '1.1b0'
   
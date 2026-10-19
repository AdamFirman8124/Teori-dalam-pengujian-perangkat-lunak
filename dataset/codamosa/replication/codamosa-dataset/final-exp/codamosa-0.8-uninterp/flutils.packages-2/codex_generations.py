

# Generated at 2022-06-13 20:43:33.370044
# Unit test for function bump_version
def test_bump_version():
    """Test functionality of bump_version."""
    this_ver = bump_version('0.0.1')
    assert this_ver == '0.0.2'
    this_ver = bump_version('0.1.2')
    assert this_ver == '0.1.3'
    this_ver = bump_version('1.2.3')
    assert this_ver == '1.2.4'
    this_ver = bump_version('1.2.4a0')
    assert this_ver == '1.2.4a1'
    this_ver = bump_version('1.2.4a1')
    assert this_ver == '1.2.4a2'
    this_ver = bump_version('1.2.4a2')

# Generated at 2022-06-13 20:43:44.349408
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.packages import bump_version as bumpv

    def _verify(
            version: str,
            pos: int = 2,
            pre_release: Union[str, None] = None,
            expected: str = '',
    ) -> None:
        if not expected:
            expected = version
        result = bumpv(version, pos, pre_release)
        assert result == expected

    _verify('1.2')
    _verify('1.2.3', expected='1.2')
    _verify('1.2.3', pos=2, expected='1.2.4')
    _verify('1.2.3', pos=1, expected='1.3')

# Generated at 2022-06-13 20:43:55.719423
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    # pylint: disable=R0201,R0914,C0200
    # noinspection PyUnusedLocal
    from flutils.packages import bump_version
    from distutils.version import StrictVersion

    # A version number string can not be a PEP440 version
    try:
        bump_version('A')
    except ValueError:
        pass
    else:
        raise AssertionError('A version number string can not be a PEP440 '
                             'version.')

    # A version number string can not be a PEP440 version
    try:
        bump_version('1.2.3a.4')
    except ValueError:
        pass

# Generated at 2022-06-13 20:44:05.365745
# Unit test for function bump_version
def test_bump_version():
    """Testing function bump_version."""
    # pylint: disable=duplicate-code
    version = '1.2.2'
    position = 2
    pre_release = None
    expect = '1.2.3'
    out = bump_version(version, position, pre_release)
    assert out == expect
    version = '1.2.3'
    position = 1
    pre_release = None
    expect = '1.3'
    out = bump_version(version, position, pre_release)
    assert out == expect
    version = '1.3.4'
    position = 0
    pre_release = None
    expect = '2.0'
    out = bump_version(version, position, pre_release)
    assert out == expect
    version = '1.2.3'


# Generated at 2022-06-13 20:44:15.311831
# Unit test for function bump_version
def test_bump_version():
    """
    Unit testing for ``bump_version``.
    """
    import unittest
    try:
        # noinspection PyPackageRequirements
        import unittest.mock as mock
    except ImportError:
        import mock

    @mock.patch('flutils.packages.bump_version.bump_version')
    def _test_bump_version(mock_bump_version):
        mock_bump_version.return_value = '1.2.3'
        ver_bump = bump_version('1.0.0', position=2)
        assert ver_bump == '1.2.3'
        mock_bump_version.assert_called_once_with('1.0.0', position=2)


# Generated at 2022-06-13 20:44:20.804447
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='a') == '1.2.4a2'
    assert bump_version('2.1.3', position=1, pre_release='a') == '2.2a0'

# Generated at 2022-06-13 20:44:33.041136
# Unit test for function bump_version
def test_bump_version():
    assert '1.2.3' == bump_version('1.2.2')
    assert '1.3' == bump_version('1.2.3', position=1)
    assert '2.0' == bump_version('1.3.4', position=0)

    assert '1.2.4a0' == bump_version('1.2.3', pre_release='a')
    assert '1.2.4a1' == bump_version('1.2.4a0', pre_release='a')
    assert '1.2.4b0' == bump_version('1.2.4a1', pre_release='b')

    assert '1.2.4' == bump_version('1.2.4a1')

# Generated at 2022-06-13 20:44:45.399669
# Unit test for function bump_version

# Generated at 2022-06-13 20:44:54.240858
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    # minor
    assert bump_version('1.2.3') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_

# Generated at 2022-06-13 20:45:04.875737
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    # Major version
    assert bump_version('2.0.0') == '3.0.0'
    assert bump_version('2.0.1') == '3.0.0'
    assert bump_version('2.1.1') == '3.0.0'
    assert bump_version('3.1.1') == '4.0.0'
    # Minor version
    assert bump_version('2.0.0', 1) == '2.1'
    assert bump_version('2.0.0', 1, 'alpha') == '2.1a0'
    assert bump_version('2.0.0', 1, 'beta') == '2.1b0'
    assert bump_version('2.0.1', 1) == '2.1'


# Generated at 2022-06-13 20:45:33.503936
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:45:46.280471
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

# Generated at 2022-06-13 20:45:56.942226
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function :func:`bump_version`"""
    ########################################
    # Test for simple bumping numbers
    ########################################
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

    ########################################
    # Test for pre-release versions
    ########################################
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

# Generated at 2022-06-13 20:46:08.601889
# Unit test for function bump_version
def test_bump_version():
    """Test the `bump_version` function.

    *New in version 0.3*

    """
    from flutils.packages import bump_version

    # This test function is tested in the module doctest
    assert bump_version("1.2.3") == "1.2.4"
    assert bump_version("1.2.3", position=1) == "1.3"
    assert bump_version("1.3.4", position=0) == "2.0"
    assert bump_version("1.2.3", pre_release='a') == "1.2.4a0"
    assert bump_version("1.2.4a0", pre_release='a') == "1.2.4a1"

# Generated at 2022-06-13 20:46:21.304442
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=C0103
    result = bump_version('1.2.2')
    assert result == '1.2.3'
    result = bump_version('1.2.3', position=1)
    assert result == '1.3'
    result = bump_version('1.3.4', position=0)
    assert result == '2.0'
    result = bump_version('1.2.3', prerelease='a')
    assert result == '1.2.4a0'
    result = bump_version('1.2.4a0', pre_release='a')
    assert result == '1.2.4a1'
    result = bump_version('1.2.4a1', pre_release='b')
    assert result == '1.2.4b0'


# Generated at 2022-06-13 20:46:32.998088
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    def _test_bump_version(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ) -> str:
        """shortcut function to bump a version string."""
        return bump_version(version, position, pre_release)

    # Test correct pre_release handling
    assert _test_bump_version('1.2.3', position=2, pre_release='a') == '1.2.4a0'
    assert _test_bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert _test_bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'


# Generated at 2022-06-13 20:46:46.621875
# Unit test for function bump_version

# Generated at 2022-06-13 20:46:59.317194
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:47:11.744337
# Unit test for function bump_version

# Generated at 2022-06-13 20:47:22.426849
# Unit test for function bump_version
def test_bump_version():
    version_num = '3.0.0'

    new_version_num = bump_version(version_num)
    assert new_version_num == '3.0.1'

    new_version_num = bump_version(version_num, position=1)
    assert new_version_num == '3.1'

    new_version_num = bump_version(version_num, position=0)
    assert new_version_num == '4.0'

    new_version_num = bump_version(version_num, pre_release='a')
    assert new_version_num == '3.0.0a0'

    new_version_num = bump_version(new_version_num, pre_release='a')
    assert new_version_num == '3.0.0a1'

    new_version

# Generated at 2022-06-13 20:47:50.689042
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

# Generated at 2022-06-13 20:47:59.972655
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function ``bump_version``."""
    for version in ('1.2.3', '0.1.0', '0.0.1', '2.5.5', '1.2.3'):
        assert bump_version(version) == '%s.4' % version.rsplit('.', 1)[0]

    for version in ('1.2.3', '0.1.0', '0.0.1', '2.5.5', '1.2.3'):
        assert bump_version(version, position=1) == '%s.0' % increment_part(
            version.split('.', 2)[1], 1, 'prezero'
        )


# Generated at 2022-06-13 20:48:10.667894
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=C0103
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:21.937248
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:26.695356
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    """Run a unit test for the function: _build_version_info."""
    def _run_test(
            test_number: int,
            cur_ver: str,
            position: int,
            pre_release: Optional[str],
            bumped_ver: str
    ) -> None:
        print(
            '\nTest (%s): "bump_version (%s, %s, %s)"'
            % (test_number, cur_ver, position, pre_release)
        )
        print('    %r should be: %r' % (version, bumped_ver))
        
        version = bump_version(
            version=cur_ver,
            position=position,
            pre_release=pre_release
        )
        

# Generated at 2022-06-13 20:48:29.728893
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for function bump_version

    .. versionadded:: 0.3.0
    """
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:48:37.067946
# Unit test for function bump_version
def test_bump_version():

    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.2.2', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:48:39.855811
# Unit test for function bump_version
def test_bump_version():
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:48:48.986545
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for function bump_version."""
    import pytest
    

# Generated at 2022-06-13 20:48:58.180234
# Unit test for function bump_version
def test_bump_version():
    import sys
    import unittest

    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    if sys.version_info[:2] >= (3, 4):
        # noinspection PyUnresolvedReferences
        import importlib.machinery
        # noinspection PyUnresolvedReferences
        import importlib.util
        # noinspection PyUnresolvedReferences
        from pathlib import Path
    else:
        from importlib2 import machinery as importlib_machinery
        from importlib2 import util as importlib_util

    from flutils.packages import bump_version


# Generated at 2022-06-13 20:49:14.824635
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version.

    Returns:
        None

    """
    # pylint: enable=C0103

# Generated at 2022-06-13 20:49:27.918165
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    # pylint: disable=W0612
    import unittest
    import os

    os.chdir(os.path.dirname(__file__))

    class Test(unittest.TestCase):
        def test_001(self):
            """TestCase for function bump_version"""
            self.assertEqual(
                bump_version('1.2.2'),
                '1.2.3'
            )
        def test_002(self):
            """TestCase for function bump_version"""
            self.assertEqual(
                bump_version('1.2.3', position=1),
                '1.3'
            )
        def test_003(self):
            """TestCase for function bump_version"""

# Generated at 2022-06-13 20:49:33.713242
# Unit test for function bump_version
def test_bump_version():
    """Test function: bump_version
    * Notes:
        - The tests are defined in the docstring of the function: bump_version
    """

    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-13 20:49:49.446679
# Unit test for function bump_version
def test_bump_version():
    """
    Test the function bump_version.

    :return: None

    """
    from flutils.packages import bump_version

# Generated at 2022-06-13 20:50:04.053562
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version()."""
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:50:17.357477
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version in the package packages."""
    # pylint: disable=E1120,W0611
    from flutils.packages import bump_version, _build_version_info
    from distutils.version import StrictVersion
    try:
        bump_version('1.2.3')
    except ImportError:
        pass
    except ValueError:
        assert True is False
    ver_info = _build_version_info('1.2.3')
    assert isinstance(ver_info.version, str)
    assert isinstance(ver_info.major, _VersionPart)
    assert ver_info.major.pos == 0
    assert ver_info.major.num == 1
    assert ver_info.major.txt == '1'
    assert ver_info.major.name == 'major'
   

# Generated at 2022-06-13 20:50:27.805898
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    # pylint: disable=C0103
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:50:38.135354
# Unit test for function bump_version
def test_bump_version():
    """Tests the :func:`bump_version` function."""

# Generated at 2022-06-13 20:50:49.772235
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version."""


# Generated at 2022-06-13 20:50:53.708120
# Unit test for function bump_version
def test_bump_version():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:51:17.109094
# Unit test for function bump_version
def test_bump_version():
    import textwrap
    import unittest

    fn = bump_version

    class TestCase(unittest.TestCase):
        def test_1(self):
            """Basic usage."""
            self.assertEqual(fn('1.2.2'), '1.2.3')
            self.assertEqual(fn('1.2.3', position=1), '1.3')
            self.assertEqual(fn('1.3.4', position=0), '2.0')

        def test_2(self):
            """Basic usage with pre-release."""
            self.assertEqual(fn('1.2.3', prerelease='a'), '1.2.4a0')

# Generated at 2022-06-13 20:51:28.317963
# Unit test for function bump_version
def test_bump_version():
    # Test various 'bump_version' method scenarios
    import unittest

    class Test_BUMP_VERSION(unittest.TestCase):

        maxDiff = None

        def setUp(self):
            self.version = '1.2.3'
            self.bump_version = bump_version
            self.version_info = _build_version_info(self.version)


# Generated at 2022-06-13 20:51:36.300502
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    from sys import stdout
    from flutils.packages import bump_version
    from flutils.testing import UnitTester


# Generated at 2022-06-13 20:51:43.360983
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.packages import bump_version
    from flutils.textutils import get_funcname

    def _test(version: str, pos: int, pre: str, expected: str):
        funcname = get_funcname()
        new_ver = bump_version(version, pos, pre)
        if new_ver != expected:
            print('%s: (%r, %r, %r) - Expected: %r, Actual: %r' % (
                funcname, version, pos, pre, expected, new_ver))

    _test('1.2.2', 2, '', '1.2.3')
    _test('1.2.3', 1, '', '1.3')

# Generated at 2022-06-13 20:51:54.742868
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from pprint import pprint  # pylint: disable=C0412
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:51:59.755778
# Unit test for function bump_version
def test_bump_version():
    from flutils.utils import run_doctest
    results = run_doctest(bump_version, globals())
    for result in results:
        assert result.outcome is True


# Make the module executable.

if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:52:14.857550
# Unit test for function bump_version

# Generated at 2022-06-13 20:52:22.272143
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function ``bump_version``."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_

# Generated at 2022-06-13 20:52:33.779175
# Unit test for function bump_version
def test_bump_version():
    def _test(
            version: str,
            position: int,
            pre_release: Optional[str],
            res: str
    ) -> None:
        out = bump_version(version, position, pre_release)
        assert out == res, (out, res)


# Generated at 2022-06-13 20:52:46.336553
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=E1101
    # Get version number
    ver = StrictVersion(__VERSION__).version
    ver_info = _build_version_info(__VERSION__)
    # Major
    bumped_ver = bump_version(__VERSION__, position=0)
    bumped_ver_info = _build_version_info(bumped_ver)
    assert bumped_ver_info.major.num == ver_info.major.num + 1
    bumped_ver = bump_version(__VERSION__, position=-3)
    bumped_ver_info = _build_version_info(bumped_ver)
    assert bumped_ver_info.major.num == ver_info.major.num + 1
    bumped_ver = bump_version(__VERSION__, position=-3, pre_release='alpha')
    bumped_
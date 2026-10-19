

# Generated at 2022-06-13 20:43:32.102508
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:43:43.150124
# Unit test for function bump_version
def test_bump_version():
    print(">>> test_bump_version")
    def check_version(
            version: str,
            target: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ) -> None:
        print("\t>>> check_version(version='%s', target='%s')" % (version, target))
        out = bump_version(version, position, pre_release)
        print("\t\t>>> out == target: %s" % (out == target))
        assert out == target

    check_version('1.2.2', '1.2.3')
    check_version('1.2.3', '1.2.4', position=1)
    check_version('1.3.4', '1.3.5', position=0)

# Generated at 2022-06-13 20:43:54.649405
# Unit test for function bump_version

# Generated at 2022-06-13 20:44:01.282646
# Unit test for function bump_version

# Generated at 2022-06-13 20:44:13.230246
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

# Generated at 2022-06-13 20:44:24.446614
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version() function.

    *New in version 0.3*

    """
    def _test_bump(ver_pos, ver_prerel, out_pos, out_act, out_expect):
        """Test a bump_version() call.

        :param ver_pos:
        :type ver_pos:
        :param ver_prerel:
        :type ver_prerel:
        :param out_pos:
        :type out_pos:
        :param out_act:
        :type out_act:
        :param out_expect:
        :type out_expect:
        :return:
        :rtype:

        """
        ver_pos = cast(int, ver_pos)
        out_pos = cast(int, out_pos)

# Generated at 2022-06-13 20:44:35.095835
# Unit test for function bump_version
def test_bump_version():
    """Test function ``bump_version``."""

    from types import MethodType  # pylint: disable=E0611,E0401
    from flutils.testing import (
        BasicTestCase,
        run_tests
    )

    # noinspection PyPep8Naming
    class TestVersion(BasicTestCase):
        # noinspection PyMissingOrEmptyDocstring,PyPropertyDefinition
        @property
        def bump_version(self) -> MethodType:
            return cast(MethodType, bump_version)

        # noinspection PyMissingOrEmptyDocstring
        def test_bump_version(self):
            self.assertEqual(
                self.bump_version('1.2.2'), '1.2.3'
            )

# Generated at 2022-06-13 20:44:46.411539
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for function flutils.packages.bump_version.
    """
    args: List[Tuple[str, int, Optional[str]]] = [
        ('1.2.2', 2, None),
        ('1.2.3', 1, None),
        ('1.3.4', 0, None),
        ('1.2.3', 2, 'a'),
        ('1.2.4a0', 2, 'a'),
        ('1.2.4a1', 2, 'b'),
        ('1.2.4b0', 2, None),
        ('1.2.4a1', 2, None),
        ('1.2.4b0', 2, None),
        ('2.1.3', 1, 'a'),
        ('1.2b0', 2, None),
    ]

# Generated at 2022-06-13 20:44:53.494332
# Unit test for function bump_version
def test_bump_version():
    """ Test function as main """
    # Test bumping major
    assert bump_version('1.1.1', position=0) == '2'
    assert bump_version('1.1.1', position=-3) == '2'
    # Test bumping minor
    assert bump_version('1.1.1', position=1) == '1.2'
    assert bump_version('1.1.1', position=-2) == '1.2'
    assert bump_version('1.1.1') == '1.1.2'
    assert bump_version('1.1.1', position=-1) == '1.1.2'
    # Test bumping patch
    assert bump_version('2.2.2', position=2) == '2.2.3'

# Generated at 2022-06-13 20:45:04.511556
# Unit test for function bump_version

# Generated at 2022-06-13 20:45:32.024908
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=W0212
    version = '1.2.2'
    bumped = bump_version(version)
    expected = '1.2.3'
    assert bumped == expected
    version = '1.2.3'
    position = 1
    bumped = bump_version(version, position)
    expected = '1.3'
    assert bumped == expected
    version = '1.3.4'
    position = 0
    bumped = bump_version(version, position)
    expected = '2.0'
    assert bumped == expected
    version = '1.2.3'
    pre_release = 'a'
    bumped = bump_version(version, pre_release=pre_release)
    expected = '1.2.4a0'
    assert bumped == expected

# Generated at 2022-06-13 20:45:44.694043
# Unit test for function bump_version
def test_bump_version():

    # New in version 0.3

    # Parameter validation
    version = '1.2.3'
    assert bump_version(version) == '1.2.4'
    position = 1
    assert bump_version(version, position=position) == '1.3'
    position = 0
    assert bump_version(version, position=position) == '2.0'
    pre_release = 'a'
    assert bump_version(version, pre_release=pre_release) == '1.2.4a0'
    assert bump_version(
        version,
        pre_release=pre_release
    ) == bump_version(
        bump_version(version, pre_release=pre_release),
        pre_release=pre_release
    ) == '1.2.4a1'

# Generated at 2022-06-13 20:45:53.050110
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=W0613,W0612
    from os import getcwd
    from os.path import dirname, realpath
    from time import time
    from unittest import TestCase
    from unittest.mock import patch

    from flutils.packages import bump_version

    test_dir = dirname(realpath(__file__))
    test_time = time()
    test_version = '10.11.12'

    class TestBumpVersion(TestCase):  # pylint: disable=R0904

        @patch('os.getcwd')
        def test_build_version_bump_position(
                self,
                getcwd_mock
        ) -> None:
            getcwd_mock.return_value = getcwd()


# Generated at 2022-06-13 20:46:05.689613
# Unit test for function bump_version
def test_bump_version():
    """Tests for function bump_version

    *New in version 0.3*
    """
    from flutils.packages import bump_version

    def _run_test(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ) -> Tuple[str, str]:
        if pre_release is None:
            pre_release = ''
        else:
            pre_release = cast(str, pre_release)
            pre_release = pre_release.strip().lower()

        if pre_release == '':
            pre_release_str = ''
        else:
            pre_release_str = ' , pre_release={},'.format(repr(pre_release))


# Generated at 2022-06-13 20:46:19.145973
# Unit test for function bump_version
def test_bump_version():
    """Coverage for function bump_version."""
    # noinspection PyUnusedLocal
    def _setup(version: str) -> None:
        """Coverage setup."""
        bump_version(version)

    # noinspection PyUnusedLocal
    def _test(
            version: str,
            pos: int = 2,
            pre: Optional[str] = None
    ) -> None:
        """Coverage test."""
        bump_version(version, pos, pre)

    for ver in ('1.0', '1.0.0', '1.0.0a0', '1.0.0b0', '1.0.0a1', '1.0.0b1'):
        _setup(ver)


# Generated at 2022-06-13 20:46:32.388357
# Unit test for function bump_version
def test_bump_version():
    """Unit test for ``bump_version``."""
    from tests.helper import assert_equal
    assert_equal(bump_version('0.0.1'), '0.0.2')
    assert_equal(bump_version('0.0.0'), '0.0.1')
    assert_equal(bump_version('1.2.3'), '1.2.4')
    assert_equal(bump_version('1.2.3', position=1), '1.3')
    assert_equal(bump_version('1.3.4', position=0), '2.0')
    assert_equal(bump_version('1.2.3', pre_release='a'), '1.2.4a0')

# Generated at 2022-06-13 20:46:46.261053
# Unit test for function bump_version
def test_bump_version():
    ''' Test that bump_version returns the correct value
    '''

    # Test that bump_version returns the correct value

    # This is a list of tuples
    #   [version, position, pre_release, expected_return]

# Generated at 2022-06-13 20:46:58.789543
# Unit test for function bump_version
def test_bump_version():
    """Pytest test case for function bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version

# Generated at 2022-06-13 20:47:11.438105
# Unit test for function bump_version
def test_bump_version():
    """ Unit test for function bump_version """
    # pylint: disable=missing-function-docstring
    from sys import version_info
    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

    assert bump_version('1.2.4a0', position=-1) == '1.2.4'
    assert bump_version('1.2.4a1', position=-1) == '1.2.4'
    assert bump_version('1.2.4b0', position=-1) == '1.2.4'


# Generated at 2022-06-13 20:47:18.631319
# Unit test for function bump_version

# Generated at 2022-06-13 20:47:42.951426
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version."""
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:47:56.409362
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:09.475078
# Unit test for function bump_version
def test_bump_version():
    from flutils.regex import rx_version
    from flutils.packages import is_version

    import copy
    import random

    def _build_rand_ver(
            isalpha: bool,
            isbeta: bool
    ) -> Tuple[str, StrictVersion, str, str]:
        major = random.randrange(0, 1000)
        minor = random.randrange(0, 1000)
        patch = random.randrange(0, 1000)

        if isalpha is True:
            pre = 'a'
        elif isbeta is True:
            pre = 'b'
        else:
            pre = ''

        if pre == '':
            pre_num = -1
        else:
            pre_num = random.randrange(0, 1000)


# Generated at 2022-06-13 20:48:21.416936
# Unit test for function bump_version
def test_bump_version():
    """Unit test the bump_version function."""

    def _basic_bump_test(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None,
            expected: str = ''
    ) -> None:
        out = bump_version(
            version=version,
            position=position,
            pre_release=pre_release
        )
        if expected != out:
            raise ValueError(
                "Expected %r from version %r, position %r, and pre_release %r, "
                "got %r." % (
                    expected,
                    version,
                    position,
                    pre_release,
                    out
                )
            )

    _basic_bump_test('0.0.0', position=0, expected='1.0')
    _basic_b

# Generated at 2022-06-13 20:48:33.795190
# Unit test for function bump_version

# Generated at 2022-06-13 20:48:46.512068
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.0.0') == '1.0.1'
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:48:56.089022
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for bump_version().

    """
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:03.962489
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version from flutils.packages."""
    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.2', position=1) == '1.3'

    # Test pre-release bumps
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:49:15.812094
# Unit test for function bump_version
def test_bump_version():
    """Test function ``bump_version``."""
    from copy import copy
    from pprint import pprint
    from textwrap import dedent

    from flutils.packages import bump_version

    def test_bump(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None,
    ) -> None:
        print('Input:')
        pprint(locals())
        out = bump_version(version, position, pre_release)
        print('\nOutput:')
        pprint(out)
        print()

    print(f'Testing function: {bump_version.__name__}\n')

    print(dedent("""\
        Test: No pre-release info:
        Expected: No change.
    """))

# Generated at 2022-06-13 20:49:28.523705
# Unit test for function bump_version
def test_bump_version():
    """ Unit test for function bump_version """
    from flutils.packages import bump_version
    from flutils.testing import AssertsMixin


# Generated at 2022-06-13 20:49:54.480745
# Unit test for function bump_version
def test_bump_version():
    '''
    Unit test for function bump_version.
    '''
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
   

# Generated at 2022-06-13 20:50:08.871730
# Unit test for function bump_version
def test_bump_version():
    """Test the function ``bump_version`` in the module ``packages``.

    *New in version 0.3*

    """
    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

# Generated at 2022-06-13 20:50:20.622110
# Unit test for function bump_version

# Generated at 2022-06-13 20:50:26.742359
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=unused-variable,invalid-name
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
   

# Generated at 2022-06-13 20:50:33.399334
# Unit test for function bump_version
def test_bump_version():
    """Unit test for ``bump_version``."""
    from flutils.packages import bump_version
    msg = '%s version: %s'

# Generated at 2022-06-13 20:50:40.588458
# Unit test for function bump_version
def test_bump_version():
    versions = [
        '1.2.2',
        '1.2.3',
        '1.2.3',
        '1.3',
        '1.3.4',
        '2.0',
        '1.2.3',
        '1.2.4a0',
        '1.2.4a1',
        '1.2.4b0',
        '1.2.4a1',
        '1.2.4',
        '1.2.4b0',
        '1.2.4',
        '2.1.3',
        '2.2a0',
        '1.2b0',
        '1.2.1',
    ]
    for ver, new_ver in zip(versions, versions[1:]):
        assert bump_version

# Generated at 2022-06-13 20:50:45.163427
# Unit test for function bump_version
def test_bump_version():
    """ Test the bump_version function """
    from flutils.packages import bump_version
    from flutils.packages import get_package_version

    old_ver = get_package_version()

    new_ver = bump_version(old_ver)

    assert new_ver != old_ver

# Generated at 2022-06-13 20:50:53.160701
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:51:05.545583
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version as bv
    def l(*args):
        last = len(args) - 1
        for i, v in enumerate(args):
            if i == last:
                break
            print(str(v))
        print('Return: {}'.format(str(args[last])))

    # These tests should work
    l('1.2.2', bv('1.2.2'))
    l('1.2.3', bv('1.2.2'))
    l('1.2.3', bv('1.2.2', position=2))
    l('1.3', bv('1.2.2', position=1))
    l('2.0', bv('1.2.2', position=0))

# Generated at 2022-06-13 20:51:13.303744
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0914
    from pprint import pprint
    from flutils.packages import bump_version
    bump_version('1.2.2')
    bump_version('1.2.2', position=2)
    bump_version('1.2.2', position=0)
    bump_version('1.2.2', position=1)
    bump_version('1.2.2', position=2)
    bump_version('1.2.2a1')
    bump_version('1.2.2a1', position=0)
    bump_version('1.2.2a1', position=1)
    bump_version('1.2.2a1', position=2)
    bump_version('1.2.2a1', position=2, pre_release='a')
   

# Generated at 2022-06-13 20:51:39.899864
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version
    """
    # pylint: disable=missing-docstring

    # noinspection PyUnresolvedReferences
    from flutils.packages import bump_version

    # Version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3') == '1.2.4'

    # Position
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.2.3', position=1) == '1.3'

    # Pre-release
    assert bump_version('1.2.3', pre_release='alpha') == '1.2.4a0'

# Generated at 2022-06-13 20:51:53.601609
# Unit test for function bump_version
def test_bump_version():
    from .utils import is_version

    def _test_bump_version(**kwargs):
        ver = bump_version(**kwargs)
        assert is_version(ver) is True
        if kwargs['position'] == 0:
            assert ver.startswith('%s.' % (kwargs['version'][:1] + 1))
        elif kwargs['position'] == 1:
            assert ver.startswith('%s.' % kwargs['version'][:3])
        else:
            assert ver.startswith('%s.' % kwargs['version'][:5])
        return ver, kwargs

    # Version with alpha
    ver, kwargs = _test_bump_version(version='0.2.3a1', pre_release='a')

# Generated at 2022-06-13 20:52:03.929163
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', prerelease='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', prerelease='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:52:18.271725
# Unit test for function bump_version
def test_bump_version():
    """Test the function 'bump_version'."""
    from sys import version_info
    from unittest import TestCase

    from flutils.packages import bump_version  # pylint: disable=import-error,no-name-in-module

    if version_info[0] == 2:
        from mock import patch
        from testfixtures import compare, ShouldRaise
    else:
        from unittest.mock import patch
        from testfixtures.compat import compare, ShouldRaise

    class UnitTest(TestCase):
        """Test the 'bump_version' function."""

        def setUp(self):
            self.addCleanup(patch.stopall)


# Generated at 2022-06-13 20:52:32.069328
# Unit test for function bump_version
def test_bump_version():

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.2.dev0', position=2) == '1.2.3'
    assert bump_version('1.2.2.dev0', position=2, pre_release='a') == '1.2.3a0'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', position=-2) == '1.2.4'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

# Generated at 2022-06-13 20:52:45.825982
# Unit test for function bump_version
def test_bump_version():
    from collections import OrderedDict
    from textwrap import dedent

    tests = OrderedDict()

# Generated at 2022-06-13 20:52:59.006683
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version.

    :rtype:
        :obj:`bool`

    """
    def test(version):
        """Test the :func:`~flutils.packages.bump_version` function.

        This is a wrapper for basic error handling.  If a problem is
        encountered then set the ``err`` attribute to ``True``.

        :param version: The version number to test.
        :type version:
            `str`
        :returns:
            The version number returned from :func:`~flutils.packages.bump_version`.
        :rtype:
            `str`

        """
        # pylint: disable=W0603
        global err
        try:
            return bump_version(version)
        except ValueError:
            err = True

    err = False
    assert test

# Generated at 2022-06-13 20:53:07.323722
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version

    def test1():
        assert bump_version('1.2.2') == '1.2.3'
        assert bump_version('1.2.2', position=2) == '1.2.3'
        assert bump_version('1.2.2', position=-1) == '1.2.3'

    def test2():
        assert bump_version('1.2.2', position=1) == '1.3'
        assert bump_version('1.2.2', position=1, pre_release='a') == '1.3a0'
        assert bump_version('1.2.2', position=1, pre_release='b') == '1.3b0'

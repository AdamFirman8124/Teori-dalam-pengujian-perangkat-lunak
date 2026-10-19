

# Generated at 2022-06-13 20:43:29.187600
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:43:41.220470
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version in module packages

    :rtype:
        :obj:`int`

        * The number of failed unit tests.

    """
    import random
    import string
    import unittest

    class TestBumpVersion(unittest.TestCase):
        """Unit tests for bump_version."""

        def test_valid_versions(self):
            """Test all valid values for bump_version."""
            for pos in range(0, 3):
                for minor_alpha in range(0, 2):
                    for minor_beta in range(0, 2):
                        for patch_alpha in range(0, 2):
                            for patch_beta in range(0, 2):
                                f1 = '1.0.0'
                                f2 = '{}.0.0'.format(minor_alpha)


# Generated at 2022-06-13 20:43:52.957372
# Unit test for function bump_version
def test_bump_version():
    ver = '1.2.3'
    assert bump_version(ver) == '1.2.4'
    ver = '1.2.3'
    assert bump_version(ver, position=1) == '1.3'
    ver = '1.3.4'
    assert bump_version(ver, position=0) == '2.0'
    ver = '1.2.3'
    assert bump_version(ver, pre_release='a') == '1.2.4a0'
    ver = '1.2.4a0'
    assert bump_version(ver, pre_release='a') == '1.2.4a1'
    ver = '1.2.4a1'
    assert bump_version(ver, pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:44:00.308912
# Unit test for function bump_version
def test_bump_version():
    """
    Test for the :func:`~flutils.packages.bump_version` function.
    """
    # pylint: disable=R0914
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
   

# Generated at 2022-06-13 20:44:12.728076
# Unit test for function bump_version
def test_bump_version():
    """Run the tests for function bump_version."""
    import unittest
    from flutils.packages import bump_version

    class TestBumpVersion(unittest.TestCase):
        def test_bump_version_01(self) -> None:
            """Test bump_version."""
            self.assertEqual(
                bump_version('1.2.3'),
                '1.2.4'
            )
        def test_bump_version_02(self) -> None:
            """Test bump_version."""
            self.assertEqual(
                bump_version('1.2.3', position=1),
                '1.3'
            )
        def test_bump_version_03(self) -> None:
            """Test bump_version."""

# Generated at 2022-06-13 20:44:24.408915
# Unit test for function bump_version
def test_bump_version():
    """Test bump_version

    *New in version 0.3*

    This test is designed to stress test various aspects of
    ``helpers.bump_version
    """

# Generated at 2022-06-13 20:44:35.058536
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version."""
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:44:46.373171
# Unit test for function bump_version
def test_bump_version():
    """Test the :func:`bump_version()` function."""
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.3.0') == '1.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

# Generated at 2022-06-13 20:44:54.522333
# Unit test for function bump_version
def test_bump_version():
    """ Unit test for :py:func:`flutils.packages.bump_version` """
    from flutils.packages import bump_version

    # Basic test
    ver = bump_version('1.2.3')
    assert ver == '1.2.4'

    # Test of positions argument
    ver = bump_version('1.2.3', position=1)
    assert ver == '1.3'

    ver = bump_version('1.2.3', position=2)
    assert ver == '1.2.4'

    ver = bump_version('1.2.3', position=-1)
    assert ver == '1.2.4'

    ver = bump_version('1.2.3', position=-2)
    assert ver == '1.3'


# Generated at 2022-06-13 20:45:04.993474
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=too-many-branches,too-many-statements
    from flutils.packages import bump_version
    import itertools

    kwargs = dict(position=2, pre_release=None)
    hold: List[Tuple[str, str]] = [
        ('1.2.3', '1.2.4'),
        ('1.2.3a0', '1.2.4'),
        ('1.2.3.4', '1.2.4.5'),
        ('11.2.2', '11.2.3'),
        ('1.2.3.4.5.6', '1.2.3.4.5.7'),
    ]
    for ver, out in hold:
        assert bump_version(ver, **kwargs) == out

    k

# Generated at 2022-06-13 20:45:32.490286
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for function bump_version
    """
    from flutils.testhelpers import unit_test_introspection
    from flutils.packages import bump_version
    unit_test_introspection(
        name='bump_version',
        modname='flutils.packages',
        func=bump_version,
        callargs={'position': '2', 'version': '0.2.1'}
    )
    unit_test_introspection(
        name='bump_version',
        modname='flutils.packages',
        func=bump_version,
        callargs={'position': '1', 'version': '0.2.1'}
    )

# Generated at 2022-06-13 20:45:41.125054
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1') == '2'
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version

# Generated at 2022-06-13 20:45:51.926775
# Unit test for function bump_version
def test_bump_version():
    """ Perform unit tests on function bump_version. """
    from os import chdir
    from os.path import abspath, dirname
    from sys import path
    from unittest import (TestCase, main)

    path.insert(0, abspath(dirname(__file__)))

    from test_helpers import (
        assert_none,
        assert_raises,
        assert_str_equal,
        return_arg
    )

    chdir(abspath(dirname(__file__)))

    class TestBumpVersion(TestCase):
        """ Unit tests for function bump_version. """

        def test_bump_version(self) -> None:
            """ Test bump_version with various input arguments. """

# Generated at 2022-06-13 20:46:04.698848
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from sys import version_info as sysv
    from os import path as osp
    from flutils.test import TestCase
    from flutils.test import TestCaseResponse
    from flutils.test import TestCaseResponseNested
    from flutils.test import TestCaseResponseSimple


# Generated at 2022-06-13 20:46:13.250394
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for function bump_version."""
    from inspect import cleandoc
    from textwrap import dedent
    from unittest.mock import patch, mock_open

    from flutils.packages import bump_version

    from testing import normalize_docstring

    from . import CommonTestCase


# Generated at 2022-06-13 20:46:23.266418
# Unit test for function bump_version
def test_bump_version():
    """Unit test for method: bump_version"""
    import unittest.mock
    from flutils.packages import bump_version

    def _test_args(
            version: str,
            position: int,
            pre_release: Optional[str]
    ) -> None:
        """ """
        if position == 0:
            return_value = '{}'.format(int(version.split('.')[0]) + 1)
        elif position <= 1:
            return_value = '.'.join(
                [
                    version.split('.')[0],
                    str(int(version.split('.')[1]) + 1)
                ]
            )

# Generated at 2022-06-13 20:46:33.594674
# Unit test for function bump_version
def test_bump_version():
    """Test ``bump_version`` function."""
    func = bump_version

    def run_tests(tests: List[Tuple[str, str]],
                  position: int = 2,
                  pre_release: Optional[str] = None) -> None:
        for count, test in enumerate(tests, start=1):
            ver_in, ver_out = test
            if pre_release is None:
                ret = func(ver_in, position)
            else:
                ret = func(ver_in, position, pre_release)
            assert ver_out == ret

# Generated at 2022-06-13 20:46:46.903485
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    """Unit test for function bump_version."""
    # pylint: disable=C0103,W0212
    import sys

    def test_version(version):
        # print(version)
        sys.stdout.flush()
        ver_info = _build_version_info(version)
        pos_max = len(ver_info) - 3
        assert pos_max == 2
        for pre in ('', 'a', 'alpha', 'b', 'beta'):
            for pos in range(-3, 3):
                pos_out = _build_version_bump_position(pos)
                assert pos_out >= 0
                assert pos_out <= 2
                bump_type = _build_version_bump_type(pos_out, pre)

# Generated at 2022-06-13 20:46:59.358235
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=C0103
    '''Test for function bump_version'''
    def execute(version, position, expected_value):
        args = dict(position=position)
        if version[-1] in ('a', 'b'):
            kwargs = dict(pre_release=version[-1])
        else:
            kwargs = {}
        cmd = 'actual_value = bump_version(%r%s, **kwargs)' % (
            version[:-1],
            ', '.join('%s=%r' % (i, j) for i, j in sorted(args.items()))
        )
        exec(cmd)
        assert actual_value == expected_value

    execute('1.0.0', 2, '1.0.1')

# Generated at 2022-06-13 20:47:11.789461
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version."""
    from flutils.packages import bump_version

    part: str = '%s.%s.%s'

# Generated at 2022-06-13 20:47:23.113927
# Unit test for function bump_version
def test_bump_version():
    return None


if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:47:27.108329
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for :py:func:`flutils.packages.bump_version`.

    *New in version 0.3*

    """
    import pytest
    from flutils.packages import bump_version

    with pytest.raises(ValueError) as err:
        bump_version('1.2.3', position=3, pre_release='x')
    assert 'position' in str(err.value)

    with pytest.raises(ValueError) as err:
        bump_version('1.2.3', position=2, pre_release='x')
    assert 'x' in str(err.value)


# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et ts=4 sw=4

# Generated at 2022-06-13 20:47:38.720007
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version"""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=-2) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:47:48.671945
# Unit test for function bump_version
def test_bump_version():  # noqa: D103
    ver = '1.2.3'
    assert bump_version(ver) == '1.2.4'

    ver = '1.2.3'
    assert bump_version(ver, 1) == '1.3'
    ver = '1.3.4'
    assert bump_version(ver, 0) == '2.0'

    # Alpha
    ver = '1.2.3'
    assert bump_version(ver, pre_release='a') == '1.2.4a0'
    ver = '1.2.4a0'
    assert bump_version(ver, pre_release='a') == '1.2.4a1'
    ver = '1.2.4a1'

# Generated at 2022-06-13 20:47:58.956278
# Unit test for function bump_version
def test_bump_version():
    """Test each case."""

# Generated at 2022-06-13 20:48:10.547895
# Unit test for function bump_version
def test_bump_version():
    """Unit test function for function bump_version.
    """
    def _do_test_bump_version(
            version: str,
            position: int,
            pre_release: Optional[str],
            exp: tuple
    ) -> None:
        """
        noinspection PyUnusedLocal
        """
        act = bump_version(version, position, pre_release)
        assert exp == act

    base_version = '1.2.3'
    exp = '1.2.3'
    _do_test_bump_version(base_version, 2, None, exp)

    exp = '1.2.4'
    _do_test_bump_version(base_version, 2, 'a', exp)

    exp = '1.2.4a0'
    _do_test_bump

# Generated at 2022-06-13 20:48:15.710660
# Unit test for function bump_version
def test_bump_version():
    from .unittests import _test_bump_version
    _test_bump_version()


# Make sure the _test_bump_version function is called when module is not
# imported
if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:48:31.362681
# Unit test for function bump_version
def test_bump_version():
    """Test :func:`~flutils.packages.bump_version`."""

    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:48:37.885893
# Unit test for function bump_version
def test_bump_version():
    """Test the 'bump_version' function."""
    from flutils.packages import bump_version

    # test_bump_version__pos_gt_2
    # position > 2
    ver_info = _build_version_info('3.2.2')
    version = '3.2.2'
    pos_max = 2
    try:
        bump_version(version, position=pos_max + 1)
    except ValueError as exc:
        pos = str(pos_max + 1)
        t = "The given value for 'position', '%s', must be an 'int' "
        t += "between ('%s') and ('%s').'"
        assert str(exc) == t % (pos, str(pos_max * -1 - 1), str(pos_max))

    # test_bump_

# Generated at 2022-06-13 20:48:48.012164
# Unit test for function bump_version
def test_bump_version():
    """Unit test for ``bump_version``.

    *New in version 0.3.0*

    """
    from flutils.pkgutils import build_version_info
    import pytest

    ver_info = build_version_info('1.2.3')
    assert ver_info.major.num == 1
    assert ver_info.minor.num == 2
    assert ver_info.patch.num == 3

    ver_info = build_version_info('1.2.01')
    assert ver_info.major.num == 1
    assert ver_info.minor.num == 2
    assert ver_info.patch.num == 1

    ver_info = build_version_info('1.02.1')
    assert ver_info.major.num == 1
    assert ver_info.minor.num == 2

# Generated at 2022-06-13 20:49:12.096261
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=W0613,W0212,C0115
    """Import the module, and call bump_version(...) with a number of
    arguments.

    """
    import unittest
    import sys

  # pylint: disable=W0632

# Generated at 2022-06-13 20:49:20.418698
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:29.836076
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version."""
    # import lib.functools.bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:49:37.979932
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:46.193328
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    ver = '1.2.3'
    bump_ver = bump_version(ver)
    assert bump_ver == '1.2.4'
    bump_ver = bump_version(ver, position=1)
    assert bump_ver == '1.3'
    bump_ver = bump_version(ver, position=0)
    assert bump_ver == '2.0'
    bump_ver = bump_version(ver, prerelease='a')
    assert bump_ver == '1.2.4a0'
    bump_ver = bump_version(bump_ver, pre_release='a')
    assert bump_ver == '1.2.4a1'
    bump_ver = bump_version(bump_ver, pre_release='b')
    assert bump_ver

# Generated at 2022-06-13 20:49:55.806641
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

    from sys import _getframe
    from flutils.misc import print_err, get_module_name

    is_pass = False
    caller = get_module_name(parent=1, frame=_getframe())
    version = bump_version('1.2.2')
    if version == '1.2.3':
        is_pass = True
    else:
        print_err(
            'FAIL: {caller}'.format(caller=caller),
            'version should be "1.2.3", but is "{version}"'.format(
                version=version
            )
        )
    version = bump_version('1.2.3', position=1)
    if version == '1.3':
        is_pass = True
    else:
        print

# Generated at 2022-06-13 20:50:09.396289
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    ver: str
    # Test bumping a version without pre-release
    ver = bump_version('1.0')
    assert ver == '1.1'
    ver = bump_version('1.1')
    assert ver == '1.2'
    ver = bump_version('1.2')
    assert ver == '1.3'
    ver = bump_version('1.2.0')
    assert ver == '1.2.1'
    ver = bump_version('1.2.1')
    assert ver == '1.2.2'
    ver = bump_version('1.2.2')
    assert ver == '1.2.3'
    ver = bump_version('1.2.9')
    assert ver == '1.2.10'
    ver

# Generated at 2022-06-13 20:50:21.033343
# Unit test for function bump_version

# Generated at 2022-06-13 20:50:30.064746
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    from flutils.packages import bump_version
    func_name = 'flutils.packages.bump_version'
    error = 'The function, %s, is not functioning properly' % func_name

    ver = '1.2.2'
    res = bump_version(ver)
    assert res == '1.2.3', '%s (1)' % error

    ver = '1.2.3'
    res = bump_version(ver, position=1)
    assert res == '1.3', '%s (2)' % error

    ver = '1.3.4'
    res = bump_version(ver, position=0)
    assert res == '2.0', '%s (3)' % error

    ver = '1.2.3'
    res

# Generated at 2022-06-13 20:50:39.157226
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=inconsistent-return-statements
    """Test function ``bump_version``."""

# Generated at 2022-06-13 20:50:52.634963
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

# Generated at 2022-06-13 20:51:05.420606
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import _each_version_part
    from flutils.packages import bump_version
    from flutils.packages import _build_version_info
    import flutils.packages

    def _test_bump_version(
            version: str,
            position: int,
            pre_release: Optional[str] = None
    ) -> None:
        flutils.packages.bump_version(version, position, pre_release)

    def _test_build_version_info(version: str) -> None:
        _build_version_info(version)

    def _test_each_version_part(version: str) -> None:
        list(_each_version_part(StrictVersion(version)))

    # Ensure test is functioning
    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2022-06-13 20:51:13.248648
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=R0914
    """Unit test for function bump_version"""
    # pylint: disable=C0111

    import sys
    import unittest as ut

    from flutils.packages import bump_version

    class Test_bump_version(ut.TestCase):

        def test_1_smoke(self):
            """Smoke test."""
            # noinspection PyUnresolvedReferences
            expected = '1.2.3'
            actual = bump_version('1.2.2')
            msg = "bump_version() failed."
            self.assertEqual(expected, actual, msg)

        def test_2_position_1(self):
            """bump_version() - position=1"""
            expected = '1.3'

# Generated at 2022-06-13 20:51:20.521964
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=C0103
    import sys
    import itertools

    def _d(data):
        print(data, file=sys.stderr)

    if sys.version_info >= (3, 6):
        # pylint: disable=W0621,C0103
        from flutils.packages import bump_version
        from flutils.test_utils import DataTestCase

        class TestBumpVersion(DataTestCase):
            def _test_data(
                    self,
                    version: str,
                    position: int = 2,
                    pre_release: Optional[str] = None,
            ) -> str:
                return bump_version(version, position, pre_release)


# Generated at 2022-06-13 20:51:30.394540
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:51:41.510891
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version.

    Used by the :ref:`tasks_test` task.

    """

    from flutils.packages import bump_version

    version = '1.2.3'
    expected = '1.2.4'
    assert bump_version(version) == expected

    version = '1.2.3'
    expected = '1.3'
    assert bump_version(version, position=1) == expected

    version = '1.3.4'
    expected = '2.0'
    assert bump_version(version, position=0) == expected

    version = '1.2.3'
    expected = '1.2.4a0'
    assert bump_version(version, prerelease='a') == expected

    version = '1.2.4a0'
    expected

# Generated at 2022-06-13 20:51:54.483016
# Unit test for function bump_version
def test_bump_version():
    """Test the function 'bump_version'"""
    # # 1
    ver = bump_version('1.2.2')
    assert ver == '1.2.3'
    # # 2
    ver = bump_version('1.2.3', position=1)
    assert ver == '1.3'
    # # 3
    ver = bump_version('1.3.4', position=0)
    assert ver == '2.0'
    # # 4
    ver = bump_version('1.2.3', prerelease='a')
    assert ver == '1.2.4a0'
    # # 5
    ver = bump_version('1.2.4a0', pre_release='a')
    assert ver == '1.2.4a1'
    # # 6
    ver = bump_

# Generated at 2022-06-13 20:52:00.252064
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:52:15.311713
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:52:22.441662
# Unit test for function bump_version
def test_bump_version():
    """Unit test for bump_version()"""

    import os
    from textwrap import dedent
    from flutils.packages import (
        compare_versions,
        get_version
    )

    from .testingutils import (
        AssertIndexableLogger,
        AssertLogger,
        get_temp_dir,
        LogTestCase
    )

    # noinspection PyUnresolvedReferences
    from tests.versions import (
        compare_versions as cv,
        get_version as gv
    )

    class BumpVersionTestCase(LogTestCase):
        _log_level: int = 30
        _log_msg: str = 'Test'
        _temp_dir: str

        def setUp(self):
            self._temp_dir = get_temp_dir(prefix='flutils-')

# Generated at 2022-06-13 20:52:34.862890
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

# Generated at 2022-06-13 20:52:46.956495
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""

# Generated at 2022-06-13 20:52:59.394761
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version

    *New in version 0.3*

    """
    # pylint: disable=W0612
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'


# Generated at 2022-06-13 20:43:29.271110
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version
    from collections import namedtuple

    TestCase = namedtuple('TestCase', ['input', 'output', 'position', 'pre_release'])

# Generated at 2022-06-13 20:43:41.329438
# Unit test for function bump_version
def test_bump_version():
    """Test :py:func:`bump_version <flutils.packages.bump_version>`."""
    import unittest

    kls = bump_version.__wrapped__

    class Test(unittest.TestCase):
        def test__build_version_bump_type(self) -> None:
            """Test :py:func:`_build_version_bump_type`."""
            self.assertEqual(kls._build_version_bump_type(0, 'alpha'), 0)
            self.assertEqual(kls._build_version_bump_type(0, 'beta'), 0)
            self.assertEqual(kls._build_version_bump_type(0, 'a'), 0)

# Generated at 2022-06-13 20:43:53.059800
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=R0914
    """Unit test for function bump_version."""

    # Version bumping
    assert bump_version('1.0.0') == '1.0.1'
    assert bump_version('1.0.1') == '1.0.2'
    assert bump_version('1.1.0') == '1.1.1'
    assert bump_version('1.1.1') == '1.1.2'
    assert bump_version('1.2.0') == '1.2.1'
    assert bump_version('1.2.1') == '1.2.2'
    assert bump_version('1.0.0', position=0) == '2.0'

# Generated at 2022-06-13 20:43:58.552746
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=C0116,C0115,C0103
    # pylint: disable=W0612,W0611,W0622

    import unittest
    from flutils.packages import bump_version  # noqa

    class TestBumpVersion(unittest.TestCase):

        def test_bump_version(self):
            self.assertEqual(bump_version('1.2.2'), '1.2.3')

        def test_bump_version_position_1(self):
            self.assertEqual(bump_version('1.2.3', position=1), '1.3')


# Generated at 2022-06-13 20:44:11.180144
# Unit test for function bump_version
def test_bump_version():

    # pylint: disable=W0612,C0103
    from flutils.packages import bump_version as _bump_version

    # pylint: disable=W0612,C0103
    from flutils.testing import (
        cli_run,
        get_temp_file,
    )

    # Set the env var to run all tests
    os.environ['RUNALLUNITTESTS'] = '1'

    def _validate_version(version: str) -> bool:
        """Unit test API to validate a version number string."""
        try:
            ver_obj = StrictVersion(version)
            return True
        except ValueError:
            return False

    # Test positional args
    cur_ver = '1.2.2'

# Generated at 2022-06-13 20:44:18.257527
# Unit test for function bump_version
def test_bump_version():
    from pprint import pprint
    from flutils.packages import bump_version
    from flutils.testing import assert_is
    from flutils.testing import assert_isinstance
    from flutils.testing import assert_raises

    def _run(
            ret_val: str,
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None,
            expected_err: Optional[str] = None
    ) -> None:
        if expected_err is not None:
            assert_raises(
                ValueError,
                bump_version,
                version,
                position,
                pre_release
            )
            return

# Generated at 2022-06-13 20:44:23.328760
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=import-outside-toplevel,import-error
    import pytest

    # Bump major
    assert bump_version('1.2.3', 0) == '2.0'
    assert bump_version('1.2.3a1', 0) == '2.0'
    assert bump_version('1.2.3b1', 0) == '2.0'
    assert bump_version('1.0', 0) == '2.0'
    assert bump_version('1', 0) == '2'

    # Bump minor
    assert bump_version('1.2.3', 1) == '1.3'
    assert bump_version('1.2.3', 1, 'a') == '1.3a0'

# Generated at 2022-06-13 20:44:34.248798
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

# Generated at 2022-06-13 20:44:45.918468
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.0', position=1) == '1.3'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:44:54.497705
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0914
    """Unit test for 'bump_version' function"""
    from flutils.packages import bump_version

    # Simple tests to ensure none of the arguments are over looked.
    assert bump_version('1.0') == '1.1'
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.9.9') == '1.10'
    assert bump_version('1.0', position=1) == '2.0'
    assert bump_version('1.0', position=1, pre_release='b') == '2.0b0'
    assert bump_version('2.0b0', pre_release='a') == '2.0a0'

# Generated at 2022-06-13 20:45:31.049658
# Unit test for function bump_version
def test_bump_version():
    """Test the functionality of :func:`bump_version`."""
    v = '0.0.1'
    v1 = bump_version(v)
    assert v1 == '0.0.2'
    v2 = bump_version(v1, position=1)
    assert v2 == '0.1'
    v3 = bump_version(v2, position=0)
    assert v3 == '1.0'
    v4 = bump_version(v3, pre_release='a')
    assert v4 == '1.0a0'
    v5 = bump_version(v4, pre_release='a')
    assert v5 == '1.0a1'
    v6 = bump_version(v5, pre_release='b')
    assert v6 == '1.0b0'

# Generated at 2022-06-13 20:45:44.346494
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=protected-access
    # pylint: disable=W0212
    # pylint: disable=C0103
    v = _build_version_info('1.2.3')
    assert v.version == '1.2.3'
    assert v.major.pos == 0
    assert v.major.txt == '1'
    assert v.major.num == 1
    assert v.major.pre_txt == ''
    assert v.major.pre_num == -1
    assert v.major.name == 'major'
    assert v.minor.pos == 1
    assert v.minor.txt == '2'
    assert v.minor.num == 2
    assert v.minor.pre_txt == ''
    assert v.minor.pre_num == -1
   

# Generated at 2022-06-13 20:45:54.297537
# Unit test for function bump_version
def test_bump_version():
    assert(bump_version('1.2.2') == '1.2.3')
    assert(bump_version('1.2.3', position=1) == '1.3')
    assert(bump_version('1.3.4', position=0) == '2.0')
    assert(bump_version('1.2.3', prerelease='a') == '1.2.4a0')
    assert(bump_version('1.2.4a0', pre_release='a') == '1.2.4a1')
    assert(bump_version('1.2.4a1', pre_release='b') == '1.2.4b0')
    assert(bump_version('1.2.4a1') == '1.2.4')

# Generated at 2022-06-13 20:46:06.458779
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.packages import bump_version
    import pytest

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


# Generated at 2022-06-13 20:46:19.917954
# Unit test for function bump_version

# Generated at 2022-06-13 20:46:32.588601
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version.
    """
    print('Test function bump_version.')

# Generated at 2022-06-13 20:46:46.381361
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    """Test the bump_version function.

    """
    from pprint import pprint

# Generated at 2022-06-13 20:46:58.901980
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

# Generated at 2022-06-13 20:47:11.482725
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

# Generated at 2022-06-13 20:47:15.931768
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version

    """

# Generated at 2022-06-13 20:47:29.689343
# Unit test for function bump_version
def test_bump_version():
    import pytest

    name = 'bump_version'

    # Version number string.
    version_str: str = '1.2.3'
    # The position (starting with zero) of the version number component to be
    # increased.
    position: int = 2
    # A value of ``a`` or ``alpha`` will create or increase an alpha version
    # number.  A value of ``b`` or ``beta`` will create or increase a beta
    # version number.
    pre_release: Optional[str] = None

    test_args = [
        ('1.2.3', 2, None)
    ]

    test_kwargs = [
        dict(version=version_str, position=position, pre_release=pre_release)
    ]


# Generated at 2022-06-13 20:47:41.190429
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:47:44.069862
# Unit test for function bump_version
def test_bump_version():
    """Unit test for bump_version."""
    import sys
    sys.path.append('.')
    import test_utils
    return test_utils.run_test(bump_version, _build_version_info)

# Generated at 2022-06-13 20:47:57.040293
# Unit test for function bump_version
def test_bump_version():
    """Unit test for the "bump_version" function."""

    def _build_call(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ) -> str:
        try:
            return bump_version(
                version=version,
                position=position,
                pre_release=pre_release
            )
        except Exception as err:
            return str(err)

    def _should_be(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None,
            expected_result: str = ''
    ) -> bool:
        result = _build_call(
            version=version,
            position=position,
            pre_release=pre_release
        )
        return result == expected_result

    assert _

# Generated at 2022-06-13 20:48:09.885467
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.packages import bump_version
    from types import ModuleType
    from unittest import TestCase

    # noinspection PyUnresolvedReferences
    mod: ModuleType = bump_version.__module__
    mod_name = mod.split('.')[-1]
    func_name = bump_version.__name__

    class Tests(TestCase):
        """Test class for function bump_version."""

        maxDiff = None

        def test1_bump_version(self):
            """Test function bump_version with the default setup."""
            self.assertEqual(bump_version('1.2.2'), '1.2.3')

        def test2_bump_version(self):
            """Test function bump_version with minor position."""
            self

# Generated at 2022-06-13 20:48:21.660961
# Unit test for function bump_version
def test_bump_version():
    _test_bump_version(
        IN_VER='1.2.3',
        EXP_VER='1.2.4',
        ERR_MSG='Major version number should not change'
    )
    _test_bump_version(
        IN_VER='1.2.3',
        OUT_VER='1.3',
        POSITION=1,
        EXP_VER='1.3',
        ERR_MSG='Minor version number should increment by 1'
    )
    _test_bump_version(
        IN_VER='1.3.4',
        OUT_VER='2.0',
        POSITION=0,
        EXP_VER='2.0',
        ERR_MSG='Major version number should increment by 1'
    )

# Generated at 2022-06-13 20:48:32.704692
# Unit test for function bump_version
def test_bump_version():
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

# Generated at 2022-06-13 20:48:46.060875
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    thismod = sys.modules[__name__]
    thismod.helpers.run_protected(
        bump_version,
        '1.2.3',
        position=2,
        pre_release=None
    )
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

# Generated at 2022-06-13 20:48:56.016962
# Unit test for function bump_version
def test_bump_version():
    """Unit testing for the bump_version() function."""
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:49:03.907749
# Unit test for function bump_version
def test_bump_version():
    version = '1.2.3'
    assert bump_version(version) == '1.2.4'

    version = '1.2.3'
    assert bump_version(version, position=1) == '1.3'

    version = '1.2.3'
    assert bump_version(version, position=0) == '2.0'

    version = '1.2.3'
    assert bump_version(version, pre_release='a') == '1.2.4a0'

    version = '1.2.4a0'
    assert bump_version(version, pre_release='a') == '1.2.4a1'

    version = '1.2.4a1'
    assert bump_version(version, pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:49:21.882531
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for function bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', 1) == '1.3'
    assert bump_version('1.3.4', 0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', 'a') == '1.2.4a1'
    assert bump_version('1.2.4a1', 'b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:26.368380
# Unit test for function bump_version
def test_bump_version():
    print('Testing =======> function "bump_version"')
    print('returns: %r' % bump_version('1.2.2'))
    print('returns: %r' % bump_version('1.2.3', position=1))
    print('returns: %r' % bump_version('1.3.4', position=0))
    print('returns: %r' % bump_version('1.2.3', pre_release='a'))
    print('returns: %r' % bump_version('1.2.4a0', pre_release='a'))
    print('returns: %r' % bump_version('1.2.4a1', pre_release='b'))
    print('returns: %r' % bump_version('1.2.4a1'))

# Generated at 2022-06-13 20:49:40.556677
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


# Generated at 2022-06-13 20:49:47.119087
# Unit test for function bump_version
def test_bump_version():
    from .unittest_root import (
        UnittestRoot,
    )

# Generated at 2022-06-13 20:49:52.817703
# Unit test for function bump_version
def test_bump_version():
    from flutils.tests.py.check import check
    from flutils.packages import bump_version

    # The main tests
    check(bump_version('1.2.2'), '1.2.3')
    check(bump_version('1.2.3', position=1), '1.3')
    check(bump_version('1.3.4', position=0), '2.0')
    check(bump_version('1.2.3', prerelease='a'), '1.2.4a0')
    check(bump_version('1.2.4a0', pre_release='a'), '1.2.4a1')
    check(bump_version('1.2.4a1', pre_release='b'), '1.2.4b0')

# Generated at 2022-06-13 20:50:08.323381
# Unit test for function bump_version

# Generated at 2022-06-13 20:50:19.624219
# Unit test for function bump_version
def test_bump_version():
    # Major version increase
    assert bump_version('1.2.3') == '1.2.4'
    # Minor version increase
    assert bump_version('1.2.3', position=1) == '1.3'
    # Patch version increase
    assert bump_version('1.3.4', position=0) == '2.0'
    # Minor prerelease alpha
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    # Minor prerelease alpha increase
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    # Minor prerelease beta
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    #

# Generated at 2022-06-13 20:50:29.224392
# Unit test for function bump_version
def test_bump_version():
    from flutils.tests.helpers import _run_tst_func


# Generated at 2022-06-13 20:50:38.765731
# Unit test for function bump_version

# Generated at 2022-06-13 20:50:40.535229
# Unit test for function bump_version
def test_bump_version():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 20:51:27.877850
# Unit test for function bump_version
def test_bump_version():  # noqa: D103
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:51:40.394153
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    # Test 1
    ver_in = '1.2.2'
    bump_pos = 2
    bump_pre_release = None
    ver_out = bump_version(ver_in, position=bump_pos,
                           pre_release=bump_pre_release)
    assert ver_out == '1.2.3'
    # Test 2
    ver_in = '1.2.3'
    bump_pos = 1
    bump_pre_release = None
    ver_out = bump_version(ver_in, position=bump_pos,
                           pre_release=bump_pre_release)
    assert ver_out == '1.3'
    # Test 3
    ver_in = '1.3.4'
    bump_pos = 0

# Generated at 2022-06-13 20:51:53.889781
# Unit test for function bump_version
def test_bump_version():
    import flutils.packages as pkg
    import pytest
    # Return a version number increased by a number of positions
    assert pkg.bump_version('1.2.3') == '1.2.4', \
        'Test 1 of bump_version failed.'
    assert pkg.bump_version('1.2.3', position=1) == '1.3', \
        'Test 2 of bump_version failed.'
    assert pkg.bump_version('1.3.4', position=0) == '2.0', \
        'Test 3 of bump_version failed.'
    assert pkg.bump_version('1.2.3', prerelease='a') == '1.2.4a0', \
        'Test 4 of bump_version failed.'

# Generated at 2022-06-13 20:52:04.095579
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0915
    """Unit test for function bump_version"""
    # noinspection PyUnusedLocal
    def assert_bump_version_result(
            version: str,
            position: int,
            pre_release: Union[str, None],
            expected: str
    ):
        actual = bump_version(version, position, pre_release)
        msg = (
            "The given version number '%s', with a bump %s, pre-release %s, "
            "did not return the expected value.  Expected: '%s', got: '%s'"
        ) % (
            version,
            position,
            pre_release,
            expected,
            actual
        )
        assert expected == actual, msg

    # noinspection PyUnusedLocal

# Generated at 2022-06-13 20:52:18.333297
# Unit test for function bump_version

# Generated at 2022-06-13 20:52:32.119771
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:52:45.826397
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""

    import pytest
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:52:59.007383
# Unit test for function bump_version

# Generated at 2022-06-13 20:53:07.871774
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for package.bump_version()."""
    from ..unit_test import (
        FunctionTestCase,
        TestCase,
    )
    from ..unit_test.package_tests import (
        build_package_test_case,
        run_package_test_case,
    )

    from . import (
        __name__ as pkg_name,
        __title__ as pkg_title,
        __version__ as pkg_ver,
    )



# Generated at 2022-06-13 20:43:33.165188
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    from flutils.test import run_test_module_by_name

    run_test_module_by_name(__file__)


if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:43:44.174934
# Unit test for function bump_version
def test_bump_version():
    """Test bump_version function."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:43:55.567360
# Unit test for function bump_version

# Generated at 2022-06-13 20:44:05.307295
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for bump_version."""
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:44:15.283653
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""

# Generated at 2022-06-13 20:44:25.237860
# Unit test for function bump_version

# Generated at 2022-06-13 20:44:35.542931
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', prerelease='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', prerelease='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:39.899519
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    update_version = bump_version('1.2.3')
    assert update_version == '1.2.4', 'Version not updated'


# Generated at 2022-06-13 20:44:49.412587
# Unit test for function bump_version
def test_bump_version():
    """Unit testing for function bump_version"""
    # noinspection PyUnusedLocal
    res: List[Tuple[str, ...]] = []

    res.append(
        (
            bump_version('1.2.2', position=0),
            '2.0',
            "Bumping version '1.2.2' by the major part: 2.0"
        )
    )
    res.append(
        (
            bump_version('1.2.2', position=1),
            '1.3',
            "Bumping version '1.2.2' by the minor part: 1.3"
        )
    )

# Generated at 2022-06-13 20:44:54.446362
# Unit test for function bump_version
def test_bump_version():
    print('--- test_bump_version start')
    print('--- test_bump_version end')


if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:45:29.183880
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

# Generated at 2022-06-13 20:45:42.374742
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:45:52.829496
# Unit test for function bump_version
def test_bump_version():
    """Test the ``bump_version`` function.

    *New in version 0.3*

    """
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version

# Generated at 2022-06-13 20:46:05.575622
# Unit test for function bump_version

# Generated at 2022-06-13 20:46:13.649343
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version
    ver = bump_version('1.2.2')
    assert ver == '1.2.3'
    ver = bump_version('1.2.3', position=1)
    assert ver == '1.3'
    ver = bump_version('1.3.4', position=0)
    assert ver == '2.0'
    ver = bump_version('1.2.3', prerelease='a')
    assert ver == '1.2.4a0'
    ver = bump_version('1.2.4a0', pre_release='a')
    assert ver == '1.2.4a1'
    ver = bump_version('1.2.4a1', pre_release='b')
    assert ver == '1.2.4b0'
   

# Generated at 2022-06-13 20:46:21.993766
# Unit test for function bump_version
def test_bump_version():
    import unittest

    class Case(unittest.TestCase):
        def test_bump_version_normal(self):
            self.assertEqual(bump_version('1.2.2'), '1.2.3')
            self.assertEqual(bump_version('1.2.3', position=1), '1.3')
            self.assertEqual(bump_version('1.3.4', position=0), '2.0')
            self.assertEqual(bump_version('1.2.3', prerelease='a'), '1.2.4a0')
            self.assertEqual(bump_version('1.2.4a0', pre_release='a'), '1.2.4a1')

# Generated at 2022-06-13 20:46:33.147465
# Unit test for function bump_version
def test_bump_version():
    """Test the flutils.packages.bump_version() function.

    *New in version 0.3*

    """
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:46:46.691932
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for the bump_version function.
    """
    from flutils.packages import bump_version

    # Test for input: '1.2.2' Expected output is '1.2.3'
    assert bump_version('1.2.2') == '1.2.3'

    # Test for input: '1.2.3', position=1 Expected output is '1.3'
    assert bump_version('1.2.3', position=1) == '1.3'


    # Test for input: '1.3.4', position=0 Expected output is '2.0'
    assert bump_version('1.3.4', position=0) == '2.0'

    # Test for input: '1.2.3', prerelease='a' Expected output is '1.2

# Generated at 2022-06-13 20:46:59.358424
# Unit test for function bump_version
def test_bump_version():
    """Test bumping a version bump_version."""

# Generated at 2022-06-13 20:47:11.788759
# Unit test for function bump_version
def test_bump_version():
    import unittest

    class TestCase(unittest.TestCase):
        def test_bump_version_1(self):
            out = bump_version('1.2.2')
            self.assertEqual(out, '1.2.3')

        def test_bump_version_2(self):
            out = bump_version('1.2.3', position=1)
            self.assertEqual(out, '1.3')

        def test_bump_version_3(self):
            out = bump_version('1.3.4', position=0)
            self.assertEqual(out, '2.0')

        def test_bump_version_4(self):
            out = bump_version('1.2.3', prerelease='a')

# Generated at 2022-06-13 20:47:39.781210
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=too-many-branches,too-many-statements
    # pylint: disable=too-many-locals,too-many-nested-blocks
    import sys
    import io
    import unittest
    import flutils.packages as pkg

    class TestBumpVersion(unittest.TestCase):
        """Tests for the :func:`bump_version` function."""

        def setUp(self):
            self.maxDiff = None
            self.old_out: Optional[io.BytesIO] = None
            if sys.version_info.major >= 3:
                self.old_out = sys.stdout
                sys.stdout = io.BytesIO()

        def tearDown(self):
            if self.old_out is not None:
                sys.stdout

# Generated at 2022-06-13 20:47:50.536121
# Unit test for function bump_version
def test_bump_version():
    import unittest

    class VersionTests(unittest.TestCase):

        def test_version_01(self):
            from flutils.packages import bump_version
            rv = bump_version('1.2.2')
            self.assertEqual(rv, '1.2.3')

        def test_version_02(self):
            from flutils.packages import bump_version
            rv = bump_version('1.2.3', position=1)
            self.assertEqual(rv, '1.3')

        def test_version_03(self):
            from flutils.packages import bump_version
            rv = bump_version('1.3.4', position=0)
            self.assertEqual(rv, '2.0')


# Generated at 2022-06-13 20:47:59.899256
# Unit test for function bump_version
def test_bump_version():

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:06.395447
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

# Generated at 2022-06-13 20:48:19.778022
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

# Generated at 2022-06-13 20:48:32.901100
# Unit test for function bump_version
def test_bump_version():
    """Test the ``bump_version`` function.

    *New in version 0.3*

    """
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:48:46.099971
# Unit test for function bump_version
def test_bump_version():
    results = [
        bump_version('1.2.2'),
        bump_version('1.2.3', position=1),
        bump_version('1.3.4', position=0),
        bump_version('1.2.3', prerelease='a'),
        bump_version('1.2.4a0', pre_release='a'),
        bump_version('1.2.4a1', pre_release='b'),
        bump_version('1.2.4a1'),
        bump_version('1.2.4b0'),
        bump_version('2.1.3', position=1, pre_release='a'),
        bump_version('1.2b0', position=2),
    ]

# Generated at 2022-06-13 20:48:55.492671
# Unit test for function bump_version
def test_bump_version():  # pylint:disable=R0915
    """Unit test for the `bump_version` function."""
    import doctest
    test_results = doctest.testmod(
        # verbose=True,
        # Report only first and last failures.
        reportflags=(doctest.REPORT_ONLY_FIRST_FAILURE |
                     doctest.REPORT_NDIFF |
                     doctest.REPORT_ONLY_FIRST_FAILURE),
        optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
    )
    __tracebackhide__ = True  # pylint: disable=W0612
    assert test_results.failed == 0



# Generated at 2022-06-13 20:49:03.778528
# Unit test for function bump_version
def test_bump_version():
    """Tests the function bump_version.
    """
    func = bump_version

    # noinspection PyUnusedLocal

# Generated at 2022-06-13 20:49:13.523729
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function `bump_version`."""

    from unittest import TestCase, main
    from sys import version_info
    from distutils.version import StrictVersion
    from flutils.packages import bump_version
    from flutils.data_structures import null_func

    if version_info >= (3, 9):
        from pathlib import Path
        from importlib.metadata import version as VERSION
        from importlib.metadata import PackageNotFoundError

        def get_version(pkg_name: str) -> str:
            """Retrieve the version number of a package."""
            try:
                pkg_name_expand = pkg_name.replace('-', '_')
                return VERSION(pkg_name_expand)
            except PackageNotFoundError:
                return '0.0.0'



# Generated at 2022-06-13 20:49:31.588731
# Unit test for function bump_version
def test_bump_version():
    from flutils.assertutils import assert_object_exists
    from flutils.assertutils import assert_not_equal
    from flutils.assertutils import assert_true
    from flutils.assertutils import assert_true_with_info
    from flutils.assertutils import assert_false

    ########################################################################
    # Test 1
    title = "Test 1: 'bump_version' is a function."

    assert_object_exists(bump_version, 'bump_version')
    assert_true(callable(bump_version), title)

    ########################################################################
    # Test 2
    title = "Test 2: Normal use."


# Generated at 2022-06-13 20:49:47.440609
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

# Generated at 2022-06-13 20:49:56.105668
# Unit test for function bump_version
def test_bump_version():  # NOQA
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:50:09.510403
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=C0116
    # pylint: disable=E0001
    # noinspection PyUnresolvedReferences
    from flutils.packages import bump_version

    # Test only major bump
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.3', 0) == '2.0'
    assert bump_version('1.2.4', 0, 'a') == '2.0'

    # Test only minor bump
    assert bump_version('1.2.3', 1) == '1.3'
    assert bump_version('1.2.3', 1, 'a') == '1.3a0'
    assert bump_version('1.2.3', 1, 'b') == '1.3b0'

   

# Generated at 2022-06-13 20:50:21.070585
# Unit test for function bump_version

# Generated at 2022-06-13 20:50:27.348548
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    test_suite = unittest.TestSuite()
    test_suite.addTest(
        unittest.TestLoader().loadTestsFromTestCase(
            TestBumpVersion
        )
    )
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)



# Generated at 2022-06-13 20:50:37.898073
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    from json import dumps
    from pprint import pprint
    from sys import version_info
    from typing import List, Tuple


    def clean_test_data(test_data: Tuple[List[int], List[int]]) -> str:
        ret = []
        for num in test_data[1]:
            txt = '{}'.format(num)
            if ret and txt == '0':
                ret.append('')
            else:
                ret.append(txt)
        return '.'.join(ret)


    # This works around the problem where tests run on Python 2.7.12 doesn't
    # get the expected result.  That is, if this code is run on that
    # Python version, it will yield the wrong answer.   If you run this same
    # code

# Generated at 2022-06-13 20:50:49.665395
# Unit test for function bump_version
def test_bump_version():
    """Test the function `bump_version` against known good values."""
    # pylint: disable=R0914
    # noinspection PyUnresolvedReferences
    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.2', position=2, pre_release='a') == '1.2.3a0'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'

# Generated at 2022-06-13 20:51:02.284397
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version.
    """

    # pylint: disable=W0612,W0613
    from copy import deepcopy
    from unittest.mock import Mock, patch

    from pytest_toolbox.comparison import AnyInt, AnyString
    from flutils.packages import bump_version
    from flutils.testing import Tools, assert_str

    fct = bump_version
    Tools.assert_eq_comp(
        fct('1.2.3'),
        '1.2.3',
        cmp_fct=assert_str
    )

# Generated at 2022-06-13 20:51:13.320322
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

    version = bump_version('1.2.3')
    assert version == '1.2.4', version

    version = bump_version('1.2.3', position=1)
    assert version == '1.3', version

    version = bump_version('1.3.4', position=0)
    assert version == '2.0', version

    version = bump_version('1.2.3', pre_release='a')
    assert version == '1.2.4a0', version

    version = bump_version('1.2.4a1', pre_release='a')
    assert version == '1.2.4a2', version

    version = bump_version('1.2.4a1', pre_release='b')

# Generated at 2022-06-13 20:51:31.477089
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    from flutils.commonutils import assert_equals
    from flutils.commonutils import assert_exception
    from flutils.commonutils import assert_not_equals
    from flutils.commonutils import assert_true


# Generated at 2022-06-13 20:51:41.377816
# Unit test for function bump_version
def test_bump_version():
    """Function bump_version tests."""
    bump_version('1.2.2')
    bump_version('1.2.3', position=1)
    bump_version('1.3.4', position=0)
    bump_version('1.2.3', pre_release='a')
    bump_version('1.2.4a0', pre_release='a')
    bump_version('1.2.4a1', pre_release='b')
    bump_version('1.2.4a1')
    bump_version('1.2.4b0')
    bump_version('2.1.3', position=1, pre_release='a')
    bump_version('1.2b0', position=2)

# Generated at 2022-06-13 20:51:54.451400
# Unit test for function bump_version
def test_bump_version():
    r"""Unit test for function ``bump_version``.

    """
    # pylint: disable=R0915,R0912,R0914,C0330

    from collections.abc import Iterable
    from itertools import zip_longest

    from flutils.common_utils import callable_reference
    from flutils.packages import bump_version

    class MTest(_VersionInfo):
        """Wrapper class for test cases.

        """

        def __init__(
                self,
                version,
                major,
                minor,
                patch,
                pre_pos,
                position,
                pre_release,
                expected
        ):
            """Initialize the class.

            """
            super().__init__(version, major, minor, patch, pre_pos)
            self.version = version

# Generated at 2022-06-13 20:52:04.412592
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

    # ... pylint: disable=C0111,C0103
    import unittest

    class TestBumpVersion(unittest.TestCase):

        def test_basic_bump_version(self):
            major = bump_version('1.2.3', 0)
            self.assertEqual(major, '2.0')
            minor = bump_version('1.2.3', 1)
            self.assertEqual(minor, '1.3')
            patch = bump_version('1.2.3')
            self.assertEqual(patch, '1.2.4')
            patch = bump_version('1.2.3', 2)
            self.assertEqual(patch, '1.2.4')


# Generated at 2022-06-13 20:52:18.453699
# Unit test for function bump_version
def test_bump_version():
    from flutils.packages import bump_version
    version = '1.2.2'
    assert bump_version(version) == '1.2.3'
    version = '1.2.3'
    assert bump_version(version, position=1) == '1.3'
    version = '1.3.4'
    assert bump_version(version, position=0) == '2.0'
    version = '1.2.3'
    assert bump_version(version, prerelease='a') == '1.2.4a0'
    version = '1.2.4a0'
    assert bump_version(version, pre_release='a') == '1.2.4a1'
    version = '1.2.4a1'
    assert bump_version(version, pre_release='b')

# Generated at 2022-06-13 20:52:32.180492
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'

    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:52:45.869889
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:52:59.042464
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover, no branch
    import os.path

    # pylint: disable=W1401
    import nose.core
    import nose.loader

    # noinspection PyUnresolvedReferences,PyTypeChecker
    import flutils.packages

    print('Executing unit tests for module: "%s"' % __file__)

    package_dir: str = os.path.dirname(__file__)
    package_dir = os.path.dirname(package_dir)

    # noinspection PyUnresolvedReferences,PyTypeChecker
    import tests
    tests_dir: str = os.path.dirname(tests.__file__)

    args = ['nosetests']
    args.append(package_dir)
    args.append(tests_dir)
    # args.append('--verbose')


# Generated at 2022-06-13 20:53:07.346699
# Unit test for function bump_version
def test_bump_version():
    """Unit test :func:`bump_version`."""
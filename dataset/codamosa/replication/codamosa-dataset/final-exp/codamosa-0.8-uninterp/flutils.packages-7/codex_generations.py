

# Generated at 2022-06-13 20:43:29.216525
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for function bump_version
    """
    import sys
    import inspect
    import unittest

    from flutils.packages import bump_version

    class Test_bump_version(unittest.TestCase):

        def test_bump_version_000(self):
            """Test for function bump_version: simple incrementation.
            """
            self.maxDiff = None
            ver = '0.0.1'
            out = '0.0.2'
            got = bump_version(ver, position=2)
            self.assertEqual(got, out)

        def test_bump_version_001(self):
            """Test for function bump_version: simple incrementation.
            """
            self.maxDiff = None
            ver = '0.0.1'

# Generated at 2022-06-13 20:43:32.882742
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version function."""
    from test import flutils_pkg_test
    flutils_pkg_test.test_functions(bump_version)

# Generated at 2022-06-13 20:43:43.842125
# Unit test for function bump_version
def test_bump_version():
    """Test bump_version with various valid and invalid values."""

    # Test version number strings that bump_version should be able to process.
    versions = (
        '1.0',
        '1.3',
        '1.3.0',
        '1.3.1',
        '1.3.2',
    )

    # Test version number strings that bump_version will raise a ValueError on.

# Generated at 2022-06-13 20:43:55.277837
# Unit test for function bump_version
def test_bump_version():
    """Unit test for the `bump_version` function."""
    import sys
    import subprocess
    import flutils.testing

    version = '1.2.4'

# Generated at 2022-06-13 20:44:01.617373
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version function.

    """
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:13.474768
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=line-too-long
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version

# Generated at 2022-06-13 20:44:24.549103
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=C0103
    """ Unit test for ``bump_version``. """
    from flutils.packages import bump_version
    from logging import getLogger
    from sys import version_info

    _LOG = getLogger(__name__)
    if version_info[0] < 3:
        # noinspection PyCompatibility
        from unittest2 import TestCase
    else:
        from unittest import TestCase

    # pylint: disable=too-few-public-methods
    class BasicTests(_TestCase):
        """ Unit tests for ``bump_version``. """

        # pylint: disable=too-many-locals,too-many-nested-blocks,too-many-branches,protected-access

# Generated at 2022-06-13 20:44:35.215054
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:46.520829
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

# Generated at 2022-06-13 20:44:53.561562
# Unit test for function bump_version
def test_bump_version():
    """Unit-test: flutils.packages.bump_version"""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:45:18.664564
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

# Generated at 2022-06-13 20:45:30.370620
# Unit test for function bump_version
def test_bump_version():
    """Test the function, bump_version."""
    import os
    import re
    import pytest

    def _get_test_data() -> List[Any]:
        data: List[Any] = []
        base = os.path.join(os.path.dirname(__file__), 'testdata', 'bumpver')
        for item in os.listdir(base):
            if item.startswith('.'):
                continue
            item = os.path.join(base, item)
            if os.path.isdir(item) is False:
                continue
            data.append(item)
        return data

    def _get_test_data_version(path: str) -> str:
        with open(os.path.join(path, 'VERSION'), 'rt') as patch_fh:
            ver = patch_

# Generated at 2022-06-13 20:45:42.893061
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version."""
    set_color(color=False)
    set_color(color=True)
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:45:53.442501
# Unit test for function bump_version
def test_bump_version():
    from collections import namedtuple
    from flutils.packages import bump_version

    A = namedtuple('A', 'version, position, pre_release, result')


# Generated at 2022-06-13 20:46:06.065020
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=C0115
    """Unit test for function bump_version."""
    # Tuple of each test.
    # Tuple of:
    #   - Input.  Tuple of:
    #     - Version number.
    #     - Position to bump.
    #     - The pre-release flag to add.
    #   - Expected output.

# Generated at 2022-06-13 20:46:13.669433
# Unit test for function bump_version
def test_bump_version():
    def test(ver, pos, pre):
        ver_info = _build_version_info(ver)
        position = _build_version_bump_position(pos)
        bump_type = _build_version_bump_type(position, pre)
        print(bump_version(ver, pos, pre))
        hold = []
        if bump_type == _BUMP_VERSION_MAJOR:
            hold = [ver_info.major.num + 1, 0]
        elif bump_type in _BUMP_VERSION_MINORS:
            if bump_type == _BUMP_VERSION_MINOR:
                if ver_info.minor.pre_txt:
                    hold = [ver_info.major.num, ver_info.minor.num]

# Generated at 2022-06-13 20:46:22.023489
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    import sys
    import pytest

    # noinspection PyUnresolvedReferences
    import flutils
    flutils.setup_logging(loglevel=10, log_to_console=True)
    logger = flutils.get_logger(name=__name__)
    logger.info("Running tests on function bump_version")

    errors = []
    def _error_collector(error):
        """Collect the errors from pytest."""
        errors.append(error)

    class ErrorCollector:
        """Collect the errors from pytest."""
        def __init__(self):
            self._errors = []
        def pytest_collectreport(self, report):
            """Pytest will call this to collect errors."""
            if report.failed:
                self._errors

# Generated at 2022-06-13 20:46:32.218446
# Unit test for function bump_version
def test_bump_version():
    import unittest

    class _TestCase(unittest.TestCase):
        def test_bump_version_major(self):
            self.assertEqual(
                bump_version(version='1.2.3', position=0, pre_release=None),
                '2.0',
            )

        def test_bump_version_minor(self):
            self.assertEqual(
                bump_version(version='1.2.3', position=1, pre_release=None),
                '1.3',
            )

        def test_bump_version_patch(self):
            self.assertEqual(
                bump_version(version='1.2.3', position=2, pre_release=None),
                '1.2.4',
            )


# Generated at 2022-06-13 20:46:46.142724
# Unit test for function bump_version

# Generated at 2022-06-13 20:46:58.687552
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for function bump_version."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:47:22.685797
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    # pylint: disable=C0116, R0915

    from flutils.packages import bump_version

    from distutils.version import StrictVersion

    def _build_case(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ) -> Tuple[bool, str, str, str]:
        try:
            out = bump_version(version, position, pre_release)
        except ValueError as exc:
            is_error = True
            err = exc
        else:
            is_error = False
            err = ''
        return is_error, version, out, err


# Generated at 2022-06-13 20:47:35.259353
# Unit test for function bump_version
def test_bump_version():
    """Test the __version__ constant"""
    # pylint: disable=W0612, W0621
    from flutils.packages import __version__, bump_version

    print("\nTesting bump_version()")
    # noinspection PyUnusedLocal
    current_version = __version__
    current_version = bump_version(current_version)
    current_version = bump_version(current_version)
    current_version = bump_version(current_version)
    current_version = bump_version(current_version)
    current_version = bump_version(current_version)
    current_version = bump_version(current_version, pre_release='a')
    current_version = bump_version(current_version, pre_release='a')

# Generated at 2022-06-13 20:47:47.509914
# Unit test for function bump_version

# Generated at 2022-06-13 20:47:58.360052
# Unit test for function bump_version
def test_bump_version():
    """
    This function contains unit tests for the bump_version function.

    """

    # pylint: disable=W0612,W0613,W0621
    import unittest

    class TestBumpVersion(unittest.TestCase):
        """
        This class contains unit tests for the bump_version function.

        """

        def test_1(self):
            """Testing when pre_release is not supplied.

            """

            self.assertEqual(bump_version('1.2.3'), '1.2.4')
            self.assertEqual(bump_version('1.2.3', position=-1), '2.0')
            self.assertEqual(bump_version('1.2.3', position=-2), '1.3')

# Generated at 2022-06-13 20:48:10.298802
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=R0914
    from six import assertRaisesRegex  # pylint: disable=E0401
    from flutils.packages import bump_version

    # Test 1: Should be able to bump a text version number
    assert bump_version('1.2.2') == '1.2.3'

    # Test 2: Should be able to bump a text version number with a minor version
    # bump
    assert bump_version('1.2.3', position=1) == '1.3'

    # Test 3: Should be able to bump a text version number with a major
    # version bump
    assert bump_version('1.3.4', position=0) == '2.0'

    # Test 4: Should be able to bump a text version number pre-release

# Generated at 2022-06-13 20:48:21.735064
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

# Generated at 2022-06-13 20:48:33.786466
# Unit test for function bump_version
def test_bump_version():
    """Unit testing for the :func:`flutils.packages.bump_version` function."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:48:46.512254
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:48.527549
# Unit test for function bump_version
def test_bump_version():
    import doctest
    doctest.testmod(
        optionflags=doctest.ELLIPSIS |
        doctest.NORMALIZE_WHITESPACE
    )

# Generated at 2022-06-13 20:48:57.881306
# Unit test for function bump_version
def test_bump_version():
    """
    .. todo::
        * Add doctests.
    """
    from flutils.packages import bump_version
    print(bump_version('1.2.2'))
    print(bump_version('1.2.3', position=1))
    print(bump_version('1.3.4', position=0))
    print(bump_version('1.2.3', prerelease='a'))
    print(bump_version('1.2.4a0', pre_release='a'))
    print(bump_version('1.2.4a1', pre_release='b'))
    print(bump_version('1.2.4a1'))
    print(bump_version('1.2.4b0'))

# Generated at 2022-06-13 20:49:40.513254
# Unit test for function bump_version
def test_bump_version():
    """Unit test for the ``bump_version`` function."""

    # The testing version
    version = '1.2.3'

    # No change.
    out = bump_version(version, position=-3)
    assert out == '1.2.3'

    # Bump the patch minor.
    out = bump_version(version)
    assert out == '1.2.4'

    # Bump the minor minor.
    out = bump_version(version, position=1)
    assert out == '1.3'

    # Bump the major minor.
    out = bump_version(version, position=0)
    assert out == '2.0'

    # Add an alpha bump to the minor minor.
    out = bump_version(version, position=1, pre_release='a')

# Generated at 2022-06-13 20:49:47.092872
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:56.106718
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for flutils.packages.bump_version.
    """
    func_ref = bump_version
    assert func_ref('1.2.2') == '1.2.3'
    assert func_ref('1.2.3', position=1) == '1.3'
    assert func_ref('1.3.4', position=0) == '2.0'
    assert func_ref('1.2.3', prerelease='a') == '1.2.4a0'
    assert func_ref('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert func_ref('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert func_ref('1.2.4a1')

# Generated at 2022-06-13 20:50:08.974867
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

# Generated at 2022-06-13 20:50:20.717522
# Unit test for function bump_version
def test_bump_version():

    # Bump the patch part for a release
    ver_info = _build_version_info('1.2.3')
    assert ver_info.patch.num == 3

    ver_info = _build_version_info('1.2.0')
    assert ver_info.patch.num == 0

    res = bump_version('1.2.3')
    assert res == '1.2.4'

    res = bump_version('1.2.0')
    assert res == '1.2.1'

    # Bump the patch part for an alpha release
    ver_info = _build_version_info('1.2.3a0')
    assert ver_info.patch.num == 3
    assert ver_info.patch.pre_txt == 'a'
    assert ver_info.patch.pre_num == 0

# Generated at 2022-06-13 20:50:31.564989
# Unit test for function bump_version
def test_bump_version():
    from random import randint
    from pprint import pformat

    class _Kwargs(NamedTuple):
        version: str
        position: int
        pre_release: str

    def _build_kwargs(
            position: int,
            pre_release: str
    ) -> _Kwargs:
        ver_part: str
        if pre_release in ('a', 'alpha', 'b', 'beta'):
            ver_part = pre_release
        else:
            ver_part = '%s' % randint(1, 10)
        position = randint(1, 3)
        pre_release_num = randint(0, 10)
        kwargs = _Kwargs(
            version='',
            position=position,
            pre_release=pre_release
        )

# Generated at 2022-06-13 20:50:39.841421
# Unit test for function bump_version
def test_bump_version():
    """Unit test for the bump_version function.

    :returns:
        :obj:`None`

    """
    import unittest
    import sys
    from io import StringIO
    from random import randint, uniform, shuffle
    from unittest.mock import patch, MagicMock
    from flutils.packages import (
        bump_version,
        _build_version_info,
        _build_version_bump_position,
        _build_version_bump_type,
    )

    class Tester(unittest.TestCase):
        """Unit test class for the bump_version function."""

        # noinspection PyUnusedLocal
        def __init__(self, *args, **kwargs):
            """Class constructor."""
            self._version: Optional[str] = None
            self._pos

# Generated at 2022-06-13 20:50:55.079165
# Unit test for function bump_version
def test_bump_version():
    # noinspection PyUnusedLocal
    def _test(
            version: str,
            position: int,
            pre_release: Optional[str],
            expected: str
    ):
        result = bump_version(version, position, pre_release)
        assert result == expected

    _test('1.2.2', 2, None, '1.2.3')
    _test('1.2.3', 1, None, '1.3')
    _test('1.3.4', 0, None, '2.0')
    _test('1.2.3', 2, 'a', '1.2.4a0')
    _test('1.2.4a0', 2, 'a', '1.2.4a1')

# Generated at 2022-06-13 20:51:07.102686
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:51:18.324550
# Unit test for function bump_version
def test_bump_version():
    '''
    Runs a test of the bump_version function against the expected output of the
    bump_version function based on the input.
    '''
    # pylint: disable=unnecessary-lambda,unnecessary-comprehension

# Generated at 2022-06-13 20:51:54.744687
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version.
    """

# Generated at 2022-06-13 20:52:00.474388
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from collections import Counter

    from flutils.packages import bump_version

    from flutils.testing.mock import (
        MagicMock,
        patch
    )

    version_start = '4.4.7'
    version_1 = bump_version(version_start)
    version_2 = bump_version(version_1)
    version_3 = bump_version(version_2)
    version_4 = bump_version(version_3)
    version_5 = bump_version(version_4, position=1)
    version_6 = bump_version(version_5, pre_release='b')
    version_7 = bump_version(version_6)
    version_8 = bump_version(version_7)

# Generated at 2022-06-13 20:52:15.438943
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version"""

    try:
        bump_version('1.2.3', position=0, pre_release='a')
        assert False
    except ValueError:
        pass
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

# Generated at 2022-06-13 20:52:22.486739
# Unit test for function bump_version
def test_bump_version():
    """Test the function: ``bump_version``."""
    import pytest
    from flutils.packages import bump_version as test_function

    version = '1.2.3'


# Generated at 2022-06-13 20:52:33.811505
# Unit test for function bump_version

# Generated at 2022-06-13 20:52:42.007042
# Unit test for function bump_version
def test_bump_version():
    """ Unit testing for bump_version """

    import os
    import sys
    import traceback
    from flutils.packages import bump_version

    TEST_FILE = os.environ.get('TEST_FILE')
    if TEST_FILE is None:
        TEST_FILE = os.path.join(os.path.expanduser('~'), 'test.txt')

    # Holds test info.
    class _Data(NamedTuple):
        in_ver: str
        out_ver: str
        position: int
        pre_release: Optional[str]


# Generated at 2022-06-13 20:52:51.118008
# Unit test for function bump_version
def test_bump_version():
    """Unit testing function bump_version"""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:53:01.877609
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
    # noinspection PyUnusedLocal
    def dummy():
        """Dummy function"""
        pass

    import unittest

    class TestUtilsPackages(unittest.TestCase):
        """Class to test flutils.utils.packages"""

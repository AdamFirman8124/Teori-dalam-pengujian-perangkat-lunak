

# Generated at 2022-06-13 20:43:33.709650
# Unit test for function bump_version
def test_bump_version():
    """
    .. code-block:: bash

        python -m flutils.packages.bump_version
    """
    import sys
    import unittest


    class TestMethods(unittest.TestCase):

        @staticmethod
        def test_bump_version():
            """
            .. code-block:: python

                from flutils.packages import bump_version
                bump_version('1.2.2')
            """
            v = bump_version('1.2.2')
            assert v == '1.2.3'


        @staticmethod
        def test_bump_version_minor():
            """
            .. code-block:: python

                from flutils.packages import bump_version
                bump_version('1.2.2', position=1)
            """

# Generated at 2022-06-13 20:43:44.913914
# Unit test for function bump_version
def test_bump_version():
    version = '1.2.2'
    assert bump_version(version) == '1.2.3'
    assert bump_version(version, position=1) == '1.3'
    assert bump_version(version, position=0) == '2.0'
    assert bump_version(version, prerelease='a') == '1.2.4a0'
    assert bump_version(version, pre_release='a') == '1.2.4a1'
    assert bump_version(version, pre_release='b') == '1.2.4b0'
    assert bump_version(version) == '1.2.4'
    assert bump_version(version) == '1.2.4'

# Generated at 2022-06-13 20:43:56.147167
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version()."""
    # pylint: disable=C0103
    from flutils.packages import bump_version
    from flutils.tests.pytest_helpers import assert_type_equals

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.2a0') == '1.2.2'
    assert bump_version('1.2b0') == '1.2.0'
    assert bump_version('1.2.2', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'

# Generated at 2022-06-13 20:44:06.199125
# Unit test for function bump_version
def test_bump_version():
    """
    Unit tests for function :obj:`~flutils.packages.bump_version`.

    Returns:
        :obj:`dict`

        * The unit test results.

    """
    bump_version_major_test: Tuple[
        str, Union[int, None, str], str
    ] = (
        '1.2.3', None, '2.0'
    )
    bump_version_minor_test: Tuple[
        str, Union[int, None, str], str
    ] = (
        '1.2.3', 1, '1.3'
    )
    bump_version_patch_test: Tuple[
        str, Union[int, None, str], str
    ] = (
        '1.2.3', 2, '1.2.4'
    )

# Generated at 2022-06-13 20:44:15.795468
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:25.461101
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:35.573591
# Unit test for function bump_version
def test_bump_version():
    func = bump_version

    assert func('1.2.2') == '1.2.3'

    assert func('1.2.3', position=1) == '1.3'
    assert func('1.3.4', position=0) == '2.0'

    assert func('1.2.3', prerelease='a') == '1.2.4a0'
    assert func('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert func('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert func('1.2.4a1') == '1.2.4'
    assert func('1.2.4b0') == '1.2.4'


# Generated at 2022-06-13 20:44:46.819224
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

# Generated at 2022-06-13 20:44:54.587379
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:45:05.045908
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version function."""
    import flutils.packages as _packages

# Generated at 2022-06-13 20:45:38.775533
# Unit test for function bump_version
def test_bump_version():
    """Unit test for the function ``bump_version``."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump

# Generated at 2022-06-13 20:45:50.618866
# Unit test for function bump_version

# Generated at 2022-06-13 20:46:03.402945
# Unit test for function bump_version
def test_bump_version():
    r = bump_version('1.2.2')
    assert r == '1.2.3'
    r = bump_version('1.2.3', position=1)
    assert r == '1.3'
    r = bump_version('1.3.4', position=0)
    assert r == '2.0'
    r = bump_version('1.2.3', pre_release='a')
    assert r == '1.2.4a0'
    r = bump_version('1.2.4a0', pre_release='a')
    assert r == '1.2.4a1'
    r = bump_version('1.2.4a1', pre_release='b')
    assert r == '1.2.4b0'

# Generated at 2022-06-13 20:46:12.754595
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from collections import namedtuple
    from pprint import pprint
    from os import path
    import pytest

    VERSION = '0.3.0'

    VersionParts = namedtuple('VersionParts', 'major minor patch')

    Version = namedtuple('Version', 'version parts')

    class VersionInfo(Version):
        @property
        def major(self):
            return self.parts.major

        @property
        def minor(self):
            return self.parts.minor

        @property
        def patch(self):
            return self.parts.patch

    class TestVersionInfo(VersionInfo):
        def __str__(self):
            return self.version

        def __repr__(self):
            return "TestVersionInfo('%s')" % self.version



# Generated at 2022-06-13 20:46:23.124411
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for flutils.packages.bump_version
    """
    from flutils.misc import get_caller_name
    import unittest

    class TestBumpVersion(unittest.TestCase):
        """ Test class for flutils.packages.bump_version() """
        def test_bump_version(self):
            """ Test for flutils.packages.bump_version() """
            from flutils.packages import bump_version

            self.assertEqual(bump_version('1.2.2'), '1.2.3')
            self.assertEqual(bump_version('1.2.3', position=1), '1.3')
            self.assertEqual(bump_version('1.3.4', position=0), '2.0')
            self.assertEqual

# Generated at 2022-06-13 20:46:34.430093
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version."""
    from flutils.packages import bump_version
    from flutils.testing import assert_equal


# Generated at 2022-06-13 20:46:47.247951
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version function."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:59.522466
# Unit test for function bump_version
def test_bump_version():

    # Cleanup
    dict_test = {
        '1.2.3': '1.2.4',
        '1.2.3.4': '1.2.4.0',
        '1.2.3.4.5': '1.2.4.0.0',
        '1.2.4': '1.3',
        '1.2.4.5': '1.3.0',
        '1.2.4.5.6': '1.3.0.0',
        '1.3.4': '2.0',
        '1.3.4.5': '2.0.0',
        '1.3.4.5.6': '2.0.0.0',
    }
    for k, v in dict_test.items():
        assert bump

# Generated at 2022-06-13 20:47:11.959291
# Unit test for function bump_version
def test_bump_version():
    args: List[Tuple[str, ...]] = [
        ('0.0.0',),
        ('0.0.1',),
        ('0.0.2',),
        ('1.2.2',),
        ('1.2.3',),
        ('1.2.3a0',),
        ('1.2.3a1',),
        ('2.0',),
    ]
    for arg in args:
        assert bump_version(*arg) == '1.2.3'
    args = [('1.2.3',), ('1.2.3', 1), ('1.2.3', 1, 'alpha')]
    for arg in args:
        assert bump_version(*arg) == '1.3'
    args = [('1.3',), ('1.3', 0)]


# Generated at 2022-06-13 20:47:22.501151
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    """Unit test for function bump_version.

    """
    # Test bumping major version number
    assert bump_version('0.0.19') == '1.0'
    assert bump_version('1.0.0') == '2.0'
    # Test bumping minor version number
    assert bump_version('1.0.19', position=1) == '1.1'
    assert bump_version('1.1.1', position=1) == '1.2'
    assert bump_version('1.1.1', position=1, pre_release='a') == '1.2a0'
    # Test bumping patch version number
    assert bump_version('1.0.19', position=2) == '1.0.20'

# Generated at 2022-06-13 20:47:38.782471
# Unit test for function bump_version
def test_bump_version():
    """Test the :func:`bump_version` function."""
    import sys

    # noinspection PyUnusedLocal
    def _(version, position):
        # noinspection PyUnresolvedReferences
        if sys.version_info < (3, 7):
            return '%s' % version
        return version


# Generated at 2022-06-13 20:47:47.085354
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from os import path
    from sys import modules
    from flutils.testing import run_tests

    mod_path = modules[__name__].__file__
    this_dir = path.dirname(mod_path)
    return run_tests(
        path.join(this_dir, 'test_bump_version.md'),
        globals(),
        supported_formats=['text', 'rst'],
    )


if __name__ == '__main__':
    import sys
    sys.exit(test_bump_version())

# Generated at 2022-06-13 20:47:58.107604
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

# Generated at 2022-06-13 20:48:10.263754
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version

    _Returns_
        :obj:`bool`
            * ``True`` if the tests run successfully.

    """
    from .testing import (
        TEST_TARGET,
        TestTarget,
    )

    bt = TestTarget()
    bt.add_test(
        TEST_TARGET,
        test_name='bump_version.1',
        test_func=bump_version,
        test_args=('1.2.2', ),
        exp_result='1.2.3'
    )

# Generated at 2022-06-13 20:48:21.696781
# Unit test for function bump_version
def test_bump_version():
    """Test :func:`bump_version` function."""
    from pprint import pprint
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:48:33.937684
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

# Generated at 2022-06-13 20:48:46.545572
# Unit test for function bump_version
def test_bump_version():
    """Unit test for bump_version."""
    import pytest
    from flutils.packages import bump_version
    from flutils.packages import _BUMP_VERSION_PATCH_BETA


# Generated at 2022-06-13 20:48:56.136390
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=E1120
    from unittest import TestCase

    # Testing function:
    class Test_bump_version(TestCase):
        def test_bump_version(self):
            # Test 1: the normal case
            ver_obj = StrictVersion(bump_version('1.2.2'))
            self.assertEqual(ver_obj.version, (1, 2, 3))
            self.assertEqual(ver_obj.prerelease, None)
            # Test 2: bump only the minor part
            ver_obj = StrictVersion(bump_version('1.2.2', position=1))
            self.assertEqual(ver_obj.version, (1, 3, 0))
            self.assertEqual(ver_obj.prerelease, None)
            # Test 3

# Generated at 2022-06-13 20:49:08.018700
# Unit test for function bump_version
def test_bump_version():
    # noinspection PyUnusedLocal
    """Unit test for function bump_version"""
    import unittest

    class TestBumpVersion(unittest.TestCase):
        def setUp(self) -> None:
            self._ver = '2012.06.05'
            self._base = _build_version_info(self._ver)

        def test_build_version_info(self):
            self.assertEqual(
                self._base.version, self._ver)
            self.assertEqual(
                self._base.major.pos, 0)
            self.assertEqual(
                self._base.major.num, 2012)
            self.assertEqual(
                self._base.major.txt, '2012')
            self.assertEqual(
                self._base.major.pre_txt, '')


# Generated at 2022-06-13 20:49:19.106583
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

# Generated at 2022-06-13 20:49:36.208453
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2') == '1.3'
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.2.3', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:45.423262
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for :func:`~.bump_version`.
    """
    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:49:55.549483
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:50:09.311512
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    # pylint: disable=E0602
    # pylint: disable=W0621
    from pprint import pprint

    def _test(
            version: str,
            position: int,
            pre_release: Optional[str],
            expected_out: str
    ) -> None:
        got_out = bump_version(version, position, pre_release)
        print('({}), ({}), ({}), Got: {}, Expected: {}'.format(
            version, position, pre_release, got_out, expected_out
        ))
        assert got_out == expected_out

    print('***** Bump Version *****')

    print('(Version)')
    _test('1.2.2', 2, None, '1.2.3')

# Generated at 2022-06-13 20:50:20.930423
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from pprint import pformat

    def test_it(
            version: str,
            position: int,
            pre_release: Optional[str],
            expect: str
    ) -> None:
        """Test bump_version with given args."""
        res = bump_version(version, position, pre_release)
        res = pformat(res)
        expect = pformat(expect)
        assert res == expect, '%r != %r' % (res, expect)

    test_it('1.2.3', pre_release='a', expect='1.2.4a0', position=2)
    test_it('1.2.4a0', pre_release='a', expect='1.2.4a1', position=2)

# Generated at 2022-06-13 20:50:26.975366
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version
    """
    import pytest
    from flutils.packages import bump_version
    #
    # def test_bump_version_verify_prerelease():
    #     assert False


# Generated at 2022-06-13 20:50:33.528853
# Unit test for function bump_version
def test_bump_version():
    """Run unit tests for function bump_version."""
    from flutils.packages import bump_version

    # pylint: disable=E1136
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:50:40.656246
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0201,W0613
    """Unit test for function bump_version."""
    # pylint: disable=E1101
    import unittest
    import sys

    class TestBumpVersion(unittest.TestCase):

        def make_test_case(self, version: str, position: int,
                           pre_release: str, expected: str):
            self.sub_test_count += 1
            test_name = 'test_%s' % self.sub_test_count
            setattr(self, test_name, self._make_test(version, position,
                                                     pre_release, expected))


# Generated at 2022-06-13 20:50:50.986233
# Unit test for function bump_version
def test_bump_version():

    # Test for function bump_version
    print("Test function: bump_version")

    # ---------------------------
    # Test bump_version() errors
    # ---------------------------

    # Test bump_version() error: position
    print("Test bump_version() error: position")
    try:
        bump_version('1.2.3', position=3)
    except ValueError as err:
        print(err)

    # Test bump_version() error: prerelease
    print("Test bump_version() error: prerelease")
    try:
        bump_version('1.2.3', pre_release='c')
    except ValueError as err:
        print(err)

    # Test bump_version() error: prerelease
    print("Test bump_version() error: prerelease")

# Generated at 2022-06-13 20:51:04.112643
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for function ``bump_version``."""

# Generated at 2022-06-13 20:51:18.759749
# Unit test for function bump_version
def test_bump_version():
    """Tests for ``bump_version``."""
    import sys

    import pytest

    from flutils.packages import bump_version

    from . import common as uc  # Unit common

    if sys.version_info.major < 3:
        pytest.skip('Requires Python 3.x or later.')

    # No tests are needed for python version < 3.5, because the same
    # code is used in the 'else' statement.
    if uc.get_python_major_minor() < (3, 5):
        pytest.skip('Requires Python 3.5 or later.')

    #
    # Setup
    #
    # Bump version tests

# Generated at 2022-06-13 20:51:28.882685
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0915,C0103
    """Unit test for function bump_version."""
    from flutils.packages import bump_version
    try:
        bump_version('1.2.2')
    except ValueError:
        raise AssertionError()
    try:
        bump_version('1.2.3', position=1)
    except ValueError:
        raise AssertionError()
    try:
        bump_version('1.3.4', position=0)
    except ValueError:
        raise AssertionError()
    try:
        bump_version('1.2.3', prerelease='a')
    except ValueError:
        raise AssertionError()

# Generated at 2022-06-13 20:51:36.957071
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version

    :return: None
    """
    # pylint: disable=W0212
    from flutils._testutils import TestBase
    from flutils.packages import bump_version, _build_version_info, \
        _build_version_bump_position, _build_version_bump_type

    class TestBumpVersion(TestBase):
        """Test for function bump_version

        :return: None
        """

        def test_build_version_info(self):
            """Test _build_version_info().

            :return: None
            """

# Generated at 2022-06-13 20:51:42.860707
# Unit test for function bump_version
def test_bump_version():
    from pprint import pformat
    count: int = 0

# Generated at 2022-06-13 20:51:54.628963
# Unit test for function bump_version
def test_bump_version():

    # noinspection PyUnusedLocal
    # pylint: disable=W0612
    def check_bump(version: str, expected: str) -> None:
        actual = bump_version(version)
        assert actual == expected

    def check_bump_pos(version: str, position:
                       int, expected: str) -> None:
        actual = bump_version(version, position=position)
        assert actual == expected

    def check_bump_pre(version: str, prerelease: str,
                       expected: str) -> None:
        actual = bump_version(version, pre_release=prerelease)
        assert actual == expected


# Generated at 2022-06-13 20:52:04.519094
# Unit test for function bump_version
def test_bump_version():
    import pytest

# Generated at 2022-06-13 20:52:18.391673
# Unit test for function bump_version
def test_bump_version():
    import hypothesis
    import pytest

    @hypothesis.given(hypothesis.strategies.text())
    def test_no_args(txt):
        with pytest.raises(ValueError):
            bump_version(txt)
    test_no_args()

    @hypothesis.given(hypothesis.strategies.text(), hypothesis.strategies.integers())
    def test_position(txt, pos):
        with pytest.raises(ValueError):
            bump_version(txt, position=pos)
    test_position()


# Generated at 2022-06-13 20:52:32.148293
# Unit test for function bump_version
def test_bump_version():
    import unittest

    class TestBumpVersion(unittest.TestCase):
        def test_bump(self):
            self.assertEqual(bump_version('1.2.2'), '1.2.3')
            self.assertEqual(bump_version('1.2.3', position=1), '1.3')
            self.assertEqual(bump_version('1.3.4', position=0), '2.0')
            self.assertEqual(bump_version('1.2.3', prerelease='a'), '1.2.4a0')
            self.assertEqual(bump_version('1.2.4a0', pre_release='a'), '1.2.4a1')

# Generated at 2022-06-13 20:52:36.173206
# Unit test for function bump_version
def test_bump_version():
    import unittest  # pylint: disable=E0401
    return unittest.FunctionTestCase(bump_version)

# Generated at 2022-06-13 20:52:45.612506
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for function bump_version
    """
    from flutils.packages import bump_version as func_bump_version
    #
    #
    #
    def _test_it(ver: str, position: int, pre_release: Optional[str]) -> str:
        out = func_bump_version(ver, position, pre_release)
        return out
    #
    #
    #
    assert _test_it('1.2.2', position=2, pre_release=None) == '1.2.3'
    assert _test_it('1.2.3', position=1, pre_release=None) == '1.3'
    assert _test_it('1.3.4', position=0, pre_release=None) == '2.0'
    assert _test_it

# Generated at 2022-06-13 20:53:01.078697
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version
    """

    def _build_test_case_bump_version(
            args: Tuple[str, str],
            expected: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ):
        actual = bump_version(*args, position=position, pre_release=pre_release)
        if actual != expected:
            raise AssertionError(
                'Failed to bump version: %r\n'
                '    args: %r\n'
                '    expected: %r\n'
                '    actual: %r' % (args, (position, pre_release), expected,
                                   actual)
            )


# Generated at 2022-06-13 20:53:08.999613
# Unit test for function bump_version
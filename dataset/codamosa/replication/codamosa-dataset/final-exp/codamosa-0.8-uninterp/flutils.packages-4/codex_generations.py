

# Generated at 2022-06-13 20:43:29.334072
# Unit test for function bump_version
def test_bump_version():
    """Test the function bump_version"""
    def tfunc(version, position, pre_release, assert_value):
        """Test the function bump_version"""
        out = bump_version(version, position, pre_release)
        print(out)
        assert out == assert_value

    tfunc('0.2.0', pre_release='a', assert_value='0.2.0a0')
    tfunc('1.2.0', pre_release='b', assert_value='1.2.0b0')
    tfunc('2.2.0a1', pre_release='a', assert_value='2.2.0a2')
    tfunc('2.2.0b1', pre_release='b', assert_value='2.2.0b2')

# Generated at 2022-06-13 20:43:41.330004
# Unit test for function bump_version
def test_bump_version():
    version = bump_version('1.2.2')
    assert version == '1.2.3'
    version = bump_version('1.2.3', position=1)
    assert version == '1.3'
    version = bump_version('1.3.4', position=0)
    assert version == '2.0'
    version = bump_version('1.2.3', pre_release='a')
    assert version == '1.2.4a0'
    version = bump_version('1.2.4a0', pre_release='a')
    assert version == '1.2.4a1'
    version = bump_version('1.2.4a1', pre_release='b')
    assert version == '1.2.4b0'

# Generated at 2022-06-13 20:43:53.058942
# Unit test for function bump_version
def test_bump_version():
    """Unit test for bump_version()."""
    # pylint: disable=missing-docstring
    def _test_bump_version(version, position, pre_release, out):
        """Cache function for testing bump_version."""
        ret = bump_version(version, position, pre_release)
        assert ret == out
    # pylint: enable=missing-docstring

    _test_bump_version('1.2.2', 2, None, '1.2.3')
    _test_bump_version('1.2.3', 1, None, '1.3')
    _test_bump_version('1.3.4', 0, None, '2.0')
    _test_bump_version('1.2.3', 0, 'alpha', '1.2.4a0')

# Generated at 2022-06-13 20:43:58.497164
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0912,R0915
    """Function: bump_version"""
    import unittest

    class TestCase(unittest.TestCase):
        def test_zero(self):
            with self.assertRaises(ValueError):
                bump_version('1.2.3', position=-4)

        def test_one(self):
            with self.assertRaises(ValueError):
                bump_version('1.2.3', position=3)

        def test_two(self):
            with self.assertRaises(ValueError):
                bump_version('1.2.3', pre_release='c')

        def test_three(self):
            with self.assertRaises(ValueError):
                bump_version('1.2.3', position=0, pre_release='a')



# Generated at 2022-06-13 20:44:03.407245
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:14.435178
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.packages import bump_version

    # noinspection PyUnusedLocal

# Generated at 2022-06-13 20:44:24.791957
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:44:35.345437
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version."""
    code = '''
    bump_version('1.2.2')
    '''
    assert eval(code) == '1.2.3'

    code = '''
    bump_version('1.2.3', position=1)
    '''
    assert eval(code) == '1.3'

    code = '''
    bump_version('1.3.4', position=0)
    '''
    assert eval(code) == '2.0'

    code = '''
    bump_version('1.2.3', prerelease='a')
    '''
    assert eval(code) == '1.2.4a0'

    code = '''
    bump_version('1.2.4a0', pre_release='a')
    '''


# Generated at 2022-06-13 20:44:46.596410
# Unit test for function bump_version

# Generated at 2022-06-13 20:44:51.527091
# Unit test for function bump_version
def test_bump_version():
    """Run unit tests for the :func:`bump_version` function."""
    import unittest
    # noinspection PyUnresolvedReferences
    import tests.test_packages

    suite = unittest.TestSuite()
    suite.addTest(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            tests.test_packages.TestBumpVersion
        )
    )
    runner = unittest.TextTestRunner()
    runner.run(suite)


# Generated at 2022-06-13 20:45:16.399683
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:45:29.183786
# Unit test for function bump_version
def test_bump_version():
    """
    Test function bump_version
    """
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', prerelease='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', prerelease='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:45:36.495879
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=W0613
    import pytest

    version = '1.2.3'

    # Basic tests
    assert bump_version(version, position=0) == '2.0'
    assert bump_version(version, position=1) == '1.3'
    assert bump_version(version, position=2) == '1.2.4'
    assert bump_version(version, position=3) == '1.2.4'

    # Test pre-release version bumps
    version = '1.2.3'
    assert bump_version(version, pre_release='a') == '1.2.4a0'
    assert bump_version(version, pre_release='b') == '1.2.4b0'
    version = '1.2.3a0'
    assert bump_

# Generated at 2022-06-13 20:45:48.586941
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

    ver = bump_version('1.2.2')
    assert ver == '1.2.3', 'version string increased incorrectly.'

    ver = bump_version('1.2.3', position=1)
    assert ver == '1.3', 'version string increased incorrectly.'

    ver = bump_version('1.3.4', position=0)
    assert ver == '2.0', 'version string increased incorrectly.'

    ver = bump_version('1.2.3', pre_release='a')
    assert ver == '1.2.4a0', 'version string increased incorrectly.'

    ver = bump_version('1.2.4a0', pre_release='a')
    assert ver == '1.2.4a1', 'version string increased incorrectly.'

    ver = bump_

# Generated at 2022-06-13 20:45:56.444763
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:07.207450
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for function bump_version
    """
    import sys

    testing = (__name__ == '__main__')

    if testing:
        import flutils.packages
        flutils.packages.bump_version = bump_version

        sys.argv.append('-v')
        sys.argv.append('-r')

    import unittest
    import doctest
    import flutils.packages as pack

    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(pack))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:46:20.360638
# Unit test for function bump_version
def test_bump_version():
    """Setup an utils.packages.bump_version unit test.

    *New in version 0.3*

    Raises:
        AssertionError: if the unit test fails.

    """

# Generated at 2022-06-13 20:46:32.664132
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version
    """
    print("Testing function bump_version")

# Generated at 2022-06-13 20:46:46.445645
# Unit test for function bump_version
def test_bump_version():
    import unittest

    with unittest.TestCase() as test:
        # Ensure that bump_version is a function
        assert test.assertTrue(
            callable(bump_version),
            "bump_version is not a function."
        )

        # Test bumping the major version number
        assert test.assertEqual(
            bump_version('1.2.1', position=0),
            '2.0',
            "bump_version('1.2.1', position=0) returned: %r" %
            bump_version('1.2.1', position=0)
        )

        # Test bumping the major version number without a patch release

# Generated at 2022-06-13 20:46:58.902941
# Unit test for function bump_version
def test_bump_version():
    # Testing bump_version
    expected = '1.2.3'
    result = bump_version('1.2.2')
    assert result == expected

    expected = '1.3'
    result = bump_version('1.2.3', position=1)
    assert result == expected

    expected = '2.0'
    result = bump_version('1.3.4', position=0)
    assert result == expected

    expected = '1.2.4a0'
    result = bump_version('1.2.3', prerelease='a')
    assert result == expected

    expected = '1.2.4a1'
    result = bump_version('1.2.4a0', pre_release='a')
    assert result == expected

    expected = '1.2.4b0'

# Generated at 2022-06-13 20:47:16.679955
# Unit test for function bump_version
def test_bump_version():
    ver = '1.2.2'
    assert bump_version(ver) == '1.2.3'
    assert bump_version(ver, position=1) == '1.3'
    assert bump_version(ver, position=0) == '2.0'
    assert bump_version(ver, prerelease='a') == '1.2.4a0'
    ver = '1.2.4a0'
    assert bump_version(ver, pre_release='a') == '1.2.4a1'
    ver = '1.2.4a1'
    assert bump_version(ver, pre_release='b') == '1.2.4b0'
    assert bump_version(ver) == '1.2.4'
    ver = '1.2.4b0'
    assert bump

# Generated at 2022-06-13 20:47:24.977634
# Unit test for function bump_version
def test_bump_version():
    # Major number
    result = bump_version('0.1.0')
    assert result == '1.0'
    result = bump_version('1.2.0')
    assert result == '2.0'
    result = bump_version('1.2.3')
    assert result == '2.0'
    # Minor number
    result = bump_version('1.0.0')
    assert result == '1.1'
    result = bump_version('1.2.0')
    assert result == '1.3'
    result = bump_version('1.2.3')
    assert result == '1.3'
    # Patch number
    result = bump_version('1.0.0')
    assert result == '1.0.1'
    result = bump_version('1.0.3')


# Generated at 2022-06-13 20:47:39.830514
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    """Test function bump_version."""
    # pylint: disable=R0914
    from textwrap import dedent

    def clean(txt: str) -> str:
        txt = txt.rstrip()
        return dedent(txt).lstrip()

    # Major
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.3', position=0) == '2.0'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.2.3', position=2) == '1.2.4'

    # Minor alpha

# Generated at 2022-06-13 20:47:50.641629
# Unit test for function bump_version
def test_bump_version():
    """Xtreme basic unit test for the function :func:`bump_version`."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:47:59.950259
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=missing-docstring
    def run_test(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ) -> None:
        out = bump_version(version, position, pre_release)
        print('%r -> %r' % (version, out))

    run_test('1.2.2')
    run_test('1.2.3', position=1)
    run_test('1.3.4', position=0)
    run_test('1.2.3', prerelease='a')
    run_test('1.2.4a0', pre_release='a')
    run_test('1.2.4a1', pre_release='b')
    run_test('1.2.4a1')


# Generated at 2022-06-13 20:48:06.395501
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    from flutils.packages import bump_version



# Generated at 2022-06-13 20:48:19.778321
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    if bump_version('1.2.2') == '1.2.3':
        print('kern test 1 passed')
    else:
        print('kern test 1 failed')

    if bump_version('1.2.3', position=1) == '1.3':
        print('kern test 2 passed')
    else:
        print('kern test 2 failed')

    if bump_version('1.3.4', position=0) == '2.0':
        print('kern test 3 passed')
    else:
        print('kern test 3 failed')

    if bump_version('1.2.3', prerelease='a') == '1.2.4a0':
        print('kern test 4 passed')

# Generated at 2022-06-13 20:48:32.897903
# Unit test for function bump_version
def test_bump_version():

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:46.100738
# Unit test for function bump_version
def test_bump_version():
    from flutils.testhelpers import FunctionTestHelper, InlineTestHelper
    from flutils.packages import bump_version
    helper = FunctionTestHelper(bump_version)
    helper.set_kwargs(position=0)
    helper.add_test_data('1.2.3', '2.0')
    helper.add_test_data('1.2.3', '2.0')
    helper.add_test_data('1.0.0', '2.0')
    helper.add_test_data('1.2.3', '2.0', position=3)
    helper.add_test_data('1.2.3', '2.0', position=-3)
    helper.add_test_data('1.2.3.4', '2.0.0')
    helper.add_test

# Generated at 2022-06-13 20:48:56.051240
# Unit test for function bump_version
def test_bump_version():
    """Test flutils' bump_version function.

    Returns:
        :obj:`bool`

        * ``True`` if the function performs as expected.  ``False`` otherwise.

    """
    from os import environ
    from sys import modules
    from unittest import TestCase, TextTestRunner
    from unittest.mock import Mock, patch, sentinel

    from flutils.packages import bump_version

    class _Test(TestCase):
        def test_bump_version(self):
            with patch.dict(environ, clear=True):
                *_, version = bump_version('1.2.2').split('.')
                self.assertIsInstance(int(version), int)
                self.assertEqual(int(version), 3)


# Generated at 2022-06-13 20:49:14.580820
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version function."""
    from flutils.packages import bump_version


# Generated at 2022-06-13 20:49:27.738744
# Unit test for function bump_version
def test_bump_version():
    from flutils import console
    from . import utils
    from .utils import PY_VER_MAJOR  # pylint: disable=E0611,E0401
    from .utils import PY_VER_MINOR  # pylint: disable=E0611,E0401
    from .utils import PY_VER_MICRO  # pylint: disable=E0611,E0401
    if PY_VER_MAJOR < 3 or (PY_VER_MAJOR == 3 and PY_VER_MINOR < 8):
        console.info(
            '\nNotice: Unit testing of %s is disabled because of lack of '
            '"importlib.metadata" library.',
            __name__
        )
        return


# Generated at 2022-06-13 20:49:35.589293
# Unit test for function bump_version
def test_bump_version():
    """Test ``bump_version``."""
    from flutils.packages import bump_version

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


# Make sure this module can be loaded

# Generated at 2022-06-13 20:49:45.142173
# Unit test for function bump_version
def test_bump_version():  # noqa
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:55.522086
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=R0201
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:50:09.310151
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for the `bump_version` function."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump

# Generated at 2022-06-13 20:50:20.930734
# Unit test for function bump_version
def test_bump_version():
    from sys import version_info
    from io import StringIO
    def run_test(
            ver: str,
            pos: Optional[int] = None,
            pre: Optional[str] = None,
            out: Optional[str] = None
    ) -> None:
        if out is None:
            out = ver
        else:
            out = str(out)
        if pos is None and pre is None:
            func = bump_version
            args = [ver]
            kwargs = {}
        elif pre is None:
            func = bump_version
            args = [ver]
            kwargs = {
                'position': pos
            }
        elif pos is None:
            func = bump_version
            args = [ver]
            kwargs = {
                'pre_release': pre
            }

# Generated at 2022-06-13 20:50:29.997088
# Unit test for function bump_version
def test_bump_version():
    """ Test bump_version function """
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:50:39.130034
# Unit test for function bump_version
def test_bump_version():

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:50:54.464511
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for function bump_version."""

# Generated at 2022-06-13 20:51:16.879888
# Unit test for function bump_version
def test_bump_version():
    """Test the function ``bump_version``."""
    from copy import copy
    from os.path import dirname, join
    from textwrap import dedent
    from unittest import mock
    from unittest.mock import Mock

    from . import _io
    from . import _parsers
    from .packages import bump_version

    opj = join

    globs = globals()
    for name in globs:
        if not name.startswith('_BUMP_VERSION_'):
            continue
        if name == '_BUMP_VERSION_POSITION_NAMES':
            continue
        globs[name] = mock.Mock()

    _io.get_read_text_results = Mock(return_value=dedent("""
        nums = 1, 2, 3
    """).strip())


# Generated at 2022-06-13 20:51:28.210827
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

# Generated at 2022-06-13 20:51:40.493574
# Unit test for function bump_version

# Generated at 2022-06-13 20:51:53.927555
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

# Generated at 2022-06-13 20:52:04.125296
# Unit test for function bump_version
def test_bump_version():
    r"""Test for flutil.packages.bump_version."""
    # -------------------------------------------------------------------------
    # noinspection PyUnresolvedReferences,PyPackageRequirements
    import flutils.packages
    # noinspection PyProtectedMember
    bump_version = flutils.packages._bump_version

    # -------------------------------------------------------------------------
    # Test - Returns a value
    # -------------------------------------------------------------------------
    # Test - Returns values
    assert bump_version(version='1.2.2') == '1.2.3'
    assert bump_version(version='1.2.3', position=1) == '1.3'
    assert bump_version(version='1.3.4', position=0) == '2.0'
    assert bump_version(version='1.2.3', pre_release='a') == '1.2.4a0'
   

# Generated at 2022-06-13 20:52:18.319382
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function ``bump_version``."""

    import unittest

    class TestBumpVersion(unittest.TestCase):
        """Test class for ``bump_version``."""

        def setUp(self):
            """Test set up."""
            self.ver_info = _build_version_info
            self.build_pos = _build_version_bump_position
            self.bump_type = _build_version_bump_type
            self.each_part = _each_version_part
            self.ver_obj = StrictVersion
            self.bump = bump_version

        def test_each_version_part(self):
            """Test ``_each_version_part``."""
            ver_obj = self.ver_obj('2.2.5a5')
            parts

# Generated at 2022-06-13 20:52:32.108821
# Unit test for function bump_version
def test_bump_version():
    import pytest


# Generated at 2022-06-13 20:52:45.870284
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    import pytest

# Generated at 2022-06-13 20:52:59.044513
# Unit test for function bump_version
def test_bump_version():
    """Flutils _packages_: Test function "bump_version"."""
    from flutils.packages import bump_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:53:07.898478
# Unit test for function bump_version
def test_bump_version():

    class _Version(NamedTuple):
        version: str
        position: int
        pre_release: str
        expected: str

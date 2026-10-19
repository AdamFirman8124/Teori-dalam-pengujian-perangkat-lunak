

# Generated at 2022-06-13 20:43:29.589376
# Unit test for function bump_version
def test_bump_version():
    if __debug__:
        assert bump_version('1.2.2') == '1.2.3'
        assert bump_version('1.2.3', position=1) == '1.3'
        assert bump_version('1.3.4', position=0) == '2.0'
        assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
        assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
        assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
        assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:43:41.493490
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=R0914

    # Test no-arguments
    raise NotImplementedError()

    # Test valid version positions
    for pos in range(3):
        out = bump_version('1.2.3', position=pos)
        assert out == '1.2.4'

    # Test valid version pre-release positions
    for pos in range(1, 2):
        out = bump_version('1.2.3', position=pos, pre_release='a')
        assert out == '1.3a0'

    # Test invalid position
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=-3)

    with pytest.raises(ValueError):
        bump_version('1.2.3', position=3)

    # Test valid pre

# Generated at 2022-06-13 20:43:53.189470
# Unit test for function bump_version
def test_bump_version():
    """Test function bump_version.

    """
    import unittest

    class TestFunc(unittest.TestCase):

        def test_version_bump_position(self):
            """Test function _build_version_bump_position.

            """
            from flutils.packages import _build_version_bump_position
            self.assertEqual(_build_version_bump_position(0), 0)
            self.assertEqual(_build_version_bump_position(-1), 1)
            self.assertEqual(_build_version_bump_position(-2), 2)

            with self.assertRaises(ValueError):
                _build_version_bump_position(-3)
            with self.assertRaises(ValueError):
                _build_version_bump_position(3)


# Generated at 2022-06-13 20:44:00.475862
# Unit test for function bump_version
def test_bump_version():
    # Test for VersionInfo
    assert _VersionInfo(
        '1.2.3',
        _VersionPart(pos=0, txt='1', num=1, pre_txt='', pre_num=-1, name='major'),
        _VersionPart(pos=1, txt='2', num=2, pre_txt='', pre_num=-1, name='minor'),
        _VersionPart(pos=2, txt='3', num=3, pre_txt='', pre_num=-1, name='patch'),
        pre_pos=-1
    ) == _build_version_info('1.2.3')
    # Test for StrictVersion.version, prerelease, and .parse_version
    ver_obj = StrictVersion('1.2.3')

# Generated at 2022-06-13 20:44:12.677934
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version"""
    # pylint: disable=R0914
    # pylint: disable=C0116
    from doctest import testmod
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b')

# Generated at 2022-06-13 20:44:24.409456
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    versions = [
        '1.2.2',
        '1.2.3',
        '1.2.3',
        '1.2.3',
        '1.2.3',
        '1.2.3',
        '1.2.3',
        '1.2.3',
        '1.2.3',
        '1.2.3',
        '1.2.3',
        '1.2.3',
        '1.2.3',
        '1.2.4',
        '1.2.4',
    ]
    for num, version in enumerate(versions):
        if num == 0:
            assert bump_version(version) == '1.2.3'
        elif num == 1:
            assert bump_version

# Generated at 2022-06-13 20:44:35.058096
# Unit test for function bump_version
def test_bump_version():
    from . import _callf_
    from .common import _bump_versions_tests  # pylint: disable=E0611,E0401

    failed = False
    if _callf_('bump_version', '1.2.3', None, None) != '1.2.3':
        print(
            "bump_version('1.2.3', None, None) did not return "
            "'1.2.3' as expected."
        )
        failed = True

    if _callf_('bump_version', '1.2.3', 1, None) != '1.3':
        print(
            "bump_version('1.2.3', 1, None) did not return "
            "'1.3' as expected."
        )
        failed = True


# Generated at 2022-06-13 20:44:46.373318
# Unit test for function bump_version
def test_bump_version():  # noqa: D103
    import unittest
    import Exscript

    class BumpVersionTest(unittest.TestCase):
        def test_add(self):
            ver = '1.2.3'
            new = bump_version(ver, position=0)
            expected = '2.0'
            self.assertEqual(new, expected)
            new = bump_version(ver, position=1)
            expected = '1.3'
            self.assertEqual(new, expected)
            new = bump_version(ver, position=2)
            expected = '1.2.4'
            self.assertEqual(new, expected)
            new = bump_version(ver, position=-3)
            expected = '2.0'
            self.assertEqual(new, expected)
            new = bump

# Generated at 2022-06-13 20:44:53.469866
# Unit test for function bump_version
def test_bump_version():
    """Unit testing for function ``bump_version``."""
    from unittest import TestCase, main


    class BumpVersionTestCase(TestCase):
        """Test the ``bump_version`` function."""

        def test_bump_version_1(self):
            """Test :func:`flutils.packages.bump_version` - 1"""
            self.assertEqual(
                bump_version('1.2.1'),
                '1.2.2'
            )

        def test_bump_version_2(self):
            """Test :func:`flutils.packages.bump_version` - 2"""
            self.assertEqual(
                bump_version('1.2.1', position=1),
                '1.3'
            )


# Generated at 2022-06-13 20:45:04.512703
# Unit test for function bump_version
def test_bump_version():
    major_test_cases = {
        '1.2.3': '2.0',
        '1.3.4a0': '2.0',
        '1.2.4a1': '2.0',
        '1.2.4b0': '2.0',
    }
    minor_test_cases = {
        '1.2.3': '1.3',
        '1.2.4a1': '1.3',
        '1.2.4b0': '1.3',
        '2.1.3': '2.2',
    }

# Generated at 2022-06-13 20:45:31.445498
# Unit test for function bump_version
def test_bump_version():
    """Test function ``bump_version``.

    """
    import flutils.packages
    #
    # General
    #
    func = flutils.packages.bump_version
    ver = '1.2.3'
    assert func(ver) == '1.2.4'
    #
    # Position
    #
    ver = '1.2.3'
    assert func(ver, position=0) == '2.0'
    ver = '1.2.3'
    assert func(ver, position=1) == '1.3'
    ver = '1.2.3'
    assert func(ver, position=2) == '1.2.4'
    #
    # Pre-release
    #
    ver = '1.2.3'

# Generated at 2022-06-13 20:45:44.488515
# Unit test for function bump_version
def test_bump_version():
    print(bump_version('1.2.2'))
    print(bump_version('1.2.3', position=1))
    print(bump_version('1.3.4', position=0))
    print(bump_version('1.2.3', prerelease='a'))
    print(bump_version('1.2.4a0', pre_release='a'))
    print(bump_version('1.2.4a1', pre_release='b'))
    print(bump_version('1.2.4a1'))
    print(bump_version('1.2.4b0'))
    print(bump_version('2.1.3', position=1, pre_release='a'))

# Generated at 2022-06-13 20:45:54.509537
# Unit test for function bump_version

# Generated at 2022-06-13 20:46:06.551233
# Unit test for function bump_version
def test_bump_version():  # noqa: D103
    from unittest import TestCase
    from .tests_utils import print_test_result

    class TestBumpVersion(TestCase):

        def test_bump_version(self):  # noqa: D102
            out = bump_version('1.2.2')
            self.assertEqual(out, '1.2.3')

        def test_bump_version_minor(self):  # noqa: D102
            out = bump_version('1.2.3', position=1)
            self.assertEqual(out, '1.3')

        def test_bump_version_major(self):  # noqa: D102
            out = bump_version('1.3.4', position=0)
            self.assertEqual(out, '2.0')



# Generated at 2022-06-13 20:46:19.998066
# Unit test for function bump_version
def test_bump_version():
    """Unit test for module function, bump_version."""
    # pylint: disable=C0111
    # pylint: disable=R0912
    # pylint: disable=R0915
    v = '1.2.2'
    assert bump_version(v) == '1.2.3'
    assert bump_version(v, position=1) == '1.3'
    assert bump_version(v, position=0) == '2.0'
    assert bump_version(v, pre_release='a') == '1.2.4a0'
    assert bump_version(v, pre_release='A') == '1.2.4a0'
    assert bump_version(v, pre_release='ALPHA') == '1.2.4a0'

# Generated at 2022-06-13 20:46:25.457310
# Unit test for function bump_version
def test_bump_version():
    """Test of bump_version."""

# Generated at 2022-06-13 20:46:31.673745
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=W0613,W0612,R0201,R0913
    """Unit test for function bump_version."""
    from flutils.packages import bump_version

    main()


if __name__ == "__main__":
    main(as_module=True)

# Generated at 2022-06-13 20:46:45.770518
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:46:58.341540
# Unit test for function bump_version
def test_bump_version():
    """Test that flutils.packages.bump_version() passes all examples."""
    from flutils.packages import bump_version
    from flutils.tests.flutils_testlib import Example  # type: ignore

    examples: List[Example] = []
    for ver in ('1', '2'):
        for pos in (0, 1, 2):
            for prem in ('a', 'alpha', 'b', 'beta'):
                inp = '{}.0.0'.format(ver)
                exp = '{}.0.1{}0'.format(ver, prem)
                desc = '{}bump_version({}, position={}, pre_release={})'.format(
                    repr(exp), repr(inp), repr(pos), repr(prem)
                )
                examples.append(Example(inp, exp, desc))

# Generated at 2022-06-13 20:47:10.985947
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""
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
   

# Generated at 2022-06-13 20:47:37.214641
# Unit test for function bump_version
def test_bump_version(): # pylint: disable=R0914
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print("")
        print("All tests passed!")
    else:
        print("")
        print("Failed to pass {0} tests.".format(count))


if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:47:48.126469
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:47:58.620627
# Unit test for function bump_version
def test_bump_version():
    """
    Unit test for function `bump_version`.

    Raises:
        AssertionError: if any of the tests fails

    """
    from flutils.formats import format_version

    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'

# Generated at 2022-06-13 20:48:10.443910
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:13.049134
# Unit test for function bump_version
def test_bump_version():
    pass


if __name__ == '__main__':
    test_bump_version()

# Generated at 2022-06-13 20:48:22.904378
# Unit test for function bump_version
def test_bump_version():
    import sys
    import pytest
    from flutils.packages import bump_version

    def _test(
            version: str,
            position: int = 2,
            pre_release: Union[str, None] = None
    ) -> str:
        version = version.strip()
        pre_release = pre_release.strip() if pre_release else pre_release
        return bump_version(version=version, position=position,
                            pre_release=pre_release)


# Generated at 2022-06-13 20:48:34.254402
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0201
    """Test the function ``bump_version``."""


# Generated at 2022-06-13 20:48:46.575514
# Unit test for function bump_version
def test_bump_version():
    """Test the function."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:48:56.179702
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:49:01.308536
# Unit test for function bump_version
def test_bump_version():
    """Test the function: :func:`bump_version`."""
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
   

# Generated at 2022-06-13 20:49:28.672944
# Unit test for function bump_version
def test_bump_version():
    # pylint: disable=C0116
    # pylint: disable=C0103
    def test_bump_version_pos_prerelease(v, pos, prerelease):
        v = bump_version(v, pre_release=prerelease, position=pos)
        if pos == 0:
            if prerelease == 'a':
                assert v == '2a0'
            else:
                assert v == '2b0'
        if pos == 1:
            if prerelease == 'a':
                assert v == '1.2a0'
            else:
                assert v == '1.2b0'
        if pos == 2:
            if prerelease == 'a':
                assert v == '1.1.2a0'
            else:
                assert v == '1.1.2b0'



# Generated at 2022-06-13 20:49:34.688187
# Unit test for function bump_version
def test_bump_version():
    """Run test for function 'bump_version'."""
    from .helpers import Testable
    from .helpers import TestRunner
    from .helpers import TestSamples

    def _get_output(sample: Dict[str, Any]):
        position = sample.get('position', 2)
        pre_release = sample.get('pre_release', None)
        return bump_version(sample['input'], position, pre_release)

    testable = Testable(target=_get_output)
    test_runner = TestRunner(testable, samples=TestSamples.bump_version)
    test_runner.run()

# Generated at 2022-06-13 20:49:43.620518
# Unit test for function bump_version
def test_bump_version():
    # Test a normal bump
    ver_txt = '1.0.0'
    ver_exp_txt = '1.0.1'
    ver_new_txt = bump_version(ver_txt)
    assert ver_new_txt == ver_exp_txt, \
        "Bump version incorrectly returned: %s" % ver_new_txt

    # Test bumping a minor part
    ver_txt = '1.2.0'
    ver_exp_txt = '1.3'
    ver_new_txt = bump_version(ver_txt, position=1)
    assert ver_new_txt == ver_exp_txt, \
        "Bump version incorrectly returned: %s" % ver_new_txt

    # Test bumping a major part
    ver_txt = '1.2.0'
    ver_

# Generated at 2022-06-13 20:49:54.861240
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    assert bump_version(version='1.2.2') == '1.2.3'
    assert bump_version(version='1.2.3', position=1) == '1.3'
    assert bump_version(version='1.3.4', position=0) == '2.0'
    assert bump_version(version='1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version(version='1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version(version='1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:50:08.559777
# Unit test for function bump_version
def test_bump_version():
    """Test the bump_version function for expected results.

    """
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump

# Generated at 2022-06-13 20:50:20.412951
# Unit test for function bump_version
def test_bump_version():
    """Tests of the `flutils.packages.bump_version` function.
    """
    # noinspection PyUnresolvedReferences
    from flutils.packages import bump_version

    def test(orig: str, expected: str,
             pos: int = 2, pre: Optional[str] = None):
        """Asserts that the given version returns the expected version.

        Args:
            orig (str): The original version.
            expected (str): The expected bump version.
            pos (int, optional): The bump position.  Defaults to: ``2``
            pre (str, optional): The bump pre-release.  Defaults to: ``None``

        Raises:
            AssertionError: if the bump version is not the same as the
                expected version.

        """

# Generated at 2022-06-13 20:50:29.797329
# Unit test for function bump_version
def test_bump_version():
    # Testing pylint: disable=E1120
    def _test_bump_version_bad_type(version, position, pre_release):
        import pytest
        with pytest.raises(TypeError):
            bump_version(version, position, pre_release)

    import sys
    if sys.version_info.major == 2:
        _test_bump_version_bad_type(0, 1, 'a')
        _test_bump_version_bad_type(0, 1, 'b')
        _test_bump_version_bad_type('0.0.0', 0, b'a')
        _test_bump_version_bad_type('0.0.0', 0, b'b')
    # Testing pylint: enable=E1120

# Generated at 2022-06-13 20:50:35.317678
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version"""

    # Example test data

# Generated at 2022-06-13 20:50:48.418445
# Unit test for function bump_version
def test_bump_version():
    def _run_test(
            version: str,
            position: int = 2,
            pre_release: Optional[str] = None
    ) -> None:
        output = bump_version(
            version=version,
            position=position,
            pre_release=pre_release
        )
        print('%s -> %s' % (version, output))

    _run_test('1.2.2')
    _run_test('1.2.3', position=1)
    _run_test('1.3.4', position=0)
    _run_test('1.2.3', pre_release='a')
    _run_test('1.2.4a0', pre_release='a')
    _run_test('1.2.4a1', pre_release='b')
    _run

# Generated at 2022-06-13 20:51:01.967762
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

# Generated at 2022-06-13 20:51:20.119172
# Unit test for function bump_version
def test_bump_version():
    """
    Run the unit tests for bump_version.

    Raises:
        None

    Returns:
        None

    """
    # pylint: disable=R0915
    cases = []
    cases.append(('1.2.2', _BUMP_VERSION_PATCH, None, '1.2.3'))
    cases.append(('1.2.3', _BUMP_VERSION_MINOR, None, '1.3'))
    cases.append(('1.3.4', _BUMP_VERSION_MAJOR, None, '2.0'))
    cases.append(('1.2.3', _BUMP_VERSION_MINOR_ALPHA, 'a', '1.2.4a0'))

# Generated at 2022-06-13 20:51:30.183662
# Unit test for function bump_version
def test_bump_version():
    """Unit tests for function bump_version"""
    # pylint: disable=R0912
    # pylint: disable=R0914
    # pylint: disable=R0915

    def _vers_info(version: str) -> _VersionInfo:
        return _build_version_info(version)

    def _vers_bump_pos(position: int) -> int:
        return _build_version_bump_position(position)

    def _vers_bump_type(
            position_positive: int,
            pre_release: Optional[str]
    ) -> int:
        return _build_version_bump_type(position_positive, pre_release)

    assert bump_version('1.2.2') == '1.2.3'

# Generated at 2022-06-13 20:51:41.405917
# Unit test for function bump_version
def test_bump_version():
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'

# Generated at 2022-06-13 20:51:54.481918
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    from pprint import pprint

    def fmt_args(args: Dict[str, Any]) -> str:
        arg_pairs = []
        for name, value in args.items():
            if isinstance(value, str):
                value = "'%s'" % value
            elif value is None:
                value = 'None'
            arg_pairs.append('%s=%s' % (name, value))
        return ', '.join(arg_pairs)


# Generated at 2022-06-13 20:52:04.440110
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=W0613
    """Test for bump_version()"""
    from flutils.packages import bump_version
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

# Generated at 2022-06-13 20:52:12.639897
# Unit test for function bump_version
def test_bump_version():
    """Test for function bump_version."""
    pass

    # noinspection PyProtectedMember
    # from flutils.packages import _each_version_part
    # from flutils.packages import _build_version_info
    # from flutils.packages import _build_version_bump_position
    # from flutils.packages import _build_version_bump_type

    # from flutils.packages import bump_version

# Generated at 2022-06-13 20:52:16.876892
# Unit test for function bump_version
def test_bump_version():  # pylint: disable=R0701
    """Test bump_version."""
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS, verbose=False)



# Generated at 2022-06-13 20:52:22.953596
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""

# Generated at 2022-06-13 20:52:33.873712
# Unit test for function bump_version
def test_bump_version():
    """Unit test for bump_version
    """
    assert(bump_version('1.2.2') == '1.2.3')
    assert(bump_version('1.2.3', position=1) == '1.3')
    assert(bump_version('1.3.4', position=0) == '2.0')
    assert(bump_version('1.2.3', prerelease='a') == '1.2.4a0')
    assert(bump_version('1.2.4a0', pre_release='a') == '1.2.4a1')
    assert(bump_version('1.2.4a1', pre_release='b') == '1.2.4b0')

# Generated at 2022-06-13 20:52:46.377516
# Unit test for function bump_version
def test_bump_version():
    """Unit test for function bump_version."""
    fns = (
        ('1.2.3', '1.2.3'),
        ('1.2.3', '1.2.3'),
        ('1.2.3', '1.2.3'),
        ('1.2.3', '1.2.3'),
        ('1.2.3', '1.2.3'),
        ('1.2.3', '1.2.3'),
        ('1.2.3', '1.2.3'),
    )
    def_kwargs = {
        'position': 2,
        'pre_release': None,
    }
    for ver, expt in fns:
        actl = bump_version(ver, **def_kwargs)

# Generated at 2022-06-13 20:53:06.476293
# Unit test for function bump_version
def test_bump_version():
    """Unit test for the ``bump_version`` function."""
    # noinspection PyUnresolvedReferences
    import doctest

    doctest.testmod(verbose=True)


if __name__ == '__main__':
    test_bump_version()
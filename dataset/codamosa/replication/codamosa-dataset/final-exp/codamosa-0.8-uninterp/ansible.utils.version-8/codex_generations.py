

# Generated at 2022-06-13 16:57:37.096461
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    # Make sure that regular versions are parsed correctly
    assert SemanticVersion('1.3.3').core == (1, 3, 3)
    assert SemanticVersion('1.3.3.7').core == (1, 3, 3)
    assert SemanticVersion('1.3.3.7.4.4').core == (1, 3, 3)
    assert SemanticVersion('1.3').core == (1, 3, 0)
    assert SemanticVersion('1.3.0').core == (1, 3, 0)

    # Make sure prerelease versions are parsed correctly
    assert SemanticVersion('1.3.3-beta').prerelease == (_Alpha('beta'),)
    assert SemanticVersion('1.3.3-beta.1').prerelease == (_Alpha('beta'), _Numeric('1'))
    assert SemanticVersion

# Generated at 2022-06-13 16:57:45.620646
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    # Given a string, an _Alpha and an _Numeric
    a_str = 'a'
    alpha = _Alpha(a_str)
    numeric = _Numeric(0)

    # When comparing the first with the others
    # Then a_str and alpha match
    assert a_str == alpha
    assert alpha == a_str

    # When comparing the first and the third
    # Then a_str is lesser than numeric
    assert a_str < numeric

    # When comparing the second and the third
    # Then alpha is lesser than numeric
    assert alpha < numeric


# Generated at 2022-06-13 16:57:54.364421
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    import pytest
    ver = SemanticVersion('1.2.3')
    assert ver.major == 1
    assert ver.minor == 2
    assert ver.patch == 3
    assert ver.prerelease == ()
    assert ver.buildmetadata == ()
    ver = SemanticVersion('1.2.3-alpha')
    assert ver.major == 1
    assert ver.minor == 2
    assert ver.patch == 3
    assert ver.prerelease == ('alpha',)
    assert ver.buildmetadata == ()
    ver = SemanticVersion('1.2.3-alpha.1')
    assert ver.major == 1
    assert ver.minor == 2
    assert ver.patch == 3
    assert ver.prerelease == ('alpha', '1')
    assert ver.buildmetadata == ()

# Generated at 2022-06-13 16:58:07.355031
# Unit test for method parse of class SemanticVersion

# Generated at 2022-06-13 16:58:21.423578
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    version = SemanticVersion("2.9.2")
    assert version.vstring == "2.9.2"
    assert version.major == 2
    assert version.minor == 9
    assert version.patch == 2
    assert version.prerelease == ()
    assert version.buildmetadata == ()

    version = SemanticVersion("0.0.2")
    assert version.vstring == "0.0.2"
    assert version.major == 0
    assert version.minor == 0
    assert version.patch == 2
    assert version.prerelease == ()
    assert version.buildmetadata == ()

    version = SemanticVersion("0.4.2-alpha.3+42")
    assert version.vstring == "0.4.2-alpha.3+42"
    assert version.major == 0
    assert version.minor

# Generated at 2022-06-13 16:58:29.947763
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    # Test constructor
    s = SemanticVersion()

    # Test valid input
    s.parse('1.2.3')
    assert s.major == 1
    assert s.minor == 2
    assert s.patch == 3
    assert s.prerelease == ()
    assert s.buildmetadata == ()

    s.parse('1.2.3-1.2.3+1.2.3')
    assert s.major == 1
    assert s.minor == 2
    assert s.patch == 3
    assert s.prerelease == (_Numeric('1'), _Numeric('2'), _Numeric('3'))
    assert s.buildmetadata == (_Numeric('1'), _Numeric('2'), _Numeric('3'))


# Generated at 2022-06-13 16:58:34.673762
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    alpha = _Alpha("alpha")
    assert(alpha <= "alpha")
    assert(alpha <= "beta")
    assert(not alpha <= "ZZZ")
    beta = _Alpha("beta")
    assert(alpha <= beta)
    assert(not beta <= alpha)


# Generated at 2022-06-13 16:58:43.996991
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose = LooseVersion('1.2.3.dev2')
    semver = SemanticVersion.from_loose_version(loose)
    assert semver == '1.2.3-dev2'

    # Version without a marker
    loose = LooseVersion('1.2.3.dev2')
    semver = SemanticVersion.from_loose_version(loose)
    assert semver == '1.2.3-dev2'

    # Version with a marker
    loose = LooseVersion('1.2.3.dev2+sivel')
    semver = SemanticVersion.from_loose_version(loose)
    assert semver == '1.2.3-dev2+sivel'

    # Version with a marker and a builder

# Generated at 2022-06-13 16:58:49.058945
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    a1 = _Alpha('a')
    a2 = _Alpha('a')
    a3 = _Alpha('b')
    assert a1 <= a2
    assert a1 <= a3
    a = _Alpha('a')
    b = _Alpha('b')
    assert a <= b
    assert not a <= 'b'


# Generated at 2022-06-13 16:58:56.533615
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test case: Invalid Argument
        # Argument is None
    with pytest.raises(ValueError) as ve:
        SemanticVersion.from_loose_version(None)
    assert 'is not a LooseVersion' in str(ve)

        # Argument is not a LooseVersion
    with pytest.raises(ValueError) as ve:
        SemanticVersion.from_loose_version(1)
    assert 'is not a LooseVersion' in str(ve)

        # Argument has non-integer values
    with pytest.raises(ValueError) as ve:
        SemanticVersion.from_loose_version('1.0.0a')
    assert 'Non integer values in' in str(ve)

    # Test case: Valid Argument
    # Source Version: 1.2.3.4+abc.1.

# Generated at 2022-06-13 16:59:15.064429
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import json
    import os
    import sys

    from ansible.module_utils._text import to_text
    from ansible.module_utils.pycompat24 import get_exception

    # Read in test cases from file
    test_file = os.path.join(os.path.dirname(__file__),
                             'unit/version/test_SemanticVersion_from_loose_version_cases.json')
    with open(test_file, 'rb') as f:
        test_cases = json.load(f)

    # Some tests will fail with a specific Python version
    # Filter out the tests that are expected to fail
    skip_version = test_cases.pop('@python_version')
    if sys.version_info[:2] in skip_version:
        return

    # Validate that test cases are

# Generated at 2022-06-13 16:59:26.460496
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test case: main algorithm test
    # Try to create a SemanticVersion from a LooseVersion with integer tuples
    try:
        v = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    except ValueError:
        raise RuntimeError('1')

    if not isinstance(v, SemanticVersion):
        raise RuntimeError('2')

    if v != '1.2.3':
        raise RuntimeError('3')

    # Test case: main algorithm test
    # Try to create a SemanticVersion from a LooseVersion with integer tuples
    try:
        v = SemanticVersion.from_loose_version(LooseVersion('1.2'))
    except ValueError:
        raise RuntimeError('4')

    if not isinstance(v, SemanticVersion):
        raise Runtime

# Generated at 2022-06-13 16:59:38.341989
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # Ensure a LooseVersion is needed
    loose_version = '1.2.3'
    try:
        SemanticVersion.from_loose_version(loose_version)
    except ValueError as e:
        assert str(e) == ('%r is not a LooseVersion' % loose_version)

    # Ensure only integers and strings are allowed
    loose_version = LooseVersion('1.2.3')
    try:
        SemanticVersion.from_loose_version(loose_version)
    except ValueError as e:
        assert str(e) == ('Non integer values in %r' % loose_version)

    loose_version = LooseVersion('1.2.3-rc1')

# Generated at 2022-06-13 16:59:51.997973
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2')) == SemanticVersion('1.2.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3.dev123')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.1')) == SemanticVersion('1.2.3-alpha.1')

# Generated at 2022-06-13 17:00:00.933427
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Basic test of class SemanticVersion:
    # Create a few test versions, then compare them to check the
    # comparison methods.
    #
    # The basic tests are of the simplest forms, three dot-separated
    # numbers.  The tests of comparison with "pre-release" and "build
    # metadata" strings are in test_semver_prerelease_metadata.py.
    #
    # The tests are intended to be comprehensive and some cases are
    # redundant, but they help to illustrate the different types of
    # version number that the code can handle.

    v0_0_0 = SemanticVersion()
    v1_0_0 = SemanticVersion('1.0.0')
    v1_0_1 = SemanticVersion('1.0.1')

# Generated at 2022-06-13 17:00:07.531289
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # Test #1: 1.2.3
    loose_version_1 = LooseVersion('1.2.3')
    semver_version_1 = SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(loose_version_1) == semver_version_1

    # Test #2: 2.0.0
    loose_version_2 = LooseVersion('2.0.0')
    semver_version_2 = SemanticVersion('2.0.0')
    assert SemanticVersion.from_loose_version(loose_version_2) == semver_version_2

    # Test #3: v2.0.0
    loose_version_3 = LooseVersion('v2.0.0')

# Generated at 2022-06-13 17:00:17.666816
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version(): 
    import unittest
    import sys
    class Test_SemanticVersion(unittest.TestCase):
        def test(self):
            import ansible
            ansible_version = ansible.__version__
            output_version = SemanticVersion.from_loose_version(ansible_version).vstring
            self.assertEqual(ansible_version, output_version)
    tester = Test_SemanticVersion()
    tester.test()


# Backwards compatibility for old-style text comparisons
SemanticVersion.__str__ = SemanticVersion.__repr__

SemanticVersion.__hash__ = Version.__hash__


__all__ = ('SemanticVersion',)

# Generated at 2022-06-13 17:00:27.176477
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six import b

    # Test the normal workflow
    loose_version = LooseVersion('2.3.4')
    assert SemanticVersion.from_loose_version(loose_version).vstring == '2.3.4'

    # Test passing a non LooseVersion
    try:
        SemanticVersion.from_loose_version('2.3.4')
    except ValueError:
        pass
    else:
        assert True, 'Attempting to pass a non LooseVersion did not raise a ValueError'

    # Passing a ValueError if an alpha value is in the LooseVersion
    loose_version = LooseVersion('2.3.3a')
    try:
        SemanticVersion.from_loose_version(loose_version)
    except ValueError:
        pass
   

# Generated at 2022-06-13 17:00:36.465476
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0Z')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.1')) == SemanticVersion('1.0.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.1.0')) == SemanticVersion('1.1.0')
    assert SemanticVersion.from_loose_version(LooseVersion('2.0.0')) == SemanticVersion('2.0.0')

# Generated at 2022-06-13 17:00:49.086439
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.1')) == SemanticVersion('1.1.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.1.1')) == SemanticVersion('1.1.1')
    assert SemanticVersion.from_loose_version(SemanticVersion('1.2.3')) == SemanticVersion('1.2.3')

    assert SemanticVersion.from_loose_version(SemanticVersion('1.2.3-alpha')) == SemanticVersion('1.2.3-alpha')

# Generated at 2022-06-13 17:01:08.991497
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v1 = SemanticVersion('0.0.1')
    v2 = SemanticVersion.from_loose_version(LooseVersion('0.0.1'))
    assert v1 == v2
    v1 = SemanticVersion('0.0.1+build_1')
    v2 = SemanticVersion.from_loose_version(LooseVersion('0.0.1-build.1'))
    assert v1 == v2
    v1 = SemanticVersion('0.0.1-alpha')
    v2 = SemanticVersion.from_loose_version(LooseVersion('0.0.1alpha'))
    assert v1 == v2
    v1 = SemanticVersion('0.0.1-beta')

# Generated at 2022-06-13 17:01:20.699265
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.parsing.convert_bool import boolean
    import operator

    for vstring in (
        '1.0.0',
        '0.0.1-alpha',
        '0.0.0+a.b.c',
        '1.2.3-alpha.1',
        '1.2.3-alpha.1234++',
        '1.2.3',
        '1.2.3-0.0.0.0',
        '1.2.3-a.b.c',
    ):
        # Should create a SemanticVersion object
        semantic_version = SemanticVersion.from_loose_version(LooseVersion(vstring))
        assert isinstance(semantic_version, SemanticVersion)

        # Should be equal to versions created from semver strings

# Generated at 2022-06-13 17:01:33.161905
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    import pytest


# Generated at 2022-06-13 17:01:43.064072
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # unittest of method from_loose_version of class SemanticVersion
    #
    # verify that method creates a proper string
    # verify that a string is not processed
    # verify that a LooseVersion is processed
    #
    # return the result
    ret = {}


# Generated at 2022-06-13 17:01:52.997358
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version('1.2.3') == '1.2.3'
    assert SemanticVersion.from_loose_version('1.2.3-alpha') == '1.2.3-alpha'
    assert SemanticVersion.from_loose_version('1.2.3+build.1.a') == '1.2.3+build.1.a'
    assert SemanticVersion.from_loose_version('1.2.3.4') == '1.2.3'
    assert SemanticVersion.from_loose_version('1.2.3.4-alpha') == '1.2.3-alpha'

# Generated at 2022-06-13 17:02:02.769496
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3.4')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+4')) == SemanticVersion('1.2.3+4')
    assert SemanticVersion.from_loose_version(LooseVersion('123+456')) == SemanticVersion('123.0.0+456')

# Generated at 2022-06-13 17:02:13.667270
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import collections
    import pytest
    from distutils.version import LooseVersion
    from ansible.module_utils.six import string_types

    t = collections.namedtuple('test', 'inp exp')


# Generated at 2022-06-13 17:02:22.768778
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('0.1.1')) == SemanticVersion('0.1.1')
    assert SemanticVersion.from_loose_version(LooseVersion('0.1.1.0')) == SemanticVersion('0.1.1')
    assert SemanticVersion.from_loose_version(LooseVersion('0.1.1+foo.1')) == SemanticVersion('0.1.1+foo.1')

# Unit test parese method of class SemanticVersion

# Generated at 2022-06-13 17:02:32.386755
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from_loose_version = SemanticVersion.from_loose_version

    version = LooseVersion('1.1.1')
    assert(from_loose_version(version) == SemanticVersion('1.1.1'))

    version = LooseVersion('1.1.1-alpha.1')
    assert(from_loose_version(version) == SemanticVersion('1.1.1-alpha.1'))

    version = LooseVersion('1.1.1+build.1')
    assert(from_loose_version(version) == SemanticVersion('1.1.1+build.1'))

    version = LooseVersion('1.1.1-alpha.1+build.1')

# Generated at 2022-06-13 17:02:40.553923
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    This test does not require any change in code.
    """

    # Create a loose version string
    loose_string = '0.1.1-dev.3+3aef6'
    # Create a loose version object
    loose_version = LooseVersion(loose_string)
    # Convert that loose version object to a semantic version
    sem_version = SemanticVersion.from_loose_version(loose_version)
    # Assert the two are equal
    assert loose_string == sem_version.vstring

# Generated at 2022-06-13 17:02:56.554530
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    print("Doing unittest for method from_loose_version of class SemanticVersion")

    # Case: exact version number
    assert str(SemanticVersion.from_loose_version(LooseVersion("1.2"))) == "1.2.0"

    # Case: partial version number
    assert str(SemanticVersion.from_loose_version(LooseVersion("1"))) == "1.0.0"

    # Case: version number with pre release
    assert str(SemanticVersion.from_loose_version(LooseVersion("1.2.3-alpha"))) == "1.2.3-alpha"

    # Case: version number with build metadata

# Generated at 2022-06-13 17:03:07.833024
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Unit test for method from_loose_version of class SemanticVersion"""

    # If the method is not given a LooseVersion as an argument, it
    # should raise a ValueError
    try:
        SemanticVersion.from_loose_version(SemanticVersion('0.1.2'))
    except ValueError:
        pass
    else:
        raise AssertionError("No ValueError raised")


# Generated at 2022-06-13 17:03:14.659870
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    Test the from_loose_version() method of the SemanticVersion class,
    specifically parsing 'distutils.version.LooseVersion' objects.
    """
    # Valid version strings that match Semantic Versioning conventions.
    valid_test_strings = [
        'v2.8.0', 'v2.8.0alpha1', 'v2.8.0beta1', 'v2.8.0rc1'
    ]

    # Invalid version strings that do not match Semantic Versioning conventions.
    invalid_test_strings = [
        'v2.8.0.1', 'v2.8.0betaA', 'v2.8.0rca'
    ]

    # Actual test case logic.

# Generated at 2022-06-13 17:03:22.049179
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:03:28.428164
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert str(SemanticVersion.from_loose_version(LooseVersion('1.2.3'))) == '1.2.3'
    assert str(SemanticVersion.from_loose_version(LooseVersion('1.2.3.4'))) == '1.2.3'
    assert str(SemanticVersion.from_loose_version(LooseVersion('1.2.3+4'))) == '1.2.3+4'
    assert str(SemanticVersion.from_loose_version(LooseVersion('1.2.3-4'))) == '1.2.3-4'



# Generated at 2022-06-13 17:03:36.424058
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Check version values containing only numbers are converted properly
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.0')).vstring == '0.0.0'
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.1')).vstring == '0.0.1'
    assert SemanticVersion.from_loose_version(LooseVersion('0.0')).vstring == '0.0.0'
    assert SemanticVersion.from_loose_version(LooseVersion('0.1')).vstring == '0.1.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')).vstring == '1.0.0'

# Generated at 2022-06-13 17:03:45.064483
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    test1 = SemanticVersion.from_loose_version(LooseVersion('1'))
    assert test1.vstring == '1.0.0'

    test2 = SemanticVersion.from_loose_version(LooseVersion('1.0'))
    assert test2.vstring == '1.0.0'

    test3 = SemanticVersion.from_loose_version(LooseVersion('1.1'))
    assert test3.vstring == '1.1.0'

    test4 = SemanticVersion.from_loose_version(LooseVersion('1.1.1'))
    assert test4.vstring == '1.1.1'

    test5 = SemanticVersion.from_loose_version(LooseVersion('1.1.1-dev'))
    assert test5.v

# Generated at 2022-06-13 17:03:54.677901
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:04:04.576953
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    vstring = '1.2.3'
    loose_version = LooseVersion(vstring)
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert(semantic_version == vstring)

    vstring = '1.2.3.4'
    loose_version = LooseVersion(vstring)
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert(semantic_version == '1.2.3')

    vstring = '1.2.3-4'
    loose_version = LooseVersion(vstring)
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert(semantic_version == vstring)


# Generated at 2022-06-13 17:04:18.112839
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    class DummyVersion(object):
        def __init__(self, version):
            self.version = version
        def __str__(self):
            return self.version
        def __repr__(self):
            return self.version

    class Test(object):
        def __init__(self, version, expected_version):
            self.version = version
            self.expected_version = expected_version
        def __str__(self):
            return 'Test(%s, %s)' % (self.version, self.expected_version)
        def __repr__(self):
            return 'Test(%r, %r)' % (self.version, self.expected_version)
    # Tests are based on https://semver.org/#spec-item-11

# Generated at 2022-06-13 17:04:51.437889
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    r = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    assert isinstance(r, SemanticVersion)
    assert r.vstring == '1.2.3'
    r = SemanticVersion.from_loose_version(LooseVersion('1.2.3.45'))
    assert isinstance(r, SemanticVersion)
    assert r.vstring == '1.2.3'
    r = SemanticVersion.from_loose_version(LooseVersion('1.2.3-45'))
    assert isinstance(r, SemanticVersion)
    assert r.vstring == '1.2.3-45'
    r = SemanticVersion.from_loose_version(LooseVersion('1.2.3-45.67'))
    assert isinstance

# Generated at 2022-06-13 17:05:05.026809
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v = LooseVersion('1.2.3.4.5.6.7~dev9.10+abc.def')
    sv = SemanticVersion.from_loose_version(v)
    assert sv.vstring == '1.2.3~dev9.10+abc.def'

    v = LooseVersion('1.2.3.4.5.6.7.8.9')
    sv = SemanticVersion.from_loose_version(v)
    assert sv.vstring == '1.2.3'

    v = LooseVersion('1.2.3.4.5.6.7.8.9abc.def')
    sv = SemanticVersion.from_loose_version(v)
    assert sv.vstring == '1.2.3'


# Generated at 2022-06-13 17:05:13.613797
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('2.3.3')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '2.3.3'

    loose_version = LooseVersion('2')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '2.0.0'

    loose_version = LooseVersion('2.3')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '2.3.0'

    loose_version = LooseVersion('2.3.3a1')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '2.3.3-a1'



# Generated at 2022-06-13 17:05:20.657744
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Arrange
    loose_version_1 = LooseVersion("1.5.5.1")
    loose_version_2 = LooseVersion("1.5.5.alpha1")
    loose_version_3 = LooseVersion("2.0a1")
    loose_version_4 = LooseVersion("2.0")

    # Act
    semver_1 = SemanticVersion.from_loose_version(loose_version_1)
    semver_2 = SemanticVersion.from_loose_version(loose_version_2)
    semver_3 = SemanticVersion.from_loose_version(loose_version_3)
    semver_4 = SemanticVersion.from_loose_version(loose_version_4)

    # Assert

# Generated at 2022-06-13 17:05:31.693752
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # test for class SemanticVersion.from_loose_version
    # given a LooseVersion, return a SemanticVersion
    from distutils.version import LooseVersion
    from ansible.module_utils.semver import SemanticVersion
    # test case 1, create a SemanticVersion from given LooseVersion
    given_version = LooseVersion('1.1')
    test_version = SemanticVersion.from_loose_version(given_version)
    # extract version info from given LooseVersion
    given_major = given_version.version[0]
    given_minor = given_version.version[1]
    given_patch = given_version.version[2]
    # compare major version number
    assert test_version.major == given_major
    # compare minor version number
    assert test_version.minor == given

# Generated at 2022-06-13 17:05:44.268170
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import ansible
    assert (SemanticVersion.from_loose_version(LooseVersion("2.9.0")) ==
            SemanticVersion("2.9.0"))
    assert (SemanticVersion.from_loose_version(LooseVersion("2.9.0.final.0")) ==
            SemanticVersion("2.9.0"))
    assert (SemanticVersion.from_loose_version(LooseVersion("2.9.0.rc.2")) ==
            SemanticVersion("2.9.0-rc.2"))
    assert (SemanticVersion.from_loose_version(LooseVersion("2.9.0.final.0.0.rc.2")) ==
            SemanticVersion("2.9.0-rc.2"))

# Generated at 2022-06-13 17:05:56.431232
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import pytest
    from ansible.module_utils.six import PY2, PY3

    if PY2:
        test_cases = {
            '0.9': '0.9',
            '0.9+123': '0.9',
            '0.9-alpha': '0.9',
            '1.0': '1.0',
            '1.0+123': '1.0',
            '1.0-alpha': '1.0'
        }

# Generated at 2022-06-13 17:06:05.599242
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    Test SemanticVersion.from_loose_version
    """

# Generated at 2022-06-13 17:06:17.768555
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+1a')) == SemanticVersion('1.2.3+1a')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-1a')) == SemanticVersion('1.2.3-1a')
    assert SemanticVersion.from_loose_version(LooseVersion('2.3')) == SemanticVersion('2.3.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')

# Generated at 2022-06-13 17:06:29.753846
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # Test that class method is present and callable
    assert callable(SemanticVersion.from_loose_version)

    # Test that we are returning a SemanticVersion object
    result = SemanticVersion.from_loose_version(LooseVersion('1'))
    assert isinstance(result, SemanticVersion)

    # Test that we can pass in a LooseVersion object with a string
    result = SemanticVersion.from_loose_version(LooseVersion('1.0.1-beta.1+build.1'))
    assert isinstance(result, SemanticVersion)

    # Test that we can pass in a LooseVersion object with a tuple
    result = SemanticVersion.from_loose_version(LooseVersion((1, 0, 1, 'beta', 1, 'build', 1)))
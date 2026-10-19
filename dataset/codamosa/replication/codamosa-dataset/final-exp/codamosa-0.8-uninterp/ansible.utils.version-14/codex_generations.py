

# Generated at 2022-06-13 16:57:38.176959
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Unit test for method from_loose_version of class SemanticVersion
    """
    assert str(SemanticVersion.from_loose_version(LooseVersion('2.3.3'))) == '2.3.3'
    assert str(SemanticVersion.from_loose_version(LooseVersion('2.3.3.beta.1'))) == '2.3.3-beta.1'
    assert str(SemanticVersion.from_loose_version(LooseVersion('2.3.3-beta.1'))) == '2.3.3-beta.1'
    assert str(SemanticVersion.from_loose_version(LooseVersion('2.3.3.rc.1'))) == '2.3.3-rc.1'

# Generated at 2022-06-13 16:57:48.705684
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    v = SemanticVersion('9.9.9')
    assert v.major == 9
    assert v.minor == 9
    assert v.patch == 9
    assert v.prerelease == ()
    assert v.buildmetadata == ()

    v = SemanticVersion('0.0.1')
    assert v.major == 0
    assert v.minor == 0
    assert v.patch == 1
    assert v.prerelease == ()
    assert v.buildmetadata == ()

    v = SemanticVersion('0.0.1-alpha')
    assert v.major == 0
    assert v.minor == 0
    assert v.patch == 1
    assert v.prerelease == ('alpha',)
    assert v.buildmetadata == ()

    v = SemanticVersion('0.0.1-0.1')
    assert v.major

# Generated at 2022-06-13 16:57:52.948593
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    version = SemanticVersion()
    version.parse('1.2.3-alpha.1+buildmetadata.1')
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == (_Numeric('alpha'), _Numeric('1'))
    assert version.buildmetadata == (_Alpha('buildmetadata'), _Numeric('1'))

    version = SemanticVersion()
    version.parse('1.2.3-alpha.1+buildmetadata.1')
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == (_Numeric('alpha'), _Numeric('1'))
    assert version.buildmetadata == (_Alpha('buildmetadata'), _Numeric('1'))



# Generated at 2022-06-13 16:58:06.142123
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # full version
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-beta.1')) == SemanticVersion('1.2.3-beta.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+build.20150101')) == SemanticVersion('1.2.3+build.20150101')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-beta.1+build.20150101')) == SemanticVersion('1.2.3-beta.1+build.20150101')

    # partial version
    assert SemanticVersion

# Generated at 2022-06-13 16:58:16.348329
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    for test_spec in (
            '1',
            '1.0',
            '1.0.0',
            '1.0.0-alpha.1',
            '1.0.0+20130313144700',
            '1.0.0-beta.11+exp.sha.5114f85',
            '1.0.0-rc.1+build.1',
    ):
        version = SemanticVersion()
        version.parse(test_spec)
        assert str(version) == test_spec


# Generated at 2022-06-13 16:58:27.194204
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('0.1.2')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    result = [semantic_version.major, semantic_version.minor, semantic_version.patch, semantic_version.prerelease]
    expected = [0, 1, 2, ()]
    assert expected == result
    loose_version = LooseVersion('1.2.3-alpha.1.2')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    result = [semantic_version.major, semantic_version.minor, semantic_version.patch, semantic_version.prerelease]
    expected = [1, 2, 3, ('alpha', '1', '2')]
    assert expected == result
    loose_version = Loose

# Generated at 2022-06-13 16:58:39.922946
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    s = SemanticVersion()
    assert (s.major, s.minor, s.patch, s.prerelease, s.buildmetadata) == (None, None, None, (), ())
    # examples from https://semver.org/#spec-item-9
    s.parse('0.0.4')
    assert (s.major, s.minor, s.patch, s.prerelease, s.buildmetadata) == (0, 0, 4, (), ())
    s.parse('1.2.3')
    assert (s.major, s.minor, s.patch, s.prerelease, s.buildmetadata) == (1, 2, 3, (), ())
    s.parse('10.20.30')

# Generated at 2022-06-13 16:58:51.856436
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 16:58:58.052845
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import collections
    if hasattr(collections, 'UserString'):
        class u(collections.UserString):
            pass
    else:
        class u(str):
            pass

    def do_test(input_vstring, expected):
        assert SemanticVersion.from_loose_version(LooseVersion(input_vstring)).vstring == expected

    do_test('1', '1.0.0')
    do_test('1.2', '1.2.0')
    do_test('1.2.3', '1.2.3')
    do_test('1.2.3-alpha4', '1.2.3-alpha4')
    do_test('1.2.3+build05', '1.2.3+build05')

# Generated at 2022-06-13 16:59:08.430188
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """The method from_loose_version of class  SemanticVersion is well tested .
    In this unit test, the parameter values are manipulated so that the test
    method can exercise all the code paths.
    """
    from ansible.module_utils.distutils.version import LooseVersion
    # Verify that a LooseVersion can be converted to SemanticVersion
    loose_version = LooseVersion("1.0.0")
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert isinstance(semantic_version, SemanticVersion)
    testresult = semantic_version.vstring == "1.0.0"
    assert testresult
    # Verify that a standard SemanticVersion can be converted to SemanticVersion
    semantic_version = SemanticVersion("1.0.0")
    new_semantic

# Generated at 2022-06-13 16:59:30.237507
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion("1.0.0-prerelease+meta")
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.vstring == '1.0.0-prerelease+meta'
    assert semantic_version.major == 1
    assert semantic_version.minor == 0
    assert semantic_version.patch == 0
    assert semantic_version.prerelease == (text_type('prerelease'),)
    assert semantic_version.buildmetadata == (text_type('meta'),)

    loose_version = LooseVersion("1.0.0+meta")
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.vstring == '1.0.0+meta'
    assert semantic_version.major

# Generated at 2022-06-13 16:59:42.995818
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    result = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    assert result.vstring == '1.2.3'
    result = SemanticVersion.from_loose_version(LooseVersion('1.2.3.0'))
    assert result.vstring == '1.2.3'
    result = SemanticVersion.from_loose_version(LooseVersion('0.2.3'))
    assert result.vstring == '0.2.3'
    result = SemanticVersion.from_loose_version(LooseVersion('0.2.3.4'))
    assert result.vstring == '0.2.3.4'
    result = SemanticVersion.from_loose_version(LooseVersion('0.2.3+abcd'))


# Generated at 2022-06-13 16:59:56.035755
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # The given LooseVersion is not a LooseVersion
    this_should_raise = SemanticVersion.from_loose_version(123)
    # The given LooseVersion has a non integer value
    this_should_raise = SemanticVersion.from_loose_version(LooseVersion("aaa.bbb.ccc"))

    # This works
    this_should_work = SemanticVersion.from_loose_version(LooseVersion("1"))
    this_should_work = SemanticVersion.from_loose_version(LooseVersion("1.2"))
    this_should_work = SemanticVersion.from_loose_version(LooseVersion("1.2.3"))
    this_should_work = SemanticVersion.from_loose_version(LooseVersion("1.2.3-alpha+meta"))
   

# Generated at 2022-06-13 17:00:04.751301
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.5.1')) == SemanticVersion('1.5.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.5.1.dev1')) == SemanticVersion('1.5.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.5.1-dev1')) == SemanticVersion('1.5.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.5')) == SemanticVersion('1.5.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.5.0')) == SemanticVersion('1.5.0')

# Generated at 2022-06-13 17:00:17.180085
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('2.0.0-alpha')) == SemanticVersion('2.0.0-alpha')
    assert SemanticVersion.from_loose_version(LooseVersion('2.0.0-alpha+001')) == SemanticVersion('2.0.0-alpha+001')

# Generated at 2022-06-13 17:00:24.412657
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test two examples from PEP-440
    assert SemanticVersion.from_loose_version(LooseVersion('0.4.2')) == SemanticVersion('0.4.2')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    # Test an example with a local version identifier
    assert SemanticVersion.from_loose_version(LooseVersion('0.4.2+foo.bar1')) == SemanticVersion('0.4.2+foo.bar1')

# Generated at 2022-06-13 17:00:30.693543
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    major = '0'
    minor = '4'
    patch = '0'
    prerelease = 'r1'
    buildmetadata = 'dev'
    looseversion = LooseVersion(major + '.' + minor + '.' + patch + '-' + prerelease + '+' + buildmetadata)
    semver = SemanticVersion.from_loose_version(looseversion)
    assert semver == '0.4.0-r1+dev'


# Generated at 2022-06-13 17:00:38.956770
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import pytest
    from ansible.module_utils.compat.version import LooseVersion

    def test(loose_version, expected):
        v = SemanticVersion.from_loose_version(loose_version)
        assert v.__class__ == SemanticVersion
        assert v.core == expected

    expected = (0, 2, 0)
    test(LooseVersion("0.2.0"), expected)

    expected = (2, 5, 4)
    test(LooseVersion("2.5.4"), expected)
    test(LooseVersion("2.5.4"), expected)

    expected = (0, 0, 100)
    test(LooseVersion("0.0.100"), expected)


# Generated at 2022-06-13 17:00:50.592481
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from distutils.version import LooseVersion


# Generated at 2022-06-13 17:00:58.942176
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Unit test the SemanticVersion.from_loose_version method"""
    import unittest

    class TestSemanticVersionFromLooseVersion(unittest.TestCase):
        def test_from_loose_version_1(self):
            # Version with no prerelease or build metadata
            loose_version = LooseVersion('1.2.3')
            semver = SemanticVersion.from_loose_version(loose_version)
            self.assertEqual(semver.core, (1, 2, 3))
            self.assertFalse(semver.prerelease)
            self.assertFalse(semver.buildmetadata)

        def test_from_loose_version_2(self):
            # Version with a prerelease, but no build metadata
            loose_version = LooseVersion('1.2.3-pre')

# Generated at 2022-06-13 17:01:12.839061
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('3.3.3-a1.1')
    if not isinstance(loose_version, LooseVersion):
        raise ValueError("%r is not a LooseVersion" % loose_version)
    try:
        version = loose_version.version[:]
    except AttributeError:
        raise ValueError("%r is not a LooseVersion" % loose_version)

    extra_idx = 3
    for marker in ('-', '+'):
        try:
            idx = version.index(marker)
        except ValueError:
            continue
        else:
            if idx < extra_idx:
                extra_idx = idx
    version = version[:extra_idx]


# Generated at 2022-06-13 17:01:23.847554
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Simple version
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')

    # Version with prerelease information
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3.alpha1')) == SemanticVersion('1.2.3-alpha1')

    # Version with build metadata
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+4')) == SemanticVersion('1.2.3+4')

    # Version with prerelease information and build metadata
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3.alpha1-1+4')) == SemanticVersion('1.2.3-alpha1-1+4')



# Generated at 2022-06-13 17:01:37.056760
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version('1.0') == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version('1.0.0') == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version('1.0.0+abc') == SemanticVersion('1.0.0+abc')
    assert SemanticVersion.from_loose_version('1.0.0-abc') == SemanticVersion('1.0.0-abc')
    assert SemanticVersion.from_loose_version('11.10.9') == SemanticVersion('11.10.9')
    assert SemanticVersion.from_loose_version('1.0+abc') == SemanticVersion('1.0.0+abc')
    assert SemanticVersion

# Generated at 2022-06-13 17:01:46.120448
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test case 1: 1.2.3-rc1 is not a LooseVersion
    try:
        v = SemanticVersion.from_loose_version('1.2.3-rc1')
        raise AssertionError('1.2.3-rc1 is not a LooseVersion')
    except ValueError:
        pass

    # Test case 2: LooseVersion is not a LooseVersion
    try:
        v = SemanticVersion.from_loose_version(LooseVersion('1.2.3-rc1'))
        raise AssertionError('LooseVersion is not a LooseVersion')
    except ValueError:
        pass

    # Test case 3: LooseVersion is not a LooseVersion

# Generated at 2022-06-13 17:01:52.195614
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Case 1. "1.2.3" will be converted to "1.2.3"
    loose_version = LooseVersion('1.2.3')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version == '1.2.3'

    # Case 2. "1.2.3.4" will be converted to "1.2.3"
    loose_version = LooseVersion('1.2.3.4')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version == '1.2.3'

    # Case 3. "1.2.3.abc" will be converted to "1.2.3"
    loose_version = LooseVersion('1.2.3.abc')

# Generated at 2022-06-13 17:02:02.221246
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Unit test for method from_loose_version of class SemanticVersion"""
    # test conversion from LooseVersion
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')).vstring == '1.0.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.1')).vstring == '1.0.1'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha.1')).vstring == '1.0.0-alpha.1'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build01')).vstring == '1.0.0+build01'

# Generated at 2022-06-13 17:02:13.545570
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion

# Generated at 2022-06-13 17:02:18.428859
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    expected = SemanticVersion('1.0.0')
    loose_version = LooseVersion('1.0.0')
    result = SemanticVersion.from_loose_version(loose_version)
    assert result == expected


# Generated at 2022-06-13 17:02:29.718607
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.1')) == SemanticVersion('1.1.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.1a')) == SemanticVersion('1.1.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.1.2')) == SemanticVersion('1.1.2')
    assert SemanticVersion.from_loose_version(LooseVersion('1.1.2.3')) == SemanticVersion('1.1.2')

# Generated at 2022-06-13 17:02:42.542276
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # pylint: disable=W0106, W0122
    # non-public function '_cmpkey'
    # used builtin function 'cmp'
    # hash_cmp 'cmp' is deprecated: use ==, !=, etc.
    cmp = SemanticVersion.__dict__['_cmp']
    cmpkey = SemanticVersion.__dict__['_cmpkey']

    class Struct:
        def __init__(self, **kw):
            for k, v in kw.items():
                setattr(self, k, v)


# Generated at 2022-06-13 17:03:04.355001
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    try:
        loose_version = LooseVersion('1.0.0-alpha.1+build.123')
        SemanticVersion.from_loose_version(loose_version)
    except ValueError:
        assert False
    else:
        assert True

    try:
        loose_version = LooseVersion('1.0.0-beta.2+build.123')
        SemanticVersion.from_loose_version(loose_version)
    except ValueError:
        assert False
    else:
        assert True

    try:
        loose_version = LooseVersion('1.0.0-rc.3+build.123')
        SemanticVersion.from_loose_version(loose_version)
    except ValueError:
        assert False
    else:
        assert True


# Generated at 2022-06-13 17:03:09.505918
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_v = LooseVersion('1.1.1.post1.dev1')
    sem_v = SemanticVersion.from_loose_version(loose_v)
    expect(sem_v=='1.1.1-post1.dev1')

# Generated at 2022-06-13 17:03:16.066290
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test case 4: Check that the right exception is raised when
    # the argument is not a LooseVersion
    my_version = SemanticVersion("7.0.0")
    my_loose_version = LooseVersion("7.0.0")
    my_semantic_version = SemanticVersion("7.0.0")

    assert my_semantic_version == my_version.from_loose_version(my_loose_version)
    try:
        my_version.from_loose_version(my_version)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")



# Generated at 2022-06-13 17:03:25.223438
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion

    # Nominal cases
    # LooseVersion('4.4.4') -> SemanticVersion('4.4.4')
    assert SemanticVersion.from_loose_version(LooseVersion('4.4.4')) == SemanticVersion('4.4.4')

    # LooseVersion('4.4.4.1') -> SemanticVersion('4.4.4')
    assert SemanticVersion.from_loose_version(LooseVersion('4.4.4.1')) == SemanticVersion('4.4.4')

    # LooseVersion('0.0.0.1') -> SemanticVersion('0.0.0')

# Generated at 2022-06-13 17:03:34.184772
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    for key in ['1.4.1', '1.4.1_alpha', '1.4.1a', '1.4.1a1', '1.4.1a2.dev456', '1', '1.0', '1.0+123.456', '1.2.3a0.post2.dev4567']:
        loose_version = LooseVersion(key)
        assert SemanticVersion.from_loose_version(loose_version) == SemanticVersion(key)

if __name__ == '__main__':
    test_SemanticVersion_from_loose_version()

# Generated at 2022-06-13 17:03:42.577430
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test normal usage
    assert repr(SemanticVersion.from_loose_version(LooseVersion('1.0.0'))) == 'SemanticVersion(\'1.0.0\')'
    assert repr(SemanticVersion.from_loose_version(LooseVersion('1.0.0a2.dev456+abcdef'))) == 'SemanticVersion(\'1.0.0-a2.dev456+abcdef\')'

    # Test bad usage
    try:
        SemanticVersion.from_loose_version('not loose version')
        assert False, 'didn\'t raise expected ValueError'
    except ValueError:
        pass

# Generated at 2022-06-13 17:03:46.026018
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    lv_testing = LooseVersion("1.4.0")
    sv_result = SemanticVersion.from_loose_version(lv_testing)
    sv_expected = SemanticVersion("1.4.0")
    assert sv_result == sv_expected


# Generated at 2022-06-13 17:03:55.419662
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert str(SemanticVersion.from_loose_version('1.1.1')) == '1.1.1'
    assert str(SemanticVersion.from_loose_version('1.1.1alpha')) == '1.1.1-alpha'
    assert str(SemanticVersion.from_loose_version('1.1.1-alpha.1')) == '1.1.1-alpha.1'
    assert str(SemanticVersion.from_loose_version('1.1.1-alpha.1.2')) == '1.1.1-alpha.1.2'
    assert str(SemanticVersion.from_loose_version('1.1.1-alpha.1.2.3')) == '1.1.1-alpha.1.2.3'

# Generated at 2022-06-13 17:04:05.481546
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    original_version = '1.5'
    loose_version = LooseVersion(original_version)
    semver_version = SemanticVersion.from_loose_version(loose_version)
    assert semver_version.vstring == '1.5.0'
    assert semver_version.is_stable
    assert not semver_version.is_prerelease

    original_version = '1.5.dev1'
    loose_version = LooseVersion(original_version)
    semver_version = SemanticVersion.from_loose_version(loose_version)
    assert semver_version.vstring == '1.5.0-dev1'
    assert not semver_version.is_stable
    assert semver_version.is_prerelease

    original_version = '1.5-1'


# Generated at 2022-06-13 17:04:18.556092
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Example 1
    version = SemanticVersion.from_loose_version(LooseVersion("1.2.3"))
    assert version == SemanticVersion("1.2.3")
    assert version.is_stable

    # Example 2
    version = SemanticVersion.from_loose_version(LooseVersion("1.2.3dev1"))
    assert version == SemanticVersion("1.2.3-dev1")
    assert not version.is_stable

    # Example 3
    version = SemanticVersion.from_loose_version(LooseVersion("1.2.3.dev1"))
    assert version == SemanticVersion("1.2.3-dev1")
    assert not version.is_stable

    # Example 4

# Generated at 2022-06-13 17:04:46.611149
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import unittest

    class TestSemanticVersion_from_loose_version(unittest.TestCase):
        def setUp(self):
            from ansible.module_utils.compat.version import LooseVersion
            self.conv_func = SemanticVersion.from_loose_version

            # version string, expected version, expected is_stable

# Generated at 2022-06-13 17:04:54.919951
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:05:07.952902
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:05:19.398830
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # LooseVersion can deal with versions like '1.0.0rc1',
    # which is not a valid semver
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0rc1')) == SemanticVersion('1.0.0-rc1')

    # LooseVersion can deal with versions like 'v1.0.0',
    # which is not a valid semver
    assert SemanticVersion.from_loose_version(LooseVersion('v1.0.0')) == SemanticVersion('1.0.0')

    # LooseVersion does not deal with versions like '1.0.0+foo',
    # which is a valid semver, but the buildmetadata MUST be ignored
    # when determining version precedence

# Generated at 2022-06-13 17:05:31.087867
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Test SemanticVersion.from_loose_version"""

    from ansible.module_utils.distro import LooseVersion

    def test(input, output):
        assert SemanticVersion.from_loose_version(input) == output

    test(LooseVersion('1.0'), '1.0.0')
    test(LooseVersion('1.0.0'), '1.0.0')
    test(LooseVersion('1.0.0-a.b.c'), '1.0.0-a.b.c')
    test(LooseVersion('1.0.0-a.b.c+d.e.f'), '1.0.0-a.b.c+d.e.f')

# Generated at 2022-06-13 17:05:43.597252
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Testing for invalid LooseVersion Objects
    try:
        SemanticVersion.from_loose_version(Version('0.5.5'))
    except ValueError as e:
        assert e.args[0] == "invalid LooseVersion"

    try:
        SemanticVersion.from_loose_version(SemanticVersion('0.5.5'))
    except ValueError as e:
        assert e.args[0] == "invalid LooseVersion"

    # Testing '-' (invalid)
    try:
        SemanticVersion.from_loose_version(LooseVersion('0.5.5-rc1'))
    except ValueError as e:
        assert e.args[0] == "Non integer values in LooseVersion('0.5.5-rc1')"

    # Testing '+' (

# Generated at 2022-06-13 17:05:50.258966
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    Unit test for SemanticVersion.from_loose_version()
    """
    # test success
    def test_success(loose_version, semver):
        returned_semver = SemanticVersion.from_loose_version(loose_version)
        expected_semver = SemanticVersion(semver)
        assert returned_semver == expected_semver

    test_success(LooseVersion('1.2.3'), '1.2.3')
    test_success(LooseVersion('1.2.3-alpha.5'), '1.2.3-alpha.5')
    test_success(LooseVersion('1.2.3-alpha.5+20200910'), '1.2.3-alpha.5+20200910')

# Generated at 2022-06-13 17:06:00.860042
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('7.4.4')) == SemanticVersion('7.4.4')
    assert SemanticVersion.from_loose_version(LooseVersion('7.4.4.1')) == SemanticVersion('7.4.4')
    assert SemanticVersion.from_loose_version(LooseVersion('27.4.4.1')) == SemanticVersion('27.4.4')
    assert SemanticVersion.from_loose_version(LooseVersion('7.44.4.1')) == SemanticVersion('7.44.4')
    assert SemanticVersion.from_loose_version(LooseVersion('7.4.44.1')) == SemanticVersion('7.4.44')
    assert SemanticVersion.from_loose_

# Generated at 2022-06-13 17:06:08.640544
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')).vstring == '1.2.3'
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-rc0.0')).vstring == '1.2.3-rc0.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+b.0')).vstring == '1.2.3+b.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.0+b.0')).vstring == '1.2.3-alpha.0+b.0'

# Generated at 2022-06-13 17:06:19.434849
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    print('test_SemanticVersion_from_loose_version')


# Generated at 2022-06-13 17:07:05.744438
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Testing version 1.2.3
    version_string = "1.2.3"
    loose_version = LooseVersion(version_string)
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.vstring == version_string
    # Testing version 1.2.3.4
    version_string = "1.2.3.4"
    loose_version = LooseVersion(version_string)
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.vstring == version_string
    # Testing version 1.2.3b1
    version_string = "1.2.3b1"
    loose_version = LooseVersion(version_string)
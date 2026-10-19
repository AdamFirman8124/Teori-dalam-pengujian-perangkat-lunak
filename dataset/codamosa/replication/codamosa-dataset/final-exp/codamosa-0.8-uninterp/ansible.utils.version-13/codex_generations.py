

# Generated at 2022-06-13 16:57:35.097925
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    # Test prerelease
    assert SemanticVersion('1.0.0-rc1').parse('1.0.0-rc1-exp.sha.5114f85')
    assert SemanticVersion('1.0.0-rc1').parse('1.0.0-rc1-exp.sha.5114F85')

    # Test build metadata
    assert SemanticVersion('1.0.0-rc1').parse('1.0.0-rc1+exp.sha.5114f85')
    assert SemanticVersion('1.0.0-rc1').parse('1.0.0-rc1+exp.sha.5114F85')

    assert SemanticVersion('2.0.0-alpha.1').parse('2.0.0-alpha.1+002')

# Generated at 2022-06-13 16:57:41.157433
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2')) == SemanticVersion('1.2.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2+foo')) == SemanticVersion('1.2.0+foo')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2+foo.bar.baz')) == SemanticVersion('1.2.0+foo.bar.baz')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2-alpha')) == SemanticVersion('1.2.0-alpha')
    assert SemanticVersion

# Generated at 2022-06-13 16:57:45.095400
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    sver = SemanticVersion('w.x.y-prerelease.1+build.metadata')
    assert sver.major == 0
    assert sver.minor == 0
    assert sver.patch == 0
    assert sver.prerelease == ('prerelease', '1')
    assert sver.buildmetadata == ('build', 'metadata')


# Generated at 2022-06-13 16:57:53.932586
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """test SemanticVersion.from_loose_version method
    """

    import distutils.version

    # basic cases
    test_cases = [
        # input, expected result
        ['3.0', '3.0.0'],
        ['3.0-alpha', '3.0.0-alpha'],
        ['3.0.1.4-alpha+build.4', '3.0.1-alpha'],
        ['3.0.1-alpha.4+build.4', '3.0.1-alpha.4'],
        ['3.0.1.4-alpha.4+build.4', '3.0.1-alpha.4'],
    ]

    for (input_version, expected) in test_cases:
        v = distutils.version.LooseVersion(input_version)

# Generated at 2022-06-13 16:57:59.132640
# Unit test for method parse of class SemanticVersion

# Generated at 2022-06-13 16:58:12.402480
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six import PY3
    import sys

    # This is needed for ``from_loose_version`` method to work in python3.
    if PY3:
        import distutils
        distutils.LooseVersion = LooseVersion

    # trivial test
    assert SemanticVersion.from_loose_version('') == SemanticVersion('0.0.0')

    # digits only
    assert SemanticVersion.from_loose_version('1') == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version('1.1') == SemanticVersion('1.1.0')
    assert SemanticVersion.from_loose_version('1.1.1') == SemanticVersion('1.1.1')

    # mixed numbers and letters
    assert Sem

# Generated at 2022-06-13 16:58:25.244633
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Unit test for method from_loose_version of class SemanticVersion."""
    import types
    loose_version = object
    try:
        SemanticVersion.from_loose_version(loose_version)
    except ValueError:
        pass
    else:
        assert False

    loose_version = 'abc'
    try:
        SemanticVersion.from_loose_version(loose_version)
    except ValueError:
        pass
    else:
        assert False

    loose_version = '1.2.3'
    try:
        SemanticVersion.from_loose_version(loose_version)
    except ValueError:
        pass
    else:
        assert False

    loose_version = '1.2.3'

# Generated at 2022-06-13 16:58:38.658567
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import pytest

    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(1)

    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(LooseVersion('1'))

    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(SemanticVersion('1'))

    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(LooseVersion('1.2'))

    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(SemanticVersion('1.2'))

    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(LooseVersion('1.2.3'))

# Generated at 2022-06-13 16:58:50.018050
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    # Test success cases
    SemanticVersion('0.0.0')  # all zeros
    SemanticVersion('1.2.3')  # no extra specifiers
    SemanticVersion('1.2.3-alpha')  # prerelease
    SemanticVersion('1.2.3+build')  # build metadata
    SemanticVersion('1.2.3-alpha.123+build.1')  # prerelease and build metadata
    # Test edge cases
    SemanticVersion('0.0.0-0')
    SemanticVersion('0.0.0-alpha')
    SemanticVersion('0.0.0-alpha.0')
    SemanticVersion('0.0.0+0')
    SemanticVersion('0.0.0+alpha')
    SemanticVersion('0.0.0+alpha.0')
   

# Generated at 2022-06-13 16:58:57.084892
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 16:59:12.864704
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Working: V=SemanticVersion.from_loose_version(LooseVersion('0.0.1'))
    #  so we do not test if it is working... (no error ? It's working)
    try:
        V = SemanticVersion.from_loose_version(LooseVersion('0.0.1'))
    except Exception as err:
        assert False, ("Can not convert LooseVersion('0.0.1') to SemanticVersion()")

    # If a non-LooseVersion is given, we should get an Error
    try:
        V = SemanticVersion.from_loose_version("not a LooseVersion")
    except Exception as err:
        assert True
    else:
        assert False, "SemanticVersion.from_loose_version should raise an exception when given a non-LooseVersion"

# Generated at 2022-06-13 16:59:23.275819
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha('foo') <= _Alpha('foo')
    assert _Alpha('foo') <= _Alpha('bar')
    assert _Alpha('bar') <= _Alpha('foo')

    assert _Alpha('foo') <= 'foo'
    assert _Alpha('foo') <= 'bar'
    assert _Alpha('bar') <= 'foo'

    assert not _Alpha('foo') <= '1'
    assert _Alpha('1') <= '1'
    assert _Alpha('1') <= '0'

    assert _Alpha('1') <= 1
    assert _Alpha('0') <= 1

    assert not _Alpha('1') <= 0
    assert not _Alpha('0') <= 0


# Generated at 2022-06-13 16:59:28.839584
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Check when version is a non valid format
    version = "1.2.3xxxx"
    result = False
    try:
        SemanticVersion.from_loose_version(version)
    except ValueError:
        result = True
    assert result == True

    # Valid string
    version = "1.2.3"
    result = False
    try:
        SemanticVersion.from_loose_version(version)
    except ValueError:
        result = True
    assert result == False

    # Valid string with prerelease
    version = "1.2.3-2"
    result = False
    try:
        SemanticVersion.from_loose_version(version)
    except ValueError:
        result = True
    assert result == False

    # Valid string with buildmetadata

# Generated at 2022-06-13 16:59:41.461924
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # These tests are taken from tests of distutils.version.LooseVersion
    # and modified to use SemanticVersion instead

    from ansible.module_utils.version import SemanticVersion

    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')).vstring == '1.2.3'
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.0')).vstring == '1.2.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.02.0')).vstring == '1.2.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.2')).vstring == '1.2.0'

# Generated at 2022-06-13 16:59:54.667173
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    Assert that ``SemanticVersion.from_loose_version`` work properly.
    """
    assert SemanticVersion.from_loose_version('1.2.3') == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version('1.2.3-beta1') == SemanticVersion('1.2.3-beta1')
    assert SemanticVersion.from_loose_version('1.2.3+build1') == SemanticVersion('1.2.3+build1')

    # Non-version strings should raise an error
    try:
        SemanticVersion.from_loose_version('test')
        raise AssertionError('SemanticVersion.from_loose_version() accepted an invalid version string')
    except ValueError:
        pass

# Generated at 2022-06-13 17:00:03.882255
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    The method from_loose_version of class SemanticVersion
    should construct a SemanticVersion from a LooseVersion
    """
    # Check for version format supported by LooseVersion
    # https://docs.python.org/3/library/distutils.version.html#distutils.version.LooseVersion.version

# Generated at 2022-06-13 17:00:09.487323
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    # This is the function you are testing
    # Replace "pass" with the body of the function
    assert _Alpha("A").__le__("A")
    assert _Alpha("A").__le__("aaa")
    assert _Alpha("B").__le__("A") == False


# Generated at 2022-06-13 17:00:19.581716
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test string values
    value = '1.2.3'
    loose_version = LooseVersion(value)
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.major == 1
    assert semantic_version.minor == 2
    assert semantic_version.patch == 3

    # Test list values
    value = ['1', '2', '3']
    loose_version = LooseVersion(value)
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.major == 1
    assert semantic_version.minor == 2
    assert semantic_version.patch == 3

    # Test int values
    value = [1, 2, 3]
    loose_version = LooseVersion(value)
    semantic_version

# Generated at 2022-06-13 17:00:23.276028
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    # Success case
    _Alpha('z') <= _Alpha('abc')
    # Failure case
    caught = None
    try:
        _Alpha('abc') <= _Alpha('z')
    except ValueError:
        caught = True
    assert caught

# Generated at 2022-06-13 17:00:26.014040
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha("a") <= _Alpha("a")
    assert _Alpha("a") <= _Alpha("b")
    assert not _Alpha("b") <= _Alpha("a")


# Generated at 2022-06-13 17:00:37.332008
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(None)

    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version('')

    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(LooseVersion(''))

    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(Text(''))

    # Test non-integer loose versions
    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(LooseVersion('a.b.c'))

    # Test non-integer loose versions

# Generated at 2022-06-13 17:00:50.012825
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # SemanticVersion(vstring)
    v1 = SemanticVersion('1.0.0')
    # LooseVersion(vstring=None)
    # LooseVersion(version)
    # LooseVersion(version=None)
    v2 = LooseVersion(str(v1))
    # LooseVersion(version=None)
    v3 = LooseVersion()
    # LooseVersion(version)
    v4 = LooseVersion(v2)
    assert v1 == v2
    assert v4 == v2
    assert v1 != v3
    # LooseVersion.__init__(self, vstring)
    v5 = LooseVersion('1.0.0-alpha')
    # LooseVersion.__init__(self, version)
    v6 = LooseVersion(v5)
    v7

# Generated at 2022-06-13 17:00:58.519705
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion('1.2.3-alpha.1').vstring == str(SemanticVersion.from_loose_version('1.2.3-alpha.1'))
    assert SemanticVersion('1.2.3-alpha.001').vstring == str(SemanticVersion.from_loose_version('1.2.3-alpha.1'))
    assert SemanticVersion('1.2.3.alpha.1').vstring == str(SemanticVersion.from_loose_version('1.2.3-alpha.1'))
    assert SemanticVersion('1.2.3').vstring == str(SemanticVersion.from_loose_version('1.2.3'))
    assert SemanticVersion('1.2').vstring == str(SemanticVersion.from_loose_version('1.2'))

# Generated at 2022-06-13 17:01:05.555176
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3a5')) == SemanticVersion('1.2.3-a5')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3.4.5')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2')) == SemanticVersion('1.2.0')

# Generated at 2022-06-13 17:01:18.192348
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion, StrictVersion

    # Single integers
    assert str(LooseVersion('1')) == '1'
    assert str(StrictVersion('1')) == '1'
    assert str(SemanticVersion.from_loose_version(LooseVersion('1'))) == '1.0.0'
    assert str(SemanticVersion.from_loose_version(StrictVersion('1'))) == '1.0.0'

    # Multiple integers separated by '.'
    assert str(LooseVersion('1.2.3')) == '1.2.3'
    assert str(StrictVersion('1.2.3')) == '1.2.3'

# Generated at 2022-06-13 17:01:27.435388
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # Test base input
    loose_version = '1.1.14'
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.core == (1, 1, 14)

    # Test with prepend
    loose_version = '.1.14'
    semantic_version = SemanticVersion.from_loose_version('0'+loose_version)
    assert semantic_version.core == (0, 1, 14)

    # Test with prepend
    loose_version = '..14'
    semantic_version = SemanticVersion.from_loose_version('0'+loose_version)
    assert semantic_version.core == (0, 0, 14)

    # Test with prepend
    loose_version = '..'

# Generated at 2022-06-13 17:01:39.392764
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    def check(loose_str, semver_str):
        loose_version = LooseVersion(loose_str)
        assert SemanticVersion.from_loose_version(loose_version) == SemanticVersion(semver_str)

    check("0.0.0", "0.0.0")
    check("1.2.3", "1.2.3")
    check("1.2.3.dev0", "1.2.3-0")
    check("1.2.3.dev0+1234", "1.2.3-0+1234")
    check("1.2.3.dev1+1234", "1.2.3-1+1234")
    check("1.2.3a0", "1.2.3-a0")

# Generated at 2022-06-13 17:01:47.651275
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version_pairs = {
        "1.0.0": "1.0.0",
        "1.0.0-alpha": "1.0.0-alpha",
        "1.0.0+git": "1.0.0+git",
        "1.0.0-alpha+git": "1.0.0-alpha+git",
    }

    for loose_version, expected_semver in loose_version_pairs.items():
        assert SemanticVersion.from_loose_version(LooseVersion(loose_version)).vstring == expected_semver, \
            "Error: expected {} to be converted to {}".format(loose_version, expected_semver)


# Generated at 2022-06-13 17:01:58.847853
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('0.2.dev6')) == SemanticVersion('0.2.0')
    assert SemanticVersion.from_loose_version(LooseVersion('2.5.0')) == SemanticVersion('2.5.0')
    assert SemanticVersion.from_loose_version(LooseVersion('3.1.1.dev3')) == SemanticVersion('3.1.1')
    assert SemanticVersion.from_loose_version(LooseVersion('0.2.dev6-SKIP_THIS_PART')) == SemanticVersion('0.2.0')
    assert SemanticVersion.from_loose_version(LooseVersion('2.5.0-SKIP_THIS_PART')) == SemanticVersion('2.5.0')


# Generated at 2022-06-13 17:02:06.811914
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:02:39.501228
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test python2
    if hasattr(text_type, 'startswith'):
        test_version_string = "0.0.1"
        test_loose_version = LooseVersion(test_version_string)
        assert(test_version_string == test_loose_version)
        semver_from_loose_version = SemanticVersion.from_loose_version(test_loose_version)
        semver_from_string = SemanticVersion(test_version_string)
        assert(semver_from_string == semver_from_loose_version)

# Generated at 2022-06-13 17:02:43.541916
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    resultat_attendu = SemanticVersion('1.2.3')
    resultat_obtenu = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    assert resultat_attendu == resultat_obtenu


# Generated at 2022-06-13 17:02:51.914492
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Python 2
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.1')) == SemanticVersion('1.0.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.1.0')) == SemanticVersion('1.1.0')
    assert SemanticVersion.from_loose_version(LooseVersion('2.0.0')) == SemanticVersion('2.0.0')

    # Python 3
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_lo

# Generated at 2022-06-13 17:03:03.816072
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:03:14.176388
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:03:24.247659
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    Unit test for method from_loose_version of class SemanticVersion
    """

# Generated at 2022-06-13 17:03:35.729874
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.distro import LooseVersion

    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-1')) == SemanticVersion('1.0.0-1')

# Generated at 2022-06-13 17:03:44.604130
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    with pytest.raises(ValueError) as err:
        SemanticVersion.from_loose_version(1.2)
        assert str(err.value) == "1.2 is not a LooseVersion"
        SemanticVersion.from_loose_version(LooseVersion('1.2'))
        assert isinstance(SemanticVersion.from_loose_version(LooseVersion('1.2')), SemanticVersion)
        SemanticVersion.from_loose_version(LooseVersion('1.2.3.4'))
        SemanticVersion.from_loose_version(LooseVersion('1.2.3.4.5.6.7.8'))
        SemanticVersion.from_loose_version(LooseVersion('1.2.3.a'))

# Generated at 2022-06-13 17:03:50.317729
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3pre')) == SemanticVersion('1.2.3-pre')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+build')) == SemanticVersion('1.2.3+build')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3pre+build')) == SemanticVersion('1.2.3-pre+build')
    assert SemanticVersion.from_loose_version(LooseVersion('')) == SemanticVersion('0.0.0')


# Generated at 2022-06-13 17:03:54.847739
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    vstring = "my_package-1.0.0-alpha+build_1"

    loose_version = LooseVersion(vstring)
    semantic_version = SemanticVersion.from_loose_version(loose_version)

    assert isinstance(semantic_version, SemanticVersion)
    assert semantic_version.vstring == vstring

# Generated at 2022-06-13 17:04:10.080382
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.common.version import SemanticVersion
    from ansible.module_utils.common.version import LooseVersion
    
    vstring = '1.1.1'
    loose_version = LooseVersion(vstring)

    try:
        # test without a LooseVersion
        version = SemanticVersion.from_loose_version('1.1.1')
        assert False
    except ValueError:
        pass

    try:
        # test with a LooseVersion that has non integer values
        version = SemanticVersion.from_loose_version(LooseVersion(vstring + 'a'))
        assert False
    except ValueError:
        pass

    # test with a valid loose version that do not have a prerelease or build metadata

# Generated at 2022-06-13 17:04:21.102186
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    versions = {
        LooseVersion('1.0.0'): SemanticVersion('1.0.0'),
        LooseVersion('1.2.3.final'): SemanticVersion('1.2.3'),
        LooseVersion('1.2.3.post1'): SemanticVersion('1.2.3'),
        LooseVersion('1.4-alpha1'): SemanticVersion('1.4.0-alpha1'),
        LooseVersion('1.4.0.dev4'): SemanticVersion('1.4.0'),
        LooseVersion('1.6-beta.11'): SemanticVersion('1.6.0-beta.11'),
    }

    for loose_version, semantic_version in versions.items():
        assert SemanticVersion.from_loose_version(loose_version) == semantic

# Generated at 2022-06-13 17:04:29.232896
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import datetime
    class MockLooseVersion():
        def __init__(self, vstring):
            self.vstring = vstring
            self.version = vstring

    # Test case with correct arguments
    loose_version = MockLooseVersion("1.8.1")
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert(semantic_version.core == (1, 8, 1))
    assert(semantic_version.prerelease == ())

    # Test case with wrong arguments
    with pytest.raises(ValueError) as excinfo:
        SemanticVersion.from_loose_version("Something")
    assert "Something is not a LooseVersion" in str(excinfo.value)

    # Test case with different version markers

# Generated at 2022-06-13 17:04:35.544261
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import sys
    semanticVersionObject = SemanticVersion()
    loose_version = LooseVersion('1.0.0')
    if sys.version_info[0] == 2:
        assert(semanticVersionObject.from_loose_version(loose_version).vstring == '1.0.0')
    else:
        assert(semanticVersionObject.from_loose_version(loose_version).vstring == '1.0.0')

# Generated at 2022-06-13 17:04:48.671599
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion
    version1 = LooseVersion("2.2.2rc3")
    version2 = SemanticVersion.from_loose_version(version1)
    assert version2.vstring == "2.2.2-rc3"

    version3 = LooseVersion("2.2.2rc3+20130313144700")
    version4 = SemanticVersion.from_loose_version(version3)
    assert version4.vstring == "2.2.2-rc3+20130313144700"

    version5 = LooseVersion("1.0b0")
    version6 = SemanticVersion.from_loose_version(version5)
    assert version6.vstring == "1.0.0-b0"


# Generated at 2022-06-13 17:04:56.036583
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    s = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    assert s.vstring == '1.2.3'

    s = SemanticVersion.from_loose_version(LooseVersion('1.2.3.4'))
    assert s.vstring == '1.2.3.4'

    s = SemanticVersion.from_loose_version(LooseVersion('1.2.3.4-alpha'))
    assert s.vstring == '1.2.3.4-alpha'

    s = SemanticVersion.from_loose_version(LooseVersion('1.2.3.4-1.alpha'))
    assert s.vstring == '1.2.3.4-1.alpha'

    s = SemanticVersion.from_loose

# Generated at 2022-06-13 17:05:08.298391
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:05:12.643196
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    new_semver = SemanticVersion.from_loose_version(LooseVersion("1.2.3.post1.dev2"))
    print(new_semver)


# Generated at 2022-06-13 17:05:21.886962
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0a1')) == SemanticVersion('1.0.0-a1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0b2')) == SemanticVersion('1.0.0-b2')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0c3')) == SemanticVersion('1.0.0-c3')

# Generated at 2022-06-13 17:05:32.822904
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    loose_version = LooseVersion('1.2.3-alpha+bravo')
    semantic_version = SemanticVersion.from_loose_version(loose_version)

    assert text_type(semantic_version) == '1.2.3-alpha+bravo'

    loose_version = LooseVersion('1.2.3-alpha')
    semantic_version = SemanticVersion.from_loose_version(loose_version)

    assert text_type(semantic_version) == '1.2.3-alpha'

    loose_version = LooseVersion('1.2.3-1')
    semantic_version = SemanticVersion.from_loose_version(loose_version)

    assert text_type(semantic_version) == '1.2.3-1'


# Generated at 2022-06-13 17:06:00.402578
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from distutils.version import LooseVersion

    # Test a version that does not have a prerelease or build metadata
    assert(SemanticVersion.from_loose_version(LooseVersion('1.2.3')) ==
        SemanticVersion('1.2.3'))

    # Test a version that has a prerelease
    assert(SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.1')) ==
        SemanticVersion('1.2.3-alpha.1'))

    # Test a version that has a prerelease and build metadata

# Generated at 2022-06-13 17:06:07.570342
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Simple test
    loose_version = LooseVersion('1.2.3')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '1.2.3'

    # Using a custom separator
    loose_version = LooseVersion('1:2:3')
    semver = SemanticVersion.from_loose_version(loose_version, sep=':')
    assert semver == '1.2.3'

    # Using a custom suffix
    loose_version = LooseVersion('1_2_3dev')
    semver = SemanticVersion.from_loose_version(loose_version, suffix='dev')
    assert semver == '1.2.3-dev'

    # Using a suffix that is not a viable prerelease

# Generated at 2022-06-13 17:06:18.565966
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3.4')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha')) == SemanticVersion('1.2.3-alpha')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.1')) == SemanticVersion('1.2.3-alpha.1')

# Generated at 2022-06-13 17:06:20.927171
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('1.10.5')
    assert isinstance(SemanticVersion.from_loose_version(loose_version), SemanticVersion)


# Generated at 2022-06-13 17:06:28.173601
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # invalid LooseVersion
    try:
        SemanticVersion.from_loose_version('0.0.0')
    except ValueError:
        pass
    else:
        assert False, 'Exception not raised'

    assert SemanticVersion.from_loose_version(
        LooseVersion('0.0.0.dev0')
    ) == SemanticVersion('0.0.0-dev0')

    assert SemanticVersion.from_loose_version(
        LooseVersion('1.0.1')
    ) == SemanticVersion('1.0.1')

    assert SemanticVersion.from_loose_version(
        LooseVersion('1.0.1.dev1')
    ) == SemanticVersion('1.0.1-dev1')


# Generated at 2022-06-13 17:06:37.371477
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # all test cases are from https://semver.org/#spec-item-11
    # Test Case 1
    input_vstring = '1.0.0-alpha'
    loose_version = LooseVersion(input_vstring)
    new_semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert new_semantic_version > '1.0.0'
    assert new_semantic_version < '1.0.0-alpha.1'
    assert new_semantic_version < '1.0.0-beta'

    # Test Case 2
    input_vstring = '1.0.0-alpha.1'
    loose_version = LooseVersion(input_vstring)

# Generated at 2022-06-13 17:06:45.143768
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion
    lv_str = "2.7.0.0-1.el7"
    loose_v = LooseVersion(lv_str)
    semver = SemanticVersion.from_loose_version(loose_v)
    assert semver.__str__().startswith(lv_str)


# Unit tests for class SemanticVersion

# Generated at 2022-06-13 17:06:49.798205
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version('1') == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version('1.2') == SemanticVersion('1.2.0')
    assert SemanticVersion.from_loose_version('1.2.3') == SemanticVersion('1.2.3')

# Generated at 2022-06-13 17:06:56.867144
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v = SemanticVersion.from_loose_version(LooseVersion('0.1.2'))
    assert v == SemanticVersion('0.1.2')

    v = SemanticVersion.from_loose_version(LooseVersion('2.0.1.dev1'))
    assert v == SemanticVersion('2.0.1-dev1')

    v = SemanticVersion.from_loose_version(LooseVersion('2.0.1.dev1+abc.1'))
    assert v == SemanticVersion('2.0.1-dev1+abc.1')

    with pytest.raises(ValueError):
        v = SemanticVersion.from_loose_version('2.0.1.dev1')

# Generated at 2022-06-13 17:07:08.825351
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
       This function tests SemanticVersion.from_loose_version function.
       It tests that only loose version is accepted and both basic and
       full version is correctly parsed.

       Argument:
          None

       Return:
          None

       Raise:
          AssertError if functions don't work as expected
    """
    assert SemanticVersion.from_loose_version(LooseVersion("1.3.3")).vstring == "1.3.3"
    assert SemanticVersion.from_loose_version(LooseVersion("2.2-rc")).vstring == "2.2.0-rc"

    try:
        SemanticVersion.from_loose_version("2.2-rc")
        assert False
    except:
        assert True

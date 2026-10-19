

# Generated at 2022-06-13 16:57:35.047310
# Unit test for method parse of class SemanticVersion

# Generated at 2022-06-13 16:57:43.081186
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    """
    Should return True when specifier of other class is equal to specifier of class
    Should return True when specifier of other class is less than specifier of class
    Should return False when specifier of other class is greater than specifier of class
    Should return False when specifier of other class is not equal to specifier of class
    """

    assert _Alpha("a")._Alpha__le__(_Alpha("a")) == True
    assert _Alpha("a")._Alpha__le__(_Alpha("b")) == True
    assert _Alpha("b")._Alpha__le__(_Alpha("a")) == False
    assert _Alpha("a")._Alpha__le__(_Alpha("c")) == False


# Generated at 2022-06-13 16:57:46.233649
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    vstring = '0.1.2'
    semver = SemanticVersion()
    semver.parse(vstring)
    assert semver.major == 0
    assert semver.minor == 1
    assert semver.patch == 2


# Generated at 2022-06-13 16:57:50.602794
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion("1.2.3-alpha1")
    version = SemanticVersion.from_loose_version(loose_version)
    assert version == "1.2.3-alpha1"

    loose_version = LooseVersion("1.2.3")
    version = SemanticVersion.from_loose_version(loose_version)
    assert version == "1.2.3"

    try:
        loose_version = LooseVersion("1.2a.3")
        version = SemanticVersion.from_loose_version(loose_version)
        assert False
    except ValueError:
        assert True


# Generated at 2022-06-13 16:58:04.138757
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    class A(object):
        def __init__(self, vstring):
            self.vstring = vstring

    # Test that exception is raised on wrong object
    try:
        SemanticVersion.from_loose_version(A('test'))
    except Exception as e:
        pass
    else:
        assert False

    # Test that exception is raised on non integer values
    try:
        SemanticVersion.from_loose_version(LooseVersion('test'))
    except Exception as e:
        pass
    else:
        assert False

    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')

# Generated at 2022-06-13 16:58:18.110865
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
  # Success cases
  testResult = SemanticVersion.from_loose_version("1.0")
  assert testResult == SemanticVersion("1.0.0")
  testResult = SemanticVersion.from_loose_version("1.1")
  assert testResult == SemanticVersion("1.1.0")
  testResult = SemanticVersion.from_loose_version("1.1.1")
  assert testResult == SemanticVersion("1.1.1")
  testResult = SemanticVersion.from_loose_version("1.0+alpha")
  assert testResult == SemanticVersion("1.0.0+alpha")
  testResult = SemanticVersion.from_loose_version("1.1+alpha")
  assert testResult == SemanticVersion("1.1.0+alpha")

# Generated at 2022-06-13 16:58:28.355997
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    Semver = SemanticVersion
    assert Semver.from_loose_version(LooseVersion('1.2.3')) == Semver('1.2.3') == Semver('1.2.3-0') == Semver('1.2.3-0.0') == Semver('1.2.3-0.0.0.0')
    assert Semver.from_loose_version(LooseVersion('1.2.3+build')) == Semver('1.2.3+build')
    assert Semver.from_loose_version(LooseVersion('1.2.3-alpha')) == Semver('1.2.3-alpha')

# Generated at 2022-06-13 16:58:36.135701
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test with a valid LooseVersion as input
    assert SemanticVersion(vstring='1.0.0') == SemanticVersion.from_loose_version(
        LooseVersion('1.0.0')
    )

    # Test with an invalid LooseVersion as input
    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(
            LooseVersion('1.0')
        )



# Generated at 2022-06-13 16:58:44.792223
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    def parse(version, expected=None):
        if expected is None:
            expected = {}
        expected.setdefault('major', 0)
        expected.setdefault('minor', 0)
        expected.setdefault('patch', 0)
        expected.setdefault('prerelease', ())
        expected.setdefault('buildmetadata', ())
        sv = SemanticVersion(version)
        assert sv.major == expected['major']
        assert sv.minor == expected['minor']
        assert sv.patch == expected['patch']
        assert sv.prerelease == expected['prerelease']
        assert sv.buildmetadata == expected['buildmetadata']

    parse('1.2.3')
    parse('1.2', {
        'major': 1,
        'minor': 2,
    })

# Generated at 2022-06-13 16:58:54.259722
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    semver = SemanticVersion()
    assert semver.parse('1.2.3') == None
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3
    assert semver.prerelease == ()
    assert semver.buildmetadata == ()

    semver = SemanticVersion()
    assert semver.parse('1.2.3-rc1') == None
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3
    assert semver.prerelease == (_Numeric('rc1'),)
    assert semver.buildmetadata == ()

    semver = SemanticVersion()
    assert semver.parse('1.2.3-rc1.0') == None
    assert semver.major == 1
    assert semver

# Generated at 2022-06-13 16:59:12.244125
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    try:
        v = SemanticVersion.from_loose_version("2.2.1")
        assert v == SemanticVersion("2.2.1"), \
            "Unexpected result for SemanticVersion.from_loose_version"
        assert v.is_stable, \
            "Unexpected result for SemanticVersion.from_loose_version"
    except ValueError:
        v = None
        assert False, \
            "Unexpected result for SemanticVersion.from_loose_version"


# Generated at 2022-06-13 16:59:24.212123
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    s = SemanticVersion.from_loose_version(LooseVersion("1.2.3a4~n5"))
    assert s.major == 1
    assert s.minor == 2
    assert s.patch == 3
    assert s.prerelease == (_Alpha("a"), _Numeric("4"), _Alpha("~"), _Alpha("n"), _Numeric("5"))
    assert s.buildmetadata == ()
    s = SemanticVersion.from_loose_version(LooseVersion("1.2.3a4~n5+6.7.8~b9"))
    assert s.major == 1
    assert s.minor == 2
    assert s.patch == 3
    assert s.prerelease == (_Alpha("a"), _Numeric("4"), _Alpha("~"), _Alpha("n"), _Numeric("5"))
   

# Generated at 2022-06-13 16:59:32.413509
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test for correct behavior given correct input
    loose_ver1 = LooseVersion("2.0.0")
    exp_ver1 = SemanticVersion("2.0.0")
    # Test that this method works with extra metadata
    loose_ver2 = LooseVersion("2.0.0+a.b.c.d")
    exp_ver2 = SemanticVersion("2.0.0+a.b.c.d")
    # Test that this method works with extra metadata and a prerelease tag
    loose_ver3 = LooseVersion("2.0.0-a.b.c.d+a.b.c.d")
    exp_ver3 = SemanticVersion("2.0.0-a.b.c.d+a.b.c.d")
    # Test that the method can handle two loose versions and

# Generated at 2022-06-13 16:59:44.904307
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.version import SemanticVersion
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.compat.version import (LooseVersion, Version)
    import sys
    import os


# Generated at 2022-06-13 16:59:57.654509
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion

    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3pre')) == SemanticVersion('1.2.3-pre')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3post')) == SemanticVersion('1.2.3-post')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3.dev')) == SemanticVersion('1.2.3-dev')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2b3')) == SemanticVersion('1.2.0-b3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2c3'))

# Generated at 2022-06-13 17:00:06.221121
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test without prerelease and buildmetadata
    assert SemanticVersion('1.0.0') == SemanticVersion.from_loose_version(LooseVersion('1.0.0'))

    # Test without prerelease and with buildmetadata
    assert SemanticVersion('1.0.0+build') == SemanticVersion.from_loose_version(LooseVersion('1.0.0+build'))

    # Test with prerelease and without buildmetadata
    assert SemanticVersion('1.0.0-pre') == SemanticVersion.from_loose_version(LooseVersion('1.0.0-pre'))

    # Test with prerelease and buildmetadata

# Generated at 2022-06-13 17:00:16.093429
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v1 = LooseVersion("1.2.3.dev2+ge2da8e0")
    v2 = SemanticVersion("1.2.3.dev2+ge2da8e0")
    assert v1 != v2
    v1 = SemanticVersion.from_loose_version(v1)
    assert v1 == v2
    try:
        v1 = "1.2.3.dev2+ge2da8e0"
        v1 = SemanticVersion.from_loose_version(v1)
    except ValueError as e:
        assert "LooseVersion" in text_type(e)
    else:
        assert False



# Generated at 2022-06-13 17:00:25.893220
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    Validate that SemanticVersion.from_loose_version() can convert
    from distutils.version.LooseVersion to ansible.module_utils.semver.SemanticVersion
    """
    from ansible.module_utils.common.version import LooseVersion as lv

    lv_to_sv = dict()
    lv_to_sv['1.2.3'] = '1.2.3'
    lv_to_sv['1.2.3.4'] = '1.2.3'
    lv_to_sv['1.2.3.4.5'] = '1.2.3'
    lv_to_sv['1.2.3-1.2.3'] = '1.2.3-1.2.3'

# Generated at 2022-06-13 17:00:29.915442
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Test method from_loose_version of class SemanticVersion

    """

    # Test single value inputs
    for vstring in ('0', '1', '3', '11', '23', '55', '66'):
        version = SemanticVersion.from_loose_version(LooseVersion(vstring))
        assert isinstance(version, SemanticVersion), "vstring = %r, type is %r" % (vstring, type(version))
        assert version == vstring, "vstring = %r, version = %r" % (vstring, version)
        assert version.core == (int(vstring), 0, 0), "vstring = %r, version = %r" % (vstring, version)

    # Test double value inputs

# Generated at 2022-06-13 17:00:38.446403
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.common._semver import SemanticVersion
    from ansible.module_utils.common._json_compat import json

    lv = SemanticVersion.from_loose_version(LooseVersion('4.4.4'))
    assert lv.is_stable

    lv = SemanticVersion.from_loose_version(LooseVersion('4.4.4-beta'))
    assert not lv.is_stable
    assert lv.prerelease == ('beta',)

    lv = SemanticVersion.from_loose_version(LooseVersion('4.4.4-beta.1.2.3'))
    assert not lv.is_stable
    assert lv.prerelease == ('beta', '1', '2', '3')



# Generated at 2022-06-13 17:00:51.183772
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.1.1+build.0')) == SemanticVersion('1.1.1+build.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.1.1-alpha-0')) == SemanticVersion('1.1.1-alpha-0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.1.1')) == SemanticVersion('1.1.1')

# Generated at 2022-06-13 17:00:55.000600
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    sv = SemanticVersion()
    sv.parse('1.2.0')
    assert sv.major == 1
    assert sv.minor == 2
    assert sv.patch == 0
    assert not sv.prerelease
    assert not sv.buildmetadata
    assert sv.vstring == '1.2.0'



# Generated at 2022-06-13 17:01:03.173173
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Unit test for method ``from_loose_version`` of class SemanticVersion"""
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+dev')) == SemanticVersion('1.0.0+dev')
    assert SemanticVersion.from_loose_version(LooseVersion('1.7.1')) == SemanticVersion('1.7.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.7')) == SemanticVersion('1.7.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.3.2')) == SemanticVersion('1.3.2')


# Generated at 2022-06-13 17:01:15.138672
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    from ansible.module_utils.common.version import SemanticVersion, SemanticVersionRange
    import ansible.module_utils.six as six
    import copy

    loose_version = SemanticVersion('1.2.3-beta.1')

    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.major == 1
    assert semantic_version.minor == 2
    assert semantic_version.patch == 3
    assert len(semantic_version.prerelease) == 2
    assert semantic_version.prerelease == tuple([_Alpha('beta'), _Numeric('1')])

    loose_version = SemanticVersion(six.u('1.2.3-beta.1'))

    semantic_version = SemanticVersion.from_loose_version(loose_version)
   

# Generated at 2022-06-13 17:01:25.425722
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test version number conversion
    assert SemanticVersion.from_loose_version(
        LooseVersion('1')
    ) == SemanticVersion('1.0.0')

    assert SemanticVersion.from_loose_version(
        LooseVersion('1.0')
    ) == SemanticVersion('1.0.0')

    assert SemanticVersion.from_loose_version(
        LooseVersion('1.0.0')
    ) == SemanticVersion('1.0.0')

    assert SemanticVersion.from_loose_version(
        LooseVersion('1.2.3')
    ) == SemanticVersion('1.2.3')

    # Test extra_idx
    assert SemanticVersion.from_loose_version(
        LooseVersion('1.2.3-rc')
    )

# Generated at 2022-06-13 17:01:30.807272
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('2.3')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    equivalent_semantic_version = SemanticVersion('2.3.0')
    assert equivalent_semantic_version == semantic_version

# Generated at 2022-06-13 17:01:41.803411
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    assert str(SemanticVersion.from_loose_version(LooseVersion('1.2.3'))) == '1.2.3'
    assert str(SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.4.5+foo.bar'))) == '1.2.3-alpha.4.5+foo.bar'

    try:
        SemanticVersion.from_loose_version(1)
    except ValueError:
        pass
    else:
        assert False, 'Should have failed'

    try:
        SemanticVersion.from_loose_version('1.2.3')
    except ValueError:
        pass
    else:
        assert False, 'Should have failed'


# Generated at 2022-06-13 17:01:51.465156
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Test method ``from_loose_version`` of class ``SemanticVersion``

    validate return object of class ``SemanticVersion``
    """
    # Create SemanticVersion object from LooseVersion
    # input
    semver_obj = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))

    # assert isinstance of class ``SemanticVersion``
    # class object
    assert isinstance(semver_obj, SemanticVersion)

    # assert core version
    # 1.2.3
    assert semver_obj.major == 1
    assert semver_obj.minor == 2
    assert semver_obj.patch == 3

    # assert prerelease and buildmetadata attributes
    # empty sequence
    assert semver_obj.prerelease == tuple()

# Generated at 2022-06-13 17:02:01.546804
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    version = LooseVersion('1.0.1')
    assert SemanticVersion.from_loose_version(version).vstring == '1.0.1'
    version = LooseVersion('1.0.1.dev1')
    assert SemanticVersion.from_loose_version(version).vstring == '1.0.1-dev1'

    # Should raise ValueError because version is not a LooseVersion
    version = '1.0.1'
    try:
        SemanticVersion.from_loose_version(version)
    except ValueError as e:
        assert str(e) == "'%s' is not a LooseVersion" % version
    else:
        raise ValueError("'%s' is not a LooseVersion but no exception raised" % version)

    # Should raise ValueError because version has non-

# Generated at 2022-06-13 17:02:13.292954
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Provided input
    class Input:
        def __init__(self, input, expected):
            self.input = input
            self.expected = expected

    # Test cases

# Generated at 2022-06-13 17:02:30.846239
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # General case
    loose_version = LooseVersion("1.2.3")
    version = SemanticVersion.from_loose_version(loose_version)
    assert version == "1.2.3"

    # General case with negative values
    loose_version = LooseVersion("-1.2.3")
    version = SemanticVersion.from_loose_version(loose_version)
    assert version == "-1.2.3"

    # General case with alpha values
    loose_version = LooseVersion("1.2.b")
    version = SemanticVersion.from_loose_version(loose_version)
    assert version == "1.2.0"

    # General case with alpha values (negative)
    loose_version = LooseVersion("-1.2.b")
    version = Semantic

# Generated at 2022-06-13 17:02:42.822410
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3.4')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-rc1')) == SemanticVersion('1.2.3-rc1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-rc1.2.3')) == SemanticVersion('1.2.3-rc1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-rc1.2.3.4'))

# Generated at 2022-06-13 17:02:51.407933
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Check if the method returns a SemanticVersion object
    loose_version = LooseVersion('2.0.dev.1')
    v1 = SemanticVersion.from_loose_version(loose_version)
    assert isinstance(v1, Version) is True

    # Check if the method returns the correct SemanticVersion object
    loose_version = LooseVersion('2.0.dev.1')
    v1 = SemanticVersion.from_loose_version(loose_version)
    expected_v1 = SemanticVersion('2.0.0-dev.1')
    assert v1 == expected_v1

    loose_version = LooseVersion('2.0.dev.1.1.2')
    v2 = SemanticVersion.from_loose_version(loose_version)
    expected_v2 = Sem

# Generated at 2022-06-13 17:03:03.705179
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion
    # Test for ints
    for v in ((1, 2, 3), (1, 2, 3, 4)):
        loose_version = LooseVersion('.'.join(str(v) for v in v))
        expected = SemanticVersion('.'.join(str(v) for v in v))
        assert expected == SemanticVersion.from_loose_version(loose_version)

    # Test for ints + alpha
    for v in (('1', '2', '3', 'alpha'), ('1', '2', '3', 'alpha', 'beta')):
        loose_version = LooseVersion('.'.join(str(v) for v in v))
        expected = SemanticVersion('.'.join(str(v) for v in v))


# Generated at 2022-06-13 17:03:12.181840
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Load the method of class SemanticVersion
    method = SemanticVersion.from_loose_version

    # Test method
    assert method(LooseVersion('2019.5.6')) == SemanticVersion('2019.5.6')
    assert method(LooseVersion('2019.5.6.0')) == SemanticVersion('2019.5.6')
    assert method(LooseVersion('2019.5.6.5')) == SemanticVersion('2019.5.6')
    assert method(LooseVersion('2019.5.6-a')) == SemanticVersion('2019.5.6-a')
    assert method(LooseVersion('2019.5.6-a+foo')) == SemanticVersion('2019.5.6-a+foo')

# Generated at 2022-06-13 17:03:23.380626
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:03:30.295621
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.1b')) == SemanticVersion('1.2.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.1-dev')) == SemanticVersion('1.2.1-dev')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.1.post2.dev4')) == SemanticVersion('1.2.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.1+foo.bar')) == SemanticVersion('1.2.1')
    assert Semantic

# Generated at 2022-06-13 17:03:39.193495
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    def compare_loose_and_semantic(loose_version):
        try:
            loose_version = LooseVersion(loose_version)
        except ValueError:
            return False
        try:
            semantic_version = SemanticVersion.from_loose_version(loose_version)
        except ValueError:
            return False
        return loose_version == semantic_version

    assert compare_loose_and_semantic('1.2') == True
    assert compare_loose_and_semantic('1.2.3') == True
    assert compare_loose_and_semantic('1.2.3-alpha.1') == True
    assert compare_loose_and_semantic('1.2.3+build.1') == True

# Generated at 2022-06-13 17:03:49.769622
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # Test with valid values
    loose_version = LooseVersion('1.0.0')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.major == 1
    assert semantic_version.minor == 0
    assert semantic_version.patch == 0

    loose_version = LooseVersion('1.0.0-pre.1')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.version == '1.0.0-pre.1'

    loose_version = LooseVersion('1.0.0+build.1')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.version == '1.0.0+build.1'

# Generated at 2022-06-13 17:03:57.476331
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v1 = SemanticVersion.from_loose_version(LooseVersion('1'))
    assert v1 == SemanticVersion('1.0.0')

    v2 = SemanticVersion.from_loose_version(LooseVersion('3.2.1-rc'))
    assert v2 == SemanticVersion('3.2.1-rc.0')

    v3 = SemanticVersion.from_loose_version(LooseVersion('1.2.3-11'))
    assert v3 == SemanticVersion('1.2.3-11.0')

    v4 = SemanticVersion.from_loose_version(LooseVersion('0.0.1.dev1'))
    assert v4 == SemanticVersion('0.0.1-dev1.0')

    v5 = SemanticVersion.from_lo

# Generated at 2022-06-13 17:04:23.826015
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:04:27.463221
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version_str = "Release_version_informatica-9.6.1-0"
    release_version = SemanticVersion.from_loose_version(LooseVersion(loose_version_str))
    assert release_version.vstring == "9.6.1"

# Generated at 2022-06-13 17:04:37.562049
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    semantic_version = SemanticVersion.from_loose_version(LooseVersion('3.4.0-1'))
    assert semantic_version == '3.4.0-1'
    assert isinstance(semantic_version, SemanticVersion)
    assert isinstance(semantic_version, Version)

    semantic_version = SemanticVersion.from_loose_version(LooseVersion('3.4.0+1'))
    assert semantic_version == '3.4.0'
    assert isinstance(semantic_version, SemanticVersion)
    assert isinstance(semantic_version, Version)

    semantic_version = SemanticVersion.from_loose_version(LooseVersion('3.4.0-1.2.3'))
    assert semantic_version == '3.4.0-1.2.3'

# Generated at 2022-06-13 17:04:49.917925
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six import PY2

    # LooseVersion is not guaranteed to be a straight integer version tuple
    # so we have to do some digging to get the version parts out
    #
    # If a LooseVersion contains a list or tuple, then the integer version
    # is the first element in that list or tuple
    # https://github.com/python/cpython/blob/2.7/Lib/distutils/version.py#L250
    #
    # If the LooseVersion contains a non-integer version, it is placed at
    # index 3 of the version tuple
    # https://github.com/python/cpython/blob/2.7/Lib/distutils/version.py#L293

# Generated at 2022-06-13 17:05:03.240398
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0b1')) == SemanticVersion('1.0.0-0b1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build1')) == SemanticVersion('1.0.0+build1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0b1+build1')) == SemanticVersion('1.0.0-0b1+build1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build1.2')) == Sem

# Generated at 2022-06-13 17:05:12.529516
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test the creation of a SemanticVersion object from a LooseVersion object
    assert SemanticVersion.from_loose_version(
        LooseVersion('0.0.1')
    ) == SemanticVersion('0.0.1')

    assert SemanticVersion.from_loose_version(
        LooseVersion('0.0.1-1.2.3-alpha')
    ) == SemanticVersion('0.0.1-1.2.3-alpha')

    assert SemanticVersion.from_loose_version(
        LooseVersion('0.0.1+build')
    ) == SemanticVersion('0.0.1+build')

    # Test the creation of a SemanticVersion object from a LooseVersion object with non-integer values
    v = LooseVersion('0.0.1-alpha')
    v

# Generated at 2022-06-13 17:05:21.844606
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('1')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '1.0.0'
    loose_version = LooseVersion('1.2')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '1.2.0'
    loose_version = LooseVersion('1.2.3')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '1.2.3'
    loose_version = LooseVersion('1.2.3-alpha')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '1.2.3-alpha'
   

# Generated at 2022-06-13 17:05:32.783718
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.common.version import LooseVersion

    assert SemanticVersion.from_loose_version('0.0.1') == SemanticVersion('0.0.1')
    assert SemanticVersion.from_loose_version('0.0.1-alpha') == SemanticVersion('0.0.1-alpha')
    assert SemanticVersion.from_loose_version('0.0.1-alpha+0000') == SemanticVersion('0.0.1-alpha+0000')
    assert SemanticVersion.from_loose_version('0.0.1-alpha.1') == SemanticVersion('0.0.1-alpha.1')

# Generated at 2022-06-13 17:05:39.313185
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(
        LooseVersion('1')
    ) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(
        LooseVersion('1.2')
    ) == SemanticVersion('1.2.0')
    assert SemanticVersion.from_loose_version(
        LooseVersion('1.2.3')
    ) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(
        LooseVersion('1.2.3-pre')
    ) == SemanticVersion('1.2.3-pre')

# Generated at 2022-06-13 17:05:52.132306
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    def check_from_loose_version(
        loose_version, semantic_version, expected_output="Error"
    ):
        output = SemanticVersion.from_loose_version(loose_version)
        assert semantic_version == output, expected_output



# Generated at 2022-06-13 17:06:28.548694
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    versions = [
        "1.2",
        "1.2.3",
        "1.2.3.4",
        "1.2.3-4",
        "1.2.3-4.5",
        "1.2.3-4.5.6",
        "1.2.3+4",
        "1.2.3+4.5",
        "1.2.3+4.5.6",
        "1.2.3+4-5.6",
        "1.2.3-4+5.6",
    ]

# Generated at 2022-06-13 17:06:37.649789
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    class TestCase:
        def __init__(self, loose_version, semver):
            self.loose_version = loose_version
            self.semver = semver


# Generated at 2022-06-13 17:06:49.797937
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-1')) == SemanticVersion('1.0.0-1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-1.alpha')) == SemanticVersion('1.0.0-1.alpha')

# Generated at 2022-06-13 17:06:55.179275
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion
    a = SemanticVersion.from_loose_version(LooseVersion("0.8.7"))
    assert a == LooseVersion("0.8.7")
    assert a == LooseVersion("0.8.7.0.0.0")

    a = SemanticVersion.from_loose_version(LooseVersion("100a2b3c"))
    assert a == LooseVersion("100a2b3c.0.0")

    a = SemanticVersion.from_loose_version(LooseVersion("10.1 beta 5"))
    assert a == LooseVersion("10.1.0.beta.5")

    a = SemanticVersion.from_loose_version(LooseVersion("20.3.0.rc2"))

# Generated at 2022-06-13 17:07:07.847315
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Create loose version
    loose_version = LooseVersion('1.2.3+build.metadata')

    # Convert looose version to semantic version
    version = SemanticVersion.from_loose_version(loose_version)
    assert isinstance(version, SemanticVersion)
    assert version.is_stable()
    assert version.vstring == '1.2.3+build.metadata'

    loose_version = LooseVersion('1.2.3-alpha1')
    version = SemanticVersion.from_loose_version(loose_version)
    assert isinstance(version, SemanticVersion)
    assert not version.is_stable()
    assert version.vstring == '1.2.3-alpha1'

    loose_version = LooseVersion('1.2.3alpha1')
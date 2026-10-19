

# Generated at 2022-06-13 16:57:36.620890
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # LooseVersion with additional characters
    loose_version = LooseVersion('1.0.0alpha')
    # LooseVersion without additional characters
    loose_version_no_addition = LooseVersion('1.0.0')

    # Convert valid LooseVersion to SemanticVersion
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.is_stable is False
    assert str(semver) == '1.0.0-alpha'

    # Convert valid LooseVersion to SemanticVersion
    semver_no_addition = SemanticVersion.from_loose_version(loose_version_no_addition)
    assert semver_no_addition.is_stable is True
    assert str(semver_no_addition) == '1.0.0'

   

# Generated at 2022-06-13 16:57:44.173430
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0+build.1')) == SemanticVersion('1.0.0+build.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build.1')) == SemanticVersion('1.0.0+build.1')


# Generated at 2022-06-13 16:57:46.041200
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha('alpha') <= _Alpha('alpha')
    assert _Alpha('beta') <= _Alpha('gamma')


# Generated at 2022-06-13 16:57:54.647677
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    from ansible.errors import AnsibleError

    with pytest.raises(ValueError):
        SemanticVersion('')

    with pytest.raises(ValueError):
        SemanticVersion('1.0')

    with pytest.raises(ValueError):
        SemanticVersion('1.0.0.0')

    with pytest.raises(ValueError):
        SemanticVersion('1.0...0')

    with pytest.raises(ValueError):
        SemanticVersion('1..0.0')

    with pytest.raises(ValueError):
        SemanticVersion('1.0.0a')

    with pytest.raises(ValueError):
        SemanticVersion('a.b.c')

    with pytest.raises(ValueError):
        SemanticVersion('01.0.0')

# Generated at 2022-06-13 16:58:07.649757
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # Assert that with a LooseVersion 0.1.2-beta.3+build.4
    # correctly creates a SemanticVersion of 0.1.2-beta.3+build.4
    assert SemanticVersion.from_loose_version(LooseVersion('0.1.2-beta.3+build.4')).vstring == '0.1.2-beta.3+build.4'

    # Assert that with a LooseVersion 1.2+build.3
    # correctly creates a SemanticVersion of 1.2.0+build.3
    assert SemanticVersion.from_loose_version(LooseVersion('1.2+build.3')).vstring == '1.2.0+build.3'

    # Assert that with a LooseVersion 1.2-beta+build.3
    # correctly

# Generated at 2022-06-13 16:58:21.699292
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Testing simple case
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    # Testing pre-release version
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha')) == SemanticVersion('1.2.3-alpha')
    # Testing build metadata
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+abc')) == SemanticVersion('1.2.3+abc')
    # Testing pre-release version with build metadata
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha+abc')) == SemanticVersion('1.2.3-alpha+abc')
    # Testing missing patch level
   

# Generated at 2022-06-13 16:58:30.827773
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0beta1')) == SemanticVersion('1.0.0-beta1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0beta1-1')) == SemanticVersion('1.0.0-beta1-1')

# Generated at 2022-06-13 16:58:41.937559
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Case 1 - LooseVersion to SemanticVersion
    v1 = LooseVersion('1.1.0.rc1')
    v2 = SemanticVersion.from_loose_version(v1)
    assert v2.vstring == '1.1.0-rc1'
    assert v2.core == (1, 1, 0)
    assert v2.prerelease == ('rc1',)
    assert v2.buildmetadata == ()
    assert v2 == '1.1.0-rc1'

    # Case 2 - LooseVersion to another LooseVersion
    v1 = LooseVersion('1.1.0.rc1')
    v2 = LooseVersion.from_loose_version(v1)
    assert v1.vstring == v2.vstring

# Generated at 2022-06-13 16:58:52.943925
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    print("\n")
    x = _Alpha("a")
    print("p = _Alpha('a')")

    #Compare "a" with "a"
    y = _Alpha("a")
    print("q = _Alpha('a')")
    print("The result of p <= q is " + str(x <= y))
    print("The result of p !<= q is " + str(x <= y))

    #Compare "a" with "b"
    y = _Alpha("b")
    print("q = _Alpha('b')")
    print("The result of p <= q is " + str(x <= y))
    print("The result of p !<= q is " + str(x <= y))

    #Compare "a" with "b"
    y = _Alpha("b")

# Generated at 2022-06-13 16:59:04.474271
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 16:59:26.373753
# Unit test for method parse of class SemanticVersion

# Generated at 2022-06-13 16:59:38.342560
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version('0.1') == '0.1.0'
    assert SemanticVersion.from_loose_version('0.1.2') == '0.1.2'
    assert SemanticVersion.from_loose_version('0.1.2.3') == '0.1.2'
    assert SemanticVersion.from_loose_version('0.1.2.3+4.5.6') == '0.1.2+4.5.6'
    assert SemanticVersion.from_loose_version('0.1.2-3.4.5.6') == '0.1.2-3.4.5.6'

# Generated at 2022-06-13 16:59:41.303332
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('020')) == SemanticVersion('020.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('020.0.20')) == SemanticVersion('020.0.20')
    assert SemanticVersion.from_loose_version(LooseVersion('020.0.20+foo')) == SemanticVersion('020.0.20+foo')

# Generated at 2022-06-13 16:59:54.508984
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """This function tests the method SemanticVersion.from_loose_version()
    """
    # Test valid input
    version = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert not version.prerelease
    assert not version.buildmetadata

    version = SemanticVersion.from_loose_version(LooseVersion('1.2.3-4-5'))
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == (4, 5)
    assert not version.buildmetadata


# Generated at 2022-06-13 17:00:03.766395
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion("5.5.5.5")
    expected_version = SemanticVersion("5.5.5")
    assert expected_version == SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion("5.5.5.5-beta")
    expected_version = SemanticVersion("5.5.5-beta")
    assert expected_version == SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion("5.5.5")
    expected_version = SemanticVersion("5.5.5")
    assert expected_version == SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion("5.5")

# Generated at 2022-06-13 17:00:15.757719
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-2')) == SemanticVersion('1.0.0-2')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0.2')) == SemanticVersion('1.0.0+2')

# Generated at 2022-06-13 17:00:25.606601
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    v1 = '1.0.0'
    v2 = '1.0.0-alpha.1'
    v3 = '1.0.0-rc10'
    v4 = '1.0.0+build10.1'
    v5 = '1.0.0-alpha+build10.1'
    v6 = '1.0.0-alpha.1+build10.1'
    v7 = '1.0.0-alpha.1.1'
    v8 = '1.0.0-alpha.beta'
    v9 = '1.0.0-alpha..1'
    v10 = '1.0.0-alpha.0beta'
    v11 = '1.0.0-alpha.1+build01.2.3'

# Generated at 2022-06-13 17:00:35.316312
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:00:47.675977
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2')) == SemanticVersion('1.2.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('0.1.2.3')) == SemanticVersion('0.1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.1')) == SemanticVersion('1.2.3-alpha.1')

# Generated at 2022-06-13 17:00:58.284624
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # Loose version instance
    version = LooseVersion('3.3')

    # Creation from a LooseVersion instance
    obj = SemanticVersion.from_loose_version(version)
    assert isinstance(obj, SemanticVersion)
    assert isinstance(obj, LooseVersion)
    assert isinstance(obj, Version)
    assert isinstance(obj, object)
    assert hasattr(obj, 'vstring')
    assert hasattr(obj, 'major')
    assert hasattr(obj, 'minor')
    assert hasattr(obj, 'patch')
    assert hasattr(obj, 'prerelease')
    assert hasattr(obj, 'buildmetadata')
    assert hasattr(obj, 'core')
    assert hasattr(obj, 'is_prerelease')
    assert hasattr(obj, 'is_stable')
   

# Generated at 2022-06-13 17:01:17.040549
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # InputData
    ild_01 = ((1, 1, 1), ())
    ild_02 = ((1, 1, 1), (1,))
    ild_03 = ((1, 1, 1), (1, 1))
    ild_04 = ((1, 1, 1), (1, 1, 1))
    ild_05 = ((1,), ())
    ild_06 = ((1,), (1,))
    ild_07 = ((1,), (1, 1))
    ild_08 = ((1,), (1, 1, 1))
    ild_09 = ((1, 1), ())
    ild_10 = ((1, 1), (1,))
    ild_11 = ((1, 1), (1, 1))

# Generated at 2022-06-13 17:01:26.612299
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six import string_types

# Generated at 2022-06-13 17:01:38.900334
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('1.0')
    version = SemanticVersion.from_loose_version(loose_version)
    assert version == '1.0.0'
    loose_version = LooseVersion('1.0.1+abc')
    version = SemanticVersion.from_loose_version(loose_version)
    assert version == '1.0.1+abc'
    loose_version = LooseVersion('1.1-dev')
    version = SemanticVersion.from_loose_version(loose_version)
    assert version == '1.1.0-dev'
    loose_version = LooseVersion('1.0.0.rc1')
    version = SemanticVersion.from_loose_version(loose_version)

# Generated at 2022-06-13 17:01:47.945318
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    def test_version(loose_version, expected_version):
        result = SemanticVersion.from_loose_version(loose_version)
        assert result == expected_version, "%s != %s" % (result, expected_version)
        assert isinstance(result, SemanticVersion), "type mismatch: %s" % type(result)

    test_version(LooseVersion('1.0.1'), SemanticVersion('1.0.1'))
    test_version(LooseVersion('1.2.3.dev0'), SemanticVersion('1.2.3-dev0'))

# Generated at 2022-06-13 17:01:55.665819
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # LooseVersion <= SemanticVersion
    assert LooseVersion('1.2.3') <= SemanticVersion('1.2.3')
    assert LooseVersion('1.2.3.4') <= SemanticVersion('1.2.3')
    assert LooseVersion('1.2.3.4.5') <= SemanticVersion('1.2.3')
    assert LooseVersion('1.2.3-4') <= SemanticVersion('1.2.3')
    assert LooseVersion('1.2.3-4.5') <= SemanticVersion('1.2.3')
    assert LooseVersion('1.2.3-4.5.6.7-8.9') <= SemanticVersion('1.2.3')

# Generated at 2022-06-13 17:02:06.872950
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import re

    assert SemanticVersion.from_loose_version(LooseVersion("0.0.1")).vstring == "0.0.1"
    assert SemanticVersion.from_loose_version(LooseVersion("0.0.1-alpha")).vstring == "0.0.1-alpha"
    assert SemanticVersion.from_loose_version(LooseVersion("0.0.1-alpha.1")).vstring == "0.0.1-alpha.1"
    assert SemanticVersion.from_loose_version(LooseVersion("0.0.1-alpha.1.1")).vstring == "0.0.1-alpha.1.1"

# Generated at 2022-06-13 17:02:08.931191
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('2.3.4-alpha.4+build.123')
    assert '2.3.4' == str(SemanticVersion.from_loose_version(loose_version))



# Generated at 2022-06-13 17:02:17.021847
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.version import LooseVersion
    assert SemanticVersion.from_loose_version(LooseVersion("2.2")) == SemanticVersion("2.2.0")
    assert SemanticVersion.from_loose_version(LooseVersion("2.2+beta1")) == SemanticVersion("2.2.0-beta1")
    assert SemanticVersion.from_loose_version(LooseVersion("2.2.1")) == SemanticVersion("2.2.1")
    assert SemanticVersion.from_loose_version(LooseVersion("2.2.1b3")) == SemanticVersion("2.2.1+b3")
    assert SemanticVersion.from_loose_version(LooseVersion("2.2-1")) == SemanticVersion("2.2.0-1")


# Generated at 2022-06-13 17:02:23.040710
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert str(SemanticVersion.from_loose_version('1.2.3')) == '1.2.3'
    assert str(SemanticVersion.from_loose_version('1.2.3.4')) == '1.2.3'
    assert str(SemanticVersion.from_loose_version('1.2.3-1.2.3')) == '1.2.3-1.2.3'
    assert str(SemanticVersion.from_loose_version('1.2.3-1.2.3.4')) == '1.2.3-1.2.3'
    assert str(SemanticVersion.from_loose_version('1.2.3+1.2.3')) == '1.2.3+1.2.3'

# Generated at 2022-06-13 17:02:32.549181
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha1')) == SemanticVersion('1.0.0-alpha1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-rc1')) == SemanticVersion('1.0.0-rc1')
    # Build metadata is not captured in a LooseVersion and therefore not in a SemanticVersion
    # created from a LooseVersion

# Generated at 2022-06-13 17:02:48.304248
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Test method ``SemanticVersion.from_loose_version``"""

    # Test that ValueError is raised if version is not a LooseVersion
    try:
        SemanticVersion.from_loose_version('1.0.0')
    except ValueError as exc:
        assert str(exc) == "'1.0.0' is not a LooseVersion"
    else:
        assert False

    # Test that ValueError is raised if non integer values are present
    try:
        SemanticVersion.from_loose_version(LooseVersion('1.0.0a'))
    except ValueError as exc:
        assert str(exc) == "Non integer values in LooseVersion ('1', '0', '0', 'a')"
    else:
        assert False

    # Test that if version has a prerelease component it is included

# Generated at 2022-06-13 17:02:53.937454
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import pytest
    from ansible.module_utils.compat.version import LooseVersion
    SemanticVersion = SemanticVersion
    loose_version = LooseVersion('2.2.2.2')
    SemanticVersion.from_loose_version(loose_version)
    if not isinstance(loose_version, LooseVersion):
        pass
    return True


# Generated at 2022-06-13 17:03:05.754067
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Some examples from https://www.johannes-bauer.com/compsci/ecc/#semver
    assert str(SemanticVersion.from_loose_version(LooseVersion('1'))) == '1.0.0'
    assert str(SemanticVersion.from_loose_version(LooseVersion('1.2'))) == '1.2.0'
    assert str(SemanticVersion.from_loose_version(LooseVersion('1.2.3'))) == '1.2.3'
    assert str(SemanticVersion.from_loose_version(LooseVersion('1.2.3.4'))) == '1.2.3.4'

# Generated at 2022-06-13 17:03:15.279343
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:03:22.531266
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Tests that existing LooseVersion instances are converted to SemanticVersion
    # instances correctly
    vstring = '1.0.0'
    loose_version = LooseVersion(vstring)
    version = SemanticVersion.from_loose_version(loose_version)
    assert version.vstring == vstring
    assert version.is_stable

    vstring = '1.2.3'
    loose_version = LooseVersion(vstring)
    version = SemanticVersion.from_loose_version(loose_version)
    assert version.vstring == vstring
    assert version.is_stable

    vstring = '0.2.3'
    loose_version = LooseVersion(vstring)
    version = SemanticVersion.from_loose_version(loose_version)

# Generated at 2022-06-13 17:03:34.353430
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test for object creation from LooseVersion object
    loose1 = LooseVersion('1.2.3-1.alpha1+abc')
    semv1 = SemanticVersion.from_loose_version(loose1)
    assert semv1.major == 1
    assert semv1.minor == 2
    assert semv1.patch == 3
    assert semv1.prerelease == tuple(_Numeric(x) if x.isdigit() else _Alpha(x) for x in '1.alpha1'.split('.'))
    assert semv1.buildmetadata == tuple(_Numeric(x) if x.isdigit() else _Alpha(x) for x in 'abc'.split('.'))

    # Test for object creation from string
    loose1 = '1.2.3-1.alpha1+abc'
    sem

# Generated at 2022-06-13 17:03:44.516855
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:03:50.274084
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    input_version = '0.0.1'
    loose_version = LooseVersion(input_version)
    assert SemanticVersion.from_loose_version(loose_version).vstring == input_version

    input_version = '0.0.1-alpha'
    loose_version = LooseVersion(input_version)
    assert SemanticVersion.from_loose_version(loose_version).vstring == input_version

    input_version = '0.0.1-alpha.1'
    loose_version = LooseVersion(input_version)
    assert SemanticVersion.from_loose_version(loose_version).vstring == input_version

    input_version = '0.0.1+build.1'
    loose_version = LooseVersion(input_version)

# Generated at 2022-06-13 17:03:57.709909
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six.moves import StringIO
    import sys
    import os

    sys.argv = [sys.argv[0]]
    sys.stderr = StringIO()

    os.environ.pop('ANSIBLE_UNIT_TEST', None)

# Generated at 2022-06-13 17:04:06.866847
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0.1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha.1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0.1-alpha.1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0.1+abc123.456')) == SemanticVersion('1.0.0')


# Generated at 2022-06-13 17:04:29.172777
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('v11')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == '11.0.0'
    assert semver.core == (11, 0, 0)
    assert semver.prerelease == ()
    assert not semver.is_prerelease
    assert semver.buildmetadata == ()
    assert not semver.is_stable

    loose_version = LooseVersion('1.101a.0')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == '1.101.0'
    assert semver.core == (1, 101, 0)
    assert semver.prerelease == ()
    assert not semver.is_prerelease
    assert sem

# Generated at 2022-06-13 17:04:38.623256
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # noinspection PyProtectedMember
    assert SemanticVersion._from_loose_version(LooseVersion('1')) == \
        SemanticVersion('1.0.0')
    # noinspection PyProtectedMember
    assert SemanticVersion._from_loose_version(LooseVersion('1.2')) == \
        SemanticVersion('1.2.0')
    # noinspection PyProtectedMember
    assert SemanticVersion._from_loose_version(LooseVersion('1.2.3')) == \
        SemanticVersion('1.2.3')
    # noinspection PyProtectedMember
    assert SemanticVersion._from_loose_version(LooseVersion('1.2.3.4')) == \
        SemanticVersion('1.2.3')

# Generated at 2022-06-13 17:04:50.796173
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('1.0')
    SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion('1.0a')
    SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion('1.0a.1')
    SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion('1.0.1a')
    SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion('1.0.1a.2')
    SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion('1.0.1.a')
    SemanticVersion.from_loose

# Generated at 2022-06-13 17:05:04.144457
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Set up some variables to be used for comparison
    loose_version_1 = LooseVersion('1.0-1.1')
    loose_version_2 = LooseVersion('1.0-2.0')
    loose_version_3 = LooseVersion('2.0.0')
    loose_version_4 = LooseVersion('1.0.1-1.1')
    loose_version_5 = LooseVersion('1.0.1-1.1-1')
    loose_version_6 = LooseVersion('1.0.1-1.1-1-1')

    # Check all exceptions
    exception_msg_1 = "TypeError: unsupported operand type(s) for -: 'LooseVersion' and 'LooseVersion'"

# Generated at 2022-06-13 17:05:16.042228
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:05:27.907341
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from distutils.version import LooseVersion

    # LooseVersion(A) < LooseVersion(B) => SemanticVersion(A) < SemanticVersion(B)
    A = LooseVersion('1.0.0-alpha0+0')
    B = LooseVersion('1.0.0-alpha0+0.alpha0')
    assert A < B
    assert SemanticVersion.from_loose_version(A) < SemanticVersion.from_loose_version(B)

    # LooseVersion(A) < LooseVersion(B) => SemanticVersion(A) < SemanticVersion(B)
    A = LooseVersion('1.0.0.alpha0.0')
    B = LooseVersion('1.0.0.0.alpha0')
    assert A < B

# Generated at 2022-06-13 17:05:36.182032
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('0.1.0')
    expected_result = SemanticVersion('0.1.0')
    assert SemanticVersion.from_loose_version(loose_version) == expected_result

    loose_version = LooseVersion('0.1.0.dev1')
    expected_result = SemanticVersion('0.1.0-dev1')
    assert SemanticVersion.from_loose_version(loose_version) == expected_result

    loose_version = LooseVersion('0.1.0-dev1')
    expected_result = SemanticVersion('0.1.0-dev1')
    assert SemanticVersion.from_loose_version(loose_version) == expected_result

    loose_version = LooseVersion('0.1.0+build1234')
    expected

# Generated at 2022-06-13 17:05:49.195481
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:06:00.121589
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion
    from ansible.module_utils.semver import SemanticVersion

    version_str = '7.0.0'
    loose = LooseVersion(version_str)
    semver = SemanticVersion.from_loose_version(loose)
    assert semver.vstring == version_str
    assert semver.major == 7
    assert semver.minor == 0
    assert semver.patch == 0
    assert semver.prerelease == ()
    assert semver.buildmetadata == ()

    version_str = '7.0.0-alpha.1'
    loose = LooseVersion(version_str)
    semver = SemanticVersion.from_loose_version(loose)
    assert semver.vstring == version_str
   

# Generated at 2022-06-13 17:06:07.346945
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('0.1.2dev')) == SemanticVersion('0.1.2-dev')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3.dev')) == SemanticVersion('1.2.3-dev')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3,dev')) == SemanticVersion('1.2.3-dev')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3.dev.4')) == SemanticVersion('1.2.3-dev.4')
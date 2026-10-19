

# Generated at 2022-06-13 16:57:37.470952
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    """Test the function of parse method of class SemanticVersion
    """
    vstring = '2.0.0'
    inst = SemanticVersion()
    try:
        inst.parse(vstring)
    except ValueError:
        assert False
    assert inst.major == '2'
    assert inst.minor == '0'
    assert inst.patch == '0'
    assert inst.prerelease == ''
    assert inst.buildmetadata == ''

    vstring = '2.0.0-pre.1'
    inst = SemanticVersion()
    try:
        inst.parse(vstring)
    except ValueError:
        assert False
    assert inst.major == '2'
    assert inst.minor == '0'
    assert inst.patch == '0'
    assert inst.prerelease == 'pre.1'

# Generated at 2022-06-13 16:57:48.619089
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    sv = SemanticVersion(vstring='1.2.3')
    assert sv.major == 1
    assert sv.minor == 2
    assert sv.patch == 3
    assert not sv.prerelease
    assert not sv.buildmetadata

    sv = SemanticVersion(vstring='1.2.3-alpha.01.2')
    assert sv.major == 1
    assert sv.minor == 2
    assert sv.patch == 3
    assert sv.prerelease == tuple([_Alpha('alpha'), _Numeric(1), _Numeric(2)])
    assert not sv.buildmetadata

    sv = SemanticVersion(vstring='1.2.3+20130313144700')
    assert sv.major == 1
    assert sv.minor == 2
    assert sv.patch == 3
    assert not sv.prerelease


# Generated at 2022-06-13 16:57:52.033303
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    alpha = _Alpha("alpha")
    assert alpha >= "alpha"
    assert not alpha <= "alpha"
    assert alpha <= "zeta"
    assert alpha <= "1"


# Generated at 2022-06-13 16:58:00.661106
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    # Test with correct version string
    correct_version_string = 'v1.0.0'
    correct_result = SemanticVersion(correct_version_string)

    # Test with incorrect version string
    incorrect_version_string = '1100.2.3'
    try:
        incorrect_result = SemanticVersion(incorrect_version_string)
    except ValueError:
        pass
    else: 
        assert False, "Did not throw a ValueError for incorrect version string"

# Generated at 2022-06-13 16:58:14.023377
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    semver = SemanticVersion()
    # Empty string is not allowed
    try:
        semver.parse('')
        assert False
    except ValueError:
        pass

    # Anything MUST NOT be preceded by leading zeroes.
    try:
        semver.parse('01.0.0')
        assert False
    except ValueError:
        pass

    # Pre-release versions have a lower precedence than the associated normal version.
    # Example: 1.0.0-alpha < 1.0.0.
    assert SemanticVersion('1.0.0-alpha') < SemanticVersion('1.0.0')

    # Build metadata SHOULD be ignored when determining version precedence.
    # Thus two versions that differ only in the build metadata, have the same precedence.
    # Example: 1.0.0-alpha+001 == 1.0.

# Generated at 2022-06-13 16:58:26.269405
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from distutils.version import LooseVersion

    # No markers - should work
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')

    # With markers - should work
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-rc1')) == SemanticVersion('1.0.0-rc1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build')) == Sem

# Generated at 2022-06-13 16:58:39.786641
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1')).major == 1
    assert SemanticVersion.from_loose_version(LooseVersion('1.4')).minor == 4
    assert SemanticVersion.from_loose_version(LooseVersion('1.4.2')).patch == 2
    assert SemanticVersion.from_loose_version(LooseVersion('1.7.8-dev')).prerelease == (_Alpha('dev'),)
    assert SemanticVersion.from_loose_version(LooseVersion('1.7.8-alpha.1')).prerelease == (_Alpha('alpha'), _Numeric('1'))

# Generated at 2022-06-13 16:58:51.729330
# Unit test for method parse of class SemanticVersion

# Generated at 2022-06-13 16:59:03.026571
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion("1.2")) == SemanticVersion("1.2.0")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3.4")) == SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3-alpha.1")) == SemanticVersion("1.2.3-alpha.1")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2b2")) == SemanticVersion("1.2.0-b2")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2")) < SemanticVersion("1.3.0")

# Generated at 2022-06-13 16:59:11.944639
# Unit test for method parse of class SemanticVersion

# Generated at 2022-06-13 16:59:41.808965
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    # Test parsing of a full semver
    semver_one = SemanticVersion('1.2.3-alpha.1.2+build.1.2')
    assert semver_one.vstring == '1.2.3-alpha.1.2+build.1.2'
    assert semver_one.major == 1
    assert semver_one.minor == 2
    assert semver_one.patch == 3
    assert semver_one.prerelease == (_Alpha('alpha'), _Numeric('1'), _Numeric('2'))
    assert semver_one.buildmetadata == (_Alpha('build'), _Numeric('1'), _Numeric('2'))

    # Test parsing of semver with no prerelease or build metadata
    semver_two = SemanticVersion('1.2.3')
    assert semver_two

# Generated at 2022-06-13 16:59:54.938509
# Unit test for method parse of class SemanticVersion

# Generated at 2022-06-13 17:00:04.063035
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    # test case 1
    vstring = '1'
    version = SemanticVersion(vstring)
    assert version.major == 1
    assert version.minor == 0
    assert version.patch == 0

    # test case 2
    vstring = '1.2'
    version = SemanticVersion(vstring)
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 0

    # test case 3
    vstring = '1.2.3'
    version = SemanticVersion(vstring)
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3

    # test case 4
    vstring = '1.2.3-alpha.1'
    version = SemanticVersion(vstring)
    assert version.major == 1

# Generated at 2022-06-13 17:00:16.048290
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    # Test with simple number
    version = '1.2.3'
    sv = SemanticVersion(version)
    sv.parse(version)
    assert (sv.major, sv.minor, sv.patch) == (1, 2, 3)
    assert sv.prerelease == ()
    assert sv.buildmetadata == ()
    assert sv.is_prerelease == False
    assert sv.is_stable == True

    # Test with prerelease
    version = '1.2.3-rc1'
    sv = SemanticVersion(version)
    sv.parse(version)
    assert (sv.major, sv.minor, sv.patch) == (1, 2, 3)
    assert sv.prerelease == ('rc1',)
    assert sv.buildmetadata == ()
    assert sv.is_prerelease == True

# Generated at 2022-06-13 17:00:19.856142
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    v = SemanticVersion()
    v.parse('3.2.1')
    assert v.major == 3
    assert v.minor == 2
    assert v.patch == 1
    assert v.prerelease == ()
    assert v.buildmetadata == ()



# Generated at 2022-06-13 17:00:28.677285
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha')) == SemanticVersion('1.0.0-alpha')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha.1')) == SemanticVersion('1.0.0-alpha.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha.1.2.3')) == SemanticVersion('1.0.0-alpha.1.2.3')

# Generated at 2022-06-13 17:00:37.647769
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:00:50.344262
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test case 1
    loose_version = LooseVersion('1.2.3')
    expected = '1.2.3'
    actual = SemanticVersion.from_loose_version(loose_version).vstring
    assert expected == actual

    # Test case 2
    loose_version = LooseVersion('1.2.3.4')
    expected = '1.2.3'
    actual = SemanticVersion.from_loose_version(loose_version).vstring
    assert expected == actual

    # Test case 3
    loose_version = LooseVersion('1.2.3-rc.1+build')
    expected = '1.2.3-rc.1+build'
    actual = SemanticVersion.from_loose_version(loose_version).vstring
    assert expected == actual

    #

# Generated at 2022-06-13 17:00:58.867704
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    from ansible.module_utils.six.moves.builtins import str


# Generated at 2022-06-13 17:01:05.827140
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    expected = SemanticVersion('1.2.3+testing')
    assert expected == SemanticVersion.from_loose_version(LooseVersion('1.2.3+testing'))
    assert expected == SemanticVersion.from_loose_version(LooseVersion('1.2.3-testing+testing'))
    assert expected == SemanticVersion.from_loose_version(LooseVersion('1.2.3-testing+testing'))
    assert expected == SemanticVersion.from_loose_version(LooseVersion('1.2.3.dev-testing+testing'))
    assert expected == SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.testing'))

# Generated at 2022-06-13 17:01:24.635319
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:01:37.735138
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Case 1. ValueError: Not a LooseVersion object
    sample_data = '1.2.3'
    expected_result = ValueError('%r is not a LooseVersion' % sample_data)
    try:
        SemanticVersion.from_loose_version(sample_data)
    except ValueError as e:
        assert str(e) == str(expected_result)

    # Case 2. ValueError: Invalid loose version
    sample_data = LooseVersion('a.b.c')
    expected_result = ValueError('%r is not a LooseVersion' % sample_data)
    try:
        SemanticVersion.from_loose_version(sample_data)
    except ValueError as e:
        assert str(e) == str(expected_result)

    # Case 3. ValueError: Invalid loose version

# Generated at 2022-06-13 17:01:40.938770
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('1.2.3')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.vstring == '1.2.3'



# Generated at 2022-06-13 17:01:49.285837
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2a1')) == SemanticVersion('1.2.0-a1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2b2')) == SemanticVersion('1.2.0-b2')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2c3')) == SemanticVersion('1.2.0-c3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2-alpha1')) == SemanticVersion('1.2.0-alpha1')

# Generated at 2022-06-13 17:02:00.002393
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # positive tests
    assert type(SemanticVersion.from_loose_version(LooseVersion('1.0'))) is SemanticVersion
    assert type(SemanticVersion.from_loose_version(LooseVersion('1.0.1'))) is SemanticVersion
    assert type(SemanticVersion.from_loose_version(LooseVersion('1.0.1-rc1'))) is SemanticVersion
    assert type(SemanticVersion.from_loose_version(LooseVersion('1.0.1-rc1.2'))) is SemanticVersion
    assert type(SemanticVersion.from_loose_version(LooseVersion('1.0.1-rc1.2.abc'))) is SemanticVersion

# Generated at 2022-06-13 17:02:11.782665
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:02:18.452603
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    Test method SemanticVersion.from_loose_version()
    """

# Generated at 2022-06-13 17:02:29.719090
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version('1.0') == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version('1.2') == SemanticVersion('1.2.0')
    assert SemanticVersion.from_loose_version('1.2a3') == SemanticVersion('1.2.0-a3')
    assert SemanticVersion.from_loose_version('1.2a3b4') == SemanticVersion('1.2.0-a3.b4')
    assert SemanticVersion.from_loose_version('1.2a3b4c5') == SemanticVersion('1.2.0-a3.b4.c5')

# Generated at 2022-06-13 17:02:42.541634
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six import PY2
    # case 1: loose version with a single integer (e.g. 1.11)
    assert SemanticVersion.from_loose_version(LooseVersion('1.11')).is_stable
    # case 2: loose version with a single float (e.g. 1.11.0)
    assert SemanticVersion.from_loose_version(LooseVersion('1.11.0')).is_stable
    # case 3: loose version with a single float and prerelease tag (e.g. 1.11.0a1)
    assert not SemanticVersion.from_loose_version(LooseVersion('1.11.0a1')).is_stable
    # case 4: loose version with a single float and build metadata (e.g. 1.11.0+dev

# Generated at 2022-06-13 17:02:51.197427
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Tests the version conversion using available version formats."""

    # Test version formats where there is an exact match between the LooseVersion and SemanticVersion
    SemanticVersion.from_loose_version(LooseVersion('0.0.2'))

    # Test version formats where there is match between the LooseVersion and SemanticVersion
    SemanticVersion.from_loose_version(
        LooseVersion('0.9.9-0.3.7.1+xyz.1.abcd.xyz.wxyz')
    )
    SemanticVersion.from_loose_version(
        LooseVersion('1.2.3-0.4.7+xyz.1.abcd.xyz.wxyz')
    )

    # Test version formats where there is a mismatch between the LooseVersion and SemanticVersion
   

# Generated at 2022-06-13 17:03:11.802819
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Tests to make sure the method from_loose_version of class SemanticVersion
    # converts versions from distutils.version.LooseVersion in the way that
    # is expected in the implementation of this module.
    #
    # Since we are depending on a different module, lets do a simple test with
    # a known value. We will expect that if we convert the distutils.version
    # 1.2.3 to the SemanticVersion class, it will be the same SemanticVersion
    # that we create directly.
    #
    # Let's make sure we capture the distutils.version.LooseVersion
    # class and not the SemanticVersion class.
    from ansible.module_utils.distutils.version import LooseVersion

    loose = LooseVersion('1.2.3')
    sv = SemanticVersion('1.2.3')

# Generated at 2022-06-13 17:03:18.167419
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose = LooseVersion('0.1.2-a.b.c+1.0-rc')
    semver = SemanticVersion.from_loose_version(loose)
    expected_version = '0.1.2-a.b.c+1.0-rc'
    assert semver.vstring == expected_version

# Generated at 2022-06-13 17:03:27.292086
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    def assert_semantic_version_from_loose_version_raises_ValueError(
            loose_version):
        try:
            SemanticVersion.from_loose_version(loose_version)
        except ValueError as e:
            pass
        else:
            raise AssertionError('ValueError not raised')

    # Test cases for non-loose versions
    assert_semantic_version_from_loose_version_raises_ValueError('0.0.0')
    assert_semantic_version_from_loose_version_raises_ValueError(
        '0.0.0-alpha+007')
    assert_semantic_version_from_loose_version_raises_ValueError(
        '0.0.0+007')
    assert_semantic_version_from_loose_

# Generated at 2022-06-13 17:03:38.482992
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:03:46.221929
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test a valid use of SemanticVersion.from_loose_version
    s = SemanticVersion.from_loose_version(LooseVersion('1.2.3.4'))
    assert s.major == 1
    assert s.minor == 2
    assert s.patch == 3
    assert s.prerelease == ()
    assert s.buildmetadata == ()

    # Test invalid use 1 (argument is not a LooseVersion)
    l = LooseVersion('1.2.3.4')
    try:
        s = SemanticVersion.from_loose_version(l)
    except ValueError:
        assert True
    else:
        raise AssertionError

    # Test invalid use 2 (argument has non-integer components)
    l = LooseVersion('a.b.c.d')

# Generated at 2022-06-13 17:03:55.553961
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion("1.0.0")).major == 1
    assert SemanticVersion.from_loose_version(LooseVersion("1.0.0")).minor == 0
    assert SemanticVersion.from_loose_version(LooseVersion("1.0.0")).patch == 0
    assert SemanticVersion.from_loose_version(LooseVersion("1.0.0")).prerelease == ()
    assert SemanticVersion.from_loose_version(LooseVersion("1.0.0")).buildmetadata == ()
    assert SemanticVersion.from_loose_version(LooseVersion("1.0.0")).is_stable == True

    assert SemanticVersion.from_loose_version(LooseVersion("1.0")).major == 1


# Generated at 2022-06-13 17:04:05.582457
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:04:18.556181
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test not a LooseVersion
    try:
        SemanticVersion.from_loose_version('1.0.0')
    except ValueError:
        pass
    else:
        assert False

    # Test non integer values in LooseVersion
    try:
        SemanticVersion.from_loose_version(LooseVersion('1.0a-1'))
    except ValueError:
        pass
    else:
        assert False

    # Test no prerelease
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == '1.0.0'

    # Test with prerelease
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-pre.1')) == '1.0.0-pre.1'

    # Test with build

# Generated at 2022-06-13 17:04:27.620003
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3.4")) == SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3-4")) == SemanticVersion("1.2.3-4")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3+4")) == SemanticVersion("1.2.3+4")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3")) == SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3.4.5.6")) == SemanticVersion("1.2.3")
    assert SemanticVersion.from_

# Generated at 2022-06-13 17:04:31.512065
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('1.0')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.vstring == '1.0'

    loose_version = LooseVersion('1.0a')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.vstring == '1.0-a'

    loose_version = LooseVersion('1.0.a')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.vstring == '1.0.a'

    loose_version = LooseVersion('1.0.a1')
    semantic_version = SemanticVersion.from_loose_version(loose_version)


# Generated at 2022-06-13 17:05:21.011929
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    SemanticVersion.from_loose_version(SemanticVersion("1.2.3")) == SemanticVersion("1.2.3") == True
    SemanticVersion.from_loose_version(LooseVersion("1.2.3")) == SemanticVersion("1.2.3") == True
    SemanticVersion.from_loose_version(LooseVersion("1.2.3.4.5")) == SemanticVersion("1.2.3") == True
    SemanticVersion.from_loose_version(LooseVersion("1.2.3.dev1")) == SemanticVersion("1.2.3-dev1") == True
    SemanticVersion.from_loose_version(LooseVersion("1.2.3.dev1+build")) == SemanticVersion("1.2.3-dev1+build") == True

# Generated at 2022-06-13 17:05:32.063528
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test that from_loose_version raises an error on a non-LooseVersion
    loose_version = 1
    try:
        SemanticVersion.from_loose_version(loose_version)
    except ValueError:
        pass

    # Test that from_loose_version raises an error on a LooseVersion that has non-integer values
    loose_version = LooseVersion('1.0.0.a')
    try:
        SemanticVersion.from_loose_version(loose_version)
    except ValueError:
        pass

    # Test that from_loose_version results in the same version if no pre/build metadata is given
    loose_version = LooseVersion('1.0.0')
    version = SemanticVersion.from_loose_version(loose_version)

# Generated at 2022-06-13 17:05:38.849691
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version_list = [
        (LooseVersion('1.2.3'), '1.2.3'),
        (LooseVersion('v1.2.3'), '1.2.3'),
        (LooseVersion('1.2.3.4'), '1.2.3.4'),
        (LooseVersion('1.2.3-4'), '1.2.3-4'),
        (LooseVersion('1.2.3+4'), '1.2.3+4'),
        (LooseVersion('1.2.3-4+5'), '1.2.3-4+5'),
    ]

    for loose_version, semver_str in loose_version_list:
        semver = SemanticVersion.from_loose_version(loose_version)
        assert semver.vstring

# Generated at 2022-06-13 17:05:51.160812
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test taking a LooseVersion
    loose_version = LooseVersion('0.2.1')
    assert isinstance(SemanticVersion.from_loose_version(loose_version), SemanticVersion)

    # Test we can take a LooseVersion
    # with an alphanumeric identifier
    loose_version = LooseVersion('0.2.1Ngx')
    assert isinstance(SemanticVersion.from_loose_version(loose_version), SemanticVersion)

    # Test we raise a ValueError when taking something
    # other than a LooseVersion
    try:
        SemanticVersion.from_loose_version('0.2.1')
    except ValueError:
        pass
    else:
        assert False, 'Must raise a ValueError'



# Generated at 2022-06-13 17:06:01.524451
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test subversion version
    SemanticVersion.from_loose_version(LooseVersion('0.7.15svn'))
    SemanticVersion.from_loose_version(LooseVersion('0.7.15svn1337'))

    # Test overlong version
    SemanticVersion.from_loose_version(LooseVersion('0.7.15.'))

    # Test overlong version with marker
    SemanticVersion.from_loose_version(LooseVersion('0.7.15.+'))
    SemanticVersion.from_loose_version(LooseVersion('0.7.15.-'))

    # Test overlong versions
    SemanticVersion.from_loose_version(LooseVersion('0.7.15.1.'))

# Generated at 2022-06-13 17:06:09.080140
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:06:19.879680
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha+2.3')) == SemanticVersion('1.0.0-alpha+2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0.0.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0.0.0.0-alpha+2.3')) == SemanticVersion('1.0.0-alpha+2.3')

# Generated at 2022-06-13 17:06:26.366500
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    '''
    _vstring = '1.0.1-1+bzr1301'
    _loose_version = LooseVersion(_vstring)
    v = SemanticVersion.from_loose_version(_loose_version)
    assert isinstance(v, SemanticVersion)
    '''
    _vstring = '1.0.1.1'
    _loose_version = LooseVersion(_vstring)
    v = SemanticVersion.from_loose_version(_loose_version)
    assert isinstance(v, SemanticVersion)

test_SemanticVersion_from_loose_version()

# Generated at 2022-06-13 17:06:36.300434
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import ansible.module_utils.six as six

    # test cases are a list of tuples in the format (LooseVersion, expected)
    # where LooseVersion is the LooseVersion object to test, and expected
    # is the expected value

# Generated at 2022-06-13 17:06:42.537916
# Unit test for method from_loose_version of class SemanticVersion
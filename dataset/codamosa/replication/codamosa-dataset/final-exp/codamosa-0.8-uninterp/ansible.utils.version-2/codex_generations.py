

# Generated at 2022-06-13 16:57:35.180109
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # valid cases
    v1 = SemanticVersion.from_loose_version(LooseVersion('alpha.beta.gamma'))
    assert v1.vstring == '0.0.0'
    assert v1.prerelease == (_Alpha('alpha'), _Alpha('beta'), _Alpha('gamma'))
    assert v1.buildmetadata == ()

    v2 = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    assert v2.vstring == '1.2.3'
    assert v2.prerelease == ()
    assert v2.buildmetadata == ()

    v3 = SemanticVersion.from_loose_version(LooseVersion('1.2-3.4+5.6'))

# Generated at 2022-06-13 16:57:45.209701
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    # Testing type of major, minor and patch
    assert isinstance(SemanticVersion("2.0.0").major, int)
    assert isinstance(SemanticVersion("2.0.0").minor, int)
    assert isinstance(SemanticVersion("2.0.0").patch, int)
    assert isinstance(SemanticVersion("2.0.0-pre").major, int)
    assert isinstance(SemanticVersion("2.0.0-pre").minor, int)
    assert isinstance(SemanticVersion("2.0.0-pre").patch, int)
    assert isinstance(SemanticVersion("2.0.0+build").major, int)
    assert isinstance(SemanticVersion("2.0.0+build").minor, int)

# Generated at 2022-06-13 16:57:54.035506
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import operator

# Generated at 2022-06-13 16:57:56.599052
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version("1.2.3") == SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version("1.2.3-rc1") == SemanticVersion("1.2.3-rc1")
# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 16:58:09.622059
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    for vstring in ('0', '0.0', '0.0.0'):
        version = SemanticVersion(vstring)
        assert version.major == 0
        assert version.minor == 0
        assert version.patch == 0
        assert version.prerelease == ()
        assert version.buildmetadata == ()
        assert version.vstring == vstring

    for vstring in ('1', '1.0', '1.0.0'):
        version = SemanticVersion(vstring)
        assert version.major == 1
        assert version.minor == 0
        assert version.patch == 0
        assert version.prerelease == ()
        assert version.buildmetadata == ()
        assert version.vstring == vstring


# Generated at 2022-06-13 16:58:23.339499
# Unit test for method parse of class SemanticVersion

# Generated at 2022-06-13 16:58:34.791755
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion
    from ansible.module_utils.common._collections_compat import Sequence

    # --------------------------
    # test normal result
    loose_version = LooseVersion("1.2.3")
    result = SemanticVersion.from_loose_version(loose_version)
    assert result.vstring == "1.2.3"
    assert result.major == 1
    assert result.minor == 2
    assert result.patch == 3
    assert result.prerelease == ()
    assert result.buildmetadata == ()
    # --------------------------


    # --------------------------
    # test invalid argument
    invalid_argument = "1.2.3"

# Generated at 2022-06-13 16:58:44.059198
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 16:58:53.836994
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    loose_versions = [
        '1.0.0',
        '2.0.0',
        '3.0.0',
        '4.0.0',
        '5.0.0',
        '6.0.0',
        '7.0.0',
        '8.0.0',
        '9.0.0',
        '10.0.0',
        '11.0.0',
    ]

# Generated at 2022-06-13 16:59:04.292519
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    loose_versions = [
        "1.0",
        "1.0.2",
        "1.0.0a1",
        "2.2.0rc2",
        "0.10.4b4",
        "1.10.4-1",
        "1.0.0+3",
        "2.2.0+1",
        "0.10.4-1+3",
        "1.10.4-2+3"
    ]

    for version in loose_versions:
        assert SemanticVersion.from_loose_version(LooseVersion(version))
        assert SemanticVersion.from_loose_version(LooseVersion(version)) == SemanticVersion(version)

# Generated at 2022-06-13 16:59:23.471298
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    def test_loose_version(loose_version, expected_result):
        assert SemanticVersion.from_loose_version(loose_version) \
        == SemanticVersion(expected_result)

    test_loose_version(LooseVersion('0.0.0'), '0.0.0')
    test_loose_version(LooseVersion('0.0.1'), '0.0.1')
    test_loose_version(LooseVersion('0.1.0'), '0.1.0')
    test_loose_version(LooseVersion('0.1.1'), '0.1.1')
    test_loose_version(LooseVersion('1.0.0'), '1.0.0')

# Generated at 2022-06-13 16:59:31.990968
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test _Alpha
    assert (_Alpha('a') == 'a') is True
    assert (_Alpha('a') == 'b') is False
    assert (_Alpha('b') == _Alpha('a')) is False
    assert (_Alpha('b') != _Alpha('a')) is True
    assert (_Alpha('b') < _Alpha('a')) is False
    assert (_Alpha('b') < _Alpha('c')) is True
    assert (_Alpha('b') > _Alpha('a')) is True
    assert (_Alpha('b') > _Alpha('c')) is False
    assert (_Alpha('b') <= _Alpha('a')) is False
    assert (_Alpha('b') <= _Alpha('c')) is True
    assert (_Alpha('b') >= _Alpha('a')) is True

# Generated at 2022-06-13 16:59:44.487693
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # non-LooseVersion
    try:
        SemanticVersion.from_loose_version(text_type())
        assert False, "Expected exception to be thrown"
    except ValueError:
        pass

    # non-integer values in LooseVersion
    try:
        SemanticVersion.from_loose_version(LooseVersion("1.2.3.beta"))
        assert False, "Expected exception to be thrown"
    except ValueError:
        pass

    # wrong number of values in LooseVersion
    try:
        SemanticVersion.from_loose_version(LooseVersion("1.2.3.4.5"))
        assert False, "Expected exception to be thrown"
    except ValueError:
        pass

    # no pre-release or metadata in LooseVersion
    version = SemanticVersion.from_

# Generated at 2022-06-13 16:59:57.314093
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    sv = SemanticVersion()

    assert sv.parse('0.0.0') == (None, None, None)
    assert sv.parse('0.0.0-prerelease.1') == (None, None, None)
    assert sv.parse('0.0.0+buildmetadata') == (None, None, None)
    assert sv.parse('0.0.0-prerelease.1+buildmetadata') == (None, None, None)
    assert sv.parse('0.0.0-alpha.2.4+buildmetadata') == (None, None, None)
    assert sv.parse('1.0.0') == (None, None, None)
    assert sv.parse('1.0.0-prerelease') == (None, None, None)

# Generated at 2022-06-13 17:00:05.849533
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version('1') == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version('1.2') == SemanticVersion('1.2.0')
    assert SemanticVersion.from_loose_version('1.2.3') == SemanticVersion('1.2.3')

    assert SemanticVersion.from_loose_version('1.2.3-alpha') == SemanticVersion('1.2.3-alpha')
    assert SemanticVersion.from_loose_version('1.2.3-alpha-4') == SemanticVersion('1.2.3-alpha.4')

# Generated at 2022-06-13 17:00:17.666362
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1')).major == 1
    assert SemanticVersion.from_loose_version(LooseVersion('1.2')).minor == 2
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.4')).patch == 4
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.4')).prerelease == ()
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.4')).buildmetadata == ()
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.4-alpha')).prerelease == ('alpha',)
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.4-alpha')).buildmetadata

# Generated at 2022-06-13 17:00:27.178126
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    SemanticVersion('1')
    SemanticVersion('1.0')
    SemanticVersion('1.2.3')
    SemanticVersion('1.2.3-rc1')
    SemanticVersion('1.2.3-rc1+build0')
    SemanticVersion('1.2.3+build0')
    SemanticVersion('1.2.3-rc1.4-alpha')
    SemanticVersion('1.2.3-rc1.4-alpha.12')
    SemanticVersion('1.2.3-rc1.4-alpha.12-beta.15')
    SemanticVersion('1.2.3-rc1.4-alpha.12-beta.15-rc3.35')

# Generated at 2022-06-13 17:00:36.465105
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    x = SemanticVersion()
    y = x.from_loose_version('1.2.3')
    assert y == x.from_loose_version('1.2.3')
    assert y != x.from_loose_version('1.2.4')
    assert y != x.from_loose_version('1.3.3')
    assert y != x.from_loose_version('2.2.3')
    assert y != x.from_loose_version('1.2.3-b')
    assert y != x.from_loose_version('1.2.3+foo')
    assert y == x.from_loose_version('1.2.3-b+foo')
    assert y == x.from_loose_version('1.2.3-1+foo')


# Generated at 2022-06-13 17:00:49.087927
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.6.0')).vstring == '1.6.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.6.0-alpha')).vstring == '1.6.0-alpha'
    assert SemanticVersion.from_loose_version(LooseVersion('1.6.0-alpha.1')).vstring == '1.6.0-alpha.1'
    assert SemanticVersion.from_loose_version(LooseVersion('1.6.0-alpha.1+meta')).vstring == '1.6.0-alpha.1+meta'

# Generated at 2022-06-13 17:00:58.324627
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:01:15.623111
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Unit test for method from_loose_version of class SemanticVersion

    This method is designed to take a ``LooseVersion``
    and attempt to construct a ``SemanticVersion`` from it

    This is useful where you want to do simple version math
    without requiring users to provide a compliant semver.
    """

    # test for version
    form_loose_version = SemanticVersion.from_loose_version(LooseVersion('1.0.0'))

    assert form_loose_version.core == (1, 0, 0)
    assert form_loose_version.is_prerelease is False
    assert form_loose_version.is_stable is True

    # test for version with build metadata

# Generated at 2022-06-13 17:01:25.796248
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Test the method from_loose_version of class SemanticVersion.
    """
    from ansible.module_utils.version import SemanticVersion

    # Test that from_loose_version() creates the correct object.
    assert (type(SemanticVersion.from_loose_version(LooseVersion("1.4.4"))._BaseVersion__ver) ==
            type(SemanticVersion("1.4.4")._BaseVersion__ver))
    assert (type(SemanticVersion.from_loose_version(LooseVersion("1.4.4+"))._BaseVersion__ver) ==
            type(SemanticVersion("1.4.4+")._BaseVersion__ver))

# Generated at 2022-06-13 17:01:38.357725
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.1')) == SemanticVersion('1.0.1')

    assert SemanticVersion.from_loose_version(LooseVersion('1.0.1-1')) == SemanticVersion('1.0.1-1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.1-1.2')) == SemanticVersion('1.0.1-1.2')

# Generated at 2022-06-13 17:01:47.424823
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    def test(expected, actual):
        if not isinstance(expected, text_type):
            expected = text_type(expected)
        assert expected == actual
    # test_SemanticVersion_from_loose_version()

    actual = SemanticVersion.from_loose_version(
        LooseVersion('zero')
    ).vstring
    test('0.0.0', actual)

    actual = SemanticVersion.from_loose_version(
        LooseVersion('0.0.0')
    ).vstring
    test('0.0.0', actual)

    actual = SemanticVersion.from_loose_version(
        LooseVersion('1.2.3')
    ).vstring
    test('1.2.3', actual)


# Generated at 2022-06-13 17:01:55.446981
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose = LooseVersion("1")
    from_loose = SemanticVersion.from_loose_version(loose)
    assert from_loose == "1.0.0"

    loose = LooseVersion("1.2")
    from_loose = SemanticVersion.from_loose_version(loose)
    assert from_loose == "1.2.0"

    loose = LooseVersion("1.2.3")
    from_loose = SemanticVersion.from_loose_version(loose)
    assert from_loose == "1.2.3"

    loose = LooseVersion("1.2.3-1")
    from_loose = SemanticVersion.from_loose_version(loose)
    assert from_loose == "1.2.3-1"

   

# Generated at 2022-06-13 17:02:04.430113
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    Test for method from_loose_version of class SemanticVersion.
    """
    v = SemanticVersion.from_loose_version(LooseVersion('1.0.0'))
    assert v.core == (1, 0, 0)
    assert v.prerelease == ()
    assert v.buildmetadata == ()
    assert v.vstring == '1.0.0'

    v = SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha.1'))
    assert v.core == (1, 0, 0)
    assert v.prerelease == (_Alpha('alpha'), _Numeric('1'))
    assert v.buildmetadata == ()
    assert v.vstring == '1.0.0-alpha.1'

    v = SemanticVersion.from_loose

# Generated at 2022-06-13 17:02:09.717680
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # case when LooseVersion is passed as an object
    v1 = LooseVersion("1.2.3")
    assert SemanticVersion.from_loose_version(v1) == SemanticVersion("1.2.3")

    # case when LooseVersion is passed as an string
    assert SemanticVersion.from_loose_version("1.2.3") == SemanticVersion("1.2.3")

    # case when any other string is passed
    try:
        assert SemanticVersion.from_loose_version("a.2.3")
    except Exception as e:
        assert type(e) == ValueError

    # case when any other object is passed
    try:
        assert SemanticVersion.from_loose_version(123)
    except Exception as e:
        assert type(e) == ValueError



# Generated at 2022-06-13 17:02:20.002618
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    expected = ("-1.2.3", "-1.2.3rc1", "-1.2.3rc1.dev0", "-1.2.3.dev0", "-1.2.3.0",
                "-1.2", "-1", "-1.2rc1", "-1.2rc1.dev0", "-1.2.dev0", "-1.2.0",
                "1.2.3", "1.2.3rc1", "1.2.3rc1.dev0", "1.2.3.dev0", "1.2.3.0",
                "1.2", "1", "1.2rc1", "1.2rc1.dev0", "1.2.dev0", "1.2.0")


# Generated at 2022-06-13 17:02:30.920600
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    string_version = "2018.03.0"
    vl = LooseVersion(string_version)
    v = SemanticVersion.from_loose_version(vl)
    assert v.major == 2018
    assert v.minor == 3
    assert v.patch == 0
    assert v.prerelease == ()
    assert v.buildmetadata == ()

    string_version = "2.0b2+dev"
    vl = LooseVersion(string_version)
    v = SemanticVersion.from_loose_version(vl)
    assert v.major == 2
    assert v.minor == 0
    assert v.patch == 0
    assert v.prerelease == (b'b', 2)
    assert v.buildmetadata == ()

    string_version = "1.4"

# Generated at 2022-06-13 17:02:42.868480
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test with a loose_version that has a valid core version and a build metadata
    lv = LooseVersion('3.2.1+build.metadata')
    sv = SemanticVersion.from_loose_version(lv)
    assert sv.vstring == '3.2.1+build.metadata'

    # Test with a loose_version that has a valid core version and a pre-release specifier
    lv = LooseVersion('3.2.1-pre.release')
    sv = SemanticVersion.from_loose_version(lv)
    assert sv.vstring == '3.2.1-pre.release'

    # Test with a loose_version that has a valid core version, a pre-release specifier, and a build metadata

# Generated at 2022-06-13 17:03:04.306725
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    class TestLooseVersion(LooseVersion):
        version = (1,2,3)

    class TestLooseVersionB(LooseVersion):
        version = (1,2,3,'beta')

    class TestLooseVersionC(LooseVersion):
        version = (1,2,3,4,'beta','gamma','delta','epsilon','zeta','eta')

    class TestLooseVersionD(LooseVersion):
        version = (1,2,3,'beta','gamma','delta','epsilon','zeta','eta')

    assert SemanticVersion.from_loose_version(TestLooseVersion('')).vstring == "1.2.3"
    assert SemanticVersion.from_loose_version(TestLooseVersionB('')).vstring == "1.2.3-beta"
   

# Generated at 2022-06-13 17:03:14.610217
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test with list-type loose version, case 1
    loose_version = LooseVersion('1.2.3.4a5')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version == '1.2.3'

    # Test with list-type loose version, case2
    loose_version = LooseVersion('1.2.3')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version == '1.2.3'

    # Test with text-type loose version, case 1
    loose_version = LooseVersion('1.2.3.4a5')
    loose_version.vstring = '1.2.3.4a5'
    semantic_version = SemanticVersion.from_lo

# Generated at 2022-06-13 17:03:24.502249
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v = SemanticVersion.from_loose_version(LooseVersion('1.1.1'))
    assert '1.1.1' == v.vstring
    v = SemanticVersion.from_loose_version(LooseVersion('1.1.1.1'))
    assert '1.1.1' == v.vstring
    v = SemanticVersion.from_loose_version(LooseVersion('1.1.1.1.1'))
    assert '1.1.1' == v.vstring
    v = SemanticVersion.from_loose_version(LooseVersion('1.1.1-1'))
    assert '1.1.1-1' == v.vstring

# Generated at 2022-06-13 17:03:35.964383
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')).vstring == '1.2.3'
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3a')).vstring == '1.2.3-a'
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3a1')).vstring == '1.2.3-a1'
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3a.1')).vstring == '1.2.3-a.1'
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3a11')).vstring == '1.2.3-a11'
    assert Semantic

# Generated at 2022-06-13 17:03:44.757584
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Get test cases
    test_cases = get_test_cases('SemanticVersion_from_loose_version')

    test_failed = False

    for test_case in test_cases:
        try:
            version = SemanticVersion.from_loose_version(test_case['input'])
            if not isinstance(version, SemanticVersion):
                raise ValueError("from_loose_version returned unexpected result of type %r" % type(version))

            if str(version) != test_case['expected_result']:
                raise ValueError("from_loose_version returned unexpected result %r; expected %r" % (version, test_case['expected_result']))
        except Exception as e:
            print("%s: exception %r" % (test_case['name'], e))
            test_failed = True


# Generated at 2022-06-13 17:03:54.420619
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test conversion from LooseVersion to SemanticVersion
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.0')) == SemanticVersion('0.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.1')) == SemanticVersion('0.0.1')
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.0-alpha')) == SemanticVersion('0.0.0-alpha')
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.0+20130304')) == SemanticVersion('0.0.0+20130304')

    # Test handling of extra characters after the core version

# Generated at 2022-06-13 17:03:58.258155
# Unit test for method parse of class SemanticVersion

# Generated at 2022-06-13 17:04:01.940918
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    Test method from_loose_version of class SemanticVersion
    """
    from ansible.module_utils.compat.version import LooseVersion
    loose_version = LooseVersion('5.5')
    version = SemanticVersion.from_loose_version(loose_version)
    assert(version == '5.5.0')



# Generated at 2022-06-13 17:04:06.956295
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    version = SemanticVersion.from_loose_version(LooseVersion("0.1.1-beta.1"))
    assert version.vstring == "0.1.1-beta.1"
    assert version.major == 0
    assert version.minor == 1
    assert version.patch == 1
    assert version.prerelease == ('beta', _Numeric('1'))
    assert version.buildmetadata == ()
    assert version.is_prerelease
    assert not version.is_stable
    assert version.core == (0, 1, 1)


# Generated at 2022-06-13 17:04:19.451327
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-beta.1')) == SemanticVersion('1.2.3-beta.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+meta')) == SemanticVersion('1.2.3+meta')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3~beta.1')) == SemanticVersion('1.2.3-beta.1')

# Generated at 2022-06-13 17:04:37.791464
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    try:
        SemanticVersion.from_loose_version('0.0.1')
        SemanticVersion.from_loose_version(LooseVersion('0.0.1'))
        SemanticVersion.from_loose_version(text_type('0.0.1'))
    except ValueError:
        assert False, 'ValueError raised in SemanticVersion.from_loose_version'

    try:
        SemanticVersion.from_loose_version(SemanticVersion('0.0.1'))
    except ValueError:
        pass
    else:
        assert False, 'No ValueError raised in SemanticVersion.from_loose_version'

# Generated at 2022-06-13 17:04:50.149166
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.1+build.1.2.3'))
    assert isinstance(loose_version, SemanticVersion) is True
    assert loose_version == '1.2.3-alpha.1+build.1.2.3'
    assert loose_version.is_prerelease is True
    assert loose_version.is_stable is False
    assert loose_version.major == 1
    assert loose_version.minor == 2
    assert loose_version.patch == 3
    assert loose_version.core == (1, 2, 3)
    assert loose_version.prerelease == (_Numeric('alpha'), _Numeric('1'))

# Generated at 2022-06-13 17:05:03.616701
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    Unit test for method from_loose_version of class SemanticVersion.
    """
    loose_version = LooseVersion("0.2.1")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.major == 0
    assert semver.minor == 2
    assert semver.patch == 1
    assert semver.prerelease == ()
    assert semver.buildmetadata == ()

    loose_version = LooseVersion("0.2.1_dev1")
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.major == 0
    assert semver.minor == 2
    assert semver.patch == 1
    assert semver.prerelease == (_Numeric("dev1"),)

# Generated at 2022-06-13 17:05:12.773252
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    tv = SemanticVersion.from_loose_version(LooseVersion('1.0.0'))
    assert(tv.major==1)
    assert(tv.minor==0)
    assert(tv.patch==0)
    assert(tv.prerelease==())
    assert(tv.buildmetadata==())

    tv = SemanticVersion.from_loose_version(LooseVersion('1.0.0dev1'))
    assert(tv.major==1)
    assert(tv.minor==0)
    assert(tv.patch==0)
    assert(tv.prerelease==('dev1',))
    assert(tv.buildmetadata==())

    tv = SemanticVersion.from_loose_version(LooseVersion('1.0.0a1'))
    assert(tv.major==1)
   

# Generated at 2022-06-13 17:05:21.936354
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:05:32.858576
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    result = SemanticVersion.from_loose_version(LooseVersion("1.3.10"))
    assert result == SemanticVersion("1.3.10")
    result = SemanticVersion.from_loose_version(LooseVersion("1.3.10+foo"))
    assert result == SemanticVersion("1.3.10+foo")
    result = SemanticVersion.from_loose_version(LooseVersion("1.3.10-foo"))
    assert result == SemanticVersion("1.3.10-foo")
    result = SemanticVersion.from_loose_version(LooseVersion("1.3.10-foo+bar"))
    assert result == SemanticVersion("1.3.10-foo+bar")

# Generated at 2022-06-13 17:05:44.106319
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')).vstring == '1.0.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha1')).vstring == '1.0.0-alpha1'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build1')).vstring == '1.0.0+build1'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha1+build1')).vstring == '1.0.0-alpha1+build1'


# Generated at 2022-06-13 17:05:56.297962
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion("1.2.3")
    assert loose_version == SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion("1.2.3-alpha.1")
    assert loose_version == SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion("1.2.3-alpha.1+abc.def")
    assert loose_version == SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion("1.2.3+abc.def")
    assert loose_version == SemanticVersion.from_loose_version(loose_version)

    loose_version = LooseVersion("1.2.3.4")
    assert loose_version == SemanticVersion

# Generated at 2022-06-13 17:06:05.483738
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:06:17.582967
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v1 = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3
    assert v1.prerelease == ()

    v1 = SemanticVersion.from_loose_version(LooseVersion('1.2.3-beta.4'))
    assert v1.major == 1
    assert v1.minor == 2
    assert v1.patch == 3
    assert v1.prerelease == (_Alpha('beta'), _Numeric(4))

    v1 = SemanticVersion.from_loose_version(LooseVersion('1.2.3+beta.4'))
    assert v1.major == 1
    assert v1.minor == 2

# Generated at 2022-06-13 17:06:49.661133
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six import PY2
    from ansible.module_utils.distro import LooseVersion

    # Test for string
    try:
        SemanticVersion.from_loose_version("10.0.0")
        assert False
    except ValueError:
        pass

    v1 = LooseVersion("10.8.3")
    v2 = SemanticVersion.from_loose_version(v1)
    assert v2.vstring == "10.8.3"
    assert v1.vstring == "10.8.3"

    v1 = LooseVersion("10.8.3.a.b")
    v2 = SemanticVersion.from_loose_version(v1)
    assert v2.vstring == "10.8.3.a.b"

# Generated at 2022-06-13 17:06:57.261987
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version('0.8') == '0.8.0'
    assert SemanticVersion.from_loose_version('1.2.3') == '1.2.3'
    # normal integers will be cast to strings
    assert SemanticVersion.from_loose_version(1) == '1.0.0'
    assert SemanticVersion.from_loose_version('1.2.3-1') == '1.2.3-1'
    assert SemanticVersion.from_loose_version('1.2.3+4') == '1.2.3+4'
    assert SemanticVersion.from_loose_version('1.2.3-1.2') == '1.2.3-1.2'
    assert SemanticVersion.from_loose_

# Generated at 2022-06-13 17:07:02.220390
# Unit test for method from_loose_version of class SemanticVersion
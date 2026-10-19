

# Generated at 2022-06-13 16:57:28.248854
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    """Validate that the SemanticVersion.parse() method can parse
    valid semver strings.
    """

# Generated at 2022-06-13 16:57:37.552795
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    version = SemanticVersion('0.1.2')
    assert version.major == 0
    assert version.minor == 1
    assert version.patch == 2
    assert version.prerelease == ()
    assert version.buildmetadata == ()

    version = SemanticVersion('1.2.3-alpha.1')
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == (_Alpha('alpha'), _Numeric('1'))
    assert version.buildmetadata == ()

    version = SemanticVersion('1.2.3+build20120401')
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == ()
    assert version.buildmetadata == (_Numeric('build20120401'),)

# Generated at 2022-06-13 16:57:44.849343
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    a = _Alpha('a')
    b = _Alpha('b')
    assert( a <= b )
    assert( a <= 'b' )
    assert( 'a' <= b )

    a = _Alpha('b')
    b = _Alpha('a')
    assert( not( a <= b ) )
    assert( not( a <= 'a' ) )
    assert( not( 'b' <= b ) )
    assert( 'a' < 'b' )


# Generated at 2022-06-13 16:57:53.707125
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('2.0.0.dev0')).is_prerelease
    assert SemanticVersion.from_loose_version(LooseVersion('2.0.0.dev1')).is_prerelease
    assert SemanticVersion.from_loose_version(LooseVersion('2.0.0.b2')).is_prerelease
    assert SemanticVersion.from_loose_version(LooseVersion('2.0.0-rc1')).is_prerelease
    assert SemanticVersion.from_loose_version(LooseVersion('2.0.0-rc1.post0')).is_prerelease
    assert not SemanticVersion.from_loose_version(LooseVersion('2.0.0')).is_prerelease


# Generated at 2022-06-13 16:57:58.292698
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    semver = SemanticVersion()
    assert semver.parse('1.2.3') == None
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3



# Generated at 2022-06-13 16:58:11.414624
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six.moves import cStringIO as StringIO
    import sys

    # Redirect stdout to a string buffer
    stdout = sys.stdout
    sys.stdout = StringIO()

    # Module should be able to recognize and initialize a valid SemanticVersion
    SemanticVersion.from_loose_version(LooseVersion('1.0.0'))
    assert sys.stdout.getvalue() == ''

    # Module should error and exit if a non-LooseVersion is used
    with pytest.raises(ValueError, match='1.0.0 is not a LooseVersion'):
        SemanticVersion.from_loose_version('1.0.0')

    # Module should error and exit if a LooseVersion with more than 3 elements is used

# Generated at 2022-06-13 16:58:24.534255
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # Test from_loose_version helper function with a loose version
    loose_version_object=LooseVersion('1.2.3-alpha4+build5678')
    expected_semantic_version='1.2.3-alpha4+build5678'
    assert SemanticVersion.from_loose_version(loose_version_object) == SemanticVersion(expected_semantic_version)

    # Test from_loose_version helper function with a loose version
    loose_version_object=LooseVersion('1.2.3-alpha4')
    expected_semantic_version='1.2.3-alpha4'
    assert SemanticVersion.from_loose_version(loose_version_object) == SemanticVersion(expected_semantic_version)

    # Test from_loose_version helper function with a loose version

# Generated at 2022-06-13 16:58:37.238175
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    '''Test of method parse of class SemanticVersion'''
    print('test_SemanticVersion_parse()')

# Generated at 2022-06-13 16:58:41.503224
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    comparator = SemanticVersion(vstring = "1.2.3+build.3000")
    tested_comp = SemanticVersion.from_loose_version(
        LooseVersion(vstring = "1.2.3+build.3000")
    )

    assert comparator == tested_comp

# Generated at 2022-06-13 16:58:52.765632
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    # Test an empty version string
    assert SemanticVersion('').parse('') is None

    # Test a non semver version string
    try:
        SemanticVersion('').parse('1')
        raise Exception('SemanticVersion.parse() should have failed due to missing minor version')
    except ValueError:
        pass

    try:
        SemanticVersion('').parse('1.2')
        raise Exception('SemanticVersion.parse() should have failed due to missing patch version')
    except ValueError:
        pass

    # Test a valid semver version string
    semver = SemanticVersion('')
    semver.parse('1.2.3')
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3

# Generated at 2022-06-13 16:59:13.229633
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')).core == (1, 2, 3)
    assert SemanticVersion.from_loose_version(LooseVersion('0.2.3')).core == (0, 2, 3)
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.1')).core == (1, 2, 3)
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+foo.bar')).core == (1, 2, 3)
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+foo.bar')).buildmetadata == ('foo', 'bar')

# Generated at 2022-06-13 16:59:25.161043
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 16:59:30.386176
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six.moves import StringIO as StringIO
    import sys

    saved_stdout = sys.stdout

# Generated at 2022-06-13 16:59:43.147572
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0-alpha')) == SemanticVersion('1.0.0-alpha')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build.1')) == SemanticVersion('1.0.0+build.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build.1-pre.1')) == SemanticVersion('1.0.0+build.1-pre.1')

# Generated at 2022-06-13 16:59:56.241775
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Unit test for the method from_loose_version of class SemanticVersion
    """
    from ansible.module_utils.version import LooseVersion, SemanticVersion
    # Test cases

# Generated at 2022-06-13 17:00:04.837270
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2')) == SemanticVersion('1.2.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')

    assert SemanticVersion.from_loose_version(LooseVersion('1-beta')) == SemanticVersion('1.0.0-beta')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2-beta')) == SemanticVersion('1.2.0-beta')

# Generated at 2022-06-13 17:00:17.223369
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    class LooseV(object):
        def __init__(self, value):
            self.value = value

    try:
        SemanticVersion.from_loose_version(LooseV('1'))
    except ValueError as ve:
        assert ve.args == ("%r is not a LooseVersion" % LooseV('1'),)

    try:
        SemanticVersion.from_loose_version(LooseV('1.1'))
    except ValueError as ve:
        assert ve.args == ("%r is not a LooseVersion" % LooseV('1.1'),)


# Generated at 2022-06-13 17:00:23.414930
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version("1.2.3") == SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version("1.2.3.4") == SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version("1.2.3.4+") == SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version("1.2.3.4+5") == SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version("1.2.3.4+5.6") == SemanticVersion("1.2.3")

# Generated at 2022-06-13 17:00:30.854283
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import unittest
    import distutils.version as version

    class TestFromLooseVersion(unittest.TestCase):
        def test_loose_version_normal(self):
            for v in '1.mb', '0', '1.2.1.4', '1.2-al', '1.2-4.c' '1.2-4.4', '1.2_4.4.4', '1.2.3-4_4.4.4', '1.2.3+4_4.4.4', '1.2.3-pre.2+build.4':
                loose_v = version.LooseVersion(v)
                semantic_v = SemanticVersion.from_loose_version(loose_v)

# Generated at 2022-06-13 17:00:39.045207
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:00:47.564703
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # test valid loose version
    assert SemanticVersion.from_loose_version(LooseVersion('0.1.0-alpha1')) == \
        SemanticVersion('0.1.0-alpha1')
    # test which is not a LooseVersion
    got_exc = False
    try:
        SemanticVersion.from_loose_version('0.1.0-alpha1')
    except ValueError:
        got_exc = True
    assert got_exc
    # test loose version with a non-integer value
    got_exc = False
    try:
        SemanticVersion.from_loose_version(LooseVersion('0.a.0-alpha1'))
    except ValueError:
        got_exc = True
    assert got_exc


# Generated at 2022-06-13 17:00:58.244065
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:01:02.418959
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    result = SemanticVersion.from_loose_version(LooseVersion('1.2.3+build4.5.6'))
    assert result.core == (1, 2, 3)
    assert result.is_stable
    assert result.prerelease == ()
    assert result.buildmetadata == ('build', 4, 5, 6)



# Generated at 2022-06-13 17:01:07.313144
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    input_version = '1.15.0'
    LooseVersion_version = LooseVersion(input_version)
    SemanticVersion_version = SemanticVersion.from_loose_version(LooseVersion_version)
    assert isinstance(SemanticVersion_version, SemanticVersion)
    assert str(LooseVersion_version) == '1.15'
    assert str(SemanticVersion_version) == '1.15.0'


# Generated at 2022-06-13 17:01:13.881756
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3a')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('0.2.3')) == SemanticVersion('0.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3a.4')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2+16.ge927ea0')) == SemanticVersion('1.2')

# Generated at 2022-06-13 17:01:24.593075
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # These are valid versions. Tests that they are converted
    # correctly.
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha')) == SemanticVersion('1.2.3-alpha')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.1')) == SemanticVersion('1.2.3-alpha.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.1.1')) == SemanticVersion('1.2.3-alpha.1.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+20130313144700')) == SemanticVersion('1.2.3+20130313144700')

# Generated at 2022-06-13 17:01:37.734913
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.version import SemanticVersion
    from ansible.module_utils.six import PY2

    # Test that the class works when passed a LooseVersion
    assert SemanticVersion.from_loose_version(SemanticVersion('0.1.2')) == SemanticVersion('0.1.2')

    # Test that it can handle a string
    assert SemanticVersion.from_loose_version('0.1.2') == SemanticVersion('0.1.2')

    if PY2:
        # Test that it can handle a unicode string
        assert SemanticVersion.from_loose_version(u'0.1.2') == SemanticVersion('0.1.2')

    # Test that it can handle a tuple

# Generated at 2022-06-13 17:01:46.870986
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('1.2.3')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3
    assert semver.prerelease == ()
    assert semver.buildmetadata == ()

    loose_version = LooseVersion('1.2.3.4')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3
    assert semver.prerelease == ()
    assert semver.buildmetadata == ()

    loose_version = LooseVersion('1.2.3.dev1')

# Generated at 2022-06-13 17:01:52.615928
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version_assetions = [
        ('0.1', '0.1.0'),
        ('1.11.1', '1.11.1'),
        ('2.2.5+5', '2.2.5+5'),
        ('1.1.0-alpha', '1.1.0-alpha'),
        ('2.2.5-alpha.beta+5', '2.2.5-alpha.beta+5'),
        ('0.1.1-1.2.3-4.5.6', '0.1.1-1.2.3-4.5.6'),
    ]

    for loose_version_str, expected_str in loose_version_assetions:
        loose_version = LooseVersion(loose_version_str)

# Generated at 2022-06-13 17:02:02.574139
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('1.1.1-1.2.3+4.5.6')
    sv = SemanticVersion.from_loose_version(loose_version)
    assert sv.major == 1
    assert sv.minor == 1
    assert sv.patch == 1
    assert sv.prerelease == (_Numeric(1), _Numeric(2), _Numeric(3))
    assert sv.buildmetadata == (_Numeric(4), _Numeric(5), _Numeric(6))

    # https://github.com/ansible/ansible/issues/61624
    loose_version = LooseVersion('1.1.1-1+2.3.4')
    sv = SemanticVersion.from_loose_version(loose_version)
    assert sv.major == 1
    assert sv

# Generated at 2022-06-13 17:02:27.079515
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion('1.0.1') == SemanticVersion.from_loose_version(LooseVersion('1.0.1'))
    assert SemanticVersion('2.0.0') == SemanticVersion.from_loose_version(LooseVersion('2.0'))
    assert SemanticVersion('2.0.0') == SemanticVersion.from_loose_version(LooseVersion('2'))

    assert SemanticVersion('1.0.1-testing') == SemanticVersion.from_loose_version(LooseVersion('1.0.1-testing'))
    assert SemanticVersion('2.0.0-testing') == SemanticVersion.from_loose_version(LooseVersion('2.0-testing'))

# Generated at 2022-06-13 17:02:38.167126
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    test_case_1 = dict()

    test_case_1['loose_version'] = LooseVersion('1.0.0-rc.1+build.1')
    test_case_1['expected'] = SemanticVersion('1.0.0-rc.1+build.1')

    test_case_2 = dict()

    test_case_2['loose_version'] = LooseVersion('1.0.0')
    test_case_2['expected'] = SemanticVersion('1.0.0')

    test_case_3 = dict()

    test_case_3['loose_version'] = LooseVersion('1.0')
    test_case_3['expected'] = SemanticVersion('1.0.0')

    test_case_4 = dict()


# Generated at 2022-06-13 17:02:45.007153
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion("1.0.0")).vstring == "1.0.0"
    assert SemanticVersion.from_loose_version(LooseVersion("1.0.0a.1")).vstring == "1.0.0-a.1"
    assert SemanticVersion.from_loose_version(LooseVersion("1.0.0.a.1")).vstring == "1.0.0"


# Generated at 2022-06-13 17:02:51.096576
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import distutils.version

    # noinspection PyUnusedLocal
    def _test(*args, **kwargs):
        distutils.version.LooseVersion(*args, **kwargs)

    # "Normal" Version
    assert SemanticVersion.from_loose_version(distutils.version.LooseVersion('2.0.3')) == SemanticVersion('2.0.3')
    assert SemanticVersion.from_loose_version(distutils.version.LooseVersion('1.2')) == SemanticVersion('1.2.0')
    assert SemanticVersion.from_loose_version(distutils.version.LooseVersion('1')) == SemanticVersion('1.0.0')

    # Prerelease and Buildmetadata variants

# Generated at 2022-06-13 17:03:03.186316
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2')) == SemanticVersion('1.2.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+build')) == SemanticVersion('1.2.3+build')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-RC1')) == SemanticVersion('1.2.3-RC1')

# Generated at 2022-06-13 17:03:11.973319
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Setup
    loose_version = LooseVersion('1.0.0')

    # Test
    with pytest.raises(ValueError, match=r"2.0.0 is not a LooseVersion"):
        SemanticVersion.from_loose_version('2.0.0')
    assert SemanticVersion.from_loose_version(loose_version).vstring == '1.0.0'
    loose_version = LooseVersion('1.0.0-1')
    assert SemanticVersion.from_loose_version(loose_version).vstring == '1.0.0-1'
    loose_version = LooseVersion('1.0.0+1')
    assert SemanticVersion.from_loose_version(loose_version).vstring == '1.0.0+1'


# Generated at 2022-06-13 17:03:19.937785
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version_1 = LooseVersion("v1.2.3")
    loose_version_2 = LooseVersion("v1.2.3+test")
    loose_version_3 = LooseVersion("v1.2.3-test")
    loose_version_4 = LooseVersion("v1.2.3-test+test")
    loose_version_5 = LooseVersion("v1.2.3-0.0.1+test")

    sem_version_1 = SemanticVersion.from_loose_version(loose_version_1)
    assert "v1.2.3" == str(sem_version_1)

    sem_version_2 = SemanticVersion.from_loose_version(loose_version_2)

# Generated at 2022-06-13 17:03:31.622547
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha')) == SemanticVersion('1.2.3-alpha')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.1')) == SemanticVersion('1.2.3-alpha.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha-1')) == SemanticVersion('1.2.3-alpha-1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha+20130313144700')) == Sem

# Generated at 2022-06-13 17:03:39.478212
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version_strings = [
        '1',
        '1.2',
        '1.2.3',
        '1.2.3-alpha1',
        '1.2.3-alpha1.beta2',
        '1.2.3-alpha1.beta2.rc3',
        '1.2.3+build1',
        '1.2.3-alpha1+build1',
        '1.2.3-alpha1.beta2+build1',
        '1.2.3-alpha1.beta2.rc3+build1'
    ]
    for loose_version_string in loose_version_strings:
        loose_version = LooseVersion(loose_version_string)
        semantic_version = SemanticVersion.from_loose_version(loose_version)
       

# Generated at 2022-06-13 17:03:49.030305
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha')) == SemanticVersion('1.0.0-alpha')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build.1')) == SemanticVersion('1.0.0+build.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build.1-alpha')) == SemanticVersion('1.0.0+build.1-alpha')



# Generated at 2022-06-13 17:04:24.529509
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    input_string = '1.2.3'
    assert SemanticVersion.from_loose_version(LooseVersion(input_string)).vstring == input_string

    input_string = '1.2.3-alpha.1'
    assert SemanticVersion.from_loose_version(LooseVersion(input_string)).vstring == input_string

    input_string = '1.2.3-alpha.1+build.1'
    assert SemanticVersion.from_loose_version(LooseVersion(input_string)).vstring == input_string

    input_string = '1.2.3+build.1'
    assert SemanticVersion.from_loose_version(LooseVersion(input_string)).vstring == input_string

# Generated at 2022-06-13 17:04:31.777104
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('2.1.1-dev')) == SemanticVersion('2.1.1-dev')
    assert SemanticVersion.from_loose_version(LooseVersion('2.1.1')) == SemanticVersion('2.1.1')
    assert SemanticVersion.from_loose_version(LooseVersion('2.1.1dev')) == SemanticVersion('2.1.1-dev')
    assert SemanticVersion.from_loose_version(LooseVersion('2.1.1+dev')) == SemanticVersion('2.1.1+dev')
    assert SemanticVersion.from_loose_version(LooseVersion('2.1.1-1')) == SemanticVersion('2.1.1-1')
    assert Semantic

# Generated at 2022-06-13 17:04:39.426107
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:04:51.437026
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    testobj = SemanticVersion.from_loose_version(LooseVersion("1.2.3"))
    assert testobj.vstring == "1.2.3"

    testobj = SemanticVersion.from_loose_version(LooseVersion("1.2.3.1"))
    assert testobj.vstring == "1.2.3"

    testobj = SemanticVersion.from_loose_version(LooseVersion("1.2.3-4"))
    assert testobj.vstring == "1.2.3-4"

    testobj = SemanticVersion.from_loose_version(LooseVersion("1.2.3-4-5"))
    assert testobj.vstring == "1.2.3-4-5"


# Generated at 2022-06-13 17:05:05.029738
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion

    ver = SemanticVersion.from_loose_version(LooseVersion('1.0'))
    assert isinstance(ver, SemanticVersion)
    assert ver.vstring == '1.0.0'
    
    ver = SemanticVersion.from_loose_version(LooseVersion('1.0.1+1'))
    assert isinstance(ver, SemanticVersion)
    assert ver.vstring == '1.0.1+1'
    
    ver = SemanticVersion.from_loose_version(LooseVersion('1.0.1-1.2.3.4+1.2.3.4.5'))
    assert isinstance(ver, SemanticVersion)

# Generated at 2022-06-13 17:05:17.524947
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # TODO: Remove me when we drop support for Ansible 2.9
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')).vstring == '1.0.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-rc.1')).vstring == '1.0.0-rc.1'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-rc.2+build.1')).vstring == '1.0.0-rc.2+build.1'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha')).vstring == '1.0.0-alpha'

# Generated at 2022-06-13 17:05:29.702099
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    test_cases = [
        ('1.2.3-alpha', SemanticVersion('1.2.3-alpha')),
        ('1.2.3.4', SemanticVersion('1.2.3.4')),
        ('0.0.1+build', SemanticVersion('0.0.1+build')),
        ('1.2.3-alpha+build', SemanticVersion('1.2.3-alpha+build')),
        ('1.2', SemanticVersion('1.2.0')),
        ('1', SemanticVersion('1.0.0')),
        ('1.2.3.4-alpha+build', SemanticVersion('1.2.3-alpha+build')),
    ]

    for version, expected_result in test_cases:
        assert SemanticVersion.from_loose_version

# Generated at 2022-06-13 17:05:37.318853
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    LooseVersion_class = LooseVersion('4.4.0')
    SemanticVersion_class = SemanticVersion.from_loose_version(LooseVersion_class)
    assert (SemanticVersion_class) == (SemanticVersion('4.4.0'))

    LooseVersion_class = LooseVersion('4.4.0-rc0')
    SemanticVersion_class = SemanticVersion.from_loose_version(LooseVersion_class)
    assert (SemanticVersion_class) == (SemanticVersion('4.4.0-rc0'))

    LooseVersion_class = LooseVersion('4.4.0-rc0+build1')
    SemanticVersion_class = SemanticVersion.from_loose_version(LooseVersion_class)

# Generated at 2022-06-13 17:05:50.286254
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version("1.2.3") == SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version("1.2.3-4") == SemanticVersion("1.2.3-4")
    assert SemanticVersion.from_loose_version("1.2.3-4.5") == SemanticVersion("1.2.3-4.5")
    assert SemanticVersion.from_loose_version("1.2.3+4.5") == SemanticVersion("1.2.3+4.5")
    assert SemanticVersion.from_loose_version("1.2.3+4.5-6") == SemanticVersion("1.2.3+4.5-6")
    assert SemanticVersion.from_loose_version

# Generated at 2022-06-13 17:05:59.419846
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils._text import to_native
    from ansible.module_utils.compat.version import LooseVersion
    from ansible.module_utils.version import SemanticVersion

    lv = LooseVersion('2.4.6')
    sv = SemanticVersion.from_loose_version(lv)
    assert sv.__dict__ == {
        'buildmetadata': (),
        'major': 2,
        'minor': 4,
        'patch': 6,
        'prerelease': (),
        'vstring': '2.4.6',
    }

    # test with prerelease
    lv = LooseVersion('2.4.6-alpha1')
    sv = SemanticVersion.from_loose_version(lv)

# Generated at 2022-06-13 17:06:54.985330
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.1.2+build.1.2.3')) == SemanticVersion('1.2.3-alpha.1.2+build.1.2.3')


# Unit test SemanticVersion.__init__

# Generated at 2022-06-13 17:07:05.262382
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert str(SemanticVersion.from_loose_version(LooseVersion('0.0.1'))) == '0.0.1'
    assert str(SemanticVersion.from_loose_version(LooseVersion('0.0.1-alpha.rc1'))) == '0.0.1-alpha.rc1'
    assert str(SemanticVersion.from_loose_version(LooseVersion('1.2.3'))) == '1.2.3'
    assert str(SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.rc1'))) == '1.2.3-alpha.rc1'

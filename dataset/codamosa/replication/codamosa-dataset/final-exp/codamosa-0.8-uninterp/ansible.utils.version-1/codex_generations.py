

# Generated at 2022-06-13 16:57:21.761021
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    vstring = '1.2.3-beta.4+build.metadata'
    semver = SemanticVersion(vstring)
    assert semver.vstring == vstring
    assert semver.major == 1
    assert semver.minor == 2
    assert semver.patch == 3
    assert semver.prerelease == (
        _Numeric(1),
        _Alpha('beta'),
        _Numeric(4),
    )
    assert semver.buildmetadata == (
        _Alpha('build'),
        _Alpha('metadata'),
    )


# Generated at 2022-06-13 16:57:29.589728
# Unit test for method __ge__ of class _Numeric
def test__Numeric___ge__():
    assert not _Numeric(1) >= '2'
    assert _Numeric(1) >= 1
    assert _Numeric(1) >= 0
    assert _Numeric(1) >= '1'
    assert _Numeric(1) >= '0'
    assert not _Numeric(1) >= _Alpha('1')
    assert _Numeric(1) >= _Numeric(1)
    assert _Numeric(1) >= _Numeric(0)

    # This is a regression test for the case where it is evaluating:
    # _Numeric(0) >= _Numeric(1)
    # and the internals end up with:
    # 0 < 1.0
    # which fails on py3
    assert not _Numeric(0) >= _Numeric(1)
    assert not _Numeric(0) >= _Numeric

# Generated at 2022-06-13 16:57:38.285163
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3")) == SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3-beta.2")) == SemanticVersion("1.2.3-beta.2")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3+build.21")) == SemanticVersion("1.2.3+build.21")
    assert SemanticVersion.from_loose_version(LooseVersion("0.2")) == SemanticVersion("0.2.0")

# Generated at 2022-06-13 16:57:47.398835
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion

    # Various valid semver inputs

# Generated at 2022-06-13 16:58:00.088618
# Unit test for method __ge__ of class _Numeric
def test__Numeric___ge__():
    # Test for x <= y
    x = _Numeric(5)
    y = _Numeric(5)
    assert x.__ge__(y)
    x = _Numeric(5)
    y = _Numeric(5)
    assert x.__ge__(y)

    # Test for x <= 0
    x = _Numeric(5)
    assert x.__ge__(0)
    x = _Numeric(0)
    assert x.__ge__(0)

    # Test for 0 <= y
    x = _Numeric(0)
    y = _Numeric(5)
    assert not x.__ge__(y)
    y = _Numeric(-5)
    assert x.__ge__(y)
    x = _Numeric(5)
    assert not x.__ge__

# Generated at 2022-06-13 16:58:13.348477
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """unit test for SemanticVersion.from_loose_version()"""
    from ansible.module_utils.compat.version import LooseVersion

# Generated at 2022-06-13 16:58:25.912215
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v = '1.2.3'
    rv = SemanticVersion.from_loose_version(LooseVersion(v))
    assert rv.major == 1
    assert rv.minor == 2
    assert rv.patch == 3
    assert rv.is_stable
    assert not rv.is_prerelease
    assert not rv.prerelease
    assert not rv.buildmetadata
    assert rv.core == (1, 2, 3)

    v = '1.2.3-alpha.1'
    rv = SemanticVersion.from_loose_version(LooseVersion(v))
    assert rv.major == 1
    assert rv.minor == 2
    assert rv.patch == 3
    assert not rv.is_stable
    assert rv.is_prerelease


# Generated at 2022-06-13 16:58:39.691898
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    test_values = [
        {
            'a_value': '1.0.0',
            'b_value': '1.0.0',
            'expected_result': True
        },
        {
            'a_value': '2.0.0',
            'b_value': '1.0.0',
            'expected_result': False
        },
        {
            'a_value': '1.0.0',
            'b_value': '2.0.0',
            'expected_result': True
        },
    ]

    for test_value in test_values:
        a = _Alpha(test_value['a_value'])
        b = _Alpha(test_value['b_value'])

        assert (a <= b) == test_value['expected_result']

# Unit

# Generated at 2022-06-13 16:58:42.112800
# Unit test for method __eq__ of class _Numeric
def test__Numeric___eq__():
    assert _Numeric(1) == 1
    assert _Numeric(1) != '1'


# Generated at 2022-06-13 16:58:47.018434
# Unit test for method __ge__ of class _Numeric
def test__Numeric___ge__():
    # Test normal operation
    test_obj_1 = _Numeric(1)
    test_obj_2 = _Numeric(2)
    result = test_obj_1.__ge__(test_obj_2)
    assert result is False


# Generated at 2022-06-13 16:59:03.028747
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('1.0.0')
    new_version = SemanticVersion.from_loose_version(loose_version)
    assert new_version.major == 1
    assert new_version.minor == 0
    assert new_version.patch == 0

    loose_version = LooseVersion('1.0.0-alpha.1')
    new_version = SemanticVersion.from_loose_version(loose_version)
    assert new_version.major == 1
    assert new_version.minor == 0
    assert new_version.patch == 0
    assert new_version.prerelease == (text_type('alpha'), _Numeric('1'))
    assert new_version.is_prerelease

    loose_version = LooseVersion('1.0.0+20180101')
    new

# Generated at 2022-06-13 16:59:06.153775
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_versions_to_test = [
        LooseVersion("1.1.1"),
        LooseVersion("1.1.1-alpha.dev"),
        LooseVersion("1.1.1-alpha+1.2.3"),
        LooseVersion("v1.1.1"),
        LooseVersion("v1.1.1-alpha.dev"),
        LooseVersion("v1.1.1-alpha+1.2.3"),
    ]
    for version in loose_versions_to_test:
        SemanticVersion.from_loose_version(version)



# Generated at 2022-06-13 16:59:14.101801
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # Test results of conversion from LooseVersion
    loose_version = LooseVersion('0.0.3')
    assert SemanticVersion.from_loose_version(loose_version) == SemanticVersion('0.0.3')

    loose_version = LooseVersion('0.0.3beta')
    assert SemanticVersion.from_loose_version(loose_version) == SemanticVersion('0.0.3-beta')

    loose_version = LooseVersion('0.0.3-beta')
    assert SemanticVersion.from_loose_version(loose_version) == SemanticVersion('0.0.3-beta')

    loose_version = LooseVersion('0.0.3.beta')

# Generated at 2022-06-13 16:59:19.412823
# Unit test for method __le__ of class _Numeric
def test__Numeric___le__():
    # Test numeric less than numeric
    numeric_1 = _Numeric('1')
    numeric_2 = _Numeric('2')
    assert numeric_1 <= numeric_2

    # Test numeric less than alpha
    numeric_1 = _Numeric('1')
    alpha_2 = _Alpha('2')
    assert numeric_1 <= alpha_2

    # Test alpha less than numeric
    alpha_1 = _Alpha('1')
    numeric_2 = _Numeric('2')
    assert not numeric_2 <= alpha_1

    # Test alpha less than alpha
    alpha_1 = _Alpha('1')
    alpha_2 = _Alpha('2')
    assert alpha_1 <= alpha_2

    # Test numeric equals numeric
    numeric_1 = _Numeric('1')
    assert numeric_1 <= numeric_1

    # Test alpha equals

# Generated at 2022-06-13 16:59:26.152489
# Unit test for method __le__ of class _Numeric
def test__Numeric___le__():
    assert _Numeric(1) <= _Numeric(1)
    assert _Numeric(1) <= _Numeric(2)
    assert not _Numeric(2) <= _Numeric(1)

    assert _Numeric(1) <= 1
    assert _Numeric(1) <= 2
    assert not _Numeric(2) <= 1

    assert _Numeric(1) <= _Alpha('1')
    assert not _Numeric(2) <= _Alpha('1')



# Generated at 2022-06-13 16:59:38.342188
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    test_data = [
        ("10.0.0", "10.0.0"),
        ("1.2.3.dev1", "1.2.3-dev1"),
        ("myTest.5", "myTest.5"),
        ("1.2.3-2.0-0-0", "1.2.3-2.0"),
        ("1.5.5+log.0.1.1", "1.5.5+log.0.1.1"),
        ("1.2b3", "1.2.b3"),
    ]

    for test in test_data:
        assert (
            SemanticVersion.from_loose_version(
                LooseVersion(test[0])
            ).vstring == test[1]
        )



# Generated at 2022-06-13 16:59:42.538476
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha.1')) == SemanticVersion('1.0.0-alpha.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0.rc1-dev')) == SemanticVersion('1.0.0-rc1-dev')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-rc1+dev')) == SemanticVersion('1.0.0-rc1+dev')

# Generated at 2022-06-13 16:59:55.648367
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import unittest
    import ansible.module_utils.compat.version

    class FakeLooseVersion(ansible.module_utils.compat.version.LooseVersion):
        def __init__(self):
            self.version = []
            self.vstring = ''

    class FakeSemanticVersion(ansible.module_utils.compat.version.SemanticVersion):
        def __init__(self):
            self.major = 0
            self.minor = 0
            self.patch = 0
            self.prerelease = ()
            self.buildmetadata = ()

    # No exception should be raised from from_loose_version if given a LooseVersion
    fake_instance = FakeLooseVersion()
    fake_instance.version = [1]
    fake_instance.vstring = '1'
    ansible.module

# Generated at 2022-06-13 17:00:01.827563
# Unit test for method __eq__ of class _Numeric
def test__Numeric___eq__():
    assert _Numeric(1) == 1
    assert _Numeric(1) == _Numeric(1)
    assert _Numeric(1) == _Numeric('1')
    assert _Numeric(1) != 2
    assert _Numeric(1) != _Numeric(2)
    assert _Numeric(1) != _Numeric('2')
    assert _Numeric(1) != _Alpha('1')


# Generated at 2022-06-13 17:00:06.766610
# Unit test for method __le__ of class _Numeric
def test__Numeric___le__():
    a = _Numeric('1')
    b = _Numeric('2')
    c = _Numeric('2')
    d = _Alpha('2')
    assert a < b
    assert a <= b
    assert b <= c
    assert c <= d
    assert b >= c
    assert c >= d

# Generated at 2022-06-13 17:00:20.785710
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Unittest is not imported by default, import it here to make it available
    # without users needing to import it in their code
    # pylint: disable=wrong-import-position
    import unittest

    class TestSemanticVersions(unittest.TestCase):
        """Test the SemanticVersion class"""

        def test_from_loose_version(self):
            """Make sure from_loose_version works as expected"""
            import ansible.module_utils.six

            if ansible.module_utils.six.PY2:
                self.assertEqual(
                    SemanticVersion.from_loose_version(LooseVersion('1')),
                    SemanticVersion('1.0.0')
                )

# Generated at 2022-06-13 17:00:31.102812
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:00:39.208350
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion("1.2.3")
    assert(str(SemanticVersion.from_loose_version(loose_version)) == "1.2.3")
    loose_version = LooseVersion("1.2.3.4")
    assert(str(SemanticVersion.from_loose_version(loose_version)) == "1.2.3")
    loose_version = LooseVersion("1.2.3-alpha")
    assert(str(SemanticVersion.from_loose_version(loose_version)) == "1.2.3-alpha")
    loose_version = LooseVersion("1.2.3+metadata")
    assert(str(SemanticVersion.from_loose_version(loose_version)) == "1.2.3+metadata")
    lo

# Generated at 2022-06-13 17:00:50.792571
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # A loose version with modifier at end of version specifier
    assert SemanticVersion.from_loose_version(
        LooseVersion('1.0')
    ) == SemanticVersion('1.0.0')

    assert SemanticVersion.from_loose_version(
        LooseVersion('1.0+test')
    ) == SemanticVersion('1.0.0+test')

    assert SemanticVersion.from_loose_version(
        LooseVersion('1.0-test')
    ) == SemanticVersion('1.0.0-test')

    # A loose version with buildmetadata and prerelease modifiers
    # at end of version specifier

# Generated at 2022-06-13 17:00:59.090698
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version('1.2') == SemanticVersion('1.2.0')
    assert SemanticVersion.from_loose_version('1.2.3') == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version('1.2.3+foo') == SemanticVersion('1.2.3+foo')
    assert SemanticVersion.from_loose_version('1.2.3-foo') == SemanticVersion('1.2.3-foo')
    assert SemanticVersion.from_loose_version('1.2.3-foo.1') == SemanticVersion('1.2.3-foo.1')
    assert SemanticVersion.from_loose_version('1.2.3-foo.1+foo.2') == Semantic

# Generated at 2022-06-13 17:01:07.963580
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+1.2')) == SemanticVersion('1.0.0+1.2')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha.0.1')) == SemanticVersion('1.0.0-alpha.0.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+1.2-alpha.0.1')) == SemanticVersion('1.0.0+1.2-alpha.0.1')

# Generated at 2022-06-13 17:01:19.874894
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version(): # noqa
    from ansible.module_utils._text import to_native
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.six import string_types

    # Create a module for testing purposes
    module = AnsibleModule(argument_spec={})

    loose_versions = {}
    loose_versions[LooseVersion('0.0.0')] = SemanticVersion('0.0.0')
    loose_versions[LooseVersion('0.0.1')] = SemanticVersion('0.0.1')
    loose_versions[LooseVersion('0.1.0')] = SemanticVersion('0.1.0')

# Generated at 2022-06-13 17:01:28.446936
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:01:40.647251
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Unit test of method from_loose_version of class SemanticVersion
    # Tests the method works fine with expected outputs
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1-alpha.3')) == SemanticVersion('1.0.0-alpha.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha.3')) == SemanticVersion('1.0.0-alpha.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build.4')) == SemanticVersion('1.0.0+build.4')
    assert SemanticVersion.from_

# Generated at 2022-06-13 17:01:49.078386
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    list_loose_versions = [
        '1.2',
        '1.2.3',
        '1.2.3.4',
        '1.2.3+5.6',
        '1.2+3.4',
        '1+2',
        '1.2-beta.1',
        '1.2.3-beta.1.2',
    ]

# Generated at 2022-06-13 17:02:06.730343
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Test method from_loose_version of class SemanticVersion

    """
    # pylint: disable=import-error,import-outside-toplevel
    try:
        from distutils.version import LooseVersion
    except ImportError:
        from distutils.version import StrictVersion as LooseVersion

    # LooseVersion is able to compare release tags
    # so we add a hack to make it not do that
    # Note: this requires _prefix to exist in LooseVersion
    if not hasattr(LooseVersion, '_prefix'):
        LooseVersion._prefix = None

    # This is the string that from_loose_version should return
    semver_string = '1.2.3+build.metadata.3.8'
    # This is the string that LooseVersion will return

# Generated at 2022-06-13 17:02:12.328144
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    input_versions = [
        '1.0.0-a.b.c.d',
        '0.2.3+0.2.3',
        '1.0.0-0.3.7',
        '1.0.0-0.3.7-rc.2',
        '1.0.0+build.42'
    ]

    expected_versions = [
        '1.0.0-a.b.c.d',
        '0.2.3+0.2.3',
        '1.0.0-0.3.7',
        '1.0.0-0.3.7-rc.2',
        '1.0.0+build.42'
    ]


# Generated at 2022-06-13 17:02:23.096517
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha("1") <= _Alpha("1")
    assert _Alpha("1") <= _Alpha("2")
    assert not _Alpha("3") <= _Alpha("1")

    assert _Alpha("1") <= "1"
    assert _Alpha("1") <= "2"
    assert not _Alpha("3") <= "1"

    assert not _Alpha("1") <= _Numeric("1")
    assert not _Alpha("1") <= 1

    try:
        _Alpha("1") <= 1.0
    except ValueError:
        pass
    else:
        assert False, "_Alpha should not be compared to a float"



# Generated at 2022-06-13 17:02:32.582241
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six import b
    from ansible.module_utils.common.text.converters import to_text
    import ansible.module_utils.basic

    version = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(
            version=dict(required=True, type='str')
        )
    ).params['version']

    if isinstance(version, text_type):
        version = b(version)
    else:
        version = to_text(version, errors='surrogate_or_strict')

    loose_version = LooseVersion(version)
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert isinstance(semantic_version, SemanticVersion)
    assert semantic_version == loose_version


# Generated at 2022-06-13 17:02:44.460532
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test the case that all the values in LooseVersion's 'version' tuple are integers
    loose_version = LooseVersion('1.22.3-rc.3-45')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '1.22.3-rc.3-45'

    # Test the case that one value in LooseVersion's 'version' tuple is non-integer
    loose_version = LooseVersion('1.22.3-rc.4beta-45')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '1.22.3-rc.4beta-45'

    # Test the case that all the values in LooseVersion's 'version' tuple are non-integer
    loose_version = Loose

# Generated at 2022-06-13 17:02:52.477318
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:02:59.477250
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    sver = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    assert sver.core == (1, 2, 3)
    assert sver.is_stable

    sver = SemanticVersion.from_loose_version(LooseVersion('1.1.4.4'))
    assert sver.core == (1, 1, 4)
    assert sver.is_stable

    sver = SemanticVersion.from_loose_version(LooseVersion('1.2'))
    assert sver.core == (1, 2, 0)
    assert sver.is_stable

    sver = SemanticVersion.from_loose_version(LooseVersion('1.2.3.4.5'))
    assert sver.core == (1, 2, 3)


# Generated at 2022-06-13 17:03:10.084819
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion("0.0.1")).__str__() == "0.0.1"
    assert SemanticVersion.from_loose_version(LooseVersion("0.0.2")).__str__() == "0.0.2"
    assert SemanticVersion.from_loose_version(LooseVersion("1.0.0")).__str__() == "1.0.0"
    assert SemanticVersion.from_loose_version(LooseVersion("2.2.2")).__str__() == "2.2.2"
    assert SemanticVersion.from_loose_version(LooseVersion("2.2.2-alpha")).__str__() == "2.2.2-alpha"
    assert SemanticVersion.from_loose

# Generated at 2022-06-13 17:03:13.614459
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    return (_Alpha('a') <= _Alpha('b')) and (_Alpha('a') <= 'b')


# Generated at 2022-06-13 17:03:17.151518
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # test comparison of a version with itself
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3")) == SemanticVersion("1.2.3")



# Generated at 2022-06-13 17:03:38.935745
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Argument is not a LooseVersion
    try:
        SemanticVersion.from_loose_version('x')
        raise AssertionError('SemanticVersion.from_loose_version(x) should have raised ValueError')
    except ValueError:
        pass

    # LooseVersion has non integer values
    try:
        SemanticVersion.from_loose_version(LooseVersion('0.a'))
        raise AssertionError('SemanticVersion.from_loose_version(LooseVersion("0.a")) should have raised ValueError')
    except ValueError:
        pass

    # LooseVersion has fewer than 3 values
    v = SemanticVersion.from_loose_version(LooseVersion('0'))
    assert v.__repr__() == repr(SemanticVersion('0.0.0'))

# Generated at 2022-06-13 17:03:49.365270
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version('0.1-alpha').vstring == '0.1.0-alpha'
    assert SemanticVersion.from_loose_version('0.1+3.2').vstring == '0.1.0+3.2'
    assert SemanticVersion.from_loose_version('0.1.1b').vstring == '0.1.1'
    assert SemanticVersion.from_loose_version('0.1.1b+3.2-beta').vstring == '0.1.1+3.2-beta'
    assert SemanticVersion.from_loose_version('0.1.1beta').vstring == '0.1.1'

# Generated at 2022-06-13 17:03:57.251357
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    version_string = '9.9.9'
    loose_version = LooseVersion(version_string)
    semver = SemanticVersion.from_loose_version(loose_version)
    assert isinstance(semver, SemanticVersion)
    assert semver.vstring == version_string

    version_string = '9.9.9.dev0'
    loose_version = LooseVersion(version_string)
    semver = SemanticVersion.from_loose_version(loose_version)
    assert isinstance(semver, SemanticVersion)
    assert semver.vstring == version_string
    assert semver.is_prerelease

    version_string = '9.9.9+sep01'
    loose_version = LooseVersion(version_string)

# Generated at 2022-06-13 17:04:06.583364
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # For 1.2.3, we should get SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version(
        LooseVersion("1.2.3")
    ) == SemanticVersion("1.2.3")

    # For 1.2.3-alpha.1, we should get SemanticVersion("1.2.3-alpha.1")
    assert SemanticVersion.from_loose_version(
        LooseVersion("1.2.3-alpha.1")
    ) == SemanticVersion("1.2.3-alpha.1")

    # For 1.2.3-alpha.1+build.1, we should get SemanticVersion("1.2.3-alpha.1+build.1")

# Generated at 2022-06-13 17:04:12.033372
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('2.0.0-rc.1')) == SemanticVersion('2.0.0-rc.1')
    assert SemanticVersion.from_loose_version(LooseVersion('3.0.0-rc.1+build.1')) == SemanticVersion('3.0.0-rc.1+build.1')
    assert SemanticVersion.from_loose_version(LooseVersion('4.0.0-rc.1+build.1')) == SemanticVersion('4.0.0-rc.1+build.1')

# Generated at 2022-06-13 17:04:23.825277
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.common.version import LooseVersion
    from ansible.module_utils.common.version import SemanticVersion


# Generated at 2022-06-13 17:04:31.218256
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:04:39.151068
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    versions = [
        '0.0.0',
        '1.0.0',
        '1.2.3',
        '2.0.5-beta.2',
        '2.0.5-beta.10.1',
        '2.0.5-beta.10a.1',
        '2.0.5+build.1',
        '2.0.5'
    ]
    for version in versions:
        expected = SemanticVersion(version)
        loose_version = LooseVersion(version)

        actual = SemanticVersion.from_loose_version(loose_version)
        assert expected.core == actual.core
        assert expected.prerelease == actual.prerelease
        assert expected.buildmetadata == actual.buildmetadata

# Generated at 2022-06-13 17:04:51.232829
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Success case
    loose_version = LooseVersion("1.2.3-4")
    assert SemanticVersion.from_loose_version(loose_version) == "1.2.3-4"
    loose_version = LooseVersion("1.2.3")
    assert SemanticVersion.from_loose_version(loose_version) == "1.2.3"
    loose_version = LooseVersion("1.2.3-alpha.1+build.1")
    assert SemanticVersion.from_loose_version(loose_version) == "1.2.3-alpha.1+build.1"
    loose_version = LooseVersion("1.2.3-hello")

# Generated at 2022-06-13 17:05:04.779763
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:05:27.170433
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    def new_loose(v):
        return LooseVersion(v)

    def new_semantic(v):
        return SemanticVersion(v)

    # TODO: Maybe some more tests for SemanticVersion class with py version checking?

    # Examples for version strings from https://semver.org/#spec-item-10

# Generated at 2022-06-13 17:05:35.694141
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-pre')) == SemanticVersion('1.0.0-pre')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-pre+build')) == SemanticVersion('1.0.0-pre+build')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build')) == SemanticVersion('1.0.0+build')

# Generated at 2022-06-13 17:05:44.163192
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion("1.1.1.SNAPSHOT+hash.code")
    semantic_version = SemanticVersion.from_loose_version(loose_version)

    if semantic_version.vstring != "1.1.1-SNAPSHOT+hash.code":
        raise ValueError("SemanticVersion conversion failed: %r" % semantic_version)
    if semantic_version.is_stable:
        raise ValueError("SemanticVersion conversion failed: %r is not a prerelease version" % semantic_version)


# Generated at 2022-06-13 17:05:56.342859
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    versions = {
        '1.2.3-alpha': '1.2.3-alpha',
        '1.2.3': '1.2.3',
        '1.2.3-alpha+test': '1.2.3-alpha+test',
        '1.2.3+test': '1.2.3+test',
        '1.2.3.4.5.6': '1.2.3',
        '1.2.3-alpha.1.2.3.4': '1.2.3-alpha.1.2.3.4',
        '1.2.3-1.2.3-alpha': '1.2.3-1.2.3-alpha',
    }


# Generated at 2022-06-13 17:06:05.521361
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    assert(SemanticVersion.from_loose_version(LooseVersion("0.0.1")) == SemanticVersion("0.0.1"))
    assert(SemanticVersion.from_loose_version(LooseVersion("0.0.1-alpha")) == SemanticVersion("0.0.1-alpha"))
    assert(SemanticVersion.from_loose_version(LooseVersion("0.0.1-alpha.1")) == SemanticVersion("0.0.1-alpha.1"))
    assert(SemanticVersion.from_loose_version(LooseVersion("0.0.1-alpha.1+build.1")) == SemanticVersion("0.0.1-alpha.1+build.1"))


# Generated at 2022-06-13 17:06:17.678764
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    def assert_equals(semver, loose_version):
        assert semver == SemanticVersion.from_loose_version(loose_version)

    assert_equals(SemanticVersion('1.2.3'), LooseVersion('1.2.3'))
    assert_equals(SemanticVersion('1.2.3-alpha.1'), LooseVersion('1.2.3-alpha.1'))
    assert_equals(SemanticVersion('1.2.3-alpha.1+build.1234'), LooseVersion('1.2.3-alpha.1+build.1234'))
    assert_equals(SemanticVersion('1.2.3'), LooseVersion('1.2.3.0'))

# Generated at 2022-06-13 17:06:29.604209
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:06:38.287402
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')) == SemanticVersion('1.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0-alpha')) == SemanticVersion('1.0.0-alpha')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0+build')) == SemanticVersion('1.0.0+build')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0-alpha+build')) == SemanticVersion('1.0.0-alpha+build')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0-1')) == SemanticVersion('1.0.0-1')
    assert SemanticVersion.from_lo

# Generated at 2022-06-13 17:06:46.111948
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version('1.2.3')
    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(LooseVersion('1.2.3-RC1'))

# Generated at 2022-06-13 17:06:54.939919
# Unit test for method from_loose_version of class SemanticVersion
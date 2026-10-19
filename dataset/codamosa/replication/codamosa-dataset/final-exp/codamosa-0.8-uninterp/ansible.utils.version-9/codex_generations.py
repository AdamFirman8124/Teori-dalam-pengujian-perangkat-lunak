

# Generated at 2022-06-13 16:57:35.135163
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version('10.1.1') == SemanticVersion('10.1.1')
    assert SemanticVersion.from_loose_version('10.1') == SemanticVersion('10.1.0')
    assert SemanticVersion.from_loose_version('0.0.1') < SemanticVersion('0.1.0')
    assert SemanticVersion.from_loose_version('0.1.2') < SemanticVersion('0.2.0')
    assert SemanticVersion.from_loose_version('1.1.2') > SemanticVersion('0.2.0')
    assert SemanticVersion.from_loose_version('0.1.2b') < SemanticVersion('0.1.2')

# Generated at 2022-06-13 16:57:45.169922
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    from pytest import raises
    from ansible.module_utils.semver import SemanticVersion
    # cases from https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string
    # 1.0.0-alpha+001, 1.0.0+20130313144700, 1.0.0-beta+exp.sha.5114f85

# Generated at 2022-06-13 16:57:54.001915
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from distutils.version import LooseVersion
    SemanticVersion_from_loose_version = SemanticVersion.from_loose_version
    assert SemanticVersion_from_loose_version(
        LooseVersion('1.2.3a4')
    ) == SemanticVersion('1.2.3-a4')
    assert SemanticVersion_from_loose_version(
        LooseVersion('1.2.3.dev4')
    ) == SemanticVersion('1.2.3-dev4')
    assert SemanticVersion_from_loose_version(
        LooseVersion('1.2.3b4')
    ) == SemanticVersion('1.2.3-b4')

# Generated at 2022-06-13 16:57:59.173256
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 16:58:05.554336
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import pytest
    # Test normal case
    loose_version = LooseVersion('1.5.5-beta1.1+3.g8dda.2')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version == '1.5.5-beta1.1+3.g8dda.2'
    # Test loose version with no extra
    loose_version = LooseVersion('1.5.5')
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version == '1.5.5'
    # Test loose version with wrong extra
    loose_version = LooseVersion('1.5.5a')

# Generated at 2022-06-13 16:58:12.735412
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    assert SemanticVersion('1.0.0').core == (1, 0, 0)
    assert SemanticVersion('1.0.0-alpha').core == (1, 0, 0)
    assert SemanticVersion('1.0.0+build').core == (1, 0, 0)
    assert SemanticVersion('1.0.0-alpha+build').core == (1, 0, 0)


# Generated at 2022-06-13 16:58:25.427018
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():

    # Test basic integer version
    version = SemanticVersion()
    version.parse('1.2.3')
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == ()
    assert version.buildmetadata == ()

    # Test basic prerelease version
    version = SemanticVersion()
    version.parse('1.2.3-alpha.123')
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == (_Alpha('alpha'), _Numeric(123))
    assert version.buildmetadata == ()

    # Test basic buildmetadata version
    version = SemanticVersion()
    version.parse('1.2.3+abcde12345')
    assert version.major == 1
    assert version

# Generated at 2022-06-13 16:58:31.425228
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    test = SemanticVersion('1.2.3-prerelease+buildmetadata')
    assert test.major == 1
    assert test.minor == 2
    assert test.patch == 3
    assert test.prerelease == tuple()
    assert test.buildmetadata == tuple()


# Generated at 2022-06-13 16:58:42.306687
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v1 = SemanticVersion.from_loose_version(LooseVersion("1.0.0"))
    assert v1.is_stable
    assert v1.major == 1
    assert v1.minor == 0
    assert v1.patch == 0
    assert not v1.prerelease
    assert not v1.buildmetadata

    v2 = SemanticVersion.from_loose_version(LooseVersion("1.0.0-3.el7.x86_64"))
    assert not v2.is_stable
    assert v2.major == 1
    assert v2.minor == 0
    assert v2.patch == 0
    assert v2.prerelease == (_Numeric("3"), _Alpha("el7"), _Alpha("x86_64"))
    assert not v2.buildmetadata

    v3 = Semantic

# Generated at 2022-06-13 16:58:48.303534
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    version = SemanticVersion()

# Generated at 2022-06-13 16:59:05.517773
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.4.4.dev0+a4b7c9b.dirty')) == SemanticVersion('1.4.4-dev0+a4b7c9b.dirty')
    assert SemanticVersion.from_loose_version(LooseVersion('1.4.4.dev0')) == SemanticVersion('1.4.4-dev0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.4.4.post0')) == SemanticVersion('1.4.4')
    assert SemanticVersion.from_loose_version(LooseVersion('1.4.4.post1')) == SemanticVersion('1.4.4')

# Generated at 2022-06-13 16:59:13.700450
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(
        LooseVersion('1.2.3')
    ) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(
        LooseVersion('1.2.3-a1')
    ) == SemanticVersion('1.2.3-a1')
    assert SemanticVersion.from_loose_version(
        LooseVersion('1.2.3-a1+b1')
    ) == SemanticVersion('1.2.3-a1+b1')
    assert SemanticVersion.from_loose_version(
        LooseVersion('1.2.3.4')
    ) == SemanticVersion('1.2.3')

# Generated at 2022-06-13 16:59:25.571855
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from distutils.version import LooseVersion


# Generated at 2022-06-13 16:59:38.293684
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion("1")) == SemanticVersion("1.0.0")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2")) == SemanticVersion("1.2.0")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3")) == SemanticVersion("1.2.3")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3~dev1")) == SemanticVersion("1.2.3-dev1")
    assert SemanticVersion.from_loose_version(LooseVersion("1.2.3.dev1")) == SemanticVersion("1.2.3-dev1")

# Generated at 2022-06-13 16:59:51.999293
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
     assert SemanticVersion.from_loose_version(LooseVersion('1.0.0a')) == SemanticVersion('1.0.0-a')
     assert SemanticVersion.from_loose_version(LooseVersion('1.0.0b')) == SemanticVersion('1.0.0-b')
     assert SemanticVersion.from_loose_version(LooseVersion('0.0.0-x.7.z.92')) == SemanticVersion('0.0.0-x.7.z.92')
     assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-rc.1')) == SemanticVersion('1.2.3-rc.1')
     assert SemanticVersion.from_loose_version(LooseVersion('2.0')) == Semantic

# Generated at 2022-06-13 17:00:00.933678
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    for semver, loose in (
        ("0.0.0", "0"),
        ("0.0.1", "0.1"),
        ("0.1.1", "0.1.1"),
        ("1.1.1", "01.1.01"),
        ("1.1.1-alpha", "01.01.01-alpha"),
        ("1.1.1+alpha", "01.01.01+alpha"),
        ("1.1.1-beta.1+alpha", "01.01.01-beta.1+alpha"),
    ):
        assert SemanticVersion.from_loose_version(LooseVersion(loose)) == SemanticVersion(semver)
    try:
        SemanticVersion.from_loose_version('1.0')
        assert False
    except:
        pass


# Generated at 2022-06-13 17:00:09.325761
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.0')) == SemanticVersion('0.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('2.4.4')) == SemanticVersion('2.4.4')
    assert SemanticVersion.from_loose_version(LooseVersion('2.4.4dev')) == SemanticVersion('2.4.4')
    assert SemanticVersion.from_loose_version(LooseVersion('2.4')) == SemanticVersion('2.4.0')


# Generated at 2022-06-13 17:00:13.094841
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha('2') <= _Alpha('2')
    assert _Alpha('2') <= _Alpha('3')
    assert not _Alpha('2') <= _Alpha('1')

    assert _Alpha('2') <= '2'
    assert _Alpha('2') <= '3'
    assert not _Alpha('2') <= '1'

    assert not _Alpha('2') <= _Numeric('2')


# Generated at 2022-06-13 17:00:21.470001
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """
    :rtype: object
    """
    versions = [
        ('1.0.0-beta.1', '1.0.0-beta.1'),
        ('1.0', '1.0.0'),
        ('1.0.0', '1.0.0'),
        ('1.0.0-rc.1', '1.0.0-rc.1'),
        ('1.0.0-alpha.beta', '1.0.0-alpha.beta'),
        ('1.0.0-0.3.7', '1.0.0-0.3.7'),
        ('1.0.0-x.7.z.92', '1.0.0-x.7.z.92')
    ]

# Generated at 2022-06-13 17:00:29.758857
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion
    loose_version = LooseVersion('1')
    assert isinstance(loose_version, LooseVersion)
    # fails with a ValueError
    try:
        SemanticVersion.from_loose_version(loose_version)
    except ValueError as e:
        assert "Non integer values in LooseVersion ('1')" in str(e)
    else:
        raise Exception("Should have raised an exception")

    loose_version = LooseVersion('1.2.3')
    assert isinstance(loose_version, LooseVersion)
    # fails with a ValueError

# Generated at 2022-06-13 17:00:41.395455
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha('a') <= _Alpha('b')
    assert _Alpha('a') <= _Alpha('a')
    assert _Alpha('b') > _Alpha('a')
    assert _Alpha('b') >= _Alpha('a')


# Generated at 2022-06-13 17:00:52.393567
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha('1') <= _Alpha('1'), '1 should be less than or equal to 1'
    assert not (_Alpha('2') <= _Alpha('1')), '2 should be greater than 1'
    assert not (_Alpha('1') <= _Alpha('2')), '1 should be less than 2'
    assert not (_Alpha('1') <= _Alpha('1.1')), '1 should be less than 1.1'
    assert _Alpha('1') <= _Alpha('1.0'), '1 should be less than or equal to 1.0'
    assert not (_Alpha('1.0') <= _Alpha('1')), '1.0 should be greater than 1'
    assert _Alpha('1.0') <= _Alpha('1.0'), '1.0 should be less than or equal to 1.0'

# Generated at 2022-06-13 17:01:00.898370
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion

    loose_version = LooseVersion('1.2.3.4')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert (semver.major, semver.minor, semver.patch) == (1, 2, 3)

    loose_version = LooseVersion('1.2.3a1')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert (semver.major, semver.minor, semver.patch) == (1, 2, 3)
    assert semver.prerelease == ('a1',)

    loose_version = LooseVersion('1.2.3.4a1')
    semver = SemanticVersion.from_loose_

# Generated at 2022-06-13 17:01:06.327092
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import sys
    import os.path

    sys.path.append(os.path.dirname(__file__))
    import test_versions

    for version_string, expected in test_versions.VERSION_TESTS:
        test_version = SemanticVersion(version_string)
        loose_version = LooseVersion(version_string)
        semantic_version = SemanticVersion.from_loose_version(loose_version)
        assert test_version == semantic_version

# Generated at 2022-06-13 17:01:18.790049
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    from ansible.module_utils.common.versions import LooseVersion

    target_version = SemanticVersion('1.0.10')
    loose_version = LooseVersion('1.0.10')
    assert target_version == SemanticVersion.from_loose_version(loose_version)

    target_version = SemanticVersion('1.0.10b1')
    loose_version = LooseVersion('1.0.10b1')
    assert target_version == SemanticVersion.from_loose_version(loose_version)

    target_version = SemanticVersion('1.0.10b1')
    loose_version = LooseVersion('1.0.10.b1')
    assert target_version == SemanticVersion.from_loose_version(loose_version)

    target_version = SemanticVersion

# Generated at 2022-06-13 17:01:27.786860
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Test SemanticVersion's from_loose_version method"""
    from ansible.module_utils.compat.version import LooseVersion
    from ansible.module_utils.six import PY2

# Generated at 2022-06-13 17:01:39.472252
# Unit test for method __le__ of class _Alpha

# Generated at 2022-06-13 17:01:48.261462
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('1.2.3.4')
    assert(isinstance(SemanticVersion.from_loose_version(loose_version), SemanticVersion))
    loose_version = LooseVersion('1.2.3')
    assert(isinstance(SemanticVersion.from_loose_version(loose_version), SemanticVersion))
    loose_version = LooseVersion('1.2')
    assert(isinstance(SemanticVersion.from_loose_version(loose_version), SemanticVersion))
    loose_version = LooseVersion('1')
    assert(isinstance(SemanticVersion.from_loose_version(loose_version), SemanticVersion))
    loose_version = LooseVersion('1.2.3+4')

# Generated at 2022-06-13 17:01:56.571505
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    def test(specifier1, specifier2):
        print("specifier1", specifier1)
        print("specifier2", specifier2)
        alpha1 = _Alpha(specifier1)
        alpha2 = _Alpha(specifier2)
        print(alpha1, '<=', alpha2, ':', alpha1 <= alpha2)

    test('a', 'b')
    test('a', 'a')
    test('b', 'a')
    test('b', 'b')
    print()


# Generated at 2022-06-13 17:02:01.010439
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    # Test for a equal objects
    assert _Alpha('a.a') <= _Alpha('a.a')
    # Test for a not equal objects
    assert _Alpha('a.a') <= _Alpha('a.b')
    # Test for a not equal objects
    assert not _Alpha('a.b') <= _Alpha('a.a')


# Generated at 2022-06-13 17:02:16.044746
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.common.version import LooseVersion

    # Result is same for int and string
    for lv_str, sv_str in [
        ('2.1.1', '2.1.1'),
        ('V2.1.1', 'V2.1.1'),
        ('proxysql-2.1.1', 'proxysql-2.1.1'),
    ]:
        assert SemanticVersion.from_loose_version(
            LooseVersion(lv_str)
        ).vstring == sv_str

    # Result is same for integers and strings

# Generated at 2022-06-13 17:02:28.313336
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    LooseVersion = LooseVersion

    # Test integer style
    loose_version = LooseVersion('1.3.3')
    assert str(SemanticVersion.from_loose_version(loose_version)) == '1.3.3'

    # Test string style
    loose_version = LooseVersion('1.3.3b')
    assert str(SemanticVersion.from_loose_version(loose_version)) == '1.3.3+0'
    loose_version = LooseVersion('1.3.3b.dev22')
    assert str(SemanticVersion.from_loose_version(loose_version)) == '1.3.3+0'

    # Test string style with tags
    loose_version = LooseVersion('1.3.3b')

# Generated at 2022-06-13 17:02:35.335120
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v_lc = '0.9.0.0.1-alpha+dfsg1'
    v_lc_conv = SemanticVersion.from_loose_version(LooseVersion(v_lc))
    assert v_lc_conv.vstring == '0.9.0-alpha+dfsg1'
    v_lc_conv = SemanticVersion.from_loose_version(v_lc)
    assert v_lc_conv.vstring == '0.9.0-alpha+dfsg1'
    v_c = '0.9.0+dfsg1'
    v_c_conv = SemanticVersion.from_loose_version(v_c)
    assert v_c_conv.vstring == v_c

# Generated at 2022-06-13 17:02:46.240222
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from distutils.version import LooseVersion

    # Test for simple version number
    version = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    assert version == SemanticVersion('1.2.3')

    # Test for simple version number, with pre-release specifier
    version = SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha'))
    assert version == SemanticVersion('1.2.3-alpha')

    # Test for simple version number, with build specifier
    version = SemanticVersion.from_loose_version(LooseVersion('1.2.3+20200101'))
    assert version == SemanticVersion('1.2.3+20200101')

    # Test for simple version number, with pre-release and build specifiers


# Generated at 2022-06-13 17:02:58.218515
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v1 = SemanticVersion.from_loose_version(LooseVersion('5'))
    v2 = SemanticVersion.from_loose_version(LooseVersion('5.2'))
    v3 = SemanticVersion.from_loose_version(LooseVersion('5.2.3'))
    v4 = SemanticVersion.from_loose_version(LooseVersion('5.2.3.alpha'))
    v5 = SemanticVersion.from_loose_version(LooseVersion('5.2.3.beta'))
    v6 = SemanticVersion.from_loose_version(LooseVersion('5.2.3.rc'))
    v7 = SemanticVersion.from_loose_version(LooseVersion('5.2.3.alpha1'))
    v8 = SemanticVersion

# Generated at 2022-06-13 17:03:09.073951
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    res = SemanticVersion.from_loose_version(LooseVersion('1'))
    assert res == SemanticVersion('1.0.0'), res

    res = SemanticVersion.from_loose_version(LooseVersion('1.2'))
    assert res == SemanticVersion('1.2.0'), res

    res = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    assert res == SemanticVersion('1.2.3'), res

    res = SemanticVersion.from_loose_version(LooseVersion('1.2.3-pre1'))
    assert res == SemanticVersion('1.2.3-pre1'), res

    res = SemanticVersion.from_loose_version(LooseVersion('1.2.3+build2'))

# Generated at 2022-06-13 17:03:20.805625
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:03:28.777665
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # Test data
    import collections
    SemanticVersionTestData = collections.namedtuple('SemanticVersionTestData', ['loose_version', 'expected_semantic_version'])

# Generated at 2022-06-13 17:03:31.579183
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('2.0.0-alpha.12')
    semver = SemanticVersion.from_loose_version(loose_version)
    assert semver == '2.0.0-alpha.12'


# Generated at 2022-06-13 17:03:42.035155
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:03:56.573213
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test that the class can be created from a LooseVersion
    lv = LooseVersion('0.1.2')
    sv = SemanticVersion.from_loose_version(lv)
    assert sv.__class__ is SemanticVersion
    assert sv.major == 0
    assert sv.minor == 1
    assert sv.patch == 2
    assert len(sv.prerelease) == 0

    # Test that the class can be created from a LooseVersion with prerelease
    lv = LooseVersion('0.1.2b3')
    sv = SemanticVersion.from_loose_version(lv)
    assert sv.prerelease == ('b', '3')

    # Test that the class can be created from a LooseVersion with buildmetadata
    lv = LooseVersion('0.1.2-alpha.b3')

# Generated at 2022-06-13 17:04:06.264420
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:04:11.791144
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.six import BytesIO
    stream = StringIO()

# Generated at 2022-06-13 17:04:23.655954
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_version = LooseVersion('test_version')
    result_semantic_version = SemanticVersion.from_loose_version(loose_version)
    expected_semantic_version = SemanticVersion('0.0.0')
    assert result_semantic_version == expected_semantic_version

    loose_version = LooseVersion('test_version.0.0.0')
    result_semantic_version = SemanticVersion.from_loose_version(loose_version)
    expected_semantic_version = SemanticVersion('0.0.0')
    assert result_semantic_version == expected_semantic_version

    loose_version = LooseVersion('test_version.0.0.0.0')

# Generated at 2022-06-13 17:04:28.455206
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Method from_loose_version of class SemanticVersion
    """

    from ansible.module_utils import distro

    # from ansible.module_utils.distro import basic
    # basic.__VERSION__ = '1.12.2'

    # from_loose_version used in library/distro
    sv = SemanticVersion.from_loose_version(LooseVersion(distro.basic.__VERSION__))

    assert sv == '1.12.2'

# Generated at 2022-06-13 17:04:38.136110
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert(repr(SemanticVersion.from_loose_version(LooseVersion('0.50.0')))=='SemanticVersion(\'0.50.0\')')
    assert(SemanticVersion.from_loose_version(LooseVersion('0.50.0')) < '1.0.0')
    assert(SemanticVersion.from_loose_version(LooseVersion('0.50.0')) < 1.0)
    assert(SemanticVersion.from_loose_version(LooseVersion('0.50.0')) >= '0.0.0')
    assert(SemanticVersion.from_loose_version(LooseVersion('0.50.0')) >= 0.50)

# Generated at 2022-06-13 17:04:50.447897
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0a0')) == SemanticVersion('1.0.0-a0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0a0.b0')) == SemanticVersion('1.0.0-a0.b0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0a0.b0+c0')) == SemanticVersion('1.0.0-a0.b0+c0')
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0.a0')) == SemanticVersion('1.0.0+a0')

# Generated at 2022-06-13 17:05:04.089022
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    class TestSemanticVersion(object):
        """Class to test the SemanticVersion class"""
        def __init__(self, tests):
            self.tests = tests
            self.passed = 0
            self.failed = 0

        def run_tests(self):
            """Run tests"""
            for test in self.tests:
                test()
            return self.passed, self.failed, len(self.tests)

        def add_passed_test(self):
            """Add passed test"""
            self.passed += 1

        def add_failed_test(self):
            """Add failed test"""
            self.failed += 1

    class Test(object):
        """Test class"""

# Generated at 2022-06-13 17:05:13.185093
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:05:22.071270
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Unit test for method from_loose_version of class SemanticVersion"""
    import distutils.version
    from ansible.module_utils.common.version import SemanticVersion


# Generated at 2022-06-13 17:05:37.773098
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
  from ansible.module_utils import distro

  (default_os, default_distro) = distro.get_distro()

  remote_os = 'Linux'
  remote_dist = 'Ubuntu'

  if not (LooseVersion(default_distro.version) <= LooseVersion('Ubuntu 19.04')):
    remote_os = 'Darwin'
    remote_dist = 'MacOS X'

  remote_dist_version = remote_dist + ' 16.04'
  remote_dist_version_obj = LooseVersion(remote_dist_version.split()[-1])

  semver_test = SemanticVersion.from_loose_version(remote_dist_version_obj)


# Generated at 2022-06-13 17:05:50.666886
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # tester vars
    main_version = '1.0.0'
    expected_semver = SemanticVersion('1.0.0')

    # test cases

# Generated at 2022-06-13 17:06:01.218372
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.1')).core == (0, 0, 1)
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.1-alpha')).core == (0, 0, 1)
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.1-alpha')).prerelease == ('alpha', )
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.1+201910281758')).core == (0, 0, 1)
    assert SemanticVersion.from_loose_version(LooseVersion('0.0.1+201910281758')).buildmetadata == ('201910281758', )

# Generated at 2022-06-13 17:06:08.062301
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test valid cases
    # https://semver.org/#spec-item-9
    for loose_version in [
        '0.0.0', '1.2.3-4+5', '10.20.30', '3.2.1-rc.1+1', '3.0.0-b1-1',
    ]:
        semantic_version = SemanticVersion.from_loose_version(LooseVersion(loose_version))
        assert semantic_version.vstring == loose_version
        assert semantic_version.major == 3
        assert semantic_version.minor == 0
        assert semantic_version.patch == 0
        assert semantic_version.prerelease == ('b1', '1')
        assert semantic_version.buildmetadata == ('rc', '1', '1')

    # Test invalid cases
    #

# Generated at 2022-06-13 17:06:18.892722
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+42')) == SemanticVersion('1.2.3+42')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-42')) == SemanticVersion('1.2.3-42')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.42')) == SemanticVersion('1.2.3-alpha.42')

# Generated at 2022-06-13 17:06:30.830923
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test #1 - passing a non-LooseVersion should raise ValueError
    loose_version = None
    try:
        SemanticVersion.from_loose_version(loose_version)
        assert False
    except ValueError:
        pass

    # Test #2 - passing a LooseVersion with non-numeric values should raise ValueError
    loose_version = LooseVersion('0.0.0')
    try:
        SemanticVersion.from_loose_version(loose_version)
        assert False
    except ValueError:
        pass

    # Test #3 - passing a LooseVersion with prerelease should set the prerelease
    loose_version = LooseVersion('0.0.0-0.1')
    expected = SemanticVersion('0.0.0-0.1')

# Generated at 2022-06-13 17:06:38.809111
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('2.0.0')) == SemanticVersion('2.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('2.0')) == SemanticVersion('2.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('2')) == SemanticVersion('2.0.0')
    assert SemanticVersion.from_loose_version(LooseVersion('2.1.2-alpha')) == SemanticVersion('2.1.2-alpha')
    assert SemanticVersion.from_loose_version(LooseVersion('2.1.2+exp.sha.5114f85')) == SemanticVersion('2.1.2+exp.sha.5114f85')
    assert Sem

# Generated at 2022-06-13 17:06:45.689392
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.fail_json = None
            self.parse = None
    instance = SemanticVersion()
    vstring = "1.0.0-rc.1+sha.5114f85"
    instance.parse(vstring)
    assert instance.vstring == vstring


# Generated at 2022-06-13 17:06:50.932204
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('0.9.9')) == SemanticVersion('0.9.9')
    assert SemanticVersion.from_loose_version(LooseVersion('0.9.9+abc123')) == SemanticVersion('0.9.9+abc123')
    assert SemanticVersion.from_loose_version(LooseVersion('0.9.9-rc.3')) == SemanticVersion('0.9.9-rc.3')
    assert SemanticVersion.from_loose_version(LooseVersion('0.9.9-rc.3+abc123')) == SemanticVersion('0.9.9-rc.3+abc123')


# Generated at 2022-06-13 17:06:58.049757
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    ver = LooseVersion('1.0.0')
    expected = '1.0.0'
    result = SemanticVersion.from_loose_version(ver).vstring
    assert result == expected, 'from_loose_version(%s) returned %s != %s' % (ver, result, expected)

    ver = LooseVersion('1.0.0+foo')
    expected = '1.0.0+foo'
    result = SemanticVersion.from_loose_version(ver).vstring
    assert result == expected, 'from_loose_version(%s) returned %s != %s' % (ver, result, expected)

    ver = LooseVersion('1.0.0-foo')
    expected = '1.0.0-foo'
    result = SemanticVersion.from_loose_
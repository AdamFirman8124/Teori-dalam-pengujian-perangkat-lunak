

# Generated at 2022-06-13 16:57:35.795937
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    assert SemanticVersion('v0.0.0-1.2.3').core == (0, 0, 0)
    assert SemanticVersion('0.0.0-1.2.3').core == (0, 0, 0)
    assert SemanticVersion('0.0.0').core == (0, 0, 0)
    assert SemanticVersion('v0.0.0+1.2.3').core == (0, 0, 0)
    assert SemanticVersion('0.0.0+1.2.3').core == (0, 0, 0)

    assert SemanticVersion('v0.0.0-1.2.3').prerelease == (1, 2, 3)
    assert SemanticVersion('0.0.0-1.2.3').prerelease == (1, 2, 3)
    assert Semantic

# Generated at 2022-06-13 16:57:39.282883
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha('a') <= _Alpha('b') == True
    assert _Alpha('a') <= _Alpha('a') == True
    assert _Alpha('b') <= _Alpha('a') == False
    assert _Alpha('a') <= _Numeric(1) == True


# Generated at 2022-06-13 16:57:47.970554
# Unit test for method parse of class SemanticVersion

# Generated at 2022-06-13 16:57:53.725151
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    a = _Alpha("a")
    assert a <= "a"
    assert a <= "b"
    assert a <= _Alpha("a")
    assert a <= _Alpha("b")
    assert a <= _Numeric("a")
    assert a <= _Numeric("b")
    assert not a <= "0"


# Generated at 2022-06-13 16:58:06.889604
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    v1 = LooseVersion('0.1')
    v2 = SemanticVersion.from_loose_version(v1)
    assert v2 == '0.1.0'

    v1 = LooseVersion('1.2.0')
    v2 = SemanticVersion.from_loose_version(v1)
    assert v2 == '1.2.0'

    v1 = LooseVersion('1.2+abc')
    v2 = SemanticVersion.from_loose_version(v1)
    assert v2 == '1.2.0+abc'

    v1 = LooseVersion('1.2-alpha')
    v2 = SemanticVersion.from_loose_version(v1)
    assert v2 == '1.2.0-alpha'


# Generated at 2022-06-13 16:58:09.674238
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha('a') <= _Alpha('a')
    assert _Alpha('a') <= _Alpha('b')
    assert not _Alpha('b') <= _Alpha('a')
    assert _Alpha('a') <= 'a'
    assert _Alpha('a') <= 'b'
    assert not _Alpha('b') <= 'a'
    assert _Alpha('a') <= 1
    assert _Alpha('a') <= 2
    assert not _Alpha('b') <= 1
    assert not _Alpha('b') <= 2


# Generated at 2022-06-13 16:58:23.395942
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion
    import pytest

    # Test that a LooseVersion can be passed and a proper SemanticVersion object returned
    loose_version = LooseVersion('1.2.3-prerelease.123+buildmetadata')
    semver = SemanticVersion.from_loose_version(loose_version)

    assert semver.vstring == '1.2.3-prerelease.123+buildmetadata'
    assert semver == '1.2.3-prerelease.123+buildmetadata'

    # Test that passing a string with a format similar to a LooseVersion
    # works as if it were a LooseVersion
    semver = SemanticVersion.from_loose_version('1.2.3-prerelease.123+buildmetadata')

    assert semver.vstring

# Generated at 2022-06-13 16:58:34.905946
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 16:58:38.765605
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
   alpha = _Alpha('a')
   assert alpha <= 'a'
   assert alpha <= 'b'
   assert alpha <= '5'
   assert not alpha <= '0'
   assert not alpha <= -1
   assert not alpha <= 1


# Generated at 2022-06-13 16:58:50.110463
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    expected_output = SemanticVersion('1.2.3+1')
    actual_output = SemanticVersion.from_loose_version(LooseVersion('1.2.3.1'))
    assert actual_output == expected_output, "method from_loose_version did not produce expected output"

    expected_output = SemanticVersion('1.2.3-alpha')
    actual_output = SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha'))
    assert actual_output == expected_output, "method from_loose_version did not produce expected output"

    expected_output = SemanticVersion('1.2.3-alpha+1')
    actual_output = SemanticVersion.from_loose_version(LooseVersion('1.2.3-alpha.1'))
   

# Generated at 2022-06-13 16:59:07.624888
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    """Test SemanticVersion.from_loose_version()"""

    # Test version strings
    test_versions = [
        '0.5.5',
        '0.5.5.0.0.3.1',
        '0.5.5-dev',
        '0.5.5-000.dev+000',
        '0.5.5-000',
        '0.5.5-001',
        '0.5.5-099.099.099',
        '0.5.5+099.099.099',
        '0.5.5+dev',
        '0.5.5+000.dev+000'
    ]

    for version in test_versions:
        loose_version = LooseVersion(version)

# Generated at 2022-06-13 16:59:14.100528
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha('1') <= _Alpha('2')
    assert _Alpha('1') <= _Alpha('2')
    assert _Alpha('1') <= _Alpha('1')
    assert _Alpha('1') <= '1'
    assert _Alpha('1') <= '2'
    assert _Alpha('1') <= '1'
    assert '1' <= _Alpha('1')
    assert '2' <= _Alpha('1')
    assert '1' <= _Alpha('1')
    try:
        assert 1 <= _Alpha('1')
    except ValueError:
        pass
    else:
        raise AssertionError('Allowed numeric <= alpha')



# Generated at 2022-06-13 16:59:25.796605
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')).vstring == '1.0.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0')).vstring == '1.0.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1')).vstring == '1.0.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-beta1')).vstring == '1.0.0-beta1'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0+build10')).vstring == '1.0.0+build10'


# Generated at 2022-06-13 16:59:38.342934
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import unittest
    from ansible.module_utils.common.version import SemanticVersion
    from ansible.module_utils.common.version import LooseVersion

    class TestSemanticVersionFromLooseVersion(unittest.TestCase):

        version_pairs = ('1.5.0', '1.5.0'), ('1.5.0.post1', '1.5.0-0')

        def test_from_loose_version(self):
            for loose_version_vstring, semver_vstring in TestSemanticVersionFromLooseVersion.version_pairs:
                loose_version = LooseVersion(loose_version_vstring)
                semver = SemanticVersion.from_loose_version(loose_version)

# Generated at 2022-06-13 16:59:52.006169
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Tests the case intended for the method, that of creating a
    # SemanticVersion from a LooseVersion
    loose = LooseVersion("0.0.0a0.dev2")
    semver = SemanticVersion.from_loose_version(loose)
    assert semver.core == (0, 0, 0)
    assert semver.prerelease == (_Alpha('a'), _Numeric('0'), _Alpha('dev'), _Numeric('2'))
    assert semver.buildmetadata == ()
    assert semver.vstring == semver.__str__()

    loose = LooseVersion("0.0.11a0.dev2")
    semver = SemanticVersion.from_loose_version(loose)
    assert semver.core == (0, 0, 11)

# Generated at 2022-06-13 17:00:00.934092
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    semantic_version = SemanticVersion()
    semantic_version.parse("1.1.1+1")
    assert semantic_version == SemanticVersion.from_loose_version(LooseVersion("1.1.1+1"))
    assert semantic_version != SemanticVersion.from_loose_version(LooseVersion("1.1.1+2"))
    assert semantic_version != SemanticVersion.from_loose_version(LooseVersion("2.1.1+1"))
    assert semantic_version != SemanticVersion.from_loose_version(LooseVersion("1.2.1+1"))
    assert semantic_version != SemanticVersion.from_loose_version(LooseVersion("1.1.2+1"))

# Generated at 2022-06-13 17:00:02.572560
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha('a') >= _Alpha('a')
    assert _Alpha('a') <= _Alpha('b')
    assert _Alpha('b') >= _Alpha('a')


# Generated at 2022-06-13 17:00:14.813041
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    loose_versions = (
        '1.2.3+abc.123',
        '1.2.3+abc.123-rc.1',
        '1.2.3-rc.1+abc.123',
        '1.2.3-rc.1.2+abc.123',
        '1.2.3-alpha.1+abc.123',
        '1.2.3-beta.1+abc.123',
        '1.2.3-0.alpha.1+abc.123',
        '1.2.3-0.beta.1+abc.123',
    )

    for loose_version in loose_versions:
        lv = LooseVersion(loose_version)
        sv_from_lv = SemanticVersion.from_loose_version(lv)

# Generated at 2022-06-13 17:00:21.933428
# Unit test for method __le__ of class _Alpha
def test__Alpha___le__():
    assert _Alpha('b') <= 'b'
    assert not _Alpha('b') <= 'a'
    assert _Alpha('a') <= 'b'
    assert not _Alpha('a') <= 'a'
    assert _Alpha('a') <= _Alpha('b')
    assert not _Alpha('b') <= _Alpha('a')
    assert _Alpha('b') <= _Numeric(1)
    assert not _Alpha('b') <= _Alpha('b')
    assert not _Alpha('b') <= _Numeric(1)



# Generated at 2022-06-13 17:00:30.053594
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test that the method raises ``ValueError`` when passed something other than
    # ``LooseVersion``
    try:
        SemanticVersion.from_loose_version('anything')
    except ValueError as e:
        assert str(e) == "'anything' is not a LooseVersion"
    else:
        assert False

    # Test that the method raises ``ValueError`` when passed a ``LooseVersion`` that has any
    # non-integer values in its version
    try:
        SemanticVersion.from_loose_version(LooseVersion('1.2.x'))
    except ValueError as e:
        assert str(e) == "Non integer values in LooseVersion ('1', '2', 'x')"
    else:
        assert False

    # Test that the method returns a ``SemanticVersion`` when passed a ``Lo

# Generated at 2022-06-13 17:00:47.970650
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion
    test_version = SemanticVersion.from_loose_version(LooseVersion('2.4.1'))
    assert test_version.vstring == '2.4.1'
    test_version = SemanticVersion.from_loose_version(LooseVersion('2.4.1-alpha.2'))
    assert test_version.vstring == '2.4.1-alpha.2'
    test_version_1 = SemanticVersion.from_loose_version(LooseVersion('2.4.3-alpha.2'))
    test_version_2 = SemanticVersion.from_loose_version(LooseVersion('2.4.3-alpha'))
    assert (test_version_1 > test_version_2)
   

# Generated at 2022-06-13 17:00:58.284544
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    version = SemanticVersion.from_loose_version(LooseVersion('1.2.3'))
    assert version.vstring == '1.2.3'

    version = SemanticVersion.from_loose_version(LooseVersion('1.2.3.4'))
    assert version.vstring == '1.2.3'

    version = SemanticVersion.from_loose_version(LooseVersion('1.2.3-4.5'))
    assert version.vstring == '1.2.3-4.5'

    version = SemanticVersion.from_loose_version(LooseVersion('1.2.3-4.5.6'))
    assert version.vstring == '1.2.3-4.5.6'

    version = SemanticVersion.from_loose_version

# Generated at 2022-06-13 17:01:07.170675
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    def f(loose_version):
        v = SemanticVersion.from_loose_version(loose_version)
        return v.vstring


# Generated at 2022-06-13 17:01:19.428561
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion
    # Make sure it converts 1.23 to 1.23.0
    assert SemanticVersion.from_loose_version(LooseVersion('1.23')) == SemanticVersion('1.23.0')
    # Make sure it converts 1.23.4 to 1.23.4
    assert SemanticVersion.from_loose_version(LooseVersion('1.23.4')) == SemanticVersion('1.23.4')
    # Make sure it converts 1.23.4b1 to 1.23.4-b1
    assert SemanticVersion.from_loose_version(LooseVersion('1.23.4b1')) == SemanticVersion('1.23.4-b1')
    # Make sure it converts 1.23.4.post

# Generated at 2022-06-13 17:01:30.888408
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    test_data = [
        (
            '1.1-alpha.1',
            '1.1.0-alpha.1'
        ),
        (
            '1.1.1-alpha.1-test',
            '1.1.1-alpha.1-test'
        ),
        (
            LooseVersion('1.1-alpha.1'),
            '1.1.0-alpha.1'
        ),
        (
            LooseVersion('1.1.1-alpha.1-test'),
            '1.1.1-alpha.1-test'
        ),
    ]
    for (input, expected) in test_data:
        actual = str(SemanticVersion.from_loose_version(input))

# Generated at 2022-06-13 17:01:41.834955
# Unit test for method parse of class SemanticVersion

# Generated at 2022-06-13 17:01:51.506741
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Check if the passed argument is a LooseVersion
    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version("1.1.1")
    # Check if the passed LooseVersion contains non-integer values
    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(LooseVersion("1.1.x"))
    # Check if the passed LooseVersion contains multiple dots
    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(LooseVersion("1.1.1.1"))
    # Check if the passed LooseVersion contains a separator
    with pytest.raises(ValueError):
        SemanticVersion.from_loose_version(LooseVersion("1.x.x-x"))
    # Check if

# Generated at 2022-06-13 17:01:55.868649
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # https://semver.org/#spec-item-4
    # https://semver.org/#spec-item-9
    # https://semver.org/#spec-item-10
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-rc.1+build.11111')) == SemanticVersion('1.2.3-rc.1')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3+build.11111')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3-rc.1')) == SemanticVersion('1.2.3-rc.1')

# Generated at 2022-06-13 17:02:07.146580
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six import PY2
    if PY2:
        # Here in python 2, we use the same method
        # There are very deep parts of the code that already
        # depends on this working this way
        from ansible.module_utils.compat.version import LooseVersion
        from ansible.module_utils.compat.version import Version
    else:
        from ansible.module_utils.six.moves import builtins
        from ansible.module_utils.compat.version import LooseVersion
        from ansible.module_utils.compat.version import Version

        # here in python 3, we use the provided method
        # that comes with python 3
        builtins.LooseVersion = LooseVersion
        builtins.Version = Version

    # INPUT

# Generated at 2022-06-13 17:02:14.409429
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    # Test with a LooseVersion instance
    try:
        loose_version = LooseVersion('1.0.0')
    except ValueError as e:
        loose_version = None
    from_loose_version = SemanticVersion.from_loose_version(loose_version)
    assert from_loose_version == '1.0.0'

    # Test with a non LooseVersion instance
    try:
        SemanticVersion.from_loose_version('1.0.0')
    except ValueError as e:
        assert True
    else:
        assert False

# Generated at 2022-06-13 17:02:28.492919
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    test_case = {
        '1.2.3': '1.2.3',
        '1.2.3.dev1': '1.2.3',
        '1.2.3+abc': '1.2.3'
    }

    for input_version, expected_version in test_case.items():
        loose_version = LooseVersion(input_version)
        semantic_version = SemanticVersion.from_loose_version(loose_version)
        assert isinstance(semantic_version, SemanticVersion)
        assert semantic_version == expected_version

# Generated at 2022-06-13 17:02:35.434037
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('2013.02.19')).vstring == '2013.2.19'

    assert SemanticVersion.from_loose_version(LooseVersion('2013.02.19-a3.57')).vstring == '2013.2.19-a3.57'

    assert SemanticVersion.from_loose_version(LooseVersion('2013.02.19+git')).vstring == '2013.2.19+git'

    assert SemanticVersion.from_loose_version(LooseVersion('2013.02.19-a3.57+git')).vstring == '2013.2.19-a3.57+git'


# Generated at 2022-06-13 17:02:46.282985
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion("4.3.0")) == \
        SemanticVersion("4.3.0")
    assert SemanticVersion.from_loose_version(LooseVersion("1.0")) == \
        SemanticVersion("1.0.0")
    assert SemanticVersion.from_loose_version(LooseVersion("1.0-alpha")) == \
        SemanticVersion("1.0.0-alpha")
    assert SemanticVersion.from_loose_version(LooseVersion("1.0+20190623")) == \
        SemanticVersion("1.0.0+20190623")

# Generated at 2022-06-13 17:02:58.218497
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.common.version import SemanticVersion
    from ansible.module_utils.compat.version import LooseVersion


# Generated at 2022-06-13 17:03:09.072905
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import pytest

    # Test should pass
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0')).vstring == '1.0.0'
    assert SemanticVersion.from_loose_version(LooseVersion('1.0.0-alpha')).vstring == '1.0.0-alpha'

# Generated at 2022-06-13 17:03:16.744487
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # init tests
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('1.2.3.4.5')) == SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(LooseVersion('2.3.4.5.6-alpha')) == SemanticVersion('2.3.4-alpha')
    assert SemanticVersion.from_loose_version(LooseVersion('2.3.4.5.6-beta10')) == SemanticVersion('2.3.4-beta10')

# Generated at 2022-06-13 17:03:25.621916
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # non LooseVersion
    try:
        SemanticVersion.from_loose_version('1.2.3')
    except ValueError as e:
        assert str(e) == "'1.2.3' is not a LooseVersion"
    else:
        raise AssertionError("Expected ValueError")

    # LooseVersion string contains non integer (e.g. the letter 'a')
    try:
        SemanticVersion.from_loose_version(LooseVersion('1.2a.3'))
    except ValueError as e:
        assert str(e) == "Non integer values in LooseVersion ('1', '2a', '3')"
    else:
        raise AssertionError("Expected ValueError")

    # LooseVersion starts with a non integer

# Generated at 2022-06-13 17:03:30.040748
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    result = SemanticVersion.from_loose_version(LooseVersion('1.0.0'))
    assert isinstance(result, SemanticVersion)
    assert result.vstring == '1.0.0'
    assert result.prerelease == ()
    assert result.buildmetadata == ()

# Generated at 2022-06-13 17:03:38.901764
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six.moves.urllib.parse import urlparse

    from packaging.version import parse as parse_packaging_version

    for sample in (
        '1.2.3-alpha+app.server',
        '3.7.3+1.0',
        '5.3.6-160',
        '20190306',
        '2.1.0a2+dirty.patch.metadata',
        '0.0.0-post+dev.abcd.abcdeabcde',
        '2.1.0+dirty.patch.metadata',
    ):
        loose_version = SemanticVersion.from_loose_version(parse_packaging_version(sample))
        semver = SemanticVersion(sample)


# Generated at 2022-06-13 17:03:46.481525
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.compat.version import LooseVersion

# Generated at 2022-06-13 17:04:03.351588
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():

    assert SemanticVersion.from_loose_version('1.20.5').vstring == '1.20.5'
    assert SemanticVersion.from_loose_version('1.20.5a7').vstring == '1.20.5-a7'
    assert SemanticVersion.from_loose_version('1.20.5-a7').vstring == '1.20.5-a7'

    assert SemanticVersion.from_loose_version('1.20.5+build324').vstring == '1.20.5+build324'
    assert SemanticVersion.from_loose_version('1.20.5-a7+build324').vstring == '1.20.5-a7+build324'


# Generated at 2022-06-13 17:04:09.841353
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    import os, sys, pytest
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.join(dir_path, "../"))
    sys.path.append(os.path.join(dir_path, "../../../"))
    sys.path.append(os.path.join(dir_path, "../../../../ansible_collections/ansible/netcommon/tests/"))
    from unit.compat import unittest
    import unit.modules.utils as utils
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.six import PY2, PY3
    from ansible.module_utils.common._text import to_native

# Generated at 2022-06-13 17:04:20.958069
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six import PY2
    if not PY2:
        from ansible.module_utils.common.version import LooseVersion
    # LooseVersion class requires exact 2 elements in tuple

# Generated at 2022-06-13 17:04:33.232332
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    version = ('0.0.1-alpha.1+20130313144700', '1.7.z.92+exp.sha.5114f85',
               '0.0.1-alpha', '0.0.1-1', '0.0.1', '0.0.1+exp.sha.5114f85', '1.0.0-rc.1+build.1', '1.0.0+build')
    instances = list()
    for v in version:
        instances.append(SemanticVersion(v))
    assert instances[0].major == 0
    assert instances[0].minor == 0
    assert instances[0].patch == 1
    assert instances[0].prerelease == (text_type('alpha'), text_type('1'))

# Generated at 2022-06-13 17:04:45.985091
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    version_loose = LooseVersion("1.2")
    version_semantic = SemanticVersion.from_loose_version(version_loose)
    assert isinstance(version_semantic, SemanticVersion)
    assert version_semantic.major == 1
    assert version_semantic.minor == 2
    assert version_semantic.patch == 0
    assert version_semantic.prerelease is None
    assert version_semantic.buildmetadata is None
    assert version_semantic.vstring == '1.2'

    version_loose = LooseVersion("1.2.3")
    version_semantic = SemanticVersion.from_loose_version(version_loose)
    assert isinstance(version_semantic, SemanticVersion)
    assert version_semantic.major == 1
    assert version_semantic

# Generated at 2022-06-13 17:04:51.089284
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:05:04.252847
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Testing different version strings input and expected output after conversion.
    # Current test cases assumes output should be in the form (major, minor, patch, pre-release)
    # If we need to add more test cases, we need to add them in a list in this format.
    # (testcase_full_version, testcase_version_tuple)
    testcase_list = [("1.2.3", ("1", "2", "3", ())),
                     ("1.2.3-prerelease.1", ("1", "2", "3", ("prerelease", "1"))),
                     ("1.2.3+buildmetadata", ("1", "2", "3", ()))]


# Generated at 2022-06-13 17:05:06.811794
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('1.1.1')) == SemanticVersion('1.1.1')



# Generated at 2022-06-13 17:05:15.069098
# Unit test for method from_loose_version of class SemanticVersion

# Generated at 2022-06-13 17:05:17.981415
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    version_string = "9.9.9"
    loose_version = LooseVersion(version_string)
    semantic_version = SemanticVersion.from_loose_version(loose_version)
    assert semantic_version.vstring == version_string


# Generated at 2022-06-13 17:05:33.686869
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # Test different LooseVersion version strings

    # Test version without build metadata
    loosev = LooseVersion('1.2.3')
    semv = SemanticVersion('1.2.3')
    assert SemanticVersion.from_loose_version(loosev) == semv

    # Test version with build metadata
    loosev = LooseVersion('1.2.3+20130313144700')
    semv = SemanticVersion('1.2.3+20130313144700')
    assert SemanticVersion.from_loose_version(loosev) == semv

    # Test version with prerelease
    loosev = LooseVersion('1.2.3-beta')
    semv = SemanticVersion('1.2.3-beta')

# Generated at 2022-06-13 17:05:46.409433
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.six.moves import cStringIO as StringIO
    from ansible.module_utils.six.moves import unittest
    from ansible.module_utils.six.moves.urllib.error import URLError

    from ansible.module_utils.six.moves.urllib.request import urlopen

    import mock

    import sys

    class FakeLooseVersion(LooseVersion):
        def __init__(self, vstring, version):
            self.vstring = vstring
            self.version = version

    class TestSemanticVersionFromLooseVersion(unittest.TestCase):
        """A TestCase for SemanticVersion.from_loose_version."""


# Generated at 2022-06-13 17:05:58.333210
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    version = SemanticVersion()
    version.parse("v0.0.1")
    assert version.major == 0
    assert version.minor == 0
    assert version.patch == 1
    assert len(version.prerelease) == 0
    assert len(version.buildmetadata) == 0

    version.parse("v1.2.3")
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert len(version.prerelease) == 0
    assert len(version.buildmetadata) == 0

    version.parse("v1.2.3-beta.1")
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert len(version.prerelease) == 2
    assert version.prerelease[0] == "beta"

# Generated at 2022-06-13 17:06:06.289821
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    class TestCase:
        def __init__(self, test_input, expected_output):
            self.test_input = test_input
            self.expected_output = expected_output


# Generated at 2022-06-13 17:06:18.249547
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # LooseVersion not provided
    ret = SemanticVersion.from_loose_version('1.2.3') # Return the SemanticVersion of LooseVersion
    assert isinstance(ret, SemanticVersion)
    assert ret.major == 1
    assert ret.minor == 2
    assert ret.patch == 3

    ret = SemanticVersion.from_loose_version('1.2.3.4')
    assert ret.major == 1
    assert ret.minor == 2
    assert ret.patch == 3

    ret = SemanticVersion.from_loose_version('1.2.3-4.5')
    assert ret.major == 1
    assert ret.minor == 2
    assert ret.patch == 3


# Generated at 2022-06-13 17:06:26.527459
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    sv1 = SemanticVersion.from_loose_version(LooseVersion("1.2.3"))
    assert sv1.major == 1
    assert sv1.minor == 2
    assert sv1.patch == 3
    assert sv1.prerelease == ()
    assert sv1.buildmetadata == ()

    sv2 = SemanticVersion.from_loose_version(LooseVersion("1.2.3-alpha.1"))
    assert sv2.major == 1
    assert sv2.minor == 2
    assert sv2.patch == 3
    assert sv2.prerelease == (Alpha("alpha"), Numeric("1"))
    assert sv2.buildmetadata == ()

    sv3 = SemanticVersion.from_loose_version(LooseVersion("1.2.3+run.1225.40"))

# Generated at 2022-06-13 17:06:28.915182
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    assert SemanticVersion.from_loose_version(LooseVersion('0.1.2')) == SemanticVersion('0.1.2')

# Generated at 2022-06-13 17:06:37.856076
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 17:06:45.091238
# Unit test for method parse of class SemanticVersion
def test_SemanticVersion_parse():
    version = SemanticVersion('1.2.3-alpha.1+b.2.4')
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.prerelease == (_Numeric('alpha'), _Numeric('1'))
    assert version.buildmetadata == (_Alpha('b'), _Numeric('2'), _Numeric('4'))


# Generated at 2022-06-13 17:06:54.417039
# Unit test for method from_loose_version of class SemanticVersion
def test_SemanticVersion_from_loose_version():
    # test input without prerelease
    input_loose_version = LooseVersion('1.2.3')
    expected_version = SemanticVersion('1.2.3')
    retrieved_version = SemanticVersion.from_loose_version(
        input_loose_version)
    assert(expected_version == retrieved_version)
    # test input with prerelease
    input_loose_version = LooseVersion('1.2.3-alpha.1')
    expected_version = SemanticVersion('1.2.3-alpha.1')
    retrieved_version = SemanticVersion.from_loose_version(
        input_loose_version)
    assert(expected_version == retrieved_version)
    # test input with build metadata
    input_loose_version = LooseVersion('1.2.3+12345')
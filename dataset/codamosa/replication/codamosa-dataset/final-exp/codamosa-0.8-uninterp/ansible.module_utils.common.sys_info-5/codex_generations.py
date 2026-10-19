

# Generated at 2022-06-12 23:38:24.918992
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    # Basic codename tests
    from unittest.mock import patch

    with patch('ansible.module_utils.distro.os_release_info', return_value={'version_codename': 'buster'}):
        assert get_distribution_codename() == 'buster'

    # Test several releases of Ubuntu
    with patch('ansible.module_utils.distro.os_release_info', return_value={'version_codename': ''}):
        with patch('ansible.module_utils.distro.lsb_release_info', return_value={'codename': 'xenial'}):
            assert get_distribution_codename() == 'xenial'


# Generated at 2022-06-12 23:38:25.900841
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == u'Centos'



# Generated at 2022-06-12 23:38:31.240945
# Unit test for function get_distribution_codename

# Generated at 2022-06-12 23:38:42.274950
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test get_distribution_codename() function
    '''
    # Test Ubuntu Xenial
    os_release_info = {
        'id': 'ubuntu',
        'version_id': '16.04',
        'version_codename': 'xenial',
        'pretty_name': 'Ubuntu 16.04.2 LTS',
    }
    lsb_release_info = {
        'codename': 'xenial',
        'description': 'Ubuntu 16.04.2 LTS',
        'id': 'Ubuntu',
        'release': '16.04',
    }
    # Ubuntu Xenial
    with distro.mock_distro(os_release_info=os_release_info, lsb_release_info=lsb_release_info):
        assert get_distribution

# Generated at 2022-06-12 23:38:44.809893
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test the get_distribution_codename function
    '''
    assert get_distribution_codename() is None

# Generated at 2022-06-12 23:38:53.714934
# Unit test for function get_distribution_version
def test_get_distribution_version():
    import unittest
    import unittest.mock as mock

    class Test_get_distribution_version(unittest.TestCase):

        @mock.patch("ansible.module_utils.common.distro.id", return_value='centos')
        @mock.patch("ansible.module_utils.common.distro.version", return_value='7')
        @mock.patch("ansible.module_utils.common.platform.system", return_value='Linux')
        def test_get_distribution_version_centos(self, id_mock, version_mock, platform_mock):
            version = get_distribution_version()
            self.assertEqual(version, "7.0")


# Generated at 2022-06-12 23:38:54.318214
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() is None

# Generated at 2022-06-12 23:39:02.268634
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.facts.system.distribution import Distribution

    class A:
        platform = 'Linux'

    class B(A):
        distribution = 'RedHat'

    class C(B):
        distribution = 'Centos'

    class D(B):
        distribution = 'Debian'

    class E(A):
        distribution = 'Mock'
        platform = 'FreeBSD'

    assert get_platform_subclass(A) is A
    assert get_platform_subclass(B) is B
    assert get_platform_subclass(C) is C
    assert get_platform_subclass(D) is D
    assert get_platform_subclass(E) is E

    class MockDistribution(Distribution):
        platform = 'Linux'
        distribution = 'Mock'


# Generated at 2022-06-12 23:39:06.305122
# Unit test for function get_distribution
def test_get_distribution():
    from ansible.module_utils.common._utils import get_distribution as _get_distribution
    from ansible.module_utils.common._utils import get_distribution_version as _get_distribution_version
    assert _get_distribution() == 'OtherLinux'
    assert _get_distribution_version() is None

# Generated at 2022-06-12 23:39:13.419092
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        platform = 'Linux'
        distribution = None

    class A1(A):
        distribution = 'RedHat'

    class A2(A):
        distribution = 'Fedora'

    class B(A):
        platform = 'OpenBSD'
        distribution = None

    assert get_platform_subclass(A) == A
    assert get_platform_subclass(A1) == A1
    assert get_platform_subclass(A2) == A2
    assert get_platform_subclass(B) == B

    has_distro = distro.id()
    if not has_distro:
        # No ID or version will be detected by distro on unsupported platforms
        assert get_platform_subclass(A) == A
        assert get_platform_subclass(B) == B
        return

# Generated at 2022-06-12 23:39:34.325631
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.basic import AnsibleModule

    class Base:
        platform = "Linux"

    class Distribution(Base):
        distribution = "Debian"

    class OtherDistribution(Base):
        distribution = "OtherLinux"

    class NonLinux(Base):
        platform = "Solaris"

    class NotADistribution(Base):
        platform = None

    class Linux(Base):
        platform = "Linux"

    class NotADistributionBis(Distribution):
        platform = None

    def assert_none(mod):
        assert(mod is None), 'Should get no module'

    def assert_base(mod):
        assert_none(mod.params.get('base', None))
        assert_none(mod.params.get('distribution', None))

# Generated at 2022-06-12 23:39:35.086507
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    distro_codename = get_distribution_codename()
    assert distro_codename is not None

# Generated at 2022-06-12 23:39:43.371515
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test the function get_platform_subclass()
    '''
    import ansible.module_utils.basic
    # Build a class hierarchy where Linux is a subclass of UNIX
    class UNIX(object):
        platform = 'Linux'
        distribution = None

    class Linux(UNIX):
        distribution = 'Linux'

    class Debian(Linux):
        distribution = 'Debian'

    class Ubuntu(Linux):
        distribution = 'Ubuntu'

    class CentOS(Linux):
        distribution = 'CentOS'

    class Suse(Linux):
        distribution = 'Suse'

    class FreeBSD(UNIX):
        platform = 'FreeBSD'

    # Make sure a plain Linux subclass is always returned
    subclass = ansible.module_utils.basic.get_platform_subclass(Linux)
    assert subclass is Linux

   

# Generated at 2022-06-12 23:39:54.442949
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform
    import copy

    # This will be tested on a Linux platform
    class LinuxOnly:
        platform = 'Linux'
        distribution = 'TestDist'

    class LinuxTestDist(LinuxOnly):
        distribution = 'TestDist'

    class LinuxTestDist2(LinuxOnly):
        distribution = 'TestDist2'

    class LinuxNoDist(LinuxOnly):
        distribution = None

    assert get_platform_subclass(LinuxOnly) == LinuxOnly
    assert get_platform_subclass(LinuxTestDist) == LinuxTestDist
    assert get_platform_subclass(LinuxTestDist2) == LinuxTestDist2
    assert get_platform_subclass(LinuxNoDist) == LinuxNoDist

    # Test cases for inheritance
    class LinuxDistX(LinuxTestDist):
        pass


# Generated at 2022-06-12 23:39:56.894438
# Unit test for function get_distribution
def test_get_distribution():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    distribution = module.get_distribution()

    assert distribution

# Generated at 2022-06-12 23:40:00.635764
# Unit test for function get_distribution
def test_get_distribution():
    """
    Test to make sure get_distribution() returns the correct values.
    """

    # Testing with linux
    assert get_distribution() == 'Redhat'

    # Testing with Windows
    assert get_distribution() == 'Windows'


# Generated at 2022-06-12 23:40:07.981471
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import types

    class BaseClass(object):
        platform = 'BasePlatform'
        distribution = None

    class PlatformClass(BaseClass):
        distribution = None
        platform = 'testplatform'

    class DistributionClass(BaseClass):
        platform = 'BasePlatform'
        distribution = 'testdistribution'

    class PlatformDistributionClass(BaseClass):
        platform = 'testplatform'
        distribution = 'testdistribution'

    subclass = get_platform_subclass(BaseClass)
    assert isinstance(subclass, types.ClassType)

    # On a non-Linux (or Amazon Linux) system, the BaseClass would be returned
    subclass = get_platform_subclass(PlatformClass)
    assert isinstance(subclass, types.ClassType)
    assert subclass == PlatformClass

    # On a Linux (or Amazon Linux) system, the Distribution

# Generated at 2022-06-12 23:40:19.621724
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    old_lsb_release_info = distro.lsb_release_info()
    old_os_release_info = distro.os_release_info()


# Generated at 2022-06-12 23:40:22.032878
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # test 1: on debian 9
    # the function get_distribution_codename should return "stretch"
    assert get_distribution_codename() == "stretch"

# Generated at 2022-06-12 23:40:26.794408
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Unit tests for function get_distribution_version
    '''
    expected = None
    # Test 1: Non-Linux platforms
    distribution = get_distribution()
    distribution_version = get_distribution_version()
    assert distribution_version == expected
    # Test 2: Linux but no version file
    distribution = 'Linux'
    distribution_version = get_distribution_version()
    assert distribution_version == expected

# Generated at 2022-06-12 23:41:02.352787
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit test for function get_platform_subclass
    '''

    # Define parent class of test class
    class ParentClass(object):
        '''
        Parent class for unit test
        '''

        distribution = None
        platform = None

    # Define test class with platform and distribution specific subclass
    class TestClass(ParentClass):
        '''
        Test class for unit test
        '''

        distribution = None
        platform = None

        class Linux(TestClass):
            '''
            Linux-specific subclass for unit test
            '''

            distribution = None
            platform = 'Linux'

            class Fedora(Linux):
                '''
                Fedora-specific subclass for unit test
                '''

                distribution = 'Fedora'
                platform = 'Linux'

    # Assert that the correct subclass is returned

# Generated at 2022-06-12 23:41:03.629778
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Redhat'


# Generated at 2022-06-12 23:41:12.459887
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Verify that get_platform_subclass works correctly
    '''
    from ansible.module_utils.distro import RedHatUser

    (subclass, subclass_name) = (None, None)
    # If the class has a platform attribute, a subclass is returned
    subclass = get_platform_subclass(RedHatUser)
    assert subclass.__name__ == u'RedHatUser'

    # If the class has no platform attribute, the original class is returned
    class NoPlatform:
        pass
    subclass = get_platform_subclass(NoPlatform)
    assert subclass == NoPlatform

    # If the class has no subclasses, the original class is returned
    subclass = get_platform_subclass(RedHatUser)
    assert subclass == RedHatUser

    # If the class has subclasses but no platform, the subclass is returned


# Generated at 2022-06-12 23:41:19.660878
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Simple test of the ``get_platform_subclass`` method.  It's not really a
    unit test as it assumes that the host where the test is running is Linux
    and that the distribution is RedHat or Amazon.

    In the future, this can be expanded to run on multiple platforms, possibly
    using something like tox or getting TravisCI to run on multiple platforms.
    '''
    # Create a class hierarchy to test with
    class Base(object):
        '''
        The base class.
        '''
        platform = 'Generic'

    class LinuxBase(Base):
        '''
        Base class for Linux platforms.
        '''
        platform = 'Linux'

    class LinuxRH(LinuxBase):
        '''
        RedHat Linux class.
        '''
        distribution = 'Redhat'


# Generated at 2022-06-12 23:41:27.802246
# Unit test for function get_distribution_version
def test_get_distribution_version():
    expected_results = {
        'ubuntu': '16.04',
        'debian': '9.5',
        'centos': '7',
        'fedora': '27',
        'osx': None,
        'suse': '11.4',
        'amzn': '2017.03',
        'alpine': '3.7',
        'freebsd': '11.1',
    }

    for distro_name, expected_version in expected_results.items():
        assert get_distribution_version(distro_name) == expected_version

# Generated at 2022-06-12 23:41:39.577081
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # import pytest
    class Base:
        platform = platform.system()

    class Linux(Base):
        platform = 'Linux'
        distribution = None

    class LinuxUbuntu(Linux):
        distribution = 'Ubuntu'

    class LinuxRedhat(Linux):
        distribution = 'Redhat'

    class Openbsd(Base):
        platform = 'OpenBSD'
        distribution = None

    class Other(Base):
        platform = 'Other'
        distribution = None

    class OtherLinux(Linux):
        distribution = 'OtherLinux'

    class OtherLinuxRedhat(LinuxRedhat):
        distribution = 'OtherLinux'

    class LinuxRedhat6(LinuxRedhat):
        distribution_version = '6'

    class LinuxRedhat7(LinuxRedhat):
        distribution_version = '7'

    # The code we're testing


# Generated at 2022-06-12 23:41:49.639712
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Unit test for function get_distribution
    '''
    class DistributionMock(object):
        def __init__(self, id_return, version_return, codename_return=None):
            self.id_return = id_return
            self.version_return = version_return
            self.codename_return = codename_return

        def id(self):
            return self.id_return

        def version(self, **kwargs):
            return self.version_return

        def codename(self, **kwargs):
            return self.codename_return

    ubuntu_bionic = DistributionMock('Ubuntu', '18.04', 'bionic')
    debian_10 = DistributionMock('debian', '10')

# Generated at 2022-06-12 23:42:00.364237
# Unit test for function get_distribution
def test_get_distribution():
    def _fake_distro(distro_id):
        return lambda: distro_id

    real_distro = distro.id
    distro.id = _fake_distro

    for distro_id, expected_distribution in [
        ('', 'OtherLinux'),
        ('amzn', 'Amazon'),
        ('centos', 'Centos'),
        ('fedora', 'Fedora'),
        ('debian', 'Debian'),
        ('ubuntu', 'Ubuntu'),
        ('rhel', 'Redhat'),
        ('otherlinux', 'OtherLinux'),
    ]:
        distro.id = lambda: distro_id
        actual_distribution = get_distribution()

# Generated at 2022-06-12 23:42:10.628135
# Unit test for function get_distribution_version
def test_get_distribution_version():

    import unittest

    class TestGetDistributionVersion(unittest.TestCase):

        def test_ubuntu_bionic(self):
            '''
            Test to ensure that get_distribution_version() returns 'bionic' when run under Ubuntu 18.04
            '''
            self.assertEqual(distro.id(), 'ubuntu')
            self.assertEqual(distro.version(), '18.04')
            self.assertEqual(get_distribution_version(), '18.04')

        def test_debian_bullseye(self):
            '''
            Test to ensure that get_distribution_version() returns 'bullseye' when run under Debian 11
            '''
            self.assertEqual(distro.id(), 'debian')
            self.assertEqual(distro.version(), '11')
           

# Generated at 2022-06-12 23:42:12.207492
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'jessie'



# Generated at 2022-06-12 23:42:48.387805
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import ansible.module_utils.basic

    class Base:
        pass

    class A(Base):
        platform = 'A'
        distribution = None

    class B(A):
        platform = 'B'
        distribution = None

    class C(B):
        platform = 'C'
        distribution = None

    class D(C):
        platform = 'D'

        @classmethod
        def distro_name(cls):
            return 'E'

    class E(D):
        @classmethod
        def distro_name(cls):
            return 'E'

    class F(Base):
        distribution = 'F'
        platform = None

    class G(F):
        distribution = 'G'
        platform = None

    class H(G):
        distribution = 'H'
        platform = None

   

# Generated at 2022-06-12 23:42:49.881095
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() not in (None, "")


# Generated at 2022-06-12 23:42:53.834724
# Unit test for function get_distribution_version
def test_get_distribution_version():
    distribution = get_distribution()
    version = get_distribution_version()
    if distribution == "Redhat":
        assert version == "7.6"
    elif distribution == "Debian":
        assert version == "8"
    elif distribution == "Arch":
        assert version == ""


# Generated at 2022-06-12 23:42:58.232107
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Unit test for function get_distribution_version
    '''
    # WARNING: This test is tightly coupled to the output of distro.version()
    # and distro.version(best=True) and will fail if the output of those
    # functions changes.  This is done because using mock here to replace the
    # output of those functions would be more complex than just testing the
    # results.  It is fine for now for testing the function.  If the output of
    # distro.version() changes, the assert below will need to be updated.
    assert get_distribution_version() == u'7.5'

# Generated at 2022-06-12 23:43:08.864406
# Unit test for function get_distribution
def test_get_distribution():

    # Test case: Platform is not Linux
    _platform = platform.system
    _distro = distro.id

    try:
        platform.system = lambda: 'FreeBSD'
        assert get_distribution() == 'Freebsd'
    finally:
        platform.system = _platform

    # Test case: Platform is Linux and distribution is known
    try:
        platform.system = lambda: 'Linux'
        distro.id = lambda: 'debian'
        assert get_distribution() == 'Debian'
    finally:
        platform.system = _platform
        distro.id = _distro

    # Test case: Platform is Linux and distribution is not known

# Generated at 2022-06-12 23:43:19.023772
# Unit test for function get_distribution
def test_get_distribution():
    '''Unit test for function get_distribution'''
    from ansible.module_utils.facts import get_distribution

    class TestDistroModule(object):

        @property
        def system(self):
            try:
                return self.data['system']
            except KeyError:
                pass

            return 'Unknown system'

        @property
        def distro_name(self):
            try:
                return self.data['name']
            except KeyError:
                pass

            return ''

        @property
        def distro_version(self):
            try:
                return self.data['version']
            except KeyError:
                pass

            return ''


# Generated at 2022-06-12 23:43:24.838637
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Unit test for function get_distribution_version
    '''

    version = get_distribution_version()

    if version:
        # Assert that this is not an empty string
        assert len(version) is not 0, "get_distribution_version() returned an empty string"

        if platform.system() == "Linux":
            # Assert that this is a string comprised of only digits and periods
            assert version.isdigit() or "." in version, 'get_distribution_version() returned "%s"' % version
        else:
            assert version is None, 'Incorrectly determined a version for non-Linux system'

    else:
        # Assert that the value of version is None
        assert version is None, "get_distribution_version() returned a non-None value"


# Generated at 2022-06-12 23:43:33.526907
# Unit test for function get_distribution_version
def test_get_distribution_version():
    id_to_version = {
        'arch': '',
        'centos': '7',
        'debian': '9.9',
        'fedora': '28',
        'opensuse-leap': '15',
        'rhel': '7.6',
        'ubuntu': '16.04',
        'ol': '7.6'
    }
    for id_, version in id_to_version.items():
        with patch('ansible.module_utils.common.distro.id', return_value=id_):
            assert get_distribution_version() == version


# Generated at 2022-06-12 23:43:41.803032
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class SubclassBase:
        distribution = None
        platform = None

    class SubclassA(SubclassBase):
        distribution = 'OtherLinux'
        platform = 'Linux'

    class SubclassB(SubclassBase):
        platform = 'Linux'

    class SubclassC(SubclassBase):
        distribution = 'OtherLinux'
        platform = 'FakeOS'

    class SubclassD(SubclassBase):
        distribution = 'FreeBSD'
        platform = 'Linux'

    class TestSubclass(SubclassBase):
        pass

    class TestSubclassA(TestSubclass):
        platform = 'Linux'

    class TestSubclassB(TestSubclass):
        platform = 'Linux'

    class TestSubclassC(TestSubclass):
        distribution = 'OtherLinux'
        platform = 'Linux'


# Generated at 2022-06-12 23:43:51.348510
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Unit test for function get_distribution_version
    '''
    # Test with a version of 7
    distro.id = lambda: 'CentOS'
    distro.version = lambda: '7'
    distro.version.__doc__ = 'A function'
    distro.version.__name__ = 'distro.version'
    distro.version = lambda best=False: '7.6'
    distro.version.__doc__ = 'A function'
    distro.version.__name__ = 'distro.version'
    assert get_distribution_version() == '7.6'

    # Test with a version of 10
    distro.id = lambda: 'CentOS'
    distro.version = lambda: '10'
    distro.version.__doc__ = 'A function'

# Generated at 2022-06-12 23:44:19.200784
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == None
    assert get_distribution_codename() == None

# Generated at 2022-06-12 23:44:29.794728
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.basic import AnsibleModule, get_platform_subclass

    this_platform = platform.system()
    distribution = get_distribution()

    class TestModule(AnsibleModule):
        def __new__(cls, *args, **kwargs):
            new_cls = get_platform_subclass(TestModule)
            return super(TestModule, new_cls).__new__(new_cls)

    # If we have a test module, try to instantiate it.  If we cannot, we're not testing the right platform.
    if TestModule:
        m = TestModule
    else:
        m = TestModule(dict())

    if distribution in ['Redhat', 'Centos', 'Fedora', 'Amazon']:
        assert m.platform == 'Linux'
        assert m.distribution

# Generated at 2022-06-12 23:44:30.546381
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() == '7'

# Generated at 2022-06-12 23:44:35.920508
# Unit test for function get_distribution
def test_get_distribution():
    '''
    :todo: Test for MacOS.
    '''

    # @todo: Test for MacOS platform
    # Test for Non-Linux platforms
    # We can't mock platform.system() here on current Python versions
    # The class method is called at the module import time.
    # It throws an exception if it's not Linux.
    # platform_system = platform.system
    # platform.system = MagicMock(return_value='darwin')
    # get_distribution()
    # platform.system = platform_system

    # Test for invalid Linux distribution
    distro_id = distro.id
    distro.id = MagicMock(return_value='')
    assert get_distribution() == 'OtherLinux'
    distro.id = distro_id

    # Test for valid Linux distributions
    distributions

# Generated at 2022-06-12 23:44:46.475836
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    """Test module for get_platform_subclass()."""
    import unittest

    class TestPlatform(platform.system()):
        """Test class for testing get_platform_subclass()."""
        def __init__(self, *args, **kwargs):
            """Instantiate the test class."""
            pass

    class TestDistribution(get_distribution()):
        """Test class for testing get_platform_subclass()."""
        def __init__(self, *args, **kwargs):
            """Instantiate the test class."""
            pass

    class TestPlatformSubclass(platform.system()):
        """Test class for testing get_platform_subclass()."""
        distribution = get_distribution()

        def __init__(self, *args, **kwargs):
            """Instantiate the test class."""


# Generated at 2022-06-12 23:44:57.761038
# Unit test for function get_distribution_codename

# Generated at 2022-06-12 23:45:07.384882
# Unit test for function get_distribution
def test_get_distribution():

    import platform

    class MockCheckDistro(object):
        def __init__(self, distro):
            self.distro = distro

    class MockDistro(object):
        id = MockCheckDistro('ubuntu')
        def version(self, best=False):
            return '16.04'

    class MockPlatform(object):
        system = MockCheckDistro('Linux')
        dist = MockDistro()

    base_distro = get_distribution()

    platform.system = MockCheckDistro('Linux')
    platform.dist = MockDistro()

    assert get_distribution() == 'Ubuntu'

    platform.system = MockCheckDistro('FreeBSD')
    assert get_distribution() == 'Other'

    platform.system = MockCheckDistro('Linux')
    platform.dist.id = MockCheckDistro

# Generated at 2022-06-12 23:45:15.573458
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # Arrange
    class DistributionId:
        def id(self):
            return self.distro

    distributionId = (DistributionId())

    # Act
    distributionId.distro = 'fedora'
    fedora = get_distribution_codename()

    distributionId.distro = 'ubuntu'
    ubuntu = get_distribution_codename()

    distributionId.distro = 'sles'
    suse = get_distribution_codename()

    distributionId.distro = 'centos'
    centos = get_distribution_codename()

    distributionId.distro = 'redhat'
    redhat = get_distribution_codename()

    distributionId.distro = 'amzn'
    amzn = get_distribution_codename()


# Generated at 2022-06-12 23:45:27.449851
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Normally, the unit tests for this function would be written as a test case in the
    # module_utils/basic.py test_get_platform_subclass but because this file is deprecated
    # as described in the note below, we do not want to add test cases for this file.
    #
    # Note: in the future, unit tests for this function may be moved to test_basic.py to ensure
    # that the function works as expected.
    from ansible.module_utils.basic import AnsibleModule

    class TestPlatform(object):
        platform = 'Linux'

    class TestRedhatPlatform(TestPlatform):
        distribution = 'Redhat'

    class TestFedoraPlatform(TestPlatform):
        distribution = 'Fedora'

    class TestDebianPlatform(TestPlatform):
        distribution = 'Debian'


# Generated at 2022-06-12 23:45:36.597777
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        distribution = None
        platform = 'Linux'
    class B(A):
        pass
    class C(B):
        pass
    class D(B):
        distribution = 'CentOS'
    class E(C):
        distribution = 'CentOS'
    class F(E):
        distribution = 'CentOS'
    class G(F):
        pass
    class H(F):
        distribution = 'CentOS'
        platform = 'Windows'
    sub_linux = get_platform_subclass(A)
    sub_centos = get_platform_subclass(B)
    sub_centos_distro = get_platform_subclass(D)
    sub_centos_platform_distro = get_platform_subclass(H)

# Generated at 2022-06-12 23:46:32.313209
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class NonLinux(object):
        platform = "NonLinux"

    class LinuxParent(object):
        platform = "Linux"

    class Fedora(LinuxParent):
        distribution = "Fedora"

    class TestModule(LinuxParent):
        platform = platform.system()
        distribution = get_distribution()

    assert NonLinux == get_platform_subclass(NonLinux)
    assert Fedora == get_platform_subclass(LinuxParent)
    assert TestModule == get_platform_subclass(LinuxParent)

# Generated at 2022-06-12 23:46:35.115290
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() is not None
    assert get_distribution_version() != ""

# Generated at 2022-06-12 23:46:39.785210
# Unit test for function get_distribution_version
def test_get_distribution_version():
    import distro
    distro.id = lambda: 'centos'
    distro.version = lambda b: '8.1'
    distro.version.__name__ = 'version'
    distro.version.__module__ = 'distro'
    distro.version.__qualname__ = 'version'

    assert get_distribution_version() == '8.1'

# Generated at 2022-06-12 23:46:40.974649
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() == distro.version()

# Generated at 2022-06-12 23:46:45.488687
# Unit test for function get_distribution

# Generated at 2022-06-12 23:46:55.186476
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    # check returns None if not a linux distro
    assert get_distribution_codename() is None

    # check returns expected codename for Ubuntu Xenial Xerus
    '''
    codename = "xenial"
    try:
        platform.uname = MagicMock(return_value=('Linux', 'test-machine', '4.4.0-127-generic',
                                                 '#153~14.04.1-Ubuntu SMP Fri May 25 14:14:10 UTC 2018', 'x86_64'))
        assert get_distribution_codename() == codename
    finally:
        platform.uname = platform.orig_uname
    '''

# Generated at 2022-06-12 23:47:05.809159
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test for function get_distribution_codename()
    '''

    # Test distro with no codename
    distro.id = lambda: 'fedora'
    distro.version = lambda *args, **kwargs: '20'
    distro.codename = lambda: ''
    distro.os_release_info = lambda: {'version_codename': ''}
    distro.lsb_release_info = lambda: {'codename': ''}
    assert get_distribution_codename() is None

    # Test distro with codename
    distro.id = lambda: 'ubuntu'
    distro.version = lambda *args, **kwargs: ''
    distro.codename = lambda: ''

# Generated at 2022-06-12 23:47:14.052084
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base():
        platform = 'Linux'
        distribution = None

    class BaseLinux(Base):
        platform = 'Linux'
        distribution = None

    class BaseLinuxSub(BaseLinux):
        platform = 'Linux'
        distribution = None

    class SpecificCentos(BaseLinux):
        distribution = 'Centos'

    class SpecificUbuntu(BaseLinux):
        distribution = 'Ubuntu'

    class SpecificSubCentos(SpecificCentos):
        distribution = 'Centos'

    class SpecificSubUbuntu(SpecificUbuntu):
        distribution = 'Ubuntu'

    class BaseFreebsd(Base):
        platform = 'FreeBSD'
        distribution = None

    class BaseFreebsdSub(BaseFreebsd):
        platform = 'FreeBSD'
        distribution = None


# Generated at 2022-06-12 23:47:24.698070
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # CentOS 6
    distro.id = lambda: "centos"
    distro.version = lambda: "6.10"
    distro.version.__annotations__ = {}
    assert get_distribution_version() == "6.10"

    # CentOS 7
    distro.id = lambda: "centos"
    distro.version = lambda: "7.6.1810"
    distro.version.__annotations__ = {}
    assert get_distribution_version() == "7.6"

    # Fedora 28
    distro.id = lambda: "fedora"
    distro.version = lambda: "28"
    distro.version.__annotations__ = {}
    assert get_distribution_version() == "28"

    # Fedora 29
    distro.id = lambda: "fedora"

# Generated at 2022-06-12 23:47:27.096986
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    codename = get_distribution_codename()
    assert codename == 'xenial'
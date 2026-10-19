

# Generated at 2022-06-12 23:38:17.781801
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Find a subclass for the platform the test is running on
    '''
    def TestClass(*args, **kwargs):
        pass

    return get_platform_subclass(TestClass)

# Generated at 2022-06-12 23:38:26.374369
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test distribution code name retrieval.

    Test get_distribution_codename() to make sure it is returning the correct
    code names for the following distributions:

    * Ubuntu 10.04, 12.04, 16.04
    * Debian 8, 9
    * Fedora 28, 29
    * RHEL 6, 7
    * CentOS 6, 7
    * Amazon Linux 2017.03, 2018.03
    '''


# Generated at 2022-06-12 23:38:37.143995
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class Base:
        pass

    class MacOSX(object):
        platform = "Darwin"
        distribution = "macOS"

    class RedHat(object):
        platform = "Linux"
        distribution = "RedHat"

    class SuSE(object):
        platform = "Linux"
        distribution = "Suse"

    class Linux(object):
        platform = "Linux"

    class BSD(object):
        platform = "BSD"

    class Solaris(object):
        platform = "SunOS"

    platform = "Linux"
    distribution = "RedHat"

    platform_to_test = get_distribution()
    distribution_to_test = get_distribution_version()

    assert get_platform_subclass(Base) == Base
    assert get_platform_subclass(MacOSX) == MacOSX


# Generated at 2022-06-12 23:38:49.275468
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import json
    needs_best_version = {
        'centos': '7',
        'centos_7': '7.5',
        'debian': '9',
        'debian_9': '9',
        'fedora': None,
        'fedora_28': '28',
        'fedora_29': '29',
        'result': '"codename" or "ubuntu_codename" in /etc/os-release (if not empty)',
    }

    ret = []
    for item in needs_best_version['result'].split(' or '):
        ret.extend(json.loads(item))

    for platform in needs_best_version:
        if platform.endswith('_x'):
            continue

# Generated at 2022-06-12 23:38:52.073832
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() == distro.version()

# Generated at 2022-06-12 23:39:00.967047
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        platform = None
        distribution = None
    class A(Base):
        platform = 'Linux'
        distribution = 'Ubuntu'
    class B(Base):
        platform = 'Linux'
        distribution = None
    class C(Base):
        platform = None
        distribution = None
    class D(Base):
        platform = 'Linux'
        distribution = 'Ubuntu'
    class E(Base):
        platform = 'Darwin'
        distribution = 'MacOS'
    class F(Base):
        platform = 'Linux'
        distribution = 'Ubuntu'

    def test_get_platform_subclass(platform, distribution, class_to_test, expected):
        import platform
        import ansible.module_utils.platform_linux
        class AnsibleModule:
            def __init__(self):
                self

# Generated at 2022-06-12 23:39:10.914929
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import ansible.module_utils.basic
    import ansible.module_utils.facts.linux
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.se.hwtype
    import ansible.module_utils.facts.system

    # Test IPv4Address on Linux
    class IPTest(ansible.module_utils.basic.AnsibleModule):
        pass
    assert ansible.module_utils.facts.network.IPv4Address == get_platform_subclass(ansible.module_utils.facts.network.IPAddress)
    assert ansible.module_utils.facts.network.IPv4Address == get_platform_subclass(ansible.module_utils.facts.network.IPv4Address)
    assert ansible.module_utils.facts.network.IPAddress == get_platform

# Generated at 2022-06-12 23:39:13.022671
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == None



# Generated at 2022-06-12 23:39:20.262022
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform
    import distro
    dist = platform.dist()
    distro.id = lambda: dist[0]
    distro.codename = lambda: dist[2]

    class Base:
        pass

    class RedHatBase(Base):
        distribution = "RedHat"
        platform = "Linux"

    class FedoraBase(Base):
        distribution = "Fedora"
        platform = "Linux"

    class LinuxBase(Base):
        distribution = None
        platform = "Linux"

    class AIXBase(Base):
        distribution = None
        platform = "AIX"

    class SunOSBase(Base):
        distribution = None
        platform = "SunOS"

    class NoMatchBase(Base):
        distribution = "Ubuntu"
        platform = "SunOS"

    # First, test the distribution is chosen if available

# Generated at 2022-06-12 23:39:30.447113
# Unit test for function get_distribution_codename

# Generated at 2022-06-12 23:39:44.046017
# Unit test for function get_distribution_version
def test_get_distribution_version():
    import platform

    class FakeOsReleaseInfo(object):
        def __init__(self, id, version, version_best, version_like=None,
                version_codename=None, ubuntu_codename=None):
            self.id = id
            self.version = version
            self.version_best = version_best
            self.version_like = version_like
            self.version_codename = version_codename
            self.ubuntu_codename = ubuntu_codename

    class FakeDistro(object):
        def __init__(self, osi, lsb_release, vendor_id=None):
            self.osi = osi
            self.lsb_release = lsb_release
            self.vendor_id = vendor_id


# Generated at 2022-06-12 23:39:55.022734
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import ansible.modules.platform as p

    # passing in the basename of the module
    assert get_platform_subclass(p.PlatformBase) == p.PlatformGeneric
    assert get_platform_subclass(p.File) == p.FileGeneric
    assert get_platform_subclass(p.User) == p.UserGeneric
    assert get_platform_subclass(p.Group) == p.GroupGeneric
    assert get_platform_subclass(p.Package) == p.PackageGeneric

    # passing in the module itself
    assert get_platform_subclass(p) == p.PlatformGeneric
    assert get_platform_subclass(p.File) == p.FileGeneric
    assert get_platform_subclass(p.User) == p.UserGeneric
    assert get_platform_subclass(p.Group) == p.GroupGeneric

# Generated at 2022-06-12 23:39:58.835504
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test for function get_distribution_codename

    :returns: None
    :rtype: None

    Method to test function get_distribution_codename.
    '''
    # Fedora has no codename.
    assert get_distribution_codename() == None


# Generated at 2022-06-12 23:40:05.722479
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Unit test for get_distribution_codename()
    '''
    assert get_distribution_codename() is None
    assert get_distribution_codename(distribution='mac') is None
    assert get_distribution_codename(distribution='ubuntu') == 'xenial'
    assert get_distribution_codename(distribution='redhat', version='7.4') is None
    assert get_distribution_codename(distribution='centos', version='7.4') is None
    assert get_distribution_codename(distribution='amazon', version='2') == '2018.03'

# Generated at 2022-06-12 23:40:18.500870
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # Redhat/CentOS
    os_release_info_centos = {
        'name': 'CentOS Linux',
        'id': 'centos',
        'version_id': '8',
        'version': '8 (Core)',
        'pretty_name': 'CentOS Linux 8 (Core)',
    }
    lsb_release_info_centos = {
        'distributor_id': 'CentOS',
        'description': 'CentOS Linux release 8 (Core)',
        'release': '8',
        'codename': 'Core',
    }
    # Fedora

# Generated at 2022-06-12 23:40:24.320094
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    if platform.system() == 'Linux':
        codename = get_distribution_codename()
        distro_id = distro.id()
        version = get_distribution_version()
        if distro_id == 'ubuntu':
            if version.startswith('14.04'):
                assert codename == 'trusty'
            elif version.startswith('16.04'):
                assert codename == 'xenial'
            elif version.startswith('18.04'):
                assert codename == 'bionic'
        elif distro_id == 'centos':
            if version.startswith('7'):
                assert codename == 'Core'
            elif version.startswith('6'):
                assert codename == 'Final'

# Generated at 2022-06-12 23:40:25.879394
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Linux'


# Generated at 2022-06-12 23:40:37.822747
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    p1 = platform.system()
    d1 = get_distribution()
    # p1 is from the OS, d1 is from distro.  In some cases (ex: Fedora 27+)
    # distro will be "linuxmint" but p1 will be "Linux"
    if p1 == d1:
        d1 = ''

    for i1 in ('', p1, d1, p1+d1):
        for i2 in ('', p1, d1, p1+d1):
            for i3 in ('', p1, d1, p1+d1):
                class TestClass:
                    platform = None
                    distribution = None

                class TestSubClass1(TestClass):
                    platform = i1

                class TestSubClass2(TestSubClass1):
                    platform = i2


# Generated at 2022-06-12 23:40:49.182541
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    ############################################################################
    # Test subclass hierarchy
    ############################################################################

    # create base class
    class A(object):
        platform = 'a'
        distribution = None
        distribution_version = None

    # create platform-specific subclass
    class B(A):
        platform = 'b'

    # create distribution-specific subclass
    class C(B):
        distribution = 'c'

    # create platform-distribution-specific subclass
    class D(C):
        platform = 'd'

    # create distribution version-specific subclass
    class E(D):
        distribution_version = 'e'

    # create platform distribution version-specific subclass
    class F(E):
        platform = 'f'

    # test that we can get the relevant subclass
    assert get_platform_subclass(A) == A
    assert get_

# Generated at 2022-06-12 23:41:00.069650
# Unit test for function get_distribution_version

# Generated at 2022-06-12 23:41:18.868101
# Unit test for function get_distribution
def test_get_distribution():

    ##########
    # CentOS #
    ##########

    # CentOS 7.5
    with open('test/get_distribution/centos-release-7.5', 'r') as f:
        distro.id = lambda: 'centos'
        distro.version = lambda: '7.5'
        distro.os_release_info = lambda: {'version_id': '7',
                                          'id': 'centos'}
        assert get_distribution() == 'Redhat'
        assert get_distribution_version() == '7.5'

    #########
    # Debian
    #########

    # Debian 9.4
    with open('test/get_distribution/debian_version-9.4', 'r') as f:
        distro.id = lambda: 'debian'
        distro

# Generated at 2022-06-12 23:41:29.206126
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class myclass:
        platform = 'This is the platform string'
        distribution = None

    class mysubclass1(myclass):
        pass

    class mysubclass2(myclass):
        platform = None
        distribution = 'This is the distribution string'

    class mysubclass3(myclass):
        platform = 'This is a different platform string'
        distribution = 'This is the distribution string'

    retval = get_platform_subclass(myclass)
    assert retval == myclass

    retval = get_platform_subclass(mysubclass1)
    assert retval == mysubclass1

    retval = get_platform_subclass(mysubclass2)
    assert retval == mysubclass2

    retval = get_platform_subclass(mysubclass3)
    assert retval == mysubclass

# Generated at 2022-06-12 23:41:40.096808
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test functionality of get_platform_subclass

    :returns: Tuple of two values. The first is a boolean indicating success or failure. The
        second is a string indicating reason for failure if the first value is False.
    :rtype: tuple
    '''
    UNIX = object()
    LINUX = object()
    REDHAT = object()
    CENTOS = object()
    AMAZON = object()
    FREEBSD = object()
    AIX = object()
    SUNOS = object()
    OTHER = object()

    class LinuxUnix(object):
        platform = 'Linux'
        distribution = None

    class OtherLinuxUnix(LinuxUnix):
        distribution = 'OtherLinux'

    class RedhatLinuxUnix(LinuxUnix):
        distribution = 'Redhat'


# Generated at 2022-06-12 23:41:51.825811
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Test that the return value of version() matches the version in /etc/os-release or /usr/lib/os-release
    '''
    version = get_distribution_version()

    supported_distros = frozenset((
        u'centos',
        u'debian',
        u'fedora',
        u'opensuse-leap',
        u'opensuse-tumbleweed',
        u'redhat',
        u'sles',
        u'ubuntu',
    ))

    if platform.system() == 'Linux':
        assert version is not None, "Returned version is None and must not be"

# Generated at 2022-06-12 23:41:56.950490
# Unit test for function get_distribution
def test_get_distribution():
    import mock
    import json
    import platform_data
    import os

    def get_os_release_contents():
        return json.dumps(platform_data.os_release_debian_wheezy)

    def get_lsb_release_contents():
        return platform_data.lsb_release_contents_debian_wheezy

    @mock.patch('ansible.module_utils.distro.os_release_info', get_os_release_contents)
    @mock.patch('ansible.module_utils.distro.lsb_release_info', get_lsb_release_contents)
    def test_get_distribution_debian_wheezy():
        distribution = get_distribution()
        version = get_distribution_version()
        codename = get_distribution_cod

# Generated at 2022-06-12 23:41:59.775553
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Confirm the get_distribution function returns correct value for Amazon
    '''
    assert get_distribution() == 'Amazon', "get_distribution() needs to return 'Amazon' for AWS Linux"



# Generated at 2022-06-12 23:42:05.939907
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.common.sys_info import SubclassA, SubclassB, SubclassC

    class BaseClass:
        platform = 'test'
        distribution = None
        def __init__(self):
            pass

    # On test platform:
    #   Base class should be returned
    #   SubclassA should be returned
    #   SubclassB should be returned
    #   SubclassC should be returned

    assert get_platform_subclass(BaseClass) == BaseClass
    assert get_platform_subclass(SubclassA) == SubclassA
    assert get_platform_subclass(SubclassB) == SubclassB
    assert get_platform_subclass(SubclassC) == SubclassC
    # End test class

    # On Linux, RedHat, 6.5:
    #   Base class should be

# Generated at 2022-06-12 23:42:08.021673
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # "fedora"
    assert get_distribution_codename() == 'Heisenbug'

    # "ubuntu"
    assert get_distribution_codename() == 'trusty'

# Generated at 2022-06-12 23:42:09.537434
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == "Fedora"



# Generated at 2022-06-12 23:42:13.142616
# Unit test for function get_distribution
def test_get_distribution():
    try:
        distro_id = distro.id()
    except Exception:
        distro_id = None

    expected = distro_id.capitalize()

    returned = get_distribution()

    if returned == "Rhel":
        returned = "RedHat"

    assert returned == expected


# Generated at 2022-06-12 23:42:39.128836
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    class MockDistroModule:
        codename = 'codename'
        id = 'id'
        os_release_info = {'version_codename': 'version_codename'}
        lsb_release_info = {'codename': 'lsb_codename'}

        @staticmethod
        def os_release_info():
            return MockDistroModule.os_release_info

        @staticmethod
        def id():
            return MockDistroModule.id

        @staticmethod
        def codename():
            return MockDistroModule.codename

        @staticmethod
        def lsb_release_info():
            return MockDistroModule.lsb_release_info

    # setup / teardown for tests
    def setup():
        distro.id = lambda: 'oldid'

# Generated at 2022-06-12 23:42:48.884783
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Unit test for function get_distribution.

    :rtype: list[str]
    :returns: list containing all failed tests
    '''
    from ansible.module_utils.common._collections_compat import Mapping

    failed_tests = []

    distribution = get_distribution()

    if not isinstance(distribution, Mapping):
        failed_tests.append("get_distribution(): return value is not a mapping")
    if not distribution[u'name']:
        failed_tests.append("get_distribution(): name is not set")
    if not distribution[u'version']:
        failed_tests.append("get_distribution(): version is not set")

    return failed_tests


# Generated at 2022-06-12 23:42:49.528823
# Unit test for function get_distribution_version
def test_get_distribution_version():
    pass

# Generated at 2022-06-12 23:42:52.450982
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test if the function get_distribution returns the right values.
    '''
    assert get_distribution() == platform.linux_distribution()[0]
    assert get_distribution() == 'Ubuntu'

# Generated at 2022-06-12 23:42:55.165247
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # Get the distribution version
    get_distribution_version()
    # Verfiy the distribution version is returned properly
    value = get_distribution_version()
    assert len(value) != 0

# Generated at 2022-06-12 23:42:56.485104
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version()
    if platform.system() != 'Linux':
        assert get_distribution_version() is None

# Generated at 2022-06-12 23:43:07.465726
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class cls:
        pass
    class sc1(cls):
        distribution = 'RedHat'
        platform = 'Linux'
    class sc2(cls):
        distribution = 'RedHat'
    class sc3(cls):
        distribution = 'RedHat'
        platform = 'Linux'
    class sc4(cls):
        distribution = 'RedHat'
    class sc5(cls):
        distribution = 'OtherLinux'
        platform = 'Linux'
    class sc6(cls):
        platform = 'Linux'
    class sc7(cls):
        distribution = 'OtherLinux'
        platform = 'Linux'
    class sc8(cls):
        distribution = 'OtherLinux'
        platform = 'Linux'


# Generated at 2022-06-12 23:43:17.754354
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Test function get_distribution_version
    '''
    # Test for platforms that use distro
    if get_distribution() == 'Ubuntu':
        assert get_distribution_version() == '16.04'
    elif get_distribution() == 'Redhat':
        assert get_distribution_version() == '7.7'
    elif get_distribution() == 'Centos':
        assert get_distribution_version() == '7'
    elif get_distribution() == 'Amazon':
        assert get_distribution_version() == '2'
    elif get_distribution() == 'OtherLinux':
        assert get_distribution_version() == ''
    elif get_distribution() == 'Suse':
        assert get_distribution_version() == '15.1'
   

# Generated at 2022-06-12 23:43:19.621502
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test get_distribution()
    '''

    assert get_distribution() == platform.system().capitalize()

# Generated at 2022-06-12 23:43:25.869947
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform
    import unittest

    class PlatformIndependentClass:
        platform = None
        distribution = None

        def __init__(self):
            pass

    class PlatformClass(PlatformIndependentClass):
        platform = None
        distribution = None

        def __init__(self):
            pass

    class DistributionClass(PlatformClass):
        platform = platform.system()
        distribution = get_distribution()

        def __init__(self):
            pass

    class PlatformDistributionClass(DistributionClass):
        platform = platform.system()
        distribution = get_distribution()

        def __init__(self):
            pass

    class TestGetPlatformSubclass(unittest.TestCase):
        def test_no_match(self):
            self.assertEqual(get_platform_subclass(PlatformIndependentClass), PlatformIndependentClass)

# Generated at 2022-06-12 23:43:55.409740
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    from ansible.module_utils.common._collections_compat import UserDict
    # Test for the first case in the function, when the version_codename is present in the os_release_info dictionary

    # Create an os_release_info dictionary with a version_codename
    os_release_info = UserDict({'version_codename': 'testing_version_codename'})

    def mock_os_release_info():
        return os_release_info

    # Create a distro.variant dictionary with a fake 'id'
    # This code runs in a try/except block that catches ImportError, so we need a real import to simulate that
    distro.variant = UserDict({'id': 'testing_id'})

    # Create a distro.os_release_info that returns our mock os_release_info
   

# Generated at 2022-06-12 23:43:56.428975
# Unit test for function get_distribution
def test_get_distribution():
    pass



# Generated at 2022-06-12 23:44:07.681914
# Unit test for function get_distribution
def test_get_distribution():
    distributions_platforms = {
        None: None,
        'arch': 'Linux',
        'centos': 'Linux',
        'debian': 'Linux',
        'fedora': 'Linux',
        'freebsd': None,
        'gentoo': 'Linux',
        'mandriva': 'Linux',
        'mandrake': 'Linux',
        'mageia': 'Linux',
        'netbsd': None,
        'openbsd': None,
        'opensuse': 'Linux',
        'sles': 'Linux',
        'suse': 'Linux',
        'ubuntu': 'Linux',
        'windows': None,
    }

    for (d, p) in distributions_platforms.items():
        distribution = get_distribution()

# Generated at 2022-06-12 23:44:18.113776
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        pass

    class Bar(Base):
        pass

    class LinuxBar(Bar):
        platform = 'Linux'

    class DarwinBar(Bar):
        platform = 'Darwin'

    class LinuxBarOnRedhat(LinuxBar):
        distribution = 'Redhat'

    # Test subclassing
    assert get_platform_subclass(Bar) is Bar
    assert get_platform_subclass(LinuxBar) is LinuxBar
    assert get_platform_subclass(DarwinBar) is DarwinBar
    # LinuxBar is more specific than DarwinBar
    assert get_platform_subclass(LinuxBarOnRedhat) is LinuxBarOnRedhat
    # But we can force it to get the base class instead
    assert get_platform_subclass(LinuxBarOnRedhat, get_base=True) is LinuxBar
    # LinuxBarOn

# Generated at 2022-06-12 23:44:28.587530
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    test_ubuntucodename = {'Ubuntu': 'xenial'}
    test_fedoracodename = {'Fedora': 'Silverblue'}
    test_centoscodename = {'CentOS': ''}
    test_debiancodename = {'Debian': 'buster'}
    test_slackwarecodename = {'Slackware': ''}
    test_rhelcodename = {'RedHat': ''}
    test_opensusecodename = {'openSUSE Leap': '15.0'}
    test_kubunutucodename = {'Kubuntu': 'bionic'}

    assert get_distribution_codename() == test_ubuntucodename.get(get_distribution())
    assert get_distribution_codename() == test_fedoracodename.get

# Generated at 2022-06-12 23:44:29.678854
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == get_distribution_codename()

# Generated at 2022-06-12 23:44:41.668523
# Unit test for function get_distribution
def test_get_distribution():
    initial_distro_id = distro.id

# Generated at 2022-06-12 23:44:42.946712
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == u'Centos'


# Generated at 2022-06-12 23:44:50.470723
# Unit test for function get_distribution_version
def test_get_distribution_version():
    class TestDistro():
        """
        Test class for distro.
        This class will mock the distro class behaviour.
        """
        def version(self, best=False):
            """
            Mock version to return the version as per distro.
            """
            distros = {'centos': '7.6.1810',
                       'redhat': '7.6',
                       'debian': '8.11',
                       'ubuntu': '16.04'}
            return distros[self.id()]

        def id(self):
            """
            Mock id to return the distro as per distro.
            """
            distros = {'centos': 'centos',
                       'redhat': 'redhat',
                       'debian': 'debian',
                       'ubuntu': 'ubuntu'}

# Generated at 2022-06-12 23:45:00.288420
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # no subclass
    class A:
        platform = None
        distribution = None

    assert get_platform_subclass(A) is A

    # Windows subclass
    class A_Win:
        platform = 'Windows'
        distribution = None

    assert get_platform_subclass(A) is A_Win

    # Windows subclass without generic
    class A_Win:
        platform = 'Windows'
        distribution = None

    assert get_platform_subclass(A_Win) is A_Win

    # Linux subclass
    class A_Linux:
        platform = 'Linux'
        distribution = None

    class A(A_Linux):
        platform = None
        distribution = None

    assert get_platform_subclass(A) is A_Linux

    # Linux subclass without generic
    class A(A_Linux):
        platform = None
       

# Generated at 2022-06-12 23:45:27.271299
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # This class is used to test the test.  It's a subclass of object so we
    # don't have to worry about other attributes having side-effects
    class Test(object):
        distribution = None
        platform = 'Linux'

    class TestEl6(Test):
        distribution = 'Redhat'
        platform = 'Linux'

    class TestOtherLinux(Test):
        distribution = 'OtherLinux'
        platform = 'Linux'

    class TestOtherOS(Test):
        distribution = 'OtherOS'
        platform = 'OtherOS'

    class TestOtherLinux2(Test):
        distribution = 'OtherLinux'
        platform = 'Linux'

    assert get_platform_subclass(Test) == Test, 'get_platform_subclass() with only one subclass'


# Generated at 2022-06-12 23:45:29.271106
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert(get_distribution_version() != None)

# Generated at 2022-06-12 23:45:35.258639
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Basic test function for function get_platform_subclass
    '''
    # Import here so that get_platform_subclass is available to the test code
    import ansible.module_utils.basic
    result = ansible.module_utils.basic.get_platform_subclass(ansible.module_utils.basic.AnsibleModule)
    assert result.__name__ == 'AnsibleModule'

# Generated at 2022-06-12 23:45:43.032351
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    """
    Function get_platform_subclass() Unit Tests
    """


# Generated at 2022-06-12 23:45:53.831532
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        platform = 'linux'

    class B:
        platform = 'linux'
        distribution = 'Redhat'

    class C:
        platform = 'linux'
        distribution = 'Amazon'

    class D:
        platform = 'ohmylinux'

    class E(A):
        platform = 'linux'
        distribution = 'Amazon'

    class F(B):
        platform = 'linux'
        distribution = 'Amazon'

    class G(C):
        platform = 'linux'
        distribution = 'Redhat'

    assert get_platform_subclass(A) == A
    assert get_platform_subclass(B) == B
    assert get_platform_subclass(C) == C
    assert get_platform_subclass(D) == D
    assert get_platform_subclass(E) == E


# Generated at 2022-06-12 23:46:05.500769
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform
    import ansible.module_utils.basic
    import ansible.module_utils.other
    import ansible.module_utils.debian_common
    import ansible.module_utils.freebsd_pkgng
    import ansible.module_utils.redhat_yum
    import ansible.module_utils.redhat_subscription

    class Subclass1:
        platform = 'Something'
        distribution = None

    class Subclass2:
        platform = 'Something'
        distribution = 'SomethingElse'

    class Subclass3:
        platform = 'Linux'
        distribution = 'SomethingElse'

    class Subclass4:
        platform = 'Darwin'
        distribution = None

    class Subclass5:
        platform = 'Something'
        distribution = None


# Generated at 2022-06-12 23:46:15.355598
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    """
    This is a unit test to verify the behavior of get_platform_subclass()
    """
    import sys

    class baseclass:
        platform = "Default"
        distribution = None

    class subclass1(baseclass):
        platform = "Linux"

    class subclass2(baseclass):
        platform = "Linux"
        distribution = "Ubuntu"

    class subclass3(baseclass):
        platform = "Linux"
        distribution = "OtherLinux"

    class subclass4(baseclass):
        platform = "Other"

    # We only want to check the return of get_platform_subclass(), so we'll
    # mock out the get_distribution() calls

    real_get_distribution = get_distribution
    def mock_get_distribution():
        return "Ubuntu"
    get_distribution = mock_get

# Generated at 2022-06-12 23:46:18.221173
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == u'Redhat' or get_distribution() == u'Amazon', "The distribution is not recognized"


# Generated at 2022-06-12 23:46:28.630904
# Unit test for function get_distribution
def test_get_distribution():
    print("FUNCTION get_distribution")
    print("========================")
    print()
    print("Test 1:")
    print("-------")
    print("  System: Linux")
    print("  Distribution: CentOS")
    print("  Expected: Redhat")
    print("  Actual: %s" % get_distribution())

    print()
    print("Test 2:")
    print("-------")
    print("  System: FreeBSD")
    print("  Distribution: N/A")
    print("  Expected: FreeBSD")
    print("  Actual: %s" % get_distribution())

    print()
    print("Test 3:")
    print("-------")
    print("  System: Linux")
    print("  Distribution: Debian")
    print("  Expected: Debian")

# Generated at 2022-06-12 23:46:35.304090
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test case for the ``get_distribution_codename`` function

    The get_distribution_codename function gets the code name for the Linux Distribution

    :rtype: None
    '''

    expected_results = {
        "Amazon": None,
        "Centos": None,
        "Debian": None,
        "Fedora": None,
        "OEL": None,
        "OracleLinux": None,
        "Redhat": None,
        "Suse": None,
        "Ubuntu": "xenial"
    }
    for key, expected_result in expected_results.items():
        distro = get_distribution_codename()
        if expected_result is not None:
            assert distro == expected_result
    return

# Generated at 2022-06-12 23:47:30.739890
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # TestCase classes need to have this  name
    class TestCase1(object):
        pass

    # TestCase classes need to have this  name
    class TestCase2(object):
        pass

    # Subclass of TestCase1
    class TestCase1Subclass(TestCase1):
        pass

    # Subclass of TestCase2
    class TestCase2Subclass(TestCase2):
        pass

    # Subclass of TestCase1Subclass
    class TestCase1SubclassSubclass(TestCase1Subclass):
        pass

    # Subclass of TestCase1
    class TestCase1OtherSubclass(TestCase1):
        pass

    # Subclass of TestCase1
    class TestCase1OtherSubclass2(TestCase1):
        pass

    returned = get_platform_subclass(TestCase1)

# Generated at 2022-06-12 23:47:31.483083
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() is None

# Generated at 2022-06-12 23:47:39.391223
# Unit test for function get_distribution_version
def test_get_distribution_version():
    cases = (
        ('amzn-1', ('amzn', u'1')),
        ('Ubuntu Linux - 14.04', ('Ubuntu', u'14.04')),
        ('RedHat Linux', ('RedHat', u'')),
        ('FreeBSD', (None, None)),
        ('OpenBSD', (None, None)),
        ('', (None, None)),
        (None, (None, None)),
    )

    for (version, expected) in cases:
        distro.id.return_value = expected[0]
        distro.version.return_value = version
        have = get_distribution()
        assert have == expected[0]

        have = get_distribution_version()
        assert have == expected[1]

# Generated at 2022-06-12 23:47:40.598933
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() == distro.version()


# Generated at 2022-06-12 23:47:41.784522
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == distro.id().capitalize()

# Generated at 2022-06-12 23:47:43.643998
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Unit test for function get_distribution_codename
    '''
    assert None == get_distribution_codename()

# Generated at 2022-06-12 23:47:50.449076
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    # create base class
    class BaseClass:
        pass

    # create subclass
    class SubClassA(BaseClass):
        platform = 'Darwin'
        distribution = None

    # create subclass
    class SubClassB(BaseClass):
        platform = 'Linux'
        distribution = 'Redhat'

    # create subclass
    class SubClassC(BaseClass):
        platform = 'Linux'
        distribution = 'Debian'

    # create subclass
    class SubClassD(BaseClass):
        platform = 'Linux'
        distribution = 'Ubuntu'

    # create subclass
    class SubClassE(BaseClass):
        platform = 'Linux'
        distribution = None

    # create platform of osx, redhat
    platform.system = lambda: 'Darwin'
    get_distribution = lambda: 'Ubuntu'

# Generated at 2022-06-12 23:48:02.081629
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    ''' Ansible get_distribution_codename() unit test '''

    # codename is expected to be None on a non-Linux system
    non_linux_codename = get_distribution_codename()
    if non_linux_codename is not None:
        assert False, 'This is not a Linux system, codename is expected to be None'

    # codename is expected to be None on unsupported Linux system
    unsupported_linux_distro_codename = 'UnsupportedLinuxDistro'
    distro.id = lambda: unsupported_linux_distro_codename
    unsupported_linux_codename = get_distribution_codename()
    if unsupported_linux_codename is not None:
        assert False, 'This is an unsupported Linux system, codename is expected to be None'

    # codename is expected to be 'focal'

# Generated at 2022-06-12 23:48:09.492464
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class foo(object):
        platform = 'foo'
        distribution = None
    class bar(foo):
        platform = 'bar'
    class baz(bar):
        distribution = 'baz'
    class biz(bar):
        distribution = 'biz'
    class fiz(foo):
        distribution = 'fiz'
    class gag(foo):
        distribution = 'gag'
    class gug(foo):
        distribution = 'gug'
    class blah(gug):
        platform = 'blah'

    platform.system = lambda: 'foo'
    get_distribution = lambda: None

    assert(get_platform_subclass(foo) == foo)
    assert(get_platform_subclass(bar) == foo)
    assert(get_platform_subclass(baz) == baz)
   
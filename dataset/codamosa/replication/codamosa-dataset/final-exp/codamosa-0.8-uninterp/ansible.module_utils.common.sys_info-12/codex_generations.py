

# Generated at 2022-06-12 23:38:21.278323
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class A:
        distribution = None
        platform = None

    class B(A):
        distribution = "TestDistro"
        platform = platform.system()

    class C(A):
        distribution = None
        platform = platform.system()

    assert get_platform_subclass(A) is A
    assert get_platform_subclass(B) is B
    if B.platform == platform.system():
        assert get_platform_subclass(C) is C
    else:
        assert get_platform_subclass(C) is A

# Test for platform.py subclasses get_platform_subclass

# Generated at 2022-06-12 23:38:29.369401
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Parent(object):
        platform = None
        distribution = None

    class OtherClass:
        pass

    class ChildA(Parent):
        platform = 'Linux'
        distribution = None

    class ChildB(Parent):
        platform = 'Linux'
        distribution = 'Centos'

    class ChildC(Parent):
        platform = 'Linux'
        distribution = 'Ubuntu'

    class ChildD(Parent):
        platform = 'FreeBSD'
        distribution = None

    assert ChildA == get_platform_subclass(Parent)
    assert ChildA == get_platform_subclass(ChildA)
    assert ChildB == get_platform_subclass(ChildB)
    assert ChildC == get_platform_subclass(ChildC)
    assert ChildD == get_platform_subclass(ChildD)
    assert _GenericUser == get

# Generated at 2022-06-12 23:38:30.486170
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution()

# Generated at 2022-06-12 23:38:39.178633
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test the get_distribution function.

    :rtype: bool
    :returns: True if successful, false otherwise

    Source files:  ansible/test/utils/test_module_utils_basic.py
    '''
    # Note:  This will not be sufficient in the future.  In the future, the
    # distribution must be determined and tested in a way that is
    # distribution-independent.
    try:
        distribution = get_distribution()
    except Exception as e:
        print('Failed to determine distribution:  ' + str(e))
        distribution = None

    if distribution is None:
        print('Failed to determine distribution')
        return False

    return True


# Generated at 2022-06-12 23:38:50.820651
# Unit test for function get_distribution_version
def test_get_distribution_version():
    def _test_get_distribution_version(distro_id, version, version_best, expected_version):
        distro._distro = None
        distro._distro_release = None
        distro._distro_version = None

        distro.id = lambda: distro_id
        distro.version = lambda: version
        distro.version = lambda best=False: version_best if best else version

        actual_version = get_distribution_version()
        assert actual_version == expected_version, 'Expected %r but got %r' % (expected_version, actual_version)

    _test_get_distribution_version('redhat', '7.5', '7.5', '7.5')

# Generated at 2022-06-12 23:39:00.398236
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    ''' test_get_platform_subclass is a unit test to confirm function get_platform_subclass returns the correct
        subclass based on the host platform.

        For this test to pass, the test must be run on a Linux host. This will exclude Windows and MacOSX.
    '''

    def test_subclass(platform, distribution):
        ''' This function will provide the subclass based on platform and distribution. '''
        class _test_subclass_template(object):
            ''' This class is a template for get_platform_subclass test class. '''

            platform = platform
            distribution = distribution

        return _test_subclass_template


# Generated at 2022-06-12 23:39:10.779372
# Unit test for function get_distribution

# Generated at 2022-06-12 23:39:11.394932
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'OtherLinux'

# Generated at 2022-06-12 23:39:13.471572
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() == distro.version()

# Generated at 2022-06-12 23:39:23.260738
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # subclass and cls are the same class
    class BaseClass:
        pass

    assert BaseClass == get_platform_subclass(BaseClass)

    # class has no subclass
    class BaseClass:
        pass

    class SubClass1(BaseClass):
        pass

    assert BaseClass == get_platform_subclass(BaseClass)

    # class has a subclass and cls is the subclass
    class BaseClass:
        pass

    class SubClass1(BaseClass):
        pass

    assert SubClass1 == get_platform_subclass(SubClass1)

    # class has a subclass and cls is the superclass
    class BaseClass:
        pass

    class SubClass1(BaseClass):
        pass

    assert SubClass1 == get_platform_subclass(BaseClass)

    # class has a subclass and cls is neither


# Generated at 2022-06-12 23:39:30.755625
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test function get_distribution_codename
    '''
    assert get_distribution_codename() == 'focal'

# Generated at 2022-06-12 23:39:40.160352
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.basic import AnsibleModule, load_platform_subclass

    class TestClass:
        pass

    class TestSubclass(TestClass):
        pass

    # Examine base class
    assert get_platform_subclass(TestClass) == TestClass

    # Examine subclass
    assert get_platform_subclass(TestSubclass) == TestSubclass

    # Examine subclass with platform and distribution
    class LinuxUser(TestClass):
        platform = 'Linux'
        distribution = None

    class LinuxUbuntuUser(LinuxUser):
        distribution = 'Ubuntu'

    class LinuxRedHatUser(LinuxUser):
        distribution = 'Redhat'

    assert get_platform_subclass(LinuxUser) == LinuxUser
    assert get_platform_subclass(LinuxUbuntuUser) == LinuxUbuntuUser
    assert get

# Generated at 2022-06-12 23:39:44.441306
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class SuperClass:
        platform = 'Linux'
        distribution = None

    class SubClass(SuperClass):
        platform = 'Linux'
        distribution = 'CentOS'

    class OtherSubClass(SuperClass):
        platform = None
        distribution = None

    assert get_platform_subclass(SuperClass) == SuperClass
    assert get_platform_subclass(SubClass) == SubClass
    assert get_platform_subclass(OtherSubClass) == OtherSubClass

# Generated at 2022-06-12 23:39:48.972810
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class PlatformIndependent(object):
        platform = "Independent"

    class BasePlatform(object):
        platform = "APlatform"

    class BasePlatformUbuntu(BasePlatform):
        distribution = "Ubuntu"

    class BasePlatformSpecificDistro(PlatformIndependent):
        platform = "APlatform"
        distribution = "ADistro"

    class BasePlatformAnotherDistro(PlatformIndependent):
        platform = "APlatform"
        distribution = "AnotherDistro"

    class BasePlatformOtherLinux(PlatformIndependent):
        platform = "APlatform"
        distribution = "OtherLinux"

    class BasePlatformBPlatform(BasePlatform):
        platform = "BPlatform"

    class BasePlatformBPlatformSpecificDistro(BasePlatformBPlatform):
        distribution = "ADistro"

    # No platform subclass of PlatformIndependent
    assert PlatformIndependent == get_platform_subclass

# Generated at 2022-06-12 23:39:53.778228
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # Return valid version numbers
    expected_distros = {'Ubuntu': '16.04', 'Debian': '8', 'CentOS': '7.6.1810', 'Raspbian': '9'}
    for distro, version in expected_distros.items():
        assert (get_distribution_version() == version)  # nosec

# Generated at 2022-06-12 23:40:03.442329
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test the get_platform_subclass() function
    '''
    class Parent(object):
        '''
        The parent class.  This class will be passed to get_platform_subclass()
        '''
        platform = None
        distribution = None

    class ChildLinuxA(Parent):
        '''
        A child that is specific to Linux distributions
        '''
        platform = u'Linux'

    class ChildLinuxB(ChildLinuxA):
        '''
        A child that is specific to Linux distributions with a distribution name
        '''
        distribution = u'Debian'

    assert get_platform_subclass(Parent) == Parent  # No Linux subclass.
    assert get_platform_subclass(ChildLinuxA) == ChildLinuxA  # platform matches, no distribution specified.

# Generated at 2022-06-12 23:40:08.155690
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Test(object):
        pass

    class TestLinux(Test):
        platform = 'Linux'

    class TestLinuxOther(Test):
        platform = 'Linux'

    class TestLinuxFedora(Test):
        platform = 'Linux'
        distribution = 'Fedora'

    class TestLinuxFedora23(Test):
        platform = 'Linux'
        distribution = 'Fedora'

    class TestLinuxFedora24(Test):
        platform = 'Linux'
        distribution = 'Fedora'

    class TestLinuxFedora25(Test):
        platform = 'Linux'
        distribution = 'Fedora'

    class TestLinuxFedora26(Test):
        platform = 'Linux'
        distribution = 'Fedora'

    class TestLinuxFedora27(Test):
        platform = 'Linux'
        distribution = 'Fedora'


# Generated at 2022-06-12 23:40:10.002082
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'jessie'

# Generated at 2022-06-12 23:40:20.547171
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    # Create classes which will subclasses of the base class
    class base(object):
        platform = None
        distribution = None

    class linux_subclass(base):
        platform = 'Linux'
        distribution = None

    class centos_subclass(linux_subclass):
        distribution = 'Centos'

    class rhel_subclass(linux_subclass):
        distribution = 'Redhat'

    class sles_subclass(linux_subclass):
        distribution = 'Sles'

    class OtherLinux_subclass(linux_subclass):
        distribution = 'OtherLinux'

    class darwin_subclass(base):
        platform = 'Darwin'
        distribution = None

    class freebsd_subclass(base):
        platform = 'FreeBSD'
        distribution = None


# Generated at 2022-06-12 23:40:21.460159
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'rolled'

# Generated at 2022-06-12 23:40:41.321246
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    # Specific platform data
    test_data = {'centos-7':u'Core',
                 'centos-7-minor':u'Core',
                 'centos-7-with-codename':u'Core',
                 'debian-9':u'stretch',
                 'rhel-8-preview':u'Core',
                 'ubuntu-16.04':u'xenial',
                 'ubuntu-16.10':u'yakkety',
                 }

    for test_case in test_data.keys():
        with open('/tmp/ansible_test_platform_data/{0}/etc/os-release'.format(test_case)) as f:
            os_release_contents = f.read()


# Generated at 2022-06-12 23:40:42.832918
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Amazon'


# Generated at 2022-06-12 23:40:52.016547
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import Debian
    from ansible.module_utils.facts.system.distribution import RedHat
    from ansible.module_utils.facts.system.distribution import SuSE
    from ansible.module_utils.facts.system.distribution import FreeBSD
    from ansible.module_utils.facts.system.distribution import OpenBSDLinux
    from ansible.module_utils.facts.system.distribution import Platform

    assert get_platform_subclass(Distribution) is Distribution
    assert get_platform_subclass(Debian) is Debian
    assert get_platform_subclass(RedHat) is RedHat
    assert get_platform_subclass(SuSE) is SuSE
    assert get_platform

# Generated at 2022-06-12 23:41:02.032072
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base(object):
        pass

    class Linux(object):
        platform = 'Linux'
    class RedHat(object):
        platform = 'Linux'
        distribution = 'RedHat'
    class Suse(object):
        platform = 'Linux'
        distribution = 'Suse'
    class OpenSuse(object):
        platform = 'Linux'
        distribution = 'OpenSuse'
    class Fedora(object):
        platform = 'Linux'
        distribution = 'Fedora'
    class Solaris(object):
        platform = 'Solaris'


# Generated at 2022-06-12 23:41:02.880349
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    pass

# Generated at 2022-06-12 23:41:04.145806
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == "jessie"

# Generated at 2022-06-12 23:41:12.990135
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        ''' This is the base class '''
        platform = 'Generic'
        distribution = None

    class A_Linux(A):
        ''' This is a linux subclass '''
        platform = 'Linux'

    class A_Linux_Distro(A):
        ''' This is a linux distro subclass '''
        platform = 'Linux'
        distribution = 'GenericLinux'

    class A_Linux_OtherDistro(A):
        ''' This is a linux other distro subclass '''
        platform = 'Linux'
        distribution = 'OtherLinux'

    class B(A_Linux_Distro):
        ''' This class is a subclass of A_Linux_Distro '''

    class C(A_Linux_OtherDistro):
        ''' This class is a subclass of A_Linux_OtherDistro '''



# Generated at 2022-06-12 23:41:19.972175
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Unit test for function get_distribution_version
    '''
    # Clear out distro cache
    distro.linux_distribution = (None, None, None)
    distro._lsb_release_info.clear()
    distro._os_release_info.clear()

    assert get_distribution_version() is None

    # Mock lsb_release to output unknown id
    def mocked_lsb_release(*args, **kwargs):
        # Linux Standard Base 3.2
        return ('N/A', 'N/A', 'N/A')
    distro.lsb_release = mocked_lsb_release

    assert get_distribution_version() is None

    # Mock lsb_release to output Ubuntu Xenial Xerus

# Generated at 2022-06-12 23:41:21.792286
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Centos'


# Generated at 2022-06-12 23:41:30.637179
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''This tests functionality of get_platform_subclass()'''
    class Base(object):
        platform = 'base'
        distribution = None

    class Linux(Base):
        platform = 'Linux'
        distribution = None

    class RedHat(Linux):
        platform = 'Linux'
        distribution = 'RedHat'

    class Fedora(RedHat):
        platform = 'Linux'
        distribution = 'Fedora'

    class Debian(Linux):
        platform = 'Linux'
        distribution = 'Debian'

    class Windows(Base):
        platform = 'Windows'
        distribution = None

    class WindowsServer(Windows):
        distribution = 'WindowsServer'

    assert get_platform_subclass(Linux) == Linux
    assert get_platform_subclass(RedHat) == Fedora
    assert get_platform_subclass(Debian)

# Generated at 2022-06-12 23:41:53.242531
# Unit test for function get_distribution_version
def test_get_distribution_version():
    from ansible.module_utils.common.collections import ImmutableDict
    try:
        import distro
        DISRO_VERSION_ATTR = 'version'
    except ImportError:
        DISRO_VERSION_ATTR = 'version_best'
    distro_value = '1337.42'

    class MockDistro:
        def __init__(self, version, id_, version_best=None):
            setattr(self, DISRO_VERSION_ATTR, version)
            self.id = lambda: id_
            if version_best is None:
                def version_best():
                    raise NotImplementedError
            else:
                self.version_best = lambda: version_best

    class MockLinuxDistro:
        def version(self, best=False):
            if best:
                return self.version

# Generated at 2022-06-12 23:41:55.237614
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'xenial' or get_distribution_codename() == None

# Generated at 2022-06-12 23:42:02.796960
# Unit test for function get_distribution
def test_get_distribution():
    # Format is:
    # (input, expected)
    test_cases = (
        ('', 'OtherLinux'),
        ('ID=fedora', 'Fedora'),
        ('ID=centos', 'Centos'),
        ('ID=redhat', 'Redhat'),
        ('ID=rhel', 'Redhat'),
        ('ID=amzn', 'Amazon'),
        ('ID=ol', 'OracleLinux'),
        ('ID=ol\nVERSION_ID=7.5', 'OracleLinux'),
    )

    for test_case in test_cases:
        distro.id = lambda: test_case[0]
        assert test_case[1] == get_distribution()

# Generated at 2022-06-12 23:42:12.253438
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Function under test
    from ansible.module_utils.facts.system.distribution import get_platform_subclass

    # Test class A
    class A:
        platform = "N/A"
        distribution = None

        def __init__(self):
            pass

    # Test class B
    class B:
        platform = "Linux"
        distribution = None

        def __init__(self):
            pass

    # Test class C
    class C:
        platform = "Linux"
        distribution = "Fedora"

        def __init__(self):
            pass

    # Test class D
    class D:
        platform = "Linux"
        distribution = "Ubuntu"

        def __init__(self):
            pass

    assert get_platform_subclass(A) == A
    assert get_platform_subclass

# Generated at 2022-06-12 23:42:22.242584
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # Parameter codename
    codename = "codename"

    # Parameter id
    id = "id"

    # Parameter version_id
    version_id = "version_id"

    # Parameter id_like
    id_like = "id_like"

    # Parameter version
    version = "version"

    # Parameter pretty_name
    pretty_name = "pretty_name"

    # Parameter version_codename
    version_codename = "version_codename"

    # Parameter variants
    variants = "variants"

    # Parameter ansible_facts

# Generated at 2022-06-12 23:42:22.915895
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() is not None

# Generated at 2022-06-12 23:42:23.533430
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Linux'

# Generated at 2022-06-12 23:42:29.751201
# Unit test for function get_distribution
def test_get_distribution():

    # Tests for all supported OSes (except FreeBSD)
    assert get_distribution() == 'Freebsd'
    assert get_distribution() == 'Darwin'
    assert get_distribution() == 'Openbsd'
    assert get_distribution() == 'Windows'
    assert get_distribution() == 'Linux'

    # handle unknown or unreleased Linux distros
    # http://distrowatch.com/search.php?distribution=foo&release=latest
    assert get_distribution() == 'OtherLinux'
    assert get_distribution() == 'OtherLinux'

    # handle known Linux distros

# Generated at 2022-06-12 23:42:35.438341
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    distro_codes = {'ubuntu': 'xenial', 'fedora': '28', 'debian': 'stretch', 'centos': '7.5.1804'}
    for distro_id, distro_codename in distro_codes.items():
        distro.id = lambda: distro_id
        assert get_distribution_codename() == distro_codename

# Generated at 2022-06-12 23:42:42.811562
# Unit test for function get_distribution
def test_get_distribution():
    from ansible.module_utils.common._collections_compat import Iterable
    import platform

    # Test base Linux distributions
    assert get_distribution() == 'Amazon'
    assert get_distribution_version() == '2'
    assert get_distribution_codename() == 'amzn2'

    # Linux distributions
    platform.system = lambda: 'Linux'
    assert get_distribution() == 'Amazon'
    assert get_distribution_version() == '2'

    distro.id = lambda: 'amzn'
    assert get_distribution() == 'Amazon'
    assert get_distribution_version() == '2'

    distro.id = lambda: 'centos'
    distro.version = lambda best: '7' if best else '7.5.1804'
    distro.version.__

# Generated at 2022-06-12 23:43:13.411034
# Unit test for function get_distribution
def test_get_distribution():
    import os
    import unittest

    class TestGetDistribution(unittest.TestCase):
        '''
        Unit test for the get_distribution function
        '''

        @property
        def orig_id(self):
            '''
            Property to save and restore id() from distro

            :returns: Value of distro.id()
            :rtype: NativeString or None
            '''
            return distro.id()

        @orig_id.setter
        def orig_id(self, val):
            '''
            Set the correct value for distro.id()
            '''
            distro.id = lambda: val


# Generated at 2022-06-12 23:43:14.738359
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Centos'


# Generated at 2022-06-12 23:43:22.913259
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class UserType:
        platform = 'Linux'
        distribution = None

    class UserType_Linux(UserType):
        platform = 'Linux'
        distribution = None

    class UserType_Linux_Redhat(UserType):
        platform = 'Linux'
        distribution = 'Redhat'

    class UserType_Linux_Amazon(UserType):
        platform = 'Linux'
        distribution = 'Amazon'

    class UserType_Linux_OtherLinux(UserType):
        platform = 'Linux'
        distribution = 'OtherLinux'

    class UserType_Linux_OtherLinux_Redhat(UserType):
        platform = 'Linux'
        distribution = 'OtherLinux_Redhat'

    class UserType_Linux_OtherLinux_Amazon(UserType):
        platform = 'Linux'
        distribution = 'OtherLinux_Amazon'


# Generated at 2022-06-12 23:43:33.935664
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class a:
        pass
    class b:
        platform = platform.system()
    class c:
        platform = "FOO"
    class d(a):
        platform = platform.system()
    class e(a):
        platform = "FOO"
    class f(d):
        distribution = "BAR"
    class g(d):
        distribution = get_distribution()

    assert get_platform_subclass(a) == a
    assert get_platform_subclass(b) == b
    assert get_platform_subclass(c) == a
    assert get_platform_subclass(d) == d
    assert get_platform_subclass(e) == e
    assert get_platform_subclass(f) == a
    assert get_platform_subclass(g) == g

# Generated at 2022-06-12 23:43:44.420572
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        platform = None
        distribution = None

    # No distribution specified, distribution should be None
    class Test1(Base):
        platform = 'Linux'
    subclass = get_platform_subclass(Test1)
    assert subclass.platform == Test1.platform
    assert subclass.distribution is None

    # Test when the caller passed in distribution
    class Test2(Base):
        platform = 'Linux'
        distribution = 'redhat'
    subclass = get_platform_subclass(Test2)
    assert subclass.platform == Test2.platform
    assert subclass.distribution == Test2.distribution

    # Test when the caller did not pass in distribution, and there are multiple
    # super classes for the same platform
    class Test3(Base):
        platform = 'Linux'
        distribution = 'debian'


# Generated at 2022-06-12 23:43:53.384557
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import default_collector
    import ansible.module_utils.facts as facts

    # Case 1:
    # - Running on FreeBSD
    # - Module does not provide a subclass for FreeBSD
    # - Default is unix
    # Expected outcome:
    # - cls returned is facts.UnixFactCollector
    # - Collector.platform is FreeBSD
    # - Collector.distribution is None
    default_collector.platform = None
    default_collector.distribution = None
    module = AnsibleModule({})
    default_collector.collect(module)
    cls = get_platform_subclass(facts.DefaultFactCollector)
    assert cls.platform == 'FreeBSD'
    assert cls.distribution is None


# Generated at 2022-06-12 23:44:06.254077
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit test for function get_platform_subclass

    :returns: True
    :rtype: bool
    '''
    class A(object):
        platform = 'A'
        distribution = 'A'

    class B(A):
        distribution = 'B'

    class C(A):
        platform = 'C'

    class D(A):
        platform = 'D'
        distribution = 'D'

    class E(C):
        distribution = 'E'

    assert A == get_platform_subclass(A)
    assert B == get_platform_subclass(A)
    assert C == get_platform_subclass(A)
    assert D == get_platform_subclass(A)
    assert E == get_platform_subclass(A)
    return True

# Generated at 2022-06-12 23:44:15.710595
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test if get_distribution_codename handle specific distros codename
    '''
    codename_dict = {'debian_stretch': 'stretch',
                     'debian_buster': 'buster',
                     'ubuntu_bionic': 'bionic',
                     'ubuntu_xenial': 'xenial',
                     'ubuntu_trusty': 'trusty',
                     'fedora_28+': None,
                     'redhat_7+': None}

    for distro_string in codename_dict:
        with distro.LinuxDistribution(distro_string):
            assert (get_distribution_codename() == codename_dict[distro_string])

# Generated at 2022-06-12 23:44:27.029467
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Get the test case for get_distribution_codename function
    '''
    def get_testcase_distribution_codename(major_version, version_id, version_codename, ubuntu_codename, lsb_release_codename, expected_codename):
        '''
        Get the test case for get_distribution_codename function
        :param major_version: major version
        :param version_id: version id
        :param version_codename: version codename
        :param ubuntu_codename: ubuntu codename
        :param lsb_release_codename: lsb release codename
        :param expected_codename: codename after running get_distribution_codename
        '''

# Generated at 2022-06-12 23:44:38.931880
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Parent:
        distribution = None
        platform = 'ABC'

    class Linux(Parent):
        distribution = "Linux"
        platform = "Linux"

    class OtherLinux(Parent):
        distribution = 'OtherLinux'
        platform = 'Linux'

    assert get_platform_subclass(Parent) is Parent
    assert get_platform_subclass(Linux) is Linux
    assert get_platform_subclass(OtherLinux) is OtherLinux

    class Linux1(Parent):
        distribution = "Linux"
        platform = "ABC"

    class OtherLinux1(Parent):
        distribution = 'OtherLinux'
        platform = 'ABC'

    class Linux2(Linux1):
        distribution = "Linux"

    assert get_platform_subclass(Linux1) is Linux1
    assert get_platform_subclass(OtherLinux1) is OtherLinux

# Generated at 2022-06-12 23:45:01.522975
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'f29'

# pylint: disable=W0613

# Generated at 2022-06-12 23:45:10.060488
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test for function get_platform_subclass
    '''
    # import needed for testing
    import ansible.module_utils.facts.system.distribution
    from ansible.module_utils.facts.system import distribution

    # test for generic platform subclass
    generic_subclass = get_platform_subclass(distribution.Distribution)
    assert generic_subclass == distribution.GenericDistribution, 'Expected GenericDistribution for generic subclass'

    # test for linux platform subclass
    class DummyLinuxDistribution(distribution.LinuxDistribution):
        distribution = 'DummyLinuxDistribution'

    linux_subclass = get_platform_subclass(distribution.LinuxDistribution)
    assert linux_subclass == DummyLinuxDistribution, 'Expected DummyLinuxDistribution for linux subclass'

    # test for linux platform subclass with

# Generated at 2022-06-12 23:45:10.852438
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'xenial'

# Generated at 2022-06-12 23:45:18.477275
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Create some platform specific classes to test with
    class Base:
        pass

    class Posix(Base):
        platform = 'Posix'
    class Linux(Posix):
        platform = 'Linux'
    class Debian(Linux):
        distribution = 'Debian'
    class Raspbian(Debian):
        distribution = 'Raspbian'
    class Redhat(Linux):
        distribution = 'Redhat'
    class CentOS(Redhat):
        distribution = 'CentOS'
    class Arch(Linux):
        distribution = 'Arch'

    class Darwin(Posix):
        platform = 'Darwin'

    class NonPlatformBase:
        pass

    class NonPlatform(NonPlatformBase):
        pass

    def set_platform(platform, distribution):
        old_platform = platform.system
        old_distro = distro.id

# Generated at 2022-06-12 23:45:29.362593
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform

    from ansible.module_utils.common._collections_compat import UserDict

    class BaseClass:
        platform = 'darwin'

        def __init__(self, a, b):
            pass

    class MacClass(BaseClass):
        platform = 'darwin'

    class LinuxClass(BaseClass):
        distribution = 'Ubuntu'
        platform = 'Linux'

    class OtherLinuxClass(BaseClass):
        distribution = 'OtherLinux'
        platform = 'Linux'

    class OtherDistroClass(BaseClass):
        distribution = 'Redhat'
        platform = 'Linux'

    class FallbackClass(BaseClass):
        pass

    # On Linux, returns the Linux-specific class if the distribution
    # matches, the default otherwise
    platform.system = lambda: 'Linux'
    get_distribution

# Generated at 2022-06-12 23:45:30.935824
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Placeholder for future unit tests of function get_platform_subclass
    '''
    pass

# Generated at 2022-06-12 23:45:39.343218
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # pylint: disable=R0903
    class super_class(object):
        pass

    class linux_sub_class(super_class):
        pass

    linux_sub_class.platform = 'Linux'
    linux_sub_class.distribution = None

    class centos_sub_class(super_class):
        pass

    centos_sub_class.platform = 'Linux'
    centos_sub_class.distribution = 'Redhat'

    assert centos_sub_class == get_platform_subclass(super_class)
    assert linux_sub_class == get_platform_subclass(super_class)

# Generated at 2022-06-12 23:45:45.364106
# Unit test for function get_platform_subclass

# Generated at 2022-06-12 23:45:54.752019
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class SuperClass(object):
        pass

    class AnsibleModule(SuperClass):
        pass

    class Platform(AnsibleModule):
        platform = 'Linux'

    class PlatformSub1(Platform):
        distribution = 'Freedombox'

    class PlatformSub2(Platform):
        distribution = None

    class PlatformSub3(Platform):
        distribution = 'Raspbian'

    class PlatformSub4(Platform):
        distribution = 'Debian'

    class PlatformSub5(Platform):
        distribution = 'Ubuntu'
        codename = 'trusty'

    class PlatformSub6(Platform):
        distribution = 'Ubuntu'
        codename = 'xenial'

    class PlatformSub7(Platform):
        distribution = 'Ubuntu'
        codename = None



# Generated at 2022-06-12 23:46:01.452378
# Unit test for function get_distribution
def test_get_distribution():

    assert get_distribution() == u'Amazon'
    assert get_distribution() == u'Redhat'
    assert get_distribution() == u'Redhat'
    assert get_distribution() == u'Ubuntu'
    assert get_distribution() == u'Ubuntu'
    assert get_distribution() == u'Suse'
    assert get_distribution() == u'OtherLinux'

# Generated at 2022-06-12 23:46:55.843491
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    from ansible.module_utils import basic
    from ansible.module_utils.common._utils import update_module_args
    import pytest
    import json
    import os

    distro_data = {
        # Old and new distro.id's
        'ubuntu': ('Ubuntu', 'xenial'),
        'debian': ('Debian', 'stretch'),
        'fedora': ('Fedora', None),
        'centos': ('Centos', '7'),
        'redhat': ('RedHat', '7'),
        'amzn': ('Amazon', None),
    }


# Generated at 2022-06-12 23:47:06.450756
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Create a base class and two subclasses, one for Linux and one for FreeBSD

    class Base:
        platform = 'Generic'

    class Linux(Base):
        platform = 'Linux'
        distribution = None

    class FreeBSD(Base):
        platform = 'FreeBSD'
        distribution = None

    class RedhatLinux(Base):
        platform = 'Linux'
        distribution = 'Redhat'

    class CentOSLinux(Base):
        platform = 'Linux'
        distribution = 'CentOS'

    class AmznLinux(Base):
        platform = 'Linux'
        distribution = 'Amzn'

    # On Linux we expect to find the Linux subclass, since Linux is more specific than Generic
    assert get_platform_subclass(Base) == Linux
    assert get_platform_subclass(Linux) == Linux

    # On FreeBSD we expect to find the FreeBSD

# Generated at 2022-06-12 23:47:13.166493
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # class hierarchy is as follows
    # A
    # |- B
    # |- C (distribution Redhat)
    # |- D (platform Linux)
    # |- E (platform Linux, distribution Redhat)
    dist = get_distribution()
    _plat = platform

    class A(object):
        platform = 'Linux'
        distribution = dist

        def __init__(self):
            self.name = 'A'

    class B(A):
        def __init__(self):
            self.name = 'B'

    class C(A):
        distribution = 'Redhat'

        def __init__(self):
            self.name = 'C'

    class D(A):
        platform = 'Darwin'

        def __init__(self):
            self.name = 'D'

   

# Generated at 2022-06-12 23:47:23.576595
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class Base(object):
        platform = 'Base'
        distribution = None

    class Derived(Base):
        platform = 'Linux'
        distribution = None

    class DerivedDistro(Derived):
        distribution = 'CentOS'

    # At the base class level, get_platform_subclass() should return
    # the base class itself
    assert get_platform_subclass(Base) == Base

    # Nothing is matched.  get_platform_subclass should return the
    # original class
    assert get_platform_subclass(Derived) == Derived

    # Derived is matched, get_platform_subclass should return the
    # derived class
    assert get_platform_subclass(DerivedDistro) == DerivedDistro

    # When given a class for a different platform, get_platform_subclass()
    # should

# Generated at 2022-06-12 23:47:29.350747
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert 'bionic' == get_distribution_codename()
    assert 'xenial' == get_distribution_codename()
    assert 'jessie' == get_distribution_codename()
    assert 'stretch' == get_distribution_codename()

    #assert 'cosmic' == get_distribution_codename()
    #assert 'bionic' == get_distribution_codename()

# Generated at 2022-06-12 23:47:31.354375
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Check the return value of get_distribution
    '''
    distro = get_distribution()
    assert distro



# Generated at 2022-06-12 23:47:39.940189
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit test for function get_platform_subclass
    '''
    class Base(object):
        pass

    class Foo(Base):
        platform = 'foo'
        distribution = None

    class FooLinux(Base):
        platform = 'foo'
        distribution = 'Linux'

    class FooRedhat(Base):
        platform = 'foo'
        distribution = 'Redhat'

    class Bar(Base):
        platform = 'bar'
        distribution = None

    # Subclass exists for this platform
    def _test_subclass_exists(mock_platform, mock_distribution):
        mocked_this_platform = platform.system
        platform.system = lambda: mock_platform
        mocked_get_distribution = get_distribution
        get_distribution = lambda: mock_distribution

        result = get_platform

# Generated at 2022-06-12 23:47:41.825112
# Unit test for function get_distribution
def test_get_distribution():

    assert get_distribution() == 'Amzn'
    assert get_distribution_version() == '2'



# Generated at 2022-06-12 23:47:48.876562
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    from ansible.module_utils._text import to_text
    osx_codename = get_distribution_codename()
    assert osx_codename is None

    ubuntu_codename = get_distribution_codename()
    assert ubuntu_codename is not None
    assert to_text(ubuntu_codename) == 'xenial'

    centos_codename = get_distribution_codename()
    assert centos_codename is None

    freebsd_codename = get_distribution_codename()
    assert freebsd_codename is None

    opensuse_codename = get_distribution_codename()
    assert opensuse_codename is None

    redhat_codename = get_distribution_codename()
    assert redhat_codename is None

# Generated at 2022-06-12 23:48:00.416370
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test function to see if the get_distribution function
    returns the expected values for each platform
    '''
    assert get_distribution() == 'Redhat'
    assert get_distribution() == 'Debian'
    assert get_distribution() == 'Freebsd'
    assert get_distribution() == 'Darwin'
    assert get_distribution() == 'Sunos'
    assert get_distribution() == 'Aix'
    assert get_distribution() == 'Hpux'
    assert get_distribution() == 'Netbsd'
    assert get_distribution() == 'Openbsd'
    assert get_distribution() == 'Openvms'
    assert get_distribution() == 'Openvms'
    assert get_distribution() == 'OtherLinux'
    assert get_distribution()
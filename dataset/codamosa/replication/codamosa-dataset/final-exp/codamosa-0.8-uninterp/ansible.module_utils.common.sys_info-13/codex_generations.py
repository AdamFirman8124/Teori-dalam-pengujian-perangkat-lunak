

# Generated at 2022-06-12 23:38:25.305829
# Unit test for function get_distribution

# Generated at 2022-06-12 23:38:31.385501
# Unit test for function get_distribution_version
def test_get_distribution_version():
    _set_distro_version_and_variant('10.2')
    assert get_distribution_version() == u'10.2'
    assert get_distribution_version() == distro.version()
    _set_distro_version_and_variant('10.2.1')
    assert get_distribution_version() == u'10.2.1'
    assert get_distribution_version() == distro.version()
    _set_distro_version_and_variant('10.2.1', variant='redhat')
    assert get_distribution_version() == u'10.2.1'
    assert get_distribution_version() == distro.version()


# Generated at 2022-06-12 23:38:42.424999
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import unittest

    class Base:
        platform = 'Linux'

    class Redhat(Base):
        distribution = 'Redhat'

    class Debian(Base):
        distribution = 'Debian'

    class Redhat5(Redhat):
        version = 5

    class Redhat6(Redhat):
        version = 6

    class Debian7(Debian):
        version = 7

    class Debian8(Debian):
        version = 8

    class MyBaseModule:
        pass

    class MyRedhatModule(MyBaseModule, Redhat):
        pass

    class MyDebianModule(MyBaseModule, Debian):
        pass

    class MyRedhat6Module(MyBaseModule, Redhat6):
        pass

    class MyDebian7Module(MyBaseModule, Debian7):
        pass


# Generated at 2022-06-12 23:38:52.396441
# Unit test for function get_distribution
def test_get_distribution():
    distributions = [
        'Redhat',
        'Centos',
        'Amazon',
        'Fedora',
        'Debian',
        'Ubuntu',
        'Darwin',
        'Openbsd',
        'Suse',
        'Freebsd',
        'Netbsd',
        'Slackware',
        'Alpine',
        'Arch',
        'Gentoo',
        'Solaris',
        'Openindiana',
        'OmniOS'
    ]

    for distribution in distributions:
        # patch the distro.id() call to return the distribution name
        import ansible.module_utils.facts.system.distro
        ansible_distro = ansible.module_utils.facts.system.distro

# Generated at 2022-06-12 23:38:54.859091
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test the function get_distribution_codename
    '''
    codename = get_distribution_codename()
    print(codename)

# Generated at 2022-06-12 23:38:55.866228
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == "bionic"


# Generated at 2022-06-12 23:38:57.890994
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Alpine'



# Generated at 2022-06-12 23:39:04.440303
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # CentOS Linux release 7.5.1804 (Core)
    assert get_distribution_codename() is None
    # Ubuntu 16.04.5 LTS
    assert get_distribution_codename() == u'xenial'
    # Fedora release 29 (Twenty Nine)
    assert get_distribution_codename() is None
    # Debian GNU/Linux 9 (stretch)
    assert get_distribution_codename() == u'stretch'

# Generated at 2022-06-12 23:39:12.388974
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Return the class object implementing the functionality of a class
    on the platform its running on.

    :rtype: Class object or None
    :returns: One of the following:
        * ``PreserveCaseOnLinux`` on a Redhat Linux platform
        * ``PreserveCaseOnOtherLinux`` on any other Linux platform
        * ``PreserveCaseOnDarwin`` on a Darwin platform
        * ``PreserveCase`` on any other platform
        * ``None`` if no platform information is available
    '''
    class PreserveCase:
        '''
        Implementation of ``PreserveCase`` on any platform
        '''
        platform = None

    class PreserveCaseOnLinux(PreserveCase):
        '''
        Implementation of ``PreserveCase`` on Linux
        '''
        platform = u'Linux'


# Generated at 2022-06-12 23:39:16.610362
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Tests for the get_distribution_version() function
    '''
    from ansible.module_utils.common._utils import get_distribution_version
    from ansible.module_utils.linux_distribution import get_distribution_version as linux_get_distribution_version

    # This can't be tested on other OSes like OSX because we don't have a version() function there
    assert linux_get_distribution_version() == get_distribution_version()

# Generated at 2022-06-12 23:39:38.731279
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    :rtype: List[str]
    :return: List of items not testing properly
    :raises AssertionError: If a test fails
    '''

    class Base:
        platform = None
        distribution = None

    class A(Base):
        platform = 'Linux'
        distribution = 'Redhat'

    class B(Base):
        platform = 'Linux'
        distribution = 'Redhat'

    class C(Base):
        platform = platform.system()
        distribution = get_distribution()

    class D(C):
        platform = platform.system()
        distribution = get_distribution()

    class E(Base):
        platform = platform.system()
        distribution = get_distribution()

    class F(Base):
        platform = platform.system()
        distribution = get_distribution()

   

# Generated at 2022-06-12 23:39:51.449758
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # class PlatformOne is a superclass, PlatformTwo uses its subclass
    class PlatformBase:
        platform = 'Base'
        distribution = None

    class PlatformOne(PlatformBase):
        distribution = 'One'

    class PlatformTwo(PlatformBase):
        distribution = 'Two'

    class PlatformGeneric(PlatformBase):
        distribution = None

    class TestClass:
        platform = 'Base'
        distribution = None

    subclass = get_platform_subclass(TestClass)

    assert subclass is TestClass

    # If a subclass is defined for the current platform, use it
    TestClass.platform = 'Base'
    TestClass.distribution = 'One'
    subclass = get_platform_subclass(TestClass)

    assert subclass is PlatformOne

    TestClass.platform = 'Base'
    TestClass.distribution = 'Two'
    subclass

# Generated at 2022-06-12 23:39:59.118160
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Class1:
        distribution = None
        platform = 'Linux'

    class Class2(Class1):
        distribution = 'Fedora'

    class Class3(Class1):
        distribution = 'Redhat'

    subclass = get_platform_subclass(Class1)
    assert Class1 == subclass

    subclass = get_platform_subclass(Class2)
    assert Class2 == subclass

    subclass = get_platform_subclass(Class3)
    assert Class3 == subclass

# Generated at 2022-06-12 23:40:07.001029
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    This function is called only when executing the module directly.
    Unit test for function get_distribution_codename
    '''
    test_distro = u'debian'
    test_codename = u'buster'
    test_version = u'10'

    assert distro.codename(pretty=True) == test_codename
    assert get_distribution_codename() == test_codename
    assert distro.id() == test_distro
    assert get_distribution() == test_distro.capitalize()
    assert distro.version(best=True) == test_version
    assert get_distribution_version() == test_version

if __name__ == '__main__':
    test_get_distribution_codename()

# Generated at 2022-06-12 23:40:19.034856
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils._text import to_bytes

    class TestClass():
        # TestClass behaves like the User class in the test case
        # init method will always raise NotImplementedError
        def __init__(self, *args, **kwargs):
            raise NotImplementedError("__init__ not implemented")

    # Test class not found case
    assert TestClass == get_platform_subclass(TestClass)

    class TestClassSubclass1(TestClass):
        platform = platform.system()  # Platform is linux
        distribution = None  # Distribution is linux

    # Test platform not null, distribution is null case
    assert TestClassSubclass1 == get_platform_subclass(TestClass)

    class TestClassSubclass2(TestClassSubclass1):
        pass

    # Test multiple platform subclass case, the platform subclass


# Generated at 2022-06-12 23:40:26.911274
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    # We test the function with an imaginary class 'testModule'
    class testModule:
        platform = 'Linux'
        distribution = None

        def get_distribution(self):
            return get_distribution()

    class testModuleCentosSubclass(testModule):
        platform = 'Linux'
        distribution = 'Centos'

    class testModuleOtherLinuxSubclass(testModule):
        platform = 'Linux'
        distribution = 'OtherLinux'

    class testModuleWindowsSubclass(testModule):
        platform = 'Windows'
        distribution = None

    class testModuleWindows10Subclass(testModuleWindowsSubclass):
        platform = 'Windows'
        distribution = 'Windows10'

    class testModuleSolarisSubclass(testModule):
        platform = 'solaris'
        distribution = None


# Generated at 2022-06-12 23:40:33.376000
# Unit test for function get_distribution
def test_get_distribution():
    expected = {
        'Linux': get_distribution()
    }
    if platform.system() == 'Linux':
        expected['Linux'] = get_distribution().replace('Other', 'OEL').replace('Redhat', 'RHEL')
        if expected['Linux'] == 'Amazon':
            expected['Linux'] = 'AMZ'

    assert expected[platform.system()] == get_distribution()

# Generated at 2022-06-12 23:40:39.014959
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import json
    from ansible.module_utils._text import to_native

    distribution_codename = get_distribution_codename()

    print("json_encoded result: %s" % json.dumps(to_native(distribution_codename), indent=4, sort_keys=True))

if __name__ == '__main__':
    test_get_distribution_codename()

# Generated at 2022-06-12 23:40:49.867272
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        pass

    class ANo:
        platform = "Darwin"

    class AYes:
        platform = "Darwin"

    class BYes(A):
        distribution = "Ubuntu"
        platform = "Linux"

    class BYesNo(A):
        distribution = "Ubuntu"

    class BNo(A):
        distribution = "Ubuntu"
        platform = "Linux"

    class AYesBYes(AYes, BYes):
        pass

    class AYesBYesNo(AYes, BYesNo):
        pass

    class AYesBNo(AYes, BNo):
        pass

    class ANoBYes(ANo, BYes):
        pass

    class AYesNoBYes(AYesNo, BYes):
        pass


# Generated at 2022-06-12 23:41:00.336604
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test function to determine the distribution
    '''

    # Create a list of tuples with all of the possible distribution
    real_distros = [
        ('Amazon', 'amzn'),
        ('Archlinux', 'arch'),
        ('CentOS', 'centos'),
        ('RedHat', 'rhel'),
        ('Debian', 'debian'),
        ('Fedora', 'fedora'),
        ('Gentoo', 'gentoo'),
        ('Mageia', 'mageia'),
        ('Mandriva', 'mandriva'),
        ('Mint', 'mint'),
        ('SuSE', 'suse'),
        ('Ubuntu', 'ubuntu'),
    ]

    for real_distro, distro_name in real_distros:
        this_distro = distro.info(distro_name)

        # Test

# Generated at 2022-06-12 23:41:35.247854
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class PlatformIndependentClass:
        platform = ''
        distribution = None

    class PlatformDependentClass(PlatformIndependentClass):
        platform = platform.system()
        distribution = None

    class DistributionDependentClass(PlatformIndependentClass):
        platform = ''
        distribution = get_distribution()

    class AllDependentClass(PlatformIndependentClass):
        platform = platform.system()
        distribution = get_distribution()

    assert get_platform_subclass(PlatformIndependentClass) == PlatformIndependentClass
    assert get_platform_subclass(PlatformDependentClass) == PlatformDependentClass
    assert get_platform_subclass(DistributionDependentClass) == DistributionDependentClass
    assert get_platform_subclass(AllDependentClass) == AllDependentClass

    class OtherPlatformDependentClass(PlatformIndependentClass):
        platform = 'OtherPlatform'
        distribution

# Generated at 2022-06-12 23:41:43.870304
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''Test the get_distribution_codename for a few platforms'''
    distro_codename_dict = dict(
        Debian='buster',
        RedHat='',
        Fedora='28',
        Suse='',
        Alpine='',
        OracleLinux='',
        Amazon='',
        Ubuntu='xenial',
        CumulusLinux='',
        Darwin='',
        OpenWrt='',
    )
    distro_id_list = list(distro_codename_dict.keys())
    for distro_id in distro_id_list:
        distro.id = lambda: distro_id
        distro.codename = lambda: distro_codename_dict[distro_id]
        distro.lsb_release_info = lambda: {}

# Generated at 2022-06-12 23:41:56.511409
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    # These attributes will be used below to create our two subclasses
    class_attributes = {
        'distribution': None,
        'version': None,
        'platform': None
    }

    # Create a generic subclass
    class GenericSubclass:
        pass

    for key in class_attributes:
        setattr(GenericSubclass, key, class_attributes[key])

    # Create a subclass to match our system
    class SpecificSubclass:
        pass

    for key in class_attributes:
        setattr(SpecificSubclass, key, class_attributes[key])

    SpecificSubclass.platform = platform.system()
    SpecificSubclass.distribution = get_distribution()

    # Create a generic class for testing
    class GenericClass:
        pass

    # Add the subclasses to the generic class

# Generated at 2022-06-12 23:42:04.541975
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform

    class SuperClass:
        pass

    class LinuxSubClass(SuperClass):
        platform = 'Linux'

    class BSDSubClass(SuperClass):
        platform = 'Darwin'

    class RedhatSubClass(LinuxSubClass):
        distribution = 'Redhat'

    class AmazonSubClass(LinuxSubClass):
        distribution = 'Amazon'

    class OtherLinuxSubClass(LinuxSubClass):
        distribution = 'OtherLinux'

    class Redhat7SubClass(RedhatSubClass):
        distribution = 'Redhat'
        version = '7'

    class Redhat6SubClass(RedhatSubClass):
        distribution = 'Redhat'
        version = '6'

    class Redhat5SubClass(RedhatSubClass):
        distribution = 'Redhat'
        version = '5'


# Generated at 2022-06-12 23:42:15.340737
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    this_platform = 'Linux'
    distribution = 'Debian'

    class debian_class():
        distribution = distribution
        platform = this_platform

        def get_info(self):
            return "debian class"

    class linux_class():
        platform = this_platform

        def get_info(self):
            return "linux class"

    class base_class():
        def get_info(self):
            return "base class"

    # Test 1: Get the most specific subclass
    assert get_platform_subclass(base_class)().get_info() == "debian class"

    # Test 2: Get the subclass matching platform
    this_platform = 'Windows'
    distribution = 'Debian'
    assert get_platform_subclass(base_class)().get_info() == "linux class"

    # Test 3: Get the

# Generated at 2022-06-12 23:42:24.195079
# Unit test for function get_distribution_version

# Generated at 2022-06-12 23:42:28.823582
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() in ('Suse', 'Redhat', 'Oracle', 'Debian', 'Ubuntu', 'Linuxmint', 'Centos', 'Fedora', 'Suselinux', 'Mandrake', 'Mageia', 'Slackware', 'Virtualbox', 'Kubuntu', 'Arch', 'Raspbian', 'Xenserver', 'Solaris', 'Windows', 'Amazon')
    # Test the different name for Amazon Linux
    # Test the default for a Linux distro with no name
    assert get_distribution() not in ('Amzn', 'OtherLinux')


# Generated at 2022-06-12 23:42:38.941190
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    codename_redhat = ('7.5', 'Maipo', 'el')
    codename_centos = ('7.5', 'Core', 'centos')
    codename_debian = ('10', 'buster', 'debian')
    codename_ubuntu = ('18.04', 'bionic', 'ubuntu')

    redhat_result = get_distribution_codename()
    centos_result = get_distribution_codename()
    debian_result = get_distribution_codename()
    ubuntu_result = get_distribution_codename()

    assert (redhat_result == codename_redhat[0])
    assert (centos_result == codename_centos[0])
    assert (debian_result == codename_debian[0])
    assert (ubuntu_result == codename_ubuntu[0])

# Generated at 2022-06-12 23:42:47.646869
# Unit test for function get_distribution
def test_get_distribution():
    # CentOS7.x
    assert (get_distribution() == 'Redhat')
    assert (distro.id().capitalize() == 'Centos')
    # Ubuntu 14.04
    assert (get_distribution() == 'Ubuntu')
    assert (distro.id().capitalize() == 'Ubuntu')
    # Debian 8
    assert (get_distribution() == 'Debian')
    assert (distro.id().capitalize() == 'Debian')
    # Fedora 28
    assert (get_distribution() == 'Fedora')
    assert (distro.id().capitalize() == 'Fedora')


# Generated at 2022-06-12 23:42:48.612606
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Ubuntu'

# Generated at 2022-06-12 23:43:39.830699
# Unit test for function get_distribution
def test_get_distribution():
    """Returns the distribution name for the machine running the unit test."""
    return get_distribution()

# Generated at 2022-06-12 23:43:49.798782
# Unit test for function get_distribution_version
def test_get_distribution_version():
    import sys
    import pytest
    from ansible.module_utils.facts import ansible_facts
    from ansible_collections.ansible.distro.tests.test_collections_ansible_distro.fixtures.facts.distro_facts import distro_facts

    pytest.importorskip('distro')

    # Test each fixture from distro_facts
    for name, fact_set in distro_facts.items():
        # Skip fact sets that are for the wrong platform
        if platform.system() != fact_set['ansible_facts']['ansible_system']:
            continue
        # Skip fact sets that don't contain the ansible_distribution_version fact
        if 'ansible_distribution_version' not in fact_set['ansible_facts']:
            continue
        # Skip fact sets that

# Generated at 2022-06-12 23:43:54.913217
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Make sure that platform subclasses are correctly identified by
    # get_platform_subclass in get_platform_subclass function

    class Base:
        platform = None
        distribution = None

    class Test1(Base):
        platform = 'Linux'
        distribution = 'Fedora'

    class Test2(Base):
        platform = 'Linux'
        distribution = 'Debian'

    class Test3(Base):
        platform = 'BSD'
        distribution = None

    class Test4(Base):
        platform = 'BSD'
        distribution = 'FreeBSD'

    class Test5(Base):
        platform = 'Linux'
        distribution = None

    class Test6(Base):
        platform = None
        distribution = None

    # Test 1
    plat = get_platform_subclass(Base)
    assert plat == Base

    # Test

# Generated at 2022-06-12 23:44:06.743389
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    distribution = get_distribution()
    codename = get_distribution_codename()

    if distribution == 'Amazon':
        assert codename == 'amzn'
    elif distribution == 'Debian':
        assert codename == 'stretch'
    elif distribution == 'Fedora':
        assert codename == 'rawhide'
    elif distribution == 'Freebsd':
        assert codename is None
    elif distribution == 'Openbsd':
        assert codename is None
    elif distribution == 'Oracle':
        assert codename == 'el7'
    elif distribution == 'Redhat':
        assert codename == '7.6'
    elif distribution == 'Suse':
        assert codename == '15'
    elif distribution == 'Ubuntu':
        assert codename == 'xenial'

# Generated at 2022-06-12 23:44:17.310956
# Unit test for function get_distribution_codename

# Generated at 2022-06-12 23:44:28.224863
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import unittest

    class SuperClass(object):
        platform = 'GenericPlatform'
        distribution = None

    class LinuxClass(SuperClass):
        platform = 'Linux'
        distribution = None

    class RedhatClass(LinuxClass):
        distribution = 'Redhat'

    class GenericLinuxClass(LinuxClass):
        distribution = 'OtherLinux'

    class GenericClass(SuperClass):
        platform = 'GenericPlatform'
        distribution = None

    class WindowsClass(SuperClass):
        platform = 'Windows'
        distribution = None

    class NonExistentClass(SuperClass):
        platform = 'NonExistentPlatform'
        distribution = None

    this_platform = platform.system()
    distribution = get_distribution()


# Generated at 2022-06-12 23:44:39.502599
# Unit test for function get_distribution
def test_get_distribution():
    # This function is called exactly one time by the platform module init.
    # We override this function to test the get_distribution() function.
    real_get_distribution = platform.linux_distribution

    distributions = {
        'redhat': ('RedHat', '7.1', 'Final'),
        'centos': ('CentOS', '7.1.1503', 'Core'),
        'fedora': ('Fedora', '25', 'Twenty Five'),
        'debian': ('Debian', '8.3', ''),
        'ubuntu': ('Ubuntu', '16.04', 'xenial'),
    }
    for distribution, (id, version, codename) in distributions.items():
        assert get_distribution() == get_distribution_version() == get_distribution_codename() is None


# Generated at 2022-06-12 23:44:42.013902
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == get_distribution_version() == \
        get_distribution_codename() == None

# Generated at 2022-06-12 23:44:49.902551
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Function used to test get_distribution_version() on a variety of platforms
    '''
    # Test versions from https://wiki.debian.org/DebianReleases

# Generated at 2022-06-12 23:44:59.930314
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import ansible_test

    class Base:
        pass

    class BSD(Base):
        distribution = None
        platform = 'FreeBSD'

    class Linux(Base):
        distribution = None
        platform = 'Linux'

    class RHEL(Linux):
        distribution = 'RedHat'

    class FreeBSD(BSD):
        distribution = 'FreeBSD'

    class Solaris(Base):
        distribution = None
        platform = 'SunOS'

    class OpenSolaris(Solaris):
        distribution = 'OpenSolaris'

    class AIX(Base):
        distribution = None
        platform = 'AIX'

    class AIX7(AIX):
        distribution = '7.1'

    # get_platform_subclass should return closest match for class
    # defined for a given platform

# Generated at 2022-06-12 23:45:53.642635
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test the get_distribution() function.

    The get_distribution() function attempts to determine the name of the
    distribution the code is running on.  However, the module it uses to
    determine this has some bugs so this test is to verify that the
    get_distribution() function does the right thing even if the underlying
    code doesn't.

    :raises AssertionError: If the test fails
    '''
    assert get_distribution() == 'Redhat'
    assert get_distribution() == 'Redhat'


# Generated at 2022-06-12 23:46:05.258456
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform

    class Test_1:
        platform = platform.system()
        distriubotn = get_distribution()

    class Test_2:
        platform = platform.system()
        distriubotn = "foo"

    class Test_3:
        pass

    class Test_4:
        platform = platform.system()
        distriubotn = None

    class Test_5:
        platform = "foo"

    class Test_6:
        platform = "foo"
        distribution = "bar"

    assert get_platform_subclass(Test_1) is Test_1
    assert get_platform_subclass(Test_2) is Test_2
    assert get_platform_subclass(Test_3) is Test_3
    assert get_platform_subclass(Test_4) is Test_4


# Generated at 2022-06-12 23:46:15.228479
# Unit test for function get_distribution
def test_get_distribution():
    plat = platform.system()
    if plat == 'Linux':
        if distro.id() == 'centos':
            assert get_distribution() == 'Centos'
        elif distro.id() == 'fedora':
            assert get_distribution() == 'Fedora'
        elif distro.id() == 'ubuntu':
            assert get_distribution() == 'Ubuntu'
        elif distro.id() == 'debian':
            assert get_distribution() == 'Debian'
        elif distro.id() == 'redhat':
            assert get_distribution() == 'Redhat'
        elif distro.id() == 'arch':
            assert get_distribution() == 'Arch'

# Generated at 2022-06-12 23:46:18.500607
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test to get the code name for this distribution
    '''
    codename = None
    codename = get_distribution_codename()
    assert codename



# Generated at 2022-06-12 23:46:28.869716
# Unit test for function get_distribution_codename

# Generated at 2022-06-12 23:46:37.877957
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        platform = None
        distribution = None

    class Linux(Base):
        platform = 'Linux'
        distribution = 'Debian'

    class BSD(Base):
        platform = 'FreeBSD'
        distribution = None

    assert get_platform_subclass(Base) is Base
    assert get_platform_subclass(Linux) is Linux
    assert get_platform_subclass(BSD) is BSD

    class FreeBSD(Base):
        platform = 'FreeBSD'
        distribution = None

    assert get_platform_subclass(FreeBSD) is FreeBSD
    class NetBSD(Base):
        platform = 'NetBSD'
        distribution = None

    assert get_platform_subclass(NetBSD) is NetBSD

# Generated at 2022-06-12 23:46:45.775813
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # This is the base class of all classes that subclass BaseUser.
    class BaseUser:
        platform = 'Generic'
        distribution = None

    # This is an example of a platform specific subclass.
    class LinuxUser(BaseUser):
        platform = 'Linux'

    # This is an example of a distribution specific subclass.
    class LinuxDebianUser(LinuxUser):
        distribution = 'Debian'

    # This is an example of a distribution specific subclass.
    class LinuxOtherLinuxUser(LinuxUser):
        distribution = 'OtherLinux'

    # This is an example of a distribution/version specific subclass.
    class LinuxDebian8User(LinuxDebianUser):
        version = '8'

    # This is an example of a distribution/version specific subclass.
    class LinuxDebian9User(LinuxDebianUser):
        version = '9'



# Generated at 2022-06-12 23:46:47.532727
# Unit test for function get_distribution
def test_get_distribution():
    distribution = get_distribution()
    assert distribution is not None

# Generated at 2022-06-12 23:46:51.771433
# Unit test for function get_distribution
def test_get_distribution():
    '''
    test_get_distribution method: test the get_distribution method

    :returns: None
    :rtype: None
    '''
    assert isinstance(get_distribution(), str)



# Generated at 2022-06-12 23:47:02.362214
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class ParentClass(object):
        pass

    class ChildClass(ParentClass):
        platform = 'Linux'
        distribution = 'Fedora'

    class ChildClass2(ParentClass):
        platform = 'Linux'
        distribution = 'Fedora'

    class LinuxParentClass(object):
        platform = 'Linux'

    class LinuxChildClass(LinuxParentClass):
        distribution = 'Fedora'

    class LinuxChildClass2(LinuxParentClass):
        distribution = 'Debian'

    class BSDChildClass(LinuxParentClass):
        platform = 'FreeBSD'

    def test_that_child_class_is_returned_if_match_distribution_and_platform():
        assert get_platform_subclass(ParentClass) == ChildClass

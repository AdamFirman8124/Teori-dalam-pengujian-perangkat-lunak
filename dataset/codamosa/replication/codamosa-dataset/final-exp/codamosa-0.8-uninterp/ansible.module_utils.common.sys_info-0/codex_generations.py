

# Generated at 2022-06-12 23:38:23.405642
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() is None
    assert get_distribution_codename('redhat') == 'Redhat'
    assert get_distribution_codename('redhat', '6.4') == 'Santiago'
    assert get_distribution_codename('redhat', '6.7') == 'Santiago'
    assert get_distribution_codename('redhat', '7.2') == 'Maipo'
    assert get_distribution_codename('redhat', '7.3') == 'Maipo'
    assert get_distribution_codename('centos', '6.4') == 'Santiago'
    assert get_distribution_codename('centos', '6.7') == 'Santiago'

# Generated at 2022-06-12 23:38:30.895925
# Unit test for function get_distribution
def test_get_distribution():
    assert(get_distribution() == 'Redhat')
    import platform
    _platform_system = platform.system
    _distro_id = distro.id


# Generated at 2022-06-12 23:38:41.937986
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test module for the get_platform_subclass function
    '''
    # This class has no sub classes, just test
    # that we get the right class back
    class TestNoSubClass:
        @classmethod
        def distribution(cls):
            return 'Fedora'

        @classmethod
        def platform(cls):
            return 'Linux'

    this_platform = platform.system()
    distribution = get_distribution()

    base_class = get_platform_subclass(TestNoSubClass)
    assert distribution == 'Fedora'
    assert this_platform == 'Linux'
    assert base_class.__name__ == 'TestNoSubClass'

    # Test class with a generic subclass

# Generated at 2022-06-12 23:38:52.126499
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''Unit test for the function get_distribution_version'''
    import random
    import string

    def random_string(string_length=6):
        '''Generate a random string of fixed length '''
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(string_length))

    # 1) All versions
    distro_versions = [
        distro.version(best=True),
        distro.version(best=False)
    ]

    # 2) Only major versions
    distro_versions.extend([
        '.'.join(distro.version(best=True).split('.')[0:1]),
        '.'.join(distro.version(best=True).split('.')[0:1])
    ])

    # 3)

# Generated at 2022-06-12 23:38:57.587149
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Redhat', "get_distribution() failed"
    assert get_distribution() == 'Amazon', "get_distribution() failed"
    assert get_distribution() == 'Debian', "get_distribution() failed"
    assert get_distribution() == 'Ubuntu', "get_distribution() failed"
    assert get_distribution() == 'OtherLinux', "get_distribution() failed"


# Generated at 2022-06-12 23:38:58.796010
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() == distro.version()



# Generated at 2022-06-12 23:39:09.234878
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class cls1(object):
        platform = 'Linux'
        distribution = 'Redhat'

    class cls2(cls1):
        distribution = 'Ubuntu'

    class cls3(cls1):
        pass

    class cls4(cls1):
        distribution = 'Redhat'
        distribution_version = '5.5'

    class cls5(cls1):
        distribution = 'CentOS'
        distribution_version = '5.5'

    class cls6(cls1):
        pass

    assert get_platform_subclass(cls1) == cls1
    assert get_platform_subclass(cls2) == cls2
    assert get_platform_subclass(cls3) == cls1

# Generated at 2022-06-12 23:39:18.517847
# Unit test for function get_distribution
def test_get_distribution():
    from ansible.module_utils.basic import AnsibleModule

    def test_distro(distro, expected):
        class Test:
            def __init__(self):
                self._distro = distro

            def distribution(self):
                return self._distro

        module = AnsibleModule({})
        module.distribution = lambda: distro
        distro_id = get_distribution()
        assert distro_id == expected, '%s != %s' % (distro_id, expected)

    # Test distro function

# Generated at 2022-06-12 23:39:28.844271
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    # class that doesn't have subclass
    class NoSubclass(object):
        platform = None
        distribution = None

    assert NoSubclass == get_platform_subclass(NoSubclass)

    # class that has no distribution subclass
    class NoDistributionSubclass(object):
        platform = "Linux"
        distribution = None
        def __init__(self):
            pass

    class NoDistributionSubclassAmazon(NoDistributionSubclass):
        distribution = "Amazon"
        def __init__(self):
            pass

    this_platform = platform.system()
    distribution = get_distribution()
    if distribution == "Amazon":
        assert NoDistributionSubclassAmazon == get_platform_subclass(NoDistributionSubclass)

# Generated at 2022-06-12 23:39:38.732333
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class Base:
        platform = None
        distribution = None

    class Linux(Base):
        platform = "Linux"

    class RedHat(Linux):
        distribution = "RedHat"

    class Debian(Linux):
        distribution = "Debian"

    class OtherLinux(Linux):
        distribution = "OtherLinux"

    class BSD(Base):
        platform = "BSD"

    # SubClass needs to be defined after BaseClass, but only for the purposes of this test.
    # If a subclass is defined after a superclass in the same file, python will execute the
    # subclass __init__ function first, so the subclass will always overwrite the superclass.

    assert Base == get_platform_subclass(Base)
    assert Base == get_platform_subclass(Base)

    assert Linux == get_platform_subclass(Linux)
    assert Linux

# Generated at 2022-06-12 23:39:54.521965
# Unit test for function get_distribution
def test_get_distribution():
    from ansible.module_utils.common._collections_compat import OrderedDict
    print("\nTest get_distribution using mock data")
    test_inputs = OrderedDict()
    test_inputs["Debian test"] = {
        "input": {
            "system": "Linux",
            "distribution": "debian",
            "version": "",
            "codename": "jessie"
        },
        "expected_result": "Debian"
    }
    test_inputs["Debian test, version present"] = {
        "input": {
            "system": "Linux",
            "distribution": "debian",
            "version": "8",
            "codename": "jessie"
        },
        "expected_result": "Debian"
    }
    test_input

# Generated at 2022-06-12 23:40:04.006245
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform

    class Base:
        def added():
            pass

    class BaseLinux:
        platform = 'Linux'
        distribution = None

    class BaseSuse(BaseLinux):
        distribution = 'Suse'

    class BaseUbuntu(BaseLinux):
        distribution = 'Ubuntu'

    class LinuxDistro():
        platform = 'Linux'
        distribution = 'OtherLinux'

    class OtherPlatform():
        platform = 'Other'
        distribution = None

    class Suse(LinuxDistro):
        def added():
            pass

    class Ubuntu(LinuxDistro):
        def added():
            pass

    class BSD(LinuxDistro):
        platform = 'FreeBSD'

    # Test matrix:
    #   platform  distribution     test     result
    #   Linux     Suse             Suse     Suse
    #   Linux

# Generated at 2022-06-12 23:40:16.803157
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    this_platform = platform.system()
    distribution = get_distribution()

    class cls:
        platform = this_platform
        distribution = distribution

    def get_all_subclasses(cls):
        return (
            cls,
            derived1,
            derived2,
        )

    class derived1(cls):
        platform = 'AIX'
        distribution = 'AIX'

    class derived2(cls):
        platform = this_platform
        distribution = 'AIX'

    # test that we got the correct platform
    is_correct_platform = (cls.__name__ == derived1.__name__)
    is_correct_platform = is_correct_platform or (cls.__name__ == derived2.__name__)

# Generated at 2022-06-12 23:40:22.064951
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # On the python 2.6.6 platform Travis 0.9.1 works with, this is the actual
    # output of distro.version() so we cannot make too many assumptions about
    # the output other than it will be useful for feeding into downstream
    # services
    if distro.version():
        assert isinstance(distro.version(), basestring)
    else:
        assert distro.version() == ''

# Generated at 2022-06-12 23:40:23.331195
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Amazon'



# Generated at 2022-06-12 23:40:24.570669
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # just run the function
    get_distribution_codename()

# Generated at 2022-06-12 23:40:30.592048
# Unit test for function get_distribution_codename

# Generated at 2022-06-12 23:40:32.899200
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'bionic', "With Ubuntu 18.04 LTS, the codename should be bionic"

# Generated at 2022-06-12 23:40:37.579694
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
  code_name = get_distribution_codename()
  if code_name:
    print("The codename is " + code_name)
  else:
    print("No codename is defined.")

if __name__ == '__main__':
  test_get_distribution_codename()

# Generated at 2022-06-12 23:40:38.901596
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Linux'

# Generated at 2022-06-12 23:40:52.368944
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    """
    This function is a unit test for the get_platform_subclass function.
    """

# Generated at 2022-06-12 23:41:02.282000
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
        Test all branches of the get_platform_subclass() function
    '''
    # pylint: disable=too-few-public-methods
    class Baseclass:
        '''
            Baseclass to test get_platform_subclass function
        '''
        platform = 'Linux'
        distribution = None

    class Subclass1(Baseclass):
        '''
            Subclass 1 of Baseclass to test get_platform_subclass function
        '''
        platform = 'Linux'
        distribution = None

    class Subclass2(Baseclass):
        '''
            Subclass 2 of Baseclass to test get_platform_subclass function
        '''
        platform = 'Linux'
        distribution = 'OtherLinux'


# Generated at 2022-06-12 23:41:11.337237
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Verify get_platform_subclass works as expected

    This function is used to unit test get_platform_subclass by:

    1. asserting the function returns a subclass for a given class
    2. asserting the function returns a subclass for a given class, platform, distribution
    3. asserting the function returns the same class if it doesn't have a subclass
    4. asserting the function returns the most specific subclass when it has both generic and specific subclasses
    '''
    from ansible.module_utils.facts import distribution
    from ansible.module_utils.facts.tests.test_distribution import get_distribution_test_subclasses

    # Run the unit tests on the Distribution class to make sure it works.
    # Instantiate the various test classes that represent the various
    # platforms
    import types

    test_subclasses = get_distribution_test

# Generated at 2022-06-12 23:41:18.718208
# Unit test for function get_distribution
def test_get_distribution():
    """
    Test case to validate the correct value of distribution is returned

    :rtype: NativeString
    :returns: Expected value of distribution
    """


# Generated at 2022-06-12 23:41:25.645665
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test function get_distribution
    '''

    ret = get_distribution()

    assert ret, 'Expected get_distribution() to return a string'
    assert ret == get_distribution(), 'Expected get_distribution() return to be identical'
    assert get_distribution() != get_distribution_version(), 'Expected get_distribution() != get_distribution_version()'


# Generated at 2022-06-12 23:41:35.982965
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    import sys

    class BaseClass(object):
        platform = sys.platform
        distribution = None

    class SubClassA(BaseClass):
        pass

    class SubClassB(BaseClass):
        distribution = 'Linux'

    class SubClassC(BaseClass):
        platform = 'darwin'
        distribution = 'Darwin'

    class SubClassD(BaseClass):
        platform = 'darwin'
        distribution = None

    if sys.platform == 'darwin':
        assert get_platform_subclass(BaseClass) == SubClassD
    elif platform.system() == 'Linux':
        assert get_platform_subclass(BaseClass) == SubClassB
    else:
        assert get_platform_subclass(BaseClass) == BaseClass

# Generated at 2022-06-12 23:41:44.279497
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    # A class that works on all Unix platforms
    class BaseUnix:
        platform = "Linux"    # Actually it works on any *nix
        distribution = None

    # A subclass that works on any Linux
    class Linux(BaseUnix):
        pass

    # A subclass that works on any Linux distro
    class AnyLinux(Linux):
        distribution = None

    # A subclass that works on a specific Linux distro
    class SpecificDistro(Linux):
        distribution = 'Redhat'

    # A subclass that works on any Linux distro except for a specific one
    class AnyLinuxExcept(Linux):
        distribution = '!Redhat'

    # A subclass that works on a specific Linux distro and version
    class SpecificLinuxVersion(Linux):
        distribution = 'Redhat'
        version = '6.9'

    # A class that works on any

# Generated at 2022-06-12 23:41:47.312565
# Unit test for function get_distribution_version
def test_get_distribution_version():

    distribution_version = get_distribution_version()
    assert distribution_version is None


# Generated at 2022-06-12 23:41:57.229418
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    This unit test demonstrates that the function get_distribution_codename
    will return the correct data for three different Linux distributions.
    '''
    assert get_distribution_codename() == u'xenial'

    with patch('ansible.module_utils.distro.os_release_info', return_value={'version_codename': 'stable'}):
        assert get_distribution_codename() == 'stable'

    with patch('ansible.module_utils.distro.id', return_value='redhat'):
        with patch('ansible.module_utils.distro.redhat_rel', return_value='8'):
            assert get_distribution_codename() == ''

# Generated at 2022-06-12 23:42:04.884444
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import unittest

    # create base class
    class Base_Program(object):
        platform = 'Linux'
        distribution = None

    # create program for all linux distros
    class Linux_Program(Base_Program):
        pass

    # create program for centos distro
    class CentOS_Program(Linux_Program):
        distribution = u'Centos'

    # create program for fedora distro
    class Fedora_Program(Linux_Program):
        distribution = u'Fedora'

    # create program for sles distro
    class SLES_Program(Linux_Program):
        distribution = u'SLES'

    # create program for FreeBSD
    class FreeBSD_Program(Linux_Program):
        distribution = None
        platform = 'FreeBSD'


# Generated at 2022-06-12 23:42:11.864632
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    for p in (
        'centos',
        'debian',
        'rhel',
        'fedora',
        'ubuntu',
        'mandrake',
        'mandrakelinux',
        'mageia',
        'meego',
        'suse',
        'opensuse',
    ):
        assert get_distribution_codename() != None

# Generated at 2022-06-12 23:42:13.345402
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == platform.linux_distribution()[0].capitalize()

# Generated at 2022-06-12 23:42:20.887429
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Create a base class for testing
    class Base(object):
        platform = None
        distribution = None

    # Add a few subclasses to test with
    class Linux(Base):
        platform = 'Linux'
        distribution = 'Redhat'

    class Linux2(Base):
        platform = 'Linux'
        distribution = 'OtherLinux'

    class Linux3(Base):
        platform = 'Linux'

    class Darwin(Base):
        platform = 'Darwin'

    class Darwin2(Base):
        platform = 'Darwin'
        distribution = 'OtherDarwin'

    # If no platform is set, we should get back the base class
    assert get_platform_subclass(Base) == Base

    # If the base class has a platform set, but no subclasses do, we should get back the base class

# Generated at 2022-06-12 23:42:28.181598
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native

    class BaseClass():
        platform = None
        distribution = None
        def __repr__(self):
            if self.platform and self.distribution:
                return "A " + self.platform + " subclass for " + self.distribution
            elif self.platform:
                return "A " + self.platform + " class"
            else:
                return "A base class"

    class RedhatSubclass(BaseClass):
        platform = 'Linux'
        distribution = 'Redhat'

    class RedhatDerivedSubclass(RedhatSubclass):
        distribution = 'Redhat'

    class DebianSubclass(BaseClass):
        platform = 'Linux'
        distribution = 'Debian'


# Generated at 2022-06-12 23:42:38.653007
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class BaseClass(object):
        platform = None
        distribution = None

    class SuperClass(BaseClass):
        pass

    class Solaris(object):
        platform = 'SunOS'
        distribution = None

    class Solaris11(object):
        platform = 'SunOS'
        distribution = 'Solaris'

    class Redhat(object):
        platform = 'Linux'
        distribution = 'Redhat'

    # if no subclass exists, the base class is returned
    assert SuperClass is get_platform_subclass(SuperClass)

    # specific subclass
    assert Solaris11 is get_platform_subclass(BaseClass)

    # generic subclass
    assert Solaris is get_platform_subclass(SuperClass)

    # if no subclass exists at all, the base class is returned

# Generated at 2022-06-12 23:42:49.251570
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Import here so that mocking can work
    from ansible.module_utils import basic

    from ansible.module_utils.basic import AnsibleModule, get_platform_subclass
    from ansible.module_utils.six import PY3

    # Create our dummy subclasses
    class PlatformA:
        platform = 'PlatformA'

    @add_metaclass(AnsibleModule)
    class PlatformB(PlatformA):
        platform = 'PlatformB'

    @add_metaclass(AnsibleModule)
    class DistributionA(PlatformB):
        distribution = 'DistributionA'

    @add_metaclass(AnsibleModule)
    class DistributionB(PlatformB):
        distribution = 'DistributionB'


# Generated at 2022-06-12 23:42:56.158646
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Define 3 classes
    class A(object):
        platform = None
    class B(A):
        distribution = None
    class C(B):
        platform = 'Linux'
        distribution = 'Debian'

    # Test that we get the right class back
    # When asked for the base class
    assert get_platform_subclass(A) is A
    # When asked for the subclass closest to the platform and distribution
    assert get_platform_subclass(B) is C
    # When asked for the subclass closest to the platform
    assert get_platform_subclass(C) is C

# Generated at 2022-06-12 23:42:58.394162
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    codename = get_distribution_codename()
    if codename is None:
        assert True
    else:
        assert False



# Generated at 2022-06-12 23:43:08.933730
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import unittest
    from unittest.mock import patch

    from ansible.module_utils.facts.system.distribution import get_distribution_codename

    distribution_mock = {
        'centos': 'CentOS',
        'debian': 'Debian',
        'fedora': 'Fedora',
        'ubuntu': 'Ubuntu',
        'arch': 'Arch',
        'opensuse': 'OpenSuse',
    }

    version_mock = {
        'centos': '7',
        'debian': '9',
        'fedora': '28',
        'ubuntu': 'xenial',
        'arch': 'rolling',
        'opensuse': '42.3',
    }


# Generated at 2022-06-12 23:43:10.397360
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == "bionic"

# Generated at 2022-06-12 23:43:25.546907
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit tests for function get_platform_subclass

    :returns: True if the unit tests pass and False otherwise
    :rtype: bool
    '''
    ret = True

    # We'll use the following class structure for testing
    class SubOne:
        platform = 'Linux'
        distribution = 'Amazon'

    class SubTwo(SubOne):
        platform = 'Linux'
        distribution = 'Ubuntu'

    class SubThree(SubOne):
        platform = 'Linux'
        distribution = None

    class SubFour(SubTwo):
        platform = 'Linux'
        distribution = 'Ubuntu'

    class SuperClass:
        platform = 'Linux'
        distribution = 'RedHat'

        def test_func(self):
            return False


# Generated at 2022-06-12 23:43:28.406230
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Unit test for function get_distribution_version
    '''
    assert get_distribution_version() == '7.6'

# Generated at 2022-06-12 23:43:38.238395
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test the get_distribution function.  The get_distribution function
    should return the distribution the module is running on.  We use
    uname to see what distribution we're running on since distro is
    very broken.
    '''

    platform_distribution = platform.dist()
    platform_system = platform.system()

    if platform_system == 'Linux':
        if platform_distribution[0].lower() == 'amazon':
            distribution = 'Amazon'
        elif platform_distribution[0].lower() == 'centos':
            distribution = 'Centos'
        elif platform_distribution[0].lower() == 'debian':
            distribution = 'Debian'
        elif platform_distribution[0].lower() == 'fedora':
            distribution = 'Fedora'

# Generated at 2022-06-12 23:43:42.784529
# Unit test for function get_distribution_version
def test_get_distribution_version():
    """
    :return: True if test passes
    """
    # Initialize
    global_commands = {}

    # Test get_distribution_version
    assert get_distribution_version() == None
    assert get_distribution_version() == u''

    # Results
    return True

# Generated at 2022-06-12 23:43:52.171618
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    This function tests the get_platform_subclass function.
    '''
    from ansible.module_utils import basic
    class parent(basic.AnsibleModule):
        platform = 'Linux'
        distribution = None
    class child1(parent):
        distribution = 'Fedora'
    class child2(parent):
        distribution = 'Fedora'
    class child3(parent):
        distribution = 'Debian'
    assert(get_platform_subclass(parent) == parent)
    assert(get_platform_subclass(child1) == child1)
    assert(get_platform_subclass(child3) == child3)
    class grandchild(child2, child3):
        distribution = 'Fedora'
    assert(get_platform_subclass(grandchild) == grandchild)

# Generated at 2022-06-12 23:43:57.463664
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    assert get_platform_subclass(object).__name__ == "object"
    class A:
        platform = platform.system()
        distribution = None
    class B(A):
        distribution = None

    assert get_platform_subclass(A) == B
    assert get_platform_subclass(B) == B

# Generated at 2022-06-12 23:43:58.902442
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Freebsd'


# Generated at 2022-06-12 23:44:08.756927
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    ''' Unit test for Ansible module_utils.basic.get_platform_subclass function '''
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(),
    )

    class BaseClass:
        ''' Base Class '''
        platform = 'base'
        distribution = None

    class LinuxA(BaseClass):
        ''' Linux Implementation A (CentOS)'''
        platform = 'Linux'
        distribution = 'CentOS'

    class LinuxB(BaseClass):
        ''' Linux Implementation B (All Others) '''
        platform = 'Linux'
        distribution = None

    class WindowsClass(BaseClass):
        ''' Windows Implementation '''
        platform = 'Windows'
        distribution = None

    # For most Linux Distributions, we want LinuxB

# Generated at 2022-06-12 23:44:19.025371
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    DISTRO_WITH_CODENAME = u'debian'
    DISTRO_WITHOUT_CODENAME = u'fedora'
    DISTRO_WITH_UBUNTU_CODENAME = u'ubuntu'
    DISTRO_WITHOUT_UBUNTU_CODENAME = u'centos'
    DISTRO_WITH_DEBIAN_CODENAME = u'debian'
    NOT_A_DISTRO = u'not_linux'

    CODENAME_FOR_DISTRO_WITH_CODENAME = u'sid'
    CODENAME_FOR_DISTRO_WITHOUT_CODENAME = None
    CODENAME_FOR_DISTRO_WITH_UBUNTU_CODENAME = u'trusty'

# Generated at 2022-06-12 23:44:29.675993
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Create some mock classes to use in testing
    class MockClass(object):
        distribution = None
        platform = None

    class MockClass2(MockClass):
        distribution = 'Amazon'

    class MockClass3(MockClass):
        distribution = 'Amazon'
        platform = 'Linux'

    class MockClass4(MockClass):
        distribution = 'Amazon'
        platform = 'Darwin'

    # test that a subclass with a matching distribution name is selected
    subclass = get_platform_subclass(MockClass)
    assert subclass is MockClass2

    # test that the more specific subclass with a matching platform is selected
    subclass = get_platform_subclass(MockClass2)
    assert subclass is MockClass3

    # test that the more specific subclass with a matching platform is selected

# Generated at 2022-06-12 23:44:59.722900
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Foo():
        platform = 'foo'
    class Foo_Bar(Foo):
        distribution = 'bar'
    class Foo_Baz(Foo):
        distribution = 'baz'
    class Foo_Baz_qux(Foo_Baz):
        distribution_release = 'qux'

    # This isn't so much a unit test as it is a way to see what subclass you
    # get on your system.  You can add entries below to see what will be
    # returned by get_platform_subclass on a particular platform.

# Generated at 2022-06-12 23:45:08.922237
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base(object):
        platform = None
        distribution = None

    class LinuxBase(Base):
        platform = 'Linux'

    class RedhatBase(LinuxBase):
        distribution = 'Redhat'

    class CentosBase(LinuxBase):
        distribution = 'Centos'

    class HpuxBase(Base):
        platform = 'HP-UX'

    class Hpux(HpuxBase):
        pass

    class Linux(LinuxBase):
        pass

    class Redhat(RedhatBase):
        pass

    class Centos(CentosBase):
        pass

    assert get_platform_subclass(Base) is Base
    assert get_platform_subclass(LinuxBase) is LinuxBase
    assert get_platform_subclass(RedhatBase) is RedhatBase

# Generated at 2022-06-12 23:45:17.042075
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform

    class Module:
        pass

    class SolarisModule(Module):
        platform = 'SunOS'
        distribution = None

    class LinuxModule(Module):
        platform = 'Linux'
        distribution = None

    class RedhatModule(Module):
        platform = 'Linux'
        distribution = 'Redhat'

    class DebianModule(Module):
        platform = 'Linux'
        distribution = 'Debian'

    class TestModule(Module):
        pass

    assert get_platform_subclass(SolarisModule) == SolarisModule
    assert get_platform_subclass(LinuxModule) == LinuxModule
    assert get_platform_subclass(RedhatModule) == RedhatModule
    assert get_platform_subclass(DebianModule) == DebianModule
    assert get_platform_subclass(TestModule) == TestModule


# Generated at 2022-06-12 23:45:18.258066
# Unit test for function get_distribution
def test_get_distribution():
    # RedHat return Redhat
    assert get_distribution() == "Redhat"


# Generated at 2022-06-12 23:45:29.162620
# Unit test for function get_distribution
def test_get_distribution():

    '''
     This test runs validates the get_distribution return value
    '''

    # Test on Redhat enterprise 6, hard to install that on all our test machines,
    # so we will fake it.
    with patch('platform.system', return_value='Linux'), \
            patch('distro.id', return_value='rhel'), \
            patch('distro.version', return_value='6.1.10'):
        assert 'Redhat' == get_distribution()

    # Test on Redhat enterprise 7, hard to install that on all our test machines,
    # so we will fake it.

# Generated at 2022-06-12 23:45:30.361369
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() != '', "get_distribution() returned an empty string"

# Generated at 2022-06-12 23:45:37.152643
# Unit test for function get_distribution_version
def test_get_distribution_version():
    import types

    # Test code path when version is not available
    distro.linux_distribution = types.ModuleType("distro").linux_distribution
    distro.linux_distribution.return_value = ("", "", "")
    assert get_distribution_version() is None

    # Test code path when version is available
    distro.linux_distribution.return_value = ("", "18.04", "")
    assert get_distribution_version() == "18.04"

# Generated at 2022-06-12 23:45:44.413828
# Unit test for function get_platform_subclass

# Generated at 2022-06-12 23:45:46.872890
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() == '7'
    assert get_distribution() == 'Redhat'

# Generated at 2022-06-12 23:45:55.461529
# Unit test for function get_distribution_version
def test_get_distribution_version():
    from ansible.module_utils.common._collections_compat import UserDict
    from ansible.module_utils.common._utils import mock_module

    class OSRelease(UserDict):
        def __init__(self, id='centos', version='7.3', version_best='7.3.1611'):
            super(OSRelease, self).__init__()
            self.data['id'] = id
            self.data['version'] = version
            self.data['version_best'] = version_best


# Generated at 2022-06-12 23:46:26.190080
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # Python 3
    assert get_distribution_codename() == None

    # CentOS

# Generated at 2022-06-12 23:46:34.129386
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Return the code name for this Linux Distribution

    :rtype: NativeString or None
    :returns: A string representation of the distribution's codename or None if not a Linux distro
    '''
    codename = None
    if platform.system() == 'Linux':
        # Until this gets merged and we update our bundled copy of distro:
        # https://github.com/nir0s/distro/pull/230
        # Fixes Fedora 28+ not having a code name and Ubuntu Xenial Xerus needing to be "xenial"
        os_release_info = distro.os_release_info()
        codename = os_release_info.get('version_codename')

        if codename is None:
            codename = os_release_info.get('ubuntu_codename')


# Generated at 2022-06-12 23:46:43.222186
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        platform = 'Base'
        distribution = None

    class BaseLinux(Base):
        platform = 'Linux'
        distribution = None

    class BaseRedhat(BaseLinux):
        distribution = 'Redhat'

    class BaseUbuntu(BaseLinux):
        distribution = 'Ubuntu'

    platform = platform.system()
    dist = get_distribution()

    assert BaseRedhat == get_platform_subclass(BaseRedhat)
    assert BaseRedhat == get_platform_subclass(BaseLinux)
    assert BaseRedhat == get_platform_subclass(Base)
    assert BaseUbuntu == get_platform_subclass(BaseUbuntu)
    assert BaseUbuntu == get_platform_subclass(BaseLinux)
    assert BaseUbuntu == get_platform_subclass(Base)
    assert Base == get_platform

# Generated at 2022-06-12 23:46:44.834952
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() is not None



# Generated at 2022-06-12 23:46:56.188648
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Return the class it's called on when no subclass is specified
    class A:
        platform = 'APlatform'
        distribution = None
    assert(A == get_platform_subclass(A))

    # Return the first subclass found for the platform
    class B:
        platform = 'BPlatform'
        distribution = None
    platform_subclasses = [B]
    for i in range(10):
        platform_subclasses.append(type('Subclass%s' % i, (B, object), dict(platform='BPlatform', distribution=None)))
    assert(B == get_platform_subclass(B))

    # Return the first subclass found for the platform and exact distribution
    class SRPMSubclass(B):
        platform = 'BPlatform'
        distribution = 'BPlatformLinux'

# Generated at 2022-06-12 23:47:05.677694
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class DistributionIndependentPlatformIndependent:
        distribution = None
        platform = None

    class DistributionSpecificPlatformIndependent(DistributionIndependentPlatformIndependent):
        distribution = 'TestDistribution'

    class DistributionSpecificPlatformSpecific(DistributionSpecificPlatformIndependent):
        platform = 'TestPlatform'

    class DistributionIndependentPlatformSpecific(DistributionIndependentPlatformIndependent):
        platform = 'TestPlatform'

    assert get_platform_subclass(DistributionIndependentPlatformIndependent) == DistributionIndependentPlatformIndependent
    assert get_platform_subclass(DistributionIndependentPlatformSpecific) == DistributionIndependentPlatformIndependent

    assert get_platform_subclass(DistributionSpecificPlatformIndependent) == DistributionSpecificPlatformIndependent
    assert get_platform_subclass(DistributionSpecificPlatformSpecific) == DistributionSpecificPlatformSpecific

# Generated at 2022-06-12 23:47:13.965560
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    """
    Unit test function for function get_platform_subclass.
    """
    class Base:
        platform = 'Base'

    class Apple(Base):
        platform = 'Darwin'
        distribution = None

    class FreeBSD(Base):
        platform = 'FreeBSD'
        distribution = None

    class Ubuntu(Base):
        platform = 'Linux'
        distribution = 'Ubuntu'

    class SUSE(Base):
        platform = 'Linux'
        distribution = 'SUSE'

    class Redhat(Base):
        platform = 'Linux'
        distribution = 'Redhat'

    class OtherLinux(Base):
        platform = 'Linux'
        distribution = None

    class FreeBSDNonFreeBSD(Base):
        platform = 'FreeBSD'
        distribution = 'CentOS'


# Generated at 2022-06-12 23:47:24.611082
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import ansible

    # Simulate CentOS 7
    distro.id = lambda: 'centos'
    distro.version = lambda: '7.1.1503'
    distro.codename = lambda: ''
    distro.lsb_release_info = lambda: {}
    distro.os_release_info = lambda: {'id': 'centos', 'version': '7.1.1503', 'version_id': '7.1.1503',
                                      'version_codename': 'Core', 'pretty_name': 'CentOS Linux 7 (Core)',
                                      'codename': 'Core'}

    assert get_distribution_codename() == 'Core', "CentOS 7 code name should be 'Core'"

    # Simulate Fedora 28
    distro.id = lambda: 'fedora'
    distro

# Generated at 2022-06-12 23:47:34.331254
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        distribution = None
        platform = None

    class LinuxBase(Base):
        platform = 'Linux'

    class Linux_Debian_Base(LinuxBase):
        distribution = 'Debian'

    class Ubuntu_Base(Linux_Debian_Base):
        codename = None

    class Ubuntu(Ubuntu_Base):
        codename = 'yakkety'

    class Ubuntu1604(Ubuntu_Base):
        codename = 'xenial'

    class Ubuntu1604_OtherLinux(LinuxBase):
        distribution = 'OtherLinux'
        codename = 'xenial'

    class Ubuntu1404(Ubuntu_Base):
        codename = 'trusty'

    class OtherLinux(LinuxBase):
        distribution = 'OtherLinux'


# Generated at 2022-06-12 23:47:43.136497
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    # Test when distribution is present
    def get_codename(os_name, os_version, os_codename):
        '''
        Test when the os_release_info is present
        '''
        return {'id': os_name, 'version': os_version, 'version_codename': os_codename, 'codename': os_codename}
    distro.os_release_info = lambda: get_codename('fedora', '27', 'TwentySeven')
    assert get_distribution_codename() == 'TwentySeven'

    distro.os_release_info = lambda: get_codename('centos', '7', 'Seven')
    assert get_distribution_codename() == 'Seven'

    # Test when the version_codename is not present
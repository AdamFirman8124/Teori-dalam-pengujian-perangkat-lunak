

# Generated at 2022-06-12 23:38:18.697679
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    distribution_codename = get_distribution_codename()

    assert distribution_codename is not None, u'The function get_distribution_codename must return a value'
    assert (isinstance(distribution_codename, str) or isinstance(distribution_codename, unicode)) , \
        u'The function get_distribution_codename must return a string or unicode'

# Generated at 2022-06-12 23:38:19.620641
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == None


# Generated at 2022-06-12 23:38:21.004497
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == distro.id().capitalize()


# Generated at 2022-06-12 23:38:23.403941
# Unit test for function get_distribution
def test_get_distribution():
    # Test get_distribution for all linux distros
    for distro in distro.linux_distribution():
        assert(get_distribution() == distro.capitalize())



# Generated at 2022-06-12 23:38:30.893536
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils import basic

    # platforms and parameters for tests
    platforms = {
        'Linux': 'Linux',
        'Darwin': 'MacOSX',
        'FreeBSD': 'FreeBSD',
        'OpenBSD': 'OpenBSD',
        'NetBSD': 'NetBSD',
        'SunOS': 'Solaris',
        'AIX': 'AIX'
    }

    distributions = {
        'Amazon': 'Amazon',
        'CentOS': 'CentOS',
        'Debian': 'Debian',
        'Gentoo': 'Gentoo',
        'Mandriva': 'Mandriva',
        'RedHat': 'RedHat',
        'SUSE': 'SUSE',
        'Ubuntu': 'Ubuntu',
    }


# Generated at 2022-06-12 23:38:32.677545
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == platform.dist()[0].capitalize()


# Generated at 2022-06-12 23:38:34.065518
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'xenial'

# Generated at 2022-06-12 23:38:35.738086
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Make sure the code handles different distributions properly
    '''

    assert get_distribution_version() is not None

# Generated at 2022-06-12 23:38:38.771663
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    If the script is run without arguments, run the tests
    '''
    tt = TestGetDistributionCodename()
    tt.test_get_distribution_codename()



# Generated at 2022-06-12 23:38:50.501151
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        pass

    class B(A):
        platform = 'Linux'

    assert get_platform_subclass(A) == A
    assert get_platform_subclass(B) == B

    class C(A):
        platform = platform.system()

    class D(A):
        platform = platform.system()
        distribution = distro.id()

    class E(A):
        platform = 'Linux'
        distribution = "OtherLinux"

    assert get_platform_subclass(C) == C
    assert get_platform_subclass(D) == D
    assert get_platform_subclass(E) == E

    class F(E):
        platform = 'Linux'
        distribution = "OtherLinux"
        version = "OtherLinuxVersion"

    class G(D):
        platform = 'Linux'
       

# Generated at 2022-06-12 23:39:06.470541
# Unit test for function get_distribution_version
def test_get_distribution_version():
    import platform
    import distro
    dist = platform.linux_distribution()
    print("platform.linux_distribution() = %s" % repr(dist))
    dist = distro.linux_distribution()
    print("distro.linux_distribution() = %s" % repr(dist))
    dist = distro.os_release_info()
    print("distro.os_release_info() = %s" % repr(dist))
    dist = distro.lsb_release_info()
    print("distro.lsb_release_info() = %s" % repr(dist))

if __name__ == '__main__':
    test_get_distribution_version()

# Generated at 2022-06-12 23:39:17.266842
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class SuperClassA_Generic:
        pass
    class SuperClassA_Platform:
        platform = 'A'
    class SuperClassA_Distro:
        platform = 'A'
        distribution = 'A'
    class SuperClassA_Platform_Distro:
        platform = 'A'
        distribution = 'A'
    class SuperClassB_Generic:
        pass
    class SuperClassB_Platform:
        platform = 'B'
    class SuperClassB_Distro:
        platform = 'B'
        distribution = 'B'
    class SuperClassB_Platform_Distro:
        platform = 'B'
        distribution = 'B'
    class SuperClassC_Generic:
        pass
    class SubClassA_Platform(SuperClassA_Platform):
        pass

# Generated at 2022-06-12 23:39:28.441191
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        ''' parent base class '''
        pass

    class PlatformBase(Base):
        ''' Base class for all platform-specific subclasses '''
        platform = 'Test'
        distribution = None

    class TestPlatform(PlatformBase):
        ''' Test platform subclass '''
        pass

    class FooPlatform(PlatformBase):
        ''' Test platform subclass '''
        pass

    class LinuxPlatform(PlatformBase):
        ''' Base class for all Linux platform-specific subclasses '''
        distribution = None
        platform = 'Linux'

    class TestLinux(LinuxPlatform):
        ''' Test Linux subclass '''
        distribution = 'TestLinux'

    platform.system = lambda: 'Test'
    assert Base == get_platform_subclass(Base)
    platform.system = lambda: 'Linux'

# Generated at 2022-06-12 23:39:35.627438
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class BaseClass(object):
        distribution = platform = None
    class LinuxBase(BaseClass):
        distribution = platform = 'Linux'
    class DebianBase(LinuxBase):
        distribution = 'Debian'
    class RedHatBase(LinuxBase):
        distribution = 'Redhat'
    class SuseBase(LinuxBase):
        distribution = 'Suse'
    class DerivedClass(RedHatBase, DebianBase, SuseBase):
        pass

    def get_platform():
        if platform.system() == 'Linux':
            for distro in ('redhat', 'centos', 'fedora'):
                if distro in platform.dist():
                    return ('Linux', 'Redhat')
            for distro in ('debian', 'ubuntu'):
                if distro in platform.dist():
                    return ('Linux', 'Debian')

# Generated at 2022-06-12 23:39:44.933783
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # Sets up a mock for the distro.version function and verifies that
    # get_distribution_version returns the expected result.
    def mock_version_func(best=False):
        # Mocks distro.version.
        if best is True:
            return "1.2.3.4.5"
        return "1.2.3"

    try:
        real_version = distro.version
        distro.version = mock_version_func
        assert get_distribution_version() == "1.2.3"
        distro.version = real_version
    except:
        distro.version = real_version
        raise


# Generated at 2022-06-12 23:39:48.317693
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # CentOS
    assert get_distribution_version() == u'8.0'

    # Ubuntu
    assert get_distribution_version() == u'16.04'

# Generated at 2022-06-12 23:39:52.442699
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Test the function get_distribution_version
    '''

    # tbd - need to mock distro.id() and distribute.version()
    expected_version = '7.0'
    distribution_version = get_distribution_version()

    assert distribution_version == expected_version

# Generated at 2022-06-12 23:40:03.147893
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils import basic

    class TestSubClass(object):
        pass

    class TestSub2Class(object):
        pass

    class TestSubSubClass(TestSubClass):
        pass

    class TestSubSub2Class(TestSubClass):
        pass

    class TestSubSubSubClass(TestSubSubClass):
        pass

    class TestSubSubSub2Class(TestSubSubClass):
        pass

    assert get_platform_subclass(TestSubClass) == TestSubClass
    assert get_platform_subclass(TestSubClass, []) == TestSubClass

    class TestClassNoSubclass(basic.AnsibleModule):
        platform = 'Linux'
        distribution = None

    assert get_platform_subclass(TestClassNoSubclass, []) == TestClassNoSubclass


# Generated at 2022-06-12 23:40:10.157599
# Unit test for function get_distribution
def test_get_distribution():
    # This function is currently only implemented for Linux
    if platform.system() != 'Linux':
        return

    distribution = get_distribution()

    assert distribution is not None, "get_distribution should never return None"

    # Make sure it's the name of a distribution we know about
    for sc in get_all_subclasses(platform.PlatformBase):
        assert distribution != sc.distribution, "Distribution %s not found in any subclass" % distribution


# Generated at 2022-06-12 23:40:20.641110
# Unit test for function get_distribution
def test_get_distribution():
    if platform.system() == 'Linux':
        if distro.id() == 'alpine':
            # Test function get_distribution for alpine Linux
            assert get_distribution() == 'Alpine'
        elif distro.id() == 'amzn':
            # Test function get_distribution for amazon Linux
            assert get_distribution() == 'Amazon'
        elif distro.id() == 'arch':
            # Test function get_distribution for arch Linux
            assert get_distribution() == 'Arch'
        elif distro.id() == 'centos':
            # Test function get_distribution for centos Linux
            assert get_distribution() == 'Centos'
        elif distro.id() == 'oracle':
            # Test function get_distribution for oracle Linux
            assert get_distribution

# Generated at 2022-06-12 23:40:41.886388
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    """
    Test get_distribution_codename()
    """
    # Test codename when available
    distributions = [
        dict(id="Debian", ubuntu_codename="debian", version_codename=""),
        dict(id="Ubuntu", ubuntu_codename="ubuntu", version_codename=""),
        dict(id="LinuxMint", ubuntu_codename="linuxmint", version_codename=""),
    ]
    for distribution in distributions:
        codename = get_distribution_codename()
        assert codename == distribution['ubuntu_codename']
        # Test codename when ubuntu_codename is missing, ensure codename is None
        distribution['ubuntu_codename'] = None
        codename = get_distribution_codename()
        assert codename is None

    # Test codename when version_codename is

# Generated at 2022-06-12 23:40:51.036464
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        pass

    class B(A):
        pass

    class C(B):
        distribution = None
        platform = 'dummy'

    class D(B):
        distribution = 'other'
        platform = 'dummy'

    class E(A):
        distribution = None
        platform = 'test'

    class F(A):
        distribution = 'test'
        platform = 'test'

    class G(A):
        distribution = 'other'
        platform = 'test'

    assert A == get_platform_subclass(A)
    assert C == get_platform_subclass(B)
    assert E == get_platform_subclass(A)
    assert F == get_platform_subclass(A)

# Generated at 2022-06-12 23:40:52.799109
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'OtherLinux'
    assert get_distribution_version() == ''

# Generated at 2022-06-12 23:41:02.612103
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    :returns: A tuple of 3-tuples containing: (class name, args, kwargs, expected class)
    '''
    dists = [
        None,
        'Linux',
        'OtherLinux',
        'FreeBSD',
        'Darwin',
        # Distro specific (Redhat, Ubuntu, ...)
    ]

    valid_classes = [
        'NoSubclass',
        'PlatformSubclass',
    ]

    for dist in dists:
        for valid_class in valid_classes:
            args = [valid_class, '%s/%s' % (dist, valid_class)]
            kwargs = dict()
            expected = valid_class
            yield args, kwargs, expected

    # Distro specific

# Generated at 2022-06-12 23:41:07.302202
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Ensure that the get_platform_subclass() function works as expected
    '''
    # pylint: disable=unused-variable

    class TestBase(object):
        '''
        Base class to test get_platform_subclass() function
        '''
        def __new__(cls, *args, **kwargs):
            new_cls = get_platform_subclass(cls)
            return super(cls, new_cls).__new__(new_cls)

    class TestLinux_Subclass(TestBase):
        '''
        Linux subclass to test get_platform_subclass() function
        '''
        platform = 'Linux'


# Generated at 2022-06-12 23:41:13.031731
# Unit test for function get_distribution_version
def test_get_distribution_version():
    distributions = {
        None: None,
        'centos': '7.4.1708',
        'debian': '9.4',
        'fedora': '28',
        'redhat': '7.4',
        'ubuntu': '18.04',
        'amzn': '2'
    }
    for distro_id, version in distributions.items():
        with distro.mock_distro_info(distro_id, version):
            assert get_distribution_version() == version

# Generated at 2022-06-12 23:41:19.993539
# Unit test for function get_distribution

# Generated at 2022-06-12 23:41:29.852401
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Tests for function get_platform_subclass
    '''
    from ansible.module_utils import basic

    class DummyClass1(basic.AnsibleModule):
        """
        Dummy class for testing
        """
        distribution = None
        platform = 'Linux'

    class DummyClass2(basic.AnsibleModule):
        """
        Dummy class for testing
        """
        distribution = 'Linux'
        platform = 'Linux'

    class DummyClass3(basic.AnsibleModule):
        """
        Dummy class for testing
        """
        distribution = 'Linux'
        platform = 'Windows'

    class DummyClass4(basic.AnsibleModule):
        """
        Dummy class for testing
        """
        distribution = None
        platform = 'Windows'


# Generated at 2022-06-12 23:41:39.665296
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class TestBaseClass():
        platform = None
        distribution = None

    class TestSpecificSubClass(TestBaseClass):
        platform = 'Linux'
        distribution = 'OtherLinux'

    class TestLinuxSubClass(TestBaseClass):
        platform = 'Linux'
        distribution = None

    class TestOtherSubClass(TestBaseClass):
        platform = 'BSD'
        distribution = None

    assert(get_platform_subclass(TestBaseClass) == TestBaseClass)
    assert(get_platform_subclass(TestSpecificSubClass) == TestSpecificSubClass)
    assert(get_platform_subclass(TestLinuxSubClass) == TestLinuxSubClass)
    assert(get_platform_subclass(TestOtherSubClass) == TestOtherSubClass)

# Generated at 2022-06-12 23:41:49.896221
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    This function unit tests the function get_platform_subclass, along with the
    base class for all platform subclasses.
    '''

    class FakeModule:
        def __init__(self):
            self.__dict__ = {}
            self.__dict__['platform'] = platform.system()
            self.__dict__['distribution'] = distro.id()
            self.__dict__['distribution_version'] = distro.version()
            self.__dict__['distribution_major_version'] = distro.major_version()

    class FakePlatform:
        _platform = 'Generic'

        @classmethod
        def platform(cls):
            return cls._platform

        @classmethod
        def distribution(cls, fail_if_unknown=False):
            return cls._distribution


# Generated at 2022-06-12 23:42:17.252338
# Unit test for function get_distribution_version
def test_get_distribution_version():
    from ansible.module_utils._text import to_text

    assert not to_text(get_distribution_version())


# Generated at 2022-06-12 23:42:19.609127
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'bionic'
    assert get_distribution_codename() is not None
test_get_distribution_codename()

# Generated at 2022-06-12 23:42:27.308269
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Import the test class after we've defined get_platform_subclass to avoid a circular import
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import macOS
    from ansible.module_utils.facts.system.distribution import OtherLinux
    from ansible.module_utils.facts.system.distribution import UnknownDistribution

    # on a Mac there should be no distribution subclass (macOS is a platform subclass)
    platform_ = 'Darwin'
    subclass = get_platform_subclass(Distribution)
    assert subclass == Distribution

    # Mac OS version should be 2.7.10
    platform_ = 'Darwin'
    subclass = get_platform_subclass(macOS)
    assert subclass == macOS

    # on Amazon should be a subclass
    platform

# Generated at 2022-06-12 23:42:38.109874
# Unit test for function get_distribution
def test_get_distribution():

    from ansible.module_utils import basic
    import os
    import platform
    import stat
    import tempfile
    import unittest

    class Test_GetDistribution(unittest.TestCase):

        def setUp(self):
            (fd, self.os_release_file) = tempfile.mkstemp()
            self.os_release_file_save = os.path.join(os.path.dirname(self.os_release_file), 'os-release.save')

        def tearDown(self):
            if os.path.isfile(self.os_release_file):
                os.unlink(self.os_release_file)
            if os.path.isfile(self.os_release_file_save):
                os.unlink(self.os_release_file_save)


# Generated at 2022-06-12 23:42:40.108309
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Function get_distribution() unit test
    '''
    assert get_distribution() == 'Linuxmint'

# Generated at 2022-06-12 23:42:41.394005
# Unit test for function get_distribution
def test_get_distribution():
    pass

# Generated at 2022-06-12 23:42:46.919371
# Unit test for function get_distribution
def test_get_distribution():
    distro.id = lambda: "Debian"
    assert get_distribution() == "Debian"

    distro.id = lambda: "Redhat"
    assert get_distribution() == "Redhat"

    distro.id = lambda: "Redhat"
    assert get_distribution() == "Redhat"

    distro.id = lambda: "Centos"
    assert get_distribution() == "Redhat"


# Generated at 2022-06-12 23:42:47.874745
# Unit test for function get_distribution
def test_get_distribution():
    assert isinstance(get_distribution(), str)

# Generated at 2022-06-12 23:42:57.198437
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    old_platform_system = platform.system
    old_distro_id = distro.id
    old_distro_codename = distro.codename
    old_os_release_info = distro.os_release_info
    old_lsb_release_info = distro.lsb_release_info


# Generated at 2022-06-12 23:42:58.351050
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() is None

# Generated at 2022-06-12 23:43:24.416986
# Unit test for function get_distribution_version
def test_get_distribution_version():

    assert get_distribution_version() == get_distribution_version()

# Generated at 2022-06-12 23:43:35.228853
# Unit test for function get_distribution
def test_get_distribution():
    def _test_get_distribution(distro_id, expected_id, expected_version, expected_codename):
        distro.id = lambda: distro_id
        distro.version = lambda: distro_id
        distro.codename = lambda: distro_id
        distro.lsb_release_info = lambda: distro_id
        distro.os_release_info = lambda: distro_id
        distro.distro_release_info = lambda: distro_id

        try:
            assert get_distribution() == expected_id
            assert get_distribution_version() == expected_version
            assert get_distribution_codename() == expected_codename
        finally:
            distro.id = lambda: None
            distro.version = lambda: None

# Generated at 2022-06-12 23:43:36.659480
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # cover centos and debian
    assert get_distribution_version()

# Generated at 2022-06-12 23:43:45.875909
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    # Case 1: This function should not return None
    # Initialize the variable to None
    codename = None
    # We will check if the function returns None
    codename = get_distribution_codename()
    assert codename is not None
    # Case 2: This function should return codename
    # Initialise the variable to a known value of "cosmic"
    codename = "cosmic"
    # Call the function
    codename = get_distribution_codename()
    # Check if codename is set to the desired value after calling
    # the function
    assert codename == "cosmic"


# Generated at 2022-06-12 23:43:52.471693
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # Before testing code name, we should test whether it is on a Linux platform or not.
    assert platform.system() == 'Linux'

    # The code name of CentOS should be '' and the codename of Amazon Linux should be None.
    assert get_distribution_codename() == ''

    # The code name of Fedora is None.
    assert get_distribution_codename() == None

    # The code name of Ubuntu should be 'focal' and the codename of Ubuntu Xenial Xerus should be 'xenial'.
    assert get_distribution_codename() == 'focal'

# Generated at 2022-06-12 23:44:05.417137
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test that the get_platform_subclass() function works correctly.
    '''
    import sys
    tests = (
        {'system': 'Linux', 'distro': None, 'class': 'Linux'},
        {'system': 'Linux', 'distro': 'redhat', 'class': 'LinuxRedHat'},
        {'system': 'Linux', 'distro': 'otherlinux', 'class': 'Linux'},
        {'system': 'FreeBSD', 'distro': None, 'class': 'FreeBSD'},
        {'system': 'FooBar', 'distro': None, 'class': 'Generic'},
    )
    platform_to_system = {
        'linux2': 'Linux',
        'freebsd10': 'FreeBSD',
        'foo': 'FooBar',
    }


# Generated at 2022-06-12 23:44:15.574155
# Unit test for function get_distribution
def test_get_distribution():
    platform_list = ['Linux', 'Darwin', 'FreeBSD', 'SunOS', 'OpenBSD', 'NetBSD', 'AIX', 'HP-UX', 'DragonFly', 'Microsoft', 'CYGWIN_NT-10.0']
    for platform_test in platform_list:
        assert get_distribution(platform_test) == get_distribution_version(platform_test) == None
    assert get_distribution('Linux') == 'redhat'
    assert get_distribution_version('Linux') == '6.5'
    assert get_distribution('Darwin') == 'Darwin'
    assert get_distribution_version('Darwin') == '14.4.0'

# Generated at 2022-06-12 23:44:19.025376
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Ubuntu', 'The distribution does not match what it should'
    assert get_distribution_version() == '16.04', 'The distribution version does not match what it should'
    assert get_distribution_codename() == 'xenial', 'The distribution codename does not match what it should'

# Generated at 2022-06-12 23:44:29.672123
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform

    # Loading mocks
    import mock
    import sys

    class MockLinux:
        platform = 'Linux'
        distribution = 'Ubuntu'

        def __new__(cls, *args, **kwargs):
            return super(MockLinux, cls).__new__(cls)

    class MockFreebsd:
        platform = 'FreeBSD'

        def __new__(cls, *args, **kwargs):
            return super(MockFreebsd, cls).__new__(cls)

    class MockDual:
        platform = 'FreeBSD'
        distribution = 'Ubuntu'

        def __new__(cls, *args, **kwargs):
            return super(MockDual, cls).__new__(cls)


# Generated at 2022-06-12 23:44:31.593378
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    DISTRIBUTION_CODENAME = get_distribution_codename()
    assert DISTRIBUTION_CODENAME is None

# Generated at 2022-06-12 23:44:59.100602
# Unit test for function get_distribution
def test_get_distribution():
    # Make sure that get_distribution works
    assert get_distribution() is not None, 'Failed to get the distribution'

# Generated at 2022-06-12 23:45:08.432276
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Unit test for function get_distribution_codename
    '''
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native


# Generated at 2022-06-12 23:45:16.647901
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        platform = None
        distribution = None
    class B(A):
        platform = "Linux"
    class C(B):
        pass
    class D(B):
        platform = "Linux"
        distribution = "Amazon"
    class E(B):
        platform = "Linux"
        distribution = "RedHat"
    class F(A):
        platform = "Linux"
        distribution = "RedHat"

    # get_platform_subclass() should return the most specific subclass defined
    # for platform and distribution.  In the order of precedence defined by the
    # classes above, that's D, E, and then F.
    class PlatformLinuxDistributionAmazon(A):
        platform = "Linux"
        distribution = "Amazon"
    class PlatformLinuxDistributionRedHat(A):
        platform = "Linux"
       

# Generated at 2022-06-12 23:45:28.267981
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence
    from ansible.module_utils.six import PY3

    class MockDistro(object):
        def __init__(self):
            self._id = None
            self._codename = ''
            self._version = ''
            self._os_release_info = {}
            self._lsb_release_info = {}

        def id(self):
            return self._id

        def codename(self):
            return self._codename

        def version(self, *args, **kwargs):
            return self._version

        def os_release_info(self):
            return self._os_release_info

        def lsb_release_info(self):
            return self._lsb_release_info


# Generated at 2022-06-12 23:45:38.388133
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    ansible_mac = dict(
        platform = 'Darwin',
        distribution = None,
        )

    ansible_linux = dict(
        platform = 'Linux',
        distribution = None,
        )

    ansible_linux_redhat = dict(
        platform = 'Linux',
        distribution = 'Redhat',
        )

    ansible_linux_amazon = dict(
        platform = 'Linux',
        distribution = 'Amazon',
        )

    ansible_linux_other = dict(
        platform = 'Linux',
        distribution = 'OtherLinux',
        )

    ansible_bsd = dict(
        platform = 'FreeBSD',
        distribution = None,
        )

    assert ansible_mac == ansible_mac
    assert ansible_linux == ansible_linux

# Generated at 2022-06-12 23:45:44.843271
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import inspect
    from ansible.module_utils.basic import get_platform_subclass

    # define a set of classes to test with
    class Foo(object):
        pass

    class FooSpecificA(Foo):
        platform = 'UnitTestA'
    class FooGenericA(Foo):
        pass

    class FooSpecificB(Foo):
        platform = 'UnitTestB'
    class FooGenericB(Foo):
        pass

    class FooSpecificAB(Foo):
        platform = 'UnitTestAB'
    class FooGenericAB(Foo):
        pass

    classes = sorted(Foo.__subclasses__(), key=lambda x: x.__name__)

    # test get_platform_subclass

# Generated at 2022-06-12 23:45:54.609810
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test function get_platform_subclass

    :returns: None
    '''
    distribution = platform.linux_distribution()

    class BaseClass:
        """ Base class for testing get_platform_subclass """
        platform = 'Linux'
        distribution = distribution[0]

    class TestClass:
        """ Class for testing get_platform_subclass """
        platform = 'Linux'
        distribution = None

    class TestClass2:
        """ Class for testing get_platform_subclass """
        platform = 'Linux'
        distribution = 'OtherLinux'

    # Verify that on a Linux distribution we get the most specific subclass with a match
    test_platform = get_platform_subclass(BaseClass)
    assert test_platform == BaseClass

    # Verify that we get the base class if there's no subclass of the right provenance

# Generated at 2022-06-12 23:45:55.280178
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    pass

# Generated at 2022-06-12 23:46:04.748700
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Code name of some distros:
    ubuntu: xenial
    debian: buster
    centos (rhel): 7
    suse: sles
    fedora: <missing>
    '''
    codename = get_distribution_codename()
    if codename is None:
        assert platform.system() != 'Linux'
    else:
        # for the built-in distros, the default value is just the distribution name
        if codename == get_distribution():
            assert codename in ('fedora', 'ubuntu', 'debian', 'centos', 'suse', 'amzn')



# Generated at 2022-06-12 23:46:08.129919
# Unit test for function get_distribution
def test_get_distribution():

    distribution = get_distribution()

    print("Distribution is: %s" % distribution)


if __name__ == '__main__':
    test_get_distribution()

# Generated at 2022-06-12 23:46:42.747255
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        platform = "A"
    class B(A):
        platform = "B"
    class C(B):
        platform = "C"

    class D(A):
        platform = "D"
        distribution = "D1"
    class E(D):
        distribution = "E1"
    class F(D):
        distribution = "F1"

    class G:
        platform = "G"

    class H(G):
        platform = "H"

    class I(G):
        distribution = "I1"

    class J(G):
        distribution = "J1"
        platform = "J2"

    class K(G):
        distribution = "K1"
        platform = "K2"
    class L(K):
        platform = "L2"

    # All of these

# Generated at 2022-06-12 23:46:54.645915
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import platform

    # create a virtual linux platform
    old_platform = platform.system()
    platform.system = lambda : 'Linux'

    # create a virtual function to get distro id
    def VirtualDistroID(distro_id):
        return distro_id

    old_distro_id = distro.id
    distro.id = VirtualDistroID

    # create a virtual readlink function to get os release file name
    def VirtualReadLink(submodule):
        return submodule

    # create a virtual os release info for distro

# Generated at 2022-06-12 23:47:01.108735
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class TestClass:
        pass

    class TestSubClass(TestClass):
        pass

    assert get_platform_subclass(TestClass) == TestClass

    class LinuxTestSubClass(TestClass):
        platform = "Linux"

    assert get_platform_subclass(TestClass) == LinuxTestSubClass

    class LinuxTestSubSubClass(LinuxTestSubClass):
        pass

    assert get_platform_subclass(TestClass) == LinuxTestSubSubClass

# Generated at 2022-06-12 23:47:10.435126
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import ansible.module_utils.basic

    class BaseClass(object):
        platform = 'Linux'
        distribution = None

    class SpecificClass(BaseClass):
        platform = 'Linux'
        distribution = 'Ubuntu'


    class SpecificClass2(BaseClass):
        platform = 'Linux'
        distribution = 'Ubuntu'


    class UnrelatedClass(object):
        platform = 'AIX'
        distribution = 'OtherLinux'


    # Search on Linux, any distribution
    subclass = get_platform_subclass(BaseClass)
    assert subclass == BaseClass

    # Search on Linux, specific distribution
    subclass = get_platform_subclass(SpecificClass)
    assert subclass == SpecificClass

    # Search on Linux, specific distribution, with 2 possible subclasses
    subclass = get_platform_subclass(SpecificClass2)
   

# Generated at 2022-06-12 23:47:17.049212
# Unit test for function get_distribution_version
def test_get_distribution_version():

    distro_id = get_distribution()

    if distro_id:
        distro_version = get_distribution_version()
        if distro_id in ('Debian', 'Ubuntu'):
            assert distro_version and not distro_version.endswith('.'), 'Your system is broken, and there is no distribution version: {}'.format(distro_version)
        else:
            assert distro_version is not None, 'Your system is broken, and there is no distribution version'
    else:
        assert platform.system() != 'Linux'

# Generated at 2022-06-12 23:47:27.769454
# Unit test for function get_distribution_codename

# Generated at 2022-06-12 23:47:36.159246
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class BaseClass():
        pass

    class BaseClass_linux(BaseClass):
        platform = 'Linux'
        distribution = None

    class BaseClass_linux_redhat(BaseClass_linux):
        distribution = 'Redhat'

    class BaseClass_linux_otherlinux(BaseClass_linux):
        distribution = 'OtherLinux'

    class BaseClass_linux_redhat_6(BaseClass_linux_redhat):
        distribution_version = '6'

    class BaseClass_linux_redhat_7(BaseClass_linux_redhat):
        distribution_version = '7'

    class BaseClass_aix(BaseClass):
        platform = 'AIX'
        distribution = None

    class BaseClass_other(BaseClass):
        platform = 'Other'
        distribution = None


# Generated at 2022-06-12 23:47:42.759905
# Unit test for function get_distribution
def test_get_distribution():
    test_platform_system = "Linux"
    test_distro_return = "Arch"
    test_distro_id = "Arch Linux"

    def _fake_distro_id():
        return test_distro_id

    old_distro_id = distro.id
    distro.id = _fake_distro_id
    old_platform_system = platform.system
    platform.system = lambda: test_platform_system

    assert get_distribution() == test_distro_return
    distro.id = old_distro_id
    platform.system = old_platform_system

# Generated at 2022-06-12 23:47:46.271061
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    ubuntu_codename = u'bionic'
    # On Ubuntu test should pass
    result = get_distribution_codename()
    assert result is not None
    assert result == ubuntu_codename, result

    # On Red Hat test should fail
    result = get_distribution_codename()
    assert result is None, result

# Generated at 2022-06-12 23:47:48.062119
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert distro.id() == 'debian'
    assert distro.codename() == 'stretch'
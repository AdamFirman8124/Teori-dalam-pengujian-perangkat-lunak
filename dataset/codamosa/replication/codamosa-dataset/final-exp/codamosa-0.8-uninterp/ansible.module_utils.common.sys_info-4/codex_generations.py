

# Generated at 2022-06-12 23:38:16.772228
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() in ('Centos', 'Redhat', 'Debian', 'Freebsd', 'Darwin', 'Openbsd', 'Sunos', 'Windows', 'Amazon')



# Generated at 2022-06-12 23:38:18.395665
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == u'Amazon', 'Platform is not Amazon'


# Generated at 2022-06-12 23:38:22.746805
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # Handle non-Linux case
    class FakeNonLinuxPlatform:
        def system(self):
            return 'Windows'
    real_platform = platform
    platform = FakeNonLinuxPlatform()

    # Call function
    result = get_distribution_codename()

    # Reset
    platform = real_platform
    assert result is None



# Generated at 2022-06-12 23:38:24.284848
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() is None
    assert get_distribution_codename() == distro.codename()

# Generated at 2022-06-12 23:38:28.656301
# Unit test for function get_distribution_version
def test_get_distribution_version():
    def test_distro_version(distro, version):
        yield lambda: distro.version() == version

    for d in [
        distro.CentOSLinux,
        distro.Debian,
        distro.openSUSELeap,
        distro.OracleLinux,
        distro.RedHatEnterpriseLinux,
    ]:
        yield test_distro_version(d, '6.8')
        yield test_distro_version(d, '7.2')
        yield test_distro_version(d, '8.0')
        yield test_distro_version(d, '8.1')
        yield test_distro_version(d, '8.2')
        yield test_distro_version(d, '8.3')


# Generated at 2022-06-12 23:38:39.281751
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Basic unit test to verify the distribution detection used in this module.
    '''
    # pylint: disable=unused-variable, unused-argument
    import pytest
    from ansible.module_utils._text import to_native


# Generated at 2022-06-12 23:38:50.899517
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # class to test platform specific subclass
    class A:
        platform = 'SunOS'
        distribution = None

    class A_Linux(A):
        platform = 'Linux'
        distribution = None

    class A_Solaris(A):
        platform = 'SunOS'
        distribution = 'Solaris'

    class A_Linux_Redhat(A_Linux):
        platform = 'Linux'
        distribution = 'Redhat'

    class A_Linux_Amazon(A_Linux):
        platform = 'Linux'
        distribution = 'Amazon'

    if platform.system() == 'Linux':
        distribution = get_distribution()
        if distribution == 'Redhat':
            assert get_platform_subclass(A) == A_Linux_Redhat

# Generated at 2022-06-12 23:39:00.397408
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class A:
        platform = 'Linux'
        distribution = None

    class B(A):
        distribution = None
        pass

    class C(B):
        distribution = None
        pass

    class D(C):
        distribution = None
        pass

    class E(D):
        distribution = 'Redhat'
        pass

    class F(D):
        distribution = 'Debian'
        pass

    class X:
        platform = 'FreeBSD'
        distribution = None
        pass

    class Z(X):
        pass

    # module A is linux, no distribution
    assert get_platform_subclass(A).__name__ == 'A'

    # module B is linux, no distribution
    assert get_platform_subclass(B).__name__ == 'B'

    # module C is linux, no distribution

# Generated at 2022-06-12 23:39:10.782327
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    ''' Unit tests for function get_platform_subclass(). '''

    class BaseModule:
        ''' Stub parent class. '''
        pass

    class SubModule1(BaseModule):
        ''' Stub sub-class 1. '''
        distribution = None

    class SubModule2(BaseModule):
        ''' Stub sub-class 2. '''
        distribution = None
        platform = 'Not the platform you are looking for'

    class SubModule3(BaseModule):
        ''' Stub sub-class 3. '''
        distribution = 'Fedora'
        platform = 'Linux'

    class SubModule4(BaseModule):
        ''' Stub sub-class 4. '''
        distribution = 'Debian'
        platform = 'Linux'

    class SubModule5(BaseModule):
        ''' Stub sub-class 5. '''


# Generated at 2022-06-12 23:39:17.578381
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Verify get_distribution_codename returns the correct codename for the current distribution
    '''
    os_distribution = get_distribution()

    # First check if the current OS is a linux distribution
    if os_distribution == "Linux":
        # Get the codename for the linux distribution
        os_codename = get_distribution_codename()

        # Check if codename is valid
        if not os_codename:
            return False

        # Check that the codename is correct for the distribution
        # The codename at this point is a string, so codename should be compared to the list of valid codenames

# Generated at 2022-06-12 23:39:25.739017
# Unit test for function get_distribution
def test_get_distribution():
    # Setup
    expected_distribution = get_distribution()

    # Testing
    actual_distribution = distro.id().capitalize()

    # Result
    assert actual_distribution == expected_distribution



# Generated at 2022-06-12 23:39:31.399929
# Unit test for function get_distribution_version
def test_get_distribution_version():
    from distutils.version import LooseVersion

    version = get_distribution_version()
    if type(version) == bytes:
        # python 2
        version = version.decode('utf-8')
    assert type(version) == unicode

    if get_distribution() in ('Debian', 'Raspbian'):
        # test that get_distribution_version() works with a debian-based distribution
        assert LooseVersion(version) >= LooseVersion('7')

# Generated at 2022-06-12 23:39:40.597956
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    # Tests for RHEL-class platforms
    os_release_rhel7 = {
        'name': 'Red Hat Enterprise Linux Server',
        'VERSION_ID': '7.5',
        'version': '7.5 (Maipo)',
        'version_id': '7.5',
    }

# Generated at 2022-06-12 23:39:52.575949
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import os
    import json
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w') as os_release_info_file:
        json.dump({'PRETTY_NAME':'Raspbian GNU/Linux 10 (buster)',
                   'NAME':'Raspbian GNU/Linux',
                   'VERSION_ID':'10',
                   'VERSION':'10 (buster)',
                   'ID':'raspbian',
                   'ID_LIKE':'debian',
                   'HOME_URL':'http://www.raspbian.org/',
                   'SUPPORT_URL':'http://www.raspbian.org/RaspbianForums',
                   'BUG_REPORT_URL':'http://www.raspbian.org/RaspbianBugs',
                   }, os_release_info_file)

# Generated at 2022-06-12 23:40:00.725277
# Unit test for function get_distribution_version
def test_get_distribution_version():
    distribution = get_distribution()

    assert get_distribution_version() is not None
    assert get_distribution_version() is not ''

    if distribution in ['Redhat', 'Centos', 'Fedora', 'Amazon']:
        assert get_distribution_version().split('.')[0] == '7'
    elif distribution == 'Debian':
        assert get_distribution_version().split('.')[0] == '9'
    elif distribution in ['Ubuntu', 'Linuxmint']:
        assert get_distribution_version().split('.')[0] == '16'

# Generated at 2022-06-12 23:40:08.027958
# Unit test for function get_distribution
def test_get_distribution():
    # CentOS / Red Hat Enterprise Linux / Oracle Linux
    distribution_name = get_distribution()
    assert distribution_name in [u'Centos', u'Redhat', u'OracleLinux']
    assert get_distribution_version() in [u'6.10', u'7.5.1804', u'7.6.1810', u'8.0']
    assert get_distribution_codename() is None

    # Debian
    distribution_name = get_distribution()
    assert distribution_name in [u'Debian']
    assert get_distribution_version() in [u'10']
    assert get_distribution_codename() in [u'buster']

    # Fedora
    distribution_name = get_distribution()
    assert distribution_name in [u'Fedora']
    assert get_distribution_version()

# Generated at 2022-06-12 23:40:19.618111
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Unit tests for AnsibleModule.get_distribution_codename.
    '''
    # patch distribution.id function call for different type of distribution names
    patch_distro_id = {
        'centos': 'centos',
        'sl': 'sl',
        'fedora': 'fedora',
        'ubuntu': 'ubuntu',
        'debian': 'debian',
        'opensuse': 'opensuse',
        'oracle': 'oracle',
    }
    patch_distro_codename = {
        'centos': 'centos',
        'sl': 'sl',
        'fedora': 'fedora',
        'ubuntu': 'xenial',
        'debian': 'stretch',
        'opensuse': 'opensuse',
        'oracle': 'oracle',
    }
   

# Generated at 2022-06-12 23:40:27.846712
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''Unit test for get_platform_subclass'''

    class TestClass:
        platform = None
        distribution = None

    class TestSubclassA(TestClass):
        pass

    class TestSubclassB(TestClass):
        platform = 'Linux'

    class TestSubclassC(TestClass):
        distribution = 'Fedora'

    class TestSubclassD(TestClass):
        platform = 'Linux'
        distribution = 'Fedora'

    class TestSubclassE(TestClass):
        platform = 'Linux'
        distribution = 'Fedora'

    class TestSubclassF(TestClass):
        platform = 'Linux'
        distribution = 'Fedora'

    class TestSubclassG(TestSubclassE):
        pass

    class TestSubclassH(TestSubclassF):
        pass


# Generated at 2022-06-12 23:40:39.135759
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    class Struct:
        def __init__(self, dict):
            self.__dict__.update(dict)

    # Test Ubuntu
    distro.id = lambda: 'ubuntu'
    distro.lsb_release_info = lambda: Struct({'codename': 'trusty'})
    assert get_distribution_codename() == 'trusty'

    # Test Fedora 28
    distro.os_release_info = lambda: Struct({'ubutnu_codename': None})
    distro.id = lambda: 'fedora'
    distro.codename = lambda: None
    assert get_distribution_codename() is None

    # Test Fedora 29
    distro.os_release_info = lambda: Struct({'ubutnu_codename': None, 'version_codename': 'Silverblue'})
    distro

# Generated at 2022-06-12 23:40:49.946164
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # Test distributions with known version formats
    # from distribution.version()
    rhel_version = get_distribution_version()
    # from distribution.version(best=True)
    rhel_version_best = distro.version(best=True)
    # from lsb_release_info().get('release')
    lsb_release_info = distro.lsb_release_info()
    lsb_version = lsb_release_info.get('release')
    # from os_release_info().get('version_id')
    os_release_info = distro.os_release_info()
    os_version = os_release_info.get('version_id')
    # from platform.version()
    platform_release = platform.version()

    assert rhel_version_best == lsb_version == os_version

# Generated at 2022-06-12 23:41:07.053043
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Test the get_distribution_version function
    '''
    import platform
    import distro

    def mock_distro_version(best=False):
        return '9.9'

    def mock_distro_id():
        return 'debian'

    platform.system = lambda: 'Linux'
    distro.version = mock_distro_version
    distro.id = mock_distro_id

    result = get_distribution_version()
    assert (result == '9')

# Generated at 2022-06-12 23:41:08.365956
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'xenial'

# Generated at 2022-06-12 23:41:16.065579
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Function to unit test the get_platform_subclass method
    '''

    class BaseClass:
        '''
        Base class for testing program
        '''
        platform = 'Linux'
        distribution = None

    class LinuxClass(BaseClass):
        '''
        Linux class for testing program
        '''
        platform = 'Linux'
        distribution = None

    class LinuxClassDistro(BaseClass):
        '''
        Linux class for testing program with distribution
        '''
        platform = 'Linux'
        distribution = 'LinuxMint'

    class MacClass(BaseClass):
        '''
        Mac class for testing program
        '''
        platform = 'Darwin'
        distribution = None

    returned_class = get_platform_subclass(BaseClass)

# Generated at 2022-06-12 23:41:27.801721
# Unit test for function get_distribution

# Generated at 2022-06-12 23:41:30.358289
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'xenial'

# Generated at 2022-06-12 23:41:40.768047
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import mock
    with mock.patch.object(distro, 'id', mock.MagicMock(return_value='ubuntu')):
        with mock.patch.object(distro, 'codename', mock.MagicMock(return_value='xenial')):
            assert get_distribution_codename() == 'xenial'
    with mock.patch.object(distro, 'id', mock.MagicMock(return_value='rhel')):
        with mock.patch.object(distro, 'codename', mock.MagicMock(return_value='Barracuda')):
            assert get_distribution_codename() == ''

# Generated at 2022-06-12 23:41:52.826091
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit test for function get_platform_subclass

    When using this function as a decorator, it works as a context manager.
    '''
    # Set up a class hierarchy
    class Parent(object):
        platform = None
        distribution = None
        def __str__(self):
            return "Parent()"
        @get_platform_subclass
        class ClassDecorator(Parent):
            pass
        @classmethod
        @get_platform_subclass
        def ClassMethodDecorator(cls):
            return cls

    class Child1(Parent):
        platform = 'XXX'
        def __str__(self):
            return "Subclass1()"
        @get_platform_subclass
        class ClassDecorator(Child1):
            pass

# Generated at 2022-06-12 23:41:56.098566
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    # In Ubuntu LTS 16.04, the codename is xenial which is the value we are expecting
    codename = get_distribution_codename()
    assert codename == "xenial"

# Generated at 2022-06-12 23:42:04.301732
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        platform = "Not a platform"
    class TestLinux(Base):
        platform = "Linux"
        distribution = "Not a distro"
    class TestRedhat(TestLinux):
        distribution = "Redhat"
        version = "Not a version"
        codename = "Not a codename"
    class TestRedhat56(TestRedhat):
        version = "5.6"
        codename = "Tikanga"
    class TestRedhat64(TestRedhat):
        version = "6.4"
        codename = "Santiago"

    import ansible_collections.ansible.community.tests.unit.module_utils.basic_utils
    import os
    import sys


# Generated at 2022-06-12 23:42:13.725063
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    platform_system = platform.system

    class TestBaseClass:
        platform = None
        distribution = None

    class TestSubClass(TestBaseClass):
        platform = 'Linux'
        distribution = None

    class TestSubClass1(TestBaseClass):
        platform = 'Linux'
        distribution = 'Redhat'

    class TestSubClass2(TestBaseClass):
        platform = 'Linux'
        distribution = 'Redhat'

    class TestSubClass3(TestBaseClass):
        platform = 'Linux'
        distribution = 'TEST'

    class TestSubClass4(TestBaseClass):
        platform = 'TEST'
        distribution = 'TEST'

    class TestSubClass5(TestBaseClass):
        platform = 'TEST'
        distribution = 'TEST'

    # Test Linux Redhat

# Generated at 2022-06-12 23:42:36.276015
# Unit test for function get_distribution
def test_get_distribution():
    # assert_equal does not handle unicode, so we need to assert the values ourselves
    assert 'windows' == get_distribution().lower()
    assert 'redhat' == get_distribution_version()

# Generated at 2022-06-12 23:42:47.562731
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Simple test for function get_platform_subclass
    '''
    import sys

    class MyClass:
        '''
        Class representing the superclass from which MySubclass1 and MySubclass2 are derived.
        The members of this class are not used so they are not defined.
        '''
        pass

    class MySubclass1(MyClass):
        '''
        Class representing a subclass of MyClass on a specific platform with a
        specific distribution.  If a subclass with a matching distribution is
        found, it is returned by get_platform_subclass.  If no subclass with a
        matching distribution is found, the class with the most specific platform
        is returned.
        '''
        platform = sys.platform
        distribution = 'Ubuntu'


# Generated at 2022-06-12 23:42:56.913412
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import sys
    class TestClass:
        platform = 'TestPlatform'
        distribution = None
        def __init__(self, testattribute):
            self.testattribute = testattribute
    class TestClassSubclass(TestClass):
        platform = 'TestPlatform'
        distribution = NotImplementedError
    class TestClassSubclassSubclass(TestClassSubclass):
        platform = 'TestPlatform'
        distribution = NotImplementedError

    testclass = TestClass('testattribute')
    testclasssubclass = TestClassSubclass('testattribute')

    # Test that this fails on Python 2
    if sys.version_info < (3,):
        try:
            get_platform_subclass(testclass)
        except TypeError:
            pass
        else:
            raise AssertionError('Failed to raise TypeError on Python 2')

# Generated at 2022-06-12 23:43:07.891342
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    assert('BsdUser' == get_platform_subclass(User).__name__)
    assert('LinuxUser' == get_platform_subclass(User, platform='Linux').__name__)
    assert('LinuxUser' == get_platform_subclass(User, distribution='Debian').__name__)
    assert('LinuxUser' == get_platform_subclass(User, distribution='Debian', platform='Linux').__name__)
    assert('LinuxSuseUser' == get_platform_subclass(User, distribution='Suse', platform='Linux').__name__)
    assert('LinuxUser' == get_platform_subclass(User, distribution='Ubuntu', platform='Linux').__name__)

# Generated at 2022-06-12 23:43:18.188898
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Basic unit test for the get_platform_subclass function
    '''

    # Set up a basic class hierarchy to test with
    class A(object):
        pass

    class B(A):
        pass

    # Set up a basic test class to test with
    class TestClass(object):
        platform = None
        distribution = None

    class TestSubclass(TestClass):
        platform = 'Linux'
        distribution = 'Something'

    class TestSubclass2(TestClass):
        platform = 'Linux'
        distribution = 'SomethingElse'

    class TestSubclass3(TestClass):
        platform = 'Windows'
        distribution = None

    # Make sure we get the base class if nothing else
    assert get_platform_subclass(TestClass) == TestClass

    # Test basic subclassing
    assert get_platform_

# Generated at 2022-06-12 23:43:22.122774
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class BasePlatform():
        platform = "Test"
        distribution = None

    class BaseDistro(BasePlatform):
        distribution = "Test"

    class SpecificDistro(BaseDistro):
        distribution = "SpecificTest"

    class OtherPlatform(BasePlatform):
        platform = "Other"

    class OtherDistro(BaseDistro):
        distribution = "Other"

    assert get_platform_subclass(BasePlatform) is BasePlatform
    assert get_platform_subclass(BaseDistro) is BasePlatform

# Generated at 2022-06-12 23:43:33.302290
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test to ensure get_platform_subclass() finds specific subclass on certain distributions
    '''
    this_platform = platform.system()

    if this_platform == 'Linux':
        distribution = get_distribution()
    else:
        distribution = None

    class BaseClass:
        pass

    # Test subclass without a specific distribution
    class TestClass(BaseClass):
        pass

    # Test subclass with a specific distribution
    class TestSubClass1(TestClass):
        distribution = 'Redhat'
        platform = 'Linux'

    class TestSubClass2(TestSubClass1):
        distribution = 'Redhat'
        platform = 'Linux'

    # Test subclass without Linux platform
    class TestSubClass3(TestClass):
        distribution = 'BSD'
        platform = 'BSD'

    # Test subclass with a specific Linux platform

# Generated at 2022-06-12 23:43:41.649390
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import os

    from ansible.module_utils.common.test_module_utils.fixtures import (
        ubuntu_release, ubuntu_os_release, centos_release, centos_os_release,
        centos_8_os_release, fedora_release, fedora_os_release
    )

    def run_test(distro_release, os_release, distro_id, version, codename):
        if os_release is not None:
            os_release_path = os.path.join(os.path.dirname(__file__), 'fixtures', os_release)
            os.environ['OS_RELEASE_PATH'] = os_release_path


# Generated at 2022-06-12 23:43:42.271209
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    pass

# Generated at 2022-06-12 23:43:51.811069
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        platform = None
        distribution = None
    class RedHat(Base):
        distribution = 'Redhat'
    class Debian(Base):
        distribution = 'Debian'
    class Debian6(Base):
        distribution = 'Debian'
        platform = 'Linux'
    class Darwin(Base):
        platform = 'Darwin'
    class Windows(Base):
        platform = 'Windows'
    class Suse(Base):
        platform = 'Linux'
        distribution = 'Suse'

    assert get_platform_subclass(Base).__name__ == 'Base'
    assert get_platform_subclass(RedHat).__name__ == 'RedHat'
    assert get_platform_subclass(Debian).__name__ == 'Debian'

# Generated at 2022-06-12 23:44:20.333598
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    #test class
    class TestPlatformSubclass:
        platform = 'Linux'

        class TestSubclass1(TestPlatformSubclass):
            distribution = 'Redhat'

        class TestSubclass2(TestPlatformSubclass):
            distribution = 'OtherLinux'

    class TestPlatformSubclass2:
        platform = 'SunOS'

        class TestSubclass3(TestPlatformSubclass2):
            pass

    # Set platform.system to return Linux
    def linux_version():
        return "2.6.18-308.el5"
    saved_version = platform.system
    platform.system = lambda: 'Linux'
    platform.linux_distribution = linux_version
    saved_distro_version = distro.id
    distro.id = linux_version

    # Set platform.system to return Redhat

# Generated at 2022-06-12 23:44:21.474140
# Unit test for function get_distribution
def test_get_distribution():
    distribution = get_distribution()
    assert distribution != None


# Generated at 2022-06-12 23:44:26.231222
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test the get_distribution() function
    '''
    assert get_distribution() == get_distribution()
    assert not get_distribution() == 'Redhat'
    assert get_distribution() != 'Redhat'
    assert get_distribution() == 'Redhat'


# Generated at 2022-06-12 23:44:31.982064
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    test_cases = [
        ('LinuxMint_18.2', 'sonya'),
        ('Ubuntu_16.04', 'xenial'),
        ('Ubuntu_14.04', 'trusty'),
        ('OEL_7.5', None),
        ('RHEL_7.6', None),
    ]

    for (test_dist, expected_codename) in test_cases:
        assert expected_codename == get_distribution_codename(), (
            "get_distribution_codename() should have returned %s when running %s but got %s"
            % (expected_codename, test_dist, get_distribution_codename())
        )

# Generated at 2022-06-12 23:44:44.406792
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Until we can have conditional dependencies, Mock is not available
    # on older releases of Ansible.  We use Pytest instead.  We may not
    # have a pytest fixture to run this test but it's better than nothing
    # so we'll fake one just so we can get some coverage on this.
    try:
        import pytest
        pytest.mark.module('This is a mock, nothing to test')
    except ImportError:
        pass

    import platform
    import ansible.module_utils.basic
    old_system = platform.system
    platform.system = lambda: 'Linux'
    import ansible.module_utils.basic

    class A:
        platform = 'Linux'
        distribution = 'Redhat'

    class B(A):
        distribution = 'Amazon'


# Generated at 2022-06-12 23:44:55.983075
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    tests = dict(
        os_release_codename='moonshine',
        lsb_release_codename='pipeline',
        ubuntu_codename='xenial',
        no_codename=None,
        empty_string=None,
        empty_list=[],
        empty_dict={},
        empty_set=set(),
    )

    for test, expected in tests.items():
        class FakeOSRelease:
            def __init__(self, test):
                self.test = test

            def get(self, var):
                if var == 'version_codename':
                    return self.test

        class FakeLsbRelease:
            def __init__(self, test):
                self.test = test

            def get(self, var):
                if var == 'codename':
                    return self.test

# Generated at 2022-06-12 23:44:58.980185
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test function get_distribution_codename()
    '''
    codename = get_distribution_codename()
    print(codename)


# Generated at 2022-06-12 23:45:08.304797
# Unit test for function get_distribution
def test_get_distribution():
    # Remove all elements from environ and set
    # distributions to test.
    # If a distribution isn't set, then distro.id()
    # defaults to the platform.system()
    # We don't want to run all tests on all distributions
    # but rather want to pick a specific distribution
    # If all distributions are tested, then the test
    # takes forever
    distribution_ids = ['redhat', 'centos', 'suse', 'debian', 'ubuntu', 'gentoo', 'fedora']
    distribution_ids_lower = [x.lower() for x in distribution_ids]
    modules_path = os.path.join(os.path.dirname(__file__), '..', '..', 'modules')


# Generated at 2022-06-12 23:45:13.169875
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Unit test for get_distribution
    '''
    my_platform = platform.system()
    my_distribution = get_distribution()
    if my_platform == 'Linux':
        if my_distribution not in ('RedHat', 'Centos', 'Fedora', 'Debian', 'Ubuntu'):
            assert False, "Distro %s not supported by unit test" % my_distribution
        else:
            assert True

# Generated at 2022-06-12 23:45:24.155912
# Unit test for function get_distribution
def test_get_distribution():
    expected = {
        'darwin': 'Macosx',
        'freebsd': 'Freebsd',
        'hp-ux': 'Hpux',
        'linux': get_distribution(),
        'netbsd': 'Netbsd',
        'openbsd': 'Openbsd',
        'openindiana': 'Openindiana',
        'opensolaris': 'Opensolaris',
        'opensuse': 'Opensuse',
        'oracle': get_distribution(),
        'sunos': 'Solaris',
    }

    platform_distro = platform.system().lower()

    if platform_distro in expected:
        assert expected[platform_distro] == get_distribution(), '%s != %s' % (expected[platform_distro], get_distribution())

# Generated at 2022-06-12 23:46:12.991454
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Unit test for function get_distribution_codename

    :rtype: None
    :returns: None
    '''
    # Test with OS release codename

# Generated at 2022-06-12 23:46:24.487894
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class base_class:
        pass

    class base_class_subclass1(base_class):
        platform = "A"
        distribution = None

    class base_class_subclass2(base_class):
        platform = "A"
        distribution = "B"

    class base_class_subclass3(base_class):
        platform = "A"
        distribution = "C"

    class base_class_subclass4(base_class):
        platform = "B"
        distribution = None

    class base_class_subclass5(base_class):
        platform = "B"
        distribution = "C"

    class base_class_subclass6(base_class):
        platform = "C"
        distribution = None

    class base_class_subclass7(base_class):
        platform = "C"

# Generated at 2022-06-12 23:46:25.822485
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() == '16.04'


# Generated at 2022-06-12 23:46:31.145102
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    codename = get_distribution_codename()

    # This is what we want when this function is ported to a module_utils.common
    # The object returned by get_platform_subclass() will be turned into its
    # string representation by pprint which just uses __str__.  We want to make
    # sure we return a string and not None.
    if codename is None:
        codename = ""

    assert codename is not None
    assert codename is not ""

# Generated at 2022-06-12 23:46:36.989444
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test module function ``get_distribution``
    '''
    expected_distribution_map = {
        'centos': u'CentOS',
        'debian': u'Debian',
        'fedora': u'Fedora',
        'mock': u'Mock',
        'redhat': u'RedHat',
        'ubuntu': u'Ubuntu',
        'unknown': u'unknown',
        'unittest': u'Unittest',
    }

    for special_distro in expected_distribution_map:
        distro.name = lambda: special_distro
        this_distribution = get_distribution()

# Generated at 2022-06-12 23:46:45.253794
# Unit test for function get_distribution
def test_get_distribution():
    import platform

    distributions = [
        ('centos', 'Linux', 'CentOS'),
        ('linuxmint', 'Linux', 'Linuxmint'),
        ('amazon', 'Linux', 'Amazon'),
        ('redhat', 'Linux', 'Redhat'),
        ('ubuntu', 'Linux', 'Ubuntu'),
        ('freebsd', 'FreeBSD', 'FreeBSD'),
        ('netbsd', 'NetBSD', 'NetBSD'),
        ('openbsd', 'OpenBSD', 'OpenBSD'),
        ('darwin', 'Darwin', 'Darwin'),
        ('sunos5', 'SunOS', 'Solaris'),
    ]

    for os_name, system, distro in distributions:
        platform.system = lambda: system
        distro.id = lambda: os_name
        assert get_distribution() == distro

# Generated at 2022-06-12 23:46:56.685049
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.basic import AnsibleModule as AM
    from ansible.module_utils.basic import AnsibleModule, get_platform_subclass

    class A:
        platform = "Linux"
        distribution = None

    class B:
        platform = "Linux"
        distribution = "CentOS"

    class C:
        platform = "Linux"
        distribution = "RedHat"

    class D:
        platform = "FreeBSD"
        distribution = None

    class E:
        platform = "FreeBSD"
        distribution = "FreeBSD"

    class F(AM):
        platform = "Linux"
        distribution = "Fedora"

    class G(AM):
        platform = "Linux"
        distribution = "RedHat"

    class H(AM):
        platform = "Linux"
        distribution = None



# Generated at 2022-06-12 23:47:07.122202
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test the definition and use of get_platform_subclass().  Python's unit test framework
    needs the test class to be defined in this file, so this has been given a leading underscore
    and is not imported into the platform module (__init__.py).
    '''
    class TestModule:
        '''
        Test class.  This class should be used as the place to define a test.  The
        actual test classes will be created dynamically.  Each test class will have
        a long name that is based on the name of the subclass and the platform it runs on.
        '''


# Generated at 2022-06-12 23:47:14.797976
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    """
    This function tests get_platform_subclass function.

    """

    class Base:
        platform = 'Linux'
        distribution = None

    class RedHat(Base):
        distribution = 'RedHat'

    class Fedora(RedHat):
        distribution = 'Fedora'

    class OtherLinux(Base):
        distribution = 'OtherLinux'

    class OtherBase:
        platform = None
        distribution = None

    class OtherDistro(OtherBase):
        platform = 'Linux'
        distribution = 'OtherDistro'

    class Other(OtherBase):
        platform = 'BSD'

    assert get_platform_subclass(Base) == Base
    assert get_platform_subclass(RedHat) == RedHat
    assert get_platform_subclass(Fedora) == Fedora

# Generated at 2022-06-12 23:47:24.478100
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # Fedora
    for line in open('/etc/os-release', 'r'):
        if 'VERSION_CODENAME' in line:
            match = line.replace('"', '').replace('\n', '').split('=')[1]
            codename = get_distribution_codename()
            assert codename == match
            return

    # Debian
    for line in open('/etc/os-release', 'r'):
        if 'VERSION_CODENAME' in line:
            match = line.replace('"', '').replace('\n', '').split('=')[1]
            codename = get_distribution_codename()
            assert codename == match
            return
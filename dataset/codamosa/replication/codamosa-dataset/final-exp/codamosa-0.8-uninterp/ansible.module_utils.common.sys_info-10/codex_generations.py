

# Generated at 2022-06-12 23:38:12.296531
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    codename = get_distribution_codename()
    # assert if codename is None or not
    assert codename is not None, "get_distribution_codename() failed to return codename"


# Generated at 2022-06-12 23:38:23.447575
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit test for module_utils.facts.get_platform_subclass
    '''
    import unittest

    class Foo(object):
        pass

    class FooLinux(Foo):
        platform = 'Linux'

    class FooLinuxRedhat(FooLinux):
        distribution = 'Redhat'

    class FooLinuxOtherLinux(FooLinux):
        distribution = 'OtherLinux'

    class FooLinuxAmazon(FooLinux):
        distribution = 'Amazon'

    class FooDarwin(Foo):
        platform = 'Darwin'

    class FooDarwinOtherOS(FooDarwin):
        distribution = 'OtherLinux'

    class FooDarwinOSX(FooDarwin):
        distribution = 'OSX'


# Generated at 2022-06-12 23:38:35.336282
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    # author the tests in a way that makes it easy to see what we're testing
    # and to help avoid typos in the names of the subclasses
    class Base:
        pass

    class SubclassA(Base):
        distribution = "DistributionName"
        platform = "PlatformName"

    class SubclassB(Base):
        distribution = "OtherDistributionName"
        platform = "OtherPlatformName"

    class SubclassC(Base):
        distribution = None
        platform = "OtherPlatformName"

    class SubclassD(Base):
        distribution = "OtherDistributionName"
        platform = None

    class SubclassE(Base):
        distribution = None
        platform = None


    this_platform = "PlatformName"
    other_platform = "OtherPlatformName"
    distribution = "DistributionName"
    other_distribution

# Generated at 2022-06-12 23:38:47.298283
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit test for get_platform_subclass
    '''
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    # Basic test, returns itself
    subclass = get_platform_subclass(DistributionFactCollector)
    assert subclass == DistributionFactCollector

    # Basic test, returns default subclass
    class MockDistribution:
        @property
        def id(self):
            return u'mock'

    with patch('ansible.module_utils.facts.system.distribution.platform', new=MockPlatform()):
        with patch('ansible.module_utils.facts.system.distribution.distro', new=MockDistribution()):
            subclass = get_platform_subclass(DistributionFactCollector)
            assert subclass == DistributionFactCollector

    # Basic test, returns subclass

# Generated at 2022-06-12 23:38:48.051113
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'xenial'

# Generated at 2022-06-12 23:38:58.515580
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    os_release_info = {}
    if platform.system() == 'Darwin':
        # On OSX, have to manually override the values returned because the
        # distro library reads from /etc/os-release
        os_release_info = {'id': 'debian', 'name': 'Mac OS X'}
        # Issue a warning if a different value is returned on the CI
        # infrastructure
        if get_distribution_codename() not in (None, 'elcapitan'):
            assert False, 'Unknown return value of %s on Mac OS X' % get_distribution_codename()

# Generated at 2022-06-12 23:39:02.876678
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Unit test of function get_distribution_version

    :rtype: bool
    :returns: True on success
    '''
    # Arrange
    expected_distribution_version = '7.5'
    expected_distribution_id = 'centos'

    # Act
    distribution_version = get_distribution_version()
    distribution_id = distro.id()

    # Assert
    assert distribution_id == expected_distribution_id
    assert distribution_version == expected_distribution_version

# Generated at 2022-06-12 23:39:11.461504
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        name = 'A'
        platform = None
        distribution = None
        def get_data(self):
            return self.name

    class B:
        name = 'B'
        platform = 'Linux'
        distribution = 'Centos'
        def get_data(self):
            return self.name

    class C:
        name = 'C'
        platform = 'Linux'
        distribution = None
        def get_data(self):
            return self.name

    # On a non-linux platform
    class D(A):
        name = 'D'

    # On a linux platform, with a matching distro
    class E(B):
        name = 'E'

    F = get_platform_subclass(A)
    assert F == D

    F = get_platform_subclass(B)

# Generated at 2022-06-12 23:39:19.873856
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Tests for the get_distribution_codename() function
    '''
    # Test on a base Ubuntu Linux install and record output
    distribution_codename = get_distribution_codename()

    # Test that the output is not blank and print info
    assert distribution_codename != "", "The distribution_codename function output is blank"
    assert distribution_codename is not None, "The distribution_codename function output is None"
    print(u"Testing get_distribution_codename using: {}".format(distribution_codename))

    # Test on an Ubuntu Linux install with a different codename and record output
    distribution_codename = get_distribution_codename()

    # Test that the output is not blank and print info
    assert distribution_codename != "", "The distribution_codename function output is blank"
   

# Generated at 2022-06-12 23:39:23.490815
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        pass

    class BaseLinux(Base):
        platform = 'Linux'

    class RedhatLinux(BaseLinux):
        distribution = 'Redhat'

    assert issubclass(get_platform_subclass(BaseLinux), RedhatLinux)

# Generated at 2022-06-12 23:39:42.256188
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import ansible.module_utils.basic
    import ansible.module_utils.facts
    import ansible.module_utils.facts.system.distribution

    # Define a platform subclass for unit testing
    class Dummy(ansible.module_utils.facts.system.distribution.Distribution):
        platform = platform.system().lower()
        distribution = None

    # Note we need to use get_all_subclasses because the unit test will be
    # running the imported module and not the local code.
    import_module_subclasses = get_all_subclasses(ansible.module_utils.facts.system.distribution.Distribution)
    # make sure the Dummy subclass is not already in the list
    assert Dummy not in import_module_subclasses

    # Get the subclass
    dummy_subclass = get_platform_subclass

# Generated at 2022-06-12 23:39:44.709017
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import sys
    import os
    import tempfile


# Generated at 2022-06-12 23:39:55.470927
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    :avocado: tags=unit
    '''
    # Some tests that are based on existing Linux distributions.
    # The tests in this section will only run on Linux because that is the
    # only valid system to be testing.
    if platform.system() == 'Linux':
        # Fedora only has major and minor numbers in /etc/os-release
        assert get_distribution_version() == u'18'
        assert get_distribution_version() == u'18'

        # Debian only has major and minor numbers but they are in the
        # /etc/debian_version file
        assert get_distribution_version() == u'8'

        # Ubuntu only has major and minor numbers but they are in the
        # /etc/lsb-release file
        assert get_distribution_version() == u'16.04'

       

# Generated at 2022-06-12 23:40:04.769256
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # Test for Debian
    def test_on_debian():
        # Mock distro.id() to return 'debian'
        distro_id_mock = distro.id
        distro.id = lambda: 'debian'

        # Mock the distro.os_release_info() to return os-release data file
        os_release_info_mock = distro.os_release_info
        distro.os_release_info = lambda: {"PRETTY_NAME": "Debian GNU/Linux 8 (jessie)", 'VERSION_ID': '8', 'HOME_URL': 'http://www.debian.org/', 'SUPPORT_URL': 'http://www.debian.org/support', 'BUG_REPORT_URL': 'https://bugs.debian.org/'}

        # Test the function
        assert get_distribution_

# Generated at 2022-06-12 23:40:17.643431
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import collections

    class SuperClass(object):
        '''
        Superclass for the purpose of unit testing
        '''

        platform = None
        distribution = None

        def __init__(self, **kwargs):
            self.from_super = kwargs.get('from_super', True)

    class OtherPlatform(SuperClass):

        platform = 'sunos'
        distribution = 'Solaris'

        def __init__(self, **kwargs):
            self.from_otherplatform = kwargs.get('from_otherplatform', True)
            super(OtherPlatform, self).__init__(**kwargs)

    class Linux(SuperClass):
        platform = 'linux'

        def __init__(self, **kwargs):
            self.from_linux = kwargs.get('from_linux', True)
           

# Generated at 2022-06-12 23:40:26.926753
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Unit test for get_distribution_codename()
    '''
    import sys
    import unittest
    import unittest.mock as mock
    from contextlib import ExitStack

    module_patcher = ExitStack()
    module_patcher.enter_context(mock.patch('ansible.module_utils.distro._distro', new=mock.Mock(return_value='LinuxMock')))
    # Return a generic os_release_info so the code tests for multiple codenames
    def mock_os_release_info():
        return {'version_codename': 'test', 'ubuntu_codename': 'test', 'test': 'test'}

# Generated at 2022-06-12 23:40:38.525446
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    _platform = platform.system()
    _distribution = get_distribution()

    class DummySuperClass(object):
        ''' Dummy base class for testing get_platform_subclass '''
        __metaclass__ = type

    class DummySuperClass2(DummySuperClass):
        ''' Dummy subclass for testing get_platform_subclass '''
        platform = None
        distribution = None

    class DummySuperClass3(DummySuperClass):
        ''' Dummy subclass for testing get_platform_subclass '''
        platform = None
        distribution = _distribution

    class DummySuperClass4(DummySuperClass):
        ''' Dummy subclass for testing get_platform_subclass '''
        platform = _platform
        distribution = None


# Generated at 2022-06-12 23:40:49.545358
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class A:
        platform = 'darwin'
        distribution = None

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        platform = 'linux'
        distribution = 'centos'

    class E(A):
        platform = 'linux'

    class F(E):
        distribution = 'redhat'

    class G(E):
        distribution = 'centos'

    class H(F):
        platform = 'solaris'

    class I(D):
        platform = 'windows'

    assert get_platform_subclass(A) is A
    assert get_platform_subclass(B) is B
    assert get_platform_subclass(C) is C
    assert get_platform_subclass(D) is D

# Generated at 2022-06-12 23:40:55.386762
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    # Set up the environment
    old_platform = platform.system
    old_distribution = get_distribution
    platform.system = lambda: "Linux"
    get_distribution = lambda: "Amazon"

    # Test + verify
    try:
        assert get_platform_subclass(A) == A
        assert get_platform_subclass(B) == B
        assert get_platform_subclass(C) == C
        assert get_platform_subclass(D) == E
        assert get_platform_subclass(F) == E
        assert get_platform_subclass(G) == E
    finally:
        # Restore the environment
        platform.system = old_platform
        get_distribution = old_distribution


# Dummy classes for unit test for function get_platform_subclass

# Generated at 2022-06-12 23:41:02.138895
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Test function to get the version of the distribution the code is running on
    '''

    # CentOS
    version = get_distribution_version()
    if version is not None:
        assert version in ['6.10', '7.5', '8.0']
    else:
        assert True

    # Ubuntu
    version = get_distribution_version()
    if version is not None:
        assert version in ['14.04', '18.04', '20.04']
    else:
        assert True



# Generated at 2022-06-12 23:41:19.903881
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Provides Unit Tests for the get_distribution_codename function
    '''
    # In this Unit test it tests get_distribution_codename by
    # running through different versions of /etc/os-release
    os_release_file = open('/etc/os-release')
    os_release = os_release_file.read()
    os_release_file.close()

    # This line tests whether get_distribution_codename works if
    # the os-release file contains both the codename variable
    # and the variable version_codename
    os_release_file = open('/etc/os-release', 'w')

# Generated at 2022-06-12 23:41:29.825491
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    mock_lsbrelease_info = {
        'codename': 'bionic'
    }
    mock_os_release_info = {
        'version_codename': 'xenial',
        'ubuntu_codename': 'xenial'
    }

    try:
        old_lsb_release_info = distro._lsb_release_info
        old_os_release_info = distro._os_release_info
        distro._lsb_release_info = mock_lsbrelease_info
        distro._os_release_info = mock_os_release_info
        assert get_distribution_codename() == 'bionic'
    finally:
        distro._lsb_release_info = old_lsb_release_info
        distro._os_release_info = old_os_release_

# Generated at 2022-06-12 23:41:34.391196
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    unit test for function get_distribution_codename
    '''

    # check if function returns None when not a Linux distro
    assert get_distribution_codename() is None

    # check if function returns codename when on a Linux distro
    assert get_distribution_codename() == 'xenial'

# Generated at 2022-06-12 23:41:35.559709
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() is None

# Generated at 2022-06-12 23:41:44.080876
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    expected = {
        u'alpine': u'edge',
        u'centos': u'Core',
        u'debian': None,
        u'fedora': u'Rawhide',
        u'oracle': u'7.5',
        u'rhel': u'Maipo',
        u'ubuntu': u'xenial',
    }

    actual = {}
    for distro_id in expected:
        # distro.id() is the name of the module which is not the same as the
        # distribution id
        if distro_id == u'alpine':
            distro_id = u'alpine_linux'
        elif distro_id == u'debian':
            distro_id = u'debian_linux'

# Generated at 2022-06-12 23:41:56.645128
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    tests = (
        ('Ubuntu', 'xenial'),
        ('Ubuntu', 'bionic'),
        ('Amazon', '2'),
        ('CentOS', '7.6.1810'),
        ('CentOS', '8.0.1905'),
        ('Fedora', '30'),  # code name starting with 30
        ('Fedora', '31'),
        ('Redhat', '6'),
        ('Redhat', '7'),
        ('Debian', '8'),
        ('Debian', '9'),
        ('Debian', '10'),
    )

    for distro, version in tests:
        distro_id = lambda: distro
        distro_version = lambda: version
        codename = get_distribution_codename()

# Generated at 2022-06-12 23:42:04.615424
# Unit test for function get_distribution
def test_get_distribution():
    # CloudLinux 6.7
    distro.id = lambda: u'cloudlinux'
    distro.like = lambda *args, **kwargs: [u'rhel']
    assert get_distribution() == u'CloudLinux'
    # Fedora 25
    distro.id = lambda: u'fedora'
    distro.version = lambda *args, **kwargs: u'25'
    assert get_distribution() == u'Fedora'
    # CentOS 7.5.1804
    distro.id = lambda: u'centos'
    distro.version = lambda *args, **kwargs: u'7.5.1804'
    assert get_distribution() == u'Centos'
    # Ubuntu 14.04.3 LTS
    distro.id = lambda: u'ubuntu'

# Generated at 2022-06-12 23:42:12.567142
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    distro_names = {
        "Fedora": "n/a",
        "Debian": "stretch",
        "Ubuntu": "xenial",
        "CentOS": "n/a",
        "openSUSE": "Leap"
    }

    # check if the codename of distribution is equal to the value
    for key, value in distro_names.items():
        assert get_distribution_codename() == value,\
            "Incorrect distribution code name for %s" % key

# Generated at 2022-06-12 23:42:22.482956
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    ubuntu_xenial_xerus = {'ID': 'ubuntu', 'VERSION_ID': '16.04',
        'VERSION': '16.04', 'VERSION_CODENAME': 'xenial',
        'UBUNTU_CODENAME': 'xenial'}
    ubuntu_bionic_beaver = {'ID': 'ubuntu', 'VERSION_ID': '18.04',
        'VERSION': '18.04', 'VERSION_CODENAME': 'bionic',
        'UBUNTU_CODENAME': 'bionic'}

# Generated at 2022-06-12 23:42:31.870556
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit test for get_platform_subclass.
    '''
    class Linux:
        platform = "Linux"
    class RedHat(Linux):
        distribution = "RedHat"
    class Debian(Linux):
        distribution = "Debian"
    class Fedora(Linux):
        distribution = "Fedora"
    class Windows:
        platform = "Windows"
    class Darwin:
        platform = "Darwin"
    class BSD:
        platform = "BSD"
    class RedHatWithSubClass(RedHat):
        distribution = "RedHat"
    class DebianWithSubClass(Debian):
        distribution = "Debian"
    class RedHatWithSubSubClass(RedHatWithSubClass):
        distribution = "RedHat"

# Generated at 2022-06-12 23:42:58.835683
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # test_linux_distro_get_distribution_version
    assert get_distribution_version() == '12.04'

    # test_linux_distro_get_distribution_version_future
    assert get_distribution_version() == '12.04'

    # test_linux_distro_get_distribution_version_centos
    assert get_distribution_version() == '7.4'

    # test_linux_distro_get_distribution_version_centos_future
    assert get_distribution_version() == '7.4'

    # test_linux_distro_get_distribution_version_redhat
    assert get_distribution_version() == '7.4'

    # test_linux_distro_get_distribution_version_amazon
    assert get_distribution_version

# Generated at 2022-06-12 23:43:09.191096
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Create two class hierarchies, one with Linux and the other with Windows
    class BasicClass:
        platform = None
        distribution = None
    class LinuxClass(BasicClass):
        platform = u'Linux'
    class DebianClass(LinuxClass):
        distribution = u'Debian'
    class OpenSuseClass(LinuxClass):
        distribution = u'OpenSUSE'
    class WindowsClass(BasicClass):
        platform = u'Windows'

    # Test actual Linux distro
    assert get_platform_subclass(BasicClass) == LinuxClass
    assert get_platform_subclass(LinuxClass) == LinuxClass
    assert get_platform_subclass(DebianClass) == DebianClass
    assert get_platform_subclass(OpenSuseClass) == OpenSuseClass

    # Test fake Linux distro

# Generated at 2022-06-12 23:43:18.529496
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test ``get_distribution()`` works properly
    '''
    import sys

    if sys.version_info.major >= 3 and sys.version_info.minor >= 5:
        assert get_distribution() in (u'Amazon', u'Arch', u'Debian', u'Fedora', u'Redhat', u'Solaris', u'Sles', u'Ubuntu', u'Windows', u'OtherLinux')
    else:
        # If Python < 3.5, the distro library fails to identify the OS on Fedora
        assert get_distribution() in (u'Amazon', u'Arch', u'Debian', u'Solaris', u'Sles', u'Ubuntu', u'Windows', u'OtherLinux')

# Generated at 2022-06-12 23:43:19.385954
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Freebsd'


# Generated at 2022-06-12 23:43:25.726940
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class One(object):
        distribution = "TestDistro"
        platform = "TestPlatform"

    class Two(One):
        distribution = "OtherDistro"
        platform = "OtherPlatform"

    class Three(One):
        distribution = "TestDistro"
        platform = "OtherPlatform"

    class Four(object):
        distribution = "OtherDistro"
        platform = "OtherPlatform"

    class Four1(Four):
        distribution = "OtherDistro"
        platform = "OtherPlatform"

    class Five(object):
        distribution = "TestDistro"
        platform = "OtherPlatform"

    class Five1(Five):
        distribution = "TestDistro"
        platform = "OtherPlatform"

    class Six(object):
        pass

    def get_distribution():
        return "TestDistro"


# Generated at 2022-06-12 23:43:28.496494
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    codename = get_distribution_codename()

    if platform.system() == 'Linux':
        assert codename is not None

# Generated at 2022-06-12 23:43:36.746371
# Unit test for function get_distribution
def test_get_distribution():
    # Detect the distribution the test is running on
    distribution = get_distribution()

    if distribution is None:
        print("This test can only be run on a Linux distribution")
        exit(1)

    # Construct the platform name the code is running on
    if distribution == 'OtherLinux':
        this_platform = 'Linux'
    else:
        this_platform = distribution

    # Check if the distribution name is correct
    if this_platform.lower() not in distro.id().lower():
        print("Distribution name {0} does not contain expected value {1}".format(distro.id(), this_platform))
        exit(1)

# Generated at 2022-06-12 23:43:39.038400
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'xenial'


# Generated at 2022-06-12 23:43:42.988793
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    if platform.system() == 'Linux':
        codename = get_distribution_codename()
        assert codename == distro.codename()
    else:
        codename = get_distribution_codename()
        assert codename == None

# Generated at 2022-06-12 23:43:47.356398
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    codename = get_distribution_codename()
    if codename is None:
        print('Skipped test_get_distribution_codename on %s.' % platform.system())
    else:
        print('Test for get_distribution_codename on %s returned %s.' % (platform.system(), codename))


# Generated at 2022-06-12 23:44:37.417020
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # Patch distro.id() to return a Linux distribution
    distro_id = 'CentOS'
    distro_version = '7.6.1810'
    distro.id = lambda: distro_id
    distro.version = lambda best=False: distro_version
    distro.version.__name__ = 'version'

    # Validate that the version is returned
    assert get_distribution_version() == distro_version


# Generated at 2022-06-12 23:44:47.271116
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        '''
        .. versionadded:: 2.12
        .. versionchanged:: 2.13
        '''
        platform = 'Linux'
        distribution = None

    class B:
        '''
        .. versionadded:: 2.12
        '''
        platform = 'Linux'
        distribution = 'Redhat'

    class C:
        '''
        .. versionchanged:: 2.13
        '''
        platform = 'Linux'
        distribution = 'Fedora'

    class D:
        platform = 'FreeBSD'
        distribution = None

    class E:
        platform = 'FreeBSD'
        distribution = 'FreeBSD'

    class F:
        platform = 'Darwin'
        distribution = None

    class G:
        platform = 'Darwin'
        distribution = 'MacOSX'


# Generated at 2022-06-12 23:44:58.343419
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    distribution = get_distribution()
    this_platform = platform.system()

    class generic1:
        distribution = None
        platform = this_platform
    class generic2:
        distribution = None
        platform = this_platform
    class generic3:
        distribution = None
        platform = 'Linux'
    class osx1:
        distribution = None
        platform = 'Darwin'
    class osx2:
        distribution = None
        platform = 'Darwin'
    class nonlinux1:
        distribution = None
        platform = 'SunOS'
    class nonlinux2:
        distribution = None
        platform = 'NonLinux'
    class linux1:
        distribution = distribution
        platform = 'Linux'
    class linux2:
        distribution = distribution
        platform = 'Linux'


# Generated at 2022-06-12 23:45:03.263559
# Unit test for function get_distribution
def test_get_distribution():
    old_name = platform.uname()[0]
    platform.system = lambda x=None: 'Linux'
    distro.id = lambda x=None: 'OtherLinux'
    assert get_distribution() == 'OtherLinux'
    platform.system = lambda x=None: old_name
    distro.id = lambda x=None: old_name


# Generated at 2022-06-12 23:45:11.008437
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import ansible_collections.community.general.plugins.modules.system.user
    import ansible_collections.community.general.plugins.modules.system.user_bsd
    import ansible_collections.community.general.plugins.modules.system.user_linux

    # test a success case
    result_cls = get_platform_subclass(ansible_collections.community.general.plugins.modules.system.user.User)
    # if this gets 3 of 3, that means the subclass worked
    assert result_cls is ansible_collections.community.general.plugins.modules.system.user_linux.UserLinux

    # test a class that does not have a subclass for this platform

# Generated at 2022-06-12 23:45:18.594940
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class BaseUser:
        platform = None
        distribution = None

    class LinuxUser(BaseUser):
        platform = "Linux"
        distribution = None

    class OtherLinuxUser(LinuxUser):
        distribution = "OtherLinux"

    class CentOSUser(LinuxUser):
        distribution = "Centos"

    class DarwinUser(BaseUser):
        platform = 'Darwin'
        distribution = None

    # Tests
    assert CentOSUser == get_platform_subclass(BaseUser)
    assert LinuxUser == get_platform_subclass(LinuxUser)
    assert LinuxUser == get_platform_subclass(OtherLinuxUser)
    assert DarwinUser == get_platform_subclass(DarwinUser)
    assert DarwinUser == get_platform_subclass(CentOSUser)


# Unit tests for function get_distribution

# Generated at 2022-06-12 23:45:23.309839
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    # Create classes for testing
    class Base(object):
        platform = 'Linux'
        distribution = None

    class RHEL(Base):
        distribution = 'Redhat'

    class CentOS(RHEL):
        distribution = 'Centos'

    class Debian(Base):
        distribution = 'Debian'

    # Get the FreeBSD class
    FreeBSD = get_platform_subclass(Base)

    # Get Linux classes
    Linux = get_platform_subclass(Base)
    RHEL_linux = get_platform_subclass(RHEL)
    Debian_linux = get_platform_subclass(Debian)

    # Test that our classes are what we expect
    assert Base == Linux
    assert Base == FreeBSD
    assert RHEL == RHEL_linux
    assert Debian == Debian_linux

# Generated at 2022-06-12 23:45:33.891548
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.basic import AnsibleModule

    # setup test data
    class Linux(object):
        platform = 'Linux'
        distribution = None

    class RedHat(Linux):
        distribution = 'RedHat'

    class RedHatFamily(Linux):
        distribution = 'RedHat'

    class Amazon(Linux):
        distribution = 'Amazon'

    class CentOS(RedHatFamily):
        pass

    class Fedora(RedHatFamily):
        pass

    class BSD(object):
        platform = 'Pugix'
        distribution = None

    class Solaris(object):
        platform = 'SunOS'
        distribution = None

    class AIX(object):
        platform = 'AIX'
        distribution = None

    class HPE(object):
        platform = 'HP-UX'
        distribution = None


# Generated at 2022-06-12 23:45:42.248104
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Ensure that we get the proper code name for our distributions
    '''

# Generated at 2022-06-12 23:45:43.846017
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename()

# Generated at 2022-06-12 23:47:11.350724
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() is None
    
    

# Generated at 2022-06-12 23:47:13.137269
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Unit test function for function get_distribution_codename
    '''
    assert get_distribution_codename() is None

# Generated at 2022-06-12 23:47:22.980725
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Foo:
        pass

    class Bar(Foo):
        platform = 'Linux'
        distribution = 'CentOS'

    class Baz(Foo):
        platform = 'Linux'
        distribution = 'RedHat'

    class OtherLinux(Foo):
        platform = 'Linux'
        distribution = None

    class OtherPlatform(Foo):
        platform = None
        distribution = None

    class NotLinux(Foo):
        platform = 'Windows'
        distribution = None

    # on Fedora we get 'Redhat'
    assert get_platform_subclass(Foo) == OtherLinux
    assert get_platform_subclass(Foo) == get_platform_subclass(Bar)
    assert get_platform_subclass(Foo) == get_platform_subclass(Baz)

# Generated at 2022-06-12 23:47:27.510582
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        pass
    class Subclass(Base):
        platform = 'Linux'
        distribution = 'RedHat'
    class Subclass2(Base):
        platform = 'Linux'
        distribution = 'OtherLinux'
    class Subclass3(Base):
        platform = 'Linux'
        distribution = None
    class Subclass4(Base):
        platform = 'Other'
        distribution = None

    assert get_platform_subclass(Base) == Base
    assert get_platform_subclass(Subclass) == Subclass
    assert get_platform_subclass(Subclass2) == Subclass2
    assert get_platform_subclass(Subclass3) == Base
    assert get_platform_subclass(Subclass4) == Base

# Generated at 2022-06-12 23:47:35.968346
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # Test Ubuntu Xenial Xerus
    platform.system = lambda: 'Linux'
    distro.id = lambda: 'ubuntu'
    distro.os_release_info = lambda: {}
    distro.lsb_release_info = lambda: {'codename': 'xenial'}
    codename = get_distribution_codename()
    assert codename == 'xenial', 'Expected codename "xenial", got {0}'.format(codename)

    # Test Ubuntu Bionic Beaver - Xenial Xerus via /etc/os-release
    distro.os_release_info = lambda: {'version_codename': 'bionic'}
    codename = get_distribution_codename()

# Generated at 2022-06-12 23:47:44.500606
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    """
    Verify correct class returned for supported platforms
    """

    class PlatformGeneric:
        platform = None
        distribution = None

    class PlatformGenericDist(PlatformGeneric):
        platform = None
        distribution = 'Generic'

    class PlatformSpecificGeneric(PlatformGeneric):
        platform = 'Specific'
        distribution = None

    class PlatformSpecificSpecific(PlatformGeneric):
        platform = 'Specific'
        distribution = 'Specific'

    assert get_platform_subclass(PlatformGeneric) == PlatformGeneric
    assert get_platform_subclass(PlatformGenericDist) == PlatformGenericDist

    selected_platform = get_platform_subclass(PlatformSpecificSpecific)
    assert selected_platform in (PlatformSpecificSpecific, PlatformSpecificGeneric)
    if selected_platform == PlatformSpecificSpecific:
        assert selected_platform.distribution == 'Specific'

    selected_platform = get_platform_

# Generated at 2022-06-12 23:47:54.645120
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Test function get_distribution_version()
    '''
    from ansible.module_utils.basic import AnsibleModule

    def _test_get_distribution_version(version, expected_value):
        '''
        Mock distro.version() and call get_distribution_version()
        '''
        old_distro_version = distro.version

        distro.version = lambda best=False: version

        distro_version = get_distribution_version()
        assert distro_version == expected_value

        distro.version = old_distro_version

    # Invalid version
    _test_get_distribution_version(None, '')

    # Major version only
    _test_get_distribution_version('7', '7')

    # Major and minor version
    _test_get_

# Generated at 2022-06-12 23:48:04.468730
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    # Define a dummy module definition as a base class
    class AnsibleModule:
        # For testing purposes we need to differentiate between the
        # original module class, and the subclass.
        original_module_class = True

        # A dummy argument for testing args / kwargs
        args = {}

        # A dummy class for testing inheritance
        def __init__(cls, args, kwargs):
            cls.args = args
            cls.kwargs = kwargs
            return

        # A dummy function for testing self
        def dummy_function(self):
            return "This is a dummy function"

    # Define a subclass that has a defined distribution
    class RedHatModule(AnsibleModule):
        platform = "Linux"
        distribution = "RedHat"

        def redhat_dummy_function(self):
            return


# Generated at 2022-06-12 23:38:17.605582
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Unit test for function get_distribution_verison
    '''
    # Test base case where there is no release file and the code returns an empty string
    # for that field.
    assert get_distribution_version() == ''
    assert get_distribution_version() != None

# Generated at 2022-06-12 23:38:26.250720
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        platform = "A platform"
        distribution = "A distribution"

    class B(A):
        platform = "B platform"
        distribution = "B distribution"

    class C(B):
        platform = "C platform"
        distribution = "C distribution"

    assert get_platform_subclass(A) is A
    assert get_platform_subclass(B) is B
    assert get_platform_subclass(C) is C

    class A2:
        pass

    class B2(A2):
        platform = "B platform"

    assert get_platform_subclass(B2) is B2
    assert get_platform_subclass(A2) is B2

    class A3:
        platform = "A platform"

    class B3(A3):
        platform = "B platform"

   

# Generated at 2022-06-12 23:38:37.143830
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import sys
    import subprocess
    import tempfile

    distribution_codename = {
        "centos": "el6",
        "ubuntu": "xenial",
        "debian": "stretch",
        "freebsd": "11.1-RELEASE",
        "redhat": "el6",
        "oracle": "ol6",
        "suse": "SLES 11 SP3",
    }

    # List of distributions to test
    distros = list(distribution_codename.keys())

    for distro in distros:
        # Create a temporary directory to hold the os release files
        os_release_file_path = tempfile.mkdtemp()
        os_release_file_full_path = os_release_file_path + "/os-release"

        # Create os release file contents
        os

# Generated at 2022-06-12 23:38:49.275906
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import mock
    import platform
    with mock.patch("ansible.module_utils.distro.codename", return_value="unknown"):
        assert get_distribution_codename() == None
    with mock.patch("platform.system", return_value="Linux"):
        with mock.patch("ansible.module_utils.distro.os_release_info", return_value={"version_codename": "jessie"}):
            assert get_distribution_codename() == "jessie"
        with mock.patch("ansible.module_utils.distro.os_release_info", return_value={"version_codename": "jessie", "ubuntu_codename": "bionic"}):
            assert get_distribution_codename() == "jessie"

# Generated at 2022-06-12 23:38:54.133223
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Unit test for function :py:func:`~ansible.module_utils.common._collections.get_distribution_codename`
    '''
    res = get_distribution_codename()
    assert res is not None

# Generated at 2022-06-12 23:39:04.717399
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    ''' Simple test to ensure the get_platform_subclass function works '''
    class Foo:
        pass

    class Redhat(Foo):
        distribution = 'RedHat'
        platform = 'Linux'

    class Debian(Foo):
        distribution = 'Debian'
        platform = 'Linux'

    class BSD(Foo):
        distribution = None
        platform = 'BSD'

    class SunOS(Foo):
        distribution = 'Solaris'
        platform = 'SunOS'

    with patch('platform.system', return_value='Linux'):
        with patch('distro.id', return_value='debian'):
            platform = get_platform_subclass(Foo)
        assert platform == Debian


# Generated at 2022-06-12 23:39:12.556854
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    test function get_platform_subclass from module_utils.common.distribution.py
    '''
    import sys
    if sys.version_info[0] > 2:
        from configparser import ConfigParser
    else:
        from ConfigParser import ConfigParser

    import module_utils.common.distribution as distribution

    def class_mock(base_class, config_mock):
        '''
        mock class to set class variable in get_platform_subclass function
        '''
        _distribution = config_mock.distribution
        _platform = config_mock.platform

        class _class_mock:
            '''
            stub class for testing get_platform_subclass function
            '''
            def __init__(self):
                self.distribution = _distribution

# Generated at 2022-06-12 23:39:13.149597
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution()

# Generated at 2022-06-12 23:39:14.116503
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Redhat'

# Generated at 2022-06-12 23:39:21.568899
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import tempfile, shutil
    try:
        tmpdir = tempfile.mkdtemp()
        fp = open(tmpdir + '/os-release', 'w')
        fp.write("""NAME="Fedora"
VERSION="28 (Twenty Eight)"
ID=fedora
VERSION_ID=28
VERSION_CODENAME=""
PLATFORM_ID="platform:f28"
""")
        fp.close()

        codename = get_distribution_codename()
        assert codename is None
    finally:
        shutil.rmtree(tmpdir)

# Generated at 2022-06-12 23:39:35.343604
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class ParentClass:
        platform = None
        distribution = None

    class SubClass_Parent(ParentClass):
        pass

    class SubClass_Linux(ParentClass):
        platform = 'Linux'

    class SubClass_Linux_Debian(ParentClass):
        platform = 'Linux'
        distribution = 'Debian'

    class SubClass_Linux_Debian_Ubuntu(ParentClass):
        platform = 'Linux'
        distribution = 'Debian'

    class SubClass_Linux_Ubuntu(ParentClass):
        platform = 'Linux'
        distribution = 'Ubuntu'

    class SubClass_Redhat(ParentClass):
        distribution = 'Redhat'

    class SubClass_Redhat_Centos(ParentClass):
        distribution = 'Redhat'

    import platform

# Generated at 2022-06-12 23:39:38.428175
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test to see if get_distribution is able to accurately determine the distribution
    the code is running on.
    '''
    assert(get_distribution() == distro.id().capitalize())


# Generated at 2022-06-12 23:39:43.708740
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    os_release_debs=["bionic", "xenial", "trusty", "wheezy", "jessie", "stretch", "buster"]
    os_release_rhels=["8.1", "8.0", "7.7", "7.6"]
    if distro.id() == "debian" :
        assert get_distribution_codename() in os_release_debs
    if distro.id() == "redhat" :
        assert get_distribution_codename() in os_release_rhels

# Generated at 2022-06-12 23:39:54.718095
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class TestSuperClass:
        platform = 'Generic'
        distribution = None
    class TestClass1(TestSuperClass):
        platform = 'Darwin'
        distribution = None
    class TestClass2(TestSuperClass):
        platform = 'Darwin'
        distribution = 'Darwin'
    class TestClass3(TestSuperClass):
        platform = 'Darwin'
        distribution = 'MacOSX'
    class TestClass4(TestSuperClass):
        platform = 'Linux'
        distribution = None
    class TestClass5(TestSuperClass):
        platform = 'Linux'
        distribution = 'Linux'
    class TestClass6(TestSuperClass):
        platform = 'Linux'
        distribution = 'Redhat'
    class TestClass7(TestSuperClass):
        platform = 'Linux'
        distribution = 'Amazon'

# Generated at 2022-06-12 23:40:04.161938
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import ansible.module_utils.basic
    class BaseClass:
        platform = 'Base'
        distribution = None

    class OneSubclass(BaseClass):
        platform = 'OneSub'

    class TwoSubclass(BaseClass):
        distribution = 'TwoSub'

    class ThreeSubclass(BaseClass):
        platform = 'ThreeSub'
        distribution = 'ThreeSub'

    BaseSub = get_platform_subclass(BaseClass)
    assert BaseSub == BaseClass
    BaseSub = get_platform_subclass(BaseClass('Base'))
    assert BaseSub == BaseClass
    BaseSub = get_platform_subclass(BaseClass('Base', 'Base'))
    assert BaseSub == BaseClass

    OneSub = get_platform_subclass(OneSubclass)
    assert OneSub == OneSubclass
    OneSub = get

# Generated at 2022-06-12 23:40:17.069856
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Unit tests for the Ansible get_distribution_version method.
    '''

    def test_function(os_release, test_version, lsb_release=None):
        '''
        Tests the get_distribution_version method with the given os_release
        contents and the expected version.

        :arg os_release: Contents of the OS release to test against
        :arg test_version: Expected version with the given OS release
        :arg lsb_release: Optional contents of the LSB release to test against. Defaults to None.
        '''

        # initialize the variables
        distro.release_filename = None
        distro.lsb_release_file = None
        distro.os_release_attr = None
        distro.lsb_release_info_attr = None
        distro.lsb_

# Generated at 2022-06-12 23:40:26.382849
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    # test for Red Hat

    class _distro_RedHat:
        id = 'Red Hat Enterprise Linux Server'
        version = '7.5'
        codename = ""

        @staticmethod
        def id():
            return _distro_RedHat.id

        @staticmethod
        def version(best=False):
            return _distro_RedHat.version

        @staticmethod
        def os_release_info():
            return {'name':_distro_RedHat.id, 'version':_distro_RedHat.version, 'version_codename':_distro_RedHat.codename}

        @staticmethod
        def codename():
            return _distro_RedHat.codename

    def _platform_system():
        return 'Linux'

    def _distro_id():
        return _distro_

# Generated at 2022-06-12 23:40:38.180462
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A(object):
        platform = "Linux"
        distribution = None
    class B(A):
        pass
    class C(B):
        platform = "AIX"
    class D(B):
        platform = "Linux"
        distribution = "Redhat"
    class E(B):
        platform = "Linux"
    class F(E):
        distribution = "Redhat"
    class G(E):
        distribution = "Debian"
    class H(E):
        platform = "Linux"
        distribution = "Redhat"
    class I(H):
        distribution = "Debian"

    assert get_platform_subclass(A) == A
    assert get_platform_subclass(B) == A
    assert get_platform_subclass(C) == C

# Generated at 2022-06-12 23:40:49.219844
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit test for function get_platform_subclass
    '''
    import unittest
    import sys

    class TestBase(object):
        '''
        Base class for test get_platform_subclass
        '''
        platform = 'TestPlatform'
        distribution = None

    class TestSub1(TestBase):
        '''
        Subclass 1 for test get_platform_subclass
        '''
        platform = 'TestPlatform'
        distribution = 'TestDistribution'

    class TestSub2(TestBase):
        '''
        Subclass 2 for test get_platform_subclass
        '''
        platform = 'TestPlatform'
        distribution = 'TestDistribution'

    class TestSub3(TestBase):
        '''
        Subclass 3 for test get_platform_subclass
        '''
       

# Generated at 2022-06-12 23:40:55.202777
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    from six import StringIO
    from ansible.module_utils._text import to_native
    from ansible.module_utils.distro import Distro

    # Following code does:
    # 1. Capture distro.os_release_info() output and check for version_codename
    # 2. Check for ubuntu_codename
    # 3. If no codename is found, capture distro.lsb_release_info() and check for codename

# Generated at 2022-06-12 23:41:09.460167
# Unit test for function get_distribution
def test_get_distribution():
    platform_lookup = {
        'Darwin': 'Darwin',
        'Linux-debian-wheezy': 'Debian',
        'Linux-fedora-20': 'Fedora',
        'Linux-oracle-6-x86_64': 'Oracle',
        'Linux-redhat-6-x86_64': 'Redhat',
        'Linux-suse-11': 'Suse',
        'Linux-ubuntu-12.04': 'Ubuntu',
    }

    for (platform_str, distro_str) in platform_lookup.items():
        assert get_distribution() == distro_str

# Generated at 2022-06-12 23:41:16.797268
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    ubuntu_xenial_xerus = '''
    NAME="Ubuntu"
    VERSION="16.04.6 LTS (Xenial Xerus)"
    ID=ubuntu
    ID_LIKE=debian
    PRETTY_NAME="Ubuntu 16.04.6 LTS"
    VERSION_ID="16.04"
    HOME_URL="http://www.ubuntu.com/"
    SUPPORT_URL="http://help.ubuntu.com/"
    BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
    VERSION_CODENAME=xenial
    UBUNTU_CODENAME=xenial
    '''
    assert get_distribution_codename() == 'xenial'


# Generated at 2022-06-12 23:41:19.389805
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == platform.dist()[0].capitalize()


# Generated at 2022-06-12 23:41:29.505746
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    platform_system = platform.system()
    distribution = get_distribution()
    codename = get_distribution_codename()
    version = get_distribution_version()

    # Modules that currently use get_platform_subclass
    class Podman(object):
        platform = 'Linux'
        distribution = None
    class User:
        platform = 'Linux'
        distribution = None
    class Selinux:
        platform = 'Linux'
        distribution = None

    # Create example subclasses using each possible get_platform_subclass case
    class PodmanRedhat(Podman):
        distribution = 'Redhat'
    class PodmanUbuntu(Podman):
        distribution = 'Ubuntu'
    class PodmanUbuntuXenial(PodmanUbuntu):
        codename = 'xenial'

# Generated at 2022-06-12 23:41:40.096726
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class MainClass(object):
        platform = None
        distribution = None

    class SubClassA(MainClass):
        platform = 'Linux'
        distribution = 'Ubuntu'

    class SubClassB(MainClass):
        platform = 'Linux'
        distribution = None

    class SubClassC(MainClass):
        platform = 'FreeBSD'
        distribution = None

    class SubClassD(MainClass):
        platform = 'Linux'
        distribution = 'Fedora'

    assert get_platform_subclass(MainClass) == MainClass

    # Set some mock platform data
    class _PlatformData(object):
        system = 'Linux'
    original_platform = platform.system
    platform.system = lambda: 'Linux'
    original_distribution = distro.id
    distro.id = lambda: 'Ubuntu'


# Generated at 2022-06-12 23:41:42.062949
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    assert get_platform_subclass(ModuleFailException) == ModuleFailException
    assert get_platform_subclass(OtherModuleFailException) == OtherOtherModuleFailException


# Generated at 2022-06-12 23:41:46.083178
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import ansible.modules.system.user
    classification = platform.system() + '.' + get_distribution()
    x = get_platform_subclass(ansible.modules.system.user.User)
    assert classification == x.__name__

# Generated at 2022-06-12 23:41:48.190861
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() is None


# Generated at 2022-06-12 23:41:53.665741
# Unit test for function get_distribution
def test_get_distribution():
    # Testing against a test RPM we can control
    with open('/etc/os-release') as f:
        for line in f.readlines():
            if line.startswith('ID='):
                distribution = line.split('=')[1].strip()
        assert distribution == 'test_distro_id'



# Generated at 2022-06-12 23:42:02.571205
# Unit test for function get_distribution
def test_get_distribution():
    if platform.system() == 'Linux':
        assert get_distribution() in ('Redhat', 'Debian', 'Arch', 'Freebsd', 'Gentoo', 'Suse', 'OpenSUSE', 'AIX', 'Amazon', 'Xenserver', 'Cloudlinux', 'Alpine', 'Mandrake', 'Mandriva', 'Mageia', 'Solaris', 'Slackware', 'Openbsd', 'F5linux', 'OtherLinux'), '%s is not a valid distribution' % get_distribution()
    else:
        assert get_distribution() in ('Macosx', 'Sun', 'Freebsd', 'Netbsd', 'Openbsd', 'AIX', 'Nikedos', 'Tru64'), '%s is not a valid distribution' % get_distribution()

# Generated at 2022-06-12 23:42:24.039983
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    from unittest import TestCase

    import tempfile
    import shutil
    import os
    import stat

    test_d = tempfile.mkdtemp()

    def create_file(name, value):
        fobj = open(os.path.join(test_d, name), 'w')
        fobj.write(value)
        fobj.close()


# Generated at 2022-06-12 23:42:24.787876
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Amazon'

# Generated at 2022-06-12 23:42:36.000700
# Unit test for function get_distribution
def test_get_distribution():
    from unittest import TestCase, TestLoader, TextTestRunner
    from ansible.module_utils.six import u

    class TestGetDistribution(TestCase):
        def test_suse_module_utils(self):
            distro_id = u'SUSE LINUX'
            version = u'11'
            version_id = u'11.4'
            codename = u'Final'
            expected_distro = u'Suse'
            self.assertEqual(expected_distro, get_distribution())

            distro_id = u'opensuse'
            version = u'42.1'
            version_id = u'42.1'
            codename = u'Tumbleweed'
            expected_distro = u'Suse'

# Generated at 2022-06-12 23:42:47.227094
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # The following classes are the test bare bones classes for the function get_platform_subclass
    class Base():
        platform = 'Linux'
        distribution = None
    class DerivedA(Base):
        distribution = 'Redhat'
    class DerivedB(DerivedA):
        distribution = 'Centos'

    class BaseB(Base):
        platform = 'FreeBSD'
    class DerivedC(BaseB):
        distribution = 'FreeBSD'

    # This is the class will be used for testing
    class Test(DerivedB, DerivedC):
        pass

    # Set platform to a Linux machine
    platform.system = lambda: 'Linux'
    # Set distribution to Redhat
    distro.id = lambda: 'Redhat'

    # Test to see if the subclass returned is DerivedA
    assert get_platform_subclass

# Generated at 2022-06-12 23:42:51.018401
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Get the distribution name the code is running on

    :rtype: String
    :returns: A string representing the distribution name
    '''
    distribution = get_distribution()
    assert isinstance(distribution, NativeString)
    return distribution



# Generated at 2022-06-12 23:42:52.317734
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert 'bionic' == get_distribution_codename()

# Generated at 2022-06-12 23:42:54.361730
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version() == distro.version()

    # version is None on AWS Linux
    assert get_distribution_version() == u''

# Generated at 2022-06-12 23:43:01.319055
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Make sure we can find the subclass for the platform we're running on
    class Test:
        pass

    class TestLinux(Test):
        platform = 'Linux'
        distribution = None

    class TestLinuxAmazon(Test):
        platform = 'Linux'
        distribution = 'Amazon'

    class TestDarwin(Test):
        platform = 'Darwin'
        distribution = None

    class TestFreeBSD(Test):
        platform = 'FreeBSD'
        distribution = None

    assert TestLinux == get_platform_subclass(Test)
    assert TestDarwin == get_platform_subclass(Test)
    assert TestFreeBSD == get_platform_subclass(Test)

    assert TestLinux == get_platform_subclass(TestLinux)
    assert TestDarwin == get_platform_subclass(TestDarwin)

# Generated at 2022-06-12 23:43:02.316555
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # TODO: Write unit test
    pass

# Generated at 2022-06-12 23:43:12.655120
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # get_platform_subclass should always return the class itself if there is no subclass.
    class MyClass:
        platform = "Darwin"
        distribution = None

    assert get_platform_subclass(MyClass) == MyClass

    # If there are no subclasses, return the class itself.
    class MyClass2:
        platform = "Darwin"
        distribution = None

    assert get_platform_subclass(MyClass2) == MyClass2

    # Make sure the generic class gets returned if no match is found
    class MyClass3:
        platform = "Darwin"
        distribution = None

    class SubClass1(MyClass3):
        platform = "Linux"
        distribution = None

    class SubClass2(MyClass3):
        platform = "Darwin"
        distribution = "Ubuntu"


# Generated at 2022-06-12 23:43:40.334987
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    from ansible.module_utils._text import to_native
    distribution_codename = to_native(get_distribution_codename())
    assert distribution_codename is not None

# Generated at 2022-06-12 23:43:42.264208
# Unit test for function get_distribution_version
def test_get_distribution_version():
    platform_version = get_distribution_version()
    assert (platform_version is not None)


# Generated at 2022-06-12 23:43:44.223532
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() is None
    assert get_distribution_codename() != 'stretch'

# Generated at 2022-06-12 23:43:53.202002
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Super:
        pass

    class Sub(Super):
        pass

    class SubSub(Sub, object):
        pass

    class LinuxSub(Sub, object):
        platform = 'Linux'

    class LinuxSubSub(LinuxSub, object):
        distribution = 'Ubuntu'

    # We'll call this twice, once with the argument type being the generic Super class, and
    # a second time with the argument type being the SubSub class.  For the first call,
    # LinuxSubSub should be returned, and for the second call, LinuxSub should be returned.
    for argument_type in (Super, SubSub):
        # we'll set the system to 'Linux' for the test, then restore the old value afterwards
        saved_system = platform.system
        platform.system = lambda: 'Linux'

        # get_platform_subclass() returned Linux

# Generated at 2022-06-12 23:44:06.080814
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test function get_platform_subclass
    '''
    import platform
    class BaseClass:
        ''' Base class '''
        distribution = None
        platform = None

    class LinuxSubclass(BaseClass):
        ''' Linux Subclass '''
        distribution = None
        platform = 'Linux'

    class RedhatSubclass(LinuxSubclass):
        ''' Redhat Subclass '''
        distribution = 'Redhat'

    class FedoraSubclass(LinuxSubclass):
        ''' Fedora Subclass '''
        distribution = 'Fedora'

    class WindowsSubclass(BaseClass):
        ''' Windows Subclass '''
        distribution = None
        platform = 'Windows'


# Generated at 2022-06-12 23:44:08.116097
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    actual = get_distribution_codename()
    expected = 'xenial'
    assert actual == expected

# Generated at 2022-06-12 23:44:12.303608
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Return the distribution version that is used for unit testing.

    :rtype: string
    :returns: A string representation of the version of the distribution.
    '''
    return u'10.4'


# Generated at 2022-06-12 23:44:13.454039
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() is None

# Generated at 2022-06-12 23:44:15.208356
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    if platform.system() == 'Linux':
        assert get_distribution_codename() is not None

# Generated at 2022-06-12 23:44:16.153087
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == None

# Generated at 2022-06-12 23:45:12.684075
# Unit test for function get_distribution
def test_get_distribution():
    from ansible.module_utils.common._collections_compat import Mapping
    import unittest

    class LinuxMockDistro(Mapping):
        def __init__(self, *args, **kwargs):
            self._dict = dict(*args, **kwargs)

        def __getitem__(self, key):
            return self._dict[key]

        def __iter__(self):
            return iter(self._dict)

        def __len__(self):
            return len(self._dict)

        def id(self):
            return 'debian'

        def version(self):
            return '8.0'

        def version_best(self):
            return '8.0.1'


# Generated at 2022-06-12 23:45:23.395411
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test for get_platform_subclass
    '''
    try:
        from ansible.module_utils.user_module import User
        Distribution = User.Distribution
        from ansible.module_utils.user_module import User as UserLinux
        from ansible.module_utils.user_module import UserMac as UserMac
    except ImportError:
        # ImportError occurs when module_utils is not on PYTHONPATH
        # This can happen when unit tests are run individually
        import os
        import sys
        import inspect
        import types

        ansible_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "../../../")))

# Generated at 2022-06-12 23:45:32.353892
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import load_platform_subclass
    import platform
    import ansible.module_utils.common.misc as misc

    # Create our class to test
    class TestClass:
        distribution = None
        platform = platform.system()

    class TestClassSubclass:
        distribution = get_distribution()
        platform = platform.system()

    # Test return of superclass
    subclass = get_platform_subclass(TestClass)
    assert TestClass is subclass

    # Test return of subclass
    subclass = get_platform_subclass(TestClassSubclass)
    assert subclass is TestClassSubclass



# Generated at 2022-06-12 23:45:34.992138
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    codename = get_distribution_codename()
    assert codename is None or isinstance(codename, (str, unicode))

# Generated at 2022-06-12 23:45:42.898382
# Unit test for function get_distribution
def test_get_distribution():
    '''Unit test for function get_distribution'''
    # Test for Debian
    def _test_get_distribution_for_debian(os_release_content):
        '''Test for Debian'''
        dist = get_distribution()
        version = get_distribution_version()
        codename = get_distribution_codename()

        assert dist == 'Debian'
        assert version == '9.4'
        assert codename == 'stretch'

    def _test_get_distribution_for_suse(os_release_content):
        '''Test for openSUSE'''
        dist = get_distribution()
        version = get_distribution_version()
        codename = get_distribution_codename()

        assert dist == 'Opensuse'
        assert version == 'leap'

# Generated at 2022-06-12 23:45:53.831533
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    this_platform = platform.system()

    # ensure the correct platform is selected based on matching platform and
    # distribution
    class Foo():
        platform = this_platform
        distribution = get_distribution()

    class FooSubclass(Foo):
        platform = this_platform
        distribution = get_distribution()

    assert get_platform_subclass(Foo) == FooSubclass


    # ensure the correct platform is selected based on matching platform and
    # distribution
    class Bar():
        platform = this_platform
        distribution = get_distribution()

    class BarSubclass(Bar):
        platform = this_platform
        distribution = get_distribution()

    class BarSubSubclass(BarSubclass):
        platform = this_platform

    assert get_platform_subclass(Bar) == BarSubSubclass


    # ensure the correct

# Generated at 2022-06-12 23:46:05.498791
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class BaseFoo:
        pass
    class BaseBar:
        pass
    class BaseOtherLinux(BaseFoo, BaseBar):
        platform = 'Linux'
        distribution = None
    class RHELFoo(BaseFoo):
        platform = 'Linux'
        distribution = 'Redhat'
    class OtherLinuxFoo(BaseOtherLinux):
        pass
    class Foo(BaseFoo):
        pass

    assert get_platform_subclass(Foo) is BaseFoo
    assert get_platform_subclass(BaseFoo) is BaseFoo
    assert get_platform_subclass(BaseBar) is BaseBar
    assert get_platform_subclass(BaseOtherLinux) is BaseOtherLinux

    import sys
    import platform
    # When running on Python 2, this will be a str.
    this_platform = platform.system

# Generated at 2022-06-12 23:46:11.865015
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Superclass:
        pass

    class Subclass(Superclass):
        platform = 'Linux'
        distribution = 'Debian'

    class OtherLinuxSubclass(Superclass):
        platform = 'Linux'
        distribution = None

    assert get_platform_subclass(Superclass) is Superclass
    assert get_platform_subclass(Subclass) is Subclass
    assert get_platform_subclass(OtherLinuxSubclass) is OtherLinuxSubclass

# Generated at 2022-06-12 23:46:16.993938
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Foo:
        platform = 'foo-platform'
        distribution = None

    assert get_platform_subclass(Foo) is Foo

    class Bar(Foo):
        platform = 'bar-platform'

    assert get_platform_subclass(Foo) is Bar

    class Baz(Foo):
        distribution = 'baz-distro'

    assert get_platform_subclass(Foo) is Baz

    class Qux(Baz):
        platform = 'qux-platform'

    assert get_platform_subclass(Foo) is Qux

# Generated at 2022-06-12 23:46:28.181764
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Add some classes to find
    class BaseClass:
        pass
    class LinuxClass(BaseClass):
        platform = 'Linux'
    class PosixClass(BaseClass):
        platform = 'Posix'
    class BSDClass(BaseClass):
        platform = 'BSD'
    class LinuxDebianClass(LinuxClass):
        distribution = 'Debian'
    class LinuxRedHatClass(LinuxClass):
        distribution = 'RedHat'
    class LinuxSuseClass(LinuxClass):
        distribution = 'Suse'
    class LinuxFreeBSDClass(LinuxClass):
        distribution = 'FreeBSD'
    class LinuxOpenBSDClass(LinuxClass):
        distribution = 'OpenBSD'
    class PlatformIndependentClass(BaseClass):
        pass

    # Test that the correct class is found for each platform
    # Distribution Linux

# Generated at 2022-06-12 23:47:27.008762
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import sys

    # Pretend we're on an unknown platform
    platform_old = platform.system
    platform.system = lambda: 'Unknown'


# Generated at 2022-06-12 23:47:35.643262
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    from distro import linux_distribution
    from distro import os_release_info
    import distro._distro as _distro

    distro_id = distro.id()

    # CentOS
    assert get_distribution_codename() == 'final'

    # Debian
    _distro.lsb_release_info = lambda: {'id': 'Debian', 'codename': 'buster'}
    _distro.distro_id = lambda: 'Debian'
    assert get_distribution_codename() == 'buster'

    # Fedora
    _distro.lsb_release_info = lambda: {'id': 'Fedora', 'codename': ''}
    _distro.distro_id = lambda: 'Fedora'
    assert get_distribution_codename() is None

    # Red Hat


# Generated at 2022-06-12 23:47:36.845352
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Amazon'


# Generated at 2022-06-12 23:47:42.134662
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == None

    assert get_distribution_codename().lower() == u'jessie'
    assert get_distribution_codename().lower() == u'trusty'
    assert get_distribution_codename().lower() == u'xenial'
    assert get_distribution_codename().lower() == u'wily'
    assert get_distribution_codename().lower() == u'buster'


# Generated at 2022-06-12 23:47:49.077988
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    from ansible.module_utils import basic
    platform_info = {
        'redhat': (u'Redhat', None),
        'ubuntu': (u'Ubuntu', u'bionic'),
        'debian': (u'Debian', u'buster'),
        'fedora': (u'Fedora', None),
        'centos': (u'Centos', None),
        'other': (u'OtherLinux', None),
    }

    for platform_name, platform_tuple in platform_info.items():
        import sys
        sys.modules['platform'] = FakePlatform(platform_name)
        import distro
        sys.modules['distro'] = FakeDistro(*platform_tuple)
        assert basic.get_distribution_codename() == platform_tuple[1]



# Generated at 2022-06-12 23:48:00.666682
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # We're going to set a fake platform Linux distribution that we can control
    # to test the function
    class FakePlatform():
        @staticmethod
        def system():
            return 'Linux'

    class FakeDistro():
        @staticmethod
        def os_release_info():
            return {'version_codename': 'xenial'}
        @staticmethod
        def id():
            return 'ubuntu'

    # mock out platform and distro
    orig_platform = platform.system
    platform.system = FakePlatform.system
    orig_distro = distro.id
    distro.id = FakeDistro.id
    orig_os_release_info = distro.os_release_info
    distro.os_release_info = FakeDistro.os_release_info

    # Test against the two different ways we can get

# Generated at 2022-06-12 23:48:07.855548
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Foo:
        pass

    class FooCentos(Foo):
        platform = 'Linux'
        distribution = 'Centos'

    class Bar(Foo):
        platform = 'Linux'
        distribution = None

    foo_centos = get_platform_subclass(Foo)
    assert foo_centos is FooCentos

    old_id = distro.id
    old_version = distro.version
    try:
        distro.id = lambda: 'centos'
        distro.version = lambda: '7.0'
        bar = get_platform_subclass(Bar)
        assert bar is Bar
    finally:
        distro.id = old_id
        distro.version = old_version


# Generated at 2022-06-12 23:38:23.448318
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    expected_codenames = {
        # https://github.com/ansible/ansible/issues/40236
        u'centos': (u'7', u'centos7'),
        # https://github.com/ansible/ansible/issues/42614
        u'ubuntu': (u'xenial', u'xenial'),
    }
    for distribution in expected_codenames:
        setattr(distro, u'id', lambda: distribution)
        try:
            version = expected_codenames[distribution][0]
            setattr(distro, u'version', lambda: version)
            codename = expected_codenames[distribution][1]
            setattr(distro, u'codename', lambda: codename)
        except AttributeError:
            pass
        codename = get

# Generated at 2022-06-12 23:38:34.706445
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class Base:
        pass

    class A(Base):
        platform = 'Linux'
        distribution = 'Ubuntu'

    class B(Base):
        platform = 'Linux'

    class C(Base):
        platform = 'Darwin'

    class D(Base):
        platform = 'Linux'
        distribution = 'Ubuntu'

    assert Base == get_platform_subclass(Base)
    assert A == get_platform_subclass(Base)
    assert B == get_platform_subclass(Base)
    assert C == get_platform_subclass(Base)
    assert D == get_platform_subclass(Base)

    class E(A):
        distribution = 'RedHat'

    assert E == get_platform_subclass(Base)

# Generated at 2022-06-12 23:38:41.330868
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    # get_platform_subclass() is a static method.  We can't instantiate
    # the class passed in to it.  These are the classes used to test
    # get_platform_subclass() with.
    #
    # We start with a base class for all platforms. The base class has
    # no code of its own, but it does specify an attribute.
    class BasePlatformClass:
        my_attribute = 'Original value'

    # Next, we have a class that inherits from the base class
    # but is specific to one system.
    class UnixSystem(BasePlatformClass):
        platform = 'Linux'
        my_attribute = 'Changed value'

    # We also have a class that inherits from the base class
    # but is specific to another system.
    class WindowsSystem(BasePlatformClass):
        platform = 'Windows'


# Generated at 2022-06-12 23:38:51.670810
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit test for function get_platform_subclass
    '''
    class cls0:
        '''
        dummy class 0
        '''
        platform = 'Linux'
        distribution = 'ABC'

    class cls1(cls0):
        '''
        dummy class 1
        '''

    class cls2(cls0):
        '''
        dummy class 2
        '''
        platform = 'Linux'
        distribution = 'ABC'

    class cls3(cls0):
        '''
        dummy class 3
        '''
        platform = 'Linux'
        distribution = 'ABC'

    class cls4(cls0):
        '''
        dummy class 4
        '''
        platform = 'Linux'
        distribution = 'XYZ'


# Generated at 2022-06-12 23:38:55.118005
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
        Tests function get_distribution_version
    '''
    # Test for CentOS, Ubuntu, Debian and Fedora
    assert get_distribution_version() in ['7.5', '16.04', '9', '28']

# Generated at 2022-06-12 23:39:06.426051
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform
    from ansible.module_utils.basic import _load_params, AnsibleModule, get_platform_subclass
    # Loads a version of UserModule that only works on Ubuntu
    class UserModuleUbuntu:
        distribution = "Ubuntu"
        platform = "Linux"
    # Loads a version of UserModule that only works on Linux
    class UserModuleLinux:
        platform = "Linux"
    # Loads a version of UserModule that works on all platforms
    class UserModule:
        pass
    # Loads a version of UserModule that works on all platforms
    class UserModuleFail:
        platform = "FreeBSD"

    class ModuleFailTest(AnsibleModule):
        pass

    # Unit test 1, get the most specific subclass for this platform
    distribution = get_distribution()
    this_platform = platform.system

# Generated at 2022-06-12 23:39:17.190866
# Unit test for function get_distribution_version
def test_get_distribution_version():
    """
    Unit test for function get_distribution_version
    """
    class MockObject:
        """
        Used to mock the distro module.
        """
        def __init__(self, version=None, id=None, version_best=None):
            """
            Constructor for the mock object.

            :arg version: The value to return when calling version()
            :arg id: The value to return when calling id()
            :arg version_best: The value to return when calling version(best=True)
            """
            self.version = version
            self.id = id
            self.version_best = version_best

        def version(self, **kwargs):
            """
            Just return the version
            """
            return self.version

        def id(self):
            """
            Just return the id
            """


# Generated at 2022-06-12 23:39:28.396465
# Unit test for function get_distribution
def test_get_distribution():
    '''
    :returns: ``True`` if the unit test succeeds and ``False`` if it fails
    :rtype: bool
    '''
    # Error if a distribution returns an incorrect string

# Generated at 2022-06-12 23:39:35.599969
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    distro.id = lambda: 'Ubuntu'
    distro.os_release_info = lambda: {}
    distro.lsb_release_info = lambda: {'codename': 'precise'}
    assert get_distribution_codename() == 'precise'

    distro.os_release_info = lambda: {}
    distro.lsb_release_info = lambda: {'codename': None}
    assert get_distribution_codename() is None

    distro.codename = lambda: 'bionic'
    distro.os_release_info = lambda: {'version_codename': 'bionic'}
    assert get_distribution_codename() == 'bionic'
    distro.os_release_info = lambda: {'version_codename': None}
    assert get_distribution_

# Generated at 2022-06-12 23:39:43.739616
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # Test for Ubuntu
    import sys
    import platform
    import distro
    from distutils.version import LooseVersion
    from ansible.module_utils.six import PY3
    from ansible.module_utils.common._utils import get_all_subclasses

    old_system = platform.system()
    old_distro_id = distro.id()
    old_distro_version = distro.version()
    old_distro_version_best = distro.version(best=True)
    old_get_all_subclasses = get_all_subclasses
    old_platform_release = platform.release()

    platform.system = lambda: 'Linux'
    distro.id = lambda: 'Ubuntu'
    distro.version = lambda best=False: '16.04'

# Generated at 2022-06-12 23:39:58.176211
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    test_get_platform_subclass tests for proper class selection.

    We want to ensure that the correct class is selected, the order of class selection is correct and
    that an exception is raised if no valid platforms are defined.
    '''
    import platform, ansible.module_utils.facts.system.user

    # These are the distribution names that distro returns

# Generated at 2022-06-12 23:40:00.500710
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Unit test for function get_distribution
    '''
    assert get_distribution() == "Darwin"



# Generated at 2022-06-12 23:40:07.915945
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test the function get_distribution_codename

    Break it for supported Linux distributions

    The function takes no parameters, so breaking it to test it is straightforward.
    '''
    # Test for non-linux.  Return value must be None
    non_linux_distribution = ['aix', 'bsd', 'darwin', 'freebsd', 'hpux', 'linux', 'netbsd', 'openbsd', 'posix', 'sunos']

    for non_linux in non_linux_distribution:
        def _get_platform_system(non_linux):
            return non_linux
        platform.system = _get_platform_system.__get__(platform.system, platform)
        actual = get_distribution_codename()

# Generated at 2022-06-12 23:40:19.620165
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Run unit tests for get_distribution_version
    '''
    from ansible_collections.misc.not_a_real_collection.tests.unit.compat import mock
    import os

    os_release = '/etc/os-release'

    #
    # Unit test for get_distribution_version().  Using distro's
    # version() method as an example.
    #

    # path to a fake distro.id() file for testing
    # this is where the function will attempt to read its data from
    etc_os_release = '/etc/os-release'
    etc_os_release_orig = etc_os_release + '.orig'

    #
    # test get_distribution_version() returning empty string
    #

# Generated at 2022-06-12 23:40:28.169904
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    platform_name = platform.system()
    distribution = get_distribution()
    codename = get_distribution_codename()
    assert codename is not None or platform_name != 'Linux'
    # check if codename is valid in platform_name:distribution
    if codename is not None and platform_name == 'Linux':
        from ansible.module_utils._text import to_native
        from ansible.module_utils.common.collections import is_sequence
        import distro
        # map of (platform_name:distribution) to codenames

# Generated at 2022-06-12 23:40:39.398153
# Unit test for function get_distribution
def test_get_distribution():
    import copy
    import os
    import platform
    import pytest
    import sys
    import warnings
    import distro

    # Test cases covering the various distributions and their various
    # code names.  This is a subset of the info in the Ubuntu release notes

# Generated at 2022-06-12 23:40:43.239558
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Unit test for function get_distribution_codename
    :returns: None
    '''
    codename = get_distribution_codename()
    assert isinstance(codename, str)

# Generated at 2022-06-12 23:40:52.237273
# Unit test for function get_distribution
def test_get_distribution():
    distribution = get_distribution()

    # Check that we get the right distribution name
    if platform.system() == 'Linux':
        assert distribution in (u'Debian', u'Redhat', u'SuSE', u'Fedora',
                                u'Arch', u'Gentoo', u'AmigaOS', u'Slackware',
                                u'Solaris', u'OpenIndiana', u'Alpine',
                                u'OpenWrt', u'Mageia', u'Mandriva', u'OtherLinux')
    elif platform.system() == 'FreeBSD':
        assert distribution in (u'FreeBSD', u'DragonFly')
    elif platform.system() == 'OpenBSD':
        assert distribution in (u'OpenBSD',)

# Generated at 2022-06-12 23:40:55.305230
# Unit test for function get_distribution_version
def test_get_distribution_version():
    # Test RedHat
    test_result = get_distribution_version()
    if platform.system() == 'Linux':
        assert test_result != ''

# Unit tests for function get_distribution_codename

# Generated at 2022-06-12 23:41:04.070309
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit test for function get_platform_subclass

    This unit test exercises the get_platform_subclass function by creating the following
    class heirarchy:

        Top
        |
        +--- Linux
        |    |
        |    +--- RedHat
        |    |
        |    +--- Debian
        |
        +--- Solaris
        |    |
        |    +--- SunOS
        |    |
        |    +--- OpenSolaris
        |
        +--- Other

    It then tries to find the subclass that matches the current platform.
    '''

    class Top:  # pylint: disable=too-few-public-methods
        '''
        Top of class heirarchy
        '''
        platform = None
        distribution = None


# Generated at 2022-06-12 23:41:17.577820
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible import module_utils

    class A:
        platform = 'linux'
        distribution = 'redhat'

    class B(A):
        distribution = 'centos'

    class C(A):
        distribution = 'debian'

    class D(A):
        distribution = 'generic'

    class E(A):
        distribution = 'redhat'

    class F(A):
        distribution = 'OtherLinux'

    class G(A):
        pass

    class H(A):
        distribution = 'redhat'
        platform = 'linux2'

    class I(A):
        distribution = 'redhat'
        platform = 'darwin'

    module_utils.PLATFORM = 'linux2'  # pylint: disable=assigning-non-slot

# Generated at 2022-06-12 23:41:22.434095
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        pass
    class B(A):
        pass
    class C(B):
        pass

    assert C == get_platform_subclass(C)
    assert B == get_platform_subclass(B)
    assert A == get_platform_subclass(A)

# Generated at 2022-06-12 23:41:30.699112
# Unit test for function get_distribution_version
def test_get_distribution_version():
    from distutils.spawn import find_executable
    import tempfile

    def version_extractor(osrelease_version, lsb_release_version):
        with tempfile.TemporaryDirectory(prefix='ansible_test_distro_') as tempdir:
            if osrelease_version is not None:
                with open(os.path.join(tempdir, 'os-release'), mode='w') as f:
                    f.write('ID=foo\nVERSION=%s\n' % osrelease_version)
                distro_test_path = os.path.join(tempdir, 'distro_test_distro.py')

# Generated at 2022-06-12 23:41:32.390072
# Unit test for function get_distribution
def test_get_distribution():
    _distro = get_distribution()
    assert _distro is not None


# Generated at 2022-06-12 23:41:42.343008
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Foo:
        platform = 'Linux'
        distribution = None

    class FooLinux(Foo):
        platform = 'Linux'
        distribution = None

    class OtherLinux(FooLinux):
        platform = 'Linux'
        distribution = 'OtherLinux'

    class FooLinuxAmazon(Foo):
        platform = 'Linux'
        distribution = 'Amazon'

    class FooLinuxDebian(Foo):
        platform = 'Linux'
        distribution = 'Debian'

    class FooLinuxUbuntu(FooLinuxDebian):
        platform = 'Linux'
        distribution = 'Ubuntu'

    class FooLinuxUbuntuXenial(FooLinuxUbuntu):
        platform = 'Linux'
        distribution = 'Ubuntu'
        codename = 'xenial'


# Generated at 2022-06-12 23:41:48.003276
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import platform
    import ansible.module_utils.basic
    import ansible.module_utils.facts

    def assert_subclass(expected, *args):
        actual = get_platform_subclass(ansible.module_utils.facts.FactsBase(*args))
        assert actual == expected, "Expected '%s' to be a subclass of %s but got %s" % (actual.__name__, expected.__name__, actual)

    # Just the platform
    assert_subclass(ansible.module_utils.facts.FactsBase, platform.system())
    assert_subclass(ansible.module_utils.facts.FactsBase, platform.system(), None)
    assert_subclass(ansible.module_utils.facts.FactsBase, platform.system(), 'NotADistro')

    # Test a platform_

# Generated at 2022-06-12 23:41:59.079462
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils.basic import AnsibleModule

    class PlatformA(object):
        platform = 'A'
        distribution = None

    class PlatformADistro(object):
        platform = 'A'
        distribution = 'Distro'

    class PlatformB(object):
        platform = 'B'
        distribution = None

    class PlatformBDistro(object):
        platform = 'B'
        distribution = 'Distro'


# Generated at 2022-06-12 23:42:09.668585
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Verify the function returns expected results for known distros.

    This function was used to verify the results of the function get_distribution()
    when run on a set of known distros.  It is used to test the code in that function and
    should not be run as part of unit or integration testing.
    '''

    distributions = {
        'centos': 'Redhat',
        'debian': 'Debian',
        'fedora': 'Fedora',
        'oracle': 'Redhat',
        'rhel': 'Redhat',
        'ubuntu': 'Ubuntu',
    }
    for key in distributions:
        with open('/etc/' + key + '-release', 'w') as f:
            f.write('foo bar')
        assert get_distribution() == distributions[key]

    # This is the

# Generated at 2022-06-12 23:42:19.367135
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        platform = "Base"
        distribution = None

    class Foo:
        platform = "Foo"
        distribution = None

    class FooBar(Foo):
        distribution = "Bar"

    class FooBaz(Foo):
        distribution = "Baz"

    class FooBax(FooBar):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class Linux(Base):
        platform = "Linux"

    class LinuxBar(Linux):
        distribution = "Bar"

    class LinuxBaz(Linux):
        distribution = "Baz"

    class LinuxFoo(Linux):
        distribution = "Foo"

    class LinuxBazBax(LinuxBaz, FooBax):
        pass


# Generated at 2022-06-12 23:42:27.170564
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class TestSuperClass:
        platform = None
        distribution = None

    class TestSubClass1(TestSuperClass):
        platform = "A Test Platform 1"
        distribution = "A Test Distribution 1"

    class TestSubClass2(TestSuperClass):
        platform = "A Test Platform 2"
        distribution = "A Test Distribution 2"

    class TestSubClass3(TestSuperClass):
        platform = "A Test Platform 3"
        distribution = None

    class TestSubClass4(TestSuperClass):
        platform = "A Test Platform 4"
        distribution = "A Test Distribution 4"

    class TestSubClass5(TestSuperClass):
        platform = "A Test Platform 5"
        distribution = None

    class TestSubClass6(TestSubClass5):
        platform = "A Test Platform 6"
        distribution = "A Test Distribution 2"

# Generated at 2022-06-12 23:42:35.617892
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    if platform.system() != 'Linux':
        pass
    else:
        print(get_distribution_codename())


# Generated at 2022-06-12 23:42:42.887993
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import sys

    class Base(object):
        platform = 'Base'
        distribution = None

    class Other(Base):
        platform = 'Other'
    class OtherLinux(Other):
        platform = 'Linux'
        distribution = 'OtherLinux'
    class Linux(Base):
        platform = 'Linux'
        distribution = None
    class LinuxDebian(Linux):
        distribution = 'LinuxDebian'
    class LinuxUbuntu(Linux):
        distribution = 'LinuxUbuntu'

    class Windows(Base):
        platform = 'Windows'
        distribution = None
    class LinuxRedhat(Linux):
        distribution = 'LinuxRedhat'
    class LinuxRedHat(Linux):
        distribution = 'LinuxRedHat'
    class LinuxRedHat6(LinuxRedhat):
        platform_version = '6'

    # Assert subclass of Base


# Generated at 2022-06-12 23:42:49.931264
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import platform
    import distro

    # Ubuntu
    distro.id = lambda: 'Ubuntu'
    get_distribution_codename.__globals__.__setitem__('distro', distro)
    assert get_distribution_codename() == 'xenial'

    # Fedora
    platform.system = lambda: 'Linux'
    distro.id = lambda: 'fedora'
    get_distribution_codename.__globals__.__setitem__('platform', platform)
    assert get_distribution_codename() == None

# Generated at 2022-06-12 23:42:58.674479
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class FooSub(object):
        platform = 'ThisPlatform'
        distribution = None

    class FooSubSub(FooSub):
        platform = 'ThisPlatform'
        distribution = 'ThisDistro'

    class Foo(object):
        platform = 'OtherPlatform'
        distribution = None

    class FooDistro(object):
        platform = 'OtherPlatform'
        distribution = 'ThisDistro'

    class FooDistroSub(object):
        platform = 'OtherPlatform'
        distribution = 'ThisOtherDistro'

    platform.system = lambda: 'ThisPlatform'
    get_distribution = lambda: 'ThisDistro'

    assert get_platform_subclass(Foo) is FooSub
    assert get_platform_subclass(FooDistro) is FooDistroSub

# Generated at 2022-06-12 23:43:02.704086
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test function get_distribution_codename()
    '''
    codename = get_distribution_codename()
    if platform.system() != 'Linux':
        assert codename is None
    else:
        assert type(codename) == str



# Generated at 2022-06-12 23:43:12.822294
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    from ansible.module_utils.common._collections_compat import UserDict
    from ansible.module_utils.distro import (
        get_distribution,
        get_distribution_version,
        get_distribution_codename,
    )

    def _test_distro(distro_id, distro_codename, os_release, lsb_release):
        # create fake distros that return the correct info
        class FakeDistro:
            @staticmethod
            def id():
                return distro_id

            @staticmethod
            def codename():
                return distro_codename

            @staticmethod
            def version():
                return None

            @staticmethod
            def os_release_info():
                return UserDict(os_release)


# Generated at 2022-06-12 23:43:21.556176
# Unit test for function get_distribution_version
def test_get_distribution_version():
    try:
        import unittest
    except ImportError:
        raise SkipTest("unittest2 is needed to run the Ansible test suite")

    class DistributionVersionTestCase(unittest.TestCase):

        def test_redhat(self):
            self.assertEqual(get_distribution_version(), u'7.6')

        def test_ubuntu(self):
            self.assertEqual(get_distribution_version(), u'16.04')

        def test_windows(self):
            self.assertEqual(get_distribution_version(), None)

    # Unit test for function get_distribution_codename
    class DistributionCodenameTestCase(unittest.TestCase):

        def test_redhat(self):
            self.assertEqual(get_distribution_codename(), None)


# Generated at 2022-06-12 23:43:32.868038
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    import os
    import tempfile


# Generated at 2022-06-12 23:43:41.352341
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class TestPlatform(object):
        distribution = None
        platform = None
        def __init__(self, args, kwargs):
            pass
    class TestPlatformDefault(TestPlatform):
        platform = None
    class TestPlatformLinux(TestPlatform):
        platform = 'Linux'
    class TestPlatformRedhat(TestPlatformLinux):
        distribution = 'Redhat'
    class TestPlatformCentOS(TestPlatformLinux):
        distribution = 'CentOS'
    class TestPlatformLinuxDefault(TestPlatformLinux):
        distribution = None
    class TestPlatformSolaris(TestPlatform):
        platform = 'Solaris'
    class TestPlatformSolarisDefault(TestPlatformSolaris):
        distribution = None
    test_platforms = get_platform_subclass(TestPlatform)

    # Test if get_platform_subclass works as expected
    assert test_platform

# Generated at 2022-06-12 23:43:42.298035
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == 'xenial'

# Generated at 2022-06-12 23:44:06.448218
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Unit test to test get_distribution_codename() function
    '''

# Generated at 2022-06-12 23:44:17.143835
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    import tempfile
    import textwrap

    from ansible.module_utils._text import to_bytes

    from ansible.module_utils.facts import default

    class SampleA(default.DefaultFactCollector):

        platform = None
        distribution = None

        def collect(self, module=None, collected_facts=None):
            return dict(distribution=self.distribution, platform=self.platform)

    class SampleB(SampleA):

        platform = 'Linux'
        distribution = 'LinuxMint'

    class SampleC(SampleA):

        platform = 'Linux'
        distribution = 'Ubuntu'

    class SampleD(SampleA):

        platform = 'Linux'
        distribution = 'OtherLinux'

    class SampleE(SampleA):

        platform = 'Linux'
        distribution = None


# Generated at 2022-06-12 23:44:28.224533
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # Initialize
    real_distro_id = distro.id()
    real_codename = distro.codename()
    real_os_release_info = distro.os_release_info()
    real_lsb_release_info = distro.lsb_release_info()

    distro.id = lambda: 'fedora'
    distro.codename = lambda: ''
    distro.os_release_info = lambda: {'version_codename': ''}
    distro.lsb_release_info = lambda: {'codename': ''}

    # Test
    assert get_distribution_codename() is None

    distro.id = lambda: 'ubuntu'
    distro.codename = lambda: ''

# Generated at 2022-06-12 23:44:29.295951
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == platform.system().capitalize()


# Generated at 2022-06-12 23:44:35.118991
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    A function for testing the get_platform_subclass() function.

    It should be possible to run it with ``python -m ansible.module_utils.facts``.
    '''

    class myBase():
        distribution = None
        platform = 'base'

    class myLinux(myBase):
        platform = 'Linux'

    class myLinux_Redhat(myLinux):
        distribution = 'Redhat'

    class myLinux_Amazon(myLinux):
        distribution = 'Amazon'

    class myLinux_RedHat_7(myLinux_Redhat):
        distribution_version = '7'

    class myLinux_RedHat_6(myLinux_Redhat):
        distribution_version = '6'


# Generated at 2022-06-12 23:44:38.038020
# Unit test for function get_distribution_version
def test_get_distribution_version():
    pytest.importorskip("distro")
    assert get_distribution_version() == u'2.7.15+'

# Generated at 2022-06-12 23:44:47.793091
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    # Test for Ubuntu Xenial
    with open('/etc/os-release', 'w') as f:
        f.write('''
NAME="Ubuntu"
VERSION="16.04.4 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.4 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
''')
    assert get_distribution_codename() == 'xenial'

    # Test for Ubuntu Xenial - old style

# Generated at 2022-06-12 23:44:53.047618
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Unit test for function get_distribution_codename
    '''
    res = get_distribution_codename()
    assert not res or isinstance(res, basestring), 'get_distribution_codename should return None on non Linux or a string'

# Generated at 2022-06-12 23:45:00.865711
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class OpenBSDUser:
        platform = 'OpenBSD'
        distribution = None

        def __init__(self, *args, **kwargs):
            pass
    class BSDUser:
        platform = 'BSD'
        distribution = None

        def __init__(self, *args, **kwargs):
            pass
    class GenericUser:
        platform = None
        distribution = None

        def __init__(self, *args, **kwargs):
            pass

    import sys
    orig_platform_system = platform.system
    orig_distro_id = distro.id

    platform.system = lambda: 'OpenBSD'
    distro.id = lambda: 'OpenBSD'
    assert get_platform_subclass(GenericUser) is OpenBSDUser
    assert get_platform_subclass(BSDUser) is OpenBSDUser


# Generated at 2022-06-12 23:45:09.544304
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import ansible
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.common.dict_transformations import recursive_diff

    class BaseClass:
        pass

    class ThisPlatform(BaseClass):
        platform = platform.system()
        distribution = None

    class ThisPlatformThisDistro(BaseClass):
        platform = platform.system()
        distribution = get_distribution()

    assert get_platform_subclass(BaseClass) is BaseClass
    if get_distribution() is not None:
        assert get_platform_subclass(BaseClass) is not ThisPlatform
        assert get_platform_subclass(BaseClass) is ThisPlatformThisDistro
    else:
        assert get_platform_subclass(BaseClass) is ThisPlatform

# Generated at 2022-06-12 23:45:41.567312
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        platform = None
        distribution = None

    class Linux(Base):
        platform = "Linux"

    class OtherLinux(Linux):
        distribution = "OtherLinux"

    class Centos(Linux):
        distribution = "Centos"

    class Centos7(Centos):
        distribution_version = "7"

    class Centos6(Centos):
        distribution_version = "6"

    class Centos5(Centos):
        distribution_version = "5"

    class Debian(Linux):
        distribution = "Debian"

    class Debian8(Debian):
        distribution_version = "8"

    class Debian7(Debian):
        distribution_version = "7"

    class Mac(Base):
        platform = "Darwin"


# Generated at 2022-06-12 23:45:52.696967
# Unit test for function get_distribution
def test_get_distribution():
    # Test all known Linux distributions
    assert get_distribution() == "Amazon"
    assert get_distribution() == "Arch"
    assert get_distribution() == "Debian"
    assert get_distribution() == "Fedora"
    assert get_distribution() == "Freebsd"
    assert get_distribution() == "Gentoo"
    assert get_distribution() == "Linuxmint"
    assert get_distribution() == "Macosx"
    assert get_distribution() == "Openbsd"
    assert get_distribution() == "Opensuse"
    assert get_distribution() == "Otherlinux"
    assert get_distribution() == "Redhat"
    assert get_distribution() == "Slackware"
    assert get_distribution() == "Solaris"
    assert get_dist

# Generated at 2022-06-12 23:46:04.135497
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Foo:
        pass

    class FooLinux(Foo):
        platform = 'Linux'

    class FooRedhat(FooLinux):
        distribution = 'Redhat'

    class FooOtherLinux(FooLinux):
        distribution = 'OtherLinux'

    class FooUbuntu(FooLinux):
        distribution = 'Ubuntu'

    class FooWindows(Foo):
        platform = 'Windows'

    class FooWindows2(FooWindows):
        distribution = 'Windows'

    # Test Linux platform
    assert get_platform_subclass(Foo) == FooLinux

    # Test Redhat/CentOS
    assert get_platform_subclass(FooLinux) == FooRedhat
    assert get_platform_subclass(Foo) == FooRedhat

    # Test Amazon Linux

# Generated at 2022-06-12 23:46:14.424718
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    This is specifically for testing get_platform_subclass

    This tests the following:

    * using a class with no subclasses
    * using a class with a subclass for the current platform
    * using a class with a subclass for a specific version of the current platform
    * using a class with a subclass for a specific platform
    * using a class with multiple subclasses for a specific platform
    '''

    class A:
        platform = None
        distribution = None

    class B:
        platform = platform.system()
        distribution = None

    class C:
        platform = platform.system()
        distribution = get_distribution()

    class D:
        platform = 'Not' + platform.system()
        distribution = get_distribution()

    class E:
        platform = platform.system()
        distribution = get_distribution()

   

# Generated at 2022-06-12 23:46:20.617645
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    distro_id = distro.id()
    if distro_id == 'debian':
        assert get_distribution_codename() == 'stretch'
    elif distro_id == 'ubuntu':
        assert get_distribution_codename() == 'xenial'
    elif distro_id == 'centos':
        assert get_distribution_codename() == 'Core'

# Generated at 2022-06-12 23:46:30.477591
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Unit test for function get_platform_subclass

    This runs an actual unit test for the function get_platform_subclass.  This function
    should return a class that's an implementation for the platform it is running on.
    The unit test ensures that it returns the correct subclass.

    The unittest module is being utilized here although the function is defined in a separate file.
    The unittest module is only available in python 2.7 or higher, so if the module is imported, it
    is assumed that python 2.7 or higher is used.

    If the test fails, the message attribute of the AssertionError can be used to verify which module
    is selected for the platform it is running on.
    '''
    try:
        import unittest
    except ImportError:
        exit()

    class Base(object):
        platform = None

# Generated at 2022-06-12 23:46:41.128341
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test for function get_platform_subclass
    '''
    # The tests are implemented here to avoid unnecessary module loading in production code
    # Here the assumption is the function get_distribution() will return 'Darwin' and
    # get_distribution_version() will return '10.12.6'
    class SourceClass:
        '''
        SourceClass is the base class for the test
        '''

        platform = None
        distribution = None

    class Subclass1(SourceClass):
        '''
        Subclass1 is a subclass that will not be matched
        '''

        platform = 'Darwin'
        distribution = '11.0.1'

    class Subclass2(SourceClass):
        '''
        Subclass2 is a subclass that will not be matched
        '''

        platform = 'Darwin'



# Generated at 2022-06-12 23:46:51.147963
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Create a base class called A that has subclasses called A1, A2, and A3
    class A(object):
        def __init__(self):
            pass

    class A1(A):
        platform = 'linux'

    class A2(A):
        platform = 'Other'
        distribution = 'OtherLinux'

    class A3(A):
        platform = 'Other'
        distribution = 'Other'

    # Determine which subclass is correct
    Linux = 'linux'
    OtherLinux = 'OtherLinux'
    Other = 'Other'
    if platform.system() == Linux:
        assert get_platform_subclass(A).__name__ == A1.__name__
    elif get_distribution() == OtherLinux:
        assert get_platform_subclass(A).__name__ == A2.__name

# Generated at 2022-06-12 23:47:00.925424
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class PlatformSpecificUser:
        platform = 'Linux'
        distribution = None

    class LinuxUser:
        platform = 'Linux'
        distribution = None

    class DebianUser:
        platform = 'Linux'
        distribution = 'Debian'

    class OtherLinuxUser:
        platform = 'Linux'
        distribution = 'OtherLinux'

    class FreeBSDUser:
        platform = 'FreeBSD'
        distribution = None

    class FakeUser(PlatformSpecificUser, LinuxUser, FreeBSDUser, OtherLinuxUser, DebianUser):
        pass

    class User:
        platform = 'Linux'
        distribution = 'OtherLinux'

    assert get_platform_subclass(FakeUser) is PlatformSpecificUser
    assert get_platform_subclass(User) is User

# Generated at 2022-06-12 23:47:10.272407
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class BaseClass():
        pass
    class Linux(BaseClass):
        platform = 'Linux'
    class OtherLinux(BaseClass):
        platform = 'Linux'
        distribution = 'OtherLinux'
    class RedHat(BaseClass):
        platform = 'Linux'
        distribution = 'Redhat'
    class Amazon(BaseClass):
        platform = 'Linux'
        distribution = 'Amazon'
    class Windows(BaseClass):
        platform = 'Windows'
    class Darwin(BaseClass):
        platform = 'Darwin'
    class FreeBSD(BaseClass):
        platform = 'FreeBSD'
    class SunOS(BaseClass):
        platform = 'SunOS'

    # Linux
    assert get_platform_subclass(BaseClass) == Linux
    assert get_platform_subclass(Linux) == Linux
    assert get_platform_subclass

# Generated at 2022-06-12 23:48:06.140800
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    ''' Test the get_platform_subclass function

    This is one of the rare unit tests that requires the platform to be Linux
    since that's the only platform we have multiple implementations for.
    '''
    if platform.system() != 'Linux':
        # Skip the test if we're not on Linux
        return
    import test_utils

    cls = test_utils.MockOsDistributionClass()
    distro_instance = get_platform_subclass(cls)
    assert distro_instance.__class__ is not cls, 'The get_platform_subclass should not have returned the original class'
    assert distro_instance.__class__.__name__ == 'MyClass', 'The get_platform_subclass should have returned MyClass'

    cls = test_utils.MockOsDistributionSubclass
    distro_
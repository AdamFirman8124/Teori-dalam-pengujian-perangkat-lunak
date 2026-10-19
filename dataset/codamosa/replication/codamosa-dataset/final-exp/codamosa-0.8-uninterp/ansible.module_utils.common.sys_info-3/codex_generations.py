

# Generated at 2022-06-12 23:38:12.248522
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == u'xenial'

# Generated at 2022-06-12 23:38:23.446964
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        pass
    class B:
        pass
    class C(B):
        pass
    class D(A):
        pass
    class E(C, D):
        pass
    class F(C, D):
        pass
    class G(E, F):
        pass
    class H:
        distribution = 'Ubuntu'
    class I(H):
        pass
    class J(H):
        pass
    class K:
        platform = 'Linux'
    class L(K):
        pass
    class M(K):
        pass

    assert get_platform_subclass(A) == A
    assert get_platform_subclass(B) == B
    assert get_platform_subclass(C) == C
    assert get_platform_subclass(D) == D
    assert get_platform_

# Generated at 2022-06-12 23:38:28.072835
# Unit test for function get_distribution
def test_get_distribution():
    """
    Tests for function get_distribution
    """
    from ansible.module_utils import basic
    import pytest

    class DistroLinux(distro.LinuxDistribution):
        """
        A fake LinuxDistribution class that returns a set of known values
        """
        def __init__(self):
            self.id = 'test-distro'
            self.name = 'TestDistro'
            self.version = '1.0'
            self.codename = 'codename'

    class DistroNotLinux(Exception):
        """
        A fake LinuxDistribution subclass that throws an exception when it
        is called.
        """
        pass

    # Test that get_distribution() returns a string when a distro is specified

# Generated at 2022-06-12 23:38:38.460506
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        platform = 'Linux'
        distribution = None

    class B(A):
        distribution = 'RedHat'

    class C(A):
        distribution = 'RedHat'
        platform = 'Windows'

    class D(C):
        pass

    class E(D):
        platform = 'Linux'
        distribution = 'RedHat'

    class F:
        platform = 'Linux'
        distribution = 'RedHat'

    assert get_platform_subclass(A) is A
    assert get_platform_subclass(B) is B
    assert get_platform_subclass(C) is C
    assert get_platform_subclass(D) is D
    assert get_platform_subclass(E) is E
    assert get_platform_subclass(F) is F


# Generated at 2022-06-12 23:38:50.336924
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    from ansible.module_utils import basic

    # Test for basic.AnsibleModule
    class TestClass(basic.AnsibleModule):
        platform = 'Linux'
        distribution = None
        dummy1 = "dummy"

    class TestClass_Linux(TestClass):
        platform = 'Linux'
        distribution = None
        dummy2 = "dummy"

    class TestClass_Linux_Redhat(TestClass):
        platform = 'Linux'
        distribution = 'Redhat'
        dummy3 = "dummy"

    class TestClass_Linux_Amazon(TestClass):
        platform = 'Linux'
        distribution = 'Amazon'
        dummy4 = "dummy"

    class TestClass_Windows(TestClass):
        platform = 'Windows'
        distribution = None
        dummy5 = "dummy"


# Generated at 2022-06-12 23:38:55.227903
# Unit test for function get_distribution
def test_get_distribution():
    import distro
    distro.id = lambda: 'redhat'
    assert get_distribution() == u'Redhat'
    distro.id = lambda: 'centos'
    assert get_distribution() == u'Centos'
    distro.id = lambda: 'fedora'
    assert get_distribution() == u'Fedora'
    distro.id = lambda: 'debian'
    assert get_distribution() == u'Debian'
    distro.id = lambda: 'ubuntu'
    assert get_distribution() == u'Ubuntu'
    distro.id = lambda: 'SuSE'
    assert get_distribution() == u'SuSE'
    distro.id = lambda: 'openSUSE'
    assert get_distribution() == u'SuSE'

# Generated at 2022-06-12 23:39:02.754687
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Basic working case
    class MainClass():
        platform = 'TestPlatform'
        distribution = None

    class MainClassSubclassA(MainClass):
        distribution = 'foo'

    class MainClassSubclassB(MainClass):
        platform = 'blah'

    class MainClassSubclassC(MainClass):
        platform = 'TestPlatform'
        distribution = 'foo'

    assert get_platform_subclass(MainClass) == MainClass
    assert get_platform_subclass(MainClassSubclassA) == MainClassSubclassA
    assert get_platform_subclass(MainClassSubclassB) == MainClass
    assert get_platform_subclass(MainClassSubclassC) == MainClassSubclassC

    # Real world case
    from ansible.module_utils.basic import get_platform_subclass as get_platform_sub

# Generated at 2022-06-12 23:39:11.967578
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import unittest2 as unittest
    class TestSuper:
        platform = 'Linux'
        distribution = None

    class TestRedhat(TestSuper):
        distribution = 'Redhat'

    class TestRedhat6(TestRedhat):
        distribution_version = '6'

    class TestRedhat7(TestRedhat):
        distribution_version = '7'

    class TestAmazon(TestRedhat):
        distribution = 'Amazon'

    class TestAmazon2(TestAmazon):
        distribution_version = '2'

    class TestAmazon1(TestAmazon):
        distribution_version = '1'

    class TestOtherLinux(TestSuper):
        platform = 'Linux'
        distribution = 'OtherLinux'

    class TestOtherLinux3(TestOtherLinux):
        distribution_version = '3'


# Generated at 2022-06-12 23:39:14.023878
# Unit test for function get_distribution
def test_get_distribution():
    distribution = get_distribution()
    assert distribution


# Generated at 2022-06-12 23:39:15.339250
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == get_distribution_version() == get_distribution_codename()

# Generated at 2022-06-12 23:39:30.755265
# Unit test for function get_distribution_codename

# Generated at 2022-06-12 23:39:37.096301
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # Setup: Create a set of parent/child classes
    class Base(object):
        platform='Linux'
        distribution=None
    class Derived(Base):
        platform='Linux'
        distribution=None
    class Derived2(Base):
        platform='Linux'
        distribution='Derived2Distro'
    class Derived3(Base):
        platform='Derived3Platform'
        distribution='Derived3Distro'

    # Test: getting subclass of Base
    subclass = get_platform_subclass(Base)
    assert subclass == Base

    # Test: getting subclass of Derived when platform and distribution is None
    subclass = get_platform_subclass(Derived)
    assert subclass == Base

    # Test: getting subclass of Derived2 when platform and distribution is None
    subclass = get_platform_subclass(Derived2)


# Generated at 2022-06-12 23:39:48.469083
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class X(object):
        platform = None
        distribution = None
    class XAIX(X):
        platform = 'AIX'
        distribution = None
    class XUnix(X):
        platform = 'Unix'
        distribution = None
    class Xlinux(X):
        platform = 'Linux'
        distribution = None
    class XLinuxRedhat(Xlinux):
        platform = 'Linux'
        distribution = 'Redhat'
    class XLinuxDebian(Xlinux):
        platform = 'Linux'
        distribution = 'Debian'
    class XLinuxCaldera(Xlinux):
        platform = 'Linux'
        distribution = 'Caldera'
    class XLinuxMandrake(XLinuxRedhat):
        platform = 'Linux'
        distribution = 'Mandrake'

# Generated at 2022-06-12 23:39:57.483225
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class BaseClass:
        pass

    class SubClass1(BaseClass):
        distribution = None
        platform = 'Linux'

    class SubClass2(BaseClass):
        distribution = 'Debian'
        platform = 'Linux'

    class SubClass3(BaseClass):
        distribution = 'Centos'
        platform = 'Linux'

    class SubClass4(BaseClass):
        distribution = None
        platform = 'Windows'

    assert get_platform_subclass(BaseClass).__name__ == 'BaseClass'
    assert get_platform_subclass(BaseClass).__name__ == 'BaseClass'

    # we expect that the most specific subclass will be chosen so
    # SubClass2 will be chosen
    assert get_platform_subclass(BaseClass).__name__ == 'SubClass2'

    # we now set the distribution to Cent

# Generated at 2022-06-12 23:40:03.903532
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Returns a tuple of strings that can be used by an assert statement
    to ensure that a Linux distribution returns the appropriate codename
    '''
    class TestError(Exception):
        pass

    distro_codename_list = {
        'debian': 'buster',
        'centos': '14',
        'fedora': 'Fedora',  # Fedora bug 954104
        'ubuntu': 'xenial',
        'SuSE': 'Tumbleweed'  # Open SuSE bug 954104
    }

    # Test an OS whose codename is returned in distro.codename()

# Generated at 2022-06-12 23:40:16.659797
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Make sure that get_platform_subclass can find the appropriate subclass
    given the class and platform distribution
    '''
    # AT THE MOMENT, this is just a stub.  The actual unit test is in
    # test/units/modules/test_platform.py
    # because we can't load the chunked module for unit testing

    # For that unit test, we need the Linux class to be a parent class
    class Linux:
        platform = 'Linux'

    # Also have a fake class that represents a specific platform
    class FakeLinux(Linux):
        platform = 'Fake'
        distribution = 'Fake'

    # Now we need a test that it'll return the best match for a given
    # platform distribution
    my_linux = Linux()
    my_fake = FakeLinux()
    assert get_platform_subclass(Linux)

# Generated at 2022-06-12 23:40:25.631139
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class a(object):
        platform = 'linux'
        distribution = 'SomeLinux'

    class aa(a):
        distribution = 'OtherLinux'

    class aaa(aa):
        distribution = 'YetAnotherLinux'

    class b(a):
        distribution = None

    class c(a):
        platform = 'Other'

    class d(a):
        platform = 'linux'
        distribution = 'WindowsNT'

    assert get_platform_subclass(a) == a
    assert get_platform_subclass(aa) == aa
    assert get_platform_subclass(aaa) == aaa
    assert get_platform_subclass(b) == b
    assert get_platform_subclass(c) == c
    assert get_platform_subclass(d) == a

# Generated at 2022-06-12 23:40:37.580990
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class Centos:
        platform = 'Linux'
        distribution = 'Centos'

    class Linux:
        platform = 'Linux'
        distribution = None

    class Windows:
        platform = 'Windows'
        distribution = None

    assert (get_platform_subclass(Centos) == Centos)
    assert (get_platform_subclass(Linux) == Linux)
    assert (get_platform_subclass(Windows) == Windows)

    class OtherLinux(Linux):
        platform = 'Linux'
        distribution = 'OtherLinux'

    assert (get_platform_subclass(Centos) == Centos)
    assert (get_platform_subclass(Linux) == OtherLinux)
    assert (get_platform_subclass(Windows) == Windows)

    class LinuxCentos(Centos):
        platform = 'Linux'

# Generated at 2022-06-12 23:40:41.150858
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Test that the distribution codename is retrieved correctly
    '''
    codename = get_distribution_codename()
    if codename is None:
        print("Platform is not Linux")
    else:
        print("Platform codename is " + codename)

if __name__ == '__main__':
    test_get_distribution_codename()

# Generated at 2022-06-12 23:40:51.106965
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test the return value for :py:func:`get_distribution()`
    which returns the name of the distribution you are on.
    '''
    from distutils.version import LooseVersion as V

    # Fedora
    assert(get_distribution() == 'Fedora')
    assert(get_distribution_version() == V('29'))
    assert(get_distribution_codename() is None)

    # Centos
    assert(get_distribution() == 'Centos')
    assert(get_distribution_version() == V('7.5.1804'))
    assert(get_distribution_codename() == 'Core')

    # Debian
    assert(get_distribution() == 'Debian')
    assert(get_distribution_version() == V('9'))

# Generated at 2022-06-12 23:41:11.135078
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class Base(object):
        pass

    class BaseLinux(Base):
        platform = "Linux"
        distribution = None

    class BaseOther(Base):
        platform = None
        distribution = None

    class Fedora(BaseLinux):
        distribution = "Fedora"

    class Rhel(BaseLinux):
        distribution = "Rhel"

    class Debian(BaseLinux):
        distribution = "Debian"

    assert get_platform_subclass(BaseLinux) == BaseLinux
    assert get_platform_subclass(BaseOther) == BaseOther
    assert get_platform_subclass(Fedora) == Fedora
    assert get_platform_subclass(Rhel) == Rhel
    assert get_platform_subclass(Debian) == Debian

    class Debian3(Debian):
        pass

    class Rhel2(Rhel):
        pass

# Generated at 2022-06-12 23:41:17.322978
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    # We can't import this from the unit tests because it will import from the
    # module being unit tested so we just copy the body of the function here
    class FakeTestA(object):
        platform = 'BSD'

    class FakeTestB(FakeTestA):
        platform = 'Linux'

    class FakeTestC(FakeTestB):
        distribution = 'A'

    class FakeTestD(FakeTestB):
        distribution = 'B'

    assert FakeTestB == get_platform_subclass(FakeTestA)
    assert FakeTestC == get_platform_subclass(FakeTestB)
    assert FakeTestD == get_platform_subclass(FakeTestB)

# Generated at 2022-06-12 23:41:19.625797
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    distribution_codename = get_distribution_codename()
    print(distribution_codename)

# Generated at 2022-06-12 23:41:27.440623
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() == None
    assert get_distribution_codename() == None
    assert get_distribution_codename() == None
    assert get_distribution_codename() == None
    assert get_distribution_codename() == None
    assert get_distribution_codename() == None
    assert get_distribution_codename() == None
    assert get_distribution_codename() == None
    assert get_distribution_codename() == None
    assert get_distribution_codename() == None



# Generated at 2022-06-12 23:41:29.838156
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() is not None

# Generated at 2022-06-12 23:41:40.338218
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # codename is not supported
    codename = get_distribution_codename()
    assert codename is None

    class TestDistro():
        pass
    test_distro = TestDistro()
    test_distro.id = lambda: 'linux'
    with patch('ansible.module_utils.distro', test_distro):
        codename = get_distribution_codename()
        assert codename is None

    class TestDistro():
        pass
    test_distro = TestDistro()
    test_distro.id = lambda: 'ubuntu'
    test_distro.codename = lambda: ''
    with patch('ansible.module_utils.distro', test_distro):
        codename = get_distribution_codename()
        assert codename is None


# Generated at 2022-06-12 23:41:52.192475
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Test for get_distribution()
    '''

    # OS X
    assert get_distribution() == 'Darwin'

    # CentOS
    for version in ('6.10', '7.5.1804', '8.1.1911'):
        with MockDistroInfo(id='centos', version=version):
            assert get_distribution() == 'Centos'
            assert get_distribution_version() == '.'.join(version.split('.')[:2])

    # Debian
    for version in ('7.11', '8.10', '9.13'):
        with MockDistroInfo(id='debian', version=version):
            assert get_distribution() == 'Debian'
            assert get_distribution_version() == version

    # Fedora

# Generated at 2022-06-12 23:41:53.401138
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    codename = get_distribution_codename()
    if not codename or codename == "NA":
        return False
    else:
        return True

# Generated at 2022-06-12 23:41:58.228148
# Unit test for function get_platform_subclass

# Generated at 2022-06-12 23:42:08.956036
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    '''
    Test cases to ensure that get_platform_subclass works.

    :returns: Nothing
    '''
    from ansible.module_utils.basic import AnsibleModule

    # Test if the code returns a subclass when a platform exists
    class TestSubclassModuleBase(object):
        pass

    class TestSubclassModule(TestSubclassModuleBase):
        platform = 'Linux'
        distribution = 'Redhat'

    assert TestSubclassModule == get_platform_subclass(TestSubclassModuleBase)

    # Test if the code returns the base class when no platform exists
    class TestNoSubclassModule(TestSubclassModuleBase):
        distribution = 'Redhat'

    assert TestSubclassModuleBase == get_platform_subclass(TestSubclassModuleBase)

    # Test if the code returns the base class when the platform exists but


# Generated at 2022-06-12 23:42:38.539252
# Unit test for function get_distribution
def test_get_distribution():
    '''
    Validates get_distribution() returns correct distribution name
    '''
    distro_map = {
        'amzn': 'Amazon',
        'arch': 'Archlinux',
        'centos': 'Redhat',
        'debian': 'Debian',
        'fedora': 'Fedora',
        'opensuse': 'OpenSuse',
        'oracle': 'OracleLinux',
        'rhel': 'Redhat',
        'ubuntu': 'Ubuntu',
        'otherlinux': None,
    }
    for distro_id in distro_map:
        distribution = distro_map[distro_id]
        result = get_distribution(distro_id)
        assert (result == distribution)

# Generated at 2022-06-12 23:42:40.164484
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == 'Fedora'


# Generated at 2022-06-12 23:42:50.583535
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        platform = None
        distribution = None
    class B(A):
        platform = 'Linux'
        distribution = 'Redhat'
    class C(A):
        platform = 'Linux'
        distribution = 'Debian'
    class D(A):
        platform = 'Linux'
    class E(B):
        distribution = 'Debian'
    class F(B):
        platform = 'Windows'
    class G(C):
        platform = 'Windows'

    # All classes defined
    assert A not in (B, C, D, E, F, G)
    assert B not in (C, D, E, F, G)
    assert C not in (D, E, F, G)
    assert D not in (E, F, G)
    assert E not in (F, G)

# Generated at 2022-06-12 23:42:54.146210
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    # Testing for Ubuntu. It should return the codename of the Ubuntu version.
    codename = get_distribution_codename()
    if "bionic" in codename:
        codename = True
    else:
        codename = False
    assert codename == True

# Generated at 2022-06-12 23:43:01.198649
# Unit test for function get_distribution_version
def test_get_distribution_version():
    import os
    import StringIO

    def get_distribution_version_test(version, id, lsb, os_release):
        for so in ('/etc/lsb-release', '/usr/bin/lsb_release'):
            if os.path.exists(so):
                os.environ['PATH'] = '/usr/bin:/bin'
                break
        if not os.path.exists(so):
            os.environ['PATH'] = '/bin:/usr/bin'
        distro.lsb_release = lambda: StringIO.StringIO(lsb)
        distro.version = lambda: version
        distro.id = lambda: id
        distro.os_release = lambda: StringIO.StringIO(os_release)

        return get_distribution_version()

    assert get_distribution_version

# Generated at 2022-06-12 23:43:12.035010
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    import ansible.module_utils.basic as basic
    import ansible.module_utils.basic.User as User
    # pylint: disable=no-member,redefined-outer-name
    class RHEL(User.User):
        platform = 'Linux'
        distribution = 'Redhat'
    class OtherLinux(User.User):
        platform = 'Linux'
        distribution = None
    class Windows(User.User):
        platform = 'Windows'
        distribution = None
    # pylint: enable=no-member,redefined-outer-name

    # RHEL
    with basic.change_system_info(platform='Linux', distribution='Redhat'):
        assert(get_platform_subclass(User.User) == RHEL)

    # Other Linux

# Generated at 2022-06-12 23:43:17.317386
# Unit test for function get_distribution_version
def test_get_distribution_version():
    from ansible.module_utils.common._collections_compat import Mapping

    distribution_version = get_distribution_version()

    assert(isinstance(distribution_version, (type(None), basestring)))
    if isinstance(distribution_version, basestring):
        # Returned value is not None, look for major.minor.point
        assert(len(distribution_version.split('.')) < 4)



# Generated at 2022-06-12 23:43:23.150607
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        platform = 'a'
        distribution = None

    class B(A):
        platform = 'b'

    class C(A):
        platform = 'c'

    class D(A):
        platform = 'd'
        distribution = 'foo'

    class E(B):
        distribution = 'foo'

    class F(B):
        pass

    class G(B):
        distribution = 'E'

    class H(B):
        distribution = 'F'

    class I(B):
        distribution = 'G'

    def mock_get_distribution(*args, **kwargs):
        return 'F'

    original_get_distribution = get_distribution
    get_distribution = mock_get_distribution


# Generated at 2022-06-12 23:43:32.689504
# Unit test for function get_platform_subclass
def test_get_platform_subclass():

    class BaseClass:
        platform = 'GenericPlatform'
        distribution = None

    class LinuxUbuntu(BaseClass):
        platform = 'Linux'
        distribution = 'Ubuntu'

    class LinuxFreeBSD(BaseClass):
        platform = 'FreeBSD'
        distribution = 'FreeBSD'

    class LinuxMint(LinuxUbuntu):
        platform = 'Linux'
        distribution = 'LinuxMint'

    assert get_platform_subclass(LinuxUbuntu) is LinuxUbuntu
    assert get_platform_subclass(LinuxFreeBSD) is LinuxFreeBSD
    assert get_platform_subclass(LinuxMint) is LinuxMint
    assert get_platform_subclass(BaseClass) is BaseClass

# Generated at 2022-06-12 23:43:33.663357
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert get_distribution_codename() is None

# Generated at 2022-06-12 23:44:06.331664
# Unit test for function get_distribution_codename
def test_get_distribution_codename():

    assert get_distribution_codename() is None

    distro.release_info = lambda: {'version_codename': 'bionic',
                                   'codename': 'bionic',
                                   'ubuntu_codename': 'bionic'}
    assert get_distribution_codename() == 'bionic'

    distro.release_info = lambda: {'version_codename': 'bionic',
                                   'codename': 'bionic'}
    assert get_distribution_codename() == 'bionic'

    distro.release_info = lambda: {'version_codename': None,
                                   'codename': 'bionic',
                                   'ubuntu_codename': 'bionic'}
    assert get_distribution_codename() == 'bionic'


# Generated at 2022-06-12 23:44:07.474805
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution()



# Generated at 2022-06-12 23:44:15.574601
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        distribution = None
        platform = 'Linux'

    class A(Base):
        distribution = 'Debian'
        platform = 'Linux'

    class B(Base):
        distribution = 'Centos'
        platform = 'Linux'

    assert get_platform_subclass(Base) == Base

    class C(Base):
        pass

    class D(C):
        distribution = 'Debian'

    assert get_platform_subclass(C) == C

    class E(C):
        platform = 'Linux'

    assert get_platform_subclass(C) == E

# Generated at 2022-06-12 23:44:26.790153
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class BaseClass:
        pass

    class SubClass(BaseClass):
        platform = 'Linux'
        distribution = ''

    class SubClass1(BaseClass):
        platform = 'Linux'
        distribution = 'Redhat'

    class SubClass2(BaseClass):
        platform = 'Linux'
        distribution = 'centos'

    class SubClass3(BaseClass):
        platform = 'FreeBSD'
        distribution = ''

    # The function should return the most specific subclass
    # distribution not given, returns the subclass with distribution name
    assert (get_platform_subclass(BaseClass) == SubClass)
    # distribution given, returns the subclass with distribution name
    assert (get_platform_subclass(BaseClass) == SubClass1)
    # distribution given, returns the subclass with distribution name

# Generated at 2022-06-12 23:44:33.338545
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        platform = 'Linux'

    class B(A):
        pass

    class C(B):
        platform = 'Windows'

    class D(B):
        distribution = 'Debian'

    class E(B):
        distribution = 'Redhat'

    class F(E):
        pass

    import ansible.module_utils.facts.system
    class G(ansible.module_utils.facts.system.System):
        platform = 'Linux'
        distribution = 'Debian'

    class H(ansible.module_utils.facts.system.System):
        distribution = 'Redhat'

    assert get_platform_subclass(A) == A
    assert get_platform_subclass(B) == B
    assert get_platform_subclass(C) == C

# Generated at 2022-06-12 23:44:35.402780
# Unit test for function get_distribution
def test_get_distribution():
    # FIXME: Need to figure out how to test this
    pass


# Generated at 2022-06-12 23:44:41.204878
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    We should return the code name of the distribution we're running on.

    :rtype: NativeString or None
    :returns: A string representing the code name or None if not a Linux distro
    '''
    assert get_distribution_codename() == 'bionic' or \
        get_distribution_codename() == 'focal'

# Generated at 2022-06-12 23:44:49.437337
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class Base:
        pass

    class One(Base):
        platform = 'Windows'
        distribution = None

    class Two(Base):
        platform = 'Windows'
        distribution = 'Microsoft'

    class Three(Base):
        platform = 'Linux'
        distribution = 'Redhat'

    class Four(Base):
        platform = 'Windows'
        distribution = 'Microsoft'

    class Five(Base):
        platform = 'Other'
        distribution = None

    # When we're on windows, we should get the most specific subclass, Two
    sub_cls = get_platform_subclass(Base, 'Windows', 'Microsoft')
    assert sub_cls in (Two, Four)

    # When we're on linux, we should get Three
    sub_cls = get_platform_subclass(Base, 'Linux', 'Redhat')


# Generated at 2022-06-12 23:44:51.552178
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    assert(get_distribution_codename() == 'xenial')


# Generated at 2022-06-12 23:44:57.033709
# Unit test for function get_distribution_version
def test_get_distribution_version():

    distro = get_distribution()
    version = get_distribution_version()

    if distro == 'Freebsd':
        assert version
        assert type(version) is str
    if distro == 'Openbsd':
        assert version
        assert type(version) is str
    if distro == 'Macos':
        assert version
        assert type(version) is str

# Generated at 2022-06-12 23:45:43.331088
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    class _Distro:
        def __init__(self, id, codename):
            self.id = id
            self.codename = codename

        def version(self, *args, **kwargs):
            return ''

        def version_best(self, *args, **kwargs):
            return ''

        def os_release_info(self, *args, **kwargs):
            return {}

    class _Platform:
        def __init__(self, system, distro):
            self.system = system
            self._distro = distro

        def dist(self):
            return self._distro

    class _OsReleaseInfo:
        def __init__(self, version_codename, ubuntu_codename):
            self.version_codename = version_codename
            self.ubuntu_codename = ubuntu_

# Generated at 2022-06-12 23:45:53.865818
# Unit test for function get_platform_subclass
def test_get_platform_subclass():
    class A:
        pass
    class LinuxA(A):
        platform = 'Linux'
        distribution = None
    class LinuxBAmazon(LinuxA):
        distribution = 'Amazon'
    class LinuxBRedhat(LinuxA):
        distribution = 'Redhat'
    class LinuxC(LinuxA):
        distribution = 'A'
    class LinuxD(LinuxA):
        distribution = 'B'
    class BSD(A):
        platform = 'Darwin'

    cls = get_platform_subclass(A)
    assert cls == A
    class Linux(A):
        platform = 'Linux'
        distribution = None
    cls = get_platform_subclass(Linux)
    assert cls == Linux
    class LinuxAndDistro(Linux):
        distribution = get_distribution()
    cls = get_

# Generated at 2022-06-12 23:46:01.397077
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    if get_distribution_codename() is None:
        return
    codename = get_distribution_codename()
    if not any(codename in distro for distro in ('bionic', 'tara', 'xenial', 'jessie', 'stretch', 'stretch', 'trusty', 'cosmic', 'disco', 'buster', 'wheezy')):
        raise AssertionError('Invalid codename returned: {0}'.format(codename))

# Generated at 2022-06-12 23:46:12.212537
# Unit test for function get_distribution
def test_get_distribution():
    """Test the output of 'get_distribution'
    """
    # Set up the test
    mocker.patch(
        'ansible.module_utils.distro.id',
        return_value = 'centos'
    )
    mocker.patch(
        'ansible.module_utils.distro.os_release_info',
        return_value = {'id': 'centos', 'version_id': '6'}
    )
    mocker.patch(
        'ansible.module_utils.distro.lsb_release_info',
        return_value = {}
    )
    mocker.patch(
        'platform.system',
        return_value = 'Linux'
    )

    rv = get_distribution()
    assert rv == 'Centos'

    # Check for the Other

# Generated at 2022-06-12 23:46:13.115568
# Unit test for function get_distribution_version
def test_get_distribution_version():
    assert get_distribution_version()

# Generated at 2022-06-12 23:46:16.727558
# Unit test for function get_distribution
def test_get_distribution():
    assert get_distribution() == get_distribution().capitalize(), 'distribution failed to capitalize'
    assert get_distribution() is None or isinstance(get_distribution(), str), 'distribution not correct type'



# Generated at 2022-06-12 23:46:27.975493
# Unit test for function get_distribution_version

# Generated at 2022-06-12 23:46:35.111124
# Unit test for function get_distribution
def test_get_distribution():

    with patch('platform.system') as mock_platform_system:
        # test Amazon Linux
        mock_platform_system.return_value = 'Linux'
        with patch('distro.id', return_value='amzn') as mock_distro_id:
            with patch('distro.version_best', return_value='2016.09.1'):
                distribution_info = get_distribution()
        mock_distro_id.assert_called_once_with()
        assert distribution_info == 'Amazon'

        # test Red Hat Linux
        mock_platform_system.return_value = 'Linux'

# Generated at 2022-06-12 23:46:43.984081
# Unit test for function get_distribution_version
def test_get_distribution_version():
    '''
    Test get_distribution_version function

    This tests the following distro version values.
    Values are in the form of:
    distro.version() - distro.version_best()
    '''

# Generated at 2022-06-12 23:46:46.941058
# Unit test for function get_distribution_codename
def test_get_distribution_codename():
    '''
    Ensure a distribution codename is properly returned for known distributions
    '''
    assert get_distribution_codename() == None
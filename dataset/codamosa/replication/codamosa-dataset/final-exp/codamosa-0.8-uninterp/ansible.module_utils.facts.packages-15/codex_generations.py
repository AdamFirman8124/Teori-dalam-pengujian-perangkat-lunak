

# Generated at 2022-06-13 02:09:19.693364
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class MyLibMgr(LibMgr):
        LIB = 'ansible.module_utils.facts.system.a_fake_lib'
    m = MyLibMgr()
    assert m._lib is None


# Generated at 2022-06-13 02:09:20.986889
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    c = CLIMgr()
    assert not c.is_available()
    assert c._cli is None



# Generated at 2022-06-13 02:09:24.235443
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    class TestCLIMgr(CLIMgr):

        CLI = 'ls'

    test_cli_mgr = TestCLIMgr()
    assert test_cli_mgr.is_available() == True

# Generated at 2022-06-13 02:09:25.877659
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr()._cli is None
    assert CLIMgr().__init__() is None


# Generated at 2022-06-13 02:09:32.273254
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    import mock
    from ansible.module_utils.facts import get_distribution
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgr

    class_mock = mock.MagicMock()
    class_mock.LIB = None
    class_mock.CLI = None

    pm = PkgMgr()
    try:
        pm.get_package_details('foobar')
    except NotImplementedError:
        pass
    except Exception as e:
        raise(Exception('Error during test_PkgMgr_get_package_details:  %s' % e))


# Generated at 2022-06-13 02:09:34.614263
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr()._cli is None
    assert not CLIMgr().is_available()


# Generated at 2022-06-13 02:09:43.377767
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # Create a dummy class called TestLibMgr
    class TestLibMgr(LibMgr):
        LIB = 'ansible.module_utils.common.netutils'

    # Create an instance of TestLibMgr
    lib_mgr = TestLibMgr()

    # The netutils module exists, so is_available() should return True
    assert lib_mgr.is_available()

    # Now make the netutils module nonexistent, so is_available() should return False
    TestLibMgr.LIB = 'ansible.module_utils.common.netutils_not_exist'
    assert not lib_mgr.is_available()


# Generated at 2022-06-13 02:09:45.509071
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pass


# Generated at 2022-06-13 02:09:46.409038
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert False, "Test not implemented"


# Generated at 2022-06-13 02:09:47.955578
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    a = CLIMgr()

    assert a.is_available()



# Generated at 2022-06-13 02:09:54.555123
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    pm = CLIMgr()
    # assert not pm.is_available() # uncomment this if you want to test on a machine which has no pkgmgr
    assert pm.is_available() is True


# Generated at 2022-06-13 02:09:57.276428
# Unit test for constructor of class LibMgr
def test_LibMgr():

    lib_mgr = LibMgr()
    assert lib_mgr._lib is None



# Generated at 2022-06-13 02:09:59.123347
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    apkg = CLIMgr()
    assert not hasattr(apkg, '_cli')



# Generated at 2022-06-13 02:10:00.425205
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    assert True is not False

# Generated at 2022-06-13 02:10:03.431525
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    """Unit test for method is_available of class CLIMgr

    :returns: None

    """
    test_mgr = CLIMgr()
    assert test_mgr.is_available() is None

# Generated at 2022-06-13 02:10:04.097175
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pass

# Generated at 2022-06-13 02:10:11.256629
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class TestPkgMgr(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return ['foo', 'bar']

        def get_package_details(self, package):
            ret = {'name': package,
                   'version': '1.0'}

            if package == 'foo':
                ret['vendor'] = 'acme'
            else:
                ret['vendor'] = 'nova'

            return ret

    pkmg = TestPkgMgr()
    installed_packages = pkmg.get_packages()
    assert 'foo' in installed_packages.keys()
    assert 'bar' in installed_packages.keys()
    assert len(installed_packages['foo']) == 1
    assert len(installed_packages['bar']) == 1
   

# Generated at 2022-06-13 02:10:12.735391
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

    class TestCLIMgr(CLIMgr):
        CLI = 'test'
    pkg_mgr = TestCLIMgr()
    assert pkg_mgr.is_available() == False

# Generated at 2022-06-13 02:10:15.002015
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert (PkgMgr.is_available is PkgMgr.is_available)

#Unit test for method is_available of class LibMgr

# Generated at 2022-06-13 02:10:19.444072
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pkg_mgr = CLIMgr()
    pkg_mgr.CLI = 'git'
    assert pkg_mgr.is_available() == True
    pkg_mgr.CLI = 'test'
    assert pkg_mgr.is_available() == False


# Generated at 2022-06-13 02:10:29.457805
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class TestPkgMgr(PkgMgr):
        def list_installed(self):
            return 'test'
    pkgMgr = TestPkgMgr()
    assert(pkgMgr.list_installed() == 'test')


# Generated at 2022-06-13 02:10:37.394337
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class SubPkgMgr(PkgMgr):
        def list_installed(self):
            return ['ansible-doc']

        def get_package_details(self, package):
            return {'name': package, 'version': '2.2.2.0'}

    # Test that method returns a dictionary, with the package name and version
    assert SubPkgMgr().get_package_details('ansible-doc') == {'name': 'ansible-doc', 'version': '2.2.2.0'}

# Generated at 2022-06-13 02:10:40.024958
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class TestCLIMgr(CLIMgr):
        CLI = 'test_CLIMgr'
    assert TestCLIMgr().CLI == 'test_CLIMgr'

# Generated at 2022-06-13 02:10:41.203317
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pm = PkgMgr()
    try:
        pm.is_available()
    except NotImplementedError:
        pass
    else:
        assert False


# Generated at 2022-06-13 02:10:45.567438
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pkg = PkgMgr()
    try:
        isavailable = pkg.is_available()
    except NotImplementedError:
        assert True
    except:
        assert False
    assert False



# Generated at 2022-06-13 02:10:46.862712
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    assert LibMgr.is_available(LibMgr) == False


# Generated at 2022-06-13 02:10:54.262005
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class MyPkgMgr(PkgMgr):

        def __init__(self):
            self.installed_packages = [
                'package1-1.0',
                'package2-2.0.1',
                'package3-3.1.1',
                'package4-4.0.1',
                'package5-5.0.1',
                'package5-5.0.2',
            ]
            super(MyPkgMgr, self).__init__()

        def is_available(self):
            return True

        def list_installed(self):
            return self.installed_packages

        def get_package_details(self, package):
            package_details = {}

# Generated at 2022-06-13 02:11:00.743567
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    print("testing class CLIMgr")
    class TestCLIMgr(CLIMgr):
        def __init__(self):
            super(TestCLIMgr, self).__init__()
    cli_mgr=TestCLIMgr()
    cli_mgr.CLI="echo"
    assert cli_mgr.is_available()
    cli_mgr.CLI="notexistcommand"
    assert not cli_mgr.is_available()



# Generated at 2022-06-13 02:11:03.745088
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cliMgr = CLIMgr()
    assert cliMgr._cli == None


# Generated at 2022-06-13 02:11:13.127141
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class MockPkgMgr(PkgMgr):
        def __init__(self):
            self.installed = []
            self.details = {}
            super(MockPkgMgr, self).__init__()

        def is_available(self):
            return True

        def list_installed(self):
            return self.installed

        def get_package_details(self, package):
            return self.details[package]

    package1_details1 = dict(name='package1', version='1.0')
    package1_details2 = dict(name='package1', version='2.0')
    package2_details = dict(name='package2', version='1.0')
    package3_details = dict(name='package3', version='1.0')
    mpm = MockPkgMgr()
    m

# Generated at 2022-06-13 02:11:29.850043
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():

    assert 'yumpkgmgr' in get_all_pkg_managers()
    assert 'dummypkgmgr' in get_all_pkg_managers()

# Generated at 2022-06-13 02:11:32.731449
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pkg = PkgMgr()
    assert type(pkg.get_packages()) == dict, "Return type of get_packages() must be dictionary"

# Generated at 2022-06-13 02:11:35.075127
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    assert LibMgr().is_available() == False

    class Test(LibMgr):
        LIB = 'sys'
    assert Test().is_available() == True


# Generated at 2022-06-13 02:11:36.260295
# Unit test for constructor of class LibMgr
def test_LibMgr():
    libm = LibMgr()
    assert libm is not None


# Generated at 2022-06-13 02:11:39.975740
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    try:
        libmgr = LibMgr()
        libmgr._lib = __import__('yum')
        assert libmgr.is_available()
    except ImportError:
        assert not libmgr.is_available()



# Generated at 2022-06-13 02:11:45.203520
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    '''
    Test that get_all_pkg_managers returns an expected number of package managers
    '''

    from ansible.module_utils.facts.packages import get_all_pkg_managers

    pkg_mgrs = get_all_pkg_managers()
    assert isinstance(pkg_mgrs, dict)
    assert len(pkg_mgrs) > 0

# Generated at 2022-06-13 02:11:46.927951
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pm = PkgMgr()
    assert pm.is_available() is None


# Generated at 2022-06-13 02:11:55.149407
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.facts import command
    import os
    import subprocess
    import tempfile

    tmpdir = tempfile.mkdtemp()
    (handle, tmpfile) = tempfile.mkstemp(dir=tmpdir)

    os.close(handle)
    os.remove(tmpfile)

    exists = os.path.exists(tmpfile)
    assert exists is False

    providers = ['ansible_test_module_utils/test' + os.sep + 'module_utils_package_fact.py']
    env = os.environ.get('PYTHONPATH')
    if env:
        providers.append(env)


# Generated at 2022-06-13 02:11:56.674819
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    assert PkgMgr.get_package_details(PkgMgr) is None


# Generated at 2022-06-13 02:12:00.282970
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    mgr = CLIMgr()
    assert isinstance(mgr,CLIMgr)
    assert mgr.is_available() == False


# Generated at 2022-06-13 02:12:30.061330
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr().CLI is None


# Generated at 2022-06-13 02:12:30.552697
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cm = CLIMgr()
    assert cm is not None

# Generated at 2022-06-13 02:12:32.774627
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    pm = CLIMgr()
    assert pm._cli is None

# Generated at 2022-06-13 02:12:41.297576
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    available_lib_mgr = LibMgr()
    not_available_lib_mgr = LibMgr()
    # Stub out __init__() to avoid a mixin test failure
    available_lib_mgr.__init__ = lambda self: None
    not_available_lib_mgr.__init__ = lambda self: None
    # Stub out _lib to simulate a library being available
    available_lib_mgr._lib = True
    assert available_lib_mgr.is_available() is True
    assert not_available_lib_mgr.is_available() is False


# Generated at 2022-06-13 02:12:47.403301
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class A(PkgMgr):
        def list_installed(self):
            return ['pkg1']

        def get_package_details(self, package):
            return {'name': 'pkg1', 'version': '1.0'}

    a = A()
    pkgs = a.get_packages()
    assert pkgs['pkg1'][0]['name'] == 'pkg1'
    assert pkgs['pkg1'][0]['version'] == '1.0'


# Generated at 2022-06-13 02:12:55.208278
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    list_packages = ['package1', 'package2']
    packages = {}
    packages_expected = {'package1': [{'name': 'package1', 'version': '1.0', 'source': 'test'}],
                         'package2': [{'name': 'package2', 'version': '2.0', 'source': 'test'}]}

    class TestClass(PkgMgr):
        def list_installed(self):
            return list_packages

        def get_package_details(self, package):
            return {'name': package, 'version': '%s.0' % package[-1], 'source': 'test'}

    class_obj = TestClass()
    packages = class_obj.get_packages()

    assert packages == packages_expected


# Generated at 2022-06-13 02:13:03.019691
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    """Check the method get_packages of class PkgMgr
    """
    class MockPkgMgr(object):
        """A mock of PkgMgr class
        """
        def list_installed(self):
            """list_installed method
            """
            return ['pack-1', 'pack-2']

        def get_package_details(self, package):
            """get_package_details method
            """
            return {'name': package.split('-')[1], 'version': '2.0'}

    expected_packages = {'1': [{'name': '1', 'version': '2.0', 'source': 'mockpkgmgr'}],
                         '2': [{'name': '2', 'version': '2.0', 'source': 'mockpkgmgr'}]}

    pkg

# Generated at 2022-06-13 02:13:12.500652
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class CLIMgrTest(CLIMgr):

        CLI = 'clitest'

        def list_installed(self):
            return ['package1-1.0', 'package2-2.0', 'package3-3.0']

        def get_package_details(self, package):
            package_details = {}
            if 'package1' in package:
                package_details['name'] = 'package1'
                package_details['version'] = '1.0'
            elif 'package2' in package:
                package_details['name'] = 'package2'
                package_details['version'] = '2.0'
            elif 'package3' in package:
                package_details['name'] = 'package3'
                package_details['version'] = '3.0'
            return package_details


# Generated at 2022-06-13 02:13:22.139782
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class test_class(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ["test_package1-2.0.0","test_package2-1.0.0"]
        def get_package_details(self, package):
            package_details = {}
            package_details['name'] = package.split('-')[0]
            package_details['version'] = package.split('-')[1]
            return package_details
    t = test_class()
    assert t.get_package_details("test_package1-2.0.0") == {'name': 'test_package1', 'version': '2.0.0'}


# Generated at 2022-06-13 02:13:23.416180
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert issubclass(LibMgr, PkgMgr)


# Generated at 2022-06-13 02:14:36.243692
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.facts.pkg_mgrs.gem import Gem
    from ansible.module_utils.facts.pkg_mgrs.npm import Npm
    from ansible.module_utils.facts.pkg_mgrs.pip import Pip
    from ansible.module_utils.facts.pkg_mgrs.pip3 import Pip3
    from ansible.module_utils.facts.pkg_mgrs.portage import Portage
    from ansible.module_utils.facts.pkg_mgrs.yum import Yum

    gem = Gem()
    npm = Npm()
    pip = Pip()
    pip3 = Pip3()
    portage = Portage()
    yum = Yum()

   

# Generated at 2022-06-13 02:14:41.547742
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # Testing a cli which is available
    class TestCLIMgr(CLIMgr):
        CLI = 'sh'

    t = TestCLIMgr()
    assert t.is_available()

    # Testing a cli which is not available
    class TestCLIMgr1(CLIMgr):
        CLI = 'notacommand'

    t1 = TestCLIMgr1()
    assert not t1.is_available()

# Generated at 2022-06-13 02:14:43.090523
# Unit test for constructor of class LibMgr
def test_LibMgr():
    pkgmgr = LibMgr()
    assert pkgmgr is not None


# Generated at 2022-06-13 02:14:46.360981
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr().is_available() == False

# Unit testing for method GetPackageDetails()
# def test_GetPackageDetails():
#     assert CLIMgr().GetPackageDetails() == False

# Unit testing for method GetPackages()
# def test_GetPackages():
#     assert CLIMgr().GetPackages() == False

# Generated at 2022-06-13 02:14:55.352284
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class FakePkgMgr(PkgMgr):

        def list_installed(self):
            return ['fake-package1', 'fake-package2', 'fake-package3']

        def get_package_details(self, package):
            return {'name': package}

    pkg_mgr = FakePkgMgr()
    installed_packages = {'fake-package1': [{'name': 'fake-package1', 'source': 'fakepkgmgr'}],
                          'fake-package2': [{'name': 'fake-package2', 'source': 'fakepkgmgr'}],
                          'fake-package3': [{'name': 'fake-package3', 'source': 'fakepkgmgr'}]}
    assert pkg_mgr.get_packages() == installed_packages


# Generated at 2022-06-13 02:14:58.570853
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import mock
    lm = LibMgr()
    lm._lib = None
    lm.LIB = 'bogus'
    assert not lm.is_available()
    lm.LIB = mock.Mock()
    assert lm.is_available()
    assert lm._lib == lm.LIB


# Generated at 2022-06-13 02:15:06.458026
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    # Test 1
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return False

        def get_package_details(self, package):
            return {'name': 'foo', 'version': '1.2.3'}

        def list_installed(self):
            return ['foo']

    assert TestPkgMgr().is_available() == False
    # Test 2
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True

        def get_package_details(self, package):
            return {'name': 'foo', 'version': '1.2.3'}

        def list_installed(self):
            return ['foo']

    assert TestPkgMgr().is_available() == True


# Generated at 2022-06-13 02:15:07.348918
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    assert 1 == 1


# Generated at 2022-06-13 02:15:11.970669
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

    class FakeCLIMgr(CLIMgr):

        def __init__(self):

            super(CLIMgr, self).__init__()

    fm = FakeCLIMgr()
    fm.CLI = 'dpkg'

    assert fm.is_available()
    assert fm._cli == "/usr/bin/dpkg"



# Generated at 2022-06-13 02:15:12.393169
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pass

# Generated at 2022-06-13 02:17:59.247285
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert PkgMgr.list_installed() is not None, "method list_installed() of class PkgMgr is not yet implemented"


# Generated at 2022-06-13 02:18:00.616837
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    test_object = CLIMgr()
    assert test_object.is_available() == True



# Generated at 2022-06-13 02:18:02.364787
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    test_class = LibMgr()
    test_class.LIB = 'test'
    assert test_class.is_available() == True


# Generated at 2022-06-13 02:18:07.160594
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ['a']
        def get_package_details(self, package):
            return {'name': 'a', 'version': '1.0'}
    t = TestPkgMgr()
    x = t.get_packages()
    assert x == {'a': [{'name': 'a', 'version': '1.0', 'source': 'testpkgmgr'}]}

# Generated at 2022-06-13 02:18:14.795091
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    from ansible.module_utils.common.params import AnsibleModule
    from ansible.module_utils.common.collections import ImmutableDict
    import os

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True,
    )

    class AptMgr(CLIMgr):
        CLI = 'apt-get'

    class YumMgr(CLIMgr):
        CLI = 'yum'

    class Up2dateMgr(CLIMgr):
        CLI = 'up2date'

    class ZypperMgr(CLIMgr):
        CLI = 'zypper'

    class DNFMgr(CLIMgr):
        CLI = 'dnf'

    class EOPKGMgr(CLIMgr):
        CLI = 'eopkg'


# Generated at 2022-06-13 02:18:15.259968
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    pass

# Generated at 2022-06-13 02:18:16.686127
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    obj = LibMgr()
    assert obj.is_available() == False


# Generated at 2022-06-13 02:18:18.375850
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pkg = CLIMgr()
    pkg.CLI = 'ls'
    assert pkg.is_available() is not None


# Generated at 2022-06-13 02:18:25.893514
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # List of package with multiple versions installed
    packages = [{'name':'tmux','version':'1.8','arch':'x86_64','size':'362'},{'name':'tmux','version':'2.0','arch':'x86_64','size':'362'}]
    # Object of class PkgMgr
    pkgmgr = PkgMgr()
    # Returns a dictionary of list of dictionaries (package = list of installed versions)
    result = pkgmgr.get_packages()
    # Check if the result is a dictionary of list of dictionaries
    assert isinstance(result,dict)
    # Check if the value part of the dictionary is list of dictionaries
    assert isinstance(list(result.values())[0],list)

# Generated at 2022-06-13 02:18:36.035360
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class _PkgMgr(PkgMgr):

        def list_installed(self):
            return ['package1', 'package2', 'package3']

        def get_package_details(self, package):
            return {'name': package, 'version': '2.0.0'}

    pm = _PkgMgr()
    assert pm.get_packages() == {'package1': [{'name': 'package1', 'version': '2.0.0', 'source': '_pkgmgr'}],
                                 'package2': [{'name': 'package2', 'version': '2.0.0', 'source': '_pkgmgr'}],
                                 'package3': [{'name': 'package3', 'version': '2.0.0', 'source': '_pkgmgr'}]}
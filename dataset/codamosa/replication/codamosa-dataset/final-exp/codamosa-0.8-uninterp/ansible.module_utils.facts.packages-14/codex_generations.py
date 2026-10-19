

# Generated at 2022-06-13 02:09:25.557138
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    # As class PkgMgr is abstract, we can't just instanciate it.
    # So we instanciate class Yum instead
    p = Yum()
    installed_packages_list = p.list_installed()

    assert isinstance(installed_packages_list, list)
    assert len(installed_packages_list) > 0
    assert isinstance(installed_packages_list[0], dict)
    assert 'name' in installed_packages_list[0].keys()


# Generated at 2022-06-13 02:09:26.594163
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    test_class = CLIMgr()
    assert not test_class.is_available()

# Generated at 2022-06-13 02:09:36.010106
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    import unittest

    class FakeMgr(PkgMgr):

        def list_installed(self):
            return ["foo", "bar"]

        def get_package_details(self, package):
            return {"name": package, "version": "3.4.5"}

    class FakeLibMgr(LibMgr):

        LIB = "lib"

        def list_installed(self):
            return ["foo", "bar"]

        def get_package_details(self, package):
            return {"name": package, "version": "3.4.5"}

    class FakeCLIMgr(CLIMgr):

        CLI = "cli"

        def list_installed(self):
            return ["foo", "bar"]


# Generated at 2022-06-13 02:09:46.527419
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    def __is_available(value):
        # this class is used to analyse if the method is_available is working as expected
        class Test(LibMgr):
            LIB = value
        test = Test()
        return test.is_available()

    assert __is_available('ansible.module_utils.facts.system.distribution') is True
    assert __is_available('ansible.module_utils.facts.system.distribution_ex') is True
    # The following two are not available for older distributions
    assert __is_available('ansible.module_utils.facts.system.distro') is False
    assert __is_available('ansible.module_utils.facts.system.distro_ex') is False
    assert __is_available('ansible.module_utils.facts.system.lsb') is True
    assert __is_

# Generated at 2022-06-13 02:09:49.889455
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    class TestCLIMgr(CLIMgr):

        CLI = "no_such_cli"

    assert TestCLIMgr().is_available() is False


# Generated at 2022-06-13 02:09:51.315174
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    mgr = CLIMgr()
    assert mgr._cli is None

# Generated at 2022-06-13 02:09:58.902579
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import os, sys
    # Remove the module from sys.modules to test the importing it again
    if 'pip' in sys.modules:
        del sys.modules['pip']

    from ansible.module_utils.common.process import PIP
    # Make sure that the pip module is not installed
    assert 'pip' not in sys.modules
    assert os.getenv('PATH', '').lower().find('pip') < 0
    pip = PIP()
    # Check if pip module is available
    assert pip.is_available()
    # Make sure that the pip module was successfully imported
    assert 'pip' in sys.modules
    assert os.getenv('PATH', '').lower().find('pip') >= 0


# Generated at 2022-06-13 02:10:08.147579
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import mock
    import sys
    import ansible_pkg_mgr.lib.package_mgr.yum as yum
    import ansible_pkg_mgr.lib.package_mgr.dnf as dnf
    import ansible_pkg_mgr.lib.package_mgr.microdnf as microdnf
    import ansible_pkg_mgr.lib.package_mgr.dnf as dnf
    import ansible_pkg_mgr.lib.package_mgr.apt as apt
    import ansible_pkg_mgr.lib.package_mgr.dnf as dnf
    import ansible_pkg_mgr.lib.package_mgr.pip as pip
    import ansible_pkg_mgr.lib.package_mgr.gem as gem
    import ansible_pkg_

# Generated at 2022-06-13 02:10:08.842677
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert True



# Generated at 2022-06-13 02:10:11.690336
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    c = CLIMgr()
    assert c.is_available() == False
    try:
        assert c._cli == None
    except AttributeError:
        pass
    assert hasattr(c, 'CLI') == True
    assert c.__class__.__name__ == 'CLIMgr'



# Generated at 2022-06-13 02:10:20.686596
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    for cls in get_all_subclasses(PkgMgr):
        if cls not in (CLIMgr, LibMgr):
            print('Testing PkgMgr subclass %s' % cls.__name__)
            try:
                instance = cls()
                if instance.is_available():
                    package_list = instance.list_installed()
                    if package_list:
                        print ('Package list: %s' % package_list)
                        success = True
                    else:
                        print ('No package list returned')
                        success = False
                else:
                    print ('Package manager not available')
                    success = True
            except Exception as e:
                print ('Exception: %s' % e)
                success = False
            assert success
    return 0


# Generated at 2022-06-13 02:10:25.175224
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():

    class TestMgr(PkgMgr):

        def list_installed(self):
            return ["test_package"]

        def get_package_details(self, package):
            return {'name': 'test_package'}

    mgr = TestMgr()
    assert mgr.list_installed() == ["test_package"]


# Generated at 2022-06-13 02:10:28.663549
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    # instantiate a class object of PkgMgr
    pm = PkgMgr()
    try:
        pm.get_package_details()
    except AttributeError:
        pass
    else:
        raise AssertionError('Method get_package_details of class PkgMgr does not raise AttributeError')


# Generated at 2022-06-13 02:10:32.890806
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    pkgmgr = PkgMgr()
    assert pkgmgr.is_available() == NotImplemented, "is_available not returning NotImplemented"


# Generated at 2022-06-13 02:10:33.803249
# Unit test for constructor of class LibMgr
def test_LibMgr():
    objLibMgr = LibMgr()
    assert objLibMgr._lib is None

# Generated at 2022-06-13 02:10:34.488888
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pass

# Generated at 2022-06-13 02:10:37.768472
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    all_pkg_managers = get_all_pkg_managers()
    for pkg_manager in all_pkg_managers.values():
        if pkg_manager().is_available():
            pkg_manager().list_installed()



# Generated at 2022-06-13 02:10:38.701058
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    # test the list installed functionality
    pass

# Generated at 2022-06-13 02:10:40.153419
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    test_cli = CLIMgr()
    assert test_cli._cli is None

# Generated at 2022-06-13 02:10:42.901836
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    test_inst = PkgMgr()
    result = test_inst.is_available()
    assert result is None


# Generated at 2022-06-13 02:10:51.241593
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    manager = CLIMgr()
    assert manager._cli is None


# Generated at 2022-06-13 02:10:58.382630
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class MyMgr(CLIMgr):
        CLI = 'MyCLI'

    mgr = MyMgr()
    assert not mgr.is_available()

    import mock
    with mock.patch('ansible.module_utils.common.process.get_bin_path') as mock_get_bin_path:
        mock_get_bin_path.return_value = 'bogus/path/to/bin'
        assert mgr.is_available()

# Generated at 2022-06-13 02:11:01.822350
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class PkgMgrClass(PkgMgr):
        pass

    # Create a PkgMgr object
    pmc = PkgMgrClass()
    # Check that the object has the attribute list_installed
    assert hasattr(pmc, 'list_installed')


# Generated at 2022-06-13 02:11:04.698838
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    class CLIMgrTest(CLIMgr):
        CLI = 'python'

    inst = CLIMgrTest()
    assert inst.is_available()



# Generated at 2022-06-13 02:11:14.101313
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    class LibMgrTest(LibMgr):
        LIB = 'ansible.utils.platform'

    obj = LibMgrTest()
    assert obj.is_available() is True, 'when library is installed, is_available should return True'
    LibMgrTest.LIB = 'ansible'
    assert obj.is_available() is False, 'when library is not installed, is_available should return False'

    class CLIMgrTest(CLIMgr):
        CLI = 'ls'

    obj = CLIMgrTest()
    assert obj.is_available() is True, 'when cli is installed, is_available should return True'
    CLIMgrTest.CLI = 'lss'
    assert obj.is_available() is False, 'when cli is not installed, is_available should return False'

# Generated at 2022-06-13 02:11:17.486120
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class TestLibMgr(LibMgr):
        LIB = 'test_lib'
    lib = TestLibMgr()
    # mock import and see if we return True
    lib._lib = 'test_lib'
    assert lib.is_available() is True
    # mock import and see if we return False
    lib._lib = 'test_lib2'
    assert lib.is_available() is False


# Generated at 2022-06-13 02:11:18.816061
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert PkgMgr.list_installed == NotImplemented

# Generated at 2022-06-13 02:11:22.105027
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lib_mgr = LibMgr()
    print(lib_mgr.is_available())

if __name__ == '__main__':

    test_LibMgr_is_available()

# Generated at 2022-06-13 02:11:30.147944
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import sys
    import os
    import shutil

    test_cli_path = os.path.join(os.path.dirname(__file__), 'test_data', 'test_cli')
    test_cli_path_bak = os.path.join(test_cli_path + '_bak')
    sys_path = os.environ.get('PATH')
    sys_path += ':%s' % test_cli_path

    # Test1: library exists
    shutil.copyfile(test_cli_path, test_cli_path_bak)
    os.chmod(test_cli_path, 0o755)
    os.environ['PATH'] = sys_path
    p = CLIMgr()
    assert p.is_available() == True

    # Test2: library exists but has no execute

# Generated at 2022-06-13 02:11:34.832356
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class TestCLIMgr(CLIMgr):
        CLI = 'test'

    expected_test_mgr = TestCLIMgr()
    assert expected_test_mgr._cli is None
    assert expected_test_mgr
    assert expected_test_mgr.is_available() is False


# Generated at 2022-06-13 02:11:49.642171
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cm = CLIMgr()
    assert cm._cli is None


# Generated at 2022-06-13 02:11:55.013854
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    test_CLIMgr_is_available.result = False
    test_CLIMgr_is_available.CLIMgr_class = CLIMgr()
    cli = get_bin_path('uptime')
    if cli is not None:
        if cli.endswith('uptime'):
            test_CLIMgr_is_available.result = True
    return test_CLIMgr_is_available.result

assert test_CLIMgr_is_available() is True, 'is_available method of CLIMgr class should return True'

# Generated at 2022-06-13 02:12:06.060855
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pkg_mgr_test_class = type("PkgMgrTestClass", (PkgMgr,), {'is_available': lambda x: True,
                                                              'list_installed': lambda x: ['package1', 'package2', 'package3'],
                                                              'get_package_details': lambda x, y: {'name': y, 'version': y[-1]}})

# Generated at 2022-06-13 02:12:07.329774
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
   assert CLIMgr().CLI is None


# Generated at 2022-06-13 02:12:08.679299
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert CLIMgr().is_available() == False


# Generated at 2022-06-13 02:12:18.002421
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class PkgMgr_get_packages_Test(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return ['package1', 'package2']

        def get_package_details(self, package):
            return {'name': package, 'version': '1', 'source': 'test'}

    pkgmgr = PkgMgr_get_packages_Test()
    packages = pkgmgr.get_packages()
    assert packages['package1'][0]['name'] == 'package1'
    assert packages['package1'][0]['version'] == '1'
    assert packages['package1'][0]['source'] == 'test'
    assert packages['package2'][0]['name'] == 'package2'

# Generated at 2022-06-13 02:12:20.100737
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    class Mgr(PkgMgr):
        CLI = 'some exe which is not available'

    m = Mgr()
    assert not m.is_available()



# Generated at 2022-06-13 02:12:26.754095
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import unittest2

    class FakeLibMgr(LibMgr):

        def list_installed(self):
            return ['pkgn1', 'pkgn2']

        def get_package_details(self, package):
            return {'name': 'name-%s' % package, 'version': '1'}

    class FakeCLIMgr(CLIMgr):

        def list_installed(self):
            return ['pkgn1', 'pkgn2']

        def get_package_details(self, package):
            return {'name': 'name-%s' % package, 'version': '1'}

    class TestGetPackages(unittest2.TestCase):

        def test_LibMgr(self):
            fake_lib = FakeLibMgr()

# Generated at 2022-06-13 02:12:32.683906
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class LibMgrConcrete(LibMgr):
        LIB = 'sys'
    assert LibMgrConcrete().is_available()
    # Test for ImportError
    class LibMgrConcrete(LibMgr):
        LIB = 'qwerty'
    assert LibMgrConcrete().is_available() == False


# Generated at 2022-06-13 02:12:36.741633
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lib1 = LibMgr()
    assert lib1._lib is None
    # Assuming 'os' module is found as part of Python environment
    class Test(LibMgr):
        LIB = 'os'
    test = Test()
    assert test._lib.name == 'os'


# Generated at 2022-06-13 02:13:06.926715
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    cm = CLIMgr()
    assert cm.is_available() == False
    cm.CLI="echo"
    assert cm.is_available() == True


# Generated at 2022-06-13 02:13:11.131466
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    # create an instance of the abstract class
    p = PkgMgr()
    # test if the call of the abstract method fails
    try:
        p.list_installed()
    except AttributeError:
        pass
    else:
        # unable to raise an exception
        assert False


# Generated at 2022-06-13 02:13:12.168495
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert CLIMgr().is_available() == False

# Generated at 2022-06-13 02:13:21.345468
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.common import pkggraph_utils
    from ansible.module_utils.common.process import get_bin_path
    #mocked_lib = "ansible.module_utils.common.pkggraph_utils.python_system"
    class mocked_pkg_mgr(LibMgr):
        LIB = "ansible.module_utils.common.pkggraph_utils.python_system_posix"

    pkg_mgr = mocked_pkg_mgr()
    assert pkg_mgr.is_available() == True
    pkg_mgr = mocked_pkg_mgr()
    #assert pkg_mgr.is_available() == False


# Generated at 2022-06-13 02:13:22.069430
# Unit test for constructor of class LibMgr
def test_LibMgr():
    pass

# Generated at 2022-06-13 02:13:31.730937
# Unit test for method get_package_details of class PkgMgr

# Generated at 2022-06-13 02:13:39.649797
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    # Test with arguments defined in the class
    mgr = PkgMgr()
    package_details = mgr.get_package_details("vim")
    assert 'name' in package_details, "Failed to return package details. Name must be present in package details."
    assert 'version' in package_details, "Failed to return package details. Version must be present in package details."
    assert 'release' in package_details, "Failed to return package details. Release must be present in package details."
    assert 'arch' in package_details, "Failed to return package details. Arch must be present in package details."
    assert 'source' in package_details, "Failed to return package details. Source must be present in package details."


# Generated at 2022-06-13 02:13:41.386231
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestLibMgr(LibMgr):
        LIB = ''
    assert TestLibMgr()


# Generated at 2022-06-13 02:13:42.982581
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    plm = CLIMgr()
    assert plm.CLI is None
    assert plm._cli is None

# Generated at 2022-06-13 02:13:48.533393
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    error_counter = 0
    yum=CLIMgr()
    assert yum.CLI == None
    assert yum._cli == None
    res = yum.is_available()
    if res!=False and res!=True:
        error_counter += 1
    assert res==False or res==True
    yum.CLI = "/bin/cat"
    res = yum.is_available()
    if res!=False and res!=True:
        error_counter += 1
    assert res==False or res==True
    assert error_counter == 0

# Generated at 2022-06-13 02:15:04.793710
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # Simple class to mock PkgMgr
    class TestPkgMgr(PkgMgr):
        def __init__(self):
            pass

        def list_installed(self):
            return ['pkg1', 'pkg2', 'pkg3']

        def get_package_details(self, package):
            attr = {'name': package, 'version': '1.0'}
            if package == 'pkg3':
                attr['source'] = 'source'
            return attr

    tpm = TestPkgMgr()

# Generated at 2022-06-13 02:15:13.735258
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class PkgMgrTest(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return [u'package1', u'package2']

        def get_package_details(self, package):
            return {u'name': package, u'version': u'1.0'}

    pkg_mgr = PkgMgrTest()
    packages = pkg_mgr.get_packages()


# Generated at 2022-06-13 02:15:18.425052
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    try:
        from ansible.module_utils.common.process import get_bin_path
        from ansible.modules.system.package_facts.main import PkgMgr
        from ansible.modules.system.package_facts.main import CLIMgr

        # get_bin_path returns path to the binary if the binary is in the $PATH.
        # Otherwise, it will raise an ValueError exception
        get_bin_path('ls')
        cliMgr = CLIMgr()
        assert cliMgr is not None
        assert cliMgr._cli == get_bin_path('ls')
    except (ImportError, ValueError) as exception:
        print("Failed to import get_bin_path or to instantiate CLIMgr: " + str(exception))



# Generated at 2022-06-13 02:15:21.198221
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    class DummyClass(PkgMgr):
        pass

    test_obj = DummyClass()
    try:
        test_obj.is_available()
    except NotImplementedError:
        return True
    return False


# Generated at 2022-06-13 02:15:22.890025
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    assert LibMgr().is_available() == False


# Generated at 2022-06-13 02:15:24.099189
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    managers = get_all_pkg_managers()
    for manager in managers:
        assert isinstance(managers[manager]().is_available(), bool)

# Generated at 2022-06-13 02:15:26.286551
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pkg_mgr = CLIMgr()
    pkg_mgr.CLI = 'any_cli'
    pkg_mgr.is_available()


# Generated at 2022-06-13 02:15:29.074757
# Unit test for constructor of class LibMgr
def test_LibMgr():
    x = LibMgr()
    assert x.is_available() is False


# Generated at 2022-06-13 02:15:32.159071
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    test_cli = CLIMgr()
    assert test_cli._cli is None
    # Calling is_available will set _cli to a path.
    assert test_cli.is_available()
    assert test_cli._cli is not None

# Generated at 2022-06-13 02:15:36.663365
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.common.packages import get_all_pkg_managers

    all_pkg_managers = get_all_pkg_managers()

    for pkgmanager in all_pkg_managers.values():
        # setup a fake package manager
        fake_pkgmanager = pkgmanager()
        assert fake_pkgmanager.get_packages() == {}

# Generated at 2022-06-13 02:18:23.273337
# Unit test for constructor of class LibMgr
def test_LibMgr():
    # Test for:
    # - instantiating the class
    # - using default values

    # Instantiate an object
    libmgr = LibMgr()

    # Check attributes value
    assert '_lib' in libmgr.__dict__
    assert not libmgr._lib


# Generated at 2022-06-13 02:18:24.649199
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    mgr = PkgMgr()
    assert mgr.list_installed() == NotImplemented



# Generated at 2022-06-13 02:18:25.653699
# Unit test for constructor of class LibMgr
def test_LibMgr():
    libmgr = LibMgr()
    assert libmgr


# Generated at 2022-06-13 02:18:29.276695
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    # CLIMgr constructor should not take any parameter
    # This will ensure that CLIMgr instances are created correctly
    try:
        p = CLIMgr()
        assert p is not None
    except TypeError as e:
        assert False

# Generated at 2022-06-13 02:18:36.940979
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class PkgMgrTest(PkgMgr):
        def __init__(self):
            super(PkgMgrTest, self).__init__()
        def list_installed(self):
            return ['package_one','package_two','package_three']
        def get_package_details(self, package):
            return {'name': str(package)}
    pkg_mgr_obj = PkgMgrTest()
    pkg_mgr_obj.list_installed()
    assert pkg_mgr_obj.list_installed() == ['package_one', 'package_two', 'package_three']


# Generated at 2022-06-13 02:18:37.743533
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    test = CLIMgr()
    assert test is not None

# Generated at 2022-06-13 02:18:38.504013
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pass


# Generated at 2022-06-13 02:18:39.742998
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert PkgMgr().is_available() is None


# Generated at 2022-06-13 02:18:45.824146
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # Case 1: Provided with a CLI which exists
    test_1_cli = 'ls'
    test_1_result = True
    # Case 2: Provided with a CLI which does not exist
    test_2_cli = 'myCLI'
    test_2_result = False
    # Case 3: Provided with a None value
    test_3_cli = None
    test_3_result = False

    class TestCLIMgr(CLIMgr):
        CLI = test_1_cli

    # Case 1
    test_object_1 = TestCLIMgr()
    is_available_result_1 = test_object_1.is_available()
    assert is_available_result_1 == test_1_result

    # Case 2
    test_object_2 = TestCLIMgr()

# Generated at 2022-06-13 02:18:46.607484
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pass

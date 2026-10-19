

# Generated at 2022-06-13 02:09:20.476911
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.common.json_utils import json

    inst = LibMgr()
    inst.LIB = 'json'
    if inst.is_available():
        assert True
    else:
        assert False

    inst = LibMgr()
    inst.LIB = 'foobar'
    if inst.is_available():
        assert False
    else:
        assert True


# Generated at 2022-06-13 02:09:21.907601
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    PkgMgr.is_available()



# Generated at 2022-06-13 02:09:24.641465
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pkg_mgr = CLIMgr()
    # this is not a valid package manager
    assert pkg_mgr.is_available() is False


# Generated at 2022-06-13 02:09:26.635550
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # create an object
    test_obj = LibMgr()
    # test
    assert test_obj.is_available() == False

# Generated at 2022-06-13 02:09:29.386175
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert hasattr(PkgMgr, 'list_installed')
    assert callable(getattr(PkgMgr, 'list_installed', None))
    assert isinstance(PkgMgr.list_installed, abstractmethod)

# Generated at 2022-06-13 02:09:37.297598
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class TestPkgMgr(PkgMgr):

        def list_installed(self):
            return ['testpackage1', 'testpackage2']

        def get_package_details(self, package):
            return {
                'name': package,
                'version': '1234'
            }

    testpkgmgr = TestPkgMgr()
    assert testpkgmgr.get_packages() == {'testpackage1': [{'name': 'testpackage1', 'version': '1234', 'source': 'testpkgmgr'}], 'testpackage2': [{'name': 'testpackage2', 'version': '1234', 'source': 'testpkgmgr'}]}

# Generated at 2022-06-13 02:09:41.981328
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.facts.pkg_mgr import get_all_pkg_managers
    pkg_managers = get_all_pkg_managers()
    instance = pkg_managers['apt']()
    assert instance.get_packages()

# Generated at 2022-06-13 02:09:43.215151
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    obj = PkgMgr()
    assert obj.is_available() is not None


# Generated at 2022-06-13 02:09:50.970912
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    return_value = dict(name='foo', version='1.0')
    class FooPkgMgr(PkgMgr):
        def __init__(self):
            pass
        def list_installed(self):
            return ['foo']
        def get_package_details(self, package):
            assert package == 'foo'
            return return_value
    assert FooPkgMgr().get_packages() == {'foo': [return_value]}


# Generated at 2022-06-13 02:09:51.989800
# Unit test for constructor of class LibMgr
def test_LibMgr():
    pkgmgr = LibMgr()
    assert pkgmgr is not None


# Generated at 2022-06-13 02:10:06.272592
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import unittest
    import json

    class MockList:
        def __init__(self):
            with open('../fixtures/apt_list_installed.json') as json_file:
                self.data = json.load(json_file)
        def readlines(self):
            return self.data
    
    class MockPkgMgr(PkgMgr):
        def __init__(self):
            pass
        def is_available(self):
            return True
        def list_installed(self):
            return list(self.get_packages().keys())
        def get_package_details(self, package):
            return {'name': package, 'version': 'version'}

    class TestGetPackages(unittest.TestCase):
        def setUp(self):
            self.mock_pkgmgr

# Generated at 2022-06-13 02:10:07.434815
# Unit test for constructor of class LibMgr
def test_LibMgr():
    obj = LibMgr()
    assert obj._lib is None


# Generated at 2022-06-13 02:10:11.267548
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    from ansible.module_utils.common import pkg_mgrs
    pkg_mgrs_list = pkg_mgrs.get_all_pkg_managers()
    assert type(pkg_mgrs_list) == dict, 'Result is not a dictionary'
    assert len(pkg_mgrs_list) > 0, 'Result is empty'
    assert len([pkg_mgr for pkg_mgr in pkg_mgrs_list if pkg_mgrs_list[pkg_mgr].is_available()]) >= 1, 'At least 1 package manager should be available'

# Generated at 2022-06-13 02:10:13.644926
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    """
    Testing class LibMgr
    """
    pm = LibMgr()
    pm.LIB = 'python27'
    assert pm.is_available() is True


# Generated at 2022-06-13 02:10:23.226498
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.facts import pkg_mgr
    import sys

    import_error = "Failed importing the 'pycurl' python module"

    mgr = pkg_mgr.get_all_pkg_managers()['pip']()

    lib_name = mgr.LIB
    del sys.modules[lib_name]

    if lib_name in sys.modules:
        raise Exception("sys.modules[%s] should be deleted" % lib_name)

    if mgr.is_available():
        raise Exception("The 'pycurl' module shouldn't be available")

    import pycurl

    if mgr.is_available():
        raise Exception("The 'pycurl' module should be available")

# Generated at 2022-06-13 02:10:33.185412
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.common._utils import is_systemd
    from ansible.module_utils.facts.system.pkg_mgr import YumMgr, AptMgr, DnfMgr, PacmanMgr, DpkgMgr, DpkgStatusMgr
    from ansible.module_utils.facts.system.pkg_mgr import ZypperMgr, RpmMgr, PkgMgr

    lib = None
    class MockLibMgr(LibMgr):
        LIB = lib

    class MockCLIMgr(CLIMgr):
        CLI = None

    cli = None
    class MockCLIMgr2(CLIMgr):
        CLI = cli


# Generated at 2022-06-13 02:10:34.579399
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pass


# Generated at 2022-06-13 02:10:45.059812
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    '''
    Test the get_package_details method of PkgMgr
    '''
    class test_PkgMgr(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            list_installed_packages = {'package1', 'package2', 'package3'}
            return list_installed_packages
        def get_package_details(self, package):
            dict_of_pkg_versions = {'name': package, 'version': 'version1'}
            return dict_of_pkg_versions
    test_p = test_PkgMgr()
    assert test_p.get_package_details('package2') == {'name': 'package2', 'version': 'version1'}


# Generated at 2022-06-13 02:10:47.255098
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class Tested(LibMgr):
        LIB = '__import_this'
    tested = Tested()
    assert not tested.is_available()

# Generated at 2022-06-13 02:10:52.568378
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    # create a mock object with list_installed
    class MockPkgMgr(PkgMgr):
        def is_available(self):
            pass
        def get_package_details(self, package):
            pass

    # create an instance
    m = MockPkgMgr()
    # assert that the class has attribute list_installed
    assert hasattr(m, 'list_installed')
    # assert that the method list_installed is abstract
    assert isinstance(m.list_installed, abstractmethod)



# Generated at 2022-06-13 02:11:04.163173
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.fail_json = lambda *args, **kwargs: dict(*args, **kwargs)
    mgrs = get_all_pkg_managers()
    results = {}
    for mgr in mgrs:
        if not mgrs[mgr]().is_available():
            continue
        results[mgr] = mgrs[mgr]().get_packages()
    if results:
        module.exit_json(packages=results)
    module.fail_json(msg="No package managers found on the system")

# Generated at 2022-06-13 02:11:06.467906
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pm = PkgMgr()
    with pytest.raises(TypeError):
        pm.is_available('foo')


# Generated at 2022-06-13 02:11:08.635682
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    p1 = PkgMgr()
    assert p1.is_available() == False

    p2 = LibMgr()
    assert p2.is_available() == False

    p3 = CLIMgr()
    assert p3.is_available() == False


# Generated at 2022-06-13 02:11:13.220683
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():

    # Check we return a non-zero number of package managers
    pkg_mgrs = get_all_pkg_managers()
    assert len(pkg_mgrs) > 0

    # Check that the PkgMgr class is not in the list of package managers
    # It should not be found as it is an abstract class with no implementation
    assert "pkgmgr" not in pkg_mgrs.keys()

# Generated at 2022-06-13 02:11:19.184997
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # test simple case
    pm = PkgMgr()
    pm.list_installed = lambda: ['pkg_one']
    pm.get_package_details = lambda pkg: {'name': 'pkg_one', 'version': '1.0-1'}
    assert pm.get_packages() == {'pkg_one': [{'name': 'pkg_one', 'version': '1.0-1', 'source': 'pkgmgr'}]}

    # test multiple versions for one package
    pm.list_installed = lambda: ['pkg_one', 'pkg_two', 'pkg_three']
    pm.get_package_details = lambda pkg: {'name': pkg, 'version': '1.0-1'}

# Generated at 2022-06-13 02:11:28.704529
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # Given

    class _TestPkgMgr(PkgMgr):
        def list_installed(self):
            return ['package1', 'package2']

        def get_package_details(self, package):
            if package == 'package1':
                return { 'name': 'package1', 'version': '1.0' }
            elif package == 'package2':
                return { 'name': 'package2', 'version': '2.0' }
            raise Exception('Invalid package passed to get_package_details')

    mgr = _TestPkgMgr()

    # When
    packages = mgr.get_packages()

    # Then

# Generated at 2022-06-13 02:11:29.601414
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert PkgMgr.list_installed() is None


# Generated at 2022-06-13 02:11:30.162792
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    c = CLIMgr()


# Generated at 2022-06-13 02:11:31.731773
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    c = CLIMgr()
    assert c is not None

# Generated at 2022-06-13 02:11:33.246112
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert PkgMgr.is_available()



# Generated at 2022-06-13 02:11:48.886364
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():

    available_pkg_managers = {}
    pkg_managers = get_all_pkg_managers()
    for pkg_manager in pkg_managers:
        if pkg_managers[pkg_manager]().is_available():
            available_pkg_managers[pkg_manager] = pkg_managers[pkg_manager]
    assert len(available_pkg_managers) > 0


if __name__ == '__main__':
    test_get_all_pkg_managers()

# Generated at 2022-06-13 02:11:51.458225
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class testMgr(LibMgr):
        LIB = 'ansible_mitogen.distro_detect'

    tm = testMgr()
    assert tm.is_available() == True


# Generated at 2022-06-13 02:11:53.462813
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class TestCLIMgr(CLIMgr):
        CLI = 'ls'
    test_one = TestCLIMgr()
    assert test_one.CLI == 'ls'

# Generated at 2022-06-13 02:11:55.048599
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lm = LibMgr()
    try:
        assert not lm.is_available()
    except Exception:
        assert True

# Generated at 2022-06-13 02:11:58.040007
# Unit test for constructor of class LibMgr
def test_LibMgr():
    from ansible.module_utils.common._collections_compat import MutableMapping
    obj = LibMgr()
    assert isinstance(obj, object)
    assert isinstance(obj, MutableMapping)


# Generated at 2022-06-13 02:12:05.855484
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class CLIMgrTest(CLIMgr):
        CLI = 'which'

    cli_mgr = CLIMgrTest()
    ret = cli_mgr.is_available()
    if type(ret) is bool:
        print("test_CLIMgr_is_available: OK")
    else:
        print("test_CLIMgr_is_available: FAILED")

# Test case for method is_available of class CLIMgr
test_CLIMgr_is_available()

# Generated at 2022-06-13 02:12:13.419160
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():

    from ansible.module_utils.common.os import package_manager

    PkgMgr += get_all_pkg_managers()

    package_managers = package_manager.get_all_pkg_managers()
    assert_equals(9, len(package_managers))

    expected_package_managers = ['apt', 'apk', 'pkgng', 'pacman', 'dnf', 'yum', 'zypper', 'pkg5', 'portage']
    for package_manager in expected_package_managers:
        assert package_manager in package_managers

# Unit test function get_packages()

# Generated at 2022-06-13 02:12:16.196804
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class DummyLibMgr(LibMgr):
        LIB = 'dummylib'
    # Test for if the library is present
    assert DummyLibMgr().is_available() == True


# Generated at 2022-06-13 02:12:17.840292
# Unit test for constructor of class LibMgr
def test_LibMgr():
    test_LibMgr = LibMgr()
    assert test_LibMgr._lib == None


# Generated at 2022-06-13 02:12:19.634017
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    mgr = LibMgr()
    mgr.LIB = 'test'
    assert mgr.is_available() == False


# Generated at 2022-06-13 02:12:37.485716
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pm = PkgMgr()
    assert pm.list_installed() is None


# Generated at 2022-06-13 02:12:45.863109
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pkg_mgr = PkgMgr()
    pkg_mgr.list_installed = lambda: ['python3-pip=9.0.1-2ubuntu0.4']
    pkg_mgr.get_package_details = lambda package: {'name': 'python3-pip', 'version': '9.0.1'}
    assert(pkg_mgr.get_packages() == {'python3-pip': [{'name': 'python3-pip', 'version': '9.0.1', 'source': 'PkgMgr'}]})

# Generated at 2022-06-13 02:12:53.836988
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    from ansible.module_utils.packaging.package_common import PkgMgr

    def test_is_available(pkgmgr):
        package_manager = pkgmgr()
        if package_manager.is_available():
            assert True
        else:
            assert False

    class ChildPkgMgr(PkgMgr):
        pass

    class ChildPkgMgr2(PkgMgr):
        pass

    test_is_available(ChildPkgMgr)
    test_is_available(ChildPkgMgr2)


# Generated at 2022-06-13 02:12:56.573533
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class TestCLIMgr(CLIMgr):
        CLI = 'test'

    tcm = TestCLIMgr()

    assert(tcm._cli == None)


# Generated at 2022-06-13 02:12:58.447526
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # Return True value when argument is correct.
    assert LibMgr.is_available(LibMgr()) == True


# Generated at 2022-06-13 02:13:00.632007
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.pkg_mgr_setup_py import SetupPy
    pkg_mgr = SetupPy()
    assert SetupPy.CLI == 'python'
    assert SetupPy.is_available()

# Generated at 2022-06-13 02:13:03.369752
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestLibMgr(LibMgr):
        LIB = 'test_lib'
    lib_mgr = TestLibMgr()
    assert lib_mgr._lib is None
    assert lib_mgr.LIB == 'test_lib'


# Generated at 2022-06-13 02:13:08.682108
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # Create a class extending PkgMgr
    class TestPkgMgr(PkgMgr):
        # Implement required list_installed() method
        def list_installed(self):
            return ['test_pkg']

        # Implement required get_package_details method
        def get_package_details(self, package):
            return {'name': 'test_pkg', 'version': '1.0'}

    # Create an object of above class
    pkg_mgr = TestPkgMgr()

    # Assert package manager is available
    assert pkg_mgr.is_available() is True

    # Call get_packages() method and assert the result

# Generated at 2022-06-13 02:13:10.417501
# Unit test for constructor of class LibMgr
def test_LibMgr():
        x = LibMgr()
        assert x is not None


# Generated at 2022-06-13 02:13:13.469453
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    '''
    test if is_available method returns True on import cffi
    '''

    class TestMgr(LibMgr):

        LIB = 'cffi'

    t = TestMgr()
    assert t.is_available()



# Generated at 2022-06-13 02:13:50.093503
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    test_cli = CLIMgr()
    test_cli.CLI = 'ls'
    assert test_cli.is_available() == True
    test_cli.CLI = 'rgerg'
    assert test_cli.is_available() == False

# Generated at 2022-06-13 02:13:55.893496
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    # Create a dictionary of all package managers
    pkg_mgrs = get_all_pkg_managers()
    # Check if each package manager is available, print result
    for pkg_mgr in pkg_mgrs:
        print('{}: {}'.format(pkg_mgr, pkg_mgrs[pkg_mgr]().is_available()))
    # Check if expected output is produced
    # Example:
    # apt_yum: False
    # cacert: True
    # easy_install: True
    # gem: True
    # go: False
    # homebrew: False
    # jpackage: False
    # macports: False
    # npm: True
    # pear: False
    # perl: False
    # pip: True
    # pkgng: False
    # portage: False


# Generated at 2022-06-13 02:13:57.485744
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    pass


# Generated at 2022-06-13 02:13:58.037470
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pass

# Generated at 2022-06-13 02:13:59.118271
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

    x = CLIMgr()
    assert x.is_available()


# Generated at 2022-06-13 02:14:00.435709
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    assert isinstance(get_all_pkg_managers(), dict)
    assert len(get_all_pkg_managers()) > 3

# Generated at 2022-06-13 02:14:04.443308
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    for name, cls in get_all_pkg_managers().items():
        if issubclass(cls, CLIMgr):
            assert (cls().is_available() == (get_bin_path(cls.CLI) is not None))


# Generated at 2022-06-13 02:14:11.821923
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    from ansible.module_utils.common.process import get_bin_path
    from os.path import join
    from ansible.module_utils.ansible_release import __file__ as afile

    mock_bin = join(afile.split('ansible')[0], 'ansible')
    get_bin_paths = get_bin_path.__globals__['get_bin_paths']
    get_bin_paths.return_value = [mock_bin]

    class MockCLIMgr(CLIMgr):
        CLI = 'ansible-python-mock'

    cli = MockCLIMgr()

    assert cli.is_available()
    assert cli._cli.startswith(mock_bin)



# Generated at 2022-06-13 02:14:16.852350
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    #test the get_package_details method
    test_pkg_mgr = PkgMgr()
    test_pkg_mgr_details = test_pkg_mgr.get_package_details("test_package")
    assert 'name' in test_pkg_mgr_details
    assert 'version' in test_pkg_mgr_details
    assert 'source' in test_pkg_mgr_details


# Generated at 2022-06-13 02:14:20.979726
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    '''
        test_CLIMgr_is_available instantiate class CLIMgr
        and call method is_available()
    '''
    obj = CLIMgr()
    assert obj.is_available() == True, 'method failed to return proper value'


# Generated at 2022-06-13 02:15:45.500592
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lib1 = LibMgr()
    assert lib1.is_available() == False


# Generated at 2022-06-13 02:15:48.407385
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # class LibMgr is used as a parent for other classes, test for it using pip
    assert LibMgr().is_available() == True



# Generated at 2022-06-13 02:15:49.244299
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr()


# Generated at 2022-06-13 02:15:50.064399
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    p = CLIMgr()
    assert p

# Generated at 2022-06-13 02:15:51.238044
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pm = PkgMgr()
    assert pm.get_packages() == {}

# Generated at 2022-06-13 02:15:58.408407
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.facts.system.pkg_mgr import LibMgr

    # test for available module
    lm = LibMgr()
    lm.LIB = 'time'
    assert lm.is_available()

    # test for non-available module
    lm = LibMgr()
    lm.LIB = 'time1'
    assert not lm.is_available()



# Generated at 2022-06-13 02:16:02.887236
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    # Ensures that is_available() responds False when the package manager is not installed
    # To be tested on machine where it is not possible to run the package manager
    pm = get_all_pkg_managers()
    for pm_name in pm:
        pm[pm_name] = pm[pm_name]()
        assert not pm[pm_name].is_available()
    print("test_PkgMgr_is_available() passed")


# Generated at 2022-06-13 02:16:08.923251
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    import shutil
    import tempfile

    is_available = CLIMgr.is_available
    class CLI_Mock(CLIMgr):
        CLI = '__some_fake_binary__'

    prev_env = dict(os.environ)

# Generated at 2022-06-13 02:16:13.532499
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class PkgMgr_subclass(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ['package_1', 'package_2']
        def get_package_details(self, package):
            return {'name': package, 'version': '1.0'}

    packages = PkgMgr_subclass().get_packages()
    assert 'package_1' in packages
    assert 'package_2' in packages
    assert len(packages['package_1']) == 1
    assert len(packages['package_2']) == 1
    assert packages['package_1'][0]['name'] == 'package_1'
    assert packages['package_2'][0]['name'] == 'package_2'

# Generated at 2022-06-13 02:16:19.299248
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    """
    Test function of PkgMgr.get_package_details()
    """
    if get_all_pkg_managers()['apt'] is not None:
        apt_mgr = get_all_pkg_managers()['apt']
        apt_mgr.is_available()
        apt_mgr.list_installed()
        apt_mgr.get_package_details('python')
        apt_mgr.get_packages()
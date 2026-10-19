

# Generated at 2022-06-13 02:09:19.017691
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    CLIMgr_obj = CLIMgr()
    CLIMgr_obj.CLI = 'python'
    CLIMgr_obj.is_available()
    assert CLIMgr_obj._cli == '/usr/bin/python'

# Generated at 2022-06-13 02:09:26.031454
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    """
    is_available() Test Case 1:

    Test Case - is_available() Test Case
    This test will check if pkg manger is available or not
    """
    def test_pkg_mgr_is_available_tc1():

        # Call is_available method from class PkgMgr
        result = PkgMgr.is_available()
        # Expected result
        expected_result = None
        assert expected_result == result

    """
    is_available() Test Case 2:

    Test Case - is_available() Test Case
    This test will check if pkg manger is available or not
    """
    def test_pkg_mgr_is_available_tc2():

        # Call is_available method from class PkgMgr
        result = PkgMgr.is_available()
        # Expected result


# Generated at 2022-06-13 02:09:27.542767
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lm = LibMgr()
    assert(lm._lib is None)


# Generated at 2022-06-13 02:09:28.435377
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr().CLI is None

# Generated at 2022-06-13 02:09:29.616786
# Unit test for constructor of class LibMgr
def test_LibMgr():
    mgr = LibMgr()
    assert mgr._lib is None



# Generated at 2022-06-13 02:09:33.082155
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    try:
        class x(CLIMgr):
            CLI = 'test'
        x()
    except NameError as e:
        assert "has no attribute 'CLI'" in str(e)

# Generated at 2022-06-13 02:09:41.210138
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return [1, 2, 3]
        def get_package_details(self, package):
            return {'name': str(package)}

    p = TestPkgMgr()
    assert p.get_packages() == {'1': [{'name': '1', 'source': 'testpkgmgr'}],
                                '2': [{'name': '2', 'source': 'testpkgmgr'}],
                                '3': [{'name': '3', 'source': 'testpkgmgr'}]}

# Generated at 2022-06-13 02:09:45.150698
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    class TestClass(PkgMgr):
        def is_available(self):
            return False
        def list_installed(self):
            return []
        def get_package_details(self, package):
            return {}
    tc = TestClass()
    assert tc.is_available() == False



# Generated at 2022-06-13 02:09:50.775620
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pkg_managers = get_all_pkg_managers()
    assert pkg_managers['dnf'].is_available() == True
    assert pkg_managers['zypper'].is_available() == True
    assert pkg_managers['apk'].is_available() == True
    #assert pkg_managers['zypper'].is_available() == True

# Generated at 2022-06-13 02:09:54.653860
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class TestLibManager(LibMgr):
        LIB = 'fake_module'
    assert not TestLibManager().is_available()
    libmgr = LibMgr()
    setattr(libmgr, '_lib', 'found')
    assert libmgr.is_available()



# Generated at 2022-06-13 02:09:59.871535
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    b = CLIMgr()
    assert(b != None)

# Generated at 2022-06-13 02:10:08.608850
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.facts import PkgMgrFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import RpmMgr, DnfMgr, AptMgr, ZypperMgr, PkgngMgr, YumMgr, PacmanMgr, PortageMgr, ApkMgr, PipMgr, GemMgr, PkginMgr, GoMgr, CondaMgr, CabalMgr
    from ansible.module_utils.facts.system.pkg_mgr import AppGetMgr, EopkgMgr, PakMgr, RPMMgr, ConaryMgr, OpkgMgr, FinkMgr, SlackpkgMgr, SlackBuildsMgr, PortMgr, NixMgr, FwPkgMgr, EntropyMgr, Pkgtool

# Generated at 2022-06-13 02:10:11.505590
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    test_mgr = CLIMgr()
    test_mgr.CLI = 'ls'
    assert test_mgr.is_available() is True
    test_mgr.CLI = 'this/is/faked/path/for/ls'
    assert test_mgr.is_available() is False

# Generated at 2022-06-13 02:10:21.119146
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class SomeMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return [ 'package1', 'package2' ]

        def get_package_details(self, package):
            return {'name': package, 'version': '1.0'}

    test_mgr = SomeMgr()

    assert test_mgr.get_packages() == {
        'package1': [{'name': 'package1', 'version': '1.0', 'source': 'some_mgr'}],
        'package2': [{'name': 'package2', 'version': '1.0', 'source': 'some_mgr'}]
    }


# Generated at 2022-06-13 02:10:25.173996
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class PkgMgrAttack(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return None
        def get_package_details(self, package):
            return None

    assert (PkgMgrAttack().list_installed() is None)

# Generated at 2022-06-13 02:10:27.310809
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    assert CLIMgr().is_available() == False
    class TestCLIMgr(CLIMgr):
        CLI = 'wget'

    assert TestCLIMgr().is_available() == True

# Generated at 2022-06-13 02:10:28.954173
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pm = CLIMgr()
    if pm.is_available():
        return True
    else:
        return False


# Generated at 2022-06-13 02:10:31.937510
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    assert LibMgr().is_available() is None


# Generated at 2022-06-13 02:10:32.401686
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pass

# Generated at 2022-06-13 02:10:34.533404
# Unit test for constructor of class LibMgr
def test_LibMgr():

    obj = LibMgr()
    assert isinstance(obj, LibMgr)

# Generated at 2022-06-13 02:10:40.765909
# Unit test for constructor of class LibMgr
def test_LibMgr():
    #__init__()
    m = LibMgr()
    assert isinstance(m, LibMgr)


# Generated at 2022-06-13 02:10:44.153056
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class DummyLib(LibMgr):
        LIB = 'some_library'

    dummy_lib = DummyLib()
    assert dummy_lib


# Generated at 2022-06-13 02:10:49.244644
# Unit test for constructor of class LibMgr
def test_LibMgr():
    from ansible.module_utils.common._collections_compat import MutableMapping
    import sys
    if sys.version_info[0] < 3:
        from collections import MutableMapping
    class TestMgr(LibMgr):
        LIB = 'ansible'

    mgr = TestMgr()
    assert isinstance(mgr, (MutableMapping,))

# Generated at 2022-06-13 02:10:51.192872
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert PkgMgr.is_available() == True



# Generated at 2022-06-13 02:10:54.813892
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    mgr = CLIMgr()
    assert mgr.is_available() == False

    mgr.CLI = "true"
    assert mgr.is_available() == True


# Generated at 2022-06-13 02:10:59.814761
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class Dummy(LibMgr):
        LIB = 'dummy'
    assert Dummy().is_available() is False
    # This one should only run if you have 'distro' modules installed
    try:
        import distro
        assert Dummy().is_available() is True
    except ImportError:
        pass


# Generated at 2022-06-13 02:11:00.742821
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    return


# Generated at 2022-06-13 02:11:05.608388
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    libmgr = LibMgr()
    lib_available = libmgr.is_available()
    if type(lib_available) != bool:
        raise AssertionError("is_available method of class LibMgr returns value of wrong type")


# Generated at 2022-06-13 02:11:08.356795
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class APMgr(CLIMgr):
        CLI = 'zypper'
    apmgr = APMgr()
    assert isinstance(apmgr, APMgr)

# Generated at 2022-06-13 02:11:08.918130
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pass

# Generated at 2022-06-13 02:11:19.309143
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class CLIMgrTest(CLIMgr):
        CLI = "fake_cli"
    cli = CLIMgrTest()
    assert cli._cli is None


# Generated at 2022-06-13 02:11:20.131553
# Unit test for constructor of class LibMgr
def test_LibMgr():
    LibMgr()

# Generated at 2022-06-13 02:11:21.685862
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    mgr = CLIMgr()
    assert mgr._cli == None


# Generated at 2022-06-13 02:11:26.967726
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    # class PkgMgr is an abstract base class. Here we use CLIMgr.
    # CLIMgr.get_package_details is a non-abstract base class method, so it is not tested.

    package='{"name":"apache2","status":"installed","arch":"amd64"}'
    cli = CLIMgr()
    cli.get_package_details(package)



# Generated at 2022-06-13 02:11:36.268110
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    try:
        import sys
        import ansible.module_utils.common.process
        from ansible.module_utils.common.collections import ImmutableDict
        from ansible.module_utils.common._utils import get_all_subclasses
    except ImportError:
        pass

    class FakeMgr(CLIMgr):
        CLI = "not_real"

    # Should return False
    assert not FakeMgr().is_available()
    sys.modules['ansible.module_utils.common.process'] = __import__('ansible.module_utils.local.process', globals(), locals(), [], 0)
    sys.modules['ansible.module_utils.common.process'].get_bin_path = lambda: None
    # Should return False
    assert not FakeMgr().is_available()

# Generated at 2022-06-13 02:11:38.271049
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pm = PkgMgr()

    assert(pm.get_package_details("inxi") is None)


# Generated at 2022-06-13 02:11:46.731454
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class Test_PkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['python', 'python-devel']

        def get_package_details(self, package):
            return {'name': package}

    pm = Test_PkgMgr()
    packages = pm.get_packages()
    assert packages == {'python': [{'name': 'python', 'source': 'test_pkgmgr'}], 'python-devel': [{'name': 'python-devel', 'source': 'test_pkgmgr'}]}

# Generated at 2022-06-13 02:11:49.106055
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # Class CLIMgr has no method named 'test_CLIMgr_is_available'
    # This name must start with 'test_'
    assert False


# Generated at 2022-06-13 02:11:51.692265
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    try:
        CLIMgr()
    except Exception as err:
        assert False, "fail to construct class CLIMgr, error msg: %s" % err
    else:
        assert True


# Generated at 2022-06-13 02:11:53.098832
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    assert PkgMgr.get_package_details(None, None) is None


# Generated at 2022-06-13 02:12:17.363384
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    """ test_PkgMgr_list_installed
    Test list_installed method of class PkgMgr with a fictive package
    """

    class TestPkgMgr(PkgMgr):
        """ TestPkgMgr
        Implementation of abstract class PkgMgr
        """
        def list_installed(self):
            """ list_installed
            Test list_installed method of class PkgMgr with a fictive package
            """
            return ["fictive_package"]

        def get_package_details(self, package):
            """ get_package_details
            Test get_package_details method of class PkgMgr with a fictive package
            """
            if package == "fictive_package":
                return {"name": "fictive_package", "version": "0.0.1"}
            else:
                raise ValueError

# Generated at 2022-06-13 02:12:24.835506
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from unittest.mock import patch
    PATH = 'test/test'
    PATH_FAIL = 'test_fail/test_fail'

    # Negative test case
    with patch('ansible.module_utils.common.process.get_bin_path', return_value=PATH_FAIL) as mock_path:
        CLI_mgr = CLIMgr()
        assert CLI_mgr.is_available() == False
        mock_path.assert_called_once_with(PATH_FAIL)

    # Positive test case
    with patch('ansible.module_utils.common.process.get_bin_path', return_value=PATH) as mock_path:
        CLI_mgr = CLIMgr()
        assert CLI_mgr.is_available() == True

# Generated at 2022-06-13 02:12:36.086046
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pm = PkgMgr()

    def test_list_installed(self):
        pass

    def test_get_package_details(self, package):
        ret = {}
        ret['name'] = 'test'
        ret['version'] = package
        return ret

    pm.list_installed = test_list_installed
    pm.get_package_details = test_get_package_details

    installed_packages = pm.get_packages()
    assert installed_packages == {}, "installed packages should be empty"

    def test_list_installed2(self):
        return ['1', '2']

    pm.list_installed = test_list_installed2
    installed_packages = pm.get_packages()
    assert len(installed_packages) == 1, "installed packages should have length 1"


# Generated at 2022-06-13 02:12:37.312704
# Unit test for constructor of class LibMgr
def test_LibMgr():
    libmgr = LibMgr()
    assert libmgr


# Generated at 2022-06-13 02:12:45.282041
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    PkgMgr_instance = PkgMgr()
    PkgMgr_instance.list_installed = lambda : ["foo","bar"]
    PkgMgr_instance.get_package_details = lambda x: dict(name=x)
    packages = PkgMgr_instance.get_packages()
    assert isinstance(packages, dict)
    assert "foo" in packages.keys()
    assert "bar" in packages.keys()
    assert isinstance(packages["foo"], list)
    assert isinstance(packages["foo"][0], dict)

# Generated at 2022-06-13 02:12:45.596739
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pass

# Generated at 2022-06-13 02:12:50.616793
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert get_all_pkg_managers()
    assert len(get_all_pkg_managers()) > 0
    for obj in get_all_pkg_managers().values():
        pkg = obj()
        available = pkg.is_available()
        if available:
            assert pkg.list_installed()


# Generated at 2022-06-13 02:12:52.416243
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cmgr = CLIMgr()
    assert cmgr._cli is None

# Generated at 2022-06-13 02:12:54.887907
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestLibMgr(LibMgr):
        LIB = "not really a lib"
    lm = TestLibMgr()
    print(lm._lib)
    assert lm._lib == None


# Generated at 2022-06-13 02:12:56.424554
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    instance = PkgMgr()
    assert not instance.list_installed(), 'Method list_installed must be implemented in child class'

# Generated at 2022-06-13 02:13:37.697436
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.modules.legacy.packaging.os import Yum
    # Yum package manager is installed by default on CentOS, so using it for testing
    yum = Yum()

    # Calling is_available to make sure the package manager is installed
    assert yum.is_available()

    # Calling get_packages
    pkg_mgr_dict = yum.get_packages()

    # The package manager dictionary should at least have one package with at least one version
    assert pkg_mgr_dict
    assert pkg_mgr_dict.get('bash', None)
    assert pkg_mgr_dict.get('bash', [{}])[0].get('version', None)

# Generated at 2022-06-13 02:13:43.431834
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    import unittest
    import os
    import sys

    # Break import cycle
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.facts.system.pkg_mgr import (LibMgr, CLIMgr, PkgMgr, get_all_pkg_managers)

    class Test_PkgMgr(unittest.TestCase):

        def test_get_packages(self):

            # Get all package managers
            pkg_managers = get_all_pkg_managers()

            # Get the name of the test directory
            test_dir = os.path.dirname(os.path.realpath(__file__))

            # Get the test case name
            test_name = self._testMethodName

            # Create a test file, if not already present
           

# Generated at 2022-06-13 02:13:49.875123
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    import ansible.module_utils.pycompat24
    cli_mgr = CLIMgr()
    lib_mgr = LibMgr()
    # Test failure of CLI and LIB not found in path
    assert cli_mgr.is_available() is False
    assert lib_mgr.is_available() is False
    # Test failure of CLI not found in path
    cli_mgr.CLI = 'python'
    lib_mgr.LIB = 'ansible.module_utils.pycompat24'
    assert cli_mgr.is_available() is True
    assert lib_mgr.is_available() is True

# Generated at 2022-06-13 02:13:53.042891
# Unit test for constructor of class LibMgr
def test_LibMgr():
    ansible_pkg_manager = LibMgr()
    assert(ansible_pkg_manager.is_available() is None)
    assert(ansible_pkg_manager.list_installed() is None)
    assert(ansible_pkg_manager.get_package_details(package="any_package") is None)

# Generated at 2022-06-13 02:13:58.260465
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class DummyMgr(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ["pkg1", "pkg2"]
        def get_package_details(self, package):
            return {'name': package}
    dum = DummyMgr()
    # Assert we get a dictionary of the list of installed packages
    assert dum.get_packages() == {'pkg1': [{'source': 'dummymgr', 'name': 'pkg1'}],
                                  'pkg2': [{'source': 'dummymgr', 'name': 'pkg2'}]}

# Generated at 2022-06-13 02:14:03.640971
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import sys
    import os.path
    # Use the current directory, unless running from the source distribution
    # in which case look in ../../lib:
    if os.path.exists(os.path.join(os.path.dirname(__file__), '__init__.py')):
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
    pkgmgr = PkgMgr()
    pkgmgr.list_installed = lambda: ['foo']
    pkgmgr.get_package_details = lambda package: {'name': 'bar', 'version': '1.2.3'}

# Generated at 2022-06-13 02:14:04.897205
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    a = CLIMgr()

# Generated at 2022-06-13 02:14:06.805213
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    test_p = CLIMgr()
    assert type(CLIMgr.is_available(test_p)) == bool


# Generated at 2022-06-13 02:14:13.134729
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class MyPkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['1', '2', '3']

        def get_package_details(self, package):
            return {'name': package}

    pkg_mgr = MyPkgMgr()
    packages = pkg_mgr.get_packages()
    assert packages['1'] == [{'name': '1', 'source': 'mypkgmgr'}]
    assert packages['2'] == [{'name': '2', 'source': 'mypkgmgr'}]
    assert packages['3'] == [{'name': '3', 'source': 'mypkgmgr'}]

# Generated at 2022-06-13 02:14:16.185863
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    mgr = CLIMgr(CLI='sh')
    assert mgr.is_available()
    
if __name__ == '__main__':
    test_CLIMgr()

# Generated at 2022-06-13 02:15:39.732655
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    pkg_mgr_list = get_all_pkg_managers()
    assert isinstance(pkg_mgr_list, dict)
    assert set(pkg_mgr_list.keys()) == set(['dpkg', 'rpm', 'python', 'node', 'java', 'virtualenv', 'npm', 'gpg', 'yum', 'apt', 'pip'])

# Generated at 2022-06-13 02:15:40.395416
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    print("Not implemented")


# Generated at 2022-06-13 02:15:43.694640
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    ''' Test to see if we can get the all pkg module names '''
    all_pkg_managers = get_all_pkg_managers()
    ignored = ['cli_mgr', 'lib_mgr', 'pkg_mgr']
    for pkg_mgr in all_pkg_managers:
        assert pkg_mgr not in ignored

# Generated at 2022-06-13 02:15:45.338563
# Unit test for constructor of class LibMgr
def test_LibMgr():

    a = LibMgr()
    if a.is_available() is True:
        assert(True)
    else:
        assert(False)


# Generated at 2022-06-13 02:15:46.476683
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pkg_mgr = LibMgr()
    assert not pkg_mgr.is_available()


# Generated at 2022-06-13 02:15:48.536733
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    assert isinstance(get_all_pkg_managers(), dict)

# Generated at 2022-06-13 02:15:52.242394
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    import os
    pkgmgr = PkgMgr()
    try:
        pkgmgr.list_installed()
    except NotImplementedError:
        pass
    except AttributeError:
        pass
    except:
        assert False
    else:
        assert True


# Generated at 2022-06-13 02:15:59.467111
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class _LibMgr(LibMgr):
        LIB = "test_LibMgr_is_available_MockLibrary"

    libmgr = _LibMgr()
    assert not libmgr.is_available()
    assert libmgr._lib is None

    class _module_mock:
        pass

    with mock.patch.dict(sys.modules, {_LibMgr.LIB: _module_mock}):
        assert libmgr.is_available()
        assert libmgr._lib == _module_mock



# Generated at 2022-06-13 02:16:01.600939
# Unit test for constructor of class LibMgr
def test_LibMgr():
    libmgr=LibMgr()
    assert (libmgr is LibMgr)

if __name__ == '__main__':
    test_LibMgr()

# Generated at 2022-06-13 02:16:08.012445
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class MockPkgMgr(PkgMgr):
        def __init__(self):
            self.list_installed_list = []
            self.get_package_details_dict_list = []
            super(MockPkgMgr, self).__init__()

        def list_installed(self):
            return self.list_installed_list

        def get_package_details(self, package):
            return self.get_package_details_dict_list.pop(0)
    pkg_mgr = MockPkgMgr()
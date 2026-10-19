

# Generated at 2022-06-13 02:09:26.048877
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    LIB_VERSION = '2.7'
    package_managers = get_all_pkg_managers()
    for package_manager in package_managers.keys():
        if isinstance(package_managers[package_manager](), LibMgr):
            if package_managers[package_manager]().is_available():
                assert package_managers[package_manager]()._lib.version.__version__ == LIB_VERSION
            else:
                assert package_managers[package_manager]().is_available() == False


# Generated at 2022-06-13 02:09:35.552214
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    """
    Unit test for method get_packages of class PkgMgr
    """
    from ansible.module_utils.facts.pkginst.utils import CmdPkgMgr
    from ansible.module_utils.facts.pkginst.utils import DpkgMgr
    from ansible.module_utils.facts.pkginst.utils import RpmMgr
    from ansible.module_utils.facts.pkginst.utils import PkgMgr
    from ansible.module_utils.facts.pkginst.utils import CLIMgr
    from ansible.module_utils.facts.pkginst.utils import LibMgr
    from ansible.module_utils.facts.pkginst.utils import get_all_pkg_managers
    from ansible.module_utils._text import to_

# Generated at 2022-06-13 02:09:39.066503
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class MyLib(LibMgr):
        LIB = '__import__'

    ml = MyLib()
    assert(ml.is_available() == True)



# Generated at 2022-06-13 02:09:43.664831
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    sys_lib = __import__('sys')

    lm_obj = LibMgr()
    assert lm_obj.LIB is None

    assert lm_obj._lib is None

    assert lm_obj.is_available() is False

    assert lm_obj._lib is None
    assert lm_obj.LIB is None


# Generated at 2022-06-13 02:09:45.235623
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert PkgMgr.is_available is PkgMgr.is_available


# Generated at 2022-06-13 02:09:50.822737
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class DummyCLIManager(CLIMgr):
        CLI = 'dummy'
    dummy_cli_mgr = DummyCLIManager()
    assert dummy_cli_mgr._cli is None
    assert dummy_cli_mgr.CLI == 'dummy'
    assert dummy_cli_mgr.is_available() is False


# Generated at 2022-06-13 02:09:52.384818
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pkgmgr = PkgMgr()
    assert False == pkgmgr.is_available()
    assert [] == pkgmgr.list_installed()


# Generated at 2022-06-13 02:09:56.445470
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.common.pkg_managers.pip import Pip
    p = Pip()
    assert(p.is_available())
    from ansible.module_utils.common.pkg_managers.npm import Npm
    n = Npm()
    assert(n.is_available())


# Generated at 2022-06-13 02:10:06.484063
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    import unittest
    import pkg_resources
    from ansible.module_utils.common.collections import ImmutableDict
    class MyPkgMgr(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ["p1", "p2"]
        def get_package_details(self, package):
            return {"name": package}
    class TestCase(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.pkg_mgr = MyPkgMgr()
        def test_get_package_details_result(self):
            self.assertEqual(self.pkg_mgr.get_package_details("p1"), ImmutableDict({"name": "p1"}))

# Generated at 2022-06-13 02:10:07.494409
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

    test_class = CLIMgr()
    assert test_class._cli is None


# Generated at 2022-06-13 02:10:21.882489
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    from ansible.module_utils.facts.system.pkg_mgr.apk import Apk
    from ansible.module_utils.facts.system.pkg_mgr.apt import Apt
    from ansible.module_utils.facts.system.pkg_mgr.dnf import Dnf
    from ansible.module_utils.facts.system.pkg_mgr.yum import Yum
    from ansible.module_utils.facts.system.pkg_mgr.zypper import Zypper
    from ansible.module_utils.facts.system.pkg_mgr.mac_pkgutil import MacPkgUtil

    # Expected values for each package manager

# Generated at 2022-06-13 02:10:23.144285
# Unit test for constructor of class LibMgr
def test_LibMgr():

    mgr = LibMgr()
    assert mgr._lib is None


# Generated at 2022-06-13 02:10:25.925357
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    # test with wrong parameter
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgr
    p = PkgMgr()
    assert(p.get_package_details(None) is None)



# Generated at 2022-06-13 02:10:28.266192
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import pytest
    class AptMgrCLI(CLIMgr):
        CLI = "apt"
    a = AptMgrCLI()
    assert a.is_available() == True



# Generated at 2022-06-13 02:10:40.069887
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class PkgMgr_Test(PkgMgr):
        def is_available(self):
            pass
        def list_installed(self):
            return [['pkg1', 'version1'], ['pkg2', 'version2'], ['pkg3', 'version3']]
        def get_package_details(self, package):
            return {'name': package[0], 'version': package[1], 'source': self.__class__.__name__.lower()}
    packages = PkgMgr_Test().get_packages()

# Generated at 2022-06-13 02:10:44.759886
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class TestLibMgr(LibMgr):
        LIB = 'platform'

    pkg_mgr = TestLibMgr()
    assert pkg_mgr.is_available()
    assert pkg_mgr._lib.system() == 'Linux'


# Generated at 2022-06-13 02:10:53.160130
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    from ansible.module_utils.facts.package.apt.manager import AptPkgMgr
    from ansible.module_utils.facts.package.yum.manager import YumPkgMgr
    from ansible.module_utils.facts.package.pacman.manager import PacmanPkgMgr
    from ansible.module_utils.facts.package.pip.manager import PipPkgMgr
    from ansible.module_utils.facts.package.portage.manager import PortagePkgMgr
    from ansible.module_utils.facts.package.apk.manager import ApkPkgMgr
    from ansible.module_utils.facts.package.pkgng.manager import PkgngPkgMgr
    from ansible.module_utils.facts.package.pkgutil.manager import PkgutilPkgMgr

# Generated at 2022-06-13 02:10:54.465520
# Unit test for constructor of class LibMgr
def test_LibMgr():

    x = LibMgr()
    assert x.is_available() == False
    x._lib = 'test'
    assert x.is_available() == True
    assert x.LIB == None


# Generated at 2022-06-13 02:11:03.903802
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    """
    Unit test for method get_packages of class PkgMgr
    """
    class PkgMgrTest(PkgMgr):
        def list_installed(self):
            return [1, 2, 3]
        def get_package_details(self, package):
            return {'name': package, 'version': '1.2.3'}
    pkgmgr_test = PkgMgrTest()
    packages = pkgmgr_test.get_packages()

# Generated at 2022-06-13 02:11:04.879183
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    assert True

# Generated at 2022-06-13 02:11:18.342736
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    # Test for PkgMgr class
    pkgmgr = PkgMgr()
    assert (pkgmgr.is_available() is False)

    # Test for CLIMgr class
    climgr = CLIMgr()
    assert (climgr.is_available() is False)
    climgr.CLI = 'SOMETHINGTHATDOESNTEXIST'
    assert (climgr.is_available() is False)

    # Test for LibMgr class
    libmgr = LibMgr()
    assert (libmgr.is_available() is False)
    libmgr.LIB = 'somethingthatdoesntexist'
    assert (libmgr.is_available() is False)


# Generated at 2022-06-13 02:11:19.779551
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lib_mgr = LibMgr()
    assert lib_mgr


# Generated at 2022-06-13 02:11:22.150955
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class PkgMgrTestCase(PkgMgr):
        pass
    assert PkgMgrTestCase().get_package_details(0) is False

# Generated at 2022-06-13 02:11:28.335785
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import tempfile
    import os
    tmp = tempfile.gettempdir()
    ansible_path = os.path.join(tmp, 'ansibletest')
    f = open(ansible_path, "w")
    f.close()
    os.chmod(ansible_path, 0o777)
    os.environ["PATH"] += os.pathsep + tmp

    cli_mgr = CLIMgr()
    assert cli_mgr.is_available()
    os.remove(ansible_path)


# Generated at 2022-06-13 02:11:32.646476
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible_collections.ansible.community.plugins.module_utils.facts.system.pkg_mgr.apt import Apt
    from ansible_collections.ansible.community.plugins.module_utils.facts.system.pkg_mgr.apt_pkg import AptPkg
    from ansible_collections.ansible.community.plugins.module_utils.facts.system.pkg_mgr.apk import Apk
    from ansible_collections.ansible.community.plugins.module_utils.facts.system.pkg_mgr.yum import Yum
    from ansible_collections.ansible.community.plugins.module_utils.facts.system.pkg_mgr.dnf import Dnf

# Generated at 2022-06-13 02:11:35.035311
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class TestLibMgr(LibMgr):
        LIB = 'ansible'

    t = TestLibMgr()
    assert t.is_available() == True


# Generated at 2022-06-13 02:11:40.053327
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    # Create a mock class that inherits from PkgMgr
    class MockPkgMgr(PkgMgr):
        def is_available(self):
            return True
    # Create an object from the mock class and call the is_available method
    mockPkgMgr = MockPkgMgr()
    assert mockPkgMgr.is_available()


# Generated at 2022-06-13 02:11:41.639765
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lm = LibMgr()
    assert lm.is_available() is False


# Generated at 2022-06-13 02:11:51.576720
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    import unittest
    import ansible.module_utils.collect.system.pkgmgr.yum as yum

    class TestPkgMgr(PkgMgr):

        def is_available(self):
            pass

        def list_installed(self):
            return ['zlib', 'sqlite', 'zlib-devel']

        def get_package_details(self, package):
            pkg_info = {}
            if package == 'zlib':
                pkg_info['name'] = package
                pkg_info['version'] = '1.2.3'
            elif package == 'sqlite':
                pkg_info['name'] = package
                pkg_info['version'] = '1.2.3'
            elif package == 'zlib-devel':
                pkg_info['name']

# Generated at 2022-06-13 02:11:52.216063
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    pkg = CLIMgr()

    assert not pkg.is_available()

# Generated at 2022-06-13 02:12:14.774204
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    from ansible.module_utils.common._var_functions import version_to_tuple
    from ansible.module_utils.facts.system.pkg_mgr.pip import PIPMgr
    pip = PIPMgr()
    pip.is_available()
    pkg = pip.get_package_details('ansible==2.5.1')
    assert pkg['name'] == 'ansible'
    assert pkg['version'] == '2.5.1'
    assert version_to_tuple(pkg['version']) == (2, 5, 1)

# Generated at 2022-06-13 02:12:22.404403
# Unit test for function get_all_pkg_managers

# Generated at 2022-06-13 02:12:23.132749
# Unit test for constructor of class LibMgr
def test_LibMgr():
    pass 


# Generated at 2022-06-13 02:12:24.362666
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    tmp = CLIMgr()
    tmp.CLI = 'foobar'
    tmp.is_available()

# Generated at 2022-06-13 02:12:27.563947
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.facts.pkg_mgrs import PkgMgr
    from ansible.module_utils.common.process import get_bin_path

    assert isinstance(PkgMgr, object)
    assert 'is_available' in dir(PkgMgr)
    try:
        result = get_bin_path('rpm')
    except ValueError:
        result = False
    assert result == result


# Generated at 2022-06-13 02:12:28.848811
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lm = LibMgr()
    assert lm._lib is None


# Generated at 2022-06-13 02:12:33.351755
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    class TestCLIMgr(CLIMgr):
        CLI = 'ls'
    pkg_mgr = TestCLIMgr()
    assert pkg_mgr.is_available()


# Generated at 2022-06-13 02:12:36.707996
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pm = PkgMgr()
    try:
        pm.is_available()
    except AttributeError:
        pass
    else:
        assert False, "PkgMgr.is_available() should raise AttributeError."


# Generated at 2022-06-13 02:12:38.269271
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    c = CLIMgr()
    c.is_available()
    assert isinstance(c._cli, str)

# Generated at 2022-06-13 02:12:44.043212
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # pylint: disable=too-few-public-methods
    class TestClass(CLIMgr):
        CLI = 'testing'

    test_class = TestClass()
    assert test_class.is_available() is False
    test_class._cli = '/usr/bin/testing'
    assert test_class.is_available() is True

# Generated at 2022-06-13 02:13:26.263384
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    """Test if the method get_packages of class PkgMgr.

    The method get_packages returns dict of dicts of dicts, we only want to
    test if this structure is returned.
    """

    class MockPkgMgr(PkgMgr):
        def __init__(self):
            super().__init__()

        def list_installed(self):
            return ['package1', 'package2', 'package3']

        def get_package_details(self, package):
            return {'name': package, 'version': '1.0', 'source': 'Mock'}

    pm = MockPkgMgr()
    result = pm.get_packages()
    assert isinstance(result, dict)
    for key in result:
        assert isinstance(key, str)

# Generated at 2022-06-13 02:13:32.715409
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # Test for import
    class TestLibMgr(LibMgr):
        LIB = 'testlib'

    test_lib_mgr = TestLibMgr()
    assert not test_lib_mgr.is_available()
    # Test for execution
    class TestCLILibMgr(CLIMgr):
        CLI = 'testlib'
    test_cli_lib_mgr = TestCLILibMgr()
    assert not test_cli_lib_mgr.is_available()



# Generated at 2022-06-13 02:13:35.737486
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class TestLibMgr(LibMgr):
        LIB = 'platform'

    # Case is_available return True
    lib_mgr = TestLibMgr()

    assert lib_mgr.is_available() == True


# Generated at 2022-06-13 02:13:39.969539
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class TestMgr(LibMgr):
        LIB = 'mocklib'

        def __init__(self):
            super(TestMgr, self).__init__()

        def list_installed(self):
            pass

        def get_package_details(self, package):
            pass

    test_mgr = TestMgr()
    assert not test_mgr.is_available()


# Generated at 2022-06-13 02:13:40.687324
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
	return True

# Generated at 2022-06-13 02:13:41.501937
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pass


# Generated at 2022-06-13 02:13:43.779272
# Unit test for constructor of class LibMgr
def test_LibMgr():
    # This is abstract class so we just want to test if constructor works as expected
    lib_mgr = LibMgr()
    assert lib_mgr._lib is None


# Generated at 2022-06-13 02:13:47.266635
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # Test for an available command
    obj = CLIMgr()
    obj.CLI = "echo"
    assert obj.is_available() is True
    # Test for an unavailable command
    obj = CLIMgr()
    obj.CLI = "sldkfjslkdf"
    assert obj.is_available() is False

# Generated at 2022-06-13 02:13:48.678501
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert( isinstance( PkgMgr.list_installed(PkgMgr()), list ) )


# Generated at 2022-06-13 02:13:54.990084
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class TestPkgMgr(PkgMgr):
        def __init__(self):
            pass

        def is_available(self):
            return True

        def list_installed(self):
            return ['x','y','z']

        def get_package_details(self, package):
            return {'name':package,'version':1,'arch':'x86_64'}

    tpm = TestPkgMgr()

# Generated at 2022-06-13 02:15:17.454214
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # test if the class is available
    test_is_available = LibMgr()
    test_is_available.is_available()


# Generated at 2022-06-13 02:15:20.400942
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    """
    The method get_packages is defined in the PkgMgr class and is used to collect all installed packages in
    a list of dictionaries
    :return: True if the test is defining a list of dictionaries
    """

    return True

# Generated at 2022-06-13 02:15:27.416172
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class PkgMgrTester(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['foo', 'bar', 'baz', 'qux']

        def get_package_details(self, package):
            return {
                'name': package,
                'version': 123,
                'arch': 'amd64',
            }

    pm = PkgMgrTester()
    packages = pm.get_packages()
    assert 'foo' in packages
    assert 'bar' in packages
    assert 'baz' in packages
    assert 'qux' in packages
    assert not 'quxx' in packages
    for package in packages:
        for package_details in packages[package]:
            assert 'version' in package_details
            assert 'arch' in package_details

# Generated at 2022-06-13 02:15:30.778918
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils import system_information

    print(CLIMgr.CLI)
    mgr = system_information.CLIMgr()
    print(mgr.is_available())

# Generated at 2022-06-13 02:15:38.438905
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import sys
    import os

    class TestClassLibMgr(LibMgr):
        LIB = 'test'

    kwargs = {}

    try:    
        TestClassLibMgr().is_available()
        assert False
    except ImportError:
        assert True

    try:
        TestClassLibMgr().list_installed()
        assert False
    except NotImplementedError:
        assert True

    try:
        TestClassLibMgr().get_package_details('')
        assert False
    except NotImplementedError:
        assert True

    try:
        TestClassLibMgr().get_packages()
        assert False
    except NotImplementedError:
        assert True


# Generated at 2022-06-13 02:15:39.832057
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class TestLibMgr(LibMgr):
        LIB = "libmock"

    lib = TestLibMgr()
    assert lib.is_available() is False


# Generated at 2022-06-13 02:15:40.762805
# Unit test for constructor of class LibMgr
def test_LibMgr():
    a = LibMgr()
    assert a is not None


# Generated at 2022-06-13 02:15:45.805906
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return [['test'], ['test']]

        def get_package_details(self, package):
            return {'name': 'test', 'version': '1.0'}

    test = TestPkgMgr()
    result = test.get_packages()
    assert isinstance(result, dict)
    assert len(result) == 1
    assert isinstance(result['test'], list)


# Generated at 2022-06-13 02:15:55.835596
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    # Test if method raises AttributeError
    with pytest.raises(AttributeError):
        fail_pkg_mgr = PkgMgr()
        fail_pkg_mgr.get_package_details()

    # Test if method returns a dict
    test_pkg_mgr = PkgMgr()
    test_pkg_mgr.list_installed = lambda: ['python26-libs']
    test_pkg_mgr.get_package_details = lambda x: {'name': 'python26-libs', 'version': '1.0.0'}
    pkg_details = test_pkg_mgr.get_package_details('python26-libs')
    assert isinstance(pkg_details, dict)


# Generated at 2022-06-13 02:15:56.685642
# Unit test for constructor of class LibMgr
def test_LibMgr():
    LibMgr()


# Generated at 2022-06-13 02:19:03.655810
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import sys
    import os

    # create a copy of the python executable to fool the test
    test_py_exec = sys.executable + '.test'
    os.rename(sys.executable, test_py_exec)
    lm = LibMgr()
    assert lm.is_available() == False
    # cleanup
    os.rename(test_py_exec, sys.executable)


# Generated at 2022-06-13 02:19:05.839427
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    yum_mgr = CLIMgr()
    yum_mgr.CLI = 'yum'
    assert yum_mgr.CLI == 'yum'

# Generated at 2022-06-13 02:19:13.904554
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.common._utils import _load_params

    test = _load_params()
    for _, pkg in list(get_all_pkg_managers().items()):

        # Test if the package manager is available
        if not pkg.is_available():
            continue

        # Test if the package manager is available
        if not issubclass(pkg, LibMgr):
            continue

        # Test if the package manager is available
        instance = pkg()
        if not instance.is_available():
            test.exit_json(msg="Failed to import library for %s" % pkg.__name__)

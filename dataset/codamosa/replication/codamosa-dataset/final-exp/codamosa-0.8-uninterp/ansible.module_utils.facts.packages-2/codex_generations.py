

# Generated at 2022-06-13 02:09:28.538553
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # Test PkgMgr class for method get_packages
    # define a class to use for testing, with a minimal value for each required method
    class TestPkgMgr(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return ['package1', 'package2']

        def get_package_details(self, package):
            if package == 'package1':
                return {'name': 'package1', 'version': '1.0', 'source': 'test1'}
            else:
                return {'name': 'package2', 'version': '2.0', 'source': 'test2'}

    # instantiate the class
    obj = TestPkgMgr()

    # call the method
    pkg_details = obj.get_packages()

    # check

# Generated at 2022-06-13 02:09:37.701653
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    with open("/tmp/test_file1", "w") as f:
        f.write("kdjfkdj") 
    with open("/tmp/test_file2", "w") as f:
        f.write("kdjfkdj")
    with open("/tmp/test_file3", "w") as f:
        f.write("kdjfkdj")

    class Test_PkgMgr(PkgMgr):
        def list_installed(self):
            return ["/tmp/test_file1", "/tmp/test_file2", "/tmp/test_file3","/tmp/test_file4"]
        def get_package_details(self,package):
            return {"name":package.split("/")[-1].split('.')[0]}


    t = Test_PkgMgr

# Generated at 2022-06-13 02:09:40.235711
# Unit test for constructor of class LibMgr
def test_LibMgr():
    packages = LibMgr()
    assert packages
    assert packages._lib is None



# Generated at 2022-06-13 02:09:42.421313
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    from ansible.module_utils.facts.pkg_mgr import get_all_pkg_managers
    assert 'dnf' in get_all_pkg_managers()
    assert 'ansible_pkg_mgr' in get_all_pkg_managers()

# Generated at 2022-06-13 02:09:45.151462
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class LibMgrTest(LibMgr):
        LIB = 'sys'

    libmgr = LibMgrTest()
    assert libmgr.is_available() is True


# Generated at 2022-06-13 02:09:55.620170
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.common._collections_compat import Mapping
    import inspect
    import imp

    # Load the actual package manager modules
    managers = []
    for mod in get_all_pkg_managers().values():
        try:
            managers.append(imp.load_source(mod.__name__, inspect.getsourcefile(mod)))
        except Exception:
            continue

    # Test is_available
    # Make sure all package managers are a subclass of LibMgr and have a LIB attribute
    # Test each package manager and make sure is_available returns a boolean

# Generated at 2022-06-13 02:09:57.216516
# Unit test for constructor of class LibMgr
def test_LibMgr():
    libMgr = LibMgr()
    assert libMgr != None


# Generated at 2022-06-13 02:09:58.616926
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    assert LibMgr.is_available(LibMgr()) == True

# Generated at 2022-06-13 02:10:08.054284
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class mock_PkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ["pack2-1.0-1.el6.x86_64", "pack1-1.0-1.el6.x86_64"]

        def get_package_details(self, pkg):
            return {"name": pkg.split('-')[0], "version": pkg.split('-')[1]}

    res = mock_PkgMgr().get_packages()

# Generated at 2022-06-13 02:10:13.987396
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    # Test with a CLIMgr
    import subprocess
    cmd = "/bin/sh"
    if "SHELL" in subprocess.os.environ:
        cmd = subprocess.os.environ.get("SHELL")

    class TestCLIMgr(CLIMgr):
        CLI = cmd

    test_is_available_CLIMgr = TestCLIMgr()
    assert test_is_available_CLIMgr.is_available() is True

    # Test with a LibMgr with a valid library
    class TestLibMgr(LibMgr):
        LIB = subprocess.__name__

    test_is_available_LibMgr = TestLibMgr()
    assert test_is_available_LibMgr.is_available() is True

    # Test with a LibMgr with a non-existing library

# Generated at 2022-06-13 02:10:25.373677
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import pkg_resources
    class TestMgr(LibMgr):
        LIB = 'pkg_resources'

    test_mgr = TestMgr()
    assert test_mgr.is_available()

    import json
    class TestMgr(LibMgr):
        LIB = 'json'

    test_mgr = TestMgr()
    assert test_mgr.is_available()

    class TestMgr(LibMgr):
        LIB = 'gevent'

    test_mgr = TestMgr()
    assert not test_mgr.is_available()


# Generated at 2022-06-13 02:10:26.854925
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lm = LibMgr()
    assert lm.is_available() is False


# Generated at 2022-06-13 02:10:32.387988
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    mgr = CLIMgr()
    mgr.CLI = 'rpm'
    assert mgr.is_available() == True

    mgr.CLI = 'rpm1'
    assert mgr.is_available() == False

    mgr.CLI = 'apt-get'
    assert mgr.is_available() == True

    mgr.CLI = 'apt'
    assert mgr.is_available() == True

    mgr.CLI = 'dpkg'
    assert mgr.is_available() == True

    mgr.CLI = 'dpk'
    assert mgr.is_available() == False


# Generated at 2022-06-13 02:10:34.153196
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    PkgMgr().is_available() is None


# Generated at 2022-06-13 02:10:41.341005
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class MyPkgMgr(PkgMgr):
        def __init__(self):
            pass

        def is_available(self):
            return True

        def list_installed(self):
            return ['package1', 'package2']

        def get_package_details(self, package):
            return {'name': package, 'version': '1.0'}

    s = MyPkgMgr()

    installed = s.list_installed()
    assert len(installed) == 2, "Unable to retrieve the list of installed packages"


# Generated at 2022-06-13 02:10:43.436751
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    pkg = CLIMgr()
    assert pkg is not None

# Generated at 2022-06-13 02:10:48.419855
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    available_pkg_mgr = PkgMgr()
    try:
        assert not available_pkg_mgr.is_available()
        assert False
    except (AttributeError, NotImplementedError):
        assert True
    except Exception as e:
        assert False, "Unexpected exception raised: " + str(e)


# Generated at 2022-06-13 02:10:49.949895
# Unit test for constructor of class LibMgr
def test_LibMgr():
    pkgmgr = LibMgr()
    assert not pkgmgr._lib


# Generated at 2022-06-13 02:10:52.105003
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pmgr = PkgMgr()
    assert pmgr.get_package_details('not a real package') is None


# Generated at 2022-06-13 02:10:54.995036
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    cli_mgr = CLIMgr()
    assert cli_mgr.is_available() == True


# Generated at 2022-06-13 02:11:02.821927
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    from ansible_collections.vmware.vmware_rest.plugins.module_utils.facts.pkg_mgr import PkgMgr
    obj = PkgMgr()
    res = obj.is_available()
    assert(res is None)

# Generated at 2022-06-13 02:11:05.660454
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class TestCLI(CLIMgr):
        CLI = 'test_CLI'
    testCLI = TestCLI()
    assert testCLI.is_available() == False


# Generated at 2022-06-13 02:11:08.579348
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import platform
    class FakeMgr(LibMgr):
        LIB = 'platform'
    obj = FakeMgr()
    assert obj.is_available() == True


# Generated at 2022-06-13 02:11:14.896016
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # Check if there is a case when the library is found
    lib_mgr = LibMgr()
    lib_mgr.LIB = 'getpass'
    lib_mgr_found = lib_mgr.is_available()
    assert lib_mgr_found is True
    # Check if there is a case when the library is not found
    lib_mgr = LibMgr()
    lib_mgr.LIB = 'foo'
    lib_mgr_not_found = lib_mgr.is_available()
    assert lib_mgr_not_found is False


# Generated at 2022-06-13 02:11:25.321568
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    import sys
    import tempfile
    import shutil
    import os

    class LibMgrTest(LibMgr):
        LIB = 'test_lib_mgr'

    sys_module = sys.modules.get('test_lib_mgr')
    if sys_module:
        del sys.modules['test_lib_mgr']

    lib_mgr_test = LibMgrTest()
    assert not lib_mgr_test.is_available(), "LibMgr available with no module"

    with tempfile.TemporaryDirectory() as dir_path:
        f = open(os.path.join(dir_path, '__init__.py'), 'w')
        f.close()

        f = open(os.path.join(dir_path, 'test.py'), 'w')
        f.close()


# Generated at 2022-06-13 02:11:35.047865
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import sys
    sys.modules['_sysconfigdata_m'] = type('FakeSysConfigData', (object,), {'_INSTALL_SCHEMES': {'posix_home': '/home'}})

    from ansible.module_utils.facts.system.bindep import BindepPkgMgr
    from ansible.module_utils.facts.system.dnf import DnfPkgMgr
    from ansible.module_utils.facts.system.dpkg import DpkgPkgMgr
    from ansible.module_utils.facts.system.freebsd_pkg import FreeBSDPkgPkgMgr
    from ansible.module_utils.facts.system.macports import MacPortsPkgMgr
    from ansible.module_utils.facts.system.netbsd_pkg import NetBSDPkgPkg

# Generated at 2022-06-13 02:11:35.873077
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert LibMgr is not None


# Generated at 2022-06-13 02:11:38.227890
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # Set up
    # Nothing to do

    # Execute
    result = LibMgr().is_available()

    # Assert
    assert result



# Generated at 2022-06-13 02:11:42.194485
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestLibMgr(LibMgr):
        LIB = 'subprocess'
    test_lib_mgr = TestLibMgr()
    assert not test_lib_mgr._lib
    assert test_lib_mgr.LIB == 'subprocess'


# Generated at 2022-06-13 02:11:45.992825
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
   class TestPkgMgr(PkgMgr):
      def list_installed(self):
         return ['foo', 'bar']

      def get_package_details(self, package):
         pass

   try:
      a = TestPkgMgr()
      res = a.list_installed()
      if type(res) is not list:
         raise AssertionError("Type of list_installed must be list, got %s" % type(res))
   except NotImplementedError:
      pass
   except Exception as err:
      raise AssertionError("list_installed raised %s" % err)

# Generated at 2022-06-13 02:11:57.270240
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    # Unit test setup
    class MockPkgMgr(PkgMgr):
        def __init__(self):
            super(MockPkgMgr, self).__init__()
            self.list_installed_packages = ["test"]
            self.package_values = {'name': 'test', 'version': 'test', 'release': 'test', 'source': 'test'}

        def is_available(self):
            return True

        def list_installed(self):
            return self.list_installed_packages

    # Unit test for method get_package_details of class PkgMgr
    # Test case 1:
    mock_pkgmgr = MockPkgMgr()
    assert mock_pkgmgr.get_package_details("test")

# Generated at 2022-06-13 02:12:07.869517
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    import pytest
    from ansible.module_utils.compat import PY2
    from ansible.module_utils.common.compat import get_encoded_line

    class NewPkgMgr(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return ("firefox", "fish", "vim")

        def get_package_details(self, package_name):
            return {"name": package_name, "version": "1.0"}

    p = NewPkgMgr()
    assert p.get_package_details("firefox")["name"] == "firefox"
    assert p.get_package_details("fish")["name"] == "fish"
    assert p.get_package_details("vim")["name"] == "vim"


# Generated at 2022-06-13 02:12:10.864486
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    for pkg in get_all_pkg_managers().values():
        m = pkg()
        if m.is_available():
            for key, value in m.get_packages().items():
                assert value != []

# Generated at 2022-06-13 02:12:12.382653
# Unit test for constructor of class LibMgr
def test_LibMgr():
    instance = LibMgr()
    assert instance


# Generated at 2022-06-13 02:12:13.330424
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pass


# Generated at 2022-06-13 02:12:15.496660
# Unit test for constructor of class LibMgr
def test_LibMgr():
    libmgr = LibMgr()
    assert libmgr is not None

# Generated at 2022-06-13 02:12:18.391543
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # Create instance of LibMgr without assignment of LIB
    # This should raise an exception
    try:
        Lib = LibMgr()
        Lib.is_available()
    except AttributeError:
        pass


# Generated at 2022-06-13 02:12:21.093078
# Unit test for constructor of class LibMgr
def test_LibMgr():
    from ansible.module_utils.facts.package_manager.pip import Pip
    libr = LibMgr()
    assert not libr.is_available()
    libr = Pip()
    assert libr.is_available()


# Generated at 2022-06-13 02:12:27.393450
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    expected_packages = {'python': [{'name': 'python', 'version': '2.7.5', 'source': 'pacman', 'comment': '', 'arch': 'x86_64', 'license': 'GPL', 'repository': 'installed', 'summary': 'Python 2', 'size': 1874880}], 'gcc-libs': [{'name': 'gcc-libs', 'version': '4.8.5-8', 'source': 'pacman', 'comment': '', 'arch': 'x86_64', 'license': 'GPL', 'repository': 'installed', 'summary': 'Runtime libraries shipped by GCC', 'size': 7424}]}
    all_pk_mgrs = get_all_pkg_managers()

# Generated at 2022-06-13 02:12:29.388011
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lm = LibMgr()
    assert lm.is_available() == False


# Generated at 2022-06-13 02:12:45.507852
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class TestCLIMgr(CLIMgr):
        CLI = 'ls'

        def get_packages(self):
            pass

    test_CLIMgr = TestCLIMgr()
    assert test_CLIMgr.is_available() == True

    class TestCLIMgr(CLIMgr):
        CLI = 'this_clicommand_does_not_exist'

        def get_packages(self):
            pass

    test_CLIMgr = TestCLIMgr()
    assert test_CLIMgr.is_available() == False

# Generated at 2022-06-13 02:12:46.492060
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    obj = CLIMgr()
    assert obj is not None

# Generated at 2022-06-13 02:12:48.543362
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pkgmgr = CLIMgr()
    assert pkgmgr.is_available() == False


# Generated at 2022-06-13 02:12:51.025930
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pkg_mgr = PkgMgr()
    assert not pkg_mgr.list_installed()
    return True


# Generated at 2022-06-13 02:12:58.549174
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import sys
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_bytes
    cmd = sys.executable.encode('utf-8')
    tmp = None
    pythonlib = None
    try:
        tmp = to_bytes(get_bin_path("python"))
        to_bytes(get_bin_path("false"))
    except ValueError:
        pythonlib = tmp
    if pythonlib is not None:
        setattr(sys, '_meipass', pythonlib)
    pythonlib = sys.executable
    class test(LibMgr):
        LIB = '_io'
    test_lib = test()
    assert test_lib.is_available() == True

# Generated at 2022-06-13 02:13:01.838281
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class TestCLIMgr(CLIMgr):
        CLI="df"
    result=TestCLIMgr().is_available()
    if result is False:
        raise RuntimeError('Test failed for method is_available of class CLIMgr')

if __name__ == "__main__":
    test_CLIMgr_is_available()

# Generated at 2022-06-13 02:13:03.160708
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert(CLIMgr().is_available() == False)

test_CLIMgr_is_available()

# Generated at 2022-06-13 02:13:03.633589
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():

    assert False

# Generated at 2022-06-13 02:13:04.498450
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    pm = CLIMgr()
    assert not pm.is_available()


# Generated at 2022-06-13 02:13:11.038162
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # Test 1: create a temporary class inherited from LibMgr, with the required attribute LIB
    class TestLibMgr(LibMgr):
        LIB = "ctypes"

    mgr = TestLibMgr()
    assert mgr.is_available() == True
    
    # Test 2: create a temporary class inherited from LibMgr, with 'LIB' to an unused string
    class TestLibMgr(LibMgr):
        LIB = "does_not_exist"

    mgr = TestLibMgr()
    assert mgr.is_available() == False
    

# Generated at 2022-06-13 02:13:29.693106
# Unit test for constructor of class LibMgr
def test_LibMgr():

    lm = LibMgr()
    assert lm._lib is None
    assert isinstance(lm, PkgMgr)


# Generated at 2022-06-13 02:13:32.291441
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class CLIMgrTest(CLIMgr):
        CLI = "python"
    assert CLIMgrTest().is_available()


# Generated at 2022-06-13 02:13:33.711125
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
	cmd = CLIMgr()
	cmd.is_available()

# Generated at 2022-06-13 02:13:38.133723
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert ApkMgr().is_available()
    assert AptMgr().is_available()
    assert DnfMgr().is_available()
    assert EmergeMgr().is_available()
    assert PacmanMgr().is_available()
    assert RpmMgr().is_available()
    assert ZypperMgr().is_available()
    assert YumMgr().is_available()


# Generated at 2022-06-13 02:13:39.612584
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cli_mgr_object = CLIMgr()
    assert cli_mgr_object.is_available() == False

# Generated at 2022-06-13 02:13:43.406211
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    from ansible.module_utils.common._utils import get_all_subclasses
    for obj in get_all_subclasses(PkgMgr):
        if obj not in (CLIMgr, LibMgr):
            cls = obj()
            assert type(cls.is_available()) is bool

# Generated at 2022-06-13 02:13:51.182605
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # Initialization
    cli = CLIMgr()
    class CLIMgrMock(CLIMgr):
        CLI = 'no_such_command'
    cliMock = CLIMgrMock()

    # Mock for get_bin_path
    get_bin_path_old = get_bin_path
    def get_bin_path_mock(name):
        if name == 'test':
            return 'path_to_test'
        else:
            raise ValueError('fail')

    # Test
    get_bin_path = get_bin_path_mock
    cli.CLI = 'test'
    assert cli.is_available()
    assert cli._cli == 'path_to_test'
    assert not cliMock.is_available()

    # Reset
    get_bin_path

# Generated at 2022-06-13 02:13:55.648103
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    from ansible.module_utils.common._collections_compat import Mapping
    all_managers = get_all_pkg_managers()
    for name, class_ in all_managers.items():
        instance = class_()
        if instance.is_available():
            installed_packages = instance.list_installed()
            assert installed_packages is not None
            assert isinstance(installed_packages, list)
            assert len(installed_packages) >= 1


# Generated at 2022-06-13 02:14:01.200203
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class dummy_package_manager(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['package_foo', 'package_bar', 'package_cake']

        def get_package_details(self, package):
            return {'name': package, 'version': '1.0'}

    package_manager = dummy_package_manager()
    result = package_manager.get_packages()

# Generated at 2022-06-13 02:14:04.906014
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():

    class TestPkgMgr(PkgMgr):
        pass

    test_pkg_mgr = TestPkgMgr()
    test_pkg_mgr.list_installed()


# Generated at 2022-06-13 02:14:55.403716
# Unit test for constructor of class LibMgr
def test_LibMgr():
    pm = LibMgr()
    assert pm is not None


# Generated at 2022-06-13 02:14:56.178249
# Unit test for constructor of class LibMgr
def test_LibMgr():
    pass


# Generated at 2022-06-13 02:15:02.489395
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    package_details_map = {}

    class TestPkgMgr(PkgMgr):

        def __init__(self):
            self.packages = [1, 2, 3]

        def is_available(self):
            return True

        def list_installed(self):
            return self.packages

        def get_package_details(self, package):
            return package_details_map[package]

    test_pkg_mgr = TestPkgMgr()

    expected_packages = {
        'first_package': [1, 42],
        'second_package': [3]
    }


# Generated at 2022-06-13 02:15:04.355313
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pkgmgr = CLIMgr("CLIMgr")
    assert pkgmgr.is_available()


# Generated at 2022-06-13 02:15:04.875438
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pass



# Generated at 2022-06-13 02:15:12.993013
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():

    pkg_managers = [pkg_mgr.__name__.lower() for pkg_mgr in get_all_pkg_managers().values()]
    assert 'aptmgr' in pkg_managers
    assert 'pacmanmgr' in pkg_managers
    assert 'pipmgr' in pkg_managers
    assert 'rpmmgr' in pkg_managers
    assert 'zyppermgr' in pkg_managers
    assert 'portage' in pkg_managers
    assert 'pkginmgr' in pkg_managers
    assert 'bundlemgr' in pkg_managers
    assert 'npm' in pkg_managers



# Generated at 2022-06-13 02:15:14.004115
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    assert LibMgr().is_available() == False


# Generated at 2022-06-13 02:15:16.096438
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    pkg_mgr = CLIMgr()
    assert pkg_mgr.is_available() is False

# Generated at 2022-06-13 02:15:19.826596
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.common._utils import get_all_subclasses
    pkg_mgrs = get_all_subclasses(CLIMgr)
    for pkg_mgr in pkg_mgrs:
        pm_ins = pkg_mgr()
        assert pm_ins.is_available()

# Generated at 2022-06-13 02:15:20.705446
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pass



# Generated at 2022-06-13 02:16:44.507522
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    test_instance = LibMgr()
    test_instance.LIB = 'os'
    assert test_instance.is_available()


# Generated at 2022-06-13 02:16:45.033804
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pass


# Generated at 2022-06-13 02:16:46.730516
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.facts import package_facts
    lib_mgr = get_all_pkg_managers()[package_facts.PackageFacts.get_distribution().lower()]
    print(lib_mgr.is_available())


# Generated at 2022-06-13 02:16:48.343760
# Unit test for constructor of class LibMgr
def test_LibMgr():
    # test libmgr constructor
    libmgr = LibMgr()
    libmgr._lib = "libname"
    assert libmgr._lib == "libname"

# Generated at 2022-06-13 02:16:49.312067
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    climgr = CLIMgr()
    assert climgr is not None

# Generated at 2022-06-13 02:16:51.933632
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():

    print(get_all_pkg_managers())
    assert len(get_all_pkg_managers()) == 6

# Generated at 2022-06-13 02:16:54.021627
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.packaging import PkgMgr
    pkg_mgr = PkgMgr
    assert pkg_mgr.is_available() == True

# Generated at 2022-06-13 02:16:54.878231
# Unit test for constructor of class LibMgr
def test_LibMgr():
    x = LibMgr()
    assert not x.is_available()


# Generated at 2022-06-13 02:16:58.577194
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    '''
    Unittest for PkgMgr.get_packages
    '''
    p = PkgMgr()
    packages = p.get_packages()
    assert False

# Generated at 2022-06-13 02:16:59.854281
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    libmgr = LibMgr()
    assert libmgr.is_available() == True
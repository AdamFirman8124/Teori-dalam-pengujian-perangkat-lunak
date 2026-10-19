

# Generated at 2022-06-13 02:09:24.806654
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    import sys

    class PkgMgrTest(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return [{'name': 'ansible', 'version': '1.2.3'},
                    {'name': 'ansible', 'version': '1.2.4'},
                    {'name': 'ansible', 'version': '1.2.1'},
                    {'name': 'python', 'version': '3.4.0'}]

        def get_package_details(self, package):
            return package

    mgr = PkgMgrTest()
    packages = mgr.get_packages()

    python = packages.get('python')
    assert len(python) == 1

# Generated at 2022-06-13 02:09:26.408265
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pkgmgr = PkgMgr()
    pkgmgr.list_installed()
    pass


# Generated at 2022-06-13 02:09:29.463525
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

    # Create CLIMgr class instance
    instance = CLIMgr()
    # cli should be None
    assert instance._cli is None
    # CLIMgr is a subclass of PkgMgr
    assert isinstance(instance, PkgMgr)


# Generated at 2022-06-13 02:09:34.810318
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    t_cli1 = CLIMgr()
    t_cli2 = CLIMgr()

    class TestCLIMgr(CLIMgr):

        CLI = 'testexe'

    t_cli3 = TestCLIMgr()

    assert t_cli1.is_available() is False
    assert t_cli2.is_available() is False
    assert t_cli3.is_available() is True



# Generated at 2022-06-13 02:09:35.660564
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert LibMgr().LIB == None


# Generated at 2022-06-13 02:09:40.440751
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    installed_packages = PkgMgr.get_packages()
    for package in installed_packages:
        assert isinstance(installed_packages[package], list)
        for versions in installed_packages[package]:
            assert isinstance(versions, dict)


# Generated at 2022-06-13 02:09:42.223322
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    class TestClass(PkgMgr):
        pass
    assert TestClass().is_available() == False


# Generated at 2022-06-13 02:09:46.231728
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.facts import ansible_software_facts
    lib_classes = ansible_software_facts.get_facts(LibMgr)
    for lib_class in lib_classes.keys():
        lib_mgr = lib_classes[lib_class]()
        lib_mgr.is_available()


# Generated at 2022-06-13 02:09:56.518532
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class TestPkgMgr(PkgMgr):
        def list_installed(self):
            return ['package1', 'package2', 'package3']

        def get_package_details(self, package):
            return {'name': package, 'version': '1.0.0'}

    test_mgr = TestPkgMgr()
    packages = test_mgr.get_packages()

# Generated at 2022-06-13 02:10:06.530499
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    import pytest
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgr, LibMgr

    class FakePkgMgr(PkgMgr):
        def is_available(self):
            return True

        @abstractmethod
        def list_installed(self):
            return [None]


    fake_pkg_mgr = FakePkgMgr()

    with pytest.raises(TypeError):
        fake_pkg_mgr.get_package_details(None)

    class FakeLibMgr(LibMgr):
        def is_available(self):
            return True

        @abstractmethod
        def list_installed(self):
            return [None]


    fake_lib_mgr = FakeLibMgr()


# Generated at 2022-06-13 02:10:12.634772
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class Lmgr(LibMgr):
        LIB = 'os'

    assert Lmgr().is_available()
    class Lmgr(LibMgr):
        LIB = '_asd'

    assert not Lmgr().is_available()


# Generated at 2022-06-13 02:10:13.599590
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert isinstance(CLIMgr(),CLIMgr)

# Generated at 2022-06-13 02:10:16.423072
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pkgMgr = CLIMgr()
    pkgMgr._cli = "/bin/yum"
    assert pkgMgr.is_available() == True


# Generated at 2022-06-13 02:10:17.959881
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    assert(PkgMgr.is_available() == False)


# Generated at 2022-06-13 02:10:18.580182
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pass

# Generated at 2022-06-13 02:10:25.862159
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class TestClass1(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ['pkg1-1.0', 'pkg2-2.0']
        def get_package_details(self, package):
            if package == 'pkg1-1.0':
                return {'name': 'pkg1', 'version': '1.0'}
            else:
                return {'name': 'pkg2', 'version': '2.0'}
    test_class1 = TestClass1()
    result = test_class1.get_packages()

# Generated at 2022-06-13 02:10:27.628284
# Unit test for constructor of class LibMgr
def test_LibMgr():
    x = LibMgr()
    if x is None:
        assert False
    else:
        assert True


# Generated at 2022-06-13 02:10:31.499828
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class TestCLIMgr(CLIMgr):
        CLI = "awscli"
    obj = TestCLIMgr()
    assert obj.is_available() == True

# Generated at 2022-06-13 02:10:32.844893
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert CLIMgr().is_available() == False



# Generated at 2022-06-13 02:10:41.222180
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class Mgr(LibMgr):
        LIB = "test_LibMgr_is_available"

    mgr = Mgr()
    if hasattr(mgr, "_lib"):
        del mgr._lib
    try:
        __import__("test_LibMgr_is_available")
    except ImportError:
        pass
    assert mgr.is_available()
    assert mgr._lib.__name__ == "test_LibMgr_is_available"
    del sys.modules["test_LibMgr_is_available"]
    assert not mgr.is_available()
    assert mgr._lib is None


# Generated at 2022-06-13 02:10:46.697473
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    libmgr = LibMgr()
    assert libmgr.is_available() == False



# Generated at 2022-06-13 02:10:48.789930
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class TestLibMgr(LibMgr):
        LIB = 'json'
    lib = TestLibMgr()
    assert lib.is_available() is True


# Generated at 2022-06-13 02:10:54.333098
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class TestLibMgr(LibMgr):
        def is_available(self):
            pass
    libmgr = TestLibMgr()
    assert libmgr.LIB is None
    assert libmgr._lib is None
    assert libmgr.is_available() is None


# Generated at 2022-06-13 02:10:59.674714
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    """
        test_PkgMgr_is_available() will unit test the method is_available() of the class PkgMgr

        :param: None
        :return: None
        :rtype: None
        """

    pkgmgr_obj = PkgMgr()
    assert not pkgmgr_obj.is_available()


# Generated at 2022-06-13 02:11:05.520720
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    print("Testing the method is_available of class LibMgr")
    pm_class = LibMgr()
    pm_class.LIB = 'pyfakefs'
    pm_class.is_available()
    assert pm_class._lib is not None
    pm_class.LIB = 'python_unavailable_library'
    assert pm_class.is_available() == False


# Generated at 2022-06-13 02:11:14.787446
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import sys
    py2_modules = ('sqlite3', 'time', 're', 'hashlib', 'json', 'base64', 'powerline', 'powerline.lib', 'powerline.lib.threaded')
    py3_modules = ('sqlite3', 'time', 'time', 're', 'hashlib', 'json', 'base64', 'powerline', 'powerline', 'powerline.lib', 'powerline.lib.threaded')
    if sys.version[0] == '2':
        modules = py2_modules
    else:
        modules = py3_modules
    for module in modules:
        lm = LibMgr()
        lm.LIB = module
        is_available = lm.is_available()

# Generated at 2022-06-13 02:11:16.627402
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pm = get_all_pkg_managers()
    for name in pm:
        assert isinstance(pm[name]().get_packages(), dict)

# Generated at 2022-06-13 02:11:17.586823
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pass



# Generated at 2022-06-13 02:11:26.735405
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    try:
        from mock import MagicMock
        cliMgr = CLIMgr()
        cliMgr.is_available = MagicMock(return_value=True)
        cliMgr.list_installed = MagicMock(return_value=["a","b"])
        cliMgr.get_package_details = MagicMock(return_value={'name': 'a'})
        result = cliMgr.get_packages()
        assert result == {"a" : [{'name': 'a','source': 'climgr'}, {'name': 'a','source': 'climgr'}]}
    except ImportError:
        # Python2
        pass

# Generated at 2022-06-13 02:11:28.496521
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lib_class = LibMgr()
    assert lib_class.LIB == None
    assert lib_class._lib == None


# Generated at 2022-06-13 02:11:40.053769
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():

    pkg_mgrs = get_all_pkg_managers()
    assert 'dnf' in pkg_mgrs
    assert 'pip' in pkg_mgrs
    assert 'rpm' in pkg_mgrs
    assert 'yum' in pkg_mgrs

# Generated at 2022-06-13 02:11:46.059071
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # create a PkgMgr object
    dummy = PkgMgr()

    # create a fake list of installed packages
    installed_packages = ['dummyPkg1']

    # check if it finds any installed packages
    if installed_packages == []:
        print("There are no installed packages on the system")
    else:
        print("Installed packages on the system:")
        for package in installed_packages:
            print(package)



# Generated at 2022-06-13 02:11:49.534124
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    class TestMgr(PkgMgr):
        def is_available(self):
            return False
        def list_installed(self):
            pass
        def get_package_details(self, package):
            pass

    t = TestMgr()
    t.is_available()

# Generated at 2022-06-13 02:11:50.782291
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert False, "No tests for PkgMgr implemented"


# Generated at 2022-06-13 02:11:53.136307
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    # Try to initialize a PkgMgr class.
    # This should raise a TypeError, since it is an abstract class.
    try:
        PkgMgr()
    except TypeError:
        pass


# Generated at 2022-06-13 02:11:55.526058
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # LibMgr.is_available(self):
    available = True
    try:
        try:
            import x11
        except ImportError:
            available = False
    except ImportError:
        pass
    assert available==False


# Generated at 2022-06-13 02:12:06.444736
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    
    import unittest
    

    class MyCLIMgr(CLIMgr):
        CLI = 'echo'

        def list_installed(self):
            pass

        def get_package_details(self, package):
            pass

    class My_CLIMgr_is_available_TestCase(unittest.TestCase):

        def test_CLIMgr_is_available_found(self):
            myCLIMgr = MyCLIMgr()
            self.assertTrue(myCLIMgr.is_available())

        def test_CLIMgr_is_available_not_found(self):
            class MyCLIMgr(CLIMgr):
                CLI = '__NONEXISTINGCMD__'

                def list_installed(self):
                    pass

                def get_package_details(self, package):
                    pass


# Generated at 2022-06-13 02:12:16.001002
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    # Workaround to be able to mock is_available()
    # See https://stackoverflow.com/a/18105557/548792
    # And https://stackoverflow.com/a/14113512/548792
    _is_available = PkgMgr.is_available
    def _is_available_for_mock(self):
        return False
    PkgMgr.is_available = _is_available_for_mock
    # Actual test
    from ansible.module_utils.common.systemd import Systemd
    from unittest import mock
    with mock.patch.object(PkgMgr, 'is_available', return_value=True):
        systemd = Systemd()
        assert systemd.has_journalctl


# Generated at 2022-06-13 02:12:17.957170
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert ('apt' in get_all_pkg_managers())
    assert ('yum' in get_all_pkg_managers())

# Generated at 2022-06-13 02:12:20.061522
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pkg_mgr = PkgMgr()
    output = pkg_mgr.is_available()
    assert(output == False)


# Generated at 2022-06-13 02:12:35.868022
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pass


# Generated at 2022-06-13 02:12:41.735451
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    # Create an instance of class PkgMgr
    pm = PkgMgr()

    # Check the return value of the get_package_details method
    details = pm.get_package_details('ansible')
    assert 'name' in details
    assert 'version' in details
    assert 'release' not in details
    assert 'arch' not in details


# Generated at 2022-06-13 02:12:42.650182
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert CLIMgr().is_available() == False

# Generated at 2022-06-13 02:12:46.033157
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    aa = PkgMgr()
    aa.list_installed = ('a1', 'a2')
    aa.get_package_details = lambda x: {'name': 'b', 'version': 'c'}
    assert {'b': [{'name': 'b', 'version': 'c', 'source': 'pkgmgr'}, {'name': 'b', 'version': 'c', 'source': 'pkgmgr'}]} == aa.get_packages()

# Generated at 2022-06-13 02:12:48.734574
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    test_class = LibMgr()
    try:
        assert test_class.is_available() == True
    finally:
        test_class = None


# Generated at 2022-06-13 02:12:52.705671
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    test_obj = LibMgr()
    test_obj.LIB = 'os'
    assert test_obj.is_available() is True

    test_obj.LIB = 'foo'
    assert test_obj.is_available() is False


# Generated at 2022-06-13 02:12:59.374283
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    def list_installed():
        return ['ansible']

    def get_package_details(package):
        return dict(name=package)

    def get_packages():
        installed_packages = {}
        for package in list_installed():
            package_details = get_package_details(package)
            if 'source' not in package_details:
                package_details['source'] = self.__class__.__name__.lower()
            name = package_details['name']
            if name not in installed_packages:
                installed_packages[name] = [package_details]
            else:
                installed_packages[name].append(package_details)
        return installed_packages

    class TestPkgMgr(PkgMgr):
        def is_available(self):
            pass

    test_cls = TestPkgMgr

# Generated at 2022-06-13 02:13:01.147938
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.facts.pkg_mgr import CLIMgr
    
    assert CLIMgr().is_available()
    

# Generated at 2022-06-13 02:13:02.772862
# Unit test for constructor of class LibMgr
def test_LibMgr():
    # test case: raw object
    with pytest.raises(NotImplementedError):
        LibMgr().is_available()


# Generated at 2022-06-13 02:13:03.692309
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cli = CLIMgr()
    assert cli._cli is None


# Generated at 2022-06-13 02:13:37.073536
# Unit test for constructor of class LibMgr
def test_LibMgr():
    test = LibMgr()

    assert test.LIB == None
    assert test._lib == None


# Generated at 2022-06-13 02:13:40.039921
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class PyPILibMgr(LibMgr):
        name = 'PyPI'
        LIB = 'pip'
    test = PyPILibMgr()
    assert(test.name == 'PyPI')
    assert(test.is_available() == False)


# Generated at 2022-06-13 02:13:42.688369
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    from ansible.module_utils.common.process import get_bin_path

    fp = CLIMgr()
    fp.CLI = 'python'
    assert fp.is_available() == True

# Generated at 2022-06-13 02:13:49.069825
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    # A class that inherits from CLIMgr
    class TestCLI(CLIMgr):
        CLI = "test_cli"
    # Creating an object, CLI will be None
    test_obj = TestCLI()
    assert test_obj._cli == None
    # Calling is_available function, it will return False as cli 'test_cli' is not available
    assert test_obj.is_available() == False
    # Creating another object, CLI is set to 'uname'
    test_obj_1 = TestCLI()
    # Calling is_available function, it will return True as cli 'uname' is available
    assert test_obj_1.is_available() != False

# Generated at 2022-06-13 02:13:56.317251
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    from ansible.module_utils._text import to_text
    import platform

    def _get_is_available(pkg_mgr):
        pkg_mgr_obj = pkg_mgr()
        supported = False
        if pkg_mgr_obj.is_available():
            supported = True
        pkg_mgr_obj = None
        return supported

    python_lib_name = 'json'
    python_lib_name_windows = 'wmi'

    # Create pkg mgr class for the python library that is always available
    class TestLibMgr(LibMgr):
        LIB = python_lib_name
    supported = _get_is_available(TestLibMgr)


# Generated at 2022-06-13 02:14:02.886911
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.common.collections import ImmutableDict
    import os
    import tempfile

# Generated at 2022-06-13 02:14:09.811944
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            pass

        def list_installed(self):
            pass

        def get_package_details(self, package):
            return {'name' : 'test_package', 'version' : '1.0.0.0'}

    pkg_mgr_obj = TestPkgMgr()
    assert pkg_mgr_obj.get_package_details('dummy_package') == {'name' : 'test_package', 'version' : '1.0.0.0'}

# Generated at 2022-06-13 02:14:15.269213
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    from ansible.module_utils.common.process import get_bin_path

    try:
        assert(PkgMgr().is_available() is False)
    except NotImplementedError:
        pass
    try:
        assert(LibMgr().is_available() is False)
    except NotImplementedError:
        pass
    try:
        assert(CLIMgr().is_available() is False)
    except NotImplementedError:
        pass


# Generated at 2022-06-13 02:14:17.927725
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    mgr = PkgMgr()
    assert mgr.is_available() == NotImplementedError


# Generated at 2022-06-13 02:14:27.336665
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # Setup
    class TestCLIMgr(CLIMgr):
        CLI = 'test_binary'
    test_package_manager = TestCLIMgr()

    # Test if binary is found
    get_bin_path_orig = get_bin_path
    get_bin_path_mock = lambda a: '/usr/bin/test_binary'
    get_bin_path = get_bin_path_mock
    assert test_package_manager.is_available()
    get_bin_path = get_bin_path_orig

    # Test if binary is not found
    get_bin_path_orig = get_bin_path
    get_bin_path_mock = lambda a: None
    get_bin_path = get_bin_path_mock
    assert not test_package_manager.is_available()
    get

# Generated at 2022-06-13 02:15:41.903490
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    foo = CLIMgr()
    assert foo == foo


# Generated at 2022-06-13 02:15:42.260282
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pass

# Generated at 2022-06-13 02:15:44.585799
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class CLIMgrDummy(CLIMgr):
        CLI = 'no_such_command'
    assert not CLIMgrDummy().is_available()
    class CLIMgrForTest(CLIMgr):
        CLI = 'python3'
    assert CLIMgrForTest().is_available()


# Generated at 2022-06-13 02:15:47.864019
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    class TestMgr(LibMgr):
        pass
    # clean up namespace for this test...
    if list(globals().keys()).count('TestMgr') > 0:
        del globals()['TestMgr']
    assert get_all_pkg_managers() == {}
    globals()['TestMgr'] = TestMgr
    assert get_all_pkg_managers() == {'testmgr': TestMgr}

# Generated at 2022-06-13 02:15:57.645846
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lib = LibMgr()
    lib.LIB = 'ansible.module_utils.software.lib.pip'
    assert lib.is_available()
    lib.LIB = 'ansible.module_utils.software.lib.yum'
    assert lib.is_available()
    lib.LIB = 'ansible.module_utils.software.lib.apt'
    assert lib.is_available()
    lib.LIB = 'ansible.module_utils.software.lib.pip'
    assert lib.is_available()
    lib.LIB = 'ansible.module_utils.software.lib.snap'
    assert lib.is_available()
    lib.LIB = 'ansible.module_utils.software.lib.zz.lib'
    assert not lib.is_available()


# Generated at 2022-06-13 02:16:05.677948
# Unit test for method get_packages of class PkgMgr

# Generated at 2022-06-13 02:16:07.576118
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.pkg_resources import PackageManager

    pkg_mgr = PackageManager()
    pkg_mgr.get_packages()

# Generated at 2022-06-13 02:16:10.316031
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    libmgr = LibMgr()
    assert libmgr.is_available() == False, "The is_available method of class LibMgr should return False if no library has been set"


# Generated at 2022-06-13 02:16:11.116736
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    p = PkgMgr()
    assert False

# Generated at 2022-06-13 02:16:17.155603
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.facts.package_manager import CLIMgr
    class FedoraMgr(CLIMgr):
        CLI = 'dnf'
    f = FedoraMgr()
    assert f.is_available()
    class DebianMgr(CLIMgr):
        CLI = 'apt-get'
    d = DebianMgr()
    assert d.is_available()

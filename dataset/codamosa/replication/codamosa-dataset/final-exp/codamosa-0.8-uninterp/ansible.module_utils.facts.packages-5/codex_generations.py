

# Generated at 2022-06-13 02:09:15.461860
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert True

# Generated at 2022-06-13 02:09:21.592327
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    """Test for method get_package_details of class PkgMgr."""

    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True

        def get_package_details(self, package):
            return {}
        def list_installed(self):
            return [package]

    testmgr = TestPkgMgr()
    package = "foo"
    source = "Base"
    testmgr.get_package_details(package)
    assert source != testmgr.get_package_details(package)["source"], "Source is 'Base' but should be 'TestPkgMgr'."

# Generated at 2022-06-13 02:09:25.819861
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

    cli = CLIMgr()
    cli.CLI = 'ansible-test-package-manager'
    try:
        # This should fail and raise
        cli.is_available()
        assert(False)
    except ValueError:
        # This is the expected result
        assert(True)

# Generated at 2022-06-13 02:09:26.721457
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert PkgMgr.list_installed() is not None

# Generated at 2022-06-13 02:09:36.123340
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch, MagicMock
    mock_get_bin_path = MagicMock()
    # check if the package is present
    mock_get_bin_path.return_value = "fake_path"
    with patch("ansible_collections.ansible.community.tests.unit.modules.clients.package.package_api.CLIMgr.get_bin_path", mock_get_bin_path):
        pkg_mgr = CLIMgr()
        result = pkg_mgr.is_available()
        assert result
    # check if the package is not present
    mock_get_bin_path.side_effect = ValueError

# Generated at 2022-06-13 02:09:37.713377
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    mgr = CLIMgr()
    assert mgr._cli == None



# Generated at 2022-06-13 02:09:47.576218
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import mock
    import os

    my_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    sys.path.append(my_dir)
    import lib.pkg_mgr.yum

    my_class = lib.pkg_mgr.yum.YumMgr()
    my_class.list_installed = mock.MagicMock()
    my_class.list_installed.return_value = ['vim-common', 'vim-enhanced']
    my_class.get_package_details = mock.MagicMock()
    my_class.get_package_details.return_value = {'name': 'vim', 'version': '7.4.160'}


# Generated at 2022-06-13 02:09:51.608760
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

    import ansible.modules.system.package_mgr as package_mgr_module

    yum_mgr = package_mgr_module.Yum()
    assert isinstance(yum_mgr, CLIMgr)



# Generated at 2022-06-13 02:09:56.729350
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    my_pkg_mgr = CLIMgr()
    if hasattr(my_pkg_mgr, 'CLI'):
        my_pkg_mgr.CLI = "fake_cmd"
    assert my_pkg_mgr.is_available() == False
    my_pkg_mgr.CLI = "pwd"
    assert my_pkg_mgr.is_available() == True

# Generated at 2022-06-13 02:10:06.695132
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pkgmgr_test = PkgMgr()
    # Create a fake package manager tester.
    class PkgMgrTest(PkgMgr):
        def list_installed(self):
            return ["pkg1", "pkg2", "pkg3"]

        def get_package_details(self, package):
            return {
                "name": package,
                "version": "1.0"
            }

    # Test the method get_packages.
    assert pkgmgr_test.get_packages() == dict()
    # Test the method get_packages in the fake package manager tester.

# Generated at 2022-06-13 02:10:21.351218
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import platform
    import os

    # Set the os name to a known supported one
    os.name = 'posix'

    # Set the platform to a known supported one
    platform.platform = lambda: 'Darwin-13.4.0-x86_64-i386-64bit'

    # Create a class that extends LibMgr
    class foo(LibMgr):
        LIB = 'platform'

    # Create an instance of the class
    f = foo()

    # Verify that it reports is_available as True
    assert f.is_available()

    # Change the platform to a non supported one
    platform.platform = lambda: 'Linux-3.0.0-16-generic-i686-with-debian-squeeze-sid'

    # Create an instance of the class
    f = foo()

    # Verify that it reports

# Generated at 2022-06-13 02:10:23.976028
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    for obj in get_all_subclasses(PkgMgr):
        assert callable(getattr(obj(), 'list_installed'))
        for package in obj().list_installed():
            assert package

# Generated at 2022-06-13 02:10:26.512977
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class DummyLib(LibMgr):
        LIB = 'some_dummy_lib'
    assert DummyLib().is_available() == False


# Generated at 2022-06-13 02:10:29.446451
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    from ansible.module_utils.packaging.package import PkgMgr

    pkg_mgr_obj = PkgMgr()
    result = pkg_mgr_obj.get_package_details('dummy-package')

    assert result == {}


# Generated at 2022-06-13 02:10:32.845420
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class PkgMgrSub(LibMgr):
        pass
    assert PkgMgrSub().is_available() == False


# Generated at 2022-06-13 02:10:34.973020
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():

    assert get_all_pkg_managers()['apt'].list_installed() != []


# Generated at 2022-06-13 02:10:38.236593
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class test_LibMgr(LibMgr):
        LIB = "ansible.module_utils.facts.hardware"
    mgr = test_LibMgr()
    assert mgr.is_available() is True



# Generated at 2022-06-13 02:10:44.459595
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class MockLibMgr(LibMgr):
        LIB = 'mylib'

    obj = MockLibMgr()
    __builtins__.__import__ = lambda name: name if name != 'mylib' else None
    assert not obj.is_available()

    obj = MockLibMgr()
    __builtins__.__import__ = lambda name: name
    assert obj.is_available()


# Generated at 2022-06-13 02:10:52.997747
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class MockPkgMgr(PkgMgr):

        def __init__(self, pkg_name, pkgs):
            self.pkg_name = pkg_name
            self.pkgs = pkgs
            self.is_available = lambda: True
            super(MockPkgMgr, self).__init__()

        def get_package_details(self, package):
            return {'name': self.pkg_name, 'version': package}

        def list_installed(self):
            return self.pkgs

    # Ensure that the 'pkg_type_name' is returned for each package
    pkg_mgr = MockPkgMgr('test_pkg', ['1', '2'])

# Generated at 2022-06-13 02:10:55.364694
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lm_obj = LibMgr()
    assert lm_obj is not None

# Generated at 2022-06-13 02:11:07.410254
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    ''' Its a unit test function '''
    def is_available(self):
        ''' Its a stub function '''
        return True
    obj = PkgMgr()
    obj.is_available = is_available
    assert obj.is_available() == True


# Generated at 2022-06-13 02:11:11.362545
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class TestLibMgr(LibMgr):
        LIB = 'testlib'
        def list_installed(self):
            return ['testlib']
        def get_package_details(self, package):
            return {'name': 'testlib'}
    obj = TestLibMgr()
    assert obj.is_available()


# Generated at 2022-06-13 02:11:13.754739
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    mock_data = {'installed_packages': {}}
    assert PkgMgr().list_installed() == mock_data['installed_packages']


# Generated at 2022-06-13 02:11:15.450806
# Unit test for constructor of class LibMgr
def test_LibMgr():
    libmgr = LibMgr()
    assert libmgr is not None, "Failed to instantiate LibMgr"


# Generated at 2022-06-13 02:11:19.399610
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class TestPkgMgr(PkgMgr):
        def list_installed(self):
            return []
        def get_package_details(self, package):
            return {}
    pkg_mgr = TestPkgMgr()
    assert list == type(pkg_mgr.list_installed())


# Generated at 2022-06-13 02:11:27.283517
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class PkgMgrChild(PkgMgr):
        def list_installed(self):
            pass
        def get_package_details(self, package):
            pass
    p = PkgMgrChild()
    package = {"name": "test-package", "version": "1.1"}
    package_dict = p.get_package_details(package)
    assert(package_dict["name"] == "test-package")
    assert(package_dict["version"] == "1.1")
    assert(package_dict["source"] == "pkgmgrchild")
    assert(len(package_dict) == 3)

# Generated at 2022-06-13 02:11:29.044518
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    climgr = CLIMgr()
    assert not climgr.is_available()
    assert not hasattr(climgr, "_cli")

# Generated at 2022-06-13 02:11:30.213295
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
 
    pkg = PkgMgr()
    res = pkg.is_available()
    
    assert isinstance(res, object)

# Generated at 2022-06-13 02:11:35.746741
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    all_pkg_managers = get_all_pkg_managers()
    for pkg_mgr, pkg_mgr_class in all_pkg_managers.items():
        if not pkg_mgr_class().is_available():
            continue

        for package in pkg_mgr_class().list_installed():
            pkg_mgr_class().get_package_details(package)

# Generated at 2022-06-13 02:11:39.810501
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    obj = PkgMgr()
    try:
        result = obj.get_package_details(None)
    except NotImplementedError as e:
        if str(e) == "Must override method __init__ in a subclass":
            return
    assert False


# Generated at 2022-06-13 02:11:57.780996
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    mgr = CLIMgr()
    assert mgr is not None

# Generated at 2022-06-13 02:12:04.333919
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import collections
    import types

    class TestCLIMgr(CLIMgr):
        CLI = 'python3'

    obj = TestCLIMgr()
    assert isinstance(obj, collections.Callable)
    assert isinstance(obj, types.FunctionType)
    assert isinstance(obj, types.MethodType)
    assert isinstance(obj, object)


# Generated at 2022-06-13 02:12:05.631250
# Unit test for constructor of class LibMgr
def test_LibMgr():
    x = LibMgr()
    assert x._lib == None

# Generated at 2022-06-13 02:12:15.124330
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():

    result0 = []
    result1 = []
    result2 = []
    result3 = []

    try:
        result0 = get_all_pkg_managers()['dpkg']().list_installed()
        result1 = get_all_pkg_managers()['freebsd_pkg']().list_installed()
        result2 = get_all_pkg_managers()['pacman']().list_installed()
        result3 = get_all_pkg_managers()['pip']().list_installed()

    except Exception:
        pass
    assert isinstance(result0, list)
    assert isinstance(result1, list)
    assert isinstance(result2, list)
    assert isinstance(result3, list)


# Generated at 2022-06-13 02:12:18.352319
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class PkgMgr_list_installed(PkgMgr):
        pass
    pkgmgr = PkgMgr_list_installed()
    try:
        pkgmgr.list_installed()
    except NotImplementedError:
        pass


# Generated at 2022-06-13 02:12:20.138843
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class C(CLIMgr):
        CLI = "ls"
    assert C().is_available() is True


# Generated at 2022-06-13 02:12:26.604291
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # Mock a PkgMgr subclass instance and test the get_packages method
    class PkgMgrImpl(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ['a', 'b', 'c', 'd', 'e']
        def get_package_details(self, package):
            return {'name': 'pkg' + package, 'version': package + '_version'}

    pkg_mgr_impl = PkgMgrImpl()
    result = pkg_mgr_impl.get_packages()

# Generated at 2022-06-13 02:12:28.642768
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.common.guest_libs import python
    assert python.is_available() == True


# Generated at 2022-06-13 02:12:30.316745
# Unit test for constructor of class LibMgr
def test_LibMgr():

    assert LibMgr().__init__() == None

# Generated at 2022-06-13 02:12:38.438661
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class TestCLIMgr(CLIMgr):
        CLI = 'test'
    # Mock 'get_bin_path' function
    def get_bin_path(binary_name):
        if binary_name == TestCLIMgr.CLI:
            raise ValueError
        return '/usr/bin/' + binary_name

    pkg_mgr = TestCLIMgr()
    # Pass a mocked get_bin_path function to the object 'pkg_mgr'
    pkg_mgr.__class__.get_bin_path = get_bin_path
    assert pkg_mgr.is_available() == False
    pkg_mgr.CLI = 'ls'
    assert pkg_mgr.is_available() == True

# Generated at 2022-06-13 02:13:16.559717
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    PM = PkgMgr()
    ans = PM.get_package_details("package")
    assert ans is None


# Generated at 2022-06-13 02:13:20.356664
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import kinds.pacman as pacman
    libmgr = pacman.LibMgr()
    assert libmgr.is_available() == False
    from six.moves import reload_module
    reload_module(pacman)
    assert libmgr.is_available() == True


# Generated at 2022-06-13 02:13:26.462082
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    # Not sure if this is the correct method of testing??
    # If this module is imported, all subclasses of class pkgMgr
    # are imported as well. Why test that?
    # This test is an attempt to verify that the constructor of
    # class CLIMgr works as expected.
    #
    # Create a subclass of CLIMgr
    class TestCLI(CLIMgr):
        CLI = 'some_cli'
    # Instantiate a TestCLI object
    assert TestCLI().CLI == 'some_cli'

# Generated at 2022-06-13 02:13:28.653906
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    pkgs = get_all_pkg_managers()
    for obj in pkgs:
        pkgs[obj]().is_available()


# Generated at 2022-06-13 02:13:31.124756
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    """
    This checks if list_installed is properly defined.
    """
    assert not list(PkgMgr.list_installed(PkgMgr()))
    assert PkgMgr.list_installed(PkgMgr()) == None


# Generated at 2022-06-13 02:13:34.009334
# Unit test for constructor of class LibMgr
def test_LibMgr():
    '''
    Test for constructor of class LibMgr
    '''
    lm = LibMgr()
    assert lm._lib is None
    assert lm.LIB is None


# Generated at 2022-06-13 02:13:37.464223
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    pkg_managers = get_all_pkg_managers()
    assert isinstance(pkg_managers, dict)
    for pkg_mgr in ('apt', 'homebrew', 'yum', 'zypper', 'dnf'):
        assert pkg_mgr in pkg_managers

# Generated at 2022-06-13 02:13:41.470874
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pkgmgrs_to_test = get_all_pkg_managers()
    for cls_name, cls in pkgmgrs_to_test.items():
        p = cls()
        is_available = p.is_available()

        if not isinstance(is_available, bool):
            raise TypeError("the method '%s.is_available' must return a boolean value" % cls_name)


# Generated at 2022-06-13 02:13:44.385235
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class LibMgrTest(LibMgr):
        LIB = 'ansible.module_utils.facts.system.packages.lib2'

    x = LibMgrTest()
    assert x.is_available()


# Generated at 2022-06-13 02:13:47.834224
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    # Assert that this method is abstract
    try:
        test_obj = PkgMgr()
        test_obj.is_available()
    except TypeError:
        test_result = True
    except Exception:
        test_result = False
    assert test_result == True, "PkgMgr is_available method test failed"


# Generated at 2022-06-13 02:15:16.303552
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    PkgMgr_obj = PkgMgr()
    PkgMgr_obj.list_installed = lambda: ["pam", "audit", "libsss_idmap"]
    PkgMgr_obj.get_package_details = lambda x: {'name': x, 'version': None, 'arch': None, 'source': None}

# Generated at 2022-06-13 02:15:21.271036
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import PkgMgr_test_class
    pm = PkgMgr_test_class.PkgMgr_test_class()
    installed_packages = pm.get_packages()
    assert installed_packages == {'a': [{'name': 'a', 'version': '1.0'}, {'name': 'a', 'version': '2.0'}], 'b': [{'name': 'b', 'version': '1.0'}]}

# Generated at 2022-06-13 02:15:26.992598
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.pkginstaller.common._utils import CLIMgr
    import os
    cm = CLIMgr()
    cm.CLI = 'fasd'
    assert cm.is_available() == True
    cm.CLI = 'fasd_to_be_delelted_for_test'
    assert cm.is_available() == False
    os.system("touch fasd_to_be_delelted_for_test")
    assert cm.is_available() == True
    os.system("rm -f fasd_to_be_delelted_for_test")

# Generated at 2022-06-13 02:15:29.426765
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert LibMgr().__class__.__name__ == 'LibMgr'


# Generated at 2022-06-13 02:15:32.512208
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class SomeClass(CLIMgr):
        CLI = 'ls'
    obj = SomeClass()
    assert obj._cli is None
    assert obj

if __name__ == '__main__':
    test_CLIMgr()

# Generated at 2022-06-13 02:15:39.383547
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class PkgMgr_check(PkgMgr):
        def list_installed(self):
            return ['abc', 'xyz']
        def get_package_details(self, package):
            return {'name': package, 'version': '1.0.0'}
    a = PkgMgr_check()
    assert a.get_packages() == {'abc': [{'source': 'pkgmgr_check', 'name': 'abc', 'version': '1.0.0'}], 'xyz': [{'source': 'pkgmgr_check', 'name': 'xyz', 'version': '1.0.0'}]}

# Generated at 2022-06-13 02:15:43.221724
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    try:
        class PkgMgr_list_installed(PkgMgr):
            def is_available(self):
                return True

            def get_package_details(self, package):
                return {}
    except (TypeError, NameError):
        raise
    try:
        instance = PkgMgr_list_installed()
        instance.list_installed()
    except (NotImplementedError, AttributeError):
        pass

# Generated at 2022-06-13 02:15:47.264679
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.common.collections import ImmutableDict
    import tempfile
    testfilepath = tempfile.mkstemp()[1]
    test_cli = CLIMgr()
    test_cli.CLI = testfilepath
    assert test_cli.is_available() == False
    with open(testfilepath, 'w') as testfile:
        testfile.write('write to a file')
    assert test_cli.is_available() == True


# Generated at 2022-06-13 02:15:57.569356
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    try:
        from pkg_resources import parse_version
        from distutils.version import LooseVersion
        from ansible.module_utils.common._collections_compat import MutableMapping
    except ImportError:
        return False

    lm = LibMgr()
    assert getattr(lm, '_lib', None) is None
    assert lm.is_available() is False
    assert getattr(lm, '_lib', None) is None

    lm.LIB = 'pkg_resources'
    assert lm.is_available() is True
    assert isinstance(lm._lib, MutableMapping)
    assert lm._lib.parse_version == parse_version
    assert lm._lib.LooseVersion == LooseVersion

    lm.LIB = 'distutils.version'
    assert l

# Generated at 2022-06-13 02:16:03.757428
# Unit test for constructor of class LibMgr
def test_LibMgr():
    # test class LibMgr - setting name to the name of class LibMgr
    LibMgr.LIB = 'LibMgr'
    # test with non existing class name
    LibMgr.LIB = 'not_existing_class'
    test_LibMgr = LibMgr()
    assert test_LibMgr.is_available() is False
    # test with existing class name
    LibMgr.LIB = 'LibMgr'
    test_LibMgr = LibMgr()
    assert test_LibMgr.is_available() is True

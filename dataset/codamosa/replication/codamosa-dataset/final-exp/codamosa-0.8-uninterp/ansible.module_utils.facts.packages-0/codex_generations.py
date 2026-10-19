

# Generated at 2022-06-13 02:09:17.444309
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pm = LibMgr()
    assert pm.is_available() is False


# Generated at 2022-06-13 02:09:21.058224
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class testMgr(CLIMgr):
        CLI = None

    obj = testMgr()
    assert obj._cli == None


# Generated at 2022-06-13 02:09:29.301515
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    all_pkgmgrs = get_all_pkg_managers()
    unseen_pkgs = [
        'apt', 'dnf', 'homebrew', 'portage', 'pip', 'pkgng', 'pkg5', 'ports', 'rpm', 'slackpkg',
        'slackpkgplus', 'yum', 'apk', 'zypper', 'pkg', 'portage_py', 'easy_install', 'emerge',
        '0install', 'guix', 'macports', 'pkgin', 'swupd', 'sw', 'xbps', 'xbps_python']
    assert set(all_pkgmgrs.keys()).issubset(set(unseen_pkgs))

# Generated at 2022-06-13 02:09:29.865383
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pass

# Generated at 2022-06-13 02:09:32.159432
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lm = LibMgr()
    assert lm.is_available() == False


# Generated at 2022-06-13 02:09:33.407937
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert(CLIMgr() is not None)


# Generated at 2022-06-13 02:09:35.395702
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class Apt(LibMgr):
        LIB = 'apt'
    assert not Apt().is_available()


# Generated at 2022-06-13 02:09:37.031898
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    c = CLIMgr()
    c.is_available()
    assert c.CLI == None
    assert c._cli is None



# Generated at 2022-06-13 02:09:39.676604
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pm = PkgMgr()
    assert pm.is_available() is False


# Generated at 2022-06-13 02:09:40.879586
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import platform
    python_version = platform.python_version()
    e = False
    if python_version == '2.7.12':
        e = True
    assert e

# Generated at 2022-06-13 02:09:46.806997
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    class TestMgr(PkgMgr):
        pass
    assert TestMgr().is_available() is False



# Generated at 2022-06-13 02:09:48.358279
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert PkgMgr.is_available() == NotImplementedError


# Generated at 2022-06-13 02:09:51.118555
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    c = CLIMgr()
    c.CLI = 'echo'
    assert c.is_available() == True 


# Generated at 2022-06-13 02:09:52.801379
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pkgm = CLIMgr()
    assert pkgm.is_available() == False


# Generated at 2022-06-13 02:09:53.692614
# Unit test for constructor of class LibMgr
def test_LibMgr():
    pass


# Generated at 2022-06-13 02:09:58.846374
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ['abc', 'def']
        def get_package_details(self, package):
            return {'name': package}
    expected_result = ['abc', 'def']
    pkgmgr = TestPkgMgr()
    actual_result = pkgmgr.list_installed()
    assert actual_result == expected_result


# Generated at 2022-06-13 02:10:00.291454
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    assert LibMgr().is_available() is False

# Generated at 2022-06-13 02:10:03.314826
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    package_list = ['python', 'python-dev', 'python-setuptools']
    assert PkgMgr.list_installed(CLIPkgMgr) == package_list


# Generated at 2022-06-13 02:10:04.278373
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert PkgMgr()


# Generated at 2022-06-13 02:10:11.411967
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    class _CLIMgr(CLIMgr):
        CLI = "test_cli"
        def list_installed(self):
            return ["bin"]

    managers = get_all_pkg_managers()
    managers["test"] = _CLIMgr

    # test if get_all_subclasses return class CLIMgr
    assert CLIMgr in get_all_subclasses(PkgMgr)

    # test if get_all_pkg_managers return a dictionary of class CLIMgr
    assert "test" in managers
    assert managers["test"] == _CLIMgr

    # test if CLIMgr.list_installed return the list of installed packages
    # which should contain "bin"
    assert "bin" in _CLIMgr().list_installed()

    # test if CLIMgr.is_available will return True because test_cli exists in

# Generated at 2022-06-13 02:10:27.282411
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['pkg1', 'pkg2']

        def get_package_details(self, package):
            return {'name': package, 'version': '1.0'}

    testPkgMgr = TestPkgMgr()
    assert testPkgMgr.get_packages() == {'pkg1': [{'version': '1.0', 'name': 'pkg1', 'source': 'testpkgmgr'}], 'pkg2': [{'version': '1.0', 'name': 'pkg2', 'source': 'testpkgmgr'}]}

# Generated at 2022-06-13 02:10:31.353939
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestLibMgr(LibMgr):
        LIB = 'foo'
    assert TestLibMgr()._lib is None
    assert TestLibMgr().is_available() is False


# Generated at 2022-06-13 02:10:41.539366
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    import pkg_resources
    import nose

    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return False
        def list_installed(self):
            return []

    test_package = {'name': 'test'}
    test_package_out = {'name': 'test', 'version': '1.0'}

    test_pm = TestPkgMgr()

    # Error when the package managers get_package_details is not implemented
    with nose.tools.assert_raises(NotImplementedError):
        test_pm.get_package_details(test_package)

    class TestPkgMgr2(TestPkgMgr):
        def get_package_details(self, package):
            return test_package_out

    test_pm = TestPkgMgr2

# Generated at 2022-06-13 02:10:43.638460
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert LibMgr().__init__() is None



# Generated at 2022-06-13 02:10:46.863308
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class FooMgr(LibMgr):
        LIB = 'package_list'

    foo_mgr = FooMgr()
    assert foo_mgr.is_available() is False


# Generated at 2022-06-13 02:10:54.300419
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import os
    import os.path
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    from lib.ansible.module_utils.facts.package import CLIMgr
    

    def mock_get_bin_path(bin_path):
        if bin_path == '/usr/bin/apt-get':
            return '/usr/bin/apt-get'

    base = CLIMgr()
    base.CLI = '/usr/bin/apt-get'

    #First test when the CLI is available
    base.get_bin_path = mock_get_bin_path
 
    assert(base.is_available() == True)

    #Test when the CLI

# Generated at 2022-06-13 02:10:55.315506
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert(CLIMgr().is_available == False)

# Generated at 2022-06-13 02:11:03.684691
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class FakePkgMgr(PkgMgr):
        # package need name and version
        def list_installed(self):
            return ["fakepackage"]

        def get_package_details(self, package):
            return {'name': 'fakepackage', 'version': "0.0.1"}

    pkgmgr = FakePkgMgr()
    packages = pkgmgr.get_packages().items()
    assert len(packages) == 1
    (name, versions) = packages[0]
    assert name == "fakepackage"
    assert len(versions) == 1
    assert versions[0] == {'name': 'fakepackage', 'version': "0.0.1", 'source': 'fakepkgmgr'}

# Generated at 2022-06-13 02:11:05.747058
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    try:
        get_bin_path('date')
    except ValueError:
        assert False
    assert True


# Generated at 2022-06-13 02:11:07.450554
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    assert CLIMgr().is_available() == False

# Generated at 2022-06-13 02:11:30.198019
# Unit test for method get_packages of class PkgMgr

# Generated at 2022-06-13 02:11:37.253727
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.six import PY3

    class TestMgr(CLIMgr):
        CLI = 'test-cli'

    testMgr = TestMgr()
    assert testMgr.is_available() == False

    if PY3:
        with get_exception() as cm:
            get_bin_path('test-cli')
    else:
        cm = None
    assert cm is not None
    assert cm.exception.args[0] == "test-cli could not be found"

# Generated at 2022-06-13 02:11:47.868013
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    try:
        from unittest.mock import patch, MagicMock
    except ImportError:
        from mock import patch, MagicMock

    mock_obj = MagicMock()
    mock_obj.list_installed.return_value = ['a', 'b']
    mock_obj.get_package_details.side_effect = [{'name': 'a', 'version': '1.0'}, {'name': 'b', 'version': '1.0'}]

    mock_pkg_mgr = MagicMock(spec=PkgMgr)
    mock_pkg_mgr.return_value = mock_obj

    with patch('ansible_collections.ansible.community.plugins.module_utils.facts.packaging.PkgMgr', mock_pkg_mgr):
        import ansible_collections.ans

# Generated at 2022-06-13 02:11:50.864991
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    # return False when CLI is not found
    class CLIMgr_sub(CLIMgr):
        CLI = None

    pkg = CLIMgr_sub()
    assert pkg.is_available() == False

    # return True when CLI is found
    class CLIMgr_sub(CLIMgr):
        CLI = 'rpm'

    pkg = CLIMgr_sub()
    assert pkg.is_available() == True

# Generated at 2022-06-13 02:11:52.091226
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class mylib(LibMgr):
        LIB='mylib'

    mylib()


# Generated at 2022-06-13 02:11:52.913367
# Unit test for constructor of class LibMgr
def test_LibMgr():
    libmgr = LibMgr()


# Generated at 2022-06-13 02:11:57.451178
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.facts import collector
    import shutil
    import os

    # Use get_bin_path to check whether the "ps" command is available
    assert collector.get_file_facts().get('ansible_os_family') == 'Linux'
    assert "ps" in get_bin_path("ps")

    # Create a dummy file to check whether the is_available method can find it
    temp_cli = "/tmp/ansible_temp_CLIMgr_is_available"
    open(temp_cli, "a").close()
    assert os.path.exists(temp_cli)

    obj = CLIMgr()
    obj.CLI = temp_cli

    # Check whether the is_available method can detect the dummy file


# Generated at 2022-06-13 02:12:03.598980
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class LibMgrTest(LibMgr):
        LIB = 'ansible_module_utils.packaging.package.platform'
    
    lib_mgr = LibMgrTest()
    assert lib_mgr.LIB == 'ansible_module_utils.packaging.package.platform'
    assert lib_mgr._lib == None
    

# Generated at 2022-06-13 02:12:13.950883
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.common.process import get_bin_path

    # For testing purposes, a class is derived from PkgMgr.
    # This class is not original code and is not supported.

    class TestPkgMgr(CLIMgr):

        CLI = 'yum'

        def list_installed(self):
            if self._cli is None:
                raise ValueError("yum command not found")
            items = []
            cmd_out = get_bin_path('yum') + ' list installed'
            rc, out, err = module.run_command(cmd_out, use_unsafe_shell=True)
            if rc == 0:
                for line in out.split('\n'):
                    items.append(line.split()[0])
            return items


# Generated at 2022-06-13 02:12:18.107673
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    class X(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ['package1-1.2.3-1']
        def get_package_details(self, package):
            return{'name': package, 'version': '1.2.3'}
    assert X().is_available()


# Generated at 2022-06-13 02:12:52.376840
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class NonExistentLibMgr(LibMgr):
        LIB = 'doesnotexist'

    class ExistingLibMgr(LibMgr):
        LIB = 'os'

    assert not NonExistentLibMgr().is_available()
    assert ExistingLibMgr().is_available()



# Generated at 2022-06-13 02:12:58.301642
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # Initialize a new instance of class CLIMgr
    class_instance = CLIMgr()

    # Try to import get_bin_path from module_utils.common.process to use it
    try:
        from ansible.module_utils.common.process import get_bin_path
    except ImportError:
        print("ansible.module_utils.common.process does not contain function get_bin_path")

    # Execute method is_available using get_bin_path which is supposed to return True
    result = class_instance.is_available()

    # Test if the function returns True
    assert (result == True)



# Generated at 2022-06-13 02:12:59.384985
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    assert PkgMgr.get_packages() == None


# Generated at 2022-06-13 02:13:04.197758
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import os
    import tempfile

    class TestPkgMgr(PkgMgr):
        def __init__(self, path):
            self.path = path
            super(TestPkgMgr, self).__init__()

        def is_available(self):
            return True

        def list_installed(self):
            return os.listdir(self.path)

        def get_package_details(self, package):
            return {'name': package,
               'source': self.__class__.__name__,
                'version': {'current': '1.0.0',
                            'latest': '2.0.0'}}

    with tempfile.TemporaryDirectory() as tmpdir:
        tpm = TestPkgMgr(tmpdir)

# Generated at 2022-06-13 02:13:05.953104
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    # Override the abstract method with a concrete implementation here
    # In the unit test it should call the abstract method so at least
    # you know its available
    pass

# Generated at 2022-06-13 02:13:13.515983
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    my_tests = [
        ("DummyCommand", False),
        ("python", True)
    ]
    for my_test in my_tests:
        my_cli = CLIMgr()
        my_cli.CLI = my_test[0]
        my_result = my_cli.is_available()
        if my_test[1] == my_result:
            print("Unit test PASSED: my_test %s expected result %s and got result %s" % (my_test, my_test[1], my_result))
        else:
            print("Unit test FAILED: my_test %s expected result %s but got result %s" % (my_test, my_test[1], my_result))

# Generated at 2022-06-13 02:13:23.666092
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class TestMgr(PkgMgr):

        def __init__(self):
            super(TestMgr, self).__init__()
            self.pkg_list = [
                {'name': 'a', 'version': '1.2.3', 'arch': 'noarch', 'release': '1.fc20'},
                {'name': 'a', 'version': '1.2.4', 'arch': 'x86_64', 'release': '7.fc20'},
                {'name': 'c', 'version': '1.2.3', 'arch': 'x86_64', 'release': '7.fc99'},
            ]

        def is_available(self):
            pass

        def list_installed(self):
            return self.pkg_list


# Generated at 2022-06-13 02:13:26.139265
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

    class PackageManagerCLI(CLIMgr):
        CLI = "PackageManager"

    class PackageManagerLib(LibMgr):
        LIB = "PackageManager"

    pass

# Generated at 2022-06-13 02:13:28.693772
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert LibMgr.__name__ == 'LibMgr'
    assert LibMgr.__bases__ == (object,)
    lm = LibMgr()
    assert lm._lib is None


# Generated at 2022-06-13 02:13:38.055517
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # Test when the list_installed method returns an empty list
    class TestPkgMgr(PkgMgr):
        def list_installed(self):
            return []
        def get_package_details(self, package):
            package_details = {}
            package_details['name'] = package
            package_details['version'] = '1.0.0'
            return package_details
    mgr = TestPkgMgr()
    assert (mgr.get_packages() == {})

    # Test when the list_installed method returns a list with one item
    class TestPkgMgr(PkgMgr):
        def list_installed(self):
            return ['pkg1']
        def get_package_details(self, package):
            package_details = {}
            package_details['name'] = package

# Generated at 2022-06-13 02:14:58.148723
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.pkg_mgmt import get_all_pkg_managers
    from collections import namedtuple

    # Initiate an instance of all PkgMgr implementations
    mgrs = get_all_pkg_managers()
    for name, mgr in mgrs.items():
        mgrs[name] = mgr()

    # Stub pkgmanager methods and return static values
    # These static values will be returned regardless of the package name passed to the method
    mock_list_installed = namedtuple('mock_list_installed', ['return_value'])
    mock_get_package_details = namedtuple('mock_get_package_details', ['return_value'])

# Generated at 2022-06-13 02:14:59.143722
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    instance = PkgMgr()
    assert not instance.is_available()


# Generated at 2022-06-13 02:15:00.867735
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    py_path = CLIMgr()
    assert py_path.is_available() == True, "PkgMgr.is_available() should return True"


# Generated at 2022-06-13 02:15:02.481471
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    mock = PkgMgr()
    package = {'name': 'test', 'version': 'test'}
    assert mock.get_package_details(package) == package


# Generated at 2022-06-13 02:15:11.870988
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class MockPkgMgr(PkgMgr):

        def list_installed(self):
            return ['package1', 'package2']

        def get_package_details(self, package):
            if package == 'package1':
                return {'name': 'package1', 'version': 1}
            else:
                return {'name': 'package2', 'version': 1, 'source': 'rpm'}

    mock_pkg_mgr = MockPkgMgr()
    pkgs = mock_pkg_mgr.get_packages()
    assert pkgs == {'package1': [{'source': 'mockpkgmgr', 'name': 'package1', 'version': 1}],
                    'package2': [{'source': 'rpm', 'name': 'package2', 'version': 1}]}

# Generated at 2022-06-13 02:15:12.967957
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    p = PkgMgr()
    assert p.is_available() == NotImplemented


# Generated at 2022-06-13 02:15:16.372406
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestMgr(LibMgr):
        LIB = 'test_lib'

    class TestMgrB(LibMgr):
        LIB = 'test_lib_b'
    try:
        import test_lib
    except ImportError:
        import test_lib_b
    tmgr = TestMgr()
    assert tmgr._lib == test_lib
    tmgrb = TestMgrB()
    assert tmgrb._lib == test_lib_b

# Generated at 2022-06-13 02:15:17.978648
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lib = LibMgr()
    assert lib.is_available() == None


# Generated at 2022-06-13 02:15:18.575493
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pass

# Generated at 2022-06-13 02:15:20.068782
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    myPkgMgr = PkgMgr()
    myPkgMgr.list_installed()


# Generated at 2022-06-13 02:18:15.095435
# Unit test for method get_packages of class PkgMgr

# Generated at 2022-06-13 02:18:17.099027
# Unit test for constructor of class LibMgr
def test_LibMgr():
    # Create a new object of class LibMgr
    from ansible.module_utils.common.list_package_manager import LibMgr
    a = LibMgr()
    assert a

# Generated at 2022-06-13 02:18:18.482167
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    # Check if the type of return of list_installed is a List
    pass


# Generated at 2022-06-13 02:18:19.960398
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    assert get_all_pkg_managers() is not None
    assert get_all_pkg_managers() != 0

# Generated at 2022-06-13 02:18:21.278083
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class Foo(CLIMgr):
        CLI = 'foo'

    assert Foo().is_available() == False

# Generated at 2022-06-13 02:18:24.750966
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    class PkgMgrForTest(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ["toto"]
        def get_package_details(self, package):
            return {}

    pm = PkgMgrForTest()
    pm.get_package_details("toto")

# Generated at 2022-06-13 02:18:25.691871
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert hasattr(PkgMgr, "list_installed")


# Generated at 2022-06-13 02:18:34.468595
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    import os
    from tempfile import mkdtemp

    from ansible.module_utils.facts.system.pkg_mgr import CLIMgr

    class FakeCLIMgr(CLIMgr):
        CLI = 'fake_cli'

    old_env = os.environ.copy()
    try:
        fake_cli_path = mkdtemp()
        os.chmod(fake_cli_path, 0o700)
        os.environ['PATH'] = fake_cli_path
        pkg_mgr = FakeCLIMgr()

        assert pkg_mgr._cli is None
    finally:
        os.environ.clear()
        os.environ.update(old_env)

#  Unit test for constructor of class LibMgr

# Generated at 2022-06-13 02:18:35.681810
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class TestCLIMgr(CLIMgr):
        CLI = 'ls'
    obj = TestCLIMgr()
    assert isinstance(obj, CLIMgr)
    assert obj._cli == get_bin_path('ls')


# Generated at 2022-06-13 02:18:42.647680
# Unit test for constructor of class LibMgr
def test_LibMgr():
    
    from ansible.module_utils.common._utils import get_all_subclasses
    from ansible.module_utils.facts.packaging.rpm.rpm_sys import RpmSys
    from ansible.module_utils.facts.packaging.gem.gem import Gem

    pkg_managers = get_all_pkg_managers()
    rpm_sys = RpmSys()
    gem = Gem()

    if rpm_sys.is_available():
        rpm_cli = pkg_managers['rpmsys'].CLI
        assert rpm_sys._cli in rpm_cli

    if gem.is_available():
        gem_cli = pkg_managers['gem'].CLI
        assert gem._cli in gem_cli

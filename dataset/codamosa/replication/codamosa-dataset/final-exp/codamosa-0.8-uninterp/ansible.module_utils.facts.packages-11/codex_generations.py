

# Generated at 2022-06-13 02:09:23.099146
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import tempfile
    import os
    import shutil
    import test.modules.linux_package_facts.test_data.dnf_data as dnf_data
    import test.modules.linux_package_facts.test_data.rpm_data as rpm_data

    class TestLibMgr(LibMgr):
        LIB = 'test'

        def list_installed(self):
            return ['a', 'b', 'c']

        def get_package_details(self, package):
            return {'name': package, 'version': package}

    class TestCLIMgr(CLIMgr):
        CLI = 'test'

        def list_installed(self):
            return ['a', 'b', 'c']

        def get_package_details(self, package):
            return {'name': package, 'version': package}



# Generated at 2022-06-13 02:09:24.389632
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    p = PkgMgr()
    results = p.get_package_details("foo")
    assert results is None

# Generated at 2022-06-13 02:09:25.894056
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    for p in get_all_pkg_managers().values():
        assert p().is_available() == False


# Generated at 2022-06-13 02:09:29.163994
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # GIVEN
    lm = LibMgr()
    try:
        import adal
        should_fail = False
    except ImportError:
        should_fail = True

    # WHEN
    available = lm.is_available()

    # THEN
    assert available == should_fail



# Generated at 2022-06-13 02:09:36.047840
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    p1 = LibMgr()
    p2 = LibMgr()
    p3 = LibMgr()
    p1.LIB = 'ansible.module_utils.facts.packages.npm'
    p2.LIB = 'ansible.module_utils.facts.packages.pip'
    p3.LIB = 'ansible.module_utils.facts.packages.rpm'
    assert p1.is_available() == True
    assert p2.is_available() == True
    assert p3.is_available() == True


# Generated at 2022-06-13 02:09:37.715023
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    assert LibMgr().is_available() == False


# Generated at 2022-06-13 02:09:47.573015
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    existed_subclass = False
    for cls in get_all_subclasses(PkgMgr):
        if cls not in (LibMgr, CLIMgr):
            existed_subclass = True
            break

    # There is at least one subclass to test
    if existed_subclass:
        INSTALLED_PARAMS = {'name': 'fake_package_name', 'version': '1.0.0', 'source': 'fake_source'}
        installed_package = {
            'name': INSTALLED_PARAMS['name'],
            'version': INSTALLED_PARAMS['version']
        }

        pkg_mgr = cls()
        assert(pkg_mgr.get_package_details(installed_package) == INSTALLED_PARAMS)
    else:
        assert(True)

# Generated at 2022-06-13 02:09:54.771185
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class PkgMgr_test(PkgMgr):
        def __init__(self):
            pass
        def is_available(self):
            return True
        def list_installed(self):
            return ['package_name']
        def get_package_details(self, package):
            package_details = {'name' : package}
            return package_details
    pm = PkgMgr_test()
    assert pm.get_packages() == {"package_name": [{"name": "package_name"}]}



# Generated at 2022-06-13 02:10:00.951758
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.facts import PkgMgrFactCollector

    collector = PkgMgrFactCollector()

    class FakePkgMgr(PkgMgr):

        def __init__(self):

            self.packages = {'package_one': [{'name': 'package_one', 'version': '1.0', 'source': 'fakepkgmgr'}]}
            super(FakePkgMgr, self).__init__()

        def is_available(self):
            return True

        def list_installed(self):
            return ['package_one']

        def get_package_details(self, package):
            return {'name': package, 'version': '1.0', 'source': 'fakepkgmgr'}

    # Add the fake package manager to the list of package managers
    collector.p

# Generated at 2022-06-13 02:10:03.197724
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class Test(LibMgr):
        LIB = 'test'
    mgr = Test()
    assert mgr._lib is None



# Generated at 2022-06-13 02:10:12.328856
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class PkgMgrTest(PkgMgr):
        def list_installed(self):
            return ['package1', 'package2']
        def get_package_details(self, package):
            return {'name':package, 'version':'1.2.3', 'full':'%s-%s' % (package, '1.2.3')}
    testclass = PkgMgrTest()
    assert sorted(testclass.get_packages().keys()) == sorted(['package1','package2'])
    assert testclass.get_packages()['package1'][0]['name'] == 'package1'
    assert testclass.get_packages()['package1'][0]['version'] == '1.2.3'

# Generated at 2022-06-13 02:10:14.132683
# Unit test for constructor of class LibMgr
def test_LibMgr():
    cls = LibMgr()
    assert cls.is_available() == False


# Generated at 2022-06-13 02:10:22.599797
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class TestObject(PkgMgr):

        def is_available(self):
            pass

        def list_installed(self):
            return ['foo', 'bar']

        def get_package_details(self, package):
            return {'name': package, 'version': package[::-1] + str(len(package))}

    test_object = TestObject()
    assert test_object.get_packages() == {'foo': [{'name': 'foo', 'version': 'oof2', 'source': 'testobject'}], 'bar': [{'name': 'bar', 'version': 'rab3', 'source': 'testobject'}]}

# Generated at 2022-06-13 02:10:24.413951
# Unit test for constructor of class LibMgr
def test_LibMgr():
    obj = LibMgr()
    if obj is None:
        return False
    return True


# Generated at 2022-06-13 02:10:27.855542
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    # Test without calling this method
    class TestPkgMgr(PkgMgr):
        pass
    test_mgr = TestPkgMgr()
    assert hasattr(test_mgr, 'list_installed') is True
    getattr(test_mgr, 'list_installed')



# Generated at 2022-06-13 02:10:28.954665
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lib = LibMgr()
    assert lib is not None


# Generated at 2022-06-13 02:10:31.938071
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
   cli = CLIMgr()
   assert cli._cli is None


# Generated at 2022-06-13 02:10:33.203061
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    assert issubclass(PkgMgr, object) == True
    print('Class PkgMgr is subclass of object')


# Generated at 2022-06-13 02:10:44.412287
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class SolidPkgMgr(PkgMgr):

        def __init__(self, installed_packages):
            self.installed_packages = installed_packages

        def is_available(self):
            return True

        def list_installed(self):
            return self.installed_packages.keys()

        def get_package_details(self, package):
            return self.installed_packages[package]

    packages = {
        'package1': {'version': '1.0.0', 'name': 'package1'},
        'package2': {'version': '2.0.0', 'name': 'package2'},
    }

    pkg_mgr = SolidPkgMgr(installed_packages=packages)

# Generated at 2022-06-13 02:10:51.766044
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class PkgMgr_test(PkgMgr):
        def list_installed(self):
            return ["test"]

    # test for inheritance for this class
    try:
        isinstance(PkgMgr_test(), PkgMgr)
    except BaseException:
        print("Inheritance test for list_installed of PkgMgr failed")

    # test for overriding of the list_installed method from class PkgMgr
    try:
        PkgMgr_test().list_installed() == ["test"]
    except BaseException:
        print("Override test for list_installed of PkgMgr failed")



# Generated at 2022-06-13 02:10:56.801820
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert True

# Generated at 2022-06-13 02:10:59.627779
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestLibMgr(LibMgr):
        pass
    test_lib_instance = TestLibMgr()
    assert test_lib_instance._lib is None


# Generated at 2022-06-13 02:11:00.969480
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    app = CLIMgr()
    assert app.CLI is None

# Generated at 2022-06-13 02:11:02.683917
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    pass

# Generated at 2022-06-13 02:11:05.835718
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    mgrs = get_all_pkg_managers()
    for mgr_name in mgrs:
        mgr = mgrs[mgr_name]()
        assert not mgr.is_available()


# Generated at 2022-06-13 02:11:06.296695
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pass

# Generated at 2022-06-13 02:11:09.500250
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lm = LibMgr()
    assert lm.is_available() == False
    lm.LIB = 'ansible.module_utils.facts.os.freebsd'
    assert lm.is_available() == True


# Generated at 2022-06-13 02:11:12.399147
# Unit test for constructor of class LibMgr
def test_LibMgr():
    test = LibMgr()
    test.LIB = 'lib'
    test.is_available()
    test.list_installed()
    test.get_package_details('Package')
    test.get_packages()


# Generated at 2022-06-13 02:11:15.246429
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    try:
        class SomeLibMgr(LibMgr):
            LIB = 'xmlrpc.client'
        mgr = SomeLibMgr()
        assert mgr.is_available() == True
    except ImportError:
        pass

# Generated at 2022-06-13 02:11:25.742809
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import shutil
    import tempfile

    from ansible.module_utils import facts

    from ansible.module_utils.facts.system.pkg_mgr import PkgMgr
    from ansible.module_utils.facts.system.pkg_mgr import get_all_pkg_managers
    from ansible.module_utils.facts.system.pkg_mgr import CLIMgr
    from ansible.module_utils.facts.system.pkg_mgr import LibMgr
    from ansible.module_utils.facts.system.pkg_mgr import test_PkgMgr_get_packages_tests as tests
    from ansible.module_utils.facts.system.pkg_mgr import test_PkgMgr_get_packages_mock_package_managers as mock_package_managers


# Generated at 2022-06-13 02:11:32.149755
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert PkgMgr.is_available()


# Generated at 2022-06-13 02:11:34.337424
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pm = LibMgr()
    pm.LIB = 'ansible_test.pm'
    assert pm.is_available()


# Generated at 2022-06-13 02:11:35.872189
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    assert LibMgr().is_available()==False


# Generated at 2022-06-13 02:11:46.416411
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import os
    import shutil
    import tempfile
    import json
    import pkg_resources
    import pkg_resources.extern.packaging
    import ansible

    class PkgMgrTest(PkgMgr):

        def __init__(self):
            super(PkgMgrTest, self).__init__()

        def is_available(self):
            return False

        def list_installed(self):
            return []

        def get_package_details(self, package):
            return {}

    pm = PkgMgrTest()
    assert pm.get_packages() == {}

    # Generate a fake package
    pyver = '%s.%s' % sys.version_info[:2]
    tdir = tempfile.mkdtemp()

# Generated at 2022-06-13 02:11:48.487161
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    is_available_result = PkgMgr.is_available(PkgMgr())
    assert is_available_result == False


# Generated at 2022-06-13 02:11:55.494493
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # set up
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            self.installed = True
            return True

        def list_installed(self):
            return ["abc", "def"]

        def get_package_details(self, package):
            return {"name": package, "version": "1.0"}

    # test
    tpm = TestPkgMgr()
    result = tpm.get_packages()

    # verify
    expected_result = {"abc": [{"name": "abc", "version": "1.0"}],
                       "def": [{"name": "def", "version": "1.0"}]}
    assert result == expected_result

# Generated at 2022-06-13 02:11:56.619225
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    test_mgr = PkgMgr()
    assert test_mgr.is_available() is False


# Generated at 2022-06-13 02:12:03.456184
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    # Create a dummy class to test
    class PkgMgr_Test(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return []

        def get_package_details(self, package):
            return {}

    package_manager = PkgMgr_Test()
    assert package_manager.is_available() is True


# Generated at 2022-06-13 02:12:07.187753
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class TestCLIMgr(CLIMgr):
        CLI = "ls"
    pkg_mgr = TestCLIMgr()
    result = pkg_mgr.is_available()
    assert result is True


# Generated at 2022-06-13 02:12:09.698985
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestLibMgr(LibMgr):
        LIB = 'sys'

    t = TestLibMgr()
    assert t.LIB == 'sys'


# Generated at 2022-06-13 02:12:18.602816
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pass

# Generated at 2022-06-13 02:12:20.377131
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    mgr = CLIMgr()
    assert mgr.CLI is None
    assert mgr._cli is None



# Generated at 2022-06-13 02:12:21.092571
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert not hasattr(LibMgr(), '_lib')

# Generated at 2022-06-13 02:12:23.298498
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    try:
        __import__('apt')
        assert LibMgr().is_available() == True
    except ImportError:
        assert LibMgr().is_available() == False


# Generated at 2022-06-13 02:12:24.516108
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    test_object = CLIMgr()
    assert test_object._cli == None
    assert test_object.CLI == None

# Generated at 2022-06-13 02:12:25.794533
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    assert (False)



# Generated at 2022-06-13 02:12:27.272016
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lm = LibMgr()

# Generated at 2022-06-13 02:12:28.557321
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    test_class = PkgMgr()
    assert test_class


# Generated at 2022-06-13 02:12:35.983236
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class LibMgrTest(LibMgr):
        LIB = 'fakelib'

    test_case_1 = LibMgrTest()
    test_case_1.is_available()

    assert test_case_1._lib is None

    try:
        import fakelib
        assert True

        test_case_2 = LibMgrTest()
        test_case_2.is_available()

        assert test_case_2._lib is not None
    except ImportError:
        assert False


# Generated at 2022-06-13 02:12:42.255989
# Unit test for constructor of class LibMgr
def test_LibMgr():
    import ansible.module_utils.common.collector.packages.python as package_python

    class testMgr(LibMgr):
        LIB = 'python' 

    test = testMgr()

    if not test.is_available():
        raise 'Failed to import the library'
    if not hasattr(test, '_lib'):
        raise 'Failed to import the library'


# Generated at 2022-06-13 02:13:01.557552
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class FakePkgMgr(PkgMgr):
        def get_package_details(self, package):
            return {}
        def list_installed(self):
            return []
    FakePkgMgr().list_installed()


# Generated at 2022-06-13 02:13:04.300108
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # currently commented out since it depends on the availability of python-apt
    # lm = LibMgr()
    # assert lm.is_available() is False
    # lm._lib = 'python-apt'
    # assert lm.is_available() is True
    pass


# Generated at 2022-06-13 02:13:08.308189
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class LibMgr1(LibMgr):
        pass

    class LibMgr2(LibMgr):
        LIB = 'json'

    class LibMgr3(LibMgr):
        LIB = 'os'

    assert LibMgr1().is_available() == False
    assert LibMgr2().is_available() == True
    assert LibMgr3().is_available() == True


# Generated at 2022-06-13 02:13:15.301547
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import mock
    from ansible.module_utils.common.process import get_bin_path
    # Mock class
    class MyMgr(CLIMgr):
        CLI = 'mycli'
    mgr = MyMgr()
    # is_available() should return True if get_bin_path() returns a non-empty string
    with mock.patch('ansible.module_utils.common.process.get_bin_path', return_value='/usr/bin/mycli'):
        assert mgr.is_available()
    # is_available() should return False if get_bin_path() raises ValueError
    with mock.patch('ansible.module_utils.common.process.get_bin_path', side_effect=ValueError("No such file or directory")):
        assert not mgr.is_available()

# Generated at 2022-06-13 02:13:16.993974
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    mgr = CLIMgr()
    assert mgr._cli is None, '_cli not None'

# Generated at 2022-06-13 02:13:21.343269
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pmgr = PkgMgr()
    result = pmgr.get_package_details("name=foo, version=1.0.0, vendor=Red Hat, installtime=None")
    assert result == {'name': 'foo', 'version': '1.0.0', 'vendor': 'Red Hat', 'installtime': 'None'}


# Generated at 2022-06-13 02:13:23.499951
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    packages = get_all_pkg_managers()
    # Test if the class CLIMgr has been added in all modules
    assert 'climgr' in packages

# Generated at 2022-06-13 02:13:33.335596
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    """
    This method is not supposed to be called. Just a unit test to verify that the
    get_packages method of the PkgMgr class behaves as expected.
    """
    class FakePkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return (('foo', '0.1'), ('bar', '0.2'))

        def get_package_details(self, package):
            return {'name': package[0], 'version': package[1]}

    package_mgr = FakePkgMgr()
    packages = package_mgr.get_packages()

    assert packages is not None
    assert isinstance(packages, dict)
    assert len(packages) == 2

    assert 'foo' in packages

# Generated at 2022-06-13 02:13:34.268268
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pass


# Generated at 2022-06-13 02:13:35.058196
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pass

# Generated at 2022-06-13 02:14:15.533616
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    import unittest
    import sys
    
    class TestPkgMgr_list_installed(unittest.TestCase):
        pkgManagerMock = None
        list_installedMock = []

        @classmethod
        def setUpClass(inst):
            import ansible.module_utils.software.pkg_mgr
            inst.pkgManagerMock = ansible.module_utils.software.pkg_mgr.PkgMgr()
            inst.pkgManagerMock.list_installed = lambda: TestPkgMgr_list_installed.list_installedMock

        def test_list_installed(self):
            self.assertEqual(self.pkgManagerMock.list_installed(), TestPkgMgr_list_installed.list_installedMock)

    # Add the test suite to the test loader

# Generated at 2022-06-13 02:14:24.899248
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible_collections.ansible.community.tests.unit.modules.utils.common.pkg_mgr.helper import FakePkgMgr

    pkg_mgr = FakePkgMgr()
    pkg_mgr.list_installed = lambda: ['a', 'b']
    pkg_mgr.get_package_details = lambda package: {'name': package}
    packages = pkg_mgr.get_packages()
    assert packages == {'a': [{'name': 'a', 'source': 'fakepkgmgr'}],
                        'b': [{'name': 'b', 'source': 'fakepkgmgr'}]}

# Generated at 2022-06-13 02:14:28.735752
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['a', 'b', 'c']

        def get_package_details(self, package):
            return {'name': package, 'version': package + '-version'}
    assert TestPkgMgr().get_packages() == {'a': [{'name': 'a', 'version': 'a-version', 'source': 'testpkgmgr'}],
                                          'b': [{'name': 'b', 'version': 'b-version', 'source': 'testpkgmgr'}],
                                          'c': [{'name': 'c', 'version': 'c-version', 'source': 'testpkgmgr'}]}


# Generated at 2022-06-13 02:14:35.343180
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible_collections.community.general.tests.unit.compat import unittest
    from ansible_collections.community.general.plugins.modules.system.pkg_mgr import PkgMgr

    # Package:
    #   Name: python
    #   Version: 2.7.10
    #   Arch: x86_64
    #   Repository: installed
    #   Summary: An interpreted, interactive, object-oriented programming language
    #   URL: http://www.python.org/
    #   License: Python
    #   Description: Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
   

# Generated at 2022-06-13 02:14:39.705926
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class Foo(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['foo', 'bar']

        def get_package_details(self):
            return {}
    package_details = Foo.get_package_details(Foo(), 'baz')
    assert package_details == {}

# Generated at 2022-06-13 02:14:47.459878
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    from ansible.module_utils.software_mgmt_base import PkgMgr
    from ansible.module_utils.software_mgmt_base import PkgMgrTestCase
    from ansible.module_utils.software_mgmt_base import TestClass
    import pytest
    # Test case where python module is not present
    assert not PkgMgrTestCase().list_installed()
    # Test case where python module is present
    assert PkgMgrTestCase(module={'version': '2.0.0', 'source': 'testpkgmgr'}).list_installed()
    # Test case where python module is not present and expected module is absent

# Generated at 2022-06-13 02:14:49.376553
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    '''
    Unit test for constructor of class CLIMgr
    '''
    mgr = CLIMgr()
    assert mgr.is_available() is False



# Generated at 2022-06-13 02:14:56.771331
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class PkgMgrMock(PkgMgr):

        def get_package_details(self, package):
            return package

        def list_installed(self):
            return ['package1', 'package2']

    pkgmgr_mock = PkgMgrMock()

    packages = pkgmgr_mock.get_packages()

    assert isinstance(packages, dict)
    assert len(packages) == 2
    assert isinstance(packages['package1'], list)
    assert isinstance(packages['package2'], list)
    assert packages['package1'][0] == 'package1'
    assert packages['package2'][0] == 'package2'


# Generated at 2022-06-13 02:15:01.297925
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    #Create fake class for test
    class TestClass(LibMgr):
        LIB = 'fake_import'

    #Case when 'fake_import' is imported
    test_instance = TestClass()
    import sys
    sys.modules['fake_import'] = 'test_module'
    assert test_instance.is_available()

    #Case when 'fake_import' is not imported
    test_instance = TestClass()
    assert not test_instance.is_available()


# Generated at 2022-06-13 02:15:01.818808
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pass



# Generated at 2022-06-13 02:16:21.896171
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class test_PkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['test_package']

        def get_package_details(self, package):
            return {'name': package}

    test = test_PkgMgr()
    assert test.get_packages() == {'test_package': [{'name': 'test_package', 'source': 'test_pkgmgr'}]}

# Generated at 2022-06-13 02:16:24.044002
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible_test._internal.test_modules.test_get_package_details import Test_get_packages
    Test_get_packages()



# Generated at 2022-06-13 02:16:25.781250
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class TestLibMgr(LibMgr):
        LIB = 'types'
    assert TestLibMgr().is_available()


# Generated at 2022-06-13 02:16:30.613058
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ._utils import run_command
    from .yumpkg import YumPkg
    import os
    import sys

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    test_instance = YumPkg
    assert test_instance.is_available() == True

# Generated at 2022-06-13 02:16:38.875814
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    def list_installed():
        return ["foo","bar"]
    def get_package_details(package):
        if package == "foo":
            return { "name": "foo", "version": "1.0.0"}
        elif package == "bar":
            return { "name": "bar", "version": "2.0.0"}
        else:
            return {}
    class PkgManager(PkgMgr):
        def list_installed(self):
            return list_installed()
        def get_package_details(self, package):
            return get_package_details(package)

    obj = PkgManager()

# Generated at 2022-06-13 02:16:39.513699
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert isinstance(CLIMgr(), PkgMgr)

# Generated at 2022-06-13 02:16:41.848587
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    class DummyCLIMgr(CLIMgr):
        CLI = 'not_installed_command'

    class DummyCLIMgr2(CLIMgr):
        CLI = 'grep'

    assert DummyCLIMgr().is_available() is False
    assert DummyCLIMgr2().is_available() is True

# Generated at 2022-06-13 02:16:44.327462
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pkg_mgr = CLIMgr()
    assert pkg_mgr.is_available() == False

    class pkgMgrTest(CLIMgr):
        CLI = "ls"

    pkg_mgr_test = pkgMgrTest()
    assert pkg_mgr_test.is_available() == True



# Generated at 2022-06-13 02:16:46.225565
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class TestLibMgr(LibMgr):
        LIB = 'somelib'

    # This test is based on the assumption that some library with the same name is installed
    assert TestLibMgr().is_available()


# Generated at 2022-06-13 02:16:46.573043
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    assert True
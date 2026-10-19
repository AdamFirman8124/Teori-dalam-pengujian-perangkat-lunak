

# Generated at 2022-06-13 02:09:20.818894
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class PkgMgr_test(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['pack1', 'pack2']

        def get_package_details(self, package):
            return package

    test_package = PkgMgr_test()
    output = test_package.get_packages()
    assert output == {'pack1': ['pack1'], 'pack2': ['pack2']}

# Generated at 2022-06-13 02:09:24.463162
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestMgr(LibMgr):
        LIB = 'ansible.module_utils.facts.system.os'
    t = TestMgr()
    assert t.LIB == 'ansible.module_utils.facts.system.os'


# Generated at 2022-06-13 02:09:26.093897
# Unit test for constructor of class LibMgr
def test_LibMgr():
    l = LibMgr()
    l._lib = "test"
    return l


# Generated at 2022-06-13 02:09:28.311006
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    from ansible.module_utils.facts.collector.pkg_mgr import get_all_pkg_managers

    assert get_all_pkg_managers()

# Generated at 2022-06-13 02:09:31.573085
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.facts.pkg_mgr.rpm import LibRpm
    rpm = LibRpm()
    assert(rpm.is_available() == True)


# Generated at 2022-06-13 02:09:33.236198
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lg = LibMgr()
    res = lg.is_available()
    assert res != True


# Generated at 2022-06-13 02:09:34.755615
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert PkgMgr.list_installed is PkgMgr().list_installed


# Generated at 2022-06-13 02:09:37.246028
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class MyCLIMgr(CLIMgr):
        CLI = 'test'
    my_mgr = MyCLIMgr()
    assert my_mgr is not None

# Generated at 2022-06-13 02:09:38.012748
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pass

# Generated at 2022-06-13 02:09:44.082845
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    pkg_mgrs = get_all_pkg_managers()
    assert isinstance(pkg_mgrs, dict)
    for pkg_mgr_key, pkg_mgr_class in pkg_mgrs.items():
        assert isinstance(pkg_mgr_key, str)
        assert issubclass(pkg_mgr_class, PkgMgr)

# Generated at 2022-06-13 02:09:56.333626
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class MockPkgMgr(PkgMgr):
        # Return a list of package names from list_installed
        def list_installed(self):
            return [1, 2, 3]

        # Return a dict with the package name and version
        def get_package_details(self, package):
            return {"name": "pkg_%s" % package, "version": "1.0"}

    mgr = MockPkgMgr()
    packages = mgr.get_packages()
    assert 3 == len(packages), "There should be 3 packages"
    assert 1 == len(packages[list(packages)[0]]), "The default source should be the class name"

# Generated at 2022-06-13 02:09:58.319246
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    test_class = CLIMgr()
    assert test_class._cli is None


# Generated at 2022-06-13 02:10:05.089186
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    import unittest

    class testclass(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['testpackage/testversion']

        def get_package_details(self, package):
            return {'name': 'testpackage', 'version': 'testversion'}

    test_object = testclass()
    assert test_object.get_packages() == {'testpackage': [{'name': 'testpackage', 'version': 'testversion', 'source': 'testclass'}]}

# Generated at 2022-06-13 02:10:07.766184
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cm = CLIMgr()
    assert cm.CLI == None, "CLI should be set to None"
    assert cm._cli == None, "_cli should be set to None"


# Generated at 2022-06-13 02:10:08.572684
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
  pass


# Generated at 2022-06-13 02:10:14.371915
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import unittest

    class DummyPkgMgr(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return [
                'foo/1-1.el7',
                'foo/2-1.el7',
                'bar/1-1.el7',
                'baz/1-1.el7'
            ]

        def get_package_details(self, package):
            return {
                'name': package.split('/')[0],
                'version': package.split('-')[0].split('/')[1]
            }

    def __init__(self):
        unittest.TestCase.__init__(self, 'test_PkgMgr_get_packages')

    dummy_pkg_mgr = D

# Generated at 2022-06-13 02:10:15.577651
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    mgr = CLIMgr()
    assert mgr._cli == None

# Unit test to ensure that the class CLIMgr inherits from PkgMgr

# Generated at 2022-06-13 02:10:17.004718
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    #Test that is_available returns false for non-existent object
    assert PkgMgr().is_available() is False

#Unit test for method list_installed of class PkgMgr

# Generated at 2022-06-13 02:10:20.109040
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    test_class = LibMgr()
    test_class.LIB = 'os' # This is an installed python library
    assert(test_class.is_available() is True)


# Generated at 2022-06-13 02:10:22.645014
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class testLibMgr(LibMgr):
        LIB = "os"

    lm = testLibMgr()
    assert lm.is_available() == True


# Generated at 2022-06-13 02:10:31.517289
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr()

# Generated at 2022-06-13 02:10:36.296609
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return False

        def list_installed(self):
            pass

        def get_package_details(self, package):
            pass
    obj = TestPkgMgr()
    assert obj.is_available() == False


# Generated at 2022-06-13 02:10:38.831981
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lib_mgr = LibMgr()
    assert lib_mgr._lib is None
    assert isinstance(lib_mgr, PkgMgr)


# Generated at 2022-06-13 02:10:49.244960
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import collections

    import ansible.module_utils.packages.package_manager_test_mock

    pm = ansible.module_utils.packages.package_manager_test_mock.PkgMgrTestMock()
    assert (pm.is_available() == True)

    assert isinstance(pm.get_packages(), collections.Mapping)
    assert (pm.get_packages() == {'a': [{'name': 'a', 'version': '1'}, {'name': 'a', 'source': 'PkgMgrTestMock', 'version': '2'}], \
            'b': [{'name': 'b', 'version': '1'}, {'name': 'b', 'version': '2'}]})



# Generated at 2022-06-13 02:10:57.165269
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    
    class test_CLIMgr(CLIMgr):
        CLI = "/bin/python"

    test_class = test_CLIMgr()

    # Should return False if CLI is not in the PATH
    test_class_1 = test_CLIMgr()
    test_class_1.CLI = "/bin/test_CLI"
    assert test_class_1.is_available() == False

    # Should return True if CLI is present
    assert test_class.is_available() == True

# Generated at 2022-06-13 02:10:59.255850
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pm = PkgMgr()
    assert pm.get_packages() == {}


# Generated at 2022-06-13 02:11:04.162757
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ['test1', 'test2']
        def get_package_details(self, package):
            pass
    instance = TestPkgMgr()
    assert instance is not None
    assert isinstance(instance, PkgMgr)
    assert instance.list_installed() == ['test1', 'test2']



# Generated at 2022-06-13 02:11:07.003710
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class TestCLIMgr(CLIMgr):
        CLI = "test_cli"

    testMgr = TestCLIMgr()
    assert testMgr._cli is None


# Generated at 2022-06-13 02:11:09.300489
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    list_installed = PkgMgr.list_installed
    try:
        list_installed(PkgMgr)
    except:
        return True
    return False


# Generated at 2022-06-13 02:11:17.127488
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import os
    import platform
    import mock
    import ansible.module_utils.system.distribution as distribution
    import ansible.module_utils.common.network as network
    import ansible.module_utils.common._utils as utils
    from importlib import import_module

    pkg_mgr = utils.get_all_pkg_managers()
    module = import_module('ansible.module_utils.system.distribution')

    distribution.add_distribution_info = mock.MagicMock()
    network.get_platform_subclass = mock.MagicMock()

    # Set Ubuntu distribution
    distribution.add_distribution_info.return_value = (distribution.Distribution.UBUNTU,
                                                       "",
                                                       "")

    # Set platform to be Linux and windows
    network

# Generated at 2022-06-13 02:11:34.293801
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pass


# Generated at 2022-06-13 02:11:35.576553
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr()



# Generated at 2022-06-13 02:11:45.313619
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # The mocked list_installed method always returns a single installed package.
    # The mocked get_package_details method always returns a single version of the package

    class MockPkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['python-foo']

        def get_package_details(self, package):
            return {'name': 'python-foo', 'version': '1.0'}

    pkg_mgr = MockPkgMgr()
    packages = pkg_mgr.get_packages()
    assert packages == {'python-foo': [{'name': 'python-foo', 'version': '1.0', 'source': 'mockpkgmgr'}]}

# Generated at 2022-06-13 02:11:53.964040
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

  # Test CLIMgr.__init__ with CLI=None, i.e. empty class
  # Expect AttributeError exception
  try:
    class A(CLIMgr):
      pass
    A()
    assert False
  except AttributeError:
    pass

  # Test CLIMgr.__init__ with CLI='a_cli'
  class B(CLIMgr):
    CLI = 'a_cli'
  b = B()
  assert isinstance(b, CLIMgr)
  assert b._cli == None
  assert b.is_available() == False

  # Test CLIMgr.__init__ with CLI='python'
  class C(CLIMgr):
    CLI = 'python'
  c = C()
  assert isinstance(c, CLIMgr)
  assert c._cli != None

# Generated at 2022-06-13 02:11:55.278740
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    pkg_mgr = CLIMgr()
    assert pkg_mgr._cli is None


# Generated at 2022-06-13 02:11:56.870759
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cm = CLIMgr()
    assert cm.CLI == None
    assert cm._cli == None
    assert cm.is_available() == False


# Generated at 2022-06-13 02:12:04.469224
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():

    class TestPkgMgr(PkgMgr):

        def list_installed(self):
            return [{'name': 'pkg1', 'version': '1.0'}, {'name': 'pkg2', 'version': '2.0'}]

    try:
        pkg_obj = TestPkgMgr()
        assert pkg_obj.list_installed
        pkg_obj.list_installed()
    except AttributeError:
        assert False



# Generated at 2022-06-13 02:12:06.371353
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class test_class(LibMgr):
        pass
    test_obj = test_class()
    assert test_obj._lib is None



# Generated at 2022-06-13 02:12:11.399264
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    # Preparation: Create test data for package details
    package = 'test_name'
    name = 'name'
    version = 'version'

    # Test: Execute method
    result = PkgMgr.get_package_details(package)

    # Verify: Result is as expected
    assert result == {name: package, version: package}



# Generated at 2022-06-13 02:12:20.066692
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    from ansible.module_utils.common.process import get_bin_path

    # create mock method
    def mock_list_installed(self):
        return ['a', 'b']

    # create mock method
    def mock_get_package_details(self, pkg):
        return {'name': pkg, 'version': '1.0'}

    # mock PkgMgr
    pm = PkgMgr()
    pm.list_installed = mock_list_installed
    pm.get_package_details = mock_get_package_details

    # run and assert

# Generated at 2022-06-13 02:12:54.148157
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert LibMgr()._lib is None



# Generated at 2022-06-13 02:12:56.954731
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    climgr = CLIMgr()
    assert(not climgr.is_available())
    climgr.CLI = "rpm"
    assert(climgr.is_available())

# Generated at 2022-06-13 02:12:58.820641
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    try:
        get_bin_path('nonsense')
        assert(False)
    except ValueError:
        assert(True)

# Generated at 2022-06-13 02:13:00.701186
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class CLIMgrTest(CLIMgr):
        CLI = 'lsb_release'

    obj = CLIMgrTest()
    assert obj.is_available()

# Generated at 2022-06-13 02:13:01.767634
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    mgr = CLIMgr()
    assert mgr._cli is None

# Generated at 2022-06-13 02:13:02.843359
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert "__init__" in dir(LibMgr())


# Generated at 2022-06-13 02:13:04.469035
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert True is CLIMgr().is_available()

# Generated at 2022-06-13 02:13:05.738847
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestClass(LibMgr):
        LIB = 'os'

    assert TestClass().is_available()


# Generated at 2022-06-13 02:13:06.442116
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr() is not None

# Generated at 2022-06-13 02:13:12.712540
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class MyPkgMgr(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ['foo']
        def get_package_details(self, package):
            return {'name':'foo', 'version':'1.0'}

    pm = MyPkgMgr()
    assert pm.get_packages() == {'foo': [{'name': 'foo', 'version': '1.0', 'source': 'mypkgmgr'}]}

# Generated at 2022-06-13 02:14:21.020352
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pass



# Generated at 2022-06-13 02:14:23.495347
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    class TestPkgMgr(CLIMgr):
        CLI = 'foo'

    assert TestPkgMgr().is_available() == False


# Generated at 2022-06-13 02:14:27.719852
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class TestPkgMgrClass(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return ['package1', 'package2', 'package3', 'package4']

        def get_package_details(self, package):
            return {'name': package, 'version': '1.0', 'source': 'test'}

    test_pkg_class = TestPkgMgrClass()

# Generated at 2022-06-13 02:14:28.762871
# Unit test for constructor of class LibMgr
def test_LibMgr():
    test_LibMgr = LibMgr()



# Generated at 2022-06-13 02:14:30.116273
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    test_mgr = PkgMgr()
    assert None == test_mgr.is_available()


# Generated at 2022-06-13 02:14:32.315930
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class TestCLIMgr(CLIMgr):
        CLI = 'test_nope'
    tcm = TestCLIMgr()
    assert(tcm.is_available() is False)


# Generated at 2022-06-13 02:14:38.540755
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    assert get_all_pkg_managers()['apt']().is_available() is True
    assert get_all_pkg_managers()['yum']().is_available() is True
    assert get_all_pkg_managers()['dnf']().is_available() is True
    assert get_all_pkg_managers()['zypper']().is_available() is True
    assert get_all_pkg_managers()['portage']().is_available() is True
    assert get_all_pkg_managers()['apk']().is_available() is True

# Generated at 2022-06-13 02:14:45.426129
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pkg_mgr = PkgMgr()
    installed_packages = pkg_mgr.list_installed()
    package_list = []
    if installed_packages:
        for pkg in installed_packages:
            package_list.append(pkg_mgr.get_package_details(pkg))
    res = {}
    for p in package_list:
        pkg_name = p['name']
        if pkg_name not in res:
            res[pkg_name] = [p]
        else:
            res[pkg_name].append(p)
    assert res == pkg_mgr.get_packages()

# Generated at 2022-06-13 02:14:46.258500
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pm = PkgMgr()
    assert pm.get_package_details([]) == {}

# Generated at 2022-06-13 02:14:51.736801
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgr
    import pytest
    class test_pkgmgr(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return ['foo', 'bar']

        def get_package_details(self, package):

            #let's test unicode too :)
            if package == 'foo':
                return {'name': 'foo', 'version': u'1.2\u2033', 'source': 'test_pkgmgr'}
            elif package == 'bar':
                return {'name': 'bar', 'version': '1.2.7', 'source': 'test_pkgmgr'}
            else:
                return

# Generated at 2022-06-13 02:17:51.749516
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import pytest
    ## Test case when given CLI does not exist
    class CLIMgr_UnitTest_NotFound(CLIMgr):
        CLI = 'does-not-exist'
    pkg_manager = CLIMgr_UnitTest_NotFound()
    assert pkg_manager.is_available() == False
    ## Test case when given CLI is exist
    class CLIMgr_UnitTest_Exist(CLIMgr):
        CLI = 'ls'
    pkg_manager = CLIMgr_UnitTest_Exist()
    assert pkg_manager.is_available() == True


# Generated at 2022-06-13 02:17:54.771450
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class CLITest(CLIMgr):
        CLI = "test"
    test = CLITest()
    assert test._cli is None
    assert test.is_available() == False
    test.CLI = "python"
    assert test.is_available() == True


# Generated at 2022-06-13 02:17:55.760368
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert LibMgr() is not None


# Generated at 2022-06-13 02:18:04.222370
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.common.collections import ImmutableDict
    import collections

    class MyPkgMgr(PkgMgr):
        def list_installed(self):
            return ['package1', 'package2']

        def get_package_details(self, package):
            return {'name': package, 'version': '1.0.0'}

    mypkgmgr = MyPkgMgr()
    assert isinstance(mypkgmgr.get_packages(), dict)
    assert len(mypkgmgr.get_packages()) == 2
    for pkg in mypkgmgr.get_packages():
        assert pkg in ['package1', 'package2']
        assert isinstance(mypkgmgr.get_packages()[pkg], list)

# Generated at 2022-06-13 02:18:12.192102
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.common._collections_compat import Mapping, MutableMapping
    import inspect
    for cls in get_all_pkg_managers().values():
        # ensure each class implements a 'get_packages' method
        assert hasattr(cls, 'get_packages')
        # ensure each class has a 'is_available' method
        assert hasattr(cls, 'is_available')
        # ensure each class has a 'get_packages' method which returns a dict
        pm = cls()
        if hasattr(cls, 'LIB'):
            assert pm.is_available()
        elif hasattr(cls, 'CLI'):
            assert pm.is_available()
        packages = pm.get_packages()
        assert inspect.isclass(packages)

# Generated at 2022-06-13 02:18:13.686027
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lib_mgr = LibMgr()
    assert lib_mgr.is_available() is False


# Generated at 2022-06-13 02:18:18.551069
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    # This is only a test to check if the function "list_installed"
    # is implemented in all the classes which are derived by class PkgMgr
    all_pkg_managers = get_all_pkg_managers()
    for manager in all_pkg_managers:
        if 'list_installed' not in str(dir(all_pkg_managers[manager])):
            raise NotImplementedError("The method list_installed from class PkgMgr is not implemented in the class " + manager)


# Generated at 2022-06-13 02:18:23.630834
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class TestPkgMgr(PkgMgr):
        def list_installed(self):
            return []
        def get_package_details(self, package):
            pass
    PkgMgr_obj = TestPkgMgr()
    assert 'name' in PkgMgr_obj.get_package_details({})
    assert 'version' in PkgMgr_obj.get_package_details({})
    assert 'source' in PkgMgr_obj.get_package_details({})


# Generated at 2022-06-13 02:18:27.305569
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    for pkg_mgr in get_all_pkg_managers():
        pkg_mgr_obj = get_all_pkg_managers()[pkg_mgr]
        pkg_mgr_obj_check = isinstance(pkg_mgr_obj(), PkgMgr)
        assert isinstance(pkg_mgr_obj(), PkgMgr)


# Generated at 2022-06-13 02:18:30.955554
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    deb = CLIMgr()
    deb.CLI = 'dpkg-deb'
    assert deb.is_available()
    deb.CLI = 'foobar'
    assert not deb.is_available()

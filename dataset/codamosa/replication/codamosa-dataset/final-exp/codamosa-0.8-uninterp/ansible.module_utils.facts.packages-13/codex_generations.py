

# Generated at 2022-06-13 02:09:17.956707
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr()

# Generated at 2022-06-13 02:09:20.457213
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

    pkg = CLIMgr()
    assert pkg



# Generated at 2022-06-13 02:09:22.544707
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pmp = LibMgr()
    assert pmp.is_available() == False


# Generated at 2022-06-13 02:09:24.641062
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    assert isinstance(PkgMgr.get_package_details(PkgMgr,{}), dict)


# Generated at 2022-06-13 02:09:27.487670
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    # Test for any package manager
    for pkg_mgr in get_all_pkg_managers().values():
        pkg_mgr_obj = pkg_mgr()
        assert not isinstance(pkg_mgr_obj.is_available(), dict)



# Generated at 2022-06-13 02:09:30.848028
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    mgrs = get_all_pkg_managers()
    for mgr in mgrs.values():
        result = mgr().is_available()
        if result is True:
            assert isinstance(result, bool)
        else:
            assert result is None or isinstance(result, bool)


# Generated at 2022-06-13 02:09:37.956333
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            # This method should return a list of installed packages
            return ['dummy_package', 'dummy_new_package']

        def get_package_details(self, package):
            return {'name': package}

    result = TestPkgMgr().get_packages()
    assert 'dummy_package' in result
    assert len(result['dummy_package']) == 1

    assert 'dummy_new_package' in result
    assert len(result['dummy_new_package']) == 1


#

# Generated at 2022-06-13 02:09:40.082356
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    t = PkgMgr()
    assert t.get_packages() == {}

# Generated at 2022-06-13 02:09:42.653158
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    a = PkgMgr()
    try:
        result = a.is_available()
    except NotImplementedError:
        result = True
    return result


# Generated at 2022-06-13 02:09:47.396304
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    test_package_details = {
        'name': 'test_name',
        'version': 'test_version',
        'source': 'test_source'
    }
    pm = PkgMgr()
    assert pm.get_package_details("test") == test_package_details


# Generated at 2022-06-13 02:09:59.013866
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import json
    class TestPkgMgr(PkgMgr):
        def __init__(self):
            super(TestPkgMgr, self).__init__()
        def list_installed(self):
            return ['a', 'b']
        def get_package_details(self, package):
            return {'name': package, 'version': package}
    tpm = TestPkgMgr()
    assertion_result = (tpm.get_packages() == {'a': [{'name': 'a', 'version': 'a', 'source': 'testpkgmgr'}],
                                              'b': [{'name': 'b', 'version': 'b', 'source': 'testpkgmgr'}]})

# Generated at 2022-06-13 02:10:00.035314
# Unit test for constructor of class LibMgr
def test_LibMgr():

    assert not LibMgr().LIB


# Generated at 2022-06-13 02:10:01.713289
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lm = LibMgr()
    result = lm.is_available()
    assert result == False


# Generated at 2022-06-13 02:10:02.832715
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert LibMgr



# Generated at 2022-06-13 02:10:03.580622
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    apg = LibMgr()
    assert (apg.is_available() == True)


# Generated at 2022-06-13 02:10:06.009365
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # To test, run the following command:
    # python -m pytest test_utils.py

    mgr = LibMgr()
    assert not mgr.is_available()


# Generated at 2022-06-13 02:10:07.542619
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    mgr = PkgMgr()
    assert mgr.is_available() == NotImplementedError

# Generated at 2022-06-13 02:10:08.320992
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    assert PkgMgr.get_package_details(None) is None


# Generated at 2022-06-13 02:10:10.032542
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    instance = CLIMgr()
    instance.CLI = "yum.py"
    assert instance.is_available() == True
    instance.CLI = "apt.py"
    assert instance.is_available() == False


# Generated at 2022-06-13 02:10:13.177410
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # Because of tight coupling between module and class, the test method has to be in the same module
    import unittest
    class TestCLIMgr(unittest.TestCase):
        def test_is_available_return_value(self):
            p = CLIMgr()
            with self.assertRaises(NotImplementedError):
                p.is_available()
    unittest.main()

# Generated at 2022-06-13 02:10:26.705980
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    import mock
    import string
    import random

    # Test case - success
    lib = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    pm = LibMgr()
    pm.LIB = lib
    with mock.patch('ansible.module_utils.common.collections.ansible_collections.community.generic.plugins.module_utils.facts.system.pkg_mgr.__import__') as mock_import:
        mock_import.return_value = 'test_value'
        assert pm.is_available()
        assert pm._lib == 'test_value'

    # Test case - failure
    pm = LibMgr()
    pm.LIB = lib

# Generated at 2022-06-13 02:10:28.414418
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestLib(LibMgr):
        LIB = 'os'
    tl = TestLib()
    assert tl._lib is None


# Generated at 2022-06-13 02:10:29.194540
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr() is not None



# Generated at 2022-06-13 02:10:40.893837
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import re
    import unittest

    class FakePkgMgr(PkgMgr):

        def list_installed(self):
            return ['foo', 'bar']

        def get_package_details(self, package):
            return {'name': package, 'version': '1.0'}

    p = FakePkgMgr()
    output = p.get_packages()

# Generated at 2022-06-13 02:10:45.950157
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    obj_cli_true = CLIMgr()
    obj_cli_false = CLIMgr()
    obj_cli_false.CLI = 'unknown'

    assert obj_cli_true.is_available() == True
    assert obj_cli_false.is_available() == False


# Generated at 2022-06-13 02:10:49.407993
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pkgs = get_all_pkg_managers()
    libs = pkgs['lib']()
    clis = pkgs['cli']()

    libs.is_available()
    clis.is_available()

# Generated at 2022-06-13 02:10:51.193895
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert PkgMgr.is_available(0) == False


# Generated at 2022-06-13 02:11:01.973179
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class PkgMgr_test(PkgMgr):
        def __init__(self):
            super(PkgMgr_test, self).__init__()
        def list_installed(self):
            return [{'name': 'a', 'version': '1.0'}, {'name': 'b', 'version': '2.0'}, {'name': 'a', 'version': '3.0'}]
        def get_package_details(self, package):
            return package
    pm = PkgMgr_test()
    installed = pm.get_packages()

# Generated at 2022-06-13 02:11:05.428671
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    test_class_name = 'LibMgr'
    test_class = globals()[test_class_name]
    test_obj = test_class()
    assert test_obj.is_available() == False


# Generated at 2022-06-13 02:11:14.423550
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    import platform
    import sys
    '''
    When calling the get_package_details method with a package it should return a dict
    with at least the name and version of the package
    '''

    def get_package_details():
        '''
        A fake get_package_details method that returns the platform info
        '''
        return {"name": platform.python_implementation(), "version": platform.python_version()}

    class PkgMgrChild(PkgMgr):
        '''
        A Fake Class inherited from PkgMgr
        '''
        def __init__(self):
            self._dict = {"ansible": "2.6", "python": "2.7"}

# Generated at 2022-06-13 02:11:24.342845
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    class Sub(PkgMgr):
        def is_available(self):
            pass
    
    assert Sub().is_available() == None



# Generated at 2022-06-13 02:11:30.775427
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class DummyPkgMgr(PkgMgr):
        def __init__(self):
            super(DummyPkgMgr, self).__init__()

        def is_available(self):
            return True

        def list_installed(self):
            return ['dummy_package']

        def get_package_details(self, package):
            package_details = {'name': package, 'version': '1.0'}
            return package_details

    dummy_pkg_mgr = DummyPkgMgr()
    result = dummy_pkg_mgr.get_package_details('dummy_package')
    assert result == {'name': 'dummy_package', 'version': '1.0', 'source': 'dummy_pkg_mgr'}


# Generated at 2022-06-13 02:11:34.205026
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # Set up test
    class P(LibMgr):
        LIB = 'openssl'

    obj = P()

    # Run test
    result = obj.is_available()

    # Verify result
    assert result



# Generated at 2022-06-13 02:11:37.225032
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    
    PkgMgr.get_package_details('unimplemented!')
    assert False, 'PkgMgr.get_package_details not implemented, should have raised NotImplementedError'

# Generated at 2022-06-13 02:11:47.867881
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.basic import AnsibleModule

    ansible_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

    # Mock the list_installed and get_package_details methods of PkgMgr class
    def mock_list_installed(self):
        return ["python2.7", "python3.6", "python3.7"]

    def mock_get_package_details(self, package):
        if package == "python2.7":
            return {"name": "python2.7", "version": "2.7.12"}
        elif package == "python3.6":
            return {"name": "python3.6", "version": "3.6.8"}

# Generated at 2022-06-13 02:11:52.155113
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    libmgr = LibMgr()
    # this class requires overriding self.LIB
    assert not libmgr.is_available()
    libmgr.LIB = 'this_lib_doesnt_exist'
    assert not libmgr.is_available()
    libmgr.LIB = 'socket'
    assert libmgr.is_available()


# Generated at 2022-06-13 02:11:55.301687
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    cliObj = CLIMgr()
    assert cliObj.CLI == None
    assert cliObj.is_available() == True

# Generated at 2022-06-13 02:11:55.822515
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pass

# Generated at 2022-06-13 02:12:06.481815
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class PkgMgr_test(PkgMgr):
        def list_installed(self):
            return [{'name': 'a', 'version': '1.0', 'source': 'yum'}, {'name': 'b', 'version': '0.1', 'source': 'pip'}]

        def get_package_details(self, package):
            return package
    pkg_mgr_test_instance = PkgMgr_test()
    assert pkg_mgr_test_instance.get_packages() == {'a': [{'name': 'a', 'version': '1.0', 'source': 'yum'}], 'b': [{'name': 'b', 'version': '0.1', 'source': 'pip'}]}

# Generated at 2022-06-13 02:12:09.794349
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    subclasses = get_all_subclasses(LibMgr)
    for obj in subclasses:
        try:
            assert obj().is_available() == True
        except ValueError:
            assert obj().is_available() == False


# Generated at 2022-06-13 02:12:24.577750
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    has_python3 = True
    try:
        import python3
    except ImportError:
        has_python3 = False
    assert has_python3 is False

# Generated at 2022-06-13 02:12:26.697651
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    example = CLIMgr()
    assert example._cli is None


# Generated at 2022-06-13 02:12:30.514469
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class TestListMgr(PkgMgr):
        def list_installed(self):
            return ['package1', 'package2']
    assert TestListMgr().list_installed() == ['package1', 'package2']


# Generated at 2022-06-13 02:12:38.857280
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # Create an object of class PkgMgr
    class DummyPkgMgr(PkgMgr):
        def is_available(self):
            pass
        def list_installed(self):
            pass
        def get_package_details(self, package):
            package_details = {}
            package_details['name'] = 'dummy'
            package_details['version'] = '1.0'
            return package_details
    dummy_pkg_mgr = DummyPkgMgr()
    # Test get_packages method
    packages = dummy_pkg_mgr.get_packages()
    assert isinstance(packages, dict)
    assert len(packages.keys()) == 1
    assert packages['dummy'][0]['source'] == 'dummypkgmgr'
    assert packages['dummy'][0]['name']

# Generated at 2022-06-13 02:12:41.829329
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    test_obj = PkgMgr()
    assert not test_obj.is_available()


# Generated at 2022-06-13 02:12:43.157972
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cm = CLIMgr()
    assert cm.is_available() == False



# Generated at 2022-06-13 02:12:44.492567
# Unit test for constructor of class LibMgr
def test_LibMgr():
    cls = LibMgr()
    assert cls



# Generated at 2022-06-13 02:12:50.437004
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class CustomPkgMgr(PkgMgr):
        def is_available(self):
            pass
        def list_installed(self):
            return [{
                'name': 'a',
                'version': '1'
            }]
        def get_package_details(self, package):
            return package

    pkgMgr = CustomPkgMgr()
    packages = pkgMgr.get_packages()
    assert packages == {'a': [{'name': 'a', 'version': '1'}]}

# Generated at 2022-06-13 02:12:52.250302
# Unit test for constructor of class LibMgr
def test_LibMgr():
    l = LibMgr()
    l._lib = None
    assert l._lib == None

# Generated at 2022-06-13 02:12:56.730882
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    import unittest

    class TestCLIMgr(unittest.TestCase):

        def setUp(self):
            self.pm = CLIMgr()

        def test_constructor(self):
            self.assertIsNone(self.pm._cli)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCLIMgr)
    unittest.TextTestRunner(verbosity=2).run(suite)


# Generated at 2022-06-13 02:13:35.237568
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    """
    Test is_available method of LibMgr class
    """
    import sys
    import mock
    import os

    sys.modules['json'] = mock.Mock()
    sys.modules['pip'] = mock.Mock()
    sys.modules['setuptools'] = mock.Mock()
    sys.modules['pkg_resources'] = mock.Mock()

    os.environ['GPG_TTY'] = mock.Mock()

    from ansible.module_utils.facts.system.pkg_mgr import LibMgr as LibMgrTest

    LIB_MGR_TEST = LibMgrTest

    LIB_MGR_TEST.LIB = 'json'
    LibMgrTest_object = LibMgrTest()
    LibMgrTest_obj = LibMgrTest_object.is_available()

# Generated at 2022-06-13 02:13:37.541338
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

    cm = CLIMgr()
    assert cm.CLI is None
    assert cm._cli is None

# Generated at 2022-06-13 02:13:39.013947
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lm = LibMgr()
    assert lm.is_available() is False


# Generated at 2022-06-13 02:13:43.976696
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class CLIMgr_test(CLIMgr):
        CLI = 'test_CLI'

    CLI_path = '/bin/test'
    CI_path = '/bin/test_not_exists'
    CI_test = CLIMgr_test()
    try:
        CI_test._cli = get_bin_path(CLIMgr_test.CLI)
        assert CI_test.CLI == CI_test._cli
        assert CI_test.is_available()
    except ValueError:
        assert False
    try:
        CI_test._cli = get_bin_path(CLIMgr_test.CLI)
        assert CI_test.CLI != CI_test._cli
        assert CI_test.is_available()
    except ValueError:
        assert True

# Generated at 2022-06-13 02:13:48.771873
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # is_available should return True if the CLI is found in $PATH
    class TestCLIMgr(CLIMgr):
        CLI = 'foo'
    assert TestCLIMgr().is_available() == False
    # is_available should return False if the CLI is not found in $PATH

    class TestCLIMgr(CLIMgr):
        CLI = 'ls'
    assert TestCLIMgr().is_available() == True
    # is_available should keep a reference to the CLI path once it's found in $PATH

# Generated at 2022-06-13 02:13:49.216485
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pass

# Generated at 2022-06-13 02:13:49.720677
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pass

# Generated at 2022-06-13 02:13:51.358863
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    """
    This method tests the CLIMgr is_available method.
    """
    assert CLIMgr.is_available()


# Generated at 2022-06-13 02:13:52.834465
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    
    assert isinstance(type(PkgMgr.list_installed(PkgMgr)), object)


# Generated at 2022-06-13 02:13:55.160845
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    """
    PkgMgr: test list_installed
    """
    pkg_mgr = PkgMgr()
    assert pkg_mgr.list_installed() is None


# Generated at 2022-06-13 02:15:09.100366
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    assert LibMgr.is_available(LibMgr) == True


# Generated at 2022-06-13 02:15:14.742165
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import os

    class FakePkgMgr(PkgMgr):

        def __init__(self):
            self.ansible_pkgs = {}

        def is_available(self):
            return True

        def list_installed(self):
            return self.ansible_pkgs.keys()

        def get_package_details(self, package):
            return self.ansible_pkgs[package]

    fpm = FakePkgMgr()
    fpm.ansible_pkgs = {'foo': {'name': 'bar', 'version': '0.0.1'}}

    assert fpm.get_packages() == {'bar': [{'name': 'bar', 'version': '0.0.1', 'source': 'fakepkgmgr'}]}

    # Simulating an error during 'get_package_

# Generated at 2022-06-13 02:15:18.492411
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    try:
        class Test_CLIMgr(CLIMgr):
            CLI = 'test_bin'
        obj = Test_CLIMgr()
        assert obj._cli is None
    except Exception:
        raise Exception('test_CLIMgr failed')


# Generated at 2022-06-13 02:15:19.672192
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    manager = CLIMgr()
    assert manager.is_available() is None

# Generated at 2022-06-13 02:15:20.858057
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cm = CLIMgr()
    assert cm is not None


# Generated at 2022-06-13 02:15:23.139219
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    climgr = CLIMgr()
    assert climgr._cli == None
    
# unit test for is_available function in CLIMgr

# Generated at 2022-06-13 02:15:24.670394
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    """
    Mocked test function to test list_installed method of class PkgMgr
    :return: return True if success else False
    """
    pass

# Generated at 2022-06-13 02:15:25.752703
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    l = PkgMgr()
    l.get_packages()



# Generated at 2022-06-13 02:15:27.443131
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cli = CLIMgr()
    assert cli.is_available()

# Generated at 2022-06-13 02:15:35.217976
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # Test for a successful import of python library
    # Mocking object to test, this class would inherit from LibMgr
    class MockLibMgr(LibMgr):
        LIB = 'mock_lib'

    mock_LibMgr = MockLibMgr()
    try:
        assert mock_LibMgr.is_available()
    except ImportError:
        assert False
    # Test for no available python library
    class NoLibMgr(LibMgr):
        LIB = 'no_lib'

    no_LibMgr = NoLibMgr()
    assert not no_LibMgr.is_available()


# Generated at 2022-06-13 02:18:14.414752
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    assert CLIMgr.is_available(None) is False


# Generated at 2022-06-13 02:18:14.894212
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pass

# Generated at 2022-06-13 02:18:22.662406
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class FakePkgMgr(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return ['fakepackage1', 'fakepackage2']

        def get_package_details(self, package):
            if package == 'fakepackage1':
                return {
                    'name': 'fakepackage1',
                    'release': '1.0',
                    'vendor': 'fakevendor1',
                    'arch': 'fakearch1',
                    'install_date': '2017-06-21T19:39:46Z',
                    'description': 'fakedescription1'
                }

# Generated at 2022-06-13 02:18:29.501553
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import sys
    import psutil
    L = LibMgr()
    cls, cls_name = L.__class__, L.__class__.__name__
    assert cls_name in ['LibMgr'], 'The class name %s must equal LibMgr' % cls_name
    is_avail = L.is_available()
    assert is_avail == False, 'The is_available() method must return False by default'
    if sys.version_info[0] == 2:
        L._lib = psutil
    else:
        L.LIB = 'psutil'
    is_avail = L.is_available()
    assert is_avail == True, 'The is_available() method must return True if the library is properly imported'


# Generated at 2022-06-13 02:18:31.785853
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    class PkgMgrTest(PkgMgr):
        pass

    pkgmgrtest = PkgMgrTest()

    assert pkgmgrtest.is_available() == None


# Generated at 2022-06-13 02:18:33.421746
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():

    assert PkgMgr.list_installed()


# Generated at 2022-06-13 02:18:36.600837
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    for cli in get_all_pkg_managers().values():
        obj = cli()
        assert isinstance(obj, CLIMgr), "CLIMgr instance is not of type PkgMgr"

# Generated at 2022-06-13 02:18:37.418135
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pass


# Generated at 2022-06-13 02:18:38.514416
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cm=CLIMgr()
    assert cm._cli == None



# Generated at 2022-06-13 02:18:44.149900
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    import datetime
    from ansible.module_utils._text import to_bytes

    mgr = LibMgr()
    assert mgr.is_available() is False

    # Test for ValueError exception
    mgr.LIB = "datetime"
    assert mgr.is_available() is True

    # Test for ImportError exception by importing random module
    mgr.LIB = "random"
    assert mgr.is_available() is False

    # Test that the module has been loaded as requested
    mgr.LIB = "datetime"
    mgr.is_available()
    assert mgr._lib == datetime

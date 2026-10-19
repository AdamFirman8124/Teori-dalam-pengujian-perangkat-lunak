

# Generated at 2022-06-13 02:09:22.146610
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.software_detection import PkgMgr
    def _is_available():
        return True
    def _list_installed():
        return [{'name': 'pkg1'}]
    def _get_package_details(package):
        return {'name': package['name']}

    pm = PkgMgr()
    pm.list_installed = _list_installed
    pm.get_package_details = _get_package_details
    pm.is_available = _is_available
    assert pm.get_packages() == {'pkg1': [{'name': 'pkg1'}]}

# Generated at 2022-06-13 02:09:28.991727
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    assert 'dpkg' in get_all_pkg_managers()
    assert 'apk' in get_all_pkg_managers()
    assert 'pip' in get_all_pkg_managers()
    assert 'gem' in get_all_pkg_managers()
    assert 'port' in get_all_pkg_managers()
    assert 'apk' in get_all_pkg_managers()
    assert 'portage' in get_all_pkg_managers()
    assert 'pkgng' in get_all_pkg_managers()
    assert 'yum' in get_all_pkg_managers()

# Generated at 2022-06-13 02:09:31.627680
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    for pkg_mgr in get_all_pkg_managers().values():
        assert pkg_mgr().is_available()


# Generated at 2022-06-13 02:09:32.622908
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert CLIMgr().is_available() is False

# Generated at 2022-06-13 02:09:39.756951
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    test_data = [{u'name': u'ccm', u'source': 'apt', u'version': u'2.0.1-2'},
                 {u'name': u'python-crypto', u'source': 'apt', u'version': u'2.6.1-6'}]
    test_result = {u'ccm': [{u'name': u'ccm', u'source': 'apt', u'version': u'2.0.1-2'}], u'python-crypto': [{u'name': u'python-crypto', u'source': 'apt', u'version': u'2.6.1-6'}]}

# Generated at 2022-06-13 02:09:42.367639
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    # Test for import a lib that does not exists
    class Test1(LibMgr):
        LIB = "nothere"
    assert not Test1().is_available()


# Generated at 2022-06-13 02:09:50.351182
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import json
    import unittest

    class MockPkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return json.loads("""
                [
                    {
                        "name": "foo",
                        "version": "1"
                    },
                    {
                        "name": "bar",
                        "version": "1"
                    },
                    {
                        "name": "foo",
                        "version": "2"
                    }
                ]
            """)

        def get_package_details(self, package):
            return package

    class TestPkgMgr(unittest.TestCase):
        def test_get_packages(self):
            mock_module = MockPkgMgr()

# Generated at 2022-06-13 02:09:52.503180
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    try:
        import packaging
        found = True
    except ImportError:
        found = False
    assert found == True


# Generated at 2022-06-13 02:09:59.772848
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    try:
        from importlib import import_module
        lm = LibMgr()
        # set the LIB variable
        lm.LIB = import_module("ansible.module_utils.software_rng_utils.pkg_managers.yum").LIB
        # test the method is_available
        print("LibMgr is available.")
        assert(lm.is_available())
    except ImportError:
        print("LibMgr is not available.")
        assert(not lm.is_available())


# Generated at 2022-06-13 02:10:01.839502
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class TestCLIMgr(CLIMgr):
        CLI = 'test'
    assert TestCLIMgr().CLI == 'test'

# Generated at 2022-06-13 02:10:12.660042
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    # Create a mock sublcass of class PkgMgr with methods is_available, list_installed and get_package_details
    class PkgMgrMock(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['package1', 'package2']

        def get_package_details(self, package):
            ret = {'name': package, 'version': '1.0'}
            return ret

    # Create an object of class PkgMgrMock
    pm_mock = PkgMgrMock()
    # The method returns a dictionary of lists of dictionaries (package = list of installed versions)
    ret = pm_mock.get_packages()

# Generated at 2022-06-13 02:10:13.643798
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert(CLIMgr() != None)

# Generated at 2022-06-13 02:10:23.863335
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # Create a dummy subclass of PkgMgr
    class DummyPkgMgr(PkgMgr):
        def is_available(self):
            pass
        def list_installed(self):
            return ['pkg1', 'pkg2', 'pkg3']
        def get_package_details(self, package):
            # We can return different packages with different versions
            if package == 'pkg1':
                return {'name': package, 'version': '1.0.0'}
            elif package == 'pkg3':
                return {'name': package, 'version': '3.0.0'}
            # If a package version is not specified, it is assumed to be None
            else:
                return {'name': package}

    dpm = DummyPkgMgr()
    packages = dpm.get_packages()


# Generated at 2022-06-13 02:10:25.484675
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    climgr = CLIMgr()
    assert CLIMgr.CLI is None

# Generated at 2022-06-13 02:10:28.480354
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pm = PkgMgr()
    try:
        package_details = pm.get_package_details("package")
    except NotImplementedError:
        pass
    else:
        raise Exception("test_PkgMgr_get_package_details failed")


# Generated at 2022-06-13 02:10:32.650616
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lm = LibMgr()
    assert not lm._lib
    lm.LIB = "os"
    assert lm.is_available()


# Generated at 2022-06-13 02:10:37.865641
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # Create a new temporary class extending CLIMgr and test is_available()
    temporary_class = type('test_CLIMgr_is_available', (CLIMgr,), {'CLI': '/usr/bin/apt-get'})
    temporary_obj = temporary_class()
    answer = temporary_obj.is_available()
    assert answer == True


# Generated at 2022-06-13 02:10:40.888431
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    t1 = PkgMgr()
    assert t1.is_available() == False
    t1 = CLIMgr()
    assert t1.is_available() == False


# Generated at 2022-06-13 02:10:43.687166
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    try:
        import pip
        assert pip is not None
        return True
    except ImportError:
        return False


# Generated at 2022-06-13 02:10:47.713826
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class FakeLibMgr(LibMgr):
        LIB = '_test_'
    fakeLibMgr = FakeLibMgr()
    fakeLibMgr._lib = '_test_'
    assert fakeLibMgr.is_available()


# Generated at 2022-06-13 02:11:02.435102
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    try:
        get_all_pkg_managers().get('applepkg').list_installed()
    except AttributeError:
        assert False

    try:
        get_all_pkg_managers().get('aptpkg').list_installed()
    except AttributeError:
        assert False

    try:
        get_all_pkg_managers().get('dnfpkg').list_installed()
    except AttributeError:
        assert False

    try:
        get_all_pkg_managers().get('eoppkg').list_installed()
    except AttributeError:
        assert False

    try:
        get_all_pkg_managers().get('freebsdpkg').list_installed()
    except AttributeError:
        assert False


# Generated at 2022-06-13 02:11:04.527256
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pkgmgr = PkgMgr()
    ret = pkgmgr.is_available()
    assert ret is None


# Generated at 2022-06-13 02:11:13.928302
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    import mock

    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True

    class TestPkgMgrException(PkgMgr):
        def is_available(self):
            raise Exception


    class TestPkgMgrListInstalled(unittest.TestCase):
        def test_list_installed(self):
            test_pkg = TestPkgMgr()
            with mock.patch('ansible_collections.notstdlib.moveitallout.plugins.module_utils.common.server_specific.list_installed_packages.PkgMgr.list_installed') as list_installed:
                list_installed.return_value = 'test_value'


# Generated at 2022-06-13 02:11:16.784638
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class TestCLIMgr(CLIMgr):
        CLI = 'test'
    class TestCLIMgr2(CLIMgr):
        CLI = 'cat'
    assert TestCLIMgr().is_available() == True
    assert TestCLIMgr2().is_available() == True


# Generated at 2022-06-13 02:11:18.157738
# Unit test for constructor of class LibMgr
def test_LibMgr():
    with open ("junk.txt", "w") as f:
        assert True

# Generated at 2022-06-13 02:11:27.956492
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    formatted_result_dict = {}
    formatted_result_dict['name'] = 'Cython'
    formatted_result_dict['version'] = '0.22'
    formatted_result_dict['status'] = 'present'
    formatted_result_dict['pkg_manager'] = 'pip'

    test_package = 'cython==0.22'
    test_pip_mgr = CLIMgr()
    test_pip_mgr.CLI = 'pip'
    test_pip_mgr.is_available()
    test_pip_mgr.list_installed = lambda: [test_package]
    test_pip_mgr.get_package_details = lambda package: formatted_result_dict

# Generated at 2022-06-13 02:11:29.383782
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    test_mgr = PkgMgr()
    assert test_mgr.get_packages() == {}


# Generated at 2022-06-13 02:11:32.480084
# Unit test for constructor of class LibMgr
def test_LibMgr():

    class test(LibMgr):
        LIB = 'os'

    t1 = test()
    assert t1.is_available() == True


# Generated at 2022-06-13 02:11:35.230644
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    c = CLIMgr()
    c._cli = None
    assert c.is_available() == False
    c._cli = '/usr/bin/test'
    assert c.is_available() == True

# Generated at 2022-06-13 02:11:37.826516
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.facts.pkg_mgr.python import PythonPip
    assert not LibMgr().is_available()
    assert PythonPip().is_available()


# Generated at 2022-06-13 02:11:42.629239
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pass

# Generated at 2022-06-13 02:11:52.429019
# Unit test for function get_all_pkg_managers

# Generated at 2022-06-13 02:12:01.024544
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    all_pkg_managers = get_all_pkg_managers()
    assert isinstance(all_pkg_managers, dict)
    assert all([isinstance(k, str) for k, v in all_pkg_managers.items()])
    assert all([isinstance(v, type) for k, v in all_pkg_managers.items()])
    assert all([isinstance(v, (CLIMgr, LibMgr)) for k, v in all_pkg_managers.items()])

# Generated at 2022-06-13 02:12:01.625837
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pass

# Generated at 2022-06-13 02:12:04.601376
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class TestCLIMgr(CLIMgr):
        CLI = 'test_CLI'
    test_CLIMgr = TestCLIMgr()
    assert test_CLIMgr is not None


# Generated at 2022-06-13 02:12:14.329747
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.common._pkg_mgrs import RPM, Yum, YumLib, Apt, AptLib, Miktex
    rpmlib = RPM()
    assert isinstance(rpmlib, RPM), 'RPM class is not a subclass of PkgMgr class'
    assert isinstance(rpmlib, Yum), 'RPM class is not a subclass of Yum class'
    assert isinstance(rpmlib, YumLib), 'RPM class is not a subclass of YumLib class'
    assert isinstance(rpmlib, CLIMgr), 'RPM class is not a subclass of CLIMgr class'
    assert isinstance(rpmlib, LibMgr), 'RPM class is not a subclass of LibMgr class'

# Generated at 2022-06-13 02:12:15.932178
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():

    package_list = PkgMgr().list_installed()
    assert not package_list


# Generated at 2022-06-13 02:12:20.101404
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    avail_pkgers = get_all_pkg_managers()
    unavail_pkgers = {k: v for k, v in avail_pkgers.items() if not v().is_available()}
    avail_pkgers = {k: v for k, v in avail_pkgers.items() if v().is_available()}



# Generated at 2022-06-13 02:12:23.910029
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    dummy_mgr = CLIMgr()

    assert dummy_mgr.is_available() == False
    assert dummy_mgr.CLI == None

    dummy_mgr.CLI = "/usr/bin/clitool"
    assert dummy_mgr.is_available() == True

    try:
        get_bin_path("/usr/bin/clitool_raise")
    except ValueError as e:
        pass



# Generated at 2022-06-13 02:12:29.199922
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.common.text_utils import to_bytes
    from ansible.module_utils.common.sys_info import PkgMgr
    from ansible.module_utils.common.sys_info import CLIMgr
    from ansible.module_utils.common.sys_info import LibMgr

    import sys
    import tempfile
    import shutil
    import os

    # All the classes that exist in the ansible.module_utils.common.sys_info module will be available
    # in the sys_info variable to override the methods
    sys_info = sys.modules['ansible.module_utils.common.sys_info']
    # Tempdir is used to store the files generated in the test
    tempdir = tempfile.mkdtemp(prefix='ansible_test_')


# Generated at 2022-06-13 02:12:40.733097
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    # Test for a class with a constructor
    class Test(CLIMgr):
        pass

    assert Test()._cli is None

# Generated at 2022-06-13 02:12:49.807726
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import unittest
    import mock

    # Mock the PkgMgr class
    class MockPkgMgr(object):

        pass

    # instantiate class PkgMgr
    m_pm = MockPkgMgr()

    # mock the list_installed method
    def mocked_list_installed():
        return ['un' + str(i) for i in range(5)]

    # mock the get_package_details method
    def mocked_get_package_details(item):
        package_details = {'name': item, 'version': item[2:]}
        return package_details

    m_pm.list_installed = mocked_list_installed
    m_pm.get_package_details = mocked_get_package_details

    result_dict = m_pm.get_packages()

# Generated at 2022-06-13 02:12:52.261412
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    lib = CLIMgr()
    lib.CLI = 'python'
    assert lib.is_available()

# Generated at 2022-06-13 02:12:53.836831
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    pmgr = PkgMgr()
    assert pmgr.is_available() == False


# Generated at 2022-06-13 02:12:57.261177
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    c = CLIMgr()
    try:
        c.is_available()
    except TypeError:
        pass
    else:
        assert False, "Expected class CLIMgr to require CLI to be defined"


# Generated at 2022-06-13 02:12:58.446671
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    assert 0, "Skipping 'test_PkgMgr_get_package_details'."

# Generated at 2022-06-13 02:13:05.231236
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class MockPkgMgr(PkgMgr):
        @classmethod
        def is_available(cls):
            return True


# Generated at 2022-06-13 02:13:06.530484
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    testMgr = CLIMgr()
    assert testMgr is not None


# Generated at 2022-06-13 02:13:07.707313
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    t = LibMgr()
    assert t.is_available() == False

# Generated at 2022-06-13 02:13:10.269426
# Unit test for constructor of class LibMgr
def test_LibMgr():

    class test_LibMgr(LibMgr):
        LIB = 'test'

    lib = test_LibMgr()
    assert lib._lib is None


# Generated at 2022-06-13 02:13:28.982893
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    obj = LibMgr()
    res = obj.is_available()
    assert res is False


# Generated at 2022-06-13 02:13:30.926338
# Unit test for constructor of class LibMgr
def test_LibMgr():
    test_libmgr = LibMgr()
    assert test_libmgr


# Generated at 2022-06-13 02:13:32.291299
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    assert PkgMgr.is_available(LibMgr) == False


# Generated at 2022-06-13 02:13:34.689590
# Unit test for constructor of class CLIMgr
def test_CLIMgr():

    class TestCLIMgr(CLIMgr):
        CLI = 'test'

    tcm = TestCLIMgr()
    assert tcm._cli is None


# Generated at 2022-06-13 02:13:37.714098
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class TestLibMgr(LibMgr):
        LIB = 'test_lib'

    tlm = TestLibMgr()
    assert tlm.LIB == 'test_lib'


# Generated at 2022-06-13 02:13:41.444284
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    # In the first case the CLI exists
    cmgr = CLIMgr()
    cmgr.CLI = "ls"
    assert cmgr.is_available()
    # In the second case the CLI does not exist
    cmgr = CLIMgr()
    cmgr.CLI = "this_command_should_never_exist_in_reality_123"
    assert cmgr.is_available() is False

# Generated at 2022-06-13 02:13:47.049728
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    test_mgr = PkgMgr()
    test_mgr.list_installed = lambda: ['test_pkg']
    test_mgr.get_package_details = lambda package: {'name': 'test_pkg', 'version': '1.0'}
    packages = test_mgr.get_packages()
    assert len(packages['test_pkg']) == 1
    assert packages['test_pkg'][0]['name'] == 'test_pkg'
    assert packages['test_pkg'][0]['version'] == '1.0'

# Generated at 2022-06-13 02:13:53.616682
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class MyPM(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['a','b','c']

        def get_package_details(self, package):
            return {'name':package, 'version':None}

    pm = MyPM()
    packages = pm.get_packages()
    assert len(packages) == 3, 'Expected number of packages %s' % len(packages)
    assert 'a' in packages, 'Expected package %s' % 'a'
    assert 'b' in packages, 'Expected package %s' % 'b'
    assert 'c' in packages, 'Expected package %s' % 'c'


# Generated at 2022-06-13 02:14:01.320947
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class TestPkgMgr(PkgMgr):

        def is_available(self):
            pass

        def list_installed(self):
            return ['package1', 'package2']

        def get_package_details(self, package):
            if package == 'package1':
                return {'name': 'package1', 'version': '1.0', 'source': 'fake'}
            elif package == 'package2':
                return {'name': 'package2', 'version': '2.0', 'source': 'fake'}
    test_pkg_mgr = TestPkgMgr()

# Generated at 2022-06-13 02:14:03.097474
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    assert get_all_pkg_managers()
    assert get_all_pkg_managers()['pip']

# Generated at 2022-06-13 02:14:53.421354
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pm = CLIMgr()
    pm.CLI = 'apt-get'
    pm.is_available()
    assert(pm._cli)
    pm.CLI = 'wrongpackage'
    assert not pm.is_available()


# Generated at 2022-06-13 02:14:59.895403
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    pkg_mgr = PkgMgr()
    pkg_mgr.list_installed = lambda: ['python2.7', 'python3']
    pkg_mgr.get_package_details = lambda pkg: {'name': pkg, 'version': '2.7' if pkg.startswith('python2') else '3'}
    exp = {'python3': [{'name': 'python3', 'version': '3', 'source': 'pkg_mgr'}],
           'python2.7': [{'name': 'python2.7', 'version': '2.7', 'source': 'pkg_mgr'}]}

    res = pkg_mgr.get_packages()

    assert res == exp

# Generated at 2022-06-13 02:15:04.620042
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    import mock
    import sys

    class DummyPkgMgr(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ["package1", "package2"]
        def get_package_details(self, package):
            if package == "package1":
                return {'name': "package1", 'version': "1.0"}
            else:
                return {'name': "package2", 'version': "2.0"}

    debug = mock.Mock()
    # get_packages
    dummy_pkg_mgr = DummyPkgMgr()

    pkgs = dummy_pkg_mgr.get_packages()
    assert len(pkgs) == 2

# Generated at 2022-06-13 02:15:07.003207
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cli = CLIMgr()
    if cli is not None:
        print("success")
    else:
        print("failure")


# Generated at 2022-06-13 02:15:16.411774
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class PkgMgrImpl(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ["foo", "bar", "baz"]
        def get_package_details(self, pkg):
            return {"name": pkg, "version": "1.0"}

    pkg_mgr = PkgMgrImpl()

    assert pkg_mgr.get_packages() == {"foo": [{"name": "foo", "version": "1.0", "source": "pkgmgrimpl"}],
                                      "bar": [{"name": "bar", "version": "1.0", "source": "pkgmgrimpl"}],
                                      "baz": [{"name": "baz", "version": "1.0", "source": "pkgmgrimpl"}]}

# Generated at 2022-06-13 02:15:17.643621
# Unit test for constructor of class LibMgr
def test_LibMgr():
    pm = LibMgr()
    assert pm._lib is None


# Generated at 2022-06-13 02:15:18.802718
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class TestLibMgr(LibMgr):
        LIB = 'datetime'

    manager = TestLibMgr()
    assert manager.is_available() == True


# Generated at 2022-06-13 02:15:21.570775
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    mock_package = 'mock_package'
    PkgMgr.get_package_details(mock_package)   # should raise NotImplementedError (abstract methods have to be implemented in child classes)


# Generated at 2022-06-13 02:15:22.722208
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cli_mgr = CLIMgr()
    assert not cli_mgr.is_available()

# Generated at 2022-06-13 02:15:29.384096
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            pass
        def list_installed(self):
            return ['a', 'b']
        def get_package_details(self, package):
            return {'name': package}
    assert TestPkgMgr().get_packages() == {
        'a': [{'name': 'a', 'source': 'TestPkgMgr'}],
        'b': [{'name': 'b', 'source': 'TestPkgMgr'}],
    }

# Generated at 2022-06-13 02:16:55.986979
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    pkg_managers = get_all_pkg_managers()
    assert 'apt_mgr' in pkg_managers
    assert 'yum_mgr' in pkg_managers
    assert 'apk_mgr' in pkg_managers

# Generated at 2022-06-13 02:17:04.024158
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import ansible.module_utils.facts.pkg_mgrs.dnf
    import ansible.module_utils.facts.pkg_mgrs.apt
    # if dnf is available, then is_available should return True
    if ansible.module_utils.facts.pkg_mgrs.dnf.DnfMgr.is_available():
        assert ansible.module_utils.facts.pkg_mgrs.dnf.DnfMgr.is_available() == True
    # if apt is available, then is_available should return True
    if ansible.module_utils.facts.pkg_mgrs.apt.AptMgr.is_available():
        assert ansible.module_utils.facts.pkg_mgrs.apt.AptMgr.is_available() == True


# Unit test

# Generated at 2022-06-13 02:17:06.663316
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pkg_managers = PkgMgr.__subclasses__()
    for pkg_manager in pkg_managers:
        if pkg_manager.is_available():
            assert pkg_manager.list_installed() is not None, "PkgMgr.list_installed failed for package manager: %s" % pkg_manager.__name__


# Generated at 2022-06-13 02:17:07.182321
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pass

# Generated at 2022-06-13 02:17:08.347994
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    assert CLIMgr().is_available() == False
    assert CLIMgr()._cli is None


# Generated at 2022-06-13 02:17:13.939832
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return []
        def get_package_details(self, package):
            return {'name': package, 'version': '1.2.3'}

    installed_packages = TestPkgMgr().get_packages()
    assert len(installed_packages) == 0


# Generated at 2022-06-13 02:17:15.031767
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert CLIMgr.is_available(CLIMgr)


# Generated at 2022-06-13 02:17:20.757327
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.common.packaging import get_package_details_yum
    from ansible.module_utils.common.packaging import list_installed_packages_yum

    class TestPkgMgr(PkgMgr):

        def __init__(self):
            super(TestPkgMgr, self).__init__()

        def is_available(self):
            return True

        def list_installed(self):
            return list_installed_packages_yum()

        def get_package_details(self, package):
            return get_package_details_yum(package)


# Generated at 2022-06-13 02:17:21.888658
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    x = CLIMgr()
    assert x is not None
    return True



# Generated at 2022-06-13 02:17:22.911723
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    a = PkgMgr()
    assert a.list_installed() == None

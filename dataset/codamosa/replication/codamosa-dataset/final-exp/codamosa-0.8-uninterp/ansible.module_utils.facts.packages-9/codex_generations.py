

# Generated at 2022-06-13 02:09:19.984578
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    results = {}
    lm = LibMgr()
    pm = PkgMgr()
    lm.list_installed = pm.list_installed = lambda: []
    lm.get_package_details = pm.get_package_details = lambda x: {'name': x, 'version': 2}
    results[type(lm).__name__] = lm.get_packages()
    results[type(pm).__name__] = pm.get_packages()

    assert results == {'LibMgr': {}, 'PkgMgr': {}}

# Generated at 2022-06-13 02:09:23.241486
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class LibMgrTest(LibMgr):

        LIB = 'shutil'

    lm = LibMgrTest()
    assert(lm.is_available() == True)


# Generated at 2022-06-13 02:09:32.845506
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class PkgMgrTest(PkgMgr):
        def __init__(self):
            super(PkgMgrTest, self).__init__()

        def is_available(self):
            return True


# Generated at 2022-06-13 02:09:42.418977
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    class TestPkgMgr(PkgMgr):

        def __init__(self):
            super(TestPkgMgr, self).__init__()

        def is_available(self):
            return False

        def list_installed(self):
            return []

        def get_package_details(self, package):
            return []

    class TestCLIMgr(CLIMgr):

        CLI = '/usr/bin/test'

        def __init__(self):
            super(TestCLIMgr, self).__init__()

        def list_installed(self):
            return []

        def get_package_details(self, package):
            return []

    class TestLibMgr(LibMgr):

        LIB = 'test'

        def __init__(self):
            super(TestLibMgr, self).__init

# Generated at 2022-06-13 02:09:53.484825
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.facts.system.pkg_mgr import CLIMgr
    from mock import Mock
    from ansible.module_utils.common._utils import get_bin_path

    ansible_module = Mock()
    cli_mgr = CLIMgr()
    cli_mgr.CLI = 'dummy_cli'
    cli_mgr._cli = 'dummy_cli_path'
    ansible_module.ansible_facts = {}
    ansible_module.ansible_facts['ansible_pkg_mgr'] = cli_mgr

    # test of false condition
    cli_mgr.CLI = 'non_existing_cli'

# Generated at 2022-06-13 02:09:57.252409
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    # Test to make sure is_available method raises TypeError
    # It should raise a TypeError because PkgMgr class is an abstract
    # base class and is not instantiable
    try:
        pm = PkgMgr()
        assert(False)
    except TypeError:
        assert(True)
    return True

# Generated at 2022-06-13 02:09:59.476146
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    """
    Test the constructor of class CLIMgr
    """
    c = CLIMgr()
    assert c._cli == None


# Generated at 2022-06-13 02:10:00.486585
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert CLIMgr().is_available() == False

# Generated at 2022-06-13 02:10:02.831994
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():

    class CLIMgrTest(CLIMgr):
        CLI = "apt-get"

    apt = CLIMgrTest()
    assert apt.is_available()

# Generated at 2022-06-13 02:10:08.749938
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pkg_mgr_list = get_all_pkg_managers()
    for cls in pkg_mgr_list.values():
        try:
            assert(isinstance(cls(), CLIMgr) or isinstance(cls(), LibMgr))
            obj = cls()
            assert(isinstance(obj, CLIMgr) or isinstance(obj, LibMgr))
            assert(obj.is_available())
        except AssertionError:
            print("Assertion failed: %s class is not a subclass of CLIMgr or LibMgr" % cls.__name__)

# Generated at 2022-06-13 02:10:22.821678
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    # Tests to check for correct
    class dummy_PkgMgr(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return ['nginx','apache2','apache2-utils','apache2-bin']

        def get_package_details(self, package):
            if package == 'nginx':
                return {'name': package}
            elif package == 'apache2':
                return {'name': package, 'version': '2.4'}
            elif package == 'apache2-utils':
                return {'name': package, 'version': '2.4'}
            elif package == 'apache2-bin':
                return {'name': 'apache2', 'version': '2.4'}

    # Package name is missing from the details returned from Pkg

# Generated at 2022-06-13 02:10:24.750848
# Unit test for constructor of class LibMgr
def test_LibMgr():
    """
    Check the constructor of class LibMgr
    """

    # Check the constructor of class LibMgr
    assert LibMgr


# Generated at 2022-06-13 02:10:28.479972
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    """
    Test LibMgr.is_available() method
    """
    class TestPkgMgr(LibMgr):
        LIB = 'os'

    pkgmgr = TestPkgMgr()
    found = pkgmgr.is_available()
    assert found
    assert pkgmgr._lib


# Generated at 2022-06-13 02:10:31.889234
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    pk = CLIMgr()
    assert not pk.is_available()


# Generated at 2022-06-13 02:10:34.610162
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # Asserts that the method get_packages of class PkgMgr returns a dict containing a list of dicts.
    pkg = PkgMgr()
    packages = pkg.get_packages()
    assert isinstance(packages, dict)
    for package_list in packages.values():
        assert isinstance(package_list, list)
        for package in package_list:
            assert isinstance(package, dict)

# Generated at 2022-06-13 02:10:35.975716
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    obj = PkgMgr()
    assert obj.is_available() is None

# Generated at 2022-06-13 02:10:46.903560
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():

    import unittest
    import ansible.module_utils.common.collectors.system.pip

    class TestPip(ansible.module_utils.common.collectors.system.pip.Pip):

        def get_installed_packages(self):
            return [

                {
                    "name": "ansible",
                    "version": "2.7.5",
                    "support_level": "core"
                }
            ]

    from ansible.module_utils.common.collectors.system.pip import Pip

    pip = TestPip()
    assert pip.list_installed() == [
        {
            "name": "ansible",
            "version": "2.7.5",
            "support_level": "core"
        }
    ]

    pip = Pip()
    assert pip.list_

# Generated at 2022-06-13 02:10:49.566919
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class LibMgrTest(LibMgr):
        pass

    lm_test = LibMgrTest()
    assert lm_test._lib is None


# Generated at 2022-06-13 02:10:59.065914
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from os import path
    from importlib.util import find_spec
    from ansible.module_utils._text import to_bytes

    print("Testing LibMgr is_available")
    if find_spec("yaml") is None:
        print("Testing LibMgr is_available failed : yaml library not installed")
        return 1
    lib = LibMgr()
    lib.LIB = "yaml"
    if lib.is_available():
        print("Testing LibMgr is_available passed")
    else:
        print("Testing LibMgr is_available failed : yaml library installed but return False")
    return 0


# Generated at 2022-06-13 02:11:02.987783
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert get_bin_path('yum') is not None
    assert get_bin_path('pip3') is not None
    assert get_bin_path('yum') is not None
    assert get_bin_path('dpkg') is not None
    assert get_bin_path('zypper') is not None


# Generated at 2022-06-13 02:11:12.634918
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class Mgr(LibMgr):
        LIB = 'os'
    pkg = Mgr()
    assert pkg.is_available()


# Generated at 2022-06-13 02:11:13.968471
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert(PkgMgr.is_available is PkgMgr)


# Generated at 2022-06-13 02:11:15.317949
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pkg_mgr = PkgMgr()
    assert callable(pkg_mgr)


# Generated at 2022-06-13 02:11:17.266448
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    cli_mgr = CLIMgr()
    assert cli_mgr is not None
    assert cli_mgr.CLI is None

# Generated at 2022-06-13 02:11:21.667822
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    from ansible.module_utils.facts.pkg_mgr import PkgMgr
    pkg_mgr = PkgMgr()
    pkg_mgr.is_available()
    pkg_list = pkg_mgr.list_installed()
    assert pkg_list is not None

# Generated at 2022-06-13 02:11:24.047280
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    test_obj = CLIMgr()
    assert test_obj._cli is None


# Generated at 2022-06-13 02:11:28.220410
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():

    mgrs = get_all_pkg_managers()
    assert mgrs.keys() == ['pip', 'gem', 'chocolatey', 'npm', 'apt', 'yum', 'dnf', 'zypper'], "Available pkg managers do not match"

# Generated at 2022-06-13 02:11:29.180529
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    lm = LibMgr()
    assert not lm.is_available()


# Generated at 2022-06-13 02:11:30.534976
# Unit test for constructor of class LibMgr
def test_LibMgr():

    class TestLibMgr(LibMgr):
        LIB = 'module_utils.common.test'

    the_object = TestLibMgr()
    assert the_object._lib is None


# Generated at 2022-06-13 02:11:31.772656
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lm = LibMgr()
    assert lm

# Generated at 2022-06-13 02:11:54.640530
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    print("Testing PkgMgr.get_packages")
    # Tests get_packages
    #
    # Sample output :
    #[root@ansible-maven-test-node ~]# dnf list --installed | grep ansible-maven | awk '{print $1}'
    #ansible-maven-1.0.1-1.el7.noarch
    #[root@ansible-maven-test-node ~]# dnf list --installed | grep ansible-maven | awk '{print $1"-"$2}'
    #ansible-maven-1.0.1-1.el7.noarch
    #[root@ansible-maven-test-node ~]# dnf list --installed | grep ansible-maven | awk '{print $1"

# Generated at 2022-06-13 02:11:56.231527
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lm = LibMgr()
    assert lm.LIB is None


# Generated at 2022-06-13 02:12:04.556099
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class _TestClass(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ['testpackage']
        def get_package_details(self, package):
            return {'name': 'testpackage', 'version': '1.0'}
    _testobj = _TestClass()
    assert _testobj.get_packages() == {'testpackage': [{'name': 'testpackage', 'version': '1.0', 'source': '_testclass'}]}

# Generated at 2022-06-13 02:12:09.508029
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import shutil
    try:
        cli = '/tmp/test_is_available'
        shutil.copy2('/bin/ls', cli)
        test_pkg_mgr = CLIMgr()
        test_pkg_mgr.CLI = 'test_is_available'
        assert test_pkg_mgr.is_available() == True
    finally:
        os.remove(cli)

# Generated at 2022-06-13 02:12:10.913743
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert PkgMgr.is_available('') is False
        

# Generated at 2022-06-13 02:12:19.401922
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    '''Testing get_packages method of class PkgMgr'''
    __test__ = True
    import os
    import json
    import pytest

    # Get all package managers
    pkg_mgrs = get_all_pkg_managers()
    # Get package managers from environment variable
    test_pkg_mgrs = os.environ.get('pkg_mgrs')
    # Get package managers from json file
    if test_pkg_mgrs is None:
        pkg_mgr_file = os.environ.get('pkg_mgr_file')
        if pkg_mgr_file is not None:
            with open(pkg_mgr_file) as json_file:
                test_pkg_mgrs = json.load(json_file)

# Generated at 2022-06-13 02:12:21.131701
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    p = PkgMgr()
    p._cli = '/usr/bin/which'
    assert p.is_available() == True


# Generated at 2022-06-13 02:12:23.584649
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.tests._fixtures.pkg_mgr import TestLibMgr
    pkg_mgr = TestLibMgr()
    assert pkg_mgr.is_available() == True


# Generated at 2022-06-13 02:12:35.346796
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    package_names_list = ['package1', 'package2', 'package3', 'package4', 'package5']
    package_info_dict = {}
    packages = ['package1-1.0.0', 'package2-2.0.0', 'package3-3.0.0', 'package4-4.0.0', 'package5-5.0.0']
    for package in packages:
        package_dict = {}
        package_dict['name'] = package.split('-')[0]
        package_dict['version'] = package.split('-')[1]
        package_dict['source'] = 'This is a test'
        package_info_dict[package] = package_dict
    pm = PkgMgr()
    pm.list_installed = lambda: package_names_list
    pm.get_

# Generated at 2022-06-13 02:12:37.415635
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    # method is_available should return true if a the module is available
    assert CLIMgr().is_available()
    assert LibMgr().is_available()

# Generated at 2022-06-13 02:13:10.109668
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    import ansible.module_utils.common.collections
    pkg = CLIMgr()
    assert pkg.is_available() == False
    assert pkg._cli is None

# Generated at 2022-06-13 02:13:14.348489
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    pkg_managers = get_all_pkg_managers()
    for pkg_mgr in pkg_managers:
        cli_mgr = pkg_managers[pkg_mgr]()
        if cli_mgr.CLI is not None:
            cli = getattr(cli_mgr, '_cli', None)
            res = cli_mgr.is_available()
            assert res is True
            assert cli is not None


# Generated at 2022-06-13 02:13:18.644678
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():

    class Dummy1(CLIMgr):
        CLI = ''

        def list_installed(self):
            return ['test_package1', 'test_package2']

    dummy1 = Dummy1()
    assert dummy1.list_installed() == ['test_package1', 'test_package2']


# Generated at 2022-06-13 02:13:21.231531
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():

    def test_function():

        # If system or python haven't got all of these installed, this will fail...hard
        assert len(get_all_pkg_managers()) == 20

    test_function()

# Generated at 2022-06-13 02:13:23.747836
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class TestMgr(CLIMgr):
        CLI = 'bash'
    test_mgr = TestMgr()
    assert test_mgr.is_available()


# Generated at 2022-06-13 02:13:25.208527
# Unit test for constructor of class LibMgr
def test_LibMgr():
    assert(LibMgr()._lib is None)


# Generated at 2022-06-13 02:13:29.917343
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    class testCLIMgr(CLIMgr):
        CLI = 'python'
    test = testCLIMgr()
    assert test.is_available() == True
    assert type(test._cli) == 'str'
    class testCLIMgr2(CLIMgr):
        CLI = 'python_not_available'
    test2 = testCLIMgr2()
    assert test2.is_available() == False

# Generated at 2022-06-13 02:13:32.157883
# Unit test for constructor of class LibMgr
def test_LibMgr():
    libmgr = LibMgr()
    assert libmgr is not None


# Generated at 2022-06-13 02:13:39.970047
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    from ansible.module_utils.basic import load_platform_subclass
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgr
    import os

    #data = {'file_exists': lambda filename: False}
    data = {'x': 'y'}
    #data = {'file_exists': lambda filename: filename == '/usr/bin/yum'}
    #obj = Yum(data)
    obj = load_platform_subclass(PkgMgr, 'Linux', data)
    print(obj.is_available())
    print(obj._lib)
    print(obj.CLI)



# Generated at 2022-06-13 02:13:42.690877
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.software_management.pkg_managers import CLIMgr
    a = CLIMgr()
    a.CLI = 'abc'
    assert a.is_available() == True

# Generated at 2022-06-13 02:14:55.454066
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pass


# Generated at 2022-06-13 02:14:56.525857
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    assert PkgMgr().is_available() is False


# Generated at 2022-06-13 02:14:57.544055
# Unit test for constructor of class LibMgr
def test_LibMgr():
    pm = LibMgr()
    assert not pm.is_available()


# Generated at 2022-06-13 02:14:59.801402
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    pkgmgr = PkgMgr()
    info = pkgmgr.get_package_details("test")

    assert(type(info) is dict)
    assert('name' in info)
    assert('version' in info)



# Generated at 2022-06-13 02:15:02.639770
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    class AptMgr(PkgMgr):

        LIB = 'apt'

    apt_mgr = AptMgr()
    assert apt_mgr.is_available()

    class FakeMgr(PkgMgr):

        LIB = 'fake'

    fake_mgr = FakeMgr()
    assert not fake_mgr.is_available()


# Generated at 2022-06-13 02:15:06.632424
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    class TestPkgMgr(PkgMgr):
        def get_package_details(self, package):
            return {'name': package}
    tpm = TestPkgMgr()
    assert tpm.get_package_details('package1') == {'name': 'package1'}


# Generated at 2022-06-13 02:15:13.701849
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.common._utils import get_all_subclasses
    # test class CLIMgr

    subclasses = [obj for obj in get_all_subclasses(CLIMgr)]
    for subclass in subclasses:
        try:
            if type(subclass()).__name__ in ['YUMMgr', 'DNFMgr']:
                assert subclass().is_available(), '%s not installed' % subclass.__name__
            else:
                assert not subclass().is_available(), '%s unexpectedly installed' % subclass.__name__
        except:
            assert False, 'unexpected exception'



# Generated at 2022-06-13 02:15:15.767216
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    pm = PkgMgr()
    assert pm.list_installed() == None


# Generated at 2022-06-13 02:15:17.225248
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    assert PkgMgr.get_packages(PkgMgr) == dict()

# Generated at 2022-06-13 02:15:25.453464
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    test_package = 'some_package'
    expected_keys = ['name', 'version']

    class TestPkgMgr(PkgMgr):

        def is_available(self):
            return True

        def list_installed(self):
            return [test_package]

        def get_package_details(self, package):
            if package == test_package:
                return {'name': 'some_package', 'version': '1.1.1'}
            return {}

    test_mgr = TestPkgMgr()
    test_package_details = test_mgr.get_package_details(test_package)
    assert test_package_details.get('name') == 'some_package'
    assert test_package_details.get('version') == '1.1.1'

# Generated at 2022-06-13 02:18:13.649131
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    assert PkgMgr.get_package_details(PkgMgr, 'nmap') == 'nmap'

# Generated at 2022-06-13 02:18:14.725286
# Unit test for constructor of class LibMgr
def test_LibMgr():
    libmgr = LibMgr()
    assert libmgr

# Generated at 2022-06-13 02:18:21.978096
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    enumerated_package_managers = get_all_pkg_managers()
    for pkg_mgr_name in enumerated_package_managers:
        pkg_mgr = enumerated_package_managers[pkg_mgr_name]()
        if pkg_mgr.is_available():
            pkg_mgr_response = pkg_mgr.get_packages()
            for single_package in pkg_mgr_response:
                for pkg_version in pkg_mgr_response[single_package]:
                    if 'name' not in pkg_version or 'version' not in pkg_version:
                        assert False, "package `%s` returned by %s has incomplete detail." % (single_package, pkg_mgr_name)
    assert True

# Generated at 2022-06-13 02:18:23.272842
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert CLIMgr().is_available() == False


# Generated at 2022-06-13 02:18:24.580646
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    test_class = LibMgr()
    assert test_class.is_available() == False


# Generated at 2022-06-13 02:18:30.751683
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    class Test_PkgMgr(PkgMgr):

        def __init__(self):
            return

        def list_installed(self):
            return []

        def get_package_details(self, package):
            return {}
    import os.path
    t = Test_PkgMgr()
    err = 'Test_PkgMgr.is_available: not False'
    assert t.is_available() == False, err
    t.CLI = os.path.basename(__file__)
    err = 'Test_PkgMgr.is_available: not True'
    assert t.is_available(), err
    t.LIB = 'ansible'
    err = 'Test_PkgMgr.is_available: not True'
    assert t.is_available(), err

# Generated at 2022-06-13 02:18:36.563030
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    """ Assert that CLIMgr class correctly detects whether a cli is available """
    class CLIMgrThatExists(CLIMgr):
        CLI = "true"
    class CLIMgrThatDoesNotExist(CLIMgr):
        CLI = "this_cli_does_not_exist"
    assert CLIMgrThatExists().is_available()
    assert not CLIMgrThatDoesNotExist().is_available()


# Generated at 2022-06-13 02:18:41.873217
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    import unittest
    import doctest
    doctest.testmod(PkgMgr)
    suite = doctest.DocTestSuite(PkgMgr)
    suite.addTest(doctest.DocTestSuite(CLIMgr))
    suite.addTest(doctest.DocTestSuite(LibMgr))
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite)

if __name__ == '__main__':
    test_PkgMgr_get_package_details()

# Generated at 2022-06-13 02:18:51.369566
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    # Create dummy class deriving from PkgMgr calling get_package_details
    class DummyPkgMgr(PkgMgr):
        def list_installed(self):
            return []
        def get_package_details(self, package):
            d = package
            if 'source' not in d:
                d['source'] = self.__class__.__name__.lower()
            return d
    d = DummyPkgMgr()
    # get_package_details returns the package dictionary with 'source' added it this key was not there
    assert d.get_package_details({'name': 'foo', 'version': '1'}) == {'name': 'foo', 'version': '1', 'source': 'dummypkgmgr'}
    # get_package_details keeps the source if it is already there

# Generated at 2022-06-13 02:18:55.963012
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():

    assert len(get_all_pkg_managers()) == 0

    class TestPkgMgr(PkgMgr):
        pass

    assert TestPkgMgr.__name__.lower() in get_all_pkg_managers()
    assert len(get_all_pkg_managers()) == 1
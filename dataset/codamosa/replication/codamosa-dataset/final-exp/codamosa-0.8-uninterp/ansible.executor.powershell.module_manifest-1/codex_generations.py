

# Generated at 2022-06-12 21:41:15.172335
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Note: Ansible module modules/utilities/logic/async_wrapper.py has been
    # updated to not use this function.
    ps_dep_finder = PSModuleDepFinder()

    # The powershell executor script should add the module to the
    # dictionary exec_scripts.
    ps_dep_finder.scan_exec_script("powershell_wrapper")
    assert ps_dep_finder.exec_scripts["powershell_wrapper"]

    # If the script is already in the dictionary, then it should not add a
    # duplicate entry.
    ps_dep_finder.scan_exec_script("powershell_wrapper")
    assert ps_dep_finder.exec_scripts["powershell_wrapper"]

    # If the script is not found, it should throw an error.
    # Note: This can be changed to an AnsibleModule specific

# Generated at 2022-06-12 21:41:28.331634
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Finds any required module_utils in a module
    ps_module_util_test_data = """# This is a test module_util, it requires the following:
#Requires -Module Ansible.ModuleUtils.Legacy
# Requires -Module Ansible.ModuleUtils.Test
# Requires -Module Ansible.ModuleUtils.Validate
# Requires -Module Ansible.ModuleUtils.NetTools
# AnsibleRequires -PowerShell Ansible.ModuleUtils.NetTools
# AnsibleRequires -PowerShell Ansible.ModuleUtils.Validate -Optional
# AnsibleRequires -PowerShell Ansible.ModuleUtils.Test
# AnsibleRequires -PowerShell ..module_utils.other.namespace.AnotherModuleUtil
"""

# Generated at 2022-06-12 21:41:40.078189
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test for method scan_module([module_data, fqn=None]) (unit test)
    test_ps_module_fqn = 'test.test_module'
    test_cs_module_fqn = 'test.my_cs_module_util'
    test_module_name = 'test_module.psm1'


# Generated at 2022-06-12 21:41:47.239858
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # mock the module to use during the unit test of the function above
    import mock
    m = mock.mock_module.MockModule()

    m.PSModuleDepFinder = PSModuleDepFinder
    m.ps_module_utils_loader = ModuleLoader()
    m.AnsibleError = AnsibleError
    m.pkgutil = ModuleLoader()
    m.C = ModuleLoader()
    m.C.DEFAULT_DEBUG = None
    m.constants = ModuleLoader()
    m.constants.DEFAULT_DEBUG = None
    m.unittest = ModuleLoader()
    m.random = ModuleLoader()
    m.errno = ModuleLoader()
    m.json = ModuleLoader()
    m.os = ModuleLoader()
    m.os.environ = {}

# Generated at 2022-06-12 21:41:49.192368
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_object = PSModuleDepFinder()
    test_object.scan_exec_script(name = 'test')


# Generated at 2022-06-12 21:41:50.427592
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    
    #TODO
    pass


# Generated at 2022-06-12 21:41:58.089071
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    testing_obj = PSModuleDepFinder()
    testing_obj.scan_module(b'test')
    testing_obj.scan_module(b'test', b'test')
    testing_obj.scan_module(b'test', b'test', False, False)
    testing_obj.scan_module(b'test', b'test', False, True)
    testing_obj.scan_module(b'test', b'test', True, False)
    testing_obj.scan_module(b'test', b'test', True, True)

# Generated at 2022-06-12 21:41:59.677138
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ex = PSModuleDepFinder()
    ex.scan_exec_script('script')



# Generated at 2022-06-12 21:42:05.278011
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script('0.0.1')
    # Test type of 'ps_module_dep_finder.exec_scripts'
    # Test number of 'ps_module_dep_finder.exec_scripts' keys
    # Test that 'ps_module_dep_finder.exec_scripts' has '0.0.1' key
    assert isinstance(ps_module_dep_finder.exec_scripts, dict)
    assert len(ps_module_dep_finder.exec_scripts) == 1
    assert '0.0.1' in ps_module_dep_finder.exec_scripts


# Generated at 2022-06-12 21:42:10.943025
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()

# Generated at 2022-06-12 21:42:37.301127
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    os.chdir("..")
    from test_utils import mock, unittest
    from ansible.module_utils.urls import open_url
    f = PSModuleDepFinder()

    p = mock.patch.object(open_url, 'get_url', autospec=True)
    with p as mock_get_url:
        f.scan_module("# AnsibleRequires -CSharpUtil Ansible.ModuleUtils.Common")
        assert mock_get_url.called
        assert mock_get_url.call_count == 1

    f = PSModuleDepFinder()
    p = mock.patch.object(open_url, 'get_url', autospec=True)

# Generated at 2022-06-12 21:42:40.526719
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    mdepfinder =  PSModuleDepFinder()
    mdepfinder.scan_exec_script("default-wrapper")

if __name__ == "__main__":
    test_PSModuleDepFinder_scan_exec_script()

# Generated at 2022-06-12 21:42:41.081793
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:42:44.714498
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()

    dep_finder.scan_exec_script("internal_test")
    assert dep_finder.exec_scripts["internal_test"] == "Exec script data\n"
    assert dep_finder.ps_modules["UtilA"]['data'] == "UtilA\n"
    assert dep_finder.ps_modules["UtilB"]['data'] == "UtilB\n"



# Generated at 2022-06-12 21:42:56.411382
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    fqn = 'example.collection.module_name'
    module_data = module_data = to_bytes('''
#Requires -Module Ansible.ModuleUtils.TestModuleUtil
#Requires -Module UsefulUtil
#Requires -Module UsefulUtil.OtherUtil
#Requires -Module UsefulUtilException
#Requires -Module UsefulUtil.FruitBasket
#Requires -Module UsefulUtil.FruitBasket.Apple
#AnsibleRequires -PowerShell UsefulUtil
#AnsibleRequires -PowerShell UsefulUtil.OtherUtil
#AnsibleRequires -PowerShell UsefulUtilException
#AnsibleRequires -PowerShell UsefulUtil.FruitBasket
#AnsibleRequires -PowerShell UsefulUtil.FruitBasket.Apple
#AnsibleRequires -PowerShell -Optional NonExistant
''')

   

# Generated at 2022-06-12 21:43:07.471824
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    args = {
        'module_data': b'#AnsibleRequires -CSharpUtil ansible_collections.namespace.collection.plugins.module_utils.name',
        'fqn': 'ansible_collections.namespace.collection.plugins.modules.name',
        'wrapper': False,
        'powershell': True
    }
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_module(**args)
    assert len(dep_finder.cs_utils_module) == 1
    assert to_text(random.choice(list(dep_finder.cs_utils_module.items()))) == 'ansible_collections.namespace.collection.plugins.module_utils.name'

# Generated at 2022-06-12 21:43:15.387413
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import unittest

    class TestPSModuleDepFinderScanModule(unittest.TestCase):
        def setUp(self):
            self.finder = PSModuleDepFinder()

        def test_scan_module_builtin(self):
            module_data = to_bytes("""#Requires -Module Ansible.ModuleUtils.SomeModule
            """)
            self.finder.scan_module(module_data)
            self.assertEqual(1, len(self.finder.ps_modules))
            self.assertIn("Ansible.ModuleUtils.SomeModule", self.finder.ps_modules.keys())

        def test_scan_module_collection(self):
            module_data = to_bytes("""#Requires -Module ansible_collections.some.collection.plugins.module_utils.SomeModule
            """)


# Generated at 2022-06-12 21:43:18.712711
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test = PSModuleDepFinder()
    test.scan_exec_script('4x.0/become_base')
    test.scan_module(b"#Requires -Module Ansible.ModuleUtils.Common")
    assert "Ansible.ModuleUtils.Common" in test.ps_modules

# Generated at 2022-06-12 21:43:27.381451
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    f = PSModuleDepFinder()
    f.ps_version = "5.1"
    f.os_version = "2012"
    f.scan_exec_script(name="powershell_5.1_common.ps1")
    assert f.exec_scripts["powershell_5.1_common.ps1"].startswith(b'#!PS')
    assert f.become == False
    assert f.os_version == "2012"
    assert len(f.cs_utils_wrapper) == 2
    assert len(f.ps_modules) == 0
    assert f.ps_version == "5.1"


# Generated at 2022-06-12 21:43:32.304110
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    PSModuleDepFinder_obj1 = PSModuleDepFinder()
    name = "ps_package"
    assert PSModuleDepFinder_obj1.exec_scripts is None
    PSModuleDepFinder_obj1.scan_exec_script(name)
    # Test for exception raised
    try:
        PSModuleDepFinder_obj1.scan_exec_script("abc")
    except Exception as e:
        assert isinstance(e, AnsibleError)

# Generated at 2022-06-12 21:44:07.446745
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # initialize test class
    p1 = PSModuleDepFinder()
    # normal cases
    p1.scan_exec_script(name='async')
    p1.scan_exec_script(name='executor')
    p1.scan_exec_script(name='json_serialize_helper')

    # exception cases
    try:
        p1.scan_exec_script(name='abc')
    except:
        pass



# Generated at 2022-06-12 21:44:16.409980
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

     _data = '''#!/usr/bin/python
import os
import base64

from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
from ansible.module_utils.six.moves.urllib.error import HTTPError
'''
     _data1 = '''using ansible_collections.test.test_collection.plugins.module_utils.test_test;
using ansible_collections.test.test1_collection.plugins.module_utils.test_test1;

'''

# Generated at 2022-06-12 21:44:18.872719
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("foo")
    assert finder.exec_scripts['foo'] == to_bytes(pkgutil.get_data("ansible.executor.powershell", "foo.ps1"))



# Generated at 2022-06-12 21:44:21.929102
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("example.ps1")
    example_script = pkgutil.get_data("ansible.executor.powershell", "example.ps1")

    assert dep_finder.exec_scripts['example'].decode('utf-8').strip() == example_script.decode('utf-8').strip()


# Generated at 2022-06-12 21:44:28.631817
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible_collections.ansible.community.tests.unit.plugins.loader.find_imports import detect_imports
    # setup the values for test
    mu = PSModuleDepFinder()
    wrapper = "ansible-doc.ps1"
    mu.scan_exec_script(wrapper)
    # test that the wrapper is added to the internal list of scripts
    assert wrapper in mu.exec_scripts.keys()
    # test that the PSModuleDepFinder has detected the ModuleUtils import
    module_utils = detect_imports(mu.exec_scripts[wrapper])
    assert 'Ansible.ModuleUtils.CommonUtils' in module_utils['ps_module'].keys()

# Generated at 2022-06-12 21:44:41.840791
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    print("Testing PSModuleDepFinder.scan_module()")

    # Expected result for vvv, module util, should be in all_ps_modules and cs_utils_module
    exp_fqname1 = 'ansible_collections.my.module_utils.moduleutil1'
    exp_fqname2 = 'ansible_collections.my.module_utils.moduleutil2'
    exp_fqname3 = 'ansible_collections.my.module_utils.moduleutil3'
    exp_fqname4 = 'ansible_collections.my.module_utils.moduleutil4'
    exp_fqname5 = 'ansible_collections.my.module_utils.moduleutil5'
    exp_fqname6 = 'ansible_collections.my.module_utils.moduleutil6'


# Generated at 2022-06-12 21:44:43.253778
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass # nothing to test, the method is only used interactively in a debugger



# Generated at 2022-06-12 21:44:55.529314
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:44:57.184024
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    #provide your implementation here
    pass


# Generated at 2022-06-12 21:44:58.967085
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # TODO: redo test
    pass

# Generated at 2022-06-12 21:46:08.879076
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import pytest

    module_utiltest_data = pkgutil.get_data('test.unit.async_wrapper_plugins', 'test_module_utils/test_ps_module.psm1')
    assert module_utiltest_data is not None
    # Use the same code as the real module loader to load collections
    # This is necessary because the original method references another collection
    psModuleDepFinder = PSModuleDepFinder()
    psModuleDepFinder.scan_module(module_utiltest_data)
    assert 'Ansible.ModuleUtils.Utils.Utils' in psModuleDepFinder.ps_modules.keys()
    assert 'Ansible.ModuleUtils.CommonUtils.CommonUtils' in psModuleDepFinder.ps_modules.keys()

# Generated at 2022-06-12 21:46:11.000688
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    PSModuleDepFinder_instance = PSModuleDepFinder()
    assert PSModuleDepFinder_instance.scan_exec_script('powershell') == None


# Generated at 2022-06-12 21:46:21.260711
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("csharp_wrapper")

    actual_exec_scripts = dep_finder.exec_scripts.copy()
    actual_cs_utils_wrapper = dep_finder.cs_utils_wrapper.copy()


    # Validate exec scripts
    assert actual_exec_scripts.keys() == {'csharp_wrapper'}, \
        "scan_exec_script() should add the specified script in exec_scripts"

    # Validate cs utils

# Generated at 2022-06-12 21:46:25.039225
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_module = mock.Mock()
    finder.scan_exec_script("whoami")
    finder.scan_module.assert_called_once_with(mock.ANY, "whoami.ps1", True, True)



# Generated at 2022-06-12 21:46:26.982031
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:46:34.449664
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    depFinder = PSModuleDepFinder()
    depFinder.scan_exec_script('test2')
    assert depFinder.exec_scripts['test2'] == 'exec_script2'
    assert depFinder.ps_modules['Ansible.ModuleUtils.Test2']['data'] == 'module_util_data2'
    assert depFinder.ps_modules['Ansible.ModuleUtils.Test2']['path'] == 'module_util2.psm1'


# Unit tests for method _add_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:46:36.973802
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print('Testing scan_exec_script method of class PSModuleDepFinder')
    obj = PSModuleDepFinder()
    obj.scan_exec_script('Config')


# Generated at 2022-06-12 21:46:40.634660
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # noinspection PyArgumentList
    new_object = object.__new__(PSModuleDepFinder)
    new_object.__init__()
    # Testing a private method
    new_object._add_module = None

    # noinspection PyCallingNonCallable
    new_object.scan_exec_script("ansible_module_run")



# Generated at 2022-06-12 21:46:47.379503
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    file_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/executor/powershell/Ansible.Completion.ps1"
    with open(file_name) as f:
        data = f.read()
    finder = PSModuleDepFinder()
    finder.scan_exec_script("Ansible.Completion")
    assert data == finder.exec_scripts['Ansible.Completion']
# Test class PSModuleDepFinder

# Generated at 2022-06-12 21:46:59.727820
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    class FakeObj():
        pass
    obj = FakeObj()
    obj.ps_modules = dict()
    obj.cs_utils_wrapper = dict()
    obj.cs_utils_module = dict()
    obj.ps_version = None
    obj.os_version = None
    obj.become = False

    data1 = b'some data'
    obj.scan_module(data1, fqn=None, wrapper=False, powershell=True)

    data2 = b'some data with #Requires -module ansible.moduleutils.legacy'
    obj.scan_module(data2, fqn=None, wrapper=False, powershell=True)
    assert obj.ps_modules.get('ansible.moduleutils.legacy', None)


# Generated at 2022-06-12 21:49:08.855747
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    assert True


# Generated at 2022-06-12 21:49:12.823885
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    name = 'base'
    finder.scan_exec_script(name)
    assert name in finder.exec_scripts
    assert name in finder.ps_modules
    assert name not in finder.cs_utils_module
    assert name in finder.cs_utils_wrapper


# Generated at 2022-06-12 21:49:20.769461
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """
    # Test case to check if the scan_exec_script method of the class PSModuleDepFinder
    # is adding the script's data into the executor_scripts attribute of the PSModuleDepFinder
    """
    obj = PSModuleDepFinder()
    obj.scan_exec_script("AdGroup")
    assert "AdGroup" in obj.exec_scripts.keys()
    assert "CanRename" in obj.exec_scripts.keys()


# Generated at 2022-06-12 21:49:30.805778
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    test_PSModuleDepFinder_scan_module.dep_finder = PSModuleDepFinder()
    test_PSModuleDepFinder_scan_module.dep_finder.scan_module('#Requires -Module Ansible.ModuleUtils.Common')

# Generated at 2022-06-12 21:49:42.218511
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:49:52.051334
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mock_name = 'mock_name'
    scan_exec_script_reference = 'ansible.executor.powershell.mock_name.ps1'

# Generated at 2022-06-12 21:49:54.889139
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    mdf = PSModuleDepFinder()
    utils = mdf.scan_module("test.psm1", "some.fq.module_name")
    # The following is the assertation for the test.
    assert utils is not None
    assert utils == set()

# Generated at 2022-06-12 21:50:04.205010
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # test fixture create a fake module in memory and call scan_exec_script on this
    # and check the contents of the self.exec_scripts dict is as expected
    psmdf = PSModuleDepFinder()

    expected_content = b"""
# this is a test
#requires -version 3.0
#ansiblerequires -powershell ansible.moduleutils.test
#ansiblerequires -wrapper test
    """
    test_fixture = {
        "test.ps1": expected_content,
    }

    def fake_get_data(package, resource):
        return test_fixture[to_native(resource)]

    pkgutil.get_data = fake_get_data
    psmdf.scan_exec_script("test")
    assert psmdf.exec_scripts["test"] == expected_content



# Generated at 2022-06-12 21:50:05.147443
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:50:16.417823
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import os
    if not os.path.exists('test_ansible_module_utils.psm1'):
        print('test_ansible_module_utils.psm1 not found!')
        assert False
    else:
        module_data = _slurp('test_ansible_module_utils.psm1')
        #print('module_data = %s' % module_data)
        dep_finder = PSModuleDepFinder()
        dep_finder.scan_module(module_data[0], fqn=None, wrapper=False, powershell=True)
        #print('PSModuleDepFinder._cs_utils_module = %s' % dep_finder._cs_utils_module)
        assert True


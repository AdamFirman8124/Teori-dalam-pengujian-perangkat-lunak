

# Generated at 2022-06-12 21:41:13.850553
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    d = PSModuleDepFinder()
    d.scan_exec_script('win_package')


# Generated at 2022-06-12 21:41:27.049179
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    psModuleDepFinder = PSModuleDepFinder()
    # Test PS Module contains 'using Ansible.*;' or 'using ansible_collections.ns.coll.plugins.module_utils.*;'
    test_str = 'using ansible_collections.sourced.collection2.plugins.module_utils.user;\r\n' \
               'using ansible_collections.sourced.collection1.plugins.module_utils.collection1_utils;\r\n' \
               'using sourced.plugins.module_utils.collection1_utils;'
    psModuleDepFinder.scan_module(test_str)

# Generated at 2022-06-12 21:41:27.852800
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True

# Generated at 2022-06-12 21:41:39.649219
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_input = [
        {
            'name' : None,
            'expectation' : AnsibleError
        },
        {
            'name' : 'group1',
            'expectation' : True
        },
        {
            'name' : 'group2',
            'expectation' : True
        }
    ]
    obj = PSModuleDepFinder()

# Generated at 2022-06-12 21:41:41.621103
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmodule = PSModuleDepFinder()
    psmodule.scan_exec_script('fake_script_name.ps1')



# Generated at 2022-06-12 21:41:44.579671
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('pwshshell')
    assert "iohelper" in finder.exec_scripts.keys()
    assert "filewrapper" in finder.exec_scripts.keys()


# Generated at 2022-06-12 21:41:47.591398
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # NOTE: this is a test stub
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script('')


# Generated at 2022-06-12 21:41:57.166285
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.executor.powershell import get_ps_versions
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.powershell import ps_script_from_shebang
    from ansible.plugins.loader import module_loader
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    # mock shell object methods
    class MockShellModule(object):
        def __init__(self, path, use_shell=True, no_log=False):
            self._path = path
            self._use_shell = use_shell
            self._no_log = no_log
            self.params = {'_ansible_shell_type': 'powershell'}
            self._shell = None
            self._become_method = 'runas'

# Generated at 2022-06-12 21:42:04.142271
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class MockExecutor(object):
        @classmethod
        def _load_module_source(cls, module_name, module_args, poweshell=True, *args, **kwargs):
            return None

    # Prepare the inputs
    test_name = 'mock_name'
    test_data = 'mock_data'
    test_psm1 = 'mock_psm1'

    # Create instance of PSModuleDepFinder
    instance = PSModuleDepFinder()

    # Call scan_exec_script()
    instance.scan_exec_script(test_name)

    # Verify scan_exec_script()
    assert instance.exec_scripts[test_name] == to_bytes(test_data)
    assert instance.ps_modules.keys() == set([to_text(test_psm1)])

# Generated at 2022-06-12 21:42:04.768644
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False, "Test not implemented"


# Generated at 2022-06-12 21:42:28.508219
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import ansible.executor.powershell as powershell
    ps_module_find = PSModuleDepFinder()

    # Extracted from actual code
    expected = {'ModuleUtil': {'data': b'using System;\nusing System.Management.Automation;',
                               'path': u'/home/james/ansible/lib/ansible/executor/powershell/ModuleUtil.cs'},
                'ModuleUtil.Utils': {'data': b'using System;\nusing System.Management.Automation;',
                                     'path': u'/home/james/ansible/lib/ansible/executor/powershell/ModuleUtil.cs'}}
    ps_module_find.scan_exec_script('ModuleUtil')
    assert ps_module_find.cs_utils_wrapper == expected

   

# Generated at 2022-06-12 21:42:31.389482
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    depfinder = PSModuleDepFinder()
    depfinder.scan_exec_script("WinEventLog")

    assert(depfinder.exec_scripts["WinEventLog"] is not None)


# Generated at 2022-06-12 21:42:42.944304
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.powershell.ps_module_utils import PSModuleDepFinder
    execution_test_file_path = os.path.join(os.path.dirname(__file__), 'library/test_execution_module.psm1')
    execution_test_module_data = to_bytes(_slurp(execution_test_file_path))
    ps_module_finder = PSModuleDepFinder()
    ps_module_finder.scan_module(execution_test_module_data)
    assert len(ps_module_finder.ps_modules.keys()) == 1
    assert len(ps_module_finder.cs_utils_module.keys()) == 0

# Generated at 2022-06-12 21:42:53.722912
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import random
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import ps_module_utils_loader

    f = PSModuleDepFinder()

    name = "dummy-exec-script"
    if name in f.exec_scripts.keys():
        raise AnsibleError("test fixture {0} already in f.exec_scripts".format(name))

    f.scan_exec_script(name)

    if name not in f.exec_scripts.keys():
        raise AnsibleError("test fixture {0} not added to f.exec_scripts".format(name))

    # ps_module_utils_loader is exposed by the plugins/loader/ps_module_utils_loader.py module

# Generated at 2022-06-12 21:43:06.135293
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible_collections.channaleer.pulse.tests.unit.compat.mock import patch
    from ansible_collections.channaleer.pulse.plugins.module_utils.common.deprecation import AnsibleDeprecationWarning
    import warnings

    mock_data = b"Mock"
    mock_path = b"path/to/powershell"

    with patch('pkgutil.get_data', return_value=mock_data):
        pdmf = PSModuleDepFinder()
        pdmf.scan_exec_script(mock_path)

        assert pdmf.exec_scripts == {mock_path.decode('utf-8'): mock_data}


# Generated at 2022-06-12 21:43:12.872968
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test use of module_utils in an exec script wrapper
    # This isn't going to catch the wrapper referencing C# module_utils, so
    # a new test is needed in test_module_dep_finder_cs.py
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script("powershell_module")
    assert len(ps_module_dep_finder.ps_modules) > 0
    assert 'Ansible.ModuleUtils.Core' in ps_module_dep_finder.ps_modules



# Generated at 2022-06-12 21:43:20.959660
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class AnsibleExitJson(Exception):
        pass

    class AnsibleFailJson(Exception):
        pass

    def exit_json(*args, **kwargs):
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise AnsibleExitJson(kwargs)

    def fail_json(*args, **kwargs):
        kwargs['failed'] = True
        raise AnsibleFailJson(kwargs)

    class MockModule(object):
        def __init__(self, *args, **kwargs):
            pass

        def exit_json(self, *args, **kwargs):
            exit_json(*args, **kwargs)

        def fail_json(self, *args, **kwargs):
            fail_json(*args, **kwargs)


# Generated at 2022-06-12 21:43:26.265396
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    my_path = ""
    expected = {}

    # Invoke method
    finder.scan_exec_script(my_path)
    # Check for idempotency
    finder.scan_exec_script(my_path)

    # Check proper functioning
    assert expected == finder.exec_scripts


# Generated at 2022-06-12 21:43:34.056872
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test for scan_module, the method that handles the _re_cs_in_ps_module,
    # _re_ps_module, _re_wrapper, _re_ps_version, _re_os_version and _re_become regexes.
    ps_module_finder = PSModuleDepFinder()

    # Insert comments between statements, to ensure comments are handled correctly.

# Generated at 2022-06-12 21:43:35.667375
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # unit test for method scan_exec_script of class PSModuleDepFinder
    pass



# Generated at 2022-06-12 21:43:58.057452
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible_collections.ansible.netcommon.plugins.module_utils import network as network_utils
    import ansible_collections.jctanner.cloud_azure.plugins.module_utils.azure_rm_common as azure_rm_module_utils
    from ansible_collections.jctanner.cloud_azure.plugins.module_utils import azure_rm_common as azure_rm_module_utils_submodule
    import ansible.module_utils.facts
    import ansible.module_utils.netutils


# Generated at 2022-06-12 21:44:09.473000
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    f = PSModuleDepFinder()
    module_data = pkgutil.get_data("ansible.plugins.modules", to_native("win_cdrom.psm1"))
    f.scan_module(module_data)

    assert 'ansible_collections.ansible.builtin.plugins.module_utils.powershell.security' in f.cs_utils_wrapper.keys()
    assert 'ansible_collections.ansible.builtin.plugins.module_utils.powershell.network' in f.cs_utils_wrapper.keys()
    assert 'ansible_collections.ansible.builtin.plugins.module_utils.powershell.windows' in f.cs_utils_wrapper.keys()

# Generated at 2022-06-12 21:44:11.119721
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False, "Test with pytest"



# Generated at 2022-06-12 21:44:16.112214
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    f = PSModuleDepFinder()
    # empty
    f.scan_exec_script("")
    # valid
    f.scan_exec_script("powershell")
    # invalid
    try:
        f.scan_exec_script("powershell1")
    except AnsibleError:
        pass



# Generated at 2022-06-12 21:44:20.387956
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Create an instance of PSModuleDepFinder class
    obj = PSModuleDepFinder()
    # scan 'ansible_powershell_command' script in the executor folder
    obj.scan_exec_script(b'ansible_powershell_command')
    # assert that the length of the object's 'exec_scripts' dictionary is 1
    assert len(obj.exec_scripts) == 1
    # assert that the length of the object's 'ps_modules' dictionary is 1
    assert len(obj.ps_modules) == 1


# Generated at 2022-06-12 21:44:32.089997
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    def _test_module_data(module_data, fqn, expected_results, expected_results_cs):
        m = PSModuleDepFinder()
        m.scan_module(module_data, fqn)

        assert m.ps_modules == expected_results
        assert m.cs_utils_module == expected_results_cs

    # Test module that has dependencies on builtin module_utils and ansible_collections module_utils
    # Can't have colons in file names but the module path is referenced in the loader for the ps module util

# Generated at 2022-06-12 21:44:41.073992
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder._add_module = MagicMock()
    ps_module_dep_finder.scan_exec_script("TestModule")
    ps_module_dep_finder._add_module.assert_called_with(
        "ansible.executor.powershell.TestModule", ".ps1", None, False, True
    )
    assert "TestModule" in ps_module_dep_finder.exec_scripts.keys()

# Generated at 2022-06-12 21:44:48.784300
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    for path in ['../../../../lib/ansible/executor/powershell/Microsoft.PowerShell.Archive.psm1',
                 '../../../../lib/ansible/executor/powershell/Microsoft.PowerShell.Management.psm1',
                 '../../../../lib/ansible/executor/powershell/Microsoft.PowerShell.Security.psm1',
                 '../../../../lib/ansible/executor/powershell/Microsoft.PowerShell.Utility.psm1',
                 '../../../../lib/ansible/executor/powershell/System.Management.Automation.psm1']:
        module = open(path, 'rb').read()
        ps_module_dep_finder = PSModuleDepFinder()
        ps_module_dep_finder.scan_module(module)
        ps_

# Generated at 2022-06-12 21:44:54.181609
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    finder = PSModuleDepFinder()
    assert finder.exec_scripts == dict()
    assert finder.cs_utils_wrapper == dict()
    assert finder.ps_modules == dict()
    assert finder.exec_scripts == dict()

    finder.scan_exec_script("posh")
    assert finder.exec_scripts == dict(posh=_validate_data("posh.ps1"))
    assert finder.cs_utils_wrapper == dict()
    assert finder.ps_modules == dict(Utils="Utils.psm1")

    finder.scan_exec_script("posh_winrm")

# Generated at 2022-06-12 21:45:00.744992
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.executor.powershell.util.module_utils.common import Common, CommonArgs
    from ansible_collections.solarwinds.orion.plugins.module_utils.argspec import OrionArgSpec
    from ansible_collections.solarwinds.orion.plugins.module_utils.argspec import OrionConnectionArgSpec
    ps_dep_finder = PSModuleDepFinder()
    # C# module_utils
    test_class = OrionArgSpec()
    ps_dep_finder.scan_module(test_class.__doc__, wrapper=False, powershell=False)
    assert(len(ps_dep_finder.cs_utils_module.keys()) == 1)
    test_class = OrionConnectionArgSpec()

# Generated at 2022-06-12 21:45:16.790426
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # No need to test, the method only calls scan_module.
    return



# Generated at 2022-06-12 21:45:27.770376
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """Test for PSModuleDepFinder._parse_version_match."""
    finder = PSModuleDepFinder()
    finder.scan_exec_script("script_no_requires")
    assert set(finder.exec_scripts.keys()) == set(["script_no_requires"])

    finder = PSModuleDepFinder()
    finder.scan_exec_script("script_one_require")
    assert set(finder.exec_scripts.keys()) == set(["script_one_require"])

    # recursion
    finder = PSModuleDepFinder()
    finder.scan_exec_script("script_recursive_require")
    assert set(finder.exec_scripts.keys()) == set(["script_recursive_require"])

    # multiple recursion
    finder = PSModuleDepFinder()
   

# Generated at 2022-06-12 21:45:38.644554
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:45:45.359630
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()
    script_name = 'test.ps1'
    module_path = os.path.join(C.DEFAULT_MODULE_PATH[0], 'powershell', script_name)
    finder.scan_module(open(module_path, 'rb').read(), script_name, False, True)
    assert finder.ps_modules is not None
    assert finder.ps_modules['Ansible.ModuleUtils.Powershell.Hashing']['path'].endswith("hashing.psm1")
    assert finder.ps_modules['Ansible.ModuleUtils.Powershell.Path']['path'].endswith("path.psm1")

# Generated at 2022-06-12 21:45:52.237982
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.utils.collection_loader.test_utils import MockModule
    import sys

    # find the current path so we can load the test modules
    ansible_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(ansible_base, 'plugins', 'module_utils')
    sys.path.insert(0, path)

    # load the test module data since these are not part of the collection
    # framework
    module_data = None
    with open(os.path.join(path, 'win_version.psm1'), 'rb') as f:
        module_data = f.read()

    cs_module_data = None

# Generated at 2022-06-12 21:45:56.077501
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    name = "ping"
    finder.scan_exec_script(name)
    assert name in finder.exec_scripts.keys()


# Generated at 2022-06-12 21:45:59.460987
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script('exec_wrapper.ps1')
    assert psmdf.exec_scripts.get('exec_wrapper.ps1')



# Generated at 2022-06-12 21:45:59.867845
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:46:07.996383
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:46:16.771390
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mod_dep_finder = PSModuleDepFinder()
    mod_data = """#Requires -Module Ansible.ModuleUtils.Foo
#Requires -Module Ansible.ModuleUtils.Bar
#Requires -Module Ansible.ModuleUtils.Baz
    """
    mod_dep_finder.scan_exec_script('Script1')
    # scan_exec_script function should populate the exec_scripts dictionary with the script name as the key and the script data as the value
    assert mod_dep_finder.exec_scripts['Script1'] == mod_data

# Unit test to check the functionality of _add_module method of class PSModuleDepFinder

# Generated at 2022-06-12 21:46:39.968897
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_module("import random\n")
    assert ps_module_dep_finder.ps_modules["random"]["path"] == to_text("/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.pyc")
    assert ps_module_dep_finder.cs_utils_wrapper == {}
    assert ps_module_dep_finder.cs_utils_module == {}
    ps_module_dep_finder.scan_module("\"Test\"\n")

# Generated at 2022-06-12 21:46:48.674064
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.common.network import register_platform_parameters

    register_platform_parameters(None)

    # Create an instance of PSModuleDepFinder
    psmd = PSModuleDepFinder()

    # Call method scan_exec_script of PSModuleDepFinder
    psmd.scan_exec_script("exec_wrapper")
    psmd.scan_exec_script("exec_wrapper")
    result = psmd.exec_scripts
    # AssertionError: psmd.exec_scripts is empty
    assert len(result) > 0

    psmd.scan_exec_script("exec_wrapper")
    # Call method scan_exec_script of PSModuleDepFinder
    result = psmd.scan_exec_script("exec_wrapper")
    # AssertionError: psm

# Generated at 2022-06-12 21:46:49.582753
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass

# Generated at 2022-06-12 21:46:53.576791
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    md = PSModuleDepFinder()
    md.scan_module(b'''
        #AnsibleRequires -Wrapper A
    ''')
    assert len(md.exec_scripts) == 1


# Generated at 2022-06-12 21:47:01.903214
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    depFinder = PSModuleDepFinder()
    depFinder.scan_exec_script("win_command")

    assert depFinder.exec_scripts.get('win_command') is not None

    wrapper_util = "win_stat"

    assert depFinder.cs_utils_wrapper.get(wrapper_util) is not None

    # TODO: Add PowerShell support
    # powershell_util = "powershell.psm1"
    #
    # assert depFinder.ps_modules.get(powershell_util) is not None



# Generated at 2022-06-12 21:47:10.462985
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    source_code = base64.b64decode(b'''
c2NhbiBtb2R1bGUgY29kZQo=
''')

    ps_dep_finder = PSModuleDepFinder()
    ps_dep_finder.scan_module(source_code)
    assert len(ps_dep_finder.ps_modules) == 0
    assert len(ps_dep_finder.cs_utils_module) == 0
    assert ps_dep_finder.ps_version is None
    assert ps_dep_finder.os_version is None
    assert ps_dep_finder.become == False


# Generated at 2022-06-12 21:47:16.091771
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    module_data = pkgutil.get_data("ansible.module_utils.powershell.basic", "Ansible.ModuleUtils.Legacy.psm1")
    finder = PSModuleDepFinder()
    finder.scan_module(module_data)
    assert len(finder.ps_modules) == 1
    for module_util, info in finder.ps_modules.items():
        assert module_util in ("Ansible.ModuleUtils.Legacy",)
        assert info['path'].endswith("Ansible.ModuleUtils.Legacy.psm1")
        assert info['data'] == module_data



# Generated at 2022-06-12 21:47:18.790700
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder_instance = PSModuleDepFinder()
    finder_instance.scan_exec_script("wrapper")


# Generated at 2022-06-12 21:47:23.304269
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script("ansible_modlib_powershell")
    assert("ansible_modlib_powershell" in ps_module_dep_finder.exec_scripts.keys())


# Generated at 2022-06-12 21:47:32.335209
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test creating a test PSModuleDepFinder object
    ps_module_dep_finder = PSModuleDepFinder()
    # Test scan_exec_script with valid input and creating the object
    assert isinstance(ps_module_dep_finder.scan_exec_script("Common"), None)
    # Test scan_exec_script with invalid input and creating the object
    invalid_input = "valid_ps1"
    try:
        ps_module_dep_finder.scan_exec_script(invalid_input)
        assert 0, "scan_exec_script(invalid_input) should have raised"
    except AnsibleError as e:
        assert str(e) == "Could not find executor powershell script for '{0}'".format(invalid_input)
    # Test scan_exec_script with null input and creating the object


# Generated at 2022-06-12 21:47:56.245851
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # We do not provide unit tests for this class as it is meant to be called from within the PowerShell module
    # code and not from a unit test file.  The class could be tested by mocking out calls to pkgutil and
    # import_module and also by mocking file reads.
    pass


# Method for creating PowerShell code to load C# module_utils

# Generated at 2022-06-12 21:47:57.919436
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    p = PSModuleDepFinder()
    p.scan_exec_script("cloudformation")



# Generated at 2022-06-12 21:48:04.798169
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # test_scan_exec_script_psm1
    import pkgutil
    data = pkgutil.get_data("ansible.executor.powershell", "elevate.ps1")
    b_data = to_bytes(data)
    finder = PSModuleDepFinder()
    finder.scan_exec_script("elevate")
    assert b_data == finder.exec_scripts["elevate"]
    assert len(finder.ps_modules) == 0
    assert len(finder.cs_utils_wrapper) == 0
    assert len(finder.cs_utils_module) == 0

    # test_scan_exec_script_no_script
    finder = PSModuleDepFinder()

# Generated at 2022-06-12 21:48:10.348221
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import tempfile

    # NOTE: currently using a tmp file is not easy for testing a path ref
    # in a cs module_util. It might be possible if we used the file system
    # package and created a mock dir on the fly but that is a lot of work
    # considering this is only used in the integration test.
    with tempfile.NamedTemporaryFile(mode="wb", delete=False) as mu:
        mu.write(b"#AnsibleRequires -CSharpUtil Ansible.ModuleUtils.Sample\r\n")
        mu.write(b"#Requires -Module Ansible.ModuleUtils.Sample\r\n")
        mu.write(b"#AnsibleRequires -CSharpUtil ansible_collections.namespace.collection.plugins.module_utils.SampleUtil\r\n")
        mu

# Generated at 2022-06-12 21:48:19.131773
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    '''Unit test for method scan_module of class PSModuleDepFinder
    '''

    mod_name = 'mod_name'

    # create a test module file

# Generated at 2022-06-12 21:48:24.612289
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    module_finder = PSModuleDepFinder()
    module_data = '#AnsibleRequires -PowerShell ansible_collections.namespace.collection.plugins.module_utils.test_module_utils'
    module_finder.scan_module(module_data)
    assert module_finder.ps_modules.get('ansible_collections.namespace.collection.plugins.module_utils.test_module_utils') is not None


# Generated at 2022-06-12 21:48:25.442281
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:48:29.339270
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("ansible_standard_library.common.json")
    finder.scan_exec_script("ansible_standard_library.common.json")
    assert len(finder.exec_scripts) == 1
    assert len(finder.ps_modules) == 0
    assert len(finder.cs_utils_wrapper) == 1
    assert len(finder.cs_utils_module) == 0


# Generated at 2022-06-12 21:48:33.303368
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:48:44.182488
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class AnsibleExitJson:
        def __init__(self, ec, value):
            self.param2 = value
    class AnsibleModule:
        def __init__(self, argspec, supports_check_mode = False):
            self.module = ''
            self.result = dict(changed=False)
            self.params = {}
            self.exit_json = AnsibleExitJson(0, self.result)
            self.fail_json = AnsibleExitJson(1, self.result)
            self.check_mode = supports_check_mode
            self.argument_spec = argspec

    from ansible.errors import AnsibleError
    from ansible.module_utils import powershell
    from ansible.utils.collection_loader import ResourceLocator

# Generated at 2022-06-12 21:49:40.220068
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    def wrapped_scan_exec_script():
        # This is a copy of the actual code for scan_exec_script in
        # PSModuleDepFinder, needed to be a function so it can be mocked in
        # the unit tests
        name = to_text(name)
        if name in self.exec_scripts.keys():
            return

        data = pkgutil.get_data("ansible.executor.powershell", to_native(name + ".ps1"))
        if data is None:
            raise AnsibleError("Could not find executor powershell script "
                               "for '%s'" % name)

        b_data = to_bytes(data)

        # remove comments to reduce the payload size in the exec wrappers
        if C.DEFAULT_DEBUG:
            exec_script = b_data
        else:
            exec

# Generated at 2022-06-12 21:49:49.780311
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_data = "windows-module-utils.ps1"
    test_data_bin = pkgutil.get_data("ansible.executor.powershell", to_native(test_data))
    mu = PSModuleDepFinder()
    mu.scan_exec_script(test_data)

    # test_data is a list of the unique module utils that it uses
    # each of these module utils has its own dependencies, so when the
    # full set is generated, we can check that what the scan module
    # method generated is equivalent
    module_utils = set()

# Generated at 2022-06-12 21:49:59.854075
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_module(b'''#Requires -Module Ansible.ModuleUtils.Foo''')
    assert dep_finder.ps_modules['Ansible.ModuleUtils.Foo']
    dep_finder.scan_module(b'''using Ansible.Foo;''')
    assert dep_finder.cs_utils_module['Ansible.Foo']
    dep_finder.scan_module(b'''#AnsibleRequires -CSharpUtil ansible_collections.namespace.collection.plugins.module_utils.foo''')
    assert dep_finder.cs_utils_module['ansible_collections.namespace.collection.plugins.module_utils.foo']

# Generated at 2022-06-12 21:50:06.766909
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test scan_exec_script for psm1
    m_mock = M(spec=PSModuleDepFinder)
    m_mock.cs_utils_wrapper = dict()
    m_mock.cs_utils_module = dict()
    name = "b64decode"
    m_mock.scan_exec_script(name)
    assert m_mock.cs_utils_wrapper == {}
    assert m_mock.cs_utils_module == {}
    assert m_mock.exec_scripts == {name: _slurp(get_data_path("executor/powershell/%s.ps1" % name))}

    # Test scan_exec_script for c#
    m_mock = M(spec=PSModuleDepFinder)
    m_mock.cs_utils_wrapper = dict

# Generated at 2022-06-12 21:50:18.346153
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test case for scan_module of C# module
    cs_module_data = "using ansible_collections.namespace.collection.plugins.module_utils.something; \n" \
                     "using ansible_collections.namespace.collection.plugins.module_utils.something.else; \n" \
                     "using ansible_collections.namespace.collection.plugins.module_utils.something; \n" \
                     "using ansible_collections.namespace.collection.plugins.module_utils.something.else; \n" \
                     "using ansible_collections.namespace.collection.plugins.module_utils.something; \n" \
                     "using Ansible.ModuleUtils.something; \n" \
                     "using Ansible.ModuleUtils.something.else; \n"
    expect_cs_utils

# Generated at 2022-06-12 21:50:29.467763
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    psmdf = PSModuleDepFinder()
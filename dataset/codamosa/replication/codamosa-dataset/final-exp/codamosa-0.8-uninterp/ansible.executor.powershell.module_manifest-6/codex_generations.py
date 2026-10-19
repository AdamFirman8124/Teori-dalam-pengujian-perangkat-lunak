

# Generated at 2022-06-12 21:41:01.115819
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Arrange
    name = 'win_dns_client'
    data = pkgutil.get_data("ansible.executor.powershell", to_native(name + ".ps1"))
    ps_finder =  PSModuleDepFinder()
    # Act
    result = ps_finder.scan_exec_script(name)
    # Assert
    assert result is not None


# Generated at 2022-06-12 21:41:05.677919
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # GIVEN
    ps_module_dep_finder = PSModuleDepFinder()

    # WHEN
    ps_module_dep_finder.scan_exec_script("main")

    # THEN
    assert len(ps_module_dep_finder.exec_scripts) > 0


# this is used by the cs_wrapper

# Generated at 2022-06-12 21:41:14.972139
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_module("# Requires -Module Ansible.ModuleUtils.Basic")
    assert "Ansible.ModuleUtils.Basic" in dep_finder.ps_modules
    dep_finder.scan_module("# Requires -Module Ansible.ModuleUtils.Basic -Module Ansible.ModuleUtils.Logging")
    assert "Ansible.ModuleUtils.Basic" in dep_finder.ps_modules
    assert "Ansible.ModuleUtils.Logging" in dep_finder.ps_modules
    dep_finder.scan_module("# Requires -Module Ansible.ModuleUtils.Basic\n# Requires -Module Ansible.ModuleUtils.Logging")
    assert "Ansible.ModuleUtils.Basic" in dep_finder.ps_modules

# Generated at 2022-06-12 21:41:17.810844
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    result = PSModuleDepFinder().scan_exec_script('hello')
    assert result == 'passed'



# Generated at 2022-06-12 21:41:31.339240
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import os

    from ansible.module_utils.compat import tempfile, os
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    from ansible.plugins.loader import ps_module_utils_loader
    from ansible.utils.collection_loader import get_collection_name
    from ansible.utils.display import Display
    from ansible.utils.hashing import secure_hash, secure_hash_s

    display = Display()

    def mock_open(*args, **kwargs):
        return tempfile.NamedTemporaryFile(delete=False)

    class MockModuleUtilsPluginLoader(object):

        def __init__(self, display):
            self._plugin_count = 0
            self._plugin_

# Generated at 2022-06-12 21:41:34.843996
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("execution_wrapper")
    assert finder.exec_scripts.get("execution_wrapper", None) is not None



# Generated at 2022-06-12 21:41:44.135692
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # PSModuleDepFinder.scan_module() should assign expected values to self.ps_modules
    finder = PSModuleDepFinder()
    obj = dict()
    finder.ps_modules = obj


# Generated at 2022-06-12 21:41:50.405428
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psModuleDepFinder = PSModuleDepFinder()
    psModuleDepFinder.scan_exec_script("standard_wrapper")
    print(psModuleDepFinder.exec_scripts)
    print(psModuleDepFinder.cs_utils_wrapper)
    # This test will fail, since the pkgutil not finding the data
    print("Test with pwsh_wrapper, expect an exception")
    psModuleDepFinder.scan_exec_script("pwsh_wrapper")
test_PSModuleDepFinder_scan_exec_script()


# Generated at 2022-06-12 21:41:51.454868
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True

# Generated at 2022-06-12 21:42:01.064723
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test scan_exec_script with a real powershell script that imports a C# module util
    depfinder = PSModuleDepFinder()

    exec_script_name = 'Get-AnsibleModuleUtilBasePath'
    depfinder.scan_exec_script(exec_script_name)
    assert depfinder.exec_scripts[exec_script_name] is not None
    assert depfinder.cs_utils_wrapper['Ansible.Common.ArgumentSpec'] is not None

    # Test scan_exec_script with an invalid powershell script
    invalid_exec_script_name = 'not-a-real.ps1'

# Generated at 2022-06-12 21:42:22.963016
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_cases = [
        # test_case, expected
        # Test normal return
        ("TestScriptName", 1),
        # Test None return
        ("TestScriptName1234", 0),
    ]

    for test_case in test_cases:
        dep_finder = PSModuleDepFinder()
        dep_finder.scan_exec_script(test_case[0])
        assert len(dep_finder.exec_scripts) == test_case[1]

# Generated at 2022-06-12 21:42:27.214835
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mod_dep_finder = PSModuleDepFinder()
    name = mod_dep_finder.scan_exec_script("./test_data/test_file_1.ps1")
    assert name == "test_data_test_file_1", "test_PSModuleDepFinder_scan_exec_script failed"



# Generated at 2022-06-12 21:42:28.273596
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:42:31.125008
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test for successful scan_exec_script
    c1 = PSModuleDepFinder()
    module_result = c1.scan_exec_script('main')
    assert True == module_result

# Generated at 2022-06-12 21:42:42.736620
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    PSModuleDepFinder = PSModuleDepFinder()
    PSModuleDepFinder.scan_module(b"#requires -mod Ansible.ModuleUtils.1.0")
    assert sorted(PSModuleDepFinder.ps_modules.keys()) == ["Ansible.ModuleUtils.1.0"]
    PSModuleDepFinder.scan_module(b"import util1.util2")
    assert sorted(PSModuleDepFinder.ps_modules.keys()) == ["Ansible.ModuleUtils.1.0"]
    PSModuleDepFinder.scan_module(b"#Requires -Module Ansible.ModuleUtils.AnotherUtil")

# Generated at 2022-06-12 21:42:44.331384
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # TODO: Write unit test for scan_exec_script of class PSModuleDepFinder
    pass


# Generated at 2022-06-12 21:42:50.331600
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    ps_module = PSModuleDepFinder()
    ps_module.scan_module("")
    assert ps_module.ps_modules == dict()
    assert ps_module.cs_utils_wrapper == dict()
    assert ps_module.cs_utils_module == dict()
    assert ps_module.ps_version == None
    assert ps_module.os_version == None
    assert ps_module.become == False


# Generated at 2022-06-12 21:42:53.184479
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script(b"basic")



# Generated at 2022-06-12 21:42:53.913727
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass

# Generated at 2022-06-12 21:43:06.297864
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:43:25.483816
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    f = PSModuleDepFinder()
    f.scan_exec_script(b"ansible.module_utils.powershell.crypto")

    assert f.exec_scripts[b"ansible.module_utils.powershell.crypto"]
    assert len(f.ps_modules) > 0
    assert len(f.cs_utils_wrapper) == 0
    assert len(f.cs_utils_module) == 0


# Generated at 2022-06-12 21:43:33.578614
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.common.collections import Mapping
    from ansible.module_utils.ansible_release import __version__ as ansible_release_version
    from ansible.module_utils.common.text.converters import to_str
    from ansible.module_utils.common.validation import check_type_list
    from ansible.module_utils.common.validation import check_type_dict
    from ansible.module_utils.common.validation import check_type_set
    from ansible.module_utils.powershell.converter import require_powershell_or_die
    from ansible.module_utils.powershell.converter import PS_VERSION
    from ansible.module_utils.powershell.converter import unicode

# Generated at 2022-06-12 21:43:45.373342
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    def _slurp(path):
        with open(path, 'rb') as fp:
            return fp.read()

    base64_bytes = base64.b64encode(to_bytes(ps_example_module.replace('\n', '')))
    ps_module_data = to_bytes('''#! %s
#Requires -Module Ansible.ModuleUtils.Legacy
#Requires -Module Ansible.ModuleUtils.Unix
#AnsibleRequires -CSharpUtil Ansible.Windows.AnsibleModule
%s''' % (C.DEFAULT_BECOME_EXE, base64_bytes))

    fd, path = tempfile.mkstemp()
    f = os.fdopen(fd, 'wb')
    f.write(ps_module_data)
    f.close()



# Generated at 2022-06-12 21:43:47.156459
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    depfinder = PSModuleDepFinder()
    depfinder.scan_exec_script('common')


# Generated at 2022-06-12 21:43:56.294981
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class TestObject(object):
        def __init__(self):
            self.cs_utils_wrapper = dict()
            self.ps_modules = dict()
            self.exec_scripts = dict()
            self.ps_version = None
            self.os_version = None
            self.become = False
    test_obj = TestObject()

    test_obj.scan_exec_script("winrm")
    assert test_obj.exec_scripts.keys() == ["winrm"]
    assert test_obj.cs_utils_wrapper.keys() == ['Ansible.ModuleUtils.Utils']
    assert test_obj.ps_modules.keys() == ['Ansible.ModuleUtils.Utils']
    assert test_obj.ps_version == '5.1'

# Generated at 2022-06-12 21:44:06.662234
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    #
    test_cases =[
        # test_name, ps_script_name, expected_output
        ("test case 1", "common", []),
        ("test case 2", "posixcommon", []),
        ("test case 3", "wincommon", [])

    ]
    for test_case in test_cases:
        print("\nRunning test case '{}'".format(test_case[0]))
        psModuleDepFinder = PSModuleDepFinder()
        output = psModuleDepFinder.scan_exec_script(test_case[1])
        assert output == test_case[2]


if __name__ == "__main__":
    test_PSModuleDepFinder_scan_exec_script()




# Generated at 2022-06-12 21:44:11.121223
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    module_name = "module_name"
    file_data = None
    # TODO: reset_deps

    finder = PSModuleDepFinder()
    finder.scan_module(file_data, fqn=module_name)
    assert finder.ps_modules == {}
    assert finder.exec_scripts == {}
    assert finder.cs_utils_wrapper == {}
    assert finder.cs_utils_module == {}
    assert finder.ps_version is None
    assert finder.os_version is None
    assert finder.become is False

# Generated at 2022-06-12 21:44:13.165974
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # tests for "scan_exec_script" are done below in test_compress_base_and_extras
    pass


# Generated at 2022-06-12 21:44:20.015361
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # This method is used to test the functionality of scan_module.
    # It will test the method against the following scenarios:
    # - The first scenario tests the case where both a module and a collection module are referenced.
    # - The second case tests the case where a module is referenced that does not exist.
    # - The third case tests the case where a collection module is referenced that does not exist.
    # The expected and actual results are asserted to be the same.
    ps_module_dep_finder = PSModuleDepFinder()
    assert ps_module_dep_finder.ps_modules == {}
    assert ps_module_dep_finder.cs_utils_module == {}


# Generated at 2022-06-12 21:44:23.411189
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    the_object = PSModuleDepFinder()
    the_object.scan_exec_script("powershell")
    assert the_object.exec_scripts['powershell'] != None


# Generated at 2022-06-12 21:44:36.723219
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    data = finder.scan_exec_script('script_name')


# Generated at 2022-06-12 21:44:39.809609
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_module(b'#Requires -Module Ansible.ModuleUtils.FakeUtil1\n#Requires -Module Ansible.ModuleUtils.FakeUtil2')
    assert dep_finder.ps_modules
    assert len(dep_finder.ps_modules) == 2
    assert b'Ansible.ModuleUtils.FakeUtil1' in dep_finder.ps_modules
    assert b'Ansible.ModuleUtils.FakeUtil2' in dep_finder.ps_modules



# Generated at 2022-06-12 21:44:45.476906
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test
    psmdf = PSModuleDepFinder()
    
    name = "BecomeGeneric"
    psmdf.scan_exec_script(name)
    
    # Test assertions
    psmdf = PSModuleDepFinder()
    assert psmdf.exec_scripts is not None
    assert len(psmdf.exec_scripts) > 0
    assert name in psmdf.exec_scripts



# Generated at 2022-06-12 21:44:57.088270
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    # unit test for method scan_module of class PSModuleDepFinder
    assert finder.ps_modules == {}
    assert finder.exec_scripts == {}
    assert finder.cs_utils_wrapper == {}
    assert finder.cs_utils_module == {}
    assert finder.ps_version is None
    assert finder.os_version is None
    assert finder.become is False
    finder.scan_exec_script("module_compile")
    assert finder.ps_modules == {}
    assert finder.exec_scripts == {}
    assert finder.cs_utils_wrapper == {}
    assert finder.cs_utils_module == {}
    assert finder.ps_version is None
    assert finder.os_version is None

# Generated at 2022-06-12 21:45:01.395150
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    obj = PSModuleDepFinder()
    module_data = "test"
    fqn = "test"
    wrapper = False
    powershell = True
    assert obj.scan_module(module_data, fqn, wrapper, powershell) == None
   

# Generated at 2022-06-12 21:45:12.022051
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:45:15.327412
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """Unit test of method PSModuleDepFinder.scan_exec_script"""
    depfinder = PSModuleDepFinder()
    depfinder.scan_exec_script('test')
    assert depfinder.exec_scripts['test'] == 'test script data'  # Test with a simple string as the module


# Generated at 2022-06-12 21:45:26.076588
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Initialize the test suite
    file_name_csharp = "./File_CSharpCode"
    file_name_powershell = "./File_PowerShellCode"
    file_name_wrapper = "./File_ExecWrapper"
    def test_exec_script_wrapper(script_name):
        def return_fake_content():
            content = "return '{0}'".format(script_name)
            return content
        ps_module_path = os.path.join(C.DEFAULT_MODULE_PATH, "windows", "./item_ScheduledTask_ps1")
        def mock_get_data(package_name, resource_name):
            content = return_fake_content()
            return to_bytes(content)

# Generated at 2022-06-12 21:45:36.876409
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # get list of all ps modules under unit test
    ps_modules = [item[:-5] for item in os.listdir(os.path.join(os.path.dirname(__file__), "unit", "module_utils", "powershell")) if item.endswith(".psm1")]
    ps_csharp_modules = [item[:-3] for item in os.listdir(os.path.join(os.path.dirname(__file__), "unit", "module_utils", "powershell")) if item.endswith(".cs")]

    finder = PSModuleDepFinder()

    # Exec powershell scripts used in module exec wrappers
    finder.scan_exec_script('ansible_powershell')

    # Builtin module_utils
    for module_name in ps_modules:
        module

# Generated at 2022-06-12 21:45:42.356412
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("exit_json")
    assert "exit_json" in dep_finder.exec_scripts
    assert "ansible_collections.ansible.builtin.plugins.module_utils.powershell.common" in dep_finder.cs_utils_wrapper
    assert "ansible_collections.ansible.builtin.plugins.module_utils.powershell.common" in dep_finder.ps_modules


# Generated at 2022-06-12 21:46:05.567913
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_object = PSModuleDepFinder()
    result = test_object.scan_exec_script("testcase1")
    pass

# Generated at 2022-06-12 21:46:13.353483
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:46:23.157189
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mu_scanner = PSModuleDepFinder()
    mu_scanner.scan_module("")
    if mu_scanner.ps_modules.keys():
        print("Imported module_util PSM1 found:")
        for name, data in mu_scanner.ps_modules.items():
            print("Name: %s Data: %s" % (name, data))
    else:
        print("No PSM1 found")

    if mu_scanner.cs_utils_module.keys():
        print("Imported module_util CS found:")
        for name, data in mu_scanner.cs_utils_module.items():
            print("Name: %s Data: %s" % (name, data))
    else:
        print("No CS found")


# Generated at 2022-06-12 21:46:28.568504
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script(b'ansible.powerbase.common')
    assert isinstance(psmdf.exec_scripts, dict)
    assert psmdf.exec_scripts['ansible.powerbase.common'].startswith(b'#Comment')


# Generated at 2022-06-12 21:46:36.354390
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print("test_PSModuleDepFinder_scan_exec_script: START")
    from ansible.executor.task_executor import ExecutorPreloader
    from ansible.plugins.loader import ps_module_utils_loader
    ps_module_utils_loader.find_plugin('Ansible.ModuleUtils.Parsing', '.psm1')
    preloader = ExecutorPreloader()
    assert(preloader)
    preloader._ps_module_dep_finder.scan_exec_script('wrapper')
    print("test_PSModuleDepFinder_scan_exec_script: FINISH")



# Generated at 2022-06-12 21:46:39.407998
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_PSModuleDepFinder = PSModuleDepFinder()
    # Testing with a valid name value
    test_PSModuleDepFinder.scan_exec_script("name")
    assert "name" in test_PSModuleDepFinder.exec_scripts.keys()


# Generated at 2022-06-12 21:46:43.073687
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    p = PSModuleDepFinder()
    # assert p.scan_exec_script('ansible.module_utils.powershell.base') == None
    # assert raise(AnsibleError,'Could not find executor powershell script for \'%s\'') == None


# Generated at 2022-06-12 21:46:46.865020
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('executor')
    assert finder.exec_scripts['executor']
    assert finder.ps_modules.get('Ansible.ModuleUtils.Common')
    assert not finder.cs_utils_wrapper


# Generated at 2022-06-12 21:46:59.194361
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.utils.collection_loader import _load_collections
    from ansible.utils.plugin_docs import get_docstring
    from ansible.parsing.yaml.dumper import AnsibleDumper

    docsnippets = to_bytes(get_docstring(
        PSModuleDepFinder,
        exclude_lines=["GetType", "ToString", "Equals"],
        vm_override_vars={'version': '2.10', 'gather_subset': 'all'},
    ))

    def get_term_data(name, docsnippet):
        # Mimic the user asking to generate powershell documentation with the given docsnippet
        docsnippet = json.loads(docsnippet)
        # Use the docsnippet to find the script name
        collection, module_name

# Generated at 2022-06-12 21:47:08.782544
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class MockedPSModuleDepFinder(PSModuleDepFinder):
        def __init__(self):
            self.ps_modules = dict()
            self.exec_scripts = dict()
            self.scanned_exec_scripts = set()

        def scan_module(self, module_data, fqn=None, wrapper=False, powershell=True):
            self.scanned_exec_scripts.add(fqn)

    finder = MockedPSModuleDepFinder()

    finder.scan_exec_script(to_native("foo"))

    assert finder.exec_scripts
    assert finder.scanned_exec_scripts

    # Test exception when script not found

# Generated at 2022-06-12 21:48:38.593385
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.plugins.loader import ps_module_utils_loader
    import ansible.executor.powershell
    # This is a very basic test, but it does test the load functionality
    # This is used by validate-modules to get a module's required utils in base and in a collection.
    x = PSModuleDepFinder()
    x.scan_exec_script('TestConvertTo')

    assert 'TestConvertTo' in x.exec_scripts.keys()
    assert 'TestConvertFrom' in x.exec_scripts.keys()

    assert x.ps_modules['Ansible.ModuleUtils.AnsibleModuleHelper']['path'] == ps_module_utils_loader.find_plugin('Ansible.ModuleUtils.AnsibleModuleHelper')

# Generated at 2022-06-12 21:48:47.619276
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import unittest

    class _MockModule(object):
        def __init__(self, module_args):
            self.params = module_args
            self.check_mode = False
            self.changed = False

    class _MockAnsibleModule(object):
        def __init__(self, module_name, module_args):
            self.module_name = module_name
            self.module = _MockModule(module_args)

        def exit_json(self, **kwargs):
            self.exit_args = kwargs
            self.exit_args['invocation'] = self.module._original_basename

        def fail_json(self, **kwargs):
            self.fail_args = kwargs
            self.fail_args['invocation'] = self.module._original_basename

   

# Generated at 2022-06-12 21:48:49.438035
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("TestScript")
    assert finder.exec_scripts["TestScript"] == b'Script Data'

# Unit tests for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:48:51.204201
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmd = PSModuleDepFinder()
    psmd.scan_exec_script('powershell_base')


# Generated at 2022-06-12 21:49:01.423604
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.common._collections_compat import Mapping
    import sys
    import base64
    import json
    import tempfile
    import os
    import shutil
    import urllib.parse  # noqa pylint: disable=E0401
    import collections


    test_dir = os.path.dirname(os.path.dirname(__file__))
    test_dir = os.path.join(test_dir, "test_data")
    module_dir = os.path.join(test_dir, "modules")
    module_utils_dir = os.path.join(test_dir, "module_utils")
    wrappers_dir = os.path.join(test_dir, "executor", "powershell")


# Generated at 2022-06-12 21:49:03.397506
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    PSModuleDepFinder().scan_exec_script(name)

# Unit tests for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:49:11.227131
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    fnd = PSModuleDepFinder()

    # Add some garbage data to the instance variables
    fnd.exec_scripts['foo'] = 'bar'
    fnd.cs_utils_wrapper['foo'] = 'bar'
    fnd.ps_modules['foo'] = 'bar'

    assert fnd.scan_module('Foo', fqn=None, wrapper=False, powershell=True) == None
    assert fnd.scan_module('Foo', fqn=None, wrapper=False, powershell=False) == None
    assert fnd.scan_module('Foo', fqn=None, wrapper=True, powershell=True) == None
    for x in fnd.cs_utils_wrapper:
        assert x == 'foo'

# Generated at 2022-06-12 21:49:12.695111
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass # test is in test_module_loader_integration.py


# Generated at 2022-06-12 21:49:15.547420
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psModuleDepFinder = PSModuleDepFinder()
    assert isinstance(psModuleDepFinder, object)

# Generated at 2022-06-12 21:49:26.731931
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    b_data = to_bytes(pkgutil.get_data("ansible.executor.powershell", "ps_main.ps1"))

    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('ps_main')
    assert dep_finder.exec_scripts['ps_main'] == _strip_comments(b_data)

    b_data = to_bytes(pkgutil.get_data("ansible.executor.powershell", "ps_common_wrapper.ps1"))
    dep_finder.scan_exec_script('ps_common_wrapper')
    assert dep_finder.exec_scripts['ps_common_wrapper'] == _strip_comments(b_data)

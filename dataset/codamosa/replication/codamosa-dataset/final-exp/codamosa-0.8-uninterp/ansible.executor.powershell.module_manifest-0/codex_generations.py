

# Generated at 2022-06-12 21:40:53.000662
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass


# Generated at 2022-06-12 21:40:59.940632
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """scan_module method of PSModuleDepFinder class."""
    from ansible.module_utils.common.collections import AnsibleCollectionRef
    finder = PSModuleDepFinder()
    fqn_collection = ["ansible_collections.ns.coll", "plugins.module_utils.psmodule"]
    module_utils = AnsibleCollectionRef.from_parts(fqn_collection,
        "psmodule")
    finder.scan_module(module_utils, fqn="ansible_collections.ns.coll.plugins.module_utils.psmodule",
        powershell=True)
    assert finder.become
    assert finder.cs_utils_module
    assert finder.ps_modules

# Generated at 2022-06-12 21:41:10.149456
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()
    finder.scan_module(b"no match")
    assert len(finder.cs_utils_wrapper.keys()) == 0
    assert len(finder.cs_utils_module.keys()) == 0
    assert len(finder.ps_modules.keys()) == 0

    # cs_utils
    # requires -Module Ansible.ModuleUtils.PowerShell
    finder.scan_module(b"#Requires -Module Ansible.ModuleUtils.PowerShell")
    assert len(finder.cs_utils_wrapper.keys()) == 0
    assert len(finder.cs_utils_module.keys()) == 1
    assert "Ansible.ModuleUtils.PowerShell" in finder.cs_utils_module
    # requires -Module Ansible.ModuleUtils.CommonUtils
    finder.scan

# Generated at 2022-06-12 21:41:15.594161
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_module(b'#AnsibleRequires -PowerShell Ansible.ModuleUtils.Posh-SSH\n')
    assert finder.ps_modules['Ansible.ModuleUtils.Posh-SSH']['data'].startswith(b'#####')


# Generated at 2022-06-12 21:41:28.774869
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:41:34.754921
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    def _scan_module_test_helper(dep_finder, data, expected_keys, expected_count, expected_deps=None):
        dep_finder.scan_module(data)
        assert len(dep_finder.ps_modules) == expected_count

        for key in expected_keys:
            assert key in dep_finder.ps_modules

        if expected_deps:
            for key in expected_deps:
                assert key in dep_finder.ps_modules[expected_deps[key]]

    # Test: empty file
    df1 = PSModuleDepFinder()
    _scan_module_test_helper(df1, b'', [], 0)

    # Test: Requires and AnsibleRequires should be found
    df2 = PSModuleDepFinder()

# Generated at 2022-06-12 21:41:41.285355
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()

    # Test that the module can find a valid script to scan
    dep_finder.scan_exec_script("common")
    assert dep_finder.exec_scripts["common"]

    # Test that the module can't find a valid script to scan
    try:
        dep_finder.scan_exec_script("common")
    except AnsibleError:
        pass
    else:
        assert False, "An error should have been raised for missing module."



# Generated at 2022-06-12 21:41:43.330196
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import ansible.executor.powershell as powershell
    import pkgutil
    #TODO
    #assert False

# Generated at 2022-06-12 21:41:47.463929
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    print("----------------- test case 1 -----------------")
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script("common_test_footer")
    assert ps_module_dep_finder
    print("----------------- test case 1 over -----------------")



# Generated at 2022-06-12 21:41:56.894745
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    os.chdir(os.path.realpath(os.path.dirname(__file__)))
    d = PSModuleDepFinder()
    d.scan_exec_script('ExecutionWrapper')

    assert len(d.cs_utils_wrapper) == 4
    assert set(d.cs_utils_wrapper.keys()) == {'Ansible.AnsibleCollection', 'Ansible.AnsibleCollection.Core.TypeExtensions', 'Ansible.AnsibleCollection.Core.AnsibleObject', 'Ansible.AnsibleCollection.Core.Runtime'}

    assert len(d.ps_modules) == 4

# Generated at 2022-06-12 21:42:13.927509
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.power_shell.executor.wrapper import ModuleExecWrapper
    from ansible.plugins.loader import module_loader
    from ansible.utils.collection_loader import AnsibleCollectionRef
    from ansible import context

    data = pkgutil.get_data("ansible.executor.powershell", "wrapper.ps1")
    context.CLIARGS = {'become': True, 'become_method': 'runas', 'become_user': 'bob'}

    wrapper = ModuleExecWrapper(b'', '', '', None, AnsibleCollectionRef(None, None, None, None, None, None), data)

    collection = AnsibleCollectionRef.from_fqcr(to_text('ansible_collections.ansible.builtin.ping'))
    module = module_

# Generated at 2022-06-12 21:42:19.659222
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    group_name = "data_encoder"
    test_data_folder = "test_data"
    fixture_file_name = "utils-powershell-conversion.ps1"
    fixture_file_path = "{}/{}".format(test_data_folder, fixture_file_name)
    with open(fixture_file_path, 'r') as fixture_file:
        fixture_file_contents = fixture_file.read()
        fixture_file_contents = fixture_file_contents.encode()
        
    finder = PSModuleDepFinder()
    
    #execute test
    finder.scan_exec_script(group_name)
    
    #verify results
    assert finder.exec_scripts[group_name] == fixture_file_contents

# Generated at 2022-06-12 21:42:27.859167
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import ansible.executor.powershell

    ansible.executor.powershell.module_data = {
        "test_exec": b"test_module_data",
    }

    # Test a valid module name
    md = PSModuleDepFinder()
    md.scan_exec_script("test_exec")

    assert md.exec_scripts["test_exec"] == "test_module_data"

    # Test an invalid module name
    md = PSModuleDepFinder()
    try:
        md.scan_exec_script("test_exec_invalid")
    except AnsibleError:
        pass
    else:
        assert False  # The above code should raise an exception

    ansible.executor.powershell.module_data = None


# Generated at 2022-06-12 21:42:30.377078
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print("Testing Method scan_exec_script")
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script(u"posh-receive")

# Generated at 2022-06-12 21:42:32.081067
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test is difficult to perform given that it is a class method and uses external data
    assert True == True

# Generated at 2022-06-12 21:42:43.423167
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Tests if pkgutil.get_data() is called once with the correct parameters and if scan_module() is called twice with the correct parameters.
    # Arrange
    # Create a mock of pkgutil.get_data() to be able to assert if it was called with the correct parameters.
    mock_get_data = MagicMock(name="get_data")
    mock_get_data.return_value = b""
    ansible_executor_powershell = MagicMock()
    type(ansible_executor_powershell).get_data = mock_get_data

    # Create a mock of PSModuleDepFinder.scan_module and overwrite the actual method with the mock to be able to assert if it was called with the correct parameters.
    mock_scan_module = MagicMock(name="scan_module")
    psmdf = PS

# Generated at 2022-06-12 21:42:54.212089
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.cloud import _to_base64

    # This is the same logic in powershell_runner.py
    def _generate_hash(data):
        """
        Returns a hash of the data that will be used as the powershell script
        name so we only generate it once for use on multiple hosts
        """
        script_hash = ('%d' % random.randint(0, 2147483647)).zfill(10)
        if isinstance(data, (unicode, str)):
            data = to_bytes(data, errors='surrogate_escape')
        script_hash = 'script%s' % script_hash
        # TODO: rewrite to use the script module so we don't have to do this
        # weird encoding here.

# Generated at 2022-06-12 21:43:06.617767
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    md = PSModuleDepFinder()
    md.scan_module(base64.b64decode(b'I2V4ZWN1dG9yIGNvbW1hbmQgZ3JhcnRlZAoKI25lZWQgdGhlIGRpcmVjdG9yeSBwYXRoCmV4ZWN1dG9ydXJpPSRhcmd2WzBdCg=='),wrapper=True, powershell=True)
    assert 1 == len(md.ps_modules.keys())

# Generated at 2022-06-12 21:43:08.457997
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:43:13.003399
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # given
    finder = PSModuleDepFinder()
    # when

# Generated at 2022-06-12 21:43:33.237038
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:43:38.218553
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script('powershell-args')
    assert len(ps_module_dep_finder.exec_scripts) == 1
    assert ps_module_dep_finder.exec_scripts.get('powershell-args') is not None


# Generated at 2022-06-12 21:43:49.194677
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Testing with a random name
    finder = PSModuleDepFinder()
    name = str(random.randint(1, 10000))
    finder.scan_exec_script(name)
    imported_script = finder.exec_scripts.get(name)
    assert imported_script is None
    assert name not in finder.exec_scripts.keys()

    # Testing with a real file path
    finder = PSModuleDepFinder()
    name = 'init'
    finder.scan_exec_script(name)
    imported_script = finder.exec_scripts.get(name)
    assert imported_script is not None
    assert 'requires -module' not in str(imported_script).lower()
    assert name in finder.exec_scripts.keys()



# Generated at 2022-06-12 21:43:49.816523
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:43:57.875318
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import tests.utils as utils
    from ansible.playbook.play_context import PlayContext

    if pkgutil.find_loader("ansible_collections.ns.coll.plugins.module_utils.basic_module_utils") is None:
        pkgutil.register_finder(utils.MockModuleFinder("ansible_collections.ns.coll.plugins.module_utils.basic_module_utils"),
                                path=["ansible_collections.ns.coll.plugins.module_utils.basic_module_utils"])


# Generated at 2022-06-12 21:43:59.622487
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    o = PSModuleDepFinder()
    o.scan_exec_script("foo")


# Generated at 2022-06-12 21:44:11.031447
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import types

    import ansible.executor.powershell
    # A module_util with no dependencies

    ps_module_util_data = pkgutil.get_data('ansible.module_utils.common.remote_management.scx', 'scx.psm1')
    psm = PSModuleDepFinder()
    psm.scan_module(ps_module_util_data)
    assert len(psm.ps_modules.keys()) == 1
    assert len(psm.cs_utils_module.keys()) == 0
    assert len(psm.cs_utils_wrapper.keys()) == 0
    assert len(psm.exec_scripts.keys()) == 0

    # A module_util with a dependency on itself, it should not add the dependency again

# Generated at 2022-06-12 21:44:23.922142
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print("")
    n_name_1 = "test-fQcR"
    n_name_2 = "test-FQCR"
    p_name_1 = "test-FQCR"
    p_name_2 = "test-fqcr"
    print("Name 1", n_name_1)
    print("Name 2", n_name_2)
    print("Name 2", p_name_2)
    print("Name 1", p_name_1)
    print("Name 1", (n_name_1 == n_name_2))
    print("Name 1", (p_name_1 == p_name_2))
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script(n_name_1)
    ps_

# Generated at 2022-06-12 21:44:33.587939
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """Test scan_exec_script() method of PSModuleDepFinder class."""
    # Setup test
    test_finder = PSModuleDepFinder()
    test_name = 'ansible_test_name'
    test_script = b'#'

    # Execute test
    test_finder.exec_scripts = {
        test_name: test_script,
    }
    test_finder.scan_exec_script(test_name)

    # Assert that scan_exec_script didn't change anything
    assert test_finder.exec_scripts[test_name] == test_script



# Generated at 2022-06-12 21:44:45.152786
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import tempfile
    import shutil
    from ansible.module_utils.basic import AnsibleModule

    # construct a temporary directory for the powershell executor scripts
    tmpdir = tempfile.mkdtemp()
    shutil.copytree(old_dir="lib/ansible/executor/powershell", new_dir=tmpdir)

    # construct a temporary module_utils location
    tmp_psm_dir = tempfile.mkdtemp()
    external_powershell_module = {
        "module_utils": tmp_psm_dir
    }

    module_loader_args = {
        "module_utils_paths": [external_powershell_module],
        "powershell_executor_script": os.path.join(tmpdir, "Powershell.ps1"),
    }
    AnsibleModule.add_module

# Generated at 2022-06-12 21:45:10.244701
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import pytest
    from ansible_galaxy.models.module_utils.module_util_mixed import MixedModuleUtil
    import ansible_collections.testns.testcoll.plugins.module_utils.test_module_utils as test_module_utils
    from ansible_collections.testns.testcoll.tests.unit.test_module_util_mixed import temp_collection_path

    # Test loading module_util and parsing version.
    finder = PSModuleDepFinder()
    finder.scan_module(pkgutil.get_data('ansible_collections.testns.testcoll.plugins.module_utils', 'test_module_util.psm1'))
    assert finder.ps_modules['Ansible.ModuleUtils.TestModuleUtil']['data'] == pkgutil.get_data

# Generated at 2022-06-12 21:45:18.342135
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    def _test_helper(dep_finder, module_data, fqn=None, wrapper=False):
        dep_finder.scan_module(module_data)
        assert dep_finder.ps_modules == expected_ps_modules
        assert dep_finder.cs_utils_wrapper == expected_cs_utils_wrapper
        assert dep_finder.cs_utils_module == expected_cs_utils_module

    dep_finder = PSModuleDepFinder()
    expected_ps_modules = {"Ansible.ModuleUtils.Foo": None, "Ansible.ModuleUtils.Bar": None}
    expected_cs_utils_module = {"Ansible.ModuleUtils.Foo": None}
    expected_cs_utils_wrapper = {"Ansible.ModuleUtils.Foo": None}
    module_data = to_

# Generated at 2022-06-12 21:45:25.695862
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psModuleDepFinderObject = PSModuleDepFinder()
    psModuleDepFinderObject.scan_exec_script("ExecutionWrapper")
    assert psModuleDepFinderObject.exec_scripts[u"ExecutionWrapper"]


if __name__ == '__main__':
    # Unit test for method scan_module of class PSModuleDepFinder
    test_PSModuleDepFinder_scan_module()

    # Unit test for method scan_exec_script of class PSModuleDepFinder
    test_PSModuleDepFinder_scan_exec_script()

# Generated at 2022-06-12 21:45:31.744477
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.common._text import to_text
    f = PSModuleDepFinder()
    f.scan_exec_script("basic")
    if not ("basic" in f.exec_scripts):
        raise Exception("")

    if not (to_text("basic") in f.exec_scripts):
        raise Exception("")

    f.scan_exec_script("basic")



# Generated at 2022-06-12 21:45:41.241594
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    fails = 0

    def assert_eq(expected, got):
        if expected != got:
            raise AssertionError("Expected '%s', got '%s' instead" % (expected, got))

    # Create some fake module_utils
    def make_psm1(path, data):
        with open(path, 'wb') as f:
            f.write(data)

    def make_cs(path, data):
        with open(path, 'wb') as f:
            f.write(data)

    temp = tempfile.mkdtemp()


# Generated at 2022-06-12 21:45:52.955386
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    """
    test_PSModuleDepFinder_scan_module()
    """
    test_case_1 = PSModuleDepFinder()
    test_case_1.scan_module(b'#Requires -Module Ansible.ModuleUtils.TestMethod1\n#\n#Requires -Module Ansible.ModuleUtils.TestMethod2\n#\n#Requires -Module Ansible.ModuleUtils.TestMethod3\n')
    assert len(test_case_1.ps_modules) == 3

    test_case_2 = PSModuleDepFinder()

# Generated at 2022-06-12 21:45:57.111876
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # test_PSModuleDepFinder_scan_exec_script(self)
    f = PSModuleDepFinder()
    m = to_text(random.random())
    f.scan_exec_script(m)
    assert f.exec_scripts[m] != ""


# Generated at 2022-06-12 21:46:06.854999
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:46:09.828137
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()

    ps_module_dep_finder.scan_exec_script('wrapper')
    assert len(ps_module_dep_finder.ps_modules) > 0
    

# Generated at 2022-06-12 21:46:11.188176
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:46:35.926450
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    scanner = PSModuleDepFinder()

    # test the import of module_utils from the stdlib
    module_data = b"""#Requires -Module Ansible.ModuleUtils.Legacy
#Requires -Module Ansible.ModuleUtils.Network
#Requires -Module Ansible.ModuleUtils.Network.Legacy
#Requires -Module Ansible.ModuleUtils.Network.Network.Common
#Requires -Module Ansible.ModuleUtils.Network.Network.F5"""
    scanner.scan_module(module_data)
    assert len(scanner.ps_modules.keys()) == 5

    # test the import of module_utils from a collection

# Generated at 2022-06-12 21:46:42.805064
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.plugins.loader import module_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from collections import namedtuple
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.plugins.callback.default import CallbackModule


# Generated at 2022-06-12 21:46:50.474216
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    isinstance(PSModuleDepFinder, object)
    isinstance(dict, object)
    isinstance(bool, object)
    
    
    
    
    
    
    
    # Unit test for method scan_module of class PSModuleDepFinder
    def test_PSModuleDepFinder_scan_module():
        isinstance(PSModuleDepFinder, object)
        isinstance(bool, object)
        
        
        
        
        
        
        # Unit test for method _add_module of class PSModuleDepFinder
        def test_PSModuleDepFinder__add_module():
            isinstance(PSModuleDepFinder, object)
            isinstance(set, object)
            isinstance(dict, object)
            isinstance(bool, object)
            isinstance(str, object)

# Generated at 2022-06-12 21:46:57.587866
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    depfinder = PSModuleDepFinder()
    depfinder.sca
    n_module(to_bytes(MODULE_DATA_PS_WITH_REQS),
             fqn="ansible_collections.foo.bar.plugins.modules.mymodule", powershell=True)

    assert depfinder.ps_modules == PS_MODULES
    assert depfinder.cs_utils_wrapper == CS_UTILS_WRAPPER



# Generated at 2022-06-12 21:47:01.196631
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    scanner = PSModuleDepFinder()
    scanner.scan_exec_script(b'ScriptName.ps1')
    assert scanner.exec_scripts[b'ScriptName.ps1'] != b''


# Generated at 2022-06-12 21:47:10.046262
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.executor.powershell.common import WIN_UNSUPPORTED_DISTROS
    psmdf = PSModuleDepFinder()
    res = psmdf.scan_exec_script("file_info")
    assert res is None
    res = psmdf.scan_exec_script("win_stat")
    assert res is None
    res = psmdf.scan_exec_script("win_dsc")
    assert res is None
    res = psmdf.scan_exec_script("win_copy_module")
    assert res is None
    res = psmdf.scan_exec_script("win_package")
    assert res is None
    res = psmdf.scan_exec_script("win_psrepository")
    assert res is None

# Generated at 2022-06-12 21:47:16.535356
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Mock exit
    exit_code = None
    def mock_exit(code):
        global exit_code
        exit_code = code
        raise SystemExit(code)

    # Mock AnsibleError
    class MockAnswerError(AnsibleError):
        def __init__(self, msg=None):
            self.message = msg

    # Mock the AnsibleError class and its constructor
    MockAnsibleError = Mock(side_effect=MockAnswerError)

    # We force coverage for the purposes of this unit test but we will get
    # the code coverage for the base class.
    default_debug = C.DEFAULT_DEBUG
    C.DEFAULT_DEBUG = True


# Generated at 2022-06-12 21:47:25.538418
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:47:33.657532
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.loader import ps_module_utils_loader
    ps_module_utils_loader.populate_cache()

# Generated at 2022-06-12 21:47:45.267209
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Check that scan_module can process a module requiring C# class
    depfinder_cs = PSModuleDepFinder()
    # The test case is the file 'datetime.cs' with a reference to 'Base64.cs'
    # and with a Requires for a builtin module_util
    # The namespace used depends on the collection, in this case it is the default one

# Generated at 2022-06-12 21:48:01.840403
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # create instance of the class
    obj = PSModuleDepFinder()
    # call method scan_exec_script
    obj.scan_exec_script('module_wrapper')

# Generated at 2022-06-12 21:48:07.575825
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    import ansible.executor.powershell
    psmd = PSModuleDepFinder()
    psmd.scan_exec_script('common')
    assert 'common' in psmd.exec_scripts
    assert psmd.exec_scripts['common'] == pkgutil.get_data("ansible.executor.powershell", "common.ps1")

# The following is a helper to write tests for methods of class PSModuleDepFinder

# Generated at 2022-06-12 21:48:16.717708
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_data = b"""
#Requires -Version 3.0
#Requires -Module Ansible.ModuleUtils.PowerShell
#Requires -Module Ansible.ModuleUtils.Legacy

$ansible_module_data = @{}
$ansible_module_data['output'] = 'dGVzdA==' | ConvertFrom-Base64
$ansible_module_data['changed'] = $false
$ansible_module_data['failed'] = $false

$ansible_module_data
"""
    finder = PSModuleDepFinder()
    finder.scan_exec_script("_ansible_module_wrapper")
    assert finder.exec_scripts["_ansible_module_wrapper"] == test_data


# Test function _add_module for class PSModuleDepFinder

# Generated at 2022-06-12 21:48:18.455953
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script(): # noqa: E501
    obj = PSModuleDepFinder()
    obj.scan_exec_script(to_text(name))


# Generated at 2022-06-12 21:48:24.958491
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.common.removed import removed_module
    from ansible.module_utils import basic
    module_finder = PSModuleDepFinder()
    module_finder.scan_exec_script('basic')
    assert 'basic' in module_finder.exec_scripts
    assert 'run_command' in module_finder.cs_utils_wrapper
    assert 'removed' in module_finder.cs_utils_wrapper
    assert 'removed' in removed_module.__name__
    assert 'removed' in module_finder


# Generated at 2022-06-12 21:48:35.571832
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # instantiate PSModuleDepFinder object
    obj = PSModuleDepFinder()

    # call method scan_exec_script
    assert not obj.exec_scripts

    obj.scan_exec_script('test')

    # list of dicts containing psm1 files

# Generated at 2022-06-12 21:48:41.160697
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Initialize a new instance of class PSModuleDepFinder
    test_instance = PSModuleDepFinder()
    # Create a new instance of a mock class
    mock_name = mock.MagicMock()
    test_instance.scan_exec_script(mock_name)
    # Compare the actual and expected results
    assert test_instance.exec_scripts == {'mock_name': b''}



# Generated at 2022-06-12 21:48:48.288674
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("collection_loader")

# Generated at 2022-06-12 21:48:56.303189
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # We need to create an instance of the object for our test
    dep_finder = PSModuleDepFinder()
    # Create a test string that we can use as the initial content of our
    # module_data variable
    module_data = 'This is a test line'
    # Use to_bytes to convert our test string to a byte string
    b_module_data = to_bytes(module_data)
    # Since we are not calling any methods, we don't need to pass any arguments
    # to our test method
    dep_finder.scan_module(b_module_data)
    # assert that the result of our scan_module method is a list of length 1
    # and contains the original test string
    assert dep_finder.ps_modules == {}
    assert dep_finder.cs_utils_wrapper == {}
    assert dep_finder.cs

# Generated at 2022-06-12 21:49:01.478723
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:49:30.708844
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    print(json.dumps(PSModuleDepFinder().cs_utils_wrapper))
    print(json.dumps(PSModuleDepFinder().cs_utils_module))

# Generated at 2022-06-12 21:49:42.133637
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    # From a collection module
    # Get the module_util from a resource.
    data = pkgutil.get_data("ansible_collections.community.powershell.plugins.module_utils", "win_update.psm1")

    finder = PSModuleDepFinder()
    finder.scan_module(data, "ansible_collections.community.powershell.plugins.win_update")

    assert finder.ps_modules["Ansible.ModuleUtils.WinSystem.WindowsUpdate"]['path'].endswith("Ansible.ModuleUtils.WinSystem.WindowsUpdate.psm1")
    assert finder.ps_modules["Ansible.ModuleUtils.WinSystem.WindowsUpdate"]['data'].startswith(to_bytes("#region generated"))

# Generated at 2022-06-12 21:49:46.136502
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mdf = PSModuleDepFinder()
    mdf.scan_exec_script("naive")

    try:
        mdf.scan_exec_script("nonexistent")
        assert False
    except AnsibleError:
        # Should raise 'Could not find executor powershell script for'
        pass


# Generated at 2022-06-12 21:49:55.594481
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import ansible.executor.powershell.library

    module_finder = PSModuleDepFinder()


# Generated at 2022-06-12 21:50:03.655633
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test with valid arguments
    depfinder = PSModuleDepFinder()
    depfinder.scan_exec_script('Script')
    assert depfinder.exec_scripts['Script'].decode() == '$Script=@{}'

    # Test with invalid arguments
    depfinder = PSModuleDepFinder()
    try:
        depfinder.scan_exec_script('ScriptWrong')
    except AnsibleError:
        out = True
    assert out

    # Test with empty arguments
    depfinder = PSModuleDepFinder()
    try:
        depfinder.scan_exec_script('')
    except AnsibleError:
        out = True
    assert out


# Generated at 2022-06-12 21:50:15.595048
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    scanner = PSModuleDepFinder()

    ps_module_util_data = pkgutil.get_data("ansible.module_utils.common.powershell", "basic.psm1")

    scanner.scan_module(ps_module_util_data)
    assert "Ansible.Basic" in scanner.ps_modules.keys()
    assert "Ansible.AnotherBasic" not in scanner.ps_modules.keys()

    cs_module_util_data = pkgutil.get_data("ansible_collections.ns.coll.plugins.module_utils.common.CSharp_module_utils", "another_basic.cs")

    scanner.scan_module(cs_module_util_data, wrapper=False, powershell=False)
    assert "Ansible.AnotherBasic" in scanner.cs_utils_module.keys()

# Generated at 2022-06-12 21:50:25.586142
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:50:33.778280
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    actor = PSModuleDepFinder()
    name = "ExecCommon"
    data = pkgutil.get_data("ansible.executor.powershell", "ExecCommon.ps1")
    b_data = to_bytes(data)
    # when C.DEFAULT_DEBUG is true, exec_script is b_data
    actor.exec_scripts[name] = b_data
    # when C.DEFAULT_DEBUG is false, exec_script is _strip_comments(b_data)
    kwargs = {"wrapper": True, "powershell": True}
    actor.scan_module(b_data, **kwargs)


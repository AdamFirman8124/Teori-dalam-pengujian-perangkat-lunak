

# Generated at 2022-06-12 21:41:23.813599
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import sys
    # If pylint was run with python2, we need to mock module_utils to scan the C# helper scripts
    if sys.version_info[0] < 3:
        import mock
        sys.modules['module_utils'] = mock.Mock()
        sys.modules['module_utils.basic'] = mock.Mock()

    module_finder = PSModuleDepFinder()
    module_finder.scan_exec_script("basic")

    assert len(module_finder.ps_modules) > 0
    assert "Ansible.Common.DictionaryExtensions" in module_finder.ps_modules
    assert "Ansible.Common.HashtableExtensions" in module_finder.ps_modules


# Generated at 2022-06-12 21:41:26.672210
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    f = PSModuleDepFinder()
    f.scan_exec_script('sample.ps1')



# Generated at 2022-06-12 21:41:38.750396
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mdf = PSModuleDepFinder()


# Generated at 2022-06-12 21:41:39.722568
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    assert True is True


# Generated at 2022-06-12 21:41:46.985045
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import tempfile
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils import basic

    # write a test psm1 module which includes a C# util and a PS util
    fd, path = tempfile.mkstemp(suffix=".psm1")
    os.close(fd)
    with open(path, "wb") as f:
        f.write(to_bytes('''\
#Requires -Module Ansible.ModuleUtils.ExampleUtil
#AnsibleRequires -CSharpUtil Ansible.ExampleUtil
'''))

    fd, cs_path = tempfile.mkstemp(suffix=".cs")
    os.close(fd)

# Generated at 2022-06-12 21:41:48.582234
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    obj = PSModuleDepFinder()
    obj.scan_exec_script('boilerplate.ps1')

# Generated at 2022-06-12 21:41:58.519856
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()

    module_util_str = \
'''#Requires -Module Ansible.ModuleUtils.Common
#AnsibleRequires -PowerShell Ansible.ModuleUtils.Common
#AnsibleRequires -PowerShell ..module_utils.powershell_common
#AnsibleRequires -PowerShell -Optional ansible_collections.organization.collection.plugins.module_utils.powershell_core
'''
    finder.scan_module(module_util_str)
    assert finder.ps_modules['Ansible.ModuleUtils.Common']
    assert finder.ps_modules['..module_utils.powershell_common']
    assert finder.ps_modules['ansible_collections.organization.collection.plugins.module_utils.powershell_core']

# Generated at 2022-06-12 21:42:05.133529
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible_collections.ansible.posix.tests.unit.plugins.modules.test_compile_wrapper import TestCompileWrapper
    from ansible_collections.ansible.posix.tests.unit.plugins.modules.test_exec_wrapper import TestExecWrapper

    # Scan the ps module first, it references the provided cs module util
    finder = PSModuleDepFinder()
    finder.scan_module(TestExecWrapper.test_data, fqn="Test.FQN")

    # Scan the cs module using the same finder, it should contain the ps
    # module_util reference
    finder.scan_module(TestCompileWrapper.test_data, wrapper=True)

    assert len(finder.ps_modules) == 1
    assert len(finder.cs_utils_wrapper) == 1


# Generated at 2022-06-12 21:42:10.790306
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmd = PSModuleDepFinder()
    psmd.scan_exec_script(b'exec_env')

# Generated at 2022-06-12 21:42:12.997316
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Check scan_exec_script without commenting out any lines
    pmdf = PSModuleDepFinder()
    pmdf.scan_exec_script("ps_wrapper")
    assert pmdf.exec_scripts == dict()
    assert pmdf.ps_modules == dict()


# Generated at 2022-06-12 21:42:42.104829
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:42:44.900252
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mu = PSModuleDepFinder()
    assert len(mu.exec_scripts) == 0
    mu.scan_exec_script("wrapper")
    assert len(mu.exec_scripts) == 1
    assert b'modulename' in mu.exec_scripts["wrapper"]


# Generated at 2022-06-12 21:42:47.311240
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dc = PSModuleDepFinder()
    dc.scan_exec_script(name="Basic")
    assert 'Basic' in dc.exec_scripts
    assert 'ansible_collections.ansible.builtin.plugins.module_utils.basic' in dc.ps_modules


# Generated at 2022-06-12 21:42:48.817948
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test function scan_exec_script
    return True



# Generated at 2022-06-12 21:43:01.595174
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    dep_finder = PSModuleDepFinder()
    data = b'#Requires -Module Ansible.ModuleUtils.Powershell\n' \
           b'#AnsibleRequires -CSharpUtil Ansible.ModuleUtils.Legacy\n' \
           b'#AnsibleRequires -CSharpUtil ansible_collections.ns.coll.plugins.module_utils.name\n' \
           b'#Requires -Version 5.1\n' \
           b'#AnsibleRequires -OSVersion 10.0\n' \
           b'#AnsibleRequires -Become\n' \
           b'#AnsibleRequires -Wrapper something.ps1\n'
    dep_finder.scan_module(data)

# Generated at 2022-06-12 21:43:06.875350
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    inst = PSModuleDepFinder()
    data = '# Requires -Module Ansible.ModuleUtils.CommonUtils'
    inst.scan_exec_script(data)
    assert inst.exec_scripts[data] == ""
    assert inst.ps_modules[data].keys() == {'data', 'path'}
# test _slurp

# Generated at 2022-06-12 21:43:13.337588
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    #
    # Create an instance of class PSModuleDepFinder
    #
    finder = PSModuleDepFinder()

    #
    # Execute the tested code
    #
    finder.scan_exec_script("script_without_dependencies")

    #
    # Now we need to verify that the tested code has been
    # executed correctly
    #
    assert finder.exec_scripts["script_without_dependencies"] == 'function script_without_dependencies() {Write-Host -NoNewline "This is the script without dependencies!"}\r\n'


# Generated at 2022-06-12 21:43:13.993178
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False, "No test"

# Generated at 2022-06-12 21:43:18.868214
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    """
    Returns:
    - ``True`` if test passes
    """

    fake_data = b'#Requires -Module Ansible.ModuleUtils.FakeModuleUtil\n'

    # expected wrapper name
    fake_name = "FakeModuleUtil"

    dep = PSModuleDepFinder()
    dep.scan_exec_script(fake_name)

    # we want to test that the data is being added to the exec_scripts dict
    assert to_text(dep.exec_scripts[fake_name]) == to_text(fake_data)
    # we also want to test if it is adding the module_util
    assert dep.ps_modules[fake_name]['data'] == fake_data
    return True


# Generated at 2022-06-12 21:43:29.333499
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.powershell.collections import ansible_collections_test

    # ******** Case 1 ********
    # Case 1.1: Testing for PS module that do not have a Requires statement
    ps_module_name = "TestPSModule"
    ps_module_data = pkgutil.get_data("ansible_collections.ansible.test.plugins.modules", to_native(ps_module_name + ".psm1"))
    assert ps_module_data is not None

    ps_module_deps = {
        'data': ps_module_data,
        'path': to_native("/path/to/TestPSModule.psm1"),
    }

    ps_module_utils = dict()
    cs_utils = dict()
    exec_scripts = dict()

    ps_module_dep

# Generated at 2022-06-12 21:43:52.502796
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('windows_common.ps1')



# Generated at 2022-06-12 21:43:57.201294
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("executor")
    assert dep_finder.exec_scripts == {
                                            "executor": to_bytes(pkgutil.get_data("ansible.executor.powershell", "executor.ps1")),
                                         }
    assert dep_finder.ps_version is None
    assert dep_finder.os_version is None
    assert dep_finder.become == False


# Generated at 2022-06-12 21:44:08.458306
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from io import StringIO

    # Setup test data
    module_name_0 = 'test_module_name_0'
    class_name_0 = 'PSModuleDepFinder'

# Generated at 2022-06-12 21:44:09.472118
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    PSModuleDepFinder()



# Generated at 2022-06-12 21:44:17.683263
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """Test :class:`ansible_collections.nleiva.tetration.plugins.module_utils.PSModuleDepFinder.scan_exec_script` method of
    :class:`ansible_collections.nleiva.tetration.plugins.module_utils.PSModuleDepFinder` on a valid input"""
    name = "Test_PSModuleDepFinder"
    obj = PSModuleDepFinder()
    obj.scan_exec_script(name)

# Generated at 2022-06-12 21:44:23.974981
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script('wrapper')
    psmdf.scan_exec_script('pswrap')  # missing script
    psmdf.scan_exec_script('powershell')
    assert(len(psmdf.ps_modules) == 2)
    assert(len(psmdf.exec_scripts) == 2)


# Generated at 2022-06-12 21:44:29.914902
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # set up
    obj = PSModuleDepFinder()
    name = "exec_wrapper"
    # tests
    with pytest.raises(AnsibleError) as exec_info:
        obj.scan_exec_script(name)
    # assert
    assert "Could not find executor powershell script" in str(exec_info.value)



# Generated at 2022-06-12 21:44:42.844531
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:44:47.645237
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
  # First unit test, this will only test that the code runs and doesn't throw an exception
  ps_module_obj = PSModuleDepFinder()
  ps_module_obj.scan_exec_script(b"Test_Module")


# Generated at 2022-06-12 21:44:53.150456
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from .test_data.powershell_util_data import read_psm1_data, read_cs_data

    # by defining an explicit dict of cs utils and where they are used, we
    # can potentially save time by not adding the type multiple times if it
    # isn't needed
    cs_util = {}
    ps_module = {}

    ps_version = None
    os_version = None
    become = False

    finder = PSModuleDepFinder()
    finder.cs_utils_wrapper = cs_util
    finder.ps_modules = ps_module

    finder.ps_version = ps_version
    finder.os_version = os_version
    finder.become = become

    # Read the contents of the powershell util we want to test
    wrapper_data = read_psm1_data

# Generated at 2022-06-12 21:45:08.690959
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    scanner = PSModuleDepFinder()
    scanner.scan_exec_script("script_name")


# Generated at 2022-06-12 21:45:09.906623
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Just testing the first call to scan_module for finding the dependencies
    PSModuleDepFinder().scan_exec_script("win_ping")



# Generated at 2022-06-12 21:45:18.124571
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    sample_module_data = b"""
        #Requires -Module Ansible.ModuleUtils.MyUtil
        #Requires -Module Ansi#ble.ModuleUtils.AnotherUtil
    """
    # Make a csharp util in collection available
    import pkgutil
    import ansible_collections.ansible.windows.plugins.module_utils.module_util_data as module_util_data
    pkgutil.get_data = lambda pkg, name: pkgutil.get_data(module_util_data.__name__, name)

    #
    # Test calling scan_exec_script with a name that doesn't exist, this should raise an error
    #
    ps_module_dep_finder = PSModuleDepFinder()


# Generated at 2022-06-12 21:45:21.397481
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script('powershell_base')
    assert(ps_module_dep_finder.exec_scripts['powershell_base'])
    assert(ps_module_dep_finder.ps_modules)
    assert(ps_module_dep_finder.cs_utils_module)


# Generated at 2022-06-12 21:45:32.640528
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.plugins.loader import ps_module_utils_loader
    from ansible.module_utils.ps_module_utils.powershell import Base
    from ansible.module_utils.powershell_executor_script import PowerShellExecutorScript
    from ansible_test_data import PS_MODULE_UTILS_DATA_SRC_PATH
    import sys
    import traceback
    
    # read the required data
    test_data = {}

# Generated at 2022-06-12 21:45:41.941209
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('exec_wrapper_template')
    finder.scan_exec_script('exec_wrapper_utils')
    finder.scan_exec_script('get_async_task_results')
    finder.scan_exec_script('get_ansible_ps_module_path')
    finder.scan_exec_script('get_ansible_bin_path')
    finder.scan_exec_script('load_async_task_result')
    finder.scan_exec_script('ansible_module')
    finder.scan_exec_script('get_custom_facter_facts')
    finder.scan_exec_script('persist_ansible_fact_entry')

# Generated at 2022-06-12 21:45:54.058415
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import re
    import os
    import types
    import sys

    # attempt to load the real one since unittest loads it automatically
    try:
        module = __import__('ansible.module_utils.powershell.PSModuleDepFinder')
    except ImportError:
        pass
    else:
        if isinstance(module, types.ModuleType):
            module = None
            sys.modules.pop('ansible.module_utils.powershell.PSModuleDepFinder', None)

    from ansible.module_utils.powershell import PSModuleDepFinder

    # Make sure this is tested with Python 2 & 3
    assert sys.version_info >= (2, 7) and sys.version_info < (3, 0)
    assert os.name == 'nt'

# Generated at 2022-06-12 21:46:04.539712
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:46:08.962459
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.exec_scripts = {'test': 'file'}
    psmdf.scan_exec_script('test')
    psmdf.scan_exec_script('test2')
    assert(psmdf.exec_scripts == {'test': 'file', 'test2': 'file'})



# Generated at 2022-06-12 21:46:12.150682
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # PSModuleDepFinder: Test scan_exec_script()
    # method scan_exec_script of class PSModuleDepFinder doesn't take parameters
    assert True

# Generated at 2022-06-12 21:46:29.072195
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test whether the data can be downloaded and loaded successfully
    depfinder = PSModuleDepFinder()
    path = depfinder.scan_exec_script("ansible_common")
    assert path is None


# Generated at 2022-06-12 21:46:32.562600
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psModuleDepFinder = PSModuleDepFinder()
    psModuleDepFinder.scan_exec_script('posh-wrapper')

    assert 'posh-wrapper' in psModuleDepFinder.exec_scripts



# Generated at 2022-06-12 21:46:35.708197
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script(name='server_info.ps1')
    assert len(psmdf.exec_scripts) == 1


# Generated at 2022-06-12 21:46:38.994551
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Setup
    ps_module_finder = PSModuleDepFinder()
    
    # Testing
    ps_module_finder.scan_exec_script("common")
    
    # Teardown



# Generated at 2022-06-12 21:46:48.190288
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    file_name = "testfile"
    tests = [
        # Test invalid powershell script 
        (b"blah", AnsibleError),
        # Test for an empty powershell script
        (b"", None),
        # Test for a valid powershell script with no dependencies
        (b"Write-Host Test", None),
        # Test for a valid powershell script with dependencies
        (b"#Requires -Module Ansible.ModuleUtils.RemoteManagement\n \nWrite-Host Test", None),
    ]
    for test_data, expected_error in tests:
        obj = PSModuleDepFinder()
        if expected_error:
            with pytest.raises(expected_error):
                obj.scan_exec_script(file_name)
        else:
            obj.scan_exec_script(file_name)
           

# Generated at 2022-06-12 21:46:50.283223
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # TODO: Test the method scan_exec_script of class PSModuleDepFinder
    pass

# Generated at 2022-06-12 21:47:02.407744
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psutil_dep = PSModuleDepFinder()

    # test with empty name
    exception_msg = 'Could not find executor powershell script for \'\''
    exception_msg = to_bytes(exception_msg)
    with pytest.raises(AnsibleError) as excinfo:
        psutil_dep.scan_exec_script(name='')
    assert excinfo.match(exception_msg)
    psutil_dep = PSModuleDepFinder()

    # test with name
    name = 'module_exec'
    exception_msg = 'Could not find executor powershell script for \'%s\'' % name
    exception_msg = to_bytes(exception_msg)

# Generated at 2022-06-12 21:47:06.228458
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("powershell_module")
    assert dep_finder.exec_scripts["powershell_module"] == pkgutil.get_data("ansible.executor.powershell", "powershell_module.ps1")

# Generated at 2022-06-12 21:47:07.450797
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # TODO: write unit test for this method
    pass


# Generated at 2022-06-12 21:47:13.991186
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.powershell import PSModuleDepFinder

    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("ps_json")
    assert dep_finder.exec_scripts["ps_json"]
    assert dep_finder.cs_utils_wrapper["ps_json"]["data"].strip().startswith(b"# PowerShell script")
    assert os.path.basename(to_native(dep_finder.cs_utils_wrapper["ps_json"]["path"])) == "ps_json.ps1"
    assert dep_finder.cs_utils_wrapper["ps_json"]["data"].strip().endswith(b"# End PowerShell script")


# Generated at 2022-06-12 21:47:27.833995
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('get_powershell_command')
    assert len(finder.exec_scripts.keys()) > 0


# Generated at 2022-06-12 21:47:28.736065
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False, "Test not implemented"


# Generated at 2022-06-12 21:47:35.456617
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils._text import to_bytes
    from ansible.executor.powershell import module_scripts, powershell_version

    # Make sure module scripts are loaded
    module_scripts()

    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("basic")
    assert dep_finder.exec_scripts["basic"]
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("win_package")
    assert dep_finder.exec_scripts["win_package"]

    from ansible.executor.powershell.module_utils.pwsh_common import PwshCommon

    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("win_package")
    win_package_data = dep_finder.exec_

# Generated at 2022-06-12 21:47:38.303134
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    f = PSModuleDepFinder()
    f.scan_exec_script('powershellscript')
    assert f.exec_scripts['powershellscript'] is not None


# Generated at 2022-06-12 21:47:40.804823
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    provider = PSModuleDepFinder()
    provider.scan_exec_script("_powershell_common")

# Generated at 2022-06-12 21:47:43.474790
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_dep_finder = PSModuleDepFinder()
    ps_dep_finder.scan_exec_script('library_utils')


# Generated at 2022-06-12 21:47:51.376314
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class AnsibleModule:
        def run_command(self, command):
            command_result = dict(rc=0, stdout='')

            return command_result

    class Executor:
        @staticmethod
        def add_module_args(module_args, task_vars):
            pass

    class PSRunner:
        @staticmethod
        def run(cmd, task_vars, module_compression='ZLIB'):
            pass

    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.block import Block

    def RunPlayBook(**kwargs):
        ansible_module = AnsibleModule()
        executor = Executor()
        ps_runner = PSRunner()

        task_executor = TaskExec

# Generated at 2022-06-12 21:47:53.906298
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mdf = PSModuleDepFinder()
    mdf.scan_exec_script(b"Common")
    assert mdf.exec_scripts.get(b"Common", False)


# Generated at 2022-06-12 21:48:01.831312
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """Test scan_exec_script"""
    module_util = PSModuleDepFinder()
    assert(module_util != None)
    module_util.cs_utils_wrapper = {}
    module_util.ps_version = ""
    module_util.os_version = ""
    module_util.become = False
    module_util.ps_modules = {}
    module_util.exec_scripts = {}
    module_util.cs_utils_module = {}
    name = "powershell_module_utils"
    assert (module_util.exec_scripts.get(name) == None )
    module_util.scan_exec_script(name)
    assert (module_util.exec_scripts.get(name) != None )


# Generated at 2022-06-12 21:48:02.802907
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True

# Generated at 2022-06-12 21:48:17.753744
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()

    dep_finder.scan_exec_script('test_data/test_depfinder/exec_wrapper_1.ps1')

# Generated at 2022-06-12 21:48:21.562267
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psdf = PSModuleDepFinder()
    psdf.scan_exec_script("test_exec_script")
    with pytest.raises(AnsibleError):
        psdf.scan_exec_script("does_not_exist")


# Generated at 2022-06-12 21:48:24.787050
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # This is a doc test
    dep_finder = PSModuleDepFinder()
    # Ansible.AnsibleModule contains #requires -module Ansible.ModuleUtils.PowerShell.Strings, Ansible.ModuleUtils.PowerShell
    dep_finder.scan_exec_script("Ansible.AnsibleModule")


# Generated at 2022-06-12 21:48:28.199413
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test that the script discovery code works
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script("basic")
    assert to_text("Get-UnicodeData", errors='surrogate_or_strict') in psmdf.exec_scripts["basic"]



# Generated at 2022-06-12 21:48:39.826531
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
  # Create two test modules
  test_module = """
  #AnsibleRequires -PowerShell Ansible.ModuleUtils.Testing
  #Requires -Module Pester
  #Requires -Module xWebAdministration

  #AnsibleRequires -Wrapper PowerShell
  #Requires -Module Test
  #Requires -Module Test2
  """

  test_module2 = """
  #AnsibleRequires -PowerShell Test3
  #AnsibleRequires -PowerShell 1.2.3.4-PreRelease
  #AnsibleRequires -PowerShell 4.0
  #AnsibleRequires -PowerShell Test4 -Optional
  #AnsibleRequires -PowerShell Test5 -Optional
  #AnsibleRequires -PowerShell Test
  """


# Generated at 2022-06-12 21:48:40.331126
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:48:47.868923
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    expected = dict()

    # noinspection PyTypeChecker
    dut = PSModuleDepFinder()

    dut.scan_exec_script('ansible_default_dict_script')
    expected['ansible_default_dict_script'] = to_bytes('function ansible_default_dict($dict) {\n'
                                                       '    if ($dict -is [System.Collections.ArrayList]) {\n'
                                                       '        $dict = $dict.ToArray()\n'
                                                       '    }\n'
                                                       '    return $dict\n'
                                                       '}')
    assert dut.exec_scripts == expected
    assert dut.cs_utils_wrapper == dict()


# Generated at 2022-06-12 21:48:52.789825
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """
    This is a unit test method.
    """
    def _slurp_mock(mu_path):
        """
        Mock slurp function.
        """
        return to_bytes(
            "##\n"
            "#Requires -Module Ansible.ModuleUtils.Powershell.Utils\n"
            "##\n"
            "b64_data=$([Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes('UTF-8 powershell script data')))\n")

    # Only tests the input module_data to see if the required module was found.
    def _add_module_mock(name, ext, fqn, optional, wrapper=False):
        """
        Mock add_module function.
        """

# Generated at 2022-06-12 21:49:03.256713
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    def do_test(name,
                expected_result,
                expected_exec_scripts,
                expected_ps_modules,
                expected_cs_utils_wrapper):
        finder = PSModuleDepFinder()
        finder.exec_scripts = dict()
        finder.ps_modules = dict()
        finder.cs_utils_wrapper = dict()
        finder.scan_exec_script(name)
        assert finder.exec_scripts == expected_exec_scripts
        assert finder.ps_modules == expected_ps_modules
        assert finder.cs_utils_wrapper == expected_cs_utils_wrapper

# Generated at 2022-06-12 21:49:08.746566
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import tempfile
    import shutil
    import os
    import sys
    test_dir = tempfile.mkdtemp()
    os.chdir(test_dir)
    shutil.rmtree(test_dir)
    try:
        returnValue = PSModuleDepFinder.scan_exec_script(PSModuleDepFinder(), None)
        assert returnValue is None

    finally:
        os.chdir(sys.path[0])
        sys.path.pop(0)

# Generated at 2022-06-12 21:49:28.080510
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Verify expected string is added to the end of a list.
    test_dep_finder = PSModuleDepFinder()

    # verify error when script doesn't exist in executor/powershell
    try:
        test_dep_finder.scan_exec_script("does_not_exist")
        assert False

    except AnsibleError:
        assert True

    # verify that the script is added correctly
    test_dep_finder.scan_exec_script("test")
    assert to_text("test") in test_dep_finder.exec_scripts.keys()

    # verify that an existing script is not added
    test_dep_finder.scan_exec_script("test")
    assert len(test_dep_finder.exec_scripts.keys()) == 1

    # verify that a second script is added
    test_dep_finder.scan_exec_

# Generated at 2022-06-12 21:49:39.592212
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class TestModule(object):
        def __init__(self, module_data=''):
            self.module_data = module_data
            self.dep_finder = PSModuleDepFinder()
            self.dep_finder.ps_modules = {}
            self.dep_finder.exec_scripts = {}
            self.dep_finder.scan_module(module_data)

    # test base64 encoded ps1 script
    with open('test/units/module_utils/test_module_utils.ps1', 'r') as f:
        encoded_data = base64.b64encode(f.read())

    module_data = '#ansiblerequires -wrapper test_module_utils\n'
    test_module = TestModule(module_data)

# Generated at 2022-06-12 21:49:47.717698
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    name = 'ansible_powershell_defaults'
    ps_depfinder = PSModuleDepFinder()
    ps_depfinder.scan_exec_script(name)
    assert len(ps_depfinder.exec_scripts) == 1
    assert len(ps_depfinder.ps_modules) == 0
    assert len(ps_depfinder.cs_utils_module) == 0
    assert len(ps_depfinder.cs_utils_wrapper) == 0
    assert name in ps_depfinder.exec_scripts
    assert ps_depfinder.ps_version is None
    assert ps_depfinder.os_version is None
    assert ps_depfinder.become is False


# Generated at 2022-06-12 21:49:55.093251
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible import context
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.text.converters import to_bytes, to_text
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.loader import fragment_loader


# Generated at 2022-06-12 21:49:56.413008
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass # needs implementation

# Generated at 2022-06-12 21:50:02.706475
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.powershell import PSModuleDepFinder
    import os

    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script('Execution')
    assert ps_module_dep_finder.exec_scripts['Execution']
    assert '# ANSIBLE_METADATA' in ps_module_dep_finder.exec_scripts['Execution'].decode('utf-8')


# Strip out comments from a script before sending it to the exec wrapper

# Generated at 2022-06-12 21:50:08.569459
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    with open('/home/mileszhou/work/testPSModuleDepFinder/ansible_test_module.psm1','rb') as f:
        data_1 = f.read()
 
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_module(data_1)
    print(dep_finder.ps_modules)
    print("hello")


# Generated at 2022-06-12 21:50:09.263357
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:50:15.325663
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Setup
    ps_module_dep_finder = PSModuleDepFinder()

    name = "Wrapper"
    pkgdata = b'#requires -version 2.0\n'

    ps_module_dep_finder.scan_exec_script(name)
    assert ps_module_dep_finder.exec_scripts.get('Wrapper') == pkgdata


# Generated at 2022-06-12 21:50:21.207269
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """
    Test scan_exec_script of PSModuleDepFinder
    """

    finder = PSModuleDepFinder()
    finder.scan_exec_script("script1")
    finder.scan_exec_script("script2")
    assert finder.exec_scripts == {"script1": b"#!/usr/bin/env python\nscript1\n",
                                   "script2": b"#!/usr/bin/env python\nscript2\n"}

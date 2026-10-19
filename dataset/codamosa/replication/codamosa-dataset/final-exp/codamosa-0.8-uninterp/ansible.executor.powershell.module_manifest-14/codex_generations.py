

# Generated at 2022-06-12 21:41:02.641433
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    PSModuleDepFinder1 = PSModuleDepFinder()
    PSModuleDepFinder1.random = random.random
    PSModuleDepFinder1.scan_exec_script("some name")

# Generated at 2022-06-12 21:41:09.696906
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    o = PSModuleDepFinder()
    with open("./ansible_module_internal.psm1", 'rb') as f:
        o.scan_module(f.read())
    with open("./ansible_module_powershell.psm1", 'rb') as f:
        o.scan_module(f.read())
    print(o.ps_modules['Ansible.ModuleUtils.Powershell.Windows.Raw'])


# Helper for PSModuleDepFinder

# Generated at 2022-06-12 21:41:10.636658
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    # TODO
    assert True


# Generated at 2022-06-12 21:41:13.967524
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_obj = PSModuleDepFinder()

    args = {
        'name': 'pwsh_wrapper',
    }
    test_obj.scan_exec_script(**args)

    return True

# Generated at 2022-06-12 21:41:27.163079
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:41:39.158284
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    def _slurp_mock(module_file):
        return module_file
    def _find_plugin_mock(module_name, ext):
        return "mock_find_plugin_path"

    finder = PSModuleDepFinder()
    finder.scan_exec_script = _scan_exec_script_mock
    finder.scan_module = _scan_module_mock
    finder.exec_scripts = dict()
    finder.ps_modules = dict()
    finder.cs_utils_wrapper = dict()
    finder.cs_utils_module = dict()

    ps_module_utils_loader.find_plugin = _find_plugin_mock
    test_data = to_bytes(pkgutil.get_data("ansible.module_utils.basic", "basic.ps1"))


# Generated at 2022-06-12 21:41:47.908646
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    ps_dep_finder = PSModuleDepFinder()
    module_data = to_bytes('''
param(
[String]$Key,
[String]$Value
)

#Requires -Module Ansible.ModuleUtils.MyPSModuleUtil
#Requires -Module Ansible.ModuleUtils.MyPSModuleUtil2
#AnsibleRequires -Powershell Ansible.ModuleUtils.MyPSModuleUtil3
#AnsibleRequires -Powershell ..module_utils.MyPSModuleUtil4
#AnsibleRequires -CSharpUtil Ansible.MyCSModuleUtil
#AnsibleRequires -CSharpUtil ansible_collections.foo.collection.plugins.module_utils.MyCSModuleUtil2
''')
    ps_dep_finder.scan_module(module_data)
    assert ps_

# Generated at 2022-06-12 21:41:57.564932
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    content = """
    #Requires -Module Ansible.ModuleUtils.some_module
    #Requires -Version 3
    #AnsibleRequires -PowerShell some_module
    #AnsibleRequires -Wrapper some.ps1
    #AnsibleRequires -CSharpUtil some_cs_module
    #AnsibleRequires -OSVersion 6.1
    #AnsibleRequires -Become

"""
    content = to_bytes(content)

    ps = PSModuleDepFinder()
    ps.scan_module(content, fqn="fake_fqn", powershell=True)

    assert ps.ps_version == "3"
    assert ps.os_version == "6.1"
    assert ps.become

    assert "Ansible.ModuleUtils.some_module" in ps.ps_modules
   

# Generated at 2022-06-12 21:42:02.735921
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    my_PSModuleDepFinder_scan_exec_script = PSModuleDepFinder()

    my_PSModuleDepFinder_scan_exec_script.scan_exec_script("Select-Object")
    assert my_PSModuleDepFinder_scan_exec_script.exec_scripts["Select-Object"]

    my_PSModuleDepFinder_scan_exec_script.scan_exec_script("Select-Object")
    assert my_PSModuleDepFinder_scan_exec_script.exec_scripts["Select-Object"]



# Generated at 2022-06-12 21:42:08.228486
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # This method is used to test methods which are in this file and cannot be
    # tested in module_utils/powershell/__init__.py

    class MockModule(object):
        # this class is used by the scan_exec_script method to satisfy the
        # scanning of itself, which is normally done by self.scan_module but
        # since it is recursive a loop is started.
        def __init__(self, name, data):
            self.name = name
            self.data = data

    def _g(n):
        return to_bytes(n)

    depfinder = PSModuleDepFinder()
    depfinder.scan_exec_script('Example1')
    assert len(depfinder.exec_scripts.keys()) == 1
    assert depfinder.exec_scripts['Example1'] == _g("Example1 script")

    dep

# Generated at 2022-06-12 21:42:22.107056
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:42:31.604313
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()

# Generated at 2022-06-12 21:42:38.913353
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    fixture_file = ansible_fixtures + "/scan_exec_script.py"
    test_data = open(fixture_file, encoding="utf-8").read()
    globals().update(json.loads(test_data))

    finder = PSModuleDepFinder()
    results = finder.scan_exec_script("test_name")

    assert results == expected_results

# Generated at 2022-06-12 21:42:42.103999
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Arrange
    test_scan_exec_script = []
    obj = PSModuleDepFinder()

    # Act
    obj.scan_exec_script(test_scan_exec_script[0])

    # Assert


# Generated at 2022-06-12 21:42:45.215804
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dependency_finder = PSModuleDepFinder()
    dependency_finder.scan_exec_script('base')

    assert b"using" in dependency_finder.cs_utils_wrapper['ansible_collections.not_a_real_collection.fake.plugins.module_utils.basic']


# Generated at 2022-06-12 21:42:57.360551
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    def _test(str_to_test, expected_length=None, result=None):
        result = {} if result is None else result
        dep_finder = PSModuleDepFinder()
        dep_finder.scan_module(str_to_test.encode('utf-8'))
        assert len(dep_finder.ps_modules) == expected_length
        for k in list(result.keys()):
            assert dep_finder.ps_modules[k]["data"].decode('utf-8') == result[k]
            
    _test("#Requires -Module Ansible.ModuleUtils.powershell", expected_length=1)
    _test("#AnsibleRequires -PowerShell Ansible.ModuleUtils.powershell", expected_length=1)

# Generated at 2022-06-12 21:43:00.182205
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    depfinder_obj = PSModuleDepFinder()
    depfinder_obj.scan_exec_script("script")


# Generated at 2022-06-12 21:43:10.904512
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # declare a folder containing dummy files
    prefix = "/tmp"
    if not os.path.exists(prefix):
        os.makedirs(prefix)

    def create_dummy_file(prefix, file_name, contents):
        path = os.path.join(prefix, file_name)
        with open(path, 'wb') as fh:
            fh.write(contents)

        return True

    # create a dummy script
    file_name = "dummy.ps1"
    contents = "#ansiblerequires -wrapper dummy"
    create_dummy_file(prefix, file_name, contents)

    # create class
    module_util = PSModuleDepFinder()
    # scan script
    module_util.scan_exec_script(file_name.split(u".")[0])
    # assert

# Generated at 2022-06-12 21:43:15.989937
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    fixture_file = os.path.join(os.path.dirname(__file__), "test_module_utils_powershell.psm1")
    data = _slurp(fixture_file)
    finder = PSModuleDepFinder()
    finder.scan_exec_script(to_native(data))
    assert finder.exec_scripts.get('common').decode().startswith('###')
    assert len(finder.cs_utils_wrapper) == 1
    assert finder.cs_utils_wrapper.get('ansible_collections.ansible.builtin.plugins.module_utils.common').get('path').endswith('Ansible.ModuleUtils.Common.Common.cs')

# Generated at 2022-06-12 21:43:16.463488
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:43:39.335514
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.cloudengine.ce import ce_base

    def _write_file(path, content):
        p = open(path, "ab")
        p.write(content)
        p.close()

    # this test breaks if you are on a zippy internet connection
    test_dir = os.path.dirname(os.path.dirname(ce_base.__file__))
    orig_dir = os.path.join(test_dir, "plugins/modules/ce_asn_pool")
    wrap_dir = os.path.join(test_dir, "plugins/module_utils/powershell/ce_asn_pool")

# Generated at 2022-06-12 21:43:43.701078
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()
    module_data = b'#AnsibleRequires -PowerShell Ansible.ModuleUtils.Util1'
    # finder.scan_module(module_data)
    # assert 0, "check the out put of scan_module"


# Generated at 2022-06-12 21:43:51.972915
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    scan_exec_script = PSModuleDepFinder().scan_exec_script

    with pytest.raises(Exception) as e:
        scan_exec_script("bad_script")

    assert_error_msg("Could not find executor powershell script for 'bad_script'", e)

    with pytest.raises(Exception) as e:
        scan_exec_script("/etc/passwd")

    assert_error_msg("Could not find executor powershell script for '/etc/passwd'", e)

    # Valid script
    scan_exec_script("test_script")


# Generated at 2022-06-12 21:43:57.110504
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    md = PSModuleDepFinder()

    md.scan_exec_script('powershell_common')
    assert any(x.startswith('Ansible.ModuleUtils.Powershell.Compression') for x in md.ps_modules.keys())
    assert md.exec_scripts.get('powershell_common', None)

    try:
        md.scan_exec_script('not_a_valid_powershell_script')
        assert False
    except:
        assert True


# Generated at 2022-06-12 21:43:59.054617
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    #Unit test for method scan_module of class PSModuleDepFinder in plugin.ps_loader.py
    pass


# Generated at 2022-06-12 21:44:10.565864
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:44:11.130950
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
            pass

# Generated at 2022-06-12 21:44:23.979194
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """
    Method scan_exec_script() scans scripts and search for dependencies
    """
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script(name=b"WorkflowCmdlet")


# Generated at 2022-06-12 21:44:28.403090
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    def _slurp(filename):
        with open(filename, 'rb') as f:
            output = f.read()
            return output

    tests = {
        "test_no_dependencies":
            """
            function foo({param_a}, {param_b}) {{ 
            }}
            """,
        "test_one_dependency":
            """
            #Requires -Module Ansible.ModuleUtils.ArgumentSpec
            function foo({param_a}, {param_b}) {{ 
            }}
            """,
        "test_two_dependencies":
            """
            #Requires -Module Ansible.ModuleUtils.ArgumentSpec
            #Requires -Module Ansible.ModuleUtils.CommonSpec
            function foo({param_a}, {param_b}) {{ 
            }}
            """,
    }

   

# Generated at 2022-06-12 21:44:39.648949
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class PSModuleDepFinder_test(PSModuleDepFinder):
        pass
    try:
        name = "test"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data", "powershell_modules", name + ".ps1")
        with open(file_path) as f:
            contents = f.read()
        psmdf = PSModuleDepFinder_test()
        psmdf.scan_exec_script(name)
        assert psmdf.exec_scripts[name] == contents
    except Exception as e:
        print(e)
        assert False


# Generated at 2022-06-12 21:45:20.296446
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script(to_bytes('powershellGetModuleVersion'))
    assert dep_finder.exec_scripts.get('powershellGetModuleVersion', to_bytes('')) != to_bytes('')

# Generated at 2022-06-12 21:45:23.731003
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test that pkgutil.get_data is called with the expected values
    # Check that scan_module is called with the expected values
    # Check that the module data is added to self.exec_scripts
    # Check that exec_scripts is a dictionary
    # Check that the length of exec_scripts is as expected
    # Check that the returned dictionary contains the expected values
    m_dep_finder = PSModuleDepFinder()
    m_dep_finder.scan_exec_script('file')

# Generated at 2022-06-12 21:45:27.857251
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_instance = PSModuleDepFinder()
    # note: the return value of this method doesn't really matter.
    # It's the side effects that we're testing.
    actual_result = test_instance.scan_exec_script('win_ping')



# Generated at 2022-06-12 21:45:32.346835
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Unit test for scan_exec_script
    #
    #  The test reads data from .\lib\ansible\executor\powershell\runspace.ps1 file
    #
    from ansible.module_utils.powershell import runspace

    CONST_PS1_WRAPPER_FILE_PATH = "{ps_path}\runspace.ps1"

    # set up needed vars
    test_ps1_wrapper_file_path = CONST_PS1_WRAPPER_FILE_PATH.format(ps_path=os.path.dirname(runspace.__file__))
    assert os.path.exists(test_ps1_wrapper_file_path)

    # set up the object
    test_ps_dep_finder = PSModuleDepFinder()

    # run the code
    test_ps_dep_

# Generated at 2022-06-12 21:45:41.737391
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import tempfile
    from pathlib import Path

    """
    This is a data-driven test for the scan_exec_script method. It
    executes the scan_exec_script method for several different data sets.
    The data set is defined as a dictionary. The format of the dictionary is
    below:
    {
        "description": 'description of the data set',
        "data": <data for the PowerShell script to be analyzed>,
        "dep_data": <data for the module_util that will be read by the
                    PowerShell script>,
        "expected": <the expected results>,
    }
    """

    # The data set "no_deps" will result in no module dependencies found.

# Generated at 2022-06-12 21:45:48.300697
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Setup the class
    ps_module_dep_finder = PSModuleDepFinder()
    # Test method
    random_int = random.randint(0, 9999)
    module_name = "test_" + (str(random_int))
    ps_module_dep_finder.scan_exec_script(module_name)
    ps_module_dep_finder.exec_scripts[module_name]


# Generated at 2022-06-12 21:45:50.867177
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    instance = PSModuleDepFinder()
    assert instance.scan_exec_script("test") == "test"


# Generated at 2022-06-12 21:46:00.884757
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import sys
    import os
    import shutil
    import tempfile
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import ps_module_utils_loader
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    def add_ps_module_utils():
        cwd = os.getcwd()
        tmp_collection_path = tempfile.mkdtemp()
        if not os.path.exists('/dev/shm'):
            sys.path.insert(0, tmp_collection_path)
            os.chdir(tmp_collection_path)
            os.mkdir('ansible_collections')
            os.chdir('ansible_collections')
            os.mkdir('test.test')

# Generated at 2022-06-12 21:46:02.682159
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print("Testing scan_exec_script")
    assert False, "Not implemented"

# Generated at 2022-06-12 21:46:10.505363
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    # read the module under test
    with open(os.path.join(test_dir, '..', '..', '..', 'lib', 'ansible', 'executor', 'powershell', 'ansible_powershell_convert.ps1'), 'rb') as f:
        module_data = f.read()
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('ansible_powershell_convert')
    assert dep_finder.exec_scripts['ansible_powershell_convert'].rstrip() == _strip_comments(module_data)


# Generated at 2022-06-12 21:47:03.381549
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Mock of the module_util module_util_common
    class mock_module_util_common:
        @staticmethod
        def find_powershell_module_utils(module_name):
            module_names = [
                "CommonArgumentCompleter",
                "CommonVars",
                "ConvertTo-Json",
                "PortableFilePath",
                "PSUtils",
                "FileUtils",
                "TextUtils",
                "NetworkUtils",
                "CertificateUtils",
                "Win32RegistryUtils",
                "Executor",
            ]
            if module_name in module_names:
                return "2.2.9.0"
            else:
                return None

    # Mock of the module_util module_util_powershell

# Generated at 2022-06-12 21:47:05.425125
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script("win_command")


# Generated at 2022-06-12 21:47:10.077616
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import ansible.executor.powershell as executor_powershell
    from ansible.module_utils.common.compat import mock

    name = "test_name"

    instance = PSModuleDepFinder()
    instance.scan_exec_script(name)
    assert len(instance.exec_scripts) == 1
    assert name in instance.exec_scripts.keys()
    assert instance.exec_scripts[name] is not None


# Generated at 2022-06-12 21:47:13.092044
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_module_finder = PSModuleDepFinder()
    test_module_finder.scan_exec_script("Microsoft.PowerShell.Management")
    assert "Microsoft.PowerShell.Management" in test_module_finder.exec_scripts.keys()
    assert "Microsoft.PowerShell.Utility" in test_module_finder.ps_modules.keys()


# Generated at 2022-06-12 21:47:22.805110
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    test_scan_module(None, 'ansible_collections.plugins.module_utils.network.eos.plugins.modules.eos_banner.psm1')
    test_scan_module(None, 'ansible_collections.ns.coll.plugins.modules.module.psm1')
    test_scan_module('Ansible.ModuleUtils.Common', 'ansible_collections.plugins.modules.module.psm1')
    test_scan_module('Ansible.ModuleUtils.Common', 'ansible_collections.my.coll.plugins.modules.module.psm1')
    test_scan_module('Ansible.ModuleUtils.Common', 'ansible_collections.my.coll.plugins.modules.module.psm1')

# Generated at 2022-06-12 21:47:29.757033
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    # fix for test to pass on windows
    if not os.path.isdir("test/test-data/test_ps_module_finder_test_scan_exec_script"):
        os.makedirs("test/test-data/test_ps_module_finder_test_scan_exec_script")

    # Exec script has no includes
    finder.scan_exec_script("test/test-data/test_ps_module_finder_test_scan_exec_script/no_include")
    assert len(finder.ps_modules) == 0
    assert len(finder.cs_utils_wrapper) == 0

    # Exec script has a powershell include

# Generated at 2022-06-12 21:47:42.892267
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import unittest
    import ansible.executor.powershell
    from ansible.errors import AnsibleError
    from io import BytesIO
    from ansible.executor.powershell import runner
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    class TestModuleDepFinder(unittest.TestCase):

        def test_scan_exec_script(self):
            # Test AnsibleError exception is raised
            pdmf = PSModuleDepFinder()
            self.assertRaises(AnsibleError, pdmf.scan_exec_script, "test")

            # Test successful execution
            pdmf = PSModuleDepFinder()
            pdmf.scan_exec_script("runner")
            self.assertEqual(pdmf.exec_scripts, runner.exec_scripts)

            # Test

# Generated at 2022-06-12 21:47:47.783924
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert _test_PSModuleDepFinder_scan_exec_script("common") == "executors/powershell/common.ps1"
    _test_PSModuleDepFinder_scan_exec_script("raw") == "executors/powershell/raw.ps1"
    _test_PSModuleDepFinder_scan_exec_script("script") == "executors/powershell/script.ps1"


# Generated at 2022-06-12 21:47:51.846355
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # test for method scan_exec_script of class PSModuleDepFinder
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script("powerstate")
    assert  "powerstate" in psmdf.exec_scripts

# Generated at 2022-06-12 21:47:58.481699
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmodule_dep_finder = PSModuleDepFinder()
    psmodule_dep_finder.scan_exec_script("chocolatey_package")
    # see if the ExecConfig object has the correct data
    assert psmodule_dep_finder.exec_scripts["chocolatey_package"].decode("utf-8").startswith("function Test-ChocolateyPackage")
    assert "ansible_collections.ns1.coll1.plugins.module_utils.common.process" in psmodule_dep_finder.ps_modules
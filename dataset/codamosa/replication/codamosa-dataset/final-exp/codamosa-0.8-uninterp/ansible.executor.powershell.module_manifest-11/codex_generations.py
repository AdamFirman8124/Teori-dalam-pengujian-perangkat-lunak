

# Generated at 2022-06-12 21:41:01.470226
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """
    PSModuleDepFinder.scan_exec_script(name)
    :param self:
    :param name:
    :return:
    """
    # mock
    with mock.patch("ansible.module_utils.common.ps_module_dep_finder.PSModuleDepFinder._add_module") as _a:
        with mock.patch("ansible.module_utils.common.ps_module_dep_finder.PSModuleDepFinder.scan_module") as _s:
            with mock.patch("pkgutil.get_data", return_value=b"test_data"):
                # initialize
                p = PSModuleDepFinder()
                # execute
                p.scan_exec_script("test_name")
                # assert
                assert (_a.call_count == 0)

# Generated at 2022-06-12 21:41:03.090401
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    
    con = PSModuleDepFinder()
    con.scan_exec_script("script")

# Generated at 2022-06-12 21:41:13.314044
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    psmdf = PSModuleDepFinder()

    with open(os.path.join(C.DEFAULT_LOCAL_TMP, "windows/powershell/win_domain_membership.psm1"), 'rb') as f:
        psmdf.scan_module(f.read())
    assert(psmdf.become)
    assert(isinstance(psmdf.ps_modules, dict))
    assert(psmdf.ps_modules['Ansible.ModuleUtils.Win_DomainMembership'])
    assert(isinstance(psmdf.cs_utils_wrapper, dict))
    assert(psmdf.cs_utils_wrapper['ansible_collections.ansible.builtin.plugins.module_utils.ansible_module_json'])

# Generated at 2022-06-12 21:41:25.446801
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    # Test with a name that exists in ansible/executor/powershell
    dep_finder.scan_exec_script(name='AnsibleModule')
    assert len(dep_finder.exec_scripts.keys()) == 1
    # Test with a non-existent name, this should raise the appropriate exception
    with pytest.raises(AnsibleError) as excinfo:
        dep_finder.scan_exec_script(name='NonAnsibleModule')
    excinfo.match("Could not find executor powershell script for 'NonAnsibleModule'")
    # Test for an empty name, this should raise the appropriate exception
    with pytest.raises(AnsibleError) as excinfo:
        dep_finder.scan_exec_script(name='')
    excinfo.match

# Generated at 2022-06-12 21:41:29.254668
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    finder = PSModuleDepFinder()
    finder.scan_exec_script('powershell')
    assert len(finder.exec_scripts) > 0



# Generated at 2022-06-12 21:41:34.599192
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    args = {"name": "name"}
    if "name" not in args:  # noqa: F841
        raise
    # Real function body
    args = {"name": "name"}
    if "name" not in args:  # noqa: F841
        raise


# Generated at 2022-06-12 21:41:43.962361
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Constructor test
    finder = PSModuleDepFinder()

    # The test_mod_hierarchy module uses a psutil and should not be found
    # here
    module_data = _read_file("test_modules/test_mod_hierarchy.ps1")
    finder.scan_module(module_data)
    assert finder.ps_version == '2.0'
    assert finder.os_version is None
    assert finder.become is False
    assert len(finder.ps_modules) == 6
    assert len(finder.cs_utils_module) == 2
    assert len(finder.exec_scripts) == 0

# Generated at 2022-06-12 21:41:47.182562
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    depfinder = PSModuleDepFinder()
    depfinder.scan_exec_script("powershell_core")
    assert depfinder.exec_scripts.keys() == ['powershell_core']


# Generated at 2022-06-12 21:41:49.943383
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # File:lib/ansible/executor/powershell/command.ps1
    # Function: wrap_commands_ps1
    # Python code:self.scan_exec_script('command')
    result = dict()
    assert result == 'result'

# Generated at 2022-06-12 21:41:59.919579
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import random,string
    import random,string
    import random,string
    import random,string
    # Assigning function return value to 'random_string3'
    random_string3 = randomword(random.randint(3, 10))
    # Assigning function return value to 'random_string2'
    random_string2 = randomword(random.randint(3, 10))
    input_params = {}
    input_params['name'] = "     " # Name of the script to scan. Should be a .ps1 file in lib/ansible/executor/powershell/<name>.ps1
    input_params['name'] = random_string2 # Name of the script to scan. Should be a .ps1 file in lib/ansible/executor/powershell/<name>.ps1
    input_params['name'] = random_string

# Generated at 2022-06-12 21:42:18.292527
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test correct flow of scan_exec_script
    o=PSModuleDepFinder()
    o.scan_exec_script("RunAsUser")

# Generated at 2022-06-12 21:42:26.383156
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    case = dict()
    case[0] = dict(
        name = "test",
        expected_data = "Data for test.ps1",
        expected_scan_module = dict(wrapper = False, ps = True)
    )
    case[1] = dict(
        name = "Ansible.ModuleUtils.CodeCoverage",
        expected_data = "Data for module_util.psm1",
        expected_scan_module = dict(wrapper = False, ps = True)
    )
    case[2] = dict(
        name = "Ansible.ModuleUtils.Foo.Bar.Util.CodeCoverage",
        expected_data = "Data for util.cs",
        expected_scan_module = dict(wrapper = False, ps = False)
    )

# Generated at 2022-06-12 21:42:38.011105
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    psmd = PSModuleDepFinder()
    psmd._add_module = MagicMock()

    # test a powershell module with a single dependency
    test_path = os.path.join(os.path.dirname(__file__), 'test_data/test_powershell_module_1')
    test_data = _slurp(test_path)

    psmd.scan_module(test_data)

    psmd._add_module.assert_called_once_with(
        'Ansible.ModuleUtils.Test.Utils.TestUtil',
        '.psm1',
        'DemoModule',
        False
    )
    psmd._add_module.reset_mock()

    # test a powershell module with multiple requirements

# Generated at 2022-06-12 21:42:46.325035
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test PSModuleDepFinder._add_module()
    # Initialize a DepFinder object
    depfinder = PSModuleDepFinder()

    psm1_path = resource_from_fqcr('ansible.module_utils.common.process', '.psm1')
    module_data = to_bytes(_slurp(psm1_path))
    depfinder.scan_module(module_data, wrapper=False)
    assert len(depfinder.ps_modules.items()) == 1
    assert len(depfinder.cs_utils_module.items()) == 0
    assert len(depfinder.cs_utils_wrapper.items()) == 0

    cs_path = resource_from_fqcr('ansible.module_utils.azure_rm_common', '.cs')

# Generated at 2022-06-12 21:42:50.223899
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Mock
    ps_module_dep_finder = PSModuleDepFinder()

    # Execution
    result = ps_module_dep_finder.scan_exec_script("TestName")

    # Verification
    assert result is None



# Generated at 2022-06-12 21:42:56.048505
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    mdf = PSModuleDepFinder()
    mdf.scan_module(b"#Requires -Module Ansible.ModuleUtils.Test")
    assert ("Test", ".psm1", None, False) in mdf.ps_modules
    assert mdf.ps_modules["Test"] == "Test.psm1"


# Generated at 2022-06-12 21:43:03.951602
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
        mu_mock = __import__('ansible_collections.test.collection_1.plugins.module_utils.test_CSharp_module',
                             globals(), locals(), [""], 0)

        mu_path = mu_mock.__file__

        p = PSModuleDepFinder()
        data = _slurp(mu_path)
        p.scan_exec_script('TestModule.ps1')
        assert b"myCSharpUtil" in p.cs_utils_wrapper.keys()

# Generated at 2022-06-12 21:43:13.529791
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('Basic')
    assert len(dep_finder.exec_scripts.keys()) == 1
    #assert 'Basic' in dep_finder.exec_scripts.keys()
    assert len(dep_finder.ps_modules.keys()) > 1

    # Test that an exception is thrown for a script that does not exist in executor/powershell
    try:
        dep_finder.scan_exec_script('ScriptDoesNotExist')
    except AnsibleError as e:
        assert to_native(str(e)) == 'Could not find executor powershell script for \'ScriptDoesNotExist\''
    else:
        assert False, "'ScriptDoesNotExist' script does not exist in executor/powershell and an exception should be thrown"


# Generated at 2022-06-12 21:43:17.966112
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    module_data = pkgutil.get_data("ansible.executor.powershell", "executor.ps1")
    finder = PSModuleDepFinder()
    finder.scan_exec_script("executor")
    assert finder.exec_scripts['executor'] == _strip_comments(to_bytes(module_data))
    assert finder.ps_modules['Ansible.ModuleUtils.Legacy']
    assert finder.ps_modules['AnsibleModuleUtilities']
    assert finder.exec_scripts['executor'] == _strip_comments(to_bytes(module_data))


# Generated at 2022-06-12 21:43:28.474538
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Creating an object for class PSModuleDepFinder
    psmdf = PSModuleDepFinder()

    # dict to store the data
    data = dict(
        module_data = r"""#Requires -Module Ansible.ModuleUtils.PSGalleryUtils
using Ansible.ModuleUtils.Common;
using Ansible.ModuleUtils.PowerShellGallery;
using Ansible.ModuleUtils.PSModulePath;
using System;
using System.Management.Automation;
"""
    )

    module_data = data['module_data']

    # calling the scan module method
    psmdf.scan_module(module_data)

    #dict to store the data

# Generated at 2022-06-12 21:43:46.838966
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test the method scan_exec_script of class PSModuleDepFinder
    test_module_dep_finder = PSModuleDepFinder()
    assert test_module_dep_finder.scan_exec_script('Test_Module') is None


# Generated at 2022-06-12 21:43:56.071953
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import os
    import tempfile
    import shutil

    fake_module_data = b'Write-Host "abc123"'
    fake_module_data_with_comments = b'#Write-Host "hello, world"\nWrite-Host "abc123"\n#Write-Host "byebye"'

    # Add a fake module utils folder based on the logic in ps_module_utils_loader
    tempdir = tempfile.mkdtemp()
    os.makedirs(os.path.join(tempdir, 'module_utils'))
    with open(os.path.join(tempdir, 'module_utils', 'fake_module_util.psm1'), 'w') as f:
        f.write("Write-Host 'Hello, world'")

    # Add a fake collection module utils folder
    os.makedirs

# Generated at 2022-06-12 21:44:07.173106
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.facts.utils.win_dsc import PSModuleDepFinder

    def _slurp(path):
        with open(path, 'rb') as f:
            return f.read()

    def _strip_comments(content):
        output = b''
        for line in content.splitlines():
            if line.lstrip().startswith(b'#'):
                continue
            output += line
            output += b'\n'
        return output

    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_module = _scan_module
    ps_module_dep_finder.ps_modules = {'Ansible.ModuleUtils.Powershell.DSC': {'data': 'data', 'path': 'path'}}
    p

# Generated at 2022-06-12 21:44:10.148943
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    obj = PSModuleDepFinder()
    # NOTE: The parameters of this method are dynamically generated to cover all cases.
    obj.scan_exec_script('Unittest-Test')



# Generated at 2022-06-12 21:44:18.223626
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test that each dependent script can be found and loaded
    # plus the recursive search finds the dependencies of them
    # this is only a partial coverage of the scan_exec_script function
    # coverage, but covers the part that matters
    finder = PSModuleDepFinder()
    finder.scan_exec_script('basic')
    assert finder
    assert finder.exec_scripts['basic']
    # The 'basic' script contains 1 dependent script, so
    # the keys length in exec_scripts should be 2
    assert len(finder.exec_scripts) == 2
    assert finder.ps_modules
    # The 'basic' script contains 1 dependent script, which
    # uses two builtin utility scripts, so there should be
    # three util scripts total
    assert len(finder.ps_modules) == 3
    finder.scan_exec_

# Generated at 2022-06-12 21:44:30.083026
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    depfinder = PSModuleDepFinder()
    depfinder.scan_module(b'#Requires -Module Ansible.ModuleUtils.Common')
    assert 'Ansible.ModuleUtils.Common' in depfinder.ps_modules
    depfinder.scan_module(b'\r\n#AnsibleRequires -Powershell Ansible.ModuleUtils.Common\r\n')
    assert 'Ansible.ModuleUtils.Common' in depfinder.ps_modules
    depfinder.scan_module(b'#AnsibleRequires -Powershell ansible_collections.namespace.collection.plugins.module_utils.Common')
    assert 'ansible_collections.namespace.collection.plugins.module_utils.Common' in depfinder.ps_modules

# Generated at 2022-06-12 21:44:31.310267
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass



# Generated at 2022-06-12 21:44:41.192540
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_psmd = PSModuleDepFinder()
    test_psmd.scan_exec_script("windows_env")
    if "windows_env" not in test_psmd.exec_scripts.keys():
        raise AnsibleError("test_PSModuleDepFinder_scan_exec_script failed for scan_exec_script")
    elif "windows_base.psm1" not in test_psmd.ps_modules.keys():
        raise AnsibleError("test_PSModuleDepFinder_scan_exec_script failed for scan_exec_script")


# Generated at 2022-06-12 21:44:48.833747
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    fname = '/Users/louis/Desktop/cisco_aci/ansible-modules-core/lib/ansible/modules/network/aci/aci_aep.py'
    module_data = _slurp(fname)

    assert(module_data)
    freq_admin = 'ansible_collections.cisco.aci.plugins.module_utils.aci_op'
    assert(freq_admin in module_data)

    module_data = module_data.encode(errors='surrogate_or_strict')

    m = PSModuleDepFinder()
    m.scan_module(module_data, "ansible_collections.cisco.aci.plugins.modules.network.aci.aci_aep")

    assert(freq_admin in m.ps_modules)


# Generated at 2022-06-12 21:44:52.157174
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # prepare data for the execution of the method under test
    import random
    _key = random.randint(0, 1000)
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.exec_scripts = {_key: None}

    try:
        ps_module_dep_finder.scan_exec_script(to_text(_key))
    except Exception:
        pass



# Generated at 2022-06-12 21:45:14.097964
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import pytest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic
    module_data = open(os.path.join(os.path.dirname(basic.__file__), "common.psm1")).read().encode('utf-8')
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_module(module_data)
    assert len(ps_module_dep_finder.ps_modules) > 0
    module_data = open(os.path.join(os.path.dirname(AnsibleModule.__file__), "basic.cs")).read().encode('utf-8')
    ps_module_dep_finder.scan_module(module_data)

# Generated at 2022-06-12 21:45:18.812552
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    ps_module_dep_finder = PSModuleDepFinder()

    assert ps_module_dep_finder.exec_scripts == {}

    ps_module_dep_finder.scan_exec_script('powershell.py')

    assert ps_module_dep_finder.exec_scripts != {}

# Generated at 2022-06-12 21:45:21.975632
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class Args():
        def __init__(self):
            self.name = "Value Was Not Set"
            self.dest = "Value Was Not Set"
            self.tempdir = "Value Was Not Set"
    args = Args()
    test_obj = PSModuleDepFinder()
    test_obj.scan_exec_script(args.name)
    assert test_obj.exec_scripts == {}

# Generated at 2022-06-12 21:45:23.646657
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Instantiate PSModuleDepFinder object
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script("test_script.ps1")


# Generated at 2022-06-12 21:45:30.354464
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Do not generate coverage for this function since it's a method of class PSModuleDepFinder
    # which is already under coverage
    #
    # Currently the method is a stub which does nothing but returning.
    # This test function is intended to cover the function definition
    # for the sake of code coverage.
    mdf = PSModuleDepFinder()
    mdf.scan_module(None)
    assert True



# Generated at 2022-06-12 21:45:40.075384
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()
    assert finder.ps_modules == dict()

    # Taken from win_ping
    finder.scan_module("#Requires -Module Ansible.ModuleUtils.Credentials.Credentials")
    assert len(finder.ps_modules) == 1
    assert finder.ps_modules["Ansible.ModuleUtils.Credentials.Credentials"]['data']

    # Taken from win_ping, wrapped in base64
    finder.scan_module("IyBSZXF1aXJlcyAtTW9kdWxlIEFuc2libGUuTW9kdWxlVW50aWxzLkNyZWRlbnRpYWxzLkNyZWRlbnRpYWxz")

# Generated at 2022-06-12 21:45:47.212621
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Setup test
    pmdf = PSModuleDepFinder()
    pmdf.scan_module('#Requires -Module Ansible.ModuleUtils.TestModule')
    pmdf.scan_module('#requires -version 4.0')
    # Assert
    assert pmdf.ps_modules['Ansible.ModuleUtils.TestModule']['data'] is not None
    assert pmdf.ps_version == "4.0"


# Generated at 2022-06-12 21:45:57.676522
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """exercise scan_exec_script method of PSModuleDepFinder

    """
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script("payload_wrapper")
    assert sorted(list(psmdf.ps_modules.keys())) == ['Ansible.ModuleUtils.Common']
    assert len(psmdf.cs_utils_wrapper) == 0
    psmdf.scan_exec_script("powershell_payload")

# Generated at 2022-06-12 21:46:07.202310
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print('Checking scan_exec_script method of PSModuleDepFinder class')
    try:
        from ansible.executor.powershell import PSModuleDepFinder
    except Exception as err:
        print("Could not import class 'PSModuleDepFinder' from ansible.executor.powershell")
        print(err)
        return
    else:
        print("Successfully imported  class 'PSModuleDepFinder' from ansible.executor.powershell")

    obj = PSModuleDepFinder()
    print("Instatntiated an object of PSModuleDepFinder class")

    name = "TEST_PSModuleDepFinder_scan_exec_script"
    print("Name is {}".format(name))

# Generated at 2022-06-12 21:46:14.412763
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    script = """#Requires -Module Ansible.ModuleUtils.Foobar
Write-Host "Hello World"
"""
    finder = PSModuleDepFinder()
    finder.scan_module(script)
    #test if the module returned is correct

# Generated at 2022-06-12 21:46:44.204979
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Setup
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.become = True
    ps_module_dep_finder.exec_scripts = {
        "CR": "123",
        "LF": "12345\n",
        "CRLF": "12345\r\n"}
    ps_module_dep_finder.ps_version = "1.0.1"
    ps_module_dep_finder.os_version = "3.5"
    ps_module_dep_finder.ps_modules = {
        "Ansible.ModuleUtils.CR": "123",
        "Ansible.ModuleUtils.LF": "12345\n",
        "Ansible.ModuleUtils.CRLF": "12345\r\n"}
   

# Generated at 2022-06-12 21:46:50.291159
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script("powershell_exec")
    assert "powershell_exec" in ps_module_dep_finder.exec_scripts.keys()
    assert "Get-PipVersion" in ps_module_dep_finder.ps_modules.keys()


# Generated at 2022-06-12 21:46:52.113517
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False, "Test cases not implemented"

# Generated at 2022-06-12 21:46:57.264731
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('powershell')
    names = set(finder.exec_scripts.keys())
    assert names == {'powershell', 'common', 'base', 'socket', 'json', 'xml', 'ymal', 'encryption', 'windows'}

# Generated at 2022-06-12 21:47:00.368128
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # mdf = PSModuleDepFinder()
    # mdf.scan_exec_script("runps")
    assert True  # TODO: implement your test here


# Generated at 2022-06-12 21:47:09.522392
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Case 1: AnsibleError exception is raised when invalid script name is passed
    finder = PSModuleDepFinder()
    try:
        finder.scan_exec_script("invalid_exec_script")
        assert False, "AnsibleError exception not raised"
    except AnsibleError:
        pass
    # Case 2: Valid script should be added to exec_scripts dict of PSModuleDepFinder
    finder = PSModuleDepFinder()
    finder.scan_exec_script("PowershellCore")
    assert finder.exec_scripts.get("PowershellCore") is not None
    # Case 3: scan_exec_script should recursively scan the module_util files in the exec script
    finder = PSModuleDepFinder()
    finder.scan_exec_script("PowershellCore")
    assert find

# Generated at 2022-06-12 21:47:12.521452
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    rd = PSModuleDepFinder()
    rd.scan_exec_script('basic')


# Generated at 2022-06-12 21:47:15.934829
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('Common')
    assert finder.exec_scripts['Common'] is not None
    assert finder.ps_modules["Ansible.PowerShell.Common"] is not None



# Generated at 2022-06-12 21:47:17.514151
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test the scan_exec_script method of class PSModuleDepFinder
    assert True



# Generated at 2022-06-12 21:47:26.046535
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    script_name = "azure_rm_loganalyticsdatasource_info"

    testcase = PSModuleDepFinder()
    testcase.scan_exec_script(script_name)


# Generated at 2022-06-12 21:48:19.119056
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass # tested in test/units/module_utils/powershell/test_module_deps.py


# Generated at 2022-06-12 21:48:20.449174
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    return


# Generated at 2022-06-12 21:48:22.542407
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    name = "executor"
    finder.scan_exec_script(name)



# Generated at 2022-06-12 21:48:25.933608
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test that the name of the __init__ script is not required
    psmdf_test1 = PSModuleDepFinder()
    psmdf_test1.scan_exec_script('SampleScript')
    assert psmdf_test1.exec_scripts == {'SampleScript': b''}


# Generated at 2022-06-12 21:48:29.316630
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    '''
    Test scan_exec_script method.
    '''
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('test')
    assert dep_finder.exec_scripts['test'] is not None


# Generated at 2022-06-12 21:48:39.534170
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # initialize the global var in module_utils.ps_general_loader
    ps_module_utils_loader.PS_MODULE_UTILS_TEXTFS_CACHE = {}

    # initialize the module_util dep finder
    finder = PSModuleDepFinder()

    # scan the exec script 'ipconfig.ps1' for all its depending module_utils
    finder.scan_exec_script("ipconfig")
    # assert that it finds the module_utils.basic and encodings
    assert "Ansible.ModuleUtils.Basic" in finder.ps_modules
    assert "Ansible.ModuleUtils.Encoding" in finder.ps_modules



# Generated at 2022-06-12 21:48:48.265226
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    test_data = b"""#Requires -Version 7.1

#AnsibleRequires -PowerShell Ansible.ModuleUtils.TestUtil1
#AnsibleRequires -PowerShell Ansible.ModuleUtils.TestUtil2
#AnsibleRequires -PowerShell Ansible.ModuleUtils.TestUtil3 -Optional
#AnsibleRequires -PowerShell ..TestUtil4
#AnsibleRequires -PowerShell ..TestUtil5 -Optional

"""
    depfinder = PSModuleDepFinder()
    depfinder.scan_module(test_data)
    assert len(depfinder.ps_modules) == 4
    assert len(depfinder.cs_utils_module) == 0
    assert len(depfinder.cs_utils_wrapper) == 0
    assert len(depfinder.exec_scripts) == 0

    # Test optional

# Generated at 2022-06-12 21:48:48.820959
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:48:53.886387
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print("Checking If method scan_exec_script of class PSModuleDepFinder is working or not")

    dep_finder = PSModuleDepFinder()
    name = "name"
    dep_finder.exec_scripts = {name : "value"}

    dep_finder.scan_exec_script(name)
    print('method scan_exec_script of class PSModuleDepFinder is working')


# Generated at 2022-06-12 21:49:00.075967
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("posh-accessibility")
    assert("posh-accessibility" in finder.exec_scripts)
    assert("posh-accessibility" in finder.cs_utils_wrapper)
    assert("Ansible.ModuleUtils.Security" in finder.ps_modules)


# Generated at 2022-06-12 21:50:03.515224
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    def _strip_comments(b_data):
        b_stripped_data = b''
        in_comment = False
        for line in b_data.split(b'\n'):
            if line.startswith(b'#'):
                in_comment = True
            elif in_comment and not line.strip():
                in_comment = False
            else:
                break
        for line in b_data.split(b'\n'):
            if not line.startswith(b'#') or in_comment:
                b_stripped_data += line + b'\n'
            if line.endswith(b'#'):
                b_stripped_data += b'\n'
                in_comment = True
            elif in_comment and not line.strip():
                in_comment

# Generated at 2022-06-12 21:50:15.554145
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    #
    # test_1
    #
    test_1_name = 'psr'
    test_1_data = '''
# this is a comment
# ansiblerequires -wrapper psr
# ansiblerequires -powershell ansible.module_utils.test_module_util
# ansiblerequires -csharputil ansible.module_utils.test_module_util
    '''
    test_1_module_util_data = '# this is a util comment\n'
    test_1_exec_script_data = '# this is a exec script comment\n'
    test_1_expected_exec_scripts = {'psr': test_1_exec_script_data}

# Generated at 2022-06-12 21:50:21.692377
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    assert psmdf.scan_exec_script("wrapper")
    psmdf = PSModuleDepFinder()
    psmdf.exec_scripts = {'foo': 'bar'}
    assert psmdf.scan_exec_script("foo")
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script.when.called_with("test_import_scripts").should.throw(AnsibleError)


# Generated at 2022-06-12 21:50:23.522543
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False  # TODO: implement your test here


# Generated at 2022-06-12 21:50:31.174931
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.powershell.executor import PSModuleDepFinder
    import ansible.executor.powershell

    test_name = 'test_exec_script'
    test_exec_script = 'Test-ExecScript'

    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script(test_name)

    assert dep_finder.exec_scripts[test_name] == to_bytes(ansible.executor.powershell.__dict__[test_exec_script])



# Generated at 2022-06-12 21:41:14.917388
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    _test_fixture_path = os.sep.join(['test', 'units', 'test_module_utils', 'support', 'test_ansible_module_wrapper_1.ps1'])
    _test_data1 = _slurp(_test_fixture_path)
    check_PSModuleDepFinder_scan_exec_script_1 = PSModuleDepFinder()
    check_PSModuleDepFinder_scan_exec_script_1.scan_module(_test_data1, wrapper=True)
    check_PSModuleDepFinder_scan_exec_script_1.scan_exec_script('test_ansible_module_wrapper_1.ps1')
    assert len(check_PSModuleDepFinder_scan_exec_script_1.exec_scripts) == 1
    assert check_PSModuleDepFinder_

# Generated at 2022-06-12 21:41:20.026776
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_module_utils = PSModuleDepFinder()
    test_module_utils.scan_exec_script(name='AnsibleModule')
    assert isinstance(test_module_utils.exec_scripts, dict)
    assert 'AnsibleModule' in test_module_utils.exec_scripts



# Generated at 2022-06-12 21:41:24.692316
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert isinstance(ps_module_dep_finder_0, PSModuleDepFinder)

    with pytest.raises(AnsibleError):
        ps_module_dep_finder_0.scan_exec_script("some_name_that_doesnt_exist")


# Generated at 2022-06-12 21:41:27.594484
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # TODO: fix the test
    raise AnsibleError('test not implemented')



# Generated at 2022-06-12 21:41:28.717977
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
  pass



# Generated at 2022-06-12 21:41:36.057102
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # TODO: mock pkgutil.get_data
    err = None
    try:
        PSModuleDepFinder().scan_exec_script("")
    except Exception as e:
        err = to_text(e)

    assert err == 'Could not find executor powershell script for \'\'', \
        'The method scan_exec_script should raise the following exception: {0}'.format(to_native(err))


# Generated at 2022-06-12 21:41:42.584549
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # This method tests scan_exec_script method of class PSModuleDepFinder
    # which scans lib/ansible/executor/powershell for scripts used in the module
    # exec side. It also scans these scripts for any dependencies
    mdf = PSModuleDepFinder()
    mdf.cs_utils_module = {""}
    mdf.cs_utils_wrapper = {""}
    mdf.ps_modules = {""}
    mdf.exec_scripts = {""}

    mdf.scan_exec_script('')


# Generated at 2022-06-12 21:41:51.183039
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import os
    from ansible.utils.collection_loader import PSModuleDepFinder

    dep_finder = PSModuleDepFinder()
    import_module_path = resource_from_fqcr("collections.ns.coll.plugins.modules.module1.psm1")
    with open(import_module_path, "rb") as module_file:
        dep_finder.scan_module(module_file.read())

    expected_result = {'Ansible.ModuleUtils.ModuleUtil1': {
        'data': to_bytes(_slurp("lib/ansible/module_utils/ModuleUtil1.psm1")),
        'path': to_text("lib/ansible/module_utils/ModuleUtil1.psm1"),
    }}
    assert dep_finder.ps_modules == expected_result

# Generated at 2022-06-12 21:41:52.219541
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:42:01.558566
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    """
    Function used to test the scan_module method of the PSModuleDepFinder class
    :return:
    """
    dep_finder = PSModuleDepFinder()


# Generated at 2022-06-12 21:42:15.829740
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    # Data prep
    depfinder = PSModuleDepFinder()
    name = "test_script"

    # Test
    depfinder.scan_exec_script(name)

    # Assert
    assert name in depfinder.exec_scripts.keys()

# Generated at 2022-06-12 21:42:22.180428
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    def mock_get_data(package, resource):
        """ Mock pkgutil.get_data function which returns a random data """
        return os.urandom(9)

    fake_exec_scripts = {to_text(random.randrange(0, 1000)): to_text(random.randrange(0, 1000)) for _ in range(0, random.randrange(0, 50))} # [random.randrange(0, 1000):random.randrange(0, 1000) for _ in range(0, random.randrange(0, 50))]

    fake_exec_scripts_b = {to_native(k): base64.b64encode(to_bytes(v)) for k, v in fake_exec_scripts.items()}


# Generated at 2022-06-12 21:42:24.630934
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_obj = PSModuleDepFinder()
    test_obj.scan_exec_script("powershell")
    assert "powershell" in test_obj.exec_scripts

# Generated at 2022-06-12 21:42:26.500520
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    f = PSModuleDepFinder()
    f.scan_exec_script("common_exec")


# Generated at 2022-06-12 21:42:36.690303
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # data contains the module code
    obj = PSModuleDepFinder()
    name = mock.MagicMock(return_value='test')
    obj.scan_exec_script(name)
    # Test with exception:
    #  raise AnsibleError("Could not find executor powershell script "
    #                        "for '%s'" % name)
    mock_executor = mock.MagicMock(return_value=None)
    with pytest.raises(AnsibleError) as err:
        obj.scan_exec_script(mock_executor)
    assert "Could not find executor powershell script for 'test'" in to_text(err.value)


# Generated at 2022-06-12 21:42:44.582011
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    ps = PSModuleDepFinder()
    ps.scan_module("""
            using System;
            using System.Management.Automation;
            using System.Management.Automation.Language;
            using System.Globalization;
            using System.Xml;
            using System.IO;
            using System.Collections.Generic;
            #Requires -Module Ansible.ModuleUtils.Pester
            #Requires -Module Ansible.ModuleUtils.MyModule
            """)
    assert ps.ps_modules["Ansible.ModuleUtils.Pester"]
    assert ps.ps_modules["Ansible.ModuleUtils.MyModule"]
    assert len(ps.ps_modules) == 2



# Generated at 2022-06-12 21:42:47.415949
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script('powershell.exe')
    assert psmdf.exec_scripts['powershell.exe'] is not None


# Generated at 2022-06-12 21:42:50.443458
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_obj = ansible.modules.windows.win_package.PSModuleDepFinder()
    assert test_obj.scan_exec_script('Name') == None


# Generated at 2022-06-12 21:43:02.943960
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script(): 
    os = mock.MagicMock()
    os.path = mock.MagicMock()
    os.path.join = mock.MagicMock(return_value='/home/myuser/fs/ansible/executor/powershell/ansible_module_augeas.ps1')
    pkg_util = mock.MagicMock()
    pkg_util.get_data = mock.MagicMock(return_value='module_source_content')
    pkg_util.get_data.return_value = 'module_source_content'
    pkg_util.get_data.return_value.split = mock.MagicMock(return_value=['module_source_content_splitted'])
    
    loader = mock.MagicMock()

# Generated at 2022-06-12 21:43:12.948359
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    '''
    Validate the scan_exec_script method against the following assumptions:
    - Scanning a module script that is not present raises an error
    - Scanning a module script that is present succeeds
    '''

    # Arrange
    finder = PSModuleDepFinder()
    script_name = 'valid_script_that_is_not_present'

    # Act/Assert
    with pytest.raises(AnsibleError):
        finder.scan_exec_script(script_name)

    valid_script_name = 'read_json'
    finder.scan_exec_script(valid_script_name)
    assert valid_script_name in finder.exec_scripts

    # Assert PS Module Dep finder is not empty
    assert bool(finder.ps_modules)

    # Assert the presence of module

# Generated at 2022-06-12 21:43:26.460445
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print("START")
    # Some tests
    psm = PSModuleDepFinder()
    psm.scan_exec_script("ansible.module_utils.basic")
    print("END")



# Generated at 2022-06-12 21:43:35.667541
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    # This is a simple test of the 'scan_module' method in the PSModuleDepFinder class.

    # Initialize an instance of the PSModuleDepFinder class
    ps_module_dep_finder = PSModuleDepFinder()

    # Initialize a string to be used as the module data to be scanned

# Generated at 2022-06-12 21:43:43.743532
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    psmd = PSModuleDepFinder()

    psmd.scan_exec_script('common')
    psmd.scan_exec_script('common')
    psmd.scan_exec_script('common_windows')
    psmd.scan_exec_script('common_windows')

    result = psmd.exec_scripts['common']
    assert result
    result = psmd.exec_scripts['common_windows']
    assert result

    assert len(psmd.exec_scripts) == 2


# Generated at 2022-06-12 21:43:54.078997
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils import basic
    import os
    from io import BytesIO
    
    #content = BytesIO(u"#Requires -Module Ansible.ModuleUtils.AnsibleModule")
    content = os.path.join(os.path.dirname(basic.__file__), "basic.ps1")
    #print(os.path.dirname(basic.__file__))
    #print(content)
    data = _slurp(content)
    #data = BytesIO(u"#Requires -Module Ansible.ModuleUtils.AnsibleModule")
    ps_module_dep_finder = PSModuleDepFinder()
    result = ps_module_dep_finder.scan_exec_script("basic")
    
    assert True == result
    

# Generated at 2022-06-12 21:43:57.681863
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    result= PSModuleDepFinder.scan_exec_script("ansible.module_utils.powershell.Network.Connection")
    assert result == None


# Generated at 2022-06-12 21:43:58.621604
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:44:01.902910
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmd = PSModuleDepFinder()
    psmd.scan_exec_script("test_script")
    assert psmd.exec_scripts["test_script"] == b"test_data"



# Generated at 2022-06-12 21:44:12.940438
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

    module_objects = {
        'ansible': basic,
        'ansible.module_utils.basic': AnsibleModule,
    }

    with open(os.path.join(os.path.dirname(__file__), '..', '..', 'hacking', 'test', 'data', 'module_data', 'lookup_module_data', 'lookup_module.ps1'), 'rb') as f:
        m = f.read()

    f = PSModuleDepFinder()

    f.scan_module(m, fqn='ansible.plugins.lookup.lookup')

    assert f.ps_modules['Ansible.ModuleUtils.PowerShell.Convert']['data'].startswith

# Generated at 2022-06-12 21:44:25.781749
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    mock_module_data = """
#AnsibleRequires -PowerShell Ansible.ModuleUtils.Powershell.Management
#Requires -Module Ansible.ModuleUtils.{name}
#AnsibleRequires -CSharpUtil Ansible.Util
#AnsibleRequires -CSharpUtil Ansible.Util
#AnsibleRequires -CSharpUtil ansible_collections.namespace.collection.plugins.module_utils.utility
#AnsibleRequires -CSharpUtil ..module_utils.utility
#requires -version 3.0
#ansiblerequires -osversion 6.1
#ansiblerequires -become
#AnsibleRequires -Wrapper util
"""
    ps_module_dep_finder = PSModuleDepFinder()

# Generated at 2022-06-12 21:44:34.238944
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mdf = PSModuleDepFinder()
    assert mdf.exec_scripts == {}
    mdf.scan_exec_script('wait_for')
    assert len(mdf.exec_scripts) == 1
    assert 'wait_for' in mdf.exec_scripts
    mdf.scan_exec_script('wait_for')
    assert len(mdf.exec_scripts) == 1
    assert 'wait_for' in mdf.exec_scripts


# Generated at 2022-06-12 21:44:58.439179
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
	file_path = get_fixture_path("basic_powershell/command_module_util.psm1")
	file_data = _slurp(file_path)
	mdf = PSModuleDepFinder()
	mdf.scan_module(file_data, fqn=None, wrapper=False, powershell=True)
	assert mdf.ps_modules == {"Ansible.ModuleUtils.PowerShell.Admin": {'data': b'[bytes]', 'path': u'C:\\Users\\ansibler\\ansible\\lib\\ansible\\module_utils\\powershell\\admin\\Ansible.ModuleUtils.PowerShell.Admin.psm1'}}
	assert mdf.cs_utils_wrapper == {}
	assert mdf.cs_utils_module == {}
	assert mdf.ps_version

# Generated at 2022-06-12 21:45:09.400078
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # A setup function to set up the objects to be used in each test
    def test_setup(ps_modules, cs_utils_wrapper, cs_utils_module, exec_scripts):
        finder = PSModuleDepFinder()
        if ps_modules is not None:
            finder.ps_modules = ps_modules
        if cs_utils_wrapper is not None:
            finder.cs_utils_wrapper = cs_utils_wrapper
        if cs_utils_module is not None:
            finder.cs_utils_module = cs_utils_module
        if exec_scripts is not None:
            finder.exec_scripts = exec_scripts

        return finder

    # Simple test that a file with no comments is not changed by comment removal.
    # This is a negative test, it ensures that a comment in a module is not found.


# Generated at 2022-06-12 21:45:13.331250
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """
    Ensure PSModuleDepFinder._scan_exec_script() works as expected.
    """
    psmd = PSModuleDepFinder()
    psmd.scan_exec_script('Get-TestExecScript')


# Helper method to generate random printable string between min and max size

# Generated at 2022-06-12 21:45:14.901070
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mu = PSModuleDepFinder()
    assert mu.scan_exec_script('script') != None

# Generated at 2022-06-12 21:45:21.481526
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import pytest
    from ansible.module_utils.powershell import AnsibleModule

    AnsibleModule.init_powershell()
    # import the powershell module_utils
    __import__('ansible_collections.ansible.builtin.plugins.module_utils.powershell.basic')
    __import__('ansible_collections.ansible.builtin.plugins.module_utils.powershell.common')

    d = PSModuleDepFinder()
    script_module = resource_from_fqcr('ansible_collections.ansible.builtin',
                                       'script', 'script')

    module_data = _slurp(script_module)

    # module contains the PS module_utils in a comment

# Generated at 2022-06-12 21:45:32.724701
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.common._json_compat import _json_read_dict

    test_module_data = """
#Requires -Module Ansible.ModuleUtils.CommonModuleUtils

param(
  [string]  $first_param,
  [string]  $second_param

)

function foo {
  Write-Output "Hello World"
}
"""
    finder = PSModuleDepFinder()
    finder.scan_module(test_module_data)
    assert finder.ps_modules == {
        u'Ansible.ModuleUtils.CommonModuleUtils': {
            'data': 'TEST_DATA',
            'path': u'TEST_PATH',
        }
    }, "Failed to find module util"


# Generated at 2022-06-12 21:45:41.736758
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    #test we can scan an exec script
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script('common_wrapper')
    assert len(ps_module_dep_finder.exec_scripts.keys()) > 0
    assert len(ps_module_dep_finder.ps_modules.keys()) > 0
    assert len(ps_module_dep_finder.cs_utils_wrapper.keys()) > 0
    assert len(ps_module_dep_finder.cs_utils_module.keys()) == 0
    assert ps_module_dep_finder.ps_version is None
    assert ps_module_dep_finder.os_version is None
    assert ps_module_dep_finder.become is False


# Generated at 2022-06-12 21:45:49.927288
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    util = ps_module_utils_loader.find_plugin(to_text('Ansible.Common.Parsing'), '.psm1')
    data = to_bytes(_slurp(util))
    f = PSModuleDepFinder()
    f.scan_module(data)
    assert(len(f.ps_modules) > 0)
    assert(len(f.cs_utils_wrapper) > 0)
    assert(len(f.cs_utils_module) == 0)
    assert(len(f.exec_scripts) == 0)


# Generated at 2022-06-12 21:46:00.535207
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:46:03.967172
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('common')
    assert 'common' in finder.exec_scripts
    assert 'common' in finder.ps_modules
    assert len(finder.cs_utils_wrapper) == 0
    assert len(finder.cs_utils_module) == 0



# Generated at 2022-06-12 21:46:19.204717
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # TODO: Implement test_PSModuleDepFinder_scan_module
    raise NotImplementedError()


# Generated at 2022-06-12 21:46:22.349945
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    run_this_code_before_the_test_case()
    # TODO: Write Unit Test
    assert True  # if we got here then the test should be marked as passed


# Generated at 2022-06-12 21:46:31.495520
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # test the following case:
    #
    # [ansible.builtin.sosreport]
    # ...
    # self.exec_wrapper_path = os.path.join(os.getcwd(), 'sosreport.ps1')
    # exec_wrapper = pkgutil.get_data("ansible.executor.powershell", "sosreport.ps1")
    #
    # Verify the executor powershell script contents can be fetched
    #
    # Verify wrapper dependencies are scanned properly
    #
    # Verify exec_scripts dictionary is populated with contents of sosreport.ps1
    pass



# Generated at 2022-06-12 21:46:40.288729
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Configure the test case data
    test_data_0 = "{0}\n{1}\n{2}\n{3}\n".format(
        "#AnsibleRequires -CSharpUtil ansible_collections.test.test_collection.plugins.module_utils.test_csutil_0",
        "#AnsibleRequires -CSharpUtil ansible_collections.test.test_collection.plugins.module_utils.test_csutil_1",
        "#AnsibleRequires -CSharpUtil test_csutil_2",
        "#AnsibleRequires -Powershell xxx.yyy")


# Generated at 2022-06-12 21:46:48.157975
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test = PSModuleDepFinder()
    # Pass no arguments, should raise an exception
    try:
        test.scan_exec_script( )
        assert False, "Should have thrown an exception"
    except Exception:
        pass
    # Pass invalid name, should raise exception
    try:
        test.scan_exec_script( "bad" )
        assert False, "Should have thrown an exception"
    except Exception:
        pass
    # Pass valid name for script
    test.scan_exec_script( "powershell_script" )
    # Check that it was added to exec_scripts
    assert "powershell_script" in test.exec_scripts, "Should have added to exec_scripts"


# Generated at 2022-06-12 21:47:00.420930
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import mock
    from ansible.executor.powershell import ps_module_utils_wrapper as ps

    test_script = """
    #Requires -Module Ansible.ModuleUtils.Powershell.Core

    $ExecutionContext = Get-Variable -Name ExecutionContext -ValueOnly

    if ($ExecutionContext -isnot [System.Management.Automation.PSLocalJobs.JobInvocationInfo]) {
        # this is being piped into powershell.exe not being invoked as a module
        $script:PathToModuleFile = [IO.Path]::GetFullPath($PSCommandPath)
    } else {
        Write-Warning 'Invoked in a job, skipping module invocation.'
        exit -1
    }

    Write-Warning "hello world!"
    """


# Generated at 2022-06-12 21:47:09.559185
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Sanity checks of the script which has already been tested here:
    # https://github.com/ansible/ansible/blob/devel/test/units/modules/windows/win_copy/test_win_copy.py#L28

    # These scripts are small so we are just going to test them again to be sure.
    # The larger ones should be tested as part of core.
    checksum_script = pkgutil.get_data("ansible.executor.powershell", "checksum.ps1")
    assert checksum_script
    checksum_script_stripped = _strip_comments(checksum_script)
    if C.DEFAULT_DEBUG:
        assert checksum_script == checksum_script_stripped
    else:
        assert b"Write-Error" not in checksum_script_stripped

   

# Generated at 2022-06-12 21:47:16.094097
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # This is a helper method that runs a few scenarios.
    # It is also used by test_PSModuleDepFinder_find_deps.
    # It currently only tests PS modules.
    finder = PSModuleDepFinder()
    finder.scan_module("""
#Requires -Module Ansible.ModuleUtils.Foo
""", fqn="ansible.builtin.foo")
    finder.scan_module("""
#Requires -Module Ansible.ModuleUtils.Foo
""", fqn="ansible.builtin.bar")
    assert finder.ps_modules['Ansible.ModuleUtils.Foo']['path'] == 'ansible/modules/foo/module_utils/Ansible.ModuleUtils.Foo.psm1'


# Generated at 2022-06-12 21:47:24.972000
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.win_module import PSModuleDepFinder
    from ansible.module_utils.six import BytesIO

    finder = PSModuleDepFinder()

    # This module has dependencies on 5 module_utils

# Generated at 2022-06-12 21:47:33.177413
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils import basic
    from ansible.plugins.action import ActionBase

    module_deps = PSModuleDepFinder()

    # Basic test that the finder works
    module_data = "".join([
        "#Requires -Module Ansible.ModuleUtils.Legacy",
        "#Requires -Module Ansible.ModuleUtils.Legacy.Common",
        "#Requires -Module Ansible.ModuleUtils.Legacy.Unix",
    ])

    module_deps.scan_module(module_data)
    assert len(module_deps.ps_modules) == 3

    # Test that a CS util is found

# Generated at 2022-06-12 21:47:49.276809
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.plugins.action.powershell import ActionModule
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script(ActionModule.executable_wrapper)

    assert ps_module_dep_finder.exec_scripts[ActionModule.executable_wrapper]
    assert ps_module_dep_finder.cs_utils_wrapper

# Generated at 2022-06-12 21:47:59.640746
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    depfinder = PSModuleDepFinder()
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("common")
    assert dep_finder.exec_scripts["common"] is not None
    assert dep_finder.ps_modules["Ansible.ModuleUtils.Common"]["data"] is not None
    assert dep_finder.ps_modules["Ansible.ModuleUtils.Common"]["path"] == "ansible.executor.powershell.module_utils.common"

    dep_finder.scan_exec_script("powershell")
    assert dep_finder.exec_scripts["powershell"] is not None
    assert dep_finder.ps_modules["Ansible.ModuleUtils.PowerShell"]["data"] is not None

# Generated at 2022-06-12 21:48:02.529032
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_dep_finder = PSModuleDepFinder()
    ps_dep_finder.scan_exec_script("win_copy")



# Generated at 2022-06-12 21:48:03.480115
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:48:13.309584
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:48:21.107372
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test the scan_exec_script method
    import ansible
    import ansible.executor.powershell as ps_exec
    from ansible.executor.powershell import scripts
    from ansible.plugins.loader import ps_module_utils_loader
    from ansible.module_utils.common.collections import PSModuleDepFinder, PSModuleUtilInfo
    # Check that the scan_exec_script works and the various results match up
    # for a script in the ansible.executor.powershell scripts dict.
    ansible_full_path = ansible.__file__.split('/__init__.py')[0]
    ps_exec_path = os.path.join(ansible_full_path, 'executor/powershell')
    dep_finder = PSModuleDepFinder()

# Generated at 2022-06-12 21:48:28.662107
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text
    import pkgutil

    # Mock AnsibleModule and basic AnsibleModule methods.
    mocked_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    mocked_module.fail_json = lambda **kwargs: module.fail_json(**kwargs)
    mocked_module.exit_json = lambda **kwargs: module.exit_json(**kwargs)
    mocked_module.params = {}

    # Required module support code to test.
    test_module_data = pkgutil.get_data("ansible_collections.ansible.builtin.plugins.modules", "win_copy.psm1")
    test_module_data = to_

# Generated at 2022-06-12 21:48:36.240418
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    b_data = '#ExecScripts: foo, exec\n#!'
    mdf = PSModuleDepFinder()
    mdf.scan_module(b_data, wrapper=True, powershell=True)
    assert 'foo' in mdf.exec_scripts
    assert mdf.exec_scripts['foo'] == b'#!'
    assert 'exec' in mdf.exec_scripts
    assert mdf.exec_scripts['exec'] == b'#!'


# Generated at 2022-06-12 21:48:38.639467
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class_inst = PSModuleDepFinder()
    class_inst.scan_exec_script(name = "1")

# Generated at 2022-06-12 21:48:46.125789
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    #
    #  In this test we use ansible_collections.microsoft.azure.plugins.module_utils.azure_arm_utils
    #
    m = PSModuleDepFinder()

    m.scan_exec_script("azure_rm_common_exec_calls")

    assert "ansible_collections.microsoft.azure.plugins.module_utils.azure_arm_utils" in m.cs_utils_wrapper
    assert "Ansible.ModuleUtils.PowerShell.MultiOutput" in m.ps_modules
    assert "azure_rm_common_exec_calls" in m.exec_scripts


# Generated at 2022-06-12 21:49:07.454251
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import os
    import sys
    import tempfile
    import unittest
    from ansible.module_utils.common._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common import tmp_module_util_path
    from ansible.module_utils.ps_module_utils import PSModuleDepFinder

    def create_temp_module_util_file(name, content):
        """Creates a temporary module_util file in the directory returned by
        L{tmp_module_util_path}, and registers it for deletion in cleanup.

        @param name: Name of the module_util file
        @param content: Contents of the module_util file
        @return: Path to the temporary module_util file
        """

# Generated at 2022-06-12 21:49:09.752570
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('Default')

    assert dep_finder.exec_scripts
    assert dep_finder.exec_scripts['Default']


# Generated at 2022-06-12 21:49:21.367356
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script(): # pylint: disable=too-many-locals,too-many-statements
    actual = PSModuleDepFinder()
    expected = PSModuleDepFinder()
    # Call function
    actual.scan_exec_script("Common")
    # Test assertions
    assert actual.ps_modules == expected.ps_modules
    assert actual.cs_utils_wrapper == expected.cs_utils_wrapper
    assert actual.cs_utils_module == expected.cs_utils_module
    assert actual.ps_version == expected.ps_version
    assert actual.os_version == expected.os_version
    assert actual.become == expected.become

# Generated at 2022-06-12 21:49:31.336272
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    plugin_loader_module_utils = to_bytes(ps_module_utils_loader.find_plugin('Ansible.ModuleUtils.Common', '.psm1'))
    plugin_loader_data = to_bytes(_slurp(plugin_loader_module_utils))
    cs_module_loader_module_utils = to_bytes(ps_module_utils_loader.find_plugin('Ansible.ModuleUtils.Legacy', '.cs'))
    cs_module_loader_data = to_bytes(_slurp(cs_module_loader_module_utils))
    mock_module_utils = to_bytes(resource_from_fqcr('namespace.collection.plugins.module_utils.some_module', 'some_module'))

# Generated at 2022-06-12 21:49:42.789718
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    _exec_script_name = "test_PSModuleDepFinder_scan_exec_script"
    _exec_script_path = os.path.join(C.TEST_DIR, "ansible", "executor", "powershell", _exec_script_name + ".ps1")
    _exec_script_data = "#Requires -Module Ansible.ModuleUtils.Windows.WSMan\n" \
                        "#AnsibleRequires -Wrapper test_PSModuleDepFinder_scan_exec_script"

    _util_script_name = "Windows"
    _util_script_data = "#Requires -Module ansible_collections.microsoft.windows.plugins.module_utils.network"

    _wrapper_script_name = "test_PSModuleDepFinder_scan_exec_script"

# Generated at 2022-06-12 21:49:51.890185
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    obj = PSModuleDepFinder()

    module_data = "this is some test data".encode('utf-8')
    obj.scan_module(module_data, wrapper=True)
    assert obj.exec_scripts == dict()
    assert obj.cs_utils_wrapper == dict()
    assert obj.ps_modules == dict()

    try:
        bad_module_data = "this is some test data".encode('utf-8')
        obj.scan_module(bad_module_data, wrapper=True, powershell=False)
        assert False
    except Exception as e:
        assert "Could not find collection imported module support code for 'Ansible.Util'" in to_native(e.args)



# Generated at 2022-06-12 21:49:54.117301
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('test')
    assert finder.exec_scripts['test'] == ""



# Generated at 2022-06-12 21:49:56.831947
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("exec-wrapper")

# Generated at 2022-06-12 21:49:58.896318
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert PSModuleDepFinder().scan_exec_script(to_text("Python3")) == "Python3"


# Generated at 2022-06-12 21:50:06.267474
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """
    Test scan_exec_script method of PSModuleDepFinder class
    """
    def get_data(data):
        return data

    def import_module(data):
        module = object()
        module.__path__ = ["/path", "mock_path"]
        return module

    def get_data_package(data):
        return data

    from ansible.module_utils import powershell
    powershell.get_data = get_data
    powershell.import_module = import_module
    powershell.pkgutil.get_data = get_data_package

    obj = PSModuleDepFinder()
    obj.become = True
    obj.os_version = "1.0.1"
    obj.ps_version = "2.0.0"


# Generated at 2022-06-12 21:50:25.987230
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    '''
    test_PSModuleDepFinder_scan_module will check scan_module function of class PSModuleDepFinder
    :param self: PSModuleDepFinder object
    :return: None
    '''
    ps = PSModuleDepFinder()
    ps.scan_module("#Requires -Module Ansible.ModuleUtils.Name1\n#Requires -Module Ansible.ModuleUtils.Name2")
    assert ps.ps_modules['Ansible.ModuleUtils.Name1']['path'].endswith("Ansible.ModuleUtils.Name1.psm1")
    assert ps.ps_modules['Ansible.ModuleUtils.Name2']['path'].endswith("Ansible.ModuleUtils.Name2.psm1")
    assert ps.cs_utils_module == {}


# Generated at 2022-06-12 21:50:35.448731
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_module(b"# AnsibleRequires -Wrapper DummyWrapper")
    ps_module_dep_finder.scan_module(b"# AnsibleRequires -CSharpUtil DummyUtil -Optional")
    ps_module_dep_finder.scan_module(b"# AnsibleRequires -PowerShell DummyUtil -Optional")
    ps_module_dep_finder.scan_module(b"# Requires -Module Ansible.DummyUtil")
    ps_module_dep_finder.scan_module(b"# AnsibleRequires -PowerShell ansible_collections.namespace.collection.plugins.module_utils.DummyUtil")
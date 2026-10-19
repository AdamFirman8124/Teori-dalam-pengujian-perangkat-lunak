

# Generated at 2022-06-12 21:41:14.874408
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

  def test_scan_module_1():
    finder = PSModuleDepFinder()
    module_data = '''#Requires -Module Ansible.ModuleUtils.ShellCompatibility
    #Requires -Module Ansible.ModuleUtils.Basic
    #AnsibleRequires -PowerShell ansible_collections.ansible.builtin.plugins.module_utils.basic
    '''
    fqn = "ansible.builtin.test"
    finder.scan_module(to_bytes(module_data), fqn)

# Generated at 2022-06-12 21:41:17.709532
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_object = PSModuleDepFinder()
    test_object.scan_exec_script("shell_common")


# Generated at 2022-06-12 21:41:18.831450
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
  if True:
    assert True


# Generated at 2022-06-12 21:41:22.017092
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("Basic")
    _test_exec_script_added(finder)



# Generated at 2022-06-12 21:41:26.626135
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('basic')
    assert dep_finder.exec_scripts['basic'].startswith(b'#')

# Generated at 2022-06-12 21:41:38.754446
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import ansible.executor.powershell

    PSModuleDepFinder.scan_exec_script(PSModuleDepFinder, 'login')
    assert pkgutil.get_data(name=ansible.executor.powershell.__name__, resource='login.ps1') == PSModuleDepFinder.exec_scripts['login']

    PSModuleDepFinder.scan_exec_script(PSModuleDepFinder, 'command.psm1')
    assert pkgutil.get_data(name=ansible.executor.powershell.__name__, resource='command.psm1') == PSModuleDepFinder.exec_scripts['command.psm1']

    PSModuleDepFinder.scan_exec_script(PSModuleDepFinder, 'command.psm1')

# Generated at 2022-06-12 21:41:42.144321
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import ansible.executor.powershell
    assert ansible.executor.powershell

    x = PSModuleDepFinder()
    assert x

    x.scan_exec_script('script_module')

    assert 'script_module.ps1' in x.exec_scripts.keys()


# Generated at 2022-06-12 21:41:50.823377
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # In order to unit test we have to mock the name/value pairs that are used
    # during the execution of this method
    test_exec_script_name = 'Ansible.ModuleUtils.Common'
    test_exec_script_name2 = 'Ansible.ModuleUtils.Logging'
    test_exec_script_name3 = 'Ansible.ModuleUtils.ArgumentSpec'
    test_cs_util_name = 'Ansible.ModuleUtils.ModuleBase'
    test_cs_util_name2 = 'System.Management.Automation.Runspaces'
    test_cs_util_name3 = 'Ansible.ModuleUtils.ParsingArguments'
    test_cs_util_name4 = 'Ansible.ModuleUtils.Url'
    test_cs_util_name5

# Generated at 2022-06-12 21:41:51.837846
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:41:52.931685
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False # TODO: implement your test here


# Generated at 2022-06-12 21:42:10.765528
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()

    # scan_module should return nothing when passed empty data
    assert finder.scan_module(b"") == set()

    # scan_module should return nothing when passed data with no module refs
    assert finder.scan_module(b"# No module refs here") == set()

    # scan_module should return module ref when passed data with old style
    # '#Requires -Module Ansible.ModuleUtils.{name}'
    assert finder.scan_module(b"#Requires -Module Ansible.ModuleUtils.MyUtil\n") == {("Ansible.ModuleUtils.MyUtil", ".psm1", None, False)}

    # scan_module should return module refs when passed data with old style
    # '#Requires -Module Ansible.ModuleUtils.{

# Generated at 2022-06-12 21:42:14.031821
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import unittest
    import ansible.executor.powershell

    f = PSModuleDepFinder()
    # There is not a good way to test this method because it modifies class
    # attributes, so we instead just call it and make sure that it does not
    # throw exceptions.
    for s in ["windows", "posix"]:
        f.scan_exec_script(s)
        f.scan_exec_script("common")



# Generated at 2022-06-12 21:42:17.114284
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    x = PSModuleDepFinder()
    x.scan_exec_script('basic')
    assert x.exec_scripts == ImmutableDict({u'basic': to_bytes(u'function test-line {return $true}\n')})



# Generated at 2022-06-12 21:42:17.862525
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False, "Test not implemented"


# Generated at 2022-06-12 21:42:18.545817
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
  pytest.skip("Not implemented")


# Generated at 2022-06-12 21:42:26.696853
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    print("START Unit test of scan_exec_script of class PSModuleDepFinder")

    # Initialize the module to be tested
    finder = PSModuleDepFinder()

    # Second parameter of scan_exec_script is the name of the script to be loaded without .ps1
    finder.scan_exec_script("WinRMFindCertificate")

    # Scan the executor script for dependencies
    # Note this test will fail if the script is modified to add dependencies
    finder.scan_module(finder.exec_scripts["WinRMFindCertificate"], fqn=None, wrapper=True)

    assert "ansible_collections.microsoft.windows.plugins.module_utils.certutil" in finder.ps_modules
    assert "Ansible.ModuleUtils.ActiveDirectory.DSC" in finder.ps_modules

# Generated at 2022-06-12 21:42:38.361105
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:42:40.859597
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('ansible_collections.ns.coll.plugins.module_utils.foo')

# Generated at 2022-06-12 21:42:41.474601
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass



# Generated at 2022-06-12 21:42:43.065009
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("powershell")


# Generated at 2022-06-12 21:43:03.238661
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """Unit test for _check_exec_script"""

    module_finder = PSModuleDepFinder()

    # Test a valid module_util reference
    module_finder.scan_exec_script("Win32")
    assert module_finder.exec_scripts["Win32"] is not None
    assert len(module_finder.ps_modules) > 0

    # Test an invalid module_util reference
    try:
        module_finder.scan_exec_script("BadModuleUtil")
        assert False
    except AnsibleError:
        # Expected
        pass


# Generated at 2022-06-12 21:43:13.111926
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    dep_finder = PSModuleDepFinder()

    dep_finder.scan_module("""
#Requires -Module Ansible.ModuleUtils.Common
#AnsibleRequires -PowerShell ansible_collections.foo.bar.plugins.module_utils.net_tools -optional
#AnsibleRequires -CSharpUtil Ansible.ModuleUtils.Basic
#Requires -Module Ansible.ModuleUtils.Network
#AnsibleRequires -CSharpUtil ansible_collections.foo.bar.plugins.module_utils.net_tools.network -Optional
#AnsibleRequires -PowerShell .module_utils.net_tools.network
    """.encode("utf-8"))

    assert dep_finder.ps_modules['Ansible.ModuleUtils.Common']['path'] == 'ansible.module_utils.basic'
   

# Generated at 2022-06-12 21:43:14.585374
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    ps_module_dep_finder = PSModuleDepFinder()
    # TODO How to test this method?
    ps_module_dep_finder.scan_module()


# Generated at 2022-06-12 21:43:19.660204
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()

    # function gets private `exec_scripts` attribute value
    # is that good?
    assert len(dep_finder.exec_scripts) == 0

    # scan_exec_script populates `exec_scripts` attribute
    dep_finder.scan_exec_script("script_name.ps1")
    assert len(dep_finder.exec_scripts) == 1
    assert "script_name.ps1" in dep_finder.exec_scripts

    # scan_exec_script does nothing if script is already in `exec_scripts`
    dep_finder.scan_exec_script("script_name.ps1")
    assert len(dep_finder.exec_scripts) == 1
    assert "script_name.ps1" in dep_finder.exec_scripts

    # scan_exec_script throws Ansible

# Generated at 2022-06-12 21:43:21.013172
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True



# Generated at 2022-06-12 21:43:23.815562
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps = PSModuleDepFinder()
    # call the method
    ps.scan_exec_script("test")
    assert 1==1  # TODO implement your test here


# Generated at 2022-06-12 21:43:32.593579
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Create random data for the test
    random_string = ''.join(random.choice('abcedefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(1, 1000)))
    random_bytes = to_bytes(random_string)

    # Unit test setup
    psmdf = PSModuleDepFinder()
    psmdf.ps_modules = {
        'Ansible.ModuleUtils.Test': {'data': random_bytes, 'path': '/path/to/ansible/lib/ansible/plugins/module_utils/test.psm1'}
    }

    # Run the unit test
    psmdf.scan_exec_script('Test')

    # Assert the result

# Generated at 2022-06-12 21:43:44.956264
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:43:54.596030
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.common._text import to_text
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.powershell.common import _build_powershell_dynamic_module
    # expect that the script is imported
    module_name = 'test_script'
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script(module_name)
    assert module_name in ps_module_dep_finder.exec_scripts.keys()
    assert module_name in ps_module_dep_finder.cs_utils_wrapper.keys()

    # expect that the script is not imported if it does not exist
    module_name = 'test_script_fake'
    ps_module_dep_finder = PSModuleDepFinder()

# Generated at 2022-06-12 21:44:06.611184
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    assert finder.exec_scripts == {}
    finder.scan_exec_script("basic")
    assert finder.exec_scripts == {'basic': b'function join-path {\n  # Implementation ...\n}\n'}
    assert finder.ps_modules == {}
    finder.scan_exec_script("script_for_ps_module")
    assert finder.exec_scripts == {'basic': b'function join-path {\n  # Implementation ...\n}\n', 'script_for_ps_module': b'#Requires -Module Ansible.ModuleUtils.Config\n'}
    assert set(finder.ps_modules.keys()) == {'Ansible.ModuleUtils.Config'}

# Generated at 2022-06-12 21:44:19.812103
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # 
    pass

# Generated at 2022-06-12 21:44:23.245216
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("exec_wrapper")
    assert "exec_wrapper" in dep_finder.exec_scripts.keys()

# Generated at 2022-06-12 21:44:29.728362
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.powershell.executor.module_docs import PowerShellModuleDocs

    psmd = PowerShellModuleDocs("demo")
    ps_executor = psmd._find_executor("thetest")

    # The test is run with CWD being the directory this file is in.
    # Make sure we get a full path to the file.
    # We need to use the original path because it is hashed to provide a unique identifier
    # for the script used in the generated wrapper script.
    original_path = os.path.abspath(__file__)
    original_data = pkgutil.get_data(to_native(__package__), original_path)

    # File (same name) in powershell/module-docs directory, used as test double
    # This file mimics this file but in the powers

# Generated at 2022-06-12 21:44:42.656591
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.common._collections_compat import MutableSequence
    from ansible.module_utils.common._collections_compat import MutableSet
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.module_utils.common._collections_compat import Set
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.psr.module_dep_finder import PSModuleDepFinder
    from ansible.module_utils.psr.module_dep_finder import _strip_comments
    import ansible.module_utils

# Generated at 2022-06-12 21:44:47.578805
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    module = AnsibleModule()
    ps_module_finder = PSModuleDepFinder()
    ps_module_finder.scan_exec_script(module.fqn)

# Utility method to get a module's PSModuleDepFinder instance

# Generated at 2022-06-12 21:44:51.637703
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    # Instantiate
    obj = PSModuleDepFinder()

    # Call method scan_exec_script with valid arguments
    obj.scan_exec_script('test_scan_exec_script')


# Generated at 2022-06-12 21:44:54.628722
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ['-m', 'test_module', 'localhost'])
    assert result.exit_code == 1



# Generated at 2022-06-12 21:45:05.972500
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Read the PowerShell module
    module_data = resource_from_fqcr("ansible.parsing.dataloader.plugins.module_utils.network.common.utils.ps1")

    ps_module_finder = PSModuleDepFinder()
    ps_module_finder.scan_module(module_data)
    assert 'Ansible.ModuleUtils.Logging.PSModuleUtils' in ps_module_finder.ps_modules
    assert 'Ansible.ModuleUtils.Network.Common.Utils' in ps_module_finder.ps_modules
    assert 'ansible_collections.ansible.parsing.plugins.module_utils.network.common.utils.ps1' not in ps_module_finder.ps_modules

    # Read a PowerShell module which imports a C# util
    module_data = resource

# Generated at 2022-06-12 21:45:10.686577
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # To test this method, we need to create a PSModuleDepFinder class object.
    psModuleDepFinder_test = PSModuleDepFinder()
    # Try to scan the file "./test_data/test_execscript.ps1"
    print("Testing scan_exec_script of class PSModuleDepFinder in scan_exec_script.py")
    psModuleTemp=[]
    psModuleDepFinder_test.scan_exec_script("test_data/test_execscript.ps1")
    for key,value in psModuleDepFinder_test.ps_modules.items():
        print("\tScanning file: %s" % key)
        print("\t\tContent: %s" % value)
        psModuleTemp.append(key)

# Generated at 2022-06-12 21:45:15.629451
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test for error condition for script exists
    ps_module_dep_finder = PSModuleDepFinder()
    name = 'name-1201935200.1646478-83584-6864987-4.ps1'
    try:
        ps_module_dep_finder.scan_exec_script(name)
    except:
        pass
    else:
        raise AssertionError("Cannot find any exception")


# Generated at 2022-06-12 21:45:38.644554
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    obj = PSModuleDepFinder()
    # Check _re_cs_module
    assert (obj.scan_module('./ansible_collections/ns/coll/plugins/module_utils/t.cs') == {'cs_utils_module': {}})

    # Check _re_cs_in_ps_module
    assert (obj.scan_module('#ansiblerequires -csharputil ansible_collections.ns.coll.plugins.module_utils.t;') == {'cs_utils_module': {}})
    assert (obj.scan_module('#ansiblerequires -csharputil ansible_collections.ns.coll.plugins.module_utils.t -Optional') == {'cs_utils_module': {}})

# Generated at 2022-06-12 21:45:49.886678
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
  with os.popen('ansible-playbook -k -i target.io/home runme.yaml -vvvv') as f:
    print(f.read())

if __name__ == "__main__":
  
  # Unit test for method scan_module of class PSModuleDepFinder
  def test_PSModuleDepFinder_scan_module():
    with os.popen('ansible-playbook -k -i target.io/home runme.yaml -vvvv') as f:
      print(f.read())


  # Unit test for class PSModuleDepFinder
  def test_PSModuleDepFinder():
    with os.popen('ansible-playbook -k -i target.io/home runme.yaml -vvvv') as f:
      print(f.read())

# Generated at 2022-06-12 21:46:00.508932
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import pkgutil
    import os

    # test the error condition
    with pytest.raises(AnsibleError) as e_info:
        finder = PSModuleDepFinder()
        finder.scan_exec_script("bad_name")
        assert e_info.value.msg == ("Could not find executor powershell script "
                                    "for 'bad_name'")

    # test the expected condition
    finder = PSModuleDepFinder()
    finder.scan_exec_script("ansible_common_executor")
    # After finder.scan_exec_script is called, the contents of
    # 'lib/ansible/executor/powershell/ansible_common_executor.ps1'
    # should be in finder.exec_scripts["ansible_common_executor"]

# Generated at 2022-06-12 21:46:01.530720
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False, "Test the method"

# Generated at 2022-06-12 21:46:10.506041
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import sys

    import pytest

    from ansible.executor.powershell.module_utils.common import to_bytes, to_native, PS_VERSION_LIST
    from ansible.module_utils.common._text import to_text

    from units.mock.path import mock_unfrackpath_noop

    from ansible.module_utils._text import to_bytes, to_text

    # scan the test dir for all modules and module-utils
    test_dir = os.path.join(os.path.dirname(__file__), "test-data", "ps")

    # We need to set these to keep the module_utils loader happy
    setattr(C, 'DEFAULT_MODULE_UTILS_PATH', [])
    setattr(C, 'DEFAULT_MODULE_PATH', [])

    # We need

# Generated at 2022-06-12 21:46:13.387318
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_util_deps_finder = PSModuleDepFinder()
    assert ps_util_deps_finder.scan_exec_script("NewManagedSchema") == None


# Generated at 2022-06-12 21:46:15.768172
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    x = PSModuleDepFinder()
    assert x.scan_exec_script('test') == None



# Generated at 2022-06-12 21:46:17.648593
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # TODO write unit test for method scan_exec_script of class PSModuleDepFinder
    pass

# Generated at 2022-06-12 21:46:23.791692
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
  finder = PSModuleDepFinder()
  finder.scan_module("using System.Web.Script.Serialization;\n")
  finder.scan_module("#Requires -Module Ansible.ModuleUtils.{name}\n")
  finder.scan_module("#AnsibleRequires -PowerShell Ansible.ModuleUtils.{name}\n")
  finder.scan_module("#AnsibleRequires -CSharpUtil Ansible.{name}\n")
  finder.scan_module("#AnsibleRequires -Wrapper serializers\n")

# Generated at 2022-06-12 21:46:34.869048
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import tempfile
    import shutil
    import ansible
    import ansible.collection
    import ansible.collection.loader

    collections_path = tempfile.mkdtemp()

    # Create a collection with a random name
    namespace = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8))
    collection_name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8))
    collection_dir = os.path.join(collections_path, namespace, collection_name)
    os.makedirs(collection_dir)

    # Create a module in the collection

# Generated at 2022-06-12 21:47:05.550813
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Initialize the class object
    test_exec_script = PSModuleDepFinder()
    
    # Test scan_exec_script with a valid name
    test_exec_script.scan_exec_script("ansible_powershell_common")
    assert test_exec_script.exec_scripts["ansible_powershell_common"] is not None

    # Test scan_exec_script with an invalid name
    try:
        test_exec_script.scan_exec_script("ansible_powershell_common_2")
    except AnsibleError as e:
        assert "Could not find executor powershell script for" in to_text(e)


# Generated at 2022-06-12 21:47:07.533730
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mu = PSModuleDepFinder()
    mu.scan_exec_script('script')
    assert mu.be == False


# Generated at 2022-06-12 21:47:13.571721
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psModuleDepFinder_object = PSModuleDepFinder()
    
    # Test with valid data
    # Test with expected success
    assert True == psModuleDepFinder_object.scan_module(name='module', ext='.py', fqn=None, optional=False, wrapper=False)
    test_data = 'module_util.py'
    
    try:
        # Test with invalid data
        # Test with unexpected success
        assert True != psModuleDepFinder_object.scan_module(name='module', ext='.py', fqn=None, optional=False, wrapper=False)
    except AssertionError as e:
        print("Exception raised for unexpected success for the test case", test_data)
        print("The exception is: ", e)

# Generated at 2022-06-12 21:47:23.291201
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Helper function to generate module_data
    def generate_module_data(
        module_util_name,
        is_csharp_in_ps_module = False,
        is_csharp_module = False,
        is_module = False,
        is_wrapper = False,
        module_util_path = None,
        ps_version = False,
        os_version = False,
        become = False):
        module_data = []
        if is_csharp_in_ps_module:
            module_data.append(
                "#AnsibleRequires -CSharpUtil {0}".format(module_util_name))
        elif is_module:
            module_data.append(
                "#Requires -Module {0}".format(module_util_name))

# Generated at 2022-06-12 21:47:32.302350
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Setup
    psmd = PSModuleDepFinder()
    psmd.cs_utils_wrapper = {'Ansible.Test.ModuleUtils.TestModuleUtil': {'path': '', 'data': b''},
                             'Ansible.ModuleUtils.Test.ModuleUtil': {'path': '', 'data': b''}}
    psmd.cs_utils_module = {'Ansible.Test.ModuleUtils.TestModuleUtil': {'path': '', 'data': b''},
                            'Ansible.ModuleUtils.Test.ModuleUtil': {'path': '', 'data': b''}}

# Generated at 2022-06-12 21:47:44.344775
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test for default case
    return_name = None
    return_ext = None
    return_name_fqn = None
    return_name_wrapper = None
    return_name_powershell = None

    def mock_add_module(self, name, ext, fqn, optional, wrapper=False):
        nonlocal return_name, return_ext, return_name_fqn, return_name_wrapper, return_name_powershell
        return_name = name
        return_ext = ext
        return_name_fqn = fqn
        return_name_wrapper = wrapper
        return_name_powershell = powershell

    def mock_scan_exec_script(self, name):
        return

    PSModuleDepFinder._add_module = mock_add_module
    PSModuleDepFinder.scan_

# Generated at 2022-06-12 21:47:46.413613
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    instance = PSModuleDepFinder()
    assert instance.scan_exec_script('posh-docker') == None


# Generated at 2022-06-12 21:47:56.606802
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.common.text.converters import mpath_to_psep

    dep_finder = PSModuleDepFinder()
    module_data = pkgutil.get_data('ansible_collections.ansible.windows.plugins.modules.psmodule', to_text(mpath_to_psep('./ansible_collections/ansible/windows/plugins/modules/psmodule.psm1')))
    dep_finder.scan_module(module_data)

    assert dep_finder.ps_version is None
    assert dep_finder.os_version is None
    assert dep_finder.become is False


# Generated at 2022-06-12 21:48:00.788024
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    result = {}
    m = PSModuleDepFinder()
    # This is an example of where someone added a script to the wrappers but failed to add it to the
    # wrappers.yml file used to generate those wrappers.
    assert m.scan_exec_script("NewRelic") == {}
    assert 'NewRelic' in m.exec_scripts



# Generated at 2022-06-12 21:48:10.862748
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    obj = PSModuleDepFinder()
    obj._add_module = MagicMock()
    obj.exec_scripts = {}
    obj.scan_exec_script('file1')
    assert(obj._add_module.call_args_list[0][0][0] == 'ansible.module_utils.powershell.basic')
    assert(obj._add_module.call_args_list[1][0][0] == 'ansible.module_utils.powershell.security')
    assert(obj._add_module.call_args_list[2][0][0] == 'ansible.module_utils.powershell.files')
    assert(obj._add_module.call_args_list[3][0][0] == 'ansible.module_utils.powershell.misc')

# Generated at 2022-06-12 21:49:09.685404
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # given
    # cwd = /home/ansible/ansible/lib/ansible/executor/powershell
    # project_dir = /home/ansible/ansible
    # name = common
    # when
    import ansible.plugins.tasks.net_put as net_put
    from ansible.module_utils._text import to_text
    import os

    os.chdir(to_text(os.path.dirname(net_put.__file__)))
    p = PSModuleDepFinder()
    p.scan_exec_script("common")
    # then
    if p.exec_scripts is not None:
        assert "common" in p.exec_scripts.keys()


# Generated at 2022-06-12 21:49:10.540461
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass



# Generated at 2022-06-12 21:49:22.764199
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()
    expected = {
        'ansible.omit.moduleutils.module_runner': {
            'data': b'module_utils data',
            'path': '',
        },
        'ansible.moduleutils.basic': {
            'data': b'module_utils data',
            'path': '',
        },
    }
    with patch.object(ps_module_utils_loader, "find_plugin", return_value="/path/to/ansible/module_utils/basic.psm1"):
        with patch.object(pkgutil, "get_data", side_effect=lambda ns, fn: b'module_utils data') as mock_data:
            finder.scan_module(data)

    assert finder.ps_modules == expected


# Generated at 2022-06-12 21:49:27.818151
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    finder.scan_exec_script(name)
    assert isinstance(finder.exec_scripts[name], bytes)


# Generated at 2022-06-12 21:49:39.166151
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    expected_result = {
        'initialize_remote_plugin': b'function initialize_remote_plugin {\n$Script:Error = $null\n'
                                    b'\n$Script:PipelineResult = $null\n'
                                    b'\n$Script:ScriptData = @{\n'
                                    b'  "rc": 0 \n'
                                    b'  "stderr": ""\n'
                                    b'  "stdout": ""\n'
                                    b'}\n}\n'
    }
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script('initialize_remote_plugin')
    assert psmdf.exec_scripts == expected_result
    assert psmdf.cs_utils_wrapper == {}
    assert psmdf.ps_modules == {}

# Generated at 2022-06-12 21:49:42.559628
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    depfinder = PSModuleDepFinder()
    name = 'TestScript'
    depfinder.scan_module(b'#Requires -Module Ansible.ModuleUtils.TestScript')
    assert name in depfinder.ps_modules.keys()



# Generated at 2022-06-12 21:49:47.716002
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
  import os
  p = PSModuleDepFinder()
  parent = os.path.dirname(os.path.abspath(__file__))
  # path to the directory containing module.psd1 ( the directory which we are trying to package )
  p.scan_exec_script('agt_winrm')
  assert p.exec_scripts['agt_winrm']



# Generated at 2022-06-12 21:49:57.816859
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import tempfile, shutil

    module_dir = os.path.dirname(os.path.abspath(__file__))
    powershell_modules_dir = os.path.join(module_dir, "..", "powershell")

    powershell_tmp_dir = os.path.join(module_dir, "..", "powershell", "tmp")
    if os.path.exists(powershell_tmp_dir):
        shutil.rmtree(powershell_tmp_dir)

    temp_module_utils_data_path = os.path.join(module_dir, "..", "powershell", "tmp", "module_utils")

    temp_module_utils_data_path_one = os.path.join(module_dir, "..", "powershell", "tmp", "module_utils", "one")

# Generated at 2022-06-12 21:50:03.475896
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    ps_module_finder = PSModuleDepFinder()
    ps_module_finder.scan_exec_script("ansible.exe_wrapper")

    print(ps_module_finder.cs_utils_wrapper.keys())
    print(ps_module_finder.ps_modules.keys())

    for k, v in ps_module_finder.exec_scripts.items():
        print("%s: %s" % (k, base64.b64encode(v).decode('ascii')))

# Generated at 2022-06-12 21:50:15.550599
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    # no assert is needed because calling scan_module raises an exception if a
    # dep is not found, so just trying to execute it without error is the test
    PSModuleDepFinder.scan_module("""\n""")

    PSModuleDepFinder.scan_module("""\n""")

    PSModuleDepFinder.scan_module("""
#AnsibleRequires -PowerShell Ansible.Windows.ModuleUtils.NetBase
    """)

    # 'Ansible.Windows.ModuleUtils.NetBase' is a builtin
    PSModuleDepFinder.scan_module("""#Requires -Module Ansible.Windows.ModuleUtils.NetBase""")

    # 'Ansible.Test.Module' is a builtin (don't need to test collection dep because it's tested below)
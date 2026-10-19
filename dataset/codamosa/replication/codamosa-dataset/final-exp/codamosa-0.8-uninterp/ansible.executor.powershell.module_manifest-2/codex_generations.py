

# Generated at 2022-06-12 21:40:58.056971
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    # Unit test to ensure the method PSModuleDepFinder.scan_exec_script always return 
    # the expected result.

    # Test input data.
    _wrapperName='/Users/ahmedzouaoui/Ansible_PS/lib/ansible/executor/powershell/wrapped.ps1'

    # Init class.
    psModuleDepFinder = PSModuleDepFinder()

    # Test execution.
    psModuleDepFinder.scan_exec_script(_wrapperName)

    # Assert expected results.
    assert psModuleDepFinder.exec_scripts=={}

# Generated at 2022-06-12 21:41:00.437186
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    with open(os.path.join(os.path.dirname(__file__), 'data/ps-module-dep-finder-fixture-1.json'), 'r') as dep_finder_fixture:
        json.loads(dep_finder_fixture.read())


# Generated at 2022-06-12 21:41:10.462200
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible import constants as C
    from ansible.plugins.loader import ps_module_utils_loader
    from ansible.module_utils.compat.importlib import import_module
    import pkgutil
    import os
    import random

    C.DEFAULT_DEBUG = True
    ext = '.cs'
    util_name = 'Ansible.CommonUtils'
    obj_module = import_module(util_name)
    data = pkgutil.get_data(util_name, to_native(util_name + ext), obj_module.__loader__)
    if data is not None:
        data = to_bytes(data)
    else:
        raise AnsibleError("Could not find imported module support code "
                           "for \'%s\'" % util_name)

    name = 'test'
   

# Generated at 2022-06-12 21:41:21.124174
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    collection_id = 'ansible_collections.my_namespace.my_collection'
    fqm = '%s.plugins.modules.my_module' % collection_id
    class_under_test = PSModuleDepFinder()
    class_under_test.scan_exec_script('my_module')
    assert class_under_test.exec_scripts[collection_id]['data'] == to_bytes(_slurp(resource_from_fqcr(fqm, 'exec_wrapper.ps1')))
    #assert len(class_under_test.<your argument>.keys()) > 0
    assert len(class_under_test.exec_scripts.keys()) == 1


# Generated at 2022-06-12 21:41:34.655802
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils import common_argparser
    from ansible.module_utils import basic
    from ansible.module_utils import six
    from ansible.module_utils import json_dict
    from ansible.module_utils import basic
    from ansible.module_utils import common_err
    psmdf = PSModuleDepFinder()

    psmdf.scan_exec_script("common_argparser")
    assert psmdf.exec_scripts["common_argparser"]
    assert psmdf.ps_modules["Ansible.ModuleUtils.Basic"]
    assert psmdf.ps_modules["Ansible.ModuleUtils.CommonErr"]
    psmdf.scan_exec_script("basic")
    assert psmdf.exec_scripts["basic"]

# Generated at 2022-06-12 21:41:35.154827
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:41:35.783315
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass



# Generated at 2022-06-12 21:41:44.661049
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # This is a unit test for method scan_module of class PSModuleDepFinder
    # It tests the ps_modules, cs_utils_module, exec_scripts, ps_version, os_version, become attributes of the returned object.
    module_obj = PSModuleDepFinder()
    data = pkgutil.get_data("ansible.plugins.modules", to_native("win_ping" + ".psm1"))
    module_obj.scan_module(b_data=data, fqn=None, wrapper=False, powershell=True)
    assert "Ansible.ModuleUtils.Common.AnsibleModuleUtils" in module_obj.ps_modules.keys()
    assert "ansible_collections.ns1.coll1.plugins.module_utils.csharp_util" in module_obj.cs_utils_module

# Generated at 2022-06-12 21:41:52.818014
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    test_obj=PSModuleDepFinder()
    assert test_obj.ps_modules == dict()
    assert test_obj.exec_scripts == dict()
    assert test_obj.cs_utils_wrapper == dict()
    assert test_obj.cs_utils_module == dict()
    assert test_obj.ps_version is  None
    assert test_obj.os_version is None
    assert test_obj.become == False
    assert test_obj._re_cs_module == [re.compile(b'(?i)^using\\s((Ansible\\..+)|'
                                b'(ansible_collections\\.\\w+\\.\\w+\\.plugins\\.module_utils\\.[\\w\\.]+));\\s*$')]
    assert test_obj._re_cs_in_ps_

# Generated at 2022-06-12 21:42:01.790419
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmd_scan_exec_script = PSModuleDepFinder.scan_exec_script
    psmd_scan_module = PSModuleDepFinder.scan_module

    script_name = "Test-Script"

    # Create temp file for the script that is being tested
    tmpfile = tempfile.NamedTemporaryFile(delete=False)
    tmpfile.close()
    exec_script = "echo 'test'\n"\
        "#AnsibleRequires -CSharpUtil Ansible.X"

    with open(tmpfile.name, 'w') as f:
        f.write(exec_script)

    # Create and setup PSModuleDepFinder
    finder = PSModuleDepFinder()
    finder.exec_scripts = dict()

    # Test with valid file

# Generated at 2022-06-12 21:42:26.179172
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test to ensure that a playbook can be loaded
    # Generated by Ansible's ansible-test module_utils.loader --explain
    # Unit test for method scan_exec_script of class PSModuleDepFinder
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


# Generated at 2022-06-12 21:42:37.792280
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    FileSystemLoader = resource_from_fqcr('ansible.executor:FileSystemLoader')

    class TestModule(object):
        def __init__(self, path, args, become_method=None, become_user=None):
            self.args = args
            self.path = path
            self.become_method = become_method
            self.become_user = become_user
            self.no_log = False
            self.check_mode = False
            self.remote_tmp = tempfile.gettempdir()
            self.warnings = []
            self.deprecations = []

        def fail_json(self, **kwargs):
            raise Exception("module failure")

        def exit_json(self, **kwargs):
            return


# Generated at 2022-06-12 21:42:42.020212
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    p = PSModuleDepFinder()
    module_data = [
        "#Requires -Module Ansible.ModuleUtils.Another",
        "#AnsibleRequires -Powershell Ansible.ModuleUtils.Another"
    ]
    assert p.scan_module("\n".join(module_data)) is None


# Generated at 2022-06-12 21:42:48.635586
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    depfinder = PSModuleDepFinder()

# Generated at 2022-06-12 21:43:01.426116
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    
    expected_data = b'# this is a comment\n\ntest\n# this is another comment\n'
    module_data = b'# this is a comment\n\ntest\n# this is another comment\n'
    
    pkg_data = {
        "name": "test",
        "data": expected_data
    }
    # run test
    test_PSModuleDepFinder = PSModuleDepFinder()
    test_PSModuleDepFinder.scan_exec_script(pkg_data["name"])

    # Check if content of the executor powershell script matches with data stored in 
    # self.exec_scripts["test"]
    assert to_text(test_PSModuleDepFinder.exec_scripts[pkg_data["name"]]) == to_text(expected_data)
    # Check

# Generated at 2022-06-12 21:43:11.886023
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test that scanning a ps module finds the correct module_utils specified
    # by '#AnsibleRequires -PowerShell Ansible.ModuleUtils.ModuleUtilName'
    test_ps_module = to_bytes(pkgutil.get_data("ansible_test.unit.module_utils.module_utils_loader",
                                               "test_module_util.psm1"))
    ps_module_finder = PSModuleDepFinder()
    ps_module_finder.scan_module(test_ps_module, fqn="ansible_test.unit.module_utils.module_utils_loader.test_module_util", powershell=True)
    assert len(ps_module_finder.ps_modules.keys()) == 1

# Generated at 2022-06-12 21:43:17.197846
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:43:18.181504
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print("Testing scan_exec_script")
    assert True

# Generated at 2022-06-12 21:43:28.650701
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    # Test that regular module without dependencies works
    finder = PSModuleDepFinder()
    raw_module = '''
{
    "module_name": "win_ping",
    "module_args": {
        "_ansible_no_log": false,
        "_ansible_verbosity": 0,
        "a": true,
        "arg": "hello world"
    }
}
'''
    finder.scan_module(base64.b64encode(raw_module), powershell=True)
    assert len(finder.ps_modules) == 0

    # Test that powershell module with builtin and collection module utils is found
    finder = PSModuleDepFinder()

# Generated at 2022-06-12 21:43:34.292336
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psdeps = PSModuleDepFinder()

    psdeps.scan_exec_script("AddToPathForAnsibleModules")

    assert b"AddToPathForAnsibleModules.ps1" in psdeps.exec_scripts
    assert len(psdeps.exec_scripts) == 1
    assert len(psdeps.ps_modules) >= 2 # because validation of the exec scripts is not mocked out


# Generated at 2022-06-12 21:44:27.886050
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()
    module_utils = set()
    fqn = "nxos.nxos.nxos_facts"
    module_utils_name = "Ansible.Nxos.Common"
    module_utils.add((module_utils_name, None, fqn, False))
    for m in set(module_utils):
        finder._add_module(*m, wrapper=False)
    assert finder.ps_modules is not None
    assert finder.ps_modules[module_utils_name] is not None



# Generated at 2022-06-12 21:44:29.501072
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # TODO: Write unit test.
    pass

# Generated at 2022-06-12 21:44:34.077743
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    args = dict(
        module_data=b'',
        fqn=None,
        wrapper=False,
        powershell=True)
    obj = PSModuleDepFinder()
    obj.scan_module(**args)

# Generated at 2022-06-12 21:44:34.920340
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass

# Generated at 2022-06-12 21:44:37.747292
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_obj = PSModuleDepFinder()
    assert(test_obj.scan_exec_script("init") == None)

# Generated at 2022-06-12 21:44:47.134056
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.common.text.formatters import to_bytes
    from ansible.module_utils.ansible_release import __version__ as version

    formatter = to_bytes("ansible_%s_payload")
    payload_name = formatter % version

    def get_data(path):
        return """
        #AnsibleRequires -Wrapper '{0}'
        $AnsiblePayload = @"
        {payload}
        "@
        """.format(payload_name, payload="x" * 10)

    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script(payload_name)

    assert ps_module_

# Generated at 2022-06-12 21:44:49.226180
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True


# Generated at 2022-06-12 21:44:49.672288
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass



# Generated at 2022-06-12 21:45:00.271339
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    scanner = PSModuleDepFinder()
    exec_script_mock_path = "psrp_get_session_mock"
    with open("test/units/module_utils/cloud/azure/azure_rm_common/tests/test_scanner/"+exec_script_mock_path+".ps1", "r") as f:
        content = f.read()
        scanner.scan_module(content, wrapper=True, powershell=True)


# Generated at 2022-06-12 21:45:11.119851
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    def _test_it(name, expected_value):
        "Unit test for method scan_exec_script of class PSModuleDepFinder"
        dep_finder = PSModuleDepFinder()
        dep_finder.scan_exec_script(name)
        assert dep_finder.exec_scripts.get(name, None) is not None
        assert dep_finder.exec_scripts[name].decode('utf-8') == expected_value
        assert len(dep_finder.cs_utils_wrapper) == 1
        assert dep_finder.cs_utils_wrapper['Ansible.ConvertToJson']['path'] == 'ansible/module_utils/powershell/ConvertToJson.cs'

# Generated at 2022-06-12 21:45:57.311064
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # initializing argument in some random order
    arg_dict = {}
    for _ in range(random.randint(2, 9)):
        arg_dict[random.choice([ 'fqn', 'module_data'])] = random.choice([random.randint(1, 9), random.randint(1, 100), random.randint(1, 1000), random.randint(1, 10000)])
    try:
        # creating instance
        instance = PSModuleDepFinder()
        # calling method to test out
        method_result = instance.scan_module(**arg_dict)
        assert True
    except AssertionError as err:
        print(err)

# Generated at 2022-06-12 21:45:59.667870
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    assert finder.scan_exec_script("ansible_powershell_wrapped") == None



# Generated at 2022-06-12 21:46:03.486380
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    p = PSModuleDepFinder()
    with pytest.raises(AnsibleError) as exec_info:
        p.scan_exec_script('does_not_exist')
    assert 'Could not find executor powershell script for \'does_not_exist\'' in to_native(exec_info.value)



# Generated at 2022-06-12 21:46:05.910226
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    return dep_finder.scan_exec_script("Common")


# Generated at 2022-06-12 21:46:08.583295
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_PSModuleDepFinder = PSModuleDepFinder()
    
    name = 'WindowsFeature'
    test_PSModuleDepFinder.scan_exec_script(name)



# Generated at 2022-06-12 21:46:11.278405
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    instance = PSModuleDepFinder()
    name = instance.scan_exec_script(name)
    assert True


# Generated at 2022-06-12 21:46:11.879573
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:46:22.023402
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    # Test the case when name is not present in self.exec_scripts.keys()
    # and data is not None and _strip_comments is called.
    module_util_class = PSModuleDepFinder()
    module_util_class.scan_module = MagicMock()
    module_util_class.exec_scripts = {}
    module_util_class.exec_scripts = {'a': 'test'}
    C.DEFAULT_DEBUG = False
    new_data = b'#test\n\n#test\n'
    pkgutil.get_data = MagicMock(return_value=new_data)
    _strip_comments = MagicMock(return_value=new_data)
    module_util_class.scan_exec_script(name='a')
    assert _strip_comments.called

    # Test

# Generated at 2022-06-12 21:46:32.936129
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    result = PSModuleDepFinder()
    p = os.path.join(os.path.dirname(__file__), '..', '..', 'test', 'support', 'test_module.psm1')
    result.scan_module(_slurp(p), fqn='test.test_module.test_module')
    assert len(result.ps_modules) == 0
    assert len(result.cs_utils_wrapper) == 0
    assert len(result.cs_utils_module) == 1
    assert result.cs_utils_module['ansible_collections.ns.coll.plugins.module_utils.test.test']['data'].startswith(b'using System;\n')

# Generated at 2022-06-12 21:46:38.262104
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    print(pkgutil.get_data("ansible.executor.powershell", "basic.ps1"))
    psmdf.scan_exec_script('basic')
    print(psmdf.ps_modules)
    print(psmdf.exec_scripts)
    print(psmdf.cs_utils_wrapper)
    print(psmdf.cs_utils_module)

# Generated at 2022-06-12 21:48:02.202563
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:48:03.144716
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    assert True

# Generated at 2022-06-12 21:48:04.860946
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    obj = PSModuleDepFinder()
    # pass


# Generated at 2022-06-12 21:48:14.252347
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:48:21.654593
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Generate a bunch of random data for the test
    rand = random.Random()
    
    # Generate a random string from a list of allowable characters
    def rand_str():
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        length = rand.randint(1, 32)
        return ''.join(rand.choice(chars) for i in range(length))
    
    # Generate a random integer from a range
    def rand_int(start, end):
        return rand.randint(start, end)
    
    # Generate a random float from a range
    def rand_float(start, end):
        return float(rand_int(start, end)) + rand.random()
    
   

# Generated at 2022-06-12 21:48:29.356004
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test Case #1: scan exec script
    test_exec_script_name = "t_" + "%x" % random.getrandbits(16 * 8)
    test_exec_script_path = os.path.join(C.DEFAULT_MODULE_UTILS_PATH,
                                         "powershell",
                                         test_exec_script_name + ".ps1")
    with open(test_exec_script_path, "w") as f:
        f.write("""
            #AnsibleRequires -CSharpUtil ansible_collections.ns.coll.plugins.module_utils.cs_util
            """)

    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script(test_exec_script_name)


# Generated at 2022-06-12 21:48:41.116604
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # setup
    psmdf = PSModuleDepFinder()


# Generated at 2022-06-12 21:48:49.354637
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()
    finder.scan_module(b'#Requires -Module ansible_collections.test.test.plugins.module_utils.test1')
    assert finder.cs_utils_module == {'ansible_collections.test.test.plugins.module_utils.test1': {'data': b'',
                                                                                                    'path': 'test.cs'}}
    finder.scan_module(b'using Test.test;')
    assert finder.cs_utils_module == {'ansible_collections.test.test.plugins.module_utils.test1': {'data': b'',
                                                                                                    'path': 'test.cs'}}

# Generated at 2022-06-12 21:48:59.200207
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    # the code below is the code from the test_ps_module_utils_loader unit test
    # which tests the full flow of finding and scanning a .psm1 file. I am
    # copying the code over here because I want to test the behavior with a
    # new_module_feature that does not exist in the main plugin loader tests
    # for PS modules.
    #
    # To see the full test (basically the entire loader process) see
    # test/units/plugins/test_ps_module_utils_loader.py

    data = b"#Requires -Module Ansible.ModuleUtils.Service"
    # this is a module that does not exist but we're testing the behavior
    # here, not the actual module name
    fake_mu = "Ansible.ModuleUtils.POSH.Platform.Windows"
    # add some data so

# Generated at 2022-06-12 21:49:02.963764
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("ansible_module_exec")
    assert finder.exec_scripts
    assert finder.ps_modules
    assert finder.cs_utils_wrapper

# Unit test method _parse_version_match of class PSModuleDepFinder
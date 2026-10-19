

# Generated at 2022-06-12 21:41:10.595247
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()
    module_data = b'#Requires -Module Ansible.ModuleUtils.Foo\n#Requires -Module Ansible.ModuleUtils.Bar'
    finder.scan_module(module_data)
    assert len(finder.ps_modules) == 2

    module_data = b'using Ansible.ModuleUtils.Foo;using Ansible.ModuleUtils.Bar;'
    finder.scan_module(module_data)
    assert len(finder.cs_utils_module) == 2

    module_data = b'#Requires -Module Ansible.ModuleUtils.Foo\n#AnsibleRequires -CSharpUtil Ansible.ModuleUtils.Bar'
    finder.scan_module(module_data)
    assert len(finder.ps_modules) == 2


# Generated at 2022-06-12 21:41:15.626081
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Verify a successful use case is handled correctly
    finder = PSModuleDepFinder()
    finder.scan_exec_script('win_package')
    assert finder.exec_scripts.get('win_package') is not None
    assert b'# AnsibleRequires -Powershell' in finder.exec_scripts['win_package']
    assert finder.ps_modules.get('Ansible.ModuleUtils.LegacyWindows') is not None
    assert b'#Author: John Westcott IV' in finder.ps_modules['Ansible.ModuleUtils.LegacyWindows']['data']
    assert finder.ps_modules.get('Ansible.ModuleUtils.PSModuleLoader') is not None

# Generated at 2022-06-12 21:41:28.774039
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('wrapper.ps1')

# Generated at 2022-06-12 21:41:30.624344
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:41:41.286800
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """Unit test for method scan_exec_script of class PSModuleDepFinder
    """

    import random

    random_seed = random.getrandbits(32)
    print("Random Seed: %s" % random_seed)
    random.seed(random_seed)

    try:
        from six import StringIO
    except ImportError:
        from io import StringIO

    from ansible.executor.powershell.module_utils import find_exec_template
    from ansible.module_utils import powershell

    template_name = random.choice(powershell.TEMPLATES)

    # paths here are what they are in the PS dir when built.
    # this is really only set up for local testing.
    template_path = find_exec_template(template_name)

# Generated at 2022-06-12 21:41:42.367747
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass



# Generated at 2022-06-12 21:41:51.039200
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from test.units.module_utils.power_shell import PsInventory

    def mock_get_data(module_name, data_file_name):
        # Determine if the exec script that needs to be mocked is in the test_data directory
        exec_script_path = os.path.join(os.path.dirname(__file__), "test_data", data_file_name)
        # If the exec script is in the test_data directory, return it's data
        # Otherwise the exec scripts are coming from the regular ansible package
        if os.path.isfile(exec_script_path):
            with open(exec_script_path, "rb") as f:
                return f.read()

        return pkgutil.get_data(module_name, data_file_name)


# Generated at 2022-06-12 21:42:00.758248
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import pytest
    from ansible.plugins.loader import ps_module_utils_loader
    from ansible.module_utils._text import to_bytes, to_native, to_text
    from ansible.utils.collection_loader import resource_from_fqcr

    # used to simulate an error as part of the unit test
    class FakeAnsibleError(Exception):
        pass


# Generated at 2022-06-12 21:42:06.234475
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    sample_module_data = """
#Requires -Module Ansible.ModuleUtils.Windows
#Requires -Module Ansible.ModuleUtils.Legacy
#AnsibleRequires -Powershell Ansible.ModuleUtils.Backport
#AnsibleRequires -CSharpUtil Ansible.Windows.Config


using System;
using System.Collections.Generic;
using System.Management.Automation;

using ansible_collections.foo.bar.plugins.module_utils.win_fad_ad_util;
using ansible_collections.foo.bar.plugins.module_utils.win_fad_ad_util.ADHelper;
"""
    expected_set = set()
    expected_set.add(("Ansible.ModuleUtils.Windows", ".psm1", None, False))

# Generated at 2022-06-12 21:42:07.590788
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    module = PSModuleDepFinder()
    module.scan_exec_script("1")
    module.scan_exec_script("2")


# Generated at 2022-06-12 21:42:26.895037
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    tester = PSModuleDepFinder()

    tester.scan_module(b'')
    assert tester.ps_modules == {}
    assert tester.cs_utils_wrapper == {}
    assert tester.cs_utils_module == {}
    assert tester.ps_version is None
    assert tester.os_version is None
    assert tester.become is False

    # PS version requirement
    tester.scan_module(b'#requires -version 5.1')
    assert tester.ps_version == '5.1.0'

    # PS version requirement with double decimal
    tester.scan_module(b'#requires -version 2.0.1')
    assert tester.ps_version == '2.0.1'

    # OS version requirement

# Generated at 2022-06-12 21:42:28.274123
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    assert True == False, "Test Case not implemented"

# Generated at 2022-06-12 21:42:31.476927
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("windows_common")
    assert len(dep_finder.exec_scripts) == 1
    assert len(dep_finder.ps_modules) == 1



# Generated at 2022-06-12 21:42:40.988883
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("test_check_for_powershell.ps1")
    if dep_finder.exec_scripts.get("test_check_for_powershell.ps1") == None:
        raise AssertionError("exec_scripts should contain test_check_for_powershell.ps1")
    if dep_finder.ps_modules.get("Ansible.ModuleUtils.ArgumentSpec") == None:
        raise AssertionError("ps_modules should contain Ansible.ModuleUtils.ArgumentSpec")

# Generated at 2022-06-12 21:42:48.676763
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # GIVEN
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.become = False
    ps_module_dep_finder.os_version = None
    ps_module_dep_finder.ps_version = None
    ps_module_dep_finder.cs_utils_wrapper = {}
    ps_module_dep_finder.cs_utils_module = {}
    ps_module_dep_finder.ps_modules = {}
    ps_module_dep_finder.exec_scripts = {}
    fqn = None
    wrapper = False
    powershell = True

# Generated at 2022-06-12 21:42:51.068271
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mdf = PSModuleDepFinder()
    mdf.scan_exec_script('scriptname')



# Generated at 2022-06-12 21:43:03.450780
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    ps_module = r'''#Requires -Module Ansible.ModuleUtils.foo,
    #Requires -Module Ansible.ModuleUtils.bar
    #Requires -Module Ansible.ModuleUtils.bar2
    #AnsibleRequires -PowerShell Ansible.ModuleUtils.foo2
    #AnsibleRequires -PowerShell Ansible.ModuleUtils.foo3
    #AnsibleRequires -CSharpUtil Ansible.Foo
    #AnsibleRequires -CSharpUtil ansible_collections.namespace.coll.plugins.module_utils.foo2
    #AnsibleRequires -CSharpUtil ..module_utils.foo3
    '''

    finder = PSModuleDepFinder()
    finder.scan_module(to_bytes(ps_module))
    # assert that scan_module method has correct results

# Generated at 2022-06-12 21:43:06.136657
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_obj = PSModuleDepFinder()
    assert test_obj.scan_exec_script('win_ping') == None


# Generated at 2022-06-12 21:43:07.275015
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("win_ping")



# Generated at 2022-06-12 21:43:08.316646
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:43:28.650504
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible_collections.testns.testcoll.plugins.module_utils.test_utils import (
        TestUtils,
    )
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
        load_provider,
    )
    TestCollectionUtils = TestUtils()
    provider_utils = load_provider()
    NetworkCommonUtils = provider_utils['parent']
    BaseUtils = provider_utils['base']
    NetworkCommonModuleUtils = provider_utils['module_utils']['common']
    CommonModuleUtils = provider_utils['common']

    # Test the scan_module method of class PSModuleDepFinder
    psdepfinder = PSModuleDepFinder()

    path = os.path.join('test_utils.psm1')


# Generated at 2022-06-12 21:43:29.390752
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True



# Generated at 2022-06-12 21:43:40.963255
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.powershell.base import AnsibleModule, win_dism_version, win_psmodulepath

    psmodule_path = win_psmodulepath()

    # Test using a builtin module_util
    psmodule_data = to_bytes(_slurp(os.path.join(psmodule_path, "Ansible.ModuleUtils.WinSystem.psm1")))

    dep_finder = PSModuleDepFinder()
    dep_finder.scan_module(psmodule_data)

    # Test using a collection module_util
    # ansible.windows.win_dism was chosen because it uses a collection module_util
    # and that module_util uses a builtin module_util

# Generated at 2022-06-12 21:43:46.426264
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    random_number = random.randint(1000,9999)
    psmdf.scan_exec_script(to_text(random_number))
    assert len(psmdf.exec_scripts.keys()) == 1
    assert to_native(random_number) in psmdf.exec_scripts.keys()


# Generated at 2022-06-12 21:43:50.282068
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """Tests for PSModuleDepFinder.scan_exec_script"""

    finder = PSModuleDepFinder()
    finder.scan_exec_script("TestScript")
    assert finder.exec_scripts.get('TestScript') is not None


# Generated at 2022-06-12 21:43:51.391035
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True


# Generated at 2022-06-12 21:43:55.529452
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Create the test instance of AnsibleModule
    stderr = """Traceback (most recent call last):
File "test_resource.py", line 2, in <module>
  test_ansible_module(name='test', arg='spam')
File "test_ansible_module.py", line 9, in test_ansible_module
  raise ValueError('This is only a test.')
ValueError: This is only a test.
"""

    stdout = "Eggs"

    ansible_module = AnsibleModule(
        argument_spec=dict(
            foo={'type': 'str', 'default': 'bar'},
            name={'type': 'path'}
        )
    )
    ansible_module.params['name'] = 'test'

# Generated at 2022-06-12 21:44:06.662058
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # This test will use a pseudo-module_utils file in a known location that is not
    # in the expected module_utils path of ansible modules, to make sure we are
    # finding the module_utils in the right place.
    sample_wrapper_path = os.path.join(C.DEFAULT_MODULE_UTILS_PATH, 'test_module_utils_scan_exec_script.ps1')
    sample_wrapper = b'#AnsibleRequires -CSharpUtil test_module_utils_scan_exec_script.cs'
    with open(sample_wrapper_path, 'w+b') as f:
        f.write(sample_wrapper)


# Generated at 2022-06-12 21:44:14.003899
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_module(b"#ansibledepends on here", powershell=True)
    dep_finder.scan_exec_script("another")
    assert dep_finder.exec_scripts["another"] == b"#ansibledepends on here"
    assert dep_finder.ps_modules
    assert dep_finder.cs_utils_wrapper
    assert dep_finder.cs_utils_module
    assert dep_finder.ps_version is None
    assert dep_finder.os_version is None
    assert dep_finder.become is False


# Generated at 2022-06-12 21:44:27.663927
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import imp
    import sys
    import os

    MODULE_NAME = 'ansible.executor.powershell'
    MODULE_PATH = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, os.pardir, 'executor', 'powershell')
    MODULE_FILE = '__init__.py'

    if MODULE_NAME in sys.modules:
        del sys.modules[MODULE_NAME]

    if not os.path.exists(os.path.join(MODULE_PATH, MODULE_FILE)):
        raise Exception("Couldn't load module %s. File %s does not exist" % (MODULE_NAME, os.path.join(MODULE_PATH, MODULE_FILE)))


# Generated at 2022-06-12 21:44:46.272073
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.utils.hashing import checksum
    from ansible.module_utils._text import to_text
    finder = PSModuleDepFinder()
    finder._add_module = MagicMock()
    finder.scan_exec_script('win_command')

    assert len(finder.exec_scripts) == 1
    assert finder.exec_scripts.get('win_command') is not None
    assert checksum(finder.exec_scripts.get('win_command')) == 742598337

    assert finder._add_module.called
    assert finder._add_module.call_count == 1
    assert finder._add_module.call_args[0][0] == 'Ansible.ModuleUtils.AnsibleModule'

# Generated at 2022-06-12 21:44:57.675612
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    def find_module_util(name):
        return True

    ps_mdf = PSModuleDepFinder()
    ps_mdf._add_module = find_module_util
    ps_mdf.scan_module = scan_module
    script_name = 'test_powershell_plugin'
    ps_mdf.scan_exec_script(script_name)

    with open(os.path.join(C.DEFAULT_LOCAL_TMP, '%s.ps1' % script_name), 'rb') as ps_script:
        ps_script_data = ps_script.readlines()

    assert ps_mdf.exec_scripts[script_name].decode('utf-8') == b'\n'.join(ps_script_data).decode('utf-8')
    assert ps_mdf.ps_

# Generated at 2022-06-12 21:45:03.641795
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # This is a trivial test to check the method scan_exec_script works.
    obj = PSModuleDepFinder()
    with pytest.raises(AnsibleError) as exec_info:
        obj.scan_exec_script('bogus')

    assert 'Could not find executor powershell script for \'bogus\'' in to_native(exec_info.value)

# Generated at 2022-06-12 21:45:13.980543
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_data = "test_data"

    def import_module(package_name, resource_name):
        assert package_name == "ansible.executor.powershell"
        assert resource_name == to_text("TestScript.ps1")
        return test_data

    # Mock the import_module method to avoid importing the whole ansible module.
    old_import_module = import_module
    import_module = import_module

# Generated at 2022-06-12 21:45:24.750960
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """
    ps_module_deps_finder.scan_exec_script validates the dependency scanning of the executor powershell scripts
    """

    test_cases = [
        ("archive", True),
        ("_lint_wrapper", True),
        ("_psrp_wrapper", True),
        ("_winrm_wrapper", True),
        ("_winrs_wrapper", True),
        ("my_script", False)
    ]

    for test_case in test_cases:
        finder = PSModuleDepFinder()
        if test_case[1]:
            try:
                finder.scan_exec_script(test_case[0])
            except AnsibleError:
                assert False

# Generated at 2022-06-12 21:45:33.329157
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mu_name = "Ansible.Sample"
    ps_path = ps_module_utils_loader.find_plugin(mu_name, ".psm1")
    mu_data = to_bytes(_slurp(ps_path))

    ps_finder = PSModuleDepFinder()
    ps_finder._add_module(mu_name, ".psm1", "", False, wrapper=False)

    assert ps_finder.ps_modules[mu_name]['data'] == mu_data
    assert ps_finder.ps_modules[mu_name]['path'] == to_text(ps_path)


# Generated at 2022-06-12 21:45:34.365285
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:45:42.814261
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import unittest
    test_env = os.path.basename(__file__).split('.')[0]
    data_dir = os.path.join(os.getcwd(), "data", test_env)
    module_name = "ping.psm1"

    # Find module_util and module_utils.basic
    loader = PSModuleDepFinder()
    data = _slurp(os.path.join(data_dir, module_name))
    loader.scan_module(data)
    assert loader.ps_modules["Ansible.ModuleUtils.basic"]["data"]
    assert loader.ps_modules["Ansible.ModuleUtils.basic"]["path"]

    # Find module_util and module_utils.connection
    module_name = "copy.psm1"
    data = _

# Generated at 2022-06-12 21:45:45.828350
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    module_dep_finder = PSModuleDepFinder()
    module_dep_finder.scan_exec_script("basic")


# Generated at 2022-06-12 21:45:46.845650
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
  assert False # TODO



# Generated at 2022-06-12 21:46:13.675616
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    from ansible.executor.powershell import ModuleExecutor
    import ansible.executor.powershell

    instance = PSModuleDepFinder()

    assert instance.exec_scripts == dict()

    with open("/tmp/module", "w") as f:
        f.write("#ansiblerequires -wrapper ModuleExecutorWrapper")

    with open("/tmp/ModuleExecutorWrapper.ps1", "w") as f:
        f.write("#requires -version 6.0")

    with open("/tmp/ModuleExecutorGenerator.ps1", "w") as f:
        f.write("#ansiblerequires -powershell Ansible.ModuleUtils.Test1")

    instance.scan_exec_script("ModuleExecutorWrapper")

    assert "ModuleExecutorWrapper" in instance.exec_scripts.keys()


# Generated at 2022-06-12 21:46:23.219906
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    data = pkgutil.get_data("ansible.executor.powershell", "main.ps1")
    if data is None:
        raise AnsibleError("Could not find executor powershell script for '%s'" % name)

    b_data = to_bytes(data)
    # remove comments to reduce the payload size in the exec wrappers
    if C.DEFAULT_DEBUG:
        exec_script = b_data
    else:
        exec_script = _strip_comments(b_data)
    #self.exec_scripts[name] = to_bytes(exec_script)
    #self.scan_module(b_data, wrapper=True, powershell=True)
    finder_obj = PSModuleDepFinder()

# Generated at 2022-06-12 21:46:31.543939
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible_test_utils.test_metrics import TestMetrics
    from ansible_test_utils.test_module_loader import TestModuleLoader

    fixture = TestModuleLoader.get_fixture('exec_script.ps1')
    with TestMetrics('test_PSModuleDepFinder_scan_exec_script'):
        f = PSModuleDepFinder()
        test_name = 'my_test_exec_script'
        f.scan_exec_script(test_name)
        assert f.exec_scripts[test_name].decode() == fixture.decode()

# Generated at 2022-06-12 21:46:32.926471
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # TODO: Implement test
    pass



# Generated at 2022-06-12 21:46:35.970258
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("noise_collector")


# Generated at 2022-06-12 21:46:46.051421
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class StubRunner(object):
        def __init__(self):
            self.path = "/tmp/stub"
            self.remote_user = "root"
            self.become = False
            self.become_user = ""
            self.become_method = ""
            self.become_flags = ""
            self.become_exe = ""
            self.no_log = False
            self.strip_prompt_regex = ""
            self.environment_variables = []
            self.passwords = []
            self.tempdir = "/tmp/stub"
            self.transport = ""
            self.connection_channel = ""
            self.executor_preserve_whitespace = True
            self.vault_password = ""
            self.runas_password = ""

# Generated at 2022-06-12 21:46:58.097294
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    obj = PSModuleDepFinder()

    obj._add_module = MagicMock()
    obj.scan_module('Ansible.ModuleUtils.Prod.ModuleA', fqn='', wrapper=False, powershell=True)
    obj._add_module.assert_called_once_with('Ansible.ModuleUtils.Prod.ModuleA',
                                            '.psm1', '', False)
    obj._add_module.reset_mock()

    obj.scan_module('..ModuleUtils.Prod.ModuleB', fqn='Ansible.ModuleUtils.Prod',
                    wrapper=False, powershell=True)

# Generated at 2022-06-12 21:47:08.057130
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # setup
    b_data = to_bytes(
        '''#Example comment
        #contains a non-comment, non-matching line
        #Requires -Module Ansible.ModuleUtils.SecondModUtil
        #AnsibleRequires -CSharpUtil Ansible.Foo.Bar;
        #AnsibleRequires -Wrapper Foo
        #AnsibleRequires -PowerShell Ansible.ModuleUtils.ThirdModUtil -Optional
        #AnsibleRequires -PowerShell ansible_collections.ns.coll.plugins.module_utils.FourthModUtil -Optional
        other
        #Example comment
        '''
    )
    pdmf = PSModuleDepFinder()

    # act
    pdmf.scan_module(b_data, wrapper=True)

    # assert
    assert pdmf.ps

# Generated at 2022-06-12 21:47:16.419530
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.executor.powershell import _strip_comments
    import tempfile
    import shutil
    import pkg_resources

    tmpdir = tempfile.mkdtemp()
    executor_dir = os.path.join(tmpdir, 'ansible', 'executor', 'powershell')
    os.makedirs(executor_dir)

    # Inject fake executor files
    executor_files = [
        os.path.join(executor_dir, 'connection_winrm.ps1'),
        os.path.join(executor_dir, 'module_json.ps1'),
    ]
    for f in executor_files:
        with open(f, 'w') as fd:
            fd.write('#Requires -Module Ansible.ModuleUtils.foo\n')

# Generated at 2022-06-12 21:47:25.272396
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:48:10.228603
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script('WinRM')
    assert psmdf.exec_scripts['WinRM'].startswith(to_bytes('# ANSIBLE MANAGED BLOCK'))
    assert 'Ansible.ModuleUtils.Powershell.Convert' in psmdf.exec_scripts['WinRM']


# Generated at 2022-06-12 21:48:11.268390
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass



# Generated at 2022-06-12 21:48:17.431124
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    with open(os.path.join(os.path.dirname(__file__), 'data/powershell_exec_script.ps1'), 'r') as f:
        powershell_exec_script = f.read()
    finder = PSModuleDepFinder()
    finder.scan_exec_script('my_script')
    assert finder.exec_scripts['my_script'] == powershell_exec_script.encode('utf-8')

# Generated at 2022-06-12 21:48:26.309543
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    fail_test = False
    fail_reason = ""

# Generated at 2022-06-12 21:48:27.168308
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True


# Generated at 2022-06-12 21:48:38.828460
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    dep_finder = PSModuleDepFinder()

    dep_finder.scan_exec_script('Basic')
    dep_finder.scan_exec_script('Process')

    assert len(dep_finder.cs_utils_wrapper) == 5
    assert 'Ansible.ModuleUtils.Basic' in dep_finder.cs_utils_wrapper
    assert 'Ansible.ModuleUtils.Process' in dep_finder.cs_utils_wrapper
    assert 'Ansible.ModuleUtils.Common' in dep_finder.cs_utils_wrapper
    assert 'Ansible.ModuleUtils.Logging' in dep_finder.cs_utils_wrapper
    assert 'Ansible.ModuleUtils.PSCompatibility' in dep_finder.cs_utils_wrapper

    assert len(dep_finder.ps_modules) == 5

# Generated at 2022-06-12 21:48:42.960741
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test with name "unix_lsb_facts"
    # posix not supported
    # ps_module_dep_finder = PSModuleDepFinder()
    # assert ps_module_dep_finder.scan_exec_script("unix_lsb_facts")
    pass


# Generated at 2022-06-12 21:48:48.556404
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import pdb
    def f():
        pass
    pdb.set_trace()
    fo = open(os.path.expanduser('~') + '\\Desktop\\ps_module_util.psm1', 'rb')
    data = fo.read()
    fo.close()
    #pdb.set_trace()
    m = PSModuleDepFinder()
    m.scan_module(data, wrapper=True, powershell=True)
    #scan_module(data, wrapper=True, powershell=True)



# Generated at 2022-06-12 21:48:58.042766
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.common.powershell import module_manifest
    from ansible_collections.ansible.windows.plugins.module_utils.network.win_dns_client import module_manifest
    data = pkgutil.get_data("ansible.module_utils.common.powershell", "module_manifest.ps1").decode()
    import ansible_collections.ansible.windows.plugins.module_utils.network
    depfinder = PSModuleDepFinder()
    depfinder.scan_module(data.encode(), fqn="module_manifest")
    # print(depfinder.ps_modules)
    # print('*'*100)
    # print(depfinder.cs_utils_wrapper)
    # print('*'*100)
    # print(depfinder.cs_utils

# Generated at 2022-06-12 21:49:07.082124
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import random
    from ansible.module_utils.six import b
    from ansible.module_utils.six.moves import builtins

    TESTING = True
    test_depfinder = PSModuleDepFinder()

    # Tests for no lines
    test_name = "test_%d" % random.randint(1, 1000000)
    test_data = b("")
    test_depfinder.scan_exec_script(test_name)
    assert test_name not in test_depfinder.exec_scripts

    # Tests for blank lines
    test_name = "test_%d" % random.randint(1, 1000000)
    test_data = b("\n")
    test_depfinder.scan_exec_script(test_name)
    assert test_name not in test_depfinder.exec_scripts


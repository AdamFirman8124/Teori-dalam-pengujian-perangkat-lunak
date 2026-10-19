

# Generated at 2022-06-12 21:41:08.745098
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script('ansible_module_wrapper')


# Generated at 2022-06-12 21:41:16.824553
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Note: This is a test for function scan_exec_script of class PSModuleDepFinder

    # Generated stub for a function.
    def _strip_comments(data):
        # This comment is pulled from `utils/module_docs_fragments/platform/windows.py`.
        data = to_bytes(data, errors='surrogate_or_strict')
        if b'\n' not in data:
            # No newlines, fast-path the regexp
            ret = re.sub(br'#.*$', b'', data, flags=re.M)
        else:
            lines = []
            for line in data.splitlines():
                lines.append(re.sub(br'#.*$', b'', line))
            ret = b'\n'.join(lines)

# Generated at 2022-06-12 21:41:30.288674
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class Assertions:
        def __init__(self):
            self.args = []
            self.kwargs = {}

        def get_data(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            return "string"

    class Assertions_pkg_data:
        def __init__(self):
            self.args = []
            self.kwargs = {}

        def get_data(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class TestAnsibleModuleDepFinder():
        def __init__(self):
            self.ps_modules = {
                "PsModule": "string",
            }

# Generated at 2022-06-12 21:41:35.119420
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    # test 1
    name = "hello"
    data = """\
#AnsibleRequires -PowerShell Ansible.ModuleUtils.Powershell.dll

    """
    assert finder.scan_exec_script(name) is None



# Generated at 2022-06-12 21:41:44.288782
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import os
    
    # Path to test data directory
    test_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    
    test_files = [
        'module_utils_test_1.psm1',
        'module_utils_test_2.psm1'
    ]
    
    ps_module_finder = PSModuleDepFinder()
    
    util_data = _slurp(os.path.join(test_data, test_files[1]))
    ps_module_finder.scan_module(util_data, fqn='Ansible.ModuleUtils.Test2')
    
    # check that the module was added to the ps module dict
    assert 'Ansible.ModuleUtils.Test2' in ps_

# Generated at 2022-06-12 21:41:45.246574
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    # Put your code here.
    pass

# Generated at 2022-06-12 21:41:53.098522
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    if not C.DEFAULT_DEBUG:
        return

    psModuleDepFinder = PSModuleDepFinder()


# Generated at 2022-06-12 21:41:57.120883
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    '''
    Test :class:`ansible.module_utils.powershell.PSModuleDepFinder`
    method :func:`ansible.module_utils.powershell.PSModuleDepFinder.scan_exec_script`
    '''
    pass


# Generated at 2022-06-12 21:41:59.395981
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script('file_common')


# Generated at 2022-06-12 21:42:05.375870
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test mocking class and methods
    class TestHelper(object):

        def __init__(self, test_object, test_methods=None):
            self._test_object = test_object

            if test_methods is None:
                test_methods = [name for name in dir(test_object) if name.startswith('test_')]

            for name in test_methods:
                setattr(self, name, getattr(test_object, name))
    
    # Mock of _strip_comments
    def mocked__strip_comments(data):
        return data
     
    # Mock of _slurp
    def mocked__slurp(path):
        return "data"
     
    # Mock of pkgutil.get_data

# Generated at 2022-06-12 21:42:23.964136
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
	mu_finder = PSModuleDepFinder()
	mu_finder.scan_exec_script("powershell_powershell")


# Generated at 2022-06-12 21:42:33.518859
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import json
    import collections

    # get a dict object
    with open("../lib/ansible/executor/powershell/exec_ps.ps1", "rb") as f:
        exec_ps_b64 = base64.b64encode(f.read()).decode('ascii')
        data = json.dumps({"args": ["python", "-c", "exec(__import__('base64').b64decode(__import__('sys').stdin.read()))"], "stdin": exec_ps_b64})
        ps_exec_script = collections.OrderedDict()
        ps_exec_script["ps_exec_script"] = data

        # serializing the data into JSON
        json_object = json.dumps(ps_exec_script, indent = 4)
        print(json_object)

# Generated at 2022-06-12 21:42:38.870270
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("win_command")
    assert finder.exec_scripts["win_command"].startswith(b"function Invoke-Ansible")



# Generated at 2022-06-12 21:42:46.415161
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
  # Create an instance of class PSModuleDepFinder
  dep_finder = PSModuleDepFinder()
  
  # Test method scan_exec_script with name, invalid_powershell_script
  with pytest.raises(AnsibleError) as excinfo:
    dep_finder.scan_exec_script(name,invalid_powershell_script)
  assert "Could not find executor powershell script for '%s'" % name in str(excinfo.value)
  
  # Test method scan_exec_script with name, valid_powershell_script
  dep_finder.scan_exec_script(name,valid_powershell_script)
  assert dep_finder.exec_scripts[name] == valid_powershell_script


# Generated at 2022-06-12 21:42:58.985865
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    class Test:
        def test_method(self):
            pass

    def get_module_fixture_data(name):
        if name == "test_module":
            return pkgutil.get_data("ansible.modules.test.test_test.test_test", "test_module.psm1")
        elif name == "module_util_1":
            return pkgutil.get_data("ansible.module_utils.test", "module_util_1.psm1")
        elif name == "module_util_2":
            return pkgutil.get_data("ansible.module_utils.test", "module_util_2.psm1")

# Generated at 2022-06-12 21:43:10.065033
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import re

    # monkey patch the dep finder so we can test the parsing of
    # exec scripts
    call_count = {'exec_scripts': 0}

    def mock_scan_exec_script(self, name):
        call_count['exec_scripts'] += 1
        assert name == 'OpenSSHUtils'
    PSModuleDepFinder.scan_exec_script = mock_scan_exec_script

    # test the handling of wrapping modules and their requirements
    dep_finder = PSModuleDepFinder()

# Generated at 2022-06-12 21:43:14.824455
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    script_name = 'windows_powershell_test_script'
    expected_utils = {'test_module', 'test_module2'}
    expected_dependencies = {'test_module': {'.psm1', '.cs'}, 'test_module2': {'.psm1'}}
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script(script_name)
    assert psmdf.exec_scripts[script_name] is not None
    assert psmdf.cs_utils_wrapper is not None
    assert psmdf.ps_modules is not None
    assert set(psmdf.cs_utils_wrapper.keys()) == expected_utils
    assert set(psmdf.ps_modules.keys()) == expected_utils

# Generated at 2022-06-12 21:43:17.572203
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test that scan_exec_script handles a non-existent script.

    instance = PSModuleDepFinder()
    try:
        instance.scan_exec_script("invalid_script")
        assert False, "AnsibleError expected."
    except AnsibleError as e:
        assert "Could not find executor powershell script" in to_text(e)



# Generated at 2022-06-12 21:43:28.024604
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    def _get_data(path):
        with open(path, 'rb') as f:
            return to_bytes(f.read())

    def _setup_dep_finder(data):
        dep_finder = PSModuleDepFinder()
        dep_finder.scan_module(data)
        return dep_finder

    current_dir = os.path.dirname(os.path.realpath(__file__))
    fixture_dir = os.path.join(current_dir, 'tests/fixtures')
    fixture_name = 'ps_module_dep_finder'

    # setup base module
    module_path = os.path.join(fixture_dir, 'ps_modules', '{}.psm1'.format(fixture_name))
    data = _get_data(module_path)

# Generated at 2022-06-12 21:43:34.556478
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    script = r"""# test"""
    finder = PSModuleDepFinder()
    finder.scan_exec_script(to_text(script))
    assert isinstance(finder.exec_scripts, dict), "scan_exec_script() did not return a dict"
    assert script in finder.exec_scripts, "scan_exec_script() did not return a dict with the script name"
    assert isinstance(finder.exec_scripts[script], bytes), "scan_exec_scripts() did not return bytecode"

# Generated at 2022-06-12 21:44:12.759665
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    file_path = os.path.join(C.MODULE_UTILS_PATH, 'powershell', 'Basic.ps1')
    scanner = PSModuleDepFinder()
    scanner.scan_exec_script('Basic')
    assert (scanner.exec_scripts["Basic"] == b_str(_slurp(file_path)))

# Generated at 2022-06-12 21:44:15.334400
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('exec_wrapper')
    result = finder.exec_scripts
    # assert result == {'exec_wrapper': expected}


# Generated at 2022-06-12 21:44:21.145164
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test with arch = x86, powershell = powershell, module_name = win_disk_facts, script_name = GetDiskInformation
    # Since you have mocked out everything all the test does is call the method under test
    # which does nothing.
    pass

# Generated at 2022-06-12 21:44:27.735264
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mu_finder = PSModuleDepFinder()
    mu_finder.scan_exec_script(name='add_host')

# Generated at 2022-06-12 21:44:40.817727
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import tempfile
    import shutil
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.ps_modules = dict()
    ps_module_dep_finder.cs_utils_wrapper = dict()
    ps_module_dep_finder.cs_utils_module = dict()
    ps_module_dep_finder.exec_scripts = dict()
    ps_module_dep_finder.ps_version = None
    ps_module_dep_finder.os_version = None
    ps_module_dep_finder.become = False
    temp_dir = tempfile.mkdtemp()
    temp_path_1 = os.path.join(temp_dir, 'test_file.txt')

# Generated at 2022-06-12 21:44:48.021930
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    PSModuleDepFinder_instance = PSModuleDepFinder()
    PSModuleDepFinder_instance.scan_exec_script("ping")
    PSModuleDepFinder_instance.scan_exec_script("internal")
    PSModuleDepFinder_instance.scan_exec_script("internal_data.json")
    PSModuleDepFinder_instance.scan_exec_script("internal_common.ps1")
    PSModuleDepFinder_instance.scan_exec_script("internal_common.pmc")
    PSModuleDepFinder_instance.scan_exec_script("internal_module_utils.ps1")
    PSModuleDepFinder_instance.scan_exec_script("internal_module_utils.pmc")


# Generated at 2022-06-12 21:44:59.289365
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import os
    import tempfile

    tmpdir = tempfile.mkdtemp()

    test_file = tempfile.NamedTemporaryFile(dir=tmpdir, mode='w+', delete=False)
    test_file.write("#AnsibleRequires -Wrapper testfile\n")

    # Mock the wrapper
    test_file_wrapper = tempfile.NamedTemporaryFile(dir=tmpdir, mode='w+', delete=False)
    test_file_wrapper.write("#AnsibleRequires -Wrapper testfile_wrapper\n")


# Generated at 2022-06-12 21:45:08.691345
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    PSModuleDepFinder.scan_exec_script = None
    from ansible.module_utils.powershell.executor import PSModuleDepFinder

    module_utils = PSModuleDepFinder()

    assert module_utils.scan_exec_script('CommonTests') == None

    # assert that the executor scripts are being added to the dict
    assert module_utils.exec_scripts['CommonTests'] is not None
    assert module_utils.exec_scripts['CommonTests'] == b'\r\n$ErrorActionPreference = \'Stop\'\r\n\r\n\r\nImport-Module CommonTests\r\n\r\n'


# Generated at 2022-06-12 21:45:09.683196
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass



# Generated at 2022-06-12 21:45:17.962737
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    random_str = to_text(base64.b64encode(os.urandom(16)).rstrip(b'='))
    script_name = "executor_test_%s" % random_str
    script_data = "#ExecutorTest\r\nWrite-Host foo"

    f, script_path = _create_script(script_data, script_name)

    psdepfinder = PSModuleDepFinder()

    psdepfinder.scan_exec_script(script_name)

    assert random_str in psdepfinder.exec_scripts, "PSModuleDepFinder did not create an entry for the executor script"
    assert psdepfinder.exec_scripts[script_name] == script_data.encode('utf-8'), \
        "The script data does not match the script data used to populate it"


# Unit

# Generated at 2022-06-12 21:46:04.804044
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("ntfs.ps1")
    assert len(finder.exec_scripts.keys()) > 0
    assert len(finder.ps_modules.keys()) > 0

# Generated at 2022-06-12 21:46:05.425881
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass

# Generated at 2022-06-12 21:46:14.630689
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    mu_scanner = PSModuleDepFinder()
    module_1 = """#Requires -Version 5.1
#Requires -Module Ansible.ModuleUtils.ConfigBuilder
#AnsibleRequires -wrapper ps_modules_wrapper -PowerShell Ansible.ModuleUtils.ConfigBuilder
"""
    mu_scanner.scan_module(module_1, fqn='test_module', wrapper=False, powershell=True)

    assert list(mu_scanner.ps_modules.keys()) == ["Ansible.ModuleUtils.ConfigBuilder"]
    assert list(mu_scanner.cs_utils_module.keys()) == ["Ansible.ModuleUtils.ConfigBuilder"]
    assert list(mu_scanner.exec_scripts.keys()) == ["ps_modules_wrapper"]

# Generated at 2022-06-12 21:46:15.297169
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass

# Generated at 2022-06-12 21:46:24.073267
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # setup
    test_module_data = '''
# Requires -Module Ansible.ModuleUtils.Foo
# Requires -Module Ansible.ModuleUtils.Bar
'''
    # setup test data
    ps_finder = PSModuleDepFinder()

    # execute
    ps_finder.scan_module(test_module_data)

    # assert expected
    assert ps_finder.ps_modules["Ansible.ModuleUtils.Foo"] == {
        'data': b'foo',
        'path': 'path/to/Foo.psm1',
    }
    assert ps_finder.ps_modules["Ansible.ModuleUtils.Bar"] == {
        'data': b'bar',
        'path': 'path/to/Bar.psm1',
    }
    assert ps_finder.cs_

# Generated at 2022-06-12 21:46:36.001993
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    
    def test_case_scan_powershell_module():
        fd, temp_file = tempfile.mkstemp()
        with open(temp_file, 'wb') as f:
            f.write(b"""
#Requires -Module Ansible.ModuleUtils.foo
#Requires -Module Ansible.ModuleUtils.bar
#Requires -Module Ansible.ModuleUtils.baz""")

        depfinder = PSModuleDepFinder()
        try:
            depfinder.scan_module(open(temp_file, 'rb').read())
            assert sorted(depfinder.ps_modules.keys()) == ['Ansible.ModuleUtils.bar', 'Ansible.ModuleUtils.baz', 'Ansible.ModuleUtils.foo']
        finally:
            os.close(fd)

# Generated at 2022-06-12 21:46:43.119712
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.plugins.loader import ps_module_utils_loader

    loader = ps_module_utils_loader
    finder = PSModuleDepFinder()
    finder.scan_exec_script("common")
    assert "common" in finder.exec_scripts.keys()
    s = finder.exec_scripts['common']
    assert type(s) == bytes
    assert len(s) > 0
    assert "common.psm1" in loader.find_plugin("Ansible.ModuleUtils.Common", ".psm1")


# Generated at 2022-06-12 21:46:50.650084
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    f = PSModuleDepFinder()

# Generated at 2022-06-12 21:47:02.793438
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    """Test for PSModuleDepFinder.scan_module"""
    # read the raw module data
    module_data = pkgutil.get_data("ansible_collections.vmware.vmware_rest.plugins.modules", "vmware_vm_shell.py")
    import os
    filename = os.path.realpath(__file__)
    module_data = open(filename, 'rb').read()
    # create a PSModuleDepFinder object
    ps_dep_finder = PSModuleDepFinder()
    ps_dep_finder.scan_module(module_data)
    # check some of the results
    assert len(ps_dep_finder.cs_utils_module) == 1
    assert len(ps_dep_finder.ps_modules) == 0

# Generated at 2022-06-12 21:47:11.037304
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Depends on values from ansible-playbook
    # .\test\units\modules\test_package_facts.py
    from ansible_collections.ansible.playbook.plugins.module_utils import package_facts as utils
    from ansible_collections.ansible.playbook.plugins.modules import package_facts

    psmd = PSModuleDepFinder()
    psmd.scan_module(to_bytes(package_facts.__doc__),
                     fqn='ansible_collections.ansible.playbook.plugins.modules.package_facts')
    # only detect the module, not the util

# Generated at 2022-06-12 21:48:28.704092
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import os
    import sys

    current_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(current_dir)
    ps_module_dep_finder = PSModuleDepFinder()

    ps_module_dep_finder.scan_module(to_bytes(r'# Requires -Module Ansible.ModuleUtils.Powershell.System'))
    ps_module_dep_finder.scan_module(to_bytes(r'# Requires -Module Ansible.ModuleUtils.Powershell.Core'))
    ps_module_dep_finder.scan_module(to_bytes(r'# ANSIBLE VERSION: ansible_collections.test.test_collection.plugins.module_utils.ansible_version'))
    ps_module_dep_finder.scan_module

# Generated at 2022-06-12 21:48:39.229493
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    obj = PSModuleDepFinder()
    data = b'#Requires -Module Ansible.ModuleUtils.Foo\n#Requires -Module Ansible.ModuleUtils.Bar'
    fqn = 'ansible_collections.ns.coll.plugins.modules.foo'
    obj.scan_module(data, fqn)
    assert obj.ps_modules == {'Ansible.ModuleUtils.Foo': {'data': b'foo', 'path': '/path/to/Foo.psm1'},
                              'Ansible.ModuleUtils.Bar': {'data': b'bar', 'path': '/path/to/Bar.psm1'}}


# Generated at 2022-06-12 21:48:48.064073
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Arrange
    ps_module_finder = PSModuleDepFinder()
    test_module_data = ("#Requires -Module Ansible.ModuleUtils.TestModuleUtil\n"
                        "#Requires -Module Ansible.ModuleUtils.AnotherTestModuleUtil")

    # Act
    ps_module_finder.scan_module(test_module_data, fqn="ansible.builtin.testmodule")

    # Assert
    assert ps_module_finder.ps_modules["Ansible.ModuleUtils.TestModuleUtil"]['data'] == \
        to_bytes(_slurp(ps_module_finder.ps_modules["Ansible.ModuleUtils.TestModuleUtil"]['path']))

# Generated at 2022-06-12 21:48:56.153321
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    my_script_name = rand_str()
    my_script_body = rand_str()
    my_script_body_after_comments_stripped = rand_str()

    my_pkg_data = rand_str()
    my_pkg_data_after_comments_stripped = rand_str()
    my_fqn = rand_str()
    my_module_data = rand_str()
    my_module_data_after_comments_stripped = rand_str()

    md5_hash = _md5_sum(my_script_body)
    md5_hash_after_comments_stripped = _md5_sum(my_script_body_after_comments_stripped)
    md5_pkg_data_hash = _md5_sum(my_pkg_data)
    md5_pkg_data

# Generated at 2022-06-12 21:49:05.582597
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
	from ansible.module_utils.basic import *
	from ansible.module_utils.six import PY2
	from ansible.module_utils.common._collections_compat import MutableMapping
	import psutil
	import os
	import time
	import sys
	import pytest
	test_dir = os.getcwd()
	test_dir = test_dir.split('test')[0] + '/hacking'
	f = open(test_dir + '/ps_script.ps1')
	data = f.readlines()
	raw_str = ""
	for line in data:
		raw_str += line.strip('\n')
	start_processes = len(psutil.pids())
	ps_module_dep = PSModuleDepFinder()
	ps_module_dep.scan_

# Generated at 2022-06-12 21:49:14.116216
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    fd = PSModuleDepFinder()
    ps_modules = {}
    cs_utils = {}
    becomes = {}
    ps_versions = {}
    os_versions = {}
    exec_scripts = {}

# Generated at 2022-06-12 21:49:26.188764
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_module('#AnsibleRequires -CSharpUtil ansible_collections.test.test.plugins.module_utils.testutil')
    assert 'ansible_collections.test.test.plugins.module_utils.testutil' in dep_finder.cs_utils_module.keys()
    assert 'ansible_collections.test.test.plugins.module_utils.testutil' not in dep_finder.cs_utils_wrapper.keys()
    assert 'ansible_collections.test.test.plugins.module_utils.testutil' not in dep_finder.ps_modules.keys()
    dep_finder.scan_module('#AnsibleRequires -CSharpUtil ansible_collections.test.test.plugins.module_utils.testutil -Optional')

# Generated at 2022-06-12 21:49:34.629681
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Constructor
    obj = PSModuleDepFinder()
    # Method scan_module
    ps_module_with_dependency_in_string = '''#Requires -Module Ansible.ModuleUtils.Common'''
    obj.scan_module(ps_module_with_dependency_in_string)
    ps_module_with_dependency_in_comment = '''\
# This is a comment
#Requires -Module Ansible.ModuleUtils.Common'''
    obj.scan_module(ps_module_with_dependency_in_comment)


# Generated at 2022-06-12 21:49:36.902472
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mu_finder = PSModuleDepFinder()
    mu_finder.scan_exec_script('exec_wrapper')

    assert mu_finder


# Generated at 2022-06-12 21:49:46.742838
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    instance = PSModuleDepFinder()


# Generated at 2022-06-12 21:50:30.011032
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    name = "Test"
    ps_module_dep_finder.scan_exec_script(name)
    assert name in ps_module_dep_finder.exec_scripts.keys()


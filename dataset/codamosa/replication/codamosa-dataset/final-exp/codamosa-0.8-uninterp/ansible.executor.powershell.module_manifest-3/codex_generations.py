

# Generated at 2022-06-12 21:41:08.573285
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:41:16.730124
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from importlib import import_module
    from ansible.module_utils.plugins.loader import ps_module_utils_loader
    import ansible.utils.path
    import ansible.utils.display
    import ansible
    p = PSModuleDepFinder()
    import_module('ansible.executor.powershell')
    ansible.utils.path._ANSIBLE_INSTALL_PATH = ansible.utils.path._ANSIBLE_INSTALL_PATH+'\\test\\unit\\'
    ansible.utils.display.DISPLAY = ansible.utils.display.Display()
    mu_path = ps_module_utils_loader.find_plugin("Ansible.ModuleUtils.TestModuleUtils", ".psm1")
    mu_data = _slurp(mu_path)
    assert len(mu_data)>0

# Generated at 2022-06-12 21:41:30.175937
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:41:40.941581
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import ansible.executor.powershell as powershell

# Generated at 2022-06-12 21:41:50.283749
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    assert finder.exec_scripts == {}
    assert finder.cs_utils_module == {}
    assert finder.ps_modules == {}
    finder.scan_exec_script("A")
    assert len(finder.exec_scripts) == 1
    assert len(finder.cs_utils_module) == 0
    assert len(finder.ps_modules) == 0
    finder.scan_exec_script("A")
    assert len(finder.exec_scripts) == 1
    assert len(finder.cs_utils_module) == 0
    assert len(finder.ps_modules) == 0
    finder.scan_exec_script("B")
    assert len(finder.exec_scripts) == 2
    assert len(finder.cs_utils_module) == 0

# Generated at 2022-06-12 21:42:00.219372
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    class Args(object):
        pass

    class Options(object):
        pass

    args = Args()
    options = Options()
    args.options = options
    args.module_args = []

    args.module_path = "/tmp"

# Generated at 2022-06-12 21:42:04.925334
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    data = pkgutil.get_data("ansible.executor.powershell", "executor.ps1")
    if data is None:
        raise AnsibleError("Could not find executor powershell script "
                           "for '%s'" % 'executor')

    b_data = to_bytes(data)
    # remove comments and extra whitespace to reduce the payload size in the exec wrappers
    if C.DEFAULT_DEBUG:
        exec_script = b_data
    else:
        exec_script = _strip_comments(b_data)
    this.exec_scripts['executor'] = to_bytes(exec_script)


# Generated at 2022-06-12 21:42:10.578717
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class X(object):
        pass

    setattr(X, '_re_cs_module', [re.compile(to_bytes(r'(?i)^using\s((Ansible\..+)|'
                                                    r'(ansible_collections\.\w+\.\w+\.plugins\.module_utils\.[\w\.]+));\s*$'))])

# Generated at 2022-06-12 21:42:16.258158
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # module_data should be of type binary.  Take the string we have and decode it.
    module_data = b"""# Copyright (c) 2017 Microsoft Corporation
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Requires -Version 5.1

# AnsibleRequires -ModuleName PSDesiredStateConfiguration
# AnsibleRequires -Version 2.2.2.0

using namespace System.Management.Automation
using namespace System.Management.Automation.Language
using namespace Microsoft.PowerShell.DesiredStateConfiguration.DSCResources
"""
    _SD = PSModuleDepFinder()

# Generated at 2022-06-12 21:42:23.017750
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test cases for PSModuleDepFinder.scan_module()
    # For all test cases that fail the assert, the error messages must be added
    # to the test case.
    # Test cases are listed by method and by 'positive' or 'negative'
    # assertions.
    # Test cases that are not marked with @pytest.mark.skip will be executed as
    # part of the unit test suite.
    # Test cases marked with @pytest.mark.skip will not be executed, but need to
    # be reviewed to be cleared and removed from the file.

    # Place for clean up and temporary scripts for the test cases.
    tempdir = None

    # Helpers for PSModuleDepFinder.scan_module() tests
    # Bootstrap a module_utils directory for the test case.
    # A module_utils directory will be created in a tempdir

# Generated at 2022-06-12 21:42:36.421812
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    PSModuleDepFinder_obj = PSModuleDepFinder()
    name = "Powershell_Common"
    # pdb.set_trace()
    PSModuleDepFinder_obj.scan_exec_script(name)



# Generated at 2022-06-12 21:42:45.242831
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils import basic
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.text.converters import to_bytes
    test_data_path = os.path.join(os.path.dirname(__file__),
                                  b'test_data/PSModuleDepFinder')
    test_data_files = [f for f in os.listdir(test_data_path) if os.path.isfile(os.path.join(test_data_path, f))]
    test_data_map = {}

# Generated at 2022-06-12 21:42:52.429138
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Create a test class
    finder = PSModuleDepFinder()
    # Function under test
    finder.scan_exec_script("ansible_module_generated.ps1")
    assert finder.exec_scripts.__len__() == 1
    # A new instance of PSModuleDepFinder must have same number of exec_scripts
    finder = PSModuleDepFinder()
    assert finder.exec_scripts.__len__() == 1



# Generated at 2022-06-12 21:42:55.638135
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Create class instance.
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('connection_wrapper')
    assert True


# Generated at 2022-06-12 21:43:07.616923
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    f = PSModuleDepFinder()
    f.scan_exec_script('Windows.ps1')
    assert b'#ansiblerequires -powershell ansible_collections.ansible.builtin.plugins.module_utils.ansible_module_common' in f.exec_scripts['Windows.ps1']
    assert b'#ansiblerequires -powershell ansible_collections.ansible.builtin.plugins.module_utils.ansible_module_runner' in f.exec_scripts['Windows.ps1']
    assert b'#ansiblerequires -powershell ansible_collections.ansible.builtin.plugins.module_utils.ansible_module_utils' in f.exec_scripts['Windows.ps1']

# Generated at 2022-06-12 21:43:08.643185
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass # TODO


# Generated at 2022-06-12 21:43:12.660606
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    script = '''#ansiblerequires -wrapper wrapper_name'''
    ps_mod_dep_finder = PSModuleDepFinder()
    ps_mod_dep_finder.scan_module(script, '', wrapper=True, powershell=True)
    assert ps_mod_dep_finder.exec_scripts['wrapper_name']


# Generated at 2022-06-12 21:43:20.616049
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils._text import to_text

    mdf = PSModuleDepFinder()

    base64_data = base64.b64encode(to_text('<# Write-Output "Hello World" #>').encode('utf-8'))
    data = {'ansible_module_version': 2,
            'ansible_module_utils': [],
            'ansible_module_wrapper': {
                'script': base64_data,
                'type': 'powershell'
            },
            'execution_environment': {
                'powershell_version': '>5.1',
                'os_family': 'windows'
            }}

    mdf.scan_exec_script('test_scan_exec_script_example')

# Generated at 2022-06-12 21:43:28.518552
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.common._collections_compat import MutableMapping

    depfinder = PSModuleDepFinder()
    depfinder.scan_exec_script("internal/importer")
    assert isinstance(depfinder.exec_scripts, MutableMapping)
    assert depfinder.exec_scripts["internal/importer"].startswith(b"Param")
    assert depfinder.exec_scripts["internal/importer"].endswith(b"\n}")
    assert depfinder.exec_scripts["internal/importer"].count(b"\n") > 2


# Generated at 2022-06-12 21:43:30.257706
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    PSModuleDepFinder_instance = PSModuleDepFinder()
    PSModuleDepFinder_instance.scan_exec_script(name)



# Generated at 2022-06-12 21:43:49.061545
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
     with open("./test/test_module_utils_ps_depfinder/module_data", "rb") as file:
         module_data = file.read()
     # module_data = to_bytes(f.read())
     psModuleDep = PSModuleDepFinder()
     psModuleDep.scan_module(module_data)
     return psModuleDep


# Generated at 2022-06-12 21:43:54.361852
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # This is an example unit test method.
    module_data = base64.b64encode(b'''\
#! /usr/bin/python
"""
ANSIBLE MODULES HERE
"""
ANSIBLE VERSION
''')
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_module(module_data, fqn=None, wrapper=False, powershell=True)
    assert True

# Generated at 2022-06-12 21:44:04.032297
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import tempfile
    import shutil
    import sys
    import imp

    test_dir = tempfile.mkdtemp()
    test_ps1 = os.path.join(test_dir, 'test.ps1')
    with open(test_ps1, 'w') as f:
        f.write("""\
#AnsibleRequires -CSharpUtil ansible_collections.{namespace}.{collection}.plugins.module_utils.pwsh
Write-Output 'Hello from powershell!'
""")

    sys.path.append(test_dir)
    imp.load_source('test', test_ps1)

    shutil.rmtree(test_dir)



# Generated at 2022-06-12 21:44:14.462558
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:44:16.601927
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:44:28.760581
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import os
    import sys

    # If you haven't installed your local repository, these environment
    # variables will not exist
    python_path = ":" + os.environ.get("PYTHONPATH", "")
    sys.path.extend(python_path.split(":"))

    # If you haven't installed your local repository, the module will not be
    # found
    import ansible_module_deps

    finder = ansible_module_deps.PSModuleDepFinder()
    finder.scan_exec_script("Ansible.ModuleRun")
    assert finder.exec_scripts["Ansible.ModuleRun"] != ""
    assert 'Ansible.ModuleUtils.Common' in finder.ps_modules.keys()

# Generated at 2022-06-12 21:44:41.074925
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # This test uses the following variables
    # test_PSModuleDepFinder_use_module_class.py
    # This class is used to test the following sections of the PS Module
    # Ansible.ModuleUtils.Powershell.

    finder = PSModuleDepFinder()

    test_script = "a"
    finder.scan_exec_script(test_script)

    test_script = "a-b"
    finder.scan_exec_script(test_script)

    test_script = "a_b"
    finder.scan_exec_script(test_script)

    test_script = "a"
    result = finder.scan_exec_script(test_script)
    assert result is None



# Generated at 2022-06-12 21:44:43.344562
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    f = PSModuleDepFinder()
    f.scan_exec_script('common')
    assert f.exec_scripts is not None



# Generated at 2022-06-12 21:44:55.576914
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:44:59.529552
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("powershell_wrapper")
    assert len(dep_finder.exec_scripts) == 1
    assert type(dep_finder.exec_scripts) is dict

# Generated at 2022-06-12 21:45:25.456683
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True



# Generated at 2022-06-12 21:45:36.261768
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    # support for python 2.6
    pb64 = base64.b64encode
    pb64d = base64.b64decode

    def base64_encode(raw):
        # Must use bytes here because Python2 has no str.encode().
        # This can be removed if we bump the minimum version to 2.7.
        return pb64(to_bytes(raw, errors='surrogate_or_strict'))

    def base64_decode(raw):
        # Must use bytes here because Python2 has no str.encode().
        # This can be removed if we bump the minimum version to 2.7.
        return pb64d(to_bytes(raw, errors='surrogate_or_strict'))


# Generated at 2022-06-12 21:45:44.010761
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    def _create_module_data(content):
        module_data = ""
        for line in content:
            if not line.startswith("#"):
                line = "#%s" % line

            if not line.endswith("\n"):
                line = "%s\n" % line

            module_data = "%s%s" % (module_data, line)

        return module_data


# Generated at 2022-06-12 21:45:56.002308
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # test_PSModuleDepFinder_scan_exec_script(self)
    # test whether collecting the executor scripts is done correctly.
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script("shell_common")
    assert ps_module_dep_finder.exec_scripts['shell_common'] == _slurp(resource_from_fqcr("ansible.executor.powershell", "shell_common.ps1"))
    assert len(ps_module_dep_finder.exec_scripts) == 1
    assert len(ps_module_dep_finder.ps_modules) == 0
    assert len(ps_module_dep_finder.cs_utils_wrapper) == 0
    assert len(ps_module_dep_finder.cs_utils_module) == 0


# Generated at 2022-06-12 21:46:05.737003
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class TestPSModuleDepFinder(PSModuleDepFinder):
        def __init__(self):
            PSModuleDepFinder.__init__(self)
            self.exec_scripts = {
                "script1": "script1_data",
                "script2": "script2_data"
            }
            self.ps_modules = {
                "Ansible.ModuleUtils.Script1": "Script1_data",
                "Ansible.ModuleUtils.Script2": "Script2_data"
            }
            self.cs_utils_wrapper = {}
            self.ps_version = None
            self.os_version = None
            self.become = False

# Generated at 2022-06-12 21:46:08.751261
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmoddepfinder = PSModuleDepFinder()
    assert psmoddepfinder.exec_scripts == {}
    psmoddepfinder.scan_exec_script('win_package')
    assert psmoddepfinder.exec_scripts != {}


# Generated at 2022-06-12 21:46:15.946230
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    module_data = b"""
    # the rest of the file is irrelevant to this test.
    #Requires -Module Ansible.ModuleUtils.MyUtil
    """
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_module(module_data)
    assert(dep_finder.ps_modules["Ansible.ModuleUtils.MyUtil"] == {"data": b"UtilData", "path": "Path/To/Util"})


# Generated at 2022-06-12 21:46:24.342807
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test scan_exec_script() where the executor script contains
    # no module dependencies.
    b_data = b"function f{}"
    tmp_dir = os.path.dirname(os.path.dirname(__file__))
    tmp_fname = "tmp_ps_exec_script.ps1"
    tmp_path = os.path.join(tmp_dir, tmp_fname)
    with open(tmp_path, "wb") as test_file:
        test_file.write(b_data)

    mdf = PSModuleDepFinder()
    mdf.scan_exec_script("tmp_ps_exec_script")
    assert mdf.exec_scripts["tmp_ps_exec_script"] == b_data

    # Test scan_exec_script() where the executor script contains
    # two

# Generated at 2022-06-12 21:46:35.576956
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()

# Generated at 2022-06-12 21:46:39.873770
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    try:
        dep_finder.scan_exec_script("non-existent-script")
    except AnsibleError:
        pass
    else:
        raise AssertionError("AnsibleError not raised")
    dep_finder.scan_exec_script("exec_wrapper")
    assert dep_finder.exec_scripts != {}


# Generated at 2022-06-12 21:47:09.521002
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    module_data = """
#Requires -Module Ansible.ModuleUtils.FirstModule
#Requires -Module Ansible.ModuleUtils.SecondModule
"""
    finder = PSModuleDepFinder()
    finder.scan_module(module_data)
    assert len(finder.ps_modules.keys()) == 2
    assert len(finder.cs_utils_module.keys()) == 0
    
    

# Generated at 2022-06-12 21:47:19.118774
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.utils.collection_loader import _get_collection_name_from_path

    psmdf = PSModuleDepFinder()

    path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'lib', 'ansible', 'modules',
                        'network_cli', 'aruba', 'aruba_command.py')

    fqm = "%s.%s" % (_get_collection_name_from_path(path),
                     os.path.splitext(path)[0].split('/')[-1])
    psmdf.scan_module(to_bytes(_slurp(path)), fqn=fqn)

    assert len(psmdf.ps_modules) != 0



# Generated at 2022-06-12 21:47:26.128285
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    instance = PSModuleDepFinder()
    name = to_text('a name')
    
    # ansible.executor.powershell.a name.ps1 does not exist.
    # AnsibleError should be raised.
    result = instance.scan_exec_script(name)
    expected = AnsibleError
    if result.__class__ != expected.__class__:
        # raise AssertionError('instance.scan_exec_script should raise ' + str(expected))
        print('instance.scan_exec_script should raise ' + str(expected))


# Generated at 2022-06-12 21:47:34.119096
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    class MyPSModuleDepFinder(PSModuleDepFinder):
        def __init__(self):
            PSModuleDepFinder.__init__(self)

    finder = MyPSModuleDepFinder()

    finder.scan_module("""#Requires -Module Ansible.ModuleUtils.Test""")

    assert finder.ps_modules['Ansible.ModuleUtils.Test']
    assert len(finder.ps_modules) == 1

    finder.scan_module("""#AnsibleRequires -Powershell Ansible.ModuleUtils.Test""")

    assert finder.ps_modules['Ansible.ModuleUtils.Test']
    assert len(finder.ps_modules) == 1

    finder.scan_module("""#AnsibleRequires -CSharpUtil Ansible.ModuleUtils.Test""")

# Generated at 2022-06-12 21:47:45.588805
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.compat.tests.mock import patch

    pkgutil_get_data_mock = patch.object(pkgutil, "get_data")
    get_data_mock = pkgutil_get_data_mock.start()
    get_data_mock.return_value = "foo"

    def get_data_side_effect(name, resource):
        if name == "ansible_collections.test_ns.test_coll.plugins.module_utils.test_mu" \
                and resource == "test_mu.psm1":
            return "foo"
        elif name == "ansible.module_utils.test_mu" and resource == "test_mu.psm1":
            return "foo"

    get_data_mock.side_effect = get_data_side_effect

# Generated at 2022-06-12 21:47:48.636784
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import doctest, sys
    results = doctest.testmod(sys.modules[__name__])
    assert results.failed == 0

# Unit test method _add_module

# Generated at 2022-06-12 21:47:58.941935
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    def _test_ps_module_util(name):
        fqn = 'ansible_collections.community.general.plugins.module_utils.%s' % name
        dep_finder = PSModuleDepFinder()
        dep_finder.scan_module(resource_from_fqcr(fqn))
        assert 'ansible.module_utils.%s' % name in dep_finder.ps_modules
        assert fqn in dep_finder.cs_utils_wrapper
        assert fqn not in dep_finder.cs_utils_module

    def _test_cs_module_util(name):
        fqn = 'ansible_collections.community.general.plugins.module_utils.%s' % name
        dep_finder = PSModuleDepFinder()

# Generated at 2022-06-12 21:48:09.506150
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    def mock_get_data(*args, **kwargs):
        if args[1] == 'powershell.ps1':
            return '{"ansible_powershell_version": "6.0", "random_stuff": "foo"}'
        elif args[1] == 'powershell6.ps1':
            return '{"ansible_powershell_version": "6.1"}'
        elif args[1] == 'powershell7.ps1':
            return '{"ansible_powershell_version": "7.0"}'
        else:
            raise Exception("Unexpected call to get_data with args=%s and kwargs=%s" % (args, kwargs))

    def mock_scan_module(*args, **kwargs):
        pass

    finder = PSModuleDepFinder()
    finder._

# Generated at 2022-06-12 21:48:18.407614
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import os
    ansible_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    module_name = 'module_name'
    test_module_path = '{}/_test_module_{}.psm1'.format(ansible_path, module_name)
    if not os.path.exists(test_module_path):
        with open(test_module_path, 'a') as f:
            test_module_content = '{} module'.format(module_name)
            f.write(test_module_content)

    test_exec_script_name = 'test_exec_script'

# Generated at 2022-06-12 21:48:27.143476
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    import sys, traceback

    def shouldFail(fqn, module_data, exceptionMessage):
        try:
            md_finder = PSModuleDepFinder()
            md_finder.scan_module(module_data, fqn)
            print("Unexpected success: scan_module(fqn=%s)" % fqn)
            print("Input module_data:")
            print(module_data)
            return False
        except Exception as e:
            if e.args[0] == exceptionMessage:
                return True
            print("Got unexpected exception:")
            traceback.print_exc()
            return False


    # Test that scan_module fails when a PowerShell module lists a module_util that
    # doesn't exist.

# Generated at 2022-06-12 21:49:22.319659
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    finder = PSModuleDepFinder()
    finder.scan_exec_script("sample_json")
    # verify that the util referenced in the sample_json file exists in PSModuleDepFinder
    assert("Ansible.ModuleUtils.Basic" in finder.ps_modules)



# Generated at 2022-06-12 21:49:26.975136
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script('ansible_modlib.common.argspec')
    assert finder.exec_scripts['ansible_modlib.common.argspec'] is not None
    assert finder.ps_modules['Ansible.ModuleUtils.Powershell.Arguments'] is not None

# Generated at 2022-06-12 21:49:38.272028
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.plugins.loader import ps_module_utils_loader
    def mocked_cs_utils(self, module_utils, ext, fqn, optional, wrapper=False):
        return module_utils
    PSModuleDepFinder.scan_module = mocked_cs_utils
    # scan_exec_script(self, name)
    # mock the mocked_cs_utils method
    def mocked_cs_utils(self, module_utils, ext, fqn, optional, wrapper=False):
        return module_utils
    PSModuleDepFinder.scan_module = mocked_cs_utils
    module_utils_loader = ps_module_utils_loader

    m = PSModuleDepFinder()
    # name = 'fake_module'
    # try:
    #     m.scan_exec_script('fake_module')
    #

# Generated at 2022-06-12 21:49:48.087737
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:49:55.392457
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # create a mocked object and set the return values for mocked object
    mock = mocker.Mock()
    mock.side_effect = [
        '456',
        None,
    ]
    # set mocker return value for the mocked object
    mocker.patch('ansible.plugins.loader.ps_module_utils_loader.find_plugin', mock)
    # initialize PSModuleDepFinder object
    ps_module_dep_finder = __main__.PSModuleDepFinder()

    # created mocked object and set the return values for mocked object
    mock = mocker.Mock()
    mock.side_effect = [
        'abc',
        'def',
        'ghi',
        'jkl',
        'mno',
        'pqr',
    ]

    # set return values for mocked object
    mocker

# Generated at 2022-06-12 21:50:04.042858
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    module_dep_finder = PSModuleDepFinder()
    test_name = "exec_wrapper"
    test_module_data = u'\n'
    test_module_data = to_bytes(test_module_data)
    test_fqn = None
    test_wrapper = False
    test_powershell = True
    module_dep_finder.scan_module(test_module_data, test_fqn, test_wrapper, test_powershell)
    with pytest.raises(AnsibleError) as exc:
        module_dep_finder.scan_exec_script(test_name)
    assert "Could not find executor powershell script for 'exec_wrapper'" in str(exc.value)

# Generated at 2022-06-12 21:50:16.011203
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.common.json import AnsibleJSONEncoder
    import os

    # this test scans a sample module that requires a module_util.  Ideally it
    # would scan a module that requires multiple module_utils but the support
    # code isn't there yet
    try:
        test_module_path = to_text(os.path.join(C.TEST_DIR, "test_data/test_module_template.ps1"))
        with open(test_module_path, 'rb') as mod:
            module_data = mod.read()
    except Exception as e:
        raise AnsibleError("Could not read test data file: %s" % to_native(e))

    dep_finder = PSModuleDepFinder()
    dep_finder.scan_module(module_data)

    # validate we have the

# Generated at 2022-06-12 21:50:24.353233
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    # exec_script_path : path of the exec script to which the command is called
    # expected_output : expected output of the command
    # description : description of the test case
    test_cases = [(b'Invoke-Process', b'', \
                  'Verify Invoke-Process is fetched as exec_script_path')]

    for exec_script_path, expected_output, description in test_cases:

        ps_module_dep_finder = PSModuleDepFinder()
        ps_module_dep_finder.scan_exec_script(exec_script_path)

        assert exec_script_path in ps_module_dep_finder.exec_scripts.keys(), \
            "scan_exec_script fetched the exec script %s" % exec_script_path

# Generated at 2022-06-12 21:50:34.359365
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import sys
    import os
    import tempfile
    import types

    test_dir = tempfile.mkdtemp()
    old_cwd = os.getcwd()

    # create a module that requires a module_util from 'ansible.module_utils'
    # but only requires 'ansible' as a collection and does not include the
    # collection name
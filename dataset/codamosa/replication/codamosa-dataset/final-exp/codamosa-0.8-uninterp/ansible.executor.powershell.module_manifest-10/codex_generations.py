

# Generated at 2022-06-12 21:40:53.136571
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True

# Generated at 2022-06-12 21:41:00.494221
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:41:01.348677
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass
    # TODO


# Generated at 2022-06-12 21:41:09.419788
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_exec_script_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "utils", "powershell", "io")
    test_exec_scripts = [f for f in os.listdir(test_exec_script_dir) if f.endswith(".ps1")]
    pmdf = PSModuleDepFinder()
    for script in test_exec_scripts:
        pmdf.scan_exec_script(script.split(".")[0])
    assert len(pmdf.exec_scripts) > 10 # make sure we have something here


# Generated at 2022-06-12 21:41:17.186448
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    obj = PSModuleDepFinder()

    obj._add_module = mock.MagicMock()
    obj.scan_module = mock.MagicMock()
    obj._parse_version_match = mock.MagicMock()
    obj._re_wrapper = re.compile(to_bytes(r'(?i)^#\s*ansiblerequires\s+-wrapper\s+(\w*)'))
    obj._re_ps_version = re.compile(to_bytes(r'(?i)^#requires\s+\-version\s+([0-9]+(\.[0-9]+){0,3})$'))

# Generated at 2022-06-12 21:41:18.668559
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # [1] test the functionality of scan_exec_script
    assert True

# Generated at 2022-06-12 21:41:32.281557
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Skip test for py27 due to import issue for ansible.executor.powershell
    try:
        import ansible.executor.powershell
    except ImportError:
        return

    def side_effect_get_data(a, b):
        return 'some data'

    def side_effect_find_plugin(a, b):
        return "some/path"

    pkgutil_mock = mock.MagicMock()
    pkgutil_mock.get_data.side_effect = side_effect_get_data
    ps_module_utils_loader_mock = mock.MagicMock()
    ps_module_utils_loader_mock.find_plugin.side_effect = side_effect_find_plugin
    ps_module_dep_finder_mock = PSModuleDepFinder()
    ps_module

# Generated at 2022-06-12 21:41:39.419580
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    assert finder.exec_scripts == dict()

    # Load a script that doesn't exist
    try:
        finder.scan_exec_script("foo")
    except AnsibleError as ex:
        assert "Could not find executor powershell script for 'foo'" in str(ex)
    else:
        raise AssertionError("AnsibleError for 'foo' script not raised")

    # Load a script that does exist
    finder.scan_exec_script("AddPath")
    assert finder.exec_scripts["AddPath"] is not None

    # Load the same script again, it should have no effect
    finder.scan_exec_script("AddPath")
    assert len(finder.exec_scripts) == 1

    # Call scan_module to load a builtin module_util


# Generated at 2022-06-12 21:41:48.315545
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # test case: f57fb67d-5b87-49c5-b1e8-a24fd41fff89
    from collections import namedtuple
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.compat.version import LooseVersion

    import pytest

    AC = namedtuple(b'Module', [b'_original_path', b'args', b'_name', b'_uses_fragment_loader', b'_load_fragment'])
    from ansible.module_utils.common.collections import ImmutableDict
    mc = AC('', ImmutableDict(), 'os_flavor', True, False)

    aw = PSModuleDepFinder()

# Generated at 2022-06-12 21:41:51.495163
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script(b'debug')
    assert finder.exec_scripts[b'debug']
    assert finder.cs_utils_wrapper[b'Ansible.Collection.AnsibleCollection.plugins.module_utils.parsing'][b'path']

# Generated at 2022-06-12 21:42:11.570197
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import pytest
    import ansible
    import ansible.plugins.loader
    module_utils = set()
    module_util_name = "Ansible.ModuleUtils.urls"
    optional = False
    module_utils.add((module_util_name, ".psm1", None, optional))
    for m in module_utils:
        PSModuleDepFinder._add_module(*m, wrapper=False)
    assert PSModuleDepFinder().ps_modules == dict()
    assert PSModuleDepFinder().cs_utils_wrapper == dict()
    assert PSModuleDepFinder().cs_utils_module == dict()

if __name__ == '__main__':
    test_PSModuleDepFinder_scan_module()

# Generated at 2022-06-12 21:42:17.281457
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    md = PSModuleDepFinder()
    module_data = b'#Requires -Module Ansible.ModuleUtils.Something'
    md.scan_module(module_data)
    assert len(md.ps_modules) == 1

    md = PSModuleDepFinder()
    module_data = b'#AnsibleRequires -PowerShell Ansible.ModuleUtils.Something'
    md.scan_module(module_data)
    assert len(md.ps_modules) == 1

    md = PSModuleDepFinder()
    module_data = b'#AnsibleRequires -CSharpUtil Ansible.ModuleUtils.Something'
    md.scan_module(module_data)
    assert len(md.cs_utils_module) == 1

    md = PSModuleDepFinder()

# Generated at 2022-06-12 21:42:24.631437
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Make sure the module utils are loaded so we can scan them
    ps_module_utils_loader.all()

    from ansible.executor.powershell import _exec_wrapper_ps

    # Fake a module to use
    fake_module = 'test'

# Generated at 2022-06-12 21:42:35.071816
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # params is a tuple of arguments used to invoke the call, param is a
    # parameter at the index specified within arg_count,
    # default is a value that will be returned if the parameter is not provided
    params=[
        {
            'arg_count': 1,
            'param':
            {
                'name': 'powershell',
                'default': True
            },
            'func_to_call': 'scan_module'
        }
    ]

    # patching the method test_scan_module with the mock object
    with mock.patch.object(PSModuleDepFinder,'scan_module',return_value=None) as scan_module_func:
        ps_module_dep_finder = PSModuleDepFinder()
        ps_module_dep_finder.scan_exec_script('powershell_name1')
        scan_

# Generated at 2022-06-12 21:42:36.482729
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script(name="powershell_wrapper")
    assert ps_module_dep_finder.ps_modules == {}

# Generated at 2022-06-12 21:42:39.959558
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script("win_ping")
    assert len(psmdf.exec_scripts.keys()) == 1
# test_PSModuleDepFinder_scan_exec_script()


# Generated at 2022-06-12 21:42:41.306941
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    p = PSModuleDepFinder()
    assert isinstance(p, PSModuleDepFinder)
    assert p.scan_exec_script('ansible/module_utils/powershell/', 'ModuleBuilder')



# Generated at 2022-06-12 21:42:49.694831
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test the method scan_module of class PSModuleDepFinder
    test_module_data = '''
#Requires -Module Ansible.ModuleUtils.CommonUtils
#AnsibleRequires -Powershell Ansible.ModuleUtils.CollectionsUtils -Optional
#AnsibleRequires -Wrapper Ping
#AnsibleRequires -Powershell .JsonUtils.psm1
#Requires -version 4.0
#AnsibleRequires -CSharpUtil Ansible.Util.Json
#AnsibleRequires -CSharpUtil ansible_collections.my.collection.plugins.module_utils.Util
#AnsibleRequires -CSharpUtil ..Util
#AnsibleRequires -CSharpUtil ..Util2 -Optional

'''
    psdepfinder = PSModuleDepFinder()
    psdep

# Generated at 2022-06-12 21:42:52.963245
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script("psbase")
    

# Generated at 2022-06-12 21:43:05.169117
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    f = PSModuleDepFinder()
    ps_data = pkgutil.get_data("ansible.plugins.powershell", "TestModule.psm1")
    b_ps_data = to_bytes(ps_data)
    f.scan_module(b_ps_data, fqn="ansible.plugins.powershell.TestModule")

# Generated at 2022-06-12 21:43:19.181514
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False, "Unit test not implemented"


# Generated at 2022-06-12 21:43:27.473725
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.executor.powershell import exec_wrapper
    import copy
    from ansible.module_utils._text import to_bytes

    depfinder = PSModuleDepFinder()
    depfinder.scan_exec_script(to_text(exec_wrapper))

    assert depfinder.exec_scripts[to_text(exec_wrapper)]
    assert depfinder.exec_scripts[to_text(exec_wrapper)] == to_bytes(_slurp(ps_module_utils_loader.find_plugin("Ansible.ModuleUtils.ExecUtils", ".psm1")))


# Generated at 2022-06-12 21:43:34.770371
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.basic import *
    from ansible.module_utils.six.moves import StringIO

    # Get the module_utils in the python package path
    test_utils = pkgutil.get_data("ansible_collections.collection_name.plugins.module_utils", "test_util.psm1")
    test_cs_utils = pkgutil.get_data("ansible_collections.collection_name.plugins.module_utils", "test_cs_util.cs")

    # Create a module with a C# util that imports another util

# Generated at 2022-06-12 21:43:46.696224
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:43:55.974140
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    depfinder = PSModuleDepFinder()

    # Test scanning a powershell module
    module_util_data = '#Requires -Module Ansible.Foo'
    module_util_data = to_bytes(module_util_data)

    depfinder.scan_module(module_util_data)
    assert 'Ansible.Foo' in depfinder.ps_modules
    assert 'Ansible.Foo' in depfinder.ps_modules.keys()

    # Test scanning a powershell module that has a version requirement
    module_util_data = '#Requires -Module Ansible.Foo\n#Requires -Version 5.1'
    module_util_data = to_bytes(module_util_data)

    depfinder.scan_module(module_util_data)
    assert 'Ansible.Foo' in depfinder

# Generated at 2022-06-12 21:44:07.126943
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    mu = PSModuleDepFinder()
    mod_data = """
#Requires -Module Ansible.ModuleUtils.UrlUtils

$x = "test"
"""
    mu.scan_module(mod_data)
    assert mu.ps_modules['Ansible.ModuleUtils.UrlUtils']
    # invalid utils names
    mod_data = """
#AnsibleRequires -PowerShell .MY-UTIL-NAME

$x = "test"
"""
    try:
        mu.scan_module(mod_data)
        assert False, "Should have thrown an exception"
    except AnsibleError:
        pass

    # invalid import
    mod_data = """
#AnsibleRequires -PowerShell Ansible.MY-UTIL-NAME

$x = "test"
"""

# Generated at 2022-06-12 21:44:11.574150
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    finder = PSModuleDepFinder()
    # test actual module
    finder.scan_module(b'#AnsibleRequires -Module ansible.module_utils.{name}')
    assert finder.ps_modules
    # test scripting module
    finder.scan_exec_script(b'{name}')


# Generated at 2022-06-12 21:44:14.940866
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script('ansible.module_utils.basic')
    assert 'ansible.module_utils.basic' in ps_module_dep_finder.exec_scripts


# Generated at 2022-06-12 21:44:23.521124
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mu = PSModuleDepFinder()
    with pytest.raises(AnsibleError):
        mu.scan_exec_script(name='nonexist')
    mu.scan_exec_script(name='script')
    assert len(mu.exec_scripts) == 1
    assert len(mu.ps_modules) > 1
    assert len(mu.cs_utils_wrapper) == 0
    assert len(mu.cs_utils_module) == 0


# Generated at 2022-06-12 21:44:36.664722
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    from ansible.module_utils.powershell import _strip_comments

    found_version = None
    found_os_version = None

# Generated at 2022-06-12 21:44:54.133150
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("powershell_common")
    assert "powershell_common" in dep_finder.exec_scripts
    assert "z_internal_net_common" in dep_finder.cs_utils_wrapper
    assert "ansible_collections.microsoft.azure.plugins.module_utils.azure_rm_common" in dep_finder.cs_utils_wrapper

# Generated at 2022-06-12 21:45:05.369087
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import sys
    import os
    import tempfile

    # Make module_utils accessible
    path = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(1, path)

    from ansible_collections.test.collection_examples.my_namespace.my_collection.plugins.module_utils import test_utils
    from ansible_collections.test.collection_examples.my_namespace.my_collection.plugins.modules import test_module

    # Get module data
    module_data = test_module.__doc__
    filename = to_bytes(test_module.__file__)
    module_data = _slurp(filename)[3:]

    module_util_data = test_utils.__doc__

# Generated at 2022-06-12 21:45:07.531617
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # These are the tests for the scan_module method of class PSModuleDepFinder.
    pass



# Generated at 2022-06-12 21:45:11.931924
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    def do_test(dep_finder):
        dep_finder.scan_exec_script("shell")
        assert len(dep_finder.exec_scripts) == 1
        assert dep_finder.exec_scripts["shell"]

    dep_finder = PSModuleDepFinder()
    do_test(dep_finder)



# Generated at 2022-06-12 21:45:15.742353
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmd = PSModuleDepFinder()
    psmd.scan_exec_script(name="wrapper")
    assert "wrapper" in psmd.exec_scripts
    assert "posh-docker" in psmd.cs_utils_wrapper
    assert "win_ping" in psmd.ps_modules


# Generated at 2022-06-12 21:45:17.380447
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    assert dep_finder.scan_exec_script("/") is None


# Generated at 2022-06-12 21:45:21.443549
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mu = PSModuleDepFinder()
    mu.scan_exec_script("script_file.ps1")
    assert mu.exec_scripts['script_file'] == '\n# This is a script file.\n'


# Generated at 2022-06-12 21:45:32.640294
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    import ansible.module_utils.powershell
    from ansible_collections.ansible.misc.plugins.module_utils import random_words
    ns = "ansible_collections"
    coll = "ansible.misc"
    mod = "random_words"
    name = "%s.%s.%s" % (ns, coll, mod)
    module_data = _slurp(os.path.join(ansible_collections_path, ns, coll, "plugins", "modules", mod + ".ps1"))
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_module(module_data, fqn=name, wrapper=False, powershell=True)
    assert to_text(module_data).count('#Requires -Module') == 1
    assert len

# Generated at 2022-06-12 21:45:40.509684
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    data_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    os.chdir(data_dir)

    test_PSModDepFind = PSModuleDepFinder()

    test_PSModDepFind.scan_exec_script('basic')
    assert 'basic' in test_PSModDepFind.exec_scripts
    assert 'basic' in test_PSModDepFind.exec_scripts
    assert 'ansible.module_utils.basic' in test_PSModDepFind.ps_modules


# Generated at 2022-06-12 21:45:46.568153
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    obj = PSModuleDepFinder()
    obj.scan_exec_script('async')
    assert obj.exec_scripts['async'] == b"# -*- coding: utf-8 -*-\n\n\nif __name__ == '__main__':\n    from ansible.module_utils.basic import main\n    main()"



# Generated at 2022-06-12 21:46:10.867169
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    args = dict(name='powershell_exec.ps1')
    result = PSModuleDepFinder().scan_exec_script(**args)
    assert isinstance(result, NoneType)



# Generated at 2022-06-12 21:46:11.866532
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass # test that first is better than second



# Generated at 2022-06-12 21:46:18.966069
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
  from ansible.module_utils.powershell import powershell

  # Arrange
  ps_module_dep_finder = PSModuleDepFinder()
  name = 'WinThrottle'

  # Act
  ps_module_dep_finder.scan_exec_script(name)

  # Assert
  assert 'WinThrottle.ps1' in powershell.powershell_scripts
  assert 'WinThrottle.ps1' in ps_module_dep_finder.exec_scripts



# Generated at 2022-06-12 21:46:26.506566
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # setup
    ps_module_dep_finder = PSModuleDepFinder()
    name = "name"
    ps_module_dep_finder.exec_scripts[name] = "exec_scripts[name]"
    ps_module_dep_finder.scan_module = lambda x, y, z, w: None
    # test
    ps_module_dep_finder.scan_exec_script(name)
    # verify
    assert ps_module_dep_finder.exec_scripts[name] == "exec_scripts[name]"


# Generated at 2022-06-12 21:46:28.888411
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    name = "common"
    finder.scan_exec_script(name)


# Generated at 2022-06-12 21:46:38.474310
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # create a random string for the datastore to avoid potential
    # nameclashes

    var_name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10))
    try:
        del os.environ[var_name]
    except KeyError:
        pass
    x = PSModuleDepFinder()
    x.scan_exec_script("common")
    assert isinstance(getattr(x, "ps_modules", None), dict)
    assert isinstance(getattr(x, "cs_utils_wrapper", None), dict)
    assert isinstance(getattr(x, "cs_utils_module", None), dict)
    assert isinstance(getattr(x, "ps_version", None), type(None))

# Generated at 2022-06-12 21:46:39.457764
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:46:45.709480
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Testing for scan_exec_script method of PSModuleDepFinder class
    # Arrange
    finder = PSModuleDepFinder()
    name = "Invoke-TestModule"
    
    # Act
    finder.scan_exec_script(name)
    
    # Assert
    assert finder.exec_scripts[name]

    # Arrange
    with pytest.raises(AnsibleError) as exception:
        # Act
        finder.scan_exec_script("Test")


# Generated at 2022-06-12 21:46:53.922168
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    depfinder = PSModuleDepFinder()
    depfinder.scan_exec_script('TestModuleExec')

    assert depfinder.exec_scripts['TestModuleExec'] == b'This is a test script with no real value.\n'

    assert depfinder.cs_utils_wrapper['TestModule'] == {'data': b'This is a test c# module\n',
                                                        'path': 'C:\\Users\\cducharme\\Documents\\test_test.psm1'}



# Generated at 2022-06-12 21:47:04.913660
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.executor.powershell.test import mock_ps_mod_find
    module_finder = mock_ps_mod_find.MockPSModuleDepFinder()
    # Testing the below wrapper
    #
    # # Requires -Version {version}
    # # AnsibleRequires -Wrapper {exec_wrapper}
    #
    # # This is a comment
    # # This is also a comment
    #
    # # Requires -Module {module_util_name}
    # function function1 {
    #     return "return function 1"
    # }
    #

# Generated at 2022-06-12 21:47:34.520361
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Create instance of PSModuleDepFinder
    ns = 'ansible_collections.some.namespace'
    col = 'some_collection'
    name = 'some_name'
    fqn = '.'.join([ns, col, name])
    pdm = PSModuleDepFinder()
    # Set module_data as string of Powershell lines

# Generated at 2022-06-12 21:47:45.968872
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mu_dir = 'path/ansible/executor/powershell'
    name = 'ansible'
    try:
        os.makedirs(mu_dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    fp = open(os.path.join(mu_dir, name+'.ps1'), 'w+')
    fp.write('#AnsibleRequires -CSharpUtil ansible_collections.networktoaster.foo.plugins.module_utils.networktoaster')
    fp.close()
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script(name)
    cs_utils_wrapper = dep_finder.cs_utils_wrapper
    exec_scripts = dep_finder.exec_scripts


# Generated at 2022-06-12 21:47:52.348201
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()

    # Test for an existing script
    n_script = to_native("Set-PSNamespace")
    b_script = to_bytes(n_script)
    finder.scan_exec_script(n_script)
    assert b_script in finder.exec_scripts

    # Test for a non-existing script
    n_script = to_native("Ansible.Test.DoesNotExist")
    b_script = to_bytes(n_script)
    try:
        finder.scan_exec_script(n_script)
        assert False, "AnsibleError should be raised"
    except AnsibleError as e:
        assert b_script in to_text(e)


# Generated at 2022-06-12 21:47:54.604455
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script("common_ps")

# Generated at 2022-06-12 21:48:02.747710
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:48:08.114297
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.exec_scripts = {}
    dep_finder.cs_utils_wrapper = {}
    dep_finder.scan_exec_script("exec_wrapper")
    assert(dep_finder.exec_scripts["exec_wrapper"] != b"")
    assert(len(dep_finder.cs_utils_wrapper) > 0)


# Generated at 2022-06-12 21:48:17.182895
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    def _mock_script_data(script_name):
        return ('#Imports -ModuleName Ansible.ModuleUtils.Legacy.AnsibleModuleUtils\n'
                '#Imports -ModuleName Ansible.ModuleUtils.Legacy.ArgumentSpec\n'
                '#Imports -ModuleName Ansible.ModuleUtils.Legacy.Config\n'
                '#Imports -ModuleName Ansible.ModuleUtils.Legacy.Custom\n'
                '#Imports -ModuleName Ansible.ModuleUtils.Legacy.Spec\n'
                '#Imports -ModuleName Ansible.ModuleUtils.Legacy.Type\n'
                '#Imports -ModuleName Ansible.ModuleUtils.Legacy.Utils').encode('utf-8')

    pkgutil_data = pkg

# Generated at 2022-06-12 21:48:23.606552
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils._text import to_bytes
    def _strip_comments(data):
        # Comments start with a #
        # We want to get rid of comments from the data that we send to the
        # remote hosts. Windows PowerShell comments start with a #
        # and can occur anywhere on the line. We allow for a trailing space +
        # comment to keep inline comments aligned with other code.
        return re.sub(to_bytes(r"(\s+)?#.*"), to_bytes(""), data)

    return _strip_comments

# Generated at 2022-06-12 21:48:28.929051
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script('common')

    # expects only 'common.ps1' to be in the list
    assert len(psmdf.exec_scripts) == 1

    # expecting only one dependency which is 'common'
    assert len(psmdf.cs_utils_wrapper) == 1
    assert len(psmdf.ps_modules) == 0
    assert len(psmdf.cs_utils_module) == 0

# test for ansible_collections.ns.coll.plugins.module_utils import in C#

# Generated at 2022-06-12 21:48:36.133904
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script = MagicMock()

    # Validate that scan_module can handle a very large buffer
    data = random.getrandbits(100000000).to_bytes(25000000, byteorder='big')
    dep_finder.scan_module(data=data)
    dep_finder.scan_exec_script.assert_not_called()



# Generated at 2022-06-12 21:48:59.220923
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Initialize the class instance
    module_dep_finder = PSModuleDepFinder()

    name = "test_module"
    dep_finder.scan_exec_script(name)

    assert dep_finder.exec_scripts[name] == "# This is a comment\n"

# Generated at 2022-06-12 21:49:05.860280
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    result_exe_ = "dGVzdCBleGVjdXRvciBzY3JpcHQ="
    result_dep_ = "dGVzdCBEZXBlbmRlbmN5"
    result_exec_data = base64.b64decode(result_exe_)

    mock_name_ = "test_executor_script"
    mock_dep_name = "test Dependency"
    mock_dep_data = base64.b64decode(result_dep_)
    pkgutil.get_data = lambda x1, x2: mock_dep_data

    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script(mock_name_)
    result_data = to_text(dep_finder.exec_scripts[mock_name_])
   

# Generated at 2022-06-12 21:49:14.890042
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    mdf = PSModuleDepFinder()
    # test 1 with builtin PS module_util
    script = b'''using Ansible.ModuleUtils.Common;
using Ansible.ModuleUtils.Powershell;

using System;
using System.Management.Automation;
using System.Management.Automation.Language;
using System.Collections.Generic;
using System.Text;
using System.Globalization;

namespace Ansible.ModuleUtils.PowerShell
{
    public class AnsibleCommonModule : IDisposable
    {
        '''
    mdf.scan_module(script)
    assert 'Ansible.ModuleUtils.Common' in mdf.cs_utils_module.keys()
    assert 'Ansible.ModuleUtils.Powershell' in mdf.cs_utils_module.keys()

# Generated at 2022-06-12 21:49:23.196268
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("test")
    assert(not finder.become)
    assert(finder.ps_version is None)
    assert(finder.os_version is None)
    assert("test" in finder.exec_scripts.keys())
    assert(not len(finder.cs_utils_wrapper))
    assert(not len(finder.cs_utils_module))
    assert(not len(finder.ps_modules))


# Generated at 2022-06-12 21:49:29.485772
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print('test_PSModuleDepFinder_scan_exec_script start')
    psModuleDepFinder = PSModuleDepFinder()
    psModuleDepFinder.scan_exec_script('powershell_wrapper')
    assert psModuleDepFinder.exec_scripts['powershell_wrapper'] is not None
    assert psModuleDepFinder.cs_utils_wrapper['ansible.module_utils.Powershell.Convert'] is not None
    print('test_PSModuleDepFinder_scan_exec_script end')



# Generated at 2022-06-12 21:49:30.484319
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True


# Generated at 2022-06-12 21:49:35.498421
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Configurations
    info = PSModuleDepFinder()
    assert info.exec_scripts == {}

    # Run method
    info.scan_exec_script("script")

    # Assertions
    assert info.exec_scripts == {'script': b''}


# Generated at 2022-06-12 21:49:45.458985
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psm_dep_finder = PSModuleDepFinder(None)
    psm_dep_finder.scan_exec_script('win_ping')
    print("Length of exec_scripts: " + str(len(psm_dep_finder.exec_scripts)))
    assert len(psm_dep_finder.exec_scripts) == 1
    assert psm_dep_finder.exec_scripts['win_ping'] is not None
    print("Length of cs_utils_module: " + str(len(psm_dep_finder.cs_utils_module)))
    assert len(psm_dep_finder.cs_utils_module) == 1
    assert psm_dep_finder.cs_utils_module['ansible_collections.microsoft.windows.plugins.module_utils.win_ping'] is not None

# Generated at 2022-06-12 21:49:54.921102
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Scenario: Test scan_exec_script of class PSModuleDepFinder
    ps_module_dep_finder = PSModuleDepFinder()

    with open("test_data/PSModuleDepFinder/FileToBeScanned.ps1") as fp:
        data = fp.read()

    ps_module_dep_finder.scan_exec_script("Base64")
    assert data == ps_module_dep_finder.exec_scripts["Base64"]
    assert len(ps_module_dep_finder.ps_modules) == 1

    ps_module_dep_finder.scan_exec_script("FileToBeScanned")
    assert data == ps_module_dep_finder.exec_scripts["FileToBeScanned"]
    assert len(ps_module_dep_finder.ps_modules) == 1

    ps_module_

# Generated at 2022-06-12 21:49:57.996292
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    scanner = PSModuleDepFinder()
    scanner.scan_exec_script("async")
    assert scanner.exec_scripts["async"]


# Generated at 2022-06-12 21:50:24.320978
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    # Testing C# module_util 'using Ansible.*;' in a C# module 
    module_util_A_path = os.path.join(C.DEFAULT_MODULE_UTILS_PATH, 'Ansible.ModuleA.cs')
    with open(module_util_A_path, 'rb') as f:
        module_util_A_data = f.read()

    module_util_A_data = module_util_A_data.decode('utf-8').encode('utf-8')
    module_util_B_path = os.path.join(C.DEFAULT_MODULE_UTILS_PATH, 'Ansible.ModuleB.cs')
    with open(module_util_B_path, 'rb') as f:
        module_util_B_data = f.read()

   

# Generated at 2022-06-12 21:50:34.326339
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Creating a test collection with module, for further testing
    test_collection_dir = os.path.join(C.DEFAULT_LOCAL_TMP, u'test_collection')
    try:
        original_umask = os.umask(0o077)
        os.makedirs(test_collection_dir)
        os.umask(original_umask)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    test_collection_module = b'#!/usr/bin/python'

    test_collection_module_util = b'#!/usr/bin/python'

    module_util_name = 'test_module_util'

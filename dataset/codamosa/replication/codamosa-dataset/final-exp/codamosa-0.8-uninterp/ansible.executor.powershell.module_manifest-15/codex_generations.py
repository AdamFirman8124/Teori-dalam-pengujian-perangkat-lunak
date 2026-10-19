

# Generated at 2022-06-12 21:40:58.864071
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('test')

    # Test that it doesn't scan the same script twice
    dep_finder.scan_exec_script('test')
    return dep_finder



# Generated at 2022-06-12 21:41:03.823497
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
	a = PSModuleDepFinder()
	with open('C:/Users/Abel Werka/Ansible_Project/ansible/module_utils/powershell/Invoke-Expression.ps1', 'rb') as f:
		data = f.read()
	a.scan_exec_script(data)

# Generated at 2022-06-12 21:41:14.057714
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    class ModuleDepFinder(object):

        def __init__(self):
            self.exec_scripts = {}
            self.module_utils = {}

    def scan_exec_script(qname):
        if qname not in mdf.exec_scripts.keys():
            raise AnsibleError("Could not find executor powershell script for '%s'" % qname)

    def scan_module(module_data, wrapper=False, powershell=True):
        if powershell:
            if "Ansible.ModuleUtils.Common" not in mdf.module_utils.keys():
                raise AnsibleError('Could not find imported module support code for \'%s\'' % "Ansible.ModuleUtils.Common")

    mdf = ModuleDepFinder()
    mdf.scan_exec_script = scan_exec_script
   

# Generated at 2022-06-12 21:41:27.172095
# Unit test for method scan_module of class PSModuleDepFinder

# Generated at 2022-06-12 21:41:39.158581
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():

    module_data = """#This is a comment
#Requires -Module Ansible.ModuleUtils.foo
#AnsibleRequires -PowerShell ansible_collections.foo.bar.plugins.module_utils.bar
using ansible_collections.foo.bar.plugins.module_utils.bar;
using Ansible.ModuleUtils.foo;"""

    util_data_1 = """#This is a comment
#Requires -Module Ansible.ModuleUtils.bar
#Requires -Version 2.3
#Requires -Version 3.0
#Requires -Version 3.1.1
#Requires -Version 10"""


# Generated at 2022-06-12 21:41:39.782842
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass

# Generated at 2022-06-12 21:41:47.042848
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test for method scan_module
    # test_PSModuleDepFinder_scan_module_1
    config = PSModuleDepFinder()
    config.scan_module(" #Requires -Module Ansible.ModuleUtils.Hyperv.ps1")
    assert config.ps_modules.keys() == ['Ansible.ModuleUtils.Hyperv']

    # test_PSModuleDepFinder_scan_module_2
    config = PSModuleDepFinder()
    config.scan_module(" #Requires -Version 5.1")
    assert config.ps_version == '5.1'

    # test_PSModuleDepFinder_scan_module_2
    config = PSModuleDepFinder()
    config.scan_module(" #Requires -Version 5")
    assert config.ps_version == '5.0'

    # test_PS

# Generated at 2022-06-12 21:41:49.846422
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    instance = PSModuleDepFinder()
    assert instance.scan_exec_script('ansible.module_utils.powershell.files') is None
    assert instance.exec_scripts['ansible.module_utils.powershell.files'] is not None


# Generated at 2022-06-12 21:41:50.851208
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_all_exec_scripts()



# Generated at 2022-06-12 21:41:59.118633
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_obj = PSModuleDepFinder()
    dep_obj.scan_exec_script("test_wrapper")
    assert dep_obj.exec_scripts == {'test_wrapper': b'#Hello World\n#\n#AnsibleRequires -CSharpUtil test_util\n'}
    assert dep_obj.cs_utils_wrapper == {}
    assert dep_obj.cs_utils_module == {}
    assert dep_obj.ps_modules == {}
    assert dep_obj.ps_version is None
    assert dep_obj.os_version is None
    assert dep_obj.become is False



# Generated at 2022-06-12 21:42:16.203075
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psModuleDepFinder = PSModuleDepFinder()
    psModuleDepFinder.scan_exec_script(name)
    assert len(psModuleDepFinder.exec_scripts) > 0


# Generated at 2022-06-12 21:42:22.922294
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    module_data = pkgutil.get_data("ansible.plugins.modules", to_native("my_test_module.psm1"))
    assert module_data is not None

    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_module(module_data)

    # Test the PS module utils
    assert ps_module_dep_finder.ps_modules['Ansible.ModuleUtils.MyUtil'] is not None
    assert ps_module_dep_finder.ps_modules['Ansible.ModuleUtils.MyUtil']['data'].endswith(b'#requires -version 3.0\n')
    assert ps_module_dep_finder.ps_modules['Ansible.ModuleUtils.MyUtil']['path'].endswith

# Generated at 2022-06-12 21:42:32.521403
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    # fail on none existent script
    with pytest.raises(AnsibleError):
        tmp = PSModuleDepFinder()
        tmp.scan_exec_script("this_script_does_not_exist")

    # Check that a simple script adds a dependency
    tmp = PSModuleDepFinder()
    tmp.scan_exec_script("test_exec_script_1")
    assert len(tmp.cs_utils_wrapper) == 1
    assert tmp.cs_utils_wrapper[".Ansible.ModuleUtils.TestUtil"]

    # Check that a nested script adds a dependency
    tmp = PSModuleDepFinder()
    tmp.scan_exec_script("test_exec_script_2")
    assert len(tmp.cs_utils_wrapper) == 2

# Generated at 2022-06-12 21:42:38.915636
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    _test = PSModuleDepFinder()

    _test.scan_exec_script(to_native('TestModuleUtil'))
    _test.scan_exec_script(to_native('TestModuleUtil'))
    assert len(_test.exec_scripts) == 1
    assert 'TestModuleUtil' in _test.ps_modules



# Generated at 2022-06-12 21:42:46.899465
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # We can't test the real data since it's located in a different file. Instead since
    # the whole point of this method is to generate a random number based on the content
    # of the provided module, we mock the random module to return a predefined value
    # everytime it is called.
    # We also need to mock the pkgutil.get_data to return the content of a mocked file.
    with patch('ansible.module_utils.basic.randint', side_effect=lambda *args: 123), \
         patch('pkgutil.get_data', return_value=b'') as mock_pkgutil:
        # We need to create our own PSModuleDepFinder object so we can look into its content
        # to see if scan_exec_script did it's job.
        dep_finder = PSModuleDepFinder()
        dep_finder

# Generated at 2022-06-12 21:42:49.291472
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    scanner = PSModuleDepFinder()
    result = scanner.scan_exec_script('script.ps1')
    assert result



# Generated at 2022-06-12 21:42:51.122779
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False  # TODO: implement your test here


# Generated at 2022-06-12 21:42:55.812907
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Get the object from the resource file
    pmdf = PSModuleDepFinder()
    pmdf.scan_exec_script('example')
    assert pmdf.exec_scripts['example'] == '#!/usr/bin/python\n\nprint "Hello World!"\n'

# Generated at 2022-06-12 21:43:01.483930
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('PsExec')
    assert 'PsExec' in dep_finder.exec_scripts
    assert 'FileTransferUtil' in dep_finder.ps_modules
    assert 'ConnectionUtil' in dep_finder.ps_modules


# Generated at 2022-06-12 21:43:11.592637
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import mock
    import os.path
    from ansible.module_utils.powershell.executor import PSModuleDepFinder

    get_data_mock = mock.MagicMock()
    get_data_mock.side_effect = Exception("Module \"ansible.executor.powershell\" has no attribute \"%s\"" % ps_script)
    with mock.patch("ansible.module_utils.powershell.executor.pkgutil.get_data", side_effect=get_data_mock):
        dep_finder = PSModuleDepFinder()
        with pytest.raises(Exception) as excinfo:
            dep_finder.scan_exec_script(ps_script)
        assert "Could not find executor powershell script" in str(excinfo)


# Generated at 2022-06-12 21:43:49.978683
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_dict = {
        'exec_scripts': {'moduletest': b'# foo bar\nfunction bar {\n\t# test'},
        'cs_utils_wrapper': {'Ansible.ModuleBase': {'data': b'# foo\nfunction foobar {',
                                                    'path': u'/path/to/Ansible.ModuleBase.cs'}},
    }
    test_obj = PSModuleDepFinder()
    for k, v in test_dict.items():
        setattr(test_obj, k, v)
    name = 'moduletest'
    test_obj.scan_exec_script(name)
    assert name not in test_obj.exec_scripts
    assert 'Ansible.ModuleBase' not in test_obj.cs_utils_wrapper


# Generated at 2022-06-12 21:43:57.981892
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    # noinspection PyUnresolvedReferences
    from ansible.module_utils.common.collections import AnsibleCollectionRef
    from ansible.module_utils.powershell._ansible_module import AnsibleModule
    from ansible.parsing.splitter import parse_kv
    from ansible.plugins.executor.powershell import default_wrapper
    from ansible.utils.display import Display
    from ansible.utils.encrypt import do_encrypt
    import ansible

    d = PSModuleDepFinder()

    # try to load a script that doesn't exist in the module_util dir
    with pytest.raises(AnsibleError) as context:
        d.scan_exec_script('foo')
    assert "Could not find executor powershell script for 'foo'" in str(context.value)

    # get

# Generated at 2022-06-12 21:44:02.404172
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    """
    Get a wrapper for the "test_PSModuleDepFinder_scan_module" function
    """
    test_PSModuleDepFinder_scan_module.__wrapped__ = _test_PSModuleDepFinder_scan_module
    return test_PSModuleDepFinder_scan_module

# Generated at 2022-06-12 21:44:13.347468
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # test an executor wrapper
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("executor")

    assert dep_finder.ps_modules
    assert "Ansible.ModuleUtils.Common" in dep_finder.ps_modules
    assert "Ansible.ModuleUtils.Powershell.Convert" in dep_finder.ps_modules

    assert dep_finder.cs_utils_wrapper
    assert "Ansible.Common.Logging" in dep_finder.cs_utils_wrapper

    # test Get-ConnectionInfo executor wrapper
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("Get-ConnectionInfo")

    assert "Ansible.ModuleUtils.Common" in dep_finder.ps_modules

# Generated at 2022-06-12 21:44:26.284231
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class module:
        def __init__(self):
            self.data = {}

    my_module = module()
    my_PSModuleDepFinder = PSModuleDepFinder()
    my_PSModuleDepFinder.cs_utils_module = {
        'ansible_collections.my_collection.my_module_utils.my_module_util.cs': {
            'data': b'',
            'path': 'my_module_util.cs'
        }
    }
    my_PSModuleDepFinder.cs_utils_wrapper = {
        'ansible_collections.my_collection.my_module_utils.my_module_util.cs': {
            'data': b'',
            'path': 'my_module_util.cs'
        }
    }
    my_PSModuleDepFinder

# Generated at 2022-06-12 21:44:40.027802
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:44:45.369577
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # create an instance of the class PSModuleDepFinder
    c = PSModuleDepFinder()
    # call the method scan_exec_script of the PSModuleDepFinder object instance
    
    c.scan_exec_script("script_name.ps1")
    # check that all the values in the instance of the inline class PSModuleDepFinder are correct
    assert c.exec_scripts == {}


# Generated at 2022-06-12 21:44:50.556839
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # define type of self
    self_type = PSModuleDepFinder()
    # call method
    result = self_type.scan_exec_script()
    # validate results
    assert result is not None
    assert isinstance(result, PSModuleDepFinder)

# Generated at 2022-06-12 21:44:59.528181
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    script = to_text(b"#AnsibleRequires -PowerShell 1.1\n#AnsibleRequires -CSharpUtil Util2\n#AnsibleRequires -Wrapper Util3\n")
    psmdf.scan_exec_script("Util1")
    assert(len(psmdf.ps_modules) == 0)
    assert(len(psmdf.cs_utils_wrapper) == 0)
    assert(len(psmdf.exec_scripts) == 1)
    assert(to_text(psmdf.exec_scripts["Util1"]) == script)


# Generated at 2022-06-12 21:45:10.509067
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test with test payload
    finder = PSModuleDepFinder()
    finder.scan_module(b"#Requires -Module Ansible.ModuleUtils.Legacy.Facts")
    assert finder.ps_modules
    assert ansible_collections.ansible.builtin in finder.ps_modules
    assert "ModuleUtils.Legacy.Facts" in finder.ps_modules[ansible_collections.ansible.builtin]
    # Test with test payload
    finder = PSModuleDepFinder()
    finder.scan_module(b"#AnsibleRequires -PowerShell Ansible.ModuleUtils.Legacy.Facts")
    assert finder.ps_modules
    assert ansible_collections.ansible.builtin in finder.ps_modules

# Generated at 2022-06-12 21:45:27.345163
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False # add real tests


# Generated at 2022-06-12 21:45:38.292407
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    for pardir in os.listdir(os.path.join(C.DEFAULT_LOCAL_TMP, 'test1')):
        libdir = os.path.join(C.DEFAULT_LOCAL_TMP, 'test1', pardir, 'lib')
        if os.path.exists(libdir):
            break
    a = PSModuleDepFinder()
    a.scan_exec_script('Test1')
    assert a.exec_scripts['Test1'] == b'if(1)\n'
    assert a.ps_modules == {}
    assert a.cs_utils_wrapper == {}
    assert a.cs_utils_module == {}
    assert a.ps_version is None
    assert a.os_version is None
    assert not a.become
    # Unit test for method scan_module of class PS

# Generated at 2022-06-12 21:45:45.146405
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    data = b"#Requires -Module Ansible.ModuleUtils.One\n" \
           b"#AnsibleRequires -PowerShell Ansible.ModuleUtils.Two"
    finder = PSModuleDepFinder()
    finder.scan_module(data)
    assert(set(finder.ps_modules.keys()) == set(['Ansible.ModuleUtils.One', 'Ansible.ModuleUtils.Two']))

    # Should not require UniqueId here
    data = b"#Requires -Module Ansible.ModuleUtils.One\n" \
           b"#AnsibleRequires -PowerShell Ansible.ModuleUtils.Two"
    finder = PSModuleDepFinder()
    finder.ps_version = "3.0"
    finder.scan_module(data)

# Generated at 2022-06-12 21:45:48.372289
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import ansible.executor.powershell
    finder = PSModuleDepFinder()
    finder.scan_exec_script('my_script')
    assert(finder.exec_scripts['my_script'] == to_bytes(pkgutil.get_data("ansible.executor.powershell", "my_script.ps1")))



# Generated at 2022-06-12 21:45:51.649089
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    name = "test"
    finder.scan_exec_script(name)
    assert finder.exec_scripts.__contains__(name)

# Generated at 2022-06-12 21:45:52.935376
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import pytest

    assert False, "TBD"

    #test_PSModuleDepFinder_scan_exec_script()


# Generated at 2022-06-12 21:46:01.869426
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    name =  "windows"
    data = "this is the data"
    pkgutil.get_data.return_value = data
    psmdf = PSModuleDepFinder()
    psmdf.ps_modules = {"name": {"data": "old data", "path": "old path"}}
    psmdf.cs_utils_wrapper = {"name": {"data": "old data", "path": "old path"}}
    psmdf.scan_exec_script(name)
    assert psmdf.exec_scripts[name] is not None
    assert not pkgutil.get_data.called
    assert not psmdf.scan_module.called


# Generated at 2022-06-12 21:46:10.755634
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Add your own test methods below
    # make sure test methods have a descriptive name and start with test_

    # This is the content of the A.ps1 script
    # #AnsibleRequires -Wrapper B

    # This is the content of the B.ps1 script
    # #Requires -Module C

    # This is the content of the C.ps1 script
    # #AnsibleRequires -PowerShell D
    # #AnsibleRequires -CSharpUtil E

    # This is the content of the E.cs script
    # using F;

    A_data = b"#AnsibleRequires -Wrapper B\n"
    B_data = b"#Requires -Module C\n"

# Generated at 2022-06-12 21:46:13.253535
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    assert ps_module_dep_finder.scan_exec_script('powershell_base') != None


# Generated at 2022-06-12 21:46:23.092786
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    data1 = "#AnsibleRequires -Powershell ansible_collections.foo.bar.plugins.module_utils.baz, ansible.module_utils.common"
    data2 = "#AnsibleRequires -CSharpUtil ansible_collections.foo.bar.plugins.module_utils.boo, ansible.module_utils.common"

    def _load_data(data2):
        return [
            {'name': 'ansible_collections.foo.bar.plugins.module_utils.baz.psm1', 'data': data1},
            {'name': 'ansible_collections.foo.bar.plugins.module_utils.boo.cs', 'data': data2},
        ]


# Generated at 2022-06-12 21:46:43.838803
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # PSModuleDepFinder: tests scan_exec_script
    # Ensure the method works as expected
    default_test_data = {'data': bytearray(b'module_utils = {}\n'), 'path': 'test_path'}
    m = PSModuleDepFinder()
    m.ps_modules = dict()
    m.exec_scripts = dict()
    m.scan_exec_script('test_script')
    assert m.ps_modules == default_test_data
    assert m.exec_scripts == {'test_script': b'#'}



# Generated at 2022-06-12 21:46:51.008414
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.playbook.play_context import PlayContext
    play_context = PlayContext()
    args = dict(
        _execute_module=dict(msg='execute module handler'),
    )
    ps_mdf = PSModuleDepFinder()
    '''
    Assert that ps_mdf.exec_scripts dictionary is empty before calling the scan_exec_script function
    '''
    assert len(ps_mdf.exec_scripts) == 0
    '''
    Assert that ps_mdf.exec_scripts dictionary is not empty after calling the scan_exec_script function with
    valid arguments
    '''
    ps_mdf.scan_exec_script('hyperv_ps_exec')
    assert len(ps_mdf.exec_scripts) != 0

# Generated at 2022-06-12 21:47:02.846453
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:47:10.297750
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils._text import to_bytes

    mock_get_data = Mock()
    mock_get_data.side_effect = [
        to_bytes('#requires -version 3.0\n#requires -module Ansible.ModuleUtils.Foo.Bar'),
        to_bytes('#requires -version 4.0\n#requires -module Ansible.ModuleUtils.Baz.Qux')
    ]
    psmdf = PSModuleDepFinder()
    psmdf._add_module = Mock()
    psmdf.cs_utils_wrapper = dict()

# Generated at 2022-06-12 21:47:16.744801
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.facts.common import FactsCommon
    from ansible.module_utils.facts.system.platform import OpenBSDPlatform
    from ansible.module_utils.facts.system.distribution import OpenBSDDistribution

    fqcr = "ansible.module_utils.facts.system.platform.OpenBSDPlatform"
    util = resource_from_fqcr(fqcr)
    util_path = util.find(OpenBSDPlatform())

    with open(util_path) as f:
        data = f.read()

    module_finder = PSModuleDepFinder()
    module_finder.scan_exec_script(OpenBSDPlatform)
    assert len(module_finder.exec_scripts) == 2  # 1 root, 1 OpenBSD
    # we need to pop the root one to

# Generated at 2022-06-12 21:47:25.639926
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    from ansible.module_utils.psmodule_common import PSModuleDepFinder
    from tempfile import mkstemp
    import os
    import ansible.module_utils.common.params as p
    
    def test(name, source_code, dependencies, not_dependencies):
        path = mkstemp(suffix=".ps1")
        with os.fdopen(path[0], 'wb') as f:
            f.write(source_code)
            f.close()
        finder = PSModuleDepFinder()
        finder.scan_module(source_code)
        assert(sorted(finder.ps_modules.keys()) == sorted(dependencies))
        assert(sorted(finder.cs_utils_module.keys()) == sorted(dependencies))

# Generated at 2022-06-12 21:47:29.362673
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mdf = PSModuleDepFinder()
    mdf.scan_exec_script("Common")
    assert mdf.exec_scripts["Common"].startswith(b"#\r\n$script_type = 'exec'")
    assert mdf.ps_modules["Ansible.ModuleUtils.Common"]["path"].endswith("Ansible.ModuleUtils.Common.psm1")



# Generated at 2022-06-12 21:47:42.845696
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psModuleDepFinder = PSModuleDepFinder()
    psModuleDepFinder.scan_exec_script('ansible_powershell')
    assert 'ansible_powershell' in psModuleDepFinder.exec_scripts
    assert 'module_name' in psModuleDepFinder.exec_scripts['ansible_powershell']
    assert 'TypeName' in psModuleDepFinder.exec_scripts['ansible_powershell']
    assert 'CommandType' in psModuleDepFinder.exec_scripts['ansible_powershell']
    assert 'ArgumentList' in psModuleDepFinder.exec_scripts['ansible_powershell']
    assert 'ansible_powershell' in psModuleDepFinder.ps_modules
    assert 'ansible_powershell' in psModuleDepFinder.cs_utils_wrapper

# Generated at 2022-06-12 21:47:44.209356
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    assert False, "Test was not implemented, but marked as complete"


# Generated at 2022-06-12 21:47:51.778347
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    def check_utils_referenced(finder, utils):
        for util in utils:
            if util not in finder.ps_modules.keys():
                return False

        return True

    finder = PSModuleDepFinder()
    module_fqn = to_native("ansible_collections.community.general.plugins.modules.debug")
    module_source = resource_from_fqcr(module_fqn)

    finder.scan_module(module_source, fqn=module_fqn, wrapper=False, powershell=True)

    ps_utils = [
        to_native("Ansible.ModuleUtils.Legacy.String"),
        to_native("ansible_collections.community.general.plugins.module_utils.basic.logger"),
    ]

# Generated at 2022-06-12 21:48:09.115708
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible import constants as C
    C.DEFAULT_DEBUG = True
    obj = PSModuleDepFinder()
    obj.scan_exec_script("test_name")

# Unit tests for class PSModuleDepFinder
# TODO: Add unit tests


# Generated at 2022-06-12 21:48:14.337309
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psModuleDepFinder = PSModuleDepFinder()
    psModuleDepFinder.scan_exec_script("Basic")

    # check that the executor powershell script was loaded
    assert isinstance(psModuleDepFinder.exec_scripts["Basic"], str)

    # check that the executor powershell script didn't have any dependencies
    assert len(psModuleDepFinder.ps_modules.keys()) == 0 


# Generated at 2022-06-12 21:48:16.633285
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script('_json')
    psmdf.scan_exec_script('_text')


# Generated at 2022-06-12 21:48:22.371751
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Setup
    psd = PSModuleDepFinder()
    psd.scan_exec_script('PowershellExecutor')

    # Test
    assert len(psd.exec_scripts.keys()) == 1
    
    psd.scan_exec_script('PowershellExecutor')

    # Test
    assert len(psd.exec_scripts.keys()) == 1
    assert psd.exec_scripts['PowershellExecutor'] is not None


# Generated at 2022-06-12 21:48:30.515498
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
   # This is used to test scan_module() of class PSModuleDepFinder
    # Make sure the present working directory is not included in the search path.
    old_path = copy.deepcopy(sys.path)
    old_cwd = os.getcwd()
    tmpdir = tempfile.mkdtemp()
    os.chdir(tmpdir)

    # Replace the module loader.
    mp = sys.modules['ansible.plugins.loader']
    mp.module_loader = ps_module_utils_loader

    # Make a fake module.

# Generated at 2022-06-12 21:48:33.090865
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    obj = PSModuleDepFinder()
    name = ""
    assert obj.scan_module(name) == ''


# Generated at 2022-06-12 21:48:36.635222
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_object = PSModuleDepFinder()
    args = []
    if len(args) == 1:
        test_object.scan_exec_script(*args)


# Generated at 2022-06-12 21:48:37.773736
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass



# Generated at 2022-06-12 21:48:38.722586
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    fixture = PSModuleDepFinder()

    assert fixture.scan_exec_script("ansible_powershell_common") == None



# Generated at 2022-06-12 21:48:47.693688
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # Test params
    # Input fqn is None, wrapper is False, powershell is True
    # Expected:
    # 1. Output ps_modules contains key "Ansible.ModuleUtils.{name}"
    # 2. No error occurs
    module_data = '#Requires -Module Ansible.ModuleUtils.{name}\n'.encode('utf8')
    psmodule_dep_finder = PSModuleDepFinder()
    psmodule_dep_finder.scan_module(module_data, None, False, True)
    ps_modules = psmodule_dep_finder.ps_modules
    assert 'Ansible.ModuleUtils.{name}' in ps_modules

    # Test params
    # Input fqn is None, wrapper is False, powershell is True
    # Expected:
    # 1. Output ps_

# Generated at 2022-06-12 21:49:02.963481
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass



# Generated at 2022-06-12 21:49:04.240042
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    result = PSModuleDepFinder().scan_exec_script("test")



# Generated at 2022-06-12 21:49:11.741932
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    psmodule_dep_finder_object = PSModuleDepFinder()
    module_name = 'test_module'
    exec_script = mock_open(read_data=b'#AnsibleRequires -Powershell Ansible.ModuleUtils.test_module\n')
    # Using mock_open to simulate open() builtin
    with patch('ansible.module_utils.powershell.PSModuleDepFinder.open', exec_script, create=True) as mo:
        # Using mock_open to simulate open() builtin
        with patch('ansible.module_utils.powershell.PSModuleDepFinder.scan_module', return_value=True):
            psmodule_dep_finder_object.scan_exec_script(module_name)
            exec_script_content = exec_script().readlines()
            assert exec_script_

# Generated at 2022-06-12 21:49:18.526297
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    post_data = {
        'first_name': 'John',
        'age': '35',
        'user_id': '123123123123123123123',
    }
    assert post_data['user_id'] == '123123123123123123123'
#   p = PSModuleDepFinder()
#   assert p.scan_exec_script('name') == exception

# Generated at 2022-06-12 21:49:22.855829
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    x = PSModuleDepFinder()
    assert x.exec_scripts == {}
    x.scan_exec_script(to_text('ScriptFullPath'))
    assert set(x.exec_scripts.keys()) == {to_text('ScriptFullPath')}


# Generated at 2022-06-12 21:49:27.640985
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Path of the Ansible module
    module_path = os.path.join(os.getcwd(), 'test/sanity/ps_invocation_test/test_module.py')
    # Path of the Ansible modules module_utils
    # module_utils_path = os.path.join(os.getcwd(), 'test/sanity/ps_invocation_test/test_module_utils.psm1')
    # Pls change the path of the test module utils
    # module_utils_path = os.path.join(os.getcwd(), 'test/sanity/ps_invocation_test/module_utils_test.psm1')
    scanner = PSModuleDepFinder()
    scanner.scan_exec_script("win_exec_wrapper")
    # scanner.scan_module(module_data=open

# Generated at 2022-06-12 21:49:37.805954
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Get a class instance first.
    obj = PSModuleDepFinder()
    # Try to load powershell module named Microsoft.PowerShell.Core (which exists).
    obj.scan_exec_script('Microsoft.PowerShell.Core')
    # Make sure it exists and contains some data.
    assert 'Microsoft.PowerShell.Core' in obj.exec_scripts
    assert obj.exec_scripts['Microsoft.PowerShell.Core'] != b''
    # Try to load powershell module named asdfasdfsadf (which does not exist).
    try:
        obj.scan_exec_script('asdfasdfsadf')
    except Exception as e:
        assert type(e) == AnsibleError


# Generated at 2022-06-12 21:49:42.744189
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Check some smoke cases
    data = to_bytes(b"foo")
    assert not PSModuleDepFinder().scan_exec_script(data)

    # Check that the returned powershell script is correctly removed from comments
    ps_script = b"# this is a comment\nTest-True"
    assert _strip_comments(ps_script) == b"Test-True"



# Generated at 2022-06-12 21:49:43.400737
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:49:44.450364
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass



# Generated at 2022-06-12 21:50:05.224592
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    class TestModule:
        def __init__(self, *args, **kwargs):
            self.options = []

    class TestConnection:
        def __init__(self, *args, **kwargs):
            self.options = []

    class TestAnsibleModule(object):
        def __init__(self, *args, **kwargs):
            self.fail_json = self.exit_json = lambda *x, **y: None

    class TestAnsibleConnection(object):
        def __init__(self, *args, **kwargs):
            self.close = lambda: None
            self.get_option = self.set_option = lambda *x, **y: None

    class TestAnsiblePlaybook(object):
        def __init__(self, *args, **kwargs):
            self.exit_json

# Generated at 2022-06-12 21:50:17.448952
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    class MockAnsibleError:
        pass

    class MockLooseVersion:
        @staticmethod
        def __new__(cls, *args, **kwargs):
            return object()

    class MockRe:
        @staticmethod
        def compile(*args, **kwargs):
            return object()

        @staticmethod
        def match(*args, **kwargs):
            return object()

    class MockPkgutil:
        @staticmethod
        def get_data(*args, **kwargs):
            return object()

    class MockOs:
        @staticmethod
        def path(path):
            return '.'.join(path.split(os.path.sep))

        @staticmethod
        def join(*args):
            return os.path.join(*args)


# Generated at 2022-06-12 21:50:18.905173
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("test")



# Generated at 2022-06-12 21:50:28.212981
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Initialize a few needed variables
    module_data = to_bytes("This string contains a pattern match")
    ext = ".txt"
    fqn = "test_collection.test_module"
    optional = False

    # Create a PSModuleDepFinder instance
    dep_finder = PSModuleDepFinder()

    # Call the method we actually want to test
    dep_finder._add_module("ansible_module_parsing.psm1", ext, fqn, optional)

    # Check the results
    assert dep_finder.ps_modules['ansible_module_parsing'] is not None

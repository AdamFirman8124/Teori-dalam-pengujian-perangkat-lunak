

# Generated at 2022-06-12 21:40:57.395960
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert True


# Generated at 2022-06-12 21:41:03.267107
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # set up test
    class Test():
        def __init__(self, name):
            self.name = name
            self.ps_modules = dict()
            self.exec_scripts = dict()
            self.cs_utils_wrapper = dict()
            self.cs_utils_module = dict()
            self.ps_version = None
            self.os_version = None
            self.become = False
    ps = Test("test")
    random_string = "".join(chr(random.randint(0, 255)) for i in range(100))

    # Positive tests
    ps.scan_exec_script("test")
    assert to_native(ps.exec_scripts['test']) == to_native(random_string)

# Generated at 2022-06-12 21:41:04.219024
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:41:09.236489
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script('dummy')
    assert ps_module_dep_finder.exec_scripts['dummy'] == b'function Dummy { return "Dummy" }'


# Generated at 2022-06-12 21:41:17.069875
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # test with a valid PowerShell file
    ps_module = 'Ansible.ModuleUtils.SqlServer.SqlServer.psm1'
    ps_module_data = _slurp(ps_module_utils_loader.find_plugin(ps_module))
    ps_module_data = to_bytes(ps_module_data)
    finder = PSModuleDepFinder()
    finder.scan_module(ps_module_data)
    assert set(finder.ps_modules.keys()) == {'Ansible.ModuleUtils.SqlServer.SqlServer.psm1'}
    assert finder.ps_modules['Ansible.ModuleUtils.SqlServer.SqlServer.psm1']['path'].endswith(ps_module)

# Generated at 2022-06-12 21:41:19.596584
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    p = PSModuleDepFinder()
    p.scan_exec_script("powershell")
    return p



# Generated at 2022-06-12 21:41:21.234297
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # TODO: Implement
    return True


# Generated at 2022-06-12 21:41:24.522449
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_object = PSModuleDepFinder()
    test_object.scan_exec_script("powershell-rest-mock")
    assert True

# Generated at 2022-06-12 21:41:37.627361
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    def _strip_comments(data):
        # strip out comments
        return re.sub(to_bytes(r'(?m)^\s?#.*\n?'), b'', data, flags=re.MULTILINE)

    def _slurp(path):
        # helper method to slurp in a files contents
        with open(path, 'rb') as f:
            return f.read()

    # Test to ensure that when the module_util is not found, an error is thrown
    finder = PSModuleDepFinder()
    try:
        finder.scan_exec_script("test_not_found")
        assert False, "An AnsibleError was not raised when trying to scan a " \
                      "powershell exec script that does not exist"
    except AnsibleError:
        pass

    # Test to ensure that

# Generated at 2022-06-12 21:41:40.102643
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("ansible_powershell_wrapper")
    assert finder.exec_scripts["ansible_powershell_wrapper"].strip().decode("utf-8").startswith("<#")



# Generated at 2022-06-12 21:41:56.041965
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    pass

# Generated at 2022-06-12 21:42:03.224768
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils._text import to_bytes
    psmdf = PSModuleDepFinder()
    psmdf.scan_exec_script(name='PowershellCredentialsFactory')

    assert 'PowershellCredentialsFactory' in psmdf.exec_scripts.keys()

    data = psmdf.exec_scripts['PowershellCredentialsFactory']

# Generated at 2022-06-12 21:42:08.681117
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # This test requires that a collection with the name test_namespace
    # containing a module_utils named test_util.py be in the path when
    # the test is run.

    class TempPaths(object):
        # Temporarily append a path to a global variable and then remove it
        # for cleanup

        def __init__(self, variable, path):
            self.variable = variable
            self.path = path
            self.orig_value = getattr(C, variable)

        def __enter__(self):
            new_value = self.orig_value + [self.path]
            setattr(C, self.variable, new_value)

        def __exit__(self, exc_type, exc_val, exc_tb):
            setattr(C, self.variable, self.orig_value)


# Generated at 2022-06-12 21:42:09.340705
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    assert False

# Generated at 2022-06-12 21:42:11.909628
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    ps_module_dep_finder = PSModuleDepFinder()
    ps_module_dep_finder.scan_exec_script('NetUtil')

    assert 'RandomStringGenerator' in ps_module_dep_finder.cs_utils_wrapper
    assert 'RandomStringGenerator' in ps_module_dep_finder.cs_utils_module

# Generated at 2022-06-12 21:42:15.412769
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Instantiate the class
    mdf = PSModuleDepFinder()
    # test for 'powershell_script'
    mdf.scan_exec_script('powershell_script')
    # test for 'powershell_wrapper'
    mdf.scan_exec_script('powershell_wrapper')
    # test for 'powershell_module_utils'
    mdf.scan_exec_script('powershell_module_utils')
    assert True


# Generated at 2022-06-12 21:42:19.059098
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """
    Test the case where there is no executor powershell script found.
    This is tested by providing a name of "pow.ps1" which doesn't exist.
    """
    test = PSModuleDepFinder()
    try:
        test.scan_exec_script("pow")
        assert False, "Expected test to raise AnsibleError"
    except AnsibleError as e:
        assert e.message == "Could not find executor powershell script for 'pow'"


# Generated at 2022-06-12 21:42:21.294508
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    #
    # This is a stub to test `ansible.module_utils.basic.PSModuleDepFinder.scan_exec_script`.
    #
    # Replace with a valid test when the method is implemented.
    #
    assert True


# Generated at 2022-06-12 21:42:22.516565
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    print('This test unit needs to be implemented')

# Generated at 2022-06-12 21:42:27.457749
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import ansible.executor.powershell
    psmdf = PSModuleDepFinder()
    assert isinstance(psmdf, PSModuleDepFinder)
    psmdf.scan_exec_script('base')
    assert psmdf.exec_scripts
    data = pkgutil.get_data("ansible.executor.powershell", "base.ps1")
    assert data


# Generated at 2022-06-12 21:42:52.596228
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    module_path = str(b64_decode(b'Ly9QYXRoVG9Nb2R1bGUKLy9UZXN0UHJvY2Vzc1N0YXJ0'))
    module_path = module_path.replace('\\', '/')
    psm1_data = pkgutil.get_data(module_path, "TestModule.psm1")
    tp = TestParams(psm1_data)
    assert tp.ps_version == "5.1"
    assert tp.os_version == "10.0.17134"
    assert tp.become

# Generated at 2022-06-12 21:43:04.779487
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
   path = os.path.dirname(os.path.realpath(__file__))
   file_name = path + "\\test_PSModuleDepFinder.py"
   test_file1 = file_name.replace('\\', '\\\\')
   exec_script_path = path + "\\exec_script.ps1"
   exec_script_path1 = exec_script_path.replace('\\', '\\\\')
   exec_script_data = _slurp(exec_script_path)
   text = exec_script_data
   base64_str = base64.b64encode(text)
   base64_str1 = base64_str.decode('utf-8')
   test_file_data = _slurp(test_file1)

# Generated at 2022-06-12 21:43:13.994080
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    import ansible.executor.powershell
    import ansible.executor.powershell.common

    # Pass when powershell script successfully read from
    # "ansible/executor/powershell/common.ps1"
    assert ansible.executor.powershell.common.__loader__.get_data("ansible/executor/powershell/common.ps1") is not None

    # Pass when powershell script successfully read from
    # "ansible/executor/powershell/common.ps1"
    assert ansible.executor.powershell.common.__loader__.get_data("ansible/executor/powershell/common.ps1") is not None

    # Pass when powershell script successfully read from
    # "ansible/executor/powershell/common.ps1"
    assert ansible.executor.powershell

# Generated at 2022-06-12 21:43:18.194680
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    string_data = b'''# This is some data
#Requires -Module Ansible.ModuleUtils.{name}
#Requires -Module Ansible.ModuleUtils.Foo
#AnsibleRequires -CSharpUtil Ansible.ModuleUtils.Foo
#Other
        '''
    x = PSModuleDepFinder()
    x.scan_module(string_data)

    assert x.ps_modules == {'Ansible.ModuleUtils.Foo': {}}
    assert x.cs_utils_module == {'Ansible.ModuleUtils.Foo': {}}


# Generated at 2022-06-12 21:43:20.669897
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    data = PSModuleDepFinder().scan_exec_script("powershell_lib")
    assert data is None


# Generated at 2022-06-12 21:43:25.581525
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """Test that PowerShell executor script scan works as expected"""
    md = PSModuleDepFinder()
    md.scan_exec_script('testscript')
    assert 'testscript' in md.exec_scripts
    assert 'testscript' in md.ps_modules
    assert 'Ansible.ModuleUtils.Foo' in md.ps_modules



# Generated at 2022-06-12 21:43:29.122351
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()

    dep_finder.scan_exec_script('GetPSVersion')
    assert 'GetPSVersion' in dep_finder.exec_scripts
    assert 'GetOSVersion' in dep_finder.exec_scripts



# Generated at 2022-06-12 21:43:40.628049
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    fake_meta_output = b'#! /usr/bin/python\n{}\n'
    fake_wrapper_output = b'#! /usr/bin/python\n{}\n'
    csmd = PSModuleDepFinder()
    csmd.scan_exec_script('fake_wrapper_1')
    assert fake_wrapper_output.format('"somestring"').replace(b'\n', b'') == csmd.exec_scripts['fake_wrapper_1'].replace(b'\n', b'')
    assert {} == csmd.cs_utils_wrapper
    assert {} == csmd.ps_modules
    csmd.scan_exec_script('fake_wrapper_2')

# Generated at 2022-06-12 21:43:51.346792
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    mdf = PSModuleDepFinder()
    if not mdf:
        raise AssertionError("Expected the PSModuleDepFinder object to be True, but got False.")

    if not mdf.ps_modules or mdf.ps_modules is None:
        raise AssertionError("ps_modules was expected to be a non-empty dict, but got None.")

    if not mdf.cs_utils_wrapper or mdf.cs_utils_wrapper is None:
        raise AssertionError("cs_utils_wrapper was expected to be a non-empty dict, but got None.")

    if not mdf.cs_utils_module or mdf.cs_utils_module is None:
        raise AssertionError("cs_utils_module was expected to be a non-empty dict, but got None.")


# Generated at 2022-06-12 21:43:58.627620
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import inspect
    import sys
    import types

    finder = PSModuleDepFinder()
    finder.scan_exec_script("pwsh.exe")
    finder.scan_exec_script("powershell-6.exe")

    def decorator(*decorator_args):
        def wrapper(*ps_scripts):
            def test():
                passes = 0
                fails = 0
                print("Testing %s" % func.__name__)

# Generated at 2022-06-12 21:44:17.187521
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    data = pkgutil.get_data("ansible.executor.powershell", "ansible_distribution.ps1")
    finder = PSModuleDepFinder()
    finder.scan_exec_script("ansible_distribution")
    assert data.strip() == finder.exec_scripts["ansible_distribution"].strip()


# Generated at 2022-06-12 21:44:18.646085
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    util = PSModuleDepFinder()
    assert util.scan_exec_script(name="pscon") == "PSCON"
    assert util.scan_exec_script(name="pip") == "PIP"



# Generated at 2022-06-12 21:44:30.412472
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import sys
    if sys.version_info[0] == 2:
        import __builtin__ as builtins
    else:
        import builtins
    builtins.__dict__['__salt__'] = {'config.get': lambda *args: None}
    import ansible.executor.powershell.module_utils.powershell as ps
    ps.__salt__ = {'config.get': lambda *args: None}
    ansible_collections = {'test_collection': {'plugins': {'module_utils': {'test_util': {'__init__.py': '', 'test_util.psm1': ''}}}}}

# Generated at 2022-06-12 21:44:43.253426
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    assert finder.exec_scripts == {}
    assert finder.ps_modules == {}
    assert finder.cs_utils_wrapper == {}

    # Test a builtin script
    finder.scan_exec_script('script')
    assert len(finder.exec_scripts) == 1
    assert len(finder.ps_modules) == 1
    assert len(finder.cs_utils_wrapper) == 0
    assert finder.exec_scripts['script']
    assert 'script' in finder.ps_modules

    # Test a custom script
    finder = PSModuleDepFinder()
    finder.scan_exec_script('custom-script')
    assert len(finder.exec_scripts) == 1
    assert len(finder.ps_modules) == 1

# Generated at 2022-06-12 21:44:55.529776
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test for method scan_exec_script of class PSModuleDepFinder
    # return value of set() is not tested
    res = PSModuleDepFinder()
    # Testing for module_data is None
    try:
        res.scan_exec_script(None)
        assert False, "test_PSModuleDepFinder_scan_exec_script: Must raise an exception if module_data is None."
    except TypeError:
        assert True
        return  # exit because of test failure
    # Testing for module_data is not None but bad value
    try:
        res.scan_exec_script(0)
        assert False, "test_PSModuleDepFinder_scan_exec_script: Must raise an exception if module_data is bad."
    except TypeError:
        assert True
        return  # exit because of test failure
    #

# Generated at 2022-06-12 21:45:01.648520
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    params = {
        'module_data': b'\nI am a module',
        'fqn': b'ansible.builtin.assert',
        'wrapper': False,
        'powershell': True
    }
    module = PSModuleDepFinder()
    try:
        module.scan_exec_script(params)
    except Exception as exception:
        raise ValueError(exception)



# Generated at 2022-06-12 21:45:11.933131
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    class Object(object):
        def __init__(self):
            self.ps_modules = {}
            self.cs_utils_wrapper = {}

    instance = PSModuleDepFinder()

    def _slurp(path):
        return b"# Requires -Module Ansible.ModuleUtils.WebAdministration\n"

    def _strip_comments(data):
        return b"# Requires -Module Ansible.ModuleUtils.WebAdministration\n"

    try:
        # Replace the actual _slurp function with our own mock,
        # and then call the method.
        instance.scan_module('')
    except AttributeError:
        # Catch the AttributeError that occurs when the RealModuleFinder
        # object has no _module_repository attribute.
        pass

# Generated at 2022-06-12 21:45:21.242011
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import ansible.executor.powershell as powershell
    b_data = to_bytes(pkgutil.get_data("ansible.executor.powershell", "collection_exec_wrapper.ps1"))
    expect_value = [b'#compress: false', b'', b'definition', b'', b'to', b'', b'the', b'', b'target', b'']
    
    finder = PSModuleDepFinder()
    finder.scan_exec_script('collection_exec_wrapper')
    for line in b_data.split(b'\n'):
        if re.match(b'(?i)^#\s*compress:\s*false$', line):
            break

    b_data = to_bytes(b_data)

# Generated at 2022-06-12 21:45:26.672918
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    """
    test for method scan_exec_script of class PSModuleDepFinder
    """
    psModuleDepFinder = PSModuleDepFinder()
    assert psModuleDepFinder.exec_scripts == {}
    psModuleDepFinder.scan_exec_script('ansible_module_exec')
    assert psModuleDepFinder.exec_scripts != {}


# Generated at 2022-06-12 21:45:30.555555
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    name = "win_payload_file"
    finder.scan_exec_script(name)
    assert name in finder.exec_scripts

# Generated at 2022-06-12 21:45:55.382964
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    hasher = PSModuleDepFinder()
    hasher.scan_module(b"#Requires -Module Ansible.ModuleUtils.Something")
    assert b"Ansible.ModuleUtils.Something" in hasher.ps_modules
# END unit test

# Generated at 2022-06-12 21:46:05.197958
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print('in test_PSModuleDepFinder_scan_exec_script')
    name = 'exec'
    # Run the utility
    util = PSModuleDepFinder()
    util.scan_exec_script(name)

# Generated at 2022-06-12 21:46:06.505680
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    assert False, 'This unit test module needs to be tested'



# Generated at 2022-06-12 21:46:13.987400
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_PSModuleDepFinder_scan_exec_script._outcome = {}
    # Test if we can scan the powershell script and return the module dependency
    test_PSModuleDepFinder_scan_exec_script._module = PSModuleDepFinder()
    test_module_name = "test.ps1"
    test_module_content = """
        #AnsibleRequires -CSharpUtil ModuleUtils.A
        #AnsibleRequires -Wrapper TestScript
    """
    # Test if we can scan the powershell script and return the module dependency
    mu_path = ps_module_utils_loader.find_plugin("ModuleUtils.A", ".cs")
    if mu_path is None:
        test_PSModuleDepFinder_scan_exec_script._outcome = {"ModuleUtils.A" : "fail"}


# Generated at 2022-06-12 21:46:23.374544
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    import tempfile

    ps_data = b"""
    #AnsibleRequires -Powershell SomeUtil
    """

    cs_data = b"""
    using Ansible.SomeOtherUtil;
    """

    ps_mod = tempfile.NamedTemporaryFile(mode='w', suffix='.psm1', delete=False)
    ps_mod.write(ps_data.decode('utf-8'))
    ps_mod.flush()

    cs_mod = tempfile.NamedTemporaryFile(mode='w', suffix='.cs', encoding='utf-8', delete=False)
    cs_mod.write(cs_data.decode('utf-8'))
    cs_mod.flush()

    # Exec module data

# Generated at 2022-06-12 21:46:28.470580
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Create a PSModuleDepFinder object to test
    dep_finder = PSModuleDepFinder()

    # scan the script 'ExecutionPolicy' in the data directory
    dep_finder.scan_exec_script("ExecutionPolicy")

    # check that no errors were thrown against a known script
    assert True


# Generated at 2022-06-12 21:46:38.164640
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()

    script_name = "test_script"
    data = "#AnsibleRequires -PowerShell Ansible.ModuleUtils.Core\n"
    with pytest.raises(AnsibleError) as e:
        psmdf.scan_exec_script(script_name)
    assert e.value.args[0].startswith("Could not find executor powershell script for 'test_script'")

    with mock.patch("ansible.executor.powershell.script.__file__", "ansible.executor.powershell"):
        with mock.patch("ansible.executor.powershell.script.get_data", return_value=data.encode("utf-8")):
            psmdf.scan_exec_script(script_name)

    assert psmdf

# Generated at 2022-06-12 21:46:44.067398
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script(test_PSModuleDepFinder_scan_exec_script.__name__)

    assert test_PSModuleDepFinder_scan_exec_script.__name__ == finder.exec_scripts.keys()[0]
    assert '#Requires -Module Ansible.ModuleUtils.Powershell.Common' in finder.ps_modules.keys()



# Generated at 2022-06-12 21:46:49.064192
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    try:
        import ansible
    except ImportError:
        pass
    else:
        if LooseVersion(ansible.__version__) < LooseVersion('2.12'):
            print('Test needs Ansible version >= 2.12')
            return

    from ansible.executor.powershell.module_utils.common import _slurp

    #test-case for module_utils
    mod_finder = PSModuleDepFinder()
    data = _slurp('test/unit/executor/powershell/test_module_utils.psm1')
    mod_finder.scan_module(data, wrapper=False, powershell=True)
    assert len(mod_finder.ps_modules.keys()) == 1
    assert len(mod_finder.cs_utils_wrapper.keys()) == 0

# Generated at 2022-06-12 21:47:01.197092
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    ps_module_data = "using ansible_collections.namespace.collection_name.plugins.module_utils.test1;\n" +\
                     "using ansible_collections.namespace.collection_name.plugins.module_utils.test2;\n"
    ps_module_data2 = "using ansible_collections.namespace.collection_name.plugins.module_utils.test3;\n" +\
                      "using ansible_collections.namespace.collection_name.plugins.module_utils.test4;\n"
    ps_module_data3 = "using ansible_collections.namespace.collection_name.plugins.module_utils.test5;\n" +\
                      "using ansible_collections.namespace.collection_name.plugins.module_utils.test6;\n"

# Generated at 2022-06-12 21:47:17.971134
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()

    finder.scan_exec_script("common")
    assert finder.exec_scripts["common"] != None

    finder.scan_exec_script("common")
    assert finder.exec_scripts["common"] != None

    try:
        finder.scan_exec_script("not_existing_script")
    except AnsibleError as e:
        assert str(e) == "Could not find executor powershell script for 'not_existing_script'"


# Generated at 2022-06-12 21:47:18.646089
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass

# Generated at 2022-06-12 21:47:21.877608
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mu_finder = PSModuleDepFinder()
    mu_finder.scan_exec_script("test_script")

    assert mu_finder.exec_scripts["test_script"]


# Generated at 2022-06-12 21:47:25.492523
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_module(b'Line1 \n Line2 \n #Requires -Module Ansible.ModuleUtils.name \n Line3')
    assert dep_finder.ps_modules['Ansible.ModuleUtils.name']



# Generated at 2022-06-12 21:47:27.048722
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    """
    Method scan_module of class PSModuleDepFinder
    """
    pass

# Generated at 2022-06-12 21:47:32.621561
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    # pylint: disable=line-too-long
    # assertions for method scan_module of the class PSModuleDepFinder.
    # tests for output of scan_module.
    fqn = ["module_utils.basic", "module_utils.boolean", "module_utils.path"]
    module_data = {
        "module_utils.basic": b"#Requires -Module Ansible.ModuleUtils.Basic",
        "module_utils.boolean": b"#Requires -Module Ansible.ModuleUtils.Boolean",
        "module_utils.path": b"#Requires -Module Ansible.ModuleUtils.Path"
    }
    powershell = True
    wrapper = False
    # instantiating the PSModuleDepFinder class.
    ps_module_finder = PSModuleDepFinder()
    # calling the scan_

# Generated at 2022-06-12 21:47:44.667009
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    #
    # Unit test for method scan_exec_script of class PSModuleDepFinder
    #
    #
    #
    # Input arguments for this test:
    #
    #   name              The name of the script to scan for dependencies
    #
    #
    #
    # The following 'returns' statements are used for unit test:
    #
    #
    #
    # The following 'print' statements are used for unit test:
    #
    #
    #
    # Procedure call:
    #
    #
    #
    # Return:
    #
    #
    #

    import json
    import os
    import psutil
    import re
    import sys
    import yaml

    actual_returns = {}
    actual_returns['return_code'] = 1

# Generated at 2022-06-12 21:47:52.040996
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    import ansible.module_utils.storage.base

    obj = PSModuleDepFinder()
    ansible.module_utils.storage.base.BASE_STORAGE_PATH = b'USE THIS DIRECTORY IF SET'
    if ansible.module_utils.storage.base.BASE_STORAGE_PATH:
        obj = PSModuleDepFinder()
        # TODO: Mock obj.scan_module
        class TestModule(object):
            def __init__(self, *args, **kwargs):
                self.params = dict(
                    no_log=False,
                )
        obj.scan_

# Generated at 2022-06-12 21:47:52.993187
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    assert False # Replace with actual unit test

# Generated at 2022-06-12 21:47:55.604165
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    failed = True
    try:
        result = PSModuleDepFinder_scan_module()
    except NameError as e:
        failed = False
    assert failed == False


# Generated at 2022-06-12 21:48:09.027944
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    '''
    Test for method scan_exec_script of class PSModuleDepFinder
    '''
    pass

# Generated at 2022-06-12 21:48:12.255363
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # setup test
    dep_finder = PSModuleDepFinder()

    # test
    dep_finder.scan_exec_script('basic')

    # check results
    assert dep_finder.exec_scripts['basic'] is not None


# Generated at 2022-06-12 21:48:20.397513
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    t = PSModuleDepFinder()
    assert t.ps_modules == {}
    assert t.cs_utils_wrapper == {}
    assert t.cs_utils_module == {}
    assert t.ps_version is None
    assert t.os_version is None
    assert t.become is False


# Generated at 2022-06-12 21:48:21.459762
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    pass


# Generated at 2022-06-12 21:48:25.859472
# Unit test for method scan_module of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_module():
    obj = PSModuleDepFinder()
    lines = ["using ansible_collections.NS.coll.plugins.module_utils.module_util_sample;"]
    fqn = "Ansible.NS.coll.plugins.module_utils.module_util_sample"
    wrapper = False
    powershell = True
    obj.scan_module(lines, fqn, wrapper,powershell)

# Generated at 2022-06-12 21:48:31.535043
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mock_module_data = '#Requires -Module Ansible.ModuleUtils.new'
    P = PSModuleDepFinder()
    assert P.ps_modules == dict()
    assert P.cs_utils_module == dict()
    assert P.cs_utils_wrapper == dict()
    P.scan_module(mock_module_data)
    assert P.ps_modules == dict()
    assert P.cs_utils_module == dict()
    assert P.cs_utils_wrapper == dict()
    P.scan_module(mock_module_data, fqn='test', wrapper=True, powershell=True)
    assert P.ps_modules == dict()
    assert P.cs_utils_module == dict()
    assert P.cs_utils_wrapper == dict()

# Generated at 2022-06-12 21:48:33.526312
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script("test")



# Generated at 2022-06-12 21:48:44.347082
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    '''
    :param class_name: the class name
    :return: a string of the unit test
    '''
    class_name = "PSModuleDepFinder"
    test_name = "test_%s_scan_exec_script" % class_name

# Generated at 2022-06-12 21:48:46.889885
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # arrange
    test_instance = PSModuleDepFinder()
    name = 'name'

    # act
    test_instance.scan_exec_script(name)

    # assert
    assert False



# Generated at 2022-06-12 21:48:50.834960
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Create object instance
    ps_module_finder = PSModuleDepFinder()

    # Create test case
    ps_module_finder.scan_exec_script('Pester')
    # Assert on the attributes of the object instance
    #ps_module_finder.scan_module
    #if ps_module_finder.scan_module:
    #    assert True
    #else:
    #    assert False


# Generated at 2022-06-12 21:49:05.226883
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script(u'ansible.module_utils.powershell.shell')


# Generated at 2022-06-12 21:49:08.670184
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    from ansible.executor.powershell import PSModuleDepFinder
    name="ExecModuleUtil"
    obj=PSModuleDepFinder()
    obj.scan_exec_script(name)
    print(obj.exec_scripts)
    assert obj.exec_scripts!=None


# Generated at 2022-06-12 21:49:11.255206
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():

    mod_finder = PSModuleDepFinder()

    # Test when file does not exist
    name = "test_exec_script"
    mod_finder.scan_exec_script(name)
    assert name in mod_finder.exec_scripts.keys()


# Generated at 2022-06-12 21:49:16.960390
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test that function scan_exec_script of class PSModuleDepFinder returns a dict with the given name.
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script(name="win_command")
    exec_script = dep_finder.exec_scripts
    assert exec_script["win_command"]


# Generated at 2022-06-12 21:49:23.196115
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    mdf = PSModuleDepFinder()
    assert len(mdf.exec_scripts) == 0
    mdf.scan_exec_script("powershell_module")
    assert len(mdf.exec_scripts) == 1
    assert mdf.exec_scripts["powershell_module"].startswith("#Requires")
    assert len(mdf.ps_modules) > 0


# Generated at 2022-06-12 21:49:26.522496
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    finder.scan_exec_script("basic")
    finder.scan_exec_script("script")
    finder.scan_exec_script("script")

    assert "basic" in finder.exec_scripts.keys()
    assert "script" in finder.exec_scripts.keys()
    assert "basic" in finder.cs_utils_wrapper.keys()
    assert "script" in finder.cs_utils_wrapper.keys()


# Generated at 2022-06-12 21:49:37.806392
# Unit test for method scan_exec_script of class PSModuleDepFinder

# Generated at 2022-06-12 21:49:39.729846
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    print("TODO: Add unit tests to %s" % __file__)



# Generated at 2022-06-12 21:49:41.990666
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()

    psmdf.scan_exec_script("common")

# Generated at 2022-06-12 21:49:51.156458
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    psmdf = PSModuleDepFinder()
    psmdf.scan_module = MagicMock()
    if not C.DEFAULT_DEBUG:
        psmdf.scan_module.return_value = 'script_data'

    # Test exception on script not found
    try:
        psmdf.scan_exec_script('test_script')
    except AnsibleError as ae:
        assert 'Could not find executor powershell script for \'test_script\'' in to_text(ae)

    # Test script scanned based on default debug setting
    psmdf.scan_exec_script('RawModule')
    assert psmdf.exec_scripts['RawModule'] == to_bytes('script_data')




# Generated at 2022-06-12 21:50:15.437382
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    obj = PSModuleDepFinder()
    obj.scan_exec_script('run_ps_script')

# Generated at 2022-06-12 21:50:20.621822
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    powershell_collections_loader = import_module('powershell_collections_loader')
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script(name="Core")
    # dep_finder.scan_module(module_data="", fqn=None, wrapper=False, powershell=True)
    assert "Core" in dep_finder.exec_scripts


# Generated at 2022-06-12 21:50:23.306663
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    # Test the method when the name does not exist
    # Return: none
    finder = PSModuleDepFinder()
    finder.scan_exec_script("name")
    assert finder.exec_scripts[name] != None

# Generated at 2022-06-12 21:50:25.759483
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    test_obj = PSModuleDepFinder()
    module_path = './test_module_path'
    test_obj.scan_exec_script(module_path)

# Generated at 2022-06-12 21:50:30.144327
# Unit test for method scan_exec_script of class PSModuleDepFinder
def test_PSModuleDepFinder_scan_exec_script():
    finder = PSModuleDepFinder()
    test1 = finder.scan_exec_script('setup')
    assert test1 == {'data': '', 'path': 'Ansible.ModuleUtils.{name}'}
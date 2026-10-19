

# Generated at 2022-06-13 14:55:41.984542
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell = ShellModule(shell_type='powershell')
    script = shell.expand_user('~/foo')
    assert(script == """Write-Output '{"_ansible_parsed": true, "_ansible_no_log": false, "_ansible_diff": {"after": "", "before": "", "before_header": "", "before_footer": ""}}\nC:\\Users\\{{ lookup(\"env\", \"USERNAME\") }}\\foo'""")
    script = shell.expand_user('~\\foo')

# Generated at 2022-06-13 14:55:53.059787
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    module = ShellModule()
    test_path = '/root/'
    assert module.path_has_trailing_slash(test_path) == True
    test_path = 'root/'
    assert module.path_has_trailing_slash(test_path) == True
    test_path = 'C:\temp'
    assert module.path_has_trailing_slash(test_path) == False
    test_path = 'C:\\temp\\putty'
    assert module.path_has_trailing_slash(test_path) == True
    test_path = '\\\\test\\test'
    assert module.path_has_trailing_slash(test_path) == False
    test_path = '//test/test'

# Generated at 2022-06-13 14:56:00.930957
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import os
    import unittest
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes
    from io import StringIO

    class TestShellModule(unittest.TestCase):
        """ Unit tests for ShellModule """

        def setUp(self):
            self.stderr = StringIO()
            self.sm = ShellModule(stderr=self.stderr)

        def tearDown(self):
            self.stderr.close()


        def test_SHELL_REDIRECT_ALLNULL(self):
            self.assertEqual(self.sm._SHELL_REDIRECT_ALLNULL, '> $null')

        def test_SHELL_AND(self):
            self.assertEqual(self.sm._SHELL_AND, ';')



# Generated at 2022-06-13 14:56:08.861245
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import sys
    import os
    # Test Windows PS Module
    p = ShellModule('', '', '/usr/bin/ansible', connect_timeout=10, running_on_windows=True)
    ps_cmd = p.build_module_command(
        '',
        '#!powershell',
        'Get-Process',
        )
    # Assert script is encoded within -EncodedCommand
    assert '-EncodedCommand' in ps_cmd
    # Assert wrapper is encoded within -EncodedCommand
    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")
    bootstrap_wrapper = to_bytes(base64.b64encode(bootstrap_wrapper), 'utf-8')

# Generated at 2022-06-13 14:56:12.624976
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    test_class = ShellModule()
    env_string = "Test_env"
    shebang = "#!test"
    cmd = "Test_cmd"
    arg_path = "test/test/test"
    print(test_class.build_module_command(env_string, shebang, cmd, arg_path))

if __name__ == "__main__":
    test_ShellModule_build_module_command()

# Generated at 2022-06-13 14:56:19.117097
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell = ShellModule()
    assert shell.expand_user('~\\test') == shell._encode_script(script='''Write-Output ((Get-Location).Path + '\\test')''')
    assert shell.expand_user('~') == shell._encode_script(script='''Write-Output (Get-Location).Path''')
    assert shell.expand_user('~foo\\test') == shell._encode_script(script='''Write-Output '~foo\\test' ''')

# Generated at 2022-06-13 14:56:26.410902
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # create the mocks
    shell = ShellModule()
    cmd = 'psexec \\bar -u goo -p secret -accepteula -h cmd /c "echo bar"'

    # call the method

# Generated at 2022-06-13 14:56:28.830973
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Check if the ShellModule class can be constructed
    shell_module = ShellModule()
    return shell_module

# Generated at 2022-06-13 14:56:35.646732
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Constructor for Powershell generation of remote execution
    shell = ShellModule(connector=None, shell_type='powershell')

    # Check that common args for Powershell is a list
    assert isinstance(shell.COMMON_ARGS, list)

    # Check that the common args for Powershell is what we expect
    assert shell.COMMON_ARGS == _common_args

    # Check that the shell plugin is returning the binary we expect
    assert shell.get_option('binary') == 'powershell.exe'

# Generated at 2022-06-13 14:56:43.749984
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    '''
    Test for "ShellModule" class method "build_module_command".
    Will test the following:
    - giving no parameters;
    - giving parameters for "Non-PowerShell" module;
    - giving parameters for "PowerShell" module;
    - giving parameters for "PowerShell" module and "shebang"
    '''

    # Calling the _build_module_command class method of class "ShellModule" with no parameters
    # Should return None

    myPShellM = ShellModule()
    test_result = myPShellM._build_module_command()
    assert test_result is None, 'Expected None, got: %s' % test_result

    # Calling the _build_module_command class method of class "ShellModule" with parameters:
    #  - cmd of type "string"
    #  - shebang of

# Generated at 2022-06-13 14:56:57.056816
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule() # https://github.com/ansible/ansible/blob/devel/lib/ansible/executor/powershell/powershell.ps1
    assert module.SHELL_FAMILY == 'powershell' # https://github.com/ansible/ansible/blob/devel/lib/ansible/executor/powershell/__init__.py#L7


# Generated at 2022-06-13 14:57:01.852245
# Unit test for constructor of class ShellModule
def test_ShellModule():
    python_file_name = "ansible/plugins/action/__init__.py"

    shell_obj = ShellModule()
    escaped_python_file_name = '"%s"' % python_file_name

    new_python_file_name = shell_obj._escape(python_file_name)

    assert escaped_python_file_name == new_python_file_name



# Generated at 2022-06-13 14:57:08.789152
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.powershell import ShellModule
    # Test object initialization
    shell_module_object = ShellModule()
    # Test value of static variables
    assert shell_module_object.SHELL_FAMILY == 'powershell'
    assert shell_module_object._IS_WINDOWS == True
    # Test value of class variables
    assert not shell_module_object.COMPATIBLE_SHELLS
    # Test value of instance variables
    assert not shell_module_object.chdir
    assert not shell_module_object.no_log
    assert not shell_module_object.prompt
    assert not shell_module_object.supports_check_mode
    assert shell_module_object.shebang == '#!powershell'

# Generated at 2022-06-13 14:57:16.539876
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()
    # test relative path
    script = shell.mkdtemp('test')
    # Expected: cmd.exe /c powershell.exe -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -OutputFormat Text -EncodedCommand
    # test absolute path
    script = shell.mkdtemp('/test', tmpdir='/tmp')
    # Expected: cmd.exe /c powershell.exe -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -OutputFormat Text -EncodedCommand

# Generated at 2022-06-13 14:57:22.529047
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule(connection=None, sort_buffersize=1024, become_methods=None, become_username=None, become_password=None, become_exe=None, environment=None, no_log=None, _ansible_debug=None, _ansible_verbose_always=None, _ansible_version=None, _ansible_no_log=None, _ansible_delegate_to=None, _ansible_socket=None)

    assert plugin is not None
    assert plugin._SHELL_REDIRECT_ALLNULL == '> $null'
    assert plugin._SHELL_AND == ';'
    assert plugin._IS_WINDOWS == True

# Generated at 2022-06-13 14:57:28.201488
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import tempfile
    from ansible.executor.powershell.powershell import ShellModule
    from ansible.module_utils._text import to_text

    # Create temp dir with tilde in path
    base_temp_dir = tempfile.mkdtemp()
    h = tempfile.mkdtemp(dir=base_temp_dir)
    h = to_text(h)

    # Convert to remote format
    shell = ShellModule(connection='winrm')
    remote_tmp = shell.get_option('remote_tmp')
    dest_tmp = shell.join_path(remote_tempdir, to_text(os.path.basename(base_temp_dir)))

    # Create another temp dir with tilde in path
    script = shell.mkdtemp(tmpdir=dest_tmp)

    # Compare paths

# Generated at 2022-06-13 14:57:31.603714
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module_obj = ShellModule()
    assert module_obj._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module_obj._SHELL_AND == ';'
    assert module_obj._IS_WINDOWS == True
    assert module_obj.COMPATIBLE_SHELLS == frozenset()
    assert module_obj.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 14:57:35.127702
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule(connection=None,
                            noop_command=None,
                            module_implementation_preferences=None)
    assert isinstance(shell_obj, ShellModule)


# Generated at 2022-06-13 14:57:46.599060
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import shlex_quote

    for tmpd in ['$env:temp', '$env:tmp', '$env:systemroot', 'c:\\windows\\system32']:
        shell = ShellModule()
        cmd = shell.mkdtemp(tmpdir=tmpd)
        # Need to quote the path to ensure it is handled correctly
        if PY3:
            script_content = ' '.join([shlex_quote(x) for x in cmd.split()])
        else:
            script_content = ' '.join([shlex.quote(x) for x in cmd.split()])
        assert script_content.startswith('$tmp_path = ')

# Generated at 2022-06-13 14:57:58.243264
# Unit test for constructor of class ShellModule
def test_ShellModule():

    os.environ.clear()

    shell_module = ShellModule()

    assert not shell_module.HAS_TTY

    # replace the actual env vars with the mock ones
    for key in os.environ:
        assert key in shell_module.SHELL_DEFAULT_ENV

    # add more env vars
    shell_module.SHELL_DEFAULT_ENV['JUNK_ENV_VAR'] = 'junk_env_var'

    # use the newly registered env vars
    shell_module.set_shell_default_env()

    # the original code would reset the env vars to the value
    # at the time of construction, so do the same here
    for key, value in os.environ.items():
        assert key in shell_module.SHELL_DEFAULT_ENV

# Generated at 2022-06-13 14:58:06.399580
# Unit test for constructor of class ShellModule
def test_ShellModule():
    n = ShellModule()
    assert n.SHELL_FAMILY == 'powershell'
    assert n._IS_WINDOWS



# Generated at 2022-06-13 14:58:15.782831
# Unit test for constructor of class ShellModule
def test_ShellModule():

    fake_shell = ShellModule()

    data = "#< CLIXML\r\n<Objs Version=\"1.1.0.1\" xmlns=\"http://schemas.microsoft.com/powershell/2004/04\"><S S=\"Error\">\r\nAt line:1 char:1\r\n+ Test-Module\r\n+ ~~~~~~~~~~~\r\n    + CategoryInfo          : ObjectNotFound: (Test-Module:String) [], CommandNotFoundException\r\n    + FullyQualifiedErrorId : CommandNotFoundException\r\n \r\n</S></Objs>\r\n"

# Generated at 2022-06-13 14:58:26.426035
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.executor.module_common
    import ansible.executor.powershell
    from ansible.executor.module_common import MOD_ARGS_BACK_COMPAT_CONFLICT
    # Create a dummy module_args
    module_args = dict(
        ANSIBLE_MODULE_ARGS=dict(
            operation='write',
            path='C:\\Temp\\test.txt',
            content='my test content'
        )
    )
    # Execute initialization code of plugin
    # De-reference AnsibleModule object
    mod = ansible.executor.module_common.AnsibleModule(**module_args)
    shell = ShellModule(mod)
    # Execute code to be tested
    plugin = PowerShellModulePlugin(shell, **module_args)
    # Expected results

# Generated at 2022-06-13 14:58:35.083151
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    powershell_shell = ShellModule(None)


# Generated at 2022-06-13 14:58:37.624863
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule()
    assert plugin.COMPATIBLE_SHELLS == frozenset()
    assert plugin.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 14:58:48.218547
# Unit test for constructor of class ShellModule
def test_ShellModule():
    p = ShellModule()
    assert hasattr(p, 'SHELL_FAMILY')
    assert p.SHELL_FAMILY == 'powershell'
    assert hasattr(p, 'COMPATIBLE_SHELLS')
    assert p.COMPATIBLE_SHELLS == frozenset()
    assert hasattr(p, '_IS_WINDOWS')
    assert p._IS_WINDOWS
    assert hasattr(p, '_SHELL_REDIRECT_ALLNULL')
    assert p._SHELL_REDIRECT_ALLNULL == '> $null'
    assert hasattr(p, '_SHELL_AND')
    assert p._SHELL_AND == ';'



# Generated at 2022-06-13 14:58:49.301571
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()



# Generated at 2022-06-13 14:58:49.763760
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 14:58:50.796015
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule == ShellModule



# Generated at 2022-06-13 14:58:54.520992
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    This function is used to test the constructor of class ShellModule,
    this function will be called when executing 'python setup.py test'.
    :return: None
    """
    shell_module = ShellModule()
    assert shell_module.SHELL_FAMILY == 'powershell'
    assert shell_module.COMPATIBLE_SHELLS == frozenset()
    assert not shell_module._IS_WINDOWS

# Generated at 2022-06-13 14:58:59.544492
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:59:01.913390
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule('test')
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 14:59:05.533808
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert type(sm) == ShellModule
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 14:59:10.634745
# Unit test for constructor of class ShellModule
def test_ShellModule():
     obj = ShellModule(connection='test',shell_executable='test.exe')
     print(obj._SHELL_REDIRECT_ALLNULL)
     print(obj._SHELL_AND)
     print(obj._IS_WINDOWS)
     print(obj.COMPATIBLE_SHELLS)
     print(obj.SHELL_FAMILY)

# Generated at 2022-06-13 14:59:11.641192
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule()

# Generated at 2022-06-13 14:59:13.979772
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule()
    print(plugin.get_remote_filename('sample.ps1'))


if __name__ == '__main__':
    test_ShellModule()

# Generated at 2022-06-13 14:59:17.968830
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule(connection=None)

    assert mod.SHELL_FAMILY == 'powershell'

# Unit test case to check if the cmd is expanded to a full path
# before being compared with the available shells or not.
#

# Generated at 2022-06-13 14:59:21.685018
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell._IS_WINDOWS == True



# Generated at 2022-06-13 14:59:23.406462
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection=None)
    print(module)

# Generated at 2022-06-13 14:59:23.822918
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# Generated at 2022-06-13 14:59:37.862411
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import os
    import tempfile
    import random

    # Create temporary file
    fd, random_temp_file = tempfile.mkstemp()
    os.close(fd)

    # Create temporary directory
    temp_dir = tempfile.mkdtemp()

    # Encode random_temp_file
    encoded_random_temp_file = base64.b64encode(random_temp_file.encode('utf-16-le')).decode('utf-8')

    test_string = "This string has spaces, 'single quotes', `backticks`, \"double quotes\", \\\\backslashes\\\\, $dollarsigns$"

    # Generate random integers
    random_number = random.randint(1, 20)
    random_number2 = random.randint(1, 20)

    shell = ShellModule

# Generated at 2022-06-13 14:59:38.967960
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule(connection=None)
    assert sm

# Generated at 2022-06-13 14:59:42.214096
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_plugin = ShellModule(connection=None)
    assert shell_plugin.SHELL_FAMILY == 'powershell'
    assert shell_plugin._IS_WINDOWS is True

# Generated at 2022-06-13 14:59:44.728365
# Unit test for constructor of class ShellModule
def test_ShellModule():
    print("Testing ShellModule")
    print("Testing instantiation")
    obj = ShellModule()
    assert obj is not None, "Unable to instantiate ShellModule object"

# Generated at 2022-06-13 14:59:46.382850
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert isinstance(shell, ShellModule)

# Generated at 2022-06-13 14:59:48.088616
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert 'PowerShell' in ShellModule().COMPATIBLE_SHELLS

# Generated at 2022-06-13 14:59:56.787388
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.module_loader import ModuleLoader
    c = ShellModule(task=None, connection=ModuleLoader.connection_loader.get('winrm', task=None,
                                                                              connection=None, play_context=None),
                    shell_type='powershell', no_log=True)
    assert c.get_option('remote_tmp') == '$env:TEMP'
    assert c.get_option('executable') == 'powershell'
    assert not c.become_methods
    assert c.shell_type == 'powershell'
    assert len(c.COMPATIBLE_SHELLS) == 0
    assert c.SHELL_FAMILY == 'powershell'
    assert c._IS_WINDOWS


# Generated at 2022-06-13 14:59:57.773805
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()


# Generated at 2022-06-13 14:59:58.369936
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule({})

# Generated at 2022-06-13 15:00:00.207430
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert ShellModule.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:00:08.122350
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell is not None

# Generated at 2022-06-13 15:00:16.815336
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    '''Unit test for method build_module_command of class ShellModule.'''
    from ansible.executor import module_common
    from ansible.plugins.connection.winrm import Connection

    # Create a new ShellModule object
    shell = ShellModule(connection=Connection(module_common.shell._shared_loader_obj.module_loader))

    # Get the expected results

# Generated at 2022-06-13 15:00:18.132635
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod._IS_WINDOWS == True

# Generated at 2022-06-13 15:00:19.810896
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:20.458532
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule()

# Generated at 2022-06-13 15:00:21.137818
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 15:00:23.830419
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    # verify the shell_plugin is ShellModule
    assert sm.__class__.__name__ == 'ShellModule'

# Generated at 2022-06-13 15:00:25.235005
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule() is not None

# Generated at 2022-06-13 15:00:34.725985
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    class ShellModuleTest(ShellModule):
        def get_option(self, opt):
            if opt == 'remote_tmp':
                return 'tmp'

    sm = ShellModuleTest()
    env_string = '$env:ANSIBLE_TEST_VALUE = "TEST_VALUE"'
    shebang = '#!Powershell'
    cmd = 'New-Item test_file.txt'
    arg_path = 'test_file.txt'
    out = sm.build_module_command(env_string, shebang, cmd, arg_path)
    # The build_module_command method calls encode_script, which results in a newline being added at the end of the output
    # so we are removing the newline before comparing the output with the expected output
    out = out.strip()

# Generated at 2022-06-13 15:00:41.722767
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm._encode_script('Get-Help') == 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand IgBlAHQAKQA9ACcAaQBuACQAZQByAC4AbwByACAAZgBvAG4AIABpAHMAIABFAHIAbwB3AHcAdwAuAG0AZQBuAHQAIABhAG4AZAAuAG8AcgBnACIAIQAgACQAbwBwAGUAcgB0AGkAYwBhAHQAaQBvAG4ALgBlAGMAcgBpAHAAdABzACkAOwA=\r\n'
    # test interpreter escaping
#    assert sm._escape(""" ' ' $ """) == r""" ''\ ''\

# Generated at 2022-06-13 15:01:00.915744
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_excute = ShellModule()

# Generated at 2022-06-13 15:01:05.749030
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''Unit tests for ShellModule class'''
    module_shell = ShellModule()

    assert module_shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module_shell._SHELL_AND == ';'
    assert module_shell._IS_WINDOWS == True

# Generated at 2022-06-13 15:01:09.105244
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm._SHELL_REDIRECT_ALLNULL == '> $null'
    assert sm._SHELL_AND == ';'

# Generated at 2022-06-13 15:01:17.590806
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert isinstance(ShellModule.COMPATIBLE_SHELLS, frozenset)
    assert ShellModule.SHELL_FAMILY == 'powershell'
    assert ShellModule._IS_WINDOWS
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'
    assert shell.which('pwd') == 'pwd'
    assert shell.DEFAULT_EXECUTABLE == 'powershell.exe'
    assert shell.DEFAULT_ARGS == '-NoLogo -NonInteractive -NoProfile -ExecutionPolicy RemoteSigned'
    assert shell.base_dir() == os.path.dirname(os.path.abspath(__file__))
    assert shell.__class__.__name__ == 'ShellModule'


# Generated at 2022-06-13 15:01:24.069807
# Unit test for constructor of class ShellModule
def test_ShellModule():
    p = ShellModule()
    p.join_path('/', '/tmp', '/var/tmp')
    p.get_remote_filename('/bin/sh')
    p.get_remote_filename('/bin/python')
    p.build_module_command(None, None, None, None)
    p.wrap_for_exec('a')
    p.expand_user('/home/username')

# Generated at 2022-06-13 15:01:28.349901
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test with powershell
    shell = ShellModule(command_consumer=None)
    assert shell.plugin_args == dict()
    assert shell.plugin_options == dict()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell._IS_WINDOWS is True

# Generated at 2022-06-13 15:01:28.922866
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 15:01:31.653772
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule(connection=None, runner_path='')
    assert mod.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:01:34.123493
# Unit test for constructor of class ShellModule
def test_ShellModule():

    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    shell_executor = ShellModule(module)
    assert shell_executor

# Generated at 2022-06-13 15:01:35.032765
# Unit test for constructor of class ShellModule
def test_ShellModule():
    pass

# Generated at 2022-06-13 15:02:11.725915
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule("ansible_connection=winrm ansible_shell_type=powershell ansible_winrm_scheme=https ansible_winrm_server=server.site.com ansible_winrm_port=5986 ansible_winrm_path=/wsman ansible_winrm_transport=certificate ansible_winrm_cert_pem=/home/user/.ansible/tmp/ansible-tmp-1469483381.91-147779855856000/winrm ansible_winrm_cert_key_pem=/home/user/.ansible/tmp/ansible-tmp-1469483381.92-147779855856000/winrm ansible_winrm_server_cert_validation=ignore ansible_winrm_read_timeout_sec=500", "gather_facts=yes").cmd

# Generated at 2022-06-13 15:02:16.669373
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule()

    # Unit test for method build_module_command of class ShellModule
    # with valid shebang and without '.ps1' extension in module name
    env_string = '''$env:ANSIBLE_MODULE_ARGS='foo';$env:ANSIBLE_MODULE_ARGS+=' bar';'''

    shebang = '#!powershell'
    cmd = 'win_ping'
    result = shell.build_module_command(env_string, shebang, cmd)
    # The following 'expected' value displays correctly in a Windows PowerShell console.
    # However, we cannot set it equal to the format string, because then the quotes
    # will appear doubled in the output of `print result`.
    # TODO(michaelgugino): investigate why this doesn't work.

# Generated at 2022-06-13 15:02:19.264857
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module._IS_WINDOWS is True
    assert module.SHELL_FAMILY == 'powershell'
    assert module.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:02:20.257057
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # No exception should be raised
    ShellModule()

# Generated at 2022-06-13 15:02:23.658188
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert not module.COMPATIBLE_SHELLS
    assert module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module._SHELL_AND == ';'
    assert module._IS_WINDOWS == True

# Generated at 2022-06-13 15:02:26.040305
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''Test the constructor of ShellModule to make sure it returns an instance of ShellModule'''
    shell = ShellModule(dict())
    assert isinstance(shell, ShellModule)

# Generated at 2022-06-13 15:02:32.309839
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import xmltodict
    import json


# Generated at 2022-06-13 15:02:33.414227
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule()
    assert shell_obj is not None

# Generated at 2022-06-13 15:02:36.969645
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule()
    assert m is not None

from ansible.plugins.loader import get_shell_plugin
from ansible.inventory.host import Host
from ansible.playbook.task import Task
from ansible.executor import task_executor
from ansible.utils.display import Display
from ansible.context import Defaults
from ansible.executor.process.worker import TaskProcessWorker


# Generated at 2022-06-13 15:02:38.344287
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''Creates an instance of ShellModule'''
    return ShellModule(connection=None)

# Generated at 2022-06-13 15:03:19.918647
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Creating a PowerShell ShellModule object for Windows
    shell = ShellModule(connection=None)
    #Test the values returned by shell.SHELL_FAMILY and shell._IS_WINDOWS
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS == True

# Generated at 2022-06-13 15:03:30.388867
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None)

    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell._IS_WINDOWS is True

    # Test join_path with 1 parameter
    # Join path with a normal path
    assert shell.join_path('/b/c') == r'\b\c'

    # Join path with an empty path
    assert shell.join_path('') == ''

    # Join path with a forward slash - should be replaced by back slash
    assert shell.join_path('\b/c') == r'\b\c'

    # Join path with a double slash - should be collapsed to a single slash
    assert shell.join_path('\b\\c') == r'\b\c'

    # Join path

# Generated at 2022-06-13 15:03:31.653709
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:03:38.241812
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert hasattr(ShellModule, '_SHELL_REDIRECT_ALLNULL')
    assert hasattr(ShellModule, '_IS_WINDOWS')
    assert hasattr(ShellModule, 'COMPATIBLE_SHELLS')
    assert hasattr(ShellModule, 'SHELL_FAMILY')
    assert hasattr(ShellModule, 'env_prefix')
    assert hasattr(ShellModule, 'join_path')
    assert hasattr(ShellModule, 'get_remote_filename')
    assert hasattr(ShellModule, 'path_has_trailing_slash')
    assert hasattr(ShellModule, 'chmod')
    assert hasattr(ShellModule, 'chown')
    assert hasattr(ShellModule, 'set_user_facl')
    assert hasattr(ShellModule, 'remove')

# Generated at 2022-06-13 15:03:47.229313
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    script = module._encode_script(u'''
        exit 11;
        # this is a comment
        ''')

# Generated at 2022-06-13 15:03:50.113676
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule.__name__ == 'ShellModule'
    assert ShellModule.COMPATIBLE_SHELLS == frozenset()
    assert ShellModule._SHELL_REDIRECT_ALLNULL == '> $null'


# Generated at 2022-06-13 15:03:59.413188
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Unit test for ShellModule"""
    shell_module = ShellModule()
    assert shell_module
    assert shell_module.COMPATIBLE_SHELLS == frozenset()
    assert shell_module.SHELL_FAMILY == 'powershell'
    assert shell_module._IS_WINDOWS
    assert shell_module.env_prefix() == ""
    assert shell_module.join_path("a", "b", "c") == "a\\b\\c"
    assert shell_module.get_remote_filename("a") == "a.ps1"
    assert shell_module.get_remote_filename("a.ps1") == "a.ps1"
    assert shell_module.get_remote_filename("a.exe") == "a.exe"

# Generated at 2022-06-13 15:04:01.119193
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # pylint: disable=unused-argument
    shell = ShellModule(command_timeout=10, persistent_command_timeout=100)
    assert shell

# Generated at 2022-06-13 15:04:03.226240
# Unit test for constructor of class ShellModule
def test_ShellModule():
    powershell_shell_test = ShellModule()
    assert powershell_shell_test is not None

# Generated at 2022-06-13 15:04:05.731203
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell._SHELL_REDIRECT_ALLNULL.startswith('>')
    assert shell._SHELL_AND.startswith(';')
    assert not shell.DEFAULT_EXECUTABLE
    assert shell._IS_WINDOWS


# Generated at 2022-06-13 15:05:27.364469
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """This constructs a ShellModule object and tests various attributes."""
    shell = ShellModule(connection=None)

    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert 'PowerShell' in shell.ENV_PREFIX
    assert '-NoProfile' in shell.ENV_PREFIX
    assert '-NonInteractive' in shell.ENV_PREFIX
    assert '-ExecutionPolicy' in shell.ENV_PREFIX
    assert 'Unrestricted' in shell.ENV_PREFIX
    assert shell.HAS_BINARY_FILES == False

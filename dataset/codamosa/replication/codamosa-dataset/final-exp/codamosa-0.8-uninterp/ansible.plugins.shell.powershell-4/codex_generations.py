

# Generated at 2022-06-13 14:55:39.259951
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = __import__('ansible.modules.test.test_shell_module', fromlist=['test_shell_module'])
    module.init_tmp_path()
    module.setMicroseconds()

    ShellModule()
    module.cleanup_tmp_path()


# Generated at 2022-06-13 14:55:50.082551
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.module_utils.powershell import ensure_pwsh, ensure_ps1, PSError
    from ansible.module_utils.powershell.base64_converter import b64encode, b64decode
    import base64

    # Test passing of the correct value to the module,
    # verifying it is correctly decoded at the other end
    test_str = "value=hello"

    # Test passing of a more complex value, with
    # multiple arguments, verifying it is correctly
    # decoded at the other end.
    test_str2 = "value=hello hello2=world"

    # Test passing of a more complex value, with
    # multiple arguments, verifying it is correctly
    # decoded at the other end.
    test_str3 = "value=hello hello2=world"

    # Test passing

# Generated at 2022-06-13 14:55:52.714086
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule('')
    foo = 'foo'
    bar = 'bar'
    assert module.join_path(foo, bar) == foo + '\\' + bar

# Generated at 2022-06-13 14:55:54.752811
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    module.no_log_values.append('Ansible modules should not log sensitive data')


# Generated at 2022-06-13 14:56:02.512398
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell = ShellModule()

    assert shell.expand_user('~') == shell._encode_script('Write-Output (Get-Location).Path')
    assert shell.expand_user('~\\test') == shell._encode_script(script="Write-Output ((Get-Location).Path + '\\test')")
    assert shell.expand_user('~/test') == shell._encode_script(script="Write-Output ((Get-Location).Path + '\\test')")
    assert shell.expand_user('test') == shell._encode_script(script="Write-Output 'test'")


# Generated at 2022-06-13 14:56:04.338704
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''Check ShellModule is created without error'''
    ShellModule()

# unit test function to generate output to wrap in <out> tags

# Generated at 2022-06-13 14:56:10.251343
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    import tempfile
    tmp_dir = tempfile.mkdtemp()
    module = ShellModule(connection='winrm', become_method=None, become_user=None, become_pass=None, check=False, diff=False)
    module.get_option = lambda x: tmp_dir if x == 'remote_tmp' else None
    cmd = module.expand_user('~')
    res = module.run(cmd)
    assert isinstance(res, dict)
    assert all(key in res for key in ['rc', 'stdout', 'stderr'])
    assert res['stdout'].rstrip() == tmp_dir.rstrip()


# Generated at 2022-06-13 14:56:11.457316
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule() is not None

# Unit test interactive_shell() method of class ShellModule

# Generated at 2022-06-13 14:56:14.825118
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    sh_mod = ShellModule()
    tmpdir = sh_mod.mkdtemp()
    tmpdir = to_text(base64.b64decode(tmpdir.encode('utf-8')), 'utf-16-le').strip()
    assert tmpdir is not None


# Generated at 2022-06-13 14:56:23.500742
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.executor.powershell import ShellModule

    # Test the default case
    module = AnsibleModule(argument_spec=dict(path='', state='present'))
    shell = ShellModule(module)
    code = to_bytes(shell.mkdtemp(), encoding='ascii', errors='surrogate_or_strict')
    module.run_command(code, check_rc=True)
    assert module.params['dir'] != ''

    # Test the tmpdir case
    module = AnsibleModule(argument_spec=dict(path='', state='present'))
    shell = ShellModule(module)

# Generated at 2022-06-13 14:56:48.603298
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.connection.winrm import Connection as WinRM
    from ansible.plugins.shell.powershell import ShellModule

    win_rm = WinRM()
    module = ShellModule(conn=win_rm)

# Generated at 2022-06-13 14:56:59.929677
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule()
    shell.shell = 'powershell'

    # file module
    cmd, args, become, become_user, sudoable = shell.build_module_command(
        '', '#!powershell', 'echo test', '/path/to/arg')
    assert args is None
    assert become is False
    assert become_user is None
    assert sudoable is False
    assert "echo test" in cmd
    assert "& . /path/to/arg |" in cmd
    assert "Bootstrap-Ansible.psm1" in cmd

    cmd, args, become, become_user, sudoable = shell.build_module_command(
        '', '#!some/path', 'echo test', '/path/to/arg')
    assert args is None
    assert become is False
    assert become_user is None

# Generated at 2022-06-13 14:57:07.528477
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule(connection=None, put_files=None, run=None)
    assert s.COMPATIBLE_SHELLS == frozenset()
    assert s.SHELL_FAMILY == 'powershell'
    assert s._IS_WINDOWS is True
    assert s.get_remote_filename("/tmp/file.sh") == "file.sh"
    assert s.get_remote_filename("/tmp/file.ps1") == "file.ps1"
    assert s.get_remote_filename("/tmp/file.exe") == "file.exe"
    s = ShellModule(connection=None, put_files=None, run=None)
    assert s.env_prefix() == ""


# Generated at 2022-06-13 14:57:13.420530
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module._SHELL_AND == ';'
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module.SHELL_FAMILY == 'powershell'
    assert module._IS_WINDOWS == True

# Generated at 2022-06-13 14:57:20.695324
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    mock_self = type('', (), dict(
        _unquote=lambda _, x: x,
    ))()
    expected = ('/', True)
    actual = (ShellModule.path_has_trailing_slash(mock_self, '/'), True)
    assert expected == actual, actual
    expected = ('\\', True)
    actual = (ShellModule.path_has_trailing_slash(mock_self, '\\'), True)
    assert expected == actual, actual
    expected = ('/foo', False)
    actual = (ShellModule.path_has_trailing_slash(mock_self, '/foo'), False)
    assert expected == actual, actual
    expected = ('\\foo', False)

# Generated at 2022-06-13 14:57:30.148960
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    connection_info = MockConnectionInfo(None, 'test_host')
    shell_plugin = ShellModule(connection_info)

    # Base case
    env_string = '"abc=def"'
    result = shell_plugin.build_module_command(env_string, '/bin/python', 'test_module')

# Generated at 2022-06-13 14:57:42.132738
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    script_ps1 = b"Write-Host 'Hello world'"
    script_ps1_contents = b'#!powershell\n' + script_ps1

    script_psm1 = b"write-host 'Modules in path'\nwrite-host $Env:PSModulePath"

    script_exe = b'@ECHO OFF\nECHO Hello world'
    shebang_exe = '#!C:/Windows/system32/cmd.exe'

    # Import tasks from the powershell plugin
    import ansible.plugins.loader as plugin_loader
    plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../../plugins'))

    # prep the module loader
    import ansible.plugins.action.normal as module_loader
    module_loader.ActionModule._

# Generated at 2022-06-13 14:57:51.585517
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    sheller = ShellModule(connection=None, shell_type='powershell')
    sheller.tmpdir = 'C:\\Users\\Jefferson\\AppData\\Local\\Temp'
    sheller.TEMP_DIR_NAME = 'ansible-tmp-{0}'.format(base64.urlsafe_b64encode(os.urandom(16)).decode('ascii'))


# Generated at 2022-06-13 14:58:02.004032
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    module = ShellModule(connection='winrm')
    module.get_option = MagicMock(return_value=None)

    actual = module.mkdtemp()
    expected = '$tmp_path = [System.Environment]::ExpandEnvironmentVariables(\'\')\n' +\
        '$tmp = New-Item -Type Directory -Path $tmp_path -Name \'tmp.\'\n' +\
        'Write-Output -InputObject $tmp.FullName\n'
    assert actual == expected

    # call by super class
    module = ShellModule(connection='winrm')
    module.get_option = MagicMock(return_value='/tmp')

    actual = module.mkdtemp()

# Generated at 2022-06-13 14:58:06.316431
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()

    # Ensure that the correct shell is selected
    assert 'powershell' == sm.SHELL_FAMILY

    # Ensure no PowerShell errors occur when getting the version
    sm.get_version()

    # Ensure the module has a remote_tmp that is set to the default value
    assert sm.get_option('remote_tmp') == '$env:TEMP\\remote_tmp'

# Generated at 2022-06-13 14:58:18.601172
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    ps = ShellModule(connection=None)
    assert shell.SHELL_FAMILY == 'powershell'
    assert ps.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 14:58:19.747515
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # TODO: implement unit test
    return

# Generated at 2022-06-13 14:58:28.758587
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None, runner_on_failed=None, runner_on_ok=None, runner_on_skipped=None, runner_on_unreachable=None, runner_on_no_hosts=None, runner_on_async_poll=None, runner_on_async_ok=None, runner_on_async_failed=None, runner_on_file_diff=None, stdin=None)
    assert shell.get_remote_filename('path/to/foo.ps1') == 'foo.ps1'
    assert shell.get_remote_filename('path/to/foo.exe') == 'foo.exe'
    assert shell.get_remote_filename('path/to/foo') == 'foo.ps1'
    assert shell.get_remote_filename('path/to/foo.sh')

# Generated at 2022-06-13 14:58:37.106658
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():

    # test bootstrap_wrapper
    shebang = '#!/usr/bin/python'
    module_cmd = '/usr/bin/python /some/module arg1 arg2 arg3'
    cmd_module_path = '/some/module'
    psmod = ShellModule()
    res = psmod.build_module_command('', shebang, module_cmd, arg_path=cmd_module_path)
    res = res.replace("'", "\\'")
    res = res.replace("\n", "")

# Generated at 2022-06-13 14:58:48.772672
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import sys
    import tempfile
    import unittest

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.shell = ShellModule(tmpdir=tempfile.gettempdir())

        def test_build_module_command_1(self):
            self.shell.SHELL_FAMILY = 'bash'

            env_string = ''
            shebang = '#!/usr/bin/python'
            cmd = "arg1 'arg2' \"arg3\""

            actual = self.shell.build_module_command(env_string=env_string, shebang=shebang, cmd=cmd)
            expected = "%s %s '%s'" % (shebang, cmd, self.shell.get_remote_filename(arg_path=None))

# Generated at 2022-06-13 14:58:49.352657
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()

# Generated at 2022-06-13 14:58:52.998595
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """This is a unit test for the constructor of the ShellModule class.
    """
    # Try to create a ShellModule object with a connection that does not exist
    shell_module = ShellModule(connection=None)
    return shell_module

# Generated at 2022-06-13 14:58:54.557456
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:59:03.894517
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    module = ShellModule(connection=None)

    assert module.path_has_trailing_slash('\\') == True
    assert module.path_has_trailing_slash('"\\"') == True
    assert module.path_has_trailing_slash('\\Program Files\\') == True
    assert module.path_has_trailing_slash('"\\Program Files\\"') == True

    assert module.path_has_trailing_slash('/') == True
    assert module.path_has_trailing_slash('"/"') == True
    assert module.path_has_trailing_slash('/Program Files/') == True
    assert module.path_has_trailing_slash('"/Program Files/"') == True


# Generated at 2022-06-13 14:59:06.983730
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.module_utils.common._collections_compat import Mapping
    m = ShellModule()
    assert issubclass(type(m), Mapping)

# Generated at 2022-06-13 14:59:11.557877
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert type(ShellModule("", "")) == ShellModule

# Generated at 2022-06-13 14:59:12.712905
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:59:13.813127
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 14:59:17.123658
# Unit test for constructor of class ShellModule
def test_ShellModule():
    win_powershell = ShellModule(None)
    print(win_powershell)

if __name__ == "__main__":
    test_ShellModule()

# Generated at 2022-06-13 14:59:25.462350
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    m = ShellModule()

# Generated at 2022-06-13 14:59:34.295867
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import os
    import inspect
    # set module path so we can read ansible
    cmd_subfolder = os.path.realpath(
        os.path.abspath(
            os.path.join(os.path.split(
                inspect.getfile(
                    inspect.currentframe()
                ))[0],
                '..', '..', 'executor', 'powershell')))
    # define the cmd_subfolder
    cmd_subfolder = os.path.realpath(
        os.path.abspath(
            os.path.join(os.path.split(
                inspect.getfile(
                    inspect.currentframe()
                ))[0],
                '..', '..', 'executor', 'powershell')))
    # find the ansible module to load

# Generated at 2022-06-13 14:59:39.635272
# Unit test for constructor of class ShellModule
def test_ShellModule():
    constructor = ShellModule()

    # test class members
    assert constructor._SHELL_REDIRECT_ALLNULL == '> $null'
    assert constructor._SHELL_AND == ';'
    assert constructor._IS_WINDOWS == True
    assert constructor.COMPATIBLE_SHELLS == frozenset()
    assert constructor.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 14:59:50.266693
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule()
    assert shell.path_has_trailing_slash('/') == False
    assert shell.path_has_trailing_slash('/tmp/') == True
    assert shell.path_has_trailing_slash('c:') == False
    assert shell.path_has_trailing_slash('c:\\tmp') == True
    assert shell.path_has_trailing_slash('\\\\tmp') == False
    assert shell.path_has_trailing_slash('\\\\tmp\\') == True
    assert shell.path_has_trailing_slash('C:\\tmp') == True
    assert shell.path_has_trailing_slash('C:/tmp') == True
    assert shell.path_has_trailing_slash('//tmp') == False
    assert shell.path_

# Generated at 2022-06-13 14:59:51.258897
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module

# Generated at 2022-06-13 14:59:52.546102
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm._shell_plugin_class is None

# Generated at 2022-06-13 15:00:07.265084
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()

# Generated at 2022-06-13 15:00:15.906764
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    sh_mod = ShellModule()
    env_string = ""
    shebang = "#!powershell"
    cmd = "hostname.exe"
    module_command = sh_mod.build_module_command(env_string, shebang, cmd)
    cmd_parts = _common_args + ['-Command', '"& C:\\\\windows\\\\system32\\\\hostname.exe | %s; exit $LASTEXITCODE"' %
        pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1").strip()]
    assert module_command == ' '.join(cmd_parts)

    env_string = ""
    shebang = ""
    cmd = "hostname.exe"

# Generated at 2022-06-13 15:00:27.816274
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # initialize the plugin
    sh_pl = ShellModule(('localhost', {}))
    # fill in the parameters
    binary_shebang = '#!/usr/bin/python'
    powershell_shebang = '#!powershell'
    cmd = 'test.ps1'
    env_string = 'env_string'
    strict_mode = True
    preserve_rc = True

    # test if it is a powershell script
    cmd_list = sh_pl.build_module_command(env_string, powershell_shebang, cmd,
                                          strict_mode, preserve_rc).split(';')
    assert cmd_list[1][2:-2] == powershell_shebang.split()[0]

    # test if it is a binary script

# Generated at 2022-06-13 15:00:36.458105
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    # set up attrs that are normally set by the ansible.runner.shell_plugins.Connection
    shell.pipelining = False
    shell.run_uuid = "uuid1"
    shell.run_command = "Write-Error 'oops'"
    shell.module_implementation_preferences = ['powershell', 'winrm', 'psrp']
    shell.become_method = None
    # set up attrs that are normally set by the ansible.runner.shell_plugins.ShellPlugin
    shell.no_log = True
    shell.connection._shell = shell
    # execute method
    output = shell.exec_command()
    # evaluate output
    assert len(output) == 3
    assert isinstance(output, tuple)
    assert isinstance(output[0], int)

# Generated at 2022-06-13 15:00:37.975623
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module_cls = ShellModule()
    assert shell_module_cls.SHELL_FAMILY == 'powershell'
    assert len(ShellModule._common_args) == 5

# Generated at 2022-06-13 15:00:40.928885
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell._SHELL_AND == ';'
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS is True


# Generated at 2022-06-13 15:00:49.497339
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import os
    import sys

    module = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    module = os.path.join(module, "_ansible_test")
    sys.path.append(module)
    from ansible_test._loader import TestLoader

    loader = TestLoader()

    # Pass in an empty argument list and make sure that it does not error
    shell_cmd = ShellModule(loader)

    # Test the _parse_clixml() method
    # - First test an empty cli_xml and make sure it returns an empty string
    # - Next test a single error stream result and make sure the string is returned correctly
    # - Next test a single warning stream result and make sure the string is returned correctly
    # - Finally test a mixture of error and warning stream results and make sure

# Generated at 2022-06-13 15:01:00.151082
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    test_module_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    test_module_path = os.path.join(test_module_dir, 'windows', 'win_ping')
    test_module_name = 'ping'

    module = ShellModule()

    # Powershell 3.0 is the default for Windows Server 2012 R2 and above
    powershell_cmd = '''&{ $VerbosePreference='Continue'; $DebugPreference='Continue'; 
    $ErrorActionPreference='Stop'; $ProgressPreference='SilentlyContinue'; 
    $host.ui.RawUI.BufferSize = New-Object Management.Automation.Host.Size(4096, 25); 
    Set-StrictMode -Version Latest; '''
   

# Generated at 2022-06-13 15:01:11.095592
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()

    # Test class attribute
    assert ShellModule.COMPATIBLE_SHELLS == frozenset()
    assert ShellModule.SHELL_FAMILY == 'powershell'
    assert not ShellModule._IS_WINDOWS

    # Test object attribute
    assert module.env == {}
    assert module.prompt
    assert module.supports_check_mode
    assert module.supports_no_log
    assert not module.targets_windows
    assert module.has_pipelining
    assert not module.always_pipeline_modules
    assert not module.su
    assert module.sudo
    assert module.sudo_exe
    assert not module.su_pass
    assert module.become
    assert module.become_exe
    assert module.become_flags
    assert module.become_method

# Generated at 2022-06-13 15:01:12.939601
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod.COMPATIBLE_SHELLS == frozenset()
    assert mod.SHELL_FAMILY == 'powershell'
    return mod


# Generated at 2022-06-13 15:01:28.432625
# Unit test for constructor of class ShellModule
def test_ShellModule():
    args = {'_ansible_connection': 'winrm',
            '_ansible_remote_tmp': 'c:/temp/ansible',
            '_ansible_keep_remote_files': False
            }
    obj = ShellModule(args)
    assert obj._IS_WINDOWS is True

    # Test the chdir functionality
    assert obj.chdir('c:\\temp\\ansible') == obj._encode_script('''Set-Location -LiteralPath 'c:\\temp\\ansible' ;''')

    # Test the join_path
    assert obj.join_path('c:\\temp', 'ansible') == 'c:\\temp\\ansible'
    assert obj.join_path('c:\\temp\\', 'ansible') == 'c:\\temp\\ansible'

# Generated at 2022-06-13 15:01:32.539048
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule()
    assert shell_obj._IS_WINDOWS == True
    assert shell_obj.COMPATIBLE_SHELLS == frozenset()
    assert shell_obj.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:01:33.597601
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert not ShellModule('/bin/bash')

# Generated at 2022-06-13 15:01:43.517292
# Unit test for constructor of class ShellModule
def test_ShellModule():
    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")
    shell = ShellModule(connection=None)
    cmd = shell.build_module_command('', '', '')
    assert cmd == bootstrap_wrapper
    cmd = shell.build_module_command('', '#!powershell', '', '')
    assert cmd == 'type  | & { %s }; exit $LASTEXITCODE' % bootstrap_wrapper
    cmd = shell.build_module_command('', '#!powershell', 'foo.ps1', '')
    assert cmd == 'type foo.ps1 | & { %s }; exit $LASTEXITCODE' % bootstrap_wrapper

# Generated at 2022-06-13 15:01:48.655633
# Unit test for constructor of class ShellModule
def test_ShellModule():
    S = ShellModule()
    assert str(S)
    assert S.COMPATIBLE_SHELLS == set()
    assert S.SHELL_FAMILY == 'powershell'
    assert S._SHELL_REDIRECT_ALLNULL == '> $null'
    assert S._SHELL_AND == ';'
    assert S._IS_WINDOWS


# Generated at 2022-06-13 15:01:58.300240
# Unit test for constructor of class ShellModule

# Generated at 2022-06-13 15:02:03.503815
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule(connection=None)
    print(shell_module._SHELL_REDIRECT_ALLNULL)
    print(shell_module.COMPATIBLE_SHELLS)
    print(shell_module.SHELL_FAMILY)


if __name__ == '__main__':
    test_ShellModule()

# Generated at 2022-06-13 15:02:05.444196
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()


# Generated at 2022-06-13 15:02:09.741195
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    Constructor test with a psrp connection plugin to ensure that the
    correct shell is chosen based on the connection plugin specified
    '''
    if not ShellBase.shell_class('psrp'):
        raise AssertionError('psrp shell plugin not found')

    shell = ShellBase()
    assert shell.SHELL_FAMILY == 'powershell', 'Shell family is not powershell'

# Generated at 2022-06-13 15:02:17.397278
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.executor.powershell
    module = ansible.executor.powershell.ShellModule()
    module.path_has_trailing_slash('/some/path/')
    module.path_has_trailing_slash('\\some\\path\\')
    module.path_has_trailing_slash('/some/path')
    module.path_has_trailing_slash('\\some\\path')

# Generated at 2022-06-13 15:02:28.187186
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test the constructor ShellModule
    s = ShellModule()
    assert s.SHELL_FAMILY == 'powershell'
    assert s._SHELL_REDIRECT_ALLNULL == '> $null'
    assert s._SHELL_AND == ';'

# Generated at 2022-06-13 15:02:30.210438
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()

    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'



# Generated at 2022-06-13 15:02:31.989180
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()


if __name__ == '__main__':
    test_ShellModule()

# Generated at 2022-06-13 15:02:38.501922
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.powershell as ps

    ansible = AnsibleModule({})
    s = ShellModule(ansible)

    # test joining of path names with the join_path method
    s.join_path('C:\\', 'Windows', 'System32') == 'C:\\Windows\\System32'
    s.join_path('C:\\Windows\\', 'System32') == 'C:\\Windows\\System32'
    s.join_path('C:\\Windows\\System32', '\\Netlogon') == 'C:\\Windows\\System32\\Netlogon'
    s.join_path('C:\\Windows\\System32\\', '\\Netlogon') == 'C:\\Windows\\System32\\Netlogon'

    # test the path_

# Generated at 2022-06-13 15:02:47.875338
# Unit test for constructor of class ShellModule
def test_ShellModule():
    command = 'dir'
    sh = ShellModule()
    cmd = sh.build_module_command('', '', command)
    assert cmd == "& " + " ".join(_common_args) + " -EncodedCommand " + to_text(base64.b64encode('dir'.encode('utf-16-le')), 'utf-8') + "; exit $LASTEXITCODE"

    script = '''
        Set-StrictMode -Version Latest
        $var1 = 1
        $var2 = 2
        $var3 = "hi"
        $var4 = "there"
        $var1 + $var2
        $var3 + $var4
        exit 1
    '''
    cmd = sh.build_module_command('', '', script)
    assert cmd == "& " + " ".join

# Generated at 2022-06-13 15:02:49.998953
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod.SHELL_FAMILY == 'powershell'
    assert mod.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:02:50.811406
# Unit test for constructor of class ShellModule
def test_ShellModule():
    print("todo")




# Generated at 2022-06-13 15:02:56.050775
# Unit test for constructor of class ShellModule
def test_ShellModule():
    the_shell = ShellModule()

    assert the_shell.COMPATIBLE_SHELLS == frozenset()
    assert the_shell.SHELL_FAMILY == 'powershell'

    assert the_shell._IS_WINDOWS == True

    assert the_shell._SHELL_REDIRECT_ALLNULL == '> $null'

    # TODO: Add tests for all public functions

# Generated at 2022-06-13 15:02:59.945032
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    # It should be a child class for ShellBase
    assert isinstance(shell, ShellBase)
    expected_shell_family = 'powershell'
    assert shell.SHELL_FAMILY == expected_shell_family
    assert shell.BINARY_MODULES is None

# Generated at 2022-06-13 15:03:00.939585
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm is not None

# Generated at 2022-06-13 15:03:28.898860
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod._SHELL_REDIRECT_ALLNULL == '> $null'
    assert mod._SHELL_AND == ';'
    assert mod._IS_WINDOWS == True
    assert 'chmod is not implemented for Powershell' in mod.chmod('foo', 'bar')
    assert 'chown is not implemented for Powershell' in mod.chown('foo', 'bar')
    assert 'set_user_facl is not implemented for Powershell' in mod.set_user_facl('foo', 'bar', 'baz')
    assert mod.get_option('remote_tmp') == '$env:TEMP'


# Generated at 2022-06-13 15:03:31.664774
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS

# Generated at 2022-06-13 15:03:40.431945
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule(connection=None, add_ansible_module='', runner_path='/usr/bin/ansible-runner', ansible_module_name='shell', ansible_module_args='', ansible_module_kwargs='')
    assert shell_obj.SHELL_FAMILY == 'powershell'
    assert shell_obj.COMPATIBLE_SHELLS == frozenset()
    assert shell_obj._IS_WINDOWS == True
    assert shell_obj.SHELL_TYPE == 'powershell'
    assert shell_obj.SHELL_VERSION == None
    assert shell_obj.ENCODER == None
    assert shell_obj.SHELL_MODULE == None



# Generated at 2022-06-13 15:03:41.884837
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module is not None

# Generated at 2022-06-13 15:03:44.901729
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # run the class' constructor without arguments and expect a TypeError
    try:
        ShellModule()
    except TypeError:
        pass
    else:
        raise Exception("Exception not raised")

# Generated at 2022-06-13 15:03:46.804439
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """This is to test the ShellModule() class constructor"""
    shell = ShellModule()
    assert _common_args == shell._common_args

# Generated at 2022-06-13 15:03:51.043390
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module.SHELL_FAMILY == 'powershell'
    assert shell_module._IS_WINDOWS
    assert type(shell_module.COMPATIBLE_SHELLS) == frozenset
    assert type(shell_module.SHELL_FAMILY) == str
    assert type(shell_module._IS_WINDOWS) == bool

# Generated at 2022-06-13 15:03:57.044995
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sheller = ShellModule()

    sheller.get_remote_filename("host-name")
    sheller.join_path("c:/", "windows")
    sheller.normpath("c:/windows/path")
    sheller.build_module_command("", "", "echo hello", "")
    sheller.can_pipelining()
    sheller.wrap_for_exec("echo hello")
    sheller.set_user_facl("/foo", "user_name", '0644')

# Generated at 2022-06-13 15:03:57.626918
# Unit test for constructor of class ShellModule
def test_ShellModule():
    return ShellModule()

# Generated at 2022-06-13 15:04:00.097582
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm.SHELL_FAMILY == 'powershell'
    assert sm._IS_WINDOWS == True



# Generated at 2022-06-13 15:04:43.639923
# Unit test for constructor of class ShellModule
def test_ShellModule():

    module = ShellModule()

    # Check the environment variable prefix is None
    assert module.env_prefix() == ""

    # Test the join path
    assert module.join_path("A") == "A"
    assert module.join_path("A B") == "A B"
    assert module.join_path("A B", "C D", "E") == "A B\\C D\\E"
    assert module.join_path("A", "B", "C", "D", "E") == "A\\B\\C\\D\\E"
    assert module.join_path("A B C", "D E F", "G") == "A B C\\D E F\\G"

    # Check the remote file name is the same as the path name
    assert module.get_remote_filename("ABC") == "ABC"
    assert module

# Generated at 2022-06-13 15:04:47.530389
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.executor.module_common
    sheller = ShellModule(connection='winrm',runner_supports_sudo=False,become_method='runas',become_user='test-adminuser')
    sheller.inject = {}
    sheller.inject['ansible_shell_executable'] = 'powershell.exe'
    sheller.inject['ansible_shell_type'] = 'powershell'
    #TODO: Write a unit test

# Generated at 2022-06-13 15:04:56.602081
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()

# Generated at 2022-06-13 15:04:58.293173
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Verify that constructor sets _shell_type to 'powershell'
    shell = ShellModule()
    assert shell._shell_type == 'powershell'

# Generated at 2022-06-13 15:05:06.050579
# Unit test for constructor of class ShellModule
def test_ShellModule():
    class Options(object):
        def __init__(self, **kwargs):
            self.__dict__ = kwargs
    options = Options(remote_tmp='/tmp', remote_uid=None, remote_user='root')
    _shell = ShellModule(play_context=options)

    class RunnerOptions(object):
        def __init__(self, **kwargs):
            self.__dict__ = kwargs
    runner_options = RunnerOptions(connection='ssh', become=False)
    _shell.set_options(direct=options, shell_type='powershell', runner_options=runner_options)
    assert _shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:05:08.186653
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Constructor of class ShellModule
    powershell = ShellModule()
    assert powershell is not None

# Generated at 2022-06-13 15:05:19.278020
# Unit test for constructor of class ShellModule
def test_ShellModule():
    d = os.path.dirname(os.path.realpath(__file__))
    pm = ShellModule(connection=None, shell_type='powershell')
    assert pm.run() == (0, '', '', '')
    assert pm.run_command() == (0, '', '', '')
    assert pm.run_command(cmd='dir') == (0, '', '', '')
    assert pm.put_file('/tmp/test.txt', 'test') == (0, '', '', '')
    assert pm.put_file('/tmp/test.txt', 'test', mode='0777') == (0, '', '', '')
    assert pm.fetch_file('test.txt', '/tmp/test.txt') == (0, '', '', '')
    assert pm.fetch

# Generated at 2022-06-13 15:05:22.551724
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection='winrm')
    assert module._IS_WINDOWS is True
    assert module.SHELL_FAMILY == 'powershell'
    assert module.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:05:25.630842
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """This is a unit test for constructor of class ShellModule"""
    x = ShellModule()
    # The script shloud be generate successfully
    assert x.exists("'~'") == b"Write-Output (Test-Path '~')"
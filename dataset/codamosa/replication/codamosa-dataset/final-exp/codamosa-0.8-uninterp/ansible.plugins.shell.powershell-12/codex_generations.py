

# Generated at 2022-06-13 14:55:42.581612
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    sm = ShellModule(connection=None)

    # Test for path that has trailing slash
    path = '/path/to/dir/'
    assert sm.path_has_trailing_slash(path) is True

    # Test for path that has no trailing slash
    path = '/path/to/file'
    assert sm.path_has_trailing_slash(path) is False

    # Test for path that has trailing
    path = '\\path\\to\\dir\\'
    assert sm.path_has_trailing_slash(path) is True

    # Test for path that has no trailing slash
    path = '\\path\\to\\file'
    assert sm.path_has_trailing_slash(path) is False

# Generated at 2022-06-13 14:55:50.538199
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():

    test_module = ShellModule()

    # Verify that valid script extensions return correctly
    assert 'file.ps1' == test_module.get_remote_filename('file.ps1')
    assert 'file.exe' == test_module.get_remote_filename('file.exe')

    # Verify that non-script extensions are appended with .ps1
    assert 'file.ps1' == test_module.get_remote_filename('file')
    assert 'file.ps1' == test_module.get_remote_filename('file.other')


# Generated at 2022-06-13 14:55:59.262570
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.COMPATIBLE_SHELLS == frozenset({"powershell"})
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._SHELL_REDIRECT_ALLNULL == "> $null"
    assert shell._SHELL_AND == ';'
    assert shell._IS_WINDOWS is True
    assert shell.env_prefix(http_proxy='proxy:3128') == ""
    assert shell.join_path('c:/Users', 'test') == 'c:\\Users\\test'
    assert shell.join_path('c:/Users/', '/test') == 'c:\\Users\\test'
    assert shell.join_path('c:/Users/', '\\test') == 'c:\\test'

# Generated at 2022-06-13 14:56:00.640750
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell

# Generated at 2022-06-13 14:56:08.627556
# Unit test for constructor of class ShellModule
def test_ShellModule():


    _SHELL_REDIRECT_ALLNULL = '> $null'
    _SHELL_AND = ';'
    name = "ansible_shell_module_test"
    class Flag:
        no_log = False
    class AnsibleModule:
        def __init__(self, *args, **kwargs):
            pass

        def exit_json(self):
            pass

        def fail_json(self):
            pass

        def is_executable(self, path):
            return True
    class PluginLoader:
        pass
    class ShellSession:
        def send(self, data, prompt=None, answer=None, newline=True, check_all=False):
            pass
    class Connection:
        def __init__(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 14:56:15.218569
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    """ Create a fake connection object and test the build_module_command method """
    fake_connection = dict(
        transport='winrm',
        become=False,
        become_pass='',
        become_user='',
        environment={},
        remote_addr='',
        remote_user='',
        port=None
    )
    test_shell = ShellModule(connection=fake_connection, no_log=False)

    # Tests for build_module_command using a local module
    cmd = test_shell.build_module_command('', '', 'setup', '')
    assert "| " in cmd
    assert "bootstrap_wrapper" in cmd

    # Tests for build_module_command using a remote module
    cmd = test_shell.build_module_command('', '#!something', 'setup', '')

# Generated at 2022-06-13 14:56:19.632443
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    shell = ShellModule()
    assert shell.get_remote_filename('/path/to/filename') == 'filename.ps1'
    assert shell.get_remote_filename('/path/to/filename.ps1') == 'filename.ps1'
    assert shell.get_remote_filename('/path/to/filename.exe') == 'filename.exe'


# Generated at 2022-06-13 14:56:30.206985
# Unit test for constructor of class ShellModule
def test_ShellModule():
    serializer = None

    # Test 1
    test_class = ShellModule(None, serializer)
    assert test_class._SHELL_REDIRECT_ALLNULL == '> $null'
    assert test_class._SHELL_AND == ';'
    assert test_class._IS_WINDOWS is True
    assert test_class._SHELL_FAMILY == 'powershell'

    # Test 2
    test_class = ShellModule(None, serializer, 'test', 'test')
    assert test_class._SHELL_REDIRECT_ALLNULL == '> $null'
    assert test_class._SHELL_AND == ';'
    assert test_class._IS_WINDOWS is True
    assert test_class._SHELL_FAMILY == 'powershell'


# helper function for join_path tests

# Generated at 2022-06-13 14:56:31.326922
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod is not None

# Generated at 2022-06-13 14:56:32.058422
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 14:56:48.239103
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell_module = ShellModule()

    # Remove temp files if they exist
    try:
        os.remove('test_arg_path')
    except OSError:
        pass

    # Normal module (e.g. copy module)
    module_cmd = "C:\Program Files\Python\Python36\python.exe C:\Program Files\Python\Python36\lib\site-packages\ansible\modules\windows\win_ping.py"
    result = shell_module.build_module_command(env_string='', shebang='#!python', cmd=module_cmd, arg_path=None)
    assert '"C:\\Program Files\\Python\\Python36\\lib\\site-packages\\ansible\\modules\\windows\\win_ping.py.ps1"' in result
    assert " -EncodedCommand " in result

    # Bin

# Generated at 2022-06-13 14:56:49.485722
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module is not None

# Generated at 2022-06-13 14:56:56.001813
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test for old style of constructing class
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.IS_WINDOWS
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'

# Generated at 2022-06-13 14:57:02.267724
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    """Tests the ShellModule.mkdtemp() method.

    This method is used by the raw connection plugin.
    If this test fails, `ansible-playbook --connection=local` will not work.
    """
    shell_module = ShellModule(connection=None, no_log=True)

    empty_cmd = shell_module.mkdtemp()
    assert len(empty_cmd) > 10
    assert empty_cmd[:10].lower() == b'powershell '

    # Test that escaping happens.
    # Otherwise, the temp directory path will have backslashes in the name,
    # and the NTFS file system won't accept it.
    basefile_cmd = shell_module.mkdtemp(basefile="test'ing.exe")
    assert b'\'test\\\'ing.exe\'' in basefile_cmd

   

# Generated at 2022-06-13 14:57:13.327119
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    sm = ShellModule()
    script = sm.mkdtemp('/tmp')

# Generated at 2022-06-13 14:57:20.631709
# Unit test for constructor of class ShellModule
def test_ShellModule():
    cmd = 'cd /tmp'
    obj = ShellModule()
    # changes to base64 encoded string
    assert(obj._encode_script(cmd) == 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -Command $([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String(\'YwBwAGwAYwBhAHMAIAA9ACAAJABzACAAPQAgACQAZgBmAGUAcgBvAGMAbwBmAHQALgBlAHgAZQA7ABYAdAByAGUAcwBzAGkAbwBuAFwAOwAgADsA\n\')))')
    # no changes
    assert(obj._escape(cmd) == cmd)
    # removes quotes

# Generated at 2022-06-13 14:57:29.215183
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None, play_context=None, shell_executable='powershell', shell_type='powershell', stdin=None, stdin_add_newline=True,
                        override_ansible_cfg=False, binary_module=False)

    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.SHELL_NAME == 'powershell'
    assert shell.SHELL_TYPE == 'powershell'
    assert shell.SHELL_EXECUTABLE == 'powershell'

    assert hasattr(shell, 'DEFAULT_ARGS')
    assert shell.DEFAULT_ARGS == '-NoProfile -NonInteractive -ExecutionPolicy Unrestricted'


# Generated at 2022-06-13 14:57:36.486474
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell = ShellModule()
    assert shell.expand_user('~') == 'UHVibGljOg==\r\n'
    assert shell.expand_user('~\\') == 'UHVibGljOg==\r\n'
    assert shell.expand_user('~\\test') == 'UHVibGljOlx0ZXN0\r\n'
    assert shell.expand_user('C:\\test') == 'Qzpc\r\n'
    assert shell.expand_user('C:\\test\\') == 'Qzpc\\\r\n'
    assert shell.expand_user('C:\\test\\test2') == 'Qzpc\\\r\n'
    assert shell.expand_user('test') == 'test\r\n'
   

# Generated at 2022-06-13 14:57:37.742739
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell is not None

# Generated at 2022-06-13 14:57:39.216218
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sh = ShellModule()
    isinstance(sh, ShellModule)


# Generated at 2022-06-13 14:57:45.325388
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert isinstance(module, ShellModule)


# Generated at 2022-06-13 14:57:53.753317
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.executor.powershell.common import CMD_CACHE
    from ansible.executor.powershell.common import CMD_CACHE_LOCK
    from ansible.executor.powershell.common import PS_DETECTION_SCRIPT
    from ansible.executor.powershell.common import POWER_SHELL_ENV_VARS
    from ansible.executor.powershell.common import WINRM_POWERSHELL_INIT_SCRIPT

    class ShellModuleStub(ShellModule):

        def __init__(self):
            super(ShellModuleStub, self).__init__()
            self.args = {}
            self.returncode = 0

        def _encode_script(self, script, *args, **kwargs):

            return script


# Generated at 2022-06-13 14:58:03.187919
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.executor.powershell.module_common import ShellModule

    shell_module = ShellModule()

    x = shell_module.mkdtemp(basefile='ansible-tmp-', system=False, mode=None, tmpdir=None)
    assert to_bytes(x) == to_bytes('& $env:ANSIBLE_POWERSHELL_SHIM='
                                   '$env:TEMP\\ansible-tmp-* '
                                   'Powershell -NoProfile -NonInteractive '
                                   '-ExecutionPolicy Bypass -Command '
                                   '-')

    x = shell_module.mkdtemp(basefile='ansible-tmp-', system=False, mode=None, tmpdir='/tmp')

# Generated at 2022-06-13 14:58:04.221736
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 14:58:08.585770
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule()
    cmd = shell.build_module_command("env_string", "#!powershell", "-Command&", "/tmp/arg_path")
    assert cmd.startswith("type ")
    assert cmd.endswith(" | ")
    assert cmd.count("|") == 1


# Generated at 2022-06-13 14:58:09.663559
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule()
    assert plugin and ShellModule



# Generated at 2022-06-13 14:58:10.516688
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()


# Generated at 2022-06-13 14:58:16.967676
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.utils.path import unfrackpath
    from ansible.plugins.shell import ShellModule
    shell = ShellModule()
    path = '/tmp/'
    basefile = 'test_file'
    remote_user = None
    remote_pass = None
    remote_port = None
    private_key_file = None
    remote_tmp = None
    variable_manager = None
    loader = None
    success_key = "changed"
    success_rc = None
    tmp = shell.mkdtemp(basefile=basefile, tmpdir=path, system=True)
    if tmp:
        print("All tests passed")

# Generated at 2022-06-13 14:58:27.205514
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    # TODO: use parametrized test and inject data as input values

# Generated at 2022-06-13 14:58:35.541616
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    '''
    Test ShellModule.build_module_command().
    '''
    import os

    from ansible.compat.tests import unittest
    from ansible.executor.powershell.shell_wrappers import ShellModule

    # Path to bootstrap_wrapper.ps1
    bootstrap_wrapper_ps1 = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
                                         "executor", "powershell", "bootstrap_wrapper.ps1")

    with open(bootstrap_wrapper_ps1, "r") as f:
        bootstrap_wrapper = f.read()

    class TestShellModule(unittest.TestCase):
        def setUp(self):
            self.shell_module = ShellModule

# Generated at 2022-06-13 14:58:40.696096
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule(**{})
# end of test_ShellModule

# Generated at 2022-06-13 14:58:41.308063
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 14:58:47.037985
# Unit test for constructor of class ShellModule
def test_ShellModule():

    # Constructor
    powerShell = ShellModule()

    assert powerShell._SHELL_REDIRECT_ALLNULL == '> $null', 'Redirect all to null failed'
    assert powerShell._SHELL_AND == ';', 'And operation failed'
    assert powerShell._IS_WINDOWS == True, 'ShellModule is not configured for Windows'



# Generated at 2022-06-13 14:58:47.559668
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule != None

# Generated at 2022-06-13 14:58:49.404928
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()

    assert 'PowerShell' == module.COMPATIBLE_SHELLS[0]
    assert 'powershell' == module.SHELL_FAMILY
    assert True == module._IS_WINDOWS


# Generated at 2022-06-13 14:58:50.984914
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm is not None



# Generated at 2022-06-13 14:59:01.282585
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    m = ShellModule()
    # Test with shebang == '#!powershell'
    test_cmd = m.build_module_command(
        env_string='$false',
        shebang='#!powershell',
        cmd='Test-Path -PathType Leaf $env:TEST_FILE_NAME',
    )
    assert test_cmd == 'type Test-Path -PathType Leaf $env:TEST_FILE_NAME | '\
        '& {$ErrorActionPreference = "Stop"; $ProgressPreference = "SilentlyContinue";'\
        '$false;[System.Convert]::FromBase64String((Get-Content -Encoding Byte -ReadCount 0 ZgBAAEAAAAAAQAAAAAAAAAAAAAAAAD/////AAAA'\
        'AA==))|iex; }; exit $LASTEXITCODE'

   

# Generated at 2022-06-13 14:59:05.481971
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS is True


# Generated at 2022-06-13 14:59:11.264265
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule({})
    shebang = '#!/usr/bin/env python'
    cmd = 'get_url'
    assert shell.build_module_command('', shebang, cmd) == shebang + ' ' + cmd
    cmd = 'get_url foo.pl'
    assert shell.build_module_command('', shebang, cmd) == shebang + ' ' + cmd
    cmd = 'get_url foo.pl'
    shebang = '#!powershell'
    assert shell.build_module_command('', shebang, cmd) == '''type "foo.pl" | & $input | Out-String | %{{ $_ }}
'''
    cmd = 'get_url foo.pl'
    shebang = '#!/usr/bin/env python'

# Generated at 2022-06-13 14:59:14.363373
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    sh = ShellModule()
    script = sh.mkdtemp(basefile='test_hostname_module')
    assert script.startswith('$tmp_path = [System.Environment]::ExpandEnvironmentVariables(\'c:\\users')
    assert 'Write-Output -InputObject $tmp.FullName' in script

# Generated at 2022-06-13 14:59:24.823714
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()
    temp_dir = shell.mkdtemp('testing')
    assert isinstance(temp_dir, str)
    assert temp_dir.startswith('powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand ')
    assert 'New-Item -Type Directory -Path %TMP% -Name testing' in temp_dir
    assert 'Write-Output -InputObject $tmp.FullName' in temp_dir



# Generated at 2022-06-13 14:59:27.813708
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''ShellModule has a class method called test'''
    assert not ShellModule.test('powershell')
    assert ShellModule.test('powershell', 'winrm')
    assert ShellModule.test('powershell', 'psrp')
    assert ShellModule.test('powershell', 'ssh')

# Generated at 2022-06-13 14:59:32.072998
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule()
    assert shell_obj.SHELL_FAMILY == 'powershell'
    assert 'powershell' not in shell_obj.COMPATIBLE_SHELLS
    assert shell_obj.COMPATIBLE_SHELLS == set()


# Generated at 2022-06-13 14:59:42.354170
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    class Options(object):
        module_name = 'ShellModule'
        connection = 'ssh'
        new_stdin = None
        remote_tmp = '%USERPROFILE%'

    class Runner(object):
        def __init__(self, **kwargs):
            pass

        def _shell(self):
            return ShellModule(runner=self, **kwargs)

    class PlayContext(object):
        def __init__(self, **kwargs):
            self.connection = 'local'
            self.network_os = 'default'
            self.remote_addr = None
            self.remote_user = None
            self.password = None
            self.port = None
            self.private_key_file = None
            self.timeout = 10
            self.shell = None
            self.become = False

# Generated at 2022-06-13 14:59:48.089578
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule(connection='winrm')
    s = ShellModule(connection='psrp')
    s = ShellModule(connection='ssh', **{
        'ansible_shell_type': 'powershell',
        'ansible_shell_executable': 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'})
    assert s.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:59:49.962844
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_TYPE == 'powershell'
    assert module._IS_WINDOWS

# Generated at 2022-06-13 14:59:58.212408
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.plugins.shell.powershell import ShellModule
    s = ShellModule()
    # test without tmpdir and without basefile
    t1 = s.mkdtemp()
    assert t1.startswith('$tmp_path = [System.Environment]::ExpandEnvironmentVariables(\'C:\\\\Users\\\\')
    assert t1.endswith('); $tmp = New-Item -Type Directory -Path $tmp_path -Name \'ansible_test_dir_\'; Write-Output -InputObject $tmp.FullName')
    # test with tmpdir and with basefile
    t2 = s.mkdtemp('test_dir', tmpdir='C:\\\\test\\\\')

# Generated at 2022-06-13 14:59:59.286470
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule('')

# Generated at 2022-06-13 15:00:02.367119
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Constructor of the ShellModule class
    """
    obj = ShellModule(None)
    assert isinstance(obj, ShellModule)

    return True


# Generated at 2022-06-13 15:00:10.217718
# Unit test for constructor of class ShellModule
def test_ShellModule():

    shell = ShellModule()

    args = ['foo1', 'foo2', 'foo3', 'foo4']
    script = shell.join_path(*args)
    assert script == 'foo1\\foo2\\foo3\\foo4'

    args = ['', 'foo2', 'foo3', 'foo4']
    script = shell.join_path(*args)
    assert script == 'foo2\\foo3\\foo4'

    args = ['', '', '', 'foo4']
    script = shell.join_path(*args)
    assert script == 'foo4'

# Generated at 2022-06-13 15:00:25.290330
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()

    # Test sanity of plugin
    assert module.get_remote_filename('test') == 'test.ps1'
    assert module.get_remote_filename('test.ps1') == 'test.ps1'

    # Test path normalization
    assert module.join_path('test\\test', 'test') == module.join_path('test\\test\\test')
    assert module.path_has_trailing_slash('test\\test')
    assert not module.path_has_trailing_slash('test')

    # Test exception handling
    try:
        module.chmod(None, None)
    except NotImplementedError:
        pass
    else:
        assert False, "chmod() should raise NotImplementedError"


# Generated at 2022-06-13 15:00:34.791188
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test that the module checks for existence of the remote_tmp path
    def tmpexists(module):
        return True
    ShellModule.exists = tmpexists

    # Override hostname to test the default temp directory
    class Hostname:
        name = 'localhost'
    Hostname.default = Hostname.name

    # Test module without remote_tmp defined
    module = ShellModule(Hostname)
    assert module
    assert module.tmpdir == 'C:\\Windows\\Temp'

    # Test module with remote_tmp defined
    module = ShellModule(Hostname, remote_tmp='C:\\Temp')
    assert module
    assert module.tmpdir == 'C:\\Temp'

    # Test user home path without ~username is expanded

# Generated at 2022-06-13 15:00:38.919385
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    assert ShellModule(run_command_environ_update={}).mkdtemp(basefile='test.py') == 'IgBlAHkAbABvACAAJwByAGUAZwBpAG4AYQB0AGkAdAB5ACAAJwBuAGgAbABsACAAJwBuAGUAdAAuAHAAcgBvAGQAZQBuACAAJwBmAG8AcgBtAGEAdABlAA=='

# Generated at 2022-06-13 15:00:40.754427
# Unit test for constructor of class ShellModule
def test_ShellModule():
    x = ShellModule()
    assert x._IS_WINDOWS
    assert x.COMPATIBLE_SHELLS == frozenset()
    assert x.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:44.336987
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_module._SHELL_AND == ';'
    assert shell_module._IS_WINDOWS == True
    assert shell_module.COMPATIBLE_SHELLS == frozenset()
    assert shell_module.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:52.430864
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()
    basefile = 'a' * 10 + '_'
    expected = '''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('%s')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name '%s'
        Write-Output -InputObject $tmp.FullName
        ''' % (shell.get_option('remote_tmp'), basefile)
    assert expected.strip() == shell.mkdtemp(basefile=basefile, system=False, mode=None, tmpdir=None).strip()

# Generated at 2022-06-13 15:00:57.557885
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule._IS_WINDOWS
    assert ShellModule.SHELL_FAMILY == 'powershell'
    assert ShellModule.COMPATIBLE_SHELLS == frozenset()
    assert ShellModule._SHELL_AND == ';'
    assert ShellModule._SHELL_REDIRECT_ALLNULL == '> $null'



# Generated at 2022-06-13 15:01:00.319601
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()
    result = shell.mkdtemp()
    assert len(result) >= 0, "Length of the result is not non-negative."
    assert isinstance(result, str), "Returned value is not a string as expected."

# Generated at 2022-06-13 15:01:09.156706
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    path = '/tmp/ansible_test_tmp_23648982'
    path_expected = '/tmp/ansible_test_tmp_23648982'
    path_contains = '__tmp_'
    user = 'anonymous'
    env = {}
    mode = None
    prefix = 'ansible_test_tmp_'
    tmpdir = '/tmp'

    plugin = ShellModule()
    result = plugin.mkdtemp(basefile=path, system=False, mode=None, tmpdir=tmpdir)
    assert path_contains in result
    assert result.find(path_expected) != -1

# Generated at 2022-06-13 15:01:11.641365
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule()
    assert shell_obj._IS_WINDOWS is True
    assert shell_obj._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_obj._SHELL_AND == ';'

# Generated at 2022-06-13 15:01:16.498439
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule._IS_WINDOWS

# Generated at 2022-06-13 15:01:19.603542
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """This is a dummy test used to test the constructor of the class ShellModule"""
    shell_obj = ShellModule()
    assert shell_obj is not None


# Generated at 2022-06-13 15:01:25.617284
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from units.compat import unittest
    from ansible.executor.powershell import ShellModule
    powershell = ShellModule()
    assert powershell
    assert powershell.SHELL_FAMILY == 'powershell'
    assert powershell.COMPATIBLE_SHELLS == frozenset()
    assert powershell._IS_WINDOWS
    assert powershell._SHELL_AND == ';'

# Generated at 2022-06-13 15:01:29.585223
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None,dos_compatible=None)
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS == True
    assert shell.DEFAULT_EXECUTABLE == 'powershell.exe'

# Generated at 2022-06-13 15:01:36.127123
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule(connection=None)
    assert shell_obj.connection == None
    assert list(_common_args) == ['PowerShell', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Unrestricted']
    assert shell_obj._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_obj._SHELL_AND == ';'
    assert shell_obj._IS_WINDOWS == True

# Generated at 2022-06-13 15:01:37.588088
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod is not None



# Generated at 2022-06-13 15:01:41.021313
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.get_option('tmpdir') == '$env:TEMP', 'tmpdir value is not correct'
    assert module.get_option('executable') == '', 'executable value is not correct'

# Generated at 2022-06-13 15:01:45.694815
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()
    s.get_remote_filename('setup.py')
    # Checking if the file has a trailing directory or not.
    assert s.path_has_trailing_slash('')
    assert s.path_has_trailing_slash('\\')
    assert s.path_has_trailing_slash('/')
    assert not s.path_has_trailing_slash('a')


# Generated at 2022-06-13 15:01:47.773241
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS is True

# Generated at 2022-06-13 15:01:51.485129
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod.COMPATIBLE_SHELLS == frozenset()
    assert mod.SHELL_FAMILY == 'powershell'
    assert mod._IS_WINDOWS == True



# Generated at 2022-06-13 15:01:57.509526
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.executor.powershell as ps
    sm = ps.ShellModule()

    if not isinstance(sm, ps.ShellModule):
        raise AssertionError("Not an instance of ShellModule")



# Generated at 2022-06-13 15:02:03.081380
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_module._SHELL_AND == ';'
    assert shell_module._IS_WINDOWS == True
    assert shell_module._SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:02:03.877791
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()

# Generated at 2022-06-13 15:02:05.242333
# Unit test for constructor of class ShellModule
def test_ShellModule():
    my_shell = ShellModule()
    assert my_shell is not None

# Generated at 2022-06-13 15:02:12.626345
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()

    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'

    assert shell.get_remote_filename(shell._unquote('c:\\users\\foo\\file.txt')) == 'file.txt'
    assert shell.get_remote_filename(shell._unquote('c:\\users\\foo\\file')) == 'file.ps1'

    # normalizes slashes, that's all
    assert shell.join_path(shell._unquote('c:\\users'), shell._unquote('file.txt')) == 'c:\\users\\file.txt'
    assert shell.join_path('c:\\users', '..\\file.txt') == 'c:\\file.txt'

    assert shell.path_has_trailing_

# Generated at 2022-06-13 15:02:15.682400
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_mod = ShellModule()
    assert shell_mod._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_mod._SHELL_AND == ';'

# Generated at 2022-06-13 15:02:18.673910
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """This is a unit test for the constructor of ShellModule class."""
    import ansible.executor.powershell.shell as shell
    sm = shell.ShellModule()
    assert isinstance(sm, shell.ShellModule)


# Generated at 2022-06-13 15:02:19.328229
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 15:02:22.016581
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert(shell.SHELL_FAMILY == 'powershell')
    assert(shell.COMPATIBLE_SHELLS == frozenset())
    assert(shell._IS_WINDOWS == True)

# Generated at 2022-06-13 15:02:24.229421
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule(None).SHELL_FAMILY == 'powershell'
    assert ShellModule(None).COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:02:29.016045
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell is not None
    assert 'powershell' in str(shell)

# Generated at 2022-06-13 15:02:36.536634
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    """
    :return: True if all tests pass otherwise False
    """

    class FakeModule():
        def __init__(self):
            self.LOAD_FILTER = ('a', 'b')
            self.args = None

    fake_module = FakeModule()

    class FakeTask():
        def __init__(self):
            self.args = dict()

    fake_task = FakeTask()

    task_vars = dict()

    inject = dict()

    task_vars['ansible_powershell_shell'] = '/usr/bin/pwsh -NoLogo -NoProfile -NonInteractive -Command -'

    # Test for known use case in which the module is a binary

# Generated at 2022-06-13 15:02:37.926482
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:02:40.420665
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod._SHELL_REDIRECT_ALLNULL
    assert mod._SHELL_AND
    assert mod._IS_WINDOWS

# Generated at 2022-06-13 15:02:42.304319
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test constructor of ShellModule
    shell_mod = ShellModule()
    assert shell_mod is not None



# Generated at 2022-06-13 15:02:42.857550
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()

# Generated at 2022-06-13 15:02:44.706111
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module_test = ShellModule()

    if shell_module_test is None:
        raise Exception('Failed to instantiate a ShellModule object')

# Generated at 2022-06-13 15:02:46.308665
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:02:48.502452
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection=None)
    script = "Get-ChildItem"

    module._encode_script(script, as_list=False, strict_mode=False, preserve_rc=False)

# Generated at 2022-06-13 15:02:55.034086
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test shell module is correctly initialized
    shell_module = ShellModule()

    assert isinstance(shell_module, ShellBase)
    assert hasattr(shell_module, 'env_prefix')
    assert hasattr(shell_module, 'join_path')
    assert hasattr(shell_module, 'get_remote_filename')
    assert hasattr(shell_module, '_DONT_USE_CHMOD')
    assert hasattr(shell_module, '_DONT_USE_CHOWN')
    assert hasattr(shell_module, 'set_user_facl')
    assert hasattr(shell_module, 'remove')
    assert hasattr(shell_module, 'mkdtemp')
    assert hasattr(shell_module, 'expand_user')
    assert hasattr(shell_module, 'exists')

# Generated at 2022-06-13 15:03:04.734875
# Unit test for constructor of class ShellModule
def test_ShellModule():
    pass

# Generated at 2022-06-13 15:03:15.967743
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import ansible.executor.module_common
    import ansible.module_utils.powershell
    import io

    def encode_module(module_data, output=None, shebang_override=None):
        if output is None:
            output = io.BytesIO()

        if not isinstance(module_data, bytes):
            module_data = to_bytes(module_data)

        output_data = ansible.utils.module_docs.get_docstring(module_data,
                                                              follow_imports=True,
                                                              ignore_errors=True)
        if output_data and output_data.strip() != b'':
            output.write(output_data)
            output.write(b'\n')

        if shebang_override is not None:
            shebang = shebang_over

# Generated at 2022-06-13 15:03:21.093108
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule()
    assert shell_obj.COMPATIBLE_SHELLS == ShellModule.COMPATIBLE_SHELLS
    assert shell_obj.SHELL_FAMILY == ShellModule.SHELL_FAMILY
    assert shell_obj._SHELL_REDIRECT_ALLNULL == ShellModule._SHELL_REDIRECT_ALLNULL
    assert shell_obj._SHELL_AND == ShellModule._SHELL_AND
    assert shell_obj._IS_WINDOWS == ShellModule._IS_WINDOWS


# Generated at 2022-06-13 15:03:25.540816
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection='winrm')
    assert shell.connection == 'winrm'
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'
    assert shell._IS_WINDOWS == True


# Generated at 2022-06-13 15:03:26.831222
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.IS_WINDOWS is True



# Generated at 2022-06-13 15:03:28.233091
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()
    assert isinstance(s, ShellBase)



# Generated at 2022-06-13 15:03:29.165649
# Unit test for constructor of class ShellModule
def test_ShellModule():
    res = ShellModule()
    assert res is not None

# Generated at 2022-06-13 15:03:30.387524
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:03:37.535986
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.executor.powershell.module_utf16 as module_utf16
    import ansible.plugins.loader as plugin_loader

    loader = plugin_loader.PluginLoader()
    tmp_shell_module = loader.find_plugin('powershell', 'shell')()
    tmp_shell_module._encode_script(module_utf16.UTF16_BOM + module_utf16.UTF16_SCRIPT_WITH_BOM)

    # Test that the constructor re-encodes the script in UTF-16LE if the BOM is present
    if not tmp_shell_module.share.module_stdout.startswith(module_utf16.UTF16_BOM):
        raise AssertionError('BOM not present in script')

    # Test that the constructor re-encodes the script in UTF-16LE if BOM is

# Generated at 2022-06-13 15:03:46.521936
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import socket
    import unittest

    #TODO: make this a true unit test
    class TestShellModule(unittest.TestCase):
        ''' Exercises the ShellModule class using the local machine.'''

        def mkdtemp(self):
            ''' exercise the mkdtemp method.'''
            sm = ShellModule()
            result = sm.mkdtemp()
            self.assertTrue(result, 'get_remote_filename resulted in an empty string.')

        def temp_filename(self):
            ''' exercise the get_remote_filename method.'''
            sm = ShellModule()
            result = sm.get_remote_filename('/tmp/file.txt')
            self.assertEqual(result, 'file.txt')

        def join_path(self):
            ''' exercise the join_path method.'''


# Generated at 2022-06-13 15:03:55.731092
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm._IS_WINDOWS

# Generated at 2022-06-13 15:03:57.624639
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Testing creation of PS Shell Module"""
    ps_shell = ShellModule()
    assert isinstance(ps_shell, ShellBase)

# Generated at 2022-06-13 15:04:01.086739
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.powershell import ShellModule
    shell_mod = ShellModule()

    assert shell_mod._IS_WINDOWS
    assert shell_mod.COMPATIBLE_SHELLS == frozenset()
    assert shell_mod.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:04:02.072580
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule()
    assert obj.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:04:03.062956
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell

# Generated at 2022-06-13 15:04:04.784087
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert ''.__class__.__name__ == 'str'
    assert ''.__class__.__name__ == 'unicode'

# Generated at 2022-06-13 15:04:11.089796
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Constructor test
    # + test case with connection=None, shell_executable='powershell'
    required_args = {
        'connection': None,
        'shell_executable': 'powershell',
    }
    optional_args = {
        'no_log': False,
        'keep_remote_files': False
    }
    default_args = {
        'stdin': None,
        'stdin_add_newline': True,
        'strip_empty_ends': True,
        'env': None,
    }

# Generated at 2022-06-13 15:04:14.289478
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    shell = ShellModule(connection=None)
    assert shell.namespace() == ''
    assert shell.for_windows() is True
    '''
    pass


# Generated at 2022-06-13 15:04:15.090301
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell is not None

# Generated at 2022-06-13 15:04:24.055812
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Create an instance of the class ShellModule with correct arguments
    """
    import tempfile
    test_file_path = os.path.realpath(tempfile.mkstemp()[1])
    os.remove(test_file_path)
    test_shell = ShellModule(connection=None, src=test_file_path)

    assert test_shell.src == test_file_path, "src initialization test"

    # Validate appending of correct suffix in generating script name
    expected_suffix = ".ps1"
    test_script_name = "test_script"
    test_script_path = test_script_name + expected_suffix
    remote_script_path = test_shell.get_remote_filename(test_script_name)


# Generated at 2022-06-13 15:04:42.768956
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule(command_timeout=33)


# Generated at 2022-06-13 15:04:51.744398
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.plugins.connection.winrm
    # powershell is not executable without winrm
    if not ansible.plugins.connection.winrm.winrm_executor_class:
        return
    shell = ShellModule(connection=None, no_log=True)

# Generated at 2022-06-13 15:05:00.308384
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''Unit test for constructor of class ShellModule'''
    shell_module = ShellModule()

    assert shell_module.COMPATIBLE_SHELLS == frozenset()
    assert shell_module.SHELL_FAMILY == 'powershell'
    assert shell_module._IS_WINDOWS == True
    assert shell_module._shell.SHELL_FAMILY == 'powershell'
    assert shell_module._shell.DEFAULT_EXECUTABLE == 'powershell'
    assert shell_module._shell.SHELL_TYPE == 'powershell'
    assert shell_module._shell.BINARY_FLAGS == []
    assert shell_module._shell.HAS_PIPE == False
    assert shell_module._shell.IS_BINARY == True
    assert shell_module._shell.IS_PERSISTENT == True


# Generated at 2022-06-13 15:05:01.547079
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule()
    assert plugin.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:05:04.132566
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'
    assert module._IS_WINDOWS is True
    assert module._SHELL_AND == ';'
    assert module._shell.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:05:09.839800
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import ansible.executor.powershell
    import ansible.plugins.shell
    import ansible.plugins.loader
    import ansible.module_utils.basic

    # setup
    test_module_name = 'test_module'
    test_module_data = b'''#!powershell
    [cmdletbinding()]
    Param($test_param)
    Write-Output "test_param is $test_param"'''
    test_params = {'test_param': 'test_value'}

    test_module_path = ansible.utils.module_docs._get_doc_path() + '/' + test_module_name + '.ps1'


# Generated at 2022-06-13 15:05:11.334874
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # TODO
    pass


# Generated at 2022-06-13 15:05:12.017494
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# Generated at 2022-06-13 15:05:21.275573
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    # a null command string should produce a safe-ish bootstrap, not a fatal error
    encoded = module._encode_script('')
    assert isinstance(encoded, str) and ' ' in encoded
    # same, but with a -
    # FIXME: this should be using _encode_script when that's fixed
    encoded = module._encode_script('-')
    assert isinstance(encoded, str) and ' ' in encoded
    # test that env vars are preserved in script calls, as was previously reported by mdouglas:
    # https://github.com/ansible/ansible/issues/23953
    encoded = module._encode_script('Get-ChildItem Env:path')
    assert isinstance(encoded, str) and ' ' in encoded
    # check that _escape is escaping

# Generated at 2022-06-13 15:05:23.674706
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm._SHELL_REDIRECT_ALLNULL == '> $null'
    assert sm.COMPATIBLE_SHELLS == frozenset()


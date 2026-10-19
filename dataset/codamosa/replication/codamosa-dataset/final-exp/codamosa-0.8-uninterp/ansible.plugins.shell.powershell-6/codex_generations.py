

# Generated at 2022-06-13 14:55:41.688134
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    from ansible.plugins.shell.powershell import ShellModule
    import os
    test_command = ShellModule(connector=None)
    home = os.path.expanduser('~')
    # ~, ~\, ~\folder, C:\Users\username\AppData\Local, C:\Users\username\AppData\Local\
    # C:\Users\username\AppData\Local\folder, C:\Users\username\AppData\Local\folder\
    test_cases = ['~', '~\\', '~\\folder', home, home + '\\',
        home + '\\folder', home + '\\folder\\']
    for case in test_cases:
        # required method
        assert to_bytes(test_command.expand_user(case), errors='surrogate_or_strict')

# Generated at 2022-06-13 14:55:49.043312
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """The following methods are tested
    1. ShellModule.__init__
    """
    shell_obj = ShellModule({})
    try:
        assert shell_obj._SHELL_REDIRECT_ALLNULL == '> $null'
        assert shell_obj._SHELL_AND == ';'
        assert shell_obj._IS_WINDOWS == True
    except AssertionError:
        print("***** test_ShellModule Failed *****")
        raise
    print("***** test_ShellModule Passed *****")


# Generated at 2022-06-13 14:55:58.254079
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell_module = ShellModule()
    assert shell_module.expand_user('~') == "$Encode([Text.Encoding]::Unicode.GetBytes(\"Set-StrictMode -Version Latest\r\nif (!(Test-Path $HOME))\r\n{\r\n    Write-Output -InputObject '1'-NoNewline;\r\n    exit 1;\r\n}\r\nWrite-Output (Get-Location).Path;\r\n\"))"

# Generated at 2022-06-13 14:56:07.361017
# Unit test for constructor of class ShellModule
def test_ShellModule():
    with open('ps_test', 'wb') as f:
        f.write(b'[Environment]::CurrentDirectory')

    module = ShellModule(connection='winrm', no_log=False, become_method='runas', become_user='user', become_password='pw')

    # Test method env_prefix
    assert module.env_prefix() == ''

    # Test method expand_user

# Generated at 2022-06-13 14:56:10.285843
# Unit test for constructor of class ShellModule
def test_ShellModule():
    props_module = ShellModule(connection=None, config=None)

    assert props_module.COMPATIBLE_SHELLS == frozenset()
    assert props_module._IS_WINDOWS is True
    assert props_module.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:56:16.577290
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import random
    import string
    test_shell = ShellModule()
    basefile = "test_file_" + ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    result = test_shell.mkdtemp(basefile=basefile)
    print('result: ' + result)
    result_string_decoded = base64.b64decode(result).decode('utf-8')
    result_string_decoded = result_string_decoded.replace('\r\n', '\n')
    print(result_string_decoded)
    print(result_string_decoded.split('\n'))

# Generated at 2022-06-13 14:56:22.686956
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Create an instance of ShellModule without parameters
    sm = ShellModule()
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm.SHELL_FAMILY == 'powershell'
    assert sm._IS_WINDOWS == True
    assert sm.env_prefix() == ""
    assert sm.join_path('C:/','path','to','some','file') == 'C:/path/to/some/file'
    assert sm.get_remote_filename('./file/to/delete') == 'delete.ps1'
    assert sm.path_has_trailing_slash('./file/to/delete/') == True
    assert sm.path_has_trailing_slash('C:/') == True

# Generated at 2022-06-13 14:56:34.707898
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule(None)
    if shell.SHELL_FAMILY != 'powershell':
        raise Exception('Unit test can only be run against powershell shell plugin')


# Generated at 2022-06-13 14:56:42.928933
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.module_utils.common.text.converters import to_bytes

    # Get an instance of ShellModule class for testing
    sh = ShellModule(connection=None, no_log=None, run_command=None, become_username=None, become_method=None, become_user=None, become_exe=None, become_flags=None, become_pass=None, module_implementation_preferences=None)

    # Test shebang with powershell
    env_string = "env_string"
    shebang = '#!powershell'
    cmd = 'some module arg'
    arg_path = "arg_path"

# Generated at 2022-06-13 14:56:51.568665
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():

    ## Powershell for Windows
    import ansible.constants as C
    from ansible.module_utils.six import text_type
    from ansible.executor.module_common import module_response_deepcopy

    # from ansible.compat.tests.mock import patch
    from ansible.plugins.loader import module_loader

    # getting our modules
    module_loader.add_directory(C.DEFAULT_MODULE_PATH)

    mod = module_loader.get_module_path('ping', 'network/ping')

    # setting no_log to True in order to suppress any output
    # this is the only way I found to suppress module's output in Ansible 2.2.2.0

# Generated at 2022-06-13 14:57:04.373743
# Unit test for constructor of class ShellModule
def test_ShellModule():

    shell_module = ShellModule()
    assert type(shell_module) == ShellModule
    assert shell_module.COMPATIBLE_SHELLS == frozenset()
    assert shell_module.SHELL_FAMILY == 'powershell'
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_module._SHELL_AND == ';'
    assert shell_module._IS_WINDOWS

    assert shell_module.env_prefix() == ""
    assert shell_module.join_path("C:", "Users", "Administrator", "Desktop") == "C:\\Users\\Administrator\\Desktop"
    assert shell_module.join_path("C:", "Users", "Administrator", "Desktop\\") == "C:\\Users\\Administrator\\Desktop"
    assert shell_module.join

# Generated at 2022-06-13 14:57:10.516238
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell_module = ShellModule()

    test_string = "function New-RandomFileName() { return 'tmp9r9y1h'; }"

    expected_output_list = ['powershell', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Unrestricted', 
        '-Command', '$tmp_path = [System.Environment]::ExpandEnvironmentVariables(\'C:\\\\temp\\\\ansible\')', 
        '$tmp = New-Item -Type Directory -Path $tmp_path -Name \'tmp9r9y1h\'', 'Write-Output -InputObject $tmp.FullName']

    output_list = shell_module.mkdtemp(tmpdir='C:\\temp\\ansible', basefile='tmp9r9y1h', system=False, mode=None)


# Generated at 2022-06-13 14:57:19.612481
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.module_utils._text import to_bytes
    shell = ShellModule.load_shell_plugin(None, connection="winrm", task_uuid='123')
    cmd = 'add-content "$env:TEMP\\123" "hello world"'
    shebang = '#!powershell'
    arg_path = '"$env:TEMP\\123"'
    env_string = '$env:ANSIBLE_CONNECTION="winrm";$env:ANSIBLE_REMOTE_TEMP="$env:TEMP"'
    wrapped = shell.build_module_command(env_string, shebang, cmd, arg_path)

    # check for expected command output

# Generated at 2022-06-13 14:57:27.154264
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell_mod = ShellModule()
    env_string = '$env:http_proxy="http://http_proxy.com:3128"'
    shebang = "#!pwsh"
    cmd = '$cf = Get-Content -Encoding UTF8 -Path "~/d/ps_script.ps1"'
    assert shell_mod.build_module_command(env_string, shebang, cmd) == shell_mod._encode_script(script='''$env:http_proxy="http://http_proxy.com:3128"
                $cf = Get-Content -Encoding UTF8 -Path "~/d/ps_script.ps1"''')

# Generated at 2022-06-13 14:57:28.762053
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sh = ShellModule()
    assert isinstance(sh, ShellModule)

# Generated at 2022-06-13 14:57:36.237398
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.plugins.shell.powershell import ShellModule, _common_args, _SHELL_AND
    sm = ShellModule(command_timeout=15, tmpdir='c:/tmp')
    assert sm.build_module_command('', '', '', '') == ' '.join(_common_args + ['-Command', '& echo Redirecting to null.\n1 > $null ' + _SHELL_AND + ' exit $LASTEXITCODE'])

# Generated at 2022-06-13 14:57:40.675395
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell_module = ShellModule()
    cases = [
        ("~", 'Write-Output $env:UserProfile'),
        ("~/test.txt", "Write-Output ((Get-Location).Path + '\\test.txt')"),
        ("~~/test.txt", "Write-Output ((Get-Location).Path + '\\test.txt')")
    ]
    for input, expected in cases:
        actual = shell_module.expand_user(input)
        assert actual == expected, "expected %s, got %s" % (expected, actual)


# Generated at 2022-06-13 14:57:43.504952
# Unit test for constructor of class ShellModule
def test_ShellModule():
    powershell = ShellModule()
    assert(powershell._IS_WINDOWS)
    assert(powershell.SHELL_FAMILY == 'powershell')
    assert('#!powershell' in powershell.COMPATIBLE_SHELLS)
    assert(powershell.COMPATIBLE_SHELLS['#!powershell'] == 'Windows PowerShell')

# Generated at 2022-06-13 14:57:44.904503
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test instantiating the class
    assert ShellModule()


# Generated at 2022-06-13 14:57:53.489686
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():

    powershell = ShellModule()

    env_string = '$env:ANSIBLE_MODULE_ARGS=\'{\"key\":\"value\"}\''
    shebang = '#!powershell'
    cmd = '/usr/bin/python /tmp/ansible_test.py'
    arg_path = '/tmp/ansible_test.py'


# Generated at 2022-06-13 14:58:02.525715
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    Test whether or not the constructor of ShellModule works properly.
    '''

    if ShellModule.SHELL_FAMILY != 'powershell':
        raise AssertionError("SHELL_FAMILY must be 'powershell'.")

    if not ShellModule.COMPATIBLE_SHELLS:
        raise AssertionError("COMPATIBLE_SHELLS must be an empty set.")

    if not ShellModule._IS_WINDOWS:
        raise AssertionError("_IS_WINDOWS must be True.")

    # Check if the ShellModule is properly inherited
    if not issubclass(ShellModule, ShellBase):
        raise AssertionError("ShellModule must be inherited from ShellModule.")

    # Check if ShellModule is instance of ShellBase

# Generated at 2022-06-13 14:58:09.390676
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection='winrm', no_log=False)
    assert shell.connection == 'winrm'
    assert not shell.no_log
    shell = ShellModule(connection='winrm', no_log=True)
    assert shell.connection == 'winrm'
    assert shell.no_log
    shell = ShellModule(connection='winrm', no_log=False)
    assert shell.connection == 'winrm'
    assert not shell.no_log
    shell = ShellModule(connection='ssh', no_log=False)
    assert shell.connection == 'ssh'
    assert not shell.no_log
    shell = ShellModule(connection='ssh', no_log=True)
    assert shell.connection == 'ssh'
    assert shell.no_log


# Generated at 2022-06-13 14:58:10.207131
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert issubclass(ShellModule, ShellBase)

# Generated at 2022-06-13 14:58:20.851840
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell = ShellModule()

    # test for:
    #  - current user home directory
    #  - current user home directory, and add a relative path
    #  - explicit user, and add a relative path
    #  - explicit user and home directory, and add a relative path
    #  - explicit user and home directory, and add a relative path

# Generated at 2022-06-13 14:58:29.455404
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import datetime
    import json
    import sys

    class EmptyModule(object):
        RUN_OK = 0
        FAILED = 1

        def __init__(self):
            self.exit_args = None
            self.exit_code = None
            self.distribution = None

        def exit_json(self, **kwargs):
            self.exit_args = kwargs
            self.exit_code = self.RUN_OK

        def fail_json(self, **kwargs):
            self.exit_args = kwargs
            self.exit_code = self.FAILED

    def test(shell, command, expected_rc, expected_stdout, expected_stderr, expected_args):
        my_shell = shell(create_tmppath=lambda: tempfile.mkdtemp())
        my_

# Generated at 2022-06-13 14:58:38.685531
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    if os.name == 'nt':
        assert 'PowerShell' == module.get_remote_filename('test')
        assert 'PowerShell' == module.get_remote_filename('test.ps1')
        assert 'test.TXT' == module.get_remote_filename('test.TXT')
    assert module.build_module_command('test', '', '', '') == module.build_module_command('test', '', '')
    assert module.build_module_command('test', None, '') == module.build_module_command('test', '', '')
    assert module.build_module_command('test', None, '') == module.build_module_command('test', None, '')
    assert module.build_module_command('test', '#!/usr/bin/', '')

# Generated at 2022-06-13 14:58:49.765353
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    print (module.get_remote_filename('/path/to/file'))
    print (module.get_remote_filename('/path/to/file.txt'))
    print (module.get_remote_filename('/path/to/file.'))
    print (module.get_remote_filename('/path/to/file.exe'))
    print (module.get_remote_filename('/path/to/file.bash'))
    print (module.get_remote_filename('/path/to/file.PS1'))
    print (module.get_remote_filename('/path/to/file.bat'))
    print (module.get_remote_filename('/path/to/file.cmd'))

# Generated at 2022-06-13 14:58:51.097104
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection='winrm')
    print(shell)

# Generated at 2022-06-13 14:58:57.738018
# Unit test for constructor of class ShellModule
def test_ShellModule():

    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'

    script = 'Set-StrictMode -Version Latest\n'
    script += 'Write-Output "Test"'
    encoded_script = to_text(base64.b64encode(script.encode('utf-16-le')), 'utf-8')
    cmd_parts = _common_args + ['-EncodedCommand', encoded_script]
    assert module._encode_script(script) == ' '.join(cmd_parts)


# Generated at 2022-06-13 14:59:06.113731
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    # Set up environment
    old_environ = dict(os.environ)

# Generated at 2022-06-13 14:59:11.808990
# Unit test for constructor of class ShellModule
def test_ShellModule():
    test_shell = ShellModule()
    assert test_shell is not None


# Generated at 2022-06-13 14:59:23.508545
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # bootstrap_wrapper.ps1 is in ansible.executor.powershell, but we have to
    # import it here because the powershell plugin is imported prior to ansible.executor.powershell
    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")

    # mock env_string, cmd, arg_path, and module_path
    env_string = "echo hello"
    cmd = "1"
    arg_path = "2"
    module_path = "3"

    testCase_list = []

    # case 1: shebang is empty, cmd is quoted, and is_powershell_to_exe_conversion is false
    shebang = ""
    is_powershell_to_exe_conversion = False

# Generated at 2022-06-13 14:59:25.007309
# Unit test for constructor of class ShellModule
def test_ShellModule():
    python = ShellModule(connection=None, run_command_environ_update=None,
                         tmpdir=None, module_compression=None, module_name=None)
    assert isinstance(python, ShellModule)

# Generated at 2022-06-13 14:59:27.753645
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert hasattr(shell, 'IS_WINDOWS')
    assert hasattr(shell, 'SHELL_FAMILY')
    assert hasattr(shell, 'COMPATIBLE_SHELLS')
    assert shell.IS_WINDOWS
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()



# Generated at 2022-06-13 14:59:29.586241
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule(connection=None, add_date=False)
    assert isinstance(sm, ShellBase)

# Generated at 2022-06-13 14:59:31.846158
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'

if __name__ == '__main__':
    test_ShellModule()

# Generated at 2022-06-13 14:59:42.076106
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # tests for legacy modules
    shell = ShellModule()
    # No shebang, no command

# Generated at 2022-06-13 14:59:52.181163
# Unit test for constructor of class ShellModule
def test_ShellModule():
    cmd_set = ShellModule()
    cmd_set.get_remote_filename('/tmp/test.sh')
    cmd_set.join_path('/tmp/a')
    cmd_set.wrap_for_exec('/tmp/test.sh')
    cmd_set.wrap_for_exec('/tmp/test.sh', 'test')
    cmd_set.get_remote_filename('/tmp//test.sh')
    cmd_set.join_path('/tmp', '/a')
    cmd_set.join_path('/tmp', 'a/')
    cmd_set.join_path('/tmp/', '/a/')
    cmd_set.join_path('/tmp/a', '/b')
    cmd_set.join_path('/tmp\\a', '/b')

# Generated at 2022-06-13 14:59:53.415499
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sn = ShellModule()
    assert sn.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:00.566576
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell = ShellModule()

    # Test when path is relative and comes along with username
    assert shell.expand_user('~testadmin', 'testadmin') == shell._encode_script(script="Write-Output '~testadmin'")

    # Test when path is relative and user name is not provided
    assert shell.expand_user('~testadmin', '') == shell._encode_script(script="Write-Output '~testadmin'")

    # Test when path is absolute and comes along with username
    assert shell.expand_user('~testadmin/temp', 'testadmin') == shell._encode_script(script="Write-Output '~testadmin/temp'")

    # Test when path is absolute and user name is not provided

# Generated at 2022-06-13 15:00:16.817358
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.module_utils._text import to_text
    a = ShellModule(conn=None)

    # Test exists
    assert a.exists('foo') == to_text(
        "$ansible_module_generated=1; Invoke-Expression -Command (If (Test-Path 'foo'){ $res = 0; }Else{ $res = 1; } ); Write-Output '$res'; Exit $res"
    )

    # Test get_remote_filename
    assert a.get_remote_filename('/foo/bar.txt') == 'bar.txt'
    assert a.get_remote_filename('/foo/bar') == 'bar.ps1'

    # Test join_path
    assert a.join_path('C:', 'foo\\bar') == 'C:\\foo\\bar'
    assert a.join_

# Generated at 2022-06-13 15:00:18.132199
# Unit test for constructor of class ShellModule
def test_ShellModule():

    assert(ShellModule() is not None)


# Generated at 2022-06-13 15:00:25.669516
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None)
    for k, v in ShellModule.__dict__.items():
        if type(v) == property:
            assert shell.__dict__[k] == v.fget(shell)
    assert len(shell.COMPATIBLE_SHELLS) == 0
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS == True
    assert shell.env_prefix() == ''


# Generated at 2022-06-13 15:00:32.900789
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    module_cmd = ShellModule.build_module_command('', '', 'Test-File')

    assert re.search(r'^(?s)Type \s*?(?P<filename>Test-File).ps1 \s*?\| \s*?.*?', module_cmd, re.MULTILINE | re.DOTALL)
    assert re.search(r'(?s)\| \s*?%s \s*?$' % _common_args[0], module_cmd, re.MULTILINE | re.DOTALL)


# Generated at 2022-06-13 15:00:36.344574
# Unit test for constructor of class ShellModule
def test_ShellModule():
    args = dict(
        executable='/bin/sh',
        stdin='',
        stdout=-1,
        stderr=-1,
        become_user='zach',
        become_pass='',
        module_name='shell',
        module_args='',
        _raw_params='',
        _uses_shell=True,
        _ansible_shell_executable='/bin/sh',
        _ansible_no_log=False)
    sm = ShellModule(**args)
    assert sm._ansible_shell_executable == '/bin/sh'

# Generated at 2022-06-13 15:00:37.671749
# Unit test for constructor of class ShellModule
def test_ShellModule():
    powershell = ShellModule(connection=None)
    assert powershell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:42.289935
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # The order of these imports is important.
    # importing the module first causes the import of the plugin class
    # to fail
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.powershell.task_executor import TaskExecutor as PowershellTaskExecutor
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.shell import ShellModule

    # Setup
    connection = connection_loader.get('local', class_only=True)()
    connection.connection._shell = shell = ShellModule(connection)

    # Exercise
    result = shell.join_path('foo', 'bar', 'baz')

    # Assert
    assert result == 'foo\\bar\\baz'

# Generated at 2022-06-13 15:00:52.311935
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    fake_inventory_manager = None
    fake_loader = None
    fake_options = None
    fake_shell_type = ''
    fake_become_method = None
    fake_become_exe = None
    fake_become_user = None
    fake_become_flags = None
    fake_timeout = None
    plugin_options = {}
    shell_obj = ShellModule(fake_inventory_manager, fake_loader, fake_options, fake_shell_type,
                            fake_become_method, fake_become_exe, fake_become_user, fake_become_flags,
                            fake_timeout, plugin_options)
    assert shell_obj.expand_user('~') == 'Write-Output (Get-Location).Path'

# Generated at 2022-06-13 15:01:01.056516
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module.COMPATIBLE_SHELLS == frozenset()
    assert shell_module.SHELL_FAMILY == 'powershell'
    assert shell_module._IS_WINDOWS
    assert shell_module.ENV_PREFIX == ""
    assert shell_module.BINARY_MODULES is None
    assert shell_module.BINARY_MODULE_DATA is None
    assert shell_module.BINARY_MODULE_PATH is None
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_module._SHELL_AND == ';'
    assert shell_module.DEFAULT_EXECUTABLE == "powershell"


# Generated at 2022-06-13 15:01:11.863153
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()

    # TODO: Add test cases for correct output of
    # chmod, chown, set_user_facl, remove, mkdtemp, expand_user,
    # exists, checksum, build_module_command, wrap_for_exec, _unquote and _escape
    # shell.chmod
    # shell.chown
    # shell.set_user_facl
    # shell.remove
    # shell.mkdtemp
    # shell.expand_user
    # shell.exists
    # shell.checksum
    # shell.build_module_command
    # shell.wrap_for_exec
    # shell._unquote
    # shell._escape

    print("Success")
    return 0

# If this script is run as a stand-alone program, call the test_ShellModule
#

# Generated at 2022-06-13 15:01:35.764752
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.COMPATIBLE_SHELLS == frozenset(), 'COMPATIBLE_SHELLS must be empty'
    assert shell.SHELL_FAMILY == 'powershell', 'SHELL_FAMILY must be powershell'
    assert shell._IS_WINDOWS, '_IS_WINDOWS must be True'


# Generated at 2022-06-13 15:01:36.480088
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# Generated at 2022-06-13 15:01:39.233668
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule(connection=None)
    assert mod.SHELL_FAMILY == "powershell"
    assert mod.COMPATIBLE_SHELLS == ()

# Generated at 2022-06-13 15:01:47.327672
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.powershell import ShellModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()

    context = PlayContext()
    context.become = False
    context.become_user = None
    context.connection = 'local'
    context.network_os = 'default'
    context.remote_addr = '127.0.0.1'
    context.remote_user = 'chris'
    context.shell = '/bin/bash'
    context.executable = None


# Generated at 2022-06-13 15:01:49.426683
# Unit test for constructor of class ShellModule
def test_ShellModule():
    p = ShellModule()
    assert p.get_remote_filename('script.sh') == 'script.ps1'

# Generated at 2022-06-13 15:01:58.739356
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # Creating a mock object for class ShellModule and setting mocked values for __init__
    mock_shell_module = type('ShellModule', (object, ), {'_SHELL_REDIRECT_ALLNULL':'> $null', '_SHELL_AND':';', '_IS_WINDOWS':True})
    # set the values of the stubs
    mock_shell_module.__init__ = lambda self, conn: None
    mock_shell_module._unquote = lambda self, val: val
    # creating the object of the ShellModule class
    sh_obj = mock_shell_module('winrm')

    # get the bootstrap_wrapper script
    bootstrap_wrapper = to_text(pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1"))

    # Testing the build_module_command method with

# Generated at 2022-06-13 15:02:07.045997
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    sm = ShellModule()
    # Test Expand user for current user
    assert sm.expand_user('~') == """Write-Output (Get-Location).Path;"""
    # Test Expand user for current user
    assert sm.expand_user('~/test') == """Write-Output ((Get-Location).Path + '''test');"""
    # Test Expand user for current user
    assert sm.expand_user('~\\test') == """Write-Output ((Get-Location).Path + 'test');"""
    # Test Expand user for another user
    assert sm.expand_user('~test', username='test') == """Write-Output '''~test';"""



# Generated at 2022-06-13 15:02:17.764588
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    m = ShellModule()
    assert m.build_module_command("", "", "", "") == u'& %s; exit $LASTEXITCODE' % m._encode_script('')


# Generated at 2022-06-13 15:02:19.022453
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_mod = ShellModule(None, '/tmp')
    assert shell_mod

# Generated at 2022-06-13 15:02:22.536428
# Unit test for constructor of class ShellModule
def test_ShellModule():

    shell_module = ShellModule()
    assert shell_module is not None
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_module._SHELL_AND == ';'
    assert shell_module._IS_WINDOWS



# Generated at 2022-06-13 15:02:50.276636
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import tempfile

    # Instantiate the ShellModule class
    shell_module = ShellModule()

    # Create a temporary directory for the module test
    temp_dir = tempfile.TemporaryDirectory()

    # Create the argument text file that will be passed to the module
    arg_path = os.path.join(temp_dir.name, 'arguments')
    with open(arg_path, 'w') as file:
        file.write('some arguments')

    # Create the module file that will be passed to the shell_module.build_module_command method
    module_path = os.path.join(temp_dir.name, 'module')
    with open(module_path, 'w') as file:
        file.write('some module')

    # Construct the command without shebang, expecting a binary module
    cmd = shell_module.build_

# Generated at 2022-06-13 15:02:57.181475
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():

    class FakeModule(object):
        def __init__(self, shebang, args):
            self.shebang = shebang
            self.args = args

    fake_module = FakeModule('#!python', 'arg_path')
    shell = ShellModule(connection=None)
    cmd = shell.build_module_command('', fake_module.shebang, fake_module.args, arg_path='arg_path')

    assert cmd
    assert '-EncodedCommand' in cmd
    assert 'Write-Output "arg_path"' in cmd



# Generated at 2022-06-13 15:02:57.849095
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# Generated at 2022-06-13 15:02:58.986965
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell

# Generated at 2022-06-13 15:03:04.503500
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shellmodule = ShellModule()
    assert shellmodule.SHELL_FAMILY == 'powershell'
    assert shellmodule.COMPATIBLE_SHELLS == frozenset()
    assert shellmodule._IS_WINDOWS is True
    assert 'chmod' not in dir(shellmodule)
    assert 'chown' not in dir(shellmodule)
    assert 'remove' in dir(shellmodule)
    assert 'mkdtemp' in dir(shellmodule)

# Generated at 2022-06-13 15:03:15.879891
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import json
    import unittest

    import ansible.executor.powershell
    import ansible.plugins.connection.winrm

    class TestConnection():

        class TestWinRM():

            class TestTransport():

                def __init__(self):
                    pass

                def get_remote_host(self):
                    return 'localhost'

                def get_remote_port(self):
                    return 5985

                def get_remote_url(self, *args, **kwargs):
                    return 'http://localhost:5985/wsman'

            def __init__(self):
                self.shell_id = '1234'
                self.transport = self.TestTransport()
                self.protocol = 'https'
                self.endpoint = 'https://localhost:5985/wsman'
                self.server_cert_

# Generated at 2022-06-13 15:03:21.985022
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    module = ShellModule()
    res = module.build_module_command("", shebang='', cmd='echo "hello world"', arg_path='')
    assert res == '& ' + module._encode_script("echo \"hello world\"", strict_mode=False, preserve_rc=False) + '; exit $LASTEXITCODE'
    res = module.build_module_command("", shebang='#!powershell', cmd='echo "hello world"', arg_path='')
    assert res == "& " + module._encode_script("echo \"hello world\"", strict_mode=False, preserve_rc=False) + '; exit $LASTEXITCODE'

# Generated at 2022-06-13 15:03:23.432487
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(command_name='powershell')
    assert shell

# Generated at 2022-06-13 15:03:27.001003
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.module_utils import windows

    obj = windows.ShellModule()
    assert obj.SHELL_FAMILY == 'powershell'
    assert obj._IS_WINDOWS


# Generated at 2022-06-13 15:03:29.406515
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    pathname = "test.txt"
    remote_filename = sm.get_remote_filename(pathname)
    assert remote_filename == "test.ps1"

# Generated at 2022-06-13 15:03:48.755483
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:03:51.404331
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.SHELL_FAMILY == 'powershell', "Expected Shell Family of powershell, got %s" % sm.SHELL_FAMILY

# Generated at 2022-06-13 15:04:00.350253
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    def module_command_assertions(shebang=None, cmd='', arg_path=None):
        """
        The assertions are specific to the module that is passed to the
        build_module_command method.
        """
        cmd_parts = shlex.split(cmd, posix=False)
        cmd_parts = list(map(to_text, cmd_parts))
        if shebang and shebang.lower() == '#!powershell':
            if not cmd_parts[0].lower().endswith('.ps1'):
                # we're running a module via the bootstrap wrapper
                cmd_parts[0] = '"%s.ps1"' % cmd_parts[0]
        elif shebang and shebang.startswith('#!'):
            cmd_parts.insert(0, shebang[2:])
       

# Generated at 2022-06-13 15:04:03.576612
# Unit test for constructor of class ShellModule
def test_ShellModule():
    loader = None
    ba = ShellModule(loader=loader)
    assert isinstance(ba, ShellModule)
    assert ba.connection._shell._connection_info.become_method == 'runas'
    assert ba.SHELL_FAMILY == 'powershell'
    assert ba.COMPATIBLE_SHELLS == 'powershell'
    ba._encode_script('Test')
    ba._escape('')
    ba._unquote('')

# Generated at 2022-06-13 15:04:05.127513
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Instantiate a ShellModule object
    obj = ShellModule()
    assert isinstance(obj, ShellModule)


# Generated at 2022-06-13 15:04:06.814271
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_ = ShellModule()
    cmd = shell_.join_path("a", "b")
    assert cmd == "a\\b"

# Unit tests for operations of class WinShell

# Generated at 2022-06-13 15:04:07.795905
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule('winrm', '#!')

# Generated at 2022-06-13 15:04:13.847286
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    wrapped_command = module.wrap_for_exec('ls')
    assert wrapped_command == "& ls; exit $LASTEXITCODE",\
        "ShellModule: When wrapping ls command in wrap_for_exec() function, " \
        "the expected result is & ls; exit $LASTEXITCODE, but the actual result is %s" % wrapped_command

    wrapped_command = module.wrap_for_exec('ls -l')
    assert wrapped_command == "& ls -l; exit $LASTEXITCODE",\
        "ShellModule: When wrapping ls -l command in wrap_for_exec() function, " \
        "the expected result is & ls -l; exit $LASTEXITCODE, but the actual result is %s" % wrapped_command

    wrapped_command = module

# Generated at 2022-06-13 15:04:15.081150
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm is not None

# Generated at 2022-06-13 15:04:20.023968
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''Unit test for constructor of class ShellModule'''
    module = 'win_command'
    cmdargs = ['-NoLogo', '-NoExit', '-ExecutionPolicy', 'Bypass', '-Command', '-']
    new_instance = ShellModule(None)
    assert new_instance.SHELL_FAMILY == 'powershell'
    assert new_instance.COMPATIBLE_SHELLS == frozenset()
    assert new_instance._IS_WINDOWS == True
    assert new_instance.SHELL_NAME == 'powershell'
    assert new_instance._SHELL_AND == ';'
    assert new_instance._SHELL_REDIRECT_ALLNULL == '> $null'
    assert new_instance.env_prefix() == ''

# Generated at 2022-06-13 15:04:57.340118
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Create an instance of ShellModule and verify the instance
    """
    module = ShellModule()

    assert module is not None

# Generated at 2022-06-13 15:05:00.582185
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule('ansible.executor.powershell', 'winrm', 'localhost', 'foo')
    assert shell._shell_name == 'powershell'
    assert shell._SHELL_NAME == 'powershell'
    assert shell._IS_BINARY == False
    assert shell._IS_POWERSHELL == True


# Generated at 2022-06-13 15:05:02.940301
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module._SHELL_AND == ';'
    assert module._IS_WINDOWS == True

# Generated at 2022-06-13 15:05:05.576833
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    # Test with no parameters passed in
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS is True
    assert isinstance(shell.COMPATIBLE_SHELLS, frozenset)
    assert not shell.COMPATIBLE_SHELLS

# Generated at 2022-06-13 15:05:10.760427
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.constants as C
    import ansible.plugins.shell.powershell as shell
    p = shell.ShellModule(connection=None, no_log=True, shell_type="powershell", **{"remote_user": C.DEFAULT_REMOTE_USER, "sudo_user": C.DEFAULT_REMOTE_USER})
    assert p.remote_user == C.DEFAULT_REMOTE_USER
    assert p.sudo_user == C.DEFAULT_REMOTE_USER
    assert p.sudo_pass == "NOT_LOGGING_PARAMETER"
    assert p.no_log is True
    assert p.remote_tmp == "~/.ansible/tmp"
    assert p.connection is None
    assert p.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:05:12.097842
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell != None

# Generated at 2022-06-13 15:05:15.575166
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # test required variables from superclass
    shell_obj = ShellModule()
    assert shell_obj == ShellModule()
    assert shell_obj.SHELL_FAMILY == 'powershell'
    assert shell_obj._SHELL_REDIRECT_ALLNULL == '> $null'

# Generated at 2022-06-13 15:05:26.499403
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import os
    import tempfile

    module_path = os.path.join(tempfile.gettempdir(), '__ansible_test_module__')
    with open(module_path, 'w') as f:
        f.write('#!python\nprint 42')
    os.chmod(module_path, 0o700)

    class FakeCommand():
        def __init__(self, cmd, **kw):
            self.cmd = cmd
            self.kw = kw

    env_string = '$env:ANSIBLE_MODULE_ARGS = ConvertTo-Json @{ANSIBLE_MODULE_ARGS=@{}}\n'
    shebang = '#!python'

    module_command = FakeCommand(module_path)
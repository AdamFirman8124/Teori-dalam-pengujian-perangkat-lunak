

# Generated at 2022-06-13 14:55:34.498649
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    print(shell)

# Generated at 2022-06-13 14:55:43.669686
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Attributes of ShellModule class
    common_path = '/usr/bin'
    stdout = '/dev/null'
    stderr = '/dev/null'
    user = 'ansadm'
    shell = 'powershell'
    executable = '/usr/bin/ansible_powershell_shell.exe'
    args = ''

    shell_module = ShellModule(common_path, stdout, stderr, user, shell, executable, args)
    assert common_path is shell_module.common_path
    assert stdout is shell_module.stdout
    assert stderr is shell_module.stderr
    assert user is shell_module.user
    assert shell is shell_module.shell
    assert executable is shell_module.executable
    assert args is shell_module.args


# Generated at 2022-06-13 14:55:54.542044
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import shlex

    def _escape(value):
        '''Return value escaped for use in PowerShell single quotes.'''
        # There are 5 chars that need to be escaped in a single quote.
        # https://github.com/PowerShell/PowerShell/blob/b7cb335f03fe2992d0cbd61699de9d9aafa1d7c1/src/System.Management.Automation/engine/parser/CharTraits.cs#L265-L272
        return re.compile(u"(['\u2018\u2019\u201a\u201b])").sub(u'\\1\\1', value)


# Generated at 2022-06-13 14:55:56.045914
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    obj = ShellModule(connection=None)
    assert obj.mkdtemp()


# Generated at 2022-06-13 14:55:56.634062
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule()

# Generated at 2022-06-13 14:55:58.181848
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module is not None


# Generated at 2022-06-13 14:56:07.318599
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    # Testing user_home_path = "~"
    shell = ShellModule()
    assert shell.expand_user('~') == "#!powershell\r\nWrite-Output (Get-Location).Path"

    # Testing user_home_path = "~\\"
    assert shell.expand_user('~\\') == "#!powershell\r\nWrite-Output (Get-Location).Path"

    # Testing user_home_path = "~\\Ansible"
    assert shell.expand_user('~\\Ansible') == "#!powershell\r\nWrite-Output (Get-Location).Path + '\\\\Ansible'"

    # Testing user_home_path = "~\\Ansible_1"

# Generated at 2022-06-13 14:56:08.613570
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()
    assert(isinstance(s, ShellModule))

# Generated at 2022-06-13 14:56:09.308714
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()


# Generated at 2022-06-13 14:56:15.824812
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    import textwrap
    from .test_shell_common import TestShellCommon
    test_shell_case = TestShellCommon(ShellModule)

    # Arrange
    test_cases = []

    # This is a series of tests that were previously collected
    # in test_shell_windows.py.  The unit tests are just importing
    # this module instead of importing the ShellPlugin directly so
    # a mock object can be swapped in to test the salt module
    # independent of the actual salt plugin.

# Generated at 2022-06-13 14:56:31.016141
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    '''
    Unit test for method build_module_command of class ShellModule

    This test case make sure module command is built correctly.
    '''
    import os

    import ansible.executor.powershell
    import ansible.executor.powershell.module_utils.common

    test_file = os.path.join(os.path.dirname(__file__), 'test_file.ps1')
    with open(test_file, 'w') as test_file_fp:
        test_file_fp.write('$test = "test"')

    with open(test_file, 'rb') as test_file_fp:
        test_script = test_file_fp.read()

# Generated at 2022-06-13 14:56:40.413800
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    fake_shebang = '#!/usr/bin/env myshell'
    fake_env_string = '$env:ANSIBLE_MODULE_ARGS=\'{"myarg1":"myarg1","myarg2":"myarg2"}\''
    fake_args = 'myarg1=myarg1 myarg2=myarg2'
    fake_cmd = 'mycmd'
    fake_module_name = 'mycmd'
    class TestShellModule(ShellModule):
        pass
    test_shell_module = TestShellModule(None, playbook_path=None)
    # Test without shebang and args
    expected_command = "%s %s" % (test_shell_module.wrap_for_exec(test_shell_module.build_module_command(fake_env_string, '', fake_cmd)), fake_env_string)

# Generated at 2022-06-13 14:56:42.787566
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection=None)

    assert module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module._SHELL_AND == ';'



# Generated at 2022-06-13 14:56:51.501079
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.executor.powershell import ShellModule
    from ansible.utils.display import Display
    import os

    display = Display()
    shebang = '#!/usr/bin/python'
    module_path = os.path.join('test', 'module.py')
    cmd_parts = [module_path, 'arg1', 'arg2']
    module_name = 'ansible_test_module'
    # Power module
    display.display('Testing Power module %s build' % module_name)
    cmd = ' '.join(cmd_parts)
    sm = ShellModule('')
    cmd = sm.build_module_command('', shebang, cmd, module_path)
    assert cmd.startswith('type \"%s\" | ' % os.path.join(os.getcwd(), module_path))

# Generated at 2022-06-13 14:56:54.629017
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()

    assert s.COMPATIBLE_SHELLS == frozenset()
    assert s.SHELL_FAMILY == 'powershell'



# Generated at 2022-06-13 14:56:56.438242
# Unit test for constructor of class ShellModule
def test_ShellModule():
    myshell = ShellModule()
    myshell.path_has_trailing_slash("C:\\tmp\\")

# Generated at 2022-06-13 14:56:59.893054
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shellmod = ShellModule()
    shellscript = shellmod._encode_script('''
        if ($true -eq $true)
        {
            Write-Output 'True is true'
        }
        else
        {
            Write-Output 'True is not true'
        }
        ''')
    assert shellscript == 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand AgABAA=='

# Generated at 2022-06-13 14:57:02.992248
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module.SHELL_FAMILY == 'powershell'
    assert module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module._SHELL_AND == ';'

# Generated at 2022-06-13 14:57:14.157964
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.executor.powershell.common import _encode_script

    cmd = 'Test-Module.ps1'
    arg_path = '-argument_path'
    shebang = '#!powershell'

    pshell = ShellModule(connection=None)
    pshell.no_log = True

    # Test with shebang == '#!powershell' and cmd ends with .ps1
    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")
    wrapper_cmd = "type " + cmd + " | " + _encode_script(script=bootstrap_wrapper, strict_mode=False, preserve_rc=False)
    assert wrapper_cmd == pshell.build_module_command('env_string', shebang, cmd)

    # Test

# Generated at 2022-06-13 14:57:15.791780
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert 'ansible.executor.powershell.ShellModule' == shell.__module__

# Generated at 2022-06-13 14:57:20.932768
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule(None)
    assert shell_obj is not None

# Generated at 2022-06-13 14:57:23.296058
# Unit test for constructor of class ShellModule
def test_ShellModule():
    current_path = '/Users/chris/.ansible/ansible.cfg'
    sh = ShellModule(current_path)
    assert sh.get_remote_filename(current_path) == 'ansible.cfg'



# Generated at 2022-06-13 14:57:29.528473
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    shell = ShellModule(None)
    assert shell.get_remote_filename('test') == 'test.ps1'
    assert shell.get_remote_filename('test.py') == 'test.py'
    assert shell.get_remote_filename('script.ps1') == 'script.ps1'
    assert shell.get_remote_filename('test.txt') == 'test.txt'

# Generated at 2022-06-13 14:57:33.017994
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    shell_obj = ShellModule()
    assert 'test.ps1' == shell_obj.get_remote_filename('test.sh')
    assert 'test.sh' == shell_obj.get_remote_filename('test.sh')


# Generated at 2022-06-13 14:57:40.659626
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()._SHELL_AND == ';'
    assert ShellModule()._SHELL_REDIRECT_ALLNULL == '> $null'
    assert ShellModule().CHANGED_STRING == '\r\nchanged: [localhost] => {"changed": true, "cmd": "..."}\r\n'
    assert ShellModule().FAILED_STRING == '\r\nfailed: [localhost] (item=...) => {"cmd": "...", "failed": true, "item": "..."}'



# Generated at 2022-06-13 14:57:42.187124
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()


# Generated at 2022-06-13 14:57:43.420058
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm is not None

# Generated at 2022-06-13 14:57:48.176427
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection='winrm')
    print(module.__dict__)
    print(module.__dict__['_shell_type'])
    print(module.__dict__['_shell'])
    #print(module.get_remote_filename('users.py'))

if __name__ == '__main__':
    test_ShellModule()

# Generated at 2022-06-13 14:57:55.656409
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import tempfile
    import os
    import re
    import shutil
    import time
    from ansible.module_utils.powershell import quote, ps_script_args

    basedir = tempfile.mkdtemp()


# Generated at 2022-06-13 14:57:59.073901
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    remote_filename = ShellModule(None).get_remote_filename('/home/test_user/test_dir_1/test_dir_2/test_file_1.sh')
    assert remote_filename == 'test_file_1.ps1'

# Generated at 2022-06-13 14:58:06.926462
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()
    result = b'[System.IO.Directory]::CreateDirectory("C:\\Windows\\Temp\\ansible-tmp-1524547962.24-1255-55794626500072").FullName'
    assert shell.mkdtemp(basefile='ansible-tmp-1524547962.24-1255-55794626500072') == result


# Generated at 2022-06-13 14:58:08.877022
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule(connection=None)
    assert shell_module.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:58:15.447123
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()

    basefile = 'ansible-tmp-PYzQjR'
    expected_result = '''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('C:\\Windows\\Temp')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'ansible-tmp-PYzQjR'
        Write-Output -InputObject $tmp.FullName
        '''

    assert shell.mkdtemp(basefile=basefile).strip() == expected_result.strip(), "result does not match"

# Generated at 2022-06-13 14:58:17.746532
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test for shell module class instantiation with given name
    shell_module = ShellModule()

    assert shell_module

# Generated at 2022-06-13 14:58:19.106577
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell

# Generated at 2022-06-13 14:58:24.358512
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    Check to see if the ShellModule class was properly initialized
    '''
    mod = ShellModule()
    assert mod.COMPATIBLE_SHELLS == frozenset()
    assert mod.SHELL_FAMILY == 'powershell'
    assert mod._IS_WINDOWS == True
    assert mod.shebang == '/usr/bin/env powershell'

# Generated at 2022-06-13 14:58:30.900071
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    module = ShellModule()
    basefile = 'test'
    system = False
    mode = None
    tmpdir = "c:\\TMP"
    cmd = module.mkdtemp(basefile=basefile, system=system,
                         mode=mode, tmpdir=tmpdir)
    cmd = cmd.decode("utf-8")
    assert cmd.find('$tmp = New-Item -Type Directory -Path $tmp_path -Name \'test\'') != -1
    assert cmd.find('Write-Output -InputObject $tmp.FullName') != -1

# Generated at 2022-06-13 14:58:32.832816
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None)
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS is True

# Generated at 2022-06-13 14:58:40.143490
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import tempfile
    from ansible.module_utils.powershell import ShellModule
    module = ShellModule()
    # Test without basefile, system, mode and tmpdir
    mkdtemp_response = module.mkdtemp()
    shell_string = b'powershell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand '

# Generated at 2022-06-13 14:58:42.307423
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import random
    import string

    random_string = ''.join(random.choice(string.hexdigits) for _ in range(0,16))
    shell = ShellModule()

    assert random_string in shell.mkdtemp(random_string)

# Generated at 2022-06-13 14:58:49.390568
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule(connection=None, shell_executable=None, no_log=False, warn_only=False, become=False, become_method=None,
                            become_user=None, become_password=None, become_exe=None, become_flags=None, check=False, executable=None,
                            stdin=None, stdin_add_newline=True, chdir=None, use_persistent_connections=False)
    assert shell_obj.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:58:50.985684
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test empty constructor
    shell = ShellModule()
    assert shell


# Generated at 2022-06-13 14:58:57.635005
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule(connection='winrm', become_method='runas', become_user='Administrator')
    # Check if all functions are implemented.
    # Methods taken from ansible.module_utils.basic.AnsibleModule
    shell_module.fail_json
    shell_module.exit_json
    shell_module.parse_kv
    shell_module.deprecate
    shell_module.get_bin_path
    shell_module.basic
    shell_module.run_command
    shell_module.no_log_values
    shell_module.add_path_info
    shell_module.jsonify
    shell_module.boolean
    shell_module.is_executable
    shell_module.strtobool
    shell_module.is_dangerous_path
    shell_module.get_platform

# Generated at 2022-06-13 14:59:06.053138
# Unit test for constructor of class ShellModule
def test_ShellModule():
    p = ShellModule()
    p._unquote('"abc"')
    p._unquote("'abc'")
    p._unquote("abc")
    p._unquote("'abc")
    p._unquote('"abc')
    p._unquote("'abc\"")
    p._unquote("'abc\''")
    p._unquote("'abc\'")
    p._unquote("\"abc\'")
    p._unquote("\'abc\'")
    p._unquote("\"abc\"")
    p._unquote("a\\'b\\\'c")
    p._escape("abc")
    p._escape("a'b'c")
    p._escape("a'b\"")
    p._encode_script("abc")
    p._encode_script("")

# Generated at 2022-06-13 14:59:07.163076
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection='winrm')

# Generated at 2022-06-13 14:59:09.861463
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module.SHELL_FAMILY == 'powershell'
    assert len(shell_module.COMPATIBLE_SHELLS) == 0

# Generated at 2022-06-13 14:59:13.340218
# Unit test for constructor of class ShellModule
def test_ShellModule():
    data = '#< CLIXML\r\n<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Error">Msg1</S><S S="Error">Msg2</S></Objs>'
    assert _parse_clixml(data) == u'Msg1\r\nMsg2'
    assert _parse_clixml("<CLIXML><Objs></Objs></CLIXML>") == b''



# Generated at 2022-06-13 14:59:16.570816
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule.ANSIBLE_MODULE_ARGS = {}
    shell_module = ShellModule()
    assert isinstance(shell_module, ShellModule)


# Generated at 2022-06-13 14:59:18.073353
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''shell_windows.py:ShellModule()'''


# Generated at 2022-06-13 14:59:20.356213
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule()
    assert plugin

if __name__ == "__main__":
    test_ShellModule()

# Generated at 2022-06-13 14:59:37.603281
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import tempfile

    module_name = 'test_module'
    (fd, fname) = tempfile.mkstemp()
    os.close(fd)
    module_data = "#!/usr/bin/python -tt\nprint 'hello'\n"
    with open(fname, 'wb') as f:
        f.write(module_data)
    module_data_ascii = base64.b64encode(module_data.encode('utf-16-le'))

    # Without striping quotes
    for args in [dict(path=fname), dict(path=fname, strip_quotes=False)]:
        shell = ShellModule(**args)
        assert shell.build_module_command('', '', module_name) == '& %s; exit $LASTEXITCODE' % base

# Generated at 2022-06-13 14:59:43.206975
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule()
    assert obj._SHELL_REDIRECT_ALLNULL == '> $null'
    assert obj._SHELL_AND == ';'

    obj = ShellModule(keep_remote_files=True)
    assert obj._SHELL_REDIRECT_ALLNULL == "> $null"
    assert obj._SHELL_AND == ';'


# Generated at 2022-06-13 14:59:48.181192
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Create a mock of a connection plugin.
    connection_plugin = type('ConnectionPlugin', (object,), {'port': 5986, 'is_psrp': False})
    shell = ShellModule(connection_plugin)
    assert shell.connection._connection.port == 5986
    assert connection_plugin.is_psrp == False

# Generated at 2022-06-13 14:59:54.379241
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.plugins.action.normal import ActionModule
    from ansible.plugins.shell import ShellBase

    module = ActionModule(None, None, None, None, None, None)
    shell = ShellBase(module)
    powershell_shell = ShellModule(module)

    assert shell != powershell_shell
    assert shell.COMPATIBLE_SHELLS == powershell_shell.COMPATIBLE_SHELLS
    assert shell.SHELL_FAMILY == powershell_shell.SHELL_FAMILY



# Generated at 2022-06-13 15:00:00.880658
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None, runner=None, host=None,
                        exec_env='',
                        become_user='', become_pass='',
                        become_exe='', become_flags='',
                        become_method='', become_info={},
                        no_log=False, become_ask_pass=False,
                        verbosity=0,
                        check=False, diff=False, expand_vars=False,
                        **{})

    assert shell is not None

# Generated at 2022-06-13 15:00:04.003616
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection=None)
    assert module is not None
    assert module._IS_WINDOWS is True
    assert module.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:07.075303
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.powershell import ShellModule

    module = ShellModule(None)

    assert module.SHELL_FAMILY == 'powershell'
    assert module._SHELL_REDIRECT_ALLNULL == '> $null'

# Generated at 2022-06-13 15:00:15.660951
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Load powershell module
    module = ShellModule()

    # Test checksum
    checksum_script = module._encode_script("If (Test-Path -PathType Leaf /Users/ansible/test123.txt) { $sp = new-object -TypeName System.Security.Cryptography.SHA1CryptoServiceProvider; $fp = [System.IO.File]::Open('/Users/ansible/test123.txt', [System.IO.Filemode]::Open, [System.IO.FileAccess]::Read); [System.BitConverter]::ToString($sp.ComputeHash($fp)).Replace('-', '').ToLower(); $fp.Dispose(); } ElseIf (Test-Path -PathType Container '/Users/ansible/test123.txt') { Write-Output '3'; } Else { Write-Output '1'; }")

# Generated at 2022-06-13 15:00:17.834719
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.get_option('remote_tmp') == "~/.ansible/tmp"

# Generated at 2022-06-13 15:00:20.877061
# Unit test for constructor of class ShellModule
def test_ShellModule():

    p = ShellModule('/dev/null')
    assert p.SHELL_FAMILY == 'powershell'
    assert p._shell_executable == 'PowerShell'

# Generated at 2022-06-13 15:00:37.459523
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule({})
    assert shell.SHELL_FAMILY == 'powershell'
    assert not shell.COMPATIBLE_SHELLS
    assert shell._IS_WINDOWS
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'


# Generated at 2022-06-13 15:00:40.376860
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell is not None
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'
    assert shell._IS_WINDOWS


# Generated at 2022-06-13 15:00:41.777691
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test for check for file module
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:42.261455
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()

# Generated at 2022-06-13 15:00:45.136055
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    shell._encode_script('#hello')
    shell._encode_script('', as_list=True)
    shell.join_path('c:\\', 'a')
    shell.join_path('c:', 'a')

# Generated at 2022-06-13 15:00:56.618239
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(conn=None)

    assert shell.COMPATIBLE_SHELLS == frozenset(), "The variable should be empty"
    assert shell.SHELL_FAMILY == 'powershell', "The variable should be 'powershell'"
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null', "The variable should be '> $null'"
    assert shell._SHELL_AND == ';', "The variable should be ';'"
    assert shell._IS_WINDOWS == True, "The variable should be True"

    # TODO: test join_path, expand_user, build_module_command, get_remote_filename properly
    assert shell.join_path('/home/test', 'test.txt') == shell.get_remote_filename('test.txt')

# Generated at 2022-06-13 15:01:00.182666
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod.COMPATIBLE_SHELLS == frozenset()
    assert mod.SHELL_FAMILY == 'powershell'
    assert mod._SHELL_REDIRECT_ALLNULL == '> $null'
    assert mod._SHELL_AND == ';'
    assert mod._IS_WINDOWS

# Generated at 2022-06-13 15:01:01.900759
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shellm = ShellModule()
    assert shellm.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:01:04.060283
# Unit test for constructor of class ShellModule
def test_ShellModule():
    r = ShellModule()
    assert r


# Generated at 2022-06-13 15:01:05.038295
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# Generated at 2022-06-13 15:01:44.644008
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule(remote_user=None,
                     host=None,
                     connection=None,
                     become_method=None,
                     become_user=None,
                     check=False,
                     diff=False)

    assert sm.can_set_mode is False
    assert sm.can_set_owner is False
    assert sm.can_set_user_facl is False
    assert sm.can_copy is False
    assert sm.can_duplicate_files is False
    assert sm.can_defer_join is True
    assert sm.can_pipe is True

    assert sm.SHELL_FAMILY == 'powershell'
    assert sm._IS_WINDOWS is True


# Generated at 2022-06-13 15:01:48.604130
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shellmodule = ShellModule()
    assert shellmodule.SHELL_FAMILY == 'powershell'
    assert shellmodule.COMPATIBLE_SHELLS == frozenset()


# Generated at 2022-06-13 15:01:49.288273
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()

# Generated at 2022-06-13 15:01:52.642985
# Unit test for constructor of class ShellModule
def test_ShellModule():
    powershell = ShellModule()
    assert powershell._SHELL_REDIRECT_ALLNULL == "> $null"
    assert powershell._SHELL_AND == ";"
    assert powershell._IS_WINDOWS == True

# Generated at 2022-06-13 15:02:01.270889
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.get_remote_filename('foo') == 'foo'
    assert sm.get_remote_filename('foo.ps1') == 'foo.ps1'
    assert sm.get_remote_filename('foo.exe') == 'foo.exe'
    assert sm.get_remote_filename('foo.sh') == 'foo.ps1'

    assert sm.join_path('foo', 'bar', 'baz') == 'foo\\bar\\baz'
    assert sm.join_path('foo/', '/bar/', 'baz') == 'foo\\bar\\baz'
    assert sm.join_path('foo\\', '\\bar\\', 'baz') == 'foo\\bar\\baz'

# Generated at 2022-06-13 15:02:02.534953
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module is not None

# Generated at 2022-06-13 15:02:03.654314
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()
    assert isinstance(s, ShellModule)


# Generated at 2022-06-13 15:02:10.023989
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None, addl_args=None, runas=None)
    test_shebang = "#!/usr/bin/python"
    command = "/usr/bin/python"
    test_args = 'PYTHONPATH="/opt/foo/lib" python -m foo.bar'
    test_cmd = shell.build_module_command(env_string='', shebang=test_shebang, cmd=test_args, arg_path=None)
    assert command in test_cmd
    assert '/opt/foo/lib"' in test_cmd
    assert 'foo.bar' in test_cmd



# Generated at 2022-06-13 15:02:13.778882
# Unit test for constructor of class ShellModule
def test_ShellModule():
    powershell = ShellModule()
    assert powershell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:02:14.861368
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Test Constructor"""

    ShellModule()

# Generated at 2022-06-13 15:03:22.828858
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_mod = ShellModule(connection=None, AddArgs={"passwd": "passwd"})
    assert shell_mod.AddArgs["passwd"] == "passwd"

# Generated at 2022-06-13 15:03:23.822947
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert ShellModule is not None

# Generated at 2022-06-13 15:03:28.899030
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Create a MockClass object
    shell = ShellModule()
    # Assert that the instance of the MockClass has been created
    assert shell is not None
    # Assert that the common_args has been assigned
    assert shell._common_args == 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted'


# Generated at 2022-06-13 15:03:30.920712
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shellm = ShellModule()
    assert shellm.SHELL_FAMILY == 'powershell'
    assert shellm._IS_WINDOWS



# Generated at 2022-06-13 15:03:34.802612
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    Instantiate a ShellModule object and verify that the class attribute
    COMPATIBLE_SHELLS is an empty set.
    '''

    shell = ShellModule()

    assert ShellModule.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:03:42.765892
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    print(module.env_prefix(**{}))
    print(module.join_path('a', 'b', 'c', 'd'))
    print(module.get_remote_filename('a/b/c/d'))
    print(module.path_has_trailing_slash('a/b/c/d'))
    print(module.expand_user('~/test'))
    print(module.remove('a/b/c/d', True))
    print(module._unquote("'hello'"))
    print(module._escape("'hello'"))
    print("")


if __name__ == '__main__':
    test_ShellModule()

# Generated at 2022-06-13 15:03:50.818322
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import json

    # basic test
    powershell = ShellModule('ansible')
    cmd = powershell.join_path('/tmp', 'foo', 'bar')
    assert cmd == '/tmp\\foo\\bar'

    # test quote handling
    cmd = powershell.join_path('"/tmp"', '\\foo', '\\"bar"')
    assert cmd == '/tmp\\foo\\"bar"'

    # test quote handling of escaped quotes
    cmd = powershell.join_path('"\\"/tmp\\""', '\\foo', '\\"bar"')
    assert cmd == '\\"/tmp\\"\\foo\\"bar"'

    # test for trailing slashes
    cmd = powershell.path_has_trailing_slash('"/tmp\\"')
    assert cmd is True
    cmd = powershell.path_has

# Generated at 2022-06-13 15:03:52.575885
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:04:01.152375
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import sys
    import os
    import sys
    import os
    import pytest
    from ansible.errors import AnsibleError

    sys.path.append('../connection/')

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    from ansible.plugins.shell import ShellModule

    def _exec(cmd, stdin=None, in_data=None, sudoable=False, shell="/bin/sh"):
        return cmd, stdin, in_data, sudoable, shell

    def _exec_command(self, cmd, in_data=None, sudoable=False):
        cmd = cmd.strip()
        if in_data:
            stdin = subprocess.PIPE
        else:
            stdin = None
        p

# Generated at 2022-06-13 15:04:08.391503
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Create a task queue manager
    tqm = TaskQueueManager(
        connection_type='smart',
        passwords={},
        stdout_callback='default'
    )

    # Create a connection plugin that uses winrm to communicate with the target
    con_plugin = tqm.get_plugin_loader().get('winrm', tqm.get_inventory(), 'test_host')

    # Create a shell module instance that executes commands via winrm
    shell_module = ShellModule(con_plugin)

    # Set a few options
    shell_module.set_option('remote_tmp', '~/.ansible/tmp')
    shell_module.set_option('remote_user', 'TEST_USER')

# Generated at 2022-06-13 15:05:22.107807
# Unit test for constructor of class ShellModule
def test_ShellModule():  # noqa: N802
    shell_module = ShellModule(connection=None, shell_executable='powershell.exe', no_log=None, keep_remote_files=False)
    assert shell_module.connection is None
    assert shell_module.no_log is None
    assert shell_module.keep_remote_files is False
    assert shell_module.DEFAULT_EXECUTABLE == 'powershell.exe'

# Generated at 2022-06-13 15:05:27.639339
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Check ShellModule class.
    shell = ShellModule(conn=None, *_common_args)
    assert shell is not None
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'
    assert shell._IS_WINDOWS is True
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'

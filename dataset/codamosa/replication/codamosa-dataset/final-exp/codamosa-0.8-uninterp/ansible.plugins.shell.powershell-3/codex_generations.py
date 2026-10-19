

# Generated at 2022-06-13 14:55:43.695781
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import datetime
    shm = ShellModule()

    assert(shm.build_module_command(env_string='', shebang='', cmd='', arg_path='') == 'powershell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -File ')
    assert(shm.build_module_command(env_string='', shebang='#!powershell', cmd='', arg_path='') == 'powershell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -Command . .\\bootstrap_wrapper.ps1; ')

    assert(shm.build_module_command(env_string='', shebang='', cmd='test.exe arg1 arg2', arg_path='/tmp') == 'powershell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -File test.exe arg1 arg2 /tmp')

# Generated at 2022-06-13 14:55:49.982175
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    # Create an power shell shell plugin
    shell_module = ShellModule()

    # Check if the home directory is expanded from a user home path starting with ~
    assert shell_module.expand_user('~/test') == shell_module._encode_script('Write-Output (Get-Location).Path + \'/test\'')

    # Check if the home directory is expanded from a user home path starting with ~\
    assert shell_module.expand_user('~\\test') == shell_module._encode_script('Write-Output ((Get-Location).Path + \'/test\')')

    # Check if the home directory is expanded from a user home path starting with ~
    assert shell_module.expand_user('~') == shell_module._encode_script('Write-Output (Get-Location).Path')

    # Check if the home directory is

# Generated at 2022-06-13 14:56:00.133629
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()
    name, options = s.get_option_info()
    assert name == 'powershell'
    assert options['executable']['default'] == 'powershell'
    assert options['executable']['env_fallback'] == ['ANSIBLE_POWERSHELL_SHEBANG', 'PS_SHEBANG', 'PS_DEFAULT_VERSION']
    assert options['executable']['required'] is True
    assert options['executable']['aliases'] == ['shell']
    assert options['executable']['choices'] == ['4', '5', '6', '2', '3', 'powershell', 'pwsh', 'pwsh3', 'pwsh4', 'pwsh5', 'pwsh6']

# Generated at 2022-06-13 14:56:08.370591
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.plugins.shell import ShellBase

    ssh = ShellBase()
    # get_remote_filename must return a string
    assert isinstance(ssh.get_remote_filename('/home/foobar/sample.txt'), str)
    # get_remote_filename must return a file name without path
    assert ssh.get_remote_filename('/home/foobar/sample.txt') == 'sample.txt'
    assert ssh.get_remote_filename('/home/foobar/sample.py') == 'sample.py'
    assert ssh.get_remote_filename('/home/foobar/sample.sh') == 'sample.sh'
    assert ssh.get_remote_filename('/home/foobar/sample') == 'sample'
    #

# Generated at 2022-06-13 14:56:11.252705
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    from ansible.plugins.shell.powershell import ShellModule

    shell = ShellModule()

    assert shell.get_remote_filename('my_script.ps1') == 'my_script.ps1'
    assert shell.get_remote_filename('my_script') == 'my_script.ps1'



# Generated at 2022-06-13 14:56:20.175208
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    module_obj = ShellModule()
    assert module_obj.expand_user('~') == module_obj._encode_script('Write-Output (Get-Location).Path')
    assert module_obj.expand_user('~\\~') == module_obj._encode_script('Write-Output ((Get-Location).Path + "~")')
    assert module_obj.expand_user('c:\\') == module_obj._encode_script('Write-Output "c:\\"')
    assert module_obj.expand_user('~\\~', 'some_user') == module_obj._encode_script('Write-Output ((Get-Location).Path + "~")')
    assert module_obj.expand_user('~') == module_obj._encode_script('Write-Output (Get-Location).Path')

# Generated at 2022-06-13 14:56:30.965294
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    shell_plugin = ShellModule()
    assert shell_plugin.get_remote_filename('test.ps1') == 'test.ps1'
    assert shell_plugin.get_remote_filename('test.py') == 'test.ps1'
    assert shell_plugin.get_remote_filename('test') == 'test.ps1'
    assert shell_plugin.get_remote_filename('test.exe') == 'test.exe'
    assert shell_plugin.get_remote_filename('test.bat') == 'test.ps1'
    assert shell_plugin.get_remote_filename('test.cmd') == 'test.ps1'
    assert shell_plugin.get_remote_filename('') == '_.ps1'

# Generated at 2022-06-13 14:56:34.959315
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Verify attributes of class ShellModule using provided __doc__
    s = ShellModule(connection=None)
    assert s.COMPATIBLE_SHELLS == frozenset()
    assert s.SHELL_FAMILY == 'powershell'
    assert s._IS_WINDOWS == True

# Generated at 2022-06-13 14:56:43.122230
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    module_name = 'ansible_test_module'
    shebang = '#!python'
    remote_module_path = '%USERPROFILE%\\Documents\\WindowsPowerShell\\Modules\\'
    environment = '$ENV:ANSIBLE_TEST_ENV = "Ansible User Environment Variable"'

# Generated at 2022-06-13 14:56:48.461722
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import tempfile

    sh = ShellModule(None)
    tf = tempfile.NamedTemporaryFile(delete=False)
    tf.write(b"#!python\nprint 'test'\n")
    tf.close()
    try:
        shebang = "#!python"
        cmd = '%s %s' % (tf.name, 'arg1')
        result = sh.build_module_command('', shebang, cmd)
        assert result == u"& python.exe -u \"" + tf.name + u".ps1\" " + "arg1"
    finally:
        os.unlink(tf.name)


# Generated at 2022-06-13 14:56:55.308949
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module.SHELL_FAMILY == 'powershell'

    # TODO: add unit test of _parse_clixml()

# Unit test of _escape()

# Generated at 2022-06-13 14:56:57.103438
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None)
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:56:57.763932
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 14:57:04.813297
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule(connection='winrm')
    # get_option is mocked to return a test string as the value of remote_tmp
    shell.get_option = lambda x: x == 'remote_tmp' and 'test_remote_tmp' or ''
    script = shell.mkdtemp('test_temporary_dir', tmpdir="test_remote_tmp")
    assert(script == '''$tmp_path = [System.Environment]::ExpandEnvironmentVariables('test_remote_tmp')
    $tmp = New-Item -Type Directory -Path $tmp_path -Name 'test_temporary_dir'
    Write-Output -InputObject $tmp.FullName
    ''')

# Generated at 2022-06-13 14:57:09.203843
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module.SHELL_FAMILY == 'powershell'
    assert module._IS_WINDOWS
    assert module.is_windows
    assert module.SHELL_FAMILY == 'powershell'
    assert module.SHELL_NAME == 'powershell'
    assert not module.SHELL_INHERIT
    assert module.COMPATIBLE_INTERPRETER_FAMILIES == frozenset()
    assert isinstance(module, ShellBase)

# Generated at 2022-06-13 14:57:19.227473
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test example from class docstring
    assert ShellModule().env_prefix(FOO='bar') == ''
    c = ShellModule(connection='trivial', become='root')
    # Test as_command

# Generated at 2022-06-13 14:57:28.420045
# Unit test for constructor of class ShellModule
def test_ShellModule():
    script = b'''\
$ANSIBLE_VERSION=@()
$ANSIBLE_VERSION+=@($PSVersionTable.PSVersion.Major,".",$PSVersionTable.PSVersion.Minor)
$ANSIBLE_VERSION+=@(" ",$PSVersionTable.PSVersion.Build," ",$PSVersionTable.PSVersion.PSCompatibleVersions)
$ANSIBLE_VERSION+=@(" ",$PSVersionTable.CLRVersion)
$ANSIBLE_VERSION+=@(" ",($PSVersionTable.GITCommitId -join ""))
$ANSIBLE_VERSION+=@(" ",$PSVersionTable.PSRemotingProtocolVersion)
$ANSIBLE_VERSION+=@(" ",$PSVersionTable.SerializationVersion)
$ANSIBLE_VERSION+=@(" ",$PSVersionTable.WSManStackVersion)
Write-Output ($ANSIBLE_VERSION -join "")
'''

# Generated at 2022-06-13 14:57:33.914614
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()

    # constructor should set these fields
    assert sm._IS_WINDOWS == True
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm.SHELL_FAMILY == 'powershell'

    # constructor should call these functions
    assert hasattr(sm, 'env_prefix')
    assert hasattr(sm, 'join_path')
    assert hasattr(sm, 'get_remote_filename')
    assert hasattr(sm, 'path_has_trailing_slash')
    assert hasattr(sm, 'chmod')
    assert hasattr(sm, 'chown')
    assert hasattr(sm, 'set_user_facl')
    assert hasattr(sm, 'remove')
    assert hasattr(sm, 'mkdtemp')

# Generated at 2022-06-13 14:57:38.217881
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule(connection='local', tmpdir='/tmp')
    assert sm.connection == 'local'
    assert sm.tmpdir == '/tmp'

    sm = ShellModule(connection='local')
    assert sm.connection == 'local'

# Generated at 2022-06-13 14:57:48.518968
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():

    def run_test(instance, basefile, system, mode, tmpdir, module_defaults):
        return instance.mkdtemp(basefile, system, mode, tmpdir)
    instance = ShellModule()
    # Create basefile with current time
    import time
    basefile = time.strftime('%Y-%m-%d-%H-%M-%S')
    tmpdir = 'C:\\temp\\'
    # Execute the test
    mkdtemp = run_test(instance, basefile, system, mode, tmpdir, module_defaults)
    # Make sure the returned string is a path
    import os
    assert os.path.isdir(mkdtemp)
    # Remove the test directory
    import shutil
    shutil.rmtree(mkdtemp)

# Generated at 2022-06-13 14:58:02.300829
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell_object = ShellModule()
    # test case with basefile and tmpdir
    test_basefile = 'test_basefile_test'
    test_tmpdir = 'test_tmpdir_test'
    result = shell_object.mkdtemp(basefile=test_basefile, tmpdir=test_tmpdir)
    assert result.startswith('$tmp_path = [System.Environment]::ExpandEnvironmentVariables(\'test_tmpdir_test\')')
    assert result.endswith('$tmp = New-Item -Type Directory -Path $tmp_path -Name \'test_basefile_test\'\r\nWrite-Output -InputObject $tmp.FullName')

    # test case with basefile only
    result = shell_object.mkdtemp(basefile=test_basefile)
    assert result.startsw

# Generated at 2022-06-13 14:58:05.275744
# Unit test for constructor of class ShellModule
def test_ShellModule():
    cm = ShellModule()
    assert cm.SHELL_FAMILY == 'powershell'
    assert 'powershell' in cm.COMPATIBLE_SHELLS
    assert 'powershell.exe' in cm.COMPATIBLE_SHELLS

# Generated at 2022-06-13 14:58:05.996394
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 14:58:10.387361
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'

# Generated at 2022-06-13 14:58:11.429107
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection='local')

# Generated at 2022-06-13 14:58:12.461920
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell is not None

# Generated at 2022-06-13 14:58:17.292807
# Unit test for constructor of class ShellModule
def test_ShellModule():
    cm = ShellModule()
    # Test defaults
    assert cm.shell_type == 'powershell'
    assert cm.SHELL_FAMILY == 'powershell'
    assert cm.COMPATIBLE_SHELLS == frozenset()
    assert cm._IS_WINDOWS is True



# Generated at 2022-06-13 14:58:22.681618
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    sm = ShellModule()

    # Test with no value specified.
    result = sm.mkdtemp()
    assert result == '''$tmp_path = [System.Environment]::ExpandEnvironmentVariables('$env:TEMP')
$tmp = New-Item -Type Directory -Path $tmp_path -Name 'tmpCY0D3O.tmp'
Write-Output -InputObject $tmp.FullName
'''
    # Test with value specified.
    result = sm.mkdtemp(basefile="ansibletmp")
    assert result == '''$tmp_path = [System.Environment]::ExpandEnvironmentVariables('$env:TEMP')
$tmp = New-Item -Type Directory -Path $tmp_path -Name 'ansibletmp'
Write-Output -InputObject $tmp.FullName
'''

# Generated at 2022-06-13 14:58:32.077547
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    # WinRM does not support ControlPersist by default
    kwargs = dict(control_persist_timeout=0)
    shell = ShellModule(connection=None, **kwargs)
    basefile = 'ansible-tmp-2401551357.85-222729078494040'
    result = shell.mkdtemp(basefile=basefile)
    cmd_parts = shlex.split(result)
    # Since PowerShell is not our default shell, we need to use the "powershell -Command"
    # invocation and then pass back the encoded script
    result_cmd = cmd_parts[0]
    assert result_cmd == 'powershell', "cmd_parts = %s" % cmd_parts
    # PowerShell requires that we pass the -EncodedCommand parameter
    result_param = cmd_parts[-2]

# Generated at 2022-06-13 14:58:36.953476
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule()
    assert(obj.SHELL_FAMILY == 'powershell')
    assert(obj.COMPATIBLE_SHELLS == frozenset())
    assert(obj._SHELL_REDIRECT_ALLNULL == '> $null')
    assert(obj._SHELL_AND == ';')
    assert(obj._IS_WINDOWS == True)



# Generated at 2022-06-13 14:58:46.539082
# Unit test for constructor of class ShellModule
def test_ShellModule():
    try:
        ShellModule(connection='winrm')
        ShellModule(connection='psrp')
    except Exception as e:
        print('An exception was raised when testing constructor of'
              ' class ShellModule: %s' % str(e))


# Generated at 2022-06-13 14:58:56.912412
# Unit test for constructor of class ShellModule
def test_ShellModule():
  shell = ShellModule()
  shell.noop_on_check(True)
  shell = ShellModule()
  shell.noop_on_check(False)

# Generated at 2022-06-13 14:58:57.896407
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()



# Generated at 2022-06-13 14:59:03.584733
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test arguments to PS module
    mod_args = dict(
        argument_spec=dict(
            foo=dict(default='bar', type='str'),
            bam=dict(default='boo', type='str'),
        ),
        supports_check_mode=False,
    )

    # initialize module, set foo='bar', bam='boo'
    mod = ShellModule(**mod_args)

    # there's no good way to test this before ModuleBase, etc.
    return True

# Generated at 2022-06-13 14:59:05.975239
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    This is how you might test the constructor of a class.
    >>> x = ShellModule()
    '''
    pass

# Generated at 2022-06-13 14:59:12.168473
# Unit test for constructor of class ShellModule
def test_ShellModule():

    shellobj = ShellModule()
    assert shellobj is not None
    print(repr(shellobj))

    assert len(shellobj.COMPATIBLE_SHELLS) == 0
    assert shellobj.SHELL_FAMILY == 'powershell'
    assert shellobj._IS_WINDOWS is True
    assert shellobj._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shellobj._SHELL_AND == ';'

# Generated at 2022-06-13 14:59:16.387587
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Create an empty class
    shell_module = ShellModule()
    # Create an instance of the ShellModule class
    shell_module = ShellModule()
    # Create an instance of the subclass ShellModule of the class ShellBase
    shell_module = ShellModule()


# Generated at 2022-06-13 14:59:18.328577
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Sanity check to make sure the constructor of the class works
    """
    sm = ShellModule()



# Generated at 2022-06-13 14:59:27.225500
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test constructor with default options
    module = ShellModule()
    assert module.get_option('become_method') == 'runas'

    # Test constructor with custom options
    module = ShellModule(
        become_method='runas',
        become_user='jerry',
        become_exe='',
        become_flags='',
        become_pass='',
    )
    assert module.get_option('become_method') == 'runas'
    assert module.get_option('become_user') == 'jerry'
    assert module.get_option('become_flags') == ''
    assert module.get_option('become_exe') == ''

# Generated at 2022-06-13 14:59:37.045648
# Unit test for constructor of class ShellModule
def test_ShellModule():

    shell_plugin = ShellModule()
    # test _parse_clixml
    from_output = "#< CLIXML\r\n<Objs Version='1.1.0.1'" \
                  "xmlns='http://schemas.microsoft.com/powershell/2004/04'><S S='Error'>Test</S></Objs>"
    script_error = b"Test"
    assert (shell_plugin._parse_clixml(from_output) == script_error)
    assert (shell_plugin._parse_clixml(b"#< CLIXML\r\n<Objs") == b"")
    assert (shell_plugin._parse_clixml(b"#< CLIXML\r\n<Objs ") == b"")

# Generated at 2022-06-13 14:59:42.573566
# Unit test for constructor of class ShellModule
def test_ShellModule():
  shellmodule=ShellModule()
  shellmodule.join_path('a','b','c')
  return shellmodule

# Generated at 2022-06-13 14:59:52.587689
# Unit test for constructor of class ShellModule
def test_ShellModule():
    #
    # Test scenario 1
    #
    mock_conn = {}

# Generated at 2022-06-13 14:59:56.608346
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()
    assert isinstance(s, ShellModule)
    assert s.SHELL_FAMILY == 'powershell'
    assert s._IS_WINDOWS
    assert s.COMPATIBLE_SHELLS == frozenset()
    assert s.DEFAULT_EXECUTABLE == 'powershell'


# Unit tests for methods of ShellModule

# Generated at 2022-06-13 15:00:07.675975
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    m = ShellModule()
    # Test a normal Windows path
    assert m.path_has_trailing_slash('C:\\Users\\Administrator\\AppData')
    # Test a normal Windows path with a slash at the end
    assert m.path_has_trailing_slash('C:\\Users\\Administrator\\AppData\\')
    # Test a normal Windows path with two slashes at the end
    assert m.path_has_trailing_slash('C:\\Users\\test_dir\\test_dir_dir\\')
    # Test a normal Windows path with two slashes at the end
    assert m.path_has_trailing_slash('C:\\Users\\test_dir\\test_dir_dir\\\\')
    # Test a normal Windows path with a single backslash at the end
    assert not m.path_has_tra

# Generated at 2022-06-13 15:00:16.824735
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ''' shell: powershell
    '''
    shell = ShellModule()
    shebang = shell.get_shebang('python')
    assert shebang == '#!python'

    (rc, out, err) = shell.run_command('echo "test"')
    assert rc == 0
    assert out == 'test'
    assert err == ''

    shell._display.verbosity = 4
    (rc, out, err) = shell.run_command('echo "test"')
    assert rc == 0
    assert out == 'test'
    assert err == ''
    shell._display.verbosity = 0

    path = shell.join_path('/tmp', 'test')
    assert path == '/tmp\\test'

    path = shell.join_path('/tmp', 'test', 'test')

# Generated at 2022-06-13 15:00:23.114181
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm1 = ShellModule()
    sm2 = ShellModule()
    sm3 = ShellModule()
    sm4 = ShellModule()

    assert sm1._SHELL_REDIRECT_ALLNULL == '> $null'
    assert sm2._SHELL_AND == ';'
    assert sm3._IS_WINDOWS == True
    assert sm4._SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:00:31.142138
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert bool(re.match(r'(\d+\.)?(\d+\.)?(\*|\d+)', shell_module.SHELL_VERSION)) == True
    assert isinstance(shell_module._IS_WINDOWS, bool) == True
    assert shell_module.SHELL_FAMILY == 'powershell'
    assert shell_module.COMPATIBLE_SHELLS == frozenset()
    assert shell_module._SHELL_AND == ';'
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'

# Generated at 2022-06-13 15:00:33.365690
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule(connection=None, no_log=False, shell_type='powershell')
    assert shell_module._connection is None
    assert shell_module._no_log is False
    assert shell_module._shell_type == 'powershell'


# Generated at 2022-06-13 15:00:38.369261
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.errors import AnsibleError
    from ansible.executor.powershell import ShellModule
    module_args = dict( _ansible_connection='winrm',
                        remote_tmp='C:\temp',
                        ansible_user='Administrator',
                        ansible_password='ansible',
                        ansible_winrm_server_cert_validation='ignore' )
    shell_module = ShellModule(task=None, connection=None, module_args=module_args)
    assert(isinstance(shell_module, ShellModule))
    assert(shell_module.args == module_args)
    try:
        shell_module.run(['echo testing'])
        assert(False)
    except AnsibleError:
        assert(True)


# Generated at 2022-06-13 15:00:39.494935
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    shell._display.verbosity = 4
    shell.run_command("ipconfig")

# Generated at 2022-06-13 15:00:45.849549
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    Tests the constructor of the ShellModule class.
    '''
    x = ShellModule()
    assert isinstance(x, ShellModule)

# Generated at 2022-06-13 15:00:49.367051
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.module_utils import mock
    the_module = mock.Mock()
    the_module.params = None
    the_module.shell = None
    shell = ShellModule(the_module)
    assert shell is not None

# Generated at 2022-06-13 15:00:57.815154
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    module = ShellModule()
    path = 'C:\\Users'
    assert not module.path_has_trailing_slash(path)
    path = 'C:\\Users\\'
    assert module.path_has_trailing_slash(path)
    path = '\\Users\\'
    assert module.path_has_trailing_slash(path)
    path = '/Users'
    assert module.path_has_trailing_slash(path)
    path = '/Users/'
    assert module.path_has_trailing_slash(path)


# Generated at 2022-06-13 15:01:00.249894
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sh_module = ShellModule()
    assert hasattr(sh_module, 'run')
    assert hasattr(sh_module, '_validate_path')
    assert hasattr(sh_module, 'join_path')

# Generated at 2022-06-13 15:01:09.894977
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule(None)
    assert shell.path_has_trailing_slash('') is False
    assert shell.path_has_trailing_slash('\\') is True
    assert shell.path_has_trailing_slash('C:\\') is True
    assert shell.path_has_trailing_slash('"C:\\"') is True
    assert shell.path_has_trailing_slash('C:\\Windows') is False
    assert shell.path_has_trailing_slash('"C:\\Windows"') is False
    assert shell.path_has_trailing_slash('"C:\\Windows\\"') is True


# Generated at 2022-06-13 15:01:17.092031
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # pylint: disable=protected-access
    sm = ShellModule()
    assert sm.build_module_command('$ENV1;$ENV2', '', '', '') == sm._encode_script(script=sm._bootstrap_wrapper, strict_mode=False, preserve_rc=False)

# Generated at 2022-06-13 15:01:28.099110
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    module_test = ShellModule(connection=None, runner_queue=None)
    assert module_test.path_has_trailing_slash(r'c:\test\test') is False
    assert module_test.path_has_trailing_slash(r'c:\test\test\\') is True
    assert module_test.path_has_trailing_slash(r'\\test\test') is False
    assert module_test.path_has_trailing_slash(r'\\test\test\\') is True
    assert module_test.path_has_trailing_slash(r'\\server\share') is False
    assert module_test.path_has_trailing_slash(r'\\server\share\\') is True

# Generated at 2022-06-13 15:01:39.046646
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # create an instance of ShellModule
    mod = ShellModule(None)

    # test module name without .ps1 extension - execute wrapper
    cmd_name = 'mytest'
    cmd, shebang = mod.build_module_command("", "", "")
    cmd_parts = shlex.split(cmd, posix=False)
    assert cmd_parts[4] == cmd_name

    # test module name with .ps1 extension - execute wrapper
    cmd_name = 'mytest.ps1'
    cmd, shebang = mod.build_module_command("", "", "")
    cmd_parts = shlex.split(cmd, posix=False)
    assert cmd_parts[4] == cmd_name

    # test module name with other extension - execute wrapper
    cmd_name = 'mytest.exe'
    cmd, she

# Generated at 2022-06-13 15:01:47.235049
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''Unit tests for ShellModule class'''
    print("Testing ShellModule class")
    c = ShellModule()
    assert c.path_has_trailing_slash('c:/foo/bar\\')
    assert not c.path_has_trailing_slash('c:/foo/bar')

    assert c.join_path('c:/', 'foo', 'bar/bas') == 'c:\\foo\\bar\\bas'
    assert c.join_path('c:/', 'foo', 'bar\\bas/') == 'c:\\foo\\bar\\bas'
    assert c.join_path('c:/', 'foo/bar\\bas\\') == 'c:\\foo\\bar\\bas'

    assert c.get_remote_filename('c:/foo\\bar/baz.txt') == 'baz.txt'

# Generated at 2022-06-13 15:01:50.497426
# Unit test for constructor of class ShellModule
def test_ShellModule():

    shell = ShellModule()
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS == True

# Generated at 2022-06-13 15:01:57.318159
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():

    shell_module = ShellModule()
    assert shell_module is not None
    result = shell_module.build_module_command('', '', '')
    assert result is not None



# Generated at 2022-06-13 15:02:02.439634
# Unit test for constructor of class ShellModule
def test_ShellModule():

    # init a Windows shell
    powershell = ShellModule(command_name='powershell')
    assert isinstance(powershell, ShellModule)
    assert powershell.SHELL_FAMILY == 'powershell'
    assert powershell._IS_WINDOWS
    assert powershell.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:02:04.107430
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert isinstance(shell, ShellModule)

# Generated at 2022-06-13 15:02:06.909366
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod.SHELL_FAMILY == 'powershell'
    assert mod._SHELL_REDIRECT_ALLNULL == '> $null'
    assert mod._SHELL_AND == ';'



# Generated at 2022-06-13 15:02:17.604775
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shellmodule = ShellModule()
    assert shellmodule.path_has_trailing_slash('C:\\foo\\bar') == False
    assert shellmodule.path_has_trailing_slash('C:\\foo\\bar\\') == True
    assert shellmodule.path_has_trailing_slash('C:\\foo\\') == True
    assert shellmodule.path_has_trailing_slash('C:\\foo') == False

    assert shellmodule.path_has_trailing_slash('C:/foo/bar') == False
    assert shellmodule.path_has_trailing_slash('C:/foo/bar/') == True
    assert shellmodule.path_has_trailing_slash('C:/foo/') == True
    assert shellmodule.path_has_trailing_slash('C:/foo') == False

# Generated at 2022-06-13 15:02:19.224852
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Test creation of shell module"""
    sm = ShellModule()
    assert isinstance(sm, ShellModule)

# Generated at 2022-06-13 15:02:27.932466
# Unit test for constructor of class ShellModule
def test_ShellModule():
    print("\nExecuting [test_ShellModule]...")

    shebang = '#!powershell'
    cmd = 'whoami'
    cm = ShellModule(None)
    cmd_parts = cm.build_module_command("","",cmd)
    print("cmd_parts:%s" % cmd_parts)

    cmd_parts = cm.build_module_command("",shebang,cmd)
    print("cmd_parts[%s]:%s" % (shebang,cmd_parts))

    cmd_parts = cm.build_module_command("","",cmd,cmd)
    print("cmd_parts[%s]:%s" % (cmd,cmd_parts))

    cmd_parts = cm.build_module_command("",shebang,cmd,cmd)

# Generated at 2022-06-13 15:02:35.713841
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule()
    assert(shell.path_has_trailing_slash('test') == False)
    assert(shell.path_has_trailing_slash('test\\') == True)
    assert(shell.path_has_trailing_slash('test\\test') == False)
    assert(shell.path_has_trailing_slash('test\\test\\') == True)
    assert(shell.path_has_trailing_slash('test/test') == False)
    assert(shell.path_has_trailing_slash('test/test/') == True)
    assert(shell.path_has_trailing_slash('test/test\\test') == False)
    assert(shell.path_has_trailing_slash('test\\test\\test/') == True)

# Unit test

# Generated at 2022-06-13 15:02:46.270115
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    sm = ShellModule()

    assert sm.path_has_trailing_slash('/this/is/a/path/') is True
    assert sm.path_has_trailing_slash('C:\\this\\is\\a\\path\\') is True
    assert sm.path_has_trailing_slash('c:\this\is\a\path\\') is True
    assert sm.path_has_trailing_slash('/') is True
    assert sm.path_has_trailing_slash('C:\\') is True

# Generated at 2022-06-13 15:02:47.096695
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module

# Generated at 2022-06-13 15:03:02.672622
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.executor.module_common import get_shebang
    from ansible.utils.display import Display
    from ansible.compat.six import PY3

    display = Display()
    pluginerror_raised = False
    python_exe = ntpath.join(os.path.dirname(os.path.dirname(__file__)), '..', '..', '..', 'test', 'runner', '$py.exe')

    script_modes = (
        ('binary', 'binary_module.exe'),
        ('ps', 'ps_module.ps1'),
        ('ps_with_bin', 'ps_module_with_bin.ps1'),
        ('ps_with_issue_34181', 'ps_module_with_issue_34181.ps1')
    )


# Generated at 2022-06-13 15:03:05.177465
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shellmodule = ShellModule()

    assert 'PowerShell' in shellmodule.COMPATIBLE_SHELLS
    assert not shellmodule.HAS_PERSISTENT_CONNECTION

# Generated at 2022-06-13 15:03:07.583040
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert isinstance(module, ShellModule)


# make sure we can actually execute powershell on the given system

# Generated at 2022-06-13 15:03:10.949737
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Tests that the constructor passes and that the shell class is initialized
    shell = ShellModule()
    assert shell

# Generated at 2022-06-13 15:03:11.861084
# Unit test for constructor of class ShellModule
def test_ShellModule():
    result = ShellModule()
    assert result is not None

# Generated at 2022-06-13 15:03:20.173340
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Testing the constructor of the ShellModule class
    # Calling the __init__ constructor of the ShellModule class
    shell_module = ShellModule()

    # Testing the COMPATIBLE_SHELLS class variable
    compatible_shells = shell_module.COMPATIBLE_SHELLS

    # Testing the SHELL_FAMILY class variable
    shell_family = shell_module.SHELL_FAMILY

    # Testing the _IS_WINDOWS class variable
    is_windows = shell_module._IS_WINDOWS

    # Testing the _SHELL_REDIRECT_ALLNULL class variable
    shell_redirect_allnull = shell_module._SHELL_REDIRECT_ALLNULL

    # Testing the _SHELL_REDIRECT_ALLNULL class variable
    shell_and = shell_module._SHELL_AND

    # Testing the env_prefix()

# Generated at 2022-06-13 15:03:22.508488
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule()
    assert m.COMPATIBLE_SHELLS == {}
    assert m.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:03:25.830929
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()



# Generated at 2022-06-13 15:03:28.602666
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule('ansible', 'localhost', {}, 'winrm', 'winrm')
    assert s.SHELL_FAMILY == 'powershell'
    assert s._IS_WINDOWS



# Generated at 2022-06-13 15:03:36.306485
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_plugin = ShellModule()
    assert shell_plugin.SHELL_FAMILY == 'powershell'

    # Test that _unquote removes single and double quotes
    quoted_value = "test"
    assert shell_plugin._unquote("'%s'" % quoted_value) == quoted_value
    assert shell_plugin._unquote('"%s"' % quoted_value) == quoted_value
    # Test that _escape escapes all five characters that may need escaping in powershell for single quoted values
    assert shell_plugin._escape("test") == "test"
    assert shell_plugin._escape("test'") == "test''"
    assert shell_plugin._escape("test\u2018") == "test\u2018\u2018"
    assert shell_plugin._escape("test\u2019") == "test\u2019\u2019"

# Generated at 2022-06-13 15:03:50.430276
# Unit test for constructor of class ShellModule
def test_ShellModule():
    options = dict(
        executable='/bin/sh',
        become=False,
        become_method='',
        become_user='',
        check=False,
        diff=False,
        remote_tmp='/tmp'
    )
    shell_obj = ShellModule(connection=None, runner_cache=dict(), play_context=None, loader=None, options=options,
                            passwords=dict())
    assert shell_obj.get_remote_filename('test') == 'test'
    assert shell_obj.get_remote_filename('test.ps1') == 'test.ps1'
    assert shell_obj.get_remote_filename('test.exe') == 'test.exe'
    assert shell_obj.get_remote_filename('test.sh') == 'test.ps1'
    assert shell_obj.get_remote

# Generated at 2022-06-13 15:03:51.973062
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Instantiate the base class, which does nothing
    ShellModule()

# Generated at 2022-06-13 15:03:54.334402
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule.COMPATIBLE_SHELLS == frozenset()
    assert ShellModule.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:03:58.705249
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule(None)
    assert obj._SHELL_REDIRECT_ALLNULL == '> $null'
    assert obj._SHELL_AND == ';'
    assert obj._IS_WINDOWS == 'true'
    assert obj.COMPATIBLE_SHELLS == '{}'
    assert obj.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:04:02.069270
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm.SHELL_FAMILY == 'powershell'
    assert sm._SHELL_REDIRECT_ALLNULL == '> $null'
    assert sm._SHELL_AND == ';'
    sm = ShellModule()


# Generated at 2022-06-13 15:04:04.033592
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # This can be removed once Python 3.7 becomes the min version
    o = ShellModule()
    o._encode_script('foo', strict_mode=True)

# Generated at 2022-06-13 15:04:04.789735
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # TODO: Write a unit test
    assert False

# Generated at 2022-06-13 15:04:06.723837
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    This test does not need to do much here as the main code is in the abstract
    class ShellBase.
    """
    shell = ShellModule(connection=None)
    assert shell is not None

# Generated at 2022-06-13 15:04:08.813506
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert isinstance(shell.COMPATIBLE_SHELLS, frozenset)
    assert isinstance(shell.SHELL_FAMILY, str)
    assert shell._IS_WINDOWS

# Generated at 2022-06-13 15:04:13.157461
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Simple test to make sure the module constructor works.
    """
    sm = ShellModule()
    assert sm


# Generated at 2022-06-13 15:04:21.670617
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module != None

    ShellModule._SHELL_REDIRECT_ALLNULL = '> $null 2>&1'
    assert module.wrap_for_exec("testcmd") == '& testcmd > $null 2>&1; exit $LASTEXITCODE'

# Generated at 2022-06-13 15:04:24.705565
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module._COMPATIBLE_SHELLS == frozenset()
    assert shell_module._SHELL_FAMILY == 'powershell'
    assert shell_module._IS_WINDOWS



# Generated at 2022-06-13 15:04:31.986483
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible_collections.ansible.windows.plugins.module_utils import shell as shell_module
    shell_mod = shell_module.ShellModule()
    assert shell_mod.get_remote_filename('/tmp/test') == 'test.ps1'
    assert shell_mod.get_remote_filename('/tmp/test.txt') == 'test.txt'
    assert shell_mod.get_remote_filename('/tmp/test.ps1') == 'test.ps1'
    assert shell_mod.get_remote_filename('/tmp/test.exe') == 'test.exe'

# Generated at 2022-06-13 15:04:33.332194
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Needs to have all attributes of the ShellBase class
    return ShellModule()

# Generated at 2022-06-13 15:04:34.716657
# Unit test for constructor of class ShellModule
def test_ShellModule():
    myShellCmd = ShellModule()
    assert myShellCmd is not None

# Generated at 2022-06-13 15:04:35.895456
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Call the constructor
    shell_instance = ShellModule()
    assert shell_instance is not None

# Generated at 2022-06-13 15:04:43.071118
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():

    # tests for non-pipelining
    # Note: In some cases the shebang is not used
    test_cases = [
        ('', '', '', '', ''),
        ('#!', '', '', '', ''),
        ('#!powershell', '', '', '', 'type .ps1 | . .\\ansible_modlib.zip; .\\my_module.ps1'),
        ('#!powershell', '', 'ping -n 1 127.0.0.1', '', 'type .ps1 | . .\\ansible_modlib.zip; ping -n 1 127.0.0.1'),
    ]


# Generated at 2022-06-13 15:04:43.662205
# Unit test for constructor of class ShellModule
def test_ShellModule():
    pass

# Generated at 2022-06-13 15:04:52.677394
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    context = PlayContext()
    result = TaskResult(host=None, task=None)
    result._result = dict(stdout=AnsibleUnsafeText(u'foo'),
                          stderr=AnsibleUnsafeText(u'bar'),
                          rc=0
                          )
    shell = ShellModule(result=result, context=context)

    # splitting allows for command and arguments
    assert shell.split_command('foo bar baz', False, False) == ['PowerShell', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Unrestricted', 'foo', 'bar baz']

# Generated at 2022-06-13 15:04:59.951525
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import datetime

    class OptionsModule(object):
        def __init__(self):
            self.accelerate = False
            self.accelerate_port = 5099
            self.accelerate_ipv6 = False
            self.become = False
            self.become_method = 'sudo'
            self.become_user = 'root'
            self.become_flags = ''
            self.check = False
            self.connection = 'paramiko'
            self.diff = False
            self.executable = None
            self.flush_cache = False
            self.force_handlers = False
            self.forks = 5
            self.remote_tmp = "~/.ansible/tmp"
            self.help = False
            self.private_key_file = None
            self.listhosts = None

# Generated at 2022-06-13 15:05:14.919457
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule(connection=None, play_context=None, shell_executable="C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
                    stdin=None, stdout=None, stderr=None, sudoable=True, become_flags=None, become_method=None,
                    become_user=None, check_rc=True, executable='C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe',
                    environment_variables=None, ansible_shell_type='powershell')
    assert s is not None
    assert s.SHELL_FAMILY == 'powershell'
    assert s.COMPATIBLE_SHELLS == frozenset()


# Generated at 2022-06-13 15:05:25.940389
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.executor.powershell as shell
    from ansible.module_utils.six import PY2
    from ansible.module_utils import common as c_u

    # Make test connection
    class Connection:
        def __init__(self, shells):
            self.shells = shells

        def get_shell_plugins(self):
            return self.shells

    # Make test module
    class ShellModuleTest(AnsibleModule):
        def __init__(self):
            super(ShellModuleTest, self).__init__(
                argument_spec=dict(
                    free_form=dict(type='str', choices=[]),
                ),
                supports_check_mode=False)

    # Unit test the  constructor

# Generated at 2022-06-13 15:05:33.090856
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    s = ShellModule(connection=None, become_method=None, become_user=None)
    env_string = s.env_prefix()
    cmd = 'write-output "Hello World"\r\n'

    # no shebang
    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")
    wrapper_cmd = 'type  | ' + s._encode_script(script=bootstrap_wrapper, strict_mode=False, preserve_rc=False)
    result = s.build_module_command(env_string, '', cmd, arg_path=None)
    assert result == wrapper_cmd

    # valid shebang
    # Note: we have to remove the carriage return at the end of the bootstrap wrapper script otherwise it
    # will fail the comparison

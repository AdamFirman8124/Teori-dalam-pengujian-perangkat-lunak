

# Generated at 2022-06-13 14:55:37.555574
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    # This class is just for testing purpose
    class TestShellModule(ShellModule):

        @staticmethod
        def _generate_temp_dir_name():
            """Return a temp directory name."""
            return 'tmp'

    # Execute get_remote_filename method of ShellModule and compare the returned value
    sh = TestShellModule()
    chk_filename = 'test_utils.py'
    assert sh.get_remote_filename(chk_filename) == chk_filename



# Generated at 2022-06-13 14:55:45.020185
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    '''Unit test for the ShellModule method expand_user.
    '''
    shell = ShellModule()

    # test regular user's home
    user_home_path = shell.expand_user('~', 'vagrant')
    print('user_home_path: %s' % user_home_path)
    assert user_home_path == 'Write-Output "C:\\Users\\vagrant"'

    # test for current user home
    user_home_path = shell.expand_user('~')
    print('user_home_path: %s' % user_home_path)
    assert user_home_path == 'Write-Output (Get-Location).Path'

    # test for current user home with a subdir name
    user_home_path = shell.expand_user('~\\.vagrant.d')
   

# Generated at 2022-06-13 14:55:47.631022
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    sm = ShellModule()
    assert sm.path_has_trailing_slash('c:\\temp\\')
    assert sm.path_has_trailing_slash('c:/temp/')
    assert not sm.path_has_trailing_slash('c:\\temp')
    assert not sm.path_has_trailing_slash('c:/temp')

# Generated at 2022-06-13 14:55:49.569931
# Unit test for constructor of class ShellModule
def test_ShellModule():
    win_conn = ShellModule()
    assert(win_conn.SHELL_FAMILY == 'powershell')

# Generated at 2022-06-13 14:55:50.291172
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()

# Generated at 2022-06-13 14:55:56.397270
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule()
    assert not shell.path_has_trailing_slash('C:/Users/Administrator/')
    assert shell.path_has_trailing_slash('C:\\Users\\Administrator')
    assert shell.path_has_trailing_slash('C:\\Users\\Administrator\\')
    assert not shell.path_has_trailing_slash('/Users/Administrator')
    assert shell.path_has_trailing_slash('/Users/Administrator/')

# Generated at 2022-06-13 14:56:00.108892
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Test ShellModule constructor"""
    from ansible.plugins.shell.powershell import ShellModule
    # For each string, test that the constructor correctly decodes it.
    for param in ['unquoted_param', '"quoted_param"']:
        sm = ShellModule('')
        assert sm._unquote(param) == 'unquoted_param'

# Generated at 2022-06-13 14:56:08.341273
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import ansible.module_utils
    from ansible.module_utils.six.moves import StringIO

    module_replacement_args = dict(
        ANSIBLE_MODULE_ARGS=dict(),
        ANSIBLE_MODULE_CONSTANTS=dict(),
    )

    mod = ShellModule(connection='winrm', no_log=True, **module_replacement_args)

    # Test that build_module_command properly wraps binary module commands
    # with bootstrap powershell
    test_cmd = 'bin/foo.exe "arg1 arg2" arg3'

# Generated at 2022-06-13 14:56:09.675435
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """This is a test method to verify that the ShellModule constructor can be called with no parameters."""
    ShellModule()

# Generated at 2022-06-13 14:56:11.627202
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'
    assert module.COMPATIBLE_SHELLS == frozenset()


# Generated at 2022-06-13 14:56:16.713951
# Unit test for constructor of class ShellModule
def test_ShellModule():
    powershell = ShellModule(connection=None)
    assert powershell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert powershell._SHELL_AND == ';'
    assert powershell._IS_WINDOWS == True

# Generated at 2022-06-13 14:56:18.433647
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule()
    assert obj.COMPATIBLE_SHELLS == ('powershell',)
    assert obj.SHELL_FAMILY == 'powershell'
    assert obj._IS_WINDOWS

# Generated at 2022-06-13 14:56:24.437064
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():

    import ansible.plugins.shell.powershell

    e = ansible.executor.powershell.ShellModule(connection=None)
    cmd = "test_cmd"
    shebang = "#!powershell"
    expected_response = "type test_cmd.ps1 | %s" % e._encode_script(script=pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1"), strict_mode=False, preserve_rc=False)
    result = e.build_module_command(env_string='', shebang=shebang, cmd=cmd)

    assert result == expected_response

# Generated at 2022-06-13 14:56:36.354429
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.shell.powershell import ShellModule
    import subprocess

    def get_rc(cmd):
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        lines = proc.communicate()[0].split('\r\n')
        return proc.returncode, lines

    # Test case 1: binary module which is attempted to be launched directly by the ShellModule because it doesn't have the
    # shebang header.
    env_dict = dict()
    module_instance = AnsibleModule(argument_spec=dict(a=dict()))

# Generated at 2022-06-13 14:56:44.304964
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    powershell = ShellModule()
    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")

    # Test normal module running
    env_string = '$Env:FOO=BAR'
    shebang = '#!powershell'
    cmd = 'echo "OK"'
    result = powershell.build_module_command(env_string, shebang, cmd)
    expect = powershell._encode_script(script='\n'.join([env_string, cmd, 'If (-not $?) { exit 1 }\r\n']),
                                       preserve_rc=False)
    assert result == '& %s; exit $LASTEXITCODE' % expect
    # Test bypass pipelining
    cmd = ''
    result = powershell.build_

# Generated at 2022-06-13 14:56:52.006751
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import platform
    # On Python 3 we need to ensure that we are using a unicode string as
    # otherwise the decoding of the script will fail as Py3's b64decode expects
    # unicode strings.
    tmp_dir = platform.system() == 'Windows' and u'C:\\Windows\\Temp' or u'/tmp'
    module = ShellModule()
    script = module.mkdtemp(tmpdir=tmp_dir)
    # the encoded string has a length that is a multiple of 4
    assert len(script) % 4 == 0
    # decode and extract the module command
    script = base64.b64decode(script.encode('utf-8')).decode('utf-16-le')
    shebang, env_string, cmd, args = script.split('\n', 3)

# Generated at 2022-06-13 14:56:56.915851
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule()
    assert not m.IS_BINARY
    assert m.DEFAULT_EXECUTABLE == 'powershell'
    assert m.SHELL_MODULE_EXECUTABLE == 'powershell'
    assert m.SHELL_MODULE_ARGS == '-NoProfile -NonInteractive -ExecutionPolicy Unrestricted'

# Generated at 2022-06-13 14:57:05.292833
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell_module = ShellModule()
    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")

# Generated at 2022-06-13 14:57:16.424193
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule()
    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")
    # non-pipelining
    # binary module
    cmd = "7z.exe a -t7z myarchive.tar.7z myarchive.tar"
    arg_path = shell.get_remote_filename('myacrhive.tar')

# Generated at 2022-06-13 14:57:21.128083
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    t_cmd = 'test'
    t_module_path = 'test_path'

    shell_module = ShellModule()
    command = shell_module.build_module_command(env_string='test', shebang='#!powershell', cmd=t_cmd, arg_path=t_module_path)

    assert command.startswith('"& { $ret=@(); $error_action_preference=\'stop\'; try { & {{ $_ansible_no_log=')
    assert t_module_path in command
    assert t_cmd in command

# Generated at 2022-06-13 14:57:34.881121
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    # Test for the case where suffixes should be added
    extension_should_be_added = [
        './test',
        '.\\test'
    ]
    for extension in extension_should_be_added:
        test_module = ShellModule()
        assert test_module.get_remote_filename(extension) == 'test.ps1'

    # Test for the case where the extension is included in the filename
    extension_should_be_included = [
        './test.py'
    ]
    for extension in extension_should_be_included:
        test_module = ShellModule()
        assert test_module.get_remote_filename(extension) == 'test.py'

    # Test for the case where the filename is empty
    test_module = ShellModule()
    assert test_module.get_remote_filename

# Generated at 2022-06-13 14:57:38.480324
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()

    assert module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module._SHELL_AND ==';'
    assert module._IS_WINDOWS == True



# Generated at 2022-06-13 14:57:46.203996
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    shell_mod = ShellModule()
    # test file with .ps1 extention - should be left unchanged
    assert shell_mod.get_remote_filename('foo.ps1') == 'foo.ps1'
    # test file without .ps1 extention - .ps1 extention should be added
    assert shell_mod.get_remote_filename('foo') == 'foo.ps1'
    # test file with .exe extention - should be left unchanged
    assert shell_mod.get_remote_filename('foo.exe') == 'foo.exe'

# Generated at 2022-06-13 14:57:51.923765
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    shell = ShellModule()
    actual = shell.get_remote_filename("foo.sh")
    assert actual == 'foo.ps1'
    actual = shell.get_remote_filename("bar/foo.sh")
    assert actual == 'foo.ps1'
    actual = shell.get_remote_filename("bar/baz.ps1")
    assert actual == 'baz.ps1'
    actual = shell.get_remote_filename("bar/baz.exe")
    assert actual == 'baz.exe'

# Generated at 2022-06-13 14:57:58.942172
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    module = ShellModule()
    assert 'myfile.ps1' == module.get_remote_filename('myfile')
    assert 'myfile.ps1' == module.get_remote_filename('myfile.exe')
    assert 'myfile.exe' == module.get_remote_filename('myfile.exe.ps1')
    assert 'myfile.exe' == module.get_remote_filename('myfile.exe.exe')

# Unit tests for method _parse_clixml

# Generated at 2022-06-13 14:58:00.280456
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sh = ShellModule()
    # This is just a stub to instantiate the class
    pass

# Generated at 2022-06-13 14:58:01.508794
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Create a new ShellModule object
    shell_module = ShellModule()

# Generated at 2022-06-13 14:58:08.824549
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    print(sm.get_option('remote_tmp'))
    print(sm.COMPATIBLE_SHELLS)
    print(sm.SHELL_FAMILY)
    print(sm._IS_WINDOWS)
    print(sm.COMPATIBLE_SHELLS)
    print(sm.env_prefix())
    print(sm.join_path('c:\\parent\\child'))
    print(sm.join_path('c:\\parent\\child', 'other\\'))
    print(sm.get_remote_filename('c:\\parent\\child\\name.ps1'))
    print(sm.path_has_trailing_slash('c:\\parent\\child\\'))
    print(sm.chmod('c:\\parent\\child', 777))

# Generated at 2022-06-13 14:58:17.163117
# Unit test for constructor of class ShellModule
def test_ShellModule():
    env_vars = [
        'PATH=/usr/bin:/usr/local/bin',
        'FOO=BAR'
    ]

    transport = 'ssh'
    executable = None
    shell = ShellModule(transport=transport, executable=executable)

    assert shell.chmod == ShellModule.chmod
    assert shell.chown == ShellModule.chown
    assert shell.set_user_facl == ShellModule.set_user_facl
    assert shell.remove == ShellModule.remove
    assert shell.mkdtemp == ShellModule.mkdtemp
    assert shell.expand_user == ShellModule.expand_user
    assert shell.exists == ShellModule.exists
    assert shell.checksum == ShellModule.checksum
    assert shell.build_module_command == ShellModule.build_module_command

# Generated at 2022-06-13 14:58:18.031737
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()

# Generated at 2022-06-13 14:58:32.158754
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    temp_dir = shell.run_command('echo %TEMP%').splitlines()[0]
    temp_dir = temp_dir.strip()

    # test creation of temporary files
    mode = '0700'
    basefile = 'test_file'
    tmpdir = temp_dir
    if not shell.path_has_trailing_slash(temp_dir):
        tmpdir += '\\'
    command = shell.mkdtemp(basefile=basefile, mode=mode, tmpdir=tmpdir)
    out = shell.run_command(command)
    dirname = out.strip()
    assert os.path.isdir(dirname)
    assert dirname == temp_dir + '\\' + basefile

    # test check for existence of files/directories
    command = shell.ex

# Generated at 2022-06-13 14:58:36.420056
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod is not None
    assert mod._SHELL_REDIRECT_ALLNULL == '> $null'
    assert mod._SHELL_AND == ';'
    assert mod._IS_WINDOWS == True
    assert not hasattr(mod, 'SHELL_FAMILY')

# Generated at 2022-06-13 14:58:40.980246
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Confirm that the constructor returns an object with the correct type
    shell_obj = ShellModule()
    assert type(shell_obj) == ShellModule
    assert shell_obj.COMPATIBLE_SHELLS == frozenset()
    assert shell_obj.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 14:58:42.129229
# Unit test for constructor of class ShellModule
def test_ShellModule():
    a = ShellModule()

# Generated at 2022-06-13 14:58:48.774813
# Unit test for constructor of class ShellModule
def test_ShellModule():
    #
    # Test case 1
    #
    # Create a object of the class ShellModule with required parameters
    #
    obj = ShellModule()
    assert obj is not None
    assert obj._IS_WINDOWS == True
    assert obj.COMPATIBLE_SHELLS == frozenset()
    assert obj.SHELL_FAMILY == 'powershell'
    assert obj._SHELL_REDIRECT_ALLNULL == "> $null"
    assert obj._SHELL_AND == ";"

# Generated at 2022-06-13 14:58:59.307399
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    module = ShellModule(connection=None, no_log=True)

    # Test 1: No basefile, no tmpdir
    script = module.mkdtemp()
    assert script.count(module._SHELL_AND) == 2
    assert '$tmp_path = [System.Environment]::ExpandEnvironmentVariables('') + "/tmp"' in script
    assert '$tmp = New-Item -Type Directory -Path $tmp_path -Name' in script
    assert 'Write-Output -InputObject $tmp.FullName' in script

    # Test 2: basefile, no tmpdir
    basefile = 'foo'
    script = module.mkdtemp(basefile)
    assert script.count(module._SHELL_AND) == 2

# Generated at 2022-06-13 14:59:02.653227
# Unit test for constructor of class ShellModule
def test_ShellModule():

    shell_obj = ShellModule('test_shell_object', timeout=1)

    assert shell_obj
    assert shell_obj._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_obj._SHELL_AND == ';'



# Generated at 2022-06-13 14:59:12.995748
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule(command_has_changed=True, become_method='runas', become_user='cloud_user', become_password='password', bin_ansible_call='ansible', use_persistent_connection=False, become=False, become_exe='runas.exe', become_user_method='sudo', no_log=False, check=False, diff=False)
    assert obj.command_has_changed == True
    assert obj.become_method == 'runas'
    assert obj.become_user == 'cloud_user'
    assert obj.become_password == 'password'
    assert obj.bin_ansible_call == 'ansible'
    assert obj.use_persistent_connection == False
    assert obj.become == False
    assert obj.become_exe == 'runas.exe'
   

# Generated at 2022-06-13 14:59:13.748265
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 14:59:17.919396
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell_module = ShellModule()
    assert shell_module.mkdtemp() == b'$tmp=(New-Item -Type Directory -Path (Get-Location).Path -Name \'ansiballz*\');Write-Output -InputObject $tmp.FullName;'

# Generated at 2022-06-13 14:59:29.209295
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")

    # test for binary modules (normally we're just running the bootstrap wrapper)
    cmd = 'echo'
    arg_path = '%s hello' % cmd
    sm = ShellModule()
    cmd = sm.build_module_command('', None, cmd, arg_path)
    assert cmd == "type echo.ps1 | %s" % bootstrap_wrapper
    cmd = sm.build_module_command('', None, cmd, '')
    assert cmd == bootstrap_wrapper



# Generated at 2022-06-13 14:59:39.207394
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import ansible_powershell_shell
    import tempfile
    import shutil
    import os.path
    from hashlib import sha1
    from ansible.parsing.vault import VaultLib

    # create a fake .ps1 file and store its SHA1 for validation
    # NOTE: this assumes a UNIX-like environment
    vault_password_file = tempfile.NamedTemporaryFile()
    module_name = 'example'
    bootstrap_wrapper = pkgutil.get_data('ansible.executor.powershell', 'bootstrap_wrapper.ps1')
    vault_password_file.write(to_bytes(VaultLib.encrypt(bootstrap_wrapper, password='ansible')))
    vault_password_file.flush()
    vault_password_file_path = vault_password_file.name
   

# Generated at 2022-06-13 14:59:45.534790
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule(connection=None, sort_buffer_size=1024, no_log=True)
    assert shell_obj is not None
    # No exception should be generated with invalid arguments
    try:
        shell_obj = ShellModule(connection="abc", sort_buffer_size=1024, no_log=True)
        assert shell_obj is not None
    except Exception:
        raise AssertionError("ShellModule constructor should not produce exception with invalid arguments")

# Generated at 2022-06-13 14:59:49.994826
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    mod = ShellModule()
    mod.get_option = lambda _: ''
    # Test to ensure that this doesn't cause an exception
    mod.mkdtemp('base.ps1')
    # Test to ensure that it returns a string
    assert isinstance(mod.mkdtemp('base.ps1'), str)

# Generated at 2022-06-13 14:59:56.455906
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import tempfile
    from shutil import rmtree
    from ansible.executor.powershell.shell_abstract import IS_WINDOWS
    if IS_WINDOWS:
        shell = ShellModule()
        basefile = tempfile.mktemp()
        command = shell.mkdtemp(basefile)
        print("Basefile = %s" % basefile)
        assert "New-Item -Type Directory -Path" in to_text(command)
        assert basefile in to_text(command)
        rmtree(basefile)

# Generated at 2022-06-13 15:00:07.591602
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import os
    import ansible.plugins.powershell.ShellModule

    test = ansible.plugins.powershell.ShellModule()
    test.get_option = lambda opt: None
    os.environ["USERNAME"] = "ansible"
    os.environ["USERPROFILE"] = "C:\\Users\\ansible"

    os.environ["HOMEDRIVE"] = "C:"
    os.environ["HOMEPATH"] = "\\Users\\ansible"
    os.environ["TEMP"] = "C:\\Users\\ansible\\AppData\\Local\\Temp"
    os.environ["TMP"] = "C:\\Users\\ansible\\AppData\\Local\\Temp"


# Generated at 2022-06-13 15:00:09.023037
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Ensure we're a subclass of ShellBase"""
    assert issubclass(ShellModule, ShellBase)


# Generated at 2022-06-13 15:00:12.366740
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module.COMPATIBLE_INTERPRETER_NAMES == frozenset()

# Generated at 2022-06-13 15:00:14.545916
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Constructor
    try:
        ShellModule()
    except Exception:
        raise AssertionError("The constructor of the class ShellModule() has been altered")


# Generated at 2022-06-13 15:00:24.803760
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection='test_connection')

    # Test string passed in correctly
    assert module.connection == 'test_connection'

    # Test _SHELL_REDIRECT_ALLNULL inherited correctly
    assert module._SHELL_REDIRECT_ALLNULL == "> $null"

    # Test _SHELL_AND inherited correctly
    assert module._SHELL_AND == ';'

    # Test _IS_WINDOWS inherited correctly
    assert module._IS_WINDOWS

    # Test COMPATIBLE_SHELLS inherited correctly
    assert module.COMPATIBLE_SHELLS == frozenset()

    # Test SHELL_FAMILY inherited correctly
    assert module.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:00:35.517239
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    cmd = to_text(module.join_path('foo', 'bar'))
    assert cmd == 'foo\\bar'
    cmd = to_text(module.join_path('foo/bar'))
    assert cmd == 'foo\\bar'
    cmd = to_text(module.join_path('/foo', 'bar'))
    assert cmd == '\\foo\\bar'
    cmd = to_text(module.join_path('/foo', 'bar/'))
    assert cmd == '\\foo\\bar'
    cmd = to_text(module.join_path('/foo', 'bar/', '/baz'))
    assert cmd == '\\foo\\bar\\baz'
    cmd = to_text(module.join_path('foo//bar', 'baz'))

# Generated at 2022-06-13 15:00:42.313966
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible_collections.ansible.executor.plugins.module_utils.powershell import ShellModule

    test_object = ShellModule()
    expected_result = test_object._encode_script("""
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('/tmp')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'ansible-tmp-1533137875.28-168502732013851'
        Write-Output -InputObject $tmp.FullName
        """)

    actual_result = test_object.mkdtemp()
    assert actual_result == expected_result

    basefile = '/var/tmp/ansible-tmp-myfile'
    tmpdir = '/var/tmp'

# Generated at 2022-06-13 15:00:45.808599
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule()
    assert m.COMPATIBLE_SHELLS == frozenset()
    assert m.SHELL_FAMILY == "powershell"
    assert m._SHELL_REDIRECT_ALLNULL == "> $null"
    assert m._SHELL_AND == ";"


# Generated at 2022-06-13 15:00:47.161392
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Make sure the constructor of ShellModule can be loaded successfully
    assert ShellModule(dict())

# Generated at 2022-06-13 15:00:58.401707
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()

    assert mod.COMPATIBLE_SHELLS == frozenset()
    assert mod.SHELL_FAMILY == 'powershell'
    assert mod._IS_WINDOWS

    assert mod.join_path("c:\\temp", "\\test\\test.txt") == "c:\\temp\\test\\test.txt"
    assert mod.join_path("c:\\temp\\", "\\test\\test.txt") == "c:\\temp\\test\\test.txt"
    assert mod.join_path("c:\\temp\\", "\\test") == "c:\\temp\\test"
    assert mod.join_path("c:\\temp\\", "test") == "c:\\temp\\test"

# Generated at 2022-06-13 15:01:09.156047
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()

    # check common args and script loading
    base64_encoded_script = base64.b64encode(('ScriptData', 'ScriptContents'))
    shell_script_load_command = '{0} "{1}"'.format(' '.join(_common_args), base64_encoded_script, )
    assert shell._encode_script('ScriptData') == shell_script_load_command
    assert shell._encode_script('ScriptData', as_list=True) == _common_args + ['-EncodedCommand', base64_encoded_script]

    # check that we're getting back the same result and that the results are of the same type (list vs string)

# Generated at 2022-06-13 15:01:17.624474
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.module_utils._text import to_bytes
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.module_common import ModuleParameters
    from ansible.module_utils.connection import Connection
    from ansible.playbook.play import Play
    from ansible.plugins.shell import ShellModule
    connection = Connection('winrm')
    play = Play().load({}, variable_manager={}, loader=None)
    m = ShellModule(connection, play=play)
    assert isinstance(m, ShellModule)
    assert hasattr(m, 'conn')
    assert hasattr(m, '_options')
    assert hasattr(m, 'no_log')
    assert hasattr(m, '_task')
    assert not hasattr(m, '_shell_type')
   

# Generated at 2022-06-13 15:01:19.171996
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()

# Generated at 2022-06-13 15:01:20.449961
# Unit test for constructor of class ShellModule
def test_ShellModule():
    x = ShellModule()
    assert x != None



# Generated at 2022-06-13 15:01:26.545939
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test that powershell is not a 'compatible' shell.  This means the shell
    # is selected when winrm is used, not the other way around
    module = ShellModule()
    assert 'powershell' not in module.COMPATIBLE_SHELLS.lower()
    assert module.SHELL_FAMILY == 'powershell'
    assert module._IS_WINDOWS is True


# Generated at 2022-06-13 15:01:32.971495
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule()
    assert shell_obj._IS_WINDOWS

# Generated at 2022-06-13 15:01:43.007568
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule(connection=None)
    assert hasattr(obj, 'env_prefix')
    assert hasattr(obj, 'join_path')
    assert hasattr(obj, 'get_remote_filename')
    assert hasattr(obj, 'path_has_trailing_slash')
    assert hasattr(obj, 'chmod')
    assert hasattr(obj, 'chown')
    assert hasattr(obj, 'set_user_facl')
    assert hasattr(obj, 'remove')
    assert hasattr(obj, 'mkdtemp')
    assert hasattr(obj, 'expand_user')
    assert hasattr(obj, 'exists')
    assert hasattr(obj, 'checksum')
    assert hasattr(obj, 'build_module_command')

# Generated at 2022-06-13 15:01:47.832546
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    test_powershell = ShellModule(dict())

    # test for no basefile
    result = test_powershell.mkdtemp()

    assert 'mkdtemp' in result

    # test for no basefile
    result = test_powershell.mkdtemp('basefile')

    assert 'basefile' in result

    # test for no basefile
    result = test_powershell.mkdtemp('basefile', tmpdir='tmpdir')

    assert 'basefile' in result
    assert 'tmpdir' in result

# Generated at 2022-06-13 15:01:57.842029
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.plugins.loader import connection_loader

    mock_connection = connection_loader.get('local')
    # Get the powershell shell plugin
    # 5 is index of ansible.executor.powershell_connection.Connection
    mock_connection.__class__ = connection_loader.all()[5]
    test_task_executor = TaskExecutor(mock_connection, 'test')
    test_task_executor.become = False
    test_task_executor.noop_task = None
    test_task_executor.task = None
    # Check if ShellModule correctly inherits ShellBase and is instance of ShellModule

# Generated at 2022-06-13 15:02:02.382374
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    sm = ShellModule()
    # can't use assertRaisesRegexp because of Python 2.6 support
    try:
        sm.mkdtemp()
    except NotImplementedError as e:
        assert "chmod is not implemented for Powershell" in str(e)

# Generated at 2022-06-13 15:02:05.199430
# Unit test for constructor of class ShellModule
def test_ShellModule():

    shell_obj = ShellModule()

    assert shell_obj.COMPATIBLE_SHELLS == frozenset()
    assert shell_obj.SHELL_FAMILY == 'powershell'
    assert shell_obj._IS_WINDOWS == True



# Generated at 2022-06-13 15:02:06.087668
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert(ShellModule() is not None)

# Generated at 2022-06-13 15:02:07.717536
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_FAMILY.lower() == 'powershell'

# Generated at 2022-06-13 15:02:08.914795
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    if shell is None:
        raise Exception('Failed to create shell.')


# Generated at 2022-06-13 15:02:15.413397
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.plugins.shell import ShellModule
    from ansible.module_utils.common import load_platform_subclass

    obj = load_platform_subclass(ShellModule, 'subclass')

    assert obj._SHELL_REDIRECT_ALLNULL == '> $null'
    assert obj._SHELL_AND == ';'

# Generated at 2022-06-13 15:02:31.382812
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Test ShellModule class constructor
    """
    connection = type('connection', (object,), {'_shell': None, '_connected': None, '_connected_to': None})
    pc = type('pc', (object,), {'become': False, 'become_user': None, 'become_pass': None})
    temppath = os.path.realpath(__file__).split("lib")[0] + 'test/testresources/temp'
    loader = type('loader', (object,), {'cfgs': {'DEFAULT': {'remote_tmp': temppath, 'connection': connection, 'module_lang': 'powershell_script', 'module_ext': '.ps1', 'module_set_locale': False}, 'privilege_escalation': pc}})
    sm = ShellModule(loader)

# Generated at 2022-06-13 15:02:32.609138
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ansible_module_instance = ShellModule()

if __name__ == '__main__':
    test_ShellModule()

# Generated at 2022-06-13 15:02:33.996006
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:02:34.825633
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm_instance = ShellModule()

# Generated at 2022-06-13 15:02:38.058854
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule(connection=None)
    shell_module.sanitize_output = False
    assert type(shell_module) is ShellModule

# Generated at 2022-06-13 15:02:40.226533
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.executor.powershell
    s = ShellModule('test')
    print(s)
    assert type(s) is ShellModule

# Generated at 2022-06-13 15:02:42.574607
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Test the constructor of the ShellModule class
    """

    sm = ShellModule()
    assert isinstance(sm, ShellModule)

# Generated at 2022-06-13 15:02:43.518273
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module_instance = ShellModule()

# Generated at 2022-06-13 15:02:46.186327
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule(connection=None, shell_executable=u'powershell', no_log=False)
    assert isinstance(m, ShellModule)

# Generated at 2022-06-13 15:02:50.040543
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None)
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell._IS_WINDOWS is True
    assert shell.env_prefix() == ''


# Generated at 2022-06-13 15:03:20.555518
# Unit test for constructor of class ShellModule
def test_ShellModule():

    from ansible.compat.tests import unittest

    class TestShellModule(unittest.TestCase):

        def test_empty_init(self):
            shell_module = ShellModule(connection=None)
            self.assertEqual(shell_module.SHELL_FAMILY, 'powershell')
            self.assertEqual(shell_module.COMPATIBLE_SHELLS, ('powershell',))

    unittest.main()

if __name__ == '__main__':
    test_ShellModule()

# Generated at 2022-06-13 15:03:30.588355
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule()
    assert shell_obj.COMPATIBLE_SHELLS == frozenset()
    assert shell_obj.SHELL_FAMILY == 'powershell'
    assert shell_obj._IS_WINDOWS
    assert not hasattr(shell_obj, '_IS_POSIX')
    assert shell_obj.COMMAND_CALLBACK_CLASS is None
    assert shell_obj.COMMAND_CALLBACK is None
    assert not hasattr(shell_obj, '_is_pipelining')
    assert not hasattr(shell_obj, '_is_pipelining_error')
    assert not hasattr(shell_obj, '_last_command_output')
    assert shell_obj.supports_executable_pipelining is True
    assert shell_obj.supports_chained_and

# Generated at 2022-06-13 15:03:31.348626
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()

# Generated at 2022-06-13 15:03:33.041833
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()
    assert 'New-Item' in shell.mkdtemp('tmp', tmpdir='%some_tmp_path%')

# Generated at 2022-06-13 15:03:34.613839
# Unit test for constructor of class ShellModule
def test_ShellModule():
    moduleTest = ShellModule()

# Generated at 2022-06-13 15:03:43.400264
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import os
    import tempfile
    from ansible.errors import AnsibleError
    from ansible.module_utils.six import text_type
    from ansible.parsing.splitter import parse_kv
    from ansible.module_utils.common._collections_compat import Mapping

    # test a few simple options
    txt = "echo foo"
    m = ShellModule(connection='winrm')
    assert m.join_path('a', 'b') == '\\'.join(('a', 'b'))
    assert parse_kv(m.build_module_command(txt, None, None, '/some/path')) == {'cmd': 'echo foo; exit $LASTEXITCODE', '_uses_shell': True}

    # test a few simple options
    txt = "echo foo"


# Generated at 2022-06-13 15:03:51.321762
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    # construct a instance of class ShellModule
    test_shell = ShellModule()

    assert test_shell.mkdtemp() == '''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('TMP')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'ansible-tmp-XXXXXXXX'
        Write-Output -InputObject $tmp.FullName
        '''.strip()

    assert test_shell.mkdtemp(basefile='ansible-tmpdir') == '''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('TMP')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'ansible-tmpdir'
        Write-Output -InputObject $tmp.FullName
        '''.strip()

    # TODO: test the

# Generated at 2022-06-13 15:04:00.314022
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    """
    Create a directory, check that it exists and delete it
    """
    import tempfile

    def _remove_test_dir(test_dir):
        # Create a pseudo tempfile and use this to remove the test dir
        tf = tempfile.NamedTemporaryFile(dir=test_dir, delete=False)
        test_dir = ntpath.dirname(tf.name)
        tf.close()
        os.unlink(tf.name)
        os.rmdir(test_dir)

    test_file = tempfile.NamedTemporaryFile(delete=False)
    test_file.close()
    base_dir = ntpath.dirname(test_file.name)
    os.unlink(test_file.name)

    path = ShellModule(no_log=False).mkdtemp()


# Generated at 2022-06-13 15:04:02.307015
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Unit test for constructor of class ShellModule."""
    shell_module = ShellModule()
    assert len(shell_module.COMPATIBLE_SHELLS) == 0
    assert shell_module.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:04:08.206915
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule(connection='local')
    cmds = shell.mkdtemp(basefile='abc', system=True, mode=None, tmpdir=None)
    assert cmds.strip() == r'''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('$env:TEMP')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'abc'
        Write-Output -InputObject $tmp.FullName
        '''.strip()
    # Ensure the basefile is used without modification
    assert cmds.find('New-Item -Type Directory -Path $tmp_path -Name \'abc\'') > 0
    # Ensure tmpdir is expanded
    assert cmds.find('$tmp_path = [System.Environment]::ExpandEnvironmentVariables(\'$env:TEMP\')')

# Generated at 2022-06-13 15:05:25.742582
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Create a instance of ShellModule
    test_class = ShellModule()
    # Check if its type is :class 'ansible.plugins.shell.ShellModule'
    assert type(test_class) == ShellModule

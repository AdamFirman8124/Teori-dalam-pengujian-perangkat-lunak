

# Generated at 2022-06-13 14:55:41.914022
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell = ShellModule()
    assert shell.expand_user('~') == shell._encode_script("Write-Output (Get-Location).Path")
    assert shell.expand_user('foo~') == shell._encode_script("Write-Output 'foo~'")
    assert shell.expand_user('~foo') == shell._encode_script("Write-Output '~foo'")
    assert shell.expand_user('~bar') == shell._encode_script("Write-Output '~bar'")
    assert shell.expand_user('~\\') == shell._encode_script("Write-Output ((Get-Location).Path + '\\')")
    assert shell.expand_user('~\\foo') == shell._encode_script("Write-Output ((Get-Location).Path + '\\foo')")
    assert shell

# Generated at 2022-06-13 14:55:43.224113
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module != None

# Generated at 2022-06-13 14:55:54.301408
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    module = ShellModule()
    assert module.build_module_command('', None, 'Test-Module -Arg') == '& amp; {Test-Module -Arg; exit $LASTEXITCODE}'

# Generated at 2022-06-13 14:56:01.719542
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule(None)

    e = shell.build_module_command("env_string", shebang="#!powershell", cmd="cmd", arg_path="arg_path")
    assert e == "type cmd.ps1 | & '{0}'; exit $LASTEXITCODE" .format(base64.b64encode("Set-StrictMode -Version Latest\r\n\r\nIf (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }\r\n".encode('utf-16-le')).decode('utf-8'))

    e = shell.build_module_command("env_string", shebang="#!other", cmd="cmd")

# Generated at 2022-06-13 14:56:06.989559
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test with no arguments
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.CAN_DELEGATE is True
    assert shell.SHELL_NAME == 'powershell'
    assert shell.HAS_PERSISTENT_CONNECTION is False
    assert shell.DEFAULT_EXTENSION == 'ps1'
    assert shell.SHELL_TYPE == 'powershell'
    assert shell.TERM_SUPPORT_ARGS == '-NoExit'

# Generated at 2022-06-13 14:56:07.769013
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module

# Generated at 2022-06-13 14:56:16.035325
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.plugins.shell import ShellModule
    from ansible.module_utils.six import PY2
    sm = ShellModule(connection=None, shell_executable='powershell', no_log=False,
                     become_user='test_become_user', become_method='test_become_method',
                     become_exe='test_become_exe', become_flags='test_become_flags',
                     check=False, diff=False, stdin_add_newline=False, executable='test_executable',
                     remote_tmp='test_remote_tmp', remote_uid='test_remote_uid')

    if PY2:
        assert '$tmp = New-Item -Type Directory -Path $tmp_path -Name ' in sm.mkdtemp(basefile='test')

# Generated at 2022-06-13 14:56:21.774771
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(task=None, connection='ssh')
    assert module._IS_WINDOWS is True
    assert module.get_remote_filename('dummyfile') == 'dummyfile.ps1'
    assert module.join_path('foo', 'bar') == r'foo\bar'
    assert module.join_path('foo\\', 'bar') == r'foo\bar'
    assert module.join_path('foo\\', 'bar/', 'baz/') == r'foo\bar\baz'
    assert module.join_path('foo/', 'bar\\', 'baz/') == r'foo\bar\baz'
    assert module.env_prefix() == ''
    assert module.build_module_command('', '', 'powershell') == b'& amp; '
    assert module.wrap_for_exec

# Generated at 2022-06-13 14:56:25.612839
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    s = ShellModule()

    assert s.path_has_trailing_slash('/c/test\\') is True
    assert s.path_has_trailing_slash('C:\\test\\') is True
    assert s.path_has_trailing_slash('C:\\test\\foo') is False
    assert s.path_has_trailing_slash('/test/foo') is False

# Generated at 2022-06-13 14:56:33.945593
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    ShellModule._random_id = lambda: 'random'
    cmd = ShellModule(connection=None, runner=None).mkdtemp()
    assert cmd == b"Write-Output (New-Item -Type Directory -Path $env:TEMP -Name 'ansible-random').FullName"
    cmd = ShellModule(connection=None, runner=None).mkdtemp(tmpdir='/foo/')
    assert cmd == b"Write-Output (New-Item -Type Directory -Path '/foo/' -Name 'ansible-random').FullName"


# Generated at 2022-06-13 14:56:46.643711
# Unit test for constructor of class ShellModule
def test_ShellModule():
    class MyTest:
        def __init__(self):
            self.tmpdir = None
            self.remote_user = None
            self.remote_pass = None
            self.become_method = None
            self.become_user = None
            self.become_pass = None
            self.no_log = None
            self.connection = None

    options = MyTest()
    options.connection = 'smart'
    options.run_hosts = [None]
    options.become_method = 'runas'
    options.become_user = 'admin'
    sm = ShellModule(options)
    assert sm._SHELL_TYPE == 'powershell'
    #assert sm.SHELL_FAMILY == 'powershell'
    assert sm.BECOME_METHODS == ['runas']
    #assert

# Generated at 2022-06-13 14:56:48.321678
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.plugins.shell.powershell import ShellModule
    ShellModule(connection='local', no_log=True, become_method='runas', become_user='test')

# Generated at 2022-06-13 14:56:59.839574
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    powershell = ShellModule()
    assert powershell.path_has_trailing_slash('C:\\Temp\\') == True
    assert powershell.path_has_trailing_slash('C:\\Temp') == False
    assert powershell.path_has_trailing_slash('C:/Temp/') == True
    assert powershell.path_has_trailing_slash('C:/Temp') == False
    assert powershell.path_has_trailing_slash('C:\Temp/') == True
    assert powershell.path_has_trailing_slash('C:\Temp') == False
    assert powershell.path_has_trailing_slash('C:\\TEMP\\') == True
    assert powershell.path_has_trailing_slash('C:\\TEMP') == False

# Generated at 2022-06-13 14:57:03.215710
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == set()
    assert shell._IS_WINDOWS is True
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'

# Generated at 2022-06-13 14:57:08.412028
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible_collections.ansible.powershell.plugins.module_utils.connection.powershell.winrm import Connection
    from ansible_collections.ansible.powershell.plugins.module_utils.connection.psrp import Connection

    for plugin in ['winrm', 'psrp']:
        ssh = ShellModule(connection=Connection(None))
        assert ssh._IS_WINDOWS == True

# Generated at 2022-06-13 14:57:14.335513
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    import copy
    plugin = copy.deepcopy(ShellModule())
    assert plugin.get_remote_filename('test.txt') == 'test.txt'
    assert plugin.get_remote_filename('test') == 'test.ps1'
    assert plugin.get_remote_filename('test.ps1') == 'test.ps1'



# Generated at 2022-06-13 14:57:17.339851
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()
    result = shell.mkdtmp(None, False, None, None)
    # This test doesn't check the correctness of result, it's very likely
    # to fail on Windows, but we can't do better today.
    assert result is not None

# Generated at 2022-06-13 14:57:17.883173
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# Generated at 2022-06-13 14:57:21.058405
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule(connection='conn')
    assert sm.connection == 'conn'
    assert sm.no_log != ['-EncodedCommand', '-EncodedCommandByte']
    assert sm.shebang == '#!/usr/bin/env powershell'
    assert sm._SHELL_REDIRECT_ALLNULL == '> $null'

# Generated at 2022-06-13 14:57:22.129907
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell._IS_WINDOWS == True

# Generated at 2022-06-13 14:57:31.532320
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    data = ['test', 'test\\', 'test/', 'test//', 'test\\//', 'test/\\/']
    expected = [False, True, True, True, True, True]
    cmd = ShellModule()
    result = [cmd.path_has_trailing_slash(x) for x in data]
    assert result == expected



# Generated at 2022-06-13 14:57:41.597478
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    # This method is a static method, so it can be called directly
    tests = [{'in': 'C:\\temp\\test.ps1', 'out': 'test.ps1'},
             {'in': 'C:\\temp\\test.exe', 'out': 'test.exe'},
             {'in': 'C:\\temp\\test.bat', 'out': 'test.bat.ps1'},
             {'in': 'C:\\temp\\test', 'out': 'test.ps1'}
             ]
    for test in tests:
        if ShellModule.get_remote_filename(test['in']) != test['out']:
            return False

    return True

# Generated at 2022-06-13 14:57:48.564604
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # The constructor of class ShellModule() should return a instance of class
    powershell = ShellModule(connection=None, kind='powershell', add_around=None, add_before=None, add_after=None)
    assert isinstance(powershell, ShellModule)
    assert powershell.SHELL_FAMILY == 'powershell'
    assert powershell._IS_WINDOWS == True
    assert not powershell._SHELL_AND.startswith('&&')
    assert len(powershell.COMPATIBLE_SHELLS) == 0


# Generated at 2022-06-13 14:57:56.548249
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule(connection=None)

    # Test for _IS_WINDOWS
    assert shell_module._IS_WINDOWS

    # Test for COMPATIBLE_SHELLS
    assert not shell_module.COMPATIBLE_SHELLS

    # Test for _SHELL_REDIRECT_ALLNULL
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'

    # Test for _SHELL_AND
    assert shell_module._SHELL_AND == ';'

# Generated at 2022-06-13 14:58:05.417965
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    from ansible.module_utils.common.text.converters import to_bytes
    # Create a generic shell plugin
    shell = ShellModule()
    assert shell.get_remote_filename("file.py") == "file.ps1"

    assert shell.get_remote_filename("file.py.j2") == "file.py.j2.ps1"
    assert shell.get_remote_filename("file.exe") == "file.exe"
    assert shell.get_remote_filename("file.ps1") == "file.ps1"
    assert shell.get_remote_filename("file.bat") == "file.bat.ps1"
    assert shell.get_remote_filename("file.bin") == "file.bin.ps1"

# Generated at 2022-06-13 14:58:15.082176
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import tempfile
    # Create a temporary directory and specify the base file name
    base_file = tempfile.mkdtemp(prefix='base_file')
    # Create a temporary directory and specify a temporary directory
    tmp_dir = tempfile.mkdtemp(prefix='tmp_dir')
    # Create a temporary directory with default base file name and default tmp dir
    base_tmp_dir = tempfile.mkdtemp()

    assert ShellModule.mkdtemp(base_file) == 'New-Item -Type Directory -Path %s -Name \'base_file\' ; Write-Output -InputObject $tmp.FullName ; ' % base_file

# Generated at 2022-06-13 14:58:25.981916
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_plugin = ShellModule()
    shell_plugin.SHELL_FAMILY = 'powershell'

    # Test case:
    # powershell requires that script files end with .ps1, so we should do the
    # same
    pathname = 'test.py'
    assert shell_plugin.get_remote_filename(pathname) == 'test.ps1'

    # Test case:
    # powershell requires that script files end with .ps1, so we should do the
    # same
    pathname = 'test'
    assert shell_plugin.get_remote_filename(pathname) == 'test.ps1'

    # Test case:
    # We are dealing with .ps1 files and so we shouldn't change the filename
    pathname = 'test.ps1'

# Generated at 2022-06-13 14:58:34.684675
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    module = ShellModule(connection=None)

    path = 'folder\\'
    assert module.path_has_trailing_slash(path) is True

    path = 'folder'
    assert module.path_has_trailing_slash(path) is False

    path = 'folder\\subfolder\\'
    assert module.path_has_trailing_slash(path) is True

    path = 'C:\\users\\current_user\\'
    assert module.path_has_trailing_slash(path) is True

    path = '\\\\domain\\shared_folder\\'
    assert module.path_has_trailing_slash(path) is True

    # Allow forward slash
    path = '//domain/shared_folder/'
    assert module.path_has_trailing_slash(path) is True




# Generated at 2022-06-13 14:58:45.802371
# Unit test for constructor of class ShellModule
def test_ShellModule():

    # Construct a ShellModule object
    shell_mod = ShellModule()

    # Check that appropriate class variables are initialized
    assert shell_mod.COMPATIBLE_SHELLS == ShellBase.COMPATIBLE_SHELLS
    assert shell_mod.SHELL_FAMILY == 'powershell'
    assert shell_mod._IS_WINDOWS
    assert shell_mod.BINARY_MODULE_RESULT == 0
    assert shell_mod.PSCRIPT_NATIVE_RETURN == 0
    assert shell_mod.PSCP_NATIVE_RETURN == 0
    assert shell_mod.PRESERVE_WHITESPACE
    assert not shell_mod.HAS_NATIVE_SELECT
    assert shell_mod.SUPPORT_CHECKMODE


# Generated at 2022-06-13 14:58:46.902804
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule() is not None

# Generated at 2022-06-13 14:59:04.187127
# Unit test for constructor of class ShellModule

# Generated at 2022-06-13 14:59:07.293671
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    path = 'C:\\Windows\\Temp\\'

    assert(ShellModule().path_has_trailing_slash(path) == True)



# Generated at 2022-06-13 14:59:15.786908
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    # Creating a ShellModule object with self.no_log = False so that the cmd
    # created after calling path_has_trailing_slash in the test can be logged
    shell = ShellModule(None, False)
    # Test case 1
    # Testing for a path not having a trailing slash
    path_no_trailing_slash = 'C:\\Users\\Administrator'
    assert shell.path_has_trailing_slash(path_no_trailing_slash) == False
    # Test case 2
    # Testing for a path having a forward slash and a back slash at the end
    # Both the forward and back slash should be followed and considered as a
    # single trailing slash
    path_trailing_slash = 'A:\\B\\C\\D\\'

# Generated at 2022-06-13 14:59:17.637681
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell is not None

# Generated at 2022-06-13 14:59:20.986984
# Unit test for constructor of class ShellModule
def test_ShellModule():
    B = ShellModule(connection=None, become_method=None)
    assert B.cmd == "powershell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted"

# Generated at 2022-06-13 14:59:25.702702
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # TODO: mock plugins.shell.ShellBase
    base = ShellBase()

    module = ShellModule(connection=None, shell_type=base.SHELL_TYPE, no_log=False, become_method=None, become_user=None, check_rc=False, executable='powershell')
    assert hasattr(module, '_compat_module')

# Generated at 2022-06-13 14:59:27.187869
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_m = ShellModule('shell_m')
    assert isinstance(shell_m, ShellModule)


# Generated at 2022-06-13 14:59:30.730762
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test with empty params
    assert ShellModule() is not None


# ========== main ==========
if __name__ == '__main__':
    # Unit test for class ShellModule
    test_ShellModule()

# Generated at 2022-06-13 14:59:33.455394
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule().COMPATIBLE_SHELLS == frozenset()
    assert ShellModule().SHELL_FAMILY == 'powershell'
    assert ShellModule()._IS_WINDOWS == True


# Generated at 2022-06-13 14:59:36.351303
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None, new_stdin=None, prompt=None, new_stdout=None, runner=None,
                        cmd_executor=None, inventory=None, *(), **{})
    assert shell.SHELL_FAMILY is 'powershell'
    assert shell.COMPATIBLE_SHELLS is frozenset()
    assert shell._IS_WINDOWS is True

# Generated at 2022-06-13 14:59:43.389230
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm.SHELL_FAMILY == 'powershell'
    assert sm._IS_WINDOWS == True

# Generated at 2022-06-13 14:59:44.774741
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule()
    assert isinstance(m, ShellModule)



# Generated at 2022-06-13 14:59:54.581342
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    my_test_shell_module = ShellModule()
    def should_be_true(path):
        if not my_test_shell_module.path_has_trailing_slash(path):
            raise AssertionError('expected ' + path + ' to be true')

    def should_be_false(path):
        if my_test_shell_module.path_has_trailing_slash(path):
            raise AssertionError('expected ' + path + ' to be false')


# Generated at 2022-06-13 14:59:56.019241
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell is not None
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:59:57.438906
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule(connection=None)
    ShellModule(connection=None, no_log=True)


# Generated at 2022-06-13 14:59:59.601939
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    shell_module._unquote('"C:\\Program Files\\"') == 'C:\\Program Files\\'

# Generated at 2022-06-13 15:00:01.362257
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule()
    assert plugin.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:07.049897
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test 1
    shell_module = ShellModule(connection='winrm')
    # winrm connection must return powershell
    assert shell_module.SHELL_FAMILY == 'powershell'
    # Test 2
    shell_module = ShellModule(connection='ssh')
    # ssh connection must return powershell
    assert shell_module.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:09.343753
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(conn=None)

    # is_powershell is a property
    assert shell.is_powershell

    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:12.366885
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None)
    assert shell.IS_WINDOWS is True
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:00:17.922251
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    shell.join_path('a', 'b', 'c')



# Generated at 2022-06-13 15:00:29.710103
# Unit test for constructor of class ShellModule
def test_ShellModule():
    _module = type(
        'AnsibleModule',
        (object,),
        {
            'params': {
                '_ansible_shell_executable': None,
                '_ansible_shell_type': ShellModule.SHELL_FAMILY,
                '_ansible_verbosity': 4,
            },
            'log': lambda *args, **kwargs: None,
        }
    )()

    shell = ShellModule(_module)
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS is True
    assert shell._IS_POSIX is False
    assert shell.DEFAULT_EXECUTABLE == 'powershell'
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()


# Generated at 2022-06-13 15:00:31.141750
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None, tmpdir=None, task_uuid=None)

    assert type(shell) == ShellModule


# Generated at 2022-06-13 15:00:32.049793
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module is not None

# Generated at 2022-06-13 15:00:33.246850
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(None)
    shell.get_option("test")



# Generated at 2022-06-13 15:00:36.212858
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Instantiate shell module and validate its properties
    """
    shell = ShellModule()

    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'
    assert shell._IS_WINDOWS is True



# Generated at 2022-06-13 15:00:39.902455
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule()

    assert shell.path_has_trailing_slash('C:\\foo\\')
    assert shell.path_has_trailing_slash('C:\\foo\\bar\\\\')
    assert shell.path_has_trailing_slash('C:\\foo\\bar\\')
    assert not shell.path_has_trailing_slash('C:\\foo\\bar')

# Generated at 2022-06-13 15:00:43.597033
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule()
    assert len(obj.COMPATIBLE_SHELLS) == 0
    assert obj.SHELL_FAMILY == 'powershell'
    assert obj._IS_WINDOWS
    assert obj.get_remote_filename('test_file') == 'test_file.ps1'
    assert obj.env_prefix(test1='test1') == ""
    assert obj.get_option('remote_tmp') is not None


# Generated at 2022-06-13 15:00:46.790791
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.SHELL_FAMILY == 'powershell'
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm._IS_WINDOWS is True


# Generated at 2022-06-13 15:00:48.834291
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Validate that ShellModule class can be instantiated"""
    obj = ShellModule({})
    assert obj is not None

# Generated at 2022-06-13 15:00:59.624971
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None)
    assert shell != None


# Generated at 2022-06-13 15:01:01.942605
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert to_bytes('test_ShellModule') == "test_ShellModule"
    assert to_bytes('test_arne') == "test_arne"


# Generated at 2022-06-13 15:01:06.534233
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule(connection=None, add_final_comment=None)
    assert s.SHELL_FAMILY == 'powershell'
    assert s.COMPATIBLE_SHELLS == frozenset()


# Generated at 2022-06-13 15:01:13.755336
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    # pylint: disable=C0303
    shell = ShellModule(connection=None, add_ansible_module_names=False)  # type: ShellModule

    assert not shell.path_has_trailing_slash('C:\\')
    assert shell.path_has_trailing_slash('C:\\Program Files\\')
    assert shell.path_has_trailing_slash('C:\\Program Files\\\\')  # double slash
    assert not shell.path_has_trailing_slash('')
    assert shell.path_has_trailing_slash('C:\\')



# Generated at 2022-06-13 15:01:20.893338
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None, no_log=None, run_in_check_mode=None)
    assert hasattr(shell, "SHELL_FAMILY")
    assert shell.SHELL_FAMILY == 'powershell'
    assert hasattr(shell, "COMPATIBLE_SHELLS")
    assert hasattr(shell, "env_prefix")
    assert hasattr(shell, "join_path")
    assert hasattr(shell, "get_remote_filename")
    assert hasattr(shell, "path_has_trailing_slash")
    assert hasattr(shell, "chmod")
    assert hasattr(shell, "chown")
    assert hasattr(shell, "set_user_facl")
    assert hasattr(shell, "remove")

# Generated at 2022-06-13 15:01:23.403126
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_mod = ShellModule()
    assert shell_mod.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:01:24.393564
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module is not None

# Generated at 2022-06-13 15:01:24.851535
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 15:01:32.467272
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert isinstance(shell._SHELL_REDIRECT_ALLNULL, str)
    assert isinstance(shell._SHELL_AND, str)
    assert isinstance(shell._IS_WINDOWS, bool)
    assert isinstance(shell.COMPATIBLE_SHELLS, frozenset)
    assert isinstance(shell.SHELL_FAMILY, str)
    assert isinstance(shell.env_prefix(foo='bar'), str)
    assert isinstance(shell.join_path(foo='bar'), str)
    assert isinstance(shell.get_remote_filename(foo='bar'), str)
    assert isinstance(shell.path_has_trailing_slash(foo='bar'), bool)

# Generated at 2022-06-13 15:01:37.031845
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.powershell import ShellModule
    s = ShellModule(connection=None, no_log=False)
    assert s._SHELL_REDIRECT_ALLNULL == '> $null'
    assert s._SHELL_AND == ';'
    assert s._IS_WINDOWS == True

# Generated at 2022-06-13 15:01:55.303180
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'
    assert module._IS_WINDOWS is True

# Generated at 2022-06-13 15:02:01.501358
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test: Constructor
    test_ShellModule = ShellModule(connection=None, **{})
    assert test_ShellModule is not None


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 15:02:04.700782
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module._SHELL_AND == ';'


# Generated at 2022-06-13 15:02:06.155688
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(None)
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:02:13.276248
# Unit test for constructor of class ShellModule
def test_ShellModule():
    class Options():
        def __init__(self):
            self.connection = None
            self.remote_user = None
            self.become = None
            self.become_user = None
            self.verbosity = None
            self.no_log = None
            self.one_line = None

            self.module_name = None
            self.module_args = None
            self.module_vars = None
            self.module_path = None
            self.module_compression = None

            self.no_log = None

            # Shell options
            self.executable = None
            self.system_warnings = None
            self.warn = None

            self.no_log = None

            self.become_ask_pass = None
            self.become_password = None


# Generated at 2022-06-13 15:02:21.251585
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.executor.powershell as powershell
    import ansible.module_utils.powershell as powershell_utils

    # Create a new powershell executor for shell module
    shell_module_executor = powershell.ShellExecutor()

    # Create a new powershell shell module
    shell_module = ShellModule(shell_module_executor)

    # Assert that the shell family is 'powershell'
    assert shell_module.SHELL_FAMILY == 'powershell'

    # Assert that the shell_executor object is really of type powershell_utils.ShellExecutor
    assert isinstance(shell_module._shell_executor, powershell_utils.ShellExecutor)

# Generated at 2022-06-13 15:02:22.535745
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm is not None

# Generated at 2022-06-13 15:02:25.221851
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm._IS_WINDOWS is True
    assert sm.COMPATIBLE_SHELLS == set()
    assert sm.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:02:26.350976
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm is not None


# Generated at 2022-06-13 15:02:29.993866
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()

    # can't check exact values, since they're system dependent
    assert sm.remote_path is not None
    assert sm.shell_plugin is not None
    assert sm.has_pipelining is not None
    assert sm._IS_WINDOWS



# Generated at 2022-06-13 15:02:59.937873
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    class Options(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    class AnsibleModule(object):
        def __init__(self, *args, **kwargs):
            pass

        def _ansible_is_private(self):
            return None

    class ModuleDeprecationWarning(object):
        def __init__(self):
            pass

        def warn(self, *args, **kwargs):
            pass

    m = AnsibleModule(argument_spec={})

    def load_shell_plugin(cls, *args, **kwargs):
        return ShellModule(m)


# Generated at 2022-06-13 15:03:07.783463
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Create an instance that sets the name of the shell to CMD
    s = ShellModule(CMD)
    # Check the family for the shell is set as CMD
    assert s._SHELL_FAMILY == 'powershell', "SHELL_FAMILY is set to %s" % (s._SHELL_FAMILY)
    # Check the common shell names are in the COMPATIBLE_SHELLS
    assert s.COMPATIBLE_SHELLS.issubset(['powershell', 'powershell2', 'powershell3', 'powershell4', 'pwsh', 'pwsh1', 'pwsh2', 'pwsh3', 'pwsh4']),\
        "COMPATIBLE_SHELLS is set to %s" % (s.COMPATIBLE_SHELLS)
    assert s

# Generated at 2022-06-13 15:03:13.764267
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule(connection=None, add_bash=None, shell_executable=None, module_style=None, wrap_for_exec=None)
    assert isinstance(sm, ShellModule)
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm.SHELL_FAMILY == 'powershell'
    assert sm._IS_WINDOWS is True

# Generated at 2022-06-13 15:03:18.128069
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    sm = ShellModule()
    assert sm.path_has_trailing_slash("c:\\temp\\")
    assert sm.path_has_trailing_slash("c:/temp/")
    assert not sm.path_has_trailing_slash("c:\\temp")
    assert not sm.path_has_trailing_slash("c:\\temp\\foo")

# Generated at 2022-06-13 15:03:18.569791
# Unit test for constructor of class ShellModule
def test_ShellModule():
    x = ShellModule()

# Generated at 2022-06-13 15:03:22.230889
# Unit test for constructor of class ShellModule
def test_ShellModule():
    a = ShellModule()
    a.SHELL_FAMILY = 'powershell'
    assert a.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:03:31.933420
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule('winrm')
    assert sm is not None
    assert sm.SHELL_FAMILY is not None
    assert sm.COMPATIBLE_SHELLS is not None
    assert sm._IS_WINDOWS
    assert sm.DEFAULT_EXECUTABLE is None
    assert sm.HAS_TTY is True
    assert sm.CHILD_ENV is None
    assert sm.PATH_SEP == ';'
    assert sm._SHELL_REDIRECT_ALLNULL == '> $null'
    assert sm._SHELL_AND == ';'
    assert sm.DEFAULT_INVOCATION_COMMAND is None
    assert sm.PATH_SEP == ';'
    assert sm.env_prefix(prefix='FOO') == ""

# Generated at 2022-06-13 15:03:35.520084
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    Run the constructor for ShellModule which takes the option of a 'shell' argument
    and returns an instance of ShellModule class
    '''
    sm = ShellModule()

    assert isinstance(sm, ShellModule)

    assert sm.SHELL_FAMILY == 'powershell'
    assert sm.IS_WINDOWS == True
    assert sm.COMPATIBLE_SHELLS == ()

# Generated at 2022-06-13 15:03:43.943151
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    sh = ShellModule()
    assert sh.path_has_trailing_slash('foo/')
    assert sh.path_has_trailing_slash('foo\\')
    assert not sh.path_has_trailing_slash('foo')
    assert sh.path_has_trailing_slash('C:/bar/')
    assert sh.path_has_trailing_slash('C:\\bar\\')
    assert not sh.path_has_trailing_slash('C:\\bar')
    assert sh.path_has_trailing_slash('"foo/')
    assert sh.path_has_trailing_slash('"foo\\')
    assert not sh.path_has_trailing_slash('"foo"')

# Generated at 2022-06-13 15:03:52.403969
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.plugins.shell.powershell import ShellModule

    shell = ShellModule(None)
    shell.get_option = lambda opt: "/tmp/"

    env_string = shell.env_string()

    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")

    # test non-pipelining
    shebang = ''
    cmd = '"/dev/null" "{{test_file}}"'
    arg_path = 'test.bin'

# Generated at 2022-06-13 15:04:13.583434
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:04:23.096814
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import json
    import time

    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell', 'SHELL_FAMILY should be powershell'
    assert module._SHELL_REDIRECT_ALLNULL == '> $null', '_SHELL_REDIRECT_ALLNULL should be > $null'
    assert module._SHELL_AND == ';', '_SHELL_AND should be ;'
    assert module._IS_WINDOWS == True, '_IS_WINDOWS should be True'

    assert module.env_prefix() == '', 'env_prefix() should be empty'

    # join_path
    path = ntpath.join('c:\\', 'foo', 'bar', 'baz')

# Generated at 2022-06-13 15:04:24.236381
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod is not None



# Generated at 2022-06-13 15:04:34.077192
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test for powershell module when shell is set as winrm
    winrm_shell_module = ShellModule('winrm', '', 'c:\\')
    assert winrm_shell_module.SHELL_FAMILY == 'powershell'

    # Test for powershell module when shell is set as psrp
    psrp_shell_module = ShellModule('psrp', '', 'c:\\')
    assert psrp_shell_module.SHELL_FAMILY == 'powershell'

    # Test for powershell module when using ssh as the connection and with C(DefaultShell) set to PowerShell
    ssh_shell_module = ShellModule('ssh', '', 'c:\\')
    ssh_shell_module.SHELL_FAMILY = 'powershell'

# Generated at 2022-06-13 15:04:38.145726
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS


# Generated at 2022-06-13 15:04:39.170042
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert isinstance(sm, ShellBase)

# Generated at 2022-06-13 15:04:46.166116
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.executor.module_common
    import ansible.module_utils
    import ansible.plugins.connection.winrm
    import operator
    import warnings

    c = ansible.executor.module_common.complex_args()
    p = ansible.plugins.connection.winrm.Connection()
    x = ShellModule(c, p)
    assert isinstance(x.SHELL_FAMILY, str)
    assert hasattr(x, '_unquote')
    assert hasattr(x, '_escape')
    assert hasattr(x, '_encode_script')
    assert hasattr(x, 'COMPATIBLE_SHELLS')
    assert hasattr(x, 'SHELL_FAMILY')
    assert operator.eq(x.COMPATIBLE_SHELLS, frozenset())


# Generated at 2022-06-13 15:04:46.881088
# Unit test for constructor of class ShellModule
def test_ShellModule():
    result = ShellModule()
    assert result

# Generated at 2022-06-13 15:04:56.109835
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell_module = ShellModule()

# Generated at 2022-06-13 15:04:59.952151
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Unit test for ShellModule constructor
    """
    p = ShellModule()
    assert p._SHELL_REDIRECT_ALLNULL == '> $null',\
           "ShellModule constructor is not working"
    assert p._SHELL_AND == ';',\
           "ShellModule constructor is not working"
    assert p._IS_WINDOWS == True,\
           "ShellModule constructor is not working"
    return True


# Generated at 2022-06-13 14:55:36.090946
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection=None)
    assert module.SHELL_FAMILY == 'powershell'
    assert module.COMPATIBLE_SHELLS == ''
    assert module._IS_WINDOWS == True



# Generated at 2022-06-13 14:55:38.836565
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    module = ShellModule()
    assert module.get_remote_filename("C:\\windows\\temp\\testfile") == "testfile.ps1"


# Generated at 2022-06-13 14:55:49.961634
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    command = shell.build_module_command(None, '#!powershell', 'echo 1', 'C:\\Users\\username\\ansible-test\\test.ps1')

# Generated at 2022-06-13 14:55:58.920489
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    module_instance = ShellModule()
    assert module_instance._unquote(r'"C:\Users\user1\Downloads\test"') == u'C:\\Users\\user1\\Downloads\\test'  # pylint: disable=protected-access
    assert module_instance._unquote(r"'C:\Users\user1\Downloads\test'") == u'C:\\Users\\user1\\Downloads\\test'  # pylint: disable=protected-access
    assert module_instance._unquote(r'"C:\Users\user1\Downloads\test') == u'C:\\Users\\user1\\Downloads\\test'  # pylint: disable=protected-access

# Generated at 2022-06-13 14:56:07.491552
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    assert ShellModule.expand_user('', '') == ShellModule._encode_script(script="Write-Output '$env:USERPROFILE'", strict_mode=False)
    assert ShellModule.expand_user('~\\file.txt', '') == ShellModule._encode_script(script="Write-Output ((Get-Location).Path + '\\file.txt')", strict_mode=False)
    assert ShellModule.expand_user('~', '') == ShellModule._encode_script(script="Write-Output (Get-Location).Path", strict_mode=False)
    assert ShellModule.expand_user('') == ShellModule._encode_script(script="Write-Output '$env:USERPROFILE'", strict_mode=False)


# Generated at 2022-06-13 14:56:14.101560
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell_plugin = ShellModule.load_plugin('powershell')
    if shell_plugin.HAS_PYWINRM:
        shell_plugin.HAS_PYWINRM = False
    assert(
        shell_plugin.expand_user('~', 'testuser') ==
        b"[System.Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes((Get-Location).Path))"
    )
    assert(
        shell_plugin.expand_user('~\\temp', 'testuser') ==
        b"[System.Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes(((Get-Location).Path + '\\temp')))"
    )



# Generated at 2022-06-13 14:56:23.286539
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from powershell.common import PS_PERSISTENT_SESSION_KEY
    from ansible.plugins.shell import ShellBase
    from ansible.plugins.shell.powershell import ShellModule
    from ansible.plugins.connection.winrm import Connection as WinRMConnection

    kwargs = {PS_PERSISTENT_SESSION_KEY: 'asdf'}
    shell_obj = ShellModule(connection=WinRMConnection(**kwargs), **kwargs)

    # Check that shell_obj is an instance of ShellBase
    assert isinstance(shell_obj, ShellBase)

    # Check that removing of quotes works
    assert shell_obj._unquote("'foo'") == 'foo'
    assert shell_obj._unquote('foo') == 'foo'

    # Check that shell_obj.get_remote_filename returns a filename ending with

# Generated at 2022-06-13 14:56:35.430283
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager

    # create a test inventory
    host = Host('test_hostname')
    group = Group('test_group')
    group.add_host(host)

    # create a test vars
    var_manager = VariableManager()

    # create a test executor
    shell_plugin = ShellModule(None, task_executor=TaskExecutor())

    # test env_prefix
    assert shell_plugin.env_prefix() == ''

    # test join_path
    assert shell_plugin.join_path('C:\\', 'foo') == 'C:\\foo'

# Generated at 2022-06-13 14:56:37.102620
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Call the constructor
    shellModule = ShellModule()

    # Make sure we initialized the class
    assert shellModule is not None

# Generated at 2022-06-13 14:56:44.332279
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    s_mod = ShellModule()
    test_path = '~/test'
    script = s_mod.expand_user(test_path)
    script_path = 'C:/Users/tester/test'
    assert script[-len(script_path):] == script_path, "Expand user failed"
    test_path = '~\\test'
    script = s_mod.expand_user(test_path)
    assert script[-len(script_path):] == script_path, "Expand user failed"
    test_path = 'test'
    script = s_mod.expand_user(test_path)
    assert script[-len(test_path):] == test_path, "Expand user failed"

# Generated at 2022-06-13 14:57:00.437825
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Constructor of class ShellModule
    shell = ShellModule()
    # test method chmod
    shell.chmod(paths='paths', mode='mode')

    # test method chown
    shell.chown(paths='paths', user='user')

    # test method set_user_facl
    shell.set_user_facl(paths='paths', user='user', mode='mode')

    # test method remove
    shell.remove(path='path', recurse='recurse')

    # test method mkdtemp
    shell.mkdtemp(basefile='basefile', system='system', mode='mode', tmpdir='tmpdir')

    # test method expand_user
    shell.expand_user(user_home_path='user_home_path', username='username')

    # test method exists
    shell

# Generated at 2022-06-13 14:57:04.955238
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell_obj = ShellModule()

    assert shell_obj.path_has_trailing_slash('C:\\Temp') is False
    assert shell_obj.path_has_trailing_slash('C:/Temp') is False
    assert shell_obj.path_has_trailing_slash('C:\\Temp\\') is True
    assert shell_obj.path_has_trailing_slash('C:/Temp/') is True



# Generated at 2022-06-13 14:57:05.765028
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 14:57:09.357969
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule(connection='winrm')

    path = "c:\\test\\\\"
    # On windows the path could be passed using the forward slash
    assert shell.path_has_trailing_slash(path) == True



# Generated at 2022-06-13 14:57:19.355587
# Unit test for constructor of class ShellModule
def test_ShellModule():

    # test the constructor
    obj = ShellModule(None, 'git', 'ssh', 'c', 'd')

    assert obj.SHELL_FAMILY == 'powershell'
    assert obj.SHELL_TYPE == 'powershell'
    assert obj.COMPATIBLE_SHELLS == frozenset()
    assert not obj._IS_BINARY
    assert not obj._IS_PERSISTENT
    assert obj._IS_POWERSHELL
    assert not obj._IS_PYTHON
    assert obj._IS_WINDOWS
    assert obj.get_option('persistent_command_timeout') == 10
    assert obj.get_option('remote_tmp') == '$env:TEMP'
    assert obj.get_option('codec') == 'utf16le'

# Generated at 2022-06-13 14:57:20.115784
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell is not None

# Generated at 2022-06-13 14:57:24.690449
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    file_name = 'test.txt'
    assert file_name == ShellModule._get_remote_filename_ps(file_name)

    file_name = 'test.ps1'
    assert file_name == ShellModule._get_remote_filename_ps(file_name)

    file_name = 'test'
    assert file_name + '.ps1' == ShellModule._get_remote_filename_ps(file_name)

    file_name = 'test.exe'
    assert file_name == ShellModule._get_remote_filename_ps(file_name)


# Generated at 2022-06-13 14:57:30.997798
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    shell = ShellModule()
    assert shell.get_remote_filename('test_module') == 'test_module.ps1'
    assert shell.get_remote_filename('test_module.ps1') == 'test_module.ps1'
    assert shell.get_remote_filename('test_module.py') == 'test_module.py.ps1'
    assert shell.get_remote_filename('test_module.exe') == 'test_module.exe'



# Generated at 2022-06-13 14:57:34.853130
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule(connection=None)
    assert shell_obj
    assert shell_obj.SHELL_FAMILY == 'powershell'
    assert shell_obj.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 14:57:46.337861
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    mod = ShellModule(connection=None, add_command_to_executable=None, runner_path=None, runner_supports_async=None, shell_type=None)
    assert mod.get_remote_filename('hello') == 'hello'
    assert mod.get_remote_filename('hello.py') == 'hello.ps1'
    assert mod.get_remote_filename('hello.csx') == 'hello.csx'
    assert mod.get_remote_filename('hello.py.csx') == 'hello.py.csx'
    assert mod.get_remote_filename('hello.ps1') == 'hello.ps1'
    assert mod.get_remote_filename('hello.exe') == 'hello.exe'

# Generated at 2022-06-13 14:58:01.110529
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    mysm = ShellModule(None)
    # Test 1
    user_home_path = '~'
    cmd = mysm.expand_user(user_home_path)
    assert cmd == 'Write-Output (Get-Location).Path'

    # Test 2
    user_home_path = '~/test'
    cmd = mysm.expand_user(user_home_path)
    assert cmd == "Write-Output ((Get-Location).Path + '\\test')"

    # Test 3
    user_home_path = '~\\test'
    cmd = mysm.expand_user(user_home_path)
    assert cmd == "Write-Output ((Get-Location).Path + '\\test')"

    # Test 4
    user_home_path = '~/test1/test2'

# Generated at 2022-06-13 14:58:03.448701
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module.SHELL_FAMILY == 'powershell'
    assert module._IS_WINDOWS


# Generated at 2022-06-13 14:58:14.137753
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    import unittest

    # Test for `path_has_trailing_slash` without any trailing slash
    with unittest.mock.patch.object(ShellModule, '_unquote', return_value='C:\\Users\\PathName'):
        assert ShellModule().path_has_trailing_slash('C:\\Users\\PathName') is False

    # Test for `path_has_trailing_slash` with forward and back slash
    with unittest.mock.patch.object(ShellModule, '_unquote', return_value='C:\\Users\\PathName\\'):
        assert ShellModule().path_has_trailing_slash('C:\\Users\\PathName\\') is True
        assert ShellModule().path_has_trailing_slash('C:\\Users\\PathName\\') is True

   

# Generated at 2022-06-13 14:58:15.729398
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:58:19.905938
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()

    # _SHELL_AND
    assert shell._SHELL_AND == ';'

    # _SHELL_REDIRECT_ALLNULL
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'

# Generated at 2022-06-13 14:58:27.422721
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell_module = ShellModule()

    assert not shell_module.path_has_trailing_slash('C:\\Users')
    assert shell_module.path_has_trailing_slash('C:\\Users\\')
    assert shell_module.path_has_trailing_slash('/home/testuser')
    assert shell_module.path_has_trailing_slash('/home/testuser/')
    assert shell_module.path_has_trailing_slash('"C:\\Program Files"')
    assert shell_module.path_has_trailing_slash('"C:\\Program Files\\"')

# Generated at 2022-06-13 14:58:35.750182
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    powershell_instance = ShellModule(connection=None, play_context=None)
    assert not powershell_instance.path_has_trailing_slash("test")
    assert not powershell_instance.path_has_trailing_slash("test\\")
    assert not powershell_instance.path_has_trailing_slash("test/")
    assert powershell_instance.path_has_trailing_slash("test/test1\\")
    assert powershell_instance.path_has_trailing_slash("test/test1\\/")
    assert powershell_instance.path_has_trailing_slash("/test/test1/")
    assert powershell_instance.path_has_trailing_slash("\\test\\test1/\\")
    assert not powershell_instance.path_has_trailing

# Generated at 2022-06-13 14:58:46.539774
# Unit test for constructor of class ShellModule
def test_ShellModule():

    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager

    myMod = ShellModule()

    def doResults(res):
        return True

    manager = TaskQueueManager(1, '127.0.0.1')
    res = TaskResult('127.0.0.1', 'shell', 'shellmodule.py None', 0, 'Ok', '', '')
    manager._rq.put((0, doResults, res, True))
    manager._rq.put(None)
    manager._worker_threads[0].join()
    manager.wait_for_pending_results()

    print('END UNIT TEST')
    sys.exit(0)

# Generated at 2022-06-13 14:58:50.672650
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    s = ShellModule()
    assert s.expand_user('~') == b"Write-Output (Get-Location).Path"
    assert s.expand_user('~\\foo') == b"Write-Output ((Get-Location).Path + 'foo')"
    assert s.expand_user('bar') == b"Write-Output 'bar'"



# Generated at 2022-06-13 14:58:57.395984
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    # This test class will have methods that will be invoked by
    # the unit test framework to validate whether the given path
    # has a trailing slash or not.
    path1 = "C:/Windows\\"
    path2 = "C:/Windows"
    path3 = "C:/Windows/"
    path4 = "C:/Windows\\/"
    path5 = "C:/Windows\\//"
    path6 = "C:/Windows\\\\"
    path7 = "C:/Windows\\\\/"
    path8 = "C:/Windows//"
    path9 = "C:/Windows//\\"

    powershell = ShellModule(connection=None)
    assert powershell.path_has_trailing_slash(path1)
    assert not powershell.path_has_trailing_slash(path2)
    assert powershell.path_has_trailing_

# Generated at 2022-06-13 14:59:02.746044
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# Generated at 2022-06-13 14:59:04.246777
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Unit tests for the constructor of class ShellModule
    """
    print(ShellModule)
    ShellModule()

# Generated at 2022-06-13 14:59:06.605657
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert isinstance(shell, ShellModule)
    assert isinstance(shell, ShellBase)

# Generated at 2022-06-13 14:59:12.854178
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None)
    assert isinstance(shell, ShellModule)

    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS
    assert shell.EXECUTABLE == 'powershell.exe'
    assert shell.BINARY_MARKERS == tuple([])
    assert shell.HAS_ARGS_IN_BINARY is False


# Generated at 2022-06-13 14:59:14.180724
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    return shell_module

# Generated at 2022-06-13 14:59:22.632155
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = __import__("ansible.plugins.shell.powershell")
    sm = module.ShellModule(empty_socket_timeout=None,
                            keepalive=None,
                            no_log=False,
                            stdin=None,
                            stdin_add_newline=True,
                            stdout_callback=None,
                            verbosity=0,
                            module_implementation_preferences=None,
                            become_method='runas')
    assert isinstance(sm, module.ShellModule)



# Generated at 2022-06-13 14:59:27.930958
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()
    assert isinstance(s.COMPATIBLE_SHELLS, frozenset)
    assert s.SHELL_FAMILY == 'powershell'
    assert s._SHELL_REDIRECT_ALLNULL == '> $null'
    assert s._SHELL_AND == ';'
    assert s._IS_WINDOWS
    assert s.is_pipelining_enabled()
    assert s.can_control_stdin()


# Generated at 2022-06-13 14:59:37.862909
# Unit test for constructor of class ShellModule
def test_ShellModule():
    with open('test.ps1', 'w') as f:
        f.write("Write-Host 'Hello World'")

    test_module = ShellModule(connection='winrm', no_log=False,
                              become_method='runas', become_user='jsmith',
                              ansible_winrm_transport='credssp',
                              ansible_winrm_server_cert_validation='ignore',
                              ansible_winrm_kerberos_delegation=False,
                              check=False, diff=False,
                              ansible_winrm_send_cbt=True)

    # Test result of get_remote_filename

# Generated at 2022-06-13 14:59:43.480445
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''shell_windows.ps1 - test module construction'''
    import ansible.executor.powershell.shell_windows as shell_windows

    if not shell_windows.HAS_WINRM or not shell_windows.HAS_PSRP:
        raise Exception("winrm or psrp libraries are not installed")
    obj = shell_windows.ShellModule()
    assert obj is not None

# Generated at 2022-06-13 14:59:46.241920
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection=None, runner=None)
    assert module is not None and module.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 14:59:53.341412
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()

# Generated at 2022-06-13 14:59:55.194441
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Create a new ShellModule object.
    """
    ShellModule(connection=None, module_implementation_preferences=None)

# Generated at 2022-06-13 14:59:56.314726
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test created ShellModule instance
    shell = ShellModule()
    assert shell is not None

# Generated at 2022-06-13 14:59:57.717118
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'



# Generated at 2022-06-13 14:59:59.512642
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(None)
    assert module is not None, "ShellModule object was not created"

# Generated at 2022-06-13 15:00:05.382306
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # This is a test stub that just validates the constructor and does nothing else
    # It does not actually test the behavior of the class

    # Import the module so that cloud providers can be initialized and so that
    # the shell module class can be constructed
    from ansible.executor.powershell import ShellModule

    # Instantiate the shell module class
    shellModule = ShellModule()

# Generated at 2022-06-13 15:00:08.551061
# Unit test for constructor of class ShellModule
def test_ShellModule():
    CONSTANTS = [
        '''
            (Get-Command 'Get-WindowsFeature').CommandType
            ''',
    ]
    for cmd in CONSTANTS:
        shebang, env, cmd_parts, need_sh_escape, executable = ShellModule.split_command(cmd)

# Generated at 2022-06-13 15:00:10.343907
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:11.430856
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule(connection=None)

# Generated at 2022-06-13 15:00:14.343900
# Unit test for constructor of class ShellModule
def test_ShellModule():
    powershell = ShellModule()
    assert powershell.IS_WINDOWS is True
    assert set(powershell.COMPATIBLE_SHELLS) == set([])
    assert powershell.SHELL_FAMILY == 'powershell'



# Generated at 2022-06-13 15:00:27.923357
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 15:00:36.562873
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Invoke constructor
    from ansible.cli.playbook import PlaybookCLI
    from ansible.errors import AnsibleError
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.vars.manager import VariableManager

    PB = PlaybookExecutor()

    loader = DataLoader()
    playbooks = ['test_shell_plugin.yml']


# Generated at 2022-06-13 15:00:38.658694
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'
    assert shell._IS_WINDOWS

# Generated at 2022-06-13 15:00:44.705999
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import json
    import datetime

    # Escape tests
    assert ShellModule()._escape(u'foo\nbar') == u'foo\nbar'

# Generated at 2022-06-13 15:00:46.621736
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.powershell.internal.shell import ShellModule
    shell = ShellModule(None)

# Generated at 2022-06-13 15:00:48.297212
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:57.163563
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()

    # basic test, no exception should be generated
    module.get_remote_filename('/tmp/test')
    assert os.path.basename(module.get_remote_filename('/tmp/test')) == 'test.ps1'

    # make sure that the original path is unmodified
    assert module.get_remote_filename('/tmp/test') == os.path.basename(module.get_remote_filename('/tmp/test'))

    # ensure that other extensions are preserved
    assert module.get_remote_filename('/tmp/test.txt') == 'test.txt'

# Generated at 2022-06-13 15:00:59.657733
# Unit test for constructor of class ShellModule
def test_ShellModule():
    class Runner(object):
        def __init__(self):
            pass
    runner = Runner()
    shell = ShellModule(runner)
    assert shell.SHELL_FAMILY == 'powershell'



# Generated at 2022-06-13 15:01:10.530600
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.tempdir is None
    assert shell.remote_tmp == '$env:TEMP'
    assert shell.remote_uid is None
    assert shell.remote_user == '$env:USERNAME'
    assert shell.sudo_exe is None
    assert shell.sudo_flags == ['-']
    assert shell.sudo_pass is None
    assert shell.default_user == '$env:USERNAME'

    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell._IS_WINDOWS is True
    

# Generated at 2022-06-13 15:01:11.212907
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# Generated at 2022-06-13 15:01:41.315490
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None)
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:01:48.030183
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # ShellModule(conect=None, prompt=None, new_stdin=None, tmpdir=None, task_uuid=None)
    sm = ShellModule(None, None, None, None, None)
    results = sm._encode_script(cmd="Write-Output 'Hello World'")
    assert results == ' '.join(_common_args + ['-EncodedCommand', "UABvAHcAZQB0AC0ATwBiAGoAZQBjAHQAIABOAGUAdwAtAE8AYgBqAGUAYwB0AC4ARQB4AGUAcwAgAFMAdABhAHQAZQAgAFQAeQBwAGUAbgB0ACAAMgAwADEAMwA="])

# Generated at 2022-06-13 15:01:53.749099
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    sm.SHELL_FAMILY = 'powershell'
    assert sm.SHELL_FAMILY == 'powershell'
    assert not sm.COMPATIBLE_SHELLS
    assert sm._IS_WINDOWS
    assert sm._SHELL_REDIRECT_ALLNULL == '> $null'
    assert sm._SHELL_AND == ';'


# Generated at 2022-06-13 15:01:54.353592
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# Generated at 2022-06-13 15:01:55.115729
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 15:02:07.361093
# Unit test for constructor of class ShellModule
def test_ShellModule():

    sm = ShellModule()

    # Verify that these attributes are not None
    for attr in [
        "COMPATIBLE_SHELLS",
        "SHELL_FAMILY",
        "_IS_WINDOWS",
        "env_prefix",
        "join_path",
        "get_remote_filename",
        "path_has_trailing_slash",
        "chmod",
        "chown",
        "set_user_facl",
        "remove",
        "mkdtemp",
        "expand_user",
        "exists",
        "checksum",
        "build_module_command",
        "wrap_for_exec",
        "_unquote",
        "_escape",
        "_encode_script",
    ]:
        assert getattr(sm, attr) is not None

   

# Generated at 2022-06-13 15:02:11.567676
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule()
    assert shell_obj._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_obj.SHELL_FAMILY == 'powershell'
    assert 'PowerShell' in shell_obj.COMPATIBLE_SHELLS


# Generated at 2022-06-13 15:02:14.862994
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ps = ShellModule(None)
    assert ps is not None
    assert issubclass(ps.__class__, ShellBase)


# Generated at 2022-06-13 15:02:15.914932
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()


# Generated at 2022-06-13 15:02:17.923092
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule()
    assert m._SHELL_REDIRECT_ALLNULL == "> $null"
    assert m._SHELL_AND == ";"

# Generated at 2022-06-13 15:03:29.368337
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.module_utils.common.removed import removed_module
    # Unit test for constructor of class ShellModule
    shell = ShellModule()
    assert shell is not None
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert getattr(shell, '_IS_WINDOWS', None) in [True, None]
    assert hasattr(shell, 'env_prefix')
    assert hasattr(shell, 'join_path')
    assert hasattr(shell, 'get_remote_filename')
    assert hasattr(shell, 'path_has_trailing_slash')
    assert hasattr(shell, 'chmod')
    assert hasattr(shell, 'chown')
    assert hasattr(shell, 'set_user_facl')


# Generated at 2022-06-13 15:03:32.937177
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    test_data = {
        'Plugins.get_plugin_shell_class': 'ShellModule'
    }
    assert sm.get_option('Plugins.get_plugin_shell_class') == test_data['Plugins.get_plugin_shell_class']


# Generated at 2022-06-13 15:03:38.130169
# Unit test for constructor of class ShellModule
def test_ShellModule():

    # Setup the test environment
    class ShellModuleNoOverwrite(ShellModule):
        pass

    # Execute the constructor and check the result
    shell_module = ShellModuleNoOverwrite(connection=None)

    # Common shell filenames that this plugin handles
    # Powershell is handled differently.  It's selected when winrm is the
    # connection
    assert shell_module.COMPATIBLE_SHELLS == frozenset()

    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_module._SHELL_AND == ';'
    assert shell_module._IS_WINDOWS is True

# Generated at 2022-06-13 15:03:43.201483
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    # Check parameters relating to the powershell shell
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm.SHELL_FAMILY == 'powershell'
    assert sm._IS_WINDOWS == True
    # Check parameters relating to the module
    assert sm._SHELL_AND == ';'
    assert sm._SHELL_REDIRECT_ALLNULL == '> $null'

# Generated at 2022-06-13 15:03:44.323613
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule() != None


# Generated at 2022-06-13 15:03:45.398373
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule()


# Generated at 2022-06-13 15:03:46.888304
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.plugins.shell.powershell import ShellModule
    shell = ShellModule()
    assert shell is not None

# Generated at 2022-06-13 15:03:47.630008
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule is not None

# Generated at 2022-06-13 15:03:56.812403
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Create Powershell object."""

# Generated at 2022-06-13 15:04:04.408105
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()

    # there are no shell file extensions associated with powershell
    assert s.SHELL_FAMILY == 'powershell'
    assert s.COMPATIBLE_SHELLS == set()

    # Should be Windows only
    assert s._IS_WINDOWS

    # Should return 'ps1'
    assert s.get_remote_filename('/path/foo') == 'foo.ps1'
    assert s.get_remote_filename('/path/foo.ps1') == 'foo.ps1'

    # Trailing slash handling
    assert not s.path_has_trailing_slash('"path"')
    assert s.path_has_trailing_slash('"path\\"')
    assert s.path_has_trailing_slash('"path/"')
    assert not s.path_has

# Generated at 2022-06-13 15:05:09.851771
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module is not None

# Generated at 2022-06-13 15:05:10.574071
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 15:05:15.932180
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_args = {
        'binary': "/usr/bin/ansible",
        '_ansible_version': "2.9.9",
        '_ansible_module_name': "shell",
        '_ansible_debug': True
    }

    powershell = ShellModule(shell_args=shell_args)
    assert powershell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:05:19.286183
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None)
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:05:23.262939
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # pylint: disable=unused-argument
    ShellModule(command_string=u'cmd', runner_on_failed=None, runner_on_ok=None)
    ShellModule(command_string=u'cmd', runner_on_failed=None, runner_on_ok=None, runner_on_unreachable=None, runner_on_skipped=None)
    # pylint: enable=unused-argument


# Generated at 2022-06-13 15:05:27.297376
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    This is a dummy unit test for the ShellModule constructor
    """
    options = get_config()
    options.become = None
    options.become_method = None
    options.become_user = None
    response = ShellModule(None, **options)
    assert response is not None

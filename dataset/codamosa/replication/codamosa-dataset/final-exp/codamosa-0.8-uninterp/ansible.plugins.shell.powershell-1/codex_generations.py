

# Generated at 2022-06-13 14:55:43.042046
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    args = {}
    args['shebang'] = '#!powershell'
    args['_is_pipelining'] = False
    args['_ansible_debug'] = False
    args['_ansible_verbosity'] = 1
    args['_ansible_no_log'] = False
    args['_ansible_version'] = '2.10.3'
    args['_ansible_diff'] = False
    args['_ansible_module_name'] = 'shell'
    args['_ansible_module_name'] = 'shell'
    args['_ansible_module_name'] = 'shell'
    args['_ansible_module_name'] = 'shell'
    args['_ansible_module_name'] = 'shell'
    args['_ansible_module_name'] = 'shell'
    args

# Generated at 2022-06-13 14:55:47.283832
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()
    assert s.COMPATIBLE_SHELLS == frozenset()
    assert s.SHELL_FAMILY == 'powershell'
    assert s._IS_WINDOWS is True



# Generated at 2022-06-13 14:55:53.597053
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    assert ShellModule().get_remote_filename('helloworld') == 'helloworld.ps1'
    assert ShellModule().get_remote_filename('helloworld.ps1') == 'helloworld.ps1'
    assert ShellModule().get_remote_filename('helloworld.py') == 'helloworld.py.ps1'
    assert ShellModule().get_remote_filename('helloworld.exe') == 'helloworld.exe'


# Generated at 2022-06-13 14:55:54.836051
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()._IS_WINDOWS == True

# Generated at 2022-06-13 14:56:02.935249
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    shell_module.set_options(
        become_method=None,
        become_user=None,
        become_pass=None,
        become_exe='',
        become_flags='',
        become_info=dict(),
        no_log=False,
        remote_tmp='',
        remote_uid='',
        remote_user='',
        transport=None,
        verbosity=0,
        module_vars=dict(),
        task_vars=dict(),
        global_vars=dict(),
        password='',
        prompt='',
        response='',
    )

# Generated at 2022-06-13 14:56:04.580814
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.SHELL_FAMILY == 'powershell'
    assert sm._IS_WINDOWS is True

# Generated at 2022-06-13 14:56:05.820968
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule(*_common_args)
    assert shell_module != None



# Generated at 2022-06-13 14:56:12.682866
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.executor.powershell import ShellModule
    from ansible.module_utils._text import to_text

    shell = ShellModule()

    # pipelining bypass
    cmd = ''
    shebang = '#!powershell'
    env_string = '$env:ANSIBLE_MODULE_ARGS = "{\\"ANSIBLE_MODULE_ARGS\\":{\\"foo\\":\\"bar\\"}}"'
    cmd = shell.build_module_command(env_string, shebang, cmd)
    assert isinstance(cmd, str)

    # Script module - non-pipelining

# Generated at 2022-06-13 14:56:13.339032
# Unit test for constructor of class ShellModule
def test_ShellModule():
    pass

# Generated at 2022-06-13 14:56:18.478972
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule()

    expected_attributes = [
        '_SHELL_REDIRECT_ALLNULL',
        '_SHELL_AND',
        '_IS_WINDOWS',
        'SHELL_FAMILY',
        'COMPATIBLE_SHELLS'
    ]

    for expected_attribute in expected_attributes:
        assert hasattr(m, expected_attribute)

# Generated at 2022-06-13 14:56:29.473579
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule('winrm')
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell._IS_WINDOWS == True
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'

# Generated at 2022-06-13 14:56:33.529832
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_mock = ShellModule()
    assert shell_mock.COMPATIBLE_SHELLS == frozenset()
    assert shell_mock.SHELL_FAMILY == 'powershell'
    assert shell_mock._IS_WINDOWS is True



# Generated at 2022-06-13 14:56:42.170015
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    class FakeModule:
        def __init__(self):
            self.args = {}
        def fail_json(self, *args, **kwargs):
            self.fail_args = args
            self.fail_kwargs = kwargs


# Generated at 2022-06-13 14:56:44.566460
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    Test to check that we can create an instance of ShellModule
    '''
    module = ShellModule()
    assert module is not None

# Generated at 2022-06-13 14:56:47.497821
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell._IS_WINDOWS == True
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 14:56:52.483705
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod.SHELL_FAMILY == 'powershell'
    assert mod._SHELL_REDIRECT_ALLNULL == '> $null'


# Generated at 2022-06-13 14:57:02.205097
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    powershell_shell = ShellModule()
    assert (powershell_shell.path_has_trailing_slash(r"C:\Windows")) == False

# Generated at 2022-06-13 14:57:09.042425
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()

    #
    # Check ShellModule.COMPATIBLE_SHELLS
    #
    assert shell_module.COMPATIBLE_SHELLS == frozenset()

    #
    # Check ShellModule.SHELL_FAMILY
    #
    assert shell_module.SHELL_FAMILY == 'powershell'

    #
    # Check ShellModule._IS_WINDOWS
    #
    assert shell_module._IS_WINDOWS == True

    #
    # Check ShellModule.env_prefix()
    #
    assert shell_module.env_prefix() == ""

    #
    # Check ShellModule.join_path()
    #
    assert shell_module._IS_WINDOWS == True
    assert shell_module.join_path(r"\\server\share") == r"\\server\share"

# Generated at 2022-06-13 14:57:19.103432
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()

    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell._IS_WINDOWS is True
    assert shell._SHELL_AND == ';'
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'

# Generated at 2022-06-13 14:57:25.400436
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()

# Generated at 2022-06-13 14:57:34.344412
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule()
    paths = [
        ('hello/', True),
        ('hello\\', True),
        ('hello\\/', False),
        ('hello/\\', False),
        ('hello//', True),
        ('hello\\\\', True),
        ('hello\\\\\\', False),
        ('hello//\\', False),
    ]
    for (path, expected_result) in paths:
        assert shell.path_has_trailing_slash(path) == expected_result

# Generated at 2022-06-13 14:57:36.157482
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule().__class__.__name__ == 'ShellModule'

# Generated at 2022-06-13 14:57:38.006939
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert 'true' == ShellModule()('echo true').strip()

# Generated at 2022-06-13 14:57:39.264663
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sh = ShellModule('')
    assert sh.shell

# Generated at 2022-06-13 14:57:49.827235
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    module = ShellModule()
    cmd = module.build_module_command("", "", "Test-Command", arg_path="Test-Path")


# Generated at 2022-06-13 14:57:51.868813
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:58:02.189336
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_mod = ShellModule()
    assert shell_mod is not None
    assert shell_mod.get_remote_filename("/path/to/a/filename") == "filename"
    assert shell_mod.get_remote_filename("/path/to/a/filename.exe") == "filename.exe"
    assert shell_mod.get_remote_filename("/path/to/a/filename.sh") == "filename.sh"
    assert shell_mod.get_remote_filename("/path/to/a/filename.ps1") == "filename.ps1"
    assert shell_mod.join_path("a") == "a"
    assert shell_mod.join_path("a", "b") == "a\\b"

# Generated at 2022-06-13 14:58:09.363949
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.executor.powershell.psexec_wrapper import PsexecWrapper
    from ansible.executor.powershell.runas_wrapper import RunasWrapper
    from ansible.executor.psrp.psrp_wrapper import PsRpWrapper
    from ansible.executor.psrp.runas_wrapper import PsRpRunasWrapper
    from ansible.executor.winrm.runas_wrapper import WinrmRunasWrapper
    from ansible.executor.winrm.winrm_wrapper import WinrmWrapper

    class MockConfig:
        def __init__(self):
            self.connection = 'winrm'
            self.become_method = 'runas'

    config = MockConfig()

    mock_psexec_wrapper = PsexecWrapper()
   

# Generated at 2022-06-13 14:58:13.276920
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()._IS_WINDOWS is True, "_IS_WINDOWS should be True for all Windows shells"
    assert ShellModule().COMPATIBLE_SHELLS == frozenset(), "COMPATIBLE_SHELLS should be frozenset() for all Windows shells"
    assert ShellModule().SHELL_FAMILY == 'powershell', "SHELL_FAMILY should be 'powershell'"

# Generated at 2022-06-13 14:58:23.710920
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # explicitly set connection_type
    connection_type = 'winrm'

    # import class for testing
    from ansible.plugins.shell import ShellModule

    # create instance of ShellModule
    shell = ShellModule()

    # check the code path for 'winrm' connection_type
    shell.set_options(connection=connection_type)

    # set some options
    shell.set_options(become=False, become_method='sudo', become_user='root', module_path=['/some/path/modules/'])

    # check return values
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell._IS_WINDOWS

# Generated at 2022-06-13 14:58:31.484057
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_module._SHELL_AND == ';'
    assert shell_module.COMPATIBLE_SHELLS == frozenset()
    assert shell_module.SHELL_FAMILY == 'powershell'
    assert shell_module._IS_WINDOWS == True



# Generated at 2022-06-13 14:58:32.090785
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 14:58:39.556704
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import ansible.executor.powershell.module_common as mc

    SM = ShellModule()

    # If a module is a binary executable, then the arguments must be
    # passed in quotes or the command fails
    assert SM.build_module_command(None, "#!bin", "./bin module", "args") ==\
        SM.wrap_for_exec(SM._encode_script('"%s" "%s"' % (mc.MODULE_COMPLEX_ARGS, "args")))

    # If a module is a binary executable and has no argument, then the
    # arguments must be passed in quotes or the command fails

# Generated at 2022-06-13 14:58:50.196757
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    assert ShellModule().expand_user('~') == ShellModule()._encode_script('Write-Output (Get-Location).Path')
    assert ShellModule().expand_user('~\\') == ShellModule()._encode_script('Write-Output ((Get-Location).Path + \'\\\\\')')
    assert ShellModule().expand_user('~\\foo bar.jpeg') == ShellModule()._encode_script('Write-Output ((Get-Location).Path + \'\\\\foo bar.jpeg\')')
    assert ShellModule().expand_user('~foo') == ShellModule()._encode_script('Write-Output \'~foo\'')
    assert ShellModule().expand_user('~foo bar.jpeg') == ShellModule()._encode_script('Write-Output \'~foo bar.jpeg\'')

# Generated at 2022-06-13 14:58:51.595986
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # test ShellModule class constructor with no arguments
    # TODO: test that it can be created with no arguments
    ShellModule()



# Generated at 2022-06-13 14:58:52.664297
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:59:00.163745
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell = ShellModule(connection=None)
    assert shell.expand_user(user_home_path="~", username='') == shell._encode_script("Write-Output (Get-Location).Path")
    assert shell.expand_user(user_home_path="~\\file", username='') == shell._encode_script("Write-Output ((Get-Location).Path + '\\\\file')")
    assert shell.expand_user(user_home_path="path", username='') == shell._encode_script("Write-Output 'path'")



# Generated at 2022-06-13 14:59:04.187314
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule()
    path1 = """Z:\\test\\test_hello\\test.py"""
    path2 = """Z:/test/test_hello/test.py"""
    assert shell.path_has_trailing_slash(path1) == False
    assert shell.path_has_trailing_slash(path2) == False



# Generated at 2022-06-13 14:59:06.499553
# Unit test for constructor of class ShellModule
def test_ShellModule():
    executable = 'PowerShell'
    plugin = ShellModule(executable)
    assert plugin.executable == executable

# Generated at 2022-06-13 14:59:09.284228
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """shell_windows.py ShellModule() Constructor Unit Test"""
    obj = ShellModule()
    assert obj
    assert isinstance(obj, ShellBase)


# Generated at 2022-06-13 14:59:24.945761
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell_module = ShellModule()
    assert shell_module.path_has_trailing_slash('C:\\') is True
    assert shell_module.path_has_trailing_slash('C:\\test\\') is True
    assert shell_module.path_has_trailing_slash('C:\\test') is False
    assert shell_module.path_has_trailing_slash('C:') is False
    assert shell_module.path_has_trailing_slash('\\\\share\\test') is False
    assert shell_module.path_has_trailing_slash('\\\\share\\test\\') is True
    assert shell_module.path_has_trailing_slash('\\\\share') is True
    assert shell_module.path_has_trailing_slash('\\\\share\\') is True

# Generated at 2022-06-13 14:59:27.423412
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Unit test for constructor of class ShellModule"""

    assert ShellModule()._SHELL_REDIRECT_ALLNULL == "> $null"
    assert ShellModule()._SHELL_AND == ";"
    assert ShellModule()._IS_WINDOWS
    assert ShellModule().COMPATIBLE_SHELLS == frozenset()
    assert ShellModule().SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:59:31.759690
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule()
    assert obj.COMPATIBLE_SHELLS == frozenset()
    assert obj._SHELL_REDIRECT_ALLNULL == '> $null'
    assert obj._SHELL_AND == ';'
    assert obj._IS_WINDOWS

# Generated at 2022-06-13 14:59:33.590719
# Unit test for constructor of class ShellModule
def test_ShellModule():

    # Create the object ShellModule
    powershell = ShellModule()

    # Check if the ShellModule is created successfully
    if not powershell:
        raise Exception("Failed to create ShellModule")
    return True


# Generated at 2022-06-13 14:59:35.489430
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module is not None
    print('test_ShellModule: SUCCESS')


# Generated at 2022-06-13 14:59:46.518121
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # set up a temp dir to put the files in
    import tempfile
    tmpdir = tempfile.mkdtemp()
    test_files_path = os.path.join(os.path.dirname(__file__), 'testdata', 'test_files')
    args_path = os.path.join(test_files_path, 'args')
    args = pkgutil.get_data('ansible.executor.powershell', 'args.ps1')
    with open(args_path, "wb") as f:
        f.write(args)

    # create a fake module
    module_path = os.path.join(tmpdir, 'testmodule.py')

# Generated at 2022-06-13 14:59:48.560061
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule()
    assert m._shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:59:58.040585
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    s = ShellModule()

    # forward and backslashed paths
    assert s.path_has_trailing_slash('"\\\\server\\share\\"')
    assert s.path_has_trailing_slash('"\\\\server\\share\\path\\"')
    assert s.path_has_trailing_slash('"\\\\server\\share\\path\\"')
    assert s.path_has_trailing_slash('"\\\\server\\share\\path"')
    assert s.path_has_trailing_slash(r'"\\server\share\"')
    assert s.path_has_trailing_slash(r'"\\server\share\path\"')
    assert s.path_has_trailing_slash(r'"\\server\share\path\"')
    assert s.path_has_trailing_slash

# Generated at 2022-06-13 15:00:06.938411
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell_mod = ShellModule()
    assert shell_mod.path_has_trailing_slash("/tmp/foo")
    assert shell_mod.path_has_trailing_slash("\\tmp\\foo")
    assert not shell_mod.path_has_trailing_slash("/tmp/foo/")
    assert not shell_mod.path_has_trailing_slash("\\tmp\\foo\\")
    assert not shell_mod.path_has_trailing_slash("/tmp/foo\\")
    assert not shell_mod.path_has_trailing_slash("\\tmp\\foo/")

# Generated at 2022-06-13 15:00:07.910457
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module is not None

# Generated at 2022-06-13 15:00:14.658736
# Unit test for constructor of class ShellModule
def test_ShellModule():
    psm = ShellModule()
    assert psm.SHELL_FAMILY == 'powershell'
    assert not psm.COMPATIBLE_SHELLS

# Generated at 2022-06-13 15:00:16.824635
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell is not None
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:22.692104
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule(None)

# Generated at 2022-06-13 15:00:25.923414
# Unit test for constructor of class ShellModule
def test_ShellModule():

    powershell = ShellModule(connection=None, shell=None, no_log=False,
                             _ansible_debug=False)
    assert powershell is not None

# Generated at 2022-06-13 15:00:35.214598
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # Note: the shebang-line will be part of the command, and needs to match with the shell used
    # Note: the test produces a command which doens't do anything, just to make it self-contained
    # Note: to be called with pytest -s
    module_cmd = """
#!python
print('Hello World')
"""
    binary_cmd = """
#!powershell
$cmd = $env:ComSpec
& $cmd /c echo 'Hello World'
"""
    shell = ShellModule(connection=None, shell_type='powershell')
    for cmd in [module_cmd, binary_cmd]:
        cmd = shell.build_module_command('', '', cmd, '/bin/foo')
        print("Final command:" + cmd)
        print("Run the following command, should print '0' (success)")
        print

# Generated at 2022-06-13 15:00:38.927846
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    for path in ['/var/lib/lorax', '/var/lib/lorax/', '\\var\\lib\\lorax', '\\var\\lib\\lorax\\']:
        assert ShellModule().path_has_trailing_slash(path) == True
    for path in ['var/lib/lorax', 'var/lib/lorax/', 'var\\lib\\lorax', 'var\\lib\\lorax\\']:
        assert ShellModule().path_has_trailing_slash(path) == False


# Generated at 2022-06-13 15:00:41.975673
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.plugins.connection.winrm import Connection
    from ansible.module_utils.powershell import Powershell

    manager = Connection(Powershell())
    assert isinstance(manager, ShellModule)
    assert manager.COMPATIBLE_SHELLS == frozenset(['cmd', 'ps'])
    assert manager.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:51.544401
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import ansible.executor.powershell
    import tempfile
    import os
    import textwrap
    import shutil

    # create temporary directory
    tmp_dir = tempfile.mkdtemp()
    # create temporary script
    tmp_filename = os.path.join(tmp_dir, 'test_file.ps1')
    with open(tmp_filename, 'w') as f:
        f.write("Write-Output 'test_output'")

    # test with a PowerShell script without shebang
    shell_module = ShellModule()
    script = shell_module.build_module_command('', '', "%s\n" % tmp_filename)
    # decode script
    script = script.decode('utf-8')
    # remove temp file
    os.remove(tmp_filename)

# Generated at 2022-06-13 15:00:52.861515
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # TODO: create tests
    pass

# Generated at 2022-06-13 15:01:01.908340
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    f = ShellModule(None)
    # no shebang, no quotes
    assert f.build_module_command(env_string="", shebang="", cmd="echo hello", arg_path=None) == '& echo hello; exit $LASTEXITCODE'
    # shebang needs quotes
    assert f.build_module_command(env_string="", shebang="#!/bin/bash", cmd="echo hello", arg_path=None) == '& "/bin/bash" echo hello; exit $LASTEXITCODE'
    # shebang needs quotes

# Generated at 2022-06-13 15:01:15.566053
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule(command_timeout=1)

    # Test that a module written in PowerShell is passed to the bootstrap script
    shebang, cmd, _ = shell.build_module_command('', shebang='#!powershell',
                                                 cmd='Test-Module.ps1 arg1 arg2', arg_path='arg_path')
    assert shebang == ''
    assert cmd == 'type Test-Module.ps1 | & ansible-powershell-shell -i; exit $LASTEXITCODE'

    # Test that a module written in another shell language is not passed to the bootstrap script
    shebang, cmd, _ = shell.build_module_command('', shebang='#!/bin/bash',
                                                 cmd='Test-Module.sh arg1 arg2', arg_path='arg_path')
    assert shebang == ''

# Generated at 2022-06-13 15:01:17.469185
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:01:28.355968
# Unit test for constructor of class ShellModule
def test_ShellModule():
    cmd = ShellModule()
    assert (cmd)
    assert (cmd.SHELL_FAMILY == 'powershell')
    assert ('#!powershell' in cmd._build_shebang(None, True))
    assert (cmd.build_module_command(None, None, None, None) != '')
    assert (cmd.build_module_command(None, '#!powershell', '', None) != '')
    assert (cmd.build_module_command(None, '#foo', None, None) != '')
    assert ("Remove-Item" in cmd.remove('foo', False))
    assert ("Remove-Item" in cmd.remove('foo', True))
    assert ("-EncodedCommand" in cmd._encode_script('foo'))

# Generated at 2022-06-13 15:01:29.983740
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:01:33.821580
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.plugins.connection.windows.winrm import Connection as WinRMConnection

    conn = WinRMConnection(host='localhost')
    conn._shell = ShellModule(conn._play_context, conn)

    assert conn._shell is not None

# Generated at 2022-06-13 15:01:38.911920
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sh = ShellModule()
    assert(sh is not None)
    assert(sh.COMPATIBLE_SHELLS == frozenset())
    assert(sh._SHELL_REDIRECT_ALLNULL == '> $null')
    assert(sh._SHELL_AND == ';')
    assert(sh._IS_WINDOWS == True)


# Generated at 2022-06-13 15:01:43.224415
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule(connection=None, runner_path=None, command=None, magic_variables=[],
                     module_args=None, become_method=None, become_user=None, become_password=None,
                     become_exe=None, become_flags=None, become_ask_pass=None, stdin=None, stdout_callback=None,
                     stderr_callback=None, connect_timeout=None, shell=None, no_log=False, keep_remote_files=False,
                     host=None, script_args=None)



# Generated at 2022-06-13 15:01:44.087666
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm is not None


# Generated at 2022-06-13 15:01:44.703978
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    pass

# Generated at 2022-06-13 15:01:49.569815
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.plugins.connection.winrm
    connection = ansible.plugins.connection.winrm.Connection()
    connection.play_context = object()
    ps = ShellModule(connection)
    assert ps.connection is connection
    assert ps.play_context is connection.play_context

# Generated at 2022-06-13 15:02:00.435003
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test the ShellModule constructor
    ShellModule()

# Generated at 2022-06-13 15:02:00.998914
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# Generated at 2022-06-13 15:02:02.237880
# Unit test for constructor of class ShellModule
def test_ShellModule():
    powershell = ShellModule()
    assert powershell is not None



# Generated at 2022-06-13 15:02:10.024318
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import json
    import sys

    if sys.version_info >= (3,):
        from io import StringIO
    else:
        from StringIO import StringIO

    class Options():
        def __init__(self):
            self.connection = 'local'
            self.remote_user = 'devops'
            self.become = False
            self.become_user = 'root'
            self.verbosity = 0
            self.module_path = ''
            self.forks = 5
            self.become_method = 'sudo'
            self.check = False
            self.private_key_file = '/dev/null'
            self.listhosts = None
            self.diff = False
            self.host_key_checking = False
            self.timeout = 10

# Generated at 2022-06-13 15:02:14.997764
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()
    assert s.SHELL_FAMILY == 'powershell'
    assert s.COMPATIBLE_SHELLS == set()
    assert s._IS_WINDOWS == True


# Generated at 2022-06-13 15:02:15.950528
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 15:02:24.218810
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():

    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")

    # call under test
    shell_mod = ShellModule()

    # pipelining bypass
    env_string = "FOO='x' BAR='y'"
    shebang = '#!/usr/bin/env pwsh'
    cmd = ''
    result = shell_mod.build_module_command(env_string, shebang, cmd)

    expected = bootstrap_wrapper
    assert result == expected

    # non-pipelining

    # module name
    env_string = "FOO='x' BAR='y'"
    shebang = '#!powershell'
    cmd = 'module_name'

# Generated at 2022-06-13 15:02:26.001708
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Instantiate the class and verify it
    """
    result = ShellModule()
    assert result

# Generated at 2022-06-13 15:02:28.518071
# Unit test for constructor of class ShellModule
def test_ShellModule():
    c = ShellModule()
    assert c.COMPATIBLE_SHELLS == frozenset()
    assert c.SHELL_FAMILY == 'powershell'
    assert c._IS_WINDOWS
    assert c.SHELL_TYPE == 'powershell'

# Generated at 2022-06-13 15:02:36.151612
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.powershell import ShellModule

    shebang_config = dict(ansible_shebang=u'#!powershell')
    env_config = dict(ansible_env=dict(PATH=u'/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games'))

    print('Testing ShellModule.__init__')

# Generated at 2022-06-13 15:02:50.501630
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module.SHELL_FAMILY == 'powershell'
    assert module._IS_WINDOWS == True


# Generated at 2022-06-13 15:03:00.397828
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.utils.display import Display
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.errors import AnsibleError
    from ansible.plugins.connection.cache import ConnectionCache
    from ansible.plugins.connection.winrm import Connection as Winrm_Connection
    from ansible.plugins.shell.powershell import ShellModule
    try:
        display = Display()
        tqm = None
        connection = Winrm_Connection(play_context=None, new_stdin=None)
        connection_cache = ConnectionCache(display, tqm)
        connection_cache.connections[connection._play_context.remote_addr] = connection
        ShellModule(connection, display)
    except Exception as ex:
        raise AnsibleError('Failed instantiating module class: %s' % ex)

# Generated at 2022-06-13 15:03:04.390158
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule()
    # Test cases
    assert shell.path_has_trailing_slash('"C:\\Users\\"')
    assert shell.path_has_trailing_slash('C:\\Users\\')
    assert not shell.path_has_trailing_slash('"C:\\Users"')


# Generated at 2022-06-13 15:03:07.529721
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test with a shell_type of 'powershell' to ensure the constructor does not raise an Exception
    shell_plugin = ShellModule.load_plugin('powershell')
    assert shell_plugin._SHELL_FAMILY == 'powershell'
    assert shell_plugin._IS_WINDOWS
    assert shell_plugin.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:03:12.310344
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell_obj = ShellModule()
    assert shell_obj.path_has_trailing_slash("/foo/bar") == False
    assert shell_obj.path_has_trailing_slash("/foo/bar/") == True

# Generated at 2022-06-13 15:03:13.631164
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert isinstance(module, ShellModule)



# Generated at 2022-06-13 15:03:21.525679
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():

    from ansible.plugins.shell import ShellModule

    shell = ShellModule()

    # test for trailing slash in windows paths

# Generated at 2022-06-13 15:03:24.707526
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection=None, shell_type=None)
    assert module.SHELL_FAMILY == "powershell"
    assert module.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:03:25.918321
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # pylint: disable=protected-access
    shell = ShellModule()
    assert shell._encode_script('Write-Output 123')

# Generated at 2022-06-13 15:03:28.358714
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection='winrm')
    assert shell.connection == 'winrm'
    assert shell.SHELL_FAMILY == 'powershell'



# Generated at 2022-06-13 15:03:40.863527
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connector=None)
    str(module)


# Generated at 2022-06-13 15:03:42.707551
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module == ShellModule()
    shell_module.noop('foo')

# Generated at 2022-06-13 15:03:46.319599
# Unit test for constructor of class ShellModule
def test_ShellModule():
    if os.name != 'nt':
        pytest.skip("Can't run test_ShellModule on a non-Windows system")

    m = ShellModule()

    assert m.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:03:47.348769
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module is not None

# Generated at 2022-06-13 15:03:50.464734
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_NAME == 'powershell'
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module.SHELL_FAMILY == 'powershell'
    assert module._IS_WINDOWS



# Generated at 2022-06-13 15:03:53.271600
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY is 'powershell'
    assert shell.COMPATIBLE_SHELLS is frozenset()
    return shell

# Generated at 2022-06-13 15:03:55.329753
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    Unit test for constructor of class ShellModule
    '''
    shell_module = ShellModule()


# Generated at 2022-06-13 15:04:03.319287
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule()
    data1 = b'#< CLIXML\r\n<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04">\r\n  <S S="Error">test</S>\r\n</Objs>\r\n'

# Generated at 2022-06-13 15:04:04.063924
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell is not None

# Generated at 2022-06-13 15:04:06.066363
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Unit test for constructor of class ShellModule"""
    # create instance of ShellModule class
    x = ShellModule()
    # testing __init__ for the class
    assert isinstance(x, ShellModule)

# Generated at 2022-06-13 15:04:38.533882
# Unit test for constructor of class ShellModule
def test_ShellModule():
    s = ShellModule()
    assert s._SHELL_REDIRECT_ALLNULL == '> $null', 'Redirect to null is not assigned'
    assert s._SHELL_AND == ';', 'And is not assigned correctly'
    assert s.COMPATIBLE_SHELLS == frozenset(), 'COMPATIBLE_SHELLS is not assigned correctly'
    assert s.SHELL_FAMILY == 'powershell', 'SHELL_FAMILY is not assigned correctly'
    assert s._IS_WINDOWS == True, '_IS_WINDOWS is not assigned correctly'

# Generated at 2022-06-13 15:04:45.654367
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import sys
    import os
    from ansible.errors import AnsibleError
    from ansible.parsing.splitter import parse_kv

    # Get windows powershell path
    powershell_path = None
    for path in os.environ["PATH"].split(os.pathsep):
        path = path.strip('"')
        exe_file = os.path.join(path, 'powershell.exe')
        if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
            powershell_path = exe_file
            break

    # Find location of ansible.executor.powershell module

# Generated at 2022-06-13 15:04:46.268539
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 15:04:55.788053
# Unit test for constructor of class ShellModule
def test_ShellModule():
    conn = ShellModule()
    conn._load_name = 'windows'
    conn.get_option = Mock()
    conn.get_option.return_value = '/cygdrive/c/WINDOWS/TEMP'
    conn._ps_version = (1, 0)
    conn.get_remote_filename = Mock()
    conn.get_remote_filename.return_value = 'foo.sh'

    # Constructor for shell plugin.
    conn.get_option.assert_called_with('remote_tmp')
    conn.get_remote_filename.assert_called_with('foo.sh')
    assert conn._local_tmp_dir == '/cygdrive/c/WINDOWS/TEMP'
    assert conn._local_files_dir == 'powershell_files'
    assert conn._remote_files_dir == 'powershell_files'

# Generated at 2022-06-13 15:04:57.860363
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ps = ShellModule()
    assert ps.COMPATIBLE_SHELLS == frozenset()
    assert ps.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:05:02.120316
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS == True

    # Test to make sure the SHELL_FAMILY does not require a file extension
    shell = ShellModule(command_name='powershell.exe')
    assert shell.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:05:03.414391
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None, runner=None, shell_type=None)
    assert shell



# Generated at 2022-06-13 15:05:05.792162
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if to_text(sys.version_info[0]) == '2':
        test_ShellModule_v2()
    else:
        test_ShellModule_v3()



# Generated at 2022-06-13 15:05:17.643101
# Unit test for constructor of class ShellModule
def test_ShellModule():
    a = ShellModule()

    # Test inherited properties
    assert a.SHELL_NAME == 'powershell'
    assert a._IS_BINARY is False
    assert a._IS_WINDOWS is True
    assert a.SHELL_FAMILY == 'powershell'
    assert a.COMPATIBLE_SHELLS == frozenset()

    # Test inherited methods
    assert a.join_path('test_path', 'test_dir') == 'test_path\\test_dir'
    assert a.set_user_facl('test_path', 'test_user', 'test_mode') is None
    assert a.env_prefix() == ''
    assert a.build_module_command('test_env_string', None, 'test_cmd') == "& 'test_cmd'; exit $LASTEXITCODE"

# Generated at 2022-06-13 15:05:21.925330
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.powershell.powershell import ShellModule
    shell = ShellModule(connection='winrm')
    assert shell._shell_executable == "PowerShell"
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS
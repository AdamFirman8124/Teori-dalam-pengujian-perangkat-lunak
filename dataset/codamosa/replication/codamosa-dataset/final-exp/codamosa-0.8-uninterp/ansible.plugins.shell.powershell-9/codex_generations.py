

# Generated at 2022-06-13 14:55:41.573032
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    sh = ShellModule(connection=None)
    assert sh.expand_user(user_home_path='~', username='') == sh.expand_user(user_home_path='~\\', username='')

    # If the path starts with '~\\', then it should be replaced with the result of 'Get-Location'.
    # to_text(sh.expand_user(user_home_path='~\\')) == "C:\Users\{user}\Documents"
    # We skip this part of the test. It depends on the current location of the user.
    # assert to_text(sh.expand_user(user_home_path='~\\', username='')).startswith("C:\\Users\\{user}")


# Generated at 2022-06-13 14:55:52.575767
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():

    powershell_shell_module = ShellModule()

    # Tests for unix style paths
    assert powershell_shell_module.path_has_trailing_slash('abcd/') == True
    assert powershell_shell_module.path_has_trailing_slash('/abcd/') == True
    assert powershell_shell_module.path_has_trailing_slash('/abcd') == False
    assert powershell_shell_module.path_has_trailing_slash('c:/abcd') == False
    assert powershell_shell_module.path_has_trailing_slash('c:/abcd/') == True

    # Tests for win style paths
    assert powershell_shell_module.path_has_trailing_slash('c:\\abcd\\') == True
    assert powershell_shell_

# Generated at 2022-06-13 14:56:00.601278
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    ps = ShellModule(None)
    assert ps.expand_user('~') == ps._encode_script(script='''Write-Output (Get-Location).Path''')
    assert ps.expand_user('~\\') == ps._encode_script(script='''Write-Output (Get-Location).Path''')
    assert ps.expand_user('~\\Downloads') == ps._encode_script(script='''Write-Output ((Get-Location).Path + 'Downloads')''')
    assert ps.expand_user('~/Downloads') == ps._encode_script(script='''Write-Output ((Get-Location).Path + 'Downloads')''')
    assert ps.expand_user(r'c:\users\test_user\appdata\local\temp') == ps._encode_script

# Generated at 2022-06-13 14:56:06.997350
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import ansible.plugins.shell.powershell
    module_name = 'ansible.plugins.shell.powershell'
    module_path = pkgutil.get_loader(module_name).filename
    module_dirname = os.path.dirname(module_path)
    module_data_path = os.path.join(module_dirname, 'data')
    # it's likely to be loaded as a zip file, but os.path.exists can't check that
    if not os.path.exists(module_data_path):
        module_data_path = os.path.join(module_path, 'data')
    bootstrap_wrapper = os.path.join(module_data_path, "bootstrap_wrapper.ps1")
    with open(bootstrap_wrapper, 'r') as f:
        bootstrap_

# Generated at 2022-06-13 14:56:13.941192
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():

    shell_module = ShellModule()

    # shell_module.get_remote_filename with pathname ending in .ps1
    filename = 'test.ps1'
    assert shell_module.get_remote_filename(filename) == filename

    # shell_module.get_remote_filename with pathname ending in .exe
    filename = 'test.exe'
    assert shell_module.get_remote_filename(filename) == filename

    # shell_module.get_remote_filename with pathname ending in .txt
    filename = 'test.txt'
    assert shell_module.get_remote_filename(filename) == 'test.ps1'

    # shell_module.get_remote_filename with pathname ending in .py
    filename = 'test.py'

# Generated at 2022-06-13 14:56:23.157486
# Unit test for method build_module_command of class ShellModule

# Generated at 2022-06-13 14:56:28.682281
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.module_utils.powershell import ShellModule
    shell = ShellModule()
    args = {}
    cmd = shell.mkdtemp(**args)
    print(cmd)
    assert shell.get_remote_filename('test_path') == 'test_path'

# Generated at 2022-06-13 14:56:31.907761
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module.SHELL_FAMILY == 'powershell'
    assert module._IS_WINDOWS


# Generated at 2022-06-13 14:56:35.340890
# Unit test for constructor of class ShellModule
def test_ShellModule():
    result = ShellModule()
    assert isinstance(result.COMPATIBLE_SHELLS, frozenset)
    assert result.COMPATIBLE_SHELLS == frozenset()
    assert result.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:56:43.407462
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.executor.powershell.winrm_wrapper import (
        WINRM_CONN_PLUGIN_CONNECTION,
        WINRM_COMM_PLUGIN_CONNECTION
    )

    def do_test(connection_type, module_is_text, shebang, cmd, arg_path, expected_result, expected_stderr):
        if connection_type not in (WINRM_CONN_PLUGIN_CONNECTION, WINRM_COMM_PLUGIN_CONNECTION):
            raise ValueError('connection_type must be one of (%s, %s)' % (WINRM_CONN_PLUGIN_CONNECTION, WINRM_COMM_PLUGIN_CONNECTION))

        sm = ShellModule(connection=connection_type)

# Generated at 2022-06-13 14:57:00.100988
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Make sure we're not processing any CLI args here
    from ansible.errors import AnsibleError
    from ansible.parsing.yaml.objects import AnsibleUnicode

    try:
        from ansible.plugins.shell import Powershell
    except ImportError:
        from ansible_collections.notmintest.not_a_real_collection.plugins.shell import Powershell

    try:
        Powershell(no_cli=True)
    except AnsibleError as e:
        assert str(e) == "Unable to find PowerShell in PATH. Please ensure that PowerShell is installed"


# Generated at 2022-06-13 14:57:04.664124
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import tempfile
    test_dir = tempfile.mkdtemp()
    s = ShellModule(None)
    test_dir_name = s.mkdtemp(basefile=None, system=False, mode=None, tmpdir=test_dir)
    test_dir_name = test_dir_name.strip()
    assert test_dir_name.startswith(test_dir)
    os.rmdir(test_dir_name)

# Generated at 2022-06-13 14:57:06.561380
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.get_option('remote_tmp') == '$env:TEMP'

# Generated at 2022-06-13 14:57:17.432212
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule(connector=None, shell_executable='/usr/bin/env')
    wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")

    # Should call module without script as remote command
    cmd = shell.build_module_command('', '#!powershell', 'foo.ps1')
    assert cmd == to_bytes(shell._encode_script(script=wrapper, strict_mode=False, preserve_rc=False))

    # Should call module with script
    cmd = shell.build_module_command('', '#!powershell', 'foo.ps1', arg_path='arg_path')

# Generated at 2022-06-13 14:57:20.659873
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell._IS_WINDOWS
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell._SHELL_AND == ';'

# Generated at 2022-06-13 14:57:24.584482
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    sm = ShellModule()
    assert sm.mkdtemp(tmpdir='c:\\temp') == sm._encode_script("""
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('c:\\temp')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'ansible-tmp-*'
        Write-Output -InputObject $tmp.FullName
    """)

# Generated at 2022-06-13 14:57:31.248433
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.plugins.shell.powershell import ShellModule
    shell = ShellModule()
    basefile = "basefile"
    tmpdir = "/tmpdir"
    script = shell.mkdtemp(basefile=basefile, tmpdir=tmpdir)
    import re
    # The script should contain a String containing the characters $tmp_path =
    # and $tmp =
    assert re.search(b"\$tmp_path =.*\$tmp =", script) is not None


# Generated at 2022-06-13 14:57:43.373168
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import json
    from ansible.executor.powershell.shell_plugin import test_powershell

    module = test_powershell._build_module()
    shell_spec = {
        'SHELL_PLUGIN': 'test_powershell',
        'SHELL_PLUGIN_SHELL': ShellModule.SHELL_FAMILY,
        'SHELL_PLUGIN_TARGET': 'test_target',
        'SHELL_PLUGIN_ARGS': 'test_args'
    }
    shell = ShellModule(shell_spec, module)

    shell._exec_wrapper = 'w'
    shell._arg_tmpdir = None
    module_return = shell.mkdtemp()

    #stdin,stdout,stderr,rc,out,err,cmd,args,prompt,encoding,codec,

# Generated at 2022-06-13 14:57:47.030612
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    Test ShellModule constructor
    '''

    sm = ShellModule()
    assert sm.SHELL_FAMILY == 'powershell'
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm._IS_WINDOWS



# Generated at 2022-06-13 14:57:58.512250
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule()
    # No shebang, module is assumed to be binary
    print(shell.build_module_command(env_string='', shebang='', cmd='/usr/bin/python', arg_path='foo'))
    # Shebang is ignored for binaries
    print(shell.build_module_command(env_string='', shebang='#!/usr/bin/env python', cmd='/usr/bin/python', arg_path='foo'))
    # Shebang starting with #! is ignored for binaries
    print(shell.build_module_command(env_string='', shebang='#!/usr/bin/env python', cmd='/usr/bin/python', arg_path='foo'))
    # Shebang is stripped for Python scripts

# Generated at 2022-06-13 14:58:10.132056
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Values needs to be set to run the unit test
    # Can be set in ansible.cfg under [defaults]
    connect_host = 'localhost'
    connect_port = 5985
    # Can be set in any of the following paths
    # Working dir
    # ~/.ansible.cfg
    # /etc/ansible/ansible.cfg
    # /etc/ansible/roles/role_under_test/tests/ansible.cfg

    shell_module = ShellModule(
        connect_host, connect_port,
        'winrm', 'ntlm',
        'plaintext'
    )

    # Functionality of ShellModule to be tested
    # shell_module.join_path
    # shell_module.get_remote_filename
    # shell_module.path_has_trailing_slash
    # shell

# Generated at 2022-06-13 14:58:19.428156
# Unit test for constructor of class ShellModule
def test_ShellModule():

    if not os.name == 'nt':
        return

    # Create an object and get instance of the object
    ShellModuleObject = ShellModule()

    # Check the type of the object
    assert type(ShellModuleObject) is ShellModule
    # Check the type of attributes
    assert type(ShellModuleObject._SHELL_REDIRECT_ALLNULL) is str
    assert type(ShellModuleObject._SHELL_AND) is str
    assert type(ShellModuleObject._IS_WINDOWS) is bool
    # Check the values of attributes
    assert ShellModuleObject._SHELL_REDIRECT_ALLNULL == "> $null"
    assert ShellModuleObject._SHELL_AND == ';'
    assert ShellModuleObject._IS_WINDOWS == True

# Generated at 2022-06-13 14:58:21.374165
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sh_module = ShellModule(connection=None)
    assert isinstance(sh_module, ShellModule)


# Generated at 2022-06-13 14:58:29.776446
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(shebang='#!/usr/bin/env bash')
    # _shell familly should be of type str
    assert isinstance(shell._shell, str)
    # _shell familly should be bash
    assert shell._shell == 'bash'
    # _IS_WINDOWS should be False
    assert not shell._IS_WINDOWS

    shell = ShellModule(shebang='#!C:/cygwin/bin/bash')
    assert shell._shell == 'bash'
    assert not shell._IS_WINDOWS

    shell = ShellModule(shebang='#!/usr/bin/env bash -x')
    assert shell._shell == 'bash'
    assert not shell._IS_WINDOWS

    shell = ShellModule(shebang='#!/usr/bin/env python')
    assert shell._shell == 'python'
    assert not shell._IS_

# Generated at 2022-06-13 14:58:30.731540
# Unit test for constructor of class ShellModule
def test_ShellModule():
    connection =  ShellModule("")

# Generated at 2022-06-13 14:58:38.266202
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import iteritems
    module = AnsibleModule(
        argument_spec=dict(
            basefile=dict(type='str', default=None),
            system=dict(type='bool', default=False),
            mode=dict(type='str', default=None),
            tmpdir=dict(type='str', default=None)
        ),
        supports_check_mode=True
    )
    t = tempfile.mkdtemp()
    m = ShellModule(
        **dict(
            [(k, v) for (k, v) in iteritems(module.params)
             if k not in ['basefile', 'system', 'mode', 'tmpdir']]
        )
    )
    new_temp_

# Generated at 2022-06-13 14:58:43.361038
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    powershell_cmd = ShellModule([])
    basefile = 'ansible-powershell-test-my-script'
    tmpdir = 'C:\\Windows\\Temp'
    result = powershell_cmd.mkdtemp(basefile=basefile, tmpdir=tmpdir)
    assert result == b'$tmp_path = [System.Environment]::ExpandEnvironmentVariables(\'C:\\Windows\\Temp\');$tmp = New-Item -Type Directory -Path $tmp_path -Name \'ansible-powershell-test-my-script\';Write-Output -InputObject $tmp.FullName;'


# Generated at 2022-06-13 14:58:44.262815
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:58:52.593466
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.get_remote_filename('test.sh') == 'test.ps1'
    assert module.get_remote_filename('test.py') == 'test.py.ps1'

    assert module.join_path('c:\\', 'does\\not\\matter') == 'c:\\does\\not\\matter'
    assert module.join_path('/', 'does\\not\\matter') == '\\does\\not\\matter'
    assert module.join_path('c:\\', '\\does\\not\\matter') == 'c:\\does\\not\\matter'
    assert module.join_path('c:\\', '\\does\\not\\matter\\') == 'c:\\does\\not\\matter'

# Generated at 2022-06-13 14:58:56.279237
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    mkdtemp_powershell_script = pkgutil.get_data("ansible.executor.powershell", "mkdtemp.ps1")
    powershell = ShellModule()
    script = powershell._encode_script(mkdtemp_powershell_script)
    result = powershell._execute_remote_cmd(script)
    assert result.startswith('C:\\\\Windows\\\\Temp')

# Generated at 2022-06-13 14:59:19.831382
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.plugins.connection.powershell as powershell

    shell = powershell.ShellModule(None)
    shell.run()
    shell.run_command()
    shell.run_pipelined_commands()
    shell.exec_command()
    shell.get_option()
    shell.add_command_to_buffer()
    shell.send_buffer()
    shell.receive()
    shell.cleanup()
    shell.exec_command()

# Generated at 2022-06-13 14:59:29.116849
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import platform

    remote_tmp = '~/tmp'
    tmpdir = '~/tmp'
    powershell_shell = ShellModule(remote_tmp=remote_tmp, tmpdir=tmpdir)
    assert powershell_shell.get_option('remote_tmp') == remote_tmp
    assert powershell_shell.get_option('tmpdir') == tmpdir
    assert powershell_shell._SHELL_REDIRECT_ALLNULL == '> $null'
    assert powershell_shell._SHELL_AND == ';'
    assert powershell_shell._IS_WINDOWS == True

    # Test COMPATIBLE_SHELLS
    if platform.system() == 'Windows':
        assert powershell_shell.COMPATIBLE_SHELLS == frozenset(['powershell', 'ps1'])
    else:
        assert powershell

# Generated at 2022-06-13 14:59:31.041625
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.executor.powershell.shell
    shell_module = ansible.executor.powershell.shell.ShellModule(None)

    assert shell_module != None

# Generated at 2022-06-13 14:59:35.868598
# Unit test for constructor of class ShellModule
def test_ShellModule():

    mod = ShellModule({})
    mod.SHELL_FAMILY = ShellModule.SHELL_FAMILY
    mod.SHELL_TYPE = ShellModule.SHELL_FAMILY
    mod._IS_WINDOWS = ShellModule._IS_WINDOWS

    # Test with_loopback
    assert mod.with_loopback('module_args', 'module_name') == '{{ ansible_user_dir }}/ansible_loopback'

# Generated at 2022-06-13 14:59:47.196559
# Unit test for constructor of class ShellModule
def test_ShellModule():
    test1 = ShellModule(run_command_environ_update={'foo': 'bar'})
    assert test1._SHELL_REDIRECT_ALLNULL == '> $null'
    assert test1._SHELL_AND == ';'
    assert test1._IS_WINDOWS is True
    assert test1.COMPATIBLE_SHELLS == frozenset()
    assert test1.SHELL_FAMILY == 'powershell'

    test2 = ShellModule(no_log={'enabled': True})
    assert test2._SHELL_REDIRECT_ALLNULL == '> $null'
    assert test2._SHELL_AND == ';'
    assert test2._IS_WINDOWS is True
    assert test2.COMPATIBLE_SHELLS == frozenset()
    assert test2.SHELL_FAMILY

# Generated at 2022-06-13 14:59:51.528836
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule()
    assert obj, "Failed to create ShellModule"
    assert obj.SHELL_FAMILY == 'powershell', "Invalid shell family"
    # These shells were deprecated, so we should not actually get here for
    # powershell
    assert not obj.COMPATIBLE_SHELLS, "No compatible shells should be supported"

# Generated at 2022-06-13 14:59:52.152927
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# Generated at 2022-06-13 14:59:56.143979
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    Unit test of the ShellModule constructor.
    '''
    module = ShellModule()
    assert module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module._SHELL_AND == ';'

# Generated at 2022-06-13 15:00:07.202805
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Test the constructor of class ShellModule"""
    # The connection to ssh or winrm
    connection = 'ssh'

    # The class ShellModule constructor requires the connection
    shell_module = ShellModule(connection)

    # Check that the shell module is using the correct prompt when using winrm
    connection = 'winrm'
    shell_module = ShellModule(connection)
    assert shell_module._IS_WINDOWS is True
    assert shell_module.SHELL_FAMILY is 'powershell'
    assert shell_module.DEFAULT_EXECUTABLE is 'powershell'
    assert shell_module._SHELL_REDIRECT_ALLNULL is '> $null'
    assert shell_module._SHELL_AND is ';'
    assert shell_module.COMPATIBLE_SHELLS == frozenset()
    assert shell_module._SH

# Generated at 2022-06-13 15:00:11.396549
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Run unit tests for ShellModule class
    """
    pwsh_shell = ShellModule(connection=None, runner=None, no_log=True, keep_remote_files=True, module_name='script')
    pwsh_shell.SHELL_FAMILY = 'powershell'
    pwsh_shell.SHELL_NAME = 'powershell'
    assert pwsh_shell is not None


# Generated at 2022-06-13 15:00:32.324991
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # create a basic powershell object
    ps = ShellModule(connection=None, add_ssh_args=None)
    # check for executable attribute
    assert ps.executable == 'powershell'
    # check for the SHELL_FAMILY attribute
    assert ps.SHELL_FAMILY == 'powershell'
    # check for the COMPATIBLE_SHELLS attribute
    assert ps.COMPATIBLE_SHELLS == frozenset()


# Generated at 2022-06-13 15:00:34.102812
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test with the default constructor
    sm = ShellModule()
    assert sm.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:00:35.256877
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule()
    assert plugin.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:00:37.794437
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()

    for shell in sm.COMPATIBLE_SHELLS:
        assert shell in ['powershell'], "ShellModule.COMPATIBLE_SHELLS has unexpected value"

    assert sm.SHELL_FAMILY == 'powershell', "ShellModule.SHELL_FAMILY has unexpected value"


# Generated at 2022-06-13 15:00:44.056160
# Unit test for constructor of class ShellModule
def test_ShellModule():

    shell = ShellModule()

    # test _shell_plugin_class_name()
    assert shell._shell_plugin_class_name() == 'ShellModule'

    # test wrap_for_exec()
    assert shell.wrap_for_exec('& echo Hello World') == '& echo Hello World; exit $LASTEXITCODE'

    # test _encode_script()
    # script = ''
    assert shell._encode_script('', False) == ' '.join(_common_args + ['-Command', '-'])

    # script = 'Hello World'
    script_hello_world = 'Hello World'

# Generated at 2022-06-13 15:00:52.556795
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''shell_module_test.py: Test class ShellModule.'''
    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'

    assert module.path_has_trailing_slash('"abc"')
    assert module.path_has_trailing_slash('"abc\\"')
    assert module.path_has_trailing_slash('"abc/"')

    assert not module.path_has_trailing_slash('"abc')
    assert not module.path_has_trailing_slash('"abc\\"\\"')



# Generated at 2022-06-13 15:01:01.704656
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    sm._IS_WINDOWS = True
    sm.update_curr_to_orig()
    sm.set_shell(None)

    assert sm.get_name() == "powershell"
    assert sm.get_extension() == "ps1"
    assert sm.get_remote_filename(name="test.ps1") == "test.ps1"
    assert sm.get_remote_filename(name="test") == "test.ps1"
    assert not sm.path_has_trailing_slash("C:\windows")
    assert sm.path_has_trailing_slash("C:\windows\\")
    assert not sm.path_has_trailing_slash("C:/windows")
    assert sm.path_has_trailing_slash("C:/windows/")
    assert not sm

# Generated at 2022-06-13 15:01:12.458932
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.get_remote_filename('/test1/test2/test3.txt') == 'test3.txt'
    assert shell.get_remote_filename('/test1/test2/test3') == 'test3.ps1'
    assert shell.get_remote_filename('test3.txt') == 'test3.txt'
    assert shell.get_remote_filename('test3') == 'test3.ps1'
    assert '/' not in shell.expand_user('~/test1')
    assert '/' not in shell.expand_user('test1')

# Generated at 2022-06-13 15:01:15.357826
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sc = ShellModule(connection='winrm')
    assert sc.connection == 'winrm'
    assert sc.SHELL_FAMILY == 'powershell'
    assert sc.DEFAULT_EXECUTABLE == 'powershell'

# Generated at 2022-06-13 15:01:16.611963
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert isinstance(mod, object)

# Generated at 2022-06-13 15:01:41.064212
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()

    # Check for common shell filenames that this plugin handles
    # Powershell is handled differently.  It's selected when winrm is the
    # connection
    assert module.COMPATIBLE_SHELLS == frozenset()

    # Family of shells this has.  Must match the filename without extension
    assert module.SHELL_FAMILY == 'powershell'

    # Used by various parts of Ansible to do Windows specific changes
    assert module._IS_WINDOWS is True

    # Timeout in seconds (float) for waiting for user to respond to a prompt sent by the shell
    assert module.PROMPT_TIMEOUT == 10

# Generated at 2022-06-13 15:01:41.916091
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule()
    assert isinstance(obj, ShellModule)


# Generated at 2022-06-13 15:01:42.534996
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()

# Generated at 2022-06-13 15:01:43.097172
# Unit test for constructor of class ShellModule
def test_ShellModule():
    pass

# Generated at 2022-06-13 15:01:44.185733
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None, runner=None)
    assert isinstance(shell, ShellModule)

# Generated at 2022-06-13 15:01:46.173029
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ps = ShellModule()


# Ansible 2.8
# Unit tests for join_path and get_remote_filename

# Generated at 2022-06-13 15:01:54.598735
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule(connection=None, _ansible_no_log=False, become_method=None, become_user='root', become_exe=None, become_flags=None)
    assert isinstance(sm, ShellBase)
    for path in ['/bin/a', '"/bin b"', '"/bin c"', '/bin\nd', '/bin\te']:
        unquoted = sm._unquote(path)
        assert unquoted == ntpath.normpath(unquoted)
        assert sm._escape(sm._unquote(path)) == sm._unquote(path)



# Generated at 2022-06-13 15:02:03.042665
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.executor.powershell
    ps = ShellModule(connection=None, play_context=None, new_stdin=None)
    print("Compatible shells: %s" % ', '.join(ps.COMPATIBLE_SHELLS))
    print("Shell family: %s" % ps.SHELL_FAMILY)
    print("Path has trailing slash: %s" % ps.path_has_trailing_slash("test\\"))
    print("Path has trailing slash: %s" % ps.path_has_trailing_slash("test"))
    print("Expand user: %s" % ps.expand_user("~\\test"))
    print("Expand user: %s" % ps.expand_user("~"))

# Generated at 2022-06-13 15:02:10.826032
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import json
    import random
    import shutil
    import time
    import tempfile
    from ansible.plugins.shell import ShellModule

    (fd, temp_path) = tempfile.mkstemp()
    f = os.fdopen(fd, "w+b")
    f.close()

    test_cases = [
        ('whoami', 'whoami', False),
        ('whoami ; exit 1', 'whoami ; exit 1', True),
    ]

    for (script, expected_script, fails) in test_cases:
        s = ShellModule(connection=None)
        # We want a random temp directory, since we're going to try to
        # create it and we don't want it to exist

# Generated at 2022-06-13 15:02:17.222069
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule(connection='winrm')
    assert sm.SHELL_FAMILY == 'powershell'

# Just like Python, a good to way to seperate logic from action in the test code.
# For the module code, the controller handle the logic and the communicator
#   code handle the action.
# We have a similar situation here, and we should keep it that way.

# Generated at 2022-06-13 15:02:55.587094
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.compat.tests.mock import patch, MagicMock

    my_mock = MagicMock()
    with patch.dict('sys.modules', {'ansible.executor.powershell': my_mock}):
        reload(shell_windows)
        reload(shell_windows.ShellModule)

    return shell_windows.ShellModule(connection=None)

# Generated at 2022-06-13 15:02:56.210512
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()

# Generated at 2022-06-13 15:03:00.167950
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mock_runner = None
    shell_obj = ShellModule(mock_runner)
    assert set(shell_obj.COMPATIBLE_SHELLS) == set([])
    assert shell_obj.SHELL_FAMILY == 'powershell'
    assert shell_obj._IS_WINDOWS == True


# Generated at 2022-06-13 15:03:03.027041
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()

    assert module._IS_WINDOWS
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module.SHELL_FAMILY == 'powershell'


# Generated at 2022-06-13 15:03:04.584468
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell._SHELL_REDIRECT_ALLNULL == '> $null'

# Generated at 2022-06-13 15:03:06.398258
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule()
    assert isinstance(obj, ShellModule)

# Generated at 2022-06-13 15:03:08.163341
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''Validate the constructor of ShellModule'''
    assert ShellModule.__doc__ is not None

# Generated at 2022-06-13 15:03:13.800638
# Unit test for constructor of class ShellModule
def test_ShellModule():

    powershell_shell_obj = ShellModule()
    print (powershell_shell_obj)

    # Validate ShellModule class constants
    assert "powershell" == powershell_shell_obj.SHELL_FAMILY
    assert True == powershell_shell_obj._IS_WINDOWS


if __name__ == '__main__':
    test_ShellModule()

# Generated at 2022-06-13 15:03:16.358659
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """This is a unit test for the constructor of ShellModule
    """
    obj = ShellModule()
    assert obj.SHELL_FAMILY == "powershell"

# Generated at 2022-06-13 15:03:17.921429
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''
    Unit test for constructor of class ShellModule
    :return:
    '''
    g_module = ShellModule()

# Generated at 2022-06-13 15:04:30.564240
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Place holder for test to be added
    pass

# Generated at 2022-06-13 15:04:34.986247
# Unit test for constructor of class ShellModule
def test_ShellModule():

    # Test for instantiation with wrong base class
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )
    try:
        ShellModule(module)
    except AssertionError:
        pass
    else:
        raise AssertionError('ShellModule used with wrong base class')

# Generated at 2022-06-13 15:04:42.934943
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_plugin_class = ShellModule
    assert shell_plugin_class.SHELL_FAMILY == 'powershell', 'SHELL_FAMILY must be powershell'
    assert shell_plugin_class.COMPATIBLE_SHELLS == set(), 'COMPATIBLE_SHELLS must be empty'
    assert shell_plugin_class.EXECUTABLE == 'powershell', 'EXECUTABLE must be powershell'
    assert shell_plugin_class.BINARY_MODULE_INTERPRETER == '', 'BINARY_MODULE_INTERPRETER must be empty'
    assert shell_plugin_class._IS_WINDOWS == True, '_IS_WINDOWS must be True'

# Generated at 2022-06-13 15:04:44.376878
# Unit test for constructor of class ShellModule
def test_ShellModule():
    a = ShellModule()
    b = ShellModule()
    assert a == b
    assert a is b



# Generated at 2022-06-13 15:04:44.948329
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 15:04:49.085637
# Unit test for constructor of class ShellModule
def test_ShellModule():
   import ansible.plugins.connection.powershell

   this_module = ansible.plugins.connection.powershell.ShellModule()

   assert this_module.COMPATIBLE_SHELLS == frozenset()
   assert this_module.SHELL_FAMILY == 'powershell'
   assert this_module._IS_WINDOWS == True

# Generated at 2022-06-13 15:04:50.494402
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule(connection=None)
    assert obj is not None

# Generated at 2022-06-13 15:04:58.332757
# Unit test for constructor of class ShellModule
def test_ShellModule():
    #Test that 'powershell' shells are supported
    shell_plugin = ShellModule('/bin/powershell')
    assert '/bin/powershell' in shell_plugin.COMPATIBLE_SHELLS
    #Test that 'powershell' shell_families are supported
    assert 'powershell' == shell_plugin.SHELL_FAMILY
    #Test that ShellPlugin.set_connection() accepts 'winrm' connections
    shell_plugin.set_connection(connection='winrm')
    assert 'winrm' == shell_plugin._connection
    #Test that ShellPlugin.set_connection() accepts 'psrp' connections
    shell_plugin.set_connection(connection='psrp')
    assert 'psrp' == shell_plugin._connection

# Generated at 2022-06-13 15:04:59.732980
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule({}) is not None

# Generated at 2022-06-13 15:05:01.166381
# Unit test for constructor of class ShellModule
def test_ShellModule():
    '''Unit test for constructor of class ShellModule.'''
    module = ShellModule()
    assert module is not None
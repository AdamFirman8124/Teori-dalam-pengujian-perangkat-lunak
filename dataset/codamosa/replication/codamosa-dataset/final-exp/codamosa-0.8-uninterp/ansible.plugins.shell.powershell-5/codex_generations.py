

# Generated at 2022-06-13 14:55:43.237065
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    # Test case 1: Provide a '~' for path
    m = ShellModule()
    script = "Write-Output (Get-Location).Path"
    cmd = m.expand_user(user_home_path='~')
    assert cmd == m._encode_script(script)

    # Test case 2: Provide a path of form '~\test_path' for path
    m = ShellModule()
    script = "Write-Output ((Get-Location).Path + '/test_path')"
    cmd = m.expand_user(user_home_path='~/test_path')
    assert cmd == m._encode_script(script)

    # Test case 3: Provide a path of form 'test_path' for path
    m = ShellModule()
    script = "Write-Output 'test_path'"

# Generated at 2022-06-13 14:55:48.368763
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule()
    assert plugin.SHELL_FAMILY == 'powershell'
    assert plugin.COMPATIBLE_SHELLS == frozenset()
    assert plugin._SHELL_REDIRECT_ALLNULL == '> $null'
    assert plugin._SHELL_AND == ';'


# Generated at 2022-06-13 14:55:57.825086
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.plugins import shell as shell_loader
    from ansible.plugins.loader import shell_loader as shell_loader_new
    import ansible.executor.module_common as module_common

    shell_kwargs = dict(
        no_log=True,
        become_user=None,
        stdin=None,
        binary_module=False,
        shebang=None,
        command_delimiter=None,
        use_persistent_connection=None,
    )
    shell_connection = module_common.ShellConnection(module_args_override=shell_kwargs)

    shell_conn = ShellModule(shell_connection)
    path_name = 'hello.py'
    path_name = shell_conn._un

# Generated at 2022-06-13 14:56:07.074199
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import shutil
    import tempfile
    import os

    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")
    bootstrap_wrapper_path = 'bootstrap_wrapper.ps1'
    with open(bootstrap_wrapper_path, 'wb') as tmpfile:
        tmpfile.write(bootstrap_wrapper)

    test_class = ShellModule()
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 14:56:14.215227
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")

    for arg in ["1", '"1"', "1", '"1"']:
        assert 'powershell -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand ' + base64.b64encode(bootstrap_wrapper.encode('utf-16-le')).decode('utf-8') == ShellModule(connection=None, runner=None).build_module_command('', '#!powershell', arg).replace("\\r\\n", "").replace("\\r", "").replace(";", "")

# Generated at 2022-06-13 14:56:20.445639
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    from ansible.executor.powershell import ShellModule
    test_shellmodule = ShellModule()
    assert test_shellmodule.get_remote_filename('c:/tmp/abc.ps1') == 'abc.ps1'
    assert test_shellmodule.get_remote_filename('c:/tmp/abc') == 'abc.ps1'
    assert test_shellmodule.get_remote_filename('c:/tmp/abc.cs') == 'abc.cs.ps1'

# Generated at 2022-06-13 14:56:27.370847
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    import pytest

    test_object = ShellModule(connection=None, add_ssh_args=None, runner=None, shell_type='')
    assert test_object.path_has_trailing_slash(path="C:\\Windows\\System32") == False
    assert test_object.path_has_trailing_slash(path="C:\\Windows\\System32\\") == True
    assert test_object.path_has_trailing_slash(path="C:/Windows/System32") == False
    assert test_object.path_has_trailing_slash(path="C:/Windows/System32/") == True
    assert test_object.path_has_trailing_slash(path="'C:\\Windows\\System32'") == False

# Generated at 2022-06-13 14:56:30.622524
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """This is a dummy test, just to create a unit test for ShellModule to figure
    out why travis is failing."""
    assert ShellModule().SHELL_FAMILY == 'powershell'



# Generated at 2022-06-13 14:56:39.500993
# Unit test for constructor of class ShellModule
def test_ShellModule():
    try:
        ShellModule(None)
    except TypeError as e:
        if e.args[0] != "ShellModule(): requires a dict object":
            raise
    except Exception:
        raise

    # TO-DO
    # Add tests for:
    #  * env_prefix
    #  * build_module_command
    #  * join_path
    #  * get_remote_filename
    #  * path_has_trailing_slash
    #  * chmod
    #  * chown
    #  * set_user_facl
    #  * remove
    #  * mkdtemp
    #  * expand_user
    #  * exists
    #  * checksum
    #  * wrap_for_exec

# Generated at 2022-06-13 14:56:49.792188
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    class MockShellModule(ShellModule):

        # Dummy class for unit testing purposes
        COMPATIBLE_SHELLS = frozenset()
        SHELL_FAMILY = 'powershell'
        _IS_WINDOWS = True

    # Verify the regex expression works as expected

    # trailing /
    assert MockShellModule().path_has_trailing_slash('/var/lib/foo/') is True
    assert MockShellModule().path_has_trailing_slash('/var/lib/foo//') is True
    assert MockShellModule().path_has_trailing_slash('\\var\\lib\\foo\\') is True
    assert MockShellModule().path_has_trailing_slash('\\var\\lib\\foo\\\\') is True

# Generated at 2022-06-13 14:56:54.855391
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert not shell.no_log
    assert not shell.always_pipeline

# Generated at 2022-06-13 14:56:59.063202
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()
    shell.noop_on_check(False)
    cmd = shell.mkdtemp(basefile='ansible-tmp-', system=False, mode=None, tmpdir='/tmp')
    script = '''$tmp_path = [System.Environment]::ExpandEnvironmentVariables('/tmp')
    $tmp = New-Item -Type Directory -Path $tmp_path -Name 'ansible-tmp-'
    Write-Output -InputObject $tmp.FullName
    '''
    assert cmd.strip() == shell._encode_script(script).strip()


# Generated at 2022-06-13 14:57:06.788369
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert hasattr(shell, 'env_prefix')
    assert hasattr(shell, 'join_path')
    assert hasattr(shell, 'get_remote_filename')
    assert hasattr(shell, 'path_has_trailing_slash')
    assert hasattr(shell, 'chmod')
    assert hasattr(shell, 'chown')
    assert hasattr(shell, 'set_user_facl')
    assert hasattr(shell, 'remove')
    assert hasattr(shell, 'mkdtemp')
    assert hasattr(shell, 'expand_user')
    assert hasattr(shell, 'exists')
    assert hasattr(shell, 'checksum')
    assert hasattr(shell, 'build_module_command')
    assert hasattr(shell, 'wrap_for_exec')

# Generated at 2022-06-13 14:57:08.323534
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule()
    print(m)


# Generated at 2022-06-13 14:57:18.557497
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule()
    assert hasattr(obj, 'run')
    assert hasattr(obj, 'run_as_root')
    assert hasattr(obj, 'put_file')
    assert hasattr(obj, 'get_file')
    assert hasattr(obj, 'add_to_log')
    assert hasattr(obj, 'join_path')
    assert hasattr(obj, 'get_remote_filename')
    assert hasattr(obj, 'path_has_trailing_slash')
    assert hasattr(obj, 'chmod')
    assert hasattr(obj, 'chown')
    assert hasattr(obj, 'set_user_facl')
    assert hasattr(obj, 'remove')
    assert hasattr(obj, 'mkdtemp')
    assert hasattr(obj, 'expand_user')


# Generated at 2022-06-13 14:57:21.439151
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    print(shell.get_remote_filename('/path/to/file/name'))
    print(shell.get_remote_filename('/path/to/file.exe'))
    print(shell.mkdtemp('/tmp/file_', tmpdir='/tmp/'))

# Generated at 2022-06-13 14:57:30.730704
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()
    assert shell.mkdtmp('abc') == '''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('{0}')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'abc'
        Write-Output -InputObject $tmp.FullName
        '''.format(shell.get_option('remote_tmp').replace('\\', '\\\\'))

    assert shell.mkdtmp('abc', tmpdir='/tmp') == '''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('/tmp')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'abc'
        Write-Output -InputObject $tmp.FullName
        '''.replace('\\', '\\\\')



# Generated at 2022-06-13 14:57:38.885023
# Unit test for constructor of class ShellModule
def test_ShellModule():
    powershell = ShellModule(connection=None, no_log=None, run_as_string=None, stdin=None, sudoable=False, transport=None, quiet=None, become_method=None)
    # Ensure we are in Windows
    assert powershell._IS_WINDOWS is True
    # Ensure we have the right Shell family
    assert powershell.SHELL_FAMILY == 'powershell'
    # Ensure we are compatible with the PowerShell Shell
    assert 'powershell' in powershell.COMPATIBLE_SHELLS


# Generated at 2022-06-13 14:57:42.189501
# Unit test for constructor of class ShellModule
def test_ShellModule():
    cmd = _common_args + ['-Command', '-']
    assert ShellModule(None, None)._encode_script('', as_list=True) == cmd


# Generated at 2022-06-13 14:57:49.232716
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shebang = u'#!/usr/bin/env python'
    cmd = u'echo "foo bar"'
    sm = ShellModule(conn=None, runner=None)
    r = sm.build_module_command(shebang=shebang, cmd=cmd)
    assert r == u'&' + sm._encode_script(u'echo "foo bar"') + u'; exit $LASTEXITCODE'

    cmd = u'"foo bar"'
    r = sm.build_module_command(shebang=shebang, cmd=cmd)
    assert r == u'&' + sm._encode_script(u'& "foo bar"; exit $LASTEXITCODE')

    cmd = u"./foo.py"

# Generated at 2022-06-13 14:57:56.791571
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule._IS_WINDOWS == True
    assert ShellModule.COMPATIBLE_SHELLS == frozenset([])
    assert ShellModule.SHELL_FAMILY == 'powershell'



# Generated at 2022-06-13 14:57:58.228642
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # make sure the ShellModule class can be instantiated
    ShellModule()

# Generated at 2022-06-13 14:58:06.546756
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import os
    import pexpect

    # These commands are specific to the winrm connection.
    # Invoke-Expression and Invoke-Command cannot be used here because
    # they do not behave in the same manner as 'cmd /c' or cmd.exe
    # shell.
    # Invoke-Expression interpolates variables while Invoke-Command
    # parses them literally.  We also need to pass the environment
    # string in such a way that it is not interpolated.
    # See: http://www.vexasoft.com/blogs/powershell/7255220-powershell-invoking-commands-remotely-with-different-credentials-and-different-configurations
    # Also, https://github.com/diyan/pywinrm/issues/146
    # https://github.com/diyan/pywin

# Generated at 2022-06-13 14:58:15.877296
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import os
    import ansible.constants as C
    import ansible.utils.template as template
    import ansible.utils.vars as vars
    import ansible.utils.unicode as unicode_utils
    from ansible.plugins.loader import ps_plugin_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # TODO: Use the template module to construct this
    env = dict(os.environ)
    env['ANSIBLE_CONFIG'] = '/dev/null'
    env['ANSIBLE_REMOTE_TEMP'] = '/tmp'

    # TODO: This needs to be set to a directory where the user running ansible has write permission

# Generated at 2022-06-13 14:58:26.463801
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import unittest

    class TestCase(unittest.TestCase):
        def test_non_pipelined_powershell(self):
            cmd = dict(cmd='echo "foo"', in_data=None, shebang='#!powershell')
            result = ShellModule(conn=None, in_data=None).build_module_command(cmd=cmd['cmd'], shebang=cmd['shebang'])

# Generated at 2022-06-13 14:58:31.043779
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sh = ShellModule()

    assert sh.get_remote_filename('/path/to/file/without/extension') == 'file.ps1'
    assert sh.get_remote_filename('/path/to/file.exe') == 'file.exe'
    assert sh.get_remote_filename('/path/to/file.ps1') == 'file.ps1'

# Generated at 2022-06-13 14:58:33.632620
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()
    assert ShellModule(connection=None)
    assert ShellModule(connection=Mock())
    assert ShellModule(connection=Mock(), no_log=True)
    assert ShellModule(connection=Mock(), no_log=False)

    assert ShellModule(tmpdir='/tmp/shell')

# Generated at 2022-06-13 14:58:35.232108
# Unit test for constructor of class ShellModule
def test_ShellModule():
    t = ShellModule('', '')
    assert t.get_option('shell_type') == 'powershell'



# Generated at 2022-06-13 14:58:41.111735
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    class fake_shell(ShellModule):
        def __init__(self):
            pass

        def get_option(self, option):
            return None

    s_shell = fake_shell()
    assert s_shell.expand_user('~') == 'Write-Output (Get-Location).Path'
    assert s_shell.expand_user('~root') == 'Write-Output \'~root\''



# Generated at 2022-06-13 14:58:51.219747
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # test shebang converting
    assert ShellModule._build_module_command(None, '#!/usr/bin/env bash', '/usr/bin/echo foo') == '/usr/bin/echo foo'
    assert ShellModule._build_module_command(None, '#!/usr/bin/env python', 'print 1') == 'python -c "print 1"'
    assert ShellModule._build_module_command(None, u'#!powershell', 'Write-Host hello') == \
        'type Write-Host hello | type %sbootstrap_wrapper.ps1' % 'ansible.executor.powershell.'

# Generated at 2022-06-13 14:58:58.400654
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    print(sm.SHELL_FAMILY)
    print(sm.COMPATIBLE_SHELLS)
    print(sm.IS_BINARY)


# Test of method _unquote()

# Generated at 2022-06-13 14:58:59.458398
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Check successful execution of a constructor
    ShellModule()

# Generated at 2022-06-13 14:59:03.656677
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule(conn_params={})
    assert ShellModule(conn_params={}, shell_type="powershell")
    assert ShellModule(conn_params={}, shell_type="powershell", become_method=None, become_user=None)

    with pytest.raises(AssertionError):
        ShellModule(conn_params={}, shell_type=None)



# Generated at 2022-06-13 14:59:13.820475
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    class TestShellModule(ShellModule):
        def __init__(self, *args):
            ShellModule.__init__(self, *args)
            self.FILE_TRANSFER_TMP_DIR = 'C:\\Windows\\Temp'
            self._IS_WINDOWS = True

    shellModule = TestShellModule("/usr/bin/python")

    env_string = '$env:ANSIBLE_MODULE_ARGS = Get-Content -raw -Encoding utf8 $env:ANSIBLE_MODULE_ARGS_PATH'
    shebang = '#!/usr/bin/python'
    cmd = 'mymodule.py'
    arg_path = 'C:\\Users\\Admin\\AppData\\Local\\Temp\\ansible_test_mvMfl5\\arg_0'


# Generated at 2022-06-13 14:59:18.893516
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.utils import context_objects as co
    ctx = co.Context()
    s = ShellModule(connection=None, runner_codec='utf-8', no_log=False, ansible_play_context=ctx)
    print(s._encode_script('Write-Host "Hello World"'))

# Generated at 2022-06-13 14:59:24.366991
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule._SHELL_REDIRECT_ALLNULL == '> $null'
    assert ShellModule._SHELL_AND == ';'
    assert ShellModule._IS_WINDOWS
    assert ShellModule.COMPATIBLE_SHELLS == frozenset()
    assert ShellModule.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 14:59:31.817311
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    pm = ShellModule()

    assert pm.expand_user('~') == 'VwByAGkAdABpAGwAZQBjAHQAUABpAHMAcwB3AG8AcgBkACAAVwBBAEwAIABbAHMA'\
                                  'dABhAHQAZQBtACAAUgBPAEsAUwB0AGkAbwBuAF0ALgBpAGMAZQBzAC4AYwBvAG0A'\
                                  'IABBAG0AcwBlAHIAUwBoAGEAdABoACkA'


# Generated at 2022-06-13 14:59:33.374485
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    if not isinstance(module, ShellModule):
        raise Exception('module not of type ShellModule')

# Generated at 2022-06-13 14:59:34.217929
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule is not None


# Generated at 2022-06-13 14:59:44.865179
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()

# Generated at 2022-06-13 14:59:52.667695
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule({})
    assert '#!powershell' == module.DEFAULT_SHELL
    assert 'powershell' == module.SHELL_FAMILY
    assert '-' == module._SHELL_REDIRECT_ALLNULL
    assert ';' == module._SHELL_AND
    assert True == module._IS_WINDOWS


# Generated at 2022-06-13 14:59:53.917482
# Unit test for constructor of class ShellModule
def test_ShellModule():
    p = ShellModule()
    assert not p.HAS_TTY



# Generated at 2022-06-13 15:00:00.869144
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.plugins.shell import ShellModule

    sm = ShellModule()
    env_string = '$Env:ANSIBLE_MODULE_ARGS=(ConvertTo-Json @{a=1;b=2})\r\n$Env:TEST_ENV="TEST_ENV_VALUE"'
    shebang = '#!powershell'
    cmd = '. \\lib\\AnsibleModules.psm1;Test-Module'
    arg_path = "test\\ansible_module_hello.exe"

# Generated at 2022-06-13 15:00:04.919303
# Unit test for constructor of class ShellModule
def test_ShellModule():
    options = dict(
        remote_tmp='',
        remote_uid='',
        remote_user='',
        remote_port=''
    )
    shell = ShellModule(session=None, **options)
    return shell.SHELL_FAMILY

# Generated at 2022-06-13 15:00:14.541469
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(None, None)
    assert module.CHECKSUM_FILES == {'sha1', 'sha256', 'sha384', 'sha512', 'md5'}
    assert module.DEFAULT_SYSLOG_FACILITY == 'user'
    assert module.DEFAULT_SYSLOG_LEVEL == 'notice'
    assert module.SUPPORTED_FILTER_PLUGINS == []
    assert module.BINARY_MODULES == {}
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module.SHELL_FAMILY == 'powershell'
    assert module.IS_WINDOWS == True
    assert module.env_prefix() == ''
    assert module.get_remote_filename('test.py') == 'test.py'
    assert module.get_remote_filename

# Generated at 2022-06-13 15:00:23.437855
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule()

# Generated at 2022-06-13 15:00:33.622124
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    import unittest

    class TestShellModuleBuildModuleCommand(unittest.TestCase):
        def test_with_shebang(self):
            import ansible.plugins.shell as shell
            shell_obj = shell.ShellModule(connection=None, shell_executable='/bin/bash')
            result = shell_obj.build_module_command('', '#!script', '', '')

# Generated at 2022-06-13 15:00:38.910344
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell = ShellModule()
    action = shell.expand_user(user_home_path="~\\test1")
    assert action == '''Write-Output ((Get-Location).Path + '\\test1')'''
    action = shell.expand_user(user_home_path="~\\test1\\test2")
    assert action == '''Write-Output ((Get-Location).Path + '\\test1\\test2')'''
    action = shell.expand_user(user_home_path="\\test1")
    assert action == '''Write-Output '\\test1' '''
    action = shell.expand_user(user_home_path="test1")
    assert action == '''Write-Output 'test1' '''

# Test for the method get_remote_filename of the class ShellModule

# Generated at 2022-06-13 15:00:41.977001
# Unit test for constructor of class ShellModule
def test_ShellModule():
    m = ShellModule('winrm')
    assert m.shell_type == 'powershell'
    assert m.SHELL_FAMILY == 'powershell'
    assert m._SHELL_REDIRECT_ALLNULL == '> $null'
    assert m._SHELL_AND == ';'
    assert m._IS_WINDOWS

    assert m.env_prefix() == ''

# Generated at 2022-06-13 15:00:51.543436
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.plugins.shell.powershell import ShellModule
    import ansible.plugins.shell.powershell
    import ansible.plugins.shell.windows

    assert ShellModule.COMPATIBLE_SHELLS == frozenset()
    assert ShellModule.SHELL_FAMILY == 'powershell'
    assert ShellModule._IS_WINDOWS == True

    # when ansible.module_utils.local_ansible_common.AnsibleDefaultShell is not defined
    assert ShellModule.__doc__ == 'Windows PowerShell'

    # when ansible.module_utils.local_ansible_common.AnsibleDefaultShell is defined
    #assert ShellModule.__doc__ == 'Windows PowerShell ( %s )' % ansible.module_utils.local_ansible_common.AnsibleDefaultShell


# Generated at 2022-06-13 15:01:00.070878
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.SHELL_FAMILY == 'powershell'
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module._IS_WINDOWS
    assert module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module._SHELL_AND == ';'


# Generated at 2022-06-13 15:01:06.132150
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule.COMPATIBLE_SHELLS == frozenset()
    assert ShellModule.SHELL_FAMILY == 'powershell'
    assert ShellModule.STDERR_FILENAME == ntpath.join(ntpath.sep, 'tmp', 'ansible_err_%s.log' % os.getpid())
    assert ShellModule._IS_WINDOWS == True

# Generated at 2022-06-13 15:01:15.243578
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import json

    def run_module(module_name, module_args, expect_success=True):
        shell_module = ShellModule(connection='winrm', no_log=True)
        result, _ = shell_module.run(module_name, module_args)
        assert 'rc' in result
        assert 'failed' in result
        assert 'stdout' in result
        assert 'stderr' in result
        assert result['rc'] == 0 ^ result['failed']
        if expect_success:
            assert result['stderr'] == ''
        return result

    def assert_result(result, expected):
        assert result['stdout'].strip() == expected
        assert result['rc'] == 0
        assert result['failed'] is False


# Generated at 2022-06-13 15:01:17.037908
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule(connection=None)
    assert module.SHELL_FAMILY == 'powershell'



# Generated at 2022-06-13 15:01:28.098070
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    module = ShellModule(connection='winrm', no_log=True)
    # binary_module

# Generated at 2022-06-13 15:01:29.550736
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Appease flake8 by making it believe that this method is actually used
    pass



# Generated at 2022-06-13 15:01:35.713427
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule()
    assert shell.path_has_trailing_slash("/some/path/")
    assert shell.path_has_trailing_slash("/another\\\\path/")
    assert shell.path_has_trailing_slash("C:\\some\\path/")
    assert not shell.path_has_trailing_slash("C:\\some\\path")



# Generated at 2022-06-13 15:01:36.434073
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()

# Generated at 2022-06-13 15:01:38.301749
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert(sm.SHELL_FAMILY == 'powershell')

# Generated at 2022-06-13 15:01:46.814633
# Unit test for constructor of class ShellModule
def test_ShellModule():
    basedir = os.path.dirname(os.path.realpath(__file__))
    test_data = open(os.path.join(basedir, 'test_data/clixml_output.txt')).read().encode('utf-16-le')

# Generated at 2022-06-13 15:01:59.950023
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    '''
    Unit test for method build_module_command of class ShellModule
    '''
    shell = ShellModule()
    shell.get_option = lambda key: None
    script = shell.build_module_command('', '', 'foo.ps1')
    assert len(script) > 0
    assert to_text(base64.b64decode(script[script.index('-EncodedCommand') + 1])).startswith('foo.ps1')
    script = shell.build_module_command('', '#!powershell', 'foo.ps1')
    assert len(script) > 0
    assert script == 'type "foo.ps1" | & {'
    script = shell.build_module_command('', '#!powershell', 'foo.exe')
    assert len(script) > 0

# Generated at 2022-06-13 15:02:08.762186
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():

    module = ShellModule()

    # Test encode script

# Generated at 2022-06-13 15:02:09.774069
# Unit test for constructor of class ShellModule
def test_ShellModule():
    plugin = ShellModule()
    assert plugin

# Generated at 2022-06-13 15:02:20.915863
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils.remote_management.powershell.executor import get_ps_script

    basedir = os.path.abspath(os.path.dirname(__file__))
    ps_script = get_ps_script(basedir, "../xUnit-runner/tools/xunit-runner.ps1", "powershell.exe")

    # From xUnit-runner.ps1 (sha: 3b8f1864a0f5f9a81c946ecb8432d65d2e3cc3f0)
    # Test that the script is correctly wrapped in a bootstrap wrapper

# Generated at 2022-06-13 15:02:23.913638
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # positive test cases
    assert isinstance(ShellModule, type)
    # negative test cases
    try:
        obj = ShellModule()
        assert False
    except TypeError as e:
        assert isinstance(e, TypeError)

# Generated at 2022-06-13 15:02:25.040724
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shellmodule = ShellModule()

# Generated at 2022-06-13 15:02:34.454723
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # TODO: Can we make this more generic?
    if not os.path.exists(os.path.join(os.path.dirname(__file__), 'bootstrap_wrapper.ps1')):
        return
    test_instance = ShellModule(connection=None)

# Generated at 2022-06-13 15:02:37.079339
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule.get_option('vault_password') is None

# Generated at 2022-06-13 15:02:41.754766
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.COMPATIBLE_SHELLS == frozenset()
    assert sm.SHELL_FAMILY == 'powershell'
    assert sm._SHELL_REDIRECT_ALLNULL == '> $null'
    assert sm._SHELL_AND == ';'
    assert sm._IS_WINDOWS == True

# Generated at 2022-06-13 15:02:44.327095
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Unit test for constructor of class ShellModule
    :return: None
    """
    from ansible.module_utils._text import to_bytes
    sm = ShellModule('test inventory')
    assert sm is not None

# Generated at 2022-06-13 15:03:00.898261
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_plugin = ShellModule()
    assert shell_plugin.SHELL_FAMILY == 'powershell'
    assert ShellModule._unquote(shell_plugin, "text") == "text"
    assert ShellModule._unquote(shell_plugin, "'text'") == "text"
    assert ShellModule._unquote(shell_plugin, '"text"') == "text"

# Generated at 2022-06-13 15:03:08.445299
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    module = ShellModule()

    # pipelining
    env_string = u'$foo = "bar"'
    shebang = u'#!powershell'
    cmd = u''
    expected = u'IgBmYXI='
    result = module.build_module_command(env_string, shebang, cmd)
    assert result == expected

    # non-pipelining non-psh module
    env_string = u'$foo = "bar"'
    shebang = u'#!/usr/bin/python'
    cmd = u'/foo'
    expected = u'IgBmYXI='
    result = module.build_module_command(env_string, shebang, cmd)
    assert result == expected

    # non-pipelining binary module

# Generated at 2022-06-13 15:03:11.901484
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Test shell module"""
    module = ShellModule(connection=None)
    assert module.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:03:20.204826
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    module = ShellModule()
    env_string = '$env:ANSIBLE_MODULE_ARGS = ConvertTo-Json -Depth 99 @{ foo = "test"; bar = "{{test}}"; baz = @("test",@("test")); };'
    shebang = '#!/usr/bin/python'
    cmd = '/usr/lib/python2.7/dist-packages/ansible/modules/commands/command.py'
    # Passing in an arg_path to return through the module
    arg_path = '/path/to/file'
    cmd_parts = shlex.split(cmd, posix=False)
    cmd_parts = list(map(to_text, cmd_parts))

    cmd_parts[0] = module._unquote(cmd_parts[0])

# Generated at 2022-06-13 15:03:28.475921
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():

    # Test module with shebang
    class TestModuleWithShebang(ShellModule):
        pass

    shell = TestModuleWithShebang()
    cmd = shell.build_module_command('', '#!powershell', 'echo hello', '')
    assert cmd == '& "type echo.ps1 | type bootstrap_wrapper.ps1"'

    # Test module with binary
    class TestModuleWithBinary(ShellModule):
        pass

    shell = TestModuleWithBinary()
    cmd = shell.build_module_command('', '', 'chocolatey', '')
    assert cmd == '& "chocolatey" ""'

# Generated at 2022-06-13 15:03:29.689022
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_obj = ShellModule()
    assert shell_obj is not None


# Generated at 2022-06-13 15:03:31.175704
# Unit test for constructor of class ShellModule
def test_ShellModule():
    p = ShellModule()
    assert isinstance(p, ShellModule)


# Generated at 2022-06-13 15:03:32.286455
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_mod = ShellModule()
    assert shell_mod is not None

# Generated at 2022-06-13 15:03:38.680240
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    def run_test(cases):
        for c in cases:
            m = ShellModule()
            cmd = m.build_module_command(c['env_string'], c['shebang'], c['cmd'], c['arg_path'])
            assert cmd == c['out'], 'Test failed: input: %s expected: %s got: %s' % (c, c['out'], cmd)

    # cmd is the command to wrap for execution.
    # env_string is the environment variables to use
    # shebang is the shebang line, if any
    # arg_path is the path to the arguments file
    # out is the result

# Generated at 2022-06-13 15:03:40.630795
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert (module.SHELL_FAMILY == 'powershell')
    assert (module._IS_WINDOWS)


# Generated at 2022-06-13 15:04:01.052953
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule()
    env_string = '$env:ANSIBLE_MODULE_ARGS=\'{"python_version": "2.7", "foo": "bar"}\''
    shebang = '#!powershell'
    cmd = 'gci'
    arg_path = "C:/Users/me/ansible.psm1"

    expected = '''$env:ANSIBLE_MODULE_ARGS='{"python_version": "2.7", "foo": "bar"}'
        $env:ANSIBLE_MODULE_RETVAL=1
        If (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }
        '''


# Generated at 2022-06-13 15:04:02.037922
# Unit test for constructor of class ShellModule
def test_ShellModule():
    test_module = ShellModule()
    assert test_module is not None

# Generated at 2022-06-13 15:04:07.974218
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection='local')
    shell._unquote('"Hello world!')
    shell._escape('"Hello world!')
    shell._encode_script('$(Get-ChildItem foo)', False)
    script = '''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('$(Get-ChildItem foo)')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name '%s'
        Write-Output -InputObject $tmp.FullName
        '''
    shell.mkdtemp(basefile="", system=False)
    shell.build_module_command(env_string="", shebang="#!powershell", cmd="", arg_path=None)
    shell.wrap_for_exec('& %s; exit $LASTEXITCODE')

# Generated at 2022-06-13 15:04:09.427249
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule('/usr/bin/python')
    assert 'SHELL_FAMILY' in dir(shell)


# Generated at 2022-06-13 15:04:20.934469
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module.COMPATIBLE_SHELLS == []
    assert module.SHELL_FAMILY == 'powershell'
    assert module._IS_WINDOWS is True
    assert module.env_prefix() == ""
    assert module.join_path("C:\\a b\\c d", "e f") == "C:\\a b\\c d\\e f"
    assert module.get_remote_filename("C:\\a b\\c d\\e f\\g h.exe") == "g h.exe"
    assert module.path_has_trailing_slash("C:\\a b\\c d\\e f\\") is True
    assert module.path_has_trailing_slash("C:\\a b\\c d\\e f") is False

# Generated at 2022-06-13 15:04:27.404000
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule('winrm')
    assert module.SHELL_FAMILY == 'powershell'
    assert module.COMPATIBLE_SHELLS == frozenset()
    assert module.SHELL_NAME == 'powershell'
    assert module.SHELL_START_DIRECTORY == r'C:\Users\Administrator'
    assert module.SHELL_STYLE == 'powershell'
    assert module.BINARY_MODULES_SHOULD_SKIP_CACHE is True
    assert module.HAS_PERSISTENT_HISTORY is True
    assert module.SHELL_PLUGIN_RESPONSE_DONE_AND_READY == 'DONE_AND_READY'

# Generated at 2022-06-13 15:04:36.420243
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    obj = ShellModule()
    obj._encode_script = MagicMock(return_value='encoded_script')
    assert obj.build_module_command('', '', '', 'arg_path') == '-EncodedCommand encoded_script'
    assert obj.build_module_command('', '#!', '', 'arg_path') == '-EncodedCommand encoded_script'
    assert obj.build_module_command('', '#!powershell', 'test.sh', 'arg_path') == \
        'type "test.sh.ps1" | encoded_script'
    assert obj.build_module_command('', '#!sh', 'test.sh arg1 arg2 arg3 arg4', 'arg_path') == \
        'sh -EncodedCommand encoded_script'

# Generated at 2022-06-13 15:04:45.397886
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    # Setup
    class ShellModuleTest(ShellModule):
        def get_option(self, option):
            if option == 'remote_tmp':
                return '%temp%'
            return None

        def _unquote(self, value):
            return value

        def _escape(self, value):
            return value

    obj = ShellModuleTest()

    # Test one: Empty command
    cmd = obj.build_module_command("", "", "")
    assert cmd == obj._encode_script(pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1"), strict_mode=False, preserve_rc=False)

    # Test two: Pipelining bypass
    # Test two assumes non-pipelining is working properly
    cmd = obj.build_module_command("", "", "command")

# Generated at 2022-06-13 15:04:46.896943
# Unit test for constructor of class ShellModule

# Generated at 2022-06-13 15:04:56.140759
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    python_shebang = '#!python'
    python_cmd = 'print("Hello world")'
    python_module_script = 'Test.py'
    python_module_script_with_path = 'test/Test.py'
    powershell_shebang = '#!powershell'
    powershell_cmd = 'Write-Output "Hello world"'
    powershell_module_script = 'Test.ps1'
    powershell_module_script_with_path = 'test/Test.ps1'

    module_args = "echo 'Module argument'"
    module_args_encoded = '$args = @("echo \'Module argument\'");'

    module_name = 'Test'
    module_path = '$pwd'
    module_default_args = '-ArgumentList $args'

    sm = ShellModule()



# Generated at 2022-06-13 15:05:18.812937
# Unit test for constructor of class ShellModule
def test_ShellModule():
    args = '-NoProfile -NonInteractive -ExecutionPolicy unrestricted'
    cmd = '& { & import-module .\ansible_powershell.psd1; ansibletest; }'
    test_shebang = '#!powershell'
    test_modulepath = 'C:\\Users\\test_user\\Ansible\\test.ps1'
    test_shell = ShellModule()
    # Test for _encode_script() with shebang
    result = test_shell._encode_script(script=cmd, strict_mode=False, preserve_rc=False)

# Generated at 2022-06-13 15:05:20.491063
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Construct a new ShellModule object
    shell_module = ShellModule()

# Generated at 2022-06-13 15:05:23.351033
# Unit test for constructor of class ShellModule
def test_ShellModule():
    mod = ShellModule()
    assert mod.COMPATIBLE_SHELLS == frozenset()
    assert mod.SHELL_FAMILY == 'powershell'
    assert mod._IS_WINDOWS

# Unit tests for methods of class ShellModule

# Generated at 2022-06-13 15:05:26.197601
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell._IS_WINDOWS is True
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell.COMPATIBLE_SHELLS == 'powershell'

# Generated at 2022-06-13 15:05:28.731418
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None, new_stdin='', prompt=None, new_stdout='', runner=None, new_stderr='')
    assert isinstance(shell, ShellBase)
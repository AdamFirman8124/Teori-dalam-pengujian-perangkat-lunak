

# Generated at 2022-06-13 14:55:34.330239
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule(connection=None, no_log=False)
    assert shell._IS_WINDOWS == True

# Generated at 2022-06-13 14:55:43.579841
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()

    # test default tmpdir is created
    cmd_result = shell.mkdtemp()
    assert cmd_result.startswith(b"powershell.exe -EncodedCommand")

    # test for tmpdir is created when no tmpdir is given
    cmd_result = shell.mkdtemp('temp')
    assert cmd_result.startswith(b"powershell.exe -EncodedCommand")
    assert b"System.IO.Path.Combine" in cmd_result
    assert b"Get-Location" in cmd_result
    assert b"New-Item" in cmd_result

    # test for tmpdir is created when a tmpdir is given
    cmd_result = shell.mkdtemp(tmpdir="/test")
    assert cmd_result.startswith(b"powershell.exe -EncodedCommand")


# Generated at 2022-06-13 14:55:51.211587
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.executor.powershell.common import ShellModule
    shell_module = ShellModule()
    shell_module.get_option = lambda x: ''
    result = shell_module.mkdtemp('{0}.ps1')
    assert result == '''$tmp_path = [System.Environment]::ExpandEnvironmentVariables('')
$tmp = New-Item -Type Directory -Path $tmp_path -Name ''{0}.ps1''
Write-Output -InputObject $tmp.FullName'''

# Generated at 2022-06-13 14:55:52.957352
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert(module.COMPATIBLE_SHELLS == frozenset())

# Generated at 2022-06-13 14:56:00.847692
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.executor.powershell.psbin.data.powershell_scripts.powershell import PowerShell

    fake_remote_tmp = 'C:\\Users\\Administrator\\AppData\\Local\\Temp'
    fake_basefile = 'shelltest_tmp'

    fake_powershell_object = PowerShell()
    # Replace the private method _generate_temp_dir_name by a function that always returns 'shelltest_tmp'
    fake_powershell_object._generate_temp_dir_name = lambda: fake_basefile

    # Generate the script and execute it
    powershell_script = fake_powershell_object.mkdtemp(basefile=fake_basefile, system=False, mode=None, tmpdir=fake_remote_tmp)
    powershell_result = fake_powershell_object.execute(powershell_script)



# Generated at 2022-06-13 14:56:02.221249
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.executor.powershell import ShellModule
    shell = ShellModule(None)
    assert isinstance(shell, ShellModule)



# Generated at 2022-06-13 14:56:09.715429
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    context = PlayContext()
    context.become = False
    context.become_method = 'runas'
    context.become_user = 'Administrator'
    context.connection = 'winrm'
    context.remote_addr = '127.0.0.1'
    context.port = 5985
    context.remote_user = 'Administrator'

    tqm = None

# Generated at 2022-06-13 14:56:16.166084
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shell = ShellModule()

    assert shell.mkdtemp() == shell._encode_script(script='''
        $tmp = New-Item -Type Directory -Name 'ansible-tmp-%%RANDOM%%'
        Write-Output -InputObject $tmp.FullName
        '''.strip(), strict_mode=False, preserve_rc=False)

    # if a custom base dir is given
    # the user folder will not be used by mkdtemp

# Generated at 2022-06-13 14:56:22.813722
# Unit test for constructor of class ShellModule
def test_ShellModule():
    myWinShell = ShellModule()
    assert myWinShell.SHELL_FAMILY == 'powershell'
    assert myWinShell.COMPATIBLE_SHELLS == frozenset()
    assert myWinShell.__class__.__name__ == 'ShellModule'
    assert myWinShell._IS_WINDOWS == True

    class MyNewClass(ShellModule):
        """This class is for unit test purpose"""
        pass
    myNewShell = MyNewClass()
    assert myNewShell.SHELL_FAMILY == 'powershell'


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 14:56:34.893959
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    Unit test for ShellModule
    """
    shell = ShellModule()

    # test default args
    assert 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted ' == shell._encode_script(script="")
    assert 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -Command -' == shell._encode_script(script='-')

    # test as_list=True
    assert ['PowerShell', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Unrestricted', '-Command', '-'] == \
        shell._encode_script(script='-', as_list=True)

    # test strict_mode=False
    assert 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand ' == \
        shell._encode_script

# Generated at 2022-06-13 14:56:48.720525
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    # create a dummy module for test
    class DummyModule:
        class DummyRunner:
            def __init__(self):
                self.noop_on_check_mode = False
                self.noop_on_check_mode_results = None

            def has_pipelining(self):
                return False

        def __init__(self):
            self.runner = self.DummyRunner()

    module = DummyModule()
    shell = ShellModule(module)

    script = shell.expand_user('~/.ansible/tmp')
    cmd = shell._encode_script(script, preserve_rc=False)
    assert cmd == '''%s -EncodedCommand '' ''' % ' '.join(_common_args)



# Generated at 2022-06-13 14:57:00.015202
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.module_utils.common._collections_compat import MutableMapping

    class DummyTaskExecutor(TaskExecutor):
        def __init__(self, *args, **kwargs):
            self.module_name = 'test_module'
            self.module_args = dict()
            self.module_vars = dict()
            self.remote_user = 'test_user'
            self.environment = dict()
            self.connection = 'winrm'
            self.play_context = dict()
            self.task_vars = dict()
            self.tmpdir = '~/ansible_test_dir'
            self.private_data_dir = '~/ansible_private_data'

            self._loader = None
           

# Generated at 2022-06-13 14:57:08.771110
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    import ansible.plugins.shell.powershell
    shell_module = ansible.plugins.shell.powershell.ShellModule(connection=None)
    # Test with a home directory relative to the user using tilde.
    assert shell_module.expand_user("~") == "Write-Output (Get-Location).Path"
    # Test with a home directory relative to the user using tilde and a slash.
    assert shell_module.expand_user("~/") == "Write-Output (Get-Location).Path"
    # Test with a home directory relative to the user using tilde and a backslash.
    assert shell_module.expand_user("~\\") == "Write-Output (Get-Location).Path"
    # Test with a home directory relative to the user using tilde and a path.
    assert shell_module.expand_

# Generated at 2022-06-13 14:57:18.313275
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell = ShellModule()
    test_cases = [
        ('~', 'Write-Output (Get-Location).Path'),
        ('~/bar', "Write-Output ((Get-Location).Path + '\\bar')"),
        ('~/bar/', "Write-Output ((Get-Location).Path + '\\bar')"),
        ('foo', "Write-Output 'foo'"),
        ('foo/bar', "Write-Output 'foo/bar'"),
        ('foo/bar/', "Write-Output 'foo/bar/'"),
    ]
    for (input, output) in test_cases:
        res = shell.expand_user(input)
        assert res == output, "expected '{0}', got '{1}'".format(output, res)

# Generated at 2022-06-13 14:57:27.230483
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()

    # Test normalization of Windows paths
    assert shell.join_path('c:\\', 'foo') == os.path.join('c:\\', 'foo')
    assert shell.join_path('c:\\', '/foo') == os.path.join('c:\\', 'foo')
    assert shell.join_path('c:\\', '/foo/bar') == os.path.join('c:\\', 'foo', 'bar')
    assert shell.join_path('c:/', 'foo') == os.path.join('c:\\', 'foo')
    assert shell.join_path('c:', 'foo') == os.path.join('c:', 'foo')
    assert shell.join_path('c:', '/foo') == os.path.join('c:', 'foo')
    assert shell

# Generated at 2022-06-13 14:57:35.449244
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    test_module = ShellModule()
    assert not test_module.path_has_trailing_slash('C:\\Users\\')
    assert test_module.path_has_trailing_slash('C:\\Users\\ ')
    assert test_module.path_has_trailing_slash('"C:\\Users\\"')
    assert test_module.path_has_trailing_slash('   "C:\\Users\\"  ')
    assert test_module.path_has_trailing_slash('   "C:\\Users\\\\"  ')
    assert not test_module.path_has_trailing_slash('C:\\Users')
    assert test_module.path_has_trailing_slash('C:\\Users ')
    assert test_module.path_has_trailing_slash

# Generated at 2022-06-13 14:57:46.898197
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """
    This unit test uses the unittest module to test the constructor of
    class ShellModule.

    Note:
        This unit test was written after the constructior was added to
        class ShellModule.

    """
    try:
        # Import the unittest module
        import unittest
    except Exception as e:
        print('Skipping test_ShellModule: unittest module not installed: %s'
              % e)
        return

    # Create a TestSuite object derived from unittest.TestCase
    class TestShellModule(unittest.TestCase):
        def setUp(self):
            self.sm = ShellModule()

        def tearDown(self):
            del self.sm

    # Create a suite of tests
    suite = unittest.TestSuite()

# Generated at 2022-06-13 14:57:51.886415
# Unit test for method expand_user of class ShellModule
def test_ShellModule_expand_user():
    shell = ShellModule()
    assert shell.expand_user(user_home_path='~', username='').decode() == "C:\\Users\\<user_name> (Get-Location).Path"
    assert shell.expand_user(user_home_path='~\\test').decode() == "(Get-Location).Path + 'test'"
    assert shell.expand_user(user_home_path='test').decode() == "'test'"

# Generated at 2022-06-13 14:57:56.138770
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule('/dev/null')
    assert 'ShellModule' == shell.__class__.__name__
    assert 'powershell' == shell.SHELL_FAMILY
    assert 'Windows' == shell.DEFAULT_SHELL_TYPE

# Generated at 2022-06-13 14:57:59.500707
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    module = ShellModule()
    assert re.match(r"^mkdir \S*$", module.mkdtemp())
    assert re.match(r"^mkdir \S*$", module.mkdtemp(tmpdir='/tmp'))

# Generated at 2022-06-13 14:58:08.073909
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible_collections.ansible.powershell.plugins.module_utils.common.module_common import PS_PYTHONIOENCODING

    # Use test data from Ansible's
    test_data = {
        None: r'ansible\local\TMPDIR\ansible-tmp-\ansible-tmp-1517892534.02-27452628399122',
        'test/': r'test/ansible-tmp-\ansible-tmp-1517892534.02-27452628399122',
    }

# Generated at 2022-06-13 14:58:11.965159
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    file_name = 'test.txt'
    expected_result = 'test.txt.ps1'

    shell_module = ShellModule()
    result = shell_module.get_remote_filename(file_name)

    assert result == expected_result


# Generated at 2022-06-13 14:58:17.798705
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sm = ShellModule()
    assert sm.shell_type == 'powershell'
    assert sm.SHELL_FAMILY == 'powershell'

    sm = ShellModule(None)
    sm.SHELL_FAMILY = 'powershell'
    assert sm.shell_type == 'powershell'
    assert sm.SHELL_FAMILY == 'powershell'



# Generated at 2022-06-13 14:58:27.598947
# Unit test for method get_remote_filename of class ShellModule
def test_ShellModule_get_remote_filename():
    # _SHELL_AND, _SHELL_REDIRECT_ALLNULL and COMPATIBLE_SHELLS are not set
    shell = ShellModule()
    # Test for file path
    assert shell.get_remote_filename('/path/to/file.exe') == 'file.exe'
    assert shell.get_remote_filename('/path/to/file.ps1') == 'file.ps1'
    assert shell.get_remote_filename('/path/to/file.bat') == 'file.ps1'
    assert shell.get_remote_filename('/path/to/file') == 'file.ps1'
    assert shell.get_remote_filename('file.exe') == 'file.exe'
    assert shell.get_remote_filename('file.ps1') == 'file.ps1'
    assert shell.get

# Generated at 2022-06-13 14:58:30.036421
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert 'powershell' == module.SHELL_FAMILY
    assert 'powershell' not in module.COMPATIBLE_SHELLS
    assert not module._IS_WINDOWS



# Generated at 2022-06-13 14:58:30.633303
# Unit test for constructor of class ShellModule
def test_ShellModule():
    x = ShellModule()

# Generated at 2022-06-13 14:58:37.631565
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    module = ShellModule()
    assert module.mkdtmp('basefile') == '''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('$env:TEMP')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'basefile'
        Write-Output -InputObject $tmp.FullName
        '''
    assert module.mkdtmp('basefile', tmpdir="/testdir") == '''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('/testdir')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'basefile'
        Write-Output -InputObject $tmp.FullName
        '''



# Generated at 2022-06-13 14:58:44.182317
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert None is not module
    assert [] == module.COMPATIBLE_SHELLS
    assert "powershell" == module.SHELL_FAMILY

    module = ShellModule()
    assert NotImplementedError == module.chmod("", "")
    assert NotImplementedError == module.chown("", "")
    assert NotImplementedError == module.set_user_facl("", "", "")
    assert NotImplementedError == module.remove("", False)
    #test_ShellModule_mkdtemp()
    assert NotImplementedError == module.expand_user("")
    assert NotImplementedError == module.exists("")
    assert NotImplementedError == module.checksum("")
    assert NotImplementedError == module.build_module_command

# Generated at 2022-06-13 14:58:47.580428
# Unit test for constructor of class ShellModule
def test_ShellModule():
    conn = ShellModule()
    assert hasattr(conn, 'get_option')
    assert hasattr(conn, 'set_option')
    assert hasattr(conn, 'run')
    assert hasattr(conn, 'run_command')
    assert hasattr(conn, 'put_file')
    assert hasattr(conn, 'fetch_file')
    assert hasattr(conn, 'close')
    assert isinstance(conn, object)


# Generated at 2022-06-13 14:58:58.446042
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():

    # value of shebang
    shebang = '#!powershell'

    # list of powershell commands
    cmd_parts = ['Get-Process', '-Name', 'notepad']

    shell = ShellModule(connection=None)

    # Check when shebang is set and module name has '.ps1' extension
    cmd = shell.build_module_command('', shebang, ' '.join(cmd_parts))
    assert cmd == "type 'Get-Process.ps1' | %s" % shell._encode_script(script=shell.bootstrap_wrapper, strict_mode=False, preserve_rc=False)

    # Set shebang to some other value
    shebang = '#!/usr/bin/env python'

    # Check when shebang is set and module name does not have '.ps1' extension
    cmd = shell.build_module

# Generated at 2022-06-13 14:59:12.635440
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    shellmodule_obj = ShellModule(None)

    # Case 1: basefile is empty
    # Expected: basefile is random generated
    result = shellmodule_obj.mkdtemp(basefile='')
    assert 'tmp' in result

    # Case 2: basefile is not None
    # Expected: basefile is not random generated
    result = shellmodule_obj.mkdtemp(basefile='test')
    assert 'test' in result

    # Case 3: tmpdir is not None
    # Expected: basefile is in tmpdir
    result = shellmodule_obj.mkdtemp(basefile='test', tmpdir='c:')
    assert 'c:\\test' in result



# Generated at 2022-06-13 14:59:18.021112
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    shell = ShellModule()
    path = 'C:\\temp\\test_shell.ps1'
    result = shell.path_has_trailing_slash(path)
    assert not result

    path = 'C:\\temp\\'
    result = shell.path_has_trailing_slash(path)
    assert result

# Generated at 2022-06-13 14:59:28.173482
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import tempfile
    from ansible.errors import AnsibleError
    from ansible.plugins.shell.powershell import ShellModule
    from ansible.release import __version__ as ansible_version
    from ansible.utils.path import makedirs_safe
    import os

    # Create a temporary directory
    tmp = tempfile.mkdtemp(prefix='ansible-tmp-test_')

    # Create a test temp directory

# Generated at 2022-06-13 14:59:38.051542
# Unit test for method build_module_command of class ShellModule

# Generated at 2022-06-13 14:59:45.304014
# Unit test for constructor of class ShellModule
def test_ShellModule():
    winrm_plugin = 'winrm'
    psrp_plugin = 'psrp'
    test_shell_powershell = ShellModule(connection=winrm_plugin)
    assert test_shell_powershell is not None
    test_shell_powershell = ShellModule(connection=psrp_plugin)
    assert test_shell_powershell is not None
    test_shell_powershell = ShellModule(connection='ssh')
    assert test_shell_powershell is not None


# Generated at 2022-06-13 14:59:54.851994
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    # Windows paths must be quoted
    assert ShellModule().path_has_trailing_slash(r'C:\Temp')
    assert ShellModule().path_has_trailing_slash(r'"C:\Temp"')
    assert not ShellModule().path_has_trailing_slash(r'"C:\Temp\\"')

    # Allow Windows paths to be specified using either slash.
    assert ShellModule().path_has_trailing_slash(r'\\server\share\directory\\')
    assert ShellModule().path_has_trailing_slash(r'\\server\share\directory/')
    assert not ShellModule().path_has_trailing_slash(r'\\server\share\directory')

# Generated at 2022-06-13 14:59:56.421317
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Unit test to test the constructor of class ShellModule"""
    assert ShellModule is not None

# Generated at 2022-06-13 15:00:07.554590
# Unit test for method build_module_command of class ShellModule
def test_ShellModule_build_module_command():
    shell = ShellModule(connection=None, playbook=None, runner=None)
    env_string = '$env:b="2";'
    shebang = '#!powershell'
    cmd = '/usr/bin/python'
    arg_path = 'test_ShellModule_build_module_command.tmp'
    module_cmd = shell.build_module_command(env_string, shebang, cmd, arg_path)
    print(module_cmd)

# Generated at 2022-06-13 15:00:09.593436
# Unit test for constructor of class ShellModule
def test_ShellModule():
    try:
        ShellModule()
    except NameError:
        return 'FAILURE'
    else:
        return 'SUCCESS'


# Generated at 2022-06-13 15:00:17.896114
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    # Test with a standard Windows absolute path:
    pathtotest = 'c:\\windows\\system32\\drivers\\etc\\'
    check = ShellModule()
    assert check.path_has_trailing_slash(pathtotest)

    # Test with a Windows path with a trailing slash that is escaped:
    pathtotest = 'c:\\windows\\system32\\drivers\\etc\\\\'
    assert check.path_has_trailing_slash(pathtotest)

    # Test with a Windows path without a trailing slash that is escaped:
    pathtotest = 'c:\\windows\\system32\\drivers\\etc\\\\\\'
    assert not check.path_has_trailing_slash(pathtotest)

    # Test with a Windows path that has a Slash but is not a UNC path.
    pathtotest

# Generated at 2022-06-13 15:00:32.170629
# Unit test for constructor of class ShellModule
def test_ShellModule():

    shebang = '#!powershell'
    wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")
    # expected output of the entire .ps1 file
    wrapper_b64 = to_text(base64.b64encode(wrapper.encode('utf-16-le')), 'utf-8')
    expected_list = _common_args + ['-EncodedCommand', wrapper_b64]
    expected_cmd = ' '.join(expected_list)

    # Test the constructor
    pobj = ShellModule('winrm', 'remote')
    # verify the commands equal
    assert pobj._encode_script(wrapper, as_list=True) == expected_list
    assert pobj._encode_script(wrapper) == expected_cmd

    # Test the constructor with a

# Generated at 2022-06-13 15:00:36.935719
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    s = ShellModule()
    s.get_option = lambda *args, **kwargs: ''

    result = s.mkdtemp()
    assert result.startswith('& ')
    assert result.endswith('; exit $LASTEXITCODE')

    result = s.mkdtemp('', '')
    assert result.startswith('& ')
    assert result.endswith('; exit $LASTEXITCODE')



# Generated at 2022-06-13 15:00:43.436123
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    class SM(ShellModule):

        def _low_level_exec_command(self, cmd, sudoable=True):
            self._exec_command_result = cmd

        def __init__(self, *args, **kwargs):
            self._exec_command_result = None
            super(SM, self).__init__(*args, **kwargs)

    # Test args with dashes
    s = SM()
    s.mkdtemp(basefile='foo-bar', tmpdir='C:\\TEMP\\foo-baz')

# Generated at 2022-06-13 15:00:54.143471
# Unit test for constructor of class ShellModule
def test_ShellModule():
    #Check function - ShellModule()
    obj = ShellModule(connection=None)
    assert obj.SHELL_FAMILY == 'powershell'

    #Check function - join_path()
    assert obj.join_path('foo', 'bar') == r'foo\bar'
    assert obj.join_path('foo/', 'bar') == r'foo\bar'
    assert obj.join_path('foo\\', 'bar') == r'foo\bar'
    assert obj.join_path('foo\\', 'bar') == r'foo\bar'

# Generated at 2022-06-13 15:01:01.383896
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    data = to_bytes('''{"STDOUT_LINES": ["C:\\Users\\patrik.dahlen-2\\AppData\\Local\\Temp\\AnsiballZ_ShellModule_3270d5b5a5e5c8d8.patrik.dahlen-2"], "CHANGED": true}''')
    result = _parse_clixml(data, stream="Output")
    assert result == b"C:\\Users\\patrik.dahlen-2\\AppData\\Local\\Temp\\AnsiballZ_ShellModule_3270d5b5a5e5c8d8.patrik.dahlen-2"



# Generated at 2022-06-13 15:01:02.321325
# Unit test for constructor of class ShellModule
def test_ShellModule():
    assert ShellModule()._IS_WINDOWS

# Generated at 2022-06-13 15:01:09.649518
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test error handling
    from ansible.errors import AnsibleError
    try:
        sm = ShellModule()
        sm.run_command('Test')
        assert False
    except AnsibleError:
        assert True
    except Exception:
        assert False
    try:
        sm = ShellModule()
        sm.run_command('Test', binary_data=True)
        assert False
    except AnsibleError:
        assert True
    except Exception:
        assert False



# Generated at 2022-06-13 15:01:16.771944
# Unit test for constructor of class ShellModule
def test_ShellModule():
    return ShellModule()

if __name__ == '__main__':
    import sys
    import unittest
    import re

    sys.modules['ansible.module_utils.basic'] = __import__('ansible.module_utils.basic')
    from ansible.module_utils.common.process import AnsibleProcess

    class MyTestCase(unittest.TestCase):

        def setUp(self):
            self.psm = ShellModule()

        def check_expected_command(self, cmd_parts, expected):
            '''
            Checks the command to ensure it matches the expected cmd_list passed in.
            Any of the actual cmd_list elements can match the corresponding expected cmd_list element
            via a regex

            :param cmd_parts:
            :param expected:
            :return:
            '''

# Generated at 2022-06-13 15:01:18.178662
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module is not None

# Generated at 2022-06-13 15:01:26.707019
# Unit test for constructor of class ShellModule
def test_ShellModule():
    powershell_plugin = ShellModule()

    # Common shell filenames that this plugin handles
    powershell_plugin.COMPATIBLE_SHELLS
    assert powershell_plugin.COMPATIBLE_SHELLS == frozenset()

    # Family of shells this has.  Must match the filename without extension
    powershell_plugin.SHELL_FAMILY
    assert powershell_plugin.SHELL_FAMILY == 'powershell'

    # Used by various parts of Ansible to do Windows specific changes
    powershell_plugin._IS_WINDOWS
    assert powershell_plugin._IS_WINDOWS is True

# Generated at 2022-06-13 15:01:32.060161
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule()

# pylint: disable=unused-argument

# Generated at 2022-06-13 15:01:42.197395
# Unit test for constructor of class ShellModule
def test_ShellModule():

    s = ShellModule()

    # Test chmod

# Generated at 2022-06-13 15:01:45.127246
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    module = ShellModule()
    assert module.mkdtemp() == module._encode_script(script='''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('{tmpdir}')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'ansible-tmp-*'
        Write-Output -InputObject $tmp.FullName
        '''.strip())

# Generated at 2022-06-13 15:01:48.886776
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    from ansible.modules.shell import ShellModule

    shell_module = ShellModule()

    assert shell_module.path_has_trailing_slash('C:\Temp\\') == True
    assert shell_module.path_has_trailing_slash('C:\Temp\\') == True
    assert shell_module.path_has_trailing_slash('C:\Temp\ ') == False
    assert shell_module.path_has_trai

# Generated at 2022-06-13 15:01:55.644364
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    sm = ShellModule()
    assert sm.path_has_trailing_slash('c:\\foo') == False
    assert sm.path_has_trailing_slash('c:\\foo\\') == True
    assert sm.path_has_trailing_slash('c:\\foo/') == True
    assert sm.path_has_trailing_slash('c:\\foo\\bar\\') == True
    assert sm.path_has_trailing_slash('c:\\foo\\bar/') == True

# Generated at 2022-06-13 15:02:03.725840
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.playbook.neighbor_loader import AnsibleLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import connection_loader

    from ansible.plugins.loader import module_loader
    module_loader._find_plugins()
    connection_loader._find_plugins()

    results_callback = AnsibleLoader()
    inventory = AnsibleLoader().load_from_file('test/unit/ansible/inventory/inventory_v2')

# Generated at 2022-06-13 15:02:11.121641
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import json
    import tempfile
    from shutil import rmtree
    path = None
    try:
        handle, path = tempfile.mkstemp(text=True, suffix='.ps1')
        os.write(handle, to_bytes("Write-Host foo"))
        os.close(handle)
        shell = ShellModule(connection=None, ansible_ssh_executable=None, become_method=None, become_exe=None, become_user=None)
        rc, out, err = module_execute(shell, path, "", "", "", "", "", "")
        assert rc == 0
        assert out == "foo"
        assert err == ""
    finally:
        if path:
            os.remove(path)


# Generated at 2022-06-13 15:02:17.266949
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Basic test with default arguments
    s = ShellModule()
    # Make sure body of the module is created properly with default arguments
    assert s.build_module_command(env_string=None, shebang=None, cmd='') == '& (Set-StrictMode -Version Latest); exit $LASTEXITCODE', 'ShellModule should instantiate with default arguments'

# Generated at 2022-06-13 15:02:24.158285
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # Test for assign the disconnect_timeout to class variable
    disconnect_timeout = '5.5'

    # Test for creating ShellModule object
    obj1 = ShellModule(disconnect_timeout=disconnect_timeout)
    assert obj1.disconnect_timeout == 5.5

    # Test for creating ShellModule object
    obj2 = ShellModule('5.5')
    assert obj2.disconnect_timeout == 5.5

    # Test the disconnect_timeout is None
    obj3 = ShellModule()
    assert obj3.disconnect_timeout is None

# Generated at 2022-06-13 15:02:28.251388
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule(connection=None, play_context=None)
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_module._SHELL_AND == ';'
    assert shell_module.CHARS_TO_ESCAPE_FOR_POWERSHELL == []
    assert shell_module._IS_WINDOWS == True

# Generated at 2022-06-13 15:02:38.529288
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import json
    import imp
    import tempfile
    fd, path = tempfile.mkstemp(suffix='ansible_test')
    with open(path, 'w') as ifs:
        ifs.write('#!python\nprint("Hello World")')
    os.chmod(path, 0o755)
    sm = imp.load_source('*test_shell_module', path)
    module = ShellModule(connection=None)
    json_msg = json.loads(module.build_module_command(module.env_prefix(), '#!python', path))
    assert json_msg['module_name'] == 'shell'
    assert len(json_msg['module_args']) > 1
    assert json_msg['module_args'].startswith("python")

# Generated at 2022-06-13 15:02:47.910059
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import pkg_resources
    import shutil
    import tempfile

    cmd = pkg_resources.resource_string("ansible.executor.powershell", "bootstrap_wrapper.ps1").decode("utf-8")
    tempdir = ntpath.normpath(tempfile.mkdtemp(prefix='ansible-test-'))
    cmd = cmd.replace('%TEMP%', tempdir).encode('utf-32-le')
    cmd = 'powershell -NoProfile -NonInteractive -ExecutionPolicy Unrestrictd -EncodedCommand %s' % to_text(base64.b64encode(cmd))
    os.system(cmd)
    assert os.path.isdir(os.path.join(tempdir, 'ansibletest'))
    shutil.rmtree(tempdir)


# Unit

# Generated at 2022-06-13 15:02:54.484853
# Unit test for constructor of class ShellModule
def test_ShellModule():

    # Constructor test without any argument
    shell_object = ShellModule()

    assert shell_object.COMPATIBLE_SHELLS == frozenset()

    assert shell_object.SHELL_FAMILY == 'powershell'

    assert shell_object._IS_WINDOWS == True

    assert shell_object._SHELL_REDIRECT_ALLNULL == '> $null'

    assert shell_object._SHELL_AND == ';'

    # Constructor test with arguments
    shell_object_with_args = ShellModule(shell_executable='/usr/bin/powershell', become_user='my_user')

    assert shell_object_with_args.shell_executable == '/usr/bin/powershell'

    assert shell_object_with_args.become_user == 'my_user'

    assert shell_object_with

# Generated at 2022-06-13 15:02:55.384291
# Unit test for constructor of class ShellModule
def test_ShellModule():
    with ShellModule(ShellBase()) as shell:
        pass


# Generated at 2022-06-13 15:03:02.631416
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ''' shell.ShellModule() constructor'''
    # pylint: disable=attribute-defined-outside-init

    shell = ShellModule()

    # is_windows
    assert shell._IS_WINDOWS

    # family
    assert shell.SHELL_FAMILY == 'powershell'

    # compatible_shells
    assert isinstance(shell.COMPATIBLE_SHELLS, frozenset)
    assert shell.COMPATIBLE_SHELLS == frozenset()

    # common_path_prefix
    assert shell.common_path_prefix == ntpath.commonprefix


# Generated at 2022-06-13 15:03:10.256299
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    s = ShellModule()
    assert s.path_has_trailing_slash('path\\') is True
    assert s.path_has_trailing_slash('path/') is True
    assert s.path_has_trailing_slash('path') is False
    assert s.path_has_trailing_slash('"path\\"') is True
    assert s.path_has_trailing_slash("'path\\'") is True


# Generated at 2022-06-13 15:03:10.748211
# Unit test for constructor of class ShellModule
def test_ShellModule():
    pass

# Generated at 2022-06-13 15:03:12.710167
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # create class object with valid parameters
    module = ShellModule(connection='ssh', no_log=True)
    assert module != None

# Generated at 2022-06-13 15:03:17.105874
# Unit test for constructor of class ShellModule
def test_ShellModule():
    obj = ShellModule(connection=None)
    assert obj.SHELL_FAMILY == 'powershell'
    assert obj._IS_WINDOWS == True
    assert obj._SHELL_REDIRECT_ALLNULL == '> $null'
    assert obj._SHELL_AND == ';'
    assert obj.COMPATIBLE_SHELLS == frozenset()

# Generated at 2022-06-13 15:03:23.669407
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    '''
    Return a remote temporary directory path.
    - basefile: basename required
    - system: ignored
    - mode: ignored
    - tmpdir: temporary directory required
    '''

    ShellMod = ShellModule()

    def test_mkdtemp(basefile, tmpdir):
        # Create a remote temporary directory
        cmd = ShellMod.mkdtemp(basefile, tmpdir=tmpdir)
        assert cmd.startswith("$tmp_path = [System.Environment]::ExpandEnvironmentVariables('%s')" % tmpdir)
        assert cmd.endswith("$tmp = New-Item -Type Directory -Path $tmp_path -Name '%s'" % basefile)


    # Test a temporary directory with basefile and tmpdir

# Generated at 2022-06-13 15:03:35.826488
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():

    import tempfile

    class MockExecutor(object):
        class connection(object):
            host = 'localhost'
            port = None

        tmpdir = tempfile.gettempdir()

    exec_obj = MockExecutor()
    powershell_obj = ShellModule(exec_obj)

    res = powershell_obj.mkdtemp()

    # We want res to be the last line of the script.
    # We should always have a last line
    assert res[-1] == b'\n'

    # We should have leading two lines of the script
    assert res[0] == b'\n'
    assert res[1:].startswith(b'$tmp = New-Item')

    # We should end in a script that writes output with the path

# Generated at 2022-06-13 15:03:39.300684
# Unit test for constructor of class ShellModule
def test_ShellModule():
    module = ShellModule()
    assert module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert module._SHELL_AND == ';'
    assert module.SHELL_FAMILY == 'powershell'



# Generated at 2022-06-13 15:03:42.032871
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS == True


# Generated at 2022-06-13 15:03:51.247874
# Unit test for constructor of class ShellModule
def test_ShellModule():

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.stats import AggregateStats
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    play_context.connection = 'local'

    # Define a DataLoader
    # Play context to be used for the shell_

# Generated at 2022-06-13 15:03:55.089670
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """This testcase is for the constructor of the class ShellModule
       The constructor is triggering the method _executable() from the class ShellBase
       This method is raised an exception by powershell
       This is why we catch this exception  and return the instance
    """
    try:
        sm = ShellModule()
    except Exception:
        return sm



# Generated at 2022-06-13 15:04:00.022491
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell = ShellModule()
    assert shell.COMPATIBLE_SHELLS == frozenset()
    assert shell.SHELL_FAMILY == 'powershell'
    assert shell._IS_WINDOWS == True
    assert shell.get_remote_filename(r"C:\test\test.exe") == "test.exe"
    assert shell.get_remote_filename(r"C:\test\test") == "test.ps1"

# Generated at 2022-06-13 15:04:01.118975
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ShellModule(command_name='shell')


# Generated at 2022-06-13 15:04:05.710436
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    # PowershellModule has been designed to be used in a subclass fashion only
    # and a very simple test can be ran with this call
    module = ShellModule(connection=None)
    # mkdtemp is a method of ShellModule
    # it returns a string with a script that create a temporary directory
    res = module.mkdtemp('tmpdir')
    assert isinstance(res, str)
    assert res.startswith('IAAAAHV4')
    # a string is returned, but it is base64 encoded, so we decode it
    # to be able to read what is in the script
    dec = base64.b64decode(res.encode('ascii'))

# Generated at 2022-06-13 15:04:07.131639
# Unit test for constructor of class ShellModule
def test_ShellModule():
    # pylint: disable=unused-variable
    mod = ShellModule()
    assert mod.SHELL_FAMILY == 'powershell'

# Generated at 2022-06-13 15:04:12.046126
# Unit test for constructor of class ShellModule
def test_ShellModule():
    ''' shell: powershell unit test for constructor of class ShellModule '''
    # We are creating a shell module object for powershell
    # this is to test the object's constructor
    powershell_shell_module = ShellModule()
    assert isinstance(powershell_shell_module, ShellBase)



# Generated at 2022-06-13 15:04:23.984756
# Unit test for constructor of class ShellModule
def test_ShellModule():
    shell_module = ShellModule()
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_module._SHELL_AND == ';'
    assert shell_module._IS_WINDOWS


# Generated at 2022-06-13 15:04:30.880911
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    b_slash = '\\'
    f_slash = '/'
    file_path = 'name'
    file_path_b_slash = 'name' + b_slash
    file_path_f_slash = 'name' + f_slash
    assert ShellModule().path_has_trailing_slash(file_path) is False
    assert ShellModule().path_has_trailing_slash(file_path_b_slash) is True
    assert ShellModule().path_has_trailing_slash(file_path_f_slash) is True

# Generated at 2022-06-13 15:04:36.740541
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    paths = [
        '\\',
        'C:\\',
        'C:\\Temp\\',
        'C:\\Temp',
        '\\Temp\\',
        '\\Temp',
        '~\\Temp\\',
        '~\\Temp'
    ]

    shell = ShellModule()

    for path in paths:
        assert shell.path_has_trailing_slash(path) == ((path in ('\\', 'C:\\', '\\Temp\\', '~\\Temp\\')))

# Generated at 2022-06-13 15:04:45.436329
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import tempfile
    module = ShellModule()
    tempdir = tempfile.gettempdir()
    module._IS_WINDOWS = True
    assert module.mkdtemp(basefile=None, system=False, mode=None, tmpdir=tempdir) == module._encode_script('''
        $tmp_path = [System.Environment]::ExpandEnvironmentVariables('%s')
        $tmp = New-Item -Type Directory -Path $tmp_path -Name 'ansible-tmp-*'
        Write-Output -InputObject $tmp.FullName
        ''' % tempdir, strict_mode=False)

    # Test that the second and subsequent calls generate a different random name
    # Use a name with a short prefix because long prefixes increase the risk of collisions
    # Note that tempfile.mkdtemp calls mkstemp to generate the temporary

# Generated at 2022-06-13 15:04:54.658510
# Unit test for constructor of class ShellModule
def test_ShellModule():
    """Return a functional test object for testing ShellModule"""
    from ansible.executor.task_executor import TaskExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 15:04:59.562225
# Unit test for method mkdtemp of class ShellModule
def test_ShellModule_mkdtemp():
    import __main__
    __main__.shell = ShellModule()
    # Test 1 - If the basefile is specified, the temp file should be created
    # in the user's temp directory
    assert __main__.shell.mkdtemp(basefile='mytmpfile')[-8:] == 'mytmpfile'
    # Test 2 - If the basefile is omitted, the temp file should be created in
    # the user's temp directory with a random filename
    assert __main__.shell.mkdtemp()[-10:] == 'tmpXXXXXXXX'

# Generated at 2022-06-13 15:05:06.455747
# Unit test for method path_has_trailing_slash of class ShellModule
def test_ShellModule_path_has_trailing_slash():
    from ansible.plugins.shell.powershell import ShellModule
    import os

    # Test with forward slash
    path = "C:/"
    sm = ShellModule()
    assert sm.path_has_trailing_slash(path) is True
    path = "C:\\"
    sm = ShellModule()
    assert sm.path_has_trailing_slash(path) is True

    # Test without trailing slash
    path = "C:"
    sm = ShellModule()
    assert sm.path_has_trailing_slash(path) is False

    # Test with drive relative path
    path = ".\\"
    sm = ShellModule()
    assert sm.path_has_trailing_slash(path) is True

    # Test with backslash
    path = "C:\\Program Files\\"

# Generated at 2022-06-13 15:05:11.955778
# Unit test for constructor of class ShellModule
def test_ShellModule():
    sut = ShellModule()
    assert sut.COMPATIBLE_SHELLS == frozenset()
    assert sut.SHELL_FAMILY == 'powershell'
    assert sut._IS_WINDOWS is True
    assert sut.DEFAULT_EXECUTABLE is None


# Generated at 2022-06-13 15:05:21.212017
# Unit test for constructor of class ShellModule
def test_ShellModule():
    import ansible.executor.powershell as powershell

    def execute_module(self, connection, tmp=None, module_name=None, module_args=None, inject=None, complex_args=None, **kwargs):
        pass


# Generated at 2022-06-13 15:05:29.598837
# Unit test for constructor of class ShellModule
def test_ShellModule():
    from ansible.module_utils.six import PY2
    python_shell = ShellModule()

    # Test for is_windows
    assert python_shell._IS_WINDOWS

    # Test for checksum
    checksum_cmd = python_shell.checksum('/fake_dir/fake_file.txt')
    if PY2:
        checksum_cmd = checksum_cmd.encode('utf-8')


# Generated at 2022-06-13 11:29:27.278688
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    bm = BecomeModule()
    bm.prompt = ''
    bm._id = '1337'

    # Test 1
    bm.get_option = lambda key: 'root' if key == 'become_user' else ''
    bm.get_option.side_effect = None
    bm.name = 'sudo'
    bm.get_option = lambda key: 'sudo -H -n' if key == 'become_flags' else ''
    bm.get_option.side_effect = None
    bm.get_option = lambda key: 'sudo' if key == 'become_exe' else ''
    bm.get_option.side_effect = None
    bm.get_option = lambda key: 'echo' if key == 'become_pass' else ''
    bm.get_

# Generated at 2022-06-13 11:29:34.897315
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    bm = BecomeModule('sudo')
    bm.prompt = ''
    test_cmd = 'test_command'
    shell = True
    test_command_str = 'sudo -H -n -S -u %s %s' % (bm.get_option('become_user') or '', test_cmd)
    assert bm.build_become_command(test_cmd, shell) == test_command_str
    bm.set_option('become_flags', '-H')
    test_command_str = 'sudo -H -S -u %s %s' % (bm.get_option('become_user') or '', test_cmd)
    assert bm.build_become_command(test_cmd, shell) == test_command_str

# Generated at 2022-06-13 11:29:41.845337
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test non-empty cmd
    cmd = "echo 'hello world'"
    shell = "/bin/sh"

    become_module = BecomeModule()
    become_module._id = "abcdef"

    become_module.get_option = lambda option: None
    result_empty = become_module.build_become_command(cmd, shell)
    assert result_empty == "/bin/sh -c 'echo 'hello world''"

    become_module.get_option = lambda option: 'sudo'
    result_become_exe = become_module.build_become_command(cmd, shell)
    assert result_become_exe == "sudo /bin/sh -c 'echo 'hello world''"

    become_module.get_option = lambda option: None
    become_module.prompt = ''
    become_module._build_

# Generated at 2022-06-13 11:29:50.694422
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    cmd = 'shell_command'
    expected_cmd = 'sudo -H -S -n -p "[sudo via ansible, key=%s] password:" -u johndoe shell_command' % (become_module._id)
    become_module.get_option = lambda option: {
        'become_exe': 'sudo',
        'become_flags': '-H -S -n',
        'become_user': 'johndoe',
        'become_pass': True,
    }[option]

    actual_cmd = become_module.build_become_command(cmd, 'shell')

    assert actual_cmd == expected_cmd

# Generated at 2022-06-13 11:29:57.572979
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    # Test case 1
    plugin = BecomeModule()
    plugin.set_options(direct=dict(become_exe='sudo'))
    plugin.set_options(direct=dict(become_flags='-b'))
    plugin.set_options(direct=dict(become_prompt='[sudo via ansible, key=%s] password:'))
    plugin.set_options(direct=dict(become_user='root'))
    plugin.set_options(direct=dict(become_pass=''))
    sudo_cmd = plugin.build_become_command('whoami', 'shell')
    assert sudo_cmd == 'sudo -b -u root (whoami)'

    # Test case 2
    plugin = BecomeModule()
    plugin.set_options(direct=dict(become_exe='sudo'))
    plugin

# Generated at 2022-06-13 11:30:05.751812
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test with become_flags.
    become_plugin = BecomeModule(become_options=dict(become_flags='-H -S -n'))
    result = become_plugin.build_become_command('ls', False)
    assert result == 'sudo -H -S -n ls'

    # Test with default become_flags.
    become_plugin = BecomeModule(become_options=dict())
    result = become_plugin.build_become_command('ls', False)
    assert result == 'sudo -H -S -n ls'

    # Test with become_exe.
    become_plugin = BecomeModule(become_options=dict(become_exe='doas'))
    result = become_plugin.build_become_command('ls', False)

# Generated at 2022-06-13 11:30:12.195443
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test options
    options = dict(
        become_exe = 'sudo',
        become_flags = '-H -S -n',
        become_pass = False,
        become_user = 'root',
    )

    # Test some commands
    cmds = [
        'id',
        'id ',
        'id --gid  ',
        'id --gid --group',
        'echo "foo"',
    ]

    # Test success commands

# Generated at 2022-06-13 11:30:16.685864
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    '''AnsibleModule_BecomeModule_build_become_command.py
    Unit test for method build_become_command of class BecomeModule
    '''

    become_exe = 'sudo'
    become_flags = '-H -S -n'
    become_pass = ''
    become_user = 'root'
    cmd = 'foo'
    shell = '/bin/sh'
    prompt = None

    # with empty password, no prompt, no user
    expected_result = become_exe + ' ' + become_flags + ' ' + cmd
    become_module = BecomeModule()
    become_module.get_option = lambda opt: None
    become_module.prompt = prompt
    become_module.name = become_exe
    result = become_module.build_become_command(cmd, shell)

# Generated at 2022-06-13 11:30:26.499066
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    module = BecomeModule()

    # Test 1
    # set become_pass=True, become_user=None and become_flags=[-H]
    module.options = {'become_pass': True, 'become_user': None, 'become_flags': ['-H']}
    module.prompt = None
    module._id = 3
    assert module.build_become_command('/bin/ls', 'sh') == 'sudo -H -p "[sudo via ansible, key=3] password:" /bin/ls && echo BECOME-SUCCESS-jvahftuo'

    # Test 2
    # set become_pass=False, become_user=root and become_flags=['-n']

# Generated at 2022-06-13 11:30:36.470532
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    bm = BecomeModule()
    bm.become_exe = 'sudo'
    bm.become_flags = '-H -S -n'
    bm.become_pass = None
    bm.become_user = 'testuser'

    # test with a shell
    cmd = 'ls /tmp'
    shell = "bash"
    assert bm.build_become_command(cmd, shell) == 'sudo -H -S -n -u testuser bash -c \'%s\'' % bm._build_success_command(cmd, shell)

    # test without a shell
    cmd = 'cat /tmp/testfile.txt'

# Generated at 2022-06-13 11:30:50.640141
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import os

    class Options(object):
        def __init__(self, **args):
            self.__dict__.update(args)

    def set_get_option(module, command, **args):
        '''
        Set options on a module instance, then run the build_become_command() method and return result
        '''
        module._options = Options(**args)
        return module.build_become_command(command, '')

    # Set global environment variable to test so shell does not find it
    os.environ['ANSIBLE_BECOME_EXE'] = 'not-sudo'

    # Test the options
    obj = BecomeModule()

    assert 'sudo echo hi' == set_get_option(obj, 'echo hi')

    # Test become_user

# Generated at 2022-06-13 11:31:04.904699
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    def call_build_become_command(c, shell=True):
        # Test arguments:
        #   cmd: The command to be become with (the 'intended command')
        #   shell: Whether to run in a shell or not
        # Returns the become command (str)
        bbm = BecomeModule()
        bbm.prompt = '[sudo via ansible, key=1] password:'
        bbm.shared_loader_obj = None
        return bbm.build_become_command(c, shell=shell)

    # Identity (no command)
    assert call_build_become_command(None) == None

    # Identity (empty command)
    assert call_build_become_command('') == ''

    # Identity (some command)

# Generated at 2022-06-13 11:31:11.794000
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    mock_become_exe = 'sudo'
    mock_become_flags = '-H -S -n'
    mock_become_user = 'root'
    mock_become_pass = 'my_password'
    mock_cmd = 'whoami'
    mock_shell = '/bin/sh'
    mock_prompt = '[sudo via ansible, key=%s] password:' % '1234'

    # Test for password prompt
    test_module = BecomeModule()
    test_module.set_options(become_exe=mock_become_exe,
                            become_flags=mock_become_flags,
                            become_user=mock_become_user,
                            become_pass=mock_become_pass)
    test_module.prompt = mock_prompt
   

# Generated at 2022-06-13 11:31:16.372864
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_args = {
        'become_exe': 'do-exec',
        'become_flags': '-H -S -n',
        'become_pass': False,
        'become_user': 'username',
    }

    cmd_exe = 'do-exec -H -S -n -u username SHELL_CMD'
    cmd_sh = 'do-exec -H -S -n -u username SHELL_CMD'
    cmd_csh = 'do-exec -H -S -n -u username SHELL_CMD'
    cmd_fish = 'do-exec -H -S -n -u username SHELL_CMD'
    cmd_powershell = 'do-exec -H -S -n -u username SHELL_CMD'

# Generated at 2022-06-13 11:31:23.105690
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule()
    # These tests assume the default settings, so the first part of the
    # become command tests the full command and the optional second part
    # tests when the password is set.

# Generated at 2022-06-13 11:31:32.760725
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule()
    module.get_option = lambda x: None
    module._id = ''
    module._build_success_command = lambda x, y: x
    module.prompt = '<prompt>'

    # empty cmd
    assert module.build_become_command('', '/bin/sh') is None

    module._id = '<id>'
    # no password, no user
    res = module.build_become_command('<cmd>', '/bin/sh')
    assert res == 'sudo -H -S <cmd>'

    # no password, with user
    module.get_option = lambda x: '<become_user>' if x == 'become_user' else None
    res = module.build_become_command('<cmd>', '/bin/sh')
    assert res

# Generated at 2022-06-13 11:31:40.536606
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    # default argument test
    cmd = become.build_become_command(cmd=None, shell='/bin/bash')
    assert cmd == None
    # optional argument test
    cmd = become.build_become_command(cmd='ls', shell='/bin/bash')
    assert cmd == 'sudo ls'
    # optional argument test
    cmd = become.build_become_command(cmd='ls', shell='/bin/csh')
    assert cmd == 'sudo ls'

    # optional argument test
    cmd = become.build_become_command(cmd='ls', shell='/bin/csh')
    become.prompt = None
    assert cmd == 'sudo ls'

# Generated at 2022-06-13 11:31:47.597287
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:31:52.308560
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    become_module = BecomeModule()
    become_module.prompt = '[sudo via ansible, key=%s] password:' % "abcd"
    cmd_output = become_module.build_become_command("ls", "False")
    assert cmd_output == "sudo -H -S -p \"{prompt}\" -u ls echo $?"


# Generated at 2022-06-13 11:32:02.713660
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:32:18.889308
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule()
#    module._id = 123
    module.prompt = '[sudo via ansible, key=%s] password:' % module._id
    module.get_option = lambda x: None
    module.get_option.__name__ = 'get_option'

    # cmd is empty string
    cmd = ''
    shell = 'shell'
    assert module.build_become_command(cmd, shell) == ''

    # cmd is None
    cmd = None
    shell = 'shell'
    assert module.build_become_command(cmd, shell) == ''

    # cmd is not empty
    cmd = 'command'
    shell = 'shell'
    assert module.build_become_command(cmd, shell) == 'sudo -p "[sudo via ansible, key=123] password:" "command"'

   

# Generated at 2022-06-13 11:32:28.624598
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    """
    Build sudo command of class BecomeModule:
    """
    def mock_get_option(option):
        """
        Mock method get_option of class BecomeModule:
        """
        return {
            'become_exe': 'sudo',
            'become_flags': '-H -S -n',
            'become_pass': True,
            'become_user': 'root',
        }[option]

    become_module = BecomeModule()
    become_module._build_success_command = lambda cmd, shell: cmd
    become_module.get_option = mock_get_option


# Generated at 2022-06-13 11:32:36.145373
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    fake_super = BecomeBase()  # noqa

    become = BecomeModule(
        module=fake_super,
        become_method='sudo',
        become_exe='/usr/bin/sudo',
        become_user='rstuart',
        become_pass='',
        become_flags='-H -S -n')

    assert become.build_become_command('ls /tmp', 'bash') == '/usr/bin/sudo -H -S -n ls /tmp'

# Generated at 2022-06-13 11:32:46.314590
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    import shutil

    module = BecomeModule('become')
    module.get_option = lambda name: None
    module._id = '7684b4f4-e7c1-4cfb-8dd8-ea08678121d9'
    module._build_success_command = lambda cmd, shell: cmd

    # Test case: cmd is empty
    assert(module.build_become_command('', '/bin/bash') == '')

    # Test case: cmd is not empty and become_pass is empty
    assert(module.build_become_command('ls -l', '/bin/bash') ==
           'sudo -H -S -n /bin/bash -c \'LS_COLORS=""; export LS_COLORS; '
           'command ls -l\'')

    # Test case: cmd is not empty and become_

# Generated at 2022-06-13 11:32:53.580190
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import os
    import tempfile
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils import basic
    from ansible.plugins.become import BecomeBase
    from ansible.plugins.loader import become_loader

    # Setup/teardown test fixtures
    def setUp():
        pass

    def tearDown():
        pass

    def test_basic():
        """ Test basic sudo become_flags """
        # create obj to instance class
        become_base = BecomeBase()

        become_base._options['become_exe'] = 'sudo'
        become_base._options['become_flags'] = '-H -S -n'
        become_base._options['become_user'] = 'root'
        become_base._options['become_pass'] = 'test'

        # create

# Generated at 2022-06-13 11:32:56.731998
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    shell = 'bash'
    cmd = 'echo "Hello World"'

    # Create instance of class
    become_module = BecomeModule()

    # execute tested method
    sudo_cmd = become_module.build_become_command(cmd, shell)

    # assert
    assert sudo_cmd == 'sudo bash -c \'"\'"\'echo "Hello World"\'"\'"\''

# Generated at 2022-06-13 11:33:05.491638
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule('sudo', [])
    become.options = {
        'become_exe': 'sudo',
        'become_flags': '-H',
        'become_pass': '',
        'become_user': '',
        'become_method': 'sudo',
        'become_options': '',
        'become_pass': None,
    }
    r = become._build_success_command('command', '/bin/sh')
    assert r == 'bash -c "unset BASH_ENV; command"'

# Generated at 2022-06-13 11:33:13.563849
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_pass = '12345'
    plugin = BecomeModule()
    plugin.set_options(become_pass=become_pass)
    cmd = 'echo hi'
    expected_cmd = 'sudo -p "%s" -u %s %s' % (plugin.prompt, plugin.get_option('become_user'), plugin._build_success_command(cmd, None))
    actual_cmd = plugin.build_become_command(cmd, None)
    assert actual_cmd == expected_cmd
    plugin.prompt = None
    actual_cmd = plugin.build_become_command(cmd, None)
    assert actual_cmd == cmd

# Generated at 2022-06-13 11:33:24.442731
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
  # Default configuration
  become = BecomeModule(None, dict(become_pass=None, become_exe=None, become_flags=None, become_user=None))

  # Command with shell
  cmd = 'echo hello'
  shell = '/bin/sh -c'
  assert become.build_become_command(cmd, shell) == 'sudo -H -S -n  sh -c echo hello'

  # Command without shell
  cmd = 'echo hello'
  shell = None
  assert become.build_become_command(cmd, shell) == 'sudo -H -S -n  echo hello'

  # Command with shell and become_user
  cmd = 'echo hello'
  shell = '/bin/sh -c'
  become.become_user = 'test'

# Generated at 2022-06-13 11:33:32.278251
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:33:58.402418
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    test_data = {
        'become': {
            'become_exe': 'sudo',
            'become_flags': '-H -S -n',
            'become_pass': '',
            'become_user': 'root'
        },
        'cmd': [
            'echo',
            'hello'
        ],
        'success_cmd': 'echo hello'
    }

    become_module = BecomeModule(play_context=None, new_stdin='', connection=None)
    become_module.prompt = 'sudo password: '
    become_module.get_option = lambda name: test_data['become'][name]


# Generated at 2022-06-13 11:34:11.529214
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    assert become_module.build_become_command('ls') == "sudo -H -S -n ls"
    assert become_module.build_become_command('ls', shell='/bin/sh') == "sudo -H -S -n sh -c 'ls'"
    assert become_module.build_become_command('ls -al') == "sudo -H -S -n ls -al"
    assert become_module.build_become_command('ls -al', shell='/bin/sh') == "sudo -H -S -n sh -c 'ls -al'"
    # test get_option
    assert become_module.get_option('become_exe') == 'sudo'
    assert become_module.get_option('become_flags') == '-H -S -n'


# Generated at 2022-06-13 11:34:14.854271
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule(dict())
    assert isinstance(become_module, BecomeModule)
    assert become_module.build_become_command(cmd='ls') == 'sudo -H -S ls'

# Generated at 2022-06-13 11:34:21.774446
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomemodule = BecomeModule()

    cmd = "echo test"
    shell = "/bin/sh"

    becomemodule.get_option = lambda x: None
    assert becomemodule.build_become_command(cmd, shell) == 'sudo -H -S -n sh -c \'%s\'' % cmd

    # version of ansible < 2.7
    becomemodule.get_option = lambda x: "echo test" if x == 'become_pass' else None
    assert becomemodule.build_become_command(cmd, shell) == 'sudo -H -S -n -p "test" sh -c \'%s\'' % cmd

    # version of ansible >= 2.7
    becomemodule.get_option = lambda x: "test" if x == 'become_user' else None
    assert becomemodule.build_become

# Generated at 2022-06-13 11:34:28.006804
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test without become_pass and without become_user
    become = BecomeModule()
    become.get_option = lambda x: None
    assert become._build_success_command("echo 'hello'", 'sh') == "echo 'hello'"
    result = become.build_become_command("echo 'hello'", 'sh')
    assert result == "sudo echo 'hello'"

    # Test with become_user but without become_pass
    become = BecomeModule()
    become.get_option = lambda x: None
    become.get_option = lambda x: 'myuser' if x == 'become_user' else None
    result = become.build_become_command("echo 'hello'", 'sh')
    assert result == "sudo -u myuser echo 'hello'"

    # Test without become_user with become_pass
    become = Become

# Generated at 2022-06-13 11:34:37.529559
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(become_user='run_as_me')

    # Method does not change passed command if no become options configured
    cmd = 'pwd'
    assert become.build_become_command(cmd, None) == cmd

    # Method sets default become_exe if no become options configured
    become = BecomeModule(become_user='run_as_me', become_exe='sudo')

# Generated at 2022-06-13 11:34:44.254438
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()

    result = become.build_become_command('ls -l', False)
    assert result == 'sudo -H -S -n ls -l'

    result = become.build_become_command('ls -l', False, become_exe='CAN_CALL_SUDO')
    assert result == 'CAN_CALL_SUDO -H -S -n ls -l'

    result = become.build_become_command('ls -l', False, become_user='F_IS_USER')
    assert result == 'sudo -H -S -n -u F_IS_USER ls -l'

    result = become.build_become_command('ls -l', False, become_flags='')
    assert result == 'sudo ls -l'

    result = become.build_become_command

# Generated at 2022-06-13 11:34:59.098769
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    mod = BecomeModule()

    # Tests for cmd
    assert mod.build_become_command(None, None) is None
    assert mod.build_become_command('cmd', None) == 'cmd'

    # Tests for shell
    assert mod.build_become_command('cmd', 'shell') == 'cmd'

    # Tests basic sudo
    become_exe = ''
    become_flags = ''
    become_user = ''
    assert mod.build_become_command('cmd', None) == 'sudo -H -S -n cmd'

    # Tests sudo user
    become_exe = ''
    become_flags = ''
    become_user = 'noshell'
    assert mod.build_become_command('cmd', None) == 'sudo -H -S -n -u noshell cmd'

    # Tests sudo password


# Generated at 2022-06-13 11:35:06.771630
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # GIVEN
    become_module = BecomeModule()

    # WHEN
    become_module.set_options(dict(
        become_pass='some_become_pass',
        become_exe='some_become_exe',
        become_flags='some_become_flags',
        become_user='some_become_user'
    ))

    # THEN
    assert become_module.build_become_command('some_command', 'some_shell') == \
        'some_become_exe some_become_flags -p "some_prompt" -u some_become_user some_command'


# Generated at 2022-06-13 11:35:15.440869
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test case 1
    becomeModule = BecomeModule({
        'become_exe': 'sudo',
        'become_flags': '-H -S -n',
        'become_user': '',
        'become_pass': False,
    },{},{},{})
    becomeModule._build_success_command = lambda cmd, shell: 'echo this-should-be-returned'
    cmd = 'do-complex-stuff'
    expected_result = 'sudo -H -S -n echo this-should-be-returned'
    assert becomeModule.build_become_command(cmd, None) == expected_result

    # Test case 2

# Generated at 2022-06-13 11:36:02.706201
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    c = BecomeModule()
    cmd = c.build_become_command('/usr/bin/ls', shell='/bin/bash')
    assert cmd == u'sudo -H -S -n /bin/bash -c \\"/usr/bin/ls\\"'

    c = BecomeModule()
    cmd = c.build_become_command('/usr/bin/ls', shell='/bin/bash')
    assert cmd == u'sudo -H -S -n /bin/bash -c \\"/usr/bin/ls\\"'

    c = BecomeModule()
    cmd = c.build_become_command('/usr/bin/ls', shell='/bin/bash')
    assert cmd == u'sudo -H -S -n /bin/bash -c \\"/usr/bin/ls\\"'

    c = BecomeModule()


# Generated at 2022-06-13 11:36:10.360718
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import os

    # mock the passed in command
    def mock_build_success_command(cmd, shell):
        return cmd

    # build a fake command to run
    cmd = '/bin/echo %s' % os.environ['HOME']

    # build a fake shell
    shell = 'a_shell'

    # create a BecomeModule instance
    bm = BecomeModule()

    # set the shell attribute of the BecomeModule
    bm.shell = shell

    # set the _build_success_command attribute to the mocked version
    bm._build_success_command = mock_build_success_command

    becomecmd = 'sudo'
    user = 'test_user'
    flags = '-H -n'
    prompt = ''
    password = 'test_password'

    # set the options on the BecomeModule instance
    bm

# Generated at 2022-06-13 11:36:18.312175
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    cls = BecomeModule()


# Generated at 2022-06-13 11:36:25.035354
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    """ Test case 1.1, 1.2 and 1.3 """
    # arrange
    bm = BecomeModule()
    bm.get_option = lambda _: None
    bm._build_success_command = lambda c, s: c

    # act
    sudo_cmd = bm.build_become_command('cmd', 'shell')
    bm.get_option = lambda x: 'flags' if x == 'become_flags' else None
    sudo_cmd_with_flags = bm.build_become_command('cmd', 'shell')
    bm.get_option = lambda x: 'user' if x == 'become_user' else None
    sudo_cmd_with_user = bm.build_become_command('cmd', 'shell')

    # assert

# Generated at 2022-06-13 11:36:36.942058
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    # Test null command.
    cmd = become.build_become_command('', 'bash')
    assert cmd == ''

    # Test command with no become_user, no become_pass, no become_flags.
    become = BecomeModule()
    cmd = become.build_become_command('ls /tmp', 'bash')
    assert cmd == 'sudo -H -S -n ls /tmp'

    # Test command with become_user, no become_pass, no become_flags.
    become = BecomeModule()
    become.set_options(direct={'become_user': 'test'})
    cmd = become.build_become_command('ls /tmp', 'bash')
    assert cmd == 'sudo -H -S -n -u test ls /tmp'

    # Test command with become_user, become

# Generated at 2022-06-13 11:36:43.487193
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.connection import ConnectionBase

    c = ConnectionBase()

    bm = BecomeModule(c)

    cmd = ["ls", "-l"]
    shell = "/bin/bash"

    # Test with ansible_become_exe
    c.set_options({"ansible_become_exe": "become_exe"})
    expected_cmd = 'become_exe -H -S -n /bin/bash -c "ls -l"'
    assert bm.build_become_command(cmd, shell) == expected_cmd

    # Test with ansible_become_exe
    c.set_options({"ansible_become_exe": "become_exe"})
    expected_cmd = 'become_exe -H -S -n /bin/bash -c "ls -l"'

# Generated at 2022-06-13 11:36:53.991283
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.loader import become_loader
    import ansible.constants as C

    C.DEFAULT_BECOME_PASS = 'fake default'

    mod = become_loader.get('sudo', class_only=True)()

    # per docs: empty command, flags, user
    assert mod.build_become_command('', '/bin/bash') == ''
    assert mod.build_become_command('', '/bin/bash') == ''

    # per docs: empty command, flags, user, custom password
    assert mod.get_option('become_pass') is None
    mod.set_options({'become_pass': 'fake custom'})
    assert mod.get_option('become_pass') == 'fake custom'

# Generated at 2022-06-13 11:36:59.150979
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    c = BecomeModule()
    c.get_option = lambda x: None
    c._build_success_command = lambda x, shell: 'complete'

# Generated at 2022-06-13 11:37:10.111175
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    """
    Test that become command is built properly
    """
    become_plugin = BecomeModule('/bin/bash', 'True', 'root', False, '-H', '-S', '-n', None)
    become_plugin.set_options(direct=None, variables=dict(ansible_become_pass="sudo_pass"))
    become_plugin._id = "test_id"
    assert become_plugin._build_success_command('run me', False) == 'bash -c "echo \\"$?\\" && sleep 0"'
    assert become_plugin.build_become_command('run me', False) == 'sudo -H -S -n -u root bash -c "echo \\"$?\\" && sleep 0"'
    become_plugin.prompt = '[sudo via ansible, key=test_id] password:'
   

# Generated at 2022-06-13 11:37:19.597006
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:39:10.342089
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import pytest
    from ansible.plugins.loader import become_loader

    class Options(object):
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

    class Runner(object):
        def __init__(self, hostname, become_pass):
            self.hostname = hostname
            self.connection = hostname
            self.become_pass = become_pass

    class PlayContext(object):
        def __init__(self, become_user, become_exe, become_flags, become_pass):
            self.become = True
            self.become_user = become_user
            self.become_exe = become_exe
            self.become_flags = become_flags
            self.become_pass = become_pass

    become_plugin = become

# Generated at 2022-06-13 11:39:17.578014
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    """Unit test for method build_become_command of class BecomeModule.

    This tests the expected output of the method when called with
    default and non default values for the become_exe, become_flags,
    become_user, become_pass and cmd.
    """

    test_cases = [{
        'become_exe': None,
        'become_flags': None,
        'become_user': None,
        'become_pass': None,
        'cmd': "echo 'Hello World!'",
        'expected': "sudo -H -S -n 'echo '\\''Hello World!'\\'''",
    }]

    for case in test_cases:
        bc = BecomeModule()
        bc.prompt = "prompt"
        bc.get_option = lambda x: case[x]


# Generated at 2022-06-13 11:29:26.599090
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.module_utils.basic import AnsibleModule

    def _build_success_command(cmd, shell):
        return cmd

    input = ['/bin/bash', '-lc', 'whoami']
    m = {'user': 'root', 'password': 'foo'}
    become = BecomeModule(AnsibleModule(m))
    become.SETUP_CACHE[become._id] = {'become_method': 'sudo'}
    become.build_become_command = _build_success_command

    become.prompt = become.get_option('become_pass_prompt')
    become.get_option = lambda z: m[z]
    become.options = m

    command = become.build_become_command(input, True)

# Generated at 2022-06-13 11:29:28.135237
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Method build_become_command of class BecomeModule is tested in test_sudo.yml
    pass

# Generated at 2022-06-13 11:29:30.511040
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # pylint: disable=line-too-long
    module = BecomeModule()
    # pylint: enable=line-too-long
    module.build_become_command('id', 'foo')

# Generated at 2022-06-13 11:29:38.495135
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    class FakeBecomeModule(BecomeModule):
        def get_option(self, name):
            if name == 'become_exe':
                return 'sudo'
            elif name == 'become_flags':
                return '-H -S -n'
            elif name == 'become_user':
                return 'admin'
            elif name == 'become_pass':
                return None
            elif name == 'become_method':
                return 'sudo'

    args = ['a', 'b', 'c']
    shell = '/bin/bash'
    fake = FakeBecomeModule()
    result = fake.build_become_command(args, shell)
    assert result == 'sudo -H -S -n /bin/bash -c \'a b c\''

# Generated at 2022-06-13 11:29:49.926677
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
  # Arrange
  task_vars = dict(ansible_become_user="test_user", ansible_become_password="password", ansible_become_flags="-n")

  module_args = dict(
    become=True,
    become_user='test_user',
    become_pass='password',
    become_flags='-n',
    ansible_become_exe='sudo',
    ansible_become_method='sudo'
    )

  become_plugin = BecomeModule(load_count=0, task_vars=task_vars, **module_args)

  # Act
  actual = become_plugin.build_become_command("testCmd", "testShell")

  # Assert
  assert actual == 'sudo -n -u test_user testCmd'



# Generated at 2022-06-13 11:30:01.456515
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_flags = '-H -S -n'
    become_password = 'testpassword'
    become_user = 'testuser'
    become_exe = 'testsudo'
    cmd = 'testcmd'
    shell = 'testshell'
    result = ' '.join([become_exe, become_flags, '-p "[sudo via ansible, key=79774c5a527cfdd5e77c5b7d5fdc8f23] password:"', '-u ' + become_user, ' '.join(["sh", "-c", '"' if shell else "", cmd, '&>', '/dev/null"', '"&>/dev/null &' if shell else '"' if shell else ""])])

# Generated at 2022-06-13 11:30:10.678239
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    command = 'cmd'
    shell = True
    become_module.prompt = 'prompt'
    become_module.get_option = lambda option: 'sudo' if option == 'become_exe' else '-H -S -n' if option == 'become_flags' else ''
    become_module.build_become_command(command, shell)
    assert become_module._id is not None
    assert become_module.prompt == '[sudo via ansible, key=%s] password:' % become_module._id
    assert become_module.success_cmd == 'sudo -n -H -S -p "%s" -u "" /bin/sh -c \'%s\'' % (become_module.prompt, command)
    become_module.prompt = None
    become_

# Generated at 2022-06-13 11:30:19.602286
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.module_utils._text import to_bytes
    bm = BecomeModule({'become_flags': '-H -S -n'}, loader=None, paramgram=None, runner_kwargs={'sudo_pass': 'bogus'})
    # Check different version of shell, and with command/shell_command
    for shell_type, cmd in [('csh', 'ls -l /etc/passwd'), ('powershell', 'Get-Content /etc/passwd')]:
        bm.runner = lambda x, **kw: x
        bm.runner.shell = shell_type
        # Check without user, without flags
        bm.runner_kwargs = {'sudo_pass': 'bogus'}
        bm.become_method = 'sudo'
        bm.become_user = None


# Generated at 2022-06-13 11:30:29.374394
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    def _build_become_pass(become_pass):
        return ' ' * len(become_pass)

    # no password is used
    become_pass = ''
    become_exe = 'sudo'
    become_flags = '-H -S -n'
    become_user = 'root'
    cmd = '/bin/foo'

    footer = '\nansible_become_success_message: True'
    expected_cmd = "sudo -H -S -n -u root %s %s" % (cmd, footer)
    b = BecomeModule(dict(become_pass=become_pass,
                          become_exe=become_exe,
                          become_flags=become_flags,
                          become_user=become_user))

# Generated at 2022-06-13 11:30:38.293113
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import pytest
    from ansible import constants as C
    from ansible.plugins.become import BecomeBase

    become = BecomeModule()
    become.prompt = None
    become.config = dict(
        ansible_become_user='user',
        ansible_become_exe='doas',
        ansible_become_flags=' -p test -N ',
        ansible_become_pass='test'
    )

    cmd = 'echo 1'
    shell = None

    result = become.build_become_command(cmd, shell)
    assert isinstance(result, str)

    # check if -p test is used

# Generated at 2022-06-13 11:30:50.440294
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    s = BecomeModule()

    # Test arguments with no become_pass
    becomecmd = s.get_option('become_exe') or s.name
    flags = s.get_option('become_flags') or ''
    prompt = ''
    if s.get_option('become_pass'):
        s.prompt = '[sudo via ansible, key=%s] password:' % s._id
        if flags:  # this could be simplified, but kept as is for now for backwards string matching
            flags = flags.replace('-n', '')
        prompt = '-p "%s"' % (s.prompt)

    user = s.get_option('become_user') or ''
    if user:
        user = '-u %s' % (user)

    # Test arguments with become_pass
    becomecmd_

# Generated at 2022-06-13 11:31:04.673608
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule(None)
    become_module.prompt = ''
    assert become_module.build_become_command('ls', False) == 'sudo  -H -S ls'
    become_module.prompt = ''
    become_module.get_option = lambda x: ''
    assert become_module.build_become_command('ls', False) == 'sudo  -H -S ls'
    become_module.prompt = 'prompt'
    assert become_module.build_become_command('ls', False) == 'sudo  -H -S -p "prompt" ls'
    become_module.prompt = ''
    become_module.get_option = lambda x: 'become_pass'

# Generated at 2022-06-13 11:31:11.611914
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    '''
        Unit test for method build_become_command of class BecomeModule
    '''
    class TestBecomeModule(BecomeModule):
        name = 'sudo'

        def build_success_command(self, cmd, executable):
            """Convenience method to generate a command line to check whether
            the provided command can run successfully, when provided with a
            valid password.

            This is mostly to ensure that no other credentials need to be
            provided before this check.

            Example: echo '' | sudo -S -p 'sudo password:' whoami > /dev/null 2>&1
            """
            pass

    become_module = TestBecomeModule()
    assert become_module.build_become_command("", "") == "sudo echo '' | sudo -S -p '' whoami"


# Generated at 2022-06-13 11:31:20.123038
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    sut = BecomeModule(None, become_user=None, become_pass=None, become_exe=None, become_flags=None)
    expected_cmd = "/bin/sh -c '  some_command'"
    cmd = sut.build_become_command(expected_cmd, shell=True)
    assert cmd == expected_cmd
    assert sut.prompt == ''

    sut = BecomeModule(None, become_user=None, become_pass="secret", become_exe=None, become_flags=None)
    expected_cmd = "/bin/sh -c '  some_command'"
    cmd = sut.build_become_command(expected_cmd, shell=True)
    assert cmd == "/bin/sh -c '  sudo -p \"%s\" some_command'" % sut.prompt
    assert s

# Generated at 2022-06-13 11:31:24.849309
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:31:33.978878
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule([], dict(
        become_pass=True,
        become_user='root',
        become_exe='sudo',
        become_flags='-H -S -n',
        prompt='[sudo via ansible, key=12345] password:',
        ansiballz_command='python /tmp/test/test-ansiballz2.py',
        ansiballz_command_args='{"foo": "bar"}',
        shell='/bin/sh -c',
    ))

# Generated at 2022-06-13 11:31:42.443790
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    args = [ 'echo', 'Hello', 'World!' ]
    opts = { 'become_exe': 'sudo', 'become_flags': '-H -S -n', 'become_user': 'root', 'become_pass': None }
    cmd = BecomeModule(check_mode=False).build_become_command(args, opts)
    assert cmd == '/usr/bin/sudo -H -S -n ' + BecomeBase.success_cmd + ' /bin/sh -c \'echo Hello World! && printf "%s\\n" 1 > "/proc/self/attr/key"'
    opts = { 'become_exe': None, 'become_flags': '-H -S -n', 'become_user': 'root', 'become_pass': None }

# Generated at 2022-06-13 11:31:50.697302
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()

    # Test default become command
    test_cmd = '/bin/ls'
    assert become_module.build_become_command(test_cmd, "bash") == '/bin/ls'

    # Test with become_exe
    become_module.set_options(become_exe='/usr/bin/sudo')
    assert become_module.build_become_command(test_cmd, "bash") == '/usr/bin/sudo -H -S -n /bin/ls'

    # Test with become_flags
    become_module.set_options(become_exe='/usr/bin/sudo', become_flags='--become-flags')

# Generated at 2022-06-13 11:32:00.944437
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    """
    Tests that `become_exe` and `become_flags` are properly substituted in command
    """
    #
    # test string substitution
    b = BecomeModule(play_context=dict(become_user='ubuntu'))
    b.sudo_exe = 'sudu'
    b.become_flags = '-E'
    b.become_pass = 'password123'
    cmd = b.build_become_command('ls', 'sh')

# Generated at 2022-06-13 11:32:11.800070
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()

    become_module.set_options(direct={'become_flags': '-H -S -n',
                                      'become_pass': 'test',
                                      'become_exe': 'sudo',
                                      'become_user': 'test'}, variables={})
    actual_result = become_module.build_become_command('/bin/sh -c "ls"', '/bin/sh -c')
    expected_result = 'sudo -H -S -p "[sudo via ansible, key=test] password:" -u test /bin/sh -c "ls"'

    assert(actual_result == expected_result)


# Generated at 2022-06-13 11:32:25.055630
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Method build_become_command return "sudo -H -S -n -p '[sudo via ansible, key=%s] password:' -u root echo 'BECOME-SUCCESS-njhftugtmjdcvenivyodgkujjfnvhjth'"
    # when become_pass is True, become_flags is "-H -S -n", become_user is "root" and cmd is "echo 'BECOME-SUCCESS-njhftugtmjdcvenivyodgkujjfnvhjth'"
    # (initial setup)
    class FakeOptions:
        become_exe='sudo'
        become_flags='-H -S -n'
        become_pass=True
        become_user='root'
    class FakeTask:
        _id = 'become_test_string'


# Generated at 2022-06-13 11:32:34.024090
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    # Set up mock for AnsibleModule and AnsibleModuleTestCase
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    module.params = {'become_pass': 'awsomepassword'}
    module.check_mode = False

    # Test build_become_command
    module.run_command = lambda *args, **kwargs: args[0]
    become = BecomeModule(module)
    cmd = 'some command'
    shell = 'some shell'

# Generated at 2022-06-13 11:32:44.525283
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule()
    command = b.build_become_command('ls', '/bin/sh')
    assert command == 'sudo -H -S -n /bin/sh -c \'echo %s; %s\'' % (b.success_key, 'ls')

    b = BecomeModule()
    b.get_option = lambda x: {'become_user': 'foo', 'become_exe': '/usr/bin/become', 'become_pass': 'test'}.get(x)
    b.prompt = '[sudo via ansible, key=%s] password:' % b._id
    command = b.build_become_command('ls', '/bin/sh')

# Generated at 2022-06-13 11:32:49.927857
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    become._id="IDMONTOFACILE"
    command = "ls -1"
    command_sudo = become.build_become_command(command)
    assert command_sudo == "sudo -H -S -np '[sudo via ansible, key=IDMONTOFACILE] password:' ls -1"
    become.set_become_user("ansible")
    command_sudo_ansible = become.build_become_command(command)
    assert command_sudo_ansible == "sudo -H -S -np '[sudo via ansible, key=IDMONTOFACILE] password:' -u ansible ls -1"
    become.set_become_pass("qwerty")
    command_sudo_ansible_password = become.build_become_command(command)
    assert command

# Generated at 2022-06-13 11:32:55.170198
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule({
        'become_exe': 'sudo',
        'prompt': '[sudo via ansible, key=%s] password:',
        'become_flags': '-H -S -n',
        'become_pass': '',
    })
    cmd = 'ls -la'
    shell = '/bin/sh'

    # test to detect that the result is equal to #{cmd}
    assert module.build_become_command(cmd, shell) == 'sudo -H -S -n /bin/sh -c \'(%s)\'' % (cmd)

    # test to detect that flags is updated
    module.get_option('become_flags') == '-H -S'
    cmd = 'ls -la'
    shell = '/bin/sh'
    assert module.build_become_

# Generated at 2022-06-13 11:33:07.234718
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:33:11.013387
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomecmd = 'sudo'
    flags = '-H -S -n'
    prompt = '-p "Sorry, try again."'
    user = '-u test_user'
    cmd = 'test'
    assert BecomeModule(None, None).build_become_command(cmd, None) == \
           ' '.join([becomecmd, flags, prompt, user, cmd])

# Generated at 2022-06-13 11:33:21.948671
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    sudo_become_module = BecomeModule()

    sudo_become_module._id = "1234567890"

    # test case where cmd is None
    assert sudo_become_module.build_become_command(None, False) is None
    assert sudo_become_module.build_become_command(None, True) is None

    # test case where cmd is not None and become_pass is not None
    sudo_become_module.prompt = ""
    sudo_become_module.get_option = lambda x: {'become_exe': '', 'become_flags': '', 'become_pass': '123456', 'become_user': ''}[x]

# Generated at 2022-06-13 11:33:30.744234
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    """
    Unit test for method build_become_command of class BecomeModule
    """
    test_cmd = "echo 'Foo'"
    test_shell = "Shell"
    expected = "sudo -H -S -n -p \"%s\" -u %s %s" % ('[sudo via ansible, key=%s] password:', 'test_user' , test_cmd)

    become_module = BecomeModule()
    become_module._id = 'f53d1c33399f5e51efccd9a9062c1a3a1afcb0cb' # test_id
    become_module.get_option = lambda section: {'become_exe': 'sudo', 'become_flags': '-H -S -n', 'become_user': 'test_user'}[section]
   

# Generated at 2022-06-13 11:33:41.552751
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    host1 = {
        "name": "localhost",
        "ansible_connection": "local"
    }
    host1["become_user"] = "ansible"
    host1["become_password"] = "iampassword"
    host1["_ansible_verbosity"] = 0
    host1["_ansible_debug"] = False
    become._connection._shell = "sh"
    # create command
    cmd = "echo hello"
    cmd = become.build_become_command(cmd, host1["_ansible_shell"])
    assert cmd == "sudo -S -p \"sudo via ansible, key=None] password:\" -u ansible sh -c 'echo hello && echo >/dev/null 2>&1'"



# Generated at 2022-06-13 11:34:00.238266
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    def _almost_equal(arr1, arr2):
        return set(arr1) == set(arr2)

# Generated at 2022-06-13 11:34:12.254867
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    plugin = BecomeModule.load()
    assert plugin.build_become_command('ls', 'sh') == 'sudo -H -S ls'
    assert plugin.build_become_command('ls', 'sh') == 'sudo -H -S ls'
    assert plugin.build_become_command('', 'sh') == ''
    assert plugin.build_become_command('ls', 'sh') == 'sudo -H -S ls'
    assert plugin.build_become_command('ls', 'sh') == 'sudo -H -S ls'
    assert plugin.build_become_command('ls', 'sh') == 'sudo -H -S ls'
    assert plugin.build_become_command('ls', 'sh') == 'sudo -H -S ls'
    assert plugin.build_become_command('ls', 'sh')

# Generated at 2022-06-13 11:34:19.663753
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Set up mock objects for a task:
    # (1) doesn't require a password; and
    # (2) has become_user set to 'root'
    task = type('', (), {})()
    task.become_pass = False
    task.become_user = 'root'

    # Run the build_become_command method
    become = BecomeModule(task, become_pass=None)
    # Check that the method returns the expected command
    assert become.build_become_command('some command', 'some shell') == 'sudo -H -S -n "-u root" some command'


# Generated at 2022-06-13 11:34:29.658677
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()
    cmd = 'ls'
    shell = '/bin/sh'
    become.get_option = lambda opt: None
    become._build_success_command = lambda cmd, shell: cmd

    # Test with become password set
    become.get_option = lambda opt: {'become_pass': 'bacon', 'become_exe': 'sudo', 'become_flags': '-H -S -n'}.get(opt)
    assert become.build_become_command(cmd, shell) == "sudo -H -S -n -p \"[sudo via ansible, key=bacon] password:\" ls"

    # Test without become password set

# Generated at 2022-06-13 11:34:38.627883
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.loader import become_loader
    mod = become_loader.get('sudo')
    assert mod.build_become_command("ls") == "sudo -H -S -n ls"
    assert mod.build_become_command("ls") == "sudo -H -S -n ls"
    assert mod.build_become_command("ls", shell=True) == "sudo -H -S -n 'ls'"
    assert mod.build_become_command("ls", shell=False) == "sudo -H -S -n ls"

    mod.set_options(dict(become_user='bob', become_pass=True))
    mod.set_option('become_exe', 'sudo-i')

# Generated at 2022-06-13 11:34:48.762107
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Preparing test objects
    become_module = BecomeModule()
    become_module._options = {'become_user': 'test_user', 'become_pass': False, 'become_exe': 'custom_sudo'}
    become_module.prompt = 'test'
    become_module._id = 'test_id'

    # Testing
    assert become_module.build_become_command('COMMAND', shell=True) == 'custom_sudo -H -S -u test_user COMMAND'
    become_module._options['become_flags'] = '-H -S -n'
    assert become_module.build_become_command('COMMAND', shell=True) == 'custom_sudo -H -S -u test_user COMMAND'

# Generated at 2022-06-13 11:34:55.369613
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.become.sudo import BecomeModule
    import os
    import sys
    import tempfile
    import subprocess
    import shutil

    class MockModule(object):
        name = 'module_name'
        prompt = ''

    module = MockModule()

    plugin_class_instance = BecomeModule(module, become_password='password', become_user='user', become_check=True)
    # cmd is empty
    cmd = ''
    shell = 'sh'
    res = plugin_class_instance.build_become_command(cmd, shell)
    assert res == 'sudo -H -S -n -u user -u user sh -c \'echo BECOME-SUCCESS-iwejfksjdfklsjdfl; %s\'' % cmd
    
    # cmd is not empty
    cmd

# Generated at 2022-06-13 11:35:03.063537
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    become_module.get_option = lambda x: None
    assert become_module.build_become_command(['command_to_become'], 'shell_to_execute') == 'sudo -H -S -n command_to_become'

    become_module.get_option = lambda x: 'mybecome_flags' if x == 'become_flags' else None
    assert become_module.build_become_command(['command_to_become'], 'shell_to_execute') == 'sudo mybecome_flags command_to_become'

    become_module.get_option = lambda x: 'mybecome_exe' if x == 'become_exe' else None

# Generated at 2022-06-13 11:35:12.947098
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Create data to be used in tests
    become_options = {
        'become_exe': 'sudo',
        'become_flags': '-H -S -n',
        'become_user': 'root',
        'become_pass': 'test_pass',
        '_id': 'ansible_test_id'
    }

    for shell in (None, '/bin/bash'):
        for cmd in (None, ['/bin/true'], ['echo', 'test']):
            # Create class instance
            test_suite = BecomeModule(None, become_options, None, None)

            # Call method under test with arguments
            result = test_suite.build_become_command(cmd, shell)

            # Check if the result is as expected
            if cmd == None:
                assert result == cmd


# Generated at 2022-06-13 11:35:17.881053
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule()

    # use sudo
    b.set_option('become_exe', 'sudo')
    b.set_option('become_flags', '')
    b.set_option('become_pass', True)
    b.set_option('become_user', 'test')

    # build shell command
    cmd = b.build_become_command('whoami', False)

    assert cmd == 'sudo -H -S -p "Sorry, try again." -u test sh -c "whoami"', \
        "unexpected command for build_become_command"
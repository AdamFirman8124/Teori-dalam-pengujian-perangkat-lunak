

# Generated at 2022-06-13 11:29:29.259937
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:29:37.958777
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test variables
    class options:
        become_exe = 'sudo'

    class become_plugin_options:
        executable = 'sudo'

    class connection:
        prompt = None

    class become_pass:
        pass

    class task_vars:
        ansible_become_password = None

    class play_context:
        become_user = None
        become_pass = None
        become_exe = None
        become_flags = None
        success_key = None

    # Create class objects
    become_module = BecomeModule()
    become_module.connection = connection
    become_module.get_option = become_pass
    become_module.get_option = options
    become_module.get_option = become_plugin_options
    become_module._build_success_command = 'true'

# Generated at 2022-06-13 11:29:44.637677
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()

    # Test with no arguments
    assert become.build_become_command([], '') == ''

    # Test with all default arguments
    become_user = become.get_option('become_user')
    become_exe = become.get_option('become_exe')
    become_flags = become.get_option('become_flags')
    assert become.build_become_command(
        [become_exe],
        ''
    ) == ' '.join([
        become_exe,
        become_flags,
        '-u %s' % (become_user),
        become._build_success_command(become_exe, '')
    ])

# Generated at 2022-06-13 11:29:54.752112
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    my_become = BecomeModule()

    # Test for std cmd
    cmd = 'ls'
    result = 'sudo -H -S -n  ls'
    assert my_become.build_become_command(cmd, None) == result

    cmd = 'ls -l'
    result = 'sudo -H -S -n  ls -l'
    assert my_become.build_become_command(cmd, None) == result

    cmd = 'ls -lh'
    result = 'sudo -H -S -n  ls -lh'
    assert my_become.build_become_command(cmd, None) == result

    cmd = 'ls -lhtr /'
    result = 'sudo -H -S -n  ls -lhtr /'
    assert my_become.build_become

# Generated at 2022-06-13 11:30:03.739360
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    # Test 1, an empty command
    become_module = BecomeModule()
    become_module.prompt = ''
    become_module.set_options({'become_exe':'', 'become_flags': '', 'become_pass': ''})
    cmd = become_module.build_become_command([], [])
    assert cmd == []

    # Test 2, a non-empty command with no flags, prompt and become user
    cmd = become_module.build_become_command(['echo', 'Hello'], [])
    assert cmd == ['sudo', '-H', '-S', '-n', 'echo Hello']

    # Test 3, a non-empty command with flags, prompt and become user

# Generated at 2022-06-13 11:30:08.819217
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    test_obj = BecomeModule(None)
    test_obj._validate_options = lambda: None
    cmd = list()
    cmd.append('/bin/sh')
    cmd.append('-c')
    cmd.append('echo hello')
    result = test_obj.build_become_command(cmd, False)
    assert result == 'sudo -H -S -n  /bin/sh -c \'echo hello\''

# Generated at 2022-06-13 11:30:13.827636
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # initialize the objects
    become_module = BecomeModule()
    # set options
    become_module.set_option('become_user', 'testUser')
    become_module.set_option('become_pass', 'testPass')
    become_module.set_option('become_flags', '')
    # execute test
    cmd = 'testCmd'
    shell = 'testShell'
    become_module._id = 42
    command = become_module.build_become_command(cmd, shell)
    assert command == 'sudo -p "[sudo via ansible, key=42] password:" -u testUser sh -c \'(umask 77 && printf "[sudo via ansible, key=42] password:" && sleep 0 && (stty -echo && printf "testPass" && stty echo) && printf "\n"'

# Generated at 2022-06-13 11:30:28.408748
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()

    become_module.prompt = 'prompt'
    become_module.get_option = lambda x : 'become_flags' if x == 'become_flags' else 'become_exe' if x == 'become_exe' else 'become_user' if x == 'become_user' else 'become_pass' if x == 'become_pass' else 'become_flags' if x == 'become_flags' else None

    # test if become_pass is set
    cmd = 'cmd'
    cond = become_module.build_become_command(cmd, False) == 'sudo -S -p "prompt" -u become_user cmd'
    assert cond

    # test if become_pass is not set
    cmd = 'cmd'

# Generated at 2022-06-13 11:30:37.749098
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:30:44.264699
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():

    # Setting up test, create class and varibles
    bm = BecomeModule()
    bm.prompt = 'test_prompt'
    bm_result = bm.build_become_command('test_cmd', 'test_shell')
    assert bm_result == 'sudo -p "%stest_prompt" test_cmd', "Unexpected error from BecomeModule.build_become_command"  # noqa

# Generated at 2022-06-13 11:31:02.566008
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    '''
    Unit test for method build_become_command of class BecomeModule.
    :return:
    '''
    bm = BecomeModule()
    bm.options = dict(
        become_user='some_user',
        become_exe='/usr/bin/sudo',
    )
    bm.prompt = '-p'
    bm._id = 'some_id'
    assert bm.build_become_command('true', 'shell') == '/usr/bin/sudo -p [sudo via ansible, key=some_id] password: -u some_user /bin/sh -c \'echo BECOME-SUCCESS-xplxgisn; true\' 2>/dev/null || (exit $? && true)'

# Generated at 2022-06-13 11:31:08.658239
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(None, None)
    become.get_option = lambda key: None
    assert become.build_become_command('test_command', False) == 'sudo -S -n test_command'
    become.get_option = lambda key: 'test_become_exe'
    assert become.build_become_command('test_command', False) == 'test_become_exe -S -n test_command'
    become.get_option = lambda key: 'test_become_flags'
    assert become.build_become_command('test_command', False) == 'sudo test_become_flags -n test_command'
    become.get_option = lambda key: 'test_become_user'

# Generated at 2022-06-13 11:31:22.453008
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.become import BecomeBase

    class TestBecomeModule(BecomeModule):
        get_option = lambda self, x: self.options[x]
        _id = '123456789'

        def __init__(self, options):
            self.options = options

        def _build_success_command(self, cmd, shell):
            return 'echo success'

    become_exe = 'sudo'
    become_flags = '-H -S -n'
    become_pass = 'password'
    become_user = 'root'

    TestModule = TestBecomeModule({'become_exe': become_exe, 'become_flags': become_flags, 'become_pass': become_pass, 'become_user': become_user})

    cmd = ['foo', 'bar']

# Generated at 2022-06-13 11:31:28.910291
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomecmd = BecomeModule()
    assert 'sudo cmd' == becomecmd.build_become_command('cmd', 'shell')
    becomecmd.prompt = 'password'
    assert 'sudo -n -u root cmd' == becomecmd.build_become_command(
        'cmd', 'shell', become_flags='-n', become_user='root')
    becomecmd.prompt = 'password'
    assert 'sudo -H -S -p "password" -u root cmd' == becomecmd.build_become_command(
        'cmd', 'shell', become_flags='-H -S', become_user='root', become_pass=True)

# Generated at 2022-06-13 11:31:37.749520
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    module = BecomeModule(None)
    module.prompt = ''
    assert module.build_become_command(['command'], None) == 'sudo -H -S -n command'

    module = BecomeModule(None)
    module.prompt = ''
    assert module.build_become_command(['command'], True) == 'sudo -H -S -n bash -c "command"'

    module = BecomeModule(None)
    module.get_option = lambda key: 'test'
    module.prompt = ''
    assert module.build_become_command(['command'], None) == 'test -H -S -n test command'

    module = BecomeModule(None)
    module.get_option = lambda key: 'test'
    module.prompt = ''

# Generated at 2022-06-13 11:31:41.735668
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.loader import become_loader

    b = become_loader.get('sudo')
    assert b.build_become_command(None, None) == None

    b = become_loader.get('sudo')
    b.get_option = lambda option: option
    assert b.build_become_command(None, None) == "sudo -H -S -n executable command"

# Generated at 2022-06-13 11:31:47.494626
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()

    become.set_options(dict(become_exe='become_exe', become_flags='become_flags', become_user='become_user', become_pass='become_pass', shell=False))
    assert become.build_become_command('test', False) == 'become_exe become_flags -p "[sudo via ansible, key=become_pass] password:" -u become_user test'

    become.set_options(dict(become_exe='become_exe', become_flags='', become_user='become_user', become_pass='become_pass', shell=False))
    assert become.build_become_command('test', False) == 'become_exe -p "[sudo via ansible, key=become_pass] password:" -u become_user test'

# Generated at 2022-06-13 11:31:56.016546
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    bcmd = BecomeModule(become_pass='secret', become_exe='sudoer', become_flags='-K', become_user='root',
                        become_exe_args='', executable=None,
                        shell=False)

    cmd = 'command'

    actual = bcmd.build_become_command(cmd, shell=False)
    expected = ' '.join(['sudoer', '-K', '-p "[sudo via ansible, key=%s] password:"' % bcmd._id, '-u root',
                         bcmd._build_success_command(cmd, False)])

    assert actual == expected, 'Got failed to build command "%s"; expected "%s"' % (actual, expected)



# Generated at 2022-06-13 11:32:06.752397
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_user = 'mike'
    become_pass = 'foobar'
    become_exe = 'sudo'
    become_flags = '-s'
    sudo_prompt = '[sudo via ansible, key=8bfb2ea3b3c31a69] password:'
    cmd = 'cat /tmp/foo'
    cmd_expected = 'sudo -s -p "%s" -u %s ansible_become_success_command="\'%s\'" ansible_become_success_command="\'%s\'" sh -c \'%s\'' % (sudo_prompt, become_user, cmd, cmd, cmd)
    bm = BecomeModule()

# Generated at 2022-06-13 11:32:16.939138
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    bmc = BecomeModule(None, {}, {})

    # Set
    bmc.become_exe = 'sudo'
    bmc.prompt = '[sudo via ansible, key=abcd123] password:'
    bmc.become_user = 'root'

    # Default
    bmc.become_flags = ''
    assert bmc._build_success_command('ls -t | head -1', True) == "bash -c 'echo BECOME-SUCCESS-abcd123; %s' || echo 'BECOME-FAILURE-abcd123'" % "ls -t | head -1"
    cmd = bmc.build_become_command('ls -t | head -1', True)

# Generated at 2022-06-13 11:32:34.831879
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    m = BecomeModule()

    # check default options
    cmd, args = m.build_become_command('test_command', 'sh')
    assert(args['become_user'] == 'root')
    assert(args['become_exe'] == 'sudo')
    assert(args['become_flags'] == '-H -S -n')
    assert(args['become_pass'] == None)

    # check shell quoting
    cmd, args = m.build_become_command('test command', 'sh')
    assert(cmd == 'test \'command\'')

    # check other shell types
    cmd, args = m.build_become_command('test command', 'csh')
    assert(cmd == 'test command')

# Generated at 2022-06-13 11:32:45.435302
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:32:48.490975
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Initialize class object
    become_module_obj = BecomeModule(
        become_pass='123456',
        become_user='ansible',
        become_flags='-H -S -n',
        become_exe='sudo'
    )
    # Test method

# Generated at 2022-06-13 11:32:55.032076
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # given
    become_module = BecomeModule(dict(become_pass='BECOME_PASS', remote_addr='REMOTE_ADDR', connection='CONNECTION'),
                                 check_mode=False)
    become_module.prompt = None
    # when
    cmd = become_module.build_become_command('mycmd', 'myshell')
    # then
    assert cmd == 'sudo -H -S -p "[sudo via ansible, key=REMOTE_ADDR] password:" -u root mycmd'

    # when
    become_module.prompt = 'PROMPT'
    cmd = become_module.build_become_command('mycmd', 'myshell')
    # then
    assert cmd == 'sudo -H -S -p "PROMPT" -u root mycmd'

    # when
   

# Generated at 2022-06-13 11:33:06.316869
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    instance = BecomeModule(
        get_option=lambda k: None,
        runner_options={
            'become_user': 'test_user',
            'become_pass': 'test_pass',
            'sudo_exe': 'sudo_exe',
            'sudo_flags': 'sudo_flags',
        },
        options=BecomeModule.options,
    )
    instance._id = 42
    actual = instance.build_become_command('some_command', False)
    expected = 'sudo_exe sudo_flags -p "[sudo via ansible, key=42] password:" -u test_user some_command'
    assert actual == expected, 'actual: {actual}, expected: {expected}'.format(actual=actual, expected=expected)

# Generated at 2022-06-13 11:33:17.218831
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:33:27.202373
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    shell = '/bin/sh'
    cmd = 'ls -la'
    test_module = BecomeModule()
    assert test_module.build_become_command(cmd, shell) == 'sudo -H -S -n /bin/sh -c "ls -la" && echo BECOME-SUCCESS-kndsjfmewx'

    test_module = BecomeModule()
    test_module.prompt = 'prompt_string'
    test_module.become_user = 'test_user'
    test_module.set_options(direct={'become_flags': '-f', 'become_pass': True})

# Generated at 2022-06-13 11:33:38.421502
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(None, become_exe='sudo', become_user='test')
    # No prompt
    assert become.build_become_command('a b c', 'c') == 'sudo -u test a b c'
    # With prompt
    become = BecomeModule(None, become_exe='sudo', become_user='test', become_pass=True)
    assert become.build_become_command('a b c', 'c') == 'sudo -p "[sudo via ansible, key=None] password:" -u test a b c'
    # With prompt and with flags
    become = BecomeModule(None, become_exe='sudo', become_user='test', become_pass=True, become_flags='-H -S')

# Generated at 2022-06-13 11:33:42.097555
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    test_input = {'become_exe': '/path/sudo',
                  'become_flags': '-H -S -n',
                  'become_user': 'root',
                  'become_pass': None,
                  'prompt': '[sudo via ansible, key=%s] password:'}


# Generated at 2022-06-13 11:33:55.959109
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule()
    assert b.build_become_command('/bin/true', None) == '/bin/true'

    b = BecomeModule()
    b.set_options(become_flags='-H -K', become_user='bob')
    assert b.build_become_command('/bin/true', None) == 'sudo -H -K -u bob /bin/true'

    b = BecomeModule()
    b.prompt = 'fakeprompt'
    b.set_options(become_pass='fakepassword', become_user='bob', become_flags='-K -H -n')
    assert b.build_become_command('/bin/true', None) == 'sudo -K -H -p "fakeprompt" -u bob /bin/true'



# Generated at 2022-06-13 11:34:22.990528
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    plugin = BecomeModule()

    # Test with no flags
    command = 'ls -la'
    assert plugin.build_become_command(command, shell=None) == 'sudo {{ command }}'

    # Add a username
    plugin.options['become_user'] = 'root'
    assert plugin.build_become_command(command, shell=None) == 'sudo -u root {{ command }}'

    # Add flags
    plugin.options['become_flags'] = '-H -S -n'
    assert plugin.build_become_command(command, shell=None) == 'sudo -H -S -n -u root {{ command }}'

    # Test with no flags and a shell
    command = 'ls -la'

# Generated at 2022-06-13 11:34:33.029668
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Test default options
    class Opts:
        become_exe = ""
        become_flags = ""
        become_user = ""
    class Module:
        _options = Opts()
        name = "test_module"
    cmd = "some_command"
    shell = "sh"
    bm = BecomeModule(shell, cmd, None, None, None)
    bm.set_module(Module)
    result = bm.build_become_command(cmd, shell)
    assert result == "sudo -H -S -n some_command"

    # Test become_flags -n
    class OptsNonInteractive:
        become_exe = ""
        become_flags = "-n"
        become_user = ""
    class ModuleNonInteractive:
        _options = OptsNonInteractive()

# Generated at 2022-06-13 11:34:37.645690
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule('become_method', 'become_exe', 'become_user', 'become_pass', 'success_command')
    become.get_option = lambda a: None
    become._build_success_command = lambda a, b: "echo 1"
    become.prompt = None
    assert 'sudo -H -S -n echo 1' == become.build_become_command(None, None)

# Generated at 2022-06-13 11:34:48.361249
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(play_context=None, new_stdin=None, loader=None, options=dict(), passwords=dict())
    test_cases = {
        'simple': (
            ['ansible'],
            'sudo -n -H -S ansible\n',
        ),
        'complex': (
            ['ansible-playbook', '--version'],
            'sudo -n -H -S ansible-playbook --version\n',
        ),
    }

    for args, expect in test_cases.items():
        test_cmd, test_expect = args, expect
        got = become.build_become_command(test_cmd, None)
        assert got == test_expect, 'Raw sudo: got %s, expected %s' % (got, test_expect)


# Generated at 2022-06-13 11:34:51.855537
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule()

    expected_result = ' '.join(['sudo',
                           '-H -S '
                           '-p "[sudo via ansible, key=test] password:"',
                           '-u root'
                           ' '])

    result = b.build_become_command('', 'sh')
    assert result == expected_result

# Generated at 2022-06-13 11:34:57.329739
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    def assert_build_become_command(become, cmd, expected_cmd, expected_prompt):
        if not cmd:
            return
        assert become.build_become_command(cmd, shell=None) == expected_cmd
        assert become.prompt == expected_prompt

    become_module = BecomeModule(
        password_prompt=None,
        prompt=None,
        prompt_re=None,
        become_user=None,
        become_pass=None,
        become_exe=None
    )

    become_module._id = 1
    assert_build_become_command(become_module, 'ls', 'sudo -H -S -n ls', '')

    become_module._id = 2

# Generated at 2022-06-13 11:35:06.168733
# Unit test for method build_become_command of class BecomeModule

# Generated at 2022-06-13 11:35:15.045951
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule()
    b.prompt = '[sudo via ansible, key=%s] password:'
    # test no become_user specified
    cmd = b.build_become_command('', 'shell')
    assert "sudo -H -S -n -p \"[sudo via ansible, key=%s] password:\" '' 'shell'" == cmd

    b.prompt = '[sudo via ansible, key=%s] password:'
    # test no become_user specified, become_pass specified
    cmd = b.build_become_command('', 'shell')
    assert "sudo -H -S -n -p \"[sudo via ansible, key=%s] password:\" '' 'shell'" == cmd

    # test become_user specified, become_pass specified

# Generated at 2022-06-13 11:35:20.911413
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    options = dict()
    shell = 'sh'
    cmd = 'echo "test"'
    prompt = '%s@%s' % (os.environ['LOGNAME'], os.environ['HOSTNAME'])

    # Test 1 with all default options
    options['become_exe'] = 'sudo'
    options['become_flags'] = '-H -S -n'
    options['become_user'] = ''
    options['become_pass'] = ''

    become_module = BecomeModule()
    become_command = become_module.build_become_command(cmd, shell)
    assert become_command == 'sudo -H -S -n %s' % (cmd)

    # Test 2 with become_user and become_pass
    options['become_user'] = 'testuser'

# Generated at 2022-06-13 11:35:27.795169
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.loader import become_loader
    loader = become_loader
    mod = loader._create_become_plugin('sudo')
    cmd = mod.build_become_command('', 'sh')
    assert cmd == 'sudo -H -S -n sh -c \'%s && sleep 0\' ' % ("%s -c 'echo BECOME-SUCCESS-dgcdujilifxzvkiyfhkl; /bin/sh -c \"\"'")

# Generated at 2022-06-13 11:36:23.983938
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.loader import become_loader

    plugin = become_loader.get('sudo')

    changed_cmd = 'id -Z'
    cmd = plugin.build_become_command(changed_cmd, None)
    assert cmd == 'sudo -H -S -n id -Z'

    plugin = become_loader.get('sudo')

    changed_cmd = 'id -Z'
    cmd = plugin.build_become_command(changed_cmd, None)
    assert cmd == 'sudo -n id -Z'

    plugin = become_loader.get('sudo')

    changed_cmd = 'id -Z'
    cmd = plugin.build_become_command(changed_cmd, None)
    assert cmd == 'sudo -p "[sudo via ansible, key=%s] password:" -n id -Z'

    plugin

# Generated at 2022-06-13 11:36:34.213188
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    shell, cmd, prompt, become_method, become_exe, become_user, become_flags, become_pass = get_test_parameters()
    options = {'become_method': become_method, 'become_exe': become_exe, 'become_user': become_user, 'become_flags': become_flags, 'become_pass': become_pass}

    bm = BecomeModule(None)
    bm.prompt = prompt
    assert bm.build_become_command(cmd, shell) == build_command(become_exe, become_flags, prompt, become_user, cmd, shell)


# Generated at 2022-06-13 11:36:41.680219
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_plugin = BecomeModule()

    becomecmd = 'somebecomecmd'
    become_plugin.get_option = lambda x: becomecmd if x == 'become_exe' else None
    become_plugin.prompt = None

    cmd = 'somecommand'
    shell = '/bin/sh'

    become_plugin.get_option = lambda x: None
    become_plugin.prompt = None

    # with password
    expect = ' '.join([becomecmd, '-p "someprompt"', '-u someuser', shell, '-c', cmd])
    become_plugin.get_option = lambda x: 'someprompt' if x == 'become_pass' else None
    become_plugin.get_option = lambda x: 'someuser' if x == 'become_user' else None
    assert become_plugin

# Generated at 2022-06-13 11:36:50.279609
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    assert(
        command_build_test(
            b_str = 'su - user -c "cmd"',
            b_params = dict(user = 'user', cmd = 'cmd'),
            b_options = dict(become_exe = 'su', become_user = 'user', become_method = 'su'),
            b_result = dict(stdout = 'Succes', rc = 0)
        ) == dict(res = True, msg = 'Success: command: su - user -c "cmd"', stdout = 'Succes', rc = 0)
    )


# Generated at 2022-06-13 11:36:55.749379
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_pass = 'secret'
    cmd = 'whoami'
    shell = 'csh'
    become_exe = 'sudo'
    become_flags = '-H -S -n'
    become_user = 'root'
    become_module = BecomeModule({}, {})
    become_module.prompt = ''
    become_module.set_options({
        'become_pass': become_pass,
        'become_exe': become_exe,
        'become_flags': become_flags,
        'become_user': become_user,
    })

# Generated at 2022-06-13 11:37:01.043989
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # Example from documentation
    from ansible.plugins.become.sudo import BecomeModule

    become = BecomeModule(play_context={
        "become_user": "root",
        "become_pass": "abc123",
        "become_exe": "sudo",
        "prompt": "[sudo via ansible, key=GBJRf5wJk5r5xHmmx5dLgDB5JZaFmZQ2] password:",
        "become": True,
        "become_method": "sudo",
        "become_flags": "-H -S -n"
    })
    cmd = "/bin/ps axo user,pid,pcpu,pmem,vsz,rss,tty,stat,start,time,command | head -10"

# Generated at 2022-06-13 11:37:12.835328
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(None)
    # testing with become_flags, but become_user and become_pass are not set
    become.get_option = lambda x: '-H -S' if x == 'become_flags' else None
    become.prompt = None
    assert become.build_become_command(['echo', '1'], 'sh') == 'sudo -H -S /bin/sh -c \'echo 1\''
    # testing with become_flags, become_user, but become_pass is not set
    become.get_option = lambda x: '-H -S' if x == 'become_flags' else 'remote_user' if x == 'become_user' else None
    become.prompt = None

# Generated at 2022-06-13 11:37:21.592686
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    becomemod = BecomeModule()
    becomemod.options = {}
    becomemod.options['_id'] = '12345'

    # when no options
    cmd = becomemod.build_become_command('ls', 'sh')
    assert cmd == 'sudo -H -S -n ls'

    # when user=foo and password=bar
    becomemod.options['become_user'] = 'foo'
    becomemod.options['become_pass'] = 'bar'
    cmd = becomemod.build_become_command('ls', 'sh')
    assert cmd == "sudo -H -S -p \"[sudo via ansible, key=12345] password:\" -u foo ls"

    # when become_exe=su and become_flags=-c and password=bar

# Generated at 2022-06-13 11:37:31.780183
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule(
        become_pass=None,
        become_exe='sudo',
        become_user='root',
        become_flags='-H -S -n',
        become_exe_new=None,
        become_user_new=None,
        become_flags_new=None,
        shell=None,
        become_pass_new=None,
        cmd=None,
        executable=None,
        _id=None
    )
    assert become_module.build_become_command('echo 1', '/bin/bash') == 'sudo -H -S -n /bin/bash -c \'(echo 1)\''


# Generated at 2022-06-13 11:37:40.879436
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule(
        become_pass=None,
        become_exe=None,
        become_flags=None,
        become_user=None,
    )
    become._id = 'test'
    become.prompt = False

    assert become.build_become_command('test', '') == 'sudo -H -S test'
    assert become.build_become_command('test', '') == 'sudo -H -S test'
    assert become.build_become_command('test', 'shell') == 'sudo -H -S shell -c "test"'
    assert become.build_become_command('test', 'shell') == 'sudo -H -S shell -c "test"'
    assert become.build_become_command('test', shell='shell') == 'sudo -H -S shell -c "test"'
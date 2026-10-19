

# Generated at 2022-06-13 11:29:26.597237
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    # initialize module
    module = BecomeModule(None)

    # test cases
    # test case 1: standard case
    cmd = 'aaa'
    shell = 'bbb'
    cmd = module.build_become_command(cmd=cmd, shell=shell)
    assert cmd == 'sudo -H -S -n aaa'

    # test case 2: sudo_exe is set
    module.options['become_exe'] = 'ccc'
    cmd = 'aaa'
    shell = 'bbb'
    cmd = module.build_become_command(cmd=cmd, shell=shell)
    assert cmd == 'ccc -H -S -n aaa'

    # test case 3: sudo_flags is set
    module.options['become_flags'] = '-p'
    cmd = 'aaa'

# Generated at 2022-06-13 11:29:34.405787
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    b = BecomeModule('become', become_user='become_user', become_exe='become_exe', become_flags='become_flags', become_pass='become_pass')
    b.prompt = 'prompt'
    b._id = '_id'
    b.success_cmd = 'success_cmd'
    
    # test with cmd
    cmd = 'cmd'
    shell = 'shell'
    result = b.build_become_command(cmd, shell)
    assert result == 'become_exe become_flags -p "prompt" -u become_user success_cmd'
    # test with empty cmd
    cmd = ''
    shell = 'shell'
    result = b.build_become_command(cmd, shell)
    assert result == ''
    # test without become_user
    b

# Generated at 2022-06-13 11:29:43.896584
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()

    become.set_option('become_user', None)
    become.set_option('become_pass', None)
    become.set_option('become_exe', None)
    become.set_option('become_flags', None)
    result = become.build_become_command('ls', '/bin/bash')
    assert(result == 'sudo -H -S -n sh -c \'echo BECOME-SUCCESS-aasdf; /bin/bash -c "ls"\'')

    become.set_option('become_user', 'test_user')
    become.set_option('become_pass', None)
    become.set_option('become_exe', None)
    become.set_option('become_flags', None)
    result = become.build

# Generated at 2022-06-13 11:29:52.946394
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    m = BecomeModule()
    m.get_option = lambda *args: 'sudo'
    m._build_success_command = lambda *args: 'true'
    m._id = 'id'

    # Test with various option combinations

# Generated at 2022-06-13 11:30:02.745857
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_pass = None

    # Test case 1
    become = BecomeModule()
    become._id = 'd0c788f6'
    become.prompt = 'password:'
    cmd = 'ls -l'
    shell = '/bin/bash'
    becomecmd = become.build_become_command(cmd, shell)
    assert becomecmd == '/bin/bash -c \'echo BECOME-SUCCESS-d0c788f6; ls -l; echo BECOME-SUCCESS-d0c788f6\''

    # Test case 2
    become = BecomeModule()
    become.prompt = 'password:'
    become._id = 'd0c788f6'
    cmd = 'ls -l'
    shell = '/bin/bash'

# Generated at 2022-06-13 11:30:12.296471
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become_module = BecomeModule()
    become_module.name = 'sudo'
    become_module._id = 'id'
    become_module.prompt = None

    become_module.get_option = lambda option: None
    assert become_module.build_become_command('cmd', 'shell') == 'sudo cmd'

    become_module.get_option = lambda option: 'sudo' if option == 'become_exe' else None
    assert become_module.build_become_command('cmd', 'shell') == 'sudo cmd'

    become_module.get_option = lambda option: '-H -S -n' if option == 'become_flags' else None
    assert become_module.build_become_command('cmd', 'shell') == 'sudo -H -S -n cmd'

    become_module.get_

# Generated at 2022-06-13 11:30:20.266448
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    become = BecomeModule()

    # Test empty command
    cmd = become.build_become_command(None, '')
    assert cmd == None

    # Test basic command
    cmd = become.build_become_command('ls', '')
    assert cmd == 'sudo -H -S -n ls'

    # Set a become user
    become.set_option('become_user', 'jjolie')
    cmd = become.build_become_command('ls', '')
    assert cmd == 'sudo -H -S -n -u jjolie ls'

    # Test password command
    become.set_option('become_pass', '123')
    cmd = become.build_become_command('ls', '')

# Generated at 2022-06-13 11:30:24.041471
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    import mock
    import collections

    test_module = collections.namedtuple('AnsibleModule', ['check_mode'])
    test_module.check_mode = False

    test_plugin = BecomeModule(test_module, become_user='test_user', become_pass='test_pass', become_exe='test_exe', become_flags=['test', 'flag'])

    test_cmd = 'test_cmd'
    test_shell = 'test_shell'

    # Test 'become_pass' field not set
    assert test_plugin.build_become_command(test_cmd, test_shell) == 'test_exe test flag -u test_user /bin/sh -c "test_cmd"'

    # Test 'become_pass' field set

# Generated at 2022-06-13 11:30:29.824837
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    from ansible.plugins.become import BecomeModule
    cmd = 'cat /etc/hosts'
    shell = '/bin/sh'
    result = '/usr/bin/sudo -H -S  -u root cat /etc/hosts'
    sudo = BecomeModule(load_info=dict(become_user='root'), runner_ident=dict(_id='bla'))
    become_cmd = sudo.build_become_command(cmd, shell)
    assert become_cmd == result

# Generated at 2022-06-13 11:30:36.922142
# Unit test for method build_become_command of class BecomeModule
def test_BecomeModule_build_become_command():
    bm = BecomeModule(become_pass='test', become_user='test', become_exe='test', become_flags='test', become_pass='test')
    assert bm.build_become_command('cmd', 'shell') == 'test -H -S -p "test" -u test (cmd) && (shell -c \'echo %s; exit 0\')'
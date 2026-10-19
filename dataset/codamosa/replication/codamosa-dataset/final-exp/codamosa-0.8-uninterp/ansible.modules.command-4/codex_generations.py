

# Generated at 2022-06-13 04:52:15.205952
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    main()
    check_command(AnsibleModule(argument_spec=dict()), './venv/bin/python ./venv/bin/ansible-playbook -i vars.yaml --private-key=~/.ssh/ansible_key -u ubuntu --sudo playbook.yaml -vvvv')

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:52:27.223863
# Unit test for function main
def test_main():
    import tempfile
    import shutil
    import filecmp
    import os
    import os.path

    test_dir = tempfile.mkdtemp()
    source_data = '''
Test string
test string
    '''

# Generated at 2022-06-13 04:52:35.485855
# Unit test for function check_command
def test_check_command():
    import ansible.module_utils.basic

    class FakeModule(ansible.module_utils.basic.AnsibleModule):
        def __init__(self, **kwargs):
            super(FakeModule, self).__init__(argument_spec={})
            self.called = []

        def _warn(self, msg):
            self.called.append(msg)

    module = FakeModule()
    check_command(module, "echo foo")
    assert module.called == []
    check_command(module, "chown root foo")

# Generated at 2022-06-13 04:52:45.375613
# Unit test for function check_command
def test_check_command():
    module = MagicMock()
    check_command(module, ['test1', 'test2'])
    check_command(module, ['test1', 'test2'])
    check_command(module, ['test1', 'test2'])
    check_command(module, ['test1'])
    check_command(module, ['test1', 'test2'])
    check_command(module, ['test1', 'test2'])
    check_command(module, ['test1', 'test2'])
    check_command(module, ['test1'])
    check_command(module, ['test1', 'test2'])
    check_command(module, ['test1', 'test2'])
    check_command(module, ['test1', 'test2'])
    check_command(module, ['test1'])

# Generated at 2022-06-13 04:52:57.625898
# Unit test for function main

# Generated at 2022-06-13 04:53:00.997239
# Unit test for function main
def test_main():
    r = '''
'''
    assert r == main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:53:12.673637
# Unit test for function main

# Generated at 2022-06-13 04:53:24.730375
# Unit test for function main
def test_main():
    from ansible.modules.command import main
    import ansible.modules.command as command
    import ansible.module_utils.command as command_utils
    import tempfile
    import os
    import shutil
    import glob
    from ansible.module_utils._text import to_native

    # Create temporary directory
    tempdir = tempfile.mkdtemp()
    directory_name = tempdir + "/test"
    os.mkdir(directory_name)
    f = open(directory_name + "/testfile", "w")
    f.close()

    # Create temporary AnsibleModule

# Generated at 2022-06-13 04:53:35.072638
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            warn=dict(type='bool', default=False),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        )
    )


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:53:47.254938
# Unit test for function main
def test_main():
    import sys
    from unittest import TextTestRunner
    from unittest.case import TestCase

    class TestModule(TestCase):
        def test_command_encoding(self):
            """Command module deals properly with unicode."""
            text = u'Caf\xe9'
            module = AnsibleModule(mock_args={})
            args = ['/bin/echo', text]
            rc, stdout, stderr = module.run_command(args, encoding=None)
            assert text in stdout

    if __name__ == '__main__':
        test = TestModule()
        runner = TextTestRunner(verbosity=2)
        runner.run(test)

    sys.exit(0)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:53:56.096330
# Unit test for function check_command
def test_check_command():
    assert()



# Generated at 2022-06-13 04:54:08.389309
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    module.warn

# Generated at 2022-06-13 04:54:20.448206
# Unit test for function main
def test_main():
    test_args = {'_raw_params': '', '_uses_shell': False, 'creates': '/root/foo', 'removes': '/root/foo'}
    test_module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    test_args['_raw_params']='dirname "/etc/nginx/sites-enabled/"'
    test_module.fail_json = {'failed': True, 'msg': 'non-zero return code'}
    test_module.exit_json = {'changed': True, 'rc': 0}
    test_module.run_command = [0, 'We are creating the file', 'An error occured']
    test_module.check_mode = False
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:54:33.157435
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(
        _raw_params=dict(),
        _uses_shell=dict(type='bool', default=False),
        argv=dict(type='list', elements='str'),
        chdir=dict(type='path'),
        executable=dict(),
        creates=dict(type='path'),
        removes=dict(type='path'),
        warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
        stdin=dict(required=False),
        stdin_add_newline=dict(type='bool', default=True),
        strip_empty_ends=dict(type='bool', default=True),
    ),
        supports_check_mode=True,
    )
    args = module.params

# Generated at 2022-06-13 04:54:41.150662
# Unit test for function main
def test_main():
    argv = [
        '-a',
        'cmd=uptime',
        '-b',
        'creates=somefile',
        '-c',
        'chdir=/tmp',
        '-d',
        'argv=["uptime"]',
        '-e',
        'executable=" "/bin/false" "',
        '-f',
        'removes=somefile',
        '-g',
        'stdin="this is my stdin"',
        '-h',
        'stdin_add_newline=False',
        '-i',
        'warn=True',
        '-j',
        'warn=False',
        '-k',
        'strip_empty_ends=False',
        '-l',
        '_uses_shell=True'
    ]

# Generated at 2022-06-13 04:54:55.080692
# Unit test for function main
def test_main():
    import os
    import platform
    import shlex
    command_name = "ansible.builtin.command"
    ansible_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    test_args = {
        '_raw_params': 'test',
        '_uses_shell': False,
        'chdir': None,
        'creates': None,
        'executable': None,
        'removes': None,
        'warn': False,
        'argv': None,
        'strip_empty_ends': True,
        'stdin': None,
        'stdin_add_newline': True,
    }
    if platform.system() == "Windows":
        test_args['_raw_params'] = 'cmd'
        test_

# Generated at 2022-06-13 04:55:07.254708
# Unit test for function main

# Generated at 2022-06-13 04:55:17.761280
# Unit test for function main
def test_main():
    import sys
    import os
    import AnsibleModule
    #fake up some ansible module args
    module_args = dict(
        executable = '/usr/bin/python',
        _raw_params = 'import sys; print (sys.argv)',
        _uses_shell = False,
        argv = ['import', 'sys', ';', 'print', '(sys.argv)', '--', '.'],
        chdir = '.',
        creates = '',
        removes = '',
        warn = True,
        stdin = "",
        stdin_add_newline = True)

    import json    
    module_args = json.dumps(module_args)
    # fake up the ansible module object
    am = AnsibleModule(module_args)
    # fake up the command module object
    cm

# Generated at 2022-06-13 04:55:24.680808
# Unit test for function main
def test_main():
    r_stdout = "Fuzzy"
    r_stderr = "Wuzzy"
    r_rc = 0
    r_changed = True
    r_cmd = ['echo', 'Fuzzy']
    r_start = "2017-09-29 22:03:48.083128"
    r_end = "2017-09-29 22:03:48.084657"
    r_delta = "0:00:00.001529"

    test_result = dict(
        msg='',
        cmd=r_cmd,
        rc=r_rc,
        stdout=r_stdout,
        stderr=r_stderr,
        changed=r_changed,
        start=r_start,
        end=r_end,
        delta=r_delta
    )

# Generated at 2022-06-13 04:55:35.399068
# Unit test for function check_command
def test_check_command():
    class ModuleStub:
        def __init__(self):
            self.warnings = []

        def warn(self, msg):
            self.warnings.append(msg)

    module = ModuleStub()
    check_command(module, '/usr/bin/chown root')
    assert module.warnings == ["Consider using the file module with owner rather than running 'chown'.  "
                               "If you need to use 'chown' because the file module is insufficient you can add 'warn: false' to "
                               "this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get "
                               "rid of this message."]
    module = ModuleStub()
    check_command(module, '/usr/bin/curl http://www.example.com/')
    assert module.warn

# Generated at 2022-06-13 04:55:58.007787
# Unit test for function main

# Generated at 2022-06-13 04:56:03.254759
# Unit test for function main
def test_main():
    args = {'_raw_params':'wget -O /tmp/zabbix-release_3.0-1+xenial_all.deb http://repo.zabbix.com/zabbix/3.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.0-1+xenial_all.deb', '_uses_shell':True}
    check_command(module, args)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:06.071181
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    check_command(module, 'ansible.builtin.command')


# Generated at 2022-06-13 04:56:17.258418
# Unit test for function main

# Generated at 2022-06-13 04:56:20.252004
# Unit test for function check_command
def test_check_command():
    commandline = 'testfile'
    result = check_command(commandline)
    assert result == 'testfile'



# Generated at 2022-06-13 04:56:29.388605
# Unit test for function main
def test_main():
    os.chdir('/tmp')

# Generated at 2022-06-13 04:56:37.094692
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native

    test_args = {'chown': 'owner', 'chmod': 'mode', 'chgrp': 'group',
                 'ln': 'state=link', 'mkdir': 'state=directory',
                 'rmdir': 'state=absent', 'rm': 'state=absent', 'touch': 'state=touch'}
    test_become = ['sudo', 'su', 'pbrun', 'pfexec', 'runas', 'pmrun', 'machinectl']

# Generated at 2022-06-13 04:56:39.200140
# Unit test for function check_command
def test_check_command():
    assert check_command(AnsibleModule(
        argument_spec=dict()
    ), 'find /foo -name bar') is None



# Generated at 2022-06-13 04:56:47.756369
# Unit test for function main
def test_main():
    #
    # Mock modules and their functions
    #
    import datetime
    import glob
    import os
    import shlex
    # consts
    failure_msg = "failed"
    rc_command = 0
    rc_msg = "non-zero return code"
    rc_zero = 0
    # dicts
    argv = {'argv': ['ls']}
    argv_fail = {'argv': ['ls', '-f']}
    argv_rm = {'argv': ['/bin/rm', '/tmp/fake_file']}
    argv_rm_ab = {'argv': ['/bin/rm', '-f', '/tmp/fake_file1', '/tmp/fake_file2', '/tmp/fake_file3']}
    chdir = {'chdir': '/'}

# Generated at 2022-06-13 04:56:57.499513
# Unit test for function main

# Generated at 2022-06-13 04:57:31.998812
# Unit test for function main
def test_main():
    test_command = ['/bin/echo', 'hello']
    test_exec = None
    test_shell = False
    test_argv = ['/bin/echo', 'hello', 'world']
    test_chdir = None
    test_creates = None
    test_removes = None
    test_warn = False
    test_stdin = None
    test_stdin_add_newline = True
    test_strip_empty_ends = True

    r = main(test_command, test_exec, test_shell, test_argv, test_chdir, test_creates, test_removes, test_warn, test_stdin, test_stdin_add_newline, test_strip_empty_ends)

    assert r['rc'] == 0
    assert r['stdout'] == 'hello\n'


# Generated at 2022-06-13 04:57:44.315436
# Unit test for function main
def test_main():
    import tempfile

    tempdir = tempfile.mkdtemp()
    tempdir1 = tempfile.mkdtemp()
    tempdir2 = tempfile.mkdtemp()
    tempdir3 = tempfile.mkdtemp()
    tempdir4 = tempfile.mkdtemp()

    # Case 1
    args = "echo hello"
    module = AnsibleModule(dict(
        _raw_params=args,
        _uses_shell=False,
    ))
    main()
    assert module.exit_json.call_count == 1

    # Case 2
    args = "echo hello"
    module = AnsibleModule(dict(
        _raw_params=args,
        _uses_shell=False,
        argv=args.split()
    ))
    main()
    assert module.exit_json.call_count

# Generated at 2022-06-13 04:57:54.435791
# Unit test for function main
def test_main():
    arg_spec = dict(
        _raw_params=dict(),
        _uses_shell=dict(type='bool', default=False),
        argv=dict(type='list', elements='str'),
        chdir=dict(type='path'),
        executable=dict(),
        creates=dict(type='path'),
        removes=dict(type='path'),
        # The default for this really comes from the action plugin
        warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
        stdin=dict(required=False),
        stdin_add_newline=dict(type='bool', default=True),
        strip_empty_ends=dict(type='bool', default=True),
    )

# Generated at 2022-06-13 04:58:03.131179
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    basic._ANSIBLE_ARGS = to_bytes(
        json.dumps({
            'ANSIBLE_MODULE_ARGS': {
                '_raw_params': 'echo test_command_module',
                '_uses_shell': False,
                'chdir': None,
                'executable': None,
                'creates': None,
                'removes': None,
                'warn': False,
                'stdin': None,
                'stdin_add_newline': True,
                'strip_empty_ends': True
            }
        })
    )
    with patch('ansible.module_utils.basic.AnsibleModule') as mock_class:
        instance = mock_class.return_value

# Generated at 2022-06-13 04:58:13.030413
# Unit test for function main
def test_main():
    test_ = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            # The default for this really comes from the action plugin
            warn=dict(type='bool', default=False),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    main()


# Generated at 2022-06-13 04:58:25.380489
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    module.run

# Generated at 2022-06-13 04:58:37.256887
# Unit test for function main
def test_main():
    # create test variable
    os.environ['ANSIBLE_MODULE_ARGS'] = '{"_raw_params": "echo hello", "warn": false}'
    os.environ['ANSIBLE_MODULE_NAME'] = 'command'
    r = main()
    assert r['stdout'] == 'hello'
    assert r['stderr'] == ''
    assert r['rc'] == 0
    assert r['cmd'] == ['echo', 'hello']

    # create test variable
    os.environ['ANSIBLE_MODULE_ARGS'] = '{"_raw_params": "ls /not/exist/path"}'
    os.environ['ANSIBLE_MODULE_NAME'] = 'command'
    r = main()
    assert r['stdout'] == ''
    assert r['stderr'] == ''

# Generated at 2022-06-13 04:58:41.155863
# Unit test for function main
def test_main():
    # prepare
    data = {
        '_raw_params': 'echo hello',
        '_uses_shell': False,
        'argv': None,
        'chdir': None,
        'creates': None,
        'removes': None,
        'warn': False,
        'stdin': None,
        'stdin_add_newline': True,
        'strip_empty_ends': True,
    }
    module = AnsibleModule(argument_spec=dict())
    module.params = data
    # run
    main()


# Generated at 2022-06-13 04:58:50.603504
# Unit test for function main

# Generated at 2022-06-13 04:58:51.140168
# Unit test for function main
def test_main():
    assert True == True

# Generated at 2022-06-13 04:59:51.596780
# Unit test for function main
def test_main():
    class MockModule(object):
        def __init__(self):
            self.params = dict()
            self.check_mode = False
            self.fail_json = Mock(side_effect=SystemExit)
            self.exit_json = Mock(side_effect=SystemExit)
            self.run_command = Mock(return_value=(0, 'mock stdout', 'mock stderr'))
            self.warn = Mock()

    module = MockModule()
    module.params['_raw_params'] = 'test-command'
    module.params['chdir'] = None
    module.params['executable'] = None
    module.params['creates'] = None
    module.params['removes'] = None
    module.params['warn'] = False
    module.params['stdin'] = None
    module.params

# Generated at 2022-06-13 04:59:54.287041
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={'warn': {'type': 'bool', 'default': True}})
    command = 'curl https://example.com'
    check_command(module, command)


# Generated at 2022-06-13 05:00:01.341218
# Unit test for function main
def test_main():
    with mock.patch('ansible_collections.ansible.builtin.plugins.module_utils.basic._ANSIBLE_ARGS',
    new=dict(
        tags={'foo': True},
        ignore_tags={'not-foo': True},
    )):
        with pytest.raises(SystemExit) as pytest_e:
            main()



# Generated at 2022-06-13 05:00:13.719860
# Unit test for function main

# Generated at 2022-06-13 05:00:23.793835
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='/usr/bin/make_database.sh db_user db_name creates=/path/to/database',
        chdir='somedir/',
        executable='/usr/bin/foo',
        creates='/path/to/database',
        removes='/path/to/database',
        warn=True,
        stdin=True,
        stdin_add_newline=True,
        strip_empty_ends=True,
    )

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:00:33.807908
# Unit test for function main

# Generated at 2022-06-13 05:00:46.115281
# Unit test for function main
def test_main():
    argv = [os.path.basename(__file__),
            '-a', 'ls',
            '-b', 'id_rsa_jie',
            '-c', './',
            '-d', 'False',
            '-e', 'ls',
            '-f', './',
            '-g', 'python',
            '-h', 'True',
            '-i', 'ls',
            '-j', 'True',
            '-k', 'False']
    with mock.patch.object(sys, 'argv', argv):
        main()
    #assert main() == 0


if __name__ == '__main__':
    import sys
    import mock
    test_main()

# Generated at 2022-06-13 05:00:50.753925
# Unit test for function check_command
def test_check_command():
    from ansible.modules.connection.connection import check_command
    from ansible.module_utils.common.collections import MOCK_MODULE
    mod = MOCK_MODULE()
    cmd = ['ansible']
    check_command(mod, cmd)
    cmd = 'ansible'
    check_command(mod, cmd)

# ===========================================
# ansible module specific support methods.
#


# Generated at 2022-06-13 05:01:02.082462
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='ls',
        # _uses_shell='False',
        argv='ls',
        chdir='/home/yury',
        executable='/bin/false',
        creates='./test',
        removes='./test2',
        stdin='test',
        stdin_add_newline=True,
        strip_empty_ends=True,
        warn=True,
        )

    r = dict(
        changed=False,
        stdout='',
        stderr='',
        rc=None,
        cmd=None,
        start=None,
        end=None,
        delta=None,
        msg='',
        )


# Generated at 2022-06-13 05:01:12.707135
# Unit test for function main
def test_main():

    def test_argv(mocker, module_args, argv_input, result):
        _args = module_args.copy()
        _args['argv'] = argv_input
        _args['_raw_params'] = ''
        module = AnsibleModule(**_args)
        result['msg'] = ''
        main()

    # This is a list of lists each containing the following elements:
    # test description, module options, argv input, expected results
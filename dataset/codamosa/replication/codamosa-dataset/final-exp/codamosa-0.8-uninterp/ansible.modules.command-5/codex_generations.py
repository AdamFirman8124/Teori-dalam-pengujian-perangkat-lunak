

# Generated at 2022-06-13 04:52:18.089721
# Unit test for function check_command
def test_check_command():
    import ansible.module_utils
    m = ansible.module_utils.basic.AnsibleModule(
            argument_spec = dict(
                foo = dict(default='bar')
            )
    )
    check_command(m, "foo")
    assert not m.warnings
    check_command(m, "sudo foo")
    assert len(m.warnings) == 1 # don't warn twice, since test already ran.
    check_command(m, "curl")
    assert len(m.warnings) == 2
    check_command(m, "rpm")
    assert len(m.warnings) == 3
    check_command(m, "tar")
    assert len(m.warnings) == 4
    check_command(m, "chown")
    assert len(m.warnings) == 5


# Generated at 2022-06-13 04:52:29.251831
# Unit test for function main

# Generated at 2022-06-13 04:52:32.954648
# Unit test for function check_command
def test_check_command():
    # simple execution
    m = AnsibleModule(argument_spec={'commands': {'type': 'str'}})
    check_command(m, ['echo', 'hello'])



# Generated at 2022-06-13 04:52:41.380231
# Unit test for function main
def test_main():
    # From Ansible 2.4, check_mode is always true
    check_mode = True

# Generated at 2022-06-13 04:52:54.750393
# Unit test for function main
def test_main():
    args = dict(
        argv=['/usr/bin/make_database.sh', 'db_user', 'db_name'],
        creates='/path/to/database',
        chdir='somedir/',
        become='yes',
        become_user='db_owner'
    )
    Check = dict(
        changed=True,
        cmd=['/usr/bin/make_database.sh', 'db_user', 'db_name'],
        end='',
        start='',
        delta='',
        msg='non-zero return code',
        rc=0,
        stderr='',
        stdout='',
        stderr_lines=[],
        stdout_lines=[]
    )

# Generated at 2022-06-13 04:52:59.455099
# Unit test for function main
def test_main():
    # fake args
    args = {'_raw_params': 'echo hello world',
            '_uses_shell': False,
            'argv': None,
            'chdir': None,
            'creates': None,
            'executable': None,
            'removes': None,
            'stdin': None,
            'stdin_add_newline': True,
            'strip_empty_ends': True,
            'warn': False}

    with pytest.raises(SystemExit):
        main()


# Generated at 2022-06-13 04:53:12.005173
# Unit test for function main
def test_main():
    import sys

# Generated at 2022-06-13 04:53:23.939782
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleMock
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 04:53:27.210527
# Unit test for function main
def test_main():
    import pytest
    args = {}
    args['_raw_params'] = ""
    args['_uses_shell'] = False
    args['argv'] = ""
    args['chdir'] = ""
    args['executable'] = ""
    args['creates'] = ""
    args['removes'] = ""
    args['warn'] = False
    args['stdin'] = ""
    args['stdin_add_newline'] = True
    args['strip_empty_ends'] = True
    result = main()
    assert result is None

# Generated at 2022-06-13 04:53:39.777233
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(type='str'),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='str'),
            executable=dict(type='str'),
            creates=dict(type='str'),
            removes=dict(type='str'),
            warn=dict(type='bool', default=False),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 04:54:01.388404
# Unit test for function main
def test_main():
    host_args = dict(
        _raw_params='echo hello',
        _uses_shell=True,
    )

# Generated at 2022-06-13 04:54:10.643137
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule({})
    check_command(module, ['curl', 'http://www.ansible.com'])
    assert module.warnings[-1]['msg'].startswith('Consider using the get_url or uri')

    module = AnsibleModule({})
    check_command(module, 'curl http://www.ansible.com')
    assert module.warnings[-1]['msg'].startswith('Consider using the get_url or uri')

    module = AnsibleModule({})
    check_command(module, 'pbrun -u bob /usr/bin/foo')
    assert module.warnings[-1]['msg'] == "Consider using 'become', 'become_method', and 'become_user' rather than running pbrun"


# Generated at 2022-06-13 04:54:17.777432
# Unit test for function main
def test_main():
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    from ansible.module_utils.ansible_release import __version__


# Generated at 2022-06-13 04:54:25.819426
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    test_arguments = dict(
        _raw_params='echo hello',
        _uses_shell=False,
        argv=dict(type='list', elements='str'),
        chdir=dict(type='path'),
        executable=dict(),
        creates=dict(type='path'),
        removes=dict(type='path'),
        warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
        stdin=dict(required=False),
        stdin_add_newline=dict(type='bool', default=True),
        strip_empty_ends=dict(type='bool', default=True),
        check_mode=True
    )


# Generated at 2022-06-13 04:54:36.769222
# Unit test for function main
def test_main():
    module = import_module('ansible.modules.command')
    module.sys.modules['json'] = import_module('json')
    module.sys.modules['os'] = import_module('os')
    module.sys.modules['shlex'] = import_module('shlex')
    module.sys.modules['glob'] = import_module('glob')
    module.sys.modules['ansible.module_utils.basic'] = import_module('ansible.module_utils.basic')
    module.sys.modules['ansible.module_utils.urls'] = import_module('ansible.module_utils.urls')
    module.sys.modules['ansible.module_utils.six'] = import_module('ansible.module_utils.six')

# Generated at 2022-06-13 04:54:46.634314
# Unit test for function main

# Generated at 2022-06-13 04:54:57.398429
# Unit test for function check_command
def test_check_command():
    import ansible.module_utils.basic
    test_module = ansible.module_utils.basic.AnsibleModule(argument_spec=dict())
    # test no warning is set by default
    check_command(test_module, ["/dev/null"])
    assert not test_module.warn.called
    # test commands that are warned on
    check_command(test_module, ["chown"])
    assert test_module.warn.called
    # test commands that are warned on
    check_command(test_module, ["curl"])
    assert test_module.warn.called
    # test become commands
    check_command(test_module, ["sudo"])
    assert test_module.warn.called



# Generated at 2022-06-13 04:55:03.251635
# Unit test for function check_command
def test_check_command():
    assert check_command(None, 'svn') == 'subversion'
    assert check_command(None, 'tar') == 'unarchive'
    assert check_command(None, 'rm') == 'file'
    assert check_command(None, 'mv') == 'None'



# Generated at 2022-06-13 04:55:11.996895
# Unit test for function check_command
def test_check_command():
    """
    Unit test for function check_command
    """
    from ansible.module_utils.basic import AnsibleModule

    class TestAnsibleModule(AnsibleModule):
        def __init__(self):
            arg_spec = dict()
            super(TestAnsibleModule, self).__init__(
                argument_spec=arg_spec,
                supports_check_mode=True
            )

    module = TestAnsibleModule()
    module.warnings = []
    commandline = 'chown Jason /abc'
    check_command(module, commandline)

# Generated at 2022-06-13 04:55:24.447296
# Unit test for function main
def test_main():
    args = {
        '_raw_params': 'pwd',
        '_uses_shell': True,
        'argv': '',
        'chdir': None,
        'executable': None,
        'creates': None,
        'removes': None,
        'warn': True,
        'stdin': '',
        'stdin_add_newline': True,
        'strip_empty_ends': True,
    }

# Generated at 2022-06-13 04:55:47.241008
# Unit test for function main

# Generated at 2022-06-13 04:55:59.543959
# Unit test for function main
def test_main():
    from ansible.module_utils.common.collections import Mapping
    import json
    import time
    import datetime

    from ansible.module_utils.six import PY3


# Generated at 2022-06-13 04:56:13.632539
# Unit test for function main
def test_main():
    cmd = 'echo hello'
    argv = ['echo', 'hello']
    args = 'echo hello'
    stdin = 'echo hello'

    def run_command(argv, executable=None, use_unsafe_shell=False, data=None, binary_data=False):
        if argv == args:
            return 0, '', ''
        if argv == argv:
            return 0, '', ''
        return 0, '', ''


# Generated at 2022-06-13 04:56:25.991382
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(type='str'),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(type='str'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            # The default for this really comes from the action plugin
            warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
            stdin=dict(type='str'),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )


# Generated at 2022-06-13 04:56:29.740581
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:32.824956
# Unit test for function main
def test_main():
    # check sanity of expected return
    r = main()
    assert isinstance(r, dict)
    assert 'cmd' in r
    assert isinstance(r['cmd'], list)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:36.287534
# Unit test for function main
def test_main():
    # main(module=None)
    module = None
    # test_return = main(module)
    # assert test_return == True


# Generated at 2022-06-13 04:56:42.069275
# Unit test for function main
def test_main():
    test = dict()
    test['chdir'] = ''
    test['executable'] = ''
    test['creates'] = ''
    test['removes'] = ''
    test['args'] = '/bin/echo test'
    test['argv'] = ''
    rc, out, err = main(test)
    print(out)
    assert 'test' in out

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:44.079548
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:56.079435
# Unit test for function main

# Generated at 2022-06-13 04:57:23.594134
# Unit test for function main
def test_main():
    args = dict(
        _raw_params = 'cmd',
        _uses_shell = False,
        argv = 'list',
        chdir = '''/home''',
        executable = None,
        creates = '/home/',
        removes = '~/',
        warn = False,
        stdin = '''hello''',
        stdin_add_newline = True,
        strip_empty_ends = True
        )

    r = dict(
        changed = True,
        stdout = '',
        stderr = '',
        rc = 0,
        msg = ''
        )

    module = AnsibleModule(argument_spec=args, supports_check_mode=True)
    obj = main()

    assert obj['changed'] == r['changed']

# Generated at 2022-06-13 04:57:35.866544
# Unit test for function main

# Generated at 2022-06-13 04:57:40.444792
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import is_iterable
    main()
    main()
    main()
    main()


# Generated at 2022-06-13 04:57:49.487638
# Unit test for function main
def test_main():
    args = dict(
        _uses_shell=False,
        argv='/usr/bin/make_database.sh db_user db_name creates=/path/to/database',
        chdir='somedir/',
        executable=None,
        creates=None,
        removes=None,
        warn=False,
        stdin=None,
        stdin_add_newline=True,
        strip_empty_ends=True,
        _raw_params='')

# Generated at 2022-06-13 04:58:00.652197
# Unit test for function main

# Generated at 2022-06-13 04:58:06.969025
# Unit test for function check_command
def test_check_command():
    # NOTE: These tests aren't true unit tests but more functional tests.  They are being
    #       kept in the functional tests because they are more functional and test more
    #       that just the unit tested.  They also need a lot of code to run safely in a
    #       unit test environment.
    test_module = AnsibleModule(argument_spec={})
    test_module.warn = lambda msg: test_module.fail_json(msg=msg)


# Generated at 2022-06-13 04:58:08.599800
# Unit test for function main
def test_main():
    # Replace assert with "import pytest; pytest.fail()" to force a test failure
    assert True

# Generated at 2022-06-13 04:58:14.993923
# Unit test for function main
def test_main():
    args = [
        dict(
            _raw_params='',
            _uses_shell=False,
            argv=[],
            chdir='',
            executable='',
            creates={},
            removes={},
            warn=False,
            stdin={},
            stdin_add_newline=True,
            strip_empty_ends=True,
        )
    ]
    result = dict(
        msg = 'no command given',
        rc = 256,
    )
    module = AnsibleModule(argument_spec=dict())
    for arg in args:
        module.params = arg
        r = main()
        assert r['msg'] == result['msg']
        assert r['rc'] == result['rc']

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:26.992686
# Unit test for function main

# Generated at 2022-06-13 04:58:27.507469
# Unit test for function main
def test_main():
    assert True == True

# Generated at 2022-06-13 04:59:21.380912
# Unit test for function main

# Generated at 2022-06-13 04:59:27.706206
# Unit test for function main
def test_main():
    # Test case for function main with fails
    print('Test case for function main')
    # Fail

# Generated at 2022-06-13 04:59:38.802481
# Unit test for function main
def test_main():

    # Test cases
    # Test 1: Test with args "command line"
    module_args = {'_raw_params': 'command line', '_uses_shell': True, 'argv': None, 'chdir': None, 'executable': None, 'creates': None, 'removes': None, 'warn': False, 'stdin': None, 'stdin_add_newline': True, 'strip_empty_ends': True}
    module_return_value = {'changed': False, 'cmd': 'command line', 'end': None, 'failed': False, 'rc': 256, 'start': None, 'stderr': '', 'stderr_lines': [], 'stdout': '', 'stdout_lines': []}
    # Test 1: Test with args "command line"

# Generated at 2022-06-13 04:59:50.299858
# Unit test for function main
def test_main():
    test_var = {
        "_raw_params": "cat /etc/motd",
        "_uses_shell": False,
        "argv": [
            "cat",
            "/etc/motd"
        ],
        "chdir": "",
        "creates": "",
        "executable": None,
        "removes": "",
        "stdin": None,
        "stdin_add_newline": True,
        "strip_empty_ends": True,
        "warn": True
    }

# Generated at 2022-06-13 04:59:57.609290
# Unit test for function main
def test_main():
    args = {}
    args['_raw_params'] = 'touch foo'
    args['creates'] = '/tmp/foo'
    args['chdir'] = '/tmp'

    m = AnsibleModule(**args)
    main_test(args, m)

    args['_raw_params'] = 'touch foo'
    args['removes'] = '/tmp/foo'
    args['chdir'] = '/tmp'

    m = AnsibleModule(**args)
    main_test(args, m)

    args['_raw_params'] = 'badcommand'
    m = AnsibleModule(**args)
    main_test(args, m)

    args['_raw_params'] = 'touch foo'
    args['creates'] = '/tmp/foo'
    args['_uses_shell'] = True

# Generated at 2022-06-13 05:00:00.574275
# Unit test for function main
def test_main():
    from ansible.modules.commands.command import main
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:00:06.757614
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec = dict(
            os = dict(type = 'str', required = False)
        )
    )
    m_args = dict(
        os = 'none'
    )
    main(test_module.params)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:00:17.242517
# Unit test for function main
def test_main():
    #Simulate arguments to script
    args = ['-a', 'test.yml', 'testplaybook.yml']
    #Specify values for the module params
    module_args = dict(
    warn=True,
    )

    set_module_args(module_args)
    #Intercept exit and fail calls so program can throw an exception and still complete
    with ExitStack() as stack:
        #Redirect stdout and stderr to a buffer so we can test the output
        stdout_buffer = io.StringIO()
        stack.enter_context(redirect_stdout(stdout_buffer))
        stderr_buffer = io.StringIO()
        stack.enter_context(redirect_stderr(stderr_buffer))
        #Run our main function
        main()
        #Get the stdout and

# Generated at 2022-06-13 05:00:26.331365
# Unit test for function main
def test_main():
    # check module arguments
    args = dict(
        _raw_params='cat /etc/motd',
        _uses_shell=False,
        argv=['cat', '/etc/motd'],
        chdir='/',
        executable=None,
        creates=None,
        removes=None,
        warn=False,
        stdin=None,
        stdin_add_newline=False,
        strip_empty_ends=False,
    )



if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:00:35.565212
# Unit test for function check_command
def test_check_command():
    class FakeModule(object):
        def __init__(self):
            self.warnings = []
        def warn(self, msg):
            self.warnings.append(msg)

    m = FakeModule()
    check_command(m, ['/usr/bin/chown', 'user', 'file'])
    check_command(m, ['/usr/bin/chmod', '0420', 'file'])
    check_command(m, ['/usr/bin/chgrp', 'group', 'file'])
    check_command(m, ['/usr/bin/ln', '-s', 'file1', 'file2'])
    check_command(m, ['/usr/bin/mkdir', 'path'])
    check_command(m, ['/usr/bin/rmdir', 'path'])
   
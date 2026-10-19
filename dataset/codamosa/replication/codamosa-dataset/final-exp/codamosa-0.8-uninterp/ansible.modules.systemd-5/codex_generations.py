

# Generated at 2022-06-13 06:21:03.488833
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    lines = [
        "Type=simple",
        "DefaultDependencies=no",
        "UnitFileState=enabled",
        "UnitFilePreset=disabled",
        "UnitFileStateResult=disabled",
        "Description=This is a multiline description that ends with a bracket }",
        "Before=multi-user.target",
        "After=",
        "ExecStartPre=-/bin/bash -c 'if [ -r /etc/selinux/config ]; then grep -q \"^SELINUX=\" /etc/selinux/config && setenforce 0; fi'",
        "ExecStart=/bin/bash -c 'echo \"This is a multiline ExecStart value\"; echo \"and it ends with a bracket }\"'",
        ]

# Generated at 2022-06-13 06:21:15.177281
# Unit test for function main

# Generated at 2022-06-13 06:21:25.163843
# Unit test for function main
def test_main():
    class MockModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def warn(self, msg):
            print(msg)

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception(kwargs['msg'])

        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs

    # Test case 1:
    # Put a test case for each execution of main() that should throw an exception
    # The main() function is called using the unit test's params
    # The unit test checks the exception and arguments to exit_json()
    # Put a test case for each assert in your main()

# Generated at 2022-06-13 06:21:32.134380
# Unit test for function main
def test_main():
    """Test module functionality"""
    file_name = os.path.join(sys.path[0], 'unit_tests/ansible_systemd_test_script')
    daemon_reload_failure_expected_output = {
        "failed": True,
        "msg": "failure %d during daemon-reload: %s" % (1, "AOEUT AOEUT\n"),
    }
    daemon_reload_success_expected_output = {
        "changed": True,
    }
    daemon_reexec_failure_expected_output = {
        "failed": True,
        "msg": "failure %d during daemon-reexec: %s" % (1, "AOEUT AOEUT\n"),
    }

# Generated at 2022-06-13 06:21:44.074109
# Unit test for function main
def test_main():
    expect = dict(
        name=None,
        changed=False,
        status=dict(),
    )

# Generated at 2022-06-13 06:21:52.013570
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    lines = [
        'Description={',
        '  This is a single line that doesn\'t end with a }.',
        '}',
        'Multi-line={',
        '  This is a multi-line value that',
        '  spreads across three lines and',
        '  ends with a }.',
        '}'
    ]
    assert parse_systemctl_show(lines) == {
        'Multi-line': 'This is a multi-line value that spreads across three lines and ends with a }.',
        'Description': 'This is a single line that doesn\'t end with a }.'
    }

# Generated at 2022-06-13 06:22:05.124631
# Unit test for function main
def test_main():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch

    with patch("os.getenv") as os_getenv:
        os_getenv.return_value = None

        with patch("os.environ") as os_environ:
            os_environ.get.return_value = None

            with patch("ansible_collections.ansible.community.plugins.modules.systemd.syd.os.environ") as os_environ:
                os_environ.get.return_value = None

                with patch("ansible_collections.ansible.community.plugins.modules.systemd.syd.os.path.exists") as path_exists:
                    path_exists.return_value = True


# Generated at 2022-06-13 06:22:16.796996
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    """
    Insure that parse_systemctl_show() can parse unit files with values on one line and values on multiple lines
    """
    unit_file_single_line = '''
        Description=foo
        ExecStart=bar
    '''
    result = parse_systemctl_show(unit_file_single_line.split('\n'))
    assert type(result) == dict
    assert len(result) == 2
    assert result['Description'] == 'foo'
    assert result['ExecStart'] == 'bar'

    unit_file_multi_line = '''
        Description=foo
        ExecStart={ bar
        }
    '''
    result = parse_systemctl_show(unit_file_multi_line.split('\n'))
    assert type(result) == dict
    assert len(result) == 2
   

# Generated at 2022-06-13 06:22:20.807059
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored("")
    assert request_was_ignored("= to 'stop'")
    assert not request_was_ignored("'stop'")
#

# Generated at 2022-06-13 06:22:25.891477
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert not request_was_ignored('[  OK  ]')
    assert request_was_ignored('[  OK  ] ignoring request')
    assert request_was_ignored('[  OK  ] ignoring command')
    assert not request_was_ignored('[  OK  ] ignored')



# Generated at 2022-06-13 06:23:00.779083
# Unit test for function main
def test_main():
    result = dict(
        status=dict(
            LoadState='loaded',
            ActiveState='running',
            SubState='running',
            FragmentPath='/lib/systemd/system/fail2ban.service',
            UnitFileState='enabled',
            UnitFileStateLoad='enabled',
        ),
        enabled=False,
        state='started',
        changed=True,
        name='fail2ban',
    )

    class AnsibleModuleTest(AnsibleModule):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fail_json = lambda **kwargs: kwargs
            self.exit_json = lambda **kwargs: result.update(kwargs)

# Generated at 2022-06-13 06:23:10.846470
# Unit test for function main
def test_main():
    "Test the function main"
    from ansible.module_utils import basic
    from ansible.module_utils.common.dict_transformations import nested_update
    from ansible.module_utils.system import systemctl as module

    name = 'httpd'


# Generated at 2022-06-13 06:23:18.718379
# Unit test for function main

# Generated at 2022-06-13 06:23:22.137103
# Unit test for function main
def test_main():
    class Args:
        name = None
        state = None
        enabled = None
        masked = None
        daemon_reload = False
        daemon_reexec = False
        scope = None
        no_block = False
    args = Args()
    args.name='sshd'
    args.state='restarted'
    main(args)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:31.298757
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:23:40.658222
# Unit test for function main
def test_main():
    # Define arguments and parameters values
    _module_args = dict(name=dict(type='str', aliases=['service', 'unit']),
                        state=dict(type='str', choices=['reloaded', 'restarted', 'started', 'stopped']),
                        enabled=dict(type='bool'),
                        force=dict(type='bool'),
                        masked=dict(type='bool'),
                        daemon_reload=dict(type='bool', default=False, aliases=['daemon-reload']),
                        daemon_reexec=dict(type='bool', default=False, aliases=['daemon-reexec']),
                        scope=dict(type='str', default='system', choices=['system', 'user', 'global']),
                        no_block=dict(type='bool', default=False),
                       )

    _supports_

# Generated at 2022-06-13 06:23:44.374553
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleExitJson) as result:
        main()
    assert result.value.args[0]['changed']



# Generated at 2022-06-13 06:23:54.396649
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:00.621345
# Unit test for function main
def test_main():
    import tempfile
    import os
    (fd, tempFile) = tempfile.mkstemp()
    os.close(fd)

# Generated at 2022-06-13 06:24:12.425354
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test single-line value with no multi-line value
    out = [
        'Type=simple',
        'Result=success'
    ]
    assert parse_systemctl_show(out) == {'Type': 'simple', 'Result': 'success'}

    # Test multi-line value (ExecReload), consisting of three lines
    out = [
        'Type=simple',
        'ExecReload={',
        'path=/bin/kill; argv[]=/bin/kill -HUP $MAINPID; ignore_errors=no;',
        '}',
        'Result=success'
    ]

# Generated at 2022-06-13 06:25:09.245269
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show(['Foo=bar', 'Baz=apple', 'Eggs=scrambled', 'Eggs=continued', 'Eggs=finished', 'Baz=pear']) == {'Foo': 'bar', 'Baz': 'apple', 'Eggs': 'scrambled\ncontinued\nfinished'}
    assert parse_systemctl_show(['ExecStart=foo', 'ExecStart=bar', 'ExecStart=baz']) == {'ExecStart': 'foo\nbar\nbaz'}

# Generated at 2022-06-13 06:25:20.937414
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # One-line value
    lines = ['Description=A one-line value']
    data = parse_systemctl_show(lines)
    assert len(data) == 1
    assert data['Description'] == 'A one-line value'
    # Two-line value
    lines = ['Description=A two-line value', 'that spans two lines']
    data = parse_systemctl_show(lines)
    assert len(data) == 1
    assert data['Description'] == 'A two-line value that spans two lines'
    # Multi-line value with embedded newlines
    lines = ['ExecStart={', 'path=/bin/true', 'argv[]=', '}']
    data = parse_systemctl_show(lines)
    assert len(data) == 1

# Generated at 2022-06-13 06:25:23.046142
# Unit test for function main
def test_main():
    pass

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:33.646380
# Unit test for function main

# Generated at 2022-06-13 06:25:41.579211
# Unit test for function main

# Generated at 2022-06-13 06:25:47.767421
# Unit test for function main
def test_main():
    test_fail_args = dict(
        name='ansible-test-service',
        state='started',
        enabled=None,
        masked=None,
        daemon_reload=None,
        force=None,
    )
    test_pass_args = dict(
        name='ansible-test-service',
        state='started',
        daemon_reload=None,
        force=None,
        scope='user',
    )
    test_fail_args_init = dict(
        name='ansible-test-service',
        state='started',
        daemon_reload=None,
        force=None,
        scope='system',
    )

# Generated at 2022-06-13 06:25:55.961085
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:26:03.116598
# Unit test for function main
def test_main():
    result = {
        'name': 'httpd',
        'changed': False,
        'status': {},
    }

    result_masked = {
        'name': 'httpd',
        'changed': True,
        'status': {},
    }
    with patch.object(AnsibleModule, 'run_command') as mock_cmd:
        mock_cmd.return_value = (0, '', '')

# Generated at 2022-06-13 06:26:14.013023
# Unit test for function main
def test_main():
    import os
    import tempfile

    filename = 'test_systemd.py'
    module = imp.new_module(filename)
    module.__file__ = filename

    builder = AnsibleModuleBuilder(module)

# Generated at 2022-06-13 06:26:16.792531
# Unit test for function main
def test_main():
    module = AnsibleModule({
        'name': 'test',
        'enabled': False,
        'force': False,
        'masked': False,
    })
    assert main() == 'success', 'Failed to get success message.'

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:03.127666
# Unit test for function main

# Generated at 2022-06-13 06:27:12.794082
# Unit test for function main

# Generated at 2022-06-13 06:27:20.861059
# Unit test for function main
def test_main():
    os.mkdir("testdata")
    os.chdir("testdata")
    f = open("test.service","w")
    f.write("""[Unit]
Description=Text to speech for fritzbox
After=network.target
Before=multi-user.target

[Service]
ExecStart=/usr/bin/svoxpico2wave -w /dev/shm/file.wav -l de-DE "

[Install]
WantedBy=default.target
""")
    f.close()

# Generated at 2022-06-13 06:27:32.909225
# Unit test for function main
def test_main():
    unit = 'anacron.service'
    state = 'stopped'
    enabled = True
    masked = False
    daemon_reload = False

    # mock module input data
    module = AnsibleModule(argument_spec=dict(name=dict(type='str', aliases=['service', 'unit']),
                                              state=dict(type='str', choices=['reloaded', 'restarted', 'started', 'stopped']),
                                              enabled=dict(type='bool'),
                                              force=dict(type='bool'),
                                              masked=dict(type='bool'),
                                              daemon_reload=dict(type='bool', default='False'),
                                              daemon_reexec=dict(type='bool', default='False'),
                                              ),
                           supports_check_mode=True)


# Generated at 2022-06-13 06:27:41.735041
# Unit test for function main

# Generated at 2022-06-13 06:27:47.347956
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show([
        'UnitFileState=enabled',
        'Description=a single-line value that starts with {',
        'ExecStart={'
    ]) == {
        'UnitFileState': 'enabled',
        'Description': 'a single-line value that starts with {',
        'ExecStart': '{\n'
    }
    assert parse_systemctl_show([
        'ExecStart={',
        'some value',
        '}',
        'Wants=something.service'
    ]) == {
        'ExecStart': '{\nsome value\n}\n',
        'Wants': 'something.service'
    }
# /Unit test for function parse_systemctl_show



# Generated at 2022-06-13 06:27:52.500000
# Unit test for function main
def test_main():
    test_unit_start = {
        'status':
            {'ActiveState': "active",
             'MainPID': '1',
             'StartLimitIntervalSec': '10',
             'StartLimitBurst': '5',
             'Type': 'notify',
             'ExecMainStatus': '0',
             'SubState': 'running'},
        'enabled': False,
        'changed': False,
        'state': 'started'
    }


# Generated at 2022-06-13 06:28:00.854249
# Unit test for function main

# Generated at 2022-06-13 06:28:13.506019
# Unit test for function main
def test_main():
    unit = 'crond.service'
    state = 'started'
    enabled = True
    masked = False
    daemon_reload = False
    daemon_reexec = False
    scope = 'system'
    no_block = False

# Generated at 2022-06-13 06:28:23.979664
# Unit test for function main

# Generated at 2022-06-13 06:29:31.462881
# Unit test for function main
def test_main():
    # FIXME: Add unit test for functions in this file.
    assert False, "Not implemented"

# import module snippets
from ansible.module_utils.basic import *

main()

# Generated at 2022-06-13 06:29:32.475975
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:29:39.032872
# Unit test for function main

# Generated at 2022-06-13 06:29:48.524361
# Unit test for function main
def test_main():
    import tempfile
    files = []
    for name in ('systemctl', 'initctl'):
        with tempfile.NamedTemporaryFile(mode='w+b', delete=False) as f:
            files.append(f.name)
            if name == 'systemctl':
                f.write('#!/bin/sh\necho "LoadState=loaded\nActiveState=active"\nexit 0')
            if name == 'initctl':
                f.write('#!/bin/sh\nexit 0')
        os.chmod(f.name, 0o755)

    saved_env = dict(os.environ)

# Generated at 2022-06-13 06:29:55.194181
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule

    # Params

# Generated at 2022-06-13 06:30:03.206744
# Unit test for function main
def test_main():
    import sys
    import StringIO
    import json
    class AnsibleModuleMock:
        def __init__(self, argument_spec, required_one_of, required_by):
            self.argument_spec = argument_spec
            self.required_one_of = required_one_of
            self.required_by = required_by
        def get_bin_path(self, path, required):
            return path
        def run_command(self, cmd, check_rc=None):
            return 0, "", ""
        def fail_json(self, msg):
            raise Exception(msg)
        def exit_json(self, **kwargs):
            print(json.dumps(kwargs))
    sys.stdout = StringIO.StringIO()

# Generated at 2022-06-13 06:30:09.117294
# Unit test for function main

# Generated at 2022-06-13 06:30:19.249905
# Unit test for function main

# Generated at 2022-06-13 06:30:33.513816
# Unit test for function main
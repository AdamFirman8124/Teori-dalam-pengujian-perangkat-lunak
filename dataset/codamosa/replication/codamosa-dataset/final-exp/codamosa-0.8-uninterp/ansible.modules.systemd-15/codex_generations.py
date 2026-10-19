

# Generated at 2022-06-13 06:21:23.634742
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # test empty input
    assert parse_systemctl_show([]) == {}
    # test a few simple parses
    assert parse_systemctl_show(['a=b']) == {'a': 'b'}
    assert parse_systemctl_show(['a=', 'b=c']) == {'a': '', 'b': 'c'}
    assert parse_systemctl_show(['a=b', 'c=d']) == {'a': 'b', 'c': 'd'}
    assert parse_systemctl_show(['a=b', 'c=d\ne=f']) == {'a': 'b', 'c': 'd\ne=f'}

# Generated at 2022-06-13 06:21:30.814520
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:32.853782
# Unit test for function main
def test_main():
    main()


# import module snippets
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:37.526520
# Unit test for function main
def test_main():
    # FIXME: There is no way to test the existence of a service that is masked due to a race condition with systemd reexecing
    # and starting the service before the code is able to run.  For now, the best we can do is make sure that the main task
    # runs successfully and the the service is masked after it completes.
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:39.998428
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request to stop job') is True
    assert request_was_ignored('ignoring command stop') is True
    assert request_was_ignored('1') is False
    assert request_was_ignored('=') is False
    assert request_was_ignored(None) is False



# Generated at 2022-06-13 06:21:50.698182
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:22:04.132514
# Unit test for function main
def test_main():
    ''' Ansible systemd module unit test for function main '''

    # Unit test for function main with daemond_reload
    from ansible.modules.system.systemd import main


# Generated at 2022-06-13 06:22:05.479419
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:13.891233
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    lines = '''
[Unit]
Description=Example Description
[Service]
execStart=/test
'''.split('\n')
    assert parse_systemctl_show(lines) == {
        'Description': 'Example Description',
        'ExecStart': '/test'
    }

    lines = '''
[Unit]
Description=Example Description with { curly braces { inside
[Service]
execStart={
    test
}
'''.split('\n')
    assert parse_systemctl_show(lines) == {
        'Description': 'Example Description with { curly braces { inside',
        'ExecStart': '{\n    test\n}'
    }

    lines = '''
[Unit]
Description=Example Description with { curly braces { inside
[Service]
execStart={
    test
'''.split('\n')
    assert parse

# Generated at 2022-06-13 06:22:14.626854
# Unit test for function main
def test_main():
    with patched_modules('systemd'):
        assert main() == 0

# Generated at 2022-06-13 06:22:46.603005
# Unit test for function main
def test_main():
    import platform
    import sys

# Generated at 2022-06-13 06:22:57.555492
# Unit test for function main

# Generated at 2022-06-13 06:23:08.219999
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:23:12.963708
# Unit test for function main
def test_main():
    testunit = 'docker'
    teststatus = {'LoadState': 'unused'}
    sysvinit_path = "/etc/init.d/docker"
    systemd_path = "/usr/lib/systemd/system/docker.service"
    (rc, out, err) = module.run_command("systemctl show docker.service")
    systemctl_dict = parse_systemctl_show(to_native(out).split('\n'))
    try:
        main()
    except SystemExit:
        # This is a normal case
        pass
    except Exception as e:
        # AssertionError means that test failed
        assert type(e) is AssertionError
    # check status
    assert unit == testunit
    assert rc == 0
    assert is_systemd == True
    assert is_initd == True

# Generated at 2022-06-13 06:23:16.990802
# Unit test for function main
def test_main():
    print("Starting Unit test for function main")
    print("Finished Unit test for function main")

if __name__ == '__main__':
    main()
    module.run_command_environ_update = dict(LANG='C', LC_ALL='C', LC_MESSAGES='C', LC_CTYPE='C')
    test_main()

# Generated at 2022-06-13 06:23:23.111794
# Unit test for function main
def test_main():
    module = AnsibleModule({
        'name': {
            'name': 'systemd-journald.service',
            'state': 'started',
            'enabled': False,
        }
    })

    unit = module.params['name']
    systemctl = module.get_bin_path('systemctl', True)

    if os.getenv('XDG_RUNTIME_DIR') is None:
        os.environ['XDG_RUNTIME_DIR'] = '/run/user/%s' % os.geteuid()

    systemctl += " --%s" % module.params['scope']

    systemctl += " --no-block"

    systemctl += " --force"

    rc = 0
    out = err = ''

# Generated at 2022-06-13 06:23:32.534145
# Unit test for function main

# Generated at 2022-06-13 06:23:41.520520
# Unit test for function main
def test_main():
    spec = dict(
        name=dict(type='str', aliases=['service', 'unit']),
        state=dict(type='str', choices=['reloaded', 'restarted', 'started', 'stopped']),
        enabled=dict(type='bool'),
        force=dict(type='bool'),
        masked=dict(type='bool'),
        daemon_reload=dict(type='bool', default=False, aliases=['daemon-reload']),
        daemon_reexec=dict(type='bool', default=False, aliases=['daemon-reexec']),
        scope=dict(type='str', default='system', choices=['system', 'user', 'global']),
        no_block=dict(type='bool', default=False),
    )
    module = AnsibleModule(spec)
    main()



# Generated at 2022-06-13 06:23:52.262021
# Unit test for function main
def test_main():
    unit = 'foo'

# Generated at 2022-06-13 06:23:58.516971
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:44.382773
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:56.256057
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import os
    import sys

    if os.getenv('XDG_RUNTIME_DIR') is None:
        os.environ['XDG_RUNTIME_DIR'] = '/run/user/%s' % os.geteuid()

    testmodule = '''
---
- hosts: localhost
  tasks:
    - name: Test service_facts
      service_facts:
        name: 'chronyd'
'''

    testmodule = os.path.join(os.path.dirname(__file__), 'testmodule.yml')
    with open(testmodule, 'w') as fp:
        fp.write(testmodule)

    ret, out, err = module_utils._ansible_module_runner(testmodule)

   

# Generated at 2022-06-13 06:25:07.479877
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:25:14.601416
# Unit test for function main
def test_main():
    # Test for request_was_ignored to return True
    data = '''Created symlink from /etc/systemd/system/multi-user.target.wants/jenkins.service to /etc/systemd/system/jenkins.service.
Created symlink from /etc/systemd/system/multi-user.target.wants/httpd.service to /usr/lib/systemd/system/httpd.service.
Failed to issue method call: Unit jenkins.service not loaded.
Failed to issue method call: Unit httpd.service not loaded.'''
    assert request_was_ignored(data)

    # Test for sysv_exists to return True
    assert sysv_exists('httpd')

    # Test for is_chroot to return False
    assert not is_chroot(None)

    #

# Generated at 2022-06-13 06:25:21.036851
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test that a description can contain { or }
    lines = [
        'Id=foo.service',
        'Description=Description that contains {',
        ' and } and a continuation line',  # Should be ignored
    ]
    assert parse_systemctl_show(lines) == {
        'Id': 'foo.service',
        'Description': 'Description that contains { and }',
    }
    # Test that a value on a single line is accepted
    lines = [
        'Id=foo.service',
        'ExecStart={ path=/bin/foo ; argv[]=/bin/foo -bar ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }',
    ]

# Generated at 2022-06-13 06:25:31.277886
# Unit test for function main
def test_main():
    """ Ansible return values are described here: http://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html
    This module supports check mode.
    """

# Generated at 2022-06-13 06:25:39.929718
# Unit test for function main
def test_main():
    sys.modules['ansible.modules.system.systemd'] = sys.modules[__name__]
    sys.modules['ansible.module_utils.system.systemd'] = sys.modules['ansible.module_utils.systemd']
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from units.modules.system.systemd import main as systemd_main
    from units.compat.mock import MagicMock, patch

    # Initial setup
    old_unit = None
    new_unit = None
    enabled = None
    masked = None
    state = None

    def run_command(command):
        global old_unit, new_unit, enabled, masked, state

# Generated at 2022-06-13 06:25:46.728544
# Unit test for function main

# Generated at 2022-06-13 06:25:55.202507
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:26:02.630203
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:27:40.930444
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    lines = [
        'Description=MyService',
        'ExecStart={path=/path/to/exe arg1 arg2}',
        'ExecStart={path=/path/to/exe2 arg1 arg2}',
        'ExecStart={path=/path/to/exe3 arg1 arg2}',
        'FooBar=Bar',
        'ExecStart={path=/path/to/exe4 arg1}',
    ]
    assert parse_systemctl_show(lines) == {
        'Description': 'MyService',
        'ExecStart': 'path=/path/to/exe3 arg1 arg2',
        'FooBar': 'Bar',
    }
    lines = [
        'Description={This is my service}',
        'ExecStart={path=/path/to/exe arg1 arg2}',
    ]
    assert parse

# Generated at 2022-06-13 06:27:47.403620
# Unit test for function main
def test_main():
    result = dict(
        name='test_name',
        changed=False,
        status=dict(
            LoadState='loaded',
            ActiveState='active',
            SubState='running'
        ),
        enabled=False,
        state='stopped'
    )
    module_args = dict(
        name='test_name',
        state='stopped',
        enabled=False,
        masked=False,
        daemon_reload=False,
        daemon_reexec=False,
        scope='system',
        no_block=False,
        force=False,
    )
    check_args = dict(
        check_mode=True,
    )
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        mock_module = MagicMock()

# Generated at 2022-06-13 06:27:52.543828
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Simple, non-multiline case
    assert {'Name': 'foo'} == parse_systemctl_show('Name=foo'.split('\n'))
    # Multiline case
    assert {'ExecStart': 'myv=1\nmyv=2'} == parse_systemctl_show('ExecStart={ myv=1\nmyv=2\n}'.split('\n'))
    # Multiline with no newline
    assert {'ExecStart': 'myv=1\nmyv=2'} == parse_systemctl_show('ExecStart={ myv=1\nmyv=2 }'.split('\n'))
    # Test parsing of a line that ends with =

# Generated at 2022-06-13 06:27:58.039711
# Unit test for function main

# Generated at 2022-06-13 06:28:10.848386
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.helpers import get_exception
    import sys

    # If a default argument is added or removed, this will have to be changed.

# Generated at 2022-06-13 06:28:22.422928
# Unit test for function main

# Generated at 2022-06-13 06:28:32.843353
# Unit test for function main
def test_main():
    class Mock(object):
        def __init__(self, *args, **kwargs):
            pass

        def run_command(self, *args, **kwargs):
            return (0, "test_main", "")

        def get_bin_path(self, *args, **kwargs):
            return "test_main"

    preset_args = {
        'name': "test_main",
        'enabled': False,
        'masked': False,
        'force': False,
        'no_block': False,
        'daemon_reload': False,
        'daemon_reexec': False,
        'scope': "system"
    }

    def call_main(args):
        module = Mock()
        module.params = args

        main(module)


# Generated at 2022-06-13 06:28:42.212194
# Unit test for function main
def test_main():
    mock = MagicMock()
    module = mock
    module.run_command.side_effect = [(0, '', ''), (0, '', ''), (0, '', ''), (0, '', ''), (0, '', '')]
    module.get_bin_path.side_effect = ['/usr/bin/systemctl']
    module.fail_json.side_effect = [""]
    unit = 'httpd'

    main()



# Generated at 2022-06-13 06:28:52.339602
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test with a simple value on one line
    lines = ['Description=Foo']
    parsed = parse_systemctl_show(lines)
    assert parsed == {'Description': 'Foo'}
    # Test with a single-line value starting with {
    lines = ['Description={Foo}']
    parsed = parse_systemctl_show(lines)
    assert parsed == {'Description': '{Foo}'}
    # Test with a multi-line value
    lines = ['ExecStart={\n    foo\n    bar\n}']
    parsed = parse_systemctl_show(lines)
    assert parsed == {'ExecStart': '{\n    foo\n    bar\n}'}
    # Test with a simple value on one line, and a multi-line value starting on the next line

# Generated at 2022-06-13 06:29:00.941695
# Unit test for function main
def test_main():
    unit = 'sshd'
    systemctl = '/usr/bin/systemctl'
    scope = 'system'
    no_block = False
    force = False
    masked = None
    daemon_reload = False
    daemon_reexec = False

    result = dict(
        name=unit,
        changed=False,
        status=dict(),
    )
    unit = 'sshd'

    is_initd = sysv_exists(unit)
    is_systemd = False

    # check service data, cannot error out on rc as it changes across versions, assume not found
    (rc, out, err) = module.run_command("%s show '%s'" % (systemctl, unit))

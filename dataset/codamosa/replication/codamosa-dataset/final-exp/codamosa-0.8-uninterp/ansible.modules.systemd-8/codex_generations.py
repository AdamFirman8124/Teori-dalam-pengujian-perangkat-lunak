

# Generated at 2022-06-13 06:20:57.523562
# Unit test for function main
def test_main():

    class AnsibleModule:
        pass

    module = AnsibleModule()
    module.params = {
      'name': 'unit',
      'state': 'started',
      'enabled': True,
      'masked': False,
      'scope': 'system',
    }
    main(module)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:04.616432
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:07.280400
# Unit test for function main
def test_main():
    assert main() is None

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 06:21:18.697742
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:28.458035
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Single-line values
    output1 = ['Description=Command Scheduler', 'LoadState=loaded']
    assert parse_systemctl_show(output1) == {'Description': 'Command Scheduler', 'LoadState': 'loaded'}

    # Multi-line values
    output2 = ['Description={', '  Command Scheduler', '}', 'LoadState=loaded']
    assert parse_systemctl_show(output2) == {'Description': 'Command Scheduler', 'LoadState': 'loaded'}

    # Single-line value that starts with {
    output3 = ['Description={Command Scheduler}', 'LoadState=loaded']
    assert parse_systemctl_show(output3) == {'Description': 'Command Scheduler', 'LoadState': 'loaded'}

    # Value that starts with { but doesn't end with }

# Generated at 2022-06-13 06:21:34.995632
# Unit test for function main
def test_main():
    module = AnsibleModule({'name': 'sshd.service'})
    assert main() == {
        'changed': False,
        'failed': False,
        'rc': 0,
        'stdout': '',
        'stdout_lines': [],
        'stderr': '',
        'stderr_lines': []
    }

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:36.979004
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request') == True
    assert request_was_ignored('ignoring command') == True
    assert request_was_ignored('=') == False
    assert request_was_ignored('foo') == False



# Generated at 2022-06-13 06:21:45.714699
# Unit test for function main
def test_main():
    # Generate test data
    data = dict()
    data["params"] = {
                         "scope": "system",
                         "enabled": False,
                         "masked": False,
                         "state": u"stopped",
                         "no_block": False,
                         "force": False,
                         "daemon_reexec": False,
                         "name": u"sshd.service",
                         "daemon_reload": False
                     }
    rc = 0
    out = ""
    err = ""
    tmp_systemctl = "/usr/bin/systemctl"

# Generated at 2022-06-13 06:21:54.862143
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:22:07.065538
# Unit test for function main

# Generated at 2022-06-13 06:22:34.070147
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    #test simple line
    assert parse_systemctl_show(["foo=3", "bar=4"]) == {"foo": "3", "bar": "4"}
    #test multiline line
    assert parse_systemctl_show(["foo=3", "bar={", "blah"]) == {"foo": "3", "bar": "{\nblah"}
    #test multiline line that doesn't end with '}'
    assert parse_systemctl_show(["foo=3", "bar={", "blah"]) == {"foo": "3", "bar": "{\nblah"}
    #test a line that starts with 'Exec' and is followed by a single-line line

# Generated at 2022-06-13 06:22:45.819043
# Unit test for function main

# Generated at 2022-06-13 06:22:55.644866
# Unit test for function main
def test_main():
    systemctl = module.get_bin_path('systemctl', True)
    test_args = {
        'name': 'test',
        'state': 'started',
        'enabled': True,
        'masked': False,
        'daemon_reload': False,
        'daemon_reexec': False,
        'scope': 'system',
        'no_block': False,
    }

    m_os = MagicMock(os)
    m_os.path.isfile.return_value = True
    m_os.getenv.return_value = '1'
    m_os.path.exists.return_value = True
    m_os.geteuid.return_value = '1'

    m_module = MagicMock(AnsibleModule)
    m_module.params = test

# Generated at 2022-06-13 06:23:07.168632
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:23:11.273170
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_native
    from ansible_collections.notmintest.not_a_real_collection.plugins.modules.systemd import main

    module = AnsibleModule(argument_spec={})
    main(module)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:19.107678
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    result = parse_systemctl_show(['ExecStart={', '  test multi-line value', '  }'])
    assert result['ExecStart'] == 'test multi-line value'
    result = parse_systemctl_show(['ExecStart={ test multi-line value', '  }'])
    assert result['ExecStart'] == 'test multi-line value'
    result = parse_systemctl_show(['ExecStart={', '  test multi-line value }'])
    assert result['ExecStart'] == 'test multi-line value'
    result = parse_systemctl_show(['ExecStart={ test multi-line value }'])
    assert result['ExecStart'] == 'test multi-line value'
    result = parse_systemctl_show(['ExecStart=test single-line value'])

# Generated at 2022-06-13 06:23:24.031054
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    data = {
        'argv[]': '/usr/sbin/sshd -D',
        'control_group': '/system.slice/sshd.service',
        'conditions': 'ConditionPathIsReadWrite=/var/empty/sshd||ConditionPathIsSymbolicLink=/var/empty/sshd|||',
    }
    lines = ["{}={}".format(k, v) for k, v in data.items()]
    assert parse_systemctl_show(lines) == data

    lines = [
        'argv[]=/usr/sbin/sshd -D',
        'control_group=/system.slice/sshd.service',
        'conditions={ ConditionPathIsReadWrite=/var/empty/sshd||ConditionPathIsSymbolicLink=/var/empty/sshd||| }',
    ]
   

# Generated at 2022-06-13 06:23:26.273076
# Unit test for function main
def test_main():
    main()
# Import test.py
if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 06:23:34.241123
# Unit test for function main
def test_main():
    class MockModule(object):

        def __init__(self):
            self.state = 'started'
            self.params = {}
            self.rc = 0
            self.out = ''
            self.err = ''
            self.runs = []

        def get_bin_path(self, executable):
            return executable

        def run_command(self, command):
            self.runs.append(command)
            return self.rc, self.out, self.err

        def exit_json(self, **kwargs):
            mock_result.update(kwargs)
            self.exit = True

        def fail_json(self, **kwargs):
            self.err = kwargs['msg']
            self.exit_json(**kwargs)


# Generated at 2022-06-13 06:23:42.708991
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:06.101743
# Unit test for function main
def test_main():
    module = AnsibleModule({
      'name': 'test_unit',
      'state': 'reloaded',
    })
    assert main() is None

# Unit test

# Generated at 2022-06-13 06:24:16.743174
# Unit test for function main
def test_main():
    def _mock_run_command(args, check_rc=False):
        if args == 'systemctl --system daemon-reload':
            return (0, '', '')
        elif args == 'systemctl --system daemon-reexec':
            return (0, '', '')
        elif args == 'systemctl --system list-unit-files':
            return (0, 'cronie.service\n', '')
        elif args == 'systemctl --system is-enabled cronie.service':
            return (0, 'enabled', '')
        else:
            raise Exception("unexpected command called: {0!s}".format(args))


# Generated at 2022-06-13 06:24:18.127483
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:19.436540
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:24.564771
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({
        'force': True,
        'name': 'test-unit',
        'state': 'started',
        '_ansible_check_mode': False,
    })

    setattr(module, 'run_command', fake_run_command)
    setattr(module, 'get_bin_path', lambda _: "/usr/bin/systemctl")

    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:36.460480
# Unit test for function main

# Generated at 2022-06-13 06:24:47.467888
# Unit test for function main

# Generated at 2022-06-13 06:24:58.690598
# Unit test for function main
def test_main():
    unit = 'test_service'
    # module = AnsibleModule(
    #
    #     argument_spec=dict(
    #         name=dict(type='str', aliases=['service', 'unit']),
    #         state=dict(type='str', choices=['reloaded', 'restarted', 'started', 'stopped']),
    #         enabled=dict(type='bool'),
    #         force=dict(type='bool'),
    #         masked=dict(type='bool'),
    #         daemon_reload=dict(type='bool', default=False, aliases=['daemon-reload']),
    #         daemon_reexec=dict(type='bool', default=False, aliases=['daemon-reexec']),
    #         scope=dict(type='str', default='system', choices=['system', '

# Generated at 2022-06-13 06:25:09.629401
# Unit test for function main
def test_main():
    from ansible import context
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.systemd._common import request_was_ignored, to_native

    module_args = dict(
        name='sshd',
        enabled=True,
        daemon_reload=True,
        daemon_reexec=True,
        state='started',
    )
    result = dict(
        changed=False,
        msg=dict(
            rc=0,
        ),
    )

# Generated at 2022-06-13 06:25:21.288605
# Unit test for function main
def test_main():

    mock_module = MagicMock()
    mock_module.params = {'daemon_reload': False, 'name': 'sshd', 'enabled': True, 'masked': False, 'force': True, 'state': None}
    mock_module.run_command.return_value = (0, 'some_out', 'some_err')
    mock_module.get_bin_path = Mock(return_value='/usr/bin/systemctl')

    expected = {'changed': True, 'name': 'sshd'}

    is_running_service = Mock(return_value=True)
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY2
    if not PY2:
        builtins = 'builtins'

# Generated at 2022-06-13 06:26:13.464322
# Unit test for function main
def test_main():
    # The assertion below fails when executed in a chroot. This is normal.
    assert is_chroot(module) == False


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:26:19.269650
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 06:26:27.758722
# Unit test for function main

# Generated at 2022-06-13 06:26:33.960627
# Unit test for function main

# Generated at 2022-06-13 06:26:46.276386
# Unit test for function main
def test_main():
    from ansible.modules.system.systemd import ServiceManager
    from ansible.module_utils.systemd import UnitManager
    from ansible.module_utils.basic import ConfigParser
    from ansible.module_utils.systemd.common import Unit, Systemctl

# Generated at 2022-06-13 06:26:56.449570
# Unit test for function main

# Generated at 2022-06-13 06:27:05.276617
# Unit test for function main

# Generated at 2022-06-13 06:27:16.120225
# Unit test for function main

# Generated at 2022-06-13 06:27:23.237857
# Unit test for function main
def test_main():
    '''
    ansible systemd module test
    '''
    sys.path.append("../ansible")

# Generated at 2022-06-13 06:27:34.436717
# Unit test for function main

# Generated at 2022-06-13 06:28:58.231352
# Unit test for function main

# Generated at 2022-06-13 06:29:01.008424
# Unit test for function main
def test_main():
    sys.argv = [sys.argv[0], 'name=foo', 'state=started']
    sys.argv = [sys.argv[0], 'name=foo', 'state=stopped']

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:29:05.411478
# Unit test for function main
def test_main():
    args = dict(
        enabled=True,
        name='firewalld'
    )
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    module.params.update(args)
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:29:15.246870
# Unit test for function main

# Generated at 2022-06-13 06:29:22.984555
# Unit test for function main
def test_main():
    ''' Unit test for function main '''


# Generated at 2022-06-13 06:29:32.285721
# Unit test for function main
def test_main():
    from ansible.module_utils.systemd import (
        is_chroot,
        is_deactivating_service,
        is_running_service,
        parse_systemctl_show,
        request_was_ignored,
        sysv_exists,
        sysv_is_enabled,
    )

    with mock.patch('ansible.module_utils.basic.AnsibleModule') as mock_amodule:
        m = mock_amodule.return_value
        m.params = dict(name='foo')
        m.check_mode = True
        m.run_command = mock.Mock(return_value=(0, '', ''))
        main()

        # run_command should only be called once
        assert m.run_command.call_count == 1
        # should be called with "system

# Generated at 2022-06-13 06:29:38.836136
# Unit test for function main
def test_main():
    argv = [
        'name=test',
        'state=stopped',
        'enabled=false',
        'masked=false',
        'force=false',
        'daemon_reload=false',
        'daemon_reexec=false',
        'scope=system',
        'no_block=false',
    ]

# Generated at 2022-06-13 06:29:48.368616
# Unit test for function main
def test_main():
    import copy
    import platform
    import subprocess
    import sys
    import tempfile
    import textwrap
    import types
    import os

    import pytest
    import yaml
    import yaml.resolver


    # Ansible's CI environment does not have the systemd libraries
    # installed. Do not test in that environment.
    if os.environ.get('TRAVIS') == 'true':
      return

    # Skip testing in environments with systemd < 200

# Generated at 2022-06-13 06:29:55.060493
# Unit test for function main
def test_main():
    # pylint: disable=protected-access

    class MockModule(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

        def run_command(self, command, check_rc=False):
            self.command = command
            if 'is-active' in command:
                return (0, 'active', '')
            elif 'show' in command:
                if 'LoadError' in command:
                    return (0, 'LoadError=an error', '')
                elif 'LoadState=masked' in command:
                    return (0, 'LoadState=masked', '')
                elif 'foobar' in command:
                    return (1, '', '')

# Generated at 2022-06-13 06:30:03.072398
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import *

    # no state and no name
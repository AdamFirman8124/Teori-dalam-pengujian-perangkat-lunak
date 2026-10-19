

# Generated at 2022-06-13 06:21:15.008265
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import sys
    import os


# Generated at 2022-06-13 06:21:25.020148
# Unit test for function main
def test_main():
    # mock the module object
    m_module = MagicMock()
    #m_module.return_value = True
    # mock the systemctl path
    m_module.get_bin_path.return_value = '/bin/systemctl'
    m_module.run_command.return_value = True
    m_module.params = {'enabled': True, 'name': 'sshd'}
    # mock the os environment variable
    os.environ['XDG_RUNTIME_DIR'] = '/run/user/%s' % os.geteuid()

    main()
    assert is_systemd() == True

#/usr/bin/python
import sys
import os
import re
import getpass
import pwd
import subprocess
import platform
import select
import time

active_status_matcher = re

# Generated at 2022-06-13 06:21:32.086697
# Unit test for function main

# Generated at 2022-06-13 06:21:37.667160
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:46.137670
# Unit test for function main
def test_main():
    # Just making sure we're not calling exiting functions
    import ansible_module_systemd as ams
    ams.main()
    ams.is_chroot()
    ams.is_running_service({})
    ams.request_was_ignored()
    ams.parse_systemctl_show([])
    ams.sysv_exists()
    ams.sysv_is_enabled()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:54.223898
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    test_lines = '''
    Id=foo.service
    Names=foo.service
    FragmentPath=/usr/lib/systemd/system/foo.service
    ActiveState=active
    ActiveEnterTimestamp=Sun 2016-05-15 18:28:49 EDT
    '''.strip().splitlines()
    assert parse_systemctl_show(test_lines) == {
        'Id': 'foo.service',
        'Names': 'foo.service',
        'FragmentPath': '/usr/lib/systemd/system/foo.service',
        'ActiveState': 'active',
        'ActiveEnterTimestamp': 'Sun 2016-05-15 18:28:49 EDT'
    }



# Generated at 2022-06-13 06:21:56.932542
# Unit test for function main
def test_main():
    main()


# import module snippets
from ansible.module_utils.basic import *


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:09.193236
# Unit test for function main
def test_main():
    import tempfile
    import shutil
    import sys
    import os

# Generated at 2022-06-13 06:22:16.602833
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    import sys
    import textwrap
    from unittest import TestCase

    class ParseSystemctlShowTests(TestCase):
        def test_parse_systemctl_show(self):
            # Test a multi-line value with no surrounding brackets
            test_lines = textwrap.dedent('''\
                Description=foo\n
                bar\n
                baz\n
                ExecStart=/bin/echo hello
                ExecStop=/bin/echo bye
                ''').split('\n')
            expected = {
                'Description': 'foo bar baz',
                'ExecStart': '/bin/echo hello',
                'ExecStop': '/bin/echo bye',
            }
            self.assertEqual(expected, parse_systemctl_show(test_lines))

            # Test a multi-line value with surrounding brackets
            test_

# Generated at 2022-06-13 06:22:28.734111
# Unit test for function main
def test_main():
    class UnitTest(unittest.TestCase):

        def setUp(self):
            self.mockPs = mock.MagicMock()
            self.mockPopen = mock.MagicMock()
            self.mockPopen = mock.MagicMock()

        def tearDown(self):
            self.mockPs = None
            self.mockPopen = None
            self.mockPopen = None

        def test_service_status_short(self):
            class MockProcess(object):
                def __init__(self):
                    self.returncode = 0
                    self.stdout = "ActiveState=unknown\n"
                    self.stderr = ""

                def communicate(self):
                    return self.stdout, self.stderr

            self.mockPopen.return_value = MockProcess()

# Generated at 2022-06-13 06:22:53.022343
# Unit test for function main
def test_main():
    srv = 'test.service'
    assert main({"state": "started", "name": srv, "enabled": None, "masked": False, "daemon_reload": None}) == {'changed': True, 'name': srv, 'state': "started"}
    assert main({"state": "stopped", "name": srv, "enabled": None, "masked": True, "daemon_reload": None}) == {'changed': True, 'name': srv, 'state': "stopped"}
    assert main({"state": "stopped", "name": srv, "enabled": None, "masked": False, "daemon_reload": None}) == {'changed': True, 'name': srv, 'state': "stopped"}

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:04.226872
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:23:12.570281
# Unit test for function main

# Generated at 2022-06-13 06:23:20.124313
# Unit test for function main

# Generated at 2022-06-13 06:23:29.640205
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    output = '''
Description=My unit
After=some.service
OnFailure=cleanup.service
OnFailureJobMode=replace-irreversibly
Environment=foo=bar
Environment=bar=baz
ExecStart={ some_command arg1 arg2 arg3 }
ExecStartPost={ some_command arg1 arg2 arg3 }
ExecReload={ some_command arg1 arg2 arg3 }
ExecStop={ some_command arg1 arg2 arg3 }
ExecStopPost={ some_command arg1 arg2 arg3 }
    '''.split('\n')

# Generated at 2022-06-13 06:23:40.124878
# Unit test for function main
def test_main():
    request = {
        'name': 'test-prod',
        'state': 'stopped',
        'daemon_reload': False,
        'masked': False,
        'enabled': None,
        'scope': 'system',
        'no_block': False,
    }


# Generated at 2022-06-13 06:23:44.204170
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request')
    assert request_was_ignored('ignoring command')
    assert not request_was_ignored('=')



# Generated at 2022-06-13 06:23:54.249903
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:00.401977
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:05.615635
# Unit test for function main
def test_main():
    unit = "foo@bar"
    # TODO: Create a test for main and uncomment the assert
    #assert True == False

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:35.474853
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:43.763552
# Unit test for function main
def test_main():
    unit = "sshd.service"
    systemctl = module.get_bin_path('systemctl', True)
    rc = 0
    out = err = ''
    result = dict(
        name=unit,
        changed=False,
        status=dict(),
    )

    # Run daemon-reload first, if requested
    if module.params['daemon_reload'] and not module.check_mode:
        (rc, out, err) = module.run_command("%s daemon-reload" % (systemctl))
        if rc != 0:
            module.fail_json(msg='failure %d during daemon-reload: %s' % (rc, err))

    # Run daemon-reexec

# Generated at 2022-06-13 06:24:55.900763
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:25:07.027919
# Unit test for function main
def test_main():
    from unittest import mock
    from io import StringIO
    import sys
    import json

    x = sys.modules[__name__]

    with mock.patch.multiple(x,
        run_command=lambda x: (0, '', ''),
    ) as mocked_modules:
        with mock.patch.object(x, 'is_running_service') as mocked_running_service:
            mocked_running_service.return_value = False
            with mock.patch.object(x, 'is_chroot') as mocked_chroot:
                mocked_chroot.return_value = False
                with mock.patch.object(x, 'sysv_exists') as mocked_sysv_exists:
                    mocked_sysv_exists.return_value = True

# Generated at 2022-06-13 06:25:14.382410
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:25:19.029440
# Unit test for function main

# Generated at 2022-06-13 06:25:23.505323
# Unit test for function main
def test_main():
    test_unit = str(time.time())
    unit = "test_unit_%s.service" % test_unit


# Generated at 2022-06-13 06:25:33.683137
# Unit test for function main
def test_main():
    # Load the unit test spec
    unit_test_spec = importlib.util.spec_from_file_location('unit_test_spec', os.path.join(os.path.dirname(__file__), 'unit_test_spec.py'))
    unit_test_spec.loader.exec_module(unit_test_spec)
    unit_test_main = unit_test_spec.unit_test_main
    if 'ansible_module_stub' in sys.modules:
        del sys.modules['ansible_module_stub']
    if 'ansible_module_stub' in globals():
        del globals()['ansible_module_stub']
    unit_test_main(sys.argv[1:], globals())



# Generated at 2022-06-13 06:25:38.151375
# Unit test for function main
def test_main():
    """ Unit tests for main"""
    result = {}

    # Check service exists
    # serv1 is a non-existant service
    # serv2 is a non-existant service
    # serv3 is a service that exists
    serv1 = 'serv1'
    serv2 = 'serv2'
    serv3 = 'serv3'
    serv4 = 'serv4'

    # Check pre-existing/non-existing service
    result = check_service_exists(serv1)
    assert result is False
    result = check_service_exists(serv2)
    assert result is False
    result = check_service_exists(serv3)
    assert result is True
    result = check_service_exists(serv4)
    assert result is True


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:42.595245
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(default=None, type='str'),
            state=dict(default=None, choices=['reloaded', 'restarted', 'started', 'stopped']),
            enabled=dict(default=None, type='bool'),
            masked=dict(default=None, type='bool'),
            daemon_reload=dict(default=False, type='bool'),
            force=dict(default=False, type='bool'),
        )
    )
    rc, out, err = module.run_command.func_defaults[0]('systemctl daemon-reload')
    assert rc == 0
    rc, out, err = module.run_command.func_defaults[0]('systemctl daemon-reexec')
    assert rc == 0
    rc, out,

# Generated at 2022-06-13 06:26:42.709206
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:26:53.828536
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    sample_input = '''
        Unit=foo.service
        UnitFileState=enabled
        Description=description
        SingleLine=single line
        MultiLine={
            multi-line
            value
        }
        Exec={
            exec
            start
        }
        ExecStart=
        Exec=
        {
            exec
        }
        ExecStart={
            exec
            start
        }
        ExecStart=
        ExecStart=
        {
            exec
            start
        }
        ExecStart=
        {
            exec
        }
        ExecStart=
        {
            exec
            start
            }
        ExecStart=
        {
            exec
            start
        }
        Other=other
    '''.split()

# Generated at 2022-06-13 06:27:05.452079
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test parsing of multi-line values
    input = [
        'Id=dhcpcd@wlan0.service',
        'FragmentPath=/usr/lib/systemd/system/dhcpcd@.service',
        'SourcePath=/usr/lib/systemd/system/dhcpcd@.service',
        'UnitFileState=enabled',
        'ExecStart={ path=/usr/libexec/dhcpcd-wrapper ; argv[]=/usr/libexec/dhcpcd-wrapper -w',
        ' }',
        'ExecStartPost={ path=/usr/bin/systemctl ; argv[]=/usr/bin/systemctl kill dhcpcd@%I.service'
    ]
    parsed = parse_systemctl_show(input)

# Generated at 2022-06-13 06:27:15.495513
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import b
    import sys

    # Unit test for function main

# Generated at 2022-06-13 06:27:19.732929
# Unit test for function main
def test_main():
    args = dict(
        name='httpd',
        enabled=True
    )
    rc, out, err = main(args)
    print('rc = %d' % rc)
    print('out = %s' % out)
    print('err = %s' % err)
    assert rc == 0, 'Exit code does not match requirement'
    assert len(out) > 0, 'Output should not be empty'

if __name__ == '__main__':
    main()
    # test_main()
#

# Generated at 2022-06-13 06:27:26.822037
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:27:35.982111
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:27:51.618527
# Unit test for function main

# Generated at 2022-06-13 06:28:00.566416
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    expected = {'ExecStart': '{\n              path=/usr/sbin/crond\n              argv[]=/usr/sbin/crond -n $CRONDARGS\n              ignore_errors=no\n              start_time=[n/a]\n              stop_time=[n/a]\n              pid=0\n              code=(null)\n              status=0/0\n          }',
                'ExecReload': '{\n              path=/bin/kill\n              argv[]=/bin/kill -HUP $MAINPID\n              ignore_errors=no\n              start_time=[n/a]\n              stop_time=[n/a]\n              pid=0\n              code=(null)\n              status=0/0\n          }',
                'Description': 'Command Scheduler'}
   

# Generated at 2022-06-13 06:28:03.472356
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleFailJson):
        main()


# Generated at 2022-06-13 06:28:47.042375
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    systemctl = 'systemctl'
    if (sys.version_info > (3, 0)):
        to_native = lambda x: to_bytes(x, encoding='utf-8')
    else:
        to_native = lambda x: to_bytes(x)
    # Load the mock env
    test_env = {
        "XDG_RUNTIME_DIR": "/run/user/%s" % os.geteuid(),
        "PATH": '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    }

# Generated at 2022-06-13 06:28:54.795448
# Unit test for function main
def test_main():
    """
        Test module main
    """

# Generated at 2022-06-13 06:29:02.389248
# Unit test for function main
def test_main():
    from ansible.modules.system.systemd import main as systemd_main

    sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
    from units.compat import unittest

    class TestSystemdModule(unittest.TestCase):
        def setUp(self):
            self.mock_module = MagicMock()
            self.mock_run_command = MagicMock()
            self.mock_get_bin_path = MagicMock()
            self.mock_fail_json = MagicMock()
            self.mock_warn = MagicMock()

            self.old_sysv_exists = systemd.sysv_exists
            systemd.sysv_exists = MagicMock()


# Generated at 2022-06-13 06:29:08.406212
# Unit test for function main
def test_main():
    import pytest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch, Mock

    from ansible.module_utils import basic

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught by the test case"""
        pass

    class AnsibleFailJson(Exception):
        """Exception class to be raised by module.fail_json and caught by the test case"""
        pass

    def exit_json(*args, **kwargs):
        """function to patch over exit_json; package return data into an exception"""
        if 'changed' not in kwargs:
            kwargs['changed'] = False
       

# Generated at 2022-06-13 06:29:18.983522
# Unit test for function main

# Generated at 2022-06-13 06:29:30.298748
# Unit test for function main
def test_main():
    #set to False to run locally
    if True:
        from ansible.module_utils.basic import *
        from ansible.module_utils._text import to_bytes

        # read in arguments for ansible module

# Generated at 2022-06-13 06:29:33.667789
# Unit test for function main
def test_main():
    # no parameters
    args = dict()
    if __name__ == '__main__':
        main()

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.facts import *

# For local testing give path to ansible/modules
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:29:43.327112
# Unit test for function main
def test_main():
    def run_command(args, check_rc=False):
        return (0, '', '')
    def exit_json(**kwargs):
        return kwargs
    def fail_json(**kwargs):
        raise AnsibleFailJson(**kwargs)

    class MockActionModule(object):
        def __init__(self, *args, **kwargs):
            self.params = {
                'name': 'foo.service',
                'masked': None,
                'enabled': None,
                'state': None,
            }
        def get_bin_path(self, arg, required=False):
            return 'systemctl'
        def run_command(self, args, check_rc=False):
            return run_command(args, check_rc=check_rc)

# Generated at 2022-06-13 06:29:52.913417
# Unit test for function main
def test_main():
    import ansible.module_utils.basic_common
    import ansible.module_utils.basic
    import ansible.module_utils.basic

    import sys
    argv = [
        sys.argv[0],
        'name=/usr/lib/systemd/system/sshd.socket',
        'state=stopped'
    ]

# Generated at 2022-06-13 06:30:01.354280
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', aliases=['service', 'unit'], default='httpd'),
            state=dict(type='str', choices=['reloaded', 'restarted', 'started', 'stopped']),
            enabled=dict(type='bool'),
            force=dict(type='bool'),
            masked=dict(type='bool'),
            no_block=dict(type='bool', default=False),
        ),
        required_one_of=[['state', 'enabled', 'masked']],
        required_by=dict(
            state=('name', ),
            enabled=('name', ),
            masked=('name', ),
        ),
        supports_check_mode=True,
    )
    # Systemd service arguments
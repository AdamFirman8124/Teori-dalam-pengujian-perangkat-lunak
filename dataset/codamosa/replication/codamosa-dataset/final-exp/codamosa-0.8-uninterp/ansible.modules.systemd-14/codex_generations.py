

# Generated at 2022-06-13 06:20:55.977719
# Unit test for function main

# Generated at 2022-06-13 06:20:59.778642
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored(
        b'ignoring request ; unit has been masked\n'
    )
    assert request_was_ignored(
        b'ignoring request ; unit has been masked'
    )
    assert request_was_ignored(
        b'ignoring command'
    )



# Generated at 2022-06-13 06:21:06.337028
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:11.533078
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show(['Key=ValueOne', 'Key=ValueTwo']) == {'Key': 'ValueTwo'}
    assert parse_systemctl_show(['Key=ValueOne', 'Key=ValueTwo=']) == {'Key': 'ValueTwo='}
    assert parse_systemctl_show(['Key=']) == {'Key': ''}
    assert parse_systemctl_show(['Key']) == {}
    assert parse_systemctl_show([]) == {}
    assert parse_systemctl_show(['ExecStart=\n']) == {'ExecStart': '\n'}
    assert parse_systemctl_show(['ExecStart={\n']) == {'ExecStart': '{'}

# Generated at 2022-06-13 06:21:21.584666
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    show_output = """
    Description=nightly yum update
    ExecStart={ path=/bin/sh ; argv[]=/bin/sh -c 'yum -y update; systemctl restart $MAINPID' ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }
    FragmentPath=/usr/lib/systemd/system/dnf-automatic.timer
    """

# Generated at 2022-06-13 06:21:29.702576
# Unit test for function main

# Generated at 2022-06-13 06:21:41.445732
# Unit test for function main

# Generated at 2022-06-13 06:21:50.933749
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:54.323741
# Unit test for function main

# Generated at 2022-06-13 06:22:06.817020
# Unit test for function main
def test_main():
    args = dict(
        state='reloaded',
        enabled=False,
        masked=False,
        daemon_reload=False,
        daemon_reexec=False,
        force=False,
        no_block=False,
    )


# Generated at 2022-06-13 06:22:28.373231
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request')
    assert request_was_ignored('ignoring command')
    assert not request_was_ignored('=1')



# Generated at 2022-06-13 06:22:36.058125
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    # Test parameters
    test_params = dict(
        name="test.service",
        state=None,
        enabled=None,
        masked=None,
        no_block=None,
        force=None,
        daemon_reload=False,
        daemon_reexec=False,
        scope="system",
    )

    # Test AnsibleModule

# Generated at 2022-06-13 06:22:46.878340
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    class options_test_object(object):
        def __init__(self, params):
            self.changed = False
            self.first = params['first']
            self.second = params['second']

    options = options_test_object({'first': 'first', 'second': 'second'})
    basic._ANSIBLE_ARGS = options

    sys.argv[1:] = [
        '-vvvv',
        '-c', 'local',
        '-m', 'systemd',
        '-a',
        '"first=first second=second"'
    ]

    systemd.main()

if __name__ == '__main__':


    if len(sys.argv) > 1 and '--unittest' in sys.argv[1]:
        test

# Generated at 2022-06-13 06:22:55.807852
# Unit test for function main

# Generated at 2022-06-13 06:23:07.286195
# Unit test for function main

# Generated at 2022-06-13 06:23:11.339667
# Unit test for function request_was_ignored
def test_request_was_ignored():
    out = "Job for sshd.service failed because the control process exited with error code. See \"systemctl status sshd.service\"\n"
    assert request_was_ignored(out) is False
    out = "Job for sshd.service failed because the control process exited with error code.\n"
    assert request_was_ignored(out) is True


# unit test: is_running_service

# Generated at 2022-06-13 06:23:12.403238
# Unit test for function main
def test_main():
    main()


# import module snippets
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:19.999109
# Unit test for function main
def test_main():
    module = AnsibleModule({
        'state': 'stopped',
        'unit': 'abrt-ccpp.service',
        'enabled': True,
        'masked': True,
        'daemon_reload': True,
        'daemon_reexec': True,
        'scope': 'system',
        'no_block': False,
        'force': True,
    })
    module.exit_json = MagicMock()
    systemctl = module.get_bin_path('systemctl', True)

    rc = 0
    out = ''
    err = ''
    # Workaround for https://github.com/ansible/ansible/issues/71528
    rc = 0
    out = ''
    err = ''

    # list taken from man systemctl(1) for systemd 244
    valid_enabled_

# Generated at 2022-06-13 06:23:29.512506
# Unit test for function main
def test_main():
    print("Checking main")

# Generated at 2022-06-13 06:23:40.124091
# Unit test for function main

# Generated at 2022-06-13 06:23:56.332320
# Unit test for function main
def test_main():
    if __name__ == '__main__':
        import doctest
        doctest.testmod()


# Generated at 2022-06-13 06:24:02.144920
# Unit test for function main
def test_main():
    # This might not work all the time, dependent on the exact output
    # of systemctl.  For now, unit tests are disabled in the PR.
    
    # FIXME
    return


# Generated at 2022-06-13 06:24:11.329040
# Unit test for function main
def test_main():
    a = dict(
        name = 'foo',
        state = 'reloaded',
        enabled = True,
        force = True,
        masked = True,
        daemon_reload = True,
        daemon_reexec = True,
        scope = 'system',
        no_block = True,
    )
    print(a)
    main()

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    # Unit test
    test_main()
    # import code; code.interact(local=dict(globals(), **locals()))
    main()

# Generated at 2022-06-13 06:24:13.002983
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:22.361798
# Unit test for function main
def test_main():
    args = dict(
        name='S42fail2ban',
        state='started',
        enabled='yes',
        force='yes',
        masked='no',
        daemon_reload='yes',
        daemon_reexec='yes',
        scope='system',
        no_block='no',
        path='/usr/bin:/bin:/usr/sbin:/sbin',
        check_mode=False
    )


# Generated at 2022-06-13 06:24:34.250065
# Unit test for function main

# Generated at 2022-06-13 06:24:42.908263
# Unit test for function main
def test_main():
    # If we were called as main, then do some unit tests
    import os
    import tempfile
    import shutil
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import b
    from ansible.module_utils.six.moves import builtins

    # Set up my own fake AnsibleModule

# Generated at 2022-06-13 06:24:55.398291
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:25:03.018020
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:25:11.997154
# Unit test for function main

# Generated at 2022-06-13 06:25:44.843787
# Unit test for function main
def test_main():
    test_manager = ServiceManager()
    service_name = 'test_service'
    test_manager.add_service(service_name)
    result = ServiceController().start(service_name)
    assert result == 0
    result = ServiceController().stop(service_name)
    assert result == 0
    result = ServiceController().restart(service_name)
    assert result == 0
    result = ServiceController().disable(service_name)
    assert result == 0
    result = ServiceController().mask(service_name)
    assert result == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:54.824671
# Unit test for function main
def test_main():
    with tempfile.TemporaryDirectory() as tmp:
        create_unit_file(tmp, 'test_module_run.service', '''[Unit]
Description=Test module run

[Install]
WantedBy=multi-user.target
''')
        with open(tmp + '/service.status', 'w') as f:
            f.write('''
    Type=notify
    Restart=always
    RestartSec=5
    NotifyAccess=none
    NotifyState=running
''')
        with open(tmp + '/systemd-ask-password', 'w') as f:
            f.write('''#!/bin/sh
echo "test-answer"
''')
        os.chmod(tmp + '/systemd-ask-password', 0o755)

# Generated at 2022-06-13 06:26:02.374379
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    ansible.module_utils.basic.AnsibleModule = AnsibleModule
    # Convert relative import to absolute (see ansiballz)
    import unit.modules.systemd.systemd_module.main as main_func

    # Arrange
    args = dict(
        state='started',
        enabled=True,
        masked=False,
        daemon_reload=False,
        daemon_reexec=False,
        scope='system',
        no_block=False,
    )

# Generated at 2022-06-13 06:26:13.105653
# Unit test for function main

# Generated at 2022-06-13 06:26:19.092703
# Unit test for function main

# Generated at 2022-06-13 06:26:27.662188
# Unit test for function main
def test_main():
  import sys

  # Mock the options
  class Options(object):
    pass
  options = Options()
  options.enabled = None
  options.force = None
  options.masked = None
  options.name = None
  options.scope = 'system'
  options.state = None

  # Mock the params
  class Params(object):
    pass
  module = Params()
  module.params = options

  # Mock the module
  class Module(object):
    def __init__(self, *args):
      pass
    def fail_json(self, *args):
      sys.exit(1)
    def exit_json(self, *args):
      sys.exit(0)
    def get_bin_path(self, *args):
      return "/bin/systemctl"

# Generated at 2022-06-13 06:26:33.937454
# Unit test for function main

# Generated at 2022-06-13 06:26:46.279318
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from os.path import splitext
    module_path = splitext(splitext(__file__)[0])[0] + '_unit_test.py'


# Generated at 2022-06-13 06:26:56.397364
# Unit test for function main

# Generated at 2022-06-13 06:27:02.071720
# Unit test for function main
def test_main():
    test_systemctl = dict(
        name=None,
        state=None,
        enabled=None,
        force=False,
        masked=None,
        daemon_reload=False,
        daemon_reexec=False,
        scope='system',
        no_block=False,
    )

    module = AnsibleModule(
        argument_spec=test_systemctl,
        supports_check_mode=True,
    )

    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:37.564778
# Unit test for function main
def test_main():

    from ansible.module_utils.systemd import State, Masked
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 06:27:45.044856
# Unit test for function main
def test_main():
    def get_bin_path(self, arg, required=False):
        return '/usr/bin/systemctl'

    def run_command(self, arg):
        return (0, '', '')

    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 06:27:57.386204
# Unit test for function main
def test_main():
    sys.modules['ansible.module_utils.basic'] = MagicMock()
    sys.modules['ansible.module_utils.six'] = MagicMock()
    sys.modules['ansible.module_utils.pycompat24'] = MagicMock()
    sys.modules['requests'] = MagicMock()
    sys.modules[
        'ansible.module_utils.ec2'] = MagicMock()
    sys.modules['ansible.module_utils.urls'] = MagicMock()
    sys.modules['ansible.module_utils.six.moves.urllib.request'] = MagicMock()
    sys.modules['ansible.module_utils.six.moves.urllib.error'] = MagicMock()

# Generated at 2022-06-13 06:28:10.132929
# Unit test for function main
def test_main():
    # Not a good unit test as we are doing side effects with main()
    from ansible.module_utils.basic import AnsibleModule

    # setup the modules arguments

# Generated at 2022-06-13 06:28:21.879300
# Unit test for function main
def test_main():
    argv = ['systemd']

# Generated at 2022-06-13 06:28:23.393218
# Unit test for function main
def test_main():
    unit_test_main(module_args)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:33.767910
# Unit test for function main
def test_main():
    test_input = sys.argv[1]

    if not os.path.isfile(test_input):
        sys.exit(0)

    # Load the test data
    with open(test_input, "r") as f:
        test_data = json.load(f)

        # Set up stdout/err/rc to appear as a normal run
        if 'status' in test_data:
            sys.exit(0)
        elif 'msg' in test_data:
            sys.stderr.write(test_data['msg'] + "\n")
            sys.exit(1)
        else:
            sys.stderr.write("Unrecognized integrity test data\n")
            sys.exit(1)

# For backwards compatibility
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:40.641112
# Unit test for function main
def test_main():
    """Unit test for function main.
    """
    # first test
    mock_module = MagicMock()
    mock_module.params = {
        'scope': 'system',
        'no_block': False,
        'daemon_reexec': False,
        'daemon_reload': False,
        'masked': None,
        'name': None,
        'force': False,
        'enabled': None,
        'state': None
    }
    mock_module.run_command.return_value = (0, '', '')
    mock_module.check_mode = False
    mock_module.fail_json.side_effect = fail_json
    main()
    # second test

# Generated at 2022-06-13 06:28:51.499985
# Unit test for function main

# Generated at 2022-06-13 06:29:00.894473
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', default='dummy.service')
        )
    )
    result = dict(
        name='dummy.service',
        changed=False,
        status=dict(),
    )
    test_result = dict(
        name='dummy.service',
        changed=False,
        status=dict(Loaded='loaded'),
    )
    test_result2 = dict(
        name='dummy.service',
        changed=False,
        status=dict(Loaded='loaded', ActiveState='active'),
    )

    # Unit test for empty systemctl output.
    module.run_command = MagicMock(return_value=(0, '', ''))  # noqa
    main()
    assert module.exit_json.called
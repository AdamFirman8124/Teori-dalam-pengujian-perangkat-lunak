

# Generated at 2022-06-13 06:21:10.125254
# Unit test for function main
def test_main():

    import json
    import os
    import shutil
    import tempfile
    import subprocess
    import sys

    import ansible.utils.path
    from ansible.module_utils.six import b
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils._text import to_bytes

    def chroot(path, cmd, shell=True):
        return subprocess.check_output(['chroot', path, 'bash', '-c', cmd], shell=shell)


# Generated at 2022-06-13 06:21:13.452286
# Unit test for function main
def test_main():
    print("Test invoking main()...")
    with open('/tmp/ansible_systemctl_test.log', 'w') as f:
        f.write('test')
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:23.818759
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:30.841141
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:42.350199
# Unit test for function main
def test_main():

    import platform
    import re
    import shutil
    import os
    import tempfile

    # Monkeypatch module class with fake constants
    module = AnsibleModule(argument_spec=dict())
    module.BIN_PATH_SYSTEMCTL_CMD = ['systemctl']
    module.BIN_PATH_CHROOT_CMD = ['chroot']


    # Monkeypatch module class with fake functions
    def mock_run_command_systemctl_show(cmd, check_rc=False):

        # Check that this is called with $systemctl show 'unit'
        s = re.match(r"^systemctl\s+(?:--\S+\s+)*show\s+'(\S+)'$", cmd)

# Generated at 2022-06-13 06:21:46.094864
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request')
    assert request_was_ignored('ignoring command')
    assert not request_was_ignored('= gamin.service - Gamin File and Directory Monitoring Service')



# Generated at 2022-06-13 06:21:56.692560
# Unit test for function main
def test_main():
    from ansible.module_utils.common.collections import namedtuple

# Generated at 2022-06-13 06:22:09.128690
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 06:22:16.567927
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # This tests the case where a key=value pair is on a single line.
    lines = ['UnitFileState=enabled\n']
    ret = parse_systemctl_show(lines)
    assert ret == {'UnitFileState': 'enabled'}

    # This tests the case where a key=value pair is on multiple lines.
    lines = [
        'ExecStart={ path=/usr/sbin/crond ; argv[]=/usr/sbin/crond -n $CRONDARGS ; '
        'ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; '
        'status=0/0 }\n',
    ]
    ret = parse_systemctl_show(lines)

# Generated at 2022-06-13 06:22:28.690232
# Unit test for function main

# Generated at 2022-06-13 06:23:01.725681
# Unit test for function main
def test_main():
    fields = {
        "name": "unit_name",
        "enabled": True,
        "masked": False,
        "daemon_reload": False,
        "daemon_reexec": False,
        "scope": "system",
        "no_block": False,
    }
    check_args(**fields)
    with pytest.raises(AnsibleFailJson) as exc:
        main()
    print('Info: %s' % exc.value.args[0]['msg'])

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:11.176330
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 06:23:19.007602
# Unit test for function main
def test_main():
    result = dict(
        name='unit',
        changed=False,
        status=dict(),
    )
    
    result['status'] = dict(LoadState='masked')
    assert is_masked_service(result['status']) == True

    result['status'] = dict(LoadState='not-found')
    assert is_masked_service(result['status']) == False

    result['status'] = dict(LoadState='loaded')
    assert is_masked_service(result['status']) == False

    result['status'] = dict()
    assert is_masked_service(result['status']) == False

    assert sysv_exists('systemd-sysv-install') == True
    assert sysv_exists('fake-service') == False


# Generated at 2022-06-13 06:23:29.037188
# Unit test for function main

# Generated at 2022-06-13 06:23:40.044148
# Unit test for function main
def test_main():
    def check(name):
        assert name.startswith('test_') or name.startswith('test-')
    # Create fake ansible module
    class FakeModule(object):
        params = {}
        fail_json = lambda *args, **kwargs: sys.exit(1)
        exit_json = lambda *args, **kwargs: sys.exit(0)
        run_command = lambda *args, **kwargs: sys.exit(0)

        if sys.version_info < (3, 0):
            # Python 2
            class CheckMode(object):
                check_mode = False
            check_mode = CheckMode()
        else:
            # Python 3
            check_mode = False

    # Create fake stdin and stdout
    File = StringIO.StringIO
    sys.stdin = File()
    sys

# Generated at 2022-06-13 06:23:52.133460
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={
        'name': dict(type='str', default='cron'),
        'state': dict(type='str'),
        'enabled': dict(type='bool'),
        'force': dict(type='bool'),
        'masked': dict(type='bool'),
        'daemon_reload': dict(type='bool', aliases=['daemon-reload']),
        'daemon_reexec': dict(type='bool', aliases=['daemon-reexec']),
        'scope': dict(type='str'),
    },
    supports_check_mode=True)

    class AnsibleRun:
        def __init__(self, module):
            self.module = module

        def run_command(self, cmd, check_rc=False):
            rc = 0

# Generated at 2022-06-13 06:23:59.209999
# Unit test for function main
def test_main():
    FAKE_SYSTEMCTL = """
● lightdm.service - Light Display Manager
   Loaded: loaded (/lib/systemd/system/lightdm.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2018-07-30 10:04:00 UTC; 1s ago
     Docs: man:lightdm(1)
 Main PID: 8473 (lightdm)
    Tasks: 2 (limit: 4915)
   CGroup: /system.slice/lightdm.service
           └─8473 /usr/sbin/lightdm
"""

# Generated at 2022-06-13 06:24:01.313871
# Unit test for function main
def test_main():
  main()
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:12.862138
# Unit test for function main

# Generated at 2022-06-13 06:24:17.095306
# Unit test for function main
def test_main():
    test_dict = {
        'unit': 'crond',
        'scope': 'system',
        'state': 'stopped',
    }

    rc, out, err = main(test_dict)
    assert rc == 0

if __name__ == "__main__":
    main()

# Generated at 2022-06-13 06:25:01.645115
# Unit test for function main

# Generated at 2022-06-13 06:25:05.038037
# Unit test for function main
def test_main():
    for i in [1,2,3,4]:
        print(i)

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
else:
    test_main()

# Generated at 2022-06-13 06:25:12.090599
# Unit test for function main
def test_main():
    args = dict(
        name=dict(type='str', aliases=['service']),
        state=dict(type='str', choices=['reloaded', 'restarted', 'started', 'stopped']),
        enabled=dict(type='bool'),
        force=dict(type='bool'),
        masked=dict(type='bool'),
        no_block=dict(type='bool', default=False),
        scope=dict(type='str', default='system', choices=['system', 'user', 'global'], aliases=['scock']),
    )
    main(args)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:22.777798
# Unit test for function main
def test_main():
    # Set up unit test environment
    ModuleData = namedtuple('ModuleData', ['params'])
    module = ModuleData(params={})

    module.params['name'] = 'cron'
    module.params['state'] = 'restarted'
    module.params['no_block'] = 'True'
    module.params['enabled'] = 'True'
    module.params['force'] = 'False'
    module.params['masked'] = 'False'
    module.params['daemon_reload'] = 'False'
    module.params['daemon_reexec'] = 'False'
    module.params['scope'] = 'system'

    result = main()

    assert result['name'] == 'cron'
    assert result['changed'] == True
    assert result['enabled'] == True

# Generated at 2022-06-13 06:25:24.098749
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={})
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:34.094851
# Unit test for function main
def test_main():
    test_dict = dict(
        state='started',
        name='Unit1',
        enabled=False,
        masked=None,
        daemon_reload=False,
        daemon_reexec=False,
        scope='system',
        no_block=False,
        force=False,
    )

    result = dict(
        name='Unit1',
        changed=False,
        status=dict(),
    )

# Generated at 2022-06-13 06:25:41.964072
# Unit test for function main
def test_main():
    # Test systemctl is installed
    try:
        __salt__['cmd.run']('systemctl --version')
    except:
        # unit test not available
        return

    with test_common.tempdir() as tmpdir:
        args = {
            'name': 'systemd-test',
            'masked': False,
            'enabled': False,
            'state': 'stopped',
            'scope': 'system',
            'force': True
        }
        client = salt.client.get_local_client()
        ret = client.cmd(
            'minion',
            'systemd.mod_watch',
            ['systemd-test.service'],
            'systemd.running',
            ['or', 'systemd.dead'],
            expr_form='compound')

# Generated at 2022-06-13 06:25:47.486009
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import os
    import sys

    module = AnsibleModule(dict())
    module.run_command = lambda x: (0, '', '')

    sys.modules['__main__'] = sys.modules['ansible.modules.system.systemd']
    sys.modules['ansible'] = sys.modules['ansible.modules.system.systemd']

    del sys.modules['ansible.modules.system.systemd'].__package__
    sys.modules['ansible.modules.system.systemd'].__package__ = 'ansible.modules.system'
    sys.modules['ansible.modules.system.systemd'].main()

# Generated at 2022-06-13 06:25:55.748920
# Unit test for function main
def test_main():
    # Imports
    import tempfile
    import shutil
    import os
    import sys
    import pytest
    import ansible.utils
    import ansible.errors
    import ansible.module_utils.basic
    import ansible.module_utils.six
    import ansible.module_utils._text
    import ansible.module_utils.systemd

    import ansible.modules.system.systemd
    import ansible.modules.system.systemd.systemd

    # Initialize
    module_args = {}
    result = {'changed': False}

    # Setup
    if os.path.exists('/tmp/ansible_systemd_test'):
        shutil.rmtree('/tmp/ansible_systemd_test')
    os.mkdir('/tmp/ansible_systemd_test')

# Generated at 2022-06-13 06:25:57.626502
# Unit test for function main
def test_main():
    main()

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:16.453155
# Unit test for function main
def test_main():
    # Chroot Tests
    temp_dir_path = tempfile.mkdtemp()
    chroot_dir = os.path.join(temp_dir_path, 'chroot')
    os.mkdir(chroot_dir)
    os.mkdir(os.path.join(chroot_dir, 'bin'))
    os.mkdir(os.path.join(chroot_dir, 'usr'))
    os.mkdir(os.path.join(chroot_dir, 'usr', 'bin'))
    os.mkdir(os.path.join(chroot_dir, 'usr', 'lib'))
    os.mkdir(os.path.join(chroot_dir, 'usr', 'libexec'))
    os.mkdir(os.path.join(chroot_dir, 'etc'))
   

# Generated at 2022-06-13 06:27:23.411365
# Unit test for function main

# Generated at 2022-06-13 06:27:34.550856
# Unit test for function main
def test_main():
    from ansible.modules.system.systemd import main
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def run_command(self, cmd):
            if "is-enabled" in cmd:
                return 1, "", ""
            elif "daemon-reload" in cmd:
                return 0, "", ""
            elif "daemon-reexec" in cmd:
                return 0, "", ""
            elif "is-active" in cmd:
                return 0, "inactive", ""
            elif "show" in cmd:
                return 0, "LoadState=not-found", ""

# Generated at 2022-06-13 06:27:42.591275
# Unit test for function main

# Generated at 2022-06-13 06:27:48.654579
# Unit test for function main

# Generated at 2022-06-13 06:27:59.448108
# Unit test for function main

# Generated at 2022-06-13 06:28:07.237714
# Unit test for function main
def test_main():
    #Params is the object that maps arguments
    params = {"state": "stopped", "enabled": None,"masked": None, "name": None, "daemon_reload": False}
    #
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    module.exit_json(**main(module, params))

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:16.874794
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.modules.system.service import main
    from ansible.module_utils.six import iteritems
    attrs = dict(
        name='sshd.service',
        state='reloaded',
        enabled=None,
        masked=None,
        daemon_reload=False,
        daemon_reexec=False,
        scope='system',
        no_block=False,
    )
    module = AnsibleModule(argument_spec=attrs)
    main(module)


if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 06:28:25.106452
# Unit test for function main
def test_main():

    class ModuleStub(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.fail_json = kwargs.get('fail_json', None)

        def get_bin_path(self, arg0, arg1):
            return "/usr/bin/systemctl"

        def run_command(self, arg0, **kwargs):
            return (0, "", "")

        def check_mode(self):
            pass

        def fail_json(self, **kwargs):
            pass

    class FunctionStub(object):
        def __init__(self, **kwargs):
            self.module = ModuleStub(**kwargs)

    # Initialize the service

# Generated at 2022-06-13 06:28:40.322616
# Unit test for function main
def test_main():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.systemd import main
    from ansible_collections.misc.not_a_real_collection.tests.unit.compat import unittest
    from ansible_collections.misc.not_a_real_collection.tests.unit.compat.mock import patch

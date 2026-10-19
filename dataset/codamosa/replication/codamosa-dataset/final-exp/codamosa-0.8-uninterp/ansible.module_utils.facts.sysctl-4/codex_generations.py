

# Generated at 2022-06-13 02:09:24.616170
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:09:26.937158
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(None, ['net.ipv4.tcp_fin_timeout']) == {'net.ipv4.tcp_fin_timeout': '60'}

# Generated at 2022-06-13 02:09:34.226238
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})
    sysctl = get_sysctl(module=module, prefixes=['kernel'])
    assert sysctl['kernel.threads-max'] == '155832'

    module = AnsibleModule({})
    rc, out, err = module.run_command(['/bin/sysctl', '-n', 'kernel.threads-max'])
    assert rc == 0
    assert to_text(out, errors='surrogate_then_replace').rstrip() == sysctl['kernel.threads-max']

# Generated at 2022-06-13 02:09:41.691537
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    assert {'kern.malloc_size': '1074266624', 'kern.waypoint_max': '10'} == get_sysctl(AnsibleModule(), ['-a']), "Should find all sysctls"
    assert {'kern.malloc_size': '1074266624'} == get_sysctl(AnsibleModule(), ['-a', '-P', '/kern/malloc_size']), "Should find sysctl with prefix"

# Generated at 2022-06-13 02:09:45.518315
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule({},{})
    sysctl = get_sysctl(module,'vm.overcommit_memory vm.overcommit_ratio')
    assert sysctl['vm.overcommit_memory'] == '0'
    assert sysctl['vm.overcommit_ratio'] == '50'
    
    

# Generated at 2022-06-13 02:09:48.558156
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={})
    results = get_sysctl(module, ['kernel.randomize_va_space'])
    assert results['kernel.randomize_va_space'] == '2'

# Generated at 2022-06-13 02:09:52.503704
# Unit test for function get_sysctl
def test_get_sysctl():
    # check if we can get sysctl output, if not the test fails right away
    # because the test environment is not correct
    sysctl = get_sysctl(dict(), ['kernel'])
    assert 'kernel' in sysctl
    assert 'version' in sysctl

# Generated at 2022-06-13 02:09:59.925384
# Unit test for function get_sysctl
def test_get_sysctl():
    from random import choice
    from tempfile import mkstemp
    from shutil import copy
    from os import fsync, close, remove
    from ansible.module_utils._text import to_bytes

    # Create temp file with sysctl params
    _, sysctl_file = mkstemp()
    sysctl_params = {
        'net.ipv4.ip_forward': '1',
        'net.ipv6.conf.all.forwarding': '1',
        'fs.aio-max-nr': '1048576',
        'vm.max_map_count': '131060',
        'vm.swappiness': '0',
        'kernel.pid_max': '4194304',
    }

# Generated at 2022-06-13 02:10:08.956411
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    # The values here mirror what's in the sysctl manpage on macOS
    assert module.get_bin_path('sysctl') == '/sbin/sysctl'
    assert get_sysctl(module, ['-n', 'hw.memsize']) == {'hw.memsize': '4294967296'}
    assert get_sysctl(module, ['-n', 'kern.boottime']) == {'kern.boottime': '{ sec = 1530448862, usec = 0 } Fri Jul 6 11:14:22 2018'}

# Generated at 2022-06-13 02:10:13.473637
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MockAnsibleModule()
    # Create a sysctl command output
    sysctl_out = """net.ipv4.tcp_max_syn_backlog = 512
    net.ipv4.ip_local_port_range = 4000    65000
    kernel.panic = 10"""

    # Create a dict from the sysctl output
    sysctl_values = dict()
    key = ''
    value = ''
    for line in sysctl_out.splitlines():
        if not line.strip():
            continue

        if line.startswith(' '):
            # handle multiline values, they will not have a starting key
            # Add the newline back in so people can split on it to parse
            # lines if they need to.
            value += '\n' + line
            continue

        if key:
            sys

# Generated at 2022-06-13 02:10:27.342532
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl({}, ['kern.maxvnodes']) == {'kern.maxvnodes': '131072'}
    assert get_sysctl({}, ['kern.maxvnodes', 'kern.maxproc']) == {'kern.maxvnodes': '131072', 'kern.maxproc': '12288'}


# Generated at 2022-06-13 02:10:38.701460
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MagicMock()
    module.fail_json.side_effect = SystemExit
    module.run_command.return_value = [0, 'net.ipv4.tcp_syncookies = 1', '']
    result = get_sysctl(module, ['net.ipv4.tcp_syncookies'])
    assert result == {'net.ipv4.tcp_syncookies': '1'}

    module.run_command.return_value = [0, 'net.ipv6.conf.all.disable_ipv6 = 1', '']
    result = get_sysctl(module, ['net.ipv6.conf.all.disable_ipv6'])
    assert result == {'net.ipv6.conf.all.disable_ipv6': '1'}

    module

# Generated at 2022-06-13 02:10:46.612341
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    prefix_list = [ 'kern.hostname', 'kern.osrelease', 'kern.version' ]
    result = get_sysctl(module, prefix_list)
    assert result == {'kern.hostname': 'localhost.localdomain', 'kern.osrelease': '4.2.2-1.fc22.x86_64', 'kern.version': '#1 SMP Mon Mar 2 22:33:52 UTC 2015'}


# Generated at 2022-06-13 02:10:54.141686
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:11:03.718049
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic


# Generated at 2022-06-13 02:11:08.692526
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict(prefixes=dict(type='list')),
        supports_check_mode=True
    )
    values = get_sysctl(module, ['kernel', 'vm'])
    assert values['kernel.hostname'] == 'nad-util'
    assert values['vm.dirty_ratio'] == '40'

# Generated at 2022-06-13 02:11:16.756783
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    import os

    class FakeModule(AnsibleModule):
        def __init__(self):
            super(FakeModule, self).__init__()

            self.params = dict()
            self.fail_json = lambda *args, **kwargs: None

            self.run_command = run_command
            self.get_bin_path = get_bin_path


# Generated at 2022-06-13 02:11:21.914745
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(argument_spec=dict())
    prefixes = ['-a', 'net.ipv4.conf']
    sysctl = get_sysctl(module, prefixes)
    assert sysctl is not None
    assert 'net.ipv4.conf.default.accept_source_route' in sysctl

# Generated at 2022-06-13 02:11:26.228301
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(module, ['vm']) == {'vm.swappiness': '1', 'vm.max_map_count': '65530', 'vm.dirty_ratio': '20', 'vm.dirty_background_ratio': '10', 'vm.dirty_writeback_centisecs': '500'}

# Generated at 2022-06-13 02:11:29.374456
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            prefixes=dict(type='list', default=[]),
        )
    )

    assert len(get_sysctl(module, [])) > 0

# Generated at 2022-06-13 02:11:47.408537
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    sysctl = get_sysctl(module, ["nothing", "does", "not", "exist"])
    assert sysctl == dict()


# Generated at 2022-06-13 02:11:50.457923
# Unit test for function get_sysctl
def test_get_sysctl():
    module = None # not needed
    prefixes = ['vm.swappiness']
    sysctl = get_sysctl(module, prefixes)
    assert 'vm.swappiness' in sysctl
    assert sysctl['vm.swappiness'] == '60'

# Generated at 2022-06-13 02:11:54.284847
# Unit test for function get_sysctl
def test_get_sysctl():
    test_command = ["sysctl", "-n", "kern.maxproc", "kern.maxprocperuid"]
    test_output = "kern.maxproc: 1\nkern.maxprocperuid: 2"
    assert get_sysctl(test_command) == {"kern.maxproc":"1", "kern.maxprocperuid":"2"}

# Generated at 2022-06-13 02:12:06.033330
# Unit test for function get_sysctl
def test_get_sysctl():
    mock_module = MockModule()

# Generated at 2022-06-13 02:12:12.904696
# Unit test for function get_sysctl
def test_get_sysctl():
    module_mock = MagicMock()
    module_mock.run_command.return_value = (0, '', '')

    sysctl_data = get_sysctl(module_mock, 'net.ipv4.ip_forward')

    module_mock.run_command.assert_called_once_with([module_mock.get_bin_path.return_value, 'net.ipv4.ip_forward'])
    assert sysctl_data == {'net.ipv4.ip_forward': ''}



# Generated at 2022-06-13 02:12:21.093489
# Unit test for function get_sysctl
def test_get_sysctl():
    import os
    import tempfile

    test_file = tempfile.mkstemp()
    os.write(test_file[0], b'''vm.swappiness = 0
net.ipv4.ip_forward = 0
net.ipv6.conf.all.forwarding = 0
''')
    os.close(test_file[0])

    os.environ["PATH"] = os.path.dirname(test_file[1]) + os.pathsep + os.environ["PATH"]

    module = type('DummyModule', (object,), dict(run_command=lambda self, x: (0, '', ''), get_bin_path=lambda self, x: x))()

# Generated at 2022-06-13 02:12:27.332850
# Unit test for function get_sysctl
def test_get_sysctl():

    from ansible.module_utils.basic import AnsibleModule
    test_module = AnsibleModule({'test': True})


# Generated at 2022-06-13 02:12:37.575689
# Unit test for function get_sysctl
def test_get_sysctl():
    try:
        from ansible.module_utils.basic import AnsibleModule
    except ImportError:
        import sys
        sys.path.append('../../../')
        from ansible.module_utils.basic import AnsibleModule
    import StringIO
    import sys

    # Simulate an AnsibleModule object
    module = AnsibleModule(argument_spec={})

    # Simulate module.run_command, globals is quirky here
    def run_command(*args, **kwargs):
        if args[0][0] == 'bad-command':
            return 1, "ERROR: Unknown argument: bad-command", ""
        return 0, "", ""
    module.run_command = run_command

    # Simulate module.get_bin_path, globals is quirky here

# Generated at 2022-06-13 02:12:43.763559
# Unit test for function get_sysctl
def test_get_sysctl():
    import ansible.module_utils.basic
    m = ansible.module_utils.basic.AnsibleModule({})
    assert m
    curr = get_sysctl(m, ['kern.ostype'])
    assert curr
    assert 'kern.ostype' in curr
    assert curr['kern.ostype'] == 'Darwin'

# Generated at 2022-06-13 02:12:48.528712
# Unit test for function get_sysctl
def test_get_sysctl():
    # pylint: disable=unused-import,import-error,unused-variable,no-name-in-module
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    # pylint: enable=unused-import,import-error,unused-variable,no-name-in-module

    module_args = dict(
        prefixes=['net.ipv4.tcp_keepalive_time', 'net.ipv4.ip_local_port_range']
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    out = ImmutableDict(changed=False, original_message='', message='')
    sysctl = get_

# Generated at 2022-06-13 02:13:27.193016
# Unit test for function get_sysctl
def test_get_sysctl():
    module = FakeAnsibleModule()

    prefixes = ['kern', 'fs']
    current_sysctl_values = get_sysctl(module, prefixes)

    # Make sure we have some values returned, some of these might go away
    # if they are not enabled in the kernel.
    # The values are not checked as that would be different by OS and kernel
    # version.
    assert current_sysctl_values['fs.aio-max-size']
    assert current_sysctl_values['kern.argmax']
    assert current_sysctl_values['kern.bootfile']
    assert current_sysctl_values['kern.boottime']
    assert current_sysctl_values['kern.hostid']



# Generated at 2022-06-13 02:13:34.148539
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec = dict()
    )

    # Test with no arguments / output
    assert get_sysctl(module, []) == {}
    # Test with a single value
    assert get_sysctl(module, ['sysctl_test.a']) == {'sysctl_test.a': '1'}
    # Test with a value that's on multiple lines
    assert get_sysctl(module, ['sysctl_test.b']) == {'sysctl_test.b': '1\n2\n3\n4'}
    # Test with multiple values

# Generated at 2022-06-13 02:13:40.525418
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    expected = dict(
        kernel = dict(
            version = '4.4.0-96-generic'
        ),
        vm = dict(
            swappiness = '60'
        )
    )

    result = get_sysctl(m, ['kernel', 'vm'])
    m.exit_json(changed = False,
                data = result,
                message = "systemctl modules loaded")

    assert result == expected



# Generated at 2022-06-13 02:13:48.439545
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    import os

    class FakeModule:
        def __init__(self, module_name, bin_path=''):
            self.name = module_name
            self.params = {}
            self.bin_path = bin_path

        def get_bin_path(self, module_name, required=True):
            return os.path.join(self.bin_path, module_name)

        def run_command(self, cmd):
            return 0, '', ''

        def warn(self, msg):
            print(msg)

    if sys.version_info.major == 2:
        from StringIO import StringIO
    elif sys.version_info.major == 3:
        from io import StringIO


# Generated at 2022-06-13 02:13:52.455064
# Unit test for function get_sysctl
def test_get_sysctl():
    import sysctl
    module = sysctl.AnsibleModule(
        argument_spec=dict(
            prefixes=dict(default=['fs.file-nr'], type='list'),
        ),
    )
    expected_dict = {'fs.file-nr.open': '903617', 'fs.file-nr.unused': '903168'}
    assert get_sysctl(module, ['fs.file-nr']) == expected_dict

# Generated at 2022-06-13 02:13:58.931123
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('TestUtilModule', (object,), dict(
        run_command=lambda self, cmd: (0, '', ''),
        get_bin_path=lambda self, bin_name: bin_name,
    ))

    assert get_sysctl(module, ['bla.bla.bla.bla=', 'bla.bla.bla.bla']) == {
        'bla.bla.bla.bla': '',
    }

    assert get_sysctl(module, ['bla.bla.bla.bla:', 'bla.bla.bla.bla']) == {
        'bla.bla.bla.bla': '',
    }


# Generated at 2022-06-13 02:14:07.448590
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:14:10.239217
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec={})
    result = get_sysctl(module, ['net.ipv4.ip_forward',
                                 'kernel.hostname'])
    assert result['kernel.hostname'] == 'localhost'


# Generated at 2022-06-13 02:14:21.060424
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MockModule()
    sysctl = get_sysctl(module, ['vm.overcommit_memory', 'vm.overcommit_ratio'])

    # In this example the module command will return:
    # vm.overcommit_memory = 0
    # vm.overcommit_ratio = 50
    #
    # Some hand tweaking is done below to make sure our test works across different linux
    # distributions which may have different sysctl output.
    #
    # ==> vm.overcommit_memory = \n0\n
    # ==> vm.overcommit_ratio = \n50\n
    #
    # And finally get_sysctl will return:
    # {
    #     'vm.overcommit_memory': '0',
    #     'vm.overcommit_ratio': '50'
    # }

# Generated at 2022-06-13 02:14:26.709527
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    keys = ['kernel.hostname', 'kernel.msgmni']
    assert module.get_bin_path('sysctl')
    sysctls = get_sysctl(module, keys)
    import socket
    for key in keys:
        assert sysctls[key]
    assert sysctls['kernel.hostname'] == socket.gethostname()
    assert isinstance(sysctls['kernel.msgmni'], int)

# Generated at 2022-06-13 02:15:42.789897
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('MockModule', (object,), {})
    module.run_command = type('MockRun_Command', (object,), {})
    module.run_command.return_value = 0, '''kernel.domainname = testing
net.ipv4.ip_forward = 0
net.ipv6.conf.all.disable_ipv6 = 1''', ''
    module.warn = type('MockWarn', (object,), {})
    module.warn.return_value = None
    sysctl = get_sysctl(module, ['net'])
    assert sysctl['net.ipv4.ip_forward'] == '0'
    assert sysctl['net.ipv6.conf.all.disable_ipv6'] == '1'

# Generated at 2022-06-13 02:15:48.708100
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl_data = {
        'dev.intr.nmi.rate': '0',
        'dev.intr.nmi.threshold': '1',
        'dev.intr.nmi.weight': 'll',
        'dev.acpi.passthru': '0',
        'dev.acpi.passthrough': '1',
        'The kernel has a feature called': '"NAME=VALUE" format',
        'The third format is a multiline value': '0',
        'The first type of sysctl parameter': '0',
        'The old-style sysctl parameter': '0',
    }

    module = MockModule()
    assert get_sysctl(module, []) == sysctl_data

    # Test no sysctl output
    module = MockModule(rc=1)
    assert get_

# Generated at 2022-06-13 02:15:51.240087
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    sysctl_result = get_sysctl(module, ['vm.swappiness'])
    assert sysctl_result['vm.swappiness'] == '60'

# Generated at 2022-06-13 02:15:58.447914
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
            argument_spec=dict(
                prefixes=dict(required=True, type='list'),
            ),
            supports_check_mode=True,
        )

    prefixes = module.params['prefixes']
    sysctl = get_sysctl(module, prefixes)

    sysctl_lines = sysctl.keys()

    module.exit_json(changed=False, lines=sysctl_lines)


# Generated at 2022-06-13 02:16:05.917594
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:16:16.002120
# Unit test for function get_sysctl
def test_get_sysctl():
    from units.compat import unittest
    from units.compat.mock import patch
    from ansible.module_utils.basic import AnsibleModule

    class TestGetSysctl(unittest.TestCase):

        def setUp(self):
            self.module = AnsibleModule(
                argument_spec=dict()
            )

            self.sysctl_results = '''
            kern.ipc.maxsockbuf: 16777216
            kern.maxfiles: 327680
            kern.maxfilesperproc: 32768
            kern.threads.max_threads_per_proc: 0

            net.inet.tcp.blackhole: 0
            net.inet.tcp.delayed_ack: 0
            net.inet.tcp.drop_synfin: 0

            '''

       

# Generated at 2022-06-13 02:16:23.649051
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import ansible_module_args

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    module.params.update(ansible_module_args)

    sysctl = get_sysctl(module, ["kernel"])
    assert "kernel.domainname" in sysctl
    assert sysctl["kernel.domainname"] == "(none)"
    assert sysctl.get("kernel.ostype") == "Linux"
    assert sysctl.get("kernel.hardwall") == "1"
    assert sysctl.get("kernel.ngroups_max") == "65536"



# Generated at 2022-06-13 02:16:29.116621
# Unit test for function get_sysctl
def test_get_sysctl():
    # Mocking module.run_command() return values
    import os

    test_cmd = 'sysctl -a'
    test_cmd_result = os.path.join(os.path.dirname(__file__), 'test_sysctl.txt')

    with open(test_cmd_result, 'r') as test_cmd_file:
        test_cmd_output = test_cmd_file.read()

    class ModuleMock(object):
        class RunCmdError(Exception):
            pass
        def __init__(self):
            self.BIN_PATH = {}
            self.BIN_PATH_ARG = {}
            self.fail_json = {}
            self.warn = {}

        def get_bin_path(self, arg, required=False, opt_dirs=[]):
            return self.BIN_

# Generated at 2022-06-13 02:16:31.968709
# Unit test for function get_sysctl
def test_get_sysctl():
    module = FakeModule(args=dict())
    sysctl = get_sysctl(module, ["nf_conntrack_max"])
    assert sysctl['nf_conntrack_max'] == '131072'


# Generated at 2022-06-13 02:16:36.813260
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.sysctl import get_sysctl
    module = AnsibleModule(argument_spec=dict())
    expected = {'kernel.hostname': 'localhost.localdomain'}
    out = get_sysctl(module, ['kernel.hostname'])
    assert out == expected
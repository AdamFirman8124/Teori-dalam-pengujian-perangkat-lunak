

# Generated at 2022-06-13 02:09:21.848008
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    import subprocess

    def run_command(command):
        ''' Run command and return returncode, stdout and stderr '''
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        rc = proc.returncode
        return rc, out, err

    m = sys.modules[__name__]

    command = '/sbin/sysctl -a'
    rc, out, err = run_command(command.split())
    sysctl = get_sysctl(m, ['-a'])

    assert rc == 0
    assert out.strip() == to_text(out).strip()
    assert err.strip() == to_text(err).strip()

# Generated at 2022-06-13 02:09:31.740166
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})

    sysctl = get_sysctl(module, ['net.ipv4.tcp_sack'])
    assert sysctl == dict(net={'ipv4': {'tcp_sack': '1'}})

    sysctl = get_sysctl(module, ['net.ipv4.tcp_sack', 'net.ipv4.tcp_dsack'])
    assert sysctl == dict(net={'ipv4': {'tcp_sack': '1', 'tcp_dsack': '1'}})


# Generated at 2022-06-13 02:09:33.094740
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(['kernel.hostname']) == {'kernel.hostname': 'localhost'}

# Generated at 2022-06-13 02:09:38.319682
# Unit test for function get_sysctl
def test_get_sysctl():
    '''
    Test function get_sysctl
    '''
    # Test argument parsing with sysctl output
    # net.ipv6.conf.all.disable_ipv6 = 0
    # net.ipv6.conf.lo.disable_ipv6 = 0
    # net.ipv6.conf.eth0.disable_ipv6 = 1
    # net.ipv6.conf.default.disable_ipv6 = 0
    # net.ipv6.conf.all.autoconf = 1
    # net.ipv6.conf.lo.autoconf = 1
    # net.ipv6.conf.eth0.autoconf = 1
    # net.ipv6.conf.default.autoconf = 1
    # net.ipv6.conf.all.accept_ra = 1
   

# Generated at 2022-06-13 02:09:42.609468
# Unit test for function get_sysctl
def test_get_sysctl():
    # Use argument spec
    module = AnsibleModule(argument_spec={
        'prefixes': {
            'type': 'list',
            'required': True,
        },
    })
    # Get the sysctl function
    get_sysctl(module, ['net'])

# Generated at 2022-06-13 02:09:50.496278
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    import os
    import pytest
    from ansible_collections.community.systemd.tests.unit.compat import unittest
    from ansible_collections.community.systemd.tests.unit.compat.mock import patch
    from ansible_collections.community.systemd.plugins.module_utils.basic import AnsibleModule

    from ansible_collections.community.systemd.plugins.module_utils.systemd import get_sysctl

    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    fixture_data = {}

    def load_fixture(name):
        path = os.path.join(fixture_path, name)

        if path in fixture_data:
            return fixture_data[path]


# Generated at 2022-06-13 02:09:56.482052
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

    # This would normally be in the invoker
    arguments = dict(
        bin_path="/usr/bin",
    )

    module = AnsibleModule(argument_spec=dict(), supports_check_mode=False)
    module.params.update(arguments)

    # Test if get_sysctl has the correct type
    assert type(get_sysctl(module, ['vm'])) is dict

# Generated at 2022-06-13 02:10:06.483869
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    import ansible.module_utils.basic as basic_module
    from ansible.module_utils.urls import open_url
    import sys

    module = basic.AnsibleModule(
        argument_spec = dict()
    )

    class FakeRunner(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def run(self, cmd):
            return self.rc, self.out, self.err
    # end class FakeRunner

    module.run_command = FakeRunner(0, '''
foo = 42
bar: 64
baz = 13
whizbang = 42
    : 1337
''', '').run

    module.warn = lambda msg: sys.stder

# Generated at 2022-06-13 02:10:13.268116
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:10:19.012526
# Unit test for function get_sysctl
def test_get_sysctl():
    mock_module = type('module', (object,), {})

    mock_module.get_bin_path = lambda x: x
    mock_module.run_command = lambda x: (0, "foo = bar\nbar: baz", "")

    ret = get_sysctl(mock_module, ["foo.bar"])

    assert ret == {"foo": "bar", "bar": "baz"}


# Generated at 2022-06-13 02:10:27.465591
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('Module', (), {
        'run_command': run_command,
        'warn': warn,
    })()

    sysctl = get_sysctl(module, ['net.ipv4.conf.all.rp_filter'])
    assert len(sysctl) == 1
    assert sysctl['net.ipv4.conf.all.rp_filter'] == '1'



# Generated at 2022-06-13 02:10:31.646093
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(['kern.hostname']) == {'kern.hostname': 'FreeBSD'}

# vim: ai et ts=4 sts=4 sw=4 ft=python

# Generated at 2022-06-13 02:10:33.350991
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    sysctl = get_sysctl(module, ['fs.file-nr'])
    assert sysctl['fs.file-nr'] == "3753 0 102724"

# Generated at 2022-06-13 02:10:44.459873
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict(),
    )

    assert module.get_bin_path('sysctl') is not None

    sysctl_out = """
kern.maxproc: 1234
hw.pagesize: 4096
hw.machine: amd64
hw.ncpu: 64
hw.byteorder: 1234
hw.memsize: 1234
hw.memsize: 1234
net.inet.ip.portrange.hifirst: 1234
net.inet.ip.portrange.hilast: 1234
net.inet.ip.portrange.first: 1234
net.inet.ip.portrange.last: 1234
net.inet.ip.redirect: 0
"""

# Generated at 2022-06-13 02:10:45.641480
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MockModule()
    sysctl = get_sysctl(module, ('kernel.domainname',))
    assert sysctl == {'kernel.domainname': 'localdomain'}



# Generated at 2022-06-13 02:10:50.929548
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())

    if sysctl_cmd:
        sysctls = get_sysctl(module, ["vm.swappiness", "kernel.sem"])

        assert sysctls['vm.swappiness'] == '30'
        assert sysctls['kernel.sem'] == '250 32000 32 128'
    else:
        # skip test, sysctl is not available
        pass


# Generated at 2022-06-13 02:10:51.584510
# Unit test for function get_sysctl
def test_get_sysctl():
    pass

# Generated at 2022-06-13 02:10:55.596954
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})
    sysctl = get_sysctl(module, [
        'kernel.sem',
    ])
    assert sysctl['kernel.sem']

# Generated at 2022-06-13 02:11:02.118308
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MagicMock()
    module.get_bin_path = Mock(return_value='/bin/sysctl')
    module.run_command = Mock(return_value=(0, 'foo: 1\nbar: 2\n\nbaz\nbat: 3', ''))

    sysctl = get_sysctl(module, ['foo', 'bar', 'baz'])

    assert sysctl == {'foo':'1', 'bar':'2', 'baz':'bat: 3'}

# Generated at 2022-06-13 02:11:08.266334
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:11:15.039418
# Unit test for function get_sysctl
def test_get_sysctl():
    '''
    ansible.module_utils.basic get_sysctl unit test stub
    '''
    module = AnsibleModule(argument_spec={})
    assert get_sysctl(module, []) == {}

# Generated at 2022-06-13 02:11:25.477461
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl_data = {
        'kern.hostname': 'localhost',
        'net.inet.tcp.delayed_ack': '2',
        'net.inet6.ip6.v6only': '0',
        'machdep.cpu.leaf7_features': '0xEXP',
    }
    sysctl_file = 'sysctl'
    with open(sysctl_file, 'w') as f:
        f.write('{}\n'.format('\n'.join(['%s: %s' % (k, v) for k, v in sysctl_data.items()])))
        f.flush()

    import ansible.module_utils.basic

# Generated at 2022-06-13 02:11:35.193318
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule:
        def get_bin_path(self, name):
            return name

        def run_command(self, cmd):
            return 0, """
kernel.domainname =
kernel.hostname = localhost
kernel.shmmax = ffffffff
kernel.shmmni = 4096
kernel.shmall = 2097152
kernel.msgmax = 65536
kernel.msgmnb = 65536
kernel.msgmni = 2878
kernel.sem = 12058624 25501368 12058624 180321
kernel.printk = 4 4 1 7
vm.swappiness = 0
fs.nr_open = 1048576
fs.file-max = 98304
""", None

    fm = FakeModule()

# Generated at 2022-06-13 02:11:37.102130
# Unit test for function get_sysctl
def test_get_sysctl():
    result = get_sysctl({}, ['kern.ostype'])
    assert result['kern.ostype'] == 'FreeBSD'

# Generated at 2022-06-13 02:11:47.740377
# Unit test for function get_sysctl
def test_get_sysctl():
    assert get_sysctl(['/bin/sh', '-c', 'echo "foo = bar"']) == {'foo': 'bar'}
    assert get_sysctl(['/bin/sh', '-c', 'echo "foo.bar.baz = 1"']) == {'foo.bar.baz': '1'}
    assert get_sysctl(['/bin/sh', '-c', 'echo "foo.bar.test = off"']) == {'foo.bar.test': 'off'}
    assert get_sysctl(['/bin/sh', '-c', 'echo "net.ipv4.route.flush = 1"']) == {'net.ipv4.route.flush': '1'}
    assert get_sysctl(['/bin/sh', '-c', 'echo "foo: bar"'])

# Generated at 2022-06-13 02:11:55.702772
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())

    module.run_command = lambda cmd: (0, 'kern.clockrate: { hz = 100, tick = 10000, tickadj = 1 }\nkern.ostype: Darwin\nkern.osrelease: 13.0.0\nkern.osrevision: 198506\n', '')

    result = get_sysctl(module, [])
    assert result == {
        'kern.clockrate': '{ hz = 100, tick = 10000, tickadj = 1 }',
        'kern.ostype': 'Darwin',
        'kern.osrelease': '13.0.0',
        'kern.osrevision': '198506'
    }

# Generated at 2022-06-13 02:12:06.624274
# Unit test for function get_sysctl
def test_get_sysctl():
    module = MockModule()

    # Test with sysctl not in PATH
    module.bin_path_exists = Mock(return_value=False)
    sysctl = get_sysctl(module, ['net.ipv4.conf.all.rp_filter'])
    assert sysctl == dict(), sysctl

    # Test with success
    module.bin_path_exists = Mock(return_value=True)
    module.run_command = Mock(return_value=(0, 'net.ipv4.conf.all.rp_filter = 1\nnet.ipv4.conf.default.rp_filter = 1', ''))
    sysctl = get_sysctl(module, ['net.ipv4.conf.all.rp_filter', 'net.ipv4.conf.default.rp_filter'])


# Generated at 2022-06-13 02:12:08.338350
# Unit test for function get_sysctl
def test_get_sysctl():
    # FIXME: Implement unit test
    #assert 0, "get_sysctl: FIXME"
    pass


# Generated at 2022-06-13 02:12:11.055203
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({'foo': 'bar'})

    sysctl = get_sysctl(module, [])

    assert sysctl['kernel.pid_max'] == '4194303'

# Generated at 2022-06-13 02:12:19.901408
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('fake_module', (object,), {
        'run_command': lambda b, c: (0, '', ''),
        'get_bin_path': lambda a: a,
        'warn': lambda a: None,
    })()
    assert get_sysctl(module, []) == {}
    module.run_command = lambda b, c: (1, '', '')
    assert get_sysctl(module, []) == {}
    module.run_command = lambda b, c: (0, 'key1 = 1\nkey2 = 2', '')
    assert get_sysctl(module, []) == {'key1': '1', 'key2': '2'}
    module.run_command = lambda b, c: (0, 'key1 = 1\n key2 = 2', '')


# Generated at 2022-06-13 02:12:37.905235
# Unit test for function get_sysctl
def test_get_sysctl():
    # Test command ansible.module_utils.helpers.get_sysctl
    from ansible.module_utils.helpers import get_sysctl
    import tempfile
    import os
    import re
    # Create temporary file, with some data
    fd, fname = tempfile.mkstemp()
    with open(fname, 'w') as tmp:
        tmp.write('abc = def\n'
                  'hij = klm\n'
                  'nop = qrs\n'
                  'nopp = tuv\n')
    # Test for function get_sysctl
    result = get_sysctl(fname, [])
    # Test a=b
    assert result['abc'] == 'def'
    # Test a=b
    assert result['hij'] == 'klm'
    # Test

# Generated at 2022-06-13 02:12:48.588209
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    sys.path.append("")
    from ansible.module_utils.basic import *
    class AnsibleModule(object):
        def __init__(self, argument_spec, bypass_checks=False, no_log=False, check_invalid_arguments=True, mutually_exclusive=None, required_together=None, required_one_of=None, add_file_common_args=False, supports_check_mode=False):
            self.argument_spec = argument_spec
            self.params = argument_spec

        def run_command(self, cmd):
            return (0, "net.ipv4.ip_forward = 1\nnet.ipv4.conf.default.rp_filter = 1\nnet.ipv4.conf.default.accept_source_route = 0\n", "")



# Generated at 2022-06-13 02:12:54.226298
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict(
            prefixes=dict(type='list', required=True)
        )
    )
    result = get_sysctl(module, ['net.ipv4.conf.all.rp_filter'])
    assert len(result) == 1
    assert result['net.ipv4.conf.all.rp_filter'] == '1'

# Generated at 2022-06-13 02:13:02.539843
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic

    class FakeModule:
        def __init__(self, result=None):
            self.params = {}
            self.result = result
            self.fail_json = basic.fail_json
            self.exit_json = basic.exit_json
            self.warn = basic.warn

        def run_command(self, cmd):
            self.result = {
                'kernel.osrelease': '3.10.0-693.21.1.el7.x86_64',
                'kernel.sysrq': '1',
                'kernel.sem': '250  32000 100 122',
            }
            return 0, self.fake_rc, ''


# Generated at 2022-06-13 02:13:12.470010
# Unit test for function get_sysctl
def test_get_sysctl():
    import ansible.module_utils.basic as basic
    import ansible.module_utils.basic as basic
    import ansible.module_utils.common.sysctl as sysctl
    import shutil

    if shutil.which('sysctl') is None:
        return

    sysctls = sysctl.get_sysctl(basic.AnsibleModule(), ['-a'])
    assert 'kernel.sched_child_runs_first' in sysctls
    assert sysctls['kernel.sched_child_runs_first'] == '0'

    sysctls = sysctl.get_sysctl(basic.AnsibleModule(), ['kernel.sched_child_runs_first'])
    assert 'kernel.sched_child_runs_first' in sysctls

# Generated at 2022-06-13 02:13:18.262213
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})

    expr = ['net.ipv4.ip_forward']
    sysctl = get_sysctl(module, expr)

    assert sysctl
    assert isinstance(sysctl, dict)
    assert sysctl['net.ipv4.ip_forward'] == '1'

# Generated at 2022-06-13 02:13:27.442762
# Unit test for function get_sysctl
def test_get_sysctl():

    import sys
    import json

    # patching module for reading environment variables
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.six import PY2

    sys.modules['ansible.module_utils.basic'] = basic

    class AnsibleModuleMock:

        def __init__(self):
            self.params = dict()
            self.params['enforce'] = 'present'
            self.params['name'] = 'net.ipv4.conf.all.rp_filter'
            self.params['value'] = '1'
            self.params['state'] = 'present'
            self.params['persistent'] = 'no'

            self.state = 'present'
            self.changed = False
            self

# Generated at 2022-06-13 02:13:33.943197
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec=dict(
            prefixes=dict(type='list', required=True)
        )
    )

    out = '''
net.ipv4.ip_forward = 0
fs.file-max = 12287


net.ipv4.ip_local_port_range = 49152   65535
'''

    # We don't need to mock the run_command function, we simply pass the data
    # returned from sysctl.  If the function fails we'll know and the test
    # coverage will be updated.
    sysctl = get_sysctl(module, module.params['prefixes'])

    assert sysctl['net.ipv4.ip_local_port_range'] == '49152   65535'

# Generated at 2022-06-13 02:13:41.496933
# Unit test for function get_sysctl
def test_get_sysctl():
    module = type('test', (), {})
    setattr(module, 'run_command', lambda x: (0, '', ''))
    settattr(module, 'get_bin_path', lambda x: '/usr/sbin/sysctl')

    assert get_sysctl(module, []) == {}
    assert get_sysctl(module, ['net.ipv4.ip_forward']) == {
                'net.ipv4.ip_forward': '1',
            }
    assert get_sysctl(module, ['net.ipv4.ip_forward', 'net.bridge.bridge-nf-call-iptables']) == {
                'net.ipv4.ip_forward': '0',
                'net.bridge.bridge-nf-call-iptables': '0',
            }

# Generated at 2022-06-13 02:13:49.215428
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    import pytest


# Generated at 2022-06-13 02:14:12.961079
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl = dict()

    sysctl_cmd = 'sysctl'
    cmd = [sysctl_cmd]
    cmd.extend(['vm.swappiness'])

    sysctl = dict()

    try:
        rc, out, err = module.run_command(cmd)
    except (IOError, OSError) as e:
        print('Unable to read sysctl: %s\n' % to_text(e))
        rc = 1

    if rc == 0:
        key = ''
        value = ''
        for line in out.splitlines():
            if not line.strip():
                continue


# Generated at 2022-06-13 02:14:23.340831
# Unit test for function get_sysctl
def test_get_sysctl():
    import json
    import sys

    class WrapModule:
        def __init__(self, errlines=None, outlines=None):
            self.errlines = errlines
            self.outlines = outlines
            self.commands = dict()
            self.warnings = list()
            self.bin_path_cache = dict()

        def get_bin_path(self, name):
            if name in self.bin_path_cache:
                return self.bin_path_cache[name]
            else:
                self.bin_path_cache[name] = name
                return name

        def warn(self, msg):
            self.warnings.append(msg)


# Generated at 2022-06-13 02:14:29.569886
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    import sys

    module = AnsibleModule(argument_spec={})

    sysctl_prefixes = [
        'kernel.domainname',
        'net.core.somaxconn'
    ]

    sysctl = get_sysctl(module, sysctl_prefixes)

    assert 'kernel.domainname' in sysctl
    assert sysctl['kernel.domainname'] == '(none)'

    assert sysctl['net.core.somaxconn'] == '128'


if __name__ == '__main__':
    test_get_sysctl()

# Generated at 2022-06-13 02:14:35.902680
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils import basic
    from ansible.module_utils.parsing.convert_bool import boolean

    test_result = {'kernel.shmmni': '4096', 'vm.swappiness': '1', 'kernel.msgmax': '65536', 'kernel.msgmnb': '65536', 'kernel.shmmax': '68719476736', 'kernel.msgmni': '2878', 'net.core.rmem_max': '16777216', 'net.core.rmem_default': '16777216', 'net.core.wmem_max': '16777216', 'net.core.wmem_default': '16777216', 'net.ipv4.tcp_wmem': '4096 16777216 16777216'}


# Generated at 2022-06-13 02:14:42.485928
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    sysctls = get_sysctl(module, ['net.ipv4.tcp_rmem'])
    assert sysctls['net.ipv4.tcp_rmem'] == '4096	87380	16777216', 'Could not get right sysctl value (%s)' % sysctls['net.ipv4.tcp_rmem']

# Generated at 2022-06-13 02:14:48.372849
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
        argument_spec={
            'prefixes': {'required': True, 'type': 'list'},
        },
        supports_check_mode=False,
    )

    module.params['prefixes'] = ['net.*', 'vm.*']

    result = get_sysctl(module, module.params['prefixes'])

    assert type(result) is dict
    assert 'kernel.domainname' in result
    assert 'net.ipv4.tcp_fin_timeout' in result
    assert 'net.ipv4.tcp_max_orphans' in result
    assert 'vm.overcommit_kbytes' in result
    assert 'vm.page-cluster' in result

# Generated at 2022-06-13 02:14:54.405949
# Unit test for function get_sysctl
def test_get_sysctl():
    import platform

    from ansible.module_utils.facts.system import get_sysctl

    if platform.system() != 'FreeBSD':
        return dict(skipped=True, msg='This test is only supported on FreeBSD')

    prefixes = ('kern.ostype', 'kern.osrelease')

    res = get_sysctl(module, prefixes)

    assert res.get('kern.ostype') == 'FreeBSD'
    assert res.get('kern.osrelease') == '11.1-RELEASE'




# Generated at 2022-06-13 02:14:58.476105
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(
            argument_spec=dict(
                prefixes=dict(type='list', default=[]),
            ),
    )

    sysctl = get_sysctl(module, ["sys.kernel.ostype", "sys.kernel.osrelease"])
    assert sysctl['sys.kernel.ostype'] == 'FreeBSD'
    assert sysctl['sys.kernel.osrelease'] == '10.3-RELEASE-p6'

# Generated at 2022-06-13 02:15:05.199946
# Unit test for function get_sysctl
def test_get_sysctl():
    fail_msg = "Could not get expected sysctl value"

    if sys.version_info.major == 2:
        net_core_somaxconn = "128"
    else:
        net_core_somaxconn = "128\n"

    sysctl_cmd = module_defaults['sysctl_path']
    cmd = [sysctl_cmd, "net.core.somaxconn"]
    rc, out, err = module.run_command(cmd)

    assert rc == 0, "get_sysctl: command %s failed" % str(sysctl_cmd)
    assert out == net_core_somaxconn, "get_sysctl: %s" % fail_msg


# Generated at 2022-06-13 02:15:11.505146
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.sysctl import (get_sysctl)
    module = AnsibleModule(argument_spec = {})
    sysctl_values = get_sysctl(module, ('kernel.msgmax', 'fs.aio-max-nr'))
    assert sysctl_values['kernel.msgmax'] == '8192'
    assert sysctl_values['fs.aio-max-nr'] == '65536'


# Generated at 2022-06-13 02:15:50.757731
# Unit test for function get_sysctl
def test_get_sysctl():
    import os
    import sys
    import tempfile
    import pytest

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

    from ansible.module_utils.basic import AnsibleModule

    # Prepare some sample data
    test_data = '''
kern.maxvnodes = 524288
hw.availpages = 411875
vm.stats.vm.v_intr = 0
vm.stats.vm.v_swtch = 0
vm.stats.vm.v_trap = 0
vm.stats.vm.v_syscall = 0
vm.stats.vm.v_intr = 0
vm.stats.vm.v_soft = 0
vm.stats.vm.v_swtch = 0
'''

    # Write test data to

# Generated at 2022-06-13 02:16:00.824680
# Unit test for function get_sysctl
def test_get_sysctl():
    module = {}

# Generated at 2022-06-13 02:16:07.510398
# Unit test for function get_sysctl
def test_get_sysctl():
    """
    Basic test of sysctl module
    """
    class MockModule(object):
        def __init__(self):
            self.params = {'failed': False, 'changed': False, 'warnings': []}
            self.run_command_count = 0

        def run_command(self, cmd, *_args, **_kwargs):
            self.run_command_count += 1
            rc = 0
            if cmd[0] == 'false':
                rc = 1

# Generated at 2022-06-13 02:16:17.366793
# Unit test for function get_sysctl
def test_get_sysctl():

    module_mock = AnsibleModule(argument_spec = dict())
    module_mock.run_command = MagicMock()
    module_mock.get_bin_path = MagicMock()

    # First check with no prefixes
    module_mock.get_bin_path.return_value = 'sysctl'
    module_mock.run_command.return_value = (0, 'hw.machine_arch: x86_64\nhw.busfrequency: 100000000\nhw.cpu64bit_capable: 1\nhw.optional.x86_64: 1', '')
    sysctl = get_sysctl(module_mock, [])

# Generated at 2022-06-13 02:16:24.348270
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModuleFake()
    prefixes = ['kern.conftxt', 'vm.conftxt']
    assert get_sysctl(module, prefixes) == {'kern.conftxt': 'hello', 'vm.conftxt': 'world'}

    prefixes = ['kern.conftxt']
    assert get_sysctl(module, prefixes) == {'kern.conftxt': 'hello'}

    prefixes = ['kern.conftxt', 'vm.conftxt']
    module.run_command = lambda x: (1, '', '')
    assert get_sysctl(module, prefixes) == {}

# Support code

# Generated at 2022-06-13 02:16:28.640073
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    sysctl_settings = get_sysctl(module, ['vm.swappiness'])

    assert sysctl_settings == {'vm.swappiness': '60'}



# Generated at 2022-06-13 02:16:37.075793
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule
    from tempfile import mkdtemp
    import os
    import shutil
    import copy

    # We need a fake module to pass to several of the functions
    module = type('obj', (object,), {'exit_json':lambda self, **kwargs: kwargs, 'fail_json':lambda self, **kwargs: kwargs})

    # Make a fake sysctl executable that we control
    TEST_DIR = mkdtemp()

    # Create a fake sysctl executable
    sysctl_exe = open(os.path.join(TEST_DIR, 'sysctl'), 'w+')

# Generated at 2022-06-13 02:16:39.649200
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule()
    sysctl = get_sysctl(module, ['net.ipv4.ip_forward'])
    assert sysctl['net.ipv4.ip_forward'] == '1'

# Generated at 2022-06-13 02:16:41.631458
# Unit test for function get_sysctl
def test_get_sysctl():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec = dict())
    sysctl_dict = get_sysctl(module, ['vm.swappiness'])
    assert len(sysctl_dict) == 1
    assert sysctl_dict['vm.swappiness'] == '60'


# Generated at 2022-06-13 02:16:46.582272
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    import types
    import platform

    # mock module
    get_bin_path_name = 'ansible.module_utils.basic.get_bin_path'
    run_command_name = 'ansible.module_utils.basic.AnsibleModule.run_command'
    warn_name = 'ansible.module_utils.basic.AnsibleModule.warn'

    class AnsibleModule(types.ModuleType):
        def __init__(self):
            self.run_command = lambda x: (0, "net.ipv6.conf.all.accept_dad = 1\nnet.ipv6.conf.default.accept_dad = 1", "")

        def get_bin_path(self, x):
            return "/sbin/sysctl"


# Generated at 2022-06-13 02:18:40.068489
# Unit test for function get_sysctl

# Generated at 2022-06-13 02:18:46.034842
# Unit test for function get_sysctl
def test_get_sysctl():
    module = argparse.Namespace()
    module.run_command = MagicMock()

# Generated at 2022-06-13 02:18:55.963543
# Unit test for function get_sysctl
def test_get_sysctl():
    import sys
    import subprocess

    def _run_command(cmd, input=None):
        p = subprocess.Popen(cmd,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        return (p.returncode, stdout, stderr)

    # Note: the following code is intended to be run on Linux.
    # It should be expanded to cover other OS's in the future.
    #
    # get_sysctl runs the "sysctl" command and parses the output, which
    # looks like one of the following (depending on the -A switch):
    # $ sysctl -a
    # kernel.sysrq = 0
    # kernel

# Generated at 2022-06-13 02:19:03.522739
# Unit test for function get_sysctl
def test_get_sysctl():
    module = AnsibleModule(argument_spec=dict())
    sysctl = get_sysctl(module, ['net.ipv4.conf'])
    assert sysctl.get('net.ipv4.conf.all.accept_local', '') == '0'
    assert sysctl.get('net.ipv4.conf.all.accept_redirects', '') == '0'
    assert sysctl.get('net.ipv4.conf.all.accept_source_route', '') == '0'
    assert sysctl.get('net.ipv4.conf.all.forwarding', '') == '0'
    assert sysctl.get('net.ipv4.conf.all.mc_forwarding', '') == '0'

# Generated at 2022-06-13 02:19:13.072708
# Unit test for function get_sysctl
def test_get_sysctl():
    sysctl_out = '''kernel.hostname = testhost1
kernel.domainname = testdomain1
kernel.osrelease = 3.10.0-327.10.1.el7.x86_64
kernel.ostype = Linux
kernel.osrelease = 3.10.0-327.10.1.el7.x86_64
kernel.version = #1 SMP Tue Feb 16 17:03:48 UTC 2016
kernel.modules_disabled = 0
kernel.hotplug =
kernel.printk = 4     1     1     7
kernel.panic = 0
kernel.panic_on_oops = 0
kernel.unknown_nmi_panic = 0
kernel.tainted = 0
kernel.nmi_watchdog = 1

fs.protected_hardlinks = 1
fs.protected_symlinks = 1
'''
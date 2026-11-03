

# Generated at 2026-11-02 10:20:15.227898
# Unit test for function get_sysctl
def test_get_sysctl():import pytest

from ansible.module_utils.six.moves import builtins
from ansible.module_utils.network.common.utils import get_sysctl


class MockModule(object):
    def __init__(self, rc=0, out='', err='', raise_exc=None, bin_path='/sbin/sysctl'):
        self.rc = rc
        self.out = out
        self.err = err
        self.raise_exc = raise_exc
        self.bin_path = bin_path
        self.warnings = []
        self.commands = []

    def get_bin_path(self, name):
        return self.bin_path

    def run_command(self, cmd):
        self.commands.append(cmd)
        if self.raise_exc is not None:
            raise self.raise_exc
        return self.rc, self.out, self.err

    def warn(self, message):
        self.warnings.append(message)


def test_get_sysctl_single_value():
    out = 'net.ipv4.ip_forward = 1\n'
    module = MockModule(out=out)
    result = module_0.get_sysctl(module, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}


def test_get_sysctl_multiple_values():
    out = (
        'net.ipv4.ip_forward = 1\n'
        'net.ipv4.conf.all.rp_filter = 2\n'
        'net.ipv6.conf.all.forwarding = 0\n'
    )
    module = MockModule(out=out)
    result = module_0.get_sysctl(module, ['net'])
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv4.conf.all.rp_filter': '2',
        'net.ipv6.conf.all.forwarding': '0',
    }


def test_get_sysctl_colon_separator():
    out = 'net.ipv4.ip_forward: 1\n'
    module = MockModule(out=out)
    result = module_0.get_sysctl(module, ['net.ipv4'])
    assert result == {'net.ipv4.ip_forward': '1'}


def test_get_sysctl_multiline_value():
    out = (
        'some.key = value1\n'
        '  continued line\n'
        '  another continued line\n'
        'other.key = value2\n'
    )
    module = MockModule(out=out)
    result = module_0.get_sysctl(module, ['some', 'other'])
    assert result == {
        'some.key': 'value1\n  continued line\n  another continued line',
        'other.key': 'value2',
    }



# Generated at 2026-11-02 10:21:26.539211
# Unit test for function get_sysctl

# Generated at 2026-11-02 10:22:10.168850
# Unit test for function get_sysctl

# Generated at 2026-11-02 10:23:20.110353
# Unit test for function get_sysctl
def test_get_sysctl():
    class FakeModule:
        def __init__(self, rc, out):
            self.rc = rc
            self.out = out
            self.warnings = []
            self.commands = []

        def get_bin_path(self, name):
            assert name == 'sysctl'
            return '/sbin/sysctl'

        def run_command(self, cmd):
            self.commands.append(cmd)
            return self.rc, self.out, ''

        def warn(self, msg):
            self.warnings.append(msg)

    out = (
        'net.ipv4.ip_forward = 1\n'
        'net.ipv4.conf.all.rp_filter = 0\n'
        'net.ipv4.tcp_rmem = 4096\n'
        ' 87380\n'
        '   \n'
        'kern.osproductversion: 10.15\n'
    )

    module = FakeModule(0, out)
    result = module_0.get_sysctl(module, ['net.ipv4', 'kern'])

    assert module.commands == [['/sbin/sysctl', 'net.ipv4', 'kern']], module.commands
    assert module.warnings == [], module.warnings
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv4.conf.all.rp_filter': '0',
        'net.ipv4.tcp_rmem': '4096\n87380',
        'kern.osproductversion': '10.15',
    }, result

    failing_module = FakeModule(1, '')
    assert module_0.get_sysctl(failing_module, ['net']) == {}, module_0.get_sysctl(failing_module, ['net'])

# Generated at 2026-11-02 10:27:06.429937
# Unit test for function get_sysctl

# Generated at 2026-11-02 10:27:56.694776
# Unit test for function get_sysctl
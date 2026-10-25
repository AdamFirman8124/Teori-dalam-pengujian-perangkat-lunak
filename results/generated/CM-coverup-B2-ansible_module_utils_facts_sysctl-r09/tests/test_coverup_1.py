# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

import pytest

from ansible.module_utils.facts.sysctl import get_sysctl


class FakeModule:
    """Minimal stand-in for AnsibleModule covering only what get_sysctl uses."""

    def __init__(self, rc=0, out='', err='', exc=None, bin_path='/sbin/sysctl'):
        self.rc = rc
        self.out = out
        self.err = err
        self.exc = exc
        self.bin_path = bin_path
        self.warnings = []
        self.commands = []
        self.bin_path_requests = []

    def get_bin_path(self, name, *args, **kwargs):
        self.bin_path_requests.append(name)
        return self.bin_path

    def run_command(self, cmd, *args, **kwargs):
        self.commands.append(cmd)
        if self.exc is not None:
            raise self.exc
        return self.rc, self.out, self.err

    def warn(self, msg):
        self.warnings.append(msg)


def test_get_sysctl_parses_all_line_shapes():
    out = (
        'kernel.shmall = 4294967296\n'
        '\n'
        '   \n'
        'net.ipv4.ip_forward = 1\n'
        'vm.swappiness: 60\n'
        'kernel.sem = 250\t32000\t32\t128\n'
        '  continued line\n'
        'badline-without-separator\n'
        'last.key = lastvalue\n'
    )
    module = FakeModule(rc=0, out=out)

    result = get_sysctl(module, ['kernel', 'net'])

    assert result == {
        'kernel.shmall': '4294967296',
        'net.ipv4.ip_forward': '1',
        'vm.swappiness': '60',
        'kernel.sem': '250\t32000\t32\t128\n  continued line',
        'last.key': 'lastvalue',
    }
    # command construction: binary path first, then prefixes
    assert module.bin_path_requests == ['sysctl']
    assert module.commands == [['/sbin/sysctl', 'kernel', 'net']]
    # exactly one warning, for the unparseable line
    assert len(module.warnings) == 1
    assert 'Unable to split sysctl line (badline-without-separator)' in module.warnings[0]


def test_get_sysctl_multiline_value_is_stripped_and_kept():
    out = 'a.b = first\n  second\n  third\n'
    module = FakeModule(rc=0, out=out)

    result = get_sysctl(module, [])

    assert result == {'a.b': 'first\n  second\n  third'}
    assert module.commands == [['/sbin/sysctl']]
    assert module.warnings == []


def test_get_sysctl_empty_output_returns_empty_dict():
    module = FakeModule(rc=0, out='')

    result = get_sysctl(module, ['kernel'])

    assert result == {}
    assert module.warnings == []


def test_get_sysctl_nonzero_rc_returns_empty_dict():
    module = FakeModule(rc=1, out='kernel.shmall = 1\n', err='boom')

    result = get_sysctl(module, ['kernel'])

    assert result == {}
    assert module.warnings == []


@pytest.mark.parametrize('exc', [OSError('no such file'), IOError('io failure')])
def test_get_sysctl_run_command_error_warns_and_returns_empty(exc):
    module = FakeModule(exc=exc)

    result = get_sysctl(module, ['kernel'])

    assert result == {}
    assert len(module.warnings) == 1
    assert module.warnings[0].startswith('Unable to read sysctl: ')
    assert str(exc) in module.warnings[0]

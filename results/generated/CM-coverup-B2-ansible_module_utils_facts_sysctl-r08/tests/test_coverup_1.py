# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

import pytest

from ansible.module_utils.facts.sysctl import get_sysctl


class FakeModule(object):
    """Minimal stand-in for an AnsibleModule; no global state is touched."""

    def __init__(self, run_command_result=None, run_command_exc=None,
                 bin_path='/sbin/sysctl'):
        self.bin_path = bin_path
        self.run_command_result = run_command_result
        self.run_command_exc = run_command_exc
        self.warnings = []
        self.run_command_calls = []

    def get_bin_path(self, name):
        self.bin_path_requests = getattr(self, 'bin_path_requests', [])
        self.bin_path_requests.append(name)
        return self.bin_path

    def run_command(self, cmd):
        self.run_command_calls.append(list(cmd))
        if self.run_command_exc is not None:
            raise self.run_command_exc
        return self.run_command_result

    def warn(self, msg):
        self.warnings.append(msg)


def test_get_sysctl_simple_success():
    out = 'kernel.osrelease = 3.18.6\nkernel.version = #1 SMP\n'
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, ['-a'])

    assert result == {
        'kernel.osrelease': '3.18.6',
        'kernel.version': '#1 SMP',
    }
    assert module.run_command_calls == [['/sbin/sysctl', '-a']]
    assert module.bin_path_requests == ['sysctl']
    assert module.warnings == []


def test_get_sysctl_multiline_and_blank_lines():
    out = (
        'key.one = value one\n'
        '\n'                            # blank line -> skipped
        '   \n'                         # whitespace-only line -> skipped
        'key.two = value two\n'
        '  continued line\n'            # continuation line (starts with space)
        'key.three = value three\n'
        '  trailing continuation\n'     # continuation as the very last line
    )
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, [])

    assert result == {
        'key.one': 'value one',
        'key.two': 'value two\n  continued line',
        'key.three': 'value three\n  trailing continuation',
    }
    assert module.warnings == []


def test_get_sysctl_unsplittable_line_warns_and_keeps_previous_pair():
    out = (
        'good.key = good value\n'
        'this line has no separator\n'
        'other.key = other value\n'
    )
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, [])

    # The bad line cannot be split, a warning is emitted and the previously
    # parsed key/value pair is retained (and flushed again on the next line).
    assert result == {
        'good.key': 'good value',
        'other.key': 'other value',
    }
    assert len(module.warnings) == 1
    assert 'Unable to split sysctl line' in module.warnings[0]
    assert 'this line has no separator' in module.warnings[0]


@pytest.mark.parametrize('exc', [IOError, OSError])
def test_get_sysctl_run_command_raises(exc):
    module = FakeModule(run_command_exc=exc('disk failure'))

    result = get_sysctl(module, ['-a'])

    assert result == {}
    assert module.run_command_calls == [['/sbin/sysctl', '-a']]
    assert len(module.warnings) == 1
    assert 'Unable to read sysctl' in module.warnings[0]
    assert 'disk failure' in module.warnings[0]


def test_get_sysctl_nonzero_rc_returns_empty_dict():
    module = FakeModule(run_command_result=(1, 'partial output', 'some error'))

    result = get_sysctl(module, ['-a'])

    assert result == {}
    assert module.warnings == []


def test_get_sysctl_prefixes_extended_into_command():
    module = FakeModule(run_command_result=(0, '', ''))

    result = get_sysctl(module, ['kernel.hostname', 'kernel.osrelease'])

    assert result == {}
    assert module.run_command_calls == [
        ['/sbin/sysctl', 'kernel.hostname', 'kernel.osrelease'],
    ]

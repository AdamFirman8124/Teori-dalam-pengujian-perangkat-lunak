# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

import pytest

from ansible.module_utils.facts.sysctl import get_sysctl


class FakeModule:
    """Minimal stand-in for an AnsibleModule.

    All state is instance-local and nothing global is patched, so tests
    leave no state pollution behind (no monkeypatch/mocker teardown needed).
    """

    def __init__(self, run_command_result=None, run_command_exc=None,
                 bin_path='/sbin/sysctl'):
        self._run_command_result = run_command_result
        self._run_command_exc = run_command_exc
        self._bin_path = bin_path
        self.bin_path_calls = []
        self.run_command_calls = []
        self.warnings = []

    def get_bin_path(self, name):
        self.bin_path_calls.append(name)
        return self._bin_path

    def run_command(self, cmd):
        self.run_command_calls.append(list(cmd))
        if self._run_command_exc is not None:
            raise self._run_command_exc
        return self._run_command_result

    def warn(self, message):
        self.warnings.append(message)


def test_get_sysctl_success_parses_all_separator_styles():
    out = ('kernel.hostname = host1\n'
           'kern.clockrate: hz 1000\n'
           'vm.swappiness=10\n')
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, ['-a'])

    assert result == {
        'kernel.hostname': 'host1',
        'kern.clockrate': 'hz 1000',
        'vm.swappiness': '10',
    }
    assert module.bin_path_calls == ['sysctl']
    # cmd must be [sysctl binary] + prefixes
    assert module.run_command_calls == [['/sbin/sysctl', '-a']]
    assert module.warnings == []


def test_get_sysctl_skips_blank_lines():
    out = '\n   \nkernel.hostname = host1\n\n'
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, ['-a'])

    assert result == {'kernel.hostname': 'host1'}
    assert module.warnings == []


def test_get_sysctl_multiline_values_are_joined_with_newline():
    out = 'kernel.a = 1\n continued line\nkernel.b = 2\n another continuation\n'
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, ['-a'])

    # continuation lines (starting with a space) are appended to the value;
    # the pair is flushed both mid-loop and at the end of the loop
    assert result == {
        'kernel.a': '1\n continued line',
        'kernel.b': '2\n another continuation',
    }
    assert module.warnings == []


def test_get_sysctl_unsplittable_line_warns_and_keeps_going():
    out = 'kernel.a = 1\ngarbage line without separator\nkernel.b = 2\n'
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, ['-a'])

    # the pair seen before the bad line is flushed, later lines still parse
    assert result == {'kernel.a': '1', 'kernel.b': '2'}
    assert len(module.warnings) == 1
    assert module.warnings[0].startswith('Unable to split sysctl line')
    assert 'garbage line without separator' in module.warnings[0]


def test_get_sysctl_unsplittable_first_line_yields_empty_dict():
    out = 'garbage line without separator\n'
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, [])

    assert result == {}
    assert len(module.warnings) == 1
    assert module.warnings[0].startswith('Unable to split sysctl line')
    assert 'garbage line without separator' in module.warnings[0]
    assert module.run_command_calls == [['/sbin/sysctl']]


def test_get_sysctl_empty_output_yields_empty_dict():
    module = FakeModule(run_command_result=(0, '', ''))

    result = get_sysctl(module, ['-a'])

    assert result == {}
    assert module.warnings == []


@pytest.mark.parametrize('exc', [IOError('sysctl exploded'),
                                 OSError('sysctl exploded')])
def test_get_sysctl_run_command_exception_warns_and_returns_empty(exc):
    module = FakeModule(run_command_exc=exc)

    result = get_sysctl(module, ['-a'])

    assert result == {}
    assert len(module.warnings) == 1
    assert module.warnings[0].startswith('Unable to read sysctl:')
    assert 'sysctl exploded' in module.warnings[0]
    # run_command was still attempted with the fully assembled command
    assert module.run_command_calls == [['/sbin/sysctl', '-a']]


def test_get_sysctl_nonzero_rc_returns_empty_dict():
    module = FakeModule(run_command_result=(1, 'kernel.a = 1\n', 'boom'))

    result = get_sysctl(module, ['-a'])

    assert result == {}
    assert module.warnings == []

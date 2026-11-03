# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

import pytest

from ansible.module_utils.facts.sysctl import get_sysctl


class FakeModule:
    """Minimal fake AnsibleModule: records calls and returns canned results.

    The fake is injected into get_sysctl(), so nothing global is patched
    and no cleanup/undo is necessary; instances are garbage collected
    when each test finishes, avoiding any state pollution.
    """

    def __init__(self, run_command_result=None, run_command_exc=None):
        self.run_command_result = run_command_result
        self.run_command_exc = run_command_exc
        self.warnings = []
        self.bin_path_args = []
        self.run_command_args = []

    def get_bin_path(self, name):
        self.bin_path_args.append(name)
        return '/sbin/sysctl'

    def run_command(self, cmd):
        self.run_command_args.append(list(cmd))
        if self.run_command_exc is not None:
            raise self.run_command_exc
        return self.run_command_result

    def warn(self, message):
        self.warnings.append(message)


def test_get_sysctl_basic_parses_keys_and_values():
    out = 'kernel.hostname = myhost\nkernel.osrelease: 1.2.3\n'
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, ['-n', '-a'])

    assert result == {'kernel.hostname': 'myhost', 'kernel.osrelease': '1.2.3'}
    assert module.bin_path_args == ['sysctl']
    assert module.run_command_args == [['/sbin/sysctl', '-n', '-a']]
    assert module.warnings == []


def test_get_sysctl_value_containing_equals_sign():
    out = 'kernel.cmdline = BOOT_IMAGE=/vmlinuz root=/dev/sda1\n'
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, [])

    assert result == {'kernel.cmdline': 'BOOT_IMAGE=/vmlinuz root=/dev/sda1'}
    assert module.warnings == []


def test_get_sysctl_multiline_value_appended_with_newline():
    out = 'kernel.some = first\n continued line\nkernel.other = second\n'
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, [])

    assert result == {
        'kernel.some': 'first\n continued line',
        'kernel.other': 'second',
    }
    assert module.warnings == []


def test_get_sysctl_blank_lines_are_skipped():
    out = '\n   \nkernel.hostname = myhost\n\n'
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, [])

    assert result == {'kernel.hostname': 'myhost'}
    assert module.warnings == []


def test_get_sysctl_unsplittable_line_warns_and_keeps_previous_key():
    out = 'kernel.hostname = myhost\nnoseparator\n'
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, [])

    assert result == {'kernel.hostname': 'myhost'}
    assert len(module.warnings) == 1
    assert 'Unable to split sysctl line (noseparator)' in module.warnings[0]


def test_get_sysctl_unsplittable_first_line_yields_empty_dict():
    out = 'noseparator\n'
    module = FakeModule(run_command_result=(0, out, ''))

    result = get_sysctl(module, [])

    assert result == {}
    assert len(module.warnings) == 1
    assert 'Unable to split sysctl line (noseparator)' in module.warnings[0]


def test_get_sysctl_nonzero_rc_returns_empty_dict():
    module = FakeModule(run_command_result=(1, 'ignored output', 'some error'))

    result = get_sysctl(module, ['-a'])

    assert result == {}
    assert module.warnings == []


def test_get_sysctl_empty_output_returns_empty_dict():
    module = FakeModule(run_command_result=(0, '', ''))

    result = get_sysctl(module, [])

    assert result == {}
    assert module.warnings == []


@pytest.mark.parametrize('exc', [
    IOError('broken pipe'),
    OSError(2, 'No such file or directory'),
])
def test_get_sysctl_run_command_raises_warns_and_returns_empty_dict(exc):
    module = FakeModule(run_command_exc=exc)

    result = get_sysctl(module, ['-a'])

    assert result == {}
    assert len(module.warnings) == 1
    assert module.warnings[0].startswith('Unable to read sysctl: ')
    assert str(exc) in module.warnings[0]

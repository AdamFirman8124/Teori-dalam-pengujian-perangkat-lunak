# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

import pytest

from ansible.module_utils.facts.sysctl import get_sysctl


class FakeModule(object):
    """Minimal stand-in for an Ansible module object.

    It does not touch any global state, so no teardown/monkeypatching
    is required; a fresh instance is created inside every test.
    """

    def __init__(self, run_command_result=None, run_command_raises=None):
        self.warnings = []
        self.last_cmd = None
        self._run_command_result = (0, '', '') if run_command_result is None else run_command_result
        self._run_command_raises = run_command_raises

    def get_bin_path(self, name):
        return '/sbin/%s' % name

    def run_command(self, cmd):
        self.last_cmd = list(cmd)
        if self._run_command_raises is not None:
            raise self._run_command_raises
        return self._run_command_result

    def warn(self, message):
        self.warnings.append(message)


def test_get_sysctl_basic():
    out = 'kernel.hostname = myhost\nkernel.ostype = Linux\n'
    module = FakeModule(run_command_result=(0, out, ''))
    result = get_sysctl(module, ['kernel.hostname', 'kernel.ostype'])

    assert module.last_cmd == ['/sbin/sysctl', 'kernel.hostname', 'kernel.ostype']
    assert result == {'kernel.hostname': 'myhost', 'kernel.ostype': 'Linux'}
    assert module.warnings == []


def test_get_sysctl_colon_separator():
    out = 'kernel.ostype: Linux\nkernel.osrelease: 4.19\n'
    module = FakeModule(run_command_result=(0, out, ''))
    result = get_sysctl(module, ['kernel.ostype', 'kernel.osrelease'])

    assert result == {'kernel.ostype': 'Linux', 'kernel.osrelease': '4.19'}
    assert module.warnings == []


def test_get_sysctl_multiline_value():
    # Covers multiline handling (lines starting with a space), the flush of
    # the previous pair when a new key appears and the final flush.
    out = (
        'kernel.some = first\n'
        '  continued line 1\n'
        '  continued line 2\n'
        'kernel.other = second\n'
        '  tail continuation\n'
    )
    module = FakeModule(run_command_result=(0, out, ''))
    result = get_sysctl(module, ['kernel.some', 'kernel.other'])

    assert result == {
        'kernel.some': 'first\n  continued line 1\n  continued line 2',
        'kernel.other': 'second\n  tail continuation',
    }
    assert module.warnings == []


def test_get_sysctl_skips_blank_lines():
    out = '\n   \n\t\nkernel.hostname = myhost\n\n'
    module = FakeModule(run_command_result=(0, out, ''))
    result = get_sysctl(module, ['kernel.hostname'])

    assert result == {'kernel.hostname': 'myhost'}
    assert module.warnings == []


def test_get_sysctl_empty_output():
    module = FakeModule(run_command_result=(0, '', ''))
    result = get_sysctl(module, ['-a'])

    assert result == {}
    assert module.warnings == []


def test_get_sysctl_unparsable_line_warns():
    # The unparsable line makes re.split fail (warn path) while the
    # previously parsed pair is flushed and parsing continues.
    out = (
        'kernel.good = value\n'
        'this line cannot be split\n'
        'kernel.good2 = value2\n'
    )
    module = FakeModule(run_command_result=(0, out, ''))
    result = get_sysctl(module, ['kernel.good'])

    assert len(module.warnings) == 1
    assert 'Unable to split sysctl line' in module.warnings[0]
    assert 'this line cannot be split' in module.warnings[0]
    assert result == {'kernel.good': 'value', 'kernel.good2': 'value2'}


def test_get_sysctl_only_unparsable_lines():
    # Nothing can ever be flushed since key stays empty.
    out = 'this line cannot be split\n'
    module = FakeModule(run_command_result=(0, out, ''))
    result = get_sysctl(module, ['this'])

    assert result == {}
    assert len(module.warnings) == 1
    assert 'Unable to split sysctl line' in module.warnings[0]


def test_get_sysctl_nonzero_rc_returns_empty_dict():
    module = FakeModule(run_command_result=(1, 'ignored output', 'boom'))
    result = get_sysctl(module, ['-a'])

    assert module.last_cmd == ['/sbin/sysctl', '-a']
    assert result == {}
    assert module.warnings == []


def test_get_sysctl_run_command_oserror():
    # run_command raising an OSError/IOError must warn and yield an empty dict.
    module = FakeModule(run_command_raises=OSError('no sysctl binary'))
    result = get_sysctl(module, ['-a'])

    assert result == {}
    assert len(module.warnings) == 1
    assert 'Unable to read sysctl' in module.warnings[0]
    assert 'no sysctl binary' in module.warnings[0]

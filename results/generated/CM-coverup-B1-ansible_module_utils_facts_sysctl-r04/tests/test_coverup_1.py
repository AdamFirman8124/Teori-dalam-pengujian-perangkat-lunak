# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

from unittest.mock import MagicMock

import pytest

from ansible.module_utils.facts.sysctl import get_sysctl


def _make_module(rc=0, out='', err='', side_effect=None):
    module = MagicMock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    if side_effect is not None:
        module.run_command.side_effect = side_effect
    else:
        module.run_command.return_value = (rc, out, err)
    return module


def test_get_sysctl_parses_simple_values():
    out = (
        'kernel.hostname = testhost\n'
        'net.ipv4.ip_forward: 1\n'
    )
    module = _make_module(rc=0, out=out)

    result = get_sysctl(module, ['kernel', 'net'])

    assert result == {
        'kernel.hostname': 'testhost',
        'net.ipv4.ip_forward': '1',
    }
    module.get_bin_path.assert_called_once_with('sysctl')
    module.run_command.assert_called_once_with(['/sbin/sysctl', 'kernel', 'net'])
    module.warn.assert_not_called()


def test_get_sysctl_skips_blank_lines_and_strips_values():
    out = (
        '\n'
        '   \n'
        'vm.swappiness = 60   \n'
        '\n'
    )
    module = _make_module(rc=0, out=out)

    result = get_sysctl(module, ['vm'])

    assert result == {'vm.swappiness': '60'}
    module.warn.assert_not_called()


def test_get_sysctl_handles_multiline_values():
    out = (
        'kernel.modprobe = /sbin/modprobe\n'
        '  continuation one\n'
        '  continuation two\n'
        'kernel.domainname = (none)\n'
    )
    module = _make_module(rc=0, out=out)

    result = get_sysctl(module, ['kernel'])

    assert result == {
        'kernel.modprobe': '/sbin/modprobe\n  continuation one\n  continuation two',
        'kernel.domainname': '(none)',
    }
    module.warn.assert_not_called()


def test_get_sysctl_multiline_value_at_end_of_output():
    out = (
        'kernel.modprobe = /sbin/modprobe\n'
        '  trailing continuation\n'
    )
    module = _make_module(rc=0, out=out)

    result = get_sysctl(module, ['kernel'])

    assert result == {'kernel.modprobe': '/sbin/modprobe\n  trailing continuation'}
    module.warn.assert_not_called()


def test_get_sysctl_warns_on_unparsable_line():
    out = (
        'kernel.hostname = testhost\n'
        'this-line-has-no-separator\n'
    )
    module = _make_module(rc=0, out=out)

    result = get_sysctl(module, ['kernel'])

    # The previous key/value pair is retained and re-stored.
    assert result == {'kernel.hostname': 'testhost'}
    assert module.warn.call_count == 1
    warn_msg = module.warn.call_args[0][0]
    assert warn_msg.startswith('Unable to split sysctl line (this-line-has-no-separator):')


def test_get_sysctl_returns_empty_dict_on_nonzero_rc():
    module = _make_module(rc=1, out='kernel.hostname = testhost\n', err='boom')

    result = get_sysctl(module, ['kernel'])

    assert result == {}
    module.warn.assert_not_called()


def test_get_sysctl_returns_empty_dict_on_empty_output():
    module = _make_module(rc=0, out='')

    result = get_sysctl(module, ['kernel'])

    assert result == {}
    module.warn.assert_not_called()


@pytest.mark.parametrize('exc', [IOError('io failure'), OSError('os failure')])
def test_get_sysctl_warns_when_run_command_raises(exc):
    module = _make_module(side_effect=exc)

    result = get_sysctl(module, ['kernel'])

    assert result == {}
    assert module.warn.call_count == 1
    warn_msg = module.warn.call_args[0][0]
    assert warn_msg.startswith('Unable to read sysctl: ')
    assert str(exc) in warn_msg

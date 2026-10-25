# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

import re
from unittest.mock import MagicMock
from ansible.module_utils.facts.sysctl import get_sysctl


def _make_module(out="", rc=0, err="", bin_path="/sbin/sysctl", side_effect=None):
    module = MagicMock()
    module.get_bin_path.return_value = bin_path
    if side_effect is not None:
        module.run_command.side_effect = side_effect
    else:
        module.run_command.return_value = (rc, out, err)
    return module


def test_get_sysctl_parses_equals_and_blank_lines():
    out = "vm.swappiness = 60\n\n   \nnet.ipv4.ip_forward = 1\n"
    module = _make_module(out=out)
    prefixes = ["vm.swappiness", "net.ipv4.ip_forward"]
    result = get_sysctl(module, prefixes)
    assert result == {"vm.swappiness": "60", "net.ipv4.ip_forward": "1"}
    module.get_bin_path.assert_called_once_with("sysctl")
    module.run_command.assert_called_once_with(["/sbin/sysctl"] + prefixes)
    # blank lines are skipped, no warnings
    assert module.warn.call_count == 0


def test_get_sysctl_colon_separator_and_multiline():
    out = "kern.msgbuf: first line\n second line continued\nkern.other = secondvalue"
    module = _make_module(out=out)
    result = get_sysctl(module, ["kern.msgbuf", "kern.other"])
    assert result == {
        "kern.msgbuf": "first line\n second line continued",
        "kern.other": "secondvalue",
    }
    # multiline value preserves newline
    assert "\n" in result["kern.msgbuf"]
    assert result["kern.msgbuf"].endswith("second line continued")


def test_get_sysctl_warn_on_unparsable_line():
    out = "good.key = goodvalue\nbadlinewithoutseparator\nanother.key = anothervalue"
    module = _make_module(out=out)
    result = get_sysctl(module, ["good.key"])
    assert result == {"good.key": "goodvalue", "another.key": "anothervalue"}
    assert module.warn.call_count == 1
    args, _ = module.warn.call_args
    assert "badlinewithoutseparator" in args[0]
    assert "Unable to split sysctl line" in args[0]


def test_get_sysctl_handles_ioerror():
    module = _make_module(side_effect=IOError("disk fail"))
    result = get_sysctl(module, ["vm.swappiness"])
    assert result == {}
    assert module.warn.call_count == 1
    args, _ = module.warn.call_args
    assert "Unable to read sysctl" in args[0]
    module.get_bin_path.assert_called_once_with("sysctl")
    module.run_command.assert_called_once()


def test_get_sysctl_handles_oserror():
    module = _make_module(side_effect=OSError("os fail"))
    result = get_sysctl(module, [])
    assert result == {}
    assert module.warn.call_count == 1
    args, _ = module.warn.call_args
    assert "Unable to read sysctl" in args[0]


def test_get_sysctl_nonzero_rc_returns_empty():
    module = _make_module(out="vm.swappiness = 60", rc=1, err="error")
    result = get_sysctl(module, ["vm.swappiness"])
    assert result == {}
    assert module.warn.call_count == 0


def test_get_sysctl_empty_output_returns_empty():
    module = _make_module(out="", rc=0)
    result = get_sysctl(module, [])
    assert result == {}
    assert module.warn.call_count == 0


def test_get_sysctl_only_blank_lines_returns_empty():
    module = _make_module(out="\n   \n\n", rc=0)
    result = get_sysctl(module, [])
    assert result == {}

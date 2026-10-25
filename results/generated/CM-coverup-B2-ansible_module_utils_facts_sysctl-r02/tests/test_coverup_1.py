# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

from unittest.mock import Mock

import pytest

from ansible.module_utils.facts.sysctl import get_sysctl


def test_get_sysctl_parses_values_multiline_output_and_warns_on_bad_line():
    module = Mock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.return_value = (
        0,
        "\n"
        "net.ipv4.conf.all.forwarding = 1\n"
        " continued value\n"
        "kernel.hostname: test-host\n"
        "invalid line\n",
        "",
    )

    result = get_sysctl(
        module,
        ["net.ipv4.conf.all.forwarding", "kernel.hostname"],
    )

    assert result == {
        "net.ipv4.conf.all.forwarding": "1\n continued value",
        "kernel.hostname": "test-host",
    }
    module.get_bin_path.assert_called_once_with("sysctl")
    module.run_command.assert_called_once_with(
        [
            "/sbin/sysctl",
            "net.ipv4.conf.all.forwarding",
            "kernel.hostname",
        ]
    )
    module.warn.assert_called_once()
    assert "Unable to split sysctl line (invalid line):" in module.warn.call_args.args[0]


def test_get_sysctl_success_with_no_parseable_keys():
    module = Mock()
    module.get_bin_path.return_value = "/usr/sbin/sysctl"
    module.run_command.return_value = (0, "\n   \ninvalid line\n", "")

    result = get_sysctl(module, [])

    assert result == {}
    module.run_command.assert_called_once_with(["/usr/sbin/sysctl"])
    module.warn.assert_called_once()
    assert "Unable to split sysctl line (invalid line):" in module.warn.call_args.args[0]


def test_get_sysctl_returns_empty_mapping_when_command_fails():
    module = Mock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.return_value = (1, "ignored = value", "failure")

    result = get_sysctl(module, ["ignored"])

    assert result == {}
    module.run_command.assert_called_once_with(["/sbin/sysctl", "ignored"])
    module.warn.assert_not_called()


@pytest.mark.parametrize("exception_type", [IOError, OSError])
def test_get_sysctl_warns_and_returns_empty_mapping_on_os_error(exception_type):
    module = Mock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.side_effect = exception_type("permission denied")

    result = get_sysctl(module, ["kernel.hostname"])

    assert result == {}
    module.run_command.assert_called_once_with(
        ["/sbin/sysctl", "kernel.hostname"]
    )
    module.warn.assert_called_once_with(
        "Unable to read sysctl: permission denied"
    )

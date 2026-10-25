# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

from unittest.mock import Mock

from ansible.module_utils.facts.sysctl import get_sysctl


def test_get_sysctl_parses_values_continuations_and_warns_on_malformed_line():
    module = Mock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.return_value = (
        0,
        "\n"
        " orphaned continuation\n"
        "kernel.example = first\n"
        " second\n"
        "network.example: value\n"
        "malformed-line\n",
        "",
    )

    result = get_sysctl(module, ["kernel.example", "network.example"])

    assert result == {
        "kernel.example": "first\n second",
        "network.example": "value",
    }
    module.get_bin_path.assert_called_once_with("sysctl")
    module.run_command.assert_called_once_with(
        ["/sbin/sysctl", "kernel.example", "network.example"]
    )
    module.warn.assert_called_once()
    warning = module.warn.call_args.args[0]
    assert warning.startswith(
        "Unable to split sysctl line (malformed-line): "
    )


def test_get_sysctl_returns_empty_mapping_when_command_fails():
    module = Mock()
    module.get_bin_path.return_value = "/usr/sbin/sysctl"
    module.run_command.return_value = (1, "ignored output", "permission denied")

    result = get_sysctl(module, [])

    assert result == {}
    module.get_bin_path.assert_called_once_with("sysctl")
    module.run_command.assert_called_once_with(["/usr/sbin/sysctl"])
    module.warn.assert_not_called()


def test_get_sysctl_warns_and_returns_empty_mapping_on_os_error():
    module = Mock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.side_effect = OSError("access denied")

    result = get_sysctl(module, ["vm"])

    assert result == {}
    module.get_bin_path.assert_called_once_with("sysctl")
    module.run_command.assert_called_once_with(["/sbin/sysctl", "vm"])
    module.warn.assert_called_once_with(
        "Unable to read sysctl: access denied"
    )


def test_get_sysctl_handles_output_without_any_key():
    module = Mock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.return_value = (
        0,
        "\n continuation without a key\n\n",
        "",
    )

    result = get_sysctl(module, ["missing"])

    assert result == {}
    module.get_bin_path.assert_called_once_with("sysctl")
    module.run_command.assert_called_once_with(["/sbin/sysctl", "missing"])
    module.warn.assert_not_called()

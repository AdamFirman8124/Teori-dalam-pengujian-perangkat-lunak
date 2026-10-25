# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

from unittest.mock import MagicMock

from ansible.module_utils.facts.sysctl import get_sysctl


def test_get_sysctl_parses_values_multiline_output_and_warns_on_invalid_line():
    module = MagicMock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.return_value = (
        0,
        "\n"
        "net.ipv4.ip_forward = 1\n"
        " continuation\n"
        "\n"
        "kernel.hostname: test-host\n"
        "malformed line\n",
        "",
    )

    result = get_sysctl(module, ["net.ipv4", "kernel"])

    assert result == {
        "net.ipv4.ip_forward": "1\n continuation",
        "kernel.hostname": "test-host",
    }
    module.get_bin_path.assert_called_once_with("sysctl")
    module.run_command.assert_called_once_with(
        ["/sbin/sysctl", "net.ipv4", "kernel"]
    )
    module.warn.assert_called_once()
    warning = module.warn.call_args.args[0]
    assert warning.startswith("Unable to split sysctl line (malformed line):")


def test_get_sysctl_returns_empty_dict_for_empty_successful_output():
    module = MagicMock()
    module.get_bin_path.return_value = "/usr/sbin/sysctl"
    module.run_command.return_value = (0, "", "")

    result = get_sysctl(module, [])

    assert result == {}
    module.get_bin_path.assert_called_once_with("sysctl")
    module.run_command.assert_called_once_with(["/usr/sbin/sysctl"])
    module.warn.assert_not_called()


def test_get_sysctl_returns_empty_dict_when_command_fails():
    module = MagicMock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.return_value = (1, "", "command failed")

    result = get_sysctl(module, ["vm"])

    assert result == {}
    module.run_command.assert_called_once_with(["/sbin/sysctl", "vm"])
    module.warn.assert_not_called()


def test_get_sysctl_warns_and_returns_empty_dict_on_oserror():
    module = MagicMock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.side_effect = OSError("permission denied")

    result = get_sysctl(module, ["kernel"])

    assert result == {}
    module.run_command.assert_called_once_with(["/sbin/sysctl", "kernel"])
    module.warn.assert_called_once_with(
        "Unable to read sysctl: permission denied"
    )

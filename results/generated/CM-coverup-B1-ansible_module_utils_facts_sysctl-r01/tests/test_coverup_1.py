# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

from unittest.mock import Mock, call

from ansible.module_utils.facts.sysctl import get_sysctl


def test_get_sysctl_parses_values_multiline_values_and_blank_lines():
    module = Mock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.return_value = (
        0,
        "\n"
        "net.ipv4.conf.all.forwarding = 1\n"
        " continued value\n"
        "\n"
        "kernel.domainname: example.test\n",
        "",
    )

    result = get_sysctl(
        module,
        ["net.ipv4.conf.all.forwarding", "kernel.domainname"],
    )

    assert result == {
        "net.ipv4.conf.all.forwarding": "1\n continued value",
        "kernel.domainname": "example.test",
    }
    module.get_bin_path.assert_called_once_with("sysctl")
    module.run_command.assert_called_once_with(
        [
            "/sbin/sysctl",
            "net.ipv4.conf.all.forwarding",
            "kernel.domainname",
        ]
    )
    module.warn.assert_not_called()


def test_get_sysctl_returns_empty_dict_when_command_fails():
    module = Mock()
    module.get_bin_path.return_value = "/usr/sbin/sysctl"
    module.run_command.return_value = (1, "ignored = value", "failure")

    result = get_sysctl(module, [])

    assert result == {}
    module.get_bin_path.assert_called_once_with("sysctl")
    module.run_command.assert_called_once_with(["/usr/sbin/sysctl"])
    module.warn.assert_not_called()


def test_get_sysctl_warns_and_returns_empty_dict_on_os_error():
    module = Mock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.side_effect = OSError("permission denied")

    result = get_sysctl(module, ["kernel.hostname"])

    assert result == {}
    module.run_command.assert_called_once_with(
        ["/sbin/sysctl", "kernel.hostname"]
    )
    module.warn.assert_called_once_with(
        "Unable to read sysctl: permission denied"
    )


def test_get_sysctl_warns_when_a_line_cannot_be_split():
    module = Mock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.return_value = (0, "malformed line", "")

    result = get_sysctl(module, ["malformed"])

    assert result == {}
    module.run_command.assert_called_once_with(
        ["/sbin/sysctl", "malformed"]
    )
    module.warn.assert_called_once()
    warning = module.warn.call_args.args[0]
    assert warning.startswith(
        "Unable to split sysctl line (malformed line): "
    )


def test_get_sysctl_preserves_previous_value_after_malformed_line():
    module = Mock()
    module.get_bin_path.return_value = "/sbin/sysctl"
    module.run_command.return_value = (
        0,
        "valid.key = valid value\nmalformed line",
        "",
    )

    result = get_sysctl(module, ["valid.key"])

    assert result == {"valid.key": "valid value"}
    assert module.warn.call_count == 1
    assert module.warn.call_args_list[0] == call(
        module.warn.call_args.args[0]
    )
    assert module.warn.call_args.args[0].startswith(
        "Unable to split sysctl line (malformed line): "
    )

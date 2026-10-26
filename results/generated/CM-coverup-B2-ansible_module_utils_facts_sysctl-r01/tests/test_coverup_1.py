# file: project/ansible/module_utils/facts/sysctl.py:24-62
# asked: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}
# gained: {"lines": [25, 26, 27, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 62], "branches": [[37, 38], [37, 62], [40, 41], [40, 59], [41, 42], [41, 44], [44, 48], [44, 51], [51, 52], [51, 54], [59, 60], [59, 62]]}

from ansible.module_utils.facts.sysctl import get_sysctl


class _FakeModule:
    def __init__(self, bin_path="/sbin/sysctl", result=(0, "", "")):
        self._bin_path = bin_path
        self._result = result
        self.cmd_seen = None
        self.warnings = []

    def get_bin_path(self, name):
        assert name == "sysctl"
        return self._bin_path

    def run_command(self, cmd):
        self.cmd_seen = cmd
        if isinstance(self._result, BaseException):
            raise self._result
        return self._result

    def warn(self, msg):
        self.warnings.append(msg)


def test_get_sysctl_simple_equals():
    module = _FakeModule(result=(0, "a = b\nc=d\n", ""))
    result = get_sysctl(module, ["a", "c"])
    assert result == {"a": "b", "c": "d"}
    assert module.cmd_seen == ["/sbin/sysctl", "a", "c"]
    assert module.warnings == []


def test_get_sysctl_colon_separator():
    module = _FakeModule(result=(0, "net.ipv4.ip_forward: 1\n", ""))
    result = get_sysctl(module, ["net.ipv4.ip_forward"])
    assert result == {"net.ipv4.ip_forward": "1"}
    assert module.cmd_seen == ["/sbin/sysctl", "net.ipv4.ip_forward"]


def test_get_sysctl_multiline_and_blank_lines():
    out = "key1 = line1\n continued line\n\nkey2 = val2\n"
    module = _FakeModule(result=(0, out, ""))
    result = get_sysctl(module, ["key1", "key2"])
    assert result == {"key1": "line1\n continued line", "key2": "val2"}
    assert module.cmd_seen == ["/sbin/sysctl", "key1", "key2"]


def test_get_sysctl_unparsable_line_warns():
    out = "good = value\nbadlinewithoutseparator\nnext = ok"
    module = _FakeModule(result=(0, out, ""))
    result = get_sysctl(module, ["good"])
    assert result == {"good": "value", "next": "ok"}
    assert len(module.warnings) == 1
    assert "badlinewithoutseparator" in module.warnings[0]


def test_get_sysctl_nonzero_rc_returns_empty():
    module = _FakeModule(result=(1, "a = b", "error"))
    result = get_sysctl(module, ["a"])
    assert result == {}
    assert module.cmd_seen == ["/sbin/sysctl", "a"]
    assert module.warnings == []


def test_get_sysctl_ioerror_returns_empty_and_warns():
    module = _FakeModule(result=IOError("no sysctl"))
    result = get_sysctl(module, ["a"])
    assert result == {}
    assert len(module.warnings) == 1
    assert "Unable to read sysctl" in module.warnings[0]


def test_get_sysctl_oserror_returns_empty_and_warns():
    module = _FakeModule(result=OSError("perm denied"))
    result = get_sysctl(module, [])
    assert result == {}
    assert module.cmd_seen == ["/sbin/sysctl"]
    assert len(module.warnings) == 1
    assert "Unable to read sysctl" in module.warnings[0]


def test_get_sysctl_empty_output_returns_empty():
    module = _FakeModule(result=(0, "", ""))
    result = get_sysctl(module, [])
    assert result == {}
    assert module.cmd_seen == ["/sbin/sysctl"]
    assert module.warnings == []

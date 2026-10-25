# file: project/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_init_parses_truthy_version_string():
    version = LooseVersion("1.2a3")

    assert version.vstring == "1.2a3"
    assert version.version == [1, 2, "a", 3]
    assert str(version) == "1.2a3"


def test_loose_version_init_skips_parsing_without_version_string(monkeypatch):
    parse_calls = []

    def record_parse(self, vstring):
        parse_calls.append((self, vstring))

    monkeypatch.setattr(LooseVersion, "parse", record_parse)

    version = LooseVersion()

    assert parse_calls == []
    assert version.__dict__ == {}

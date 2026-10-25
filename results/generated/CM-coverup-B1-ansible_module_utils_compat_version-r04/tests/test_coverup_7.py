# file: project/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_init_parses_truthy_vstring(monkeypatch):
    parsed = []

    def fake_parse(self, vstring):
        parsed.append((self, vstring))
        self.parsed_vstring = vstring

    monkeypatch.setattr(LooseVersion, "parse", fake_parse)

    version = LooseVersion("1.5.2b2")

    assert parsed == [(version, "1.5.2b2")]
    assert version.parsed_vstring == "1.5.2b2"


def test_loose_version_init_skips_parse_for_falsy_vstrings(monkeypatch):
    def unexpected_parse(self, vstring):
        raise AssertionError("parse() must not be called for a falsy vstring")

    monkeypatch.setattr(LooseVersion, "parse", unexpected_parse)

    for vstring in (None, ""):
        version = LooseVersion(vstring)
        assert vars(version) == {}

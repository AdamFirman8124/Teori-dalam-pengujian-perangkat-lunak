# file: project/ansible/plugins/lookup/ini.py:136-204
# asked: {"lines": [138, 139, 141, 142, 143, 145, 146, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 163, 164, 165, 167, 168, 169, 174, 177, 179, 180, 181, 184, 185, 186, 187, 189, 190, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 203, 204], "branches": [[142, 143], [142, 145], [146, 148], [146, 204], [150, 151], [150, 174], [155, 156], [155, 168], [156, 157], [156, 161], [158, 159], [158, 160], [161, 155], [161, 163], [168, 169], [168, 174], [179, 180], [179, 184], [198, 146], [198, 199], [199, 200], [199, 203], [200, 146], [200, 201]]}
# gained: {"lines": [138, 139, 141, 142, 143, 145, 146, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 163, 164, 165, 167, 168, 169, 174, 177, 179, 180, 181, 184, 185, 186, 187, 189, 190, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 203, 204], "branches": [[142, 143], [142, 145], [146, 148], [146, 204], [150, 151], [150, 174], [155, 156], [155, 168], [156, 157], [156, 161], [158, 159], [158, 160], [161, 155], [161, 163], [168, 169], [168, 174], [179, 180], [179, 184], [198, 146], [198, 199], [199, 200], [199, 203], [200, 146], [200, 201]]}

import pytest
from unittest.mock import MagicMock
from ansible.errors import AnsibleLookupError, AnsibleOptionsError
from ansible.module_utils._text import to_native
import ansible.plugins.lookup.ini as ini_module
from ansible.plugins.lookup.ini import LookupModule


def _base_paramvals(**overrides):
    vals = {
        'allow_no_value': False,
        'allow_none': False,
        'case_sensitive': False,
        'file': 'test.ini',
        'type': 'ini',
        'section': 'global',
        'encoding': 'utf-8',
        'default': '',
        're': False,
    }
    vals.update(overrides)
    return vals


def _ensure_readfp(monkeypatch):
    CP = ini_module.configparser.ConfigParser
    if not hasattr(CP, 'readfp'):
        def readfp(self, fp, filename=None):
            if filename is not None:
                return self.read_file(fp, source=filename)
            return self.read_file(fp)
        monkeypatch.setattr(CP, 'readfp', readfp, raising=False)


def _wire_common(monkeypatch, lookup, paramvals, file_bytes):
    _ensure_readfp(monkeypatch)
    monkeypatch.setattr(lookup, "set_options", lambda var_options=None, direct=None: None)
    monkeypatch.setattr(lookup, "get_options", lambda: paramvals)
    monkeypatch.setattr(
        lookup, "find_file_in_search_path",
        lambda variables, subdir, file: "/fake/test.ini",
    )
    monkeypatch.setattr(lookup, "_deprecate_inline_kv", lambda: None)
    fake_loader = MagicMock()
    fake_loader._get_file_contents.return_value = (file_bytes, False)
    lookup._loader = fake_loader
    lookup.loader = fake_loader
    return fake_loader


def test_plain_key_string_value(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals()
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nmykey=myvalue\n")
    ret = lookup.run(["mykey"], variables={})
    assert ret == ["myvalue"]


def test_case_sensitive_properties_list_value(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals(case_sensitive=True, type="properties", allow_no_value=True)
    _wire_common(monkeypatch, lookup, paramvals, b"mykey=myvalue\n")
    monkeypatch.setattr(lookup, "get_value", lambda key, section, dflt, is_regexp: ["a", "b"])
    ret = lookup.run(["mykey"], variables={})
    assert ret == ["a", "b"]
    assert paramvals["section"] == "java_properties"
    assert lookup.cp.optionxform == to_native


def test_var_none_returns_empty(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals()
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nmykey=myvalue\n")
    monkeypatch.setattr(lookup, "get_value", lambda key, section, dflt, is_regexp: None)
    ret = lookup.run(["missing"], variables={})
    assert ret == []


def test_multiple_plain_terms(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals()
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nmykey=myvalue\n")
    calls = []
    def _gv(key, section, dflt, is_regexp):
        calls.append(key)
        return "v-" + key
    monkeypatch.setattr(lookup, "get_value", _gv)
    ret = lookup.run(["k1", "k2"], variables={})
    assert ret == ["v-k1", "v-k2"]
    assert calls == ["k1", "k2"]


def test_inline_space_key_plus_option(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals()
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nmykey=myvalue\n")
    monkeypatch.setattr(
        ini_module, "_parse_params", lambda term, pv: ["mykey", "section=mysection"]
    )
    captured = {}
    def _gv(key, section, dflt, is_regexp):
        captured["key"] = key
        captured["section"] = section
        return "v"
    monkeypatch.setattr(lookup, "get_value", _gv)
    ret = lookup.run(["mykey section=mysection"], variables={})
    assert ret == ["v"]
    assert captured["key"] == "mykey"
    assert captured["section"] == "mysection"
    assert paramvals["section"] == "mysection"


def test_inline_equals_term_key_plus_option(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals()
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nmykey=myvalue\n")
    monkeypatch.setattr(
        ini_module, "_parse_params", lambda term, pv: ["mykey", "file=test.ini"]
    )
    captured = {}
    def _gv(key, section, dflt, is_regexp):
        captured["key"] = key
        return "v2"
    monkeypatch.setattr(lookup, "get_value", _gv)
    ret = lookup.run(["mykey,section=global"], variables={})
    assert ret == ["v2"]
    assert captured["key"] == "mykey"
    assert paramvals["file"] == "test.ini"


def test_inline_second_bare_param_ignored(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals()
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nmykey=myvalue\n")
    monkeypatch.setattr(
        ini_module, "_parse_params", lambda term, pv: ["realkey", "extra"]
    )
    captured = {}
    def _gv(key, section, dflt, is_regexp):
        captured["key"] = key
        return "ok"
    monkeypatch.setattr(lookup, "get_value", _gv)
    ret = lookup.run(["realkey extra"], variables={})
    assert ret == ["ok"]
    assert captured["key"] == "realkey"


def test_inline_invalid_option_raises(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals()
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nmykey=myvalue\n")
    monkeypatch.setattr(
        ini_module, "_parse_params", lambda term, pv: ["badopt=val", "mykey"]
    )
    with pytest.raises(AnsibleLookupError, match="not a valid option"):
        lookup.run(["badopt=val mykey"], variables={})


def test_inline_split_value_error_raises(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals()
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nmykey=myvalue\n")
    monkeypatch.setattr(ini_module, "_parse_params", lambda term, pv: ["a=b=c"])
    with pytest.raises(AnsibleLookupError, match="Could not use"):
        lookup.run(["a=b=c"], variables={})


def test_inline_no_key_raises_options_error(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals()
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nmykey=myvalue\n")
    monkeypatch.setattr(ini_module, "_parse_params", lambda term, pv: ["section=global"])
    with pytest.raises(AnsibleOptionsError, match="No key to lookup"):
        lookup.run(["section=global"], variables={})


def test_duplicate_option_raises(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals()
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nkey=1\nkey=2\n")
    monkeypatch.setattr(lookup, "get_value", lambda key, section, dflt, is_regexp: "x")
    with pytest.raises(AnsibleLookupError, match="Duplicate option"):
        lookup.run(["key"], variables={})


def test_no_section_raises(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals(section="missing")
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nkey=1\n")
    def _gv(key, section, dflt, is_regexp):
        raise ini_module.configparser.NoSectionError("missing")
    monkeypatch.setattr(lookup, "get_value", _gv)
    with pytest.raises(AnsibleLookupError, match="No section"):
        lookup.run(["key"], variables={})


def test_allow_none_fallback_no_value(monkeypatch):
    lookup = LookupModule()
    paramvals = _base_paramvals()
    del paramvals["allow_no_value"]
    paramvals["allow_none"] = True
    _wire_common(monkeypatch, lookup, paramvals, b"[global]\nbarekey\n")
    monkeypatch.setattr(lookup, "get_value", lambda key, section, dflt, is_regexp: "bare")
    ret = lookup.run(["barekey"], variables={})
    assert ret == ["bare"]

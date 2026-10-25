# file: project/ansible/plugins/lookup/ini.py:136-204
# asked: {"lines": [138, 139, 141, 142, 143, 145, 146, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 163, 164, 165, 167, 168, 169, 174, 177, 179, 180, 181, 184, 185, 186, 187, 189, 190, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 203, 204], "branches": [[142, 143], [142, 145], [146, 148], [146, 204], [150, 151], [150, 174], [155, 156], [155, 168], [156, 157], [156, 161], [158, 159], [158, 160], [161, 155], [161, 163], [168, 169], [168, 174], [179, 180], [179, 184], [198, 146], [198, 199], [199, 200], [199, 203], [200, 146], [200, 201]]}
# gained: {"lines": [138, 139, 141, 142, 143, 145, 146, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 163, 164, 165, 167, 168, 169, 174, 177, 179, 180, 181, 184, 185, 186, 187, 189, 190, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 203, 204], "branches": [[142, 143], [142, 145], [146, 148], [146, 204], [150, 151], [150, 174], [155, 156], [155, 168], [156, 157], [156, 161], [158, 159], [158, 160], [161, 155], [161, 163], [168, 169], [168, 174], [179, 180], [179, 184], [198, 146], [198, 199], [199, 200], [199, 203], [200, 146], [200, 201]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.lookup.ini import LookupModule
import ansible.plugins.lookup.ini as ini_module
from ansible.module_utils.six.moves import configparser
from ansible.module_utils._text import to_native
from ansible.errors import AnsibleLookupError, AnsibleOptionsError

if not hasattr(configparser.ConfigParser, "readfp"):
    configparser.ConfigParser.readfp = configparser.ConfigParser.read_file


def _base_paramvals(**over):
    d = {
        "allow_no_value": False,
        "allow_none": False,
        "case_sensitive": False,
        "file": "test.ini",
        "type": "ini",
        "section": "global",
        "encoding": "utf-8",
        "default": "",
        "re": False,
    }
    d.update(over)
    return d


def _make_lookup(paramvals, file_contents):
    lookup = LookupModule(loader=MagicMock(), templar=MagicMock())
    lookup.set_options = MagicMock()
    lookup.get_options = MagicMock(return_value=paramvals)
    lookup.find_file_in_search_path = MagicMock(return_value="/tmp/fake.ini")
    lookup._loader = MagicMock()
    lookup._loader._get_file_contents.return_value = (file_contents, True)
    lookup._deprecate_inline_kv = MagicMock()
    return lookup


def test_plain_single_value():
    paramvals = _base_paramvals()
    lookup = _make_lookup(paramvals, b"[global]\nmykey=myvalue\n")
    ret = lookup.run(["mykey"], variables={})
    assert ret == ["myvalue"]
    lookup.find_file_in_search_path.assert_called_once()
    lookup._loader._get_file_contents.assert_called_once()
    lookup._deprecate_inline_kv.assert_not_called()


def test_case_sensitive_true():
    paramvals = _base_paramvals(case_sensitive=True)
    lookup = _make_lookup(paramvals, b"[global]\nMyKey=val1\n")
    ret = lookup.run(["MyKey"], variables={})
    assert ret == ["val1"]
    assert lookup.cp.optionxform == to_native


def test_allow_no_value_key_without_value():
    paramvals = _base_paramvals(allow_no_value=True)
    lookup = _make_lookup(paramvals, b"[global]\nmykey\n")
    ret = lookup.run(["mykey"], variables={})
    assert ret == []
    assert lookup.cp._allow_no_value is True


def test_allow_none_fallback():
    paramvals = _base_paramvals()
    del paramvals["allow_no_value"]
    paramvals["allow_none"] = True
    lookup = _make_lookup(paramvals, b"[global]\nmykey\n")
    ret = lookup.run(["mykey"], variables={})
    assert ret == []
    assert lookup.cp._allow_no_value is True


def test_properties_type():
    paramvals = _base_paramvals(type="properties", section="global")
    lookup = _make_lookup(paramvals, b"mykey=myvalue\n")
    ret = lookup.run(["mykey"], variables={})
    assert ret == ["myvalue"]
    assert paramvals["section"] == "java_properties"


def test_inline_kv_valid():
    paramvals = _base_paramvals()
    lookup = _make_lookup(paramvals, b"[global]\nmykey=v\n")
    ret = lookup.run(["mykey section=global"], variables={})
    assert ret == ["v"]
    lookup._deprecate_inline_kv.assert_called_once()
    assert paramvals["section"] == "global"


def test_inline_only_options_no_key():
    paramvals = _base_paramvals()
    lookup = _make_lookup(paramvals, b"[global]\na=1\n")
    with pytest.raises(AnsibleOptionsError, match="No key to lookup"):
        lookup.run(["section=global"], variables={})


def test_inline_invalid_option():
    paramvals = _base_paramvals()
    lookup = _make_lookup(paramvals, b"[global]\na=1\n")
    with pytest.raises(AnsibleLookupError, match="not a valid option"):
        lookup.run(["mykey badkey=val"], variables={})


def test_inline_value_error():
    paramvals = _base_paramvals()
    lookup = _make_lookup(paramvals, b"[global]\na=1\n")
    with pytest.raises(AnsibleLookupError, match="Could not use"):
        lookup.run(["section=a=b=c"], variables={})


def test_inline_second_bare_ignored(monkeypatch):
    paramvals = _base_paramvals()
    lookup = _make_lookup(paramvals, b"[global]\nkey1=v1\n")
    monkeypatch.setattr(ini_module, "_parse_params", lambda term, pv: ["key1", "key2"])
    ret = lookup.run(["key1 key2"], variables={})
    assert ret == ["v1"]
    lookup._deprecate_inline_kv.assert_called_once()


def test_duplicate_option_error():
    paramvals = _base_paramvals()
    lookup = _make_lookup(paramvals, b"[global]\nkey=1\nkey=2\n")
    with pytest.raises(AnsibleLookupError, match="Duplicate option"):
        lookup.run(["key"], variables={})


def test_no_section_error():
    paramvals = _base_paramvals(section="missing")
    lookup = _make_lookup(paramvals, b"[global]\na=1\n")
    with pytest.raises(AnsibleLookupError, match="No section"):
        lookup.run(["a"], variables={})


def test_re_list_expansion():
    paramvals = _base_paramvals(section="section1", re=True)
    lookup = _make_lookup(paramvals, b"[section1]\nkey1=val1\nkey2=val2\n")
    ret = lookup.run([".*"], variables={})
    assert sorted(ret) == ["val1", "val2"]
    assert len(ret) == 2


def test_var_none_returns_empty():
    paramvals = _base_paramvals(default=None)
    lookup = _make_lookup(paramvals, b"[global]\na=1\n")
    ret = lookup.run(["missing"], variables={})
    assert ret == []


def test_multiple_terms():
    paramvals = _base_paramvals()
    lookup = _make_lookup(paramvals, b"[global]\nkey1=val1\nkey2=val2\n")
    ret = lookup.run(["key1", "key2"], variables={})
    assert ret == ["val1", "val2"]

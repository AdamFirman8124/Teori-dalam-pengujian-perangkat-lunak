# file: project/ansible/plugins/lookup/ini.py:124-134
# asked: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}

import re
from ansible.module_utils.six.moves import configparser
from ansible.plugins.lookup.ini import LookupModule


def _make_lookup():
    lookup = LookupModule()
    cp = configparser.ConfigParser()
    cp.read_string("[mysection]\nkey1 = value1\nkey2 = value2\nother = value3\n")
    lookup.cp = cp
    return lookup


def test_get_value_regexp_matching():
    lookup = _make_lookup()
    result = lookup.get_value("key.*", "mysection", "dflt", True)
    assert sorted(result) == ["value1", "value2"]


def test_get_value_regexp_no_match():
    lookup = _make_lookup()
    result = lookup.get_value("nomatch.*", "mysection", "dflt", True)
    assert result == []


def test_get_value_single_existing_key():
    lookup = _make_lookup()
    result = lookup.get_value("key1", "mysection", "dflt", False)
    assert result == "value1"


def test_get_value_missing_key_returns_default():
    lookup = _make_lookup()
    result = lookup.get_value("missing_key", "mysection", "mydefault", False)
    assert result == "mydefault"

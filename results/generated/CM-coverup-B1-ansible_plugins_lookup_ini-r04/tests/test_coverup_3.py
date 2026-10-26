# file: project/ansible/plugins/lookup/ini.py:124-134
# asked: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}

import re

import pytest
from ansible.module_utils.six.moves import configparser

from ansible.plugins.lookup.ini import LookupModule


@pytest.fixture
def ini_lookup():
    lookup = LookupModule()
    cp = configparser.ConfigParser()
    cp.read_dict(
        {
            "section": {
                "key1": "value1",
                "key2": "value2",
                "other": "other_value",
            }
        }
    )
    lookup.cp = cp
    yield lookup
    del lookup.cp


def test_get_value_regexp_returns_only_matching_values(ini_lookup):
    result = ini_lookup.get_value(r"key\d", "section", "default", True)

    assert result == ["value1", "value2"]
    assert "other_value" not in result


def test_get_value_regexp_with_no_matches_returns_empty_list(ini_lookup):
    result = ini_lookup.get_value(r"missing\d+", "section", "default", True)

    assert result == []


def test_get_value_regexp_matches_from_start_of_key(ini_lookup):
    result = ini_lookup.get_value(r"key", "section", None, True)

    assert result == ["value1", "value2"]
    # Verify the same pattern semantics used by the implementation.
    assert all(re.match(r"key", key) for key in ("key1", "key2"))


def test_get_value_single_existing_key_returns_value(ini_lookup):
    result = ini_lookup.get_value("key1", "section", "default", False)

    assert result == "value1"


def test_get_value_single_other_key_returns_value(ini_lookup):
    result = ini_lookup.get_value("other", "section", "default", False)

    assert result == "other_value"


def test_get_value_missing_option_returns_default(ini_lookup):
    result = ini_lookup.get_value("missing", "section", "fallback", False)

    assert result == "fallback"


def test_get_value_missing_option_returns_none_default(ini_lookup):
    result = ini_lookup.get_value("missing", "section", None, False)

    assert result is None

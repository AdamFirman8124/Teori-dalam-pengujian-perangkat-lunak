# file: project/ansible/plugins/lookup/ini.py:124-134
# asked: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}

from ansible.module_utils.six.moves import configparser
from ansible.plugins.lookup.ini import LookupModule


def _lookup_with_config(options):
    parser = configparser.ConfigParser()
    parser.add_section("example")
    for key, value in options.items():
        parser.set("example", key, value)

    lookup = object.__new__(LookupModule)
    lookup.cp = parser
    return lookup


def test_get_value_returns_all_values_matching_regexp():
    lookup = _lookup_with_config(
        {
            "db_1": "primary",
            "db_2": "replica",
            "cache_1": "redis",
        }
    )

    result = lookup.get_value(r"^db_\d+$", "example", "unused", True)

    assert result == ["primary", "replica"]


def test_get_value_returns_single_existing_value():
    lookup = _lookup_with_config({"username": "alice"})

    result = lookup.get_value("username", "example", "fallback", False)

    assert result == "alice"


def test_get_value_returns_default_when_option_is_missing():
    lookup = _lookup_with_config({"username": "alice"})
    default = object()

    result = lookup.get_value("missing", "example", default, False)

    assert result is default

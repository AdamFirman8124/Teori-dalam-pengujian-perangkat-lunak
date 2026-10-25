# file: project/ansible/plugins/lookup/ini.py:124-134
# asked: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}

from ansible.module_utils.six.moves import configparser
from ansible.plugins.lookup.ini import LookupModule


def test_get_value_returns_values_matching_regular_expression():
    parser = configparser.ConfigParser()
    parser.add_section("settings")
    parser.set("settings", "foo_one", "first")
    parser.set("settings", "unrelated", "ignored")
    parser.set("settings", "foo_two", "second")

    lookup = LookupModule()
    lookup.cp = parser

    assert lookup.get_value(r"^foo_", "settings", "default", True) == [
        "first",
        "second",
    ]


def test_get_value_returns_single_existing_value():
    parser = configparser.ConfigParser()
    parser.add_section("settings")
    parser.set("settings", "answer", "42")

    lookup = LookupModule()
    lookup.cp = parser

    assert lookup.get_value("answer", "settings", "default", False) == "42"


def test_get_value_returns_default_when_option_does_not_exist():
    parser = configparser.ConfigParser()
    parser.add_section("settings")

    lookup = LookupModule()
    lookup.cp = parser

    default = object()
    assert lookup.get_value("missing", "settings", default, False) is default

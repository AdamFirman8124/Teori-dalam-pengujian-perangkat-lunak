# file: project/ansible/plugins/lookup/ini.py:124-134
# asked: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}

import re
from ansible.module_utils.six.moves import configparser

import pytest

from ansible.plugins.lookup.ini import LookupModule


def _make_lookup_with_cp(sections):
    """Build a LookupModule whose .cp is a ConfigParser populated from `sections`."""
    lm = LookupModule()
    cp = configparser.ConfigParser()
    for section, options in sections.items():
        cp.add_section(section)
        for k, v in options.items():
            cp.set(section, k, v)
    lm.cp = cp
    return lm


def test_get_value_regexp_matches_all_keys():
    lm = _make_lookup_with_cp({
        'sect': {'alpha.one': '1', 'alpha.two': '2', 'beta': '3'},
    })
    result = lm.get_value(r'alpha\..*', 'sect', 'unused', True)
    assert result == ['1', '2']


def test_get_value_regexp_no_match_returns_empty_list():
    lm = _make_lookup_with_cp({
        'sect': {'alpha.one': '1'},
    })
    result = lm.get_value(r'nomatch.*', 'sect', 'unused', True)
    assert result == []


def test_get_value_single_existing_key():
    lm = _make_lookup_with_cp({
        'sect': {'key': 'value'},
    })
    result = lm.get_value('key', 'sect', 'dflt', False)
    assert result == 'value'


def test_get_value_missing_key_returns_default():
    lm = _make_lookup_with_cp({
        'sect': {'other': 'value'},
    })
    result = lm.get_value('missing', 'sect', 'dflt', False)
    assert result == 'dflt'


def test_get_value_missing_key_default_none():
    lm = _make_lookup_with_cp({
        'sect': {'other': 'value'},
    })
    result = lm.get_value('missing', 'sect', None, False)
    assert result is None

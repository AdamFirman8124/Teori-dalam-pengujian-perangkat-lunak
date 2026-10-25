# file: project/ansible/plugins/lookup/ini.py:124-134
# asked: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [126, 127, 128, 130, 131, 132, 133, 134], "branches": [[126, 127], [126, 128]]}

import re

import pytest

from ansible.module_utils.six.moves import configparser
from ansible.plugins.lookup.ini import LookupModule


@pytest.fixture
def lookup(monkeypatch):
    """A LookupModule instance whose ``cp`` is a throwaway ConfigParser."""
    cp = configparser.ConfigParser()
    cp.add_section('main')
    cp.set('main', 'foo', '1')
    cp.set('main', 'bar', '2')
    cp.set('main', 'baz', '3')

    obj = LookupModule.__new__(LookupModule)
    monkeypatch.setattr(obj, 'cp', cp, raising=False)
    return obj


def test_get_value_regexp_returns_all_matching_values(lookup):
    # lines 126-127: is_regexp branch
    result = lookup.get_value('ba', 'main', None, True)

    assert result == ['2', '3']
    assert isinstance(result, list)
    # postcondition: the config parser was not mutated
    assert lookup.cp.items('main') == [
        ('foo', '1'),
        ('bar', '2'),
        ('baz', '3'),
    ]


def test_get_value_regexp_no_match_returns_empty_list(lookup):
    # lines 126-127: regexp branch with zero matches
    result = lookup.get_value('nomatch', 'main', 'default', True)

    assert result == []
    assert isinstance(result, list)


def test_get_value_single_option_found(lookup):
    # lines 128-131 and 134: non-regexp path, option exists
    result = lookup.get_value('foo', 'main', 'default', False)

    assert result == '1'
    assert lookup.cp.get('main', 'foo') == '1'


def test_get_value_single_option_missing_returns_default(lookup):
    # lines 130-133: NoOptionError -> return dflt
    result = lookup.get_value('missing', 'main', 'default', False)

    assert result == 'default'
    # postcondition: nothing was added to the section
    assert 'missing' not in dict(lookup.cp.items('main'))


def test_get_value_single_option_missing_default_none(lookup):
    # lines 132-133: dflt is returned verbatim, even when None
    assert lookup.get_value('missing', 'main', None, False) is None

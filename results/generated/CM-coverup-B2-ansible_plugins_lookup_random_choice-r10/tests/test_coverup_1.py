# file: project/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import random

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup_module():
    """Fresh lookup plugin instance per test (no shared state between tests)."""
    return LookupModule()


def test_run_empty_terms_returns_empty_list(lookup_module):
    """Covers the falsy-terms branch of 'if terms:' (ret stays as terms)."""
    result = lookup_module.run([])
    assert result == []


def test_run_falsy_terms_returned_unchanged(lookup_module):
    """Other falsy values also take the 'if terms:' false branch untouched."""
    assert lookup_module.run(None) is None
    assert lookup_module.run('') == ''


def test_run_non_empty_terms_returns_one_random_term(lookup_module):
    """Covers the truthy-terms branch and the try body (random.choice call)."""
    terms = ['a', 'b', 'c']
    result = lookup_module.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_run_returns_element_chosen_by_random_choice(lookup_module, monkeypatch):
    """Deterministically verifies ret == [random.choice(terms)] on success."""
    terms = ['a', 'b', 'c']
    seen = {}

    def fake_choice(seq):
        seen['seq'] = seq
        return 'b'

    monkeypatch.setattr(random, 'choice', fake_choice)

    result = lookup_module.run(terms)

    assert seen['seq'] is terms
    assert result == ['b']


def test_run_wraps_random_choice_failure_in_ansible_error(lookup_module, monkeypatch):
    """Covers the except clause: the failure is re-raised as AnsibleError."""
    def failing_choice(seq):
        raise ValueError('boom')

    monkeypatch.setattr(random, 'choice', failing_choice)

    with pytest.raises(AnsibleError) as excinfo:
        lookup_module.run(['a', 'b'])

    assert 'Unable to choose random term' in str(excinfo.value)
    assert 'boom' in str(excinfo.value)

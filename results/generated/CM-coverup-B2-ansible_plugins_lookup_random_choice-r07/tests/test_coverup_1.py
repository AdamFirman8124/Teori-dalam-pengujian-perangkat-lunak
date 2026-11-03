# file: project/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import random

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup():
    """Provide a fresh LookupModule instance for each test."""
    return LookupModule()


def test_run_empty_terms(lookup):
    """Falsy terms: line 46 executes, line 47 takes the False branch, line 53 returns terms unchanged."""
    terms = []
    result = lookup.run(terms)
    # The original (empty) list is returned untouched.
    assert result == []
    assert result is terms


def test_run_non_empty_terms(lookup):
    """Truthy terms: lines 47 (True branch), 48, 49 and 53 execute; one random term is returned."""
    terms = ['a', 'b', 'c']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_run_random_choice_exception(lookup, monkeypatch):
    """Lines 50-51: an exception from random.choice is converted into an AnsibleError."""

    def fake_choice(seq):
        raise ValueError('boom')

    # Patch the random module attribute used by the plugin; monkeypatch restores it afterwards.
    monkeypatch.setattr(random, 'choice', fake_choice)

    with pytest.raises(AnsibleError) as exc_info:
        lookup.run(['a', 'b'])

    assert 'Unable to choose random term' in str(exc_info.value)
    assert 'boom' in str(exc_info.value)

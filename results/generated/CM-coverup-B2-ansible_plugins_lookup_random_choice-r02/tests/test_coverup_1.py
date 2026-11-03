# file: project/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import random

import pytest

from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup():
    """Provide a fresh LookupModule instance for each test."""
    return LookupModule()


def test_run_empty_terms_returns_terms_unchanged(lookup):
    """Falsy terms skip the random choice entirely (line 47 false branch)."""
    for empty in ([], (), None, ''):
        result = lookup.run(empty)
        # 'ret = terms' then 'return ret' with no modification
        assert result is empty


def test_run_nonempty_terms_returns_single_random_element(lookup):
    """Non-empty terms go through random.choice (lines 47-49)."""
    terms = ['a', 'b', 'c']
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_run_nonempty_terms_uses_random_choice(lookup, monkeypatch):
    """Deterministically verify random.choice is invoked with the terms."""
    terms = ['a', 'b', 'c']
    calls = []

    def fake_choice(seq):
        calls.append(seq)
        return seq[1]

    monkeypatch.setattr(random, 'choice', fake_choice)

    result = lookup.run(terms)

    assert calls == [terms]
    assert result == ['b']


def test_run_random_choice_failure_raises_ansible_error(lookup, monkeypatch):
    """An exception from random.choice is converted to AnsibleError (lines 50-51)."""

    def boom(seq):
        raise ValueError('boom')

    monkeypatch.setattr(random, 'choice', boom)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['a', 'b'])

    assert 'Unable to choose random term: boom' in to_native(excinfo.value)

# file: project/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import random

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_run_empty_terms():
    """Empty terms list: the `if terms:` branch is False, ret stays as terms."""
    lookup = LookupModule()
    result = lookup.run([])
    assert result == []


def test_run_nonempty_terms():
    """Non-empty terms: random.choice is called and a single-element list is returned."""
    terms = ['a', 'b', 'c']
    lookup = LookupModule()
    result = lookup.run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_run_single_term():
    """Single term: must return exactly that term."""
    lookup = LookupModule()
    result = lookup.run(['only'])
    assert result == ['only']


def test_run_random_choice_raises(monkeypatch):
    """Exception path: random.choice raising leads to AnsibleError."""

    def fake_choice(seq):
        raise ValueError('boom')

    monkeypatch.setattr(random, 'choice', fake_choice)

    lookup = LookupModule()
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['a', 'b'])

    assert 'Unable to choose random term: boom' in str(excinfo.value)

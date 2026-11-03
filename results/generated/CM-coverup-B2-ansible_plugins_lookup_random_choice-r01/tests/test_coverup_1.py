# file: project/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import random

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup():
    return LookupModule()


def test_run_empty_terms_returns_empty_list(lookup):
    """Covers: ret = terms, the False branch of `if terms:`, and `return ret`."""
    result = lookup.run([])
    assert result == []


def test_run_non_empty_terms_returns_single_random_term(lookup, monkeypatch):
    """Covers: the True branch of `if terms:`, the try block, and
    ret = [random.choice(terms)], plus `return ret`."""
    terms = ['a', 'b', 'c']
    # Patch random.choice for a deterministic result; monkeypatch restores it.
    monkeypatch.setattr(random, 'choice', lambda seq: 'b')

    result = lookup.run(terms)

    assert result == ['b']
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_run_random_choice_failure_raises_ansible_error(lookup, monkeypatch):
    """Covers: the except branch and the `raise AnsibleError(...)` line."""

    def failing_choice(seq):
        raise ValueError('boom')

    monkeypatch.setattr(random, 'choice', failing_choice)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['a', 'b'])

    assert excinfo.value.message == 'Unable to choose random term: boom'

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
    # LookupBase.__init__ accepts loader=None, templar=None, so plain
    # instantiation is safe and requires no global state.
    return LookupModule()


def test_run_empty_terms(lookup):
    """Covers lines 46-47 (assignment + falsy branch) and line 53 (return)."""
    result = lookup.run([])
    # With empty terms, ret stays as the original terms object.
    assert result == []
    assert result is not lookup.run  # sanity: it's the list, not the method


def test_run_none_terms(lookup):
    """Covers the falsy branch of 'if terms' when terms is None."""
    result = lookup.run(None)
    assert result is None


def test_run_non_empty_terms(lookup, monkeypatch):
    """Covers lines 48-49: the try block with a successful random.choice."""
    # Pin random.choice so the result is deterministic; monkeypatch
    # automatically restores the original on test teardown.
    monkeypatch.setattr(random, 'choice', lambda seq: seq[0])
    terms = ['a', 'b', 'c']
    result = lookup.run(terms)
    assert result == ['a']
    # The original terms list must not be mutated.
    assert terms == ['a', 'b', 'c']


def test_run_random_choice_raises(lookup, monkeypatch):
    """Covers lines 50-51: exception path converting failure to AnsibleError."""

    def boom(seq):
        raise ValueError('boom')

    monkeypatch.setattr(random, 'choice', boom)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['a', 'b'])

    message = to_native(excinfo.value)
    assert 'Unable to choose random term' in message
    assert 'boom' in message

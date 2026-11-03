# file: project/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import random

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup_module():
    """Fresh LookupModule instance for each test (LookupBase needs no args)."""
    return LookupModule()


def test_run_falsy_terms_returned_unchanged(lookup_module):
    """Covers line 46, the false branch of line 47, and line 53.

    With falsy terms, 'ret = terms' is returned directly without
    invoking random.choice.
    """
    for falsy in ([], (), '', None):
        result = lookup_module.run(falsy)
        assert result == falsy
        assert result is falsy  # returned object is the very same one


def test_run_nonempty_terms_returns_single_random_element(lookup_module):
    """Covers the true branch of line 47, line 49 and line 53.

    With truthy terms, exactly one element randomly chosen from the
    input must be returned inside a list.
    """
    terms = ['a', 'b', 'c']
    result = lookup_module.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms


def test_run_wraps_random_choice_failure_in_ansible_error(lookup_module, monkeypatch):
    """Covers lines 50-51: any exception raised by random.choice is
    converted into an AnsibleError whose message contains the original
    error text.

    monkeypatch automatically restores random.choice after the test,
    so no state pollution occurs.
    """

    def failing_choice(seq):
        raise ValueError('boom')

    monkeypatch.setattr(random, 'choice', failing_choice)

    with pytest.raises(AnsibleError) as excinfo:
        lookup_module.run(['a', 'b'])

    message = str(excinfo.value)
    assert 'Unable to choose random term' in message
    assert 'boom' in message

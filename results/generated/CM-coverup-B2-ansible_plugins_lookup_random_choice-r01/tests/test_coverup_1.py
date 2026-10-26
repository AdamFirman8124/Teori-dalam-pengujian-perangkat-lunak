# file: project/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import random

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_run_empty_terms():
    """Empty terms list: line 46 executes, line 47 branch is False, returns []."""
    lookup = LookupModule()
    ret = lookup.run([])
    assert ret == []


def test_run_non_empty_terms():
    """Non-empty terms: line 49 executes, result is one of the terms."""
    terms = ['a', 'b', 'c']
    lookup = LookupModule()
    ret = lookup.run(terms)
    assert len(ret) == 1
    assert ret[0] in terms


def test_run_exception_raises_ansible_error(monkeypatch):
    """Exception in random.choice: lines 50-51 execute, AnsibleError raised."""

    def fake_choice(seq):
        raise ValueError("boom")

    monkeypatch.setattr(random, 'choice', fake_choice)

    lookup = LookupModule()
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['a', 'b'])
    assert "Unable to choose random term: boom" in str(excinfo.value)

# file: project/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import random

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


def test_run_empty_terms_returns_empty_list():
    lookup = LookupModule()
    result = lookup.run([])
    assert result == []


def test_run_non_empty_terms_returns_one_term():
    terms = ['a', 'b', 'c']
    lookup = LookupModule()
    result = lookup.run(terms)
    assert len(result) == 1
    assert result[0] in terms


def test_run_exception_raised_as_ansible_error(monkeypatch):
    def fake_choice(seq):
        raise ValueError("boom")

    monkeypatch.setattr(
        "ansible.plugins.lookup.random_choice.random.choice", fake_choice
    )
    lookup = LookupModule()
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['a', 'b'])
    assert "Unable to choose random term: boom" in str(excinfo.value)

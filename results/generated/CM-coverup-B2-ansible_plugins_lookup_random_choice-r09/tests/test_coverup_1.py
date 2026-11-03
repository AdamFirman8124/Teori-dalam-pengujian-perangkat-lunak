# file: project/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import random

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule


@pytest.fixture
def lookup():
    """Fresh lookup instance for each test (no shared state)."""
    return LookupModule()


def test_run_empty_terms(lookup):
    """Falsy terms: 'if terms' False branch taken, terms returned unchanged."""
    terms = []
    result = lookup.run(terms)
    assert result == []
    assert result is terms  # ret = terms is returned as-is when falsy


def test_run_none_terms(lookup):
    """None terms: also falsy branch, returned unchanged."""
    result = lookup.run(None)
    assert result is None


def test_run_nonempty_terms(lookup):
    """Truthy terms: random.choice is used, a single-element list is returned."""
    terms = ["a", "b", "c"]
    result = lookup.run(terms)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms
    # original terms must not be mutated
    assert terms == ["a", "b", "c"]


def test_run_nonempty_terms_deterministic(monkeypatch, lookup):
    """Truthy terms with a stubbed random.choice for a deterministic result."""
    monkeypatch.setattr(random, "choice", lambda seq: seq[-1])
    result = lookup.run(["a", "b", "c"])
    assert result == ["c"]


def test_run_choice_exception(monkeypatch, lookup):
    """Exception inside random.choice is converted into an AnsibleError."""
    def fake_choice(seq):
        raise ValueError("boom")

    monkeypatch.setattr(random, "choice", fake_choice)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(["a", "b"])

    assert "Unable to choose random term" in str(excinfo.value)
    assert "boom" in str(excinfo.value)

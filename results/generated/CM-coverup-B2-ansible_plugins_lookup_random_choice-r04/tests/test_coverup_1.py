# file: project/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup import random_choice


def test_run_returns_empty_terms_unchanged(monkeypatch):
    terms = []

    def unexpected_choice(_terms):
        pytest.fail("random.choice must not be called for empty terms")

    monkeypatch.setattr(random_choice.random, "choice", unexpected_choice)

    result = random_choice.LookupModule().run(terms)

    assert result is terms
    assert result == []


def test_run_returns_randomly_chosen_term(monkeypatch):
    terms = ["first", "second", "third"]
    calls = []

    def choose(received_terms):
        calls.append(received_terms)
        return "second"

    monkeypatch.setattr(random_choice.random, "choice", choose)

    result = random_choice.LookupModule().run(terms)

    assert calls == [terms]
    assert result == ["second"]
    assert result is not terms


def test_run_wraps_choice_exception_as_ansible_error(monkeypatch):
    terms = ["first"]

    def fail_choice(received_terms):
        assert received_terms is terms
        raise ValueError("choice failed")

    monkeypatch.setattr(random_choice.random, "choice", fail_choice)

    with pytest.raises(
        AnsibleError,
        match=r"^Unable to choose random term: choice failed$",
    ) as exc_info:
        random_choice.LookupModule().run(terms)

    assert isinstance(exc_info.value.__context__, ValueError)
    assert str(exc_info.value.__context__) == "choice failed"

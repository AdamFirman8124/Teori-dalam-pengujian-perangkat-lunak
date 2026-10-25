# file: project/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup import random_choice


def test_run_returns_empty_terms_unchanged():
    terms = []

    result = random_choice.LookupModule().run(terms)

    assert result is terms
    assert result == []


def test_run_returns_selected_term(monkeypatch):
    terms = ["first", "second"]
    calls = []

    def fake_choice(values):
        calls.append(values)
        return "second"

    monkeypatch.setattr(random_choice.random, "choice", fake_choice)

    result = random_choice.LookupModule().run(
        terms, inject={"unused": True}, unused_option=True
    )

    assert result == ["second"]
    assert calls == [terms]


def test_run_wraps_choice_exception_as_ansible_error(monkeypatch):
    terms = ["first"]

    def raise_choice_error(values):
        assert values is terms
        raise ValueError("choice failed")

    monkeypatch.setattr(random_choice.random, "choice", raise_choice_error)

    with pytest.raises(
        AnsibleError,
        match=r"^Unable to choose random term: choice failed$",
    ):
        random_choice.LookupModule().run(terms)

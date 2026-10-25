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

    def choose_second(sequence):
        assert sequence is terms
        return sequence[1]

    monkeypatch.setattr(random_choice.random, "choice", choose_second)

    result = random_choice.LookupModule().run(terms)

    assert result == ["second"]
    assert terms == ["first", "second"]


def test_run_wraps_choice_exception_as_ansible_error(monkeypatch):
    terms = ["only"]

    def fail_choice(sequence):
        assert sequence is terms
        raise ValueError("selection failed")

    monkeypatch.setattr(random_choice.random, "choice", fail_choice)

    with pytest.raises(AnsibleError) as exc_info:
        random_choice.LookupModule().run(terms)

    assert str(exc_info.value) == "Unable to choose random term: selection failed"
    assert terms == ["only"]

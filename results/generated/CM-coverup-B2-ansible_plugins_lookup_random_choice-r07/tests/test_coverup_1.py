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


def test_empty_list_terms_returns_terms_unchanged(lookup, monkeypatch):
    def fail(seq):
        raise AssertionError("random.choice must not be called for empty terms")

    monkeypatch.setattr(random, "choice", fail)

    terms = []
    result = lookup.run(terms)

    assert result is terms
    assert result == []


def test_empty_tuple_terms_returns_terms_unchanged(lookup, monkeypatch):
    def fail(seq):
        raise AssertionError("random.choice must not be called for empty terms")

    monkeypatch.setattr(random, "choice", fail)

    terms = ()
    result = lookup.run(terms)

    assert result is terms
    assert result == ()


def test_none_terms_returns_none(lookup, monkeypatch):
    def fail(seq):
        raise AssertionError("random.choice must not be called for falsy terms")

    monkeypatch.setattr(random, "choice", fail)

    assert lookup.run(None) is None


def test_non_empty_terms_returns_single_element_list(lookup, monkeypatch):
    terms = ["a", "b", "c"]
    monkeypatch.setattr(random, "choice", lambda seq: seq[1])

    result = lookup.run(terms)

    assert result == ["b"]
    assert isinstance(result, list)
    assert len(result) == 1
    # original terms must not be mutated
    assert terms == ["a", "b", "c"]


def test_non_empty_terms_passes_terms_to_random_choice(lookup, monkeypatch):
    seen = []

    def fake_choice(seq):
        seen.append(list(seq))
        return seq[-1]

    monkeypatch.setattr(random, "choice", fake_choice)

    terms = ["x", "y"]
    result = lookup.run(terms, inject={"foo": "bar"}, extra="ignored")

    assert result == ["y"]
    assert seen == [["x", "y"]]


def test_choice_exception_is_wrapped_in_ansible_error(lookup, monkeypatch):
    def boom(seq):
        raise ValueError("boom")

    monkeypatch.setattr(random, "choice", boom)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(["a", "b"])

    assert "Unable to choose random term: boom" in str(excinfo.value)


def test_choice_exception_message_is_native_text(lookup, monkeypatch):
    def boom(seq):
        raise RuntimeError(u"caf\u00e9 failure")

    monkeypatch.setattr(random, "choice", boom)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(["a"])

    message = str(excinfo.value)
    assert "Unable to choose random term:" in message
    assert u"caf\u00e9 failure" in message

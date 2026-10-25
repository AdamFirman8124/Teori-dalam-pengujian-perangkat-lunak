# file: project/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafe, _wrap_set, wrap_var


def test_wrap_set_direct_wraps_strings_as_unsafe():
    original = {"hello", "world"}
    result = _wrap_set(original)

    assert type(result) is set
    assert result == original
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert all(getattr(item, "__UNSAFE__", False) is True for item in result)
    # Original is unchanged / not mutated
    assert all(type(item) is str for item in original)
    assert not any(isinstance(item, AnsibleUnsafe) for item in original)


def test_wrap_var_wraps_set_of_strings_as_unsafe():
    original = {"alpha", "beta", "gamma"}
    result = wrap_var(original)

    assert type(result) is set
    assert result == original
    assert len(result) == 3
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert all(getattr(item, "__UNSAFE__", False) is True for item in result)
    assert all(type(item) is str for item in original)


def test_wrap_set_empty_set():
    result_direct = _wrap_set(set())
    result_wrapped = wrap_var(set())

    assert type(result_direct) is set
    assert result_direct == set()
    assert type(result_wrapped) is set
    assert result_wrapped == set()


def test_wrap_set_non_string_items_pass_through():
    original = {1, 2, 3}
    result = _wrap_set(original)

    assert type(result) is set
    assert result == {1, 2, 3}
    assert all(type(item) is int for item in result)

    result_wrapped = wrap_var({42})
    assert type(result_wrapped) is set
    assert result_wrapped == {42}
    assert all(type(item) is int for item in result_wrapped)


def test_wrap_set_nested_tuple_items():
    original = {("a", "b"), "c"}
    result = _wrap_set(original)

    assert type(result) is set
    assert result == original
    assert len(result) == 2

    tuples = [item for item in result if isinstance(item, tuple)]
    strings = [item for item in result if isinstance(item, str) and not isinstance(item, tuple)]
    assert len(tuples) == 1
    assert tuples[0] == ("a", "b")
    assert all(isinstance(part, AnsibleUnsafe) for part in tuples[0])
    assert len(strings) == 1
    assert isinstance(strings[0], AnsibleUnsafe)


def test_wrap_var_set_nested_in_dict_and_list():
    result_dict = wrap_var({"key": {"x", "y"}})
    assert type(result_dict["key"]) is set
    assert result_dict["key"] == {"x", "y"}
    assert all(isinstance(item, AnsibleUnsafe) for item in result_dict["key"])

    result_list = wrap_var([{"only"}])
    assert type(result_list[0]) is set
    assert result_list[0] == {"only"}
    assert all(isinstance(item, AnsibleUnsafe) for item in result_list[0])

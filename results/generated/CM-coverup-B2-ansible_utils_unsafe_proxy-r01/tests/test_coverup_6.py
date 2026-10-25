# file: project/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeText, _wrap_dict, wrap_var


def test_wrap_var_dict_simple_marks_keys_and_values_unsafe():
    original = {"key": "value"}
    result = wrap_var(original)
    assert result == {"key": "value"}
    assert len(result) == 1
    k, v = next(iter(result.items()))
    assert isinstance(k, AnsibleUnsafe)
    assert isinstance(v, AnsibleUnsafe)
    assert isinstance(k, AnsibleUnsafeText)
    assert isinstance(v, AnsibleUnsafeText)
    assert str(k) == "key"
    assert str(v) == "value"
    # input must not be mutated
    assert original == {"key": "value"}
    assert not isinstance("key", AnsibleUnsafe)


def test_wrap_dict_direct_empty_and_nonempty():
    assert _wrap_dict({}) == {}
    result = _wrap_dict({"a": "b", 1: "x", "n": None})
    assert len(result) == 3
    # string key/value are wrapped
    assert result[AnsibleUnsafeText("a")] == AnsibleUnsafeText("b")
    for k, item in result.items():
        if k == "a":
            assert isinstance(k, AnsibleUnsafe)
            assert isinstance(item, AnsibleUnsafe)
        if k == 1:
            # non-string keys are left as-is
            assert type(k) is int
            assert isinstance(item, AnsibleUnsafe)
            assert str(item) == "x"
        if k == "n":
            assert isinstance(k, AnsibleUnsafe)
            assert item is None


def test_wrap_var_dict_nested_and_list_values():
    result = wrap_var({"outer": {"inner": "val"}, "lst": ["a", 1]})
    assert set(result.keys()) == {"outer", "lst"}
    for k in result.keys():
        assert isinstance(k, AnsibleUnsafe)
    nested = result["outer"]
    assert isinstance(nested, dict)
    assert nested == {"inner": "val"}
    nk, nv = next(iter(nested.items()))
    assert isinstance(nk, AnsibleUnsafe)
    assert isinstance(nv, AnsibleUnsafe)
    lst = result["lst"]
    assert lst == ["a", 1]
    assert isinstance(lst[0], AnsibleUnsafe)
    assert lst[1] == 1

# file: project/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    _wrap_dict,
    wrap_var,
)


def test_wrap_var_empty_dict_executes_wrap_dict():
    result = wrap_var({})
    assert result == {}
    assert type(result) is dict
    assert result is not None


def test_wrap_var_dict_wraps_keys_and_values():
    original = {"key": "value", "count": 42}
    snapshot = dict(original)
    result = wrap_var(original)
    assert result is not original
    # original must not be mutated (no state pollution)
    assert original == snapshot
    assert len(result) == 2
    for k, v in result.items():
        assert isinstance(k, AnsibleUnsafe)
        assert isinstance(k, AnsibleUnsafeText)
    assert result["key"] == "value"
    assert isinstance(result["key"], AnsibleUnsafeText)
    assert isinstance(result["count"], int)
    assert result["count"] == 42
    # wrapped keys compare equal to plain strings but are unsafe
    assert set(result.keys()) == {"key", "count"}


def test_wrap_dict_direct_covers_generator_branch():
    result = _wrap_dict({"a": "b", 1: "c"})
    assert isinstance(result, dict)
    assert len(result) == 2
    assert result["a"] == "b"
    assert isinstance(result["a"], AnsibleUnsafeText)
    assert result[1] == "c"
    assert isinstance(result[1], AnsibleUnsafeText)
    # string key was wrapped
    wrapped_key = [k for k in result.keys() if k == "a"][0]
    assert isinstance(wrapped_key, AnsibleUnsafeText)
    # integer key is left as-is
    assert 1 in result


def test_wrap_dict_nested_dict_recursion():
    original = {"outer": {"inner": "val"}, "lst": ["x", "y"]}
    result = wrap_var(original)
    assert isinstance(result["outer"], dict)
    assert result["outer"] == {"inner": "val"}
    assert isinstance(result["outer"]["inner"], AnsibleUnsafeText)
    inner_key = next(iter(result["outer"].keys()))
    assert isinstance(inner_key, AnsibleUnsafeText)
    assert result["lst"] == ["x", "y"]
    assert all(isinstance(i, AnsibleUnsafeText) for i in result["lst"])
    # original nested structures unchanged and still plain strings
    assert type(original["outer"]["inner"]) is str
    assert type(original["lst"][0]) is str

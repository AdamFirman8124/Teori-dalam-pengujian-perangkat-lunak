# file: project/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    wrap_var,
)


def test_wrap_var_set_of_strings_executes_wrap_set():
    result = wrap_var({"hello", "world"})

    assert isinstance(result, set)
    assert result == {"hello", "world"}
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert all(getattr(item, "__UNSAFE__", False) is True for item in result)


def test_wrap_var_empty_set_executes_wrap_set():
    result = wrap_var(set())

    assert isinstance(result, set)
    assert result == set()
    assert len(result) == 0


def test_wrap_var_set_mixed_hashable_types():
    unsafe_text = AnsibleUnsafeText("already")
    result = wrap_var({unsafe_text, b"bytes", 42, ("nested", "tuple")})

    assert isinstance(result, set)
    assert len(result) == 4
    assert 42 in result
    assert any(item is unsafe_text for item in result)
    assert any(
        isinstance(item, AnsibleUnsafeBytes) and item == b"bytes"
        for item in result
    )
    assert any(
        isinstance(item, tuple)
        and item == ("nested", "tuple")
        and all(isinstance(part, AnsibleUnsafeText) for part in item)
        for item in result
    )


def test_wrap_var_set_does_not_mutate_original():
    original = {"a", "b"}
    result = wrap_var(original)

    assert result is not original
    assert original == {"a", "b"}
    assert all(type(item) is str for item in original)
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)

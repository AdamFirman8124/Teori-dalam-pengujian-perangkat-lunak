# file: project/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeText, _wrap_sequence, wrap_var


def test_wrap_sequence_list_via_wrap_var():
    original = ["a", "b", 1, None]
    result = wrap_var(original)
    assert isinstance(result, list)
    assert result is not original
    assert result[0] == "a"
    assert result[1] == "b"
    assert result[2] == 1
    assert result[3] is None
    assert isinstance(result[0], AnsibleUnsafe)
    assert isinstance(result[0], AnsibleUnsafeText)
    assert isinstance(result[1], AnsibleUnsafe)
    # non-string / None passthrough checks
    assert result[2] == 1
    assert result[3] is None


def test_wrap_sequence_tuple_via_wrap_var():
    original = ("a", "b")
    result = wrap_var(original)
    assert isinstance(result, tuple)
    assert result == ("a", "b")
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)


def test_wrap_sequence_direct_preserves_type():
    for v_type in (list, tuple):
        value = v_type(["x", 42])
        result = _wrap_sequence(value)
        assert isinstance(result, v_type)
        assert list(result) == ["x", 42]
        assert isinstance(result[0], AnsibleUnsafe)
        assert isinstance(result[0], AnsibleUnsafeText)

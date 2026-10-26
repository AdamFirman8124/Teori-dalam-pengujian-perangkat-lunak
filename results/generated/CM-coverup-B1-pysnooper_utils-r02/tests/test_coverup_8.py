# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import pysnooper.utils as utils_module


def test_normalize_repr_removes_memory_address():
    func = getattr(utils_module, "normalize_repr", None)
    if func is None:
        # Fall back to exercising the nested definition via its outer caller.
        class WithAddress:
            def __repr__(self):
                return "<WithAddress at 0x1234ABCD>"
        result = utils_module.get_shortish_repr(WithAddress(), normalize=True)
        assert result == "<WithAddress>"
        assert "at 0x" not in result
        return
    assert func("<object object at 0x7f8b8c0d5e00>") == "<object object>"
    assert func("<X at 0xDEADBEEF>") == "<X>"
    assert func("foo at 0x1234 bar") == "foo bar"


def test_normalize_repr_leaves_plain_repr_unchanged():
    func = getattr(utils_module, "normalize_repr", None)
    if func is None:
        pytest_skip = __import__("pytest").skip
        pytest_skip("normalize_repr not exposed at module level")
    assert func("hello") == "hello"
    assert func("") == ""
    assert func("<object object>") == "<object object>"
    # Fewer than 4 hex digits does not match DEFAULT_REPR_RE.
    assert func("foo at 0x12") == "foo at 0x12"
    assert "0x" not in func("<A at 0xABCDEF> and <B at 0x123456>")


def test_get_shortish_repr_with_normalize_covers_normalize_repr():
    class WithAddress:
        def __repr__(self):
            return "<WithAddress at 0x1234ABCD>"

    obj = WithAddress()
    normalized = utils_module.get_shortish_repr(obj, normalize=True)
    assert normalized == "<WithAddress>"
    assert "at 0x" not in normalized
    assert "0x1234ABCD" not in normalized

    # Control case: without normalize the address is preserved.
    unnormalized = utils_module.get_shortish_repr(obj, normalize=False)
    assert unnormalized == "<WithAddress at 0x1234ABCD>"
    assert "at 0x" in unnormalized

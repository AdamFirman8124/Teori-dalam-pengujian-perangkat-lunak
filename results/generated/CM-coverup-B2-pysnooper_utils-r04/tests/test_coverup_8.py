# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import pysnooper.utils as utils_module


def test_get_shortish_repr_normalize_true_strips_address():
    class WithAddress:
        def __repr__(self):
            return "<WithAddress at 0x1234ABCD>"

    result = utils_module.get_shortish_repr(WithAddress(), normalize=True)
    assert result == "<WithAddress>"
    assert "at 0x" not in result
    assert "0x1234ABCD" not in result


def test_get_shortish_repr_normalize_false_keeps_address():
    class WithAddress:
        def __repr__(self):
            return "<WithAddress at 0x1234ABCD>"

    result = utils_module.get_shortish_repr(WithAddress(), normalize=False)
    assert result == "<WithAddress at 0x1234ABCD>"
    assert "at 0x" in result


def test_normalize_repr_direct_strips_address():
    func = getattr(utils_module, "normalize_repr", None)
    if func is None:
        # normalize_repr is nested; already exercised via normalize=True above
        result = utils_module.get_shortish_repr("<X at 0xDEADBEEF>", normalize=True)
        assert "at 0x" not in result
        return
    assert func("<object object at 0x7f8b8c0d5e00>") == "<object object>"
    assert func("<MyClass object at 0x00abCD12>") == "<MyClass object>"
    assert func("<plain object>") == "<plain object>"
    assert func("hello") == "hello"
    assert func("") == ""
    # Regex requires at least 4 hex digits, so short address is kept
    assert func("foo at 0x12") == "foo at 0x12"
    assert "0x" not in func("<X at 0xDEADBEEF>")

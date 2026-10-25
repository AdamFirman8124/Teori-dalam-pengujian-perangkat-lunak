# file: project/pysnooper/utils.py:67-78
# asked: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}
# gained: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}

import pysnooper.utils as utils


def test_get_shortish_repr_removes_newlines_and_truncates():
    custom_repr = ((str, lambda item: "ab\r\ncdefgh"),)

    result = utils.get_shortish_repr(
        "item",
        custom_repr=custom_repr,
        max_length=7,
    )

    assert result == "ab...gh"


def test_get_shortish_repr_handles_repr_exception():
    class BrokenRepr:
        def __repr__(self):
            raise RuntimeError("repr failed")

    assert utils.get_shortish_repr(BrokenRepr()) == "REPR FAILED"


def test_get_shortish_repr_normalizes_after_removing_newlines(monkeypatch):
    normalized_inputs = []

    def fake_normalize_repr(value):
        normalized_inputs.append(value)
        return "normalized"

    monkeypatch.setattr(utils, "normalize_repr", fake_normalize_repr)
    custom_repr = ((str, lambda item: "before\r\nnormalization"),)

    result = utils.get_shortish_repr(
        "item",
        custom_repr=custom_repr,
        normalize=True,
    )

    assert result == "normalized"
    assert normalized_inputs == ["beforenormalization"]

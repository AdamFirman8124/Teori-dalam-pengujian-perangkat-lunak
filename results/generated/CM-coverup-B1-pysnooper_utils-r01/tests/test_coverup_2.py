# file: project/pysnooper/utils.py:67-78
# asked: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}
# gained: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}

from pysnooper import utils


def test_get_shortish_repr_cleans_normalizes_and_truncates():
    custom_repr = (
        (str, lambda item: "prefix at 0xABCDEF-suffix\r\n"),
    )

    result = utils.get_shortish_repr(
        "ignored",
        custom_repr=custom_repr,
        max_length=9,
        normalize=True,
    )

    assert result == "pre...fix"


def test_get_shortish_repr_handles_repr_failure():
    def failing_repr(item):
        raise RuntimeError("representation failed")

    result = utils.get_shortish_repr(
        object(),
        custom_repr=((lambda item: True, failing_repr),),
    )

    assert result == "REPR FAILED"


def test_get_shortish_repr_uses_default_repr_without_optional_processing():
    item = {"answer": 42}

    result = utils.get_shortish_repr(item)

    assert result == repr(item)

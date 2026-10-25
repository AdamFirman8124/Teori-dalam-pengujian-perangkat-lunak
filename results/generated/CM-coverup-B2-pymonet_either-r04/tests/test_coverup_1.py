# file: project/pymonet/either.py:22-35
# asked: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}

from pymonet.either import Left, Right


def test_case_calls_success_handler_on_right():
    right = Right(42)

    result = right.case(
        error=lambda value: "error: {}".format(value),
        success=lambda value: "success: {}".format(value)
    )

    assert result == "success: 42"
    assert right.is_right() is True


def test_case_calls_error_handler_on_left():
    left = Left("boom")

    result = left.case(
        error=lambda value: "error: {}".format(value),
        success=lambda value: "success: {}".format(value)
    )

    assert result == "error: boom"
    assert left.is_right() is False

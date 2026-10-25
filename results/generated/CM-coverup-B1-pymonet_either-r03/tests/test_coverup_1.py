# file: project/pymonet/either.py:22-35
# asked: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [33, 34, 35], "branches": [[33, 34], [33, 35]]}

from pymonet.either import Left, Right


def test_case_on_right_calls_success():
    calls = {"error": [], "success": []}

    def error(v):
        calls["error"].append(v)
        return f"error:{v}"

    def success(v):
        calls["success"].append(v)
        return f"success:{v}"

    result = Right(42).case(error, success)

    assert result == "success:42"
    assert calls["success"] == [42]
    assert calls["error"] == []


def test_case_on_left_calls_error():
    calls = {"error": [], "success": []}

    def error(v):
        calls["error"].append(v)
        return f"error:{v}"

    def success(v):
        calls["success"].append(v)
        return f"success:{v}"

    result = Left("oops").case(error, success)

    assert result == "error:oops"
    assert calls["error"] == ["oops"]
    assert calls["success"] == []

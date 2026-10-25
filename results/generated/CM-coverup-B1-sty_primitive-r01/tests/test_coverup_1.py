# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

from sty.primitive import Register


def test_register_call_returns_empty_string_when_muted(monkeypatch):
    register = Register()

    def unexpected_call(*args, **kwargs):
        raise AssertionError("A render function was called while muted")

    monkeypatch.setattr(register, "is_muted", True)
    monkeypatch.setattr(register, "eightbit_call", unexpected_call)
    monkeypatch.setattr(register, "rgb_call", unexpected_call)

    assert register(42) == ""
    assert register(1, 2, 3) == ""


def test_register_call_dispatches_integer_to_eightbit_renderer(monkeypatch):
    register = Register()
    calls = []

    def eightbit_call(value, **kwargs):
        calls.append((value, kwargs))
        return "eight-bit-result"

    monkeypatch.setattr(register, "eightbit_call", eightbit_call)

    assert register(42, mode="test") == "eight-bit-result"
    assert calls == [(42, {"mode": "test"})]


def test_register_call_returns_named_attribute(monkeypatch):
    register = Register()
    monkeypatch.setattr(register, "red", "named-colour-result", raising=False)

    assert register("red") == "named-colour-result"


def test_register_call_dispatches_three_arguments_to_rgb_renderer(monkeypatch):
    register = Register()
    calls = []

    def rgb_call(red, green, blue, **kwargs):
        calls.append(((red, green, blue), kwargs))
        return "rgb-result"

    monkeypatch.setattr(register, "rgb_call", rgb_call)

    assert register(102, 49, 42, mode="test") == "rgb-result"
    assert calls == [((102, 49, 42), {"mode": "test"})]


def test_register_call_returns_empty_string_for_unsupported_argument_counts():
    register = Register()

    assert register() == ""
    assert register(1, 2) == ""
    assert register(1, 2, 3, 4) == ""

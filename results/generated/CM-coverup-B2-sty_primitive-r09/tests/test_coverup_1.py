# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

from sty.primitive import Register


def test_register_call_returns_empty_string_when_muted(monkeypatch):
    register = Register()

    def unexpected_call(*args, **kwargs):
        raise AssertionError("A muted register must not invoke a render function")

    monkeypatch.setattr(register, "eightbit_call", unexpected_call)
    monkeypatch.setattr(register, "rgb_call", unexpected_call)
    monkeypatch.setattr(register, "is_muted", True)

    assert register(42) == ""


def test_register_call_dispatches_integer_to_eightbit_renderer(monkeypatch):
    register = Register()
    calls = []

    def render_eightbit(value, **kwargs):
        calls.append((value, kwargs))
        return "eightbit-result"

    monkeypatch.setattr(register, "eightbit_call", render_eightbit)

    result = register(42, option="value")

    assert result == "eightbit-result"
    assert calls == [(42, {"option": "value"})]


def test_register_call_returns_named_attribute(monkeypatch):
    register = Register()
    monkeypatch.setattr(register, "custom_color", "named-result", raising=False)

    assert register("custom_color") == "named-result"


def test_register_call_dispatches_three_arguments_to_rgb_renderer(monkeypatch):
    register = Register()
    calls = []

    def render_rgb(red, green, blue, **kwargs):
        calls.append(((red, green, blue), kwargs))
        return "rgb-result"

    monkeypatch.setattr(register, "rgb_call", render_rgb)

    result = register(102, 49, 42, option="value")

    assert result == "rgb-result"
    assert calls == [((102, 49, 42), {"option": "value"})]


def test_register_call_returns_empty_string_for_unsupported_argument_count(
    monkeypatch,
):
    register = Register()

    def unexpected_call(*args, **kwargs):
        raise AssertionError("Unsupported arguments must not invoke a renderer")

    monkeypatch.setattr(register, "eightbit_call", unexpected_call)
    monkeypatch.setattr(register, "rgb_call", unexpected_call)

    assert register() == ""
    assert register(1, 2) == ""
    assert register(1, 2, 3, 4) == ""

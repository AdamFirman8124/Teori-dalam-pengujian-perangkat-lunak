# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

from sty.primitive import Register


def test_call_when_muted_returns_empty(monkeypatch):
    reg = Register()
    monkeypatch.setattr(reg, "is_muted", True)
    assert reg(42) == ""
    assert reg(1, 2, 3) == ""
    assert reg() == ""
    assert reg(1, 2) == ""


def test_call_mute_method_mutes_all_forms():
    reg = Register()
    reg.mycolor = "VALUE"
    try:
        reg.mute()
        assert reg.is_muted is True
        assert reg(42) == ""
        assert reg("mycolor") == ""
        assert reg(1, 2, 3) == ""
        assert reg() == ""
    finally:
        reg.unmute()
    assert reg.is_muted is False


def test_single_int_delegates_to_eightbit_call(monkeypatch):
    reg = Register()
    # default eightbit_call is identity
    assert reg(42) == 42

    calls = {}

    def fake_eightbit(x, *args, **kwargs):
        calls["x"] = x
        calls["args"] = args
        calls["kwargs"] = kwargs
        return "EIGHTBIT:%r" % (x,)

    monkeypatch.setattr(reg, "eightbit_call", fake_eightbit)
    assert reg.is_muted is False
    result = reg(99)
    assert result == "EIGHTBIT:99"
    assert calls["x"] == 99

    def fake_eightbit_kw(x, suffix=""):
        return "EIGHTBIT:%r%s" % (x, suffix)

    monkeypatch.setattr(reg, "eightbit_call", fake_eightbit_kw)
    assert reg(7, suffix="!") == "EIGHTBIT:7!"


def test_single_str_returns_matching_attribute():
    reg = Register()
    reg.mycolor = "MYCOLOR_VALUE"
    assert reg("mycolor") == "MYCOLOR_VALUE"
    # getattr path returns whatever attribute holds
    reg.other = "OTHER"
    assert reg("other") == "OTHER"


def test_three_args_delegates_to_rgb_call(monkeypatch):
    reg = Register()
    # default rgb_call returns tuple
    assert reg(10, 20, 30) == (10, 20, 30)

    calls = {}

    def fake_rgb(r, g, b, *args, **kwargs):
        calls["r"] = r
        calls["g"] = g
        calls["b"] = b
        calls["kwargs"] = kwargs
        return "RGB:%r,%r,%r" % (r, g, b)

    monkeypatch.setattr(reg, "rgb_call", fake_rgb)
    result = reg(1, 2, 3)
    assert result == "RGB:1,2,3"
    assert (calls["r"], calls["g"], calls["b"]) == (1, 2, 3)

    def fake_rgb_kw(r, g, b, sep=","):
        return sep.join([str(r), str(g), str(b)])

    monkeypatch.setattr(reg, "rgb_call", fake_rgb_kw)
    assert reg(4, 5, 6, sep=";") == "4;5;6"


def test_invalid_arg_counts_return_empty():
    reg = Register()
    assert reg() == ""
    assert reg(1, 2) == ""
    assert reg(1, 2, 3, 4) == ""
    assert reg(1, 2, 3, 4, 5) == ""

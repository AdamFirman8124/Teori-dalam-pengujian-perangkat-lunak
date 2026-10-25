# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

import sty.primitive as primitive_module
from sty.primitive import Register, Style


def _make_style():
    try:
        return Style("dummy-rule")
    except Exception:
        try:
            return Style()
        except Exception:
            obj = object.__new__(Style)
            obj.rules = ()
            try:
                obj.value = ""
            except Exception:
                pass
            return obj


def _rendered_of(style):
    if hasattr(style, "value"):
        return style.value
    return str(style)


def test_unmute_clears_flag_and_rerenders_style(monkeypatch):
    monkeypatch.setattr(
        primitive_module,
        "_render_rules",
        lambda renderfuncs, rules: ("RENDERED", tuple(rules)),
    )
    r = Register()
    r.sample = _make_style()
    expected_rules = tuple(r.sample.rules)

    r.mute()
    assert r.is_muted is True
    assert isinstance(r.sample, Style)
    assert _rendered_of(r.sample) == ""

    r.unmute()
    assert r.is_muted is False
    assert isinstance(r.sample, Style)
    assert tuple(r.sample.rules) == expected_rules
    assert _rendered_of(r.sample) == "RENDERED"
    # non-Style attributes are preserved / ignored by the loop
    assert isinstance(r.renderfuncs, dict)
    assert r.eightbit_call is not None


def test_unmute_without_prior_mute_still_loops(monkeypatch):
    monkeypatch.setattr(
        primitive_module,
        "_render_rules",
        lambda renderfuncs, rules: ("UNMUTED-VAL", tuple(rules)),
    )
    r = Register()
    r.extra = _make_style()
    r.plain = "not-a-style"
    expected_rules = tuple(r.extra.rules)

    assert r.is_muted is False
    r.unmute()

    assert r.is_muted is False
    assert isinstance(r.extra, Style)
    assert tuple(r.extra.rules) == expected_rules
    assert _rendered_of(r.extra) == "UNMUTED-VAL"
    assert r.plain == "not-a-style"

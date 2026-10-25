# file: project/sty/primitive.py:78-91
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

from sty.primitive import Register
try:
    from sty.primitive import Style
except ImportError:
    try:
        from sty.style import Style
    except ImportError:
        from sty import Style


def test_setattr_muted_empty_rules_covers_line_83():
    reg = Register()
    reg.mute()
    assert reg.is_muted is True
    original = Style(value="should-be-discarded")
    reg.my_style = original
    stored = reg.my_style
    assert isinstance(stored, Style)
    assert str(stored) == ""
    assert stored.rules == ()
    assert stored is not original
    assert str(original) == "should-be-discarded"


def test_setattr_muted_preserves_rules_covers_line_83():
    reg = Register()
    reg.is_muted = True
    assert reg.is_muted is True
    sentinel1 = object()
    sentinel2 = object()
    original = Style(sentinel1, sentinel2, value="rendered-value")
    reg.custom = original
    stored = reg.custom
    assert isinstance(stored, Style)
    assert str(stored) == ""
    assert len(stored.rules) == 2
    assert stored.rules[0] is sentinel1
    assert stored.rules[1] is sentinel2
    assert stored is not original


def test_mute_rerenders_existing_style_covers_line_83():
    reg = Register()
    assert reg.is_muted is False
    object.__setattr__(reg, "preexisting", Style(value="non-empty"))
    assert isinstance(reg.preexisting, Style)
    assert str(reg.preexisting) == "non-empty"
    reg.mute()
    assert reg.is_muted is True
    assert isinstance(reg.preexisting, Style)
    assert str(reg.preexisting) == ""
    assert reg.preexisting.rules == ()

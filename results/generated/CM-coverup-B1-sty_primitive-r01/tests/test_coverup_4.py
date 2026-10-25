# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

from sty.primitive import Register, Style


def test_unmute_after_mute_resets_flag_and_reapplies_style_attributes():
    register = Register()
    try:
        register.accent = Style()
        assert isinstance(register.accent, Style)

        register.mute()
        assert register.is_muted is True
        assert isinstance(register.accent, Style)

        register.unmute()

        assert register.is_muted is False
        assert isinstance(register.accent, Style)
        # The register must be usable again after unmuting.
        register.second = Style()
        assert isinstance(register.second, Style)
    finally:
        del register


def test_unmute_visits_all_style_attributes_and_is_idempotent():
    register = Register()
    try:
        register.first = Style()
        register.second = Style()
        register.third = Style()
        for name in ("first", "second", "third"):
            assert isinstance(getattr(register, name), Style)

        register.mute()
        assert register.is_muted is True

        register.unmute()
        assert register.is_muted is False
        for name in ("first", "second", "third"):
            assert isinstance(getattr(register, name), Style)

        # Calling unmute again must be harmless and keep the flag cleared.
        register.unmute()
        assert register.is_muted is False
        for name in ("first", "second", "third"):
            assert isinstance(getattr(register, name), Style)
    finally:
        del register


def test_unmute_without_style_attributes_only_clears_flag():
    register = Register()
    try:
        register.mute()
        assert register.is_muted is True

        register.unmute()

        assert register.is_muted is False
        assert register.renderfuncs == {}
        assert register.eightbit_call("sentinel") == "sentinel"
        assert register.rgb_call(1, 2, 3) == (1, 2, 3)
    finally:
        del register


def test_unmute_on_never_muted_register_keeps_styles_intact():
    register = Register()
    try:
        register.bold = Style()
        assert isinstance(register.bold, Style)
        assert register.is_muted is False

        register.unmute()

        assert register.is_muted is False
        assert isinstance(register.bold, Style)
        register.bold = Style()
        assert isinstance(register.bold, Style)
    finally:
        del register

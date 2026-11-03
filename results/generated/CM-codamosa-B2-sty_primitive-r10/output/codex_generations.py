

# Generated at 2026-11-03 05:58:05.000080
# Unit test for method mute of class Register
def test_Register_mute():
    from sty import Register, Style
    from sty.rendertype import Sgr

    # Create a register with a render-function and a custom style-attribute.
    r = Register()
    r.set_renderfunc(Sgr, lambda code: "\x1b[%sm" % code)

    rule = Sgr(34)
    r.blue = Style(rule, value="\x1b[34m")

    # Sanity check: before muting, the style renders normally.
    assert str(r.blue) == "\x1b[34m"

    # Mute the register.
    r.mute()

    # The mute flag must be set.
    assert r.is_muted is True

    # All existing style-attributes should render as empty strings now...
    assert str(r.blue) == ""
    # ...but their styling rules should be preserved.
    assert r.blue.rules == (rule,)

    # New styles assigned while muted are rendered as empty strings as well.
    r.red = Style(Sgr(31))
    assert str(r.red) == ""

    # Direct calls on a muted register return an empty string.
    assert r(42) == ""          # 8bit call
    assert r(10, 20, 30) == ""  # rgb call
    assert r("blue") == ""      # attribute call

# Generated at 2026-11-03 06:00:33.611436
# Unit test for method copy of class Register

# Generated at 2026-11-03 06:01:35.429088
# Unit test for method copy of class Register
def test_Register_copy():reg = Register()

# Generated at 2026-11-03 06:02:58.779910
# Unit test for constructor of class Style
def test_Style():
    """
    Test the constructor of the Style class.
    """
    # Test with no rules and no value
    style = Style()
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert str(style) == ""
    assert style.rules == ()

    # Test with a single rule and no value
    rule = "Sgr(1)"
    style = Style(rule)
    assert style.rules == (rule,)
    assert str(style) == ""

    # Test with multiple rules and no value
    rule1, rule2 = "RgbFg(1, 5, 10)", "Sgr(1)"
    style = Style(rule1, rule2)
    assert style.rules == (rule1, rule2)
    assert str(style) == ""

    # Test with a value only
    style = Style(value="\x1b[38;2;1;5;10m")
    assert str(style) == "\x1b[38;2;1;5;10m"
    assert style.rules == ()

    # Test with rules and a value
    style = Style(rule1, rule2, value="\x1b[38;2;1;5;10m\x1b[1m")
    assert style.rules == (rule1, rule2)
    assert str(style) == "\x1b[38;2;1;5;10m\x1b[1m"

    # Test that Style instances are independent (rules are not shared)
    style1 = Style(rule1)
    style2 = Style(rule2)
    assert style1.rules == (rule1,)
    assert style2.rules == (rule2,)

    # Test that Style behaves like a str
    style = Style(rule1, value="orange")
    assert style == "orange"
    assert style.upper() == "ORANGE"
    assert len(style) == 6

# Generated at 2026-11-03 06:04:19.271429
# Unit test for method __new__ of class Style
def test_Style___new__():
    from sty.register import Style

    # Test creating a Style instance with a value and no rules
    style = Style(value="hello")
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert str(style) == "hello"
    assert style.rules == ()

    # Test creating a Style instance with rules and a value
    rule1 = "rule1"
    rule2 = "rule2"
    style2 = Style(rule1, rule2, value="world")
    assert isinstance(style2, Style)
    assert isinstance(style2, str)
    assert str(style2) == "world"
    assert style2.rules == (rule1, rule2)

    # Test creating a Style instance with rules but no value
    style3 = Style(rule1)
    assert str(style3) == ""
    assert style3.rules == (rule1,)

    # Test creating a Style instance with no arguments
    style4 = Style()
    assert str(style4) == ""
    assert style4.rules == ()

# Generated at 2026-11-03 06:05:48.562705
# Unit test for method mute of class Register
def test_Register_mute():
    from sty.register import Register, Style
    from sty.rendertype import RgbFg, Sgr

    register = Register()

    # Setup render functions
    register.set_renderfunc(RgbFg, lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m")
    register.set_renderfunc(Sgr, lambda *codes: f"\x1b[{';'.join(map(str, codes))}m")

    # Assign a style; it should be rendered normally before muting
    register.orange = Style(RgbFg(1, 2, 3), Sgr(1))
    assert isinstance(register.orange, Style)
    assert str(register.orange) == "\x1b[38;2;1;2;3m\x1b[1m"

    # Mute the register
    register.mute()

    # The mute flag is set
    assert register.is_muted is True

    # Existing styles are re-rendered as empty strings, but rules are preserved
    assert str(register.orange) == ""
    assert register.orange.rules == (RgbFg(1, 2, 3), Sgr(1))

    # New styles assigned while muted are also rendered as empty strings
    register.blue = Style(RgbFg(4, 5, 6))
    assert isinstance(register.blue, Style)
    assert str(register.blue) == ""

    # Direct calls on a muted register return an empty string
    assert register(42) == ""
    assert register(1, 2, 3) == ""
    assert register("orange") == ""

    # Non-style attributes are unaffected by muting
    assert register.is_muted is True
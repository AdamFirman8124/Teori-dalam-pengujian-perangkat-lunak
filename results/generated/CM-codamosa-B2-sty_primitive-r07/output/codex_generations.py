

# Generated at 2026-11-02 11:04:58.216538
# Unit test for method unmute of class Register
def test_Register_unmute():
    class FakeRenderType(RenderType):
        def __init__(self, *args):
            self.args = args

    def render_func(*args):
        return "<" + ",".join(str(a) for a in args) + ">"

    reg = Register()
    reg.set_renderfunc(FakeRenderType, render_func)

    # Assign a style attribute; it should be rendered immediately.
    reg.rose = Style(FakeRenderType(1, 2, 3))
    assert isinstance(reg.rose, Style)
    assert str(reg.rose) == "<1,2,3>"

    # Mute the register: styles are re-rendered to empty strings.
    reg.mute()
    assert reg.is_muted is True
    assert str(reg.rose) == ""

    # Unmute: is_muted is False and all styles are rendered again.
    reg.unmute()
    assert reg.is_muted is False
    assert str(reg.rose) == "<1,2,3>"

    # String lookup returns the unmuted (rendered) style.
    assert str(reg("rose")) == "<1,2,3>"

# Generated at 2026-11-02 11:05:53.579871
# Unit test for constructor of class Style
def test_Style():
    # Test constructor without any rules and default value
    s = Style()
    assert isinstance(s, Style)
    assert isinstance(s, str)
    assert s == ""
    assert s.rules == ()

    # Test constructor with a value but without rules
    s = Style(value="some value")
    assert isinstance(s, Style)
    assert isinstance(s, str)
    assert s == "some value"
    assert s.rules == ()

    # Test constructor with rules but without a value
    rule1 = Style(value="rule1")
    rule2 = Style(value="rule2")
    s = Style(rule1, rule2)
    assert isinstance(s, Style)
    assert isinstance(s, str)
    assert s == ""
    assert s.rules == (rule1, rule2)
    assert s.rules[0] is rule1
    assert s.rules[1] is rule2

    # Test constructor with rules and a value
    s = Style(rule1, rule2, value="rendered")
    assert isinstance(s, Style)
    assert isinstance(s, str)
    assert s == "rendered"
    assert s.rules == (rule1, rule2)
    assert s.rules[0] is rule1
    assert s.rules[1] is rule2

# Generated at 2026-11-02 11:07:03.105099
# Unit test for constructor of class Style
def test_Style():
    # No arguments: empty string, no rules
    style = Style()
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert style == ""
    assert style.rules == ()

    # Only a value: string content is stored, rules are empty
    style = Style(value="\x1b[31m")
    assert isinstance(style, Style)
    assert style == "\x1b[31m"
    assert style.rules == ()

    # Rules plus value: rules are stored as a tuple in the .rules attribute
    rule1 = "Sgr(1)"
    rule2 = "RgbFg(1, 2, 3)"
    style = Style(rule1, rule2, value="styled")
    assert isinstance(style, Style)
    assert style == "styled"
    assert style.rules == (rule1, rule2)
    assert len(style.rules) == 2

    # Arbitrary objects (e.g. RenderType-like instances) can be stored as rules
    class DummyRule:
        pass

    dummy = DummyRule()
    style = Style(dummy, value="x")
    assert style == "x"
    assert style.rules == (dummy,)

    # A Style instance can itself be used as a rule (nesting)
    inner = Style(value="inner")
    outer = Style(inner, value="outer")
    assert outer == "outer"
    assert outer.rules == (inner,)

    # Style behaves like a normal string
    style = Style(value="abc")
    assert style.upper() == "ABC"
    assert len(style) == 3
    assert style + "def" == "abcdef"

# Generated at 2026-11-02 11:07:56.727216
# Unit test for method copy of class Register
def test_Register_copy():
    reg = Register()
    reg.red = "foo"
    reg.is_muted = False

    copied_reg = reg.copy()

    # The copy should be a new object, not a reference to the original.
    assert copied_reg is not reg
    assert isinstance(copied_reg, Register)

    # All attributes should be copied over.
    assert copied_reg.red == "foo"
    assert copied_reg.is_muted is False

    # The copy should be a deepcopy: mutating the original
    # must not affect the copy.
    reg.red = "bar"
    reg.is_muted = True

    assert copied_reg.red == "foo"
    assert copied_reg.is_muted is False

    # The renderfuncs dict should be deep-copied as well.
    reg2 = Register()
    reg2.renderfuncs = {int: str}
    copied2 = reg2.copy()

    assert copied2.renderfuncs == reg2.renderfuncs
    assert copied2.renderfuncs is not reg2.renderfuncs

# Generated at 2026-11-02 11:08:18.956492
# Unit test for constructor of class Register
def test_Register():
    """
    Unit test for the constructor of the Register class.

    Verifies that a newly created Register instance initializes its
    attributes with the expected default values.
    """
    register = Register()

    # renderfuncs should be initialized as an empty dict
    assert isinstance(register.renderfuncs, dict)
    assert register.renderfuncs == {}

    # A new register should not be muted
    assert register.is_muted is False

    # eightbit_call should be a callable that echoes a single int input
    assert callable(register.eightbit_call)
    assert register.eightbit_call(42) == 42

    # rgb_call should be a callable that returns its three inputs as a tuple
    assert callable(register.rgb_call)
    assert register.rgb_call(1, 2, 3) == (1, 2, 3)

# Generated at 2026-11-02 11:11:04.382242
# Unit test for method set_renderfunc of class Register

# Generated at 2026-11-02 11:13:14.729959
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():from sty.register import Register, Style
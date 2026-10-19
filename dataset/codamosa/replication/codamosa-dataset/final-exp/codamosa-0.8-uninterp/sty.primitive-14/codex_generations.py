

# Generated at 2022-06-14 08:20:58.819105
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    reg = Register()
    reg.set_eightbit_call(RenderType)
    assert reg.eightbit_call == RenderType.eightbit_render
    assert reg.eightbit_call(144) == RenderType.eightbit_render(144)


# Generated at 2022-06-14 08:21:05.896350
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    fg = Register()
    r = RenderType("RgbFg")

    def render_rgb_fg(r, g, b):
        return "rgb({}, {}, {})".format(r, g, b)

    fg.set_eightbit_call(r)
    fg.set_renderfunc(r, render_rgb_fg)

    fg.red = Style(r(255, 0, 0))

    assert fg(1, 2, 3) == "rgb(1, 2, 3)"
    assert fg("red") == fg.red


# Generated at 2022-06-14 08:21:09.033234
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    fg = Register()

    assert(fg.eightbit_call == fg.eightbit_call)

    fg.set_eightbit_call(RgbFg)

    assert(fg.eightbit_call == fg.renderfuncs[RgbFg])


# Generated at 2022-06-14 08:21:19.724822
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    class EightBit(RenderType):
        def __init__(self, number: int) -> None:
            self.args: Tuple[int] = (number,)

    class CustomRenderFunc:
        @staticmethod
        def eightbit(number: int) -> str:
            return f"\x1b[38;5;{number}m"

    r = Register()

    assert r.eightbit_call(42) == ""

    r.set_renderfunc(EightBit, CustomRenderFunc.eightbit)

    r.set_eightbit_call(EightBit)

    assert r.eightbit_call(42) == "\x1b[38;5;42m"


# Generated at 2022-06-14 08:21:29.469187
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    from .color import Color

    color = Color()
    color.fg.set_eightbit_call(color.fg.RgbFg)
    assert color.fg(13) == '\x1b[38;2;19;19;19m'
    assert color.fg(144) == '\x1b[38;2;128;128;128m'
    assert color.fg(0) == '\x1b[38;2;0;0;0m'
    assert color.fg(255) == '\x1b[38;2;255;255;255m'



# Generated at 2022-06-14 08:21:37.694470
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    from .rendertype import RgbBg, EightBitBg
    from .color import Color

    light_blue = Color(102, 49, 42)

    reg = Register()
    reg.set_eightbit_call(RgbBg)
    default_call = reg.eightbit_call

    # Test default
    assert default_call == reg.rgb_call

    # Test change
    reg.set_eightbit_call(EightBitBg)

    assert reg.eightbit_call != default_call

    assert reg.eightbit_call(light_blue) == "\x1b[48;5;61m"



# Generated at 2022-06-14 08:21:45.939040
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .renderattr import RgbFg

    class MockRegister(Register):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.set_renderfunc(RgbFg, lambda r, g, b: (r, g, b))

    r = MockRegister()
    r.set_eightbit_call(RgbFg)
    assert r.eightbit_call == RgbFg



# Generated at 2022-06-14 08:21:52.255123
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    """
    Test method set_eightbit_call.
    """
    import sty
    sty.register_renderfuncs(fg=lambda i: "fg", bg=lambda i: "bg")

    r = Register()
    r.set_eightbit_call(fg)

    assert str(r(144)) == "fg"


# Generated at 2022-06-14 08:21:59.996474
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    """
    Test set_eightbit_call method of register class.
    """

    def render_test(x):
        return "\x1b[%sm" % x

    new_register = Register()
    new_register.set_renderfunc(RenderType.EIGHTBIT, render_test)
    new_register.set_eightbit_call(RenderType.EIGHTBIT)

    assert new_register(144) == "\x1b[144m"

# Generated at 2022-06-14 08:22:03.309465
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    # Define custom renderfunc
    def render_test(*args, **kwargs):
        return

    register = Register()

    # Set renderfunc for Eightbit-calls
    register.set_eightbit_call(RenderType)
    assert register.eightbit_call == RenderType

    # Set custom render-func for Eightbit-calls
    register.set_renderfunc(RenderType, render_test)
    assert register.eightbit_call == render_test



# Generated at 2022-06-14 08:22:11.582579
# Unit test for constructor of class Register
def test_Register():
    assert Register()

# Generated at 2022-06-14 08:22:16.926609
# Unit test for method __new__ of class Style
def test_Style___new__():

    from .rendertype import Sgr, RgbFg

    rules = [Sgr(1), RgbFg(1, 2, 3)]

    actual = Style(*rules)
    expected = Style(Sgr(1), RgbFg(1, 2, 3), value="")

    assert actual == expected



# Generated at 2022-06-14 08:22:26.951232
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """
    Unit test for method set_renderfunc of class Register.
    """

    class RgbFgTest:
        """
        A class that implements rendertype RgbFg to test renderfunc setter.
        """

        def __init__(self, r, g, b):
            self.r = r
            self.g = g
            self.b = b

    f = lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m"
    register = Register()
    register.set_renderfunc(RgbFgTest, f)

    assert register.renderfuncs[RgbFgTest] == f

    test_style = Style(RgbFgTest(42, 0, 255))
    register.test_style = test_style


# Generated at 2022-06-14 08:22:36.879606
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertype import Sgr, RgbFg

    from .register import Register
    from .rendertype import Rgb

    r = Register()
    r.set_renderfunc(Sgr, lambda *_: "\x1b[1m")
    r.set_renderfunc(
        RgbFg,
        lambda r, g, b: "\x1b[38;2;{};{};{}m".format(r, g, b),
    )

    # Change default color call method to RgbFg
    r.set_rgb_call(RgbFg)

    r.red = Style(Rgb(10, 20, 30))
    r.red2 = Style(RgbFg(10, 20, 30))

# Generated at 2022-06-14 08:22:47.251936
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from .rendertype import RgbFg, RgbBg, Sgr
    from .render import render_seq
    from . import fg, bg

    # set render function for rgb-fg
    fg.set_renderfunc(RgbFg, render_seq)
    bg.set_renderfunc(RgbBg, render_seq)

    # set style attributes
    fg.red = Style(RgbFg(255, 0, 0))
    bg.red = Style(RgbBg(255, 0, 0))

    # Create attributes (equal to Style-instance but without values)
    fg.orange = Style(RgbFg(255, 100, 0))
    bg.orange = Style(RgbBg(255, 100, 0))

    # Change attribute (add Sgr object)
   

# Generated at 2022-06-14 08:22:59.745359
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    Register()

    class TakenRenderType(RenderType):
        pass

    class TakenName(str):
        pass

    class MyRegister(Register):
        default = Style(TakenRenderType())

    r = MyRegister()

    # Setting a name that is already taken as a attribute name (not Style).
    with pytest.raises(ValueError) as e:
        r.default = Style(TakenRenderType())
        assert "taken" in str(e)
        assert "default" in str(e)

    # Setting a name that is already taken as a Style attribute name.
    with pytest.raises(ValueError) as e:
        r.another_name = Style(TakenRenderType())
        assert "taken" in str(e)

    # Setting a name that is already taken as a render type.

# Generated at 2022-06-14 08:23:13.857051
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import RgbFg, Sgr

    def _render_rgb_fg(r: int, g: int, b: int) -> str:
        return '\x1b[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'

    def _render_sgr(code: int) -> str:
        return '\x1b[' + str(code) + 'm'

    # Create register-object.
    fg = Register()

    # Create renderfuncs and connect each to a rendertype.
    fg.renderfuncs.update({RgbFg: _render_rgb_fg})
    fg.renderfuncs.update({Sgr: _render_sgr})

    # Define rendertype for RGB-c

# Generated at 2022-06-14 08:23:22.166539
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    ############################################################################
    # 1st test

    reg = Register()
    reg.set_renderfunc(RenderType, lambda *args: ("",))
    reg.set_rgb_call(RenderType)
    reg.set_eightbit_call(RenderType)
    reg.green = Style(RenderType(), "green")

    # Check if we can access style attributes as usual
    assert hasattr(reg, "green")
    assert reg.green == "green"

    # Check if calling the register-object works
    assert reg(2) == ("",)
    assert reg(99) == ("",)
    assert reg(0, 0, 0) == ("",)

    ############################################################################
    # 2st test

    reg = Register()

# Generated at 2022-06-14 08:23:31.051353
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import Rgb, RgbFg, RgbBg

    r = Register()
    r.set_rgb_call(RgbFg) # (10, 20, 30) -> (10, 20, 30)
    assert r(10, 20, 30) == (10, 20, 30)
    r.set_rgb_call(RgbBg) # (10, 20, 30) -> (30, 20, 10)
    assert r(10, 20, 30) == (30, 20, 10)



# Generated at 2022-06-14 08:23:39.711589
# Unit test for method copy of class Register
def test_Register_copy():
    """
    Unit test for method copy of class Register.

    Returns
    -------
    bool
        True if test passed, False if test fails.
    """

    r1 = Register()
    r1.a = "test"
    r1.b = "test2"
    r2 = r1.copy()

    if r1.a != r2.a:
        return False

    if r1.b != r2.b:
        return False

    r1.a = "changed"

    if r1.a == r2.a:
        return False

    return True

# Generated at 2022-06-14 08:23:49.774290
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    from sty import fg
    from collections import namedtuple

    assert isinstance(fg.red, Style)
    assert isinstance(fg.red, str)

    d = fg.as_dict()
    assert isinstance(d, dict)
    assert "red" in d.keys()
    assert isinstance(d["red"], str)

    nt = fg.as_namedtuple()
    assert isinstance(nt, namedtuple)
    assert "red" in nt._fields
    assert isinstance(getattr(nt, "red"), str)

# Generated at 2022-06-14 08:23:56.746208
# Unit test for method __new__ of class Style
def test_Style___new__():
    style = Style(RgbFg(1,2,3), RgbBg(4,5,6), Sgr(7))
    assert str(style) == "\x1b[38;2;1;2;3m\x1b[48;2;4;5;6m\x1b[7m"
    assert isinstance(style, Style)
    assert isinstance(style, str)

# Generated at 2022-06-14 08:24:05.736206
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class RgbFg(RenderType):

        def __init__(self, *args):
            super().__init__(*args)

    class Sgr(RenderType):

        def __init__(self, *args):
            super().__init__(*args)

    def render_rgb_fg(r: int, g: int, b: int) -> str:
        return f"\033[38;2;{r};{g};{b}m"

    def render_sgr(sgr: int) -> str:
        return f"\033[{sgr}m"

    fg = Register()
    fg.set_renderfunc(RgbFg, render_rgb_fg)
    fg.set_renderfunc(Sgr, render_sgr)


# Generated at 2022-06-14 08:24:15.641417
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    r = Register()
    r.red = Style(RgbFg(255, 0, 0))
    r.blue = Style(RgbFg(0, 0, 255))
    r.green = Style(RgbFg(0, 255, 0))
    r.yellow = Style(RgbFg(255, 255, 0))
    r.white = Style(RgbFg(255, 255, 255))

    t = r.as_namedtuple()

    assert t.red == r.red
    assert t.blue == r.blue
    assert t.green == r.green
    assert t.yellow == r.yellow
    assert t.white == r.white



# Generated at 2022-06-14 08:24:25.289523
# Unit test for method unmute of class Register
def test_Register_unmute():

    def renderfunc(B, *args):
        return f"\x1b[{B}m"

    from .rendertype import B
    from .rendertype import Sgr

    register = Register()

    register.set_renderfunc(B, renderfunc)
    register.set_eightbit_call(B)

    register.test = Style(B(10), Sgr(1), Sgr(0))
    register.test2 = Style(B(20), Sgr(1), Sgr(0))

    register.mute()

    assert str(register.test) == ""
    assert str(register.test2) == ""

    register.unmute()

    assert str(register.test) == "\x1b[10m\x1b[1m\x1b[0m"

# Generated at 2022-06-14 08:24:38.021241
# Unit test for method __new__ of class Style
def test_Style___new__():
    """
    Test converting kwargs to StylingRule.
    """
    # Test 1: 
    Style.__new__(Style, RgbFg(1, 2, 3), value="")
    Style.__new__(Style, Sgr(1), value="")
    Style.__new__(Style, Sgr(1), RgbFg(1, 2, 3), value="")

    # Test 2:
    Style.__new__(Style, RgbFg(1, 2, 3), Sgr(1))
    Style.__new__(Style, Sgr(1), Sgr(2))
    Style.__new__(Style, Sgr(1), RgbFg(1, 2, 3), Sgr(0))

    # Test 3:

# Generated at 2022-06-14 08:24:51.499505
# Unit test for method __call__ of class Register
def test_Register___call__():

    import re
    from sty.types import RgbFg, RgbBg, RgbEf

    def r_rgb(r, g, b) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    def r_8bit(v) -> str:
        return f"\x1b[38;5;{v}m"

    red = Register()
    red_dark = Register()
    red.set_eightbit_call(RgbFg)
    red.set_rgb_call(RgbFg)
    red.set_renderfunc(RgbFg, r_rgb)
    red.set_renderfunc(RgbBg, r_rgb)

# Generated at 2022-06-14 08:25:04.395752
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertype import EightbitBg, EightbitFg, RgbBg, RgbFg
    from .styles import fg, bg

    assert fg(5) == "\x1b[38;5;5m"
    assert fg(42) == "\x1b[38;5;42m"
    assert fg(11, 22, 33) == "\x1b[38;2;11;22;33m"
    assert fg(red=11, green=22, blue=33) == "\x1b[38;2;11;22;33m"
    assert fg("red") == "\x1b[38;2;255;0;0m"

    assert bg(5) == "\x1b[48;5;5m"

# Generated at 2022-06-14 08:25:14.651211
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertype import EightBit, RgbFg, Sgr
    from .utils import ansi_len

    register = Register()
    register.set_eightbit_call(RgbFg)
    register.set_rgb_call(EightBit)

    def fg_rgb(r: int, g: int, b: int) -> str:
        return f"\033[38;2;{r};{b};{g}m"

    def fg_sgr(code: int) -> str:
        return f"\033[38;5;{code}m"

    def bg_rgb(r: int, g: int, b: int) -> str:
        return f"\033[48;2;{r};{b};{g}m"


# Generated at 2022-06-14 08:25:23.089732
# Unit test for method __call__ of class Register
def test_Register___call__():

    # Make a new Register-object
    r = Register()

    # Add eightbit rendertype
    r.set_renderfunc(RenderType.Eightbit, lambda x: f"\x1b[48;5;{x}m")

    # Add attribute with Style-object.
    r.yellow = Style(RenderType.Eightbit(3))

    # Evaluate the Style-object.
    yellow = r.yellow

    # Check if yellow is a Style-object.
    assert isinstance(yellow, Style)

    # Check if yellow is a str-object.
    assert isinstance(yellow, str)

    # Check if yellow is the right ANSI-sequence.
    assert yellow == "\x1b[48;5;3m"

    # Check if calling the register with an int works.

# Generated at 2022-06-14 08:25:43.011659
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    from .simple import fg, bg
    assert fg.red == "\x1b[38;2;255;0;0m"
    assert fg.green == "\x1b[38;2;0;255;0m"
    fg.blue = Style(RgbFg(0, 0, 255))
    assert fg.blue == "\x1b[38;2;0;0;255m"
    c8 = fg.copy()
    c8.set_eightbit_call(Eightbit)
    c8.red_eightbit = Style(Eightbit(1))
    assert c8.red_eightbit == "\x1b[31m"
    c8_dict = c8.as_dict()
    assert c8_dict["red_eightbit"] == "\x1b[31m"

# Generated at 2022-06-14 08:25:46.828895
# Unit test for method copy of class Register
def test_Register_copy():
    """Deepcopy of register-object should not have any reference
    to the orignary object."""
    r = Register()
    r2 = r.copy()
    assert not r is r2
    assert r.__dict__ is not r2.__dict__


# Generated at 2022-06-14 08:25:58.249047
# Unit test for method copy of class Register
def test_Register_copy():

    def test_dicts(d1: Dict[str, str], d2: Dict[str, str]) -> None:

        for key1, value1 in d1.items():

            value2 = d2[key1]
            assert value1 == value2

    from . import sty

    sty_dict = sty.as_dict()
    sty_tuple = sty.as_namedtuple()

    sty_copy_dict = sty.copy().as_dict()
    sty_copy_tuple = sty.copy().as_namedtuple()

    test_dicts(sty_dict, sty_copy_dict)
    test_dicts(sty_tuple._asdict(), sty_copy_tuple._asdict())

# Generated at 2022-06-14 08:26:03.409301
# Unit test for constructor of class Style
def test_Style():

    from .sgr import Sgr

    rules = (Sgr(1),)
    value = "\x1b[1m"

    new_style = Style(*rules, value=value)

    assert isinstance(new_style, Style)
    assert isinstance(new_style, str)

    assert value == new_style
    assert rules == new_style.rules

# Generated at 2022-06-14 08:26:06.805615
# Unit test for constructor of class Register
def test_Register():
    """
    Test constuctor of the Register-class.
    """
    r = Register()
    assert r.is_muted == False

# Generated at 2022-06-14 08:26:13.867499
# Unit test for method unmute of class Register
def test_Register_unmute():
    """
    Test_Register_unmute()

    """
    fg = Register()
    fg.black = Style(RgbFg(0, 0, 0), Sgr(0))
    fg.mute()
    assert fg.black == ""
    fg.unmute()
    assert fg.black == "\x1b[39m\x1b[22m"



# Generated at 2022-06-14 08:26:21.454988
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    from .rendertype import RgbFg, Sgr

    class CustomRegister(Register):
        def __init__(self):
            super().__init__()
            self.esc = "\x1b["
            self.rst = Style(RgbFg(0, 0, 0), Sgr(0))
            self.set_eightbit_call(RgbFg)
            self.set_rgb_call(RgbFg)

    c = CustomRegister()
    assert c(144) == "\x1b[38;2;4;4;4m"
    assert c(10, 42, 255) == "\x1b[38;2;10;42;255m"

    # This should not affect the existing styles (including background styles)

# Generated at 2022-06-14 08:26:32.923695
# Unit test for method copy of class Register
def test_Register_copy():
    import pytest

    r1 = Register()

    # Setup
    r1.set_renderfunc(RenderType.EIGHTBIT_FOREGROUND, lambda x: f"\033[38;5;{x}m")
    r1.set_eightbit_call(RenderType.EIGHTBIT_FOREGROUND)

    # Test
    r1.pink = Style(RenderType.EIGHTBIT_FOREGROUND(1))

    r2 = r1.copy()
    assert r2.pink == "\033[38;5;1m"

    r1.pink = Style(RenderType.EIGHTBIT_FOREGROUND(2))
    assert r1.pink == "\033[38;5;2m"
    assert r2.pink == "\033[38;5;1m"


# Generated at 2022-06-14 08:26:40.406327
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    # Setup
    r = Register()
    r.black = Style(RgbFg(0,0,0))
    r.white = Style(RgbFg(100,100,100))

    # Act
    r_d = r.as_dict()

    # Assert
    assert type(r_d) is dict
    assert "black" in r_d
    assert "white" in r_d


# Generated at 2022-06-14 08:26:50.726649
# Unit test for method copy of class Register
def test_Register_copy():
    """
    Unit test for method copy of class Register.
    """
    tmp = Register()
    tmp2 = Register()
    tmp.style1 = Style()
    tmp.style2 = Style()
    tmp2.style3 = Style()
    tmp3 = tmp.copy()
    tmp4 = tmp2.copy()
    assert isinstance(tmp3, Register)
    assert isinstance(tmp4, Register)
    assert hasattr(tmp3, "style1") and hasattr(tmp3, "style2") and not hasattr(tmp3, "style3")
    assert hasattr(tmp4, "style3") and not hasattr(tmp4, "style1") and not hasattr(tmp4, "style2")
    assert not (tmp3.style1 is tmp.style1)

# Generated at 2022-06-14 08:27:03.977133
# Unit test for constructor of class Register
def test_Register():
    reg = Register()
    #  Test if initialisation is working.
    assert reg.renderfuncs == {}
    assert reg.is_muted == False
    assert callable(reg.eightbit_call)

# Generated at 2022-06-14 08:27:07.103207
# Unit test for method unmute of class Register
def test_Register_unmute():

    from sty import fg

    fg.mute()
    assert fg.is_muted == True

    fg.unmute()
    assert fg.is_muted == False



# Generated at 2022-06-14 08:27:19.129135
# Unit test for method copy of class Register
def test_Register_copy():

    from . import fg, rendertype, style

    # Create renderfunc for custom rendertype
    rendertype.add_rendertype(
        name="my_rendertype",
        ansi_format=["\x1b[{}m"],
        renderfunc=lambda x: "\x1b[{}m".format(x),
    )

    # Create new register object
    r = Register()

    # Add a new renderfunc
    r.set_renderfunc(rendertype.my_rendertype, lambda x: "\x1b[{}m".format(x))

    # Add style
    r.red = style.Style(rendertype.my_rendertype(1))

    # Copy register object
    r_copy = r.copy()

    assert r_copy.red == "\x1b[1m"
    assert r_copy

# Generated at 2022-06-14 08:27:20.261496
# Unit test for constructor of class Style
def test_Style():
    assert Style("TEST") == "TEST"

# Generated at 2022-06-14 08:27:31.960393
# Unit test for method mute of class Register
def test_Register_mute():

    # Define register-object
    r1 = Register()

    # Create a StylingRule with a name
    r1.myrule = Style(RgbFg(1, 2, 3), Sgr(1))

    # Create a Style with a name
    r1.mystyle = Style(r1.myrule)

    # Check values
    assert r1.myrule == "\x1b[38;2;1;2;3m\x1b[1m"
    assert r1.mystyle == "\x1b[38;2;1;2;3m\x1b[1m"

    # Mute register
    r1.mute()

    # Check values
    assert r1.myrule == ""
    assert r1.mystyle == ""

    # Unmute register
    r1.unmute

# Generated at 2022-06-14 08:27:33.220019
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r


# Generated at 2022-06-14 08:27:40.066447
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class TestRenderType(RenderType):
        _ANSI = "test"

        def __init__(self, arg1="arg1", arg2="arg2"):
            self.arg1 = arg1
            self.arg2 = arg2

    def test_renderfunc(arg1, arg2):
        return ANSI(arg1 + arg2)

    r = Register()
    r.set_renderfunc(TestRenderType, test_renderfunc)

    r.test = Style(TestRenderType("arg1", "22"))
    assert r.test == ANSI("arg122")


# Generated at 2022-06-14 08:27:48.730009
# Unit test for method mute of class Register
def test_Register_mute():
    register = Register()
    render_func = lambda *args: f"\x1b[38;2;{args[0]};{args[1]};{args[2]}m\x1b[1m"
    register.set_renderfunc(rendertype=RgbFg, func=render_func)
    red = Style(RgbFg(255, 0, 0), Sgr(1))
    setattr(register, "red", red)
    register.mute()

    assert register.red == ""


# Generated at 2022-06-14 08:27:57.043087
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    class MyRegister(Register):
        pass

    rg = MyRegister()
    rg.red = Style(RgbFg(10, 40, 50))
    rg.green = Style(Bold)
    rg.blue = Style(Underlined)
    rg.grey = Style(Bold, RgbBg(10,40,50))

    assert rg.as_dict() == {
        "red": "\x1b[38;2;10;40;50m",
        "green": "\x1b[1m",
        "blue": "\x1b[4m",
        "grey": "\x1b[1m\x1b[48;2;10;40;50m",
    }

# Generated at 2022-06-14 08:28:10.147014
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import RgbFg, TrueColor

    rend1 = Register()
    rend2 = Register()

    rend1.set_renderfunc(RgbFg, lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m")
    rend2.set_renderfunc(TrueColor, lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m")

    # Initialize style with RgbFg
    rend1.red = Style(RgbFg(255, 0, 0), value="\x1b[38;2;255;0;0m")

    # Call style with red rgb code
    rgb_call = rend1(255, 0, 0)
    assert rgb_call == rend1.red

   

# Generated at 2022-06-14 08:28:29.201857
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    class TestRegister(Register):
        def __init__(self):
            super().__init__()
            self.red = Style(RgbFg(255, 0, 0))
            self.green = Style(RgbFg(0, 255, 0))
            self.blue = Style(RgbFg(0, 0, 255))

    # Test if __init__ throws error if some names are missing
    nt = TestRegister().as_namedtuple()
    assert nt.red == "\x1b[38;2;255;0;0m"
    assert nt.green == "\x1b[38;2;0;255;0m"
    assert nt.blue == "\x1b[38;2;0;0;255m"

    # Test if __init__ throws error if some keys are duplicated


# Generated at 2022-06-14 08:28:37.477671
# Unit test for method unmute of class Register
def test_Register_unmute():
    r = Register()
    r.set_eightbit_call(RenderType)
    r.set_rgb_call(RenderType)

    r.reset = Style(RenderType)
    r.test = Style(RenderType)

    assert r.test == ""
    assert r.reset == ""

    r.unmute()

    assert r.test == "\x1b[0m"
    assert r.reset == "\x1b[0m"

# Generated at 2022-06-14 08:28:49.871425
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    # Create register
    r = Register()

    # Define styling rules for register
    r.bold = Style(Sgr(1))
    r.dim = Style(Sgr(2))
    r.black = Style(RgbFg(0, 0, 0))
    r.white = Style(RgbFg(255, 255, 255))
    r.bold_black = Style(r.bold, r.black)
    r.bold_white = Style(r.bold, r.white)
    r.bold_dim_white = Style(r.bold, r.dim, r.white)

    # Run tests
    assert r.bold_dim_white(10, 20, 30) == "\x1b[1m\x1b[2m\x1b[38;2;10;20;30m"

# Generated at 2022-06-14 08:28:58.668604
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .sgr import Sgr
    from .fg import RgbFg

    r = Register()
    setattr(r, "foo", Style(RgbFg(144, 122, 255), Sgr(1)))

    r.set_eightbit_call(RgbFg)
    r.set_rgb_call(RgbFg)

    # Test explicit call.
    assert r("foo") == "\x1b[38;2;144;122;255m\x1b[1m"

    # Test implicit call, 8bit.
    assert r(144) == "\x1b[38;2;144;0;0m"

    # Test implicit call, 24bit
    assert r(144, 122, 255) == "\x1b[38;2;144;122;255m"


# Generated at 2022-06-14 08:29:00.789291
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    register = Register()
    register.blue = Style(Sgr(34))
    register.red = Style(Sgr(31))

    assert register.as_dict() == {"blue": "\033[34m", "red": "\033[31m"}


# Generated at 2022-06-14 08:29:09.951141
# Unit test for method __new__ of class Style
def test_Style___new__():

    class RgbFg(RenderType):
        pass
    class Sgr(RenderType):
        pass

    fg = Register()
    setattr(fg, "rgb_func", lambda *args: "".join([str(arg) for arg in args]))
    fg.set_renderfunc(RgbFg, lambda *args: fg.rgb_func(*args))
    fg.set_renderfunc(Sgr, lambda *args: "".join([str(arg) for arg in args]))

    style = Style(RgbFg(1,2,3), Sgr("1", "2", "3"))

    assert hasattr(style, "rules")
    assert style.rules == (RgbFg(1,2,3), Sgr("1", "2", "3"))


# Generated at 2022-06-14 08:29:14.422881
# Unit test for method copy of class Register
def test_Register_copy():
    r1 = Register()
    r1.set_eightbit_call(RenderType)
    r1.set_rgb_call(RenderType)
    r1.set_renderfunc(RenderType, lambda x: x)
    r1.rs = Style(RenderType)
    r1.name = "Xenia"
    r1.age = 30

    r2 = r1.copy()

    assert r1.__dict__ != r2.__dict__
    assert r1.__dict__ == r2.__dict__



# Generated at 2022-06-14 08:29:21.100559
# Unit test for method copy of class Register
def test_Register_copy():
    register = Register()

    # Add new style
    register.bold = Style(RgbFg(255, 124, 0), Sgr(1))

    # Make copy
    copy = register.copy()

    # Check if copy is a new object.
    assert register is not copy

    # Check if styles are identical.
    assert register.bold == copy.bold

    # Check if styles are different objects.
    assert register.bold is not copy.bold

# Generated at 2022-06-14 08:29:26.979345
# Unit test for method copy of class Register
def test_Register_copy():
    test = Register()
    test.foo = Style(RgbFg(1, 2, 3))
    copied = test.copy()
    assert copied.foo.rules == test.foo.rules
    # Test if copied dict is referential different from original dict.
    assert copied.renderfuncs is not test.renderfuncs

# Generated at 2022-06-14 08:29:30.200910
# Unit test for method mute of class Register
def test_Register_mute():
    import sty

    bg = Register()
    bg.renderfuncs.update({sty.Sgr: lambda *x: "SGR"})
    bg.red = Style(sty.Sgr(1))
    bg.mute()
    assert bg.red == ""
    bg.unmute()
    assert bg.red == "SGR"

# Generated at 2022-06-14 08:29:55.772913
# Unit test for method mute of class Register
def test_Register_mute():

    # Register with two style-rules.
    orig_reg = Register()
    orig_reg.renderfuncs = {int: lambda x: "int", str: lambda x: "str"}
    setattr(orig_reg, "style", Style(1, "foo"))
    orig_reg.set_eightbit_call(int)
    orig_reg.set_rgb_call(str)

    # Make deepcopy to work on.
    reg = orig_reg.copy()

    # Mute and unmute register.
    reg.mute()
    reg.unmute()

    # Check if register has been changed.
    assert orig_reg.eightbit_call == reg.eightbit_call
    assert orig_reg.rgb_call == reg.rgb_call
    assert orig_reg.renderfuncs == reg.renderfun

# Generated at 2022-06-14 08:30:05.178644
# Unit test for method unmute of class Register
def test_Register_unmute():
    """
    If Sty is muted, the registers should ignore the mute-command.

    Idea: Create a Register, mute it and check if the styles are empty strings.
    Then, call Sty.unmute and check if the styles are not empty strings.

    Result: It works.
    """
    rr = Register()
    rr.mute()
    assert str(getattr(rr, "bold")) == ""

    Sty.unmute()
    assert str(getattr(rr, "bold")) != ""
    Sty.mute()

# Generated at 2022-06-14 08:30:18.381456
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .sty import Sty
    from .rendertype import EightBit

    s = Sty()
    r = Register()
    r.renderfuncs = {EightBit: lambda x: x}

    s.set_renderfunc(EightBit, lambda x: x+1)
    r.set_renderfunc(EightBit, lambda x: x+1)

    assert s.cyan == "\x1b[96m"
    assert r.cyan == "\x1b[96m"

    s.mute()
    r.mute()

    assert s.cyan == ""
    assert r.cyan == ""

    s.unmute()
    r.unmute()

    assert s.cyan == "\x1b[96m"
    assert r.cyan == "\x1b[96m"

    # TODO

# Generated at 2022-06-14 08:30:24.794239
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    """
    Test if as_namedtuple() returns a NamedTuple with the same name as the Class.
    """
    reg = Register()
    reg.foo = Style("foo")
    reg.baa = Style("baa")

    assert reg.as_namedtuple() == namedtuple("StyleRegister", "foo baa")("foo", "baa")

# Generated at 2022-06-14 08:30:36.668912
# Unit test for method copy of class Register
def test_Register_copy():
    from .rendertype import Sgr, SgrFg, SgrBg
    from .color import Color
    from .style import Style

    foo = Register()
    foo.set_renderfunc(Sgr, lambda x: "SGR-ANSI")
    foo.set_renderfunc(SgrFg, lambda x: "SGR-ANSI")

    foo.red = Style(SgrFg(41))
    foo.blue = Style(SgrFg(42))
    foo.yellow_bold =  Style(SgrFg(43), Sgr(1))

    _foo = foo.copy()

    assert _foo.red == foo.red
    assert _foo.blue == foo.blue
    assert _foo.yellow_bold == foo.yellow_bold
    assert _foo.renderfuncs == foo.renderfuncs

# Generated at 2022-06-14 08:30:46.824233
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    """
    Create register (fg) and set render-type for 8bit-call to
    ``sty.sgr.SetFg(ansicode)``

        >>> r = Register()
        >>> r.set_eightbit_call(sty.sgr.SetBg)
        >>> test_style = Style(sty.sgr.SetBg(42))
        >>> r.test_style
        '\x1b[48;5;42m'
        >>> r.test_style(5)
        '\x1b[48;5;5m'

    """
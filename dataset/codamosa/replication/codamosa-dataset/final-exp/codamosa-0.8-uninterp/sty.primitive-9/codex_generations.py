

# Generated at 2022-06-14 08:20:53.931524
# Unit test for constructor of class Register
def test_Register():
    rg = Register()
    assert type(rg) is Register


# Generated at 2022-06-14 08:20:57.417089
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()
    setattr(r, "dict", Style("AAA"))
    assert r("dict") == "AAA"
    assert r(1) == ""

# Generated at 2022-06-14 08:21:06.635614
# Unit test for method __call__ of class Register
def test_Register___call__():
    class RegisterMock(Register):
        def __init__(self):
            super().__init__()
            self.rgb_call = lambda r, g, b: (r, g, b)
            self.eightbit_call = lambda x: x
            self.is_muted = False

        def set_eightbit_call(self, rendertype: Type[RenderType]) -> None:
            raise NotImplementedError

        def set_rgb_call(self, rendertype: Type[RenderType]) -> None:
            raise NotImplementedError
    # Test: str-call and int-call
    fg = RegisterMock()
    fg.red = Style()
    fg.set_eightbit_call(None)
    fg.set_rgb_call(None)

    assert fg("red")

# Generated at 2022-06-14 08:21:13.248354
# Unit test for method __call__ of class Register
def test_Register___call__():

    r: Register = Register()

    class RgbFg(RenderType):
        def __str__(self):
            return "RgbFg(r, g, b)"

    class RgbBg(RenderType):
        def __str__(self):
            return "RgbBg(r, g, b)"

    r.set_renderfunc(RgbFg, lambda r, g, b: f"Renderfunc(RgbFg): {r}, {g}, {b}")
    r.set_renderfunc(RgbBg, lambda r, g, b: f"Renderfunc(RgbFg): {r}, {g}, {b}")

    r.red = Style(RgbFg(10, 0, 0))
    r.blue = Style(RgbBg(0, 0, 255))

   

# Generated at 2022-06-14 08:21:16.773951
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r.renderfuncs == {}

# Generated at 2022-06-14 08:21:24.065556
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .core import fg

    rgb_fg = fg.copy()
    rgb_fg.set_rgb_call(RenderType.RGB_FG)

    assert fg(144) == "\x1b[38;5;144m"
    assert rgb_fg(10, 42, 255) == "\x1b[38;2;10;42;255m"

    assert fg(10, 42, 255) == ""
    assert rgb_fg(144) == ""

    class CustomRegister(Register):
        def __call__(self, *args: Union[int, str], **kwargs) -> str:
            return "Custom call result."
    custom = CustomRegister()
    custom.set_renderfunc(RenderType.ANSI, lambda asnsi_code: str(asnsi_code))
    assert custom(42)

# Generated at 2022-06-14 08:21:28.856627
# Unit test for method __call__ of class Register
def test_Register___call__():

    r = Register()
    r.red = Style("\x1b[31m")
    r.yellow = Style("\x1b[33m")

    assert r("red") == "\x1b[31m"
    assert r("yellow") == "\x1b[33m"

# Generated at 2022-06-14 08:21:35.496480
# Unit test for constructor of class Register
def test_Register():
    from .rendertype import Sgr

    class MyRegister(Register):
        def __init__(self):
            super().__init__()
            self.blue = Style(Sgr(34))

    mr = MyRegister()
    mr.set_renderfunc(Sgr, lambda x: f"\x1b[{x}m")
    assert mr.blue == "\x1b[34m"


# Generated at 2022-06-14 08:21:37.484557
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert isinstance(register, Register)

# Generated at 2022-06-14 08:21:45.227880
# Unit test for method __call__ of class Register
def test_Register___call__():

    class _RS(RenderType):
        pass

    register = Register()
    renderfunc = lambda: ""
    rendertype = _RS
    register.set_renderfunc(rendertype, renderfunc)
    register.set_eightbit_call(rendertype)
    assert register("test") == ""
    assert register(1) == ""
    assert register(1, 2) == ""
    assert register(1, 2, 3) == ""



# Generated at 2022-06-14 08:22:08.982009
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .rendertypes import AnsiBg, AnsiFg

    class rgbfg(NamedTuple):
        black: str
        red: str
        green: str
        yellow: str
        blue: str
        magenta: str
        cyan: str
        white: str
        lred: str
        lgreen: str
        lyellow: str
        lblue: str
        lmagenta: str
        lcyan: str
        lwhite: str

    def render_ansifg(code):
        return f"\x1b[38;5;{code}m"

    # Test as_namedtuple

# Generated at 2022-06-14 08:22:17.355684
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class A(RenderType):
        pass

    class B(RenderType):
        pass

    a_func = lambda *args: "a_func"
    b_func = lambda *args: "b_func"

    reg = Register()
    reg.set_renderfunc(A, a_func)
    reg.set_renderfunc(B, b_func)

    assert reg.renderfuncs == {A: a_func, B: b_func}



# Generated at 2022-06-14 08:22:22.337996
# Unit test for method __new__ of class Style
def test_Style___new__():
    s = Style(RgbFg(1, 5, 10), Sgr(1))
    assert isinstance(s, Style)
    assert isinstance(s, str)
    assert str(s) == "\x1b[38;2;1;5;10m\x1b[1m"


# Generated at 2022-06-14 08:22:27.457327
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    # Create a new register and define a color entry
    reg = Register()
    reg.green = Style(RgbFg(0, 255, 0))

    # Create a namedtuple from register
    snt = reg.as_namedtuple()

    # Test attributes for equality
    assert snt.green == "\x1b[38;2;0;255;0m"

# Generated at 2022-06-14 08:22:41.798769
# Unit test for method __call__ of class Register
def test_Register___call__():

    def test_value1(value: Style, eightbit: int, rgb: Tuple[int, int, int], string: str):
        """
        Test function for a RGB-register (eg the fg-register).
        """

        assert value(eightbit) == value
        assert value(rgb) == value
        assert value(string) == value

    def test_value2(value: Style, eightbit: int, string: str):
        """
        Test function for an 8bit-register (eg the ef-register).
        """

        assert value(eightbit) == value
        assert value(string) == value

    def test_register(register: Register):

        test_value1(register.blue, 4, (0, 0, 255), "blue")

# Generated at 2022-06-14 08:22:48.182061
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    """
    Test method as_namedtuple of class Register.
    """
    from . import fg, bg

    nt1 = fg.as_namedtuple()

    assert isinstance(nt1, namedtuple)
    assert hasattr(nt1, "black")
    assert hasattr(nt1, "white")
    assert hasattr(nt1, "red")

    nt2 = bg.as_namedtuple()

    assert isinstance(nt2, namedtuple)
    assert hasattr(nt2, "black")
    assert hasattr(nt2, "white")
    assert hasattr(nt2, "red")

# Generated at 2022-06-14 08:22:49.517594
# Unit test for constructor of class Register
def test_Register():
    assert isinstance(Register, type)



# Generated at 2022-06-14 08:23:00.650879
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class MyRegister(Register):
        pass

    a = MyRegister()
    a.x = "Hello World!"

    assert a.x == "Hello World!"
    assert not isinstance(a.x, Style)

    b = MyRegister()
    b.x = Style(value="Hello World!")

    assert b.x == "Hello World!"
    assert isinstance(b.x, Style)
    assert isinstance(b.x.value, str)
    assert b.x.value == "Hello World!"
    assert isinstance(b.x.rules, tuple)
    assert b.x.rules == ()

    c = MyRegister()
    b.x = Style(value="Hello World!", rules=("Test",))

    assert c.x == "Hello World!"
    assert isinstance(c.x, Style)

# Generated at 2022-06-14 08:23:06.093758
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r.renderfuncs == {}
    assert r.is_muted is False

# Generated at 2022-06-14 08:23:15.065236
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    class MockRegister1(Register):
        def __init__(self):
            super().__init__()
            self.one = Style("1")
            self.two = Style("2")
            self.three = Style("3")
            self.four = Style("4")

    reg = MockRegister1()

    out = reg.as_dict()

    assert out == {'one': '1', 'two': '2', 'three': '3', 'four': '4'}


# Generated at 2022-06-14 08:23:23.152228
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert isinstance(register, Register)



# Generated at 2022-06-14 08:23:29.457098
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    style_reg = Register()
    style_reg.blue = Style(RgbFg(0,0,255))
    style_reg.is_muted = True
    style_reg.red = Style(RgbFg(255,0,0))

    assert style_reg.as_dict() == {"blue": "", "red": ""}



# Generated at 2022-06-14 08:23:33.420425
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .sgr import Sgr

    r = Register()
    r.set_eightbit_call(type(Sgr(1)))

    r.bold = Style(Sgr(1))

    assert r('bold') == r.bold

    r.mute()

    assert r('bold') == ''

# Generated at 2022-06-14 08:23:45.286777
# Unit test for constructor of class Style
def test_Style():
    """ Unit test for constructor of class Style """

    import pytest

    dummy_rgb_fg_renderfunc = lambda r, g, b: (r, g, b)
    dummy_sgr_renderfunc = lambda sgr: sgr

    my_fg = Register()
    my_fg.set_renderfunc(RgbFg, dummy_rgb_fg_renderfunc)
    my_fg.set_renderfunc(Sgr, dummy_sgr_renderfunc)

    my_fg.red = Style(RgbFg(1, 2, 3), Sgr(4))

    assert isinstance(my_fg.red, Style)
    assert (1, 2, 3) == my_fg.red.rules[0].args
    assert 4 == my_fg.red.rules[1].args[0]

# Generated at 2022-06-14 08:23:51.054904
# Unit test for constructor of class Style
def test_Style():

    import pytest

    rule1 = RenderType()
    rule2 = RenderType()
    rule3 = RenderType()

    args = (rule1, rule2, rule3)

    style = Style(*args)

    assert style.rules == args

    assert str(style) == "".join(str(x) for x in args)



# Generated at 2022-06-14 08:24:03.083548
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertypes import Fg, EightbitRgbFg, SixteenbitRgbFg
    from .sgr import FgBg

    def f1(value):
        return value

    def f2(value):
        return f"f2 {value}"

    def f3(value):
        return f"f3 {value}"

    renderfuncs = {Sgr: f1, Fg: f2, EightbitRgbFg: f2, SixteenbitRgbFg: f3}
    style = Style(Fg(255), FgBg(225, 254), EightbitRgbFg(255, 255, 255))
    r1 = Register()
    r1.renderfuncs = deepcopy(renderfuncs)
    r1.set_rgb_call(EightbitRgbFg)
   

# Generated at 2022-06-14 08:24:10.339418
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class TestRenderType(RenderType):
        pass

    class TestRegister(Register):
        def __init__(self):
            super().__init__()
            self.test = Style(TestRenderType(45))

    register = TestRegister()
    style_before = register.test

    def test_func(style_code: int) -> str:
        style_str = f"{style_code}"
        return style_str

    register.set_renderfunc(TestRenderType, test_func)
    style_after = register.test

    assert style_before != style_after
    assert style_after == "45"



# Generated at 2022-06-14 08:24:14.539026
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    register = Register()

    register.test = "test"
    register.test2 = "test2"

    assert register.as_dict() == {"test": "test", "test2": "test2"}



# Generated at 2022-06-14 08:24:24.800286
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from .render import ANSI, HTML, CSS

    fg = Register()
    fg.set_eightbit_call(ANSI.RgbFg)
    fg.set_rgb_call(ANSI.RgbFg)

    fg.red = Style(ANSI.RgbFg(255, 0, 0))
    assert fg.red == "\x1b[38;2;255;0;0m"

    fg.set_renderfunc(ANSI.RgbFg, lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m")

    fg.red = Style(ANSI.RgbFg(255, 0, 0))
    assert fg.red == "\x1b[38;2;255;0;0m"

# Generated at 2022-06-14 08:24:36.886733
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from sty import fg, bg, ef, rs, RenderType, Rule
    fg.black = Style(Rule(RenderType.SGR, 38, 2, 0, 0, 0))
    assert str(fg.black) == '\x1b[38;2;0;0;0m'
    fg.set_renderfunc(RenderType.SGR, lambda x, y, r, g, b: "\x1b[38;5;{}m".format(x))
    assert str(fg.black) == '\x1b[38;5;0m'
    assert fg.black == Style(Rule(RenderType.SGR, 38, 2, 0, 0, 0))
    bg.black = Style(Rule(RenderType.SGR, 48, 2, 0, 0, 0))
    assert str

# Generated at 2022-06-14 08:24:49.993386
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    assert Register.as_namedtuple(fg) == fg.as_namedtuple()

# Generated at 2022-06-14 08:24:58.810949
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()
    r.red = Style(RgbFg(255, 0, 0))
    r.blue = Style(RgbFg(0, 0, 255))
    r.set_renderfunc(RgbFg, lambda x, y, z: f"\x1b[{x}|{y}|{z}")
    r.set_eightbit_call(RgbFg)
    r.set_rgb_call(RgbFg)

    assert r(255, 0, 0) == "\x1b[255|0|0"
    assert r(0, 0, 255) == "\x1b[0|0|255"
    assert r("red") == "\x1b[255|0|0"
    assert r("blue") == "\x1b[0|0|255"

# Generated at 2022-06-14 08:25:04.042512
# Unit test for method __new__ of class Style
def test_Style___new__():

    from .render import Sgr, RgbFg

    style = Style(RgbFg(1,2,3), value="\x1b[38;2;1;2;3m")

    assert style._rules[0].args == (1,2,3)

    assert style._value == "\x1b[38;2;1;2;3m"



# Generated at 2022-06-14 08:25:15.522513
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .renderfunc import render_ansi256_rgb
    from .rendertype import Rgb16BitFg, Rgb16BitBg, Rgb24BitFg, Rgb24BitBg

    r = Register()
    r.set_renderfunc(Rgb16BitFg, render_ansi256_rgb)
    r.set_rgb_call(Rgb16BitFg)
    assert str(r(120, 120, 120)) == "\x1b[38;5;232m"
    r.set_renderfunc(Rgb16BitBg, render_ansi256_rgb)
    r.set_rgb_call(Rgb16BitBg)
    assert str(r(120, 120, 120)) == "\x1b[48;5;232m"
    r.set_render

# Generated at 2022-06-14 08:25:29.189770
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    # Create a new Register
    class MyReg(Register):
        black = Style(RgbFg(0,0,0))
        white = Style(RgbFg(255, 255, 255))

    reg = MyReg()

    # Create namedtuple from dict
    class Regtuple(NamedTuple):
        black: str
        white: str

    # Convert register to namedtuple
    regtuple = Regtuple(**reg.as_dict())

    # Compare two namedtuples
    assert isinstance(regtuple, Regtuple)

    assert (
        regtuple.black
        == reg.as_namedtuple().black
        == reg.black
        == "\x1b[38;2;0;0;0m"
    )


# Generated at 2022-06-14 08:25:41.137820
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import Sgr, RgbFg
    from .context import StyContext

    sty = StyContext(True)

    sty.fg.black = Style(Sgr(30))
    sty.fg.white = Style(Sgr(37))
    sty.bg.white = Style(Sgr(47))

    sty.fg.set_rgb_call(RgbFg)

    decorated_string = sty.fg(255, 255, 255)("Hello") + sty.bg.white("World")

    assert decorated_string == "\x1b[38;2;255;255;255mHello\x1b[47mWorld\x1b[0m"

# Generated at 2022-06-14 08:25:46.462266
# Unit test for method __new__ of class Style
def test_Style___new__():

    from sty import fg, bg

    sty_rule = fg.magenta + bg.blue + fg.bold + bg.bold
    assert isinstance(sty_rule, Style)
    assert str(sty_rule) == '\x1b[38;2;255;0;255m\x1b[48;2;0;0;255m\x1b[1m\x1b[1m\x1b[0m'



# Generated at 2022-06-14 08:25:57.606523
# Unit test for constructor of class Register
def test_Register():
    from .defaults import fg
    from .rendertype import EightbitFg

    assert isinstance(fg, Register)

    fg.set_renderfunc(EightbitFg, lambda x: str(x))

    fg.green = Style(EightbitFg(2))

    assert fg.green == "2"

    fg.red = Style(EightbitFg(1), fg.green)
    assert fg.red == "12"

    # Test mute and unmute:
    fg.mute()
    assert fg.red == ""

    fg.unmute()
    assert fg.red == "12"



# Generated at 2022-06-14 08:26:03.871300
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    from .rendertype import RgbBg
    from .renderfunc import rgb_bg_call

    class TestRegister(Register):

        a: Style

    r = TestRegister()

    r.set_renderfunc(RgbBg, rgb_bg_call)

    r.a = Style(RgbBg(1, 2, 3))

    assert str(r.a) == "\x1b[48;2;1;2;3m"

# Generated at 2022-06-14 08:26:08.897488
# Unit test for method copy of class Register
def test_Register_copy():
    rs = Register()
    rs.blue = Style(RgbFg(10, 223, 10))
    copy = rs.copy()
    assert getattr(rs, "blue") == getattr(copy, "blue")


# Generated at 2022-06-14 08:26:41.562007
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    bg = Register()

    bg.blue = Style(RgbBg(0, 0, 255))
    bg.white = Style(RgbBg(255, 255, 255))

    assert bg.blue == Style(RgbBg(0, 0, 255), value="\x1b[48;2;0;0;255m")
    assert bg.white == Style(RgbBg(255, 255, 255), value="\x1b[48;2;255;255;255m")


# Generated at 2022-06-14 08:26:52.106178
# Unit test for method __call__ of class Register
def test_Register___call__():

    class MockRenderType(RenderType):
        pass

    s = Register()
    s.set_renderfunc(MockRenderType, lambda x: "Mock")

    s.mock = Style(MockRenderType(1))

    assert s.mock == "\x1b[Mock"
    assert s(1) == ""
    assert s(42) == ""
    assert s("mock") == "\x1b[Mock"
    assert s("non-existing") == ""

    s.set_eightbit_call(MockRenderType)
    assert s(42) == "\x1b[Mock"

    s.set_renderfunc(MockRenderType, lambda r, g, b: "RGBMock")
    s.set_rgb_call(MockRenderType)

# Generated at 2022-06-14 08:27:05.701476
# Unit test for method mute of class Register
def test_Register_mute():
    from .rendertype import Sgr
    from .rendertype import RgbFg

    class myRegister(Register):
        red = Style(Sgr(1), RgbFg(255, 0, 0))
        blue = Style(Sgr(2), RgbFg(0, 0, 255))

    reg = myRegister()
    assert reg.red == "\x1b[38;2;255;0;0m\x1b[1m"
    assert reg.blue == "\x1b[38;2;0;0;255m\x1b[2m"
    reg.mute()
    assert reg.red == ""
    assert reg.blue == ""
    reg.unmute()
    assert reg.red == "\x1b[38;2;255;0;0m\x1b[1m"

# Generated at 2022-06-14 08:27:11.759837
# Unit test for method __new__ of class Style
def test_Style___new__():
    rule_1: RenderType = RenderType(fg=1)
    style_1: Style = Style(rule_1, value="\x1b[38;2;1m")

    assert isinstance(style_1, Style)
    assert isinstance(style_1, str)
    assert style_1 == "\x1b[38;2;1m"

# Generated at 2022-06-14 08:27:22.243076
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .fg import fg, rgb_fg
    from .bg import bg, rgb_bg

    # Setup
    fg_styler = fg.copy()
    bg_styler = bg.copy()

    fg.orange = Style(rgb_fg(1, 5, 10), fg.bold)
    bg.blue = Style(rgb_bg(10, 20, 30), bg.underline)

    # Execute
    fg_nt = fg_styler.as_namedtuple()
    bg_nt = bg_styler.as_namedtuple()

    fg_styler.orange = Style(rgb_fg(1, 5, 10), fg.bold)

# Generated at 2022-06-14 08:27:32.018216
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertype import RgbFg

    class TestRegister(Register):
        blue = Style(RgbFg(255, 255, 255), value="\x1b[38;2;0;0;255m")

    test_reg = TestRegister()
    result1 = test_reg(1, 0, 255)
    assert result1 == "\x1b[38;2;1;0;255m"

    result2 = test_reg("blue")
    assert result2 == "\x1b[38;2;0;0;255m"



# Generated at 2022-06-14 08:27:40.775785
# Unit test for method __call__ of class Register
def test_Register___call__():

    class RenderTypeNoArgs(RenderType):

        def __call__(self, *args):
            return "value"

    class Sty(Register):

        def __init__(self):

            super().__init__()

            self.register_func(RenderTypeNoArgs)

            self.set_eightbit_call(RenderTypeNoArgs)
            self.set_rgb_call(RenderTypeNoArgs)

            self.value1: Style = Style(value="a")
            self.value2: Style = Style(value="b")

    sty = Sty()

    # Assert that a call like sty(42) works.
    assert sty(42) == "value"

    # Assert that a call like sty(10, 255, 42) works.
    assert sty(10, 255, 42) == "value"

    # Assert that

# Generated at 2022-06-14 08:27:52.946174
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    """
    Test the as_namedtuple method of class Register.
    """
    from sty import fg, rs

    class MyType(NamedTuple):
        black: str
        red: str
        green: str
        yellow: str
        blue: str
        magenta: str
        cyan: str
        white: str
        reset: str

    reg = Register()
    reg.black = fg(0)
    reg.red = fg(1)
    reg.green = fg(2)
    reg.yellow = fg(3)
    reg.blue = fg(4)
    reg.magenta = fg(5)
    reg.cyan = fg(6)
    reg.white = fg(7)
    reg.reset = rs.all

    assert reg.as_namedt

# Generated at 2022-06-14 08:27:59.021162
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    from .rendertype import RgbBg, RgbFg
    from .renderrule import RenderRule

    def renderfunc1(*args, **kwargs):  # pylint: disable=unused-argument
        return "\x1b[38;2;10;42;255m"

    def renderfunc2(*args, **kwargs):  # pylint: disable=unused-argument
        return "\x1b[48;2;10;42;255m"

    r = Register()
    r.set_renderfunc(RgbFg, renderfunc1)
    r.set_renderfunc(RgbBg, renderfunc2)

    r.set_rgb_call(RgbFg)
    r.set_eightbit_call(RgbBg)


# Generated at 2022-06-14 08:28:07.900997
# Unit test for constructor of class Style
def test_Style():
    from .rendertype import Sgr
    style1 = Style(Sgr(1))
    style2 = Style(Sgr(1), Sgr(3))
    style3 = Style('x')
    style4 = Style(Sgr(1), style3)
    assert style1.route == '\x1b[1m'
    assert style2.route == '\x1b[1m\x1b[3m'
    assert style3.route == 'x'
    assert style4.route == '\x1b[1mx'



# Generated at 2022-06-14 08:29:07.542575
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    FakeRegister = Register()
    FakeColor1 = RenderType("FakeColor1", ["fake1"])
    FakeColor2 = RenderType("FakeColor2", ["fake2"])

    FakeRegister.set_renderfunc(FakeColor1, lambda fake1: f"{fake1}1")
    FakeRegister.set_renderfunc(FakeColor2, lambda fake2: f"{fake2}2")

    FakeRegister.a = Style(FakeColor1("unused_parameter"), FakeColor2("unused_parameter"))

    assert getattr(FakeRegister, "a") == "\x1b[fake12\x1b[fake22"

# Generated at 2022-06-14 08:29:16.502842
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    class Rgb(RenderType):
        """
        This dummy rendertype is needed for the unit tests.
        """
        def __init__(self, *args):
            self.args = args

    def render_rgb(r, g, b):
        return "rgb"

    r = Register()
    r.set_renderfunc(Rgb, render_rgb)

    r.set_rgb_call(Rgb)
    assert r(1, 2, 3) == "rgb"

# Generated at 2022-06-14 08:29:28.992271
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from .constants import fg, bg, ef, rs

    r1 = Register()
    r1.red: Style = Style(fg.red)
    assert str(r1.red) == "\x1b[38;2;255;0;0m"

    r1.red: Style = Style(bg.red)
    assert str(r1.red) == "\x1b[48;2;255;0;0m"

    r1.red: Style = Style(ef.red)
    assert str(r1.red) == "\x1b[38;2;255;0;0m"

    r1.red: Style = Style(rs.red)
    assert str(r1.red) == "\x1b[38;2;255;0;0m"

    r1.red: Style

# Generated at 2022-06-14 08:29:40.285169
# Unit test for method __call__ of class Register
def test_Register___call__():

    class RenderTypeMock(RenderType):
        start: str = "start"
        end: str = "end"

    class RegisterMock(Register):
        def __init__(self):
            super().__init__()
            self.set_renderfunc(RenderTypeMock, lambda x, y: f"{x} {y}")

    r = RegisterMock()

    assert r(1, 2) == "1 2"
    assert r(x=1, y=2) == "1 2"
    assert r(1, 2, x=1, y=2) == "1 2"

    r = RegisterMock()
    r.foo = Style(
        RenderTypeMock(x=1, y=2), RenderTypeMock(x=3, y=4), value="foobar"
    )

# Generated at 2022-06-14 08:29:50.463525
# Unit test for method unmute of class Register
def test_Register_unmute():
    r = Register()

    r.set_renderfunc(RenderType, lambda x: f"{x}")
    r.set_eightbit_call(RenderType)

    r.orange = Style(RenderType(1))
    r.muted = Style(RenderType(1))

    r.mute()
    assert r.orange == ""
    assert r.orange() == ""

    r.unmute()
    assert r.orange == "1"
    assert r.orange() == "1"

    assert r.muted == ""
    assert r.muted() == ""




# Generated at 2022-06-14 08:29:54.611798
# Unit test for method copy of class Register
def test_Register_copy():
    """
    Method copy of class Register should return an independent copy.
    """
    reg1 = Register()
    setattr(reg1, "style", Style())
    reg2 = reg1.copy()

    assert reg1.style != reg2.style

# Generated at 2022-06-14 08:30:00.626268
# Unit test for method __new__ of class Style
def test_Style___new__():

    # Hacky way to check whether __new__ worked as intended.
    s = Style("sgr(1)", "sgr(2)")
    assert isinstance(s, str)
    assert isinstance(s, Style)
    assert s.rules == ("sgr(1)", "sgr(2)")



# Generated at 2022-06-14 08:30:13.187335
# Unit test for method mute of class Register
def test_Register_mute():
    from .rendertype import RgbFg, Sgr

    class MyRegister(Register):
        pass

    myreg = MyRegister()
    myreg.red = Style(RgbFg(255, 0, 0))

    assert str(myreg.red) == "\x1b[38;2;255;0;0m"

    myreg.mute()

    assert str(myreg.red) == ""

    myreg.unmute()

    assert str(myreg.red) == "\x1b[38;2;255;0;0m"

    myreg.red = Style(RgbFg(255, 0, 0), Sgr(1))

    assert str(myreg.red) == "\x1b[38;2;255;0;0m\x1b[1m"


# Generated at 2022-06-14 08:30:26.359451
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    class MyRegister(Register):
        def __init__(self):
            super().__init__()
            self.red = Style(RgbFg(255, 0, 0))
            self.white = Style(RgbFg(255, 255, 255))

    r = MyRegister()

    assert isinstance(r, Register)
    assert isinstance(r.red, str)
    assert isinstance(r.white, str)
    assert isinstance(r.as_dict(), dict)
    assert r.red != r.white
    assert r.as_dict().get("red") == r.as_dict().get("white")
    assert r.as_dict().get("red", "") == "\x1b[38;2;255;0;0m"


# Generated at 2022-06-14 08:30:37.530622
# Unit test for method copy of class Register
def test_Register_copy():
    """
    Test if deepcopy of register-object works.
    """

    import os
    import sys
    import unittest

    # When testing on Windows, remove ANSI-escape-sequences
    if os.name == "nt":
        import colorama
        colorama.init()

    class RenderType1(RenderType):
        """
        Dummy rendertype for testing.
        """

    class RenderType2(RenderType):
        """
        Dummy rendertype for testing.
        """

    # Dummy renderfuncs for testing
    renderfunc1: Callable = lambda: "RENDERFUNC1"
    renderfunc2: Callable = lambda: "RENDERFUNC2"

    # Create two dummy classes. One has a custom renderfunc, the other not.
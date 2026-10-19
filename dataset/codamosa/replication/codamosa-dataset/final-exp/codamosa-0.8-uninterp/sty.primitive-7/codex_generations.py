

# Generated at 2022-06-14 08:20:59.814384
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()
    r.renderfuncs = {"str": lambda a: f"8bit: {a}", "tuple": lambda a, b, c: f"24bit: {a} {b} {c}"}
    r.set_eightbit_call("str")
    r.set_rgb_call("tuple")
    assert r(255) == "8bit: 255"
    assert r(42, 100, 230) == "24bit: 42 100 230"

# Generated at 2022-06-14 08:21:02.943394
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r.renderfuncs == {}
    assert r.is_muted == False
    assert r.rgb_call != None
    assert r.eightbit_call != None

# Generated at 2022-06-14 08:21:09.738440
# Unit test for method __call__ of class Register
def test_Register___call__():
    # Empty r object
    r = Register()
    assert r() == ""
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert r("red") == ""

    # Filled r object
    r.red = Style(RenderType.fg, RenderType.bg)
    assert r() == ""
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert r("red") == "\x1b[38;5;1m\x1b[48;5;1m"


# Generated at 2022-06-14 08:21:20.977828
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .eightbit import Eightbit
    from .rgb import RgbFg, RgbBg
    from .sgr import Sgr
    from .dim import Dim

    class DummyRegister(Register):
        def __init__(self):
            super().__init__()

        def render_eightbit(self, val: int) -> str:
            return f"eightbit {val}"

        def render_rgb(self, r: int, g: int, b: int) -> str:
            return f"rgb {r} {g} {b}"

    myregister = DummyRegister()

    # Test Eightbit-call
    myregister.set_eightbit_call(Eightbit)
    assert myregister(1) == "eightbit 1"

    # Test RGB-call

# Generated at 2022-06-14 08:21:33.910706
# Unit test for constructor of class Register
def test_Register():

    fn_start = lambda: "\x1b[38;2;"
    fn_middle = lambda x,y,z: f"{int(x)};{int(y)};{int(z)};"
    fn_end = lambda: "m"

    r = Register()

    # Test __init__()
    assert r.eightbit_call == r.rgb_call == r

    # Test set_eightbit_call()
    r.set_eightbit_call(r.rgb_call)
    assert r.eightbit_call == r.rgb_call

    # Test set_rgb_call()
    r.set_rgb_call(r.eightbit_call)
    assert r.eightbit_call == r.rgb_call

    # Test set_renderfunc()
    r.set_render

# Generated at 2022-06-14 08:21:41.029682
# Unit test for method __call__ of class Register
def test_Register___call__():

    reg = Register()

    # Set some render-functions
    reg.set_renderfunc(RenderType, lambda x: "")
    reg.set_renderfunc(type, lambda x: "%s:" % x)

    # Create a simple style-attribute
    reg.test = Style(RenderType())

    # Test return of style-attribute
    assert reg.test == ":"

    # Test call of style-attribute
    assert reg("test") == ":"

    # Test call of style-attribute and __getattr__
    assert reg("test", RenderType()) == ":"
    assert reg("test", type("")) == ":"

    # Test call of style-attribute and __getattr__
    assert reg("test", RenderType()) == ":"
    assert reg("test", type("")) == ":"

    # Test call of style-attribute and __

# Generated at 2022-06-14 08:21:54.273738
# Unit test for method __call__ of class Register
def test_Register___call__():

    renderType = RenderType()

    renderfuncs: Renderfuncs = {
        renderType.__class__: lambda x: x + "testCall"
    }

    register = Register()

    register.eightbit_call = lambda x: "eightBitCall"
    register.rgb_call = lambda r, g, b: "rgbCall"
    register.renderfuncs = renderfuncs

    # Test call with integer argument:
    assert (
        register(42) == "eightBitCall"
    ), "Method __call__ of class Register does not work as intended."

    # Test call with RGB argument:
    assert (
        register(42, 255, 128) == "rgbCall"
    ), "Method __call__ of class Register does not work as intended."

    # Test call with style name:
    register.testCall = Style

# Generated at 2022-06-14 08:22:02.509746
# Unit test for method __call__ of class Register
def test_Register___call__():
    class TestRegister(Register):
        def __init__(self):
            super().__init__()
            self.renderfuncs.update({int: lambda x: x})

    register: TestRegister = TestRegister()
    register.test = Style(1)
    register.test2 = Style(1, 2, 3)

    assert register(8) == 8
    assert register("test") == "1"
    assert register(10, 20, 30) == (10, 20, 30)

# Generated at 2022-06-14 08:22:12.880466
# Unit test for method __call__ of class Register
def test_Register___call__():
    """
    Test call-behavior
    """
    class RgbFg(RenderType):
        pass

    class RgbBg(RenderType):
        pass

    def render_rgb_fg(r: int, g: int, b: int) -> str:
        return "\x1b[38;2;{};{};{}m".format(r, g, b)

    def render_rgb_bg(r: int, g: int, b: int) -> str:
        return "\x1b[48;2;{};{};{}m".format(r, g, b)

    reg = Register()
    reg.set_renderfunc(RgbFg, render_rgb_fg)
    reg.set_rgb_call(RgbFg)

# Generated at 2022-06-14 08:22:24.353261
# Unit test for method __call__ of class Register
def test_Register___call__():
    """
    Test for method __call__ of class Register.
    """

    from sty import RenderType, fg, ef, rs
    from sty import Rgb, RgbFg, Sgr

    # Setup
    fg.rgb(10, 50, 100)
    fg.rgb_call = RenderType.from_ansi_seq(RgbFg)
    ef.rgb(10, 50, 100)
    ef.rgb_call = RenderType.from_ansi_seq(Rgb)
    rs.rgb(10, 50, 100)
    rs.rgb_call = RenderType.from_ansi_seq(Sgr)
    expected_ansi_seq = "\x1b[38;2;10;50;100m"


# Generated at 2022-06-14 08:22:29.447681
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()
    r.__call__(1)
    r.__call__(2, 3, 4)
    r.__call__("dummy")



# Generated at 2022-06-14 08:22:33.221142
# Unit test for constructor of class Register
def test_Register():
    """
    Test if Register-object is created correctly.
    """

    # Setup
    r = Register()

    # Execute
    r.red = Style(Sgr(1), RgbFg(255, 0, 0))
    r.blue = Style(Sgr(1), RgbFg(0, 0, 255))
    r.green = Style(Sgr(1), RgbFg(0, 128, 0))

    # Test
    assert r.red == '\x1b[38;2;255;0;0m\x1b[1m'
    assert r.blue == '\x1b[38;2;0;0;255m\x1b[1m'

# Generated at 2022-06-14 08:22:41.594105
# Unit test for method __call__ of class Register
def test_Register___call__():
    """
    Unit test for method __call__ of class Register.
    """
    from .termui import Rgb24bitBg

    # Test with 8bit-call
    reg = Register()
    assert reg(8) is ""

    setattr(reg, 'foo', Style(8))
    assert reg(8) == reg.foo
    assert reg('foo') == reg.foo
    assert reg(8) == reg('foo')

    # Test with 24bit-call
    reg = Register()
    setattr(reg, "r", Style(Rgb24bitBg(2, 3, 4)))
    assert reg(2, 3, 4) == reg.r
    assert reg(2, 3, 4) == reg('r')

# Generated at 2022-06-14 08:22:48.951564
# Unit test for constructor of class Register
def test_Register():
    """
    This function tests the constructor of the Register-class.
    """
    from .rendertype import RgbBg

    r = Register()

    r.set_eightbit_call(RgbBg)
    r.set_rgb_call(RgbBg)
    r.set_renderfunc(RgbBg, lambda *args: "RgbBg")

    test0 = r(12) # This will call r.eightbit_call
    assert test0 == "RgbBg"

    test1 = r(10, 42, 255) # This will call r.rgb_call
    assert test1 == "RgbBg"

    test2 = r("test")
    assert test2 == ""

    r.test = Style(RgbBg(12, 42, 255))

# Generated at 2022-06-14 08:22:50.390386
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert bool(r)



# Generated at 2022-06-14 08:22:52.244298
# Unit test for constructor of class Register
def test_Register():
    r = Register()

    assert isinstance(r, Register)



# Generated at 2022-06-14 08:22:59.367276
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .constants import fg

    # Test 1 eightbit-call
    assert fg(144) == "\x1b[38;5;144m"
    # Test 2 rgb-call
    assert fg(255, 210, 0) == "\x1b[38;2;255;210;0m"
    # Test 3 str-call
    assert fg("orange") == "\x1b[38;2;255;165;0m"

# Generated at 2022-06-14 08:23:13.340423
# Unit test for method __call__ of class Register
def test_Register___call__():

    # TODO: This test needs to be rewritten to not use internals of the Register.
    def render_eightbit(*args, **kwargs):
        return "<" + ";".join([str(n) for n in args]) + ">"

    def render_rgb(*args, **kwargs):
        return "#" + ";".join([str(n) for n in args]) + "#"

    r = Register()

    r.set_eightbit_call(RenderType)
    r.set_rgb_call(RenderType)

    r.set_renderfunc(RenderType, render_eightbit)

    # Register-object is callable with an 8bit color code.
    assert r(42) == "<42>"

    # Register-object is callable with an 24bit color code.
    assert r(1, 2, 3)

# Generated at 2022-06-14 08:23:17.959796
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r.is_muted == False
    assert r.renderfuncs == {}

# Generated at 2022-06-14 08:23:30.978348
# Unit test for method __call__ of class Register
def test_Register___call__():

    class CustomRegister(Register):
        pass

    r: CustomRegister = CustomRegister()

    r.on_off = Style(Sgr(1))
    r.red = Style(Sgr(30))
    r.blue = Style(Sgr(34))
    r.green = Style(Sgr(32))
    r.orange = Style(RgbFg(1, 5, 10))

    # Test set_eightbit_call
    r.set_eightbit_call(Sgr)

    assert r(31) == "\x1b[31m"
    assert r(31) != "\x1b[38;2;1;5;10m\x1b[1m"

    # Test set_rgb_call
    r.set_rgb_call(RgbFg)

# Generated at 2022-06-14 08:23:48.192633
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .rendertype import Sgr, RgbBg
    from .registers import bg

    bg.unmute()

    assert not bg.is_muted

    bg.black = Sgr(30)
    bg.red = RgbBg(200,50,50)
    bg.mute()

    assert bg.is_muted

    bg.unmute()

    assert not bg.is_muted

    assert bg.black == "\x1b[40m"
    assert bg.red == "\x1b[48;2;200;50;50m"

# Generated at 2022-06-14 08:24:01.147512
# Unit test for constructor of class Style
def test_Style():

    # Test style constructor with one parameter
    style_1 = Style(RgbFg(1, 5, 10))
    assert isinstance(style_1, Style)
    assert isinstance(style_1, str)
    assert str(style_1) == "\x1b[38;2;1;5;10m"

    # Test style constructor with two parameters
    style_3 = Style(RgbFg(1, 5, 10), Sgr(1))
    assert isinstance(style_3, Style)
    assert isinstance(style_3, str)
    assert str(style_3) == "\x1b[38;2;1;5;10m\x1b[1m"

    # Test style constructor with three parameters

# Generated at 2022-06-14 08:24:05.211966
# Unit test for constructor of class Style
def test_Style():
    s = Style(RgbFg(0,0,0), RgbBg(0,0,0), Sgr(0))
    assert isinstance(s, str)
    assert isinstance(s, Style)

# Generated at 2022-06-14 08:24:17.482158
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .rendertype import RgbFg, Sgr

    register = Register()
    register.set_renderfunc(RgbFg, lambda r, g, b: "RgbFg({}, {}, {})".format(r, g, b))
    register.set_renderfunc(Sgr, lambda x: "Sgr({})".format(x))

    register.red = Style(RgbFg(255, 0, 0), Sgr(1))
    register.blue = Style(RgbFg(0, 55, 255), Sgr(1))

    r1 = Register()
    r1.red = register.red

    assert(r1.red == "RgbFg(255, 0, 0)Sgr(1)")

    r1.mute()
    assert(r1.red == "")

    r

# Generated at 2022-06-14 08:24:19.108594
# Unit test for constructor of class Register
def test_Register():
    r1 = Register()
    assert isinstance(r1, Register)

# Generated at 2022-06-14 08:24:23.433205
# Unit test for method unmute of class Register
def test_Register_unmute():

    class MyRegister(Register):
        def __init__(self):
            super().__init__()
            self.mystyle = Style(RgbFg(0, 0, 0))

    reg = MyRegister()

    assert reg.mystyle == "\x1b[38;2;0;0;0m"

    reg.mute()

    assert reg.mystyle == ""

    reg.unmute()

    assert reg.mystyle == "\x1b[38;2;0;0;0m"



# Generated at 2022-06-14 08:24:28.142138
# Unit test for method mute of class Register
def test_Register_mute():
    r = Register()
    r._test = Style(None)
    r.mute()
    assert r._test == ""
    assert r.is_muted
    r.unmute()
    assert r._test == ""
    assert not r.is_muted



# Generated at 2022-06-14 08:24:36.099231
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .fg import fg
    from .sgr import Fg

    new_register = fg.copy()
    setattr(new_register, "test", Style(Fg(42)))
    assert str(new_register.test) == "\x1b[38;5;42m"

    new_register.mute()
    assert str(new_register.test) == ""

    new_register.unmute()
    assert str(new_register.test) == "\x1b[38;5;42m"

# Generated at 2022-06-14 08:24:40.789527
# Unit test for method mute of class Register
def test_Register_mute():
    fg = Register()
    fg.red = Style(RgbFg(1, 5, 10))
    fg.mute()

    assert fg.red == ""



# Generated at 2022-06-14 08:24:45.575939
# Unit test for method copy of class Register
def test_Register_copy():
    fg = Register()
    fg.black = Style(Bold())
    fg2 = fg.copy()
    assert fg2 is not fg
    assert isinstance(fg2, Register)
    assert fg2.black == fg.black

# Generated at 2022-06-14 08:24:58.779785
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class Fg(RenderType):

        def __init__(self, n: int):
            self.n = n

        @property
        def args(self) -> Tuple[int]:
            return (self.n,)

    class Bg(RenderType):

        def __init__(self, n: int):
            self.n = n

        @property
        def args(self) -> Tuple[int]:
            return (self.n,)

    def render_Fg(n: int) -> str:
        return "\x1b[38;5;" + str(n) + "m"

    def render_Bg(n: int) -> str:
        return "\x1b[48;5;" + str(n) + "m"

    reg = Register()

    assert reg.renderfuncs == {}
    assert has

# Generated at 2022-06-14 08:25:05.976272
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    import sty
    import pytest
    reg = Register()
    reg.set_renderfunc(sty.RgbFg, lambda r, g, b: "RgbFg")
    reg.set_renderfunc(sty.RgbBg, lambda r, g, b: "RgbBg")
    reg.set_eightbit_call(sty.RgbFg)
    assert reg(144) == "RgbFg"
    reg.set_eightbit_call(sty.RgbBg)
    assert reg(12) == "RgbBg"



# Generated at 2022-06-14 08:25:15.043279
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from .sgr import Sgr

    Rule1 = namedtuple("Rule1", ["a"])
    r1 = Rule1(1)

    Rule2 = namedtuple("Rule2", ["a"])
    r2 = Rule2(2)

    Sty1 = Style(r1)
    Sty2 = Style(r2)

    Sty3 = Style(Sty1)
    Sty4 = Style(Sty2)

    Sty5 = Style(r1, r2)
    Sty6 = Style(Sty1, Sty2)

    Sty7 = Style(r1, Sty1)
    Sty8 = Style(Sty1, Sty2, Sty1)
    Sty9 = Style(Sty1, r2)

    Reg = Register()


# Generated at 2022-06-14 08:25:23.391912
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class DummyRenderType(RenderType):
        """This is only for testing purposes"""

    class DummyRenderType2(RenderType):
        """This is only for testing purposes"""

    def dummy_render_func(*args, **kwargs):
        return "dummy_render_func"

    def dummy_render_func2(*args, **kwargs):
        return "dummy_render_func2"

    reg = Register()

    # When calling a non-existing renderfunc the system should return an
    # empty str.
    assert reg(155) == ""

    # Setting a renderfunc should work.
    reg.set_renderfunc(DummyRenderType, dummy_render_func)
    assert reg(155) == "dummy_render_func"

    # Replacing a renderfunc should work.

# Generated at 2022-06-14 08:25:25.719491
# Unit test for method __new__ of class Style
def test_Style___new__():
    """Unit test for method __new__ of class Style."""
    import pytest
    from sty import fg

    style = Style(fg.red, value="\x1b[31m")

    assert isinstance(style, Style)
    assert str(style) == "\x1b[31m"



# Generated at 2022-06-14 08:25:28.279589
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    class MyRegister(Register):
        blue = Style(Sgr(34))
        red = Style(Sgr(31))

    style = MyRegister()
    style.set_renderfunc(Sgr, lambda x: "\x1b[{}m".format(x))

    assert hasattr(style.as_namedtuple(), "blue")
    assert hasattr(style.as_namedtuple(), "red")

# Generated at 2022-06-14 08:25:32.451187
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .ansi import RgbFg, RgbBg, RgbColor

    register = Register()
    register.set_rgb_call(RgbFg)

    assert register.rgb_call == RgbFg.render


# Generated at 2022-06-14 08:25:44.512580
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertype import Sgr

    # Case: 1 argument
    r8 = Register()
    r8.blue = Style(Sgr(38), Sgr(5), Sgr(4))
    assert r8(38) == "\\x1b[38;5;4m"

    # Case: 3 arguments
    r24 = Register()
    r24.blue = Style(Sgr(38), Sgr(2))
    assert r24(102, 49, 42) == "\\x1b[38;2;102;49;42m"

    # Case: string argument
    rstr = Register()
    rstr.blue = Style(Sgr(38), Sgr(5), Sgr(4))
    assert rstr("blue") == "\\x1b[38;5;4m"


# Generated at 2022-06-14 08:25:50.706284
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    class TestRegister(Register):
        pass

    r = TestRegister()
    r.a = Style(Sgr(41))
    assert isinstance(r.a, Style)
    assert isinstance(r.a, str)
    assert str(r.a) == "\x1b[41m"


# Generated at 2022-06-14 08:26:01.174899
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertype import Sgr8bit

    renderfuncs = {}

    # renderfunc for Sgr8bit
    def f1(x: int) -> str:
        return f"({x})"

    renderfuncs.update({Sgr8bit: f1})

    r = Register()
    r.set_renderfunc(Sgr8bit, f1)

    # Setting Eightbit call
    r.set_eightbit_call(Sgr8bit)
    assert r(5) == "(5)"

    # Setting Eightbit call
    r.set_eightbit_call(Sgr8bit)
    assert r(5) == "(5)"

# Generated at 2022-06-14 08:26:15.852177
# Unit test for method unmute of class Register
def test_Register_unmute():
    register = Register()
    register.black = Style(Sgr(30))
    register.white = Style(Sgr(37))

    register.unmute()
    assert isinstance(register.black, str)
    assert isinstance(register.white, str)
    assert register.black == "\x1b[30m"
    assert register.white == "\x1b[37m"



# Generated at 2022-06-14 08:26:28.363311
# Unit test for method __call__ of class Register
def test_Register___call__():

    # TODO: Test for muted objects.

    black = Style(Fg(0))
    orange = Style(RgbFg(1, 5, 10))

    fg = Register()
    setattr(fg, "black", black)
    setattr(fg, "orange", orange)
    fg.set_eightbit_call(Fg)

    bg = Register()
    setattr(bg, "black", black)
    setattr(bg, "orange", orange)
    bg.set_rgb_call(RgbBg)

    assert fg(0) == black == fg("black")
    assert bg(1, 5, 10) == orange == bg("orange")

# Generated at 2022-06-14 08:26:34.409979
# Unit test for method __new__ of class Style
def test_Style___new__():

    from .rendertype import Sgr, RgbFg

    Style(*[Sgr(1), RgbFg(1, 5, 10)], value="")
    Style(*[Sgr(1), RgbFg(1, 5, 10)], value="XXX")
    Style(*[Sgr(1), RgbFg(1, 5, 10)])

    assert True

# Generated at 2022-06-14 08:26:39.576560
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .colors import fg
    assert fg.red == '\x1b[31m'
    assert fg.orange == '\x1b[38;5;208m'
    assert fg.color('red') == '\x1b[31m'

# Generated at 2022-06-14 08:26:45.053246
# Unit test for method copy of class Register
def test_Register_copy():

    test_reg = Register()
    test_reg.black = Style(RgbFg(1,2,3))
    new_reg = test_reg.copy()
    new_reg.black = Style(RgbFg(3,2,1))
    assert test_reg.black != new_reg.black

# Generated at 2022-06-14 08:26:49.557550
# Unit test for constructor of class Style
def test_Style():
    class TestType(RenderType):
        pass

    style = Style(TestType(1), TestType(2,3))

    assert isinstance(style, Style)
    assert style.rules[0].args == (1,)
    assert style.rules[1].args == (2,3)

# Generated at 2022-06-14 08:26:54.261339
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    reg1 = Register()
    reg1.red = 4

    t = reg1.as_namedtuple()
    assert t.red == reg1.red, "Failed to convert register to namedtuple."


# Generated at 2022-06-14 08:26:59.535866
# Unit test for method copy of class Register
def test_Register_copy():
    import pytest

    fg = Register()
    fg.brown = Style(RgbFg(1,1,1), Sgr(1))
    fg_copy = fg.copy()

    assert fg.brown == fg_copy.brown

# Generated at 2022-06-14 08:27:10.169914
# Unit test for method __call__ of class Register
def test_Register___call__():
    import unittest
    from .builder import Sty

    @Sty
    class mySty(Sty):
        fg = Register()
        fg.set_eightbit_call(RenderType.SE)
        fg.set_rgb_call(RenderType.RGB)

        fg.test1 = Style(RenderType.SE(42))
        fg.test2 = Style(RenderType.RGB(10, 42, 255))

        @staticmethod
        def render_se(code: int) -> str:
            return f"se: {code}"

        @staticmethod
        def render_rgb(r: int, g: int, b: int) -> str:
            return f"rgb: {r};{g};{b}"

    fg = mySty.fg

# Generated at 2022-06-14 08:27:20.935159
# Unit test for method mute of class Register
def test_Register_mute():

    class Rgb(RenderType):
        def sgr(self, r, g, b):
            return f"\x1b[38;2;{r};{g};{b}m"

    class _Bg(RenderType):
        def sgr(self, color):
            return f"\x1b[48;5;{color}m"

    bg: Register = Register()
    bg.renderfuncs.update({Rgb: Rgb.sgr, _Bg: _Bg.sgr})
    bg.set_eightbit_call(Rgb)
    bg.set_rgb_call(_Bg)

    bg.muted_blue = Style(_Bg(1), Rgb(1, 2, 42))

# Generated at 2022-06-14 08:27:46.211405
# Unit test for method mute of class Register
def test_Register_mute():
    from .rendertype import sgr, rgb_fg

    # Init register-object
    r = Register()
    r.renderfuncs[sgr] = lambda *args: "\x1b[{}m".format(args[0])
    r.renderfuncs[rgb_fg] = lambda *args: "\x1b[38;2;{};{};{}m".format(*args)

    # Create style
    r.test = Style(sgr(1), rgb_fg(0, 0, 0))

    # Mute register
    r.mute()

    assert r.test == ""

    # Unmute register
    r.unmute()

    assert str(r.test) == "\x1b[38;2;0;0;0m\x1b[1m"

# Generated at 2022-06-14 08:27:55.729468
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    # Test creating a new register
    register1 = Register()

    # Test setting a new render-function for that register.
    def render_Sgr(index: int):
        return "\x1b[{}m".format(index)

    register1.set_renderfunc(Sgr, render_Sgr)

    # Test setting a new style for the register, based on the render-function above.
    register1.red = Style(Sgr(31))

    # Test if style was created successfully
    assert isinstance(register1.red, Style)
    assert register1.red == "\x1b[31m"

    # Test if register can handle inheritance
    register1.rgb = Style(RgbFg(255, 0, 0))
    register1.red = Style(register1.rgb, Sgr(1))


# Generated at 2022-06-14 08:28:03.384403
# Unit test for method copy of class Register
def test_Register_copy():
    bg = Register()
    bg.green = Style(SgrFg(102))
    bg.blue = Style(SgrFg(12))
    bg.mute()

    bg2 = bg.copy()
    bg2.blue = Style(SgrFg(3))
    assert(bg.blue == "")
    assert(bg2.blue == "\x1b[38;5;3m")

# Generated at 2022-06-14 08:28:05.464500
# Unit test for constructor of class Register
def test_Register():
    res: Register = Register()
    assert res



# Generated at 2022-06-14 08:28:08.069610
# Unit test for method __new__ of class Style
def test_Style___new__():
    bg_green: RenderType = RenderType()
    sty: Style = Style(bg_green)
    assert sty.rules == (bg_green,)

# Generated at 2022-06-14 08:28:11.313750
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    """
    Test method as_dict of class Register.
    """

    r = Register()
    r.red = 14
    assert r.red == 14
    assert r.as_dict() == {'red': 14}

# Generated at 2022-06-14 08:28:15.554808
# Unit test for method __new__ of class Style
def test_Style___new__():
    style = Style(value="\x1b[33m")
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert style == "\x1b[33m"

# Generated at 2022-06-14 08:28:22.739476
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .control import ef, rs

    class Test(RenderType):
        pass

    test = Register()
    test.set_renderfunc(Test, lambda x, y: f"{x}{y}")

    test.test = Style(Test(42, "H"))

    assert test(42) == ""
    assert test(1, 2, 3) == ""
    assert test("test") == "42H"

# Generated at 2022-06-14 08:28:27.911001
# Unit test for constructor of class Style
def test_Style():
    style = Style(fg=255, bg=15, bold=True)
    assert str(style) == "\x1b[38;5;255m\x1b[48;5;15m\x1b[1m"

# Unit tests for setattr and getattr of register-object.

# Generated at 2022-06-14 08:28:34.031237
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    renderfuncs = {type: lambda: type.__name__}

    # Create new register type
    fg = Register()

    # Set render-functions for register
    fg.set_renderfunc(RenderType, renderfuncs[RenderType])

    # Create style-object
    blue = Style(RenderType())

    # Set style on register
    fg.blue = blue

    # Test if style-object is rendered correctly.
    assert str(fg.blue) == "RenderType"
    assert isinstance(fg.blue, Style)
    assert isinstance(fg.blue, str)

# Generated at 2022-06-14 08:29:21.508434
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .colors import fg
    from .rendertype import Eightbit
    assert isinstance(fg.blue, Style)
    assert isinstance(fg.blue, str)
    assert fg.blue == "\x1b[34m"
    fg.set_eightbit_call(Eightbit)
    assert isinstance(fg.blue, str)
    assert fg.blue == "\x1b[38;5;21m"



# Generated at 2022-06-14 08:29:35.598083
# Unit test for method __call__ of class Register
def test_Register___call__():

    register = Register()
    register.set_eightbit_call(RenderType.FG)
    register.set_rgb_call(RenderType.FG)

    assert register.__call__(42) == ""
    assert register.__call__(42, 43, 44) == ""
    assert register.__call__("red") == ""

    def eightbit_func(*args, **kwargs) -> str:
        return "eightbit"

    register.set_renderfunc(RenderType.FG, eightbit_func)

    assert register.__call__(42) == "eightbit"
    assert register.__call__(42, 43, 44) == ""
    assert register.__call__("red") == ""

    def rgb_func(*args, **kwargs) -> str:
        return "rgb"

    register.set_render

# Generated at 2022-06-14 08:29:46.945076
# Unit test for constructor of class Style
def test_Style():
    StylingRule2 = Union[RenderType, Style]
    rule_dict: Dict[StylingRule2, Style] = {
        RgbFg(1, 5, 10): Style(RgbFg(1, 5, 10)),
        Style(RgbFg(1, 5, 10)): Style(RgbFg(1, 5, 10)),
        Style(Style(RgbFg(1, 5, 10))): Style(RgbFg(1, 5, 10)),
        Style(RgbFg(1, 5, 10), RgbFg(2, 6, 20)): Style(RgbFg(1, 5, 10), RgbFg(2, 6, 20)),
    }

    for rule, expected in rule_dict.items():
        assert Style(rule, value="") == expected


#

# Generated at 2022-06-14 08:29:54.436886
# Unit test for method mute of class Register
def test_Register_mute():
    import sty
    sty.register_custom_style('CustomStyle', lambda: '\x1b[38;2;1;1;1m')
    rs = sty.rs(CustomStyle)
    rs.set_eightbit_call(sty.RgbFg)

    assert str(rs.red) == '\x1b[38;2;1;1;1m'
    rs.mute()
    assert str(rs.red) == ''


# Generated at 2022-06-14 08:30:00.040827
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    reg = Register()
    reg.red = Style(RgbFg(255, 0, 0))

    style_register = reg.as_namedtuple()
    assert style_register.red == '\x1b[38;2;255;0;0m'

# Generated at 2022-06-14 08:30:12.851152
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    from .fg import fg
    from .rendertype import RgbFg
    from .style import Style
    from .rs import rs

    def render_rgb(r, g, b):
        return Style(rgb_fg(r, g, b))

    def render_fg(fg_col):
        return Style(RgbFg(0, 0, fg_col))

    # Test default register
    assert fg(42) == "\x1b[38;5;42m"
    assert fg(102, 49, 42) == "\x1b[38;2;102;49;42m"
    assert fg.rgb_call(10, 20, 30) == "\x1b[38;2;10;20;30m"

    # Test changing renderfunc for rgb-rendertype
    rgb_fg

# Generated at 2022-06-14 08:30:20.635156
# Unit test for constructor of class Style
def test_Style():
    style = Style(RgbBg(1,2,3), RgbFg(1,2,3))
    assert style == '\x1b[48;2;1;2;3m\x1b[38;2;1;2;3m'
    assert style.rules == (RgbBg(1,2,3), RgbFg(1,2,3))


# Generated at 2022-06-14 08:30:23.895406
# Unit test for method __new__ of class Style
def test_Style___new__():

    class Test(Style):
        pass

    t = Test("test")

    assert isinstance(t, Style)
    assert isinstance(t, str)
    assert t == "test"

# Generated at 2022-06-14 08:30:36.381956
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    from .enhanced import EnhancedRegister

    from .fg import fg
    from .bg import bg
    from .ef import ef

    from sty.const import *
    from sty.ansi import *

    r = EnhancedRegister()

    r.set_renderfunc(AnsiFg, lambda x: "I")
    r.set_renderfunc(AnsiBg, lambda x: "am")
    r.set_renderfunc(AnsiEf, lambda x: "the")
    r.set_renderfunc(AnsiSgr, lambda x: "king")

    # We do not want the default styles:
    r.black = Style(AnsiFg(0))
    r.white = Style(AnsiFg(15))

    # Add some custom styles:

# Generated at 2022-06-14 08:30:49.601191
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .ansi_codes import fg
    from .rendertype import Fg
    from .rendertype import Sgr
    from .sty import Sty

    def myfunc(n: int) -> str:
        return f"\x1b[38;5;{n}m"

    sty = Sty()
    sty.register("fg", Register())
    sty.fg.set_renderfunc(Fg, myfunc)

    sty.fg.red = sty.fg(1)
    sty.fg.bold_red = sty.fg.red + sty.fg(Sgr(1))

    sty.fg.mute()
    assert str(sty.fg.bold_red) == ""

    sty.fg.unmute()
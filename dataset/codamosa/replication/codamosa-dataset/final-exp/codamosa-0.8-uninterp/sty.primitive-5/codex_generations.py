

# Generated at 2022-06-14 08:20:58.992374
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    fg = Register()
    bg = Register()

    fg.set_renderfunc(RgbFg, lambda r, g, b: f"{r}, {g}, {b} RGB")
    bg.set_renderfunc(RgbBg, lambda r, g, b: f"{r}, {g}, {b} RGB")

    fg.set_eightbit_call(RgbFg)
    bg.set_eightbit_call(RgbBg)

    assert fg(10) == "10, 0, 0 RGB"
    assert bg(10) == "10, 0, 0 RGB"



# Generated at 2022-06-14 08:21:05.724919
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    """
    Test functionality of method `set_eightbit_call` of class Register.
    """

    from .rendertype import RgbFg, Sgr

    def my_render_func(x, y) -> str:
        """
        This is a custom render-function that renders with the parameters x, y.
        """
        return ""

    r = Register()

    r.set_renderfunc(Sgr, my_render_func)

    r.set_eightbit_call(Sgr)

    assert r.eightbit_call == my_render_func



# Generated at 2022-06-14 08:21:09.532228
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    # TODO: Refactor this code and write a proper unit test.

    from sty import fg

    def _test(x):
        return f"{x}test"

    fg.set_eightbit_call(fg, _test)

    assert fg(100) == "100test"
    assert fg(fg.black) == "0test"

# Generated at 2022-06-14 08:21:18.270972
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    from .rendertype import RgbFg, SgrFg

    fg = Register()
    fg.set_renderfunc(RgbFg, lambda r, g, b: "RGB" + str(r) + str(g) + str(b))
    fg.set_renderfunc(SgrFg, lambda x: "SGR" + str(x))

    fg.set_eightbit_call(RgbFg)
    assert fg(10, 5, 2) == "RGB10502"



# Generated at 2022-06-14 08:21:26.690991
# Unit test for method __call__ of class Register
def test_Register___call__():
    from sty import fg
    assert fg(42) == "\x1b[38;5;42m"
    assert fg(10, 42, 255) == "\x1b[38;2;10;42;255m"
    assert fg("red") == "\x1b[31m"
    assert fg("red_h42") == "\x1b[38;2;102;37;27m"



# Generated at 2022-06-14 08:21:31.005621
# Unit test for constructor of class Register
def test_Register():
    t: Register = Register()
    assert isinstance(t.is_muted, bool)
    assert isinstance(t.eightbit_call, Callable)
    assert isinstance(t.rgb_call, Callable)
    assert isinstance(t.renderfuncs, Dict)

# Generated at 2022-06-14 08:21:33.265128
# Unit test for constructor of class Register
def test_Register():
    import sty
    rs = sty.Register()
    assert isinstance(rs, sty.Register)


# Generated at 2022-06-14 08:21:44.203057
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertype import EightbitBg, EightbitFg, RgbBg, RgbFg
    from .sty import sty, sty_copy, sty_mute, sty_unmute

    sty_copy(None)

    sty_mute()
    sty.fg.red # Type annotation for typecheckers.
    sty_unmute()

    sty.set_renderfunc(EightbitBg, lambda x: f"\x1b[48;5;{x}m")
    sty.set_renderfunc(EightbitFg, lambda x: f"\x1b[38;5;{x}m")

    sty.set_renderfunc(RgbBg, lambda r, g, b: f"\x1b[48;2;{r};{g};{b}m")
    sty.set

# Generated at 2022-06-14 08:21:54.619928
# Unit test for method __call__ of class Register
def test_Register___call__():

    r = Register()

    r.set_rgb_call(RenderType.rgb_fg)
    r.set_eightbit_call(RenderType.eightbit_bg)

    class DummyFG:
        def __call__(self, *args, **kwargs):
            return "\x1b[38;2;{};{};{}m".format(*args)

    class DummyBG:
        def __call__(self, *args, **kwargs):
            return "\x1b[48;5;{}m".format(args[0])

    r.set_renderfunc(RenderType.rgb_fg, DummyFG())
    r.set_renderfunc(RenderType.eightbit_bg, DummyBG())


# Generated at 2022-06-14 08:22:02.840480
# Unit test for method __call__ of class Register
def test_Register___call__():
    fg = Register()
    setattr(fg, "blue", Style(RgbFg(0, 0, 255)))
    assert fg(10, 20, 30) == ""
    assert fg(0, 0, 255) == ""
    assert fg("blue") == ""
    assert fg(10, 20, 30, bold=True) == ""
    assert fg(0, 0, 255, bold=True) == ""
    assert fg("blue", bold=True) == ""

# Generated at 2022-06-14 08:22:13.230259
# Unit test for method mute of class Register
def test_Register_mute():

    from sty import fg

    oldval = fg.red
    fg.mute()

    assert oldval is not fg.red
    assert fg.red == ""



# Generated at 2022-06-14 08:22:19.869816
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    
    fg = Register()
    setattr(fg, "red", Style(RgbFg(1,5,10)))
    setattr(fg, "blue", Style(RgbFg(10,40,255)))
    setattr(fg, "green", Style(RgbFg(11,255,200)))

    reg = fg.as_namedtuple()
    assert isinstance(reg, NamedTuple)

# Generated at 2022-06-14 08:22:21.210985
# Unit test for method copy of class Register
def test_Register_copy():
    pass
# EOF

# Generated at 2022-06-14 08:22:22.711897
# Unit test for constructor of class Register
def test_Register():

    reg = Register()
    assert reg.is_muted is False


# Generated at 2022-06-14 08:22:33.844438
# Unit test for method unmute of class Register
def test_Register_unmute():
    from sty.rs import rs
    from sty.ansi_escape_code import Sgr

    r1 = Register()
    r2 = Register()

    r2.set_renderfunc(Sgr, lambda x: str(x))
    r2.rs = Style(Sgr(0))
    r2.reset = Style(Sgr(0))

    r2.mute()
    assert str(r2.reset) == ""
    assert str(r2.rs) == ""

    r2.unmute()
    assert str(r2.reset) == "\x1b[0m"
    assert str(r2.rs) == "\x1b[0m"
    r2.mute()

    # Compare r2 with r1

    # If a mutable object is used as a class attribute and mutate that object,

# Generated at 2022-06-14 08:22:39.738916
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    """
    Tests if the as_dict method returns a dict with all attributes that are not
    starting with an underscore.

    This also tests if the values in the dict are strings.

    If the test fails, an AssertionError will be raised.
    """

    class DummyRegister(Register):
        pass

    test_register = DummyRegister()
    test_register.foo = "foo"
    test_register._bar = "bar"
    test_register.baz = 0
    test_register.bam = Style(RgbFg(42, 57, 70,), Sgr(1))
    test_register.lol = Style(RgbFg(42, 57, 70,), Sgr(1), value="")

    d = test_register.as_dict()

    assert "foo" in d

# Generated at 2022-06-14 08:22:44.994952
# Unit test for method __new__ of class Style
def test_Style___new__():
    class Sgr(RenderType):
        """
        Placeholder for SGR-rendertype.
        """
        seq_str = "m"

    sgr = Sgr()

    style: Style = Style(sgr)

    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert str(style) == "\x1b[0m"

# Generated at 2022-06-14 08:22:58.475633
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertype import Bg, Fg

    reg = Register()
    reg.set_renderfunc(Fg, lambda x: f"Fg_{x}")
    reg.set_renderfunc(Bg, lambda x: f"Bg_{x}")

    # To see if this works properly we have to output the 8-bit calls to the console.
    reg.set_eightbit_call(Bg)
    reg.set_rgb_call(Fg)

    # The following line outputs Bg_144 to the console
    print(reg(144))  # --> Bg_144

    # The following line outputs Fg_10_42_255 to the console
    print(reg(10, 42, 255))  # --> Fg_10_42_255

# Generated at 2022-06-14 08:23:04.408014
# Unit test for method copy of class Register
def test_Register_copy():
    r = Register()
    r.red = Style(value="red")
    r.blue = Style(value="blue")
    r2 = r.copy()
    assert r == r2
    assert r is not r2
    assert r.red is not r2.red
    assert r.blue is not r2.blue
    assert r.red == r2.red
    assert r.blue == r2.blue

# Generated at 2022-06-14 08:23:15.594104
# Unit test for method unmute of class Register
def test_Register_unmute():
    # Create some sample data to test
    class DummyRegister(Register):
        # Sample attribute
        x = Style(RgbFg(1, 5, 10))

    def dummy_renderfunc(*args, **kwargs) -> str:
        return ""

    # Test if object behaves correctly after attribute x was unmuted
    reg = DummyRegister()
    reg.set_renderfunc(RgbFg, dummy_renderfunc)
    reg.mute()
    assert reg.is_muted == True
    assert str(reg.x) == ""
    reg.unmute()
    assert reg.is_muted == False
    assert str(reg.x) == "\x1b[38;2;1;5;10m"

# Generated at 2022-06-14 08:23:31.376777
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class R2(RenderType):
        args = (1, 2)
        renderfunc = lambda x, y: str(x) + ";" + str(y)

    class R1(RenderType):
        args = (1,)
        renderfunc = lambda x: str(x)

    class R3(RenderType):
        args = (1,)
        renderfunc = lambda x: str(x)

    # Test with one RenderType.
    r = Register()
    r.set_renderfunc(R1, lambda x: "R1")
    r.set_eightbit_call(R1)
    assert r(1) == "R1"
    del r

    # Test with two RenderTypes.
    r = Register()
    r.set_renderfunc(R1, lambda x: "R1")
    r.set_

# Generated at 2022-06-14 08:23:38.668551
# Unit test for method __new__ of class Style
def test_Style___new__():

    from .rendertypes import Sgr, RgbFg

    a = Style(Sgr(1), RgbFg(1, 1, 1), value="\x1b[38;2;1;1;1m\x1b[1m")

    assert isinstance(a, Style)
    assert isinstance(a, str)
    assert str(a) == "\x1b[38;2;1;1;1m\x1b[1m"



# Generated at 2022-06-14 08:23:47.803636
# Unit test for method __call__ of class Register
def test_Register___call__():

    r = Register()
    r.test = Style(Sgr(1))
    r.set_eightbit_call(Sgr)

    assert str(r) == ""
    assert str(r('test')) == "\x1b[1m"
    assert str(r(42)) == "\x1b[42m"

    r.mute()

    assert str(r) == ""
    assert str(r('test')) == ""
    assert str(r(42)) == ""

    r.unmute()

    assert str(r) == ""
    assert str(r('test')) == "\x1b[1m"
    assert str(r(42)) == "\x1b[42m"

# Generated at 2022-06-14 08:24:00.774919
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    class Sgr(RenderType):
        fmt = "\x1b[{}m"
    f1 = lambda *x: "".join(x)  # type: ignore
    r1 = Register()
    r1.set_renderfunc(Sgr, f1)

    def set_test_style(val, correct):
        setattr(r1, "test", val)
        assert getattr(r1, "test") == correct

    set_test_style(Style(Sgr(1), Sgr(2)), "\x1b[1m\x1b[2m")
    set_test_style(Style(Style(Sgr(1)), Sgr(2)), "\x1b[1m\x1b[2m")

# Generated at 2022-06-14 08:24:10.016553
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    """
    Test method as_namedtuple.
    """
    class TestRegister(Register):
        def __init__(self):
            super().__init__()
            self.color1 = Style(Sgr(49))
            self.color2 = Style(Sgr(38))

    # Create register-object from class TestRegister
    test_register: Register = TestRegister()

    # Create expected namedtuple
    expected = namedtuple("TestRegister", ["color1", "color2"])(color1="\x1b[49m", color2="\x1b[38m")

    # Get test result
    result = test_register.as_namedtuple()

    # Test assert
    assert expected == result

# Generated at 2022-06-14 08:24:22.621814
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    # Setup

    class Rgbfg(RenderType):
        """
        This render type represents the ANSI-escape-sequence for 24bit-background color.
        """

        name = "38;2"

    class Sgr(RenderType):
        """
        This render type represents the ANSI-escape-sequence for a style modifier such as bold, italic etc.
        """

        name = "0"

    def render_rgbfg(r: int, g: int, b: int) -> str:
        ansi_sequence = f"\x1b[38;2;{r};{g};{b}m"
        return ansi_sequence

    def render_sgr(n: int) -> str:
        ansi_sequence = f"\x1b[{n}m"
        return ansi_sequence

   

# Generated at 2022-06-14 08:24:35.564974
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    class RgbFg(RenderType):
        """
        A rendertype.
        """
    class Sgr(RenderType):
        """
        A rendertype.
        """
    
    def rgbfunc(r: int, g: int, b: int) -> str:
        """
        A renderfunc.
        """
        return ""
    def sgrfunc(x: int) -> str:
        """
        A renderfunc.
        """
        return ""

    register = Register()
    register.set_eightbit_call(RgbFg)
    assert isinstance(register.eightbit_call, Callable)

    register.set_renderfunc(RgbFg, rgbfunc)
    register.set_renderfunc(Sgr, sgrfunc)
    register.set_eightbit_call(Sgr)
   

# Generated at 2022-06-14 08:24:41.793864
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class RgbFg(RenderType):
        pass

    class Sgr(RenderType):
        pass

    register = Register()
    register.test = Style(Sgr(1), RgbFg(49, 42, 255))
    assert str(register.test) == r"\x1b[1m"

    def renderfunc(val, *args):
        return r"\x1b[38;2;{};{};{}m".format(args[0], args[1], args[2])

    register.set_renderfunc(RgbFg, renderfunc)
    assert str(register.test) == r"\x1b[1m\x1b[38;2;49;42;255m"



# Generated at 2022-06-14 08:24:45.060033
# Unit test for method copy of class Register
def test_Register_copy():

    class R(Register):
        pass

    r1 = R()
    r2 = r1.copy()

    assert id(r1) != id(r2)



# Generated at 2022-06-14 08:24:52.382826
# Unit test for method mute of class Register
def test_Register_mute():
    class MyRegister(Register):
        pass

    myreg = MyRegister()
    myreg.set_renderfunc(RenderType.SGR, lambda x: "SGR({})".format(x))
    myreg.red = Style(RenderType.SGR(1))
    assert myreg.red == "SGR(1)"
    myreg.mute()
    assert myreg.red == ""



# Generated at 2022-06-14 08:25:03.292651
# Unit test for constructor of class Register
def test_Register():
    """
    Test the constructor of class Register by creating a test-register and
    setting some known attributes.
    """
    r = Register()
    setattr(r, "test", Style(RgbFg(100, 100, 100)))
    assert r.test == "\x1b[38;2;100;100;100m"
    setattr(r, "test2", Style(Bg(), RgbFg(100, 100, 100)))
    assert r.test2 == "\x1b[48m\x1b[38;2;100;100;100m"

# Generated at 2022-06-14 08:25:04.644637
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    # TODO:
    pass


# Generated at 2022-06-14 08:25:15.912270
# Unit test for method mute of class Register
def test_Register_mute():
    def renderfunc(code, *args):
        return str(code)

    rendertype = NamedTuple("MyRenderType", [("args", Tuple[int, ...])])

    reg1 = Register()
    reg1.set_renderfunc(rendertype, renderfunc)

    reg1.set_eightbit_call(rendertype)
    reg1.set_rgb_call(rendertype)

    reg1.a = Style(rendertype(1), rendertype(2))
    reg1.b = Style(rendertype(3))
    reg1.c = Style(rendertype(4), rendertype(5))

    reg1.mute()

    assert str(reg1.a) == ""
    assert str(reg1.b) == ""
    assert str(reg1.c) == ""


# Generated at 2022-06-14 08:25:24.002760
# Unit test for method __call__ of class Register
def test_Register___call__():
    from sty import RenderType
    from sty import ef as eff
    from sty import fg as fore
    from sty import bg as back
    from sty import ef as effects

    import pytest

    # A custom register (you can use this for your own custom registers).
    class A(Register):
        red = Style(fore.red)
        green = Style(fore.green)

    a = A()
    a.set_eightbit_call(RenderType.SGR)

    # You can call a register-object with a integer argument and get the corresponding
    # style back.
    assert str(a(1)) == str(a.red)
    assert str(a(2)) != str(a.red)
    assert str(a(2)) == str(a.green)

    # You can call a register-object with a string

# Generated at 2022-06-14 08:25:34.992769
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    from .rendertype import RenderType

    # TODO (felix): Why did we need this?
    class Renderer(RenderType):
        def as_str(self, *args) -> str:
            return "".join(args)

        def as_bytes(self, *args) -> bytes:
            return "".join(args).encode()

    class TestRegister(Register):
        pass

    register = TestRegister()

    register.set_renderfunc(Renderer, lambda *args: "".join(args))

    register.red = Style(Renderer("F", "o", "o", "B", "a", "r"))

    assert register.red == "FooBar"

    assert register.as_dict() == {"red": "FooBar"}

# Generated at 2022-06-14 08:25:43.062061
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .render import RgbFg, Sgr

    FG = Register()

    FG.set_renderfunc(RgbFg, lambda r, g, b: f"{r},{g},{b}")
    FG.set_renderfunc(Sgr, lambda x: f"style:{x}")

    FG.blue = Style(RgbFg(0, 0, 255), Sgr(1))

    assert str(FG.blue) == str(FG(0, 0, 255))
    assert str(FG.blue) == str(FG("blue"))

# Generated at 2022-06-14 08:25:48.758613
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    # Test is type
    assert isinstance(Register().as_dict(), dict)

    # Test if all members are included
    r = Register()
    r.black = Style(RgbFg(0,0,0))
    r.white = Style(RgbFg(255,255,255))
    assert set(r.as_dict().items()) == {('white', '\x1b[38;2;255;255;255m'),('black', '\x1b[38;2;0;0;0m')}


# Generated at 2022-06-14 08:25:57.009714
# Unit test for method mute of class Register
def test_Register_mute():
    import sys

    # Create Register-instance
    r = Register()
    r.set_renderfunc(RenderType, lambda *x: f"\x1b[{x[0]};{x[1]}m")

    # Create a style attribute
    r.red = Style(RenderType(5, 1))

    # Test
    print(r.red, file=sys.stderr)
    r.mute()
    print(r.red, file=sys.stderr)



# Generated at 2022-06-14 08:25:59.763940
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert isinstance(register, Register), "Constructor of class Register failed."


# Generated at 2022-06-14 08:26:11.424411
# Unit test for method mute of class Register
def test_Register_mute():
    # Test a basic style object
    r = Register()
    r.renderfuncs = {RenderType: lambda x: f"{x}"}
    r.a = Style(RenderType(0))
    r.b = Style(RenderType(1), RenderType(2))

    assert str(r.a) == "0"
    assert str(r.b) == "12"

    r.mute()

    assert str(r.a) == ""
    assert str(r.b) == ""

    r.unmute()

    assert str(r.a) == "0"
    assert str(r.b) == "12"


# Generated at 2022-06-14 08:26:33.388118
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    # Test 1: Create a new register object and set attributes
    # -------------------------------------------------------------------------

    r1 = Register()

    # Test 1.1: Create style with a single render type and check if
    #           it behaves as expected.
    setattr(r1, "test1", Style(RgbFg(1, 2, 3), RgbBg(4, 5, 6)))
    assert isinstance(getattr(r1, "test1"), Style)
    assert str(getattr(r1, "test1")) == "\x1b[38;2;1;2;3m\x1b[48;2;4;5;6m"

    # Test 1.2: Create style with mutiple render types and check
    #           if it behaves as expected.

# Generated at 2022-06-14 08:26:41.798789
# Unit test for method copy of class Register
def test_Register_copy():
    r1 = Register()
    r1.foo = Style(RgbFg(10, 20, 30))
    r2 = r1.copy()
    r2.foo = Style(RgbFg(40, 50, 60))
    assert str(r1.foo) == '\x1b[38;2;10;20;30m'
    assert str(r2.foo) == '\x1b[38;2;40;50;60m'

# Generated at 2022-06-14 08:26:51.327708
# Unit test for method copy of class Register
def test_Register_copy():

    def _(a, b):
        return "test"

    r = Register()
    r.set_eightbit_call(object)
    r.set_renderfunc(object, _)
    r.test = Style(object(1), object(2))
    r.test2 = Style(object(2))

    r2 = r.copy()

    assert r._is_muted == r2._is_muted
    assert r.eightbit_call == r2.eightbit_call
    assert not r.renderfuncs == r2.renderfuncs

    assert r.test.rules == r2.test.rules
    assert r.test != r2.test



# Generated at 2022-06-14 08:26:57.679713
# Unit test for method __new__ of class Style
def test_Style___new__():
    value = Style(value="\x1b[38;2;1;5;10m\x1b[1m")
    assert isinstance(value, Style)
    assert isinstance(value, str)
    assert str(value) == "\x1b[38;2;1;5;10m\x1b[1m"

# Generated at 2022-06-14 08:27:08.262526
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    class RGBI:
        rgb = Register()
        rgb.r = Style(RgbFg(255, 0, 0))
        rgb.g = Style(RgbFg(0, 255, 0))
        rgb.b = Style(RgbFg(0, 0, 255))

    assert RGBI.rgb.as_namedtuple() == RGBI.rgb.as_namedtuple()
    assert RGBI.rgb.as_namedtuple() != RGBI.rgb.as_dict()
    assert RGBI.rgb.as_namedtuple().r == "\x1b[38;2;255;0;0m"
    assert RGBI.rgb.as_namedtuple().g == "\x1b[38;2;0;255;0m"
    assert RGBI.rgb.as_

# Generated at 2022-06-14 08:27:14.290636
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    class MyRegister(Register):
        mysty = Style(RgbFg(1, 2, 3))

    reg = MyRegister()
    d = reg.as_dict()

    assert isinstance(d, dict)
    assert "mysty" in d
    assert d["mysty"] == "\033[38;2;1;2;3m"



# Generated at 2022-06-14 08:27:15.918408
# Unit test for method __new__ of class Style
def test_Style___new__():
    assert issubclass(Style, str)
    assert isinstance(Style(), str)

# Generated at 2022-06-14 08:27:24.412024
# Unit test for method copy of class Register
def test_Register_copy():

    from .rendertype import Fg, RgbBg, RgbFg

    r = Register()
    r.renderfuncs = {Fg.__class__: lambda x: "Fg",
                     RgbFg.__class__: lambda r, g, b: "RgbFg",
                     RgbBg.__class__: lambda r, g, b: "RgbBg"}
    r.is_muted = False
    r.eightbit_call = lambda x: "Eigthbit"
    r.rgb_call = lambda r, g, b: "rgb"

    r.red = Style(RgbFg(1, 1, 1), Fg(1), RgbBg(1, 1, 1))

# Generated at 2022-06-14 08:27:26.002820
# Unit test for constructor of class Register
def test_Register():
    fg = Register()
    assert fg


# Generated at 2022-06-14 08:27:31.736338
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .register import Register

    r = Register()
    r.red = Style("\x1b[31m")
    r.green = Style("\x1b[32m")

    d = r.as_namedtuple()

    assert d.red == "\x1b[31m"
    assert d.green == "\x1b[32m"



# Generated at 2022-06-14 08:28:08.632322
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    class Mock:
        @staticmethod
        def render(x: int, y: int) -> str:
            return ""

    def render_func(x: int) -> str:
        return ""

    r = Register()

    r.set_renderfunc(Mock, render_func)

    a = Style(Mock(1, 2))
    b = Style(Mock(1, 2))
    c = Style(Mock(1, 2))

    r.a = a
    r.b = b
    r.c = c

    assert hasattr(r, "a")
    assert hasattr(r, "b")
    assert hasattr(r, "c")

    r.b = Style(Mock(2, 3))

    assert hasattr(r, "a")
    assert hasattr(r, "b")

# Generated at 2022-06-14 08:28:12.591674
# Unit test for method unmute of class Register
def test_Register_unmute():

    from sty import fg

    # This is the call that we want to test:
    fg.black.unmute()

    # 1. Check if all style attributes have a value.
    for attr_name in dir(fg):
        assert getattr(fg, attr_name) != ""


# Generated at 2022-06-14 08:28:15.035758
# Unit test for constructor of class Style
def test_Style():
    assert Style() == ""
    assert Style(value="Test") == "Test"



# Generated at 2022-06-14 08:28:27.335093
# Unit test for method __call__ of class Register
def test_Register___call__():

    # The test-register for testing the __call__ method.
    @Register.create("TestRegister")
    class TestRegister(Register):
        pass

    # Rendertype for the next test-renderfunctions.
    class TestRenderer(RenderType):
        @staticmethod
        def renderfunc(*args):
            return f"TestRenderer:{args}"

    # Renderfunctions that use the TestRenderer.
    def renderfunc_int(*args):
        return f"int:{args}"

    def renderfunc_str(*args):
        return f"str:{args}"

    def renderfunc_rgb(*args):
        return f"rgb:{args}"

    register = TestRegister()

    # Check if __call__ returns empty string if register-object is muted.
    register.mute()

    assert register() == ""

   

# Generated at 2022-06-14 08:28:35.368283
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    import sty
    import ansiwrap

    def custom_renderfunc(r, g, b) -> str:
        return f"<{r}, {g}, {b}>"

    # create a new register object
    reg = Register()

    # add a new render function to the register
    reg.set_renderfunc(sty.RgbFg, custom_renderfunc)

    # create a new style
    reg.my_style = sty.Style(sty.RgbFg(100, 200, 100))

    # test whether the new render function has been applied
    assert str(reg.my_style) == "<100, 200, 100>"

    # test whether custom render func is used for rgb-calls
    assert reg(10, 10, 10) == "<10, 10, 10>"

    # test whether custom render func is used for eightbit-

# Generated at 2022-06-14 08:28:38.536098
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    from .fg import fg

    fg.violet = Style(RgbFg(128, 0, 128))

    d = fg.as_dict()

    assert d["violet"] == "\x1b[38;2;128;0;128m"

# Generated at 2022-06-14 08:28:47.891057
# Unit test for method copy of class Register
def test_Register_copy():
    """
    Testing the copy-method of Register.
    """
    from .render import fg, bg
    from .rendertype import RgbBg

    # Setup Register objects that are to be copied.
    r1 = Register()
    r1.magenta = Style(RgbBg(100, 200, 255))
    r1.red = Style()
    r2 = Register()
    r2.magenta = Style(RgbBg(144, 34, 78))
    r2.blue = Style()

    # Setup copy of Register objects.
    r1_copy = r1.copy()
    r2_copy = r2.copy()

    # Change values of originals
    r1.magenta = Style(RgbBg(1, 2, 3))
    del r1.red
    del r2.magenta

# Generated at 2022-06-14 08:29:01.499384
# Unit test for method mute of class Register
def test_Register_mute():

    from . import fg
    from .rendertype import RgbFg

    # Create a test-register
    test_register = Register()

    # Create style-attributes
    test_register.red = Style(RgbFg(255, 0, 0))
    test_register.green = Style(RgbFg(0, 255, 0))
    test_register.blue = Style(RgbFg(0, 0, 255))

    # Set standard render-funcs of register-object
    test_register.set_eightbit_call(type(fg))
    test_register.set_rgb_call(type(fg))
    test_register.set_renderfunc(type(fg), lambda *args: "\x1b[38;2;" + ";".join(map(str, args)) + "m")

    # Test

# Generated at 2022-06-14 08:29:10.220625
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    """
    Make sure that if a register style is changed, the ANSI-code is updated.
    """

    r = Register()
    r.bold = Style(RgbFg(255, 255, 255))
    r.italic = Style(RgbFg(0, 0, 0))

    assert str(r.bold) == "\x1b[38;2;255;255;255m"
    assert str(r.italic) == "\x1b[38;2;0;0;0m"

    r.bold.rules = [RgbFg(0, 0, 0)]
    r.italic.rules = [RgbFg(255, 255, 255)]

    assert str(r.bold) == "\x1b[38;2;0;0;0m"

# Generated at 2022-06-14 08:29:14.198081
# Unit test for method unmute of class Register
def test_Register_unmute():
    r = Register()
    test_color = Style(RgbFg(1,2,3))
    r.blue = test_color
    assert r.blue != '\x1b[38;2;1;2;3m'
    assert r.blue != test_color
    r.unmute()
    assert r.blue == '\x1b[38;2;1;2;3m'
    assert r.blue == test_color

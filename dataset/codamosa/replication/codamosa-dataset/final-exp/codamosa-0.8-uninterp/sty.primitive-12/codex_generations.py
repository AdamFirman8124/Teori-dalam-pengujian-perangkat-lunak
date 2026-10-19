

# Generated at 2022-06-14 08:21:04.664806
# Unit test for method mute of class Register
def test_Register_mute():
    from .register import fg, bg, ef, rs

    fg.mute()

    assert fg.muted is True

    assert fg.red == ""

    assert str(bg.cyan + ef.bold + "Hello World") == ""

    fg.yellow(ef.italic + "Hello World") == ""

    bg.mute()

    assert bg.muted is True

    assert ef.underline + "Hello World" == ""

    bg.unmute()

    assert bg.muted is False

    ef.mute()

    assert ef.muted is True

    rs.mute()

    assert rs.muted is True

    rs.unmute()

    assert rs.muted is False



# Generated at 2022-06-14 08:21:10.631204
# Unit test for method __new__ of class Style
def test_Style___new__():
    class Rule(str):
        pass
    
    r1 = Rule("testrule")
    s1 = Style(r1, value="test")
    assert isinstance(s1, str)
    assert isinstance(s1, Style)
    assert str(s1) == "test"
    assert s1.rules == (r1,)



# Generated at 2022-06-14 08:21:22.763553
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    # Initialize register
    class TestRegister(Register):
        pass

    test_register = TestRegister()

    # Create test-render-type for easy testing
    class TestRenderType(RenderType):
        index: int

        def __init__(self, index: int):
            self.index = index

    # Create test render-func
    def test_render_func(*_):
        return f"\x1b[48;5;{TestRenderType.index}m"

    # set render func
    test_register.set_renderfunc(TestRenderType, test_render_func)
    assert hasattr(test_register, "renderfuncs")
    assert TestRenderType in test_register.renderfuncs.keys()
    assert test_register.renderfuncs[TestRenderType] == test_render_func

    # Add style

# Generated at 2022-06-14 08:21:35.273124
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    fg = Register()
    fg.brown = Style(RgbFg(0.5, 0.2, 0.1))
    fg.blue = Style(RgbFg(0.1, 0.2, 0.5))
    fg.red = Style(RgbFg(0.5, 0.2, 0.1), Sgr(1))
    fg.yellow = Style(RgbFg(0.5, 0.4, 0.1), Sgr(3))
    fg.green = Style(RgbFg(0.2, 0.5, 0.1), Sgr(4))
    fg.red_ = Style(RgbFg(1, 0, 0), Sgr(9))

# Generated at 2022-06-14 08:21:41.523608
# Unit test for method __call__ of class Register
def test_Register___call__():

    class CustomRegister(Register):
        def __init__(self):
            super().__init__()
            self.red = "red"
            self.green = "green"

    reg = CustomRegister()

    assert reg("green") == "green"
    assert reg("red") == "red"
    assert reg("yellow") == ""



# Generated at 2022-06-14 08:21:49.194019
# Unit test for method unmute of class Register
def test_Register_unmute():

    # Create a register-object with a style.
    import sty
    r: Register = sty.Register()
    r.test_style = sty.Style(sty.fg.red)
    print(f"Before unmute: {r.test_style}")

    # Activate mute.
    r.mute()
    print(f"During mute: {r.test_style}")

    # Activate unmute.
    r.unmute()
    print(f"After unmute: {r.test_style}")

# Generated at 2022-06-14 08:21:55.071183
# Unit test for method copy of class Register
def test_Register_copy():

    from sty import fg, bg, ef, rs
    
    assert fg.red is fg.red

    fg2 = fg.copy()

    assert fg.red is fg2.red

    fg.blue.rules = [RgbBg(42, 42, 42)]
    assert fg.blue.rules[0] is not fg2.blue.rules[0]

    ef2 = ef.copy()

    assert ef.bold is ef.bold
    assert ef2.bold is ef2.bold

# Generated at 2022-06-14 08:22:07.785811
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from .rendertype import Sgr, RgbFg, RgbBg
    from .renderfunc import render_sgr, render_rgb_fg

    # Create register object
    register = Register()

    # Add a renderfunc for rendertype Sgr
    register.set_renderfunc(Sgr, render_sgr)

    # Add a renderfunc for rendertype RgbFg and RgbBg
    register.set_renderfunc(RgbFg, render_rgb_fg)
    register.set_renderfunc(RgbBg, render_rgb_fg)

    # Define a new style

# Generated at 2022-06-14 08:22:15.554314
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class TestRegister(Register):

        def __init__(self):
            super().__init__()

    rgba = TestRegister()
    rgba.test = Style(RgbFg(1,2,3), RgbBg(2,3,4), Sgr(1))
    assert isinstance(rgba.test, Style)
    assert isinstance(rgba.test, str)
    assert rgba.test == '\x1b[38;2;1;2;3m\x1b[48;2;2;3;4m\x1b[1m'

    rgba.test = Style(RgbFg(1,2,3), RgbBg(2,3,4), Sgr(1))
    assert isinstance(rgba.test, Style)

# Generated at 2022-06-14 08:22:23.382092
# Unit test for constructor of class Register
def test_Register():

    class Foo:
        pass

    r = Register()
    assert r.renderfuncs == {}
    assert r.is_muted is False
    assert r.eightbit_call(144) == 144
    assert r.rgb_call(10, 42, 255) == (10, 42, 255)

    with raises(AttributeError):

        r.test = Foo
        r.test = 5
        r.test = []
        r.test = Style()
        r.test = register.fg.blue


# Generated at 2022-06-14 08:22:31.298926
# Unit test for method __new__ of class Style
def test_Style___new__():
    # Setup
    rules = [1]
    value = ""
    style = Style(*rules, value=value)

    # Assertion
    assert style == value
    assert style.rules == rules



# Generated at 2022-06-14 08:22:35.472740
# Unit test for method mute of class Register
def test_Register_mute():
    from .rendertype import Eightbit
    from .constants import fg, bg

    fg.blue = Style(Eightbit(4))
    fg.mute()
    assert fg.blue == ""

# Generated at 2022-06-14 08:22:39.197108
# Unit test for method __new__ of class Style
def test_Style___new__():

    x = Style("asd", "zxc")
    assert isinstance(x, str)
    assert x == "asdzxc"
    assert x.rules == ("asd", "zxc")

# Generated at 2022-06-14 08:22:48.039721
# Unit test for method copy of class Register
def test_Register_copy():

    from . import fg, rs

    fg.red = Style(fg.Red)
    fg.green = Style(fg.Green)

    fg_copy = fg.copy()

    assert fg.red == fg_copy.red
    assert fg.green == fg_copy.green

    fg.red = Style(fg.Green)
    fg_copy.green = Style(fg.Red)

    assert fg.red != fg_copy.red
    assert fg.green != fg_copy.green
    assert fg.red == fg_copy.green
    assert fg.green == fg_copy.red

    assert not fg.rgb is fg_copy.rgb
    assert fg.rgb_call is not fg_copy.rgb_call

# Generated at 2022-06-14 08:22:52.560179
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    fg_namedtuple = fg.as_namedtuple()
    assert fg_namedtuple.red == "\x1b[31m"
    assert fg_namedtuple.green == "\x1b[32m"

# Generated at 2022-06-14 08:23:00.164543
# Unit test for method mute of class Register
def test_Register_mute():
    """
    Test :class:`Register` mute method.
    """
    register = Register()
    func_one = lambda x, y: x
    func_two = lambda x, y: y
    register.set_renderfunc(Type, func_one)
    register.set_renderfunc(Type, func_two)
    register.blue = Style(Type(1, 2), Type(3, 4))
    assert str(register.blue) == func_two(3, 4)
    register.mute()
    assert str(register.blue) == ""

# Generated at 2022-06-14 08:23:04.237467
# Unit test for constructor of class Style
def test_Style():
    Style(RgbFg(0, 255, 0))
    Style(RgbBg(100, 255, 100), Sgr(1))
    Style(RgbFg(10, 20, 30), RgbBg(10, 20, 30), Sgr(1), Sgr(2))

# Generated at 2022-06-14 08:23:05.900465
# Unit test for constructor of class Register
def test_Register():
    reg = Register()
    assert isinstance(reg, Register)



# Generated at 2022-06-14 08:23:10.491380
# Unit test for method __new__ of class Style
def test_Style___new__():
    style = Style(Sgr(1), Sgr(2))
    assert isinstance(style, Style)
    assert style.rules == (Sgr(1), Sgr(2))
    assert str(style) == "\033[1m\033[2m"


# Generated at 2022-06-14 08:23:20.786852
# Unit test for method __call__ of class Register
def test_Register___call__():

    class TestRegister(Register):

        def __init__(self):
            super().__init__()
            self.renderfuncs = {int: lambda x: f"{x}-renderfunc",
                                str: lambda x: f"{x}-renderfunc"}
            self.eightbit_call = self.renderfuncs[int]
            self.rgb_call = self.renderfuncs[str]

    r = TestRegister()

    # Test Eightbit-calls
    assert r(42) == "42-renderfunc"

    # Test rgb-calls
    assert r(10, 20, 30) == "10-renderfunc20-renderfunc30-renderfunc"

    # Test attr-calls
    r.x = Style(42)
    assert r("x") == "42"



# Generated at 2022-06-14 08:23:28.715362
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .rendertype import Sgr
    from .registers import fg

    s = Style(Sgr(1))
    fg.bold = s
    fg.mute()

    assert fg.bold == ""

    fg.unmute()

    assert fg.bold != ""



# Generated at 2022-06-14 08:23:37.441646
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    from .fgcodes import fg
    from .bgcodes import bg
    from .sgrcodes import bold
    from .rgb import rgb256_to_ansi

    fg.red = Style(fg.fg_red, bold)
    fg.green = Style(fg.fg_green, bold)
    fg.blue = Style(fg.fg_blue, bold)

    bg.red = Style(bg.bg_red, bold)
    bg.green = Style(bg.bg_green, bold)
    bg.blue = Style(bg.bg_blue, bold)

    fg.gray = Style(fg.fg_gray, bold)
    bg.gray = Style(bg.bg_gray, bold)


# Generated at 2022-06-14 08:23:41.742427
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    class C(Register):
        def __init__(self):
            super().__init__()
            setattr(self, "a", 12)  # type: ignore

    c = C()
    assert c.a == 12

# Generated at 2022-06-14 08:23:51.457892
# Unit test for method copy of class Register
def test_Register_copy():

    fg = Register()
    fg.red = Style(RgbFg(255, 0, 0))

    fg_copy = fg.copy()

    assert fg.red == fg_copy.red
    assert fg.red != fg_copy.blue

    fg_copy.blue = Style(RgbFg(0, 0, 255))

    assert fg.red != fg_copy.red
    assert fg.red != fg_copy.blue
    assert fg.blue != fg_copy.red
    assert fg.blue != fg_copy.blue

# Generated at 2022-06-14 08:23:56.296516
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    reg = Register()

    styled_attr = Style("\x1b[0m")
    setattr(reg, "default", styled_attr)

    assert styled_attr.rules == reg.default.rules
    assert styled_attr == reg.default


# Generated at 2022-06-14 08:24:00.097402
# Unit test for constructor of class Style
def test_Style():
    # Arrange
    rules: Iterable[StylingRule] = [1,2, 3]
    style = Style("a")

    # Act
    new_style = Style(*rules, value="")

    # Assert
    assert isinstance(new_style, Style)
    assert isinstance(new_style, str)
    assert new_style.rules == rules



# Generated at 2022-06-14 08:24:03.608475
# Unit test for constructor of class Register
def test_Register():
    new_register = Register()
    assert new_register
    assert isinstance(new_register.renderfuncs, dict)

# Generated at 2022-06-14 08:24:15.840658
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    import pytest, sty
    from sty.ansi import RgbFg, Sgr

    class TestRegister(Register):
        x = Style(RgbFg(1,2,3))
        x2 = Style(Sgr(1, Sgr(4)))

    def func(r: int, g: int, b: int) -> str:
        return "RGB(" + str(r) + ", " + str(g) + ", " + str(b) + ")"

    styl = TestRegister()
    styl.set_rgb_call(rendertype=RgbFg)
    styl.set_renderfunc(rendertype=RgbFg, func=func)

    assert styl.x2 == "\x1b[1m\x1b[4m"
    assert styl.x == "RGB(1, 2, 3)"

# Generated at 2022-06-14 08:24:25.359005
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertypes import RgbBg, RgbFg, Sgr

    # Create register for foreground and background color
    fg = Register()
    bg = Register()

    # Set render functions for these registers
    fg.set_renderfunc(RgbFg, lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m")
    bg.set_renderfunc(RgbBg, lambda r, g, b: f"\x1b[48;2;{r};{g};{b}m")

    # Define some styles
    fg.red = Style(RgbFg(255, 0, 0))
    fg.bg_red = Style(RgbBg(255, 0, 0))

# Generated at 2022-06-14 08:24:26.832376
# Unit test for constructor of class Style
def test_Style():
    assert isinstance("a", Style)


# Generated at 2022-06-14 08:24:31.645086
# Unit test for constructor of class Style
def test_Style():
    r1 = Style()
    assert len(r1) == 0

    r2 = Style("hello")
    assert len(r2) == 5



# Generated at 2022-06-14 08:24:40.741817
# Unit test for constructor of class Style
def test_Style():
    """
    Create a new Style object.
    """
    bold = Style(RgbFg(255, 255, 255), Sgr(1))
    assert isinstance(bold, Style)
    assert bold == "\x1b[38;2;255;255;255m\x1b[1m"
    assert bold.rules == (RgbFg(255, 255, 255), Sgr(1))
    bold.rules == (RgbFg(255, 255, 255), Sgr(1))
    bold = Style(RgbBg(0, 52, 122), Sgr(3))
    assert bold == "\x1b[48;2;0;52;122m\x1b[3m"
    assert bold.rules == (RgbBg(0, 52, 122), Sgr(3))
    bold = Style

# Generated at 2022-06-14 08:24:45.718700
# Unit test for method __new__ of class Style
def test_Style___new__():
    from .rendertype import RgbFg, Sgr
    style = Style(RgbFg(1,5,10), Sgr(1))
    assert str(style) == "\x1b[38;2;1;5;10m\x1b[1m"


# Generated at 2022-06-14 08:24:53.435680
# Unit test for method __call__ of class Register
def test_Register___call__():

    class TestRegister(Register):
        def __init__(self):
            super().__init__()
            self.renderfuncs = {int: lambda x: f"{x}"}

        def foo(self):
            return "bar"

    tr = TestRegister()
    assert tr(0) == "0"
    assert tr(42) == "42"
    assert tr(foo="bar") == ""
    assert tr("foo") == "bar"

# Generated at 2022-06-14 08:24:56.601812
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .sty import sty
    assert sty.fg.red == sty.fg.red.as_namedtuple().red


# Generated at 2022-06-14 08:24:58.936201
# Unit test for constructor of class Register
def test_Register():
    r: Register = Register()

    assert isinstance(r, Register)


# Generated at 2022-06-14 08:25:07.805275
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    from .registers import fg

    # Before we can call as_dict, we need to set some styles
    def render(code):
        return f"\x1b[38;5;{code}m"

    fg.set_renderfunc(RenderType.Eightbit, render)

    fg.red = Style(RenderType.Eightbit(1))

    fg.test = Style(RenderType.Eightbit(2))

    data = fg.as_dict()

    # Should be {'red': '\x1b[38;5;1m', 'test': '\x1b[38;5;2m'}
    assert data == {"red": "\x1b[38;5;1m", "test": "\x1b[38;5;2m"}


# Generated at 2022-06-14 08:25:14.694274
# Unit test for method mute of class Register
def test_Register_mute():
    import sty

    nr = sty.NumberRegister()
    nr.set_renderfunc(sty.RgbBg, sty.RgbBg)
    nr.set_rgb_call(sty.RgbBg)
    assert nr(12, 34, 56) == "\x1b[48;2;12;34;56m"
    nr.mute()
    assert nr(12, 34, 56) == ""


# Generated at 2022-06-14 08:25:21.775999
# Unit test for method copy of class Register
def test_Register_copy():
    from .rendertype import Sgr
    from .register import Register
    r1 = Register()
    r1.set_renderfunc(Sgr, lambda x: f"\x1b{x}")
    r1.bold = Style(Sgr(1))
    r1.underline = Style(Sgr(4))

    r2 = r1.copy()
    assert(r2.is_muted == r1.is_muted)
    assert(r2.underline == r1.underline)
    assert(r2.bold == r1.bold)
    assert(r2.renderfuncs == r1.renderfuncs)

# Generated at 2022-06-14 08:25:31.836353
# Unit test for method copy of class Register
def test_Register_copy():

    register: Register = Register()

    # Set renderfunc
    renderfunc: Callable = lambda x: "test_function_call"
    register.set_renderfunc(RenderType, renderfunc)

    # Set eightbit rendertype
    rendertype: Type[RenderType] = RenderType
    register.set_eightbit_call(rendertype)

    # Add style
    register.test_style = Style(rendertype(42))

    # Copy register
    copied_register: Register = register.copy()

    # Assert that renderfuncs are equal
    assert register.renderfuncs == copied_register.renderfuncs

    # Assert that eightbit_call is equal
    assert register.eightbit_call == copied_register.eightbit_call

    # Assert that style 'test_style' is equal
    assert register.test_style == copied

# Generated at 2022-06-14 08:25:38.653582
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r.renderfuncs == {}
    assert r.is_muted is False


# Generated at 2022-06-14 08:25:48.283557
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from .rendertype import Fg, RenderType

    class Fg8(RenderType):
        """
        Just a stub for unit test.
        """

    class Fg24(RenderType):
        """
        Just a stub for unit test.
        """

    def render_fg8(stub, n: int) -> str:
        return f"{stub}{n}"

    def render_fg24(stub, r: int, g: int, b: int) -> str:
        return f"{stub};{r};{g};{b}"

    rs = Register()

    rs.set_renderfunc(Fg8, render_fg8)
    rs.set_renderfunc(Fg24, render_fg24)

    rs.set_eightbit_call(Fg8)
    rs.set_rgb

# Generated at 2022-06-14 08:26:00.330204
# Unit test for method __call__ of class Register
def test_Register___call__():
    """
    Ensure Register class works as expected
    """
    def _mock_render_call_muted(value: str) -> str:
        """
        Function that is called as a "render_call" with muted register
        """
        return str(value)

    def _mock_render_call(value: str) -> str:
        """
        Function that is called as a "render_call" with normal register
        """
        return f"{str(value)}{str(value)}"

    def _mock_render_call_int(value: int) -> str:
        """
        Function that is called as a "render_call" when using integers
        """
        return str(value)

    # Create register with render_call
    register = Register()

# Generated at 2022-06-14 08:26:11.103075
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class RgbFg(RenderType):
        pass

    class Sgr(RenderType):
        pass

    class MyRegister(Register):
        pass

    r = MyRegister()
    r.set_renderfunc(RgbFg, lambda *args: f"{args[0]}, {args[1]}, {args[2]}")
    r.set_renderfunc(Sgr, lambda *args: f"{args[0]}")
    r.blue = Style(RgbFg(0, 0, 255), Sgr(1))

    assert r.blue == "0, 0, 255, 1"


# Generated at 2022-06-14 08:26:16.775089
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class TestRenderType(RenderType):
        def render(self) -> str:
            return f"Test {self.args[0]}"

    # Create dummy instance of Register.
    r = Register()

    # Set method that holds implementation for TestRenderType.
    r.set_renderfunc(TestRenderType, lambda arg: arg)

    # Create style with render-type TestRenderType with arg 42.
    r.test = Style(TestRenderType(42))

    # Create style with render-type TestRenderType with arg 41,42.
    r.test2 = Style(TestRenderType(41), TestRenderType(42))

    # Create style with render-type TestRenderType with arg 40,41,42 and
    # string value 'T'.

# Generated at 2022-06-14 08:26:30.781974
# Unit test for method __call__ of class Register
def test_Register___call__():

    class TestRegister(Register):

        def __init__(self):
            super().__init__()
            self.foo = Style(value="foo")
            self.bar = Style(value="bar")
            self.baz = Style(value="baz")

            def eightbit_call_func(x: int) -> str:
                return str(x)

            def rgb_call_func(r: int, g: int, b: int) -> str:
                return str(r) + str(g) + str(b)

            self.set_eightbit_call(eightbit_call_func)
            self.set_rgb_call(rgb_call_func)

    r = TestRegister()

    assert r("foo") == "foo"
    assert r(1) == "1"

# Generated at 2022-06-14 08:26:32.767066
# Unit test for constructor of class Style
def test_Style():
    sty = Style(value="foo", rules=["bar", Style("bazz")])
    assert sty.value == "foo"
    assert sty.rules == ["bar", Style("bazz")]



# Generated at 2022-06-14 08:26:45.929325
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    from .defaults import fg, bg, ef, rs

    class_ = Register.as_namedtuple.__func__.__globals__["namedtuple"]
    nt_fg = class_("fg", fg.as_dict().keys())(*fg.as_dict().values())
    nt_bg = class_("bg", bg.as_dict().keys())(*bg.as_dict().values())
    nt_ef = class_("ef", ef.as_dict().keys())(*ef.as_dict().values())
    nt_rs = class_("rs", rs.as_dict().keys())(*rs.as_dict().values())

    assert isinstance(nt_fg, NamedTuple)
    assert isinstance(nt_bg, NamedTuple)
    assert isinstance

# Generated at 2022-06-14 08:26:49.031254
# Unit test for constructor of class Register
def test_Register():
    class A:
        pass

    a = Register()
    assert isinstance(a, Register)

    a = A()
    assert isinstance(a, A)

# Generated at 2022-06-14 08:26:54.636997
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    _register = Register()

    _register.set_rgb_call(RgbBg)

    _register.rgb_call(10, 42, 255)

    _register.set_rgb_call(RgbFg)

    _register.rgb_call(10, 42, 255)


# Generated at 2022-06-14 08:27:07.838365
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .rendertype import EightBit, RgbFg

    def eightbit_call(n: int) -> str:
        return f"{EightBit(n)}\n"

    def rgb_call(r: int, g: int, b: int) -> str:
        return f"{RgbFg(r, g, b)}\n"

    reg = Register()
    reg.set_eightbit_call(EightBit)
    reg.set_rgb_call(RgbFg)

    assert reg(42) == eightbit_call(42)
    assert reg(10, 42, 255) == rgb_call(10, 42, 255)

# Generated at 2022-06-14 08:27:17.185448
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    test_register = Register()
    test_register.black = Style(RgbFg(0, 0, 0))
    test_register.white = Style(RgbFg(255, 255, 255), Sgr(1))

    assert isinstance(test_register.as_namedtuple(), namedtuple)
    assert test_register.as_namedtuple().black == "\x1b[38;2;0;0;0m"
    assert test_register.as_namedtuple().white == "\x1b[38;2;255;255;255m\x1b[1m"


# Generated at 2022-06-14 08:27:25.813524
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from .rendertype import Sgr

    class testRegister(Register):
        pass

    testRegister.renderfuncs[Sgr] = lambda x: "Sgr:" + str(x)

    r1 = testRegister()
    assert(not hasattr(r1, "test_attr"))

    r1.test_attr = Style(Sgr(1))
    r1.test_attr_2 = Style(Sgr(1), Sgr(2))

    assert(r1.test_attr == "Sgr:1")
    assert(r1.test_attr_2 == "Sgr:1Sgr:2")

# Generated at 2022-06-14 08:27:36.708404
# Unit test for constructor of class Style
def test_Style():
    assert Style() == ""
    assert Style("", Sgr(1)) == "\x1b[1m"
    assert Style("" * 2, Sgr(1)) == "\x1b[1m\x1b[1m"
    assert Style("", Sgr(1), Sgr(23)) == "\x1b[1m\x1b[23m"
    assert Style("", Sgr(1), Sgr(23), Sgr(2)) == "\x1b[1m\x1b[23m\x1b[2m"
    assert Style(Sgr(1), Sgr(23), Sgr(2), Sgr(4)) == "\x1b[1m\x1b[23m\x1b[2m\x1b[4m"

# Generated at 2022-06-14 08:27:42.364124
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .fg import fg, RgbFg

    # Create a styling rule:
    fg.test_red = RgbFg(255, 0, 0)

    # Create a named tuple from the styling rule:
    NamedtupleRegister = fg.as_namedtuple()

    # We can use it like any other namedtuple:
    assert NamedtupleRegister.test_red == '\x1b[38;2;255;0;0m'

# Generated at 2022-06-14 08:27:53.096485
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    import sty

    sty.register_style_name(sty.Style, "Style")
    sty.register_style_name(sty.RgbFg, "RgbFg")
    sty.mute()

    fg = sty.fg.copy()

    fg.black = Style(RgbFg(0,0,0))
    fg.white = Style(RgbFg(255,255,255))

    style_register = fg.as_namedtuple()

    sty.unmute()

    assert style_register.black == "\x1b[38;2;0;0;0m"
    assert style_register.white == "\x1b[38;2;255;255;255m"

# Generated at 2022-06-14 08:28:05.464238
# Unit test for method mute of class Register
def test_Register_mute():

    r = Register()
    r.set_renderfunc(RenderType, RenderType.color_render_func)
    r.red = Style(RenderType(81))
    r.orange = Style(RenderType(82), RenderType(1))

    assert str(r.red) == "\x1b[38;2;255;0;0m"
    assert str(r.orange) == "\x1b[38;2;255;127;0m\x1b[1m"

    r.mute()

    assert str(r.red) == ""
    assert str(r.orange) == ""

    r.unmute()

    assert str(r.red) == "\x1b[38;2;255;0;0m"

# Generated at 2022-06-14 08:28:14.424845
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    # ----------------- Simple test -----------------

    # Set up
    a = Register()
    setattr(a, "test", Style(RgbFg(1, 2, 3)))

    # Assert
    assert isinstance(a.test, Style)
    assert a.test.rules == (RgbFg(1, 2, 3),)

    # ----------------- Nested Style -----------------

    # Set up
    a = Register()
    setattr(a, "test", Style(Style(RgbFg(1, 2, 3))))

    # Assert
    assert isinstance(a.test, Style)
    assert isinstance(a.test.rules[0], Style)
    assert a.test.rules[0].rules == (RgbFg(1, 2, 3),)

    # ----------------- Muted -----------------

    # Set

# Generated at 2022-06-14 08:28:27.867377
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    from .rendertype import RgbFg, SgrFg

    # Create register instance with both renderfunc-types
    reg = Register()
    reg.set_renderfunc(RgbFg, lambda x: " \x1b[38;2;{};{};{}m".format(x, x, x))
    reg.set_renderfunc(SgrFg, lambda x: " \x1b[38;5;{}m".format(x))

    # Define default rendertype
    reg.set_eightbit_call(RgbFg)

    # Check if call of register-object with color input is routed to
    # the right rendertype
    assert reg(100) == " \x1b[38;2;100;100;100m"



# Generated at 2022-06-14 08:28:35.841891
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from .rendertype import RgbBg

    r1 = Register()
    r1.set_renderfunc(RgbBg, lambda r, g, b: f"\x1b[48;2;{r};{g};{b}m")

    r1.test_color = Style(RgbBg(1, 2, 3))
    assert getattr(r1, "test_color") == "\x1b[48;2;1;2;3m"
    assert r1.test_color == "\x1b[48;2;1;2;3m"
    assert isinstance(r1.test_color, Style)
    assert isinstance(r1.test_color, str)

    r1.mute()
    assert getattr(r1, "test_color") == ""
    assert r1

# Generated at 2022-06-14 08:28:52.461284
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .fg import fg
    from .bg import bg
    from .ef import ef
    from .rs import rs

    fg.red = Style(RgbFg(255, 0, 0), Sgr(1))
    bg.blue = Style(RgbBg(0, 255, 0), Sgr(1))
    ef.bold = Style(Sgr(1))
    rs.reset = Style(Sgr(0))

    # It's important that *all* styles get muted at once so that
    # they all will get remade with the new renderfuncs.
    fg.mute()
    bg.mute()
    ef.mute()
    rs.mute()

    # Check that *all* styles are muted.
    assert fg.red == ""
    assert bg.blue

# Generated at 2022-06-14 08:29:02.073915
# Unit test for method __call__ of class Register
def test_Register___call__():

    class CustomRegister(Register):
        pass

    # Test if the eightbit_call works properly.
    r1 = CustomRegister()
    r1.set_eightbit_call(RenderType.ANSI_256)
    r1.set_renderfunc(RenderType.ANSI_256, lambda x: str(x))
    assert r1(42) == "42"
    r1.mute()
    assert r1(42) == ""
    r1.unmute()
    assert r1(42) == "42"
    assert r1("black") == ""



# Generated at 2022-06-14 08:29:10.532330
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from sty import fg

    # No need to test this method. Instead, we can test it indirectly
    # by declaring a namedtuple using the result of the method and comparing
    # two namedtuple instances.

    # Setup Register
    r = Register()
    r.set_eightbit_call(lambda x: "")
    r.set_rgb_call(lambda r, g, b: "")
    r.hello = Style("HELLO")
    r.world = Style("WORLD")

    # Setup NamedTuple
    NT = r.as_namedtuple()

    # Check equality
    assert NT.hello == "HELLO"
    assert isinstance(NT, namedtuple)
    assert isinstance(NT.hello, str)
    assert isinstance(NT.world, str)

    # Check if fg is

# Generated at 2022-06-14 08:29:17.820070
# Unit test for constructor of class Style
def test_Style():

    class foobar(RenderType):
        pass

    def render_foobar(arg1):
        return arg1

    sty = Register()
    sty.set_renderfunc(foobar, render_foobar)

    sty.foo = Style(foobar('bar'))
    sty.foobaz = Style(foobar('baz'))

    assert sty.foo == 'bar'
    assert sty.foobaz == 'baz'



# Generated at 2022-06-14 08:29:21.972770
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert isinstance(r, Register)
    assert not hasattr(r, "renderfuncs")
    assert not hasattr(r, "is_muted")
    assert not hasattr(r, "rgb_call")
    assert not hasattr(r, "eightbit_call")



# Generated at 2022-06-14 08:29:30.113205
# Unit test for method __new__ of class Style
def test_Style___new__():

    s1 = Style(fg=1, bg=2)
    assert s1 == Style(fg=1, bg=2)
    assert type(s1) == Style
    assert type(s1) == str
    assert s1.rules == (fg(1), bg(2))
    assert str(s1) == "\x1b[38;5;1m\x1b[48;5;2m"



# Generated at 2022-06-14 08:29:34.886180
# Unit test for constructor of class Style
def test_Style():

    from .rendertype import Sgr, RgbFg

    style = Style(RgbFg(1, 5, 10), Sgr(1))

    assert isinstance(style, Style)
    assert hasattr(style, "rules")



# Generated at 2022-06-14 08:29:42.907589
# Unit test for method copy of class Register
def test_Register_copy():
    reg = Register()
    reg.a = Style(value="a")
    reg.b = Style(value="b")

    regcopy = reg.copy()

    assert regcopy is not reg
    assert regcopy.a == "a"
    assert regcopy.b == "b"

    regcopy.a = "A"
    assert reg.a == "a"
    assert regcopy.a == "A"

    reg.b = "B"
    assert reg.b == "B"
    assert regcopy.b == "b"

# Generated at 2022-06-14 08:29:44.787547
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    pass
    # TODO: Write a unit test.


# Generated at 2022-06-14 08:29:56.266148
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .rendertypes import Sgr
    from .rules import Fg, Bg
    from .sty import Sty
    from .modes import Light
    from .register import Register

    sty = Sty()
    Fg = sty.register.Fg

    # The new render type.
    class It(RenderType):
        pass

    # The new renderfunc for 'It'.
    def renderit(*args):
        return "\x1b[?1h\x1b=", args

    sty.register.set_renderfunc(It, renderit)

    # The style rules.
    Fg.orange = Style(Fg(220), Bg(122), It(55, 1, 22))

    # The registers
    rs = sty.register
    fg = sty.register.Fg
    bg = sty.register.Bg


# Generated at 2022-06-14 08:30:16.123976
# Unit test for method unmute of class Register
def test_Register_unmute():
    fg = Register()
    fg.red = Style(Sgr(1), Sgr(38, 5, 1))
    fg.mute()
    fg.unmute()
    assert fg.red == "\x1b[1m\x1b[38;5;1m"


# Generated at 2022-06-14 08:30:28.705454
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .rendertype import RgbBg, RgbFg
    from .renderfunc import ansicolor

    def eightbit_bg_call(x: int) -> str:
        return ansicolor(x, 49, RgbBg)

    def rgb_bg_call(r: int, g: int, b: int) -> str:
        return ansicolor(r, g, b, RgbBg)

    r = Register()
    r.set_eightbit_call(RgbBg)
    r.set_rgb_call(RgbBg)
    r.set_renderfunc(RgbFg, ansicolor)
    r.red = Style(RgbFg(250, 10, 5))
    r.bgred = Style(RgbBg(250, 10, 5))

# Generated at 2022-06-14 08:30:33.299581
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    from . import fg
    from .rendertype import EightyBitFg

    fg.red = Style(EightyBitFg(1))

    assert fg.as_dict() == {"red": "\x1b[38;5;1m"}



# Generated at 2022-06-14 08:30:38.621607
# Unit test for method unmute of class Register
def test_Register_unmute():
    def render_func(value):
        return "bg is muted"

    r = Register()
    r.set_renderfunc(str, render_func)
    r.bg = Style(str("blue"))
    r.mute()
    r.unmute()

    assert str(r.bg) == "bg is muted"

# Generated at 2022-06-14 08:30:45.239563
# Unit test for method copy of class Register
def test_Register_copy():
    a = Register()
    a.a = Style(RgbFg(1, 2, 3))
    b = a.copy()
    assert a is not b
    assert a.a is not b.a
    assert a.a.rules is not b.a.rules
    assert a.a.rules[0] is not b.a.rules[0]
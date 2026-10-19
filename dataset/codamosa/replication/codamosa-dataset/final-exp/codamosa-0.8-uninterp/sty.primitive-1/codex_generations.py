

# Generated at 2022-06-14 08:20:58.623847
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    r1 = Register()

    style_black = Style(RgbFg(0, 0, 0), Sgr(0))
    style_red = Style(RgbFg(255, 0, 0), Sgr(0))
    style_yellow = Style(RgbFg(255, 255, 0), Sgr(0))

    setattr(r1, "black", style_black)
    setattr(r1, "red", style_red)
    setattr(r1, "yellow", style_yellow)

    assert r1(0, 0, 0) == "\x1b[38;2;0;0;0m\x1b[0m"
    assert r1(255, 0, 0) == "\x1b[38;2;255;0;0m\x1b[0m"

    r1

# Generated at 2022-06-14 08:21:07.167215
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import RgbBg

    # Make a register-object with two rgb-render-functions.
    r = Register()

    def rgb_bg_renderfunc(r, g, b):
        return "a"

    def rgb_bg_renderfunc2(r, g, b):
        return "b"

    r.set_renderfunc(RgbBg, rgb_bg_renderfunc)
    r.set_renderfunc(RgbBg, rgb_bg_renderfunc2)

    # Initialize a new style that uses the first render-function.
    r.style = Style(RgbBg(1, 2, 3))
    assert str(r.style) == "a"

    # Change rbg-call to use second rgb-render-function.

# Generated at 2022-06-14 08:21:18.745155
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import RgbFg, RgbBg

    # Setup test objects
    fg = Register()
    fg.red = Style(RgbFg(255, 0, 0))
    fg.black = Style(RgbFg(0, 0, 0))

    bg = Register()
    bg.yellow = Style(RgbBg(255, 255, 0))
    bg.white = Style(RgbBg(255, 255, 255))

    # Unit test
    assert fg.red == "\x1b[38;2;255;0;0m"
    assert bg.yellow == "\x1b[48;2;255;255;0m"

    fg.set_rgb_call(RgbBg)


# Generated at 2022-06-14 08:21:31.689445
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    
    from sty import fg, bg, ef, rs

    # Example call
    fg.set_rgb_call(RgbFg)
    fg(10, 20, 30)

    # Set new render-function
    def custom_rgb(r, g, b):
        r = int(r)
        g = int(g)
        b = int(b)

        return f"R: {r}, G: {g}, B: {b}"

    # Register new render-function
    fg.set_renderfunc(RgbFg, custom_rgb)

    # Use new function in 8bit-call
    fg.set_rgb_call(RgbFg)
    assert fg(10, 20, 30) == "R: 10, G: 20, B: 30"

   

# Generated at 2022-06-14 08:21:43.415185
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import RgbFg
    from .rendertype import Sgr

    # Define funcs
    def rgb_func(r, g, b):
        return f"RgbFg{r}{g}{b}"

    def sgr_func(x):
        return f"Sgr{x}"

    # Create register object
    colour = Register()

    # Add renderfuncs
    colour.set_renderfunc(RgbFg, rgb_func)
    colour.set_renderfunc(Sgr, sgr_func)

    # Add style
    colour.style1 = Style(RgbFg(0, 0, 0), Sgr(1))

    # Test RGB-call
    assert colour.set_rgb_call(RgbFg) == None

# Generated at 2022-06-14 08:21:54.022591
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    """ """
    import sys

    class MockRgbFg(RenderType):
        """ """
        args: Tuple[int, int, int] = (0, 0, 0)

        def __init__(self, r: int, g: int, b: int) -> None:
            """ """
            self.args = (r, g, b)

    class MockRgbBg(RenderType):
        """ """
        args: Tuple[int, int, int] = (0, 0, 0)

        def __init__(self, r: int, g: int, b: int) -> None:
            """ """
            self.args = (r, g, b)


# Generated at 2022-06-14 08:21:59.924460
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    def renderfunc(r: int, g: int, b: int, **kwargs) -> str:
        return f"{r}, {g}, {b}"

    register = Register()
    register.set_renderfunc(renderfunc)
    register.set_rgb_call(renderfunc)



# Generated at 2022-06-14 08:22:10.662163
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # Test if set_rgb_call works with class RgbFg of rendertype.py
    class RgbBg(RenderType):
        ansi_code = 48
        args_template = ";".join(["2"] + ["1"] * 3)

    class RgbFg(RenderType):
        args_template = ";".join(["2"] + ["1"] * 3)

    r = Register()
    r.renderfuncs.update({RgbFg: lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m"})
    r.renderfuncs.update({RgbBg: lambda r, g, b: f"\x1b[48;2;{r};{g};{b}m"})
    r.set_rgb_

# Generated at 2022-06-14 08:22:18.878712
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertype import RgbBg, RgbEf, RgbFg

    my_reg = Register()
    my_reg.set_renderfunc(RgbFg, lambda x,y,z: f"\x1b[38;2;{x};{y};{z}m")
    my_reg.set_rgb_call(RgbBg)
    assert my_reg(10, 20, 30) == "\x1b[48;2;10;20;30m"



# Generated at 2022-06-14 08:22:26.630910
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertype import RgbFg

    r = Register()

    r.black = Style(value="\x1b[30m")
    r.red = r.black
    setattr(r, "blue", r.black)

    assert r.black == r.red
    assert r.black == getattr(r, "blue")

    r.set_rgb_call(RgbFg)
    r.black = Style(RgbFg(0, 0, 0))

    assert r.black == "\x1b[38;2;0;0;0m"

    r.red = Style(RgbFg(255, 0, 0))
    r.blue = Style(RgbFg(0, 0, 255))


# Generated at 2022-06-14 08:22:34.702668
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import RgbBg

    reg = Register()
    reg.set_renderfunc(RgbBg, lambda r, g, b: f"\x1b[48;2;{r};{g};{b}m")

    reg = Register()
    reg.set_rgb_call(RgbBg)

    assert reg(255, 255, 255) == "\x1b[48;2;255;255;255m"

# Generated at 2022-06-14 08:22:44.855185
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    """
    >>> reg = Register()
    >>> reg.set_rgb_call(RgbFg)
    >>> reg.set_eightbit_call(RgbFg)
    >>> reg(10,42,255)
    '\x1b[38;2;10;42;255m'
    >>> reg(42)
    '\x1b[42m'
    >>> reg.set_rgb_call(Sgr)
    >>> reg(10,42,255)
    '\x1b[10;42;255m'
    >>> reg(42)
    '\x1b[42m'
    """
    pass



# Generated at 2022-06-14 08:22:58.731483
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from sty import fg, bg

    fg.defined = fg(100, 200, 10)
    bg.defined = bg(100, 200, 10)

    assert ";2;100;200;10" in str(fg.defined)
    assert ";2;100;200;10" not in str(bg.defined)

    bg.set_rgb_call(bg.RGB)

    assert ";2;100;200;10" not in str(bg.defined)
    assert bg.defined == bg(100, 200, 10)

    assert ";2;100;200;10" in str(bg.defined)
    assert bg.defined == bg(100, 200, 10)

    bg.set_rgb_call(bg.ALPHA24)


# Generated at 2022-06-14 08:23:07.926789
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import RgbFg, RgbBg, Setaf, Setab

    def func(r, g, b):
        return (r, g, b)

    # List of rendertypes that can be used for RGB-calls
    rendertypes_rgb = [RgbFg, RgbBg, Setaf, Setab]

    # Create a new register-object and set all render-funcs to function func.
    reg = Register()
    for rt in rendertypes_rgb:
        reg.set_renderfunc(rt, func)

    # The RGB-call should have been set to rendertype RgbFg
    assert reg.rgb_call == reg.renderfuncs[RgbFg]

    # Change the RGB-call to rendertype RgbBg

# Generated at 2022-06-14 08:23:19.351552
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # Define some test methods
    eightbit_render = lambda x: f"\x1b[38;5;{x}m"
    rgb_render = lambda r, g, b: f"\x1b[{r};{g};{b}m"
    register = Register()

    # Add those methods to the register object
    register.set_renderfunc(RgbFg, rgb_render)
    register.set_renderfunc(EightbitFg, eightbit_render)

    # Test method set_eightbit_call
    register.set_eightbit_call(RgbFg)
    assert isinstance(register.eightbit_call, Callable)
    assert register.eightbit_call(42) == rgb_render(42)

    # Test method set_rgb_call
    register.set_rgb_

# Generated at 2022-06-14 08:23:26.509671
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class RGBAttribute():
        pass

    r = Register()
    r.renderfuncs = {"RgbFg": lambda x, y, z: "RgbFg()"}
    e = Style(RGBAttribute())
    setattr(r, "e", e)

    r.set_rgb_call("RgbFg")

    assert r("e") == "RgbFg()"

# Generated at 2022-06-14 08:23:36.475942
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class AnsiString(str): pass

    class RgbFg:
        def __init__(self):
            self.args = [10, 20, 30]

    class RgbBg:
        def __init__(self):
            self.args = [40, 50, 60]

    def test_render_rgb_fg(r: int, g: int, b: int) -> AnsiString:
        return AnsiString(f"\x1b[38;5;12m")

    def test_render_rgb_bg(r: int, g: int, b: int) -> AnsiString:
        return AnsiString(f"\x1b[48;5;12m")


# Generated at 2022-06-14 08:23:50.230808
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class TestRenderType1(RenderType):
        pass

    class TestRenderType2(RenderType):
        pass

    class TestRegister(Register):

        def __init__(self):
            super().__init__()
            self.test = Style(TestRenderType1(42), TestRenderType2(255))

    register = TestRegister()
    assert hasattr(register, "test")

    def renderfunc1(*args):
        return f"\u001b[{args[0]}m"

    def renderfunc2(*args):
        return f"\u001b[{args[0]}m"

    register.set_rgb_call(TestRenderType1)
    register.set_renderfunc(TestRenderType1, renderfunc1)
    register.set_renderfunc(TestRenderType2, renderfunc2)


# Generated at 2022-06-14 08:23:56.295510
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertypes import RgbBg, RgbFg

    reg = Register()
    reg.set_rgb_call(RgbBg)

    assert reg.rgb_call == RgbBg

    reg.set_rgb_call(RgbFg)

    assert reg.rgb_call == RgbFg

# Generated at 2022-06-14 08:24:05.537309
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class RgbFg(RenderType):
        num_args = 3

    class RgbBg(RenderType):
        num_args = 3

    # Create new register
    r = Register()

    # Define default render functions
    r.set_renderfunc(RgbFg, lambda r, g, b: f"RgbFg{r}-{g}-{b}")
    r.set_renderfunc(RgbBg, lambda r, g, b: f"RgbBg{r}-{g}-{b}")

    # Assign style attributes
    r.red = Style(RgbFg(255, 0, 0))
    r.blue = Style(RgbBg(0, 0, 255))

# Generated at 2022-06-14 08:24:13.970951
# Unit test for method copy of class Register
def test_Register_copy():
    fg = Register()
    fg.red = Style(RgbFg(255, 0, 0))

    fg2 = fg.copy()

    assert fg2.red == fg.red

# Generated at 2022-06-14 08:24:20.102808
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    reg = Register()

    # Testcase: Add renderfunc for with default rendertype and without default rendertype
    reg.set_renderfunc(namedtuple("rendertype", "__doc__")(None), lambda x: x)
    reg.set_renderfunc(namedtuple("rendertype", "__doc__")(None), lambda x: x)


# Generated at 2022-06-14 08:24:31.466358
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    class TestRenderType(RenderType):

        def __init__(self):
            super().__init__()
            self.args = (1, 2)

    renderfuncs: Renderfuncs = {TestRenderType: lambda x, y: f"Test-{x}-{y}"}

    register = Register()
    register.renderfuncs = renderfuncs

    register.set_eightbit_call(TestRenderType)
    assert register.eightbit_call(5, 5) == "Test-5-5"

    register.set_eightbit_call(TestRenderType)
    assert register.eightbit_call(1, 1) == "Test-1-1"


# Unit test _render_rules of class Register

# Generated at 2022-06-14 08:24:37.950707
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    r = Register()

    r.set_eightbit_call(RgbFg)
    assert r.eightbit_call("\x1b[38;2;0;0;0m", 0) == "\x1b[38;2;0;0;0m"

    r.set_eightbit_call(Sgr)
    assert r.eightbit_call("\x1b[0m", 0) == "\x1b[0m"



# Generated at 2022-06-14 08:24:42.351005
# Unit test for method copy of class Register
def test_Register_copy():

    import pytest

    reg = Register()
    reg.fg_red = Style("\x1b[31m")

    reg2 = reg.copy()

    assert reg2.fg_red == "\x1b[31m"

# Generated at 2022-06-14 08:24:55.374041
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class DummySgr(RenderType):
        pass

    # init test object
    reg = Register()
    reg.hello = Style(DummySgr(42))

    expected_hello = Style(DummySgr(42), value="")
    expected_world = Style(DummySgr(42), value="\x1b[42m")

    assert getattr(reg, "hello") == expected_hello

    def dummy_renderfunc(x: int) -> str:
        return f"\x1b[{x}m"

    reg.set_renderfunc(DummySgr, dummy_renderfunc)

    assert getattr(reg, "hello") == expected_world

    # Unset renderfunc again.
    reg.set_renderfunc(DummySgr, lambda x: x)

# Generated at 2022-06-14 08:25:06.391748
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    class Sgr(RenderType):
        """
        SGR (Select Graphic Rendition)

        The SGR rendertype defines the attributes for a standard SGR-code.

        :param args: The attributes for the SGR code.
        """
        args = None

    class RgbFg(RenderType):
        """
        RGB-foreground color

        The RgbFg rendertype defines the attributes for a RGB-foreground color.

        :param r: The red-value.
        :param g: The green-value.
        :param b: The blue-value.
        """
        args = ["r", "g", "b"]


# Generated at 2022-06-14 08:25:10.851608
# Unit test for method __call__ of class Register
def test_Register___call__():

    class MyRegister(Register):
        def __init__(self):
            super().__init__()

    myregister = MyRegister()

    myregister.a = Style(RgbFg(1, 5, 10))

    assert myregister.a == myregister("a")
    assert myregister.a == myregister(1, 5, 10)

# Generated at 2022-06-14 08:25:16.621692
# Unit test for method __new__ of class Style
def test_Style___new__():
    rules = (RgbFg(1, 5, 10), Sgr(1))
    value = ""
    style = Style(*rules, value=value)
    assert style == value
    assert style.rules == rules
    assert isinstance(style, Style)
    assert isinstance(style, str)



# Generated at 2022-06-14 08:25:21.135223
# Unit test for method __new__ of class Style
def test_Style___new__():
    from .rendertype import Sgr
    s = Style(Sgr(1), value="")
    assert (s == "")
    assert (isinstance(s, Style))
    assert (isinstance(s, str))


# Generated at 2022-06-14 08:25:38.291992
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class TestRegister(Register):
        pass

    def dummy(x: int) -> str:
        return str(x)

    r = TestRegister()

    assert "RgbFg" not in r.renderfuncs

# Generated at 2022-06-14 08:25:45.363566
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    class MyRegister(Register):
        def __init__(self):
            super().__init__()
            self.red = "red"
            self.green = "green"
            self.blue = "blue"

    reg = MyRegister()
    nt = reg.as_namedtuple()
    assert nt.red == "red"
    assert nt.green == "green"
    assert nt.blue == "blue"
    assert hasattr(nt, "blue")


# Generated at 2022-06-14 08:25:54.948172
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # Create new register.
    test_reg = Register()

    # Add a renderfunc to the register.
    test_reg.set_renderfunc(RenderType, lambda *args: f"{args[0]}")

    # Set the render-type for RGB-calls.
    test_reg.set_rgb_call(RenderType)

    # Test
    assert test_reg(0) == ""
    assert test_reg(10, 20, 30) == "RenderType"
    assert test_reg("not_existing_name") == ""


# Generated at 2022-06-14 08:26:04.678195
# Unit test for method unmute of class Register
def test_Register_unmute():
    # Code that should be tested
    register = Register()
    register.set_renderfunc(RenderType.eightbit, lambda x: f"\x1b[38;5;{x}m")
    register.set_eightbit_call(RenderType.eightbit)
    register.red = Style(RenderType.eightbit(1))

    register.mute()

    assert register.red == ""
    assert register.red == ""
    assert register.red == ""

    register.unmute()

    assert register.red == "\x1b[38;5;1m"
    assert register.red == "\x1b[38;5;1m"
    assert register.red == "\x1b[38;5;1m"

# Generated at 2022-06-14 08:26:09.811351
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    register = Register()
    register.red = Style()
    register.green = Style()

    d = register.as_dict()

    assert len(d) == 2
    assert d["red"] == ""
    assert d["green"] == ""



# Generated at 2022-06-14 08:26:19.183716
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from .rendertype import RgbBg, Sgr

    # Test for style, string instanciated as a Style-object

    register_object = Register()

    # Construct and set a style-object
    style_object = Style(RgbBg(1, 2, 3), Sgr(1))

    # setting the style-object
    register_object.style_object = style_object

    # Assert that the style_object was set
    assert register_object.style_object == style_object

    # Assert that the register was properly rendered
    assert (
        register_object.style_object == "\x1b[48;2;1;2;3m\x1b[1m"
    )  # type: ignore

    # Test for style, string instanciated as a string (must raise error)

    register_

# Generated at 2022-06-14 08:26:26.511709
# Unit test for method __new__ of class Style
def test_Style___new__():
    style = Style(fg(255), sgr(1))
    assert isinstance(style, str)
    assert isinstance(style, Style)
    assert style.rules == (fg(255), sgr(1))
    assert str(style) == '\x1b[38;5;255m\x1b[1m'


# Generated at 2022-06-14 08:26:33.270245
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertype import RgbBg
    from .eightbit import EightBit

    register = Register()
    register.set_renderfunc(RgbBg, lambda *args: "".join(args))
    register.set_rgb_call(RgbBg)
    assert register(144, 41, 69) == "1444169"



# Generated at 2022-06-14 08:26:35.776147
# Unit test for constructor of class Style
def test_Style():

    from sty import ef

    Style(ef.bold, ef.underline)
    assert True

# Generated at 2022-06-14 08:26:49.405656
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    # The render type and the render func that is used in the test
    class RgbFg(RenderType):
        pass

    def func(r, g, b):
        return f"{r}{g}{b}"

    def test_new_renderfunc():
        # Create a new Register with an old render-func 'func1'
        func1 = lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m"
        r = Register()
        r.set_renderfunc(RgbFg, func1)

        # Create a Style with the old render-func
        style1 = Style(RgbFg(255, 255, 255))

        # Assert that the style is rendered with the old render-func

# Generated at 2022-06-14 08:27:05.987099
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .ansi import fg, bg, ef, rs

    # 8bit calls, fg
    assert fg(39) == "\x1b[39m"
    assert fg(0) == "\x1b[38;5;0m"
    assert fg(1) == "\x1b[38;5;1m"
    assert fg(1, "red") == "\x1b[38;5;1m"

    # 8bit calls, bg
    assert bg(40) == "\x1b[40m"
    assert bg(0) == "\x1b[48;5;0m"
    assert bg(1) == "\x1b[48;5;1m"

# Generated at 2022-06-14 08:27:14.757191
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    class ExampleRegister(Register):
        pass

    e = ExampleRegister()
    e.s1 = Style(value="\x1b[10m\x1b[4m")
    e.s2 = Style(value="\x1b[10m\x1b[4m")

    n = e.as_namedtuple()
    assert isinstance(n, NamedTuple)
    assert isinstance(n.s1, str)
    assert isinstance(n.s2, str)
    assert len(n) == 2

# Generated at 2022-06-14 08:27:22.789514
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .sty import Sty
    from .rendertype import Sgr
    from .colour import RgbFg

    sty = Sty()

    fg = sty.fg
    bg = sty.bg

    assert fg(42, Sgr(1)) == "\x1b[38;5;42m\x1b[1m"
    assert fg(RgbFg(1, 42, 42), Sgr(1)) == "\x1b[38;2;1;42;42m\x1b[1m"

    assert bg(42, Sgr(1)) == "\x1b[48;5;42m\x1b[1m"

# Generated at 2022-06-14 08:27:36.087964
# Unit test for method copy of class Register
def test_Register_copy():

    from sty import Style as S, fg, bg

    register = Register()
    register.set_eightbit_call(S.fg)
    register.set_rgb_call(S.fg)
    register.set_renderfunc(S.fg, lambda *_: "")
    register.__setattr__("red", Style(fg.red))

    copy = register.copy()
    copy.__setattr__("yellow", Style(fg.yellow))
    copy.set_renderfunc(S.fg, lambda *_: "!")

    assert register.renderfuncs[S.fg] != copy.renderfuncs[S.fg]
    assert copy.red == register.red
    assert copy.yellow != register.yellow
    assert copy.red != copy.yellow
    assert copy.renderfuncs[S.fg]("")

# Generated at 2022-06-14 08:27:39.339082
# Unit test for constructor of class Register
def test_Register():
    fg = Register()
    assert fg.is_muted == False
    assert fg.eightbit_call(144) == ''
    assert fg.rgb_call(144, 144, 144) == ''



# Generated at 2022-06-14 08:27:50.797910
# Unit test for constructor of class Style
def test_Style():

    # Test basic
    assert isinstance(Style(), Style)

    # Test single rule
    assert isinstance(Style(RgbFg(10, 20, 30)), Style)

    # Test different rules
    assert isinstance(Style(RgbFg(10, 20, 30), Sgr(1, 5)), Style)

    # Test with value
    assert isinstance(Style(RgbFg(10, 20, 30, value="\x1b[38;2;10;20;30m")), Style)

    # Test wrong type
    try:
        Style(42)
    except ValueError:
        pass
    else:
        raise AssertionError("Style-constructor must raise ValueError if called with wrong parameter.")



# Generated at 2022-06-14 08:27:58.359968
# Unit test for method copy of class Register
def test_Register_copy():
    """
    This method tests the copy method of class Register.
    """
    from .render import sgr
    from .rendertype import Sgr, Bg, Bg256, RgbBg

    r = Register()
    for stylet in (Sgr, Bg, Bg256, RgbBg):
        r.set_renderfunc(stylet, sgr.render)
    r.set_rgb_call(RgbBg)
    r.set_eightbit_call(Bg256)

    r.red = Style(Bg(1))
    r.orange = Style(Bg256(94))
    r.gray = Style(Bg(245))
    r.blue = Style(RgbBg(150, 200, 100))

    r2 = r.copy()

    assert r2.rgb_

# Generated at 2022-06-14 08:28:11.103829
# Unit test for method mute of class Register
def test_Register_mute():
    """Test mute method"""

    import os
    import sys
    import platform

    # Skip test on Windows
    if platform.system().lower() == "windows":
        print("Test skipped.")
        sys.exit()

    # Prepare ANSI escape code if not yet defined
    if not os.environ.get("ANSI_COLORS_DISABLED"):
        os.environ["ANSI_COLORS_DISABLED"] = "1"

    # Prepare
    from sty import Style, fg, bg, ef, rs

    # Store style before mute
    style = fg(1)
    style_old = str(style)

    # Mute
    fg.mute()

    # Store style after mute
    style_new = str(style)

    # Assert
    assert style_old != style_new



# Generated at 2022-06-14 08:28:18.503379
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertypes import Sgr, RgbFg

    reg = Register()

    setattr(reg, "red", Style(RgbFg(1, 0, 0)))
    setattr(reg, "bold", Style(Sgr(1)))

    assert reg("red") == "\x1b[38;2;1;0;0m"
    assert reg("bold") == "\x1b[1m"

# Generated at 2022-06-14 08:28:31.107607
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .rendertype import Sgr

    # Init register
    fg = Register()

    # Add render-functions
    fg.set_renderfunc(Sgr, lambda x: f"\x1b[{x}m")

    # Set a style
    fg.orange = Style(Sgr(1), Sgr(38, 2, 1, 5, 10))

    # Test if the style-attribute of fg-register is a Style
    assert isinstance(fg.orange, Style)

    # Test if the value of fg.orange is a str
    assert isinstance(fg.orange, str)

    # Test if the ANSI-sequence is correctly rendered to a str
    assert str(fg.orange) == "\x1b[1m\x1b[38;2;1;5;10m"

# Unit test

# Generated at 2022-06-14 08:28:43.284198
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    class myRegister(Register):
        def __init__(self):
            super().__init__()
            self.test = Style("test_ansi_style")

    reg = myRegister()

    nt = reg.as_namedtuple()

    assert nt.test == "test_ansi_style"



# Generated at 2022-06-14 08:28:51.727904
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertype import Fg, Bg, Ef, Rs

    reg: Register = Register()

    reg.set_renderfunc(Fg, lambda x: '\x1b[38;5;%dm' % x)
    reg.set_renderfunc(Bg, lambda x: '\x1b[48;5;%dm' % x)
    reg.set_renderfunc(Ef, lambda x: '\x1b[%dm' % x)
    reg.set_renderfunc(Rs, lambda: '\x1b[0m')

    # Test eightbit call with default rendertype Fg.
    assert (reg(42) == '\x1b[38;5;%dm' % 42)

    # Now set rendertype Bg for eightbit call.

# Generated at 2022-06-14 08:28:59.886342
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    from . import Ansi, RgbFg, Sgr

    def rgb_call(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    def sgr_call(code: int) -> str:
        return f"\x1b[{code}m"

    red = RgbFg(255, 0, 0)
    bold = Sgr(1)

    register = Register()
    register.set_renderfunc(RgbFg, rgb_call)
    register.set_renderfunc(Sgr, sgr_call)
    register.red = Style(red, bold)

    assert register.red == "\x1b[38;2;255;0;0m\x1b[1m"



# Generated at 2022-06-14 08:29:09.409998
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    """
    The register class of stylable can have a global call function.
    This is the function that is run when you call the register-object directly.
    At first these functions are automatically set to render 8bit and RGB colors.
    But you can also change them.
    """

    class Rgb(RenderType):
        def __init__(self, r: int, g: int, b: int):
            self.args = [r, g, b]

    class Eightbit(RenderType):
        def __init__(self, color: int):
            self.args = [color]

    class Bg(RenderType):
        def __init__(self, r: int, g: int, b: int):
            self.args = [r, g, b]

    def render_eightbit(color: int) -> str:
        return

# Generated at 2022-06-14 08:29:17.426857
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class CustomRegister(Register):
        pass

    from sty import fg, bg, ef, rs
    from sty.render import RgbFg, RgbBg, Bg, Fg, Default

    r = CustomRegister()
    r.renderfuncs = {
        RgbFg: lambda *args: "RgbFg " + " ".join([str(arg) for arg in args]),
        Fg: lambda *args: "Fg " + " ".join([str(arg) for arg in args]),
        RgbBg: lambda *args: "RgbBg " + " ".join([str(arg) for arg in args]),
        Bg: lambda *args: "Bg " + " ".join([str(arg) for arg in args]),
        Default: lambda *args: "Default",
    }


# Generated at 2022-06-14 08:29:18.245686
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r

# Generated at 2022-06-14 08:29:26.127335
# Unit test for constructor of class Style
def test_Style():
    rt = namedtuple("RenderType", ["args"])

    def get_rt(arg1: int, arg2: int) -> NamedTuple:
        rendertype = rt(args=(arg1, arg2))
        return rendertype

    test_style = Style(get_rt(0, 1), get_rt(2, 3), value=None)

    assert isinstance(test_style, str)
    assert test_style.rules == [get_rt(0, 1), get_rt(2, 3)]

# Generated at 2022-06-14 08:29:31.425549
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    def redfunc(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    fg = Register()
    fg.set_renderfunc(RenderType, lambda x: x)
    fg.set_rgb_call(RenderType)
    assert fg(42, 44, 46) == ""

    fg.set_renderfunc(RenderType, redfunc)
    fg.set_rgb_call(RenderType)
    assert fg(42, 44, 46) == "\x1b[38;2;42;44;46m"



# Generated at 2022-06-14 08:29:43.543240
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    class TestRegister(Register):
        pass

    t = TestRegister()

    assert isinstance(t, Register)
    assert type(t) == TestRegister

    t.test = Style(RgbFg(1,2,3), Sgr(4))

    assert t.test
    assert type(t.test) == Style
    assert str(t.test) == "\x1b[38;2;1;2;3m\x1b[4m"

    # Try to override a Style
    t.test = Style(RgbFg(9,8,7), Sgr(6))

    assert t.test
    assert type(t.test) == Style
    assert str(t.test) == "\x1b[38;2;9;8;7m\x1b[6m"

    #
    #

# Generated at 2022-06-14 08:29:55.627099
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .render import RgbFg, RgbBg

    class MyRegister(Register):
        pass

    rf = MyRegister()

    rf.set_rgb_call(RgbFg)
    rf.set_rgb_call(RgbBg)

    rf.set_renderfunc(RgbFg, lambda r, g, b: "(RgbFg)".join([str(r), str(g), str(b)]))
    rf.set_renderfunc(RgbBg, lambda r, g, b: "(RgbBg)".join([str(r), str(g), str(b)]))

    assert rf(1, 2, 3) == "(RgbFg)".join([str(1), str(2), str(3)])

# Generated at 2022-06-14 08:30:05.450428
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertype import CsiFg, CsiBg
    r = Register()
    r.set_eightbit_call(CsiFg)
    r.fg = Style(CsiFg(10))
    assert r(10) == r.fg


# Generated at 2022-06-14 08:30:18.572747
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    rf = Register()
    rf.set_rgb_call(RenderType())

    # Unit test for method set_eightbit_call of class Register
    def test_Register_set_eightbit_call():
        rf = Register()
        rf.set_eightbit_call(RenderType())

    # Unit test for method set_renderfunc of class Register
    def test_Register_set_renderfunc():
        rf = Register()
        rf.set_renderfunc(RenderType(), lambda x: x)

    # Unit test for method mute of class Register
    def test_Register_mute():
        rf = Register()
        rf.mute()

    # Unit test for method unmute of class Register
    def test_Register_unmute():
        rf = Register()
        rf.unmute()

# Generated at 2022-06-14 08:30:27.155532
# Unit test for method unmute of class Register
def test_Register_unmute():
    rgb = Register()
    rgb.rgb_call = lambda r, g, b: (r, g, b)
    rgb.eightbit_call = lambda x: x

    rgb.red = Style(RgbFg(255, 0, 0))

    assert rgb.red == "\x1b[38;2;255;0;0m"

    rgb.mute()

    assert rgb.red == ""

    rgb.unmute()

    assert rgb.red == "\x1b[38;2;255;0;0m"

# Generated at 2022-06-14 08:30:37.967449
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    # Create a new SGR-Register.
    sgr = Register()

    # Add two render-functions.
    sgr.set_renderfunc(RgbFg, render_rgb_fg)
    sgr.set_renderfunc(Sgr, render_sgr)

    # Create some styled attributes in the SGR-Register.
    sgr.blue = Style(RgbFg(10, 20, 30))
    sgr.bold = Style(Sgr(1))

    # Create some styled attributes that should be ignored for render-type-change.
    sgr.foo = Style(RgbBg(10, 20, 30))

    # 1. Test that set-eightbit-call works with a selection of render-types
    # that are registered in the SGR-Register.

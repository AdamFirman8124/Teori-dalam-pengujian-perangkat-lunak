

# Generated at 2022-06-14 08:20:53.639317
# Unit test for constructor of class Register
def test_Register():
    assert isinstance(Register(), Register)


# Generated at 2022-06-14 08:20:56.137083
# Unit test for constructor of class Register
def test_Register():
    """Unit test for constructor of class Register"""
    a = Register()
    assert a


# Generated at 2022-06-14 08:21:00.275294
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert isinstance(register, Register)
    assert isinstance(register.renderfuncs, dict)
    assert register.is_muted == False
    assert callable(register.eightbit_call)
    assert callable(register.rgb_call)


# Generated at 2022-06-14 08:21:03.041377
# Unit test for constructor of class Register
def test_Register():
    # Create a new Register-Object.
    r = Register()
    assert isinstance(r, Register)



# Generated at 2022-06-14 08:21:13.123533
# Unit test for method __call__ of class Register
def test_Register___call__():

    class NewRenderType(RenderType):
        def __init__(self, n: int, s: str):
            super().__init__(n, s)

    NewRegister = Register()
    NewRegister.set_renderfunc(NewRenderType, lambda n, s: f"{n},{s}")
    NewRegister.set_eightbit_call(NewRenderType)
    NewRegister.set_rgb_call(NewRenderType)

    assert NewRegister(144) == "144,3"
    assert NewRegister(255, 255, 255) == "255,255,255,3"



# Generated at 2022-06-14 08:21:18.008837
# Unit test for constructor of class Register
def test_Register():

    def test_renderfunc(x):
        return x

    r = Register()
    r.set_renderfunc(int, test_renderfunc)
    r.set_eightbit_call(int)

    r.test_style = Style(1)

    assert r.test_style == "1"



# Generated at 2022-06-14 08:21:28.977447
# Unit test for constructor of class Register
def test_Register():
    from .rendertypes import Sgr
    from .builtin_register import fg
    from .rendertypes import Sgr, RgbBg, RgbFg

    custom_fg = Register()

    custom_fg.set_renderfunc(Sgr, lambda *args: "\x1b[1m")
    custom_fg.set_renderfunc(RgbFg, lambda *args: "\x1b[31m")

    custom_fg.red = Style(RgbFg(255, 0, 0), Sgr(1))

    assert custom_fg.red == fg.red



# Generated at 2022-06-14 08:21:34.203325
# Unit test for constructor of class Register
def test_Register():

    class MockRenderType:
        def __init__(self, *args):
            pass

    def func(*args, **kwargs):
        return ""

    reg = Register()
    reg.set_renderfunc(MockRenderType, func)

    assert reg.is_muted == False


# Generated at 2022-06-14 08:21:38.919187
# Unit test for constructor of class Register
def test_Register():
    assert Register().renderfuncs == {}
    assert Register().is_muted == False
    assert Register().eightbit_call(144) == 144
    assert Register().rgb_call(144, 12, 3) == (144, 12, 3)


# Generated at 2022-06-14 08:21:44.011118
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r.renderfuncs == {}
    assert r.is_muted == False
    assert r.eightbit_call.__name__ == '<lambda>'
    assert r.rgb_call.__name__ == '<lambda>'
    

# Generated at 2022-06-14 08:21:51.767293
# Unit test for constructor of class Register
def test_Register():
    assert Register() is not None

# Generated at 2022-06-14 08:22:05.039457
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    assert reg.renderfuncs == {}
    assert reg.is_muted == False

    reg.set_eightbit_call(RenderType)
    reg.set_rgb_call(RenderType)

    assert callable(reg.eightbit_call)
    assert callable(reg.rgb_call)

    try:
        reg.set_eightbit_call(int)
    except Exception:
        pass
    else:
        raise ValueError("Expected Exception")

    try:
        reg.set_rgb_call(int)
    except Exception:
        pass
    else:
        raise ValueError("Expected Exception")

    try:
        reg.set_rgb_call(RenderType)
        reg.set_renderfunc(int, "")
    except Exception:
        pass
   

# Generated at 2022-06-14 08:22:14.817401
# Unit test for method __call__ of class Register

# Generated at 2022-06-14 08:22:21.657926
# Unit test for constructor of class Register
def test_Register():
    """
    Test for the constructor.
    """

    register = Register()
    assert register.is_muted is False
    assert register.__class__.__name__ == "Register"

    # See __call__-test for test of eightbit_call and rgb_call.

    assert isinstance(register.renderfuncs, dict)
    assert register.renderfuncs == {}


# Test __call__ method of class Register

# Generated at 2022-06-14 08:22:23.174990
# Unit test for constructor of class Register
def test_Register():
    g = Register()
    return isinstance(g, Register)


# Generated at 2022-06-14 08:22:34.482306
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .render import NixRender, AnsiRender
    from .types import EightBit, Rgb
    from .rendertype import RenderType, RenderTypes

    ansi_render = AnsiRender()
    nix_render = NixRender()

    # Case 1: Eightbit-call with integer input.
    #         First argument is passed to the render function.
    #         First and second argument are passed to the render function.
    d = {
        EightBit: {
            1: ansi_render,
            2: nix_render
        }
    }
    r = Register()
    r.set_eightbit_call(EightBit)
    for rendertype, renderfunc in d.items():
        for n_args in rendertype.args_fcn:
            r.eightbit_call = lambda *args, **kwargs: args

# Generated at 2022-06-14 08:22:35.808981
# Unit test for constructor of class Register
def test_Register():
    r: Register = Register()
    assert isinstance(r, Register)

# Generated at 2022-06-14 08:22:38.897153
# Unit test for constructor of class Register
def test_Register():
    reg = Register()
    assert not reg.is_muted
    assert reg.eightbit_call
    assert reg.rgb_call

# Generated at 2022-06-14 08:22:39.638051
# Unit test for constructor of class Register
def test_Register():
    _ = Register()

# Generated at 2022-06-14 08:22:47.808820
# Unit test for constructor of class Register
def test_Register():

    from .rendertype.eightbit import Eightbit

    r = Register()
    r.set_renderfunc(Eightbit, lambda fg: f"\x1b[38;5;{fg}m")
    r.set_eightbit_call(Eightbit)
    r.set_rgb_call(Eightbit)
    r.red = Style(Eightbit(1))

    assert r.red == "\x1b[38;5;1m"
    assert r(1) == "\x1b[38;5;1m"
    assert r(255, 0, 0) == "\x1b[38;5;1m"
    assert r.as_dict() == {"red": "\x1b[38;5;1m"}

# Generated at 2022-06-14 08:23:09.498147
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    """
    Test set_eightbit_call method of Register
    """
    from .constants import Sgr
    from .rendertypes import RgbFg, EightbitFg, HsvFg
    from .ansi import RenderEightbit, RenderRgb
    from .color import Color

    def check(color_code, render_type, color):
        color_code.set_eightbit_call(render_type)
        assert color_code(color) == color_code.renderfuncs[render_type](color)

    color_code = Color(render_types=[
        ("color_rgb", RgbFg, RenderRgb), ("color_eightbit", EightbitFg, RenderEightbit),
        ("color_hsv", HsvFg, RenderRgb)
    ])


# Generated at 2022-06-14 08:23:17.995819
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .registers import fg

    fg.mute()
    assert fg.is_muted
    for attr_name in dir(fg):
        val = getattr(fg, attr_name)
        if isinstance(val, Style):
            assert val.value == ""
    fg.unmute()
    assert not fg.is_muted
    for attr_name in dir(fg):
        val = getattr(fg, attr_name)
        if isinstance(val, Style):
            assert val.value != ""


# Generated at 2022-06-14 08:23:30.978415
# Unit test for constructor of class Register
def test_Register():
    from sty.render import NoRender
    from sty.types import NoStyle
    r = Register()

    # Test that all standard attributes are set correctly.
    for attr in [
        "renderfuncs",
        "is_muted",
        "eightbit_call",
        "rgb_call",
    ]:
        assert hasattr(r, attr)
        assert getattr(r, attr)

    # Test that standard renderfuncs are registered.
    assert NoRender in r.renderfuncs

    # Test that eightbit and rgb calls use NoRender by default.
    assert r(42) == NoStyle.value
    assert r(10, 42, 255) == NoStyle.value

    # Test that NoStyle is used in all attributes.

# Generated at 2022-06-14 08:23:35.150493
# Unit test for constructor of class Style
def test_Style():
    str(Style(RgbFg(1, 2, 3), Rgb(10, 20, 30, bg=True)))
    Style(RgbFg(1, 2, 3), Rgb(10, 20, 30, bg=True), value="HALLO")



# Generated at 2022-06-14 08:23:42.918257
# Unit test for method copy of class Register
def test_Register_copy():
    class TestRegister(Register):
        pass

    tr = TestRegister()

    tr.set_eightbit_call(int)
    tr.set_rgb_call(int)

    tr.set_renderfunc(int, lambda x: "test" + str(x))

    t1 = tr.copy()
    t2 = tr.copy()

    assert t1 is not tr
    assert t2 is not tr
    assert t1 is not t2

# Generated at 2022-06-14 08:23:49.073153
# Unit test for method mute of class Register
def test_Register_mute():
    fg = Register()
    fg.red = Style(Sgr(1))

    assert fg.red == Style(Sgr(1))
    assert fg.red == "\x1b[1m"

    fg.mute()

    assert fg.red == Style(Sgr(1))
    assert fg.red == ""

# Generated at 2022-06-14 08:23:55.656443
# Unit test for constructor of class Style
def test_Style():
    a = Style(1, 2, value="1")
    assert hasattr(a, "rules")
    assert a == "1"
    assert a.rules == (1, 2)

    b = Style(3, 4, a, value=a)
    assert b.rules == (3, 4, a)
    assert b == "31"



# Generated at 2022-06-14 08:24:07.494329
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    register = Register()
    register.red = Style(RgbFg(10, 20, 30))
    register.blue = Style(RgbFg(100, 200, 300))
    register.green = Style(RgbFg(1000, 2000, 3000))
    register.yellow = Style(RgbFg(10000, 20000, 30000))

    nt = register.as_namedtuple()

    assert nt.red == '\x1b[38;2;10;20;30m'
    assert nt.blue == '\x1b[38;2;100;200;300m'
    assert nt.green == '\x1b[38;2;1000;2000;3000m'
    assert nt.yellow == '\x1b[38;2;10000;20000;30000m'


# Generated at 2022-06-14 08:24:21.122154
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """
    Test setting a new render-function for a register-object.
    """
    class Sty3(NamedTuple):
        """
        Testcase for method set_renderfunc of class Register.
        """
        # Renderfuncs for testcase
        renderfuncs: Renderfuncs = {}

    class Test:
        """
        Testcase for method set_renderfunc of class Register.
        """

        FF000F = Style(
            RgbFg(255, 0, 15), value="\x1b[38;2;255;0;15m"
        )  # Some given Style for testcase

    sty3 = Sty3(renderfuncs)

    sty3.FF000F = Test.FF000F

    sty3.renderfuncs.update({RgbFg: None})
    sty3.set_renderfunc

# Generated at 2022-06-14 08:24:33.972522
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    from sty import fg
    import json
    ans_dict = fg.as_dict()
    ans_json = json.dumps(ans_dict)

# Generated at 2022-06-14 08:25:10.536416
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from .rendertypes import Rgb

    class CustomRegister(Register):
        pass

    reg = CustomRegister()

    # create new Style objects before adding a new renderfunc
    reg.red = Style(Rgb(1, 2, 3), Rgb(4, 5, 6))
    reg.blue = Style(Rgb(1, 2, 3))

    def render_rgb(r, g, b):
        return f"RENDER({r}, {g}, {b})"

    def render_rgb2(r, g, b):
        return f"RENDER2({r}, {g}, {b})"

    # register a new renderfunc
    reg.set_renderfunc(Rgb, render_rgb)

    # all existing styles should be updated automatically

# Generated at 2022-06-14 08:25:18.873458
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """
    Check that set_renderfunc works as expected.
    """

    def test_renderfunc(x: int, y: int) -> str:
        return f"{x}{y}"

    class TestType(RenderType):
        args = ("x", "y")

    r = Register()
    r.set_renderfunc(TestType, test_renderfunc)
    r.test1 = Style(TestType(42, 43))
    assert r.test1 == "4243"

# Generated at 2022-06-14 08:25:28.941139
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertype import Sgr

    register = Register()
    register.GREEN = Style(Sgr(32))
    register.set_renderfunc(Sgr, lambda *args: f"\x1b[{args[0]}m")

    assert register.GREEN == "\x1b[32m"

    assert register("GREEN") == "\x1b[32m"

    assert register(32) == "\x1b[32m"

    assert register(**{"r": 10, "g": 10, "b": 10}) == "\x1b[32m"


# Generated at 2022-06-14 08:25:36.546370
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class TestRegister(Register):
        pass

    r_test = TestRegister()
    r_test.mute()

    def renderfunc(x: int) -> str:
        return str(x)

    r_test.set_renderfunc(RgbFg, renderfunc)

    r_test.blue = Style(RgbFg(14, 42, 1))
    assert str(r_test.blue) == "14,42,1"
    assert r_test.b

# Generated at 2022-06-14 08:25:47.340965
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class Bar(RenderType):
        pass

    class Foo(RenderType):
        pass

    def bar(x):
        return f"bar {x}"

    def foo(x):
        return f"foo {x}"

    renderfuncs = {Bar: bar, Foo: foo}

    class MyRegister(Register):
        pass

    myreg = MyRegister()
    myreg.renderfuncs = renderfuncs

    assert myreg.renderfuncs[Bar] == bar
    assert myreg.renderfuncs[Foo] == foo

    myreg.set_renderfunc(Bar, foo)
    myreg.set_renderfunc(Foo, bar)

    assert myreg.renderfuncs[Bar] == foo
    assert myreg.renderfuncs[Foo] == bar

# Generated at 2022-06-14 08:25:50.988201
# Unit test for method __new__ of class Style
def test_Style___new__():
    assert isinstance(Style("foo", value="\x1b[42m"), Style)
    assert not isinstance(Style("foo", value="\x1b[42m"), str)

# Generated at 2022-06-14 08:25:55.189333
# Unit test for constructor of class Register
def test_Register():
    """
    Register should be new-style class and has to be callable.
    """
    reg = Register()
    assert isinstance(reg, Register)
    assert callable(reg)


# Unit tests for function Register.__call__()

# Generated at 2022-06-14 08:26:04.802544
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    # Create black rendertype for eightbit-calls.
    class Black(RenderType):
        def render(self, args: Tuple[int]) -> str:
            return "black"

    # Create renderfunc for black rendertype.
    def renderfunc_black(args: Tuple[int]) -> str:
        return "black"

    # Create custom color register
    r = Register()

    # Apply renderfunc to black render type.
    r.set_renderfunc(Black, renderfunc_black)

    # Assign rendertype to register.
    r.set_eightbit_call(Black)

    # Assign named style to register.
    r.black = Style(Black(0))

    # Test that register calls return 'black'
    assert r() == "black"
    assert r(0) == "black"
    assert r

# Generated at 2022-06-14 08:26:17.334631
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class Rgbfg(RenderType):
        def render(self, r, g, b):
            return '\x1b[38;2;{};{};{}m'.format(r, g, b)

    class Sgr(RenderType):
        def render(self, *args):
            return '\x1b[{}m'.format(";".join(map(str, args)))

    r = Register()
    r.renderfuncs.update({Sgr: Sgr.render})
    r.renderfuncs.update({Rgbfg: Rgbfg.render})

    r.test = Style(Rgbfg(1, 2, 3), Sgr(1))

    assert r.test == "\x1b[38;2;1;2;3m\x1b[1m"

# Generated at 2022-06-14 08:26:29.473812
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    class RegisterSub(Register): ...

    reg1 = RegisterSub()

    reg1.yellow = Style("\e[33m", Sgr(1))
    reg1.blue = Style("\e[34m", Sgr(1))
    reg1.carbon = Style("\e[38;2;10;20;15m", Sgr(1))

    assert reg1.as_dict == {'yellow': '\x1b[33m\x1b[1m',
                            'blue': '\x1b[34m\x1b[1m',
                            'carbon': '\x1b[38;2;10;20;15m\x1b[1m'}



# Generated at 2022-06-14 08:27:24.395098
# Unit test for method unmute of class Register
def test_Register_unmute():

    register = Register()
    register.set_eightbit_call(lambda x: x)
    register.set_rgb_call(lambda r, g, b: r + g + b)
    register.a = Style(1, 2, 3)

    assert register.a == "123"

    register.mute()

    assert register.a == ""

    register.unmute()

    assert register.a == "123"

    register.a = Style(1, 4, 7)

    assert register.a == "147"

# Generated at 2022-06-14 08:27:35.143729
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class Test0(RenderType):
        pass

    class Test1(RenderType):
        pass

    class Test2(RenderType):
        pass

    def renderfunc(arg1: str) -> str:
        return f"\x1b[{arg1}m"

    class MyTest(Register):

        def __init__(self):
            super().__init__()
            self.test = Style(Test0("My First Test"), Test1("My Second Test"))

    mytest = MyTest()

    # Make sure, the register has no render function for the class Test0.
    assert mytest.test == "\x1b[My First Testm\x1b[My Second Testm"

    # Now we add a render function for the class Test0.
    mytest.set_renderfunc(Test0, renderfunc)

    #

# Generated at 2022-06-14 08:27:36.461697
# Unit test for method mute of class Register
def test_Register_mute():
    pass
    # assert True

# Generated at 2022-06-14 08:27:45.718197
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    class RgbFg(RenderType):
        def __str__(self):
            return f"\x1b[38;2;{self.r};{self.g};{self.b}m"

    class RgbBg(RenderType):
        def __str__(self):
            return f"\x1b[48;2;{self.r};{self.g};{self.b}m"

    fg = Register()
    fg.set_renderfunc(RgbFg, lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m")
    fg.set_renderfunc(RgbBg, lambda r, g, b: f"\x1b[48;2;{r};{g};{b}m")

    f

# Generated at 2022-06-14 08:27:50.904820
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    import sty
    fg = sty.fg
    blue = fg.blue
    assert isinstance(blue, str)
    assert isinstance(blue, Style)
    assert blue == str(blue)
    assert str(blue) == "\033[38;2;0;0;170m"


# Generated at 2022-06-14 08:27:57.354657
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    class RgbFg(RenderType):
        """
        Foreground RGB color.
        """
        args = ("r", "g", "b")

        def __call__(self, r, g, b):
            return f"\x1b[38;2;{r};{g};{b}m"

    class RgbBg(RenderType):
        """
        Background RGB color.
        """
        args = ("r", "g", "b")

        def __call__(self, r, g, b):
            return f"\x1b[48;2;{r};{g};{b}m"

    def _rgb_to_24(r, g, b):
        return RgbFg(r, g, b)


# Generated at 2022-06-14 08:28:02.253947
# Unit test for constructor of class Style
def test_Style():
    rules = [0, 1]
    s = Style(*rules, value="test")
    print(s)
    print(s.rules == rules)
    print(isinstance(s, str))
    print(isinstance(s, Style))


# Generated at 2022-06-14 08:28:11.407619
# Unit test for method mute of class Register
def test_Register_mute():
    r = Register()
    setattr(r, "red", Style(RgbFg(255, 0, 0)))

    assert not r.is_muted
    assert str(r.red) == "\x1b[38;2;255;0;0m"

    r.mute()

    assert r.is_muted
    assert str(r.red) == ""

    r.unmute()

    assert not r.is_muted
    assert str(r.red) == "\x1b[38;2;255;0;0m"



# Generated at 2022-06-14 08:28:25.249978
# Unit test for method mute of class Register
def test_Register_mute():
    import sty
    from .rendertype import Sgr

    # Create a new custom register
    my_register = Register()

    # Define some colors for this register
    my_register.blue = Style(Sgr(34), "blue")
    my_register.red = Style(Sgr(31), "red")
    my_register.green = Style(Sgr(32), "green")

    # Define a renderfunction for 8bit colors
    def render_func_8bit(code: int) -> str:
        return Sgr(30 + code).render()

    # Define a renderfunction for 24bit colors
    # TODO: Make 24bit support more flexible to account for different 24bit standards.

# Generated at 2022-06-14 08:28:34.645465
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    from .rendertype import Sgr, RgbBg

    class TestRegister(Register):
        pass

    # Create new register object
    test_reg = TestRegister()

    # Set renderfunc
    test_reg.set_renderfunc(RgbBg, lambda *args: f"{args[0]}, {args[1]}, {args[2]}")
    test_reg.set_renderfunc(Sgr, lambda x: f"{x}")

    # Define some styles
    test_reg.style1 = Style(Sgr(1))
    test_reg.style2 = Style(Sgr(3), Sgr(4))
    test_reg.style3 = Style(RgbBg(10, 11, 12))

    # Export to dict
    test_dict = test_reg.as_dict()

    # Ass

# Generated at 2022-06-14 08:29:47.156022
# Unit test for method __call__ of class Register
def test_Register___call__():
    from . import fg, bg, ef, rs

    # Call with 1 parameter: fg(42)
    assert fg.eightbit_call(0) == "\x1b[38;5;0m"
    assert fg.rgb_call(1, 2, 3) == "\x1b[38;2;1;2;3m"
    assert fg(0) == "\x1b[38;5;0m"
    assert fg(1, 2, 3) == "\x1b[38;2;1;2;3m"
    assert fg("red") == "\x1b[31m"

    # Call with 3 parameters: fg(142, 255, 0)
    assert bg.eightbit_call(0) == "\x1b[48;5;0m"
   

# Generated at 2022-06-14 08:29:58.206238
# Unit test for method __new__ of class Style
def test_Style___new__():

    class MockRenderer(RenderType):

        args: Tuple[int]

        def __init__(self, *args):
            self.args = args

        def __repr__(self):
            return f"MockRenderer({self.args})".replace(",)", ")")

    def render_mock_renderer(self, *args):
        return f"M({self.args})"

    fg = Register()
    fg.set_renderfunc(MockRenderer, render_mock_renderer)

    fg.orange = Style(MockRenderer(1))
    fg.red = Style(MockRenderer(2))

    assert str(fg.orange) == "M((1,))"
    assert str(fg.red) == "M((2,))"



# Generated at 2022-06-14 08:30:10.877143
# Unit test for method unmute of class Register
def test_Register_unmute():
    from sty import RenderType, SGR, SGRParam

    r = Register()

    # the render function for SGR(SGRParam.SGR_RESET)
    r.set_renderfunc(SGR, lambda _: "[R]")

    # set new style attributes
    r.red = Style(SGR(SGRParam.SGR_FG_RED))
    r.blue = Style(SGR(SGRParam.SGR_FG_BLUE))
    r.green = Style(SGR(SGRParam.SGR_FG_GREEN))

    # because mute is called in the constructor, we have to remove the
    # empty values
    for k, v in r.__dict__.items():
        if not isinstance(v, str):
            delattr(r, k)

    r.mute()

    assert r

# Generated at 2022-06-14 08:30:12.697323
# Unit test for constructor of class Style
def test_Style():
    s = Style()
    assert isinstance(s, Style)


# Generated at 2022-06-14 08:30:20.083375
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    r = Register()
    setattr(r, "name1", Style("value1"))
    setattr(r, "name2", Style("value2"))
    setattr(r, "_name3", Style("value3"))

    d = r.as_dict()
    assert d == {"name1": "value1", "name2": "value2"}


# Generated at 2022-06-14 08:30:21.298214
# Unit test for constructor of class Register
def test_Register():
    r = Register()


# Generated at 2022-06-14 08:30:29.138293
# Unit test for method copy of class Register
def test_Register_copy():

    s = Register()
    s.rules = Renderfuncs()

    s.reset = Style(RenderType.Sgr0)
    s.black = Style(RenderType.Sgr30)

    s2 = s.copy()

    assert s.reset == s2.reset
    assert s.black == s2.black

    s.reset = Style(RenderType.Sgr1)

    assert s.reset != s2.reset

# Generated at 2022-06-14 08:30:38.686045
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import RgbBg, RgbFg

    class NewRegister(Register):
        pass

    fg = NewRegister()
    fg.red = Style(RgbFg(255, 0, 0))
    fg.green = Style(RgbFg(0, 255, 0))
    fg.blue = Style(RgbFg(0, 0, 255))

    fg.set_rgb_call(RgbFg)
    assert fg(0, 0, 0) == fg.black
    assert fg(255, 0, 0) == fg.red
    assert fg(0, 255, 0) == fg.green
    assert fg(0, 0, 255) == fg.blue



# Generated at 2022-06-14 08:30:50.427349
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    def func1(*args):
        return "Func1"

    def func2(*args):
        return "Func2"

    class A(RenderType):
        pass

    class B(RenderType):
        pass

    class X(RenderType):
        pass

    register = Register()

    register.set_renderfunc(A, func1)
    assert len(register.renderfuncs) == 1
    assert register.renderfuncs[A] == func1

    # Test if renderfunc is replaced.
    register.set_renderfunc(A, func2)
    assert len(register.renderfuncs) == 1
    assert register.renderfuncs[A] == func2

    # Add another renderfunc.
    register.set_renderfunc(B, func1)
    assert len(register.renderfuncs) == 2
   
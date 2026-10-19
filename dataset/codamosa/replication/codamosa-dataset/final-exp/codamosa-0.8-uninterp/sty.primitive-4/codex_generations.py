

# Generated at 2022-06-14 08:20:54.853937
# Unit test for constructor of class Register
def test_Register():
    r = Register()

# Generated at 2022-06-14 08:20:58.768308
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()
    r.red = Style(value="\\x1b[31m")

    assert r.red == r("red")
    assert r.red == r(1)



# Generated at 2022-06-14 08:21:01.346810
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r.is_muted == False
    assert r.renderfuncs == {}



# Generated at 2022-06-14 08:21:13.069915
# Unit test for method __call__ of class Register
def test_Register___call__():

    class MyRegister(Register):
        pass

    myregister = MyRegister()
    myregister.set_rgb_call(RgbBg)
    myregister.set_eightbit_call(EightbitBg)

    myregister.red = Style(RgbBg(255, 0, 0))

    # Test rgbcall.
    assert myregister(255, 0, 0) == "\x1b[48;2;255;0;0m"

    # Test eightbit-call.
    assert myregister(42) == "\x1b[48;5;42m"

    # Test attribute call.
    assert myregister("red") == "\x1b[48;2;255;0;0m"



# Generated at 2022-06-14 08:21:14.853835
# Unit test for constructor of class Register
def test_Register():
    reg = Register()
    assert isinstance(reg, Register)

# Generated at 2022-06-14 08:21:23.210068
# Unit test for method __call__ of class Register
def test_Register___call__():
    class MockRegister(Register):

        def __init__(self, items: List[str]):
            super().__init__()
            self.items = items

        def __setattr__(self, name, value):
            if name == "items":
                return super().__setattr__(name, value)
            else:
                self.items.append(name)

        def __getattr__(self, name):
            if name in self.items:
                return name
            else:
                raise AttributeError

    mr = MockRegister([])
    assert len(mr.items) == 0

    mr(42)
    assert len(mr.items) == 1
    assert mr.items[0] == "42"

    mr(42)
    assert len(mr.items) == 2

# Generated at 2022-06-14 08:21:35.505664
# Unit test for method __call__ of class Register
def test_Register___call__():

    class Foo(RenderType):
        pass

    class Bar(RenderType):
        pass

    class TestRegister(Register):
        pass

    r: TestRegister = TestRegister()
    r.set_renderfunc(Foo, lambda x: "Foo{}".format(x))
    r.set_renderfunc(Bar, lambda x, y, z: "Bar{}-{}-{}".format(x, y, z))
    r.set_eightbit_call(Foo)
    r.set_rgb_call(Bar)

    assert r(42) == "Foo42"
    assert r(10, 10, 10) == "Bar10-10-10"

    # Test setattr()
    r.test = Style(Foo(42), Bar(10, 11, 12))

# Generated at 2022-06-14 08:21:39.110222
# Unit test for constructor of class Register
def test_Register():
    # TODO: Unit test for constructor of class Register
    pass

from .rendertype import RgbBg, RgbFg, Reset, Sgr

from . import ANSIColors

# Generated at 2022-06-14 08:21:41.524045
# Unit test for constructor of class Register
def test_Register():
    """
    Test register class constructor.
    """

    reg = Register()
    assert reg is not None

# Generated at 2022-06-14 08:21:50.003078
# Unit test for method __call__ of class Register
def test_Register___call__():

    r: Register = Register()
    r.foo = Style(value="foo1")
    r.bar = Style(value="bar1")
    r.bla = Style(value="bla1")

    assert r(10) == ""
    assert r(255) == ""
    assert r(42, 255, 255) == ""
    assert r("foo") == "foo1"
    assert r("bar") == "bar1"
    assert r("bla") == "bla1"

# Generated at 2022-06-14 08:21:59.995251
# Unit test for method __call__ of class Register
def test_Register___call__():

    r: Register = Register()
    r.test_style = Style(RgbBg(1, 5, 10))

    assert str(r("test_style")) == str("\x1b[48;2;1;5;10m")
    assert str(r(42)) == ""
    assert str(r(1, 5, 10)) == ""

# Generated at 2022-06-14 08:22:10.432698
# Unit test for method __call__ of class Register
def test_Register___call__():
    from . import fg

    fg.blue = Style(RgbFg(0, 0, 255))
    assert fg(0, 0, 255) == "\x1b[38;2;0;0;255m"
    assert fg(0, 0, 256) == ""
    assert fg("blue") == "\x1b[38;2;0;0;255m"
    assert fg("red") == ""
    assert fg.blue == "\x1b[38;2;0;0;255m"
    assert fg(0) == ""

    fg.set_eightbit_call(RgbFg)
    assert fg(0) == "\x1b[38;2;0;0;0m"



# Generated at 2022-06-14 08:22:16.178852
# Unit test for method __call__ of class Register
def test_Register___call__():
    """
    This unit test checks wether the fg and bg classes behave correctly when
    they are called.
    """

    # Create new register object.
    class Register2(Register):
        pass

    # Define ANSI-functions for this register object.
    def eight_bit(colorcode: int) -> str:
        return f"\x1b[{colorcode}m"

    Register2.set_eightbit_call(Rgb)
    Register2.set_renderfunc(Rgb, eight_bit)

    # Define attributes for new register object.
    setattr(Register2, "red", Style(Rgb(255, 0, 0)))
    Register2.red: Style

    # Check if register object can be called with 8bit-call

# Generated at 2022-06-14 08:22:19.332382
# Unit test for constructor of class Register
def test_Register():
    r1 = Register()
    assert not hasattr(r1, "hello")
    r1.hello = "world"
    assert hasattr(r1, "hello")

# Generated at 2022-06-14 08:22:27.116538
# Unit test for constructor of class Register
def test_Register():
    """
    Tests for the constructor of class Register
    """
    # Test 1: check type of attribute 'renderfuncs'
    r = Register()
    assert isinstance(r.renderfuncs, dict)

    # Test 2: check type of attribute 'is_muted'
    assert isinstance(r.is_muted, bool)

    # Test 3: check type of attribute 'eightbit_call'
    assert isinstance(r.eightbit_call, Callable)

    # Test 4: check type of attribute 'rgb_call'
    assert isinstance(r.rgb_call, Callable)


# Test for method __setattr__ of class Register

# Generated at 2022-06-14 08:22:36.986042
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .rendertype import RgbFg
    from .rendertype import Sgr

    r = Register()
    r.red = Style(RgbFg(255, 0, 0), Sgr(1))
    r.blue = Style(RgbFg(0, 0, 255), Sgr(1), value="\x1b[38;2;0;0;255m\x1b[1m")
    r.green = Style(RgbFg(0, 255, 0), Sgr(1))

    assert(r("red") == "\x1b[38;2;255;0;0m\x1b[1m")
    assert(r("blue") == "\x1b[38;2;0;0;255m\x1b[1m")

# Generated at 2022-06-14 08:22:42.755510
# Unit test for constructor of class Register
def test_Register():

    test_register = Register()

    assert test_register.renderfuncs == {}
    assert test_register.is_muted == False

# Generated at 2022-06-14 08:22:44.454782
# Unit test for constructor of class Register
def test_Register():
    reg = Register()
    assert isinstance(reg, Register)


# Generated at 2022-06-14 08:22:58.436304
# Unit test for method __call__ of class Register
def test_Register___call__():

    # Check if register can be called as a function
    # with an 8bit color code.
    renderfuncs = {"eightbit": lambda x: str(x)}
    test_reg = Register()
    test_reg.set_eightbit_call(RenderType.EightBit)
    test_reg.set_renderfunc(RenderType.EightBit, renderfuncs["eightbit"])

    assert test_reg(42) == "42"
    assert test_reg("42") == "42"
    # assert test_reg(42, 10)  # Should error

    # Check if register can be called as a function
    # with an rgb color code.
    renderfuncs = {"rgb": lambda r,g,b: str(r)+";"+str(g)+";"+str(b)}
    test_reg = Register()
    test

# Generated at 2022-06-14 08:23:01.769777
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()
    r.red = Style(RgbFg(255, 0, 0))
    assert r("red") == '\x1b[38;2;255;0;0m'

# Generated at 2022-06-14 08:23:08.688972
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r


# Generated at 2022-06-14 08:23:14.877904
# Unit test for method __call__ of class Register
def test_Register___call__():

    import sty

    assert sty.fg(144) == "\x1b[38;5;144m"
    assert sty.bg(42,42,42) == "\x1b[48;2;42;42;42m"
    assert sty.fg('orange') == "\x1b[38;5;208m"


# Generated at 2022-06-14 08:23:22.488029
# Unit test for method __call__ of class Register
def test_Register___call__():

    SGR = RenderType("SGR")

    class SgrFg(SGR):
        pass

    class SgrBg(SGR):
        pass

    def sgr_fg(x: int) -> str:
        return f"\x1b[38;5;{x}m"

    def sgr_bg(x: int) -> str:
        return f"\x1b[48;5;{x}m"

    # Create test-register
    test_register = Register()
    test_register.set_renderfunc(SgrFg, sgr_fg)
    test_register.set_renderfunc(SgrBg, sgr_bg)
    test_register.set_eightbit_call(SgrFg)
    test_register.set_rgb_call(SgrBg)

# Generated at 2022-06-14 08:23:33.189275
# Unit test for method __call__ of class Register
def test_Register___call__():
    class TestRegister(Register):
        def __init__(self):
            super().__init__()

        def test_func(self, val: int) -> str:
            return str(val)

        def test_func2(self, val: int) -> str:
            return str(val + 1)

    reg = TestRegister()
    reg.set_eightbit_call(int)
    reg.set_rgb_call(int)
    reg.test_attr = "Test"

    assert reg(3) == "3"
    assert reg(3, 4, 5) == "3"
    assert reg("test_attr") == "Test"
    assert reg() == ""



# Generated at 2022-06-14 08:23:42.305440
# Unit test for constructor of class Register
def test_Register():
    """
    We can define our own registers with the Register class.
    """
    def my_renderfunc(code: int) -> str:
        return f"\x1b[{code};0m"

    # Create a Register object
    my_register = Register()

    # Add a renderfunction for 8bit-colors
    my_register.set_renderfunc(EightBit, my_renderfunc)

    # Define a 8bit color by calling the Register object with an 8bit code.
    my_register(144) == "\x1b[144;0m"

# Generated at 2022-06-14 08:23:47.941547
# Unit test for constructor of class Register
def test_Register():
    # Test correct init of class
    r = Register()
    assert r.renderfuncs == {}
    assert r.is_muted == False
    assert r.eightbit_call == r.eightbit_call
    assert r.rgb_call == r.rgb_call


# Generated at 2022-06-14 08:23:51.312228
# Unit test for constructor of class Register
def test_Register():
    """
    Test if the Register class creates a new instance of the registe class.
    """
    r = Register()
    assert isinstance(r, Register)

# Generated at 2022-06-14 08:23:52.857873
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert isinstance(r, Register)

# Generated at 2022-06-14 08:23:54.114574
# Unit test for constructor of class Register
def test_Register():
    reg = Register()
    assert True

# Generated at 2022-06-14 08:23:55.829945
# Unit test for constructor of class Register
def test_Register():
    reg = Register()
    assert reg is not None
    assert isinstance(reg, Register)

# Generated at 2022-06-14 08:24:10.106986
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    from .ansi import Ansi
    from .rendertype import Rgb

    register = Register()
    register.set_eightbit_call(Ansi)
    register.set_rgb_call(Rgb)
    register.red = "red"
    register.blue = Style(Ansi(4), Rgb(0,0,1))

    d = register.as_dict()
    assert sorted(d.keys()) == sorted(["red", "blue"])
    assert d["red"] == "red"
    assert d["blue"] == "\x1b[4m\x1b[38;2;0;0;1m"

    # Make sure we got a _deepcopy_.
    d["red"] = "orange"
    assert register.red == "red"



# Generated at 2022-06-14 08:24:16.347219
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    r = Register()
    r.red = Style(r.rgb_call, "red")
    r.blue = Style(r.rgb_call, "blue")
    r.purple = Style(r.rgb_call, "purple")
    assert isinstance(r.as_namedtuple(), namedtuple)


# Generated at 2022-06-14 08:24:24.504315
# Unit test for method __call__ of class Register
def test_Register___call__():

    # Create new Register instance
    new_reg = Register()

    # Define styles
    setattr(new_reg, "red", Style(RgbFg(255, 0, 0)))

    # Change default renderfuncs
    new_reg.set_eightbit_call(RgbFg)

    # Define a dummy renderfunction
    def dummy_render(x: int, y: int, *args):
        return str(x)

    new_reg.set_renderfunc(RgbFg, dummy_render)

    # Assertions
    assert new_reg(255, 0, 0) == "255"
    assert new_reg(255, 0, 0) == new_reg.red
    assert new_reg("red") == new_reg.red



# Generated at 2022-06-14 08:24:30.304191
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    # Create new Register.
    class Foo(Register):
        bar = Style()

    f = Foo()

    assert f.as_dict() == {"bar": ""}

    f.bar = Style(Sgr(1))

    assert f.as_dict() == {"bar": "\x1b[1m"}



# Generated at 2022-06-14 08:24:37.237111
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class A(RenderType):
        pass

    class B(RenderType):
        pass

    def f1(*args):
        return "A"

    def f2(*args):
        return "B"

    r = Register()
    r.set_renderfunc(A, f1)
    r.set_renderfunc(B, f2)

    assert r.renderfuncs[A] == f1
    assert r.renderfuncs[B] == f2

# Generated at 2022-06-14 08:24:48.277394
# Unit test for method mute of class Register
def test_Register_mute():

    from .const import fg, RgbFg, Sgr

    fg.yellow = Style(RgbFg(0, 0, 0), Sgr(1), value="\x1b[38;2;0;0;0m\x1b[1m")
    assert fg.yellow == "\x1b[38;2;0;0;0m\x1b[1m"
    fg.mute()
    assert fg.yellow == ""
    fg.unmute()
    assert fg.yellow == "\x1b[38;2;0;0;0m\x1b[1m"



# Generated at 2022-06-14 08:24:57.870535
# Unit test for method __call__ of class Register
def test_Register___call__():
    """
    Unit test for method __call__ of class Register
    """
    from .rendertype import RgbFg, RgbBg, Ef, Rs
    from .func import render_rgb_fg, render_rgb_bg, render_ef, render_rs

    r = Register()
    r.set_renderfunc(RgbFg, render_rgb_fg)
    r.set_renderfunc(RgbBg, render_rgb_bg)
    r.set_renderfunc(Ef, render_ef)
    r.set_renderfunc(Rs, render_rs)
    r.set_eightbit_call(RgbFg)
    r.set_rgb_call(RgbFg)

    # Check that calling register with one integer returns correct string

# Generated at 2022-06-14 08:25:02.268070
# Unit test for constructor of class Style
def test_Style():
    style = Style(RgbBg(1, 5, 10), Sgr(1))
    assert style == "\x1b[48;2;1;5;10m\x1b[1m"
    assert style.rules == (RgbBg(1, 5, 10), Sgr(1))
    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert not isinstance(style, RenderType)



# Generated at 2022-06-14 08:25:05.625641
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    from sty import fg

    fg.red = "bla"
    fg.green = "blub"

    assert fg.as_dict() == {'red': 'bla', 'green': 'blub'}


# Generated at 2022-06-14 08:25:16.540729
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .rendertype import RgbFg, RgbBg, RgbFg256, RgbBg256, Sgr, Reset

    # Create simple Register object.
    reg = Register()

    # Add render functions.
    reg.set_renderfunc(RgbFg, lambda r, g, b: "RGB-FG")
    reg.set_renderfunc(RgbBg, lambda r, g, b: "RGB-BG")

    # Mute Register.
    reg.mute()

    # Create some styles.
    reg.RGB_FG = Style(RgbFg(42, 42, 42))
    reg.RGB_BG = Style(RgbBg(42, 42, 42))

    # Test if styles where correctly muted.
    assert reg.RGB_FG == ""
    assert reg.RGB_BG == ""



# Generated at 2022-06-14 08:25:35.266881
# Unit test for constructor of class Style
def test_Style():
    fg_orange = Style(RgbFg(255, 165, 0))
    str(fg_orange)  # '\x1b[38;2;255;165;0m'



# Generated at 2022-06-14 08:25:40.816835
# Unit test for method __call__ of class Register
def test_Register___call__():
    register = Register()
    register.red = Style("\x1b[91m")
    register.set_rgb_call(RgbFg)

    assert register("red") == "\x1b[91m"
    assert register(1, 2, 3) == "\x1b[38;2;1;2;3m"

# Generated at 2022-06-14 08:25:48.476634
# Unit test for method mute of class Register
def test_Register_mute():

    from sty import fg, bg, ef
    fg.red = Style(RgbFg(255, 0, 0))
    bg.white = Style(RgbBg(255, 255, 255))
    ef.bold = Style(Sgr(1))

    # Do mute
    fg.mute()
    bg.mute()
    ef.mute()

    # Assert that registers are empty (but not None)
    for attr in dir(fg):
        if not attr.startswith("_"):
            assert getattr(fg, attr) == ""

    for attr in dir(bg):
        if not attr.startswith("_"):
            assert getattr(bg, attr) == ""


# Generated at 2022-06-14 08:25:53.400422
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    # Check that attributes only point to None
    for attr in dir(reg):
        val = getattr(reg, attr)
        if not isinstance(val, (int, list, dict, tuple, set)):
            assert val is None



# Generated at 2022-06-14 08:26:03.187736
# Unit test for method mute of class Register
def test_Register_mute():
    # test case 1
    # init register and styles
    class _TestRegister(Register):
        def __init__(self):
            super().__init__()
            self.f1 = Style(Sgr(1))
            self.f2 = Style(Sgr(1), Sgr(4))
            self.f3 = Style(Sgr(2), Sgr(4), Sgr(7))

    # init test object
    r = _TestRegister()

    # check register before mute
    assert isinstance(r.f1, Style)
    assert isinstance(r.f2, Style)
    assert isinstance(r.f3, Style)
    assert r.f1.value == "\x1b[1m"
    assert r.f2.value == "\x1b[1m\x1b[4m"


# Generated at 2022-06-14 08:26:08.105735
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .StyleRegister import fg

    fg.unmute()

    assert fg.is_muted == False

    assert fg.grey2 == '\x1b[38;5;235m'


# Generated at 2022-06-14 08:26:13.635379
# Unit test for constructor of class Style
def test_Style():

    for case in [
        Style(),
        Style(""),
        Style("a"),
        Style("b"),
        Style("a", "b"),
        Style("a", "b", "c"),
    ]:
        assert isinstance(case, str)
        assert isinstance(case, Style)

# Generated at 2022-06-14 08:26:19.177391
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    class MyRegister(Register):
        pass

    r = MyRegister()
    r.a = Style(RenderType("sup"), RenderType("i"), value="sup i")
    r.b = Style(RenderType("supi"), RenderType("supi"), value="supi supi")

    result = r.as_dict()

    assert result == {"a": "sup i", "b": "supi supi"}



# Generated at 2022-06-14 08:26:32.011871
# Unit test for method copy of class Register
def test_Register_copy():
    """
    this is a unit test for the method 'copy' of the class Register.
    """
    from .stypes import EightBit, EffectType, RgbFg, RgbBg, Sgr
    from .registers import fg

    # test copying functionality of fg-register
    # first create a copy of the fg-register and make it mute
    fg_copy = fg.copy()
    fg_copy.mute()

    # check that both fg and fg_copy are mute
    assert fg.is_muted is True
    assert fg_copy.is_muted is True

    # change the color red in fg-register and check if fg_copy remains unchanged
    fg.red = Style(RgbFg(255, 255, 0), Sgr(1))
    assert fg

# Generated at 2022-06-14 08:26:45.395358
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # This is our mock object that we want to register.
    class Dummy(RenderType):
        pass

    # We define this for convenience.
    dummy = Dummy

    # If we want to use Dummy as our rendertype for foreground calls we
    # do the following.
    fg = Register()
    fg.set_renderfunc(Dummy, lambda: "DummyRenderfunc")
    fg.set_rgb_call(Dummy)
    fg.red = Style(dummy(100, 50, 42))

    # Now we can call the register object with rgb values.
    assert fg(100, 50, 42) == "DummyRenderfunc"
    # Or we can just access the attribute "red":
    assert fg.red == "DummyRenderfunc"
    # We can also access the attribute "red" by

# Generated at 2022-06-14 08:27:06.023327
# Unit test for method __new__ of class Style
def test_Style___new__():
    from .rendertype import Sgr, SgrFg
    Style(Sgr(1))
    Style(SgrFg(5))
    Style(Sgr(1), SgrFg(5))
    Style(Sgr(1), Sgr(5))
    Style(Sgr(1), Style(Sgr(5)))
    Style(Sgr(1), Style(SgrFg(5), Sgr(6)))

# Generated at 2022-06-14 08:27:09.012140
# Unit test for method mute of class Register
def test_Register_mute():

    Register_obj = Register()
    Register_obj.fg = Style(RgbFg(1, 10, 100))

    Register_obj.mute()

    assert Register_obj.fg == ""


# Generated at 2022-06-14 08:27:20.096787
# Unit test for method __call__ of class Register
def test_Register___call__():

    class TestRendertype1(RenderType):
        def render(self, x: int) -> str:
            return f"{x}"

    TestRendertype2 = RenderType.as_func(lambda x: f"-{x}")

    class TestRegister(Register):
        def __init__(self):
            super().__init__()
            self.red = Style(TestRendertype1(13))
            self.green = Style(TestRendertype1(42))
            self.blue = Style(TestRendertype1(99))

    tr = TestRegister()

    tr.set_eightbit_call(TestRendertype1)
    assert tr(13) == "13"
    assert tr(42) == "42"
    assert tr(99) == "99"
    assert tr(13, 42, 99) == "99"

    tr

# Generated at 2022-06-14 08:27:21.462192
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """
    Test the method set_renderfunc of class Register.
    """
    assert True

# Generated at 2022-06-14 08:27:34.965454
# Unit test for constructor of class Style
def test_Style():
    """Unit test for constructor of class Style"""
    from .rendertype import RgbBg, RgbFg, Sgr

    style = Style(RgbFg(1, 2, 3), RgbBg(4, 5, 6))
    result = (1, 2, 3, 4, 5, 6)
    assert result == tuple(style.rules)

    style = Style(RgbFg(1, 2, 3), RgbBg(4, 5, 6), Sgr(1))
    result = (1, 2, 3, 4, 5, 6, 1)
    assert result == tuple(style.rules)

    from .sty import Style as S

    S.set_renderfunc(RgbFg, lambda r, g, b: (r, g, b))

# Generated at 2022-06-14 08:27:44.490468
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    """
    This is a unit test for method as_dict of class Register.
    """
    # Import is done here, so we can test the method without the other modules present.
    from .rendertype import RgbFg, Sgr
    r = Register()
    r.red = Style(RgbFg(10, 42, 255))
    r.blue = Style(RgbFg(10, 42, 255), Sgr(1))
    r.green = Style()

    d = r.as_dict()

    assert d["red"] == "\x1b[38;2;10;42;255m"
    assert d["blue"] == "\x1b[38;2;10;42;255m\x1b[1m"
    assert d["green"] == ""

# Generated at 2022-06-14 08:27:55.048841
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    import pytest

    # Register and two rendertypes
    r = Register()
    x = namedtuple("X", "args")
    y = namedtuple("Y", "args")

    # Create renderfunc-dict
    r.renderfuncs.update({
        x: lambda x: "x({})".format(x),
        y: lambda x: "y({})".format(x),
    })

    # Set renderfunc for rgb_call
    r.set_rgb_call(x)

    # Check
    assert r.rgb_call(42) == "x(42)"
    assert r(42) == ""
    assert r(10, 42, 255) == "x(10)"

    # Change renderfunc for rgb_call
    r.set_rgb_call(y)

    # Check
    assert r

# Generated at 2022-06-14 08:28:07.560322
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from .rendertype import Sgr

    # class Style(str):

    #     def __new__(cls, *rules: StylingRule, value: str = "") -> "Style":
    #         new_cls = str.__new__(cls, value)  # type: ignore
    #         setattr(new_cls, "rules", rules)
    #         return new_cls

    class R:
        pass

    r = R()

    r.style = Style(Sgr(1))

    assert isinstance(r.style, Style)

    assert isinstance(r.style, str)

    assert str(r.style) == "\x1b[1m"

    assert r.style.rules == (Sgr(1),)

# Generated at 2022-06-14 08:28:13.762278
# Unit test for method mute of class Register
def test_Register_mute():
    # Create test-register
    r = Register()

    # Set up normal style-attributes and render-functions
    r.set_renderfunc(int, lambda x: f"{x}")
    r.test1 = Style(1)
    r.test2 = Style(2)

    # Check that the values are as expected
    assert r.test1 == "1"
    assert r.test2 == "2"

    # Mute register
    r.mute()

    assert r.test1 == ""
    assert r.test2 == ""

# Generated at 2022-06-14 08:28:18.193647
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    """
    This is a unit-test for the method Register.set_eightbit_call.
    """

    class RgbFg(RenderType):
        ansi = 38

    class RgbBg(RenderType):
        ansi = 48

    fg = Register()
    return

# Generated at 2022-06-14 08:29:05.534365
# Unit test for method unmute of class Register
def test_Register_unmute():
    import sty
    # Test if unmute returns the state before mute() was called.
    rObj = Register()
    rObj.set_renderfunc(sty.RenderType.Sgr, lambda *a: 'x')
    rObj.set_eightbit_call(sty.RenderType.Sgr)
    rObj.set_rgb_call(sty.RenderType.RgbFg)
    rObj.set_eightbit_call(sty.RenderType.RgbFg)
    rObj.set_rgb_call(sty.RenderType.RgbBg)
    rObj.set_eightbit_call(sty.RenderType.RgbBg)
    rObj.red = sty.Style(sty.RgbFg(191, 66, 67))

# Generated at 2022-06-14 08:29:13.934897
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    r = Register()
    r.red = Style(RgbFg(255, 0, 0))
    r.green = Style(RgbFg(0, 255, 0))
    nt = r.as_namedtuple()
    assert nt.red == "\x1b[38;2;255;0;0m"
    assert nt.green == "\x1b[38;2;0;255;0m"

# Generated at 2022-06-14 08:29:23.130761
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertype import EightbitFg, RgbFg

    # Setup register object.
    reg = Register()
    reg.set_renderfunc(EightbitFg, lambda x: "\x1b[38;5;{}m".format(x))
    reg.set_renderfunc(RgbFg, lambda r, g, b: "\x1b[38;2;{};{};{}m".format(r, g, b))

    # Setup expected value.
    expected = "\x1b[38;2;10;20;30m"

    # Default RGB-call should be a Eightbit-call.
    assert reg.rgb_call(250, 240, 230) != expected

    # Changing the RGB-call should change the output of a RGB-call.

# Generated at 2022-06-14 08:29:37.060627
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class RgbFg:
        pass

    class Sgr:
        pass

    # Define renderfunctions
    def sgr_renderfunc(bold: bool = False) -> str:
        return ""

    def rgb_renderfunc(r: int, g: int, b: int) -> str:
        return ""

    # Create register
    register = Register()

    # Set renderfunctions
    register.set_renderfunc(rendertype=Sgr, func=sgr_renderfunc)
    register.set_renderfunc(rendertype=RgbFg, func=rgb_renderfunc)

    # Create Style
    s1 = Style(RgbFg(0, 0, 0), Sgr(bold=True))

    # Assign style
    register.white = s1

    # Check if renderfunc for rgb is set correctly


# Generated at 2022-06-14 08:29:44.653542
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    from .framework import Sty

    sty = Sty()
    r = sty.fg.red
    d = r.as_dict()

    assert(list(d.keys())[0]=="red")
    assert(list(d.values())[0]=="\x1b[38;2;255;0;0m")

    assert(sty.bg.blue.as_dict()["blue"] == "\x1b[48;2;0;0;255m")



# Generated at 2022-06-14 08:29:56.196878
# Unit test for method mute of class Register
def test_Register_mute():
    # create a new register-object
    register = Register()
    # create a query-object for this new register
    API = NamedColorRegister(register)
    # add some colors from the API
    API.register_colors_256({"red": 1, "orange": 3, "yellow": 11, "green": 2})

    # Normal case: muting a register makes all colors empty strings
    register.mute()
    assert register.red == ""
    assert register.orange == ""
    assert register.yellow == ""
    assert register.green == ""

    # Mute again: colors should stay empty strings
    register.mute()
    assert register.red == ""
    assert register.orange == ""
    assert register.yellow == ""
    assert register.green == ""

    # Unmute and add more colors
    register.unmute()

# Generated at 2022-06-14 08:30:01.097255
# Unit test for constructor of class Style
def test_Style():
    """
    Test if constructor works.
    """
    r = Style(1, 2, 3, 4, value="test")

    assert isinstance(r, str)
    assert isinstance(r, Style)

    assert r == "test"

# Generated at 2022-06-14 08:30:07.769539
# Unit test for method __new__ of class Style
def test_Style___new__():

    class MyRenderType(RenderType):
        pass

    class MyOtherRenderType(RenderType):
        pass

    new_style = Style(MyRenderType(1, 2), MyOtherRenderType(3))

    assert new_style == ""
    assert new_style.rules == (MyRenderType(1, 2), MyOtherRenderType(3))



# Generated at 2022-06-14 08:30:19.436353
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    from sty.ansi import fg as sty_fg

    # Set style attributes
    sty_fg.red = Style(RgbFg(255, 0, 0))
    sty_fg.blue = Style(RgbFg(0, 0, 255))
    sty_fg.magenta = Style(RgbFg(255, 0, 255))

    # Create a register
    register = Register()

    # Set renderfuncs and style attributes
    register.set_renderfunc(RgbFg, render_rgb_fg)
    register.red = Style(RgbFg(255, 0, 0))
    register.blue = Style(RgbFg(0, 0, 255))
    register.magenta = Style(RgbFg(255, 0, 255))


# Generated at 2022-06-14 08:30:30.314379
# Unit test for method unmute of class Register
def test_Register_unmute():
    import textwrap
    from .colors import fg, bg, ef, rs

    class A(Register):
        pass

    x = A()
    x.red = Style(fg("red"))
    x.blue = Style(bg("blue"))
    x.bold = Style(ef("bold"))

    x.mute()
    assert x.red == ""
    assert x.blue == ""
    assert x.bold == ""

    x.unmute()
    assert x.red == "\x1b[38;2;217;0;0m"
    assert x.blue == "\x1b[48;2;0;0;217m"
    assert x.bold == "\x1b[1m"

    x.red = Style(fg("red"))
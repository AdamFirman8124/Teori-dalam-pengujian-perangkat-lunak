

# Generated at 2022-06-14 08:20:58.022225
# Unit test for method __call__ of class Register
def test_Register___call__():
    """
    This test ensures that method __call__ of class Register works as intended.
    """
    # TODO: Implement this test
    pass

# Generated at 2022-06-14 08:21:06.905062
# Unit test for method __call__ of class Register
def test_Register___call__():

    # Check Eightbit-call
    fg = Register()

    # Add a Eightbit-call function to register.
    fg.set_eightbit_call(RenderType)
    fg.renderfuncs[RenderType] = lambda x: f"\x1b[38;5;{x}m"

    # Set a style for this register.
    fg.red = Style(RenderType(1))

    # Check if Eightbit-call method returns the same string as Style attribute.
    assert fg(1) == fg.red

    # Check if empty strings are returned when register is muted
    fg.mute()
    assert not fg(1)
    assert not fg("red")
    assert not fg(1, 2, 3)

    # Check RGB-call.
    bg = Register()

    #

# Generated at 2022-06-14 08:21:07.772028
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r

# Generated at 2022-06-14 08:21:19.354564
# Unit test for method __call__ of class Register
def test_Register___call__():
    from . import Register
    from .rendertype import RgbBg
    reg = Register()

    reg.set_eightbit_call(RgbBg)  # 8bit calls are RGB now.
    reg.set_rgb_call(RgbBg)  # RGB calls are RGB now.

    red = RgbBg(100, 0, 0)

    reg.red = Style(red)  # Define a new color attribute.

    # Test 8bit call.
    assert str(reg(1)) == str(red)

    # Test RGB call.
    assert str(reg(20, 20, 20)) == str(red)

    # Test kwargs call.
    assert str(reg(r=10, g=10, b=10)) == str(red)

    # Test string call.

# Generated at 2022-06-14 08:21:31.807095
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertype import EightBit, RgbFg, RgbBg

    reg = Register()
    reg.yellow = Style(EightBit(3))
    reg.red = Style(RgbBg(200, 0, 0))

    reg.set_eightbit_call(EightBit)
    reg.set_rgb_call(RgbFg)

    # Test Eightbit-call
    assert reg(3) == "\x1b[33m"

    # Test RGB-call
    assert reg(200, 0, 0) == "\x1b[38;2;200;0;0m"

    # Test named-style call
    assert reg("yellow") == "\x1b[33m"

    # Test that register is muted correctly.
    reg.mute()
    assert reg("yellow") == ""
    assert reg

# Generated at 2022-06-14 08:21:43.415157
# Unit test for constructor of class Register
def test_Register():

    def renderfunc1(*args):
        return "1"

    def renderfunc2(*args):
        return "2"

    r = Register()
    r.set_renderfunc(Type1, renderfunc1)
    r.set_renderfunc(Type2, renderfunc2)
    r.set_eightbit_call(Type1)
    r.set_rgb_call(Type2)

    r.red = Style(Type1(4))
    r.purple = Style(Type2(4, 2, 1))

    assert r.red == "\x1b[31m"
    assert r.purple == "\x1b[1m"
    assert r(42) == "\x1b[31m"
    assert r(1, 2, 3) == "\x1b[1m"

# Generated at 2022-06-14 08:21:54.022743
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertype import RgbFg
    from .style import Style

    def rgb_func(r, g, b):
        return f"{r}, {g}, {b}"

    def eightbit_func(x):
        return str(x)

    rg = Register()
    rg.set_rgb_call(RgbFg)
    rg.set_eightbit_call(RgbFg)
    rg.set_renderfunc(RgbFg, rgb_func)
    rg.set_renderfunc(RgbFg, eightbit_func)
    rg.green = Style(RgbFg(1, 5, 10))

    assert rg("green") == "\x1b[38;2;1;5;10m"
    assert rg(111) == "111"

# Generated at 2022-06-14 08:21:55.266496
# Unit test for constructor of class Register
def test_Register():
    assert Register()


# Generated at 2022-06-14 08:21:57.448204
# Unit test for constructor of class Register
def test_Register():
    rg = Register()
    assert isinstance(rg, Register)

# Generated at 2022-06-14 08:22:02.330270
# Unit test for constructor of class Register
def test_Register():
    reg = Register()
    assert isinstance(reg, Register)
    assert isinstance(reg.as_dict(), dict)
    assert isinstance(reg.as_namedtuple(), NamedTuple)
    assert isinstance(reg.copy(), Register)



# Generated at 2022-06-14 08:22:10.432605
# Unit test for constructor of class Register
def test_Register():
    fg = Register()
    assert hasattr(fg, "renderfuncs")
    assert hasattr(fg, "is_muted")
    assert hasattr(fg, "eightbit_call")
    assert hasattr(fg, "rgb_call")



# Generated at 2022-06-14 08:22:13.668431
# Unit test for constructor of class Register
def test_Register():
    reg = Register()
    assert(reg.renderfuncs == {})
    assert(reg.is_muted == False)
    assert(reg.eightbit_call == reg.rgb_call)

# Generated at 2022-06-14 08:22:15.460552
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert isinstance(register, Register)

# Generated at 2022-06-14 08:22:22.096986
# Unit test for constructor of class Register
def test_Register():
    class TestRegister(Register):
        pass

    r = TestRegister()
    assert isinstance(r, TestRegister)

    name: str = "test_name"
    value: str = "test_value"

    setattr(r, name, value)
    assert getattr(r, name) == value

    assert r() == ""
    assert r(10) == ""
    assert r(123, 43, 56) == ""



# Generated at 2022-06-14 08:22:33.249197
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    reg.set_eightbit_call(RenderType)
    reg.set_rgb_call(RenderType)

    with pytest.raises(AttributeError):
        reg(1,2,3)

    with pytest.raises(TypeError):
        reg('red')

    # TODO: Check for all calls.
    reg.set_eightbit_call(RenderType)
    reg.set_rgb_call(RenderType)

    reg(0)
    reg(255)

    reg(0,0,0)
    reg(255,255,255)

    with pytest.raises(AttributeError):
        reg.set_eightbit_call(RenderType)
        reg.set_rgb_call(RenderType)

        with pytest.raises(TypeError):
            reg

# Generated at 2022-06-14 08:22:33.915026
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert isinstance(register, Register)


# Generated at 2022-06-14 08:22:38.623894
# Unit test for constructor of class Register
def test_Register():
    # Make sure that objects that are not Styles are not registered.
    r = Register()
    r.test = "foo"
    assert not hasattr(r, "test")

    # Make sure that Styles are registered.
    r = Register()
    r.test = Style()
    assert hasattr(r, "test")



# Generated at 2022-06-14 08:22:40.004804
# Unit test for constructor of class Register
def test_Register():
    assert Register().renderfuncs == {}

# Generated at 2022-06-14 08:22:48.364862
# Unit test for constructor of class Register
def test_Register():
    class RenderType1(RenderType):
        def render(self, code: int) -> str:
            return "\x1b[38;5;%sm" % (code)

    class RenderType2(RenderType):
        def render(self, *args, **kwargs) -> str:
            return "\x1b[38;2;%s;%s;%sm" % (args[0], args[1], args[2])

    r = Register()
    r.set_renderfunc(RenderType1, lambda x: "\x1b[38;5;%sm" % (x))
    r.set_renderfunc(RenderType2, lambda r, g, b: "\x1b[38;2;%s;%s;%sm" % (r, g, b))


# Generated at 2022-06-14 08:23:00.192084
# Unit test for constructor of class Register
def test_Register():

    from .rendertype import Sgr, RgbBg, RgbFg

    def render_bg(x):
        return "\x1b[48;5;" + str(x)

    def render_fg(x):
        return "\x1b[38;5;" + str(x)

    def render_sgr(x):
        return "\x1b[%sm" % x

    def render_rgb_fg(r, g, b):
        return "\x1b[38;2;" + str(r) + ";" + str(g) + ";" + str(b)

    def render_rgb_bg(r, g, b):
        return "\x1b[48;2;" + str(r) + ";" + str(g) + ";" + str(b)

    r = Register()
   

# Generated at 2022-06-14 08:23:17.394273
# Unit test for constructor of class Register
def test_Register():
    from sty import fg, bg, ef, rs

    assert isinstance(fg, Register)
    assert isinstance(bg, Register)
    assert isinstance(ef, Register)
    assert isinstance(rs, Register)

    assert len(fg.renderfuncs) == 9
    assert len(bg.renderfuncs) == 9
    assert len(ef.renderfuncs) == 5
    assert len(rs.renderfuncs) == 2

    assert hasattr(fg, "blue")
    assert hasattr(bg, "green")
    assert hasattr(ef, "bold")
    assert hasattr(rs, "reset_all")

    assert isinstance(fg.blue, Style)
    assert isinstance(bg.green, Style)
    assert isinstance(ef.bold, Style)

# Generated at 2022-06-14 08:23:19.255152
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert isinstance(r, Register)



# Generated at 2022-06-14 08:23:21.586483
# Unit test for constructor of class Register
def test_Register():

    r = Register()
    assert isinstance(r, Register)

# Generated at 2022-06-14 08:23:24.715222
# Unit test for constructor of class Register
def test_Register():
    r = Register()

    assert len(r.__dict__) == 6
    assert r.is_muted == False
    assert len(r.renderfuncs.keys()) == 0

# Generated at 2022-06-14 08:23:25.978910
# Unit test for constructor of class Register
def test_Register():
    assert isinstance(Register(), Register)


# Generated at 2022-06-14 08:23:36.193388
# Unit test for constructor of class Register
def test_Register():
    class TestRenderingType(RenderType):
        pass

    r = Register()

    assert isinstance(r, Register)

    # Test register.set_renderfunc()
    r.set_renderfunc(TestRenderingType, lambda x: "AA" * x)
    assert r.renderfuncs[TestRenderingType](2) == "AAAA"

    # Test register.set_eightbit_call()
    r.set_eightbit_call(TestRenderingType)
    assert r(100) == r.eightbit_call(100)

    # Test register.set_rgb_call()
    r.set_rgb_call(TestRenderingType)
    assert r(1, 2, 3) == r.rgb_call(1, 2, 3)

    # Test register.mute() and register

# Generated at 2022-06-14 08:23:41.690200
# Unit test for constructor of class Register
def test_Register():
    """
    Unit test for constructor of class Register
    """
    r = Register()
    assert isinstance(r, Register)
    assert r.renderfuncs == {}
    assert not r.is_muted
    assert r.eightbit_call.__name__ == "lambda"
    assert r.rgb_call.__name__ == "lambda"

# Generated at 2022-06-14 08:23:53.549089
# Unit test for constructor of class Register
def test_Register():
    def func1() -> str:
        return "\x1b[1m"

    def func2() -> str:
        return "\x1b[2m"

    def func3() -> str:
        return "\x1b[3m"

    def func4(r: int, g: int, b: int) -> str:
        return "\x1b[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

    r1 = Register()
    r1.set_renderfunc(Sgr, func1)
    r1.set_renderfunc(Rgb, func4)
    r1.set_eightbit_call(Sgr)
    r1.set_rgb_call(Rgb)


# Generated at 2022-06-14 08:23:54.774288
# Unit test for constructor of class Register
def test_Register():
    assert isinstance(Register(), Register)

# Generated at 2022-06-14 08:23:56.409085
# Unit test for constructor of class Register
def test_Register():
    reg = Register()
    assert reg.is_muted == False



# Generated at 2022-06-14 08:24:07.213116
# Unit test for constructor of class Register
def test_Register():
    """
    >>> r = Register()
    >>> assert isinstance(r, Register)
    >>> r.is_muted
    False
    >>> r.mute()
    >>> r.is_muted
    True
    >>> r.unmute()
    >>> r.is_muted
    False
    """



# Generated at 2022-06-14 08:24:15.190936
# Unit test for constructor of class Register
def test_Register():
    """Unit test for constructor of class Register"""
    def test_renderfunc(x: int) -> str:
        return str(x)

    new_register = Register()
    new_register.set_renderfunc(int, test_renderfunc)
    new_register.zero = Style(int(0))
    assert new_register.zero == "0"
    assert new_register(0) == "0"

# Generated at 2022-06-14 08:24:17.061257
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert isinstance(r, Register)

# Generated at 2022-06-14 08:24:18.265601
# Unit test for constructor of class Register
def test_Register():
    assert Register() is not None

# Generated at 2022-06-14 08:24:21.571501
# Unit test for constructor of class Register
def test_Register():
    """
    Test if constructor of class Register works as expected.
    """
    reg = Register()

    assert isinstance(reg, Register)

# Generated at 2022-06-14 08:24:23.838391
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert callable(register)
    assert dict == type(register.renderfuncs)

# Generated at 2022-06-14 08:24:25.063708
# Unit test for constructor of class Register
def test_Register():
    r = Register()


# Generated at 2022-06-14 08:24:26.625666
# Unit test for constructor of class Register
def test_Register():
    assert isinstance(Register(), Register)

# Generated at 2022-06-14 08:24:28.309391
# Unit test for constructor of class Register
def test_Register():
    new_register = Register()
    assert new_register is not None

# Generated at 2022-06-14 08:24:29.108759
# Unit test for constructor of class Register
def test_Register():
    Register()

# Generated at 2022-06-14 08:24:48.340365
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertypes import Sgr, EightbitFg
    from .compatibility import compatibility

    r = Register()
    r.set_renderfunc(Sgr, lambda x: "SGR")
    r.set_renderfunc(EightbitFg, lambda x: "EIGHTBITFG")

    r.set_eightbit_call(Sgr)
    assert r(42) == "SGR"

    r.set_eightbit_call(EightbitFg)
    assert r(42) == "EIGHTBITFG"

# Generated at 2022-06-14 08:25:01.573263
# Unit test for method __call__ of class Register
def test_Register___call__():

    from sty import fg, bg, Printer, Rule
    from sty.types import *

    # Check Eightbit_call
    assert fg(144) == Printer().render(fg=144)
    assert fg(144) != Printer().render(bg=144)

    # Check RGB_call
    assert fg(14, 142, 24) == Printer().render(fg=Rgb(14, 142, 24))
    assert fg(0, 12, 145) == Printer().render(fg=0, fg_rgb=(0, 12, 145))

    # Check string-call
    assert fg("green") == Printer().render(fg=2)

    # Check if mute works
    fg.mute()
    assert fg(144) == ""

    # Check if unmute works

# Generated at 2022-06-14 08:25:07.246936
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    register = Register()
    register.red = Style(RgbFg(1, 2, 3), Sgr(1))
    register.blue = Style(RgbFg(3, 2, 1), Sgr(1))
    assert register.as_dict() == {"red": "\x1b[38;2;1;2;3m\x1b[1m", "blue": "\x1b[38;2;3;2;1m\x1b[1m"}

# Generated at 2022-06-14 08:25:15.538197
# Unit test for method __new__ of class Style
def test_Style___new__():

    class R(RenderType):
        rules = ("RULE",)
        args = (1,)
        kwargs = {"kwarg": 42}

    class R1(RenderType):
        rules = ("RULE1",)
        args = (2,)
        kwargs = {"kwarg": 43}

    class R2(RenderType):
        rules = ("RULE2",)
        args = (3,)
        kwargs = {"kwarg": 44}

    s = Style(R(), R1(), R2())
    assert isinstance(s, Style)
    assert isinstance(s, str)
    assert s.rules == (R(), R1(), R2())
    assert str(s) == ""

    s = Style(value="HELLO")
    assert isinstance(s, Style)

# Generated at 2022-06-14 08:25:23.750391
# Unit test for method mute of class Register
def test_Register_mute():
    test = Register()
    test.set_renderfunc(RenderType, lambda x: rf"\x1b{x}")
    test.reset = Style(RenderType("[0m"))
    test.test = Style(RenderType("[1m"))
    test.mute()
    assert test.reset == ""
    assert test.test == ""
    test.unmute()
    assert test.reset == r"\x1b[0m"
    assert test.test == r"\x1b[1m"
    test.mute()
    assert test.reset == ""
    assert test.test == ""
    test.unmute()
    assert test.reset == r"\x1b[0m"
    assert test.test == r"\x1b[1m"


# Generated at 2022-06-14 08:25:33.176772
# Unit test for method __call__ of class Register
def test_Register___call__():
    # Create a register-object with some style rules
    class TransparentRegister(Register):
        def __init__(self):
            super().__init__()
            self.red = Style(RgbFg(255, 0, 0))
            self.blue = Style(RgbFg(0, 0, 255))

    # Create test register
    tr = TransparentRegister()

    # Test if 8bit-call works.
    assert tr(10) == tr.red

    # Test if RGB-call works.
    assert tr(200, 40, 40) == tr.blue

    # Test if Attribute-call works.
    assert tr("red") == tr.red



# Generated at 2022-06-14 08:25:36.618047
# Unit test for constructor of class Register
def test_Register():

    assert isinstance(fg, Register)
    assert isinstance(bg, Register)
    assert isinstance(ef, Register)
    assert isinstance(rs, Register)



# Generated at 2022-06-14 08:25:43.167255
# Unit test for method copy of class Register
def test_Register_copy():
    r1 = Register()
    r1.white = Style(Sgr(1), RgbFg(255, 255, 255))
    r1.black = Style(Sgr(0), RgbFg(0, 0, 0))

    r2 = r1.copy()
    assert r2.white != r1.white
    assert r2.black != r1.black
    assert r2.white != ""
    assert r2.black != ""

# Generated at 2022-06-14 08:25:47.685084
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    r = Register()
    r.red = Style(RgbFg(255, 0, 0))
    r.green = Style(RgbFg(0, 255, 0))

    nt: NamedTuple = r.as_namedtuple()
    assert nt.red == r.red

    assert nt.green == r.green


# Generated at 2022-06-14 08:25:53.649671
# Unit test for constructor of class Style
def test_Style():
    r = Style(RgbFg(255, 0, 0), SgrBold(), SgrUnderline(), value="\x1b[31m\x1b[1m\x1b[4m")
    assert str(r) == "\x1b[31m\x1b[1m\x1b[4m"



# Generated at 2022-06-14 08:26:17.778343
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """
    Unit test for method set_renderfunc of class Register
    """

    class Foo(RenderType):
        """
        Just a dummy class.
        """
        pass

    def func(x: int) -> str:
        """
        Just a dummy function.
        """
        return "foo"

    reg = Register()
    reg.set_renderfunc(Foo, func)
    assert hasattr(reg, "renderfuncs")
    assert reg.renderfuncs == {Foo: func}


# Generated at 2022-06-14 08:26:31.386650
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    # Test dict
    # The dict maps rendertypes to the render-functions that are used during the test.
    # The render-functions are all very simple: They return the name of the rendertype followed by the args.
    test_renderfuncs = {
        RenderType: lambda rendertype, *args: f"{rendertype.__name__} {args}",
        RenderType2: lambda *args: f"{RenderType2.__name__} {args}",
    }

    # Create registers to test with..
    class Register_test_obj(Register):
        pass

    register_test_obj = Register_test_obj()

    # Add test_renderfuncs to the registers
    for rendertype, func in test_renderfuncs.items():
        register_test_obj.set_renderfunc(rendertype, func)

   

# Generated at 2022-06-14 08:26:35.698382
# Unit test for method copy of class Register
def test_Register_copy():

    register = Register()
    register.set_renderfunc(RgbFg, lambda x, y, z: "Render")
    register.__setattr__("red", Style(RgbFg(1,2,3)))

    new_register = register.copy()

    assert register != new_register
    assert register.renderfuncs != new_register.renderfuncs
    assert register.red != new_register.red

    assert register.red == Style(RgbFg(1,2,3))
    assert new_register.red == Style(RgbFg(1,2,3))


# Generated at 2022-06-14 08:26:48.562269
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    """
    This function tests the method ``__setattr__`` of the ``Register`` class.
    """

    r: Register = Register()
    r.red = Style(RgbFg(200, 0, 0))
    r.bold = Style(Sgr(1))
    r.boldred = Style(r.red, r.bold)

    assert r.red == "\x1b[38;2;200;0;0m"
    assert r.bold == "\x1b[1m"
    assert r.boldred == "\x1b[38;2;200;0;0m\x1b[1m"

    r.green = Style(RgbFg(0, 200, 0))
    r.red = Style(RgbFg(200, 0, 0))


# Generated at 2022-06-14 08:27:01.356636
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    """
    Tests the logic of `Register.__setattr__`.
    """
    def rendertypeA_func(*args: Tuple[int, int], **kwargs) -> str:
        return "".join([str(a) for a in args[:2]])

    def rendertypeB_func(b) -> str:
        return str(b)

    RenderTypeA = RenderType("RenderTypeA", (int, int))
    RenderTypeB = RenderType("RenderTypeB", (int,))

    reg = Register()
    reg.set_renderfunc(RenderTypeA, rendertypeA_func)
    reg.set_renderfunc(RenderTypeB, rendertypeB_func)

    reg.test = Style(RenderTypeA(1, 2), RenderTypeB(4))

    assert str(reg.test) == "12"

# Generated at 2022-06-14 08:27:07.381970
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    r = Register()

    class X(RenderType):
        def render_eightbit(self, x):
            return "8"

        def render_rgb(self, r, g, b):
            return "24"

    r.set_renderfunc(X, X.render_eightbit)
    r.set_eightbit_call(X)

    assert r(42) == "8"
    assert r(42, 43, 44) == "24"



# Generated at 2022-06-14 08:27:17.186107
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    class TestRegister(Register):
        pass

    tr = TestRegister()
    setattr(tr, "foo", "42")
    setattr(tr, "bar", "100")
    setattr(tr, "baz", "101")

    d = tr.as_dict()

    assert "foo" in d.keys()
    assert d["foo"] == "42"
    assert "bar" in d.keys()
    assert d["bar"] == "100"
    assert "baz" in d.keys()
    assert d["baz"] == "101"
    assert "as_dict" not in d.keys()



# Generated at 2022-06-14 08:27:28.461171
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertypes import RgbFg, RgbBg, Sgr0, Sgr, Reset

    fg = Register()
    fg.set_renderfunc(RgbFg, lambda r, g, b: "\x1b[38;2;{};{};{}m".format(r, g, b))
    fg.set_renderfunc(RgbBg, lambda r, g, b: "\x1b[48;2;{};{};{}m".format(r, g, b))
    fg.set_renderfunc(Sgr0, lambda x: "\x1b[{}m".format(x))
    fg.set_renderfunc(Sgr, lambda x: "\x1b[{}m".format(x))

# Generated at 2022-06-14 08:27:32.582172
# Unit test for method __new__ of class Style
def test_Style___new__():
    """
    Class Style has no public methods. This test is to test the __new__ method of Style.
    """

    class A(RenderType):
        pass

    style = Style(A())
    assert isinstance(style, Style)
    assert style.rules == (A(),)

# Generated at 2022-06-14 08:27:42.365301
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    fg = Register()
    fg.set_renderfunc(RgbFg, lambda r, g, b: "\x1b[38;2;{};{};{}m".format(r, g, b))
    fg.set_eightbit_call(RgbFg)
    fg.r = Style(RgbFg(255,0,0))

    assert fg(255, 0, 0) == "\x1b[38;2;255;0;0m"
    assert fg[255, 0, 0] == "\x1b[38;2;255;0;0m"
    assert fg["r"] == "\x1b[38;2;255;0;0m"
    assert fg.r == "\x1b[38;2;255;0;0m"



# Generated at 2022-06-14 08:28:04.415920
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    cls = Register()
    cls.set_renderfunc(RenderType, lambda x: "foo")
    cls.set_eightbit_call(RenderType)
    assert cls(42) == "foo"



# Generated at 2022-06-14 08:28:14.151873
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    fg = Register()
    fg.set_rgb_call(RgbFg)
    assert fg.rgb_call(5,5,5) == "5,5,5"
    fg.set_rgb_call(RgbFg)
    fg.set_rgb_call(RgbBg)
    assert fg.rgb_call(5,5,5) == "5,5,5"
    fg.set_rgb_call(RgbBg)
    assert fg.rgb_call(5,5,5) == "5,5,5"
    fg.set_rgb_call(RgbFg)
    assert fg.rgb_call(5,5,5) == "5,5,5"

# Generated at 2022-06-14 08:28:26.093226
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertypes import RgbFg, Sgr

    # Define a class that has similar functionality to style.RgbFg
    class DummyRgbFg(RenderType):

        def __init__(self, r, g, b):
            self.r = r
            self.g = g
            self.b = b

        def args(self):
            return self.r, self.g, self.b

        def render(self, r, g, b):
            return f"dummy-{self.r}-{self.g}-{self.b}"

    # Create an instance of class Register
    r = Register()

    # Add new render-function for a render type
    r.set_renderfunc(DummyRgbFg, DummyRgbFg.render)

    # Create a style object of

# Generated at 2022-06-14 08:28:33.654362
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class TestRenderType(RenderType):
        def __new__(cls, *args, **kwargs) -> str:
            return "42"

    def my_renderfunc(rendertype: Type[RenderType], *args) -> str:
        return f"{args[0]}-{args[1]}-{args[2]}"

    r1 = Register()

    r1.set_renderfunc(TestRenderType, my_renderfunc)

    r1.set_rgb_call(TestRenderType)

    assert r1(42, 42, 42) == "42-42-42"

# Unit Test for __call__ method of class Register

# Generated at 2022-06-14 08:28:36.195532
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertype import RgbFg

    fg = Register()
    fg.renderfuncs[RgbFg] = lambda r, g, b: r + g + b

    fg.set_rgb_call(RgbFg)
    assert fg(3, 4, 7) == 14



# Generated at 2022-06-14 08:28:49.301365
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """
    Unit test for method set_renderfunc of class Register

    This test creates a register-object with a predefined renderfunc. It then replaces
    this renderfunc with another one.
    """
    def render_func(
        *args: Iterable[Union[int, NamedTuple, List, str]],
    ) -> str:
        return "rendered:" + str(args)  # pragma: no cover

    def render_func2(
        *args: Iterable[Union[int, NamedTuple, List, str]],
    ) -> str:
        return "rendered2:" + str(args)  # pragma: no cover

    from .rendertype import RenderType, Sgr

    register = Register()
    register.set_renderfunc(Sgr, render_func)

    # Insert a style for this register. This should be

# Generated at 2022-06-14 08:29:02.073714
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    # Create a mock-register with some attributes.
    class TestRegister(Register):
        pass

    TestRegister.a = Style(value=1)
    TestRegister.b = Style(value=2)
    TestRegister.c = Style(value=3)

    # Expected result
    expected_type = NamedTuple
    expected_fields = ("a", "b", "c")
    expected_values = (1, 2, 3)

    # Get result
    result = TestRegister().as_namedtuple()

    # Test
    assert isinstance(result, expected_type)
    assert result.__fields__ == expected_fields
    assert result == expected_values
    assert result[0] == 1
    assert result[1] == 2
    assert result[2] == 3

# Generated at 2022-06-14 08:29:10.521326
# Unit test for method __call__ of class Register
def test_Register___call__():
    red_str = '\x1b[38;2;255;0;0m\x1b[1m'
    fg = Register()

    fg.red = Style(RgbFg(255, 0, 0), Sgr(1))

    # Custom color:
    assert fg("red") == red_str

    fg.set_eightbit_call(RgbFg)
    assert fg(214) == '\x1b[38;2;196;96;0m'

    fg.set_rgb_call(RgbFg)
    assert fg(255, 0, 0) == '\x1b[38;2;255;0;0m'

    # Default color:
    fg.red = Style(RgbFg(255, 0, 0))
    assert f

# Generated at 2022-06-14 08:29:17.630977
# Unit test for method __new__ of class Style
def test_Style___new__():

    from .rendertype import RgbFg, Sgr

    test_style = Style(RgbFg(1, 5, 10), Sgr(1))

    assert isinstance(test_style, Style)
    assert isinstance(test_style, str)
    assert test_style.rules == (RgbFg(1, 5, 10), Sgr(1))
    assert str(test_style) == '\x1b[38;2;1;5;10m\x1b[1m'

    test_style = Style(RgbFg(1, 5, 10), Sgr(1), "Test")

    assert isinstance(test_style, Style)
    assert isinstance(test_style, str)
    assert test_style.rules == (RgbFg(1, 5, 10), Sgr(1))


# Generated at 2022-06-14 08:29:28.493404
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    class Test1:
        pass

    class Test2:
        pass

    class Test3:
        pass

    class Test4:
        pass

    register = Register()
    register.set_renderfunc(Test1, lambda x: "Test1(" + str(x) + ")")
    register.set_renderfunc(Test2, lambda x: "Test2(" + str(x) + ")")
    register.set_renderfunc(Test3, lambda x: "Test3(" + str(x) + ")")
    register.set_renderfunc(Test4, lambda x: "Test4(" + str(x) + ")")
    register.set_eightbit_call(Test1)


# Generated at 2022-06-14 08:30:12.761534
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class Rs(Register):
        pass

    r = Rs()
    r.reset = Style(Sgr(0))

    assert str(r.reset) == "\x1b[0m"

    r.set_renderfunc(Sgr, lambda *x: "a" + str(x))

    assert str(r.reset) == "a(0)"


# Generated at 2022-06-14 08:30:26.414142
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    def ret_rgb_string(*args, **kwargs) -> str:
        return "rgb string"

    def ret_8bit_string(*args, **kwargs) -> str:
        return "8bit string"

    def test_mute():
        def do_test(r, attr, value, rendered_value, is_muted):
            # set up a new() style and set it
            style = Style(rendertype1(*value))
            setattr(r, attr, style)

            # check for muted state
            assert r.is_muted is is_muted

            # check if correct string is returned
            assert getattr(r, attr) == rendered_value

        # First test case: Register is muted.
        r = Register()

# Generated at 2022-06-14 08:30:37.566978
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    # test_item is just a dummy class that implements the basic functions of RenderType
    class test_item(RenderType):
        def __init__(self, r, g, b, sgr=None):
            self.args = (r, g, b)
            self.sgr = sgr
            self.esc = "test1"
            self.sgr_esc = "test2"

    # func is a testfunc
    func = lambda *args, **kwargs: "test3"

    # register is just a subclass of Register
    class register(Register):
        pass

    # This test-register gets a render-func for RgbFg.
    test_reg = register()

    test_reg.set_renderfunc(test_item, func)

    assert test_item in test_reg.renderfuncs


# Unit test

# Generated at 2022-06-14 08:30:42.646029
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    assert Register().as_dict() == {}

    class R(Register):
        a = Style(value="a")
        b = Style(value="b")

    assert R().as_dict() == {"a": "a", "b": "b"}


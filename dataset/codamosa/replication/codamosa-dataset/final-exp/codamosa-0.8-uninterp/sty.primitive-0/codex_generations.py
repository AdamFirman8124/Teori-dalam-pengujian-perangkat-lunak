

# Generated at 2022-06-14 08:20:57.796744
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """
    Test Register.set_renderfunc
    """
    import pytest
    from .rendertype import _get_stderr, _get_stdout
    from .style import Style, StyleFactory

    cb = StyleFactory(
        "cb",
        register=Register(),
        sgrrender=_get_stdout().write,
        eightbit=32,
        eightbitrender=_get_stdout().write,
    )

    def render0(a):
        return a

    def render1(a):
        return a + 100

    cb.set_renderfunc(type(cb.eightbit), render0)

    assert cb(32) == 32

    cb.set_renderfunc(type(cb.eightbit), render1)
    assert cb(32) == 132

    # Test if we can only

# Generated at 2022-06-14 08:21:04.483352
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    # Setup:
    reg = Register()
    # Create dummy render function:
    def rf(x): return f"R{x}R"
    # Setup renderfuncs:
    reg.renderfuncs = {type(BaseFg(0)): rf}
    # Call method:
    reg.set_rgb_call(BaseFg)
    # Assertion:
    assert reg(1) == ""
    assert reg(1,2,3) == "R(1,2,3)R"

# Generated at 2022-06-14 08:21:17.677509
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertype import RenderType, RgbBg, RgbFg, RenderTypeABC
    from .renderstyle import render_style

    fg = Register()

    def render_rgb_fg(r: int, g: int, b: int) -> str:
        return "\x1b[38;2;{};{};{}m".format(r, g, b)

    fg.set_renderfunc(RgbFg, render_rgb_fg)
    fg.set_rgb_call(RgbFg)

    assert fg(10, 42, 100) == "\x1b[38;2;10;42;100m"

    assert fg.rgb_call(10, 42, 100) == "\x1b[38;2;10;42;100m"


# Unit test

# Generated at 2022-06-14 08:21:31.434854
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .render import RgbBg, RgbFg, SGR

    # Test default rendertype
    r = Register()
    r.test_red = Style(RgbBg(255, 0, 0))
    assert str(r.test_red) == RgbBg(255, 0, 0).render()

    # Test SGR rendertype
    r.set_rgb_call(rendertype=SGR)
    assert str(r(255, 0, 0)) == SGR.render(RgbBg(255, 0, 0))

    # Test RgbFg rendertype
    r.set_rgb_call(rendertype=RgbFg)
    assert str(r(255, 0, 0)) == RgbFg(255, 0, 0).render()

    # Test RgbBg rendertype
   

# Generated at 2022-06-14 08:21:34.982972
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    testreg = Register()
    testreg.set_rgb_call(RgbBg)

    assert testreg.rgb_call == RgbBg.func

# Generated at 2022-06-14 08:21:48.680761
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .sty import Sty
    from .rendertype import RgbFg, Sgr, Bg

    register = Register()
    register.set_renderfunc(RgbFg, Sty.render_rgb_fg)
    register.set_renderfunc(Sgr, Sty.render_sgr)
    register.set_renderfunc(Bg, Sty.render_bg)


    class CustomRegister(Register):

        def __init__(self):
            super().__init__()
            self.red = Style(RgbFg(255, 0, 0), Sgr(1))
            self.green = Style(RgbFg(0, 255, 0), Sgr(1))
            self.blue = Style(RgbFg(0, 0, 255), Sgr(1))

# Generated at 2022-06-14 08:22:01.861397
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # create register
    r = Register()

    # define renderfunctions
    def renderfunc_RgbFg(r, g, b):
        return f"\x1b[38;2;{r};{g};{b}m"

    def renderfunc_RgbBg(r, g, b):
        return f"\x1b[48;2;{r};{g};{b}m"

    def renderfunc_RgbEf(r, g, b):
        return f"\x1b[48;2;{r};{g};{b}m"

    # register renderfunctions
    r.set_renderfunc(RenderType.RGB_FG, renderfunc_RgbFg)
    r.set_renderfunc(RenderType.RGB_BG, renderfunc_RgbBg)


# Generated at 2022-06-14 08:22:12.675295
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class Foo:
        pass

    def renderfunc_foo(x: int) -> str:
        return f"foo({x})"

    def renderfunc_bar(x: int) -> str:
        return f"bar({x})"

    r = Register()
    r.set_renderfunc(Foo, renderfunc_foo)

    assert r.renderfuncs[Foo] == renderfunc_foo

    r.set_renderfunc(Foo, renderfunc_bar)

    assert r.renderfuncs[Foo] == renderfunc_bar


TEST_CODE_AS_DICT = {
    "broken": "\x1b[0m\x1b[38;2;85;85;85m\x1b[2m"
}


# Generated at 2022-06-14 08:22:24.268236
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    """
    test_Register_set_rgb_call

    This function tests the implementation of method 'set_rgb_call' of the class Register.
    """
    from .rendertype import RgbFg, Sgr
    from .helper import render_sgr_call_func, render_rgb_call_func

    rg = Register()
    rg.set_renderfunc(Sgr, render_sgr_call_func)
    rg.set_renderfunc(RgbFg, render_rgb_call_func)

    rg.default = Style(RgbFg(10, 20, 30))

    # Assert that the function 'rg(*args)' is using the rgb-render-func.
    assert rg(10, 20, 30) == "\x1b[38;2;10;20;30m"  # R

# Generated at 2022-06-14 08:22:35.268633
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class RgbFg(RenderType):
        aliases = ["rgb_fg"]

    class RgbBg(RenderType):
        aliases = ["rgb_bg"]

    def ansi_seq_to_rgb(r, g, b):
        return f"{r};{g};{b}"

    reg = Register()

    reg.set_renderfunc(RgbFg, ansi_seq_to_rgb)

    reg.set_rgb_call(RgbFg)

    assert reg(255, 0, 0) == "255;0;0"

    reg.set_renderfunc(RgbBg, ansi_seq_to_rgb)

    reg.set_rgb_call(RgbBg)

    assert reg(255, 0, 0) == "255;0;0"



# Generated at 2022-06-14 08:22:56.758169
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # Create two rendertypes
    RenderType1 = RenderType(name="type1", ansi_code_24bit=100)
    RenderType2 = RenderType(name="type2", ansi_code_24bit=200)

    # Create Register instance
    Reg = Register()

    # Define renderfunctions
    Reg.renderfuncs.update(
        {
            RenderType1: lambda r, g, b: f"\x1b[{RenderType1.ansi_code_24bit}m",
            RenderType2: lambda r, g, b: f"\x1b[{RenderType2.ansi_code_24bit}m",
        }
    )

    # Define some styles
    Reg.red = Style(RenderType1(10, 42, 42))

# Generated at 2022-06-14 08:23:07.034490
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # Test with subclass of Register
    class RegisterSubclass(Register):
        pass

    register = RegisterSubclass()

    def rgb_call(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    register.set_renderfunc(rendertype=RgbFg, func=rgb_call)

    register.set_rgb_call(rendertype=RgbFg)

    assert register(255, 0, 0) == "\x1b[38;2;255;0;0m"

    # Test with instance of Register class
    register = Register()


# Generated at 2022-06-14 08:23:18.746019
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # Test class used for unit testing.
    class render_type1():
        def __init__(self, a: int):
            pass

    class render_type2():
        def __init__(self, a: int):
            pass

    # Create new register-object and test that calls do not work before setting a
    # render-type for the calls.
    reg = Register()
    with pytest.raises(TypeError):
        reg(123)
    with pytest.raises(TypeError):
        reg(1, 2, 3)

    # Add new render-types.
    reg.set_renderfunc(render_type1, lambda a, b, c: (a, b, c))
    reg.set_renderfunc(render_type2, lambda a: a)

    # Set render-type for eightbit and rgb

# Generated at 2022-06-14 08:23:22.544094
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    r = Register()
    r.set_rgb_call(RgbFg)
    assert r.as_dict() == {"set_rgb_call": ""}



# Generated at 2022-06-14 08:23:31.766297
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from sty.render import RgbFg
    from sty.render import ansi_code

    fg = Register()
    fg.set_renderfunc(RgbFg, lambda r, g, b: ansi_code("38;2;{};{};{}m".format(r, g, b)))
    fg.set_rgb_call(RgbFg)
    assert fg(255, 255, 255) == ansi_code("38;2;255;255;255m")
    assert type(fg(255, 255, 255)) == str


# Generated at 2022-06-14 08:23:38.288567
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertype import RgbcFg, RgbcBg

    r1 = Register()

    r1.set_renderfunc(RgbcFg, lambda r, g, b: (r, g, b))

    r1.set_rgb_call(RgbcFg)

    assert r1(200, 50, 0) == (200, 50, 0)



# Generated at 2022-06-14 08:23:51.300509
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from sty.rendertype import RgbBg

    # Create a new class with the methods of base class register
    class MyRegister(Register):
        pass

    # create a new register-object
    r = MyRegister()

    # set render-functions
    r.set_renderfunc(RgbBg, lambda r, g, b: "\x1b[48;2;{};{};{}m".format(r, g, b))

    # define some styles
    r.red = Style(RgbBg(255, 0, 0))
    r.blue = Style(RgbBg(0, 0, 255))

    # assert that both styles are correctly created
    assert str(r.red) == "\x1b[48;2;255;0;0m"

# Generated at 2022-06-14 08:24:03.293295
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import RgbFg

    fg = Register()
    style: Style = Style(RgbFg(10, 20, 30))

    assert str(style) == "\x1b[38;2;10;20;30m"

    # Change renderfunc for rgb-calls.
    fg.set_rgb_call(RgbFg)

    # Define test renderfunc
    def render_test(x, y, z):
        return "%s:%s:%s" % (x, y, z)

    # Assing new renderfunc
    fg.set_renderfunc(RgbFg, render_test)

    assert str(style) == "10:20:30"

    # Check if RGB-call can handle integers as inputs.

# Generated at 2022-06-14 08:24:10.870923
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    """
    This is a bit of a workaround. The issue is that the attributes of a register
    class are only created when they are first accessed. Because of that, the
    function ``set_rgb_call`` doesn't work unless at least one attribute of the
    color register class was accessed before.

    This is a hack to circumvent this behaviour.
    """

    r = Register()

    r.set_rgb_call(RenderType.RgbBg)

    r.black = Style(RenderType.RgbFg(0, 0, 0))

    assert r.black == "\x1b[48;2;0;0;0m\x1b[38;2;0;0;0m"

# Generated at 2022-06-14 08:24:16.999884
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    r = Register()
    r.set_renderfunc(RenderType.rgb_fg, lambda r, g, b: str(r) + str(g) + str(b))  # noqa
    r.set_rgb_call(RenderType.rgb_fg)
    assert r(1, 2, 3) == "123"

# Generated at 2022-06-14 08:24:32.526459
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    reg1 = Register()
    reg2 = Register()

    sgr = lambda *args: f"Sgr:{args}"
    rgb = lambda *args: f"RGB:{args}"

    reg1.set_renderfunc(type(Sgr), sgr)
    reg2.set_renderfunc(type(RgbFg), rgb)

    reg1.set_rgb_call(type(Sgr))
    reg2.set_rgb_call(type(RgbFg))

    assert reg1(100, 100, 100) == "Sgr:100,100,100"
    assert reg2(100, 100, 100) == "RGB:100,100,100"



# Generated at 2022-06-14 08:24:38.999176
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .ansi_csi import RgbFg
    from .rendertype import RenderType

    def render_test(r: int, g: int, b: int) -> str:
        return f"{r};{g};{b}"

    r1: Register = Register()
    r1.set_renderfunc(RgbFg, render_test)

    r1.set_rgb_call(RgbFg)
    assert r1(10, 20, 30) == "10;20;30"



# Generated at 2022-06-14 08:24:51.971482
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    RgbBg = RenderType()
    RgbFg = RenderType()
    SgrBold = RenderType()
    SgrReverse = RenderType()

    fg = Register()
    fg.set_rgb_call(RgbFg)
    fg.set_renderfunc(RgbFg, lambda r, g, b: "\x1b[38;2;{};{};{}m".format(r, g, b))
    fg.set_renderfunc(SgrBold, lambda: "\x1b[1m")

    # RGB Call has been set to RgbFg
    assert fg(10, 42, 50) == "\x1b[38;2;10;42;50m"



# Generated at 2022-06-14 08:24:57.758604
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    def dummy(r, g, b):
        return (r, g, b)

    r = Register()
    r.set_rgb_call(RenderType)
    assert r.rgb_call(255, 255, 255) == "\x1b[38;2;255;255;255m"

# Generated at 2022-06-14 08:25:04.904660
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class Rgb(RenderType):
        @property
        def args(self):
            return (1,2,3)

    rs = Register()
    rs.set_renderfunc(Rgb, lambda r, g, b: f'\x1b[38;2;{r};{g};{b}m')
    rs.set_rgb_call(Rgb)

    assert str(rs(1,2,3)) == '\x1b[38;2;1;2;3m'
    assert str(rs(15, 255, 101)) == '\x1b[38;2;15;255;101m'


# Generated at 2022-06-14 08:25:13.070226
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertypes import Sgr, RgbFg

    r = Register()
    r.set_renderfunc(Sgr, lambda x: "SGRFUNC")
    r.set_renderfunc(RgbFg, lambda x, y, z: "RGBFUNC")

    r.set_rgb_call(RgbFg)

    assert r(101, 102, 103) == "RGBFUNC"
    assert r(104) == ""
    assert r("foo") == ""
    assert r(None) == ""
    assert r(1, 2, 3, 4, 5) == ""


# Generated at 2022-06-14 08:25:27.236732
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    """
    Unit test for method set_rgb_call of class Register.
    """
    # Create register
    register = Register()

    # Define some dummy rendertype and renderfunc
    class DummyRgbRenderType(RenderType):
        pass

    def dummy_rgb_renderfunc(r: int, g: int, b: int) -> str:
        return f"{r}{g}{b}"

    # Add renderfunc
    register.set_renderfunc(DummyRgbRenderType, dummy_rgb_renderfunc)

    # Set rendertype for rgb-calls
    register.set_rgb_call(DummyRgbRenderType)

    # Make a rgb-call
    result = register(10, 42, 255)

    # Make assertion
    assert result == "10422255"



# Generated at 2022-06-14 08:25:35.605643
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    def f1(*args, **kwargs):
        return "f1"

    class A(RenderType):
        ...

    class B(RenderType):
        ...

    reg = Register()
    reg.set_renderfunc(A, f1)

    reg.set_rgb_call(B)
    assert reg.rgb_call is None

    reg.set_rgb_call(A)
    assert reg.rgb_call(1, 2, 3) == "f1"



# Generated at 2022-06-14 08:25:46.292607
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertype import RgbBg, RgbFg
    from .render import STY_VARIABLES

    # Create register and set renderfunc for RgbBg
    reg = Register()
    f = lambda a, b, c: "RgbBg({}, {}, {})".format(a, b, c)
    reg.set_renderfunc(rendertype=RgbBg, func=f)

    # Create initial style
    s = Style(RgbBg(255, 255, 255), RgbFg(0, 0, 0))

    # Set style as attribute of register
    setattr(reg, "red", s)

    # Check if initial 8-bit call works
    assert reg("red") == "RgbBg(255, 255, 255)"

    # Change 8-bit call to RgbF

# Generated at 2022-06-14 08:25:57.175464
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    def dummy_func(r, g, b):
        return f"dummy-func({r}, {g}, {b})"
    def dummy_func_2(r, g, b):
        return f"dummy-func-2({r}, {g}, b)"

    r = Register()
    r.set_rgb_call(dummy_func)

    assert r(255, 255, 255) == dummy_func(255, 255, 255)

    r.set_rgb_call(dummy_func_2)

    assert r(255, 255, 255) == dummy_func_2(255, 255, 255)



# Generated at 2022-06-14 08:26:17.911944
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    """
    This function is used to test the set_rgb_call method of the Register class.
    """

    def renderfunc(r, g, b):
        return "ansi-sequence-" + str(r) + str(g) + str(b)

    class CustomRenderType(RenderType):
        """
        This is a custom rendertype class that is used to test the ``set_rgb_call`` method
        of the ``Register`` class.
        """

    class CustomRegister(Register):
        """
        This is a custom register class that is used to test the ``set_rgb_call`` method
        of the ``Register`` class.
        """

    register: CustomRegister = CustomRegister()
    assert register.rgb_call(1, 2, 3) == (1, 2, 3)

    register.set_renderfunc

# Generated at 2022-06-14 08:26:31.425532
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import RgbFg, RgbBg, EightBit

    def rgb_fg(r, g, b):
        return "\x1b[38;2;{};{};{}m".format(r, g, b)

    def rgb_bg(r, g, b):
        return "\x1b[48;2;{};{};{}m".format(r, g, b)

    def eightbit(code):
        return "\x1b[38;5;{}m".format(code)

    def eightbit_bg(code):
        return "\x1b[48;5;{}m".format(code)

    def eightbit_bg_bold(code):
        return "\x1b[48;5;{};1m".format(code)

    r1 = Register()


# Generated at 2022-06-14 08:26:45.070071
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class _RgbFg(RenderType):
        """
        This is an example Render-Type.
        """

        def render(self) -> str:
            return f"\x1b[38;2;{self.r};{self.g};{self.b}m"

    class _RgbBg(RenderType):
        """
        This is an example Render-Type.
        """

        def render(self) -> str:
            return f"\x1b[48;2;{self.r};{self.g};{self.b}m"

    class _SgrFg(RenderType):
        """
        This is an example Render-Type.
        """

        def render(self) -> str:
            return f"\x1b[38;5;{self.code}m"


# Generated at 2022-06-14 08:26:50.443910
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .render import RgbBg

    class MyRegister(Register):
        # Attribute attr_name
        attr_name1 = Style(RgbBg(10, 20, 30))

    myreg = MyRegister()
    myreg.set_rgb_call(RgbBg)
    rgb_call_result = myreg.rgb_call(1, 2, 3)
    assert rgb_call_result == myreg.attr_name1

# Generated at 2022-06-14 08:27:02.971677
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from sty import fg

    fg_copy = fg.copy()

    setattr(fg_copy, "test", Style(fg(1)))
    setattr(fg_copy, "test_new", Style(fg(2)))

    assert fg_copy.test == '\x1b[38;5;1m'
    assert fg_copy.test_new == '\x1b[38;5;2m'

    fg_copy.set_rgb_call(fg.rgb.rgb8)

    assert fg_copy.test == '\x1b[38;2;1;0;0m'
    assert fg_copy.test_new == '\x1b[38;2;2;0;0m'

# Generated at 2022-06-14 08:27:10.530262
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import RgbBg, RgbFg
    from .sequtils import rgb_to_sixbit

    def render_rgb(R: int, G: int, B: int) -> str:
        r, g, b = rgb_to_sixbit(R, G, B)
        return f"\x1b[38;2;{r};{g};{b}m"

    reg = Register()
    reg.set_renderfunc(RgbFg, render_rgb)
    reg.set_rgb_call(RgbFg)
    assert reg.rgb_call(0, 0, 0) == "\x1b[38;2;0;0;0m"

# Generated at 2022-06-14 08:27:14.701990
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class DummyClass:
        pass

    dummy = DummyClass()
    dummy.renderfuncs = {RenderType: lambda: "test"}
    dummy.set_rgb_call(RenderType)
    assert dummy.rgb_call == "test"

# Generated at 2022-06-14 08:27:23.733876
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from sty import RgbFg, RgbBg
    from sty.utils import rgb_to_ansi256
    from sty.ansi256colors import color_table

    r = Register()
    r.set_renderfunc(RgbFg, rgb_to_ansi256)
    r.set_renderfunc(RgbBg, rgb_to_ansi256)

    r.set_rgb_call(RgbFg)
    r.set_eightbit_call(RgbBg)

    assert str(r(255, 255, 255)) == "\x1b[38;2;255;255;255m"
    assert str(r(255, 255, 255)) == r.white

    def printout(str1: str, str2: str):
        print("\n" + str1)
       

# Generated at 2022-06-14 08:27:34.620668
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .rendertype import Fg, RgbBg

    # Create a Register object
    rg = Register()

    # Add a render-function for Fg
    rg.set_renderfunc(rendertype=Fg, func=lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m")

    # Add a render-function for RgbBg
    rg.set_renderfunc(rendertype=RgbBg, func=lambda r, g, b: f"\x1b[48;2;{r};{g};{b}m")

    # Create two styles
    rg.style1 = Style(Fg(255, 0, 0))

    rg.style2 = Style(RgbBg(102, 105, 0))

    # Set style1 as rgb-call.

# Generated at 2022-06-14 08:27:44.488820
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    from .ansi import RgbBg, RgbFg

    # Create a test-register with some colors and a test function, that appends
    # a sequence of numbers to a string.
    def test_render_function(*args) -> str:
        return "".join([str(i) for i in args])

    r = Register()
    r.test1 = Style(RgbFg(10, 15, 20))  # type: ignore
    r.test2 = Style(RgbBg(25, 30, 35))  # type: ignore

    r.set_renderfunc(RgbFg, test_render_function)
    r.set_renderfunc(RgbBg, test_render_function)

    # Test rgb-call with RgbFg.

# Generated at 2022-06-14 08:28:02.254483
# Unit test for constructor of class Register
def test_Register():

    r1 = Register()

    assert len(r1.renderfuncs) == 0
    assert r1.is_muted == False

# Generated at 2022-06-14 08:28:13.271511
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .sgr import Bold
    from .sgr import Fg, Bg

    class RegisterB(Register):
        def __init__(self):
            Register.__init__(self)
            setattr(self, "bold_kitkat", Style(Bold(1), Fg(255, 100, 100), Bg(1, 2, 3)))

    r = RegisterB()
    r.set_renderfunc(Fg, lambda x: "Fg: " + str(x))
    r.set_renderfunc(Bg, lambda x: "Bg: " + str(x))
    r.set_renderfunc(Bold, lambda x: "Bold: " + str(x))

    r.mute()

    # Mute results in > ""
    assert r.bold_kitkat == ""

    r.unm

# Generated at 2022-06-14 08:28:17.676387
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    r = Register()
    r.foo = Style(RgbFg(1, 10, 20))
    assert isinstance(getattr(r, "foo"), Style)
    assert str(getattr(r, "foo")) == "\x1b[38;2;1;10;20m"

# Generated at 2022-06-14 08:28:22.737529
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    # Setup
    test_str = "test"

    # Test
    test_register = Register()
    test_register.test_str = test_str

    # Assert
    assert test_register.as_dict() == {"test_str": test_str}

# Generated at 2022-06-14 08:28:33.373807
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    class Test8bit(RenderType):
        type = "Test8bit"
        args = ("n",)

    class TestRgb(RenderType):
        type = "TestRgb"
        args = ("r", "g", "b")

    def _render_8bit(n: int) -> str:
        return f"\x1b[{n}m"

    def _render_rgb(r: int, g: int, b: int) -> str:
        return f"\x1b[{r}, {g}, {b}m"

    r = Register()
    r.set_renderfunc(Test8bit, _render_8bit)
    r.set_renderfunc(TestRgb, _render_rgb)

    r.set_eightbit_call(Test8bit)

# Generated at 2022-06-14 08:28:35.681873
# Unit test for constructor of class Register
def test_Register():

    r1 = Register()
    r2 = Register()

    r1.purple = Style(r1.fg["purple"])
    r2.green = Style(r2.fg["green"])

    assert r1.purple != r2.green


# Generated at 2022-06-14 08:28:45.531062
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertype import RgbFg, RgbBg
    from .ansi import eightbit_to_rgb

    def rgb_fg(r, g, b):
        return "RgbFg {} {} {}".format(r, g, b)

    def rgb_bg(r, g, b):
        return "RgbBg {} {} {}".format(r, g, b)

    reg = Register()
    reg.set_renderfunc(RgbFg, rgb_fg)
    reg.set_renderfunc(RgbBg, rgb_bg)

    assert reg.eightbit_call == rgb_fg
    assert reg.rgb_call == rgb_fg

    reg.set_eightbit_call(RgbFg)
    assert reg.eightbit_call == rgb_fg

    reg.set_eight

# Generated at 2022-06-14 08:28:49.521768
# Unit test for method copy of class Register
def test_Register_copy():

    import pytest

    rs = Register()
    rs.red = Style(rs.Sgr(1))

    rs_copied = rs.copy()
    assert rs_copied is not rs
    assert rs_copied.red is not rs.red
    assert rs_copied.red == rs.red



# Generated at 2022-06-14 08:29:02.765820
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    """
    Test the namedtuple export method of the Register class.
    """
    class MyRegister(Register):
        """
        This is a dummy class for the unit test.
        """
        blue = Style(RgbFg(5,5,5))

    # Use class with MyRegister
    class MyClass:
        """
        This is a dummy class. It uses an instance of MyRegister.
        """

        def __init__(self):
            self.my_register = MyRegister()
            self.my_register.blue = Style(RgbFg(1,2,3))

    # Create a new instance of MyClass
    obj = MyClass()

    # Register a new renderfunc for RgbFg
    def func(r, g, b):
        return "I am a function"


# Generated at 2022-06-14 08:29:10.160487
# Unit test for method unmute of class Register
def test_Register_unmute():
    # Set up
    class ThreeByteARenderType(RenderType):
        args = (int, int, int)

    renderfuncs: Renderfuncs = {
        ThreeByteARenderType: lambda r, g, b: f"{r}{g}{b}",
    }
    # ---------

    register = Register()
    register.renderfuncs = renderfuncs
    setattr(register, "a", Style(ThreeByteARenderType(1, 2, 3)))
    setattr(register, "b", Style(ThreeByteARenderType(4, 5, 6)))
    register.mute()
    register.unmute()

    assert register.a == "123"
    assert register.b == "456"

# Generated at 2022-06-14 08:29:33.278977
# Unit test for constructor of class Register
def test_Register():

    r = Register()
    attr = "Haha"
    color = Style(rgb_fg="DuDu")

    r.__setattr__(attr, color)
    assert getattr(r, attr) == color

# Generated at 2022-06-14 08:29:40.874062
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    import sty

    class TmpRegister(Register):
        pass

    register = TmpRegister()

    register.foo = Style("\x1b[48;2;1;5;10m", "foo")
    register.bar = Style("\x1b[48;2;1;5;11m", "bar")

    t = register.as_namedtuple()

    assert t.foo == register.foo
    assert t.bar == register.bar



# Generated at 2022-06-14 08:29:54.032490
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    from .rendertype import RgbBg
    from .sty import Sty

    sty = Sty({"fg": {"red": Style(RgbFg(10, 20, 30))}})
    d = sty.fg.as_dict()
    dt = sty.fg.as_namedtuple()

    assert d["red"] == "\x1b[38;2;10;20;30m"
    assert dt["red"] == "\x1b[38;2;10;20;30m"

    sty.fg.red = Style(RgbBg(100, 200, 300))
    d = sty.fg.as_dict()
    dt = sty.fg.as_namedtuple()

    assert d["red"] == "\x1b[48;2;100;200;300m"

# Generated at 2022-06-14 08:30:02.185891
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    import sty

    import random
    import string
    import sys

    random_string = "".join(random.choice(string.ascii_letters) for i in range(15))

    class Test1(RenderType):
        pass
    class Test2(RenderType):
        pass

    def my_func(args1, args2) -> str:
        return f"{args1}{args2}"

    def my_func2(args1, args2) -> str:
        return f"{args1}{args2}"

    t = Register()
    t.set_renderfunc(Test1, my_func)
    t.set_renderfunc(Test2, my_func2)

    # Test if renderfuncs are set right.
    assert t.renderfuncs[Test1] == my_func
    assert t.renderfun

# Generated at 2022-06-14 08:30:10.794816
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .rendertype import RgbFg, Sgr
    from .register import Register

    reg = Register()
    reg.set_renderfunc(RgbFg, lambda r, g, b: f"{r}-{g}-{b}")
    reg.red = Style(RgbFg(1,2,3), Sgr(1))

    assert reg.red == "1-2-3\x1b[1m"


# Generated at 2022-06-14 08:30:20.949776
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    reg = Register()
    assert isinstance(reg.as_dict(), dict)
    t = type("reg", (Register,), {})
    t.__init__ = lambda x: None

    assert isinstance(t().as_dict(), dict)

    # set some attrs
    setattr(reg, "foo", "foo")
    setattr(reg, "bar", "bar")
    setattr(reg, "baz", "baz")

    # set some styles
    setattr(reg, "foo_", Style("foo", RgbFg(1, 1, 1)))
    setattr(reg, "bar_", Style("bar", RgbBg(2, 2, 2)))

# Generated at 2022-06-14 08:30:34.548232
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    class Test(Register):
        a = Style(RgbFg(255,0,0))
        b = Style(RgbBg(0,255,0))
        c = Style(RgbEf(0,0,255))
        d = Style(RgbFg(255,0,0), RgbBg(0,255,0))

    r = Test()

# Generated at 2022-06-14 08:30:45.006656
# Unit test for method mute of class Register
def test_Register_mute():
    from .rules import RgbEf, Sgr

    rgf_ef_red = RgbEf(255, 0, 0)
    sgr_bold = Sgr(1)
    style_red_bold = Style(rgf_ef_red, sgr_bold)

    r: Register = Register()
    r.red = style_red_bold

    assert isinstance(r.red, Style)
    assert str(r.red) == "\x1b[38;2;255;0;0m\x1b[1m"

    r.mute()
    assert isinstance(r.red, Style)
    assert str(r.red) == ""

    r.unmute()
    assert isinstance(r.red, Style)
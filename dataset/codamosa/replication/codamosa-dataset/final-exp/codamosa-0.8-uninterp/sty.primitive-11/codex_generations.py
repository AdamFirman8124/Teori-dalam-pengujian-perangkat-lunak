

# Generated at 2022-06-14 08:21:04.221772
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    import pytest

    class RgbStyle(NamedTuple):
        red: str
        green: str
        blue: str

    r = Register()
    r.red = Style(RgbFg(255, 0, 0))
    r.green = Style(RgbFg(0, 255, 0))
    r.blue = Style(RgbFg(0, 0, 255))

    named_tuple = r.as_namedtuple()

    assert isinstance(named_tuple, RgbStyle)
    assert named_tuple.red == "\x1b[38;2;255;0;0m"
    assert named_tuple.green == "\x1b[38;2;0;255;0m"

# Generated at 2022-06-14 08:21:05.504320
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    pass



# Generated at 2022-06-14 08:21:18.268541
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class RgbBg(RenderType):
        def __init__(self, r: int, g: int, b: int) -> None:
            self.args = (r, g, b)

        def __int__(self) -> int:
            return 1

    def rgb_bg_renderfunc(r: int, g: int, b: int) -> str:
        return f"\x1b[48;2;{r};{g};{b}m"

    r = Register()
    r.set_renderfunc(RgbBg, rgb_bg_renderfunc)
    r.set_rgb_call(RgbBg)

    # Test with existing names
    assert r(3, 2, 1) == "\x1b[48;2;3;2;1m"


# Generated at 2022-06-14 08:21:31.586861
# Unit test for constructor of class Style
def test_Style():
    # Test constructor for class `Style`
    s = Style(41)
    assert str(s) == "\x1b[41m"
    assert s.rules == (41,)

    s = Style(41, 1)
    assert str(s) == "\x1b[41;1m"
    assert s.rules == (41, 1)

    s = Style(41, 1, s)
    assert str(s) == "\x1b[41;1m"
    assert s.rules == (41, 1, s)

    s2 = Style(42, 1)
    assert str(s2) == "\x1b[42;1m"
    assert s2.rules == (42, 1)

    s3 = Style(s2, 44, 1)

# Generated at 2022-06-14 08:21:43.314350
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    # Creating some test objects
    rt1 = RenderType("Test1")
    rt2 = RenderType("Test2")
    rt3 = RenderType("Test3")
    rt4 = RenderType("Test4")

    # Used later in the test to check if the register-objects hold the correct
    # attributes.

# Generated at 2022-06-14 08:21:46.763233
# Unit test for method copy of class Register
def test_Register_copy():
    r = Register()
    r.foo = Style(value="foo")
    r_copy = r.copy()
    assert r_copy.foo == "foo"

# Generated at 2022-06-14 08:21:53.512980
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    reg = Register()
    reg.color1 = Style(RgbFg(1, 1, 1))
    reg.color2 = Style(RgbFg(2, 2, 2))
    reg.color3 = Style(RgbFg(3, 3, 3))

    assert reg.as_namedtuple().color1 == str(reg.color1)
    assert reg.as_namedtuple().color2 == str(reg.color2)
    assert reg.as_namedtuple().color3 == str(reg.color3)

# Generated at 2022-06-14 08:22:07.402042
# Unit test for method __call__ of class Register
def test_Register___call__():
    class RgbFg(RenderType):
        """
        Render rule for foreground color.
        """
        ANSI_CODE = "fg"
        STREAM = "stdout"
    class RgbBg(RenderType):
        """
        Render rule for background color.
        """
        ANSI_CODE = "bg"
        STREAM = "stdout"
    def _render_fg(r, g, b):
        return "fg", r, g, b
    def _render_bg(r, g, b):
        return "bg", r, g, b
    fg = Register()
    fg.set_eightbit_call(RgbFg)
    fg.set_rgb_call(RgbFg)

# Generated at 2022-06-14 08:22:13.204544
# Unit test for method __call__ of class Register
def test_Register___call__():

    class TestRegister(Register):
        blue = Style(SgrFg(4))
        red = Style(SgrFg(1))

    r1 = TestRegister()
    assert r1(4) == r1.blue
    assert r1(1) == r1.red
    assert r1("blue") == r1.blue
    assert r1("red") == r1.red
    assert r1(2) == ""



# Generated at 2022-06-14 08:22:24.493022
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    # Test 1: Assign an attribute to register-object
    fg = Register()
    fg.black = Style(1)
    assert getattr(fg, "black") == Style(1)

    # Test 2: Assign a style (style is a subclass of str) to register-object
    fg.black = Style(1)
    fg.black_bold = Style(fg.black, 2)
    assert getattr(fg, "black_bold") == Style(1, 2)
    assert isinstance(getattr(fg, "black_bold"), Style)
    assert isinstance(getattr(fg, "black_bold"), str)

    # Test 3: NameError for wrong assignment
    fg = Register()

# Generated at 2022-06-14 08:22:32.385952
# Unit test for constructor of class Register
def test_Register():
    """
    This function tests the constructor of class Register.
    """

    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False

# Generated at 2022-06-14 08:22:37.039887
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    """
    Unit test for method set_eightbit_call of class Register.
    """
    from .sgr import Sgr

    r: Register = Register()
    r.set_renderfunc(Sgr, lambda *args: "@" + "".join([str(x) for x in args]) + "@")
    r.set_eightbit_call(Sgr)
    res = r(10)
    assert res == "@10@"

# Generated at 2022-06-14 08:22:47.253667
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    # Prepare register object.
    register = Register()
    register.bold = Style(Sgr(1))
    register.fg_red = Style(RgbFg(255, 0, 0))
    register.bg_blue = Style(RgbBg(0, 0, 255))
    register.bg_blue_bold = Style(RgbBg(0, 0, 255), Sgr(1))

    # Make sure that cls is returned.
    StyleRegister = register.as_namedtuple()
    assert type(StyleRegister) == namedtuple
    assert type(StyleRegister.bold) == str
    assert type(StyleRegister.fg_red) == str
    assert type(StyleRegister.bg_blue) == str
    assert type(StyleRegister.bg_blue_bold) == str

    # Make sure that values are correct.
   

# Generated at 2022-06-14 08:23:00.127383
# Unit test for method unmute of class Register
def test_Register_unmute():
    """
    With sty you can mute() a register-object, so that it dosn't render
    the ANSI-codes anymore. After muting them some new rules are set. This
    method tests if this new rules are rendered.
    """

    # Create a register
    register = Register()

    # Register as mutable and then unmute it
    register.mute()
    register.unmute()

    # Create a new Style
    reset_style = Style("reset")

    # Set the new style as an attribute of the register
    register.reset = reset_style

    # Assure style is rendered
    assert str(register.reset) == "reset"

    # Register a new renderfunc for the reset-style
    register.set_renderfunc(type("Reset"), lambda: "42")

    # Assert style is again rendered

# Generated at 2022-06-14 08:23:04.977928
# Unit test for method copy of class Register
def test_Register_copy():

    r1 = Register()
    r2 = r1.copy()

    assert r1 is not r2
    assert r1.__dict__ == r2.__dict__
    assert r1.renderfuncs == r2.renderfuncs

# Generated at 2022-06-14 08:23:17.751481
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    def func(value):
        return value

    r = Register()

    # Test if Style attribute is only assigned if a Style-object
    # is given as value.
    with pytest.raises(ValueError):
        r.test = "Not a Style object"

    # Test if a Style-object is assigned if a Style-object is given
    # as value.
    value = Style(RgbFg(50, 100, 200))
    r.test1 = value
    assert getattr(r, "test1") == value

    # Test if object is muted if object is muted.
    r.is_muted = True
    value = Style(RgbFg(50, 100, 200))

    r.test2 = value
    assert getattr(r, "test2") == Style(*value.rules, value="")

# Generated at 2022-06-14 08:23:24.532642
# Unit test for method __call__ of class Register
def test_Register___call__():

    register = Register()
    register.set_eightbit_call(RenderType)

    for i in range(0, 256):
        assert register(i) == f"\x1b[38;5;{i}m"

    for i in range(0, 256):
        assert register(i, bold=True) == f"\x1b[38;5;{i};1m"

# Generated at 2022-06-14 08:23:34.494084
# Unit test for method mute of class Register
def test_Register_mute():
    """
    Unit test for method Register.mute().
    """

    register = Register()
    register.set_eightbit_call(RenderType)
    register.set_rgb_call(RenderType)

    register.red = Style(RenderType(1, 2, 3))
    register.green = Style(RenderType(4, 5, 6))
    register.blue = Style(RenderType(7, 8, 9))

    # Mute register
    register.mute()

    # Check that all attributes are set and render to ''
    assert register.red == ""
    assert register.green == ""
    assert register.blue == ""
    assert register(1) == ""
    assert register(2, 1, 5) == ""

    # Unmute register
    register.unmute()

    # Check that all attributes are set and render

# Generated at 2022-06-14 08:23:40.175798
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertype import EightBit, Rgb

    fg = Register()

    fg.set_eightbit_call(rendertype=EightBit)
    fg.set_rgb_call(rendertype=Rgb)

    assert fg(5) == ""
    assert fg(5, 7, 8) == ""



# Generated at 2022-06-14 08:23:51.430247
# Unit test for method mute of class Register
def test_Register_mute():

    class TestRegister(Register):
        pass

    test_register = TestRegister()

    test_register.test = Style(rendertype_1=1, rendertype_2=2)
    test_register.test_2 = Style(
        test_register.test, rendertype_3=3, rendertype_4=4
    )
    test_register.set_renderfunc(RenderType, lambda x: str(x))

    test_register.mute()

    assert test_register.test == ""
    assert test_register.test_2 == ""

    test_register.unmute()
    assert test_register.test == "12"
    assert test_register.test_2 == "1234"



# Generated at 2022-06-14 08:24:03.779119
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class MyRegister(Register):
        def __init__(self):
            super().__init__()
            self.renderfuncs = {
                type: lambda: ""
                for type in [
                    RenderType,
                    Style,
                ]
            }

    r = MyRegister()

    r.test1 = Style(RenderType(16))
    r.test2 = Style(Style(RenderType(16)))

    assert r.test1 == "\x1b[16m"
    assert r.test2 == "\x1b[16m"

# Generated at 2022-06-14 08:24:16.017226
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    msg = "sty: test_Register_set_renderfunc() - "

    r = Register()

    r.set_renderfunc(rendertype=Sgr, func=lambda x: f"\x1b[{x}m")

    r.dim = Style(Sgr(2))
    r.dim_bold = Style(Sgr(2), Sgr(1))

    assert r.dim == "\x1b[2m"
    assert r.dim_bold == "\x1b[2m\x1b[1m"

    r.set_renderfunc(rendertype=Sgr, func=lambda x: f"*{x}*")

    assert r.dim == "*2*"
    assert r.dim_bold == "*2**1*"

    print(msg, "it works.")

# Generated at 2022-06-14 08:24:20.484263
# Unit test for method __new__ of class Style
def test_Style___new__():

    from .rendertype import Sgr

    s = Style(Sgr(1), Sgr(2))

    assert isinstance(s, str)
    assert s == "\x1b[1m\x1b[2m"
    assert isinstance(s, Style)

# Generated at 2022-06-14 08:24:24.387211
# Unit test for method __new__ of class Style
def test_Style___new__():
    sty = Style()

    assert sty == ""
    assert not sty
    assert sty.rules is None

    sty = Style()

    assert sty == ""
    assert not sty
    assert sty.rules is None

# Generated at 2022-06-14 08:24:36.620066
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    def render(r, g, b, *args, **kwargs):
        return "({},{},{})".format(r, g, b)

    def render_eightbit(color, *args, **kwargs):
        return "({})".format(color)

    r = Register()
    r.set_renderfunc(RgbFg, render)

    r.set_eightbit_call(EightbitFg)
    r.set_eightbit_call(EightBitFg)
    """
    TODO: check why this does not work:
    r.set_eightbit_call(EightBitFg)
    """

    r.set_eightbit_call(EightBitFg)
    r.set_renderfunc(EightbitFg, render_eightbit)

# Generated at 2022-06-14 08:24:50.527513
# Unit test for method copy of class Register
def test_Register_copy():

    # Create new TestClass as a subclass of Register.
    # The class attributes will be copied later.
    class TestClass(Register):
        pass

    r1 = TestClass()
    r1.test = Style("test")  # Create attribute test with some styling

    r2 = r1.copy()  # r2 is a deepcopy of r1

    # Check if r2 has the same attributes as r1 and if their type is the same.
    for name, attr in vars(r1).items():

        assert(hasattr(r2, name))

        assert(type(attr) is type(getattr(r2, name)))

    # Check if r2 has the same functions as r1 and if their type is the same.
    for name in dir(r1):

        assert (hasattr(r2, name))


# Generated at 2022-06-14 08:24:56.302701
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    """
    Unit test for method as_namedtuple of class Register.
    """
    r = Register()
    r.test = Style(RgbFg(10, 20, 30))
    r.test2 = Style(RgbFg(40, 50, 60))

    t: NamedTuple = r.as_namedtuple()
    assert t.test == r.test
    assert t.test2 == r.test2

# Generated at 2022-06-14 08:25:06.322211
# Unit test for method copy of class Register
def test_Register_copy():

    # Create a new register-object.
    r1: Register = Register()

    # Fill it with some dummy data.
    r1.test1 = Style("1")
    r1.test2 = Style("2")

    # Make a copy of r1.
    copy: Register = r1.copy()

    # Check if copy is equal to r1.
    assert copy.test1 == r1.test1
    assert copy.test2 == r1.test2
    assert copy.is_muted == r1.is_muted
    assert copy.renderfuncs == r1.renderfuncs
    assert copy.eightbit_call == r1.eightbit_call
    assert copy.rgb_call == r1.rgb_call

# Generated at 2022-06-14 08:25:08.557224
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .register import fg

    assert type(fg.as_namedtuple()) == type(fg.as_namedtuple())



# Generated at 2022-06-14 08:25:15.939335
# Unit test for method unmute of class Register
def test_Register_unmute():

    class MyRegister(Register):
        muted_fg_blue = Style(RgbFg(0, 0, 255))

        unmuted_fg_red = Style(RgbFg(255, 0, 0))

    inst = MyRegister()
    inst.mute()

    assert inst.muted_fg_blue == ""
    assert inst.unmuted_fg_red == ""

    inst.unmute()

    assert inst.muted_fg_blue == "\x1b[38;2;0;0;255m"
    assert inst.unmuted_fg_red == "\x1b[38;2;255;0;0m"


# Generated at 2022-06-14 08:25:38.961272
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class RgbFg(RenderType):
        def __init__(self, r, g, b):
            self.args = (r, g, b)

    class RgbBg(RenderType):
        def __init__(self, r, g, b):
            self.args = (r, g, b)

    def _rgb_fg(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    def _rgb_bg(r: int, g: int, b: int) -> str:
        return f"\x1b[48;2;{r};{g};{b}m"

    reg = Register()

# Generated at 2022-06-14 08:25:47.823998
# Unit test for method mute of class Register
def test_Register_mute():

    class MockRegister(Register):
        pass

    mockreg = MockRegister()

    rt = namedtuple("RenderType", ["args"])

    # Mock function 1
    def mockfunc1(arg1: str):
        return f"<{arg1}>"  # returns '<foo>'

    # Mock function 2
    def mockfunc2(arg1: str, arg2: str):
        return f"*{arg1}:{arg2}*"  # returns '*foo:bar*'

    # Mock function 3
    def mockfunc3(arg1: int, arg2: int, arg3: int):
        return f"[{arg1} {arg2} {arg3}]"  # returns '[1 2 3]'

    # Add mock render functions to mock register

# Generated at 2022-06-14 08:25:57.120718
# Unit test for constructor of class Style
def test_Style():

    from .rendertype import RgbBg, Sgr

    rgb_bg = Style(RgbBg(1,2,3))
    sgr = Style(Sgr(1,2,3))

    assert isinstance(rgb_bg, Style)
    assert isinstance(sgr, Style)

    assert isinstance(rgb_bg, str)
    assert isinstance(sgr, str)

    assert rgb_bg == "\x1b[48;2;1;2;3m"
    assert sgr == "\x1b[1;2;3m"


# Generated at 2022-06-14 08:26:04.055747
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .rendertype import RgbFg

    r = Register()
    r.new_style = Style(RgbFg(1,2,3))
    assert r.new_style == "\x1b[38;2;1;2;3m"

    r.new_style = Style(RgbFg(4,5,6))
    assert r.new_style == "\x1b[38;2;4;5;6m"

    del r.new_style


# Generated at 2022-06-14 08:26:06.341623
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    r = Register()

    r.set_eightbit_call(RgbFg)

    assert r.eightbit_call(42) == "\x1b[38;2;42;42;42m"



# Generated at 2022-06-14 08:26:17.935439
# Unit test for method copy of class Register
def test_Register_copy():
    reg = Register()
    reg.foo = Style(value="bar")
    reg.bar = Style(value="foo")

    reg2 = reg.copy()

    # Check if deepcopy was made.
    assert reg != reg2

    # Check if copy worked while maintaining references.
    assert reg.foo == reg2.foo
    assert reg.bar == reg2.bar

    # Check if attributes were copied.
    assert hasattr(reg, "foo")
    assert hasattr(reg, "bar")
    assert hasattr(reg2, "foo")
    assert hasattr(reg2, "bar")

    # Check if attributes have the same type.
    assert isinstance(reg.foo, Style)
    assert isinstance(reg.bar, Style)
    assert isinstance(reg2.foo, Style)

# Generated at 2022-06-14 08:26:23.024366
# Unit test for method copy of class Register
def test_Register_copy():
    test = Register()
    test.reset = Style(RenderType())
    test.test = Style(RenderType())
    cop = test.copy()
    assert test.reset == cop.reset
    assert test.test == cop.test
#

# Generated at 2022-06-14 08:26:35.509039
# Unit test for method copy of class Register
def test_Register_copy():
    from . import rendertype
    from .register import Register
    from .utils import print_colors

    rgb = Register()
    rgb.set_renderfunc(rendertype.RgbFg, lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m")
    rgb.red = Style(rgb.RgbFg(255, 0, 0))

    assert rgb.red == rgb.red
    # import pdb; pdb.set_trace()
    rgb2 = rgb.copy()
    assert rgb.red == rgb2.red
    print_colors(rgb)
    print()
    print_colors(rgb2)

    # Check if render-functions are the same

# Generated at 2022-06-14 08:26:48.406586
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class RedRenderType(RenderType):
        name = "red"
        ansi = "\x1b[31m"

    class Renderfunc1(RenderType):
        name = "renderfunc1"
        ansi = "**"

    class Renderfunc2(RenderType):
        name = "renderfunc2"
        ansi = "***"

    rf1 = Renderfunc1()
    rf2 = Renderfunc2()
    rs = RedRenderType()
    r = Register()

    r.set_renderfunc(Renderfunc1, lambda x: Renderfunc1.ansi)
    r.set_renderfunc(Renderfunc2, lambda x: Renderfunc2.ansi)
    r.set_renderfunc(RedRenderType, lambda x: RedRenderType.ansi)


# Generated at 2022-06-14 08:26:51.622547
# Unit test for method unmute of class Register
def test_Register_unmute():
    import sty
    r1 = sty.Register()
    r1.a = sty.Style(sty.fg.red)
    r1.mute()
    assert r1.a == ""
    r1.unmute()
    assert r1.a != ""

# Generated at 2022-06-14 08:27:16.452529
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    r1 = Register()
    r1.test1 = "abc"
    r1.test2 = "def"
    assert r1.as_dict() == {"test1": "abc", "test2": "def"}
    assert r1.as_namedtuple() == r1.as_namedtuple()


# Generated at 2022-06-14 08:27:24.670959
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    """
    Test method as_namedtuple of class Register.
    """
    reg = Register()
    setattr(reg, "foo", Style())
    setattr(reg, "bar", Style())
    as_nt = reg.as_namedtuple()
    assert hasattr(as_nt, "foo")
    assert hasattr(as_nt, "bar")
    assert not hasattr(as_nt, "as_namedtuple")
    assert not hasattr(as_nt, "set_renderfunc")
    assert not hasattr(as_nt, "set_eightbit_call")
    assert not hasattr(as_nt, "set_rgb_call")
    assert not hasattr(as_nt, "as_dict")
    assert not hasattr(as_nt, "mute")

# Generated at 2022-06-14 08:27:28.108747
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    from .rendertype import NoOp

    # Configure Renderfuncs for testing.
    f1: Callable = lambda *args: ""
    f2: Callable = lambda *args: ""

    renderfuncs: Renderfuncs = {
        NoOp: f1
    }

    register = Register()
    register.set_renderfunc(NoOp, f2)
    assert(register.renderfuncs[NoOp] == f2)

    # Revert Renderfuncs to normal.
    renderfuncs: Renderfuncs = {
        NoOp: NoOp.render
    }

# Generated at 2022-06-14 08:27:38.749363
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .graphics import G0, G1
    from .rendertype import make_text_rendertype, RenderType
    from . import fg, bg, ef, rs

    def int_to_ansi(i: int) -> str:
        res_func = lambda n: f"\x1b[4{n}m" + "\N{EM SPACE}"
        return res_func(i)

    def str_to_ansi(s: str) -> str:
        res_func = lambda s: f"\x1b[4{s}m" + "\N{EM SPACE}"
        return res_func(s)

    def make_rendertype(s: str) -> RenderType:
        def wrapper(*args):
            return (int(s) - 1, )


# Generated at 2022-06-14 08:27:44.444942
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .definition import fg

    def new_func(r, g, b):
        return (r, g, b, "test")

    fg.set_rgb_call(RenderType.RgbFg, new_func)
    assert fg(2, 3, 4) == (2, 3, 4, "test")

# Generated at 2022-06-14 08:27:56.071109
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # Receive RGB-style string with RgbBg render type
    r = Register()

    r.renderfuncs.update({RgbBg: lambda x, y, z: "rgb(" + str(x) + "," + str(y) + "," + str(z) + ")"})
    r.test = Style(RgbBg(1, 5, 10))
    r.set_rgb_call(RgbBg)

    assert r(1, 5, 10) == r.test  # Test for style-attribute

    # Receive RGB-style string with RgbFg render type
    r = Register()


# Generated at 2022-06-14 08:28:09.577828
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class CustomRenderType(RenderType):
        pass

    class CustomStyle(Style):
        pass

    class CustomRegister(Register):
        pass

    def render_func(string):
        return string

    # Create register object
    r = CustomRegister()

    # Add renderfunc renderfunc to register
    r.set_renderfunc(CustomRenderType, render_func)

    # Create StylingRule
    rule1 = CustomRenderType("rule1")

    # Create custom Style object
    style1 = CustomStyle(rule1)

    # Set attr 'style'. Calling __setattr__.
    setattr(r, "style1", style1)

    assert str(getattr(r, "style1")) == "rule1"


if __name__ == "__main__":
    test_Register___setattr__()

# Generated at 2022-06-14 08:28:12.940632
# Unit test for method copy of class Register
def test_Register_copy():
    r = Register()

    r.test0 = Style('foo')
    r.test1 = Style('bar')

    r_copy = r.copy()

    assert r_copy.test0 == r.test0
    assert r_copy.test1 == r.test1

# Generated at 2022-06-14 08:28:18.933469
# Unit test for method __new__ of class Style
def test_Style___new__():

    from .rendertype import RgbFg, Sgr

    r1 = Style(RgbFg(1, 5, 10), Sgr(1))
    assert isinstance(r1, Style)
    assert isinstance(r1, str)
    assert str(r1) == "\x1b[38;2;1;5;10m\x1b[1m"

# Generated at 2022-06-14 08:28:24.099665
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    register = Register()
    register.set_renderfunc(RenderType.eightbit_fg, lambda x: x)
    register.set_eightbit_call(RenderType.eightbit_fg)
    result = register(33)
    assert result == "33"



# Generated at 2022-06-14 08:29:46.690011
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .render import Sty

    def func(*args):
        return "".join((el + ";" for el in args))[:-1]

    fg = Sty().fg
    fg.mute()
    fg.set_renderfunc(RenderType, func)
    fg.unmute()
    assert str(fg.black) == ""
    assert fg.black == ""

# Generated at 2022-06-14 08:29:51.746692
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    import pytest
    from .rendertype import Sgr

    # Create test register with test attribute
    fg = Register()
    fg.test = Style(Sgr(1))

    # Check for correct export
    assert fg.as_dict() == {'test': "\x1b[1m"}


# Generated at 2022-06-14 08:30:00.987917
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class R1(RenderType):
        """
        Just a dummy render type.
        """
        @staticmethod
        def render(*arg):
            return "R1"

    class R2(RenderType):
        """
        Just a dummy render type.
        """
        @staticmethod
        def render(*arg):
            return "R2"

    r = Register()

    # Default:
    assert r.eightbit_call(100, 200) == ""  # type: ignore
    assert r.rgb_call(10, 20, 30) == ""  # type: ignore

    # Set eightbit call to R1.
    r.set_eightbit_call(R1)
    assert r.eightbit_call(100, 200) == "R1"  # type: ignore

# Generated at 2022-06-14 08:30:06.200142
# Unit test for constructor of class Style
def test_Style():
    from . import ef, bg

    style = Style(ef.underline, bg.blue, bg.white)
    assert style.rules == (ef.underline, bg.blue, bg.white)
    assert isinstance(style, Style)
    assert isinstance(style, str)



# Generated at 2022-06-14 08:30:11.979857
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class TestRegister(Register):
        pass

    test_register = TestRegister()
    test_register.set_rgb_call(RgbFg)

    assert test_register.rgb_call(11, 22, 33) == "\x1b[38;2;11;22;33m"

# Generated at 2022-06-14 08:30:21.420309
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    from .sgr import Sgr
    from .rgb import RgbFg, RgbBg
    from .truecolor import TrueColorFg, TrueColorBg

    # Create a register
    r = Register()

    # Create & set the renderfuncs for the register

    def sgr_renderfunc(*args):
        return '\x1b[{}m'.format(*args)

    def rgb_renderfunc(*args):
        return '\x1b[{};2;{};{};{}m'.format(args[0], args[1], args[2], args[3])

    def truecolor_renderfunc(*args):
        return '\x1b[{};2;{};{};{}m'.format(args[0], args[1], args[2], args[3])

    r.set_render

# Generated at 2022-06-14 08:30:34.927311
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class MyTestRenderType(RenderType):
        pass

    class MyRegister(Register):
        pass

    r = MyRegister()

    # Create styles
    r.black = Style(MyTestRenderType(0))
    r.red = Style(MyTestRenderType(1))

    # Register should contain only one renderfunc.
    assert len(r.renderfuncs) == 1

    # The renderfunc should return "The renderfunc was called with {0}".format(args[0])
    def f(x):
        return "The renderfunc was called with {0}".format(x)

    # Replace renderfunc
    r.set_renderfunc(MyTestRenderType, f)

    # Register should contain only one renderfunc.
    assert len(r.renderfuncs) == 1

    # The register should be muted and all styles should have

# Generated at 2022-06-14 08:30:45.203930
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    import attr
    from .rendertype import RenderType, Sgr, RgbFg, RgbBg

    rt1 = Sgr(1)
    rt2 = RgbFg(1, 2, 3)
    rt3 = RgbBg(2, 3, 4)

    r = Register()
    r.set_renderfunc(rt1, lambda x: f"mock_sgr({x})")
    r.set_renderfunc(rt2, lambda x, y, z: f"mock_rgbfg({x}, {y}, {z})")
    r.set_renderfunc(rt3, lambda x, y, z: f"mock_rgbbg({x}, {y}, {z})")

    r.x = Style(rt1, rt2)
    r.y = Style